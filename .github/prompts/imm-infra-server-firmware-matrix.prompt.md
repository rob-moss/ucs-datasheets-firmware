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
5. **IMM Recommended Firmware**: `ucs-docs/recommended-firmware-imm.md` — This is the authoritative source for recommended version notation and labels.  Only use the versions and recommendations from this file when marking versions in the report. 
Do NOT use the release notes for recommended versions, as they may be outdated. The authoritative source for recommended versions is the `recommended-firmware-imm.md` file.

If any of the five input files cannot be read or returns empty content, stop and output only the following error message: "ERROR: Could not read [filename]. Report generation aborted. Please verify the file path and retry." Do not generate partial output.

This report is focused exclusively on **Intersight Managed Mode (IMM)** and not UCS Manager (UCSM) or standalone (Cisco IMC) mode.

If the output directory does not exist or the file cannot be written, stop and show a header warning: "WARNING: Could not write to ucs-firmware-reports/report-imm-infra-server-firmware-matrix.md"

# Output File

The filename should be `ucs-firmware-reports/report-imm-infra-server-firmware-matrix.md`.
- If the file already exists, read the previous version number and increment it (following the minor version increment rule defined in the metadata section).
- Replace the entire contents of the file with the newly generated report.



---

# Headings and Structure

At the beginning of the report list the following metadata fields:

- **Source Files**: "Cisco IMM Infrastructure Firmware Release Notes 4.3 and 6.0 / Server Firmware Release Notes 4.3–5.4 and 6.0"
- **Generated Date**: Use today's date (current date when creating/updating the report)
- **Last Updated Date**: Extract the most recent "Last Updated" date in the header from the four release note source documents (files 1–4 listed in the Input Files section). If there is no date available, put in today's date. Do not use the recommended-firmware-imm.md file for this field.
- **Document version**: Increment the version number each time this report is regenerated. If the file already exists, read the previous document version number and increment the minor version by 0.1 (e.g., 1.0 → 1.1 → 1.2). Always increment the minor version regardless of the scope of changes.

---

# Overview Section Requirements

Immediately after the document metadata, create an "Overview" section that:

1. Briefly explains the IMM firmware model:
   - **Infrastructure firmware** runs on Fabric Interconnects (FI-6400, 6500, 6600 Series and X-Series Direct IFM-9108). It is separate from server firmware.
   - **Server firmware** runs on X-Series, B-Series, and C-Series servers.
   - Infrastructure and server firmware can be upgraded independently — you do NOT need to upgrade infra firmware to use latest server firmware and vice versa.

2. Lists all supported infrastructure hardware models organized by type:
   - **Fabric Interconnects (FI):** FI-6454, FI-64108, FI-6536, FI-6600 Series (if supported)
   - **Intelligent Fabric Modules (IFM):** 9108-100G (UCSX-I-9108-100G IFM), 9108-25G (UCSX-I-9108-25G IFM), 
   - **X-Direct FI**: S9108-100G (X-Direct FI and IFM)
   - **X-Fabric Modules (XFM):** X9416 (UCSX-FS-9416), X9516 (UCSX-FS-9516)
   - **PCIe Nodes**: X440p, X580p
   - **I/O Modules (IOM):** 2204, 2208, 2304, 2304V2, 2408 (if still relevant for 4.3/6.0.x)

3. Lists all supported server hardware models organized by family. **The following are examples only.** The agent must extract and list **ALL** server models mentioned in the release notes files, organized by family and generation:
   - **X-Series Compute Nodes:** UCSX-210C-M6, UCSX-210C-M7, UCSX-210C-M8, UCSX-410C-M7, UCSX-410C-M8, etc. (all M6+)
   - **B-Series Blade Servers:** UCSB-B200-M5, UCSB-B200-M6, UCSB-B480-M5, UCSB-B480-M6, etc. (all M5+)
   - **C-Series Rack Servers:** UCSC-C220-M5, UCSC-C220-M6/M7/M8, UCSC-C240-M5/M6/M7/M8, UCSC-C480-M5/M6/M7/M8, etc. (all M5+)
   
   If the release notes mention additional models (e.g., UCSX-215C-M8, UCSX-580P, UCSB-B480-M6, UCSC-C225-M6, UCSC-C245-M8, etc.), include them in the appropriate family section. Omit any models not explicitly referenced in the four release note source documents.

4. Lists recommended firmware versions from `ucs-docs/recommended-firmware-imm.md` grouped by platform type. Use exact versions and labels from the recommended-firmware-imm.md file; do not hard-code versions in this prompt. The report must reference the versions found in that authoritative file.

5. Notes the scope: this report covers IMM Infrastructure Firmware 4.3.x and 6.0.x, and IMM Server Firmware 4.3.x, 5.2.x, 5.3.x, 5.4.x, and 6.0.x, applied to the infrastructure and server hardware models listed above.

---

# Actions to Take

1. Extract the **Cross-Version Firmware Support** tables from both the 4.3 and 6.0 infrastructure firmware release notes. These tables map infrastructure firmware versions to compatible server firmware versions across all server families (X-Series, B-Series, C-Series).

2. Create a **consolidated cross-version compatibility matrix** that shows:
   - Infrastructure firmware version (left column)
   - Compatible X-Series server firmware versions (separate column)
   - Compatible B-Series server firmware versions (separate column)
   - Compatible C-Series server firmware versions (separate column)
   - Supported infrastructure hardware (FI models, IOM/IFM models) - use bold labels (**FI:**, **IOM:**, **IFM:**)
   - Notes column for recommended versions and special constraints
   - Always include IOMs and IFMs that are compatible with the FIs listed.
   - Compatible firmware must be based on the Infrastructure firmware (Fabric Interconnects).  Only compatible equipment should be listed.


3. For each server family (X-Series, B-Series, C-Series), create a table listing:
   - Server model (e.g., UCSX-210C-M8, UCSB-B200-M6, UCSC-C220-M7)
   - All supported server firmware versions (in descending order)
   - Chassis/platform information
   - Notes about generation, socket count, or deprecation status

4. Use **exact version notation** from `ucs-docs/recommended-firmware-imm.md` for all recommended versions throughout the report. For example, use `6.0(2.260045)` rather than a generic `6.0(2)`.

5. IMM firmware versions use an extended notation format:
   - Infrastructure FI: e.g., `4.3(6.250094)`, `6.0(1.260006)`, `6.0(2.260045)`
   - Server (X-Series): e.g., `5.4(0.250040)`, `6.0(2.260040)`
   - Server (B-Series, C-Series): e.g., `4.3(6.250044)`, `6.0(1.260012)`, `6.0(2.260044)`
   - Use exact versions from the source documents; do not abbreviate or shorten.
   - Some documents abbreviate firmware versions (e.g., `6.0(2)` instead of `6.0(2.260045)`). Always use the full version notation from the authoritative recommended-firmware-imm.md and the release notes cross-firmware tables where available.

6. List out all major firmware versions and patch versions in descending order within each cell of the tables. For example, if a cell lists multiple compatible server firmware versions, list the latest version first.

## Firmware bundles, patches, and updates

The following versions are abbreviated in the release notes and recommended-firmware-imm.md file. Use the full version notation from the authoritative source when generating the report.

There are three categories of firmware versions to consider:
- Major versions (e.g., 4.3.x, 6.0.x)
- Minor versions (e.g., 4.3(6), 6.0(2))
- Patch versions (e.g., 4.3(6.250094), 6.0(2.260045))

Whenever referring to a version, always use the full version notation from the authoritative source (recommended-firmware-imm.md) and do not abbreviate.


### Infrastructure firmware
Newest first, oldest last:
- **6.0.x:** -- all versions
  - 6.0(1)
  - 6.0(2)
- **4.3.x:** -- all versions
  - 4.3(2)
  - 4.3(3)
  - 4.3(4)
  - 4.3(5)
  - 4.3(6)
- **4.2.x:** -- all versions
  - 4.2(1)
  - 4.2(2)
  - 4.2(3)
- **4.1.x:** -- all versions
  - 4.1(3)

### X-Series server firmware
Newest first, oldest last:
- **6.0.x:** -- all versions
  - 6.0(2)
  - 6.0(1)
- **5.4.x:** -- all versions
  - 5.4(0)
- **5.3.x:** -- all versions
  - 5.3(0)
- **5.2.x:** -- all versions
  - 5.2(2)
  - 5.2(1)
  - 5.2(0)
- **5.1.x:** -- all versions
  - 5.1(0)
- **4.3.x:** -- all versions
  - 4.3(6)
  - 4.3(5)
  - 4.3(4)
  - 4.3(3)
  - 4.3(2)
  - 4.3(1)
- **4.2.x:** -- all versions
  - 4.2(3)
  - 4.2(2)
  - 4.2(1)
- **4.1.x:** -- all versions
  - 4.1(3)

### B-Series server firmware
Newest first, oldest last:
  - **6.0.x:** -- all versions
   - 6.0(2)
   - 6.0(1)
  - **5.4.x:** -- all versions
   - 5.4(0)
  - **5.3.x:** -- all versions
   - 5.3(0)
  - **5.2.x:** -- all versions
   - 5.2(2)
   - 5.2(1)
   - 5.2(0)
  - **5.1.x:** -- all versions
   - 5.1(0)
  - **4.3.x:** -- all versions
   - 4.3(3)
   - 4.3(2)
  - **4.2.x:** -- all versions
   - 4.2(3)
   - 4.2(2)
   - 4.2(1)
   - 4.1(3)

### C-Series server firmware
Newest first, oldest last:
  - **6.0.x:** -- all versions
   - 6.0(2)
   - 6.0(1)
  - **5.4.x:** -- all versions
   - 5.4(0)
  - **5.3.x:** -- all versions
   - 5.3(0)
  - **5.2.x:** -- all versions
   - 5.2(2)
   - 5.2(1)
   - 5.2(0)
  - **5.1.x:** -- all versions
   - 5.1(0)
  - **4.3.x:** -- all versions
   - 4.3(6)
   - 4.3(5)
   - 4.3(4)
   - 4.3(3)
   - 4.3(2)


---

# Infrastructure Firmware Cross-Version Matrix

Create a **Cross-Version Firmware Support** matrix for infrastructure firmware. Use data extracted from the 4.3 and 6.0 infrastructure release notes. 

**IMM Infrastructure firmware is deployed on:**
- Fabric Interconnects (FI-6400/6500/6600 Series)
- Intelligent Fabric Modules (IFM) for X-Series Direct

Create a consolidated matrix showing infrastructure firmware versions and compatible server firmware across all server families:

## IMM Infrastructure and Server Firmware Cross-Version Compatibility Matrix

Extract the **"Cross-Version Firmware Support"** or **"Supported Server Firmware Versions"** table from the 4.3 and 6.0 infrastructure firmware release notes (Input Files 1 and 2). Consolidate these into a single matrix organized by infrastructure firmware version.

**Table structure and data source:**

| Infrastructure FW Version | X-Series Server FW | B-Series Server FW | C-Series Server FW | Supported Infrastructure Hardware | Notes |
|--------------------------|--------------------|--------------------|--------------------|------------------------------------|-------|
| [Latest 6.0.x from release notes] | [All compatible X-Series versions from RN, newest first] | [All compatible B-Series versions from RN, newest first] | [All compatible C-Series versions from RN, newest first] | **FI:** [models from RN]<br>**IFM:** [if applicable]<br>**IOM:** [if applicable] | Mark with **LATEST RECOMMENDED** if version matches top recommended from recommended-firmware-imm.md |
| [Other 6.0.x versions from release notes] | [Applicable versions] | [Applicable versions] | [Applicable versions] | [Hardware models] | [Constraints, if any] |
| [Latest 4.3.x from release notes] | [All compatible X-Series versions] | [All compatible B-Series versions] | [All compatible C-Series versions] | [Hardware models] | Mark with **RECOMMENDED STABLE** if explicitly designated in release notes |
| [Other 4.3.x versions] | [Applicable versions] | [Applicable versions] | [Applicable versions] | [Hardware models] | [Constraints] |

**Data extraction rules:**
- **Source:** Extract the cross-version table directly from the infrastructure firmware release notes (files 1 and 2)
- **Version format:** Use the **exact full version notation** from the release notes (e.g., `6.0(2.260045)`, not abbreviated `6.0(2)`)
- **Column order:** List all compatible server firmware versions in **descending order** (latest first) within each cell, separated by `<br>`
- **Hardware:** List supported FI models, IFM, and IOM models for each infrastructure firmware row. Include only models explicitly mentioned in the release notes for that version
- **Recommended labels:** 
  - `**LATEST RECOMMENDED**` = highest recommended version per infrastructure generation from recommended-firmware-imm.md
  - `**RECOMMENDED STABLE**` = only if the release notes or recommended-firmware-imm.md explicitly designates a version as stable/LTS
- **Constraints:** Note any hardware-specific requirements (e.g., "IOM-2408 requires FI 6.0.1+") in the Notes column

**Table formatting rules:**
- List firmware versions in descending order (latest first)
- Mark recommended versions from `ucs-docs/recommended-firmware-imm.md` with labels in the Notes column:
  - `**LATEST RECOMMENDED**` for the single highest recommended version per infrastructure firmware generation (4.3.x and 6.0.x separately)
  - `**RECOMMENDED STABLE**` only if the file explicitly designates a version as a stable or long-term release. If the file does not use this designation, omit the **RECOMMENDED STABLE** label entirely.
- Use `<br>` to separate multiple compatible versions within a cell
- List server firmware versions in descending order within each cell
- Infrastructure hardware column uses bold labels (**FI:**, **IOM:**, **IFM:**) for clarity
- Note any hardware-specific constraints (e.g., IOM-2408 minimum FI version) in the Notes column
- Include IOM-2204 and IOM-2208 in the Supported Infrastructure Hardware column for any infrastructure firmware row where the source release notes confirm their support. If the source documents do not mention them for a given version, omit them from that row.

---

# Server Firmware Support by Server Family

Create a "Server Firmware Support" section that lists all server models by family and the firmware versions they support.

## Infrastructure Hardware Models (IMM-supported)
For any hardware model listed in this section with a conditional qualifier (e.g., "if supported"), include it in the report only if it is explicitly referenced in one of the four release note source documents. If not found, omit it without comment.
### Fabric Interconnects (FI)
- **6400 Series:** FI-6454, FI-64108
- **6500 Series:** FI-6536
- **6600 Series:** (if supported in 4.3/6.0 release notes)

### Intelligent Fabric Modules (IFM) - X-Series Direct
- **9108-100G:** Supports X-Series Direct deployments with standalone fabric interconnect

### I/O Modules (IOM) - For Traditional Chassis-based deployments
- **2204, 2208:** Legacy IOMs (Still supported in 4.3.x)
- **2304, 2304V2:** Standard IOMs for FI-6300/6400 series
- **2408:** Modern IOM for FI-6400/6536 series


---

## X-Series Compute Node Firmware Support

| Server Model | Supported Server FW Versions | Chassis | Notes |
|-------------|------------------------------|---------|-------|
| **[Server Model from release notes]** | [All supported X-Series versions from release notes, newest first] | UCSX-9508 | [Generation, socket count] |
| (Add all X-Series M6+ models found in the release notes, with supported firmware versions from the cross-version support tables) | | | |

---

## B-Series Blade Server Firmware Support

| Server Model | Supported Server FW Versions | Blade Chassis | Notes |
|-------------|------------------------------|---------------|----|  
| **[Server Model from release notes]** | [All supported B-Series versions from release notes, newest first] | UCSB-5108 | [Generation, socket count] |
| (Add all B-Series M5+ models found in the release notes, with supported firmware versions from the cross-version support tables) | | | |

---

## C-Series Rack Server Firmware Support

| Server Model | Supported Server FW Versions | Form Factor | Notes |
|-------------|------------------------------|-------------|-------|
| **[Server Model from release notes]** | [All supported C-Series versions from release notes, newest first] | [1U, 2U, etc.] | [Generation, socket count, max version if applicable] |
| (Add all C-Series M5+ models found in the release notes, with supported firmware versions from the cross-version support tables) | | | |

**Formatting rules for server tables:**
- Use exact version strings from source documents—do not abbreviate
- In server firmware table cells that list multiple versions, bold only the version string that matches the recommended version for that model server from recommended-firmware-imm.md. Leave all other version strings in plain text. Example: **[Latest recommended version]**<br>[Other supported versions]<br>[Older supported versions]
- Use `<br>` to separate multiple versions within a cell
- List versions in descending order (latest first)
- For M5-generation servers with limited firmware support, note max supported version
- For M6/M7/M8 servers, emphasize latest recommendations

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

**Local Cached Files (Preferred):**
- `ucs-docs/ucs-Release-Notes-for-Cisco-Intersight-Managed-Mode-Infrastructure-Firmware-Release-4.3.md` — IMM Infrastructure Firmware 4.3 Release Notes
- `ucs-docs/ucs-Release-Notes-for-Cisco-Intersight-Managed-Mode-Infrastructure-Firmware-Release-6.0.md` — IMM Infrastructure Firmware 6.0 Release Notes
- `ucs-docs/ucs-Release-Notes-for-Cisco-Intersight-Managed-Mode-Server-Firmware-Release-4.3-5.2-5.3-and-5.4.md` — IMM Server Firmware 4.3/5.2/5.3/5.4 Release Notes
- `ucs-docs/ucs-Release-Notes-for-Cisco-Intersight-Managed-Mode-Server-Firmware-Release-6.0.md` — IMM Server Firmware 6.0 Release Notes

**Online Documentation (Fallback):**
- [IMM Infrastructure Firmware 4.3 Release Notes](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/imm_infra_fw_rn_4_3/b_imm_infra_fw_rn_lb.html)
- [IMM Infrastructure Firmware 6.0 Release Notes](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/6-0/b-intersight-infrastructure-fw-rn-6-0.html)
- [IMM Server Firmware 4.3/5.2/5.3/5.4 Release Notes](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/4_3/b_intersight_server_fw_rn_4_3.html)
- [IMM Server Firmware 6.0 Release Notes](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/6-0/b-rn-cisco-intersight-managed-mode-server-firmware-release-6-0.html)
- [Cisco UCS Equivalency Matrix](https://www.cisco.com/c/dam/en/us/td/docs/unified_computing/ucs/c/sw/UCS-Equivalency-Matrix/index.html)
- [Managing Firmware in Intersight Managed Mode (Intersight Help)](https://intersight.com/help/saas/resources#managing_firmware_in_intersight_managed_mode)

## 7. Recommended Actions
1. For all new X-Series, C-Series M6/M7/M8, and B-Series M6 deployments, standardize on the latest recommended 6.0.x server firmware from `ucs-docs/recommended-firmware-imm.md`
2. For C-Series M5 and B-Series M5 deployments, use the latest recommended 4.3.x or 6.0.x server firmware from `ucs-docs/recommended-firmware-imm.md`
3. For infrastructure firmware, use the latest recommended version from `ucs-docs/recommended-firmware-imm.md`
4. Plan firmware upgrades during scheduled maintenance windows using Intersight firmware policies
5. Validate HCL compatibility before deploying new firmware versions
6. Monitor Cisco Security Advisories for any firmware-related CVEs


---

# Example Cross-Version Matrix Format

NOTE: This section is for prompt guidance only. Do NOT include this heading or the code blocks below in the output report file.

**The version strings shown below are illustrative examples only and must not be copied into the report. All version data must be extracted from the source documents (release notes and recommended-firmware-imm.md).**

**Example Cross-Version Firmware Support Matrix Structure:**

```
| Infrastructure FW Version | X-Series Server FW | B-Series Server FW | C-Series Server FW | Supported Infrastructure Hardware | Notes |
|--------------------------|--------------------|--------------------|--------------------|------------------------------------|-------|
| [Latest 6.0.x version from RN] | [All compatible X-Series versions, newest first] | [All compatible B-Series versions, newest first] | [All compatible C-Series versions, newest first] | **FI:** [FI models from RN]<br>**IFM:** [IFM models if applicable]<br>**IOM:** [IOM models if applicable] | [Mark with **LATEST RECOMMENDED** if this version matches the highest recommended version per generation] |
| [Other 6.0.x versions from RN] | [Applicable versions] | [Applicable versions] | [Applicable versions] | [Hardware models] | [Notes/constraints] |
| [Latest 4.3.x version from RN] | [All compatible X-Series versions] | [All compatible B-Series versions] | [All compatible C-Series versions] | [Hardware models] | [Mark with **RECOMMENDED STABLE** if explicitly designated] |
| [Other 4.3.x versions] | [Applicable versions] | [Applicable versions] | [Applicable versions] | [Hardware models] | [Constraints] |
```

**Example Server Model Table Structure:**

```
| Server Model | Supported Server FW Versions | Chassis/Form Factor | Notes |
|-------------|------------------------------|-----------|-------|
| [Server model from RN] | [Latest version]<br>[Other versions, descending order] | [Chassis] | [Generation, socket count] |
| [Another server model] | **[Bold if recommended]**<br>[Other versions] | [Chassis] | [Generation, socket count] |
```
