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
- Supported UCS Server Models
- Notes (if any)

The output should be as follows;
- Beginning with firmware version 4.2(2)
- List all supported server models and fabric interconnect + IOM combinations for each firmware version

The filename should be `ucs-firmware-reports/ucs-crossfirmware-4.3.md`


An example of the output format in markdown:
| Infrastructure Bundle | B and C Server Bundle Versions | Supported Fabric Interconnect + IOM | Supported UCS Server Models | Notes |
|----------------------|--------------------------------|-------------------------------------|----------------------------|--------|
| **4.3(6)** | 4.3(6), 4.3(5), 4.3(4), 4.3(3), 4.3(2), 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1) | **FI:** 6332, 6332-16UP, 6454, 64108, 6536<br>**IOM:** 2204, 2208, 2304, 2304V2, 2408 | B200 M4, B200 M5, B200 M6, B480 M5 | Full support for all M5, and M6 generation servers. IOM-2408 requires FI 6400/6536. IOM-2304/2304V2 requires FI 6300/6536 |
