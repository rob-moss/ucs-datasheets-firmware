---
agent: agent
name: process-server-firmware-adapter-matrix-v4
description: Generate a UCS Server Hardware Compatibility Matrix in markdown format by extracting data from JSON files.
---

# Generate UCS Server Hardware Compatibility Matrix

Create a Python script that extracts UCS blade server hardware compatibility data from JSON files and generates a comprehensive markdown report.

The version of this prompt v4. The Python Script should also include this version information in a comment at the top, and the output markdown should also include the version information.



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

Extract from the JSON structure:
1. **Server Firmware**: From `Version` field in JSON
  - Example: 4.2(2)
  - Only include versions 4.2(2) and above ie beginning with 4.2(2) and later


Extract from the `HardwareTypes.Adapters.CNA` array:

1. **Adapter Model Numbers**:
   - Extract VIC model numbers from full names
   - Example: "Cisco UCSB-MLOM-40G-04: Cisco UCS 1440 Virtual Interface Card" → "VIC 1440"
   - Example: "Cisco UCSB-ML-V5Q10G: UCS 15411 Virtual Interface Card" → "VIC 15411"
   - Exclude Port Expander adapters

2. **Firmware Versions**:
   - Extract from `FirmwareVersion` field
   - Associate with each adapter model

3. **Driver Names**:
   - Extract from `DriverVersion` field (typically the last word in the string)
   - Filter for: `nenic`, `nfnic`, `nenic-ens`, `nfnic-ens`
   - Example: "2.0.11.0-1OEM.800.1.0.20143090 nenic" → "nenic" and "2.0.11.0-1OEM.800.1.0.20143090" is the version
   - Do not use braces () around the version


## Output Format
Between UCS Blade verisons, separate each model server with an empty row.

The Headings for the markdown file should include the version of this prompt used to generate it, e.g., "Generated with process-server-firmware-adapter-matrix-v4".


Create a markdown matrix with the following fields:
- Blade Model + CPU Version
- Server Firmware
- ESXi Version
- Adapter Model and Firmware
- Driver Names and Versions

An example is below:
| Blade Model + CPU Version | Server Firmware | ESXi Version | Adapter Model + Firmware | Driver + Version |
| ------------ | ------------ | ------------ | ------------ | ------------ |  ------------ | 
| B200 M4 V3 | 4.2(2) | ESXi 6.7 U3 | VIC 1280 - 4.4(1) | nenic-ens 1.0.2.0-1OEM.670.0.0.8169922 |














## Requirements

1. **Group by Blade Model**: Organize sections by server model (B200 M4, B200 M5, B200 M6, B480 M5)

2. **Sort Configurations**: Within each model, sort by:
   - Server firmware version (ascending, oldest first)
   - CPU version (V1, V2, V3, V4)
   - ESXi version (ascending, oldest first)

3. **List All Adapters**: Include all unique adapter/firmware combinations found in the JSON data

4. **Deduplicate Drivers**: Show unique driver types only (nenic, nfnic, nenic-ens, nfnic-ens)

5. **Clean Formatting**: 
   - Use proper markdown headings (##, ###)
   - Use horizontal rules (---) between sections
   - Use bullet points for lists

6. **Group Adapter and Driver Versions**: 
   - For each driver type (nenic, nfnic, nenic-ens, nfnic-ens), list all unique full version strings associated with that driver type under the respective configuration.

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
ucs-firmware-reports/server-adapter-driver-matrix-raw.md
```

## Execution

After creating the script:
1. Save it as `extract_server_data.py`
2. Run it with: `python3 extract_server_data.py`
3. Verify the output file `server-adapter-driver-matrix.md` is created successfully
4. Review the markdown report for accuracy and completeness
5. Commit the script and output file to the repository with the commit message "Updated server firmware adapter matrix version x"
6. Run the prompt `push-all` to push changes to GitHub
