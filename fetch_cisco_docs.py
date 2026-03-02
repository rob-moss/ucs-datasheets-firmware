#!/usr/bin/env python3
# v3
"""
Fetch Cisco UCS documentation pages recursively and convert to Markdown.

This script:
1. Reads URLs from urls.md (in the project root)
2. For HTML pages:
   - Saves each raw HTML file to ./ucs-docs-raw/html/
   - Fetches the main page and all linked sub-pages recursively
   - Combines everything into a single Markdown file named from the <title> tag
   - Saves the Markdown file to ./ucs-docs/
3. For PDF files:
   - Saves the raw PDF to ./ucs-docs-raw/pdf/
   - Converts text to Markdown and saves to ./ucs-docs/
4. For JSON files:
   - Saves the raw JSON to ./ucs-docs-raw/json/
   - Formats as a fenced code block Markdown and saves to ./ucs-docs/

Directory defaults:
    DEFAULT_HTML_RAW_DIR  = './ucs-docs-raw/html'
    DEFAULT_PDF_RAW_DIR   = './ucs-docs-raw/pdf'
    DEFAULT_JSON_RAW_DIR  = './ucs-docs-raw/json'
    DEFAULT_MARKDOWN_DIR  = './ucs-docs'

Dependencies (pip install):
    requests beautifulsoup4 html2text pdfminer.six
"""

import io
import json
import os
import re
import time
import datetime
import email.utils
import requests
from urllib.parse import urljoin, urlparse, unquote
from bs4 import BeautifulSoup
from pathlib import Path
import html2text
from collections import OrderedDict
from json_to_markdown import (
    value_to_markdown as _json_value_to_markdown,
    try_load_json as _json_try_load,
)

try:
    from pdfminer.high_level import extract_text as pdf_extract_text
    _PDFMINER_AVAILABLE = True
except ImportError:
    _PDFMINER_AVAILABLE = False

    def pdf_extract_text(*args, **kwargs) -> str:  # type: ignore[misc]
        return ""


# Default directory paths
DEFAULT_HTML_RAW_DIR  = './ucs-docs-raw/html'
DEFAULT_PDF_RAW_DIR   = './ucs-docs-raw/pdf'
DEFAULT_JSON_RAW_DIR  = './ucs-docs-raw/json'
DEFAULT_OTHER_RAW_DIR = './ucs-docs-raw/other'
DEFAULT_MARKDOWN_DIR  = './ucs-docs'


class CiscoDocFetcher:
    def __init__(
        self,
        markdown_dir=DEFAULT_MARKDOWN_DIR,
        html_raw_dir=DEFAULT_HTML_RAW_DIR,
        pdf_raw_dir=DEFAULT_PDF_RAW_DIR,
        json_raw_dir=DEFAULT_JSON_RAW_DIR,
        other_raw_dir=DEFAULT_OTHER_RAW_DIR,
        delay=1.0,
        force=False,
    ):
        """
        Initialize the documentation fetcher.

        Args:
            markdown_dir:  Directory where converted Markdown files are written.
            html_raw_dir:  Directory where raw HTML files are saved before conversion.
            pdf_raw_dir:   Directory where raw PDF files are saved before conversion.
            json_raw_dir:  Directory where raw JSON files are saved before conversion.
            other_raw_dir: Directory where raw files of unrecognised types are saved.
            delay:         Delay between requests in seconds (be respectful).
            force:         Skip all freshness checks and re-download every file.
        """
        self.output_dir    = Path(markdown_dir)
        self.html_raw_dir  = Path(html_raw_dir)
        self.pdf_raw_dir   = Path(pdf_raw_dir)
        self.json_raw_dir  = Path(json_raw_dir)
        self.other_raw_dir = Path(other_raw_dir)

        for d in [self.output_dir, self.html_raw_dir, self.pdf_raw_dir,
                  self.json_raw_dir, self.other_raw_dir]:
            d.mkdir(parents=True, exist_ok=True)

        self.delay = delay
        self.force = force
        self.max_pages = 200  # overrideable; see set_max_pages() or --max-pages
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })

        # Configure html2text
        self.html_converter = html2text.HTML2Text()
        self.html_converter.ignore_links = False
        self.html_converter.ignore_images = False
        self.html_converter.ignore_emphasis = False
        self.html_converter.body_width = 0  # Don't wrap lines
        self.html_converter.single_line_break = False
        
    def extract_urls_from_file(self, filepath):
        """Extract all URLs from a markdown file."""
        urls = []
        with open(filepath, 'r', encoding='utf-8') as f:
            for raw_line in f:
                line = raw_line.strip()

                # Skip blank lines and comment lines
                if not line or line.startswith('#') or line == '':
                    continue

                # Find all URLs (both markdown links and plain URLs)
                markdown_links = re.findall(r'\[([^\]]+)\]\(([^\)]+)\)', line)
                plain_urls = re.findall(r'(?<![\(\[])(https?://[^\s\)\]]+)', line)

                # Add URLs from markdown links
                urls.extend([url for _, url in markdown_links])
                # Add plain URLs
                urls.extend(plain_urls)

        return list(OrderedDict.fromkeys(urls))  # Remove duplicates while preserving order
    
    # ------------------------------------------------------------------
    # Filename helpers
    # ------------------------------------------------------------------

    def _url_basename(self, url):
        """
        Return the last path segment of a URL with its original extension,
        suitable for use as a raw-file name on disk.

        Returns None when there is no usable segment (bare domain, trailing
        slash, or a name starting with '.').
        """
        path = unquote(urlparse(url).path).rstrip('/')
        basename = os.path.basename(path)
        if not basename or basename.startswith('.'):
            return None
        return basename

    def _get_html_title(self, soup):
        """
        Extract the page title from a BeautifulSoup object.

        Strips the common ' - Cisco' suffix and returns None when no <title>
        tag is present.
        """
        if not soup:
            return None
        tag = soup.find('title')
        if not tag:
            return None
        title = tag.get_text(strip=True)
        # Remove common Cisco suffix
        title = re.sub(r'\s*-\s*Cisco\s*$', '', title, flags=re.IGNORECASE).strip()
        return title or None

    def _title_to_filename(self, title):
        """
        Convert a human-readable page title to a safe Markdown filename.

        Example: 'Cisco UCS Manager Storage Management Guide, Release 4.3'
                 → 'Cisco-UCS-Manager-Storage-Management-Guide-Release-4.3.md'
        """
        # Remove characters that are illegal in filenames on common OS
        safe = re.sub(r'[<>:"/\\|?*]', '', title)
        # Collapse whitespace and replace with hyphens
        safe = re.sub(r'[\s,]+', '-', safe.strip())
        # Collapse repeated hyphens
        safe = re.sub(r'-{2,}', '-', safe).strip('-')
        if not safe:
            return None
        # Cap length and add extension
        return safe[:200] + '.md'

    # Map of lowercase file extensions to content-type labels.
    # Extensions absent from this map are treated as 'other'.
    _EXT_TYPE_MAP = {
        # HTML
        '.html': 'html', '.htm': 'html', '.xhtml': 'html', '.shtml': 'html',
        # PDF
        '.pdf': 'pdf',
        # JSON
        '.json': 'json',
    }

    def detect_url_type(self, url):
        """
        Determine the content type of a URL from its filename extension.

        Returns one of: 'html', 'pdf', 'json', 'other'.

        URLs with no extension (common for Cisco guide entry-points) are
        treated as 'html'.  Everything else with an unrecognised extension
        is classified as 'other'.
        """
        path = urlparse(url).path.rstrip('/')
        _, ext = os.path.splitext(path)
        ext = ext.lower()

        if not ext:
            # No extension – assume it is an HTML page (e.g. Cisco guide TOC)
            return 'html'

        return self._EXT_TYPE_MAP.get(ext, 'other')
    
    def is_same_guide(self, url, base_url):
        """
        Check if a URL belongs to the same documentation guide.
        
        For Cisco docs, sub-pages typically share the same base path.
        """
        parsed_url = urlparse(url)
        parsed_base = urlparse(base_url)
        
        # Must be same domain
        if parsed_url.netloc != parsed_base.netloc:
            return False
        
        # For Cisco docs, get the guide directory path
        base_path_parts = parsed_base.path.rstrip('/').split('/')
        url_path_parts = parsed_url.path.rstrip('/').split('/')
        
        # Check if they share the same guide path structure
        # Typically: /c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/{GUIDE-NAME}/{VERSION}/
        if len(base_path_parts) >= 2:
            # Compare all parts except the last one (the actual page)
            return url_path_parts[:-1] == base_path_parts[:-1] or \
                   '/'.join(url_path_parts[:-1]).startswith('/'.join(base_path_parts[:-1]))
        
        return False
    
    # ------------------------------------------------------------------
    # Network helpers
    # ------------------------------------------------------------------

    def fetch_raw(self, url, extra_headers=None):
        """
        Fetch raw bytes from a URL.

        Args:
            url:          The URL to fetch.
            extra_headers: Optional dict of additional request headers (e.g.
                           ``{'Accept': 'application/json'}``).  These are
                           merged on top of the session defaults for this
                           single request only.

        Returns (content_bytes, response) or (None, None) on error.
        """
        try:
            print(f"  Fetching: {url}")
            headers = extra_headers or {}
            response = self.session.get(url, timeout=30, headers=headers)
            response.raise_for_status()
            time.sleep(self.delay)  # Be respectful
            return response.content, response
        except Exception as e:
            print(f"  Error fetching {url}: {e}")
            return None, None

    def fetch_page(self, url):
        """Fetch a page, return (BeautifulSoup, raw_bytes) or (None, None)."""
        content, _ = self.fetch_raw(url)
        if content is None:
            return None, None
        return BeautifulSoup(content, 'html.parser'), content

    def _save_raw(self, raw_dir, filename, content):
        """Write raw bytes to raw_dir/filename, creating dirs as needed."""
        dest = raw_dir / filename
        dest.write_bytes(content)
        print(f"  Saved raw: {dest}")
        return dest
    
    # ------------------------------------------------------------------
    # Sub-page discovery
    # ------------------------------------------------------------------

    def find_subpages(self, soup, base_url):
        """
        Find all sub-pages within the documentation.
        
        Cisco docs typically have navigation elements with links to other pages.
        """
        subpages = []
        
        if not soup:
            return subpages
        
        # Look for navigation elements and content links
        # Cisco docs often use specific classes for navigation
        nav_selectors = [
            'nav a',
            '.navigation a',
            '.nav a',
            '.toc a',
            '.sidebar a',
            '#sidebar a',
            '.content a',
            'a[href$=".html"]',
        ]
        
        links = []
        for selector in nav_selectors:
            links.extend(soup.select(selector))
        
        # Also get all links from the main content
        content_links = soup.find_all('a', href=True)
        links.extend(content_links)
        
        for link in links:
            href = link.get('href', '')
            if not href or href.startswith('#') or href.startswith('javascript:'):
                continue

            # Strip fragment so we don't treat foo.html#section as a new page
            href = href.split('#')[0]
            if not href:
                continue

            # Build absolute URL
            absolute_url = urljoin(base_url, href)

            # Only include if it's part of the same guide
            if self.is_same_guide(absolute_url, base_url) and absolute_url not in subpages:
                subpages.append(absolute_url)

        return list(OrderedDict.fromkeys(subpages))  # Remove duplicates
    
    def extract_main_content(self, soup):
        """Extract the main content from a Cisco documentation page."""
        if not soup:
            return ""
        
        # Cisco docs typically have the main content in specific containers
        content_selectors = [
            'article',
            'main',
            '.content',
            '#content',
            '.main-content',
            'div[role="main"]',
            '.documentation-content',
        ]
        
        main_content = None
        for selector in content_selectors:
            main_content = soup.select_one(selector)
            if main_content:
                break
        
        # Fallback to body if no specific content container found
        if not main_content:
            main_content = soup.find('body')
        
        if not main_content:
            return ""
        
        # Remove navigation, footer, scripts, styles
        for element in main_content.find_all(['script', 'style', 'nav', 'footer', 'header']):
            element.decompose()
        
        return str(main_content)
    
    def clean_markdown(self, markdown):
        """
        Clean up invalid Markdown syntax.
        
        Fixes:
        - Headings with bullet prefixes (e.g., '  * ####' -> '####')
        - Excessive indentation in bullets
        - Multiple blank lines
        """
        if not markdown:
            return ""
        
        lines = markdown.split('\n')
        cleaned_lines = []
        
        for line in lines:
            # Fix headings that are prefixed with list bullets
            # Pattern: optional spaces + asterisk + spaces + hash symbols
            if re.match(r'^\s*\*\s+(#{1,6})\s+', line):
                # Extract just the heading part (remove bullet prefix)
                line = re.sub(r'^\s*\*\s+(#{1,6}\s+.+)$', r'\1', line)
            
            # Fix excessive indentation in bullet points
            # Convert 4+ spaces before asterisk to 2 spaces per indent level
            if re.match(r'^\s{4,}\*\s+', line):
                # Count leading spaces
                leading_spaces = len(line) - len(line.lstrip())
                # Calculate proper indent (2 spaces per level)
                indent_level = leading_spaces // 4
                proper_indent = '  ' * indent_level
                # Rebuild line with proper indentation
                line = proper_indent + line.lstrip()
            
            cleaned_lines.append(line)
        
        # Join lines and clean up multiple consecutive blank lines
        cleaned = '\n'.join(cleaned_lines)
        cleaned = re.sub(r'\n{4,}', '\n\n\n', cleaned)  # Max 3 newlines (2 blank lines)
        
        return cleaned
    
    def _parse_fetched_on(self, output_path):
        """
        Read the '*Fetched on: YYYY-MM-DD HH:MM:SS*' timestamp embedded in a
        Markdown file and return a timezone-aware UTC datetime.

        Returns None if the line is absent or cannot be parsed.
        """
        try:
            with open(output_path, 'r', encoding='utf-8') as f:
                for line in f:
                    m = re.search(
                        r'\*Fetched on:\s*(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\*',
                        line
                    )
                    if m:
                        naive = datetime.datetime.strptime(m.group(1), '%Y-%m-%d %H:%M:%S')
                        # strptime produces a naive datetime; treat it as local time
                        return naive.astimezone(datetime.timezone.utc)
        except Exception:
            pass
        return None

    def check_should_download(self, url, output_path):
        """
        Determine whether the remote URL needs to be downloaded.

        Rules (applied in order):
        0. If --force is set, always download regardless of any other check.
        1. If the local file was last modified less than 24 hours ago (filesystem
           mtime) → skip (file is fresh enough; may have been manually edited).
        2. Send an HTTP HEAD request for the URL and compare Last-Modified
           against the 'Fetched on' timestamp embedded in the Markdown file
           (falls back to filesystem mtime if the header is missing):
           a. Remote is not newer → skip.
           b. Remote is newer, no header, or HEAD fails → download.

        Returns:
            (skip: bool, reason: str)
        """
        # Rule 0: force flag overrides everything
        if self.force:
            return False, "force flag set (-f): skipping all freshness checks"

        path = Path(output_path)
        if not path.exists():
            return False, "local file does not exist"

        file_mtime = datetime.datetime.fromtimestamp(path.stat().st_mtime, tz=datetime.timezone.utc)
        age = datetime.datetime.now(tz=datetime.timezone.utc) - file_mtime

        # Rule 1: file was modified (on disk) within the last 24 hours
        if age < datetime.timedelta(hours=24):
            return True, f"local file is {age.seconds // 3600}h {(age.seconds % 3600) // 60}m old (< 1 day)"

        # Rule 2: compare HTTP Last-Modified against the 'Fetched on' date
        #         embedded in the Markdown file (falls back to filesystem mtime
        #         if the header line is missing or unparseable).
        fetched_on = self._parse_fetched_on(output_path)
        if fetched_on:
            reference_dt = fetched_on
            reference_label = f"'Fetched on' date {fetched_on.strftime('%Y-%m-%d %H:%M:%S UTC')}"
        else:
            reference_dt = file_mtime
            reference_label = f"file mtime {file_mtime.strftime('%Y-%m-%d %H:%M:%S UTC')} (no 'Fetched on' found in file)"

        try:
            print(f"  HEAD {url}")
            resp = self.session.head(url, timeout=15, allow_redirects=True)
            last_modified_str = resp.headers.get('Last-Modified') or resp.headers.get('last-modified')
            if last_modified_str:
                remote_mtime = datetime.datetime.fromtimestamp(
                    email.utils.parsedate_to_datetime(last_modified_str).timestamp(),
                    tz=datetime.timezone.utc
                )
                if remote_mtime <= reference_dt:
                    return True, (
                        f"remote Last-Modified {remote_mtime.strftime('%Y-%m-%d %H:%M:%S UTC')} "
                        f"<= {reference_label}"
                    )
                else:
                    return False, (
                        f"remote Last-Modified {remote_mtime.strftime('%Y-%m-%d %H:%M:%S UTC')} "
                        f"> {reference_label}"
                    )
            else:
                return False, "no Last-Modified header; downloading to be safe"
        except Exception as e:
            return False, f"HEAD request failed ({e}); downloading to be safe"

    # ------------------------------------------------------------------
    # Per-type processors  (download phase then convert phase)
    # ------------------------------------------------------------------

    def _url_to_raw_filename(self, url):
        """
        Return a filesystem-safe filename for storing a raw download.

        Uses the URL basename (last path segment) when it has a usable name.
        For extension-less URLs (Cisco guide entry-points) the basename is
        kept as-is without appending a suffix, since the file is saved as
        the HTML content it actually is.  As a last resort the entire path
        is sanitised and used directly – no artificial extension is added.
        """
        basename = self._url_basename(url)
        if basename:
            return basename
        # Fallback: sanitise the full path into a flat filename
        path = unquote(urlparse(url).path).strip('/')
        safe = re.sub(r'[^a-zA-Z0-9._-]', '_', path)
        return safe[:200] or 'index'

    def _is_cached(self, path):
        """
        Return True when *path* exists on disk and was last modified less
        than 24 hours ago (i.e. it is a fresh cached copy that can be
        re-used without a network request).

        Returns:
            (cached: bool, reason: str)
        """
        p = Path(path)
        if not p.exists():
            return False, 'no local file'
        file_mtime = datetime.datetime.fromtimestamp(
            p.stat().st_mtime, tz=datetime.timezone.utc
        )
        age = datetime.datetime.now(tz=datetime.timezone.utc) - file_mtime
        if age < datetime.timedelta(hours=24):
            h = age.seconds // 3600
            m = (age.seconds % 3600) // 60
            return True, f'cached {h}h {m}m ago (< 24 h)'
        return False, f'cache expired ({age.days}d {age.seconds // 3600}h old)'

    # --- HTML guide ---

    def download_guide(self, base_url, max_pages=200):
        """
        Download all pages of an HTML documentation guide to html_raw_dir.

        Crawls the base page and every sub-page (up to *max_pages*), saving
        each raw HTML file to html_raw_dir.  Sub-page discovery and the
        Markdown filename derivation both happen here so the convert step
        needs only to read local files.

        Args:
            base_url:  The entry-point URL for the guide.
            max_pages: Safety cap on the number of pages fetched.

        Returns:
            (pages: OrderedDict[url -> Path], md_filename: str | None)
            *pages* maps each fetched URL to its saved local Path.
            *md_filename* is None when no <title> could be extracted.
        """
        print(f"\nDownloading guide: {base_url}")

        visited = set()
        to_visit = [base_url]
        pages = OrderedDict()   # url -> Path of saved raw HTML
        md_filename = None

        while to_visit and len(visited) < max_pages:
            url = to_visit.pop(0)

            if url in visited:
                continue
            visited.add(url)

            raw_name = self._url_to_raw_filename(url)
            raw_path = self.html_raw_dir / raw_name

            # Use the cached file if it is still fresh (< 24 h old)
            cached, cache_reason = self._is_cached(raw_path)
            if cached and not self.force:
                print(f"  ⏭  Using cached file ({cache_reason}): {raw_path}")
                content = raw_path.read_bytes()
            else:
                if self.force or not Path(raw_path).exists():
                    pass  # will download below
                else:
                    print(f"  ↓  Cache miss ({cache_reason}), re-downloading: {url}")
                content, _ = self.fetch_raw(url)
                if content is None:
                    continue
                raw_path = self._save_raw(self.html_raw_dir, raw_name, content)

            pages[url] = raw_path

            soup = BeautifulSoup(content, 'html.parser')

            # Derive Markdown filename from the base page <title>
            if url == base_url:
                title = self._get_html_title(soup)
                if title:
                    md_filename = self._title_to_filename(title)
                    print(f"  Title: {title}")

            # Discover sub-pages for further crawling.
            # Only queue HTML pages – PDFs and other file types linked from a
            # guide are skipped here; they are only downloaded when explicitly
            # listed in urls.md.
            subpages = self.find_subpages(soup, base_url)
            new_subpages = [
                p for p in subpages
                if p not in visited
                and p not in to_visit
                and self.detect_url_type(p) == 'html'
            ]
            skipped = [p for p in subpages if self.detect_url_type(p) != 'html']
            if skipped:
                print(f"  Skipped {len(skipped)} non-HTML sub-page link(s) (PDF/other)")
            if new_subpages:
                print(f"  Found {len(new_subpages)} new HTML sub-page(s) from {url}")
            to_visit.extend(new_subpages)

        print(f"  Downloaded/cached {len(pages)} page(s) to {self.html_raw_dir}")
        return pages, md_filename

    def convert_guide_from_raw(self, pages, base_url):
        """
        Convert downloaded raw HTML files into a single combined Markdown document.

        Reads each file from disk (as saved by download_guide), extracts the
        main content, converts to Markdown, and concatenates everything.

        Args:
            pages:    OrderedDict[url -> Path] as returned by download_guide().
            base_url: The entry-point URL (used in the document header).

        Returns:
            Combined Markdown string.
        """
        print(f"\nConverting guide to Markdown: {base_url}")

        combined  = f"# Documentation: {base_url}\n\n"
        combined += f"*Fetched on: {time.strftime('%Y-%m-%d %H:%M:%S')}*\n\n"
        combined += "---\n\n"

        for idx, (url, raw_path) in enumerate(pages.items(), 1):
            try:
                content = Path(raw_path).read_bytes()
                soup = BeautifulSoup(content, 'html.parser')
                html_content = self.extract_main_content(soup)
                page_md = self.html_converter.handle(html_content)
                page_md = self.clean_markdown(page_md)
            except Exception as e:
                print(f"  Warning: could not convert {raw_path}: {e}")
                page_md = f"*Error converting page: {e}*"

            combined += f"## Page {idx}: {url}\n\n"
            combined += page_md
            combined += "\n\n---\n\n"

        combined = self.clean_markdown(combined)
        print(f"  Converted {len(pages)} page(s) to Markdown")
        return combined

    # --- PDF ---

    def download_pdf(self, url):
        """
        Download a PDF file to pdf_raw_dir.

        Returns the local Path on success, or None on error.
        Uses the cached file without a network request when it is less than
        24 hours old (and --force is not set).
        """
        print(f"\nDownloading PDF: {url}")
        raw_name = self._url_to_raw_filename(url)
        raw_path = self.pdf_raw_dir / raw_name

        cached, cache_reason = self._is_cached(raw_path)
        if cached and not self.force:
            print(f"  ⏭  Using cached file ({cache_reason}): {raw_path}")
            return raw_path

        if raw_path.exists():
            print(f"  ↓  Cache miss ({cache_reason}), re-downloading")
        content, _ = self.fetch_raw(url)
        if content is None:
            return None
        return self._save_raw(self.pdf_raw_dir, raw_name, content)

    def convert_pdf_from_raw(self, url, local_path):
        """
        Convert a downloaded PDF file to Markdown.

        Args:
            url:        Original URL (used in the document header).
            local_path: Path to the saved PDF file.

        Returns:
            Markdown string.
        """
        print(f"\nConverting PDF to Markdown: {local_path}")

        md  = f"# Documentation: {url}\n\n"
        md += f"*Fetched on: {time.strftime('%Y-%m-%d %H:%M:%S')}*\n\n"
        md += "---\n\n"

        if not _PDFMINER_AVAILABLE:
            md += ("*pdfminer.six is not installed; install it with "
                   "`pip install pdfminer.six` to enable PDF text extraction.*\n")
            return md

        try:
            content = Path(local_path).read_bytes()
            text = pdf_extract_text(io.BytesIO(content))
            md += text or "*(no text extracted)*"
        except Exception as e:
            md += f"*Error extracting PDF text: {e}*"

        return md

    # --- Other / unknown file types ---

    def download_other(self, url):
        """
        Download a file of unrecognised type to other_raw_dir.

        Returns the local Path on success, or None on error.
        Uses the cached file without a network request when it is less than
        24 hours old (and --force is not set).
        """
        print(f"\nDownloading (other): {url}")
        raw_name = self._url_to_raw_filename(url)
        raw_path = self.other_raw_dir / raw_name

        cached, cache_reason = self._is_cached(raw_path)
        if cached and not self.force:
            print(f"  ⏭  Using cached file ({cache_reason}): {raw_path}")
            return raw_path

        if raw_path.exists():
            print(f"  ↓  Cache miss ({cache_reason}), re-downloading")
        content, _ = self.fetch_raw(url)
        if content is None:
            return None
        return self._save_raw(self.other_raw_dir, raw_name, content)

    def convert_other_from_raw(self, url, local_path):
        """
        Wrap a file of unrecognised type in a minimal Markdown document.

        Text-based content is embedded in a fenced code block; binary
        content is noted with a size hint.

        Args:
            url:        Original URL (used in the document header).
            local_path: Path to the saved file.

        Returns:
            Markdown string.
        """
        print(f"\nConverting (other) to Markdown: {local_path}")

        md  = f"# Documentation: {url}\n\n"
        md += f"*Fetched on: {time.strftime('%Y-%m-%d %H:%M:%S')}*\n\n"
        md += "---\n\n"

        try:
            raw_bytes = Path(local_path).read_bytes()
            # Try to decode as UTF-8 text; fall back to latin-1 as last resort
            try:
                text = raw_bytes.decode('utf-8')
            except UnicodeDecodeError:
                try:
                    text = raw_bytes.decode('latin-1')
                except Exception:
                    text = None

            if text is not None:
                _, ext = os.path.splitext(str(local_path))
                lang = ext.lstrip('.') or ''
                md += f"```{lang}\n"
                md += text
                md += "\n```\n"
            else:
                md += (f"*Binary file ({len(raw_bytes):,} bytes) – "
                       f"no text representation available.*\n")
        except Exception as e:
            md += f"*Error reading file: {e}*\n"

        return md

    # --- JSON ---

    def download_json(self, url):
        """
        Download a JSON file to json_raw_dir.

        Returns the local Path on success, or None on error.
        Uses the cached file without a network request when it is less than
        24 hours old (and --force is not set).
        """
        print(f"\nDownloading JSON: {url}")
        raw_name = self._url_to_raw_filename(url)
        raw_path = self.json_raw_dir / raw_name

        cached, cache_reason = self._is_cached(raw_path)
        if cached and not self.force:
            print(f"  ⏭  Using cached file ({cache_reason}): {raw_path}")
            return raw_path

        if raw_path.exists():
            print(f"  ↓  Cache miss ({cache_reason}), re-downloading")
        # Request JSON explicitly so the server returns application/json
        content, _ = self.fetch_raw(url, extra_headers={'Accept': 'application/json'})
        if content is None:
            return None
        return self._save_raw(self.json_raw_dir, raw_name, content)

    def convert_json_from_raw(self, url, local_path):
        """
        Convert a downloaded JSON file to Markdown.

        Uses the same rendering logic as json_to_markdown.py:
        - dict      → Key/Value table
        - list[dict] → table with union of keys
        - list[scalars] → bullet list
        - complex nested → fenced JSON code block

        A collapsible "Raw JSON" appendix is appended for full fidelity.

        Args:
            url:        Original URL (used in the document header).
            local_path: Path to the saved JSON file.

        Returns:
            Markdown string.
        """
        print(f"\nConverting JSON to Markdown: {local_path}")

        md  = f"# Documentation: {url}\n\n"
        md += f"*Fetched on: {time.strftime('%Y-%m-%d %H:%M:%S')}*\n\n"
        md += "---\n\n"

        try:
            data = _json_try_load(str(local_path))
            md += _json_value_to_markdown(data)
            md += "\n\n"
            # Collapsible raw JSON appendix
            try:
                pretty = json.dumps(data, ensure_ascii=False, indent=2)
                md += "<details><summary>Raw JSON</summary>\n\n```json\n"
                md += pretty
                md += "\n```\n\n</details>\n"
            except Exception:
                pass
        except Exception as e:
            # Fallback: embed raw text in a fenced block
            print(f"  Warning: could not parse JSON ({e}); using raw content")
            raw_text = Path(local_path).read_bytes().decode('utf-8', errors='replace')
            md += "```json\n" + raw_text + "\n```\n"

        return md

    def process_urls_file(self, urls_file):
        """
        Process all URLs from urls_file in two phases:

        Phase 1 – Download: fetch every raw file (HTML pages + sub-pages,
            PDFs, or JSON) and save to the appropriate raw directory.
        Phase 2 – Convert: read the saved raw files and convert to Markdown,
            then write the combined output to DEFAULT_MARKDOWN_DIR.
        """
        print(f"Reading URLs from: {urls_file}")
        urls = self.extract_urls_from_file(urls_file)
        print(f"Found {len(urls)} URLs to process")

        for idx, url in enumerate(urls, 1):
            print(f"\n{'='*80}")
            print(f"Processing URL {idx}/{len(urls)}: {url}")
            print(f"{'='*80}")

            try:
                url_type = self.detect_url_type(url)
                raw_basename = self._url_to_raw_filename(url)

                # ----------------------------------------------------------
                # Freshness check (against the raw entry-point file)
                # ----------------------------------------------------------
                if url_type == 'html':
                    raw_check_path = self.html_raw_dir / raw_basename
                elif url_type == 'pdf':
                    raw_check_path = self.pdf_raw_dir / raw_basename
                elif url_type == 'json':
                    raw_check_path = self.json_raw_dir / raw_basename
                else:
                    raw_check_path = self.other_raw_dir / raw_basename

                skip, reason = self.check_should_download(url, raw_check_path)
                if skip:
                    print(f"\n⏭  Skipping (up to date): {reason}")
                    print(f"   Raw file: {raw_check_path}")
                    continue
                print(f"\n↓  Downloading: {reason}")

                # ----------------------------------------------------------
                # Phase 1 – Download raw files
                # ----------------------------------------------------------
                pages: OrderedDict = OrderedDict()
                local_path = None
                print(f"\n--- Phase 1: Download ---")
                if url_type == 'html':
                    pages, md_filename = self.download_guide(url, max_pages=self.max_pages)
                    if not pages:
                        print(f"\n✗ No pages downloaded for {url}")
                        continue
                    # Fall back when <title> was not found
                    if not md_filename:
                        stem = raw_basename.rsplit('.', 1)[0] if '.' in raw_basename else raw_basename
                        md_filename = stem + '.md'
                elif url_type == 'pdf':
                    local_path = self.download_pdf(url)
                    if not local_path:
                        print(f"\n✗ Could not download PDF: {url}")
                        continue
                    md_filename = raw_basename + '.md'
                elif url_type == 'json':
                    local_path = self.download_json(url)
                    if not local_path:
                        print(f"\n✗ Could not download JSON: {url}")
                        continue
                    md_filename = raw_basename + '.md'
                else:  # other
                    local_path = self.download_other(url)
                    if not local_path:
                        print(f"\n✗ Could not download file: {url}")
                        continue
                    md_filename = raw_basename + '.md'

                # ----------------------------------------------------------
                # Phase 2 – Convert raw files to Markdown
                # ----------------------------------------------------------
                print(f"\n--- Phase 2: Convert to Markdown ---")
                if url_type == 'html':
                    markdown_content = self.convert_guide_from_raw(pages, url)
                elif url_type == 'pdf':
                    markdown_content = self.convert_pdf_from_raw(url, local_path)
                elif url_type == 'json':
                    markdown_content = self.convert_json_from_raw(url, local_path)
                else:  # other
                    markdown_content = self.convert_other_from_raw(url, local_path)

                output_path = self.output_dir / md_filename
                output_path.write_text(markdown_content, encoding='utf-8')
                print(f"\n✓ Saved Markdown to: {output_path}")

            except Exception as e:
                print(f"\n✗ Error processing {url}: {e}")
                import traceback
                traceback.print_exc()

            # Longer delay between guides
            if idx < len(urls):
                print(f"\nWaiting before next guide...")
                time.sleep(self.delay * 2)

        print(f"\n{'='*80}")
        print(f"All done! Processed {len(urls)} URLs")
        print(f"{'='*80}")


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Fetch Cisco UCS documentation and convert to Markdown'
    )
    parser.add_argument(
        'urls_file',
        nargs='?',
        default='urls.md',
        help='Path to the file containing URLs (default: urls.md)'
    )
    parser.add_argument(
        '-o', '--output-dir',
        default=DEFAULT_MARKDOWN_DIR,
        help=f'Markdown output directory (default: {DEFAULT_MARKDOWN_DIR})'
    )
    parser.add_argument(
        '--html-raw-dir',
        default=DEFAULT_HTML_RAW_DIR,
        help=f'Directory for raw HTML files (default: {DEFAULT_HTML_RAW_DIR})'
    )
    parser.add_argument(
        '--pdf-raw-dir',
        default=DEFAULT_PDF_RAW_DIR,
        help=f'Directory for raw PDF files (default: {DEFAULT_PDF_RAW_DIR})'
    )
    parser.add_argument(
        '--json-raw-dir',
        default=DEFAULT_JSON_RAW_DIR,
        help=f'Directory for raw JSON files (default: {DEFAULT_JSON_RAW_DIR})'
    )
    parser.add_argument(
        '--other-raw-dir',
        default=DEFAULT_OTHER_RAW_DIR,
        help=f'Directory for raw files of unrecognised type (default: {DEFAULT_OTHER_RAW_DIR})'
    )
    parser.add_argument(
        '-d', '--delay',
        type=float,
        default=1.0,
        help='Delay between requests in seconds (default: 1.0)'
    )
    parser.add_argument(
        '--max-pages',
        type=int,
        default=200,
        help='Maximum pages to fetch per guide (default: 200)'
    )
    
    parser.add_argument(
        '-f', '--force',
        action='store_true',
        default=False,
        help='Force re-download of all files, ignoring freshness checks'
    )

    args = parser.parse_args()

    # Create fetcher
    fetcher = CiscoDocFetcher(
        markdown_dir=args.output_dir,
        html_raw_dir=args.html_raw_dir,
        pdf_raw_dir=args.pdf_raw_dir,
        json_raw_dir=args.json_raw_dir,
        other_raw_dir=args.other_raw_dir,
        delay=args.delay,
        force=args.force,
    )
    fetcher.max_pages = args.max_pages

    if args.force:
        print("\n⚠  Force mode enabled: all files will be re-downloaded")

    # Process URLs file
    fetcher.process_urls_file(args.urls_file)


if __name__ == '__main__':
    main()
