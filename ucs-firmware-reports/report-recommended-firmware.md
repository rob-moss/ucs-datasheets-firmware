# Firmware Recommendation Report for Cisco UCS Manager

**Generated:** December 10, 2025  
**Source:** Cisco UCS Manager Cross-Version Firmware Support, Release 4.3

---

## Overview

This report provides the recommended firmware versions for Cisco UCS Manager infrastructure and servers based on Cisco's official documentation. The recommendations are organized by infrastructure bundle versions and their compatible server bundle versions.

---

## Recommended Firmware Versions for Infrastructure

The recommended firmware versions for Cisco UCS Manager are:
- **6.0(1b)** - Latest release
- **4.3(6c)** - Recommended stable release
- **4.2(3o)** - Long-term stable release

---

## Recommended Firmware Versions for Cisco UCS Servers

### Blade Servers
The recommended firmware versions for Cisco UCS Blade Servers are:
- **6.0(1b)** - Latest release
- **4.3(6c)** - Recommended stable release
- **4.2(3o)** - Long-term stable release

### C-Series Rack Servers
The recommended firmware versions for Cisco UCS C-Series Rack Servers are:
- **6.0(1b)** - Latest release
- **4.3(6c)** - Recommended stable release
- **4.2(3o)** - Long-term stable release

---

## Infrastructure Firmware Recommendations

### Cross-Version Compatibility Matrix

The following matrix shows the recommended infrastructure bundle versions and their compatible B and C Server Bundle Versions:

| Recommended Version | Infrastructure Bundle | B and C Server Bundle Versions |
|---------------------|----------------------|--------------------------------|
| **4.3(6c)** | 4.3(6) | 4.3(6), 4.3(5), 4.3(4), 4.3(3), 4.3(2), 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1) |
| **4.2(3o)** | 4.2(3) | 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1), 4.0(4), 4.0(2), 4.0(1) |

**Note:** The recommended version (e.g., 4.3(6c)) maps to the main infrastructure version (e.g., 4.3(6)) for compatibility purposes.

---

## Server Bundle Versions by Server Model

Based on the server adapter driver matrix data, the following server bundle versions are available for Cisco UCS Blade Servers:

### B200 M4 Series
- **Models:** B200 M4 V3, B200 M4 V4
- **Server Firmware:** 4.2(2)
- **Supported ESXi Versions:** 6.7 U3, 7.0 U3

### B200 M5 Series
- **Models:** B200 M5 V1, B200 M5 V2
- **Server Firmware:** 4.2(2), 4.2(3)
- **Supported ESXi Versions:** 6.7 U3, 7.0 U3, 8.0 U3

### B200 M6 Series
- **Models:** B200 M6 V1
- **Server Firmware:** 4.2(2), 4.2(3)
- **Supported ESXi Versions:** 7.0 U3, 8.0 U3

### B480 M5 Series
- **Models:** B480 M5 V1
- **Server Firmware:** 4.2(2)
- **Supported ESXi Versions:** 7.0 U3

---

## Platform Support

### UCS 6300/6400/6536 Series Fabric Interconnects

#### Infrastructure Bundle 4.3(6)
- **Supported Fabric Interconnects:** 6332, 6332-16UP, 6454, 64108, 6536
- **Supported IOMs:** 2204, 2208, 2304, 2304V2, 2408
- **Compatible Server Bundles:** 4.3(6), 4.3(5), 4.3(4), 4.3(3), 4.3(2), 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1)

#### Infrastructure Bundle 4.2(3)
- **Supported Fabric Interconnects:** 6200, 6332, 6332-16UP, 6454, 64108, 6536
- **Supported IOMs:** 2204, 2208, 2304, 2304V2, 2408
- **Compatible Server Bundles:** 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1), 4.0(4), 4.0(2), 4.0(1)
- **Note:** First version supporting FI-6536

### UCS Mini (6324 Fabric Interconnect)

#### Infrastructure Bundle 4.3(6)
- **Supported Fabric Interconnects:** 6324 (Mini)
- **Supported IOMs:** 2204, 2208
- **Compatible Server Bundles:** 4.3(6), 4.3(5), 4.3(4), 4.3(3), 4.3(2), 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1)
- **Deployment:** Single chassis deployment, maximum 8 blade servers per chassis

#### Infrastructure Bundle 4.2(3)
- **Supported Fabric Interconnects:** 6324 (Mini)
- **Supported IOMs:** 2204, 2208
- **Compatible Server Bundles:** 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1), 4.0(4), 4.0(2), 4.0(1)
- **Note:** Full backward compatibility with 4.0(x) and 4.1(x) server bundles

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

5. **Mixed Generation Support:**
   - Different server generations can run different firmware versions
   - All servers must be supported by infrastructure firmware version

---

## Upgrade Recommendations

### Recommended Upgrade Path to 4.3(6c)

1. **Current Infrastructure:** Upgrade to 4.3(6) or higher
2. **Server Bundles:** Can remain on 4.1(x), 4.2(x), or upgrade to 4.3(x)
3. **Supported Platforms:** FI 6300/6400/6536 Series, UCS Mini (6324)

### Recommended Upgrade Path to 4.2(3o)

1. **Current Infrastructure:** Upgrade to 4.2(3) or higher
2. **Server Bundles:** Can remain on 4.0(x), 4.1(x), or upgrade to 4.2(x)
3. **Supported Platforms:** All FI models including 6200, 6300/6400/6536 Series, UCS Mini (6324)
4. **Note:** First version supporting FI-6536

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

## Additional Resources

For complete hardware compatibility information, please refer to:
- Cisco UCS Hardware Compatibility List (HCL)
- Cisco UCS Manager Cross-Version Firmware Support, Release 4.3
- Cisco UCS Manager Firmware Management Guide

---

**Document Version:** 1.0  
**Last Updated:** December 10, 2025
