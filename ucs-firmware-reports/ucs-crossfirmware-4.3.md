# UCS Manager 4.3 Cross-Version Firmware Compatibility Matrix

**Source:** Cisco UCS Manager Cross-Version Firmware Support, Release 4.3  
**Generated:** December 8, 2025  
**Last Updated:** September 23, 2025 (Cisco official documentation)

---

## UCS 6300/6400/6536 Series Fabric Interconnects

| Infrastructure Bundle | B and C Server Bundle Versions | Supported Fabric Interconnect + IOM | Supported UCS Server Models | Notes |
|----------------------|--------------------------------|-------------------------------------|----------------------------|--------|
| **4.3(6)** | 4.3(6), 4.3(5), 4.3(4), 4.3(3), 4.3(2), 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1) | **FI:** 6332, 6332-16UP, 6454, 64108, 6536<br>**IOM:** 2204, 2208, 2304, 2304V2, 2408 | B200 M4, B200 M5, B200 M6, B480 M5 | Full support for all M4, M5, and M6 generation servers. IOM-2408 requires FI 6400/6536. IOM-2304/2304V2 requires FI 6300/6536 |
| **4.3(5)** | 4.3(5), 4.3(4), 4.3(3), 4.3(2), 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1) | **FI:** 6332, 6332-16UP, 6454, 64108, 6536<br>**IOM:** 2204, 2208, 2304, 2304V2, 2408 | B200 M4, B200 M5, B200 M6, B480 M5 | Full support for all M4, M5, and M6 generation servers. IOM-2408 requires FI 6400/6536. IOM-2304/2304V2 requires FI 6300/6536 |
| **4.3(4)** | 4.3(4), 4.3(3), 4.3(2), 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1) | **FI:** 6332, 6332-16UP, 6454, 64108, 6536<br>**IOM:** 2204, 2208, 2304, 2304V2, 2408 | B200 M4, B200 M5, B200 M6, B480 M5 | Full support for all M4, M5, and M6 generation servers. IOM-2408 requires FI 6400/6536. IOM-2304/2304V2 requires FI 6300/6536 |
| **4.3(3)** | 4.3(3), 4.3(2), 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1) | **FI:** 6332, 6332-16UP, 6454, 64108, 6536<br>**IOM:** 2204, 2208, 2304, 2304V2, 2408 | B200 M4, B200 M5, B200 M6, B480 M5 | Full support for all M4, M5, and M6 generation servers. IOM-2408 requires FI 6400/6536. IOM-2304/2304V2 requires FI 6300/6536 |
| **4.3(2)** | 4.3(2), 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1) | **FI:** 6332, 6332-16UP, 6454, 64108, 6536<br>**IOM:** 2204, 2208, 2304, 2304V2, 2408 | B200 M4, B200 M5, B200 M6, B480 M5 | Full support for all M4, M5, and M6 generation servers. IOM-2408 requires FI 6400/6536. IOM-2304/2304V2 requires FI 6300/6536 |
| **4.2(3)** | 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1), 4.0(4), 4.0(2), 4.0(1) | **FI:** 6200, 6332, 6332-16UP, 6454, 64108, 6536<br>**IOM:** 2204, 2208, 2304, 2304V2, 2408 | B200 M4, B200 M5, B200 M6, B480 M5 | First version supporting FI-6536. Full backward compatibility with 4.0(x), 4.1(x), and 4.2(x) server bundles. IOM-2408 requires FI 6400/6536. IOM-2304/2304V2 requires FI 6300/6536. IOM-2204/2208 on FI-6200 |
| **4.2(2)** | 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1), 4.0(4), 4.0(2), 4.0(1) | **FI:** 6200, 6332, 6332-16UP, 6454, 64108<br>**IOM:** 2204, 2208, 2304, 2304V2, 2408 | B200 M4, B200 M5, B480 M5 | M6 servers NOT supported. FI-6536 NOT supported. IOM-2408 requires FI 6400. IOM-2304/2304V2 requires FI 6300. IOM-2204/2208 on all FI models |
| **4.2(1)** | 4.2(1), 4.1(3), 4.1(2), 4.1(1), 4.0(4), 4.0(2), 4.0(1) | **FI:** 6200, 6332, 6332-16UP, 6454, 64108<br>**IOM:** 2204, 2208, 2304, 2304V2, 2408 | B200 M4, B200 M5, B200 M6, B480 M5 | First infrastructure version supporting M6 servers. Minimum version required for B200 M6. FI-6536 NOT supported. IOM-2408 requires FI 6400. IOM-2304/2304V2 requires FI 6300 |

---

## UCS Mini (6324 Fabric Interconnect)

| Infrastructure Bundle | B and C Server Bundle Versions | Supported Fabric Interconnect + IOM | Supported UCS Server Models | Notes |
|----------------------|--------------------------------|-------------------------------------|----------------------------|--------|
| **4.3(6)** | 4.3(6), 4.3(5), 4.3(4), 4.3(3), 4.3(2), 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1) | **FI:** 6324 (Mini)<br>**IOM:** 2204, 2208 | B200 M4, B200 M5 | Single chassis deployment. Maximum 8 blade servers per chassis |
| **4.3(5)** | 4.3(5), 4.3(4), 4.3(3), 4.3(2), 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1) | **FI:** 6324 (Mini)<br>**IOM:** 2204, 2208 | B200 M4, B200 M5 | Single chassis deployment. Maximum 8 blade servers per chassis |
| **4.3(4)** | 4.3(4), 4.3(3), 4.3(2), 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1) | **FI:** 6324 (Mini)<br>**IOM:** 2204, 2208 | B200 M4, B200 M5 | Single chassis deployment. Maximum 8 blade servers per chassis |
| **4.3(3)** | 4.3(3), 4.3(2), 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1) | **FI:** 6324 (Mini)<br>**IOM:** 2204, 2208 | B200 M4, B200 M5 | Single chassis deployment. Maximum 8 blade servers per chassis |
| **4.3(2)** | 4.3(2), 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1) | **FI:** 6324 (Mini)<br>**IOM:** 2204, 2208 | B200 M4, B200 M5 | Single chassis deployment. Maximum 8 blade servers per chassis |
| **4.2(3)** | 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1), 4.0(4), 4.0(2), 4.0(1) | **FI:** 6324 (Mini)<br>**IOM:** 2204, 2208 | B200 M4, B200 M5 | Single chassis deployment. Maximum 8 blade servers per chassis. Full backward compatibility with 4.0(x) and 4.1(x) server bundles |
| **4.2(2)** | 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1), 4.0(4), 4.0(2), 4.0(1) | **FI:** 6324 (Mini)<br>**IOM:** 2204, 2208 | B200 M4, B200 M5 | Single chassis deployment. Maximum 8 blade servers per chassis |
| **4.2(1)** | 4.2(1), 4.1(3), 4.1(2), 4.1(1), 4.0(4), 4.0(2), 4.0(1) | **FI:** 6324 (Mini)<br>**IOM:** 2204, 2208 | B200 M4, B200 M5 | Single chassis deployment. Maximum 8 blade servers per chassis |

---

## UCS X-Series Direct (UCSX-S9108-100G)

| Infrastructure Bundle | B Server Bundle Versions | Supported Fabric Interconnect + IOM | Supported UCS Server Models | Notes |
|----------------------|--------------------------|-------------------------------------|----------------------------|--------|
| **4.3(6)** | 4.3(6), 4.3(5), 4.3(4) | **FI:** UCSX-S9108-100G (Integrated Fabric Manager)<br>**IOM:** N/A (Direct connectivity) | X210c M6, X210c M7, X210c M8 | X210c M8 requires minimum 4.3(6a). Cannot downgrade infrastructure below 4.3(4b). X-Series servers only |
| **4.3(5)** | 4.3(5), 4.3(4) | **FI:** UCSX-S9108-100G (Integrated Fabric Manager)<br>**IOM:** N/A (Direct connectivity) | X210c M6, X210c M7 | Cannot downgrade infrastructure below 4.3(4b). X-Series servers only |
| **4.3(4)** | 4.3(4) | **FI:** UCSX-S9108-100G (Integrated Fabric Manager)<br>**IOM:** N/A (Direct connectivity) | X210c M6, X210c M7 | First version supporting UCS X-Series Direct. Cannot downgrade infrastructure below 4.3(4b). X-Series servers only |

---

## Hardware Specifications

### Fabric Interconnects

#### UCS 6200 Series
- **Models:** 6248 (48-port), 6296 (96-port)
- **Port Types:** 10GbE SFP+, 1GbE
- **Compatible IOMs:** 2204, 2208
- **Status:** End of support, not compatible with M6 servers

#### UCS 6300 Series
- **Models:** 6332 (32-port), 6332-16UP (16-port unified)
- **Port Types:** 40GbE QSFP+
- **Compatible IOMs:** 2204, 2208, 2304, 2304V2
- **Server Support:** M4, M5, M6 generations

#### UCS 6324 Fabric Interconnect (Mini)
- **Configuration:** Integrated into UCS 5108 chassis
- **Uplink Ports:** Four 40GbE QSFP+
- **Compatible IOMs:** 2204, 2208
- **Deployment:** Single chassis only
- **Server Support:** M4, M5 generations

#### UCS 6400 Series
- **Models:** 6454 (54-port), 64108 (108-port)
- **Port Types:** 10/25GbE SFP28, 40/100GbE QSFP28
- **Compatible IOMs:** 2204, 2208, 2408
- **Server Support:** M4, M5, M6 generations

#### UCS 6536 Fabric Interconnect
- **Ports:** 36 x 100/400GbE QSFP-DD
- **Compatible IOMs:** 2204, 2208, 2304, 2304V2, 2408
- **Server Support:** M4 (VIC 1300 only), M5, M6 generations
- **Minimum Infrastructure:** 4.2(3)

#### UCSX-S9108-100G (X-Series Direct)
- **Configuration:** Integrated fabric manager in X9508 chassis
- **Ports:** Eight 100GbE QSFP28
- **Server Support:** X210c M6, M7, M8 compute nodes only
- **Minimum Infrastructure:** 4.3(4)

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
- **Notes:** M4/M5 servers require VIC 1300/1400 series adapters

### Blade Servers

#### B200 M4
- **CPU:** Intel Xeon E5-2600 v3/v4
- **Form Factor:** Half-width blade
- **Memory:** Up to 768GB DDR4
- **VIC Options:** 1227, 1240, 1340, 1380, 1387, 1455, 1457
- **Compatible FIs:** 6200, 6300, 6324, 6400, 6536 (VIC 1300 only)

#### B200 M5
- **CPU:** Intel Xeon Scalable 1st/2nd Gen
- **Form Factor:** Half-width blade
- **Memory:** Up to 3TB DDR4
- **VIC Options:** 1340, 1380, 1387, 1455, 1457
- **Compatible FIs:** 6200, 6300, 6324, 6400, 6536

#### B480 M5
- **CPU:** Intel Xeon Scalable 1st/2nd Gen
- **Form Factor:** Full-width blade (4 sockets)
- **Memory:** Up to 6TB DDR4
- **VIC Options:** 1340, 1380, 1387, 1455, 1457
- **Compatible FIs:** 6200, 6300, 6400, 6536

#### B200 M6
- **CPU:** Intel Xeon Scalable 3rd Gen
- **Form Factor:** Half-width blade
- **Memory:** Up to 4TB DDR4
- **VIC Options:** 1455, 1457, 15411, 15420, 15425
- **Compatible FIs:** 6300, 6324, 6400, 6536
- **Minimum Infrastructure:** 4.2(1)

### X-Series Compute Nodes

#### X210c M6
- **CPU:** Intel Xeon Scalable 3rd Gen
- **Form Factor:** Single-wide compute node
- **Chassis:** X9508 chassis
- **Fabric Manager:** UCSX-S9108-100G
- **Minimum Infrastructure:** 4.3(4)

#### X210c M7
- **CPU:** Intel Xeon Scalable 4th Gen
- **Form Factor:** Single-wide compute node
- **Chassis:** X9508 chassis
- **Fabric Manager:** UCSX-S9108-100G
- **Minimum Infrastructure:** 4.3(4)

#### X210c M8
- **CPU:** Intel Xeon Scalable 5th Gen
- **Form Factor:** Single-wide compute node
- **Chassis:** X9508 chassis
- **Fabric Manager:** UCSX-S9108-100G
- **Minimum Infrastructure:** 4.3(6a)

---

## Important Compatibility Rules

### Cross-Version Firmware Guidelines

1. **Infrastructure First:** Always upgrade Infrastructure (A Bundle) before upgrading Server Firmware (B/C Bundle)

2. **Configuration Compatibility:** Verify all UCS domain configurations are supported by firmware versions on server endpoints

3. **M6 Server Requirements:**
   - Minimum infrastructure: 4.2(1)
   - Not supported on FI-6200 series
   - Requires VIC 1400/15000 series adapters

4. **UCS 6536 Requirements:**
   - Minimum infrastructure: 4.2(3)
   - B200 M4 requires VIC 1300 series only
   - Supports all IOM types (2204, 2208, 2304, 2304V2, 2408)

5. **IOM Compatibility:**
   - Cannot mix IOM-2304 and IOM-2304V2 in same chassis
   - IOM-2304V2 requires minimum UCSM 4.0(4)
   - IOM-2408 requires FI 6400 or 6536
   - IOM-2408 with M4/M5 servers requires VIC 1300/1400 series

6. **X-Series Direct:**
   - UCSX-S9108-100G supports X-Series compute nodes only
   - Cannot downgrade infrastructure below 4.3(4b)
   - X210c M8 cannot downgrade below 4.3(6a)

7. **Mixed Generation Support:**
   - Can mix M4, M5, and M6 servers in same chassis (subject to IOM/FI compatibility)
   - Different server generations can run different firmware versions
   - All servers must be supported by infrastructure firmware version

### Upgrade Paths

**From 4.0(x) to 4.3(6):**
- ✓ Supported on FI 6200, 6300, 6324, 6400
- ✓ Server bundles 4.0(x) remain compatible
- ✓ Can add M6 servers after infrastructure upgrade

**From 4.1(x) to 4.3(6):**
- ✓ Supported on FI 6200, 6300, 6324, 6400
- ✓ Server bundles 4.1(x) remain compatible
- ✓ Can add M6 servers after infrastructure upgrade

**From 4.2(x) to 4.3(6):**
- ✓ Supported on all FI models including 6536
- ✓ All server bundles remain compatible
- ✓ M6 servers fully supported

---

## References

- **Official Documentation:** [Cisco UCS Manager Cross-Version Firmware Support, Release 4.3](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/release/notes/b_cross-version-fw-support_4_3.html)
- **Release Notes:** [Release Notes for Cisco UCS Manager, Release 4.3](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/release/notes/b_release-notes-ucsm-4_3.html)
- **Equivalency Matrix:** [Cisco UCS Equivalency Matrix](https://www.cisco.com/c/dam/en/us/td/docs/unified_computing/ucs/c/sw/UCS-Equivalency-Matrix/index.html)
- **Hardware Compatibility Tool:** [UCS Hardware and Software Interoperability Matrix](https://ucshcltool.cloudapps.cisco.com/public/)

---

**Document Version:** 1.0  
**Generated:** December 8, 2025  
**Based on:** Cisco UCS Manager Release 4.3(6)  
**Verified:** Against official Cisco documentation dated September 23, 2025
