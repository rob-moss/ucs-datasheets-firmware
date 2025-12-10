---
agent: agent
name: validate-server-firmware-adapter-matrix-v5
description: Validate UCS firmware data between JSON files and markdown report to identify discrepancies in blade server configurations, adapter models, ESXi versions, and driver versions.
---

# Validate UCS Server Firmware Adapter Matrix

## Version


## Objective
Create a validation script that compares UCS firmware data between JSON files and the markdown report to identify discrepancies in blade server configurations, adapter models, ESXi versions, and driver versions.

## Requirements

### Input Files
1. **Markdown Report**: `ucs-firmware-reports/server-adapter-driver-matrix-raw.md`
   - Contains the compatibility matrix in table format
   - Columns: Blade Model + CPU Version | Server Firmware | ESXi Version | Adapter Model + Firmware | Driver + Version

2. **JSON Files** to validate (configurable):
   - `jsondata/ucsm-*.json`
    - Each file corresponds to a specific blade model, CPU version, and ESXi version
    - Contains adapter and driver version information
    - Example filenames:
      - `ucsm-b200m4-v3-esxi-67u3.json`
      - `ucsm-b200m5-v1-esxi-8u3.json`
      - `ucsm-b200m6-v1-esxi-8u3.json`
      - `ucsm-b480m5-v1-esxi-8u3.json`
    - Exclude files: `UCS-Equivalency-Matrix.json`, `ucsmupgradematrix.json`, `ucsmcrossver.json`
    - JSON files contain an array of version objects with adapter and driver details



### Validation Goals
1. **Identify Entries in Markdown but NOT in JSON**
   - Blade/Adapter/ESXi/Driver combinations present in the markdown report but missing from the JSON files.
2. **Identify Entries in JSON but NOT in Markdown**
   - Blade/Adapter/ESXi/Driver combinations present in the JSON files but missing from the markdown report.
3. **Identify Driver Version Mismatches**
   - Same Blade/Adapter/ESXi combination exists in both markdown and JSON but with different driver versions.
3. **UCS Server firmware versions to consider**: Only versions 4.2(2) and above.

### Data Extraction
Extract from the `HardwareTypes.Adapters.CNA` array:

1. **Adapter Model Numbers**:
   - Extract VIC model numbers from full names
   - Example: "Cisco UCSB-MLOM-40G-04: Cisco UCS 1440 Virtual Interface Card" → "VIC 1440"
   - Example: "Cisco UCSB-ML-V5Q10G: UCS 15411 Virtual Interface Card" → "VIC 15411"
   - Exclude Port Expander adapters

2. **Adapter Model + Firmware**:
   - The markdown report combines adapter model and firmware version in one column (e.g., "VIC 1440 - 5.2(2)") in the column named "Adapter Model + Firmware".
   - The JSON files provide these as separate fields.
   - The script should parse and compare these correctly in the same format.



### Data to Compare
- **UCS Blade Server Type**: B200 M4, B200 M5, B200 M6, B480 M5
- **UCS Blade Firmware Version**: e.g., 4.2(2), 4.3(1), 4.4(1), 5.0(1), 5.1(1), 5.2(2), 5.3(2)
- **CPU Version**: V1, V2, V3, V4
- **ESXi Version**: 6.7 U3, 7.0 U3, 8.0 U3
- **Adapter Model**: VIC 1240, VIC 1280, VIC 1340, VIC 1380, VIC 1440, VIC 1480, VIC 15411 and more
- **Adapter Firmware Version**: e.g., 4.4(1), 4.5(2), 5.2(3)
- **Driver Types**: nenic, nfnic, nenic-ens
- **Driver Types**: Ignore all nfnic drivers that contain the suffix "(nvme)"
- **Driver Types**: Keep all other nfnic drivers
- **Driver Versions**: e.g., 1.0.42.0-1OEM.670.0.0.8169922, 2.0.17.0-1OEM.800.1.0.20613240



### JSON Structure
JSON files are arrays of version objects. Each object contains:
```json
[
  {
    "Version": "4.2(2)",
    "HardwareTypes": {
      "Adapters": {
        "CNA": [
          {
            "Model": "Cisco UCSB-MLOM-40G-03: Cisco UCS 1340 Virtual Interface Card",
            "FirmwareVersion": "4.5(2)",
            "DriverVersion": "1.0.42.0-1OEM.670.0.0.8169922 nenic"
          }
        ]
      }
    }
  }
]
```

## Validation Logic

### 1. Parse Markdown Report
- Extract table rows (lines starting with `|`)
- Parse columns: blade model, server firmware, ESXi version, adapter info, drivers
- Handle multiple drivers per row (separated by `<br>`)
- Extract VIC model numbers (e.g., "VIC 1340")
- Parse driver type and version from each driver entry

### 2. Parse JSON Files
- Handle array of version objects
- Extract blade/CPU info from filename: `ucsm-<blade>-<cpu>-esxi-<version>.json`
  - Example: `ucsm-b200m5-v1-esxi-8u3.json` → B200 M5 V1, ESXi 8.0 U3
- Navigate to `HardwareTypes.Adapters.CNA`
- Extract VIC model from adapter Model field
- Parse driver version string: `"<version> <type>"` → extract version and type

### 3. Compare and Report Discrepancies

Generate three types of reports:

#### A. Missing in JSON
Entries that exist in markdown but not found in JSON files.

**Format:**
Create a matrix  in markdown format as below:

| Blade Model + CPU Version | Server Firmware | ESXi Version | Adapter Model + Firmware | Driver + Version |
| ------------ | ------------ | ------------ | ------------ | ------------ |  ------------ |
| B200 M5 V1 | 4.2(2) | ESXi 7.0 U3 | VIC 1440 - 5.2(2) | nenic-ens 1.0.6.0-1OEM.700.1.0.15843807 |


#### B. Missing in Markdown
Entries that exist in JSON but not found in markdown report.

**Format:**
Create a matrix  in markdown format as below:

| Blade Model + CPU Version | Server Firmware | ESXi Version | Adapter Model + Firmware | Driver + Version |
| ------------ | ------------ | ------------ | ------------ | ------------ |  ------------ |
| B200 M5 V1 | 4.2(2) | ESXi 7.0 U3 | VIC 1440 - 5.2(2) | nenic-ens 1.0.6.0-1OEM.700.1.0.15843807 |


#### C. Version Mismatches
Same blade/adapter/ESXi combo exists in both but with different driver versions.

**Format:**
```
Blade: B200 M5 V1 | CPU: V1 | ESXi: ESXi 8.0 U3
  Adapter: VIC 1440 (FW: 5.3(2))
  Driver: nenic
    Markdown: 2.0.17.0-1OEM.800.1.0.20613240
    JSON:     2.0.11.0-1OEM.800.1.0.20143090
```

## Output Requirements

### Console Output
```
============================================================================================
UCS FIRMWARE DATA VALIDATION
============================================================================================

Parsing markdown file: ucs-firmware-reports/server-adapter-driver-matrix-raw.md
  Found 454 entries in markdown
Parsing JSON file: jsondata/ucsm-b200m4-v3-esxi-67u3.json
  Found 72 relevant entries in JSON
...

Comparing data...

============================================================================================
VALIDATION REPORT
============================================================================================

Found 736 discrepancies:

────────────────────────────────────────────────────────────────────────────────────────
ENTRIES IN MARKDOWN BUT NOT IN JSON (454 items)
────────────────────────────────────────────────────────────────────────────────────────
[Detailed entries listed here]

────────────────────────────────────────────────────────────────────────────────────────
ENTRIES IN JSON BUT NOT IN MARKDOWN (282 items)
────────────────────────────────────────────────────────────────────────────────────────
[Detailed entries listed here]

────────────────────────────────────────────────────────────────────────────────────────
DRIVER VERSION MISMATCHES (0 items)
────────────────────────────────────────────────────────────────────────────────────────
[Detailed entries listed here]

============================================================================================
SUMMARY: 736 total discrepancies
  - Missing in JSON: 454
  - Missing in Markdown: 282
  - Version Mismatches: 0
============================================================================================
```

## Implementation Guidelines

### Script Structure
1. **FirmwareValidator Class**
   - `parse_markdown()` - Parse markdown table
   - `parse_json_files()` - Parse JSON array structures
   - `compare_data()` - Find discrepancies
   - `generate_report()` - Output formatted report

2. **Key Functions**
   - Extract CPU version from blade model string
   - Extract VIC model from full adapter name
   - Parse ESXi version from filename
   - Group entries by comparison key (blade + ESXi + adapter + firmware + driver type)

3. **Data Structures**
   - Use dictionaries with composite keys for efficient comparison
   - Group markdown and JSON data separately by key
   - Use sets for finding differences

### Filename Parsing
Convert filename to structured data:
- `ucsm-b200m4-v3-esxi-67u3.json` → B200 M4 V3, ESXi 6.7 U3
- `ucsm-b200m5-v1-esxi-8u3.json` → B200 M5 V1, ESXi 8.0 U3
- `ucsm-b480m5-v1-esxi-7u3.json` → B480 M5 V1, ESXi 7.0 U3

### ESXi Version Mapping
- `67u3` → "ESXi 6.7 U3"
- `7u3` → "ESXi 7.0 U3"
- `8u3` → "ESXi 8.0 U3"

## Success Criteria

1. ✅ Script successfully parses markdown table format
2. ✅ Script correctly handles JSON array of version objects
3. ✅ Script extracts blade/CPU/ESXi info from filenames
4. ✅ Script identifies all three types of discrepancies
5. ✅ Output is clearly formatted and easy to read
6. ✅ Report includes summary statistics
7. ✅ Script can be easily configured for different JSON files

## Usage

```bash
# Run validation
python3 validate_firmware_data.py

# Save output to file
python3 validate_firmware_data.py > validation_report.txt
```

## Deliverables

1. **validate_firmware_data.py** - Main validation script
2. **VALIDATION_README.md** - Documentation on usage and customization
3. **validation_report.txt** - Sample output showing discovered discrepancies

## Constraints

- Use Python 3.6+ standard library only (no external dependencies)
- Handle malformed data gracefully
- Support both full adapter names and short VIC model numbers
- Case-insensitive matching where appropriate
- Handle multiple driver versions per adapter