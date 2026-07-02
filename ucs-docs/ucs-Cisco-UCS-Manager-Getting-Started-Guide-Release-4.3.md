# Cisco UCS Manager Getting Started Guide, Release 4.3 - Cisco

| | |
|---|---|
| **URL Title** | Cisco UCS Manager Getting Started Guide, Release 4.3 - Cisco |
| **URL** | https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Getting-Started/4-3/b_ucsm_getting_started_guide_4_3.html |
| **Long URL** |  |
| **HTML Title** | Cisco UCS Manager Getting Started Guide, Release 4.3 |
| **Source file** | `ucs-docs-raw/html/b_ucsm_getting_started_guide_4_3.html` |
| **File type** | HTML |
| **Fetched on** | 2026-07-02 13:01:10 |

---

## Page 1: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Getting-Started/4-3/b_ucsm_getting_started_guide_4_3.html

![Clear Contents of Search](/etc/designs/cdc/fw/i/ic_clear_gray.png)

---

## Page 2: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Getting-Started/4-3/b_ucsm_getting_started_guide_4_3/b_UCSM_Getting_Started_Guide_4_1_preface_00.html

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

## Page 3: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Getting-Started/4-3/b_ucsm_getting_started_guide_4_3/m_new_and_changed_4-3.html

# New and Changed Information 

## New and Changed Information for This Release

The following table provides an overview of the significant changes to this guide for this current release. The table does not provide an exhaustive list of all changes made to this guide or of all new features in this release. 

Table 1. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(6a) Feature |  Description |  Where Documented  
---|---|---  
Support for Cisco UCS C240 M8 Server, Cisco UCS C220 M8 Server, and Cisco UCS X210c M8 Compute Node |  Cisco UCS Manager now includes support for Cisco UCS C240 M8 Server, Cisco UCS C220 M8 Server, and Cisco UCS X210c M8 Compute Node.  |  -  
Table 2. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(5a) Feature |  Description |  Where Documented  
---|---|---  
Support for Cisco UCS X215c M8 Compute Node |  Cisco UCS Manager now includes support for Cisco UCS X215c M8 Compute Node.  |  [Overview of Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct)](m_overview.html#overview-of-cisco-ucs-x-direct)  
Table 3. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(4b) Feature |  Description |  Where Documented  
---|---|---  
Support for Cisco UCS Fabric Interconnects 9108 100G |  Cisco UCS Manager now includes support for Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct).  | 

  * [Cisco UCS Fabric Infrastructure Portfolio](m_overview.html#concept_pmw_z1l_3jb)
  * [Link-Level Flow Control](m_overview.html#concept_7D5436A5ECF144B787687A2A7CBF10A9)
  * [Cisco UCS Building Blocks and Connectivity](m_overview.html#concept_uxd_4pl_3jb)
  * [Overview of Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct)](m_overview.html#overview-of-cisco-ucs-x-direct)
  * [Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct) Architecture](m_overview.html#cisco-ucs-x-direct-architecture)
  * [Port Breakout Functionality on Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct)](m_overview.html#port-breakout-functionality-on-cisco-ucs-x-direct)
  * [Configure the Primary Fabric Interconnect Using GUI](m_initial_configuration.html#task_2382994894256504235)

  
Table 4. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(2c) Feature |  Description |  Where Documented  
---|---|---  
Deprecated support for Cisco UCS 6200 series Fabric Interconnect. |  Cisco UCS Manager support for Cisco UCS 6200 Series Fabric Interconnect is deprecated. |  —

---

## Page 4: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Getting-Started/4-3/b_ucsm_getting_started_guide_4_3/m_overview.html

# Overview  
  
## Cisco UCS Manager User Documentation 

Cisco UCS Manager offers you a new set of smaller, use-case based documentation described in the following table: 

Guide  |  Description   
---|---  
[Cisco UCS Manager Getting Started Guide ](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses Cisco UCS architecture and Day 0 operations, including Cisco UCS Manager initial configuration and configuration best practices.   
[Cisco UCS Manager Administration Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses password management, role-based access configuration, remote authentication, communication services, CIMC session management, organizations, backup and restore, scheduling options, BIOS tokens, and deferred deployments.   
[Cisco UCS Manager Infrastructure Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses physical and virtual infrastructure components used and managed by Cisco UCS Manager.   
[Cisco UCS Manager Firmware Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses downloading and managing firmware, upgrading through Auto Install, upgrading through service profiles, directly upgrading at endpoints using firmware auto sync, managing the capability catalog, deployment scenarios, and troubleshooting.   
[Cisco UCS Manager Server Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses the new licenses, registering Cisco UCS domain with Cisco UCS Central, power capping, server boot, server profiles, and server-related policies.   
[Cisco UCS Manager Storage Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses all aspects of storage management, such as SAN and VSAN in Cisco UCS Manager.   
[Cisco UCS Manager Network Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses all aspects of network management, such as LAN and VLAN connectivity in Cisco UCS Manager.   
[Cisco UCS Manager System Monitoring Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses all aspects of system and health monitoring, including system statistics in Cisco UCS Manager.   
  
## Fundamentals of Cisco Unified Computing System 

  * Cisco Unified Computing System Overview
  * IOMs and Fabric Interconnects Connectivity
  * Unified Fabric
  * Cisco UCS Building Blocks and Connectivity
  * Introduction to Cisco UCS Manager


### Cisco Unified Computing System Overview 

Cisco UCS has a unique architecture that integrates compute, data network access, and storage network access into a common set of components under a single-pane-of-glass management interface. 

Cisco UCS fuses access layer networking and servers. This high-performance, next-generation server system provides a data center with a high degree of workload agility and scalability. The hardware and software components support Cisco's unified fabric, which runs multiple types of data center traffic over a single converged network adapter. 

Figure 1. Cisco Unified Computing System Architecture  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/305001-306000/305219.jpg)

#### Architectural Simplification

The simplified architecture of Cisco UCS reduces the number of required devices and centralizes switching resources. By eliminating switching inside a chassis, network access-layer fragmentation is significantly reduced. Cisco UCS implements Cisco unified fabric within racks and groups of racks, supporting Ethernet and Fibre Channel protocols over 10/25/40 Gigabit Cisco Data Center Ethernet and Fibre Channel over Ethernet (FCoE) links. This radical simplification reduces the number of switches, cables, adapters, and management points by up to two-thirds. All devices in a Cisco UCS domain remain under a single management domain, which remains highly available through the use of redundant components. 

#### High Availability

The management and data plane of Cisco UCS is designed for high availability and redundant access layer fabric interconnects. In addition, Cisco UCS supports existing high availability and disaster recovery solutions for the data center, such as data replication and application-level clustering technologies. 

#### Scalability

A single Cisco UCS domain supports multiple chassis and their servers, all of which are administered through one Cisco UCS Manager. For more detailed information about the scalability, speak to your Cisco representative. 

#### Flexibility

A Cisco UCS domain allows you to quickly align computing resources in the data center with rapidly changing business requirements. This built-in flexibility is determined by whether you choose to fully implement the stateless computing feature. Pools of servers and other system resources can be applied as necessary to respond to workload fluctuations, support new applications, scale existing software and business services, and accommodate both scheduled and unscheduled downtime. Server identity can be abstracted into a mobile service profile that can be moved from server to server with minimal downtime and no need for additional network configuration. 

With this level of flexibility, you can quickly and easily scale server capacity without having to change the server identity or reconfigure the server, LAN, or SAN. During a maintenance window, you can quickly do the following: 

  * Deploy new servers to meet unexpected workload demand and rebalance resources and traffic. 

  * Shut down an application, such as a database management system, on one server and then boot it up again on another server with increased I/O capacity and memory resources. 


#### Optimized for Server Virtualization

Cisco UCS has been optimized to implement VM-FEX technology. This technology provides improved support for server virtualization, including better policy-based configuration and security, conformance with a company's operational model, and accommodation for VMware's VMotion. 

### IOMs and Fabric Interconnects Connectivity

Each chassis is equipped with two IOMs: IOM 1 should be connected to Fabric Interconnect A. IOM 2 should be connected to Fabric Interconnect B. This configuration provides redundant paths, ensuring uninterrupted operation of the Cisco UCS system even in the event of a failure in one of the Fabric Interconnects or IOMs. Additionally, this configuration enables traffic load distribution across both Fabric Interconnects, enhancing load balancing and increasing throughput. As a result, the Cisco UCS system achieves high availability, reliability, and optimal performance, making it ideal for data center environments. 

  * Uplink Connectivity
  * Downlink Connectivity


#### Uplink Connectivity 

Use fabric interconnect ports configured as uplink ports to connect to uplink upstream network switches. Connect these uplink ports to upstream switch ports as individual links, or as links configured as port channels. Port channel configurations provide bandwidth aggregation as well as link redundancy. 

You can achieve northbound connectivity from the fabric interconnect through a standard uplink, a port channel, or a virtual port channel configuration. The port channel name and ID configured on fabric interconnect should match the name and ID configuration on the upstream Ethernet switch. 

It is also possible to configure a port channel as a vPC, where port channel uplink ports from a fabric interconnect are connected to different upstream switches. After all uplink ports are configured, create a port channel for these ports. 

#### Downlink Connectivity 

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
  
### Unified Fabric 

With unified fabric, multiple types of data center traffic can run over a single Data Center Ethernet (DCE) network. Instead of having a series of different host bus adapters (HBAs) and network interface cards (NICs) present in a server, unified fabric uses a single converged network adapter. This type of adapter can carry LAN and SAN traffic on the same cable. 

Cisco UCS uses Fibre Channel over Ethernet (FCoE) to carry Fibre Channel and Ethernet traffic on the same physical Ethernet connection between the fabric interconnect and the server. This connection terminates at a converged network adapter on the server, and the unified fabric terminates on the uplink ports of the fabric interconnect. On the core network, the LAN and SAN traffic remains separated. Cisco UCS does not require that you implement unified fabric across the data center. 

The converged network adapter presents an Ethernet interface and Fibre Channel interface to the operating system. At the server, the operating system is not aware of the FCoE encapsulation because it sees a standard Fibre Channel HBA. 

At the fabric interconnect, the server-facing Ethernet port receives the Ethernet and Fibre Channel traffic. The fabric interconnect (using Ethertype to differentiate the frames) separates the two traffic types. Ethernet frames and Fibre Channel frames are switched to their respective uplink interfaces. 

  * Fibre Channel over Ethernet


#### Fibre Channel over Ethernet 

Cisco UCS leverages Fibre Channel over Ethernet (FCoE) standard protocol to deliver Fibre Channel. The upper Fibre Channel layers are unchanged, so the Fibre Channel operational model is maintained. FCoE network management and configuration is similar to a native Fibre Channel network. 

FCoE encapsulates Fibre Channel traffic over a physical Ethernet link. FCoE is encapsulated over Ethernet with the use of a dedicated Ethertype, 0x8906, so that FCoE traffic and standard Ethernet traffic can be carried on the same link. FCoE has been standardized by the ANSI T11 Standards Committee. 

Fibre Channel traffic requires a lossless transport layer. Instead of the buffer-to-buffer credit system used by native Fibre Channel, FCoE depends upon the Ethernet link to implement lossless service. 

Ethernet links on the fabric interconnect provide two mechanisms to ensure lossless transport for FCoE traffic: 

  * Link-level flow control 

  * Priority flow control 


  * Link-Level Flow Control
  * Priority Flow Control


##### Link-Level Flow Control

IEEE 802.3x link-level flow control allows a congested receiver to signal the endpoint to pause data transmission for a short time. This link-level flow control pauses all traffic on the link. 

The transmit and receive directions are separately configurable. By default, link-level flow control is disabled for both directions. 

On each Ethernet interface, the fabric interconnect can enable either priority flow control or link-level flow control (but not both). 

When an interface on a Cisco UCS Fabric Interconnects 9108 100G, Cisco UCS 6500 Series Fabric Interconnect,  or Cisco UCS 6400 Series Fabric Interconnect has Priority Flow Control (PFC) admin configured as auto and Link-Level Flow Control (LLFC) admin configured as on, the PFC operation mode will be off and the LLFC operation mode will be on. On UCS 6300 Series and earlier Fabric Interconnects, the same configuration will result in the PFC operation mode being on and the LLFC operation mode being off. 

##### Priority Flow Control

The priority flow control (PFC) feature applies pause functionality to specific classes of traffic on the Ethernet link. For example, PFC can provide lossless service for the FCoE traffic, and best-effort service for the standard Ethernet traffic. PFC can provide different levels of service to specific classes of Ethernet traffic (using IEEE 802.1p traffic classes). 

PFC decides whether to apply pause based on the IEEE 802.1p CoS value. When the fabric interconnect enables PFC, it configures the connected adapter to apply the pause functionality to packets with specific CoS values. 

By default, the fabric interconnect negotiates to enable the PFC capability. If the negotiation succeeds, PFC is enabled and link-level flow control remains disabled (regardless of its configuration settings). If the PFC negotiation fails, you can either force PFC to be enabled on the interface or you can enable IEEE 802.x link-level flow control. 

### Cisco UCS Building Blocks and Connectivity

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


#### Cisco UCS Fabric Infrastructure Portfolio

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
  
Cisco UCS Manager Fabric Interconnects

Cisco UCS X-Series Direct

#### Overview of Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct) 

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

#### Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct) Architecture 

The Cisco UCS X-Series Direct architecture is engineered to support a diverse range of workloads, from traditional applications to cloud-native services, by offering a composable and disaggregated approach to computing resources. Key components of the Cisco UCS X-Series Direct architecture include: 

  * **Cisco UCSX-9508 Chassis** —A modular and future-proof chassis that can accommodate various types of compute nodes, providing the flexibility to adapt to different workload requirements without the need for a complete hardware overhaul. 

  * **Cisco UCS Fabric Interconnects 9108 100G** —This solution is centered around a single-chassis system, the Cisco UCS X9508 Chassis, which incorporates Cisco UCS Fabric Interconnects 9108 100G directly into the chassis for a consolidated and efficient infrastructure. To ensure high availability, each chassis houses two Cisco UCS Fabric Interconnects 9108 100G that establish direct downlink connections to servers and provide uplink connections to facilitate seamless integration with both Local Area Network (LAN) and Storage Area Network (SAN) systems. 

  * **Software Architecture** —In terms of the startup and operational model, the management, Cisco UCS Manager aligns with the approach taken in the Cisco UCS 6500 and 6400 Series Fabric Interconnects. In this model, Cisco UCS Manager is encapsulated within a container and is initiated by the underlying NX-OS, depending on the selected management mode. 


#### Port Breakout Functionality on Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct) 

The Cisco UCS Fabric Interconnects 9108 100G is equipped with advanced port breakout functionality, which allows network administrators to subdivide a single high-bandwidth port into multiple lower-bandwidth ports. This feature is particularly beneficial for optimizing port utilization, managing cabling complexity, and adapting to various bandwidth requirements. 

Physical Port |  Breakout Options |  Logical Ports After Breakout |  Supported Speeds through breakout cables  
---|---|---|---  
Ethernet 1/1 - Ethernet 1/8 |  4x25G |  Ethernet 1/1/1 to Ethernet 1/8/4 |  Up to 8x100 Gbps  
Fibre Channel 1/1 and 1/2 |  4x8G, 4x16G, 4x32G |  Fibre Channel 1/1/1 to Fibre Channel 1/2/4 |  Up to 8x32Gbps  
  
##### Breakout Port Guidelines

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

#### **Cisco UCS 6536 Fabric Interconnect**

The Cisco UCS 6536 Fabric Interconnect (UCSC-FI-6536) is a One-rack unit (1RU), top of rack (TOR), fixed-port data center platform that provides both network connectivity and management capabilities to the Cisco UCS system. 

The fabric interconnect can provide Ethernet and Fibre Channel connectivity to the servers in the system. The servers connect to the fabric interconnect, and then to the LAN or SAN. 

Cisco UCS Manager on UCS 6536 Fabric Interconnect supports Cisco UCS X-Series Compute Nodes, B-Series Blade Servers and C-Series Rack Servers, Cisco UCS S-Series Storage Servers, as well as the associated storage resources and networks. 

High availability and redundancy can be achieved by connecting a pair of fabric interconnects to each other through L1 or L2 ports in cluster mode configuration. 

Each Cisco UCS 6536 Fabric Interconnect offers the following features: 

  * Thirty-six QSFP28 ports capable of 100G including 4 unified ports (33-36). Ports also support: 

  * Autonegotiating with peer devices to speeds of 100G, 40G, 25G, 10G, and 1G.

  * Port breakout is supported for Ethernet ports (1-32) and Unified ports (33-36). 

  * Ethernet breakout is supported on switch ports 1 through 36 when each port is configured with a breakout cable. 

  * The Dynamic Ethernet Breakout feature enables converting a standard Ethernet port to a breakout port on-the-fly so that you do not need to reboot the Fabric Interconnect. Dynamic Ethernet Breakout also supports converting breakout ports back to a standard Ethernet port without a reboot. 

  * FC breakout is supported on ports 33 through 36 wherein each port is configured with a four-port breakout cable. For example 1/33/1, 1/33/2, 1/33/3, and 1/33/4 are the four FC breakout ports on the physical port 33. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Fibre Channel support is only available through the configuration of Unified Ports (33-36) as FC breakout port.

* * *  
  
---|---  
  * FC breakout ports support peer communication at fixed speeds of 8Gbs, 16 Gbps, and 32 Gbps. 

  * All four FC breakout ports must be configured with the same speed. Mixed speeds on a QSFP port's FC breakout ports are not supported. 

  * Using breakout ports enables the fabric interconnect to support the maximum 16 FC ports supported by Fibre Channel.

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

  * Converting from Ethernet to FC breakout ports, or FC breakout ports back to Ethernet, requires a reboot/reload after changing the breakout type. 
  * FCoE storage ports are not supported. 

* * *  
  
---|---  
  * One management port (one 10/100/1000BASE-T port)

  * Two L1/L2 Ethernet RJ-45 ports for high availability or cluster configurations. Ethernet ports support 10/100/1000Mb speed.

  * One console port (RS-232)

  * One USB 3.0 port

  * CPU: 4 Core, 1.8GHz, Intel 5th-Generation core processor

  * Memory: 

  * 32 GB DDR4 DIMMs

  * 128 GB M.2 SSD Flash Drive

  * 32 GB Boot Flash (16 MB primary, and 16 MB standby/golden)


This fabric interconnect includes the following user-replaceable components:

  * Fan modules (6), each is a port-side exhaust fan module with dark grey latch coloring (UCS-FAN-6536).

  * Power supply modules (2). One power supply module (PSU) is the active module for operations, and the second PSU is the standby for redundancy [1+1]) with the following choices: 

  * 1100-W AC power supply with dark grey latch coloring (UCS-PSU-6536-AC)

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

All fan modules and power supplies must use the same airflow direction.

* * *  
  
---|---  


The following figure shows the fabric interconnect features on the port side of the chassis. 

![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540351.jpg) 1  |  LEDs  |  3  |  36 40/100-Gigabit QSFP28 ports  
---|---|---|---  
2  |  Lane Select button  |  |   
  
To determine which transceivers, adapters, and cables are support the fabric interconnect, see the [Cisco Transceiver Modules Compatibility Information](http://www.cisco.com/c/en/us/support/interfaces-modules/transceiver-modules/products-device-support-tables-list.html) document. 

The following figure shows the fabric interconnect features on the power supply side of the chassis. 

![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540354.jpg) 1  |  Power supply modules (1 or 2) (AC power supplies shown) with slots numbered 1 (left) and 2 (right). |  2  |  Fan modules (6) with slots numbered from 1 (left) to 6 (right).  
---|---|---|---  
3  |  Layer 2 (L2) Ethernet port, 10/100/100Mb autonegotiating. Supports high availability (HA) or clustering through an RJ-45 port. |  4  |  Layer 1 (L1) Ethernet port, 10/100/100Mb autonegotiating.  Supports high availability (HA) or clustering through an RJ-45 port.  
5 |  Ethernet network management port (RJ45), 10/100/1000Mb autonegotiating  |  6  |  Serial Console port (RJ45), 9600 baud.  
7 |  USB 3.0/2.0 port Supports booting the system and downloading scripts. |  8 |  Beacon (BCN) LED  
9 |  Status (STS) LED |  - |   
  
The following figure shows the side of the chassis. 

![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540353.jpg) 1  |  Screw holes for mounting brackets |  2  |  Grounding pad  
---|---|---|---  
  
Plan to position the ports in a hot aisle so that fans and power supplies intake air from the cold aisle, blow the cool air through the fabric interconnect, and exhaust the heated air into the hot aisle. 

The fan and power supply modules are field replaceable. You can replace one fan module or one power supply module during operations so long as the other modules are installed and operating. If you have only one power supply installed, you can install the replacement power supply in the open slot before removing the original power supply. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

All fan and power supply modules must have the same direction of airflow. Otherwise, the fabric interconnect can overheat and shut down. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Because fans and power supply modules have port-side exhaust airflow (blue coloring for fan modules), you must locate the ports in the hot aisle. If you locate the air intake in a hot aisle, the fabric interconnect can overheat and shut down. 

* * *  
  
---|---  
  
#### Port Breakout Functionality on Cisco UCS 6536 Fabric Interconnects

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
  
##### Breakout Port Guidelines

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

#### Cisco UCS 6400 Series Fabric Interconnect Overview 

Cisco UCS 6400 Series Fabric Interconnect provides both network connectivity and management capabilities to the Cisco UCS system. The fabric interconnect provides Ethernet and Fibre Channel to the servers in the system, the servers connect to the fabric interconnect, and then to the LAN or SAN. 

Each Cisco UCS 6400 Series Fabric Interconnect runs Cisco UCS Manager to fully manage all Cisco UCS elements. The fabric interconnect supports 10/25 Gigabit ports in the fabric with 40/100 Gigabit uplink ports. High availability can be achieved when a Cisco UCS 6400 Series Fabric Interconnect is connected to another Cisco UCS 6400 Series Fabric Interconnect through the L1 or L2 port on each device. 

Cisco UCS 6400 Series Fabric Interconnect consists of: 

  * Cisco UCS 6454 Fabric Interconnects 

  * Cisco UCS 64108 Fabric Interconnects 


The Cisco UCS 6400 Series fabric interconnect supports Cisco UCS B-Series Blade Servers, UCS 5108 B-Series Server Chassis, C-Series Rack Servers, and UCS S-Series Storage Servers. 

#### Cisco UCS 64108 Fabric Interconnect

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
  
#### Port Breakout Functionality on Cisco UCS 64108 Fabric Interconnects

##### About Breakout Ports

Cisco UCS 64108 fabric interconnects support splitting a single 40/100G QSFP port into four 10/25G ports using a supported breakout cable. On the UCS 64108 fabric interconnect, by default, there are 12 ports in the 40/100G mode. These are ports 97 to 108. These 40/100G ports are numbered in a 2-tuple naming convention. For example, the second 40G port is numbered as 1/99. The process of changing the configuration from 40G to 10 G, or from 100G to 25G is called breakout, and the process of changing the configuration from [4X]10G to 40G or from [4X]25G to 100G is called unconfigure. These ports can be used as uplink port, appliance port, server port (using FEX), and FCoE storage port. 

When you break out a 40G port into 10G ports or a 100G port into 25G ports, the resulting ports are numbered using a 3-tuple naming convention. For example, the breakout ports of the second 40-Gigabit Ethernet port are numbered as 1/99/1, 1/99/2, 1/99/3, 1/99/4. 

Starting with Cisco UCS Manager Release 4.2(3b), configuring the Ethernet breakout ports will not lead to Fabric Interconnect reboot. 

The following image shows the rear view of the Cisco UCS 64108 fabric interconnect, and includes the ports that support breakout port functionality: 

Figure 7. Cisco UCS 64108 Fabric Interconnect Rear View ![](/c/dam/en/us/td/i/300001-400000/300001-310000/307001-308000/307644.jpg) 1  |  Ports 1-16. Unified Ports can operate as 10/25 Gbps Ethernet or 8/16/32 Gbps Fibre Channel. FC ports are converted in groups of four.  Unified ports:

  * 10/25 Gbps Ethernet or FCoE
  * 8/16/32 Gbps Fibre Channel

|  2  |  Ports 1-96. Each port can operate as either a 10 Gbps or 25 Gbps Ethernet or FCoE SFP28 port.   
---|---|---|---  
3  |  Uplink Ports 97-108. Each port can operate as either a 40 Gbps or 100 Gbps Ethernet or FCoE port. When using a breakout cable, each of these ports can operate as 4 x 10 Gbps or 4 x 25 Gbps Ethernet or FCoE ports.  Ports 97 - 108 can be used to connect to Ethernet or FCoE uplink ports, and not to UCS server ports. |  4 |  Ports 89-96

  * 10/25 Gbps Ethernet or FCoE
  * 1 Gbps Ethernet

  
5 |  System environment (fan fault) LED |  6 |  System status LED  
7 |  Beacon LED |  |   
  
##### Breakout Port Guidelines

The following are the guidelines for breakout functionality for Cisco UCS 64108 fabric interconnects: 

  * The breakout configurable ports are ports 97-108.

  * You cannot configure the speed for each breakout port. Each breakout port is in auto mode.

  * Breakout ports are not supported as destinations for traffic monitoring.

  * Ports 97-108 at 40/100G can be configured as uplink, FCoE, or appliance port. Ports 97-108 after breakout to 10/25G can be configured as uplink, appliance, FCoE, or for direct-connect rack server connectivity. 


#### Cisco UCS 6454 Fabric Interconnect

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


Figure 8. Cisco UCS 6454 Fabric Interconnect Rear View ![](/c/dam/en/us/td/i/300001-400000/300001-310000/306001-307000/306755.jpg) 1  |  Ports 1-16 (Unified Ports 10/25 Gbps Ethernet or FCoE or 8/16/32 Gbps Fibre Channel) |  **Note** |  When using Cisco UCS Manager releases earlier than 4.0(4), only ports 1-8 are Unified Ports.  
---|---  
2  |  Ports 17-44 (10/25 Gbps Ethernet or FCoE) |  **Note** |  When using Cisco UCS Manager releases earlier than 4.0(4), ports 9-44 are 10/25 Gbps Ethernet or FCoE.  
---|---  
3  |  Ports 45-48 (1/10/25 Gbps Ethernet or FCoE)  |  4 |  Uplink Ports 49-54 (40/100 Gbps Ethernet or FCoE) Each of these ports can be 4 x 10/25 Gbps Ethernet or FCoE uplink ports when using an appropriate breakout cable.  
  
The Cisco UCS 6454 Fabric Interconnect chassis has two power supplies and four fans. Two of the fans provide front to rear airflow. 

Figure 9. Cisco UCS 6454 Fabric Interconnect Front View ![](/c/dam/en/us/td/i/300001-400000/300001-310000/306001-307000/306354.jpg) **1** |  Power supply and power cord connector  |  **2** |  Fans 1 through 4, numbered left to right, when facing the front of the chassis.  
---|---|---|---  
**3** |  L1 port, L2 port, RJ45, console, USB port, and LEDs |  |   
  
#### Port Breakout Functionality on Cisco UCS 6454 Fabric Interconnects

##### About Breakout Ports

Cisco UCS 6454 fabric interconnects support splitting a single 40/100G QSFP port into four 10/25G ports using a supported breakout cable. These ports can be used only as uplink ports connecting to a 10/25G switch. On the UCS 6454 fabric interconnect, by default, there are 6 ports in the 40/100G mode. These are ports 49 to 54. These 40/100G ports are numbered in a 2-tuple naming convention. For example, the second 40G port is numbered as 1/50. The process of changing the configuration from 40G to 10 G, or from 100G to 25G is called breakout, and the process of changing the configuration from [4X]10G to 40G or from [4X]25G to 100G is called unconfigure. 

When you break out a 40G port into 10G ports or a 100G port into 25G ports, the resulting ports are numbered using a 3-tuple naming convention. For example, the breakout ports of the second 40-Gigabit Ethernet port are numbered as 1/50/1, 1/50/2, 1/50/3, 1/50/4. 

Starting with Cisco UCS Manager Release 4.2(3b), Ethernet breakout ports configuration will not lead to Fabric Interconnect reboot. 

The following image shows the rear view of the Cisco UCS 6454 fabric interconnect, and includes the ports that support breakout port functionality: 

Figure 10. Cisco UCS 6454 Fabric Interconnect Rear View ![](/c/dam/en/us/td/i/300001-400000/300001-310000/306001-307000/306755.jpg) 1  |  Ports 1-16 (Unified Ports 10/25 Gbps Ethernet or FCoE or 8/16/32 Gbps Fibre Channel) |  2  |  Ports 17-44 (10/25 Gbps Ethernet or FCoE)  
---|---|---|---  
3  |  Ports 45-48 (1/10/25 Gbps Ethernet or FCoE)  |  4 |  Uplink Ports 49-54 (40/100 Gbps Ethernet or FCoE)   
  
##### Breakout Port Guidelines

The following are the guidelines for breakout functionality for Cisco UCS 6454 fabric interconnects: 

  * The breakout configurable ports are ports 49-54.

  * You cannot configure the speed for each breakout port. Each breakout port is in auto mode.

  * In Cisco UCS Manager Release 4.0(2), breakout ports are not supported as destinations for traffic monitoring.

  * Ports 49-54 at 40/100G can be configured as uplink, FCoE, or appliance port. Ports 49-54 after breakout to 10/25G can be configured as uplink, appliance, FCoE, or for direct-connect rack server connectivity. 


Cisco UCS 6300 Series Fabric Interconnects

#### Fabric Interconnect Features 

A Cisco UCS 6300 Series Fabric Interconnect provides both network connectivity and management capabilities to a Cisco UCS system. The fabric interconnect provides Ethernet and Fibre Channel to the servers in the system, the servers connect to the fabric interconnect, and the fabric interconnect connects to the LAN or SAN. 

Each Cisco UCS 6300 Series Fabric Interconnect runs Cisco UCS Manager to fully manage all Cisco UCS elements. The fabric interconnect supports full end-to-end 40-Gigabit capabilities in the fabric and enables 16-Gigabit Fibre Channel capabilities. High availability can be achieved when a Cisco UCS 6300 Series Fabric Interconnect is connected to another Cisco UCS 6300 Series Fabric Interconnect through the L1 or L2 port on each device. 

The Cisco UCS 6300 Series Fabric Interconnect joins next-generation UCS products, including the following hardware: 

  * Cisco UCS 6332 Fabric Interconnect, an Ethernet or Fibre Channel over Ethernet (FCoE) chassis with 32 40-Gigabit QSFP+ ports 

  * Cisco UCS 6332-16UP Fabric Interconnect, an Ethernet, FCoE, and Fibre Channel chassis with 16 1- or 10-Gigabit SFP+ ports or 16 4-, 8-, or 16-Gigabit Fibre Channel ports, 24 40-Gigabit QSFP+ ports 

  * Cisco 2304 IOM  or Cisco 2304V2, I/O modules with 8 40-Gigabit backplane ports and 4 40-Gigabit uplink ports 

  * Multiple VICs 


#### Cisco UCS 6332 Fabric Interconnect 

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
  
#### Cisco UCS 6332-16UP Fabric Interconnect 

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
  
#### Ports on the Cisco UCS 6300 Series Fabric Interconnects 

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


##### Port Modes

The port mode determines whether a unified port on the fabric interconnect is configured to carry Ethernet or Fibre Channel traffic. You configure the port mode in Cisco UCS Manager. However, the fabric interconnect does not automatically discover the port mode. 

Changing the port mode deletes the existing port configuration and replaces it with a new logical port. Any objects associated with that port configuration, such as VLANs and VSANS, are also removed. There is no restriction on the number of times you can change the port mode for a unified port. 

##### Port Types

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


##### Port Breakout Functionality on Cisco UCS 6300 Series Fabric Interconnects 

###### About Breakout Ports 

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
  
###### Breakout Port Constraints 

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
  
#### Ports on the Cisco UCS Fabric Interconnects

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
  
#### Migration for Cisco UCS Fabric Interconnects

Cisco UCS Manager allows you to migrate from the following:

  * Cisco UCS 6200 Series to UCS 6500 Fabric Interconnects. 

  * Cisco UCS 6300 Series to UCS 6500 Fabric Interconnects.

  * Cisco UCS 6400 Series to Cisco UCS 6536 Fabric Interconnect

  * Cisco UCS 6454 Series to Cisco UCS 6536 Fabric Interconnect

  * Cisco UCS 64108 Series to Cisco UCS 6536 Fabric Interconnect

  * Cisco UCS 6454 Series to Cisco UCS 6536 Fabric Interconnect migration to UCS Central

  * Cisco UCS 64108 Series to Cisco UCS 6536 Fabric Interconnect migration to UCS Central


For more information, refer to the corresponding _Migration Guide for Cisco UCS Fabric Interconnects_ on the [Cisco UCS Manager Configuration Guides](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) listing page. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct) cannot currently be migrated to any other Fabric Interconnects. 

* * *  
  
---|---  
  
### Introduction to Cisco UCS Manager

Cisco UCS Manager is embedded software that resides on the fabric interconnects, providing complete configuration and management capabilities for all of the components in the Cisco UCS system. This configuration information is replicated between the two fabric interconnects, providing a highly available solution for this critical function. The most common way to access Cisco UCS Manager for simple tasks is to use a Web browser. A command-line interface (CLI) and an XML API are also included for command-line or programmatic operations. 

The Cisco UCS Manager GUI provides role-based access control (RBAC) to allow multiple levels of users administrative rights to system objects. Users can be restricted to certain portions of the system based on locale, which corresponds to an optional organizational structure that can be created. Users can also be classified based on their access levels or areas of expertise, such as Storage Administrator, Server Equipment Administrator, or Read-Only. 

Cisco UCS Manager provides unified, embedded management of all software and hardware components. Every instance of Cisco UCS Manager and all of the components managed by it form a domain. For organizations that deploy multiple Cisco UCS domains, Cisco UCS Central software provides a centralized user interface that allows you to manage multiple, globally distributed Cisco UCS domains with thousands of servers. Cisco UCS Central integrates with Cisco UCS Manager and utilizes it to provide global configuration capabilities for pools, policies, and firmware. 

## Configuration Options 

You can configure a Cisco UCS domain in the following ways: 

  * As a single fabric interconnect in a standalone configuration 

  * As a redundant pair of fabric interconnects in a cluster configuration 


A cluster configuration provides high availability. If one fabric interconnect becomes unavailable, the other takes over. Only one management port (Mgmt0) connection is required to support a cluster configuration. However, both Mgmt0 ports should be connected to provide link-level redundancy. In a cluster configuration, the master and slave slots are identified as primary and subordinate. 

In addition, a cluster configuration actively enhances failover recovery time for redundant virtual interface (VIF) connections. When an adapter has an active VIF connection to one fabric interconnect and a standby VIF connection to the second, the learned MAC addresses of the active VIF are replicated but not installed on the second fabric interconnect. If the active VIF fails, the second fabric interconnect installs the replicated MAC addresses and broadcasts them to the network through gratuitous ARP messages, shortening the switchover time. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The cluster configuration provides redundancy only for the management plane. Data redundancy is dependent on the user configuration and might require a third-party tool to support data redundancy. 

* * *  
  
---|---

---

## Page 5: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Getting-Started/4-3/b_ucsm_getting_started_guide_4_3/m_system_requirements.html

# System Requirements   
  
## System Requirements Overview 

The following minimum hardware, browser, and port requirements must be met prior to Cisco UCS Manager initial configuration. 

## Hardware Requirements 

Before you set up Cisco UCS Manager, make sure that the following physical cabling requirements are met:  ![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The Cisco UCS Fabric Interconnects act as the concentration point for all cabling to and from the Blade Server Chassis. The following diagram shows the Cisco UCS Fabric Interconnects Cluster Connectivity. 

* * *  
  
---|---  
Figure 1. Cisco UCS Fabric Interconnects Physical Cable Connectivity   
![](/c/dam/en/us/td/i/300001-400000/300001-310000/305001-306000/305199.jpg)  


  * Connect the two fabric interconnects using the integrated ports labeled L1 and L2. These ports are used for replication of cluster information between the two fabric interconnects, not for the forwarding of data traffic. 

  * The management Ethernet ports of each fabric interconnect to the out-of-band Ethernet management network or Ethernet segment where they can be accessed for overall administration of the system. 

  * Populate each blade chassis with two fabric extenders (I/O modules) to provide connectivity back to the fabric interconnects. 

  * From the Blade Server Chassis, connect one I/O module to the first fabric interconnect. Connect the second I/O module to the second fabric interconnect. After you have configured the fabric interconnects, they will be designated as "A" and "B" fabric interconnects. 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

You can connect the I/O modules to the fabric interconnects by using one, two, four, or eight cables per module. For system resiliency and throughput, it is recommended that you use a minimum of two connections per I/O module 

* * *  
  
---|---  
  
##  Browser Requirements 

To use Cisco UCS Manager your computer must meet or exceed the following minimum browser requirements: 

  * Cisco UCS Manager uses web start and supports the following web browsers: 

  * Apple Safari 16.2 (18614.3.7.1.5)

  * Google Chrome 109.0.5414.75

  * Microsoft Internet Explorer 11.0.9600.18739 (Microsoft Internet

  * Explorer is Retired. Support is available only until Windows 8.1

  * Microsoft Edge 109.0.1518.55

  * Mozilla Firefox 108.0.2

  * Opera 94.0.4606.76


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

HTML-5 UI supports one user session per browser. 

* * *  
  
---|---  
  
## Port Requirements 

### Hardware and Software Requirements 

Cisco UCS 6332 and Cisco UCS 6332-16UP ports are supported on the Cisco UCS 6300 Series Fabric Interconnects with Cisco UCS Manager 3.1 and later releases. 

### Port Channel Requirements 

The ports with the same speed can be configured in a port channel. A port channel cannot have both breakout and regular ports due to the difference in the speed. 

---

## Page 6: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Getting-Started/4-3/b_ucsm_getting_started_guide_4_3/m_initial_configuration.html

# Initial Configuration 

## Initial Configuration Overview 

Before you get started with Cisco UCS Manager initial configuration, review the Fundamentals of Cisco Unified Computing System and System Requirements sections in this guide. 

The Cisco UCS Manager initial configuration involves the following steps: 

Figure 1. Cisco UCS Manager Initial Configuration Overview   
![](/c/dam/en/us/td/i/300001-400000/300001-310000/305001-306000/305200.jpg)  


  1. Console Setup—This step involves launching Cisco UCS Manager using the serial console. The Fabric Interconnect runs an initial configuration wizard and assigns three IP addresses in the management and administrative subnet: one for each Fabric Interconnect and one for the virtual IP interface that defines the Cisco UCS Manager instance and enables management. For more information on this step, see Console Setup

  2. Configure Administration Policies—This step involves configuration of administration policies, such as DNS Server, NTP, and Time Zone, that are necessary for proper functioning of all components. For more information on this step, see Configure Administration Policies. 

  3. Configure Equipment Policies—This step involves performing chassis discovery by setting the equipment policies in Cisco UCS Manager. The Chassis Discovery Policy specifies the minimum number of connections between the I/O modules and the Fabric Interconnects. This value must be set explicitly. For more information on this step, see Configure Equipment Policies

  4. Configure Unified Ports—This step involves configuring Unified Ports on the primary and subordinate Fabric Interconnects. Configure Unified Ports

  5. Configure Fabric Interconnect Server Ports—This step involves configuring Fabric Interconnect Server Ports. For more information on this step, see Configure Fabric Interconnect Server Ports
  6. Configure LAN Connectivity—This step involves establishing initial LAN connectivity from Fabric Interconnects. For more information on this step, see Configure LAN Connectivity. 

  7. Configure SAN Connectivity—This step involves establishing initial SAN connectivity from Fabric Interconnects. For more information on this step, see Configure SAN Connectivity

  8. Define Workloads—After completing initial configuration, you can define your workloads. For more information on this step, see Define Workloads. 


## Console Setup 

Initial configuration of Cisco UCS Fabric Interconnects is performed using the console connection. It is essential to maintain symmetric Cisco UCS Manager versions between the fabric interconnects in a domain. Refer to the latest Cisco UCS Manager Release Notes, and Firmware Management guide to determine the supported firmware versions. 

### Before you begin 

Collect the following required information for the console setup: 

  * System name 

  * Password for the admin account. Choose a strong password that meets the guidelines for Cisco UCS Manager passwords. The password field cannot be blank. 

  * Management port IPv4 and subnet mask, or IPv6 address and prefix. 

  * Default gateway IPv4 or IPv6 address. 

  * DNS server IPv4 or IPv6 address (optional). 

  * Domain name for the system (optional). 


### Installation method 

You can set up Cisco UCS Manager via GUI or CLI. 

Installation Method  |  See   
---|---  
GUI |  Configure the Primary Fabric Interconnect Using GUI  
CLI |  Configure the Primary Fabric Interconnect Using CLI  
  
  * Configure Fabric Interconnects
  * Verify Console Setup


### Configure Fabric Interconnects 

Initial configuration of Fabric Interconnects is performed using the console connection. It is essential to maintain symmetric Cisco UCS Manager versions between the Fabric Interconnects in a domain. Refer to the latest Cisco UCS Manager Release Notes, and Firmware Management guide to determine the supported firmware versions. 

  * Configure the Primary Fabric Interconnect Using GUI
  * Configure the Subordinate Fabric Interconnect Using GUI
  * Configure the Primary Fabric Interconnect Using CLI
  * Configure the Subordinate Fabric Interconnect Using CLI


#### Configure the Primary Fabric Interconnect Using GUI

You can either follow the procedure below for configuring the primary fabric interconnect or watch [Cisco UCS Manager Initial Setup part 1](http://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/videos/3-1/cisco_ucs_manager_initial_setup.html). 

##### Procedure

* * *

**Step 1** |  Power on the fabric interconnect.  You will see the power on self-test messages as the fabric interconnect boots.   
---|---  
**Step 2** |  If the system obtains a lease, go to step 6, otherwise, continue to the next step.   
**Step 3** |  Connect to the console port.   
**Step 4** |  At the installation method prompt, enter `gui`.   
**Step 5** |  If the system cannot access a DHCP server, you are prompted to enter the following information: 

  * IPv4 or IPv6 address for the management port on the fabric interconnect. 
  * IPv4 subnet mask or IPv6 prefix for the management port on the fabric interconnect. 
  * IPv4 or IPv6 address for the default gateway assigned to the fabric interconnect. 

|  **Note** |  In a cluster configuration, both fabric interconnects must be assigned the same management interface address type during setup.   
---|---  
**Step 6** |  Copy the web link from the prompt into a web browser and go to the Cisco UCS Manager GUI launch page.   
**Step 7** |  On the Cisco UCS Manager GUI launch page, select Express Setup.   
**Step 8** |  On the Express Setup page, select Initial Setup and click Submit.  |  **Note** |  In the Fabric Interconnects initial setup page, if the Fabric Interconnect defaults to Intersight managed mode, you can choose to change during confirmation and select required mode again in console setup method alone. This is applicable for Cisco UCS 6400 Series, 6500 SeriesFabric Interconnects , and Cisco UCS Fabric Interconnects 9108 100G.   
---|---  
**Step 9** |  In the Cluster and Fabric Setup area: 

  1. Click the Enable Clustering option. 
  2. For the Fabric Setup option, select Fabric A. 
  3. In the Cluster IP Address field, enter the IPv4 or IPv6 address that Cisco UCS Manager will use. 

  
**Step 10** |  In the System Setup area, complete the following fields:  |  **Field** |  **Description**  
---|---  
System Name |  The name assigned to the Cisco UCS domain.  In a standalone configuration, the system adds "-A" to the system name. In a cluster configuration, the system adds "-A" to the fabric interconnect assigned to fabric A, and "-B" to the fabric interconnect assigned to fabric B.   
Admin Password |  The password used for the Admin account on the fabric interconnect.  Choose a strong password that meets the guidelines for Cisco UCS Manager passwords. This password cannot be blank.   
Confirm Admin Password |  The password used for the Admin account on the fabric interconnect.   
Mgmt IP Address |  The static IPv4 or IPv6 address for the management port on the fabric interconnect.   
Mgmt IP Netmask or Mgmt IP Prefix  |  The IPv4 subnet mask or IPv6 prefix for the management port on the fabric interconnect.  |  **Note** |  The system prompts for a Mgmt IP Netmask or a Mgmt IP Prefix based on what address type you entered in the Mgmt IP Address.   
---|---  
Default Gateway |  The IPv4 or IPv6 address for the default gateway assigned to the management port on the fabric interconnect.  |  **Note** |  The system prompts for a Default Gateway address type based on what type you entered in the Mgmt IP Address field.   
---|---  
DNS Server IP |  The IPv4 or IPv6 address for the DNS Server assigned to the fabric interconnect.   
Domain Name |  The name of the domain in which the fabric interconnect resides.   
**Step 11** |  Click Submit.  A page displays the results of your setup operation.   
  
* * *

#### Configure the Subordinate Fabric Interconnect Using GUI

You can either follow the procedure below for configuring the subordinate fabric interconnect or watch[ Cisco UCS Manager Initial Setup part 2](http://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/videos/3-1/cisco_ucs_manager_initial_setup.html). 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

When adding a new fabric interconnect to an existing High Availability cluster, for example, during a new install or when replacing a fabric interconnect, the new device will not be able to log into the cluster as long as the authentication method is set to remote. To successfully add a new fabric interconnect to the cluster, the authentication method must be temporarily set to local and the local admin credentials of the primary fabric interconnect must be used. 

* * *  
  
---|---  
  
##### Procedure

* * *

**Step 1** |  Power up the fabric interconnect.  You will see the power-up self-test message as the fabric interconnect boots.   
---|---  
**Step 2** |  If the system obtains a lease, go to step 6, otherwise, continue to the next step.   
**Step 3** |  Connect to the console port.   
**Step 4** |  At the installation method prompt, enter `gui`.   
**Step 5** |  If the system cannot access a DHCP server, you are prompted to enter the following information: 

  * IPv4 or IPv6 address for the management port on the fabric interconnect 
  * IPv4 subnet mask or IPv6 prefix for the management port on the fabric interconnect 
  * IPv4 or IPv6 address for the default gateway assigned to the fabric interconnect 

|  **Note** |  In a cluster configuration, both fabric interconnects must be assigned the same management interface address type during setup.   
---|---  
**Step 6** |  Copy the web link from the prompt into a web browser and go to the Cisco UCS Manager GUI launch page.   
**Step 7** |  On the Cisco UCS Manager GUI launch page, select Express Setup.   
**Step 8** |  On the Express Setup page, select Initial Setup and click Submit.  The fabric interconnect should detect the configuration information for the first fabric interconnect.   
**Step 9** |  In the Cluster and Fabric Setup Area: 

  1. Select the Enable Clustering option. 
  2. For the Fabric Setup option, make sure Fabric B is selected. 

  
**Step 10** |  In the System Setup Area, enter the password for the Admin account into the Admin Password of Master field.  The Manager Initial Setup Area is displayed.   
**Step 11** |  In the Manager Initial Setup Area, the field that is displayed depends on whether you configured the first fabric interconnect with an IPv4 or IPv6 management address. Complete the field that is appropriate for your configuration, as follows:  |  Field  |  Description   
---|---  
Peer FI is IPv4 Cluster enabled. Please Provide Local fabric interconnect Mgmt0 IPv4 Address |  Enter an IPv4 address for the Mgmt0 interface on the local fabric interconnect.   
Peer FI is IPv6 Cluster Enabled. Please Provide Local fabric interconnect Mgmt0 IPv6 Address |  Enter an IPv6 for the Mgmt0 interface on the local fabric interconnect.   
**Step 12** |  Click Submit.  A page displays the results of your setup operation.   
  
* * *

#### Configure the Primary Fabric Interconnect Using CLI

##### Procedure

* * *

**Step 1** |  Connect to the console port.   
---|---  
**Step 2** |  Power on the fabric interconnect. You will see the power-on self-test messages as the fabric interconnect boots.   
**Step 3** |  When the unconfigured system boots, it prompts you for the setup method to be used. Enter  console to continue the initial setup using the console CLI.   
**Step 4** |  Enter  setup to continue as an initial system setup.   
**Step 5** |  Enter  y to confirm that you want to continue the initial setup.   
**Step 6** |  Enter the password for the admin account.   
**Step 7** |  To confirm, re-enter the password for the admin account.   
**Step 8** |  Enter  yes to continue the initial setup for a cluster configuration.   
**Step 9** |  Enter the fabric interconnect fabric (either  A or  B ).   
**Step 10** |  Enter the system name.   
**Step 11** |  Enter the IPv4 or IPv6 address for the management port of the fabric interconnect.  If you enter an IPv4 address, you will be prompted to enter an IPv4 subnet mask. If you enter an IPv6 address, you will be prompted to enter an IPv6 network prefix.   
**Step 12** |  Enter the respective IPv4 subnet mask or IPv6 network prefix, then press `Enter`.  You are prompted for an IPv4 or IPv6 address for the default gateway, depending on the address type you entered for the management port of the fabric interconnect.   
**Step 13** |  Enter either of the following: 

  * IPv4 address of the default gateway 
  * IPv6 address of the default gateway 

  
**Step 14** |  Enter  yes if you want to specify the IP address for the DNS server, or  no if you do not.   
**Step 15** |  (Optional) Enter the IPv4 or IPv6 address for the DNS server.  The address type must be the same as the address type of the management port of the fabric interconnect.   
**Step 16** |  Enter  yes if you want to specify the default domain name, or  no if you do not.   
**Step 17** |  (Optional) Enter the default domain name.   
**Step 18** |  Review the setup summary and enter  yes to save and apply the settings, or enter  no to go through the Setup wizard again to change some of the settings.  If you choose to go through the Setup wizard again, it provides the values you previously entered, and the values appear in brackets. To accept previously entered values, press Enter.   
  
* * *

##### Example

The following example sets up the first fabric interconnect for a cluster configuration using the console and IPv4 management addresses: 
    
    
    Enter the installation method (console/gui)?  **console**
    Enter the setup mode (restore from backup or initial setup) [restore/setup]? **setup**
    You have chosen to setup a new switch.  Continue? (y/n): **y**
    Enter the password for "admin": 
    Confirm the password for "admin": 
    Do you want to create a new cluster on this switch (select 'no' for standalone setup or if you want this switch to be added to an existing cluster)? (yes/no) [n]: **yes**
    Enter the switch fabric (A/B): **A**
    Enter the system name: **foo**
    Mgmt0 IPv4 address: **192.168.10.10**
    Mgmt0 IPv4 netmask: **255.255.255.0**
    IPv4 address of the default gateway: **192.168.10.1**
    Virtual IPv4 address: **192.168.10.12**
    Configure the DNS Server IPv4 address? (yes/no) [n]: **yes**
      DNS IPv4 address: **20.10.20.10**
    Configure the default domain name? (yes/no) [n]: **yes**
      Default domain name: **domainname.com**
    Join centralized management environment (UCS Central)? (yes/no) [n]: **no**
    Following configurations will be applied:
      Switch Fabric=A
      System Name=foo
      Management IP Address=192.168.10.10
      Management IP Netmask=255.255.255.0
      Default Gateway=192.168.10.1
      Cluster Enabled=yes  
      Virtual Ip Address=192.168.10.12
      DNS Server=20.10.20.10
      Domain Name=domainname.com
    Apply and save the configuration (select 'no' if you want to re-enter)? (yes/no): **yes**
    

The following example sets up the first fabric interconnect for a cluster configuration using the console and IPv6 management addresses: 
    
    
    Enter the installation method (console/gui)?  **console**
    Enter the setup mode (restore from backup or initial setup) [restore/setup]? **setup**
    You have chosen to setup a new switch.  Continue? (y/n): **y**
    Enter the password for "admin": 
    Confirm the password for "admin": 
    Do you want to create a new cluster on this switch (select 'no' for standalone setup or if you want this switch to be added to an existing cluster)? (yes/no) [n]: **yes**
    Enter the switch fabric (A/B): **A**
    Enter the system name: **foo**
    Mgmt0 address: **2001::107**
    Mgmt0 IPv6 prefix: **64**
    IPv6 address of the default gateway: **2001::1**
    Configure the DNS Server IPv6 address? (yes/no) [n]: **yes**
      DNS IP address: **2001::101**
    Configure the default domain name? (yes/no) [n]: **yes**
      Default domain name: **domainname.com**
    Join centralized management environment (UCS Central)? (yes/no) [n]: **no**
    Following configurations will be applied:
      Switch Fabric=A
      System Name=foo
      Enforced Strong Password=no
      Physical Switch Mgmt0 IPv6 Address=2001::107
      Physical Switch Mgmt0 IPv6 Prefix=64
      Default Gateway=2001::1
      Ipv6 value=1
      DNS Server=2001::101
      Domain Name=domainname.com
    Apply and save the configuration (select 'no' if you want to re-enter)? (yes/no): **yes**
    

#### Configure the Subordinate Fabric Interconnect Using CLI

This procedure describes setting up the second fabric interconnect using IPv4 or IPv6 addresses for the management port. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

When adding a new Fabric Interconnect to an existing High Availability cluster, for example, during a new install or when replacing a Fabric Interconnect, the new device will not be able to log into the cluster as long as the authentication method is set to remote. To successfully add a new Fabric Interconnect to the cluster, the authentication method must be temporarily set to local and the local admin credentials of the primary Fabric Interconnect must be used. 

* * *  
  
---|---  
  
##### Procedure

* * *

**Step 1** |  Connect to the console port.   
---|---  
**Step 2** |  Power up the fabric interconnect.  You will see the power-on self-test messages as the fabric interconnect boots.   
**Step 3** |  When the unconfigured system boots, it prompts you for the setup method to be used. Enter  console to continue the initial setup using the console CLI.  |  **Note** |  The fabric interconnect should detect the peer fabric interconnect in the cluster. If it does not, check the physical connections between the L1 and L2 ports, and verify that the peer fabric interconnect has been enabled for a cluster configuration.   
---|---  
**Step 4** |  Enter  y to add the subordinate fabric interconnect to the cluster.   
**Step 5** |  Enter the admin password of the peer fabric interconnect.   
**Step 6** |  Enter the IP address for the management port on the subordinate fabric interconnect.   
**Step 7** |  Review the setup summary and enter  yes to save and apply the settings, or enter  no to go through the Setup wizard again to change some of the settings.  If you choose to go through the Setup wizard again, it provides the values you previously entered, and the values appear in brackets. To accept previously entered values, press Enter.   
  
* * *

##### Example

The following example sets up the second fabric interconnect for a cluster configuration using the console and the IPv4 address of the peer: 
    
    
    Enter the installation method (console/gui)? **console**
    Installer has detected the presence of a peer Fabric interconnect. This Fabric interconnect will be added to the cluster. Continue (y/n) ? **y**
    Enter the admin password of the peer Fabric Interconnect: 
    Peer Fabric interconnect Mgmt0 IPv4 Address: **192.168.10.11**
    Apply and save the configuration (select 'no' if you want to re-enter)? (yes/no): **yes**
    

The following example sets up the second fabric interconnect for a cluster configuration using the console and the IPv6 address of the peer: 
    
    
    Enter the installation method (console/gui)? **console**
    Installer has detected the presence of a peer Fabric interconnect. This Fabric interconnect will be added to the cluster. Continue (y/n) ? **y**
    Enter the admin password of the peer Fabric Interconnect: 
    Peer Fabric interconnect Mgmt0 IPv6 Address: **2001::107**
    Apply and save the configuration (select 'no' if you want to re-enter)? (yes/no): **yes**
    

### Verify Console Setup 

You can verify that both fabric interconnect configurations are complete by logging into the fabric interconnect via SSH and verifying the cluster status through CLI. For this procedure, you can watch [Cisco UCS Manager Initial Setup part 3](http://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/videos/3-1/cisco_ucs_manager_initial_setup.html). 

Use the following commands to verify the cluster state:  Command  |  Purpose  |  Sample Output   
---|---|---  
show cluster state |  Displays the operational state and leadership role for both fabric interconnects in a high availability cluster.  |  The following example displays that both fabric interconnects are in the Up state, HA is in the Ready state, fabric interconnect A has the primary role, and fabric interconnect B has the subordinate role: 
    
    
    UCS-A# show cluster state 
    Cluster Id: 0x4432f72a371511de-0xb97c000de1b1ada4 
    
    A: UP, PRIMARY 
    B: UP,
    SUBORDINATE HA READY
      
  
show cluster extended-state |  Displays extended details about the cluster state and typically used when troubleshooting issues.  |  The following example shows how to view the extended state of a cluster: 
    
    
    UCSC# show cluster extended-state 0x2e95deacbd0f11e2-0x8ff35147e84f3de2Start time: Thu May 16 06:54:22 2013Last election time: Thu May 16 16:29:28 2015System Management
    Viewing the Cluster State
    A: UP, PRIMARY
    B: UP, SUBORDINATE
    
    A: memb state UP, lead state PRIMARY, mgmt services state: UP
    B: memb state UP, lead state SUBORDINATE, 
    mgmt services state: UP heartbeat state PRIMARY_OK 
    HA READY 
    Detailed state of the device selected for HA quorum data: 
    Device 1007, serial: a66b4c20-8692-11df-bd63-1b72ef3ac801, state: active 
    Device 1010, serial: 00e3e6d0-8693-11df-9e10-0f4428357744, state: active 
    Device 1012, serial: 1d8922c8-8693-11df-9133-89fa154e3fa1, state: active  
  
## Configure Administration Policies 

After completing initial configuration, configure global system administration settings such as faults, events, users, external directory services, communication services, and licensing. 

Use the following table for specific guidance on how to configure various administration policies. 

Task  |  See   
---|---  
Time Zone Management  |  Cisco UCS Manager Administration Management Guide  
Register with Cisco UCS Central  |  Cisco UCS Manager Infrastructure Management Guide  
User Management  |  Cisco UCS Manager Infrastructure Management Guide  
Communications Management  |  Cisco UCS Manager Administration Management Guide  
(Optional) Key Management  |  Cisco UCS Manager Administration Management Guide  
License Management  |  Cisco UCS Manager Administration Management Guide  
  
## Configure Equipment Policies 

After configuring administration policies, set equipment policies such as Chassis/FEX Discovery policy, Power Policy, MAC Address changing policy and SEL Policy. 

Use the following table for specific guidance on how to configure various equipment policies. 

Task  |  See   
---|---  
Configure global policies including Chassis/FEX Discovery Policy, Power Policy and Information Policy  |  Cisco UCS Manager Infrastructure Management Guide  
Configure SEL Policy  |  Cisco UCS Manager Administration Management Guide  
  
## Configure Unified Ports 

After configuring equipment policies, enable Unified Ports. It is recommended that you first configure Unified Ports on the Primary Fabric Interconnect, then on the Subordinate Fabric Interconnect. 

Use the following table for specific guidance on how to configure Unified ports. 

Task  |  See   
---|---  
Configure Unified Ports  |  Cisco UCS Network Management Guide  
  
## Configure Fabric Interconnect Server Ports 

After configuring Unified Ports, enable Fabric Interconnect Server Ports. 

Use the following table for specific guidance on how to configure fabric interconnect server ports. 

Task  |  See   
---|---  
Configure Fabric Interconnect Server Ports  |  **Note** |  Starting with Cisco UCS Manager release 3.1(3), you can automatically configure the fabric interconnect server ports.  
---|---  
Cisco UCS Manager Network Management Guide  
  
## Configure LAN Connectivity 

After configuring Fabric Interconnect Server Ports, complete initial LAN connectivity by enabling Fabric Interconnect Ethernet Ports. 

Use the following table for specific guidance on how to configure LAN connectivity. 

Task  |  See   
---|---  
Configure Fabric Interconnect Ethernet Ports  |  Cisco UCS Manager Network Management Guide  
  
## Configure SAN Connectivity 

After configuring LAN connectivity, complete initial SAN connectivity by enabling Fabric Interconnect FC Ports. 

Use the following table for specific guidance on how to configure SAN connectivity. 

Task  |  See   
---|---  
Configure Fabric Interconnect FC Ports  |  Cisco UCS Manager Storage Management Guide  
  
## Define Workloads 

After completing Cisco UCS Manager initial configuration, use the following steps in the recommended order to define your workload:  Step  |  Description  |  See   
---|---|---  
Define organizational hierarchy  |  Cisco UCS organizational structure facilitates hierarchical configuration of Cisco UCS resources. An Organization can be created for policies, pools, and service profiles. The default Organization for any resource category is Root. Based on requirements, multiple sub-organizations can be created under the Root organization. You can create nested sub-organization under a sub-organization.  |  Cisco UCS Manager Administration Management Guide  
Define Pools  |  Pools in Cisco UCS Manager are used for abstracting unique identities and resources for devices such as vNICs, vHBAs and server pools can assign servers in groups based on similar server characteristics.  |  Cisco UCS Manager Network Management Guide  
Configure Adapters  |  Cisco UCS contains predefined adapter policies for most operating systems, including hypervisors. The settings in these predefined policies are for optimal adapter performance.  |  Cisco UCS Manager Network Management Guide  
Configure Server Policies  |  Configuring Server Policies in Cisco UCS Manager includes Server-Related Policies such as BIOS Policy, Local Disk Configuration Policy, IPMI Access Profiles, and Server Autoconfiguration.  |  Cisco UCS Manager Server Management Guide  
Configure Service Profile Templates  |  Cisco UCS Service Profile Templates are used to create multiple services profiles with similar characteristics.  |  Cisco UCS Manager Server Management Guide

---

## Page 7: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Getting-Started/4-3/b_ucsm_getting_started_guide_4_3/m_appendix.html

# Appendix  
  
## Recommendations and Best Practices 

  * Pools
  * Policies
  * Templates
  * Monitoring
  * Network Availability
  * Best Practices for Installing ESXi 5.5 U2 Custom ISO to FlexFlash
  * Configuration Backup


### Pools

Pools are the base building blocks for uniquely identifying hardware resources. As the basis for the UCS management model, they allow Service Profiles to be associated with any blade, while still providing the exact same ID and presentation to the upstream LAN or SAN. There are three sets of pools used as part of best practices: 

  * WWNN and WWPN pools: Provide unique IDs for Fibre Channel resources on a server (Fibre Channel nodes and ports). 

  * MAC address pools: Provide unique IDs for network interface ports. 

  * UUID pools: Provide IDs similar to a serial number or service tag. 


In the Cisco UCS Manager GUI, these pools are all functionally organized, with UUID pools maintained from the Server tab, WWNN and WWPN pools maintained from the SAN tab, and MAC address pools maintained from the LAN tab. 

Define and use Pools as a standard practice. Ensure the following: 

  * UUID pools are referenced when you create Service Profiles. 

  * MAC address pools are referenced when you create vNICs. 

  * WWNN pools are referenced when you create Service Profiles. 

  * WWPN pools are referenced when you create vHBAs. 


Similarly, Pools should also be referenced when you create any corresponding template objects (vNICs, vHBAs, and Service Profiles). Trade-offs exist when considering pool management. There are two simple ways to manage pools: populate and use the default pools, or create domain-wide pools. This approach reduces the number of objects that need to be configured and managed. Alternatively, operators are free to configure different pools on a per-tenant or per-application basis. This approach can provide more specific identity management and more granular traffic monitoring of tenants, applications. 

### Policies

Policies are a primary mechanism for enforcing rules, which helps ensure consistency and repeatability. Defining and using a comprehensive set of policies enables greater consistency, control, predictability and automation. The following sections contain various policy-related best practices. 

  * Boot Policies
  * Host Firmware Policies
  * Maintenance Policies
  * Local Disk Policies
  * Scrub Policies
  * BIOS Policies


#### Boot Policies 

Boot Policy determines how a server boots, specifying the boot devices, the method, and the boot order. 

The traditional use of SAN boot requires manual configuration for each server performing SAN boot. Typically, having 100 servers SAN-boot would require configuring 100 servers manually and individually. Cisco UCS inverts this unwieldy model, and instead requires configuring only in proportion to the number of storage arrays serving SAN-boot images, regardless of the number of servers doing SAN-boot. A single boot policy, with the WWPNs of a single storage array can be referenced and reused by any number of servers, without additional manual configuration. 

Much of the Cisco UCS core value around availability is predicated on SAN boot. Therefore, the use of SAN boot within a Boot policy is a most highly recommended best practice to improve service availability. 

Refer to the following best practices for boot policies: 

  * Have a CD-ROM as the first in the boot order, for emergencies and for booting in recovery mode. 

  * For SAN boot, define separate boot policies for each storage array that would be serving boot LUNs. 

  * For network boot, define the vNIC device as last in the boot order, following either SAN or local boot. This allows you to perform a network boot and installation, only if the OS was not previously been installed. 


#### Host Firmware Policies 

Use Host Firmware Policy to associate qualified or well-known versions of the BIOS, adapter ROM, or local disk controller with logical Service Profiles, as described earlier. A best practice is to create one policy, based on the latest packages that correspond with the Cisco UCS Manager infrastructure and server software release, and to reference that Host Firmware Package for all Service Profiles and templates created. This best practice will help ensure version consistency of a server's lowest-level firmware, regardless of physical server failures that may cause re-association of Service Profiles on other blades. 

#### Maintenance Policies 

Use the Maintenance Policy to specify how Cisco UCS Manager should proceed for configuration changes that will have a service impact or require a server reboot. Values for the Maintenance Policy can be "immediate," "userack," or "timer automatic". The best practice is to not use the "default" policy, and instead to create and use Maintenance Policies for either "user-ack" or "timer automatic", and to always have these as elements of the Service Profile or Service Profile Template definition. 

#### Local Disk Policies 

Local disk policy specifies how to configure any local disks on the blade. A best practice is to specify no local storage for SAN boot environments, thereby precluding any problems at Service Profile association time, when local disks may present themselves to the host OS during installation. You can also remove or unseat local disks from blades completely, especially blades used for OS installation. 

#### Scrub Policies 

Scrub policy determines what happens to local disks and BIOS upon Service Profile disassociation. The default policy is no scrubbing. A best practice is to set the policy to scrub the local disk, especially for service providers, multi-tenant customers, and environments in which network installation to a local disk is used. 

#### BIOS Policies 

BIOS policy enables very specific control of CPU settings that are normally accessible only through the console during startup. For VMware and virtual environments that depend on CPU support for Intel Virtualization Technology, a corresponding policy can be created, removing any requirement for manual intervention during server provisioning. Similarly, applications that are sensitive to Intel Turbo Boost or Hyper-Threading can have dedicated BIOS policies referenced. Also, setting "Quiet Boot" to "disabled" allows diagnostic message visibility, which may be helpful in troubleshooting situations. 

### Templates

Refer to the following best practices for templates: 

  * In the Cisco UCS Manager GUI, use expert mode when creating Service Profile templates to achieve the optimal level of control and definition. 

  * When creating templates, reference the subordinate Pools and Policies that have been previously defined. 


#### vNIC and vHBA Templates 

Create reusable vNIC and vHBA templates in which termination is either reflected in the name (e.g., "fc0-A") or through well-accepted conventions (e.g., an even interface to A side, and an odd interface to B side). vNIC templates should be thought of as application-specific network profiles that include important security definitions, such as VLAN mappings. 

#### Service Profile Templates 

Use a Service Profile template as a definition for a class or type or version of an application, service, or operating system. 

### Monitoring

Cisco UCS provides the standard set of health and monitoring methods, such as syslog and Simple Network Management Protocol (SNMP) with its associated MIBs8 (get and fault traps only; no set). The best practice for Cisco UCS monitoring is to use existing methods and frameworks that are already familiar and well understood, such as SCOM, OpenView, or BPPM. 

### Network Availability 

For network availability, either use hardware failover or use NIC teaming (or bonding), but do not use both concurrently. After a vNIC and vHBA template is defined, it can be referenced through expert-mode service-profile creation by selecting Use LAN (or SAN) Connectivity Template. 

### Best Practices for Installing ESXi 5.5 U2 Custom ISO to FlexFlash 

Before installing the ESXi 5.5 U2 custom ISO to FlexFlash, scrub the FlexFlash drives to avoid any ISO installation issues. 

### Configuration Backup 

The Cisco UCS configuration can be backed up easily and should be backed up regularly through the GUI or automated scripts. There are four types of backups:  Type  |  Description   
---|---  
Full State  |  Used for full system restore as part of disaster recovery.   
System Configuration  |  Roles, Call Home, communication services and distributed virtual switch.   
Logical Configuration  |  Service profiles, VLANs, VSANs, pools, policies and templates   
All Configurations  |  Both Logical and System configurations   
For the Logical Configuration and All Configurations backups, select the Cisco UCS Manager Preserve Identities feature to preserve the actual MAC address, WWN, and UUID values; otherwise, the backup references only the logical pool names, but not the actual identities. The following are configuration backup related best practices: 

  * Use the Preserve Identities feature when backing up individual domains for prescribed restoration (same site or domain or exact recovery site or domain). 

  * Do not use Preserve Identities when creating "gold UCSM domain configuration" templates. 


## Configuration Examples 

Refer to [Configuration Examples and TechNotes](http://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-configuration-examples-list.html) for Cisco UCS Manager configuration examples. 

## Glossary

AD 
    

Active Directory. A distributed directory service. 

adapter port channel 
    

A channel that groups all the physical links from a Cisco UCS Virtual Interface Card (VIC) to an IOM into one logical link. 

BIOS 
    

Basic Input Output System. In a computer system, it performs the power up self-test procedure, searches, and loads to the Master Boot Record in the system booting process. 

DNS 
    

Domain Name System. An application layer protocol used throughout the Internet for translating hostnames into their associated IP addresses. 

Dynamic FCoE 
    

The ability to overlay FCoE traffic across Spine-Leaf data center switching architecture. In its first instantiation, Dynamic FCoE allows running FCoE on top of Cisco FabricPath network in a converged fashion. 

Ethernet Port 
    

A generic term for the opening on the side of any Ethernet node, typically in an Ethernet NIC or LAN switch, into which an Ethernet cable can be connected. 

Fabric port channel 
    

Fibre Channel uplinks defined in a Cisco UCS Fabric Interconnect, bundled together and configured as a port channel, allowing increased bandwidth and redundancy. 

FCoE 
    

Fibre Channel over Ethernet. A computer network technology that encapsulates Fibre Channel frames over Ethernet networks. This allows Fibre Channel to use 10 Gigabit Ethernet networks (or higher speeds) while preserving the Fibre Channel protocol characteristics. The specification is part of the International Committee for Information Technology Standards T11 FC-BB-5 standard published in 2009. FCoE maps Fibre Channel directly over Ethernet while being independent of the Ethernet forwarding scheme. 

Hypervisor 
    

A software allowing multiple operating systems, known as guest operating systems, to share a single physical server. Guest operating systems run inside virtual machines and have fair scheduled access to underlying server physical resources. 

IP address (IP version 4) 
    

IP version 4 (IPv4), a 32-bit address assigned to hosts using TCP/IP. Each address consists of a network number, an optional subnetwork number, and a host number. The network and subnetwork numbers together are used for routing, and the host number is used to address an individual host within the network or subnetwork. 

IP address (IP version 6) 
    

In IP version 6 (IPv6), a 128-bit address assigned to hosts using TCP/IP. Addresses use different formats, commonly using a routing prefix, subnet, and interface ID, corresponding to the IPv4 network, subnet, and host parts of an address. 

KVM 
    

Keyboard, video, and mouse 

LAN 
    

Logical Area Network. A computer network that interconnects computers within a limited area, such as a home, school, computer laboratory, or office building, using network media. The defining characteristics of LANs, in contrast to Wide-Area Networks (WANs), include their smaller geographic area and non-inclusion of leased telecommunication lines. 

Logical unit number 
    

Logical unit number. In computer storage, a number used to identify a logical unit, which is a device addressed by the SCSI protocol or protocols that encapsulate SCSI, such as Fibre Channel or iSCSI. A LUN may be used with any device that supports read/write operations, such as a tape drive, but is most often used to refer to a logical disk as created on a SAN. 

MAC address 
    

A standardized data link layer address that is required for every device that connects to a LAN. Ethernet MAC addresses are 6 bytes long and are controlled by the IEEE. 

out-of-band 
    

A storage virtualization method that provides separate paths for data and control, presenting an image of virtual storage to the host by one link and allowing the host to directly retrieve data blocks from physical storage on another. 

---

## Page 8: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Getting-Started/4-3/m_overview.html

# Overview

## Cisco UCS Manager User Documentation 

Cisco UCS Manager offers you a new set of smaller, use-case based documentation described in the following table: 

Guide  |  Description   
---|---  
[Cisco UCS Manager Getting Started Guide ](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses Cisco UCS architecture and Day 0 operations, including Cisco UCS Manager initial configuration and configuration best practices.   
[Cisco UCS Manager Administration Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses password management, role-based access configuration, remote authentication, communication services, CIMC session management, organizations, backup and restore, scheduling options, BIOS tokens, and deferred deployments.   
[Cisco UCS Manager Infrastructure Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses physical and virtual infrastructure components used and managed by Cisco UCS Manager.   
[Cisco UCS Manager Firmware Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses downloading and managing firmware, upgrading through Auto Install, upgrading through service profiles, directly upgrading at endpoints using firmware auto sync, managing the capability catalog, deployment scenarios, and troubleshooting.   
[Cisco UCS Manager Server Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses the new licenses, registering Cisco UCS domain with Cisco UCS Central, power capping, server boot, server profiles, and server-related policies.   
[Cisco UCS Manager Storage Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses all aspects of storage management, such as SAN and VSAN in Cisco UCS Manager.   
[Cisco UCS Manager Network Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses all aspects of network management, such as LAN and VLAN connectivity in Cisco UCS Manager.   
[Cisco UCS Manager System Monitoring Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses all aspects of system and health monitoring, including system statistics in Cisco UCS Manager.   
  
## Fundamentals of Cisco Unified Computing System 

  * Cisco Unified Computing System Overview
  * IOMs and Fabric Interconnects Connectivity
  * Unified Fabric
  * Cisco UCS Building Blocks and Connectivity
  * Introduction to Cisco UCS Manager


### Cisco Unified Computing System Overview 

Cisco UCS has a unique architecture that integrates compute, data network access, and storage network access into a common set of components under a single-pane-of-glass management interface. 

Cisco UCS fuses access layer networking and servers. This high-performance, next-generation server system provides a data center with a high degree of workload agility and scalability. The hardware and software components support Cisco's unified fabric, which runs multiple types of data center traffic over a single converged network adapter. 

Figure 1. Cisco Unified Computing System Architecture  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/305001-306000/305219.jpg)

#### Architectural Simplification

The simplified architecture of Cisco UCS reduces the number of required devices and centralizes switching resources. By eliminating switching inside a chassis, network access-layer fragmentation is significantly reduced. Cisco UCS implements Cisco unified fabric within racks and groups of racks, supporting Ethernet and Fibre Channel protocols over 10/25/40 Gigabit Cisco Data Center Ethernet and Fibre Channel over Ethernet (FCoE) links. This radical simplification reduces the number of switches, cables, adapters, and management points by up to two-thirds. All devices in a Cisco UCS domain remain under a single management domain, which remains highly available through the use of redundant components. 

#### High Availability

The management and data plane of Cisco UCS is designed for high availability and redundant access layer fabric interconnects. In addition, Cisco UCS supports existing high availability and disaster recovery solutions for the data center, such as data replication and application-level clustering technologies. 

#### Scalability

A single Cisco UCS domain supports multiple chassis and their servers, all of which are administered through one Cisco UCS Manager. For more detailed information about the scalability, speak to your Cisco representative. 

#### Flexibility

A Cisco UCS domain allows you to quickly align computing resources in the data center with rapidly changing business requirements. This built-in flexibility is determined by whether you choose to fully implement the stateless computing feature. Pools of servers and other system resources can be applied as necessary to respond to workload fluctuations, support new applications, scale existing software and business services, and accommodate both scheduled and unscheduled downtime. Server identity can be abstracted into a mobile service profile that can be moved from server to server with minimal downtime and no need for additional network configuration. 

With this level of flexibility, you can quickly and easily scale server capacity without having to change the server identity or reconfigure the server, LAN, or SAN. During a maintenance window, you can quickly do the following: 

  * Deploy new servers to meet unexpected workload demand and rebalance resources and traffic. 

  * Shut down an application, such as a database management system, on one server and then boot it up again on another server with increased I/O capacity and memory resources. 


#### Optimized for Server Virtualization

Cisco UCS has been optimized to implement VM-FEX technology. This technology provides improved support for server virtualization, including better policy-based configuration and security, conformance with a company's operational model, and accommodation for VMware's VMotion. 

### IOMs and Fabric Interconnects Connectivity

Each chassis is equipped with two IOMs: IOM 1 should be connected to Fabric Interconnect A. IOM 2 should be connected to Fabric Interconnect B. This configuration provides redundant paths, ensuring uninterrupted operation of the Cisco UCS system even in the event of a failure in one of the Fabric Interconnects or IOMs. Additionally, this configuration enables traffic load distribution across both Fabric Interconnects, enhancing load balancing and increasing throughput. As a result, the Cisco UCS system achieves high availability, reliability, and optimal performance, making it ideal for data center environments. 

  * Uplink Connectivity
  * Downlink Connectivity


#### Uplink Connectivity 

Use fabric interconnect ports configured as uplink ports to connect to uplink upstream network switches. Connect these uplink ports to upstream switch ports as individual links, or as links configured as port channels. Port channel configurations provide bandwidth aggregation as well as link redundancy. 

You can achieve northbound connectivity from the fabric interconnect through a standard uplink, a port channel, or a virtual port channel configuration. The port channel name and ID configured on fabric interconnect should match the name and ID configuration on the upstream Ethernet switch. 

It is also possible to configure a port channel as a vPC, where port channel uplink ports from a fabric interconnect are connected to different upstream switches. After all uplink ports are configured, create a port channel for these ports. 

#### Downlink Connectivity 

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
  
### Unified Fabric 

With unified fabric, multiple types of data center traffic can run over a single Data Center Ethernet (DCE) network. Instead of having a series of different host bus adapters (HBAs) and network interface cards (NICs) present in a server, unified fabric uses a single converged network adapter. This type of adapter can carry LAN and SAN traffic on the same cable. 

Cisco UCS uses Fibre Channel over Ethernet (FCoE) to carry Fibre Channel and Ethernet traffic on the same physical Ethernet connection between the fabric interconnect and the server. This connection terminates at a converged network adapter on the server, and the unified fabric terminates on the uplink ports of the fabric interconnect. On the core network, the LAN and SAN traffic remains separated. Cisco UCS does not require that you implement unified fabric across the data center. 

The converged network adapter presents an Ethernet interface and Fibre Channel interface to the operating system. At the server, the operating system is not aware of the FCoE encapsulation because it sees a standard Fibre Channel HBA. 

At the fabric interconnect, the server-facing Ethernet port receives the Ethernet and Fibre Channel traffic. The fabric interconnect (using Ethertype to differentiate the frames) separates the two traffic types. Ethernet frames and Fibre Channel frames are switched to their respective uplink interfaces. 

  * Fibre Channel over Ethernet


#### Fibre Channel over Ethernet 

Cisco UCS leverages Fibre Channel over Ethernet (FCoE) standard protocol to deliver Fibre Channel. The upper Fibre Channel layers are unchanged, so the Fibre Channel operational model is maintained. FCoE network management and configuration is similar to a native Fibre Channel network. 

FCoE encapsulates Fibre Channel traffic over a physical Ethernet link. FCoE is encapsulated over Ethernet with the use of a dedicated Ethertype, 0x8906, so that FCoE traffic and standard Ethernet traffic can be carried on the same link. FCoE has been standardized by the ANSI T11 Standards Committee. 

Fibre Channel traffic requires a lossless transport layer. Instead of the buffer-to-buffer credit system used by native Fibre Channel, FCoE depends upon the Ethernet link to implement lossless service. 

Ethernet links on the fabric interconnect provide two mechanisms to ensure lossless transport for FCoE traffic: 

  * Link-level flow control 

  * Priority flow control 


  * Link-Level Flow Control
  * Priority Flow Control


##### Link-Level Flow Control

IEEE 802.3x link-level flow control allows a congested receiver to signal the endpoint to pause data transmission for a short time. This link-level flow control pauses all traffic on the link. 

The transmit and receive directions are separately configurable. By default, link-level flow control is disabled for both directions. 

On each Ethernet interface, the fabric interconnect can enable either priority flow control or link-level flow control (but not both). 

When an interface on a Cisco UCS Fabric Interconnects 9108 100G, Cisco UCS 6500 Series Fabric Interconnect,  or Cisco UCS 6400 Series Fabric Interconnect has Priority Flow Control (PFC) admin configured as auto and Link-Level Flow Control (LLFC) admin configured as on, the PFC operation mode will be off and the LLFC operation mode will be on. On UCS 6300 Series and earlier Fabric Interconnects, the same configuration will result in the PFC operation mode being on and the LLFC operation mode being off. 

##### Priority Flow Control

The priority flow control (PFC) feature applies pause functionality to specific classes of traffic on the Ethernet link. For example, PFC can provide lossless service for the FCoE traffic, and best-effort service for the standard Ethernet traffic. PFC can provide different levels of service to specific classes of Ethernet traffic (using IEEE 802.1p traffic classes). 

PFC decides whether to apply pause based on the IEEE 802.1p CoS value. When the fabric interconnect enables PFC, it configures the connected adapter to apply the pause functionality to packets with specific CoS values. 

By default, the fabric interconnect negotiates to enable the PFC capability. If the negotiation succeeds, PFC is enabled and link-level flow control remains disabled (regardless of its configuration settings). If the PFC negotiation fails, you can either force PFC to be enabled on the interface or you can enable IEEE 802.x link-level flow control. 

### Cisco UCS Building Blocks and Connectivity

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


#### Cisco UCS Fabric Infrastructure Portfolio

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
  
Cisco UCS Manager Fabric Interconnects

Cisco UCS X-Series Direct

#### Overview of Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct) 

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

#### Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct) Architecture 

The Cisco UCS X-Series Direct architecture is engineered to support a diverse range of workloads, from traditional applications to cloud-native services, by offering a composable and disaggregated approach to computing resources. Key components of the Cisco UCS X-Series Direct architecture include: 

  * **Cisco UCSX-9508 Chassis** —A modular and future-proof chassis that can accommodate various types of compute nodes, providing the flexibility to adapt to different workload requirements without the need for a complete hardware overhaul. 

  * **Cisco UCS Fabric Interconnects 9108 100G** —This solution is centered around a single-chassis system, the Cisco UCS X9508 Chassis, which incorporates Cisco UCS Fabric Interconnects 9108 100G directly into the chassis for a consolidated and efficient infrastructure. To ensure high availability, each chassis houses two Cisco UCS Fabric Interconnects 9108 100G that establish direct downlink connections to servers and provide uplink connections to facilitate seamless integration with both Local Area Network (LAN) and Storage Area Network (SAN) systems. 

  * **Software Architecture** —In terms of the startup and operational model, the management, Cisco UCS Manager aligns with the approach taken in the Cisco UCS 6500 and 6400 Series Fabric Interconnects. In this model, Cisco UCS Manager is encapsulated within a container and is initiated by the underlying NX-OS, depending on the selected management mode. 


#### Port Breakout Functionality on Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct) 

The Cisco UCS Fabric Interconnects 9108 100G is equipped with advanced port breakout functionality, which allows network administrators to subdivide a single high-bandwidth port into multiple lower-bandwidth ports. This feature is particularly beneficial for optimizing port utilization, managing cabling complexity, and adapting to various bandwidth requirements. 

Physical Port |  Breakout Options |  Logical Ports After Breakout |  Supported Speeds through breakout cables  
---|---|---|---  
Ethernet 1/1 - Ethernet 1/8 |  4x25G |  Ethernet 1/1/1 to Ethernet 1/8/4 |  Up to 8x100 Gbps  
Fibre Channel 1/1 and 1/2 |  4x8G, 4x16G, 4x32G |  Fibre Channel 1/1/1 to Fibre Channel 1/2/4 |  Up to 8x32Gbps  
  
##### Breakout Port Guidelines

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

#### **Cisco UCS 6536 Fabric Interconnect**

The Cisco UCS 6536 Fabric Interconnect (UCSC-FI-6536) is a One-rack unit (1RU), top of rack (TOR), fixed-port data center platform that provides both network connectivity and management capabilities to the Cisco UCS system. 

The fabric interconnect can provide Ethernet and Fibre Channel connectivity to the servers in the system. The servers connect to the fabric interconnect, and then to the LAN or SAN. 

Cisco UCS Manager on UCS 6536 Fabric Interconnect supports Cisco UCS X-Series Compute Nodes, B-Series Blade Servers and C-Series Rack Servers, Cisco UCS S-Series Storage Servers, as well as the associated storage resources and networks. 

High availability and redundancy can be achieved by connecting a pair of fabric interconnects to each other through L1 or L2 ports in cluster mode configuration. 

Each Cisco UCS 6536 Fabric Interconnect offers the following features: 

  * Thirty-six QSFP28 ports capable of 100G including 4 unified ports (33-36). Ports also support: 

  * Autonegotiating with peer devices to speeds of 100G, 40G, 25G, 10G, and 1G.

  * Port breakout is supported for Ethernet ports (1-32) and Unified ports (33-36). 

  * Ethernet breakout is supported on switch ports 1 through 36 when each port is configured with a breakout cable. 

  * The Dynamic Ethernet Breakout feature enables converting a standard Ethernet port to a breakout port on-the-fly so that you do not need to reboot the Fabric Interconnect. Dynamic Ethernet Breakout also supports converting breakout ports back to a standard Ethernet port without a reboot. 

  * FC breakout is supported on ports 33 through 36 wherein each port is configured with a four-port breakout cable. For example 1/33/1, 1/33/2, 1/33/3, and 1/33/4 are the four FC breakout ports on the physical port 33. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Fibre Channel support is only available through the configuration of Unified Ports (33-36) as FC breakout port.

* * *  
  
---|---  
  * FC breakout ports support peer communication at fixed speeds of 8Gbs, 16 Gbps, and 32 Gbps. 

  * All four FC breakout ports must be configured with the same speed. Mixed speeds on a QSFP port's FC breakout ports are not supported. 

  * Using breakout ports enables the fabric interconnect to support the maximum 16 FC ports supported by Fibre Channel.

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

  * Converting from Ethernet to FC breakout ports, or FC breakout ports back to Ethernet, requires a reboot/reload after changing the breakout type. 
  * FCoE storage ports are not supported. 

* * *  
  
---|---  
  * One management port (one 10/100/1000BASE-T port)

  * Two L1/L2 Ethernet RJ-45 ports for high availability or cluster configurations. Ethernet ports support 10/100/1000Mb speed.

  * One console port (RS-232)

  * One USB 3.0 port

  * CPU: 4 Core, 1.8GHz, Intel 5th-Generation core processor

  * Memory: 

  * 32 GB DDR4 DIMMs

  * 128 GB M.2 SSD Flash Drive

  * 32 GB Boot Flash (16 MB primary, and 16 MB standby/golden)


This fabric interconnect includes the following user-replaceable components:

  * Fan modules (6), each is a port-side exhaust fan module with dark grey latch coloring (UCS-FAN-6536).

  * Power supply modules (2). One power supply module (PSU) is the active module for operations, and the second PSU is the standby for redundancy [1+1]) with the following choices: 

  * 1100-W AC power supply with dark grey latch coloring (UCS-PSU-6536-AC)

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

All fan modules and power supplies must use the same airflow direction.

* * *  
  
---|---  


The following figure shows the fabric interconnect features on the port side of the chassis. 

![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540351.jpg) 1  |  LEDs  |  3  |  36 40/100-Gigabit QSFP28 ports  
---|---|---|---  
2  |  Lane Select button  |  |   
  
To determine which transceivers, adapters, and cables are support the fabric interconnect, see the [Cisco Transceiver Modules Compatibility Information](http://www.cisco.com/c/en/us/support/interfaces-modules/transceiver-modules/products-device-support-tables-list.html) document. 

The following figure shows the fabric interconnect features on the power supply side of the chassis. 

![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540354.jpg) 1  |  Power supply modules (1 or 2) (AC power supplies shown) with slots numbered 1 (left) and 2 (right). |  2  |  Fan modules (6) with slots numbered from 1 (left) to 6 (right).  
---|---|---|---  
3  |  Layer 2 (L2) Ethernet port, 10/100/100Mb autonegotiating. Supports high availability (HA) or clustering through an RJ-45 port. |  4  |  Layer 1 (L1) Ethernet port, 10/100/100Mb autonegotiating.  Supports high availability (HA) or clustering through an RJ-45 port.  
5 |  Ethernet network management port (RJ45), 10/100/1000Mb autonegotiating  |  6  |  Serial Console port (RJ45), 9600 baud.  
7 |  USB 3.0/2.0 port Supports booting the system and downloading scripts. |  8 |  Beacon (BCN) LED  
9 |  Status (STS) LED |  - |   
  
The following figure shows the side of the chassis. 

![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540353.jpg) 1  |  Screw holes for mounting brackets |  2  |  Grounding pad  
---|---|---|---  
  
Plan to position the ports in a hot aisle so that fans and power supplies intake air from the cold aisle, blow the cool air through the fabric interconnect, and exhaust the heated air into the hot aisle. 

The fan and power supply modules are field replaceable. You can replace one fan module or one power supply module during operations so long as the other modules are installed and operating. If you have only one power supply installed, you can install the replacement power supply in the open slot before removing the original power supply. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

All fan and power supply modules must have the same direction of airflow. Otherwise, the fabric interconnect can overheat and shut down. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Because fans and power supply modules have port-side exhaust airflow (blue coloring for fan modules), you must locate the ports in the hot aisle. If you locate the air intake in a hot aisle, the fabric interconnect can overheat and shut down. 

* * *  
  
---|---  
  
#### Port Breakout Functionality on Cisco UCS 6536 Fabric Interconnects

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
  
##### Breakout Port Guidelines

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

#### Cisco UCS 6400 Series Fabric Interconnect Overview 

Cisco UCS 6400 Series Fabric Interconnect provides both network connectivity and management capabilities to the Cisco UCS system. The fabric interconnect provides Ethernet and Fibre Channel to the servers in the system, the servers connect to the fabric interconnect, and then to the LAN or SAN. 

Each Cisco UCS 6400 Series Fabric Interconnect runs Cisco UCS Manager to fully manage all Cisco UCS elements. The fabric interconnect supports 10/25 Gigabit ports in the fabric with 40/100 Gigabit uplink ports. High availability can be achieved when a Cisco UCS 6400 Series Fabric Interconnect is connected to another Cisco UCS 6400 Series Fabric Interconnect through the L1 or L2 port on each device. 

Cisco UCS 6400 Series Fabric Interconnect consists of: 

  * Cisco UCS 6454 Fabric Interconnects 

  * Cisco UCS 64108 Fabric Interconnects 


The Cisco UCS 6400 Series fabric interconnect supports Cisco UCS B-Series Blade Servers, UCS 5108 B-Series Server Chassis, C-Series Rack Servers, and UCS S-Series Storage Servers. 

#### Cisco UCS 64108 Fabric Interconnect

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
  
#### Port Breakout Functionality on Cisco UCS 64108 Fabric Interconnects

##### About Breakout Ports

Cisco UCS 64108 fabric interconnects support splitting a single 40/100G QSFP port into four 10/25G ports using a supported breakout cable. On the UCS 64108 fabric interconnect, by default, there are 12 ports in the 40/100G mode. These are ports 97 to 108. These 40/100G ports are numbered in a 2-tuple naming convention. For example, the second 40G port is numbered as 1/99. The process of changing the configuration from 40G to 10 G, or from 100G to 25G is called breakout, and the process of changing the configuration from [4X]10G to 40G or from [4X]25G to 100G is called unconfigure. These ports can be used as uplink port, appliance port, server port (using FEX), and FCoE storage port. 

When you break out a 40G port into 10G ports or a 100G port into 25G ports, the resulting ports are numbered using a 3-tuple naming convention. For example, the breakout ports of the second 40-Gigabit Ethernet port are numbered as 1/99/1, 1/99/2, 1/99/3, 1/99/4. 

Starting with Cisco UCS Manager Release 4.2(3b), configuring the Ethernet breakout ports will not lead to Fabric Interconnect reboot. 

The following image shows the rear view of the Cisco UCS 64108 fabric interconnect, and includes the ports that support breakout port functionality: 

Figure 7. Cisco UCS 64108 Fabric Interconnect Rear View ![](/c/dam/en/us/td/i/300001-400000/300001-310000/307001-308000/307644.jpg) 1  |  Ports 1-16. Unified Ports can operate as 10/25 Gbps Ethernet or 8/16/32 Gbps Fibre Channel. FC ports are converted in groups of four.  Unified ports:

  * 10/25 Gbps Ethernet or FCoE
  * 8/16/32 Gbps Fibre Channel

|  2  |  Ports 1-96. Each port can operate as either a 10 Gbps or 25 Gbps Ethernet or FCoE SFP28 port.   
---|---|---|---  
3  |  Uplink Ports 97-108. Each port can operate as either a 40 Gbps or 100 Gbps Ethernet or FCoE port. When using a breakout cable, each of these ports can operate as 4 x 10 Gbps or 4 x 25 Gbps Ethernet or FCoE ports.  Ports 97 - 108 can be used to connect to Ethernet or FCoE uplink ports, and not to UCS server ports. |  4 |  Ports 89-96

  * 10/25 Gbps Ethernet or FCoE
  * 1 Gbps Ethernet

  
5 |  System environment (fan fault) LED |  6 |  System status LED  
7 |  Beacon LED |  |   
  
##### Breakout Port Guidelines

The following are the guidelines for breakout functionality for Cisco UCS 64108 fabric interconnects: 

  * The breakout configurable ports are ports 97-108.

  * You cannot configure the speed for each breakout port. Each breakout port is in auto mode.

  * Breakout ports are not supported as destinations for traffic monitoring.

  * Ports 97-108 at 40/100G can be configured as uplink, FCoE, or appliance port. Ports 97-108 after breakout to 10/25G can be configured as uplink, appliance, FCoE, or for direct-connect rack server connectivity. 


#### Cisco UCS 6454 Fabric Interconnect

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


Figure 8. Cisco UCS 6454 Fabric Interconnect Rear View ![](/c/dam/en/us/td/i/300001-400000/300001-310000/306001-307000/306755.jpg) 1  |  Ports 1-16 (Unified Ports 10/25 Gbps Ethernet or FCoE or 8/16/32 Gbps Fibre Channel) |  **Note** |  When using Cisco UCS Manager releases earlier than 4.0(4), only ports 1-8 are Unified Ports.  
---|---  
2  |  Ports 17-44 (10/25 Gbps Ethernet or FCoE) |  **Note** |  When using Cisco UCS Manager releases earlier than 4.0(4), ports 9-44 are 10/25 Gbps Ethernet or FCoE.  
---|---  
3  |  Ports 45-48 (1/10/25 Gbps Ethernet or FCoE)  |  4 |  Uplink Ports 49-54 (40/100 Gbps Ethernet or FCoE) Each of these ports can be 4 x 10/25 Gbps Ethernet or FCoE uplink ports when using an appropriate breakout cable.  
  
The Cisco UCS 6454 Fabric Interconnect chassis has two power supplies and four fans. Two of the fans provide front to rear airflow. 

Figure 9. Cisco UCS 6454 Fabric Interconnect Front View ![](/c/dam/en/us/td/i/300001-400000/300001-310000/306001-307000/306354.jpg) **1** |  Power supply and power cord connector  |  **2** |  Fans 1 through 4, numbered left to right, when facing the front of the chassis.  
---|---|---|---  
**3** |  L1 port, L2 port, RJ45, console, USB port, and LEDs |  |   
  
#### Port Breakout Functionality on Cisco UCS 6454 Fabric Interconnects

##### About Breakout Ports

Cisco UCS 6454 fabric interconnects support splitting a single 40/100G QSFP port into four 10/25G ports using a supported breakout cable. These ports can be used only as uplink ports connecting to a 10/25G switch. On the UCS 6454 fabric interconnect, by default, there are 6 ports in the 40/100G mode. These are ports 49 to 54. These 40/100G ports are numbered in a 2-tuple naming convention. For example, the second 40G port is numbered as 1/50. The process of changing the configuration from 40G to 10 G, or from 100G to 25G is called breakout, and the process of changing the configuration from [4X]10G to 40G or from [4X]25G to 100G is called unconfigure. 

When you break out a 40G port into 10G ports or a 100G port into 25G ports, the resulting ports are numbered using a 3-tuple naming convention. For example, the breakout ports of the second 40-Gigabit Ethernet port are numbered as 1/50/1, 1/50/2, 1/50/3, 1/50/4. 

Starting with Cisco UCS Manager Release 4.2(3b), Ethernet breakout ports configuration will not lead to Fabric Interconnect reboot. 

The following image shows the rear view of the Cisco UCS 6454 fabric interconnect, and includes the ports that support breakout port functionality: 

Figure 10. Cisco UCS 6454 Fabric Interconnect Rear View ![](/c/dam/en/us/td/i/300001-400000/300001-310000/306001-307000/306755.jpg) 1  |  Ports 1-16 (Unified Ports 10/25 Gbps Ethernet or FCoE or 8/16/32 Gbps Fibre Channel) |  2  |  Ports 17-44 (10/25 Gbps Ethernet or FCoE)  
---|---|---|---  
3  |  Ports 45-48 (1/10/25 Gbps Ethernet or FCoE)  |  4 |  Uplink Ports 49-54 (40/100 Gbps Ethernet or FCoE)   
  
##### Breakout Port Guidelines

The following are the guidelines for breakout functionality for Cisco UCS 6454 fabric interconnects: 

  * The breakout configurable ports are ports 49-54.

  * You cannot configure the speed for each breakout port. Each breakout port is in auto mode.

  * In Cisco UCS Manager Release 4.0(2), breakout ports are not supported as destinations for traffic monitoring.

  * Ports 49-54 at 40/100G can be configured as uplink, FCoE, or appliance port. Ports 49-54 after breakout to 10/25G can be configured as uplink, appliance, FCoE, or for direct-connect rack server connectivity. 


Cisco UCS 6300 Series Fabric Interconnects

#### Fabric Interconnect Features 

A Cisco UCS 6300 Series Fabric Interconnect provides both network connectivity and management capabilities to a Cisco UCS system. The fabric interconnect provides Ethernet and Fibre Channel to the servers in the system, the servers connect to the fabric interconnect, and the fabric interconnect connects to the LAN or SAN. 

Each Cisco UCS 6300 Series Fabric Interconnect runs Cisco UCS Manager to fully manage all Cisco UCS elements. The fabric interconnect supports full end-to-end 40-Gigabit capabilities in the fabric and enables 16-Gigabit Fibre Channel capabilities. High availability can be achieved when a Cisco UCS 6300 Series Fabric Interconnect is connected to another Cisco UCS 6300 Series Fabric Interconnect through the L1 or L2 port on each device. 

The Cisco UCS 6300 Series Fabric Interconnect joins next-generation UCS products, including the following hardware: 

  * Cisco UCS 6332 Fabric Interconnect, an Ethernet or Fibre Channel over Ethernet (FCoE) chassis with 32 40-Gigabit QSFP+ ports 

  * Cisco UCS 6332-16UP Fabric Interconnect, an Ethernet, FCoE, and Fibre Channel chassis with 16 1- or 10-Gigabit SFP+ ports or 16 4-, 8-, or 16-Gigabit Fibre Channel ports, 24 40-Gigabit QSFP+ ports 

  * Cisco 2304 IOM  or Cisco 2304V2, I/O modules with 8 40-Gigabit backplane ports and 4 40-Gigabit uplink ports 

  * Multiple VICs 


#### Cisco UCS 6332 Fabric Interconnect 

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
  
#### Cisco UCS 6332-16UP Fabric Interconnect 

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
  
#### Ports on the Cisco UCS 6300 Series Fabric Interconnects 

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


##### Port Modes

The port mode determines whether a unified port on the fabric interconnect is configured to carry Ethernet or Fibre Channel traffic. You configure the port mode in Cisco UCS Manager. However, the fabric interconnect does not automatically discover the port mode. 

Changing the port mode deletes the existing port configuration and replaces it with a new logical port. Any objects associated with that port configuration, such as VLANs and VSANS, are also removed. There is no restriction on the number of times you can change the port mode for a unified port. 

##### Port Types

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


##### Port Breakout Functionality on Cisco UCS 6300 Series Fabric Interconnects 

###### About Breakout Ports 

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
  
###### Breakout Port Constraints 

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
  
#### Ports on the Cisco UCS Fabric Interconnects

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
  
#### Migration for Cisco UCS Fabric Interconnects

Cisco UCS Manager allows you to migrate from the following:

  * Cisco UCS 6200 Series to UCS 6500 Fabric Interconnects. 

  * Cisco UCS 6300 Series to UCS 6500 Fabric Interconnects.

  * Cisco UCS 6400 Series to Cisco UCS 6536 Fabric Interconnect

  * Cisco UCS 6454 Series to Cisco UCS 6536 Fabric Interconnect

  * Cisco UCS 64108 Series to Cisco UCS 6536 Fabric Interconnect

  * Cisco UCS 6454 Series to Cisco UCS 6536 Fabric Interconnect migration to UCS Central

  * Cisco UCS 64108 Series to Cisco UCS 6536 Fabric Interconnect migration to UCS Central


For more information, refer to the corresponding _Migration Guide for Cisco UCS Fabric Interconnects_ on the [Cisco UCS Manager Configuration Guides](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) listing page. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct) cannot currently be migrated to any other Fabric Interconnects. 

* * *  
  
---|---  
  
### Introduction to Cisco UCS Manager

Cisco UCS Manager is embedded software that resides on the fabric interconnects, providing complete configuration and management capabilities for all of the components in the Cisco UCS system. This configuration information is replicated between the two fabric interconnects, providing a highly available solution for this critical function. The most common way to access Cisco UCS Manager for simple tasks is to use a Web browser. A command-line interface (CLI) and an XML API are also included for command-line or programmatic operations. 

The Cisco UCS Manager GUI provides role-based access control (RBAC) to allow multiple levels of users administrative rights to system objects. Users can be restricted to certain portions of the system based on locale, which corresponds to an optional organizational structure that can be created. Users can also be classified based on their access levels or areas of expertise, such as Storage Administrator, Server Equipment Administrator, or Read-Only. 

Cisco UCS Manager provides unified, embedded management of all software and hardware components. Every instance of Cisco UCS Manager and all of the components managed by it form a domain. For organizations that deploy multiple Cisco UCS domains, Cisco UCS Central software provides a centralized user interface that allows you to manage multiple, globally distributed Cisco UCS domains with thousands of servers. Cisco UCS Central integrates with Cisco UCS Manager and utilizes it to provide global configuration capabilities for pools, policies, and firmware. 

## Configuration Options 

You can configure a Cisco UCS domain in the following ways: 

  * As a single fabric interconnect in a standalone configuration 

  * As a redundant pair of fabric interconnects in a cluster configuration 


A cluster configuration provides high availability. If one fabric interconnect becomes unavailable, the other takes over. Only one management port (Mgmt0) connection is required to support a cluster configuration. However, both Mgmt0 ports should be connected to provide link-level redundancy. In a cluster configuration, the master and slave slots are identified as primary and subordinate. 

In addition, a cluster configuration actively enhances failover recovery time for redundant virtual interface (VIF) connections. When an adapter has an active VIF connection to one fabric interconnect and a standby VIF connection to the second, the learned MAC addresses of the active VIF are replicated but not installed on the second fabric interconnect. If the active VIF fails, the second fabric interconnect installs the replicated MAC addresses and broadcasts them to the network through gratuitous ARP messages, shortening the switchover time. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The cluster configuration provides redundancy only for the management plane. Data redundancy is dependent on the user configuration and might require a third-party tool to support data redundancy. 

* * *  
  
---|---

---

## Page 9: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Getting-Started/4-3/m_initial_configuration.html

# Initial Configuration   
  
## Initial Configuration Overview 

Before you get started with Cisco UCS Manager initial configuration, review the Fundamentals of Cisco Unified Computing System and System Requirements sections in this guide. 

The Cisco UCS Manager initial configuration involves the following steps: 

Figure 1. Cisco UCS Manager Initial Configuration Overview   
![](/c/dam/en/us/td/i/300001-400000/300001-310000/305001-306000/305200.jpg)  


  1. Console Setup—This step involves launching Cisco UCS Manager using the serial console. The Fabric Interconnect runs an initial configuration wizard and assigns three IP addresses in the management and administrative subnet: one for each Fabric Interconnect and one for the virtual IP interface that defines the Cisco UCS Manager instance and enables management. For more information on this step, see Console Setup

  2. Configure Administration Policies—This step involves configuration of administration policies, such as DNS Server, NTP, and Time Zone, that are necessary for proper functioning of all components. For more information on this step, see Configure Administration Policies. 

  3. Configure Equipment Policies—This step involves performing chassis discovery by setting the equipment policies in Cisco UCS Manager. The Chassis Discovery Policy specifies the minimum number of connections between the I/O modules and the Fabric Interconnects. This value must be set explicitly. For more information on this step, see Configure Equipment Policies

  4. Configure Unified Ports—This step involves configuring Unified Ports on the primary and subordinate Fabric Interconnects. Configure Unified Ports

  5. Configure Fabric Interconnect Server Ports—This step involves configuring Fabric Interconnect Server Ports. For more information on this step, see Configure Fabric Interconnect Server Ports
  6. Configure LAN Connectivity—This step involves establishing initial LAN connectivity from Fabric Interconnects. For more information on this step, see Configure LAN Connectivity. 

  7. Configure SAN Connectivity—This step involves establishing initial SAN connectivity from Fabric Interconnects. For more information on this step, see Configure SAN Connectivity

  8. Define Workloads—After completing initial configuration, you can define your workloads. For more information on this step, see Define Workloads. 


## Console Setup 

Initial configuration of Cisco UCS Fabric Interconnects is performed using the console connection. It is essential to maintain symmetric Cisco UCS Manager versions between the fabric interconnects in a domain. Refer to the latest Cisco UCS Manager Release Notes, and Firmware Management guide to determine the supported firmware versions. 

### Before you begin 

Collect the following required information for the console setup: 

  * System name 

  * Password for the admin account. Choose a strong password that meets the guidelines for Cisco UCS Manager passwords. The password field cannot be blank. 

  * Management port IPv4 and subnet mask, or IPv6 address and prefix. 

  * Default gateway IPv4 or IPv6 address. 

  * DNS server IPv4 or IPv6 address (optional). 

  * Domain name for the system (optional). 


### Installation method 

You can set up Cisco UCS Manager via GUI or CLI. 

Installation Method  |  See   
---|---  
GUI |  Configure the Primary Fabric Interconnect Using GUI  
CLI |  Configure the Primary Fabric Interconnect Using CLI  
  
  * Configure Fabric Interconnects
  * Verify Console Setup


### Configure Fabric Interconnects 

Initial configuration of Fabric Interconnects is performed using the console connection. It is essential to maintain symmetric Cisco UCS Manager versions between the Fabric Interconnects in a domain. Refer to the latest Cisco UCS Manager Release Notes, and Firmware Management guide to determine the supported firmware versions. 

  * Configure the Primary Fabric Interconnect Using GUI
  * Configure the Subordinate Fabric Interconnect Using GUI
  * Configure the Primary Fabric Interconnect Using CLI
  * Configure the Subordinate Fabric Interconnect Using CLI


#### Configure the Primary Fabric Interconnect Using GUI

You can either follow the procedure below for configuring the primary fabric interconnect or watch [Cisco UCS Manager Initial Setup part 1](http://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/videos/3-1/cisco_ucs_manager_initial_setup.html). 

##### Procedure

* * *

**Step 1** |  Power on the fabric interconnect.  You will see the power on self-test messages as the fabric interconnect boots.   
---|---  
**Step 2** |  If the system obtains a lease, go to step 6, otherwise, continue to the next step.   
**Step 3** |  Connect to the console port.   
**Step 4** |  At the installation method prompt, enter `gui`.   
**Step 5** |  If the system cannot access a DHCP server, you are prompted to enter the following information: 

  * IPv4 or IPv6 address for the management port on the fabric interconnect. 
  * IPv4 subnet mask or IPv6 prefix for the management port on the fabric interconnect. 
  * IPv4 or IPv6 address for the default gateway assigned to the fabric interconnect. 

|  **Note** |  In a cluster configuration, both fabric interconnects must be assigned the same management interface address type during setup.   
---|---  
**Step 6** |  Copy the web link from the prompt into a web browser and go to the Cisco UCS Manager GUI launch page.   
**Step 7** |  On the Cisco UCS Manager GUI launch page, select Express Setup.   
**Step 8** |  On the Express Setup page, select Initial Setup and click Submit.  |  **Note** |  In the Fabric Interconnects initial setup page, if the Fabric Interconnect defaults to Intersight managed mode, you can choose to change during confirmation and select required mode again in console setup method alone. This is applicable for Cisco UCS 6400 Series, 6500 SeriesFabric Interconnects , and Cisco UCS Fabric Interconnects 9108 100G.   
---|---  
**Step 9** |  In the Cluster and Fabric Setup area: 

  1. Click the Enable Clustering option. 
  2. For the Fabric Setup option, select Fabric A. 
  3. In the Cluster IP Address field, enter the IPv4 or IPv6 address that Cisco UCS Manager will use. 

  
**Step 10** |  In the System Setup area, complete the following fields:  |  **Field** |  **Description**  
---|---  
System Name |  The name assigned to the Cisco UCS domain.  In a standalone configuration, the system adds "-A" to the system name. In a cluster configuration, the system adds "-A" to the fabric interconnect assigned to fabric A, and "-B" to the fabric interconnect assigned to fabric B.   
Admin Password |  The password used for the Admin account on the fabric interconnect.  Choose a strong password that meets the guidelines for Cisco UCS Manager passwords. This password cannot be blank.   
Confirm Admin Password |  The password used for the Admin account on the fabric interconnect.   
Mgmt IP Address |  The static IPv4 or IPv6 address for the management port on the fabric interconnect.   
Mgmt IP Netmask or Mgmt IP Prefix  |  The IPv4 subnet mask or IPv6 prefix for the management port on the fabric interconnect.  |  **Note** |  The system prompts for a Mgmt IP Netmask or a Mgmt IP Prefix based on what address type you entered in the Mgmt IP Address.   
---|---  
Default Gateway |  The IPv4 or IPv6 address for the default gateway assigned to the management port on the fabric interconnect.  |  **Note** |  The system prompts for a Default Gateway address type based on what type you entered in the Mgmt IP Address field.   
---|---  
DNS Server IP |  The IPv4 or IPv6 address for the DNS Server assigned to the fabric interconnect.   
Domain Name |  The name of the domain in which the fabric interconnect resides.   
**Step 11** |  Click Submit.  A page displays the results of your setup operation.   
  
* * *

#### Configure the Subordinate Fabric Interconnect Using GUI

You can either follow the procedure below for configuring the subordinate fabric interconnect or watch[ Cisco UCS Manager Initial Setup part 2](http://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/videos/3-1/cisco_ucs_manager_initial_setup.html). 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

When adding a new fabric interconnect to an existing High Availability cluster, for example, during a new install or when replacing a fabric interconnect, the new device will not be able to log into the cluster as long as the authentication method is set to remote. To successfully add a new fabric interconnect to the cluster, the authentication method must be temporarily set to local and the local admin credentials of the primary fabric interconnect must be used. 

* * *  
  
---|---  
  
##### Procedure

* * *

**Step 1** |  Power up the fabric interconnect.  You will see the power-up self-test message as the fabric interconnect boots.   
---|---  
**Step 2** |  If the system obtains a lease, go to step 6, otherwise, continue to the next step.   
**Step 3** |  Connect to the console port.   
**Step 4** |  At the installation method prompt, enter `gui`.   
**Step 5** |  If the system cannot access a DHCP server, you are prompted to enter the following information: 

  * IPv4 or IPv6 address for the management port on the fabric interconnect 
  * IPv4 subnet mask or IPv6 prefix for the management port on the fabric interconnect 
  * IPv4 or IPv6 address for the default gateway assigned to the fabric interconnect 

|  **Note** |  In a cluster configuration, both fabric interconnects must be assigned the same management interface address type during setup.   
---|---  
**Step 6** |  Copy the web link from the prompt into a web browser and go to the Cisco UCS Manager GUI launch page.   
**Step 7** |  On the Cisco UCS Manager GUI launch page, select Express Setup.   
**Step 8** |  On the Express Setup page, select Initial Setup and click Submit.  The fabric interconnect should detect the configuration information for the first fabric interconnect.   
**Step 9** |  In the Cluster and Fabric Setup Area: 

  1. Select the Enable Clustering option. 
  2. For the Fabric Setup option, make sure Fabric B is selected. 

  
**Step 10** |  In the System Setup Area, enter the password for the Admin account into the Admin Password of Master field.  The Manager Initial Setup Area is displayed.   
**Step 11** |  In the Manager Initial Setup Area, the field that is displayed depends on whether you configured the first fabric interconnect with an IPv4 or IPv6 management address. Complete the field that is appropriate for your configuration, as follows:  |  Field  |  Description   
---|---  
Peer FI is IPv4 Cluster enabled. Please Provide Local fabric interconnect Mgmt0 IPv4 Address |  Enter an IPv4 address for the Mgmt0 interface on the local fabric interconnect.   
Peer FI is IPv6 Cluster Enabled. Please Provide Local fabric interconnect Mgmt0 IPv6 Address |  Enter an IPv6 for the Mgmt0 interface on the local fabric interconnect.   
**Step 12** |  Click Submit.  A page displays the results of your setup operation.   
  
* * *

#### Configure the Primary Fabric Interconnect Using CLI

##### Procedure

* * *

**Step 1** |  Connect to the console port.   
---|---  
**Step 2** |  Power on the fabric interconnect. You will see the power-on self-test messages as the fabric interconnect boots.   
**Step 3** |  When the unconfigured system boots, it prompts you for the setup method to be used. Enter  console to continue the initial setup using the console CLI.   
**Step 4** |  Enter  setup to continue as an initial system setup.   
**Step 5** |  Enter  y to confirm that you want to continue the initial setup.   
**Step 6** |  Enter the password for the admin account.   
**Step 7** |  To confirm, re-enter the password for the admin account.   
**Step 8** |  Enter  yes to continue the initial setup for a cluster configuration.   
**Step 9** |  Enter the fabric interconnect fabric (either  A or  B ).   
**Step 10** |  Enter the system name.   
**Step 11** |  Enter the IPv4 or IPv6 address for the management port of the fabric interconnect.  If you enter an IPv4 address, you will be prompted to enter an IPv4 subnet mask. If you enter an IPv6 address, you will be prompted to enter an IPv6 network prefix.   
**Step 12** |  Enter the respective IPv4 subnet mask or IPv6 network prefix, then press `Enter`.  You are prompted for an IPv4 or IPv6 address for the default gateway, depending on the address type you entered for the management port of the fabric interconnect.   
**Step 13** |  Enter either of the following: 

  * IPv4 address of the default gateway 
  * IPv6 address of the default gateway 

  
**Step 14** |  Enter  yes if you want to specify the IP address for the DNS server, or  no if you do not.   
**Step 15** |  (Optional) Enter the IPv4 or IPv6 address for the DNS server.  The address type must be the same as the address type of the management port of the fabric interconnect.   
**Step 16** |  Enter  yes if you want to specify the default domain name, or  no if you do not.   
**Step 17** |  (Optional) Enter the default domain name.   
**Step 18** |  Review the setup summary and enter  yes to save and apply the settings, or enter  no to go through the Setup wizard again to change some of the settings.  If you choose to go through the Setup wizard again, it provides the values you previously entered, and the values appear in brackets. To accept previously entered values, press Enter.   
  
* * *

##### Example

The following example sets up the first fabric interconnect for a cluster configuration using the console and IPv4 management addresses: 
    
    
    Enter the installation method (console/gui)?  **console**
    Enter the setup mode (restore from backup or initial setup) [restore/setup]? **setup**
    You have chosen to setup a new switch.  Continue? (y/n): **y**
    Enter the password for "admin": 
    Confirm the password for "admin": 
    Do you want to create a new cluster on this switch (select 'no' for standalone setup or if you want this switch to be added to an existing cluster)? (yes/no) [n]: **yes**
    Enter the switch fabric (A/B): **A**
    Enter the system name: **foo**
    Mgmt0 IPv4 address: **192.168.10.10**
    Mgmt0 IPv4 netmask: **255.255.255.0**
    IPv4 address of the default gateway: **192.168.10.1**
    Virtual IPv4 address: **192.168.10.12**
    Configure the DNS Server IPv4 address? (yes/no) [n]: **yes**
      DNS IPv4 address: **20.10.20.10**
    Configure the default domain name? (yes/no) [n]: **yes**
      Default domain name: **domainname.com**
    Join centralized management environment (UCS Central)? (yes/no) [n]: **no**
    Following configurations will be applied:
      Switch Fabric=A
      System Name=foo
      Management IP Address=192.168.10.10
      Management IP Netmask=255.255.255.0
      Default Gateway=192.168.10.1
      Cluster Enabled=yes  
      Virtual Ip Address=192.168.10.12
      DNS Server=20.10.20.10
      Domain Name=domainname.com
    Apply and save the configuration (select 'no' if you want to re-enter)? (yes/no): **yes**
    

The following example sets up the first fabric interconnect for a cluster configuration using the console and IPv6 management addresses: 
    
    
    Enter the installation method (console/gui)?  **console**
    Enter the setup mode (restore from backup or initial setup) [restore/setup]? **setup**
    You have chosen to setup a new switch.  Continue? (y/n): **y**
    Enter the password for "admin": 
    Confirm the password for "admin": 
    Do you want to create a new cluster on this switch (select 'no' for standalone setup or if you want this switch to be added to an existing cluster)? (yes/no) [n]: **yes**
    Enter the switch fabric (A/B): **A**
    Enter the system name: **foo**
    Mgmt0 address: **2001::107**
    Mgmt0 IPv6 prefix: **64**
    IPv6 address of the default gateway: **2001::1**
    Configure the DNS Server IPv6 address? (yes/no) [n]: **yes**
      DNS IP address: **2001::101**
    Configure the default domain name? (yes/no) [n]: **yes**
      Default domain name: **domainname.com**
    Join centralized management environment (UCS Central)? (yes/no) [n]: **no**
    Following configurations will be applied:
      Switch Fabric=A
      System Name=foo
      Enforced Strong Password=no
      Physical Switch Mgmt0 IPv6 Address=2001::107
      Physical Switch Mgmt0 IPv6 Prefix=64
      Default Gateway=2001::1
      Ipv6 value=1
      DNS Server=2001::101
      Domain Name=domainname.com
    Apply and save the configuration (select 'no' if you want to re-enter)? (yes/no): **yes**
    

#### Configure the Subordinate Fabric Interconnect Using CLI

This procedure describes setting up the second fabric interconnect using IPv4 or IPv6 addresses for the management port. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

When adding a new Fabric Interconnect to an existing High Availability cluster, for example, during a new install or when replacing a Fabric Interconnect, the new device will not be able to log into the cluster as long as the authentication method is set to remote. To successfully add a new Fabric Interconnect to the cluster, the authentication method must be temporarily set to local and the local admin credentials of the primary Fabric Interconnect must be used. 

* * *  
  
---|---  
  
##### Procedure

* * *

**Step 1** |  Connect to the console port.   
---|---  
**Step 2** |  Power up the fabric interconnect.  You will see the power-on self-test messages as the fabric interconnect boots.   
**Step 3** |  When the unconfigured system boots, it prompts you for the setup method to be used. Enter  console to continue the initial setup using the console CLI.  |  **Note** |  The fabric interconnect should detect the peer fabric interconnect in the cluster. If it does not, check the physical connections between the L1 and L2 ports, and verify that the peer fabric interconnect has been enabled for a cluster configuration.   
---|---  
**Step 4** |  Enter  y to add the subordinate fabric interconnect to the cluster.   
**Step 5** |  Enter the admin password of the peer fabric interconnect.   
**Step 6** |  Enter the IP address for the management port on the subordinate fabric interconnect.   
**Step 7** |  Review the setup summary and enter  yes to save and apply the settings, or enter  no to go through the Setup wizard again to change some of the settings.  If you choose to go through the Setup wizard again, it provides the values you previously entered, and the values appear in brackets. To accept previously entered values, press Enter.   
  
* * *

##### Example

The following example sets up the second fabric interconnect for a cluster configuration using the console and the IPv4 address of the peer: 
    
    
    Enter the installation method (console/gui)? **console**
    Installer has detected the presence of a peer Fabric interconnect. This Fabric interconnect will be added to the cluster. Continue (y/n) ? **y**
    Enter the admin password of the peer Fabric Interconnect: 
    Peer Fabric interconnect Mgmt0 IPv4 Address: **192.168.10.11**
    Apply and save the configuration (select 'no' if you want to re-enter)? (yes/no): **yes**
    

The following example sets up the second fabric interconnect for a cluster configuration using the console and the IPv6 address of the peer: 
    
    
    Enter the installation method (console/gui)? **console**
    Installer has detected the presence of a peer Fabric interconnect. This Fabric interconnect will be added to the cluster. Continue (y/n) ? **y**
    Enter the admin password of the peer Fabric Interconnect: 
    Peer Fabric interconnect Mgmt0 IPv6 Address: **2001::107**
    Apply and save the configuration (select 'no' if you want to re-enter)? (yes/no): **yes**
    

### Verify Console Setup 

You can verify that both fabric interconnect configurations are complete by logging into the fabric interconnect via SSH and verifying the cluster status through CLI. For this procedure, you can watch [Cisco UCS Manager Initial Setup part 3](http://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/videos/3-1/cisco_ucs_manager_initial_setup.html). 

Use the following commands to verify the cluster state:  Command  |  Purpose  |  Sample Output   
---|---|---  
show cluster state |  Displays the operational state and leadership role for both fabric interconnects in a high availability cluster.  |  The following example displays that both fabric interconnects are in the Up state, HA is in the Ready state, fabric interconnect A has the primary role, and fabric interconnect B has the subordinate role: 
    
    
    UCS-A# show cluster state 
    Cluster Id: 0x4432f72a371511de-0xb97c000de1b1ada4 
    
    A: UP, PRIMARY 
    B: UP,
    SUBORDINATE HA READY
      
  
show cluster extended-state |  Displays extended details about the cluster state and typically used when troubleshooting issues.  |  The following example shows how to view the extended state of a cluster: 
    
    
    UCSC# show cluster extended-state 0x2e95deacbd0f11e2-0x8ff35147e84f3de2Start time: Thu May 16 06:54:22 2013Last election time: Thu May 16 16:29:28 2015System Management
    Viewing the Cluster State
    A: UP, PRIMARY
    B: UP, SUBORDINATE
    
    A: memb state UP, lead state PRIMARY, mgmt services state: UP
    B: memb state UP, lead state SUBORDINATE, 
    mgmt services state: UP heartbeat state PRIMARY_OK 
    HA READY 
    Detailed state of the device selected for HA quorum data: 
    Device 1007, serial: a66b4c20-8692-11df-bd63-1b72ef3ac801, state: active 
    Device 1010, serial: 00e3e6d0-8693-11df-9e10-0f4428357744, state: active 
    Device 1012, serial: 1d8922c8-8693-11df-9133-89fa154e3fa1, state: active  
  
## Configure Administration Policies 

After completing initial configuration, configure global system administration settings such as faults, events, users, external directory services, communication services, and licensing. 

Use the following table for specific guidance on how to configure various administration policies. 

Task  |  See   
---|---  
Time Zone Management  |  Cisco UCS Manager Administration Management Guide  
Register with Cisco UCS Central  |  Cisco UCS Manager Infrastructure Management Guide  
User Management  |  Cisco UCS Manager Infrastructure Management Guide  
Communications Management  |  Cisco UCS Manager Administration Management Guide  
(Optional) Key Management  |  Cisco UCS Manager Administration Management Guide  
License Management  |  Cisco UCS Manager Administration Management Guide  
  
## Configure Equipment Policies 

After configuring administration policies, set equipment policies such as Chassis/FEX Discovery policy, Power Policy, MAC Address changing policy and SEL Policy. 

Use the following table for specific guidance on how to configure various equipment policies. 

Task  |  See   
---|---  
Configure global policies including Chassis/FEX Discovery Policy, Power Policy and Information Policy  |  Cisco UCS Manager Infrastructure Management Guide  
Configure SEL Policy  |  Cisco UCS Manager Administration Management Guide  
  
## Configure Unified Ports 

After configuring equipment policies, enable Unified Ports. It is recommended that you first configure Unified Ports on the Primary Fabric Interconnect, then on the Subordinate Fabric Interconnect. 

Use the following table for specific guidance on how to configure Unified ports. 

Task  |  See   
---|---  
Configure Unified Ports  |  Cisco UCS Network Management Guide  
  
## Configure Fabric Interconnect Server Ports 

After configuring Unified Ports, enable Fabric Interconnect Server Ports. 

Use the following table for specific guidance on how to configure fabric interconnect server ports. 

Task  |  See   
---|---  
Configure Fabric Interconnect Server Ports  |  **Note** |  Starting with Cisco UCS Manager release 3.1(3), you can automatically configure the fabric interconnect server ports.  
---|---  
Cisco UCS Manager Network Management Guide  
  
## Configure LAN Connectivity 

After configuring Fabric Interconnect Server Ports, complete initial LAN connectivity by enabling Fabric Interconnect Ethernet Ports. 

Use the following table for specific guidance on how to configure LAN connectivity. 

Task  |  See   
---|---  
Configure Fabric Interconnect Ethernet Ports  |  Cisco UCS Manager Network Management Guide  
  
## Configure SAN Connectivity 

After configuring LAN connectivity, complete initial SAN connectivity by enabling Fabric Interconnect FC Ports. 

Use the following table for specific guidance on how to configure SAN connectivity. 

Task  |  See   
---|---  
Configure Fabric Interconnect FC Ports  |  Cisco UCS Manager Storage Management Guide  
  
## Define Workloads 

After completing Cisco UCS Manager initial configuration, use the following steps in the recommended order to define your workload:  Step  |  Description  |  See   
---|---|---  
Define organizational hierarchy  |  Cisco UCS organizational structure facilitates hierarchical configuration of Cisco UCS resources. An Organization can be created for policies, pools, and service profiles. The default Organization for any resource category is Root. Based on requirements, multiple sub-organizations can be created under the Root organization. You can create nested sub-organization under a sub-organization.  |  Cisco UCS Manager Administration Management Guide  
Define Pools  |  Pools in Cisco UCS Manager are used for abstracting unique identities and resources for devices such as vNICs, vHBAs and server pools can assign servers in groups based on similar server characteristics.  |  Cisco UCS Manager Network Management Guide  
Configure Adapters  |  Cisco UCS contains predefined adapter policies for most operating systems, including hypervisors. The settings in these predefined policies are for optimal adapter performance.  |  Cisco UCS Manager Network Management Guide  
Configure Server Policies  |  Configuring Server Policies in Cisco UCS Manager includes Server-Related Policies such as BIOS Policy, Local Disk Configuration Policy, IPMI Access Profiles, and Server Autoconfiguration.  |  Cisco UCS Manager Server Management Guide  
Configure Service Profile Templates  |  Cisco UCS Service Profile Templates are used to create multiple services profiles with similar characteristics.  |  Cisco UCS Manager Server Management Guide

---
