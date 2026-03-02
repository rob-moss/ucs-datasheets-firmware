# Documentation: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/6-0/b-rn-cisco-intersight-managed-mode-server-firmware-release-6-0.html

*Fetched on: 2026-02-27 17:30:25*

---

## Page 1: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/6-0/b-rn-cisco-intersight-managed-mode-server-firmware-release-6-0.html

![Clear Contents of Search](/etc/designs/cdc/fw/i/ic_clear_gray.png)


---

## Page 2: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/6-0/b-rn-cisco-intersight-managed-mode-server-firmware-release-6-0.pdf


---

## Page 3: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/6-0/b-rn-cisco-intersight-managed-mode-server-firmware-release-6-0/m-introduction.html

## Cisco Intersight Managed Mode Server Firmware, Release 6.0

Cisco Intersight Managed Mode server firmware updates are released to provide updated versions of BIOS, CIMC, adapters, and other server components for supported Cisco UCS servers and Cisco Unified Edge servers managed through Intersight. To manage the server firmware, Cisco UCS server firmware, see [Managing Firmware in Intersight Managed Mode](https://intersight.com/help/saas/resources#managing_firmware_in_intersight_managed_mode) and Upgrading Firmware for Unified Edge Compute Nodes. This feature is available with a Cisco Intersight Essentials or Advanced license tier. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

This document covers known issues and limitations related to these IMM servers only.

* * *  
  
---|---  
  
Supported servers managed through Intersight are:

  * Intersight Managed Mode (IMM) servers:

These include:

  * Cisco UCS XE-Series Unified Edge servers connected to Intersight through Edge Chassis Management Controllers (eCMC).

  * Cisco UCS X-Series, B-Series, and C-Series servers connected to Intersight through Cisco UCS Fabric Interconnects (FI).

  * Intersight Standalone Mode servers:

These include Cisco UCS C-Series and S-Series rack servers without Fabric Interconnect attachment, managed by Cisco Integrated Management Controller (CIMC). For known issues and limitations related to ISM servers, see [Cisco IMC Release Notes](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c-series-integrated-management-controller/products-release-notes-list.html). 

  * UCS Manager (UCSM) Managed Mode (UMM) servers:

These include Cisco UCS B-Series, C-Series, X-Series, S-Series, and HX-Series servers, which are attached to Fabric Interconnects (FIs), and managed through UCS Manager. 

For known issues and limitations related to UMM servers, see [Cisco UCS Manager Release Notes](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-release-notes-list.html). 

  * Cisco UCS C885A M8 Rack server:

For known issues and limitations related to Cisco UCS C885A M8 Rack server, see [Cisco Baseboard Management Controller Release Notes for Cisco UCS C885A M8 Rack Server](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/release/notes/Cisco-BMC-Release-Notes/1-1-0/b_cisco-openbmc-release-notes-1_1.html). 

  * Cisco UCS C845A M8 Rack server:

For known issues and limitations related to Cisco UCS C845A M8 Rack server, see [Cisco Baseboard Management Controller 2.0 Release Notes, Release 2.0](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/release/notes/Cisco-BMC-Release-Notes/2-0-1/b_cisco-bmc-2-0-release-notes.html). 


Firmware upgrades in Intersight include both server and infrastructure firmware updates, which can be updated independently. That is, you do not always need to upgrade the Fabric Interconnects or Unified Edge Chassis Management Controller (eCMC) infrastructure firmware to use the latest server firmware and vice versa. For more information on compatibility between infrastructure firmware and server firmware, see [Cross Version Firmware Support](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/6-0/b-rn-cisco-intersight-managed-mode-server-firmware-release-6-0/m-compatibility.html). For more information on infrastructure firmware updates, see [Release Notes for Cisco Intersight Managed Mode Infrastructure Firmware](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/6-0/b-intersight-infrastructure-fw-rn-6-0.html) and [Release Notes for Cisco Intersight Unified Edge eCMC Infrastructure Firmware](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/Avatar-infra/b-rn-cisco-intersight-unified-edge-Infra-firmware-release-6-0.html). 


---

## Page 4: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/6-0/b-rn-cisco-intersight-managed-mode-server-firmware-release-6-0/m-new-software-features.html

## New software features

Intersight software features may not align with the Intersight firmware release schedule. To know more about the latest software features, see the [What's New](https://intersight.com/help/saas/whats_new) section in Intersight Help Center. 


---

## Page 5: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/6-0/b-rn-cisco-intersight-managed-mode-server-firmware-release-6-0/m-new-hardware-features.html

## New Hardware in Cisco UCS XE-Series M8 Server Firmware Release, 6.0(1.260001) — None 


---

## Page 6: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/6-0/b-rn-cisco-intersight-managed-mode-server-firmware-release-6-0/m-security-fixes.html

## Security Fixes in Cisco UCS XE-Series M8 Server Firmware Release, 6.0(1.260001) — None 


---

## Page 7: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/6-0/b-rn-cisco-intersight-managed-mode-server-firmware-release-6-0/m-resolved-issues.html

## Resolved issues in Cisco UCS XE-Series M8 Server Firmware Release, 6.0(1.260001)

This section provides a brief description of the resolved issues.

Defect ID |  Description |  First Version Affected |  Resolved in Release  
---|---|---|---  
CSCws24234 |  On Cisco UCS XE130c M8 Compute Node, when the UCS-M2-HWRAID2 MINI STOR controller is missing but its carrier is installed, the system log is continuously flooded with `unable to read fru information `errors.  Upgrade the firmware to resolve this issue. If the same errors persist post-upgrade, physically verify that both the M.2 controller and its carrier are properly seated and installed.  |  6.0(1.251030) |  6.0(1.260001)  
CSCws22743 |  On Cisco UCS XE130c servers, L4/L40S GPUs may experience a link downgrade to x8 width and GEN 1 speed due to a race condition. This can reduce GPU performance and typically occurs when the link is downgraded or lane width is reduced.  To recover from a link downgrade, a workaround has been implemented to return the device to normal operation. |  6.0(2.250123) |  6.0(1.260001)


---

## Page 8: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/6-0/b-rn-cisco-intersight-managed-mode-server-firmware-release-6-0/m-open-issues.html

## Open Caveats in Cisco UCS XE-Series M8 Server Firmware Release, 6.0(1.260001) — None 


---

## Page 9: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/6-0/b-rn-cisco-intersight-managed-mode-server-firmware-release-6-0/m-known-issues.html

## Known issues in Cisco UCS XE-Series M8 Server Firmware Release, 6.0(1.260001) — None 


---

## Page 10: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/6-0/b-rn-cisco-intersight-managed-mode-server-firmware-release-6-0/m-compatibility.html

## Cross-Version Firmware Support  
  
XE-Series Server Firmware Version |  eCMC Infrastructure Firmware Version  
---|---  
6.0(1)  
6.0(1) |  Yes  
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

## Page 11: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/6-0/b-rn-cisco-intersight-managed-mode-server-firmware-release-6-0/m-related-resources.html

## Related resources  
  
  * [Release Notes and Release Bundles for Cisco Intersight](https://www.cisco.com/c/en/us/support/servers-unified-computing/intersight/products-release-notes-list.html)

  * [Cisco Baseboard Management Controller Release Notes for Cisco UCS C885A M8 Rack Server](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/release/notes/Cisco-BMC-Release-Notes/1-1-0/b_cisco-openbmc-release-notes-1_1.html)

  * [Release Notes for Cisco UCS Manager](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-release-notes-list.html)

  * [Release Notes for Cisco UCS Rack Server Software](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c-series-integrated-management-controller/products-release-notes-list.html)

  * [Cisco UCS Manager and Intersight Release Strategy](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/release/notes/b_ucsm-and-intersight-release-strategy-doc.html)

  * [Cisco UCS Equivalency Matrix for Cisco Intersight, Cisco IMC, and Cisco UCS Manager](https://www.cisco.com/c/dam/en/us/td/docs/unified_computing/ucs/c/sw/UCS-Equivalency-Matrix/index.html)

  * [Release Notes for Cisco Intersight Unified Edge eCMC Infrastructure Firmware Release, 6.0](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/Avatar-infra/b-rn-cisco-intersight-unified-edge-Infra-firmware-release-6-0.html)

  * [Release Notes and Release Bundles for Unified Edge](https://www.cisco.com/c/en/us/support/servers-unified-computing/intersight/products-release-notes-list.html)

  * [Managing Firmware in Unified Edge](/help/resources/fw_mgmnt_ue)


---

