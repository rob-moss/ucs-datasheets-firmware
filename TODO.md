
# Directories
DEFAULT_URLDATA_FILE = 'urldata.sh'
DEFAULT_HTML_DIR = './ucs-firmware-docs-raw'
DEFAULT_JSON_DIR = './ucs-firmware-docs-raw/jsondata'
DEFAULT_MARKDOWN_DIR = './ucs-firmware-docs' # Markdown output directory: `./ucs-firmware-docs`


# TODO

* Convert all Shell scripts to Python for better maintainability and error handling
* Convert urldata.sh to urls.md with proper formatting and metadata
  * Use proper Markdown ie "- [URL description/HTML Title](URL) - additional info"


* Convert all HTML, JSON files to Markdown and save in ucs-firmware-docs
* Update query agent to search ucs-firmware-docs instead of ucs-firmware-doc
* Clean up headings, navigation, and irrelevant content during HTML to Markdown conversion
* Add metadata to Markdown files
  * source URL
  * fetch date, etc.
* Implement error handling and logging in data fetching and conversion processes

### Recommended Firmware Versions
* UCS Manager - Consistently fetch the Recommended Firmware versions for both infrastructure and servers, and update the report [ucs-recommended-firmware](ucs-firmware-reports/ucsm-recommended-firmware.md) accordingly
* Intersight Managed Mode - Fetch the latest recommended firmware versions for Intersight Managed Mode and update the report [imm-recommended-firmware](ucs-firmware-reports/imm-recommended-firmware.md) accordingly


### Merge
* Merge ucs-firmware-reports and ucs-guides-help-query into a single repository for better organization and maintenance
* Implement checks to avoid re-downloading files that haven't changed since the last fetch (using timestamps or checksums)
* Update ucs-guides-help-query/fetch_cisco_guides.py to fetch HTML files and place them in ucs-firmware-docs-raw, and then convert to Markdown in ucs-firmware-docs



### Done
* Implement checks to avoid re-downloading files that haven't changed since the last fetch (using timestamps or checksums)
* Move all HTML, JSON files to ucs-firmware-docs-raw
