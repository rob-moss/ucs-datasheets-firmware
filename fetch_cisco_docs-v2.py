#!/usr/bin/env python3
# v11 fetch_cisco_docs-v2.py
# Inline json_to_markdown functions; single-file, no external module dependency.
# v2 changes vs v10:
#   - Tighter Markdown output: strips leading indent from list items, removes
#     blank lines between consecutive list items, collapses excess blank lines.
#   - Removes boilerplate: search widgets, feedback prompts, nav-only headings,
#     and other chrome that html2text converts to noise.
#   - html2text configured to ignore images and mark code blocks.
# See commit history for earlier changes.
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
  1. The CDN version is scraped live from https://intersight.com/help/saas on
     every run (no disk cache).
  2. URL Routes changed
     SaaS routes are built from {CDN_BASE}/model/en/cloud-model.json.
     Appliance routes are built from {CDN_BASE}/model/en/onprem-model.json.
     Both model files are fetched dynamically using the same resolved CDN version.
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
from typing import Any
from urllib.parse import urljoin, urlparse, unquote

import html2text
from bs4 import BeautifulSoup

try:
    from pdfminer.high_level import extract_text as pdf_extract_text
    _PDF_OK = True
except ImportError:
    _PDF_OK = False
    def pdf_extract_text(*a, **kw) -> str:  # type: ignore[misc]
        return ""


# ---------------------------------------------------------------------------
# JSON → Markdown helpers (inlined from json_to_markdown.py)
# ---------------------------------------------------------------------------

def _jmd_escape(val: Any) -> str:
    """Escape characters that break Markdown tables."""
    if val is None:
        return ""
    s = str(val)
    s = s.replace("|", "\\|")
    s = s.replace("\n", "<br>")
    s = s.replace("\r", "")
    s = s.replace("`", "\\`")
    return s

def _jmd_is_list_of_dicts(lst: list) -> bool:
    return isinstance(lst, list) and len(lst) > 0 and all(isinstance(x, dict) for x in lst)

def _jmd_is_list_of_scalars(lst: list) -> bool:
    return isinstance(lst, list) and all(not isinstance(x, (dict, list)) for x in lst)

def _jmd_collect_keys(rows: list[dict]) -> list[str]:
    keys: set[str] = set()
    for r in rows:
        keys.update(r.keys())
    return sorted(keys)

def _jmd_to_inline(value: Any) -> str:
    """Render nested values as inline JSON snippet or plain string for scalars."""
    if isinstance(value, (dict, list)):
        try:
            return _jmd_escape(json.dumps(value, ensure_ascii=False, separators=(",", ":")))
        except Exception:
            return _jmd_escape(str(value))
    return _jmd_escape(value)

def _jmd_dict_to_table(d: dict) -> str:
    lines = ["| Key | Value |", "| --- | --- |"]
    for k, v in d.items():
        lines.append(f"| {_jmd_escape(k)} | {_jmd_to_inline(v)} |")
    return "\n".join(lines)

def _jmd_list_of_dicts_to_table(rows: list[dict]) -> str:
    headers = _jmd_collect_keys(rows)
    if not headers:
        return "_(empty list)_"
    head = "| " + " | ".join(_jmd_escape(h) for h in headers) + " |"
    sep  = "| " + " | ".join("---" for _ in headers) + " |"
    out  = [head, sep]
    for r in rows:
        row = [_jmd_to_inline(r.get(h, "")) for h in headers]
        out.append("| " + " | ".join(row) + " |")
    return "\n".join(out)

def _jmd_list_of_scalars_to_md(lst: list) -> str:
    return "\n".join(f"- {_jmd_escape(x)}" for x in lst)

def json_to_md(data: Any) -> str:
    """Convert a JSON-decoded value to a Markdown table or list."""
    if isinstance(data, dict):
        return _jmd_dict_to_table(data)
    if isinstance(data, list):
        if _jmd_is_list_of_dicts(data):
            return _jmd_list_of_dicts_to_table(data)
        if _jmd_is_list_of_scalars(data):
            return _jmd_list_of_scalars_to_md(data)
        # Mixed/complex list → fenced code block
        return "```json\n" + json.dumps(data, ensure_ascii=False, indent=2) + "\n```"
    # scalar
    return _jmd_escape(data)


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

CACHE_TTL    = datetime.timedelta(hours=24)
DEFAULT_DELAY = 0.0   # seconds between HTTP requests was 0.2

# ---------------------------------------------------------------------------
# Intersight constants
# ---------------------------------------------------------------------------
_IS_HOME     = 'https://intersight.com'
_IS_CDN_BASE = 'https://cdn.intersight.com/components/an-hulk'
_IS_ONPREM_MODEL_CACHE = RAW_JSON_DIR / 'onprem-model.json'
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

# Appliance CDN path fallbacks used when onprem-model.json does not cover a route.
# These were originally confirmed via Playwright and are kept as a last resort.
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
_H2T.ignore_links  = False   # keep hyperlinks for reference
_H2T.ignore_images = True    # skip image alt-text clutter
_H2T.mark_code     = True    # wrap <code>/<pre> in backtick fences
_H2T.body_width    = 0       # no line-wrapping

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


_DYNAMIC_URL_PREFIXES = (
    'https://pwc014-nextgen-prod-rcdn.cisco.com',
)

# URLs whose responses are always JSON regardless of file extension.
# These are fetched with fetch_json (not fetch_html_guide) and with no caching.
_JSON_URL_PREFIXES = (
    'https://pwc014-nextgen-prod-rcdn.cisco.com',
)


def _is_forced_json_url(url: str) -> bool:
    """Return True for URLs that must always be fetched as JSON."""
    return any(url.startswith(p) for p in _JSON_URL_PREFIXES)


def _is_dynamic_url(url: str) -> bool:
    """Return True for URLs that must never be served from cache.

    A URL is considered dynamic if:
    - it matches a known dynamic-host prefix, or
    - its query string contains '?' or '&' (parametric/search endpoints).
    """
    if any(url.startswith(p) for p in _DYNAMIC_URL_PREFIXES):
        return True
    parsed = urlparse(url)
    return bool(parsed.query)  # non-empty query string → dynamic


def _title_to_filename(title: str) -> str:
    safe = re.sub(r'[<>:"/\\|?*]', '', title)
    safe = re.sub(r'[\s,]+', '-', safe.strip())
    safe = re.sub(r'-{2,}', '-', safe).strip('-')
    return (safe[:200] or 'document') + '.md'


def _md_header(
    url: str,
    *,
    url_title: str | None = None,
    html_title: str | None = None,
    long_url: str | None = None,
    raw_path: Path | None = None,
    file_type: str = 'HTML',
) -> str:
    """Return a standard Markdown header block with enriched metadata.

    Fields written:
      - URL Title  : label from urls.md (url_title)
      - URL        : the canonical / help URL
      - Long URL   : CDN long URL for Intersight pages (long_url)
      - HTML Title : text of the HTML <title> element, blank for non-HTML
      - Source file: cached raw file path
      - File type  : HTML / PDF / JSON / other
      - Fetched on : timestamp

    The H1 heading is url_title if set, else html_title, else the URL slug.
    """
    heading  = url_title or html_title or _url_slug(url)
    raw_file = str(raw_path) if raw_path else _url_slug(url)
    rows = [
        f'| **URL Title** | {url_title or ""} |',
        f'| **URL** | {url} |',
        f'| **Long URL** | {long_url or ""} |',
        f'| **HTML Title** | {html_title or ""} |',
        f'| **Source file** | `{raw_file}` |',
        f'| **File type** | {file_type} |',
        f'| **Fetched on** | {time.strftime("%Y-%m-%d %H:%M:%S")} |',
    ]
    table = '| | |\n|---|---|\n' + '\n'.join(rows)
    return f'# {heading}\n\n{table}\n\n---\n\n'


def _is_fresh(path: Path) -> bool:
    if not path.exists():
        return False
    age = datetime.datetime.now(tz=datetime.timezone.utc) - \
          datetime.datetime.fromtimestamp(path.stat().st_mtime, tz=datetime.timezone.utc)
    return age < CACHE_TTL


# ---------------------------------------------------------------------------
# Boilerplate line patterns stripped from converted Markdown output (v2)
# ---------------------------------------------------------------------------
_BOILERPLATE_EXACT: frozenset[str] = frozenset({
    'search', 'search documentation', 'search by keyword', 'search results',
    'search this guide', 'was this article helpful?', 'was this page helpful?',
    'table of contents', 'on this page', 'in this article',
    'please rate this article', 'please rate this content',
    'submit feedback', 'rate this page', 'helpful?',
    'yes', 'no',  # lone yes/no after feedback prompts
    'cookie policy', 'privacy statement', 'terms & conditions',
    'back to top', 'skip to main content',
})

# Regex for boilerplate lines that need pattern matching rather than exact text
_BOILERPLATE_RE = re.compile(
    r'^\s*('
    r'Search(\s+(by Keyword|Documentation|Results|this guide))?'
    r'|Was this (article|page) helpful'
    r'|Please rate this (article|content)'
    r'|Submit Feedback'
    r'|Rate this (page|article)'
    r'|Table of Contents'
    r'|On [Tt]his [Pp]age'
    r'|In [Tt]his [Aa]rticle'
    r'|Skip to (main )?[Cc]ontent'
    r'|Back to [Tt]op'
    r'|\[.*?\]\(#\)'
    r')\s*$',
    re.IGNORECASE,
)

# List-item line: optional leading whitespace, then numbered or bullet marker
_LIST_ITEM_RE = re.compile(r'^[ \t]*(\d+\.|[-*+])\s')


def _clean_markdown(md: str) -> str:  # noqa: C901
    """Post-process html2text output for tighter, cleaner Markdown.

    Applied transforms (v2):
    - Removes search widgets, feedback prompts, cookie/nav boilerplate lines.
    - Fixes '* ## Heading' artefacts → '## Heading'.
    - Strips up-to-3-space leading indent from top-level list items.
    - Normalises deep indentation on nested bullets (4+ spaces → 2-space levels).
    - Removes blank lines between consecutive list items.
    - Collapses 3+ consecutive blank lines to a single blank line.
    """
    output: list[str] = []
    for line in md.splitlines():
        # --- Hard-skip known boilerplate ---
        stripped = line.strip()
        if stripped.lower() in _BOILERPLATE_EXACT:
            continue
        if _BOILERPLATE_RE.match(line):
            continue

        # --- Fix '* ## Heading' → '## Heading' artefact from html2text ---
        if re.match(r'^\s*\*\s+(#{1,6})\s+', line):
            line = re.sub(r'^\s*\*\s+(#{1,6}\s+.+)$', r'\1', line)

        # --- Strip up-to-3-space indent from top-level list items ---
        # Handles "  1. foo", "   * bar", "  - baz" produced by html2text
        if re.match(r'^ {1,3}(\d+\.|[-*+])\s', line):
            line = line.lstrip()

        # --- Normalise deep indent on nested bullets (4-space steps → 2-space) ---
        elif re.match(r'^\s{4,}(\d+\.|[-*+])\s', line):
            n_spaces = len(line) - len(line.lstrip())
            level = n_spaces // 4
            line = '  ' * level + line.lstrip()

        output.append(line)

    joined = '\n'.join(output)

    # --- Remove blank lines between consecutive list items ---
    # A list line followed by one or more blank lines then another list line
    joined = re.sub(
        r'(?m)(^[ \t]*(\d+\.|[-*+])\s[^\n]*)(\n\n+)(?=[ \t]*(\d+\.|[-*+])\s)',
        r'\1\n',
        joined,
    )
    # A list line followed by blank lines then a nested sub-list opener
    joined = re.sub(
        r'(?m)(^[ \t]*(\d+\.|[-*+])\s[^\n]*)(\n\n+)(?=[ \t]{2,}(\d+\.|[-*+])\s)',
        r'\1\n',
        joined,
    )

    # --- Collapse 3+ consecutive blank lines to one blank line ---
    joined = re.sub(r'\n{3,}', '\n\n', joined)

    return joined.strip()


def _strip_html(raw: str) -> str:
    return BeautifulSoup(raw, 'html.parser').get_text(' ', strip=True)


_UCS_PATH_KEYWORDS = ('unified_computing', 'ucs', 'ucs-manager', 'servers-unified-computing')


def _md_outname(url: str, title: str | None = None) -> str:
    """
    Determine the output .md filename for *url*.

    - intersight.com/help  → isfileprefix + slug
    - *.cisco.com + a UCS path keyword → ucsfileprefix + title-derived name (or slug)
    - everything else      → title-derived name (or slug), no prefix
    """
    parsed = urlparse(url)
    netloc = parsed.netloc
    path = parsed.path
    slug_stem = os.path.splitext(_url_slug(url))[0]  # strip any .html/.pdf etc.

    # Intersight help pages
    if 'intersight.com' in netloc and path.startswith('/help'):
        return isfileprefix + slug_stem + '.md'

    # Cisco UCS pages — path must contain at least one UCS-related keyword
    if 'cisco.com' in netloc and any(kw in path for kw in _UCS_PATH_KEYWORDS):
        stem = _title_to_filename(title) if title else (slug_stem + '.md')
        return ucsfileprefix + stem

    # Everything else: use title if available, else bare slug
    if title:
        return _title_to_filename(title)
    return slug_stem + '.md'


# ---------------------------------------------------------------------------
# Intersight CDN helpers
# ---------------------------------------------------------------------------

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
    Build URL-key -> CDN long-URL mapping from cloud-model.json.
    Keys match the path after /help/ (saas section only).
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

    # Special "whats_new" route — the node in model['menu'] has no data/folder,
    # but model['whats_new'] lists released items with explicit folder names.
    # Use the first 'released' entry's first item folder (most recent year).
    for wn_entry in model.get('whats_new', []):
        if wn_entry.get('type') == 'released':
            items = (wn_entry.get('data') or {}).get('items', [])
            if items:
                folder = items[0].get('folder', '')
                if folder:
                    routes['whats_new'] = cdn_url(folder, 'index.html', 'articles')
            break

    return routes


def _build_onprem_routes(cdn_base: str, model: dict) -> dict[str, str]:
    """
    Build URL-key -> CDN long-URL mapping from onprem-model.json.
    Keys match the path after /help/ (e.g. 'appliance/settings').
    The model is walked with an 'appliance/' prefix so route keys align
    with Intersight help URL paths.
    _IS_APPLIANCE_FALLBACKS are inserted for any key not found in the model.
    """
    routes: dict[str, str] = {}

    def cdn_url(folder: str, file_name: str | None = None,
                resource: str = 'articles') -> str:
        return f"{cdn_base}/docs/onprem/data/{resource}/{folder}/{file_name or 'index.html'}"

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

    # Article routes, prefixed with 'appliance/' to match /help/appliance/... URLs
    for art in model.get('articles', []):
        walk(art, 'appliance')

    # Resource routes for appliance
    for res in model.get('resources', []):
        folder = res.get('folder', '')
        for doc in res.get('docs', []):
            link, name = doc.get('link', ''), doc.get('name', '')
            if link and name:
                routes[link.lower()] = cdn_url(folder, name, 'resources')

    # Fill in any gaps with the hardcoded fallbacks
    for key, path in _IS_APPLIANCE_FALLBACKS.items():
        if key not in routes:
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
        delay:     float = DEFAULT_DELAY,
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
        self._routes: dict | None = None    # SaaS CDN route table (cloud-model.json)
        self._onprem_model:  dict | None = None   # onprem-model.json, loaded once
        self._onprem_routes: dict | None = None   # Appliance CDN route table (onprem-model.json)
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
        if _is_dynamic_url(url):
            print(f'  ↻  dynamic (no cache): {url}')
        elif _is_fresh(raw_path) and not self.force:
            print(f'  ⏭  cached: {raw_path.name}')
            return raw_path.read_bytes()
        data = self._get(url, headers)
        if data is not None:
            if not _is_dynamic_url(url):
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

        # Scrape the Intersight help page for CDN version
        print(f'  [IS] Fetching https://intersight.com/help/saas for CDN version …')
        try:
            resp = _SESSION.get('https://intersight.com/help/saas',
                                timeout=30, headers=_IS_HEADERS)
            if not resp.ok:
                print(f'  [IS] WARNING: help page returned HTTP {resp.status_code}')
                return
            version = _extract_cdn_version(resp.text)
            if version:
                self._cdn_base = f'{_IS_CDN_BASE}/{version}'
                print(f'  [IS] CDN version: {version}')
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
        cache = RAW_JSON_DIR / 'cloud-model.json'
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
            RAW_JSON_DIR.mkdir(parents=True, exist_ok=True)
            cache.write_text(json.dumps(self._model, indent=2), encoding='utf-8')
            print(f'  [IS] Cached → {cache}')

        assert self._model is not None
        self._routes = _build_intersight_routes(self._cdn_base, self._model)
        print(f'  [IS] {len(self._routes)} saas routes built')

    def _ensure_onprem_model_routes(self) -> None:
        """Load onprem-model.json and build appliance routes, at most once per instance."""
        if self._onprem_routes is not None:
            return
        if not self._cdn_base:
            self._onprem_routes = {}
            return

        # Load onprem model (cached to disk)
        cache = _IS_ONPREM_MODEL_CACHE
        if cache.exists() and not self.force:
            print(f'  [IS] Using cached {cache.name}')
            self._onprem_model = json.loads(cache.read_text(encoding='utf-8'))
        else:
            url = f'{self._cdn_base}/model/en/onprem-model.json'
            print(f'  [IS] Fetching {url}')
            data = self._get(url, {**_IS_HEADERS, 'Accept': 'application/json'})
            if data is None:
                print('  [IS] WARNING: could not load onprem-model.json – '
                      'falling back to _IS_APPLIANCE_FALLBACKS only.')
                self._onprem_routes = {
                    k: f'{self._cdn_base}/{v}'
                    for k, v in _IS_APPLIANCE_FALLBACKS.items()
                }
                return
            self._onprem_model = json.loads(data.decode('utf-8'))
            cache.write_text(json.dumps(self._onprem_model, indent=2), encoding='utf-8')
            print(f'  [IS] Cached → {cache}')

        assert self._onprem_model is not None
        self._onprem_routes = _build_onprem_routes(self._cdn_base, self._onprem_model)
        print(f'  [IS] {len(self._onprem_routes)} appliance routes built')

    # ------------------------------------------------------------------
    # Intersight guide
    # ------------------------------------------------------------------

    def fetch_intersight_guide(self, is_url: str, title: str | None = None) -> tuple[str, str] | None:
        self._ensure_cdn()

        # Choose the correct model/routes based on URL variant
        is_appliance = urlparse(is_url).path.startswith('/help/appliance')
        if is_appliance:
            self._ensure_onprem_model_routes()
            active_routes = self._onprem_routes or {}
        else:
            self._ensure_model_routes()
            active_routes = self._routes or {}

        slug = _intersight_url_slug(is_url)
        raw_path = RAW_HTML_DIR / f'{slug}.html'
        md_path  = self.out_dir / f'{slug}.md'

        # --- Client-rendered model-data page (no CDN HTML) ---
        model_key = _intersight_model_key(is_url)
        if model_key:
            if not self._model:
                self._failures.append({'url': is_url, 'reason': 'model not loaded'})
                return None
            raw_content = _model_to_markdown(self._model, model_key)
            # Extract the H1 from model content so _md_header owns the heading
            lines = raw_content.splitlines()
            model_title: str | None = None
            body_start = 0
            if lines and lines[0].startswith('# '):
                model_title = lines[0][2:].strip()
                body_start = 2 if len(lines) > 1 and not lines[1].strip() else 1
            body = '\n'.join(lines[body_start:])
            header = _md_header(is_url, url_title=title, html_title=model_title,
                                raw_path=None, file_type='HTML')
            print(f'  [IS] [model:{model_key}] → {md_path.name}')
            return md_path.name, header + body

        # --- CDN HTML page ---
        # Resolve the CDN URL now (pure lookup) so it is available as long_url
        # both when fetching fresh and when serving from cache.
        cdn_url = _resolve_intersight_url(is_url, active_routes)

        if _is_fresh(raw_path) and not self.force:
            print(f'  ⏭  cached: {raw_path.name}')
            doc_html = raw_path.read_text(encoding='utf-8')
        else:
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
        content_node = (soup.select_one('article, [role="main"], main, .content, #content')
                        or soup.find('body') or soup)
        page_md = _clean_markdown(_H2T.handle(str(content_node)))

        title_tag  = soup.find('title')
        html_title = title_tag.get_text(strip=True) if title_tag else slug.replace('_', ' ').title()

        md = _md_header(
            is_url,
            url_title  = title,
            html_title = html_title,
            long_url   = cdn_url,
            raw_path   = raw_path,
            file_type  = 'HTML',
        ) + page_md
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

    def fetch_html_guide(self, base_url: str,
                         title: str | None = None) -> tuple[str, str] | None:
        """Crawl *base_url* and all sub-pages, returning (filename, markdown).

        *title* is the label from urls.md (if any).  The fetched HTML <title>
        element takes precedence; the urls.md label is used as a fallback so
        the MD header always has a meaningful heading.
        """
        print(f'\n  Crawling guide: {base_url}')
        visited: set[str] = set()
        queue:   list[str] = [base_url]
        pages:   list[tuple[str, BeautifulSoup]] = []
        md_filename: str | None = None
        page_title:  str | None = None  # populated from the base page <title>

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
                if tag:
                    t = tag.get_text(strip=True)
                    if 'cisco.com' in urlparse(base_url).netloc:
                        t = re.sub(r'\s*-\s*Cisco\s*$', '', t, flags=re.IGNORECASE).strip()
                    page_title = t or None
                # HTML <title> wins; fall back to urls.md label
                best_title = page_title or title
                md_filename = _md_outname(base_url, best_title)
                print(f'  filename: {md_filename}')

            pages.append((url, soup))
            new_links = [lnk for lnk in self._collect_links(soup, base_url)
                         if lnk not in visited and lnk not in queue]
            if new_links:
                print(f'  found {len(new_links)} sub-page(s) from {url}')
            queue.extend(new_links)

        if not pages:
            return None

        first_raw  = RAW_HTML_DIR / _raw_name(base_url, 'html')
        md = _md_header(
            base_url,
            url_title  = title,
            html_title = page_title,
            raw_path   = first_raw,
            file_type  = 'HTML',
        )
        for i, (url, soup) in enumerate(pages, 1):
            md += f'## Page {i}: {url}\n\n'
            md += _clean_markdown(_H2T.handle(self._extract_body(soup)))
            md += '\n\n---\n\n'

        print(f'  converted {len(pages)} page(s)')
        assert md_filename is not None
        return md_filename, _clean_markdown(md)

    # ------------------------------------------------------------------
    # PDF
    # ------------------------------------------------------------------

    def fetch_pdf(self, url: str, title: str | None = None) -> tuple[str, str] | None:
        """Fetch a PDF and convert to Markdown.

        *title* is the label from urls.md (if any) and becomes the H1 heading.
        """
        print(f'\n  Fetching PDF: {url}')
        raw_path = RAW_PDF_DIR / _raw_name(url, 'pdf')
        data = self._cached_or_fetch(url, raw_path)
        if data is None:
            return None
        md = _md_header(
            url,
            url_title  = title,
            raw_path   = raw_path,
            file_type  = 'PDF',
        )
        if not _PDF_OK:
            md += '*pdfminer.six not installed — run `pip install pdfminer.six`.*\n'
        else:
            try:
                md += pdf_extract_text(io.BytesIO(data)) or '*(no text extracted)*'
            except Exception as exc:
                md += f'*PDF extraction error: {exc}*\n'
        return _md_outname(url, title), md

    # ------------------------------------------------------------------
    # JSON
    # ------------------------------------------------------------------

    def fetch_json(self, url: str, title: str | None = None) -> tuple[str, str] | None:
        """Fetch a JSON resource and render as Markdown.

        *title* is the label from urls.md (if any) and becomes the H1 heading.
        """
        print(f'\n  Fetching JSON: {url}')
        raw_path = RAW_JSON_DIR / _raw_name(url, 'json')
        json_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        data = self._cached_or_fetch(url, raw_path, json_headers)
        if data is None:
            return None
        md = _md_header(
            url,
            url_title  = title,
            raw_path   = raw_path,
            file_type  = 'JSON',
        )
        try:
            text = data.decode('utf-8').strip()
            try:
                parsed = json.loads(text)
            except Exception:
                # Try JSON Lines (.jsonl)
                lines = [ln for ln in text.splitlines() if ln.strip()]
                parsed = [json.loads(ln) for ln in lines]
            md += json_to_md(parsed) + '\n\n'
            md += ('<details><summary>Raw JSON</summary>\n\n```json\n'
                   + json.dumps(parsed, ensure_ascii=False, indent=2)
                   + '\n```\n\n</details>\n')
        except Exception as exc:
            print(f'  WARNING: could not parse JSON ({exc}); embedding raw')
            md += '```json\n' + data.decode('utf-8', errors='replace') + '\n```\n'
        # Use URL title from urls.md (ensures unique names for same-path URLs)
        if title:
            md_filename = 'json-' + _title_to_filename(title)
        else:
            md_filename = 'json-' + _md_outname(url)
        return md_filename, md

    # ------------------------------------------------------------------
    # Other / unknown
    # ------------------------------------------------------------------

    def fetch_other(self, url: str, title: str | None = None) -> tuple[str, str] | None:
        """Fetch an unknown resource and wrap as a fenced code block.

        *title* is the label from urls.md (if any) and becomes the H1 heading.
        """
        print(f'\n  Fetching (other): {url}')
        raw_path = RAW_OTHER_DIR / _raw_name(url, 'other')
        data = self._cached_or_fetch(url, raw_path)
        if data is None:
            return None
        ext = os.path.splitext(_url_slug(url))[1].lstrip('.').upper() or 'other'
        md = _md_header(
            url,
            url_title  = title,
            raw_path   = raw_path,
            file_type  = ext,
        )
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
        return _md_outname(url, title), md

    # ------------------------------------------------------------------
    # Dispatch
    # ------------------------------------------------------------------

    def process_url(self, url: str, title: str | None = None) -> bool:
        """Process one URL.  Returns True if a network request was made."""
        parsed = urlparse(url)

        # Intersight: all help pages use CDN route resolution
        if parsed.netloc == 'intersight.com' and '/help/' in parsed.path:
            result = self.fetch_intersight_guide(url, title=title)
        elif _is_forced_json_url(url):
            # Force JSON fetch regardless of URL path/extension
            result = self.fetch_json(url, title=title)
        else:
            ctype = _content_type(url)
            if ctype == 'json':
                result = self.fetch_json(url, title=title)
            elif ctype == 'pdf':
                result = self.fetch_pdf(url, title=title)
            elif ctype == 'html':
                result = self.fetch_html_guide(url, title=title)
            else:
                result = self.fetch_other(url, title=title)

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
        entries = _extract_urls(filepath)
        print(f'Found {len(entries)} URL(s) in {filepath}')

        for i, (url, title) in enumerate(entries, 1):
            print(f'\n{"="*72}')
            print(f'[{i}/{len(entries)}] {url}')
            if title:
                print(f'  title: {title}')
            print('=' * 72)
            try:
                fetched = self.process_url(url, title=title)
            except Exception as exc:
                print(f'  ✗  unhandled error: {exc}')
                traceback.print_exc()
                fetched = True
            if fetched and i < len(entries):
                time.sleep(self.delay)

        if self._failures:
            print(f'\n{"="*72}')
            print(f'Failed URLs ({len(self._failures)} failure(s)):')
            for fail in self._failures:
                print(f'  ✗  {fail["url"]} → {fail["reason"]}')

        print(f'\nDone. Processed {len(entries)} URL(s), {len(self._failures)} failure(s).')


# ---------------------------------------------------------------------------
# URL extraction
# ---------------------------------------------------------------------------

def _extract_urls(filepath: str) -> list[tuple[str, str | None]]:
    """Return a list of (url, title) pairs extracted from a Markdown file.

    Markdown link syntax ``[title](url)`` captures the title; bare URLs get
    ``None`` as their title.  Duplicates are removed (first occurrence wins).
    """
    entries: OrderedDict[str, str | None] = OrderedDict()
    with open(filepath, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            for link_title, url in re.findall(r'\[([^\]]*)\]\(([^)]+)\)', line):
                if url not in entries:
                    entries[url] = link_title.strip() or None
            for url in re.findall(r'(?<![\(\[])(https?://[^\s\)\]]+)', line):
                if url not in entries:
                    entries[url] = None
    return list(entries.items())


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
    p.add_argument('-d', '--delay', type=float, default=DEFAULT_DELAY,
                   help=f'Seconds between requests (default: {DEFAULT_DELAY})')
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
