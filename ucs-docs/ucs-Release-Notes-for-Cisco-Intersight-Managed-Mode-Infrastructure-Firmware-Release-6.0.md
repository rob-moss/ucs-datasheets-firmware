# Release Notes for Cisco Intersight Managed Mode Infrastructure Firmware, Release 6.0

| | |
|---|---|
| **URL Title** | Release Notes for Cisco Intersight Managed Mode Infrastructure Firmware, Release 6.0 |
| **URL** | https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/6-0/b-intersight-infrastructure-fw-rn-6-0.html |
| **Long URL** |  |
| **HTML Title** | Release Notes for Cisco Intersight Managed Mode Infrastructure Firmware, Release 6.0 |
| **Source file** | `ucs-docs-raw/html/b-intersight-infrastructure-fw-rn-6-0.html` |
| **File type** | HTML |
| **Fetched on** | 2026-04-08 08:42:48 |

---

## Page 1: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/6-0/b-intersight-infrastructure-fw-rn-6-0.html

![Clear Contents of Search](/etc/designs/cdc/fw/i/ic_clear_gray.png)

---

## Page 2: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/6-0/b-intersight-infrastructure-fw-rn-6-0/m-introduction.html

## Cisco Intersight Managed Mode Infrastructure Firmware, Release 6.0

Firmware upgrades in Intersight include server firmware upgrades and infrastructure firmware upgrades. Infrastructure firmware upgrades in Intersight Managed mode is supported on Cisco UCS Fabric Interconnects Series 6600, 6500, 6400, and Cisco UCS X-Series Direct Fabric Interconnects. To manage the Cisco UCS infrastructure firmware, see [Upgrading Fabric Interconnect Firmware in IMM](https://intersight.com/help/saas/resources/Upgrading_Fabric_Interconnect_Firmware_imm). This feature is available with a Cisco Intersight Essentials or Advanced license tier. 

In Intersight, infrastructure and server firmware upgrades can be done independently. That is, you do not need to upgrade infrastructure firmware to use the latest server firmware and vice versa. For more information on compatibility between infrastructure firmware and server firmware, see [Cross Version Firmware Support](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/6-0/b-intersight-infrastructure-fw-rn-6-0/m-compatibility.html). For more information on server firmware updates, see [Release Notes for Cisco Intersight Managed Mode Server Firmware](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/6-0/b-rn-cisco-intersight-managed-mode-server-firmware-release-6-0.html). 

---

## Page 3: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/6-0/b-intersight-infrastructure-fw-rn-6-0/m-new-software-features.html

## New software features

Intersight software features may not align with the Intersight firmware release schedule. To know more about the latest software features, see the [What's New](https://intersight.com/help/saas/whats_new) section in Intersight Help Center. 

---

## Page 4: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/6-0/b-intersight-infrastructure-fw-rn-6-0/m-new-hardware-features.html

## New hardware features in Infrastructure Firmware Release 6.0(1.260006) — None 

---

## Page 5: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/6-0/b-intersight-infrastructure-fw-rn-6-0/m-security-fixes.html

## Security fixes in Release 6.0(1.260006) — None 

---

## Page 6: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/6-0/b-intersight-infrastructure-fw-rn-6-0/m-resolved-issues.html

## Resolved issues in Release 6.0(1.260006)

This section provides a brief description of the resolved issues.

Defect ID |  Description |  First Version Affected |  Resolved in Release  
---|---|---|---  
[CSCwt36346](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwt36346) |  On Cisco UCS 6500 Series and 6400 Series Fabric Interconnects, when the allowed VLAN string on the vEth interface exceeds 900 characters, data corruption occurs over time. This eventually causes both Fabric Interconnects to perform a hard reboot. The generic error message `Reset Requested due to Fatal Module Error` is displayed when the `show system reset-reason` command is run.  This issue is resolved. |  6.0(1.250198) |  6.0(1.260006) 6.0(2.260045)  
[CSCwn65484](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwn65484) |  Cisco UCS Fabric Interconnects (6400, 6500, 6600 Series, and Cisco UCS X-Series Direct UCS 9108 100G) may generate a missing FCOE_NPV_PKG license warning. The warning message is: %LICMGR-2-LOG_LIC_MISSING_WARNING.  Despite this warning, the FCoE feature continues to operate normally under honor-based licensing. This issue is resolved. |  4.3(3.240007) |  6.0(1.260006)

---

## Page 7: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/6-0/b-intersight-infrastructure-fw-rn-6-0/m-open-issues.html

## Open issues in Release 6.0(1.260006) — None 

---

## Page 8: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/6-0/b-intersight-infrastructure-fw-rn-6-0/m-known-issues.html

## Known issues in Release 6.0(1.260006) — None 

---

## Page 9: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/6-0/b-intersight-infrastructure-fw-rn-6-0/m-compatibility.html

## Cross-Version Firmware Support  
  
X-Series Server Firmware Version |  Infrastructure Firmware Version  
---|---  
4.1(3) |  4.2(1) |  4.2(2) |  4.2(3) |  4.3(2) |  4.3(3) |  4.3(4) |  4.3(5) |  4.3(6) |  6.0(1) |  6.0(2)  
6.0(2) |  N/A |  No |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
6.0(1) |  N/A |  No |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.4(0) |  N/A |  No |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.3(0)  |  N/A |  No |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.2(2) |  N/A |  No |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.2(1) |  N/A |  No |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.2(0) |  N/A |  No |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.1(1) |  N/A |  No |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.1(0) |  N/A |  No |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.0(4) |  N/A |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.0(2) |  N/A |  Yes |  Yes |  Yes |  No |  No |  No |  No |  No |  No |  No  
5.0(1) |  N/A |  Yes |  Yes |  Yes |  No |  No |  No |  No |  No |  No |  No  
C-Series Server Firmware Version |  Infrastructure Firmware Version  
---|---  
4.1(3) |  4.2(1) |  4.2(2) |  4.2(3) |  4.3(2) |  4.3(3) |  4.3(4) |  4.3(5) |  4.3(6) |  6.0(1) |  6.0(2)  
6.0(2) |  No |  No |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
6.0(1) |  No |  No |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
4.3(6) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
4.3(5)  |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
4.3(4) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
4.3(3) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
4.3(2) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
4.3(1) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
4.2(3) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
4.2(2) |  Yes |  Yes |  Yes |  Yes |  No |  No |  No |  No |  No |  No |  No  
4.2(1) |  Yes |  Yes |  Yes |  Yes |  No |  No |  No |  No |  No |  No |  No  
4.1(3) |  Yes |  Yes |  Yes |  Yes |  No |  No |  No |  No |  No |  No |  No  
B-Series Server Firmware Version |  Infrastructure Firmware Version  
---|---  
4.1(3) |  4.2(1) |  4.2(2) |  4.2(3) |  4.3(2) |  4.3(3) |  4.3(4) |  4.3(5) |  4.3(6) |  6.0(1) |  6.0(2)  
6.0(2) |  No |  No |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
6.0(1) |  No |  No |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.4(0) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.3(0)  |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.2(2) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.2(1) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.2(0) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.1(0) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
4.3(3) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
4.3(2) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
4.2(3) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
4.2(2) |  Yes |  Yes |  Yes |  Yes |  No |  No |  No |  No |  No |  No |  No  
4.2(1) |  Yes |  Yes |  Yes |  Yes |  No |  No |  No |  No |  No |  No |  No  
4.1(3) |  Yes |  Yes |  Yes |  Yes |  No |  No |  No |  No |  No |  No |  No

---

## Page 10: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/6-0/b-intersight-infrastructure-fw-rn-6-0/m-related-resources.html

## Related resources  
  
  * [Release Notes and Release Bundles for Cisco Intersight](https://www.cisco.com/c/en/us/support/servers-unified-computing/intersight/products-release-notes-list.html)

  * [Cisco UCS Equivalency Matrix for Cisco Intersight, Cisco IMC, and Cisco UCS Manager](https://www.cisco.com/c/dam/en/us/td/docs/unified_computing/ucs/c/sw/UCS-Equivalency-Matrix/index.html)

  * [Release Notes for Cisco UCS Manager](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-release-notes-list.html)

  * [Release Notes for Cisco UCS Rack Server Software](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c-series-integrated-management-controller/products-release-notes-list.html)

  * [Cisco Baseboard Management Controller Release Notes for Cisco UCS C885A M8 Rack Server](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/release/notes/Cisco-BMC-Release-Notes/1-1-0/b_cisco-openbmc-release-notes-1_1.html)

  * [Cisco UCS Manager and Intersight Release Strategy](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/release/notes/b_ucsm-and-intersight-release-strategy-doc.html)


---

## Page 11: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/6-0/m-resolved-issues.html

## Resolved issues in Release 6.0(1.260006)

This section provides a brief description of the resolved issues.

Defect ID |  Description |  First Version Affected |  Resolved in Release  
---|---|---|---  
[CSCwt36346](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwt36346) |  On Cisco UCS 6500 Series and 6400 Series Fabric Interconnects, when the allowed VLAN string on the vEth interface exceeds 900 characters, data corruption occurs over time. This eventually causes both Fabric Interconnects to perform a hard reboot. The generic error message `Reset Requested due to Fatal Module Error` is displayed when the `show system reset-reason` command is run.  This issue is resolved. |  6.0(1.250198) |  6.0(1.260006) 6.0(2.260045)  
[CSCwn65484](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwn65484) |  Cisco UCS Fabric Interconnects (6400, 6500, 6600 Series, and Cisco UCS X-Series Direct UCS 9108 100G) may generate a missing FCOE_NPV_PKG license warning. The warning message is: %LICMGR-2-LOG_LIC_MISSING_WARNING.  Despite this warning, the FCoE feature continues to operate normally under honor-based licensing. This issue is resolved. |  4.3(3.240007) |  6.0(1.260006)

---

## Page 12: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/6-0/m-new-hardware-features.html

## New hardware features in Infrastructure Firmware Release 6.0(1.260006) — None 

---

## Page 13: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/6-0/m-open-issues.html

## Open issues in Release 6.0(1.260006) — None 

---

## Page 14: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/6-0/m-known-issues.html

## Known issues in Release 6.0(1.260006) — None 

---

## Page 15: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/6-0/m-compatibility.html

## Cross-Version Firmware Support  
  
X-Series Server Firmware Version |  Infrastructure Firmware Version  
---|---  
4.1(3) |  4.2(1) |  4.2(2) |  4.2(3) |  4.3(2) |  4.3(3) |  4.3(4) |  4.3(5) |  4.3(6) |  6.0(1) |  6.0(2)  
6.0(2) |  N/A |  No |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
6.0(1) |  N/A |  No |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.4(0) |  N/A |  No |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.3(0)  |  N/A |  No |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.2(2) |  N/A |  No |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.2(1) |  N/A |  No |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.2(0) |  N/A |  No |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.1(1) |  N/A |  No |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.1(0) |  N/A |  No |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.0(4) |  N/A |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.0(2) |  N/A |  Yes |  Yes |  Yes |  No |  No |  No |  No |  No |  No |  No  
5.0(1) |  N/A |  Yes |  Yes |  Yes |  No |  No |  No |  No |  No |  No |  No  
C-Series Server Firmware Version |  Infrastructure Firmware Version  
---|---  
4.1(3) |  4.2(1) |  4.2(2) |  4.2(3) |  4.3(2) |  4.3(3) |  4.3(4) |  4.3(5) |  4.3(6) |  6.0(1) |  6.0(2)  
6.0(2) |  No |  No |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
6.0(1) |  No |  No |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
4.3(6) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
4.3(5)  |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
4.3(4) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
4.3(3) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
4.3(2) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
4.3(1) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
4.2(3) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
4.2(2) |  Yes |  Yes |  Yes |  Yes |  No |  No |  No |  No |  No |  No |  No  
4.2(1) |  Yes |  Yes |  Yes |  Yes |  No |  No |  No |  No |  No |  No |  No  
4.1(3) |  Yes |  Yes |  Yes |  Yes |  No |  No |  No |  No |  No |  No |  No  
B-Series Server Firmware Version |  Infrastructure Firmware Version  
---|---  
4.1(3) |  4.2(1) |  4.2(2) |  4.2(3) |  4.3(2) |  4.3(3) |  4.3(4) |  4.3(5) |  4.3(6) |  6.0(1) |  6.0(2)  
6.0(2) |  No |  No |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
6.0(1) |  No |  No |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.4(0) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.3(0)  |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.2(2) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.2(1) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.2(0) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
5.1(0) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
4.3(3) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
4.3(2) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
4.2(3) |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
4.2(2) |  Yes |  Yes |  Yes |  Yes |  No |  No |  No |  No |  No |  No |  No  
4.2(1) |  Yes |  Yes |  Yes |  Yes |  No |  No |  No |  No |  No |  No |  No  
4.1(3) |  Yes |  Yes |  Yes |  Yes |  No |  No |  No |  No |  No |  No |  No

---
