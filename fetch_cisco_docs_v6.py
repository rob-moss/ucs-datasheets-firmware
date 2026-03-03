#!/usr/bin/env python3
# v6
"""
Fetch Cisco UCS documentation pages and convert to Markdown.

For each URL in urls.md:
  - HTML  → crawl all sub-pages, combine into one .md file in ./ucs-docs/
  - PDF   → extract text, save as .md in ./ucs-docs/
  - JSON  → render as table/list, save as .md in ./ucs-docs/
  - other → wrap raw text in a fenced block, save as .md in ./ucs-docs/

Raw downloads are cached in ./ucs-docs-raw/{html,pdf,json,other}/.
Files fetched within the last 24 hours are skipped unless --force is set.

Intersight URLs (intersight.com/help/…) are fetched via Cisco CDN (no JS needed):
  1. The CDN version is scraped live from https://intersight.com/help/saas.
     A file-based cache (~/.ucs-docs-raw/html/.intersight_cdn_version, 7-day TTL)
     is validated with a HEAD request before accepting.
  2. Routes are built from {CDN_BASE}/model/en/cloud-model.json.
  3. Three saas pages (home, glossary, resources) are client-rendered; they are
     generated directly from model JSON without fetching a CDN URL.
  4. A 403 on any CDN doc page is a non-fatal skip.

Dependencies:
    pip install requests beautifulsoup4 html2text pdfminer.six
"""

import io
import json
import os
import re
import time
import traceback
import datetime
import requests
from collections import OrderedDict
from pathlib import Path
from urllib.parse import urljoin, urlparse, unquote

import html2text
from bs4 import BeautifulSoup

from json_to_markdown import value_to_markdown as json_to_md, try_load_json

try:
    from pdfminer.high_level import extract_text as pdf_extract_text
    _PDF_OK = True
except ImportError:
    _PDF_OK = False
    def pdf_extract_text(*a, **kw) -> str:  # type: ignore[misc]
        return ""


# ---------------------------------------------------------------------------
# Paths & constants
# ---------------------------------------------------------------------------

urlsfile='urls.md'                          # Default input file with URLs to fetch
isfileprefix = 'intersight-'                # Prefix for intersight based files
ucsfileprefix = 'ucs-'                      # Prefix for UCS based files (non-intersight)


RAW_HTML_DIR  = Path('./ucs-docs-raw/html')
RAW_PDF_DIR   = Path('./ucs-docs-raw/pdf')
RAW_JSON_DIR  = Path('./ucs-docs-raw/json')
RAW_OTHER_DIR = Path('./ucs-docs-raw/other')
MD_OUT_DIR    = Path('./ucs-docs')

_RAW_DIRS = {'html': RAW_HTML_DIR, 'pdf': RAW_PDF_DIR,
             'json': RAW_JSON_DIR, 'other': RAW_OTHER_DIR}
_EXT_MAP  = {'.html': 'html', '.htm': 'html', '.xhtml': 'html', '.shtml': 'html',
             '.pdf': 'pdf', '.json': 'json'}

CACHE_TTL = datetime.timedelta(hours=24)

# ---------------------------------------------------------------------------
# Intersight constants
# ---------------------------------------------------------------------------
_IS_HOME     = 'https://intersight.com'
_IS_CDN_BASE = 'https://cdn.intersight.com/components/an-hulk'
_IS_CDN_TTL  = datetime.timedelta(days=7)
_IS_CDN_CACHE = RAW_HTML_DIR / '.intersight_cdn_version'
_IS_HEADERS  = {
    'User-Agent':      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:147.0) Gecko/20100101 Firefox/147.0',
    'Referer':         'https://intersight.com/',
    'Origin':          'https://intersight.com',
    'DNT':             '1',
    'Connection':      'keep-alive',
    'Sec-Fetch-Dest':  'empty',
    'Sec-Fetch-Mode':  'cors',
    'Sec-Fetch-Site':  'same-site',
}


# URL path segment aliases (segment in base URL -> key in model)
_IS_SECTION_ALIASES = {
    "monitoring_get_started": "monitoring_get_start",
    "role_based_access":      "role_based",
}

# saas pages rendered client-side from model JSON (no CDN HTML file)
_IS_MODEL_PAGES = {
    "saas":           "home",
    "saas/glossary":  "glossary",
    "saas/resources": "resources",
}

# Appliance CDN paths not present in cloud-model.json (confirmed via Playwright)
_IS_APPLIANCE_FALLBACKS = {
    "appliance/whats_new/connected_appliance": "docs/onprem/data/articles/connected_appliance/new_2026/en/index.html",
    "appliance/whats_new/private_appliance":   "docs/onprem/data/articles/private_appliance/new_2026/en/index.html",
    "appliance/system/settings":               "docs/onprem/data/articles/features/cisco_intersight/settings/en/index.html",
    "appliance/operate/servers":               "docs/onprem/data/articles/features/servers/operate/en/index.html",
    "appliance/settings":                      "docs/onprem/data/articles/settings/en/index.html",
    "appliance/device_console":                "docs/onprem/data/articles/device_console/en/index.html",
}

# ---------------------------------------------------------------------------
# Shared utilities
# ---------------------------------------------------------------------------
_H2T = html2text.HTML2Text()
_H2T.ignore_links = False
_H2T.ignore_images = False
_H2T.body_width = 0

_SESSION = requests.Session()
_SESSION.headers['User-Agent'] = (
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
)


def _url_slug(url: str) -> str:
    """Last non-empty path segment of a URL, URL-decoded."""
    path = unquote(urlparse(url).path).rstrip('/')
    seg  = os.path.basename(path)
    if seg and not seg.startswith('.'):
        return seg
    flat = re.sub(r'[^a-zA-Z0-9._-]', '_', path.strip('/'))
    return flat[:200] or 'index'


def _content_type(url: str) -> str:
    _, ext = os.path.splitext(urlparse(url).path.rstrip('/'))
    return _EXT_MAP.get(ext.lower(), 'html' if not ext else 'other')


def _raw_name(url: str, ctype: str) -> str:
    """Cache filename for *url* with the correct extension."""
    slug = _url_slug(url)
    if ctype == 'html':
        if not os.path.splitext(slug)[1]:
            slug += '.html'
        if urlparse(url).netloc == 'intersight.com':
            slug = _is_prefix(url) + slug
        return slug
    suffix = {'pdf': '.pdf', 'json': '.json'}.get(ctype, '')
    if suffix and not slug.lower().endswith(suffix):
        slug += suffix
    return slug


def _is_prefix(url: str) -> str:
    path = urlparse(url).path
    if '/saas/' in path:
        return 'intersight-saas-'
    if '/appliance/' in path:
        return 'intersight-appliance-'
    return 'intersight-'


def _title_to_filename(title: str) -> str:
    safe = re.sub(r'[<>:"/\\|?*]', '', title)
    safe = re.sub(r'[\s,]+', '-', safe.strip())
    safe = re.sub(r'-{2,}', '-', safe).strip('-')
    return (safe[:200] or 'document') + '.md'


def _md_header(url: str) -> str:
    return (
        f'# Documentation: {url}\n\n'
        f'*Fetched on: {time.strftime("%Y-%m-%d %H:%M:%S")}*\n\n'
        '---\n\n'
    )


def _is_fresh(path: Path) -> bool:
    if not path.exists():
        return False
    age = datetime.datetime.now(tz=datetime.timezone.utc) - \
          datetime.datetime.fromtimestamp(path.stat().st_mtime, tz=datetime.timezone.utc)
    return age < CACHE_TTL


def _clean_markdown(md: str) -> str:
    lines = []
    for line in md.splitlines():
        if re.match(r'^\s*\*\s+(#{1,6})\s+', line):
            line = re.sub(r'^\s*\*\s+(#{1,6}\s+.+)$', r'\1', line)
        if re.match(r'^\s{4,}\*\s+', line):
            level = (len(line) - len(line.lstrip())) // 4
            line  = '  ' * level + line.lstrip()
        lines.append(line)
    return re.sub(r'\n{4,}', '\n\n\n', '\n'.join(lines))


def _strip_html(raw: str) -> str:
    return BeautifulSoup(raw, 'html.parser').get_text(' ', strip=True)


# ---------------------------------------------------------------------------
# Intersight CDN helpers
# ---------------------------------------------------------------------------

def _load_cdn_version() -> str | None:
    if not _IS_CDN_CACHE.exists():
        return None
    age = (datetime.datetime.now(tz=datetime.timezone.utc)
           - datetime.datetime.fromtimestamp(_IS_CDN_CACHE.stat().st_mtime,
                                             tz=datetime.timezone.utc))
    if age > _IS_CDN_TTL:
        return None
    return _IS_CDN_CACHE.read_text(encoding='utf-8').strip() or None


def _save_cdn_version(version: str) -> None:
    _IS_CDN_CACHE.parent.mkdir(parents=True, exist_ok=True)
    _IS_CDN_CACHE.write_text(version, encoding='utf-8')


def _validate_cdn_version(version: str) -> bool:
    url = f'{_IS_CDN_BASE}/{version}/model/en/cloud-model.json'
    try:
        return _SESSION.head(url, timeout=10, allow_redirects=True).status_code == 200
    except Exception:
        return False


def _extract_cdn_version(html: str) -> str | None:
    # More specific pattern from v4 — matches the base-bundle.js script tag
    m = re.search(r'an-hulk/([\d.]+-\d+)/build/base-bundle\.js', html)
    if m:
        return m.group(1)
    # Fallback: any CDN path reference
    m = re.search(r'cdn\.intersight\.com/components/an-hulk/([^/"\' ]+)/', html)
    return m.group(1) if m else None


# ---------------------------------------------------------------------------
# Intersight route building & resolution (ported from fetch_intersight_v4.py)
# ---------------------------------------------------------------------------

def _build_intersight_routes(cdn_base: str, model: dict) -> dict[str, str]:
    """
    Build URL-key -> CDN long-URL mapping from cloud-model.json +
    hardcoded appliance fallbacks.  Keys match the path after /help/.
    """
    routes: dict[str, str] = {}

    def cdn_url(folder: str, file_name: str | None = None,
                resource: str = 'articles', cloud: str = 'cloud') -> str:
        return f"{cdn_base}/docs/{cloud}/data/{resource}/{folder}/{file_name or 'index.html'}"

    def walk(item: dict, prefix: str) -> None:
        sec  = item.get('section', '')
        path = f"{prefix}/{sec}".strip('/') if sec else prefix.strip('/')
        for d in item.get('data') or []:
            if d.get('folder'):
                routes[path] = cdn_url(d['folder'], d.get('fileName'),
                                       d.get('resource') or 'articles')
            for sub in d.get('items') or []:
                walk(sub, path)
        for child in item.get('items') or []:
            walk(child, path)

    # Article routes (saas)
    for art in model.get('articles', []):
        walk(art, '')

    # Resource routes (saas/resources/*)
    for res in model.get('resources', []):
        folder = res.get('folder', '')
        for doc in res.get('docs', []):
            link, name = doc.get('link', ''), doc.get('name', '')
            if link and name:
                routes[link.lower()] = cdn_url(folder, name, 'resources')

    # Appliance fallbacks
    for key, path in _IS_APPLIANCE_FALLBACKS.items():
        routes[key] = f"{cdn_base}/{path}"

    return routes


def _resolve_intersight_url(base_url: str, routes: dict[str, str]) -> str | None:
    """Map a help URL to its CDN long URL, or None if not found."""
    base_url = base_url.rstrip('/')
    parts = base_url.split('/')
    if 'help' not in parts:
        return None
    rest = parts[parts.index('help') + 1:]
    if not rest:
        return None

    variant = rest[0]
    section = rest[1] if len(rest) > 1 else ''
    topics  = [_IS_SECTION_ALIASES.get(t, t) for t in rest[2:]]

    if variant == 'saas':
        # resources/* uses a flat key (just the resource name)
        if section == 'resources' and topics:
            return routes.get(topics[0].lower())
        path = '/'.join([section] + topics) if section else ''
        return routes.get(path)
    else:
        key = '/'.join([variant, section] + topics)
        return routes.get(key)


def _intersight_model_key(base_url: str) -> str | None:
    """Return the _IS_MODEL_PAGES key for client-rendered pages, or None."""
    base_url = base_url.rstrip('/')
    parts = base_url.split('/')
    if 'help' not in parts:
        return None
    rest = parts[parts.index('help') + 1:]
    path = '/'.join(rest[:2]) if len(rest) > 1 else (rest[0] if rest else '')
    return _IS_MODEL_PAGES.get(path)


def _intersight_url_slug(base_url: str) -> str:
    """Produce a filesystem-safe stem from an intersight.com/help/ URL."""
    parts = base_url.rstrip('/').split('/')
    if 'help' in parts:
        tail = parts[parts.index('help') + 1:]
    else:
        tail = parts[-4:]
    return isfileprefix + '_'.join(tail)[:109]


def _model_to_markdown(model: dict, key: str) -> str:
    """Generate Markdown for client-rendered pages from cloud-model.json data."""
    lines: list[str] = []

    if key == 'home':
        home = model.get('home', {})
        lines.append('# Intersight Help')
        if home.get('description'):
            lines.append(home['description'])
        for row in home.get('rows', []):
            for h in row.get('helplets', []):
                if h.get('title'):
                    lines.append(f"\n## {h['title']}")
                if h.get('description'):
                    lines.append(h['description'])
                for link in (h.get('links') or {}).get('data', []):
                    lines.append(f"- [{link['label']}]({link['url']})")

    elif key == 'glossary':
        lines.append('# Glossary')
        for entry in model.get('glossary', []):
            lines.append(f"\n## {entry.get('name', '')}")
            if entry.get('description'):
                lines.append(_strip_html(entry['description']))

    elif key == 'resources':
        lines.append('# Resources')
        for item in model.get('resources', []):
            if item.get('title'):
                lines.append(f"\n## {item['title']}")
            if item.get('description'):
                lines.append(_strip_html(item['description']))
            for doc in item.get('docs', []):
                label = doc.get('name') or doc.get('link', '')
                if label:
                    lines.append(f"- [{label}]({doc.get('link', '')})")

    return '\n'.join(lines)


# ---------------------------------------------------------------------------
# Core fetcher
# ---------------------------------------------------------------------------

class DocFetcher:
    def __init__(
        self,
        out_dir:   Path  = MD_OUT_DIR,
        delay:     float = 0.1,
        max_pages: int   = 200,
        force:     bool  = False,
    ):
        self.out_dir   = out_dir
        self.delay     = delay
        self.max_pages = max_pages
        self.force     = force
        self._cdn_base: str | None = None   # resolved once per run
        self._cdn_init = False              # True once resolution has been attempted
        self._model:  dict | None = None    # cloud-model.json, loaded once
        self._routes: dict | None = None    # CDN route table, built once
        self._failures: list[dict] = []

        for d in _RAW_DIRS.values():
            d.mkdir(parents=True, exist_ok=True)
        out_dir.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------------
    # Network
    # ------------------------------------------------------------------

    def _get(self, url: str, headers: dict | None = None) -> bytes | None:
        try:
            print(f'  GET {url}')
            resp = _SESSION.get(url, timeout=30, headers=headers or {})
            if resp.status_code == 403:
                print(f'  WARNING 403 Forbidden: {url} – skipping.')
                return None
            resp.raise_for_status()
            time.sleep(self.delay)
            return resp.content
        except Exception as exc:
            print(f'  ERROR {url}: {exc}')
            return None

    def _cached_or_fetch(self, url: str, raw_path: Path,
                         headers: dict | None = None) -> bytes | None:
        if _is_fresh(raw_path) and not self.force:
            print(f'  ⏭  cached: {raw_path.name}')
            return raw_path.read_bytes()
        data = self._get(url, headers)
        if data is not None:
            raw_path.parent.mkdir(parents=True, exist_ok=True)
            raw_path.write_bytes(data)
            print(f'  saved → {raw_path}')
        return data

    # ------------------------------------------------------------------
    # Intersight CDN resolution
    # ------------------------------------------------------------------

    def _ensure_cdn(self) -> None:
        """Resolve the Intersight CDN version at most once per instance."""
        if self._cdn_init:
            return
        self._cdn_init = True

        # 1. Disk cache
        cached = _load_cdn_version()
        if cached and _validate_cdn_version(cached):
            self._cdn_base = f'{_IS_CDN_BASE}/{cached}'
            print(f'  [IS] CDN version (cache): {cached}')
            return
        if cached:
            print(f'  [IS] Cached CDN version {cached!r} stale; refreshing …')

        # 2. Scrape the Intersight help page for CDN version
        print(f'  [IS] Fetching https://intersight.com/help/saas for CDN version …')
        try:
            resp = _SESSION.get('https://intersight.com/help/saas',
                                timeout=30, headers=_IS_HEADERS)
            if not resp.ok:
                print(f'  [IS] WARNING: help page returned HTTP {resp.status_code}')
                return
            version = _extract_cdn_version(resp.text)
            if version:
                _save_cdn_version(version)
                self._cdn_base = f'{_IS_CDN_BASE}/{version}'
                print(f'  [IS] CDN version (help page): {version}')
                return
        except Exception as exc:
            print(f'  [IS] WARNING: could not fetch help page – {exc}')

        print('  [IS] WARNING: CDN version unavailable – Intersight URLs will be skipped.')

    def _ensure_model_routes(self) -> None:
        """Load cloud-model.json and build routes, at most once per instance."""
        if self._routes is not None:
            return
        if not self._cdn_base:
            self._routes = {}
            return

        # Load model (cached to disk)
        cache = RAW_HTML_DIR / 'cloud-model.json'
        if cache.exists() and not self.force:
            print(f'  [IS] Using cached {cache.name}')
            self._model = json.loads(cache.read_text(encoding='utf-8'))
        else:
            url = f'{self._cdn_base}/model/en/cloud-model.json'
            print(f'  [IS] Fetching {url}')
            data = self._get(url, {**_IS_HEADERS, 'Accept': 'application/json'})
            if data is None:
                print('  [IS] WARNING: could not load cloud-model.json – Intersight routes unavailable.')
                self._routes = {}
                return
            self._model = json.loads(data.decode('utf-8'))
            cache.write_text(json.dumps(self._model, indent=2), encoding='utf-8')
            print(f'  [IS] Cached → {cache}')

        self._routes = _build_intersight_routes(self._cdn_base, self._model)
        print(f'  [IS] {len(self._routes)} routes built')

    # ------------------------------------------------------------------
    # Intersight guide
    # ------------------------------------------------------------------

    def fetch_intersight_guide(self, is_url: str) -> tuple[str, str] | None:
        self._ensure_cdn()
        self._ensure_model_routes()

        slug = _intersight_url_slug(is_url)
        raw_path = RAW_HTML_DIR / f'{slug}.html'
        md_path  = self.out_dir / f'{slug}.md'

        # --- Client-rendered model-data page (no CDN HTML) ---
        model_key = _intersight_model_key(is_url)
        if model_key:
            if _is_fresh(md_path) and not self.force:
                print(f'  ⏭  cached: {md_path.name}')
                return md_path.name, md_path.read_text(encoding='utf-8')
            if not self._model:
                self._failures.append({'url': is_url, 'reason': 'model not loaded'})
                return None
            content = _model_to_markdown(self._model, model_key)
            print(f'  [IS] [model:{model_key}] → {md_path.name}')
            return md_path.name, content

        # --- CDN HTML page ---
        if _is_fresh(raw_path) and not self.force:
            print(f'  ⏭  cached: {raw_path.name}')
            doc_html = raw_path.read_text(encoding='utf-8')
        else:
            cdn_url = _resolve_intersight_url(is_url, self._routes or {})
            if not cdn_url:
                print(f'  [IS] WARNING: no CDN URL found for {is_url}')
                self._failures.append({'url': is_url, 'reason': 'CDN URL not found'})
                return None
            print(f'  [IS] → {cdn_url}')
            data = self._get(cdn_url, _IS_HEADERS)
            if data is None:
                self._failures.append({'url': is_url, 'reason': 'HTTP 403 / fetch error'})
                return None
            doc_html = data.decode('utf-8', errors='replace')
            raw_path.write_text(doc_html, encoding='utf-8')
            print(f'  [IS] cached HTML → {raw_path.name}')

        # Convert HTML → Markdown
        soup = BeautifulSoup(doc_html, 'html.parser')
        content = (soup.select_one('article, [role="main"], main, .content, #content')
                   or soup.find('body') or soup)
        page_md = _clean_markdown(_H2T.handle(str(content)))

        title_tag = soup.find('title')
        heading   = title_tag.get_text(strip=True) if title_tag else slug.replace('_', ' ').title()
        md = (f'# {heading}\n\n'
              f'> Source: {is_url}\n\n'
              f'*Fetched on: {time.strftime("%Y-%m-%d %H:%M:%S")}*\n\n'
              '---\n\n') + page_md
        return md_path.name, _clean_markdown(md)

    # ------------------------------------------------------------------
    # HTML guide (multi-page crawl)
    # ------------------------------------------------------------------

    def _extract_body(self, soup: BeautifulSoup) -> str:
        for sel in ('article', 'main', '.content', '#content',
                    '.main-content', 'div[role="main"]'):
            node = soup.select_one(sel)
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
        pu, pb = urlparse(url), urlparse(base_url)
        if pu.netloc != pb.netloc:
            return False
        base_parts = pb.path.rstrip('/').split('/')[:-1]
        url_parts  = pu.path.rstrip('/').split('/')
        return '/'.join(url_parts[:len(base_parts)]) == '/'.join(base_parts)

    def _collect_links(self, soup: BeautifulSoup, base_url: str) -> list[str]:
        seen: set[str] = set()
        result: list[str] = []
        for a in soup.find_all('a', href=True):
            href = str(a['href']).split('#')[0].strip()
            if not href or href.startswith('javascript:'):
                continue
            abs_url = urljoin(base_url, href)
            if abs_url not in seen and self._same_guide(abs_url, base_url):
                seen.add(abs_url)
                if _content_type(abs_url) == 'html':
                    result.append(abs_url)
        return result

    def fetch_html_guide(self, base_url: str) -> tuple[str, str] | None:
        print(f'\n  Crawling guide: {base_url}')
        visited: set[str] = set()
        queue:   list[str] = [base_url]
        pages:   list[tuple[str, BeautifulSoup]] = []
        md_filename: str | None = None

        while queue and len(visited) < self.max_pages:
            url = queue.pop(0)
            if url in visited:
                continue
            visited.add(url)

            raw_path = RAW_HTML_DIR / _raw_name(url, 'html')
            data = self._cached_or_fetch(url, raw_path)
            if data is None:
                continue

            soup = BeautifulSoup(data, 'html.parser')

            if url == base_url:
                tag = soup.find('title')
                if tag and urlparse(base_url).netloc != 'intersight.com':
                    title = re.sub(r'\s*-\s*Cisco\s*$', '', tag.get_text(strip=True),
                                   flags=re.IGNORECASE).strip()
                    md_filename = ucsfileprefix + _title_to_filename(title) if title else None
                if not md_filename:
                    md_filename = ucsfileprefix + _url_slug(base_url) + '.md'
                print(f'  filename: {md_filename}')

            pages.append((url, soup))
            new_links = [l for l in self._collect_links(soup, base_url)
                         if l not in visited and l not in queue]
            if new_links:
                print(f'  found {len(new_links)} sub-page(s) from {url}')
            queue.extend(new_links)

        if not pages:
            return None

        md = _md_header(base_url)
        for i, (url, soup) in enumerate(pages, 1):
            md += f'## Page {i}: {url}\n\n'
            md += _clean_markdown(_H2T.handle(self._extract_body(soup)))
            md += '\n\n---\n\n'

        print(f'  converted {len(pages)} page(s)')
        return md_filename or (ucsfileprefix + _url_slug(base_url) + '.md'), _clean_markdown(md)

    # ------------------------------------------------------------------
    # PDF
    # ------------------------------------------------------------------

    def fetch_pdf(self, url: str) -> tuple[str, str] | None:
        print(f'\n  Fetching PDF: {url}')
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
        return ucsfileprefix + _url_slug(url) + '.md', md

    # ------------------------------------------------------------------
    # JSON
    # ------------------------------------------------------------------

    def fetch_json(self, url: str) -> tuple[str, str] | None:
        print(f'\n  Fetching JSON: {url}')
        raw_path = RAW_JSON_DIR / _raw_name(url, 'json')
        data = self._cached_or_fetch(url, raw_path, {'Accept': 'application/json'})
        if data is None:
            return None
        md = _md_header(url)
        try:
            parsed = try_load_json(str(raw_path))
            md += json_to_md(parsed) + '\n\n'
            md += ('<details><summary>Raw JSON</summary>\n\n```json\n'
                   + json.dumps(parsed, ensure_ascii=False, indent=2)
                   + '\n```\n\n</details>\n')
        except Exception as exc:
            print(f'  WARNING: could not parse JSON ({exc}); embedding raw')
            md += '```json\n' + data.decode('utf-8', errors='replace') + '\n```\n'
        return ucsfileprefix + _url_slug(url) + '.md', md

    # ------------------------------------------------------------------
    # Other / unknown
    # ------------------------------------------------------------------

    def fetch_other(self, url: str) -> tuple[str, str] | None:
        print(f'\n  Fetching (other): {url}')
        raw_path = RAW_OTHER_DIR / _raw_name(url, 'other')
        data = self._cached_or_fetch(url, raw_path)
        if data is None:
            return None
        md = _md_header(url)
        for enc in ('utf-8', 'latin-1'):
            try:
                text = data.decode(enc)
                ext  = os.path.splitext(_url_slug(url))[1].lstrip('.')
                md  += f'```{ext}\n{text}\n```\n'
                break
            except UnicodeDecodeError:
                continue
        else:
            md += f'*Binary file ({len(data):,} bytes) — no text representation.*\n'
        return ucsfileprefix + _url_slug(url) + '.md', md

    # ------------------------------------------------------------------
    # Dispatch
    # ------------------------------------------------------------------

    def process_url(self, url: str) -> bool:
        """Process one URL.  Returns True if a network request was made."""
        parsed = urlparse(url)

        # Intersight: all help pages use CDN route resolution
        if parsed.netloc == 'intersight.com' and '/help/' in parsed.path:
            slug     = _intersight_url_slug(url)
            html_p   = RAW_HTML_DIR / f'{slug}.html'
            md_p     = self.out_dir / f'{slug}.md'
            # For model-only pages check the .md; for CDN pages check the .html
            cache_p  = md_p if _intersight_model_key(url) else html_p
            if _is_fresh(cache_p) and not self.force:
                print('  ⏭  skipping (cached)')
                return False
            result = self.fetch_intersight_guide(url)
        else:
            ctype    = _content_type(url)
            raw_path = _RAW_DIRS[ctype] / _raw_name(url, ctype)
            if _is_fresh(raw_path) and not self.force:
                print('  ⏭  skipping (cached)')
                return False
            handler = {'html':  self.fetch_html_guide,
                       'pdf':   self.fetch_pdf,
                       'json':  self.fetch_json,
                       'other': self.fetch_other}[ctype]
            result = handler(url)

        if result is None:
            print(f'  ✗  failed: {url}')
            self._failures.append({'url': url, 'reason': 'fetch failed'})
            return True

        md_filename, content = result
        out_path = self.out_dir / md_filename
        out_path.write_text(content, encoding='utf-8')
        print(f'  ✓  {out_path}')
        return True

    def process_urls_file(self, filepath: str) -> None:
        urls = _extract_urls(filepath)
        print(f'Found {len(urls)} URL(s) in {filepath}')

        for i, url in enumerate(urls, 1):
            print(f'\n{"="*72}')
            print(f'[{i}/{len(urls)}] {url}')
            print('=' * 72)
            try:
                fetched = self.process_url(url)
            except Exception as exc:
                print(f'  ✗  unhandled error: {exc}')
                traceback.print_exc()
                fetched = True
            if fetched and i < len(urls):
                time.sleep(self.delay * 2)

        # Write failure report
        failed_path = Path('urls-failed.md')
        with open(failed_path, 'w', encoding='utf-8') as fh:
            fh.write('# Failed URLs\n\n')
            fh.write(f'*Run: {time.strftime("%Y-%m-%d %H:%M:%S")}*  '
                     f'— {len(self._failures)} failure(s)\n\n')
            if not self._failures:
                fh.write('*(no failures)*\n')
            else:
                for i, fail in enumerate(self._failures, 1):
                    fh.write(f'## {i}. {fail["url"]}\n\n'
                             f'- **URL:** {fail["url"]}\n'
                             f'- **Reason:** {fail["reason"]}\n\n---\n\n')
        print(f'\nFailed URLs → {failed_path} ({len(self._failures)} failure(s))')
        print(f'Done. Processed {len(urls)} URL(s).')


# ---------------------------------------------------------------------------
# URL extraction
# ---------------------------------------------------------------------------

def _extract_urls(filepath: str) -> list[str]:
    urls: list[str] = []
    with open(filepath, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            for _, url in re.findall(r'\[([^\]]*)\]\(([^)]+)\)', line):
                urls.append(url)
            for url in re.findall(r'(?<![\(\[])(https?://[^\s\)\]]+)', line):
                urls.append(url)
    return list(OrderedDict.fromkeys(urls))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    import argparse
    p = argparse.ArgumentParser(
        description='Fetch Cisco UCS/Intersight documentation and convert to Markdown.')
    p.add_argument('urls_file',    nargs='?', default=urlsfile,
                   help='Markdown file containing URLs (default: urls.md)')
    p.add_argument('-o', '--output-dir', default=str(MD_OUT_DIR),
                   help=f'Markdown output directory (default: {MD_OUT_DIR})')
    p.add_argument('-d', '--delay', type=float, default=1.0,
                   help='Seconds between requests (default: 1.0)')
    p.add_argument('--max-pages',  type=int,   default=200,
                   help='Max pages per HTML guide (default: 200)')
    p.add_argument('-f', '--force', action='store_true',
                   help='Re-download everything, ignoring cache')
    args = p.parse_args()

    if args.force:
        print('⚠  Force mode: ignoring all cached files')

    DocFetcher(
        out_dir   = Path(args.output_dir),
        delay     = args.delay,
        max_pages = args.max_pages,
        force     = args.force,
    ).process_urls_file(args.urls_file)


if __name__ == '__main__':
    main()
