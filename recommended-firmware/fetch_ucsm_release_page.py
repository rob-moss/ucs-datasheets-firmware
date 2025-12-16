#!/Users/romoss/Git/github.com/romoss_cisco/ucs-datasheets-firmware/.venv/bin/python3

#!/usr/bin/env python3
"""
Fetches a specific UCS Manager release page from software.cisco.com

This script fetches release information for a specific UCS Manager version
using anonymous authentication and browser-like headers.

Usage:
    python fetch_ucsm_release_page.py
    python fetch_ucsm_release_page.py --version "6.0(1b)"
    python fetch_ucsm_release_page.py --version "4.3(6c)" --output release.html
"""

import argparse
import requests
import time
from pathlib import Path
from datetime import datetime


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
            response.raise_for_status()
            
            # Check if we got session cookies
            if 'swsession' in self.session.cookies:
                print(f"  ✓ Session established (swsession cookie received)")
            else:
                print(f"  ⚠ Session established (but no swsession cookie)")
            
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
            response.raise_for_status()
            
            print(f"  ✓ Successfully fetched page ({len(response.text)} bytes)")
            print(f"  ✓ Status code: {response.status_code}")
            print(f"  ✓ Final URL: {response.url}")
            
            return response.text
            
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
        description='Fetches UCS Manager release page from software.cisco.com'
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
    
    args = parser.parse_args()
    
    try:
        print("\033[96mCisco UCS Manager Release Page Fetcher\033[0m")
        print("=" * 60 + "\n")
        
        # Initialize fetcher
        fetcher = CiscoSoftwarePageFetcher(args.mdfid, args.softwareid)
        
        # Step 1: Establish session
        print("\033[93mStep 1: Establishing anonymous session...\033[0m")
        fetcher.establish_session()
        
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
        
        # Step 3: Save to file
        if args.output:
            output_path = args.output
        else:
            # Auto-generate filename
            timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
            # Sanitize version string for filename
            safe_version = args.version.replace('(', '').replace(')', '').replace('.', '_')
            output_path = f"ucs-release-{safe_version}-{timestamp}.html"
        
        print(f"\n\033[93mStep 3: Saving to file...\033[0m")
        saved_path = save_html(html_content, output_path)
        print(f"  ✓ Saved to: {saved_path.absolute()}")
        
        # Show preview
        print(f"\n\033[96mContent Preview (first 500 chars):\033[0m")
        print("-" * 60)
        print(html_content[:500])
        print("...")
        print("-" * 60)
        
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
