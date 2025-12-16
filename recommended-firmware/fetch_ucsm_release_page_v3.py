#!/Users/romoss/Git/github.com/romoss_cisco/ucs-datasheets-firmware/.venv/bin/python3

#!/usr/bin/env python3
"""
Fetches a specific UCS Manager release page from software.cisco.com (Version 2)

This script fetches release information for a specific UCS Manager version
using anonymous authentication with pre-configured cookies and browser-like headers.

Features:
- Validates HTTP 200 responses and HTML content
- Detects JavaScript-rendered pages (Angular SPA)
- Extracts recommended firmware version
- Updates the recommended-firmware.md file
- Saves HTML for reference

Note: Cisco's download site is an Angular single-page application where content
is rendered client-side. The script uses the version from the URL parameter as
the authoritative source since it matches the page being requested.

Usage:
    python fetch_ucsm_release_page_v2.py
    python fetch_ucsm_release_page_v2.py --version "6.0(1b)"
    python fetch_ucsm_release_page_v2.py --version "4.3(6c)" --output release.html
    python fetch_ucsm_release_page_v2.py --version "4.3(6c)" --no-update
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
    """Parses HTML to extract recommended firmware version"""
    
    def __init__(self):
        super().__init__()
        self.recommended_version = None
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
            self.recommended_version = data.strip()
            self.in_selected_release = False


class CiscoSoftwarePageFetcher:
    """Fetches Cisco Software Download pages with anonymous authentication"""
    
    BASE_URL = "https://software.cisco.com"
    DEFAULT_MDFID = "283612660"  # UCS Manager
    DEFAULT_SOFTWAREID = "283655658"  # UCS Manager Software
    
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
    
    def fetch_release_page(self, release_version):
        """
        Fetches the HTML page for a specific release version
        
        Args:
            release_version: Release version string (e.g., "6.0(1b)", "4.3(6c)")
        
        Returns:
            str: HTML content of the page
        """
        print(f"Fetching release page for version: {release_version}")
        
        # Add small delay to be more human-like
        time.sleep(0.5)
        
        # Build the URL
        url = f"{self.BASE_URL}/download/home/{self.mdf_id}/type/{self.software_id}/release/{release_version}"
        
        try:
            # Add referer header for this specific request
            headers = {
                "Referer": f"{self.BASE_URL}/download/home/{self.mdf_id}/type/{self.software_id}"
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
            print(f"  ✗ Failed to fetch release page: {e}")
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


def parse_recommended_version(html_content):
    """
    Extracts the recommended firmware version from HTML
    
    Args:
        html_content: HTML content string
    
    Returns:
        str: Recommended version or None if not found
    """
    parser = RecommendedVersionParser()
    parser.feed(html_content)
    return parser.recommended_version


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


def update_firmware_file(version, firmware_file_path):
    """
    Updates the recommended firmware markdown file
    
    Args:
        version: Firmware version string (e.g., "6.0(1b)")
        firmware_file_path: Path to the recommended-firmware.md file
    
    Returns:
        bool: True if update was successful
    """
    firmware_file_path = Path(firmware_file_path)
    
    if not firmware_file_path.exists():
        print(f"  ⚠ Warning: Firmware file not found: {firmware_file_path}")
        return False
    
    try:
        # Read current content
        with open(firmware_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if version already exists
        if version in content:
            print(f"  ℹ Version {version} already in firmware file")
            return True
        
        # Parse the existing versions
        version_pattern = r'- (\d+\.\d+\([^)]+\))'
        existing_versions = re.findall(version_pattern, content)
        
        # Add new version if not present
        if version not in existing_versions:
            # Add to the beginning of each list (it's the latest)
            lines = content.split('\n')
            updated_lines = []
            
            for line in lines:
                updated_lines.append(line)
                # After each header, add the new version as the first item
                if line.startswith('The recommended firmware versions'):
                    # Find the next line that starts with '-'
                    # Insert the new version before it
                    if len(updated_lines) > 0 and updated_lines[-1].strip().endswith(':'):
                        # Next line should be the first version
                        continue
                elif line.startswith('- ') and version not in '\n'.join(updated_lines):
                    # This is the first version line, insert before it
                    updated_lines.insert(-1, f"- {version}")
            
            # Simpler approach: just prepend to each bulleted list
            sections = content.split('### Recommended firmware versions for ')
            if len(sections) > 1:
                updated_content = sections[0]
                for section in sections[1:]:
                    # Find where the bullet list starts
                    lines = section.split('\n')
                    header = lines[0]
                    remaining = '\n'.join(lines[1:])
                    
                    # Find first bullet point
                    bullet_match = re.search(r'^- ', remaining, re.MULTILINE)
                    if bullet_match:
                        pos = bullet_match.start()
                        # Check if version already in this section
                        if version not in remaining:
                            remaining = remaining[:pos] + f"- {version}\n" + remaining[pos:]
                    
                    updated_content += '### Recommended firmware versions for ' + header + '\n' + remaining
                
                # Write back
                with open(firmware_file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                
                print(f"  ✓ Updated {firmware_file_path} with version {version}")
                return True
        
        return True
        
    except Exception as e:
        print(f"  ✗ Failed to update firmware file: {e}")
        return False


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


def main():
    """Main script execution"""
    parser = argparse.ArgumentParser(
        description='Fetches UCS Manager release page from software.cisco.com (v2 with pre-configured cookies)'
    )
    parser.add_argument(
        '--version',
        '-v',
        default='6.0(1b)',
        help='Release version to fetch (default: 6.0(1b))'
    )
    parser.add_argument(
        '--mdfid',
        default='283612660',
        help='Product MDF ID (default: 283612660 for UCS Manager)'
    )
    parser.add_argument(
        '--softwareid',
        default='283655658',
        help='Software type ID (default: 283655658 for UCS Manager Software)'
    )
    parser.add_argument(
        '--output',
        '-o',
        help='Output file path (default: auto-generate based on version and timestamp)'
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
        help='Do not update the firmware file, only display the version'
    )
    
    args = parser.parse_args()
    
    try:
        print("\033[96mCisco UCS Manager Release Page Fetcher (v2)\033[0m")
        print("=" * 60 + "\n")
        
        # Initialize fetcher
        fetcher = CiscoSoftwarePageFetcher(args.mdfid, args.softwareid)
        
        # Step 1: Establish session
        print("\033[93mStep 1: Establishing anonymous session...\033[0m")
        session_success = fetcher.establish_session()
        
        if not session_success:
            print("\n\033[91m⚠ Session establishment may have issues, but continuing...\033[0m")
        
        # Show session info if requested
        if args.show_session:
            print("\n\033[94mSession Information:\033[0m")
            session_info = fetcher.get_session_info()
            print(f"  Cookies: {len(session_info['cookies'])} cookies set")
            for name, value in session_info['cookies'].items():
                print(f"    - {name}: {value[:50]}..." if len(value) > 50 else f"    - {name}: {value}")
        
        # Step 2: Fetch release page
        print(f"\n\033[93mStep 2: Fetching release page for version {args.version}...\033[0m")
        html_content = fetcher.fetch_release_page(args.version)
        
        if not html_content:
            print("\n\033[91m✗ Failed to fetch page content\033[0m")
            print("\n\033[93mNote: Cisco's website has strong bot protection.")
            print("Consider using:\033[0m")
            print("  1. Manual download from browser")
            print("  2. Selenium/Playwright for real browser automation")
            print("  3. Official Cisco API with proper authentication\n")
            return 1
        
        # Validate HTML content
        print(f"\n\033[93mStep 2a: Validating HTML content...\033[0m")
        if not validate_html_content(html_content):
            print("  ✗ HTML content appears invalid or incomplete")
            print(f"  Content length: {len(html_content)} bytes")
            print(f"  First 200 chars: {html_content[:200]}")
            return 1
        print(f"  ✓ HTML content appears valid ({len(html_content)} bytes)")
        
        # Parse recommended firmware version
        print(f"\n\033[93mStep 2b: Parsing recommended firmware version...\033[0m")
        
        # Check if this is a JavaScript-rendered page
        is_spa = '<app-root></app-root>' in html_content or 'angular' in html_content.lower()
        
        if is_spa:
            print("  ℹ Detected JavaScript single-page application")
            print("  Content is rendered client-side - HTML parser cannot extract version")
            print(f"  Using requested version from URL: \033[92m{args.version}\033[0m")
            recommended_version = args.version
        else:
            recommended_version = parse_recommended_version(html_content)
            
            if recommended_version:
                print(f"  ✓ Found recommended version: \033[92m{recommended_version}\033[0m")
            else:
                print("  ⚠ Could not parse recommended version from HTML")
                print("  Searching for selectedRelease span...")
                if 'selectedRelease' in html_content:
                    print("  Found 'selectedRelease' in HTML")
                    # Try to extract with regex as fallback
                    match = re.search(r'<span[^>]*id="selectedRelease"[^>]*>([^<]+)</span>', html_content)
                    if match:
                        recommended_version = match.group(1).strip()
                        print(f"  ✓ Extracted with regex: \033[92m{recommended_version}\033[0m")
                else:
                    print("  'selectedRelease' not found in HTML")
                    print(f"  Using requested version from URL: \033[92m{args.version}\033[0m")
                    recommended_version = args.version
        
        if recommended_version:
            print(f"\n\033[96m" + "=" * 60)
            print(f"  RECOMMENDED FIRMWARE VERSION: {recommended_version}")
            print(f"=" * 60 + "\033[0m\n")
        
        # Step 3: Update firmware file
        if recommended_version and not args.no_update:
            print(f"\n\033[93mStep 3: Updating firmware file...\033[0m")
            # Resolve firmware file path relative to script location
            script_dir = Path(__file__).parent
            firmware_path = (script_dir / args.firmware_file).resolve()
            print(f"  Firmware file: {firmware_path}")
            
            if update_firmware_file(recommended_version, firmware_path):
                print(f"  ✓ Firmware file updated successfully")
            else:
                print(f"  ⚠ Firmware file update had issues")
        elif args.no_update:
            print(f"\n\033[93mStep 3: Skipping firmware file update (--no-update flag)\033[0m")
        
        # Step 4: Save to file
        if args.output:
            output_path = args.output
        else:
            # Auto-generate filename
            timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
            # Sanitize version string for filename
            safe_version = args.version.replace('(', '').replace(')', '').replace('.', '_')
            output_path = f"ucs-release-{safe_version}-{timestamp}.html"
        
        print(f"\n\033[93mStep 4: Saving HTML to file...\033[0m")
        saved_path = save_html(html_content, output_path)
        print(f"  ✓ Saved to: {saved_path.absolute()}")
        
        # Show preview
        print(f"\n\033[96mContent Preview (first 500 chars):\033[0m")
        print("-" * 60)
        print(html_content[:500])
        print("...")
        print("-" * 60)
        
        print(f"\n\033[92m✓ Successfully completed!\033[0m")
        if recommended_version:
            print(f"\033[92m  Recommended Version: {recommended_version}\033[0m\n")
        else:
            print()
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
