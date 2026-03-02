Found 14 JSON files to validate

============================================================================================
UCS FIRMWARE DATA VALIDATION
============================================================================================
Parsing markdown file: ucs-firmware-reports/server-adapter-driver-matrix-raw.md
  Found 595 entries in markdown
Parsing JSON file: jsondata/ucsm-b200m4-v3-esxi-67u3.json
  Found 12 relevant entries in JSON
Parsing JSON file: jsondata/ucsm-b200m4-v3-esxi-7u3.json
  Found 22 relevant entries in JSON
Parsing JSON file: jsondata/ucsm-b200m4-v4-esxi-67u3.json
  Found 12 relevant entries in JSON
Parsing JSON file: jsondata/ucsm-b200m4-v4-esxi-7u3.json
  Found 22 relevant entries in JSON
Parsing JSON file: jsondata/ucsm-b200m5-v1-esxi-67u3.json
  Found 12 relevant entries in JSON
Parsing JSON file: jsondata/ucsm-b200m5-v1-esxi-7u3.json
  Found 82 relevant entries in JSON
Parsing JSON file: jsondata/ucsm-b200m5-v1-esxi-8u3.json
  Found 68 relevant entries in JSON
Parsing JSON file: jsondata/ucsm-b200m5-v2-esxi-67u3.json
  Found 12 relevant entries in JSON
Parsing JSON file: jsondata/ucsm-b200m5-v2-esxi-7u3.json
  Found 82 relevant entries in JSON
Parsing JSON file: jsondata/ucsm-b200m5-v2-esxi-8u3.json
  Found 68 relevant entries in JSON
Parsing JSON file: jsondata/ucsm-b200m6-v1-esxi-7u3.json
  Found 72 relevant entries in JSON
Parsing JSON file: jsondata/ucsm-b200m6-v1-esxi-8u3.json
  Found 63 relevant entries in JSON
Parsing JSON file: jsondata/ucsm-b480m5-v1-esxi-7u3.json
  Found 82 relevant entries in JSON
Parsing JSON file: jsondata/ucsm-b480m5-v1-esxi-8u3.json
  Found 68 relevant entries in JSON

Comparing data...

============================================================================================
VALIDATION REPORT
============================================================================================

Found 15 discrepancies:


────────────────────────────────────────────────────────────────────────────────────────────
DRIVER VERSION MISMATCHES (15 items)
────────────────────────────────────────────────────────────────────────────────────────────

Blade: B480 M5 V1 | CPU: V1 | ESXi: ESXi 8.0 U3
  Adapter: VIC 1380 (FW: 4.6(5))
  Driver: nfnic
    Markdown: 5.0.0.46-1OEM.803.0.0.24022510
    JSON:     5.0.0.48-1OEM.803.0.0.24022510

Blade: B200 M5 V1 | CPU: V1 | ESXi: ESXi 8.0 U3
  Adapter: VIC 1440 (FW: 5.3(5))
  Driver: nfnic
    Markdown: 5.0.0.46-1OEM.803.0.0.24022510
    JSON:     5.0.0.48-1OEM.803.0.0.24022510

Blade: B200 M5 V2 | CPU: V2 | ESXi: ESXi 8.0 U3
  Adapter: VIC 1340 (FW: 4.6(5))
  Driver: nfnic
    Markdown: 5.0.0.46-1OEM.803.0.0.24022510
    JSON:     5.0.0.48-1OEM.803.0.0.24022510

Blade: B200 M5 V2 | CPU: V2 | ESXi: ESXi 8.0 U3
  Adapter: VIC 1480 (FW: 5.3(5))
  Driver: nfnic
    Markdown: 5.0.0.46-1OEM.803.0.0.24022510
    JSON:     5.0.0.48-1OEM.803.0.0.24022510

Blade: B200 M5 V1 | CPU: V1 | ESXi: ESXi 8.0 U3
  Adapter: VIC 1340 (FW: 4.6(5))
  Driver: nfnic
    Markdown: 5.0.0.46-1OEM.803.0.0.24022510
    JSON:     5.0.0.48-1OEM.803.0.0.24022510

Blade: B200 M6 V1 | CPU: V1 | ESXi: ESXi 8.0 U3
  Adapter: VIC 1440 (FW: 5.3(5))
  Driver: nfnic
    Markdown: 5.0.0.46-1OEM.803.0.0.24022510
    JSON:     5.0.0.48-1OEM.803.0.0.24022510

Blade: B200 M6 V1 | CPU: V1 | ESXi: ESXi 8.0 U3
  Adapter: VIC 1480 (FW: 5.3(5))
  Driver: nfnic
    Markdown: 5.0.0.46-1OEM.803.0.0.24022510
    JSON:     5.0.0.48-1OEM.803.0.0.24022510

Blade: B480 M5 V1 | CPU: V1 | ESXi: ESXi 8.0 U3
  Adapter: VIC 1340 (FW: 4.6(5))
  Driver: nfnic
    Markdown: 5.0.0.46-1OEM.803.0.0.24022510
    JSON:     5.0.0.48-1OEM.803.0.0.24022510

Blade: B480 M5 V1 | CPU: V1 | ESXi: ESXi 8.0 U3
  Adapter: VIC 1440 (FW: 5.3(5))
  Driver: nfnic
    Markdown: 5.0.0.46-1OEM.803.0.0.24022510
    JSON:     5.0.0.48-1OEM.803.0.0.24022510

Blade: B200 M6 V1 | CPU: V1 | ESXi: ESXi 8.0 U3
  Adapter: VIC 15411 (FW: 5.3(5))
  Driver: nfnic
    Markdown: 5.0.0.46-1OEM.803.0.0.24022510
    JSON:     5.0.0.48-1OEM.803.0.0.24022510

Blade: B200 M5 V2 | CPU: V2 | ESXi: ESXi 8.0 U3
  Adapter: VIC 1380 (FW: 4.6(5))
  Driver: nfnic
    Markdown: 5.0.0.46-1OEM.803.0.0.24022510
    JSON:     5.0.0.48-1OEM.803.0.0.24022510

Blade: B200 M5 V1 | CPU: V1 | ESXi: ESXi 8.0 U3
  Adapter: VIC 1480 (FW: 5.3(5))
  Driver: nfnic
    Markdown: 5.0.0.46-1OEM.803.0.0.24022510
    JSON:     5.0.0.48-1OEM.803.0.0.24022510

Blade: B480 M5 V1 | CPU: V1 | ESXi: ESXi 8.0 U3
  Adapter: VIC 1480 (FW: 5.3(5))
  Driver: nfnic
    Markdown: 5.0.0.46-1OEM.803.0.0.24022510
    JSON:     5.0.0.48-1OEM.803.0.0.24022510

Blade: B200 M5 V2 | CPU: V2 | ESXi: ESXi 8.0 U3
  Adapter: VIC 1440 (FW: 5.3(5))
  Driver: nfnic
    Markdown: 5.0.0.46-1OEM.803.0.0.24022510
    JSON:     5.0.0.48-1OEM.803.0.0.24022510

Blade: B200 M5 V1 | CPU: V1 | ESXi: ESXi 8.0 U3
  Adapter: VIC 1380 (FW: 4.6(5))
  Driver: nfnic
    Markdown: 5.0.0.46-1OEM.803.0.0.24022510
    JSON:     5.0.0.48-1OEM.803.0.0.24022510

============================================================================================
SUMMARY: 15 total discrepancies
  - Missing in JSON: 0
  - Missing in Markdown: 0
  - Version Mismatches: 15
============================================================================================
