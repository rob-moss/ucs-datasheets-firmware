---
agent: agent
version: 1.0
description: Process all JSON files in jsondata/ and create a single conscice Markdown file with all of the processed data
---

# Generate UCS Server Hardware Compatibility Matrix

Create a Python script that extracts UCS blade server hardware compatibility data from JSON files and generates a comprehensive markdown report.

## Data Source

Parse all JSON files in the `jsondata/` directory, excluding:
- UCS-Equivalency-Matrix.json
- ucsmupgradematrix.json
- ucsmcrossver.json

## Extract the Following Information

### From Filename Pattern
Parse filenames like `b200m5-v2-esxi-8u3.json` or `ucsm-b200m6-v1-esxi-7u3.json` to extract:

1. **Blade Model**: B200 M4, B200 M5, B200 M6, B480 M5, C220 M5, C240 M5, etc.
   - Format: Convert `b200m5` to `B200 M5`
   - Handle both blade (B-series) and rack (C-series) servers

2. **CPU Version/Generation**: V1, V2, V3, V4
   - Extract from pattern `-v1-`, `-v2-`, `-v3-`, `-v4-`

3. **ESXi Version**: 
   - Convert `67u3` to `ESXi 6.7 U3`
   - Convert `7u3` to `ESXi 7.0 U3`
   - Convert `8u3` to `ESXi 8.0 U3`

### From JSON Content

Extract from the `HardwareTypes.Adapters.CNA` array:

1. **Adapter Model Numbers**:
   - Extract VIC model numbers from full names
   - Example: "Cisco UCSB-MLOM-40G-04: Cisco UCS 1440 Virtual Interface Card" → "VIC 1440"
   - Example: "Cisco UCSB-ML-V5Q10G: UCS 15411 Virtual Interface Card" → "VIC 15411"
   - Do not include Port Expander adapters

2. **Firmware Versions**:
   - Extract from `FirmwareVersion` field
   - Associate with each adapter model

3. **Driver Names**:
   - Extract from `DriverVersion` field (typically the last word in the string)
   - Filter for: `nenic`, `nfnic`, `nenic-ens`, `nfnic-ens`
   - Example: "2.0.11.0-1OEM.800.1.0.20143090 nenic" → "nenic"



## Output Format

Generate a markdown file named `ucs-firmware-docs/server-adapter-driver-matrix.md` with the following structure:


```markdown
# UCS Server Hardware Compatibility Matrix

**Generated:** [Current Date]

This matrix shows UCS blade server models with their supported adapters, ESXi versions, and drivers.

---

## [Blade Model]

### [Blade Model] - [CPU Version] - [ESXi Version]

**Adapters:**
- [Adapter Model] (FW: [Firmware Version])
- [Adapter Model] (FW: [Firmware Version])
...

**Drivers:**
- [driver1], [driver2], [driver3]

---
```

## Requirements

1. **Group by Blade Model**: Organize sections by server model (B200 M4, B200 M5, B200 M6, B480 M5)

2. **Sort Configurations**: Within each model, sort by:
   - CPU version (V1, V2, V3, V4)
   - ESXi version (ascending)

3. **List All Adapters**: Include all unique adapter/firmware combinations found in the JSON data

4. **Deduplicate Drivers**: Show unique driver types only (nenic, nfnic, nenic-ens, nfnic-ens)

5. **Clean Formatting**: 
   - Use proper markdown headings (##, ###)
   - Use horizontal rules (---) between sections
   - Use bullet points for lists

## Script Requirements

- Use Python 3
- Parse JSON files with the `json` module
- Use regex for filename and model name parsing
- Handle errors gracefully (print errors but continue processing)
- Print progress messages showing which files are being processed
- Report final statistics (number of configurations processed)

## Output Location

Save the generated markdown file as:
```
server-adapter-driver-matrix.md
```

## Example Output Section

```markdown
## B200 M6

### B200 M6 - V1 - ESXi 8.0 U3

**Adapters:**
- VIC 1440 (FW: 5.2(3))
- VIC 1440 (FW: 5.3(2))
- VIC 1480 (FW: 5.2(3))
- VIC 1480 (FW: 5.3(2))
- VIC 15411 (FW: 5.2(3))
- VIC 15411 (FW: 5.3(2))

**Drivers:**
- nenic, nenic-ens, nfnic

---
```

## Execution

After creating the script:
1. Save it as `extract_server_data.py`
2. Run it with: `python3 extract_server_data.py`
3. Verify the output file `server-adapter-driver-matrix.md` is created successfully
