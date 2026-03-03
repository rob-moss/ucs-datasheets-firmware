#!/usr/bin/env python3
# v5
"""
Fetch Cisco UCS documentation pages and convert to Markdown.

For each URL in urls.md:
  - HTML  → crawl all sub-pages, combine into one .md file in ./ucs-docs/
  - PDF   → extract text, save as .md in ./ucs-docs/
  - JSON  → render as table/list, save as .md in ./ucs-docs/
  - other → wrap raw text in a fenced block, save as .md in ./ucs-docs/

Raw downloads are cached in ./ucs-docs-raw/{html,pdf,json,other}/.
Files fetched within the last 24 hours are skipped unless --force is set.

Intersight URLs are JS-rendered SPAs fetched via the Cisco CDN (no JS needed):
  1. A cached CDN version string (~/.intersight_cdn_version, 7-day TTL) is validated
     with a HEAD request.  On a cache miss the home page is scraped for the version.
  2. A 403 on any CDN doc page is a non-fatal skip.

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

# Intersight
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

_H2T = html2text.HTML2Text()
_H2T.ignore_links = False
_H2T.ignore_images = False
_H2T.body_width = 0

_SESSION = requests.Session()
_SESSION.headers['User-Agent'] = (
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# Intersight CDN version helpers
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
    url = f'{_IS_CDN_BASE}/{version}/model/en/onprem-model.json'
    try:
        return _SESSION.head(url, timeout=10, allow_redirects=True).status_code == 200
    except Exception:
        return False


def _extract_cdn_version(html: str) -> str | None:
    m = re.search(r'cdn\.intersight\.com/components/an-hulk/([^/"\' ]+)/', html)
    return m.group(1) if m else None


# ---------------------------------------------------------------------------
# Core fetcher
# ---------------------------------------------------------------------------

class DocFetcher:
    def __init__(
        self,
        out_dir:   Path  = MD_OUT_DIR,
        delay:     float = 1.0,
        max_pages: int   = 200,
        force:     bool  = False,
    ):
        self.out_dir   = out_dir
        self.delay     = delay
        self.max_pages = max_pages
        self.force     = force
        self._cdn_base: str | None = None   # resolved once per run
        self._cdn_init = False              # True once resolution has been attempted
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

        # 2. Scrape the Intersight home page
        print(f'  [IS] Fetching {_IS_HOME} for CDN version …')
        try:
            resp = _SESSION.get(_IS_HOME, timeout=30, headers=_IS_HEADERS)
            if not resp.ok:
                print(f'  [IS] WARNING: home page returned HTTP {resp.status_code}')
                return
            version = _extract_cdn_version(resp.text)
            if version:
                _save_cdn_version(version)
                self._cdn_base = f'{_IS_CDN_BASE}/{version}'
                print(f'  [IS] CDN version (home page): {version}')
                return
        except Exception as exc:
            print(f'  [IS] WARNING: could not fetch home page – {exc}')

        print('  [IS] WARNING: CDN version unavailable – Intersight URLs will be skipped.')

    def _resolve_cdn_doc_url(self, topic: str, section: str) -> str | None:
        """Probe the two section-casing variants and return the live URL."""
        if not self._cdn_base:
            return None
        for sec in dict.fromkeys([section.capitalize(), section]):   # dedup
            url = (f'{self._cdn_base}/docs/cloud/data/articles/features'
                   f'/{topic}/{sec}/en/index.html')
            print(f'  [IS] HEAD probe: {url}')
            try:
                if _SESSION.head(url, timeout=10, headers=_IS_HEADERS,
                                 allow_redirects=True).status_code == 200:
                    print(f'  [IS] Resolved: {url}')
                    return url
            except Exception:
                pass
        print(f'  [IS] WARNING: no working CDN URL for {topic}/{section}')
        return None

    # ------------------------------------------------------------------
    # Intersight guide
    # ------------------------------------------------------------------

    @staticmethod
    def _parse_is_url(url: str) -> dict | None:
        """Parse https://intersight.com/help/<variant>/<section>/<topic>."""
        parts = [p for p in urlparse(url).path.strip('/').split('/') if p]
        if len(parts) < 4 or parts[0] != 'help':
            return None
        return {'variant': parts[1], 'section': parts[2], 'topic': parts[3]}

    def fetch_intersight_guide(self, is_url: str) -> tuple[str, str] | None:
        info = self._parse_is_url(is_url)
        if info is None:
            return self.fetch_html_guide(is_url)

        variant, section, topic = info['variant'], info['section'], info['topic']
        stem = f'intersight-{variant}-{section}_{topic}'
        raw_path = RAW_HTML_DIR / f'{stem}.html'

        if _is_fresh(raw_path) and not self.force:
            print(f'  ⏭  cached: {raw_path.name}')
            doc_html = raw_path.read_text(encoding='utf-8')
        else:
            self._ensure_cdn()
            doc_url = self._resolve_cdn_doc_url(topic, section)
            if not doc_url:
                self._failures.append({'url': is_url, 'reason': 'CDN URL not found'})
                return None
            data = self._get(doc_url, _IS_HEADERS)
            if data is None:
                self._failures.append({'url': is_url, 'reason': 'HTTP 403 / fetch error'})
                return None
            doc_html = data.decode('utf-8', errors='replace')
            raw_path.write_text(doc_html, encoding='utf-8')
            print(f'  [IS] cached HTML → {raw_path}')

        soup = BeautifulSoup(doc_html, 'html.parser')
        content = (soup.select_one('article, [role="main"], main, .content, #content')
                   or soup.find('body') or soup)
        page_md = _clean_markdown(_H2T.handle(str(content)))

        title = soup.find('title')
        heading = title.get_text(strip=True) if title else f'{section} {topic}'
        md = (f'# {heading}\n\n'
              f'> IS URL: {is_url}\n'
              f'*Fetched on: {time.strftime("%Y-%m-%d %H:%M:%S")}*\n\n'
              '---\n\n') + page_md
        return f'{stem}.md', md

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
                # Derive filename from <title>
                tag = soup.find('title')
                if tag and urlparse(base_url).netloc != 'intersight.com':
                    title = re.sub(r'\s*-\s*Cisco\s*$', '', tag.get_text(strip=True),
                                   flags=re.IGNORECASE).strip()
                    md_filename = _title_to_filename(title) if title else None
                if not md_filename:
                    md_filename = _is_prefix(base_url) + _url_slug(base_url) + '.md'
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
        return md_filename or (_url_slug(base_url) + '.md'), _clean_markdown(md)

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
        return _url_slug(url) + '.md', md

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
        return _url_slug(url) + '.md', md

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
        return _url_slug(url) + '.md', md

    # ------------------------------------------------------------------
    # Dispatch
    # ------------------------------------------------------------------

    def process_url(self, url: str) -> bool:
        """Process one URL.  Returns True if a network request was made."""
        if urlparse(url).netloc == 'intersight.com' and self._parse_is_url(url):
            info  = self._parse_is_url(url)
            stem  = f'intersight-{info["variant"]}-{info["section"]}_{info["topic"]}'
            if _is_fresh(RAW_HTML_DIR / f'{stem}.html') and not self.force:
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
    p.add_argument('urls_file',    nargs='?', default='urls.md',
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
