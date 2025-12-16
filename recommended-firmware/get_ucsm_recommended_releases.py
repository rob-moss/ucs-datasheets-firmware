#!.venv/bin/python3
### #!/usr/bin/env python3
"""
Gets recommended releases for UCS Manager from software.cisco.com

This script authenticates anonymously to software.cisco.com and retrieves
the recommended software releases for UCS Manager.

Usage:
    python get_ucsm_recommended_releases.py
    python get_ucsm_recommended_releases.py --mdfid 283612660 --softwareid 283655658
"""

import argparse
import json
import requests
from datetime import datetime
from pathlib import Path


class CiscoSoftwareDownload:
    """Client for Cisco Software Download API"""
    
    BASE_URL = "https://software.cisco.com"
    
    def __init__(self, mdf_id, software_id):
        """
        Initialize the client
        
        Args:
            mdf_id: Product MDF ID (default: 283612660 for UCS Manager)
            software_id: Software type ID (default: 283655658 for UCS Manager Software)
        """
        self.mdf_id = mdf_id
        self.software_id = software_id
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9"
        })
    
    def get_anonymous_session(self):
        """
        Gets an anonymous session token from Cisco Software Download
        
        Makes an initial request to the download page which sets the swsession cookie
        containing a JWT token for anonymous access.
        
        Returns:
            bool: True if session was obtained successfully
        """
        print("Obtaining anonymous session token...")
        
        download_page_url = f"{self.BASE_URL}/download/home/{self.mdf_id}/type/{self.software_id}"
        
        try:
            headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
            }
            
            response = self.session.get(download_page_url, headers=headers, timeout=30)
            response.raise_for_status()
            
            # Check if swsession cookie was set
            if 'swsession' not in self.session.cookies:
                raise Exception("swsession cookie not found in response")
            
            print("  ✓ Successfully obtained session token")
            return True
            
        except Exception as e:
            print(f"  ✗ Failed to obtain session token: {e}")
            raise
    
    def get_software_releases(self):
        """
        Gets software releases for the Cisco product
        
        Returns:
            dict: Release data containing suggested, latest, and all releases
        """
        print(f"Retrieving releases for MDF ID: {self.mdf_id}, Software ID: {self.software_id}")
        
        # Generate timestamp (similar to original script)
        now = datetime.now()
        timestamp = f"L{now.strftime('%d%H%M%S%f')[:-3]}{now.strftime('%Y%m%d%H%M%S')}"
        
        # Build the API URL
        releases_url = f"{self.BASE_URL}/services/catalog/v1/releases"
        params = {
            'mdfid': self.mdf_id,
            'softwareId': self.software_id,
            'ts': timestamp
        }
        
        # Create headers
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Referer": f"{self.BASE_URL}/download/home/{self.mdf_id}/type/{self.software_id}"
        }
        
        try:
            response = self.session.get(releases_url, params=params, headers=headers, timeout=30)
            response.raise_for_status()
            
            print("  ✓ Successfully retrieved releases")
            return response.json()
            
        except Exception as e:
            print(f"  ✗ Failed to retrieve releases: {e}")
            raise


def format_release_output(releases_data):
    """
    Formats release information for console output
    
    Args:
        releases_data: Dictionary containing release information
    """
    print("\n" + "=" * 60)
    print("UCS Manager Software Releases")
    print("=" * 60 + "\n")
    
    # Display Suggested/Recommended Releases
    if releases_data.get('suggestedRelease'):
        print("\033[92mRECOMMENDED RELEASES:\033[0m")
        print("-" * 20)
        for release in releases_data['suggestedRelease']:
            print(f"  \033[93mVersion: {release.get('releaseVersion')}\033[0m")
            print(f"    Release Track: {release.get('bucket1', 'N/A')}")
            print(f"    Status: {release.get('releaseIndicator', 'N/A')}")
            print()
    
    # Display Latest Releases
    if releases_data.get('latestRelease'):
        print("\n\033[92mLATEST RELEASES (per major version):\033[0m")
        print("-" * 35)
        for release in releases_data['latestRelease']:
            print(f"  \033[93mVersion: {release.get('releaseVersion')}\033[0m")
            print(f"    Status: {release.get('releaseIndicator', 'N/A')}")
            print()
    
    # Display Deferred Releases
    if releases_data.get('deferredRelease'):
        deferred_count = len(releases_data['deferredRelease'])
        if deferred_count > 0:
            print(f"\n\033[91mDEFERRED RELEASES: {deferred_count} versions\033[0m")
    
    # Display Total
    total_count = len(releases_data.get('allRelease', []))
    print(f"\n\033[96mTotal Available Releases: {total_count}\033[0m")
    print("=" * 60 + "\n")


def export_to_json(data, output_dir=None):
    """
    Exports release data to JSON file
    
    Args:
        data: Release data to export
        output_dir: Directory to save file (default: script directory)
    
    Returns:
        Path: Path to exported file
    """
    if output_dir is None:
        output_dir = Path(__file__).parent
    else:
        output_dir = Path(output_dir)
    
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    filename = f"ucs-releases-{timestamp}.json"
    filepath = output_dir / filename
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    return filepath


def main():
    """Main script execution"""
    parser = argparse.ArgumentParser(
        description='Gets recommended releases for UCS Manager from software.cisco.com'
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
        help='Output directory for JSON export (default: script directory)'
    )
    parser.add_argument(
        '--no-export',
        action='store_true',
        help='Do not export to JSON file'
    )
    
    args = parser.parse_args()
    
    try:
        print("\033[96mCisco UCS Manager Release Information\033[0m")
        print("=" * 60 + "\n")
        
        # Step 1: Initialize client and get session
        print("\033[93mStep 1: Establishing anonymous session...\033[0m")
        client = CiscoSoftwareDownload(args.mdfid, args.softwareid)
        client.get_anonymous_session()
        print("\033[92m  ✓ Session established\033[0m")
        
        # Step 2: Get releases
        print("\n\033[93mStep 2: Retrieving release information...\033[0m")
        releases = client.get_software_releases()
        print("\033[92m  ✓ Release information retrieved\033[0m")
        
        # Step 3: Display results
        format_release_output(releases)
        
        # Step 4: Export to JSON (optional)
        if not args.no_export:
            filepath = export_to_json(releases, args.output)
            print(f"\033[90mFull data exported to: {filepath}\033[0m\n")
        
        return 0
        
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user")
        return 130
    except Exception as e:
        print(f"\n\033[91mScript execution failed: {e}\033[0m")
        return 1


if __name__ == "__main__":
    exit(main())
