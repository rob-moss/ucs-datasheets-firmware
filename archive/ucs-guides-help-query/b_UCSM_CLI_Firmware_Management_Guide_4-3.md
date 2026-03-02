# Documentation: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Firmware-Mgmt/4-3/b_UCSM_CLI_Firmware_Management_Guide_4-3.html

*Fetched on: 2026-02-27 17:20:16*

---

## Page 1: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Firmware-Mgmt/4-3/b_UCSM_CLI_Firmware_Management_Guide_4-3.html

![Clear Contents of Search](/etc/designs/cdc/fw/i/ic_clear_gray.png)


---

## Page 2: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Firmware-Mgmt/4-3/b_UCSM_CLI_Firmware_Management_Guide_4-3.pdf


---

## Page 3: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Firmware-Mgmt/4-3/b_UCSM_CLI_Firmware_Management_Guide_4-3/b_UCSM_CLI_Firmware_Management_Guide_preface_00.html

## Audience  
  
This guide is intended primarily for data center administrators with responsibilities and expertise in one or more of the following: 

  * Server administration 

  * Storage administration 

  * Network administration 

  * Network security 


---

## Page 4: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Firmware-Mgmt/4-3/b_UCSM_CLI_Firmware_Management_Guide_4-3/m-new-and-changed-information.html

## New and Changed Information

This section provides information on new feature and changed behavior in Cisco UCS Manager, Release 4.3.

Table 1. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(6a) Feature |  Description |  Where Documented  
---|---|---  
Support for Cisco UCS C-Series M8 and Cisco UCS X-Series M8 servers |  Cisco UCS Manager now supports Cisco UCS C240 M8 Server, Cisco UCS C220 M8 Server, and UCS X210c M8 Compute Node.  |  [Server Pack](b_UCSM_CLI_Firmware_Management_Guide_chapter_01.html#concept_307E8D76B75640079C5A6EF6636B2977)  
Table 2. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(5a) Feature  |  Description  |  Where Documented   
---|---|---  
Support for Cisco UCS C-Series M8 and X-Series M8 servers |  Cisco UCS Manager now supports Cisco UCS C225 M8 Server and Cisco UCS X215c M8 Compute Node.  |  [Server Pack](b_UCSM_CLI_Firmware_Management_Guide_chapter_01.html#concept_307E8D76B75640079C5A6EF6636B2977)  
Table 3. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(4b) Feature  |  Description  |  Where Documented   
---|---|---  
Support for Cisco UCS Fabric Interconnects 9108 100G |  Cisco UCS Manager now supports Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct).  | 

  * [Overview](b_UCSM_CLI_Firmware_Management_Guide_chapter_01.html#concept_epr_qzz_pjb)
  * [Components That Support Firmware Upgrade](b_UCSM_CLI_Firmware_Management_Guide_chapter_01.html#concept_k54_vzz_pjb)
  * [Direct Firmware Upgrade at Endpoints](b_UCSM_CLI_Firmware_Management_Guide_chapter_01.html#concept_D45D1AE0617B4A2DA523A6EA1FB27B3A)
  * [Verifying the Ethernet Data Path](b_UCSM_CLI_Firmware_Management_Guide_chapter_010.html#task_9C7303165E1D456F81D0862D05F413AB)
  * [Firmware Upgrades through Auto Install](b_UCSM_CLI_Firmware_Management_Guide_chapter_01.html#concept_4F52361A2A7D4459B64BE93BC9CA566A)
  * [Firmware Image Management](b_UCSM_CLI_Firmware_Management_Guide_chapter_011.html#concept_cfq_2gr_zdb)
  * [Obtaining Software Bundles from Cisco](b_UCSM_CLI_Firmware_Management_Guide_chapter_011.html#task_v5y_2kr_zdb)

  
Table 4. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(4b) Feature  |  Description  |  Where Documented   
---|---|---  
Support for Cisco UCS C-Series M8 server |  Cisco UCS Manager now supports Cisco UCS C245 M8 Server.  |  [Server Pack](b_UCSM_CLI_Firmware_Management_Guide_chapter_01.html#concept_307E8D76B75640079C5A6EF6636B2977)  
Table 5. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(4a) Feature  |  Description  |  Where Documented   
---|---|---  
Cross-Version Firmware Support |  The Cisco UCS Manager A bundle software (Cisco UCS Manager, Cisco NX-OS, IOM and FEX firmware) can be mixed with previous B or C bundle releases on the servers (host firmware [FW], BIOS, Cisco IMC, adapter FW and drivers).  | [Cross-Version Firmware Support](b_UCSM_CLI_Firmware_Management_Guide_chapter_01.html#ucsmRN_43_crossversion)  
Force option to activate capability catalog.  |  Introduction of Force option to activate capability catalog.  |  [Activating a Capability Catalog Update](b_UCSM_CLI_Firmware_Management_Guide_chapter_0100.html#task_67A8990409FF49968F6EFDAFB61C9598)  
Deprecated command |  The show cat-updater command is deprecated.  |  —  
Table 6. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(2c) Feature  |  Description  |  Where Documented   
---|---|---  
Support for Cisco UCS X-Series servers |  Cisco UCS Manager supports Cisco UCS X410c M7 Compute Node.  Cisco UCS X-Series servers support Intelligent Fabric Modules (IFM), which function similarly to the Input/Output Module (IOM) in Cisco UCS B-Series servers.  |  [Server Pack](b_UCSM_CLI_Firmware_Management_Guide_chapter_01.html#concept_307E8D76B75640079C5A6EF6636B2977)  
Table 7. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(2b) Feature  |  Description  |  Where Documented   
---|---|---  
Support for Firmware Upgrade |  Cisco UCS Manager supports Firmware Upgrade to Cisco UCS Manager Release 4.3 version |  [Firmware Upgrade to Cisco UCS Manager Release 4.3](b_UCSM_CLI_Firmware_Management_Guide_chapter_01.html#firmware-upgrade-to-cisco-ucs-manager-release-4.3)  
Support for Cisco UCS C-Series M7 servers. |  Cisco UCS Manager supports the following C-Series M7 servers:

  * Cisco UCS C240 M7 Server
  * Cisco UCS C220 M7 Server

|  [Server Pack](b_UCSM_CLI_Firmware_Management_Guide_chapter_01.html#concept_307E8D76B75640079C5A6EF6636B2977)  
Support for Cisco UCS X9508 server chassis with Cisco UCS X-Series servers |  Cisco UCS Manager supports Cisco UCSX-9508 Chassis with the following Cisco UCS X-Series servers: 

  * Cisco UCS X210c M7 Compute Node
  * Cisco UCS X210c M6 Compute Node

Cisco UCS X-Series servers support Intelligent Fabric Modules (IFM), which function similarly to the Input/Output Module (IOM) in Cisco UCS B-Series servers.  |  [Server Pack](b_UCSM_CLI_Firmware_Management_Guide_chapter_01.html#concept_307E8D76B75640079C5A6EF6636B2977)  
Support for Cisco UCS 6200 Series Fabric Interconnect is deprecated |  Cisco UCS Manager deprecates support for Cisco UCS 6200 Series Fabric Interconnects. |  [Cross-Version Firmware Support](b_UCSM_CLI_Firmware_Management_Guide_chapter_01.html#ucsmRN_43_crossversion)  
Support for Cisco UCS M4 servers are deprecated. |  Cisco UCS Manager deprecates support for UCS B-series, C-series, and S-series M4 servers. |  —


---

## Page 5: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Firmware-Mgmt/4-3/b_UCSM_CLI_Firmware_Management_Guide_4-3/b_UCSM_CLI_Firmware_Management_Guide_chapter_01.html

## Overview  
  
Cisco UCS uses firmware obtained from and certified by Cisco to support the endpoints in a Cisco UCS domain. Each endpoint is a component in the Cisco UCS domain, and requires firmware to function. This guide explains how to obtain firmware and upgrade the endpoints in a Cisco UCS domain by using Cisco UCS Manager. It also details the best practices to be followed while upgrading these endpoints. 

Cisco UCS Manager Release 4.3(4b) introduces the support for Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct) platform offers a compact and integrated solution for smaller-scale data centers by incorporating networking and management directly within the chassis, eliminating the need for separate Fabric Interconnects. It features a single-chassis system with built-in Intelligent Fabric Modules (Cisco UCS 9108 100G Intelligent Fabric Module) for efficient connectivity and high availability, supporting various speeds and allowing flexible port configurations for both LAN and SAN integration.

Cisco UCS Manager Release 4.2(3p) introduces the Cisco UCS 6536 Fabric Interconnect to Cisco UCS 6500 Series Fabric Interconnects. Cisco releases unified Cisco UCS Manager software and firmware upgrades for each of the following platforms with every release of Cisco UCS Manager: 

Cisco UCS Manager Release 4.1(1) introduces the Cisco UCS 64108 Fabric Interconnect to Cisco UCS 6400 Series Fabric Interconnects. 

Cisco releases unified Cisco UCS Manager software and firmware upgrades for each of the following platforms with every release of Cisco UCS Manager: 

  * Cisco UCS Fabric Interconnects 9108 100G with Cisco UCS X-Series servers 

  * Cisco UCS 6500 Series Fabric Interconnect with Cisco UCS B-Series, C-Series, and X-Series servers 

  * Cisco UCS 6400 Series Fabric Interconnect with Cisco UCS B-Series, and C-Series servers 

  * Cisco UCS 6300 Series Fabric Interconnect with Cisco UCS B-Series, and C-Series servers 

  * Cisco UCS 6324 Fabric Interconnect with Cisco UCS B-Series Servers and C-Series servers, which is also known as UCS Mini 


The following images display the different platforms and their respective firmware bundles that Cisco UCS Manager supports, serving as illustrative examples. 

Figure 1. Cisco UCS 6500 Series Fabric Interconnect with Cisco UCS B-Series, C-Series, and X-Series servers  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540998.jpg)

Figure 2. Cisco UCS 6400 Series Fabric Interconnect with Cisco UCS B-Series and C-Series servers  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/306001-307000/306739.jpg)

Figure 3. Cisco UCS 6300 Series Fabric Interconnect with Cisco UCS B-Series and C-Series servers  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/305001-306000/305746.jpg)

Figure 4. Cisco UCS 6324 Fabric Interconnect with Cisco UCS B-Series Servers and C-Series servers    
![](/c/dam/en/us/td/i/300001-400000/300001-310000/305001-306000/305157.jpg)  


Each release has the following firmware bundles: 

  * Infrastructure software bundle—This bundle is also called the A bundle. It contains the firmware images that the fabric interconnects, IO Modules/FI-IO Modules, and Cisco UCS Manager require to function. 

Cisco UCS Manager 4.1 and later releases contain three separate infrastructure bundles: 

  * Cisco UCS X-Series Direct—ucs-x-direct-k9-infra.4.x.x.xxxxxx.A.bin 

  * Cisco UCS 6500 Series Fabric Interconnect—ucs-6500-k9-bundle-infra.4.x.x.xxx.A.bin 

  * Cisco UCS 6400 Series Fabric Interconnect—ucs-6400-k9-bundle-infra.4.x.x.xxx.A.bin 

  * Cisco UCS 6300 Series Fabric Interconnect—ucs-6300-k9-bundle-infra.4.x.x.xxx.A.bin 

  * Cisco UCS 6324 Fabric Interconnect—ucs-mini-k9-bundle-infra.4.x.x.xxx.A.bin 

  * B-Series server software bundle—Also called the B bundle, this bundle contains the firmware images that the B-Series blade servers require to function, such as adapter, BIOS, CIMC, and board controller firmware. Release Bundle Contents for Cisco UCS Managerfor the appropriate 4.x release provides details about the contents of the B-Series server software bundle. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Starting with Cisco UCS Manager Release 3.1(2), the firmware for endpoints that are common to both the B-Series and C-Series server software bundles, such as local disk, is available in both the B-Series and C-Series server software bundles. 

* * *  
  
---|---  
  * C-Series server software bundle—Also called the C bundle, this bundle contains the firmware images that the C-Series rack-mount servers require to function, such as adapter, BIOS, CIMC, and board controller firmware. The C bundle also contains the firmware images for Cisco UCS S3260 storage servers. Release Bundle Contents for Cisco UCS Manager  for the appropriate 4.1 or later release provides details about the contents of the C-Series server software bundle. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Starting with Cisco UCS Manager Release 3.1(2), the firmware for endpoints that are common to both the B-Series and C-Series server software bundles, such as local disk, is available in both the B-Series and C-Series server software bundles. 

* * *  
  
---|---  
  * Capability catalog software bundle—Also called the T bundle, this bundle specifies implementation-specific tunable parameters, hardware specifics. and feature limits. 

Cisco UCS Manager uses the capability catalog to update the display and configurability of server components such as newly qualified DIMMs and disk drives. The Cisco UCS Manager Capability Catalog is a single image, but it is also embedded in Cisco UCS Manager software. Cisco UCS Manager Release 4.1 and later releases work with any 4.1 or later catalog file, but not with 4.0 or 3.2 catalog versions. If a server component is not dependent on a specific BIOS version, using it and having it recognized by Cisco UCS Manager is primarily a function of the catalog version. In addition to the catalog being bundled with UCS infrastructure releases, it can, sometimes, also be released as a standalone image. 


The upgrade order for the endpoints in a Cisco UCS domain depends upon the upgrade path. 

See the required order of steps for your upgrade path to determine the appropriate order in which to upgrade the endpoints in your Cisco UCS domain. 

Cisco maintains a set of best practices for managing firmware images and updates in this document and in the following technical note: [Unified Computing System Firmware Management Best Practices](http://www.cisco.com/en/US/products/ps10281/products_configuration_example09186a0080aee43e.shtml). 

This document uses the following definitions for managing firmware: 

  * Update—Copies the firmware image to the backup partition on an endpoint. 

  * Activate—Sets the firmware in the backup partition as the active firmware version on the endpoint. Activation can require or cause the reboot of an endpoint. 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For capability catalog upgrades, update and activate occur simultaneously. You only need to update or activate those upgrades. You do not need to perform both steps. 

* * *  
  
---|---  
  
### Cisco UCS Manager User CLI Documentation

Cisco UCS Manager offers you a set of smaller, use-case based documentation described in the following table: 

Guide  |  Description   
---|---  
[Cisco UCS Manager Getting Started Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses Cisco UCS architecture and Day 0 operations, including Cisco UCS Manager initial configuration, and configuration best practices.   
[Cisco UCS Manager Administration Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses password management, role-based access configuration, remote authentication, communication services, CIMC session management, organizations, backup and restore, scheduling options, BIOS tokens and deferred deployments.   
[Cisco UCS Manager Infrastructure Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses physical and virtual infrastructure components used and managed by Cisco UCS Manager.   
[Cisco UCS Manager Firmware Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses downloading and managing firmware, upgrading through Auto Install, upgrading through service profiles, directly upgrading at endpoints using firmware auto sync, managing the capability catalog, deployment scenarios, and troubleshooting.   
[Cisco UCS Manager Server Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses the new licenses, registering Cisco UCS domains with Cisco UCS Central, power capping, server boot, server profiles and server-related policies.   
[Cisco UCS Manager Storage Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses all aspects of storage management such as SAN and VSAN in Cisco UCS Manager.   
[Cisco UCS Manager Network Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses all aspects of network management such as LAN and VLAN connectivity in Cisco UCS Manager.   
[Cisco UCS Manager System Monitoring Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses all aspects of system and health monitoring including system statistics in Cisco UCS Manager.   
[Cisco UCS S3260 Server Integration with Cisco UCS Manager](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses all aspects of management of UCS S-Series servers that are managed through Cisco UCS Manager. 


---

## Page 6: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Firmware-Mgmt/4-3/b_UCSM_CLI_Firmware_Management_Guide_4-3/b_UCSM_CLI_Firmware_Management_Guide_chapter_010.html

## Guidelines, and Best Practices for Firmware Upgrades   
  
Before you upgrade the firmware for any endpoint in a Cisco UCS domain, consider the following guidelines, best practices, and limitations: 

### Configuration Changes and Settings that Can Impact Upgrades 

Depending on the configuration of your Cisco UCS domain, the upgrade process may require you to make additional changes. 

#### Default Maintenance Policy Should be Configured for User Acknowledgment 

The default maintenance policy is configured to immediately reboot the server when disruptive changes are made to the service profile, such as server firmware upgrades through a host maintenance policy. We recommend that you change the reboot policy setting in the default maintenance policy to user acknowledgment to avoid unexpected disruption of server traffic. 

When you configure the reboot policy in the default maintenance policy to user acknowledgment, the list of disruptive changes are listed with the pending activities. You can then control when the servers are rebooted. 

#### Overlapping FCoE VLAN IDs and Ethernet VLAN IDs Are No Longer Allowed with Cisco UCS Release 2.0 and Higher 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

In Cisco UCS 1.4 and earlier releases, Ethernet VLANs and FCoE VLANs could have overlapping VLAN IDs. However, starting with Cisco UCS release 2.0, overlapping VLAN IDs are not allowed. If Cisco UCS Manager detects overlapping VLAN IDs during an upgrade, it raises a critical fault. If you do not reconfigure your VLAN IDs, Cisco UCS Manager raises a critical fault and drops Ethernet traffic from the overlapped VLANs. Therefore, we recommend that you ensure there are no overlapping Ethernet and FCoE VLAN IDs before you upgrade to Cisco UCS Release 3.1 and later releases.  Be aware that when an uplink trunk is configured with VLAN ID 1 defined and set as the native VLAN, changing the Ethernet VLAN 1 ID to another value can cause network disruption and flapping on the fabric interconnects, resulting in an HA event that introduces a large amount of traffic and makes services temporarily unavailable. 

* * *  
  
---|---  
  
For a new installation of Cisco UCS Release 3.1 and later releases, the default VLAN IDs are as follows: 

  * The default Ethernet VLAN ID is 1. 

  * The default FCoE VLAN ID is 4048. 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

If a Cisco UCS domain uses one of the default VLAN IDs, which results in overlapping VLANs, you can change one or more of the default VLAN IDs to any VLAN ID that is not used or reserved. From release 2.0 and higher, VLANs with IDs from 4043 to 4047 are reserved. 

* * *  
  
---|---  
  
#### VSANs with IDs in the Reserved Range are not Operational 

A VSAN with an ID in the reserved range is not operational after an upgrade. Make sure that none of the VSANs configured in Cisco UCS Manager are in these reserved ranges: 

  * If you plan to use FC switch mode in a Cisco UCS domain, do not configure VSANs with an ID in the range from 3040 to 4078. 

  * If you plan to use FC end-host mode in a Cisco UCS domain, do not configure VSANs with an ID in the range from 3840 to 4079. 


If a VSAN has an ID in the reserved range, change that VSAN ID to any VSAN ID that is not used or reserved. 

### Hardware-Related Guidelines for Firmware Upgrades 

The hardware in a Cisco UCS domain can impact how you upgrade. Before you upgrade any endpoint, consider the following guidelines and limitations: 

#### No Server or Chassis Maintenance 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Do not remove the hardware that contains the endpoint or perform any maintenance on it until the update process completes. If the hardware is removed or otherwise unavailable due to maintenance, the firmware update fails. This failure might corrupt the backup partition. You cannot update the firmware on an endpoint with a corrupted backup partition. 

* * *  
  
---|---  
  
#### Avoid Replacing RAID-Configured Hard Disks During or Prior to Upgrade 

During or prior to Cisco UCS infrastructure and server firmware upgrades: 

  * Do not remove, insert or replace any local storage hard disks or SSDs in the servers. 

  * Ensure that no storage operations are running, including Rebuild, Association, Copyback, BGI, and so on. 


#### Always Upgrade Third-Party Adapters through a Host Firmware Package 

You cannot upgrade third-party adapters directly at the endpoints. You must upgrade the firmware on those adapters through a host firmware package. 

#### Configure the Fabric Interconnects 

The clustered fabric interconnects provide data path redundancy by design. However, to ensure that data traffic is not disrupted, you must configure redundant Ethernet and storage (FC/FCoE) interfaces within the service profile. You must also ensure that the corresponding Operating System is configured correctly to handle one fabric path outage. 

For a  non-cluster configuration with a single fabric interconnect, you can minimize the disruption to data traffic when you perform a direct firmware upgrade of the endpoints. However, you must reboot the fabric interconnect to complete the upgrade and, therefore, cannot avoid disrupting traffic. 

### Firmware- and Software-Related Guidelines for Upgrades 

Before you upgrade any endpoint, consider the following guidelines and limitations: 

#### Determine the Appropriate Type of Firmware Upgrade for Each Endpoint 

Some endpoints, such as Cisco adapters and the server CIMC, can be upgraded through either a direct firmware upgrade or a firmware package included in a service profile. The configuration of a Cisco UCS domain determines how you upgrade these endpoints. If the service profiles associated with the servers include a host firmware package, upgrade the adapters for those servers through the firmware package. 

Upgrades of an adapter through a firmware package in the service profile associated with the server take precedence over direct firmware upgrades. You cannot directly upgrade an endpoint if the service profile associated with the server includes a firmware package. To perform a direct upgrade, you must remove the firmware package from the service profile. 

#### Do Not Activate All Endpoints Simultaneously in Cisco UCS Manager GUI

If you use Cisco UCS Manager GUI to update the firmware, do not select ALL from the Filter drop-down list in the Activate Firmware dialog box to activate all endpoints simultaneously. Many firmware releases and patches have dependencies that require the endpoints to be activated in a specific order for the firmware update to succeed. This order can change depending upon the contents of the release or patch. Activating all endpoints does not guarantee that the updates occur in the required order, and can disrupt communications between the endpoints and the fabric interconnects and Cisco UCS Manager. For information about the dependencies in a specific release or patch, see the release notes provided with that release or patch. 

#### Determine Available Bootflash and Workspace Partition 

The bootflash partition is dedicated solely to firmware images managed by Cisco UCS Manager. To initiate upgrade or downgrade, at least 20 percent of the bootflash partition must be available. When the bootflash partition exceeds 70 percent, faults are raised, but Auto Install proceeds. When the bootflash partition exceeds 80 percent, faults are raised and Auto Install does not proceed. 

The workspace partition on the fabric interconnect stores tech support files, core files, and the debug plugin. To initiate upgrade or downgrade, at least 20 percent of the workspace partition must be available. 

#### Determine the Impact of Activation for Adapters and I/O Modules 

During a direct upgrade, you should configure Set Startup Version Only for an adapter. With this setting, the activated firmware moves into the pending-next-boot state, and the server is not immediately rebooted. The activated firmware does not become the running version of firmware on the adapter until the server is rebooted. You cannot configure Set Startup Version Only for an adapter in the host firmware package. 

If a server is not associated with a service profile, the activated firmware remains in the pending-next-boot state. Cisco UCS Manager does not reboot the endpoints or activate the firmware until the server is associated with a service profile. If necessary, you can manually reboot or reset an unassociated server to activate the firmware. 

When you configure Set Startup Version Only for an I/O module, the I/O module is rebooted when the fabric interconnect in its data patch is rebooted. If you do not configure Set Startup Version Only for an I/O module, the I/O module reboots and disrupts traffic. In addition, if Cisco UCS Manager detects a protocol and firmware version mismatch between the fabric interconnect and the I/O module, Cisco UCS Manager automatically updates the I/O module with the firmware version that matches the firmware in the fabric interconnect and then activates the firmware and reboots the I/O module again. 

#### Disable Call Home before Upgrading to Avoid Unnecessary Alerts (Optional) 

When you upgrade a Cisco UCS domain, Cisco UCS Manager restarts the components to complete the upgrade process. This restart causes events that are identical to the service disruptions and component failures that trigger Call Home alerts to be sent. If you do not disable Call Home before you begin the upgrade, alerts will be generated by the upgrade-related component, restarts and notifications will be sent out based on your Call Home configuration. 

#### Fabric Interconnect Traffic Evacuation 

Fabric interconnect traffic evacuation, introduced in Release 2.2(4), is the ability to evacuate all traffic that flows through a fabric interconnect from all servers attached to it through an IOM or FEX, while upgrading a system. 

Upgrading the subordinate fabric interconnect in a system disrupts the traffic that is active on the fabric interconnect. This traffic fails over to the primary fabric interconnect. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

  * Fabric interconnect traffic evacuation is supported only in a cluster configuration. 
  * You can evacuate traffic only from the subordinate fabric interconnect. 
  * The IOM or FEX backplane ports of the fabric interconnect on which evacuation is configured will go down, and their state will appear as Admin down. During the manual upgrade process, to move these backplane ports back to the Up state and resume traffic flow, you must explicitly configure Admin Evac Mode as Off. 


* * *  
  
---|---  
  
You can perform fabric evacuation as follows during the manual upgrade process:

  1. Stop all the traffic that is active through a fabric interconnect by configuring Admin Evac Mode as On. 

  2. For vNICs configured with failover, verify that the traffic has failed over by using Cisco UCS Manager or tools such as vCenter. 

  3. Upgrade the subordinate fabric interconnect. 

  4. Restart all the stopped traffic flows by configuring Admin Evac Mode as Off. 

  5. Change the cluster lead to the subordinate fabric interconnect. 

  6. Repeat steps 1 to 4 and upgrade the other fabric interconnect. 


##### Fabric Evacuation with Auto Install

Starting with Cisco UCS Manager Release 3.1(3), you can use fabric evacuation during Auto Install. While initiating Auto Install, when you enable fabric evacuation and then begin Auto Install, the following sequence of events occur: 

  1. The subordinate fabric interconnect (FI-B) is evacuated and activated.

  2. Failover occurs and the primary fabric interconnect (FI-A) becomes the subordinate fabric interconnect. FI-B now becomes the cluster lead. 

  3. FI-A is now evacuated and activated.


If you use fabric evacuation with Auto Install, and fabric evacuation was enabled on the fabric interconnect before Auto Install, fabric evacuation is disabled after Auto Install is complete. 

Ensure that you do not initiate Auto Install with fabric evacuation enabled on the primary fabric interconnect. If fabric evacuation was manually enabled on the primary fabric interconnect before Auto Install, it must be manually disabled before initiating Auto Install. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

  * Fabric interconnect traffic evacuation is supported only in a cluster configuration.
  * You can evacuate traffic only from the subordinate fabric interconnect.
  * The IOM or FEX backplane ports of the fabric interconnect on which evacuation is configured will go down, and their state will appear as Admin down. These backplane ports will move back to Up state after Auto Install is complete. 


* * *  
  
---|---  
  
##### Stopping Traffic on a Fabric Interconnect 

###### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A # scope fabric-interconnect {a | b}  |  Enters fabric interconnect mode for the specified Fabric Interconnect.   
**Step 2** |  UCS-A /fabric-interconnect # stop server traffic [force]  |  Stops all the traffic that is active through the specified Fabric Interconnect.  Use the force option to evacuate a Fabric Interconnect irrespective of its current evacuation state.   
**Step 3** |  UCS-A /fabric-interconnect # commit-buffer |  Commits the transaction to the system configuration.   
  
###### Example

This example shows how to stop all traffic that is active through Fabric Interconnect B: 
    
    
    UCS-A# **scope fabric-interconnect b**
    UCS-A /fabric-interconnect # **stop server traffic**
    Warning: Enabling fabric evacuation will stop all traffic through this Fabric Interconnect from servers attached through IOM/FEX. The traffic will fail over to the Primary Fabric Interconnect for fail over vnics.
    UCS-A /fabric-interconnect # **commit-buffer**
    
    
    

##### Restarting Traffic on a Fabric Interconnect 

###### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A # scope fabric-interconnect {a | b}  |  Enters fabric interconnect mode for the specified Fabric Interconnect.   
**Step 2** |  UCS-A /fabric-interconnect # start server traffic |  Restarts traffic through the specified Fabric Interconnect.   
**Step 3** |  UCS-A /fabric-interconnect # commit-buffer |  Commits the transaction to the system configuration.   
  
###### Example

This example shows how to restart traffic through Fabric Interconnect B: 
    
    
    UCS-A# **scope fabric-interconnect b**
    UCS-A /fabric-interconnect # **start server traffic**
    Warning: Resetting fabric evacuation will cause server traffic that failed over to the Primary Fabric Interconnect to fail back to this Fabric Interconnect.
    UCS-A /fabric-interconnect # **commit-buffer**
    
    
    

##### Verifying Fabric Evacuation 

###### Procedure

Command or Action | Purpose  
---|---  
UCS-A# show service-profile circuit server server-id |  Shows the network circuit information for the service profile associated with the specified server.   
  
###### Example

This example shows the VIF paths before fabric evacuation. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

  * VIF at Fabric Interconnect A shows that traffic is initially active through the Fabric interconnect. 
  * VIF at Fabric Interconnect B is passive before evacuation. 


* * *  
  
---|---  
      
    
    UCS-A# **show service-profile circuit server 1/6**
    Service Profile: test1
    Server: 1/6
        Fabric ID: A
            Path ID: 1
            VIF        vNIC            Link State  Oper State Prot State    Prot Role   Admin Pin  Oper Pin   Transport
            ---------- --------------- ----------- ---------- ------------- ----------- ---------- ---------- ---------
                   692 eth0            Up          Active     Active        Primary     0/0        1/15       Ether
        Fabric ID: B
            Path ID: 1
            VIF        vNIC            Link State  Oper State Prot State    Prot Role   Admin Pin  Oper Pin   Transport
            ---------- --------------- ----------- ---------- ------------- ----------- ---------- ---------- ---------
                   693 eth0            Up          Active     Passive       Backup      0/0        1/15       Ether
    UCS-A#
    
    
    

This example shows the VIF paths after Fabric Interconnect A is evacuated. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

  * After fail over, the VIF state at Fabric Interconnect A goes into error. 
  * VIF at Fabric Interconnect B takes over as active. 


* * *  
  
---|---  
      
    
    UCS-A# **show service-profile circuit server 1/6**
    Service Profile: test1
    Server: 1/6
        Fabric ID: A
            Path ID: 1
            VIF        vNIC            Link State  Oper State Prot State    Prot Role   Admin Pin  Oper Pin   Transport
            ---------- --------------- ----------- ---------- ------------- ----------- ---------- ---------- ---------
                   692 eth0            Error       Error      Active        Primary     0/0        0/0        Ether
        Fabric ID: B
            Path ID: 1
            VIF        vNIC            Link State  Oper State Prot State    Prot Role   Admin Pin  Oper Pin   Transport
            ---------- --------------- ----------- ---------- ------------- ----------- ---------- ---------- ---------
                   693 eth0            Up          Active     Passive       Backup      0/0        1/15       Ether
    UCS-A#
    

##### Displaying the Status of Evacuation at a Fabric Interconnect 

###### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A # scope fabric-interconnect {a | b}  |  Enters fabric interconnect mode for the specified Fabric Interconnect.   
**Step 2** |  UCS-A /fabric-interconnect # show detail |  Displays details about the specified Fabric Interconnect.   
  
###### Example

This example shows how to display the detailed status of a Fabric Interconnect. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Admin Evacuation and Oper Evacuation show the status of evacuation at the Fabric Interconnect. 

* * *  
  
---|---  
      
    
     UCS-A /fabric-interconnect # **show detail**
    
    Fabric Interconnect:
        ID: B
        Product Name: Cisco UCS 6248UP
        PID: UCS-FI-6248UP
        VID: V01
        Vendor: Cisco Systems, Inc.
        Serial (SN): SSI171400HG
        HW Revision: 0
        Total Memory (MB): 16165
        OOB IP Addr: 10.193.32.172
        OOB Gateway: 10.193.32.1
        OOB Netmask: 255.255.255.0
        OOB IPv6 Address: ::
        OOB IPv6 Gateway: ::
        Prefix: 64
        Operability: Operable
        Thermal Status: Ok
        Admin Evacuation: On
        Oper Evacuation: On
        Current Task 1:
        Current Task 2:
        Current Task 3:
    
    
    

#### Secure Firmware Update 

Cisco UCS Manager, Release 3.1(2) introduces secure firmware update, which enables you to update the adapter firmware securely for third-party Intel network and storage adapters. Only server administrators can upgrade or downgrade firmware for the adapters. OS administrators with root privileges are not allowed to downgrade the adapter firmware. 

The following Cisco UCS servers support secure firmware update: 

##### Secure Firmware Update Supported Network Adapters and Storage Disks 

###### Supported Storage Disks on Cisco Blade Servers 

The following Intel NVMe storage disks support secure firmware update on Cisco UCS B200 M5 Server and Cisco UCS B480 M5 Server. 

Table 1. Supported NVMe Storage Disks  NVMe Storage Disks   
---  
UCSC-NVMEHW-H800  
UCSC-NVMEHW-H1600  
UCSC-NVMEHW-H3200  
UCSC-NVMEHW-H6400  
UCSC-NVMEHW-H7680  
  
###### Supported Network Adapters and Storage Disks on Cisco Rack Servers 

The following NVMe storage disks support secure firmware update on Cisco UCS C220 M5 Server, Cisco UCS C240 M5 Server, and Cisco UCS C480 M5 Server servers: 

Table 2. Supported NVMe Storage Disks  NVMe Storage Disks   
---  
UCSC-NVMEHW-H800  
UCSC-NVMEHW-H1600  
UCSC-NVMEHW-H3200  
UCSC-NVMEHW-H6400  
UCSC-NVMEHW-H7680  
UCSC-NVME-H16003 to UCSC-F-H16003  
UCSC-NVME-H32003  
UCSC-NVME-H38401  
UCSC-NVME-H64003  
UCSC-NVME-H76801  
  
##### Guidelines for Secure Firmware Support on Cisco UCS Servers 

Cisco UCS Manager Release 3.1(2) introduces support for secure firmware update. For Cisco UCS M5 servers, secure firmware update is introduced in Cisco UCS Manager Release 3.2(2).

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

Ensure that CIMC is running Version 2.0(13) or later and Cisco UCS Manager is running Release 3.1(2) or later releases. Secure firmware update cannot be done when the CIMC is running a version earlier than 2.0(13) and Cisco UCS Manager is running a release earlier than Release 3.1(2). 

* * *  
  
---|---  
  
###### Guidelines for Blade Servers 

For secure firmware update on , B200 M5, and B480 M5 servers, do the following: 

  * Install the UCSB-LSTOR-PT storage controller and insert the NVMe disks on a Cisco UCS B200 M5 or B480 M5 server. 

  * Reacknowledge the server. Refer to the Reacknowledging a Blade Server section in the Cisco UCS Manager Infrastructure Management Guide, Release 3.2. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Ensure that server discovery does not fail and the NVMe disks are identified by CIMC and BIOS. After the server is associated to the service profile with the default host firmware package, Auto Install is triggered. NVMe disks can be updated with the latest firmware during Auto Install.  Cisco UCS Manager, Release 3.2(1) supports NVMe boot. 

* * *  
  
---|---  


###### Guidelines for Rack Servers 

For secure firmware update on Cisco UCS C460, C240, C220 M5 servers and C480 M5 servers, do the following: 

  * Reacknowledge the Cisco UCS servers. Refer to the Reacknowledging a Rack Server section in the Cisco UCS Manager Infrastructure Management Guide, Release 3.2. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Ensure that server discovery does not fail and the NVMe disks are identified by CIMC and BIOS. After the server is associated to the service profile with the default host firmware package, Auto Install is triggered. NVMe disks can be updated with the latest firmware during Auto Install.  Cisco UCS Manager, Release 3.2(1) supports NVMe boot. 

* * *  
  
---|---  


### Cautions, and Guidelines for Upgrading with Auto Install

Before you use Auto Install to upgrade the firmware for any endpoint in a Cisco UCS domain, consider the following cautions, guidelines, and limitations: 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

These guidelines are specific to Auto Install and are in addition to those listed in Guidelines, and Best Practices for Firmware Upgrades. 

* * *  
  
---|---  
  
#### State of the Endpoints 

Before you begin an upgrade, all affected endpoints must be as follows: 

  * For a cluster configuration, verify that the high availability status of the fabric interconnects shows that both are up and running. 

  * For a  non-cluster configuration, verify that the Overall Status of the fabric interconnect is Operable. 

  * For all endpoints to be upgraded, verify that they are in an Operable state. 

  * For all servers to be upgraded, verify that all the servers have been discovered and that discovery did not fail. Install Server Firmware will fail if any server endpoints cannot be upgraded. 

  * For each server to be upgraded, check the running firmware version on the storage controller and local disks, and verify that they are in the Ready state. 


#### Recommendations for the Default Host Firmware Policy 

After you upgrade Cisco UCS Manager, a new host firmware policy named "default" is created, and is assigned to all service profiles that did not already include a host firmware policy. The default host firmware policy is blank. It does not contain any firmware entries for any components. This default policy is also configured for an immediate reboot rather than waiting for user acknowledgment before rebooting the servers. 

During the upgrade of server firmware, you can modify the default host firmware policy to add firmware for the blade and rack-mount servers in the Cisco UCS domain. To complete the upgrade, all servers must be rebooted. 

Every service profile that is assigned to the default host firmware policy reboots the associated server according to the maintenance policy included in the service profile. If the maintenance policy is set to immediate reboot, you cannot cancel the upgrade or prevent the servers from rebooting after you complete the configuration in the Install Server Firmware wizard. We recommend that you verify the maintenance policy associated with these service profiles to ensure that they are set for a timed reboot or for user acknowledgment. 

#### Time, Date, and Time Zone on Fabric Interconnects Must Be Identical 

To ensure that the fabric interconnects in a cluster configuration are in sync, you must ensure that they are configured for the same date, time, and time zone. We recommend that you configure an NTP server and the correct time zone in both fabric interconnects. If the date, time or time zone in the fabric interconnects are out of sync, the Auto Install might fail. 

#### Cannot Upgrade Infrastructure and Server Firmware Simultaneously 

You cannot upgrade the infrastructure firmware at the same time as you upgrade server firmware. We recommend that you upgrade the infrastructure firmware first and then upgrade the server firmware. Do not begin the server firmware upgrade until the infrastructure firmware upgrade is completed. 

#### Required Privileges 

Users must have the following privileges to upgrade endpoints with Auto Install: 

Privileges  | Upgrade Tasks User Can Perform   
---|---  
admin  | 

  * Run Install Infrastructure Firmware
  * Run Install Server Firmware
  * Add, delete, and modify host firmware packages 

  
Service profile compute (ls-compute)  |  Run Install Server Firmware  
Service profile server policy (ls-server-policy)  |  Add, delete, and modify host firmware packages   
Service profile config policy (ls-config-policy)  |  Add, delete, and modify host firmware packages   
  
#### Impact of Host Firmware Packages on Install Server Firmware

Because Install Server Firmware uses host firmware packages to upgrade the servers, you do not have to upgrade all servers in a Cisco UCS domain to the same firmware versions. However, all servers which have associated service profiles that include the host firmware packages you selected when you configured Install Server Firmware are upgraded to the firmware versions in the specified software bundles. 

#### Effect of Using Install Server Firmware on Servers Whose Service Profiles Do Not Include a Host Firmware Package 

If you use Install Server Firmware to upgrade server endpoints on servers that have associated service profiles without host firmware packages, Install Server Firmware uses the default host firmware package to upgrade the servers. You can only update the default host firmware package through Install Server Firmware. 

If you want to upgrade the CIMC or adapters in a server with an associated service profile that has previously been updated through the default host firmware package in Install Server Firmware, you must use one of the following methods: 

  * Use Install Server Firmware to modify the default host firmware package and then upgrade the server through Install Server Firmware. 

  * Create a new host firmware package policy, assign it to the service profile associated with the server, and then upgrade the server through that host firmware package policy. 

  * Disassociate the service profile from the server and then directly upgrade the server endpoints. 


#### Upgrading Server Firmware on Newly Added Servers 

If you add a server to a Cisco UCS domain after you run Install Server Firmware, the firmware on the new server is not automatically upgraded by Install Server Firmware. If you want to upgrade the firmware on a newly added server to the firmware version used when you last ran Install Server Firmware, you must manually upgrade the endpoints to upgrade the firmware on that server. Install Server Firmware requires a change in firmware version each time. You cannot rerun Install Server Firmware to upgrade servers to the same firmware version. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

After you finish the upgrade, you can use the Firmware Auto Sync Server policy in Cisco UCS Manager to automatically update newly discovered servers. 

* * *  
  
---|---


---

## Page 7: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Firmware-Mgmt/4-3/b_UCSM_CLI_Firmware_Management_Guide_4-3/b_UCSM_CLI_Firmware_Management_Guide_chapter_011.html

##  Download and Manage Firmware in Cisco UCS Manager   
  
### Firmware Image Management

Cisco delivers all firmware updates to Cisco UCS components in bundles of images. Each image represents an individual firmware package specific to one hardware component. For example: IOM image, Cisco UCS Manager image, and so on.Cisco UCS firmware updates are available to be downloaded to fabric interconnects in a Cisco UCS domain in the following bundles: 

Cisco UCS Infrastructure Software Bundle
    

Cisco UCS Manager includes infrastructure bundles that contain firmware images required to update components such as:

  * Cisco UCS Manager software 

  * Kernel and system firmware for the fabric interconnects 

  * I/O module/FI-IO module firmware

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCS X-Series Direct, Cisco UCS 6500 Series Fabric Interconnects, Cisco UCS 6400 Series Fabric Interconnects do not have separate kickstart and system images. 

* * *  
  
---|---  

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The UCS infrastructure bundle for one platform cannot be used to activate another platform. 

* * *  
  
---|---  
Cisco UCS B-Series Blade Server Software Bundle
    

This bundle includes the following firmware images that are required to update the firmware for the blade servers in a Cisco UCS domain. In addition to the bundles created for a release, these bundles can also be released between infrastructure bundles to enable Cisco UCS Manager to support a blade server that is not included in the most recent infrastructure bundle. 

  * CIMC firmware 

  * BIOS firmware 

  * Adapter firmware 

  * Board controller firmware 

  * Third-party firmware images required by the new server 


     ![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For all server components where firmware updates are applicable (such as CIMC, BIOS, or Disk), when the firmware version of a component is the same across two different firmware packages, Cisco UCS Manager selects the component firmware from the package with the latest package version.  This behavior prioritizes the latest package version for the component firmware rather than strictly adhering to the firmware version specified in the Host Firmware Package (HFP) policy associated with the server. This behavior ensures that the most recent package version is used for firmware components when versions are identical, potentially overriding the HFP policy version. 

* * *  
  
---|---  
Cisco UCS C-Series Rack-Mount UCS-Managed Server Software Bundle
    

This bundle includes the following firmware images that are required to update components on rack-mount servers that have been integrated with and are managed by Cisco UCS Manager: 

  * CIMC firmware 

  * BIOS firmware 

  * Adapter firmware 

  * Storage controller firmware 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

You cannot use this bundle for standalone C-series servers. The firmware management system in those servers cannot interpret the header required by Cisco UCS Manager. For information on how to upgrade standalone C-series servers, see the C-series configuration guides. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For all server components where firmware updates are applicable (such as CIMC, BIOS, or Disk), when the firmware version of a component is the same across two different firmware packages, Cisco UCS Manager selects the component firmware from the package with the latest package version.  This behavior prioritizes the latest package version for the component firmware rather than strictly adhering to the firmware version specified in the Host Firmware Package (HFP) policy associated with the server. This behavior ensures that the most recent package version is used for firmware components when versions are identical, potentially overriding the HFP policy version. 

* * *  
  
---|---  
  
Cisco also provides release notes, which you can obtain on the same website from which you obtained the bundles.

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Ensure that before starting the auto-install process, you capture the data according to [Verification that the Data Path is Ready](b_UCSM_CLI_Firmware_Management_Guide_chapter_010.html#concept_7406EAC0852E4A52968DFBAE84E1A1C8). 

  * Before acknowledging the pending activity during auto-install, it is important to confirm that all the subordinate VIF paths are rebuilt. 
  * Ensure that you monitor the UCS VIF paths only from the CLI and not from the faults within the UCS Manager GUI.
  * If you fail to monitor the UCS VIF paths, it may result in partial or complete "All Paths Down" state.

We recommend that you follow the guidelines prior to any processes that require reboot of both Fabric Interconnects.

* * *  
  
---|---  
  
**Recommendation:** Before starting any firmware upgrade or downgrade, refer [Cisco UCS Manager Upgrade and Downgrade Matrix](https://www.cisco.com/c/dam/en/us/td/docs/unified_computing/ucs/ucs-manager/UCSM-upgrade-downgrade-matrix/index.html). 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For more information, see [Cisco UCS Manager Release Bundle Contents](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-release-notes-list.html). 

* * *  
  
---|---  
  
#### Firmware Image Headers

Every firmware image has a header, which includes the following:

  * Checksum

  * Version information

  * Compatibility information that the system can use to verify the compatibility of component images and any dependencies


#### Firmware Image Catalog 

Cisco UCS Manager maintains an inventory of all available images. The image catalog contains a list of images and packages. A package is a read-only object that is created when it is downloaded. It does not occupy disk space and represents a list or collection of images that were unpacked as part of the package download. When an individual image is downloaded, the package name remains the same as the image name. 

Cisco UCS Manager provides you with two views of the catalog of firmware images and their contents that have been downloaded to the fabric interconnect: 

Packages 
    

This view provides you with a read-only representation of the firmware bundles that have been downloaded onto the fabric interconnect. This view is sorted by image, not by the contents of the image. For packages, you can use this view to see which component images are in each downloaded firmware bundle. 

Images 
    

The images view lists the component images available on the system. You cannot use this view to see complete firmware bundles or to group the images by bundle. The information available about each component image includes the name of the component, the image size, the image version, and the vendor and model of the component. 

You can use this view to identify the firmware updates available for each component. You can also use this view to delete obsolete and unneeded images. After all the images in the package have been deleted, Cisco UCS Manager deletes the package itself. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/tip.gif)  
**Tip** | 

* * *

Cisco UCS Manager stores the images in bootflash on the fabric interconnect. In a cluster system, space usage in bootflash on both fabric interconnects is the same, because all images are synchronized between them. Faults are raised when the bootflash partition exceeds 70 percent and total used space exceeds 90 percent. If Cisco UCS Manager generates such a fault, delete obsolete images to free up space. 

* * *  
  
---|---  
  
### Obtaining Software Bundles from Cisco

#### Before you begin

Determine which of the following software bundles you need in order to update the Cisco UCS domain: 

  * Cisco UCS Infrastructure Software Bundle for Cisco UCS Fabric Interconnects 9108 100G, Cisco UCS 6500 Series Fabric Interconnect, Cisco UCS 6400 Series Fabric Interconnect, 6300 Series Fabric Interconnects—Required for all Cisco UCS domains. 

  * Cisco UCS B-Series Blade Server Software Bundle—Required for all Cisco UCS domains that include blade servers. 

  * Cisco UCS C-Series Rack-Mount UCS-Managed Server Software Bundle—Only required for Cisco UCS domains that include integrated rack-mount servers. This bundle contains firmware to enable Cisco UCS Manager to manage those servers and is not applicable to standalone C-Series rack-mount servers. 


#### Procedure

* * *

**Step 1** |  In a web browser, navigate to [ Cisco.com](http://www.cisco.com).   
---|---  
**Step 2** |  Under Support, click All Downloads.   
**Step 3** |  In the center pane, click Servers - Unified Computing.   
**Step 4** |  If prompted, enter your Cisco.com username and password to log in.   
**Step 5** |  In the right pane, click the link for the software bundles you require, as follows:  | Bundle  | Navigation Path  
---|---  
Cisco UCS Infrastructure Software Bundle for Cisco UCS Fabric Interconnects 9108 100G, Cisco UCS 6500 Series Fabric Interconnect, Cisco UCS 6400 Series Fabric Interconnect, 6300 Series Fabric Interconnects,  and 6324 Fabric Interconnects  |  Click UCS Infrastructure and UCS Manager Software > Unified Computing System (UCS) Infrastructure Software Bundle.   
Cisco UCS B-Series Blade Server Software Bundle |  Click UCS B-Series Blade Server Software > Unified Computing System (UCS) Server Software Bundle.   
Cisco UCS C-Series Rack-Mount UCS-Managed Server Software Bundle |  Click UCS C-Series Rack-Mount UCS-Managed Server Software > Unified Computing System (UCS) Server Software Bundle.   
**Tip** |  The Unified Computing System (UCS) Documentation Roadmap Bundle, which is accessible through these paths, is a downloadable ISO image of all Cisco UCS documentation.   
---|---  
**Step 6** |  On the first page from which you download a software bundle, click the Release Notes link to download the latest version of the Release Notes.   
**Step 7** |  For each software bundle that you want to download, do the following: 

  1. Click the link for the latest release 4.0 software bundle.  The release number is followed by a number and a letter in parentheses. The number identifies the maintenance release level, and the letter differentiates between patches of that maintenance release. For more information about what is in each maintenance release and patch, see the latest version of the Release Notes. 
  2. Click one of the following buttons and follow the instructions provided: 
  * Download Now—Allows you to download the software bundle immediately. 
  * Add to Cart—Adds the software bundle to your cart to be downloaded at a later time. 
  3. Follow the prompts to complete your download of the software bundle(s). 

  
**Step 8** |  Read the Release Notes before upgrading your Cisco UCS domain.   
  
* * *

#### What to do next

Download the software bundles to the fabric interconnect. 

### Downloading Firmware Images to the Fabric Interconnect from a Remote Location

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

In a cluster setup, the image file for the firmware bundle is downloaded to both fabric interconnects, regardless of which fabric interconnect is used to initiate the download. Cisco UCS Manager maintains all firmware packages and images in both fabric interconnects in sync. If one fabric interconnect is down, the download finishes successfully. The images are synced to the other fabric interconnect when it comes back online. 

* * *  
  
---|---  
  
#### Before you begin

Obtain the required firmware bundles from Cisco. 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope firmware |  Enters firmware mode.   
**Step 2** |  UCS-A /firmware #  download image ` ` URL |  Downloads the firmware bundle. Using the download path provided by Cisco, specify the URL with one of the following syntax: 

  * ftp:// server-ip-addr / path
  * scp:// username@server-ip-addr / path
  * sftp:// username@server-ip-addr / path
  * tftp:// server-ip-addr : port-num / path |  **Note** |  TFTP has a file size limitation of 32 MB. Because firmware bundles can be much larger than that, we recommend that you do not select TFTP for firmware downloads.   
---|---  
  * usbA:/ path

  * usbB:/ path


**Note** |  USB A and USB B are applicable only for Cisco UCS 6324 (UCS Mini) and Cisco UCS 6300 Series fabric interconnects.  For Cisco UCS 6300 Series fabric interconnects, only the first of the two ports is detected.   
---|---  
**Note** |  If you use a hostname rather than an IP address, configure a DNS server in Cisco UCS Manager.   
---|---  
**Step 3** |  Enter the password for the remote server.  |  The password for the remote server username. This field does not apply if the protocol is tftp.   
**Step 4** |  UCS-A /firmware #  show download-task |  Displays the status for your download task. When your image is completely downloaded, the task state changes from Downloading to Downloaded. The CLI does not automatically refresh, so you may have to enter the  show download-task command multiple times until the task state displays Downloaded.   
**Step 5** |  Repeat this task until all of the firmware bundles have been downloaded to the fabric interconnect.  |   
  
#### Example

The following example uses SCP to download the firmware package. 
    
    
    UCS-A# **scope firmware**
    UCS-A /firmware # **download image scp://user1@111.100.10.10/images/ucs-k9-bundle.4.0.1.988.bin**
    OR
    **download image usbB:/username/ucs-k9-bundle-b-series.4.0.1a.B.bin**
    UCS-A /firmware # **show download-task**
    UCS-A /firmware # 

#### What to do next

After the image file for the firmware bundles download completes, update the firmware on the endpoints. 

### Displaying the Firmware Package Download Status

After a firmware download operation has been started, you can check the download status to see if the package is still downloading or if it has completely downloaded. 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope firmware |  Enters firmware mode.   
**Step 2** |  UCS-A /firmware #  show download-task |  Displays the status for your download task. When your image is completely downloaded, the task state changes from Downloading to Downloaded. The CLI does not automatically refresh, so you may have to enter the  show download-task command multiple times until the task state displays Downloaded.   
  
#### Example

The following example displays the download status for the firmware package. The  show download-task command is entered multiple times until the download state indicates that the firmware package has been downloaded: 
    
    
    UCS-A# **scope firmware**
    UCS-A /firmware # **show download-task**
    
    Download task:
    File Name 																						       Protocol   Server            Userid      State
    --------- 																							      --------   ---------------   ---------			-----
    ucs-6400-k9-bundle-infra.4.0.1a.A.bin  Scp        100.100.100.10    user1       Downloading
    
    UCS-A /firmware # **show download-task**
    
    Download task:
    File Name 																						       Protocol   Server            Userid      State
    --------- 																							      --------   ---------------   ---------			-----
    ucs-6400-k9-bundle-infra.4.0.1a.A.bin  Scp        100.100.100.10    user1       Downloading
    
    UCS-A /firmware # **show download-task**
    
    Download task:
    File Name 																						       Protocol   Server            Userid      State
    --------- 																							      --------   ---------------   ---------			-----
    ucs-6400-k9-bundle-infra.4.0.1a.A.bin  Scp        100.100.100.10    user1       Downloaded
    

### Canceling an Image Download

You can cancel the download task for an image only while it is in progress. After the image has downloaded, deleting the download task does not delete the image that was downloaded. You cannot cancel the FSM related to the image download task. 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope firmware |  Enters firmware mode.   
**Step 2** |  UCS-A /firmware #  delete download-task ` ` image_filename |  Deletes the specified image file.   
**Step 3** |  UCS-A /firmware #  commit-buffer |  Commits the transaction to the system configuration.   
  
#### Example

The following example cancels an image download: 
    
    
    UCS-A# **scope firmware**
    UCS-A /firmware # **delete download-task ucs-k9-bundle-b-series.4.0.1a.B.bin**
    UCS-A /firmware* # **commit-buffer**
    UCS-A /firmware* 

### Displaying All Available Software Images on the Fabric Interconnect

This procedure is optional and displays the available software images on the fabric interconnect for all endpoints. You can also use the  show image command in each endpoint mode to display the available software images for that endpoint. 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope firmware |  Enters firmware mode.   
**Step 2** |  UCS-A /firmware #  show image |  Displays all software images downloaded onto the fabric interconnect.  |  **Note** |  You must provide the software version number when directly updating an endpoint. If you intend to directly update firmware at an endpoint, note its version number in the right column.   
---|---  
  
#### Example

The following example displays all available software images on the fabric interconnect: 
    
    
    UCS-A# **scope firmware**
    UCS-A /firmware # **show image**
    
    Name                                          Type                 Version
    --------------------------------------------- -------------------- -------
    ucs-2200.3.2.2cS2.gbin                        Chassis Adaptor      3.2(2cS2)
    ucs-2200.4.0.0.46.gbin                        Chassis Adaptor      4.0(0.46)
    ucs-3260.3.0.4d.gbin                          Chassis Management Controller
                                                                       3.0(4d)
    ucs-3260.4.0.0.149.gbin                       Chassis Management Controller
                                                                       4.0(0.149)
    ucs-3260.4.0.0.155.gbin                       Chassis Management Controller
                                                                       4.0(0.155)
    ucs-6100-k9-kickstart.5.0.3.N2.3.22cS2.gbin   Fabric Interconnect Kernel
                                                                       5.0(3)N2(3.22cS2)
    ucs-6100-k9-kickstart.5.0.3.N2.4.00.46.gbin   Fabric Interconnect Kernel
                                                                       5.0(3)N2(4.00.46)
    ucs-6100-k9-system.5.0.3.N2.3.22cS2.gbin      Fabric Interconnect System
                                                                       5.0(3)N2(3.22cS2)
    ucs-6100-k9-system.5.0.3.N2.4.00.46.gbin      Fabric Interconnect System
                                                                       5.0(3)N2(4.00.46)
    ucs-adaptor-pcie-ucsc-pcie-x710ta4.800031CA-1.812.1.gbin
                                                  Adapter              800031CA-1.812.1
    ucs-adaptor-pcie-ucsc-pcie-xxx710da2.8000364C-1.812.1.gbin
                                                  Adapter              8000364C-1.812.1
    ucs-bmc-brdprog-S3260M5.2.0.gbin              Board Controller     2.0
    
    
    ...
     
    
    

### Displaying All Available Packages on the Fabric Interconnect

This procedure is optional and displays the available software packages on the fabric interconnect for all endpoints.. You can also use the  show package command in each endpoint mode to display the available software images for that endpoint. 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope firmware |  Enters firmware mode.   
**Step 2** |  UCS-A /firmware #  show package |  Displays all software packages downloaded onto the fabric interconnect.  |  **Note** |  You must provide the software version number when directly updating an endpoint. If you intend to directly update firmware at an endpoint, note its version number in the right column.   
---|---  
  
#### Example

The following example displays all available software packages on the fabric interconnect: 
    
    
    UCS-A# **scope firmware**
    UCS-A /firmware # **show package**
    Name                                          Version
    --------------------------------------------- -------
    ucs-c125-bios.C125.4.0.0.15.0504180159.gbin
    ucs-c125-bios.C125.4.0.0.17.0518180446.gbin
    ucs-c125-k9-cimc.4.0.0.130.gbin
    ucs-c125-k9-cimc.4.0.0.149.gbin
    ucs-k9-bundle-c-series.3.1.3h.C.gbin          3.1(3h)C
    ucs-k9-bundle-c-series.4.0.0.112.C.gbin       4.0(0.112)C
    ucs-k9-bundle-c-series.4.0.0.115.C.gbin       4.0(0.115)C
    ucs-k9-bundle-infra.3.2.2eS9.A.gbin           3.2(2eS9)A
    ucs-k9-bundle-infra.4.0.0.57.A.gbin           4.0(0.57)A
    ucs-manager-k9.4.0.0.8769.gbin
    ucs-manager-k9.4.0.0.8777.gbin
    ucs-manager-k9.4.0.0.8911.gbin
    
    

### Determining the Contents of a Firmware Package

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope firmware |  Enters firmware mode.   
**Step 2** |  UCS-A /firmware #  show package ` ` package-name ` ` expand |  Displays the contents of the specified firmware package.   
  
#### Example

The following example displays the contents of a firmware package: 
    
    
    UCS-A# **scope firmware**
    UCS-A /firmware # **show package ucs-k9-bundle-infra.4.0.0.57.A.gbin expand**
    Package ucs-k9-bundle-infra.4.0.0.57.A.gbin:
        Images:
            ucs-2200.4.0.0.46.gbin
            ucs-6100-k9-kickstart.5.0.3.N2.4.00.46.gbin
            ucs-6100-k9-system.5.0.3.N2.4.00.46.gbin
            ucs-manager-k9.4.0.0.56b.gbin
    
    

### Checking the Available Space on a Fabric Interconnect

If an image download fails, check whether the bootflash on the fabric interconnect or fabric interconnects in the Cisco UCS has sufficient available space. 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope fabric-interconnect ` `{a | b}  |  Enters fabric interconnect mode for the specified fabric.   
**Step 2** |  UCS-A /fabric-interconnect #  show storage ` `[detail | expand}  |  Displays the available space for the specified fabric.  |  **Note** |  When you download a firmware image bundle, a fabric interconnect needs at least twice as much available space as the size of the firmware image bundle. If the bootflash does not have sufficient space, delete the obsolete firmware, core files, and other unneeded objects from the fabric interconnect.   
---|---  
  
#### Example

The following example displays the available space for a fabric interconnect: 
    
    
    UCS-A# **scope fabric-interconnect a**
    UCS-A /fabric-interconnect # **show storage**
    Storage on local flash drive of fabric interconnect:
        Partition        Size (MBytes)    Used Percentage
        ---------------- ---------------- ---------------
        bootflash        16342            81
        opt              3873             3
        spare            5759             2
        usbdrive         Nothing          Empty
        var_sysmgr       2000             24
        var_tmp          600              2
        volatile         240              Empty
        workspace        3848             6
    UCS-A /fabric-interconnect # 


---

## Page 8: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Firmware-Mgmt/4-3/b_UCSM_CLI_Firmware_Management_Guide_4-3/b_UCSM_CLI_Firmware_Management_Guide_chapter_0101.html

## Recovering Fabric Interconnect During Upgrade 

If one or both fabric interconnects fail during failover or firmware upgrade, you can recover them by using one of the following approaches: 

  * Recover a fabric interconnect when you do not have a working image on the fabric interconnect 

  * Recover a fabric interconnect when you have a working image on the fabric interconnect 

  * Recover an unresponsive fabric interconnect during upgrade or failover 

  * Recover fabric interconnects from a failed FSM during upgrade with Auto Install


### Recovering Fabric Interconnects When You Do Not Have Working Images on the Fabric Interconnect or the Bootflash

You can perform these steps when both or any fabric interconnect goes down during firmware upgrade, gets rebooted, and is stuck at the loader prompt, and you do not have working images on the fabric interconnect. 

#### Procedure

* * *

**Step 1** |  Reboot the switch, and in the console, press Ctrl+L as it boots to get the loader prompt.  |  **Note** |  You may need to press the selected key combination multiple times before your screen displays the loader prompt.   
---|---  
  
#### Example:
    
    
    loader>
    
      
  
**Step 2** |  Configure the interface to receive the kickstart image through TFTP. 

  1. Enter the local IP address and subnet mask for the system at the loader> prompt, and press Enter. 

#### Example:
         
         loader> **set ip 10.104.105.136 255.255.255.0**
         
         

  2. Specify the IP address of the default gateway. 

#### Example:
         
         loader> **set gw 10.104.105.1**
         
         

  3. Boot the kickstart image file from the required server. 

#### Example:
         
         loader> **boot tftp://10.104.105.22/tftpboot/Images.3.0.2/ucs-6300-k9-kickstart.5.0.2.N1.3.02d56.bin**
         switch(boot)#
         
         


|  **Note** |  You do not need to do this step if you already have a kickstart image in the bootflash.   
---|---  
**Step 3** |  Enter the init system command at the switch(boot)# prompt.  This will reformat the fabric interconnect. 

#### Example:
    
    
    switch(boot)# **init system**
    
      
  
**Step 4** |  Configure the management interface. 

  1. Change to configuration mode and configure the IP address of the mgmt0 interface . 

#### Example:
         
         switch(boot)# **config t**
         switch(boot)(config)# **interface mgmt0**
         
         

  2. Enter the ip address command to configure the local IP address and the subnet mask for the system. 

#### Example:
         
         switch(boot)(config-if)# **ip address 10.104.105.136 255.255.255.0**
         
         

  3. Enter the no shutdown command to enable the mgmt0 interface on the system. 

#### Example:
         
         switch(boot)(config-if)# **no shutdown**
         
         

  4. Enter the ip default-gateway command to configure the IP address of the default gateway. 

#### Example:
         
         switch(boot)(config-if)# **exit**
         switch(boot)(config)# **ip default-gateway 10.104.105.1**
         
         

  5. Enter exit to exit to EXEC mode. 

#### Example:
         
         switch(boot)(config)# **exit**
         
         


  
**Step 5** |  Copy the kickstart, system, and Cisco UCS Manager management images from the TFTP server to the bootflash. 

#### Example:
    
    
    switch(boot)# **copy scp:// <username>@10.104.105.22/tftpboot/Images.3.0.2/ucs-6300-k9-kickstart.5.0.2.N1.3.02d56.bin bootflash://**
    switch(boot)# **copy scp:// <username>@10.104.105.22/tftpboot/Images.3.0.2/ucs-6300-k9-system.5.0.2.N1.3.02d56.bin bootflash://**
    switch(boot)# **copy scp:// <username>@10.104.105.22/tftpboot/Images.3.0.2/ucs-manager-k9.3.0.2d56.bin bootflash:// **
      
  
**Step 6** |  Create separate directories for installables and installables/switch in the bootflash. 

#### Example:
    
    
    switch(boot)# **mkdir bootflash:installables**
    switch(boot)# **mkdir bootflash:installables/switch**
    
      
  
**Step 7** |  Copy the kickstart, system, and Cisco UCS Manager images to the installables/switch directory. 

#### Example:
    
    
    switch(boot)# **copy ucs-6300-k9-kickstart.5.0.2.N1.3.02d56.bin bootflash:installables/switch/**
    switch(boot)# **copy ucs-6300-k9-system.5.0.2.N1.3.02d56.bin bootflash:installables/switch/**
    switch(boot)# **copy ucs-manager-k9.3.02d56.bin bootflash:installables/switch/**
    
      
  
**Step 8** |  Ensure that the management image is linked to nuova-sim-mgmt-nsg.0.1.0.001.bin.  nuova-sim-mgmt-nsg.0.1.0.001.bin is the name that the reserved system image uses, and it makes the management image Cisco UCS Manager-compliant. 

#### Example:
    
    
    switch(boot)# **copy bootflash:installables/switch/ucs-manager-k9.3.02d56.bin nuova-sim-mgmt-nsg.0.1.0.001.bin**
    
      
  
**Step 9** |  Reload the switch. 

#### Example:
    
    
    switch(boot)# **reload**
    This command will reboot this supervisor module. (y/n) ? **y**
    
      
  
**Step 10** |  Boot from the kickstart image. 

#### Example:
    
    
    loader> **dir**
    nuova-sim-mgmt-nsg.0.1.0.001.bin
    ucs-6300-k9-kickstart.5.0.2.N1.3.02d56.bin
    ucs-6300-k9-system.5.0.2.N1.3.02d56.bin
    ucs-manager-k9.3.02d56.bin
    loader> **boot ucs-6300-k9-kickstart.5.0.2.N1.3.02d56.bin**
    switch(boot)#
    
      
  
**Step 11** |  Load the system image.  The Basic System Configuration Dialog wizard appears after the system image is completely loaded. Use this wizard to configure the fabric interconnect. 

#### Example:
    
    
    switch(boot)# **load ucs-6300-k9-system.5.0.2.N1.3.02d56.bin**
    Uncompressing system image: bootflash:/ucs-6300-k9-system.5.0.2.N1.3.02d56.bin
    
    ...
    
    ---- Basic System Configuration Dialog ----
    
      This setup utility will guide you through the basic configuration of
      the system. Only minimal configuration including IP connectivity to
      the Fabric interconnect and its clustering mode is performed through these steps.
    
    ...
    
    Apply and save the configuration (select 'no' if you want to re-enter)? (yes/no): **yes**
    Applying configuration. Please wait.
    
    Configuration file - Ok
    
      
  
**Step 12** |  Log in to Cisco UCS Manager and download the firmware. 

#### Example:
    
    
    UCS-A# **scope firmware**
    UCS-A /firmware # **download image scp:// <username>@<server ip>//<downloaded image location>/<infra bundle name>**
    Password:
    UCS-A /firmware # **download image scp:// <username>@<server ip>//<downloaded image location>/<b-series bundle name>**
    Password:
    UCS-A /firmware # **download image scp:// <username>@<server ip>//<downloaded image location>/<c-series bundle name>**
    Password:
    UCS-A /firmware # **show download-task**
    Download task:
        File Name Protocol Server          Userid          State
        --------- -------- --------------- --------------- -----
        ucs-k9-bundle-b-series.3.0.2.B.bin
           	      Scp      10.104.105.22   abcdefgh        Downloading
        ucs-k9-bundle-c-series.3.0.2.C.bin
           	      Scp      10.104.105.22   abcdefgh        Downloading
        ucs-k9-bundle-infra.3.0.2.A.bin
           	      Scp      10.104.105.22   abcdefgh        Downloading
    UCS-A /firmware # 
      
  
**Step 13** |  After the firmware download is complete, activate the fabric interconnect firmware and Cisco UCS Manager firmware.  This step updates Cisco UCS Manager and the fabric interconnects to the version you want, and then reboots them. 

#### Example:
    
    
    UCS-A# **scope fabric-interconnect a**
    UCS-A /fabric-interconnect* # **activate firmware kernel-version 5.0(2)N1(3.02d56) ignorecompcheck**
    Warning: When committed this command will reset the end-point
    UCS-A /fabric-interconnect* # **activate firmware system-version 5.0(2)N1(3.02d56) ignorecompcheck**
    Warning: When committed this command will reset the end-point
    UCS-A /fabric-interconnect* # **commit-buffer**
    UCS-A /fabric-interconnect # **exit**
    
    UCS-A# **scope system**
    UCS-A /system # **show image**
    
    Name                                          Type                 Version
    --------------------------------------------- -------------------- -------
    ucs-manager-k9.3.02d56.bin                    System               3.0(2d)
    UCS-A /system # **activate firmware 3.0(2d) ignorecompcheck**
    The version specified is the same as the running version
    UCS-A /system # **activate firmware 3.0(2d) ignorecompcheck**
    The version specified is the same as the running version
    UCS-A /system # 
    
      
  
* * *

### Recovering Fabric Interconnect During Upgrade When You have Working Images on the Bootflash 

You can perform these steps when both or any fabric interconnect goes down during firmware upgrade, gets rebooted, and is stuck at the loader prompt. 

#### Before you begin

You must have working images on the bootflash to perform these steps. 

#### Procedure

* * *

**Step 1** |  Reboot the switch, and in the console, press Ctrl+L as it boots to get the loader prompt.  |  **Note** |  You may need to press the selected key combination multiple times before your screen displays the loader prompt.   
---|---  
  
#### Example:
    
    
    loader>
    
      
  
**Step 2** |  Run the dir command.  The list of available kernel, system, and Cisco UCS Manager images in the bootflash appears. 

#### Example:
    
    
    loader> **dir**
    nuova-sim-mgmt-nsg.0.1.0.001.bin
    ucs-6400-k9-kickstart.5.0.2.N1.3.02d56.bin
    ucs-6400-k9-system.5.0.2.N1.3.02d56.bin
    ucs-manager-k9.3.02d56.bin
    
      
  
**Step 3** |  Boot the kernel firmware version from the bootflash.  |  **Note** |  Any kernel image available here will be a working image from which you can boot.   
---|---  
  
#### Example:
    
    
    loader> **boot ucs-6400-k9-kickstart.5.0.2.N1.3.02d56.bin**
    
      
  
**Step 4** |  Ensure that the management image is linked to nuova-sim-mgmt-nsg.0.1.0.001.bin.  nuova-sim-mgmt-nsg.0.1.0.001.bin is the name that the reserved system image uses, and it makes the management image Cisco UCS Manager-compliant. 

#### Example:
    
    
    switch(boot)# **copy ucs-manager-k9.1.4.1k.bin nuova-sim-mgmt-nsg.0.1.0.001.bin**
    
      
  
**Step 5** |  Load the system image. 

#### Example:
    
    
    switch(boot)# **load ucs-6400-k9-system.5.0.2.N1.3.02d56.bin**
    
      
  
**Step 6** |  Log in to Cisco UCS Manager and update your fabric interconnect and Cisco UCS Manager software to the version that you want.   
  
* * *

### Recovering Unresponsive Fabric Interconnects During Upgrade or Failover 

During upgrade or failover, avoid performing the following tasks because they introduce additional risk: 

  * Pmon stop/start 

  * FI reboots – power cycle or CLI 

  * HA failover 


#### Procedure

* * *

**Step 1** |  If the httpd_cimc.sh process is lost, as documented in CSCup70756, you lose access to the KVM. Continue with the failover or contact Cisco Technical Assistance.   
---|---  
**Step 2** |  If you lose access to the KVM on the primary side, continue with the failover to resolve the issue.   
**Step 3** |  If KVM is needed or is down on the subordinate side, start only that service using the debug plugin. Contact TAC to run the debug image.   
**Step 4** |  If the /dev/null issue is encountered, as documented in CSCuo50049, fix the rights to 666 with the debug-plugin at both steps if required. Contact Cisco Technical Assistance to run debug commands.   
**Step 5** |  If both CSCup70756 and CSCuo50049 are encountered, it can cause VIP loss. If the VIP is lost, do the following: 

  1. Access the primary physical address through the GUI and use the GUI to verify all IO Module backplane ports recovered. 
  2. If the GUI is down, verify IO Module backplane ports with the NXOS show fex detail command. 
  3. Perform the workaround and verify that the cluster state is UP on both fabric interconnects. 
  4. If the cluster state is UP on both fabric interconnects, continue the upgrade by reacknowledging the primary fabric interconnect reboot using the SSH CLI syntax: 
         
         UCS-A# **scope firmware**
         UCS-A /firmware # **scope auto-install**
         UCS-A /firmware/auto-install # **acknowledge primary fabric-interconnect reboot**
         UCS-A /firmware/auto-install* # **commit-buffer**
         UCS-A /firmware/auto-install #
         
         


  
  
* * *

### Recovering Fabric Interconnects From a Failed FSM During Upgrade With Auto Install

You can perform these steps when all the following occur: 

  * You are upgrading or downgrading firmware using Auto Install between Cisco UCS Manager Release 3.1(2) and Release 3.1(3) while a service pack is installed on the fabric interconnects. 

  * Both or any fabric interconnect goes down because of an FSM failure or multiple retries in the DeployPollActivate stage of the FSM 


#### Procedure

* * *

**Step 1** |  When the FSM fails, or when multiple retries are observed in the DeployPollActivate stage of the FSM on the subordinate fabric interconnect, do the following: 

  1. Clear the startup version of the default infrastructure pack and the service pack. 

#### Example:
         
         UCS-A# scope org
         UCS-A /org # scope fw-infra-pack default
         UCS-A /org/fw-infra-pack # set infra-bundle-version ""
         UCS-A /org/fw-infra-pack* # commit-buffer

  2. Remove the service pack from the subordinate fabric interconnect. 

#### Example:
         
         UCS-A# scope fabric-interconnect b
         UCS-A# /fabric-interconnect # remove service-pack security
         UCS-A# /fabric-interconnect* # commit-buffer


  
---|---  
**Step 2** |  Upgrade the infrastructure firmware using the force option through Auto Install. 

#### Example:
    
    
    UCS-A# scope firmware
    UCS-A /firmware # scope auto-install
    UCS-A /firmware/auto-install # install infra infra-vers 3.1(3a)A force
    This operation upgrades firmware on UCS Infrastructure Components
    (UCS manager, Fabric Interconnects and IOMs).
    Here is the checklist of things that are recommended before starting Auto-Install
    (1) Review current critical/major faults
    (2) Initiate a configuration backup
    (3) Check if Management Interface Monitoring Policy is enabled
    (4) Check if there is a pending Fabric Interconnect Reboot activitiy
    (5) Ensure NTP is configured
    (6) Check if any hardware (fabric interconnects, io-modules, servers or adapters) is
    unsupported in the target release
    Do you want to proceed? (yes/no): yes
    Triggering Install-Infra with:
    Infrastructure Pack Version: 3.1(3a)A  
  
**Step 3** |  Acknowledge the reboot of the primary fabric interconnect. 

#### Example:
    
    
    UCS-A /firmware/auto-install # acknowledge primary fabric-interconnect reboot
    UCS-A /firmware/auto-install* # commit-buffer
    UCS-A /firmware/auto-install #  
  
**Step 4** |  When the FSM fails, or when multiple retries are observed in the DeployPollActivate stage of the FSM on the current subordinate fabric interconnect, do the following: 

  1. Clear the startup version of the default infrastructure pack and the service pack. 

#### Example:
         
         UCS-A# scope org
         UCS-A /org # scope fw-infra-pack default
         UCS-A /org/fw-infra-pack # set infra-bundle-version ""
         UCS-A /org/fw-infra-pack* # commit-buffer

  2. Remove the service pack from the current subordinate fabric interconnect. 

#### Example:
         
         UCS-A# scope fabric-interconnect a
         UCS-A# /fabric-interconnect # remove service-pack security
         UCS-A# /fabric-interconnect* # commit-buffer


  
  
* * *

Both fabric interconnects will now reflect Release 3.1(3) firmware and the default service pack for Running and Startup versions. 


---

