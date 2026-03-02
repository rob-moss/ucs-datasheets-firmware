#!/usr/bin/env python3
"""
pull-data.py
v2.0 - Python conversion of pull-data.sh

Pulls data from Cisco.com URLs defined in urldata.sh
- Downloads JSON files for HCL data
- Downloads HTML files and names them by their HTML <title>
- Processes whitepapers, release notes, datasheets, and CLI guides
"""

import os
import re
import sys
from pathlib import Path
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
from typing import Dict, Optional


# Default configuration
DEFAULT_URLDATA_FILE = 'urldata.sh'
DEFAULT_HTML_DIR = './ucs-firmware-docs-raw'
DEFAULT_JSON_DIR = './ucs-firmware-docs-raw/jsondata'


class DataPuller:
    """Main class for pulling Cisco UCS data files"""
    
    def __init__(self, urldata_file: str = DEFAULT_URLDATA_FILE, 
                 html_dir: str = DEFAULT_HTML_DIR,
                 json_dir: str = DEFAULT_JSON_DIR):
        self.urldata_file = urldata_file
        self.html_dir = Path(html_dir)
        self.json_dir = Path(json_dir)
        
        # Data dictionaries
        self.whitepapers: Dict[str, str] = {}
        self.relnotes: Dict[str, str] = {}
        self.datasheets: Dict[str, str] = {}
        self.cliguides: Dict[str, str] = {}
        self.hcl: Dict[str, str] = {}
        self.jsons: Dict[str, str] = {}
        
    def parse_urldata_file(self) -> None:
        """Parse the urldata.sh file to extract associative arrays"""
        print(f"* Parsing {self.urldata_file}")
        
        if not os.path.exists(self.urldata_file):
            print(f"ERROR: {self.urldata_file} not found")
            sys.exit(1)
            
        with open(self.urldata_file, 'r') as f:
            content = f.read()
        
        # Parse each associative array type
        self.whitepapers = self._parse_bash_array(content, 'whitepapers')
        self.relnotes = self._parse_bash_array(content, 'relnotes')
        self.datasheets = self._parse_bash_array(content, 'datasheets')
        self.cliguides = self._parse_bash_array(content, 'cliguides')
        self.hcl = self._parse_bash_array(content, 'hcl')
        self.jsons = self._parse_bash_array(content, 'jsons')
        
        print(f"  - Loaded {len(self.whitepapers)} whitepapers")
        print(f"  - Loaded {len(self.relnotes)} release notes")
        print(f"  - Loaded {len(self.datasheets)} datasheets")
        print(f"  - Loaded {len(self.cliguides)} CLI guides")
        print(f"  - Loaded {len(self.hcl)} HCL entries")
        print(f"  - Loaded {len(self.jsons)} JSON files")
        
    def _parse_bash_array(self, content: str, array_name: str) -> Dict[str, str]:
        """Parse a bash associative array from the content"""
        result = {}
        
        # Pattern to match: arrayname["key"]='value' or arrayname["key"]="value"
        pattern = rf'{array_name}\["([^"]+)"\]\s*=\s*[\'"]([^\'"]+)[\'"]'
        
        matches = re.findall(pattern, content)
        for key, value in matches:
            result[key] = value
            
        return result
    
    def get_json_to_file(self, url: str, filepath: Path) -> bool:
        """Download JSON data from URL to file"""
        print(f"  Pulling {url}")
        print(f"    -> {filepath}")
        
        try:
            response = requests.get(
                url,
                headers={'Content-Type': 'application/json'},
                stream=True,
                timeout=60
            )
            response.raise_for_status()
            
            # Write to file
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
                    
            print(f"    ✓ Downloaded successfully")
            return True
            
        except requests.exceptions.RequestException as e:
            print(f"    ✗ ERROR: {e}")
            return False
    
    def get_html_to_title(self, url: str) -> bool:
        """Download HTML and save with title as filename"""
        print(f"  Pulling {url}")
        
        try:
            # Download HTML
            response = requests.get(url, timeout=60)
            response.raise_for_status()
            
            html_content = response.text
            
            # Parse HTML to extract title
            soup = BeautifulSoup(html_content, 'html.parser')
            title_tag = soup.find('title')
            
            if title_tag and title_tag.string:
                title = title_tag.string.strip()
            else:
                # Fallback to URL-based filename if no title found
                parsed_url = urlparse(url)
                title = Path(parsed_url.path).stem or 'untitled'
            
            # Clean title for use as filename
            title = self._clean_filename(title)
            
            # Save to file
            filename = self.html_dir / f"{title}.html"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            print(f"    Title: \"{title}\"")
            print(f"    -> {filename}")
            print(f"    ✓ Downloaded successfully")
            return True
            
        except requests.exceptions.RequestException as e:
            print(f"    ✗ ERROR downloading: {e}")
            return False
        except Exception as e:
            print(f"    ✗ ERROR processing: {e}")
            return False
    
    def _clean_filename(self, filename: str) -> str:
        """Clean a string to be used as a filename"""
        # Remove or replace invalid filename characters
        cleaned = re.sub(r'[<>:"/\\|?*]', '-', filename)
        # Remove leading/trailing spaces and dots
        cleaned = cleaned.strip('. ')
        # Limit length (optional, but recommended)
        if len(cleaned) > 200:
            cleaned = cleaned[:200]
        return cleaned
    
    def create_directories(self) -> None:
        """Create output directories if they don't exist"""
        print("* Create directories")
        self.html_dir.mkdir(parents=True, exist_ok=True)
        self.json_dir.mkdir(parents=True, exist_ok=True)
        print(f"  - {self.html_dir}")
        print(f"  - {self.json_dir}")
    
    def pull_cli_guides(self) -> None:
        """Fetch CLI guides"""
        if not self.cliguides:
            return
            
        print(f"\n* Fetch CLI guides ({len(self.cliguides)} files)")
        for key, url in self.cliguides.items():
            self.get_html_to_title(url)
    
    def pull_release_notes(self) -> None:
        """Fetch release notes"""
        if not self.relnotes:
            return
            
        print(f"\n* Fetch release notes ({len(self.relnotes)} files)")
        for key, url in self.relnotes.items():
            self.get_html_to_title(url)
    
    def pull_datasheets(self) -> None:
        """Fetch datasheets"""
        if not self.datasheets:
            return
            
        print(f"\n* Fetch datasheets ({len(self.datasheets)} files)")
        for key, url in self.datasheets.items():
            self.get_html_to_title(url)
    
    def pull_whitepapers(self) -> None:
        """Fetch whitepapers"""
        if not self.whitepapers:
            return
            
        print(f"\n* Fetch whitepapers ({len(self.whitepapers)} files)")
        for key, url in self.whitepapers.items():
            self.get_html_to_title(url)
    
    def pull_hcl_json(self) -> None:
        """Fetch HCL JSON data"""
        if not self.hcl:
            return
            
        print(f"\n* Fetch HCL JSON data ({len(self.hcl)} files)")
        for key, url in self.hcl.items():
            filename = self.json_dir / f"{key}.json"
            self.get_json_to_file(url, filename)
    
    def pull_json_files(self) -> None:
        """Fetch JSON files (equivalency matrix, upgrade matrix, etc.)"""
        if not self.jsons:
            return
            
        print(f"\n* Fetch JSON data - equivalency matrix and upgrade matrix ({len(self.jsons)} files)")
        for key, url in self.jsons.items():
            filename = self.json_dir / f"{key}.json"
            self.get_json_to_file(url, filename)
    
    def run(self) -> None:
        """Main execution method"""
        print("* Setting up to pull data\n")
        
        # Parse URL data file
        self.parse_urldata_file()
        
        # Create directories
        self.create_directories()
        
        # Pull all data types
        self.pull_cli_guides()
        self.pull_release_notes()
        self.pull_datasheets()
        self.pull_whitepapers()
        self.pull_hcl_json()
        self.pull_json_files()
        
        print("\n* Data pull complete!")


def main():
    """Main entry point"""
    puller = DataPuller(
        urldata_file=DEFAULT_URLDATA_FILE,
        html_dir=DEFAULT_HTML_DIR,
        json_dir=DEFAULT_JSON_DIR
    )
    puller.run()


if __name__ == '__main__':
    main()
