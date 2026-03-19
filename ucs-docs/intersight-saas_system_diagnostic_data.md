# Intersight SaaS System Diagnostic Data

| | |
|---|---|
| **URL Title** | Intersight SaaS System Diagnostic Data |
| **URL** | https://intersight.com/help/saas/system/diagnostic_data |
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260316155144543/docs/cloud/data/overview/system/diagnostic_data.html |
| **HTML Title** | Diagnostic Data |
| **Source file** | `ucs-docs-raw/html/intersight-saas_system_diagnostic_data.html` |
| **File type** | HTML |
| **Fetched on** | 2026-03-19 15:36:33 |

---

# Diagnostic Data

Intersight allows you to collect diagnostic data for severs, chassis, and Fabric Interconnects for troubleshooting and further analysis.

## Tech Support Bundle

Cisco Intersight enables Cisco TAC to automatically generate and upload Tech Support Diagnostic files when a Service Request is opened. An account admin can collect the tech support bundle from the Intersight application interface.

To submit a tech support bundle collection request:

  1. Log in to Cisco Intersight with Account Administrator role.

  2. Navigate to System > Diagnostic Data > Tech Support Bundle page.

  3. Click Add Tech Support Bundle.

  4. Enter device’s PID, Platform Type, and Serial.

  5. Click Save.


Once the file is available, it can be downloaded by clicking the download icon located before the relevant file record.

For more information on Configuring Tech Support Bundle Collection, refer the following:

  * For SaaS, see [Configuring Tech Support Bundle Collection](../../../../../../../../../../help/saas/settings#configuring_tech_support_bundle_collection).

  * For Appliance, see [Configuring Tech Support Bundle Collection](../../../../../../../../../../help/appliance/system/settings#configuring_tech_support_bundle_collection).


## Core Files

Cisco Intersight enables you to manage the core diagnostic files generated in the Intersight Managed Mode (IMM) domain. You can view, download, and delete the core files generated on Cisco Integrated Management Controller, Chassis Management Controller, adapters, and switches. These files are useful for identifying and debugging issues within IMM endpoints.

To access and download core files:

  1. Log in to Cisco Intersight with your Cisco ID and select admin role.

  2. Navigate to System > Diagnostic Data > Core Files page.

  3. Click the download icon located before the relevant file record.


Core Files Deletion

Manual Deletion

To manually delete one or more core files, navigate to System > Diagnostic Data > Core Files. From the list view, select the desired file(s) and click the trash icon to remove them.

Auto Deletion

The system automatically deletes core files under the following conditions:

  * If the retention period of the core files has exceeded 30 days.

  * If the disk space usage on the Fabric Interconnects exceeds 82%, the oldest files are deleted first until sufficient disk space is freed.

  * When the Fabric Interconnect is unclaimed, all core files get cleaned up from the core directory.


Note:

Core file management is currently not supported for Cisco UCS Fabric Interconnects 9108 100G.

## Firmware Requirements for Core Files Management

Supported Server| Minimum Firmware Version  
---|---  
Cisco UCS B-Series and X-Series servers| Server firmware version 5.2(2a)Infrastructure firmware version 4.3(4a)  
Cisco UCS C-Series servers| Server firmware version 4.3(4a)Infrastructure firmware version 4.3(4a)