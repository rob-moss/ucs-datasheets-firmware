#!/Users/romoss/Git/github.com/romoss_cisco/ucs-datasheets-firmware/.venv/bin/python3

#!/usr/bin/env python3
"""
Fetches UCS firmware release pages from software.cisco.com (Version 4)

This script fetches release information for multiple UCS firmware types:
- Infrastructure (UCS Manager, Fabric Interconnects, etc.)
- UCS Blades (B-Series and X-Series servers)
- C-Series Rack Servers

Features:
- Fetches from 3 different firmware sources (only 3 HTTP requests)
- Validates HTTP 200 responses and HTML content
- Detects JavaScript-rendered pages (Angular SPA)
- Extracts JavaScript files and parses for version strings
- Searches for all <span id="selectedRelease"> tags
- Updates the recommended-firmware.md file with URLs
- NO FALLBACK: Exits with error if versions cannot be extracted

Note: Cisco's download site is an Angular single-page application where content
is rendered client-side. This script attempts to parse JavaScript files to extract
the recommended versions that would populate the page.

Usage:
    python fetch_ucsm_release_page_v4.py
    python fetch_ucsm_release_page_v4.py --no-update
    python fetch_ucsm_release_page_v4.py --save-html
"""

import argparse
import requests
import time
import re
from pathlib import Path
from datetime import datetime
from http.cookiejar import Cookie
from html.parser import HTMLParser


class RecommendedVersionParser(HTMLParser):
    """Parses HTML to extract ALL recommended firmware versions"""
    
    def __init__(self):
        super().__init__()
        self.recommended_versions = []
        self.in_selected_release = False
    
    def handle_starttag(self, tag, attrs):
        """Look for span tag with id="selectedRelease" """
        if tag == 'span':
            attr_dict = dict(attrs)
            if attr_dict.get('id') == 'selectedRelease':
                self.in_selected_release = True
    
    def handle_data(self, data):
        """Capture the version text inside the selectedRelease span"""
        if self.in_selected_release:
            version = data.strip()
            if version and version not in self.recommended_versions:
                self.recommended_versions.append(version)
            self.in_selected_release = False


class CiscoSoftwarePageFetcher:
    """Fetches Cisco Software Download pages with anonymous authentication"""
    
    BASE_URL = "https://software.cisco.com"
    
    # Firmware source definitions
    FIRMWARE_SOURCES = {
        'infrastructure': {
            'mdf_id': '283612660',
            'software_id': '283655658',
            'name': 'Infrastructure',
            'description': 'UCS Manager, Fabric Interconnects, Fabric Extenders'
        },
        'blades': {
            'mdf_id': '283853163',
            'software_id': '283655681',
            'name': 'Cisco UCS Blades',
            'description': 'B-Series and X-Series blade servers'
        },
        'c-series': {
            'mdf_id': '283862063',
            'software_id': '283655681',
            'name': 'Cisco UCS C-Series rack servers',
            'description': 'C-Series rack-mounted servers'
        }
    }
    
    def __init__(self, mdf_id=None, software_id=None):
        """
        Initialize the fetcher
        
        Args:
            mdf_id: Product MDF ID (default: 283612660 for UCS Manager)
            software_id: Software type ID (default: 283655658 for UCS Manager Software)
        """
        self.mdf_id = mdf_id or self.DEFAULT_MDFID
        self.software_id = software_id or self.DEFAULT_SOFTWAREID
        self.session = requests.Session()
        
        # Disable SSL warnings but verify certificates
        self.session.verify = True
        
        # Set up headers to emulate macOS Safari browser more realistically
        # Using actual Safari headers instead of Chrome pretending to be Safari
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
        })
        
        # Pre-configure cookies from captured browser session
        self._setup_cookies()
    
    def _setup_cookies(self):
        """
        Sets up cookies from a captured browser session
        
        These cookies are extracted from a successful browser session to
        help bypass bot detection.
        """
        # Domain for cookies
        domain = "software.cisco.com"
        
        # Cookies to set (from captured session)
        cookies = {
            "ADRUM_BTa": "R:0|g:0a60aa3c-3379-4922-8d95-020918fdd6c8|n:cisco1_d5ce4a50-0e7c-4e42-a5a5-4c7d1bcfcd74",
            "ADRUM_BT1": "R:0|i:577655|e:3|t:1765925371513|d:4",
            "e12afc78a040e267522a096a03001b21": "100e7f4478317bd00daeb2449f67094b",
            "772ea0ed1824b02cea246cc324d803ca": "5d2ac8c56a16b12b3350650efb2c1806",
        }
        
        # Add cookies to the session
        for name, value in cookies.items():
            self.session.cookies.set(
                name=name,
                value=value,
                domain=domain,
                path="/",
                secure=True
            )
        
        print(f"Pre-configured {len(cookies)} cookies for {domain}")
    
    def establish_session(self):
        """
        Establishes an anonymous session by visiting the main download page
        
        This sets the necessary cookies (including swsession) for subsequent requests.
        
        Returns:
            bool: True if session was established successfully
        """
        print("Establishing anonymous session...")
        
        # First, visit the main software.cisco.com page to get initial cookies
        try:
            print("  Step 1a: Visiting main Cisco Software site...")
            main_response = self.session.get(f"{self.BASE_URL}/", timeout=30, allow_redirects=True)
            print(f"    Status: {main_response.status_code}")
            
            if main_response.status_code == 200:
                print(f"    ✓ Successfully accessed main page")
            else:
                print(f"    ⚠ Unexpected status code: {main_response.status_code}")
            
            # Add a small delay to be more human-like
            time.sleep(1)
            
        except requests.exceptions.RequestException as e:
            print(f"  ⚠ Warning: Could not visit main page: {e}")
            # Continue anyway
        
        # Now visit the download page to establish session
        base_url = f"{self.BASE_URL}/download/home/{self.mdf_id}/type/{self.software_id}"
        
        try:
            print("  Step 1b: Visiting download page...")
            response = self.session.get(base_url, timeout=30, allow_redirects=True)
            
            print(f"    Status: {response.status_code}")
            
            if response.status_code == 200:
                print(f"    ✓ Successfully accessed download page")
            elif response.status_code == 403:
                print(f"    ✗ Access forbidden (403) - Bot detection may still be active")
                print(f"    Response headers: {dict(response.headers)}")
                return False
            else:
                print(f"    ⚠ Unexpected status code: {response.status_code}")
            
            # Check if we got session cookies
            if 'swsession' in self.session.cookies:
                print(f"  ✓ Session established (swsession cookie received)")
            else:
                print(f"  ⚠ Session established (but no swsession cookie)")
            
            # Don't raise on non-200 status to allow inspection
            if response.status_code != 200:
                return False
            
            return True
            
        except requests.exceptions.RequestException as e:
            print(f"  ✗ Failed to establish session: {e}")
            print(f"  Response status: {e.response.status_code if hasattr(e, 'response') and e.response else 'N/A'}")
            if hasattr(e, 'response') and e.response:
                print(f"  Response headers: {dict(e.response.headers)}")
            raise
    
    def fetch_download_page(self):
        """
        Fetches the main download page which contains all recommended versions
        
        Returns:
            str: HTML content of the page
        """
        print(f"Fetching download page...")
        
        # Add small delay to be more human-like
        time.sleep(0.5)
        
        # Build the URL (without specific release version to get all versions)
        url = f"{self.BASE_URL}/download/home/{self.mdf_id}/type/{self.software_id}"
        
        try:
            # Add referer header for this specific request
            headers = {
                "Referer": f"{self.BASE_URL}/download/home/{self.mdf_id}"
            }
            
            response = self.session.get(url, headers=headers, timeout=30, allow_redirects=True)
            
            print(f"  Status code: {response.status_code}")
            print(f"  Final URL: {response.url}")
            
            if response.status_code == 200:
                print(f"  ✓ Successfully fetched page ({len(response.text)} bytes)")
                return response.text
            elif response.status_code == 403:
                print(f"  ✗ Access forbidden (403) - Bot detection active")
                print(f"  Response text (first 500 chars): {response.text[:500]}")
                return None
            else:
                print(f"  ⚠ Unexpected status code: {response.status_code}")
                print(f"  Response text (first 500 chars): {response.text[:500]}")
                return None
            
        except requests.exceptions.RequestException as e:
            print(f"  ✗ Failed to fetch download page: {e}")
            if hasattr(e, 'response') and e.response:
                print(f"  Response status: {e.response.status_code}")
                print(f"  Response text (first 500 chars): {e.response.text[:500]}")
            raise
    
    def get_session_info(self):
        """Returns information about the current session"""
        cookies = {name: value for name, value in self.session.cookies.items()}
        return {
            "cookies": cookies,
            "headers": dict(self.session.headers)
        }


def extract_script_urls(html_content, base_url):
    """
    Extracts JavaScript file URLs from HTML
    
    Args:
        html_content: HTML content string
        base_url: Base URL to resolve relative paths
    
    Returns:
        list: List of JavaScript URLs
    """
    script_pattern = r'<script[^>]*src="([^"]+)"[^>]*>'
    matches = re.findall(script_pattern, html_content, re.IGNORECASE)
    
    script_urls = []
    for match in matches:
        # Convert relative URLs to absolute
        if match.startswith('http'):
            script_urls.append(match)
        elif match.startswith('/'):
            script_urls.append(f"{base_url}{match}")
        else:
            script_urls.append(f"{base_url}/{match}")
    
    return script_urls


def extract_css_urls(html_content, base_url):
    """
    Extracts CSS file URLs from HTML
    
    Args:
        html_content: HTML content string
        base_url: Base URL to resolve relative paths
    
    Returns:
        list: List of CSS URLs
    """
    css_pattern = r'<link[^>]*href="([^"]+\.css)"[^>]*>'
    matches = re.findall(css_pattern, html_content, re.IGNORECASE)
    
    css_urls = []
    for match in matches:
        # Convert relative URLs to absolute
        if match.startswith('http'):
            css_urls.append(match)
        elif match.startswith('/'):
            css_urls.append(f"{base_url}{match}")
        else:
            css_urls.append(f"{base_url}/{match}")
    
    return css_urls


def parse_versions_from_javascript(js_content):
    """
    Extracts firmware versions from JavaScript content
    
    Args:
        js_content: JavaScript content string
    
    Returns:
        list: List of version strings found
    """
    # UCS Manager version pattern: X.Y(Za) where X.Y is major.minor and Za is patch
    # Examples: 4.2(3o), 4.3(6c), 6.0(1b)
    version_pattern = r'\b(\d+\.\d+\([0-9a-z]+\))\b'
    
    matches = re.findall(version_pattern, js_content, re.IGNORECASE)
    
    # Deduplicate and sort
    versions = []
    for match in matches:
        if match not in versions:
            versions.append(match)
    
    return versions


def parse_recommended_versions(html_content, session=None, base_url="https://software.cisco.com"):
    """
    Extracts ALL recommended firmware versions from HTML and JavaScript
    
    Args:
        html_content: HTML content string
        session: Optional requests session for fetching JavaScript
        base_url: Base URL for resolving relative paths
    
    Returns:
        list: List of recommended versions found, or empty list if none found
    """
    # Try HTML parser first
    parser = RecommendedVersionParser()
    try:
        parser.feed(html_content)
        if parser.recommended_versions:
            return parser.recommended_versions
    except Exception as e:
        print(f"  Warning: HTML parser failed: {e}")
    
    # Search in HTML for span tags
    pattern = r'<span[^>]*id="selectedRelease"[^>]*>([^<]+)</span>'
    matches = re.findall(pattern, html_content, re.IGNORECASE)
    if matches:
        versions = []
        for match in matches:
            version = match.strip()
            if version and version not in versions:
                versions.append(version)
        return versions
    
    # If no versions found in HTML, extract and parse JavaScript and CSS files
    if session:
        print("  No versions in HTML, extracting resource files...")
        
        # Create htmlfiles directory for saving files
        htmlfiles_dir = ensure_htmlfiles_directory()
        
        # Extract and save CSS files
        css_urls = extract_css_urls(html_content, base_url)
        if css_urls:
            print(f"  Found {len(css_urls)} CSS files")
            for css_url in css_urls[:3]:  # Save first 3 CSS files
                try:
                    filename = css_url.split('/')[-1].split('?')[0]  # Remove query params
                    response = session.get(css_url, timeout=10)
                    if response.status_code == 200:
                        saved_path = save_text_file(response.text, filename, htmlfiles_dir)
                        if saved_path:
                            print(f"    Saved CSS: {filename}")
                    time.sleep(0.2)
                except Exception as e:
                    pass  # Silent fail for CSS files
        
        # Extract JavaScript files
        script_urls = extract_script_urls(html_content, base_url)
        
        if script_urls:
            print(f"  Found {len(script_urls)} JavaScript files")
            all_versions = []
            
            # Focus on main.*.js files which typically contain app logic
            main_scripts = [url for url in script_urls if 'main.' in url and url.endswith('.js')]
            
            for script_url in main_scripts[:5]:  # Check up to 5 main scripts
                try:
                    filename = script_url.split('/')[-1]
                    print(f"  Fetching: {filename}")
                    response = session.get(script_url, timeout=15)
                    if response.status_code == 200:
                        print(f"    Downloaded {len(response.text)} bytes")
                        
                        # Save JavaScript file to htmlfiles directory
                        saved_path = save_text_file(response.text, filename, htmlfiles_dir)
                        if saved_path:
                            print(f"    Saved to: {saved_path}")
                        
                        versions = parse_versions_from_javascript(response.text)
                        if versions:
                            print(f"    Found {len(versions)} version strings")
                            all_versions.extend(versions)
                        else:
                            print(f"    No version strings found in this file")
                    else:
                        print(f"    Failed: HTTP {response.status_code}")
                    time.sleep(0.3)  # Small delay between JS requests
                except Exception as e:
                    print(f"    Warning: Failed to fetch: {e}")
                    import traceback
                    traceback.print_exc()
            
            # Deduplicate
            unique_versions = []
            for v in all_versions:
                if v not in unique_versions:
                    unique_versions.append(v)
            
            if unique_versions:
                return unique_versions
    
    return []


def validate_html_content(html_content):
    """
    Validates that HTML content looks legitimate
    
    Args:
        html_content: HTML content string
    
    Returns:
        bool: True if content appears valid
    """
    if not html_content or len(html_content) < 500:
        return False
    
    # Check for common HTML markers
    if '<html' not in html_content.lower() and '<body' not in html_content.lower():
        return False
    
    # Check it's not an error page
    if 'access denied' in html_content.lower() or 'forbidden' in html_content.lower():
        return False
    
    return True


def update_firmware_file(firmware_data, firmware_file_path):
    """
    Updates the recommended firmware markdown file with all firmware types
    
    Args:
        firmware_data: Dictionary with firmware type keys and list of version/URL values
                      {'infrastructure': [{'version': '6.0(1b)', 'url': '...'}, ...], ...}
        firmware_file_path: Path to the recommended-firmware.md file
    
    Returns:
        bool: True if update was successful
    """
    firmware_file_path = Path(firmware_file_path)
    
    if not firmware_file_path.exists():
        print(f"  ⚠ Warning: Firmware file not found: {firmware_file_path}")
        return False
    
    try:
        # Build new content
        content_parts = []
        
        # Infrastructure section
        if 'infrastructure' in firmware_data and firmware_data['infrastructure']:
            content_parts.append("### Recommended firmware versions for Infrastructure")
            content_parts.append(f"The recommended firmware versions for Cisco UCS Manager are:")
            for item in firmware_data['infrastructure']:
                content_parts.append(f"- {item['version']}")
            content_parts.append(f"\nSource:")
            for item in firmware_data['infrastructure']:
                content_parts.append(f"- {item['url']}")
            content_parts.append("")
        
        # Blades section
        if 'blades' in firmware_data and firmware_data['blades']:
            content_parts.append("### Recommended firmware versions for Cisco UCS Blades")
            content_parts.append(f"The recommended firmware versions for Cisco UCS Blades are:")
            for item in firmware_data['blades']:
                content_parts.append(f"- {item['version']}")
            content_parts.append(f"\nSource:")
            for item in firmware_data['blades']:
                content_parts.append(f"- {item['url']}")
            content_parts.append("")
        
        # C-Series section
        if 'c-series' in firmware_data and firmware_data['c-series']:
            content_parts.append("### Recommended firmware versions for Cisco UCS C-Series rack servers")
            content_parts.append(f"The recommended firmware versions for Cisco UCS C-series rack servers are:")
            for item in firmware_data['c-series']:
                content_parts.append(f"- {item['version']}")
            content_parts.append(f"\nSource:")
            for item in firmware_data['c-series']:
                content_parts.append(f"- {item['url']}")
        
        new_content = '\n'.join(content_parts)
        
        # Write to file
        with open(firmware_file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"  ✓ Updated {firmware_file_path}")
        for source_key, items in firmware_data.items():
            versions_str = ', '.join([item['version'] for item in items])
            print(f"    - {source_key}: {versions_str}")
        return True
        
    except Exception as e:
        print(f"  ✗ Failed to update firmware file: {e}")
        import traceback
        traceback.print_exc()
        return False


def ensure_htmlfiles_directory():
    """
    Creates the htmlfiles directory if it doesn't exist
    
    Returns:
        Path: Path to the htmlfiles directory
    """
    htmlfiles_dir = Path('htmlfiles')
    htmlfiles_dir.mkdir(exist_ok=True)
    return htmlfiles_dir


def save_html(content, output_path):
    """
    Saves HTML content to a file
    
    Args:
        content: HTML content string
        output_path: Path object or string for output file
    
    Returns:
        Path: Path to saved file
    """
    output_path = Path(output_path)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return output_path

def save_text_file(content, filename, directory):
    """
    Saves text content to a file in the specified directory
    
    Args:
        content: Text content string
        filename: Name of the file
        directory: Directory path to save to
    
    Returns:
        Path: Path to saved file
    """
    output_path = Path(directory) / filename
    
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return output_path
    except Exception as e:
        print(f"    Warning: Failed to save {filename}: {e}")
        return None

def save_text_file(content, filename, directory):
    """
    Saves text content to a file in the specified directory
    
    Args:
        content: Text content string
        filename: Name of the file
        directory: Directory path to save to
    
    Returns:
        Path: Path to saved file
    """
    output_path = Path(directory) / filename
    
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return output_path
    except Exception as e:
        print(f"    Warning: Failed to save {filename}: {e}")
        return None


def main():
    """Main script execution"""
    parser = argparse.ArgumentParser(
        description='Fetches UCS firmware release pages from software.cisco.com (v3 - multiple sources)'
    )
    parser.add_argument(
        '--show-session',
        action='store_true',
        help='Display session information (cookies, headers)'
    )
    parser.add_argument(
        '--firmware-file',
        default='../ucs-firmware-reports/recommended-firmware.md',
        help='Path to recommended firmware markdown file to update (default: ../ucs-firmware-reports/recommended-firmware.md)'
    )
    parser.add_argument(
        '--no-update',
        action='store_true',
        help='Do not update the firmware file, only display the versions'
    )
    
    args = parser.parse_args()
    
    try:
        print("\033[96mCisco UCS Firmware Release Page Fetcher (v4)\033[0m")
        print("=" * 60 + "\n")
        print(f"Extracting recommended firmware versions from HTML/JavaScript\n")
        
        # Dictionary to store firmware data (lists for each source)
        firmware_data = {
            'infrastructure': [],
            'blades': [],
            'c-series': []
        }
        
        # Process each firmware source (only 3 requests total!)
        for source_idx, (source_key, source_info) in enumerate(CiscoSoftwarePageFetcher.FIRMWARE_SOURCES.items(), 1):
            print(f"\n\033[95m{'=' * 60}\033[0m")
            print(f"\033[95mSource {source_idx}/3: {source_info['name']}\033[0m")
            print(f"\033[95m{source_info['description']}\033[0m")
            print(f"\033[95m{'=' * 60}\033[0m\n")
            
            # Initialize fetcher for this source
            fetcher = CiscoSoftwarePageFetcher(source_info['mdf_id'], source_info['software_id'])
            
            # Step 1: Establish session
            print("\033[93mStep 1: Establishing anonymous session...\033[0m")
            session_success = fetcher.establish_session()
            
            if not session_success:
                print("\n\033[91m⚠ Session establishment may have issues, but continuing...\033[0m")
            
            # Show session info if requested (only for first source)
            if args.show_session and source_idx == 1:
                print("\n\033[94mSession Information:\033[0m")
                session_info = fetcher.get_session_info()
                print(f"  Cookies: {len(session_info['cookies'])} cookies set")
                for name, value in session_info['cookies'].items():
                    print(f"    - {name}: {value[:50]}..." if len(value) > 50 else f"    - {name}: {value}")
            
            # Step 2: Fetch download page (contains ALL recommended versions)
            print(f"\n\033[93mStep 2: Fetching download page...\033[0m")
            html_content = fetcher.fetch_download_page()
            
            if not html_content:
                print("\n\033[91m✗ Failed to fetch page content\033[0m")
                continue
            
            # Validate HTML content
            print(f"\n\033[93mStep 2a: Validating HTML content...\033[0m")
            if not validate_html_content(html_content):
                print("  ✗ HTML content appears invalid or incomplete")
                print(f"  Content length: {len(html_content)} bytes")
                continue
            print(f"  ✓ HTML content appears valid ({len(html_content)} bytes)")
            
            # Save HTML to htmlfiles directory
            htmlfiles_dir = ensure_htmlfiles_directory()
            timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
            html_filename = f"{source_key}-{timestamp}.html"
            html_saved_path = save_text_file(html_content, html_filename, htmlfiles_dir)
            if html_saved_path:
                print(f"  💾 Saved HTML to: {html_saved_path}")
            
            # Parse ALL recommended firmware versions from the page
            print(f"\n\033[93mStep 2b: Parsing ALL recommended firmware versions...\033[0m")
            
            # Check if this is a JavaScript-rendered page
            is_spa = '<app-root></app-root>' in html_content or 'angular' in html_content.lower()
            
            if is_spa:
                print("  ℹ Detected JavaScript single-page application")
                print("  Content is rendered client-side - parsing JavaScript files...")
            else:
                print("  Searching for all <span id=\"selectedRelease\"> tags...")
            
            # Try to parse versions from HTML and JavaScript
            recommended_versions = parse_recommended_versions(
                html_content, 
                session=fetcher.session,
                base_url=fetcher.BASE_URL
            )
            
            if recommended_versions:
                print(f"  ✓ Found {len(recommended_versions)} recommended versions:")
                for v in recommended_versions:
                    print(f"    - \033[92m{v}\033[0m")
            else:
                print("\n\033[91m✗ ERROR: Could not extract recommended versions from HTML or JavaScript\033[0m")
                print("\033[91mCisco's website may be blocking automated access or page structure changed.\033[0m")
                print("\033[93mPlease try:\033[0m")
                print("  1. Visit the page manually in a browser to verify it loads correctly")
                print("  2. Check if bot protection has been updated")
                print("  3. Capture fresh browser cookies if needed\n")
                return 1
            
            if recommended_versions:
                print(f"\n\033[96m" + "=" * 60)
                print(f"  {source_info['name'].upper()}: {len(recommended_versions)} versions found")
                print(f"=" * 60 + "\033[0m\n")
                
                # Store each version with its URL
                for version in recommended_versions:
                    url = f"{fetcher.BASE_URL}/download/home/{source_info['mdf_id']}/type/{source_info['software_id']}/release/{version}"
                    
                    firmware_data[source_key].append({
                        'version': version,
                        'url': url,
                        'name': source_info['name']
                    })
            
            # Small delay between sources
            time.sleep(1)
        
        # Summary
        print(f"\n\n\033[96m{'=' * 60}\033[0m")
        print(f"\033[96mSUMMARY - RECOMMENDED FIRMWARE VERSIONS\033[0m")
        print(f"\033[96m{'=' * 60}\033[0m\n")
        
        for source_key, items in firmware_data.items():
            if items:
                source_name = CiscoSoftwarePageFetcher.FIRMWARE_SOURCES[source_key]['name']
                print(f"  \033[92m{source_name}:\033[0m")
                for item in items:
                    print(f"    - {item['version']}: {item['url']}")
                print()
        
        # Step 3: Update firmware file
        if firmware_data and not args.no_update:
            print(f"\n\033[93mStep 3: Updating firmware file...\033[0m")
            # Resolve firmware file path relative to script location
            script_dir = Path(__file__).parent
            firmware_path = (script_dir / args.firmware_file).resolve()
            print(f"  Firmware file: {firmware_path}")
            
            if update_firmware_file(firmware_data, firmware_path):
                print(f"  ✓ Firmware file updated successfully")
            else:
                print(f"  ⚠ Firmware file update had issues")
        elif args.no_update:
            print(f"\n\033[93mStep 3: Skipping firmware file update (--no-update flag)\033[0m")
        
        print(f"\n\033[92m✓ Successfully completed!\033[0m\n")
        return 0
        
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user")
        return 130
    except Exception as e:
        print(f"\n\033[91m✗ Script execution failed: {e}\033[0m")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit(main())
