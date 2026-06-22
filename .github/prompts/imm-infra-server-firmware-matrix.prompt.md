---
agent: agent
name: imm-infra-server-firmware-matrix
---
# Input Files (read in parallel for efficiency)

Read all of the following files in parallel:

1. **IMM Infrastructure Firmware 4.3 Release Notes**: `ucs-docs/ucs-Release-Notes-for-Cisco-Intersight-Managed-Mode-Infrastructure-Firmware-Release-4.3.md`
2. **IMM Infrastructure Firmware 6.0 Release Notes**: `ucs-docs/ucs-Release-Notes-for-Cisco-Intersight-Managed-Mode-Infrastructure-Firmware-Release-6.0.md`
3. **IMM Server Firmware 4.3/5.2/5.3/5.4 Release Notes**: `ucs-docs/ucs-Release-Notes-for-Cisco-Intersight-Managed-Mode-Server-Firmware-Release-4.3-5.2-5.3-and-5.4.md`
4. **IMM Server Firmware 6.0 Release Notes**: `ucs-docs/ucs-Release-Notes-for-Cisco-Intersight-Managed-Mode-Server-Firmware-Release-6.0.md`
5. **IMM Recommended Firmware**: `ucs-docs/recommended-firmware-imm.md` — This is the authoritative source for recommended version notation and labels.

This report is focused exclusively on **Intersight Managed Mode (IMM)** and not UCS Manager (UCSM) or standalone (Cisco IMC) mode.

---

# Headings and Structure

At the beginning of the report list the following metadata fields:

- **Source**: "Cisco IMM Infrastructure Firmware Release Notes 4.3 and 6.0 / Server Firmware Release Notes 4.3–5.4 and 6.0"
- **Generated**: Use today's date (current date when creating/updating the report)
- **Last Updated**: Extract the most recent "Last Updated" date from any of the four source documents above (use the latest date found)
- **Document version**: Increment the version number each time this report is regenerated (e.g., 1.0 → 1.1 → 1.2)

---

# Overview Section Requirements

Immediately after the document metadata, create an "Overview" section that:

1. Briefly explains the IMM firmware model:
   - **Infrastructure firmware** runs on Fabric Interconnects (FI 6400, 6500, 6600 Series and X-Series Direct 9108). It is separate from server firmware.
   - **Server firmware** runs on B-Series, C-Series, and X-Series servers.
   - Infrastructure and server firmware can be upgraded independently — you do NOT need to upgrade infra firmware to use latest server firmware and vice versa.

2. Lists all recommended firmware versions from `ucs-docs/recommended-firmware-imm.md` grouped by platform type (Infrastructure FI, X-Series, B-Series, C-Series). Use bold notation, for example:
   - Infrastructure (FI 6454/64108/6536/6600): **6.0(2.260045)** (Latest)
   - X-Series M6/M7/M8 Server: **6.0(2.260040)** (Latest)
   - B-Series M5/M6 Server: see file for version per model
   - C-Series M5 Server: **4.3(2.250045)** (Latest for M5)
   - C-Series M6/M7/M8 Server: **6.0(2.260044)** (Latest)

3. Notes the scope: this report covers IMM Infrastructure Firmware 4.3.x and 6.0.x, and IMM Server Firmware 4.3.x, 5.2.x, 5.3.x, 5.4.x, and 6.0.x.

---

# Actions to Take

1. Extract the **Cross-Version Firmware Support** tables from both the 4.3 and 6.0 infrastructure firmware release notes. These tables map infrastructure firmware versions to compatible server firmware versions (by server family: X-Series, B-Series, C-Series).

2. Use **exact version notation** from `ucs-docs/recommended-firmware-imm.md` for all recommended versions throughout the report. For example, use `6.0(2.260045)` rather than a generic `6.0(2)`.

3. IMM firmware versions use an extended notation format:
   - Infrastructure FI: e.g., `4.3(6.250094)`, `6.0(1.260006)`, `6.0(2.260045)`
   - Server (X-Series): e.g., `5.4(0.250040)`, `6.0(2.260040)`
   - Server (B-Series, C-Series): e.g., `4.3(6.250044)`, `6.0(1.260012)`, `6.0(2.260044)`
   - Use exact versions from the source documents; do not abbreviate or shorten.

---

# Infrastructure Firmware Cross-Version Matrix

Create a **Cross-Version Firmware Support** matrix for infrastructure firmware. Use data extracted from the 4.3 and 6.0 infrastructure release notes.

**Infrastructure firmware is deployed on Fabric Interconnects, not servers.** Create separate matrices for each FI series:

## Matrix 1 — UCS 6400 and 6500 Series Fabric Interconnects (FI-6454, FI-64108, FI-6536)

| Infrastructure FW Version | Compatible X-Series Server FW | Compatible B-Series Server FW | Compatible C-Series Server FW | Notes |
|--------------------------|-------------------------------|-------------------------------|-------------------------------|-------|
| **6.0(2.260045)** | ... | ... | ... | **LATEST RECOMMENDED** |
| **6.0(1.260006)** | ... | ... | ... | |
| **4.3(6.250094)** | ... | ... | ... | **RECOMMENDED STABLE** (4.3.x) |
| ... | ... | ... | ... | |

## Matrix 2 — UCS 6600 Series Fabric Interconnects

Include if 6600 Series FI data is present in the release notes. Otherwise note that coverage begins in a future document update.

## Matrix 3 — UCS X-Series Direct Fabric Interconnect (UCS 9108-100G)

| Infrastructure FW Version | Compatible X-Series Server FW | Notes |
|--------------------------|-------------------------------|-------|
| **6.0(2.260045)** | ... | **LATEST RECOMMENDED** |
| ... | ... | |

**Table formatting rules:**
- List firmware versions in descending order (latest first)
- Mark recommended versions from `ucs-docs/recommended-firmware-imm.md` with labels in the Notes column:
  - `**LATEST RECOMMENDED**` for the latest version
  - `**RECOMMENDED STABLE**` for any designated stable version
- Use `<br>` to separate multiple compatible versions within a cell
- List server firmware versions in descending order within each cell

---

# Server Firmware Support by Server Family

Create a "Server Firmware Support" section with subsections per server family. Use data from the server firmware release notes (4.3/5.2/5.3/5.4 and 6.0).

## B-Series Blade Servers

| Server Model | Supported Server FW Versions | Supported Infrastructure FW | VIC Adapters | Notes |
|-------------|------------------------------|------------------------------|--------------|-------|
| **UCSB-B200-M5** | 6.0(1.260012)<br>5.4(0.x)<br>5.3(0.x)<br>... | 4.3(x) / 6.0(x) | VIC 1340, VIC 1440 | 5th gen blade |
| **UCSB-B200-M6** | 6.0(2.260040)<br>5.4(0.x)<br>... | 4.3(x) / 6.0(x) | VIC 14425 | 6th gen blade |
| **UCSB-B480-M5** | 6.0(1.260012)<br>... | 4.3(x) / 6.0(x) | VIC 1440 | 4-socket blade |

## C-Series Rack Servers

| Server Model | Supported Server FW Versions | Supported Infrastructure FW | VIC Adapters | Notes |
|-------------|------------------------------|------------------------------|--------------|-------|
| **UCSC-C220-M5** | 4.3(2.250045)<br>4.3(6.x)<br>... | 4.3(x) / 6.0(x) | VIC 1457 | 5th gen 1U rack |
| **UCSC-C220-M6** | 6.0(2.260044)<br>5.4(0.x)<br>... | 4.3(x) / 6.0(x) | VIC 14425 | 6th gen 1U rack |
| **UCSC-C220-M7** | 6.0(2.260044)<br>... | 4.3(x) / 6.0(x) | VIC 15235 | 7th gen 1U rack |
| **UCSC-C220-M8** | 6.0(2.260044)<br>... | 6.0(x) | VIC 15235 | 8th gen 1U rack |
| **UCSC-C240-M5** | 4.3(2.250045)<br>... | 4.3(x) / 6.0(x) | VIC 1457 | 5th gen 2U rack |
| (add all models found in release notes) | | | | |

## X-Series Compute Nodes

| Server Model | Supported Server FW Versions | Supported Infrastructure FW | Chassis | Notes |
|-------------|------------------------------|------------------------------|---------|-------|
| **UCSX-210C-M6** | 6.0(2.260040)<br>5.4(0.x)<br>... | 4.3(x) / 6.0(x) | UCSX-9508 | 6th gen X-Series |
| **UCSX-210C-M7** | 6.0(2.260040)<br>... | 4.3(x) / 6.0(x) | UCSX-9508 | 7th gen X-Series |
| **UCSX-210C-M8** | 6.0(2.260040)<br>... | 4.3(x) / 6.0(x) | UCSX-9508 | 8th gen X-Series |
| **UCSX-410C-M7** | 6.0(2.260040)<br>... | 4.3(x) / 6.0(x) | UCSX-9508 | 4-socket X-Series |
| (add all models found in release notes) | | | | |

**Formatting rules for server tables:**
- Use exact version strings from the source documents — do not abbreviate
- Mark recommended versions from `ucs-docs/recommended-firmware-imm.md` in bold within cells
- Use `<br>` to separate multiple versions within a cell
- List versions in descending order (latest first)
- For server models with no 6.0.x version (older M4/M5 generation), note the end-of-support status if indicated in the release notes

---

# Summary Section

Include all of the following subsections:

## 1. IMM Firmware Architecture Overview
Explain the separation of infrastructure (FI) firmware and server firmware in IMM. Key points:
- Infrastructure firmware controls FI behavior, fabric connectivity, and chassis management
- Server firmware controls BIOS, CIMC, adapters, and storage controllers for compute nodes
- Upgrades are managed independently through Intersight policies (firmware policies)
- License requirement: Cisco Intersight Essentials or Advanced tier is required for firmware management

## 2. Cross-Version Compatibility Guidelines
Key rules from the release notes:
- Which server firmware generations are compatible with which infrastructure firmware versions
- Any specific constraints (e.g., minimum infra version required for a given server model)
- X-Series Direct FI vs standard 6400/6500/6600 compatibility differences

## 3. Upgrade Path Guidelines
Specific paths for upgrading from:
- 4.3.x infra → 6.0.x infra
- 4.3.x server → 5.x/6.0.x server
- Pre-4.3.x deployments: minimum version requirements before jumping to 6.0.x
- Note any "skip version" restrictions documented in the release notes

## 4. Best Practices
- Back up configuration before upgrading
- Use maintenance windows; schedule upgrades during low-traffic periods
- Upgrade infrastructure firmware before or independently from server firmware
- Test with a subset of servers before rolling out fleet-wide
- Use Intersight firmware policies for consistent, policy-driven upgrades

## 5. Critical Considerations
- Server firmware bundles are per-server-family (X-Series M8 has its own bundle, separate from C-Series M8)
- VIC adapter firmware is included in server bundles but may require driver updates on the OS side
- Ensure HCL compliance before deploying new firmware versions
- Legacy M4-generation servers (C220-M4, C240-M4) have end-of-life firmware paths; note maximum supported versions

## 6. Official Documentation
- [IMM Infrastructure Firmware 4.3 Release Notes](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/imm_infra_fw_rn_4_3/b_imm_infra_fw_rn_lb.html)
- [IMM Infrastructure Firmware 6.0 Release Notes](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/6-0/b-intersight-infrastructure-fw-rn-6-0.html)
- [IMM Server Firmware 4.3/5.2/5.3/5.4 Release Notes](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/4_3/b_intersight_server_fw_rn_4_3.html)
- [IMM Server Firmware 6.0 Release Notes](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/6-0/b-rn-cisco-intersight-managed-mode-server-firmware-release-6-0.html)
- [Cisco UCS Equivalency Matrix](https://www.cisco.com/c/dam/en/us/td/docs/unified_computing/ucs/c/sw/UCS-Equivalency-Matrix/index.html)
- [Managing Firmware in Intersight Managed Mode (Intersight Help)](https://intersight.com/help/saas/resources#managing_firmware_in_intersight_managed_mode)

## 7. Recommended Actions
1. For all new X-Series, C-Series M6/M7/M8, and B-Series M6 deployments, standardize on **6.0(2.x)** server firmware (latest generation)
2. For C-Series M5 and B-Series M5 deployments, use the latest recommended 4.3.x or 6.0.x server firmware from `ucs-docs/recommended-firmware-imm.md`
3. For infrastructure firmware, upgrade FI 6454/64108/6536 to **6.0(2.260045)** (latest recommended)
4. Plan firmware upgrades during scheduled maintenance windows using Intersight firmware policies
5. Validate HCL compatibility before deploying new firmware versions
6. Monitor Cisco Security Advisories for any firmware-related CVEs

---

# Output File

The filename should be `ucs-firmware-reports/report-imm-infra-server-firmware-matrix.md`.
- If the file already exists, read the previous version number and increment it.
- Replace the entire contents of the file with the newly generated report.

---

# Example Cross-Version Matrix Format

```
| Infrastructure FW Version | Compatible X-Series Server FW | Compatible B-Series Server FW | Compatible C-Series Server FW | Notes |
|--------------------------|-------------------------------|-------------------------------|-------------------------------|-------|
| **6.0(2.260045)** | 6.0(2.260040)<br>6.0(2.260042)<br>5.4(0.260010) | 6.0(2.260040)<br>6.0(1.260012) | 6.0(2.260044)<br>4.3(6.260026) | **LATEST RECOMMENDED** for FI 6454/64108/6536 |
| **6.0(1.260006)** | 6.0(1.x)<br>5.4(0.x) | 6.0(1.260012)<br>5.4(0.x) | 6.0(1.x)<br>4.3(6.x) | Initial 6.0 GA release |
| **4.3(6.250094)** | 5.4(0.250040)<br>5.3(0.x)<br>5.2(0.x) | 5.4(0.x)<br>4.3(6.x) | 4.3(6.250044)<br>4.3(5.x)<br>4.3(2.x) | **RECOMMENDED STABLE** for 4.3.x infra |
```

Once the report is generated and saved, run the prompt in `.github/prompts/push-all.prompt.md` to push the changes to the repository.
