# UCS Manager 4.3 Cross-Version Firmware Compatibility Matrix

**Source:** Cisco UCS Manager Cross-Version Firmware Support, Release 4.3  
**Generated:** December 9, 2025  
**Last Updated:** September 23, 2025 (Cisco official documentation)

---

## Overview

This matrix shows the supported combinations of Infrastructure (A Bundle) and Server Firmware (B/C Bundle) versions across different Cisco UCS platforms. The Infrastructure Bundle includes Cisco UCS Manager, Cisco NX-OS, IOM and FEX firmware. The Server Bundle includes host firmware, BIOS, Cisco IMC, adapter firmware and drivers.

**Note:** This report covers cross-version firmware compatibility for UCS Manager infrastructure (Fabric Interconnects, IOMs) and does not enumerate specific server model support in the infrastructure tables below. Server model compatibility information is available in the Cisco UCS Hardware Compatibility List (HCL).

---

## UCS 6300/6400/6536 Series Fabric Interconnects

| Infrastructure Bundle | B and C Server Bundle Versions | Supported Fabric Interconnect + IOM | Notes |
|----------------------|--------------------------------|-------------------------------------|--------|
| **4.3(6)** | 4.3(6), 4.3(5), 4.3(4), 4.3(3), 4.3(2), 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1) | **FI:** 6332, 6332-16UP, 6454, 64108, 6536<br>**IOM:** 2204, 2208, 2304, 2304V2, 2408 | IOM-2408 requires FI 6400/6536. IOM-2304/2304V2 requires FI 6300/6536 |
| **4.3(5)** | 4.3(5), 4.3(4), 4.3(3), 4.3(2), 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1) | **FI:** 6332, 6332-16UP, 6454, 64108, 6536<br>**IOM:** 2204, 2208, 2304, 2304V2, 2408 | IOM-2408 requires FI 6400/6536. IOM-2304/2304V2 requires FI 6300/6536 |
| **4.3(4)** | 4.3(4), 4.3(3), 4.3(2), 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1) | **FI:** 6332, 6332-16UP, 6454, 64108, 6536<br>**IOM:** 2204, 2208, 2304, 2304V2, 2408 | IOM-2408 requires FI 6400/6536. IOM-2304/2304V2 requires FI 6300/6536 |
| **4.3(3)** | 4.3(3), 4.3(2), 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1) | **FI:** 6332, 6332-16UP, 6454, 64108, 6536<br>**IOM:** 2204, 2208, 2304, 2304V2, 2408 | IOM-2408 requires FI 6400/6536. IOM-2304/2304V2 requires FI 6300/6536 |
| **4.3(2)** | 4.3(2), 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1) | **FI:** 6332, 6332-16UP, 6454, 64108, 6536<br>**IOM:** 2204, 2208, 2304, 2304V2, 2408 | IOM-2408 requires FI 6400/6536. IOM-2304/2304V2 requires FI 6300/6536 |
| **4.2(3)** | 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1), 4.0(4), 4.0(2), 4.0(1) | **FI:** 6200, 6332, 6332-16UP, 6454, 64108, 6536<br>**IOM:** 2204, 2208, 2304, 2304V2, 2408 | First version supporting FI-6536. IOM-2408 requires FI 6400/6536. IOM-2304/2304V2 requires FI 6300/6536. IOM-2204/2208 supported on FI-6200 |
| **4.2(2)** | 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1), 4.0(4), 4.0(2), 4.0(1) | **FI:** 6200, 6332, 6332-16UP, 6454, 64108<br>**IOM:** 2204, 2208, 2304, 2304V2, 2408 | FI-6536 NOT supported. IOM-2408 requires FI 6400. IOM-2304/2304V2 requires FI 6300. IOM-2204/2208 supported on all FI models |

---

## UCS Mini (6324 Fabric Interconnect)

| Infrastructure Bundle | B and C Server Bundle Versions | Supported Fabric Interconnect + IOM | Notes |
|----------------------|--------------------------------|-------------------------------------|--------|
| **4.3(6)** | 4.3(6), 4.3(5), 4.3(4), 4.3(3), 4.3(2), 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1) | **FI:** 6324 (Mini)<br>**IOM:** 2204, 2208 | Single chassis deployment. Maximum 8 blade servers per chassis |
| **4.3(5)** | 4.3(5), 4.3(4), 4.3(3), 4.3(2), 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1) | **FI:** 6324 (Mini)<br>**IOM:** 2204, 2208 | Single chassis deployment. Maximum 8 blade servers per chassis |
| **4.3(4)** | 4.3(4), 4.3(3), 4.3(2), 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1) | **FI:** 6324 (Mini)<br>**IOM:** 2204, 2208 | Single chassis deployment. Maximum 8 blade servers per chassis |
| **4.3(3)** | 4.3(3), 4.3(2), 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1) | **FI:** 6324 (Mini)<br>**IOM:** 2204, 2208 | Single chassis deployment. Maximum 8 blade servers per chassis |
| **4.3(2)** | 4.3(2), 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1) | **FI:** 6324 (Mini)<br>**IOM:** 2204, 2208 | Single chassis deployment. Maximum 8 blade servers per chassis |
| **4.2(3)** | 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1), 4.0(4), 4.0(2), 4.0(1) | **FI:** 6324 (Mini)<br>**IOM:** 2204, 2208 | Single chassis deployment. Maximum 8 blade servers per chassis. Full backward compatibility with 4.0(x) and 4.1(x) server bundles |
| **4.2(2)** | 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1), 4.0(4), 4.0(2), 4.0(1) | **FI:** 6324 (Mini)<br>**IOM:** 2204, 2208 | Single chassis deployment. Maximum 8 blade servers per chassis |

---

## UCS X-Series Direct (UCSX-S9108-100G)

| Infrastructure Bundle | B Server Bundle Versions | Supported Fabric Interconnect + IOM | Notes |
|----------------------|--------------------------|-------------------------------------|--------|
| **4.3(6)** | 4.3(6), 4.3(5), 4.3(4) | **FI:** UCSX-S9108-100G (Integrated Fabric Manager)<br>**IOM:** N/A (Direct connectivity) | Cannot downgrade infrastructure below 4.3(4b). X-Series compute nodes only |
| **4.3(5)** | 4.3(5), 4.3(4) | **FI:** UCSX-S9108-100G (Integrated Fabric Manager)<br>**IOM:** N/A (Direct connectivity) | Cannot downgrade infrastructure below 4.3(4b). X-Series compute nodes only |
| **4.3(4)** | 4.3(4) | **FI:** UCSX-S9108-100G (Integrated Fabric Manager)<br>**IOM:** N/A (Direct connectivity) | First version supporting UCS X-Series Direct. Cannot downgrade infrastructure below 4.3(4b). X-Series compute nodes only |

---

## Hardware Specifications

### Fabric Interconnects

#### UCS 6200 Series (End of Support)
- **Models:** 6248 (48-port), 6296 (96-port)
- **Port Types:** 10GbE SFP+, 1GbE
- **Compatible IOMs:** 2204, 2208
- **Status:** Legacy platform, not compatible with M6 generation servers

#### UCS 6300 Series
- **Models:** 6332 (32-port), 6332-16UP (16-port unified)
- **Port Types:** 40GbE QSFP+
- **Compatible IOMs:** 2204, 2208, 2304, 2304V2
- **Infrastructure Versions:** 4.0(x) through 4.3(6)

#### UCS 6324 Fabric Interconnect (Mini)
- **Configuration:** Integrated into UCS 5108 chassis
- **Uplink Ports:** Four 40GbE QSFP+
- **Compatible IOMs:** 2204, 2208
- **Deployment:** Single chassis only
- **Infrastructure Versions:** 4.0(x) through 4.3(6)

#### UCS 6400 Series
- **Models:** 6454 (54-port), 64108 (108-port)
- **Port Types:** 10/25GbE SFP28, 40/100GbE QSFP28
- **Compatible IOMs:** 2204, 2208, 2408
- **Infrastructure Versions:** 4.0(x) through 4.3(6)

#### UCS 6536 Fabric Interconnect
- **Ports:** 36 x 100/400GbE QSFP-DD
- **Compatible IOMs:** 2204, 2208, 2304, 2304V2, 2408
- **Minimum Infrastructure:** 4.2(3)
- **Note:** First 400GbE capable fabric interconnect

#### UCSX-S9108-100G (X-Series Direct)
- **Configuration:** Integrated fabric manager in X9508 chassis
- **Ports:** Eight 100GbE QSFP28
- **Minimum Infrastructure:** 4.3(4)
- **Note:** X-Series compute nodes only

---

### I/O Modules (IOMs / Fabric Extenders)

#### UCS-IOM-2204
- **Generation:** 2nd generation
- **Ports:** Eight 10GbE SFP+ uplink ports
- **Server Connectivity:** 4 x 10GbE per half-width blade
- **Total Bandwidth:** 80 Gbps
- **Compatible FIs:** 6200, 6300, 6324, 6400, 6536

#### UCS-IOM-2208
- **Generation:** 2nd generation
- **Ports:** Eight 10GbE SFP+ uplink ports
- **Server Connectivity:** 4 x 10GbE per half-width blade
- **Total Bandwidth:** 80 Gbps
- **Compatible FIs:** 6200, 6300, 6324, 6400, 6536

#### UCS-IOM-2304
- **Generation:** 3rd generation
- **Ports:** Four 40GbE QSFP+ uplink ports
- **Server Connectivity:** 1 x 40GbE per half-width blade (2 x 40GbE with port expander)
- **Total Bandwidth:** 160 Gbps
- **Compatible FIs:** 6300, 6536 only
- **Notes:** Cannot mix with 2304V2 in same chassis

#### UCS-IOM-2304V2
- **Generation:** 3rd generation (Version 2)
- **Ports:** Four 40GbE QSFP+ uplink ports
- **Server Connectivity:** 1 x 40GbE per half-width blade (2 x 40GbE with port expander)
- **Total Bandwidth:** 160 Gbps
- **Compatible FIs:** 6300, 6536 only
- **Minimum Infrastructure:** 4.0(4)
- **Notes:** Cannot mix with 2304 in same chassis

#### UCS-IOM-2408
- **Generation:** 4th generation
- **Ports:** Eight 25GbE SFP28 uplink ports
- **Server Connectivity:** 4 x 10GbE per half-width blade (4 x 40GbE with port expander)
- **Total Bandwidth:** 200 Gbps
- **Compatible FIs:** 6400, 6536 only

---

## Important Compatibility Rules

### Cross-Version Firmware Guidelines

1. **Infrastructure First:** Always upgrade Infrastructure (A Bundle) before upgrading Server Firmware (B/C Bundle)

2. **Configuration Compatibility:** Verify all UCS domain configurations are supported by firmware versions on server endpoints

3. **IOM Compatibility:**
   - Cannot mix IOM-2304 and IOM-2304V2 in same chassis
   - IOM-2304V2 requires minimum UCSM 4.0(4)
   - IOM-2408 requires FI 6400 or 6536
   - IOM-2304/2304V2 requires FI 6300 or 6536

4. **UCS 6536 Requirements:**
   - Minimum infrastructure: 4.2(3)
   - Supports all IOM types (2204, 2208, 2304, 2304V2, 2408)

5. **X-Series Direct:**
   - UCSX-S9108-100G supports X-Series compute nodes only
   - Cannot downgrade infrastructure below 4.3(4b)

6. **Mixed Generation Support:**
   - Different server generations can run different firmware versions
   - All servers must be supported by infrastructure firmware version

---

## Upgrade Paths

### From 4.0(x) to 4.3(6)
- ✓ Supported on FI 6200, 6300, 6324, 6400
- ✓ Server bundles 4.0(x) remain compatible

### From 4.1(x) to 4.3(6)
- ✓ Supported on FI 6200, 6300, 6324, 6400
- ✓ Server bundles 4.1(x) remain compatible

### From 4.2(x) to 4.3(6)
- ✓ Supported on all FI models including 6536
- ✓ All server bundles remain compatible

---

## Bundle Definitions

### A Bundle (Infrastructure)
- Cisco UCS Manager
- Cisco NX-OS firmware
- IOM firmware
- FEX firmware

### B Bundle (Server Firmware - Blade Servers)
- Server BIOS
- Cisco IMC firmware
- Adapter firmware
- Adapter drivers

### C Bundle (Server Firmware - Rack Servers)
- Server BIOS
- Cisco IMC firmware
- Adapter firmware
- Adapter drivers

---

---

## Summary

### Document Sources

This report was compiled from the following official Cisco documentation:

1. **Primary Source:** [Cisco UCS Manager Cross-Version Firmware Support, Release 4.3](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/release/notes/b_cross-version-fw-support_4_3.html)
   - Main compatibility matrix for mixed A, B, and C bundle versions
   - Platform support tables (Tables 1-4)
   - Hardware compatibility guidelines

2. **Supporting Documentation:**
   - [Release Notes for Cisco UCS Manager, Release 4.3](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/release/notes/b_release-notes-ucsm-4_3.html)
   - [Cisco UCS Equivalency Matrix](https://www.cisco.com/c/dam/en/us/td/docs/unified_computing/ucs/c/sw/UCS-Equivalency-Matrix/index.html)
   - [UCS Hardware and Software Interoperability Matrix](https://ucshcltool.cloudapps.cisco.com/public/)

### Important Notes and Caveats

#### Critical Cross-Version Firmware Guidelines

1. **Upgrade Sequence:**
   - ⚠️ **ALWAYS upgrade Infrastructure (A Bundle) BEFORE Server Firmware (B/C Bundle)**
   - Failure to follow this sequence may result in compatibility issues or service disruption

2. **Configuration Validation:**
   - Verify ALL UCS domain configurations are supported by firmware versions on server endpoints
   - Check that features enabled in UCS Manager are compatible with older server firmware versions
   - Review release notes for any deprecated features or configuration limitations

3. **IOM Mixing Restrictions:**
   - ⚠️ **CRITICAL:** Cannot mix IOM-2304 and IOM-2304V2 in the same chassis
   - Attempting to mix these IOMs will result in configuration errors
   - IOM-2304V2 requires minimum UCSM 4.0(4) infrastructure

4. **Fabric Interconnect Limitations:**
   - **FI-6536:** Minimum infrastructure version 4.2(3) required
   - **FI-6200:** End of support - not compatible with M6 generation servers or newer firmware
   - **FI-6324 (Mini):** Limited to single chassis deployments only

5. **IOM to FI Dependencies:**
   - **IOM-2408:** ONLY supported with FI 6400 or FI 6536 series
   - **IOM-2304/2304V2:** ONLY supported with FI 6300 or FI 6536 series
   - **IOM-2204/2208:** Universal support across all FI models

6. **X-Series Specific Restrictions:**
   - UCS X-Series Direct (UCSX-S9108-100G) supports X-Series compute nodes ONLY
   - ⚠️ Cannot downgrade infrastructure below 4.3(4b) once upgraded
   - X210c M8 compute nodes cannot downgrade below 4.3(6a)

7. **Backward Compatibility:**
   - Infrastructure version 4.3(6) maintains backward compatibility with server bundles back to 4.1(1)
   - Infrastructure version 4.2(3) maintains backward compatibility with server bundles back to 4.0(1)
   - Server bundle 4.0(x) versions NOT supported with infrastructure 4.3(x) on FI-6536

8. **Platform Transition Considerations:**
   - When migrating from FI-6200 to newer platforms, plan for infrastructure and server firmware upgrades
   - M6 servers require minimum infrastructure 4.2(1)
   - Verify VIC adapter compatibility when upgrading to newer IOM models

9. **Testing and Validation:**
   - Test cross-version firmware combinations in non-production environments first
   - Validate all service profiles and policies after infrastructure upgrades
   - Monitor system health metrics during and after firmware updates

10. **Support and Documentation:**
    - Always consult the latest release notes before upgrading
    - Use the UCS Hardware Compatibility Tool to verify specific hardware/firmware combinations
    - Review the Cisco UCS Equivalency Matrix for component version mappings

### Version Coverage

This report covers firmware versions from **4.2(2)** through **4.3(6)**, representing the current supported cross-version firmware matrix for UCS Manager 4.3. Older versions (4.0(x) and 4.1(x)) are included in backward compatibility references but are not the primary focus of this document.

---

## References

- **Official Documentation:** [Cisco UCS Manager Cross-Version Firmware Support, Release 4.3](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/release/notes/b_cross-version-fw-support_4_3.html)
- **Release Notes:** [Release Notes for Cisco UCS Manager, Release 4.3](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/release/notes/b_release-notes-ucsm-4_3.html)
- **Equivalency Matrix:** [Cisco UCS Equivalency Matrix](https://www.cisco.com/c/dam/en/us/td/docs/unified_computing/ucs/c/sw/UCS-Equivalency-Matrix/index.html)
- **Hardware Compatibility Tool:** [UCS Hardware and Software Interoperability Matrix](https://ucshcltool.cloudapps.cisco.com/public/)

---

**Document Version:** 1.1  
**Generated:** December 9, 2025  
**Based on:** Cisco UCS Manager Release 4.3(6)  
**Source Document:** Cisco UCS Manager Cross-Version Firmware Support, Release 4.3 (Updated September 23, 2025)
