#!/usr/bin/env python3
# v4
"""
Fetch Cisco UCS documentation pages and convert to Markdown.

For each URL in urls.md:
  - HTML  → crawl all sub-pages, combine into one .md file in ./ucs-docs/
  - PDF   → extract text, save as .md in ./ucs-docs/
  - JSON  → render as table/list, save as .md in ./ucs-docs/
  - other → wrap raw text in a fenced block, save as .md in ./ucs-docs/

Raw downloads are cached in ./ucs-docs-raw/{html,pdf,json,other}/
Files already fetched in the last 24 hours are skipped unless --force is set.

Markdown filenames:
  - Cisco HTML guides  → derived from the page <title>
  - intersight.com/…/saas/<section>/<topic>      → intersight-saas-<section>_<topic>.md
  - intersight.com/…/appliance/<section>/<topic> → intersight-appliance-<section>_<topic>.md
  - intersight.com (other paths) → intersight-<url-slug>.md

Intersight URLs are JavaScript-rendered SPAs.  This script fetches them by:
  1. Loading the Intersight home page to find the CDN base-bundle.js URL.
  2. Downloading base-bundle.js and scanning for the versioned CDN doc URL.
  3. Falling back to reading the CDN version directly from the help page HTML.
  4. Fetching the static CDN HTML doc page (no JS needed) and converting to MD.

Dependencies:
    pip install requests beautifulsoup4 html2text pdfminer.six markdownify
"""

import io
import json
import os
import re
import time
import datetime
import email.utils
import traceback
import requests
from collections import OrderedDict
from pathlib import Path
from urllib.parse import urljoin, urlparse, unquote

import html2text
from bs4 import BeautifulSoup

from json_to_markdown import (
    value_to_markdown as json_to_md,
    try_load_json,
)

try:
    from pdfminer.high_level import extract_text as pdf_extract_text
    _PDF_OK = True
except ImportError:
    _PDF_OK = False
    def pdf_extract_text(*a, **kw) -> str:  # type: ignore[misc]
        return ""

try:
    from markdownify import markdownify as _markdownify
    _MARKDOWNIFY_OK = True
except ImportError:
    _MARKDOWNIFY_OK = False


# ---------------------------------------------------------------------------
# Directory layout
# ---------------------------------------------------------------------------
RAW_HTML_DIR  = Path('./ucs-docs-raw/html')

# ---------------------------------------------------------------------------
# Intersight CDN constants
# ---------------------------------------------------------------------------
_INTERSIGHT_HOME    = 'https://intersight.com'
_INTERSIGHT_CDN_BASE = 'https://cdn.intersight.com/components/an-hulk'
RAW_PDF_DIR   = Path('./ucs-docs-raw/pdf')
RAW_JSON_DIR  = Path('./ucs-docs-raw/json')
RAW_OTHER_DIR = Path('./ucs-docs-raw/other')
MD_OUT_DIR    = Path('./ucs-docs')

# Map file extensions → content category.  No extension → treated as html.
EXT_MAP = {
    '.html': 'html', '.htm': 'html', '.xhtml': 'html', '.shtml': 'html',
    '.pdf':  'pdf',
    '.json': 'json',
}

CACHE_TTL = datetime.timedelta(hours=24)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _url_slug(url: str) -> str:
    """Return the last non-empty path segment of a URL, URL-decoded."""
    path = unquote(urlparse(url).path).rstrip('/')
    segment = os.path.basename(path)
    if segment and not segment.startswith('.'):
        return segment
    # Fallback: flatten the whole path into a safe filename
    flat = re.sub(r'[^a-zA-Z0-9._-]', '_', path.strip('/'))
    return flat[:200] or 'index'


def _content_type(url: str) -> str:
    """Classify a URL as 'html', 'pdf', 'json', or 'other'."""
    _, ext = os.path.splitext(urlparse(url).path.rstrip('/'))
    if not ext:
        return 'html'
    return EXT_MAP.get(ext.lower(), 'other')


def _raw_dir(content_type: str) -> Path:
    return {
        'html':  RAW_HTML_DIR,
        'pdf':   RAW_PDF_DIR,
        'json':  RAW_JSON_DIR,
        'other': RAW_OTHER_DIR,
    }[content_type]


def _title_to_filename(title: str) -> str:
    """'Cisco UCS Manager Storage Guide, 4.3' → 'Cisco-UCS-Manager-Storage-Guide-4.3.md'"""
    safe = re.sub(r'[<>:"/\\|?*]', '', title)       # strip illegal chars
    safe = re.sub(r'[\s,]+', '-', safe.strip())       # spaces/commas → hyphens
    safe = re.sub(r'-{2,}', '-', safe).strip('-')     # collapse repeated hyphens
    return (safe[:200] or 'document') + '.md'


def _intersight_prefix(url: str) -> str:
    """Return 'intersight-saas-', 'intersight-appliance-', or 'intersight-'."""
    path = urlparse(url).path
    if '/saas/' in path:
        return 'intersight-saas-'
    if '/appliance/' in path:
        return 'intersight-appliance-'
    return 'intersight-'


def _raw_html_name(url: str) -> str:
    """Return the filename used to cache an HTML page on disk.

    Always ends in '.html'.  Intersight pages are also prefixed
    (e.g. 'intersight-saas-server_policies.html') so they are clearly
    separated from Cisco guide pages in the raw cache.
    """
    slug = _url_slug(url)
    if not os.path.splitext(slug)[1]:   # no extension → add .html
        slug += '.html'
    if url.startswith('https://intersight.com'):
        return _intersight_prefix(url) + slug
    return slug


def _raw_name(url: str, ctype: str) -> str:
    """Return the cache filename for *url*, guaranteed to have the correct suffix.

    - html  → via _raw_html_name (handles Intersight prefix + .html)
    - pdf   → <slug>.pdf
    - json  → <slug>.json
    - other → <slug> unchanged (extension from URL, if any)
    """
    if ctype == 'html':
        return _raw_html_name(url)
    slug = _url_slug(url)
    required = {'pdf': '.pdf', 'json': '.json'}.get(ctype, '')
    if required and not slug.lower().endswith(required):
        slug += required
    return slug


def _md_header(url: str) -> str:
    return (
        f"# Documentation: {url}\n\n"
        f"*Fetched on: {time.strftime('%Y-%m-%d %H:%M:%S')}*\n\n"
        "---\n\n"
    )


def _is_fresh(path: Path) -> tuple[bool, str]:
    """Return (True, reason) if the file exists and is younger than CACHE_TTL."""
    if not path.exists():
        return False, 'no local file'
    age = datetime.datetime.now(tz=datetime.timezone.utc) - \
          datetime.datetime.fromtimestamp(path.stat().st_mtime, tz=datetime.timezone.utc)
    if age < CACHE_TTL:
        h, m = age.seconds // 3600, (age.seconds % 3600) // 60
        return True, f'cached {h}h {m}m ago'
    return False, f'cache expired ({age.days}d {age.seconds // 3600}h old)'


def _parse_fetched_on(md_path: Path) -> datetime.datetime | None:
    """Extract the '*Fetched on: …*' timestamp from a saved Markdown file."""
    try:
        for line in md_path.read_text(encoding='utf-8').splitlines():
            m = re.search(r'\*Fetched on:\s*(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\*', line)
            if m:
                naive = datetime.datetime.strptime(m.group(1), '%Y-%m-%d %H:%M:%S')
                return naive.astimezone(datetime.timezone.utc)
    except Exception:
        pass
    return None


def _clean_markdown(md: str) -> str:
    """Fix common html2text artefacts: bulleted headings and deep indentation."""
    lines = []
    for line in md.splitlines():
        # '  * ### Heading' → '### Heading'
        if re.match(r'^\s*\*\s+(#{1,6})\s+', line):
            line = re.sub(r'^\s*\*\s+(#{1,6}\s+.+)$', r'\1', line)
        # Normalise deep bullet indentation to 2-space steps
        if re.match(r'^\s{4,}\*\s+', line):
            level = (len(line) - len(line.lstrip())) // 4
            line = '  ' * level + line.lstrip()
        lines.append(line)
    # Collapse 4+ blank lines to max 2
    return re.sub(r'\n{4,}', '\n\n\n', '\n'.join(lines))


# ---------------------------------------------------------------------------
# HTTP session (module-level, shared across the fetcher)
# ---------------------------------------------------------------------------
_SESSION = requests.Session()
_SESSION.headers['User-Agent'] = (
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
)

_HTML2TEXT = html2text.HTML2Text()
_HTML2TEXT.ignore_links = False
_HTML2TEXT.ignore_images = False
_HTML2TEXT.body_width = 0


# ---------------------------------------------------------------------------
# Core fetcher
# ---------------------------------------------------------------------------

class DocFetcher:
    def __init__(
        self,
        out_dir: Path = MD_OUT_DIR,
        delay: float = 1.0,
        max_pages: int = 200,
        force: bool = False,
    ):
        self.out_dir   = out_dir
        self.delay     = delay
        self.max_pages = max_pages
        self.force     = force

        # Intersight bundle cache — loaded once per fetcher instance
        self._bundle_text: str | None       = None
        self._cdn_version_base: str | None  = None

        for d in [out_dir, RAW_HTML_DIR, RAW_PDF_DIR, RAW_JSON_DIR, RAW_OTHER_DIR]:
            d.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------------
    # Network
    # ------------------------------------------------------------------

    def _get(self, url: str, extra_headers: dict | None = None) -> bytes | None:
        """GET a URL, return raw bytes or None on error."""
        try:
            print(f"  GET {url}")
            resp = _SESSION.get(url, timeout=30, headers=extra_headers or {})
            resp.raise_for_status()
            time.sleep(self.delay)
            return resp.content
        except Exception as exc:
            print(f"  ERROR {url}: {exc}")
            return None

    def _should_skip(self, url: str, raw_path: Path) -> tuple[bool, str]:
        """
        Return (True, reason) when the URL does not need re-downloading.

        Order of checks:
          1. --force → always download
          2. Raw file younger than 24 h → skip
          3. HTTP HEAD Last-Modified vs stored 'Fetched on' timestamp → decide
        """
        if self.force:
            return False, '--force: re-downloading'

        fresh, reason = _is_fresh(raw_path)
        if fresh:
            return True, reason

        # Raw file exists but is stale — check remote Last-Modified
        if raw_path.exists():
            reference = _parse_fetched_on(raw_path)
            if reference is None:
                reference = datetime.datetime.fromtimestamp(
                    raw_path.stat().st_mtime, tz=datetime.timezone.utc
                )
            try:
                print(f"  HEAD {url}")
                resp = _SESSION.head(url, timeout=15, allow_redirects=True)
                lm = resp.headers.get('Last-Modified') or resp.headers.get('last-modified')
                if lm:
                    remote_dt = datetime.datetime.fromtimestamp(
                        email.utils.parsedate_to_datetime(lm).timestamp(),
                        tz=datetime.timezone.utc,
                    )
                    if remote_dt <= reference:
                        return True, f'remote unchanged since {remote_dt:%Y-%m-%d %H:%M UTC}'
                    return False, f'remote updated {remote_dt:%Y-%m-%d %H:%M UTC}'
            except Exception as exc:
                return False, f'HEAD failed ({exc}); will re-download'

        return False, reason  # cache expired, no HEAD check possible

    # ------------------------------------------------------------------
    # Raw-file helpers
    # ------------------------------------------------------------------

    def _save_raw(self, dest: Path, data: bytes) -> None:
        dest.write_bytes(data)
        print(f"  saved → {dest}")

    def _cached_or_fetch(self, url: str, raw_path: Path,
                         extra_headers: dict | None = None) -> bytes | None:
        """Return file bytes from cache if fresh, otherwise fetch and save."""
        fresh, reason = _is_fresh(raw_path)
        if fresh and not self.force:
            print(f"  ⏭  {reason}: {raw_path.name}")
            return raw_path.read_bytes()
        data = self._get(url, extra_headers)
        if data is None:
            return None
        self._save_raw(raw_path, data)
        return data

    # ------------------------------------------------------------------
    # Intersight CDN-based fetch
    # ------------------------------------------------------------------

    @staticmethod
    def _parse_is_url(is_url: str) -> dict | None:
        """
        Parse https://intersight.com/help/<variant>/<section>/<topic> into parts.
        Returns None if the URL does not match the expected pattern.
        """
        parsed = urlparse(is_url)
        parts  = [p for p in parsed.path.strip('/').split('/') if p]
        # Expect: help / <variant> / <section> / <topic>
        if len(parts) < 4 or parts[0] != 'help':
            return None
        return {
            'variant':     parts[1],              # e.g. 'saas'
            'section':     parts[2],              # e.g. 'configure'
            'topic':       parts[3],              # e.g. 'chassis'
            'section_cap': parts[2].capitalize(), # e.g. 'Configure'
        }

    def _ensure_intersight_bundle(self) -> None:
        """
        Populate self._bundle_text and self._cdn_version_base (once per instance).
        Tries:
          1. Home-page <script src="..."> tags for base-bundle.js
          2. Regex scan of home-page HTML
        Sets self._cdn_version_base to the 'an-hulk' version prefix found in the
        bundle (if any); leaves it None if only a non-hulk bundle was found.
        """
        if self._bundle_text is not None:
            return  # already loaded

        print(f'  [IS] Fetching Intersight home page for base-bundle URL …')
        try:
            resp = _SESSION.get(_INTERSIGHT_HOME, timeout=30)
            resp.raise_for_status()
        except Exception as exc:
            print(f'  [IS] WARNING: could not fetch home page – {exc}')
            self._bundle_text = ''
            return

        home_html = resp.text

        # Locate base-bundle.js URL
        bundle_url: str | None = None
        soup = BeautifulSoup(home_html, 'html.parser')
        for tag in soup.find_all('script', src=True):
            src = tag['src']
            if 'base-bundle' in src:
                bundle_url = src if src.startswith('http') else urljoin(_INTERSIGHT_HOME, src)
                print(f'  [IS] base-bundle.js via <script>: {bundle_url}')
                break

        if not bundle_url:
            m = re.search(
                r'(https://cdn\.intersight\.com[^"\' ]*base-bundle[^"\' ]*\.js)',
                home_html,
            )
            if m:
                bundle_url = m.group(1)
                print(f'  [IS] base-bundle.js via regex: {bundle_url}')

        # Extract an-hulk CDN version from the home page directly (used as fallback)
        m2 = re.search(
            r'cdn\.intersight\.com/components/an-hulk/([^/"\' ]+)/',
            home_html,
        )
        if m2:
            self._cdn_version_base = f'{_INTERSIGHT_CDN_BASE}/{m2.group(1)}'
            print(f'  [IS] CDN version from home page: {self._cdn_version_base}')

        if not bundle_url:
            print('  [IS] base-bundle.js URL not found; will use CDN version only.')
            self._bundle_text = ''
            return

        # Extract an-hulk version from the bundle URL itself
        m3 = re.match(
            r'(https://cdn\.intersight\.com/components/an-hulk/[^/]+)',
            bundle_url,
        )
        if m3 and not self._cdn_version_base:
            self._cdn_version_base = m3.group(1)

        print(f'  [IS] Downloading base-bundle.js …')
        try:
            bresp = _SESSION.get(bundle_url, timeout=60, stream=True)
            bresp.raise_for_status()
            chunks, size = [], 0
            for chunk in bresp.iter_content(chunk_size=1024 * 1024):
                chunks.append(chunk)
                size += len(chunk)
                print(f'  [IS] Downloaded {size / 1024 / 1024:.1f} MB …', end='\r')
            self._bundle_text = b''.join(chunks).decode('utf-8', errors='replace')
            print(f'\n  [IS] bundle downloaded ({size / 1024 / 1024:.1f} MB)')

            # Also extract an-hulk version from inside the bundle text
            if not self._cdn_version_base:
                m4 = re.search(
                    r'https://cdn\.intersight\.com/components/an-hulk/([^/"\' ]+)/',
                    self._bundle_text,
                )
                if m4:
                    self._cdn_version_base = f'{_INTERSIGHT_CDN_BASE}/{m4.group(1)}'
        except Exception as exc:
            print(f'\n  [IS] WARNING: could not download bundle – {exc}')
            self._bundle_text = ''

    def _resolve_is_doc_url(
        self,
        is_url: str,
        topic: str,
        section_cap: str,
    ) -> str | None:
        """
        Resolve the CDN HTML URL for an Intersight help topic.
        Search order:
          1. bundle text → full CDN URL match
          2. bundle text → CDN version prefix + constructed path
          3. cdn_version_base (from home-page) + constructed path
          4. Fetch the IS help page and extract the CDN version from its HTML
        """
        doc_path = (
            f'docs/cloud/data/articles/features/{topic}/{section_cap}/en/index.html'
        )

        # --- bundle search ---
        bt = self._bundle_text or ''
        if bt:
            # Full URL in bundle
            m = re.search(
                r'(https://cdn\.intersight\.com/components/an-hulk/[^"\' ]*'
                + re.escape(f'features/{topic}/{section_cap}/en/index.html')
                + r')',
                bt,
            )
            if m:
                print(f'  [IS] Doc URL found in bundle: {m.group(1)}')
                return m.group(1)

            # Version prefix inside bundle
            if self._cdn_version_base:
                url = f'{self._cdn_version_base}/{doc_path}'
                print(f'  [IS] Constructed doc URL from bundle version: {url}')
                return url

        # --- cdn_version_base from home page ---
        if self._cdn_version_base:
            url = f'{self._cdn_version_base}/{doc_path}'
            print(f'  [IS] Constructed doc URL from CDN version base: {url}')
            return url

        # --- last resort: fetch the IS help page and scrape the CDN version ---
        print(f'  [IS] Fetching IS help page to extract CDN version: {is_url}')
        try:
            resp = _SESSION.get(is_url, timeout=30)
            m = re.search(
                r'cdn\.intersight\.com/components/an-hulk/([^/"\' ]+)/',
                resp.text,
            )
            if m:
                version_base = f'{_INTERSIGHT_CDN_BASE}/{m.group(1)}'
                self._cdn_version_base = version_base
                url = f'{version_base}/{doc_path}'
                print(f'  [IS] Doc URL from IS help page scrape: {url}')
                return url
        except Exception as exc:
            print(f'  [IS] WARNING: could not fetch IS help page – {exc}')

        return None

    def fetch_intersight_guide(self, is_url: str) -> tuple[str, str] | None:
        """
        Fetch an Intersight help topic via the CDN static HTML (no JS required).
        Returns (md_filename, markdown_content) or None on failure.
        """
        info = self._parse_is_url(is_url)
        if info is None:
            # URL doesn't match /help/<variant>/<section>/<topic> pattern;
            # fall back to standard HTML guide crawl.
            print(f'  [IS] URL does not match /help/variant/section/topic; '
                  f'falling back to HTML crawl.')
            return self.fetch_html_guide(is_url)

        variant     = info['variant']
        section     = info['section']
        topic       = info['topic']
        section_cap = info['section_cap']

        out_stem   = f'intersight-{variant}-{section}_{topic}'
        md_filename = out_stem + '.md'

        print(f'  [IS] Resolving doc URL for {variant}/{section}/{topic} …')
        self._ensure_intersight_bundle()
        doc_url = self._resolve_is_doc_url(is_url, topic, section_cap)

        if not doc_url:
            print(f'  [IS] ERROR: could not determine CDN doc URL for {is_url}')
            return None

        # Fetch CDN page — always decode as UTF-8 to avoid double-encoding artefacts
        print(f'  [IS] GET {doc_url}')
        try:
            resp = _SESSION.get(doc_url, timeout=30)
            resp.raise_for_status()
            doc_html = resp.content.decode('utf-8', errors='replace')
            time.sleep(self.delay)
        except Exception as exc:
            print(f'  [IS] ERROR fetching CDN page: {exc}')
            return None

        # Cache the raw HTML
        raw_path = RAW_HTML_DIR / f'{out_stem}.html'
        raw_path.write_text(doc_html, encoding='utf-8')
        print(f'  [IS] cached HTML → {raw_path}')

        # Extract main content
        soup = BeautifulSoup(doc_html, 'html.parser')
        content_el = None
        for selector in ('article', '[role="main"]', 'main',
                         '.article-content', '.content', '#content', '#main'):
            content_el = soup.select_one(selector)
            if content_el:
                break
        content_html = str(content_el or soup.find('body') or soup)

        # Convert to Markdown (prefer markdownify; fall back to html2text)
        if _MARKDOWNIFY_OK:
            page_md = _markdownify(
                content_html,
                heading_style='ATX',
                bullets='-',
                strip=['script', 'style', 'nav', 'footer', 'header'],
            )
        else:
            page_md = _clean_markdown(_HTML2TEXT.handle(content_html))

        # Build Markdown with header
        title_tag  = soup.find('title')
        page_title = (title_tag.get_text(strip=True)
                      if title_tag else f'{section_cap} {topic.capitalize()}')
        md = (
            f'# {page_title}\n\n'
            f'> IS URL: {is_url}\n'
            f'> Source: {doc_url}\n'
            f'*Fetched on: {time.strftime("%Y-%m-%d %H:%M:%S")}*\n\n'
            '---\n\n'
        ) + page_md

        return md_filename, md

    # ------------------------------------------------------------------
    # HTML guide (multi-page crawl)
    # ------------------------------------------------------------------

    def _extract_body(self, soup: BeautifulSoup) -> str:
        """Return the main content HTML, stripping chrome (nav/header/footer)."""
        for selector in ('article', 'main', '.content', '#content',
                         '.main-content', 'div[role="main"]'):
            node = soup.select_one(selector)
            if node:
                break
        else:
            node = soup.find('body')
        if not node:
            return ''
        for tag in node.find_all(['script', 'style', 'nav', 'footer', 'header']):
            tag.decompose()
        return str(node)

    def _same_guide(self, url: str, base_url: str) -> bool:
        """True if *url* shares the same path prefix as *base_url*."""
        pu, pb = urlparse(url), urlparse(base_url)
        if pu.netloc != pb.netloc:
            return False
        base_parts = pb.path.rstrip('/').split('/')[:-1]
        url_parts  = pu.path.rstrip('/').split('/')
        return '/'.join(url_parts[:len(base_parts)]) == '/'.join(base_parts)

    def _collect_links(self, soup: BeautifulSoup, base_url: str) -> list[str]:
        """Return absolute sub-page URLs belonging to the same guide."""
        seen: set[str] = set()
        result: list[str] = []
        for a in soup.find_all('a', href=True):
            href = a['href'].split('#')[0].strip()
            if not href or href.startswith('javascript:'):
                continue
            abs_url = urljoin(base_url, href)
            if abs_url not in seen and self._same_guide(abs_url, base_url):
                seen.add(abs_url)
                if _content_type(abs_url) == 'html':
                    result.append(abs_url)
        return result

    def _md_filename_for_guide(self, base_url: str, soup: BeautifulSoup) -> str:
        """Derive the output .md filename for an HTML guide."""
        if base_url.startswith('https://intersight.com'):
            prefix = _intersight_prefix(base_url)
            slug   = _url_slug(base_url)
            name   = slug if slug.endswith('.md') else slug + '.md'
            return prefix + name

        # Cisco guide: use <title>
        tag = soup.find('title')
        if tag:
            title = re.sub(r'\s*-\s*Cisco\s*$', '', tag.get_text(strip=True),
                           flags=re.IGNORECASE).strip()
            if title:
                return _title_to_filename(title)

        # Fallback: URL slug
        return _url_slug(base_url) + '.md'

    def fetch_html_guide(self, base_url: str) -> tuple[str, str] | None:
        """
        Crawl all pages of an HTML guide, convert to Markdown, and return
        (md_filename, markdown_content).  Returns None on failure.
        """
        print(f"\n  Crawling guide: {base_url}")
        visited:  set[str]          = set()
        queue:    list[str]         = [base_url]
        pages:    list[tuple[str, BeautifulSoup]] = []   # (url, soup)
        md_filename: str | None     = None

        while queue and len(visited) < self.max_pages:
            url = queue.pop(0)
            if url in visited:
                continue
            visited.add(url)

            raw_path = RAW_HTML_DIR / _raw_html_name(url)
            data = self._cached_or_fetch(url, raw_path)
            if data is None:
                continue

            soup = BeautifulSoup(data, 'html.parser')

            if url == base_url:
                md_filename = self._md_filename_for_guide(base_url, soup)
                print(f"  filename: {md_filename}")

            pages.append((url, soup))
            new_links = [l for l in self._collect_links(soup, base_url)
                         if l not in visited and l not in queue]
            if new_links:
                print(f"  found {len(new_links)} sub-page(s) from {url}")
            queue.extend(new_links)

        if not pages:
            return None

        # Build combined Markdown
        md = _md_header(base_url)
        for i, (url, soup) in enumerate(pages, 1):
            body_html = self._extract_body(soup)
            page_md   = _clean_markdown(_HTML2TEXT.handle(body_html))
            md += f"## Page {i}: {url}\n\n{page_md}\n\n---\n\n"

        md = _clean_markdown(md)
        print(f"  converted {len(pages)} page(s)")
        return md_filename or (_url_slug(base_url) + '.md'), md

    # ------------------------------------------------------------------
    # PDF
    # ------------------------------------------------------------------

    def fetch_pdf(self, url: str) -> tuple[str, str] | None:
        """Download a PDF and return (md_filename, markdown_content)."""
        print(f"\n  Fetching PDF: {url}")
        raw_path = RAW_PDF_DIR / _raw_name(url, 'pdf')
        data = self._cached_or_fetch(url, raw_path)
        if data is None:
            return None

        md = _md_header(url)
        if not _PDF_OK:
            md += '*pdfminer.six not installed — run `pip install pdfminer.six`.*\n'
        else:
            try:
                md += pdf_extract_text(io.BytesIO(data)) or '*(no text extracted)*'
            except Exception as exc:
                md += f'*PDF extraction error: {exc}*\n'

        return _url_slug(url) + '.md', md

    # ------------------------------------------------------------------
    # JSON
    # ------------------------------------------------------------------

    def fetch_json(self, url: str) -> tuple[str, str] | None:
        """Download a JSON file and return (md_filename, markdown_content)."""
        print(f"\n  Fetching JSON: {url}")
        raw_path = RAW_JSON_DIR / _raw_name(url, 'json')
        data = self._cached_or_fetch(url, raw_path,
                                     extra_headers={'Accept': 'application/json'})
        if data is None:
            return None

        md = _md_header(url)
        try:
            parsed = try_load_json(str(raw_path))
            md += json_to_md(parsed) + '\n\n'
            pretty = json.dumps(parsed, ensure_ascii=False, indent=2)
            md += '<details><summary>Raw JSON</summary>\n\n```json\n'
            md += pretty
            md += '\n```\n\n</details>\n'
        except Exception as exc:
            print(f"  WARNING: could not parse JSON ({exc}); embedding raw")
            md += '```json\n' + data.decode('utf-8', errors='replace') + '\n```\n'

        return _url_slug(url) + '.md', md

    # ------------------------------------------------------------------
    # Other / unknown
    # ------------------------------------------------------------------

    def fetch_other(self, url: str) -> tuple[str, str] | None:
        """Download an unknown file type and return (md_filename, markdown_content)."""
        print(f"\n  Fetching (other): {url}")
        raw_path = RAW_OTHER_DIR / _raw_name(url, 'other')
        data = self._cached_or_fetch(url, raw_path)
        if data is None:
            return None

        md = _md_header(url)
        try:
            text = data.decode('utf-8')
        except UnicodeDecodeError:
            try:
                text = data.decode('latin-1')
            except Exception:
                text = None

        if text is not None:
            ext  = os.path.splitext(_url_slug(url))[1].lstrip('.')
            md  += f'```{ext}\n{text}\n```\n'
        else:
            md += f'*Binary file ({len(data):,} bytes) — no text representation.*\n'

        return _url_slug(url) + '.md', md

    # ------------------------------------------------------------------
    # Entry point
    # ------------------------------------------------------------------

    def process_url(self, url: str) -> None:
        """Process a single URL: download, convert, and write the .md file."""
        # Intersight pages are JS-rendered SPAs; use CDN-based fetch instead
        if urlparse(url).netloc == 'intersight.com':
            info = self._parse_is_url(url)
            if info is not None:
                out_stem = (
                    f'intersight-{info["variant"]}-'
                    f'{info["section"]}_{info["topic"]}'
                )
                raw_path = RAW_HTML_DIR / f'{out_stem}.html'
                skip, reason = self._should_skip(url, raw_path)
                if skip:
                    print(f'  ⏭  skipping ({reason})')
                    return
                print(f'  ↓  {reason}')
                result = self.fetch_intersight_guide(url)
                if result is None:
                    print(f'  ✗  failed: {url}')
                    return
                md_filename, content = result
                out_path = self.out_dir / md_filename
                out_path.write_text(content, encoding='utf-8')
                print(f'  ✓  {out_path}')
                return

        ctype    = _content_type(url)
        raw_path = _raw_dir(ctype) / _raw_name(url, ctype)

        skip, reason = self._should_skip(url, raw_path)
        if skip:
            print(f"  ⏭  skipping ({reason})")
            return
        print(f"  ↓  {reason}")

        dispatch = {
            'html':  self.fetch_html_guide,
            'pdf':   self.fetch_pdf,
            'json':  self.fetch_json,
            'other': self.fetch_other,
        }
        result = dispatch[ctype](url)
        if result is None:
            print(f"  ✗  failed: {url}")
            return

        md_filename, content = result
        out_path = self.out_dir / md_filename
        out_path.write_text(content, encoding='utf-8')
        print(f"  ✓  {out_path}")

    def process_urls_file(self, filepath: str) -> None:
        """Read URLs from a Markdown file and process each one."""
        urls = _extract_urls(filepath)
        print(f"Found {len(urls)} URL(s) in {filepath}")

        for i, url in enumerate(urls, 1):
            print(f"\n{'='*72}")
            print(f"[{i}/{len(urls)}] {url}")
            print('='*72)
            try:
                self.process_url(url)
            except Exception as exc:
                print(f"  ✗  unhandled error: {exc}")
                traceback.print_exc()
            if i < len(urls):
                time.sleep(self.delay * 2)

        print(f"\nDone. Processed {len(urls)} URL(s).")


# ---------------------------------------------------------------------------
# URL extraction
# ---------------------------------------------------------------------------

def _extract_urls(filepath: str) -> list[str]:
    """Extract all HTTP(S) URLs from a Markdown file, skipping comment lines."""
    urls: list[str] = []
    with open(filepath, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            # Markdown links [text](url)
            for _, url in re.findall(r'\[([^\]]*)\]\(([^)]+)\)', line):
                urls.append(url)
            # Bare URLs
            for url in re.findall(r'(?<![\(\[])(https?://[^\s\)\]]+)', line):
                urls.append(url)
    # Preserve order, deduplicate
    return list(OrderedDict.fromkeys(urls))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(
        description='Fetch Cisco UCS/Intersight documentation and convert to Markdown.'
    )
    parser.add_argument('urls_file', nargs='?', default='urls.md',
                        help='Markdown file containing URLs (default: urls.md)')
    parser.add_argument('-o', '--output-dir', default=str(MD_OUT_DIR),
                        help=f'Markdown output directory (default: {MD_OUT_DIR})')
    parser.add_argument('-d', '--delay', type=float, default=1.0,
                        help='Seconds between requests (default: 1.0)')
    parser.add_argument('--max-pages', type=int, default=200,
                        help='Max pages per HTML guide (default: 200)')
    parser.add_argument('-f', '--force', action='store_true',
                        help='Re-download everything, ignoring cache')
    args = parser.parse_args()

    if args.force:
        print('⚠  Force mode: ignoring all cached files')

    fetcher = DocFetcher(
        out_dir   = Path(args.output_dir),
        delay     = args.delay,
        max_pages = args.max_pages,
        force     = args.force,
    )
    fetcher.process_urls_file(args.urls_file)


if __name__ == '__main__':
    main()
