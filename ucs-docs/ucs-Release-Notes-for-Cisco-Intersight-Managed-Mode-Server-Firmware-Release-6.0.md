# Release Notes for Cisco Intersight Managed Mode Server Firmware, Release 6.0

| | |
|---|---|
| **URL Title** | Release Notes for Cisco Intersight Managed Mode Server Firmware, Release 6.0 |
| **URL** | https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/6-0/b-rn-cisco-intersight-managed-mode-server-firmware-release-6-0.html |
| **Long URL** |  |
| **HTML Title** | Release Notes for Cisco Intersight Managed Mode Server Firmware, Release 6.0 |
| **Source file** | `ucs-docs-raw/html/b-rn-cisco-intersight-managed-mode-server-firmware-release-6-0.html` |
| **File type** | HTML |
| **Fetched on** | 2026-03-04 11:11:07 |

---

## Page 1: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/6-0/b-rn-cisco-intersight-managed-mode-server-firmware-release-6-0.html

![Clear Contents of Search](/etc/designs/cdc/fw/i/ic_clear_gray.png)

---

## Page 2: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/6-0/b-rn-cisco-intersight-managed-mode-server-firmware-release-6-0/m-introduction.html

## Overview

Firmware upgrades in Intersight include server firmware upgrades and infrastructure firmware upgrades. Infrastructure firmware upgrades in Intersight Managed mode is supported on Cisco Unified Edge Edge Chassis Management Controller (eCMC). To manage the eCMC infrastructure firmware, see [Upgrading Firmware for Unified Edge Chassis](https://intersight.com/help/saas/resources/fw_mgmnt_ue#upgrading_firmware_for_unified_edge_chassis). This feature is available with a Cisco Intersight Essentials or Advanced license tier. 

In Intersight, infrastructure and server firmware upgrades can be done independently. That is, you do not always need to upgrade infrastructure firmware to use the latest server firmware and vice versa. For more information on Unified Edge server firmware updates, see [Release Notes for Cisco Intersight Managed Mode Server Firmware](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/6-0/b-rn-cisco-intersight-managed-mode-server-firmware-release-6-0.html). 

---

## Page 3: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/6-0/b-rn-cisco-intersight-managed-mode-server-firmware-release-6-0/m-new-software-features.html

## New software features

Intersight software features may not align with the Intersight firmware release schedule. To know more about the latest software features, see the [What's New](https://intersight.com/help/saas/whats_new) section in Intersight Help Center. 

---

## Page 4: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/6-0/b-rn-cisco-intersight-managed-mode-server-firmware-release-6-0/m-new-hardware-features.html

## New Hardware Features in Infrastructure Firmware Release 6.0(1.251006) — None 

---

## Page 5: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/6-0/b-rn-cisco-intersight-managed-mode-server-firmware-release-6-0/m-security-fixes.html

## Security fixes in Release 6.0(1.251006) — None 

---

## Page 6: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/6-0/b-rn-cisco-intersight-managed-mode-server-firmware-release-6-0/m-resolved-issues.html

## Resolved issues in Release 6.0(1.251006)

This section provides a brief description of the resolved issues.

Defect ID |  Description |  First Version Affected |  Resolved in Release  
---|---|---|---  
CSCws30566 |  Unified Edge Chassis Management Controllers may experience unexpected reboots when the MTS watchdog heartbeat times out. This is caused by mismatched polling intervals between mtsmanager and mtswdwatcher, which can result in incorrect detection of a system reset and a **NetworkInterClusterLinkStateDown** alarm in Intersight.There is no workaround for this issue. Please contact Cisco TAC for support.  |  6.0(1.251005) |  6.0(1.251006)

---

## Page 7: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/6-0/b-rn-cisco-intersight-managed-mode-server-firmware-release-6-0/m-open-issues.html

## Open issues in Release 6.0(1.251006) — None 

---

## Page 8: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/6-0/b-rn-cisco-intersight-managed-mode-server-firmware-release-6-0/m-known-issues.html

## Known issues in Cisco UCS XE-Series M8 Server Firmware Release, 6.0(1.260001) — None 

---

## Page 9: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/6-0/b-rn-cisco-intersight-managed-mode-server-firmware-release-6-0/m-compatibility.html

## Cross-Version Firmware Support  
  
X-Series Server Firmware Version |  Infrastructure Firmware Version  
---|---  
4.1(3) |  4.2(1) |  4.2(2) |  4.2(3) |  4.3(2) |  4.3(3) |  4.3(4) |  4.3(5) |  4.3(6) |  6.0(1)  
6.0(1) |  N/A |  No |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.4(0) |  N/A |  No |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.3(0)  |  N/A |  No |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.2(2) |  N/A |  No |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.2(1) |  N/A |  No |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.2(0) |  N/A |  No |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.1(1) |  N/A |  No |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.1(0) |  N/A |  No |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.0(4) |  N/A |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.0(2) |  N/A |  Yes |  Yes |  Yes |  No |  No |  No |  No |  No |  No  
5.0(1) |  N/A |  Yes |  Yes |  Yes |  No |  No |  No |  No |  No |  No  
C-Series Server Firmware Version |  Infrastructure Firmware Version  
---|---  
4.1(3) |  4.2(1) |  4.2(2) |  4.2(3) |  4.3(2) |  4.3(3) |  4.3(4) |  4.3(5) |  4.3(6) |  6.0(1)  
6.0(1) |  No |  No |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
4.3(6) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
4.3(5)  |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
4.3(4) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
4.3(3) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
4.3(2) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
4.3(1) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
4.2(3) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
4.2(2) |  Yes |  Yes |  Yes |  Yes |  No |  No |  No |  No |  No |  No  
4.2(1) |  Yes |  Yes |  Yes |  Yes |  No |  No |  No |  No |  No |  No  
4.1(3) |  Yes |  Yes |  Yes |  Yes |  No |  No |  No |  No |  No |  No  
B-Series Server Firmware Version |  Infrastructure Firmware Version  
---|---  
4.1(3) |  4.2(1) |  4.2(2) |  4.2(3) |  4.3(2) |  4.3(3) |  4.3(4) |  4.3(5) |  4.3(6) |  6.0(1)  
6.0(1) |  No |  No |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.4(0) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.3(0)  |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.2(2) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.2(1) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.2(0) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.1(0) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
4.3(3) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
4.3(2) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
4.2(3) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
4.2(2) |  Yes |  Yes |  Yes |  Yes |  No |  No |  No |  No |  No |  No  
4.2(1) |  Yes |  Yes |  Yes |  Yes |  No |  No |  No |  No |  No |  No  
4.1(3) |  Yes |  Yes |  Yes |  Yes |  No |  No |  No |  No |  No |  No

---

## Page 10: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/6-0/b-rn-cisco-intersight-managed-mode-server-firmware-release-6-0/m-related-resources.html

## Related resources  
  
  * [Release Notes for Cisco Intersight Unified Edge Server Firmware, Release 6.0](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/6-0/b-rn-cisco-intersight-managed-mode-server-firmware-release-6-0.html)

  * [Release Notes for Cisco Intersight Unified Edge eCMC Infrastructure Firmware Release, 6.0](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/Avatar-infra/b-rn-cisco-intersight-unified-edge-Infra-firmware-release-6-0.html)

  * [Release Notes and Release Bundles for Unified Edge](https://www.cisco.com/c/en/us/support/servers-unified-computing/intersight/products-release-notes-list.html)

  * [Managing Firmware in Unified Edge](/help/resources/fw_mgmnt_ue)


---

## Page 11: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/6-0/m-resolved-issues.html

## Resolved issues in Release 6.0(1.251006)

This section provides a brief description of the resolved issues.

Defect ID |  Description |  First Version Affected |  Resolved in Release  
---|---|---|---  
CSCws30566 |  Unified Edge Chassis Management Controllers may experience unexpected reboots when the MTS watchdog heartbeat times out. This is caused by mismatched polling intervals between mtsmanager and mtswdwatcher, which can result in incorrect detection of a system reset and a **NetworkInterClusterLinkStateDown** alarm in Intersight.There is no workaround for this issue. Please contact Cisco TAC for support.  |  6.0(1.251005) |  6.0(1.251006)

---

## Page 12: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/6-0/m-new-hardware-features.html

## New Hardware Features in Infrastructure Firmware Release 6.0(1.251006) — None 

---

## Page 13: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/6-0/m-open-issues.html

## Open issues in Release 6.0(1.251006) — None 

---
