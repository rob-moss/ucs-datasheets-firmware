#!/usr/bin/env python3
"""
Fetch Cisco UCS documentation pages recursively and convert to Markdown.

This script:
1. Reads URLs from urls.md
2. Fetches each main page and all linked sub-pages
3. Converts the entire documentation structure to Markdown
4. Saves as a single Markdown file per main URL
"""

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


class CiscoDocFetcher:
    def __init__(self, output_dir=".", delay=1.0, force=False):
        """
        Initialize the documentation fetcher.

        Args:
            output_dir: Directory to save markdown files
            delay: Delay between requests in seconds (be respectful)
            force: Skip all freshness checks and re-download every file
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.delay = delay
        self.force = force
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
    
    def get_filename_from_url(self, url):
        """
        Extract a Markdown filename from a URL.

        Returns None if the URL has no usable filename component (e.g. bare
        domain, trailing slash, or a path whose basename has no meaningful stem).
        """
        parsed = urlparse(url)
        path = unquote(parsed.path)

        # Get the last non-empty path segment
        basename = os.path.basename(path.rstrip('/'))

        # Reject empty basenames or those with no stem (e.g. just an extension)
        if not basename or basename.startswith('.'):
            return None

        # Remove .html extension and add .md
        if basename.endswith('.html'):
            filename = basename[:-5] + '.md'
        elif basename.endswith('.md'):
            filename = basename
        else:
            filename = basename + '.md'

        return filename
    
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
    
    def fetch_page(self, url):
        """Fetch a page and return BeautifulSoup object."""
        try:
            print(f"  Fetching: {url}")
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            time.sleep(self.delay)  # Be respectful
            return BeautifulSoup(response.content, 'html.parser')
        except Exception as e:
            print(f"  Error fetching {url}: {e}")
            return None
    
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

    def process_guide(self, base_url, max_pages=200):
        """
        Process a complete documentation guide.
        
        Args:
            base_url: The main URL of the guide
            max_pages: Maximum number of pages to fetch (safety limit)
            
        Returns:
            Combined markdown content
        """
        print(f"\nProcessing guide: {base_url}")
        
        visited = set()
        to_visit = [base_url]
        pages_content = OrderedDict()
        
        while to_visit and len(visited) < max_pages:
            url = to_visit.pop(0)
            
            if url in visited:
                continue
                
            visited.add(url)
            
            # Fetch the page
            soup = self.fetch_page(url)
            if not soup:
                continue
            
            # Extract main content
            html_content = self.extract_main_content(soup)
            
            # Convert to markdown
            markdown = self.html_converter.handle(html_content)
            
            # Clean up invalid markdown syntax
            markdown = self.clean_markdown(markdown)
            
            # Store the content
            pages_content[url] = markdown
            
            # Find sub-pages only if this is the first page (base_url)
            # or if we want to recursively explore all pages
            if url == base_url:
                subpages = self.find_subpages(soup, base_url)
                print(f"  Found {len(subpages)} potential sub-pages")
                
                # Add new subpages to visit
                for subpage in subpages:
                    if subpage not in visited and subpage not in to_visit:
                        to_visit.append(subpage)
        
        print(f"  Processed {len(pages_content)} pages")
        
        # Combine all content
        combined_markdown = f"# Documentation: {base_url}\n\n"
        combined_markdown += f"*Fetched on: {time.strftime('%Y-%m-%d %H:%M:%S')}*\n\n"
        combined_markdown += "---\n\n"
        
        for idx, (url, content) in enumerate(pages_content.items(), 1):
            combined_markdown += f"## Page {idx}: {url}\n\n"
            combined_markdown += content
            combined_markdown += "\n\n---\n\n"
        
        # Final cleanup of the combined markdown
        combined_markdown = self.clean_markdown(combined_markdown)
        
        return combined_markdown
    
    def process_urls_file(self, urls_file):
        """Process all URLs from the urls.md file."""
        print(f"Reading URLs from: {urls_file}")
        urls = self.extract_urls_from_file(urls_file)
        
        print(f"Found {len(urls)} URLs to process")
        
        for idx, url in enumerate(urls, 1):
            print(f"\n{'='*80}")
            print(f"Processing URL {idx}/{len(urls)}")
            print(f"{'='*80}")
            
            try:
                # Determine output path early so freshness checks can use it
                filename = self.get_filename_from_url(url)
                if not filename:
                    print(f"\n⚠  Skipping (no usable filename): {url}")
                    continue
                output_path = self.output_dir / filename

                # Freshness checks — skip download if local copy is current
                skip, reason = self.check_should_download(url, output_path)
                if skip:
                    print(f"\n⏭  Skipping (up to date): {reason}")
                    print(f"   File: {output_path}")
                    continue
                else:
                    print(f"\n↓  Downloading: {reason}")

                # Process the guide
                markdown_content = self.process_guide(url)

                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(markdown_content)

                print(f"\n✓ Saved to: {output_path}")
                
            except Exception as e:
                print(f"\n✗ Error processing {url}: {e}")
                import traceback
                traceback.print_exc()
            
            # Longer delay between guides
            if idx < len(urls):
                print(f"\nWaiting before next guide...")
                time.sleep(self.delay * 2)
        
        print(f"\n{'='*80}")
        print(f"All done! Processed {len(urls)} guides")
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
        default='.',
        help='Output directory for markdown files (default: current directory)'
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
    fetcher = CiscoDocFetcher(output_dir=args.output_dir, delay=args.delay, force=args.force)

    if args.force:
        print("\n⚠  Force mode enabled: all files will be re-downloaded")

    # Process URLs file
    fetcher.process_urls_file(args.urls_file)


if __name__ == '__main__':
    main()
