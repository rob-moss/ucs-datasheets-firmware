---
agent: agent
name: report-crossfirmware43-v2
---
# Input Files (read in parallel for efficiency)

1. Read the Cisco UCS Manager Cross-Version Firmware Support, Release 4.3 document located at: `ucs-firmware-docs/Cisco UCS Manager Cross-Version Firmware Support, Release 4.3 - Cisco.html`

2. Read the file `ucs-firmware-reports/report-recommended-firmware.md` which lists the Recommended Firmware for Infrastructure. This is the authoritative source for recommended version notation and labels.

Ensure the data is accurate and corresponds to the official UCS Cross-Reference Hardware Compatibility Matrix for UCS Manager 4.3.

This document provides information on the compatibility of different UCS Manager firmware versions with various server models, fabric interconnects, and IOMs.

This report is focused on UCS Manager and not Intersight, Intersight Managed Mode or IMM.

# Headings and Structure
At the beginning of the report list the following fields:
- **Source**: Extract from the Cisco document metadata
- **Generated**: Use today's date (current date when creating/updating the report)
- **Last Updated**: Extract from the source Cisco document metadata (NOT today's date)
- **Document version**: Increment the version number each time this report is regenerated (e.g., 1.0 → 1.1 → 1.2)


# Overview Section Requirements

Immediately after the document metadata, create an "Overview" section that:
1. Lists ALL recommended firmware versions from report-recommended-firmware.md in bold with their designations:
   - Latest recommended version (e.g., **6.0(1b)** (Latest))
   - Recommended stable version (e.g., **4.3(6c)** (Recommended Stable))
   - Long-term stable version (e.g., **4.2(3o)** (Long-term Stable))

2. When recommended versions include releases outside the 4.3.x series:
   - Add a scope note explaining this document covers 4.3.x versions specifically
   - Reference where users can find documentation for other major releases
   - Example: "**Note**: This document covers UCS Manager 4.3.x firmware versions. For UCS Manager 6.0(1b) compatibility information, refer to the UCS Manager 6.0 Cross-Version Firmware Support documentation."

# Actions to take

1. Compare the Recommended Firmware versions for Infrastructure from the report-recommended-firmware.md file with the data in the Cisco UCS Manager Cross-Version Firmware Support, Release 4.3 document.

2. For each Recommended Firmware version for Infrastructure, use the exact recommended version notation rather than the general version (e.g., use 4.3(6c) rather than 4.3(6), use 4.2(3o) rather than 4.2(3)). This notation must be maintained consistently throughout ALL tables and text in the document.



Create a matrix of firmware versions that support the hardware listed above.
The matrix should have the following columns:
- Infrastructure Version
- Host FW versions (B and C Server Bundle Versions)
- Supported Fabric Interconnect + IOM
- Notes (if any)

Create separate matrixes for the following UCS Fabric Interconnects:
- UCS 6300/6400/6500 Series Fabric Interconnects
- UCS 6324 and UCS Mini Series Fabric Interconnects


The output should be as follows;
- List all supported server models and fabric interconnect + IOM combinations for each firmware version
- Do not list UCS B, C or X series servers in this table
- Begin firmware versions with the latest first, going down to 4.2(2) as the oldest supported version
- Format the output in markdown table format
- **IMPORTANT**: For rows containing recommended firmware versions (as identified in report-recommended-firmware.md):
  * Use the exact version notation with suffixes (4.3(6c), 4.2(3o))
  * Add visual labels in the Notes column:
    - "**RECOMMENDED STABLE**" for the recommended stable version
    - "**LONG-TERM STABLE**" for the long-term stable version
  * Example: "**RECOMMENDED STABLE**. Latest 4.3.x release with full backward compatibility"

In the summary section at the end of the report, include:

1. **Important Compatibility Guidelines**: Key requirements for IOM, FI, and upgrade paths

2. **Upgrade Path Guidelines**: Specific paths from different starting versions (4.0.x, 4.1.x, 4.2.x to 4.3.x)

3. **Best Practices**: Configuration backup, maintenance windows, testing, compatibility verification

4. **Critical Considerations**: Server bundle mixing, adapter firmware, driver compatibility, IOM/FI pairing

5. **Official Documentation**: Links to public Cisco documentation including:
   - Primary cross-version firmware support document
   - UCS Manager Firmware Management Guide
   - Release notes and compatibility matrices

6. **Recommended Actions** (CRITICAL - must include all recommended versions):
   - For latest features: Guidance on migrating to the latest recommended version (e.g., 6.0(1b)) with reference to appropriate documentation
   - For stable 4.3.x deployments: Recommendation to standardize on the recommended stable version (e.g., 4.3(6c))
   - For long-term stability: Recommendation to maintain the long-term stable version (e.g., 4.2(3o))
   - Plan upgrades during maintenance windows
   - Validate compatibility before upgrades
   - Monitor security advisories
   
   Example format:
   ```
   **Recommended Actions**:
   1. For latest features and capabilities, plan migration to **6.0(1b)** (refer to UCS Manager 6.0 documentation)
   2. For stable 4.3.x deployments, standardize on **4.3(6c)** for optimal stability and latest 4.3 features
   3. For long-term stability on 4.2.x, maintain **4.2(3o)** with extended support and backward compatibility
   4. Plan upgrades during scheduled maintenance windows
   ...
   ```



# Output file
The filename should be `ucs-firmware-reports/report-ucs-crossfirmware-4.3.md`.
- You can replace the contents of this file with the generated report.
- You can read the previous report version from this file if needed and increment its version number.


# Cross Firmware Output
An example of the output format in markdown:
| Infrastructure Bundle | B and C Server Bundle Versions | Supported Fabric Interconnect + IOM | Notes |
|----------------------|--------------------------------|-------------------------------------|--------|
| **4.3(6c)** | 4.3(6), 4.3(5), 4.3(4), 4.3(3), 4.3(2), 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1) | **FI:** 6332, 6332-16UP, 6454, 64108, 6536<br>**IOM:** 2204, 2208, 2304, 2304V2, 2408 | **RECOMMENDED STABLE**. Latest 4.3.x release with full backward compatibility |
| **4.3(5)** | 4.3(5), 4.3(4), 4.3(3), 4.3(2), 4.3(1), 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1) | **FI:** 6332, 6332-16UP, 6454, 64108, 6536<br>**IOM:** 2204, 2208, 2304, 2304V2, 2408 | Supports all 6300/6400/6536 models |
| **4.2(3o)** | 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1), 4.0(4), 4.0(2), 4.0(1) | **FI:** 6200, 6332, 6332-16UP, 6454, 64108, 6536<br>**IOM:** 2204, 2208, 2304, 2304V2, 2408 | **LONG-TERM STABLE**. First version supporting FI-6536. Includes legacy 6200 support |



# Server Models Support

Create a "Server Models Support" section with separate subsections for each server bundle version.

**IMPORTANT**: Use the exact recommended version notation (e.g., 4.2(3o)) in section headings:
- "### Server Bundle 4.2(3o) - Long-Term Stable Compatibility Matrix"
- "### Server Bundle 4.2(2) - Compatibility Matrix"

# Server Models Report Output

For each server bundle version, create a table in the following format:

| Server Model | VIC Adapters (Firmware) | Supported ESXi Versions | Driver Versions | Notes |
|--------------|------------------------|------------------------|-----------------|--------|
| **B200 M5** | VIC 1340 (4.5(2))<br>VIC 1440 (5.2(2)) | ESXi 6.7 U3<br>ESXi 7.0 U3<br>ESXi 8.0 U3 | nenic 1.0.42.0<br>nenic-ens 1.0.42.0<br>nfnic 5.0.0.44 | 5th generation blade, widely deployed |

**Formatting Requirements**:
- List server models by generation (B200 M4, B200 M5, B200 M6, B480 M5, and relevant C-Series models)
- Server firmware versions: List in descending order, starting from latest down to 4.2(2)
- VIC adapters: Show model and firmware version in format "VIC 1440 (5.2(2))"
- Use line breaks (<br>) to separate multiple adapters, ESXi versions, or drivers within a cell
- Driver versions: List only the version number (e.g., "nenic 1.0.42.0"), not the full OEM string
- Drivers of interest: nenic, nenic-ens, nfnic, nefnic-ens
- Include a Notes column for additional context about each server model (generation, key features, common use cases)

Once the report is generated, save it to the specified file path.

Finally, run the prompt in `.github/prompts/push-all.prompt.md` to push the changes to the repository.
