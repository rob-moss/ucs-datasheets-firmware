# UCS Firmware Data Validation Script

## Overview

`validate_firmware_data.py` is a Python script that compares UCS firmware data between JSON files and the markdown report to identify discrepancies in:

- UCS Blade server types (B200 M4, B200 M5, B200 M6, B480 M5)
- CPU versions (V1, V2, V3, V4)
- ESXi versions (6.7 U3, 7.0 U3, 8.0 U3)
- Adapter models (VIC 1240, VIC 1280, VIC 1340, VIC 1380, VIC 1440, VIC 1480, VIC 15411, and more)
- Driver versions for: `nenic`, `nfnic`, `nenic-ens`

**Important Filters**:
- The script only processes entries with UCS Server firmware version **4.2(2) and above**. Earlier firmware versions are automatically filtered out.
- **nfnic (nvme) entries are excluded** from validation - only Ethernet nfnic drivers are included.
- **Port Expander adapters are excluded** (e.g., Cisco UCSB-MLOM-PT-01) - only VIC adapters are validated.

## Usage

### Basic Usage

```bash
python3 validate_firmware_data.py
```

### Save Output to File

```bash
python3 validate_firmware_data.py > validation_report.txt
```

## Files Validated

The script automatically discovers and validates all relevant JSON files:

- **Markdown Report**: `ucs-firmware-reports/server-adapter-driver-matrix-raw.md`
- **JSON Files**: All files matching `jsondata/ucsm-*.json` (14 files total)
  - Excludes: `UCS-Equivalency-Matrix.json`, `ucsmupgradematrix.json`, `ucsmcrossver.json`
  - Automatically processes all blade server configurations with their ESXi versions

## Output

The script generates a detailed report with three types of discrepancies:

### 1. Entries in Markdown but NOT in JSON
These are combinations of blade/adapter/ESXi/driver that appear in the markdown report but are missing from the JSON files.

**Output Format**: Markdown table with columns:
- Blade Model + CPU Version
- Server Firmware
- ESXi Version
- Adapter Model + Firmware
- Driver + Version

**Example**:
```
| B200 M5 V1 | 4.2(2) | ESXi 7.0 U3 | VIC 1440 - 5.2(2) | nenic 1.0.45.0-1OEM |
```

### 2. Entries in JSON but NOT in Markdown
These are combinations present in the JSON files but missing from the markdown report.

**Output Format**: Markdown table with columns showing full adapter names from JSON files.

**Example**:
```
| B200 M5 V1 | 4.2(2) | ESXi 8.0 U3 | Cisco UCSB-MLOM-40G-04: Cisco UCS 1440 Virtual Interface Card - 5.3(2) | nenic 2.0.17.0-1OEM.800.1.0.20613240 |
```

### 3. Driver Version Mismatches
When the same blade/adapter/ESXi combination exists in both sources but with different driver versions.

## Report Summary

At the end of the report, a summary shows:
- Total number of discrepancies
- Count of entries missing in JSON
- Count of entries missing in markdown
- Count of version mismatches

## Customization

The script automatically discovers JSON files matching the pattern `jsondata/ucsm-*.json`. 

To modify the behavior, edit the `main()` function:

```python
def main():
    markdown_file = "ucs-firmware-reports/server-adapter-driver-matrix-raw.md"
    
    # Customize the exclusion list if needed
    exclude_files = {
        "UCS-Equivalency-Matrix.json",
        "ucsmupgradematrix.json",
        "ucsmcrossver.json"
    }
    
    # Files are auto-discovered from jsondata/ucsm-*.json
    # To manually specify files instead, replace the auto-discovery logic
```

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## Example Output

```
============================================================================================
UCS FIRMWARE DATA VALIDATION
============================================================================================

Parsing markdown file: ucs-firmware-reports/server-adapter-driver-matrix-raw.md
  Found 454 entries in markdown
Parsing JSON file: jsondata/ucsm-b200m4-v3-esxi-67u3.json
  Found 72 relevant entries in JSON
...

============================================================================================
VALIDATION REPORT
============================================================================================

Found 736 total discrepancies

────────────────────────────────────────────────────────────────────────────────────────
ENTRIES IN MARKDOWN BUT NOT IN JSON (454 items)
────────────────────────────────────────────────────────────────────────────────────────
...

============================================================================================
SUMMARY: 736 total discrepancies
  - Missing in JSON: 454
  - Missing in Markdown: 282
  - Version Mismatches: 0
============================================================================================
```

## Troubleshooting

### No entries found in JSON
If the script reports 0 entries found in JSON files, ensure:
1. The JSON files exist and are readable
2. The JSON structure matches the expected format (array of version objects)
3. The files contain CNA adapter entries under `HardwareTypes > Adapters > CNA`

### Incorrect blade model matching
The script extracts blade model information from filenames using the pattern:
`ucsm-<blade>-<cpu>-esxi-<version>.json`

Example: `ucsm-b200m5-v1-esxi-8u3.json`
- Blade: B200 M5
- CPU: V1
- ESXi: 8.0 U3

Ensure your filenames follow this convention.
