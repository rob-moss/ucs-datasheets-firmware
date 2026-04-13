# UCS Datasheets, HCL and Firmware

This project collects and processes UCS Datasheets, Hardware Compatibility List (HCL) data, and Firmware documentation for Cisco UCS server products.

**Purpose**: Provide structured, AI-readable documentation for CIRCUIT and other AI LLMs to query specific UCS product information.

**Key Features**:
* Fetches UCS Manager configuration guides and release notes from cisco.com (HTML, recursive sub-page crawl)
* Fetches Intersight SaaS and Appliance help guides from intersight.com via the Intersight CDN (no browser / JS required)
* Downloads structured JSON data files (HCL queries, equivalency and upgrade matrices) and renders them as Markdown tables
* Downloads PDF documentation and extracts text to Markdown
* Generates enriched Markdown headers with URL title, source URL, CDN long URL, HTML page title, file type, and fetch timestamp
* Generates comprehensive firmware compatibility reports
* Validates firmware data consistency across sources

---

## Setup and Requirements

### Python Environment Setup

Requires Python 3.10 or higher (uses `str | None` union syntax).

**Create and activate a virtual environment**:
```bash
python3 -m venv .venv
source .venv/bin/activate       # macOS / Linux
.venv\Scripts\activate          # Windows
```

**Install dependencies**:
```bash
pip install requests beautifulsoup4 html2text pdfminer.six
```

The main fetch script (`fetch-cisco-docs.py`) is self-contained — all JSON-to-Markdown conversion logic is inlined; no additional local modules are required.

---

## Fetching Documentation

### `fetch-cisco-docs.py` (v10)

Reads a list of URLs from `urls.md` (Markdown link syntax `[Title](URL)` or bare URLs) and, for each URL:

1. **Downloads** the raw file to the appropriate subdirectory under `ucs-docs-raw/`.
2. **Converts** the content to Markdown and writes it to `ucs-docs/`.

Each output Markdown file starts with a metadata table:

| Field | Source |
|---|---|
| **URL Title** | Label from `urls.md` (`[Title](URL)`) |
| **URL** | The canonical URL (cisco.com or intersight.com help URL) |
| **Long URL** | Resolved Intersight CDN URL (blank for non-Intersight pages) |
| **HTML Title** | Text of the HTML `<title>` element (blank for PDF / JSON) |
| **Source file** | Path to the cached raw file under `ucs-docs-raw/` |
| **File type** | `HTML`, `PDF`, `JSON`, or extension-derived label |
| **Fetched on** | Timestamp of the fetch |

---

### Fetching cisco.com pages

cisco.com documentation URLs are HTML guides that span multiple sub-pages. The script:

1. Fetches the base page and caches it to `ucs-docs-raw/html/`.
2. Extracts all same-guide links (`<a href>`) and recursively crawls sub-pages up to `--max-pages` (default 200).
3. Combines all pages into a single Markdown file in `ucs-docs/`, with each page rendered under a `## Page N` heading.
4. Strips the trailing ` - Cisco` suffix from HTML `<title>` elements on cisco.com pages.
5. Output filename is derived from the HTML `<title>` (preferred) or the urls.md label, prefixed with `ucs-`.

**Raw cache**: `ucs-docs-raw/html/<slug>.html` (one file per sub-page)  
**Markdown output**: `ucs-docs/ucs-<Title>.md`

---

### Fetching intersight.com pages

Intersight help pages (`intersight.com/help/…`) are JavaScript-rendered and cannot be fetched directly. The script resolves them via the Intersight CDN without using a browser:

1. **CDN version discovery**: scrapes `https://intersight.com/help/saas` on every run to extract the current CDN bundle version (e.g. `5.2.1-12345`). No disk cache — always live.
2. **Route tables**: fetches `{CDN_BASE}/model/en/cloud-model.json` (SaaS) and `{CDN_BASE}/model/en/onprem-model.json` (Appliance) to build a URL-path → CDN-URL mapping. These model files are cached to `ucs-docs-raw/json/`.
3. **Content fetch**: the resolved CDN URL (a static HTML fragment) is fetched with Intersight CDN headers. The `<article>` / `<main>` / `<body>` content is extracted and converted to Markdown.
4. **Client-rendered pages** (`/help/saas`, `/help/saas/glossary`, `/help/saas/resources`): generated directly from the model JSON; no CDN HTML page is fetched.
5. **Appliance fallbacks**: a hardcoded map covers appliance routes not present in `onprem-model.json`.
6. A 403 on any CDN page is a non-fatal skip (logged, execution continues).

**SaaS** URL pattern: `intersight.com/help/saas/…`  
**Appliance** URL pattern: `intersight.com/help/appliance/…`  
**Raw cache**: `ucs-docs-raw/html/intersight-<saas|appliance>-<slug>.html`  
**Markdown output**: `ucs-docs/intersight-<slug>.md`  
**Long URL** field in the header contains the resolved CDN URL for traceability.

---

### Fetching JSON data files

JSON URLs (including dynamic HCL query endpoints on `pwc014-nextgen-prod-rcdn.cisco.com`) are handled as follows:

- URLs with a query string (`?…`) or matching the known dynamic-host prefix are always fetched fresh (never served from cache).
- The response is parsed as JSON (or JSON Lines if standard JSON parse fails).
- Rendered to Markdown as:
  - `dict` → two-column key/value table
  - `list[dict]` → multi-column table (union of all keys)
  - `list[scalars]` → bullet list
  - complex/mixed → fenced `json` code block
- A collapsible `<details>` raw JSON appendix is appended for full fidelity.
- Filename is prefixed with `json-` and derived from the urls.md title.

**Raw cache**: `ucs-docs-raw/json/<slug>.json`  
**Markdown output**: `ucs-docs/json-<Title>.md`

---

### Fetching PDF files

PDF URLs are downloaded and text is extracted using `pdfminer.six`.

**Raw cache**: `ucs-docs-raw/pdf/<slug>.pdf`  
**Markdown output**: `ucs-docs/ucs-<Title>.md`

---

### Caching behaviour

All raw files are cached for 24 hours. The script skips re-downloading any file whose cached copy is less than 24 hours old. Use `-f` / `--force` to bypass all cache checks and re-fetch everything.

Dynamic URLs (query-string or HCL host) are **never** cached.

---

### Basic usage

```bash
source .venv/bin/activate

# Fetch all URLs in urls.md (default)
python3 fetch-cisco-docs.py

# Use a different URLs file
python3 fetch-cisco-docs.py my-urls.md

# Force re-download everything
python3 fetch-cisco-docs.py --force
```

If HTTP_PROXY / HTTPS_PROXY (or lowercase variants) are set in the environment,
the script automatically uses them. Hosts listed in NO_PROXY / no_proxy bypass
the proxy.

### CLI options

```
usage: fetch-cisco-docs.py [-h] [-o OUTPUT_DIR] [-d DELAY]
                           [--max-pages MAX_PAGES] [-f]
                           [urls_file]

positional arguments:
  urls_file             Markdown file containing URLs (default: urls.md)

optional arguments:
  -o, --output-dir      Markdown output directory (default: ./ucs-docs)
  -d, --delay           Seconds between HTTP requests (default: 0.0)
  --max-pages           Max sub-pages per HTML guide (default: 200)
  -f, --force           Re-download everything, ignoring cache
```

### Output layout

```
ucs-docs/                          ← converted Markdown files
ucs-docs-raw/
    html/                          ← raw HTML pages (one file per fetched sub-page)
    pdf/                           ← raw PDF files
    json/                          ← raw JSON files + cloud-model.json / onprem-model.json
    other/                         ← raw files of unrecognised type
```

---

## URL input format (`urls.md`)

URLs are read from `urls.md`. Both formats are supported:

```markdown
[Title label](https://example.com/page)   ← title captured as URL Title
https://example.com/bare-url              ← URL Title will be blank
```

Lines starting with `#` and blank lines are ignored. Duplicate URLs are deduplicated (first occurrence wins).

---

## Python Scripts

| Script | Output | Description |
|--------|--------|-------------|
| **fetch-cisco-docs.py** (v10) | `ucs-docs/*.md`<br>`ucs-docs-raw/html/`<br>`ucs-docs-raw/pdf/`<br>`ucs-docs-raw/json/`<br>`ucs-docs-raw/other/` | Single-file fetcher and converter. Handles cisco.com HTML guides (recursive crawl), intersight.com help pages (CDN route resolution, no browser), JSON data endpoints (dynamic HCL queries + static files), and PDF extraction. JSON-to-Markdown conversion is inlined; no external local modules required. Enriched Markdown headers include URL Title, URL, Long URL, HTML Title, Source file, File type, and Fetched on. |
| **archive/extract_server_data.py** | `ucs-firmware-reports/server-adapter-driver-matrix-raw.md` | Extracts UCS blade server compatibility data from JSON files (v4). Generates matrix of blade models, CPU versions, ESXi versions, adapter models/firmware, and driver versions. |
| **archive/validate_firmware_data.py** | `validation_report.md`<br>`validation_report.txt` | Validates firmware data consistency (v5). Compares JSON source files against Markdown reports to identify discrepancies. |

---

## AI Agent Prompt Files

Located in `.github/prompts/`, these files provide instructions for AI agents (like GitHub Copilot) to automate report generation:

| Prompt File | Output File(s) | Description |
|-------------|----------------|-------------|
| **refresh-data.prompt.md** | Various | Triggers a full documentation refresh cycle using `fetch-cisco-docs.py` |
| **process-server-firmware-adapter-matrix.prompt.md** | `ucs-firmware-reports/server-adapter-driver-matrix-raw.md` | Generates Python script (`extract_server_data.py`) to create UCS Server Hardware Compatibility Matrix from JSON files (v4) |
| **validate-server-firmware-adapter-matrix.prompt.md** | `validation_report.md`<br>`validation_report.txt` | Creates Python validation script (`validate_firmware_data.py`) to compare JSON data against Markdown reports and identify discrepancies (v5) |
| **report-infra-server-models.prompt.md** | `ucs-firmware-reports/report-recommended-firmware.md` | Generates firmware recommendation report showing recommended versions for Infrastructure and Server models with compatibility matrices |
| **report-crossfirmware43.prompt.md** | `ucs-firmware-reports/report-ucs-crossfirmware-4.3.md` | Generates comprehensive cross-version firmware support report (v2) for UCS Manager 4.3, including infrastructure/server compatibility matrices, upgrade paths, and best practices |
| **push-all.prompt.md** | N/A | Executes `git push all` to push changes to all configured git remotes |

---

## Report Files

Located in `ucs-firmware-reports/`:

| Report File | Generated By | Description |
|-------------|--------------|-------------|
| **server-adapter-driver-matrix-raw.md** | `extract_server_data.py`<br>(via `process-server-firmware-adapter-matrix.prompt.md`) | Raw compatibility matrix showing blade models, CPU versions, ESXi versions, VIC adapters with firmware, and driver versions. Source data for other reports. |
| **report-recommended-firmware.md** | AI agent via<br>`report-infra-server-models.prompt.md` | Consolidated firmware recommendations for UCS Infrastructure and Servers. Lists recommended versions: 6.0(1b) (Latest), 4.3(6c) (Recommended Stable), 4.2(3o) (Long-term Stable) with compatibility matrices. |
| **report-ucs-crossfirmware-4.3.md** | AI agent via<br>`report-crossfirmware43.prompt.md` | Comprehensive cross-version firmware support report for UCS Manager 4.3. Includes infrastructure bundles, server bundles, fabric interconnect compatibility, IOM support, upgrade paths, and best practices. |

---

## Directories

| Directory | Description |
|-----------|-------------|
| **ucs-docs/** | Converted Markdown documentation files generated by `fetch-cisco-docs.py` |
| **ucs-docs-raw/** | Raw downloaded files, organised by type: `html/`, `pdf/`, `json/`, `other/` |
| **ucs-firmware-reports/** | Generated firmware compatibility and recommendation reports in Markdown format |
| **recommended-firmware/** | Scripts and data for fetching UCS recommended firmware release pages |
| **mcp/** | MCP server exposing `ucs-docs/` content as a tool for AI agents |
| **archive/** | Legacy scripts and data (extract_server_data.py, validate_firmware_data.py, jsondata/, etc.) |
| **wip/** | Work-in-progress files |
| **.github/prompts/** | AI agent prompt instruction files for automated report generation |

---

## Workflow

### Fetch and Convert All Documentation
```bash
source .venv/bin/activate
python3 fetch-cisco-docs.py
```
This will:
1. Read all URLs from `urls.md`
2. For each URL, determine type (cisco.com HTML, intersight.com, JSON, PDF)
3. Download raw files to the appropriate `ucs-docs-raw/` subdirectory
4. Convert to Markdown in `ucs-docs/`
5. Skip files already fetched within the last 24 hours (use `-f` to force)

### Force Re-download Everything
```bash
python3 fetch-cisco-docs.py --force
```

### Generate Specific Reports
Use AI agents (GitHub Copilot) with the prompt files:
1. Open the desired prompt file from `.github/prompts/`
2. Execute the prompt instructions with the AI agent
3. Generated reports appear in `ucs-firmware-reports/`

---

## Data Sources

All data is sourced from official Cisco documentation:
- Cisco UCS Manager configuration guides, release notes, and datasheets (cisco.com)
- Cisco Intersight SaaS and Appliance help documentation (intersight.com/help → CDN)
- Cisco UCS Hardware Compatibility List (HCL) dynamic query endpoints
- Cisco UCS Equivalency Matrix and Upgrade/Downgrade Matrix JSON files

---

## Version Information

- **fetch-cisco-docs.py**: v10
- **archive/extract_server_data.py**: v4
- **archive/validate_firmware_data.py**: v5
- **report-crossfirmware43.prompt.md**: v2
- **Last Updated**: March 4, 2026


