# Release Notes for Cisco Intersight Managed Mode Server Firmware, Release 4.3, 5.2, 5.3, and 5.4

| | |
|---|---|
| **URL Title** | Release Notes for Cisco Intersight Managed Mode Server Firmware, Release 4.3, 5.2, 5.3, and 5.4 |
| **URL** | https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/4_3/b_intersight_server_fw_rn_4_3.html |
| **Long URL** |  |
| **HTML Title** | Release Notes for Cisco Intersight Managed Mode Server Firmware, Release 4.3, 5.2, 5.3, and 5.4 |
| **Source file** | `ucs-docs-raw/html/b_intersight_server_fw_rn_4_3.html` |
| **File type** | HTML |
| **Fetched on** | 2026-03-19 16:13:16 |

---

## Page 1: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/4_3/b_intersight_server_fw_rn_4_3.html

###   
  
**First Published: November 15, 2023**

**Last Updated: February 23, 2026**

# Overview

![](/c/dam/en/us/td/i/400001-500000/470001-480000/473001-474000/473341.jpg) ![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

In IMM Server Firmware bundles prior to the 5.2(0.230040) release, X-Series BIOS images had major versions of 5.0 and 5.1. Beginning with IMM Server Firmware 5.2(0.230040), the IMM and UCSM BIOS images will be common and numbered beginning with 4.3(2).  The resulting IMM BIOS Image major version sequence will follow 5.0 -> 5.1 -> 4.3 -> so on.

* * *  
  
---|---  
  
Cisco Intersight Managed Mode server firmware updates are released to provide updated versions of BIOS, CIMC, adapters, and other server components for supported Cisco UCS servers managed through Intersight. To manage the Cisco UCS server firmware, see [ _Managing Firmware in Intersight Managed Mode_ ](https://intersight.com/help/saas/resources#managing_firmware_in_intersight_managed_mode) _._ This feature is available with a Cisco Intersight Essentials or Advanced license tier. 

Supported Cisco UCS servers managed through Intersight are:

  * Intersight Managed Mode (IMM) servers:

These include Cisco UCS B-Series, C-Series, and X-Series servers connected to Intersight through Cisco UCS Fabric Interconnects.

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

This document covers known issues and limitations related to these IMM servers only. 

* * *  
  
---|---  
  * Intersight Standalone Mode servers:

These include Cisco UCS C-Series and S-Series rack servers without Fabric Interconnect attachment, managed by Cisco Integrated Management Controller (CIMC). For known issues and limitations related to ISM servers, see [Cisco IMC Release Notes](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c-series-integrated-management-controller/products-release-notes-list.html). 

  * UCS Manager (UCSM) Managed Mode (UMM) servers:

These include Cisco UCS B-Series, C-Series, X-Series, S-Series, and HX-Series servers, which are attached to Fabric Interconnects (FIs), and managed through UCS Manager. 

For known issues and limitations related to UMM servers, see [Cisco UCS Manager Release Notes](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-release-notes-list.html). 

  * Cisco UCS C885A M8 Rack server:

For known issues and limitations related to Cisco UCS C885A M8 Rack server, see [Cisco Baseboard Management Controller Release Notes for Cisco UCS C885A M8 Rack Server](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/release/notes/Cisco-BMC-Release-Notes/1-1-0/b_cisco-openbmc-release-notes-1_1.html). 

  * Cisco UCS C845A M8 Rack server:

For known issues and limitations related to Cisco UCS C845A M8 Rack server, see [Cisco Baseboard Management Controller 2.0 Release Notes, Release 2.0](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/release/notes/Cisco-BMC-Release-Notes/2-0-1/b_cisco-bmc-2-0-release-notes.html). 


Firmware upgrades in Intersight include both server and infrastructure firmware updates, which can be updated independently. That is, you do not need to upgrade infrastructure firmware to use the latest server firmware and vice versa. For more information on compatibility between infrastructure firmware and server firmware , see [Cross Version Firmware Support](https://cisco-compute.atlassian.net/wiki/spaces/DCG/pages/778010727/IMM+Maverick+Release+-+Release+Notes+for+Cisco+Intersight+Managed+Mode+Server+Firmware+Release+6.0#Cross-Version-Firmware-Support). For more information on infrastructure firmware updates, see [Release Notes for Cisco Intersight Managed Mode Infrastructure Firmware](https://www.cisco.com/c/en/us/support/servers-unified-computing/intersight/products-release-notes-list.html). 

## Firmware Version Equivalency Between Cisco Intersight, Cisco IMC, and Cisco UCS Manager

For more information, see [Cisco UCS Equivalency Matrix for Cisco Intersight, Cisco IMC, and Cisco UCS Manager](https://www.cisco.com/c/dam/en/us/td/docs/unified_computing/ucs/c/sw/UCS-Equivalency-Matrix/index.html). 

To view the complete matrix in PDF format, click [here](https://www.cisco.com/c/dam/en/us/td/docs/unified_computing/ucs/c/sw/UCS-Equivalency-Matrix/Equivalency_Matrix.pdf). 

### Latest Supported Firmware for End-of-Life Intersight Managed Mode Servers

Platform |  Supported Latest Firmware version  
---|---  
Cisco UCS C-Series M5 (C220, C240, C480) |  4.3(2.260007)  
Cisco UCS C-Series M6 (C220, C240) |  4.3(6.260017)  
Cisco UCS B-Series M5 (B200, B480) |  5.4(0.260011)  
Cisco UCS B-Series M6 (B200) |  5.4(0.260011)  
  
For more information, see [End-of-Life and End-of-Sale Notices for C-Series Servers](https://www.cisco.com/c/en/us/products/servers-unified-computing/ucs-c-series-rack-servers/eos-eol-notice-listing.html) and [End-of-Life and End-of-Sale Notices for B-Series Servers](https://www.cisco.com/c/en/us/products/servers-unified-computing/ucs-b-series-blade-servers/eos-eol-notice-listing.html). 

## Revision History

The following table includes the change history for this document.

Table 1. Release 4.3(6) Revision Date |  Description  
---|---  
February 23, 2026 |  Updated release notes for the following Server Firmware Release versions:

  * Cisco UCS X-Series M8 and M7 Server Firmware Release 5.4(0.260010)
  * Cisco UCS X-Series M6 Server Firmware Release 5.4(0.260009)
  * Cisco UCS C-Series M8, M7, and M6 Server Firmware Release 4.3(6.260017)
  * Cisco UCS B-Series M6 and M5 Server Firmware Release 5.4(0.260011)

This release includes updates to:

  * Resolved Caveats in Cisco UCS B-Series M5 5.4(0.260011) and C-Series M7, M6 Server Firmware Release 4.3(6.260017)

It does not include any new hardware support, security fixes, or open caveats.  
January 14, 2026 |  Updated release notes for the following Server Firmware Release versions:

  * Cisco UCS X-Series M7 Server Firmware Release 5.4(0.260001)
  * Cisco UCS C-Series M8 and M7 Server Firmware Release 4.3(6.260003)

This release includes updates to:

  * Resolved Caveats in Cisco UCS X-Series M7 5.4(0.260001) and C-Series M8, M7 Server Firmware Release 4.3(6.260003)

It does not include any new hardware support, security fixes, or open caveats.  
November 13, 2025 |  Updated release notes for Cisco UCS C-Series M7 Server Firmware Release 4.3(6.250117).  This release includes updates to:

  * Resolved Caveats in Cisco UCS C-Series M7 Server Firmware Release 4.3(6.250117)

It does not include any new hardware support, security fixes, or open caveats.  
October 28, 2025 |  Updated release notes for the following Server Firmware Release versions:

  * Cisco UCS X-Series M8 Server Firmware Release 5.4(0.250105)
  * Cisco UCS X-Series M8 and M7 Server Firmware Release 5.4(0.250106)
  * Cisco UCS X-Series M6 Server Firmware Release 5.4(0.250097)
  * Cisco UCS C-Series M8, M7, and M6 Server Firmware Release 4.3(6.250101)
  * Cisco UCS B-Series M6 and M5 Server Firmware Release 5.4(0.250090)

This release includes updates to:

  * Security Fixes in Cisco UCS C-Series M7 and M6 Server Firmware Release 4.3(6.250101)
  * Resolved Caveats in Cisco UCS X-Series M8 5.4(0.250105) and C-Series M6 4.3(6.250101) Server Firmware Release

It does not include any new hardware support or open caveats.  
August 25, 2025 |  Updated release notes for Cisco UCS C-Series M8 Server Firmware Release 4.3(6.250060).  This release includes updates to:

  * Resolved Caveats in Cisco UCS C-Series M8 Server Firmware Release 4.3(6.250060)

It does not include any new hardware support, security fixes, or open caveats.  
July 07, 2025 |  Updated release notes for the following Server Firmware Release versions:

  * Cisco UCS X-Series M8 Server Firmware Release 5.4(0.250052)
  * Cisco UCS X-Series M8 and M7 Server Firmware Release 5.4(0.250048)
  * Cisco UCS X-Series M6 Server Firmware Release 5.4(0.250047)
  * Cisco UCS C-Series M8, M7, and M6 Server Firmware Release 4.3(6.250053)
  * Cisco UCS B-Series M6 Server Firmware Release 5.4(0.250048)
  * Cisco UCS B-Series M5 Server Firmware Release 5.4(0.250047)

This release includes updates to:

  * Security Fixes in X-Series M6 5.4(0.250047), C-Series M6 4.3(6.250053), and B-Series M6 5.4(0.250048) Server Firmware Release
  * Security Fixes in X-Series M7 5.4(0.250048) and C-Series M7 4.3(6.250053) Server Firmware Release
  * Resolved Caveats in X-Series M8 5.4(0.250052) and C-Series M8 4.3(6.250053) Server Firmware Release
  * Open Caveats in X-Series M8 5.4(0.250052), M7 5.4(0.250048), M6 5.4(0.250047) and C-Series M8, M7, M6 4.3(6.250053) Server Firmware Release

It does not include any new hardware support.  
May 22, 2025 |  Updated release notes for the following Server Firmware Release versions:

  * Cisco UCS X210C M8 Server Firmware Release 5.4(0.250044)
  * Cisco UCS X215C M8, X410C M7, and X210C M7 Server Firmware Release 5.4(0.250040)
  * Cisco UCS C-Series M8 and M7 Server Firmware Release 4.3(6.250044)

This release includes updates to:

  * Resolved Caveats in C-Series M8 and M7 Server Firmware Release 4.3(6.250044)

It does not include any new hardware support, security fixes, or open caveats.  
April 30, 2025 |  Updated release notes for the following Server Firmware Release versions:

  * Cisco UCS X210c M8 Server Firmware Release 5.4(0.250037)
  * Cisco UCS X215c M8, X210c M7, and X410c M7 Server Firmware Release 5.4(0.250035)
  * Cisco UCS X210c M6 Server Firmware Release5.4(0.250033)
  * Cisco UCS C-Series M7 and M6 Server Firmware Release 4.3(6.250040)
  * Cisco UCS C225 M8 and C245 M8 Server Firmware Release 4.3(6.250040)
  * Cisco UCS C220 M8 and C240 M8 Server Firmware Release 4.3(6.250039)
  * Cisco UCS B-Series M6 and M5 Server Firmware Release 5.4(0.250034)

This release includes updates to:

  * New Hardware in X-Series M8 5.4(0.250037) and C-Series M8 Server4.3(6.250039) Firmware Release
  * Cross-Version Firmware Support
  * Security Fixes in B-Series M5 5.4(0.250034) Server Firmware Release
  * Resolved Caveats in C-Series M8 Firmware Release 4.3(6.250040) and 4.3(6.250039)
  * Resolved Caveats in X-Series M8 5.4(0.250037) and 5.4(0.250035), M7 5.4(0.250035), M6 5.4(0.250033) and B-Series M6, M5 5.4(0.250034) Server Firmware Release
  * Open Caveats in X-Series M8 5.4(0.250037) and C-Series M8 4.3(6.250040) and 4.3(6.250039), M7, M6 4.3(6.250040) Server Firmware Release
  * Known Behavior and Limitations

  
Table 2. Release 4.3(5) Revision Date |  Description  
---|---  
September 02, 2025 |  Updated release notes for Cisco UCS C-Series M8 Server Firmware Release 4.3(5.250045). 

  * Resolved Caveats in Cisco UCS C-Series M8 Server Firmware Release 4.3(5.250045)

It does not include any new hardware support, security fixes, or open caveats.  
July 07, 2025 |  Updated release notes for Cisco UCS C-Series M8 Server Firmware Release 4.3(5.250043).  This release includes updates to:

  * Resolved Caveats in C-Series M8 Server Firmware Release 4.3(5.250043)

It does not include any new hardware support, security fixes, or open caveats.  
June 05, 2025 |  Intersight Infrastructure Firmware versions 4.3(5.250012) and 4.3(5.250034) have been released. There is no corresponding Server Firmware release.   
May 19, 2025 |  Updated release notes for Cisco UCS C-Series M8, M7, and M6 Server Firmware Release 4.3(5.250033).  This release includes updates to:

  * Resolved Caveats in C-Series M8, M7, and M6 Server Firmware Release 4.3(5.250033)

It does not include any new hardware support, security fixes, or open caveats.  
April 10, 2025 |  Cisco UCS X-Series Direct FI Infrastructure Firmware version 4.3(5.250033) has been released.  There is no corresponding Server Firmware release.  
March 25, 2025 |  Updated release notes for Cisco UCS C-Series M8, M7, and M6 Server Firmware Release 4.3(5.250030) This release includes updates to:

  * Security Fixes in C-Series M8, M7, and M6 Server Firmware Release 4.3(5.250030)
  * Resolved Caveats in C-Series M8, M7, and M6 Server Firmware Release 4.3(5.250030)

It does not include any new hardware support or open caveats.  
March 05, 2025 |  Updated release notes for the following Server Firmware Release versions:

  * Cisco UCS X-Series M8, M7, and M6 Server Firmware Release 5.3(0.250021)
  * Cisco UCS B-Series M6 and M5 Server Firmware Release 5.3(0.250021)

This release includes updates to Resolved Caveats in X-Series M8, M7, M6 5.3(0.250021) and B-Series M6, M5 5.3(0.250021) Server Firmware Release.  It does not include any new hardware support, security fixes, or open caveats.  
January 20, 2025 |  Updated release notes for the following Server Firmware Release versions:

  * Cisco UCS X-Series M8, M7, and M6 Server Firmware Release 5.3(0.250001)
  * Cisco UCS B-Series M6 and M5 Server Firmware Release 5.3(0.250001)
  * Cisco UCS C-Series M8, M7, and M6 Server Firmware Release 4.3(5.250001)

This release includes updates to:

  * New Hardware in X-Series M8 5.3(0.250001) and C-Series M8 4.3(5.250001) Server Firmware Release
  * Resolved Caveats in X-Series M8, M7, M6 5.3(0.250001) and B-Series M6, M5 5.3(0.250001) Server Firmware Release
  * Resolved Caveats in C-Series M8, M7, and M6 4.3(5.250001) Server Firmware Release

It does not include any security fixes or open caveats.  
November 15, 2024 |  Added CSCwm06766 under Resolved Caveats in X-Series Firmware Release 5.3(0.240016).   
October 22, 2024 |  Updated release notes for the following Server Firmware Release versions:

  * Cisco UCS X-Series M8, M7, and M6 Server Firmware Release 5.3(0.240016)
  * Cisco UCS B-Series M6 and M5 Server Firmware Release 5.3(0.240014)
  * Cisco UCS C-Series M8, M7, and M6 Server Firmware Release 4.3(5.240021)

This release includes updates to:

  * New Hardware in X-Series and C-Series Server Firmware Release
  * Cross-Version Firmware Support
  * Security Fixes in X- Series 5.3(0.240016) and B-Series 5.3(0.240014) Server Firmware Release
  * Resolved Caveats in X-Series Firmware Release 5.3(0.240016)
  * Resolved Caveats in C-series Server Firmware Release 4.3(5.240021)
  * Open Caveats in C-Series Server Firmware Release 4.3(5.240021)
  * Open Caveats in X-Series Server Firmware Release 5.3(0.240016)

  
Table 3. Release 4.3(4) Revision Date |  Description  
---|---  
December 16, 2024 |  Updated release notes for the following Server Firmware Release versions:

  * Cisco UCS X-Series M7 5.2(2.240080) and M6 5.2(2.240078) Server Firmware Release 
  * Cisco UCS B-Series M6 and M5 Server Firmware Release 5.2(2.240080)
  * Cisco UCS C-Series M7 and M6 Server Firmware Release 4.3(4.242066)

This release includes updates to:

  * Resolved Caveats in X-Series M7 5.2(2.240080) and M6 5.2(2.240078) Server Firmware Release
  * Resolved Caveats in B-Series M6 and M5 Server Firmware Release 5.2(2.240080)
  * Resolved Caveats in C-series M7 and M6 Server Firmware Release 4.3(4.242066)

It does not include any new hardware support, security fixes, or open caveats.  
November 15, 2024 |  Added CSCwk62723 under Security Fixes in X-Series M7 5.2(2.240074), X-Series M6 5.2(2.240073), and B-series M6 5.2(2.240073) Firmware Release.   
October 10, 2024 |  Updated the following sections:

  * Resolved Caveats in X-series M7 Server Firmware Release 5.2(2.240074)
  * Resolved Caveats in C-Series M6 Server Firmware Release 4.3(4.242038)

  
October 03, 2024 |  Updated New Hardware in C-Series M7 Server Firmware Release 4.3(4.242038).   
September 26, 2024 |  Updated release notes for Cisco UCS C-Series M7 and M6 Server Firmware, Release 4.3(4.242038).  This release includes updates to:

  * Security Fixes in C-Series M6 Server Firmware Release 4.3(4.242038)
  * Resolved Caveats in C-Series M6 Firmware Release 4.3(4.242038)
  * Open Caveats in C-Series M6 Firmware Release 4.3(4.242038)

It does not include any new hardware support.  
September 03, 2024 |  Intersight Infrastructure Firmware version 4.3(4.240074) has been released.  Cisco UCS X-Series M7 5.2(2.240074), X-Series M6 5.2(2.240073), and B-series M6 5.2(2.240073) Server Firmware versions have been released. These server firmware versions do not include any new hardware support, security fixes, open caveats, or resolved caveats.   
August 20, 2024 |  Updated release notes for Cisco UCS C-Series M7 and M6 Server Firmware, Release 4.3(4.241063).  This release includes updates to:

  * Resolved Caveats in C-Series M7 and M6 Firmware Release 4.3(4.241063)
  * Security Fixes in C-Series M7 and M6 Server Firmware Release 4.3(4.241063)

It does not include any new hardware support or open caveats.  
July 25, 2024 |  Intersight Infrastructure Firmware version  4.3(4.240078) has been released. There is no corresponding Server Firmware release.   
June 25, 2024 |  Updated release notes for Cisco UCS C-Series M8 Server Firmware, Release 4.3(4.241014).  This release includes updates to New Hardware Features in C-Series M8 Server Firmware Release 4.3(4.241014).   
June 13, 2024 |  Updated [Resolved Caveats in X-Series M6 and M7 Firmware Release 5.2(2.240053)](https://www-author3.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/4_3/b_intersight_server_fw_rn_4_3.html#lbmr2).   
June 05, 2024 |  Updated release notes for the following Server Firmware Release versions:

  * Cisco UCS X-Series M7 and M6 Server Firmware, Release 5.2(2.240053)
  * Cisco UCS B-Series M6 and M5 Server Firmware, Release 5.2(2.240051)
  * Cisco UCS C-Series M7, M6, and M5 Server Firmware, Release 4.3(4.240152)

This release includes updates to [New Hardware Features in C-Series M6 and M7 servers](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/4_3/b_intersight_server_fw_rn_4_3.html#lbmr2_c-series), [New Hardware Features in B-Series M6 servers and X-Series M7 and M6 servers](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/4_3/b_intersight_server_fw_rn_4_3.html#lbmr2_x_b_series), [Open Caveats in X-Series M7 and M6 servers](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/4_3/b_intersight_server_fw_rn_4_3.html#lbmr2_x-series), and [Resolved Caveats in X-Series M7 and M6 servers](https://www-author3.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/4_3/b_intersight_server_fw_rn_4_3.html#lbmr2).   
Table 4. Release 4.3(3) Revision Date |  Description  
---|---  
April 24, 2024 |  Updated release notes for Cisco UCS C-Series M7 and M6 Server Firmware, Release 4.3(3.240043).  
February 15, 2024 |  Updated release notes for the following Server Firmware Release versions:

  * Cisco UCS X-Series M7 Server Firmware, Release 5.2(1.240010)
  * Cisco UCS X-Series M6 Server Firmware, Release 5.2(1.240010)
  * Cisco UCS B-Series M6 Server Firmware, Release 5.2(1.240010)
  * Cisco UCS C-Series M7 and M6 Server Firmware, Release 4.3(3.240022)

  
Table 5. Release 4.3(2) Revision Date |  Description  
---|---  
February 23, 2026 |  Updated release notes for Cisco UCS C-Series M5 Server Firmware Release 4.3(2.260007).  This release includes updates to:

  * Resolved Caveats in C-Series M5 Server Firmware Release 4.3(2.260007)

It does not include any new hardware support, security fixes, or open caveats.  
December 18, 2025 |  Updated release notes for Cisco UCS C-Series M5 Server Firmware Release 4.3(2.250063).  This release includes updates to:

  * Resolved Caveats in C-Series M5 Server Firmware Release 4.3(2.250063)

It does not include any new hardware support, security fixes, or open caveats.  
July 31, 2025 |  Updated release notes for Cisco UCS C-Series M5 Server Firmware Release 4.3(2.250045).  This release includes updates to:

  * Resolved Caveats in C-Series M5 Server Firmware Release 4.3(2.250045)

It does not include any new hardware support, security fixes, or open caveats.  
July 07, 2025 |  Updated release notes for Cisco UCS C-Series M5 Server Firmware Release 4.3(2.250037).  This release includes updates to:

  * Security Fixes in C-series M5 Server Firmware Release 4.3(2.250037)
  * Resolved Caveats in C-series M5 Server Firmware Release 4.3(2.250037)

It does not include any new hardware support or open caveats.  
April 17, 2025 |  Included CSCwh81377 to Resolved Caveats in C-Series Firmware Release 4.3(2.230270).   
March 18, 2025 |  Updated release notes for Cisco UCS C-series M5 Server Firmware Release 4.3(2.250021).  This release includes updates to Resolved Caveats in C-series M5 Server Firmware Release 4.3(2.250021).  It does not include any new hardware support, security fixes, or open caveats.  
March 11, 2025 |  Included CSCwn97854 to Open Caveats in C-series M5 Server Firmware Release 4.3(2.250016).   
February 28, 2025 |  Updated release notes for Cisco UCS C-series M5 Server Firmware Release 4.3(2.250016).  This release includes updates to:

  * Security Fixes in C-series M5 Server Firmware Release 4.3(2.250016)
  * Resolved Caveats in C-series M5 Server Firmware Release 4.3(2.250016)

It does not include any new hardware support or open caveats.  
December 09, 2024 |  Updated release notes for Cisco UCS C-series M5 Server Firmware Release 4.3(2.240107).  This release includes updates to Resolved Caveats in C-series M5 Server Firmware Release 4.3(2.240107).  It does not include any new hardware support, security fixes, or open caveats.  
October 08, 2024 |  Updated release notes for Cisco UCS C-Series M5 Server Firmware, Release 4.3(2.240090).  This release includes updates to:

  * Security Fixes in C-Series M5 Server Firmware Release 4.3(2.240090)
  * Resolved Caveats in C-Series M5 Server Firmware Release 4.3(2.240090)
  * Open Caveats in C-Series M5 Server Firmware Release 4.3(2.240090)

It does not include any new hardware support.  
August 13, 2024 |  C-Series M5 Server Firmware, Release 4.3(2.240077) has been release.  This release includes updates to:

  * Security Fixes in C-Series M5 Firmware Release 4.3(2.240077)
  * Resolved Caveats in C-Series M5 Firmware Release 4.3(2.240077)

It does not include any new hardware support or open caveats.  
June 03, 2024 |  C-Series Server Firmware version 4.3(2.240053) has been released. This release includes updates to [security fixes](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/4_3/b_intersight_server_fw_rn_4_3.html#lbmr1-patch4) and [resolved caveats](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/4_3/b_intersight_server_fw_rn_4_3.html#lbmr1_p5). It does not include any new hardware support or open caveats.   
May 22, 2024 |  C-Series Server Firmware version 4.3(2.240037) has been released. This release includes enhancements to Baseboard Management Controller (BMC) on Cisco UCS C225 M6 and C245 M6 servers. It does not include any new hardware support, security fixes, open caveats, or resolved caveats.   
April 17, 2024 |  Updated the Firmware Version Equivalency Between UCSM and IMM table to include UCS X-Series server version 5.1(1).  
Moved the following 4.3.1 release-specific sections from _Release Notes for Cisco Intersight Server Firmware 4.2, 5.0, and 5.1_ to [_Release Notes for Cisco Intersight Server Firmware 4.3 and 5.2_](https://www.cisco.com/c/en/us/support/servers-unified-computing/intersight/products-release-notes-list.html) (this document): 

  * New Hardware Support in C-Series Firmware 4.3(1.230097)
  * Resolved Caveats in C-Series M7 Firmware Release 4.3(1.230138)
  * Resolved Caveats in C-Series M7 Firmware Release 4.3(1.230124)

This is to consolidate the 4.3 release information.  
March 07, 2024 |  Updated release notes for Cisco UCS C-Series M7, M6, and M5 Server Firmware, Release 4.3(2.240009).  
January 24, 2024 |  Updated release notes for the following server firmware release versions:

  * Cisco UCS X-Series M7 Server Firmware, Release 5.2(0.230127)
  * Cisco UCS X-Series M6 Server Firmware, Release 5.2(0.230127)
  * Cisco UCS C-Series M5, M6, and M7 Server Firmware, Release 4.3(2.240002)
  * Cisco UCS B-Series M5 and M6 Server Firmware, Release 5.2(0.230127)

  
November 14, 2023 |  Updated release notes for the following server firmware release versions:

  * Cisco UCS X-Series M7 Server Firmware, Release 5.2(0.230092)
  * Cisco UCS X-Series M6 Server Firmware, Release 5.2(0.230092
  * Cisco UCS C-Series Server Firmware, Release 4.3(2.230270)
  * Cisco UCS B-Series Server Firmware, Release 5.2(0.230100)

  
September 12, 2023 |  Updated release notes for Cisco UCS X-Series 410c M7 Server Firmware, Release 5.2(0.230061).  
August 16, 2023 |  Created release notes for the following server firmware release versions: 

  * Cisco UCS X-Series M7 Server Firmware, Release 5.2(0.230041)
  * Cisco UCS X-Series M6 Server Firmware, Release 5.2(0.230040)
  * Cisco UCS C-Series Server Firmware, Release 4.3(2.230207)
  * Cisco UCS B-Series Server Firmware, Release 5.2(0.230039)

  
  
## New Software Support

Intersight software features may not align with the Intersight firmware release schedule. To know more about the latest software features, see the [What's New](https://intersight.com/help/saas/whats_new) section in Intersight Help Center. 

## New Hardware Features in Server Firmware Release

### New Hardware in X-Series M8, M7 5.4(0.260010), M6 5.4(0.260009), C-Series M8, M7, M6 4.3(6.260017), and B-Series M6, M5 5.4(0.260011) Server Firmware Release — None 

### New Hardware in C-Series M5 Server Firmware Release 4.3(2.260007) — None 

### New Hardware in Cisco UCS X-Series M7 5.4(0.260001) and C-Series M8, M7 4.3(6.260003) Server Firmware Release — None 

### New Hardware in C-Series M5 Server Firmware Release 4.3(2.250063) — None 

### New Hardware in Cisco UCS C-Series M7 Server Firmware Release 4.3(6.250117) — None 

### New Hardware in Cisco UCS X-Series M8 5.4(0.250105), 5.4(0.250106), M7 5.4(0.250106), M6 5.4(0.250097), C-Series M8, M7, M6 4.3(6.250101), and B-Series M6, M5 5.4(0.250090) Server Firmware Release — None 

### New Hardware in Cisco UCS C-Series M8 Server Firmware Release 4.3(5.250045) — None 

### New Hardware in Cisco UCS C-Series M8 Server Firmware Release 4.3(6.250060) — None 

### New Hardware in C-Series M5 Server Firmware Release 4.3(2.250045) — None 

### New Hardware in C-Series M8 Server Firmware Release 4.3(5.250043) — None 

### New Hardware in X-Series M8 5.4(0.250052), 5.4(0.250048), M7 5.4(0.250048), M6 5.4(0.250047), C-Series M8, M7, M6 4.3(6.250053), and B-Series M6 5.4(0.250048), M5 5.4(0.250047) Server Firmware Release — None 

### New Hardware in C-series M5 Server Firmware Release 4.3(2.250037) — None 

### New Hardware in X-Series M8 5.4(0.250040), 5.4(0.250044) and M7 5.4(0.250040), and C-Series 4.3(6.250044) Server Firmware Release — None 

### New Hardware in C-Series M8, M7, and M6 Server Firmware Release 4.3(5.250033) — None 

### New Hardware in X-Series M8 5.4(0.250037) and C-Series M8 Server4.3(6.250039) Firmware Release 

#### X-Series M8 5.4(0.250037) Server Firmware 

Cisco UCS X210c M8 Compute Node

The Cisco UCS X210c M8 Compute Node is the third generation of compute node to integrate into the Cisco UCS X-Series Modular System. It delivers performance, flexibility, and optimization for deployments in data centers, and at remote sites. This enterprise-class server offers market-leading performance, versatility, and density without compromise for workloads. Up to eight compute nodes can reside in the 7-Rack-Unit (7RU) Cisco UCS X9508 Chassis, offering one of the highest densities of compute, I/O, and storage per rack unit in the industry. 

The Cisco UCS X210c M8 Compute Node provides these main features:

  * CPU: Up to 2x Intel® Xeon® 6 Scalable Processors with up to 86 cores per processor and and up to 336MB of Level 3 cache per CPU. 

  * Memory: Up to 8TB with 32 x 256GB DDR5-6400 DIMMs, in a 2-socket configuration with Intel® Xeon® 6 Scalable Processors. 

  * Storage:

  * Up to nine hot-pluggable EDSFF E3.S NVMe drives with a new passthrough front mezzanin controller option new to the Cisco UCS X210c M8. 

  * Up to six hot-pluggable, solid-state rives (SSDs), or non-volatile memory express (NVMe) 2.5-inch drives with a choice of enterprise-class redundant array of independent disks (RAIDs) or passthrough controllers with four lanes each of PCIe Gen 5 connectivity. 

  * Up to two M.2 SATA drives or two M.2 NVMe drives for flexible boot and local storage capabilities.

  * Optional Front Mezzanine GPU module: The Cisco UCS Front Mezzanine GPU module GPU module is a passive PCIe Gen 4 front mezzanine option with support for up to two U.2 or U.3 NVMe drives and two HHHL GPUs. 

  * mLOM virtual interface cards:

  * Cisco UCS VIC (Virtual Interface Card) 15420 occupies the server's modular LAN on motherboard (mLOM) slot, enabling up to 50 Gbps (2x 25Gbps) of unified fabric connectivity to each of the chassis's intelligent fabric modules (IFMs) for 100 Gbps connectivity per server with secure boot technology. 

  * Cisco UCS VIC 15230 occupies the server's modular LAN on motherboard (mLOM) slot, enabling up to 100 Gbps of unified fabric connectivity to each of the chassis's intelligent fabric modules (IFMs) for 100 Gbps connectivity per server with secure boot technology. 

  * Optional Mezzanine card:

  * Cisco UCS VIC 15422, a 5th Gen virtual interface card, can occupy the server's mezzanine slot at the bottom rear of the chassis. This card's I/O connectors link to Cisco UCS X-Fabric technology. An included bridge card extends this VIC's 4x 25 Gbps of network connections through IFM connectors, bringing the total bandwidth to 100 Gbps per fabric (for a total of 200 Gbps per server). 

  * Cisco UCS PCI mezzanine card for Cisco UCS X-Fabric can occupy the server's mezzanine slot at the bottom rear of the chassis. This card's I/O connectors link to Cisco UCS X-Fabric modules and enable connectivity to the Cisco UCS X-Series PCIe Nodes. 

  * All VIC mezzanine cards also provide I/O connections from the Cisco UCS X210c Compute Node to the Cisco UCS X-Series PCIe Nodes. 

  * Security: The server supports an optional trusted platform module (TPM). Additional features include a secure boot FPGA and ACT2 anti-counterfeit provisions. 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCS X210c M8 Compute Node requires one of the following Cisco Intersight Infrastructure firmware versions: 

  * Cisco UCS 6400 and 6500 Series FI - 4.3(6.250048) or later. 
  * Cisco UCS X-Series Direct FI - 4.3(6.250094) or later. 


* * *  
  
---|---  
  
For complete list of supported peripherals for Cisco UCS X210c M8 Compute Node, see [Cisco UCS X210c M8 Compute Node Spec Sheet](https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-x-series-modular-system/x210cm8-specsheet.pdf). 

#### C-Series M8 4.3(6.250039) Server Firmware 

  * Cisco UCS C220 M8 Server

The 1RU, 2-socket Cisco UCS C220 M8 Rack Server is designed to meet the needs of customers that choose to deploy high density rack-mount servers. It combines the latest Intel® processors and is a versatile general-purpose application and infrastructure server delivering leading performance and efficiency for a wide range of workloads, including virtualization, collaboration, and bare-metal applications. 

The Cisco UCS C220 M8 Server extends the capabilities of the Cisco UCS rack server portfolio incorporating Intel Xeon® 6 CPUs. It improves security, performance, and efficiency while helping achieve sustainability goals with built-in accelerators such as Intel Trust Domain Extensions (TDX), Intel Data Streaming Accelerator (DSA), Intel QuickAssist Technology (QAT), Intel Advanced Matrix Extensions (AMX), and Intel In-Memory Analytics Accelerator (IAA). 

Operating Expenses (OpEx) for power and cooling, management, and maintenance can be decreased by consolidating older servers onto the latest generation of Cisco UCS C220 M8 Rack Servers. 

The Cisco UCS C220 M8 Server is a dense, fault-tolerant server that provides value, performance, and flexibility for both commercial and enterprise customers. 

The Cisco UCS C220 M8 Server offers the following:

  * CPU: Up to 2x Intel Xeon 6700P or 6500P processors (1 or 2) 

  * Memory:

  * 32 DIMM slots (16 DIMMS per CPU): 16, 32, 48, 64, 96, 128GB DDR5 at up to 6400 MT/s for up to 4TB of memory.

  * 32, 64GB MRDIMMs at up to 8000 MT/s.

  * PCIe expansion: Up to 3 PCIe 5.0 half-height slots or up to 2 PCIe 5.0 full-height slots plus 1 dedicated24-Gbps RAID controller slot and 1 dedicated mLOM/OCP 3.0 slot. 

  * RAID controllers:

  * Cisco® 24-Gbps modular tri-mode RAID controller supports SAS 4 or NVMe hardware RAID.

  * Cisco 24-Gbps modular tri-mode SAS Host Bus Adapter (HBA).

  * Internal storage:

  * Backplane options: 

  * Up to 10 SFF SAS/SATA/U.3 NVMe drives through SAS4 tri-mode RAID orHBA controller, with optional up to eight direct-attach U.2/U.3 NVMe drives. 

  * Up to 16 E3.S 1T direct-attach NVMe drives at PCIe Gen5 x4 each.

  * mLOM/OCP 3.0:

  * One dedicated PCIe Gen5x16 slot that can be used to add an mLOM or OCP 3.0 card for additional rear-panel connectivity.

  * mLOM slot can flexibly accommodate 10/25/50 and 40/100/200 Gbps Cisco VIC adapters.

  * OCP 3.0 slot features full out-of-band manageability that supports Intel X710 OCP dual 10GBase-T through mLOM interposer.

  * Power supplies: Hot-pluggable, redundant platinum, and titanium options: 

  * Platinum: 1050W DC and 1600W AC

  * Titanium: 1200W AC and 2300W AC

  * Other storage:

  * Dedicated Baseboard Management Controller (BMC) FlexMMC for utilities (on board).

  * Dual M.2 SATA SSDs (internal or hot-swappable) with HW RAID support.

  * GPU: Up to three single-wide GPUs supported. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

  * Cisco UCS C-Series M8 servers support only 15000 series secure boot adapters.
  * Cisco UCS C220 M8 server requires Cisco Intersight Infrastructure Firmware version 4.3(6.250048) or later. 

* * *  
  
---|---  
  
For complete list of supported peripherals for Cisco UCS C220 M8 Compute Node, see [Cisco UCS C220 M8 Compute Node Spec Sheet](https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/ucs-c220-m8-sff-rack-server.pdf). 

  * Cisco UCS C240 M8 Server

The 2RU, 2-socket Cisco UCS C240 M8 Rack Server offers I/O flexibility and larger storage capacity. It combines the fastest Intel® processors and is a versatile general-purpose application and infrastructure server delivering leading performance and efficiency for a wide range of workloads, including AI, big-data analytics, databases, collaboration, virtualization, and high-performance computing. 

The Cisco UCS C240 M8 Server extends the capabilities of the Cisco UCS rack server portfolio by incorporatingIntel Xeon® 6 CPUs. It improves security, performance, and efficiency while helping you achieve your sustainability goals with built-in accelerators such as Intel Trust Domain Extensions (TDX), Intel DataStreaming Accelerator (DSA), Intel QuickAssist Technology (QAT), Intel Advanced Matrix Extensions(AMX), and Intel In-Memory Analytics Accelerator (IAA). 

You are able to decrease server Operating Expenses (OpEx) for power and cooling, management, and maintenance by consolidating older servers onto the latest generation of Cisco UCS C240 M8 Server. 

The Cisco UCS C240 M8 Server offers the following:

  * CPU: Up to 2x Intel Xeon 6700P or 6500P processors (1 or 2). 

  * Memory:

  * 32 DIMM slots (16 DIMMS per CPU): 16, 32, 48, 64, 96, 128, 256GB DDR5 at up to 6400 MT/sfor up to 8TB of memory.

  * 32, 64GB MRDIMMs at up to 8000 MT/s.

  * PCIe expansion: Up to 8 PCIe 5.0 slots plus 1 dedicated 24-Gbps RAID controller slot and 1 dedicated mLOM/OCP 3.0 slot 

  * RAID controllers:

  * Cisco 24-Gbps modular tri-mode RAID controller supports SAS 4 or NVMe hardware RAID.

  * Cisco 24-Gbps modular tri-mode SAS Host Bus Adapter (HBA).

  * Internal storage:

  * Backplane options: Up to 28 SFF SAS/SATA/U.3 NVMe drives through SAS4 tri-mode RAID orHBA controller, with optional up to eight direct-attach U.2/U.3 NVMe drives. 

  * Up to 36 E3.S 1T direct-attach NVMe drives.

  * Up to 16 LFF SAS HDDs plus optional 4 rear SFF HDD/SSDs.

  * mLOM/OCP 3.0: One dedicated PCIe Gen5x16 slot that can be used to add an mLOM or OCP 3.0 card for additional rear-panel connectivity. 

  * mLOM slot can flexibly accommodate 10/25/50 and 40/100/200 Gbps Cisco VIC adapters.

  * OCP 3.0 slot features full out-of-band manageability that supports Intel X710 OCP Dual 10GBase-T via mLOM interposer.

  * Power supplies: Hot-pluggable, redundant platinum and titanium options: 

  * Platinum: 1050W DC and 1600W AC

  * Titanium: 1200W AC and 2300W AC

  * Other storage:

  * Dedicated Baseboard Management Controller (BMC) FlexMMC for utilities (on board).

  * Dual M.2 SATA SSDs (internal or hot-swappable) with HW RAID support.

  * GPU: Up to three double-wide or eight single-wide GPUs supported. 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

  * Cisco UCS C-Series M8 servers support only 15000 series secure boot adapters.
  * Cisco UCS C240 M8 server requires Cisco Intersight Infrastructure Firmware version 4.3(6.250048) or later. 


* * *  
  
---|---  
  
For complete list of supported peripherals for Cisco UCS C240 M8 Compute Node, see [Cisco UCS C240 M8 Compute Node Spec Sheet](https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/ucs-c240-m8-sff-rack-server.pdf). 

### New Hardware in C-Series M8, M7, and M6 Server Firmware Release 4.3(5.250030) — None 

### New Hardware in C-series M5 Server Firmware Release 4.3(2.250021) — None 

### New Hardware in X-Series M8 5.3(0.250001) and C-Series M8 4.3(5.250001) Server Firmware Release 

#### X-Series M8 5.3(0.250001) Server Firmware 

  * Support for the following 5th Generation AMD EPYC CPU on Cisco UCS X215c M8 Compute Node:

  * UCSX-CPU-A9655

  * UCSX-CPU-A9555

  * UCSX-CPU-A9355

  * UCSX-CPU-A9135

  * UCSX-CPU-A9575F

  * Support for UCSC-GPU-MI210 GPU on Cisco UCS X215c M8 Compute Node.

  * Support for the following DDR5-6400 MT/s DIMM for 5th Generation AMD EPYC™ CPU on Cisco UCS X215c M8 Compute Node:

  * UCS-MRX32G1RE5 

  * UCS-MRX64G2RE5 

  * Support for the following DDR5-5600 MT/s DIMM for 4th Generation AMD EPYC™ CPU on Cisco UCS X215c M8 Compute Node:

  * UCSX-MR128G2RG3


#### C-Series M8 4.3(5.250001) Server Firmware 

  * Support for the following 5th Generation AMD EPYC CPU on Cisco UCS C245 M8 servers:

  * UCS-CPU-A9655

  * UCS-CPU-A9555

  * UCS-CPU-A9355

  * UCS-CPU-A9135

  * UCS-CPU-A9575F

  * Support for the following 5th Generation AMD EPYC CPU on Cisco UCS C225 M8 servers:

  * UCS-CPU-A9655

  * UCS-CPU-A9555

  * UCS-CPU-A9355

  * UCS-CPU-A9135

  * UCS-CPU-A9575F

  * Support for the following Cisco Tri-Mode M1 24G RAID storage controllers on Cisco UCS C225 M8 and C245 M8 servers equipped with 4th and 5th Generation AMD EPYC Processors. 

  * UCSC-RAID-M1L16

  * UCSC-RAID-MP1L32

  * Support for UCSC-GPU-MI210 GPU on Cisco UCS C245 M8 server.

  * Support for the following DDR5-6400 MT/s DIMM for 5th Generation AMD EPYC™ CPU on Cisco UCS C225 M8 and C245 M8 servers:

  * UCS-MRX32G1RE5 

  * UCS-MRX64G2RE5 

  * Support for the following DDR5-6400 MT/s DIMM for 5th Generation AMD EPYC™ CPU on Cisco UCS C245 M8 servers:

  * UCS-MRX96G2RF5 

  * Support for the following DDR5-5600 MT/s DIMM for 4th Generation AMD EPYC™ CPU on Cisco UCS C225 M8 and C245 M8 servers:

  * UCS-MR128G2RG3


### New Hardware in X-Series M7 5.2(2.240080), M6 5.2(2.240078), B-Series M6, M5 5.2(2.240080), and C-series M7, M6 4.3(4.242066) Firmware Release — None 

### New Hardware in X-Series and C-Series Server Firmware Release

#### X-Series M8 5.3(0.240016) Server Firmware 

**Cisco UCS X215c M8 Compute Node**

The Cisco UCS X-Series Modular System simplifies your data center, adapting to the unpredictable needs of modern applications while also providing for traditional scale-out and enterprise workloads. It reduces the number of server types to maintain, thereby helping to improve operational efficiency and agility by minimizing complexity. Powered by the Cisco Intersight™ cloud operations platform, it shifts your thinking from administrative details to business outcomes with hybrid cloud infrastructure that is assembled from the cloud, shaped to your workloads, and continuously optimized. 

The Cisco UCS X215c M8 Compute Node is integrate into the Cisco UCS X-Series Modular System. Up to eight compute nodes can reside in the 7-Rack-Unit (7RU) Cisco UCS X9508 Chassis, offering one of the highest densities of compute, IO, and storage per rack unit in the industry. 

The Cisco UCS X215c M8 Compute Node offers the following:

  * CPU: Up to 2x 4th Generation AMD EPYC Processors with up to 128 cores per processors

  * Memory:

  * 24 DIMM slots (12 DIMMs per CPU socket), up to 4800 MT/s DDR5

  * Up to 6 TB of capacity

  * Storage: Up to 6 hot-pluggable, Solid-State Drives (SSDs), or Non-Volatile Memory Express (NVMe) 2.5-inch drives with a choice of enterprise-class Redundant Array of Independent Disks (RAID) or pass-through controllers with four lanes each of PCIe Gen 4 connectivity and up to 2 M.2 SATA or NVMe drives for flexible boot and local storage capabilities. 

  * Optional Front Mezzanine GPU module: The Cisco UCS Front Mezzanine GPU module is a passive PCIe Gen 4 front mezzanine option with support for up to two U.2 or U.3 NVMe drives and two HHHL GPUs. 

  * mLOM virtual interface cards:

  * Cisco UCS Virtual Interface Card (VIC) 15420 occupies the server's Modular LAN on Motherboard (mLOM) slot, enabling up to 50 Gbps (2 x25Gbps) of unified fabric connectivity to each of the chassis Intelligent Fabric Modules (IFMs) for 100Gbps connectivity per server. 

  * Cisco UCS Virtual Interface Card (VIC) 15230 occupies the server's modular LAN on motherboard (mLOM) slot, enabling up to 100 Gbps of unified fabric connectivity to each of the chassis Intelligent Fabric Modules (IFMs) for 100 Gbps connectivity per server with secure boot capability. 

  * Optional Mezzanine card:

  * Cisco UCS Virtual Interface Card (VIC) 15422 can occupy the server's mezzanine slot at the bottom rear of the chassis. An included bridge card extends this VIC's 100 Gbps (4 x 25Gbps) of network connections through IFM connectors, bringing the total bandwidth to 100 Gbps per VIC 15420 and 15422 (for a total of 200 Gbps per server). In addition to IFM connectivity, the VIC 15422 I/O connectors link to Cisco UCS X-Fabric technology. 

  * Cisco UCS PCI Mezz card for X-Fabric can occupy the server's mezzanine slot at the bottom rear of the chassis. This card's I/O connectors link to Cisco UCS X-Fabric modules and enable connectivity to the X440p PCIe Node. 

  * Security: Includes secure boot silicon root of trust FPGA, ACT2 anti-counterfeit provisions, and optional Trusted Platform Model (TPM). 


For complete list of supported peripherals for Cisco UCS X215c M8 Compute Node, see [Cisco UCS X215c M8 Compute Node Spec Sheet](https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-x-series-modular-system/ucs-x215c-m8-compute-node.pdf). 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCS X215c M8 Compute Node support only 14000 Series and 15000 Series secure boot VIC adapters.

* * *  
  
---|---  
  
#### X-Series M7 5.3(0.240016) Server Firmware 

**Added support for the following GPUs on the UCSX-210C-M7 Compute Node:**

  * UCSX-GPU-H100-NVL

  * UCSX-GPU-L4-MEZZ


#### C-Series M8 4.3(5.240021) Server Firmware 

  * **Cisco UCS C225 M8 Servers**

The Cisco UCS C225 M8 Servers is a versatile general-purpose infrastructure and application server. This high-density, 1RU, single-socket rack server delivers industry-leading performance and efficiency for a wide range of workloads, including virtualization, collaboration, and bare-metal applications. 

The Cisco UCS C225 M8 Servers extends the capabilities of the Cisco UCS rack server portfolio. It powers 4thGen AMD EPYC™ Processors with 100 percent more cores per socket designed using AMD’s chiplet architecture. With advanced features such as AMD Infinity Guard, compute-intensive applications will see significant performance improvements and reap other benefits such as power and cost efficiencies. 

You can deploy the Cisco UCS C225 M8 Servers as standalone servers or as part of the Cisco Unified Computing System™ managed by Cisco Intersight® or Cisco UCS Manager to take advantage of Cisco® standards-based unified computing innovations that can help reduce your Total Cost of Ownership (TCO) and increase your business agility. 

The C225 M8 rack server brings many new innovations to the Cisco UCS AMD rack server portfolio. With the introduction of PCIe Gen 5.0 for high-speed I/O, a DDR5 memory bus, and expanded storage capabilities, the server delivers significant performance and efficiency gains that will improve your application performance. 

The key features of Cisco UCS C225 M8 Servers include:

  * Supports one 4thGen AMD EPYC CPU, with up to 128 cores per socket

  * Up to 12 DDR5 DIMMs for up to 1.5 TB of capacity using 128 GB DIMMs

  * Up to 4800 MT/s DDR5 memory

  * Up to 3 PCIe 4.0 slots or up to 2 PCIe 5.0 slots, plus a modular LAN on motherboard (mLOM) / OCP slot 3.0

  * Support for Cisco UCS VIC 15000 Series adapters as well as a host of third-party NIC options

  * UCS C225 M8S chassis: up to 10 SAS/SATA or NVMe disk drives

  * New tri-mode RAID controller supports SAS4 or NVMe hardware RAID

  * Up to 4 direct-attach NVMe SSDs

  * UCS C225 M8N chassis: up to 10 direct attach NVMe SSDs

  * All 10 NVMe drives connected at PCIe Gen4 x4

  * M.2 boot options

  * Up to two 960 GB SATA M.2 drives with hardware RAID

  * Up to two 960 GB NVMe M.2 drives with NVMe hardware RAID

  * Up to three GPUs supported

  * Hybrid modular LOM/OCP 3.0

  * One dedicated Gen 4.0 x16 slot that can be used to add an mLOM or OCP 3.0 card for additional rear-panel connectivity

  * mLOM allows for Cisco UCS Virtual Interface Cards (VICs) without consuming a PCIe slot, supporting quad-port 10/25/50 Gbps or dual-port 40/100/200 Gbps network connectivity 

  * OCP 3.0 slot features full out-of-band management for select adapters

For complete list of supported peripherals for Cisco UCS C225 M8 Servers, see [Cisco UCS C225 M8 SFF Rack Server Spec Sheet](https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/ucs-c225-m8-sff-rack-server.pdf). 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCS C225 M8 Servers support only 14000 Series and 15000 Series secure boot VIC adapters.

* * *  
  
---|---  
  * **Added support for the following GPU on Cisco UCS C245 M8 Server:**

  * UCSC-GPU-H100-NVL


### New Hardware in X-Series M7 5.2(2.240074), X-Series M6 5.2(2.240073), and B-series M6 5.2(2.240073) Firmware Release — None 

### New Hardware Features in X-Series M7 and M6 Server Firmware 5.2(2.240053) and B-Series M6 Server Firmware 5.2(2.240051)

  * Support for the following DIMM on Cisco UCS X410c M7 Compute Nodes:

  * UCSX-MRX96G2RF3

  * Support for the following Graphics Processing Unit on Cisco UCS X410c M7 and Cisco UCS X210c M7 Compute Nodes:

  * UCSX-GPU-L40S

  * Support for the following Trusted Platform Module on Cisco UCS X210c M7, X410c M7, X210c M6 Compute Nodes, and Cisco UCS B200 M6 servers: 

  * UCS-TPM-002D

  * Support for the following 5th Generation Intel® Xeon® Scalable Processors on Cisco UCS X210c Compute Nodes: 

  * UCSX-CPU-I4510T - Intel® Xeon® Silver 4510T Processor 

  * UCSX-CPU-I4510 - Intel® Xeon® Silver 4510 Processor 

  * UCSX-CPU-I4509Y - Intel® Xeon® Silver 4509Y Processor 

  * UCSX-CPU-I3508U - Intel® Xeon® Bronze 3508U Processor 


### New Hardware Support in X-Series M7 Firmware 5.2(1.240010) and C-Series M7 Firmware 4.3(3.240022)

Support for the following 5th Generation Intel® Xeon® Scalable Processors on Cisco UCS X210c M7 Compute Nodes with server firmware release version 5.2(1.240010): 

  * UCSX-CPU-I8592V - Intel® Xeon® Platinum 8592V Processor 

  * UCSX-CPU-I8592+ - Intel® Xeon® Platinum 8592+ Processor 

  * UCSX-CPU-I8581V - Intel® Xeon® Platinum 8581V Processor 

  * UCSX-CPU-I8580 - Intel® Xeon® Platinum 8580 Processor 

  * UCSX-CPU-I8571N - Intel® Xeon® Platinum 8571 Processor 

  * UCSX-CPU-I8570 - Intel® Xeon® Platinum 8570 Processor 

  * UCSX-CPU-I8568Y+ - Intel® Xeon® Platinum 8568Y+ Processor 

  * UCSX-CPU-I8562Y+ - Intel® Xeon® Platinum 8562Y+ Processor 

  * UCSX-CPU-I8558U - Intel® Xeon® Platinum 8558U Processor 

  * UCSX-CPU-I8558P - Intel® Xeon® Platinum 8558P Processor 

  * UCSX-CPU-I8558 - Intel® Xeon® Platinum 8558 Processor 

  * UCSX-CPU-I6554S - - Intel® Xeon® Gold 6554S Processor 

  * UCSX-CPU-I6548Y+ - Intel® Xeon® Gold 6548Y+ Processor 

  * UCSX-CPU-I6548N - Intel® Xeon® Gold 6548N Processor 

  * UCSX-CPU-I6544Y - Intel® Xeon® Gold 6544Y Processor 

  * UCSX-CPU-I6542Y - Intel® Xeon® Gold 6542 Processor 

  * UCSX-CPU-I6538Y+ - Intel® Xeon® Gold 6538Y+ Processor 

  * UCSX-CPU-I6538N - Intel® Xeon® Gold 6538N Processor 

  * UCSX-CPU-I6534 - Intel® Xeon® Gold 6534 Processor 

  * UCSX-CPU-I6530 - Intel® Xeon® Gold 6530 Processor 

  * UCSX-CPU-I6526Y - Intel® Xeon® Gold 6526Y Processor 

  * UCSX-CPU-I5520+ - Intel® Xeon® Gold 5520+ Processor 

  * UCSX-CPU-I5515+ - Intel® Xeon® Gold 5515+ Processor 

  * UCSX-CPU-I5512U - Intel® Xeon® Gold 5512U Processor 

  * UCSX-CPU-I4516Y+ - Intel® Xeon® Silver 4516Y+ Processor 

  * UCSX-CPU-I4514Y - Intel® Xeon® Silver 4514Y Processor 


Support for the following 5th Generation Intel® Xeon® Scalable Processors on Cisco UCS C220 M7 and C240 M7 servers with server firmware version 4.3(3.240022): 

  * UCS-CPU-I8592V - Intel® Xeon® Platinum 8592V Processor 

  * UCS-CPU-I8592+ - Intel® Xeon® Platinum 8592+ Processor 

  * UCS-CPU-I8580 - Intel® Xeon® Platinum 8580 Processor 

  * UCS-CPU-I8568Y+ - Intel® Xeon® Platinum 8568Y+ Processor 

  * UCS-CPU-I8562Y+ - Intel® Xeon® Platinum 8562Y+ Processor 

  * UCS-CPU-I8558P - Intel® Xeon® Platinum 8558P Processor 

  * UCS-CPU-I8558 - Intel® Xeon® Platinum 8558 Processor 

  * UCS-CPU-I6554S - Intel® Xeon® Gold 6554S Processor 

  * UCS-CPU-I6548Y+ - Intel® Xeon® Gold 6548Y+ Processor 

  * UCS-CPU-I6548N - Intel® Xeon® Gold 6548N Processor 

  * UCS-CPU-I6544Y - Intel® Xeon® Gold 6544Y Processor 

  * UCS-CPU-I6542Y - Intel® Xeon® Gold 6542Y Processor 

  * UCS-CPU-I6538Y+ - Intel® Xeon® Gold 6538Y+ Processor 

  * UCS-CPU-I6534 - Intel® Xeon® Gold 6534 Processor 

  * UCS-CPU-I6530 - Intel® Xeon® Gold 6530 Processor 

  * UCS-CPU-I6526Y - Intel® Xeon® Gold 6526Y Processor 

  * UCS-CPU-I5520+ - Intel® Xeon® Gold 5520+ Processor 

  * UCS-CPU-I5515+ - Intel® Xeon® Gold 5515+ Processor 

  * UCS-CPU-I4516Y+ - Intel® Xeon® Silver 4516Y+ Processor 

  * UCS-CPU-I4514Y - Intel® Xeon® Silver 4514Y Processor 


#### Supported GPUs

Support for the following GPU cards with the above listed CPUs:

  * Support for Data Center GPU Flex 170, FH-3/4L, 150W PCIe on Cisco UCS C240 M7 servers

  * Support for Data Center GPU Flex 140, HHHL, 75W PCIe on Cisco UCS C220 M7 and C240 M7 servers


#### Support for DDR5 5600 MT/s DIMM

Support for the following 5600 DIMMs on Cisco UCS X410c M7 and X210c M7 Compute Nodes with server firmware version 5.2(1.240010):

  * UCSX-MRX16G1RE3 - 16GB DDR5-5600 RDIMM 1Rx8 (16Gb)

  * UCSX-MRX32G1RE3 - 32GB DDR5-5600 RDIMM 1Rx4 (16GB)

  * UCSX-MRX64G2RE3 - 64GB DDR5-5600 RDIMM 2Rx4 (16GB)

  * UCSX-MRX96G2RF3 - 96GB DDR5-5600 RDIMM 2Rx4 (24GB)

  * UCSX-MR128G4RE3 - 128GB DDR5-5600B RDIMM 4Rx4 (16GB)

  * UCSX-MR256G8RE3 - 256GB DDR5-5600 RDIMM 8Rx4 (16Gb)


Support for the following 5600 DIMMs on Cisco UCS C240 M7 and C220 M7 servers with Server Firmware version 4.3(3.240022):

  * UCS-MRX16G1RE3 - 16GB DDR5-5600 RDIMM 1Rx8 (16Gb)

  * UCS-MRX32G1RE3 - 32GB DDR5-5600 RDIMM 1Rx4 (16Gb)

  * UCS-MRX64G2RE3 - 64GB DDR5-5600 RDIMM 2Rx4 (16GB))

  * UCS-MRX96G2RF3 - 96GB DDR5-5600 RDIMM 2Rx4 (24GB) 

  * UCS-MR128G4RE3 - 128GB DDR5-5600 RDIMM 4Rx4 (16GB)

  * UCS-MR256G8RE3 - 256GB DDR5-5600 RDIMM 8Rx4 (16Gb)


### New Hardware Support in X-Series Firmware 5.2(0.230127), B-Series Firmware 5.2(0.230127), and C-Series Firmware Version 4.3(2.240002) — None 

### New Hardware Support in X-Series M7 Firmware 5.2(0.230092)

Support for the following Cisco UCS VIC 15000 Series Secure Boot-enabled mLOM adapter on Cisco UCS X-Series servers:

UCSX-ML-V5D200GV2 - Cisco UCS VIC 15230 (2x100G or 4x25G) mLOM on X-Series M6 and M7 servers.

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The hardware listed above is compatible with Infrastructure firmware version 4.3(2.230129) and later.

* * *  
  
---|---  
  
For more information on the new Hardware Support, see [Supported Hardware for Intersight Managed Mode](https://intersight.com/help/appliance/supported_systems#supported_hardware_for_intersight_managed_mode). 

### New Hardware Support in X-Series M7 Firmware 5.2(0.230041)

  * Support for UCSX-M2-PT-FPN (M.2 NVMe controller) on Cisco UCS X210c M7 Compute Node.

  * Support for the following Graphics Processing Units on Cisco UCS X210c M7 and UCS X410c M7 Compute Nodes.

  * UCSC-GPU-H100-80 

  * UCSC-GPU-L40 

  * UCSC-GPU-L4 

  * UCSC-GPU-FLEX140 

  * UCSC-GPU-FLEX170


For more information, see [Supported Hardware for Intersight Managed Mode](https://intersight.com/help/saas/supported_systems#supported_hardware_systems_and_software_versions). 

### New Hardware Support in B-Series M5 5.2(0.230127) and B-Series M6 Firmware 5.2(1.240010) — None

### New Hardware in C-series M5 Server Firmware Release 4.3(2.250016) — None 

### New Hardware in C-series M5 Server Firmware Release 4.3(2.240107) — None 

### New Hardware in C-Series M7 Server Firmware Release 4.3(4.242038)

Support for the following Cisco Trimode M1 24G RAID and HBA controllers:

  * UCSC-HBA-M1L16 and UCSC-RAID-M1L16 on Cisco UCSC-C220-M7 servers

  * UCSC-HBA-M1L16 and UCSC-RAID-MP1L32 on Cisco UCSC-C240-M7 servers


Advantages of Cisco Trimode M1 24G RAID and HBA controllers:

  * Uses Enterprise Key Management (EKMS) for remote key management, enhancing the physical security of data.

  * Uses the Distributed Management Task Force's (DMTF's) Redfish schema, ensuring independence from changes in storage software architecture or stack. 

  * Allows quick integration of new vendors and adaptors via Out-Of-Band management.

  * 5% of maximum drive space is reserved to allow slight variance in drive sizes over time. 


### New Hardware Support in C-Series M7 and M6 Server Firmware Release 4.3(4.241063) — None 

### New Hardware Support in C-Series M5 Firmware 4.3(2.240077) — None 

### New Hardware Features in C-Series M8 Server Firmware Release 4.3(4.241014)

#### Cisco UCS C245 M8 Rack Server

The Cisco UCS C245 M8 Rack Server extends the capabilities of the Cisco UCS rack server portfolio. It powers 4th Gen AMD EPYC™ Processors that have double the number of cores per socket compared to the previous generation, and are designed using AMD’s chiplet architecture. With advanced features like AMD Infinity Guard, compute-intensive applications will see significant performance improvements and will reap other benefits such as power and cost efficiencies. 

With the introduction of PCIe Gen 5.0 expansion slots for high-speed I/O, a DDR5 memory bus, and expanded storage capabilities, the server delivers significant performance and efficiency gains that will greatly enhance application performance. 

Some of the features of the server include:

  * CPU: Support for up to two 4th Gen AMD EPYC™ CPUs in a server designed to drive as much as 256 CPU cores (128 cores per socket) 

  * Storage: Up to 24 DDR5 DIMM slots, yielding up to 6 TB of capacity, using 256 GB DIMMs (12 DIMMs per socket)

  * Memory: Up to 4800 MT/s DDR5 memory

  * Up to 8 x PCIe Gen 4.0 slots or up to 4 x PCIe Gen 5.0 slots, plus a hybrid modular LAN on motherboard (mLOM) /OCP 3.0 slot (details below) 

  * Adapters: Support for Cisco UCS VIC 15000 Series adapters as well as multiple third-party NIC options

  * Up to 28 hot-swappable small-form-factor (SFF) SAS/SATA or NVMe drives (with up to 8 direct-attach NVMe drives)

  * New tri-mode RAID controller supports SAS4 plus NVMe hardware RAID

  * M.2 boot options

  * Up to two 960GB SATA M.2 drives with hardware RAID support

  * Up to two 960GB NVMe M.2 drives with NVMe hardware RAID

  * GPU: Support for up to Eight GPUs

  * Modular LOM / OCP 3.0

  * One dedicated PCIe Gen4x16 slot that can be used to add an mLOM or OCP 3.0 card for additional rear-panel connectivity

  * mLOM slot that can be used to install a Cisco UCS Virtual Interface Card (VIC) without consuming a PCIe slot, supporting quad-port 10/25/50 Gbps or dual-port 40/100/200 Gbps network connectivity 

  * OCP 3.0 slot that features full out-of-band management for select adapters


For more information on the sub-components bundled with the server, see [Cisco UCS C245 M8 Server Spec Sheet](https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/ucs-c245-m8-sff-rack-server.pdf). 

### New Hardware Features in C-Series M7 and M6 Server Firmware Release 4.3(4.240152)

  * Support for the following Graphics Processing Unit on Cisco UCS C240 M7 server:

  * UCSC-GPU-L40S

  * Support for the following Graphics Processing Unit on Cisco UCS C220 M6 and C240 M6 servers:

  * UCSC-GPU-L4

  * Support for the following Trusted Platform Module on Cisco UCS C220 M7, C240 M7, C220 M6, and C240 M6 servers:

  * UCS-TPM-002D

  * Support for the following Trusted Platform Module on Cisco UCS C225 M6 and C245 M6 servers:

  * UCS-TPM2-002D

  * Support for the following 5th Generation Intel® Xeon® Scalable Processors on Cisco UCS C220 M7 and C240 M7 servers: 

  * UCS-CPU-I4510T - Intel® Xeon® Silver 4510T Processor 

  * UCS-CPU-I4510 - Intel® Xeon® Silver 4510 Processor 

  * UCS-CPU-I4509Y - Intel® Xeon® Silver 4509Y Processor 

  * UCS-CPU-I3508U - Intel® Xeon® Bronze 3508U Processor 


### New Hardware Support in C-Series M5 Firmware 4.3(2.240053) — None 

### New Hardware Support in C-Series M6 Firmware 4.3(2.240037) — None 

### New Hardware Support in C-Series M7 and M6 4.3(3.240043) — None

### New Hardware Support in C-Series M7, M6, and M5 4.3(2.240009) — None

### New Hardware Support in C-Series Firmware 4.3(2.230270)

Support for the following Cisco UCS VIC 15000 Series Secure Boot-enabled mLOM adapters on Cisco UCS C-Series servers:

  * UCSC-M-V5D200GV2 - Cisco UCS VIC 15237 (2x40/100/200G) mLOM on C-Series M6 and M7 servers.

  * UCSC-M-V5Q50GV2 - Cisco UCS VIC 15427 (4x10/25/50G) mLOM on C-Series M6 and M7 servers.


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The hardware listed above is compatible with Infrastructure Firmware version 4.3(2.230129) and later.

* * *  
  
---|---  
  
For more information, see [Supported Hardware for Intersight Managed Mode](https://intersight.com/help/saas/supported_systems#supported_hardware_systems_and_software_versions). 

### New Hardware Support in C-Series Firmware 4.3(2.230207)

  * Support for the following Cisco UCS VIC 15000 Series Secure Boot-enabled PCIe adapters on Cisco UCS C-Series M6 and M7 servers:

  * UCSC-P-V5D200G - Cisco UCS VIC 15235 2x40/100/200G

  * UCSC-P-V5Q50G - Cisco UCS VIC 15425 4x10/25/50G


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The hardware listed above is compatible with Infrastructure Firmware version 4.3(2.230117) and later.

* * *  
  
---|---  
  
  * Support for the following Graphics Processing Units:

  * UCSC-GPU-H100-80 on Cisco UCS C240 M7 server

  * UCSC-GPU-L40 on Cisco UCS C240 M7 server

  * UCSC-GPU-L4 on Cisco UCS C-Series M7 server

  * UCSC-GPU-FLEX140 on Cisco UCS C-Series M7 server

  * UCSC-GPU-FLEX170 on Cisco UCS C240 M7 server


For more information, see [Supported Hardware for Intersight Managed Mode](https://intersight.com/help/saas/supported_systems#supported_hardware_systems_and_software_versions). 

### New Hardware Support in C-Series Firmware 4.3(1.230097)

  * Support for Cisco UCS C220 M7 and C240 M7 servers.

  * Support for the following Graphics Processing Units on C-Series M7 servers:

  * UCSC-GPU-A16

  * UCSC-GPU-A100-80


For more information, see [Supported Hardware for Intersight Managed Mode](https://intersight.com/help/saas/supported_systems#supported_hardware_systems_and_software_versions). 

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
  
## Updating the Firmware

To update the Cisco UCS firmware, see [Managing Firmware in Intersight Managed Mode](https://intersight.com/help/saas/resources#managing_firmware_in_intersight_managed_mode). 

## Security Fixes

### Security Fixes in X-Series M8, M7 5.4(0.260010), M6 5.4(0.260009), C-Series M8, M7, M6 4.3(6.260017), and B-Series M6, M5 5.4(0.260011) Server Firmware Release — None 

### Security Fixes in C-Series M5 Server Firmware Release 4.3(2.260007) — None 

### Security Fixes in Cisco UCS X-Series M7 5.4(0.260001) and C-Series M8, M7 4.3(6.260003) Server Firmware Release — None 

### Security Fixes in C-Series M5 Server Firmware Release 4.3(2.250063) — None 

### Security Fixes in Cisco UCS C-Series M7 Server Firmware Release 4.3(6.250117) — None 

### Security Fixes in Cisco UCS C-Series M7 and M6 Server Firmware Release 4.3(6.250101)

Defect ID - CSCwq36167

The Cisco UCS C-Series M6 Rack Servers include an Intel CPU that is affected by the vulnerability identified by the following Common Vulnerability and Exposures (CVE) ID: 

  * CVE-2025-20067 — Observable timing discrepancy in firmware for some Intel(R) CSME and Intel(R) SPS may allow a privileged user to potentially enable information disclosure via local access. 


The affected third-party software component has been upgraded to a version that includes fixes for the vulnerability. Future versions of the product(s) will not be affected by this vulnerability. 

Defect ID - CSCwq36171

The Cisco UCS C-Series M7 Rack Servers include an Intel CPU that is affected by the vulnerabilities identified by the following Common Vulnerability and Exposures (CVE) IDs: 

  * CVE-2025-21096 — Improper buffer restrictions in the firmware for some Intel(R) TDX may allow a privileged user to potentially enable escalation of privilege via local access. 

  * CVE-2025-20053 — Improper buffer restrictions for some Intel(R) Xeon(R) Processor firmware with SGX enabled may allow a privileged user to potentially enable escalation of privilege via local access. 

  * CVE-2025-24305 — Insufficient control flow management in the Alias Checking Trusted Module (ACTM) firmware for some Intel(R) Xeon(R) processors may allow a privileged user to potentially enable escalation of privilege via local access. 

  * CVE-2025-20613 — Predictable Seed in Pseudo-Random Number Generator (PRNG) in the firmware for some Intel(R) TDX may allow an authenticated user to potentially enable information disclosure via local access. 

  * CVE-2025-21090 — Missing reference to active allocated resource for some Intel(R) Xeon(R) processors may allow an authenticated user to potentially enable denial of service via local access. 

  * CVE-2025-22853 — Improper synchronization in the firmware for some Intel(R) TDX may allow a privileged user to potentially enable escalation of privilege via local access. 


The affected third-party software component has been upgraded to a version that includes fixes for the vulnerability. Future versions of the product(s) will not be affected by this vulnerability. 

### Security Fixes in Cisco UCS C-Series M8 Server Firmware Release 4.3(5.250045) — None 

### Security Fixes in Cisco UCS C-Series M8 Server Firmware Release 4.3(6.250060) — None 

### Security Fixes in C-Series M5 Server Firmware Release 4.3(2.250045) — None 

### Security Fixes in C-Series M8 Server Firmware Release 4.3(5.250043) — None 

### Security Fixes in X-Series M6 5.4(0.250047), C-Series M6 4.3(6.250053), and B-Series M6 5.4(0.250048) Server Firmware Release 

Defect ID - CSCwo49706

The Cisco UCS B-Series M6 Blade Servers, UCS C-Series M6 Rack Servers, and UCS X-Series M6 Compute Nodes include an Intel CPU that is affected by the vulnerability identified by the following Common Vulnerability and Exposures (CVE) ID: 

  * CVE-2024-45332 — Exposure of sensitive information caused by shared microarchitectural predictor state that influences transient execution in the indirect branch predictors for some Intel®Processors may allow an authenticated user to potentially enable information disclosure via local access. 


The affected third-party software component has been upgraded to a version that includes fixes for the vulnerability. Future versions of the product(s) will not be affected by this vulnerability. 

### Security Fixes in X-Series M7 5.4(0.250048) and C-Series M7 4.3(6.250053) Server Firmware Release 

Defect ID - CSCwo49711

The Cisco products UCS C-Series M7 Rack Servers and UCS X-Series M7 Compute Nodes include an Intel CPU that is affected by the vulnerabilities identified by the following Common Vulnerability and Exposures (CVE) IDs: 

  * CVE-2025-20103 — Insufficient resource pool in the core management mechanism for some Intel®Processors may allow an authenticated user to potentially enable denial of service via local access. 

  * CVE-2025-20054 — Uncaught exception in the core management mechanism for some Intel®Processors may allow an authenticated user to potentially enable denial of service through local access. 

  * CVE-2024-45332 — Exposure of sensitive information caused by shared microarchitectural predictor state that influences transient execution in the indirect branch predictors for some Intel®Processors may allow an authenticated user to potentially enable information disclosure via local access. 


The affected third-party software component has been upgraded to a version that includes fixes for the vulnerability. Future versions of the product(s) will not be affected by this vulnerability. 

### Security Fixes in C-series M5 Server Firmware Release 4.3(2.250037)

Defect ID - CSCwo49702

The UCS C-Series M5 Rack Servers include an Intel CPU that is affected by the vulnerability identified by the following Common Vulnerability and Exposures (CVE) ID: 

  * CVE-2024-45332 — Exposure of sensitive information caused by shared microarchitectural predictor state that influences transient execution in the indirect branch predictors for some Intel(R) Processors may allow an authenticated user to potentially enable information disclosure via local access. 


### Security Fixes in X-Series M8 5.4(0.250040), 5.4(0.250044) and M7 5.4(0.250040), and C-Series 4.3(6.250044) Server Firmware Release — None 

### Security Fixes in C-Series M8, M7, and M6 Server Firmware Release 4.3(5.250033) — None 

### Security Fixes in B-Series M5 5.4(0.250034) Server Firmware Release 

CSCwm73565

Cisco UCS B-Series M5 servers, which include an Intel CPU and BIOS, are affected by the vulnerabilities identified under the following Common Vulnerabilities and Exposures (CVE) IDs: 

  * CVE-2024-28047—Improper input validation in UEFI firmware for some Intel(R) Processors may allow a privileged user to potentially enable information disclosure via local access. 


### Security Fixes in C-Series M8, M7, and M6 Server Firmware Release 4.3(5.250030)

Defect ID - CSCwn63691

Cisco UCS C225 M6 and C245 M6 servers are affected by vulnerabilities identified by the following Common Vulnerability and Exposures (CVE) IDs: 

  * CVE-2024-56161—Improper signature verification in AMD CPU ROM microcode patch loader may allow an attacker with local administrator privilege to load malicious CPU microcode resulting in loss of confidentiality and integrity of a confidential guest running under AMD SEV-SNP. 

  * CVE-2024-21925—Improper input validation within the AmdPspP2CmboxV2 driver may allow a privileged attacker to overwrite SMRAM, leading to arbitrary code execution. 

  * CVE-2024-21924—SMM callout vulnerability within the AmdPlatformRasSspSmm driver could allow a ring 0 attacker to modify boot services handlers, potentially resulting in arbitrary code execution. 


### Security Fixes in C-series M5 Server Firmware Release 4.3(2.250021) — None 

### Security Fixes in X-Series M8, M7, M6 5.3(0.250021) and B-Series M6, M5 5.3(0.250021) Server Firmware Release — None

### Security Fixes in X-Series M7 5.2(2.240080), M6 5.2(2.240078), B-Series M6, M5 5.2(2.240080), and C-series M7, M6 4.3(4.242066) Firmware Release — None 

### Security Fixes in X- Series 5.3(0.240016) and B-Series 5.3(0.240014) Server Firmware Release 

Defect ID - CSCwk62723

Cisco UCS B-Series Blade Servers-Serial over LAN (SOL) and Cisco UCS X-Series Compute Nodes-Serial over LAN (SOL) includes Third-party Software that is affected by the vulnerabilities identified by the following Common Vulnerability and Exposures (CVE) IDs: 

  * CVE-2024-6387—A security regression (CVE-2006-5051) has been discovered in the OpenSSH server (sshd). A race condition exists that may cause sshd to handle certain signals unsafely. This vulnerability can potentially be exploited by an unauthenticated, remote attacker by failing to authenticate within a specified time period. 


The affected third-party software component has been upgraded to a version that includes fixes for the vulnerability. Future versions of the product(s) will not be affected by this vulnerability. 

### Security Fixes in X-Series M7 5.2(2.240074), X-Series M6 5.2(2.240073), and B-series M6 5.2(2.240073) Firmware Release 

Defect ID - CSCwk62723

Cisco UCS B-Series Blade Servers-Serial over LAN (SOL) and Cisco UCS X-Series Compute Nodes-Serial over LAN (SOL) includes Third-party Software that is affected by the vulnerabilities identified by the following Common Vulnerability and Exposures (CVE) IDs: 

  * CVE-2024-6387—A security regression (CVE-2006-5051) has been discovered in the OpenSSH server (sshd). A race condition exists that may cause sshd to handle certain signals unsafely. This vulnerability can potentially be exploited by an unauthenticated, remote attacker by failing to authenticate within a specified time period. 


The affected third-party software component has been upgraded to a version that includes fixes for the vulnerability. Future versions of the product(s) will not be affected by this vulnerability. 

### Security Fixes in X-Series M7 and M6 Firmware Release 5.2(2.240053) — None 

### Security Fixes in X-Series M6 Server 5.2(0.230127), B-Series Server 5.2(0.230127), and C-Series M6 Server 4.3(2.240002)

The following security issue is resolved:

**Defect ID - CSCwh68315**

The Cisco products UCS B-Series M6 Servers; UCS C-Series M6 servers; UCS X-Series M6 Compute Nodes include an Intel® CPU that is affected by the vulnerability identified by the following Common Vulnerability and Exposures (CVE) ID: 

CVE-2023-23583—Sequence of processor instructions leads to unexpected behavior for some Intel® Processors may allow an authenticated user to potentially enable escalation of privilege and/or information disclosure and/or denial of service via local access. 

### Security Fixes in B-Series M6 and M5 Server Firmware Release 5.2(2.240051) — None 

### Security Fixes in B-Series M6 5.2(1.240010) and C-Series 4.3(3.240022), X-Series 5.2(1.240010) M6 and M7 Servers

The following security issues are resolved:

Defect ID - CSCwh58728

Cisco UCS Manager includes Third-party Software that is affected by the vulnerabilities identified by the following Common Vulnerability and Exposures (CVE) IDs: 

  * CVE-2023-38408—The PKCS#11 feature in ssh-agent in OpenSSH before 9.3p2 has an insufficiently trustworthy search path, leading to remote code execution if an agent is forwarded to an attacker-controlled system. (Code in /usr/lib is not necessarily safe for loading into ssh-agent.) 


The affected third-party software component has been upgraded to a version that includes fixes for the vulnerability. Future versions of the product(s) will not be affected by this vulnerability. 

### Security Fixes in C-series M5 Server Firmware Release 4.3(2.250016)

Defect ID - CSCwm73565

Cisco UCS M5 servers are affected by the vulnerabilities identified by the following Common Vulnerability and Exposures (CVE) IDs: 

  * CVE-2024-28047—Improper input validation in UEFI firmware for some Intel(R) Processors may allow a privileged user to potentially enable information disclosure via local access. 


### Security Fixes in C-series M5 Server Firmware Release 4.3(2.240107) — None 

### Security Fixes in C-Series M5 Server Firmware Release 4.3(2.240090)

#### Defect ID - CSCwk77757

Cisco UCS M5 servers are affected by the vulnerabilities identified by the following Common Vulnerability and Exposures (CVE) IDs: 

  * CVE-2024-24853—Incorrect behavior order in transition between executive monitor and SMI transfer monitor (STM) in some Intel(R) Processor may allow a privileged user to potentially enable escalation of privilege through local access. 

  * CVE-2024-21781—Improper input validation in UEFI firmware for some Intel(R) Processors may allow a privileged user to enable information disclosure or denial of service through local access. 


#### Defect ID - CSCwi21160

Cisco UCS server includes Third-party Software that is affected by the vulnerabilities identified by the following Common Vulnerability and Exposures (CVE) IDs: 

  * CVE-2019-1543—ChaCha20-Poly1305 is an AEAD cipher, and requires a unique nonce input for every encryption operation. RFC 7539 specifies that the nonce value (IV) should be 96 bits (12 bytes). OpenSSL allows a variable nonce length and front pads the nonce with 0 bytes if it is less than 12 bytes. However it also incorrectly allows a nonce to be set of up to 16 bytes. In this case only the last 12 bytes are significant and any additional leading bytes are ignored. It is a requirement of using this cipher that nonce values are unique. Messages encrypted using a reused nonce value are susceptible to serious confidentiality and integrity attacks. If an application changes the default nonce length to be longer than 12 bytes and then makes a change to the leading bytes of the nonce expecting the new value to be a new unique nonce then such an application could inadvertently encrypt messages with a reused nonce. Additionally the ignored bytes in a long nonce are not covered by the integrity guarantee of this cipher. Any application that relies on the integrity of these ignored leading bytes of a long nonce may be further affected. Any OpenSSL internal use of this cipher, including in SSL/TLS, is safe because no such use sets such a long nonce value. However user applications that use this cipher directly and set a non-default nonce length to be longer than 12 bytes may be vulnerable. OpenSSL versions 1.1.1 and 1.1.0 are affected by this issue. Due to the limited scope of affected deployments this has been assessed as low severity and therefore we are not creating new releases at this time. Fixed in OpenSSL 1.1.1c (Affected 1.1.1-1.1.1b). Fixed in OpenSSL 1.1.0k (Affected 1.1.0-1.1.0j). 

  * CVE-2019-1547—Normally in OpenSSL EC groups always have a co-factor present and this is used in side channel resistant code paths. However, in some cases, it is possible to construct a group using explicit parameters (instead of using a named curve). In those cases it is possible that such a group does not have the cofactor present. This can occur even where all the parameters match a known named curve. If such a curve is used then OpenSSL falls back to non-side channel resistant code paths which may result in full key recovery during an ECDSA signature operation. In order to be vulnerable an attacker would have to have the ability to time the creation of a large number of signatures where explicit parameters with no co-factor present are in use by an application using libcrypto. For the avoidance of doubt libssl is not vulnerable because explicit parameters are never used. Fixed in OpenSSL 1.1.1d (Affected 1.1.1-1.1.1c). Fixed in OpenSSL 1.1.0l (Affected 1.1.0-1.1.0k). Fixed in OpenSSL 1.0.2t (Affected 1.0.2-1.0.2s). 

  * CVE-2019-1552—OpenSSL has internal defaults for a directory tree where it can find a configuration file as well as certificates used for verification in TLS. This directory is most commonly referred to as OPENSSLDIR, and is configurable with the -\\-prefix / -\\-openssldir configuration options. For OpenSSL versions 1.1.0 and 1.1.1, the mingw configuration targets assume that resulting programs and libraries are installed in a Unix-like environment and the default prefix for program installation as well as for OPENSSLDIR should be '/usr/local'. However, mingw programs are Windows programs, and as such, find themselves looking at sub-directories of 'C:/usr/local', which may be world writable, which enables untrusted users to modify OpenSSL's default configuration, insert CA certificates, modify (or even replace) existing engine modules, etc. For OpenSSL 1.0.2, '/usr/local/ssl' is used as default for OPENSSLDIR on all Unix and Windows targets, including Visual C builds. However, some build instructions for the diverse Windows targets on 1.0.2 encourage you to specify your own -\\-prefix. OpenSSL versions 1.1.1, 1.1.0 and 1.0.2 are affected by this issue. Due to the limited scope of affected deployments this has been assessed as low severity and therefore we are not creating new releases at this time. Fixed in OpenSSL 1.1.1d (Affected 1.1.1-1.1.1c). Fixed in OpenSSL 1.1.0l (Affected 1.1.0-1.1.0k). Fixed in OpenSSL 1.0.2t (Affected 1.0.2-1.0.2s). 

  * CVE-2019-1563—In situations where an attacker receives automated notification of the success or failure of a decryption attempt an attacker, after sending a very large number of messages to be decrypted, can recover a CMS/PKCS7 transported encryption key or decrypt any RSA encrypted message that was encrypted with the public RSA key, using a Bleichenbacher padding oracle attack. Applications are not affected if they use a certificate together with the private RSA key to the CMS_decrypt or PKCS7_decrypt functions to select the correct recipient info to decrypt. Fixed in OpenSSL 1.1.1d (Affected 1.1.1-1.1.1c). Fixed in OpenSSL 1.1.0l (Affected 1.1.0-1.1.0k). Fixed in OpenSSL 1.0.2t (Affected 1.0.2-1.0.2s). 

  * CVE-2020-1968—The Raccoon attack exploits a flaw in the TLS specification which can lead to an attacker being able to compute the pre-master secret in connections which have used a Diffie-Hellman (DH) based ciphersuite. In such a case this would result in the attacker being able to eavesdrop on all encrypted communications sent over that TLS connection. The attack can only be exploited if an implementation re-uses a DH secret across multiple TLS connections. Note that this issue only impacts DH ciphersuites and not ECDH ciphersuites. This issue affects OpenSSL 1.0.2 which is out of support and no longer receiving public updates. OpenSSL 1.1.1 is not vulnerable to this issue. Fixed in OpenSSL 1.0.2w (Affected 1.0.2-1.0.2v). 

  * CVE-2021-23840—Calls to EVP_CipherUpdate, EVP_EncryptUpdate and EVP_DecryptUpdate may overflow the output length argument in some cases where the input length is close to the maximum permissable length for an integer on the platform. In such cases the return value from the function call will be 1 (indicating success), but the output length value will be negative. This could cause applications to behave incorrectly or crash. OpenSSL versions 1.1.1i and below are affected by this issue. Users of these versions should upgrade to OpenSSL 1.1.1j. OpenSSL versions 1.0.2x and below are affected by this issue. However OpenSSL 1.0.2 is out of support and no longer receiving public updates. Premium support customers of OpenSSL 1.0.2 should upgrade to 1.0.2y. Other users should upgrade to 1.1.1j. Fixed in OpenSSL 1.1.1j (Affected 1.1.1-1.1.1i). Fixed in OpenSSL 1.0.2y (Affected 1.0.2-1.0.2x). 

  * CVE-2021-3711—In order to decrypt SM2 encrypted data an application is expected to call the API function EVP_PKEY_decrypt(). Typically an application will call this function twice. The first time, on entry, the "out" parameter can be NULL and, on exit, the "outlen" parameter is populated with the buffer size required to hold the decrypted plaintext. The application can then allocate a sufficiently sized buffer and call EVP_PKEY_decrypt() again, but this time passing a non-NULL value for the "out" parameter. A bug in the implementation of the SM2 decryption code means that the calculation of the buffer size required to hold the plaintext returned by the first call to EVP_PKEY_decrypt() can be smaller than the actual size required by the second call. This can lead to a buffer overflow when EVP_PKEY_decrypt() is called by the application a second time with a buffer that is too small. A malicious attacker who is able present SM2 content for decryption to an application could cause attacker chosen data to overflow the buffer by up to a maximum of 62 bytes altering the contents of other data held after the buffer, possibly changing application behaviour or causing the application to crash. The location of the buffer is application dependent but is typically heap allocated. Fixed in OpenSSL 1.1.1l (Affected 1.1.1-1.1.1k). 

  * CVE-2021-3712—ASN.1 strings are represented internally within OpenSSL as an ASN1_STRING structure which contains a buffer holding the string data and a field holding the buffer length. This contrasts with normal C strings which are repesented as a buffer for the string data which is terminated with a NUL (0) byte. Although not a strict requirement, ASN.1 strings that are parsed using OpenSSL's own "d2i" functions (and other similar parsing functions) as well as any string whose value has been set with the ASN1_STRING_set() function will additionally NUL terminate the byte array in the ASN1_STRING structure. However, it is possible for applications to directly construct valid ASN1_STRING structures which do not NUL terminate the byte array by directly setting the "data" and "length" fields in the ASN1_STRING array. This can also happen by using the ASN1_STRING_set0() function. Numerous OpenSSL functions that print ASN.1 data have been found to assume that the ASN1_STRING byte array will be NUL terminated, even though this is not guaranteed for strings that have been directly constructed. Where an application requests an ASN.1 structure to be printed, and where that ASN.1 structure contains ASN1_STRINGs that have been directly constructed by the application without NUL terminating the "data" field, then a read buffer overrun can occur. The same thing can also occur during name constraints processing of certificates (for example if a certificate has been directly constructed by the application instead of loading it via the OpenSSL parsing functions, and the certificate contains non NUL terminated ASN1_STRING structures). It can also occur in the X509_get1_email(), X509_REQ_get1_email() and X509_get1_ocsp() functions. If a malicious actor can cause an application to directly construct an ASN1_STRING and then process it through one of the affected OpenSSL functions then this issue could be hit. This might result in a crash (causing a Denial of Service attack). It could also result in the disclosure of private memory contents (such as private keys, or sensitive plaintext). Fixed in OpenSSL 1.1.1l (Affected 1.1.1-1.1.1k). Fixed in OpenSSL 1.0.2za (Affected 1.0.2-1.0.2y). 

  * CVE-2022-0778—The BN_mod_sqrt() function, which computes a modular square root, contains a bug that can cause it to loop forever for non-prime moduli. Internally this function is used when parsing certificates that contain elliptic curve public keys in compressed form or explicit elliptic curve parameters with a base point encoded in compressed form. It is possible to trigger the infinite loop by crafting a certificate that has invalid explicit curve parameters. Since certificate parsing happens prior to verification of the certificate signature, any process that parses an externally supplied certificate may thus be subject to a denial of service attack. The infinite loop can also be reached when parsing crafted private keys as they can contain explicit elliptic curve parameters. Thus vulnerable situations include: - TLS clients consuming server certificates \- TLS servers consuming client certificates - Hosting providers taking certificates or private keys from customers - Certificate authorities parsing certification requests from subscribers - Anything else which parses ASN.1 elliptic curve parameters Also any other applications that use the BN_mod_sqrt() where the attacker can control the parameter values are vulnerable to this DoS issue. In the OpenSSL 1.0.2 version the public key is not parsed during initial parsing of the certificate which makes it slightly harder to trigger the infinite loop. However any operation which requires the public key from the certificate will trigger the infinite loop. In particular the attacker can use a self-signed certificate to trigger the loop during verification of the certificate signature. This issue affects OpenSSL versions 1.0.2, 1.1.1 and 3.0. It was addressed in the releases of 1.1.1n and 3.0.2 on the 15th March 2022. Fixed in OpenSSL 3.0.2 (Affected 3.0.0,3.0.1). Fixed in OpenSSL 1.1.1n (Affected 1.1.1-1.1.1m). Fixed in OpenSSL 1.0.2zd (Affected 1.0.2-1.0.2zc). 


#### Defect ID - CSCwi21161

Cisco UCS server includes Third-party Software that is affected by the vulnerabilities identified by the following Common Vulnerability and Exposures (CVE) IDs: 

  * CVE-2010-4252—OpenSSL before 1.0.0c, when J-PAKE is enabled, does not properly validate the public parameters in the J-PAKE protocol, which allows remote attackers to bypass the need for knowledge of the shared secret, and successfully authenticate, by sending crafted values in each round of the protocol. 

  * CVE-2010-5298—Race condition in the ssl3_read_bytes function in s3_pkt.c in OpenSSL through 1.0.1g, when SSL_MODE_RELEASE_BUFFERS is enabled, allows remote attackers to inject data across sessions or cause a denial of service (use-after-free and parsing error) via an SSL connection in a multithreaded environment. 

  * CVE-2011-1945—The elliptic curve cryptography (ECC) subsystem in OpenSSL 1.0.0d and earlier, when the Elliptic Curve Digital Signature Algorithm (ECDSA) is used for the ECDHE_ECDSA cipher suite, does not properly implement curves over binary fields, which makes it easier for context-dependent attackers to determine private keys via a timing attack and a lattice calculation. 

  * CVE-2011-4108—The DTLS implementation in OpenSSL before 0.9.8s and 1.x before 1.0.0f performs a MAC check only if certain padding is valid, which makes it easier for remote attackers to recover plaintext via a padding oracle attack. 

  * CVE-2011-4576—The SSL 3.0 implementation in OpenSSL before 0.9.8s and 1.x before 1.0.0f does not properly initialize data structures for block cipher padding, which might allow remote attackers to obtain sensitive information by decrypting the padding data sent by an SSL peer. 

  * CVE-2011-4577—OpenSSL before 0.9.8s and 1.x before 1.0.0f, when RFC 3779 support is enabled, allows remote attackers to cause a denial of service (assertion failure) via an X.509 certificate containing certificate-extension data associated with (1) IP address blocks or (2) Autonomous System (AS) identifiers. 

  * CVE-2011-4619—The Server Gated Cryptography (SGC) implementation in OpenSSL before 0.9.8s and 1.x before 1.0.0f does not properly handle handshake restarts, which allows remote attackers to cause a denial of service (CPU consumption) via unspecified vectors. 

  * CVE-2012-0027—The GOST ENGINE in OpenSSL before 1.0.0f does not properly handle invalid parameters for the GOST block cipher, which allows remote attackers to cause a denial of service (daemon crash) via crafted data from a TLS client. 

  * CVE-2013-6449—The ssl_get_algorithm2 function in ssl/s3_lib.c in OpenSSL before 1.0.2 obtains a certain version number from an incorrect data structure, which allows remote attackers to cause a denial of service (daemon crash) via crafted traffic from a TLS 1.2 client. 

  * CVE-2014-0076—The Montgomery ladder implementation in OpenSSL through 1.0.0l does not ensure that certain swap operations have a constant-time behavior, which makes it easier for local users to obtain ECDSA nonces via a FLUSH+RELOAD cache side-channel attack. 

  * CVE-2014-3566—The SSL protocol 3.0, as used in OpenSSL through 1.0.1i and other products, uses nondeterministic CBC padding, which makes it easier for man-in-the-middle attackers to obtain cleartext data via a padding-oracle attack, aka the "POODLE" issue. 

  * CVE-2014-3567—Memory leak in the tls_decrypt_ticket function in t1_lib.c in OpenSSL before 0.9.8zc, 1.0.0 before 1.0.0o, and 1.0.1 before 1.0.1j allows remote attackers to cause a denial of service (memory consumption) via a crafted session ticket that triggers an integrity-check failure. 

  * CVE-2014-3568—OpenSSL before 0.9.8zc, 1.0.0 before 1.0.0o, and 1.0.1 before 1.0.1j does not properly enforce the no-ssl3 build option, which allows remote attackers to bypass intended access restrictions via an SSL 3.0 handshake, related to s23_clnt.c and s23_srvr.c. 

  * CVE-2014-3570—The BN_sqr implementation in OpenSSL before 0.9.8zd, 1.0.0 before 1.0.0p, and 1.0.1 before 1.0.1k does not properly calculate the square of a BIGNUM value, which might make it easier for remote attackers to defeat cryptographic protection mechanisms via unspecified vectors, related to crypto/bn/asm/mips.pl, crypto/bn/asm/x86_64-gcc.c, and crypto/bn/bn_asm.c. 

  * CVE-2014-3571—OpenSSL before 0.9.8zd, 1.0.0 before 1.0.0p, and 1.0.1 before 1.0.1k allows remote attackers to cause a denial of service (NULL pointer dereference and application crash) via a crafted DTLS message that is processed with a different read operation for the handshake header than for the handshake body, related to the dtls1_get_record function in d1_pkt.c and the ssl3_read_n function in s3_pkt.c. 

  * CVE-2014-3572—The ssl3_get_key_exchange function in s3_clnt.c in OpenSSL before 0.9.8zd, 1.0.0 before 1.0.0p, and 1.0.1 before 1.0.1k allows remote SSL servers to conduct ECDHE-to-ECDH downgrade attacks and trigger a loss of forward secrecy by omitting the ServerKeyExchange message. 

  * CVE-2014-8275—OpenSSL before 0.9.8zd, 1.0.0 before 1.0.0p, and 1.0.1 before 1.0.1k does not enforce certain constraints on certificate data, which allows remote attackers to defeat a fingerprint-based certificate-blacklist protection mechanism by including crafted data within a certificate's unsigned portion, related to crypto/asn1/a_verify.c, crypto/dsa/dsa_asn1.c, crypto/ecdsa/ecs_vrf.c, and crypto/x509/x_all.c. 

  * CVE-2015-0204—The ssl3_get_key_exchange function in s3_clnt.c in OpenSSL before 0.9.8zd, 1.0.0 before 1.0.0p, and 1.0.1 before 1.0.1k allows remote SSL servers to conduct RSA-to-EXPORT_RSA downgrade attacks and facilitate brute-force decryption by offering a weak ephemeral RSA key in a noncompliant role, related to the "FREAK" issue. NOTE: the scope of this CVE is only client code based on OpenSSL, not EXPORT_RSA issues associated with servers or other TLS implementations. 

  * CVE-2015-0209—Use-after-free vulnerability in the d2i_ECPrivateKey function in crypto/ec/ec_asn1.c in OpenSSL before 0.9.8zf, 1.0.0 before 1.0.0r, 1.0.1 before 1.0.1m, and 1.0.2 before 1.0.2a might allow remote attackers to cause a denial of service (memory corruption and application crash) or possibly have unspecified other impact via a malformed Elliptic Curve (EC) private-key file that is improperly handled during import. 

  * CVE-2015-0286—The ASN1_TYPE_cmp function in crypto/asn1/a_type.c in OpenSSL before 0.9.8zf, 1.0.0 before 1.0.0r, 1.0.1 before 1.0.1m, and 1.0.2 before 1.0.2a does not properly perform boolean-type comparisons, which allows remote attackers to cause a denial of service (invalid read operation and application crash) via a crafted X.509 certificate to an endpoint that uses the certificate-verification feature. 

  * CVE-2015-0287—The ASN1_item_ex_d2i function in crypto/asn1/tasn_dec.c in OpenSSL before 0.9.8zf, 1.0.0 before 1.0.0r, 1.0.1 before 1.0.1m, and 1.0.2 before 1.0.2a does not reinitialize CHOICE and ADB data structures, which might allow attackers to cause a denial of service (invalid write operation and memory corruption) by leveraging an application that relies on ASN.1 structure reuse. 

  * CVE-2015-0288—The X509_to_X509_REQ function in crypto/x509/x509_req.c in OpenSSL before 0.9.8zf, 1.0.0 before 1.0.0r, 1.0.1 before 1.0.1m, and 1.0.2 before 1.0.2a might allow attackers to cause a denial of service (NULL pointer dereference and application crash) via an invalid certificate key. 

  * CVE-2015-0289—The PKCS#7 implementation in OpenSSL before 0.9.8zf, 1.0.0 before 1.0.0r, 1.0.1 before 1.0.1m, and 1.0.2 before 1.0.2a does not properly handle a lack of outer ContentInfo, which allows attackers to cause a denial of service (NULL pointer dereference and application crash) by leveraging an application that processes arbitrary PKCS#7 data and providing malformed data with ASN.1 encoding, related to crypto/pkcs7/pk7_doit.c and crypto/pkcs7/pk7_lib.c. 

  * CVE-2015-0293—The SSLv2 implementation in OpenSSL before 0.9.8zf, 1.0.0 before 1.0.0r, 1.0.1 before 1.0.1m, and 1.0.2 before 1.0.2a allows remote attackers to cause a denial of service (s2_lib.c assertion failure and daemon exit) via a crafted CLIENT-MASTER-KEY message. 

  * CVE-2015-1788—The BN_GF2m_mod_inv function in crypto/bn/bn_gf2m.c in OpenSSL before 0.9.8s, 1.0.0 before 1.0.0e, 1.0.1 before 1.0.1n, and 1.0.2 before 1.0.2b does not properly handle ECParameters structures in which the curve is over a malformed binary polynomial field, which allows remote attackers to cause a denial of service (infinite loop) via a session that uses an Elliptic Curve algorithm, as demonstrated by an attack against a server that supports client authentication. 

  * CVE-2015-1789—The X509_cmp_time function in crypto/x509/x509_vfy.c in OpenSSL before 0.9.8zg, 1.0.0 before 1.0.0s, 1.0.1 before 1.0.1n, and 1.0.2 before 1.0.2b allows remote attackers to cause a denial of service (out-of-bounds read and application crash) via a crafted length field in ASN1_TIME data, as demonstrated by an attack against a server that supports client authentication with a custom verification callback. 

  * CVE-2015-1790—The PKCS7_dataDecodefunction in crypto/pkcs7/pk7_doit.c in OpenSSL before 0.9.8zg, 1.0.0 before 1.0.0s, 1.0.1 before 1.0.1n, and 1.0.2 before 1.0.2b allows remote attackers to cause a denial of service (NULL pointer dereference and application crash) via a PKCS#7 blob that uses ASN.1 encoding and lacks inner EncryptedContent data. 

  * CVE-2015-1791—Rare condition in the ssl3_get_new_session_ticket function in ssl/s3_clnt.c in OpenSSL before 0.9.8zg, 1.0.0 before 1.0.0s, 1.0.1 before 1.0.1n, and 1.0.2 before 1.0.2b, when used for a multi-threaded client, allows remote attackers to cause a denial of service (double free and application crash) or possibly have unspecified other impact by providing a NewSessionTicket during an attempt to reuse a ticket that had been obtained earlier. 

  * CVE-2015-1792—The do_free_upto function in crypto/cms/cms_smime.c in OpenSSL before 0.9.8zg, 1.0.0 before 1.0.0s, 1.0.1 before 1.0.1n, and 1.0.2 before 1.0.2b allows remote attackers to cause a denial of service (infinite loop) via vectors that trigger a NULL value of a BIO data structure, as demonstrated by an unrecognized X.660 OID for a hash function. 

  * CVE-2015-3195—The ASN1_TFLG_COMBINE implementation in crypto/asn1/tasn_dec.c in OpenSSL before 0.9.8zh, 1.0.0 before 1.0.0t, 1.0.1 before 1.0.1q, and 1.0.2 before 1.0.2e mishandles errors caused by malformed X509_ATTRIBUTE data, which allows remote attackers to obtain sensitive information from process memory by triggering a decoding failure in a PKCS#7 or CMS application. 

  * CVE-2015-4000—The TLS protocol 1.2 and earlier, when a DHE_EXPORT ciphersuite is enabled on a server but not on a client, does not properly convey a DHE_EXPORT choice, which allows man-in-the-middle attackers to conduct cipher-downgrade attacks by rewriting a ClientHello with DHE replaced by DHE_EXPORT and then rewriting a ServerHello with DHE_EXPORT replaced by DHE, aka the "Logjam" issue. 

  * CVE-2016-0703—The get_client_master_key function in s2_srvr.c in the SSLv2 implementation in OpenSSL before 0.9.8zf, 1.0.0 before 1.0.0r, 1.0.1 before 1.0.1m, and 1.0.2 before 1.0.2a accepts a nonzero CLIENT-MASTER-KEY CLEAR-KEY-LENGTH value for an arbitrary cipher, which allows man-in-the-middle attackers to determine the MASTER-KEY value and decrypt TLS ciphertext data by leveraging a Bleichenbacher RSA padding oracle, a related issue to CVE-2016-0800. 

  * CVE-2016-0704—An oracle protection mechanism in the get_client_master_key function in s2_srvr.c in the SSLv2 implementation in OpenSSL before 0.9.8zf, 1.0.0 before 1.0.0r, 1.0.1 before 1.0.1m, and 1.0.2 before 1.0.2a overwrites incorrect MASTER-KEY bytes during use of export cipher suites, which makes it easier for remote attackers to decrypt TLS ciphertext data by leveraging a Bleichenbacher RSA padding oracle, a related issue to CVE-2016-0800. 

  * CVE-2016-2106—Integer overflow in the EVP_EncryptUpdate function in crypto/evp/evp_enc.c in OpenSSL before 1.0.1t and 1.0.2 before 1.0.2h allows remote attackers to cause a denial of service (heap memory corruption) via a large amount of data. 

  * CVE-2016-2107—The AES-NI implementation in OpenSSL before 1.0.1t and 1.0.2 before 1.0.2h does not consider memory allocation during a certain padding check, which allows remote attackers to obtain sensitive cleartext information via a padding-oracle attack against an AES CBC session. NOTE: this vulnerability exists because of an incorrect fix for CVE-2013-0169. 

  * CVE-2016-2108—The ASN.1 implementation in OpenSSL before 1.0.1o and 1.0.2 before 1.0.2c allows remote attackers to execute arbitrary code or cause a denial of service (buffer underflow and memory corruption) via an ANY field in crafted serialized data, aka the "negative zero" issue. 

  * CVE-2016-2109—The asn1_d2i_read_bio function in crypto/asn1/a_d2i_fp.c in the ASN.1 BIO implementation in OpenSSL before 1.0.1t and 1.0.2 before 1.0.2h allows remote attackers to cause a denial of service (memory consumption) via a short invalid encoding. 

  * CVE-2016-2176—The X509_NAME_oneline function in crypto/x509/x509_obj.c in OpenSSL before 1.0.1t and 1.0.2 before 1.0.2h allows remote attackers to obtain sensitive information from process stack memory or cause a denial of service (buffer over-read) via crafted EBCDIC ASN.1 data. 

  * CVE-2016-7056—A timing attack flaw was found in OpenSSL 1.0.1u and before that could allow a malicious user with local access to recover ECDSA P-256 private keys. 

  * CVE-2017-3735—While parsing an IPAddressFamily extension in an X.509 certificate, it is possible to do a one-byte overread. This would result in an incorrect text display of the certificate. This bug has been present since 2006 and is present in all versions of OpenSSL before 1.0.2m and 1.1.0g. 

  * CVE-2021-23840—Calls to EVP_CipherUpdate, EVP_EncryptUpdate and EVP_DecryptUpdate may overflow the output length argument in some cases where the input length is close to the maximum permissable length for an integer on the platform. In such cases the return value from the function call will be 1 (indicating success), but the output length value will be negative. This could cause applications to behave incorrectly or crash. OpenSSL versions 1.1.1i and below are affected by this issue. Users of these versions should upgrade to OpenSSL 1.1.1j. OpenSSL versions 1.0.2x and below are affected by this issue. However OpenSSL 1.0.2 is out of support and no longer receiving public updates. Premium support customers of OpenSSL 1.0.2 should upgrade to 1.0.2y. Other users should upgrade to 1.1.1j. Fixed in OpenSSL 1.1.1j (Affected 1.1.1-1.1.1i). Fixed in OpenSSL 1.0.2y (Affected 1.0.2-1.0.2x). 

  * CVE-2021-3711—In order to decrypt SM2 encrypted data an application is expected to call the API function EVP_PKEY_decrypt(). Typically an application will call this function twice. The first time, on entry, the "out" parameter can be NULL and, on exit, the "outlen" parameter is populated with the buffer size required to hold the decrypted plaintext. The application can then allocate a sufficiently sized buffer and call EVP_PKEY_decrypt() again, but this time passing a non-NULL value for the "out" parameter. A bug in the implementation of the SM2 decryption code means that the calculation of the buffer size required to hold the plaintext returned by the first call to EVP_PKEY_decrypt() can be smaller than the actual size required by the second call. This can lead to a buffer overflow when EVP_PKEY_decrypt() is called by the application a second time with a buffer that is too small. A malicious attacker who is able present SM2 content for decryption to an application could cause attacker chosen data to overflow the buffer by up to a maximum of 62 bytes altering the contents of other data held after the buffer, possibly changing application behaviour or causing the application to crash. The location of the buffer is application dependent but is typically heap allocated. Fixed in OpenSSL 1.1.1l (Affected 1.1.1-1.1.1k). 

  * CVE-2021-3712—ASN.1 strings are represented internally within OpenSSL as an ASN1_STRING structure which contains a buffer holding the string data and a field holding the buffer length. This contrasts with normal C strings which are repesented as a buffer for the string data which is terminated with a NUL (0) byte. Although not a strict requirement, ASN.1 strings that are parsed using OpenSSL's own "d2i" functions (and other similar parsing functions) as well as any string whose value has been set with the ASN1_STRING_set() function will additionally NUL terminate the byte array in the ASN1_STRING structure. However, it is possible for applications to directly construct valid ASN1_STRING structures which do not NUL terminate the byte array by directly setting the "data" and "length" fields in the ASN1_STRING array. This can also happen by using the ASN1_STRING_set0() function. Numerous OpenSSL functions that print ASN.1 data have been found to assume that the ASN1_STRING byte array will be NUL terminated, even though this is not guaranteed for strings that have been directly constructed. Where an application requests an ASN.1 structure to be printed, and where that ASN.1 structure contains ASN1_STRINGs that have been directly constructed by the application without NUL terminating the "data" field, then a read buffer overrun can occur. The same thing can also occur during name constraints processing of certificates (for example if a certificate has been directly constructed by the application instead of loading it via the OpenSSL parsing functions, and the certificate contains non NUL terminated ASN1_STRING structures). It can also occur in the X509_get1_email(), X509_REQ_get1_email() and X509_get1_ocsp() functions. If a malicious actor can cause an application to directly construct an ASN1_STRING and then process it through one of the affected OpenSSL functions then this issue could be hit. This might result in a crash (causing a Denial of Service attack). It could also result in the disclosure of private memory contents (such as private keys, or sensitive plaintext). Fixed in OpenSSL 1.1.1l (Affected 1.1.1-1.1.1k). Fixed in OpenSSL 1.0.2za (Affected 1.0.2-1.0.2y). 

  * CVE-2021-4044—Internally libssl in OpenSSL calls X509_verify_cert() on the client side to verify a certificate supplied by a server. That function may return a negative return value to indicate an internal error (for example out of memory). Such a negative return value is mishandled by OpenSSL and will cause an IO function (such as SSL_connect() or SSL_do_handshake()) to not indicate success and a subsequent call to SSL_get_error() to return the value SSL_ERROR_WANT_RETRY_VERIFY. This return value is only supposed to be returned by OpenSSL if the application has previously called SSL_CTX_set_cert_verify_callback(). Since most applications do not do this the SSL_ERROR_WANT_RETRY_VERIFY return value from SSL_get_error() will be totally unexpected and applications may not behave correctly as a result. The exact behaviour will depend on the application but it could result in crashes, infinite loops or other similar incorrect responses. This issue is made more serious in combination with a separate bug in OpenSSL 3.0 that will cause X509_verify_cert() to indicate an internal error when processing a certificate chain. This will occur where a certificate does not include the Subject Alternative Name extension but where a Certificate Authority has enforced name constraints. This issue can occur even with valid chains. By combining the two issues an attacker could induce incorrect, application dependent behaviour. Fixed in OpenSSL 3.0.1 (Affected 3.0.0). 


### Security Fixes in C-Series M6 Server Firmware Release 4.3(4.242038)

#### Defect ID - CSCwk90710

Cisco UCS C-Series M6 servers are affected by vulnerabilities identified by the following Common Vulnerability and Exposures (CVE) IDs: 

  * CVE-2024-24853—Incorrect behavior order in transition between executive monitor and SMI transfer monitor (STM) in some Intel(R) Processor may allow a privileged user to potentially enable escalation of privilege via local access. 

  * CVE-2024-24980—Protection mechanism failure in some 3rd, 4th, and 5th Generation Intel(R) Xeon(R) Processors may allow a privileged user to potentially enable escalation of privilege via local access. 

  * CVE-2024-21829—Improper input validation in UEFI firmware error handler for some Intel® Processors may allow a privileged user to potentially enable escalation of privilege via local access. 

  * CVE-2024-21781—Improper input validation in UEFI firmware for some Intel® Processors may allow a privileged user to enable information disclosure or denial of service via local access. 

  * CVE-2023-43753—Improper conditions check in some Intel(R) Processors with Intel® Software Guard Extensions (Intel® SGX) may allow a privileged user to potentially enable information disclosure via local access. 

  * CVE-2024-24968—Improper finite state machines (FSMs) in hardware logic in some Intel® Processors may allow an privileged user to potentially enable a denial of service via local access. 

  * CVE-2024-23984—Observable discrepancy in RAPL interface for some Intel® Processors may allow a privileged user to potentially enable information disclosure via local access. 


### Security Fixes in C-Series M7 and M6 Server Firmware Release 4.3(4.241063)

#### Defect ID - CSCwk62266

Cisco UCS C-Series M7 and M6 servers are affected by the vulnerabilities identified by the following Common Vulnerability and Exposures (CVE) IDs: 

  * CVE-2024-6387—A race condition has been identified in the sshd service related to its signal handler. If a client fails to authenticate within the LoginGraceTime period (default is 120 seconds, previously 600 seconds in older OpenSSH versions), the sshd SIGALRM handler is triggered asynchronously. This handler, however, invokes several functions that are not safe to call from within a signal handler, such as syslog(). 


The affected third-party software component has been upgraded to a version that includes fixes for the vulnerability. Future versions of the product(s) will not be affected by this vulnerability. 

### Security Fixes in C-Series M5 Firmware Release 4.3(2.240077)

#### Defect ID - CSCwk62266

Cisco UCS C-Series M5 servers are affected by the vulnerabilities identified by the following Common Vulnerability and Exposures (CVE) IDs: 

  * CVE-2024-6387—A race condition has been identified in the sshd service related to its signal handler. If a client fails to authenticate within the LoginGraceTime period (default is 120 seconds, previously 600 seconds in older OpenSSH versions), the sshd SIGALRM handler is triggered asynchronously. This handler, however, invokes several functions that are not safe to call from within a signal handler, such as syslog(). 


The affected third-party software component has been upgraded to a version that includes fixes for the vulnerability. Future versions of the product(s) will not be affected by this vulnerability. 

### Security Fixes in C-Series M8 Server Firmware Release 4.3(4.241014) — None 

### Security Fixes in C-Series M5, M6, and M7 Firmware Release 4.3(4.240152) — None 

### Security Fixes in C-Series M5 Firmware Release 4.3(2.240053)

Defect ID - CSCwi59840

Cisco UCS M5 servers are affected by vulnerabilities identified by the following Common Vulnerability and Exposures (CVE) IDs: 

CVE-2023-48795—The SSH transport protocol with certain OpenSSH extensions, found in OpenSSH before 9.6 and other products, allows remote attackers to bypass integrity checks, such that some packets are omitted (from the extension negotiation message), and a client and server may consequently end up with a connection for which some security features have been downgraded or disabled, also known as Terrapin attack. 

This occurs because the SSH Binary Packet Protocol (BPP), implemented by these extensions, mishandles the handshake phase and use of sequence numbers. For example, when there is an effective attack against SSH's use of ChaCha20-Poly1305 (and CBC with Encrypt-then-MAC), the bypass occurs in chacha20-poly1305@openssh.com, (and if CBC is used, then the -etm@openssh.com MAC algorithms). 

### Security Fixes in C-Series M6 Firmware Release 4.3(2.240037)— None 

### Security Fixes in C-Series M7 and M6 Firmware Release 4.3(3.240043) — None

### Security Fixes in C-Series M7, M6, M5 Firmware 4.3(2.240009) — None

### Security Fixes in C-Series Firmware Release 4.3(2.230270)

The following security issue is resolved:

**Defect ID - CSCwh17053**

Cisco UCS C225 and C245 M6 servers are affected by vulnerabilities identified by the following Common Vulnerability and Exposures (CVE) IDs: 

**CVE-2023-20593** —An issue in Zen 2 CPUs, under specific microarchitectural circumstances, might allow an attacker to potentially access sensitive information. 

**Defect ID - CSCwh18140**

Cisco UCS C125 M5 servers are affected by vulnerabilities identified by the following Common Vulnerability and Exposures (CVE) IDs: 

**CVE-2023-20593** —An issue in Zen 2 CPUs, under specific microarchitectural circumstances, might allow an attacker to potentially access sensitive information. 

### Security Fixes in C-Series Firmware Release 4.3(2.230207)

The following security issues are resolved:

  * **Defect ID - CSCwe96259**

Cisco UCS C-series M6 servers are affected by vulnerabilities identified by the following Common Vulnerability and Exposures (CVE) IDs: 

CVE-2023-20228—This vulnerability is due to insufficient validation of user input. An attacker could exploit this vulnerability by persuading a user of an affected interface to click a crafted link. A successful exploit could allow the attacker to execute arbitrary script code in the browser of the targeted user or access sensitive, browser-based information. 

  * **Defect ID - CSCwf30460**

Cisco UCS C-series M6 servers are affected by vulnerabilities identified by the following Common Vulnerability and Exposures (CVE) IDs: 

  * CVE-2022-41804—Unauthorized error injection in Intel® SGX or Intel® TDX for some Intel® Xeon® Processors which may allow a privileged user to potentially enable escalation of privilege through local access. 

  * CVE-2022-40982—Information exposure through microarchitectural state after transient execution in certain vector execution units for some Intel(R) Processors may allow an authenticated user to potentially enable information disclosure through local access. 

  * CVE-2023-23908—Improper access control in some 3rd Generation Intel® Xeon® Scalable processors may allow a privileged user to potentially enable information disclosure through local access. 

  * CVE-2022-37343— Improper access control in the BIOS firmware for some Intel® Processors may allow a privileged user to potentially enable escalation of privilege through local access. 

  * **Defect ID - CSCwf30468**

Cisco UCS C-series M5 servers are affected by vulnerabilities identified by the following Common Vulnerability and Exposures (CVE) IDs: 

  * CVE-2022-40982—Information exposure through microarchitectural state after transient execution in certain vector execution units for some Intel® Processors may allow an authenticated user to potentially enable information disclosure through local access. 

  * CVE-2022-43505—Insufficient control flow management in the BIOS firmware for some Intel® Processors may allow a privileged user to potentially enable denial of service through local access. 


## Caveats

You can view the open issues, resolved issues, and security fixes using the [Cisco Bug Search Tool](https://bst.cloudapps.cisco.com/bugsearch). 

### **Resolved Caveats**

#### Resolved Caveats in Cisco UCS B-Series M5 5.4(0.260011) and C-Series M7, M6 Server Firmware Release 4.3(6.260017)

The following table lists the resolved caveats in this release:

Defect ID |  Description |  First Version Affected |  Resolved in Release  
---|---|---|---  
[CSCwr84583](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwr84583) |  On Cisco UCS C480 M6 servers with firmware 4.3(2.240009), secure syslog communication from Cisco IMC to remote syslog servers (Graylog/rsyslog) intermittently or continuously fails due to TLS handshake errors and session drops.  This issue is resolved. |  4.3(2.240009) |  4.3(6.260017) 4.3(2.260007)  
[CSCws44775](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCws44775) |  On Cisco UCS C220 M7 servers running firmware 4.3(6.250101), Cisco IMC may raise alarms such as _Storage controller MRAID inoperable: controller unresponsive_ and _Storage Virtual Drive is inoperable: Check storage controller, or reseat the storage drive,_ indicating possible loss of contact with the storage controller. This issue can occur in various hardware configurations.  Restarting the Cisco IMC will clear the alarms. This issue is resolved. |  4.3(6.250121) |  4.3(6.260017)  
[CSCwi71153](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwi71153) |  On Cisco UCS C-Series M6 servers, a kernel panic in the BMC OS causes the BMC to become unresponsive. The watchdog timer detects this and resets the BMC to recover its functionality. The server OS is not impacted by this process. Only management functions provided by the BMC—such as remote management, virtual media, and hardware monitoring—will be temporarily unavailable while the BMC restarts.  This issue is resolved. |  4.2(3b) |  4.3(6.260017) 6.0(1.250192)  
[CSCwr21671](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwr21671) |  On Cisco UCS B200 M5 servers with an LSI 12G RAID controller running Windows Server 2019 (megasas2 driver), an L2/L3 cache error may be detected on the RAID controller. This causes the storage controller to become inoperable, and Cisco IMC is unable to detect the controller.  This issue is resolved. |  4.2(3e) |  5.4(0.260011)  
  
#### Resolved Caveats in C-Series M5 Server Firmware Release 4.3(2.260007)

The following table lists the resolved caveats in C-Series M5 firmware release 4.3(2.260007): 

Defect ID |  Description |  First Version Affected |  Resolved in Release  
---|---|---|---  
[CSCwm03289](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwm03289) |  On Cisco UCS C-Series M5 servers, upgrading Cisco IMC to release version 4.3(2.240009) causes SNMPv3 to stop working for FAN and PSU Object Identifier (OIDs). SNMPv2 continues to function correctly. The affected OIDs are under the parent OID 1.3.6.1.4.1.9.9.719.1.15.  This issue is resolved. |  4.3(2.240002) |  4.3(2.260007)  
[CSCwr84583](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwr84583) |  On Cisco UCS C480 M5 servers with firmware 4.3(2.240009), secure syslog communication from Cisco IMC to remote syslog servers (Graylog/rsyslog) intermittently or continuously fails due to TLS handshake errors and session drops.  |  4.3(2.240009) |  4.3(2.260007) 4.3(6.260017)  
  
#### Resolved Caveats in Cisco UCS X-Series M7 5.4(0.260001) and C-Series M8, M7 Server Firmware Release 4.3(6.260003)

The following table lists the resolved caveats in this release:

Defect ID |  Description |  First Version Affected |  Resolved in Release  
---|---|---|---  
CSCws30219 |  Cisco UCS M7 servers are susceptible to host lockups triggered by ECC (Error Correcting Code) memory events. This issue is specifically related to how the server’s BIOS interacts with the EFI (Extensible Firmware Interface) during error conditions. During these events, the BIOS does not correctly retrieve a required variable, causing EFI to return an invalid parameter. As a result, the operating system is unable to continue normal operation and freezes without logging any errors. When this occurs, the host becomes unresponsive and KVM (keyboard, video, mouse) input is not accepted.  Single-bit ECC errors—while not logged due to DDR5 specifications—can trigger this condition, resulting in complete loss of host responsiveness.  |  X-Series M7: 5.4(0.250048) C-series M7: 4.3(6.250053) |  X-Series M7: 5.4(0.260001), 6.0(1.250179) C-series M7: 4.3(6.260003), 6.0(1.250192)  
CSCwr46765 |  On Cisco UCS C-Series M8 servers with Trimode M1 RAID controllers, if the BMC time is yet to be synced with the BIOS and the controller has a certificate with a newer date, the CIMC may wrongly display a critical alarm to reseat or replace the controller. This happens because the controller cannot authenticate (SPDM Authentication Failure), not due to hardware failure. The error message should instead mention an authentication issue.  To resolve this, set the correct date and time on the CIMC manually, or wait for it to sync, so the controller can be recognized. |  4.3(6.250040) |  4.3(6.260003)  
  
#### Resolved Caveats in C-Series M5 Server Firmware Release 4.3(2.250063)

The following table lists the resolved caveats in C-Series M5 firmware release 4.3(2.250063): 

Defect ID |  Description |  First Version Affected |  Resolved in Release  
---|---|---|---  
CSCwr05546 |  On Cisco UCS C240 M5 servers running Windows Server 2022 with firmware version 4.3(2.250016), a Blue Screen of Death (BSOD) may occur referencing the ITSAS35.SYS driver module. This module is associated with the Cisco 12G Modular SAS Host Bus Adapter (HBA), and the crash results in an OS-triggered reboot.  |  4.3(2.250016) |  4.3(2.250063)  
CSCwq53978 |  On Cisco UCS C240 M5 servers, uploading an external certificate using the CLI causes the Security Management tab in the CIMC GUI to become inaccessible. Attempts to upload an external certificate through the CIMC GUI fail with the error: **External Certificate upload failed**. After uploading via the CLI, the Security Management tab no longer loads, the Host Upgrade Utility (HUU) fails to load, and there is a failure to contact the LDAP server.  |  4.2(2a) |  4.3(2.250063)  
  
#### Resolved Caveats in Cisco UCS C-Series M7 Server Firmware Release 4.3(6.250117)

The following table lists the resolved caveats in this release:

Defect ID |  Description |  First Version Affected |  Resolved in Release  
---|---|---|---  
CSCwr75284 |  On Cisco UCS C220 M7 servers with Intel processors, enabling immersion cooling mode may trigger frequent soft PSOC faults, which causes the host power state to become locked. When this happens, you cannot change the server’s power state from either the web interface or the IMM. This behavior does not occur when the servers use standard air cooling.  To avoid this problem in immersion cooling mode, the system has been updated so that soft PSOC faults no longer lock the host power.  |  4.3(6.250053) |  4.3(6.250117)  
  
#### Resolved Caveats in Cisco UCS X-Series M8 5.4(0.250105) and C-Series M6 4.3(6.250101) Server Firmware Release 

The following table lists the resolved caveats in this release:

Defect ID |  Description |  First Version Affected |  Resolved in Release  
---|---|---|---  
CSCwq61388 |  On Cisco UCS C-Series M6 servers running CIMC 4.3.5 or later, enabling VMD in BIOS with multiple NVME drives can cause storage subsystem initialization to exceed 15 minutes, leading to Intersight Server Profile deployment failures.  The likelihood of encountering this issue increases with the number of drives installed. Disabling VMD or reducing the number of drives can resolve the issue. |  4.3(5.250001) |  4.3(6.250101) 5.4(0.250105)  
CSCwr24516 |  On Cisco UCS X210c M8, some servers may not power on or start up if they contain a hardware part (inductor) from a specific vendor. This issue causes a startup failure, and the server will remain off even when you try to turn it on. The problem is caused by a difference in how the new hardware part works, but it can be fully resolved by updating the board to the latest VR (Voltage Regulator) image, which is designed to support this new component.  Update the server with the latest VR image, clear any power on error, and turn the server off and on again. If the server still does not start, contact Cisco TAC for further assistance.  |  6.0(1.250126) |  4.3(6.250101) 5.4(0.250105) 6.0(1.250162) 6.0(1.250174)  
CSCwr31522 |  On Cisco UCS X-Series M8 servers, if the BMC firmware is downgraded from 6.0.1. to 5.4.0. and a warm reset is performed, the host may fail to fully boot. This issue only occurs when the server firmware is downgraded from 6.0.1.* to 5.4.0.Servers originally running 5.4.0. are unaffected.To resolve this, power cycle the host or upgrade the BMC to the latest firmware version.  |  5.4(0.250076) |  4.3(6.250101) 5.4(0.250105)  
CSCwq58890 |  The firmware for the Cisco UCS VIC 15000 series adapters is updated to fix a rare, intermittently seen memory issue and to ensure more robust and consistent operation across diverse memory types and configurations.  |  **Note** |  If you continue to experience any memory error, then contact Cisco TAC.  
---|---  
X-series: 6.0(1.250120) B-series: 6.0(1.250126) C-series: 6.0(1.250127) |  4.3(6.250101) 5.4(0.250105) 6.0(1.250122) 6.0(1.250127) 6.0(1.250131)  
  
#### Resolved Caveats in Cisco UCS C-Series M8 Server Firmware Release 4.3(5.250045)

The following table lists the resolved caveats in this release:

Defect ID |  Description |  First Version Affected |  Resolved in Release  
---|---|---|---  
CSCwp21596 |  On Cisco UCS C225 M8 servers, after upgrading the Solidigm NVMe drive firmware (non-UCS), the CPU may become unresponsive for a prolonged period with no automatic recovery. This hang typically occurs after a fatal CPU error, which can be triggered during device hotplug events or I/O malfunctions. This is an edge case that requires a specific combination of conditions to occur.  If the system hangs after the firmware upgrade, switch the system off and then back on (power cycle) to restore normal operation. |  4.3(5.250033) |  4.3(5.250045)  
  
#### Resolved Caveats in Cisco UCS C-Series M8 Server Firmware Release 4.3(6.250060)

The following table lists the resolved caveats in this release:

Defect ID |  Description |  First Version Affected |  Resolved in Release  
---|---|---|---  
CSCwq74490 |  On the Cisco UCS C245 M8 platform with AMD EPYC 9655 processors, fully loaded NVIDIA L4 GPUs experience random PCIe link width downgrades on different slots when running the Linux Rebooter Stress test. The affected slots change after actions such as an AC power cycle or HUU update; for example, if slots 2 and 6 are downgraded initially, other slots may be downgraded after these actions. This results in GPUs operating at reduced speeds in the OS environment.  |  4.3(6.250053) |  4.3(6.250060)  
  
#### Resolved Caveats in C-Series M5 Server Firmware Release 4.3(2.250045)

The following table lists the resolved caveats in C-Series M5 firmware release 4.3(2.250045): 

Defect ID |  Description |  First Version Affected |  Resolved in Release  
---|---|---|---  
CSCwp05235 |  On Cisco UCS C240 M5 servers running firmware version 4.3(2.250016), CIMC management becomes unavailable during a CIMC reboot caused by an out-of-memory (OOM) condition. The CIMC recovers automatically, and the data plane is not affected.  |  4.3(2.250016) |  4.3(2.250045)  
CSCwp25032 |  On Cisco UCS C220 M5 servers running CIMC version 4.3(2.240077), modifying the Ethernet Adapter Policy settings (RX Ring Queue, interrupt, and RX/TX size) and attaching it to a LAN Connectivity Policy allows the server profile to deploy successfully. However, after a few minutes, the server profile status changes to Inconsistent State because the endpoint configuration no longer matches the deployed configuration. Additionally, the LAN Connectivity Policy reports "Out-Of-Sync" due to this configuration mismatch. Changes to Ethernet Adapter Policy settings were made as per [_Cisco UCS VIC 1400 Series Best Practices in Ethernet Fabric White Paper - Cisco_](https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/unified-computing-system-adapters/white-paper-c11-744754.html).  |  4.3(2.240077) |  4.3(2.250045)  
  
#### Resolved Caveats in C-Series M8 Server Firmware Release 4.3(5.250043)

The following table lists the resolved caveats in this release:

Defect ID |  Description |  First Version Affected |  Resolved in Release  
---|---|---|---  
CSCwp18182 |  On Cisco UCS C225 M8 servers with NVMe drives and Bluefield-3 NICs, fan speeds were at 37% PWM when running firmware version 4.3(5.250030). After upgrading to firmware version 4.3(5.250033), fan speeds increased to 100% PWM.  This issue is not triggered by any specific action and does not impact server functionality. However, the elevated fan speeds result in significantly higher power consumption and noise levels.  This issue has now been addressed in the latest firmware. |  4.3(5.250033) |  4.3(5.250043)  
  
#### **Resolved Caveats in X-Series M8 5.4(0.250052) and C-Series M8 4.3(6.250053) Server Firmware Release**

The following table lists the resolved caveats in this release:

Defect ID |  Description |  First Version Affected |  Resolved in Release  
---|---|---|---  
CSCwo67388 |  On Cisco UCS X210c M8, C220 M8, and C240 M8 servers in Intersight Managed or Standalone mode, the Password History feature in Local User Policy (LUP) does not enforce the password reuse restriction during user creation or SP redeployment, allowing the same password to be accepted even when the Password History Count is set between 1 and 5.  |  4.3(6.250012) |  5.4(0.250052) 4.3(6.250053)  
  
#### Resolved Caveats in C-series M5 Server Firmware Release 4.3(2.250037)

The following table lists the resolved caveats in C-Series M5 firmware release 4.3(2.250037): 

Defect ID |  Description |  First Version Affected |  Resolved in Release  
---|---|---|---  
CSCwn97625 |  On Cisco UCS C240 M5 servers with DCPMM (Intel Optane DC Persistent Memory Modules), enabling DIMM blocklisting caused memory policies to go out of sync after a server reboot.  This issue occurred because, although SMBIOS (System Management BIOS) detects DCPMM and indicates DIMM blocklisting should be disabled, the configuration was not retained after a server reboot, causing the SP to report an out-of-sync state.  This problem is specific to setups with DCPMM and does not affect servers without DCPMM. With this fix, DIMM blocklisting is now automatically disabled on setups with DCPMM, ensuring that memory policies remain functional after server reboots.  |  4.3(2.240107) |  4.3(2.250037)  
CSCwo57529 |  On Cisco UCS C220 M5 servers, SMTP (Simple Mail Transfer Protocol) fails to send alert emails (e.g., for PSU or disk removal) after upgrading the firmware to 4.3(2.240053) or 4.3(2.250021). This issue is not limited to these firmware versions.  Test emails work, but no SMTP activity is triggered during alerts. There is no workaround for this issue. This issue is resolved now. |  4.3(2.240053) |  4.3(2.250037)  
CSCwo96142 |  Cisco UCS C-Series M5 servers are being flagged by vulnerability scanners for using SHA-1 algorithms and deprecated `ssh-rsa` and `ssh-dss` host keys, potentially exposing security risks.  The SHA-1 algorithm and the `ssh-rsa`/`ssh-dss` host keys have been removed in this release to ensure compliance with current security standards.  Before this fix, the issue could be mitigated by disabling SSH access through Intersight. |  4.2(3b) 4.3(2.250016) |  4.3(2.250037)  
CSCwo99876 |  On Cisco UCS C-Series C220 M5 servers, after upgrading to firmware 4.3(2.250016) or 4.3(2.250021), the BMC_DIE_TEMP sensor crosses the Upper Critical (UC) threshold but does not appear in the CIMC WebUI Sensor list or generate alarms in CIMC or Intersight. However, the sensor is visible in IPMI and Redfish.  This issue occurs during high CPU usage when RackFanControl is not actively cooling the server.  Downgrading to 4.3(2.240077) resolves the issue but is not ideal if 4.3(2.250016) includes a required fix. This issue is not limited to these firmware versions or server model.  |  4.3(2.250016) |  4.3(2.250037)  
  
#### Resolved Caveats in C-Series M8 and M7 Server Firmware Release 4.3(6.250044)

The following table lists the resolved caveats in this release:

Defect ID |  Description |  First Version Affected |  Resolved in Release  
---|---|---|---  
CSCwm45755 |  M.2 SATA disks connected to storage controllers on the MSTOR-RAID slot are not being detected during the installation of Windows Server 2025.  The affected storage controllers are:

  * UCS-M2-HWRAID2 on Cisco UCS C220/C240 M8 Servers
  * UCSC-M2RM-M8 on Cisco UCS C220/C240 M8 Servers
  * UCSC-M2RR-240M8 on Cisco UCS C240 M8 Servers

This issue is specific to Windows Server 2025 for the storage controllers mentioned above. These M.2 disks, however, are detected and fully functional in Windows Server 2022 or other operating systems. |  4.3(6.250039) |  4.3(6.250044)  
CSCwn99720 |  On Cisco UCS C-Series M8 servers with Intel processors and an R1S CPU configured in a single-CPU setup on the 2-socket platform, Intel SGX remains disabled even after being enabled in the BIOS. This issue does not occur with a dual CPU configuration.  |  4.3(6.250039) |  4.3(6.250044)  
CSCwn51498 |  On Cisco UCS C220 and C240 M8 servers, raw OEM SEL records are logged in the CIMC SEL during the boot and shutdown of Windows Server 2025. This does not impact system functionality or performance.  |  4.3(6.250039) |  4.3(6.250044)  
CSCwn44614 |  On Cisco UCS C220 and C240 M8 servers, enabling Pre-Boot DMA Protection may cause slowness when downloading the OS ISO image via HTTP/HTTPS boot. This issue occurs during the pre-boot process with this configuration.  |  4.3(6.250039) |  4.3(6.250044)  
  
#### Resolved Caveats in C-Series M8, M7, and M6 Server Firmware Release 4.3(5.250033)

The following table lists the resolved caveats in this release:

Defect ID |  Description |  First Version Affected |  Resolved in Release  
---|---|---|---  
CSCwo84654 |  On Cisco UCS C225 M8 servers, PCIe Gen5-capable NICs installed in Riser slots 1C, 1B, or 3C may have PCIe in downgraded Gen4 speed instead of the supported Gen5 after upgrading to Release 4.3(5.250030).  This affects performance but does not impact reliability. The downgraded PCIe link speed is visible in both the BIOS and the operating system during boot. The issue occurs without any specific trigger.  There is no workaround available. Upgrading the firmware resolves the issue. |  4.3(5.250030) |  4.3(5.250033)  
  
#### **Resolved Caveats in X-Series M8 5.4(0.250037) and 5.4(0.250035), M7 5.4(0.250035), M6 5.4(0.250033) and B-Series M6, M5 5.4(0.250034) Server Firmware Release**

The following table lists the resolved caveats in this release:

Defect ID |  Description |  First Version Affected |  Resolved in Release  
---|---|---|---  
CSCwj61708 |  When performing a warm reboot of multiple servers in a scale-setup of 160 servers and high PV count of greater than 64K in Cisco UCS FI domain, secure boot adapters may not restart instantly under certain situations. This was observed in a scale setup where simultaneous warm reboot of 22 blades across three chassis was initiated. Some blades with Cisco UCS VIC 15000 series secure boot adapters failed to boot from the SAN after a soft reboot. These adapters execute a cleanup process with the Fabric Interconnects to maintain system integrity, which needs to be finished before the server BIOS can recognize the adapters. This issue arises specifically under conditions of very high PV count or exceptionally high CPU utilization on the FI. During these instances, if the server BIOS finalizes the boot sequence before the secure boot adapters finish the cleanup, the adapters may fail to be detected. Consequently, the server may not successfully boot from the SAN. This issue is observed in configurations using Cisco UCS blade servers equipped with Cisco UCS VIC 15000 series adapters.  |  5.2(2.240053) |  5.4(0.250033)  
CSCwn52355 |  On Cisco UCS B200-M5 servers, In-Band IP address management fails over between FI-A and FI-B every 30 seconds, impacting Application Centric Infrastructure (ACI). Using Out-Of-Band IP addresses or resetting the system can help.  |  5.1(0.230075) |  5.4(0.250034)  
CSCwj60167 |  Cisco UCS B-Series servers may experience BMC reboots from kernel panics due to "hung tasks or Oops," affecting only the management plane. The data plane stays functional, but blades become temporarily unmanageable. Fault code F1681 indicates CIMC connectivity loss, confirmed by SEL logs showing a watchdog reset. The blade automatically recovers after an unexpected BMC reboot.  |  5.2(2.240053) 5.2(0.230100) 4.2(3j) |  5.4(0.250034) 5.3(0.250021)  
CSCwk71382 |  Some servers disconnect from Intersight after a Device Connector update, remaining online but inaccessible. This affects multiple Device Connector versions, with no known bug. Customers can resolve the issue by generating a tech-support bundle from the FI console or reseating the server.  |  5.2(0.230092) 5.2(0.230040) |  5.4(0.250033) 5.4(0.250034)  
CSCwn28051 |  Cisco UCS X210c M6 servers in Intersight Managed Mode show an alert: "Intel PCH Secure Fuse Verification has failed on motherboard." The servers function normally, and the alert can typically be cleared by resetting the CIMC or CMOS.  |  5.2(2.240053) |  5.4(0.250033)  
CSCwo05709 |  Intersight Managed Mode (IMM) does not support Non-Maskable Interrupt (NMI) diagnostics on Cisco UCS B200 M5, M6, and X210c M6, M7 servers, whether using Private Virtual Appliance (PVA), Connected Virtual Appliance (CVA), or Software as a Service (SaaS) models. NMI diagnostics are crucial for resolving OS freezes.  The fix is a feature enhancement. |  — |  5.4(0.250033) 5.4(0.250034) 5.4(0.250035)  
CSCwo15215 |  Cisco UCS X210c M6 servers connected to Intersight may remain in a disconnected state, while DC and CIMC continue running. Users see the message: "Connection to Server was lost X hours/days ago. Data may not be relevant at this point. View Target Details." Despite the disconnection, CIMC remains operational, enabling connections and command execution. Contact Technical Assistance Center for a reboot or reset the server slot to restore manageability.  |  5.4(0.250011) |  5.4(0.250033)  
CSCwo40461 |  Cisco UCS X210c M7 servers encounter shallow discovery issues due to out-of-memory (OOM) conditions in the Cisco Integrated Management Controller (CIMC). The CIMC automatically recovers post-OOM, enabling the discovery process to complete. Logs confirm CIMC reset due to OOM conditions on UCSX-210C-M7 hardware with BMC Firmware version 5.2(0.230041), though the issue is not restricted to this version.  |  5.2(0.230041) |  5.4(0.250035)  
  
#### Resolved Caveats in C-Series M8 Firmware Release 4.3(6.250040) and 4.3(6.250039)

The following table lists the resolved caveats in this release:

Defect ID |  Description |  First Version Affected |  Resolved in Release  
---|---|---|---  
CSCwn48372 |  In Cisco UCS M8 servers, setting the BIOS token to Auto for CbsCmnEfficiencyModeEnRs results in the value being incorrectly displayed as High Performance Mode. This is a display issue and there is no functional impact. Intersight sends the value as Auto, and BMC correctly sets the default performance mode.  |  4.3(5.240021) |  4.3(6.250040)  
CSCwo60509 |  In Cisco UCS C240 M8 servers, if the controller is attached in No Raids system and U.3 NVMe drives are to be used under the controller, then either perform Backplane Reset to Default or manually change backplane management to controller-attached.  |  4.3(6.250026) |  4.3(6.250039)  
  
#### Resolved Caveats in C-Series M8, M7, and M6 Server Firmware Release 4.3(5.250030)

The following table lists the resolved caveats in C-Series M8, M7, and M6 4.3(5.250030) server firmware release: 

Defect ID |  Description |  First Version Affected |  Resolved in Release  
---|---|---|---  
CSCwk33013 |  Cisco UCS M5 servers are experiencing an `EFI Secure Boot Key Error [0x5304]`. This issue is caused when the Secure boot keys (DB, DBx, PK, KEK) are set to zero file size.  |  4.3(2.240090) |  4.3(5.250030)  
CSCwm67863 |  In Cisco UCS servers running RHEL 9.4, upgrading the BIOS and switching the boot mode from non-secure to secure causes the host to power off.  |  4.3(5.250001) |  4.3(5.250030)  
CSCwn48372 |  In Cisco UCS M8 servers, setting the BIOS token to "Auto" for CbsCmnEfficiencyModeEnRs results in the value being displayed as High Performance Mode.  |  4.3(5.240021) |  4.3(5.250030)  
CSCwn85649 |  The Ethernet Network Adapter I710, utilizing the i40e driver, repeatedly displays the message: `i40e 0000:17:00.0: ARQ: Unknown event 0x0000 ignored.` |  4.3(4.240152) |  4.3(5.250030)  
CSCwn62845 |  Cisco UCS C220 M7 servers report a Storage Raid Battery MRAID degradation, suggesting battery or controller issues. |  4.3(4.242038) |  4.3(5.250030)  
CSCwn65087 |  Upgrading to server firmware 4.3(2.240090) causes HTTP/HTTPS access loss if IP filtering entries exceed three. Manually re-enable HTTP/HTTPS to restore access.  |  4.3(2.240090) |  4.3(5.250030)  
  
#### Resolved Caveats in C-series M5 Server Firmware Release 4.3(2.250021)

The following table lists the resolved caveats in C-Series M5 firmware release 4.3(2.250021): 

Defect ID |  Description |  First Version Affected |  Resolved in Release  
---|---|---|---  
CSCwn97854 | Server Profile activation fails on Cisco UCS C240 M5 server when upgrading from 4.3(2.240107) to 4.3(2.250016). | 4.3(2.250016) | 4.3(2.250021)  
  
#### Resolved Caveats in X-Series M8, M7, M6 5.3(0.250021) and B-Series M6, M5 5.3(0.250021) Server Firmware Release 

The following table lists the resolved caveats in X-Series M8, M7, M6 5.3(0.250021) and B-Series M6, M5 5.3(0.250021) server firmware release: 

Defect ID |  Description |  First Version Affected |  Resolved in Release  
---|---|---|---  
CSCwj60167 |  UCS-B servers may experience BMC reboots from kernel panics due to "hung tasks or Oops," affecting only the management plane. The data plane stays functional, but blades become temporarily unmanageable. Fault code F1681 indicates CIMC connectivity loss, confirmed by SEL logs showing a watchdog reset.  |  4.3(2c) |  5.3(0.250021)  
CSCwm13829 |  On Cisco UCS X210c M6 or M7 servers with a UCSX-X10C-RAIDF RAID controller, a BBU fault may occur, indicated by Safety Status Register `0xf000` in logs. This suggests a corrupted voltage reading, marking the BBU as bad and potentially needing replacement. To resolve, access the RAID setup during boot, reset to factory defaults, confirm, and save changes.  |  5.2(0.230092) |  5.3(0.250021) 5.0(4i)  
  
#### Resolved Caveats in X-Series M8, M7, M6 5.3(0.250001) and B-Series M6, M5 5.3(0.250001) Server Firmware Release 

The following table lists the resolved caveats in X-Series M8, M7, M6 5.3(0.250001) and B-Series M6, M5 5.3(0.250001) server firmware release: 

Defect ID |  Description |  First Version Affected |  Resolved in Release  
---|---|---|---  
CSCwm72893 |  Under rare conditions, Cisco UCS VIC adapter may experience a firmware hang due to a software anomaly in the embedded CPU (eCPU), leading to a watchdog timeout and Non-Maskable Interrupt (NMI). This can result in temporary storage connectivity loss. The latest firmware update addresses this issue by enhancing error-handling mechanisms to prevent such occurrences.  |  4.2(3i) |  5.3(0.250001)  
CSCwm36266 |  In certain conditions, after a watchdog reset or kernel panic, the blade IOM may incorrectly set the blade to Safe Mode, causing fans to spin at full speed.  This issue occurs when the CIMC kernel experiences a panic, and before rebooting completes, the IOM misidentifies the CIMC capabilities, leading to an incorrect state. This state persists even after rebooting the CIMC or the blade, resulting in elevated fan speeds. The issue is observed with Cisco UCS B200 M6 blade servers and requires an update to ensure proper IOM communication and blade state management.  |  4.2(3b) |  5.3(0.250001)  
  
#### Resolved Caveats in X-Series M7 5.2(2.240080) and M6 5.2(2.240078) Server Firmware Release 

The following table lists the resolved caveats in X-Series M7 5.2(2.240080) and M6 5.2(2.240078) firmware release: 

Defect ID |  Description |  First Version Affected |  Resolved in Release  
---|---|---|---  
CSCwm26679 |  The disk scrub process fails due to faulty drives in the server’s controller and displays the following error message:
    
    
    Cannot complete Disk Scrub

To resolve this, remove the faulty disk and then perform the disk scrub again. |  5.2(2.240053) |  5.2(2.240080) 5.2(2.240078)  
CSCwm04776 |  Optimized the disk scrub process timings when initiated via HSU or Redfish. Previously, the process required approximately 25 minutes to complete.  |  5.2(2.240053) |  5.2(2.240080) 5.2(2.240078)  
  
#### Resolved Caveats in X-Series Firmware Release 5.3(0.240016)

The following table lists the resolved caveats in X-Series firmware release 5.3(0.240016)

Defect ID |  Description |  First Release Affected  
---|---|---  
CSCwm67631 |  This issue occurs with UCS Blade servers equipped with AMD® processors that are fully populated with 64GB or higher DIMMs and have all drives installed, if they have not been powered on previously.  After updating the BMC and BIOS, clicking Power Off followed by Reset CMOS may cause a failure where the server remains powered off, even after a Redfish power-on command.  |  5.3(99.240008)  
CSCwm06766 |  The Cisco UCS X410c M7 powers off unexpectedly and does not power back on due to a power-lock issue.  Attempting to turn on the server via Cisco Intersight results in a failure with the error message: 
    
    
    Invoke the Server Power On
    
    
    Status - Failed
    
    
    The operation has timed out. Please check issues related to connectivity/target entity and retry.

|  5.2(0.230127)  
  
#### Resolved Caveats in X-series M7 Server Firmware Release 5.2(2.240074)

Defect ID |  Description |  First Release Affected  
---|---|---  
CSCwk37506 |  When Cisco UCS servers with 15000 series adapters have multiple paths for SANboot configured, and one path has issues in discovering the LUN while another path is successful, the clean-up done by fnic driver causes crash when the OS is loaded. This issue is resolved.  |  5.2(0.230092)  
  
#### Resolved Caveats in X-Series M6 5.2(2.240073) Firmware Release — None 

#### Resolved Caveats in X-Series M6 and M7 Firmware Release 5.2(2.240053)

The following caveats are resolved in Release 5.2(2.240053): 

Defect ID  |  Description |  First Bundle Affected   
---|---|---  
CSCwf13106 |  Firmware upgrades on Cisco UCS X210c M6 servers were halted due to a Cisco IMC crash, delaying the process for up to 8 hours with the message: 
    
    
    Waiting for firmware upgrade to complete. Trying to connect to the device. Check after some time.

Resetting the server restored communication with Cisco IMC and allowed the upgrade to complete. |  5.0(1b)  
CSCwj07992 |  The discovery issue with the 8th Cisco UCSX-210C-M7 server was resolved by changing minimum and maximum power values to match hardware specifications.  |  5.1(1.230052)  
  
#### Resolved Caveats in X-Series M7 and M6 Server Firmware Release 5.2(1.240010) — None

#### Resolved Caveats in X-Series M7 Firmware Release 5.2(0.230127)

The following table lists the resolved caveats in X-Series M7 firmware release 5.2(0.230127)

Defect ID | Description | First Bundle Affected  
---|---|---  
CSCwh26280 |  On Cisco UCS X210c M7 servers, when IPMI tool sends a query to the out-of-band (OOB) IP address for the server, it takes more than 30 seconds to receive a response. This delay causes monitoring tools to display an error because the expected response time in less than 30 seconds.  |  5.1(0.230075)  
  
#### Resolved Caveats in X-Series M7 Firmware Release 5.2(0.230092)

The following table lists the resolved caveats in X-Series M7 firmware release 5.2(0.230092)

Defect ID | Description | First Bundle Affected  
---|---|---  
CSCwh28307 |  After upgrading the X210cM7 or X410c M7 servers to version 5.2(0.230041), VIC techsupport files were not included in the techsupport package.  |  5.1(0.230075)  
  
#### Resolved Caveats in X-Series M7 Firmware Release 5.2(0.230061)

The following table lists the resolved caveats in X-Series 410c M7 firmware release 5.2(0.230061)

Defect ID | Description | First Bundle Affected  
---|---|---  
CSCwh42695  |  Platform ID for Cisco UCS X410c M7 Compute Node appears incorrect in two boards as X210c M7 ID 0x84 instead of 0x85. |  5.2(0.230041)  
CSCwd97069 |  In Cisco UCS X410c M7 Compute Node, with PXE boot policy enable MK-TME and disable the CPU PA limit. Try to boot into the OS. It is observed that the Compute Node cannot boot into W2K22 and RHEL8.2.  |  5.2(0.230041)  
CSCwh10938 |  SPR PLR3 OOB MCC SKU S3 stepping fix is required for Cisco UCS X410c M7 Compute Node. |  5.2(0.230041)  
CSCwf99117 |  Optimized Power Mode token is enabled in Cisco UCS X410c M7 Compute Node. It is observed that C1E is disabled. |  5.2(0.230041)  
  
#### Resolved Caveats in X-Series M6 Firmware Release 5.2(0.230127)

The following table lists the resolved caveats in X-Series M6 firmware release 5.2(0.230127)

Defect ID | Description | First Bundle Affected  
---|---|---  
CSCwi50991 |  The Cisco UCS X210c M6 servers, operating on the server firmware version 5.2(0.230040), encountered a critical issue wherein the Watchdog Baseboard Management Controller (BMC) experienced persistent crashes, impeding server stability.  |  5.2(0.230040)  
  
#### Resolved Caveats in X-Series M6 Firmware Release 5.2(0.230040)

The following table lists the resolved caveats in X-Series M6 firmware release 5.2(0.230040)

Defect ID | Description | First Bundle Affected  
---|---|---  
CSCwe87623  |  In all models of M6 servers, it is observed that with every power cycle, there is latency in generic inventory Information update as a result HCL status appears Incomplete. The genericInventory mo entries get deleted and inserted completely. During this update of the inventory info, missing OS information results in momentary invalidation of HCL status until OS is booted.  |  5.0(2b)  
CSCwf23487  |  Server discovery fails after firmware upgrade for Cisco UCS X-Series M6 Compute Node. |  5.1(0.230054)  
  
#### Resolved Caveats in B-Series M6 and M5 Server Firmware Release 5.2(2.240080)

The following table lists the resolved caveats in B-Series M6 and M5 5.2(2.240080) firmware release: 

Defect ID |  Description |  First Version Affected |  Resolved in Release  
---|---|---|---  
CSCwm26679 |  The disk scrub process fails due to faulty drives in the server’s controller and displays the following error message:
    
    
    Cannot complete Disk Scrub

To resolve this, remove the faulty disk and then perform the disk scrub again. |  5.2(2.240051) |  5.2(2.240080)  
CSCwm04776 |  Optimized the disk scrub process timings when initiated via HSU or Redfish. Previously, the process required approximately 25 minutes to complete.  |  5.2(2.240051) |  5.2(2.240080)  
  
#### Resolved Caveats in B-Series M6 Firmware Release 5.2(2.240073) — None 

#### Resolved Caveats in B-Series M6 and M5 Firmware Release 5.2(2.240051) — None 

#### Resolved Caveats in B-Series M6 5.2(1.240010) and M5 5.2(0.230127) Firmware Release — None

#### Resolved Caveats in B-Series Firmware Release 5.2(0.230127) — None

#### Resolved Caveats in B-Series Firmware Release 5.2(0.230039)

The following table lists the resolved caveats in X-Series M6 firmware release 5.2(0.230039)

Defect ID | Description | First Bundle Affected  
---|---|---  
CSCwe00937  |  Cisco UCS B200 M6 servers respond to SSH requests but have Serial Over LAN (SOL) disabled. As hmac-sha1 are enabled for SSH, the CIMC IPs get flagged as vulnerable in the security scans.  |  4.2(2d)  
CSCwe19822  |  In all models of M5 servers, it is observed that CIMC reset occurs due to kernel crash and watchdog reset. |  4.2(2e)  
CSCwe87623 |  In all models of M6 servers, it is observed that with every power cycle, there is latency in generic inventory Information update as a result HCL status appears Incomplete. The genericInventory mo entries get deleted and inserted completely. During this update of the inventory info, missing OS information results in momentary invalidation of HCL status until OS is booted.  |  5.1(0.230069)  
CSCwf02413 |  For Cisco UCS B200 M6 server, Power Budget alert is observed on an unassociated server. Alert clears on its own if server is not associated with a server profile and if discovery is successful.  |  4.2(2d)  
  
#### Resolved Caveats in C-series M5 Server Firmware Release 4.3(2.250016)

The following table lists the resolved caveats in C-Series M5 firmware release 4.3(2.250016): 

Defect ID |  Description |  First Version Affected |  Resolved in Release  
---|---|---|---  
CSCwf93621 |  In Cisco UCS C240 M5SX and UCS HX240c M5SX servers, when the firmware is upgraded to the release 4.2(3d), discovery or association is failing with a faulty drive in the system.  |  4.2(3d) |  4.3(2.250016) 4.2(3j)  
CSCwm45280 |  In Cisco UCS C-series servers, Cisco UCS VIC adapter with low memory in Intersight mode is unable to reply to an adapter inventory request because the adapter is unable to create a process to handle the request.  |  4.2(3b) |  4.3(2.250016) 4.3(4.242066) 4.3(2.240107)  
CSCwm48655 |  PSU alerts are flapping on Cisco IMC and the the SEL logs are being populated with PSU error messages. |  4.3(3c) |  4.3(2.250016)  
CSCwn00366 |  Server discovery failures occur on Cisco UCS C-series servers in Intersight Managed Mode when only eNICs or only vHBAs are configured. This issue is caused due to a memory leak in the vniccfgd process, triggered by the palo_vnic_listtype() API call. Over a period of time, the memory leak accumulates, eventually reaching a threshold that leads to failures.  |  4.3(2.230207) |  4.3(2.250016) 4.3(5.250001)  
CSCwn56294 |  In Cisco UCS C220 M5 server, Cisco IMC reboots abruptly and watchdog reset the BMC due to Out of Memory (OOM) error. |  4.3(2.240053) |  4.3(2.250016)  
CSCwi95393 |  The UCSC-C220-M5SX server, running firmware version 4.2(3e) and managed by Intersight CVA version 1.0.9-615, displays random 32-character strings in the Product Name, Serial Number, and PID fields on the CIMC summary tab. This issue is resolved after rebooting the CIMC.  |  4.2(3e) |  4.3(2.250016) 4.2(3o)  
CSCwj68672 |  Cisco UCS 240 M6 servers is stuck during the booting process of hardware platform configuration and the server fails to deploy or activate the profile of the node.  |  4.3(2.230207) |  4.3(2.250016)  
CSCwm47183 |  Toshiba HDDs (Model MG06SCA800A) in C240-M6L servers with Cisco 12G SAS HBA are randomly marked for removal by Cohesity. Despite no CIMC log failures, Smartctl cannot retrieve data once marked. Cohesity logs report I/O errors and superblock read issues. Affects JBOD setups; reseating drives occasionally resolves it  |  4.3(2.240002) |  4.3(2.250016) 4.2(3o) 4.3(5.250001) 4.3(4.242066)  
  
#### Resolved Caveats in C-Series M8, M7, and M6 4.3(5.250001) Server Firmware Release 

The following table lists the resolved caveats in C-Series M8, M7, and M6 4.3(5.250001) server firmware release: 

Defect ID |  Description |  First Version Affected |  Resolved in Release  
---|---|---|---  
CSCwn42969 |  After power cycling or resetting a Cisco UCS server, NVME disk FRONT-NVME-2 may become inoperable when left idle for over 1.5 weeks or under minimal workload. If this issue occurs and the drive is inoperable, check your drive PID against Drive PIDs for NVME Disk FRONT-NVME Inoperable Issue - CSCwn42969. If listed, contact Cisco TAC for a replacement. If not listed, upgrade to firmware release 9CV10490.  |  4.3(5.240021) |  4.3(5.250001) 4.3(4.242066) 4.2(3n)  
CSCwm47183 |  Certain HDDs (model MG06SCA800A) unexpectedly show removal marks by the backup application, even though Cisco IMC logs do not indicate any failures. This issue occurs on the Cisco UCS C240 M6 servers with firmware version 4.3(2.240002) equipped with Cisco 12G SAS HBA controller.  Disk I/O errors indicate timeouts and read issues, preventing successful mounting and leading to removal marks on the disks. This situation impacts clusters using the backup application, requiring further investigation to prevent disruptions.  |  4.3(2.240002) |  4.3(5.250001) 4.3(4.242066) 4.2(3o) 4.3(2.250016)  
CSCwn00366 |  Server discovery failures occur on Cisco UCS C-series servers in Intersight Managed Mode when only eNICs or only vHBAs are configured. This issue is caused due to a memory leak in the vniccfgd process, triggered by the palo_vnic_listtype() API call. Over a period of time, the memory leak accumulates, eventually reaching a threshold that leads to failures.  |  4.3(2.230207) |  4.3(5.250001) 4.3(2.250016)  
  
##### Drive PIDs for NVME Disk FRONT-NVME Inoperable Issue - CSCwn42969

UCS-NVME4-1600, UCSX-NVME4-1600-D, HX-NVME4-1600, UCS-NVME4-3200, UCSB-NVME4-3200,UCSX-NVME4-3200, HX-NVME4-3200, UCS-NVME4-6400, UCSB-NVME4-6400, UCSX-NVME4-6400, HX-NVME4-6400, UCS-NVME4-1920, UCSB-NVME4-1920, UCSX-NVME4-1920, HX-NVME4-1920, UCS-NVME4-3840, UCSB-NVME4-3840, UCSX-NVME4-3840, HX-NVME4-3840, UCS-NVME4-7680, UCSB-NVME4-7680, UCSX-NVME4-7680, HX-NVME4-7680, UCS-NVME4-15360, UCSB-NVME4-15360, UCSX-NVME4-15360, HX-NVME4-15360, UCSX-NVB1T6O1P, HX-NVB1T6O1PM6, UCS-NVB3T2O1PM6, UCSB-NVA3T2O1P, UCSX-NVB3T2O1PM6, UCS-NVB3T2O1P, UCSX-NVB3T2O1P, HX-NVB3T2O1PM6, UCS-NVB6T4O1PM6, UCSB-NVA6T4O1P, UCSX-NVB6T4O1PM6, UCS-NVB6T4O1P, UCSX-NVB6T4O1P, HX-NVB6T4O1PM6, UCS-NVB1T9O1VM6, UCSB-NVA1T9O1V, UCSX-NVB1T9O1VM6, UCS-NVB1T9O1V, UCSX-NVB1T9O1V, HX-NVB1T9O1VM6, UCS-NVB3T8O1VM6, UCSB-NVA3T8O1V, UCSX-NVB3T8O1VM6, UCS-NVB3T8O1V, UCSX-NVB3T8O1V, HX-NVB3T8O1VM6, UCS-NVB7T6O1VM6, UCSB-NVA7T6O1V, UCSX-NVB7T6O1VM6, UCS-NVB7T6O1V, UCSX-NVB7T6O1V, HX-NVB7T6O1VM6, UCS-NVB15TO1VM6, UCSB-NVA15TO1V, UCSX-NVB15TO1VM6, UCS-NVB15TO1V, UCSX-NVB15TO1V, HX-NVB15TO1VM6 

#### Resolved Caveats in C-series M7 and M6 Server Firmware Release 4.3(4.242066)

The following table lists the resolved caveats in C-Series M7 and M6 firmware release 4.3(4.242066): 

Defect ID |  Description |  First Version Affected |  Resolved in Release  
---|---|---|---  
CSCwm72893 |  Under rare circumstances, the Cisco UCS VIC adapter might hang when the eCPU hangs due to a software issue. This causes temporary storage loss.  |  4.2(3i) |  4.3(4.242066) 4.3(2.240107)  
CSCwm45280 |  In Cisco UCS C-series servers, Cisco UCS VIC adapter with low memory in Intersight mode is unable to reply to an adapter inventory request because the adapter is unable to create a process to handle the request.  |  4.2(3b) |  4.3(4.242066) 4.3(2.240107) 4.3(2.250016)  
CSCwm02539 |  Boot from SAN may fail to UEFI shell sporadically when multiple servers boot from SAN to a target (such as IBM array) that uses ADISC to build the connection.  |  4.3.4.240152 |  4.3(4.242066)  
CSCwm58947 |  In Cisco UCS servers with Microsoft Windows OS and equipped with Cisco UCS VIC adapter configured with VXLAN, NVGRE and RDMA, the adapter goes into hang state and the Windows OS faces a fatal system error (BSOD).  |  4.2(3b) |  4.3(4.242066)  
CSCwn18475 |  The VIC adapter in a Xen server cluster crashes randomly. Errors appear, the network briefly disconnects, and a timeout occurs. Contact TAC for help and reboot the server, if necessary.  |  5.2(1.240010) |  4.3(4.242066)  
CSCwn42969 |  After resetting or power cycling a Cisco UCS server, the NVME disk FRONT-NVME-2 might stop working if it is idle for over 1.5 weeks or has minimal workload. If the drive becomes inoperable, 

  * Check if the drive's Product ID (PID) is one of the affected models.
  * If the PID is listed, contact Cisco TAC for a replacement.
  * If the PID is not listed, upgrade the firmware to version 9CV10490.

|  4.3(5.240021) |  4.3(4.242066) 4.2(3n)  
CSCwm26679 |  The disk scrub process fails due to faulty drives in the server’s controller and displays the following error message:
    
    
    Cannot complete Disk Scrub

To resolve this, remove the faulty disk and then perform the disk scrub again. |  4.3(3.240043) |  4.3(4.242066)  
CSCwm04776 |  Optimized the disk scrub process timings when initiated via HSU or Redfish. Previously, the process required approximately 25 minutes to complete.  |  4.3(3.240043) |  4.3(4.242066)  
  
#### Resolved Caveats in C-series M5 Server Firmware Release 4.3(2.240107)

The following table lists the resolved caveats in C-Series M5 firmware release 4.3(2.240107): 

Defect ID |  Description |  First Version Affected |  Resolved in Release  
---|---|---|---  
CSCwm72893 |  Under rare circumstances, the Cisco UCS VIC adapter might hang when the eCPU hangs due to a software issue. This causes temporary storage loss.  |  4.2(3i) |  4.3(2.240107) 4.3(4.242066)  
CSCwm45280 |  In Cisco UCS C-series servers, Cisco UCS VIC adapter with low memory in Intersight mode is unable to reply to an adapter inventory request because the adapter is unable to create a process to handle the request.  |  4.2(3b) |  4.3(2.240107) 4.3(4.242066) 4.3(2.250016)  
  
#### Resolved Caveats in C-series Server Firmware Release 4.3(5.240021)

The following caveats are resolved in Release 4.3(5.240021): 

Defect ID |  Description |  First Release Affected  
---|---|---  
CSCwk73250 |  In Cisco UCS servers RAID 1 configuration with more than 2 drives fails at OOB Storage Config. |  4.3(5.240094)A  
CSCwk87002  |  In Cisco UCS M8 servers, on changing the host name in the Web UI, the Cisco IMC certificate is auto-generated with a new hostname as Common Name without the user's consent.  |  4.3(99.240120)  
CSCwk87070  |  In Cisco UCS M8 servers, the label does not appear for a few text fields while using the Web UI in Dark Theme mode. So the user will not be able to identify the text field to perform network-related operations.  |  4.3(99.240119)  
CSCwk98195 |  In Cisco UCS M8 servers, when the port number in the Mount Options field is modified to set for vMedia mapping in the Web UI, vMedia continues to use the default port number for vMedia mappings for the CIFS and NFS shares.  |  4.3(99.240129)  
  
#### Resolved Caveats in C-Series M5 Server Firmware Release 4.3(2.240090)

The following table lists the resolved caveats in C-Series M5 firmware release 4.3(2.240090): 

Defect ID |  Description |  First Bundle Affected  
---|---|---  
CSCwm02322 |  In Cisco UCS C220 M5 servers, the XML API commands for fault monitoring does not capture the fan alerts. This issue is now resolved. |  4.1(3f)  
CSCwj86973 |  In Cisco UCS C220 M5 servers, the SNMP users are not displayed on the 
    
    
    snmpd.conf

file after configuring SNMP. |  4.2(2a)  
CSCwk22654 |  In Cisco UCS C220 M5 servers, the SNMP responses must be improved with better response values for non-populated CPU slots. |  4.3(2.230270)  
  
#### Resolved Caveats in C-Series M6 Server Firmware Release 4.3(4.242038)

The following caveats are resolved in Release 4.3(4.242038): 

Defect ID |  Description |  First Release Affected  
---|---|---  
CSCwk37506 |  When Cisco UCS servers with 1400 or 15000 series adapters have multiple paths for SANboot configured, and one path has issues in discovering the LUN while another path is successful, the clean-up done by fnic driver causes crash when the OS is loaded. This issue is resolved.  |  4.3(3.240043)  
CSCwi35681 |  In Cisco UCS C245 M6 servers, the NUMA node count reverts to the default value and does not retain its configuration after a BIOS upgrade in the host OS.  |  4.3(2.240270)  
CSCwk70990 |  In Cisco UCS C240 M6 servers, the Onboard LOM controller (x550) cannot be disabled. |  4.3(2.230270)  
  
#### Resolved Caveats in C-Series M7 and M6 Firmware Release 4.3(4.241063)

The following caveats are resolved in Release 4.3(4.241063): 

Defect ID |  Description |  First Release Affected  
---|---|---  
CSCwk45810 |  In Cisco UCS C-Series M7 and M6 servers, the HSU Redfish update fails to initiate when the HSU ISO is stored in a CIFS share and the remote CIFS share password includes the following special characters: Single Quote('), Backslash(\\), Comma(,), or Double Quote(").  |  4.3(2.240053)  
CSCwk29026 |  In Cisco UCS C-Series M7 and M6 servers with the release version 4.3(2.230270) or later, importing Cisco IMC configuration causes LDAP domain and domain groups to not be populated.  |  4.3(2.230270)  
CSCwi52997 |  In Cisco UCS C-Series M7 and M6 servers, while using network monitoring tools or running the SNMP walk command, you might face issues in retrieving data for specific Cisco MIBs OIDs when the CIMC is under a low to moderate amount of workload.  The command fails and the following message is displayed: No Such Object available on this agent at this OID. |  4.3(4.230064)  
  
#### Resolved Caveats in C-Series M5 Firmware Release 4.3(2.240077)

The following caveats are resolved in Release 4.3(2.240077): 

Defect ID |  Description |  First Release Affected  
---|---|---  
CSCwk29026 |  In Cisco UCS C-Series M5 servers with the release version 4.3.2.230270 or later, importing Cisco IMC configuration causes LDAP domain and domain groups to not be populated.  The fields are not populated in the below mentioned tabs in the Cisco IMC GUI:

  * Admin > Users > LDAP > Domain
  * Admin > Users > LDAP > Groups > Domain  (for each group specified)

This issue is now resolved. |  4.3(2.230270)  
  
#### Resolved Caveats in C-Series M8 Firmware Release 4.3(4.241014) — None 

#### Resolved Caveats in C-Series M7, M6, and M5 Firmware Release 4.3(4.240152) — None 

#### Resolved Caveats in C-Series M5 Firmware Release 4.3(2.240053)

The following caveats are resolved in Release 4.3(2.240053): 

Defect ID  |  Description |  First Bundle Affected   
---|---|---  
CSCwj09095 |  On Cisco UCS C220 M5SX and C240 M5SX servers with firmware version 4.3(2.240002) or earlier, an error occurred when sending SR-IOV properties through the XML API: 
    
    
    XML Parsing Error: Element 'adaptorEthSRIOVProfile

Upgrading to firmware version 4.3(2.240020) or later resolved this issue. |  4.3(2.230189)  
  
#### **Resolved Caveats in C-Series M6 Server Firmware, Release 4.3(2.240037) — None**

#### Resolved Caveats in C-Series M7 and M6 Firmware Release 4.3(3.240043) — None

#### Resolved Caveats in C-Series M7, M6, and M5 Server Firmware, Release 4.3(2.240009) 

The following table lists the resolved caveats in C-Series firmware release 4.3(2.240009)

Defect ID | Description | First Bundle Affected  
---|---|---  
CSCwj00617 |  In Cisco UCS C-Series M5 and M6 servers, the SAS expander firmware update from the XML API interface, using HTTP and TFTP protocol, fails and displays the following error message: 
    
    
    Operation failed. Invalid Password!

|  4.2(3i)  
CSCwi97945 |  In Cisco UCS M5 and M6 servers, the SAS expander firmware update from the Cisco Integrated Management Controller (CLI) interface, using HTTP and TFTP protocol, fails and displays the following error message: 
    
    
    Operation failed. Invalid Password!

|  4.2(3i)  
  
#### Resolved Caveats in C-Series Firmware Release 4.3(2.240002)

The following table lists the resolved caveats in C-Series firmware release 4.3(2.240002)

Defect ID | Description | First Bundle Affected  
---|---|---  
CSCwh53073 |  On Cisco UCS C240 M5 SD and Cisco UCS C245 M6 SX, the alarms generated from Cisco Integrated Management Controller (CIMC) are not accurately represented in Intersight User Interface (UI). The Alarm page in the Intersight UI displayed the date/time of the associated alarm as 'in 9 hours' though the alarm was triggered immediately after the event.  |  4.2(2a)  
CSCwi04192 |  On Cisco UCS C220 M6 and C240 M6 servers, the third-party Mellanox MLOM cards (Mellanox UCSC-O-N6CD100GF) are prone to overheating and link flapping due to the default fan policy failing to offer adequate cooling and required fan speed alteration settings to cool the card.  |  4.3(2.230207)  
  
#### Resolved Caveats in C-Series Firmware Release 4.3(2.230270)

The following table lists the resolved caveats in C-Series firmware release 4.3(2.230270)

Defect ID | Description | First Bundle Affected  
---|---|---  
CSCwh34432  |  While mounting vMedia using Redfish API, when the user forgets to post the TransferProtocolType field, the following error message is displayed: 
    
    
    Message: Bad request format

|  4.3(1.230097)  
CSCwf44478  |  In Cisco UCS C-series M7 servers with Red Hat Enterprise Linux OS versions 8.6 and 9.0, Micron 7450 NVMe drive does not get detected after hot-plug.  |  4.3(2.230207)  
CSCwh13701 |  When Cisco UCS C225 M6 and C245 M6 servers, equipped with power supply units (PSUs) and have firmware versions prior to 4.2(3h), the servers may power off unexpectedly without any warning.  |  4.3(1.230097)  
CSCwf94278 |  In Cisco UCS C-series M5 servers with release versions 4.1(3b), 4.2(2a), 4.2(3b), the user can create a session with a 'read only' user, but unable to delete or log out from the session while using the Redfish API interface.  |  4.2(2a)  
CSCwh81377 |  On Cisco UCS C-series M7 servers, deploying a vMedia policy via Intersight results in a failure with the error message: "Error removing existing Virtual Media: Virtual Medias 0, 1 not ejected. Please retry operation after some time." This issue arises when the vMedia policy is created with enabled vMedia configuration.  |  4.3(2.230207)  
  
#### Resolved Caveats in C-Series Firmware Release 4.3(2.230207)

The following table lists the resolved caveats in C-Series firmware release 4.3(2.230207)

Defect ID | Description | First Bundle Affected  
---|---|---  
CSCwe19822  |  In all models of M5 servers, it is observed that CIMC reset occurs due to kernel crash and watchdog reset. |  4.2(2f)  
CSCwe87623  |  In all models of M6 servers, it is observed that with every power cycle, there is latency in generic inventory Information update as a result HCL status appears Incomplete. The genericInventory mo entries get deleted and inserted completely. During this update of the inventory info, missing OS information results in momentary invalidation of HCL status until OS is booted.  |  4.2(3e)  
  
#### Resolved Caveats in C-Series M7 Firmware Release 4.3(1.230138)

The following table lists the resolved caveats in C-Series M7 firmware release 4.3(1.230138)

Defect ID | Description | First Bundle Affected  
---|---|---  
CSCwe87764 |  In Cisco UCS M7 servers equipped with 128GB DIMMs, there might be a decrease in the performance of the CPU when the values of the voltage regulator is modified to enhance the system performance.  |  4.3(1.230124)  
  
#### Resolved Caveats in C-Series M7 Firmware Release 4.3(1.230124)

The following table lists the resolved caveats in C-Series M7 firmware release 4.3(1.230124)

Defect ID | Description | First Bundle Affected  
---|---|---  
CSCwe47118 |  Redfish monitor core occured during combinational stress(Redfish stress included). |  4.3(1.230097)  
  
### Open Caveats

#### Open Caveats in X-Series M8, M7 5.4(0.260010), M6 5.4(0.260009), C-Series M8, M7, M6 4.3(6.260017), and B-Series M6, M5 5.4(0.260011) Server Firmware Release — None 

#### Open Caveats in C-Series M5 Server Firmware Release 4.3(2.260007) — None 

#### Open Caveats in Cisco UCS X-Series M7 5.4(0.260001) and C-Series M8, M7 4.3(6.260003) Server Firmware Release — None 

#### Open Caveats in C-Series M5 Server Firmware Release 4.3(2.250063) — None 

#### Open Caveats in Cisco UCS C-Series M7 Server Firmware Release 4.3(6.250117) — None 

#### Open Caveats in Cisco UCS X-Series M8 5.4(0.250105), 5.4(0.250106), M7 5.4(0.250106), M6 5.4(0.250097), C-Series M8, M7, M6 4.3(6.250101), and B-Series M6, M5 5.4(0.250090) Server Firmware Release — None 

#### Open Caveats in Cisco UCS C-Series M8 Server Firmware Release 4.3(5.250045) — None 

#### Open Caveats in Cisco UCS C-Series M8 Server Firmware Release 4.3(6.250060) — None 

#### Open Caveats in C-Series M5 Server Firmware Release 4.3(2.250045) — None 

#### Open Caveats in C-Series M8 Server Firmware Release 4.3(5.250043) — None 

#### Open Caveats in X-Series M8 5.4(0.250052), M7 5.4(0.250048), M6 5.4(0.250047) and C-Series M8, M7, M6 4.3(6.250053) Server Firmware Release 

The following table lists the open caveats in this release:

Defect ID |  Description | Workaround |  First Bundle Affected  
---|---|---|---  
CSCws30219 |  Cisco UCS M7 servers are susceptible to host lockups triggered by ECC (Error Correcting Code) memory events. This issue is specifically related to how the server’s BIOS interacts with the EFI (Extensible Firmware Interface) during error conditions. During these events, the BIOS does not correctly retrieve a required variable, causing EFI to return an invalid parameter. As a result, the operating system is unable to continue normal operation and freezes without logging any errors. When this occurs, the host becomes unresponsive and KVM (keyboard, video, mouse) input is not accepted.  Single-bit ECC errors—while not logged due to DDR5 specifications—can trigger this condition, resulting in complete loss of host responsiveness.  |  Downgrade server bundle:

  * For X-Series servers, downgrade the server bundle to version 5.4(0.250040) or an earlier release.
  * For C-Series servers, downgrade the server bundle to version 4.3(6.250044) or an earlier release.

|  X-Series M7: 5.4(0.250048) C-series M7: 4.3(6.250053)  
CSCwj57044 |  Cisco UCS VIC 1400 and 15000 series adapters configured inEtherChannel mode may experience lower than expected TCP/UDP throughput. Network bandwidth does not scale to the combined line rateof the physical links. These issues observed with Quad Port adapters whenused in port-channelconfigurations.  |  There is no known workaround. |  4.3(2.240002)  
  
#### Open Caveats in C-series M5 Server Firmware Release 4.3(2.250037) — None 

#### Open Caveats in X-Series M8 5.4(0.250040), 5.4(0.250044) and M7 5.4(0.250040), and C-Series 4.3(6.250044) Server Firmware Release — None 

#### Open Caveats in C-Series M8, M7, and M6 Server Firmware Release 4.3(5.250033) — None 

#### Open Caveats in X-Series M8 5.4(0.250037) and C-Series M8 4.3(6.250040) and 4.3(6.250039), M7, M6 4.3(6.250040) Server Firmware Release 

The following table lists the open caveats in this release:

Defect ID |  Description | Workaround |  First Bundle Affected  
---|---|---|---  
CSCwo67388 |  On Cisco UCS X210c M8, C220 M8, and C240 M8 servers in Intersight or Standalone mode, the "Password History" feature does not function correctly. When the "Password History" field is set between 1 and 5, the Cisco Integrated Management Controller (CIMC) fails to check new passwords against previous ones, allowing password reuse.  |  Ensure to use unique, non-repetitive passwords. |  4.3(6.250012)  
CSCwn95239 |  On Cisco UCS C-Series servers, the server may fail to power on due to BIOS corruption. The following message is displayed: "Power on failure asserted [Power on Fail, Server failed to power-on]." This issue can occur if the BIOS flashing is interrupted by a CMOS clear operation triggered during an update, a factory default reset, a Cisco IMC reboot, or other operations.  |  Do one of these: 

  * Reboot of CIMC. In-turn, recovery mechanism will start that is bios activation. 
  * Activate of bacup BIOS. 
  * Update and activate BIOS.

|  4.3(6.250039)  
CSCwo67280 |  In Cisco UCS C-Series servers with release version 4.3.5.250001, the VIC out-of-band (OOB) firmware update is not triggered when using the CLI for the activate command.  |  Use the UI or XML interfaces, or use the CLI with the "no-activate" option. After initiating the update, manually power cycle the host to ensure the update completes successfully.  |  4.3(6.250033)  
CSCwn47257 |  In Cisco UCS C-Series servers, when upgrading the VIC firmware following a change in the VIC FPGA, the system may occasionally boot from the Golden FPGA image, indicated by a "G" suffix in the version.  |  Flash the same image and perform the power-cycle of the host. |  4.3(6.250039)  
CSCwm33093 |  On U.3/SAS/SATA drives, creating a RAID-10 storage profile applied to disks 1, 2, 3, and 4 results in unexpected behavior. Removing disk-1 causes the virtual drive (VD) to degrade, but removing disk-2 leads to the VD going offline instead of degraded. Re-inserting disks 1 and 2 restores them to an online state, but the VD remains inoperable. This issue arises because firmware-driven span assignments override user configurations to optimize performance.  |  Use arcconf to check accurate span assignments, as firmware overrides management tool configurations for performance optimization. |  4.3(5.240134)  
CSCwo02722 |  On Cisco UCS C240 M7 servers, the firmware upgrade for UCSC-GPU-FLEX170 fails when upgrading to firmware version DG02_1.3274-7.0.0.0, which corresponds to HUU 4.3.6.250039 or later releases. This issue occurs when the current running firmware version of UCSC-GPU-FLEX170 is DG02_1.3260-6.4.0.0 or DG02_1.3260-6.7.0.0.  |  Upgrade the UCSC-GPU-FLEX170 to an intermediate firmware version DG02_1.3271-6.8.0.0, which is equivalent to HUU 4.3(4.24xxxx) or 4.3(5.2xxxxx) release level.  |  **Note** |  In the mentioned HUU version numbers, "xxxx" represents all versions available within the series.  
---|---  
4.3(6.250040)  
CSCwo68248 |  On Cisco UCS C220 M7 and C240 M7 servers running HUU 4.3(3.240xxx) level firmware with 2 PCIe VICs and 1 MLOM VIC, upgrading the server firmware to HUU 4.3(4.xxxxxx), 4.3(5.xxxxxx), 4.3(6.xxxxx), or later using the Redfish API interface may cause the UCSUpdate task to falsely report an update failure for the PCIe VIC (riser1) through which CiscoCard mode is configured. However, the firmware is actually updated and activated successfully in the background.  |  **Note** |  In the mentioned HUU version numbers, "xxxx" represents all versions available within the series.  
---|---  
There is no workaround. Ignore the false failure update. |  4.3(3.240043)  
CSCwo77289 |  When a Cisco UCS B-series B200 M5 server is upgraded to firmware version 5.3(0.250001), all the M2 disks report alerts for exceeding the temperature thresholds.  |  Rollback to the previous firmware version 5.3(0.240014). |  5.3(0.250001)  
CSCwm45755 |  In Cisco UCS C220 M8 servers equipped with M.2 disks connected to a storage controller, the disks are not detected on the Windows Server 2025installation page. However, the disks are detected during the installation of WindowsServer 2022. This issue occurs specifically with Windows Server 2025.  |  There is no workaround. |  4.3(6.250039)  
CSCwn99720 |  On Cisco UCS C-Series M8 servers with Intel processors and an R1S CPU configured in a single CPU setup on the 2S platform, Intel SGX remains disabled even after being enabled in the BIOS.  |  Use a dual CPU configuration. |  4.3(6.250039)  
CSCwn51498 |  On Cisco UCS C220 and C240 M8 servers, raw OEM SEL records are logged in the CIMC SEL during the boot and shutdown of Windows Server 2025. This does not impact system functionality or performance.  |  No workaround is required. Ignore the raw OEM SEL records logged during the boot process of Windows Server 2025. |  4.3(6.250039)  
  
#### Open Caveats in C-Series M8, M7, and M6 Server Firmware Release 4.3(5.250030) — None 

#### Open Caveats in C-series M5 Server Firmware Release 4.3(2.250021) — None 

#### Open Caveats in X-Series M8, M7, M6 5.3(0.250021) and B-Series M6, M5 5.3(0.250021) Server Firmware Release — None 

#### Open Caveats in X-Series M7 5.2(2.240080), M6 5.2(2.240078), B-Series M6, M5 5.2(2.240080), and C-series M7, M6 4.3(4.242066) Firmware Release — None 

#### Open Caveats in X-Series Server Firmware Release 5.3(0.240016)

The following table lists the open caveats in this release:

Defect ID |  Description | Workaround |  First Bundle Affected  
---|---|---|---  
CSCwj96037 |  In an ESXi 8.0U2 environment with VMs running RHEL9.3/RHEL9.4, there are observed issues when hot-pluggable Intel® and Micron® NVMe drives are removed or inserted. Commands such as lsblk, lspci, and nvme list do not update correctly, resulting in incorrect drive information and potential VM power-off. VMs may not properly recognize and update new drive information after NVMe drive removal or insertion.  |  Perform the following steps to ensure that VM can detect the newly inserted NVME drive:

  1. Power off VM.
  2. Add PCIe NVME Drive to VM Config.
  3. Power on VM. 

|  5.2(99.241014)  
  
#### Open Caveats in X-Series M7 5.2(2.240074), X-Series M6 5.2(2.240073), and B-series M6 5.2(2.240073) Firmware Release — None 

#### Open Caveats in X-Series M7 and M6 Firmware Release 5.2(2.240053)

The following table lists the open caveats in this release:

Defect ID  |  Description |  Workaround |  First Bundle Affected   
---|---|---|---  
CSCwj61708 |  When performing a reboot of multiple servers in a scale-setup of 160 servers and high PV count of greater than 64K in Cisco UCS FI domain, secure boot adapters may not restart instantly under certain situations. This was observed in a scale setup where simultaneous warm reboot of 22 blades across three chassis was initiated. Some blades with Cisco UCS VIC 15000 series secure boot adapters failed to boot from the SAN after a soft reboot. These adapters execute a cleanup process with the Fabric Interconnects to maintain system integrity, which needs to be finished before the server BIOS can recognize the adapters. This issue arises specifically under conditions of very high PV count or exceptionally high CPU utilization on the FI. During these binstances, if the server BIOS finalizes the boot sequence before the secure boot adapters finish the cleanup, the adapters may fail to be detected. Consequently, the server may not successfully boot from the SAN. This issue is observed in configurations on servers equipped with Cisco UCS VIC 15000 series adapters.  |  Reboot the failed servers. |  4.3(4a)  
  
#### Open Caveats in X-Series M7 Firmware Release 5.2(1.240010) — None

#### Open Caveats in X-Series M7 Firmware Release 5.2(0.230127) — None

#### Open Caveats in X-Series M6 Firmware Release 5.2(0.230127) — None

#### Open Caveats in B-Series M6 and M5 Firmware Release 5.2(2.240051) — None 

#### Open Caveats in B-Series M5 Firmware Release 5.2(0.230127) and M6 Firmware Release 5.2(1.240010) — None

#### Open Caveats in C-series M5 Server Firmware Release 4.3(2.250016)

The following table lists the open caveats in this release:  Defect ID  |  Description |  Workaround |  First Bundle Affected   
---|---|---|---  
CSCwn97854 |  Server Profile activation on a Cisco UCS M5 C240 server fails when upgrading from 4.3(2.240107) to 4.3(2.250016).  |  **Scenario 1: Using Firmware Policy** If server discovery is successful, follow these steps: 

  * Remove the firmware policy and reactivate the server profile.
  * Verify that the server profile has vNICs and vHBAs configured correctly in the LCP/SCP. 
  * Upgrade to version 4.3(2.250016) using the firmware policy or through the direct upgrade workflow.

**Scenario 2: Using Direct Upgrade** \- Downgrade or upgrade to a stable BIOS version to recover the server. For assistance with recovering the server, contact Cisco TAC.  |  4.3(2.250016)  
  
#### Open Caveats in C-series M5 Server Firmware Release 4.3(2.240107) — None 

#### Open Caveats in C-Series Server Firmware Release 4.3(5.240021)

The following table lists the open caveats in C-Series firmware release 4.3(5.240021): 

Defect ID |  Description | Workaround |  First Bundle Affected  
---|---|---|---  
CSCwk79108 |  Drive migration between servers with Miami Beach Plus controllers on same drive slots, list virtual drives that were not imported. |  There is no workaround. |  4.3(5.240094)A  
CSCwm36068 |  In Cisco UCS M7 servers, creation of virtual drives using self-encrypting drive and non self-encrypting drive combination fails for out-of-band management (OOB). This issue is seen in the Web UI and CLI interfaces.  |  There is no workaround. |  4.3(4.240152)  
  
#### Open Caveats in C-Series M5 Server Firmware Release 4.3(2.240090)

The following table lists the open caveats in this release:

Defect ID |  Description | Workaround |  First Bundle Affected  
---|---|---|---  
CSCwm55124 |  Due to the Broadcom/VMware data center migration, any new Cisco UCS M5 server certifications can be initiated only after 14th October 2024.  VMware certifications and equivalencies will need to be started again with a new session in VIVa 2.0. The new session is planned to be launched on 14th October 2024. |  There is no workaround. |  4.1(3f)  
  
#### Open Caveats in C-Series M6 Server Firmware Release 4.3(4.242038)

The following table lists the open caveats in this release:

Defect ID | Description |  Workaround |  First Bundle Affected  
---|---|---|---  
CSCwe84825 |  In Cisco UCS C245 M6 servers, the configured AMD CBS setting policy reverts to the default state when the BIOS is updated on the host.  |  Re-apply the CBS setting policy to retain the earlier settings for the BIOS update. | 4.3(2.230078)  
  
#### Open Caveats in C-Series M7 and M6 Firmware Release 4.3(4.241063) — None 

#### Open Caveats in C-Series M5 Firmware Release 4.3(2.240077) — None 

#### Open Caveats in C-Series M8 Server Firmware Release 4.3(4.241014)

The following table lists the open caveats in this release:

Defect ID  |  Description |  Workaround |  First Bundle Affected   
---|---|---|---  
CSCwj79250 |  Config Drift has been observed for SNMP, SMTP, and Syslog policies intermittently on C220 M7, C240 M7, and C245 M8 servers. |  This issue has no workaround. |  4.3(4.240152)  
  
#### Open Caveats in C-Series M7, M6, and M5 Firmware Release 4.3(4.240152) — None 

#### Open Caveats in C-Series M5 Firmware Release 4.3(2.240053) — None 

#### Open Caveats in C-Series M6 Firmware Release 4.3(2.240037) — None 

#### Open Caveats in C-Series M7 and M6 Firmware Release 4.3(3.240043) — None

#### Open Caveats in C-Series M7, M6, and M5 Firmware 4.3(2.240009) — None

#### Open Caveats in C-Series Firmware Release 4.3(3.240022)

The following table lists the open caveats in this release:

Defect ID | Symptom |  Workaround |  First Bundle Affected  
---|---|---|---  
CSCwi85031 |  Cisco UCS C240 M7 server with an Emerald Rapids 8558+, 8568Y+ or CPU SKUs processor and two Intel Flex 170 GPUs, experienced a crash and failed to load the RHEL 9.2 or Ubuntu 22.04.3. Instead of successfully booting and installing the OS, the system hung and crashed.  | 

  1. Access the BIOS setup.
  2. Navigate Advanced > Socket Configuration > Uncore Configuration > Uncore General Configuration.
  3. Change MMIO High Granularity Size to 1024G and Press F10to save. 
  4. Reboot the server.

|  4.3(3.240022)  
CSCwi85033 |  Cisco UCS C240 M7 server with an Emerald Rapids 8558+, 8568Y+ or CPU SKUs processor and two NVDIA H100 GPUs, experienced a crash and failed to load the RHEL 9.2 or Ubuntu 22.04.3, led to operational disruptions.  | 

  1. Access the BIOS setup.
  2. Navigate Advanced > Socket Configuration > Uncore Configuration > Uncore General Configuration.
  3. Change MMIO High Granularity Size to 1024G and Press F10to save. 
  4. Reboot the server.

|  4.3(3.240022)  
  
#### Open Caveats in C-Series M7 Firmware Release 4.3(2.240002) — None

## Known Behavior and Limitations

Defect ID |  Symptom |  Workaround |  First Version Affected  
---|---|---|---  
CSCwo27237 |  During installation of the Microsoft Windows 2025® operating system on Cisco UCS X-Series M8 servers equipped with Intel® processors, with VMD enabled in the BIOS, the loading of the F6 Intel VMD driver may experience a longer-than-usual delay.  The time required to display NVMe drives increases with the number of NVMe drives present in the system. |  Once the Windows installer screen appears, follow these steps:

  * Click Load VMD driver once and wait up to 3 minutes before clicking Refresh. 
  * If the drives are not listed, load the driver a second time. If you encounter any error messages, click the Back button to search for the disks again. 
  * All the NVMe drive should be visible now.

|  5.4(0.250037)  
CSCwn60053 |  On Cisco UCS C-Series M8 servers, when a tampered VIC is detected, the following message is displayed: "No Signal. Reason: Host is powered but no output on video. Press any key to wake up." The POST command does not complete on the host, and the overall system health is displayed as Critical. The fault summary displays the message: "Adapter [MLOM/PCI] secure validation failed."  |  There is no workaround. |  4.3.5.240021  
CSCwn26554 |  On Cisco UCS C-Series servers, the host reboots under the following conditions if the BMC reboots abruptly during an HSU update in progress: 

  * "ApplyTime":"OnNextBoot" and "Targets":["/redfish/v1/UpdateService/FirmwareInventory/BIOS", "/redfish/v1/UpdateService/FirmwareInventory/CIMC"]
  * "ApplyTime":"OnNextBoot" and "Targets":["/redfish/v1/UpdateService/FirmwareInventory/BIOS"]
  * "ApplyTime":"OnNextBoot" and "Targets":["/redfish/v1/UpdateService/FirmwareInventory/CIMC"]

|  HSU update flow works fine with "ApplyTime":"Immediate" for all the following target combinations.

  * "Targets":["/redfish/v1/UpdateService/FirmwareInventory/BIOS","/redfish/v1/UpdateService/FirmwareInventory/CIMC"]}'.
  * "Targets":["/redfish/v1/UpdateService/FirmwareInventory/BIOS"]}'.
  * "Targets":["/redfish/v1/UpdateService/FirmwareInventory/CIMC"]}'.

|  4.3.5.240021  
CSCwn36143 |  In Cisco UCS C225 M8 servers with Genoa 1U NVMe SKU, PCIe PERR errors are observed during the hotplugging of NVMe drives. |  There is no workaround.  These errors are SEL warnings and can be ignored as they do not have any functional impact. |  4.3.5.240021  
  
## Related resources

  * [Release Notes and Release Bundles for Cisco Intersight](https://www.cisco.com/c/en/us/support/servers-unified-computing/intersight/products-release-notes-list.html)

  * [Cisco UCS Equivalency Matrix for Cisco Intersight, Cisco IMC, and Cisco UCS Manager](https://www.cisco.com/c/dam/en/us/td/docs/unified_computing/ucs/c/sw/UCS-Equivalency-Matrix/index.html)

  * [Release Notes for Cisco UCS Manager](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-release-notes-list.html)

  * [Release Notes for Cisco UCS Rack Server Software](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c-series-integrated-management-controller/products-release-notes-list.html)

  * [Cisco Baseboard Management Controller Release Notes for Cisco UCS C885A M8 Rack Server](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/release/notes/Cisco-BMC-Release-Notes/1-1-0/b_cisco-openbmc-release-notes-1_1.html)

  * [Cisco UCS Manager and Intersight Release Strategy](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/release/notes/b_ucsm-and-intersight-release-strategy-doc.html)


---
