# UCS Manager CLI Infrastructure Management Guide 4.3

| | |
|---|---|
| **URL Title** | UCS Manager CLI Infrastructure Management Guide 4.3 |
| **URL** | https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_4_3.html |
| **Long URL** |  |
| **HTML Title** | Cisco UCS Manager Infrastructure Management Using the CLI, Release 4.3 |
| **Source file** | `ucs-docs-raw/html/b_UCSM_CLI_Infrastructure_Management_Guide_4_3.html` |
| **File type** | HTML |
| **Fetched on** | 2026-07-02 13:02:24 |

---

## Page 1: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_4_3.html

![Clear Contents of Search](/etc/designs/cdc/fw/i/ic_clear_gray.png)

---

## Page 2: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_4_3/b_UCSM_CLI_Infrastructure_Management_Guide_4_1_preface_00.html

# Preface

## Audience

This guide is intended primarily for data center administrators with responsibilities and expertise in one or more of the following: 

  * Server administration 

  * Storage administration 

  * Network administration 

  * Network security 


## Conventions

Text Type  |  Indication   
---|---  
GUI elements  |  GUI elements such as tab titles, area names, and field labels appear in this font.  Main titles such as window, dialog box, and wizard titles appear in this font.   
Document titles  |  Document titles appear in this font.   
TUI elements  |  In a Text-based User Interface, text the system displays appears in this font.   
System output  |  Terminal sessions and information that the system displays appear in this font.   
CLI commands  |  CLI command keywords appear in this font .  Variables in a CLI command appear in this font .   
[ ]  |  Elements in square brackets are optional.   
{x | y | z}  |  Required alternative keywords are grouped in braces and separated by vertical bars.   
[x | y | z]  |  Optional alternative keywords are grouped in brackets and separated by vertical bars.   
string  |  A nonquoted set of characters. Do not use quotation marks around the string or the string will include the quotation marks.   
< > |  Nonprinting characters such as passwords are in angle brackets.   
[ ]  |  Default responses to system prompts are in square brackets.   
!, #  |  An exclamation point (!) or a pound sign (#) at the beginning of a line of code indicates a comment line.   
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Means _reader take note_. Notes contain helpful suggestions or references to material not covered in the document. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/tip.gif)  
**Tip** | 

* * *

Means _the following information will help you solve a problem_. The tips information might not be troubleshooting or even an action, but could be useful information, similar to a Timesaver. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/timesave.gif)  
**Timesaver** | 

* * *

Means _the described action saves time_. You can save time by performing the action described in the paragraph. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Means _reader be careful_. In this situation, you might perform an action that could result in equipment damage or loss of data. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/warn.gif)  
**Warning** | 

* * *

IMPORTANT SAFETY INSTRUCTIONS  This warning symbol means danger. You are in a situation that could cause bodily injury. Before you work on any equipment, be aware of the hazards involved with electrical circuitry and be familiar with standard practices for preventing accidents. Use the statement number provided at the end of each warning to locate its translation in the translated safety warnings that accompanied this device.  SAVE THESE INSTRUCTIONS 

* * *  
  
---|---  
  
## Related Cisco UCS Documentation

### Documentation Roadmaps 

For a complete list of all B-Series documentation, see the Cisco UCS B-Series Servers Documentation Roadmap available at the following URL: <https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/overview/guide/UCS_roadmap.html>

For a complete list of all C-Series documentation, see the Cisco UCS C-Series Servers Documentation Roadmapdoc roadmap available at the following URL: <https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/overview/guide/ucs_rack_roadmap.html>. 

For information on supported firmware versions and supported UCS Manager versions for the rack servers that are integrated with the UCS Manager for management, refer to [Release Bundle Contents for Cisco UCS Software](http://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-release-notes-list.html). 

## Documentation Feedback

To provide technical feedback on this document, or to report an error or omission, please send your comments to [ucs-docfeedback@external.cisco.com](mailto:ucs-docfeedback@external.cisco.com). We appreciate your feedback. 

---

## Page 3: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_4_3/b_UCSM_CLI_Infrastructure_Management_Guide_chapter_01101.html

# New and Changed Information

## New and Changed Information

This section provides information on new feature and changed behavior in Release 4.3.

Table 1. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(6a) Feature |  Description |  Where Documented  
---|---|---  
Support for Package Power Limit (PPL) |  Cisco UCS Manager supports configuring the Package Power Limit for Power Control Policy. |  [Creating a Power Control Policy](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_0111.html#task_E14D7E00D291462A8BAF78D11C604A4C)  
Support for Maximum Cooling in Fan Speed Policy |  Cisco UCS Manager supports Maximum Cooling option in Fan Speed Policy to optimize cooling efficiency for CPU. |  [Creating a Power Control Policy](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_0111.html#task_E14D7E00D291462A8BAF78D11C604A4C)  
Table 2. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(5a) Feature |  Description |  Where Documented  
---|---|---  
Support for Cisco UCS C-Series M8 server |  Cisco UCS Manager now supports Cisco UCS C225 M8 Server.  |  [Data Sanitization](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_01000.html#data-sanitization)  
Support for Cisco UCS X-Series M8 server |  Cisco UCS Manager now supports Cisco UCS X215c M8 Compute Node.  | 

  * [Overview of Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct)](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_01110.html#overview-of-cisco-ucs-x-direct)
  * [Data Sanitization](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_01000.html#data-sanitization)

  
Table 3. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(4b) Feature |  Description |  Where Documented  
---|---|---  
Support for Cisco UCS X-Series Direct |  Cisco UCS Manager now supports Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct).  | 

  * [Cisco UCS Building Blocks and Connectivity](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_01110.html#concept_uxd_4pl_3jb)
  * [Overview of Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct)](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_01110.html#overview-of-cisco-ucs-x-direct)
  * [Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct) Architecture](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_01110.html#cisco-ucs-x-direct-architecture)
  * [Port Breakout Functionality on Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct)](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_01110.html#port-breakout-functionality-on-cisco-ucs-x-direct)
  * [Chassis/FEX Discovery Policy](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_011.html#concept_40AFE09861FA4D02A9879856A1411FAC)
  * [Configuring the Chassis/FEX Discovery Policy](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_011.html#task_4984141203506035088)
  * [Chassis Connectivity Policy](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_011.html#concept_4E5E1F56073248329020AC2927156A9F)
  * [Configuring a Chassis Connectivity Policy](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_011.html#task_D41B14E4E5524F53845D38A6C8FF2C50)
  * [Power Capping in Cisco UCS](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_0111.html#concept_943D968485A04A92BAA307A2FC59AD18)

  
Table 4. New Features and Changed Behavior in Cisco UCS Manager, Release4.3(4b) Feature |  Description |  Where Documented  
---|---|---  
Support for Cisco UCS C-Series M8 servers |  Cisco UCS Manager now supports Cisco UCS C245 M8 Servers.  | 

  * [Power Capping in Cisco UCS](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_0111.html#concept_943D968485A04A92BAA307A2FC59AD18)
  * [Data Sanitization](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_01000.html#data-sanitization)

  
Table 5. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(2c) Feature |  Description |  Where Documented  
---|---|---  
Support for Cisco UCS X-Series servers |  Cisco UCS Manager supports Cisco UCS X410c M7 Compute Node.  Cisco UCS X-Series servers support Intelligent Fabric Modules (IFM), which function similarly to the Input/Output Module (IOM) in Cisco UCS B-Series servers.  |  —   
Support for Cisco UCS VIC cards |  Cisco UCS Manager supports the following Cisco UCS VIC cards:

  * Cisco UCS VIC 15230
  * Cisco UCS VIC 15237 mLOM
  * Cisco UCS VIC 15427

|  —  
Table 6. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(2b) Feature |  Description |  Where Documented  
---|---|---  
Support for Power Capping and Power Management for Cisco UCSX-9508 Chassis |  Cisco UCS Manager now supports Power Capping and Power Management for Cisco UCSX-9508 Chassis. |  [Power Capping in Cisco UCS](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_0111.html#concept_943D968485A04A92BAA307A2FC59AD18)  
Support for Cisco UCS X9508 server chassis with Cisco UCS X-Series servers |  Cisco UCS Manager supports Cisco UCSX-9508 Chassis with the following Cisco UCS X-Series servers:

  * Cisco UCS X210c M7 Compute Node
  * Cisco UCS X210c M6 Compute Node

Cisco UCS X-Series servers support Intelligent Fabric Modules (IFM), which function similarly to the Input/Output Module (IOM) in Cisco UCS B-Series servers.  |  —   
Support Cisco UCS C-Series M7 servers |  Cisco UCS Manager now supports the following C-Series M7 servers:

  * Cisco UCS C240 M7 Server
  * Cisco UCS C220 M7 Server

|  [Power Capping in Cisco UCS](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_0111.html#concept_943D968485A04A92BAA307A2FC59AD18)  
Support for Cisco UCS X9508 Server Chassis equipped with X-Fabric Module (XFM) |  Cisco UCS Manager introduces inventory support for Cisco UCS X9508 Server Chassis equipped with X-Fabric Module (XFM) |  [Viewing X-Fabric Module (XFM) Fan Status](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_0111.html#viewing-xfm-fan-overall-status)  
Support for Cisco UCS 6200 Series Fabric Interconnect is deprecated |  Cisco UCS Manager deprecates support for Cisco UCS 6200 Series Fabric Interconnects. |  —   
Support for Cisco UCS M4 servers are deprecated |  Cisco UCS Manager deprecates support for UCS B-series, C-series, and S-series M4 servers. |  — 

---

## Page 4: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_4_3/b_UCSM_CLI_Infrastructure_Management_Guide_chapter_01110.html

# Overview  
  
## Cisco UCS Manager User CLI Documentation

Cisco UCS Manager offers you a new set of smaller, use-case based documentation described in the following table: 

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
  
## Cisco Unified Computing System Overview 

Cisco UCS has a unique architecture that integrates compute, data network access, and storage network access into a common set of components under a single-pane-of-glass management interface. 

Cisco UCS fuses access layer networking and servers. This high-performance, next-generation server system provides a data center with a high degree of workload agility and scalability. The hardware and software components support Cisco's unified fabric, which runs multiple types of data center traffic over a single converged network adapter. 

Figure 1. Cisco Unified Computing System Architecture  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/305001-306000/305219.jpg)

### Architectural Simplification 

The simplified architecture of Cisco UCS reduces the number of required devices and centralizes switching resources. By eliminating switching inside a chassis, network access-layer fragmentation is significantly reduced. Cisco UCS implements Cisco unified fabric within racks and groups of racks, supporting Ethernet and Fibre Channel protocols over 10 Gigabit Cisco Data Center Ethernet and Fibre Channel over Ethernet (FCoE) links. This radical simplification reduces the number of switches, cables, adapters, and management points by up to two-thirds. All devices in a Cisco UCS domain remain under a single management domain, which remains highly available through the use of redundant components. 

### High Availability 

The management and data plane of Cisco UCS is designed for high availability and redundant access layer fabric interconnects. In addition, Cisco UCS supports existing high availability and disaster recovery solutions for the data center, such as data replication and application-level clustering technologies. 

### Scalability

A single Cisco UCS domain supports multiple chassis and their servers, all of which are administered through one Cisco UCS Manager. For more detailed information about the scalability, speak to your Cisco representative. 

### Flexibility

A Cisco UCS domain allows you to quickly align computing resources in the data center with rapidly changing business requirements. This built-in flexibility is determined by whether you choose to fully implement the stateless computing feature. Pools of servers and other system resources can be applied as necessary to respond to workload fluctuations, support new applications, scale existing software and business services, and accommodate both scheduled and unscheduled downtime. Server identity can be abstracted into a mobile service profile that can be moved from server to server with minimal downtime and no need for additional network configuration. 

With this level of flexibility, you can quickly and easily scale server capacity without having to change the server identity or reconfigure the server, LAN, or SAN. During a maintenance window, you can quickly do the following: 

  * Deploy new servers to meet unexpected workload demand and rebalance resources and traffic. 

  * Shut down an application, such as a database management system, on one server and then boot it up again on another server with increased I/O capacity and memory resources. 


### Optimized for Server Virtualization 

Cisco UCS has been optimized to implement VM-FEX technology. This technology provides improved support for server virtualization, including better policy-based configuration and security, conformance with a company's operational model, and accommodation for VMware's VMotion. 

## IOMs and Fabric Interconnects Connectivity

Each chassis is equipped with two IOMs: IOM 1 should be connected to Fabric Interconnect A. IOM 2 should be connected to Fabric Interconnect B. This configuration provides redundant paths, ensuring uninterrupted operation of the Cisco UCS system even in the event of a failure in one of the Fabric Interconnects or IOMs. Additionally, this configuration enables traffic load distribution across both Fabric Interconnects, enhancing load balancing and increasing throughput. As a result, the Cisco UCS system achieves high availability, reliability, and optimal performance, making it ideal for data center environments. 

  * Uplink Connectivity
  * Downlink Connectivity


### Uplink Connectivity 

Use fabric interconnect ports configured as uplink ports to connect to uplink upstream network switches. Connect these uplink ports to upstream switch ports as individual links, or as links configured as port channels. Port channel configurations provide bandwidth aggregation as well as link redundancy. 

You can achieve northbound connectivity from the fabric interconnect through a standard uplink, a port channel, or a virtual port channel configuration. The port channel name and ID configured on fabric interconnect should match the name and ID configuration on the upstream Ethernet switch. 

It is also possible to configure a port channel as a vPC, where port channel uplink ports from a fabric interconnect are connected to different upstream switches. After all uplink ports are configured, create a port channel for these ports. 

### Downlink Connectivity 

Beginning with release 4.3(2a), Cisco UCS Manager supports Cisco UCS X9508 server chassis with Cisco UCS X-Series servers. Cisco UCS X-Series servers support Intelligent Fabric Modules (IFM), which function similarly to the Input/Output Module (IOM) in Cisco UCS B-Series servers. This guide uses the term IOM to refer both IOM and IFM.

Each fabric interconnect is connected to IOMs in the UCS chassis, which provides connectivity to each blade server. Internal connectivity from blade servers to IOMs is transparently provided by Cisco UCS Manager using 10BASE-KR Ethernet standard for backplane implementations, and no additional configuration is required. You must configure the connectivity between the fabric interconnect server ports and IOMs. Each IOM, when connected with the fabric interconnect server port, behaves as a line card to fabric interconnect, hence IOMs should never be cross-connected to the fabric interconnect. Each IOM is connected directly to a single fabric interconnect. 

The Fabric Extender (also referred to as the IOM, or FEX) logically extends the fabric interconnects to the blade server. The best analogy is to think of it as a remote line card that’s embedded in the blade server chassis, allowing connectivity to the external world. IOM settings are pushed via Cisco UCS Manager and are not managed directly. The primary functions of this module are to facilitate blade server I/O connectivity (internal and external), multiplex all I/O traffic up to the fabric interconnects, and help monitor and manage the Cisco UCS infrastructure. 

Configure Fabric interconnect ports that should be connected to downlink IOM cards as server ports. Make sure there is physical connectivity between the fabric interconnect and IOMs. You must also configure the IOM ports and the global chassis discovery policy. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For UCS 2200 I/O modules, you can also select the Port Channel option and all I/O module-connected server ports will be automatically added to a port channel. 

* * *  
  
---|---  
  
## Cisco UCS Building Blocks and Connectivity

Figure 2. Cisco UCS Building Blocks and Connectivity 

The primary components included within Cisco UCS Manager are as follows:

  * Cisco UCS Manager—Cisco UCS Manager is the centralized management interface for Cisco UCS. For more information on Cisco UCS Manager, see Introduction to Cisco UCS Manager in Cisco UCS Manager Getting Started Guide

  * Cisco UCS Fabric Interconnects—The Cisco UCS Fabric Interconnect is the core component of Cisco UCS deployments, providing both network connectivity and management capabilities for the Cisco UCS system. The Cisco UCS Fabric Interconnects run the Cisco UCS Manager control software and consist of the following components: 

  * Cisco UCS fabric interconnects:

  * Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct) 

  * Cisco UCS 6536 Fabric Interconnect

  * Cisco UCS 6400 Series Fabric Interconnect

  * Cisco UCS 6332 Series Fabric Interconnects

  * Cisco UCS-FI-6324 (Cisco UCS Mini)

  * Transceivers for network and storage connectivity

  * Expansion modules for various Fabric Interconnects

  * Cisco UCS Manager software

For more information on Cisco UCS Fabric Interconnects, see Cisco UCS Fabric Infrastructure Portfolio. 

  * Cisco UCS I/O Modules and Cisco UCS Fabric Extender—IO modules are also known as Cisco FEX or simply FEX modules. These modules serve as line cards to the FIs in the same way that Cisco Nexus Series switches can have remote line cards. IO modules also provide interface connections to blade servers. They multiplex data from blade servers and provide this data to FIs and do the same in the reverse direction. In production environments, IO modules are always used in pairs to provide redundancy and failover. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

The 40G backplane setting is not applicable for 22xx IOMs. 

* * *  
  
---|---  
  * Cisco UCS Blade Server Chassis—The Cisco UCS 5100 Series Blade Server Chassis is a crucial building block of Cisco UCS, delivering a scalable and flexible architecture for current and future data center needs, while helping reduce total cost of ownership. 

  * Cisco UCS Blade and Rack Servers—Cisco UCS Blade servers are at the heart of the UCS solution. They come in various system resource configurations in terms of CPU, memory, and hard disk capacity. The Cisco UCS rack-mount servers are standalone servers that can be installed and controlled individually. Cisco provides Fabric Extenders (FEXs) for the rack-mount servers. FEXs can be used to connect and manage rack-mount servers from FIs. Rack-mount servers can also be directly attached to the fabric interconnect. 

Small and Medium Businesses (SMBs) can choose from different blade configurations as per business needs.

  * Cisco UCS I/O Adapters—Cisco UCS B-Series Blade Servers are designed to support up to two network adapters. This design can reduce the number of adapters, cables, and access-layer switches by as much as half because it eliminates the need for multiple parallel infrastructure for both LAN and SAN at the server, chassis, and rack levels. 


  * Cisco UCS Fabric Infrastructure Portfolio
  * Cisco UCS Chassis
  * Cisco UCS Mini Infrastructure
  * Cisco UCS Infrastructure Virtualization


### Cisco UCS Fabric Infrastructure Portfolio

The Cisco UCS fabric interconnects are top-of-rack devices and provide unified access to the Cisco UCS domain. The following fabric interconnects are available in the Cisco UCS fabric interconnects product family: 

  * Cisco UCS Manager Release 4.3(4b) introduces Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct). 

  * Cisco UCS Manager Release 4.2(3b) introduces Cisco UCS 6536 Fabric Interconnect to the Cisco UCS 6500 Series Fabric Interconnects. 

  * Cisco UCS Manager Release 4.1 introduces the Cisco UCS 64108 Fabric Interconnect to the Cisco UCS 6400 Series Fabric Interconnects. 

  * Cisco UCS 6300 Series Fabric Interconnects

  * Cisco UCS 6324 Fabric Interconnects


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The Cisco UCS 6200 Series, Cisco UCS 6100 Series Fabric Interconnects, and Cisco UCS 2104 I/O Modules have reached end of life. 

* * *  
  
---|---  
  
Cisco UCS X-Series Direct

### Overview of Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct) 

The Cisco UCS X-Series Direct is identified by the product ID UCSX-S9108-100G, and the product description Cisco UCS Fabric Interconnects 9108 100G. 

Components of Cisco UCS Fabric Interconnects 9108 100G:

  * Cisco UCS X9508 Chassis

  * A pair of Cisco UCS Fabric Interconnects 9108 100G

  * One or more of Cisco UCS X-Series M6, M7, and M8 Compute Nodes

  * Optional components:

  * Cisco UCS 9416 X-Fabric Modules

  * Cisco UCS X440p PCIe Node with up to four GPUs used in conjunction with the 9416 X-Fabric Modules


The Cisco UCS Fabric Interconnects 9108 100G platform streamlines data center architecture by eliminating the need for separate Fabric Interconnects (FIs), integrating essential networking and management functionality directly within the chassis. The Cisco UCS Fabric Interconnects 9108 100G platform is designed for deployments in smaller settings, where the compute server requirements are less extensive than those of a traditional data center. This solution is centered around a single-chassis system, the Cisco UCS X9508 Chassis, which incorporates Cisco UCS Fabric Interconnects 9108 100G directly into the chassis for a consolidated and efficient infrastructure. To ensure high availability, each chassis houses two Cisco UCS Fabric Interconnects 9108 100G that establish direct downlink connections to servers and provide uplink connections to facilitate seamless integration with both Local Area Network (LAN) and Storage Area Network (SAN) systems. The Fabric Interconnects (FIs) are adeptly designed to fit into the Cisco UCS X-Series chassis, presenting as a single module within the NX-OS environment that merges QSFP ports with server backplane ports. 

The hardware configuration of the Cisco UCS Fabric Interconnects 9108 100G platform retains the same form factor as the standard Cisco UCS X-Series chassis, and features 17 MACs, each configurable for 10G, 25G, 40G, or 100G connectivity. It is equipped with an CPU, for operating NX-OS, Cisco UCS Manager for management and Chassis Management Controller (CMC) software. The Cisco UCS Fabric Interconnects 9108 100G includes an onboard Ethernet switch with multiple 10G links dedicated to out-of-band communication between blade components such as the Baseboard Management Controller (BMC), CMC. A dedicated 1G link facilitates IFM-to-IFM clustering and high availability synchronization. Within the Cisco UCS Fabric Interconnects 9108 100G, Ethernet ports 1-8, backplane ports 9-16, and the Baseboard Interface (BIF) port 17 coexist on a singular switch card. Ports 1-2 are unified to manage all SAN features and configurations. The 100G Ethernet ports [1-8] can also be configured as 25Gx4 SFP28 compatible breakout ports or 4x10G ports, offering flexible networking solutions to accommodate a range of data center needs. 

### Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct) Architecture 

The Cisco UCS X-Series Direct architecture is engineered to support a diverse range of workloads, from traditional applications to cloud-native services, by offering a composable and disaggregated approach to computing resources. Key components of the Cisco UCS X-Series Direct architecture include: 

  * **Cisco UCSX-9508 Chassis** —A modular and future-proof chassis that can accommodate various types of compute nodes, providing the flexibility to adapt to different workload requirements without the need for a complete hardware overhaul. 

  * **Cisco UCS Fabric Interconnects 9108 100G** —This solution is centered around a single-chassis system, the Cisco UCS X9508 Chassis, which incorporates Cisco UCS Fabric Interconnects 9108 100G directly into the chassis for a consolidated and efficient infrastructure. To ensure high availability, each chassis houses two Cisco UCS Fabric Interconnects 9108 100G that establish direct downlink connections to servers and provide uplink connections to facilitate seamless integration with both Local Area Network (LAN) and Storage Area Network (SAN) systems. 

  * **Software Architecture** —In terms of the startup and operational model, the management, Cisco UCS Manager aligns with the approach taken in the Cisco UCS 6500 and 6400 Series Fabric Interconnects. In this model, Cisco UCS Manager is encapsulated within a container and is initiated by the underlying NX-OS, depending on the selected management mode. 


### Port Breakout Functionality on Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct) 

The Cisco UCS Fabric Interconnects 9108 100G is equipped with advanced port breakout functionality, which allows network administrators to subdivide a single high-bandwidth port into multiple lower-bandwidth ports. This feature is particularly beneficial for optimizing port utilization, managing cabling complexity, and adapting to various bandwidth requirements. 

Physical Port |  Breakout Options |  Logical Ports After Breakout |  Supported Speeds through breakout cables  
---|---|---|---  
Ethernet 1/1 - Ethernet 1/8 |  4x25G |  Ethernet 1/1/1 to Ethernet 1/8/4 |  Up to 8x100 Gbps  
Fibre Channel 1/1 and 1/2 |  4x8G, 4x16G, 4x32G |  Fibre Channel 1/1/1 to Fibre Channel 1/2/4 |  Up to 8x32Gbps  
  
#### Breakout Port Guidelines

Breakout ports are supported as destinations for traffic monitoring. The following are the guidelines for breakout functionality for Cisco UCS Fabric Interconnects 9108 100G: 

  * Breakout Availability: Breakout functionality is available for physical ports 1-8. 

  * Ethernet Breakout: Ethernet breakout ports can be configured on physical ports 1 through 8, resulting in 32 logical ports. 

  * Fibre Channel Breakout: Fibre Channel breakout ports can be configured on unified ports 1/8 and 2/8, resulting in 8 logical ports. 

  * Port Configurations: Physical Ports 1-8 can be configured as Uplink Ports, FCoE Uplink Ports, FCoE Storage Ports, and Appliance Ports. 

  * Port Conversions: All port conversions support up to 8 standard ports or 8 breakout ports. 

  * Server Ports: Configuration as Server Ports is not supported. 

  * Fibre Channel Direct Ports: Direct ports for Fibre Channel are not supported. 

  * Traffic Monitoring: Breakout ports can be utilized as destinations for traffic monitoring. 


Cisco UCS 6500 Series Fabric Interconnects

###  Cisco UCS 6536 Fabric Interconnect Overview 

The Cisco UCS 6536 Fabric Interconnect is a core part of the Cisco Unified Computing System, providing both network connectivity and management capabilities for the system. The Cisco UCS 6536 Fabric Interconnect provides the communication backbone and management connectivity for UCS B-series blade servers and UCS C-series rack servers. 

Cisco UCS 6500 Series Fabric Interconnects currently include Cisco UCS 6536 Fabric Interconnect. All servers attached to a Cisco UCS 6536 Fabric Interconnect become part of a single, highly available management domain. In addition, by supporting a unified fabric, Cisco UCS 6536 Fabric Interconnect provides both LAN and SAN connectivity for all servers within its domain. 

The Cisco UCS 6536 Fabric Interconnect supports multiple traffic classes over a lossless Ethernet fabric from the server through the fabric interconnect. 

### Port Breakout Functionality on Cisco UCS 6536 Fabric Interconnects

The Cisco UCS 6536 36-Port Fabric Interconnect is a One-Rack-Unit (1RU) 1/10/25/40/100 Gigabit Ethernet, FCoE, and Fibre Channel switch offering up to 7.42 Tbps throughput and up to 36 ports. 

Cisco UCS 6536 Fabric Interconnect supports splitting a single 40 Gigabit(G)/100G Quad Small Form-factor Pluggable (QSFP) port into four 10G/25G ports using a supported breakout cable. The switch has 32 40/100-Gbps Ethernet ports and four unified ports that can support 40/100-Gbps Ethernet ports or 16 Fiber Channel (FC) ports after breakout at 8/16/32-Gbps FC speeds. The 16 FC ports after breakout can operate as an FC Uplink or FC storage port. The switch also supports two ports (Port 9 and Port 10) at 1-Gbps speed using QSA, and all 36 ports can breakout for 10 or 25 Gbps Ethernet connectivity. All Ethernet ports can support FCoE. 

Port breakout is supported for Ethernet ports (1-32) and Unified ports (33-36). These 40/100G ports are numbered in a 2-tuple naming convention. The process of changing the configuration from 40G to 10G, or from 100G to 25G is called breakout, and the process of changing the configuration from [4X]10G to 40G or from [4X]25G to 100G is called unconfigure. 

When you break out a 40G port into 10G ports or a 100G port into 25G ports, the resulting ports are numbered using a 3-tuple naming convention. For example, the breakout ports of the second 40-Gigabit Ethernet port are numbered as 1/31/1, 1/31/2, 1/31/3, and 1/31/4. 

FC breakout is supported on ports 36 through 33 when each port is configured with a four-port breakout cable. For example: Four FC breakout ports on the physical port 33 are numbered as 1/33/1, 1/33/2, 1/33/3, and 1/33/4. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Fibre Channel support is only available through the configuration of the Unified Ports (36-33) as Fibre Channel breakout port.

* * *  
  
---|---  
  
The following image shows the rear view of the Cisco UCS 6536 fabric interconnect:

Figure 3. Cisco UCS 6536 Fabric Interconnect Rear View  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540805.jpg)

The following image shows the rear view of the Cisco UCS 6536 fabric interconnect that include Ports and LEDs:

Figure 4. Cisco UCS 6536 Fabric Interconnect Rear View  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540989.jpg) 1  |  Ports 1-32. Uplink ports are Ethernet port that can operate with the port speed of 10 Gbps/25 Gbps/40 Gbps/100 Gbps. When using a breakout cable, each of these ports can operate as: 4 x 10 Gbps/4x 25 Gbps/1 x 40 Gbps/1 x 100 Gbps Ethernet or FCoE ports.  |  2  |  Ports 33-36. Unified Ports can operate with port speed of 10 Gbps/25 Gbps/ 40 Gbps/100 Gbps Ethernet. or  8 Gbps/16 Gbps/32 Gbps Fibre Channel (FC). When using a breakout cable, each of these ports can operate as 4 x 10 Gbps/4 x 25 Gbps Ethernet or 4x8Gbps/4x16Gbps/4x32Gbps FC ports.   
---|---|---|---  
3  |  Ports 1-36. Uplink ports and Unified ports that can be configured as Ethernet Breakout Port and can operate with the port speed of 10 Gbps/25 Gbps/40 Gbps/100 Gbps.  When using a breakout cable, each of these ports can operate as: 4 x 10 Gbps/4x 25 Gbps/1 x 40 Gbps/1 x 100 Gbps Ethernet or FCoE ports.  |  4 | System environment (fan fault) LED  
5 |  System status (STS) LED |  6 |  Beacon (BCN) LED  
  
#### Breakout Port Guidelines

The following are the guidelines for breakout functionality for Cisco UCS 6536 Fabric Interconnects: 

  * The configurable breakout ports are from port 1-36.

  * You can configure the speed for each breakout port. Each breakout port can be configured at the speed of 4 x 8 Gbps/ 4 x 16 Gbps/ 4 x 32 Gbps for Fibre Channel. 

  * For Fibre Channel breakout, each breakout port can be configured at the speed of 4 x 8 Gbps/ 4 x 16 Gbps/ 4 x 32 Gbps.

  * For Ethernet breakout, each breakout port can be configured at the speed of 4 x 10 Gbps/4 x 25 Gbps.

  * Fibre Channel breakout ports are supported, and Fiber Channel direct ports are not supported.

  * FC breakout port can be configured from 1/36 through 1/33. FC breakout ports (36-33) cannot be configured unless the previous ports are FC breakout ports. Configuration of a single (individual) FC breakout port is also supported. 

  * If the breakout mode for any of the supported Fabric Interconnect ports (1-36) is an Ethernet breakout, the Fabric Interconnect does not lead to a reboot. 

  * If the breakout mode for any of the supported Fabric Interconnect ports (36-33) is a Fibre Channel uplink breakout, the Fabric Interconnect leads to a reboot. 

  * Breakout ports are supported as destinations for traffic monitoring.

  * Ports 1-36 can be configured as Server Port, FCoE Uplink Port, Appliance Port, and Monitor Port.

  * Port 36-33 can be configured also as FC Uplink Port or FC Storage Port when configured as unified port.


Cisco UCS 6400 Series Fabric Interconnects

### Cisco UCS 6400 Series Fabric Interconnect Overview 

Cisco UCS 6400 Series Fabric Interconnect provides both network connectivity and management capabilities to the Cisco UCS system. The fabric interconnect provides Ethernet and Fibre Channel to the servers in the system, the servers connect to the fabric interconnect, and then to the LAN or SAN. 

Each Cisco UCS 6400 Series Fabric Interconnect runs Cisco UCS Manager to fully manage all Cisco UCS elements. The fabric interconnect supports 10/25 Gigabit ports in the fabric with 40/100 Gigabit uplink ports. High availability can be achieved when a Cisco UCS 6400 Series Fabric Interconnect is connected to another Cisco UCS 6400 Series Fabric Interconnect through the L1 or L2 port on each device. 

Cisco UCS 6400 Series Fabric Interconnect consists of: 

  * Cisco UCS 6454 Fabric Interconnects 

  * Cisco UCS 64108 Fabric Interconnects 


The Cisco UCS 6400 Series fabric interconnect supports Cisco UCS B-Series Blade Servers, UCS 5108 B-Series Server Chassis, C-Series Rack Servers, and UCS S-Series Storage Servers. 

### Cisco UCS 64108 Fabric Interconnect

The Cisco UCS 64108 Fabric Interconnect is a 2 RU top-of-rack (TOR) switch that mounts in a standard 19-inch rack such as the Cisco R Series rack. 

The high-density Cisco UCS 64108 Fabric Interconnect has 96 10/25 Gb SFP28 ports and 12 40/100 Gb QSFP28 ports. Each 40/100 Gb port can break out into 4 x 10/25 Gb uplink ports. Ports 1 - 16 are unified ports that support 10/25 GbE or 8/16/32G Fibre Channel speeds. Ports 89-96 support 1Gbps Ethernet speeds. 

The Cisco UCS 64108 Fabric Interconnect supports either: 

  * Eight FCoE port channels

  * Or Four SAN port channels

  * or Four SAN port channels and four FCoE port channels


The Cisco UCS 64108 Fabric Interconnect also has one network management port, one RS-232 serial console port for setting the initial configuration, and one USB port for saving or loading configurations. The FI also includes L1/L2 ports for connecting two fabric interconnects in a high-availability configuration. 

The Cisco UCS 64108 Fabric Interconnect also contains a CPU board that consists of: 

  * Intel Xeon Processor, 6 core

  * 64 GB of RAM 

  * 8 MB of NVRAM (4 x NVRAM chips)

  * 128 GB SSD (bootflash)


Figure 5. Cisco UCS 64108 Fabric Interconnect Rear View ![](/c/dam/en/us/td/i/300001-400000/300001-310000/307001-308000/307644.jpg) 1  |  Ports 1-16  Unified ports:

  * 10/25 Gbps Ethernet or FCoE
  * 8/16/32 Gbps Fibre Channel

|  2  |  Ports 17-88 (10/25 Gbps Ethernet or FCoE)  
---|---|---|---  
3  |  Ports 89-96

  * 10/25 Gbps Ethernet or FCoE
  * 1 Gbps Ethernet

|  4 |  Uplink Ports 97-108 (40/100 Gbps Ethernet or FCoE) Each of these ports can be 4 x 10/25 Gbps Ethernet or FCoE uplink ports when using a breakout cable.  
5 |  System environment (fan fault) LED |  6 |  System status LED  
7 |  Beacon LED |  |   
  
The Cisco UCS 64108 Fabric Interconnect has two power supplies (redundant as 1+1) and three fans (redundant as 2+1). 

Figure 6. Cisco UCS 64108 Fabric Interconnect Front View ![](/c/dam/en/us/td/i/300001-400000/300001-310000/307001-308000/307645.jpg) **1** |  Cooling fans (hot swappable, 2+1 redundancy) |  **2** |  RS-232 serial console port (RJ-45 connector)  
---|---|---|---  
**3** |  Network management port (RJ-45 connector) |  4 |  USB port  
5 |  Grounding pad for two-hole grounding lug (under protective label) |  6 |  Power supplies Two identical AC or DC PSUs, hot-swappable, 1+1 redundancy)  
7 |  L1/L2 high-availability ports (RJ-45 connector) |  8 |  Beacon LED  
9 |  System status LED |  |   
  
### Cisco UCS 6454 Fabric Interconnect

The Cisco UCS 6454 Fabric Interconnect (FI) is a 1-RU top-of-rack switch that mounts in a standard 19-inch rack such as the Cisco R Series rack. 

The Cisco UCS 6454 Fabric Interconnect has 48 10/25 Gb SFP28 ports (16 unified ports) and 6 40/100 Gb QSFP28 ports. Each 40/100 Gb port can break out into 4 x 10/25 Gb uplink ports. The sixteen unified ports support 10/25 GbE or 8/16/32G Fibre Channel speeds. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The Cisco UCS 6454 Fabric Interconnect supported 8 unified ports (ports 1 - 8) with Cisco UCS Manager 4.0(1) and 4.0(2), but with release 4.0(4) and later it supports 16 unified ports (ports 1 - 16). 

* * *  
  
---|---  
  
The Cisco UCS 6454 Fabric Interconnect supports: 

  * Maximum of 8 FCoE port channels

  * Or 4 SAN port channels

  * Or a maximum of 8 SAN port channels and FCoE port channels (4 each)


The Cisco UCS 6454 Fabric Interconnect also has one network management port, one console port for setting the initial configuration, and one USB port for saving or loading configurations. The FI also includes L1/L2 ports for connecting two fabric interconnects for high availability. 

The Cisco UCS 6454 Fabric Interconnect also contains a CPU board that consists of: 

  * Intel Xeon D-1528 v4 Processor, 1.6 GHz

  * 64 GB of RAM 

  * 8 MB of NVRAM (4 x NVRAM chips)

  * 128 GB SSD (bootflash)


Figure 7. Cisco UCS 6454 Fabric Interconnect Rear View ![](/c/dam/en/us/td/i/300001-400000/300001-310000/306001-307000/306755.jpg) 1  |  Ports 1-16 (Unified Ports 10/25 Gbps Ethernet or FCoE or 8/16/32 Gbps Fibre Channel) |  **Note** |  When using Cisco UCS Manager releases earlier than 4.0(4), only ports 1-8 are Unified Ports.  
---|---  
2  |  Ports 17-44 (10/25 Gbps Ethernet or FCoE) |  **Note** |  When using Cisco UCS Manager releases earlier than 4.0(4), ports 9-44 are 10/25 Gbps Ethernet or FCoE.  
---|---  
3  |  Ports 45-48 (1/10/25 Gbps Ethernet or FCoE)  |  4 |  Uplink Ports 49-54 (40/100 Gbps Ethernet or FCoE) Each of these ports can be 4 x 10/25 Gbps Ethernet or FCoE uplink ports when using an appropriate breakout cable.  
  
The Cisco UCS 6454 Fabric Interconnect chassis has two power supplies and four fans. Two of the fans provide front to rear airflow. 

Figure 8. Cisco UCS 6454 Fabric Interconnect Front View ![](/c/dam/en/us/td/i/300001-400000/300001-310000/306001-307000/306354.jpg) **1** |  Power supply and power cord connector  |  **2** |  Fans 1 through 4, numbered left to right, when facing the front of the chassis.  
---|---|---|---  
**3** |  L1 port, L2 port, RJ45, console, USB port, and LEDs |  |   
  
### Ports on the Cisco UCS Fabric Interconnects

Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct) has eight ports that include: 

  * Ports 1 & 2 that are unified ports to manage all SAN features and configurations.

  * The 100G Ethernet ports [1-8] can also be configured as 25Gx4 SFP28 compatible breakout ports or 4x10G ports, offering flexible networking solutions to accommodate a range of data center needs. 

  * The 32G Fibre Channel ports [1 & 2] can also be configured as 8Gx4 SFP28 compatible breakout ports offering flexible networking solutions to accommodate a range of data center needs. 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Migration of any previous generation Fabric Interconnects to the Cisco UCS 9108 100G Intelligent Fabric Module is currently not supported. 

* * *  
  
---|---  
  
Ports on the Cisco UCS 6536 Fabric Interconnects can be configured to carry either Ethernet or Fibre Channel traffic. You can configure only ports 33-36 to carry Fibre Channel traffic. The ports cannot be used by a Cisco UCS domain until you configure them. 

Ports on the Cisco UCS 6400 Series Fabric Interconnects can be configured to carry either Ethernet or Fibre Channel traffic. You can configure only ports 1-16 to carry Fibre Channel traffic. The ports cannot be used by a Cisco UCS domain until you configure them. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

  * The Cisco UCS 6454 Fabric Interconnect supported 8 unified ports (ports 1 - 8) with Cisco UCS Manager 4.0(1) and 4.0(2), but with Release 4.0(4) and later releases, it supports 16 unified ports (ports 1 - 16).  When you configure a port on a Fabric Interconnect, the administrative state is automatically set to enabled. If the port is connected to another device, this may cause traffic disruption. The port can be disabled and enabled after it has been configured. 


* * *  
  
---|---  
  
The following table summarizes the port support for third, fourth, fifth generation of Cisco UCS Fabric Interconnects, and Cisco UCS Fabric Interconnects 9108 100G.

|  Third Generation  |  Fourth Generation |  Fifth Generation |  Cisco UCS X-Series Direct  
---|---|---|---|---  
Item  |  Cisco UCS 6332  |  Cisco UCS 6332-16UP  |  Cisco UCS 6454 |  Cisco UCS 64108 |  Cisco UCS 6536 |  Cisco UCS 9108 100G FI  
Description  |  32-Port Fabric Interconnect  |  40-Port Fabric Interconnect  |  54-Port Fabric Interconnect  |  108-Port Fabric Interconnect |  36-Port Fabric Interconnect |  8 Ports  
Form factor  |  1 RU  |  1 RU  |  1 RU  |  2 RU |  1 RU |  1 RU  
Number of fixed 10 GB Interfaces  |  96 (40G to 4 x 10G breakout cables), QSA, Port 13 and 14 do not support 40G to 10G breakout  |  88 (40G to 4 x 10G breakout cables)  |  48 10G/25G interfaces |  96 10G/25G interfaces |  36 10G/25G/40G/100G interfaces |  **Note** |  144 breakout ports (36x4)  
---|---  
—   
Number of Unified Ports |  —  |  16  |  16 This FI supported 8 unified ports (ports 1 - 8) with Cisco UCS Manager 4.0(1) and 4.0(2), but with Release 4.0(4) and later it supports 16 unified ports (ports 1 - 16).  |  16 ports 1-16 |  4 |  **Note** |  16 breakout ports (4x4)  
---|---  
Ports 1-2  
Unified Port Speeds in Gbps |  —  |  1G/10G or 4G/8G/16G-FC  |  10G/25G or 8G/16G/32G-FC  |  10G/25G or 8G/16G/32G-FC |  10G/25G/40G/100G FC |  8G/16G/32G FC  
Number of 40-Gbps ports  |  32  |  24  |  6 40G/100G  |  12 40G/100G  |  36 |  —   
Unified Port Range  |  None  |  Ports 1-16  |  Ports 1-16  |  Ports 1-16  |  Ports 33-36 |  Ports 1-2  
Compatibility with the IOM  |  UCS 2204, UCS 2208, UCS 2304, UCS 2304V2 |  UCS 2204, UCS 2208, UCS 2304, UCS 2304V2 |  UCS 2204, UCS 2208, UCS 2408 |  UCS 2204, UCS 2208, UCS 2408 |  UCS 2408, UCS 2304, UCS 2304V2 |  —   
Compatibility with the FEX |  Cisco Nexus 2232PP Cisco Nexus 2232TM-E Cisco Nexus 2348UPQ |  Cisco Nexus 2232PP Cisco Nexus 2232TM-E Cisco Nexus 2348UPQ |  Cisco Nexus 2232PP Cisco Nexus 2232TM-E Cisco Nexus 93180YC-FX3 |  Cisco Nexus 2232PP Cisco Nexus 2232TM-E Cisco Nexus 93180YC-FX3 |  Cisco Nexus 93180YC-FX3 N2K-C2348UPQ |  —   
Expansion Slots  |  None  |  None  |  None  |  None |  None |  —   
Fan Modules  |  4  |  4  |  4 |  3 |  6 |  3  
Power Supplies  |  2 (AC/DC)  |  2 (AC/DC)  |  2 (AC/DC)  |  2 (AC/DC)  |  2 (AC) |  Supplied by chassis  
  
### Port Breakout Functionality on Cisco UCS 64108 Fabric Interconnects

#### About Breakout Ports

Cisco UCS 64108 fabric interconnects support splitting a single 40/100G QSFP port into four 10/25G ports using a supported breakout cable. On the UCS 64108 fabric interconnect, by default, there are 12 ports in the 40/100G mode. These are ports 97 to 108. These 40/100G ports are numbered in a 2-tuple naming convention. For example, the second 40G port is numbered as 1/99. The process of changing the configuration from 40G to 10 G, or from 100G to 25G is called breakout, and the process of changing the configuration from [4X]10G to 40G or from [4X]25G to 100G is called unconfigure. These ports can be used as uplink port, appliance port, server port (using FEX), and FCoE storage port. 

When you break out a 40G port into 10G ports or a 100G port into 25G ports, the resulting ports are numbered using a 3-tuple naming convention. For example, the breakout ports of the second 40-Gigabit Ethernet port are numbered as 1/99/1, 1/99/2, 1/99/3, 1/99/4. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCS Manager does not support connection of FEX, chassis, blade, IOM, or adapters (other than VIC adapters) to the uplink ports of Fabric Interconnect. 

* * *  
  
---|---  
  
Starting with Cisco UCS Manager Release 4.2(3b), configuring the Ethernet breakout ports will not lead to Fabric Interconnect reboot. 

The following image shows the rear view of the Cisco UCS 64108 fabric interconnect, and includes the ports that support breakout port functionality: 

Figure 9. Cisco UCS 64108 Fabric Interconnect Rear View ![](/c/dam/en/us/td/i/300001-400000/300001-310000/307001-308000/307644.jpg) 1  |  Ports 1-16. Unified Ports can operate as 10/25 Gbps Ethernet or 8/16/32 Gbps Fibre Channel. FC ports are converted in groups of four.  Unified ports:

  * 10/25 Gbps Ethernet or FCoE
  * 8/16/32 Gbps Fibre Channel

|  2  |  Ports 1-96. Each port can operate as either a 10 Gbps or 25 Gbps Ethernet or FCoE SFP28 port.   
---|---|---|---  
3  |  Uplink Ports 97-108. Each port can operate as either a 40 Gbps or 100 Gbps Ethernet or FCoE port. When using a breakout cable, each of these ports can operate as 4 x 10 Gbps or 4 x 25 Gbps Ethernet or FCoE ports.  Ports 97 - 108 can be used to connect to Ethernet or FCoE uplink ports, and not to UCS server ports. |  4 |  Ports 89-96

  * 10/25 Gbps Ethernet or FCoE
  * 1 Gbps Ethernet

  
5 |  System environment (fan fault) LED |  6 |  System status LED  
7 |  Beacon LED |  |   
  
#### Breakout Port Guidelines

The following are the guidelines for breakout functionality for Cisco UCS 64108 fabric interconnects: 

  * The breakout configurable ports are ports 97-108.

  * You cannot configure the speed for each breakout port. Each breakout port is in auto mode.

  * Breakout ports are not supported as destinations for traffic monitoring.

  * Ports 97-108 at 40/100G can be configured as uplink, FCoE, or appliance port. Ports 97-108 after breakout to 10/25G can be configured as uplink, appliance, FCoE, or for direct-connect rack server connectivity. 


### Port Breakout Functionality on Cisco UCS 6454 Fabric Interconnects

#### About Breakout Ports

Cisco UCS 6454 fabric interconnects support splitting a single 40/100G QSFP port into four 10/25G ports using a supported breakout cable. These ports can be used only as uplink ports connecting to a 10/25G switch. On the UCS 6454 fabric interconnect, by default, there are 6 ports in the 40/100G mode. These are ports 49 to 54. These 40/100G ports are numbered in a 2-tuple naming convention. For example, the second 40G port is numbered as 1/50. The process of changing the configuration from 40G to 10 G, or from 100G to 25G is called breakout, and the process of changing the configuration from [4X]10G to 40G or from [4X]25G to 100G is called unconfigure. 

When you break out a 40G port into 10G ports or a 100G port into 25G ports, the resulting ports are numbered using a 3-tuple naming convention. For example, the breakout ports of the second 40-Gigabit Ethernet port are numbered as 1/50/1, 1/50/2, 1/50/3, 1/50/4. 

Starting with Cisco UCS Manager Release 4.2(3b), Ethernet breakout ports configuration will not lead to Fabric Interconnect reboot. 

Starting with Cisco UCS Manager Release 4.1(3a), you can connect Cisco UCS Rack servers with VIC 1455 and 1457 adapters, to the uplink ports 49 to 54 (40/100 Gbps Ethernet or FCoE) in Cisco UCS 6454 Fabric Interconnects. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCS Manager does not support connection of FEX, chassis, blade, IOM, or adapters (other than VIC 1455 and 1457 adapters) to the uplink ports of Fabric Interconnect. 

* * *  
  
---|---  
  
The following image shows the rear view of the Cisco UCS 6454 fabric interconnect, and includes the ports that support breakout port functionality: 

Figure 10. Cisco UCS 6454 Fabric Interconnect Rear View ![](/c/dam/en/us/td/i/300001-400000/300001-310000/306001-307000/306755.jpg) 1  |  Ports 1-16 (Unified Ports 10/25 Gbps Ethernet or FCoE or 8/16/32 Gbps Fibre Channel) |  2  |  Ports 17-44 (10/25 Gbps Ethernet or FCoE)  
---|---|---|---  
3  |  Ports 45-48 (1/10/25 Gbps Ethernet or FCoE)  |  4 |  Uplink Ports 49-54 (40/100 Gbps Ethernet or FCoE)   
  
#### Breakout Port Guidelines

The following are the guidelines for breakout functionality for Cisco UCS 6454 fabric interconnects: 

  * The breakout configurable ports are ports 49-54.

  * You cannot configure the speed for each breakout port. Each breakout port is in auto mode.

  * In Cisco UCS Manager Release 4.0(2), breakout ports are not supported as destinations for traffic monitoring.

  * Ports 49-54 at 40/100G can be configured as uplink, FCoE, or appliance port. Ports 49-54 after breakout to 10/25G can be configured as uplink, appliance, FCoE, or for direct-connect rack server connectivity. 


### Software Feature Configuration on Cisco UCS 6400 Series Fabric Interconnects 

Cisco UCS Manager Release 4.0(1) and 4.0(2) introduced support for various software features on Cisco UCS 6454 Fabric Interconnects. Cisco UCS Manager Release 4.1 extends support for these features on Cisco UCS 64108 Fabric Interconnects. These software features are: 

  * Switching Modes—Support for Ethernet and FC switching modes on Cisco UCS 6400 Series Fabric Interconnects . 

  * MAC Security—Support for MAC security on Cisco UCS 6400 Series Fabric Interconnects. 

  * Breakout Uplink Ports—Support for splitting a single 40/100G QSFP port into four 10/25G ports using a supported breakout cable. These ports can be used only as Ethernet uplink or FCoE uplink ports connecting to a 10/25G switch. They cannot be configured as server ports, FCoE storage ports, appliance ports or monitoring ports. 

  * MTU Configuration—Cisco UCS 64108 Fabric Interconnects support MTU configuration for QOS drop class policy. 


Cisco UCS 6400 Series Fabric Interconnects do not support the following software features: 

  * Chassis Discovery Policy in Non-Port Channel Mode—Cisco UCS 6400 Series Fabric Interconnects support only Port Channel mode. 

  * Chassis Connectivity Policy in Non-Port Channel Mode—Cisco UCS 6400 Series Fabric Interconnects support only Port Channel mode. 

  * Multicast Hardware Hash—Cisco UCS 6400 Series Fabric Interconnects do not support multicast hardware hash. 

  * Service Profiles with Dynamic vNICS—Cisco UCS 6400 Series Fabric Interconnects do not support Dynamic vNIC Connection Policies. 

  * Multicast Optimize—Cisco UCS 6400 Series Fabric Interconnects do not support Multicast Optimize for QoS. 

  * Port profiles and DVS Related Configurations—Cisco UCS 6400 Series Fabric Interconnects do not support configurations related to port profiles and distributed virtual switches (DVS). 


Configuration of the following software features has changed for Cisco UCS 6400 Series Fabric Interconnects: 

  * Unified Ports—Cisco UCS 6400 Series Fabric Interconnects support up to 16 unified ports, which can be configured as FC. These ports appear at the beginning of the module. 

  * VLAN Optimization—On Cisco UCS 6400 Series Fabric Interconnects, you can configure VLAN port count optimization through port VLAN (VP) grouping when the PV count exceeds 16000. The following table illustrates the PV Count with VLAN port count optimization enabled and disabled on Cisco UCS 6400 Series Fabric Interconnect, Cisco UCS 6300 Series Fabric Interconnects. 

|  6300 Series FI |  6400 Series FI |  6500 Series FI (6536 FI)  
---|---|---|---  
PV Count with VLAN Port Count Optimization Disabled |  16000 |  16000 |  16000  
PV Count with VLAN Port Count Optimization Enabled |  64000 |  108000 |  108000  
  
When a Cisco UCS 6400 Series Fabric Interconnect is in Ethernet switching mode: 

  * The Fabric Interconnect does not support VLAN Port Count Optimization Enabled

  * The Fabric Interconnect supports 16000 PVs, similar to EHM mode, when set to VLAN Port Count Optimization Disabled

  * Limited Restriction on VLAN—Cisco UCS 6400 Series Fabric Interconnects reserve 128 additional VLANs for system purposes. 


Cisco UCS 6300 Series Fabric Interconnects

### Fabric Interconnect Features 

A Cisco UCS 6300 Series Fabric Interconnect provides both network connectivity and management capabilities to a Cisco UCS system. The fabric interconnect provides Ethernet and Fibre Channel to the servers in the system, the servers connect to the fabric interconnect, and the fabric interconnect connects to the LAN or SAN. 

Each Cisco UCS 6300 Series Fabric Interconnect runs Cisco UCS Manager to fully manage all Cisco UCS elements. The fabric interconnect supports full end-to-end 40-Gigabit capabilities in the fabric and enables 16-Gigabit Fibre Channel capabilities. High availability can be achieved when a Cisco UCS 6300 Series Fabric Interconnect is connected to another Cisco UCS 6300 Series Fabric Interconnect through the L1 or L2 port on each device. 

The Cisco UCS 6300 Series Fabric Interconnect joins next-generation UCS products, including the following hardware: 

  * Cisco UCS 6332 Fabric Interconnect, an Ethernet or Fibre Channel over Ethernet (FCoE) chassis with 32 40-Gigabit QSFP+ ports 

  * Cisco UCS 6332-16UP Fabric Interconnect, an Ethernet, FCoE, and Fibre Channel chassis with 16 1- or 10-Gigabit SFP+ ports or 16 4-, 8-, or 16-Gigabit Fibre Channel ports, 24 40-Gigabit QSFP+ ports 

  * Cisco 2304 IOM  or Cisco 2304V2, I/O modules with 8 40-Gigabit backplane ports and 4 40-Gigabit uplink ports 

  * Multiple VICs 


### Cisco UCS 6332 Fabric Interconnect 

The Cisco UCS 6332 Fabric Interconnect is a 1-RU, top-of-rack switch with 32 40-Gigabit QSFP+ ports, one 100/1000 network management port, one RS-232 console port for setting the initial configuration, and two USB ports for saving or loading configurations. The switch also includes an L1 port and an L2 port for connecting two fabric interconnects to provide high availability. The switch mounts in a standard 19-inch rack, such as the Cisco R Series rack. 

Cooling fans pull air front-to-rear. That is, air intake is on the fan side and air exhaust is on the port side.

Figure 11. Cisco UCS 6332 Fabric Interconnect Rear View ![](/c/dam/en/us/td/i/300001-400000/300001-310000/305001-306000/305190.jpg) 1  |  Port lane switch button, port lane LEDs, and L1 and L2 ports.  |  2  |  Ports 1–12 and ports 15–26 can operate as 40-Gbps QSFP+ ports, or as 4 x 10-Gbps SFP+ breakout ports.  Ports 1 - 4 support Quad to SFP or SFP+ (QSA) adapters to provide 1-Gbps/10 Gbps operation. Ports 13 and 14 can operate as 40-Gbps QSFP+ ports. They cannot operate as 4 x 10-Gbps SFP+ breakout ports.   
---|---|---|---  
3  |  Ports 27–32 operate as 40-Gbps QSFP+ ports.  |  |   
Figure 12. Cisco UCS 6332 Fabric Interconnect Front View   
![](/c/dam/en/us/td/i/300001-400000/300001-310000/305001-306000/305191.jpg)  
**1** |  Power supply and power cord connector  |  **2** |  Fans1 through 4, numbered left to right, when facing the front of the chassis.   
---|---|---|---  
**3** |  Management, console, and USB ports, and LEDs. |  **** |   
  
### Cisco UCS 6332-16UP Fabric Interconnect 

The Cisco UCS 6332-16UP Fabric Interconnect is a 1-RU top-of-rack switch with 24 40-Gb QSFP+ ports, 16 10-Gb SFP ports, one 100/1000 network management port, one RS-232 console port for setting the initial configuration, and two USB ports for saving or loading configurations. The switch also includes an L1 port and an L2 port for connecting two fabric interconnects to provide high availability. The switch mounts in a standard 19-inch rack, such as the Cisco R Series rack. 

Cooling fans pull air front-to-rear. That is, air intake is on the fan side and air exhaust is on the port side.

Figure 13. Cisco UCS 3223-16UP Fabric Interconnect Rear View ![](/c/dam/en/us/td/i/300001-400000/300001-310000/305001-306000/305256.jpg) **1** |  Port lane switch button, port lane LEDs, and L1 and L2 ports. |  **2** |  Ports 1–16 are Unified Ports (UP) that operate either as 1- or 10-Gbps SFP+ fixed Ethernet ports; or as 4-, 8-, or 16-Gigabit Fibre Channel ports.   
---|---|---|---  
**3** |  Ports 17–34 operate either as 40-Gbps QSFP+ ports, breakout mode for 4 x 10-Gigabit SFP+ breakout ports, or QSA for 10G.  |  **4** |  Ports 35–40 operate as 40-Gbps QSFP+ ports.   
Figure 14. Cisco UCS 6332-16UP Fabric Interconnect Front View   
![](/c/dam/en/us/td/i/300001-400000/300001-310000/305001-306000/305185.jpg)  
**1** |  Power supply and power cord connector  |  **2** |  Fans1 through 4, numbered left to right, when facing the front of the chassis.  
---|---|---|---  
**3** |  Management, console, and USB ports, and LEDs.  |  **** |   
  
### Ports on the Cisco UCS 6300 Series Fabric Interconnects 

Ports on the Cisco UCS 6300 Series Fabric Interconnects can be configured to carry either Ethernet or Fibre Channel traffic. These ports are not reserved. They cannot be used by a Cisco UCS domain until you configure them. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

When you configure a port on a fabric interconnect, the administrative state is automatically set to enabled. If the port is connected to another device, this may cause traffic disruption. You can disable the port after it has been configured. 

* * *  
  
---|---  
  
The following table summarizes the third generation ports for the Cisco UCS fabric interconnects. 

|  Cisco UCS Mini  |  Third Generation   
---|---|---  
Item  |  Cisco UCS 6324  |  Cisco UCS 6332  |  Cisco UCS 6332-16UP   
Description  |  Fabric Interconnect with 4 unified ports and 1 scalability port  |  32–Port Fabric Interconnect  |  40–Port Fabric Interconnect   
Form factor  |  1 RU  |  1 RU  |  1 RU   
Number of fixed 40 GB Interfaces  |  —  |  6(Ports 17–32)  |  6(Ports 35–40)   
Number of 1GB/10GB Interfaces (depending on the SFP module installed)  |  All  |  Ports 5–26 using breakout cable  |  Ports 17–34 using breakout cable   
Unified Ports (8 Gb/s, FC, FCoE)  |  4  |  None  |  Ports 1–16   
Compatibility with all IOMs  |  All  |  All  |  All   
Expansion Slots  |  None  |  None  |  None   
Fan Modules  |  4  |  4  |  4   
Power Supplies  |  —  |  2 (AC/DC available)  |  2 (AC/DC available)   
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCS 6300 Series Fabric Interconnects support breakout capability for ports. For more information on how the 40G ports can be converted into four 10G ports, see Port Breakout Functionality on Cisco UCS 6300 Series Fabric Interconnects. 

* * *  
  
---|---  
  
  * Port Modes
  * Port Types
  * Port Breakout Functionality on Cisco UCS 6300 Series Fabric Interconnects


#### Port Modes

The port mode determines whether a unified port on the fabric interconnect is configured to carry Ethernet or Fibre Channel traffic. You configure the port mode in Cisco UCS Manager. However, the fabric interconnect does not automatically discover the port mode. 

Changing the port mode deletes the existing port configuration and replaces it with a new logical port. Any objects associated with that port configuration, such as VLANs and VSANS, are also removed. There is no restriction on the number of times you can change the port mode for a unified port. 

#### Port Types

The port type defines the type of traffic carried over a unified port connection. 

By default, unified ports changed to Ethernet port mode are set to the Ethernet uplink port type. Unified ports changed to Fibre Channel port mode are set to the Fibre Channel uplink port type. You cannot unconfigure Fibre Channel ports. 

Changing the port type does not require a reboot. 

Ethernet Port Mode

When you set the port mode to Ethernet, you can configure the following port types: 

  * Server ports 

  * Ethernet uplink ports 

  * Ethernet port channel members 

  * FCoE ports 

  * Appliance ports 

  * Appliance port channel members 

  * SPAN destination ports 

  * SPAN source ports 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For SPAN source ports, configure one of the port types and then configure the port as SPAN source. 

* * *  
  
---|---  


Fibre Channel Port Mode

When you set the port mode to Fibre Channel, you can configure the following port types: 

  * Fibre Channel uplink ports 

  * Fibre Channel port channel members

  * Fibre Channel storage ports 

  * SPAN source ports 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For SPAN source ports, configure one of the port types and then configure the port as SPAN source. 

* * *  
  
---|---  


#### Port Breakout Functionality on Cisco UCS 6300 Series Fabric Interconnects 

##### About Breakout Ports 

Cisco UCS fabric interconnect 6300 series supports splitting a single QSFP port into four 10G ports using a supported breakout cable. By default, there are 32 ports in the 40G mode. These 40G ports are numbered in a 2-tuple naming convention. For example, the second 40G port is numbered as 1/2. The process of changing the configuration from 40G to 10G is called breakout and the process of changing the configuration from [4X]10G to 40G is called unconfigure. 

When you break out a 40G port into 10G ports, the resulting ports are numbered using a 3-tuple naming convention. For example, the breakout ports of the second 40-Gigabit Ethernet port are numbered as 1/2/1, 1/2/2, 1/2/3, 1/2/4. 

The following image shows the front view for the Cisco UCS 6332 series fabric interconnects, and includes the ports that may support breakout port functionality: 

Figure 15. Cisco UCS 6332 Series Fabric Interconnects Front View  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/305001-306000/305235.jpg) 1  |  L1 and L2 high availability ports   
---|---  
2  |  28 X 40G QSFP ports ( 98 X 10G SFP ports)  |  **Note** | 

  * QSA module is required on ports 13–14 
  * A QSFP to 4XSFP breakout cable is required for 10G support. 

  
---|---  
3  |  6 X 40G QSFP ports   
  
The following image shows the front view for the Cisco UCS 6332-16UP series fabric interconnects, and includes the ports that may support breakout port functionality: 

Figure 16. Cisco UCS 6332-16UP Series Fabric Interconnects Front View  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/305001-306000/305236.jpg) 1  |  L1 and L2 high availability ports   
---|---  
2  |  16 X 1/10G SFP (16 X 4/8/16G FC ports)   
3  |  18 X 40G QSFP(72 X 10G SFP+)  |  **Note** | 

  * A QSFP to 4XSFP breakout cable is required for 10G support. 

  
---|---  
4  |  6 X 40G QSFP ports   
  
The following image shows the rear view of the Cisco UCS 6300 series fabric interconnects. 

Figure 17. Cisco UCS 6300 Series Fabric Interconnects Rear View  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/305001-306000/305237.jpg) 1  |  Power supply   
---|---  
2  |  Four fans   
3  |  Power supply   
4  |  Serial ports   
  
##### Breakout Port Constraints 

The following table summarizes the constraints for breakout functionality for Cisco UCS 6300 series fabric interconnects: 

Cisco UCS 6300 Series Fabric Interconnect Series  |  Breakout Configurable Ports  |  Ports without breakout functionality support   
---|---|---  
Cisco UCS 6332  |  1–12, 15–26  |  13–14, 27–32  |  **Note** | 

  * Auto-negotiate behavior is not supported on ports 27–32. 

  
---|---  
Cisco UCS 6332-16UP  |  17–34  |  1–16, 35–40  |  **Note** | 

  * Auto-negotiate behavior is not supported on ports 35–40 

  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

Up to four breakout ports are allowed if QoS jumbo frames are used. 

* * *  
  
---|---  
  
### Cisco UCS Chassis 

Cisco UCS Manager Release 3.1(1) and later releases provide support for Cisco UCS 5108 Blade Server Chassis 

Chassis Management provides details on managing the chassis through Cisco UCS Manager. 

#### Cisco UCS 5108 Blade Server Chassis 

The Cisco UCS 5108 Blade Server Chassis, is six rack units (6RU) high, can mount in an industry-standard 19-inch rack, and uses standard front-to-back cooling. A chassis can accommodate up to eight half-width, or four full-width Cisco UCS B-Series Blade Servers form factors within the same chassis. By incorporating unified fabric and fabric-extender technology, the Cisco Unified Computing System enables the chassis to: 

  * Have fewer physical components 

  * Require no independent management

  * Be more energy efficient than a traditional blade-server chassis 


The Cisco UCS 5108 Blade Server Chassis is supported with all generations of fabric interconnects. 

### Cisco UCS Mini Infrastructure 

The Cisco UCS Mini solution extends the Cisco UCS architecture into environments with requirements for smaller domains, including branch and remote offices, point-of-sale locations, and smaller IT environments. Cisco UCS Mini has three main infrastructure components: 

  * Cisco UCS 6324 fabric interconnect 

  * Cisco UCS blade server chassis 

  * Cisco UCS blade or rack mount servers 


Figure 18. Cisco UCS Mini   
![](/c/dam/en/us/td/i/300001-400000/300001-310000/305001-306000/305218.jpg)  


In the Cisco UCS Mini solution, the Cisco UCS 6324 fabric interconnect is collapsed into the IO Module form factor, and is inserted into the IOM slot of the blade server chassis. The Cisco UCS 6324 fabric interconnect has 24 10G ports available on it. Sixteen of these ports are server facing, two 10G ports are dedicated to each of the eight half width blade slots. The remaining eight ports are divided into groups of four 1/10G Enhanced Small Form-Factor Pluggable (SFP+) ports and one 40G Quad Small Form-factor Pluggable (QSFP) port, which is called the 'scalability port'. 

Cisco UCS Manager Release 3.1(1) introduces support for a second UCS 5108 chassis to an existing single-chassis Cisco UCS 6324 fabric interconnect setup. This extended chassis enables you to configure an additional 8 servers. Unlike the primary chassis, the extended chassis supports IOMs. Currently, it supports UCS-IOM-2204XP and UCS-IOM-2208XP IOMs. The extended chassis can only be connected through the scalability port on the FI-IOM. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

Currently, Cisco UCS Manager supports only one extended chassis for UCS Mini. 

* * *  
  
---|---  
  
### Cisco UCS Infrastructure Virtualization 

Cisco UCS is a single integrated system with switches, cables, adapters, and servers that are all tied together and managed by unified management software. One capability that enables this unification is the ability to virtualize every component of the system at every level. Switch port, cables, adapter, and servers can all be virtualized. Because of the virtualization capabilities at every component of the system, you have the unique capability to provide rapid provisioning of any service on any server on any blade through a system that is wired once. The following image illustrates these virtualization capabilities. 

Figure 19. Virtualization Capabilities of Cisco UCS   
![](/c/dam/en/us/td/i/300001-400000/300001-310000/305001-306000/305216.jpg)  


#### Switch Port Virtualization 

The physical interfaces provide physical connectivity for what are logical virtual interfaces on the fabric interconnects-virtual Fibre Channel interfaces (vFC) and virtual Ethernet interfaces (vEth). The logical connectivity to a server is provided through these virtual interfaces. 

####  Cable Virtualization 

The physical cables that connect to physical switch ports provide the infrastructure for logical and virtual cables. These virtual cables connect to virtual adapters on any given server in the system. 

####  Adapter Virtualization 

On the server, you have physical adapters, which provide physical infrastructure for virtual adapters. A virtual network interface card (vNIC) or virtual host bus adapter (vHBA) logically connects a host to a virtual interface on the fabric interconnect and allows the host to send and receive traffic through that interface. Each virtual interface in the fabric interconnect corresponds to a vNIC. 

An adapter that is installed on the server appears to the server as multiple adapters through standard PCIe virtualization. When the server scans the PCIe bus, the virtual adapters that are provisioned appear to be physically plugged into the PCIe bus. 

####  Server Virtualization 

Server virtualization provides you with the ability of stateless servers. As part of the physical infrastructure, you have physical servers. However, the configuration of a server is derived from the service profile to which it is associated. All service profiles are centrally managed and stored in a database on the fabric interconnect. A service profile defines all the settings of the server, for example, the number of adapters, virtual adapters, the identity of these adapters, the firmware of the adapters, and the firmware of the server. It contains all the settings of the server that you typically configure on a physical machine. Because the service profile is abstracted from the physical infrastructure, you can apply it to any physical server and the physical server will be configured according to the configuration defined in the service profile. Cisco UCS Manager Server Management Guide provides detailed information about managing service profiles. 

---

## Page 5: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_4_3/b_UCSM_CLI_Infrastructure_Management_Guide_chapter_011.html

# Equipment Policies

## Chassis/FEX Discovery Policy 

The chassis/FEX discovery policy determines how the system reacts when you add a new chassis or FEX. Cisco UCS Manager uses the settings in the chassis/FEX discovery policy to determine the minimum threshold for the number of links between the chassis or FEX and the fabric interconnect and whether to group links from the IOM to the fabric interconnect in a fabric port channel. 

In a Cisco UCS Mini (Cisco UCS 6324 Fabric Interconnect) setup, chassis discovery policy is supported only on the extended chassis. 

### Chassis Links

If you have a Cisco UCS domain with some of the chassis' wired with one link, some with two links, some with four links, and some with eight links, Cisco recommends configuring the chassis/FEX discovery policy for the minimum number links in the domain so that Cisco UCS Manager can discover all chassis. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/tip.gif)  
**Tip** | 

* * *

To establish the highest available chassis connectivity in a Cisco UCS domain where Fabric Interconnect is connected to different types of IO Modules supporting different max number of uplinks, select platform max value. Setting the platform max ensures that Cisco UCS Manager discovers the chassis including the connections and servers only when the maximum supported IOM uplinks are connected per IO Module. 

* * *  
  
---|---  
  
After the initial discovery of a chassis, if chassis/FEX discovery policy changes are done, acknowledge IO Modules rather than the entire Chassis to avoid disruption. The discovery policy changes can include increasing the number of links between Fabric Interconnect and IO Module, or changes to the Link Grouping preference. 

Make sure that you monitor for faults before and after the IO Module acknowledgement to ensure that the connectivity is restored before proceeding to the other IO Module for the chassis. 

Cisco UCS Manager cannot discover any chassis that is wired for fewer links than are configured in the chassis/FEX discovery policy. For example, if the chassis/FEX discovery policy is configured for four links, Cisco UCS Manager cannot discover any chassis that is wired for one link or two links. Re-acknowledgement of the chassis resolves this issue. 

The following table provides an overview of how the chassis/FEX discovery policy works in a multi-chassis Cisco UCS domain: 

Table 1. Chassis/FEX Discovery Policy and Chassis Links Number of Links Wired for the Chassis  | 1-Link Discovery Policy  | 2-Link Discovery Policy  | 4-Link Discovery Policy  | 8-Link Discovery Policy  | Platform-Max Discovery Policy   
---|---|---|---|---|---  
**1 link between IOM and fabric interconnects** |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 1 link.  |  Chassis connections and servers cannot be discovered by Cisco UCS Manager and are not added to the Cisco UCS domain.  |  Chassis connections and servers cannot be discovered by Cisco UCS Manager and are not added to the Cisco UCS domain.  |  Chassis connections and servers cannot be discovered by Cisco UCS Manager and are not added to the Cisco UCS domain.  |  Chassis connections and servers cannot be discovered by Cisco UCS Manager and are not added to the Cisco UCS domain.   
**2 links between IOM and fabric interconnects** |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 1 link.  After initial discovery, reacknowledge the chassis and Cisco UCS Manager recognizes and uses the additional links.  |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 2 link.  |  Chassis connections and servers cannot be discovered by Cisco UCS Manager and are not added to the Cisco UCS domain.  |  Chassis connections and servers cannot be discovered by Cisco UCS Manager and are not added to the Cisco UCS domain.  |  Chassis connections and servers cannot be discovered by Cisco UCS Manager and are not added to the Cisco UCS domain.   
**4 links between IOM and fabric interconnects** |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 1 link.  After initial discovery, reacknowledge the chassis and Cisco UCS Manager recognizes and uses the additional links.  |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 2 links.  After initial discovery, reacknowledge the chassis and Cisco UCS Manager recognizes and uses the additional links.  |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 4 link.  |  Chassis connections and servers cannot be discovered by Cisco UCS Manager and are not added to the Cisco UCS domain.  |  If the IOM has 4 links, the chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 4 links.  |  **Note** |  If the FEX status shows accessibility problem then reacknowledge the chassis after decommissioning/recommissioning FEX.  
---|---  
  
If the IOM has 8 links, the chassis is not fully discovered by Cisco UCS Manager.   
  
**8 links between IOM and fabric interconnects** |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 1 link.  After initial discovery, reacknowledge the chassis and Cisco UCS Manager recognizes and uses the additional links.  |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 2 links.  After initial discovery, reacknowledge the chassis and Cisco UCS Manager recognizes and uses the additional links.  |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 4 links.  After initial discovery, reacknowledge the chassis and Cisco UCS Manager recognizes and uses the additional links.  |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 8 links.  |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 8 links.   
  
### Link Grouping

For hardware configurations that support fabric port channels, link grouping determines whether all of the links from the IOM to the fabric interconnect are grouped in to a fabric port channel during chassis discovery. If the link grouping preference is set to Port Channel, all of the links from the IOM to the fabric interconnect are grouped in a fabric port channel. If set to None, links from the IOM are pinned to the fabric interconnect. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

For Cisco UCS X-Series Direct, Cisco UCS 6500 Series Fabric Interconnects, Cisco UCS 6400 Series Fabric Interconnect, the link grouping preference is always set to Port Channel. 

* * *  
  
---|---  
  
After a fabric port channel is created through Cisco UCS Manager, you can add or remove links by changing the link group preference and re-acknowledging the chassis, or by enabling or disabling the chassis from the port channel. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The link grouping preference only takes effect if both sides of the links between an IOM and IFM (IOM for Cisco UCS X-Series Servers) or FEX and the fabric interconnect support fabric port channels. If one side of the links does not support fabric port channels, this preference is ignored and the links are not grouped in a port channel. 

* * *  
  
---|---  
  
### Multicast Hardware Hash

In a port channel, by default, ingress multicast traffic on any port in the fabric interconnect (FI) selects a particular link between the IOM and the fabric interconnect to egress the traffic. To reduce potential issues with the bandwidth, and to provide effective load balancing of the ingress multicast traffic, hardware hashing is used for multicast traffic. When multicast hardware hashing is enabled, all links between the IOM and the fabric interconnect in a port channel can be used for multicast traffic. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCS X-Series Direct, Cisco UCS 6500 Series Fabric Interconnects, andCisco UCS 6400 Series Fabric Interconnect do not support multicast hardware hashing. 

* * *  
  
---|---  
  
  * Pinning
  * Port-Channeling
  * Configuring the Chassis/FEX Discovery Policy


### Pinning

Pinning in Cisco UCS is only relevant to uplink ports. If you configure Link Grouping Preference as None during chassis discovery, the IOM forwards traffic from a specific server to the fabric interconnect through its uplink ports by using static route pinning. 

The following table showcases how pinning is done between an IOM and the fabric interconnect based on the number of active fabric links between the IOM and the fabric interconnect. 

Table 2. Pinning on an IOM Number of Active Fabric Links  |  Server slot pinned to fabric link   
---|---  
1-Link  |  All the HIF ports are pinned to the active link   
2-Link  |  1,3,5,7 to link-1  2,4,6,8 to link-2   
4-Link  |  1,5 to link-1  2,6 to link-2  3,7 to link-3  4,8 to link-4   
8-Link (Applies only to 2208XP )  |  1 to link-1  2 to link-2  3 to link-3  4 to link-4  5 to link-5  6 to link-6  7 to link-7  8 to link-8   
  
Only 1,2,4 and 8 links are supported. 3,5,6, and 7 links are not valid configurations. 

### Port-Channeling

While pinning traffic from a specific server to an uplink port provides you with greater control over the unified fabric and ensures optimal utilization of uplink port bandwidth, it could also mean excessive traffic over certain circuits. This issue can be overcome by using port channeling. Port channeling groups all links between the IOM and the fabric interconnect into one port channel. The port channel uses a load balancing algorithm to decide the link over which to send traffic. This results in optimal traffic management. 

Cisco UCS supports port-channeling only through the Link Aggregation Control Protocol (LACP). For hardware configurations that support fabric port channels, link grouping determines whether all of the links from the IOM to the fabric interconnect are grouped into a fabric port channel during chassis discovery. If the Link Grouping Preference is set to Port Channel, all of the links from the IOM to the fabric interconnect are grouped in a fabric port channel. If this parameter is set to None, links from the IOM to the fabric interconnect are not grouped in a fabric port channel. 

Once a fabric port channel is created, links can be added or removed by changing the link group preference and reacknowledging the chassis, or by enabling or disabling the chassis from the port channel. 

### Configuring the Chassis/FEX Discovery Policy 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

In a setup with Cisco UCS 6400 Series Fabric Interconnects, the Link Grouping Preference value for Chassis/FEX Discovery Policy is not user configurable. The value is set to Port Channel. 

* * *  
  
---|---  
  
#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope org / |  Enters the root organization mode.  |  **Note** |  The chassis/FEX discovery policy can be accessed only from the root organization.   
---|---  
**Step 2** |  UCS-A /org #  scope chassis-disc-policy |  Enters organization chassis/FEX discovery policy mode.   
**Step 3** |  UCS-A /org/chassis-disc-policy #  set action ` `{1-link | 2-link | 4-link | 8-link | platform-max}  |  Specifies the minimum threshold for the number of links between the chassis or FEX and the fabric interconnect.   
**Step 4** |  (Optional) UCS-A /org/chassis-disc-policy # set descr ` ` description | (Optional)  Provides a description for the chassis/FEX discovery policy.  |  **Note** |  If your description includes spaces, special characters, or punctuation, you must begin and end your description with quotation marks. The quotation marks will not appear in the description field of any  show command output.   
---|---  
**Step 5** |  UCS-A /org/chassis-disc-policy #  set link-aggregation-pref ` `{none | port-channel}  |  Specifies whether the links from the IOMs or FEXes to the fabric interconnects are grouped in a port channel.  |  **Note** |  The link grouping preference only takes effect if both sides of the links between an IOM and IFM (IOM for Cisco UCS X-Series Servers) or FEX and the fabric interconnect support fabric port channels. If one side of the links does not support fabric port channels, this preference is ignored and the links are not grouped in a port channel.   
---|---  
**Note** |  For UCS manager to discover VIC 1455 and VIC 1457, Link Grouping Preference must be configured as Port Channel.   
---|---  
**Step 6** |  UCS-A /org/chassis-disc-policy # set multicast-hw-hash {disabled | enabled}  |  Specifies whether the all the links between the IOM and the fabric interconnect in a port channel can be used for multicast traffic. 

  * disabled —Only one link between the IOM and the fabric interconnect is used for multicast traffic 
  * enabled —All links between the IOM and the fabric interconnect can be used for multicast traffic 

  
**Step 7** |  (Optional) UCS-A /org/chassis-disc-policy #  set qualifier ` ` qualifier | (Optional)  Uses the specified server pool policy qualifications to associate this policy with a server pool.   
**Step 8** |  UCS-A /org/chassis-disc-policy #  commit-buffer |  Commits the transaction to the system configuration.   
  
#### Example

The following example scopes to the default chassis/FEX discovery policy, sets it to discover chassis with four links to a fabric interconnect, provides a description for the policy, specifies the server pool policy qualifications that will be used to qualify the chassis, and commits the transaction: 
    
    
    UCS-A# **scope org /**
    UCS-A /org # **scope chassis-disc-policy**
    UCS-A /org/chassis-disc-policy* # **set action 4-link**
    UCS-A /org/chassis-disc-policy* # **set descr "This is an example chassis/FEX discovery policy."**
    UCS-A /org/chassis-disc-policy* # **set qualifier ExampleQual**
    UCS-A /org/chassis-disc-policy* # **commit-buffer**
    UCS-A /org/chassis-disc-policy # 
    
    
    

The following example scopes to the default chassis/FEX discovery policy, sets it to discover chassis with eight links to a fabric interconnect, provides a description for the policy, sets the link grouping preference to port channel, specifies the server pool policy qualifications that will be used to qualify the chassis, and commits the transaction: 
    
    
    UCS-A# **scope org /**
    UCS-A /org # **scope chassis-disc-policy**
    UCS-A /org/chassis-disc-policy* # **set action 8-link**
    UCS-A /org/chassis-disc-policy* # **set descr "This is an example chassis/FEX discovery policy."**
    UCS-A /org/chassis-disc-policy* # **set link-aggregation-pref port-channel**
    UCS-A /org/chassis-disc-policy* # **set qualifier ExampleQual**
    UCS-A /org/chassis-disc-policy* # **commit-buffer**
    UCS-A /org/chassis-disc-policy # 
    
    
    

The following example scopes to the default chassis/FEX discovery policy, sets it to discover chassis with four links to a fabric interconnect, provides a description for the policy, sets the link grouping preference to port channel, enables multicast hardware hashing, specifies the server pool policy qualifications that will be used to qualify the chassis, and commits the transaction: 
    
    
    UCS-A# scope org /
    UCS-A /org # scope chassis-disc-policy
    UCS-A /org/chassis-disc-policy* # set action 4-link
    UCS-A /org/chassis-disc-policy* # set descr "This is an example chassis/FEX discovery
    policy."
    UCS-A /org/chassis-disc-policy* # set link-aggregation-pref port-channel
    UCS-A /org/chassis-disc-policy* # set multicast-hw-hash enabled
    UCS-A /org/chassis-disc-policy* # set qualifier ExampleQual
    UCS-A /org/chassis-disc-policy* # commit-buffer
    UCS-A /org/chassis-disc-policy #
    
    

#### What to do next

To customize fabric port channel connectivity for a specific chassis, configure the chassis connectivity policy. 

## Chassis Connectivity Policy 

The chassis connectivity policy determines the whether a specific chassis is included in a fabric port channel after chassis discovery. This policy is helpful for users who want to configure one or more chassis differently from what is specified in the global chassis discovery policy. The chassis connectivity policy also allows for different connectivity modes per fabric interconnect, further expanding the level of control offered with regards to chassis connectivity. 

By default, the chassis connectivity policy is set to global. This means that connectivity control is configured when the chassis is newly discovered, using the settings configured in the chassis discovery policy. Once the chassis is discovered, the chassis connectivity policy controls whether the connectivity control is set to none or port channel. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

The 40G backplane setting is not applicable for 22xx IOMs. 

* * *  
  
---|---  
  
The chassis connectivity policy is created by Cisco UCS Manager only when the hardware configuration supports fabric port channels. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

For the following fabric interconnects, the chassis connectivity policy is always Port Channel: 

  * Cisco UCS X-Series Direct (UCSX-S9108-100G) 
  * Cisco UCS 6500 Series Fabric Interconnect
  * Cisco UCS 6400 Series Fabric Interconnect


* * *  
  
---|---  
  
In a Cisco UCS Mini setup, the creation of a chassis connectivity policy is supported only on the extended chassis. 

  * Configuring a Chassis Connectivity Policy


### Configuring a Chassis Connectivity Policy

Changing the connectivity mode for a chassis might result in decreased VIF namespace. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Changing the connectivity mode for a chassis results in chassis re-acknowledgement. Traffic might be disrupted during this time. 

* * *  
  
---|---  
  
#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope org org-name |  Enters the organization mode for the specified organization. To enter the root organization mode, enter / as the org-name .   
**Step 2** |  UCS-A /org # scope chassis-conn-policy` `chassis-num` `[a | b}  |  Enters chassis connection policy organization mode for the specified chassis and fabric.  
**Step 3** |  UCS-A /org/chassis-conn-policy # set link-aggregation-pref` `{global | none | port-channel}  |  Specifies whether the links from the IOMs or FEXes to the fabric interconnects are grouped in a port channel. 

  * None—No links are grouped in a port channel 
  * Port Channel—All links from an IOM to a fabric interconnect are grouped in a port channel.  |  **Note** |  The following fabric interconnects support only Port Channel mode:
  * Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct) 
  * Cisco UCS 6536 Fabric Interconnect
  * Cisco UCS 6400 Series Fabric Interconnect  
---|---  
  * Global—The chassis inherits this configuration from the chassis discovery policy. This is the default value. 


  
**Step 4** |  UCS-A /org/chassis-conn-policy # commit-buffer |  Commits the transaction to the system configuration.  
  
#### Example

The following example shows how to change the fabric port channel connectivity for two chassis. Chassis 6, fabric A is changed to port channel and chassis 12, fabric B is changed to discrete links: 
    
    
    UCS-A# **scope org /**
    UCS-A /org # **scope chassis-conn-policy 6 a**
    UCS-A /org/chassis-conn-policy # **set link-aggregation-pref port-channel**
    UCS-A /org/chassis-conn-policy* # **up**
    UCS-A /org* # **scope chassis-conn-policy 12 b**
    UCS-A /org/chassis-conn-policy* # **set link-aggregation-pref none**
    UCS-A /org/chassis-conn-policy* # **commit-buffer**
    UCS-A /org/chassis-conn-policy #

## Rack Server Discovery Policy

The rack server discovery policy determines how the system reacts when you perform any of the following actions:

  * Add a new rack-mount server

  * Decommission/recommission a previously added or discovered rack-mount server


Cisco UCS Manager uses the settings in the rack server discovery policy to determine whether any data on the hard disks are scrubbed and whether server discovery occurs immediately or needs to wait for explicit user acknowledgement. 

Cisco UCS Manager cannot discover any rack-mount server that has not been correctly cabled and connected to the fabric interconnects. For information about how to integrate a supported Cisco UCS rack-mount server with Cisco UCS Manager, see the appropriate [rack-mount server integration guide](http://www.cisco.com/en/US/products/ps11736/products_installation_and_configuration_guides_list.html). 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

  * Cisco UCS VIC 1400, 14000, and 15000 series VIC adapters support 10/25/40/100G connectivity with Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct). 
  * Cisco UCS 1400, 14000, and 15000 series adapters support 10/25/40/100G with Cisco UCS 6536 fabric interconnects. 
  * Cisco UCS VIC 1400, 14000, and 15000 series adapters support 10/25G connectivity with Cisco UCS 6400 series fabric interconnects. 

When connecting to the Fabric Interconnects, use the same speed cables on all the adapter ports that are connected to same Fabric Interconnect. Cisco UCS VIC adapter ports connected to Cisco UCS Fabric Interconnect through a mix of 10G and 25G cables can result in UCS rack-mount server discovery failure and ports moving to suspended state. In this scenario, Cisco UCS Manager does not raise any faults. 

* * *  
  
---|---  
  
  * Configuring the Rack Server Discovery Policy


### Configuring the Rack Server Discovery Policy

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope org / |  Enters the root organization mode.  |  **Note** |  The rack server discovery policy can be accessed only from the root organization.   
---|---  
**Step 2** |  UCS-A /org #  scope rackserver-disc-policy |  Enters organization rack server discovery policy mode.   
**Step 3** |  UCS-A /org/rackserver-disc-policy #  set action ` `{immediate | user-acknowledged}  |  Specifies the way the system reacts when you perform any of the following actions:

  * Add a new rack server
  * Decommission/recommission a previously added or discovered rack server

  
**Step 4** |  (Optional) UCS-A /org/rackserver-disc-policy # set descr ` ` description | (Optional)  Provides a description for the rack server discovery policy.  |  **Note** |  If your description includes spaces, special characters, or punctuation, you must begin and end your description with quotation marks. The quotation marks will not appear in the description field of any  show command output.   
---|---  
**Step 5** |  UCS-A /org/rackserver-disc-policy #  set scrub-policy ` ` scrub-pol-name |  Specifies the scrub policy that should run on a newly discovered rack server or a decommissioned/recommissioned server.  
**Step 6** |  UCS-A /org/rackserver-disc-policy #  commit-buffer |  Commits the transaction to the system configuration.   
  
#### Example

The following example scopes to the default rack server discovery policy, sets it to immediately discover new rack servers or decommissioned/recommissioned server, provides a description for the policy, specifies a scrub policy called scrubpol1, and commits the transaction: 
    
    
    UCS-A# **scope org /**
    UCS-A /org # **scope rackserver-disc-policy**
    UCS-A /org/rackserver-disc-policy* # **set action immediate**
    UCS-A /org/rackserver-disc-policy* # **set descr "This is an example rackserver discovery policy."**
    UCS-A /org/rackserver-disc-policy* # **set scrub-policy scrubpol1**
    UCS-A /org/rackserver-disc-policy* # **commit-buffer**
    UCS-A /org/rackserver-disc-policy # 
    

##  Aging Time for the MAC Address Table

To efficiently switch packets between ports, the fabric interconnect maintains a MAC address table. It dynamically builds the MAC address table by using the MAC source address from the packets received and the associated port on which the packets were learned. The fabric interconnect uses an aging mechanism, defined by a configurable aging timer, to determine how long an entry remains in the MAC address table. If an address remains inactive for a specified number of seconds, it is removed from the MAC address table. 

You can configure the amount of time (age) that a MAC address entry (MAC address and associated port) remains in the MAC address table. 

  * Configuring the Aging Time for the MAC Address Table


###  Configuring the Aging Time for the MAC Address Table

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope eth-uplink |  Enters Ethernet uplink mode.   
**Step 2** |  UCS-A /eth-uplink #  set mac-aging {dd hh mm ss | mode-default | never}  |  Specifies the aging time for the MAC address table. Use the  mode-default keyword to set the aging time to a default value dependent on the configured Ethernet switching mode. Use the  never keyword to never remove MAC addresses from the table regardless of how long they have been idle.   
**Step 3** |  UCS-A /eth-uplink #  commit-buffer |  Commits the transaction to the system configuration.  
  
#### Example

The following example sets the aging time for the MAC address table to one day and 12 hours and commits the transaction:
    
    
    UCS-A# **scope eth-uplink**
    UCS-A /eth-uplink # **set mac-aging 01 12 00 00**
    UCS-A /eth-uplink* # **commit-buffer**
    UCS-A /eth-uplink # 
    

## HA Version Holder Replacement 

In releases earlier than Cisco UCS Manager Release 3.1(2), version holders are selected on a first come first serve basis. As chassis and rack servers are discovered, they can become version holders if they meet the requirements, and if the number of version holders has not reached the maximum permitted number. After a device is marked as a version holder, it persists as a version holder until it is decommissioned or removed. For example, if the connection status between the device and one or both fabric interconnects goes down, the device will not be removed as version holder. 

In some situations, the shared storage devices that are selected as high availability (HA) version holders become unreachable for an extended period of time. Cisco UCS Manager Release 3.1(2) introduces the ability to specify new preferred HA version holders corresponding to the devices that are functioning correctly. When you trigger a reelection of version holders, these new preferred HA devices are selected first. 

  * Guidelines for Preferred HA Version Holder Replacement
  * Creating a Preferred Version Holder
  * Deleting a Preferred Version Holder
  * Triggering the Reelection of Version Holders
  * Displaying Operational Version Holders


### Guidelines for Preferred HA Version Holder Replacement 

Consider the following guidelines when replacing HA version holders: 

  * Both fabric interconnects must be up for device reelection to be triggered. 

  * Cisco UCS Mini does not support preferred HA version holder replacement. 

  * A preferred version holder can be any device that is currently supported for shared storage. 

  * You can specify up to five preferred version holder devices. However, only three devices will be selected for active HA access. 

  * When you trigger shared storage device reelection, it removes all currently active devices and selects a new set of active devices. This set of devices may include previously active devices. Devices that are specified as preferred version holders are selected first as active devices. 

  * You can trigger reelection of shared storage devices at any time. However, the device will be selected as a version holder only in the following scenarios: 

  * When the connection path is both fabric interconnect A and B for UCS B Series blade chassis 

  * When the connection status is both fabric interconnect A and B for UCS C Series racks 

  * For a device to be selected as a version holder, the following requirements must be met: 
  * There must be less than three devices selected for active HA access. 

  * Chassis removal must not be in progress. 

  * A chassis that has been removed from the system must not be used as a version holder. 

  * The connection path must be both fabric interconnect A and B. 

  * Replacement of HA version holders can be done only through Cisco UCS Manager CLI. 


### Creating a Preferred Version Holder 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope system |  Enters system mode.   
**Step 2** |  UCS-A /system # create preferred-ha-device device-serial |  Creates the specified preferred HA device.   
**Step 3** |  UCS-A /system/ preferred-ha-device # commit-buffer |  Commits the transaction to the system configuration.   
**Step 4** |  UCS-A /system/ preferred-ha-device* # exit |  Enters system mode.   
**Step 5** |  UCS-A /system # show preferred-ha-devices |  Displays the list of preferred HA version holders and whether they are active or not.   
  
#### Example

This example shows how to create a preferred version holder: 
    
    
    UCS-A# **scope system**
    UCS-A /system # **create preferred-ha-device FCH1606V02F**
    UCS-A /system/ preferred-ha-device* # **commit-buffer**
    UCS-A /system/ preferred-ha-device # **exit**
    UCS-A /system # **show preferred-ha-devices**
    
    Preferred Version Holder:
        Chassis Serial Active
        -------------- ------
        FCH1606V02F    Yes
        FOX1636H6R3    Yes
        FOX1636H6R4    No
    
    
    

#### What to do next

Trigger a reelection of version holders. 

### Deleting a Preferred Version Holder 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope system |  Enters system mode.   
**Step 2** |  UCS-A /system # delete preferred-ha-device device-serial |  Deletes the specified preferred HA device.   
**Step 3** |  UCS-A /system/ preferred-ha-device* # commit-buffer |  Commits the transaction to the system configuration.   
**Step 4** |  UCS-A /system/ preferred-ha-device # exit |  Enters system mode.   
**Step 5** |  UCS-A /system # show preferred-ha-devices |  Displays the list of preferred HA version holders and whether they are active or not.   
  
#### Example

This example shows how to delete a preferred version holder: 
    
    
    UCS-A# **scope system**
    UCS-A /system # **delete preferred-ha-device FCH1606V02F**
    UCS-A /system/ preferred-ha-device* # **commit-buffer**
    UCS-A /system/ preferred-ha-device # **exit**
    UCS-A /system # **show preferred-ha-devices**
    
    Preferred Version Holder:
        Chassis Serial Active
        -------------- ------
        FOX1636H6R3    Yes
        FOX1636H6R4    No
    
    
     

### Triggering the Reelection of Version Holders 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope system |  Enters system mode.   
**Step 2** |  UCS-A /system # re-elect-ha-devices |  Triggers reelection of version holders for HA devices.   
  
#### Example

This example shows how to trigger the reelection of version holders: 
    
    
    UCS-A# **scope system**
    UCS-A /system # **re-elect-ha-devices**
    
    

### Displaying Operational Version Holders 

You can use this command to display all operational version holders, including preferred version holders. 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope system |  Enters system mode.   
**Step 2** |  UCS-A /system # show operational-ha-devices |  Displays the list of all currently operational HA version holders.   
  
#### Example

This example shows how to display all currently operational version holders: 
    
    
    UCS-A# **scope system**
    UCS-A /system # **show operational-ha-devices**
    
    Current Version Holder:
        Serial
        ------
        FOX1636H6R5
    
    
    

---

## Page 6: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_4_3/b_UCSM_CLI_Infrastructure_Management_Guide_4_1_chapter_0100.html

# Chassis Management

## Chassis Management in Cisco UCS Manager CLI

You can manage and monitor all chassis in a Cisco UCS domain through Cisco UCS Manager CLI. 

  * Cisco UCS X9508 Series Chassis
  * The Cisco UCS S3260 Chassis
  * Cisco UCS 5108 Blade Server Chassis
  * Extended Chassis for UCS Mini


### Cisco UCS X9508 Series Chassis

The Cisco UCS X-Series Modular System begins with the Cisco UCS X9508 Chassis. With a midplane-free design, I/O connectivity for the X9508 chassis is accomplished with frontloading, vertically oriented compute nodes intersecting with horizontally oriented I/O connectivity modules in the rear of the chassis. A unified Ethernet fabric is supplied with the Cisco UCS 9108 Intelligent Fabric Modules. 

The system is primed with Cisco UCS 9108 Intelligent Fabric Modules that provide a robust Ethernet fabric and is set to accommodate emerging protocols with the innovative Cisco UCS X-Fabric Technology, ensuring easy upgrades with new modules as they become available. 

The major feature of the chasssi include:

  * 7-Rack-Unit (7RU) chassis has 8x front-facing flexible slots. These can house a combination of compute nodes and a pool of future I/O resources that may include GPU accelerators, disk storage, and nonvolatile memory. 

  * 2x Cisco UCS 9108 Intelligent Fabric Modules (IFMs) at the top of the chassis that connect the chassis to upstream Cisco UCS 6400 Series Fabric Interconnects. Each IFM features. 

  * Up to 100 Gbps of unified fabric connectivity per compute node

  * 8x 25-Gbps SFP28 uplink ports. The unified fabric carries management traffic to the Cisco Intersight cloud-operations platform, Fibre Channel over Ethernet (FCoE) traffic, and production Ethernet traffic to the fabric interconnects. 

  * At the bottom are slots ready to house future I/O modules that can flexibly connect the compute modules with I/O devices. We call this connectivity Cisco UCS X-Fabric technology because “X” is a variable that can evolve with new technology developments. 

  * Six 2800W Power Supply Units (PSUs) provide 54V power to the chassis with N, N+1, and N+N redundancy. A higher voltage allows efficient power delivery with less copper and reduced power loss. 

  * Efficient, 4x100mm, dual counter-rotating fans deliver industry-leading airflow and power efficiency. Optimized thermal algorithms enable different cooling modes to best support the network environment. Cooling is modular so that future enhancements can potentially handle open- or closed-loop liquid cooling to support even higher-power processors. 


This Cisco UCS X9508 Chassis supports Cisco UCS X-Series Direct, Cisco UCS 6536, UCS 6454, UCS 64108 fabric interconnects.

The Cisco UCS X-Series Direct, identified as UCSX-S9108-100G, enhances the Cisco UCS X-Series Modular System by incorporating a pair of internal Cisco UCS Fabric Interconnects S9108 100G. This integration creates a self-contained system that connects up to eight server nodes with unified fabric, IP, and Fibre Channel connectivity, all managed by Cisco UCS Manager. The X-Series Direct is compatible with all components of the X-Series Modular System. 

For more information, see [Cisco UCS X9508 Chassis Data Sheet](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-x-series-modular-system/datasheet-c78-2472574.html). 

### The Cisco UCS S3260 Chassis

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


### Cisco UCS 5108 Blade Server Chassis 

The Cisco UCS 5100 Series Blade Server Chassis is logically part of the fabric interconnects, thus creating a single, coherent management domain and decreasing management complexity. In the management domain, server management is handled by the fabric interconnect, while I/O and network management is extended to every chassis and blade server. Basing the I/O infrastructure on a unified fabric allows the Cisco Unified Computing System to have a simple and streamlined chassis yet offer a comprehensive set of I/O options. This results in the chassis having only five basic components: 

  * The physical chassis with passive midplane and active environmental monitoring circuitry 

  * Four power-supply bays with power entry in the rear, and redundant-capable, hot-swappable power supply units accessible from the front panel 

  * Eight hot-swappable fan trays, each with two fans 

  * Two fabric extender slots accessible from the back panel 

  * Eight blade server slots accessible from the front panel 


The blade server chassis has flexible partitioning with removable dividers to handle two blade server form factors: 

  * Half-width blade servers have access to power and two 10GBASE-KR connections, one to each fabric extender slot. 

  * Full-width blade servers connect to power and two connections to each fabric extender. 


### Extended Chassis for UCS Mini 

Cisco UCS Manager Release 3.1(1) introduces support for an extended UCS 5108 chassis to an existing single-chassis Cisco UCS 6324 fabric interconnect setup. This extended chassis enables you to configure an additional 8 servers. Unlike the primary chassis, the extended chassis supports IOMs. Currently, it supports UCS-IOM-2204XP and UCS-IOM-2208XP IOMs. The extended chassis can only be connected through the scalability port on the FI-IOM. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

Currently, Cisco UCS Manager supports only one extended chassis for UCS Mini. 

* * *  
  
---|---  
To use a extended chassis, do the following: 

  * Connect the second Cisco UCS 5108 chassis to the existing single-chassis Cisco UCS 6324 Series fabric interconnect configuration through the scalability port. 

  * Configure the chassis discovery policy. 

  * Configure the server ports and wait for the second chassis to be discovered. 


## Guidelines for Removing and Decommissioning Chassis 

Consider the following guidelines when deciding whether to remove or decommission a chassis using Cisco UCS Manager: 

### Decommissioning a Chassis 

Decommissioning is performed when a chassis is physically present and connected but you want to temporarily remove it from the Cisco UCS Manager configuration. Because it is expected that a decommissioned chassis will be eventually recommissioned, a portion of the chassis' information is retained by Cisco UCS Manager for future use. 

### Removing a Chassis 

Removing is performed when you physically remove a chassis from the system. Once the physical removal of the chassis is completed, the configuration for that chassis can be removed in Cisco UCS Manager. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

You cannot remove a chassis from Cisco UCS Manager if it is physically present and connected. 

* * *  
  
---|---  
  
If you need to add a removed chassis back to the configuration, it must be reconnected and then rediscovered. During rediscovery Cisco UCS Manager will assign the chassis a new ID that may be different from ID that it held before. 

## Acknowledging a Chassis

Acknowledging the chassis ensures that Cisco UCS Manager is aware of the change in the number of links and that traffics flows along all available links. 

After you enable or disable a port on a fabric interconnect, wait for at least 1 minute before you re-acknowledge the chassis. If you re-acknowledge the chassis too soon, the pinning of server traffic from the chassis might not get updated with the changes to the port that you enabled or disabled. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  acknowledge chassis  ` ` chassis-num |  Acknowledges the specified chassis.   
**Step 2** |  UCS-A#  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example acknowledges chassis 2 and commits the transaction: 
    
    
    UCS-A# **acknowledge chassis 2**
    UCS-A* # **commit-buffer**
    UCS-A # 
    

## Decommissioning a Chassis

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  decommission chassis ` ` chassis-num |  Decommissions the specified chassis.  
**Step 2** |  UCS-A#  commit-buffer |  Commits the transaction to the system configuration.  
  
The decommission may take several minutes to complete.

### Example

The following example decommissions chassis 2 and commits the transaction:
    
    
    UCS-A# **decommission chassis 2**
    UCS-A* # **commit-buffer**
    UCS-A # **show chassis**
    
    Chassis:
        Chassis    Overall Status           Admin State
        ---------- ------------------------ -----------
                 1 Operable                 Acknowledged
                 2 Accessibility Problem    Decommission
    UCS-A # 
    

## Removing a Chassis

### Before you begin

Physically remove the chassis before performing the following procedure. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  remove chassis ` ` chassis-num |  Removes the specified chassis.  
**Step 2** |  UCS-A#  commit-buffer |  Commits the transaction to the system configuration.  
  
The removal may take several minutes to complete.

### Example

The following example removes chassis 2 and commits the transaction:
    
    
    UCS-A# **remove chassis 2**
    UCS-A* # **commit-buffer**
    UCS-A # 
    

## Recommissioning a Chassis 

This procedure returns the chassis to the configuration and applies the chassis discovery policy to the chassis. After this procedure, you can access the chassis and any servers in it. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

This procedure is not applicable for Cisco UCS S3260 Chassis. 

* * *  
  
---|---  
  
### Before you begin

Collect the following information about the chassis to be recommissioned by using the show chassis decommissioned or show chassis inventory commands: 

  * Vendor name 

  * Model name 

  * Serial number 


### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  recommission chassis ` ` vendor-name model-name serial-num |  Recommissions the specified chassis.   
**Step 2** |  UCS-A#  commit-buffer |  Commits the transaction to the system configuration.  |  **Note** |  After recommissioning a chassis and committing the transaction, if you immediately run the show chassis command, you may not see any change in the Admin State of the chassis. It may take a while before the state of the chassis changes after it is recommissioned.   
---|---  
  
### Example

The following example recommissions a Cisco UCS 5108 chassis and commits the transaction: 
    
    
    UCS-A# **show chassis**
    
    Chassis:
        Chassis    Overall Status           Admin State
        ---------- ------------------------ -----------
                 1 Accessibility Problem    Decommission
    
    UCS-A# **recommission chassis "Cisco Systems Inc" "N20-C6508" FOX1252GNNN**
    UCS-A* # **commit-buffer**
    UCS-A # 
    

## Renumbering a Chassis 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

You cannot renumber a blade server through Cisco UCS Manager. The ID assigned to a blade server is determined by its physical slot in the chassis. To renumber a blade server, you must physically move the server to a different slot in the chassis. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

This procedure is not applicable for Cisco UCS S3260 Chassis. 

* * *  
  
---|---  
  
### Before you begin

If you are swapping IDs between chassis, you must first decommission both chassis, then wait for the chassis decommission FSM to complete before proceeding with the renumbering steps. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  show chassis inventory |  Displays information about your chassis.   
**Step 2** |  Verify that the chassis inventory does not include the following:  | 

  * The chassis you want to renumber 
  * A chassis with the number you want to use 

If either of these chassis are listed in the chassis inventory, decommission those chassis. You must wait until the decommission FSM is complete and the chassis are not listed in the chassis inventory before continuing. This might take several minutes.  To see which chassis have been decommissioned, issue the show chassis decommissioned command.   
**Step 3** |  UCS-A#  recommission chassis ` ` vendor-name model-name serial-num [chassis-num]  |  Recommissions and renumbers the specified chassis.   
**Step 4** |  UCS-A#  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example decommissions two Cisco UCS chassis (chassis 8 and 9), switches their IDs, and commits the transaction: 
    
    
    UCS-A# **show chassis inventory**
    
        Chassis    PID       Vendor         Serial (SN) HW Revision
        ------- --------- ---------------   ----------- -------------
              1 N20-C6508 Cisco Systems Inc FOX1252GAAA 0 
              2 N20-C6508 Cisco Systems Inc FOX1252GBBB 0 
              3 N20-C6508 Cisco Systems Inc FOX1252GCCC 0 
              4 N20-C6508 Cisco Systems Inc FOX1252GDDD 0 
              5 N20-C6508 Cisco Systems Inc FOX1252GEEE 0 
              6 N20-C6508 Cisco Systems Inc FOX1252GFFF 0
              7 N20-C6508 Cisco Systems Inc FOX1252GGGG 0
              8 N20-C6508 Cisco Systems Inc FOX1252GHHH 0 
              9 N20-C6508 Cisco Systems Inc FOX1252GIII 0 
             10 N20-C6508 Cisco Systems Inc FOX1252GJJJ 0 
             11 N20-C6508 Cisco Systems Inc FOX1252GKKK 0 
             12 N20-C6508 Cisco Systems Inc FOX1252GLLL 0 
             13 N20-C6508 Cisco Systems Inc FOX1252GMMM 0 
             14 N20-C6508 Cisco Systems Inc FOX1252GNNN 0 
    
    UCS-A# **decommission chassis 8**
    UCS-A*# **commit-buffer**
    UCS-A# **decommission chassis 9**
    UCS-A*# **commit-buffer**
    UCS-A# **show chassis inventory**
    
        Chassis    PID       Vendor         Serial (SN) HW Revision
        ------- --------- ---------------   ----------- -------------
              1 N20-C6508 Cisco Systems Inc FOX1252GAAA 0 
              2 N20-C6508 Cisco Systems Inc FOX1252GBBB 0 
              3 N20-C6508 Cisco Systems Inc FOX1252GCCC 0 
              4 N20-C6508 Cisco Systems Inc FOX1252GDDD 0 
              5 N20-C6508 Cisco Systems Inc FOX1252GEEE 0 
              6 N20-C6508 Cisco Systems Inc FOX1252GFFF 0
              7 N20-C6508 Cisco Systems Inc FOX1252GGGG 0
             10 N20-C6508 Cisco Systems Inc FOX1252GJJJ 0 
             11 N20-C6508 Cisco Systems Inc FOX1252GKKK 0 
             12 N20-C6508 Cisco Systems Inc FOX1252GLLL 0 
             13 N20-C6508 Cisco Systems Inc FOX1252GMMM 0 
             14 N20-C6508 Cisco Systems Inc FOX1252GNNN 0 
    
    UCS-A# **show chassis decommissioned**
    
        Chassis    PID       Vendor         Serial (SN) HW Revision
        ------- --------- ---------------   ----------- -------------
              8 N20-C6508 Cisco Systems Inc FOX1252GHHH 0
              9 N20-C6508 Cisco Systems Inc FOX1252GIII 0 
    
    UCS-A# **recommission chassis "Cisco Systems Inc" "N20-C6508" FOX1252GHHH 9**
    UCS-A* # **commit-buffer**
    UCS-A# **recommission chassis "Cisco Systems Inc" "N20-C6508" FOX1252GIII 8**
    UCS-A* # **commit-buffer**
    UCS-A # **show chassis inventory**
    
        Chassis    PID       Vendor         Serial (SN) HW Revision
        ------- --------- ---------------   ----------- -------------
              1 N20-C6508 Cisco Systems Inc FOX1252GAAA 0 
              2 N20-C6508 Cisco Systems Inc FOX1252GBBB 0 
              3 N20-C6508 Cisco Systems Inc FOX1252GCCC 0 
              4 N20-C6508 Cisco Systems Inc FOX1252GDDD 0 
              5 N20-C6508 Cisco Systems Inc FOX1252GEEE 0 
              6 N20-C6508 Cisco Systems Inc FOX1252GFFF 0
              7 N20-C6508 Cisco Systems Inc FOX1252GGGG 0
              8 N20-C6508 Cisco Systems Inc FOX1252GIII 0 
              9 N20-C6508 Cisco Systems Inc FOX1252GHHH 0 
             10 N20-C6508 Cisco Systems Inc FOX1252GJJJ 0 
             11 N20-C6508 Cisco Systems Inc FOX1252GKKK 0 
             12 N20-C6508 Cisco Systems Inc FOX1252GLLL 0 
             13 N20-C6508 Cisco Systems Inc FOX1252GMMM 0 
             14 N20-C6508 Cisco Systems Inc FOX1252GNNN 0 
    

## Turning On the Locator LED for a Chassis

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope chassis ` ` chassis-num |  Enters chassis mode for the specified chassis.  
**Step 2** |  UCS-A /chassis #  enable locator-led ` ` |  Turns on the chassis locator LED.  
**Step 3** |  UCS-A /chassis #  commit-buffer |  Commits the transaction to the system configuration.  
  
### Example

The following example turns on the locator LED for chassis 2 and commits the transaction:
    
    
    UCS-A# scope chassis 2
    UCS-A /chassis # enable locator-led
    UCS-A /chassis* # commit-buffer
    UCS-A /chassis # 
    

## Turning Off the Locator LED for a Chassis

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope chassis ` ` chassis-num |  Enters chassis mode for the specified chassis.  
**Step 2** |  UCS-A /chassis #  disable locator-led ` ` |  Turns off the chassis locator LED.  
**Step 3** |  UCS-A /chassis #  commit-buffer |  Commits the transaction to the system configuration.  
  
### Example

The following example turns off the locator LED for chassis 2 and commits the transaction:
    
    
    UCS-A# scope chassis 2
    UCS-A /chassis # disable locator-led
    UCS-A /chassis* # commit-buffer
    UCS-A /chassis # 
    

---

## Page 7: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_4_3/b_UCSM_CLI_Infrastructure_Management_Guide_chapter_0101.html

# I/O Management

## I/O Module Management in Cisco UCS Manager CLI

You can manage and monitor all I/O modules in a Cisco UCS domain through Cisco UCS Manager CLI. 

Cisco UCS Manager Release 4.1(1) extends support for the Cisco 2408 IO module to the Cisco UCS 64108 Fabric Interconnect. 

Cisco UCS Manager Release 4.0(4c) introduces the Cisco 2408 IO module. This IO Module has 32 25-Gigabit backplane ports and 4 100-Gigabit uplink ports, and is supported only on the Cisco UCS 6454 Fabric Interconnect. 

Cisco UCS Manager Release 4.0(4a) introduces the Cisco UCS-IOM-2304V2 I/O module which is based on Cisco UCS-IOM-2304 I/O module. 

Cisco UCS Manager Release 3.1(1) introduces the Cisco UCS-IOM-2304 I/O module with 40 GbE connectivity to the Cisco UCS 6300 Series Fabric Interconnect. The Cisco UCS Manager Getting Started Guide provides more information about this functionality. 

## Acknowledging an IO Module 

Cisco UCS Manager Release 2.2(4) introduces the ability to acknowledge a specific IO module in a chassis. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

  * After adding or removing physical links between Fabric Interconnect and IO Module, an acknowledgement of the IO Module is required to properly configure the connection. 
  * The ability to re-acknowledge each IO Module individually allows to rebuild the network connectivity between a single IO Module and its parent Fabric Interconnect without disrupting production traffic in the other fabric interconnect. 


* * *  
  
---|---  
  
### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope chassis chassis-num |  Enters chassis mode for the specified chassis.   
**Step 2** |  UCS-A /chassis # acknowledge iom {1 | 2}  |  Acknowledges the specified IOM in the chassis.   
**Step 3** |  UCS-A /chassis* # commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example acknowledges IO Module 1 and commits the transaction: 
    
    
    UCS-A# **scope chassis 1**
    UCS-A /chassis # **acknowledge iom 1**
    UCS-A /chassis* # **commit-buffer**
    UCS-A /chassis #
    
    

## Resetting the I/O Module

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope chassis ` ` chassis-num |  Enters chassis mode for the specified chassis.  
**Step 2** |  UCS-A /chassis #  scope iom ` `{a b}  |  Enters chassis IOM mode for the specified IOM.   
**Step 3** |  UCS-A /chassis/iom #  reset |  Resets the IOM.  
**Step 4** |  UCS-A /chassis/iom #  commit-buffer |  Commits the transaction to the system configuration.  
  
### Example

The following example resets the IOM on fabric A and commits the transaction:
    
    
    UCS-A# scope chassis 1
    UCS-A /chassis # scope iom a
    UCS-A /chassis/iom # reset
    UCS-A /chassis/iom* # commit-buffer
    UCS-A /chassis/iom #
    

## Resetting an I/O Module from a Peer I/O Module 

Sometimes, I/O module upgrades can result in failures or I/O modules can become unreachable from Cisco UCS Manager due to memory leaks. You can now reboot an I/O module that is unreachable through its peer I/O module. 

Resetting the I/O module restores the I/O module to factory default settings, deletes all cache files and temporary files, but retains the size-limited OBFL file. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope chassis chassis-num |  Enters chassis mode for the specified chassis.   
**Step 2** |  UCS-A /chassis # scope iom {a b}  |  Enters chassis IOM mode for the specified IOM.  Specify the peer IOM of the IOM that you want to reset.   
**Step 3** |  UCS-A /chassis/iom # reset-peer |  Resets the peer IOM of the specified IOM.   
**Step 4** |  UCS-A /chassis/iom* # commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

This example shows how to reset IOM b from IOM a: 
    
    
    UCS-A# **scope chassis 1**
    UCS-A /chassis # **scope iom a**
    UCS-A /chassis/iom # **reset-peer**
    UCS-A /chassis/iom* # **commit-buffer**

---

## Page 8: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_4_3/b_UCSM_CLI_Infrastructure_Management_Guide_chapter_0110.html

# SIOC Management

## SIOC Management in Cisco UCS Manager

You can manage and monitor all System Input/Output Controllers (SIOC) in a Cisco UCS domain through Cisco UCS Manager. 

  * SIOC Removal or Replacement


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


## Acknowledging an SIOC 

Cisco UCS Manager has the ability to acknowledge a specific SIOC in a chassis. Perform the following procedure when you replace an SIOC in a chassis. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

This operation rebuilds the network connectivity between the SIOC and the fabric interconnects to which it is connected. The server corresponding to this SIOC becomes unreachable, and traffic is disrupted. 

* * *  
  
---|---  
  
### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope chassis chassis-num |  Enters chassis mode for the specified chassis.   
**Step 2** |  UCS-A /chassis # acknowledge sioc {1 | 2}  |  Acknowledges the specified SIOC in the chassis.   
**Step 3** |  UCS-A /chassis* # commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example acknowledges SIOC 1 and commits the transaction: 
    
    
    UCS-A# **scope chassis 3**
    UCS-A /chassis # **acknowledge sioc 1**
    UCS-A /chassis* # **commit-buffer**
    UCS-A /chassis #
    
    

## Migrating to SIOC with PCIe Support

### Before you begin

Ensure that the Cisco UCS Manager is at release 4.0(1a) or higher. 

### Procedure

* * *

**Step 1** |  Update the chassis and server firmware to 4.0(1) release.   
---|---  
**Step 2** |  Decommission the chassis.  
**Step 3** |  Shut down and remove power from the entire chassis. You must disconnect all power cords to completely remove power.  
**Step 4** |  Disconnect the cables connecting the SIOC to the system.  
**Step 5** |  Remove the SIOC from the system.  
**Step 6** |  Connect the new SIOC to the system.  
**Step 7** |  Connect the cables to the SIOC.  
**Step 8** |  Connect power cords and then power on the system.  
**Step 9** |  Acknowledge the new SIOC.  
  
* * *

## Resetting the CMC 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope chassis chassis-num |  Enters chassis mode for the specified chassis.   
**Step 2** |  UCS-A /chassis # scope sioc {1 | 2}  |  Enters the specified SIOC in the chassis.   
**Step 3** |  UCS-A /chassis/sioc # scope cmc |  Enters the CMC of the selected SIOC slot.   
**Step 4** |  UCS-A /chassis/sioc/cmc # reset |  Resets the CMC.   
**Step 5** |  UCS-A /chassis/sioc/cmc* # commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example resets the CMC on SIOC 1 and commits the transaction: 
    
    
    UCS-A# **scope chassis 1**
    UCS-A /chassis # **scope sioc 1**
    UCS-A /chassis/sioc # **scope cmc**
    UCS-A /chassis/sioc/cmc # **reset**
    UCS-A /chassis/sioc/cmc* # **commit-buffer**
    
    
    

## CMC Secure Boot 

With Chassis Management Controller (CMC) secure boot, only Cisco-signed firmware images can be installed and run on the CMC. When the CMC is updated, the image is certified before the firmware is flashed. If certification fails, the firmware is not flashed. This prevents unauthorized access to the CMC firmware. 

  * Guidelines and Limitations for CMC Secure Boot
  * Enabling CMC Secure Boot


### Guidelines and Limitations for CMC Secure Boot 

  * CMC secure boot is supported only on the Cisco UCS S3260 chassis. 

  * When chassis association is in progress, enabling secure boot on one of the SIOCs will result in a failed operation. 

  * After CMC secure boot is enabled, it cannot be disabled. 

  * CMC secure boot is specific to the SIOC on which it is enabled. If you replace the SIOC on which CMC secure boot is enabled, the Secure boot operational state field will now display the secure boot status of the new SIOC. 

  * After CMC secure boot is enabled on a chassis, you cannot move the chassis back to  non-cluster setup and downgrade the firmware to a CMC firmware image earlier than Cisco IMC Release 2.0(13). 

  * The Secure boot operational state field shows the secure boot status. This can be one of the following: 

  * Disabled—When CMC secure boot is not enabled. This is the default state. 

  * Enabling—When CMC secure boot is being enabled. 

  * Enabled—When CMC secure boot is enabled. 

  * Beginning with 4.0(1), Secure boot operational state is Enabled by default and is not user configurable. The option is grayed out. 


### Enabling CMC Secure Boot 

Cisco UCS Manager Release 3.1(2) introduces the ability to enable Chassis Management Controller (CMC) secure boot so that only Cisco-signed firmware images can be installed and run on the CMC. 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope chassis chassis-num |  Enters chassis mode for the specified chassis.   
**Step 2** |  UCS-A /chassis # scope sioc {1 | 2}  |  Enters the specified SIOC in the chassis.   
**Step 3** |  UCS-A /chassis/sioc # scope cmc |  Enters the CMC of the selected SIOC slot.   
**Step 4** |  UCS-A /chassis/sioc/cmc # enable secure-boot |  Enables CMC secure boot.  If you run this command when the secure boot state is enabled, Cisco UCS Manager will display an error message and the operation will fail.  |  **Note** |  This is an irreversible operation. You cannot disable CMC secure boot.   
---|---  
**Step 5** |  UCS-A /chassis/sioc/cmc* # commit-buffer |  Commits the transaction to the system configuration.   
  
#### Example

The following example enables CMC secure boot on SIOC 1 and commits the transaction: 
    
    
    UCS-A# **scope chassis 1**
    UCS-A /chassis # **scope sioc 1**
    UCS-A /chassis/sioc # **scope cmc**
    UCS-A /chassis/sioc/cmc # **enable secure-boot**
    Warning: This is an irreversible operation. 
    Do you want to proceed? [Y/N] **Y**
    UCS-A /chassis/sioc/cmc* # **commit-buffer**
    
    
    

---

## Page 9: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_4_3/b_UCSM_CLI_Infrastructure_Management_Guide_chapter_0111.html

# Power Management

## Power Capping in Cisco UCS

You can control the maximum power consumption on a server through power capping, as well as manage the power allocation in the Cisco UCS Manager for blade servers, rack servers, UCS Mini, and mixed UCS domains. 

Cisco UCS Manager supports power capping on the following: 

  * Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct) 

  * UCS 6500 Series Fabric Interconnects

  * UCS 6400 Series Fabric Interconnects

  * UCS 6300 Series Fabric Interconnects 

  * UCS 6324 Series Fabric Interconnects (Cisco UCS Mini)


You can use Policy Driven Chassis Group Power Cap, or Manual Blade Level Power Cap methods to allocate power that applies to all of the servers in a chassis. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCSX-9508 Chassis supports Policy Driven Chassis Group Cap.  When you choose to select Policy Driven Chassis Group Cap, Cisco UCS Manager calculates the power allotment for Cisco UCSX-9508 Chassis and when you choose to select Manual Blade Level Power Cap, Chassis Management Controller (CMC) calculates the power allotment for Cisco UCSX-9508 Chassis. 

* * *  
  
---|---  
  
Cisco UCS Manager provides the following power management policies to help you allocate power to your servers: 

Power Management Policies  |  Description   
---|---  
Power Policy |  Specifies the redundancy for power supplies in all chassis in a Cisco UCS domain.   
Power Control Policies |  Specifies the priority to calculate the initial power allocation for each blade in a chassis.   
Power Save Policy |  Globally manages the chassis to maximize energy efficiency or availability.  
Cisco UCSX-9508 Chassis Power Extended Policy |  Manages the chassis to maximize energy efficiency or availability.  Power Extended Policy is effective only when we have PSU Redundant Policy Mode. For example, the total power available can be extended when we have N+1, N+2 and Grid to PSU Redundancy modes.   
Cisco UCSX-9508 Chassis Fan Control Policy |  Manages you to control the fan speed to bring down server power consumption and noise levels.  
Global Power Allocation |  Specifies the Policy Driven Chassis Group Power Cap or the Manual Blade Level Power Cap to apply to all servers in a chassis.   
Global Power Profiling  |  Specifies how the power cap values of the servers are calculated. If it is enabled, the servers will be profiled during discovery through benchmarking. This policy applies when the Global Power Allocation Policy is set to Policy Driven Chassis Group Cap.   
  
Power Policy Configuration

## Power Policy for Cisco UCS Servers 

The power policy is global and is inherited by all of the chassis' managed by the Cisco UCS Manager instance. You can add the power policy to a service profile to specify the redundancy for power supplies in all chassis' in the Cisco UCS domain. This policy is also known as the PSU policy. 

For more information about power supply redundancy, see Cisco UCS 5108 Server Chassis Hardware Installation Guide. 

## Configuring the Power Policy 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope org ` ` org-name |  Enters organization mode for the specified organization. To enter the root organization mode, type  / as the  org-name .   
**Step 2** |  UCS-A /org #  scope psu-policy |  Enters PSU policy mode.   
**Step 3** |  UCS-A /org/psu-policy #  set redundancy {grid | n-plus-1|n-plus-2 |non-redund}  |  Specifies one of the following redundancy types: 

  * grid —Two power sources are turned on, or the chassis requires greater than N+1 redundancy. If one source fails (which causes a loss of power to one or two PSUs), the surviving PSUs on the other power circuit continue to provide power to the chassis. 
  * n-plus-1 —The total number of PSUs to satisfy non-redundancy, plus one additional PSU for redundancy, are turned on and equally share the power load for the chassis. If any additional PSUs are installed, Cisco UCS Manager sets them to a "turned-off" state. 
  * non-redund —All installed power supplies (PSUs) are turned on and the load is evenly balanced. Only smaller configurations (requiring less than 2500W) can be powered by a single PSU. 
  * n-plus-2 —The total number of PSUs to satisfy non-redundancy, plus two additional PSU for redundancy, are turned on and equally share the power load for the chassis. If any additional PSUs are installed, Cisco UCS Manager sets them to a "turned-off" state.  |  **Note** |  n-plus-2 redundancy mode is supported only for Cisco UCS X9508 chassis. For all other chassis, Cisco UCS Manager treats n-plus-2 mode as n-plus-1 mode only.   
---|---  


For more information about power redundancy, see the Cisco UCS 5108 Server Chassis Installation Guide.   
  
**Step 4** |  UCS-A /org/psu-policy #  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example configures the power policy to use grid redundancy and commits the transaction: 
    
    
    UCS-A# **scope org /**
    UCS-A /org # **scope psu-policy**
    UCS-A /org/psu-policy # **set redundancy grid**			 
    UCS-A /org/psu-policy* # **commit-buffer**
    UCS-A /org/psu-policy #
    

The following example configures the power policy to use n-plus-2 redundancy for Cisco UCS X9508 chassis and shows the details: 
    
    
    UCS-A# **scope org**
    UCS-A /org # **scope psu-policy**
    UCS-A /org/psu-policy # **set redundancy n-plus-2**
    UCS-A /org/psu-policy # **commit-buffer**

##  Power Supply for Redundancy Method 

**PSU Redundancy** |  **Max Power @ 240 V**  
---|---  
Grid |  5000 Watts  
N+1 |  7500 Watts  
Non-Redundant |  8280 Watts  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

This table is valid if there are four PSUs installed in the chassis.

* * *  
  
---|---  
  
Policy Driven Power Capping

## Policy Driven Chassis Group Power Capping 

When you select the Policy Driven Chassis Group Power Cap in the Global Cap Policy, Cisco UCS can maintain the over-subscription of servers without risking power failures. You can achieve over-subscription through a two-tier process. For example, at the chassis level, Cisco UCS divides the amount of power available among members of the power group, and at the blade level, the amount of power allotted to a chassis is divided among blades based on priority. 

Each time a service profile is associated or disassociated, Cisco UCS Manager recalculates the power allotment for each blade server within the chassis. If necessary, power from lower-priority service profiles is redistributed to higher-priority service profiles. 

UCS power groups cap power in less than one second to safely protect data center circuit breakers. A blade must stay at its cap for 20 seconds before the chassis power distribution is optimized. This is intentionally carried out over a slower timescale to prevent reacting to transient spikes in demand. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The system reserves enough power to boot a server in each slot, even if that slot is empty. This reserved power cannot be leveraged by servers requiring more power. Blades that fail to comply with the power cap are penalized. 

* * *  
  
---|---  
  
## Power Control Policy 

Cisco UCS uses the priority set in the power control policy along with the blade type and configuration to calculate the initial power allocation for each blade within a chassis. During normal operation, the active blades within a chassis can borrow power from idle blades within the same chassis. If all blades are active and reach the power cap, service profiles with higher priority power control policies take precedence over service profiles with lower priority power control policies. 

Priority is ranked on a scale of 1-10, where 1 indicates the highest priority and 10 indicates lowest priority. The default priority is 5. 

Starting with Cisco UCS Manager 3.2(2), chassis dynamic power rebalance mechanism is enabled by default. The mechanism continuously monitors the power usage of the blade servers and adjusts the power allocation accordingly. Chassis dynamic power rebalance mechanism operates within the overall chassis power budget set by Cisco UCS Manager, which is calculated from the available PSU power and Group power. 

For mission-critical application a special priority called no-cap is also available. Setting the priority to no-cap does not guarantee that a blade server gets maximum power all the time, however, it prioritizes the blade server over other servers during the chassis dynamic power rebalance budget allocations. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

If all the blade servers are set with no-cap priority and all of them run high power consuming loads, then there is a chance that some of the blade servers get capped under high power usage, based on the power distribution done through dynamic balance. 

* * *  
  
---|---  
  
Global Power Control Policy options are inherited by all the chassis managed by the Cisco UCS Manager. 

Starting with Cisco UCS Manager 4.1(3), a global policy called Power Save Mode is available. It is disabled by default, meaning that all PSUs present remain active regardless of power redundancy policy selection. Enabling the policy restores the older behavior.. 

Starting with Cisco UCS Manager 4.1(2), the power control policy is also used for regulating fans in Cisco UCS C220 M5 and C240 M5 rack servers in acoustically-sensitive environments. The Acoustic setting for these fans is only available on these servers. On C240 SD M5 rack servers, Acoustic mode is the default mode. 

Starting with Cisco UCS Manager 4.2(1), the power control policy is also used for regulating cooling in potentially high-temperature environments. This option is only available with Cisco UCS C220 M6, C240 M6, C225 M6, and C245 M6 rack servers and can be used with any fan speed option. 

Starting with Cisco UCS Manager 4.3(2), a global policy called Cisco UCS X9508 Chassis Power Extended Policy. This option is only available with Cisco UCS X9508 Chassis. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

You must include the power control policy in a service profile and that service profile must be associated with a server for it to take effect. 

* * *  
  
---|---  
  
  * Creating a Power Control Policy
  * Deleting a Power Control Policy


### Creating a Power Control Policy

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope org ` ` org-name |  Enters organization mode for the specified organization. To enter the root organization mode, use / as the org-name.  
**Step 2** |  UCS-A /org #  create power-control-policy ` ` power-control-pol-name |  Creates a power control policy and enters power control policy mode.  
**Step 3** |  UCS-A /org/power-control-policy #  set fanspeed ` `{any | balanced|high-power|low-power | max-power | performance | acoustic | max-cooling}  |  Specifies the fan speed for the power control policy. |  **Note** |  The Performance option is not supported on Cisco UCS C-Series M5 and M6 servers.   
---|---  
**Step 4** |  UCS-A /org/power-control-policy #  set cpu-package-power-limit ` `{default | min| max}  |  Specifies the Central Processing Unit (CPU) power consumption settings by selecting the Package Power Limits (PPL) in watts: default, min, or max. This setting determines the power a CPU can draw, thereby impacting system performance and thermal output.  |  **Note** |  The PPL is currently supported only on the processors of Cisco UCS C225 M8 and C245 M8 servers.  
---|---  
**Step 5** |  UCS-A /org/power-control-policy #  set priority ` `{priority-num | no-cap}  |  Specifies the priority for the power control policy.  
**Step 6** |  UCS-A /org/power-control-policy #  commit-buffer |  Commits the transaction to the system configuration.  
  
#### Example

The following example creates a power control policy called powerpolicy15, sets the priority at level 2, configures the CPU Package Power Limit to max, and commits the transaction: 
    
    
    UCS-A# **scope org /**
    UCS-A /org # **create power-control-policy powerpolicy15**
    UCS-A /org/power-control policy* # **set priority 2**
    UCS-A /org/power-control policy* # **set cpu-package-power-limit max**
    UCS-A /org/power-control policy* # **commit-buffer**
    UCS-A /org/power-control policy #

#### What to do next

Include the power control policy in a service profile.

Configuring Acoustic Mode

### Acoustic Mode Fan Profile

The Acoustic Mode fan profile is available on Cisco UCS C-Series rack servers..

Setting up an Acoustic Mode fan policy lets you reduce the noise level on Cisco UCS C-Series rack servers. The higher capacity fans on Cisco UCS C-Series rack servers increase the cooling capacity, but also create more acoustic noise. The standard fan profiles for Cisco UCS C-Series rack servers (Low Power, Balanced, High Power, and Max Power) are designed to regulate the server to optimize energy consumption. The primary goal of these fan profiles is to prevent throttling of CPU’s and peripherals. 

The goal of Acoustic Mode is reducing fan speed to reduce noise levels in acoustic-sensitive environments. Power capping has no effect when Acoustic Mode is selected. 

### Creating an Acoustic Mode Fan Policy

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope org ` ` org-name |  Enters organization mode for the specified organization. To enter the root organization mode, type / as the org-name.  
**Step 2** |  UCS-A /org #  create power-control-policy ` ` fan-policy-name |  Creates a fan control policy and enters power control policy mode. Fan policies are created through the power control interface.  
**Step 3** |  UCS-A /org/power-control-policy #  set fanspeed ` `{ acoustic }  |  Specifies Acoustic Mode as the fan speed for the power control policy.  
**Step 4** |  UCS-A /org/power-control-policy #  set priority ` `{priority-num | no-cap}  |  Specifies the priority for the fan's power control policy.  
**Step 5** |  UCS-A /org/power-control-policy #  commit-buffer |  Commits the transaction to the system configuration.  
  
#### What to do next

Include the power control policy in a service profile.

### Deleting a Power Control Policy

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope org ` ` org-name |  Enters organization mode for the specified organization. To enter the root organization mode, type / as the org-name.  
**Step 2** |  UCS-A /org #  delete power-control-policy ` ` power-control-pol-name |  Deletes the specified power control policy.  
**Step 3** |  UCS-A /org #  commit-buffer |  Commits the transaction to the system configuration.  
  
#### Example

The following example deletes a power control policy called powerpolicy15 and commits the transaction:
    
    
    UCS-A# **scope org /**
    UCS-A /org # **delete power-control-policy powerpolicy15**
    UCS-A /org* # **commit-buffer**
    UCS-A /org #

## Power Groups in UCS Manager 

A power group is a set of chassis that all draw power from the same power distribution unit (PDU). In Cisco UCS Manager, you can create power groups that include one or more chassis, then set a peak power cap in AC watts for that power grouping. 

Implementing power capping at the chassis level requires the following: 

  * IOM, CIMC, and BIOS version 1.4 or higher 

  * Two Power Supply Units (PSUs) 


The peak power cap is a static value that represents the maximum power available to all blade servers within a given power group. If you add or remove a blade from a power group, but do not manually modify the peak power value, the power group adjusts the peak power cap to accommodate the basic power-on requirements of all blades within that power group. 

A minimum of 890 AC watts should be set for each chassis. This converts to 800 watts of DC power, which is the minimum amount of power required to power an empty chassis. To associate a half-width blade, the group cap needs to be set to 1475 AC watts. For a full-width blade, it needs to be set to 2060 AC watts. 

After a chassis is added to a power group, all service profile associated with the blades in the chassis become part of that power group. Similarly, if you add a new blade to a chassis, that blade inherently becomes part of the chassis' power group. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Creating a power group is not the same as creating a server pool. However, you can populate a server pool with members of the same power group by creating a power qualifier and adding it to server pool policy. 

* * *  
  
---|---  
  
When a chassis is removed or deleted, the chassis gets removed from the power group. 

UCS Manager supports explicit and implicit power groups. 

  * Explicit: You can create a power group, add chassis' and racks, and assign a budget for the group. 

  * Implicit: Ensures that the chassis is always protected by limiting the power consumption within safe limits. By default, all chassis that are not part of an explicit power group are assigned to the default group and the appropriate caps are placed. New chassis that connect to UCS Manager are added to the default power group until you move them to a different power group. 


The following table describes the error messages you might encounter while assigning power budget and working with power groups. 

Error Message  | Cause  | Recommended Action   
---|---|---  
Insufficient budget for power group POWERGROUP_NAME and/or  Chassis N cannot be capped as group cap is low. Please consider raising the cap. and/or  Admin committed insufficient for power group GROUP_NAME, using previous value N and/or  Power cap application failed for chassis N  |  One of these messages displays if you did not meet the minimum limit when assigning the power cap for a chassis, or the power requirement increased because of the addition of blades or change of power policies.  |  Increase the power cap limit to the  Minimum Power Cap for Allowing Operations (W) value displayed on the Power Group page for the specified power group.   
Chassis N cannot be capped as the available PSU power is not enough for the chassis and the blades. Please correct the problem by checking input power or replace the PSU |  Displays when the power budget requirement for the chassis is more than the PSU power that is available.  |  Check the PSU input power and redundancy policy to ensure that enough power is available for the chassis.  If a PSU failed, replace the PSU.   
Power cap application failed for server N |  Displays when the server is consuming more power than allocated and cannot be capped, or the server is powered on when no power is allocated.  |  Do not power on un-associated servers.   
P-State lowered as consumption hit power cap for server |  Displays when the server is capped to reduce the power consumption below the allocated power.  |  This is an information message.  If a server should not be capped, in the service profile set the value of the power control policy Power Capping field to no-cap.   
Chassis N has a mix of high-line and low-line PSU input power sources. |  This fault is raised when a chassis has a mix of high-line and low-line PSU input sources connected.  |  This is an unsupported configuration. All PSUs must be connected to similar power sources.   
  
  * Creating a Power Group
  * Deleting a Power Group


### Creating a Power Group 

#### Before you begin

Ensure that the global power allocation policy is set to Policy Driven Chassis Group Cap. 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope power-cap-mgmt |  Enters power cap management mode.   
**Step 2** |  UCS-A /power-cap-mgmt #  create power-group ` ` power-group-name |  Creates a power group and enters power group mode.   
**Step 3** |  UCS-A /power-cap-mgmt/power-group #  set peak ` `{peak-num | disabled | uninitialized}  |  Specifies the maximum peak power (in watts) available to the power group.   
**Step 4** |  UCS-A /power-cap-mgmt/power-group #  create chassis ` ` chassis-id |  Adds the specified chassis to the power group and enters power group chassis mode.   
**Step 5** |  UCS-A /power-cap-mgmt/power-group #  create rack ` ` rack-id |  Adds the specified rack to the power group.   
**Step 6** |  UCS-A /power-cap-mgmt/power-group #  create fex ` ` fex-id |  Adds the specified FEX to the power group.   
**Step 7** |  UCS-A /power-cap-mgmt/power-group #  create fi ` ` fi-id |  Adds the specified FI to the power group.   
**Step 8** |  UCS-A /power-cap-mgmt/power-group/chassis #  commit-buffer |  Commits the transaction to the system configuration.   
  
#### Example

The following example creates a power group called powergroup1, specifies the maximum peak power for the power group (10000 watts), adds chassis 1 to the group, and commits the transaction: 
    
    
    UCS-A# **scope power-cap-mgmt**
    UCS-A /power-cap-mgmt # **create power-group powergroup1**
    UCS-A /power-cap-mgmt/power-group* # **set peak 10000**
    UCS-A /power-cap-mgmt/power-group* # **create chassis 1**
    UCS-A /power-cap-mgmt/power-group/chassis* # **commit-buffer**
    UCS-A /power-cap-mgmt/power-group/chassis #

### Deleting a Power Group

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope power-cap-mgmt |  Enters power cap management mode.  
**Step 2** |  UCS-A /power-cap-mgmt #  delete power-group ` ` power-group-name |  Deletes the specified power group.  
**Step 3** |  UCS-A /power-cap-mgmt/power-group/chassis #  commit-buffer |  Commits the transaction to the system configuration.  
  
#### Example

The following example deletes a power group called powergroup1 and commits the transaction:
    
    
    UCS-A# **scope power-cap-mgmt**
    UCS-A /power-cap-mgmt # **delete power-group powergroup1**
    UCS-A /power-cap-mgmt* # **commit-buffer**
    UCS-A /power-cap-mgmt #

Blade Level Power Capping

## Manual Blade Level Power Cap 

When manual blade-level power cap is configured in the global cap policy, you can set a power cap for each blade server in a Cisco UCS domain. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCSX-9508 Chassis does not support Manual Blade Level Power Cap. When you choose to select Manual Blade Level Power Cap, Chassis Management Controller (CMC) calculates the power allotment for Cisco UCSX-9508 Chassis. 

* * *  
  
---|---  
  
The following configuration options are available: 

  * Watts—You can specify the maximum amount of power that the server can consume at one time. This maximum can be any amount between 0 watts and 1300 watts. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

B480 M5 systems using 256GB DIMMs must have a manual blade level cap at 1300W.

* * *  
  
---|---  
  * Unbounded—No power usage limitations are imposed on the server. The server can use as much power as it requires. 


If the server encounters a spike in power usage that meets or exceeds the maximum configured for the server, Cisco UCS Manager does not disconnect or shut down the server. Instead, Cisco UCS Manager reduces the power that is made available to the server. This reduction can slow down the server, including a reduction in CPU speed. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

If you configure the manual blade-level power cap using Equipment > Policies > Global Policies > Global Power Allocation Policy, the priority set in the Power Control Policy is no longer relevant. 

* * *  
  
---|---  
  
## Setting the Blade-Level Power Cap for a Server 

### Before you begin

Ensure that the global power allocation policy is set to Manual Blade Level Cap. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server ` ` chassis-id / server-id |  Enters chassis server mode for the specified server.   
**Step 2** |  UCS-A /chassis/server #  set power-budget committed {unbounded | watts}  |  Commits the server to one of the following power usage levels: 

  * unbounded —Does not impose any power usage limitations on the server. 
  * watts —Allows you to specify the upper level for power usage by the server. If you choose this setting, enter the maximum number of watts that the server can use. The range is 0 to 10000000 watts. 

  
**Step 3** |  UCS-A /chassis/server #  commit-buffer |  Commits the transaction to the system configuration.   
**Step 4** |  UCS-A /chassis/server #  show power-budget |  (Optional) Displays the power usage level setting.   
  
### Example

The following example limits the power usage for a server to unbounded and then to 1000 watts and commits the transaction: 
    
    
    UCS-A# **scope server 1/7**
    UCS-A /chassis/server # **show power-budget**
    
    Budget:
        AdminCommitted (W)
    				-----------------
        139
    UCS-A /chassis/server # **set power-budget committed unbounded**
    UCS-A /chassis/server* # **commit-buffer**
    UCS-A /chassis/server # **show power-budget**
    
    Budget:
        AdminCommitted (W)
    				-----------------
        Unbounded 
    
    UCS-A /chassis/server # **set power-budget committed 1000**
    UCS-A /chassis/server* # **commit-buffer**
    UCS-A /chassis/server # **show power-budget**
    
    Budget:
        AdminCommitted (W)
    				-----------------
        1000 
    UCS-A /chassis/server #
    
    

Configuring a Chassis Level Fan Policy

## Configuring Fan Speed for Power Management

Globally managing the fan speed can help in power management by applying a single policy for all B-series server fans in an enclosure, based on general cooling needs. Set the fan speed on a per-chassis basis in the Global Policies. The two options are: 

  * Balanced—The fan runs at a faster speed when needed, based on the heat generated by the server. When possible, the fan returns to the minimum required speed. (Default.) 

  * Low Power—The fan runs at the minimum speed that is required to keep the server cool. 


The new option takes effect when the new selection is saved. Use Low Power to save on system power. 

## Configuring the Global Fan Control Policy

### Procedure

* * *

**Step 1** |  In the Navigation pane, click Equipment.   
---|---  
**Step 2** |  Click the Equipment node.   
**Step 3** |  In the Work pane, click the Policies tab.   
**Step 4** |  Click the Global Policies subtab.   
**Step 5** |  In the Fan Control Policy area, click one of the following radio buttons: 

  * Balanced—This is the default option. 
  * Low Power

  
**Step 6** |  Click Save Changes.   
  
* * *

## Viewing Server Statistics 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server ` ` chassis-id / server-id |  Enters chassis server mode for the specified server.   
**Step 2** |  UCS-A /chassis/server #  show ` ` stats |  Displays the following server statistics: 

  * Ethernet Port Error 
  * Ethernet Port Multicast 
  * Ethernet Port 
  * Virtual Interface 
  * Motherboard Power 
  * PC Ie Fatal Completion Error 
  * PC Ie Fatal Protocol Error 
  * PC Ie Fatal Receiving Error 
  * PC Ie Fatal Error 
  * Memory Error 
  * DIMM Env 
  * CPU Env 

  
  
### Example

The following example shows the section on motherboard power usage statistics: 
    
    
    UCS-A# **scope server 2/4**
    UCS-A /chassis/server # **show stats**
    
    Motherboard Power Statistics:
    Time Collected: 2016-07-11T20:51:24.722
    Monitored Object: sys/chassis-1/blade-1/board/power-stats
    Suspect: No
    Consumed Power (W): 126.000000
    Input Voltage (V): 11.859000
    Input Current (A): 10.624842
    Thresholded: 0
    
    UCS-A /chassis/server # 
    

Global Power Profiling Policy Configuration

## Global Power Profiling Policy 

The Global Power Profiling Policy specifies how power allocation is applied to all of the servers in a chassis. The policy applies when you set the Global Power Allocation Policy to policy-driven-chassis-group-cap . You can set the Global Power Profiling Policy to one of the following: 

  * Disabled—The minimum and maximum power cap values of the blades are calculated based on the static power consumption values of each of the components. 

  * Enabled—The minimum and maximum power cap values of the blades are measured as part of the server discovery. These values are similar to the actual power consumption of the blades. 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

After enabling the Global Power Profiling Policy, you must re-acknowledge the blades to obtain the minimum and maximum power cap. 

* * *  
  
---|---  
  
## Configuring the Global Power Profile Policy 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope power-cap-mgmt |  Enters power cap management mode.   
**Step 2** |  UCS-A /power-cap-mgmt #  set profile-policy ` `{no | yes}  |  Enables or disables the global power profiling policy.   
**Step 3** |  UCS-A /power-cap-mgmt #  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example shows how to enable the global power profile policy and commit the transaction: 
    
    
    UCS-A# **scope power-cap-mgmt**
    UCS-A /power-cap-mgmt # **set profile-policy yes**
    UCS-A /power-cap-mgmt* # **commit-buffer**
    UCS-A /power-cap-mgmt #

Global Power Allocation Policy

## Global Power Allocation Policy 

The Global Power Allocation Policy allows you to specify the Policy Driven Chassis Group Power Cap or Manual Blade-level Power Cap power allocation method applied to servers in a chassis. 

Cisco recommends using the default Policy Driven Chassis Group Power Cap power allocation method. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

Any change to the Manual Blade level Power Cap configuration results in the loss of any groups or configuration options set for the Policy Driven Chassis Group Power Cap. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCSX-9508 Chassis supports Policy Driven Chassis Group Cap only.  When you choose to select Policy Driven Chassis Group Cap, Cisco UCS Manager calculates the power allotment for Cisco UCS X9508 chassis and when you choose to select Manual Blade Level Power Cap, Chassis Management Controller (CMC) calculates the power allotment for Cisco UCSX-9508 Chassis. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For Cisco UCSX-9508 Chassis Allocated (W) and Measured Max. (W) will not match. The max allocated values are used to calculate the chassis-level power limit and Intelligent Fabric Modules (IFM) allocates the power based on the power limit. 

* * *  
  
---|---  
  
## Configuring the Global Power Allocation Policy 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope power-cap-mgmt |  Enters power cap management mode.   
**Step 2** |  UCS-A /power-cap-mgmt #  set cap-policy ` `{manual-blade-level-cap | policy-driven-chassis-group-cap}  |  Sets the global cap policy to the specified power cap management mode.  By default, the global cap policy is set to policy driven chassis group cap.   
**Step 3** |  UCS-A /power-cap-mgmt #  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example sets the global cap policy to manual blade power cap and commits the transaction: 
    
    
    UCS-A# **scope power-cap-mgmt**
    UCS-A /power-cap-mgmt # **set cap-policy manual-blade-level-cap**
    UCS-A /power-cap-mgmt* # **commit-buffer**
    UCS-A /power-cap-mgmt #

## Viewing the Power Cap Values for Servers 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope power-cap-mgmt |  Enters power cap management mode.   
**Step 2** |  UCS-A /power-cap-mgmt #  show power-measured |  Displays the minimum and maximum power cap values.   
  
### Example

The following example shows how to display the minimum and maximum power cap values: 
    
    
    UCS-A# **scope power-cap-mgmt**
    UCS-A /power-cap-mgmt # **show power-measured**
    
    Measured Power:
        Device Id (W)  Minimum power (W) Maximum power (W) OperMethod
        -------------- ----------------- ----------------- ----------
        blade   1/1    234               353               Pnuos
    
    UCS-A /power-cap-mgmt # 
    

## Power Management During Power-on Operations 

### Boot Staggering during Power on

Cisco UCS Manager attempts to boot as many blades as possible based on the amount of available power. If the power required to boot a blade is not available, Cisco UCS Manager staggers the boot in the Finite State Machine (FSM) CheckPowerAvailability stage, and raises the following fault on the blade: Insufficient power available to power-on server x/y. 

When the required power becomes available, the FSM proceeds with blade power on. After a blade powers off, the allocated power budget is reclaimed. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

When the power budget that was allocated to the blade is reclaimed, the allocated power displays as 0 Watts. 

* * *  
  
---|---  
  
**Limitation**

If you power on a blade outside of the Cisco UCS Manager and if there is not enough power available for allocation, the following fault is raised: 

Power cap application failed for server x/y

### Power Allocation during Service Profile Association

The power allocated to a blade during service profile association depends on the Power Control Policy used, and the power that is available from the power group. After the power is allocated to a server during a successful service profile association, the blade is guaranteed the minimum power cap. If the Power Control Policy priority is set to no-cap, a blade is allocated a potential maximum power cap, which might exceed the measured maximum power cap that displays. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

If the priority of an associated blade is changed to no-cap, and is not able to allocate the maximum power cap, you might see one of the following faults: 

  * PSU-insufficient—There is not enough available power for the PSU. 
  * Group-cap-insufficient—The group cap value is not sufficient for the blade. 


* * *  
  
---|---  
  
Power Sync Policy Configuration

## Power Sync Policy 

Cisco UCS Manager includes a global (default) power sync policy to address power synchronization issues between the associated service profiles and the servers. You can use the power sync policy to synchronize the power state when the power state of the service profile differs from the actual power state of the server. The policy allows you to control when to synchronize the power state on the associated service profiles for the servers. The power sync policy does not affect other power-related policies. 

The power synchronization policy applies to all the service profiles by default. You cannot delete the default power sync policy, but you can edit the default policy. You can create your own power sync policies and apply them to the service profiles. You can also create a power sync policy that is specific to a service profile and it always takes precedence over the default policy. 

Cisco UCS Manager creates a fault on the associated service profile when the power sync policy referenced in the service profile does not exist. Cisco UCS Manager automatically clears the fault once you create a power sync policy for the specified service profile or change the reference to an existing policy in the service profile. 

## Power Synchronization Behavior 

Cisco UCS Manager synchronizes the power state only when the actual power state of the server is OFF. The current power synchronization behavior is based on the actual power state and the preferred power state after shallow association occurs. 

For example, the following events trigger shallow association: 

  * Fabric Interconnects(FI) and IOM disconnected. 

  * IOM reset 

  * FI power loss or reboot 

  * Chassis reacknowledgment 

  * Chassis power loss 

  * Service profile change 


The following table describes the current power synchronization behavior: 

Event  |  Preferred Power State  |  Actual Power State Before Event  |  Actual Power State After Event   
---|---|---|---  
Shallow Association  |  ON  |  OFF  |  ON   
Shallow Association  |  OFF  |  OFF  |  OFF   
Shallow Association  |  ON  |  ON  |  ON   
Shallow Association  |  OFF  |  ON  |  ON   
  
## Displaying the Global Power Sync Policy 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A #  scope org ` ` org-name |  Enters organization mode for the specified organization. To enter the root organization mode, type / as the org-name.   
**Step 2** |  UCS-A/org #  scope power-sync-policy default ` ` |  Enters the global power sync policy mode.   
**Step 3** |  UCS-A /org/power/-sync-policy #  show  ` ` {detail | expand | detail expand }  |  Displays the global power sync policy information.   
  
### Example

The following example displays the global (default) power sync policy: 
    
    
    UCS-A # **scope org**
    UCS-A /org # **scope power-sync-policy default-sync**
    UCS-A /org/power-sync-policy # **show expand**
    
    Power Sync Policy:
        Name                 Power Sync Option
        -------------------- -----------------
        default              Default Sync
    
    UCS-A /org/power-sync-policy # **show detail expand**
    
    Power Sync Policy:
        Full Name: org-root/power-sync-default
        Name: default
        Description:
        Power Sync Option: Default Sync
        Policy Owner: Local
    
    UCS-A /org/power-sync-policy # 
    

## Setting Global Policy Reference for a Service Profile

To refer the global power sync policy in a service profile, use the following commands in service profile mode: 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A #  scope org ` ` org-name |  Enters organization mode for the specified organization. To enter the root organization mode, type / as the org-name.   
**Step 2** |  UCS-A/org #  scope service-profile ` ` service-profile-name |  Enters the service profile mode for the specified service profile. The name of the service profile can be a minimum of two characters and a maximum up to 32 characters.   
**Step 3** |  UCS-A /org/service-profile #  set power-sync-policy default |  Specifies the global power sync policy that can be referenced in the service profile. You can also change the policy reference from the default to other power sync policies using this command.   
**Step 4** |  UCS-A /org/service-profile* # commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example sets the reference to the global power sync policy for use in the service profile. 
    
    
    UCS-A # **scope org**
    			 UCS-A/org # **scope service-profile spnew**
    			 UCS-A/org/service-profile # **set power-sync-policy default**
    			 UCS-A/org/service-profile* # **commit-buffer**
    			 

## Creating a Power Sync Policy

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A #  scope org ` ` org-name |  Enters organization mode for the specified organization. To enter the root organization mode, type / as the org-name.   
**Step 2** |  UCS-A /org #  create power-sync-policy ` ` power-sync-pol-name |  Creates a power sync policy and enters power sync policy mode. The power sync policy name can be up to 16 characters.   
**Step 3** |  (Optional) UCS-A /org/power-sync-policy* # set` ` descr` ` optionall-description | (Optional)  Specifies the description of the power-sync-policy. You can also modify the description using the descr keyword.   
**Step 4** |  UCS-A /org/power-sync-policy* # set` ` sync-option` ` { always-sync | default-sync | initial-only-sync }  |  Specifies the power synchronization option to the physical server. You can also modify the power synchronization option using the sync-option keyword. This can be one of the following: 

  * Default Sync—After the initial server association, any configuration change or management connectivity changes that you perform trigger a server reassociation. This option synchronizes the desired power state to the physical server if the physical server power state is off and the desired power state is on. This is the default behavior. 
  * Always Sync—When the initial server association or the server reassociation occurs, this option always synchronizes the desired power state to the physical server even if the physical server power state is on and the desired power state is off. 
  * Initial Only Sync—This option only synchronizes the power to a server when a service profile is associated to the server for the first time or when the server is re-commissioned. When you set this option, resetting the power state from the physical server side does not affect the desired power state on the service profile. 

  
**Step 5** |  UCS-A /org/power-sync-policy* # commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example creates a power sync policy called newSyncPolicy, sets the default sync-option, and commits the transaction to the system configuration: 
    
    
    UCS-A # **scope org**
    UCS-A /org # **create power-sync-policy newSyncPolicy**
    UCS-A /org/power-sync-policy* # **set decsr newSyncPolicy**
    UCS-A /org/power-sync-policy* # **set sync-option default-sync**
    UCS-A /org/power-sync-policy* # **commit-buffer**
    UCS-A /org/power-sync-policy #
    

### What to do next

Include the power sync policy in a service profile or in a service profile template. 

## Deleting a Power Sync Policy

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A #  scope org ` ` org-name |  Enters organization mode for the specified organization. To enter the root organization mode, type / as the org-name.   
**Step 2** |  UCS-A /org #  delete power-sync-policy ` ` power-sync-pol-name |  Deletes the specified power sync policy.   
**Step 3** |  UCS-A /org #  commit buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example deletes the power sync policy called spnew and commits the transaction to the system: 
    
    
    UCS-A # **scope org**
    UCS-A /org # **delete power-sync-policy spnew**
    UCS-A /org # **commit-buffer**

## Displaying All Power Sync Policies

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A #  scope org ` ` org-name |  Enters organization mode for the specified organization. To enter the root organization mode, type / as the org-name.   
**Step 2** |  UCS-A /org #  show power-sync-policy ` ` {detail | expand | detail expand }  |  Displays the default, local, and other power sync policies.   
  
### Example

The following example displays power sync policies that are defined: 
    
    
    UCS-A # **scope org**
    UCS-A /org # **show power-sync-policy expand**
    Power Sync Policy:
        Name                 Power Sync Option
        -------------------- -----------------
        default              Default Sync
        policy-1             Default Sync
    
    UCS-A /org # **show power-sync-policy detail expand**
    Power Sync Policy:
        Full Name: org-root/power-sync-default
        Name: default
        Description:
        Power Sync Option: Default Sync
        Policy Owner: Local
    
        Full Name: org-root/power-sync-policy-1
        Name: policy-1
        Description:
        Power Sync Option: Default Sync
        Policy Owner: Local
    
    UCS-A /org #

## Creating a Local Policy

To create a local power sync policy that you want to use by any service profile, create a power sync definition for the power sync policy. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A #  scope org ` ` org-name |  Enters organization mode for the specified organization. To enter the root organization mode, type / as the org-name.   
**Step 2** |  UCS-A /org #  scope service-profile ` ` service-profile-name |  Enters the service profile mode for the specified service profile. The name of the service profile can be a minimum of two characters and a maximum up to 32 characters.   
**Step 3** |  UCS-A /org/service-profile #  create power-sync-definition |  Enters the power sync definition mode. You can create a power sync policy definition that you defined for the power sync policy.   
**Step 4** |  (Optional) UCS-A /org/service-profile/power-sync-definition* # set` ` descr` ` optional-description | (Optional)  Specifies the description of the power-sync-policy. You can also change the description using the descr keyword.   
**Step 5** |  UCS-A /org/service-profile/power-sync-definition* # set` ` sync-option` ` { always-sync | default-sync | initial-only-sync }  |  Specifies the power synchronization option to the physical server. You can also change the power synchronization option using the sync-option keyword.   
**Step 6** |  UCS-A /org/service-profile/power-sync-definition* # commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example creates a local policy using the policy sync definition, sets the sync-option, and commits the transaction to the system configuration: 
    
    
     UCS-A # **scope org**
     UCS-A/org # **scope service-profile spnew**
    UCS-A/org/service-profile # **create power-sync-definition**
    UCS-A/org/service-profile/power-sync-definition* # **set decsr spnew**
    UCS-A/org/service-profile/power-sync-definition* # **set sync-option default-sync**
    UCS-A/org/service-profile/power-sync-definition* # **commit-buffer**

## Showing a Local Policy

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A #  scope org ` ` org-name |  Enters organization mode for the specified organization. To enter the root organization mode, type / as the org-name.   
**Step 2** |  UCS-A/org #  scope service-profile ` ` service-profile-name |  Enters the service profile mode for the specified service profile. The name of the service profile can be a minimum of two characters and a maximum up to 32 characters.   
**Step 3** |  (Optional) UCS-A /org/service-profile #  show power-sync-policy ` ` {detail | expand | detail expand }  | (Optional)  Displays the local policy in the power-sync-policy mode.   
**Step 4** |  UCS-A /org/service-profile #  show power-sync-definition ` ` {detail | expand | detail expand }  |  Displays the local policy for the specified service policy in the power-sync-definition mode.  |  **Note** |  If you do not have a definition for the power sync policy, you can still use the command, but you cannot see anything displayed.   
---|---  
  
### Example

The following example displays the local policy in use by the service profile spnew: 
    
    
     UCS-A # **scope org**
    UCS-A/org # **scope service-profile spnew**
    UCS-A/org/service-profile # **show power-sync-definition expand**
    
    Power Sync Definition:
        Name                 Power Sync Option
        -------------------- -----------------
        spnew                Always Sync
    
    UCS-A/org/service-profile # **show power-sync-definition detail expand**
    
    Power Sync Definition:
        Full Name: org-root/ls-sp2/power-sync-def
        Name: spnew 
        Description: optional description
        Power Sync Option: Always Sync
        Policy Owner: Local
    
    UCS-A/org/service-profile # 

## Deleting a Local Policy

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A #  scope org ` ` org-name |  Enters organization mode for the specified organization. To enter the root organization mode, type / as the org-name.   
**Step 2** |  UCS-A/org #  scope service-profile ` ` service-profile-name |  Enters the service profile mode for the specified service profile. The name of the service profile can be a minimum of two characters and a maximum up to 32 characters.   
**Step 3** |  UCS-A /org/service-profile #  delete power-sync-definition |  Enters the power sync definition mode. You can delete a power sync policy definition that you defined for the power sync policy.   
**Step 4** |  UCS-A /org/service-profile* # commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example deletes the local policy in use by the service profile. 
    
    
    UCS-A # **scope org**
    			 UCS-A/org # **scope service-profile spnew**
    			 UCS-A/org/service-profile # **delete power-sync-definition**
    			 UCS-A/org/service-profile* # **commit-buffer**
    			 

## Rack Server Power Management

Power capping is supported for all the Cisco UCS C-Series servers except Cisco UCS C125 M5 Servers. 

##  UCS Mini Power Management 

You can manage power of the blade servers in the Cisco UCS 6324 Fabric Interconnect (FI), which is used for remote offices and branch sites, and for limited server deployments. UCS Manager supports Dual Line Power Supply Unit and 110V when used with the Cisco UCS 6324 Fabric Interconnect. You can manage how you want to allocate power when using 110V power supplies, because they might not provide enough power for a fully loaded chassis. Dual power supplies is standard for both AC and DC-48V on the Cisco UCS Mini 6324. 

## Viewing X-Fabric Module (XFM) Fan Status

This procedure is applicable only for Cisco UCS X9508 Server Chassis equipped with XFM. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope chassis chassis-num |  Enters chassis mode for the specified chassis.   
**Step 2** |  UCS-A /chassis#  scope xfm xfm-num |  Enters the XFM specified in the command.  
**Step 3** |  UCS-A /chassis/xfm#  scope fan-module Tray-num Module-num |  Enters the specified fan tray in the specified module.  
**Step 4** |  UCS-A /chassis/xfm/fan-module#  scope fan fan-num |  Enters the specified fan module.  
**Step 5** |  UCS-A /chassis/xfm/fan-module/fan #  show detail |  Displays the following:
    
    
    Overall Status: 
        Operability: 
        Threshold Status: 
        Power State: 
        Presence: 
        Thermal Status: 
        Product Name: 
        PID: 
        VID: 
        Vendor: 
        Serial (SN): 
        HW Revision:   
  
### Example

Following examples show how to scope to XFM and see fan overall status:
    
    
    UCS-A# scope chassis 2
    UCS-A /chassis # scope xfm 1
    UCS-A /chassis/xfm # scope fan-module 1 1
    UCS-A /chassis/xfm/fan-module # scope fan 1
    UCS-A /chassis/xfm/fan-module/fan # show detail
    
    Fan:
        ID: 1
        Overall Status: Operable
        Operability: Operable
        Threshold Status: OK
        Power State: On
        Presence: Equipped
        Thermal Status: N/A
        Product Name: Fan Module for UCS 9508 Chassis IOM/XFM
        PID: UCSX-RSFAN
        VID: V01
        Vendor: Cisco Systems Inc
        Serial (SN): N/A
        HW Revision: 0
    

---

## Page 10: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_4_3/b_UCSM_CLI_Infrastructure_Management_Guide_chapter_01000.html

# Blade Server Management

  * Blade Server Management
  * Guidelines for Removing and Decommissioning Blade Servers
  * Recommendations for Avoiding Unexpected Server Power Changes
  * Booting a Blade Server
  * Shutting Down a Blade Server
  * Power Cycling a Blade Server
  * Performing a Hard Reset on a Blade Server
  * Acknowledging a Blade Server
  * Removing a Blade Server from a Chassis
  * Decommissioning a Blade Server
  * Recommissioning a Blade Server
  * Turning On the Locator LED for a Blade Server
  * Turning Off the Locator LED for a Blade Server
  * Resetting the CMOS for a Blade Server
  * Resetting the CIMC for a Blade Server
  * Clearing TPM for a Blade Server
  * Resetting the BIOS Password for a Blade Server
  * Issuing an NMI from a Blade Server
  * Health LED Alarms
  * Smart SSD
  * Data Sanitization


## Blade Server Management 

You can manage and monitor all blade servers in a Cisco UCS domain through Cisco UCS Manager. You can perform some blade server management tasks, such as changes to the power state, from the server and service profile. 

The remaining management tasks can only be performed on the server. 

The power supply units go into power save mode when a chassis has two blades or less. When a third blade is added to the chassis and is fully discovered, the power supply units return to regular mode. 

If a blade server slot in a chassis is empty, Cisco UCS Manager provides information, errors, and faults for that slot. You can also re-acknowledge the slot to resolve server mismatch errors and to have Cisco UCS Manager rediscover the blade server in the slot. 

## Guidelines for Removing and Decommissioning Blade Servers 

Consider the following guidelines when deciding whether to remove or decommission a blade server using Cisco UCS Manager: 

### Decommissioning a Blade Server 

If you want to temporarily decommission a physically present and connected blade server, you can temporarily remove it from the configuration. A portion of the server's information is retained by Cisco UCS Manager for future use, in case the blade server is recommissioned. 

### Removing a Blade Server 

Removing is performed when you physically remove a blade server from the Cisco UCS Manager by disconnecting it from the chassis. You cannot remove a blade server from Cisco UCS Manager if it is physically present and connected to a chassis. After the physical removal of the blade server is completed, the configuration for that blade server can be removed in Cisco UCS Manager. 

During removal, active links to the blade server are disabled, all entries from databases are removed, and the server is automatically removed from any server pools that it was assigned to during discovery. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Only servers added to a server pool automatically during discovery are removed automatically. Servers that were manually added to a server pool must be removed manually. 

* * *  
  
---|---  
  
To add a removed blade server back to the configuration, it must be reconnected, then rediscovered. When a server is reintroduced to Cisco UCS Manager, it is treated as a new server and is subject to the deep discovery process. For this reason, it is possible for Cisco UCS Manager to assign the server a new ID that might be different from the ID that it held before. 

## Recommendations for Avoiding Unexpected Server Power Changes 

If a server is not associated with a service profile, you can use any available means to change the server power state, including the physical `Power` or `Reset` buttons on the server. 

If a server is associated with, or assigned to, a service profile, you should only use the following methods to change the server power state: 

  * In Cisco UCS Manager GUI, go to the General tab for the server or the service profile associated with the server and select Boot Server or Shutdown Server from the Actions area. 

  * In Cisco UCS Manager CLI, scope to the server or the service profile associated with the server and use the power up or power down commands. 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

Do _not_ use any of the following options on an associated server that is currently powered off: 

  * Reset in the GUI 
  * cycle cycle-immediate or reset hard-reset-immediate in the CLI 
  * The physical `Power` or `Reset` buttons on the server 


* * *  
  
---|---  
  
If you reset, cycle, or use the physical power buttons on a server that is currently powered off, the server's actual power state might become out of sync with the desired power state setting in the service profile. If the communication between the server and Cisco UCS Manager is disrupted or if the service profile configuration changes, Cisco UCS Manager might apply the desired power state from the service profile to the server, causing an unexpected power change. 

Power synchronization issues can lead to an unexpected server restart, as shown below: 

Desired Power State in Service Profile  |  Current Server Power State  |  Server Power State After Communication Is Disrupted   
---|---|---  
Up  |  Powered Off  |  Powered On   
Down  |  Powered On  |  Powered On  |  **Note** |  Running servers are not shut down regardless of the desired power state in the service profile.   
---|---  
  
## Booting a Blade Server 

### Before you begin

Associate a service profile with a blade server or server pool. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope org ` ` org-name |  Enters organization mode for the specified organization. To enter the root organization mode, type  / as the  org-name .   
**Step 2** |  UCS-A /org #  scope service-profile ` ` profile-name |  Enters organization service profile mode for the specified service profile.   
**Step 3** |  UCS-A /org/service-profile #  power up |  Boots the blade server associated with the service profile.   
**Step 4** |  UCS-A /org/service-profile #  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example boots the blade server associated with the service profile named ServProf34 and commits the transaction: 
    
    
    UCS-A# **scope org /**
    UCS-A /org* # **scope service-profile ServProf34**
    UCS-A /org/service-profile* # **power up**
    UCS-A /org/service-profile* # **commit-buffer**
    UCS-A /org/service-profile #
    

## Shutting Down a Blade Server 

When you use this procedure to shut down a server with an installed operating system, Cisco UCS Manager triggers the OS into a graceful shutdown sequence. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

When a blade server that is associated with a service profile is shut down, the VIF down alerts F0283 and F0479 are automatically suppressed. 

* * *  
  
---|---  
  
### Before you begin

Associate a service profile with a blade server or server pool. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope org ` ` org-name |  Enters organization mode for the specified organization. To enter the root organization mode, type / as the org-name.   
**Step 2** |  UCS-A /org #  scope service-profile ` ` profile-name |  Enters organization service profile mode for the specified service profile.   
**Step 3** |  UCS-A /org/service-profile #  power down |  Shuts down the blade server associated with the service profile.   
**Step 4** |  UCS-A /org/service-profile #  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example shuts down the blade server associated with the service profile named ServProf34 and commits the transaction: 
    
    
    UCS-A# **scope org /**
    UCS-A /org # **scope service-profile ServProf34**
    UCS-A /org/service-profile # **power down**
    UCS-A /org/service-profile* # **commit-buffer**
    UCS-A /org/service-profile #
    

## Power Cycling a Blade Server 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server ` ` chassis-num / server-num |  Enters chassis server mode for the specified blade server.   
**Step 2** |  UCS-A /chassis/server #  cycle ` `{cycle-immediate | cycle-wait}  |  Power cycles the blade server.  Use the  cycle-immediate keyword to immediately begin power cycling the blade server; use the  cycle-wait keyword to schedule the power cycle to begin after all pending management operations have completed.   
**Step 3** |  UCS-A#  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example immediately power cycles blade server 4 in chassis 2 and commits the transaction: 
    
    
    UCS-A# **scope server 2/4**
    UCS-A /chassis/server # **cycle cycle-immediate**
    UCS-A /chassis/server* # **commit-buffer**
    UCS-A /chassis/server # 
    

## Performing a Hard Reset on a Blade Server 

When you reset a server, Cisco UCS Manager sends a pulse on the reset line. You can choose to gracefully shut down the operating system. If the operating system does not support a graceful shutdown, the server is power cycled. The option to have Cisco UCS Manager complete all management operations before it resets the server does not guarantee the completion of these operations before the server is reset. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

If you are trying to boot a server from a power-down state, you should not use Reset.  If you continue the power-up with this process, the desired power state of the servers become out of sync with the actual power state and the servers might unexpectedly shut down at a later time. To safely reboot the selected servers from a power-down state, click Cancel, then select the Boot Server action. 

* * *  
  
---|---  
  
### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server ` ` chassis-num / server-num |  Enters chassis server mode for the specified server.   
**Step 2** |  UCS-A /chassis/server #  reset ` `{hard-reset-immediate | hard-reset-wait}  |  Performs a hard reset of the blade server.  Use the hard-reset-immediate keyword to immediately begin hard resetting the server; use the hard-reset-wait keyword to schedule the hard reset to begin after all pending management operations have completed.   
**Step 3** |  UCS-A /server #  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example performs an immediate hard reset of blade server 4 in chassis 2 and commits the transaction: 
    
    
    UCS-A#  scope server 2/4
    UCS-A /chassis/server # reset hard-reset-immediate
    UCS-A /chassis/server* # commit-buffer
    UCS-A /chassis/server # 
    

## Acknowledging a Blade Server 

Perform the following procedure to rediscover the server and all endpoints in the server. For example, you can use this procedure if a server is stuck in an unexpected state, such as the discovery state. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  acknowledge server ` ` chassis-num / server-num |  Acknowledges the specified blade server.   
**Step 2** |  UCS-A#  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example acknowledges server 4 in chassis 2 and commits the transaction: 
    
    
    UCS-A# **acknowledge server 2/4**
    UCS-A* # **commit-buffer**
    UCS-A # 
    

## Removing a Blade Server from a Chassis 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  remove server ` ` chassis-num / server-num |  Removes the specified blade server.   
**Step 2** |  UCS-A#  commit-buffer |  Commits the transaction to the system configuration.   
**Step 3** |  Go to the physical location of the chassis and remove the server hardware from the slot.  |  For instructions on how to remove the server hardware, see the Cisco UCS Hardware Installation Guide for your chassis.   
  
### Example

The following example removes blade server 4 in chassis 2 and commits the transaction: 
    
    
    UCS-A#  **remove server 2/4**
    UCS-A* # **commit-buffer**
    UCS-A # 
    

### What to do next

If you physically re-install the blade server, you must re-acknowledge the slot for the Cisco UCS Manager to rediscover the server. 

For more information, see Acknowledging a Blade Server. 

## Decommissioning a Blade Server 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  decommission server ` ` chassis-num / server-num |  Decommissions the specified blade server.   
**Step 2** |  UCS-A#  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example decommissions blade server 4 in chassis 2 and commits the transaction: 
    
    
    UCS-A# decommission server 2/4
    UCS-A* # commit-buffer
    UCS-A # 
    

### What to do next

After decommissioning the blade server, you must wait for few minutes to initiate the recommissioning of the server.

## Recommissioning a Blade Server

### Before you begin

Incase of recommissioning a blade server after decommission, you should wait for few minutes to initiate the recommission of the server. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  recommission server ` ` chassis-num / server-num |  Recommissions the specified blade server.   
**Step 2** |  UCS-A#  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example recommissions blade server 4 in chassis 2 and commits the transaction: 
    
    
    UCS-A# recommission server 2/4
    UCS-A* # commit-buffer
    UCS-A # 
    

## Turning On the Locator LED for a Blade Server 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server ` ` chassis-num / server-num |  Enters chassis server mode for the specified chassis.   
**Step 2** |  UCS-A /chassis/server #  enable locator-led [multi-master | multi-slave]  |  Turns on the blade server locator LED. For the Cisco UCS B460 M4 blade server, you can add the following keywords: 

  * multi-master—Turns on the LED for the master node only. 
  * multi-slave—Turns on the LED for the slave node only. 

  
**Step 3** |  UCS-A /chassis/server #  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example turns on the locator LED on blade server 4 in chassis 2 and commits the transaction: 
    
    
    UCS-A# scope server 2/4
    UCS-A /chassis/server # enable  locator-led
    UCS-A /chassis/server* # commit-buffer
    UCS-A /chassis/server # 
    
    

The following example turns on the locator LED for the master node only on blade server 7 in chassis 2 and commits the transaction: 
    
    
    UCS-A# scope chassis 2/7
    UCS-A /chassis/server # enable locator-led multi-master
    UCS-A /chassis/server* # commit-buffer
    UCS-A /chassis/server # 
    

## Turning Off the Locator LED for a Blade Server 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server chassis-num / server-num |  Enters chassis mode for the specified chassis.   
**Step 2** |  UCS-A /chassis/server #  disable locator-led [multi-master | multi-slave]  |  Turns off the blade server locator LED. For the Cisco UCS B460 M4 blade server, you can add the following keywords: 

  * multi-master—Turns off the LED for the master node only. 
  * multi-slave—Turns off the LED for the slave node only. 

  
**Step 3** |  UCS-A /chassis/server #  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example turns off the locator LED on blade server 4 in chassis 2 and commits the transaction: 
    
    
    UCS-A# scope chassis 2/4
    UCS-A /chassis/server # disable locator-led
    UCS-A /chassis/server* # commit-buffer
    UCS-A /chassis/server # 
    
    

The following example turns off the locator LED for the master node on blade server 7 in chassis 2 and commits the transaction: 
    
    
    UCS-A# scope chassis 2/7
    UCS-A /chassis/server # disable locator-led multi-master
    UCS-A /chassis/server* # commit-buffer
    UCS-A /chassis/server # 
    

## Resetting the CMOS for a Blade Server 

Sometimes, troubleshooting a server might require you to reset the CMOS. Resetting the CMOS is not part of the normal maintenance of a server. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server ` ` chassis-num / server-num |  Enters chassis server mode for the specified chassis.   
**Step 2** |  UCS-A /chassis/server #  reset-cmos |  Resets the CMOS for the blade server.   
**Step 3** |  UCS-A /chassis/server #  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example resets the CMOS for blade server 4 in chassis 2 and commits the transaction: 
    
    
    UCS-A# **scope server 2/4**
    UCS-A /chassis/server # **reset-cmos**
    UCS-A /chassis/server* # **commit-buffer**
    UCS-A /chassis/server #  
    

## Resetting the CIMC for a Blade Server 

Sometimes, with the firmware, troubleshooting a server might require you to reset the CIMC. Resetting the CIMC is not part of the normal maintenance of a server. After you reset the CIMC, the CIMC reboots the management controller of the blade server. 

If the CIMC is reset, the power monitoring functions of Cisco UCS become briefly unavailable until the CIMC reboots. Typically, the reset only takes 20 seconds; however, it is possible that the peak power cap can exceed during that time. To avoid exceeding the configured power cap in a low power-capped environment, consider staggering the rebooting or activation of CIMCs. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server ` ` chassis-num / server-num |  Enters chassis server mode for the specified chassis.   
**Step 2** |  UCS-A /chassis/server #  scope CIMC |  Enters chassis server CIMC mode   
**Step 3** |  UCS-A /chassis/server/CIMC #  reset |  Resets the CIMC for the blade server.   
**Step 4** |  UCS-A /chassis/server/CIMC #  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example resets the CIMC for blade server 4 in chassis 2 and commits the transaction: 
    
    
    UCS-A# **scope server 2/4**
    UCS-A /chassis/server # **scope CIMC**
    UCS-A /chassis/server/cimc # **reset**
    UCS-A /chassis/server/cimc* # **commit-buffer**
    UCS-A /chassis/server/cimc #  
    

## Clearing TPM for a Blade Server 

You can clear TPM only on Cisco UCS M4 blade and rack-mount servers that include support for TPM. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Clearing TPM is a potentially hazardous operation. The OS may stop booting. You may also see loss of data. 

* * *  
  
---|---  
  
### Before you begin

TPM must be enabled. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope server [chassis-num/server-num | dynamic-uuid]  |  Enters server mode for the specified server.   
**Step 2** |  UCS-A# /chassis/server # scope tpm tpm-ID |  Enters org TPM mode for the specified TPM.   
**Step 3** |  UCS-A# /chassis/server/tpm # set adminaction clear-config |  Specifies that the TPM is to be cleared.   
**Step 4** |  UCS-A# /chassis/server/tpm # commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example shows how to clear TPM for a blade server: 
    
    
    UCS-A# **scope server 1/3**
    UCS-A# /chassis/server # **scope tpm 1**
    UCS-A# /chassis/server/tpm # **set adminaction clear-config**
    UCS-A#/chassis/server/tpm* # **commit-buffer**
    
    
    
    

## Resetting the BIOS Password for a Blade Server

This option allows you to reset the BIOS password without using the F2 BIOS configuration prompt. Resetting the BIOS password is not part of the normal maintenance of a server. After the BIOS password reset, the server is rebooted immediately and the new BIOS password gets updated. 

### Procedure

* * *

**Step 1** |  UCS-A#  scope server ` ` chassis-num / server-num Enters chassis server mode for the specified chassis.   
---|---  
**Step 2** |  UCS-A /chassis/server #  reset-bios-password Resets the BIOS password for the blade server.   
**Step 3** |  UCS-A /chassis/server #  commit-buffer Commits the transaction to the system configuration.   
  
* * *

## Issuing an NMI from a Blade Server 

Perform the following procedure if the system remains unresponsive and you need Cisco UCS Manager to issue a Non-Maskable Interrupt (NMI) to the BIOS or operating system from the CIMC. This action creates a core dump or stack trace, depending on the operating system installed on the server. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope server [chassis-num/server-num | dynamic-uuid]  |  Enters server mode for the specified server.   
**Step 2** |  UCS-A /chassis/server # diagnostic-interrupt |   
**Step 3** |  UCS-A /chassis/server* # commit-buffer |  Commits any pending transactions.   
  
### Example

The following example sends an NMI from server 4 in chassis 2 and commits the transaction: 
    
    
    UCS-A# **scope server 2/4**
    UCS-A /chassis/server # **diagnostic-interrupt**
    UCS-A /chassis/server* # **commit-buffer**
    UCS-A /chassis/server # 
    

## Health LED Alarms

The blade health LED is located on the front of each Cisco UCS B-Series blade server. Cisco UCS Manager allows you to view the sensor faults that cause the blade health LED to change color from green to amber or blinking amber. 

The health LED alarms display the following information:

Name  | Description   
---|---  
Severity column |  The severity of the alarm. This can be one of the following:

  * Critical—The blade health LED is blinking amber. 
  * Minor—The blade health LED is amber. 

  
Description column |  A brief description of the alarm.  
Sensor ID column |  The ID of the sensor the triggered the alarm.  
Sensor Name column |  The name of the sensor that triggered the alarm.  
  
## Smart SSD

Beginning with release 3.1(3), Cisco UCS Manager supports monitoring SSD health. This feature is called Smart SSD. It provides statistical information about the properties like wear status in days, percentage life remaining, and so on. For every property, a minimum, a maximum and an average value is recorded and displayed. The feature also allows you to provide threshold limit for the properties. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The Smart SSD feature is supported only for a selected range of SSDs. It is not supported for any HDDs. 

* * *  
  
---|---  
  
The SATA range of supported SSDs are: 

  * Intel

  * Samsung 

  * Micron 


The SAS range of supported SSDs are: 

  * Toshiba 

  * Sandisk 

  * Samsung 

  * Micron 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

  * Power Cycle Count is not available on SAS SSDs. 
  * Smart SSD feature is supported only on M5 servers and later. 


* * *  
  
---|---  
  
  * Viewing SSD Health Statistics


### Viewing SSD Health Statistics 

Perform this procedure to view the SSD Health statistics. 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server chassis-id / server-id |  Enters chassis server mode for the specified server.   
**Step 2** |  UCS-A /chassis/server #  show stats |  Displays the SSD health statistics for the specified server.   
  
#### Example

The following example displays the SSD health statistics for blade 3 in chassis 1: 
    
    
    UCS-A# **scope server 1/3**
    UCS-A /chassis/server # **show stats**
    
    Ssd Health Stats:
        Time Collected: 2016-12-07T19:35:15.920
        Monitored Object: sys/chassis-1/blade-3/board/storage-SAS-1/ssd-health-stats-1
        Suspect: No
        Id: 1
        Power Cycle Count: 1022
        Power On Hours: 4793
        Percentage Life Left: 92
        Wear Status In Days: 1679
        Thresholded: 0
    
        Time Collected: 2016-12-07T19:35:38.912
        Monitored Object: sys/chassis-1/blade-3/board/storage-SAS-1/ssd-health-stats-2
        Suspect: No
        Id: 2
        Power Cycle Count: 1017
        Power On Hours: 4270
        Percentage Life Left: 87
        Wear Status In Days: 1587
        Thresholded: 0
    
        Time Collected: 2016-12-07T19:35:15.920
        Monitored Object: sys/chassis-1/blade-3/board/storage-SAS-4/ssd-health-stats-1
        Suspect: No
        Id: 1
        Power Cycle Count: 1506
        Power On Hours: 5029
        Percentage Life Left: 98
        Wear Status In Days: 1788
        Thresholded: 0
            
        Time Collected: 2016-12-07T19:35:15.920
        Monitored Object: sys/chassis-1/blade-3/board/storage-SAS-4/ssd-health-stats-2
        Suspect: No
        Id: 2
        Power Cycle Count: 58
        Power On Hours: 4731
        Percentage Life Left: 100
        Wear Status In Days: 1825
        Thresholded: 0
    UCS-A /chassis/server #
    
    

## Data Sanitization

Beginning with release 4.3(4a), Cisco UCS Manager supports data sanitization feature. Using the data sanitization process, Cisco UCS Manager erases all sensitive data, thus making extraction or recovery of data impossible. As Cisco UCS Manager progresses through the erase process, the status report is updated. You can check the status and progress of the data sanitization process for each individual device erase from the report, identify and rectify any issues, if required. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

  * You must perform data sanitization on the components that contain data.
  * This feature is supported on all the Cisco UCS C-Series, B-Series, and X-Series servers.


* * *  
  
---|---  
  
Erase process for data sanitization is performed in the following order on the server components:

  * Storage components

  * Network adapters

  * NVDIMMs

  * BIOS and BMC components


You can choose to either perform data sanitization on all the server components or select only VIC and Storage components for data sanitization. During the data sanitization process, the Cisco UCS server reboots and is subsequently decommissioned after the sanitization is finalized. In the event that the sanitization process is interrupted because of any issue, you must troubleshoot and resolve the issue and then recommence the data sanitization procedure. 

  * Performing Data Sanitization on Blade Servers
  * Performing Data Sanitization on Rack Servers


### Performing Data Sanitization on Blade Servers

Data sanitization may take several hours to finish depending on the amount of data. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

You cannot perform any other server operation while data sanitization is in progress.

* * *  
  
---|---  
  
#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server chassis-num/server-num |  Enters chassis server mode for the specified server.   
**Step 2** |  UCS-A /chassis/server # data-sanitize  all|board|host |  Performs the selected data sanitization.

  * Host—Storage components, network adapters, NVDIMMs
  * Board—BIOS and BMC components
  * All—Includes both the host and board components.

  
**Step 3** |  UCS-A /chassis/server* # commit buffer  |   
  
#### Example

Following example performs host data sanitization for server 4 in chassis 2:
    
    
    UCS-A # scope server 2/4
    UCS-A /chassis/server # data sanitize host
    Warning: Data sanitization is a destructive and long-running operation. Data on                                                                     the selected component will be completely erased.
    Warning: The server will be decommissioned on successful data sanitization.
    UCS-A /chassis/server* # commit buffer
    UCS-A /chassis/server #

---

## Page 11: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_4_3/b_UCSM_CLI_Infrastructure_Management_Guide_chapter_01001.html

# Rack Server Hardware Management

  * Rack-Mount Server Management
  * Rack-Enclosure Server Management
  * Guidelines for Removing and Decommissioning Rack-Mount Servers
  * Recommendations for Avoiding Unexpected Server Power Changes
  * Booting a Rack-Mount Server
  * Shutting Down a Rack-Mount Server
  * Resetting a Rack-Mount Server to Factory Default Settings
  * Performing Persistent Memory Scrub
  * Power Cycling a Rack-Mount Server
  * Performing a Hard Reset on a Rack-Mount Server
  * Acknowledging a Rack-Mount Server
  * Decommissioning a Rack-Mount Server
  * Recommissioning a Rack-Mount Server
  * Renumbering a Rack-Mount Server
  * Removing a Rack-Mount Server
  * Turning On the Locator LED for a Rack-Mount Server
  * Turning Off the Locator LED for a Rack-Mount Server
  * Resetting the CMOS for a Rack-Mount Server
  * Resetting the CIMC for a Rack-Mount Server
  * Clearing TPM for a Rack-Mount Server
  * Resetting the BIOS Password for a Rack-Mount Server
  * Showing the Status for a Rack-Mount Server
  * Issuing an NMI from a Rack-Mount Server
  * Viewing the Power Transition Log
  * Viewing Rack Enclosure Slot Statistics
  * Data Sanitization


## Rack-Mount Server Management 

You can manage and monitor all rack-mount servers that are integrated with a Cisco UCS domain through Cisco UCS Manager. All management and monitoring features are supported for rack-mount servers except power capping. Some rack-mount server management tasks, such as changes to the power state, can be performed from both the server and service profile. The remaining management tasks can only be performed on the server. 

Cisco UCS Manager provides information, errors, and faults for each rack-mount server that it has discovered. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/tip.gif)  
**Tip** | 

* * *

For information on how to integrate a supported Cisco UCS rack-mount server with Cisco UCS Manager, see the Cisco UCS C-series server integration guide or Cisco UCS S-series server integration guide for your Cisco UCS Manager release. 

* * *  
  
---|---  
  
## Rack-Enclosure Server Management

Beginning with release 4.0(1a), Cisco UCS Manager extends support for all existing features on Cisco UCS C125 M5 Servers unless specifically noted in this guide. 

Cisco UCS C125 M5 Servers are housed in the Cisco UCS C4200 Series Rack Server Chassis. Each Cisco UCS C4200 Series Rack Server Chassis supports up to four Cisco UCS C125 M5 Server nodes. To manage the Cisco UCS C125 M5 Server nodes, Cisco UCS Manager supports `rack-enclosure` object in CLI. 

Rack enclosures can be scoped using the CLI interface. For example:

UCS-A # scope `rack-enclosure 1`

You can scope `rack-enclosure` for the following: 

  * fan-module

  * psu

  * slot


fan-module and psu can be managed the same way as other rack servers. For slot, see Viewing Rack Enclosure Slot Statistics. 

You can also use the `show` command to view the following in `rack-enclosure`: 

  * detail

  * event

  * expand

  * fan-module

  * fault

  * fsm

  * psu

  * slot

  * stats


## Guidelines for Removing and Decommissioning Rack-Mount Servers

Consider the following guidelines when deciding whether to remove or decommission a rack-mount server using Cisco UCS Manager: 

### Decommissioning a Rack-Mount server

Decommissioning is performed when a rack-mount server is physically present and connected but you want to temporarily remove it from the configuration. Because it is expected that a decommissioned rack-mount server will be eventually recommissioned, a portion of the server's information is retained by Cisco UCS Manager for future use. 

### Removing a Rack-Mount server

Removing is performed when you physically remove the server from the system by disconnecting the rack-mount server from the fabric extender. You cannot remove a rack-mount server from Cisco UCS Manager if it is physically present and connected to the fabric extender. Once the rack-mount server is disconnected, the configuration for that rack-mount server can be removed in Cisco UCS Manager. 

During removal, management interfaces are disconnected, all entries from databases are removed, and the server is automatically removed from any server pools that it was assigned to during discovery. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Only those servers added to a server pool automatically during discovery will be removed automatically. Servers that have been manually added to a server pool have to be removed manually. 

* * *  
  
---|---  
  
If you need to add a removed rack-mount server back to the configuration, it must be reconnected and then rediscovered. When a server is reintroduced to Cisco UCS Manager it is treated like a new server and is subject to the deep discovery process. For this reason, it's possible that Cisco UCS Manager will assign the server a new ID that may be different from the ID that it held before. 

## Recommendations for Avoiding Unexpected Server Power Changes 

If a server is not associated with a service profile, you can use any available means to change the server power state, including the physical `Power` or `Reset` buttons on the server. 

If a server is associated with, or assigned to, a service profile, you should only use the following methods to change the server power state: 

  * In Cisco UCS Manager GUI, go to the General tab for the server or the service profile associated with the server and select Boot Server or Shutdown Server from the Actions area. 

  * In Cisco UCS Manager CLI, scope to the server or the service profile associated with the server and use the power up or power down commands. 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

Do _not_ use any of the following options on an associated server that is currently powered off: 

  * Reset in the GUI 
  * cycle cycle-immediate or reset hard-reset-immediate in the CLI 
  * The physical `Power` or `Reset` buttons on the server 


* * *  
  
---|---  
  
If you reset, cycle, or use the physical power buttons on a server that is currently powered off, the server's actual power state might become out of sync with the desired power state setting in the service profile. If the communication between the server and Cisco UCS Manager is disrupted or if the service profile configuration changes, Cisco UCS Manager might apply the desired power state from the service profile to the server, causing an unexpected power change. 

Power synchronization issues can lead to an unexpected server restart, as shown below: 

Desired Power State in Service Profile  |  Current Server Power State  |  Server Power State After Communication Is Disrupted   
---|---|---  
Up  |  Powered Off  |  Powered On   
Down  |  Powered On  |  Powered On  |  **Note** |  Running servers are not shut down regardless of the desired power state in the service profile.   
---|---  
  
## Booting a Rack-Mount Server

### Before you begin

Associate a service profile with a rack-mount server.

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope org ` ` org-name |  Enters organization mode for the specified organization. To enter the root organization mode, type  / as the  org-name .   
**Step 2** |  UCS-A /org #  scope service-profile ` ` profile-name |  Enters organization service profile mode for the specified service profile.   
**Step 3** |  UCS-A /org/service-profile #  power up |  Boots the rack-mount server associated with the service profile.  
**Step 4** |  UCS-A /org/service-profile #  commit-buffer |  Commits the transaction to the system configuration.  
  
### Example

The following example boots the rack-mount server associated with the service profile named ServProf34 and commits the transaction:
    
    
    UCS-A# **scope org /**
    UCS-A /org* # **scope service-profile ServProf34**
    UCS-A /org/service-profile # **power up**
    UCS-A /org/service-profile* # **commit-buffer**
    UCS-A /org/service-profile #
    

## Shutting Down a Rack-Mount Server

When you use this procedure to shut down a server with an installed operating system, Cisco UCS Manager triggers the OS into a graceful shutdown sequence. 

### Before you begin

Associate a service profile with a rack-mount server.

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope org ` ` org-name |  Enters organization mode for the specified organization. To enter the root organization mode, type / as the org-name.   
**Step 2** |  UCS-A /org #  scope service-profile ` ` profile-name |  Enters organization service profile mode for the specified service profile.   
**Step 3** |  UCS-A /org/service-profile #  power down |  Shuts down the rack-mount server associated with the service profile.  
**Step 4** |  UCS-A /org/service-profile #  commit-buffer |  Commits the transaction to the system configuration.  
  
### Example

The following example shuts down the rack-mount server associated with the service profile named ServProf34 and commits the transaction: 
    
    
    UCS-A# **scope org /**
    UCS-A /org # **scope service-profile ServProf34**
    UCS-A /org/service-profile # **power down**
    UCS-A /org/service-profile* # **commit-buffer**
    UCS-A /org/service-profile #
    

## Resetting a Rack-Mount Server to Factory Default Settings 

You can now reset a rack-mount server to its factory settings. By default, the factory reset operation does not affect storage, including storage drives and flexflash drives. This is to prevent any loss of data. However, you can choose to reset these devices to a known state as well. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

Resetting storage devices will result in loss of data. 

* * *  
  
---|---  
  
Perform the following procedure if you need to reset the server to factory default settings. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope server server-num |  Enters server mode for the specified rack-mount server.   
**Step 2** |  UCS-A /server # reset factory-default [delete-flexflash-storage | delete-storage [create-initial-storage-volumes] ]  |  Resets server settings to factory default using the following command options: 

  * factory-default —Resets the server to factory defaults without deleting storage 
  * delete-flexflash-storage —Resets the server to factory defaults and deletes flexflash storage 
  * delete-storage —Resets the server to factory defaults and deletes all storage 
  * create-initial-storage-volumes —Resets the server to factory defaults, deletes all storage, sets all disks to their initial state  |  **Important** |  Do not use the create-initial-storage-volumes command option if you want to use storage profiles. Creating initial volumes when you are using storage profiles may result in configuration errors.   
---|---  

  
**Step 3** |  UCS-A /server # commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example resets the server settings to factory default without deleting storage, and commits the transaction: 
    
    
    UCS-A# **scope server 2**
    UCS-A /server # **reset factory-default**
    UCS-A /server* # **commit-buffer**
    UCS-A /server #
    
     
    

The following example resets the server settings to factory default, deletes flexflash storage, and commits the transaction: 
    
    
    UCS-A# **scope server 2**
    UCS-A /server # **reset factory-default delete-flexflash-storage**
    UCS-A /server* # **commit-buffer**
    
    
    

The following example resets the server settings to factory default, deletes all storage, and commits the transaction: 
    
    
    UCS-A# **scope server 2**
    UCS-A /server # **reset factory-default delete-storage**
    UCS-A /server* # **commit-buffer**
    

The following example resets the server settings to factory default, deletes all storage, sets all disks to their initial state, and commits the transaction: 
    
    
    UCS-A# **scope server 2**
    UCS-A /server # **reset factory-default delete-storage create-initial-storage-volumes**
    UCS-A /server* # **commit-buffer**

## Performing Persistent Memory Scrub

In Cisco UCS Manager, you can scrub persistent memory by using one of the following methods:

  * Disassociating the Service Profile and the Scrub Policy with Persistent Memory Scrub Selected

  * Resetting a Server to Factory Defaults With Persistent Memory Scrub Selected

  * Deleting a Goal


## Power Cycling a Rack-Mount Server

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server ` ` server-num |  Enters server mode for the specified rack-mount server.  
**Step 2** |  UCS-A /server #  cycle ` `{cycle-immediate | cycle-wait}  |  Power cycles the rack-mount server. Use the  cycle-immediate keyword to immediately begin power cycling the rack-mount server; use the  cycle-wait keyword to schedule the power cycle to begin after all pending management operations have completed.   
**Step 3** |  UCS-A#  commit-buffer |  Commits the transaction to the system configuration.  
  
### Example

The following example immediately power cycles rack-mount server 2 and commits the transaction:
    
    
    UCS-A# **scope server 2**
    UCS-A /server # **cycle cycle-immediate**
    UCS-A /server* # **commit-buffer**
    UCS-A /server # 
    

## Performing a Hard Reset on a Rack-Mount Server

When you reset a server, Cisco UCS Manager sends a pulse on the reset line. You can choose to gracefully shut down the operating system. If the operating system does not support a graceful shutdown, the server is power cycled. The option to have Cisco UCS Manager complete all management operations before it resets the server does not guarantee the completion of these operations before the server is reset. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

If you are trying to boot a server from a power-down state, you should not use Reset.  If you continue the power-up with this process, the desired power state of the servers become out of sync with the actual power state and the servers might unexpectedly shut down at a later time. To safely reboot the selected servers from a power-down state, click Cancel, then select the Boot Server action. 

* * *  
  
---|---  
  
### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server ` ` server-num |  Enters server mode for the specified rack-mount server.  
**Step 2** |  UCS-A /server #  reset ` `{hard-reset-immediate | hard-reset-wait}  |  Performs a hard reset of the rack-mount server. Use the hard-reset-immediate keyword to immediately begin hard resetting the rack-mount server; use the hard-reset-wait keyword to schedule the hard reset to begin after all pending management operations have completed.   
**Step 3** |  UCS-A /server #  commit-buffer |  Commits the transaction to the system configuration.  
  
### Example

The following example performs an immediate hard reset of rack-mount server 2 and commits the transaction:
    
    
    UCS-A#  scope server 2
    UCS-A /server # reset hard-reset-immediate
    UCS-A /server* # commit-buffer
    UCS-A /server # 
    

## Acknowledging a Rack-Mount Server

Perform the following procedure to rediscover the server and all endpoints in the server. For example, you can use this procedure if a server is stuck in an unexpected state, such as the discovery state. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  acknowledge server ` ` server-num |  Acknowledges the specified rack-mount server.  
**Step 2** |  UCS-A#  commit-buffer |  Commits the transaction to the system configuration.  
  
### Example

The following example acknowledges rack-mount server 2 and commits the transaction:
    
    
    UCS-A# **acknowledge server 2**
    UCS-A* # **commit-buffer**
    UCS-A # 
    

## Decommissioning a Rack-Mount Server

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  decommission server ` ` server-num |  Decommissions the specified rack-mount server.  
**Step 2** |  UCS-A#  commit-buffer |  Commits the transaction to the system configuration.  
  
### Example

The following example decommissions rack-mount server 2 and commits the transaction:
    
    
    UCS-A# decommission server 2
    UCS-A* # commit-buffer
    UCS-A # 
    

### What to do next

After decommissioning the rack-mount server, you must wait for few minutes to initiate the recommissioning of the server.

For more information, see Recommissioning a Rack-Mount Server

## Recommissioning a Rack-Mount Server

### Before you begin

Incase of recommissioning a rack-mount server after decommission, you should wait for few minutes to initiate the recommission of the server. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  recommission server ` ` server-num |  Recommissions the specified rack-mount server.  
**Step 2** |  UCS-A#  commit-buffer |  Commits the transaction to the system configuration.  
  
### Example

The following example recommissions rack-mount server 2 and commits the transaction:
    
    
    UCS-A# recommission server 2
    UCS-A* # commit-buffer
    UCS-A # 
    

## Renumbering a Rack-Mount Server

### Before you begin

If you are swapping IDs between servers, you must first decommission both servers, then wait for the server decommission FSM to complete before proceeding with the renumbering steps. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  show server inventory |  Displays information about your servers.  
**Step 2** |  Verify that the server inventory does not include the following: | 

  * The rack-mount server you want to renumber
  * A rack-mount server with the number you want to use

If either of these rack-mount servers are listed in the server inventory, decommission those servers. You must wait until the decommission FSM is complete and the rack-mount servers are not listed in the server inventory before continuing. This might take several minutes.  To see which servers have been decommissioned, issue the show server decommissioned command.   
**Step 3** |  UCS-A#  recommission server ` ` vendor-name model-name serial-numnew-id |  Recommissions and renumbers the specified rack-mount server.  
**Step 4** |  UCS-A#  commit-buffer |  Commits the transaction to the system configuration.  
  
### Example

The following example decommissions a rack-mount server with ID 2, changes the ID to 3, recommissions that server, and commits the transaction: 
    
    
    UCS-A# **show server inventory**
    
    Server  Equipped PID Equipped VID Equipped Serial (SN) Slot Status      Ackd Memory (MB) Ackd Cores
    ------- ------------ ------------ -------------------- ---------------- ---------------- ----------
    1/1     UCSB-B200-M4 V01          FCH1532718P          Equipped         131072           16
    1/2     UCSB-B200-M4 V01          FCH153271DF          Equipped         131072           16
    1/3     UCSB-B200-M4 V01          FCH153271DL          Equipped         114688           16
    1/4     UCSB-B200-M4 V01                               Empty
    1/5                                                    Empty
    1/6                                                    Empty
    1/7     N20-B6730-1  V01          JAF1432CFDH          Equipped         65536            16
    1/8                                                    Empty
    1       R200-1120402W V01          QCI1414A02J          N/A             49152            12
    2       R210-2121605W V01          QCI1442AHFX          N/A             24576            8
    4       UCSC-BSE-SFF-C200 V01      QCI1514A0J7          N/A             8192             8
    
    UCS-A# **decommission server 2**
    UCS-A*# **commit-buffer**
    UCS-A# **show server decommissioned**
    
    Vendor            Model         Serial (SN) Server
    ----------------- ----------    ----------- ------
    Cisco Systems Inc R210-2121605W QCI1442AHFX 2
    
    UCS-A# **recommission chassis "Cisco Systems Inc" "R210-2121605W" QCI1442AHFX 3**
    UCS-A* # **commit-buffer**
    UCS-A # **show server inventory**
    
    Server  Equipped PID Equipped VID Equipped Serial (SN) Slot Status      Ackd Memory (MB) Ackd Cores
    ------- ------------ ------------ -------------------- ---------------- ---------------- ----------
    1/1     UCSB-B200-M4 V01          FCH1532718P          Equipped         131072           16
    1/2     UCSB-B200-M4 V01          FCH153271DF          Equipped         131072           16
    1/3     UCSB-B200-M4 V01          FCH153271DL          Equipped         114688           16
    1/4     UCSB-B200-M4 V01                               Empty
    1/5                                                    Empty
    1/6                                                    Empty
    1/7     N20-B6730-1  V01          JAF1432CFDH          Equipped         65536            16
    1/8                                                    Empty
    1       R200-1120402W V01          QCI1414A02J          N/A             49152            12
    3       R210-2121605W V01          QCI1442AHFX          N/A             24576            8
    4       UCSC-BSE-SFF-C200 V01      QCI1514A0J7          N/A             8192             8
    
    

## Removing a Rack-Mount Server 

### Before you begin

Physically disconnect the CIMC LOM cables that connect the rack-mount server to the fabric extender before performing the following procedure. For high availability setups, remove both cables. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  remove server` `server-num |  Removes the specified rack-mount server.   
**Step 2** |  UCS-A#  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example removes rack-mount server 4 and commits the transaction: 
    
    
    UCS-A#  remove server 4
    UCS-A* # commit-buffer
    UCS-A # 
    

### What to do next

If you physically reconnect the rack-mount server, you must re-acknowledge it for the Cisco UCS Manager to rediscover the server. 

For more information, see Acknowledging a Rack-Mount Server. 

## Turning On the Locator LED for a Rack-Mount Server

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server ` ` server-num |  Enters server mode for the specified rack-mount server.  
**Step 2** |  UCS-A /server #  enable locator-led ` ` |  Turns on the rack-mount server locator LED.  
**Step 3** |  UCS-A /server #  commit-buffer |  Commits the transaction to the system configuration.  
  
### Example

The following example turns on the locator LED for rack-mount server 2 and commits the transaction:
    
    
    UCS-A# scope server 2
    UCS-A /server # enable  locator-led
    UCS-A /server* # commit-buffer
    UCS-A /server # 
    

## Turning Off the Locator LED for a Rack-Mount Server

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server ` ` server-num |  Enters server mode for the specified rack-mount server.  
**Step 2** |  UCS-A /server #  disable locator-led ` ` |  Turns off the rack-mount server locator LED.  
**Step 3** |  UCS-A /server #  commit-buffer |  Commits the transaction to the system configuration.  
  
### Example

The following example turns off the locator LED for rack-mount server 2 and commits the transaction:
    
    
    UCS-A# scope server 2
    UCS-A /server # disable  locator-led
    UCS-A /server* # commit-buffer
    UCS-A /server # 
    

## Resetting the CMOS for a Rack-Mount Server

Sometimes, troubleshooting a server might require you to reset the CMOS. Resetting the CMOS is not part of the normal maintenance of a server. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server ` ` server-num |  Enters server mode for the rack-mount server.  
**Step 2** |  UCS-A /server #  reset-cmos |  Resets the CMOS for the rack-mount server.  
**Step 3** |  UCS-A /server #  commit-buffer |  Commits the transaction to the system configuration.  
  
### Example

The following example resets the CMOS for rack-mount server 2 and commits the transaction:
    
    
    UCS-A# **scope server 2**
    UCS-A /server # **reset-cmos**
    UCS-A /server* # **commit-buffer**
    UCS-A /server #  
    

## Resetting the CIMC for a Rack-Mount Server

Sometimes, with the firmware, troubleshooting a server might require you to reset the CIMC. Resetting the CIMC is not part of the normal maintenance of a server. After you reset the CIMC, the CIMC reboots the management controller of the blade server. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server ` ` server-num |  Enters server mode for the specified rack-mount server.  
**Step 2** |  UCS-A /server #  scope CIMC |  Enters server CIMC mode  
**Step 3** |  UCS-A /server/CIMC #  reset |  Resets the CIMC for the rack-mount server.  
**Step 4** |  UCS-A /server/CIMC #  commit-buffer |  Commits the transaction to the system configuration.  
  
### Example

The following example resets the CIMC for rack-mount server 2 and commits the transaction:
    
    
    UCS-A# **scope server 2**
    UCS-A /server # **scope CIMC**
    UCS-A /server/cimc # **reset**
    UCS-A /server/cimc* # **commit-buffer**
    UCS-A /server/cimc #  
    

## Clearing TPM for a Rack-Mount Server 

You can clear TPM only on Cisco UCS M4 blade and rack-mount servers that include support for TPM. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Clearing TPM is a potentially hazardous operation. The OS may stop booting. You may also see loss of data. 

* * *  
  
---|---  
  
### Before you begin

TPM must be enabled. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope server server-num |  Enters server mode for the rack-mount server.   
**Step 2** |  UCS-A# /server # scope tpm tpm-ID |  Enters org TPM mode for the specified TPM.   
**Step 3** |  UCS-A# /server/tpm # set adminaction clear-config |  Specifies that the TPM is to be cleared.   
**Step 4** |  UCS-A# /server/tpm # commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example shows how to clear TPM for a rack-mount server: 
    
    
    UCS-A# **scope server 3**
    UCS-A# /server # **scope tpm 1**
    UCS-A# /server/tpm # **set adminaction clear-config**
    UCS-A# /server/tpm* # **commit-buffer**
    
    
    
    

## Resetting the BIOS Password for a Rack-Mount Server

This option allows you to reset the BIOS password without using the F2 BIOS configuration prompt. Resetting the BIOS password is not part of the normal maintenance of a server. After the BIOS password reset, the server is rebooted immediately and the new BIOS password gets updated. 

### Procedure

* * *

**Step 1** |  UCS-A#  scope server ` ` server-num Enters chassis server mode for the specified chassis.   
---|---  
**Step 2** |  UCS-A /chassis/server #  reset-bios-password Resets the BIOS password for the rack-mount server.   
**Step 3** |  UCS-A /chassis/server #  commit-buffer Commits the transaction to the system configuration.   
  
* * *

## Showing the Status for a Rack-Mount Server

### Procedure

Command or Action | Purpose  
---|---  
UCS-A# show server status |  Shows the status for all servers in the Cisco UCS domain.   
  
### Example

The following example shows the status for all servers in the Cisco UCS domain. The servers numbered 1 and 2 do not have a slot listed in the table because they are rack-mount servers. 
    
    
    Server Slot  Status    Availability  Overall Status  Discovery
    --------------------------------------------------------------------
    1/1          Equipped  Unavailable   Ok              Complete  
    1/2          Equipped  Unavailable   Ok              Complete  
    1/3          Equipped  Unavailable   Ok              Complete  
    1/4          Empty     Unavailable   Ok              Complete  
    1/5          Equipped  Unavailable   Ok              Complete  
    1/6          Equipped  Unavailable   Ok              Complete  
    1/7          Empty     Unavailable   Ok              Complete  
    1/8          Empty     Unavailable   Ok              Complete
    1            Equipped  Unavailable   Ok              Complete 
    2            Equipped  Unavailable   Ok              Complete 
    

## Issuing an NMI from a Rack-Mount Server

Perform the following procedure if the system remains unresponsive and you need Cisco UCS Manager to issue a Non-Maskable Interrupt (NMI) to the BIOS or operating system from the CIMC. This action creates a core dump or stack trace, depending on the operating system installed on the server. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope server [chassis-num/server-num | dynamic-uuid]  |  Enters server mode for the specified server.   
**Step 2** |  UCS-A /chassis/server # diagnostic-interrupt |   
**Step 3** |  UCS-A /chassis/server* # commit-buffer |  Commits any pending transactions.   
  
### Example

The following example sends an NMI from server 4 in chassis 2 and commits the transaction:
    
    
    UCS-A# **scope server 2/4**
    UCS-A /chassis/server # **diagnostic-interrupt**
    UCS-A /chassis/server* # **commit-buffer**
    UCS-A /chassis/server # 
    

## Viewing the Power Transition Log

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope server server-num |  Enters server mode for the rack-mount server.   
**Step 2** |  UCS-A# /chassis/server # show power-transition-log |  Displays the computeRebootLog instances for the specified server.   
  
### Example

The following example shows how to view the power transition log for server 3. 
    
    
    UCS-A# **scope server 3**
    UCS-A# /chassis/server # **show power-transition-log**
    
    
    Last 5 server reboots (Newest first):
     
    Pwr Change Source              	Last pwr transition timestamp
    ------------------------------ 	-----------------------------
    UCSM TURNUP                    	2016-10-28T09:35:04.498
    HOST PWR TRANSITION            	2016-10-27T17:06:56.157
    UCSM TURNUP                    	2016-10-27T17:06:24.734
    UCSM ASSOCIATE                 	2016-10-27T17:06:24.068
    UCSM SERVER DISCOVER          	2016-10-27T16:56:56.153

## Viewing Rack Enclosure Slot Statistics

You can see the stats for server slot in the rack enclosure housing the C125 M5 Servers. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope rack-enclosure  rack-enclosure -num |  Enters the rack-enclosure.   
**Step 2** |  UCS-A# /rack-enclosure # show slot  |  Displays the slot stats.  
**Step 3** |  UCS-A# /rack-enclosure # scope slot slot_ID |  Enters the slot.  
**Step 4** |  UCS-A# /rack-enclosure/slot # show detail |  Displays the following stats:

  * Id
  * Slot Type
  * Presence State
  * Server ID
  * Server DN
  * Current Task

  
  
### Example

The following example shows how to view slot stats in for an enclosure and individual slot stats: 
    
    
    UCS-A# **scope rack-enclosure 1**
    UCS-A /rack-enclosure # **show slot**
    UCS-A /rack-enclosure # show slot
    
    Slot:
        Id         Presence State
        ---------- --------------
                 1 Equipped
                 2 Empty
                 3 Equipped
                 4 Empty
    UCS-A /rack-enclosure # scope slot 1
    UCS-A /rack-enclosure/slot # show detail
    
    Slot:
        Id: 1
        Slot Type: Compute
        Presence State: Equipped
        Server ID: 4
        Server DN: sys/rack-unit-4
        Current Task:
    UCS-A /rack-enclosure/slot # 

## Data Sanitization

Beginning with release 4.3(4a), Cisco UCS Manager supports data sanitization feature. Using the data sanitization process, Cisco UCS Manager erases all sensitive data, thus making extraction or recovery of data impossible. As Cisco UCS Manager progresses through the erase process, the status report is updated. You can check the status and progress of the data sanitization process for each individual device erase from the report, identify and rectify any issues, if required. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

  * You must perform data sanitization on the components that contain data.
  * This feature is supported on all the Cisco UCS C-Series, B-Series, and X-Series servers.


* * *  
  
---|---  
  
Erase process for data sanitization is performed in the following order on the server components:

  * Storage components

  * Network adapters

  * NVDIMMs

  * BIOS and BMC components


You can choose to either perform data sanitization on all the server components or select only VIC and Storage components for data sanitization. During the data sanitization process, the Cisco UCS server reboots and is subsequently decommissioned after the sanitization is finalized. In the event that the sanitization process is interrupted because of any issue, you must troubleshoot and resolve the issue and then recommence the data sanitization procedure. 

  * Performing Data Sanitization on Blade Servers
  * Performing Data Sanitization on Rack Servers


### Performing Data Sanitization on Rack Servers

Data sanitization may take several hours to finish depending on the amount of data. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

You cannot perform any other server operation while data sanitization is in progress.

* * *  
  
---|---  
  
#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server server-num |  Enters server mode for the specified rack-mount server.  
**Step 2** |  UCS-A /server # data-sanitize  all|board|host |  Performs the selected data sanitization.

  * Host—Storage components, network adapters, NVDIMMs
  * Board—BIOS and BMC components
  * All—Includes both the host and board components.

  
**Step 3** |  UCS-A /server* # commit buffer  |   
  
#### Example

Following example performs host data sanitization for server 1:
    
    
    UCS-A # scope server 1
    UCS-A / server # data sanitize host
    Warning: Data sanitization is a destructive and long-running operation. Data on                                                                     the selected component will be completely erased.
    Warning: The server will be decommissioned on successful data sanitization.
    UCS-A / server* # commit buffer
    UCS-A / server #

---

## Page 12: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_4_3/b_UCSM_CLI_Infrastructure_Management_Guide_chapter_01010.html

# S3X60 Server Node Hardware Management

  * Cisco UCS S3260 Server Node Management
  * Booting a Server from the Service Profile
  * Acknowledging a Server
  * Power Cycling a Server
  * Shutting Down a Server
  * Performing a Hard Reset on a Server
  * Resetting a Cisco UCS S3260 Server Node to Factory Default Settings
  * Removing a Server from a Chassis
  * Decommissioning a Server
  * Recommissioning a Server
  * Turning On the Locator LED for a Server
  * Turning Off the Locator LED for a Server
  * Resetting All Memory Errors
  * Resetting IPMI to Factory Default Settings
  * Resetting the CIMC for a Server
  * Resetting the CMOS for a Server
  * Resetting the BIOS Password for a Cisco UCS S3260 Server Node
  * Resetting KVM
  * Issuing an NMI from a Server
  * Recovering a Corrupt BIOS
  * Health LED Alarms


## Cisco UCS S3260 Server Node Management 

You can manage and monitor all Cisco UCS S3260 server nodes in a Cisco UCS domain through Cisco UCS Manager. You can perform some server management tasks, such as changes to the power state, from the server and service profile. 

The remaining management tasks can only be performed on the server. 

If a server slot in a chassis is empty, Cisco UCS Manager provides information, errors, and faults for that slot. You can also re-acknowledge the slot to resolve server mismatch errors and rediscover the server in the slot. 

## Booting a Server from the Service Profile 

### Before you begin

Associate a service profile with a server or server pool. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope org ` ` org-name |  Enters organization mode for the specified organization. To enter the root organization mode, type  / as the  org-name .   
**Step 2** |  UCS-A /org #  scope service-profile ` ` profile-name |  Enters organization service profile mode for the specified service profile.   
**Step 3** |  UCS-A /org/service-profile #  power up |  Boots the server associated with the service profile.   
**Step 4** |  UCS-A /org/service-profile* #  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example boots the server associated with the service profile named ServProf34 and commits the transaction: 
    
    
    UCS-A# **scope org /**
    UCS-A /org # **scope service-profile ServProf34**
    UCS-A /org/service-profile # **power up**
    UCS-A /org/service-profile* # **commit-buffer**
    UCS-A /org/service-profile #
    

## Acknowledging a Server 

Perform the following procedure to rediscover the server and all endpoints in the server. For example, you can use this procedure if a server is stuck in an unexpected state, such as the discovery state. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  acknowledge server ` ` chassis-num / server-num |  Acknowledges the specified server.   
**Step 2** |  UCS-A*#  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example acknowledges server 1 in chassis 3 and commits the transaction: 
    
    
    UCS-A# **acknowledge server 3/1**
    UCS-A* # **commit-buffer**
    UCS-A # 
    

## Power Cycling a Server 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server ` ` chassis-num / server-num |  Enters chassis server mode for the specified server.   
**Step 2** |  UCS-A /chassis/server #  cycle ` `{cycle-immediate | cycle-wait}  |  Power cycles the server.  Use the  cycle-immediate keyword to immediately begin power cycling the server; use the  cycle-wait keyword to schedule the power cycle to begin after all pending management operations have completed.   
**Step 3** |  UCS-A /chassis/server* #  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example immediately power cycles server 1 in chassis 3 and commits the transaction: 
    
    
    UCS-A# **scope server 3/1**
    UCS-A /chassis/server # **cycle cycle-immediate**
    UCS-A /chassis/server* # **commit-buffer**
    UCS-A /chassis/server # 
    

## Shutting Down a Server 

When you use this procedure to shut down a server with an installed operating system, Cisco UCS Manager triggers the OS into a graceful shutdown sequence. 

### Before you begin

Associate a service profile with a server or server pool. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope org ` ` org-name |  Enters organization mode for the specified organization. To enter the root organization mode, type / as the org-name.   
**Step 2** |  UCS-A /org #  scope service-profile ` ` profile-name |  Enters organization service profile mode for the specified service profile.   
**Step 3** |  UCS-A /org/service-profile #  power down |  Shuts down the server associated with the service profile.   
**Step 4** |  UCS-A /org/service-profile* #  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example shuts down the server associated with the service profile named ServProf34 and commits the transaction: 
    
    
    UCS-A# **scope org /**
    UCS-A /org # **scope service-profile ServProf34**
    UCS-A /org/service-profile # **power down**
    UCS-A /org/service-profile* # **commit-buffer**
    UCS-A /org/service-profile #
    

## Performing a Hard Reset on a Server 

When you reset a server, Cisco UCS Manager sends a pulse on the reset line. You can choose to gracefully shut down the operating system. If the operating system does not support a graceful shutdown, the server is power cycled. The option to have Cisco UCS Manager complete all management operations before it resets the server does not guarantee the completion of these operations before the server is reset. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

If you are trying to boot a server from a power-down state, you should not use Reset.  If you continue the power-up with this process, the desired power state of the servers become out of sync with the actual power state and the servers might unexpectedly shut down at a later time. To safely reboot the selected servers from a power-down state, click Cancel, then select the Boot Server action. 

* * *  
  
---|---  
  
### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server ` ` chassis-num / server-num |  Enters chassis server mode for the specified server.   
**Step 2** |  UCS-A /chassis/server #  reset ` `{hard-reset-immediate | hard-reset-wait}  |  Performs a hard reset of the server.  Use the: 

  * hard-reset-immediate keyword to immediately begin hard resetting the server. 
  * hard-reset-wait keyword to schedule the hard reset to begin after all pending management operations have completed. 

  
**Step 3** |  UCS-A /server* #  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example performs an immediate hard reset of server 1 in chassis 3 and commits the transaction: 
    
    
    UCS-A#  scope server 3/1
    UCS-A /chassis/server # reset hard-reset-immediate
    UCS-A /chassis/server* # commit-buffer
    UCS-A /chassis/server # 
    

## Resetting a Cisco UCS S3260 Server Node to Factory Default Settings 

You can now reset a Cisco UCS S3260 Server Node to its factory settings. By default, the factory reset operation does not affect storage drives. This is to prevent any loss of data. However, you can choose to reset these devices to a known state as well. 

The following guidelines apply to Cisco UCS S3260 Server Nodes when using scrub policies: 

  * For Cisco UCS S3260 Server Nodes, you cannot delete storage by using the scrub policy. 

  * Cisco UCS S3260 Server Nodes do not support FlexFlash drives. 

  * For Cisco UCS S3260 Server Nodes, you can only reset the BIOS by using the scrub policy. 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

Resetting storage devices will result in loss of data. 

* * *  
  
---|---  
  
Perform the following procedure to reset the server to factory default settings. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope server chassis-num / server-num |  Enters chassis server mode for the specified server.   
**Step 2** |  UCS-A /chassis/server # reset factory-default [delete-flexflash-storage | delete-storage [create-initial-storage-volumes] ]  |  Resets server settings to factory default using the following command options: 

  * factory-default —Resets the server to factory defaults without deleting storage  |  **Note** |  This operation resets the BIOS.   
---|---  
  * delete-flexflash-storage —Resets the server to factory defaults and deletes flexflash storage 

**Note** |  This operation is not supported on Cisco UCS S3260 Server Nodes.   
---|---  
  * delete-storage —Resets the server to factory defaults and deletes all storage 

  * create-initial-storage-volumes —Resets the server to factory defaults, deletes all storage, sets all disks to their initial state 


  
**Step 3** |  UCS-A /chassis/server* # commit-buffer |  Commits any pending transactions.   
  
### Example

The following example resets the server settings to factory default without deleting storage, and commits the transaction: 
    
    
    UCS-A# **scope server 3/1**
    UCS-A /chassis/server # **reset factory-default**
    UCS-A /chassis/server* # **commit-buffer**
    
    
    

The following example resets the server settings to factory default, deletes flexflash storage, and commits the transaction: 
    
    
    UCS-A# **scope server 3/1**
    UCS-A /chassis/server # **reset factory-default delete-flexflash-storage**
    UCS-A /chassis/server* # **commit-buffer**
    
    
    

The following example resets the server settings to factory default, deletes all storage, and commits the transaction: 
    
    
    UCS-A# **scope server 3/1**
    UCS-A /chassis/server # **reset factory-default delete-storage**
    UCS-A /chassis/server* # **commit-buffer**
    
    

The following example resets the server settings to factory default, deletes all storage, sets all disks to their initial state, and commits the transaction: 
    
    
    UCS-A# **scope server 3/1**
    UCS-A /chassis/server # **reset factory-default delete-storage create-initial-storage-volumes**
    UCS-A /chassis/server* # **commit-buffer**
    
    

## Removing a Server from a Chassis 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  remove server ` ` chassis-num / server-num |  Removes the specified server.   
**Step 2** |  UCS-A*#  commit-buffer |  Commits the transaction to the system configuration.   
**Step 3** |  Go to the physical location of the chassis and remove the server hardware from the slot.  |  For instructions on how to remove the server hardware, see the Cisco UCS Hardware Installation Guide for your chassis.   
  
### Example

The following example removes server 1 in chassis 3 and commits the transaction: 
    
    
    UCS-A#  **remove server 3/1**
    UCS-A* # **commit-buffer**
    UCS-A # 
    

### What to do next

If you physically re-install the blade server, you must re-acknowledge the slot for the Cisco UCS Manager to rediscover the server. 

For more information, see Acknowledging a Server. 

## Decommissioning a Server 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  decommission server ` ` chassis-num / server-num |  Decommissions the specified server.   
**Step 2** |  UCS-A*#  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example decommissions server 1 in chassis 3 and commits the transaction: 
    
    
    UCS-A# decommission server 3/1
    UCS-A* # commit-buffer
    UCS-A # 
    

### What to do next

After decommissioning the server, you must wait for few minutes to initiate the recommissioning of the server.

For more information, see Recommissioning a Server

## Recommissioning a Server

### Before you begin

Incase of recommissioning the server after decommission, you should wait for few minutes to initiate the recommission of the server. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  recommission server ` ` chassis-num / server-num |  Recommissions the specified server.   
**Step 2** |  UCS-A*#  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example recommissions server 1 in chassis 3 and commits the transaction: 
    
    
    UCS-A# recommission server 3/1
    UCS-A* # commit-buffer
    UCS-A # 
    

## Turning On the Locator LED for a Server 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server ` ` chassis-num / server-num |  Enters chassis server mode for the specified chassis.   
**Step 2** |  UCS-A /chassis/server #  enable locator-led [multi-master | multi-slave]  |  Turns on the server locator LED. The following command options are not applicable to Cisco UCS S3260 Server Nodes: 

  * multi-master—Turns on the LED for the master node only. 
  * multi-slave—Turns on the LED for the slave node only. 

  
**Step 3** |  UCS-A /chassis/server* #  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example turns on the locator LED on server 1 in chassis 3 and commits the transaction: 
    
    
    UCS-A# scope server 3/1
    UCS-A /chassis/server # enable  locator-led
    UCS-A /chassis/server* # commit-buffer
    UCS-A /chassis/server # 
    
    

The following example turns on the locator LED for the master node only on server 1 in chassis 3 and commits the transaction: 
    
    
    UCS-A# scope chassis 3/1
    UCS-A /chassis/server # enable locator-led multi-master
    UCS-A /chassis/server* # commit-buffer
    UCS-A /chassis/server # 
    

## Turning Off the Locator LED for a Server 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server chassis-num / server-num |  Enters chassis mode for the specified chassis.   
**Step 2** |  UCS-A /chassis/server #  disable locator-led [multi-master | multi-slave]  |  Turns off the server locator LED. The following command options are not applicable to Cisco UCS S3260 Server Nodes: 

  * multi-master—Turns off the LED for the master node only. 
  * multi-slave—Turns off the LED for the slave node only. 

  
**Step 3** |  UCS-A /chassis/server* #  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example turns off the locator LED on server 1 in chassis 3 and commits the transaction: 
    
    
    UCS-A# scope chassis 3/1
    UCS-A /chassis/server # disable locator-led
    UCS-A /chassis/server* # commit-buffer
    UCS-A /chassis/server # 
    
    

The following example turns off the locator LED for the master node on server 1 in chassis 3 and commits the transaction: 
    
    
    UCS-A# scope chassis 3/1
    UCS-A /chassis/server # disable locator-led multi-master
    UCS-A /chassis/server* # commit-buffer
    UCS-A /chassis/server # 
    

## Resetting All Memory Errors 

Use this procedure to reset all correctable and uncorrectable memory errors encountered by . 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server ` ` chassis-num / server-num |  Enters chassis server mode for the specified server.   
**Step 2** |  UCS-A /chassis/server #  reset-all-memory-errors |  Performs a reset of the memory cards.   
**Step 3** |  UCS-A /chassis/server* #  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example performs an immediate hard reset of server 1 in chassis 3 and commits the transaction: 
    
    
    UCS-A#  scope server 3/1
    UCS-A /chassis/server # reset-all-memory-errors
    UCS-A /chassis/server* # commit-buffer
    UCS-A /chassis/server # 
    

## Resetting IPMI to Factory Default Settings 

Perform the following procedure if you need to reset IPMI to factory default settings. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope server chassis-num / server-num |  Enters chassis server mode for the specified server.   
**Step 2** |  UCS-A /chassis/server # reset-ipmi |  Resets IPMI settings to factory default.   
**Step 3** |  UCS-A /chassis/server* # commit-buffer |  Commits any pending transactions.   
  
### Example

The following example resets the IPMI settings to factory default and commits the transaction: 
    
    
    UCS-A# **scope server 3/1**
    UCS-A /chassis/server # **reset-ipmi**
    UCS-A /chassis/server* # **commit-buffer**
    UCS-A /chassis/server # 
    
    

## Resetting the CIMC for a Server 

Sometimes, with the firmware, troubleshooting a server might require you to reset the CIMC. Resetting the CIMC is not part of the normal maintenance of a server. After you reset the CIMC, the CIMC reboots the management controller of the blade server. 

If the CIMC is reset, the power monitoring functions of Cisco UCS become briefly unavailable until the CIMC reboots. Typically, the reset only takes 20 seconds; however, it is possible that the peak power cap can exceed during that time. To avoid exceeding the configured power cap in a low power-capped environment, consider staggering the rebooting or activation of CIMCs. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server ` ` chassis-num / server-num |  Enters chassis server mode for the specified chassis.   
**Step 2** |  UCS-A /chassis/server #  scope cimc |  Enters chassis server CIMC mode   
**Step 3** |  UCS-A /chassis/server/cimc #  reset |  Resets the CIMC for the server.   
**Step 4** |  UCS-A /chassis/server/cimc* #  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example resets the CIMC for server 1 in chassis 3 and commits the transaction: 
    
    
    UCS-A# **scope server 3/1**
    UCS-A /chassis/server # **scope cimc**
    UCS-A /chassis/server/cimc # **reset**
    UCS-A /chassis/server/cimc* # **commit-buffer**
    UCS-A /chassis/server/cimc #  
    

## Resetting the CMOS for a Server 

Sometimes, troubleshooting a server might require you to reset the CMOS. Resetting the CMOS is not part of the normal maintenance of a server. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server ` ` chassis-num / server-num |  Enters chassis server mode for the specified chassis.   
**Step 2** |  UCS-A /chassis/server #  reset-cmos |  Resets the CMOS for the server.   
**Step 3** |  UCS-A /chassis/server* #  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example resets the CMOS for server 1 in chassis 3 and commits the transaction: 
    
    
    UCS-A# **scope server 3/1**
    UCS-A /chassis/server # **reset-cmos**
    UCS-A /chassis/server* # **commit-buffer**
    UCS-A /chassis/server #  
    

## Resetting the BIOS Password for a Cisco UCS S3260 Server Node

This option allows you to reset the BIOS password without using the F2 BIOS configuration prompt. Resetting the BIOS password is not part of the normal maintenance of a server. After the BIOS password reset, the server is rebooted immediately and the new BIOS password gets updated. 

### Procedure

* * *

**Step 1** |  UCS-A#  scope server ` ` chassis-num / server-num Enters chassis server mode for the specified chassis.   
---|---  
**Step 2** |  UCS-A /chassis/server #  reset-bios-password Resets the BIOS password for the Cisco UCS S3260 server.   
**Step 3** |  UCS-A /chassis/server #  commit-buffer Commits the transaction to the system configuration.   
  
* * *

## Resetting KVM 

Perform the following procedure if you need to reset and clear all KVM sessions. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope server chassis-num / server-num |  Enters chassis server mode for the specified server.   
**Step 2** |  UCS-A /chassis/server # reset-kvm |  Resets and clears all KVM sessions.   
**Step 3** |  UCS-A /chassis/server* # commit-buffer |  Commits any pending transactions.   
  
### Example

The following example resets and clears all KVM sessions and commits the transaction: 
    
    
    UCS-A# **scope server 3/1**
    UCS-A /chassis/server # **reset-kvm**
    UCS-A /chassis/server* # **commit-buffer**
    UCS-A /chassis/server # 
    
    

## Issuing an NMI from a Server 

Perform the following procedure if the system remains unresponsive and you need Cisco UCS Manager to issue a Non-Maskable Interrupt (NMI) to the BIOS or operating system from the CIMC. This action creates a core dump or stack trace, depending on the operating system installed on the server. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope server chassis-num / server-num |  Enters chassis server mode for the specified server.   
**Step 2** |  UCS-A /chassis/server # diagnostic-interrupt |   
**Step 3** |  UCS-A /chassis/server* # commit-buffer |  Commits any pending transactions.   
  
### Example

The following example sends an NMI from server 1 in chassis 3 and commits the transaction: 
    
    
    UCS-A# **scope server 3/1**
    UCS-A /chassis/server # **diagnostic-interrupt**
    UCS-A /chassis/server* # **commit-buffer**
    UCS-A /chassis/server # 
    

## Recovering a Corrupt BIOS 

On rare occasions, an issue with a server may require you to recover the corrupted BIOS. This procedure is not part of the normal maintenance of a server. After you recover the BIOS, the server boots with the running version of the firmware for that server. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server ` ` chassis-num / server-num |  Enters chassis server mode for the specified chassis.   
**Step 2** |  UCS-A /chassis/server #  recover-bios version |  Loads and activates the specified BIOS version.   
**Step 3** |  UCS-A /chassis/server* #  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example shows how to recover the BIOS: 
    
    
    UCS-A# **scope server 3/1**
    UCS-A /chassis/server # **recover-bios S5500.0044.0.3.1.010620101125**
    UCS-A /chassis/server* # **commit-buffer**
    UCS-A /chassis/server #  
    

## Health LED Alarms 

The server health LED is located on the front of each server. Cisco UCS Manager allows you to view the sensor faults that cause the blade health LED to change color from green to amber or blinking amber. 

The health LED alarms display the following information:  Name  |  Description   
---|---  
Severity column  |  The severity of the alarm. This can be one of the following: 

  * Critical - The server health LED blinks amber. This is indicated with a red dot. 
  * Minor - The server health LED is amber. This is indicated with an orange dot. 

  
Description column  |  A brief description of the alarm.   
Sensor ID column  |  The ID of the sensor that triggered the alarm.   
Sensor Name column  |  The name of the sensor that triggered the alarm.   
  
  * Viewing Health LED Status


### Viewing Health LED Status 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server chassis-id / server-id |  Enters chassis server mode for the specified server.   
**Step 2** |  UCS-A /chassis/server #  show health-led expand |  Displays the health LED and sensor alarms for the selected server.   
  
#### Example

The following example shows how to display the health LED status and sensor alarms for chassis 1 server 3: 
    
    
    UCS-A# **scope server 1/3**
    UCS-A /chassis/server # **show health-led expand**
    Health LED:
        Severity: Normal
        Reason:
        Color: Green
        Oper State: On
    
    UCS-A /chassis/server # 

---

## Page 13: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_4_3/b_UCSM_CLI_Infrastructure_Management_Guide_chapter_01011.html

# Virtual Interface Management

## Virtual Circuits 

A virtual circuit or virtual path refers to the path that a frame takes from its source vNIC to its destination virtual switch port (vEth) or from a source virtual switch port to its destination vNIC. There are many possible virtual circuits that traverse through a physical cable. Cisco UCS Manager uses virtual network tags (VN-TAG) to identify these virtual circuits and differentiate between them. The OS decides the virtual circuit that a frame must traverse on a basis of a series of decisions. 

In the server, the OS decides the Ethernet interface from which to send the frame. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

During service profile configuration, you can select the fabric interconnect to be associated with a vNIC. You can also choose whether fabric failover is enabled for the vNIC. If fabric failover is enabled, the vNIC can access the second fabric interconnect when the default fabric interconnect is unavailable. Cisco UCS Manager Server Management Guide provides more details about vNIC configuration during service profile creation. 

* * *  
  
---|---  
  
After the host vNIC is selected, the frame exits the selected vNIC and, through the host interface port (HIF), enters the IOM to which the vNIC is pinned. The frame is then forwarded to the corresponding network Interface port (NIF) and then to the Fabric Interconnect to which the IOM is pinned. 

The NIF is selected based on the number of physical connections between the IOM and the Fabric Interconnect, and on the server ID from which the frame originated. 

## Virtual Interfaces 

In a blade server environment, the number of vNICs and vHBAs configurable for a service profile is determined by adapter capability and the amount of virtual interface (VIF) namespace available on the adapter. In Cisco UCS, portions of VIF namespace are allotted in chunks called VIFs. Depending on your hardware, the maximum number of VIFs are allocated on a predefined, per-port basis. 

The maximum number of VIFs varies based on hardware capability and port connectivity. For each configured vNIC or vHBA, one or two VIFs are allocated. Stand-alone vNICs and vHBAs use one VIF and failover vNICs and vHBAs use two. 

The following variables affect the number of VIFs available to a blade server, and therefore, how many vNICs and vHBAs you can configure for a service profile. 

  * Maximum number of VIFs supported on your fabric interconnect 

  * How the fabric interconnects are cabled 

  * If your fabric interconnect and IOM are configured in fabric port channel mode 


For more information about the maximum number of VIFs supported by your hardware configuration, see the appropriate Cisco UCS Configuration Limits for Cisco UCS Manager for your software release. 

## Virtual Interface Subscription Management and Error Handling

For fabric interconnects grouped in a port-channel, changes to the way you connect the fabric interconnect to the I/O module could result in a drastic change to the number of VIFs available to a blade server. To help you track the effect of these changes, Cisco UCS Manager maintains the following metrics: 

  * Maximum number of VIFs supported by hardware

  * Connectivity type


If you change your configuration in a way that decreases the number of VIFs available to a blade, UCS Manager will display a warning and ask you if you want to proceed. This includes several scenarios, including times where adding or moving a connection decreases the number of VIFs. 

## Virtualization in Cisco UCS

  * Overview of Virtualization
  * Overview of Cisco Virtual Machine Fabric Extender
  * Virtualization with Network Interface Cards and Converged Network Adapters
  * Virtualization with a Virtual Interface Card Adapter


### Overview of Virtualization

Virtualization allows you to create multiple Virtual Machines (VMs) to run in isolation, side by side on the same physical machine. 

Each virtual machine has its own set of virtual hardware (RAM, CPU, NIC) upon which an operating system and fully configured applications are loaded. The operating system sees a consistent, normalized set of hardware regardless of the actual physical hardware components. 

In a virtual machine, both hardware and software are encapsulated in a single file for rapid provisioning and moving between physical servers. You can move a virtual machine, within seconds, from one physical server to another for zero-downtime maintenance and continuous workload consolidation. 

The virtual hardware makes it possible for many servers, each running in an independent virtual machine, to run on a single physical server. The advantages of virtualization include better use of computing resources, greater server density, and seamless server migration. 

### Overview of Cisco Virtual Machine Fabric Extender

A virtualized server implementation consists of one or more VMs that run as guests on a single physical server. The guest VMs are hosted and managed by a software layer called the hypervisor or virtual machine manager (VMM). Typically, the hypervisor presents a virtual network interface to each VM and performs Layer 2 switching of traffic from a VM to other local VMs or to another interface to the external network. 

Working with a Cisco virtual interface card (VIC) adapter, the Cisco Virtual Machine Fabric Extender (VM-FEX) bypasses software-based switching of VM traffic by the hypervisor for external hardware-based switching in the fabric interconnect. This method reduces the load on the server CPU, provides faster switching, and enables you to apply a rich set of network management features to local and remote traffic. 

VM-FEX extends the IEEE 802.1Qbh port extender architecture to the VMs by providing each VM interface with a virtual Peripheral Component Interconnect Express (PCIe) device and a virtual port on a switch. This solution allows precise rate limiting and quality of service (QoS) guarantees on the VM interface. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

VM-FEX is not supported with Cisco UCS 6400 Series Fabric Interconnects. 

* * *  
  
---|---  
  
### Virtualization with Network Interface Cards and Converged Network Adapters

Network interface card (NIC) and converged network adapters support virtualized environments with the standard VMware integration with ESX installed on the server and all virtual machine management performed through the VC. 

#### Portability of Virtual Machines

If you implement service profiles you retain the ability to easily move a server identity from one server to another. After you image the new server, the ESX treats that server as if it were the original. 

#### Communication between Virtual Machines on the Same Server

These adapters implement the standard communications between virtual machines on the same server. If an ESX host includes multiple virtual machines, all communications must go through the virtual switch on the server. 

If the system uses the native VMware drivers, the virtual switch is out of the network administrator's domain and is not subject to any network policies. As a result, for example, QoS policies on the network are not applied to any data packets traveling from VM1 to VM2 through the virtual switch. 

If the system includes another virtual switch, such as the Nexus 1000, that virtual switch is subject to the network policies configured on that switch by the network administrator. 

### Virtualization with a Virtual Interface Card Adapter 

A Cisco VIC adapter is a converged network adapter (CNA) that is designed for both bare metal and VM-based deployments. The VIC adapter supports static or dynamic virtualized interfaces, which includes up to 116 virtual network interface cards (vNICs). 

There are two types of vNICs used with the VIC adapter—static and dynamic. A static vNIC is a device that is visible to the OS or hypervisor. Dynamic vNICs are used for VM-FEX by which a VM is connected to a veth port on the Fabric Interconnect. 

VIC adapters support VM-FEX to provide hardware-based switching of traffic to and from virtual machine interfaces. 

---

## Page 14: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_4_3/b_UCSM_CLI_Infrastructure_Management_Guide_chapter_01100.html

# Troubleshoot Infrastructure

## Recovering the Corrupt BIOS on a Blade Server 

On rare occasions, an issue with a blade server may require you to recover the corrupted BIOS. This procedure is not part of the normal maintenance of a server. After you recover the BIOS, the blade server boots with the running version of the firmware for that server. 

### Before you begin

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

Remove all attached or mapped USB storage from a server before you attempt to recover the corrupt BIOS on that server. If an external USB drive is attached or mapped from vMedia to the server, BIOS recovery fails. 

* * *  
  
---|---  
  
### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server ` ` chassis-id / server-id |  Enters chassis server mode for the specified blade server in the specified chassis.   
**Step 2** |  UCS-A /chassis/server #  recover-bios ` ` version |  Loads and activates the specified BIOS version.   
**Step 3** |  UCS-A /chassis/server #  commit-buffer |  Commits the transaction.   
  
### Example

The following example shows how to recover the BIOS: 
    
    
    UCS-A# **scope server 1/7**
    UCS-A /chassis/server # **recover-bios S5500.0044.0.3.1.010620101125**
    UCS-A /chassis/server* # **commit-buffer**
    UCS-A /chassis/server # 
    

## Recovering the Corrupt BIOS on a Rack-Mount Server 

On rare occasions, an issue with a rack-mount server may require you to recover the corrupted BIOS. This procedure is not part of the normal maintenance of a rack-mount server. After you recover the BIOS, the rack-mount server boots with the running version of the firmware for that server. 

### Before you begin

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

Remove all attached or mapped USB storage from a server before you attempt to recover the corrupt BIOS on that server. If an external USB drive is attached or mapped from vMedia to the server, BIOS recovery fails. 

* * *  
  
---|---  
  
### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server ` ` server-id |  Enters server mode for the specified rack-mount server.   
**Step 2** |  UCS-A /server #  recover-bios ` ` version |  Loads and activates the specified BIOS version.   
**Step 3** |  UCS-A /server #  commit-buffer |  Commits the transaction.   
  
### Example

The following example shows how to recover the BIOS: 
    
    
    UCS-A# **scope server 1**
    UCS-A /server # **recover-bios S5500.0044.0.3.1.010620101125**
    UCS-A /server* # **commit-buffer**
    UCS-A /server # 
    

---

## Page 15: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_chapter_0111.html

# Power Management

## Power Capping in Cisco UCS

You can control the maximum power consumption on a server through power capping, as well as manage the power allocation in the Cisco UCS Manager for blade servers, rack servers, UCS Mini, and mixed UCS domains. 

Cisco UCS Manager supports power capping on the following: 

  * Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct) 

  * UCS 6500 Series Fabric Interconnects

  * UCS 6400 Series Fabric Interconnects

  * UCS 6300 Series Fabric Interconnects 

  * UCS 6324 Series Fabric Interconnects (Cisco UCS Mini)


You can use Policy Driven Chassis Group Power Cap, or Manual Blade Level Power Cap methods to allocate power that applies to all of the servers in a chassis. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCSX-9508 Chassis supports Policy Driven Chassis Group Cap.  When you choose to select Policy Driven Chassis Group Cap, Cisco UCS Manager calculates the power allotment for Cisco UCSX-9508 Chassis and when you choose to select Manual Blade Level Power Cap, Chassis Management Controller (CMC) calculates the power allotment for Cisco UCSX-9508 Chassis. 

* * *  
  
---|---  
  
Cisco UCS Manager provides the following power management policies to help you allocate power to your servers: 

Power Management Policies  |  Description   
---|---  
Power Policy |  Specifies the redundancy for power supplies in all chassis in a Cisco UCS domain.   
Power Control Policies |  Specifies the priority to calculate the initial power allocation for each blade in a chassis.   
Power Save Policy |  Globally manages the chassis to maximize energy efficiency or availability.  
Cisco UCSX-9508 Chassis Power Extended Policy |  Manages the chassis to maximize energy efficiency or availability.  Power Extended Policy is effective only when we have PSU Redundant Policy Mode. For example, the total power available can be extended when we have N+1, N+2 and Grid to PSU Redundancy modes.   
Cisco UCSX-9508 Chassis Fan Control Policy |  Manages you to control the fan speed to bring down server power consumption and noise levels.  
Global Power Allocation |  Specifies the Policy Driven Chassis Group Power Cap or the Manual Blade Level Power Cap to apply to all servers in a chassis.   
Global Power Profiling  |  Specifies how the power cap values of the servers are calculated. If it is enabled, the servers will be profiled during discovery through benchmarking. This policy applies when the Global Power Allocation Policy is set to Policy Driven Chassis Group Cap.   
  
Power Policy Configuration

## Power Policy for Cisco UCS Servers 

The power policy is global and is inherited by all of the chassis' managed by the Cisco UCS Manager instance. You can add the power policy to a service profile to specify the redundancy for power supplies in all chassis' in the Cisco UCS domain. This policy is also known as the PSU policy. 

For more information about power supply redundancy, see Cisco UCS 5108 Server Chassis Hardware Installation Guide. 

## Configuring the Power Policy 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope org ` ` org-name |  Enters organization mode for the specified organization. To enter the root organization mode, type  / as the  org-name .   
**Step 2** |  UCS-A /org #  scope psu-policy |  Enters PSU policy mode.   
**Step 3** |  UCS-A /org/psu-policy #  set redundancy {grid | n-plus-1|n-plus-2 |non-redund}  |  Specifies one of the following redundancy types: 

  * grid —Two power sources are turned on, or the chassis requires greater than N+1 redundancy. If one source fails (which causes a loss of power to one or two PSUs), the surviving PSUs on the other power circuit continue to provide power to the chassis. 
  * n-plus-1 —The total number of PSUs to satisfy non-redundancy, plus one additional PSU for redundancy, are turned on and equally share the power load for the chassis. If any additional PSUs are installed, Cisco UCS Manager sets them to a "turned-off" state. 
  * non-redund —All installed power supplies (PSUs) are turned on and the load is evenly balanced. Only smaller configurations (requiring less than 2500W) can be powered by a single PSU. 
  * n-plus-2 —The total number of PSUs to satisfy non-redundancy, plus two additional PSU for redundancy, are turned on and equally share the power load for the chassis. If any additional PSUs are installed, Cisco UCS Manager sets them to a "turned-off" state.  |  **Note** |  n-plus-2 redundancy mode is supported only for Cisco UCS X9508 chassis. For all other chassis, Cisco UCS Manager treats n-plus-2 mode as n-plus-1 mode only.   
---|---  


For more information about power redundancy, see the Cisco UCS 5108 Server Chassis Installation Guide.   
  
**Step 4** |  UCS-A /org/psu-policy #  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example configures the power policy to use grid redundancy and commits the transaction: 
    
    
    UCS-A# **scope org /**
    UCS-A /org # **scope psu-policy**
    UCS-A /org/psu-policy # **set redundancy grid**			 
    UCS-A /org/psu-policy* # **commit-buffer**
    UCS-A /org/psu-policy #
    

The following example configures the power policy to use n-plus-2 redundancy for Cisco UCS X9508 chassis and shows the details: 
    
    
    UCS-A# **scope org**
    UCS-A /org # **scope psu-policy**
    UCS-A /org/psu-policy # **set redundancy n-plus-2**
    UCS-A /org/psu-policy # **commit-buffer**

##  Power Supply for Redundancy Method 

**PSU Redundancy** |  **Max Power @ 240 V**  
---|---  
Grid |  5000 Watts  
N+1 |  7500 Watts  
Non-Redundant |  8280 Watts  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

This table is valid if there are four PSUs installed in the chassis.

* * *  
  
---|---  
  
Policy Driven Power Capping

## Policy Driven Chassis Group Power Capping 

When you select the Policy Driven Chassis Group Power Cap in the Global Cap Policy, Cisco UCS can maintain the over-subscription of servers without risking power failures. You can achieve over-subscription through a two-tier process. For example, at the chassis level, Cisco UCS divides the amount of power available among members of the power group, and at the blade level, the amount of power allotted to a chassis is divided among blades based on priority. 

Each time a service profile is associated or disassociated, Cisco UCS Manager recalculates the power allotment for each blade server within the chassis. If necessary, power from lower-priority service profiles is redistributed to higher-priority service profiles. 

UCS power groups cap power in less than one second to safely protect data center circuit breakers. A blade must stay at its cap for 20 seconds before the chassis power distribution is optimized. This is intentionally carried out over a slower timescale to prevent reacting to transient spikes in demand. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The system reserves enough power to boot a server in each slot, even if that slot is empty. This reserved power cannot be leveraged by servers requiring more power. Blades that fail to comply with the power cap are penalized. 

* * *  
  
---|---  
  
## Power Control Policy 

Cisco UCS uses the priority set in the power control policy along with the blade type and configuration to calculate the initial power allocation for each blade within a chassis. During normal operation, the active blades within a chassis can borrow power from idle blades within the same chassis. If all blades are active and reach the power cap, service profiles with higher priority power control policies take precedence over service profiles with lower priority power control policies. 

Priority is ranked on a scale of 1-10, where 1 indicates the highest priority and 10 indicates lowest priority. The default priority is 5. 

Starting with Cisco UCS Manager 3.2(2), chassis dynamic power rebalance mechanism is enabled by default. The mechanism continuously monitors the power usage of the blade servers and adjusts the power allocation accordingly. Chassis dynamic power rebalance mechanism operates within the overall chassis power budget set by Cisco UCS Manager, which is calculated from the available PSU power and Group power. 

For mission-critical application a special priority called no-cap is also available. Setting the priority to no-cap does not guarantee that a blade server gets maximum power all the time, however, it prioritizes the blade server over other servers during the chassis dynamic power rebalance budget allocations. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

If all the blade servers are set with no-cap priority and all of them run high power consuming loads, then there is a chance that some of the blade servers get capped under high power usage, based on the power distribution done through dynamic balance. 

* * *  
  
---|---  
  
Global Power Control Policy options are inherited by all the chassis managed by the Cisco UCS Manager. 

Starting with Cisco UCS Manager 4.1(3), a global policy called Power Save Mode is available. It is disabled by default, meaning that all PSUs present remain active regardless of power redundancy policy selection. Enabling the policy restores the older behavior.. 

Starting with Cisco UCS Manager 4.1(2), the power control policy is also used for regulating fans in Cisco UCS C220 M5 and C240 M5 rack servers in acoustically-sensitive environments. The Acoustic setting for these fans is only available on these servers. On C240 SD M5 rack servers, Acoustic mode is the default mode. 

Starting with Cisco UCS Manager 4.2(1), the power control policy is also used for regulating cooling in potentially high-temperature environments. This option is only available with Cisco UCS C220 M6, C240 M6, C225 M6, and C245 M6 rack servers and can be used with any fan speed option. 

Starting with Cisco UCS Manager 4.3(2), a global policy called Cisco UCS X9508 Chassis Power Extended Policy. This option is only available with Cisco UCS X9508 Chassis. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

You must include the power control policy in a service profile and that service profile must be associated with a server for it to take effect. 

* * *  
  
---|---  
  
  * Creating a Power Control Policy
  * Deleting a Power Control Policy


### Creating a Power Control Policy

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope org ` ` org-name |  Enters organization mode for the specified organization. To enter the root organization mode, use / as the org-name.  
**Step 2** |  UCS-A /org #  create power-control-policy ` ` power-control-pol-name |  Creates a power control policy and enters power control policy mode.  
**Step 3** |  UCS-A /org/power-control-policy #  set fanspeed ` `{any | balanced|high-power|low-power | max-power | performance | acoustic | max-cooling}  |  Specifies the fan speed for the power control policy. |  **Note** |  The Performance option is not supported on Cisco UCS C-Series M5 and M6 servers.   
---|---  
**Step 4** |  UCS-A /org/power-control-policy #  set cpu-package-power-limit ` `{default | min| max}  |  Specifies the Central Processing Unit (CPU) power consumption settings by selecting the Package Power Limits (PPL) in watts: default, min, or max. This setting determines the power a CPU can draw, thereby impacting system performance and thermal output.  |  **Note** |  The PPL is currently supported only on the processors of Cisco UCS C225 M8 and C245 M8 servers.  
---|---  
**Step 5** |  UCS-A /org/power-control-policy #  set priority ` `{priority-num | no-cap}  |  Specifies the priority for the power control policy.  
**Step 6** |  UCS-A /org/power-control-policy #  commit-buffer |  Commits the transaction to the system configuration.  
  
#### Example

The following example creates a power control policy called powerpolicy15, sets the priority at level 2, configures the CPU Package Power Limit to max, and commits the transaction: 
    
    
    UCS-A# **scope org /**
    UCS-A /org # **create power-control-policy powerpolicy15**
    UCS-A /org/power-control policy* # **set priority 2**
    UCS-A /org/power-control policy* # **set cpu-package-power-limit max**
    UCS-A /org/power-control policy* # **commit-buffer**
    UCS-A /org/power-control policy #

#### What to do next

Include the power control policy in a service profile.

Configuring Acoustic Mode

### Acoustic Mode Fan Profile

The Acoustic Mode fan profile is available on Cisco UCS C-Series rack servers..

Setting up an Acoustic Mode fan policy lets you reduce the noise level on Cisco UCS C-Series rack servers. The higher capacity fans on Cisco UCS C-Series rack servers increase the cooling capacity, but also create more acoustic noise. The standard fan profiles for Cisco UCS C-Series rack servers (Low Power, Balanced, High Power, and Max Power) are designed to regulate the server to optimize energy consumption. The primary goal of these fan profiles is to prevent throttling of CPU’s and peripherals. 

The goal of Acoustic Mode is reducing fan speed to reduce noise levels in acoustic-sensitive environments. Power capping has no effect when Acoustic Mode is selected. 

### Creating an Acoustic Mode Fan Policy

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope org ` ` org-name |  Enters organization mode for the specified organization. To enter the root organization mode, type / as the org-name.  
**Step 2** |  UCS-A /org #  create power-control-policy ` ` fan-policy-name |  Creates a fan control policy and enters power control policy mode. Fan policies are created through the power control interface.  
**Step 3** |  UCS-A /org/power-control-policy #  set fanspeed ` `{ acoustic }  |  Specifies Acoustic Mode as the fan speed for the power control policy.  
**Step 4** |  UCS-A /org/power-control-policy #  set priority ` `{priority-num | no-cap}  |  Specifies the priority for the fan's power control policy.  
**Step 5** |  UCS-A /org/power-control-policy #  commit-buffer |  Commits the transaction to the system configuration.  
  
#### What to do next

Include the power control policy in a service profile.

### Deleting a Power Control Policy

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope org ` ` org-name |  Enters organization mode for the specified organization. To enter the root organization mode, type / as the org-name.  
**Step 2** |  UCS-A /org #  delete power-control-policy ` ` power-control-pol-name |  Deletes the specified power control policy.  
**Step 3** |  UCS-A /org #  commit-buffer |  Commits the transaction to the system configuration.  
  
#### Example

The following example deletes a power control policy called powerpolicy15 and commits the transaction:
    
    
    UCS-A# **scope org /**
    UCS-A /org # **delete power-control-policy powerpolicy15**
    UCS-A /org* # **commit-buffer**
    UCS-A /org #

## Power Groups in UCS Manager 

A power group is a set of chassis that all draw power from the same power distribution unit (PDU). In Cisco UCS Manager, you can create power groups that include one or more chassis, then set a peak power cap in AC watts for that power grouping. 

Implementing power capping at the chassis level requires the following: 

  * IOM, CIMC, and BIOS version 1.4 or higher 

  * Two Power Supply Units (PSUs) 


The peak power cap is a static value that represents the maximum power available to all blade servers within a given power group. If you add or remove a blade from a power group, but do not manually modify the peak power value, the power group adjusts the peak power cap to accommodate the basic power-on requirements of all blades within that power group. 

A minimum of 890 AC watts should be set for each chassis. This converts to 800 watts of DC power, which is the minimum amount of power required to power an empty chassis. To associate a half-width blade, the group cap needs to be set to 1475 AC watts. For a full-width blade, it needs to be set to 2060 AC watts. 

After a chassis is added to a power group, all service profile associated with the blades in the chassis become part of that power group. Similarly, if you add a new blade to a chassis, that blade inherently becomes part of the chassis' power group. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Creating a power group is not the same as creating a server pool. However, you can populate a server pool with members of the same power group by creating a power qualifier and adding it to server pool policy. 

* * *  
  
---|---  
  
When a chassis is removed or deleted, the chassis gets removed from the power group. 

UCS Manager supports explicit and implicit power groups. 

  * Explicit: You can create a power group, add chassis' and racks, and assign a budget for the group. 

  * Implicit: Ensures that the chassis is always protected by limiting the power consumption within safe limits. By default, all chassis that are not part of an explicit power group are assigned to the default group and the appropriate caps are placed. New chassis that connect to UCS Manager are added to the default power group until you move them to a different power group. 


The following table describes the error messages you might encounter while assigning power budget and working with power groups. 

Error Message  | Cause  | Recommended Action   
---|---|---  
Insufficient budget for power group POWERGROUP_NAME and/or  Chassis N cannot be capped as group cap is low. Please consider raising the cap. and/or  Admin committed insufficient for power group GROUP_NAME, using previous value N and/or  Power cap application failed for chassis N  |  One of these messages displays if you did not meet the minimum limit when assigning the power cap for a chassis, or the power requirement increased because of the addition of blades or change of power policies.  |  Increase the power cap limit to the  Minimum Power Cap for Allowing Operations (W) value displayed on the Power Group page for the specified power group.   
Chassis N cannot be capped as the available PSU power is not enough for the chassis and the blades. Please correct the problem by checking input power or replace the PSU |  Displays when the power budget requirement for the chassis is more than the PSU power that is available.  |  Check the PSU input power and redundancy policy to ensure that enough power is available for the chassis.  If a PSU failed, replace the PSU.   
Power cap application failed for server N |  Displays when the server is consuming more power than allocated and cannot be capped, or the server is powered on when no power is allocated.  |  Do not power on un-associated servers.   
P-State lowered as consumption hit power cap for server |  Displays when the server is capped to reduce the power consumption below the allocated power.  |  This is an information message.  If a server should not be capped, in the service profile set the value of the power control policy Power Capping field to no-cap.   
Chassis N has a mix of high-line and low-line PSU input power sources. |  This fault is raised when a chassis has a mix of high-line and low-line PSU input sources connected.  |  This is an unsupported configuration. All PSUs must be connected to similar power sources.   
  
  * Creating a Power Group
  * Deleting a Power Group


### Creating a Power Group 

#### Before you begin

Ensure that the global power allocation policy is set to Policy Driven Chassis Group Cap. 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope power-cap-mgmt |  Enters power cap management mode.   
**Step 2** |  UCS-A /power-cap-mgmt #  create power-group ` ` power-group-name |  Creates a power group and enters power group mode.   
**Step 3** |  UCS-A /power-cap-mgmt/power-group #  set peak ` `{peak-num | disabled | uninitialized}  |  Specifies the maximum peak power (in watts) available to the power group.   
**Step 4** |  UCS-A /power-cap-mgmt/power-group #  create chassis ` ` chassis-id |  Adds the specified chassis to the power group and enters power group chassis mode.   
**Step 5** |  UCS-A /power-cap-mgmt/power-group #  create rack ` ` rack-id |  Adds the specified rack to the power group.   
**Step 6** |  UCS-A /power-cap-mgmt/power-group #  create fex ` ` fex-id |  Adds the specified FEX to the power group.   
**Step 7** |  UCS-A /power-cap-mgmt/power-group #  create fi ` ` fi-id |  Adds the specified FI to the power group.   
**Step 8** |  UCS-A /power-cap-mgmt/power-group/chassis #  commit-buffer |  Commits the transaction to the system configuration.   
  
#### Example

The following example creates a power group called powergroup1, specifies the maximum peak power for the power group (10000 watts), adds chassis 1 to the group, and commits the transaction: 
    
    
    UCS-A# **scope power-cap-mgmt**
    UCS-A /power-cap-mgmt # **create power-group powergroup1**
    UCS-A /power-cap-mgmt/power-group* # **set peak 10000**
    UCS-A /power-cap-mgmt/power-group* # **create chassis 1**
    UCS-A /power-cap-mgmt/power-group/chassis* # **commit-buffer**
    UCS-A /power-cap-mgmt/power-group/chassis #

### Deleting a Power Group

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope power-cap-mgmt |  Enters power cap management mode.  
**Step 2** |  UCS-A /power-cap-mgmt #  delete power-group ` ` power-group-name |  Deletes the specified power group.  
**Step 3** |  UCS-A /power-cap-mgmt/power-group/chassis #  commit-buffer |  Commits the transaction to the system configuration.  
  
#### Example

The following example deletes a power group called powergroup1 and commits the transaction:
    
    
    UCS-A# **scope power-cap-mgmt**
    UCS-A /power-cap-mgmt # **delete power-group powergroup1**
    UCS-A /power-cap-mgmt* # **commit-buffer**
    UCS-A /power-cap-mgmt #

Blade Level Power Capping

## Manual Blade Level Power Cap 

When manual blade-level power cap is configured in the global cap policy, you can set a power cap for each blade server in a Cisco UCS domain. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCSX-9508 Chassis does not support Manual Blade Level Power Cap. When you choose to select Manual Blade Level Power Cap, Chassis Management Controller (CMC) calculates the power allotment for Cisco UCSX-9508 Chassis. 

* * *  
  
---|---  
  
The following configuration options are available: 

  * Watts—You can specify the maximum amount of power that the server can consume at one time. This maximum can be any amount between 0 watts and 1300 watts. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

B480 M5 systems using 256GB DIMMs must have a manual blade level cap at 1300W.

* * *  
  
---|---  
  * Unbounded—No power usage limitations are imposed on the server. The server can use as much power as it requires. 


If the server encounters a spike in power usage that meets or exceeds the maximum configured for the server, Cisco UCS Manager does not disconnect or shut down the server. Instead, Cisco UCS Manager reduces the power that is made available to the server. This reduction can slow down the server, including a reduction in CPU speed. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

If you configure the manual blade-level power cap using Equipment > Policies > Global Policies > Global Power Allocation Policy, the priority set in the Power Control Policy is no longer relevant. 

* * *  
  
---|---  
  
## Setting the Blade-Level Power Cap for a Server 

### Before you begin

Ensure that the global power allocation policy is set to Manual Blade Level Cap. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server ` ` chassis-id / server-id |  Enters chassis server mode for the specified server.   
**Step 2** |  UCS-A /chassis/server #  set power-budget committed {unbounded | watts}  |  Commits the server to one of the following power usage levels: 

  * unbounded —Does not impose any power usage limitations on the server. 
  * watts —Allows you to specify the upper level for power usage by the server. If you choose this setting, enter the maximum number of watts that the server can use. The range is 0 to 10000000 watts. 

  
**Step 3** |  UCS-A /chassis/server #  commit-buffer |  Commits the transaction to the system configuration.   
**Step 4** |  UCS-A /chassis/server #  show power-budget |  (Optional) Displays the power usage level setting.   
  
### Example

The following example limits the power usage for a server to unbounded and then to 1000 watts and commits the transaction: 
    
    
    UCS-A# **scope server 1/7**
    UCS-A /chassis/server # **show power-budget**
    
    Budget:
        AdminCommitted (W)
    				-----------------
        139
    UCS-A /chassis/server # **set power-budget committed unbounded**
    UCS-A /chassis/server* # **commit-buffer**
    UCS-A /chassis/server # **show power-budget**
    
    Budget:
        AdminCommitted (W)
    				-----------------
        Unbounded 
    
    UCS-A /chassis/server # **set power-budget committed 1000**
    UCS-A /chassis/server* # **commit-buffer**
    UCS-A /chassis/server # **show power-budget**
    
    Budget:
        AdminCommitted (W)
    				-----------------
        1000 
    UCS-A /chassis/server #
    
    

Configuring a Chassis Level Fan Policy

## Configuring Fan Speed for Power Management

Globally managing the fan speed can help in power management by applying a single policy for all B-series server fans in an enclosure, based on general cooling needs. Set the fan speed on a per-chassis basis in the Global Policies. The two options are: 

  * Balanced—The fan runs at a faster speed when needed, based on the heat generated by the server. When possible, the fan returns to the minimum required speed. (Default.) 

  * Low Power—The fan runs at the minimum speed that is required to keep the server cool. 


The new option takes effect when the new selection is saved. Use Low Power to save on system power. 

## Configuring the Global Fan Control Policy

### Procedure

* * *

**Step 1** |  In the Navigation pane, click Equipment.   
---|---  
**Step 2** |  Click the Equipment node.   
**Step 3** |  In the Work pane, click the Policies tab.   
**Step 4** |  Click the Global Policies subtab.   
**Step 5** |  In the Fan Control Policy area, click one of the following radio buttons: 

  * Balanced—This is the default option. 
  * Low Power

  
**Step 6** |  Click Save Changes.   
  
* * *

## Viewing Server Statistics 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server ` ` chassis-id / server-id |  Enters chassis server mode for the specified server.   
**Step 2** |  UCS-A /chassis/server #  show ` ` stats |  Displays the following server statistics: 

  * Ethernet Port Error 
  * Ethernet Port Multicast 
  * Ethernet Port 
  * Virtual Interface 
  * Motherboard Power 
  * PC Ie Fatal Completion Error 
  * PC Ie Fatal Protocol Error 
  * PC Ie Fatal Receiving Error 
  * PC Ie Fatal Error 
  * Memory Error 
  * DIMM Env 
  * CPU Env 

  
  
### Example

The following example shows the section on motherboard power usage statistics: 
    
    
    UCS-A# **scope server 2/4**
    UCS-A /chassis/server # **show stats**
    
    Motherboard Power Statistics:
    Time Collected: 2016-07-11T20:51:24.722
    Monitored Object: sys/chassis-1/blade-1/board/power-stats
    Suspect: No
    Consumed Power (W): 126.000000
    Input Voltage (V): 11.859000
    Input Current (A): 10.624842
    Thresholded: 0
    
    UCS-A /chassis/server # 
    

Global Power Profiling Policy Configuration

## Global Power Profiling Policy 

The Global Power Profiling Policy specifies how power allocation is applied to all of the servers in a chassis. The policy applies when you set the Global Power Allocation Policy to policy-driven-chassis-group-cap . You can set the Global Power Profiling Policy to one of the following: 

  * Disabled—The minimum and maximum power cap values of the blades are calculated based on the static power consumption values of each of the components. 

  * Enabled—The minimum and maximum power cap values of the blades are measured as part of the server discovery. These values are similar to the actual power consumption of the blades. 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

After enabling the Global Power Profiling Policy, you must re-acknowledge the blades to obtain the minimum and maximum power cap. 

* * *  
  
---|---  
  
## Configuring the Global Power Profile Policy 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope power-cap-mgmt |  Enters power cap management mode.   
**Step 2** |  UCS-A /power-cap-mgmt #  set profile-policy ` `{no | yes}  |  Enables or disables the global power profiling policy.   
**Step 3** |  UCS-A /power-cap-mgmt #  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example shows how to enable the global power profile policy and commit the transaction: 
    
    
    UCS-A# **scope power-cap-mgmt**
    UCS-A /power-cap-mgmt # **set profile-policy yes**
    UCS-A /power-cap-mgmt* # **commit-buffer**
    UCS-A /power-cap-mgmt #

Global Power Allocation Policy

## Global Power Allocation Policy 

The Global Power Allocation Policy allows you to specify the Policy Driven Chassis Group Power Cap or Manual Blade-level Power Cap power allocation method applied to servers in a chassis. 

Cisco recommends using the default Policy Driven Chassis Group Power Cap power allocation method. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

Any change to the Manual Blade level Power Cap configuration results in the loss of any groups or configuration options set for the Policy Driven Chassis Group Power Cap. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCSX-9508 Chassis supports Policy Driven Chassis Group Cap only.  When you choose to select Policy Driven Chassis Group Cap, Cisco UCS Manager calculates the power allotment for Cisco UCS X9508 chassis and when you choose to select Manual Blade Level Power Cap, Chassis Management Controller (CMC) calculates the power allotment for Cisco UCSX-9508 Chassis. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For Cisco UCSX-9508 Chassis Allocated (W) and Measured Max. (W) will not match. The max allocated values are used to calculate the chassis-level power limit and Intelligent Fabric Modules (IFM) allocates the power based on the power limit. 

* * *  
  
---|---  
  
## Configuring the Global Power Allocation Policy 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope power-cap-mgmt |  Enters power cap management mode.   
**Step 2** |  UCS-A /power-cap-mgmt #  set cap-policy ` `{manual-blade-level-cap | policy-driven-chassis-group-cap}  |  Sets the global cap policy to the specified power cap management mode.  By default, the global cap policy is set to policy driven chassis group cap.   
**Step 3** |  UCS-A /power-cap-mgmt #  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example sets the global cap policy to manual blade power cap and commits the transaction: 
    
    
    UCS-A# **scope power-cap-mgmt**
    UCS-A /power-cap-mgmt # **set cap-policy manual-blade-level-cap**
    UCS-A /power-cap-mgmt* # **commit-buffer**
    UCS-A /power-cap-mgmt #

## Viewing the Power Cap Values for Servers 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope power-cap-mgmt |  Enters power cap management mode.   
**Step 2** |  UCS-A /power-cap-mgmt #  show power-measured |  Displays the minimum and maximum power cap values.   
  
### Example

The following example shows how to display the minimum and maximum power cap values: 
    
    
    UCS-A# **scope power-cap-mgmt**
    UCS-A /power-cap-mgmt # **show power-measured**
    
    Measured Power:
        Device Id (W)  Minimum power (W) Maximum power (W) OperMethod
        -------------- ----------------- ----------------- ----------
        blade   1/1    234               353               Pnuos
    
    UCS-A /power-cap-mgmt # 
    

## Power Management During Power-on Operations 

### Boot Staggering during Power on

Cisco UCS Manager attempts to boot as many blades as possible based on the amount of available power. If the power required to boot a blade is not available, Cisco UCS Manager staggers the boot in the Finite State Machine (FSM) CheckPowerAvailability stage, and raises the following fault on the blade: Insufficient power available to power-on server x/y. 

When the required power becomes available, the FSM proceeds with blade power on. After a blade powers off, the allocated power budget is reclaimed. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

When the power budget that was allocated to the blade is reclaimed, the allocated power displays as 0 Watts. 

* * *  
  
---|---  
  
**Limitation**

If you power on a blade outside of the Cisco UCS Manager and if there is not enough power available for allocation, the following fault is raised: 

Power cap application failed for server x/y

### Power Allocation during Service Profile Association

The power allocated to a blade during service profile association depends on the Power Control Policy used, and the power that is available from the power group. After the power is allocated to a server during a successful service profile association, the blade is guaranteed the minimum power cap. If the Power Control Policy priority is set to no-cap, a blade is allocated a potential maximum power cap, which might exceed the measured maximum power cap that displays. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

If the priority of an associated blade is changed to no-cap, and is not able to allocate the maximum power cap, you might see one of the following faults: 

  * PSU-insufficient—There is not enough available power for the PSU. 
  * Group-cap-insufficient—The group cap value is not sufficient for the blade. 


* * *  
  
---|---  
  
Power Sync Policy Configuration

## Power Sync Policy 

Cisco UCS Manager includes a global (default) power sync policy to address power synchronization issues between the associated service profiles and the servers. You can use the power sync policy to synchronize the power state when the power state of the service profile differs from the actual power state of the server. The policy allows you to control when to synchronize the power state on the associated service profiles for the servers. The power sync policy does not affect other power-related policies. 

The power synchronization policy applies to all the service profiles by default. You cannot delete the default power sync policy, but you can edit the default policy. You can create your own power sync policies and apply them to the service profiles. You can also create a power sync policy that is specific to a service profile and it always takes precedence over the default policy. 

Cisco UCS Manager creates a fault on the associated service profile when the power sync policy referenced in the service profile does not exist. Cisco UCS Manager automatically clears the fault once you create a power sync policy for the specified service profile or change the reference to an existing policy in the service profile. 

## Power Synchronization Behavior 

Cisco UCS Manager synchronizes the power state only when the actual power state of the server is OFF. The current power synchronization behavior is based on the actual power state and the preferred power state after shallow association occurs. 

For example, the following events trigger shallow association: 

  * Fabric Interconnects(FI) and IOM disconnected. 

  * IOM reset 

  * FI power loss or reboot 

  * Chassis reacknowledgment 

  * Chassis power loss 

  * Service profile change 


The following table describes the current power synchronization behavior: 

Event  |  Preferred Power State  |  Actual Power State Before Event  |  Actual Power State After Event   
---|---|---|---  
Shallow Association  |  ON  |  OFF  |  ON   
Shallow Association  |  OFF  |  OFF  |  OFF   
Shallow Association  |  ON  |  ON  |  ON   
Shallow Association  |  OFF  |  ON  |  ON   
  
## Displaying the Global Power Sync Policy 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A #  scope org ` ` org-name |  Enters organization mode for the specified organization. To enter the root organization mode, type / as the org-name.   
**Step 2** |  UCS-A/org #  scope power-sync-policy default ` ` |  Enters the global power sync policy mode.   
**Step 3** |  UCS-A /org/power/-sync-policy #  show  ` ` {detail | expand | detail expand }  |  Displays the global power sync policy information.   
  
### Example

The following example displays the global (default) power sync policy: 
    
    
    UCS-A # **scope org**
    UCS-A /org # **scope power-sync-policy default-sync**
    UCS-A /org/power-sync-policy # **show expand**
    
    Power Sync Policy:
        Name                 Power Sync Option
        -------------------- -----------------
        default              Default Sync
    
    UCS-A /org/power-sync-policy # **show detail expand**
    
    Power Sync Policy:
        Full Name: org-root/power-sync-default
        Name: default
        Description:
        Power Sync Option: Default Sync
        Policy Owner: Local
    
    UCS-A /org/power-sync-policy # 
    

## Setting Global Policy Reference for a Service Profile

To refer the global power sync policy in a service profile, use the following commands in service profile mode: 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A #  scope org ` ` org-name |  Enters organization mode for the specified organization. To enter the root organization mode, type / as the org-name.   
**Step 2** |  UCS-A/org #  scope service-profile ` ` service-profile-name |  Enters the service profile mode for the specified service profile. The name of the service profile can be a minimum of two characters and a maximum up to 32 characters.   
**Step 3** |  UCS-A /org/service-profile #  set power-sync-policy default |  Specifies the global power sync policy that can be referenced in the service profile. You can also change the policy reference from the default to other power sync policies using this command.   
**Step 4** |  UCS-A /org/service-profile* # commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example sets the reference to the global power sync policy for use in the service profile. 
    
    
    UCS-A # **scope org**
    			 UCS-A/org # **scope service-profile spnew**
    			 UCS-A/org/service-profile # **set power-sync-policy default**
    			 UCS-A/org/service-profile* # **commit-buffer**
    			 

## Creating a Power Sync Policy

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A #  scope org ` ` org-name |  Enters organization mode for the specified organization. To enter the root organization mode, type / as the org-name.   
**Step 2** |  UCS-A /org #  create power-sync-policy ` ` power-sync-pol-name |  Creates a power sync policy and enters power sync policy mode. The power sync policy name can be up to 16 characters.   
**Step 3** |  (Optional) UCS-A /org/power-sync-policy* # set` ` descr` ` optionall-description | (Optional)  Specifies the description of the power-sync-policy. You can also modify the description using the descr keyword.   
**Step 4** |  UCS-A /org/power-sync-policy* # set` ` sync-option` ` { always-sync | default-sync | initial-only-sync }  |  Specifies the power synchronization option to the physical server. You can also modify the power synchronization option using the sync-option keyword. This can be one of the following: 

  * Default Sync—After the initial server association, any configuration change or management connectivity changes that you perform trigger a server reassociation. This option synchronizes the desired power state to the physical server if the physical server power state is off and the desired power state is on. This is the default behavior. 
  * Always Sync—When the initial server association or the server reassociation occurs, this option always synchronizes the desired power state to the physical server even if the physical server power state is on and the desired power state is off. 
  * Initial Only Sync—This option only synchronizes the power to a server when a service profile is associated to the server for the first time or when the server is re-commissioned. When you set this option, resetting the power state from the physical server side does not affect the desired power state on the service profile. 

  
**Step 5** |  UCS-A /org/power-sync-policy* # commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example creates a power sync policy called newSyncPolicy, sets the default sync-option, and commits the transaction to the system configuration: 
    
    
    UCS-A # **scope org**
    UCS-A /org # **create power-sync-policy newSyncPolicy**
    UCS-A /org/power-sync-policy* # **set decsr newSyncPolicy**
    UCS-A /org/power-sync-policy* # **set sync-option default-sync**
    UCS-A /org/power-sync-policy* # **commit-buffer**
    UCS-A /org/power-sync-policy #
    

### What to do next

Include the power sync policy in a service profile or in a service profile template. 

## Deleting a Power Sync Policy

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A #  scope org ` ` org-name |  Enters organization mode for the specified organization. To enter the root organization mode, type / as the org-name.   
**Step 2** |  UCS-A /org #  delete power-sync-policy ` ` power-sync-pol-name |  Deletes the specified power sync policy.   
**Step 3** |  UCS-A /org #  commit buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example deletes the power sync policy called spnew and commits the transaction to the system: 
    
    
    UCS-A # **scope org**
    UCS-A /org # **delete power-sync-policy spnew**
    UCS-A /org # **commit-buffer**

## Displaying All Power Sync Policies

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A #  scope org ` ` org-name |  Enters organization mode for the specified organization. To enter the root organization mode, type / as the org-name.   
**Step 2** |  UCS-A /org #  show power-sync-policy ` ` {detail | expand | detail expand }  |  Displays the default, local, and other power sync policies.   
  
### Example

The following example displays power sync policies that are defined: 
    
    
    UCS-A # **scope org**
    UCS-A /org # **show power-sync-policy expand**
    Power Sync Policy:
        Name                 Power Sync Option
        -------------------- -----------------
        default              Default Sync
        policy-1             Default Sync
    
    UCS-A /org # **show power-sync-policy detail expand**
    Power Sync Policy:
        Full Name: org-root/power-sync-default
        Name: default
        Description:
        Power Sync Option: Default Sync
        Policy Owner: Local
    
        Full Name: org-root/power-sync-policy-1
        Name: policy-1
        Description:
        Power Sync Option: Default Sync
        Policy Owner: Local
    
    UCS-A /org #

## Creating a Local Policy

To create a local power sync policy that you want to use by any service profile, create a power sync definition for the power sync policy. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A #  scope org ` ` org-name |  Enters organization mode for the specified organization. To enter the root organization mode, type / as the org-name.   
**Step 2** |  UCS-A /org #  scope service-profile ` ` service-profile-name |  Enters the service profile mode for the specified service profile. The name of the service profile can be a minimum of two characters and a maximum up to 32 characters.   
**Step 3** |  UCS-A /org/service-profile #  create power-sync-definition |  Enters the power sync definition mode. You can create a power sync policy definition that you defined for the power sync policy.   
**Step 4** |  (Optional) UCS-A /org/service-profile/power-sync-definition* # set` ` descr` ` optional-description | (Optional)  Specifies the description of the power-sync-policy. You can also change the description using the descr keyword.   
**Step 5** |  UCS-A /org/service-profile/power-sync-definition* # set` ` sync-option` ` { always-sync | default-sync | initial-only-sync }  |  Specifies the power synchronization option to the physical server. You can also change the power synchronization option using the sync-option keyword.   
**Step 6** |  UCS-A /org/service-profile/power-sync-definition* # commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example creates a local policy using the policy sync definition, sets the sync-option, and commits the transaction to the system configuration: 
    
    
     UCS-A # **scope org**
     UCS-A/org # **scope service-profile spnew**
    UCS-A/org/service-profile # **create power-sync-definition**
    UCS-A/org/service-profile/power-sync-definition* # **set decsr spnew**
    UCS-A/org/service-profile/power-sync-definition* # **set sync-option default-sync**
    UCS-A/org/service-profile/power-sync-definition* # **commit-buffer**

## Showing a Local Policy

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A #  scope org ` ` org-name |  Enters organization mode for the specified organization. To enter the root organization mode, type / as the org-name.   
**Step 2** |  UCS-A/org #  scope service-profile ` ` service-profile-name |  Enters the service profile mode for the specified service profile. The name of the service profile can be a minimum of two characters and a maximum up to 32 characters.   
**Step 3** |  (Optional) UCS-A /org/service-profile #  show power-sync-policy ` ` {detail | expand | detail expand }  | (Optional)  Displays the local policy in the power-sync-policy mode.   
**Step 4** |  UCS-A /org/service-profile #  show power-sync-definition ` ` {detail | expand | detail expand }  |  Displays the local policy for the specified service policy in the power-sync-definition mode.  |  **Note** |  If you do not have a definition for the power sync policy, you can still use the command, but you cannot see anything displayed.   
---|---  
  
### Example

The following example displays the local policy in use by the service profile spnew: 
    
    
     UCS-A # **scope org**
    UCS-A/org # **scope service-profile spnew**
    UCS-A/org/service-profile # **show power-sync-definition expand**
    
    Power Sync Definition:
        Name                 Power Sync Option
        -------------------- -----------------
        spnew                Always Sync
    
    UCS-A/org/service-profile # **show power-sync-definition detail expand**
    
    Power Sync Definition:
        Full Name: org-root/ls-sp2/power-sync-def
        Name: spnew 
        Description: optional description
        Power Sync Option: Always Sync
        Policy Owner: Local
    
    UCS-A/org/service-profile # 

## Deleting a Local Policy

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A #  scope org ` ` org-name |  Enters organization mode for the specified organization. To enter the root organization mode, type / as the org-name.   
**Step 2** |  UCS-A/org #  scope service-profile ` ` service-profile-name |  Enters the service profile mode for the specified service profile. The name of the service profile can be a minimum of two characters and a maximum up to 32 characters.   
**Step 3** |  UCS-A /org/service-profile #  delete power-sync-definition |  Enters the power sync definition mode. You can delete a power sync policy definition that you defined for the power sync policy.   
**Step 4** |  UCS-A /org/service-profile* # commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example deletes the local policy in use by the service profile. 
    
    
    UCS-A # **scope org**
    			 UCS-A/org # **scope service-profile spnew**
    			 UCS-A/org/service-profile # **delete power-sync-definition**
    			 UCS-A/org/service-profile* # **commit-buffer**
    			 

## Rack Server Power Management

Power capping is supported for all the Cisco UCS C-Series servers except Cisco UCS C125 M5 Servers. 

##  UCS Mini Power Management 

You can manage power of the blade servers in the Cisco UCS 6324 Fabric Interconnect (FI), which is used for remote offices and branch sites, and for limited server deployments. UCS Manager supports Dual Line Power Supply Unit and 110V when used with the Cisco UCS 6324 Fabric Interconnect. You can manage how you want to allocate power when using 110V power supplies, because they might not provide enough power for a fully loaded chassis. Dual power supplies is standard for both AC and DC-48V on the Cisco UCS Mini 6324. 

## Viewing X-Fabric Module (XFM) Fan Status

This procedure is applicable only for Cisco UCS X9508 Server Chassis equipped with XFM. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope chassis chassis-num |  Enters chassis mode for the specified chassis.   
**Step 2** |  UCS-A /chassis#  scope xfm xfm-num |  Enters the XFM specified in the command.  
**Step 3** |  UCS-A /chassis/xfm#  scope fan-module Tray-num Module-num |  Enters the specified fan tray in the specified module.  
**Step 4** |  UCS-A /chassis/xfm/fan-module#  scope fan fan-num |  Enters the specified fan module.  
**Step 5** |  UCS-A /chassis/xfm/fan-module/fan #  show detail |  Displays the following:
    
    
    Overall Status: 
        Operability: 
        Threshold Status: 
        Power State: 
        Presence: 
        Thermal Status: 
        Product Name: 
        PID: 
        VID: 
        Vendor: 
        Serial (SN): 
        HW Revision:   
  
### Example

Following examples show how to scope to XFM and see fan overall status:
    
    
    UCS-A# scope chassis 2
    UCS-A /chassis # scope xfm 1
    UCS-A /chassis/xfm # scope fan-module 1 1
    UCS-A /chassis/xfm/fan-module # scope fan 1
    UCS-A /chassis/xfm/fan-module/fan # show detail
    
    Fan:
        ID: 1
        Overall Status: Operable
        Operability: Operable
        Threshold Status: OK
        Power State: On
        Presence: Equipped
        Thermal Status: N/A
        Product Name: Fan Module for UCS 9508 Chassis IOM/XFM
        PID: UCSX-RSFAN
        VID: V01
        Vendor: Cisco Systems Inc
        Serial (SN): N/A
        HW Revision: 0
    

---

## Page 16: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_chapter_01000.html

# Blade Server Management

  * Blade Server Management
  * Guidelines for Removing and Decommissioning Blade Servers
  * Recommendations for Avoiding Unexpected Server Power Changes
  * Booting a Blade Server
  * Shutting Down a Blade Server
  * Power Cycling a Blade Server
  * Performing a Hard Reset on a Blade Server
  * Acknowledging a Blade Server
  * Removing a Blade Server from a Chassis
  * Decommissioning a Blade Server
  * Recommissioning a Blade Server
  * Turning On the Locator LED for a Blade Server
  * Turning Off the Locator LED for a Blade Server
  * Resetting the CMOS for a Blade Server
  * Resetting the CIMC for a Blade Server
  * Clearing TPM for a Blade Server
  * Resetting the BIOS Password for a Blade Server
  * Issuing an NMI from a Blade Server
  * Health LED Alarms
  * Smart SSD
  * Data Sanitization


## Blade Server Management 

You can manage and monitor all blade servers in a Cisco UCS domain through Cisco UCS Manager. You can perform some blade server management tasks, such as changes to the power state, from the server and service profile. 

The remaining management tasks can only be performed on the server. 

The power supply units go into power save mode when a chassis has two blades or less. When a third blade is added to the chassis and is fully discovered, the power supply units return to regular mode. 

If a blade server slot in a chassis is empty, Cisco UCS Manager provides information, errors, and faults for that slot. You can also re-acknowledge the slot to resolve server mismatch errors and to have Cisco UCS Manager rediscover the blade server in the slot. 

## Guidelines for Removing and Decommissioning Blade Servers 

Consider the following guidelines when deciding whether to remove or decommission a blade server using Cisco UCS Manager: 

### Decommissioning a Blade Server 

If you want to temporarily decommission a physically present and connected blade server, you can temporarily remove it from the configuration. A portion of the server's information is retained by Cisco UCS Manager for future use, in case the blade server is recommissioned. 

### Removing a Blade Server 

Removing is performed when you physically remove a blade server from the Cisco UCS Manager by disconnecting it from the chassis. You cannot remove a blade server from Cisco UCS Manager if it is physically present and connected to a chassis. After the physical removal of the blade server is completed, the configuration for that blade server can be removed in Cisco UCS Manager. 

During removal, active links to the blade server are disabled, all entries from databases are removed, and the server is automatically removed from any server pools that it was assigned to during discovery. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Only servers added to a server pool automatically during discovery are removed automatically. Servers that were manually added to a server pool must be removed manually. 

* * *  
  
---|---  
  
To add a removed blade server back to the configuration, it must be reconnected, then rediscovered. When a server is reintroduced to Cisco UCS Manager, it is treated as a new server and is subject to the deep discovery process. For this reason, it is possible for Cisco UCS Manager to assign the server a new ID that might be different from the ID that it held before. 

## Recommendations for Avoiding Unexpected Server Power Changes 

If a server is not associated with a service profile, you can use any available means to change the server power state, including the physical `Power` or `Reset` buttons on the server. 

If a server is associated with, or assigned to, a service profile, you should only use the following methods to change the server power state: 

  * In Cisco UCS Manager GUI, go to the General tab for the server or the service profile associated with the server and select Boot Server or Shutdown Server from the Actions area. 

  * In Cisco UCS Manager CLI, scope to the server or the service profile associated with the server and use the power up or power down commands. 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

Do _not_ use any of the following options on an associated server that is currently powered off: 

  * Reset in the GUI 
  * cycle cycle-immediate or reset hard-reset-immediate in the CLI 
  * The physical `Power` or `Reset` buttons on the server 


* * *  
  
---|---  
  
If you reset, cycle, or use the physical power buttons on a server that is currently powered off, the server's actual power state might become out of sync with the desired power state setting in the service profile. If the communication between the server and Cisco UCS Manager is disrupted or if the service profile configuration changes, Cisco UCS Manager might apply the desired power state from the service profile to the server, causing an unexpected power change. 

Power synchronization issues can lead to an unexpected server restart, as shown below: 

Desired Power State in Service Profile  |  Current Server Power State  |  Server Power State After Communication Is Disrupted   
---|---|---  
Up  |  Powered Off  |  Powered On   
Down  |  Powered On  |  Powered On  |  **Note** |  Running servers are not shut down regardless of the desired power state in the service profile.   
---|---  
  
## Booting a Blade Server 

### Before you begin

Associate a service profile with a blade server or server pool. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope org ` ` org-name |  Enters organization mode for the specified organization. To enter the root organization mode, type  / as the  org-name .   
**Step 2** |  UCS-A /org #  scope service-profile ` ` profile-name |  Enters organization service profile mode for the specified service profile.   
**Step 3** |  UCS-A /org/service-profile #  power up |  Boots the blade server associated with the service profile.   
**Step 4** |  UCS-A /org/service-profile #  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example boots the blade server associated with the service profile named ServProf34 and commits the transaction: 
    
    
    UCS-A# **scope org /**
    UCS-A /org* # **scope service-profile ServProf34**
    UCS-A /org/service-profile* # **power up**
    UCS-A /org/service-profile* # **commit-buffer**
    UCS-A /org/service-profile #
    

## Shutting Down a Blade Server 

When you use this procedure to shut down a server with an installed operating system, Cisco UCS Manager triggers the OS into a graceful shutdown sequence. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

When a blade server that is associated with a service profile is shut down, the VIF down alerts F0283 and F0479 are automatically suppressed. 

* * *  
  
---|---  
  
### Before you begin

Associate a service profile with a blade server or server pool. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope org ` ` org-name |  Enters organization mode for the specified organization. To enter the root organization mode, type / as the org-name.   
**Step 2** |  UCS-A /org #  scope service-profile ` ` profile-name |  Enters organization service profile mode for the specified service profile.   
**Step 3** |  UCS-A /org/service-profile #  power down |  Shuts down the blade server associated with the service profile.   
**Step 4** |  UCS-A /org/service-profile #  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example shuts down the blade server associated with the service profile named ServProf34 and commits the transaction: 
    
    
    UCS-A# **scope org /**
    UCS-A /org # **scope service-profile ServProf34**
    UCS-A /org/service-profile # **power down**
    UCS-A /org/service-profile* # **commit-buffer**
    UCS-A /org/service-profile #
    

## Power Cycling a Blade Server 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server ` ` chassis-num / server-num |  Enters chassis server mode for the specified blade server.   
**Step 2** |  UCS-A /chassis/server #  cycle ` `{cycle-immediate | cycle-wait}  |  Power cycles the blade server.  Use the  cycle-immediate keyword to immediately begin power cycling the blade server; use the  cycle-wait keyword to schedule the power cycle to begin after all pending management operations have completed.   
**Step 3** |  UCS-A#  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example immediately power cycles blade server 4 in chassis 2 and commits the transaction: 
    
    
    UCS-A# **scope server 2/4**
    UCS-A /chassis/server # **cycle cycle-immediate**
    UCS-A /chassis/server* # **commit-buffer**
    UCS-A /chassis/server # 
    

## Performing a Hard Reset on a Blade Server 

When you reset a server, Cisco UCS Manager sends a pulse on the reset line. You can choose to gracefully shut down the operating system. If the operating system does not support a graceful shutdown, the server is power cycled. The option to have Cisco UCS Manager complete all management operations before it resets the server does not guarantee the completion of these operations before the server is reset. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

If you are trying to boot a server from a power-down state, you should not use Reset.  If you continue the power-up with this process, the desired power state of the servers become out of sync with the actual power state and the servers might unexpectedly shut down at a later time. To safely reboot the selected servers from a power-down state, click Cancel, then select the Boot Server action. 

* * *  
  
---|---  
  
### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server ` ` chassis-num / server-num |  Enters chassis server mode for the specified server.   
**Step 2** |  UCS-A /chassis/server #  reset ` `{hard-reset-immediate | hard-reset-wait}  |  Performs a hard reset of the blade server.  Use the hard-reset-immediate keyword to immediately begin hard resetting the server; use the hard-reset-wait keyword to schedule the hard reset to begin after all pending management operations have completed.   
**Step 3** |  UCS-A /server #  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example performs an immediate hard reset of blade server 4 in chassis 2 and commits the transaction: 
    
    
    UCS-A#  scope server 2/4
    UCS-A /chassis/server # reset hard-reset-immediate
    UCS-A /chassis/server* # commit-buffer
    UCS-A /chassis/server # 
    

## Acknowledging a Blade Server 

Perform the following procedure to rediscover the server and all endpoints in the server. For example, you can use this procedure if a server is stuck in an unexpected state, such as the discovery state. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  acknowledge server ` ` chassis-num / server-num |  Acknowledges the specified blade server.   
**Step 2** |  UCS-A#  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example acknowledges server 4 in chassis 2 and commits the transaction: 
    
    
    UCS-A# **acknowledge server 2/4**
    UCS-A* # **commit-buffer**
    UCS-A # 
    

## Removing a Blade Server from a Chassis 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  remove server ` ` chassis-num / server-num |  Removes the specified blade server.   
**Step 2** |  UCS-A#  commit-buffer |  Commits the transaction to the system configuration.   
**Step 3** |  Go to the physical location of the chassis and remove the server hardware from the slot.  |  For instructions on how to remove the server hardware, see the Cisco UCS Hardware Installation Guide for your chassis.   
  
### Example

The following example removes blade server 4 in chassis 2 and commits the transaction: 
    
    
    UCS-A#  **remove server 2/4**
    UCS-A* # **commit-buffer**
    UCS-A # 
    

### What to do next

If you physically re-install the blade server, you must re-acknowledge the slot for the Cisco UCS Manager to rediscover the server. 

For more information, see Acknowledging a Blade Server. 

## Decommissioning a Blade Server 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  decommission server ` ` chassis-num / server-num |  Decommissions the specified blade server.   
**Step 2** |  UCS-A#  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example decommissions blade server 4 in chassis 2 and commits the transaction: 
    
    
    UCS-A# decommission server 2/4
    UCS-A* # commit-buffer
    UCS-A # 
    

### What to do next

After decommissioning the blade server, you must wait for few minutes to initiate the recommissioning of the server.

## Recommissioning a Blade Server

### Before you begin

Incase of recommissioning a blade server after decommission, you should wait for few minutes to initiate the recommission of the server. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  recommission server ` ` chassis-num / server-num |  Recommissions the specified blade server.   
**Step 2** |  UCS-A#  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example recommissions blade server 4 in chassis 2 and commits the transaction: 
    
    
    UCS-A# recommission server 2/4
    UCS-A* # commit-buffer
    UCS-A # 
    

## Turning On the Locator LED for a Blade Server 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server ` ` chassis-num / server-num |  Enters chassis server mode for the specified chassis.   
**Step 2** |  UCS-A /chassis/server #  enable locator-led [multi-master | multi-slave]  |  Turns on the blade server locator LED. For the Cisco UCS B460 M4 blade server, you can add the following keywords: 

  * multi-master—Turns on the LED for the master node only. 
  * multi-slave—Turns on the LED for the slave node only. 

  
**Step 3** |  UCS-A /chassis/server #  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example turns on the locator LED on blade server 4 in chassis 2 and commits the transaction: 
    
    
    UCS-A# scope server 2/4
    UCS-A /chassis/server # enable  locator-led
    UCS-A /chassis/server* # commit-buffer
    UCS-A /chassis/server # 
    
    

The following example turns on the locator LED for the master node only on blade server 7 in chassis 2 and commits the transaction: 
    
    
    UCS-A# scope chassis 2/7
    UCS-A /chassis/server # enable locator-led multi-master
    UCS-A /chassis/server* # commit-buffer
    UCS-A /chassis/server # 
    

## Turning Off the Locator LED for a Blade Server 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server chassis-num / server-num |  Enters chassis mode for the specified chassis.   
**Step 2** |  UCS-A /chassis/server #  disable locator-led [multi-master | multi-slave]  |  Turns off the blade server locator LED. For the Cisco UCS B460 M4 blade server, you can add the following keywords: 

  * multi-master—Turns off the LED for the master node only. 
  * multi-slave—Turns off the LED for the slave node only. 

  
**Step 3** |  UCS-A /chassis/server #  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example turns off the locator LED on blade server 4 in chassis 2 and commits the transaction: 
    
    
    UCS-A# scope chassis 2/4
    UCS-A /chassis/server # disable locator-led
    UCS-A /chassis/server* # commit-buffer
    UCS-A /chassis/server # 
    
    

The following example turns off the locator LED for the master node on blade server 7 in chassis 2 and commits the transaction: 
    
    
    UCS-A# scope chassis 2/7
    UCS-A /chassis/server # disable locator-led multi-master
    UCS-A /chassis/server* # commit-buffer
    UCS-A /chassis/server # 
    

## Resetting the CMOS for a Blade Server 

Sometimes, troubleshooting a server might require you to reset the CMOS. Resetting the CMOS is not part of the normal maintenance of a server. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server ` ` chassis-num / server-num |  Enters chassis server mode for the specified chassis.   
**Step 2** |  UCS-A /chassis/server #  reset-cmos |  Resets the CMOS for the blade server.   
**Step 3** |  UCS-A /chassis/server #  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example resets the CMOS for blade server 4 in chassis 2 and commits the transaction: 
    
    
    UCS-A# **scope server 2/4**
    UCS-A /chassis/server # **reset-cmos**
    UCS-A /chassis/server* # **commit-buffer**
    UCS-A /chassis/server #  
    

## Resetting the CIMC for a Blade Server 

Sometimes, with the firmware, troubleshooting a server might require you to reset the CIMC. Resetting the CIMC is not part of the normal maintenance of a server. After you reset the CIMC, the CIMC reboots the management controller of the blade server. 

If the CIMC is reset, the power monitoring functions of Cisco UCS become briefly unavailable until the CIMC reboots. Typically, the reset only takes 20 seconds; however, it is possible that the peak power cap can exceed during that time. To avoid exceeding the configured power cap in a low power-capped environment, consider staggering the rebooting or activation of CIMCs. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server ` ` chassis-num / server-num |  Enters chassis server mode for the specified chassis.   
**Step 2** |  UCS-A /chassis/server #  scope CIMC |  Enters chassis server CIMC mode   
**Step 3** |  UCS-A /chassis/server/CIMC #  reset |  Resets the CIMC for the blade server.   
**Step 4** |  UCS-A /chassis/server/CIMC #  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example resets the CIMC for blade server 4 in chassis 2 and commits the transaction: 
    
    
    UCS-A# **scope server 2/4**
    UCS-A /chassis/server # **scope CIMC**
    UCS-A /chassis/server/cimc # **reset**
    UCS-A /chassis/server/cimc* # **commit-buffer**
    UCS-A /chassis/server/cimc #  
    

## Clearing TPM for a Blade Server 

You can clear TPM only on Cisco UCS M4 blade and rack-mount servers that include support for TPM. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Clearing TPM is a potentially hazardous operation. The OS may stop booting. You may also see loss of data. 

* * *  
  
---|---  
  
### Before you begin

TPM must be enabled. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope server [chassis-num/server-num | dynamic-uuid]  |  Enters server mode for the specified server.   
**Step 2** |  UCS-A# /chassis/server # scope tpm tpm-ID |  Enters org TPM mode for the specified TPM.   
**Step 3** |  UCS-A# /chassis/server/tpm # set adminaction clear-config |  Specifies that the TPM is to be cleared.   
**Step 4** |  UCS-A# /chassis/server/tpm # commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example shows how to clear TPM for a blade server: 
    
    
    UCS-A# **scope server 1/3**
    UCS-A# /chassis/server # **scope tpm 1**
    UCS-A# /chassis/server/tpm # **set adminaction clear-config**
    UCS-A#/chassis/server/tpm* # **commit-buffer**
    
    
    
    

## Resetting the BIOS Password for a Blade Server

This option allows you to reset the BIOS password without using the F2 BIOS configuration prompt. Resetting the BIOS password is not part of the normal maintenance of a server. After the BIOS password reset, the server is rebooted immediately and the new BIOS password gets updated. 

### Procedure

* * *

**Step 1** |  UCS-A#  scope server ` ` chassis-num / server-num Enters chassis server mode for the specified chassis.   
---|---  
**Step 2** |  UCS-A /chassis/server #  reset-bios-password Resets the BIOS password for the blade server.   
**Step 3** |  UCS-A /chassis/server #  commit-buffer Commits the transaction to the system configuration.   
  
* * *

## Issuing an NMI from a Blade Server 

Perform the following procedure if the system remains unresponsive and you need Cisco UCS Manager to issue a Non-Maskable Interrupt (NMI) to the BIOS or operating system from the CIMC. This action creates a core dump or stack trace, depending on the operating system installed on the server. 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope server [chassis-num/server-num | dynamic-uuid]  |  Enters server mode for the specified server.   
**Step 2** |  UCS-A /chassis/server # diagnostic-interrupt |   
**Step 3** |  UCS-A /chassis/server* # commit-buffer |  Commits any pending transactions.   
  
### Example

The following example sends an NMI from server 4 in chassis 2 and commits the transaction: 
    
    
    UCS-A# **scope server 2/4**
    UCS-A /chassis/server # **diagnostic-interrupt**
    UCS-A /chassis/server* # **commit-buffer**
    UCS-A /chassis/server # 
    

## Health LED Alarms

The blade health LED is located on the front of each Cisco UCS B-Series blade server. Cisco UCS Manager allows you to view the sensor faults that cause the blade health LED to change color from green to amber or blinking amber. 

The health LED alarms display the following information:

Name  | Description   
---|---  
Severity column |  The severity of the alarm. This can be one of the following:

  * Critical—The blade health LED is blinking amber. 
  * Minor—The blade health LED is amber. 

  
Description column |  A brief description of the alarm.  
Sensor ID column |  The ID of the sensor the triggered the alarm.  
Sensor Name column |  The name of the sensor that triggered the alarm.  
  
## Smart SSD

Beginning with release 3.1(3), Cisco UCS Manager supports monitoring SSD health. This feature is called Smart SSD. It provides statistical information about the properties like wear status in days, percentage life remaining, and so on. For every property, a minimum, a maximum and an average value is recorded and displayed. The feature also allows you to provide threshold limit for the properties. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The Smart SSD feature is supported only for a selected range of SSDs. It is not supported for any HDDs. 

* * *  
  
---|---  
  
The SATA range of supported SSDs are: 

  * Intel

  * Samsung 

  * Micron 


The SAS range of supported SSDs are: 

  * Toshiba 

  * Sandisk 

  * Samsung 

  * Micron 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

  * Power Cycle Count is not available on SAS SSDs. 
  * Smart SSD feature is supported only on M5 servers and later. 


* * *  
  
---|---  
  
  * Viewing SSD Health Statistics


### Viewing SSD Health Statistics 

Perform this procedure to view the SSD Health statistics. 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server chassis-id / server-id |  Enters chassis server mode for the specified server.   
**Step 2** |  UCS-A /chassis/server #  show stats |  Displays the SSD health statistics for the specified server.   
  
#### Example

The following example displays the SSD health statistics for blade 3 in chassis 1: 
    
    
    UCS-A# **scope server 1/3**
    UCS-A /chassis/server # **show stats**
    
    Ssd Health Stats:
        Time Collected: 2016-12-07T19:35:15.920
        Monitored Object: sys/chassis-1/blade-3/board/storage-SAS-1/ssd-health-stats-1
        Suspect: No
        Id: 1
        Power Cycle Count: 1022
        Power On Hours: 4793
        Percentage Life Left: 92
        Wear Status In Days: 1679
        Thresholded: 0
    
        Time Collected: 2016-12-07T19:35:38.912
        Monitored Object: sys/chassis-1/blade-3/board/storage-SAS-1/ssd-health-stats-2
        Suspect: No
        Id: 2
        Power Cycle Count: 1017
        Power On Hours: 4270
        Percentage Life Left: 87
        Wear Status In Days: 1587
        Thresholded: 0
    
        Time Collected: 2016-12-07T19:35:15.920
        Monitored Object: sys/chassis-1/blade-3/board/storage-SAS-4/ssd-health-stats-1
        Suspect: No
        Id: 1
        Power Cycle Count: 1506
        Power On Hours: 5029
        Percentage Life Left: 98
        Wear Status In Days: 1788
        Thresholded: 0
            
        Time Collected: 2016-12-07T19:35:15.920
        Monitored Object: sys/chassis-1/blade-3/board/storage-SAS-4/ssd-health-stats-2
        Suspect: No
        Id: 2
        Power Cycle Count: 58
        Power On Hours: 4731
        Percentage Life Left: 100
        Wear Status In Days: 1825
        Thresholded: 0
    UCS-A /chassis/server #
    
    

## Data Sanitization

Beginning with release 4.3(4a), Cisco UCS Manager supports data sanitization feature. Using the data sanitization process, Cisco UCS Manager erases all sensitive data, thus making extraction or recovery of data impossible. As Cisco UCS Manager progresses through the erase process, the status report is updated. You can check the status and progress of the data sanitization process for each individual device erase from the report, identify and rectify any issues, if required. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

  * You must perform data sanitization on the components that contain data.
  * This feature is supported on all the Cisco UCS C-Series, B-Series, and X-Series servers.


* * *  
  
---|---  
  
Erase process for data sanitization is performed in the following order on the server components:

  * Storage components

  * Network adapters

  * NVDIMMs

  * BIOS and BMC components


You can choose to either perform data sanitization on all the server components or select only VIC and Storage components for data sanitization. During the data sanitization process, the Cisco UCS server reboots and is subsequently decommissioned after the sanitization is finalized. In the event that the sanitization process is interrupted because of any issue, you must troubleshoot and resolve the issue and then recommence the data sanitization procedure. 

  * Performing Data Sanitization on Blade Servers
  * Performing Data Sanitization on Rack Servers


### Performing Data Sanitization on Blade Servers

Data sanitization may take several hours to finish depending on the amount of data. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

You cannot perform any other server operation while data sanitization is in progress.

* * *  
  
---|---  
  
#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server chassis-num/server-num |  Enters chassis server mode for the specified server.   
**Step 2** |  UCS-A /chassis/server # data-sanitize  all|board|host |  Performs the selected data sanitization.

  * Host—Storage components, network adapters, NVDIMMs
  * Board—BIOS and BMC components
  * All—Includes both the host and board components.

  
**Step 3** |  UCS-A /chassis/server* # commit buffer  |   
  
#### Example

Following example performs host data sanitization for server 4 in chassis 2:
    
    
    UCS-A # scope server 2/4
    UCS-A /chassis/server # data sanitize host
    Warning: Data sanitization is a destructive and long-running operation. Data on                                                                     the selected component will be completely erased.
    Warning: The server will be decommissioned on successful data sanitization.
    UCS-A /chassis/server* # commit buffer
    UCS-A /chassis/server #

---

## Page 17: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_chapter_01110.html

# Overview

## Cisco UCS Manager User CLI Documentation

Cisco UCS Manager offers you a new set of smaller, use-case based documentation described in the following table: 

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
  
## Cisco Unified Computing System Overview 

Cisco UCS has a unique architecture that integrates compute, data network access, and storage network access into a common set of components under a single-pane-of-glass management interface. 

Cisco UCS fuses access layer networking and servers. This high-performance, next-generation server system provides a data center with a high degree of workload agility and scalability. The hardware and software components support Cisco's unified fabric, which runs multiple types of data center traffic over a single converged network adapter. 

Figure 1. Cisco Unified Computing System Architecture  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/305001-306000/305219.jpg)

### Architectural Simplification 

The simplified architecture of Cisco UCS reduces the number of required devices and centralizes switching resources. By eliminating switching inside a chassis, network access-layer fragmentation is significantly reduced. Cisco UCS implements Cisco unified fabric within racks and groups of racks, supporting Ethernet and Fibre Channel protocols over 10 Gigabit Cisco Data Center Ethernet and Fibre Channel over Ethernet (FCoE) links. This radical simplification reduces the number of switches, cables, adapters, and management points by up to two-thirds. All devices in a Cisco UCS domain remain under a single management domain, which remains highly available through the use of redundant components. 

### High Availability 

The management and data plane of Cisco UCS is designed for high availability and redundant access layer fabric interconnects. In addition, Cisco UCS supports existing high availability and disaster recovery solutions for the data center, such as data replication and application-level clustering technologies. 

### Scalability

A single Cisco UCS domain supports multiple chassis and their servers, all of which are administered through one Cisco UCS Manager. For more detailed information about the scalability, speak to your Cisco representative. 

### Flexibility

A Cisco UCS domain allows you to quickly align computing resources in the data center with rapidly changing business requirements. This built-in flexibility is determined by whether you choose to fully implement the stateless computing feature. Pools of servers and other system resources can be applied as necessary to respond to workload fluctuations, support new applications, scale existing software and business services, and accommodate both scheduled and unscheduled downtime. Server identity can be abstracted into a mobile service profile that can be moved from server to server with minimal downtime and no need for additional network configuration. 

With this level of flexibility, you can quickly and easily scale server capacity without having to change the server identity or reconfigure the server, LAN, or SAN. During a maintenance window, you can quickly do the following: 

  * Deploy new servers to meet unexpected workload demand and rebalance resources and traffic. 

  * Shut down an application, such as a database management system, on one server and then boot it up again on another server with increased I/O capacity and memory resources. 


### Optimized for Server Virtualization 

Cisco UCS has been optimized to implement VM-FEX technology. This technology provides improved support for server virtualization, including better policy-based configuration and security, conformance with a company's operational model, and accommodation for VMware's VMotion. 

## IOMs and Fabric Interconnects Connectivity

Each chassis is equipped with two IOMs: IOM 1 should be connected to Fabric Interconnect A. IOM 2 should be connected to Fabric Interconnect B. This configuration provides redundant paths, ensuring uninterrupted operation of the Cisco UCS system even in the event of a failure in one of the Fabric Interconnects or IOMs. Additionally, this configuration enables traffic load distribution across both Fabric Interconnects, enhancing load balancing and increasing throughput. As a result, the Cisco UCS system achieves high availability, reliability, and optimal performance, making it ideal for data center environments. 

  * Uplink Connectivity
  * Downlink Connectivity


### Uplink Connectivity 

Use fabric interconnect ports configured as uplink ports to connect to uplink upstream network switches. Connect these uplink ports to upstream switch ports as individual links, or as links configured as port channels. Port channel configurations provide bandwidth aggregation as well as link redundancy. 

You can achieve northbound connectivity from the fabric interconnect through a standard uplink, a port channel, or a virtual port channel configuration. The port channel name and ID configured on fabric interconnect should match the name and ID configuration on the upstream Ethernet switch. 

It is also possible to configure a port channel as a vPC, where port channel uplink ports from a fabric interconnect are connected to different upstream switches. After all uplink ports are configured, create a port channel for these ports. 

### Downlink Connectivity 

Beginning with release 4.3(2a), Cisco UCS Manager supports Cisco UCS X9508 server chassis with Cisco UCS X-Series servers. Cisco UCS X-Series servers support Intelligent Fabric Modules (IFM), which function similarly to the Input/Output Module (IOM) in Cisco UCS B-Series servers. This guide uses the term IOM to refer both IOM and IFM.

Each fabric interconnect is connected to IOMs in the UCS chassis, which provides connectivity to each blade server. Internal connectivity from blade servers to IOMs is transparently provided by Cisco UCS Manager using 10BASE-KR Ethernet standard for backplane implementations, and no additional configuration is required. You must configure the connectivity between the fabric interconnect server ports and IOMs. Each IOM, when connected with the fabric interconnect server port, behaves as a line card to fabric interconnect, hence IOMs should never be cross-connected to the fabric interconnect. Each IOM is connected directly to a single fabric interconnect. 

The Fabric Extender (also referred to as the IOM, or FEX) logically extends the fabric interconnects to the blade server. The best analogy is to think of it as a remote line card that’s embedded in the blade server chassis, allowing connectivity to the external world. IOM settings are pushed via Cisco UCS Manager and are not managed directly. The primary functions of this module are to facilitate blade server I/O connectivity (internal and external), multiplex all I/O traffic up to the fabric interconnects, and help monitor and manage the Cisco UCS infrastructure. 

Configure Fabric interconnect ports that should be connected to downlink IOM cards as server ports. Make sure there is physical connectivity between the fabric interconnect and IOMs. You must also configure the IOM ports and the global chassis discovery policy. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For UCS 2200 I/O modules, you can also select the Port Channel option and all I/O module-connected server ports will be automatically added to a port channel. 

* * *  
  
---|---  
  
## Cisco UCS Building Blocks and Connectivity

Figure 2. Cisco UCS Building Blocks and Connectivity 

The primary components included within Cisco UCS Manager are as follows:

  * Cisco UCS Manager—Cisco UCS Manager is the centralized management interface for Cisco UCS. For more information on Cisco UCS Manager, see Introduction to Cisco UCS Manager in Cisco UCS Manager Getting Started Guide

  * Cisco UCS Fabric Interconnects—The Cisco UCS Fabric Interconnect is the core component of Cisco UCS deployments, providing both network connectivity and management capabilities for the Cisco UCS system. The Cisco UCS Fabric Interconnects run the Cisco UCS Manager control software and consist of the following components: 

  * Cisco UCS fabric interconnects:

  * Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct) 

  * Cisco UCS 6536 Fabric Interconnect

  * Cisco UCS 6400 Series Fabric Interconnect

  * Cisco UCS 6332 Series Fabric Interconnects

  * Cisco UCS-FI-6324 (Cisco UCS Mini)

  * Transceivers for network and storage connectivity

  * Expansion modules for various Fabric Interconnects

  * Cisco UCS Manager software

For more information on Cisco UCS Fabric Interconnects, see Cisco UCS Fabric Infrastructure Portfolio. 

  * Cisco UCS I/O Modules and Cisco UCS Fabric Extender—IO modules are also known as Cisco FEX or simply FEX modules. These modules serve as line cards to the FIs in the same way that Cisco Nexus Series switches can have remote line cards. IO modules also provide interface connections to blade servers. They multiplex data from blade servers and provide this data to FIs and do the same in the reverse direction. In production environments, IO modules are always used in pairs to provide redundancy and failover. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

The 40G backplane setting is not applicable for 22xx IOMs. 

* * *  
  
---|---  
  * Cisco UCS Blade Server Chassis—The Cisco UCS 5100 Series Blade Server Chassis is a crucial building block of Cisco UCS, delivering a scalable and flexible architecture for current and future data center needs, while helping reduce total cost of ownership. 

  * Cisco UCS Blade and Rack Servers—Cisco UCS Blade servers are at the heart of the UCS solution. They come in various system resource configurations in terms of CPU, memory, and hard disk capacity. The Cisco UCS rack-mount servers are standalone servers that can be installed and controlled individually. Cisco provides Fabric Extenders (FEXs) for the rack-mount servers. FEXs can be used to connect and manage rack-mount servers from FIs. Rack-mount servers can also be directly attached to the fabric interconnect. 

Small and Medium Businesses (SMBs) can choose from different blade configurations as per business needs.

  * Cisco UCS I/O Adapters—Cisco UCS B-Series Blade Servers are designed to support up to two network adapters. This design can reduce the number of adapters, cables, and access-layer switches by as much as half because it eliminates the need for multiple parallel infrastructure for both LAN and SAN at the server, chassis, and rack levels. 


  * Cisco UCS Fabric Infrastructure Portfolio
  * Cisco UCS Chassis
  * Cisco UCS Mini Infrastructure
  * Cisco UCS Infrastructure Virtualization


### Cisco UCS Fabric Infrastructure Portfolio

The Cisco UCS fabric interconnects are top-of-rack devices and provide unified access to the Cisco UCS domain. The following fabric interconnects are available in the Cisco UCS fabric interconnects product family: 

  * Cisco UCS Manager Release 4.3(4b) introduces Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct). 

  * Cisco UCS Manager Release 4.2(3b) introduces Cisco UCS 6536 Fabric Interconnect to the Cisco UCS 6500 Series Fabric Interconnects. 

  * Cisco UCS Manager Release 4.1 introduces the Cisco UCS 64108 Fabric Interconnect to the Cisco UCS 6400 Series Fabric Interconnects. 

  * Cisco UCS 6300 Series Fabric Interconnects

  * Cisco UCS 6324 Fabric Interconnects


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The Cisco UCS 6200 Series, Cisco UCS 6100 Series Fabric Interconnects, and Cisco UCS 2104 I/O Modules have reached end of life. 

* * *  
  
---|---  
  
Cisco UCS X-Series Direct

### Overview of Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct) 

The Cisco UCS X-Series Direct is identified by the product ID UCSX-S9108-100G, and the product description Cisco UCS Fabric Interconnects 9108 100G. 

Components of Cisco UCS Fabric Interconnects 9108 100G:

  * Cisco UCS X9508 Chassis

  * A pair of Cisco UCS Fabric Interconnects 9108 100G

  * One or more of Cisco UCS X-Series M6, M7, and M8 Compute Nodes

  * Optional components:

  * Cisco UCS 9416 X-Fabric Modules

  * Cisco UCS X440p PCIe Node with up to four GPUs used in conjunction with the 9416 X-Fabric Modules


The Cisco UCS Fabric Interconnects 9108 100G platform streamlines data center architecture by eliminating the need for separate Fabric Interconnects (FIs), integrating essential networking and management functionality directly within the chassis. The Cisco UCS Fabric Interconnects 9108 100G platform is designed for deployments in smaller settings, where the compute server requirements are less extensive than those of a traditional data center. This solution is centered around a single-chassis system, the Cisco UCS X9508 Chassis, which incorporates Cisco UCS Fabric Interconnects 9108 100G directly into the chassis for a consolidated and efficient infrastructure. To ensure high availability, each chassis houses two Cisco UCS Fabric Interconnects 9108 100G that establish direct downlink connections to servers and provide uplink connections to facilitate seamless integration with both Local Area Network (LAN) and Storage Area Network (SAN) systems. The Fabric Interconnects (FIs) are adeptly designed to fit into the Cisco UCS X-Series chassis, presenting as a single module within the NX-OS environment that merges QSFP ports with server backplane ports. 

The hardware configuration of the Cisco UCS Fabric Interconnects 9108 100G platform retains the same form factor as the standard Cisco UCS X-Series chassis, and features 17 MACs, each configurable for 10G, 25G, 40G, or 100G connectivity. It is equipped with an CPU, for operating NX-OS, Cisco UCS Manager for management and Chassis Management Controller (CMC) software. The Cisco UCS Fabric Interconnects 9108 100G includes an onboard Ethernet switch with multiple 10G links dedicated to out-of-band communication between blade components such as the Baseboard Management Controller (BMC), CMC. A dedicated 1G link facilitates IFM-to-IFM clustering and high availability synchronization. Within the Cisco UCS Fabric Interconnects 9108 100G, Ethernet ports 1-8, backplane ports 9-16, and the Baseboard Interface (BIF) port 17 coexist on a singular switch card. Ports 1-2 are unified to manage all SAN features and configurations. The 100G Ethernet ports [1-8] can also be configured as 25Gx4 SFP28 compatible breakout ports or 4x10G ports, offering flexible networking solutions to accommodate a range of data center needs. 

### Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct) Architecture 

The Cisco UCS X-Series Direct architecture is engineered to support a diverse range of workloads, from traditional applications to cloud-native services, by offering a composable and disaggregated approach to computing resources. Key components of the Cisco UCS X-Series Direct architecture include: 

  * **Cisco UCSX-9508 Chassis** —A modular and future-proof chassis that can accommodate various types of compute nodes, providing the flexibility to adapt to different workload requirements without the need for a complete hardware overhaul. 

  * **Cisco UCS Fabric Interconnects 9108 100G** —This solution is centered around a single-chassis system, the Cisco UCS X9508 Chassis, which incorporates Cisco UCS Fabric Interconnects 9108 100G directly into the chassis for a consolidated and efficient infrastructure. To ensure high availability, each chassis houses two Cisco UCS Fabric Interconnects 9108 100G that establish direct downlink connections to servers and provide uplink connections to facilitate seamless integration with both Local Area Network (LAN) and Storage Area Network (SAN) systems. 

  * **Software Architecture** —In terms of the startup and operational model, the management, Cisco UCS Manager aligns with the approach taken in the Cisco UCS 6500 and 6400 Series Fabric Interconnects. In this model, Cisco UCS Manager is encapsulated within a container and is initiated by the underlying NX-OS, depending on the selected management mode. 


### Port Breakout Functionality on Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct) 

The Cisco UCS Fabric Interconnects 9108 100G is equipped with advanced port breakout functionality, which allows network administrators to subdivide a single high-bandwidth port into multiple lower-bandwidth ports. This feature is particularly beneficial for optimizing port utilization, managing cabling complexity, and adapting to various bandwidth requirements. 

Physical Port |  Breakout Options |  Logical Ports After Breakout |  Supported Speeds through breakout cables  
---|---|---|---  
Ethernet 1/1 - Ethernet 1/8 |  4x25G |  Ethernet 1/1/1 to Ethernet 1/8/4 |  Up to 8x100 Gbps  
Fibre Channel 1/1 and 1/2 |  4x8G, 4x16G, 4x32G |  Fibre Channel 1/1/1 to Fibre Channel 1/2/4 |  Up to 8x32Gbps  
  
#### Breakout Port Guidelines

Breakout ports are supported as destinations for traffic monitoring. The following are the guidelines for breakout functionality for Cisco UCS Fabric Interconnects 9108 100G: 

  * Breakout Availability: Breakout functionality is available for physical ports 1-8. 

  * Ethernet Breakout: Ethernet breakout ports can be configured on physical ports 1 through 8, resulting in 32 logical ports. 

  * Fibre Channel Breakout: Fibre Channel breakout ports can be configured on unified ports 1/8 and 2/8, resulting in 8 logical ports. 

  * Port Configurations: Physical Ports 1-8 can be configured as Uplink Ports, FCoE Uplink Ports, FCoE Storage Ports, and Appliance Ports. 

  * Port Conversions: All port conversions support up to 8 standard ports or 8 breakout ports. 

  * Server Ports: Configuration as Server Ports is not supported. 

  * Fibre Channel Direct Ports: Direct ports for Fibre Channel are not supported. 

  * Traffic Monitoring: Breakout ports can be utilized as destinations for traffic monitoring. 


Cisco UCS 6500 Series Fabric Interconnects

###  Cisco UCS 6536 Fabric Interconnect Overview 

The Cisco UCS 6536 Fabric Interconnect is a core part of the Cisco Unified Computing System, providing both network connectivity and management capabilities for the system. The Cisco UCS 6536 Fabric Interconnect provides the communication backbone and management connectivity for UCS B-series blade servers and UCS C-series rack servers. 

Cisco UCS 6500 Series Fabric Interconnects currently include Cisco UCS 6536 Fabric Interconnect. All servers attached to a Cisco UCS 6536 Fabric Interconnect become part of a single, highly available management domain. In addition, by supporting a unified fabric, Cisco UCS 6536 Fabric Interconnect provides both LAN and SAN connectivity for all servers within its domain. 

The Cisco UCS 6536 Fabric Interconnect supports multiple traffic classes over a lossless Ethernet fabric from the server through the fabric interconnect. 

### Port Breakout Functionality on Cisco UCS 6536 Fabric Interconnects

The Cisco UCS 6536 36-Port Fabric Interconnect is a One-Rack-Unit (1RU) 1/10/25/40/100 Gigabit Ethernet, FCoE, and Fibre Channel switch offering up to 7.42 Tbps throughput and up to 36 ports. 

Cisco UCS 6536 Fabric Interconnect supports splitting a single 40 Gigabit(G)/100G Quad Small Form-factor Pluggable (QSFP) port into four 10G/25G ports using a supported breakout cable. The switch has 32 40/100-Gbps Ethernet ports and four unified ports that can support 40/100-Gbps Ethernet ports or 16 Fiber Channel (FC) ports after breakout at 8/16/32-Gbps FC speeds. The 16 FC ports after breakout can operate as an FC Uplink or FC storage port. The switch also supports two ports (Port 9 and Port 10) at 1-Gbps speed using QSA, and all 36 ports can breakout for 10 or 25 Gbps Ethernet connectivity. All Ethernet ports can support FCoE. 

Port breakout is supported for Ethernet ports (1-32) and Unified ports (33-36). These 40/100G ports are numbered in a 2-tuple naming convention. The process of changing the configuration from 40G to 10G, or from 100G to 25G is called breakout, and the process of changing the configuration from [4X]10G to 40G or from [4X]25G to 100G is called unconfigure. 

When you break out a 40G port into 10G ports or a 100G port into 25G ports, the resulting ports are numbered using a 3-tuple naming convention. For example, the breakout ports of the second 40-Gigabit Ethernet port are numbered as 1/31/1, 1/31/2, 1/31/3, and 1/31/4. 

FC breakout is supported on ports 36 through 33 when each port is configured with a four-port breakout cable. For example: Four FC breakout ports on the physical port 33 are numbered as 1/33/1, 1/33/2, 1/33/3, and 1/33/4. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Fibre Channel support is only available through the configuration of the Unified Ports (36-33) as Fibre Channel breakout port.

* * *  
  
---|---  
  
The following image shows the rear view of the Cisco UCS 6536 fabric interconnect:

Figure 3. Cisco UCS 6536 Fabric Interconnect Rear View  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540805.jpg)

The following image shows the rear view of the Cisco UCS 6536 fabric interconnect that include Ports and LEDs:

Figure 4. Cisco UCS 6536 Fabric Interconnect Rear View  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540989.jpg) 1  |  Ports 1-32. Uplink ports are Ethernet port that can operate with the port speed of 10 Gbps/25 Gbps/40 Gbps/100 Gbps. When using a breakout cable, each of these ports can operate as: 4 x 10 Gbps/4x 25 Gbps/1 x 40 Gbps/1 x 100 Gbps Ethernet or FCoE ports.  |  2  |  Ports 33-36. Unified Ports can operate with port speed of 10 Gbps/25 Gbps/ 40 Gbps/100 Gbps Ethernet. or  8 Gbps/16 Gbps/32 Gbps Fibre Channel (FC). When using a breakout cable, each of these ports can operate as 4 x 10 Gbps/4 x 25 Gbps Ethernet or 4x8Gbps/4x16Gbps/4x32Gbps FC ports.   
---|---|---|---  
3  |  Ports 1-36. Uplink ports and Unified ports that can be configured as Ethernet Breakout Port and can operate with the port speed of 10 Gbps/25 Gbps/40 Gbps/100 Gbps.  When using a breakout cable, each of these ports can operate as: 4 x 10 Gbps/4x 25 Gbps/1 x 40 Gbps/1 x 100 Gbps Ethernet or FCoE ports.  |  4 | System environment (fan fault) LED  
5 |  System status (STS) LED |  6 |  Beacon (BCN) LED  
  
#### Breakout Port Guidelines

The following are the guidelines for breakout functionality for Cisco UCS 6536 Fabric Interconnects: 

  * The configurable breakout ports are from port 1-36.

  * You can configure the speed for each breakout port. Each breakout port can be configured at the speed of 4 x 8 Gbps/ 4 x 16 Gbps/ 4 x 32 Gbps for Fibre Channel. 

  * For Fibre Channel breakout, each breakout port can be configured at the speed of 4 x 8 Gbps/ 4 x 16 Gbps/ 4 x 32 Gbps.

  * For Ethernet breakout, each breakout port can be configured at the speed of 4 x 10 Gbps/4 x 25 Gbps.

  * Fibre Channel breakout ports are supported, and Fiber Channel direct ports are not supported.

  * FC breakout port can be configured from 1/36 through 1/33. FC breakout ports (36-33) cannot be configured unless the previous ports are FC breakout ports. Configuration of a single (individual) FC breakout port is also supported. 

  * If the breakout mode for any of the supported Fabric Interconnect ports (1-36) is an Ethernet breakout, the Fabric Interconnect does not lead to a reboot. 

  * If the breakout mode for any of the supported Fabric Interconnect ports (36-33) is a Fibre Channel uplink breakout, the Fabric Interconnect leads to a reboot. 

  * Breakout ports are supported as destinations for traffic monitoring.

  * Ports 1-36 can be configured as Server Port, FCoE Uplink Port, Appliance Port, and Monitor Port.

  * Port 36-33 can be configured also as FC Uplink Port or FC Storage Port when configured as unified port.


Cisco UCS 6400 Series Fabric Interconnects

### Cisco UCS 6400 Series Fabric Interconnect Overview 

Cisco UCS 6400 Series Fabric Interconnect provides both network connectivity and management capabilities to the Cisco UCS system. The fabric interconnect provides Ethernet and Fibre Channel to the servers in the system, the servers connect to the fabric interconnect, and then to the LAN or SAN. 

Each Cisco UCS 6400 Series Fabric Interconnect runs Cisco UCS Manager to fully manage all Cisco UCS elements. The fabric interconnect supports 10/25 Gigabit ports in the fabric with 40/100 Gigabit uplink ports. High availability can be achieved when a Cisco UCS 6400 Series Fabric Interconnect is connected to another Cisco UCS 6400 Series Fabric Interconnect through the L1 or L2 port on each device. 

Cisco UCS 6400 Series Fabric Interconnect consists of: 

  * Cisco UCS 6454 Fabric Interconnects 

  * Cisco UCS 64108 Fabric Interconnects 


The Cisco UCS 6400 Series fabric interconnect supports Cisco UCS B-Series Blade Servers, UCS 5108 B-Series Server Chassis, C-Series Rack Servers, and UCS S-Series Storage Servers. 

### Cisco UCS 64108 Fabric Interconnect

The Cisco UCS 64108 Fabric Interconnect is a 2 RU top-of-rack (TOR) switch that mounts in a standard 19-inch rack such as the Cisco R Series rack. 

The high-density Cisco UCS 64108 Fabric Interconnect has 96 10/25 Gb SFP28 ports and 12 40/100 Gb QSFP28 ports. Each 40/100 Gb port can break out into 4 x 10/25 Gb uplink ports. Ports 1 - 16 are unified ports that support 10/25 GbE or 8/16/32G Fibre Channel speeds. Ports 89-96 support 1Gbps Ethernet speeds. 

The Cisco UCS 64108 Fabric Interconnect supports either: 

  * Eight FCoE port channels

  * Or Four SAN port channels

  * or Four SAN port channels and four FCoE port channels


The Cisco UCS 64108 Fabric Interconnect also has one network management port, one RS-232 serial console port for setting the initial configuration, and one USB port for saving or loading configurations. The FI also includes L1/L2 ports for connecting two fabric interconnects in a high-availability configuration. 

The Cisco UCS 64108 Fabric Interconnect also contains a CPU board that consists of: 

  * Intel Xeon Processor, 6 core

  * 64 GB of RAM 

  * 8 MB of NVRAM (4 x NVRAM chips)

  * 128 GB SSD (bootflash)


Figure 5. Cisco UCS 64108 Fabric Interconnect Rear View ![](/c/dam/en/us/td/i/300001-400000/300001-310000/307001-308000/307644.jpg) 1  |  Ports 1-16  Unified ports:

  * 10/25 Gbps Ethernet or FCoE
  * 8/16/32 Gbps Fibre Channel

|  2  |  Ports 17-88 (10/25 Gbps Ethernet or FCoE)  
---|---|---|---  
3  |  Ports 89-96

  * 10/25 Gbps Ethernet or FCoE
  * 1 Gbps Ethernet

|  4 |  Uplink Ports 97-108 (40/100 Gbps Ethernet or FCoE) Each of these ports can be 4 x 10/25 Gbps Ethernet or FCoE uplink ports when using a breakout cable.  
5 |  System environment (fan fault) LED |  6 |  System status LED  
7 |  Beacon LED |  |   
  
The Cisco UCS 64108 Fabric Interconnect has two power supplies (redundant as 1+1) and three fans (redundant as 2+1). 

Figure 6. Cisco UCS 64108 Fabric Interconnect Front View ![](/c/dam/en/us/td/i/300001-400000/300001-310000/307001-308000/307645.jpg) **1** |  Cooling fans (hot swappable, 2+1 redundancy) |  **2** |  RS-232 serial console port (RJ-45 connector)  
---|---|---|---  
**3** |  Network management port (RJ-45 connector) |  4 |  USB port  
5 |  Grounding pad for two-hole grounding lug (under protective label) |  6 |  Power supplies Two identical AC or DC PSUs, hot-swappable, 1+1 redundancy)  
7 |  L1/L2 high-availability ports (RJ-45 connector) |  8 |  Beacon LED  
9 |  System status LED |  |   
  
### Cisco UCS 6454 Fabric Interconnect

The Cisco UCS 6454 Fabric Interconnect (FI) is a 1-RU top-of-rack switch that mounts in a standard 19-inch rack such as the Cisco R Series rack. 

The Cisco UCS 6454 Fabric Interconnect has 48 10/25 Gb SFP28 ports (16 unified ports) and 6 40/100 Gb QSFP28 ports. Each 40/100 Gb port can break out into 4 x 10/25 Gb uplink ports. The sixteen unified ports support 10/25 GbE or 8/16/32G Fibre Channel speeds. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The Cisco UCS 6454 Fabric Interconnect supported 8 unified ports (ports 1 - 8) with Cisco UCS Manager 4.0(1) and 4.0(2), but with release 4.0(4) and later it supports 16 unified ports (ports 1 - 16). 

* * *  
  
---|---  
  
The Cisco UCS 6454 Fabric Interconnect supports: 

  * Maximum of 8 FCoE port channels

  * Or 4 SAN port channels

  * Or a maximum of 8 SAN port channels and FCoE port channels (4 each)


The Cisco UCS 6454 Fabric Interconnect also has one network management port, one console port for setting the initial configuration, and one USB port for saving or loading configurations. The FI also includes L1/L2 ports for connecting two fabric interconnects for high availability. 

The Cisco UCS 6454 Fabric Interconnect also contains a CPU board that consists of: 

  * Intel Xeon D-1528 v4 Processor, 1.6 GHz

  * 64 GB of RAM 

  * 8 MB of NVRAM (4 x NVRAM chips)

  * 128 GB SSD (bootflash)


Figure 7. Cisco UCS 6454 Fabric Interconnect Rear View ![](/c/dam/en/us/td/i/300001-400000/300001-310000/306001-307000/306755.jpg) 1  |  Ports 1-16 (Unified Ports 10/25 Gbps Ethernet or FCoE or 8/16/32 Gbps Fibre Channel) |  **Note** |  When using Cisco UCS Manager releases earlier than 4.0(4), only ports 1-8 are Unified Ports.  
---|---  
2  |  Ports 17-44 (10/25 Gbps Ethernet or FCoE) |  **Note** |  When using Cisco UCS Manager releases earlier than 4.0(4), ports 9-44 are 10/25 Gbps Ethernet or FCoE.  
---|---  
3  |  Ports 45-48 (1/10/25 Gbps Ethernet or FCoE)  |  4 |  Uplink Ports 49-54 (40/100 Gbps Ethernet or FCoE) Each of these ports can be 4 x 10/25 Gbps Ethernet or FCoE uplink ports when using an appropriate breakout cable.  
  
The Cisco UCS 6454 Fabric Interconnect chassis has two power supplies and four fans. Two of the fans provide front to rear airflow. 

Figure 8. Cisco UCS 6454 Fabric Interconnect Front View ![](/c/dam/en/us/td/i/300001-400000/300001-310000/306001-307000/306354.jpg) **1** |  Power supply and power cord connector  |  **2** |  Fans 1 through 4, numbered left to right, when facing the front of the chassis.  
---|---|---|---  
**3** |  L1 port, L2 port, RJ45, console, USB port, and LEDs |  |   
  
### Ports on the Cisco UCS Fabric Interconnects

Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct) has eight ports that include: 

  * Ports 1 & 2 that are unified ports to manage all SAN features and configurations.

  * The 100G Ethernet ports [1-8] can also be configured as 25Gx4 SFP28 compatible breakout ports or 4x10G ports, offering flexible networking solutions to accommodate a range of data center needs. 

  * The 32G Fibre Channel ports [1 & 2] can also be configured as 8Gx4 SFP28 compatible breakout ports offering flexible networking solutions to accommodate a range of data center needs. 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Migration of any previous generation Fabric Interconnects to the Cisco UCS 9108 100G Intelligent Fabric Module is currently not supported. 

* * *  
  
---|---  
  
Ports on the Cisco UCS 6536 Fabric Interconnects can be configured to carry either Ethernet or Fibre Channel traffic. You can configure only ports 33-36 to carry Fibre Channel traffic. The ports cannot be used by a Cisco UCS domain until you configure them. 

Ports on the Cisco UCS 6400 Series Fabric Interconnects can be configured to carry either Ethernet or Fibre Channel traffic. You can configure only ports 1-16 to carry Fibre Channel traffic. The ports cannot be used by a Cisco UCS domain until you configure them. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

  * The Cisco UCS 6454 Fabric Interconnect supported 8 unified ports (ports 1 - 8) with Cisco UCS Manager 4.0(1) and 4.0(2), but with Release 4.0(4) and later releases, it supports 16 unified ports (ports 1 - 16).  When you configure a port on a Fabric Interconnect, the administrative state is automatically set to enabled. If the port is connected to another device, this may cause traffic disruption. The port can be disabled and enabled after it has been configured. 


* * *  
  
---|---  
  
The following table summarizes the port support for third, fourth, fifth generation of Cisco UCS Fabric Interconnects, and Cisco UCS Fabric Interconnects 9108 100G.

|  Third Generation  |  Fourth Generation |  Fifth Generation |  Cisco UCS X-Series Direct  
---|---|---|---|---  
Item  |  Cisco UCS 6332  |  Cisco UCS 6332-16UP  |  Cisco UCS 6454 |  Cisco UCS 64108 |  Cisco UCS 6536 |  Cisco UCS 9108 100G FI  
Description  |  32-Port Fabric Interconnect  |  40-Port Fabric Interconnect  |  54-Port Fabric Interconnect  |  108-Port Fabric Interconnect |  36-Port Fabric Interconnect |  8 Ports  
Form factor  |  1 RU  |  1 RU  |  1 RU  |  2 RU |  1 RU |  1 RU  
Number of fixed 10 GB Interfaces  |  96 (40G to 4 x 10G breakout cables), QSA, Port 13 and 14 do not support 40G to 10G breakout  |  88 (40G to 4 x 10G breakout cables)  |  48 10G/25G interfaces |  96 10G/25G interfaces |  36 10G/25G/40G/100G interfaces |  **Note** |  144 breakout ports (36x4)  
---|---  
—   
Number of Unified Ports |  —  |  16  |  16 This FI supported 8 unified ports (ports 1 - 8) with Cisco UCS Manager 4.0(1) and 4.0(2), but with Release 4.0(4) and later it supports 16 unified ports (ports 1 - 16).  |  16 ports 1-16 |  4 |  **Note** |  16 breakout ports (4x4)  
---|---  
Ports 1-2  
Unified Port Speeds in Gbps |  —  |  1G/10G or 4G/8G/16G-FC  |  10G/25G or 8G/16G/32G-FC  |  10G/25G or 8G/16G/32G-FC |  10G/25G/40G/100G FC |  8G/16G/32G FC  
Number of 40-Gbps ports  |  32  |  24  |  6 40G/100G  |  12 40G/100G  |  36 |  —   
Unified Port Range  |  None  |  Ports 1-16  |  Ports 1-16  |  Ports 1-16  |  Ports 33-36 |  Ports 1-2  
Compatibility with the IOM  |  UCS 2204, UCS 2208, UCS 2304, UCS 2304V2 |  UCS 2204, UCS 2208, UCS 2304, UCS 2304V2 |  UCS 2204, UCS 2208, UCS 2408 |  UCS 2204, UCS 2208, UCS 2408 |  UCS 2408, UCS 2304, UCS 2304V2 |  —   
Compatibility with the FEX |  Cisco Nexus 2232PP Cisco Nexus 2232TM-E Cisco Nexus 2348UPQ |  Cisco Nexus 2232PP Cisco Nexus 2232TM-E Cisco Nexus 2348UPQ |  Cisco Nexus 2232PP Cisco Nexus 2232TM-E Cisco Nexus 93180YC-FX3 |  Cisco Nexus 2232PP Cisco Nexus 2232TM-E Cisco Nexus 93180YC-FX3 |  Cisco Nexus 93180YC-FX3 N2K-C2348UPQ |  —   
Expansion Slots  |  None  |  None  |  None  |  None |  None |  —   
Fan Modules  |  4  |  4  |  4 |  3 |  6 |  3  
Power Supplies  |  2 (AC/DC)  |  2 (AC/DC)  |  2 (AC/DC)  |  2 (AC/DC)  |  2 (AC) |  Supplied by chassis  
  
### Port Breakout Functionality on Cisco UCS 64108 Fabric Interconnects

#### About Breakout Ports

Cisco UCS 64108 fabric interconnects support splitting a single 40/100G QSFP port into four 10/25G ports using a supported breakout cable. On the UCS 64108 fabric interconnect, by default, there are 12 ports in the 40/100G mode. These are ports 97 to 108. These 40/100G ports are numbered in a 2-tuple naming convention. For example, the second 40G port is numbered as 1/99. The process of changing the configuration from 40G to 10 G, or from 100G to 25G is called breakout, and the process of changing the configuration from [4X]10G to 40G or from [4X]25G to 100G is called unconfigure. These ports can be used as uplink port, appliance port, server port (using FEX), and FCoE storage port. 

When you break out a 40G port into 10G ports or a 100G port into 25G ports, the resulting ports are numbered using a 3-tuple naming convention. For example, the breakout ports of the second 40-Gigabit Ethernet port are numbered as 1/99/1, 1/99/2, 1/99/3, 1/99/4. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCS Manager does not support connection of FEX, chassis, blade, IOM, or adapters (other than VIC adapters) to the uplink ports of Fabric Interconnect. 

* * *  
  
---|---  
  
Starting with Cisco UCS Manager Release 4.2(3b), configuring the Ethernet breakout ports will not lead to Fabric Interconnect reboot. 

The following image shows the rear view of the Cisco UCS 64108 fabric interconnect, and includes the ports that support breakout port functionality: 

Figure 9. Cisco UCS 64108 Fabric Interconnect Rear View ![](/c/dam/en/us/td/i/300001-400000/300001-310000/307001-308000/307644.jpg) 1  |  Ports 1-16. Unified Ports can operate as 10/25 Gbps Ethernet or 8/16/32 Gbps Fibre Channel. FC ports are converted in groups of four.  Unified ports:

  * 10/25 Gbps Ethernet or FCoE
  * 8/16/32 Gbps Fibre Channel

|  2  |  Ports 1-96. Each port can operate as either a 10 Gbps or 25 Gbps Ethernet or FCoE SFP28 port.   
---|---|---|---  
3  |  Uplink Ports 97-108. Each port can operate as either a 40 Gbps or 100 Gbps Ethernet or FCoE port. When using a breakout cable, each of these ports can operate as 4 x 10 Gbps or 4 x 25 Gbps Ethernet or FCoE ports.  Ports 97 - 108 can be used to connect to Ethernet or FCoE uplink ports, and not to UCS server ports. |  4 |  Ports 89-96

  * 10/25 Gbps Ethernet or FCoE
  * 1 Gbps Ethernet

  
5 |  System environment (fan fault) LED |  6 |  System status LED  
7 |  Beacon LED |  |   
  
#### Breakout Port Guidelines

The following are the guidelines for breakout functionality for Cisco UCS 64108 fabric interconnects: 

  * The breakout configurable ports are ports 97-108.

  * You cannot configure the speed for each breakout port. Each breakout port is in auto mode.

  * Breakout ports are not supported as destinations for traffic monitoring.

  * Ports 97-108 at 40/100G can be configured as uplink, FCoE, or appliance port. Ports 97-108 after breakout to 10/25G can be configured as uplink, appliance, FCoE, or for direct-connect rack server connectivity. 


### Port Breakout Functionality on Cisco UCS 6454 Fabric Interconnects

#### About Breakout Ports

Cisco UCS 6454 fabric interconnects support splitting a single 40/100G QSFP port into four 10/25G ports using a supported breakout cable. These ports can be used only as uplink ports connecting to a 10/25G switch. On the UCS 6454 fabric interconnect, by default, there are 6 ports in the 40/100G mode. These are ports 49 to 54. These 40/100G ports are numbered in a 2-tuple naming convention. For example, the second 40G port is numbered as 1/50. The process of changing the configuration from 40G to 10 G, or from 100G to 25G is called breakout, and the process of changing the configuration from [4X]10G to 40G or from [4X]25G to 100G is called unconfigure. 

When you break out a 40G port into 10G ports or a 100G port into 25G ports, the resulting ports are numbered using a 3-tuple naming convention. For example, the breakout ports of the second 40-Gigabit Ethernet port are numbered as 1/50/1, 1/50/2, 1/50/3, 1/50/4. 

Starting with Cisco UCS Manager Release 4.2(3b), Ethernet breakout ports configuration will not lead to Fabric Interconnect reboot. 

Starting with Cisco UCS Manager Release 4.1(3a), you can connect Cisco UCS Rack servers with VIC 1455 and 1457 adapters, to the uplink ports 49 to 54 (40/100 Gbps Ethernet or FCoE) in Cisco UCS 6454 Fabric Interconnects. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCS Manager does not support connection of FEX, chassis, blade, IOM, or adapters (other than VIC 1455 and 1457 adapters) to the uplink ports of Fabric Interconnect. 

* * *  
  
---|---  
  
The following image shows the rear view of the Cisco UCS 6454 fabric interconnect, and includes the ports that support breakout port functionality: 

Figure 10. Cisco UCS 6454 Fabric Interconnect Rear View ![](/c/dam/en/us/td/i/300001-400000/300001-310000/306001-307000/306755.jpg) 1  |  Ports 1-16 (Unified Ports 10/25 Gbps Ethernet or FCoE or 8/16/32 Gbps Fibre Channel) |  2  |  Ports 17-44 (10/25 Gbps Ethernet or FCoE)  
---|---|---|---  
3  |  Ports 45-48 (1/10/25 Gbps Ethernet or FCoE)  |  4 |  Uplink Ports 49-54 (40/100 Gbps Ethernet or FCoE)   
  
#### Breakout Port Guidelines

The following are the guidelines for breakout functionality for Cisco UCS 6454 fabric interconnects: 

  * The breakout configurable ports are ports 49-54.

  * You cannot configure the speed for each breakout port. Each breakout port is in auto mode.

  * In Cisco UCS Manager Release 4.0(2), breakout ports are not supported as destinations for traffic monitoring.

  * Ports 49-54 at 40/100G can be configured as uplink, FCoE, or appliance port. Ports 49-54 after breakout to 10/25G can be configured as uplink, appliance, FCoE, or for direct-connect rack server connectivity. 


### Software Feature Configuration on Cisco UCS 6400 Series Fabric Interconnects 

Cisco UCS Manager Release 4.0(1) and 4.0(2) introduced support for various software features on Cisco UCS 6454 Fabric Interconnects. Cisco UCS Manager Release 4.1 extends support for these features on Cisco UCS 64108 Fabric Interconnects. These software features are: 

  * Switching Modes—Support for Ethernet and FC switching modes on Cisco UCS 6400 Series Fabric Interconnects . 

  * MAC Security—Support for MAC security on Cisco UCS 6400 Series Fabric Interconnects. 

  * Breakout Uplink Ports—Support for splitting a single 40/100G QSFP port into four 10/25G ports using a supported breakout cable. These ports can be used only as Ethernet uplink or FCoE uplink ports connecting to a 10/25G switch. They cannot be configured as server ports, FCoE storage ports, appliance ports or monitoring ports. 

  * MTU Configuration—Cisco UCS 64108 Fabric Interconnects support MTU configuration for QOS drop class policy. 


Cisco UCS 6400 Series Fabric Interconnects do not support the following software features: 

  * Chassis Discovery Policy in Non-Port Channel Mode—Cisco UCS 6400 Series Fabric Interconnects support only Port Channel mode. 

  * Chassis Connectivity Policy in Non-Port Channel Mode—Cisco UCS 6400 Series Fabric Interconnects support only Port Channel mode. 

  * Multicast Hardware Hash—Cisco UCS 6400 Series Fabric Interconnects do not support multicast hardware hash. 

  * Service Profiles with Dynamic vNICS—Cisco UCS 6400 Series Fabric Interconnects do not support Dynamic vNIC Connection Policies. 

  * Multicast Optimize—Cisco UCS 6400 Series Fabric Interconnects do not support Multicast Optimize for QoS. 

  * Port profiles and DVS Related Configurations—Cisco UCS 6400 Series Fabric Interconnects do not support configurations related to port profiles and distributed virtual switches (DVS). 


Configuration of the following software features has changed for Cisco UCS 6400 Series Fabric Interconnects: 

  * Unified Ports—Cisco UCS 6400 Series Fabric Interconnects support up to 16 unified ports, which can be configured as FC. These ports appear at the beginning of the module. 

  * VLAN Optimization—On Cisco UCS 6400 Series Fabric Interconnects, you can configure VLAN port count optimization through port VLAN (VP) grouping when the PV count exceeds 16000. The following table illustrates the PV Count with VLAN port count optimization enabled and disabled on Cisco UCS 6400 Series Fabric Interconnect, Cisco UCS 6300 Series Fabric Interconnects. 

|  6300 Series FI |  6400 Series FI |  6500 Series FI (6536 FI)  
---|---|---|---  
PV Count with VLAN Port Count Optimization Disabled |  16000 |  16000 |  16000  
PV Count with VLAN Port Count Optimization Enabled |  64000 |  108000 |  108000  
  
When a Cisco UCS 6400 Series Fabric Interconnect is in Ethernet switching mode: 

  * The Fabric Interconnect does not support VLAN Port Count Optimization Enabled

  * The Fabric Interconnect supports 16000 PVs, similar to EHM mode, when set to VLAN Port Count Optimization Disabled

  * Limited Restriction on VLAN—Cisco UCS 6400 Series Fabric Interconnects reserve 128 additional VLANs for system purposes. 


Cisco UCS 6300 Series Fabric Interconnects

### Fabric Interconnect Features 

A Cisco UCS 6300 Series Fabric Interconnect provides both network connectivity and management capabilities to a Cisco UCS system. The fabric interconnect provides Ethernet and Fibre Channel to the servers in the system, the servers connect to the fabric interconnect, and the fabric interconnect connects to the LAN or SAN. 

Each Cisco UCS 6300 Series Fabric Interconnect runs Cisco UCS Manager to fully manage all Cisco UCS elements. The fabric interconnect supports full end-to-end 40-Gigabit capabilities in the fabric and enables 16-Gigabit Fibre Channel capabilities. High availability can be achieved when a Cisco UCS 6300 Series Fabric Interconnect is connected to another Cisco UCS 6300 Series Fabric Interconnect through the L1 or L2 port on each device. 

The Cisco UCS 6300 Series Fabric Interconnect joins next-generation UCS products, including the following hardware: 

  * Cisco UCS 6332 Fabric Interconnect, an Ethernet or Fibre Channel over Ethernet (FCoE) chassis with 32 40-Gigabit QSFP+ ports 

  * Cisco UCS 6332-16UP Fabric Interconnect, an Ethernet, FCoE, and Fibre Channel chassis with 16 1- or 10-Gigabit SFP+ ports or 16 4-, 8-, or 16-Gigabit Fibre Channel ports, 24 40-Gigabit QSFP+ ports 

  * Cisco 2304 IOM  or Cisco 2304V2, I/O modules with 8 40-Gigabit backplane ports and 4 40-Gigabit uplink ports 

  * Multiple VICs 


### Cisco UCS 6332 Fabric Interconnect 

The Cisco UCS 6332 Fabric Interconnect is a 1-RU, top-of-rack switch with 32 40-Gigabit QSFP+ ports, one 100/1000 network management port, one RS-232 console port for setting the initial configuration, and two USB ports for saving or loading configurations. The switch also includes an L1 port and an L2 port for connecting two fabric interconnects to provide high availability. The switch mounts in a standard 19-inch rack, such as the Cisco R Series rack. 

Cooling fans pull air front-to-rear. That is, air intake is on the fan side and air exhaust is on the port side.

Figure 11. Cisco UCS 6332 Fabric Interconnect Rear View ![](/c/dam/en/us/td/i/300001-400000/300001-310000/305001-306000/305190.jpg) 1  |  Port lane switch button, port lane LEDs, and L1 and L2 ports.  |  2  |  Ports 1–12 and ports 15–26 can operate as 40-Gbps QSFP+ ports, or as 4 x 10-Gbps SFP+ breakout ports.  Ports 1 - 4 support Quad to SFP or SFP+ (QSA) adapters to provide 1-Gbps/10 Gbps operation. Ports 13 and 14 can operate as 40-Gbps QSFP+ ports. They cannot operate as 4 x 10-Gbps SFP+ breakout ports.   
---|---|---|---  
3  |  Ports 27–32 operate as 40-Gbps QSFP+ ports.  |  |   
Figure 12. Cisco UCS 6332 Fabric Interconnect Front View   
![](/c/dam/en/us/td/i/300001-400000/300001-310000/305001-306000/305191.jpg)  
**1** |  Power supply and power cord connector  |  **2** |  Fans1 through 4, numbered left to right, when facing the front of the chassis.   
---|---|---|---  
**3** |  Management, console, and USB ports, and LEDs. |  **** |   
  
### Cisco UCS 6332-16UP Fabric Interconnect 

The Cisco UCS 6332-16UP Fabric Interconnect is a 1-RU top-of-rack switch with 24 40-Gb QSFP+ ports, 16 10-Gb SFP ports, one 100/1000 network management port, one RS-232 console port for setting the initial configuration, and two USB ports for saving or loading configurations. The switch also includes an L1 port and an L2 port for connecting two fabric interconnects to provide high availability. The switch mounts in a standard 19-inch rack, such as the Cisco R Series rack. 

Cooling fans pull air front-to-rear. That is, air intake is on the fan side and air exhaust is on the port side.

Figure 13. Cisco UCS 3223-16UP Fabric Interconnect Rear View ![](/c/dam/en/us/td/i/300001-400000/300001-310000/305001-306000/305256.jpg) **1** |  Port lane switch button, port lane LEDs, and L1 and L2 ports. |  **2** |  Ports 1–16 are Unified Ports (UP) that operate either as 1- or 10-Gbps SFP+ fixed Ethernet ports; or as 4-, 8-, or 16-Gigabit Fibre Channel ports.   
---|---|---|---  
**3** |  Ports 17–34 operate either as 40-Gbps QSFP+ ports, breakout mode for 4 x 10-Gigabit SFP+ breakout ports, or QSA for 10G.  |  **4** |  Ports 35–40 operate as 40-Gbps QSFP+ ports.   
Figure 14. Cisco UCS 6332-16UP Fabric Interconnect Front View   
![](/c/dam/en/us/td/i/300001-400000/300001-310000/305001-306000/305185.jpg)  
**1** |  Power supply and power cord connector  |  **2** |  Fans1 through 4, numbered left to right, when facing the front of the chassis.  
---|---|---|---  
**3** |  Management, console, and USB ports, and LEDs.  |  **** |   
  
### Ports on the Cisco UCS 6300 Series Fabric Interconnects 

Ports on the Cisco UCS 6300 Series Fabric Interconnects can be configured to carry either Ethernet or Fibre Channel traffic. These ports are not reserved. They cannot be used by a Cisco UCS domain until you configure them. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

When you configure a port on a fabric interconnect, the administrative state is automatically set to enabled. If the port is connected to another device, this may cause traffic disruption. You can disable the port after it has been configured. 

* * *  
  
---|---  
  
The following table summarizes the third generation ports for the Cisco UCS fabric interconnects. 

|  Cisco UCS Mini  |  Third Generation   
---|---|---  
Item  |  Cisco UCS 6324  |  Cisco UCS 6332  |  Cisco UCS 6332-16UP   
Description  |  Fabric Interconnect with 4 unified ports and 1 scalability port  |  32–Port Fabric Interconnect  |  40–Port Fabric Interconnect   
Form factor  |  1 RU  |  1 RU  |  1 RU   
Number of fixed 40 GB Interfaces  |  —  |  6(Ports 17–32)  |  6(Ports 35–40)   
Number of 1GB/10GB Interfaces (depending on the SFP module installed)  |  All  |  Ports 5–26 using breakout cable  |  Ports 17–34 using breakout cable   
Unified Ports (8 Gb/s, FC, FCoE)  |  4  |  None  |  Ports 1–16   
Compatibility with all IOMs  |  All  |  All  |  All   
Expansion Slots  |  None  |  None  |  None   
Fan Modules  |  4  |  4  |  4   
Power Supplies  |  —  |  2 (AC/DC available)  |  2 (AC/DC available)   
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCS 6300 Series Fabric Interconnects support breakout capability for ports. For more information on how the 40G ports can be converted into four 10G ports, see Port Breakout Functionality on Cisco UCS 6300 Series Fabric Interconnects. 

* * *  
  
---|---  
  
  * Port Modes
  * Port Types
  * Port Breakout Functionality on Cisco UCS 6300 Series Fabric Interconnects


#### Port Modes

The port mode determines whether a unified port on the fabric interconnect is configured to carry Ethernet or Fibre Channel traffic. You configure the port mode in Cisco UCS Manager. However, the fabric interconnect does not automatically discover the port mode. 

Changing the port mode deletes the existing port configuration and replaces it with a new logical port. Any objects associated with that port configuration, such as VLANs and VSANS, are also removed. There is no restriction on the number of times you can change the port mode for a unified port. 

#### Port Types

The port type defines the type of traffic carried over a unified port connection. 

By default, unified ports changed to Ethernet port mode are set to the Ethernet uplink port type. Unified ports changed to Fibre Channel port mode are set to the Fibre Channel uplink port type. You cannot unconfigure Fibre Channel ports. 

Changing the port type does not require a reboot. 

Ethernet Port Mode

When you set the port mode to Ethernet, you can configure the following port types: 

  * Server ports 

  * Ethernet uplink ports 

  * Ethernet port channel members 

  * FCoE ports 

  * Appliance ports 

  * Appliance port channel members 

  * SPAN destination ports 

  * SPAN source ports 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For SPAN source ports, configure one of the port types and then configure the port as SPAN source. 

* * *  
  
---|---  


Fibre Channel Port Mode

When you set the port mode to Fibre Channel, you can configure the following port types: 

  * Fibre Channel uplink ports 

  * Fibre Channel port channel members

  * Fibre Channel storage ports 

  * SPAN source ports 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For SPAN source ports, configure one of the port types and then configure the port as SPAN source. 

* * *  
  
---|---  


#### Port Breakout Functionality on Cisco UCS 6300 Series Fabric Interconnects 

##### About Breakout Ports 

Cisco UCS fabric interconnect 6300 series supports splitting a single QSFP port into four 10G ports using a supported breakout cable. By default, there are 32 ports in the 40G mode. These 40G ports are numbered in a 2-tuple naming convention. For example, the second 40G port is numbered as 1/2. The process of changing the configuration from 40G to 10G is called breakout and the process of changing the configuration from [4X]10G to 40G is called unconfigure. 

When you break out a 40G port into 10G ports, the resulting ports are numbered using a 3-tuple naming convention. For example, the breakout ports of the second 40-Gigabit Ethernet port are numbered as 1/2/1, 1/2/2, 1/2/3, 1/2/4. 

The following image shows the front view for the Cisco UCS 6332 series fabric interconnects, and includes the ports that may support breakout port functionality: 

Figure 15. Cisco UCS 6332 Series Fabric Interconnects Front View  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/305001-306000/305235.jpg) 1  |  L1 and L2 high availability ports   
---|---  
2  |  28 X 40G QSFP ports ( 98 X 10G SFP ports)  |  **Note** | 

  * QSA module is required on ports 13–14 
  * A QSFP to 4XSFP breakout cable is required for 10G support. 

  
---|---  
3  |  6 X 40G QSFP ports   
  
The following image shows the front view for the Cisco UCS 6332-16UP series fabric interconnects, and includes the ports that may support breakout port functionality: 

Figure 16. Cisco UCS 6332-16UP Series Fabric Interconnects Front View  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/305001-306000/305236.jpg) 1  |  L1 and L2 high availability ports   
---|---  
2  |  16 X 1/10G SFP (16 X 4/8/16G FC ports)   
3  |  18 X 40G QSFP(72 X 10G SFP+)  |  **Note** | 

  * A QSFP to 4XSFP breakout cable is required for 10G support. 

  
---|---  
4  |  6 X 40G QSFP ports   
  
The following image shows the rear view of the Cisco UCS 6300 series fabric interconnects. 

Figure 17. Cisco UCS 6300 Series Fabric Interconnects Rear View  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/305001-306000/305237.jpg) 1  |  Power supply   
---|---  
2  |  Four fans   
3  |  Power supply   
4  |  Serial ports   
  
##### Breakout Port Constraints 

The following table summarizes the constraints for breakout functionality for Cisco UCS 6300 series fabric interconnects: 

Cisco UCS 6300 Series Fabric Interconnect Series  |  Breakout Configurable Ports  |  Ports without breakout functionality support   
---|---|---  
Cisco UCS 6332  |  1–12, 15–26  |  13–14, 27–32  |  **Note** | 

  * Auto-negotiate behavior is not supported on ports 27–32. 

  
---|---  
Cisco UCS 6332-16UP  |  17–34  |  1–16, 35–40  |  **Note** | 

  * Auto-negotiate behavior is not supported on ports 35–40 

  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

Up to four breakout ports are allowed if QoS jumbo frames are used. 

* * *  
  
---|---  
  
### Cisco UCS Chassis 

Cisco UCS Manager Release 3.1(1) and later releases provide support for Cisco UCS 5108 Blade Server Chassis 

Chassis Management provides details on managing the chassis through Cisco UCS Manager. 

#### Cisco UCS 5108 Blade Server Chassis 

The Cisco UCS 5108 Blade Server Chassis, is six rack units (6RU) high, can mount in an industry-standard 19-inch rack, and uses standard front-to-back cooling. A chassis can accommodate up to eight half-width, or four full-width Cisco UCS B-Series Blade Servers form factors within the same chassis. By incorporating unified fabric and fabric-extender technology, the Cisco Unified Computing System enables the chassis to: 

  * Have fewer physical components 

  * Require no independent management

  * Be more energy efficient than a traditional blade-server chassis 


The Cisco UCS 5108 Blade Server Chassis is supported with all generations of fabric interconnects. 

### Cisco UCS Mini Infrastructure 

The Cisco UCS Mini solution extends the Cisco UCS architecture into environments with requirements for smaller domains, including branch and remote offices, point-of-sale locations, and smaller IT environments. Cisco UCS Mini has three main infrastructure components: 

  * Cisco UCS 6324 fabric interconnect 

  * Cisco UCS blade server chassis 

  * Cisco UCS blade or rack mount servers 


Figure 18. Cisco UCS Mini   
![](/c/dam/en/us/td/i/300001-400000/300001-310000/305001-306000/305218.jpg)  


In the Cisco UCS Mini solution, the Cisco UCS 6324 fabric interconnect is collapsed into the IO Module form factor, and is inserted into the IOM slot of the blade server chassis. The Cisco UCS 6324 fabric interconnect has 24 10G ports available on it. Sixteen of these ports are server facing, two 10G ports are dedicated to each of the eight half width blade slots. The remaining eight ports are divided into groups of four 1/10G Enhanced Small Form-Factor Pluggable (SFP+) ports and one 40G Quad Small Form-factor Pluggable (QSFP) port, which is called the 'scalability port'. 

Cisco UCS Manager Release 3.1(1) introduces support for a second UCS 5108 chassis to an existing single-chassis Cisco UCS 6324 fabric interconnect setup. This extended chassis enables you to configure an additional 8 servers. Unlike the primary chassis, the extended chassis supports IOMs. Currently, it supports UCS-IOM-2204XP and UCS-IOM-2208XP IOMs. The extended chassis can only be connected through the scalability port on the FI-IOM. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

Currently, Cisco UCS Manager supports only one extended chassis for UCS Mini. 

* * *  
  
---|---  
  
### Cisco UCS Infrastructure Virtualization 

Cisco UCS is a single integrated system with switches, cables, adapters, and servers that are all tied together and managed by unified management software. One capability that enables this unification is the ability to virtualize every component of the system at every level. Switch port, cables, adapter, and servers can all be virtualized. Because of the virtualization capabilities at every component of the system, you have the unique capability to provide rapid provisioning of any service on any server on any blade through a system that is wired once. The following image illustrates these virtualization capabilities. 

Figure 19. Virtualization Capabilities of Cisco UCS   
![](/c/dam/en/us/td/i/300001-400000/300001-310000/305001-306000/305216.jpg)  


#### Switch Port Virtualization 

The physical interfaces provide physical connectivity for what are logical virtual interfaces on the fabric interconnects-virtual Fibre Channel interfaces (vFC) and virtual Ethernet interfaces (vEth). The logical connectivity to a server is provided through these virtual interfaces. 

####  Cable Virtualization 

The physical cables that connect to physical switch ports provide the infrastructure for logical and virtual cables. These virtual cables connect to virtual adapters on any given server in the system. 

####  Adapter Virtualization 

On the server, you have physical adapters, which provide physical infrastructure for virtual adapters. A virtual network interface card (vNIC) or virtual host bus adapter (vHBA) logically connects a host to a virtual interface on the fabric interconnect and allows the host to send and receive traffic through that interface. Each virtual interface in the fabric interconnect corresponds to a vNIC. 

An adapter that is installed on the server appears to the server as multiple adapters through standard PCIe virtualization. When the server scans the PCIe bus, the virtual adapters that are provisioned appear to be physically plugged into the PCIe bus. 

####  Server Virtualization 

Server virtualization provides you with the ability of stateless servers. As part of the physical infrastructure, you have physical servers. However, the configuration of a server is derived from the service profile to which it is associated. All service profiles are centrally managed and stored in a database on the fabric interconnect. A service profile defines all the settings of the server, for example, the number of adapters, virtual adapters, the identity of these adapters, the firmware of the adapters, and the firmware of the server. It contains all the settings of the server that you typically configure on a physical machine. Because the service profile is abstracted from the physical infrastructure, you can apply it to any physical server and the physical server will be configured according to the configuration defined in the service profile. Cisco UCS Manager Server Management Guide provides detailed information about managing service profiles. 

---

## Page 18: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_chapter_011.html

# Equipment Policies

## Chassis/FEX Discovery Policy 

The chassis/FEX discovery policy determines how the system reacts when you add a new chassis or FEX. Cisco UCS Manager uses the settings in the chassis/FEX discovery policy to determine the minimum threshold for the number of links between the chassis or FEX and the fabric interconnect and whether to group links from the IOM to the fabric interconnect in a fabric port channel. 

In a Cisco UCS Mini (Cisco UCS 6324 Fabric Interconnect) setup, chassis discovery policy is supported only on the extended chassis. 

### Chassis Links

If you have a Cisco UCS domain with some of the chassis' wired with one link, some with two links, some with four links, and some with eight links, Cisco recommends configuring the chassis/FEX discovery policy for the minimum number links in the domain so that Cisco UCS Manager can discover all chassis. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/tip.gif)  
**Tip** | 

* * *

To establish the highest available chassis connectivity in a Cisco UCS domain where Fabric Interconnect is connected to different types of IO Modules supporting different max number of uplinks, select platform max value. Setting the platform max ensures that Cisco UCS Manager discovers the chassis including the connections and servers only when the maximum supported IOM uplinks are connected per IO Module. 

* * *  
  
---|---  
  
After the initial discovery of a chassis, if chassis/FEX discovery policy changes are done, acknowledge IO Modules rather than the entire Chassis to avoid disruption. The discovery policy changes can include increasing the number of links between Fabric Interconnect and IO Module, or changes to the Link Grouping preference. 

Make sure that you monitor for faults before and after the IO Module acknowledgement to ensure that the connectivity is restored before proceeding to the other IO Module for the chassis. 

Cisco UCS Manager cannot discover any chassis that is wired for fewer links than are configured in the chassis/FEX discovery policy. For example, if the chassis/FEX discovery policy is configured for four links, Cisco UCS Manager cannot discover any chassis that is wired for one link or two links. Re-acknowledgement of the chassis resolves this issue. 

The following table provides an overview of how the chassis/FEX discovery policy works in a multi-chassis Cisco UCS domain: 

Table 1. Chassis/FEX Discovery Policy and Chassis Links Number of Links Wired for the Chassis  | 1-Link Discovery Policy  | 2-Link Discovery Policy  | 4-Link Discovery Policy  | 8-Link Discovery Policy  | Platform-Max Discovery Policy   
---|---|---|---|---|---  
**1 link between IOM and fabric interconnects** |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 1 link.  |  Chassis connections and servers cannot be discovered by Cisco UCS Manager and are not added to the Cisco UCS domain.  |  Chassis connections and servers cannot be discovered by Cisco UCS Manager and are not added to the Cisco UCS domain.  |  Chassis connections and servers cannot be discovered by Cisco UCS Manager and are not added to the Cisco UCS domain.  |  Chassis connections and servers cannot be discovered by Cisco UCS Manager and are not added to the Cisco UCS domain.   
**2 links between IOM and fabric interconnects** |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 1 link.  After initial discovery, reacknowledge the chassis and Cisco UCS Manager recognizes and uses the additional links.  |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 2 link.  |  Chassis connections and servers cannot be discovered by Cisco UCS Manager and are not added to the Cisco UCS domain.  |  Chassis connections and servers cannot be discovered by Cisco UCS Manager and are not added to the Cisco UCS domain.  |  Chassis connections and servers cannot be discovered by Cisco UCS Manager and are not added to the Cisco UCS domain.   
**4 links between IOM and fabric interconnects** |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 1 link.  After initial discovery, reacknowledge the chassis and Cisco UCS Manager recognizes and uses the additional links.  |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 2 links.  After initial discovery, reacknowledge the chassis and Cisco UCS Manager recognizes and uses the additional links.  |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 4 link.  |  Chassis connections and servers cannot be discovered by Cisco UCS Manager and are not added to the Cisco UCS domain.  |  If the IOM has 4 links, the chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 4 links.  |  **Note** |  If the FEX status shows accessibility problem then reacknowledge the chassis after decommissioning/recommissioning FEX.  
---|---  
  
If the IOM has 8 links, the chassis is not fully discovered by Cisco UCS Manager.   
  
**8 links between IOM and fabric interconnects** |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 1 link.  After initial discovery, reacknowledge the chassis and Cisco UCS Manager recognizes and uses the additional links.  |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 2 links.  After initial discovery, reacknowledge the chassis and Cisco UCS Manager recognizes and uses the additional links.  |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 4 links.  After initial discovery, reacknowledge the chassis and Cisco UCS Manager recognizes and uses the additional links.  |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 8 links.  |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 8 links.   
  
### Link Grouping

For hardware configurations that support fabric port channels, link grouping determines whether all of the links from the IOM to the fabric interconnect are grouped in to a fabric port channel during chassis discovery. If the link grouping preference is set to Port Channel, all of the links from the IOM to the fabric interconnect are grouped in a fabric port channel. If set to None, links from the IOM are pinned to the fabric interconnect. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

For Cisco UCS X-Series Direct, Cisco UCS 6500 Series Fabric Interconnects, Cisco UCS 6400 Series Fabric Interconnect, the link grouping preference is always set to Port Channel. 

* * *  
  
---|---  
  
After a fabric port channel is created through Cisco UCS Manager, you can add or remove links by changing the link group preference and re-acknowledging the chassis, or by enabling or disabling the chassis from the port channel. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The link grouping preference only takes effect if both sides of the links between an IOM and IFM (IOM for Cisco UCS X-Series Servers) or FEX and the fabric interconnect support fabric port channels. If one side of the links does not support fabric port channels, this preference is ignored and the links are not grouped in a port channel. 

* * *  
  
---|---  
  
### Multicast Hardware Hash

In a port channel, by default, ingress multicast traffic on any port in the fabric interconnect (FI) selects a particular link between the IOM and the fabric interconnect to egress the traffic. To reduce potential issues with the bandwidth, and to provide effective load balancing of the ingress multicast traffic, hardware hashing is used for multicast traffic. When multicast hardware hashing is enabled, all links between the IOM and the fabric interconnect in a port channel can be used for multicast traffic. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCS X-Series Direct, Cisco UCS 6500 Series Fabric Interconnects, andCisco UCS 6400 Series Fabric Interconnect do not support multicast hardware hashing. 

* * *  
  
---|---  
  
  * Pinning
  * Port-Channeling
  * Configuring the Chassis/FEX Discovery Policy


### Pinning

Pinning in Cisco UCS is only relevant to uplink ports. If you configure Link Grouping Preference as None during chassis discovery, the IOM forwards traffic from a specific server to the fabric interconnect through its uplink ports by using static route pinning. 

The following table showcases how pinning is done between an IOM and the fabric interconnect based on the number of active fabric links between the IOM and the fabric interconnect. 

Table 2. Pinning on an IOM Number of Active Fabric Links  |  Server slot pinned to fabric link   
---|---  
1-Link  |  All the HIF ports are pinned to the active link   
2-Link  |  1,3,5,7 to link-1  2,4,6,8 to link-2   
4-Link  |  1,5 to link-1  2,6 to link-2  3,7 to link-3  4,8 to link-4   
8-Link (Applies only to 2208XP )  |  1 to link-1  2 to link-2  3 to link-3  4 to link-4  5 to link-5  6 to link-6  7 to link-7  8 to link-8   
  
Only 1,2,4 and 8 links are supported. 3,5,6, and 7 links are not valid configurations. 

### Port-Channeling

While pinning traffic from a specific server to an uplink port provides you with greater control over the unified fabric and ensures optimal utilization of uplink port bandwidth, it could also mean excessive traffic over certain circuits. This issue can be overcome by using port channeling. Port channeling groups all links between the IOM and the fabric interconnect into one port channel. The port channel uses a load balancing algorithm to decide the link over which to send traffic. This results in optimal traffic management. 

Cisco UCS supports port-channeling only through the Link Aggregation Control Protocol (LACP). For hardware configurations that support fabric port channels, link grouping determines whether all of the links from the IOM to the fabric interconnect are grouped into a fabric port channel during chassis discovery. If the Link Grouping Preference is set to Port Channel, all of the links from the IOM to the fabric interconnect are grouped in a fabric port channel. If this parameter is set to None, links from the IOM to the fabric interconnect are not grouped in a fabric port channel. 

Once a fabric port channel is created, links can be added or removed by changing the link group preference and reacknowledging the chassis, or by enabling or disabling the chassis from the port channel. 

### Configuring the Chassis/FEX Discovery Policy 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

In a setup with Cisco UCS 6400 Series Fabric Interconnects, the Link Grouping Preference value for Chassis/FEX Discovery Policy is not user configurable. The value is set to Port Channel. 

* * *  
  
---|---  
  
#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope org / |  Enters the root organization mode.  |  **Note** |  The chassis/FEX discovery policy can be accessed only from the root organization.   
---|---  
**Step 2** |  UCS-A /org #  scope chassis-disc-policy |  Enters organization chassis/FEX discovery policy mode.   
**Step 3** |  UCS-A /org/chassis-disc-policy #  set action ` `{1-link | 2-link | 4-link | 8-link | platform-max}  |  Specifies the minimum threshold for the number of links between the chassis or FEX and the fabric interconnect.   
**Step 4** |  (Optional) UCS-A /org/chassis-disc-policy # set descr ` ` description | (Optional)  Provides a description for the chassis/FEX discovery policy.  |  **Note** |  If your description includes spaces, special characters, or punctuation, you must begin and end your description with quotation marks. The quotation marks will not appear in the description field of any  show command output.   
---|---  
**Step 5** |  UCS-A /org/chassis-disc-policy #  set link-aggregation-pref ` `{none | port-channel}  |  Specifies whether the links from the IOMs or FEXes to the fabric interconnects are grouped in a port channel.  |  **Note** |  The link grouping preference only takes effect if both sides of the links between an IOM and IFM (IOM for Cisco UCS X-Series Servers) or FEX and the fabric interconnect support fabric port channels. If one side of the links does not support fabric port channels, this preference is ignored and the links are not grouped in a port channel.   
---|---  
**Note** |  For UCS manager to discover VIC 1455 and VIC 1457, Link Grouping Preference must be configured as Port Channel.   
---|---  
**Step 6** |  UCS-A /org/chassis-disc-policy # set multicast-hw-hash {disabled | enabled}  |  Specifies whether the all the links between the IOM and the fabric interconnect in a port channel can be used for multicast traffic. 

  * disabled —Only one link between the IOM and the fabric interconnect is used for multicast traffic 
  * enabled —All links between the IOM and the fabric interconnect can be used for multicast traffic 

  
**Step 7** |  (Optional) UCS-A /org/chassis-disc-policy #  set qualifier ` ` qualifier | (Optional)  Uses the specified server pool policy qualifications to associate this policy with a server pool.   
**Step 8** |  UCS-A /org/chassis-disc-policy #  commit-buffer |  Commits the transaction to the system configuration.   
  
#### Example

The following example scopes to the default chassis/FEX discovery policy, sets it to discover chassis with four links to a fabric interconnect, provides a description for the policy, specifies the server pool policy qualifications that will be used to qualify the chassis, and commits the transaction: 
    
    
    UCS-A# **scope org /**
    UCS-A /org # **scope chassis-disc-policy**
    UCS-A /org/chassis-disc-policy* # **set action 4-link**
    UCS-A /org/chassis-disc-policy* # **set descr "This is an example chassis/FEX discovery policy."**
    UCS-A /org/chassis-disc-policy* # **set qualifier ExampleQual**
    UCS-A /org/chassis-disc-policy* # **commit-buffer**
    UCS-A /org/chassis-disc-policy # 
    
    
    

The following example scopes to the default chassis/FEX discovery policy, sets it to discover chassis with eight links to a fabric interconnect, provides a description for the policy, sets the link grouping preference to port channel, specifies the server pool policy qualifications that will be used to qualify the chassis, and commits the transaction: 
    
    
    UCS-A# **scope org /**
    UCS-A /org # **scope chassis-disc-policy**
    UCS-A /org/chassis-disc-policy* # **set action 8-link**
    UCS-A /org/chassis-disc-policy* # **set descr "This is an example chassis/FEX discovery policy."**
    UCS-A /org/chassis-disc-policy* # **set link-aggregation-pref port-channel**
    UCS-A /org/chassis-disc-policy* # **set qualifier ExampleQual**
    UCS-A /org/chassis-disc-policy* # **commit-buffer**
    UCS-A /org/chassis-disc-policy # 
    
    
    

The following example scopes to the default chassis/FEX discovery policy, sets it to discover chassis with four links to a fabric interconnect, provides a description for the policy, sets the link grouping preference to port channel, enables multicast hardware hashing, specifies the server pool policy qualifications that will be used to qualify the chassis, and commits the transaction: 
    
    
    UCS-A# scope org /
    UCS-A /org # scope chassis-disc-policy
    UCS-A /org/chassis-disc-policy* # set action 4-link
    UCS-A /org/chassis-disc-policy* # set descr "This is an example chassis/FEX discovery
    policy."
    UCS-A /org/chassis-disc-policy* # set link-aggregation-pref port-channel
    UCS-A /org/chassis-disc-policy* # set multicast-hw-hash enabled
    UCS-A /org/chassis-disc-policy* # set qualifier ExampleQual
    UCS-A /org/chassis-disc-policy* # commit-buffer
    UCS-A /org/chassis-disc-policy #
    
    

#### What to do next

To customize fabric port channel connectivity for a specific chassis, configure the chassis connectivity policy. 

## Chassis Connectivity Policy 

The chassis connectivity policy determines the whether a specific chassis is included in a fabric port channel after chassis discovery. This policy is helpful for users who want to configure one or more chassis differently from what is specified in the global chassis discovery policy. The chassis connectivity policy also allows for different connectivity modes per fabric interconnect, further expanding the level of control offered with regards to chassis connectivity. 

By default, the chassis connectivity policy is set to global. This means that connectivity control is configured when the chassis is newly discovered, using the settings configured in the chassis discovery policy. Once the chassis is discovered, the chassis connectivity policy controls whether the connectivity control is set to none or port channel. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

The 40G backplane setting is not applicable for 22xx IOMs. 

* * *  
  
---|---  
  
The chassis connectivity policy is created by Cisco UCS Manager only when the hardware configuration supports fabric port channels. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

For the following fabric interconnects, the chassis connectivity policy is always Port Channel: 

  * Cisco UCS X-Series Direct (UCSX-S9108-100G) 
  * Cisco UCS 6500 Series Fabric Interconnect
  * Cisco UCS 6400 Series Fabric Interconnect


* * *  
  
---|---  
  
In a Cisco UCS Mini setup, the creation of a chassis connectivity policy is supported only on the extended chassis. 

  * Configuring a Chassis Connectivity Policy


### Configuring a Chassis Connectivity Policy

Changing the connectivity mode for a chassis might result in decreased VIF namespace. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Changing the connectivity mode for a chassis results in chassis re-acknowledgement. Traffic might be disrupted during this time. 

* * *  
  
---|---  
  
#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope org org-name |  Enters the organization mode for the specified organization. To enter the root organization mode, enter / as the org-name .   
**Step 2** |  UCS-A /org # scope chassis-conn-policy` `chassis-num` `[a | b}  |  Enters chassis connection policy organization mode for the specified chassis and fabric.  
**Step 3** |  UCS-A /org/chassis-conn-policy # set link-aggregation-pref` `{global | none | port-channel}  |  Specifies whether the links from the IOMs or FEXes to the fabric interconnects are grouped in a port channel. 

  * None—No links are grouped in a port channel 
  * Port Channel—All links from an IOM to a fabric interconnect are grouped in a port channel.  |  **Note** |  The following fabric interconnects support only Port Channel mode:
  * Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct) 
  * Cisco UCS 6536 Fabric Interconnect
  * Cisco UCS 6400 Series Fabric Interconnect  
---|---  
  * Global—The chassis inherits this configuration from the chassis discovery policy. This is the default value. 


  
**Step 4** |  UCS-A /org/chassis-conn-policy # commit-buffer |  Commits the transaction to the system configuration.  
  
#### Example

The following example shows how to change the fabric port channel connectivity for two chassis. Chassis 6, fabric A is changed to port channel and chassis 12, fabric B is changed to discrete links: 
    
    
    UCS-A# **scope org /**
    UCS-A /org # **scope chassis-conn-policy 6 a**
    UCS-A /org/chassis-conn-policy # **set link-aggregation-pref port-channel**
    UCS-A /org/chassis-conn-policy* # **up**
    UCS-A /org* # **scope chassis-conn-policy 12 b**
    UCS-A /org/chassis-conn-policy* # **set link-aggregation-pref none**
    UCS-A /org/chassis-conn-policy* # **commit-buffer**
    UCS-A /org/chassis-conn-policy #

## Rack Server Discovery Policy

The rack server discovery policy determines how the system reacts when you perform any of the following actions:

  * Add a new rack-mount server

  * Decommission/recommission a previously added or discovered rack-mount server


Cisco UCS Manager uses the settings in the rack server discovery policy to determine whether any data on the hard disks are scrubbed and whether server discovery occurs immediately or needs to wait for explicit user acknowledgement. 

Cisco UCS Manager cannot discover any rack-mount server that has not been correctly cabled and connected to the fabric interconnects. For information about how to integrate a supported Cisco UCS rack-mount server with Cisco UCS Manager, see the appropriate [rack-mount server integration guide](http://www.cisco.com/en/US/products/ps11736/products_installation_and_configuration_guides_list.html). 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

  * Cisco UCS VIC 1400, 14000, and 15000 series VIC adapters support 10/25/40/100G connectivity with Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct). 
  * Cisco UCS 1400, 14000, and 15000 series adapters support 10/25/40/100G with Cisco UCS 6536 fabric interconnects. 
  * Cisco UCS VIC 1400, 14000, and 15000 series adapters support 10/25G connectivity with Cisco UCS 6400 series fabric interconnects. 

When connecting to the Fabric Interconnects, use the same speed cables on all the adapter ports that are connected to same Fabric Interconnect. Cisco UCS VIC adapter ports connected to Cisco UCS Fabric Interconnect through a mix of 10G and 25G cables can result in UCS rack-mount server discovery failure and ports moving to suspended state. In this scenario, Cisco UCS Manager does not raise any faults. 

* * *  
  
---|---  
  
  * Configuring the Rack Server Discovery Policy


### Configuring the Rack Server Discovery Policy

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope org / |  Enters the root organization mode.  |  **Note** |  The rack server discovery policy can be accessed only from the root organization.   
---|---  
**Step 2** |  UCS-A /org #  scope rackserver-disc-policy |  Enters organization rack server discovery policy mode.   
**Step 3** |  UCS-A /org/rackserver-disc-policy #  set action ` `{immediate | user-acknowledged}  |  Specifies the way the system reacts when you perform any of the following actions:

  * Add a new rack server
  * Decommission/recommission a previously added or discovered rack server

  
**Step 4** |  (Optional) UCS-A /org/rackserver-disc-policy # set descr ` ` description | (Optional)  Provides a description for the rack server discovery policy.  |  **Note** |  If your description includes spaces, special characters, or punctuation, you must begin and end your description with quotation marks. The quotation marks will not appear in the description field of any  show command output.   
---|---  
**Step 5** |  UCS-A /org/rackserver-disc-policy #  set scrub-policy ` ` scrub-pol-name |  Specifies the scrub policy that should run on a newly discovered rack server or a decommissioned/recommissioned server.  
**Step 6** |  UCS-A /org/rackserver-disc-policy #  commit-buffer |  Commits the transaction to the system configuration.   
  
#### Example

The following example scopes to the default rack server discovery policy, sets it to immediately discover new rack servers or decommissioned/recommissioned server, provides a description for the policy, specifies a scrub policy called scrubpol1, and commits the transaction: 
    
    
    UCS-A# **scope org /**
    UCS-A /org # **scope rackserver-disc-policy**
    UCS-A /org/rackserver-disc-policy* # **set action immediate**
    UCS-A /org/rackserver-disc-policy* # **set descr "This is an example rackserver discovery policy."**
    UCS-A /org/rackserver-disc-policy* # **set scrub-policy scrubpol1**
    UCS-A /org/rackserver-disc-policy* # **commit-buffer**
    UCS-A /org/rackserver-disc-policy # 
    

##  Aging Time for the MAC Address Table

To efficiently switch packets between ports, the fabric interconnect maintains a MAC address table. It dynamically builds the MAC address table by using the MAC source address from the packets received and the associated port on which the packets were learned. The fabric interconnect uses an aging mechanism, defined by a configurable aging timer, to determine how long an entry remains in the MAC address table. If an address remains inactive for a specified number of seconds, it is removed from the MAC address table. 

You can configure the amount of time (age) that a MAC address entry (MAC address and associated port) remains in the MAC address table. 

  * Configuring the Aging Time for the MAC Address Table


###  Configuring the Aging Time for the MAC Address Table

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope eth-uplink |  Enters Ethernet uplink mode.   
**Step 2** |  UCS-A /eth-uplink #  set mac-aging {dd hh mm ss | mode-default | never}  |  Specifies the aging time for the MAC address table. Use the  mode-default keyword to set the aging time to a default value dependent on the configured Ethernet switching mode. Use the  never keyword to never remove MAC addresses from the table regardless of how long they have been idle.   
**Step 3** |  UCS-A /eth-uplink #  commit-buffer |  Commits the transaction to the system configuration.  
  
#### Example

The following example sets the aging time for the MAC address table to one day and 12 hours and commits the transaction:
    
    
    UCS-A# **scope eth-uplink**
    UCS-A /eth-uplink # **set mac-aging 01 12 00 00**
    UCS-A /eth-uplink* # **commit-buffer**
    UCS-A /eth-uplink # 
    

## HA Version Holder Replacement 

In releases earlier than Cisco UCS Manager Release 3.1(2), version holders are selected on a first come first serve basis. As chassis and rack servers are discovered, they can become version holders if they meet the requirements, and if the number of version holders has not reached the maximum permitted number. After a device is marked as a version holder, it persists as a version holder until it is decommissioned or removed. For example, if the connection status between the device and one or both fabric interconnects goes down, the device will not be removed as version holder. 

In some situations, the shared storage devices that are selected as high availability (HA) version holders become unreachable for an extended period of time. Cisco UCS Manager Release 3.1(2) introduces the ability to specify new preferred HA version holders corresponding to the devices that are functioning correctly. When you trigger a reelection of version holders, these new preferred HA devices are selected first. 

  * Guidelines for Preferred HA Version Holder Replacement
  * Creating a Preferred Version Holder
  * Deleting a Preferred Version Holder
  * Triggering the Reelection of Version Holders
  * Displaying Operational Version Holders


### Guidelines for Preferred HA Version Holder Replacement 

Consider the following guidelines when replacing HA version holders: 

  * Both fabric interconnects must be up for device reelection to be triggered. 

  * Cisco UCS Mini does not support preferred HA version holder replacement. 

  * A preferred version holder can be any device that is currently supported for shared storage. 

  * You can specify up to five preferred version holder devices. However, only three devices will be selected for active HA access. 

  * When you trigger shared storage device reelection, it removes all currently active devices and selects a new set of active devices. This set of devices may include previously active devices. Devices that are specified as preferred version holders are selected first as active devices. 

  * You can trigger reelection of shared storage devices at any time. However, the device will be selected as a version holder only in the following scenarios: 

  * When the connection path is both fabric interconnect A and B for UCS B Series blade chassis 

  * When the connection status is both fabric interconnect A and B for UCS C Series racks 

  * For a device to be selected as a version holder, the following requirements must be met: 
  * There must be less than three devices selected for active HA access. 

  * Chassis removal must not be in progress. 

  * A chassis that has been removed from the system must not be used as a version holder. 

  * The connection path must be both fabric interconnect A and B. 

  * Replacement of HA version holders can be done only through Cisco UCS Manager CLI. 


### Creating a Preferred Version Holder 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope system |  Enters system mode.   
**Step 2** |  UCS-A /system # create preferred-ha-device device-serial |  Creates the specified preferred HA device.   
**Step 3** |  UCS-A /system/ preferred-ha-device # commit-buffer |  Commits the transaction to the system configuration.   
**Step 4** |  UCS-A /system/ preferred-ha-device* # exit |  Enters system mode.   
**Step 5** |  UCS-A /system # show preferred-ha-devices |  Displays the list of preferred HA version holders and whether they are active or not.   
  
#### Example

This example shows how to create a preferred version holder: 
    
    
    UCS-A# **scope system**
    UCS-A /system # **create preferred-ha-device FCH1606V02F**
    UCS-A /system/ preferred-ha-device* # **commit-buffer**
    UCS-A /system/ preferred-ha-device # **exit**
    UCS-A /system # **show preferred-ha-devices**
    
    Preferred Version Holder:
        Chassis Serial Active
        -------------- ------
        FCH1606V02F    Yes
        FOX1636H6R3    Yes
        FOX1636H6R4    No
    
    
    

#### What to do next

Trigger a reelection of version holders. 

### Deleting a Preferred Version Holder 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope system |  Enters system mode.   
**Step 2** |  UCS-A /system # delete preferred-ha-device device-serial |  Deletes the specified preferred HA device.   
**Step 3** |  UCS-A /system/ preferred-ha-device* # commit-buffer |  Commits the transaction to the system configuration.   
**Step 4** |  UCS-A /system/ preferred-ha-device # exit |  Enters system mode.   
**Step 5** |  UCS-A /system # show preferred-ha-devices |  Displays the list of preferred HA version holders and whether they are active or not.   
  
#### Example

This example shows how to delete a preferred version holder: 
    
    
    UCS-A# **scope system**
    UCS-A /system # **delete preferred-ha-device FCH1606V02F**
    UCS-A /system/ preferred-ha-device* # **commit-buffer**
    UCS-A /system/ preferred-ha-device # **exit**
    UCS-A /system # **show preferred-ha-devices**
    
    Preferred Version Holder:
        Chassis Serial Active
        -------------- ------
        FOX1636H6R3    Yes
        FOX1636H6R4    No
    
    
     

### Triggering the Reelection of Version Holders 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope system |  Enters system mode.   
**Step 2** |  UCS-A /system # re-elect-ha-devices |  Triggers reelection of version holders for HA devices.   
  
#### Example

This example shows how to trigger the reelection of version holders: 
    
    
    UCS-A# **scope system**
    UCS-A /system # **re-elect-ha-devices**
    
    

### Displaying Operational Version Holders 

You can use this command to display all operational version holders, including preferred version holders. 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope system |  Enters system mode.   
**Step 2** |  UCS-A /system # show operational-ha-devices |  Displays the list of all currently operational HA version holders.   
  
#### Example

This example shows how to display all currently operational version holders: 
    
    
    UCS-A# **scope system**
    UCS-A /system # **show operational-ha-devices**
    
    Current Version Holder:
        Serial
        ------
        FOX1636H6R5
    
    
    

---
