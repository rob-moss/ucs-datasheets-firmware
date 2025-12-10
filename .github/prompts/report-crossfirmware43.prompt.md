---
agent: agent
name: report-crossfirmware43-v1
---
Read the Cisco UCS Manager Cross-Version Firmware Support, Release 4.3 document located at: ucs-firmware-docs/Cisco UCS Manager Cross-Version Firmware Support, Release 4.3 - Cisco.html

Also read the file ucs-firmware-reports/report-recommended-firmware.md which lists the Recommended Firmware for Infrastructure.

Ensure the data is accurate and corresponds to the official UCS Cross-Reference Hardware Compatibility Matrix for UCS Manager 4.3.

This document provides information on the compatibility of different UCS Manager firmware versions with various server models, fabric interconnects, and IOMs.

This report is focused on UCS Manager and not Intersight, Intersight Managed Mode or IMM.

# Headings and Structure
At the beginning of the report list the following fields, based on the document metadata.  The Document Version should be incremented each time this report is generated.
- Source
- Generated
- Last Updated
- Document version


# Actions to take

Compare the Recommended Firmware versions for Infrastructure from the report-recommended-firmware.md file with the data in the Cisco UCS Manager Cross-Version Firmware Support, Release 4.3 document.

1. For each Recommended Firmware version for Infrastructure, use the Recommended verison rather than the overall version ie 4.3(6c) rather than 4.3(6) to find all matching firmware versions in the Cross-Version Firmware Support document.



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

In the summary section at the end of the report, include:
- Links to each of the document sections used to compile the report as a URL to the public document
- Any important notes or caveats about cross-firmware support for UCS Manager 4.3



# Output file
The filename should be `ucs-firmware-reports/report-ucs-crossfirmware-4.3.md`.
- You can replace the contents of this file with the generated report.
- You can read the previous report version from this file if needed and increment its version number.


# Cross Firmware Output
An example of the output format in markdown:
| Infrastructure Bundle | B and C Server Bundle Versions | Supported Fabric Interconnect + IOM | Notes |
|----------------------|--------------------------------|-------------------------------------|----------------------------|--------|
| **4.3(6c)** | 4.3(6), 4.3(5), 4.3(4), 4.3(3), 4.3(2), 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1) | **FI:** 6332, 6332-16UP, 6454, 64108, 6536<br>**IOM:** 2204, 2208, 2304, 2304V2, 2408 | IOM-2408 requires FI 6400/6536. IOM-2304/2304V2 requires FI 6300/6536 |



# Server Models Support
In another table, with the heading of "Server Models Support", list all supported server models for UCS Manager 4.3 firmware versions.
- the server firmware version should be listed in descending order, starting from the latest version 4.3(6) down to 4.2(2)
- the table should include the following columns:
  - Server firmware version
  - Server Models Supported
  - Adapters Supported
  - ESXi Versions
  - Driver nenic/nefnic versions
- The CNA or Adapter should list only the model numbers, not the full names, such as "UCS-VIC-M82-8P, etc rather than "Cisco UCS-VIC-M82-8P: Cisco UCS 1280 Virtual Interface Card" and should also list the firmware version supported for that adapter ie 4.4(1)
- The Driver Versions that we are interested in are as follows
  - nenic-ens
  - nefnic-ens
  - nfnic
  - nenic
  - The nenic/nfnic Driver versions should list all supported versions for that firmware version from the "Driver Version" field, ie "1.0.6.0-1OEM.700.1.0.15843807 nenic-ens" or "5.0.0.43-1OEM.700.1.0.15843807 nfnic"
  - List the drivers supported for that firmware version, separated by commas


# Server Models Report Output
Create a matrix in the following format:

| Server firmware version | Server Models Supported | Adapter and Firmware Supported | ESXi Versions | Driver nenic/nefnic versions |
|-----------------------|------------------------|--------------------|---------------|--------------------------|
| **4.3(6)** | UCS B200 M5, UCS B200 M6, UCS C220 M5, UCS C240 M5, UCS C220 M6, UCS C240 M6 | CNA VIC 1457, CNA VIC 1457E, CNA VIC 1455, CNA VIC 1455E, CNA VIC 1387, CNA VIC 1387E | ESXi 6.5, ESXi 6.7, ESXi 7.0, ESXi 7.0U1, ESXi 7.0U2, ESXi 7.0U3, ESXi 7.0U3c, ESXi 8.0 | nenic 2.5(4a), nenic 2.5(4b), nenic 2.6(1a), nenic 2.6(1b), nefnic 1.9(4a), nefnic 1.9(4b), nefnic 1.10(1a), nefnic 1.10(1b) |

Once the report is generated, save it to the specified file path.

Finally, run the prompt in `.github/prompts/push-all.prompt.md` to push the changes to the repository.
