
# Directories
DEFAULT_URLDATA_FILE = 'urls.md''
DEFAULT_HTML_DIR = './ucs-docs-raw/html'
DEFAULT_PDF_DIR = './ucs-docs-raw/pdf'
DEFAULT_JSON_DIR = './ucs-docs-raw/json'
DEFAULT_MARKDOWN_DIR = './ucs-docs' # Markdown output directory: `./ucs-docs`


# TODO

* Clean up headings, navigation, and irrelevant content during HTML to Markdown conversion
* Add metadata to Markdown files
  * source URL
  * fetch date, etc.
* Implement error handling and logging in data fetching and conversion processes
* Create MCP server to expose the Markdown files to AI assistants, and update the README with instructions for use




### Recommended Firmware Versions
* UCS Manager - Consistently fetch the Recommended Firmware versions for both infrastructure and servers, and update the report [ucs-recommended-firmware](ucs-firmware-reports/ucsm-recommended-firmware.md) accordingly
* Intersight Managed Mode - Fetch the latest recommended firmware versions for Intersight Managed Mode and update the report [imm-recommended-firmware](ucs-firmware-reports/imm-recommended-firmware.md) accordingly


### Merge

* Implement checks to avoid re-downloading files that haven't changed since the last fetch (using timestamps or checksums)



### Done
* Implement checks to avoid re-downloading files that haven't changed since the last fetch (using timestamps or checksums)
* Move all HTML, JSON files to ucs-firmware-docs-raw
* Convert all Shell scripts to Python for better maintainability and error handling
* Convert urldata.sh to urls.md with proper formatting and metadata
  * Use proper Markdown ie "- [URL description/HTML Title](URL) - additional info"
* Convert all HTML, JSON files to Markdown and save in ucs-docs
* Update query agent to search ucs-docs instead of ucs-firmware-docs-raw
* Merge ucs-firmware-reports and ucs-guides-help-query into a single repository for better organization and maintenance
* Update ucs-guides-help-query/fetch_cisco_guides.py to fetch HTML files and place them in ucs-docs-raw, and then convert to Markdown in ucs-docs

