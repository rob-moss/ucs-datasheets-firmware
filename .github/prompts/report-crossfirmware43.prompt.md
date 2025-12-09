---
agent: agent
---
Read the Cisco UCS Manager Cross-Version Firmware Support, Release 4.3 document located at: ucs-firmware-docs/Cisco UCS Manager Cross-Version Firmware Support, Release 4.3 - Cisco.html


Ensure the data is accurate and corresponds to the official UCS Cross-Reference Hardware Compatibility Matrix for UCS Manager 4.3.


Create a matrix of firmware versions that support the hardware listed above.
The matrix should have the following columns:
- Infrastructure Version
- Host FW versions (B and C Server Bundle Versions)
- Supported Fabric Interconnect + IOM
- Notes (if any)


The output should be as follows;
- List all supported server models and fabric interconnect + IOM combinations for each firmware version
- Do not list UCS B, C or X series servers in this table
- Begin firmware versions with the latest first, going down to 4.2(2) as the oldest supported version
- Format the output in markdown table format

In the summary section at the end of the report, include:
- Links to each of the document sections used to compile the report as a URL to the public document
- Any important notes or caveats about cross-firmware support for UCS Manager 4.3




The filename should be `ucs-firmware-reports/ucs-crossfirmware-4.3.md`. You can replace the contents of this file with the generated report.


An example of the output format in markdown:
| Infrastructure Bundle | B and C Server Bundle Versions | Supported Fabric Interconnect + IOM | Notes |
|----------------------|--------------------------------|-------------------------------------|----------------------------|--------|
| **4.3(6)** | 4.3(6), 4.3(5), 4.3(4), 4.3(3), 4.3(2), 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1) | **FI:** 6332, 6332-16UP, 6454, 64108, 6536<br>**IOM:** 2204, 2208, 2304, 2304V2, 2408 | IOM-2408 requires FI 6400/6536. IOM-2304/2304V2 requires FI 6300/6536 |

In another table, with the heading of "Server Models Support", list all supported server models for UCS Manager 4.3 firmware versions in the following format:
| Server firmware version | Server Models Supported | Adapters Supported | ESXi Versions | Driver nenic/nefnic versions |
|-----------------------|------------------------|--------------------|---------------|--------------------------|
| **4.3(6)** | UCS B200 M5, UCS B200 M6, UCS C220 M5, UCS C240 M5, UCS C220 M6, UCS C240 M6 | CNA VIC 1457, CNA VIC 1457E, CNA VIC 1455, CNA VIC 1455E, CNA VIC 1387, CNA VIC 1387E | ESXi 6.5, ESXi 6.7, ESXi 7.0, ESXi 7.0U1, ESXi 7.0U2, ESXi 7.0U3, ESXi 7.0U3c, ESXi 8.0 | nenic 2.5(4a), nenic 2.5(4b), nenic 2.6(1a), nenic 2.6(1b), nefnic 1.9(4a), nefnic 1.9(4b), nefnic 1.10(1a), nefnic 1.10(1b) |
