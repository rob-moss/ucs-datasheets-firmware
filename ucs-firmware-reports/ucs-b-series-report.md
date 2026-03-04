# UCS B-Series Server Firmware Report

**Generated:** 2026-03-04  
**Report Inputs (Defaults Applied):**

| Parameter | Value |
|---|---|
| Server Model | Cisco UCS B200 M5 |
| Firmware Version | 4.3(6e) |
| Operating System / Hypervisor | VMware ESXi 8u3 |

---

## 1. Compatible Fabric Interconnects (FIs) and IO Modules (IOMs)

UCS B-Series blade servers are housed in the **Cisco UCS 5108 Blade Server Chassis** and connect to Fabric Interconnects through IO Modules (IOMs). The following FIs and IOMs are compatible with the Cisco UCS B200 M5.

### Compatible Fabric Interconnects

| FI Series | Model | Min. Firmware for B200 M5 Support |
|---|---|---|
| **UCS 6400 Series** | UCS 6454 | 4.0(1a) |
| **UCS 6400 Series** | UCS 64108 | 4.1(1a) |
| **UCS 6500 Series** | UCS 6536 | 4.2(3p) |
| **UCS 6600 Series** | UCS 6652 | 4.3(6a) |
| **UCS 6600 Series** | UCS 6664 | 6.0(2) *(mixed-cluster with 6652 only)* |

> **Note:** The UCS 6664 Fabric Interconnect originally supported only UCS X-Series servers. Support for the UCS 5108 B-Series chassis (and thus B-Series blades) was extended from UCSM 6.0(2) in a mixed-cluster configuration paired with a UCS 6652.

### Compatible IO Modules (IOMs) for UCS 5108 Chassis

| IOM Model | Notes |
|---|---|
| **UCS-IOM-2408** | Recommended IOM for M5 servers with UCS 6400/6500/6600 series FIs. Requires VIC 1300/1400 series adapters for M5. |
| **UCS-IOM-2304V1/V2** | Supported with UCS 6300/6536 series FIs |
| **UCS-IOM-220x** | Supported with UCS 6200/6300/6400 series FIs |

> **Source:** `ucs-Release-Notes-for-Cisco-UCS-Manager-Release-6.0.md` (b_cisco-ucs-manager-internal-dependencies-release-6-0.html) — Table 1: Minimum Host Firmware Versions for Blade Servers; `ucs-Cisco-UCS-6600-Series-Fabric-Interconnects-Data-Sheet.md` — Table 3.

---

## 2. Latest Firmware Version Available for UCS B-Series Servers

The latest available firmware bundle for UCS B-Series servers as of the date of this report is in the **4.3(6)** release train. The specific default version used in this report is **4.3(6e)**.

### Firmware Bundle Overview

| Release Train | Latest Known Patch | Release Notes URL |
|---|---|---|
| **4.3(6)** | 4.3(6e) | https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/release/notes/b_release-notes-ucsm-4_3.html |
| **4.3(5)** | 4.3(5d) | https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/release/notes/b_release-notes-ucsm-4_3.html |
| **4.3(2)** | 4.3(2f) | https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/release/notes/b_release-notes-ucsm-4_3.html |

Firmware downloads are available at:  
https://software.cisco.com/download/release.html?mdfid=283853163&flowid=25821&softwareid=283655681

The B-Series ISO driver download is available at:  
https://software.cisco.com/download/home/283853163/type/283853158

> **Source:** `json-UCS-Managed-Mode-B200-M5-CPU-v1-ESXi-8u3.md` — Version column (lines 12676+); `ucs-Release-Notes-for-Cisco-UCS-Manager-Release-4.3.md`.

---

## 3. Supported Operating Systems and Hypervisors

The following operating systems and hypervisors have been validated with the Cisco UCS B200 M5 under UCSM Managed Mode:

### VMware ESXi

| Version | Status |
|---|---|
| VMware ESXi 6.7 Update 3 | Supported |
| VMware ESXi 7.0 Update 3 | Supported |
| VMware ESXi 8.0 Update 3 | Supported *(default in this report)* |

### Other Operating Systems

Based on available HCL data for the UCS B200 M5 UCSM Managed Mode, the following additional OSes are supported:

- **Microsoft Windows Server** — 2016, 2019, 2022
  - Note: Windows Server 2019 with VIC 14xx/1400-series adapters requires hotfix KB5001384
- **Red Hat Enterprise Linux (RHEL)** — Multiple versions supported
- **SUSE Linux Enterprise Server (SLES)** — Multiple versions supported
- **Oracle Linux** — Multiple versions supported

> **Source:** `json-UCS-Managed-Mode-B200-M5-CPU-v1-ESXi-8u3.md`, `json-UCS-Managed-Mode-B200-M5-CPU-v1-ESXi-7u3.md`, `json-UCS-Managed-Mode-B200-M5-CPU-v2-ESXi-7u3.md` — URL Title fields confirming per-OS data files.

---

## 4. Supported Adapters for UCS B-Series Servers

The following Virtual Interface Cards (VICs) are supported in the Cisco UCS B200 M5:

| PID | Description | Form Factor | VIC Generation |
|---|---|---|---|
| **UCSB-MLOM-40G-03** | Cisco UCS 1340 Virtual Interface Card | mLOM | 1300-series |
| **UCSB-VIC-M83-8P** | Cisco UCS 1380 Virtual Interface Card | Mezz (8-port) | 1300-series |
| **UCSB-MLOM-40G-04** | Cisco UCS 1440 Virtual Interface Card | mLOM | 1400-series |
| **UCSB-VIC-M84-4P** | Cisco UCS 1480 Virtual Interface Card | Mezz (4-port) | 1400-series |

### RAID Controllers

| PID | Description |
|---|---|
| **UCS-M2-HWRAID** | Cisco Boot Optimized M.2 RAID Controller |
| **UCSB-MRAID12G** | Broadcom FlexStorage 12G SAS RAID Controller |
| **UCSB-MRAID12G-HE** | Broadcom FlexStorage 12G SAS RAID Controller (High-Endurance) |

> **Note:** The VIC 1300-series (1340, 1380) uses the `nenic` Ethernet driver. The VIC 1400-series (1440, 1480) supports both `nenic` and `nenic-ens` (Enhanced Network Stack). `NENIC` is the native version of the ENIC driver; ENIC is no longer supported with ESXi 6.5 and later.

> **Source:** `json-UCS-Managed-Mode-B200-M5-CPU-v1-ESXi-8u3.md` — HardwareTypes → Adapters → CNA section, firmware bundle 4.3(6) entry.

---

## 5. Recommended Adapter Firmware and Driver Versions

The following table provides the recommended VIC adapter firmware and driver versions for **Cisco UCS B200 M5** running **VMware ESXi 8u3** at firmware bundle **4.3(6e)**.

### VIC Adapter Firmware and Driver Versions — Bundle 4.3(6) / ESXi 8u3

| Adapter | PID | VIC Firmware | Driver Type | Driver Version |
|---|---|---|---|---|
| Cisco UCS 1340 VIC | UCSB-MLOM-40G-03 | **4.6(5)** | nenic (Ethernet) | `2.0.17.0-1OEM.800.1.0.20613240` |
| Cisco UCS 1340 VIC | UCSB-MLOM-40G-03 | **4.6(5)** | nfnic (Fibre Channel) | `5.0.0.50-1OEM.803.0.0.24022510` |
| Cisco UCS 1380 VIC | UCSB-VIC-M83-8P | **4.6(5)** | nenic (Ethernet) | `2.0.17.0-1OEM.800.1.0.20613240` |
| Cisco UCS 1380 VIC | UCSB-VIC-M83-8P | **4.6(5)** | nfnic (Fibre Channel) | `5.0.0.50-1OEM.803.0.0.24022510` |
| Cisco UCS 1440 VIC | UCSB-MLOM-40G-04 | **5.3(5)** | nenic (Ethernet) | `2.0.17.0-1OEM.800.1.0.20613240` |
| Cisco UCS 1440 VIC | UCSB-MLOM-40G-04 | **5.3(5)** | nenic-ens (Ethernet ENS) | `1.0.18.0-1OEM.800.1.0.20613240` |
| Cisco UCS 1440 VIC | UCSB-MLOM-40G-04 | **5.3(5)** | nfnic (Fibre Channel) | `5.0.0.50-1OEM.803.0.0.24022510` |
| Cisco UCS 1480 VIC | UCSB-VIC-M84-4P | **5.3(5)** | nenic (Ethernet) | `2.0.17.0-1OEM.800.1.0.20613240` |
| Cisco UCS 1480 VIC | UCSB-VIC-M84-4P | **5.3(5)** | nenic-ens (Ethernet ENS) | `1.0.18.0-1OEM.800.1.0.20613240` |
| Cisco UCS 1480 VIC | UCSB-VIC-M84-4P | **5.3(5)** | nfnic (Fibre Channel) | `5.0.0.50-1OEM.803.0.0.24022510` |

### RAID Controller Driver Versions — Bundle 4.3(6) / ESXi 8u3

| Controller | PID | Firmware Version | Driver | Driver Version |
|---|---|---|---|---|
| Broadcom FlexStorage 12G SAS RAID | UCSB-MRAID12G | `24.21.0-0156 \| 6.36.00.3 \| NA` | lsi_mr3 | `7.728.02.00-1vmw.803.0.0.24022510` |
| Broadcom FlexStorage 12G SAS RAID (HE) | UCSB-MRAID12G-HE | `24.21.0-0156 \| 6.36.00.3 \| NA` | lsi_mr3 | `7.728.02.00-1vmw.803.0.0.24022510` |
| Boot Optimized M.2 RAID | UCS-M2-HWRAID | `2.3.17.1014` | *(included in OS)* | N/A |

### Driver Version Notes

- **nenic** — Native ENIC driver (Ethernet). Replaces the older `enic` driver for ESXi 6.5+.
- **nenic-ens** — Enhanced Network Stack (ENS) variant of nenic. Available on VIC 1400-series (1440, 1480) only. Offers higher performance in ENS-enabled environments.
- **nfnic** — Native FC NIC driver (Fibre Channel over Ethernet/FCoE). Required when using FCoE or native FC via the VIC.

> **Source:** `json-UCS-Managed-Mode-B200-M5-CPU-v1-ESXi-8u3.md` — firmware bundle version **4.3(6)** entry (lines 12676–12850), HardwareTypes → Adapters → CNA section. The 4.3(6) entry in the HCL data corresponds to the 4.3(6e) patch level referenced in this report's inputs.

---

## References

| Source | URL / Filename |
|---|---|
| UCS B200 M5 HCL — ESXi 8u3 | `json-UCS-Managed-Mode-B200-M5-CPU-v1-ESXi-8u3.md` |
| UCS 6600 Series Data Sheet | `ucs-Cisco-UCS-6600-Series-Fabric-Interconnects-Data-Sheet.md` |
| UCS Manager 4.3 Release Notes | `ucs-Release-Notes-for-Cisco-UCS-Manager-Release-4.3.md` |
| UCS Manager 6.0 Release Notes | `ucs-Release-Notes-for-Cisco-UCS-Manager-Release-6.0.md` |
| UCS Manager 6.0 Internal Dependencies | `ucs-Release-Notes-for-Cisco-UCS-Manager-Release-6.0.md` (b_cisco-ucs-manager-internal-dependencies-release-6-0.html) |
