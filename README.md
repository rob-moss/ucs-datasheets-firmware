# UCS Datasheets, HCL and Firmware

This project collects and processes UCS Datasheets, Hardware Compatibility List (HCL) data, and Firmware recommendations for Cisco UCS server products.

**Purpose**: Provide structured, AI-readable documentation for CIRCUIT and other AI LLMs to query specific UCS product information.

**Key Features**:
* Gathers UCS product datasheets in HTML format
* Collects UCS Manager Release notes (4.2, 4.3, and 6.0) in HTML format
* Downloads UCS HCL JSON files for common blade models (B200, B480) for VMware ESXi 6.7 U3, 7.0 U3, 8.0 U3
* Converts JSON files to Markdown format for AI consumption
* Generates comprehensive firmware compatibility reports
* Validates firmware data consistency across sources

---

## Setup and Requirements

### Python Environment Setup

This project requires Python 3.7 or higher. The Python scripts use only standard library modules, so no external dependencies are required for the main functionality.

**Create and activate a virtual environment**:
```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate
```

**Install dependencies**:
```bash
pip install requests beautifulsoup4 html2text pdfminer.six
```

---

## Fetching Cisco Documentation

### `fetch_cisco_docs.py`

This script reads a list of URLs from `urls.md` and downloads them in two phases:

**Phase 1 – Download**: fetches each URL and saves the raw file to the appropriate subdirectory under `ucs-docs-raw/`:

| File type | Raw output directory |
|-----------|----------------------|
| HTML pages (+ sub-pages) | `ucs-docs-raw/html/` |
| PDF files | `ucs-docs-raw/pdf/` |
| JSON files | `ucs-docs-raw/json/` |
| Other file types | `ucs-docs-raw/other/` |

**Phase 2 – Convert**: reads the saved raw files and converts them to Markdown, writing the output to `ucs-docs/`.

For JSON URLs the `Accept: application/json` header is set so the server returns structured JSON data. The converted Markdown includes a rendered table (or list/code block depending on structure) followed by a collapsible raw JSON appendix.

#### Basic usage

```bash
# Activate virtual environment first
source .venv/bin/activate

# Fetch all URLs listed in urls.md (default)
python3 fetch_cisco_docs.py

# Specify a different URLs file
python3 fetch_cisco_docs.py my-urls.md
```

#### CLI options

```
usage: fetch_cisco_docs.py [-h] [-o OUTPUT_DIR]
                           [--html-raw-dir HTML_RAW_DIR]
                           [--pdf-raw-dir PDF_RAW_DIR]
                           [--json-raw-dir JSON_RAW_DIR]
                           [--other-raw-dir OTHER_RAW_DIR]
                           [-d DELAY] [--max-pages MAX_PAGES]
                           [-f]
                           [urls_file]

positional arguments:
  urls_file             Path to the file containing URLs (default: urls.md)

optional arguments:
  -o, --output-dir      Markdown output directory (default: ./ucs-docs)
  --html-raw-dir        Directory for raw HTML files (default: ./ucs-docs-raw/html)
  --pdf-raw-dir         Directory for raw PDF files (default: ./ucs-docs-raw/pdf)
  --json-raw-dir        Directory for raw JSON files (default: ./ucs-docs-raw/json)
  --other-raw-dir       Directory for raw files of unrecognised type (default: ./ucs-docs-raw/other)
  -d, --delay           Delay between requests in seconds (default: 1.0)
  --max-pages           Maximum pages to fetch per HTML guide (default: 200)
  -f, --force           Force re-download of all files, ignoring freshness checks
```

#### Caching behaviour

The script skips re-downloading files that were already fetched within the last 24 hours. Use `-f` / `--force` to bypass all cache checks and re-download everything.

#### Output layout

```
ucs-docs/                          ← converted Markdown files
ucs-docs-raw/
    html/                          ← raw HTML pages (one file per page)
    pdf/                           ← raw PDF files
    json/                          ← raw JSON files
    other/                         ← raw files of unrecognised type
```

---

## Python Scripts

| Script | Output Files | Description |
|--------|--------------|-------------|
| **fetch_cisco_docs.py** | `ucs-docs/*.md`<br>`ucs-docs-raw/html/`<br>`ucs-docs-raw/pdf/`<br>`ucs-docs-raw/json/`<br>`ucs-docs-raw/other/` | Fetches Cisco documentation URLs from `urls.md` in two phases: download raw files to typed subdirectories under `ucs-docs-raw/`, then convert to Markdown in `ucs-docs/`. Supports HTML guides (with recursive sub-page crawling), PDF, JSON, and other file types. Includes 24-hour file cache and `--force` re-download flag. |
| **json_to_markdown.py** | `markdown_out/*.md` | General-purpose converter: transforms JSON/JSONL files to Markdown tables with collapsible raw JSON sections. Handles dicts, lists, and nested structures. Also used internally by `fetch_cisco_docs.py` for JSON rendering. |
| **extract_server_data.py** | `ucs-firmware-reports/server-adapter-driver-matrix-raw.md` | Extracts UCS blade server compatibility data from JSON files (v4). Generates comprehensive matrix showing blade models, CPU versions, ESXi versions, adapter models/firmware, and driver versions |
| **validate_firmware_data.py** | `validation_report.md`<br>`validation_report.txt` | Validates firmware data consistency (v5). Compares JSON files against markdown reports to identify discrepancies in blade configurations, adapters, ESXi versions, and drivers |

---

## AI Agent Prompt Files

Located in `.github/prompts/`, these files provide instructions for AI agents (like GitHub Copilot) to automate report generation:

| Prompt File | Output File(s) | Description |
|-------------|----------------|-------------|
| **refresh-data.prompt.md** | Various | Triggers a full documentation refresh cycle using `fetch_cisco_docs.py` |
| **process-server-firmware-adapter-matrix.prompt.md** | `ucs-firmware-reports/server-adapter-driver-matrix-raw.md` | Generates Python script (`extract_server_data.py`) to create UCS Server Hardware Compatibility Matrix from JSON files (v4) |
| **validate-server-firmware-adapter-matrix.prompt.md** | `validation_report.md`<br>`validation_report.txt` | Creates Python validation script (`validate_firmware_data.py`) to compare JSON data against markdown reports and identify discrepancies (v5) |
| **report-infra-server-models.prompt.md** | `ucs-firmware-reports/report-recommended-firmware.md` | Generates firmware recommendation report showing recommended versions for Infrastructure and Server models with compatibility matrices |
| **report-crossfirmware43.prompt.md** | `ucs-firmware-reports/report-ucs-crossfirmware-4.3.md` | Generates comprehensive cross-version firmware support report (v2) for UCS Manager 4.3, including infrastructure/server compatibility matrices, upgrade paths, and best practices |
| **push-all.prompt.md** | N/A | Executes `git push all` to push changes to all configured git remotes |

---

## Report Files

Located in `ucs-firmware-reports/`:

| Report File | Generated By | Description |
|-------------|--------------|-------------|
| **server-adapter-driver-matrix-raw.md** | `extract_server_data.py`<br>(via `process-server-firmware-adapter-matrix.prompt.md`) | Raw compatibility matrix showing blade models, CPU versions, ESXi versions, VIC adapters with firmware, and driver versions. Source data for other reports |
| **report-recommended-firmware.md** | AI agent via<br>`report-infra-server-models.prompt.md` | Consolidated firmware recommendations for UCS Infrastructure and Servers. Lists recommended versions: 6.0(1b) (Latest), 4.3(6c) (Recommended Stable), 4.2(3o) (Long-term Stable) with compatibility matrices |
| **report-ucs-crossfirmware-4.3.md** | AI agent via<br>`report-crossfirmware43.prompt.md` | Comprehensive cross-version firmware support report for UCS Manager 4.3. Includes infrastructure bundles, server bundles, fabric interconnect compatibility, IOM support, upgrade paths, and best practices |
| **recommended-firmware.md** | Manual/Legacy | Legacy firmware recommendations file |
| **ucs-crossfirmware-4.3.md** | Manual/Legacy | Legacy cross-firmware support documentation |

---

## Directories

| Directory | Description |
|-----------|-------------|
| **ucs-docs/** | Converted Markdown documentation files generated by `fetch_cisco_docs.py` |
| **ucs-docs-raw/** | Raw downloaded files, organised by type: `html/`, `pdf/`, `json/`, `other/` |
| **jsondata/** | JSON data files: HCL data, equivalency matrix, upgrade matrix, server/adapter compatibility data from cisco.com |
| **ucs-firmware-docs/** | UCS product datasheets and HCL data in HTML and Markdown formats. Ready for CIRCUIT AI project import |
| **ucs-firmware-reports/** | Generated firmware compatibility and recommendation reports in Markdown format |
| **wip/** | Work-in-progress files (can be ignored) |
| **.github/prompts/** | AI agent prompt instruction files for automated report generation |

---

## Workflow

### Fetch and Convert Cisco Documentation
```bash
source .venv/bin/activate
python3 fetch_cisco_docs.py
```
This will:
1. Read all URLs from `urls.md`
2. Download raw files to `ucs-docs-raw/html/`, `ucs-docs-raw/pdf/`, `ucs-docs-raw/json/`, or `ucs-docs-raw/other/` depending on file type
3. Convert each downloaded file to Markdown and write to `ucs-docs/`
4. Skip files already downloaded within the last 24 hours (use `-f` to force a full re-download)

### Force Re-download Everything
```bash
python3 fetch_cisco_docs.py --force
```

### Generate Specific Reports
Use AI agents (GitHub Copilot) with the prompt files:
1. Open desired prompt file from `.github/prompts/`
2. Execute the prompt instructions with AI agent
3. Generated reports appear in `ucs-firmware-reports/`

### Validate Data Consistency
```bash
python3 validate_firmware_data.py
```
Generates validation reports showing any discrepancies between JSON source data and markdown reports.

---

## Data Sources

All data is sourced from official Cisco documentation:
- Cisco UCS Hardware Compatibility List (HCL)
- Cisco UCS Manager Release Notes and Documentation
- Cisco UCS Product Datasheets
- Cisco UCS Cross-Version Firmware Support Documentation

---

## Version Information

- **extract_server_data.py**: v4
- **validate_firmware_data.py**: v5
- **report-crossfirmware43.prompt.md**: v2
- **Last Updated**: December 11, 2025


