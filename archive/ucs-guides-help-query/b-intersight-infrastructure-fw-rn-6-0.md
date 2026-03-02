# Documentation: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/6-0/b-intersight-infrastructure-fw-rn-6-0.html

*Fetched on: 2026-02-27 17:29:46*

---

## Page 1: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/6-0/b-intersight-infrastructure-fw-rn-6-0.html

![Clear Contents of Search](/etc/designs/cdc/fw/i/ic_clear_gray.png)


---

## Page 2: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/6-0/b-intersight-infrastructure-fw-rn-6-0.pdf


---

## Page 3: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/6-0/b-intersight-infrastructure-fw-rn-6-0/m-introduction.html

## Cisco Intersight Managed Mode Infrastructure Firmware, Release 6.0

Firmware upgrades in Intersight include server firmware upgrades and infrastructure firmware upgrades. Infrastructure firmware upgrades in Intersight Managed mode is supported on Cisco UCS Fabric Interconnects Series 6600, 6500, 6400, and Cisco UCS X-Series Direct Fabric Interconnects. To manage the Cisco UCS infrastructure firmware, see [Upgrading Fabric Interconnect Firmware in IMM](https://intersight.com/help/saas/resources/Upgrading_Fabric_Interconnect_Firmware_imm). This feature is available with a Cisco Intersight Essentials or Advanced license tier. 

In Intersight, infrastructure and server firmware upgrades can be done independently. That is, you do not need to upgrade infrastructure firmware to use the latest server firmware and vice versa. For more information on compatibility between infrastructure firmware and server firmware, see [Cross Version Firmware Support](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/6-0/b-intersight-infrastructure-fw-rn-6-0/m-compatibility.html). For more information on server firmware updates, see [Release Notes for Cisco Intersight Managed Mode Server Firmware](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/6-0/b-rn-cisco-intersight-managed-mode-server-firmware-release-6-0.html). 


---

## Page 4: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/6-0/b-intersight-infrastructure-fw-rn-6-0/m-new-hardware-features.html

## New Hardware Features in Infrastructure Firmware Release 6.0(1.260003) — None 


---

## Page 5: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/6-0/b-intersight-infrastructure-fw-rn-6-0/m-security-fixes.html

## Security Fixes in Release 6.0(1.260003) — None 


---

## Page 6: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/6-0/b-intersight-infrastructure-fw-rn-6-0/m-resolved-issues.html

## Resolved issues in Release 6.0(1.260003)

This section provides a brief description of the resolved issues.

Defect ID |  Description |  First Version Affected |  Resolved in Release  
---|---|---|---  
CSCws83445 |  On Cisco UCS 6664 Fabric Interconnects, certain unified ports failed to come up. This issue occurred on devices reporting a hardware changes bit value of 0x0 in the supervisor SPROM. Only ports 1/25, 1/28, 1/29, 1/36, 1/37, and 1/40 will be operational; all other ports might not link-up or encounter issues even when up and should be disabled until the device is upgraded to 6.0(1.260003) or later. This issue affects both Ethernet and Fibre Channel ports and is not resolved by RMA, as hardware replacement without a firmware update will not correct the problem.  |  6.0(2.250085) |  6.0(1.260003)


---

## Page 7: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/6-0/b-intersight-infrastructure-fw-rn-6-0/m-open-issues.html

## Open issues in Release 6.0(1.260003) — None 


---

## Page 8: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/6-0/b-intersight-infrastructure-fw-rn-6-0/m-compatibility.html

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

