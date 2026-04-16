# TODO list

* Fix the JSON outputs in `ucs-docs-raw/searchResults` to re-use the expected names ie `ucsm-b200m5-v1-esxi-8u3.json` etc
  * Potentially download the entire JSON struct and then create separate JSON files for each relevant section (e.g., firmware versions, datasheets, guides) with the expected naming convention for easier consumption by the prompts
* fix the prompt `process-server-firmware-adapter-matrix.prompt.md` 
* fix the prompt `validate-server-firmware-adapter-matrix.prompt.md`
* fix the prompt `report-infra-server-models.prompt.md`
* fix the prompt `report-crossfirmware43.prompt.md`



* Clean up headings, navigation, and irrelevant content during HTML to Markdown conversion
  * Make Markdown files more concise and focused on the relevant information for firmware versions and datasheets
  * Deduplicate content across multiple sources to avoid redundancy in the Markdown files
  * Remove boilerplate content that is not relevant to the firmware information, such as navigation menus, footers, and unrelated sections of the documentation
* better logic to handle URLs for UCSM, IMM, UCS Hardware, X-Series hardware, Intersight, etc. to ensure that the correct documents are fetched and processed for each category
  * For example, use specific URL patterns or keywords to identify which documents belong to UCSM, which belong to IMM, etc., and organize the Markdown files accordingly in the ucs-docs directory
  * Use the URL patterns to categorize the documents and ensure that the correct information is extracted for each category, such as firmware versions, datasheets, and guides
  * Set the file prefix accordingly based on the category (e.g., ucsm- for UCS Manager, imm- for Intersight Managed Mode, etc.) to maintain consistency and organization in the Markdown files
  * ucsm for all UCS Manager docs
  * imm for all Intersight Managed Mode docs
  * ucshw for all UCS Hardware docs
  * wp for all Whitepapers
  * ishelp for all Intersight Help docs
  * ucsxhw for all X-Series Hardware docs


# Reports
* IMM BIOS Defaults (tokens) list with explanations of each token, default value and how it is used in the Intersight BIOS Profile
* Recommended firmware for UCS and IMM
* UCSM compat matrix of servers, adapters, firmware, esxi ver, nfnic/nenic
  * update fetch script to save JSON files with filename expecrted by prompt
* IMM compat matrix of servers, adapters, firmware, esxi ver, nfnic/nenic

* Review UCS docs to identify conflicting information. Produce a report with links and summary details to send to doc owners
  * Make a list of use cases / issues that are not clearly documented or have conflicting information
  


# Recommended Firmware Versions

### UCS Manager
- Consistently fetch the Recommended Firmware versions for both infrastructure and servers, and update the report [ucs-recommended-firmware](ucs-firmware-reports/ucsm-recommended-firmware.md) accordingly


### Intersight Managed Mode
- Fetch the latest recommended firmware versions for Intersight Managed Mode and update the report [imm-recommended-firmware](ucs-firmware-reports/imm-recommended-firmware.md) accordingly
* May need to fetch from Intersight API or parse from Intersight documentation, depending on where the information is available
* Intersight API path
* Inersitght documentation path

* If there are discrepancies between Intersight documentation and API data, use Intersight API first, and write a warning in the report about the discrepancy and the source of the data




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

* Add metadata to Markdown files
  * source URL
  * fetch date, etc.
* Create MCP server to expose the Markdown files to AI assistants, and update the README with instructions for use
* Implement checks to avoid re-downloading files that haven't changed since the last fetch (using timestamps or checksums)
* Implement error handling and logging in data fetching and conversion processes
