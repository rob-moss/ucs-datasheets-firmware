# Cisco IMM Infrastructure and Server Firmware Matrix

| | |
|---|---|
| **Source** | Cisco IMM Infrastructure Firmware Release Notes 4.3 and 6.0 / Server Firmware Release Notes 4.3–5.4 and 6.0 |
| **Generated** | 2026-06-22 |
| **Last Updated** | May 4, 2026 |
| **Document Version** | 1.0 |

---

## Overview

### IMM Firmware Architecture

In Intersight Managed Mode (IMM), firmware upgrades are split into two independent tracks:

- **Infrastructure firmware** — runs on Cisco UCS Fabric Interconnects (FI 6400 Series: FI-6454, FI-64108; FI 6500 Series: FI-6536; FI 6600 Series: FI-6652, FI-6664; and the X-Series Direct FI: UCSX-S9108-100G). Infrastructure firmware controls fabric connectivity, chassis management, and I/O module behavior.
- **Server firmware** — runs on B-Series blade servers, C-Series rack servers, and X-Series compute nodes. Server firmware controls BIOS, CIMC, VIC adapters, and storage controllers.

> **Important**: Infrastructure and server firmware can be upgraded **independently**. You do **not** need to upgrade infrastructure firmware to use the latest server firmware, and vice versa. Both tracks are managed through Intersight firmware policies (requires Cisco Intersight Essentials or Advanced license tier).

### Recommended Firmware Versions

The following recommended firmware versions are sourced from `ucs-docs/recommended-firmware-imm.md` (fetched from software.cisco.com 2026-06-11).

#### Infrastructure (Fabric Interconnects)

| Platform | Recommended Version | Notes |
|----------|---------------------|-------|
| UCS-FI-6454, UCS-FI-64108 (6400 Series) | **6.0(2.260045)** | Latest Recommended |
| UCS-FI-6536 (6500 Series) | **6.0(2.260045)** | Latest Recommended |
| UCS-FI-6652, UCS-FI-6664 (6600 Series) | **6.0(2.260045)** | Latest Recommended |
| UCSX-S9108-100G (X-Series Direct) | **6.0(2.260045)** | Latest Recommended |

#### Server Firmware

| Platform | Recommended Version | Status |
|----------|---------------------|--------|
| UCSX-210C-M6, M7, M8 | **6.0(2.260040)** | Latest Recommended |
| UCSX-215C-M8 | **6.0(2.260040)** | Latest Recommended |
| UCSX-410C-M7, M8 | **6.0(2.260040)** | Latest Recommended |
| UCSX-9508 Chassis | **6.0(2.260042)** | Latest Recommended |
| UCSXE-130C-M8 (Edge) | **6.0(2.260042)** | Latest Recommended |
| UCSB-B200-M5, B480-M5 | **6.0(1.260012)** | Latest Recommended (EOL server) |
| UCSB-B200-M6 | **6.0(2.260040)** | Latest Recommended (EOL server) |
| UCSC-C220-M5, C240-M5, C480-M5 | **4.3(2.250045)** | Latest Recommended (EOL server) |
| UCSC-C125 | **4.3(2.250016)** | Latest Recommended |
| UCSC-C220-M6, C240-M6, C225-M6, C245-M6 | **6.0(2.260044)** | Latest Recommended (EOL server) |
| UCSC-C220-M7, C240-M7 | **6.0(2.260044)** | Latest Recommended |
| UCSC-C220-M8, C240-M8, C225-M8, C245-M8 | **6.0(2.260044)** | Latest Recommended |

### Scope

This report covers:
- **Infrastructure Firmware**: IMM Infrastructure releases 4.3.x and 6.0.x (for FI 6400, 6500, 6600 Series, and X-Series Direct)
- **Server Firmware**: IMM Server Firmware releases 4.3.x, 5.2.x, 5.3.x, 5.4.x, and 6.0.x

This report covers **Intersight Managed Mode (IMM) only** — not UCS Manager (UCSM) or Cisco IMC standalone mode.

---

## Infrastructure Firmware Cross-Version Compatibility Matrix

The following tables map **infrastructure firmware major versions** to compatible server firmware versions. These tables apply to all FI 6400/6500/6600 Series Fabric Interconnects. The X-Series Direct (9108 100G) FI was introduced in infrastructure release 4.3(4).

> **Note**: The cross-version firmware support table is identical across both the IMM Infrastructure 4.3 and 6.0 release notes. The tables were verified consistent across both sources.

### Matrix 1 — UCS 6400, 6500, and 6600 Series Fabric Interconnects

(FI-6454, FI-64108, FI-6536, FI-6652, FI-6664)

| Infrastructure FW | Latest Build | Compatible X-Series Server FW | Compatible B-Series Server FW | Compatible C-Series Server FW | Notes |
|-------------------|-------------|-------------------------------|-------------------------------|-------------------------------|-------|
| **6.0(2)** | **6.0(2.260045)** | 6.0(2), 6.0(1), 5.4(0), 5.3(0), 5.2(2), 5.2(1), 5.2(0), 5.1(1), 5.1(0), 5.0(4) | 6.0(2), 6.0(1), 5.4(0), 5.3(0), 5.2(2), 5.2(1), 5.2(0), 5.1(0), 4.3(3), 4.3(2), 4.2(3) | 6.0(2), 6.0(1), 4.3(6), 4.3(5), 4.3(4), 4.3(3), 4.3(2), 4.3(1), 4.2(3) | **LATEST RECOMMENDED**. Supports all current FI models including 6600 Series. |
| **6.0(1)** | 6.0(1.260006) | 6.0(2), 6.0(1), 5.4(0), 5.3(0), 5.2(2), 5.2(1), 5.2(0), 5.1(1), 5.1(0), 5.0(4) | 6.0(2), 6.0(1), 5.4(0), 5.3(0), 5.2(2), 5.2(1), 5.2(0), 5.1(0), 4.3(3), 4.3(2), 4.2(3) | 6.0(2), 6.0(1), 4.3(6), 4.3(5), 4.3(4), 4.3(3), 4.3(2), 4.3(1), 4.2(3) | Initial 6.0 GA release. |
| **4.3(6)** | 4.3(6.260026) | 6.0(2), 6.0(1), 5.4(0), 5.3(0), 5.2(2), 5.2(1), 5.2(0), 5.1(1), 5.1(0), 5.0(4) | 6.0(2), 6.0(1), 5.4(0), 5.3(0), 5.2(2), 5.2(1), 5.2(0), 5.1(0), 4.3(3), 4.3(2), 4.2(3) | 6.0(2), 6.0(1), 4.3(6), 4.3(5), 4.3(4), 4.3(3), 4.3(2), 4.3(1), 4.2(3) | Latest 4.3.x infra. Adds C220 M8 and C240 M8 support (requires build 4.3(6.250048)+). |
| **4.3(5)** | 4.3(5.250012) | 6.0(2), 6.0(1), 5.4(0), 5.3(0), 5.2(2), 5.2(1), 5.2(0), 5.1(1), 5.1(0), 5.0(4) | 6.0(2), 6.0(1), 5.4(0), 5.3(0), 5.2(2), 5.2(1), 5.2(0), 5.1(0), 4.3(3), 4.3(2), 4.2(3) | 6.0(2), 6.0(1), 4.3(6), 4.3(5), 4.3(4), 4.3(3), 4.3(2), 4.3(1), 4.2(3) | Note: 4.3(5.240040) was **deprecated** due to CSCwn43752. Use 4.3(5.250004) or later. |
| **4.3(4)** | 4.3(4.240074) | 6.0(2), 6.0(1), 5.4(0), 5.3(0), 5.2(2), 5.2(1), 5.2(0), 5.1(1), 5.1(0), 5.0(4) | 6.0(2), 6.0(1), 5.4(0), 5.3(0), 5.2(2), 5.2(1), 5.2(0), 5.1(0), 4.3(3), 4.3(2), 4.2(3) | 6.0(2), 6.0(1), 4.3(6), 4.3(5), 4.3(4), 4.3(3), 4.3(2), 4.3(1), 4.2(3) | — |
| **4.3(3)** | 4.3(3.240007) | 6.0(2), 6.0(1), 5.4(0), 5.3(0), 5.2(2), 5.2(1), 5.2(0), 5.1(1), 5.1(0), 5.0(4) | 6.0(2), 6.0(1), 5.4(0), 5.3(0), 5.2(2), 5.2(1), 5.2(0), 5.1(0), 4.3(3), 4.3(2), 4.2(3) | 6.0(2), 6.0(1), 4.3(6), 4.3(5), 4.3(4), 4.3(3), 4.3(2), 4.3(1), 4.2(3) | — |
| **4.3(2)** | 4.3(2.240002) | 6.0(2), 6.0(1), 5.4(0), 5.3(0), 5.2(2), 5.2(1), 5.2(0), 5.1(1), 5.1(0), 5.0(4) | 6.0(2), 6.0(1), 5.4(0), 5.3(0), 5.2(2), 5.2(1), 5.2(0), 5.1(0), 4.3(3), 4.3(2), 4.2(3) | 6.0(2), 6.0(1), 4.3(6), 4.3(5), 4.3(4), 4.3(3), 4.3(2), 4.3(1), 4.2(3) | First release in 4.3.x series (GA: Nov 2023). VIC 15000 Series Secure Boot adapters introduced. |
| **4.2(3)** | 4.2(3.x) | 6.0(2), 6.0(1), 5.4(0), 5.3(0), 5.2(2), 5.2(1), 5.2(0), 5.1(1), 5.1(0), 5.0(4), 5.0(2), 5.0(1) | 6.0(2), 6.0(1), 5.4(0), 5.3(0), 5.2(2), 5.2(1), 5.2(0), 5.1(0), 4.3(3), 4.3(2), 4.2(3), 4.2(2), 4.2(1), 4.1(3) | 6.0(2), 6.0(1), 4.3(6), 4.3(5), 4.3(4), 4.3(3), 4.3(2), 4.3(1), 4.2(3), 4.2(2), 4.2(1), 4.1(3) | Broadest C/B-Series backward compat. Also supports older X-Series 5.0(2), 5.0(1). |
| **4.2(2)** | 4.2(2.x) | 5.0(4), 5.0(2), 5.0(1) only | 5.4(0), 5.3(0), 5.2(2), 5.2(1), 5.2(0), 5.1(0), 4.3(3), 4.3(2), 4.2(3), 4.2(2), 4.2(1), 4.1(3) | 4.3(6), 4.3(5), 4.3(4), 4.3(3), 4.3(2), 4.3(1), 4.2(3), 4.2(2), 4.2(1), 4.1(3) | No 6.0.x server FW support. |
| **4.2(1)** | 4.2(1.x) | 5.0(4), 5.0(2), 5.0(1) only | 5.4(0), 5.3(0), 5.2(2), 5.2(1), 5.2(0), 5.1(0), 4.3(3), 4.3(2), 4.2(3), 4.2(2), 4.2(1), 4.1(3) | 4.3(6), 4.3(5), 4.3(4), 4.3(3), 4.3(2), 4.3(1), 4.2(3), 4.2(2), 4.2(1), 4.1(3) | No 6.0.x server FW support. |
| **4.1(3)** | 4.1(3.x) | Not supported (N/A) | 5.4(0), 5.3(0), 5.2(2), 5.2(1), 5.2(0), 5.1(0), 4.3(3), 4.3(2), 4.2(3), 4.2(2), 4.2(1), 4.1(3) | 4.3(6), 4.3(5), 4.3(4), 4.3(3), 4.3(2), 4.3(1), 4.2(3), 4.2(2), 4.2(1), 4.1(3) | X-Series servers not supported in 4.1.x infrastructure. |

### Matrix 2 — UCS X-Series Direct Fabric Interconnect (UCSX-S9108-100G)

The X-Series Direct FI was introduced with infrastructure release **4.3(4.240078)**. Only X-Series compute nodes are connected to the X-Series Direct FI. B-Series and C-Series servers attach through standard 6400/6500/6600 Series FIs only.

| Infrastructure FW | Latest Build | Compatible X-Series Server FW | Notes |
|-------------------|-------------|-------------------------------|-------|
| **6.0(2)** | **6.0(2.260045)** | 6.0(2), 6.0(1), 5.4(0), 5.3(0), 5.2(2), 5.2(1), 5.2(0), 5.1(1), 5.1(0), 5.0(4) | **LATEST RECOMMENDED**. Supports X210c M8 (requires build 6.0(2.260045) for X-Direct or 4.3(6.250094)+). |
| **6.0(1)** | 6.0(1.260006) | 6.0(2), 6.0(1), 5.4(0), 5.3(0), 5.2(2), 5.2(1), 5.2(0), 5.1(1), 5.1(0), 5.0(4) | Initial 6.0 release for X-Series Direct. |
| **4.3(6)** | 4.3(6.260026) | 6.0(2), 6.0(1), 5.4(0), 5.3(0), 5.2(2), 5.2(1), 5.2(0), 5.1(1), 5.1(0), 5.0(4) | X210c M8 requires 4.3(6.250094) or later for X-Direct. Latest 4.3.x for X-Direct. |
| **4.3(5)** | 4.3(5.250034) | 6.0(2), 6.0(1), 5.4(0), 5.3(0), 5.2(2), 5.2(1), 5.2(0), 5.1(1), 5.1(0), 5.0(4) | — |
| **4.3(4)** | 4.3(4.240078) | 6.0(2), 6.0(1), 5.4(0), 5.3(0), 5.2(2), 5.2(1), 5.2(0), 5.1(1), 5.1(0), 5.0(4) | **First release** supporting X-Series Direct (UCS 9108 100G). Introduced with infrastructure release 4.3(4.240078). |

> **Note**: The X-Series Direct does not connect B-Series or C-Series servers. Only X-Series compute nodes (UCSX-210C, UCSX-215C, UCSX-410C) and X-Series Edge compute nodes (UCSXE-130C-M8) apply.

---

## Server Firmware Support by Server Family

The following tables list current server model support based on the IMM Server Firmware release notes (4.3/5.2/5.3/5.4 and 6.0) and recommended versions from `ucs-docs/recommended-firmware-imm.md`.

### B-Series Blade Servers

B-Series servers attach to FI 6400, 6500, or 6600 Series Fabric Interconnects.

> **Note**: Cisco UCS B-Series M5 and M6 servers are **End-of-Life (EOL)**. The latest supported IMM firmware versions are listed below.

| Server Model | PIDs | IMM Server FW Latest (Recommended) | Min Infra FW | VIC Adapters (mLOM) | Notes |
|-------------|------|-------------------------------------|--------------|---------------------|-------|
| **UCSB-B200-M5** | UCSB-B200-M5 | **6.0(1.260012)** | 4.2(3) | VIC 1340, VIC 1440 | 5th gen blade. EOL. Max supported: 6.0(1.260012). Compatible with all infra 4.2(3)+ |
| **UCSB-B480-M5** | UCSB-B480-M5 | **6.0(1.260012)** | 4.2(3) | VIC 1440 | 4-socket, 5th gen. EOL. Max supported: 6.0(1.260012). |
| **UCSB-B200-M6** | UCSB-B200-M6 | **6.0(2.260040)** | 4.2(3) | VIC 14425 | 6th gen blade. EOL. Max supported: 6.0(2.260040) per recommended firmware. Latest supported per EOL notice: 5.4(0.260028). |

**B-Series Server FW Compatibility with Infrastructure FW (from cross-version table):**

| B-Series Server FW | Min Infrastructure FW | Max Infrastructure FW | Notes |
|-------------------|----------------------|----------------------|-------|
| **6.0(2)** (e.g., **6.0(2.260040)**) | 4.2(3) | 6.0(2) | **LATEST RECOMMENDED** for M6 |
| **6.0(1)** (e.g., **6.0(1.260012)**) | 4.2(3) | 6.0(2) | **LATEST RECOMMENDED** for M5 |
| 5.4(0) | 4.1(3) | 6.0(2) | Compatible with all infra versions 4.1(3)+ |
| 5.3(0) | 4.1(3) | 6.0(2) | Compatible with all infra versions 4.1(3)+ |
| 5.2(2) | 4.1(3) | 6.0(2) | Compatible with all infra versions 4.1(3)+ |
| 5.2(1) | 4.1(3) | 6.0(2) | Compatible with all infra versions 4.1(3)+ |
| 5.2(0) | 4.1(3) | 6.0(2) | Compatible with all infra versions 4.1(3)+ |
| 5.1(0) | 4.1(3) | 6.0(2) | Compatible with all infra versions 4.1(3)+ |
| 4.3(3) | 4.1(3) | 6.0(2) | Compatible with all infra versions 4.1(3)+ |
| 4.3(2) | 4.1(3) | 6.0(2) | Compatible with all infra versions 4.1(3)+ |
| 4.2(3) | 4.1(3) | 6.0(2) | Compatible with all infra versions 4.1(3)+ |
| 4.2(2) | 4.1(3) | 4.2(3) | Not compatible with 4.3.x or 6.0.x infra |
| 4.2(1) | 4.1(3) | 4.2(3) | Not compatible with 4.3.x or 6.0.x infra |
| 4.1(3) | 4.1(3) | 4.2(3) | Not compatible with 4.3.x or 6.0.x infra |

---

### C-Series Rack Servers

C-Series servers attach to FI 6400, 6500, or 6600 Series Fabric Interconnects.

> **Note**: C-Series M5 and M6 are **End-of-Life (EOL)**. The latest supported IMM firmware versions are shown below. C-Series M7 and M8 are current-generation servers.

#### C-Series 1U/2U Rack Servers (Mainstream)

| Server Model | PIDs | IMM Server FW Latest (Recommended) | Min Infra FW | VIC Adapters (mLOM) | Generation | Notes |
|-------------|------|-------------------------------------|--------------|---------------------|------------|-------|
| **UCSC-C220-M5** | UCSC-C220-M5L/SN/SX | **4.3(2.250045)** | 4.1(3) | VIC 1457 | 5th gen 1U | EOL. Max supported: 4.3(2.260007). Compatible infra: 4.1(3) through 6.0(2). |
| **UCSC-C240-M5** | UCSC-C240-M5L/S/SD/SN/SX | **4.3(2.250045)** | 4.1(3) | VIC 1457 | 5th gen 2U | EOL. Max supported: 4.3(2.260007). Compatible infra: 4.1(3) through 6.0(2). |
| **UCSC-C480-M5** | UCSC-C480-M5, UCSC-C480-M5ML | **4.3(2.250045)** | 4.1(3) | VIC 1455 | 5th gen 4U | EOL. Max supported: 4.3(2.260007). Compatible infra: 4.1(3) through 6.0(2). |
| **UCSC-C220-M6** | UCSC-C220-M6N/S | **6.0(2.260044)** | 4.1(3) | VIC 14425, VIC 15237, VIC 15427 | 6th gen 1U | EOL. Max supported: 4.3(6.260033) per EOL notice (but 6.0(2.260044) present in recommended firmware). |
| **UCSC-C240-M6** | UCSC-C240-M6L/N/S/SN/SX | **6.0(2.260044)** | 4.1(3) | VIC 14425, VIC 15237, VIC 15427 | 6th gen 2U | EOL. See C220 M6 notes. |
| **UCSC-C225-M6** | UCSC-C225-M6L/N/S/SD/SN/SX | **6.0(2.260044)** | 4.1(3) | VIC 14425 | 6th gen 1U AMD | EOL. See C220 M6 notes. |
| **UCSC-C245-M6** | UCSC-C245-M6SX | **6.0(2.260044)** | 4.1(3) | VIC 14425 | 6th gen 2U AMD | EOL. See C220 M6 notes. |
| **UCSC-C220-M7** | UCSC-C220-M7N/S | **6.0(2.260044)** | 4.2(3) | VIC 15235, VIC 15425, VIC 15230, VIC 15427 | 7th gen 1U | Current gen. Compatible infra: 4.2(3) through 6.0(2). |
| **UCSC-C240-M7** | UCSC-C240-M7SN/SX | **6.0(2.260044)** | 4.2(3) | VIC 15235, VIC 15425 | 7th gen 2U | Current gen. Compatible infra: 4.2(3) through 6.0(2). |
| **UCSC-C220-M8** | UCSC-C220-M8E3S/S | **6.0(2.260044)** | 4.3(6) | VIC 15235, VIC 15420 | 8th gen 1U | Current gen. **Requires infra 4.3(6.250048)+ (6400/6500) or 6.0.x**. |
| **UCSC-C240-M8** | UCSC-C240-M8E3S/L/SX | **6.0(2.260044)** | 4.3(6) | VIC 15235, VIC 15420 | 8th gen 2U | Current gen. **Requires infra 4.3(6.250048)+**. |
| **UCSC-C225-M8** | UCSC-C225-M8N/S | **6.0(2.260044)** | 4.3(6) | VIC 15235, VIC 15420 | 8th gen 1U AMD | Current gen. **Requires infra 4.3(6.250048)+**. |
| **UCSC-C245-M8** | UCSC-C245-M8SX | **6.0(2.260044)** | 4.3(6) | VIC 15235, VIC 15420 | 8th gen 2U AMD | Current gen. **Requires infra 4.3(6.250048)+**. |

#### C-Series Specialty Rack Servers

| Server Model | PIDs | IMM Server FW Latest (Recommended) | Notes |
|-------------|------|-------------------------------------|-------|
| **UCSC-C125 M5** | UCSC-C125 | **4.3(2.250016)** | Single-socket AMD 2U node; EOL. |
| **UCSC-C460-M4** | UCSC-C460-M4 | 4.1(2m) | Very old; not supported in IMM 4.3.x+ |

**C-Series Server FW Compatibility with Infrastructure FW (from cross-version table):**

| C-Series Server FW | Min Infrastructure FW | Max Infrastructure FW | Notes |
|-------------------|----------------------|----------------------|-------|
| **6.0(2)** (e.g., **6.0(2.260044)**) | 4.2(3) | 6.0(2) | **LATEST RECOMMENDED** for M7/M8 |
| **6.0(1)** | 4.2(3) | 6.0(2) | — |
| **4.3(6)** (e.g., 4.3(6.260033)) | 4.1(3) | 6.0(2) | Compatible with all infra 4.1(3)+ |
| 4.3(5) | 4.1(3) | 6.0(2) | — |
| 4.3(4) | 4.1(3) | 6.0(2) | — |
| 4.3(3) | 4.1(3) | 6.0(2) | — |
| **4.3(2)** (e.g., **4.3(2.250045)**) | 4.1(3) | 6.0(2) | **LATEST RECOMMENDED** for M5 |
| 4.3(1) | 4.1(3) | 6.0(2) | — |
| 4.2(3) | 4.1(3) | 6.0(2) | Compatible with all infra 4.1(3)+ |
| 4.2(2) | 4.1(3) | 4.2(3) | Not compatible with 4.3.x or 6.0.x infra |
| 4.2(1) | 4.1(3) | 4.2(3) | Not compatible with 4.3.x or 6.0.x infra |
| 4.1(3) | 4.1(3) | 4.2(3) | Not compatible with 4.3.x or 6.0.x infra |

---

### X-Series Compute Nodes

X-Series compute nodes attach to FI 6400/6500/6600 Series (standard chassis mode) or directly to the UCSX-S9108-100G (X-Series Direct mode). They reside in the UCSX-9508 chassis.

> **Note**: X-Series server firmware uses a different version numbering scheme from B/C-Series. X-Series firmware major versions: 5.0.x, 5.1.x, 5.2.x, 5.3.x, 5.4.x, 6.0.x (not 4.3.x). The BIOS version numbering changed starting with 5.2(0.230040); X-Series BIOS follows 4.3 numbering internally from that point onward.

#### Standard X-Series Compute Nodes

| Server Model | PIDs | IMM Server FW Latest (Recommended) | Min Infra FW | VIC Adapters (mLOM) | Generation | Notes |
|-------------|------|-------------------------------------|--------------|---------------------|------------|-------|
| **UCSX-210C-M6** | UCSX-210C-M6 | **6.0(2.260040)** | 4.2(3) | VIC 15230, VIC 15420 | 6th gen 2-socket | EOL. Compatible infra: 4.2(3) through 6.0(2). |
| **UCSX-210C-M7** | UCSX-210C-M7 | **6.0(2.260040)** | 4.2(3) | VIC 15230, VIC 15420 | 7th gen 2-socket | EOL. Compatible infra: 4.2(3) through 6.0(2). |
| **UCSX-210C-M8** | UCSX-210C-M8 | **6.0(2.260040)** | 4.3(6) | VIC 15230, VIC 15420, VIC 15422 | 8th gen 2-socket | Current gen. **Requires infra 4.3(6.250048)+ (6400/6500) or 4.3(6.250094)+ (X-Direct)**. Server FW req: 5.4(0.250037)+. |
| **UCSX-215C-M8** | UCSX-215C-M8 | **6.0(2.260040)** | 4.3(6) | VIC 15420 | 8th gen 2-socket AMD | Current gen. X-Series Direct: Supported with Cisco UCS X9508 chassis. |
| **UCSX-410C-M7** | UCSX-410C-M7 | **6.0(2.260040)** | 4.2(3) | VIC 15230 | 7th gen 4-socket | EOL. Compatible infra: 4.2(3) through 6.0(2). |
| **UCSX-410C-M8** | UCSX-410C-M8 | **6.0(2.260040)** | 4.3(6) | VIC 15230 | 8th gen 4-socket | Current gen. See X210C M8 infra requirements. |
| **UCSX-9508 Chassis** | UCSX-9508 | **6.0(2.260042)** | 4.2(3) | — | X-Series Chassis | Firmware managed via Intersight. Holds up to 8 X-Series compute nodes. |

#### X-Series PCIe and Expansion Nodes

| Component | PIDs | IMM FW Latest (Recommended) | Notes |
|-----------|------|------------------------------|-------|
| **UCSX-580P PCIe Node** | UCSX-580P | **6.0(2.260043)** | GPU/PCIe expansion node for X9508 chassis. Requires 9416 X-Fabric Modules. |

#### X-Series Direct (XE Edge) Compute Nodes

| Server Model | PIDs | IMM Server FW Latest (Recommended) | Notes |
|-------------|------|-------------------------------------|-------|
| **UCSXE-130C-M8** | UCSXE-130C-M8-12, -20, -32 | **6.0(2.260042)** | Edge X-Series Direct compute node. Requires UCSX-S9108-100G infra FW 6.0(2.260045). |
| **UCSXE-ECMC** | UCSXE-ECMC-10G, UCSXE-ECMC-G1 | **6.0(2.260026)** | X-Series Edge chassis management controller firmware. |

**X-Series Server FW Compatibility with Infrastructure FW (from cross-version table):**

| X-Series Server FW | Min Infrastructure FW | Max Infrastructure FW | Notes |
|-------------------|----------------------|----------------------|-------|
| **6.0(2)** (e.g., **6.0(2.260040)**) | 4.2(3) | 6.0(2) | **LATEST RECOMMENDED** |
| **6.0(1)** | 4.2(3) | 6.0(2) | — |
| 5.4(0) | 4.2(3) | 6.0(2) | Compatible with infra 4.2(3)+; X210c M8 requires 5.4(0.250037)+ |
| 5.3(0) | 4.2(3) | 6.0(2) | Compatible with infra 4.2(3)+ |
| 5.2(2) | 4.2(3) | 6.0(2) | Compatible with infra 4.2(3)+ |
| 5.2(1) | 4.2(3) | 6.0(2) | Compatible with infra 4.2(3)+ |
| 5.2(0) | 4.2(3) | 6.0(2) | Compatible with infra 4.2(3)+ |
| 5.1(1) | 4.2(3) | 6.0(2) | Compatible with infra 4.2(3)+ |
| 5.1(0) | 4.2(3) | 6.0(2) | Compatible with infra 4.2(3)+ |
| 5.0(4) | 4.2(1) | 6.0(2) | Compatible with infra 4.2(1)+ |
| 5.0(2) | 4.2(1) | 4.2(3) | Not compatible with 4.3.x or 6.0.x infra |
| 5.0(1) | 4.2(1) | 4.2(3) | Not compatible with 4.3.x or 6.0.x infra |

---

## Summary

### 1. IMM Firmware Architecture Overview

Cisco Intersight Managed Mode decouples infrastructure and server firmware into two independent lifecycle tracks:

| Firmware Type | What It Controls | Managed By | FW Policy Type |
|---------------|-----------------|------------|----------------|
| **Infrastructure** | FI OS, switch fabric, chassis management, IFM/IOM behavior | Intersight FW Upgrade Policy | Infrastructure FW Policy |
| **Server** | BIOS, CIMC, VIC adapters, storage controllers, GPU firmware | Intersight FW Policy (per Server Profile) | Host FW Policy |

Key principles:
- **Independent upgrades**: You can upgrade infrastructure firmware without touching server firmware, and vice versa.
- **Policy-driven management**: Both tracks are managed via Intersight Firmware Policies applied to Server Profiles or Organization-level defaults.
- **License requirement**: Cisco Intersight **Essentials or Advanced** tier is required for firmware upgrade management.
- **FI support**: Infrastructure firmware 4.3.x supports FI 6400 and 6500 Series; 6.0.x adds FI 6600 Series support and introduces new capabilities.
- **X-Series Direct**: A special mode where UCSX-S9108-100G FIs are embedded in the X9508 chassis. Introduced with 4.3(4) infrastructure. Only supports X-Series compute nodes.

### 2. Cross-Version Compatibility Guidelines

Key compatibility rules from the release notes:

1. **6.0.x server firmware requires infra 4.2(3) or later** for all server families (B, C, X-Series). It does NOT work with infra 4.2(2) or earlier.
2. **C-Series and B-Series 6.0.x** server firmware is compatible with all infra versions from 4.2(3) through 6.0(2).
3. **X-Series 5.0(2) and 5.0(1)** server firmware is **only** compatible with infra 4.2(1) through 4.2(3). Not with 4.3.x or 6.0.x.
4. **C-Series 4.2(2), 4.2(1), 4.1(3)** server firmware is only compatible with infra up to 4.2(3). Not with 4.3.x or 6.0.x.
5. **New hardware requirements**: C220/C240 M8 servers require infra **4.3(6.250048)** or later on 6400/6500 FIs; X210c M8 compute requires **4.3(6.250094)+** on X-Series Direct FI.
6. **B-Series in X-Series Direct**: B-Series and C-Series servers connect through standard 6400/6500/6600 FIs only — not through X-Series Direct FI.
7. **4.3(5.240040) deprecated**: This specific build was deprecated due to CSCwn43752. Use 4.3(5.250004) or later in the 4.3(5) series.

### 3. Upgrade Path Guidelines

| Starting Point | Recommended Upgrade Path | Notes |
|---------------|--------------------------|-------|
| Infra 4.2.x | Upgrade to 4.3(2) → 4.3(6) → 6.0(2) | Verify server firmware compatibility at each step. |
| Infra 4.3(2)–4.3(5) | Upgrade directly to 4.3(6.260026) or 6.0(2.260045) | No intermediate stop required within 4.3.x. |
| Infra 4.3(6.x) | Upgrade directly to 6.0(2.260045) | Recommended upgrade path for all deployments. |
| Server FW 4.2.x or earlier | Upgrade to 4.3.x server FW first before upgrading infra to 6.0.x | 4.2(1), 4.2(2) server FW not compatible with 4.3+ infra. |
| Server FW (C-Series M5) | Target: **4.3(2.250045)** | EOL — 4.3(2.x) is the final supported train. |
| Server FW (B/X-Series M5/M6, C-Series M6) | Target: **6.0(1.260012)** or **6.0(2.260040/044)** | EOL servers still receive 6.0.x FW updates. |

**Before upgrading from 4.2.x to 4.3.x infra:**
- Ensure all server firmware is on 4.2(3) or later (C/B-Series) or 5.0(4)+ (X-Series) before upgrading infrastructure to 4.3.x, OR plan to upgrade server FW immediately after infra upgrade.
- 4.3.x infra does NOT support C/B-Series server FW 4.2(2) or earlier.

### 4. Best Practices

1. **Back up configuration** before any firmware upgrade using Intersight configuration backup or manual export.
2. **Use maintenance windows**: schedule upgrades during low-traffic periods. FI upgrades require a brief service outage for each FI in the pair.
3. **Policy-driven upgrades**: Use Intersight Firmware Policies for consistent, repeatable upgrades across the fleet. Avoid manual one-off upgrades.
4. **Stage rollout**: Test firmware upgrades on a subset of servers or a non-production domain before rolling out fleet-wide.
5. **Upgrade infrastructure first (or independently)**: If upgrading both tracks, consider upgrading infrastructure firmware first to ensure the FI supports the target server firmware.
6. **Validate HCL**: Before deploying new firmware, verify hardware compatibility using the [Cisco IMM HCL](https://intersight.com/help/saas/supported_systems#supported_hardware_for_intersight_managed_mode).
7. **Monitor deprecations**: Watch for deprecated builds (e.g., 4.3(5.240040)) in the release notes and avoid deploying them.

### 5. Critical Considerations

1. **Server firmware is per server family**: X-Series M8 firmware (`5.4(0.x)`) is separate from C-Series M8 firmware (`4.3(6.x)`). Each family has its own firmware bundle and release cadence.
2. **VIC adapter firmware** is included in server firmware bundles, but OS-level drivers (e.g., nenic, nfnic) must be updated separately to match adapter firmware.
3. **X-Series Direct FI is embedded**: The UCSX-S9108-100G FI resides in the X9508 chassis, not in a traditional FI rack slot. It uses different infrastructure FW filenames (`intersight-ucs-x-direct-infra.x.x.x.bin`).
4. **EOL servers still receive FW updates**: B-Series M5/M6 and C-Series M5/M6 are EOL but receive ongoing security and bug-fix firmware updates. They remain compatible with 6.0.x infrastructure.
5. **BIOS version numbering**: Starting with IMM Server FW 5.2(0.230040), X-Series BIOS follows the 4.3.x numbering scheme (consistent with UCSM). Earlier X-Series BIOS used 5.0.x / 5.1.x. Be aware of this when verifying BIOS version strings.
6. **C-Series M4 generation**: C220-M4, C240-M4 servers are not supported in IMM 4.3.x+ or Intersight Managed Mode. They can only be managed in Cisco IMC standalone mode.

### 6. Official Documentation

- [IMM Infrastructure Firmware 4.3 Release Notes](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/imm_infra_fw_rn_4_3/b_imm_infra_fw_rn_lb.html)
- [IMM Infrastructure Firmware 6.0 Release Notes](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/6-0/b-intersight-infrastructure-fw-rn-6-0.html)
- [IMM Server Firmware 4.3/5.2/5.3/5.4 Release Notes](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/4_3/b_intersight_server_fw_rn_4_3.html)
- [IMM Server Firmware 6.0 Release Notes](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/6-0/b-rn-cisco-intersight-managed-mode-server-firmware-release-6-0.html)
- [Cisco UCS Equivalency Matrix (IMM ↔ IMC ↔ UCSM)](https://www.cisco.com/c/dam/en/us/td/docs/unified_computing/ucs/c/sw/UCS-Equivalency-Matrix/index.html)
- [Managing Firmware in Intersight Managed Mode](https://intersight.com/help/saas/resources#managing_firmware_in_intersight_managed_mode)
- [Upgrading Fabric Interconnect Firmware in IMM](https://intersight.com/help/saas/resources/Upgrading_Fabric_Interconnect_Firmware_imm)
- [Supported Hardware for Intersight Managed Mode](https://intersight.com/help/saas/supported_systems#supported_hardware_for_intersight_managed_mode)
- [Cisco IMM Cross-Version Firmware Support (Confluence)](https://cisco-compute.atlassian.net/wiki/spaces/DCG/pages/778010727)

### 7. Recommended Actions

1. **For infrastructure firmware**: Upgrade all FI 6454, FI-64108, FI-6536, FI-6652, and FI-6664 Fabric Interconnects to **6.0(2.260045)** — the current recommended infrastructure firmware for all supported FI models.

2. **For X-Series Direct (9108)**: Upgrade to **6.0(2.260045)** infrastructure to ensure support for the latest X-Series M8 compute nodes and Edge (XE) nodes.

3. **For X-Series server firmware (M6/M7/M8)**: Standardize on **6.0(2.260040)** server firmware. This applies to UCSX-210C-M6/M7/M8, UCSX-215C-M8, and UCSX-410C-M7/M8.

4. **For C-Series M7/M8 server firmware**: Standardize on **6.0(2.260044)** for C220-M7/M8, C240-M7/M8, C225-M8, and C245-M8.

5. **For EOL C-Series M5 deployments**: Maintain on **4.3(2.250045)** — the latest recommended firmware in the 4.3(2).x series (final supported firmware train for M5).

6. **For EOL B-Series M5/M6 and C-Series M6 deployments**: Use **6.0(1.260012)** (M5) or **6.0(2.260040/044)** (M6) as the latest available firmware and continue monitoring security advisories.

7. **Plan upgrades** using Intersight Firmware Policies during scheduled maintenance windows. Test in staging before fleet-wide rollout.

8. **Validate HCL compliance** before deploying firmware upgrades using [Intersight's HCL validation tools](https://intersight.com/help/saas/supported_systems).

9. **Monitor Cisco Security Advisories (PSIRTs)** at [tools.cisco.com/security/center](https://tools.cisco.com/security/center/publicationListing.x) for any firmware-related CVEs affecting your deployed versions.
