#!/Users/romoss/Git/github.com/romoss_cisco/ucs-datasheets-firmware/.venv/bin/python
#!/usr/bin/env python3.14
# venv:  /Users/romoss/Git/github.com/romoss_cisco/ucs-datasheets-firmware/.venv/bin/python
"""
Fetch Cisco UCS Firmware information from software.cisco.com
Extracts all Suggested Firmware versions from the download page.
Uses Selenium to bypass Akamai protection and handle JavaScript rendering.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import sys
import time


def fetch_firmware_versions(url):
    """
    Fetch the firmware page using Selenium and extract all suggested firmware versions.
    
    Args:
        url: The Cisco software download URL
        
    Returns:
        List of firmware version strings found, empty list if none found
    """
    driver = None
    try:
        print(f"Initializing Chrome browser...")
        
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # Run in background
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
        
        # Initialize the Chrome driver
        driver = webdriver.Chrome(options=chrome_options)
        
        # Remove webdriver property to avoid detection
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        print(f"Navigating to: {url}")
        driver.get(url)
        
        # Wait for the page to load and check for various scenarios
        print("Waiting for page to load...")
        time.sleep(5)  # Give time for JavaScript to execute
        
        # Try to wait for the selectedRelease element
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "selectedRelease"))
            )
            print("✓ Found selectedRelease element")
        except:
            print("⚠ selectedRelease element not found immediately, checking page content...")
        
        # Get the page source
        page_source = driver.page_source
        
        # Check if we hit a login page
        if 'login' in page_source.lower() or 'sign in' in page_source.lower() or 'authenticate' in page_source.lower():
            print("\n✗ Login page detected. This URL requires authentication.")
            print("\nTo access this data, you need to:")
            print("1. Log into software.cisco.com in your browser")
            print("2. Use browser cookies with this script")
            print("3. Or manually save the HTML file while logged in")
            return []
        
        # Parse with BeautifulSoup
        soup = BeautifulSoup(page_source, 'html.parser')
        
        # Find all spans with id="selectedRelease"
        selected_releases = soup.find_all('span', {'id': 'selectedRelease'})
        
        versions = []
        if selected_releases:
            print(f"\n✓ Found {len(selected_releases)} firmware version(s):")
            for idx, release in enumerate(selected_releases, 1):
                version = release.get_text(strip=True)
                if version:  # Only add non-empty versions
                    versions.append(version)
                    print(f"  {idx}. {version}")
        else:
            print("Warning: Could not find any selectedRelease span elements")
            
            # Debug: look for alternative selectors
            print("\nDebugging - searching for alternative elements:")
            
            # Try to find release information in other ways
            release_elements = soup.find_all('span', class_=lambda x: x and 'release' in str(x).lower())
            if release_elements:
                print(f"Found {len(release_elements)} elements with 'release' in class:")
                for elem in release_elements[:10]:
                    text = elem.get_text(strip=True)
                    if text:
                        print(f"  - {elem.get('class')}: {text}")
            
            # Save page source for debugging
            with open('/tmp/cisco_page_debug.html', 'w') as f:
                f.write(page_source)
            print(f"\n→ Page source saved to /tmp/cisco_page_debug.html for analysis")
        
        return versions
            
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return []
    finally:
        if driver:
            driver.quit()


def main():
    """Main function to execute the script."""
    # Default URL
    url = "https://software.cisco.com/download/home/283612660/type/283655658/release/6.0(1b)"
    
    # Allow URL to be passed as command line argument
    if len(sys.argv) > 1:
        url = sys.argv[1]
    
    versions = fetch_firmware_versions(url)
    
    if versions:
        print(f"\n✓ Success: Found {len(versions)} firmware version(s)")
        print(f"Versions: {', '.join(versions)}")
        return 0
    else:
        print("\n✗ Failed to extract firmware versions")
        return 1


if __name__ == "__main__":
    sys.exit(main())
