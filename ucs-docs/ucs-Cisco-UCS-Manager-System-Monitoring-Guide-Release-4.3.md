# Cisco UCS Manager System Monitoring Guide, Release 4.3 - Cisco

| | |
|---|---|
| **URL Title** | Cisco UCS Manager System Monitoring Guide, Release 4.3 - Cisco |
| **URL** | https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/System-Monitoring/4-3/b-ucsm-gui-system-monitoring-guide-4-3.html |
| **Long URL** |  |
| **HTML Title** | Cisco UCS Manager System Monitoring Guide, Release 4.3 |
| **Source file** | `ucs-docs-raw/html/b-ucsm-gui-system-monitoring-guide-4-3.html` |
| **File type** | HTML |
| **Fetched on** | 2026-04-08 08:41:46 |

---

## Page 1: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/System-Monitoring/4-3/b-ucsm-gui-system-monitoring-guide-4-3.html

![Clear Contents of Search](/etc/designs/cdc/fw/i/ic_clear_gray.png)

---

## Page 2: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/System-Monitoring/4-3/b-ucsm-gui-system-monitoring-guide-4-3/m_preface.html

## Audience

This guide is intended primarily for data center administrators with responsibilities and expertise in one or more of the following: 

  * Server administration 

  * Storage administration 

  * Network administration 

  * Network security 


---

## Page 3: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/System-Monitoring/4-3/b-ucsm-gui-system-monitoring-guide-4-3/m-new-and-changed-4-3.html

## New and Changed Information for This Release

This section provides information on new features and changed behaviors in Cisco UCS Manager, Release 4.3.

Table 1. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(6a) Feature |  Description |  Where Documented  
---|---|---  
Support for X-Series M8 and C-Series M8 servers |  Cisco UCS Manager now supports Cisco UCS X210c M8 Compute Node, Cisco UCS C240 M8 Server, and Cisco UCS C220 M8 Server | 

  * [Support for Local Storage Monitoring](m_hardware_monitoring.html#reference_s5w_2fy_ndb)
  * [Graphics Card Server Support](m_hardware_monitoring.html#concept_B6CBDE8AAEE041B9A3E5165193A53B36)
  * [TFM and Supercap Guidelines and Limitations](m_hardware_monitoring.html#concept_ED653EA1CAA349739E8BF2616A29C645)

  
Table 2. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(5a) Feature |  Description |  Where Documented  
---|---|---  
Support for Cisco UCS X215c M8 Compute Node |  Cisco UCS Manager now supports Cisco UCS X215c M8 Compute Node.  | 

  * [Graphics Card Server Support](m_hardware_monitoring.html#concept_B6CBDE8AAEE041B9A3E5165193A53B36)
  * [TFM and Supercap Guidelines and Limitations](m_hardware_monitoring.html#concept_ED653EA1CAA349739E8BF2616A29C645)

  
Support for Cisco UCS C225 M8 Server |  Cisco UCS Manager now supports Cisco UCS C225 M8 Server | 

  * [Graphics Card Server Support](m_hardware_monitoring.html#concept_B6CBDE8AAEE041B9A3E5165193A53B36)
  * [TFM and Supercap Guidelines and Limitations](m_hardware_monitoring.html#concept_ED653EA1CAA349739E8BF2616A29C645)

  
Table 3. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(4b) Feature |  Description |  Where Documented  
---|---|---  
Support for Cisco UCS Fabric Interconnects 9108 100G |  Cisco UCS Manager now supports Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct).  | 

  * [Configuring the Syslog Using Cisco UCS Manager GUI](m_syslog.html#task_6BC3B5C19B1B439A9A5CBB8445740400)
  * [Configuring Smart Call Home](m_call_home_and_smart_call_home_monitoring.html#task_8C24D00D7DF74266B508C0AC1CCDD84C)
  * [NetFlow Monitoring](m_netflow_monitoring.html#concept_k2x_dxz_22b)
  * [NetFlow Limitations](m_netflow_monitoring.html#netflow-limitations)

  
Table 4. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(4b) Feature |  Description |  Where Documented  
---|---|---  
Support for Cisco UCS C-Series M8 servers |  Cisco UCS Manager now supports Cisco UCS C245 M8 Servers.  | 

  * [Support for Local Storage Monitoring](m_hardware_monitoring.html#reference_s5w_2fy_ndb)
  * [TFM and Supercap Guidelines and Limitations](m_hardware_monitoring.html#concept_ED653EA1CAA349739E8BF2616A29C645)

  
Table 5. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(4a) Feature |  Description |  Where Documented  
---|---|---  
Traffic Monitoring |  Cisco UCS Manager guidelines for configuring ERSPAN Traffic Monitoring on Cisco UCS 64108 Fabric Interconnects and Cisco UCS 6532 Fabric Interconnects.  |  [Traffic Monitoring](m_traffic_monitoring.html#concept_hcj_z1r_tdb)  
PCIe Node Monitoring |  PCIe node inventory monitoring. |  [Monitoring PCIe Node](m_hardware_monitoring.html#monitoring-pcie-node)  
  
### New in Relese 4.3(4b)

### Cisco UCS X-Series Direct®

The Cisco UCS X-Series Direct® simplifies your data center, adapting to the unpredictable needs of modern applications while also providing an edge scaled for remote branch office workloads. It minimizes the IT infrastructure deployed at edge locations to achieve desired business outcomes. As you are looking to increase the number of applications at the edge while deploying as little IT infrastructure as possible, the Cisco UCS X-Series Direct®, powered by Cisco Intersight® and Cisco UCS Manager, enables the benefits of scale together with a secure and unified connectivity. 

The Cisco UCS X-Series Direct begins with the Cisco UCS X9508 Chassis engineered to be adaptable and future ready. It is a standard, open system designed to deploy and automate faster in concert with a hybrid-cloud environment. 

With a midplane-free design, I/O connectivity for the X9508 chassis is accomplished with frontloading, vertically oriented compute nodes intersecting with horizontally oriented I/O connectivity modules in the rear of the chassis. The I/O connectivity modules of the solution are the Cisco UCS X-Series Direct Fabric Interconnect Modules, a unified fabric for Ethernet and Fibre Channel. Additionally, the UCS X9508 chassis can have expanded GPU capabilities using the Cisco UCS X-Fabric technology which interconnects X-series compute and PCIe nodes using high-speed PCIe technology. 

For more information see [Cisco UCS X-Series Direct Data Sheet](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-x-series-modular-system/ucs-x-series-direct-ds.html). 

### New in Release 4.3(4b)

### Cisco UCS C245 M8 Rack Server

The Cisco UCS C245 M8 Server is perfectly suited for a wide range of storage and I/O-intensive applications such as big data analytics, databases, collaboration, virtualization, consolidation, AI/ML and high-performance computing supporting up to two AMD® CPUs in a 2RU form factor. 

The Cisco UCS C245 M8 Server extends the capabilities of the Cisco UCS rack server portfolio. With advanced features like AMD Infinity Guard, compute-intensive applications will see significant performance improvements and will reap other benefits such as power and cost efficiencies. 

You can deploy the Cisco UCS C-Series rack servers as part of the Cisco Unified Computing System™ managed by Cisco Intersight® or Cisco UCS Manager® to take advantage of Cisco® standards-based unified computing innovations that can help reduce your Total Cost of Ownership (TCO) and increase your business agility or as standalone servers. 

The Cisco UCS C245 M8 Server brings many innovations to the UCS AMD® rack server line. With the introduction of PCIe Gen 5.0 expansion slots for high-speed I/O, a DDR5 memory bus, and expanded storage capabilities, the server delivers significant performance and efficiency gains that will greatly enhance application performance. Features include: 

  * Support for up to two 4th Gen AMD EPYC™ CPUs in a server designed to drive as much as 256 CPU cores (128 cores per socket) 

  * Up to 24 DDR5 DIMM slots

  * Up to 4800 MT/s DDR5 memory

  * Up to 8 x PCIe Gen 4.0 slots or up to 4 x PCIe Gen 5.0 slots, plus a hybrid modular LAN on motherboard (mLOM) /OCP 3.0 slot (details below) 

  * Support for Cisco UCS VIC 15000 Series adapters as well as a host of third-party NIC options

  * Up to 28 hot-swappable small-form-factor (SFF) SAS/SATA or NVMe drives (with up to 8 direct-attach NVMe drives) and New tri-mode RAID controller supports SAS4 plus NVMe hardware RAID. 

  * M.2 boot options

  * Up to two 960GB SATA M.2 drives with hardware RAID support

  * Up to two 960GB NVMe M.2 drives with NVMe hardware RAID

  * Support for up to Eight GPUs

  * Modular LOM / OCP 3.0

  * One dedicated PCIe Gen4x16 slot that can be used to add an mLOM or OCP 3.0 card for additional rear-panel connectivity

  * mLOM slot that can be used to install a Cisco UCS Virtual Interface Card (VIC) without consuming a PCIe slot, supporting quad-port 10/25/50 Gbps or dual-port 40/100/200 Gbps network connectivity 

  * OCP 3.0 slot that features full out-of-band management for select adapters


Cisco UCS Manager supports all the peripherals supported by Cisco UCS C245 M8 Server. For complete list of supported peripherals for Cisco UCS C245 M8 Server, see [Cisco UCS C245 M8 SFF Rack Server Spec Sheet](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/ucs-c245-m8-sff-rack-server.pdf&ved=2ahUKEwjDqcbvxdiGAxXuzzgGHUbnAy0QFnoECBUQAQ&usg=AOvVaw0MzOh0jzcaa9bNdqgl3iaT). 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCS C245 M8 Server supports only 15000 Series secure boot VIC adapters. 

* * *  
  
---|---  
  
### New in Release 4.3(2c)

### Cisco UCS X410c M7 Compute Node

The Cisco UCS X410c M7 Compute Node is the first 4-socket 4th Gen Intel® Xeon® Scalable Processors computing device to integrate into the Cisco UCS X-Series Modular System. Up to four compute nodes or two compute nodes and two GPU nodes can reside in the 7-rack-unit (7RU) Cisco UCS X9508 Server Chassis, offering high performance and efficiency gains for a wide range of mission-critical enterprise applications, memory-intensive applications and bare-metal and virtualized workloads. 

The Cisco UCS X410c M7 Compute Node provides these main features: 

  * CPU: Four 4th Gen Intel Xeon Scalable Processors with up to 60 cores per processor

  * Memory: Up to 16TB of main memory with 64x 256 GB DDR5-4800 Memory DIMMs

  * Storage: Up to six hot-pluggable solid-state drives (SSDs), or non-volatile memory express (NVMe) 2.5-inch drives with a choice of enterprise-class RAID or passthrough controllers, up to two M.2 SATA drives with optional hardware RAID 

  * mLOM virtual interface cards:

  * Cisco UCS VIC 15420 occupies the server's modular LAN on motherboard (mLOM) slot, enabling up to 50 Gbps of unified fabric connectivity to each of the chassis’s intelligent fabric modules (IFMs) for 100 Gbps connectivity per server. 

  * Cisco UCS VIC 15231 occupies the server's modular LAN on motherboard (mLOM) slot, enabling up to 100 Gbps of unified fabric connectivity to each of the chassis’s intelligent fabric modules (IFMs) for 100 Gbps connectivity per server. 

  * Cisco UCS VIC 15230 (with secure boot feature) occupies the server's modular LAN on motherboard (mLOM) slot, enabling up to 100 Gbps of unified fabric connectivity to each of the chassis’s intelligent fabric modules (IFMs) for 100 Gbps connectivity per server. 

  * Optional mezzanine card:

  * Cisco UCS 5th Gen VIC 15422 can occupy the server's mezzanine slot at the bottom rear of the chassis. This card's I/O connectors link to Cisco UCS X-Fabric technology. An included bridge card extends this VIC's 2x 50 Gbps of network connections through IFM connectors, bringing the total bandwidth to 100 Gbps per fabric (for a total of 200 Gbps per server). 

  * Cisco UCS PCI Mezz card for Cisco UCS X-Fabric can occupy the server's mezzanine slot at the bottom rear of the chassis. This card's I/O connectors link to Cisco UCS X-Fabric modules and enable connectivity to the Cisco UCS X440p PCIe Node. 

  * All VIC mezzanine cards also provide I/O connections from the X410c M7 compute node to the X440p PCIe node.

  * Security: The server supports an optional trusted platform module (TPM). Additional features include a secure boot FPGA and ACT2 anti-counterfeit provisions. 


### Cisco UCS VIC Cards

Following Cisco UCS VIC Cards are supported from release 4.3(2c) onwards: 

  * Cisco UCS VIC 15427—The Cisco UCS VIC 15427 is a Quad Port CNA MLOM, 4 x 10/25/50G with Secure Boot for Cisco UCS C-Series M6 and M7 servers. 

  * Cisco UCS VIC 15230—The Cisco UCS VIC 15230 is a MLOM with Secure Boot for Cisco UCS X210c M6, X210c M7, and X410c M7 servers. 

  * Cisco UCS VIC 15237 mLOM—The Cisco UCS VIC 15237 mLOM is a MLOM, 2x40/100/200G with Secure Boot for Cisco UCS C-Series M6 and M7 servers. 


### New in Release 4.3(2b)

### Cisco UCS X210c M7 Compute Node

The Cisco UCS X210c M7 Compute Node is the second generation of compute node to integrate into the Cisco UCS X-Series Modular System. It delivers performance, flexibility, and optimization for deployments in data centers, in the cloud, and at remote sites. This enterprise-class server offers market-leading performance, versatility, and density without compromise for workloads. Up to eight compute nodes can reside in the 7-rack-unit (7RU) Cisco UCSX-9508 Chassis, offering one of the highest densities of compute, I/O, and storage per rack unit in the industry. 

The Cisco UCS X210c M7 Compute Node provides these main features: 

  * CPU: Up to 2x 4th Gen Intel® Xeon® Scalable Processors with up to 60 cores per processor and up to 2.625 MB Level 3 cache per core and up to 112.5 MB per CPU. 

  * Memory: Up to 8TB of main memory with 32x 256 GB DDR5-4800 DIMMs.

  * Storage: Up to six hot-pluggable, solid-state drives (SSDs), or non-volatile memory express (NVMe) 2.5-inch drives with a choice of enterprise-class redundant array of independent disks (RAIDs) or passthrough controllers, up to two M.2 SATA and M.2 NVMe drives with optional hardware RAID. 

  * Optional front mezzanine GPU module: The Cisco UCS front mezzanine GPU module is a passive PCIe Gen 4.0 front mezzanine option with support for up to two U.2 NVMe drives and two HHHL GPUs. 

  * mLOM virtual interface cards:

  * Cisco UCS Virtual Interface Card (VIC) 15420 occupies the server's modular LAN on motherboard (mLOM) slot, enabling up to 50 Gbps of unified fabric connectivity to each of the chassis intelligent fabric modules (IFMs) for 100 Gbps connectivity per server. 

  * ◦ Cisco UCS Virtual Interface Card (VIC) 15231 occupies the server's modular LAN on motherboard (mLOM) slot, enabling up to 100 Gbps of unified fabric connectivity to each of the chassis intelligent fabric modules (IFMs) for 100 Gbps connectivity per server. 

  * Optional mezzanine card:

  * Cisco UCS 5th Gen Virtual Interface Card (VIC) 15422 can occupy the server's mezzanine slot at the bottom rear of the chassis. This card's I/O connectors link to Cisco UCS X-Fabric technology. An included bridge card extends this VIC's 2x 50 Gbps of network connections through IFM connectors, bringing the total bandwidth to 100 Gbps per fabric (for a total of 200 Gbps per server). 

  * Cisco UCS PCI Mezz card for X-Fabric can occupy the server's mezzanine slot at the bottom rear of the chassis. This card's I/O connectors link to Cisco UCS X-Fabric modules and enable connectivity to the Cisco UCS X440p PCIe Node. 

  * All VIC mezzanine cards also provide I/O connections from the X210c M7 compute node to the X440p PCIe Node.

  * Security: The server supports an optional trusted platform module (TPM). Additional features include a secure boot FPGA and ACT2 anti-counterfeit provisions. 


### Cisco UCS X210c M6 Compute Node

The Cisco UCS X210c M6 Compute Node is the first computing device to integrate into the Cisco UCS X-Series Modular System. Up to eight compute nodes can reside in the 7-Rack-Unit (7RU) Cisco UCS X9508 Chassis, offering one of the highest densities of compute, I/O, and storage per rack unit in the industry. 

The Cisco UCS X210c M6 Compute Node provides these main features: 

  * CPU: Up to 2x 3rd Gen Intel® Xeon® Scalable Processors with up to 40 cores per processor and 1.5 MB Level 3 cache per core 

  * Memory: Up to 32x 256 GB DDR4-3200 DIMMs for up to 8 TB of main memory. Configuring up to 16x 512-GB Intel Optane™ persistent memory DIMMs can yield up to 12 TB of memory. 

  * Storage: Up to 6 hot-pluggable, solid-state drives (SSDs), or non-volatile memory express (NVMe) 2.5-inch drives with a choice of enterprise-class redundant array of independent disks (RAIDs) or pass-through controllers with four lanes each of PCIe Gen 4 connectivity and up to 2 M.2 SATA drives for flexible boot and local storage capabilities 

  * Optional front mezzanine GPU module: The Cisco UCS Front Mezzanine GPU module is a passive PCIe Gen 4 front mezzanine option with support for up to two U.2 NVMe drives and two GPUs. 

  * mLOM virtual interface cards:

  * Cisco UCS Virtual Interface Card (VIC) 14425 occupies the server's modular LAN on motherboard (mLOM) slot, enabling up to 50 Gbps of unified fabric connectivity to each of the chassis intelligent fabric modules (IFMs) for 100 Gbps connectivity per server. 

  * Cisco UCS VIC 15231 occupies the server's modular LAN on motherboard (mLOM) slot, enabling up to 100 Gbps of unified fabric connectivity to each of the chassis intelligent fabric modules (IFMs) for 100 Gbps connectivity per server. 

  * Cisco UCS VIC 15420 occupies the server's modular LAN on motherboard (mLOM) slot, enabling up to 100 Gbps of unified fabric connectivity to each of the chassis intelligent fabric modules (IFMs) for 100 Gbps connectivity per server. 

  * Optional mezzanine card:

  * Cisco UCS VIC 14825 can occupy the server's mezzanine slot at the bottom rear of the chassis. This card's I/O connectors link to Cisco UCS X-Fabric technology. An included bridge card extends this VIC's 2x 50 Gbps of network connections through IFM connectors, bringing the total bandwidth to 100 Gbps per fabric (for a total of 200 Gbps per server). 

  * Cisco UCS VIC 15422 X-Series mezz (UCSX-ME-V5Q50G) 4x25G can occupy the server's mezzanine slot at the bottom rear of the chassis. This card's I/O connectors link to Cisco UCS X-Fabric technology. An included bridge card extends this VIC's 2x 50 Gbps of network connections through IFM connectors, bringing the total bandwidth to 100 Gbps per fabric (for a total of 200 Gbps per server). 

  * Cisco UCS PCI Mezz card for X-Fabric can occupy the server's mezzanine slot at the bottom rear of the chassis. This card's I/O connectors link to Cisco UCS X-Fabric modules and enable connectivity to the X440p PCIe Node. 

  * Security: The server supports an optional trusted platform module (TPM). Additional features include a secure boot FPGA and ACT2 anti-counterfeit provisions 


### Cisco UCS 245 M8 Server

The UCS C245 M8 SFF server extends the capabilities of Cisco’s Unified Computing System portfolio in a 2U form factor with the addition of the AMD CPUs, 12 DIMM slots per CPU for 4800 MT/s DDR5 DIMMs with individual DIMM capacity points up to 256 GB. The maximum memory capacity for 2 CPUs is 6 TB (for 24 x 256 GB DDR5 DIMMs). The Cisco UCS C245 M8 offers Up to 2x 4th Generation AMD Processors with up to 128 cores per processors, 24 DIMM slots (12 DIMMs per CPU socket), up to 4800 MT/s DDR5, Up to 6 TB of capacity. Cisco 24G Tri-mode RAID controller with cache backup to control SAS/SATA/NVMe drives 

The Cisco UCS C245 M8 server can be used standalone, or as part of the Cisco Unified Computing System, which unifies computing, networking, management, virtualization, and storage access into a single integrated architecture enabling end-to-end server visibility, management, and control in both bare metal and virtualized environments. 

### Cisco UCS C240 M7 Server

The Cisco UCS C240 M7 Server is well-suited for a wide range of storage and I/O-intensive applications such as big data analytics, databases, collaboration, virtualization, consolidation, and high-performance computing in its two-socket, 2RU form factor. It incorporates the 4th Gen Intel® Xeon® Scalable Processors with up to 60 cores per socket. 

In addition to the advanced features, the server is also equipped with the PCIe Gen 5.0 for high-speed I/O, a DDR5 memory bus, and expanded storage capabilities (up to 32 DDR5 DIMMs for up to 8 TB of capacity using 128 GB DIMMs (16 DIMMs per socket)) and delivers sigficant performance and efficiency gains that will improve your application performance. 

You can deploy the Cisco UCS C-Series Rack Servers as standalone servers or as part of the Cisco Unified Computing System managed by Cisco Intersight or Intersight Managed Mode. 

### Cisco UCS C220 M7 Server

The Cisco UCS C220 M7 Server is a versatile general-purpose infrastructure and application server. This high-density, 1RU, 2-socket rack server delivers industry-leading performance and efficiency for a wide range of workloads, including virtualization, collaboration, and bare-metal applications. It incorporates the 4th Gen Intel® Xeon® Scalable Processors, with up to 52 cores per socket. With advanced features such as Intel Advanced Matrix Extensions (AMX), Data Streaming Accelerator (DSA), In-Memory Analytics Accelerator (IAA), and QuickAssist Technology (QAT), the server offers significant performance improvements. 

In addition to the advanced features, the server is also equipped with the PCIe Gen 5.0 for high-speed I/O, a DDR5 memory bus, and expanded storage capabilities (up to 32 DDR5 DIMMs for up to 4 TB of capacity using 128 GB DIMMs (16 DIMMs per socket)). 

You can deploy the Cisco UCS C-Series rack servers as standalone servers or as part of the Cisco Unified Computing System™ with the Cisco Intersight Infrastructure Service cloud-based management platform. These computing innovations help reduce Total Cost of Ownership (TCO) and increase their business agility. These improvements deliver significant performance and efficiency gains that improve your application performance. 

### Intelligent Fabric Module (IFM for Cisco UCS X-Series Servers)

Beginning with release 4.3(2a), Cisco UCS Manager supports Cisco UCS X9508 server chassis with Cisco UCS X-Series servers. Cisco UCS X-Series servers support Intelligent Fabric Modules (IFM), which function similarly to the Input/Output Module (IOM) in Cisco UCS B-Series servers. This guide uses the term IOM to refer both IOM and IFM.

### New Cisco UCS VIC Cards

Following new Cisco VIC cards are supported in this release:

  * Cisco UCS VIC 15425

  * Cisco UCS VIC 15235

  * Cisco UCS VIC 15420

  * Cisco UCS VIC 15231

  * Cisco UCS VIC 14425

  * Cisco UCS VIC 15422

  * Cisco UCS VIC 14825


---

## Page 4: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/System-Monitoring/4-3/b-ucsm-gui-system-monitoring-guide-4-3/m_system_monitoring_overview.html

## System Monitoring Overview 

This guide describes how to configure and use system monitoring to manage a Cisco UCS Manager environment. 

Cisco UCS Manager can detect system faults: critical, major, minor, and warnings. We recommend that: 

  * You monitor all faults of either critical or major severity status, as immediate action is not required for minor faults and warnings. 

  * You monitor faults that are not of type Finite State Machine (FSM), as FSM faults will transition over time and resolve. 


This guide covers the following information: 

  * System Log 

  * System logs including faults, failures, and alarm thresholds (Syslog) 

  * The three types of Syslogs: Fault, Event, and Audit logs 

  * The Global Fault Policy and settings that control Syslogs 


  * System Event Log 

  * System hardware events for servers and chassis components and their internal components (System Event Log [SEL] logs) 

  * The SEL policy that controls SEL logs 

  * Simple Network Management Protocol 

  * SNMP for monitoring devices from a central network management station and the host and user settings 

  * Fault suppression policies for SNMP traps, Call Home notifications, and specific devices 

  * Core File Exporter and logs, such as Syslog, Audit Log, and the System Event Log 

  * Statistics Collection and Threshold Policies for adapters, chassis, host, ports, and servers 

  * Call Home and Smart Call Home Cisco embedded device support 

  * Hardware monitoring using the Cisco UCS Manager user interface 

  * Traffic Monitoring sessions for analysis by a network analyzer 

  * Cisco Netflow Monitor for IP network traffic accounting, usage-based network billing, network planning, security, Denial of Service monitoring capabilities, and network monitoring 


---

## Page 5: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/System-Monitoring/4-3/b-ucsm-gui-system-monitoring-guide-4-3/m_syslog.html

## Syslog

Cisco UCS Manager generates system log, or syslog messages to record the following incidents that take place in the Cisco UCS Manager system: 

  * Routine system operations 

  * Failures and errors 

  * Critical and emergency conditions 


There are three kinds of syslog entries: Fault, Event, and Audit. 

Each syslog message identifies the Cisco UCS Manager process that generated the message and provides a brief description of the operation or error that occurred. The syslog is useful both in routine troubleshooting, incident handling, and management. 

Cisco UCS Manager collects and logs syslog messages internally. You can send them to external syslog servers running a syslog daemon. Logging to a central syslog server helps in aggregation of logs and alerts. Some syslog messages to monitor include, DIMM problems, equipment failures, thermal problems, voltage problems, power problems, high availability (HA) cluster problems, and link failures. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The FSM faults, threshold faults, and unresolved policy events are not sent to syslog server. However, SNMP traps are generated for the threshold fault events. 

* * *  
  
---|---  
  
Syslog messages contain an event code and fault code. To monitor syslog messages, you can define syslog message filters. These filters can parse the syslog messages based on the criteria you choose. You can use the following criteria to define a filter: 

  * By event or fault codes: Define a filter with a parsing rule to include only the specific codes that you intend to monitor. Messages that do not match these criteria are discarded. 

  * By severity level: Define a filter with a parsing rule to monitor syslog messages with specific severity levels. You can set syslog severity levels individually for OS functions, to facilitate logging and display of messages ranging from brief summaries to detailed information for debugging. 


Cisco devices can send their log messages to a Unix-style syslog service. A syslog service simply accepts messages, then stores them in files or prints them according to a simple configuration file. This form of logging is the best available for Cisco devices because it can provide protected long-term storage of logs. 

---

## Page 6: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/System-Monitoring/4-3/b-ucsm-gui-system-monitoring-guide-4-3/m_system_event_log.html

## System Event Log 

The System Event Log (SEL) resides on the CIMC in NVRAM. The SEL is used for troubleshooting system health. It records most server-related events, such as instances of over or under voltage, temperature events, fan events, and BIOS events. The types of events supported by SEL include BIOS events, memory unit events, processor events, and motherboard events. 

The SEL logs are stored in the CIMC NVRAM, through a SEL log policy. It is best practice to periodically download and clear the SEL logs. The SEL file is approximately 40KB in size, and no further events can be recorded once it is full. It must be cleared before additional events can be recorded. 

You can use the SEL policy to back up the SEL to a remote server, and optionally to clear the SEL after a backup operation occurs. Backup operations can be triggered based on specific actions, or they can be set to occur at regular intervals. You can also manually back up or clear the SEL. 

The backup file is automatically generated. The filename format is sel-SystemName-ChassisID-ServerID-ServerSerialNumber-Timestamp. 

For example, sel-UCS-A-ch01-serv01-QCI12522939-20091121160736. 

---

## Page 7: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/System-Monitoring/4-3/b-ucsm-gui-system-monitoring-guide-4-3/m_core_file_exporter.html

## Core File Exporter 

Critical failures in the Cisco UCS components, such as a fabric interconnect or an I/O module, can cause the system to create a core dump file. Cisco UCS Manager uses the Core File Exporter to immediately export the core dump files to a specified location on the network through TFTP. This functionality allows you to export the tar file with the contents of the core dump file. The Core File Exporter provides system monitoring and automatic export of core dump files that need to be included in TAC cases. 

---

## Page 8: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/System-Monitoring/4-3/b-ucsm-gui-system-monitoring-guide-4-3/m_audit_logs.html

## Audit Logs

Audit Logs record system events that occurred, where they occurred, and which users initiated them. 

---

## Page 9: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/System-Monitoring/4-3/b-ucsm-gui-system-monitoring-guide-4-3/m_fault_collection_suppression.html

## Global Fault Policy 

The global fault policy controls the lifecycle of a fault in a Cisco UCS domain, including when faults are cleared, the flapping interval (the length of time between the fault being raised and the condition being cleared), and the retention interval (the length of time a fault is retained in the system). 

A fault in Cisco UCS has the following lifecycle: 

  1. A condition occurs in the system and Cisco UCS Manager raises a fault. This is the active state. 

  2. When the fault is alleviated, it enters a flapping or soaking interval that is designed to prevent flapping. Flapping occurs when a fault is raised and cleared several times in rapid succession. During the flapping interval, the fault retains its severity for the length of time specified in the global fault policy. 

  3. If the condition reoccurs during the flapping interval, the fault returns to the active state. If the condition does not reoccur during the flapping interval, the fault is cleared. 

  4. The cleared fault enters the retention interval. This interval ensures that the fault reaches the attention of an administrator even if the condition that caused the fault has been alleviated and the fault has not been deleted prematurely. The retention interval retains the cleared fault for the length of time specified in the global fault policy. 

  5. If the condition reoccurs during the retention interval, the fault returns to the active state. If the condition does not reoccur, the fault is deleted. 


---

## Page 10: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/System-Monitoring/4-3/b-ucsm-gui-system-monitoring-guide-4-3/m_snmp_monitoring.html

## SNMP Overview 

The Simple Network Management Protocol (SNMP) is an application-layer protocol that provides a message format for communication between SNMP managers and agents. SNMP provides a standardized framework and a common language for monitoring and managing devices in a network. 

### SNMP Functional Overview 

The SNMP framework consists of three parts: 

  * An SNMP manager—The system used to control and monitor the activities of network devices using SNMP. 

  * An SNMP agent—The software component within Cisco UCS, the managed device that maintains the data for Cisco UCS, and reports the data as needed to the SNMP manager. Cisco UCS includes the agent and a collection of MIBs. To enable the SNMP agent and create the relationship between the manager and agent, enable and configure SNMP in Cisco UCS Manager. 

  * A managed information base (MIB)—The collection of managed objects on the SNMP agent. Cisco UCS release 1.4(1) and higher supports a larger number of MIBs than earlier releases. 


Cisco UCS supports SNMPv1, SNMPv2c and SNMPv3. Both SNMPv1 and SNMPv2c use a community-based form of security. SNMP is defined in the following: 

  * RFC 3410 (<http://tools.ietf.org/html/rfc3410>) 

  * RFC 3411 (<http://tools.ietf.org/html/rfc3411>) 

  * RFC 3412 (<http://tools.ietf.org/html/rfc3412>) 

  * RFC 3413 (<http://tools.ietf.org/html/rfc3413>) 

  * RFC 3414 (<http://tools.ietf.org/html/rfc3414>) 

  * RFC 3415 (<http://tools.ietf.org/html/rfc3415>) 

  * RFC 3416 (<http://tools.ietf.org/html/rfc3416>) 

  * RFC 3417 (<http://tools.ietf.org/html/rfc3417>) 

  * RFC 3418 (<http://tools.ietf.org/html/rfc3418>) 

  * RFC 3584 (<http://tools.ietf.org/html/rfc3584>) 


### SNMP Notifications 

A key feature of SNMP is the ability to generate notifications from an SNMP agent. These notifications do not require that requests be sent from the SNMP manager. Notifications can indicate improper user authentication, restarts, the closing of a connection, loss of connection to a neighbor router, or other significant events. 

Cisco UCS Manager generates SNMP notifications as either traps or informs. Traps are less reliable than informs because the SNMP manager does not send any acknowledgment when it receives a trap, and Cisco UCS Manager cannot determine if the trap was received. An SNMP manager that receives an inform request acknowledges the message with an SNMP response Protocol Data Unit (PDU). If the Cisco UCS Manager does not receive the PDU, it can send the inform request again. 

### SNMP Security Levels and Privileges 

SNMPv1, SNMPv2c, and SNMPv3 each represent a different security model. The security model combines with the selected security level to determine the security mechanism applied when the SNMP message is processed. 

The security level determines the privileges required to view the message associated with an SNMP trap. The privilege level determines whether the message requires protection from disclosure or whether the message is authenticated. The supported security level depends on which security model is implemented. SNMP security levels support one or more of the following privileges: 

  * noAuthNoPriv—No authentication or encryption 

  * authNoPriv—Authentication but no encryption 

  * authPriv—Authentication and encryption 


SNMPv3 provides for both security models and security levels. A security model is an authentication strategy that is set up for a user and the role in which the user resides. A security level is the permitted level of security within a security model. A combination of a security model and a security level determines which security mechanism is employed when handling an SNMP packet. 

### Supported Combinations of SNMP Security Models and Levels 

The following table identifies the combinations of security models and levels. 

Table 1.  SNMP Security Models and Levels Model  |  Level  |  Authentication  |  Encryption  |  What Happens   
---|---|---|---|---  
v1  |  noAuthNoPriv  |  Community string  |  No  |  Uses a community string match for authentication.   
v2c  |  noAuthNoPriv  |  Community string  |  No  |  Uses a community string match for authentication.   
v3  |  noAuthNoPriv  |  Username  |  No  |  Uses a username match for authentication.   
v3  |  authNoPriv  |  HMAC-MD5 or HMAC-SHA  |  No  |  Provides authentication based on the Hash-Based Message Authentication Code (HMAC) Message Digest 5 (MD5) algorithm or the HMAC Secure Hash Algorithm (SHA).   
v3  |  authPriv  |  HMAC-MD5 or HMAC-SHA  |  DES  |  Provides authentication based on the HMAC-MD5 or HMAC-SHA algorithms. Provides Data Encryption Standard (DES) 56-bit encryption in addition to authentication based on the Cipher Block Chaining (CBC) DES (DES-56) standard.   
  
### SNMPv3 Security Features 

SNMPv3 provides secure access to devices through a combination of authenticating and encrypting frames over the network. SNMPv3 authorizes only configured users to perform management operations and encrypts SNMP messages. The SNMPv3 User-Based Security Model (USM) refers to SNMP message-level security and offers the following services: 

  * Message integrity—Ensures that messages are not altered or destroyed in an unauthorized manner, and that data sequences are not altered beyond what can occur non-maliciously. 

  * Message origin authentication—Ensures that the identity of a message originator is verifiable. 

  * Message confidentiality and encryption—Ensures that information is not made available or disclosed to unauthorized individuals, entities, or processes. 


### SNMP Support in Cisco UCS

Cisco UCS provides the following support for SNMP: 

#### Support for MIBs 

Cisco UCS supports read-only access to MIBs. 

For information about the specific MIBs available for Cisco UCS and where you can obtain them, see the <http://www.cisco.com/en/US/docs/unified_computing/ucs/sw/mib/b-series/b_UCS_MIBRef.html> for B-series servers, and <http://www.cisco.com/en/US/docs/unified_computing/ucs/sw/mib/c-series/b_UCS_Standalone_C-Series_MIBRef.html> C-series servers. 

#### Authentication Protocols for SNMPv3 Users 

Cisco UCS supports the following authentication protocols for SNMPv3 users: 

  * HMAC-MD5-96 (MD5) 

  * HMAC-SHA-96 (SHA) 


#### AES Privacy Protocol for SNMPv3 Users 

Cisco UCS uses Advanced Encryption Standard (AES) as one of the privacy protocols for SNMPv3 message encryption and conforms with RFC 3826. 

The privacy password, or priv option, offers a choice of DES or 128-bit AES encryption for SNMP security encryption. If you enable AES-128 configuration and include a privacy password for an SNMPv3 user, Cisco UCS Manager uses the privacy password to generate a 128-bit AES key. The AES privacy password can have a minimum of eight characters. If the passphrases are specified in clear text, you can specify a maximum of 64 characters. 

To deploy such a user, enable AES-128 encryption. 

---

## Page 11: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/System-Monitoring/4-3/b-ucsm-gui-system-monitoring-guide-4-3/m-spdm-security.html

## SPDM Security

Cisco UCS M6, M7, and M8 servers can contain mutable components that could provide vectors for attack against a device itself or use of a device to attack another device within the system. To defend against these attacks, the Security Protocol and Data Model (SPDM) Specification enables a secure transport implementation that challenges a device to prove its identity and the correctness of its mutable component configuration. 

SPDM defines messages, data objects, and sequences for performing message exchanges between devices over a variety of transport and physical media. It orchestrates message exchanges between Baseboard Management Controllers (BMC) and end-point devices over a Management Component Transport Protocol (MCTP). Message exchanges include authentication of hardware identities accessing the BMC. The SPDM enables access to low-level security capabilities and operations by specifying a managed level for device authentication, firmware measurement, and certificate management. Endpoint devices are challenged to provide authentication. and BMC authenticates the endpoints and only allows access for trusted entities. 

The UCS Manager optionally allows uploads of external security certificates to BMC. A maximum of 40 SPDM certificates is allowed, including native internal certificates. Once the limit is reached, no more certificates can be uploaded. User uploaded certificates can be deleted but internal/default certificates cannot. 

A SPDM security policy allows you to specify one of three Security level settings. Security can be set at one of the three levels listed below: 

  * Full Security:

This is the highest MCTP security setting. When you select this setting, a fault is generated when any endpoint authentication failure or firmware measurement failure is detected. A fault will also be generated if any of the endpoints do not support either endpoint authentication or firmware measurements. 

  * Partial Security (default):

When you select this setting, a fault is generated when any endpoint authentication failure or firmware measurement failure is detected. There will NOT be a fault generated when the endpoint doesn’t support endpoint authentication or firmware measurements. 

  * No Security

When you select this setting, there will NOT be a fault generated for any failure (either endpoint measurement or firmware measurement failures). 


You can also upload the content of one or more external/device certificates into BMC. Using a SPDM policy allows you to change or delete security certificates or settings as desired. Certificates can be deleted or replaced when no longer needed. 

Certificates are listed in all user interfaces on a system. 

---

## Page 12: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/System-Monitoring/4-3/b-ucsm-gui-system-monitoring-guide-4-3/m_statistics_collection_policy.html

## Statistics Collection Policy 

A statistics collection policy defines how frequently statistics are collected (collection interval) and how frequently the statistics are reported (reporting interval). Reporting intervals are longer than collection intervals so that multiple statistical data points can be collected during the reporting interval. This provides Cisco UCS Manager with sufficient data to calculate and report minimum, maximum, and average values. 

For NIC statistics, Cisco UCS Manager displays the average, minimum, and maximum of the change since the last collection of statistics. If the values are 0, there has been no change since the last collection. 

Statistics can be collected and reported for the following five functional areas of the Cisco UCS system: 

  * Adapter — Statistics related to the adapters 

  * Chassis — Statistics related to the chassis 

  * Host — This policy is a placeholder for future support 

  * Port — Statistics related to the ports, including server ports, uplink Ethernet ports, and uplink Fibre Channel ports 

  * Server — Statistics related to servers 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCS Manager has one default statistics collection policy for each of the five functional areas. You cannot create additional statistics collection policies and you cannot delete the existing default policies. You can only modify the default policies.  The values that are displayed for delta counter in Cisco UCS Manager are calculated as the difference between the last two samples in a collection interval. In addition, Cisco UCS Manager displays the average, minimum, and maximum delta values of the samples in the collection interval. 

* * *  
  
---|---

---

## Page 13: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/System-Monitoring/4-3/b-ucsm-gui-system-monitoring-guide-4-3/m_call_home_and_smart_call_home_monitoring.html

##  Call Home in UCS Overview   
  
Call Home provides an email-based notification for critical system policies. A range of message formats are available for compatibility with pager services or XML-based automated parsing applications. You can use this feature to page a network support engineer, email a Network Operations Center, or use Cisco Smart Call Home services to generate a case with the Technical Assistance Center. 

The Call Home feature can deliver alert messages containing information about diagnostics and environmental faults and events. 

The Call Home feature can deliver alerts to multiple recipients, referred to as Call Home destination profiles. Each profile includes configurable message formats and content categories. A predefined destination profile is provided for sending alerts to the Cisco TAC, but you also can define your own destination profiles. 

When you configure Call Home to send messages, Cisco UCS Manager executes the appropriate CLI show command and attaches the command output to the message. 

Cisco UCS delivers Call Home messages in the following formats: 

  * Short text format which provides a one or two line description of the fault that is suitable for pagers or printed reports. 

  * Full text format which provides fully formatted message with detailed information that is suitable for human reading. 

  * XML machine-readable format that uses Extensible Markup Language (XML) and Adaptive Messaging Language (AML) XML Schema Definition (XSD). The AML XSD is published on the [Cisco.com website](http://www.cisco.com). The XML format enables communication with the Cisco Systems Technical Assistance Center. 


For information about the faults that can trigger Call Home email alerts, see the Cisco UCS Faults and Error Messages Reference. 

The following figure shows the flow of events after a Cisco UCS fault is triggered in a system with Call Home configured: 

Figure 1. Flow of Events after a Fault is Triggered  ![Flowchart showing events that can occur after a fault is triggered in a Cisco UCS domain](/c/dam/en/us/td/i/100001-200000/190001-200000/196001-197000/196367.jpg)

### SMTP Authentication

Beginning with release 4.2(3b), UCS Manager supports secured authentication for the transport email with the SMTP server. 

You can toggle SMTP Authentication between 

  * Off—SMTP Authentication is not used for this Cisco UCS domain. 

  * On—SMTP Authentication is used for this Cisco UCS domain. 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

SMTP server should be capable of supporting STARTTLS, SSL based SMTP communication.  You should also install the server root CA certificate on the SMTP-Client (switch) for succesfull connection between SSL to SMTP-AUTH server. 

* * *  
  
---|---

---

## Page 14: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/System-Monitoring/4-3/b-ucsm-gui-system-monitoring-guide-4-3/m_hardware_monitoring.html

## Monitoring a Fabric Interconnect  
  
### Procedure

* * *

**Step 1** |  In the Navigation pane, click Equipment.   
---|---  
**Step 2** |  Expand Equipment > Fabric Interconnects.   
**Step 3** |  Click the node for the fabric interconnect that you want to monitor.   
**Step 4** |  In the Work pane, click one of the following tabs to view the status of the fabric interconnect:  | Option | Description  
---|---  
General tab  |  Provides an overview of the status of the fabric interconnect, including a summary of any faults, a summary of the fabric interconnect properties, and a physical display of the fabric interconnect and its components.   
Physical Ports tab  |  Displays the status of all ports on the fabric interconnect. This tab includes the following subtabs: 

  * Ethernet Ports tab 
  * FC Ports tab 

  
Fans tab  |  Displays the status of all fan modules in the fabric interconnect.   
PSUs tab  |  Displays the status of all power supply units in the fabric interconnect.   
Physical Display tab  |  Provides a graphical view of the fabric interconnect and all ports and other components. If a component has a fault, the fault icon is displayed next to that component.   
FSM tab  |  Provides details about the current FSM task running on the server, including the status of that task. You can use this information to diagnose errors with those tasks.   
Faults tab  |  Provides details of faults generated by the fabric interconnect.   
Events tab  |  Provides details of events generated by the fabric interconnect.   
Neighbors tab  |  Provides details about the LAN, SAN, and LLDP neighbors of the fabric interconnect.  |  **Note** |  Enable Info Policy to view Neighbors details.   
---|---  
Statistics tab  |  Provides statistics about the fabric interconnect and its components. You can view these statistics in tabular or chart format.   
  
* * *

---

## Page 15: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/System-Monitoring/4-3/b-ucsm-gui-system-monitoring-guide-4-3/m_traffic_monitoring.html

## Traffic Monitoring

Traffic monitoring copies traffic from one or more source ports and sends the copied traffic to a dedicated destination port for analysis by a network analyzer. This feature is also known as Switched Port Analyzer (SPAN). 

However, this traffic monitoring is limited to one switch. SPAN can send the traffic between switches, but this traffic cannot be routed. To overcome this problem, support for ERSPAN (Encapsulated Remote Switched Port Analyzer) is provided from Cisco UCS Manager 4.3(4a). 

ERSPAN uses GRE encapsulation, which allows you to route SPAN traffic from a source to a destination in the L3 network.

ERSPAN is used to transport mirrored traffic in an IP network. An origin interface will be created on each Fabric Interconnect with a configured source IP address to forward the packets on the L3 network. A unique IP address per fabric is captured along with the VLAN information. 

### Types of Traffic Monitoring Sessions

There are two types of monitoring sessions: 

  * Ethernet

  * Fibre Channel


The type of destination port determines what kind of monitoring session you need. For an Ethernet traffic monitoring session, the destination port must be an unconfigured physical port. For a Fibre Channel traffic monitoring session, the destination port must be a Fibre Channel uplink port except when you are using Cisco UCS 6536 Fabric Interconnect, Cisco UCS 6454 Fabric Interconnect, Cisco UCS 6400 Series Fabric Interconnect and 6300 Series Fabric Interconnects. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For Cisco UCS 6332, 6332-16UP, 64108, 6454, and 6536 Fabric Interconnects, you cannot choose Fibre Channel destination ports. The destination port must be an unconfigured physical Ethernet port. 

* * *  
  
---|---  
  
### Traffic Monitoring Across Ethernet

An Ethernet traffic monitoring session can monitor any of the following traffic source and destination ports: 

Source Ports  |  Destination Ports   
---|---  
  
  * Uplink Ethernet port 
  * Ethernet port channel 
  * VLAN 
  * Service profile vNIC 
  * Service profile vHBA 
  * FCoE port 
  * Port channels 
  * Unified uplink port 
  * VSAN 

|  Unconfigured Ethernet Port   
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

All traffic sources must be located within the same switch as the destination port. A port configured as a destination port cannot also be configured as a source port. A member port of a port channel cannot be configured individually as a source. If the port channel is configured as a source, all member ports are source ports. 

* * *  
  
---|---  
  
A server port can be a source, only if it is a non-virtualized rack server adapter-facing port. 

### Traffic Monitoring for Cisco UCS 6500,6400 Series Fabric Interconnects 

  * Cisco UCS 6500, 6400 Series Fabric Interconnects do not support a Fibre Channel port as a destination port. Therefore, an Ethernet port is the only option for configuring any traffic monitoring session on this Fabric Interconnect. 

  * Cisco UCS 6500, 6400 Series Fabric Interconnects support monitoring traffic in the transmit direction for more than two sources per Fabric Interconnect. 

  * You can monitor or use SPAN on port channels sources for traffic in the transmit and receive directions.

  * You can configure a port as a destination port for only one monitor session.

  * You can monitoring Port-Channel as a source in the transmit direction.

  * You cannot monitor vEth as a source in the transmit direction.


### Traffic Monitoring for Cisco UCS 6300 Fabric Interconnects

  * Cisco UCS 6300 Fabric Interconnect supports port-based mirroring.

  * Cisco UCS 6300 Fabric Interconnects support VLAN SPAN only in the receive direction. 

  * Ethernet SPAN is port based on the Cisco UCS 6300 Fabric Interconnect. 


### Traffic Monitoring Across Fibre Channel

You can monitor Fibre Channel traffic using either a Fibre Channel traffic analyzer or an Ethernet traffic analyzer. When Fibre Channel traffic is monitored with an Ethernet traffic monitoring session, at an Ethernet destination port, the destination traffic is FCoE. The Cisco UCS 6300 Fabric Interconnect supports FC SPAN only on the ingress side. 

A Fibre Channel traffic monitoring session can monitor any of the following traffic source and destination ports: 

Source Ports  |  Destination Ports   
---|---  
  
  * FC Port 
  * FC Port Channel 
  * Uplink Fibre Channel port 
  * SAN port channel 
  * VSAN 
  * Service profile vHBA 
  * Fibre Channel storage port 

| 

  * Fibre Channel uplink port 
  * Unconfigured Ethernet Port (Cisco UCS 6536, 64108, 6454, 6332, and 6332-16UP Fabric Interconnects) 


---

## Page 16: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/System-Monitoring/4-3/b-ucsm-gui-system-monitoring-guide-4-3/m_netflow_monitoring.html

## NetFlow Monitoring  
  
NetFlow is a standard network protocol for collecting IP traffic data. NetFlow enables you to define a flow in terms of unidirectional IP packets that share certain characteristics. All packets that match the flow definition are collected and exported to one or more external NetFlow Collectors, where they can be further aggregated, analyzed, and used for application-specific processing. 

Cisco UCS Manager uses NetFlow-capable adapters (Cisco UCS Cisco UCS VIC 1300 series, Cisco UCS VIC 1400 series, Cisco UCS VIC 14000 series, and Cisco UCS VIC 15000 series) to communicate with the routers and switches that collect and export flow information. 

Starting from 4.3(2b) release, NetFlow monitoring is supported on Cisco UCS 6400 and 6500 series Fabric Interconnects. 

Starting from 4.3(4b) release, NetFlow monitoring is supported on Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct). 

### Network Flows

A flow is a set of unidirectional IP packets that have common properties such as, the source or destination of the traffic, routing information, and protocol used. Flows are collected when they match the definitions in the flow record definition. 

### Flow Record Definitions

A flow record definition contains information about the properties used to define the flow, which can include both characteristic properties or measured properties. Characteristic properties, also called flow keys, are the properties that define the flow. Cisco UCS Manager supports IPv4, IPv6, and Layer 2 keys. Measured characteristics, also called flow values or non-keys, measurable values such as the number of bytes contained in all packets of the flow, or the total number of packets. 

A flow record definition is a specific combination of flow keys and flow values. The two types of flow record definitions are: 

  * System-defined—Default flow record definitions supplied by Cisco UCS Manager. 

  * User-defined—Flow record definitions that you can create yourself. 


### Flow Exporters, Flow Exporter Profiles, and Flow Collectors

Flow exporters transfer the flows to the flow connector based on the information in a flow exporter profile. The flow exporter profile contains the networking properties used to export NetFlow packets. The networking properties include a VLAN, the source IP address, and the subnet mask for each fabric interconnect. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

In the Cisco UCS Manager GUI, the networking properties are defined in an exporter interface that is included in the profile. In the Cisco UCS Manager CLI, the properties are defined in the profile. 

* * *  
  
---|---  
  
Flow collectors receive the flows from the flow exporter. Each flow collector contains an IP address, port, external gateway IP, and VLAN that defines where the flows are sent. 

### Flow Monitors and Flow Monitor Sessions

A flow monitor consists of a flow definition, one or two flow exporters, and a timeout policy. You can use a flow monitor to specify which flow information you want to gather, and where you want to collect it from. Each flow monitor operates in either the egress or ingress direction. 

A flow monitor session contains up to four flow monitors: two flow monitors in the ingress direction and two flow monitors in the egress direction. A flow monitor session can also be associated with a vNIC. 

---

## Page 17: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/System-Monitoring/4-3/m_hardware_monitoring.html

## Monitoring a Fabric Interconnect

### Procedure

* * *

**Step 1** |  In the Navigation pane, click Equipment.   
---|---  
**Step 2** |  Expand Equipment > Fabric Interconnects.   
**Step 3** |  Click the node for the fabric interconnect that you want to monitor.   
**Step 4** |  In the Work pane, click one of the following tabs to view the status of the fabric interconnect:  | Option | Description  
---|---  
General tab  |  Provides an overview of the status of the fabric interconnect, including a summary of any faults, a summary of the fabric interconnect properties, and a physical display of the fabric interconnect and its components.   
Physical Ports tab  |  Displays the status of all ports on the fabric interconnect. This tab includes the following subtabs: 

  * Ethernet Ports tab 
  * FC Ports tab 

  
Fans tab  |  Displays the status of all fan modules in the fabric interconnect.   
PSUs tab  |  Displays the status of all power supply units in the fabric interconnect.   
Physical Display tab  |  Provides a graphical view of the fabric interconnect and all ports and other components. If a component has a fault, the fault icon is displayed next to that component.   
FSM tab  |  Provides details about the current FSM task running on the server, including the status of that task. You can use this information to diagnose errors with those tasks.   
Faults tab  |  Provides details of faults generated by the fabric interconnect.   
Events tab  |  Provides details of events generated by the fabric interconnect.   
Neighbors tab  |  Provides details about the LAN, SAN, and LLDP neighbors of the fabric interconnect.  |  **Note** |  Enable Info Policy to view Neighbors details.   
---|---  
Statistics tab  |  Provides statistics about the fabric interconnect and its components. You can view these statistics in tabular or chart format.   
  
* * *

---

## Page 18: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/System-Monitoring/4-3/m_syslog.html

## Syslog

Cisco UCS Manager generates system log, or syslog messages to record the following incidents that take place in the Cisco UCS Manager system: 

  * Routine system operations 

  * Failures and errors 

  * Critical and emergency conditions 


There are three kinds of syslog entries: Fault, Event, and Audit. 

Each syslog message identifies the Cisco UCS Manager process that generated the message and provides a brief description of the operation or error that occurred. The syslog is useful both in routine troubleshooting, incident handling, and management. 

Cisco UCS Manager collects and logs syslog messages internally. You can send them to external syslog servers running a syslog daemon. Logging to a central syslog server helps in aggregation of logs and alerts. Some syslog messages to monitor include, DIMM problems, equipment failures, thermal problems, voltage problems, power problems, high availability (HA) cluster problems, and link failures. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The FSM faults, threshold faults, and unresolved policy events are not sent to syslog server. However, SNMP traps are generated for the threshold fault events. 

* * *  
  
---|---  
  
Syslog messages contain an event code and fault code. To monitor syslog messages, you can define syslog message filters. These filters can parse the syslog messages based on the criteria you choose. You can use the following criteria to define a filter: 

  * By event or fault codes: Define a filter with a parsing rule to include only the specific codes that you intend to monitor. Messages that do not match these criteria are discarded. 

  * By severity level: Define a filter with a parsing rule to monitor syslog messages with specific severity levels. You can set syslog severity levels individually for OS functions, to facilitate logging and display of messages ranging from brief summaries to detailed information for debugging. 


Cisco devices can send their log messages to a Unix-style syslog service. A syslog service simply accepts messages, then stores them in files or prints them according to a simple configuration file. This form of logging is the best available for Cisco devices because it can provide protected long-term storage of logs. 

---

## Page 19: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/System-Monitoring/4-3/m_call_home_and_smart_call_home_monitoring.html

##  Call Home in UCS Overview 

Call Home provides an email-based notification for critical system policies. A range of message formats are available for compatibility with pager services or XML-based automated parsing applications. You can use this feature to page a network support engineer, email a Network Operations Center, or use Cisco Smart Call Home services to generate a case with the Technical Assistance Center. 

The Call Home feature can deliver alert messages containing information about diagnostics and environmental faults and events. 

The Call Home feature can deliver alerts to multiple recipients, referred to as Call Home destination profiles. Each profile includes configurable message formats and content categories. A predefined destination profile is provided for sending alerts to the Cisco TAC, but you also can define your own destination profiles. 

When you configure Call Home to send messages, Cisco UCS Manager executes the appropriate CLI show command and attaches the command output to the message. 

Cisco UCS delivers Call Home messages in the following formats: 

  * Short text format which provides a one or two line description of the fault that is suitable for pagers or printed reports. 

  * Full text format which provides fully formatted message with detailed information that is suitable for human reading. 

  * XML machine-readable format that uses Extensible Markup Language (XML) and Adaptive Messaging Language (AML) XML Schema Definition (XSD). The AML XSD is published on the [Cisco.com website](http://www.cisco.com). The XML format enables communication with the Cisco Systems Technical Assistance Center. 


For information about the faults that can trigger Call Home email alerts, see the Cisco UCS Faults and Error Messages Reference. 

The following figure shows the flow of events after a Cisco UCS fault is triggered in a system with Call Home configured: 

Figure 1. Flow of Events after a Fault is Triggered  ![Flowchart showing events that can occur after a fault is triggered in a Cisco UCS domain](/c/dam/en/us/td/i/100001-200000/190001-200000/196001-197000/196367.jpg)

### SMTP Authentication

Beginning with release 4.2(3b), UCS Manager supports secured authentication for the transport email with the SMTP server. 

You can toggle SMTP Authentication between 

  * Off—SMTP Authentication is not used for this Cisco UCS domain. 

  * On—SMTP Authentication is used for this Cisco UCS domain. 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

SMTP server should be capable of supporting STARTTLS, SSL based SMTP communication.  You should also install the server root CA certificate on the SMTP-Client (switch) for succesfull connection between SSL to SMTP-AUTH server. 

* * *  
  
---|---

---

## Page 20: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/System-Monitoring/4-3/m_netflow_monitoring.html

## NetFlow Monitoring  
  
NetFlow is a standard network protocol for collecting IP traffic data. NetFlow enables you to define a flow in terms of unidirectional IP packets that share certain characteristics. All packets that match the flow definition are collected and exported to one or more external NetFlow Collectors, where they can be further aggregated, analyzed, and used for application-specific processing. 

Cisco UCS Manager uses NetFlow-capable adapters (Cisco UCS Cisco UCS VIC 1300 series, Cisco UCS VIC 1400 series, Cisco UCS VIC 14000 series, and Cisco UCS VIC 15000 series) to communicate with the routers and switches that collect and export flow information. 

Starting from 4.3(2b) release, NetFlow monitoring is supported on Cisco UCS 6400 and 6500 series Fabric Interconnects. 

Starting from 4.3(4b) release, NetFlow monitoring is supported on Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct). 

### Network Flows

A flow is a set of unidirectional IP packets that have common properties such as, the source or destination of the traffic, routing information, and protocol used. Flows are collected when they match the definitions in the flow record definition. 

### Flow Record Definitions

A flow record definition contains information about the properties used to define the flow, which can include both characteristic properties or measured properties. Characteristic properties, also called flow keys, are the properties that define the flow. Cisco UCS Manager supports IPv4, IPv6, and Layer 2 keys. Measured characteristics, also called flow values or non-keys, measurable values such as the number of bytes contained in all packets of the flow, or the total number of packets. 

A flow record definition is a specific combination of flow keys and flow values. The two types of flow record definitions are: 

  * System-defined—Default flow record definitions supplied by Cisco UCS Manager. 

  * User-defined—Flow record definitions that you can create yourself. 


### Flow Exporters, Flow Exporter Profiles, and Flow Collectors

Flow exporters transfer the flows to the flow connector based on the information in a flow exporter profile. The flow exporter profile contains the networking properties used to export NetFlow packets. The networking properties include a VLAN, the source IP address, and the subnet mask for each fabric interconnect. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

In the Cisco UCS Manager GUI, the networking properties are defined in an exporter interface that is included in the profile. In the Cisco UCS Manager CLI, the properties are defined in the profile. 

* * *  
  
---|---  
  
Flow collectors receive the flows from the flow exporter. Each flow collector contains an IP address, port, external gateway IP, and VLAN that defines where the flows are sent. 

### Flow Monitors and Flow Monitor Sessions

A flow monitor consists of a flow definition, one or two flow exporters, and a timeout policy. You can use a flow monitor to specify which flow information you want to gather, and where you want to collect it from. Each flow monitor operates in either the egress or ingress direction. 

A flow monitor session contains up to four flow monitors: two flow monitors in the ingress direction and two flow monitors in the egress direction. A flow monitor session can also be associated with a vNIC. 

---

## Page 21: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/System-Monitoring/4-3/m_traffic_monitoring.html

## Traffic Monitoring

Traffic monitoring copies traffic from one or more source ports and sends the copied traffic to a dedicated destination port for analysis by a network analyzer. This feature is also known as Switched Port Analyzer (SPAN). 

However, this traffic monitoring is limited to one switch. SPAN can send the traffic between switches, but this traffic cannot be routed. To overcome this problem, support for ERSPAN (Encapsulated Remote Switched Port Analyzer) is provided from Cisco UCS Manager 4.3(4a). 

ERSPAN uses GRE encapsulation, which allows you to route SPAN traffic from a source to a destination in the L3 network.

ERSPAN is used to transport mirrored traffic in an IP network. An origin interface will be created on each Fabric Interconnect with a configured source IP address to forward the packets on the L3 network. A unique IP address per fabric is captured along with the VLAN information. 

### Types of Traffic Monitoring Sessions

There are two types of monitoring sessions: 

  * Ethernet

  * Fibre Channel


The type of destination port determines what kind of monitoring session you need. For an Ethernet traffic monitoring session, the destination port must be an unconfigured physical port. For a Fibre Channel traffic monitoring session, the destination port must be a Fibre Channel uplink port except when you are using Cisco UCS 6536 Fabric Interconnect, Cisco UCS 6454 Fabric Interconnect, Cisco UCS 6400 Series Fabric Interconnect and 6300 Series Fabric Interconnects. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For Cisco UCS 6332, 6332-16UP, 64108, 6454, and 6536 Fabric Interconnects, you cannot choose Fibre Channel destination ports. The destination port must be an unconfigured physical Ethernet port. 

* * *  
  
---|---  
  
### Traffic Monitoring Across Ethernet

An Ethernet traffic monitoring session can monitor any of the following traffic source and destination ports: 

Source Ports  |  Destination Ports   
---|---  
  
  * Uplink Ethernet port 
  * Ethernet port channel 
  * VLAN 
  * Service profile vNIC 
  * Service profile vHBA 
  * FCoE port 
  * Port channels 
  * Unified uplink port 
  * VSAN 

|  Unconfigured Ethernet Port   
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

All traffic sources must be located within the same switch as the destination port. A port configured as a destination port cannot also be configured as a source port. A member port of a port channel cannot be configured individually as a source. If the port channel is configured as a source, all member ports are source ports. 

* * *  
  
---|---  
  
A server port can be a source, only if it is a non-virtualized rack server adapter-facing port. 

### Traffic Monitoring for Cisco UCS 6500,6400 Series Fabric Interconnects 

  * Cisco UCS 6500, 6400 Series Fabric Interconnects do not support a Fibre Channel port as a destination port. Therefore, an Ethernet port is the only option for configuring any traffic monitoring session on this Fabric Interconnect. 

  * Cisco UCS 6500, 6400 Series Fabric Interconnects support monitoring traffic in the transmit direction for more than two sources per Fabric Interconnect. 

  * You can monitor or use SPAN on port channels sources for traffic in the transmit and receive directions.

  * You can configure a port as a destination port for only one monitor session.

  * You can monitoring Port-Channel as a source in the transmit direction.

  * You cannot monitor vEth as a source in the transmit direction.


### Traffic Monitoring for Cisco UCS 6300 Fabric Interconnects

  * Cisco UCS 6300 Fabric Interconnect supports port-based mirroring.

  * Cisco UCS 6300 Fabric Interconnects support VLAN SPAN only in the receive direction. 

  * Ethernet SPAN is port based on the Cisco UCS 6300 Fabric Interconnect. 


### Traffic Monitoring Across Fibre Channel

You can monitor Fibre Channel traffic using either a Fibre Channel traffic analyzer or an Ethernet traffic analyzer. When Fibre Channel traffic is monitored with an Ethernet traffic monitoring session, at an Ethernet destination port, the destination traffic is FCoE. The Cisco UCS 6300 Fabric Interconnect supports FC SPAN only on the ingress side. 

A Fibre Channel traffic monitoring session can monitor any of the following traffic source and destination ports: 

Source Ports  |  Destination Ports   
---|---  
  
  * FC Port 
  * FC Port Channel 
  * Uplink Fibre Channel port 
  * SAN port channel 
  * VSAN 
  * Service profile vHBA 
  * Fibre Channel storage port 

| 

  * Fibre Channel uplink port 
  * Unconfigured Ethernet Port (Cisco UCS 6536, 64108, 6454, 6332, and 6332-16UP Fabric Interconnects) 


---
