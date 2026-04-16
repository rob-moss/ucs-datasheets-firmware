# UCS Manager Cross-Version Firmware Support 4.3

| | |
|---|---|
| **URL Title** | UCS Manager Cross-Version Firmware Support 4.3 |
| **URL** | https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/release/notes/b_cross-version-fw-support_4_3.html |
| **Long URL** |  |
| **HTML Title** | Cisco UCS Manager Cross-Version Firmware Support, Release 4.3 |
| **Source file** | `ucs-docs-raw/html/b_cross-version-fw-support_4_3.html` |
| **File type** | HTML |
| **Fetched on** | 2026-04-16 10:50:04 |

---

## Page 1: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/release/notes/b_cross-version-fw-support_4_3.html

**First Published: September 23, 2025**

# Cisco UCS Manager Cross-Version Firmware Support, Release 4.3

The Cisco UCS Manager A bundle software (Cisco UCS Manager, Cisco NX-OS, IOM and FEX firmware) can be mixed with previous B or C bundle releases on the servers (host firmware [FW], BIOS, Cisco IMC, adapter FW and drivers). 

[Cisco UCS Equivalency Matrix for Cisco Intersight, Cisco IMC, and Cisco UCS Manager](https://www.cisco.com/c/dam/en/us/td/docs/unified_computing/ucs/c/sw/UCS-Equivalency-Matrix/index.html) outlines the release timeline for Cisco Intersight, Cisco Integrated Management Controller (IMC), and Cisco UCS Manager (UCS Manager). It includes essential information such as the date each patch was posted, the specific patch version, and the platforms that are supported by each release. By referring to this matrix, you can identify the appropriate firmware and software versions required for your servers before migrating them to Cisco Intersight. This ensures that your server infrastructure remains supported and operates efficiently during and after the transition. 

The following table lists the mixed A, B, and C bundle versions that are supported on Cisco UCS 6300, 6400 series and 6536 Fabric Interconnects: 

Table 1. Mixed Cisco UCS Releases Supported on Cisco UCS 6300, 6400, 6536 Series Fabric Interconnects |  Infrastructure Versions (A Bundles)  
---|---  
Host FW Versions (B or C Bundles)  |  4.0(1) |  4.0(2) |  4.0(4) |  4.1(1) |  4.1(2) |  4.1(3) |  4.2(1) |  4.2(2) |  4.2(3) |  4.3(2) |  4.3(3) |  4.3(4) |  4.3(5) |  4.3(6)  
4.3(6) |  —  |  —  |  —  |  —  |  —  |  —  |  —  |  —  |  —  |  6332, 6332-16UP, 6454, 64108, 6536 |  6332, 6332-16UP, 6454, 64108, 6536 |  6332, 6332-16UP, 6454, 64108, 6536 |  6332, 6332-16UP, 6454, 64108, 6536 |  6332, 6332-16UP, 6454, 64108, 6536  
4.3(5) |  —  |  —  |  —  |  —  |  —  |  —  |  —  |  —  |  —  |  6332, 6332-16UP, 6454, 64108, 6536 |  6332, 6332-16UP, 6454, 64108, 6536 |  6332, 6332-16UP, 6454, 64108, 6536 |  6332, 6332-16UP, 6454, 64108, 6536 |  6332, 6332-16UP, 6454, 64108, 6536  
4.3(4) |  —  |  —  |  —  |  —  |  —  |  —  |  —  |  —  |  —  |  6332, 6332-16UP, 6454, 64108, 6536 |  6332, 6332-16UP, 6454, 64108, 6536 |  6332, 6332-16UP, 6454, 64108, 6536 |  6332, 6332-16UP, 6454, 64108, 6536 |  6332, 6332-16UP, 6454, 64108, 6536  
4.3(3) |  —  |  —  |  —  |  —  |  —  |  —  |  —  |  —  |  —  |  6332, 6332-16UP, 6454, 64108, 6536 |  6332, 6332-16UP, 6454, 64108, 6536 |  6332, 6332-16UP, 6454, 64108, 6536 |  6332, 6332-16UP, 6454, 64108, 6536 |  6332, 6332-16UP, 6454, 64108, 6536  
4.3(2) |  —  |  —  |  —  |  —  |  —  |  —  |  —  |  —  |  —  |  6332, 6332-16UP, 6454, 64108, 6536 |  6332, 6332-16UP, 6454, 64108, 6536 |  6332, 6332-16UP, 6454, 64108, 6536 |  6332, 6332-16UP, 6454, 64108, 6536 |  6332, 6332-16UP, 6454, 64108, 6536  
4.2(3) |  —  |  —  |  —  |  —  |  —  |  —  |  6200, 6332, 6332-16UP, 6454, 64108 |  6200, 6332, 6332-16UP, 6454, 64108 |  6200, 6332, 6332-16UP, 6454, 64108, 6536 |  6332, 6332-16UP, 6454, 64108, 6536 |  6332, 6332-16UP, 6454, 64108, 6536 |  6332, 6332-16UP, 6454, 64108, 6536 |  6332, 6332-16UP, 6454, 64108, 6536 |  6332, 6332-16UP, 6454, 64108, 6536  
4.2(2) |  —  |  —  |  —  |  —  |  —  |  —  |  6200, 6332, 6332-16UP, 6454, 64108 |  6200, 6332, 6332-16UP, 6454, 64108 |  6200, 6332, 6332-16UP, 6454, 64108 |  6332, 6332-16UP, 6454, 64108 |  6332, 6332-16UP, 6454, 64108 |  6332, 6332-16UP, 6454, 64108 |  6332, 6332-16UP, 6454, 64108 |  6332, 6332-16UP, 6454, 64108  
4.2(1) |  —  |  —  |  —  |  —  |  —  |  —  |  6200, 6332, 6332-16UP, 6454, 64108  |  6200, 6332, 6332-16UP, 6454, 64108  |  6200, 6332, 6332-16UP, 6454, 64108  |  6332, 6332-16UP, 6454, 64108 |  6332, 6332-16UP, 6454, 64108 |  6332, 6332-16UP, 6454, 64108 |  6332, 6332-16UP, 6454, 64108 |  6332, 6332-16UP, 6454, 64108  
4.1(3) |  —  |  —  |  —  |  6200, 6332, 6332-16UP, 6454, 64108  |  6200, 6332, 6332-16UP, 6454, 64108  |  6200, 6332, 6332-16UP, 6454, 64108  |  6200, 6332, 6332-16UP, 6454, 64108  |  6200, 6332, 6332-16UP, 6454, 64108  |  6200, 6332, 6332-16UP, 6454, 64108  |  6332, 6332-16UP, 6454, 64108 |  6332, 6332-16UP, 6454, 64108 |  6332, 6332-16UP, 6454, 64108 |  6332, 6332-16UP, 6454, 64108 |  6332, 6332-16UP, 6454, 64108  
4.1(2) |  —  |  —  |  —  |  6200, 6332, 6332-16UP, 6454, 64108  |  6200, 6332, 6332-16UP, 6454, 64108  |  6200, 6332, 6332-16UP, 6454, 64108  |  6200, 6332, 6332-16UP, 6454, 64108  |  6200, 6332, 6332-16UP, 6454, 64108  |  6200, 6332, 6332-16UP, 6454, 64108  |  —  |  —  |  —  |  —  |  —   
4.1(1) |  —  |  —  |  —  |  6200, 6332, 6332-16UP, 6454, 64108  |  6200, 6332, 6332-16UP, 6454, 64108  |  6200, 6332, 6332-16UP, 6454, 64108  |  6200, 6332, 6332-16UP, 6454, 64108  |  6200, 6332, 6332-16UP, 6454, 64108  |  6200, 6332, 6332-16UP, 6454, 64108  |  —  |  —  |  —  |  —  |  —   
4.0(4) |  6200, 6332, 6332-16UP, 6454  |  6200, 6332, 6332-16UP, 6454  |  6200, 6332, 6332-16UP, 6454  |  6200, 6332, 6332-16UP, 6454  |  6200, 6332, 6332-16UP, 6454  |  6200, 6332, 6332-16UP, 6454  |  6200, 6332, 6332-16UP, 6454  |  6200, 6332, 6332-16UP, 6454  |  6200, 6332, 6332-16UP, 6454  |  —  |  —  |  —  |  —  |  —   
4.0(2) |  6200, 6332, 6332-16UP, 6454  |  6200, 6332, 6332-16UP, 6454  |  6200, 6332, 6332-16UP, 6454  |  6200, 6332, 6332-16UP, 6454  |  6200, 6332, 6332-16UP, 6454  |  6200, 6332, 6332-16UP, 6454  |  6200, 6332, 6332-16UP, 6454  |  6200, 6332, 6332-16UP, 6454  |  6200, 6332, 6332-16UP, 6454  |  —  |  —  |  —  |  —  |  —   
4.0(1) |  6200, 6332, 6332-16UP, 6454  |  6200, 6332, 6332-16UP, 6454  |  6200, 6332, 6332-16UP, 6454  |  6200, 6332, 6332-16UP, 6454  |  6200, 6332, 6332-16UP, 6454  |  6200, 6332, 6332-16UP, 6454  |  6200, 6332, 6332-16UP, 6454  |  6200, 6332, 6332-16UP, 6454  |  6200, 6332, 6332-16UP, 6454  |  —  |  —  |  —  |  —  |  —   
  
The following table lists the mixed A and B bundle versions that are supported on Cisco UCS X-Series Direct: 

Table 2. Mixed Cisco UCS Releases Supported on Cisco UCS X-Series Direct Host FW Versions (B Bundles)  |  Infrastructure Versions (A Bundles)   
---|---  
|  4.3(4) |  4.3(5) |  4.3(6)  
4.3(6) |  UCSX-S9108-100G |  UCSX-S9108-100G |  UCSX-S9108-100G  
4.3(5) |  UCSX-S9108-100G |  UCSX-S9108-100G |  UCSX-S9108-100G  
4.3(4) |  UCSX-S9108-100G |  UCSX-S9108-100G |  UCSX-S9108-100G  
|  **Note** |  In a setup equipped with Cisco UCS X210c M8 Compute Node, you cannot downgrade Infrastructure Version (A Bundle) or Host Firmware Version (B bundle) to any release earlier than 4.3(6a).  In a setup equipped with Cisco UCS X-Series Direct, you cannot downgrade Infrastructure Version (A Bundle) to any release earlier than 4.3(4b).   
---|---  
  
The following table lists the mixed A, B, and C bundle versions that are supported on Cisco UCS Mini fabric interconnects: 

Table 3. Mixed Cisco UCS Releases Supported on Cisco UCS Mini Fabric Interconnects |  Infrastructure Versions (A Bundles)   
---|---  
Host FW Versions (B or C Bundles)  |  4.0(1) |  4.0(2) |  4.0(4) |  4.1(1) |  4.1(2) |  4.1(3) |  4.2(1) |  4.2(2) |  4.2(3) |  4.3(2) |  4.3(3) |  4.3(4) |  4.3(5) |  4.3(6)  
4.3(6) |  —  |  —  |  —  |  —  |  —  |  —  |  —  |  —  |  —  |  6324 |  6324 |  6324 |  6324 |  6324  
4.3(5) |  —  |  —  |  —  |  —  |  —  |  —  |  —  |  —  |  —  |  6324 |  6324 |  6324 |  6324 |  6324  
4.3(4) |  —  |  —  |  —  |  —  |  —  |  —  |  —  |  —  |  —  |  6324 |  6324 |  6324 |  6324 |  6324  
4.3(3) |  —  |  —  |  —  |  —  |  —  |  —  |  —  |  —  |  —  |  6324 |  6324 |  6324 |  6324 |  6324  
4.3(2) |  —  |  —  |  —  |  —  |  —  |  —  |  —  |  —  |  —  |  6324 |  6324 |  6324 |  6324 |  6324  
4.2(3) |  —  |  —  |  —  |  —  |  —  |  —  |  6324  |  6324  |  6324  |  6324 |  6324 |  6324 |  6324 |  6324  
4.2(2) |  —  |  —  |  —  |  —  |  —  |  —  |  6324  |  6324  |  6324  |  6324 |  6324 |  6324 |  6324 |  6324  
4.2(1) |  —  |  —  |  —  |  —  |  —  |  —  |  6324  |  6324  |  6324  |  6324 |  6324 |  6324 |  6324 |  6324  
4.1(3) |  —  |  —  |  —  |  6324  |  6324  |  6324  |  6324  |  6324  |  6324  |  6324 |  6324 |  6324 |  6324 |  6324  
4.1(2) |  —  |  —  |  —  |  6324  |  6324  |  6324  |  6324  |  6324  |  6324  |  —  |  —  |  —  |  —  |  —   
4.1(1) |  —  |  —  |  —  |  6324  |  6324  |  6324  |  6324  |  6324  |  6324  |  —  |  —  |  —  |  —  |  —   
4.0(4) |  6324  |  6324  |  6324  |  6324  |  6324  |  6324  |  6324  |  6324  |  6324  |  —  |  —  |  —  |  —  |  —   
4.0(2) |  6324  |  6324  |  6324  |  6324  |  6324  |  6324  |  —  |  —  |  —  |  —  |  —  |  —  |  —  |  —   
4.0(1) |  6324  |  6324  |  6324  |  6324  |  6324  |  6324  |  —  |  —  |  —  |  —  |  —  |  —  |  —  |  —   
  
The following table lists the mixed B, C bundles that are supported on all platforms with the 4.3(6)A bundle: 

Table 4. Mixed B, C Bundles Supported on All Platforms with the 4.3(6)A Bundle |  Infrastructure Versions (A Bundles)   
---|---  
Host FW Versions (B, C Bundles) |  4.3(6)  
6300  |  6324  |  6400 |  6500 |  UCSX-S9108-100G  
|  **Note** |  Cisco UCSX-S9108-100G supports only Cisco UCS X-Series Servers.  
---|---  
4.3(6) |  Yes |  Yes |  Yes |  Yes |  Yes  
4.3(5) |  Yes |  Yes |  Yes |  Yes |  Yes  
4.3(4) |  Yes |  Yes |  Yes |  Yes |  Yes  
4.3(3) |  Yes |  Yes |  Yes |  Yes |  No  
4.3(2) |  Yes |  Yes |  Yes |  Yes |  No  
4.2(3) |  Yes |  Yes |  Yes |  Yes |  No  
4.2(2) |  Yes |  Yes |  Yes |  Yes |  No  
4.2(1) |  Yes |  Yes |  Yes |  Yes |  No  
4.1(3) |  Yes |  Yes |  Yes |  Yes |  No  
4.1(2) |  Yes |  Yes |  Yes |  No |  No  
4.1(1) |  Yes  |  Yes  |  Yes  |  No |  No  
4.0(1), 4.0(4) (B, C Bundles) |  No |  No |  No |  No |  No  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

If you implement cross-version firmware, you must ensure that the configurations for the Cisco UCS domain are supported by the firmware version on the server endpoints. 

* * *  
  
---|---

---
