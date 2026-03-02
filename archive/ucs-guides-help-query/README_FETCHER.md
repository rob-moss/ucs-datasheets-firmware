# Cisco Documentation Fetcher

This script recursively fetches Cisco UCS documentation pages and converts them to Markdown format.

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Basic usage:

```bash
python fetch_cisco_docs.py urls.md
```

This will:
1. Read all URLs from `urls.md`
2. Fetch each documentation guide and all its sub-pages
3. Convert the HTML content to Markdown
4. Save each guide as a single `.md` file in the current directory

### Options

```bash
python fetch_cisco_docs.py urls.md -o ucs-guides-help-query -d 1.5 --max-pages 300
```

- `-o, --output-dir`: Directory to save markdown files (default: current directory)
- `-d, --delay`: Delay between requests in seconds (default: 1.0) - be respectful to Cisco's servers
- `--max-pages`: Maximum pages to fetch per guide (default: 200) - safety limit

### Examples

Fetch all docs and save to `ucs-guides-help-query` folder:
```bash
python fetch_cisco_docs.py urls.md -o ucs-guides-help-query
```

Fetch with longer delay (2 seconds) between requests:
```bash
python fetch_cisco_docs.py urls.md -o ucs-guides-help-query -d 2.0
```

## Output

Each main URL will generate one markdown file named after the original HTML file. For example:

- `https://...b_cisco_ucs_manager_server_mgmt_guide_4_3.html` → `b_cisco_ucs_manager_server_mgmt_guide_4_3.md`

Each output file contains:
- A header with the source URL and fetch timestamp
- All pages from that documentation guide
- Each sub-page is separated with page headers and dividers

## Notes

- The script is respectful of Cisco's servers with built-in delays between requests
- It automatically detects and follows links within the same documentation guide
- Navigation elements, scripts, and styles are removed during conversion
- The script maintains the document structure using Markdown formatting
