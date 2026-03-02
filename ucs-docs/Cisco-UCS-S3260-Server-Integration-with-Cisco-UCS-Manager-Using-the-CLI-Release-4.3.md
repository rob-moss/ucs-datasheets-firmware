# Documentation: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Dense-Storage-Server-Integ-Mgmt/4-2/b_CLI_UCSM_3260_Integration_Guide_4_3.html

*Fetched on: 2026-03-02 15:11:59*

---

## Page 1: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Dense-Storage-Server-Integ-Mgmt/4-2/b_CLI_UCSM_3260_Integration_Guide_4_3.html

![Clear Contents of Search](/etc/designs/cdc/fw/i/ic_clear_gray.png)


---

## Page 2: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Dense-Storage-Server-Integ-Mgmt/4-2/b_CLI_UCSM_3260_Integration_Guide_4_3/b_CLI_UCSM_3260_Integration_Guide_4_1_preface_00.html

## Audience

This guide is intended primarily for data center administrators with responsibilities and expertise in one or more of the following: 

  * Server administration 

  * Storage administration 

  * Network administration 

  * Network security 


---

## Page 3: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Dense-Storage-Server-Integ-Mgmt/4-2/b_CLI_UCSM_3260_Integration_Guide_4_3/b_CLI_UCSM_3260_Integration_Guide_4_1_chapter_01.html

## New and Changed Information

### New and Changed Information in Cisco UCS Manager, Release 4.3 

This section provides information on new feature and changed behavior in Cisco UCS Manager, Release 4.3. 

Table 1. New Features and Changed Behavior in **Cisco UCS Manager** , Release 4.3(2c) Feature |  Description |  Where Documented  
---|---|---  
Support Cisco UCS X-Series Server |  Cisco UCS Manager supports Cisco UCS X410c M7 Compute Node.  Cisco UCS X-Series servers support Intelligent Fabric Modules (IFM), which function similarly to the Input/Output Module (IOM) in Cisco UCS B-Series servers.  |  —  
  
This section provides information on new feature and changed behavior in Cisco UCS Manager, Release 4.3(2b). 

Table 2. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(2b) Feature |  Description |  Where Documented  
---|---|---  
Deprecated support for Cisco UCS S3260 M4 server. |  Cisco UCS Manager support for Cisco UCS S3260 M4 server is deprecated. |  -  
Deprecated support for Cisco UCS 6200 series Fabric Interconnect. |  Cisco UCS Manager support for Cisco UCS 6200 Series Fabric Interconnect is deprecated. |  -


---

## Page 4: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Dense-Storage-Server-Integ-Mgmt/4-2/b_CLI_UCSM_3260_Integration_Guide_4_3/b_CLI_UCSM_3260_Integration_Guide_4_1_chapter_010.html

## About the Cisco UCS S3260 System   
  
The Cisco UCS S3260 is a dense storage rack server with dual server nodes, optimized for large data sets used in environments such as Big data, cloud, object storage, and content delivery. It belongs to the Cisco UCS S-Series rack-mount servers product family. 

Beginning with Cisco UCS Manager Release 3.1(3), Cisco UCS C3260/C3X60 is renamed to Cisco UCS S3260. You may still see certain components in the system labeled as C3260/C3X60. For this release, the terms S3260 and C3260/C3X60 are used interchangeably. Both, S3260 and C3260/C3X60, refer to the same hardware component. 

Cisco UCS Manager Release 3.2(3) introduces Cisco UCS S3260 M5 server. Cisco UCS S3260 M5 server integrates with Cisco UCS Manager the same way Cisco UCS S3260 does. The information and procedures in this document can be used for Cisco UCS S3260 M5 servers. 

The Cisco UCS S3260 system is designed to operate in a  non-cluster environment and as part of the Cisco Unified Computing System with Cisco UCS Manager integration. It assumes almost the same characteristics of its predecessor, Cisco UCS C3160, but with the following additional features: 

  * System IO Controllers (SIOC) with Cisco VIC 1300 and 1400 Series Embedded Chip supporting 10/25/40/100G speeds.

  * Support of up to two server modules 

  * Capability to operate in a  non-cluster setup and with Cisco UCS Manager 

  * Individual hard disk drives (HDD) can be assigned to either server in the dedicated or shared mode 


In addition, one of the server slots in the Cisco UCS S3260 system can be utilized by a storage expansion module for an additional four 3.5" drives. The server modules can also accommodate two solid state drives (SSD) for internal storage dedicated to that module. The chassis supports Serial Attached SCSI (SAS) expanders that can be configured to assign the 3.5" drives to individual server modules. 

Beginning with release 3.1(3), Cisco UCS S3260 system supports the following: 

  * Server SIOC Connectivity functionality

  * Second RAID controller in the optional I/O expander module

  * Dual HBA Controller

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

If a Cisco UCS S3260 system has Dual HBA Controller then you cannot downgrade Cisco UCS Manager to any release earlier than 3.1(3). 

* * *  
  
---|---  


In a Cisco UCS S3260 system, both servers should have either dual RAID controllers or dual HBA controllers. Mixing the controller types is not supported. 

Cisco UCS S3260 system supports Server SIOC Connectivity functionality. Using this functionality, you can configure the data path through both the primary and auxiliary SIOCs when the chassis has single server and dual SIOCs set up. For more details, see Server SIOC Connectivity Functionality. 

Cisco UCS S3260 system supports Second RAID controller in the optional I/O expander module that attaches to the top of the server node. You cannot downgrade Cisco UCS Manager, BMC, CMC, and BIOS to any release earlier than 3.1(3) depending on the number of disk zoned to the controllers : 

Controller Configuration |  Is Downgrade Possible?  
---|---  
Two controllers in the server (one in optional I/O expander) or one controller in the server (in optional I/O expander) and at least one disk is zoned to the controller in the optional I/O expander.  |  No  
Two controllers in the server (one in optional I/O expander) or one controller in the server (in optional I/O expander) and at least one disk is pre-provisioned to controller in the optional I/O expander.  |  No  
Two controllers in the server (one in optional I/O expander) or one controller in the server (in any slot) and disk are not zoned or pre-provisioned to the controller in optional I/O expander.  |  Yes  
  
### License Requirement 

Beginning with release 4.2(3b), for Cisco UCS 6536 Fabric Interconnect (UCS-FI-6536), all ports are enabled using a term-based subscription license (Supported license term: 36-60 months). 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Licensing for FI 6536 is not a port-based license like in previous FI generations. 

* * *  
  
---|---  
  
ETH_PORT_ACTIVATION_PKG (/6400 FI series), 40G_ETH_PORT_ACTIVATION_PKG (for 6400 and 6300 FI - 6332), 10G_PORT_ACTIVATION_PKG (for 6300 FI - 6332-16UP), licenses are used when S3260 system is connected to FI as appliance (appliance port) or Cisco UCS Manager managed node (server port). 

For more information on license requirement, refer Server License Management chapter in Cisco UCS Manager Server Management Guide. 


---

## Page 5: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Dense-Storage-Server-Integ-Mgmt/4-2/b_CLI_UCSM_3260_Integration_Guide_4_3/b_CLI_UCSM_3260_Integration_Guide_4_1_chapter_011.html

## Migration to UCSM Managed Cisco UCS S3260

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Direct migration of Cisco UCS C3160 to UCSM managed Cisco UCS S3260 is not supported. First migrate standalone Cisco UCS C3160 to standalone Cisco UCS S3260 and then to UCSM managed Cisco UCS S3260. 

* * *  
  
---|---  
  
### Migrating Standalone Cisco UCS C3160 to UCSM Managed Cisco UCS S3260

To migrate standalone Cisco UCS C3160 to UCSM Managed Cisco UCS S3260: 

  1. Standalone Cisco UCS C3160 to Standalone Cisco UCS Cisco UCS S3260

  2. Standalone Cisco UCS Cisco UCS S3260 to UCSM managed Cisco UCS S3260

  3. Configure Server Ports Using Cisco UCS Manager 


### Migrating Standalone Cisco UCS Cisco UCS S3260 to UCSM Managed Cisco UCS S3260

To migrate standalone Cisco UCS Cisco UCS S3260 to UCSM Managed Cisco UCS S3260: 

  1. Standalone Cisco UCS Cisco UCS S3260 to UCSM managed Cisco UCS S3260

  2. Configure Server Ports Using Cisco UCS Manager 


---

## Page 6: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Dense-Storage-Server-Integ-Mgmt/4-2/b_CLI_UCSM_3260_Integration_Guide_4_3/b_CLI_UCSM_3260_Integration_Guide_4_1_chapter_0100.html

## Chassis Discovery Policy 

The chassis discovery policy determines how the system reacts when you add a new Cisco UCS S3260 chassis or an existing standalone Cisco UCS S3260 chassis to a Cisco UCS system. [Cisco UCS S3260 System Architectural Overview](b_CLI_UCSM_3260_Integration_Guide_4_1_chapter_010.html#id_20266) describes the connectivity for a Cisco UCS S3260 system managed by Cisco UCS Manager. Cisco UCS Manager uses the settings in the chassis discovery policy to determine whether to group links from the system I/O controllers (SIOCs) to the fabric interconnects in fabric port channels. 

To add a previously standalone Cisco UCS S3260 chassis to a Cisco UCS system, you must first configure it to factory default. You can then connect both SIOCs on the chassis to both fabric interconnects. After you connect the SIOCs on the chassis to the fabric interconnects, and mark the ports as server ports, chassis discovery begins. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Chassis/IOM acknowledgement after chassis/FEX discovery policy changes is not applicable for S3260 chassis. 

* * *  
  
---|---  
  
### Server Discovery 

Cisco UCS Manager automatically discovers the Cisco UCS S3260 server nodes after the Cisco UCS S3260 chassis is discovered. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Server discovery fails if the SIOC corresponding to the server is not present. 

* * *  
  
---|---  
  
### Link Grouping

In release 4.0(1a), Link Group Preference is automatically set to Port Channel when using new SIOC with PCIe slots. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For the Cisco UCS 6400 Series Fabric Interconnect, and Cisco UCS 6536 Fabric Interconnect, the Link Group Preference is always set to Port Channel. 

* * *  
  
---|---  
  
When you connect a Cisco UCS S3260 chassis through a FEX to directly to a Cisco UCS 6300 Series fabric interconnect, or Cisco UCS 6400 Series Fabric Interconnect, and Cisco UCS 6536 Fabric Interconnect, Cisco UCS Manager ignores the Port Channel preference and the SIOCs operate in the non-port channel mode. 

Set the link grouping preference to None if the Cisco UCS S3260 chassis is connected to a fabric interconnect through a single 10G cable. 

After changing the Link Group Preference value in the Cisco UCS Manager GUI, Decommission and then Recommission the Cisco UCS S3260 chassis for the change to take effect. 

In the Cisco UCS domain, if there are other chassis operating in Port Channel mode, do the following: 

  1. Discover the chassis in the Cisco UCS system with the Link Group Preference set to Port Channel

  2. Change the link aggregation preference for the Cisco UCS S3260 chassis through Chassis Connectivity Policy 

  3. Decommission the chassis 

  4. Recommission the chassis 


### Configuring the Chassis/FEX Discovery Policy 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope org / |  Enters the root organization mode.  |  **Note** |  The chassis/FEX discovery policy can be accessed only from the root organization.   
---|---  
**Step 2** |  UCS-A /org #  scope chassis-disc-policy |  Enters organization chassis/FEX discovery policy mode.   
**Step 3** |  (Optional) UCS-A /org/chassis-disc-policy # set descr ` ` description | (Optional)  Provides a description for the chassis/FEX discovery policy.  |  **Note** |  If your description includes spaces, special characters, or punctuation, you must begin and end your description with quotation marks. The quotation marks will not appear in the description field of any  show command output.   
---|---  
**Step 4** |  UCS-A /org/chassis-disc-policy #  set link-aggregation-pref ` `{none | port-channel}  |  Specifies whether the links from the SIOCs or FEXes to the fabric interconnects are grouped into a port channel. Link aggregation can be one of the following: 

  * none—links from the SIOC or FEX are pinned to the fabric interconnect. 
  * port-channel—links from the SIOCs to the fabric interconnects are grouped into a port channel 

  
**Step 5** |  UCS-A /org/chassis-disc-policy #  commit-buffer |  Commits the transaction to the system configuration.   
  
#### Example

The following example scopes to the default chassis discovery policy, provides a description for the policy, sets the link grouping preference to port channel, specifies the server pool policy qualifications that will be used to qualify the chassis, and commits the transaction: 
    
    
    UCS-A# **scope org /**
    UCS-A /org # **scope chassis-disc-policy**
    UCS-A /org/chassis-disc-policy* # **set descr "This is an example chassis discovery policy."**
    UCS-A /org/chassis-disc-policy* # **set link-aggregation-pref port-channel**
    UCS-A /org/chassis-disc-policy* # **commit-buffer**
    UCS-A /org/chassis-disc-policy # 
    

#### What to do next

To customize fabric port channel connectivity for a specific chassis, configure the chassis connectivity policy. 


---

## Page 7: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Dense-Storage-Server-Integ-Mgmt/4-2/b_CLI_UCSM_3260_Integration_Guide_4_3/b_CLI_UCSM_3260_Integration_Guide_4_1_chapter_0101.html

## Chassis Profiles in Cisco UCS Manager

A chassis profile defines the storage, firmware, and maintenance characteristics of a chassis. You can create a chassis profile for the Cisco UCS S3260 chassis. When a chassis profile is associated to a chassis, Cisco UCS Manager automatically configures the chassis to match the configuration specified in the chassis profile. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

At any given time, each S3260 chassis can be associated with only one chassis profile. Similarly, each chassis profile can be associated with only one S3260 chassis at a time. 

* * *  
  
---|---  
  
A chassis profile includes the following information: 

  * Chassis definition—Defines the specific chassis to which the profile is assigned. 

  * Maintenance policy—Includes the maintenance policy to be applied to the profile. 

  * Firmware specifications—Defines the chassis firmware package that can be applied to a chassis through this profile. 

  * Disk zoning policy—Includes the zoning policy to be applied to the storage disks. 

  * Compute Connection policy — Defines the data path between the primary, auxiliary SIOC, and server. 


---

## Page 8: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Dense-Storage-Server-Integ-Mgmt/4-2/b_CLI_UCSM_3260_Integration_Guide_4_3/b_CLI_UCSM_3260_Integration_Guide_4_1_chapter_0110.html

## Storage Server Features and Components Overview 

### Storage Server Features 

The following table summarizes the Cisco UCS S3260 system features: 

Table 1. Cisco UCS S3260 System Features Feature  |  Description   
---|---  
Chassis  |  Four rack unit (4RU) chassis   
Processors  | 

  * Cisco UCS S3260 M5 server nodes: Two Intel Skylake 2S-EP processors inside each server node. 

  
Memory  |  Up to 16 DIMMs inside each server node.   
Multi-bit error protection  |  This system supports multi-bit error protection.   
Storage  |  The system has the following storage options: 

  * Up to 56 top-loading 3.5-inch drives 
  * Up to four 3.5-inch, rear-loading drives in the optional drive expander module 
  * Up to four 2.5-inch, rear-loading SAS solid state drives (SSDs) 
  * Two 7 mm NVMe drive inside the server node  |  **Note** |  This is applicable for S3260 M5 servers only.   
---|---  
  * Two 15 mm NVMe drive supported for IO Expander 


  
Disk Management  |  The system supports up to two storage controllers: 

  * One dedicated mezzanine-style socket for a Cisco storage controller card inside each server node 

  
RAID Backup  |  The supercap power module (SCPM) mounts to the RAID controller card.   
PCIe I/O  |  The optional I/O expander provides two 8x Gen 3 PCIe expansion slots. Release 3.2(3) and later supports the following for S3260 M5 servers:

  * Intel X550 dual-port 10GBase-T 
  * Qlogic QLE2692 dual-port 16G Fiber Channel HBA
  * N2XX-AIPCI01 Intel X520 Dual Port 10Gb SFP+ Adapter

  
Network and Management I/O  |  The system can have one or two system I/O controllers (SIOCs). These provide rear-panel management and data connectivity. 

  * Two SFP+ 40 Gb ports each SIOC. 
  * One 10/100/1000 Ethernet dedicated management port on each SIOC. 

The server nodes each have one rear-panel KVM connector that can be used with a KVM cable, which provides two USB, one VGA DB-15, and one serial DB-9 connector.   
Power  |  Two or four power supplies, 1050 W each (hot-swappable and redundant as 2+2).   
Cooling  |  Four internal fan modules that pull front-to-rear cooling, hot-swappable. Each fan module contains two fans.  In addition, there is one fan in each power supply.   
  
### Front Panel Features 

The following image shows the front panel features for the Cisco UCS S3260 system: 

Figure 1. Front Panel Features   
![](/c/dam/en/us/td/i/300001-400000/350001-360000/353001-354000/353375.eps/_jcr_content/renditions/353375.jpg)  
1  |  Operations panel  |  6  |  Temperature status LED   
---|---|---|---  
2  |  System Power button/LED  |  7  |  Power supply status LED   
3  |  System unit identification button/LED  |  8  |  Network link activity LED   
4  |  System status LED  |  9  |  Pull-out asset tag (not visible under front bezel)   
5  |  Fan status LED  |  10  |  Internal-drive status LEDs   
  
### Rear Panel Features

The following image shows the rear panel features for the Cisco UCS S3260 system: 

Figure 2. Front Panel Features   
![](/c/dam/en/us/td/i/300001-400000/300001-310000/305001-306000/305363.jpg)  
Disk Slots  1  |  Server bay 1 

  * (Optional) I/O expander, as shown (with Cisco UCS S3260 M5 server node only) 
  * (Optional) server node 
  * (Optional) drive expansion module 

|  8  |  Not used at this time   
---|---|---|---  
2  |  Server bay 2 

  * (Optional) server node (Cisco UCS S3260 M5 shown) (Optional) drive expansion module 

|  9  |  Not used at this time   
3  |  System I/O controller (SIOC) 

  * SIOC 1 is required if you have a server node in server bay 1 
  * SIOC 2 is required if you have server node in server bay 2 

|  10  |  Solid state drive bays (up to four 2.5-inch SAS SSDs) 

  * SSDs in bays 1 and 2 require a server node in server bay 1 
  * SSDs in bays 3 and 4 require a server node in server bay 2 

  
4  |  Power supplies (four, redundant as 2+2)  |  11  |  |  **Note** |  This label identifies a Cisco UCS S3260 M5 server node.   
---|---  
5  |  40-Gb SFP+ ports (two on each SIOC)  |  12  |  KVM console connector (one each server node).  Used with a KVM cable that provides two USB, one VGA, and one serial connector   
6  |  Chassis Management Controller (CMS) Debug Firmware Utility port (one each SIOC)  |  13  |  Server node unit identification button/LED   
7  |  10/100/1000 dedicated management port, RJ-45 connector (one each SIOC)  |  14  |  Server node power button   
|  |  15  |  Server node reset button (resets chipset in the server node   
  
### Storage Server Components 

Server Nodes

The Cisco UCS S3260 system consists of one or two server nodes, each with two CPUs, DIMM memory of 128, 256, or 512 GB, and a RAID card up to 4 GB cache or a pass-through controller. The server nodes can be one of the following: 

  * Cisco UCS S3260 M5 Server Node—This node might include an optional I/O expander module that attaches to the top of the server node. 


Disk Slots 

The Cisco UCS S3260 chassis has 4 rows of 14 disk slots on the HDD motherboard and 4 additional disk slots on the HDD expansion tray. The following image shows the disk arrangement for the 56 top-accessible, hot swappable 3.5-inch 6 TB or 4 TB 7200 rpm NL-SAS HDD drives. A disk slot has two SAS ports and each is connected a SAS expander in the chassis. 

Figure 3. Cisco UCS S3260 Top View  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/305001-306000/305448.jpg)

The following image shows the Cisco UCS S3260 chassis with the 4 additional disk slots on the HDD expansion tray. 

Figure 4. Cisco UCS 3260 with the HDD expansion tray (Rear View)   
![](/c/dam/en/us/td/i/300001-400000/300001-310000/305001-306000/305447.jpg)  


If you have two server nodes with two SIOCs, you will have the following functionality: 

  1. The top server node works with the left SIOC (Server Slot1 with SIOC1). 

  2. The bottom server works with the right SIOC (Sever Slot 2 with SIOC2). 


If you have one server node with two SIOCs, you can enable Server SIOC Connectivity functionality. Beginning with release 3.1(3), Cisco UCS S3260 system supports Server SIOC Connectivity functionality. Using this functionality, you can configure the data path through both the primary and auxiliary SIOCs when the chassis has single server and dual SIOCs set up. 

SAS Expanders 

The Cisco UCS S3260 system has two SAS expanders that run in redundant mode and connect the disks at the chassis level to storage controllers on the servers. The SAS expanders provide two paths between a storage controller, and hence enable high availability. They provide the following functionality: 

  * Manage the pool of hard drives. 

  * Disk zone configuration of the hard drives to storage controllers on the servers. 


Beginning with release 3.2(3a), Cisco UCS Manager can enable single path access to disk by configuring single DiskPort per disk slot. This ensures that the server discovers only a single device and avoid a multi-path configuration. 

The following table describes how the ports in each SAS expander are connected to the disks based on the type of deployment. 

Port range  |  Connectivity   
---|---  
1-56  |  Top accessible disks   
57-60  |  Disks in the HDD expansion tray.   
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The number of SAS uplinks between storage controller and SAS expander can vary based on the type of controller equipped in the server. 

* * *  
  
---|---  
  
Storage Enclosures 

A Cisco UCS S3260 system has the following types of storage enclosures: 

Chassis Level Storage Enclosures 
    

  * HDD motherboard enclosure—The 56 dual port disk slots in the chassis comprise the HDD motherboard enclosure. 

  * HDD expansion tray—The 4 additional dual disk slots in the Cisco UCS S3260 system comprise the HDD expansion tray. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The HDD expansion tray is a field replaceable unit (FRU). The disks will remain unassigned upon insertion, and can be assigned to storage controllers. For detailed steps on how to perform disk zoning, see Disk Zoning Policies

* * *  
  
---|---  


Server level Storage Enclosures 
    

Server level storage enclosures are pre-assigned dedicated enclosures to the server. These can be one of the following: 

  * Rear Boot SSD enclosure—This enclosure contains two 2.5 inch disk slots on the rear panel of the Cisco UCS S3260 system. Each server has two dedicated disk slots. These disk slots support SATA SSDs. 

  * Server board NVMe enclosure—This enclosure contains one PCIe NVMe controller. 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

In the Cisco UCS S3260 system, even though disks can be physically present on the two types of enclosures described above, from the host OS all the disks are viewed as part of one SCSI enclosure. They are connected to SAS expanders that are configured to run as single SES enclosure. 

* * *  
  
---|---  
  
Storage Controllers 

Mezzanine Storage Controllers 
    

The following table lists the storage controller type, firmware type, modes, sharing and OOB support for the various storage controllers. 

Table 2.  Storage Controller Type  |  Firmware type  |  Modes  |  Sharing  |  OOB Support   
---|---|---|---|---  
UCSC-S3X60-R1GB  |  Mega RAID  |  HW RAID, JBOD  |  No  |  Yes   
UCSC-S3X60-HBA  |  Initiator Target  |  Pass through  |  Yes  |  Yes   
UCS-S3260-DHBA |  Initiator Target  |  Pass through  |  Yes  |  Yes   
UCS-S3260-DRAID |  Mega RAID  |  HW RAID, JBOD  |  No  |  Yes   
  
Other storage controllers 
    SW RAID Controller—The servers in the Cisco UCS S3260 system support two dedicated internal SSDs embedded into the PCIe riser that is connected to the SW RAID Controller. 
    

NVMe Controller—This controller is used by servers in the Cisco UCS S3260 system for inventory and firmware updates of NVMe disks. 

For more details about the storage controllers supported in the various server nodes, see the related service note: 

  * [Cisco UCS S3260 M5 Server Node For Cisco UCS S3260 Storage Server Service Note](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/s/hw/S3260M5/install/S3260M5.html)


---

## Page 9: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Dense-Storage-Server-Integ-Mgmt/4-2/b_CLI_UCSM_3260_Integration_Guide_4_3/b_CLI_UCSM_3260_Integration_Guide_4_1_chapter_0111.html

## Firmware Management for Cisco UCS S3260 Systems 

Cisco UCS uses firmware obtained from and certified by Cisco to support the endpoints in a Cisco UCS domain. Each endpoint is a component in the Cisco UCS domain that requires firmware to function. 

Cisco UCS Manager Firmware Management Guide, Release 3.2 provides detailed information about the complete firmware management process. Additionally, beginning with Cisco UCS Manager Release 3.1(2), you can upgrade the firmware of Cisco UCS S3260 chassis components by defining a chassis firmware policy and including it in the chassis profile associated with a Cisco UCS S3260 chassis. 

You can upgrade a Cisco UCS domain with a S3260 chassis and servers through Cisco UCS Manager in the following ways: 

  * Upgrade infrastructure components through Auto Install—You can upgrade the infrastructure components, such as the Cisco UCS Manager software and the fabric interconnects, in a single step by using Auto Install. Cisco UCS Manager Firmware Management Guide, Release 3.2 provides detailed information about the Auto Install process. 

  * Upgrade chassis through one of the following:

  * Upgrade chassis components through Auto Install—Beginning with Cisco UCS Manager Release 3.2(3), you can upgrade the firmware of Cisco UCS S3260 chassis components in a single step by using Auto Install. 

  * Upgrade chassis through chassis firmware packages in chassis profiles—This option enables you to upgrade all chassis endpoints in a single step. The chassis endpoints that you can upgrade through a chassis firmware package are: 

  * Chassis Adapter 

  * Chassis Management Controller 

  * Chassis Board Controller 

  * Local Disk 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

You can upgrade local disks in the chassis through a chassis firmware package. Upgrade the local disks in a server through a host firmware package. 

* * *  
  
---|---  
  * SAS Expander 

  * Upgrade servers through firmware packages in service profiles—This option enables you to upgrade all server endpoints in a single step, reducing the amount of disruption caused by a server reboot. You can combine this option with the deferred deployment of service profile updates to ensure that server reboots occur during scheduled maintenance windows. The server endpoints that you can upgrade through a host firmware package are: 

  * CIMC 

  * BIOS 

  * Board Controller 

  * Storage Controller 

  * Local Disk 

  * NVMe in SIOC

  * Third-party adapter in SIOC

Cisco UCS Manager Firmware Management Guide, Release 3.2 provides detailed information about upgrading server endpoints through host firmware packages. 


You can also directly upgrade the firmware at each infrastructure, chassis, and server endpoint. This option enables you to upgrade many infrastructure, chassis, and server endpoints directly, including the fabric interconnects, SAS expanders, CMCs, chassis adapters, storage controllers, and board controllers. However, direct upgrade is not available for all endpoints, including the storage controller, HBA firmware, HBA option ROM and local disk. 

This chapter explains the following newly introduced firmware management capabilities for the Cisco UCS S3260 system: 

  * Upgrading firmware through chassis firmware packages in chassis profiles 

  * Directly upgrading firmware on Cisco UCS S3260 chassis and server endpoints 


---

## Page 10: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Dense-Storage-Server-Integ-Mgmt/4-2/b_CLI_UCSM_3260_Integration_Guide_4_3/b_CLI_UCSM_3260_Integration_Guide_4_1_chapter_01000.html

## The Cisco UCS S3260 Chassis

Cisco UCS Manager Release 4.2(3) introduces support for the Cisco UCS S3260 chassis on Cisco UCS 6536 Fabric Interconnect. 

Cisco UCS Manager Release 4.1(1) introduces support for the Cisco UCS S3260 chassis on Cisco UCS 64108 Fabric Interconnect. 

Cisco UCS Manager Release 4.0(1) introduces support for the Cisco UCS S3260 chassis on Cisco UCS 6454 Fabric Interconnect. 

Cisco UCS Manager Release 3.1(2) introduces support for the Cisco UCS S3260 chassis on Cisco UCS 6300 Series fabric interconnect setups. 

The Cisco UCS S3260 chassis is a 4U chassis that is designed to operate in a standalone environment and also as part of the Cisco Unified Computing System. It has the following main components: 

  * Four 1050 Watt AC modular power supplies (2 + 2 shared and redundant mode of operation) 

  * Two System IO Controller (SIOC) slots 

  * Two storage server slots out of which one can be used for storage expansion 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The second server slot in the chassis can be utilized by an HDD expansion tray module for an additional four 3.5” drives. 

* * *  
  
---|---  
  * 56 3.5” drive bays with an optional 4 x 3.5” HDD expansion tray module instead of the second server 

  * Up to 360 TB storage capacity by using 6 TB HDDs 

  * Serial Attached SCSI (SAS) expanders that can be configured to assign the 3.5” drives to individual server modules 

  * The two servers in the chassis can be replaced by a single, dual-height server with an IO expander 


---

## Page 11: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Dense-Storage-Server-Integ-Mgmt/4-2/b_CLI_UCSM_3260_Integration_Guide_4_3/b_CLI_UCSM_3260_Integration_Guide_4_1_chapter_01001.html

## Cisco UCS S3260 Server Node Management 

You can manage and monitor all Cisco UCS S3260 server nodes in a Cisco UCS domain through Cisco UCS Manager. You can perform some server management tasks, such as changes to the power state, from the server and service profile. 

The remaining management tasks can only be performed on the server. 

If a server slot in a chassis is empty, Cisco UCS Manager provides information, errors, and faults for that slot. You can also re-acknowledge the slot to resolve server mismatch errors and rediscover the server in the slot. 


---

## Page 12: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Dense-Storage-Server-Integ-Mgmt/4-2/b_CLI_UCSM_3260_Integration_Guide_4_3/b_CLI_UCSM_3260_Integration_Guide_4_1_chapter_01010.html

## SIOC Management in Cisco UCS Manager

You can manage and monitor all System Input/Output Controllers (SIOC) in a Cisco UCS domain through Cisco UCS Manager. 

### SIOC Removal or Replacement 

You can remove or replace an SIOC from a chassis. Removal or replacement of an SIOC is a service-affecting operation, which requires you to power down the entire chassis. 

#### Guidelines for SIOC Removal 

  * To remove the active SIOC, or both SIOCs, shut down and remove power from the entire chassis. You must disconnect all power cords to completely remove power. 

  * Removal of SIOCs from a chassis results in the entire chassis being disconnected from Cisco UCS Manager. 


#### SIOC Removal 

Do the following to remove an SIOC from the system: 

  1. Shut down and remove power from the entire chassis. You must disconnect all power cords to completely remove power.

  2. Disconnect the cables connecting the SIOC to the system. 

  3. Remove the SIOC from the system. 


#### SIOC Replacement 

Do the following to remove an SIOC from the system and replace it with another SIOC: 

  1. Shut down and remove power from the entire chassis. You must disconnect all power cords to completely remove power.

  2. Disconnect the cables connecting the SIOC to the system. 

  3. Remove the SIOC from the system. 

  4. Connect the new SIOC to the system. 

  5. Connect the cables to the SIOC. 

  6. Connect power cords and then power on the system.

  7. Acknowledge the new SIOC. 

The server connected to the replaced SIOC is rediscovered. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

If the firmware of the replaced SIOC is not the same version as the peer SIOC, then it is recommended to update the firmware of the replaced SIOC by re-triggering chassis profile association. 

* * *  
  
---|---  


---

## Page 13: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Dense-Storage-Server-Integ-Mgmt/4-2/b_CLI_UCSM_3260_Integration_Guide_4_1_chapter_01010.html

## SIOC Management in Cisco UCS Manager

You can manage and monitor all System Input/Output Controllers (SIOC) in a Cisco UCS domain through Cisco UCS Manager. 

### SIOC Removal or Replacement 

You can remove or replace an SIOC from a chassis. Removal or replacement of an SIOC is a service-affecting operation, which requires you to power down the entire chassis. 

#### Guidelines for SIOC Removal 

  * To remove the active SIOC, or both SIOCs, shut down and remove power from the entire chassis. You must disconnect all power cords to completely remove power. 

  * Removal of SIOCs from a chassis results in the entire chassis being disconnected from Cisco UCS Manager. 


#### SIOC Removal 

Do the following to remove an SIOC from the system: 

  1. Shut down and remove power from the entire chassis. You must disconnect all power cords to completely remove power.

  2. Disconnect the cables connecting the SIOC to the system. 

  3. Remove the SIOC from the system. 


#### SIOC Replacement 

Do the following to remove an SIOC from the system and replace it with another SIOC: 

  1. Shut down and remove power from the entire chassis. You must disconnect all power cords to completely remove power.

  2. Disconnect the cables connecting the SIOC to the system. 

  3. Remove the SIOC from the system. 

  4. Connect the new SIOC to the system. 

  5. Connect the cables to the SIOC. 

  6. Connect power cords and then power on the system.

  7. Acknowledge the new SIOC. 

The server connected to the replaced SIOC is rediscovered. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

If the firmware of the replaced SIOC is not the same version as the peer SIOC, then it is recommended to update the firmware of the replaced SIOC by re-triggering chassis profile association. 

* * *  
  
---|---  


---

## Page 14: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Dense-Storage-Server-Integ-Mgmt/4-2/b_CLI_UCSM_3260_Integration_Guide_4_1_chapter_010.html

## About the Cisco UCS S3260 System 

The Cisco UCS S3260 is a dense storage rack server with dual server nodes, optimized for large data sets used in environments such as Big data, cloud, object storage, and content delivery. It belongs to the Cisco UCS S-Series rack-mount servers product family. 

Beginning with Cisco UCS Manager Release 3.1(3), Cisco UCS C3260/C3X60 is renamed to Cisco UCS S3260. You may still see certain components in the system labeled as C3260/C3X60. For this release, the terms S3260 and C3260/C3X60 are used interchangeably. Both, S3260 and C3260/C3X60, refer to the same hardware component. 

Cisco UCS Manager Release 3.2(3) introduces Cisco UCS S3260 M5 server. Cisco UCS S3260 M5 server integrates with Cisco UCS Manager the same way Cisco UCS S3260 does. The information and procedures in this document can be used for Cisco UCS S3260 M5 servers. 

The Cisco UCS S3260 system is designed to operate in a  non-cluster environment and as part of the Cisco Unified Computing System with Cisco UCS Manager integration. It assumes almost the same characteristics of its predecessor, Cisco UCS C3160, but with the following additional features: 

  * System IO Controllers (SIOC) with Cisco VIC 1300 and 1400 Series Embedded Chip supporting 10/25/40/100G speeds.

  * Support of up to two server modules 

  * Capability to operate in a  non-cluster setup and with Cisco UCS Manager 

  * Individual hard disk drives (HDD) can be assigned to either server in the dedicated or shared mode 


In addition, one of the server slots in the Cisco UCS S3260 system can be utilized by a storage expansion module for an additional four 3.5" drives. The server modules can also accommodate two solid state drives (SSD) for internal storage dedicated to that module. The chassis supports Serial Attached SCSI (SAS) expanders that can be configured to assign the 3.5" drives to individual server modules. 

Beginning with release 3.1(3), Cisco UCS S3260 system supports the following: 

  * Server SIOC Connectivity functionality

  * Second RAID controller in the optional I/O expander module

  * Dual HBA Controller

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

If a Cisco UCS S3260 system has Dual HBA Controller then you cannot downgrade Cisco UCS Manager to any release earlier than 3.1(3). 

* * *  
  
---|---  


In a Cisco UCS S3260 system, both servers should have either dual RAID controllers or dual HBA controllers. Mixing the controller types is not supported. 

Cisco UCS S3260 system supports Server SIOC Connectivity functionality. Using this functionality, you can configure the data path through both the primary and auxiliary SIOCs when the chassis has single server and dual SIOCs set up. For more details, see Server SIOC Connectivity Functionality. 

Cisco UCS S3260 system supports Second RAID controller in the optional I/O expander module that attaches to the top of the server node. You cannot downgrade Cisco UCS Manager, BMC, CMC, and BIOS to any release earlier than 3.1(3) depending on the number of disk zoned to the controllers : 

Controller Configuration |  Is Downgrade Possible?  
---|---  
Two controllers in the server (one in optional I/O expander) or one controller in the server (in optional I/O expander) and at least one disk is zoned to the controller in the optional I/O expander.  |  No  
Two controllers in the server (one in optional I/O expander) or one controller in the server (in optional I/O expander) and at least one disk is pre-provisioned to controller in the optional I/O expander.  |  No  
Two controllers in the server (one in optional I/O expander) or one controller in the server (in any slot) and disk are not zoned or pre-provisioned to the controller in optional I/O expander.  |  Yes  
  
### License Requirement 

Beginning with release 4.2(3b), for Cisco UCS 6536 Fabric Interconnect (UCS-FI-6536), all ports are enabled using a term-based subscription license (Supported license term: 36-60 months). 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Licensing for FI 6536 is not a port-based license like in previous FI generations. 

* * *  
  
---|---  
  
ETH_PORT_ACTIVATION_PKG (/6400 FI series), 40G_ETH_PORT_ACTIVATION_PKG (for 6400 and 6300 FI - 6332), 10G_PORT_ACTIVATION_PKG (for 6300 FI - 6332-16UP), licenses are used when S3260 system is connected to FI as appliance (appliance port) or Cisco UCS Manager managed node (server port). 

For more information on license requirement, refer Server License Management chapter in Cisco UCS Manager Server Management Guide. 


---

## Page 15: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Dense-Storage-Server-Integ-Mgmt/4-2/b_CLI_UCSM_3260_Integration_Guide_4_1_chapter_0100.html

## Chassis Discovery Policy 

The chassis discovery policy determines how the system reacts when you add a new Cisco UCS S3260 chassis or an existing standalone Cisco UCS S3260 chassis to a Cisco UCS system. [Cisco UCS S3260 System Architectural Overview](b_CLI_UCSM_3260_Integration_Guide_4_1_chapter_010.html#id_20266) describes the connectivity for a Cisco UCS S3260 system managed by Cisco UCS Manager. Cisco UCS Manager uses the settings in the chassis discovery policy to determine whether to group links from the system I/O controllers (SIOCs) to the fabric interconnects in fabric port channels. 

To add a previously standalone Cisco UCS S3260 chassis to a Cisco UCS system, you must first configure it to factory default. You can then connect both SIOCs on the chassis to both fabric interconnects. After you connect the SIOCs on the chassis to the fabric interconnects, and mark the ports as server ports, chassis discovery begins. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Chassis/IOM acknowledgement after chassis/FEX discovery policy changes is not applicable for S3260 chassis. 

* * *  
  
---|---  
  
### Server Discovery 

Cisco UCS Manager automatically discovers the Cisco UCS S3260 server nodes after the Cisco UCS S3260 chassis is discovered. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Server discovery fails if the SIOC corresponding to the server is not present. 

* * *  
  
---|---  
  
### Link Grouping

In release 4.0(1a), Link Group Preference is automatically set to Port Channel when using new SIOC with PCIe slots. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For the Cisco UCS 6400 Series Fabric Interconnect, and Cisco UCS 6536 Fabric Interconnect, the Link Group Preference is always set to Port Channel. 

* * *  
  
---|---  
  
When you connect a Cisco UCS S3260 chassis through a FEX to directly to a Cisco UCS 6300 Series fabric interconnect, or Cisco UCS 6400 Series Fabric Interconnect, and Cisco UCS 6536 Fabric Interconnect, Cisco UCS Manager ignores the Port Channel preference and the SIOCs operate in the non-port channel mode. 

Set the link grouping preference to None if the Cisco UCS S3260 chassis is connected to a fabric interconnect through a single 10G cable. 

After changing the Link Group Preference value in the Cisco UCS Manager GUI, Decommission and then Recommission the Cisco UCS S3260 chassis for the change to take effect. 

In the Cisco UCS domain, if there are other chassis operating in Port Channel mode, do the following: 

  1. Discover the chassis in the Cisco UCS system with the Link Group Preference set to Port Channel

  2. Change the link aggregation preference for the Cisco UCS S3260 chassis through Chassis Connectivity Policy 

  3. Decommission the chassis 

  4. Recommission the chassis 


### Configuring the Chassis/FEX Discovery Policy 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope org / |  Enters the root organization mode.  |  **Note** |  The chassis/FEX discovery policy can be accessed only from the root organization.   
---|---  
**Step 2** |  UCS-A /org #  scope chassis-disc-policy |  Enters organization chassis/FEX discovery policy mode.   
**Step 3** |  (Optional) UCS-A /org/chassis-disc-policy # set descr ` ` description | (Optional)  Provides a description for the chassis/FEX discovery policy.  |  **Note** |  If your description includes spaces, special characters, or punctuation, you must begin and end your description with quotation marks. The quotation marks will not appear in the description field of any  show command output.   
---|---  
**Step 4** |  UCS-A /org/chassis-disc-policy #  set link-aggregation-pref ` `{none | port-channel}  |  Specifies whether the links from the SIOCs or FEXes to the fabric interconnects are grouped into a port channel. Link aggregation can be one of the following: 

  * none—links from the SIOC or FEX are pinned to the fabric interconnect. 
  * port-channel—links from the SIOCs to the fabric interconnects are grouped into a port channel 

  
**Step 5** |  UCS-A /org/chassis-disc-policy #  commit-buffer |  Commits the transaction to the system configuration.   
  
#### Example

The following example scopes to the default chassis discovery policy, provides a description for the policy, sets the link grouping preference to port channel, specifies the server pool policy qualifications that will be used to qualify the chassis, and commits the transaction: 
    
    
    UCS-A# **scope org /**
    UCS-A /org # **scope chassis-disc-policy**
    UCS-A /org/chassis-disc-policy* # **set descr "This is an example chassis discovery policy."**
    UCS-A /org/chassis-disc-policy* # **set link-aggregation-pref port-channel**
    UCS-A /org/chassis-disc-policy* # **commit-buffer**
    UCS-A /org/chassis-disc-policy # 
    

#### What to do next

To customize fabric port channel connectivity for a specific chassis, configure the chassis connectivity policy. 


---

