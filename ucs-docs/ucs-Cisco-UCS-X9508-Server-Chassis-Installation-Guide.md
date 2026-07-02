# Cisco UCS X9508 Chassis Installation and Service Guide

| | |
|---|---|
| **URL Title** | Cisco UCS X9508 Chassis Installation and Service Guide |
| **URL** | https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x9508/install/b-ucs-x9508-install.html |
| **Long URL** |  |
| **HTML Title** | Cisco UCS X9508 Server Chassis Installation Guide |
| **Source file** | `ucs-docs-raw/html/b-ucs-x9508-install.html` |
| **File type** | HTML |
| **Fetched on** | 2026-07-02 13:04:43 |

---

## Page 1: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x9508/install/b-ucs-x9508-install.html

![Clear Contents of Search](/etc/designs/cdc/fw/i/ic_clear_gray.png)

---

## Page 2: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x9508/install/b-ucs-x9508-install/m-preface.html

# Preface

This preface contains the following topics:

## Bias-Free Documentation

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The documentation set for this product strives to use bias-free language. For purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on standards documentation, or language that is used by a referenced third-party product. 

* * *  
  
---|---  
  
## Full Cisco Trademarks with Hardware License

THE SPECIFICATIONS AND INFORMATION REGARDING THE PRODUCTS IN THIS MANUAL ARE SUBJECT TO CHANGE WITHOUT NOTICE. ALL STATEMENTS, INFORMATION, AND RECOMMENDATIONS IN THIS MANUAL ARE BELIEVED TO BE ACCURATE BUT ARE PRESENTED WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. USERS MUST TAKE FULL RESPONSIBILITY FOR THEIR APPLICATION OF ANY PRODUCTS. 

THE SOFTWARE LICENSE AND LIMITED WARRANTY FOR THE ACCOMPANYING PRODUCT ARE SET FORTH IN THE INFORMATION PACKET THAT SHIPPED WITH THE PRODUCT AND ARE INCORPORATED HEREIN BY THIS REFERENCE. IF YOU ARE UNABLE TO LOCATE THE SOFTWARE LICENSE OR LIMITED WARRANTY, CONTACT YOUR CISCO REPRESENTATIVE FOR A COPY. 

The following information is for FCC compliance of Class A devices: This equipment has been tested and found to comply with the limits for a Class A digital device, pursuant to part 15 of the FCC rules. These limits are designed to provide reasonable protection against harmful interference when the equipment is operated in a commercial environment. This equipment generates, uses, and can radiate radio-frequency energy and, if not installed and used in accordance with the instruction manual, may cause harmful interference to radio communications. Operation of this equipment in a residential area is likely to cause harmful interference, in which case users will be required to correct the interference at their own expense. 

The following information is for FCC compliance of Class B devices: This equipment has been tested and found to comply with the limits for a Class B digital device, pursuant to part 15 of the FCC rules. These limits are designed to provide reasonable protection against harmful interference in a residential installation. This equipment generates, uses and can radiate radio frequency energy and, if not installed and used in accordance with the instructions, may cause harmful interference to radio communications. However, there is no guarantee that interference will not occur in a particular installation. If the equipment causes interference to radio or television reception, which can be determined by turning the equipment off and on, users are encouraged to try to correct the interference by using one or more of the following measures: 

  * Reorient or relocate the receiving antenna. 

  * Increase the separation between the equipment and receiver. 

  * Connect the equipment into an outlet on a circuit different from that to which the receiver is connected. 

  * Consult the dealer or an experienced radio/TV technician for help. 


Modifications to this product not authorized by Cisco could void the FCC approval and negate your authority to operate the product. 

The Cisco implementation of TCP header compression is an adaptation of a program developed by the University of California, Berkeley (UCB) as part of UCB’s public domain version of the UNIX operating system. All rights reserved. Copyright © 1981, Regents of the University of California. 

NOTWITHSTANDING ANY OTHER WARRANTY HEREIN, ALL DOCUMENT FILES AND SOFTWARE OF THESE SUPPLIERS ARE PROVIDED "AS IS" WITH ALL FAULTS. CISCO AND THE ABOVE-NAMED SUPPLIERS DISCLAIM ALL WARRANTIES, EXPRESSED OR IMPLIED, INCLUDING, WITHOUT LIMITATION, THOSE OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT OR ARISING FROM A COURSE OF DEALING, USAGE, OR TRADE PRACTICE. 

IN NO EVENT SHALL CISCO OR ITS SUPPLIERS BE LIABLE FOR ANY INDIRECT, SPECIAL, CONSEQUENTIAL, OR INCIDENTAL DAMAGES, INCLUDING, WITHOUT LIMITATION, LOST PROFITS OR LOSS OR DAMAGE TO DATA ARISING OUT OF THE USE OR INABILITY TO USE THIS MANUAL, EVEN IF CISCO OR ITS SUPPLIERS HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. 

Any Internet Protocol (IP) addresses and phone numbers used in this document are not intended to be actual addresses and phone numbers. Any examples, command display output, network topology diagrams, and other figures included in the document are shown for illustrative purposes only. Any use of actual IP addresses or phone numbers in illustrative content is unintentional and coincidental. 

All printed copies and duplicate soft copies of this document are considered uncontrolled. See the current online version for the latest version. 

Cisco has more than 200 offices worldwide. Addresses and phone numbers are listed on the Cisco website at www.cisco.com/go/offices.

Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries. To view a list of Cisco trademarks, go to this URL: <https://www.cisco.com/c/en/us/about/legal/trademarks.html>. Third-party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (1721R) 

## Communications, Services, and Additional Information

  * To receive timely, relevant information from Cisco, sign up at [Cisco Profile Manager](https://www.cisco.com/offer/subscribe). 

  * To get the business impact you’re looking for with the technologies that matter, visit [Cisco Services](https://www.cisco.com/go/services). 

  * To submit a service request, visit [Cisco Support](https://www.cisco.com/c/en/us/support/index.html). 

  * To discover and browse secure, validated enterprise-class apps, products, solutions and services, visit [Cisco Marketplace](https://developer.cisco.com/site/marketplace/). 

  * To obtain general networking, training, and certification titles, visit [Cisco Press](http://www.ciscopress.com). 

  * To find warranty information for a specific product or product family, access [Cisco Warranty Finder](http://www.cisco-warrantyfinder.com). 


### Cisco Bug Search Tool

[Cisco Bug Search Tool](https://www.cisco.com/c/en/us/support/web/tools/bst/bsthelp/index.html) (BST) is a web-based tool that acts as a gateway to the Cisco bug tracking system that maintains a comprehensive list of defects and vulnerabilities in Cisco products and software. BST provides you with detailed defect information about your products and software. 

---

## Page 3: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x9508/install/b-ucs-x9508-install/m-ucsx-9508-chassis-overview.html

# Overview

This chapter contains the following topics:

## System Overview 

The Cisco UCS X9508 Server Chassis and its components are part of the Cisco Unified Computing System (UCS). This system can use multiple server chassis configurations along with the Cisco UCS Fabric Interconnects to provide advanced options and capabilities in server and data management. The following configuration options are supported: 

  * All Cisco UCS compute nodes. In a compute node-only configuration, two Intelligent Fabric Modules (IFMs) are required.

  * A mix of Cisco UCS compute nodes and Cisco UCS PCIe Nodes. In this configuration, the compute nodes are paired with Cisco UCS PCIe nodes. 

  * With the Cisco UCS X440p PCIe Node, an M7 generation compute node is paired 1:1.

  * With the Cisco UCS X580p PCIe node, up to two M8 generation compute nodes can be paired with each PCIe node.

  * Two Intelligent Fabric Modules (IFMs) and two Cisco X9416 X-Fabric Modules (XFMs) or Cisco X9516 X-Fabric Modules are required in each UCS X9508 chassis for full performance. 


Either servers or compute nodes, and PCIe nodes are managed through the GUI or API with Cisco Intersight. 

The Cisco UCS X9508 Server Chassis system consists of the following components: 

  * Chassis versions: 

  * Cisco UCS X9508 server chassis–AC version 

  * Intelligent Fabric Modules (IFMs), two deployed as a pair:

  * Cisco UCS 9108 100G IFMs (UCSX-I-9108-100G)—Two I/O modules, each with 8 100 Gigabit QSFP28 optical ports

  * Cisco UCS 9108 25G IFMs (UCSX-I-9108-25G)—Two I/O modules, each with 8 25 Gigabit SFP28 optical ports 

  * X-Fabric Modules:

  * Two UCS X9416 XFMs are required in each UCS X9508 server chassis to support GPU acceleration through Cisco UCS X440p PCIe nodes. 

  * Two UCS X9516 XFMs are required in each UCS X9508 server chassis to support GPU acceleration through Cisco UCS X580p PCIe nodes. 

  * Power supplies—Up to six 2800 Watt, hot-swappable power supplies 

  * Fan modules—Four hot-swappable fan modules 

  * Up to 8 UCS X Series compute nodes of M6 or M7 generation for PCIe Gen4 connectivity through the X9416 XFMs, or up to 8 UCS X series compute nodes of M8 generation for PCIe Gen5 connectivity through the UCS X516 XFMs. 

  * Up to 4 UCS X-Series M6 or M7 compute nodes paired 1:1 with up to 4 Cisco UCS X440p PCIe Nodes and two UCS X9416 XFMs for PCIe Gen4 connectivity. 

  * Up to 4 UCS X-Series M8 compute nodes paired with up to 2 Cisco UCS X580p PCIe Nodes and two UCS X516 XFMs for PCIe Gen5 connectivity. 


The following figures show the server chassis front and back.  Figure 1. Cisco UCS X9508 Server Chassis, Front  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308909.jpg) 1 |  System LEDs:

  * Locator LED/Button
  * System Status LED
  * Network Link LED

For information about System LEDs, see LEDs.  |  2 |  Node Slots, a total of 8. Shown populated with compute nodes, but can also contain PCIe Nodes  
---|---|---|---  
3 |  Power Supplies, a maximum of 6.  |  4 |  System Asset Tag  
5 |  System side panels (two), which are removable. The side panels cover the rack mounting brackets.  |  |   
Figure 2. Cisco UCS X9508 Server Chassis, Rear  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308910.jpg) 1 |  Power Entry Modules (PEMs) for facility inlet power Each PEM contains 3 IEC 320 C20 inlets. 

  * PEM 1 is at the top of the chassis, and it supports IEC inlets 1 through 3, with inlet 1 at the top of PEM 1.
  * PEM 2 is at the bottom of chassis, and it supports IEC inlets 4 through 6, with inlet 4 at the top of PEM 2

|  2 |  Intelligent Fabric Modules (shown populated), which are always deployed as a pair of the following:

  * Cisco UCS 9108 100G modules
  * Cisco UCS 9108 25G modules

  
---|---|---|---  
3 |  System fans (four)  |  4 |  X-Fabric Module slots for either UCS active filler panels (for compute nodes) or up to two UCS X-Fabric Modules (for compute nodes paired with PCIe nodes).   
  
## Features and Benefits

The Cisco UCS X9508 server chassis revolutionizes the use and deployment of compute-node and PCIe-node based systems. By incorporating unified fabric, cloud native management, and X-Fabric technology, the Cisco Unified Computing System enables the chassis to have fewer physical components, no independent management, and to be more energy efficient than traditional blade server chassis. 

This simplicity eliminates the need for dedicated chassis management and blade switches, reduces cabling, and enables the Cisco Unified Computing System to scale to 20 chassis without adding complexity. The Cisco UCS X9508 server chassis is a critical component in delivering the Cisco Unified Computing System benefits of data center simplicity and IT responsiveness. 

Table 1. Features and Benefits Feature  |  Benefit   
---|---  
Management by Cisco Intersight  |  Reduces total cost of ownership by removing management modules from the chassis, making the chassis stateless.  Provides a single, highly available cloud-based management tool for all server chassis, IFMs, XFMs, and nodes, thus reducing administrative tasks.   
Unified fabric  |  Decreases TCO by reducing the number of network interface cards (NICs), host bus adapters (HBAs), switches, and cables needed.   
Support for two UCS I/O Modules  |  Eliminates switches from the chassis, including the complex configuration and management of those switches, allowing a system to scale without adding complexity and cost.  Allows use of two I/O modules for redundancy or aggregation of bandwidth.   
Auto discovery  |  Requires no configuration; like all components in the Cisco Unified Computing System, chassis are automatically recognized and configured by Cisco Intersight.   
Direct node to fabric connectivity |  Provides reconfigurable chassis to accommodate a variety of form factors and functions, which supports investment protection for new fabrics and future compute and PCIe nodes.  Provides IFM-to-compute node connectivity to chassis through an Ortho-Direct connection.  Provides 8 nodes with 200 Gbps (dual 25G-PAM4-ETH x8 lanes) of available Ethernet fabric throughput for each compute node. The system is designed to support higher potential Ethernet fabric throughput for future and emerging technologies, such as 112 GbpsPAM4 Ethernet.  Provides 8 nodes with 200 Gbps (dual 16G-PCIe x 16 lanes) of available PCIe fabric throughput for each compute node. The system is designed to support higher potential Ethernet fabric throughput for future and emerging technologies, such as 32 Gbps PCIe Gen5.   
Redundant hot swappable power supplies and fans  |  Provides high availability in multiple configurations.  Increases serviceability.  Provides uninterrupted service during maintenance.  Available configured for AC environments (mixing not supported)   
Hot-pluggable compute nodes and intelligent fabric modules  |  Provides uninterrupted service during maintenance and server deployment.   
Comprehensive monitoring  |  Provides extensive environmental monitoring on each chassis  Allows use of user thresholds to optimize environmental management of the chassis.   
Efficient front-to-back airflow  |  Helps reduce power consumption and increase component reliability.   
Tool-free installation  |  Requires no specialized tools for chassis installation.  Provides mounting rails for easy installation and servicing.   
Node configurations  |  Allows up to 8 UCS compute nodes or up to 4 compute nodes paired with either 4 UCS X440p PCIe Nodes (Gen4 support) or two UCS X580p PCIe Nodes (Gen 5 support)   
  
## Chassis Components

This section lists an overview of chassis components.

  * Cisco UCS X9508 Server Chassis


### Cisco UCS X9508 Server Chassis

The Cisco UCS X9508 Series server chassis is a scalable and flexible chassis for today’s and tomorrow’s data center that helps reduce total cost of ownership. 

The chassis is seven rack units (7 RU) high and can mount in an industry-standard 19-inch rack with square holes for use with cage nuts or round-holes for use with spring nuts. The chassis can house up to eight Cisco UCS nodes. 

Up to six hot-swappable AC power supplies are accessible from the front of the chassis. These power supplies can be configured to support nonredundant, N+1 redundant, N+2 redundant, and grid-redundant configurations. The rear of the chassis contains four hot-swappable fans, six power connectors (one per power supply), two horizontal top slots for Intelligent Fabric Modules (IFM1, IFM2), and two additional horizontal bottom slots for X-Fabric modules (XFM1, XFM2). 

Scalability is dependent on both hardware and software. For more information, see the appropriate [UCS software release notes](http://www.cisco.com/en/US/products/ps10281/prod_release_notes_list.html). 

## Compute Nodes

The Cisco UCS X Series compute nodes are based on industry-standard server technologies and provide the following: 

  * Up to two Intel multi-core processors

  * Front-accessible, hot-swappable NVMe drives or solid-state disk (SSD) drives 

  * Depending on the compute node, support is available for up to two adapter card connections for up to 200 Gbps of redundant I/O throughput 

  * Industry-standard double-data-rate 4 (DDR4) memory (M6 and M7 compute nodes) or DDR5 memory (M8 compute nodes)

  * Remote management through an integrated service processor that also executes policy established in Cisco Intersight cloud-based server management 

  * Local keyboard, video, and mouse (KVM) and serial console access through a front console port on each compute node 


  * Cisco UCS X210c M6 Compute Node
  * Cisco UCS X210c M7 Compute Nodes
  * Cisco UCS X410c M7 Compute Nodes
  * Cisco UCS X440p PCIe Nodes
  * Cisco UCS X210c M8 Compute Nodes
  * Cisco UCS X215c M8 Compute Nodes
  * Cisco UCS X580p PCIe Nodes


### Cisco UCS X210c M6 Compute Node

The Cisco UCS X210c M6 is a two-socket compute node that hosts a maximum of two M6 CPUs. This compute node is supported in the Cisco UCS X9508 server chassis, which provides power and cooling. Data interconnect for the compute node to other data center equipment is supported through Intelligent Fabric Modules in the same server chassis. 

Each Cisco UCS X210c M6 compute node has Cisco-standard indicators on the face of the module. Indicators are grouped for module-level information, and drive-level indicators. 

Figure 3. Cisco UCS X210c M6 Compute Node  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308977.jpg)

### Cisco UCS X210c M7 Compute Nodes

The Cisco UCS X210c M7 Compute Node is the computing device to integrate into the Cisco UCS X-Series Modular System. Up to eight compute nodes can reside in the 7-Rack-Unit (7RU) Cisco UCS X9508 Chassis, offering one of the highest densities of compute, IO, and storage per rack unit in the industry. 

The Cisco UCS X210c M7 Compute Node harnesses the power of up to two 5th Generation Intel® Xeon® Scalable Processors with up to 64 cores per processor or up to 2x 4th Generation Intel® Xeon® Scalable Processors with up to 60 cores per processor. 

The compute node supports up to 6 hot-pluggable, Solid-State Drives (SSDs), or Non-Volatile Memory Express (NVMe 2.5-inch drives with a choice of enterprise-class RAID or pass-through controllers with four lanes each of PCIe Gen 4 connectivity and up to 2 M.2 SATA or NVMe drives for flexible boot and local storage capabilities. This option is shown in the illustration below. 

To support customization for your deployment, the Cisco UCS X210c M7 Compute Nodes offers an optional PCIe Gen 4 front mezzanine module with support for up to two U.2 or U.3 NVMe drives and two GPUs. 

![](/c/dam/en/us/td/i/400001-500000/490001-500000/493001-494000/493166.jpg)

For more information, see the [Cisco UCS X210c M7 Compute Node Installation and Service Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x210c-m7/install/b-cisco-ucs-x210c-m7-install-guide.html). 

### Cisco UCS X410c M7 Compute Nodes

The Cisco UCS X410c M7 Compute Node (UCSX-410C-M7) is a two-slot compute node that supports four CPU sockets for 4th Generation Intel® Xeon® Scalable Processors, offering robust processing capabilities, extensive memory, flexible storage, and advanced networking options to meet the demands of diverse and evolving IT requirements. 

Each compute node consists of two distinct subnodes, a primary and a secondary. 

  * The primary contains two CPUs (1 and 2), two heatsinks, and half of the DIMMs. All additional hardware components and supported functionality are supported through the primary, including the front and rear mezzanine hardware options, rear mezzanine bridge card, front panel, KVM, management console, and status LEDs. 

  * The secondary contains two additional CPUs (3 and 4), two heatsinks, and the other half of the DIMMs. 


The primary node can support a front storage module, which supports multiple different storage device configurations: 

  * All SAS/SATA configuration consisting of up to six SAS/SATA SSDs with an integrated RAID controller (HWRAID) in slots 1 through 6\. 

  * All NVMe configuration consisting of up to six U.2 NVMe Gen4 (x4 PCIe) SSDs in slots 1 through 6.

  * A mixed storage configuration consisting of up to six SAS/SATA or up to four NVMe drives is supported. In this configuration, U.2 NVMe drives are supported in slots 1 through 4 only. U.3 NVMe drives can be used in slots 1 through 6. 


For more information, see the [Cisco UCS X410c M7 Compute Node Installation and Service Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x410c-m7/install/b-cisco-ucs-x410c-m7-install-guide.html). 

### Cisco UCS X440p PCIe Nodes

The Cisco UCS X440p Gen4 PCIe Node is a modular node that can be paired 1:1 with a Cisco UCS X-Series M7 Compute Node in the UCS X9508 chassis to provide GPU-accelerator support using the UCS X9416 X-Fabric modules in the same chassis. 

Each Cisco UCS X440p PCIe Node supports up to four of the supported FHFL GPUs to a Cisco UCS X-Series M7 Compute Node. This PCIe node supports PCIE Gen4 connectivity. 

![](/c/dam/en/us/td/i/400001-500000/490001-500000/494001-495000/494025.jpg)

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

A single Cisco UCS X9508 chassis cannot support a mix of different PCIe nodes, so if the same server chassis contains Cisco UCS X440p PCIe Nodes, it cannot contain Cisco UCS X580p PCIe Nodes. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The compute node paired with the X440p PCIe Node must be a Cisco M7 X-Series Compute Node.  For more information, see the [Cisco UCS X440p PCIe Node Installation and Service Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x440p/install/b-cisco-ucs-x440p-gen4-pcie-install-guide.html). 

* * *  
  
---|---  
  
### Cisco UCS X210c M8 Compute Nodes

The Cisco UCS X210c M8 Compute Node is the third generation of compute node to integrate into the Cisco UCS X-Series Modular System. It delivers performance, flexibility, and optimization for deployments in data centers, and at remote sites. 

The Cisco UCS X210c M8 Compute Node is a single-slot compute node that has two CPU sockets that can support Sixth Generation Intel Xeon Scalable Server Processors. 

Additionally, each compute node supports a front storage module offers the following different storage device configurations: 

  * Up to six SAS/SATA NVMe SSDs with an integrated RAID controller.

  * Up to six NVMe SSDs in slots 1 through 6.

  * A mixture of up to six SATA/SATA or up to four NVMe drives is supported. In this configuration, U.3 NVMe drives in slots 1 through 6. The U.3 NVMe drives are also supported with an integrated RAID module (MRAID Controller, UCSX-RAID-M1L6) and Compute RAID Controller (UCSX-X10C-RAIDF). 

  * Up to nine hot-pluggable EDSFF E3.S NVMe drives with a passthrough front mezzanine controller option.

  * With an integrated RAID module, the following drive configurations are supported:

  * SAS/SATA drives in slots 1 through 6

  * NMVe U.3 drives in slots 1 through 6

  * A mix of NVMe U.3 and SAS/SATA drives. SAS/SATA and NVMe U.3 drives are supported in on Slots 1 through 6


For more information, see the [Cisco UCS X210c M8 Compute Node Installation and Service Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x210c-m8/install/b-x210c-m8-install.html). 

### Cisco UCS X215c M8 Compute Nodes

The Cisco UCS X215c M8 is a single-slot compute node that has two CPU sockets that can support a maximum of one Fourth Gen AMD EPYC™ Processors with up to 96 cores per processor and up to 384 MB of Level 3 cache per CPU or Fifth Gen AMD EPYC™ Processors with up to 196 cores per processor and up to 384 MB of Level 3 cache per CPU. The minimum system configuration requires one CPU installed in the CPU1 slot. 

Additionally, each compute node has a front mezzanine modules the offers the following:

  * A front storage module, which supports multiple different storage device configurations: 

  * Up to six hot pluggable SAS/SATA/U.3 NVMe 2.5inch SSDs (slots 1-6).

  * SATA/SAS/U.3 drives can co-exist on the front mezzanine module. RAID volumes are restricted to same type of drives only. For example, RAID 1 volume need to use a set of SATA or SAS or U.3 NVMe drives. 


![](/c/dam/en/us/td/i/400001-500000/490001-500000/494001-495000/494024.jpg)

For more information, see the [Cisco UCS X215c M8 Compute Node Installation and Service Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x215c-m8/install/b-cisco-ucs-x215c-m8-install.html). 

### Cisco UCS X580p PCIe Nodes

The Cisco UCS X580p PCIe Node delivers high-performance GPU support with associated Cisco UCS X-Series M8 Compute nodes through UCS X9516 X-Fabric Modules in the same chassis. 

Each Cisco UCS X580p PCIe node is a dual-slot node that supports up to four FHFL PCIe GPUs and can be paired with the Cisco UCS X210c M8 Compute Node with Intel® Xeon® 6 processors, as well as the UCS X215c M8 compute node with EPYC processors. This node offers significantly greater flexibility than the Cisco UCS X440p PCIe Node, allowing users to associate up to four GPUs with up to two Cisco UCS M8 X-Series Compute Nodes. This node supports PCIe Gen 5 connectivity. 

![](/c/dam/en/us/td/i/400001-500000/490001-500000/494001-495000/494026.jpg)

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

A single Cisco UCS X9508 chassis cannot support a mix of different PCIe nodes, so if the same server chassis contains Cisco UCS X580p PCIe Nodes, it cannot contain Cisco UCS X440p PCIe Nodes. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The compute nodes associated with the X580p PCIe Node must be a Cisco M8 X-Series Compute Nodes.  For more information, see the [Cisco UCS X580p PCIe Node Installation and Service Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x580p/install/b-cisco-ucs-x580p-gen5-pcie-install-guide.html). 

* * *  
  
---|---  
  
## Intelligent Fabric Modules

The Cisco UCS X9508 contains Intelligent Fabric Modules (IFMs) on the rear of the server chassis. IFMs have multiple functions in the server chassis: 

  * Data traffic: IFMs support network-level communication for traditional LAN and SAN traffic as well as aggregating and disaggregating traffic to and from individual compute nodes. 

  * Chassis health: IFMs monitor common equipment in the server chassis, such as fan units, power supplies, environmental data, LED status panel, and so on. Management functions for the common equipment is supported through IFMs. 

  * Compute Node health: IFMs monitor Keyboard-Video-Mouse (KVM) data, Serial over LAN (SoL) data, and IPMI data for the compute nodes in the chassis, as well as provide management of these features. 


IFMs must always be deployed in pairs to provide redundancy and failover to safeguard system operation. 

  * Cisco UCS 9108 25G Intelligent Fabric Module
  * Cisco UCS 9108 100G Fabric Module


### Cisco UCS 9108 25G Intelligent Fabric Module

The Cisco UCS 9108 Intelligent Fabric Module (UCSX-I-9108-25G) is an IFM that supports aggregate data throughput of 2TB/s through two groups of four optical ports. 

Figure 4. UCS 9108 25 Gbps Intelligent Fabric Module, Faceplate View  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308980.jpg) 1 |  Status LEDs:

  * IFM Status (top LED)
  * Fan Status LEDs 1 through 3, with Fan 1 as LED 2, Fan 2 as LED 3, and Fan 3 as LED 4. 

|  2 |  IFM Reset Button  
---|---|---|---  
3 |  SFP28 Optical Ports Ports are arranged in two groups of four physical ports:

  * Ports are in groups of four. Port number 1 is the left port in this group, and port number 4 is the right port in the group. 
  * Ports are in groups of four. Port number 5 is the left port in this group, and port number 8 is the right port in the group. 

|  4 |  IFM Ejector Handles, left and right  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For information about removing and installing the IFM's components, see [Cisco UCS 9108 25G IFM Field Replaceable Unit Replacement Instructions](m-ifm-afm-xfm-fru-replacement-instructions-labels.html#cisco-ucs-9108-25g-ifm-field-replaceable-unit-instructions). 

* * *  
  
---|---  
  
### Cisco UCS 9108 100G Fabric Module

The Cisco UCS 9108 Intelligent Fabric Module (UCSX-I-9108-100G) is an IFM that supports data throughput of 100G through two groups of 4 ports. 

Figure 5. UCS 9108 100 Gbps Intelligent Fabric Module, Faceplate View  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308981.jpg) 1 |  Status LEDs:

  * IFM Status (top LED)
  * Fan Status LEDs 1 through 3, with Fan 1 as LED 2, Fan 2 as LED 3, and Fan 3 as LED 4. 

|  2 |  IFM Reset Button  
---|---|---|---  
3 |  QSFP28 Optical Ports.  Ports are arranged in two groups of four physical ports. Ports are stacked in vertical pairs, with two ports in each vertical port stack. 

  * Port number 1 is the top port in the left port pair in the first port group, and port number 3 is the top port of the right port pair in the group. 
  * Port number 5 is the top port in the left port pair of the second group, and port number 7 is the top port in the right port pair of the group. 

|  4 |  IFM Ejector Handles, left and right  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For information about removing and installing the IFM's components, see [Cisco UCS 9108 100G IFM Field Replaceable Unit Replacement Instructions](m-ifm-afm-xfm-fru-replacement-instructions-labels.html#cisco-ucs-9108-100g-intelligent-fabric-module-field-replacement-unit-instructions). 

* * *  
  
---|---  
  
## X-Fabric Modules

The Cisco UCS X9508 server chassis supports Cisco X-Fabric Modules, including the Cisco UCS X9416 X-Fabric Module and Cisco UCS X9516 X-Fabric Modules (XFMs). 

The module is a configuration option:

  * The UCS X9416 X-Fabric Modules are required when the server chassis contains the Cisco UCS X440p PCIe node.

  * The UCS X9516 X-Fabric Modules are required when the server chassis contains the Cisco UCS X580p PCIe node.

  * The X-Fabric module is not required if your server chassis contains only Cisco UCS X-Series compute nodes, such as the Cisco UCS X210c. 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Although Cisco UCS X-Fabric Modules can be removed, the best practice is to leave them installed even during installation. If your Cisco UCS X9508 server is configured so that no XFMs are installed, only XFM blanks, leave the blanks installed also, even during chassis installation. 

* * *  
  
---|---  
  
X-Fabric Modules are always deployed in pairs to support GPU acceleration through the Cisco UCS X440p PCIe nodes (Gen4 support) or Cisco UCS X580p PCIe nodes (Gen5 support). Therefore, two PCIe modules must be installed in a server chassis that contains any number of PCIe nodes. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Do not operate the server chassis with the XFM slots empty!

* * *  
  
---|---  
  
Each server chassis supports two UCS X9416 modules, which are located in the two horizontal module slots at the bottom of the chassis rear. 

![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540739.jpg)

1 |  XFM slot 1 (XFM1) |  Provides PCIe connectivity to all module slots 1 through 8 |   
---|---|---|---  
2 |  XFM slot 2 (XFM2) |  Provides PCIe connectivity to all module slots 1 through 8 |   
  
For additional information, see the following topics:

  * Cisco UCS X9416 Fabric Module

  * Cisco UCS X9516 Fabric Module

  * Cisco UCS X-Fabric Module Blanks


  * Cisco UCS X9416 Fabric Module
  * Cisco UCS X9516 Fabric Module
  * Cisco UCS X-Fabric Module Blanks


### Cisco UCS X9416 Fabric Module

The Cisco UCS X9416 module is a Cisco X-Fabric Module (XFM) that provides PCIe connectivity for module slots one through eight on the front of the server chassis. Each X-Fabric Module is installed in the bottom two slots of the rear of the Cisco UCS X9508 server chassis. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Although the Cisco UCS X9416 Fabric Modules can be removed, the best practice is to leave them installed even during chassis installation. 

* * *  
  
---|---  
  
Each module provides:

  * Integrated, hot-swappable active fans for optimal cooling

  * PCIe x16 connectivity and signaling between pairs of compute nodes and GPU modules, such as the Cisco X440p PCIe node


Each module has STATUS LEDs to visually indicate operational status the X-Fabric module and its fans. 

![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540441.jpg)

1 |  Status LEDs:

  * Module Status (top LED)
  * Fan Status LEDs 1 through 3, with Fan 1 as LED 2, Fan 2 as LED 3, and Fan 3 as LED 4. 

|  2 |  Module Ejector Handles, Left and Right  
---|---|---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For information about removing and installing the XFM's components, see [Cisco UCS X9416 X-Fabric Module Field Replaceable Unit Replacement Instructions](m-ifm-afm-xfm-fru-replacement-instructions-labels.html#cisco-ucs-x9416-x-fabric-module-field-replaceable-unit-replacement-instructions). 

* * *  
  
---|---  
  
### Cisco UCS X9516 Fabric Module

The Cisco UCS X9516 (UCSX-FS-9516) is a Cisco X-Fabric Module (XFM) that provides PCIe Gen 5 connectivity for module slots one through eight on the front of the server chassis. A total of two of these modules is required. 

Each X-Fabric Module is installed in the bottom two slots of the rear of the Cisco UCS X9508 server chassis.

Each module provides:

  * Integrated, hot-swappable active fans for optimal cooling

  * PCIe x16 connectivity and signaling between pairs of compute nodes and GPU modules, such as the available M8 series of Cisco UCS X Series Compute Nodes and the Cisco UCS X580p PCIe Node. Additional information about these products is available through the Cisco website. 


Each Cisco UCS X9516 X-Fabric Module features:

  * Two PCIe cages (numbered 1 and 2) that accept PCI cards to offer flexibility for your deployment. The XFM faceplate has identifiers for each slot at the upper left corner of the cage. For information about the supported Gen5 PCIe cards, see Cisco UCS X9516 Supported PCIe Cards. 

  * Connectivity and operational information available through the LED cluster at the left edge of the XFM. 

  * Ejector handles for tool-less installation and removal from the rear panel of the Cisco UCS X9508 server chassis that contains the XFMs. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Although the Cisco UCS X9516 Fabric Modules can be removed, the best practice is to leave them installed even during chassis installation. 

* * *  
  
---|---  

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The following illustration shows the XFM populated with PCIe cards. Filler blanks are available. If the XFM will not contain any PCIe cards, each unused card slot must be covered with a filler blank. 

* * *  
  
---|---  
  
![](/c/dam/en/us/td/i/400001-500000/490001-500000/490001-491000/490995.jpg)

**1** |  Status LEDs:

  * Module Status (top LED)
  * Fan Status LEDs 1 through 3, with Fan 1 as LED 2, Fan 2 as LED 3, and Fan 3 as LED 4. 

|  **2** |  PCIe Cage 2  
---|---|---|---  
**3** |  PCIe Card Slot 2 Supports one Gen5 x16 card |  **4** |  PCIe Card Slot 1 Supports one Gen5 x16 card  
**5** |  PCIe Cage 1 |  **6** |  Module ejectors, two One on the left of the module and one on the right  
**7** |  Module Ejector Handles, two One per ejector, left and right |  **-** |   
  
  * Cisco UCS X9516 Supported PCIe Cards


#### Cisco UCS X9516 Supported PCIe Cards

The UCS X9516 Fabric Modules offer customizable PCIe connectivity through two PCIe cages. Each cage can accept one of the following third-party PCIe Gen 5 x16 NICs for a total of two NICs per XFM: 

  * NVIDIA ConnectX®-7 200/400G Network Adapter cards


### Cisco UCS X-Fabric Module Blanks

The Cisco UCSX-9508-RBLK is Cisco UCS X-Fabric Module Blank slot which is used for providing future X-Fabric connectivity. Currently this module blank has active fans to facilitate airflow, and it is often called the Active Fan Module (AFM). 

In a typical configuration, this module blank can be installed in either of the two bottom slots in the rear of the chassis below the IFM slots. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

If your Cisco UCS X9508 server is configured so that no XFMs are installed, only XFM blanks, leave the blanks installed even during chassis installation. 

* * *  
  
---|---  
Figure 6. UCS X9508 Rear Module Blank (AFM), Faceplate View  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308982.jpg) 1 |  Status LEDs:

  * Module Status (top LED)
  * Fan Status LEDs 1 through 3, with Fan 1 as LED 2, Fan 2 as LED 3, and Fan 3 as LED 4. 

|  2 |  Module Ejector Handles, Left and Right  
---|---|---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For information about removing and installing the XFM's components, see [Cisco UCS 9508 Active Fan Module (AFM) Field Replaceable Unit Replacement Instructions](m-ifm-afm-xfm-fru-replacement-instructions-labels.html#Blankfield_Installation). 

* * *  
  
---|---  
  
## Fan Modules

The chassis contains four, 100 mm fan modules (UCSX-9508-FAN=), with the minimum configuration of 4 fan modules for optimal cooling. Fans draw air in through the front of the chassis (the cool aisle) and exhaust air through the back of the chassis (the hot aisle) 

Fans are located in the middle of the server chassis rear panel. Fans are numbered one to four starting with the leftmost fan. 

Figure 7. Fan Module  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308851.jpg) ![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Additional 40 mm fan modules are equipped on the Intelligent Fabric Modules and X-Fabric Modules installed in the chassis. These fans (UCSX-RSFAN=) are not interchangeable with the chassis fans. 

* * *  
  
---|---  
  
## Power Supplies

The chassis supports up to 6 AC power supplies (PSUs), with the minimum configuration of 2 PSUs required. They are Titanium certified 2800W capable AC Power Supply Units (PSUs) that support input power from AC sources. 

PSUs are redundant and load-sharing and can be used in the following power modes:

  * N+1 power supply configuration, where N is the number of power supplies required to support system power requirements

  * N+2 power supply configuration, where N is the number of power supplies required to support system power requirements

  * Grid configuration, which is also known as N+N power supply configuration, in which N is the amount of power supplies required to support the system power requirements. 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The chassis requires a minimum of two PSUs to operate.

* * *  
  
---|---  
Figure 8. AC Power Supply  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308931.jpg)

To determine the number of power supplies needed for a given configuration, use the [Cisco UCS Power Calculator](https://mainstayadvisor.com/Go/Cisco/Cisco-UCS-Power-Calculator.aspx) tool. 

  * LEDs
  * Buttons
  * Connectors
  * Power Supply Configuration


### LEDs

One LED indicates power connection presence, power supply operation, and fault states. See Interpreting LEDs for details. 

### Buttons

There are no buttons on a power supply.

### Connectors

The AC power connections are at the rear of the chassis on the Power Entry Module (PEM) to support AC input from the facility. The chassis has two PEMs (PEM 1 and PEM 2), and each supports 3 power supplies. 

  * PEM 1 supports PSUs 1, 2, and 3.

  * PEM 2 supports PSUs 4, 5, and 6. 


Each of the six hot-swappable power supplies is accessible from the front of the chassis. These power supplies are Titanium efficiency, and they can be configured to support non-redundant, N+1 redundant, N+2 redundant, and grid-redundant configurations. 

### Power Supply Configuration

When considering power supply configuration, you need to take several things into consideration: 

  * AC power supplies are all single phase and have a single input for connectivity to its respective PEM. The customer power source (a rack PDU or equivalent) connects input power directly to the chassis power entry module (PEM), not the actual AC power supplies. 

  * The number of power supplies required to power a chassis varies depending on the following factors: 

  * The total "Maximum Draw" required to power all the components configured within that chassis—such as intelligent fabric modules (IFMs), fans, compute nodes (CPU and memory configuration of the compute nodes). 

  * The Desired Power configuration for the chassis. The chassis supports non-redundant power supply configuration, N+1 power supply configuration, N+2 power supply configuration, and grid power supply configuration, which is also known as N+N redundancy. The system also supports an Extended Power mode. 

  * The load is balanced across all active power supplies excluding power supplies in the standby mode.

  * When connecting the chassis to facility power, make sure not to overload the capacity of a PDU or power strip, for example, by connecting all PSUs to one PDU or power strip that is not capable of carrying the total power draw of the chassis. 


  * Power Save Mode
  * Extended Power Mode
  * Non-Redundant Mode
  * N+1 Power Supply Configuration
  * N+2 Power Supply Configuration
  * Grid Configuration


#### Power Save Mode

If the Power Save mode is enabled in the Power policy of the Chassis Profile, power supplies that are not needed to meet the current power demand will be placed into standby mode and will not share the power load. Power supplies required to maintain power supply redundancy will remain active and will not enter standby. Power supplies in standby mode will automatically turn on if the power demand increases or if there is a failure in an active power supply. 

#### Extended Power Mode

The Cisco UCS X9508 Server Chassis supports an Extended Power mode that allows the chassis to utilize an additional 15% of the redundant power reserve. If a power supply fails, the extended power from that failed supply is lost. In response, the chassis limits power consumption to the remaining extended power available from the other redundant power supplies. If no redundant power supplies remain, the chassis limits power to the non-extended power value. 

To protect the system from power faults, the chassis includes a hardware mechanism known as the "emergency brake". The "emergency brake" activates if the actual power demand exceeds the non-extended power limit, and it limits power consumption faster than the remaining PSUs can reach an over-current state or cause a power distribution unit (PDU) breaker to trip. Once the power demand falls below the limit, the emergency brake is released, and normal server throttling is used to maintain power under the cap. 

#### Non-Redundant Mode

In non-redundant mode, the system may go down with the loss of any supply or power grid associated with any particular chassis. We do not recommend operating the system in non-redundant mode in a production environment. 

To operate in non-redundant mode, each chassis should have at least two power supplies installed. The supplies that are placed into standby depends on the installation order (not on the slot number). The load is balanced across active power supplies, not including any supplies in standby. 

The chassis requires a minimum of 2 power supplies. In cases of low-line operation, the total available power is 1400W each for a total of 2800W. Do not attempt to run the chassis on less than the minimum number of power supplies. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

In a non-redundant system, power supplies can be in any slot. Installing less than the required number of power supplies results in undesired behavior such as compute node shutdown. Installing more than the required amount of power supplies may result in lower power supply efficiency. At a minimum, this mode will require two power supplies. 

* * *  
  
---|---  
  
  * Consideration for Non-Redundant Power Mode


##### Consideration for Non-Redundant Power Mode

When the chassis is configured for non-redundant power mode, any PSUs you select can be put into standby mode. In this mode, the PSUs do not actively supply power. Instead, the PSUs are online standbys. For more information about non-redundant power mode, see Non-Redundant Mode. 

When the chassis is in non-redundant power mode and multiple PSUs are installed, through Intersight you can configure the server chassis for **Power Save Mode**. In this mode, any unused PSUs are put into standby mode. They are not actively providing power. 

In non-redundant mode and when **Power Save Mode** is enabled, the server chassis can have one or more active PSUs and one or more standby PSUs. In this configuration, if all active PSUs fail either simultaneously or almost simultaneously, a timing issue can prevent the server chassis from having sufficient time to activate the standby PSUs. As a result, the server chassis may experience a brownout condition. 

  * You can avoid this consideration by not enabling **Power Save Mode**. 

  * You can recover from this consideration by power cycling or rebooting the server chassis. If PSUs are powered cycled, the chassis automatically power cycles. Based on the settings in the Server Profiles for the installed servers or compute nodes, servers might or might not power on. Based on the number of servers that power on, the brownout condition can be cleared. 


#### N+1 Power Supply Configuration

In an N+1 configuration, the chassis contains a total number of power supplies to satisfy system power requirements, plus one additional power supply for redundancy. Any additional power supplies may be placed into Standby mode, if the Standby mode is enabled in the Power Policy of the Chassis Profile. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

In an N+1 configuration, a maximum power of 14kW is delivered with five PSUs configured as Active while the remaining one PSU is in standby mode. The 14kW maximum delivered power is only possible at high input voltage range (200-240VAC). In low input voltage range (100-127VAC nominal), the maximum delivered power would be 7kW. 

* * *  
  
---|---  
  
If one Active power supply should fail, the surviving supplies can provide power to the chassis, until the Standby power supply can be switched to Active status. In addition, Cisco Intersight turns on any "turned-off" power supplies to bring the system back to N+1 status. The system will continue to operate, giving you a chance to replace the failed power supply. 

#### N+2 Power Supply Configuration

In an N+2 configuration, the chassis contains a total number of power supplies to satisfy system power requirements, plus two additional power supplies for redundancy. Any additional power supplies may be placed into Standby mode, if the Standby mode is enabled in the Power Policy of the Chassis Profile. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

In N+2 redundant mode, a maximum power load of 11.2KW is supported with four active modules. The 11.2KW maximum power load is only possible at high input voltage range (200-240VAC). In low input voltage range (100-127VAC nominal), the maximum delivered power would be 5.6KW. 

* * *  
  
---|---  
  
If one or two power supplies should fail, the surviving supplies can provide power to the chassis. In addition, the Cisco Intersight interface supports turning on any "turned-off" power supplies to bring the system back to N+2 status. 

#### Grid Configuration

With grid power configuration (also called N+N redundancy), each set of three PSUs has its own input power circuit, so each set of PSUs is isolated from any failures that might affect the other set of PSUs. If one input power source fails, causing a loss of power to three power supplies, the surviving power supplies on the other power circuit continue to provide power to the chassis. The two power sources in the chassis are defined by the Power Entry Module (PEM) boundaries: PEM1 corresponds to source 1 and connects to power supplies 1-3, while PEM2 corresponds to source 2 and connects to power supplies 4-6. For Grid mode operation, it is required to have an even number of power supplies that are equally distributed across these two PEMs. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Grid redundant mode requires the chassis load to be limited to 8.4kW for high input voltage range (200-240VAC) and 4.2kW for low input power range for a maximum grid configuration (3+3). For a 2+2 minimum configuration, the chassis load is limited to 5.6kW for high line input voltage and 2.8kW for low line input voltage.  If Extended Power Mode is enabled in the Power policy of the Cisco UCS X9508 Chassis Profile, the power limit is increased by 15%. Specifically: 

  * For a 6 PSU configuration in Grid mode, the normal power limit is 8400W. With Extended Power Mode enabled, this limit increases to 9660W total, which corresponds to 1610W per PSU or 4830W per power grid (PEM) under high line/low line conditions. 
  * For a 4 PSU configuration, the power limit increases to 6440W total (3220W per power grid).


* * *  
  
---|---  
  
Grid redundant mode is configured when:

  * all six PSUs are in Active mode to provide power

  * two sets of three PSUs are each connected to separate facility input power sources, including separate cabling for each set 

  * For grid redundant mode, the total number of PSUs should always be divided equally. So, a grid power configuration supports 3+3 (maximum configuration per input power source) or 2+2 (minimum configuration per power input source). 


The grid power configuration is primarily used when you have two separate facility input power sources available to a chassis. A common reason for using this power supply configuration is if the rack power distribution is such that power is provided by two PDUs and you want redundant protection in the case of a PDU failure or to allow continued operation during power facilities maintenance. 

## LEDs

LEDs on both the chassis and the modules installed within the chassis identify operational states, both separately and in combination with other LEDs. 

  * LED Locations
  * Interpreting LEDs


### LED Locations

The UCS X9508 server chassis uses LEDs to indicate power, status, location/identification. Other LEDs on IFMs, PSUs, fans, and compute nodes indicate status information for those elements of the system. 

Figure 9. LEDs on a Cisco UCS X9508 Server Chassis—Front View  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308956.jpg) Figure 10. LEDs on the Cisco UCS X9508 Server Chassis—Rear View  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308957.jpg)

### Interpreting LEDs

Table 2. Chassis, System Fans, and Power Supply LEDs LED  |  Color  |  Description   
---|---|---  
Locator  LED and button (callout 1 on the chassis front panel) ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309096.jpg) |  Off  |  Locator not enabled.   
Blue  |  Locates a selected chassis You can initiate beaconing in UCS Intersight or with the button, which toggles the LED on and off.   
Network Status  (callout 1 on the chassis front panel)![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309098.jpg) |  Off  |  Network link state undefined.  
Solid Green  |  Network link state established on at least one IFM, but no traffic detected.   
Blinking Green  |  Network traffic detected on at least one IFM.   
System Status (callout 1 on the chassis front panel)![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309097.jpg) |  Solid amber  |  Chassis is in a degraded operational state. For example:

  * Power Supply Redundancy Lost
  * Mismatched Processors
  * 1 on N Processors Faulty
  * Memory RAS Failure
  * Failed Storage Drive/SSD

  
Solid Green |  Normal operating condition.  
Blinking Amber |  Chassis is in a critical error state. For example:

  * Boot Failure
  * Fatal Processor and/or bus error detected
  * Loss of both I/O Modules
  * Over Temperature Condition

  
Off |  System is in an undefined operational state or not receiving power.  
Fan Module  (callout 3 on the Chassis Rear Panel)![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309097.jpg) |  Off  |  No power to the chassis or the fan module was removed from the chassis.   
Amber  |  Fan module restarting.   
Green  |  Normal operation.   
Blinking amber  |  The fan module has failed.   
Power Supplies, each has one a bicolor LED (callout 2 on the Chassis Front Panel)![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309097.jpg) |  Off  |  Power supply is not fully seated, so no connection exists.  
Green  |  Normal operation.   
Blinking green  |  AC power is present, but the power supply is in Standby mode.  
Amber  |  Any fault condition is detected. Some examples:

  * Over or under voltage
  * Over temperature alarm
  * Power supply has no connection to a power cord. 

  
Blinking Amber  |  Any warning condition is detected. Some examples:

  * Over voltage warning
  * Over temperature warning

  
Table 3. Intelligent Fabric Module and Rear Module Blank LEDs  LED  |  Color  |  Description   
---|---|---  
Module Status  (callout 1 and 4 on the Chassis Rear Panel)![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309097.jpg) |  Off  |  No power.   
Green  |  Normal operation.   
Amber  |  Booting or minor temperature alarm.   
Blinking amber  |  POST error or other error condition.   
Module Fans (callout 1 and 4 the Chassis Rear Panel)![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309100.jpg) |  Off  |  Link down.   
Green  |  Link up and operationally enabled.   
Amber  |  Link up and administratively disabled.   
Blinking amber  |  POST error or other error condition.   
Table 4. Compute Node Server LEDs LED  |  Color  |  Description   
---|---|---  
Compute Node Power  (callout 3 on the Chassis Front Panel) ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309112.jpg) |  Off  |  Power off.   
Green  |  Normal operation.   
Amber  |  Standby.   
Compute Node Activity  (callout 3 on the Chassis Front Panel)![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309098.jpg) |  Off  |  None of the network links are up.   
Green  |  At least one network link is up.   
Compute Node Health (callout 3 on the Chassis Front Panel) ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309097.jpg) |  Off  |  Power off.   
Green  |  Normal operation.   
Amber  |  Degraded operation.   
Blinking Amber  |  Critical error.   
Compute Node Locator LED and button (callout 3 on the Chassis Front Panel) ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309111.jpg) |  Off  |  Locator not enabled.   
Blinking Blue 1 Hz |  Locates a selected compute node—If the LED is not blinking, the compute node is not selected.  You can initiate the LED in UCS Intersight or by pressing the button, which toggles the LED on and off.   
Drive Activity ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309102.jpg) |  Off  |  Inactive.   
Green  |  Outstanding I/O to disk drive.   
Drive Health ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309101.jpg) |  Off  |  No fault detected, the drive is not installed, or it is not receiving power.  
Amber  |  Fault detected  
Flashing Amber 4 Hz |  Rebuild drive active. If the Drive Activity LED is also flashing amber, a drive rebuild is in progress.  
  
## Optional Hardware Configuration

As an option, the server chassis can support a GPU-based PCIe node that pairs with Cisco UCS X-Series compute nodes to provide GPU acceleration. The following PCIe nodes are supported. 

  * The Cisco UCS X440p PCIe Node, which offers:

  * A GPU adapter node supporting zero, one or two GPUs through two separate GPU cages. For information about supported GPUs, go to the [Cisco UCS X440p PCIe Node Spec Sheet](https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-x-series-modular-system/x440p-specsheet.pdf). 

  * Each GPU installs directly into the GPU adapter card by a x8 Gen 4 PCI connection.

  * A storage adapter and riser card supporting zero, one, or two U.2 NVMe drives. NVMe RAID is supported through Intel VROC key on connected M6 compute nodes only. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For the Cisco UCS X9508 chassis to support any number of Cisco UCS X440p PCIe Nodes, both Cisco UCS X9416 Fabric Modules must be installed to provide proper PCIe signaling and connectivity to the node slots on the front of the server chassis. 
  * For information about the optional Cisco UCS X440p PCIe node, go to [Cisco UCS X440p PCIe Node Installation and Service Guide](https://www.cisco.com/content/en/us/td/docs/unified_computing/ucs/x/hw/x440p/install/b-cisco-ucs-x440p-gen4-pcie-install-guide.html). 
  * For information about the Cisco UCS X9416 Fabric Module, see Cisco UCS X9416 Fabric Module. 

* * *  
  
---|---  
  * The Cisco UCS X580p PCIe Node, which offers:

  * A GPU adapter node supporting zero through four GPUs through two separate PCIe cages. For information about supported GPUs, go to the [Cisco UCS X580p PCIe Node Spec Sheet](https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-x-series-modular-system/x580p-specsheet.pdf). 

  * Each GPU installs directly into a GPU cage by x16 Gen5 PCIe connection

  * Each PCIe node can connect to up to two separate M8 compute nodes. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For the Cisco UCS X9508 chassis to support any number of Cisco UCS X580p PCIe Nodes, both Cisco UCS X9516 Fabric Modules must be installed to provide proper PCIe signaling and connectivity to the node slots on the front of the server chassis. 
  * For information about the optional Cisco UCS X580p PCIe node, go to the [Cisco UCS X580p PCIe Node Installation and Service Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x580p/install/b-cisco-ucs-x580p-gen5-pcie-install-guide/m-servicing-the-node.html). 
  * For information about the Cisco UCS X9516 Fabric Module, see Cisco UCS X9516 Fabric Module. 

* * *  
  
---|---  


---

## Page 4: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x9508/install/b-ucs-x9508-install/m-installation.html

# Installation

This chapter contains the following topics:

## Installation Notes and Warnings for the Cisco UCS X9508 Server Chassis

The following notes and warnings apply to all installation tasks: 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Before you install, operate, or service the system, see the [Regulatory Compliance and Safety Information for Cisco UCS ](http://www.cisco.com/en/US/docs/unified_computing/ucs/hw/regulatory/compliance/ucs_regulatory_compliance_Information.html) for important safety information. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

The chassis can be shipped either empty or pre-populated. If the chassis is shipped pre-populated, do not remove the X-Fabric Modules in the two bottom rear slots. Other rear components, such as Intelligent Fabric Modules and fan modules should be removed to lighten the weight of the chassis.  On the front of the chassis, such as PSUs and Compute Nodes, can be removed to lessen the overall chassis weight before installation. However, even with compute nodes and PSUs removed, the chassis still has considerable weight. So, make sure to use a scissors jack, equipment lift, or other machinery to bear the weight of the chassis during installation. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/warn.gif)  
**Warning** | 

* * *

IMPORTANT SAFETY INSTRUCTIONS  This warning symbol means danger. You are in a situation that could cause bodily injury. Before you work on any equipment, be aware of the hazards involved with electrical circuitry and be familiar with standard practices for preventing accidents. Use the statement number provided at the end of each warning to locate its translation in the translated safety warnings that accompanied this device. Statement 1071  **SAVE THESE INSTRUCTIONS**

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/warn.gif)  
**Warning** | 

* * *

This unit is intended for installation in restricted access areas. A restricted access area can be accessed only through the use of a special tool, lock and key, or other means of security. Statement 1017 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/warn.gif)  
**Warning** | 

* * *

Only trained and qualified personnel must be allowed to install, replace, or service this equipment. Statement 1030

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

Watch your hands and fingers whenever you handle the chassis, modules, nodes, and components! Narrow vertical or horizontal spaces in situations like, but not limited to, moving the chassis into or out of the shipping container or equipment rack can cause pinch hazards for your hands and fingers.  Although they do not eliminate the possibility of pinching, the chassis has defined grasp points to facilitate handling and moving it. For information about chassis grasp points, see Handling the Chassis. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Do not lift or handle the chassis by the top rear sheet metal, as indicated by the DO NOT LIFT label on the top rear surface. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

The Cisco UCS X9508 Server Chassis can support the Cisco UCS X440p PCIe Nodes (Gen4) and the Cisco X580p PCIe Nodes (Gen5), but only one type per chassis. You cannot install the X440p and X580p PCIe nodes in the same chassis. If you are installing either of these PCIe nodes, each X9508 must be homogenous regarding the PCIe node type, all Gen4 PCIe nodes or all Gen5. 

* * *  
  
---|---  
  
  * Rack Requirements
  * Airflow Considerations
  * Earth Ground Considerations
  * Handling the Chassis
  * Moving Server Chassis
  * Installation Guidelines
  * Required Equipment
  * Unpacking and Inspecting the Chassis


### Rack Requirements

This section provides the requirements for installing in a standard open rack, assuming an external ambient air temperature range of 41 to 95°F (5 to 35°C): 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Do not use racks that have obstructions. These obstructions could impair access to field-replaceable units (FRUs).

* * *  
  
---|---  
  
Cisco UCS is compliant with any EIA-310-D/E compliant rack. Your equipment racks must also be compliant with EIA-310-D/E standard.

The Cisco UCS X9508 chassis can be installed in either a 9.5 mm square-hole rack or a 7.1 mm unthreaded round-hole rack. These racks require either square-hole cage nuts or round-hole cage nuts (also called spring nuts), respectively. 

  * Cage nuts are provided by Cisco as part of the accessory kit for your chassis.

  * Spring nuts are not provided by Cisco. They should have accompanied your equipment rack. 


Always use the proper cage nut or spring nut for your rack. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Some racks might be tapped, with threaded holes drilled directly into the rack's sheetmetal instead of square- or round-hole punch-outs for cage nuts. The rail kit for the server is not currently supported in tapped (threaded hole) racks. Do not attempt to install the chassis in a tapped (threaded hole) equipment rack. 

* * *  
  
---|---  
  
Also, be aware of these additional requirements:

  * The tool-less rack-mount kits (either Type 1 or Type 2) shipped with the chassis are required. The adjustable rack rails shipped with each enclosure extend from 29 inches (73.66 cm) to 35 inches (88.9 cm) 

  * Front and rear doors—If your equipment rack includes closing front and rear doors, the doors must have 65 percent open perforated area evenly distributed from top to bottom to permit adequate airflow. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Always use blanking panels to fill all remaining empty front panel U-spaces in the rack. This arrangement ensures proper airflow. Using a rack without blanking panels results in improper cooling that can lead to thermal damage. 

* * *  
  
---|---  


The rack must also meet the following requirements:

  * The minimum available vertical rack space per chassis must be seven RU (rack units), equal to 12.25 inches (31.2 cm).


### Airflow Considerations

Airflow through the chassis is from front to back. Air enters the chassis through the nodes and power supply grills at the front of the chassis and exits through the fan modules on the back of the chassis. To ensure proper airflow, follow these guidelines: 

  * Maintain ambient airflow throughout the data center to ensure normal operation. 

  * Consider the heat dissipation of all equipment when determining air-conditioning requirements. Do not allow the exhaust of one system to be the intake for another system. 

  * When evaluating airflow requirements, take into consideration that the hot air generated by equipment at the bottom of the rack can be drawn in the intake of the equipment above. 

  * Make sure that the exhaust at the rear of the chassis is unobstructed for at least 24 in. (61 cm). This includes obstruction due to messy cabling practices. 

  * If an enclosed rack is used, the front door must be 65 percent perforated to ensure adequate airflow to the nodes. 


### Earth Ground Considerations

#### Earth Ground Compliance

![](https://www.cisco.com/content/dam/en/us/td/i/templates/warn.gif)  
**Warning** | 

* * *

This equipment must be grounded. Never defeat the ground conductor or operate the equipment in the absence of a suitably installed ground conductor. Contact the appropriate electrical inspection authority or an electrician if you are uncertain that suitable grounding is available. Statement 1024 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/warn.gif)  
**Warning** | 

* * *

For Nordic countries (Norway, Finland, Sweden and Denmark) this system must be installed in a Restricted Access Location, where the voltage of the main ground connection of all equipment is the same (equipotential earth) and the system is connected to a grounded electrical outlet. Statement 328 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/warn.gif)  
**Warning** | 

* * *

High leakage current – earth connection essential before connection to system power supply. Statement 342

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/warn.gif)  
**Warning** | 

* * *

This equipment must be externally grounded using a customer-supplied ground wire before power is applied. Contact the appropriate electrical inspection authority or an electrician if you are uncertain that suitable grounding is available. Statement 366 

* * *  
  
---|---  
  
#### Ground Lug

Connecting the chassis to earth ground is completed by installing a grounding bracket, assembling the ground wire and ground lug, then screwing the ground lug and ground wire to the grounding bracket. 

The ground lug is provided in the accessory kit. If needed, additional ground lugs are available through third-party retailers, such as Panduit. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The following information is for standard AC power installations in North America. Your location might require different specifications. Make sure that you are using the correct ground lug and ground cable for your location. 

* * *  
  
---|---  
  
The ground lug must be a two-stud, copper barrel lug like the example shown below. 

  
![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309413.jpg)  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The positive and negative wires can be installed pointing either to the right or to the left as long as the terminal cover is used.  Panduit LCD4-14A-L connectors (or equivalent) may be used supply and return wires, and Panduit LCD4-14A or equivalent connectors may be used for the 90-degree ground lug wire. Both connections have double lugs with .25-inch holes measuring .625 inches from center to center. 

* * *  
  
---|---  
  
### Handling the Chassis

As a best practice, handle the chassis when it is empty, and use either a scissors jack or multiple people to bear the weight. 

The Cisco UCS X9508 has defined areas for holding the chassis (grasp points). Grasp points are not indicated on the chassis itself, but facilitate handling or moving the chassis. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

Watch your hands and fingers whenever you handle the chassis, modules, nodes, and components! Narrow vertical or horizontal spaces in situations including, but not limited to, moving the chassis into or out of the shipping container or equipment rack can cause pinch hazards for your hands and fingers. 

* * *  
  
---|---  
  
Use the following grasp points when handling the chassis. 

  * Front grasp points, horizontal

![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309700.jpg)

![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309701.jpg)

  * Rear grasp points

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Do not lift or handle the chassis by the top rear sheet metal, as indicated by the DO NOT LIFT label on the top rear surface. 

* * *  
  
---|---  
![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472423.jpg)


### Moving Server Chassis

A fully configured chassis is very heavy! Be aware of its weight, and follow these guidelines:

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Do not try to lift the chassis without mechanical assistance! The chassis weighs 400 lbs (181.43 kg) fully configured and 92 lbs (41.73 kg) empty. If available, use a scissor jack or other lifting device designed for installing heavy equipment into data center racks. 

* * *  
  
---|---  
  
  * Disconnect all power and external cables before lifting the chassis.

  * Remove all IFMs, fan modules, power supplies and compute nodes from the chassis before lifting. If XFMs are installed, do not remove them. Instead, leave them in the chassis during installation. 

  * Ensure that your footing is solid, and the weight of the system is evenly distributed between your feet.

  * If you must lift an empty chassis, do not attempt this alone. Get assistance from at least one other person. Lift the system slowly, keeping your back straight. Lift with your legs, not with your back. Bend at the knees, not at the waist. 


### Installation Guidelines

When installing the chassis, follow these guidelines: 

  * Plan your site configuration and prepare the site before installing the chassis. See [Site Planning and Maintenance Records](m-site-planning-and-maint-records.html#ID9) for the recommended site planning tasks. For details, see the [Cisco UCS Site Preparation Guide](http://www.cisco.com/en/US/docs/unified_computing/ucs/hw/site-prep-guide/ucs_site_prep.html). 

  * Record the information listed in [Site Planning and Maintenance Records](m-site-planning-and-maint-records.html#ID9) as you install and configure the chassis. 

  * Ensure that there is adequate space around the chassis to allow for servicing the chassis and for airflow. 

  * Ensure that the air-conditioning meets the heat dissipation requirements listed in [Technical Specifications](m-technical-specs.html#ID6)

  * Ensure that the cabinet or rack meets the requirements listed in Rack Requirements. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Jumper power cords are available for use in a rack. See [Specifications for the Cisco UCS X9508 Chassis Power Supply Units](m-technical-specs.html#ID256). 

* * *  
  
---|---  
  * Ensure that the site power meets the power requirements listed in [Technical Specifications](m-technical-specs.html#ID6). We recommend that you use a UPS to protect the UCS system. Using an unprotected supply exposes you to a risk of system failure due to input supply voltage variations or failures. 

Avoid UPS types that use ferroresonant technology. These UPS types can become unstable with systems such as the Cisco UCS, which can have substantial current draw fluctuations due to fluctuating data traffic patterns. 

  * Ensure that circuits are sized according to local and national codes. For North America, the power supply requires a 20 A circuit. 

To prevent loss of input power, ensure that the total maximum loads on the circuits supplying power to the chassis are within the current ratings for the wiring and breakers. 

  * Use the following torque values when installing the chassis: 

  * M6 x 20 mm screws: 48 +/- 5 in-lb 


### Required Equipment

Before you begin the installation, ensure that you have the following items:

  * Scissor jack or other lift device capable of bearing the weight of a fully loaded chassis, which is 400 lbs (181.43 kg).

  * Number 1 and number 2 Phillips-head screwdrivers with torque measuring capabilities

  * Flat-head screwdriver

  * Tape measure and level

  * ESD wrist strap or other grounding device

  * Antistatic mat or antistatic foam


### Unpacking and Inspecting the Chassis

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

When handling chassis components, wear an ESD strap and handle modules by the carrier edges only.

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/tip.gif)  
**Tip** | 

* * *

Keep the shipping container in case the chassis requires shipping in the future.

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The chassis is thoroughly inspected before shipment. If any damage occurred during transportation or any items are missing, contact your customer service representative immediately. 

* * *  
  
---|---  
  
As part of this procedure, you will be moving an empty chassis out of the shipping container. Be aware of the following precautions:

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

You will find it helpful to wear gloves when unpacking and lifting the chassis. Also, beware of hand and finger placement while unpacking, lifting, and moving the chassis to avoid possible pinch hazards. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

To lighten the weight of the chassis, remove compute nodes and PSUs from the front of the chassis. Remove the IFMs and fan modules from the rear of the chassis, but leave the XFMs installed in the lower rear slots of the chassis. Even with these parts removed, the chassis still has considerable weight. Always use a scissors jack, equipment lift, or other mechanical device to lift and support the chassis when moving or installing it. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/warn.gif)  
**Warning** | 

* * *

Use two or more people to lift the empty chassis. Do not attempt to lift the chassis by yourself! Always use safe lifting practices when lifting or moving the chassis.  Use a lift or scissors jack to support the chassis when lifting and moving it.

* * *  
  
---|---  
  
#### Procedure

* * *

**Step 1** |  Make sure to read and understand the preceding warnings in this topic, as well as the information in the following topics:

  * Installation Notes and Warnings for the Cisco UCS X9508 Server Chassis
  * Handling the Chassis
  * Moving Server Chassis

  
---|---  
**Step 2** |  Open the chassis shipping container.

  1. Remove the top and side panels so that the chassis is sitting on the bottom pallet. 
  2. Save all packaging material.

  
**Step 3** |  Do a visual inspection of the chassis to ensure there was no damage during transport.  
**Step 4** |  Compare the shipment to the equipment list provided by your customer service representative and verify that you have received the following items: 

  * Accessory kit, which contains:
  * M6 cage nuts (4) for square-hole equipment racks. Spring nuts for round-hole equipment racks are not provided by Cisco.
  * M6 x 20mmL screw (16)
  * Power Cable Management Arm (2), UCSX-9508-PCMA
  * Rail Kit, UCSX-9508-RAIL1=
  * Any printed documentation
  * Any optional items, which will be present in the accessory kit only if you ordered them with your system. 
  * Rear Mounting Brackets (1 left bracket, 1 right bracket), UCSX-9508-RACKBK. These brackets are optional. They should be ordered only if you plan to install the chassis in shippable rack. If you don't plan on shipping the rack, these brackets are not required. 
  * Compute Node Debug Cable, UCSX-C-DEBUGCBL, which is orderable as a customer option. 

  
**Step 5** |  Verify that all unused node slots and power supply bays have blank covers.  
**Step 6** |  If your chassis was shipped with hardware pre-installed, make sure to remove all compute nodes and PSUs, fans, and IFMs to reduce the chassis weight significantly before lifting it out of the shipping container. Blank faceplates can remain installed. Leave the XFMs installed in the bottom two rear chassis slots.  |  **Warning** |  Do not lift a chassis! The chassis has considerable weight even with all modules except the XFMs removed. Use a mechanical lift of scissors jack to lift and bear the weight of the chassis.   
---|---  
**Step 7** |  Locate the chassis handles, which are also the stabilizing brackets that secure the chassis to the bottom pallet.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309944.jpg)  
**Step 8** |  Using a 13-millimeter socket driver, remove the four M8 hex-head securing bolts (two per side).  |  **Note** |  Save the securing bolts.  
---|---  
  
![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540011.jpg)  
  
**Step 9** |  With two or more people, grasp the handles, lift the empty chassis off of the bottom palette, and set the chassis onto a lift or scissor jack that can support the chassis weight.   
**Step 10** |  Before installing the chassis into an equipment rack, use a #2 Phillips screwdriver to remove the two M5 screws (two per handle) that secure the handles to the chassis.  |  **Note** |  Save the handles and screws.   
---|---  
  
![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309945.jpg)

**1** |  Chassis handles, two per side |  **2** |  M5 screws, two per handle  
---|---|---|---  
  
* * *

## Rail Installation Templates

Two rail kits are available, and each shipping container will contain a left and right rail as a matched set. For each rail kit, a corresponding template is provided for reference through the following sections of this document. The templates show the locations on the rack for cage nuts, rail kit locator pegs, and screws should be installed. 

The templates facilitate installing the rail kit and chassis by ensuring proper spacing and alignment of installation hardware in both the left and right sides of the rack. The chassis has one template for the front of the rack and one for the back. 

Rail installation templates are applicable to either square-hole or round-hole equipment racks.

For each rail installation template, see: 

  * Front Install Template

  * Rear Install Template


  * Front Install Template
  * Rear Install Template


### Front Install Template

Use this installation to locate the correct spacing and alignment for chassis mounting hardware on the rack. This template shows the rack locations for mounting the front of the chassis. 

Align the Chassis Top of the template with the location in the rack where the top of the chassis will be and install the cage nuts and other hardware as shown. 

Figure 1. Rack Installation Template, Front  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308940.jpg)

### Rear Install Template

Use this installation to locate the correct spacing and alignment for chassis mounting hardware on the rack. This template shows the rack locations for mounting the rear of the chassis. 

Align the Chassis Top of the template with the location in the rack where the top of the chassis will be and install the cage nuts and other hardware as shown. 

Figure 2. Rack Installation Template, Rear  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308949.jpg) ![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The eight cage nuts shown near the top of the template (four per side) are required only when you are installing the rear tie down brackets, which are an orderable option, but not required for basic installation. 

* * *  
  
---|---  
  
## Installing Cage Nuts

The Cisco UCS X9508 chassis can be installed in standard size, untapped equipment racks that have either square or round-holes. For more information, see Rack Requirements. The X9508 server is supported on a rail kit which mounts to the square-hole or round hole cage. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

For untapped equipment racks, you must install cage nuts to provide a way for mounting screws to secure rails and the chassis to the rack. 

* * *  
  
---|---  
  
Use the appropriate option depending on your type of equipment rack:

  * Installing Cage Nuts, Square-Hole Rack

  * Installing Cage Nuts, Round-Hole Rack


  * Installing Cage Nuts, Square-Hole Rack
  * Installing Cage Nuts, Round-Hole Rack


### Installing Cage Nuts, Square-Hole Rack

Use the following task to install twelve, M6x1.00 square-hole cage nuts into a 9.5 mm unthreaded square-hole rack. Spring nuts are not supplied by Cisco. They should have accompanied your equipment rack. 

#### Before you begin

This document provides illustrations of installation templates for the front and rear of the chassis. The templates are designed to show you the proper holes within which the rails and cage nuts should be placed. Once you align the rack holes line up with the template, you should mark the holes on the rack so that they are easy to use. 

To use the rack installation templates, go to the appropriate topic:

  * Front Install Template

  * Rear Install Template


#### Procedure

* * *

**Step 1** |  Gather the M6 cage nuts and a flat head screwdriver.   
---|---  
**Step 2** |  Locate the template and refer to the chassis location in the rack and the cage nut locations on the template.   
**Step 3** |  Position one of the curled sides of the cage nut on the inside of the square cutout in the rack.   
**Step 4** |  Press the cage nut into the cutout and use the screwdriver to pinch the other curled edge inward until the cage nut clicks into place in the rack.  |  **Note** |  Cage nuts install on the inside of the rack so that most of the nut is behind the rack's sheet metal.  
---|---  
Figure 3. Cage Nut Installation  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308941.jpg)  
**Step 5** |  Verify that the cage nut is fully and correctly installed before installing the remaining cage nuts.   
  
* * *

### Installing Cage Nuts, Round-Hole Rack

Use the following task to install twelve M6x1.00 round-hole cage nuts (also called spring nuts) into a 7.1 mm unthreaded round-hole rack. Spring nuts are not supplied by Cisco. They should have accompanied your equipment rack. 

#### Before you begin

This document provides illustrations of installation templates for the front and rear of the chassis. The templates are designed to show you the proper holes within which the rails and cage nuts (spring nuts) should be placed. Once you align the rack holes line up with the template, you should mark the holes on the rack so that they are easy to use. 

To use the rack installation templates, go to the appropriate topic:

  * Front Install Template

  * Rear Install Template


#### Procedure

* * *

**Step 1** |  Gather the M6 spring nuts and a flat head screwdriver.   
---|---  
**Step 2** |  Using the rack installation template, refer to the chassis location in the rack and the spring nut locations on the template.   
**Step 3** |  Position the open end of the spring nut so that the rack's sheetmetal can slide into the gap between the spring nut's sheetmetal.   
**Step 4** |  Slide the spring nut so that its round hole lines up with the round hole in the equipment rack.  |  **Note** |  Cage nuts install so that most of the nut is behind the rack's sheet metal.  
---|---  
**Note** |  If needed, use the flat-head screwdriver to slightly pry open the gap between the spring nut's sheetmetal to allow it to slide onto the rack over the round hole.   
---|---  
![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540686.jpg)  
**Step 5** |  Verify that the cage nut is fully and correctly installed before installing the remaining cage nuts.   
  
* * *

## Rail Kits

The Cisco UCS X9508 supports two rail kits, Type 1 and Type 2.

  * Each rail kit consists of two stationary rails that facilitate rack installation of the chassis and stabilize the chassis in the rack. 

  * Each rail extends to fit the depth of the rack. The rails are not a sliding shelf that allow pulling the chassis out of the rack to gain access to the chassis' sides. 

  * Each rail kit can fit into either a 9.5 mm square hole equipment rack or a 7.1 mm round-hole equipment rack. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Some racks might be tapped, with threaded holes drilled directly into the rack's sheetmetal instead of square- or round-hole punchouts for cage nuts. The rail kit for the server is not currently supported in tapped (threaded hole) racks. Do not attempt to install the chassis in a tapped (threaded-hole) equipment rack. 

* * *  
  
---|---  


The rails are shipped in the accessory kit with each chassis, and each rail kit will contain a left and right side as a matched pair. Both sides must be installed in the rack to securely support the chassis. 

If you ordered multiple UCS X9508 chassis, you might receive both types of rail kit. For example, in a shipment of 4 chassis, the shipment might have all one type of rail kit, or a few chassis with each type of rail kit. 

Compare the two types of rail kits:

Figure 4. Two Types of Rail Kits  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308950.jpg)

The rail kits are similar in size, function, and construction with a few exceptions:

  * the type of release tab at the top corner of the rail

  * the type of locator pegs, either round or square depending on whether you have a round-hole or square-hole rack. The locator pegs temporarily hold the rail in the rack to allow free use of both hands. 

  * the positioning of the screw holes at the rear of the rails


## Installing the Chassis

This section describes how to install the chassis in either a square-hole unthreaded or round-hole unthreaded equipment rack. This two-part process consists of installing the rails into the rack, then installing the chassis into the rack and onto the rails. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

The fully configured chassis weighs approximately 400s lbs (163.29 kg)! Never attempt to lift the chassis by yourself. Instead, use a chassis lift or some other device to lift and bear the weight of the chassis while you are installing it. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

If the rack has wheels, ensure that the brakes are engaged, the stabilizing pads are extended, or that the rack is otherwise stabilized. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/warn.gif)  
**Warning** | 

* * *

The plug-socket combination must be accessible at all times, because it serves as the main disconnecting device. **Statement 1019**

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

When connecting the chassis to facility power, make sure not to overload the capacity of a PDU or power strip. For example, do not connect all PSUs to one PDU or power strip that is not capable of carrying the total power draw of the chassis. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

Watch your hands and fingers whenever you handle the chassis, modules, nodes, and components! Narrow vertical or horizontal spaces in situations including, but not limited to, moving the chassis into or out of the shipping container or equipment rack can cause pinch hazards for your hands and fingers.  Although they do not eliminate the possibility of pinching, the chassis has defined grasp points to facilitate handling and moving it. For information about chassis grasp points, see Handling the Chassis. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

To complete the installation, the chassis must be connected to earth ground, which requires a ground lug that Cisco provides, or an equivalent. See "Ground Lug" in Earth Ground Considerations. 

* * *  
  
---|---  
  
Where applicable, the following installation topics have options for square-hole and round-hole racks. Pick the appropriate topic based on your rack type. 

  * Installing the Rails, Square-Hole Rack
  * Installing the Rails, Round-Hole Rack
  * Rail Installation Layout, Square-Hole Rack
  * Rail Installation Layout, Round-Hole Rack
  * Installing the Top Cable Management Arms
  * Installing the Ground Bracket and Bottom Cable Management Arms
  * Inserting the Chassis into a Square-Hole Rack
  * Inserting the Chassis into a Round-Hole Rack
  * Installing Rear Mounting Brackets, Square-Hole Rack
  * Installing Rear Mounting Brackets, Round-Hole Rack
  * Completing Installation
  * Choosing Earth Ground Option
  * Attaching Cable Management Trays


### Installing the Rails, Square-Hole Rack

Use the following task to install the rail kit into a square-hole unthreaded equipment rack by using twelve, M6x1.00 square-hole cage nuts. 

#### Before you begin

Make sure that you have marked the correct cage nut and rail locations on the rack by using the illustrations of the rack installation templates. See Rail Installation Templates. 

#### Procedure

* * *

**Step 1** |  Adjust the length of the rail by sliding the ends of the rail back and forth until they match the depth of the rack.   
---|---  
**Step 2** |  At the front of the rack, use the front installation template to position the two locator pegs on the rail with the corresponding location in the rack. See Front Install Template.  The locator pegs will hold the rail in the rack so that you don't have to hold the rail in place.   
**Step 3** |  At the rear of the rack, use the rear installation template to position the two locator pegs on the rail with the corresponding location in the rack. See Rear Install Template.   
**Step 4** |  Repeat the previous steps to install the other rack rail.  Figure 5. Install Rails into Front of the Rack  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308937.jpg)  
**Step 5** |  (Optional) Use a tape measure and level to verify that the rack rails are horizontal and at the same height.   
**Step 6** |  At the front of the rack, refer to the template, then insert a screw in each front rail to secure each rail to the rack at the correct location.  Figure 6. Secure the Rail at the Front to the Rack  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308939.jpg)  
**Step 7** |  At the rear of the rack, refer to the template, then insert a screw in each rear rail to secure each rail to the rack at the correct location.   
**Step 8** |  Figure 7. Secure the Rail at the Rear of the Rack  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308948.jpg)  
  
* * *

#### What to do next

Verify that the rails are correctly installed. See Rail Installation Layout, Square-Hole Rack. 

### Installing the Rails, Round-Hole Rack

Use the following task to install the rail kit into a round-hole unthreaded equipment rack by using twelve, M6x1.00 round-hole spring nuts. 

#### Before you begin

Make sure that you have marked the correct cage nut (spring nut) and rail locations on the rack by using the illustrations of the rack installation templates. See Rail Installation Templates. 

#### Procedure

* * *

**Step 1** |  Adjust the length of the rail by sliding the ends of the rail back and forth until they match the depth of the rack.   
---|---  
**Step 2** |  At the front of the rack, use the front installation template to position the two locator pegs on the rail with the corresponding location in the rack. See Front Install Template.  The locator pegs will keep the rail in the rack so that you don't have to hold the rail in place.   
**Step 3** |  At the rear of the rack, use the rear installation template to position the two locator pegs on the rail with the corresponding location in the rack. See Rear Install Template.   
**Step 4** |  Repeat the previous steps to install the other rack rail.  Figure 8. Install Rails into Front of the Rack  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540665.jpg)  
**Step 5** |  (Optional) Use a tape measure and level to verify that the rack rails are horizontal and at the same height.   
**Step 6** |  At the front of the rack, refer to the template, then insert a screw in each front rail to secure each rail to the rack at the correct location.  Figure 9. Secure the Rail at the Front to the Rack  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540667.jpg)  
**Step 7** |  At the rear of the rack, refer to the template, then insert a screw in each rear rail to secure each rail to the rack at the correct location.   
**Step 8** |  Figure 10. Secure the Rail at the Rear of the Rack  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308948.jpg)  
  
* * *

#### What to do next

Verify that the rails are correctly installed. See Rail Installation Layout, Round-Hole Rack. 

### Rail Installation Layout, Square-Hole Rack

Before installing the chassis in the rack, compare the rail installation in the rack against the following layout images. If the rail installation is different than what is shown in each layout, remove the rails and reinstall them. 

Figure 11. Front Rail Layout, Both Rail Kits  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308938.jpg) ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540754.jpg) |  Cage Nut, square-hole rack  
---|---  
![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540755.jpg) |  Empty RETMA Rail Hole, square-hole rack  
![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540756.jpg) |  Locator Peg for Rail Kit  
![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540758.jpg) and ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540757.jpg) |  Mounting Screw for Rail Kit  
Figure 12. Rear Rail Layout, Both Rail Kits  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308947.jpg) ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540754.jpg) |  Cage Nut, square-hole rack  
---|---  
![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540755.jpg) |  Empty RETMA Rail Hole, square-hole rack  
![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540756.jpg) and  |  Locator Peg for Rail Kit  
![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540758.jpg) and ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540757.jpg) |  Mounting Screw for Rail Kit  
  
### Rail Installation Layout, Round-Hole Rack

Before installing the chassis in the rack, compare the rail installation in the rack against the following layout images. If the rail installation is different than what is shown in each layout, remove the rails and reinstall them. 

Figure 13. Front Rail Layout, Both Rail Kits  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540666.jpg) ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540759.jpg) |  Spring Nut for round-hole rack  
---|---  
![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540760.jpg) |  Empty RETMA Rail Hole, round-hole rack  
![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540761.jpg) |  Locator Peg for Rail Kit  
![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540762.jpg) |  Mounting Screw for Rail Kit  
Figure 14. Rear Rail Layout, Both Rail Kits  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540674.jpg) ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540759.jpg) |  Spring Nut for round-hole rack  
---|---  
![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540760.jpg) |  Empty RETMA Rail Hole, round-hole rack  
![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540761.jpg) |  Locator Peg for Rail Kit  
![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540762.jpg) |  Mounting Screw for Rail Kit  
  
### Installing the Top Cable Management Arms

The accessory kit contains two cable management assemblies, each one consisting of three cable management arms and three cable ties. The cable management assemblies facilitate gathering and organizing the chassis power cables. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The server also has cable management trays (UCSX-9508-CMA) for gathering and organizing the cables from the IFMs and X-Fabric modules. 

* * *  
  
---|---  
  
In this topic, top and bottom refer to the location on the chassis. Cable management arms are interchangeable, so there is no specific top and bottom cable arm. 

Each cable management assembly is for a set of three PSUs. The top cable management arms attach to the top set of PSUs in the chassis. The bottom cable management arms attach a grounding bracket for the bottom set of PSUs, so the installation procedure is slightly different. See Installing the Ground Bracket and Bottom Cable Management Arms. 

Use this task to attach the cable management assemblies to the chassis before installing the chassis in the rack.

#### Procedure

* * *

**Step 1** |  Align the captive screws in the cable management sheet metal with the threaded standoffs on the chassis.   
---|---  
**Step 2** |  Using a #2 Phillips-head screwdriver, attach the cable management arms to the server chassis by tightening the captive screws.  Figure 15. Attaching the Top Cable Management Arms to the Chassis  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308904.jpg)  
**Step 3** |  Adjust the cable tie horizontally to align with where you wish to grasp the power cable.  
**Step 4** |  You can use the cable ties to gather the power cables and secure the plugs in place.  Figure 16. Gathering Power Cables  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308966.jpg)  
  
* * *

#### What to do next

Attach the remaining cable management arms. See Installing the Ground Bracket and Bottom Cable Management Arms. 

### Installing the Ground Bracket and Bottom Cable Management Arms

The cable management arm (CMA) for the bottom set of PSUs contains an integrated ground lug that provides earth grounding for the chassis. The horizontal metal piece is the ground lug to which the grounding cable can be attached. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

In this topic, top and bottom refer to the specific cable management arms. Cable management arms are not interchangeable. The bottom CMA contains the integrated ground lug, but the top CMA does not. 

* * *  
  
---|---  
  
For the additional ground requirements, see Earth Ground Considerations. 

#### Procedure

* * *

Attach the bottom cable management arm to the chassis. 

  1. Align the long side of the ground bracket with the threaded standoff on the chassis.
  2. Align the captive screws in the cable management arm with the threaded standoffs on the chassis.  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472424.jpg) |  1 |  Threaded Standoffs on chassis |  2 |  Bottom CMA, long side aligned with standoffs  
---|---|---|---  
3 |  Captive Screws on CMA  |  |   
  3. Using a #2 Phillips-head screwdriver, secure the bottom cable management arms to the server chassis by tightening the captive screws. 


  
  
* * *

### Inserting the Chassis into a Square-Hole Rack

#### Before you begin

If you have not already verified that the rails are installed as indicated in the front and rear layouts, do so now. See Rail Installation Layout, Square-Hole Rack. 

Also, make sure to review Installation Notes and Warnings for the Cisco UCS X9508 Server Chassis. 

The chassis must be grounded by a ground lug that Cisco provides, or an equivalent. See "Ground Lug" in Earth Ground Considerations. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Before beginning this procedure, make sure that the rails are correctly installed, and all the rail kits' mounting screws are installed and tightened. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

Watch your hands and fingers whenever you handle the chassis, modules, nodes, and components! Narrow vertical or horizontal spaces in situations including, but not limited to, moving the chassis into or out of the shipping container or equipment rack can cause pinch hazards for your hands and fingers.  Although they do not eliminate the possibility of pinching, the chassis has defined grasp points to facilitate handling and moving it. For information about chassis grasp points, see Handling the Chassis. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/tip.gif)  
**Tip** | 

* * *

You will find it easier to move the chassis if you have additional people to help you.

* * *  
  
---|---  
  
#### Procedure

* * *

**Step 1** |  Using a scissor jack, chassis lift, or other mechanical device, lift the chassis and position it so that you can slide it into the rack.   
---|---  
**Step 2** |  Slide the chassis into the rack until the front flange is flat against the cage nuts.  Figure 17. Inserting the Chassis into the Rack  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308944.jpg)  
**Step 3** |  At the front of the chassis, remove each of the side trim panels from the chassis.  The side trim panels are attached magnetically, so you should be able to easily pull them off. Removing the side trim panels exposes the screw holes in each of the front mounting brackets. |  **Note** |  Keep the side trim panels in a safe location nearby. You will replace them when the chassis is installed.   
---|---  
Figure 18. Detach the Chassis Side Trim Panels  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308942.jpg)  
**Step 4** |  At the front of the chassis, use a #3 Phillips-head screwdriver to insert and tighten the eight M6 x 20mm screws through the front mounting flanges.  Figure 19. Securing the Front of the Chassis to the Rack  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308943.jpg)  
**Step 5** |  Choose the appropriate option:

  1. If your chassis will ship per-installed in a rack, attach the rear mounting brackets. If you plan to install and ship your chassis in a shippable rack, attach the rear mounting brackets. See Installing Rear Mounting Brackets, Square-Hole Rack. 
  2. If you will be installing the chassis in a stationary rack, continue the installation procedure. See Completing Installation. 

  
  
* * *

### Inserting the Chassis into a Round-Hole Rack

#### Before you begin

If you have not already verified that the rails are installed as indicated in the front and rear layouts, do so now. See Rail Installation Layout, Round-Hole Rack. 

Also, make sure to review Installation Notes and Warnings for the Cisco UCS X9508 Server Chassis. 

The chassis must be grounded by a ground lug that Cisco provides, or an equivalent. See "Ground Lug" in Earth Ground Considerations. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Before beginning this procedure, make sure that the rails are correctly installed, and all the rail kits' mounting screws are installed and tightened. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

Watch your hands and fingers whenever you handle the chassis, modules, nodes, and components! Narrow vertical or horizontal spaces in situations including, but not limited to, moving the chassis into or out of the shipping container or equipment rack can cause pinch hazards for your hands and fingers.  Although they do not eliminate the possibility of pinching, the chassis has defined grasp points to facilitate handling and moving it. For information about chassis grasp points, see Handling the Chassis. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/tip.gif)  
**Tip** | 

* * *

You will find it easier to move the chassis if you have additional people to help you.

* * *  
  
---|---  
  
#### Procedure

* * *

**Step 1** |  Using a scissor jack, chassis lift, or other mechanical device, lift the chassis and position it so that you can slide it into the rack.   
---|---  
**Step 2** |  Slide the chassis into the rack until the front flange is flat against the cage nuts (spring nuts).  Figure 20. Inserting the Chassis into the Rack  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540671.jpg)  
**Step 3** |  At the front of the chassis, remove each of the side trim panels from the chassis.  The side trim panels are attached magnetically, so you should be able to easily pull them off. Removing the side trim panels exposes the screw holes in each of the front mounting brackets. |  **Note** |  Keep the side trim panels in a safe location nearby. You will replace them when the chassis is installed.   
---|---  
Figure 21. Detach the Chassis Side Trim Panels  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540669.jpg)  
**Step 4** |  At the front of the chassis, use a #3 Phillips-head screwdriver to insert and tighten the eight M6 x 20mm screws through the front mounting flanges.  Figure 22. Securing the Front of the Chassis to the Rack  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540670.jpg)  
**Step 5** |  Choose the appropriate option:

  1. If your chassis will ship pre-installed in a rack, attach the rear mounting brackets. If you plan to install and ship your chassis in a shippable rack, attach the rear mounting brackets. See Installing Rear Mounting Brackets, Round-Hole Rack. 
  2. If you will be installing the chassis in a stationary rack, continue the installation procedure. See Completing Installation. 

  
  
* * *

### Installing Rear Mounting Brackets, Square-Hole Rack

Use this procedure to install the rear mounting (tie down) brackets (UCSX-9508-RACKBK) for a chassis that is not pre-installed in a rack. 

#### Before you begin

If the chassis is shipped pre-installed in a rack, the rear mounting brackets are already attached. 

#### Procedure

* * *

**Step 1** |  At the rear of the chassis, use your hands to install each rear mounting bracket, which has a folded tab at the top and a folded metal hook at the bottom. 

  1. Slide the hook the into the cutout in the chassis side wall.
  2. Slide each rear mounting bracket until the tab seats into the emboss in the chassis top.

Figure 23. Attaching Rear Mounting Brackets, Square-Hole Rack  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472425.jpg)  
---|---  
**Step 2** |  Holding the rear mounting brackets in place, use the #3 Phillips-head screwdriver to insert the 8 M6 x 20mm screws through the rear mounting brackets, then tighten the screws to secure the rear of the chassis to the rear of the rack.  Figure 24. Securing the Chassis to the Rack, Square-Hole Rack  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472426.jpg)  
  
* * *

#### What to do next

Complete installing the chassis into the rack. Go to Completing Installation. 

### Installing Rear Mounting Brackets, Round-Hole Rack

Use this procedure to install the rear mounting (tie down) brackets (UCSX-9508-RACKBK) for a chassis that is not pre-installed in a rack. 

#### Before you begin

If the chassis is shipped pre-installed in a rack, the rear mounting brackets are already attached. 

#### Procedure

* * *

**Step 1** |  At the rear of the chassis, use your hands to install each rear mounting bracket, which has a folded tab at the top and a folded metal hook at the bottom. 

  1. Slide the hook the into the cutout in the chassis side wall.
  2. Slide each rear mounting bracket until the tab seats into the emboss in the chassis top.

Figure 25. Attaching the Rear Mounting Brackets  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472427.jpg)  
---|---  
**Step 2** |  Holding the rear mounting brackets in place, use the #3 Phillips-head screwdriver to insert the 8 M6 x 20mm screws through the rear mounting brackets, then tighten the screws to secure the rear of the chassis to the rear of the rack.  Figure 26. Securing the Rear of the Chassis to the Rack  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472428.jpg)  
  
* * *

#### What to do next

Complete installing the chassis into the rack. Go to Completing Installation. 

### Completing Installation

Continue with installing the chassis.

#### Procedure

* * *

**Step 1** |  Verify that all the front and rear mounting screws for the rails and the chassis are tight, and the chassis is secured to the rack.   
---|---  
**Step 2** |  At the front of the chassis, attach the side trim panels. The side trim panels attach magnetically, so you don't need any tools.  
**Step 3** |  Making sure that all people and equipment are not under the chassis, lower and remove the lift.  
**Step 4** |  Install any additional IFMs, PSUs, nodes or other chassis components, if needed.  
**Step 5** |  To power up the chassis, connect the appropriate power cables to the inlet connector corresponding to each installed power supply, and then connect the other end of the cables to the power source. To determine the number of power supplies needed for a given configuration, use the [Cisco UCS Power Calculator](https://mainstayadvisor.com/Go/Cisco/Cisco-UCS-Power-Calculator.aspx) tool.  |  **Note** |  Both grids in a power redundant system should have the same number of power supplies. If your system is configured for grid power (N+N redundancy), slots 1, 2, and 3 are assigned to grid 1, and slots 4, 5, and 6 are assigned to grid 2. If fewer than six power supplies (PS) are configured in grid redundant mode, they should be equally distributed between the grid 1 and grid 2 slots.   
---|---  
**Step 6** |  Attach any remaining cables to provide fabric connectivity for the chassis and nodes and do a visual inspection of LEDs to ensure the chassis and its components are operating in runtime.   
  
* * *

### Choosing Earth Ground Option

The Cisco UCS X9508 server chassis supports connection to facility earth ground through either of the following options:

  * side mount, which supports connecting the ground cable directly to the chassis through a ground point on one side of the chassis. For this option, go to Connecting Side-Mount Earth Ground. 

  * rear mount, which supports connecting the ground cable to a ground bracket that attaches to one of the rear mounting brackets at the rear of the chassis. For this option, go to Connecting Rear-Mount Earth Ground. 


Choose the option that is appropriate for your installation. Both options require you to assemble the ground cable by crimping a ground lug onto the end of the ground cable. For information about the ground lug, see "Ground Lug" in Earth Ground Considerations. 

  * Connecting Side-Mount Earth Ground
  * Connecting Rear-Mount Earth Ground


#### Connecting Side-Mount Earth Ground

To connect side-mount earth ground you will connect a ground lug to a ground cable, then attach the cable to the designated earth ground point on the chassis sheet metal. The designated earth ground is on the side of the chassis. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The chassis also has a rear-mount option for earth ground by using a specific ground bracket that attaches to the rear of the chassis. For more information, see Connecting Rear-Mount Earth Ground. 

* * *  
  
---|---  
  
The facility ground cable must be terminated with the ground lug provided by Cisco, or an equivalent. For more information, see "Ground Lug" in Earth Ground Considerations. 

##### Procedure

* * *

**Step 1** |  Locate the two screw holes for the side-mount attachment point for earth ground.  The side-mount attachment point is designated with the earth ground symbol (![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309519.jpg) ).  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472429.jpg)  
---|---  
**Step 2** |  Assemble the ground cable.

  1. Use a wire-stripping tool to remove approximately 0.75 inches (19 mm) of the covering from the end of the grounding cable.
  2. Insert the stripped end of the grounding cable into the open end of the grounding lug. We recommend 6-AWG wire for the U.S. installations. Make sure to use the proper grounding cable and grounding wire as appropriate for your country or region.    
![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309378.jpg)  

  3. Use a crimping tool to secure the grounding cable in the grounding lug.
  4. Prepare the other end of the grounding cable and connect it to an appropriate ground point at the facility.  |  **Note** |  When the chassis is fully installed, the side-mount earth ground point should be in front of the rear mounting brackets. As a result, you should have enough space to attach the ground cable.   
---|---  

  
**Step 3** |  Attach the grounding cable to the grounding point on the side of the chassis.

  1. Position the ground lug.
  2. Align the terminal holes in the ground lug with the terminal holes in the side of the chassis.
  3. Using a #2 Phillips screwdriver, insert and tighten two M5 x 10mm pan-head screws to secure the grounding cable to the side of the chassis.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309496.jpg)

|  1 |  Assembled ground cable with lug positioned on chassis ground point |  2 |  Screw down ground cable to secure it to the side-mount ground point  
---|---|---|---  
  
* * *

#### Connecting Rear-Mount Earth Ground

Connecting the chassis to facility earth ground is supported through the chassis ground lug, which is installed at the side of the bottom set of PSUs. 

The facility grounding cable must be terminated with the ground lug provided by Cisco, or an equivalent. For more information, see "Ground Lug" in Earth Ground Considerations. 

Use this procedure to connect the chassis to earth ground. 

##### Before you begin

This procedure assumes that you have already attached the bottom cable management arm with the integrated grounding lug. For information, see Installing the Ground Bracket and Bottom Cable Management Arms. 

##### Procedure

* * *

**Step 1** |  Verify that the bottom CMA and ground lug is correctly installed. If not, install it now. See Installing the Ground Bracket and Bottom Cable Management Arms.  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472430.jpg) |  1 |  Bottom CMA with integrated ground lug |  2 |  Terminal holes for attaching the ground cable  
---|---|---|---  
**Step 2** |  Assemble the ground cable.

  1. Use a wire-stripping tool to remove approximately 0.75 inches (19 mm) of the covering from the end of the grounding cable.
  2. Insert the stripped end of the grounding cable into the open end of the grounding lug. We recommend 6-AWG wire for the U.S. installations. Make sure to use the proper grounding cable and grounding wire as appropriate for your country or region.    
![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309378.jpg)  

  3. Use a crimping tool to secure the grounding cable in the grounding lug.
  4. Prepare the other end of the grounding cable and connect it to an appropriate ground point at the facility. 

  
**Step 3** |  Attach the ground cable to the ground lug.

  1. Position the ground cable on top of the ground lug.
  2. Align the terminal holes in the ground lug with the terminal holes in the ground bracket.
  3. Using a #2 Phillips screwdriver, insert and tighten two M5 x 10mm pan-head screws to secure the ground cable to the ground lug.  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472431.jpg)

  
**Step 4** |  Route the ground cable out of the way of the chassis, making sure not to damage the ground cable, for example, by exceeding its bend radius.   
**Step 5** |  After the chassis is connected to earth ground, connect PSU cables to power up the chassis.   
  
* * *

### Attaching Cable Management Trays

The Cisco UCS X9508 server chassis offers up to four cable management trays (UCSX-9508-CMA) to organize the cables for the intelligent fabric module (IFM) cables. The trays are interchangeable, so you can use them for either IFM's cables. There are no specific cable management trays for the top and bottom of the chassis. 

You can use one tray for each IFM installed in the Cisco UCS X9508 server chassis but Cisco recommends that you use one tray for all IFM cables. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The chassis also has cable management arms, which organize the PSU cables. The cable management arms are different from the cable management tray, which organizes IFM cables.  Because the cable management tray sits in front of an IFM , you should remove the cable management tray to allow access to the IFM. For example, if you need to access IFM 2, you should remove the cable management tray 2 

* * *  
  
---|---  
  
Cable management trays attach to the server chassis by hooks at the top rear of each tray.

![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309497.jpg)

To install or remove the cable management tray, use the following procedures:

  * Installing the Cable Management Tray

  * Removing the Cable Management Tray


  * Installing the Cable Management Tray
  * Removing the Cable Management Tray


#### Installing the Cable Management Tray

For IFM cables, you can use the cable management tray to gather and organize the cables. The tray attaches to notches in the server chassis sheet metal. 

Use the following procedure to install the cable management tray. 

##### Procedure

* * *

**Step 1** |  Orient the cable management tray so that the hooks are at the top and facing toward the chassis.   
---|---  
**Step 2** |  Attach the cable management tray to the chassis. 

  1. Align the hooks on the cable management tray with the rectangular notches in the server chassis. 
  2. Holding the cable management tray level, insert the hooks into the notches. 
  3. When the cable management tray is flush against the chassis, push down to seat the hook into the notch. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309498.jpg)

  
**Step 3** |  Repeat this procedure as needed to install the other cable management trays, if needed.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309499.jpg)  
**Step 4** |  Attach any IFM cables as needed.   
  
* * *

#### Removing the Cable Management Tray

Use the following procedure to remove the cable management tray(s). 

##### Procedure

* * *

**Step 1** |  (Optional) Remove or lift the cables to allow easier access to the cable management tray.   
---|---  
**Step 2** |  Detach the cable management tray from the chassis. 

  1. At each corner of the cable management tray, apply equal pressure to slide the tray upward in the chassis notch until it can no longer slide up.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309501.jpg)
  2. Holding the cable management tray level, pull it towards you to detach the tray from the chassis.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309502.jpg)

  
  
* * *

## Removing the Chassis from a Rack

### Procedure

* * *

**Step 1** |  Use Cisco Intersight to do the following:

  1. Shut down the OS on all nodes in the chassis.
  2. Disable the Smart Call Home feature.
  3. Decommission the chassis.

  
---|---  
**Step 2** |  Disconnect the power cords and networking cables from the chassis.  
**Step 3** |  Remove all modules, fans, power supplies, and nodes from the chassis to lighten its weight.  
**Step 4** |  Remove the screws holding the front rack-mount flange to the rack.  
**Step 5** |  With two people holding the chassis, make sure that its weight is fully supported. |  **Important** |  Watch your hands and fingers whenever you handle the chassis, modules, compute nodes, and components! Narrow vertical or horizontal spaces in situations including, but not limited to, moving the chassis into or out of the shipping container or equipment rack can cause pinch hazards for your hands and fingers.  Although they do not eliminate the possibility of pinching, the chassis has defined grasp points to facilitate handling and moving it. For information about chassis grasp points, see Handling the Chassis.   
---|---  
**Step 6** |  Gently slide the chassis off the rails, and out of the rack.  
**Step 7** |  Replace the modules, fans, power supplies, and nodes in the server chassis. If you are returning the product, go to Repacking the Chassis.   
  
* * *

## Repacking the Chassis

If you need to repack the chassis, remove it from the rack by following the steps in the Removing the Chassis from a Rack section. 

When repacking the chassis for return shipment, be aware of the following. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/warn.gif)  
**Warning** | 

* * *

Only lift an empty chassis! Make sure that all PSUs, fans, nodes, Intelligent Fabric Modules, and X-Fabric Modules are removed from the chassis before moving it out of the rack and packing it for shipment. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/warn.gif)  
**Warning** | 

* * *

When the chassis is out of the rack, make sure to install the handles onto the chassis before putting the chassis on the bottom palette. The handles are also securing brackets that bolt the chassis onto the bottom pallet. 

* * *  
  
---|---  
  
If possible, use the original packing materials and container to pack the chassis. 

If needed, you can order spare packaging from Cisco by using PID UCSX-9508-PKG=.

If you are returning the chassis to Cisco, contact your Cisco customer service representative to arrange for return shipment to Cisco. 

---

## Page 5: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x9508/install/b-ucs-x9508-install/m-installing-and-removing-components.html

# Installing and Removing Components

This chapter contains the following topics:

##  Components

The following figure shows an empty Cisco UCS X9508 server chassis and identifies the front, back, and vertical node slots, and horizontal module slots. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Before you remove or install components, please ensure that all software applications are shut down and management software is in a good state. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Whenever you remove a module from the chassis for an extended period of time, always replace the module with the appropriate blank panel. Failing to do so can result in heating and EMI issues. Blank panels can be ordered from Cisco Systems. 

* * *  
  
---|---  
Figure 1. View of Cisco UCS X9508 Server Chassis, Right Side  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308908.jpg)

The side of the chassis has no handles because the chassis is heavy, and not intended to be lifted unless you are using a scissor lift or another type of mechanical lift device to bear the weight of the chassis. The right side of the chassis has the PSU Keying Bracket which enforces proper PSU orientation as well as proper PSU type. 

Figure 2. View of UCS X9508 Server Chassis, Left Side  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308906.jpg)

The left side of the chassis has no handles.

Figure 3. View of Empty Cisco UCS X9508 Chassis, Front  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308905.jpg) 1 |  Node slots (8). Each slot is numbered horizontally below each slot.  Compute nodes and PCIe nodes can be inserted vertically and connect to the power socket for each slot.  |  2 |  PSU bays (6). Each PSU bay is numbered vertically to the right of the bay.  Each PSU bay is keyed so that the PSU inserts only one way.   
---|---|---|---  
  
The front of the chassis accepts up to 8 single-slot or 4 dual-slot compute nodes with connections for power and basic signaling through the per-slot socket connections to the midplane. The front of the server chassis also hosts up to 6 PSUs providing power to the chassis power plane through internal connectors. PSUs are numbered one through six with PSU bay one as the topmost slot and PSU bay 6 on the bottom. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Any node slot that is not occupied must have a compute node blank panel (UCSX-9508-FSBK) installed.

* * *  
  
---|---  
Figure 4. View of the UCS X9508 Server Chassis, Rear View  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308907.jpg) 1 |  Power Entry Modules (2) Each PEM houses three IEC 320 compatible C20 power inlets inlet facility power.  |  2 |  IFM slots (2)  
---|---|---|---  
3 |  Fan Bays (4) Fans are numbered 1 through 4 with fan 1 as the leftmost.  |  4 |  Expansion Slots (2)  
  
The top of the chassis rear contains up to two Intelligent Fabric Modules (IFMs). Power connections and minimal signaling are supported through the per-slot socket connections to the midplane. Three vertically stacked Power Entry Module (PEM) connectors are also supported, which correspond with PSUs one through three, with PSU one as the topmost connector. 

The middle of the chassis rear houses up to four fan modules and power is supplied through one connector per fan module. Fans are numbered from one to four with Fan 1 being the leftmost fan, and Fan 4 being the right most. 

The bottom of the chassis rear houses two active fan modules. Power connections and minimal signaling are supported through the per-slot socket connections to the midplane. Three vertically stacked PEM connectors are also supported, which correspond with PSUs four through six, with PSU four as the topmost connector. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Before you install, operate, or service the system, see the [Regulatory Compliance and Safety Information for Cisco UCS](http://www.cisco.com/en/US/docs/unified_computing/ucs/hw/regulatory/compliance/ucs_regulatory_compliance_Information.html) for important safety information. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/warn.gif)  
**Warning** | 

* * *

IMPORTANT SAFETY INSTRUCTIONS  This warning symbol means danger. You are in a situation that could cause bodily injury. Before you work on any equipment, be aware of the hazards involved with electrical circuitry and be familiar with standard practices for preventing accidents. Use the statement number provided at the end of each warning to locate its translation in the translated safety warnings that accompanied this device. Statement 1071  **SAVE THESE INSTRUCTIONS**

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/warn.gif)  
**Warning** | 

* * *

This unit is intended for installation in restricted access areas. A restricted access area can be accessed only through the use of a special tool, lock and key, or other means of security. Statement 1017 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/warn.gif)  
**Warning** | 

* * *

Only trained and qualified personnel must be allowed to install, replace, or service this equipment. Statement 1030 

* * *  
  
---|---  
  
  * Cisco UCS 9108 25G IFM Components
  * Cisco UCS 9108 100G IFM Components
  * Cisco UCS X9416 Fabric Module Components
  * Cisco UCS X9516 Fabric Module Components
  * Cisco UCS X-Fabric Module Blank Components


### Cisco UCS 9108 25G IFM Components

The Cisco UCS 9108 25G Intelligent Fabric Module has the following board-level components.

Figure 5. UCS 9108 25G Intelligent Fabric Module, Component View  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308929.jpg) 1 |  Fans (UCSX-RSFAN=), three, which are numbered 1 through 3 starting with the left fan. |  2 |  One M.2 mini storage module slot  
---|---|---|---  
3 |  SFP28 Optical Ports.  Ports are arranged in two groups of four physical ports. Port number 1 is the left port in this group, and port number 4 is the right port in the group.  |  4 |  SFP28 Optical Ports.  Ports are arranged in two groups of four physical ports. Port number 5 is the left port in this group, and port number 8 is the right port in the group.   
5 |  IFM ejector handles, left and right |  |   
  
### Cisco UCS 9108 100G IFM Components

The Cisco UCS 9108 Intelligent Fabric Module (UCS-I-9108-100G) has the following board-level components.  Figure 6. UCS 9108 100G Intelligent Fabric Module, Component View  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308930.jpg) 1 |  Fans, (UCSX-RSFAN=), three, which are numbered 1 through 3 starting with the left fan |  2 |  One M.2 mini storage module slot  
---|---|---|---  
3 |  QSFP28 Optical Ports.  Ports are arranged in two groups of four physical ports. Ports are stacked in vertical pairs, with two ports in each vertical port stack.  Port number 1 is the top port of the left port pair in this group, and port number 3 is the top port of the right port pair in the group.  |  4 |  QSFP28 Optical Ports.  Ports are arranged in two groups of four physical ports. Ports are stacked in vertical pairs, with two ports in each vertical port stack.  Port number 5 is the top port in the left port pair of this group, and port number 7 is the top port in the right port pair of the group.   
5 |  IFM ejector handles, left and right |  |   
  
### Cisco UCS X9416 Fabric Module Components

The Cisco X9416 module (UCSX-F-9416) has the following components. 

Figure 7. UCS X9416 Fabric Module, Component View  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540442.jpg) 1 |  Fans (UCSX-RSFAN=), three, which are numbered 1 through 3 starting with the left fan |  2 |  Module Ejector Handles, Left and Right  
---|---|---|---  
  
### Cisco UCS X9516 Fabric Module Components

The Cisco UCS X9516 module (UCSX-FS-9516) X-Fabric Module has the following components. 

Figure 8. UCS X9516 Fabric Module, Component View  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525956.jpg) ![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The module has multiple heatsinks, but they are not field-serviceable.

* * *  
  
---|---  
**1** |  Fans (UCSX-RSFAN=), three, which are numbered 1 through 3 starting with the left fan |  **2** |  Module Ejector Handles, Left and Right  
---|---|---|---  
**3** |  PCIe Cage 2 Supports up to one PCIe Gen5 x16 card, or a filler blank if no card is present.  For information about valid PCIe cards, see [Cisco UCS X9516 Supported PCIe Cards](m-ucsx-9508-chassis-overview.html#r-x9516-supported-pcie-cards).  |  **Note** |  The PCIe cages are not field-replaceable. If a cage becomes damaged or needs to be replaced, you must RMA the X Fabric Module  
---|---  
**4** |  PCIe Cage 1 Supports up to one PCIe Gen5 x16 card, or a filler blank if no card is present.  For information about valid PCIe cards, see [Cisco UCS X9516 Supported PCIe Cards](m-ucsx-9508-chassis-overview.html#r-x9516-supported-pcie-cards).  |  **Note** |  The PCIe cages are not field-replaceable. If a cage becomes damaged or needs to be replaced, you must RMA the X Fabric Module  
---|---  
  
### Cisco UCS X-Fabric Module Blank Components

The Cisco X-Fabric Module Blank (UCSX-9508-RBLK) has the following components. 

Figure 9. UCS X-Fabric Module Blank, Component View  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308926.jpg) 1 |  Fans (UCSX-RSFAN=), three, which are numbered 1 through 3 starting with the left fan |  2 |  Module Ejector Handles, Left and Right  
---|---|---|---  
  
## Installing and Removing a Compute Node Blank

The UCS X9508 supports up to 8 compute nodes, with a minimum configuration of one compute node. If compute node slots do not contain a compute node, you must install a compute node blank. 

Use these procedures to replace a compute node blank:

  * Installing a Compute Node Blank

  * Removing a Compute Node Blank


  * Removing a Compute Node Blank
  * Installing a Compute Node Blank


### Removing a Compute Node Blank

Do not operate the server chassis with an empty compute node slot. Fill any empty compute node slots with either a blank (UCSX-9508-FSBK) or a compute node. 

Use this task to remove a compute node blank.

#### Procedure

* * *

**Step 1** |  Grasp the compute node by the finger holds.  Figure 10. Compute Node Blanks, Installed  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308917.jpg)  
---|---  
**Step 2** |  Pull the compute node blank towards you until it is completely removed from the chassis.  Notice that the module blank has indicators that show how to orient the blank. You will use this information when you install a blank.  Figure 11. Removing a Compute Node Blank  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309103.jpg)  
  
* * *

#### What to do next

Choose the appropriate option:

  * Installing a Compute Node

  * Installing a Compute Node Blank


### Installing a Compute Node Blank

If you remove a compute node, and you will not be installing another compute node, you must install a compute node blank. Do not operate the server with an empty compute node slot. The minimum configuration is 1 installed compute node, so in this configuration you need 7 module blanks installed. 

Compute node blanks are interchangeable within the same chassis or other chassis. 

Use this task to install a compute node blank

#### Procedure

* * *

**Step 1** |  Grasp the blank by the finger holds.   
---|---  
**Step 2** |  Hold the module blank vertically and align the module blank with the slot.  |  **Note** |  The module blank has an arrow and the word UP that show how to orient the blank. Also, if you attempt to install the blank with the wrong orientation, the module does not sit flush with the front of the chassis.   
---|---  
  
. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309104.jpg)  
  
**Step 3** |  Keeping the compute node blank vertical, slide it into the slot until the blank is flush with the face of the chassis.  Figure 12. Installing a Compute Node Blank  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308917.jpg)  
  
* * *

## Installing and Removing a Compute Node

The Cisco UCS X9508 server chassis supports full-height compute nodes. For details, see the Installation and Service Note for your compute nodes. See <http://www.cisco.com/en/US/products/ps10280/prod_installation_guides_list.html>

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

When working with the compute nodes, handle them carefully to avoid damage to the modules, connectors, and pins.

* * *  
  
---|---  
  
  * Installing a Compute Node
  * Removing a Compute Node


### Installing a Compute Node

Use this task to install a compute node in an empty slot.

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

When working with the compute nodes, handle them carefully to avoid damage to the modules, connectors, and pins! Make sure that the modules are level during insertion and slide them into the chassis slowly. 

* * *  
  
---|---  
  
#### Before you begin

If there is a module blank in the slot where you want to install a compute node, remove the blank now. See Removing a Compute Node Blank. 

Compute nodes are shipped with the ejector handles closed and locked. Each compute node has a release button in the center of the node that releases the ejectors from the locked position. 

#### Procedure

* * *

**Step 1** |  Press the release button at the center of the compute node faceplate to release the ejectors. |  **Caution** |  The ejectors have a hook at the pivoting end that attaches to the compute node. While you are inserting the compute node, keep the ejectors open as shown in the following illustration. If the ejectors are not open, the hook can be an obstruction while sliding the node into the chassis.   
---|---  
**Step 2** |  Holding the compute node vertical, align it with the empty module bay in the chassis.  The compute node is correctly aligned when the server top cover is pointing to the left.  Figure 13. Aligning and Installing a Compute Node  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309120.jpg)  
**Step 3** |  Keeping the compute node vertical, slowly slide it into the chassis. As the compute node is almost completely installed, you might feel some resistance. This resistance is normal. It occurs because the connectors at the rear of the compute node contacts the connector on the inside of the chassis.  |  **Caution** |  Make sure to apply even pressure when sliding the module into the chassis. Do not push down or pull up on the module handles, and do not apply more force to one ejector handle than the other.   
---|---  
**Step 4** |  When the compute node is almost completely installed, grasp the ejector handles and arc them toward each other.  This step seats the compute node into the connector. The compute node should power up. |  **Caution** |  Make sure to apply even pressure when closing the module ejector handles! Do not push down or pull up on the module handles, and do not apply more force to one ejector handle than the other.   
---|---  
**Step 5** |  Push the ejectors until they are parallel with the face of the compute node.  When the compute node is completely installed, the retention latches at the end of each handle click into place.   
  
* * *

### Removing a Compute Node

Use this task to remove a compute node.

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

When working with the compute nodes, handle them carefully to avoid damage to the modules, connectors, and pins! Make sure that the modules are level during removal and slide them out of the chassis slowly. 

* * *  
  
---|---  
  
#### Before you begin

Do not operate the server with an empty compute node slot. If you will not be installing a compute node in an empty slot, install a compute node blank to cover the empty slot. 

#### Procedure

* * *

**Step 1** |  Press the release button at the center of the compute node faceplate to disengage the ejector handles.   
---|---  
**Step 2** |  Grasp the ejector handles and pull them outward so that they arc vertically away from each other. While moving the compute node handles, you might feel some resistance. This resistance is normal. It occurs because the connectors at the rear of the compute node are unseating from the corresponding sockets in the chassis.  Also, when the compute node disconnects from the midplane, the server powers off. Figure 14. Removing a Compute Node  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309119.jpg)  
**Step 3** |  Grasp the compute node handles and slide the compute node partially out of the chassis.  Make sure to keep the compute node vertical while removing it.  |  **Caution** |  Make sure to apply even pressure when sliding the module out of the chassis. Do not push down or pull up on the module handles, and do not apply more force to one ejector handle than the other.   
---|---  
**Step 4** |  Place your other hand underneath the compute node to support it and slide the compute node completely out of the chassis.   
  
* * *

#### What to do next

Fill the empty compute node slot. Go to the appropriate option:

  * Installing a Compute Node

  * Installing a Compute Node Blank


## Installing and Removing Power Supplies

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The power supplies are keyed to work only with their respective power expansion module (PEM), depending on the chassis version. 

* * *  
  
---|---  
  
When in installing and removing power supplies, make sure that the minimum number of power supplies are active before replacing the other PSUs. For example, in a 3+3 grid power configuration, at least 3 PSUs must be active before replacing the other 3 units one at a time per grid. 

The PSUs are installed vertically along the side of the chassis.

![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308924.jpg)

  * PSU Population Rules
  * Installing a Power Supply
  * Removing a Power Supply


### PSU Population Rules

When you install PSUs, they must be equally divided into top and bottom PSU slots to ensure redundancy. See the following PSU population rules. 

  * For 2 PSUs: Install a PSU in slots 1 and 4. This is the minimum supported config. 

  * For 3 PSUs: Install a PSU in slots 1, 2, and 4. 

  * For 4 PSUs: Install a PSU in slots 1, 2, 4, and 5. 

  * For 5 PSUs: Install a PSU in slots 1, 2, 3, 4, and 5. 

  * For 6 PSUs: Install a PSU in all slots. 


Any slots that do not contain a PSU must be covered by a PSU blank.

### Installing a Power Supply

The Cisco UCS X9508 AC PSU does not have a discrete power switch. It powers on immediately when it is successfully connected to the power midplane. When installing a PSU, you must comply with the PSU population rules. See PSU Population Rules. 

PSUs are hot swappable with a minimum population of two in the chassis to provide redundancy. PSUs are interchangeable and none are reserved through the management software. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

When connecting the chassis to facility power, make sure not to overload the capacity of a PDU or power strip. For example, do not connect all PSUs to one PDU or power strip that is not capable of carrying the total power draw of the chassis. 

* * *  
  
---|---  
  
Use the following procedure to install the PSUs.

#### Procedure

* * *

**Step 1** |  Grasp the PSU with one hand.   
---|---  
**Step 2** |  Use your other hand to support the PSU, and holding it level, orient it with the PSU bay. The PSU is correctly oriented when the latch is facing you and parallel with the right side of the PSU bay.   
**Step 3** |  Holding the PSU level, slide it into the PSU bay.  |  **Note** |  When the PSU is almost all the way in, you will feel some resistance, which is normal. The resistance is the connector at the rear of the PSU meeting the power socket inside the chassis.  The PSU will power on when you have successfully seated it in its socket.   
---|---  
Figure 15. Installing a PSU  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308923.jpg)  
**Step 4** |  For each PSU that must be installed, repeat these steps.   
**Step 5** |  Verify the power supplies are operating by checking the power supply LEDs. See [LED Locations](m-ucsx-9508-chassis-overview.html#ID499) and [Interpreting LEDs](m-ucsx-9508-chassis-overview.html#ID544).  |  **Note** |  Both grids in a power redundant system should have the same number of power supplies. If your system is configured for grid power (N+N redundancy), slots 1, 2 and 3 are assigned to grid 1, and slots 4, 5, and 6 are assigned to grid 2. If fewer than six power supplies (PS) are configured in grid redundant mode, they should be equally distributed between the grid 1 and grid 2 slots.   
---|---  
  
* * *

### Removing a Power Supply

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

If you are using the Cisco UCS X9508 server chassis with one power supply, which is a non-redundant power configuration. Removing the power supply will cause the compute nodes and chassis to shut down. If you are using more than two power supplies, and you remove one of them (the minimum supported power configuration is 3 PSUs), the servers continue to operate as long as the other power supplies are sufficient to meet the power requirements of the number of compute nodes in the chassis. 

* * *  
  
---|---  
  
The PSU has a locking latch that secures the PSU in the chassis. You must unlock the latch to remove the PSU. You can expect some resistance as the PSU slides out due to its weight. 

#### Procedure

* * *

**Step 1** |  Place your thumb on the PSU locking latch at the vertical fingerhold on the right side of the blank's faceplate and allow your other fingers to rest along the side of the chassis.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309526.jpg)  
---|---  
**Step 2** |  Press the latch to unlock the PSU, then pull until it disengages from the power socket inside the chassis.  You will feel some resistance initially as the connector at the rear of the PSU unseats from the power socket inside the chassis.   
**Step 3** |  As you slide the PSU out of the chassis, use your other hand to support the PSU.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309528.jpg)  
**Step 4** |  Install a blank power supply filler panel if the power supply bay is to remain empty.  
  
* * *

#### What to do next

Choose the appropriate option: 

  * If you will be reinstalling a PSU, go to Installing a Power Supply

  * If you will be installing a PSU blank, go to Installing a PSU Blank. 


## Replacing a PSU Blank

PSU blanks (UCSX-9508-PSUBK) are interchangeable, but if you will be operating the server chassis without a PSU, the empty bay must be covered with a PSU blank. Replace a PSU blank when you remove a PSU but will not install another PSU in that PSU bay, or when you remove a PSU blank and need to cover the empty PSU bay. 

  * Removing a PSU Blank

  * Installing a PSU Blank


  * Removing a PSU Blank
  * Installing a PSU Blank


### Removing a PSU Blank

Use this procedure to remove a PSU blank.

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The PSU blank is a small plastic piece. It does not have a locking latch, so it slides out easily. 

* * *  
  
---|---  
  
#### Procedure

* * *

**Step 1** |  Place your thumb behind the vertical fingerhold on the right side of the blank's faceplate and allow your other fingers to rest along the side of the chassis.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309526.jpg)  
---|---  
**Step 2** |  Using your thumb, grasp the PSU blank by the vertical fingerhold and pull the PSU blank straight towards you.  The PSU should easily slide out of the chassis.  Figure 16. Removing a PSU Blank  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309527.jpg)  
  
* * *

#### What to do next

Choose the appropriate option: 

  * If you are installing a PSU, go to Installing a Power Supply. 

  * If you are installing a PSU blank, go to Installing a PSU Blank. 


### Installing a PSU Blank

The minimum supported power configuration for the UCS X9508 server chassis is three PSUs. If you will be operating the server chassis with an empty PSU bay, it must be covered with a PSU blank (UCSX-9508-PSUBK). 

Use this procedure to install a PSU blank.

#### Procedure

* * *

**Step 1** |  Grasp the PSU blank by the vertical finger hold on the right side of the blank's face.  
---|---  
**Step 2** |  Align the PSU blank so that the word UP is facing up, and the handle is parallel to the right side of the PSU bay.  
**Step 3** |  Insert the PSU blank until its faceplate is flush with the front of the server chassis.  Figure 17. Inserting a PSU Blank  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308983.jpg)  
  
* * *

## Replacing the PSU Keying Bracket

The PSU Keying bracket is attached to the right exterior side of the chassis. The bracket ensures that only the correct type of PSU can be installed, and that the PSU is inserted in correct orientation in the chassis. 

Use the following procedures to replace the PSU Keying bracket:

  * Removing the PSU Keying Bracket

  * Installing the PSU Keying Bracket


  * Removing the PSU Keying Bracket
  * Installing the PSU Keying Bracket


### Removing the PSU Keying Bracket

Use this procedure to remove the PSU Keying bracket. 

#### Before you begin

The chassis must be completely removed from the rack to provide access to the exterior of the chassis where the PSU Keying bracket will be installed. 

When the chassis is removed from the rack, make sure that you place the chassis on an ESD-safe workspace, for example, a rubberized mat. 

#### Procedure

* * *

**Step 1** |  If you have not already removed the chassis from the rack, do so now.  Go to [Removing the Chassis from a Rack](m-installation.html#ID487).  |  **Caution** |  Make sure to follow all safety requirements while uninstalling the chassis, including using a device, such as a mechanical lift, to bear the weight of the chassis.   
---|---  
**Step 2** |  With the chassis in an ESD-safe work area, locate the PSU Keying bracket on the right exterior side of the chassis. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309360.jpg)  
**Step 3** |  Using a T10 screwdriver, remove the six screws that attach the bracket to the chassis.  
**Step 4** |  Grasp the PSU keying bracket and detach it from the chassis.  
**Step 5** |  Keep the screws and bracket.   
  
* * *

#### What to do next

Installing the PSU Keying Bracket. 

### Installing the PSU Keying Bracket

Use this task to install a PSU Keying bracket (UCSX-9508-KEY-AC=).

#### Procedure

* * *

**Step 1** |  With the chassis on an ESD-safe work area, grasp the new PSU Keying Bracket, and align it with right exterior side of the chassis.   
---|---  
**Step 2** |  Place the bracket against the side of the chassis, aligning the screwholes in the bracket with the screwholes in the chassis.  
**Step 3** |  Insert the 6 screws into the screwholes. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309078.jpg)  
**Step 4** |  Using a T10 screwdriver, secure the bracket to the chassis by tightening each screw to snug.  If you have access to a torque wrench, tighten the screws to 6 in-lb.  
**Step 5** |  Reinstall the chassis:

  1. Insert the chassis into the rack.
  2. Reinstall the chassis components and reconnect any cables that were disconnected. For additional info, see [Installing the Chassis](m-installation.html#ID199). 

  
  
* * *

## Replacing the Power Entry Modules (PEMs)

The Cisco UCS X9508 chassis contains two power entry modules (PEMs). Each PEM (UCSX-9508-ACPEM=) is a grouping of 3 IEC 320 compatible C20 power inlets. The top PEM supports PSUs 1 through 3, and the bottom PEM supports PSUs 4 through 6. Each PEM is field replaceable. 

Use the following procedures to replace the PEMs:

  * Installing the Power Entry Modules

  * Removing the Power Entry Modules


  * Installing the Power Entry Modules
  * Removing the Power Entry Modules


### Installing the Power Entry Modules

Use this procedure to install a PEM (UCSX-9508-ACPEM=). 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The following task shows installing both PEMs. If you are installing only one PEM, you will need to tighten only the PEM screw for the replaced PEM, not both screws as shown in the illustrations. 

* * *  
  
---|---  
  
#### Before you begin

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**DANGER** | 

* * *

Follow all electrical safety precautions when working with facility power. Failure to do so can result in damage to the equipment or pose a risk of injury or death to personnel. 

* * *  
  
---|---  
  
#### Procedure

* * *

**Step 1** |  Grasp the PEM and orient it correctly.  The PEM is keyed so that you can insert it only one way.   
---|---  
**Step 2** |  Holding the PEM level, slide it into the PEM slot.  You might feel some resistance as the connector on the rear of the PEM meets the connector on the interior of the chassis.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309106.jpg)  
**Step 3** |  Using a T10 screwdriver, tighten the captive screws which are easily identifiable because they are next to the electrical ground icons on the chassis walls. 

  1. Tighten the exterior captive screws.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309108.jpg)
  2. Tighten the interior captive screws.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309110.jpg)

  
**Step 4** |  Reinstall the IFMs and expansion modules.

  1. Go to Installing an Intelligent Fabric Module. 
  2. Go to Installing a UCS X-Fabric Module Blank. 

  
**Step 5** |  Reconnect all power cables.  The chassis automatically powers on when it receives inlet power.   
  
* * *

### Removing the Power Entry Modules

PEMs support inlet power to the chassis from the facility. It is a best practice to remove all power from the system when replacing a PEM. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**DANGER** | 

* * *

Follow all electrical safety precautions when working with facility power. Failure to do so can result in damage to equipment or pose a risk of injury or death to personnel. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The following task shows removing both PEMs. If you are removing only one PEM, you will need to loosen only the PEM screw for the replaced PEM, not both screws as shown in the illustrations. 

* * *  
  
---|---  
  
#### Before you begin

The power entry modules (PEMs, UCSX-9508-ACPEM=) are connected to facility power, so you must disconnect facility power from the PEM that you will be removing. 

#### Procedure

* * *

**Step 1** |  Power down all compute nodes.  
---|---  
**Step 2** |  Remove any power cables that are attached to the PEM.   
**Step 3** |  Remove the IFMs and expansion modules.

  1. Go to Removing an Intelligent Fabric Module. 
  2. Go to Removing a UCS X-Fabric Module Blank. 

  
**Step 4** |  Using a T10 screwdriver, loosen the captive screws that attach the PEM to the chassis.  The captive screws are easily identifiable because they are next to the electrical ground icons on the chassis walls. 

  1. Loosen the exterior captive screws. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309107.jpg)
  2. Loosen the interior captive screws. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309109.jpg)

  
**Step 5** |  Grasp the PEM and slide it out of the chassis.  When you remove a PEM, you must replace it with another one. Do not operate the system with an empty PEM slot. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309105.jpg)  
  
* * *

#### What to do next

Install a PEM. Go to Installing the Power Entry Modules. 

## Installing and Removing a Fan Module

You can hot swap a 100 mm chassis fan module (UCSX-9508-FAN) without causing an electrical hazard or damage to the system. However, you can only remove one fan module at a time while the system is operating. Removing more than one fan module could cause overheating. 

  * Fan Module Replacement Consideration
  * Installing a Fan Module
  * Removing a Fan Module


### Fan Module Replacement Consideration

While a fan module is absent from the chassis, the pair of compute nodes physically associated with that fan may be throttled to prevent thermal overload. After the fan module is replaced in the chassis, throttling is removed and the associated blades resume normal operation. 

To minimize the impact to system performance, do not remove a fan module until a replacement fan module is available. When replacing a fan module, you must insert a new fan in less than one minute after removing the old fan. Leaving the fan module out of the chassis for longer durations of time will result in power throttling of the associated compute nodes. In extreme cases, the compute nodes might shutdown. 

The following table shows the mapping of fan modules to their associated compute nodes.

Fan Module |  Compute Node Slots  
---|---  
1 |  7, 8  
2 |  5, 6  
3 |  3, 4  
4 |  1, 2  
  
### Installing a Fan Module

#### Procedure

* * *

**Step 1** |  Hold the chassis fan module (UCSX-9508-FAN) with the handle at the bottom and place your other hand underneath the fan module to support it.   
---|---  
**Step 2** |  Align the fan with the fan bay in the rear of the chassis.  Figure 18. Aligning the Fan Module  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309077.jpg)  
**Step 3** |  Slide the fan into the chassis until it is flush with the face of the chassis.  |  **Note** |  Make sure that the latch on the handle is engaged with the chassis.  
---|---  
  
When the fan module is almost completely installed, you might feel some resistance. The resistance is normal, and it occurs when the connector at the rear of the fan contacts the corresponding socket inside the chassis. 

Figure 19. Seating the Fan into the Chassis  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308912.jpg)  
**Step 4** |  Listen for the fan to power up and verify that the LED behavior is as expected. See [LED Locations](m-ucsx-9508-chassis-overview.html#ID499) and [Interpreting LEDs](m-ucsx-9508-chassis-overview.html#ID544).   
  
* * *

### Removing a Fan Module

#### Before you begin

Removing a chassis fan module (UCSX-9508-FAN) can cause throttling of the compute nodes associated with that fan. When replacing a fan, you must insert a new fan in less than one minute after removing the old fan. You will find it helpful to have the replacement fan ready before attempting fan replacement. For more information, see Fan Module Replacement Consideration. 

#### Procedure

* * *

**Step 1** |  Grasp the chassis fan module handle and push down on the release button.  Figure 20. Disengaging the Fan Module  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308912.jpg)  
---|---  
**Step 2** |  Slide the fan module partially out of the chassis and place your hand underneath it to support it.  When the fan disconnects from the midplane, it will power down.   
**Step 3** |  Slide the fan completely out of the chassis, making sure to support its weight with your other hand.  |  **Caution** |  The fan module is relatively heavy! Do not attempt to handle or carry it by only its handle. Instead, make sure support the fan's weight with your other hand.  Figure 21. Removing the Fan Module  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308911.jpg)  
---|---  
  
* * *

#### What to do next

Insert a fan module. Go to Installing a Fan Module. 

## Installing and Removing a Rear Module's Fan

The Cisco UCS X9508 Intelligent Fabric Module (IFM) and X-Fabric Module (XFM) blanks use the same 40 mm fan (UCSX-RSFAN=), which makes the fans interchangeable between these modules and module blanks. In a typical configuration, there are three fans numbered from one to three. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The fans for IFM and XFMs (UCSX-RSFAN=) are different from the 100 mm chassis fan modules (UCSX-9508-FAN=) that provide cooling and ventilation for the entire server chassis. These two types of fans are not interchangeable. 

* * *  
  
---|---  
  
Use the following procedures to replace a fan on a Cisco UCS X9508 module or module blank. 

  * Installing a Fan for a UCS Intelligent Fabric Module (IFM) or X-Fabric Module (XFM) Blank

  * Removing a Fan for a UCS Intelligent Fabric Module (IFM) or X-Fabric Module (XFM) Blank


  * Installing a Fan for a UCS Intelligent Fabric Module (IFM) or X-Fabric Module (XFM) Blank
  * Removing a Fan for a UCS Intelligent Fabric Module (IFM) or X-Fabric Module (XFM) Blank


### Installing a Fan for a UCS Intelligent Fabric Module (IFM) or X-Fabric Module (XFM) Blank 

Use this task to install the fan (UCSX-RSFAN=) for a UCS Intelligent Fabric Module (IFM) or X-Fabric Module (XFM) Blank. 

#### Procedure

* * *

**Step 1** |  Align the fan correctly.

  1. Align the power connector on the replacement fan with power connector on the board.
  2. Align the guides on long fan side walls with the corresponding cutouts on the module. Figure 22. Aligning the Fan  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308954.jpg)

  
---|---  
**Step 2** |  Press down evenly on the fan until it is fully seated. Make sure the fan is level while you're installing it. You will feel the fan click into place when it is correctly seated on the module or module blank.   
  
* * *

### Removing a Fan for a UCS Intelligent Fabric Module (IFM) or X-Fabric Module (XFM) Blank 

Use the following procedure for removing a fan (UCSX-RSFAN=) from a UCS Intelligent Fabric Module (IFM) or X-Fabric Module (XFM) Blank. 

#### Procedure

* * *

**Step 1** |  Grasp the fan by the tabs on each long side wall.   
---|---  
**Step 2** |  Pull the fan straight up. This step disconnects the fan from the power connector and lifts the fan off of the board. Figure 23. Removing the Fan from a UCS X9508 Module or Module Blank  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309543.jpg)  
  
* * *

#### What to do next

Insert a fan module. Go to Installing a Fan for a UCS Intelligent Fabric Module (IFM) or X-Fabric Module (XFM) Blank. 

## Installing and Removing an Intelligent Fabric Module

Intelligent Fabric Modules (IFMs) install in the rear of the chassis. They are always deployed in pairs, and the minimum IFM configuration for each UCS X9508 is two. For more information, see [Intelligent Fabric Modules](m-ucsx-9508-chassis-overview.html#Cisco_Concept.dita_db0ed713-8b40-439d-aa83-c8a1e91020a5). 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

When working with the IFMs, handle them carefully to avoid damage to the modules, connectors, and pins.

* * *  
  
---|---  
  
Use the following procedures to replace an IFM:

  * Installing an Intelligent Fabric Module

  * Removing an Intelligent Fabric Module


  * Installing an Intelligent Fabric Module
  * Removing an Intelligent Fabric Module


### Installing an Intelligent Fabric Module

Intelligent Fabric Modules (IFM) must be deployed in pairs, so there are no IFM module blanks that can be installed. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

When working with the IFMs, handle them carefully to avoid damage to the modules, connectors, and pins! Make sure that the modules are level during insertion and slide them into the chassis slowly. 

* * *  
  
---|---  
  
#### Procedure

* * *

**Step 1** |  If the IFM has a cable management tray, remove it.  See [Removing the Cable Management Tray](m-installation.html#Cisco_Task_in_List_GUI.dita_377c830e-a9c3-4cf8-b274-2a3d166bd736).   
---|---  
**Step 2** |  Swing the ejector handles to the open position.   
**Step 3** |  Placing one hand underneath the IFM, align the module with the empty IFM slot on the rear of the chassis. Figure 24. Aligning the Intelligent Fabric Module  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308915.jpg)  
**Step 4** |  Holding the IFM level, slide it almost all the way into the chassis until you feel some resistance.  This resistance is normal. It occurs when the connectors at the rear of the IFM contact the socket inside the chassis.  |  **Caution** |  Make sure to apply even pressure when sliding the module into the chassis. Do not push down or pull up on the module handles, and do not apply more force to one ejector handle than the other.   
---|---  
**Step 5** |  Grasp each of the ejector handles, and keeping them level, slowly arc them inward toward the chassis. This step seats the IFM connectors into the sockets on the midplane.  |  **Caution** |  Make sure to apply even pressure when closing the module ejector handles! Do not push down or pull up on the module handles, and do not apply more force to one ejector handle than the other.   
---|---  
**Step 6** |  Push the ejector handles until both are parallel with the face of the IFM.  Make sure the ejector latch is fully inserted in the front panel  
**Step 7** |  If the IFM has a cable management tray, attach it.  See [Installing the Cable Management Tray](m-installation.html#Cisco_Task_in_List_GUI.dita_77a99c2e-2c25-4fd0-afa6-596b075668c8).   
  
* * *

### Removing an Intelligent Fabric Module

Intelligent Fabric Modules (IFM) must be deployed in pairs, so when you remove one, you must insert another IFM in its place. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

When working with the IFMs, handle them carefully to avoid damage to the modules, connectors, and pins! Make sure that the modules are level during removal and slide them out of the chassis slowly. 

* * *  
  
---|---  
  
#### Procedure

* * *

**Step 1** |  If the IFM has a cable management tray, remove it. See [Removing the Cable Management Tray](m-installation.html#Cisco_Task_in_List_GUI.dita_377c830e-a9c3-4cf8-b274-2a3d166bd736).   
---|---  
**Step 2** |  Using your fingers, pinch the interior end of both handles to disengage the ejector latch. This step unlocks the module handles so that they can move.  Figure 25. Opening the Module Handles  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308916.jpg)  
**Step 3** |  Keeping the modules handles level, pull them towards you so that they arc away from the chassis.  You might feel some resistance as the IFM disconnects from the socket inside the chassis.   
**Step 4** |  Slide the module about halfway out of the chassis, then place your other hand underneath the IFM to support it. |  **Caution** |  Make sure to apply even pressure when sliding the module out of the chassis. Do not push down or pull up on the module handles, and do not apply more force to one ejector handle than the other.   
---|---  
**Step 5** |  Continue sliding the IFM out of the chassis until it is completely removed.  Figure 26. Removing an Intelligent Fabric Module  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308984.jpg)  
  
* * *

#### What to do next

Insert an IFM. Go to Installing an Intelligent Fabric Module

## Installing and Removing an X-Fabric Module

X-Fabric Modules are required when the UCS X9508 chassis contains one or more pairs of X-Series compute nodes and X-Series PCIe Nodes. For more information, see [X-Fabric Modules](m-ucsx-9508-chassis-overview.html#Cisco_Concept.dita_44aedf58-a967-49a2-ab8d-846770a6b57a). 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Because both XFMs connect to all slots on the front of the server chassis, all pairs of compute nodes and PCIe nodes must be powered off before removing or inserting XFMs. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Although the Cisco UCS X-Fabric Modules can be removed, it is a best practice to leave them installed even during chassis installation. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

To ensure graceful/non-disruptive replacement of X-Fabric Modules, use your Cisco management tool, such as Cisco Intersight, to properly deactivate any profiles before removing the XFMs. 

* * *  
  
---|---  
  
Use the following procedures to install or remove a UCS X9416 or X9516 X-Fabric Module. 

  * Removing an X-Fabric Module

  * Installing an X-Fabric Module


For a UCS X9516 X-Fabric Module, also use the following procedures to install or remove the module's network adapters. 

  * Replacement Guidelines and Considerations for Cisco UCS X9516 X-Fabric Modules

  * Removing a PCIe Card from a UCS X9516 X-Fabric Module PCIe Cage

  * Removing a PCIe Filler Panel from a UCS X9516 X Fabric Module

  * Installing a PCIe Card into a UCS X9516 X-Fabric Module PCIe Cage

  * Installing a PCIe Filler Panel in a UCS X9516 X- Fabric Module


  * Removing an X-Fabric Module
  * Installing an X-Fabric Module
  * Replacement Guidelines and Considerations for Cisco UCS X9516 X-Fabric Modules
  * Removing a PCIe Card from a UCS X9516 X-Fabric Module PCIe Cage
  * Removing a PCIe Filler Panel from a UCS X9516 X Fabric Module
  * Installing a PCIe Card into a UCS X9516 X-Fabric Module PCIe Cage
  * Installing a PCIe Filler Panel in a UCS X9516 X- Fabric Module


### Removing an X-Fabric Module

Use the following procedure to remove a Cisco UCS X-Fabric Module.

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

When working with the XFMs, handle them carefully to avoid damage to the modules, connectors, and pins! Make sure that the modules are level during removal and slide them out of the chassis slowly. 

* * *  
  
---|---  
  
#### Before you begin

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Make sure that all pairs of compute nodes and PCIe nodes are completely powered off before removing an X-Fabric Module (XFM).

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

To ensure graceful/non-disruptive replacement of X-Fabric Modules, use your Cisco management tool, such as Cisco Intersight, to properly deactivate any profiles before removing the XFMs. 

* * *  
  
---|---  
  
#### Procedure

* * *

**Step 1** |  Using your fingers, pinch the interior end of both handles to disengage the ejector latch. This step unlocks the module handles so that they can move.   
---|---  
**Step 2** |  Keeping the modules handles level, pull them towards you so that they arc away from the chassis.  |  **Caution** |  Make sure to apply even pressure when sliding the module out of the chassis. Do not push down or pull up on the module handles, and do not apply more force to one ejector handle than the other.   
---|---  
  
You might feel some resistance as the module disconnects from the socket inside the chassis. 

Figure 27. Opening the Module Ejector Handles  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540772.jpg)  
**Step 3** |  Keeping the module level, slowly slide the module about halfway out of the chassis, then place your other hand underneath the module to support it.   
**Step 4** |  Continue sliding the module out of the chassis until it is completely removed.  Figure 28. Removing an X-Fabric Module  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540774.jpg)  
  
* * *

#### What to do next

Insert an X-Fabric Module. Go to Installing an X-Fabric Module

### Installing an X-Fabric Module

Use the following procedure to install a Cisco UCS X-Fabric Module. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

When working with the XFMs, handle them carefully to avoid damage to the modules, connectors, and pins! Make sure that the modules are level during installation and slide them into of the chassis slowly. 

* * *  
  
---|---  
  
#### Before you begin

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Make sure that all pairs of compute nodes and PCIe nodes are completely powered off before inserting XFMs.

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

After installing X-Fabric Modules, use your Cisco management tool, such as Cisco Intersight, to properly activate any profiles that include the XFMs. 

* * *  
  
---|---  
  
#### Procedure

* * *

**Step 1** |  Swing the ejector handles to the open position.   
---|---  
**Step 2** |  Placing one hand underneath the module, align the module with the empty module slot on the rear of the chassis. Figure 29. Installing an X-Fabric Module  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540773.jpg)  
**Step 3** |  Holding the module level, slowly slide it almost all the way into the chassis until you feel some resistance.  This resistance is normal. It occurs when the connectors at the rear of the module contact the socket inside the chassis.  |  **Caution** |  Make sure to apply even pressure when sliding the module into the chassis. Do not push down or pull up on the module handles, and do not apply more force to one ejector handle than the other.   
---|---  
**Step 4** |  Grasp each of the ejector handles, and keeping them level, arc them inward toward the chassis. This step seats the module connectors into the sockets on the midplane.  |  **Caution** |  Make sure to apply even pressure when closing the module ejector handles! Do not push down or pull up on the module handles, and do not apply more force to one ejector handle than the other.   
---|---  
**Step 5** |  Push the ejector handles until both are parallel with the face of the module.  Make sure the ejector latch is fully inserted in the front panel  
  
* * *

### Replacement Guidelines and Considerations for Cisco UCS X9516 X-Fabric Modules 

When replacing PCIe cages or cards, be aware of the following.

#### PCIe Cage Considerations and Guidelines

  * PCIe cages for the Cisco UCS X9516 X-Fabric Module are interchangeable. You can install either cage in slot 1 or slot 2 of the XFM. 

  * Individual PCIe cages are not field-serviceable. The only supported workflows for removing or installing a PCIe cage is to remove or install the network adapter (such as the ConnectX-7 NIC) or for product recycling. Be careful when handling PCIe cages! Because they are not field-replaceable, the entire XFM must be replaced if a PCIe cage becomes damaged. 

  * PCIe cages have alignment features consisting of guide pins that meet guide holes on each cage and a metal tab on the side of the cage near the front panel (not shown in the following illustration). These alignment features key the cages so that they ensure proper alignment with securing screws and prevent incorrect installation. You will find it helpful to know the locations of these features on the cage and the XFM itself. 

![](/c/dam/en/us/td/i/400001-500000/490001-500000/490001-491000/490996.jpg) **1** |  Guide pin on motherboard and guide hole (PCIe Cage 2).  
---|---  
**2** |  Guide pin on motherboard and guide hole (PCIe Cage 1).  
**3** |  Threaded standoff for thumbscrew (PCIe Cage 1)  
**4** |  Threaded standoff for thumbscrew (PCIe Cage 2)  
  * Both PCIe cages must be installed during normal operation. To ensure proper airflow and to minimize the amount of airborne particulates, do not operate the XFM with an empty PCIe Cage slot. 

  * Take care to keep a PCIe Cage horizontal while removing or installing it. Tipping, twisting, or rotating the cage during removal or installation increases the chance of damaging the cage's PCIe connector (golden fingers) or the XFM motherboard's PCIe socket. 


#### PCIe Card Considerations and Guidelines

  * When handling a PCIe card, always use safe ESD handling practices. 

  * Third-party PCIe cards can be installed in one, or both of the XFM's PCI cages. Although not a requirement, it is a best practice to install a PCIe card in PCIe Cage 1 if only one PCIe card is required for your deployment. 

  * Third-party PCIe cards have typical alignment features consisting of beveled tab that inserts into a slot inside the PCIe cage and a right angle tab on the card's faceplate. The XFM PCIe cage is designed to accept cards with these features. You will find it helpful to familiarize yourself with these PCIe card features and how they mate with the appropriate locations on each PCIe cage. 

  * If your deployment requires only one PCIe card, you must install a PCIe card blank (bracket). To ensure proper airflow and to minimize the amount of airborne particulates, do not operate the XFM with an uncovered PCIe card slot. 

  * Take care to keep a PCIe card horizontal while removing or installing it. Tipping, twisting, or rotating the card during removal or installation increases the chance of damaging the PCIe connector (golden fingers) on the card or the PCIe socket inside the PCIe cage. 

  * The Cisco UCS X9516 X Fabric Module has the following operational temperatures which differ depending on the network adapter installed: 

  * With ConnectX7 1x400G cards installed, the module's maximum supported ambient temperature is 82.4° F (28° C)

  * With ConnectX7 2x200G cards installed, the module's maximum supported ambient temperature is 86° F (30° C)


### Removing a PCIe Card from a UCS X9516 X-Fabric Module PCIe Cage

The UCS X9516 X-Fabric Module offers two PCIe Cages that support PCIe Cards, such as NVIDIA ConnectX-7 NICs. Each PCIe Cage (numbered 1 and 2, as indicated on the faceplate of the XFM) contains up to one network adapter. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

As part of this procedure, you will remove the PCIe cage from the XFM. Individual PCIe cages are not field-replaceable, so handle them carefully, especially when removing or installing them. If the cage or its connectors are damaged, you must RMA the entire XFM. 

* * *  
  
---|---  
  
Use this task to remove a PCIe card from the UCS X9516 XFM.

#### Before you begin

Before attempting this task, gather a #2 Phillips screwdriver. 

You will find it helpful to read Replacement Guidelines and Considerations for Cisco UCS X9516 X-Fabric Modules before attempting this task. 

#### Procedure

* * *

**Step 1** |  If you have not already removed the XFM from the chassis, do so now.  See Removing an X-Fabric Module.   
---|---  
**Step 2** |  If you have not already removed the X-Fabric Module's top cover, do so now. 

  1. Press and hold the release button down. 
  2. While holding the release button down, slide the top cover toward the rear of the module.  This step frees the catch pins on the top cover from the retaining grooves on the top of the XFM's side walls. 
  3. Lift the top cover up to remove it from the XFM. 

  
**Step 3** |  Loosen the screws.

  1. Using the #2 Phillips screwdriver, loosen two thumbscrews on the XFM faceplate.  ![](/c/dam/en/us/td/i/400001-500000/490001-500000/490001-491000/490997.jpg)
  2. Using the screwdriver, loosen the thumbscrews on the PCIe cage.  ![](/c/dam/en/us/td/i/400001-500000/490001-500000/490001-491000/490998.jpg)

  
**Step 4** |  Grasping both the front and rear edges of the PCIe cage, keep the PCIe cage level while lifting it off of the XFM.  |  **Caution** |  **_Do not tip, twist, or rotate the PCIe cage while removing it!_** Failure to keep the PCIe cage while removing it can cause damage to the connector.   
---|---  
![](/c/dam/en/us/td/i/400001-500000/490001-500000/490001-491000/490999.jpg)  
**Step 5** |  Place the PCIe Cage on an ESD-safe surface while you work on it.  
**Step 6** |  Open the PCIe Cage.

  1. Using the screwdriver, loosen the captive screw.
  2. Swing the PCIe Cage door open.  ![](/c/dam/en/us/td/i/400001-500000/490001-500000/491001-492000/491003.jpg)

  
**Step 7** |  Grasp the front and rear edges of the PCIe card, and holding it level, pull it straight out of the PCIe cage.  |  **Caution** |  **_Do not tip, twist, or rotate the PCIe card while removing it!_** Failure to keep the PCIe card level while removing it can cause damage to the card's connector or cage's socket.   
---|---  
  
![](/c/dam/en/us/td/i/400001-500000/490001-500000/491001-492000/491004.jpg)  
  
* * *

#### What to do next

Insert a NIC card and reinstall the PCIe cage onto the UCS X9516 X-Fabric Module. 

See Installing a PCIe Card into a UCS X9516 X-Fabric Module PCIe Cage. 

### Removing a PCIe Filler Panel from a UCS X9516 X Fabric Module

Use this procedure to remove a filler blank from the PCIe card slot, when needed.

#### Before you begin

Before attempting this task, gather a #2 Phillips screwdriver. 

You will find it helpful to read Replacement Guidelines and Considerations for Cisco UCS X9516 X-Fabric Modules before attempting this task. 

#### Procedure

* * *

**Step 1** |  If you have not already removed the XFM from the chassis, do so now.  See Removing an X-Fabric Module.   
---|---  
**Step 2** |  If you have not already removed the X-Fabric Module's top cover, do so now. 

  1. Press and hold the release button down. 
  2. While holding the release button down, slide the top cover toward the rear of the module.  This step frees the catch pins on the top cover from the retaining grooves on the top of the XFM's side walls. 
  3. Lift the top cover up to remove it from the XFM. 

  
**Step 3** |  Loosen the screws.

  1. Using the #2 Phillips screwdriver, loosen two thumbscrews on the XFM faceplate.  ![](/c/dam/en/us/td/i/400001-500000/490001-500000/493001-494000/493121.jpg)
  2. Using the screwdriver, loosen the thumbscrews on the PCIe cages.  ![](/c/dam/en/us/td/i/400001-500000/490001-500000/493001-494000/493122.jpg)

  
**Step 4** |  Grasping both the front and rear edges of the PCIe cage, keep the PCIe cage level while lifting it off of the XFM.  |  **Caution** |  **_Do not tip, twist, or rotate the PCIe cage while removing it!_** Failure to keep the PCIe cage while removing it can cause damage to the connector.   
---|---  
![](/c/dam/en/us/td/i/400001-500000/490001-500000/493001-494000/493123.jpg)  
**Step 5** |  Place the PCIe Cage on an ESD-safe surface while you work on it.  
**Step 6** |  Open the PCIe cage.

  1. Using the screwdriver, loosen the captive screw.
  2. Swing the PCIe Cage door open. 

  
**Step 7** |  Grasp the front edge of the filler panel, and holding it level, pull it straight out of the PCIe cage.  ![](/c/dam/en/us/td/i/400001-500000/490001-500000/493001-494000/493120.jpg)  
  
* * *

### Installing a PCIe Card into a UCS X9516 X-Fabric Module PCIe Cage

Use the following task to install a PCIe cage onto a Cisco UCS X9516 X-Fabric Module. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

As part of this procedure, you will install the PCIe cage onto the XFM. Be careful when doing so. PCIe cages are not field-replaceable. If the PCIe cage or connectors are damaged, you must RMA the entire XFM. 

* * *  
  
---|---  
  
#### Before you begin

Before attempting this procedure, gather a #2 Phillips torque driver. 

You will find it helpful to read Replacement Guidelines and Considerations for Cisco UCS X9516 X-Fabric Modules before attempting this task. 

#### Procedure

* * *

**Step 1** |  Orient the PCIe card so that the connector and the PCIe socket inside the PCIe cage are in plane with each other.   
---|---  
**Step 2** |  Holding the PCIe card level, slide it into the PCIe cage making sure that the beveled tag inserts into the slot inside the cage.  ![](/c/dam/en/us/td/i/400001-500000/490001-500000/491001-492000/491005.jpg)  
**Step 3** |  Press firmly to fully seat the card's connector into the PCIe socket inside the PCIe cage.   
**Step 4** |  Swing the PCIe cage door closed, making sure that the door closes completely and sits flush against the cage.  ![](/c/dam/en/us/td/i/400001-500000/490001-500000/491001-492000/491006.jpg)  
**Step 5** |  Using the screwdriver, tighten the captive screw to secure the door to the PCIe cage. |  **Caution** |  Do not overtighten the thumbscrews! Make sure to tighten them to finger-tight only or you risk stripping them.  
---|---  
  
![](/c/dam/en/us/td/i/400001-500000/490001-500000/491001-492000/491007.jpg)  
  
**Step 6** |  Attach the PCIe Cage to the XFM. 

  1. Locate the guide pins, threaded standoff for the thumbscrews, and the PCIe socket on the XFM. 
  2. Holding the PCIe Cage level, lower it onto the XFM so that the PCIe connector on the cage seats into the socket on the XFM.  |  **Caution** |  **_Do not tip, twist, or rotate the PCIe cage while installing it!_** Failure to keep the PCIe cage while removing it can cause damage to the PCIe connector.   
---|---  
  
![](/c/dam/en/us/td/i/400001-500000/490001-500000/490001-491000/491000.jpg)


  
**Step 7** |  Using the screwdriver, tighten the thumbscrews on the XFM. ![](/c/dam/en/us/td/i/400001-500000/490001-500000/491001-492000/491001.jpg)  
**Step 8** |  Using the screwdriver, tighten the thumbscrews on the XFM's faceplate. ![](/c/dam/en/us/td/i/400001-500000/490001-500000/491001-492000/491002.jpg)  
**Step 9** |  Attach the top cover of the X Fabric Module. 

  1. Lay the top cover on the XFM.
  2. Slide it forward, making sure that the pins on the underside of the top cover meet the grooves on the top of the XFM's sidewalls. 
  3. Making sure that the leading edge of the top cover slides under the front of the XFM, seat the top cover until it clicks into place. 

  
**Step 10** |  Insert the XFM into the chassis.  See Installing an X-Fabric Module.   
  
* * *

### Installing a PCIe Filler Panel in a UCS X9516 X- Fabric Module

Use this task to install a filler panel in the PCIe card slot, when needed. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Do not operate the system without a filler panel or PCIe card installed. 

* * *  
  
---|---  
  
#### Before you begin

Before attempting this procedure, gather a #2 Phillips screwdriver. 

You will find it helpful to read Replacement Guidelines and Considerations for Cisco UCS X9516 X-Fabric Modules before attempting this task. 

#### Procedure

* * *

**Step 1** |  If you have not already loosened the screw and opened the PCIe cage door, do so now.   
---|---  
**Step 2** |  Orient the filler panel so that the tabbed end of the filler panel lines up with the slot inside the PCIe cage.   
**Step 3** |  Holding the filler panel level, slide it into the PCIe cage making sure that the beveled tab inserts into the slot inside the cage.  ![](/c/dam/en/us/td/i/400001-500000/490001-500000/493001-494000/493119.jpg)  
**Step 4** |  Swing the PCIe cage door closed, making sure that the door closes completely and sits flush against the cage.  
**Step 5** |  Using the screwdriver, tighten the captive screw to secure the door to the PCIe cage. |  **Caution** |  Do not overtighten the thumbscrews! Make sure to tighten them to finger-tight only or you risk stripping them.  
---|---  
**Step 6** |  Attach the PCIe Cage to the XFM. 

  1. Locate the guide pins, threaded standoff for the thumbscrews, and the PCIe socket on the XFM (1). 
  2. Holding the PCIe Cage level, lower it onto the XFM so that the PCIe connector on the cage seats into the socket on the XFM (2).  |  **Caution** |  **_Do not tip, twist, or rotate the PCIe cage while installing it!_** Failure to keep the PCIe cage while removing it can cause damage to the PCIe connector.   
---|---  
  
![](/c/dam/en/us/td/i/400001-500000/490001-500000/493001-494000/493124.jpg)


  
**Step 7** |  Using the screwdriver, tighten the thumbscrews on the XFM. ![](/c/dam/en/us/td/i/400001-500000/490001-500000/493001-494000/493122.jpg)  
**Step 8** |  Using the screwdriver, tighten the thumbscrews on the XFM's faceplate. ![](/c/dam/en/us/td/i/400001-500000/490001-500000/493001-494000/493121.jpg)  
**Step 9** |  Attach the top cover of the X Fabric Module. 

  1. Lay the top cover on the XFM.
  2. Slide it forward, making sure that the pins on the underside of the top cover meet the grooves on the top of the XFM's sidewalls. 
  3. Making sure that the leading edge of the top cover slides under the front of the XFM, seat the top cover until it clicks into place. 

  
  
* * *

## Installing and Removing the UCS X-Fabric Module Blank

The UCS X-Fabric Module Blank (UCSX-9508-RBLK) is a filler module for the expansion slots on the bottom of the chassis rear. For more information, see [Cisco UCS X-Fabric Module Blanks](m-ucsx-9508-chassis-overview.html#Cisco_Concept.dita_0691f606-292d-47a3-a279-288591a892a9). 

Use the following procedures to replace the UCSX-9508-RBLK. 

  * Installing a UCS X-Fabric Module Blank

  * Removing a UCS X-Fabric Module Blank


  * Installing a UCS X-Fabric Module Blank
  * Removing a UCS X-Fabric Module Blank


### Installing a UCS X-Fabric Module Blank

Use this procedure to install an UCS X-Fabric Module Blank in the bottom two slots in the chassis rear. These module blanks must be deployed in pairs and must be installed. You cannot operate the server chassis with empty IOM bays. 

#### Procedure

* * *

**Step 1** |  Placing one hand underneath the blank, align it with the empty slot at the bottom of the rear of the chassis.  
---|---  
**Step 2** |  Holding the blank level, slowly slide it all the way into the chassis until the blank stops.  |  **Caution** |  Make sure to apply even pressure when sliding the module into the chassis. Do not push down or pull up on the module handles, and do not apply more force to one ejector handle than the other.   
---|---  
**Step 3** |  Grasp each of the module handles, and keeping them level, arc them inward toward the chassis. This step seats the blank connectors into the sockets on the midplane.  |  **Caution** |  Make sure to apply even pressure when closing the module ejector handles! Do not push down or pull up on the module handles, and do not apply more force to one ejector handle than the other.   
---|---  
**Step 4** |  Push the module handles until both are parallel with the face of the blank.  The fan modules on the blank will power up when the module is completely seated.   
  
* * *

### Removing a UCS X-Fabric Module Blank

Use this task to remove a UCS X-Fabric Module Blank (UCSX-9508-BLK). 

#### Procedure

* * *

**Step 1** |  Using your fingers, pinch the interior end of both handles to disengage the retention clip. This step unlocks the module handles so that they can move.   
---|---  
**Step 2** |  Keeping the modules handles level, pull them towards you so that they arc away from the chassis.  |  **Caution** |  Make sure to apply even pressure when sliding the blank out of the chassis. Do not push down or pull up on the module handles, and do not apply more force to one ejector handle than the other.   
---|---  
**Step 3** |  Slowly slide the blank about halfway out of the chassis, then place your other hand underneath the blank to support it.  
**Step 4** |  Continue sliding the blank out of the chassis until it is completely removed.   
**Step 5** |  Reinsert a UCS X-Fabric Module blank (UCSX-9508-RBLK).  
  
* * *

#### What to do next

Installing a UCS X-Fabric Module Blank

## Recycling Printed Circuit Boards

The Cisco UCS X9508 and some of its modules have printed circuit boards (PCBs) that must be disposed of in compliance with your appropriate recycling and e-waste regulations, including, but not limited to Commission Regulation (EU) 2019/424. 

The following procedures are not standard field-service options. They should be used only by certified or approved recyclers.

  * Recycling the UCS 9108 25G IFM PCBs

  * Recycling the UCS 9108 100G IFM PCBs

  * Recycling the Chassis PCB Assembly (PCBA)


  * Recycling the Chassis PCB Assembly (PCBA)
  * Recycling the UCS 9108 25G IFM PCBs
  * Recycling the UCS 9108 100G IFM PCBs
  * Recycling a UCS X9416 X-Fabric Module PCB
  * Recycling a UCS X9516 X-Fabric Module PCB
  * Recycling X-Fabric Module Blank PCBs


### Recycling the Chassis PCB Assembly (PCBA)

Each Cisco UCS X9508 chassis has a PCBA (motherboard) that is connected to the chassis midplane sheet metal. You must disconnect the PCBA from the chassis sheet metal to recycle the PCBA. Each PCBA is attached to the midplane sheet metal by 19 M4 screws. You will need to disassemble and remove additional parts to gain access to the PCBA. 

You will need to recycle the PCBA for each UCS X9508 chassis.

Use the following procedure to recycle the Cisco UCS X9508 motherboard.

#### Before you begin

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

**For Recyclers Only!** This procedure is not a standard field-service option. This procedure is for recyclers who will be reclaiming the electronics and sheet metal for proper disposal to comply with local eco design and e-waste regulations. 

* * *  
  
---|---  
  
To remove the chassis printed circuit board assembly (PCBA), the following requirements must be met:

  * The chassis must be disconnected from facility power.

  * The chassis must have all compute nodes and IFMs removed. If they are not removed, remove them now. Go to:

  * Removing a Compute Node

  * Removing an Intelligent Fabric Module

  * The chassis must be removed from the equipment rack.


You will find it helpful to gather a T10, T15, and T20 screwdriver before beginning this procedure.

#### Procedure

* * *

**Step 1** |  At the rear of the chassis, remove the fan modules.  See Removing a Fan Module.   
---|---  
**Step 2** |  On the left side of the chassis, use a T10 screwdriver to remove 14 M4 screws.  Figure 30. Cisco UCS X9508 Chassis, Left Side  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309213.jpg)  
**Step 3** |  On the right side of the chassis, use a T10 screwdriver to remove 14 M4 screws plus the two captive M3 screws for the PEMs.  Figure 31. Cisco UCS X9508 Chassis, Right Side  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309214.jpg)  
**Step 4** |  On the top of the chassis, use a T10 screwdriver to remove the eight M4 screws.  Figure 32. Cisco UCS X9508 Chassis, Top  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309216.jpg)  
**Step 5** |  Remove the PEMs.

  1. On the interior of the chassis, use the T10 screwdriver to remove the two M3 captive screws for the PEMs, which are indicated by the ground symbol (![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309215.jpg)). 
  2. When the screws are removed, grasp each PEM and remove it from the chassis. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309217.jpg)

  
**Step 6** |  Disconnect the rear bracket assembly:

  1. Grasp the two cables and unplug them. 
  2. Using a T20 screwdriver, remove the four M4 screws. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309218.jpg)

  
**Step 7** |  Grasp the rear bracket assembly and disconnect it from the rest of the chassis.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309219.jpg)  
**Step 8** |  With the rear bracket assembly removed, disconnect the PCB: 

  1. Grasp the cable and unplug it.
  2. Using the T15 screwdriver, remove the 19 M4 screws, and remove the PCB from the chassis midplane sheet metal.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309220.jpg)

  
**Step 9** |  Recycle the sheet metal and motherboard in compliance with your local recycling and e-waste regulations.   
  
* * *

### Recycling the UCS 9108 25G IFM PCBs

Each Cisco UCS Intelligent Fabric Module (IFM) has a printed circuit board (PCB) that is connected to the IFM's sheet metal tray. You must: 

  * Disassemble and remove additional parts to gain access to the PCB. 

  * Disconnect the PCB from the sheet metal to recycle the PCB. 

  * Recycle each IFM in the Cisco UCS X9508 chassis.


Use the following procedure to recycle the UCS IFMs.

#### Before you begin

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

**For Recyclers Only!** This procedure is not a standard field-service option. This procedure is for recyclers who will be reclaiming the electronics and sheet metal for proper disposal to comply with local eco design and e-waste regulations. 

* * *  
  
---|---  
  
You will find it helpful to gather the following tools before beginning this procedure:

  * Screwdrivers: One each of T8 and T10 screwdriver, and #1 Phillips.

  * Nut drivers: One 8mm hexagonal.


#### Procedure

* * *

**Step 1** |  Remove the following components by hand: 

  1. Grasp each fan module cable and remove it. 
  2. Grasp each fan module and remove it. 
  3. Grasp the M.2 storage module and remove it.
  4. Grasp the light pipe and remove it.

![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309257.jpg)  
---|---  
**Step 2** |  Remove the stiffener bracket.

  1. Using a T10 screwdriver, remove the M3 screws.
  2. Grasp the bracket and remove it.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309258.jpg)

  
**Step 3** |  Remove the horizontal rear bracket.

  1. Using a T8 screwdriver, remove the M3 screws on the exterior of the IFM.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309259.jpg)
  2. Using a T10 screwdriver, remove the M3 screws on the interior of the IFM. 
  3. Grasp the bracket and remove it.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309260.jpg)

  
**Step 4** |  Disconnect additional components and fasteners.

  1. Using a T8 screwdriver, remove the M3 screw on the IFM faceplate.
  2. Grasp the plastic HDMI plug and remove it. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309261.jpg)
  3. Using an 8mm hexagonal nut driver, remove the standoffs.
  4. Using a T10 screwdriver, remove the M3 screws. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309262.jpg) |  Red circles (![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309210.jpg) )  |  M3 hexagonal standoffs, 4  
---|---  
Blue circles (![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309209.jpg) )  |  M3 screws, 6  
  5. Grasp the PCBA and disconnect it from the sheet metal. 


  
**Step 5** |  Disconnect the remaining components from the PCBA.

  1. Using the T10 screwdriver, remove the M3 screws for the top heatsink.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309263.jpg)
  2. Turn the PCBA over so that the bottom is facing up.
  3. Using the #1 Phillips screwdriver and remove the M2 screws. 
  4. Using a pliers, release the four heatsink pushpins.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309264.jpg) |  Red circles (![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309210.jpg) )  |  M2 screws for plastic bracket, 4  
---|---  
Blue circles (![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309209.jpg) )  |  Heatsink pushpins, 4  
  5. Turn the PCBA over again so that the top is facing up. 

  6. Grasp the plastic bracket for the M.2 module and remove it.

  7. If the top heat sink is still attached, grasp and remove it. 

  8. Grasp the three fan baffles and remove them.

  9. Grasp the center heatsink and remove it.

![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309265.jpg)


  
**Step 6** |  Recycle the sheet metal and motherboard in compliance with your local recycling and e-waste regulations.   
  
* * *

#### What to do next

To remove the chassis motherboard, go to Recycling the Chassis PCB Assembly (PCBA). 

### Recycling the UCS 9108 100G IFM PCBs

Each Cisco UCS Intelligent Fabric Module (IFM) has a printed circuit board (PCB) that is connected to the IFM's sheet metal tray. You must: 

  * Disassemble and remove additional parts to gain access to the PCB. 

  * Disconnect the PCB from the sheet metal to recycle the PCB. 

  * Recycle each IFM in the Cisco UCS X9508 chassis.


Use the following procedure to recycle the UCS IFMs.

#### Before you begin

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

**For Recyclers Only!** This procedure is not a standard field-service option. This procedure is for recyclers who will be reclaiming the electronics and sheet metal for proper disposal to comply with local eco design and e-waste regulations. 

* * *  
  
---|---  
  
You will find it helpful to gather the following tools before beginning this procedure:

  * Screwdrivers: One each of T8 and T10 screwdriver, and #1 Phillips.

  * Nut drivers: One 8mm hexagonal.


#### Procedure

* * *

**Step 1** |  Remove the following components by hand: 

  1. Grasp each fan module cable and remove it. 
  2. Grasp each fan module and remove it. 
  3. Grasp the M.2 storage module and remove it.
  4. Grasp the light pipe and remove it.

![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540710.jpg)  
---|---  
**Step 2** |  Remove the stiffener bracket.

  1. Using a T10 screwdriver, remove the M3 screws.
  2. Grasp the bracket and remove it.  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540711.jpg)

  
**Step 3** |  Remove the horizontal rear bracket.

  1. Using a T8 screwdriver, remove the M3 screws on the exterior of the IFM.  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540712.jpg)
  2. Using a T10 screwdriver, remove the M3 screws on the interior of the IFM. 
  3. Grasp the bracket and remove it.  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540713.jpg)

  
**Step 4** |  Disconnect additional components and fasteners.

  1. Using a T8 screwdriver, remove the M3 screw on the IFM faceplate.
  2. Grasp the plastic HDMI plug and remove it. ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540714.jpg)
  3. Using an 8mm hexagonal nut driver, remove the standoffs.
  4. Using a T10 screwdriver, remove the M3 screws. ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540715.jpg) |  Red circles (![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309210.jpg) )  |  M3 hexagonal standoffs, 4  
---|---  
Blue circles (![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309209.jpg) )  |  M3 screws, 6  
  5. Grasp the PCBA and disconnect it from the sheet metal. 


  
**Step 5** |  Disconnect the remaining components from the PCBA.

  1. Using the T10 screwdriver, remove the M3 screws for the top heatsink.  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540716.jpg)
  2. Turn the PCBA over so that the bottom is facing up.
  3. Using the #1 Phillips screwdriver and remove the M2 screws. 
  4. Using a pliers, release the four heatsink pushpins.  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540717.jpg) |  Red circles (![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309210.jpg) )  |  M2 screws for plastic bracket, 4  
---|---  
Blue circles (![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309209.jpg) )  |  Heatsink pushpins, 4  
  5. Turn the PCBA over again so that the top is facing up. 

  6. Grasp the plastic bracket for the M.2 module and remove it.

  7. If the top heat sink is still attached, grasp and remove it. 

  8. Grasp the three fan baffles and remove them.

  9. Grasp the center heatsink and remove it.

![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540718.jpg)

  
**Step 6** |  Recycle the sheet metal and motherboard in compliance with your local recycling and e-waste regulations.   
  
* * *

#### What to do next

To remove the chassis motherboard, go to Recycling the Chassis PCB Assembly (PCBA). 

### Recycling a UCS X9416 X-Fabric Module PCB

Each UCS X9416 Fabric Module has a printed circuit board (PCB) that is connected to module's sheet metal tray. To recycle each module's PCB, you must: 

  * Disassemble and remove additional parts to gain access to the PCB. 

  * Disconnect the PCB from the sheet metal to recycle the PCB. 

  * Recycle each module in the Cisco UCS X9508 chassis.


Use the following task to recycle the X9416 fabric modules.

#### Before you begin

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

**For Recyclers Only!** This procedure is not a standard field-service option. This procedure is for recyclers who will be reclaiming the electronics and sheet metal for proper disposal to comply with local eco design and e-waste regulations. 

* * *  
  
---|---  
  
You will find it helpful to gather the following tools before attempting this procedure:

  * Screwdrivers: One each of T8 and T10 screwdriver 

  * Nut drivers: One 8mm hexagonal head nut driver. 


#### Procedure

* * *

**Step 1** |  Remove the following components by hand: 

  1. Grasp each fan cable and remove it. 
  2. Grasp each fan module and remove it.  For information, see Removing a Fan for a UCS Intelligent Fabric Module (IFM) or X-Fabric Module (XFM) Blank. 
  3. Grasp the light pipe and remove it. ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540806.jpg)

  
---|---  
**Step 2** |  Remove the rear fan bracket.

  1. Using a T10 screwdriver, remove the M3 screws.
  2. Grasp the bracket and remove it.  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540807.jpg)

  
**Step 3** |  Remove the rear back-panel connector bracket.

  1. Using a T8 screwdriver, remove the M3 screws (two per side) on the exterior of the module. ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540745.jpg)![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540746.jpg)
  2. Using a T10 screwdriver, remove the M3 screws on the interior of the module.
  3. Grasp the bracket and remove it.  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540808.jpg)

  
**Step 4** |  Remove additional components and fasteners. 

  1. Using an 8mm hexagonal nut driver, remove the standoffs.
  2. Using a T10 screwdriver, remove the M3 screws. ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540744.jpg) |  Red circles (![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309210.jpg) )  |  M3 hexagonal standoffs, 4  
---|---  
Blue circles (![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309209.jpg) )  |  M3 screws, 4  
  3. Grasp the PCBA and disconnect it from the sheet metal.


  
**Step 5** |  Disconnect the PCB from the sheetmetal. ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540747.jpg)  
**Step 6** |  Recycle the sheet metal and motherboard in compliance with your local recycling and e-waste regulations.   
  
* * *

#### What to do next

Choose the appropriate option:

  * To recycle an X-Fabric Module Blank motherboard, go to: Recycling X-Fabric Module Blank PCBs. 

  * To recycle a 100G UCS Intelligent Fabric Module motherboard, go to: Recycling the UCS 9108 100G IFM PCBs. 

  * To recycle a 25G UCS Intelligent Fabric Module motherboard, go to: Recycling the UCS 9108 25G IFM PCBs. 

  * To recycle the chassis motherboard, go to Recycling the Chassis PCB Assembly (PCBA). 


### Recycling a UCS X9516 X-Fabric Module PCB

Each Cisco UCS X9516 X-Fabric Module has a printed circuit board (PCB) that is connected to the module's sheet metal tray. You must: 

  * Disassemble and remove additional parts to gain access to the PCB. 

  * Disconnect the PCB from the sheet metal to recycle the PCB. 

  * Recycle each module in the Cisco UCS X9508 chassis.


Use the following procedure to recycle the UCS X9516 module.

#### Before you begin

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

**For Recyclers Only!** This procedure is not a standard field-service option. This procedure is for recyclers who will be reclaiming the electronics and sheet metal for proper disposal to comply with local eco design and e-waste regulations. 

* * *  
  
---|---  
  
You will find it helpful to gather the following tools before beginning this procedure:

  * Screwdrivers: One each of T8 and T10 screwdriver, and #1 Phillips.

  * Nut drivers: One 8mm hexagonal.


#### Procedure

* * *

**Step 1** |  Remove the fans: 

  1. Grasp each fan module cable and disconnect it from the motherboard connector. 
  2. Grasp each fan module and remove it by pinching the release tabs and lifting each fan off of the module. ![](/c/dam/en/us/td/i/500001-600000/520001-530000/526001-527000/526605.jpg)

  
---|---  
**Step 2** |  Using a #2 Phillips screwdriver, loosen the captive screws for each cage, then lift each cage up to detach it from the PCB.  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525957.jpg)  
**Step 3** |  Grasp each PCIe cage air baffle and lift it up to disconnect it from the module.  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525958.jpg)  
**Step 4** |  Remove the stiffener bracket.

  1. Using a T10 screwdriver, remove the M3 screws.
  2. Grasp the bracket and remove it.  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525959.jpg)

  
**Step 5** |  Remove the horizontal rear bracket.

  1. Using a T8 screwdriver, remove the M3 screws on the exterior of the module  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525963.jpg)
  2. Using a T10 screwdriver, remove the M3 screws on the rear bracket (1), the guide pins for the PCIe cages (2), and the air baffle screw at the front of the module (3). 
  3. Grasp the rear bracket and remove it.  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525960.jpg) |  **1** |  Rear bracket screws  
---|---  
**2** |  Securing screws, one for each PCIe cage guide-pin.  
**3** |  Front air baffle screw  

  
**Step 6** |  Disconnect additional components and fasteners.

  1. Using a T8 screwdriver, remove the M3 screw on the IFM faceplate.
  2. Grasp the plastic HDMI plug and remove it. ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525964.jpg)
  3. Using an 8mm hexagonal nut driver, remove the four M3 hexagonal standoffs (1).
  4. Using a T10 screwdriver, remove the six M3 screws (1). ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525965.jpg)
  5. Grasp the PCBA and disconnect it from the sheet metal. 

  
**Step 7** |  Disconnect the remaining components from the PCBA.

  1. Using the T10 screwdriver, remove the M3 screws for the small heatsink.  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525966.jpg)
  2. Turn the PCBA over so that the bottom is facing up.
  3. Using a pliers, release the eight heatsink pushpins.  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525967.jpg)
  4. Turn the PCBA over again so that the top is facing up. 
  5. Grasp all three heatsinks and remove them from the module's PCB. ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525968.jpg)

  
**Step 8** |  Disconnect the PCIe cage's PCB from the cage.

  1. Using a #2 Phillips screwdriver, loosen the captive thumbscrew on the PCIe cage (1).
  2. Open the cage door and remove the card (2). 
  3. Using a #2 Phillips screwdriver, remove the three M3 screws that secure the card PCB to the cage (3). 
  4. Disconnect the PCB from the sheetmetal PCIe cage (4). ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525969.jpg)

  
**Step 9** |  Recycle the sheet metal and motherboard in compliance with your local recycling and e-waste regulations.   
  
* * *

#### What to do next

To remove the chassis motherboard, go to Recycling the Chassis PCB Assembly (PCBA). 

### Recycling X-Fabric Module Blank PCBs

Each UCS X-Fabric Module Blank (module blank) has a printed circuit board (PCB) that is connected to module blank's sheet metal tray. To recycle each module blank's PCB, you must: 

  * Disassemble and remove additional parts to gain access to the PCB. 

  * Disconnect the PCB from the sheet metal to recycle the PCB. 

  * Recycle each module blank in the Cisco UCS X9508 chassis.


Use the following task to recycle the module blank.

#### Before you begin

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

**For Recyclers Only!** This procedure is not a standard field-service option. This procedure is for recyclers who will be reclaiming the electronics and sheet metal for proper disposal to comply with local eco design and e-waste regulations. 

* * *  
  
---|---  
  
You will find it helpful to gather a T10 screwdriver before attempting this procedure:

#### Procedure

* * *

**Step 1** |  Remove the following components by hand: 

  1. Grasp each fan cable and remove it. 
  2. Grasp each fan module and remove it.  For information, see Removing a Fan for a UCS Intelligent Fabric Module (IFM) or X-Fabric Module (XFM) Blank. 
  3. Grasp the light pipe and remove it. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309254.jpg)

  
---|---  
**Step 2** |  Grasp the fan module support bracket and remove it.   
**Step 3** |  Remove the vertical rear bracket.

  1. Using a T10 screwdriver, remove the M3 screws.
  2. Grasp the bracket and remove it.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309255.jpg)

  
**Step 4** |  Remove additional components and fasteners. 

  1. Using a T10 screwdriver, remove the M3 screws. ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540750.jpg)
  2. Grasp the PCB and disconnect it from the sheet metal. ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540747.jpg)

  
**Step 5** |  Recycle the sheet metal and motherboard in compliance with your local recycling and e-waste regulations.   
  
* * *

#### What to do next

Choose the appropriate option:

  * To recycle an X-Fabric Module motherboard, go to: Recycling a UCS X9416 X-Fabric Module PCB. 

  * To recycle a 100G UCS Intelligent Fabric Module motherboard, go to: Recycling the UCS 9108 100G IFM PCBs. 

  * To recycle a 25G UCS Intelligent Fabric Module motherboard, go to: Recycling the UCS 9108 25G IFM PCBs. 

  * To recycle the chassis motherboard, go to Recycling the Chassis PCB Assembly (PCBA). 


---

## Page 6: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x9508/install/b-ucs-x9508-install/m-technical-specs.html

# Technical Specifications

This appendix lists the technical specifications for the Cisco UCS X9508 server chassis.

## KVM Cable

The KVM cable (UCSX-C-DEBUGCBL) provides a connection into a Cisco UCS compute node, providing a DB-9 serial connector, a DB-15 connector, and a USB ports for a keyboard and mouse. With this cable you can create a direct connection to the operating system and the BIOS running on a compute node. 

Figure 1. KVM Cable for Compute Nodes    
![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309412.jpg)  
**1** |  Oculink Connector to compute node |  **2** |  DB-9 serial connector to host Console port  
---|---|---|---  
**3** |  USB connector to connect to single USB 3.0 port (keyboard or mouse) |  **4** |  DB-15 connector to connect to a host VGA monitor   
  
## Chassis Specifications

Figure 2. Chassis Dimensions 

![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309536.jpg)

1 |  Chassis Width: 17.5 in (444.5 mm)  
---|---  
2 |  Total Chassis Length, plus protrusions: 35.8 in (909.32 mm)  
3 |  Chassis Length measured from front rack rail: 33.05 in (839.47 mm)   
4 |  Chassis Length, front face to rear face: 34.8 in (884 mm)  
5 |  Chassis Front Clearance: 1.77 in (44.96 mm) Cable management trays, if used, add 4.5 in (114.3 mm) of length to the chassis.   
6 |  Chassis Height: 12.05 in (306.07 mm)  
Table 1. Chassis Capacities and Metrics Description  |  Specification   
---|---  
Node slots  |  8   
IFM slots  |  2   
XFM slots |  2  
Fan module bays  |  4  
Power supply bays  |  6   
PSU Power  |  2800 W  
Maximum Output |  9554 British Thermal Units (BTUs) per hour  
Table 2. Weight of the Chassis Components Description  |  Specification   
---|---  
Empty chassis  |  92 lbs (41.73 kg)   
IFM  |  8.4 lbs (3.81 kg)   
IFM Filler Panel |  5.8 lbs (2.63 kg)  
Fan module  |  3.4 lbs (1.54 kg)   
PSU  |  4 lbs (1.81 kg)  
Compute Node  |  14.9 to 25 lbs (6.76 to 11.34 kg) depending on hardware options.   
PCIe Node |  12.84 to 17.9 lbs (5.83 kg to 8.12 kg) depending on the quantity and types of GPUs installed.  
Fully Populated UCS X9508 Chassis  |  Approximately 400 lbs (181.43 kg) depending on models and options selected   
1 The system weight listed here is an estimate for a fully configured system and will vary depending on the devices installed. 

## Environmental Specifications

Table 3. Environmental Specifications for the Chassis Description |  Specification  
---|---  
Temperature, operating within altitude: 0 to 10,000 feet (0 to 3,000 meters) |  50 to 95°F (10 to 35°C) (As altitude increases, maximum temperature decreases by 1°C per 300m.) For general information, see the [Cisco Unified Computing System Site Planning Guide: Data Center Power and Cooling](https://www.cisco.com/c/en/us/solutions/collateral/data-center-virtualization/unified-computing/white_paper_c11-680202.pdf).   
Temperature, non-operating within altitude: 0 to 40,000 feet (0 to 12,000 meters) |  –40 to 149°F (–40 to 65°C)  
Humidity (RH), noncondensing |  Operating: 10-90%, 28°C max. wet bulb Nonoperating: 5-93%, 38°C max wet bulb  
Altitude |  Operating – 0 to 10000 feet (0 to 3000 meters) Above 10,000 feet, maximum temperature decreases by 1°C per 1000 feet (~300 meters) above 10,000 feet  Nonoperating – 40,000 ft (12,000 m)  
Sound Pressure Level |  83 dBA—at normal operating temperature.  
  
  * Environmental Conditions and Power Requirement Specifications for Twinax SFP+ Transceivers


### Environmental Conditions and Power Requirement Specifications for Twinax SFP+ Transceivers

Table 4. Environmental Conditions and Power Requirement for the SFP+ Transceiver Parameter |  Symbol |  Min. |  Max. |  Unit  
---|---|---|---|---  
Storage temperature |  TS |  –40 |  85 |  °C  
Case temperature |  TC |  0 |  50 |  °C  
Module supply voltage |  VCCT,R |  3.1 |  3.5 |  V  
  
##  Specifications for the Cisco UCS X9508 Chassis Power Supply Units

Table 5. AC-input Titanium Power Supply (N20-PAC5-2800W) Specifications Description  | Specification   
---|---  
AC-input voltage  |  Voltage Range 100-127 VAC, 200-240 VAC Nominal (range: 90-140 VAC, 180-264 VAC)   
AC-input frequency  |  50 to 60 Hz nominal (range: 47 to 63 Hz)   
Maximum AC-input current  |  18 A @ 90 VAC  18 A @ 180 VAC   
Maximum input VA  |  3200 VA at 230 VAC   
Maximum output power per power supply  |  2800 W @ 200-240 VAC Nominal 1400 W @ 100-127 VAC Nominal   
Maximum inrush current  |  35 A (sub cycle duration)   
Minimum hold up time  |  10 ms @ 1400 W  10 ms @ 2800 W   
Power supply main output voltage  |  54 VDC   
Power supply standby voltage  |  3.4 V   
Efficiency Rating  |  80+ Titanium Certified   
Input connector  |  IEC320 C20  System input power connectors are located in the chassis PEMs, not on the power supply  
  
For information about supported power cords, see Technical Specifications. 

## Supported AC Power Cords and Plugs

The AC power connectors on the chassis PEM use an IEC 320 C20 socket. Each chassis power supply has a separate power cord. The power cord that you use to connect the power supply units to an AC power source will have an IEC 320 C19 plug on one end and on the other end one that conforms to the AC power outlet specifications for your country. See the following table to determine which cord to order for your chassis power supply units. When you determine which power cord you need to order, you can verify that its plugs conform to the power outlets for your facility by clicking on its reference link. 

The jumper power cords, for use in racks, are available as an optional alternative to the standard power cords. The optional jumper power cords have an IEC C19 connector (such as a Cisco RP Series PEM) on the end that plugs into the chassis’ PEM and an IEC C20 connector on the end that plugs into an IEC C19 outlet receptacle. For more information, contact your Cisco Systems representative. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Only the regular power cords or jumper power cords provided with the chassis are supported.

* * *  
  
---|---  
  
  * Australia and New Zealand
  * Continental Europe
  * International
  * Israel
  * Japan and North America
  * Peoples Republic of China
  * Taiwan
  * Switzerland


### Australia and New Zealand

Power Cord Part Number—CAB-AC-16A-AUS

Cord Set Rating—16A, 250 VAC

Figure 3. CAB-AC-16A-AUS Power Cord for the Cisco UCS X9508 Chassis  ![](/c/dam/en/us/td/i/100001-200000/140001-150000/140001-141000/140586.eps/_jcr_content/renditions/140586.jpg)

### Continental Europe

Power Cord Part Number—CAB-AC-2800W-EU

Cord Set Rating—16A, 250 VAC

Figure 4. CAB-AC-2800W-EU Power Cord for the UCS X9508 Chassis  ![](/c/dam/en/us/td/i/100001-200000/110001-120000/113001-114000/113360.eps/_jcr_content/renditions/113360.jpg)

### International

Power Cord Part Number—CAB-AC-2800W-INT

Cord Set Rating—16A, 250 VAC

Figure 5. CAB-AC-2800W-INT Power Cord for the UCS X9508 Chassis  ![](/c/dam/en/us/td/i/100001-200000/110001-120000/113001-114000/113361.eps/_jcr_content/renditions/113361.jpg)

### Israel

Power Cord Part Number—CAB-AC-2800W-ISRL

Cord Set Rating—16A, 250 VAC

Figure 6. CAB-AC-2800W-ISRL Power Cord for the UCS X9508 Chassis  ![](/c/dam/en/us/td/i/100001-200000/130001-140000/130001-131000/130113.eps/_jcr_content/renditions/130113.jpg)

### Japan and North America

#### Non-Locking 200 to 240 VAC operation

Power Cord Part Number—CAB-AC-2800W-US1

Cord Set Rating—16A, 250 VAC

Figure 7. CAB-AC-2800W-US1 Power Cord for the UCS X9508 Chassis  ![](/c/dam/en/us/td/i/100001-200000/110001-120000/113001-114000/113362.ps/_jcr_content/renditions/113362.jpg)

#### Locking 200 to 240 VAC Operation

Power Cord Part Number—CAB-AC-C6K-TWLK

Cord Set Rating—16A, 250 VAC

Figure 8. CAB-AC-C6K-TWLK Power Cord for the UCS X9508 Chassis  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309544.jpg)

### Peoples Republic of China

Power Cord Part Number—CAB-AC-16A-CH

Cord Set Rating—16A, 250 VAC

Figure 9. CAB-AC-16A-CH Power Cord for the Cisco UCSX X9508 Chassis  ![](/c/dam/en/us/td/i/100001-200000/120001-130000/126001-127000/126792.eps/_jcr_content/renditions/126792.jpg)

### Taiwan

Power Cord—CAB-AC-C19-TW

Plug—250 VAC 16 A, C19 

Length—7.5 feet / 2.3 meters

### Switzerland

Power Cord Part Number—CAB-ACS-16

Cord Set Rating—16A, 250 VAC

Figure 10. CAB-ACS-16 Power Cord for the UCS X9508 Chassis  ![](/c/dam/en/us/td/i/100001-200000/190001-200000/192001-193000/192844.eps/_jcr_content/renditions/192844.jpg)

### 

---

## Page 7: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x9508/install/b-ucs-x9508-install/m-ifm-afm-xfm-fru-replacement-instructions-labels.html

# Intelligent Fabric Module (IFM), X-Fabric Module, and Active Fan Module Field Replaceable Unit Instructions

This appendix contains the following topics:

## Cisco UCS 9108 25G IFM Field Replaceable Unit Replacement Instructions

The rear of the Cisco UCS X9508 can contain a pair of UCS 9108 Intelligent Fabric Modules (IFMs), which come in either 25G or 100G speeds. 

Refer to the following illustration for information about field-replacement options on the UCS 9108 25G IFM (UCSX-I-9108-25G).

Figure 1. Cisco UCS 9108 25G IFMs (UCSX-I-9108-25G) Replacement Instructions  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/473001-474000/473982.jpg)

## Cisco UCS 9108 100G IFM Field Replaceable Unit Replacement Instructions

The rear of the Cisco UCS X9508 contains a pair of UCS 9108 Intelligent Fabric Modules (IFMs), which come in either 25Gbps or 100Gbps speeds. 

Refer to the following illustration for information about field-replacement options on the UCS 9108 100G IFM (UCSX-I-9108-100G).

Figure 2. Cisco UCS 9108 100G IFMs (UCSX-I-9108-100G) Replacement Instructions  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/473001-474000/473981.jpg)

## Cisco UCS 9508 Active Fan Module (AFM) Field Replaceable Unit Replacement Instructions

The rear of the Cisco UCS X9508 chassis can contain a rear blank (UCS-9508-RBLK) that is an active fan module. 

Refer to the relevant section below for the specific AFM installed in your system.

Figure 3. Cisco UCS 9508 Rear Blank (UCSX-9508-RBLK) Replacement Instructions  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/476001-477000/476034.png)

## Cisco UCS X9416 X-Fabric Module Field Replaceable Unit Replacement Instructions

Refer to the following illustration for field-replacement instructions for the Cisco UCS X9416 X-Fabric Module (XFM). 

Figure 4. Cisco UCS X9416 X-Fabric Module (UCSX-F-9416) Field Replacement Instructions  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/476001-477000/476033.jpg)

## Cisco UCS X9516 X-Fabric Module Field Replaceable Unit Replacement Instructions

Refer to the following illustration for field-replacement instructions for the Cisco UCS X9516 X-Fabric Module (XFM). 

Figure 5. Cisco UCS X9516 X-Fabric Module (UCSX-F-9516) Field Replacement Instructions  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/476001-477000/476033.jpg)

---

## Page 8: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x9508/install/b-ucs-x9508-install/m-site-planning-and-maint-records.html

# Site Planning and Maintenance Records

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For information about how to query the chassis for configuration information, see the _Cisco UCS Configuration Guide._

* * *  
  
---|---  
  
This appendix includes the following records to use when installing the Cisco UCS X9508 server chassis:

## Site Preparation Checklist

Planning the location and layout of your equipment is essential for successful network operation, ventilation, and accessibility. Consider heat dissipation when sizing the air-conditioning requirements for an installation. 

Table 1. Site Planning Checklist Task No. |  Planning Activity |  Verified By |  Time |  Date  
---|---|---|---|---  
1 |  Space evaluation:

  * Space and layout
  * Floor covering
  * Impact and vibration
  * Lighting
  * Maintenance access

|  |  |   
2 |  Environmental evaluation:

  * Ambient temperature
  * Humidity
  * Altitude
  * Atmospheric contamination
  * Air flow

|  |  |   
3 |  Power evaluation:

  * Input power type
  * Power receptacles 
  * Receptacle proximity to the equipment
  * Dedicated circuit for power supply
  * Dedicated (separate) circuits for redundant power supplies
  * UPS for power failures 

|  |  |   
4 |  Grounding evaluation:

  * Circuit breaker size
  * CO ground (AC- powered systems)

|  |  |   
5 |  Cable and interface equipment evaluation:

  * Cable type
  * Connector type
  * Cable distance limitations
  * Interface equipment (transceivers)

|  |  |   
6 |  EMI evaluation: 

  * Distance limitations for signaling
  * Site wiring
  * RFI levels 

|  |  |   
1 Verify that the power supply installed in the chassis has a dedicated AC source circuit.  2 UPS: uninterruptable power supply.  3 EMI: electromagnetic interference.  4 RFI: radio frequency interference. 

## Contact and Site Information

Use the following worksheet to record contact and site information.

Table 2. Contact and Site Information Contact person  |   
---|---  
Contact phone  |   
Contact e-mail |   
Building/site name  |   
Data center location  |   
Floor location  |   
Address (line 1)  |   
Address (line 2)  |   
City  |   
State  |   
Zip code  |   
Country  |   
  
## Chassis and Module Information

Use the following worksheets to record information about the server chassis and the modules it contains.

**Contract Number_______________________________________________**

**Chassis Serial Number___________________________________________**

**Product Number________________________________________________**

Table 3. Device Information Device |  Serial Number | Notes  
---|---|---  
**Compute Node–1** |  |   
**Compute Node–2** |  |   
**Compute Node–3** |  |   
**Compute Node–4** |  |   
**Compute Node–5** |  |   
**Compute Node–6** |  |   
**Compute Node–7** |  |   
**Compute Node–8** |  |   
**Intelligent Fabric Module-1** |  |   
**Intelligent Fabric Module-2** |  |   
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The serial numbers of all server chassis modules can be obtained using the Intersight management interface. 

* * *  
  
---|---  
  
## FEX Port Connection Record

Table 4. Chassis FEX to Fabric Interconnect Port Connection Record FEX |  Connected to  
---|---  
Number |  Port |  Fabric Interconnect A or B |  Slot |  Port |  Connection notes  
**1** |  1 |  |  |  |   
2 |  |  |  |   
3 |  |  |  |   
4 |  |  |  |   
5 |  |  |  |   
6 |  |  |  |   
7 |  |  |  |   
8 |  |  |  |   
**2** |  1 |  |  |  |   
2 |  |  |  |   
3 |  |  |  |   
4 |  |  |  |   
5 |  |  |  |   
6 |  |  |  |   
7 |  |  |  |   
8 |  |  |  |   
  
## UCS 6536 Fabric Interconnect Port Connection Record

Table 5.  Port Connection Record Fabric Interconnect  | Connected to   
---|---  
Number  |  Port  |  Slot  |  Port  |  Connection notes   
**1** |  1  |  |  |   
2  |  |  |   
3  |  |  |   
4  |  |  |   
5  |  |  |   
6  |  |  |   
7  |  |  |   
8  |  |  |   
**2** |  1  |  |  |   
2  |  |  |   
3  |  |  |   
4  |  |  |   
5  |  |  |   
6  |  |  |   
7  |  |  |   
8  |  |  | 

---

## Page 9: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x9508/install/b-ucs-x9508-install/b-ucs-x9508-install_index.html

> ## Contents  
>   
> A \- B \- C \- E \- F \- G \- H \- I \- L \- M \- O \- P \- R \- S \- T \- U \- W \- X
> 
> ## Index
> 
> A
> 
> air flow [1](m-installing-and-removing-components.html#concept_D5090FAF2DEB41A691B34E8A9294C30A)
> 
> attaching, cable management trays [1](m-installation.html#Cisco_Concept.dita_65c12002-7b80-4316-97a6-d086e870bda4)
> 
> B
> 
> bottom cable management, installing [1](m-installation.html#Cisco_Task_in_List_GUI.dita_9f3ea19e-b3f1-47a1-9ee4-967a269bc5da)
> 
> C
> 
> cable management tray, installing [1](m-installation.html#Cisco_Task_in_List_GUI.dita_77a99c2e-2c25-4fd0-afa6-596b075668c8)
> 
> cable management tray, removing [1](m-installation.html#Cisco_Task_in_List_GUI.dita_377c830e-a9c3-4cf8-b274-2a3d166bd736)
> 
> cable management, trays, attaching [1](m-installation.html#Cisco_Concept.dita_65c12002-7b80-4316-97a6-d086e870bda4)
> 
> cage nuts, installing [1](m-installation.html#Cisco_Task_in_List_GUI.dita_a54f3a08-0675-4766-a253-bb930d5cdbdf)
> 
> cage nuts, installing, round-hole rack [1](m-installation.html#Cisco_Task_in_List_GUI.dita_a54f3a08-0675-4766-a253-bb930d5cdbdf)
> 
> chassis
> 
> Cisco UCS X9508 server chassis [1](m-ucsx-9508-chassis-overview.html#Cisco_Concept.dita_01ec45d3-1795-4a1b-b700-a59924d729eb)
> 
> chassis installation [1](m-installation.html#Cisco_Reference.dita_e84d4377-03c6-4a77-9fad-011cdc846f76) [2](m-installation.html#ID199)
> 
> chassis installation, completing [1](m-installation.html#Cisco_Task_in_List_GUI.dita_39c3cddb-dbd6-4a29-bafb-59d0b2d12673)
> 
> chassis installation, round-hole rack [1](m-installation.html#Cisco_Task_in_List_GUI.dita_d4b5c01a-7ab3-4d58-b5b2-27189418f5c1)
> 
> chassis installation, square-hole rack [1](m-installation.html#ID325)
> 
> chassis LED locations [1](m-ucsx-9508-chassis-overview.html#ID499)
> 
> chassis LEDs [1](m-ucsx-9508-chassis-overview.html#concept_17C27E0BAF3947CA84830EA2FF1DB14C)
> 
> chassis PCB Assembly (PCBA), recycling [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_a7d44deb-bfe5-4915-b7bd-9ce9bbd0df9b)
> 
> chassis removal [1](m-installation.html#ID487)
> 
> chassis repacking [1](m-installation.html#ID526)
> 
> chassis specifications [1](m-technical-specs.html#ID20)
> 
> chassis, inspection [1](m-installation.html#ID151)
> 
> chassis, unpacking [1](m-installation.html#ID151)
> 
> Cisco UCS 9108 intelligent fabric module [1](m-ucsx-9508-chassis-overview.html#Cisco_Concept.dita_079dc31b-44e1-4d0a-87dd-ff1e91e343b2) [2](m-ucsx-9508-chassis-overview.html#Cisco_Concept.dita_adf5e8fb-ef7b-483e-83e3-b6371c539036)
> 
> Cisco UCS chassis power configuration [1](m-ucsx-9508-chassis-overview.html#ID447)
> 
> Cisco UCS Chassis Power Supplies [1](m-ucsx-9508-chassis-overview.html#ID437)
> 
> Cisco UCS Chassis Power Supply buttons [1](m-ucsx-9508-chassis-overview.html#ID443)
> 
> Cisco UCS Chassis Power supply connectors [1](m-ucsx-9508-chassis-overview.html#ID445)
> 
> Cisco UCS Chassis Power supply LEDs [1](m-ucsx-9508-chassis-overview.html#ID440)
> 
> compute node
> 
> installing and removing [1](m-installing-and-removing-components.html#reference_5563DA0494CB47048459002B6B6A3566)
> 
> compute node blank, installing [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_4bc54a18-554d-4884-912d-ece689386837)
> 
> compute node blank, removing [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_4e829454-48fa-495a-801a-8539c84d7c8e)
> 
> compute node, Cisco UCS X210c M6 [1](m-ucsx-9508-chassis-overview.html#Cisco_Concept.dita_44202810-64b3-4051-aa3c-738a205f638f)
> 
> compute node, installing [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_a5de4997-a755-4e98-85ae-2ddea6267cc0)
> 
> compute node, removing [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_ca63ac0d-2bea-478d-8155-5b12d443a302)
> 
> compute nodes, general [1](m-ucsx-9508-chassis-overview.html#ID112)
> 
> connecting earth ground [1](m-installation.html#Cisco_Task_in_List_GUI.dita_6b9a7f83-0722-4c2a-8bcf-fb9c9fced336)
> 
> connecting earth ground, side [1](m-installation.html#Cisco_Task_in_List_GUI.dita_f8f56b50-bd03-4386-9a36-1b4796e59461)
> 
> E
> 
> earth ground options [1](m-installation.html#Cisco_Concept.dita_abe7095b-983f-42a1-9bae-e4288d507532)
> 
> earth ground, connecting [1](m-installation.html#Cisco_Task_in_List_GUI.dita_f8f56b50-bd03-4386-9a36-1b4796e59461) [2](m-installation.html#Cisco_Task_in_List_GUI.dita_6b9a7f83-0722-4c2a-8bcf-fb9c9fced336)
> 
> extended power mode [1](m-ucsx-9508-chassis-overview.html#ID460)
> 
> F
> 
> fan module, replacing [1](m-installing-and-removing-components.html#concept_D5090FAF2DEB41A691B34E8A9294C30A)
> 
> fan modules [1](m-ucsx-9508-chassis-overview.html#ID430)
> 
> Features and Benefits [1](m-ucsx-9508-chassis-overview.html#ID40)
> 
> filler panel [1](m-installing-and-removing-components.html#removing-the-pcie-filler-panel)
> 
> filler panel (X9516), removing [1](m-installing-and-removing-components.html#removing-the-pcie-filler-panel)
> 
> G
> 
> ground lug, installing [1](m-installation.html#Cisco_Task_in_List_GUI.dita_9f3ea19e-b3f1-47a1-9ee4-967a269bc5da)
> 
> grounding options [1](m-installation.html#Cisco_Concept.dita_abe7095b-983f-42a1-9bae-e4288d507532)
> 
> H
> 
> height [1](m-technical-specs.html#ID20)
> 
> I
> 
> IFM (UCS 9108 100G), recycling [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_5667164d-680e-4432-93b5-4c21f361e414)
> 
> IFM (UCS 9108 25G), recycling [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_184093b0-3726-40d1-9713-ef4c8184a4b2)
> 
> installation
> 
> airflow considerations [1](m-installation.html#ID76)
> 
> guidelines [1](m-installation.html#ID107)
> 
> moving server chassis [1](m-installation.html#ID91)
> 
> rack requirements [1](m-installation.html#ID54)
> 
> required equipment [1](m-installation.html#ID141)
> 
> shipping container [1](m-installation.html#ID151)
> 
> unpacking and inspection [1](m-installation.html#ID151)
> 
> installation, completing [1](m-installation.html#Cisco_Task_in_List_GUI.dita_39c3cddb-dbd6-4a29-bafb-59d0b2d12673)
> 
> installation, rack rails, round-hole rack [1](m-installation.html#Cisco_Task_in_List_GUI.dita_9de7639c-07fb-40c4-bce3-9936ade099c0)
> 
> installation, rack rails, square-hole rack [1](m-installation.html#ID241)
> 
> installing bottom cable management [1](m-installation.html#Cisco_Task_in_List_GUI.dita_9f3ea19e-b3f1-47a1-9ee4-967a269bc5da)
> 
> installing cage nuts [1](m-installation.html#Cisco_Task_in_List_GUI.dita_a54f3a08-0675-4766-a253-bb930d5cdbdf)
> 
> installing cage nuts, round-hole rack [1](m-installation.html#Cisco_Task_in_List_GUI.dita_a54f3a08-0675-4766-a253-bb930d5cdbdf)
> 
> installing chassis [1](m-installation.html#ID199)
> 
> installing chassis, round-hole rack [1](m-installation.html#Cisco_Task_in_List_GUI.dita_d4b5c01a-7ab3-4d58-b5b2-27189418f5c1)
> 
> installing chassis, square-hole rack [1](m-installation.html#ID325)
> 
> installing ground lug [1](m-installation.html#Cisco_Task_in_List_GUI.dita_9f3ea19e-b3f1-47a1-9ee4-967a269bc5da)
> 
> installing Power Entry Modules [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_9ee2f06c-b5d1-4345-bd19-c78086e04334)
> 
> installing spring nuts, round-hole rack [1](m-installation.html#Cisco_Task_in_List_GUI.dita_a54f3a08-0675-4766-a253-bb930d5cdbdf)
> 
> installing the chassis [1](m-installation.html#Cisco_Reference.dita_e84d4377-03c6-4a77-9fad-011cdc846f76) [2](m-installing-and-removing-components.html#concept_88175EB15FF14DAAA5E6226CCC4A6857)
> 
> installing, cable management tray [1](m-installation.html#Cisco_Task_in_List_GUI.dita_77a99c2e-2c25-4fd0-afa6-596b075668c8)
> 
> installing, compute node [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_a5de4997-a755-4e98-85ae-2ddea6267cc0)
> 
> installing, compute node blank [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_4bc54a18-554d-4884-912d-ece689386837)
> 
> installing, Intelligent Fabric Module (IFM) [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_8b4b666c-e890-4d76-bba0-2720cedc21e8)
> 
> installing, PCIe card (X9516) [1](m-installing-and-removing-components.html#installing-a-pcie-card-into-a-ucs-x9516-x-fabric-module-pcie-cage)
> 
> installing, PCIe filler panel (X9516) [1](m-installing-and-removing-components.html#installing-the-pcie-filler-panel)
> 
> installing, power supply blank [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_74186ea3-fa34-456a-8d21-86218ba5ffdd)
> 
> installing, PSU keying bracket [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_b68a2a6c-5ab0-41e5-9bae-8338be6c0728)
> 
> installing, rear module's fan [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_6da08bac-e5f2-499d-8b2c-61efa38b7a85)
> 
> installing, top cable management [1](m-installation.html#Cisco_Task_in_List_GUI.dita_42a15b91-234d-4247-893d-2059d848cc3d)
> 
> installing, X-Fabric Module [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_6aacc16c-a0ba-465b-a63c-82b01ed2ff96)
> 
> installing, X-Fabric Module blank [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_c7ad8a2f-a54e-42f8-89a0-17591eedf9fa)
> 
> Intelligent Fabric Module (IFM), installing [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_8b4b666c-e890-4d76-bba0-2720cedc21e8)
> 
> Intelligent Fabric Module (IFM), removing [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_214ffc57-18df-4e50-90d6-d08f707177fb)
> 
> intelligent fabric module, Cisco UCS 9108 [1](m-ucsx-9508-chassis-overview.html#Cisco_Concept.dita_079dc31b-44e1-4d0a-87dd-ff1e91e343b2) [2](m-ucsx-9508-chassis-overview.html#Cisco_Concept.dita_adf5e8fb-ef7b-483e-83e3-b6371c539036)
> 
> L
> 
> LED
> 
> compute node health [1](m-ucsx-9508-chassis-overview.html#ID544)
> 
> LEDs [1](m-ucsx-9508-chassis-overview.html#concept_17C27E0BAF3947CA84830EA2FF1DB14C)
> 
> M
> 
> mounting brackets (rear), installing, round-hole rack [1](m-installation.html#Cisco_Task_in_List_GUI.dita_90c294c3-becb-4df3-ae52-e1bf4441d4df)
> 
> mounting brackets (rear), installing, square-hole rack [1](m-installation.html#Cisco_Task_in_List_GUI.dita_565b29de-af1e-426e-b13c-03d64e1454f7)
> 
> O
> 
> overview, system [1](m-ucsx-9508-chassis-overview.html#concept_893CC74ADFB44A9FB4EFCF8FDA4CF0C7)
> 
> P
> 
> PCIe card [1](m-installing-and-removing-components.html#removing-a-pcie-card-from-a-ucs-x9516-x-fabric-module-pcie-cage) [2](m-installing-and-removing-components.html#installing-a-pcie-card-into-a-ucs-x9516-x-fabric-module-pcie-cage)
> 
> PCIe card (X9516), installing [1](m-installing-and-removing-components.html#installing-a-pcie-card-into-a-ucs-x9516-x-fabric-module-pcie-cage)
> 
> PCIe card (X9516), removing [1](m-installing-and-removing-components.html#removing-a-pcie-card-from-a-ucs-x9516-x-fabric-module-pcie-cage)
> 
> PCIe filler panel (X9516), installing [1](m-installing-and-removing-components.html#installing-the-pcie-filler-panel)
> 
> power configuration
> 
> grid redundancy [1](m-ucsx-9508-chassis-overview.html#ID476)
> 
> n+1 redundancy [1](m-ucsx-9508-chassis-overview.html#ID465)
> 
> n+2 redundancy [1](m-ucsx-9508-chassis-overview.html#ID465)
> 
> non-redundant [1](m-ucsx-9508-chassis-overview.html#ID460)
> 
> power entry modules, installing [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_9ee2f06c-b5d1-4345-bd19-c78086e04334)
> 
> power entry modules, removing [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_5a104076-fbd7-4e78-97d0-3f553784c16e)
> 
> power save mode [1](m-ucsx-9508-chassis-overview.html#ID460)
> 
> power supply
> 
> AC-input current [1](m-technical-specs.html#ID256)
> 
> maximum power for each power supply [1](m-technical-specs.html#ID256)
> 
> power supply output voltage [1](m-technical-specs.html#ID256)
> 
> power supply blank, installing [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_74186ea3-fa34-456a-8d21-86218ba5ffdd)
> 
> power supply blank, removing [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_2619b2ab-3542-4071-b66b-5419c090a668)
> 
> PSU keying bracket, installing [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_b68a2a6c-5ab0-41e5-9bae-8338be6c0728)
> 
> PSU keying bracket, removing [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_0de333c6-236e-4e4f-82da-c34596b93819)
> 
> R
> 
> rack layout, round-hole rack [1](m-installation.html#Cisco_Reference.dita_fd7bb4df-c1f3-4457-a981-f83ebbbb9975)
> 
> rack layout, square-hole rack [1](m-installation.html#Cisco_Reference.dita_c6c7fd99-c54e-47c4-aa7d-a3f6ddfb8e0f)
> 
> rack rails [1](m-installation.html#Cisco_Concept.dita_2a45d63e-4148-45f6-8137-276a3bd2847b)
> 
> rail kit [1](m-installation.html#Cisco_Concept.dita_2a45d63e-4148-45f6-8137-276a3bd2847b)
> 
> rails, installing, round-hole rack [1](m-installation.html#Cisco_Task_in_List_GUI.dita_9de7639c-07fb-40c4-bce3-9936ade099c0)
> 
> rails, installing, sqaure-hole rack [1](m-installation.html#ID241)
> 
> rear module fan, installing [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_6da08bac-e5f2-499d-8b2c-61efa38b7a85)
> 
> rear module fan, removing [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_9c84a39b-e540-4afa-bedd-ea0f62e44b4d)
> 
> rear mounting brackets, installing, round-hole rack [1](m-installation.html#Cisco_Task_in_List_GUI.dita_90c294c3-becb-4df3-ae52-e1bf4441d4df)
> 
> rear mounting brackets, installing, square-hole rack [1](m-installation.html#Cisco_Task_in_List_GUI.dita_565b29de-af1e-426e-b13c-03d64e1454f7)
> 
> recycling, chassis PCB Assembly (PCBA) [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_a7d44deb-bfe5-4915-b7bd-9ce9bbd0df9b)
> 
> recycling, UCS 100G IFM PCB [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_5667164d-680e-4432-93b5-4c21f361e414)
> 
> recycling, UCS 25G IFM PCB [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_184093b0-3726-40d1-9713-ef4c8184a4b2)
> 
> recycling, X-Fabric Module Blank PCBs [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_6366807c-f98f-47a5-af24-5c7e643339af)
> 
> recycling, X9416 Fabric Module PCBs [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_ecf973be-ff4a-4ca6-9a5d-b53c4f4c3fa7)
> 
> recycling, X9516 Fabric Module PCBs [1](m-installing-and-removing-components.html#recycling-a-ucs-x9516-x-fabric-module-pcb)
> 
> removing
> 
> fan module [1](m-installing-and-removing-components.html#ID303)
> 
> power supply [1](m-installing-and-removing-components.html#ID163)
> 
> removing power supply blank [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_2619b2ab-3542-4071-b66b-5419c090a668)
> 
> removing PSU keying bracket [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_0de333c6-236e-4e4f-82da-c34596b93819)
> 
> removing, cable management tray [1](m-installation.html#Cisco_Task_in_List_GUI.dita_377c830e-a9c3-4cf8-b274-2a3d166bd736)
> 
> removing, chassis [1](m-installation.html#ID487)
> 
> removing, compute node [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_ca63ac0d-2bea-478d-8155-5b12d443a302)
> 
> removing, compute node blank [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_4e829454-48fa-495a-801a-8539c84d7c8e)
> 
> removing, Intelligent Fabric Module (IFM) [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_214ffc57-18df-4e50-90d6-d08f707177fb)
> 
> removing, PCIe cad (X9516) [1](m-installing-and-removing-components.html#removing-a-pcie-card-from-a-ucs-x9516-x-fabric-module-pcie-cage) [2](m-installing-and-removing-components.html#removing-the-pcie-filler-panel)
> 
> removing, power entry modules [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_5a104076-fbd7-4e78-97d0-3f553784c16e)
> 
> removing, rear module's fan [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_9c84a39b-e540-4afa-bedd-ea0f62e44b4d)
> 
> removing, X-Fabric Module [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_439fad4d-f60c-4159-a435-ac9504b2e08a)
> 
> removing, X-Fabric Module blank [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_f2b9f428-2d8c-4471-bff3-b798f442ae41)
> 
> repacking, chassis [1](m-installation.html#ID526)
> 
> replacing fan module [1](m-installing-and-removing-components.html#concept_D5090FAF2DEB41A691B34E8A9294C30A)
> 
> round-hole rack, chassis installation [1](m-installation.html#Cisco_Task_in_List_GUI.dita_d4b5c01a-7ab3-4d58-b5b2-27189418f5c1)
> 
> S
> 
> serial numbers [1](m-site-planning-and-maint-records.html#reference_cbj_b3d_vhb)
> 
> SFP+
> 
> module supply voltage [1](m-technical-specs.html#ID205)
> 
> side-mount ground, connecting [1](m-installation.html#Cisco_Task_in_List_GUI.dita_f8f56b50-bd03-4386-9a36-1b4796e59461)
> 
> site planning
> 
> checklist [1](m-site-planning-and-maint-records.html#ID23)
> 
> information [1](m-site-planning-and-maint-records.html#ID119)
> 
> spring nuts, installing, round-hole rack [1](m-installation.html#Cisco_Task_in_List_GUI.dita_a54f3a08-0675-4766-a253-bb930d5cdbdf)
> 
> square-hole rack, chassis installation [1](m-installation.html#ID325)
> 
> system overview [1](m-ucsx-9508-chassis-overview.html#concept_893CC74ADFB44A9FB4EFCF8FDA4CF0C7)
> 
> T
> 
> technical specifications
> 
> chassis dimensions [1](m-technical-specs.html#ID6)
> 
> top cable management, installing [1](m-installation.html#Cisco_Task_in_List_GUI.dita_42a15b91-234d-4247-893d-2059d848cc3d)
> 
> U
> 
> UCS 100G IFM PCB, recycling [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_5667164d-680e-4432-93b5-4c21f361e414)
> 
> UCS 25G IFM PCB, recycling [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_184093b0-3726-40d1-9713-ef4c8184a4b2)
> 
> UCS X210c M6 compute node [1](m-ucsx-9508-chassis-overview.html#Cisco_Concept.dita_44202810-64b3-4051-aa3c-738a205f638f)
> 
> W
> 
> weight
> 
> chassis fully populated [1](m-technical-specs.html#ID20)
> 
> width [1](m-technical-specs.html#ID20)
> 
> X
> 
> X-Fabric Module Blank PCBs, recycling [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_6366807c-f98f-47a5-af24-5c7e643339af)
> 
> X-Fabric Module blank, installing [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_c7ad8a2f-a54e-42f8-89a0-17591eedf9fa)
> 
> X-Fabric Module, installing [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_6aacc16c-a0ba-465b-a63c-82b01ed2ff96)
> 
> X-Fabric Module, removing [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_439fad4d-f60c-4159-a435-ac9504b2e08a)
> 
> X-Fabric Moodule blank, removing [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_f2b9f428-2d8c-4471-bff3-b798f442ae41)
> 
> X9416 Fabric Module PCBs, recycling [1](m-installing-and-removing-components.html#Cisco_Task_in_List_GUI.dita_ecf973be-ff4a-4ca6-9a5d-b53c4f4c3fa7)
> 
> X9516 Fabric Module PCBs, recycling [1](m-installing-and-removing-components.html#recycling-a-ucs-x9516-x-fabric-module-pcb)
> 
> X9516 module [1](m-installing-and-removing-components.html#removing-a-pcie-card-from-a-ucs-x9516-x-fabric-module-pcie-cage) [2](m-installing-and-removing-components.html#removing-the-pcie-filler-panel) [3](m-installing-and-removing-components.html#installing-a-pcie-card-into-a-ucs-x9516-x-fabric-module-pcie-cage)

---

## Page 10: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x9508/install/m-ifm-afm-xfm-fru-replacement-instructions-labels.html

# Intelligent Fabric Module (IFM), X-Fabric Module, and Active Fan Module Field Replaceable Unit Instructions

This appendix contains the following topics:

## Cisco UCS 9108 25G IFM Field Replaceable Unit Replacement Instructions

The rear of the Cisco UCS X9508 can contain a pair of UCS 9108 Intelligent Fabric Modules (IFMs), which come in either 25G or 100G speeds. 

Refer to the following illustration for information about field-replacement options on the UCS 9108 25G IFM (UCSX-I-9108-25G).

Figure 1. Cisco UCS 9108 25G IFMs (UCSX-I-9108-25G) Replacement Instructions  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/473001-474000/473982.jpg)

## Cisco UCS 9108 100G IFM Field Replaceable Unit Replacement Instructions

The rear of the Cisco UCS X9508 contains a pair of UCS 9108 Intelligent Fabric Modules (IFMs), which come in either 25Gbps or 100Gbps speeds. 

Refer to the following illustration for information about field-replacement options on the UCS 9108 100G IFM (UCSX-I-9108-100G).

Figure 2. Cisco UCS 9108 100G IFMs (UCSX-I-9108-100G) Replacement Instructions  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/473001-474000/473981.jpg)

## Cisco UCS 9508 Active Fan Module (AFM) Field Replaceable Unit Replacement Instructions

The rear of the Cisco UCS X9508 chassis can contain a rear blank (UCS-9508-RBLK) that is an active fan module. 

Refer to the relevant section below for the specific AFM installed in your system.

Figure 3. Cisco UCS 9508 Rear Blank (UCSX-9508-RBLK) Replacement Instructions  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/476001-477000/476034.png)

## Cisco UCS X9416 X-Fabric Module Field Replaceable Unit Replacement Instructions

Refer to the following illustration for field-replacement instructions for the Cisco UCS X9416 X-Fabric Module (XFM). 

Figure 4. Cisco UCS X9416 X-Fabric Module (UCSX-F-9416) Field Replacement Instructions  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/476001-477000/476033.jpg)

## Cisco UCS X9516 X-Fabric Module Field Replaceable Unit Replacement Instructions

Refer to the following illustration for field-replacement instructions for the Cisco UCS X9516 X-Fabric Module (XFM). 

Figure 5. Cisco UCS X9516 X-Fabric Module (UCSX-F-9516) Field Replacement Instructions  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/476001-477000/476033.jpg)

---

## Page 11: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x9508/install/m-site-planning-and-maint-records.html

# Site Planning and Maintenance Records

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For information about how to query the chassis for configuration information, see the _Cisco UCS Configuration Guide._

* * *  
  
---|---  
  
This appendix includes the following records to use when installing the Cisco UCS X9508 server chassis:

## Site Preparation Checklist

Planning the location and layout of your equipment is essential for successful network operation, ventilation, and accessibility. Consider heat dissipation when sizing the air-conditioning requirements for an installation. 

Table 1. Site Planning Checklist Task No. |  Planning Activity |  Verified By |  Time |  Date  
---|---|---|---|---  
1 |  Space evaluation:

  * Space and layout
  * Floor covering
  * Impact and vibration
  * Lighting
  * Maintenance access

|  |  |   
2 |  Environmental evaluation:

  * Ambient temperature
  * Humidity
  * Altitude
  * Atmospheric contamination
  * Air flow

|  |  |   
3 |  Power evaluation:

  * Input power type
  * Power receptacles 
  * Receptacle proximity to the equipment
  * Dedicated circuit for power supply
  * Dedicated (separate) circuits for redundant power supplies
  * UPS for power failures 

|  |  |   
4 |  Grounding evaluation:

  * Circuit breaker size
  * CO ground (AC- powered systems)

|  |  |   
5 |  Cable and interface equipment evaluation:

  * Cable type
  * Connector type
  * Cable distance limitations
  * Interface equipment (transceivers)

|  |  |   
6 |  EMI evaluation: 

  * Distance limitations for signaling
  * Site wiring
  * RFI levels 

|  |  |   
1 Verify that the power supply installed in the chassis has a dedicated AC source circuit.  2 UPS: uninterruptable power supply.  3 EMI: electromagnetic interference.  4 RFI: radio frequency interference. 

## Contact and Site Information

Use the following worksheet to record contact and site information.

Table 2. Contact and Site Information Contact person  |   
---|---  
Contact phone  |   
Contact e-mail |   
Building/site name  |   
Data center location  |   
Floor location  |   
Address (line 1)  |   
Address (line 2)  |   
City  |   
State  |   
Zip code  |   
Country  |   
  
## Chassis and Module Information

Use the following worksheets to record information about the server chassis and the modules it contains.

**Contract Number_______________________________________________**

**Chassis Serial Number___________________________________________**

**Product Number________________________________________________**

Table 3. Device Information Device |  Serial Number | Notes  
---|---|---  
**Compute Node–1** |  |   
**Compute Node–2** |  |   
**Compute Node–3** |  |   
**Compute Node–4** |  |   
**Compute Node–5** |  |   
**Compute Node–6** |  |   
**Compute Node–7** |  |   
**Compute Node–8** |  |   
**Intelligent Fabric Module-1** |  |   
**Intelligent Fabric Module-2** |  |   
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The serial numbers of all server chassis modules can be obtained using the Intersight management interface. 

* * *  
  
---|---  
  
## FEX Port Connection Record

Table 4. Chassis FEX to Fabric Interconnect Port Connection Record FEX |  Connected to  
---|---  
Number |  Port |  Fabric Interconnect A or B |  Slot |  Port |  Connection notes  
**1** |  1 |  |  |  |   
2 |  |  |  |   
3 |  |  |  |   
4 |  |  |  |   
5 |  |  |  |   
6 |  |  |  |   
7 |  |  |  |   
8 |  |  |  |   
**2** |  1 |  |  |  |   
2 |  |  |  |   
3 |  |  |  |   
4 |  |  |  |   
5 |  |  |  |   
6 |  |  |  |   
7 |  |  |  |   
8 |  |  |  |   
  
## UCS 6536 Fabric Interconnect Port Connection Record

Table 5.  Port Connection Record Fabric Interconnect  | Connected to   
---|---  
Number  |  Port  |  Slot  |  Port  |  Connection notes   
**1** |  1  |  |  |   
2  |  |  |   
3  |  |  |   
4  |  |  |   
5  |  |  |   
6  |  |  |   
7  |  |  |   
8  |  |  |   
**2** |  1  |  |  |   
2  |  |  |   
3  |  |  |   
4  |  |  |   
5  |  |  |   
6  |  |  |   
7  |  |  |   
8  |  |  | 

---

## Page 12: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x9508/install/m-technical-specs.html

# Technical Specifications  
  
This appendix lists the technical specifications for the Cisco UCS X9508 server chassis.

## KVM Cable

The KVM cable (UCSX-C-DEBUGCBL) provides a connection into a Cisco UCS compute node, providing a DB-9 serial connector, a DB-15 connector, and a USB ports for a keyboard and mouse. With this cable you can create a direct connection to the operating system and the BIOS running on a compute node. 

Figure 1. KVM Cable for Compute Nodes    
![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309412.jpg)  
**1** |  Oculink Connector to compute node |  **2** |  DB-9 serial connector to host Console port  
---|---|---|---  
**3** |  USB connector to connect to single USB 3.0 port (keyboard or mouse) |  **4** |  DB-15 connector to connect to a host VGA monitor   
  
## Chassis Specifications

Figure 2. Chassis Dimensions 

![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309536.jpg)

1 |  Chassis Width: 17.5 in (444.5 mm)  
---|---  
2 |  Total Chassis Length, plus protrusions: 35.8 in (909.32 mm)  
3 |  Chassis Length measured from front rack rail: 33.05 in (839.47 mm)   
4 |  Chassis Length, front face to rear face: 34.8 in (884 mm)  
5 |  Chassis Front Clearance: 1.77 in (44.96 mm) Cable management trays, if used, add 4.5 in (114.3 mm) of length to the chassis.   
6 |  Chassis Height: 12.05 in (306.07 mm)  
Table 1. Chassis Capacities and Metrics Description  |  Specification   
---|---  
Node slots  |  8   
IFM slots  |  2   
XFM slots |  2  
Fan module bays  |  4  
Power supply bays  |  6   
PSU Power  |  2800 W  
Maximum Output |  9554 British Thermal Units (BTUs) per hour  
Table 2. Weight of the Chassis Components Description  |  Specification   
---|---  
Empty chassis  |  92 lbs (41.73 kg)   
IFM  |  8.4 lbs (3.81 kg)   
IFM Filler Panel |  5.8 lbs (2.63 kg)  
Fan module  |  3.4 lbs (1.54 kg)   
PSU  |  4 lbs (1.81 kg)  
Compute Node  |  14.9 to 25 lbs (6.76 to 11.34 kg) depending on hardware options.   
PCIe Node |  12.84 to 17.9 lbs (5.83 kg to 8.12 kg) depending on the quantity and types of GPUs installed.  
Fully Populated UCS X9508 Chassis  |  Approximately 400 lbs (181.43 kg) depending on models and options selected   
1 The system weight listed here is an estimate for a fully configured system and will vary depending on the devices installed. 

## Environmental Specifications

Table 3. Environmental Specifications for the Chassis Description |  Specification  
---|---  
Temperature, operating within altitude: 0 to 10,000 feet (0 to 3,000 meters) |  50 to 95°F (10 to 35°C) (As altitude increases, maximum temperature decreases by 1°C per 300m.) For general information, see the [Cisco Unified Computing System Site Planning Guide: Data Center Power and Cooling](https://www.cisco.com/c/en/us/solutions/collateral/data-center-virtualization/unified-computing/white_paper_c11-680202.pdf).   
Temperature, non-operating within altitude: 0 to 40,000 feet (0 to 12,000 meters) |  –40 to 149°F (–40 to 65°C)  
Humidity (RH), noncondensing |  Operating: 10-90%, 28°C max. wet bulb Nonoperating: 5-93%, 38°C max wet bulb  
Altitude |  Operating – 0 to 10000 feet (0 to 3000 meters) Above 10,000 feet, maximum temperature decreases by 1°C per 1000 feet (~300 meters) above 10,000 feet  Nonoperating – 40,000 ft (12,000 m)  
Sound Pressure Level |  83 dBA—at normal operating temperature.  
  
  * Environmental Conditions and Power Requirement Specifications for Twinax SFP+ Transceivers


### Environmental Conditions and Power Requirement Specifications for Twinax SFP+ Transceivers

Table 4. Environmental Conditions and Power Requirement for the SFP+ Transceiver Parameter |  Symbol |  Min. |  Max. |  Unit  
---|---|---|---|---  
Storage temperature |  TS |  –40 |  85 |  °C  
Case temperature |  TC |  0 |  50 |  °C  
Module supply voltage |  VCCT,R |  3.1 |  3.5 |  V  
  
##  Specifications for the Cisco UCS X9508 Chassis Power Supply Units

Table 5. AC-input Titanium Power Supply (N20-PAC5-2800W) Specifications Description  | Specification   
---|---  
AC-input voltage  |  Voltage Range 100-127 VAC, 200-240 VAC Nominal (range: 90-140 VAC, 180-264 VAC)   
AC-input frequency  |  50 to 60 Hz nominal (range: 47 to 63 Hz)   
Maximum AC-input current  |  18 A @ 90 VAC  18 A @ 180 VAC   
Maximum input VA  |  3200 VA at 230 VAC   
Maximum output power per power supply  |  2800 W @ 200-240 VAC Nominal 1400 W @ 100-127 VAC Nominal   
Maximum inrush current  |  35 A (sub cycle duration)   
Minimum hold up time  |  10 ms @ 1400 W  10 ms @ 2800 W   
Power supply main output voltage  |  54 VDC   
Power supply standby voltage  |  3.4 V   
Efficiency Rating  |  80+ Titanium Certified   
Input connector  |  IEC320 C20  System input power connectors are located in the chassis PEMs, not on the power supply  
  
For information about supported power cords, see Technical Specifications. 

## Supported AC Power Cords and Plugs

The AC power connectors on the chassis PEM use an IEC 320 C20 socket. Each chassis power supply has a separate power cord. The power cord that you use to connect the power supply units to an AC power source will have an IEC 320 C19 plug on one end and on the other end one that conforms to the AC power outlet specifications for your country. See the following table to determine which cord to order for your chassis power supply units. When you determine which power cord you need to order, you can verify that its plugs conform to the power outlets for your facility by clicking on its reference link. 

The jumper power cords, for use in racks, are available as an optional alternative to the standard power cords. The optional jumper power cords have an IEC C19 connector (such as a Cisco RP Series PEM) on the end that plugs into the chassis’ PEM and an IEC C20 connector on the end that plugs into an IEC C19 outlet receptacle. For more information, contact your Cisco Systems representative. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Only the regular power cords or jumper power cords provided with the chassis are supported.

* * *  
  
---|---  
  
  * Australia and New Zealand
  * Continental Europe
  * International
  * Israel
  * Japan and North America
  * Peoples Republic of China
  * Taiwan
  * Switzerland


### Australia and New Zealand

Power Cord Part Number—CAB-AC-16A-AUS

Cord Set Rating—16A, 250 VAC

Figure 3. CAB-AC-16A-AUS Power Cord for the Cisco UCS X9508 Chassis  ![](/c/dam/en/us/td/i/100001-200000/140001-150000/140001-141000/140586.eps/_jcr_content/renditions/140586.jpg)

### Continental Europe

Power Cord Part Number—CAB-AC-2800W-EU

Cord Set Rating—16A, 250 VAC

Figure 4. CAB-AC-2800W-EU Power Cord for the UCS X9508 Chassis  ![](/c/dam/en/us/td/i/100001-200000/110001-120000/113001-114000/113360.eps/_jcr_content/renditions/113360.jpg)

### International

Power Cord Part Number—CAB-AC-2800W-INT

Cord Set Rating—16A, 250 VAC

Figure 5. CAB-AC-2800W-INT Power Cord for the UCS X9508 Chassis  ![](/c/dam/en/us/td/i/100001-200000/110001-120000/113001-114000/113361.eps/_jcr_content/renditions/113361.jpg)

### Israel

Power Cord Part Number—CAB-AC-2800W-ISRL

Cord Set Rating—16A, 250 VAC

Figure 6. CAB-AC-2800W-ISRL Power Cord for the UCS X9508 Chassis  ![](/c/dam/en/us/td/i/100001-200000/130001-140000/130001-131000/130113.eps/_jcr_content/renditions/130113.jpg)

### Japan and North America

#### Non-Locking 200 to 240 VAC operation

Power Cord Part Number—CAB-AC-2800W-US1

Cord Set Rating—16A, 250 VAC

Figure 7. CAB-AC-2800W-US1 Power Cord for the UCS X9508 Chassis  ![](/c/dam/en/us/td/i/100001-200000/110001-120000/113001-114000/113362.ps/_jcr_content/renditions/113362.jpg)

#### Locking 200 to 240 VAC Operation

Power Cord Part Number—CAB-AC-C6K-TWLK

Cord Set Rating—16A, 250 VAC

Figure 8. CAB-AC-C6K-TWLK Power Cord for the UCS X9508 Chassis  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309544.jpg)

### Peoples Republic of China

Power Cord Part Number—CAB-AC-16A-CH

Cord Set Rating—16A, 250 VAC

Figure 9. CAB-AC-16A-CH Power Cord for the Cisco UCSX X9508 Chassis  ![](/c/dam/en/us/td/i/100001-200000/120001-130000/126001-127000/126792.eps/_jcr_content/renditions/126792.jpg)

### Taiwan

Power Cord—CAB-AC-C19-TW

Plug—250 VAC 16 A, C19 

Length—7.5 feet / 2.3 meters

### Switzerland

Power Cord Part Number—CAB-ACS-16

Cord Set Rating—16A, 250 VAC

Figure 10. CAB-ACS-16 Power Cord for the UCS X9508 Chassis  ![](/c/dam/en/us/td/i/100001-200000/190001-200000/192001-193000/192844.eps/_jcr_content/renditions/192844.jpg)

### 

---

## Page 13: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x9508/install/m-ucsx-9508-chassis-overview.html

# Overview

This chapter contains the following topics:

## System Overview 

The Cisco UCS X9508 Server Chassis and its components are part of the Cisco Unified Computing System (UCS). This system can use multiple server chassis configurations along with the Cisco UCS Fabric Interconnects to provide advanced options and capabilities in server and data management. The following configuration options are supported: 

  * All Cisco UCS compute nodes. In a compute node-only configuration, two Intelligent Fabric Modules (IFMs) are required.

  * A mix of Cisco UCS compute nodes and Cisco UCS PCIe Nodes. In this configuration, the compute nodes are paired with Cisco UCS PCIe nodes. 

  * With the Cisco UCS X440p PCIe Node, an M7 generation compute node is paired 1:1.

  * With the Cisco UCS X580p PCIe node, up to two M8 generation compute nodes can be paired with each PCIe node.

  * Two Intelligent Fabric Modules (IFMs) and two Cisco X9416 X-Fabric Modules (XFMs) or Cisco X9516 X-Fabric Modules are required in each UCS X9508 chassis for full performance. 


Either servers or compute nodes, and PCIe nodes are managed through the GUI or API with Cisco Intersight. 

The Cisco UCS X9508 Server Chassis system consists of the following components: 

  * Chassis versions: 

  * Cisco UCS X9508 server chassis–AC version 

  * Intelligent Fabric Modules (IFMs), two deployed as a pair:

  * Cisco UCS 9108 100G IFMs (UCSX-I-9108-100G)—Two I/O modules, each with 8 100 Gigabit QSFP28 optical ports

  * Cisco UCS 9108 25G IFMs (UCSX-I-9108-25G)—Two I/O modules, each with 8 25 Gigabit SFP28 optical ports 

  * X-Fabric Modules:

  * Two UCS X9416 XFMs are required in each UCS X9508 server chassis to support GPU acceleration through Cisco UCS X440p PCIe nodes. 

  * Two UCS X9516 XFMs are required in each UCS X9508 server chassis to support GPU acceleration through Cisco UCS X580p PCIe nodes. 

  * Power supplies—Up to six 2800 Watt, hot-swappable power supplies 

  * Fan modules—Four hot-swappable fan modules 

  * Up to 8 UCS X Series compute nodes of M6 or M7 generation for PCIe Gen4 connectivity through the X9416 XFMs, or up to 8 UCS X series compute nodes of M8 generation for PCIe Gen5 connectivity through the UCS X516 XFMs. 

  * Up to 4 UCS X-Series M6 or M7 compute nodes paired 1:1 with up to 4 Cisco UCS X440p PCIe Nodes and two UCS X9416 XFMs for PCIe Gen4 connectivity. 

  * Up to 4 UCS X-Series M8 compute nodes paired with up to 2 Cisco UCS X580p PCIe Nodes and two UCS X516 XFMs for PCIe Gen5 connectivity. 


The following figures show the server chassis front and back.  Figure 1. Cisco UCS X9508 Server Chassis, Front  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308909.jpg) 1 |  System LEDs:

  * Locator LED/Button
  * System Status LED
  * Network Link LED

For information about System LEDs, see LEDs.  |  2 |  Node Slots, a total of 8. Shown populated with compute nodes, but can also contain PCIe Nodes  
---|---|---|---  
3 |  Power Supplies, a maximum of 6.  |  4 |  System Asset Tag  
5 |  System side panels (two), which are removable. The side panels cover the rack mounting brackets.  |  |   
Figure 2. Cisco UCS X9508 Server Chassis, Rear  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308910.jpg) 1 |  Power Entry Modules (PEMs) for facility inlet power Each PEM contains 3 IEC 320 C20 inlets. 

  * PEM 1 is at the top of the chassis, and it supports IEC inlets 1 through 3, with inlet 1 at the top of PEM 1.
  * PEM 2 is at the bottom of chassis, and it supports IEC inlets 4 through 6, with inlet 4 at the top of PEM 2

|  2 |  Intelligent Fabric Modules (shown populated), which are always deployed as a pair of the following:

  * Cisco UCS 9108 100G modules
  * Cisco UCS 9108 25G modules

  
---|---|---|---  
3 |  System fans (four)  |  4 |  X-Fabric Module slots for either UCS active filler panels (for compute nodes) or up to two UCS X-Fabric Modules (for compute nodes paired with PCIe nodes).   
  
## Features and Benefits

The Cisco UCS X9508 server chassis revolutionizes the use and deployment of compute-node and PCIe-node based systems. By incorporating unified fabric, cloud native management, and X-Fabric technology, the Cisco Unified Computing System enables the chassis to have fewer physical components, no independent management, and to be more energy efficient than traditional blade server chassis. 

This simplicity eliminates the need for dedicated chassis management and blade switches, reduces cabling, and enables the Cisco Unified Computing System to scale to 20 chassis without adding complexity. The Cisco UCS X9508 server chassis is a critical component in delivering the Cisco Unified Computing System benefits of data center simplicity and IT responsiveness. 

Table 1. Features and Benefits Feature  |  Benefit   
---|---  
Management by Cisco Intersight  |  Reduces total cost of ownership by removing management modules from the chassis, making the chassis stateless.  Provides a single, highly available cloud-based management tool for all server chassis, IFMs, XFMs, and nodes, thus reducing administrative tasks.   
Unified fabric  |  Decreases TCO by reducing the number of network interface cards (NICs), host bus adapters (HBAs), switches, and cables needed.   
Support for two UCS I/O Modules  |  Eliminates switches from the chassis, including the complex configuration and management of those switches, allowing a system to scale without adding complexity and cost.  Allows use of two I/O modules for redundancy or aggregation of bandwidth.   
Auto discovery  |  Requires no configuration; like all components in the Cisco Unified Computing System, chassis are automatically recognized and configured by Cisco Intersight.   
Direct node to fabric connectivity |  Provides reconfigurable chassis to accommodate a variety of form factors and functions, which supports investment protection for new fabrics and future compute and PCIe nodes.  Provides IFM-to-compute node connectivity to chassis through an Ortho-Direct connection.  Provides 8 nodes with 200 Gbps (dual 25G-PAM4-ETH x8 lanes) of available Ethernet fabric throughput for each compute node. The system is designed to support higher potential Ethernet fabric throughput for future and emerging technologies, such as 112 GbpsPAM4 Ethernet.  Provides 8 nodes with 200 Gbps (dual 16G-PCIe x 16 lanes) of available PCIe fabric throughput for each compute node. The system is designed to support higher potential Ethernet fabric throughput for future and emerging technologies, such as 32 Gbps PCIe Gen5.   
Redundant hot swappable power supplies and fans  |  Provides high availability in multiple configurations.  Increases serviceability.  Provides uninterrupted service during maintenance.  Available configured for AC environments (mixing not supported)   
Hot-pluggable compute nodes and intelligent fabric modules  |  Provides uninterrupted service during maintenance and server deployment.   
Comprehensive monitoring  |  Provides extensive environmental monitoring on each chassis  Allows use of user thresholds to optimize environmental management of the chassis.   
Efficient front-to-back airflow  |  Helps reduce power consumption and increase component reliability.   
Tool-free installation  |  Requires no specialized tools for chassis installation.  Provides mounting rails for easy installation and servicing.   
Node configurations  |  Allows up to 8 UCS compute nodes or up to 4 compute nodes paired with either 4 UCS X440p PCIe Nodes (Gen4 support) or two UCS X580p PCIe Nodes (Gen 5 support)   
  
## Chassis Components

This section lists an overview of chassis components.

  * Cisco UCS X9508 Server Chassis


### Cisco UCS X9508 Server Chassis

The Cisco UCS X9508 Series server chassis is a scalable and flexible chassis for today’s and tomorrow’s data center that helps reduce total cost of ownership. 

The chassis is seven rack units (7 RU) high and can mount in an industry-standard 19-inch rack with square holes for use with cage nuts or round-holes for use with spring nuts. The chassis can house up to eight Cisco UCS nodes. 

Up to six hot-swappable AC power supplies are accessible from the front of the chassis. These power supplies can be configured to support nonredundant, N+1 redundant, N+2 redundant, and grid-redundant configurations. The rear of the chassis contains four hot-swappable fans, six power connectors (one per power supply), two horizontal top slots for Intelligent Fabric Modules (IFM1, IFM2), and two additional horizontal bottom slots for X-Fabric modules (XFM1, XFM2). 

Scalability is dependent on both hardware and software. For more information, see the appropriate [UCS software release notes](http://www.cisco.com/en/US/products/ps10281/prod_release_notes_list.html). 

## Compute Nodes

The Cisco UCS X Series compute nodes are based on industry-standard server technologies and provide the following: 

  * Up to two Intel multi-core processors

  * Front-accessible, hot-swappable NVMe drives or solid-state disk (SSD) drives 

  * Depending on the compute node, support is available for up to two adapter card connections for up to 200 Gbps of redundant I/O throughput 

  * Industry-standard double-data-rate 4 (DDR4) memory (M6 and M7 compute nodes) or DDR5 memory (M8 compute nodes)

  * Remote management through an integrated service processor that also executes policy established in Cisco Intersight cloud-based server management 

  * Local keyboard, video, and mouse (KVM) and serial console access through a front console port on each compute node 


  * Cisco UCS X210c M6 Compute Node
  * Cisco UCS X210c M7 Compute Nodes
  * Cisco UCS X410c M7 Compute Nodes
  * Cisco UCS X440p PCIe Nodes
  * Cisco UCS X210c M8 Compute Nodes
  * Cisco UCS X215c M8 Compute Nodes
  * Cisco UCS X580p PCIe Nodes


### Cisco UCS X210c M6 Compute Node

The Cisco UCS X210c M6 is a two-socket compute node that hosts a maximum of two M6 CPUs. This compute node is supported in the Cisco UCS X9508 server chassis, which provides power and cooling. Data interconnect for the compute node to other data center equipment is supported through Intelligent Fabric Modules in the same server chassis. 

Each Cisco UCS X210c M6 compute node has Cisco-standard indicators on the face of the module. Indicators are grouped for module-level information, and drive-level indicators. 

Figure 3. Cisco UCS X210c M6 Compute Node  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308977.jpg)

### Cisco UCS X210c M7 Compute Nodes

The Cisco UCS X210c M7 Compute Node is the computing device to integrate into the Cisco UCS X-Series Modular System. Up to eight compute nodes can reside in the 7-Rack-Unit (7RU) Cisco UCS X9508 Chassis, offering one of the highest densities of compute, IO, and storage per rack unit in the industry. 

The Cisco UCS X210c M7 Compute Node harnesses the power of up to two 5th Generation Intel® Xeon® Scalable Processors with up to 64 cores per processor or up to 2x 4th Generation Intel® Xeon® Scalable Processors with up to 60 cores per processor. 

The compute node supports up to 6 hot-pluggable, Solid-State Drives (SSDs), or Non-Volatile Memory Express (NVMe 2.5-inch drives with a choice of enterprise-class RAID or pass-through controllers with four lanes each of PCIe Gen 4 connectivity and up to 2 M.2 SATA or NVMe drives for flexible boot and local storage capabilities. This option is shown in the illustration below. 

To support customization for your deployment, the Cisco UCS X210c M7 Compute Nodes offers an optional PCIe Gen 4 front mezzanine module with support for up to two U.2 or U.3 NVMe drives and two GPUs. 

![](/c/dam/en/us/td/i/400001-500000/490001-500000/493001-494000/493166.jpg)

For more information, see the [Cisco UCS X210c M7 Compute Node Installation and Service Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x210c-m7/install/b-cisco-ucs-x210c-m7-install-guide.html). 

### Cisco UCS X410c M7 Compute Nodes

The Cisco UCS X410c M7 Compute Node (UCSX-410C-M7) is a two-slot compute node that supports four CPU sockets for 4th Generation Intel® Xeon® Scalable Processors, offering robust processing capabilities, extensive memory, flexible storage, and advanced networking options to meet the demands of diverse and evolving IT requirements. 

Each compute node consists of two distinct subnodes, a primary and a secondary. 

  * The primary contains two CPUs (1 and 2), two heatsinks, and half of the DIMMs. All additional hardware components and supported functionality are supported through the primary, including the front and rear mezzanine hardware options, rear mezzanine bridge card, front panel, KVM, management console, and status LEDs. 

  * The secondary contains two additional CPUs (3 and 4), two heatsinks, and the other half of the DIMMs. 


The primary node can support a front storage module, which supports multiple different storage device configurations: 

  * All SAS/SATA configuration consisting of up to six SAS/SATA SSDs with an integrated RAID controller (HWRAID) in slots 1 through 6\. 

  * All NVMe configuration consisting of up to six U.2 NVMe Gen4 (x4 PCIe) SSDs in slots 1 through 6.

  * A mixed storage configuration consisting of up to six SAS/SATA or up to four NVMe drives is supported. In this configuration, U.2 NVMe drives are supported in slots 1 through 4 only. U.3 NVMe drives can be used in slots 1 through 6. 


For more information, see the [Cisco UCS X410c M7 Compute Node Installation and Service Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x410c-m7/install/b-cisco-ucs-x410c-m7-install-guide.html). 

### Cisco UCS X440p PCIe Nodes

The Cisco UCS X440p Gen4 PCIe Node is a modular node that can be paired 1:1 with a Cisco UCS X-Series M7 Compute Node in the UCS X9508 chassis to provide GPU-accelerator support using the UCS X9416 X-Fabric modules in the same chassis. 

Each Cisco UCS X440p PCIe Node supports up to four of the supported FHFL GPUs to a Cisco UCS X-Series M7 Compute Node. This PCIe node supports PCIE Gen4 connectivity. 

![](/c/dam/en/us/td/i/400001-500000/490001-500000/494001-495000/494025.jpg)

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

A single Cisco UCS X9508 chassis cannot support a mix of different PCIe nodes, so if the same server chassis contains Cisco UCS X440p PCIe Nodes, it cannot contain Cisco UCS X580p PCIe Nodes. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The compute node paired with the X440p PCIe Node must be a Cisco M7 X-Series Compute Node.  For more information, see the [Cisco UCS X440p PCIe Node Installation and Service Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x440p/install/b-cisco-ucs-x440p-gen4-pcie-install-guide.html). 

* * *  
  
---|---  
  
### Cisco UCS X210c M8 Compute Nodes

The Cisco UCS X210c M8 Compute Node is the third generation of compute node to integrate into the Cisco UCS X-Series Modular System. It delivers performance, flexibility, and optimization for deployments in data centers, and at remote sites. 

The Cisco UCS X210c M8 Compute Node is a single-slot compute node that has two CPU sockets that can support Sixth Generation Intel Xeon Scalable Server Processors. 

Additionally, each compute node supports a front storage module offers the following different storage device configurations: 

  * Up to six SAS/SATA NVMe SSDs with an integrated RAID controller.

  * Up to six NVMe SSDs in slots 1 through 6.

  * A mixture of up to six SATA/SATA or up to four NVMe drives is supported. In this configuration, U.3 NVMe drives in slots 1 through 6. The U.3 NVMe drives are also supported with an integrated RAID module (MRAID Controller, UCSX-RAID-M1L6) and Compute RAID Controller (UCSX-X10C-RAIDF). 

  * Up to nine hot-pluggable EDSFF E3.S NVMe drives with a passthrough front mezzanine controller option.

  * With an integrated RAID module, the following drive configurations are supported:

  * SAS/SATA drives in slots 1 through 6

  * NMVe U.3 drives in slots 1 through 6

  * A mix of NVMe U.3 and SAS/SATA drives. SAS/SATA and NVMe U.3 drives are supported in on Slots 1 through 6


For more information, see the [Cisco UCS X210c M8 Compute Node Installation and Service Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x210c-m8/install/b-x210c-m8-install.html). 

### Cisco UCS X215c M8 Compute Nodes

The Cisco UCS X215c M8 is a single-slot compute node that has two CPU sockets that can support a maximum of one Fourth Gen AMD EPYC™ Processors with up to 96 cores per processor and up to 384 MB of Level 3 cache per CPU or Fifth Gen AMD EPYC™ Processors with up to 196 cores per processor and up to 384 MB of Level 3 cache per CPU. The minimum system configuration requires one CPU installed in the CPU1 slot. 

Additionally, each compute node has a front mezzanine modules the offers the following:

  * A front storage module, which supports multiple different storage device configurations: 

  * Up to six hot pluggable SAS/SATA/U.3 NVMe 2.5inch SSDs (slots 1-6).

  * SATA/SAS/U.3 drives can co-exist on the front mezzanine module. RAID volumes are restricted to same type of drives only. For example, RAID 1 volume need to use a set of SATA or SAS or U.3 NVMe drives. 


![](/c/dam/en/us/td/i/400001-500000/490001-500000/494001-495000/494024.jpg)

For more information, see the [Cisco UCS X215c M8 Compute Node Installation and Service Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x215c-m8/install/b-cisco-ucs-x215c-m8-install.html). 

### Cisco UCS X580p PCIe Nodes

The Cisco UCS X580p PCIe Node delivers high-performance GPU support with associated Cisco UCS X-Series M8 Compute nodes through UCS X9516 X-Fabric Modules in the same chassis. 

Each Cisco UCS X580p PCIe node is a dual-slot node that supports up to four FHFL PCIe GPUs and can be paired with the Cisco UCS X210c M8 Compute Node with Intel® Xeon® 6 processors, as well as the UCS X215c M8 compute node with EPYC processors. This node offers significantly greater flexibility than the Cisco UCS X440p PCIe Node, allowing users to associate up to four GPUs with up to two Cisco UCS M8 X-Series Compute Nodes. This node supports PCIe Gen 5 connectivity. 

![](/c/dam/en/us/td/i/400001-500000/490001-500000/494001-495000/494026.jpg)

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

A single Cisco UCS X9508 chassis cannot support a mix of different PCIe nodes, so if the same server chassis contains Cisco UCS X580p PCIe Nodes, it cannot contain Cisco UCS X440p PCIe Nodes. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The compute nodes associated with the X580p PCIe Node must be a Cisco M8 X-Series Compute Nodes.  For more information, see the [Cisco UCS X580p PCIe Node Installation and Service Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x580p/install/b-cisco-ucs-x580p-gen5-pcie-install-guide.html). 

* * *  
  
---|---  
  
## Intelligent Fabric Modules

The Cisco UCS X9508 contains Intelligent Fabric Modules (IFMs) on the rear of the server chassis. IFMs have multiple functions in the server chassis: 

  * Data traffic: IFMs support network-level communication for traditional LAN and SAN traffic as well as aggregating and disaggregating traffic to and from individual compute nodes. 

  * Chassis health: IFMs monitor common equipment in the server chassis, such as fan units, power supplies, environmental data, LED status panel, and so on. Management functions for the common equipment is supported through IFMs. 

  * Compute Node health: IFMs monitor Keyboard-Video-Mouse (KVM) data, Serial over LAN (SoL) data, and IPMI data for the compute nodes in the chassis, as well as provide management of these features. 


IFMs must always be deployed in pairs to provide redundancy and failover to safeguard system operation. 

  * Cisco UCS 9108 25G Intelligent Fabric Module
  * Cisco UCS 9108 100G Fabric Module


### Cisco UCS 9108 25G Intelligent Fabric Module

The Cisco UCS 9108 Intelligent Fabric Module (UCSX-I-9108-25G) is an IFM that supports aggregate data throughput of 2TB/s through two groups of four optical ports. 

Figure 4. UCS 9108 25 Gbps Intelligent Fabric Module, Faceplate View  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308980.jpg) 1 |  Status LEDs:

  * IFM Status (top LED)
  * Fan Status LEDs 1 through 3, with Fan 1 as LED 2, Fan 2 as LED 3, and Fan 3 as LED 4. 

|  2 |  IFM Reset Button  
---|---|---|---  
3 |  SFP28 Optical Ports Ports are arranged in two groups of four physical ports:

  * Ports are in groups of four. Port number 1 is the left port in this group, and port number 4 is the right port in the group. 
  * Ports are in groups of four. Port number 5 is the left port in this group, and port number 8 is the right port in the group. 

|  4 |  IFM Ejector Handles, left and right  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For information about removing and installing the IFM's components, see [Cisco UCS 9108 25G IFM Field Replaceable Unit Replacement Instructions](m-ifm-afm-xfm-fru-replacement-instructions-labels.html#cisco-ucs-9108-25g-ifm-field-replaceable-unit-instructions). 

* * *  
  
---|---  
  
### Cisco UCS 9108 100G Fabric Module

The Cisco UCS 9108 Intelligent Fabric Module (UCSX-I-9108-100G) is an IFM that supports data throughput of 100G through two groups of 4 ports. 

Figure 5. UCS 9108 100 Gbps Intelligent Fabric Module, Faceplate View  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308981.jpg) 1 |  Status LEDs:

  * IFM Status (top LED)
  * Fan Status LEDs 1 through 3, with Fan 1 as LED 2, Fan 2 as LED 3, and Fan 3 as LED 4. 

|  2 |  IFM Reset Button  
---|---|---|---  
3 |  QSFP28 Optical Ports.  Ports are arranged in two groups of four physical ports. Ports are stacked in vertical pairs, with two ports in each vertical port stack. 

  * Port number 1 is the top port in the left port pair in the first port group, and port number 3 is the top port of the right port pair in the group. 
  * Port number 5 is the top port in the left port pair of the second group, and port number 7 is the top port in the right port pair of the group. 

|  4 |  IFM Ejector Handles, left and right  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For information about removing and installing the IFM's components, see [Cisco UCS 9108 100G IFM Field Replaceable Unit Replacement Instructions](m-ifm-afm-xfm-fru-replacement-instructions-labels.html#cisco-ucs-9108-100g-intelligent-fabric-module-field-replacement-unit-instructions). 

* * *  
  
---|---  
  
## X-Fabric Modules

The Cisco UCS X9508 server chassis supports Cisco X-Fabric Modules, including the Cisco UCS X9416 X-Fabric Module and Cisco UCS X9516 X-Fabric Modules (XFMs). 

The module is a configuration option:

  * The UCS X9416 X-Fabric Modules are required when the server chassis contains the Cisco UCS X440p PCIe node.

  * The UCS X9516 X-Fabric Modules are required when the server chassis contains the Cisco UCS X580p PCIe node.

  * The X-Fabric module is not required if your server chassis contains only Cisco UCS X-Series compute nodes, such as the Cisco UCS X210c. 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Although Cisco UCS X-Fabric Modules can be removed, the best practice is to leave them installed even during installation. If your Cisco UCS X9508 server is configured so that no XFMs are installed, only XFM blanks, leave the blanks installed also, even during chassis installation. 

* * *  
  
---|---  
  
X-Fabric Modules are always deployed in pairs to support GPU acceleration through the Cisco UCS X440p PCIe nodes (Gen4 support) or Cisco UCS X580p PCIe nodes (Gen5 support). Therefore, two PCIe modules must be installed in a server chassis that contains any number of PCIe nodes. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Do not operate the server chassis with the XFM slots empty!

* * *  
  
---|---  
  
Each server chassis supports two UCS X9416 modules, which are located in the two horizontal module slots at the bottom of the chassis rear. 

![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540739.jpg)

1 |  XFM slot 1 (XFM1) |  Provides PCIe connectivity to all module slots 1 through 8 |   
---|---|---|---  
2 |  XFM slot 2 (XFM2) |  Provides PCIe connectivity to all module slots 1 through 8 |   
  
For additional information, see the following topics:

  * Cisco UCS X9416 Fabric Module

  * Cisco UCS X9516 Fabric Module

  * Cisco UCS X-Fabric Module Blanks


  * Cisco UCS X9416 Fabric Module
  * Cisco UCS X9516 Fabric Module
  * Cisco UCS X-Fabric Module Blanks


### Cisco UCS X9416 Fabric Module

The Cisco UCS X9416 module is a Cisco X-Fabric Module (XFM) that provides PCIe connectivity for module slots one through eight on the front of the server chassis. Each X-Fabric Module is installed in the bottom two slots of the rear of the Cisco UCS X9508 server chassis. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Although the Cisco UCS X9416 Fabric Modules can be removed, the best practice is to leave them installed even during chassis installation. 

* * *  
  
---|---  
  
Each module provides:

  * Integrated, hot-swappable active fans for optimal cooling

  * PCIe x16 connectivity and signaling between pairs of compute nodes and GPU modules, such as the Cisco X440p PCIe node


Each module has STATUS LEDs to visually indicate operational status the X-Fabric module and its fans. 

![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540441.jpg)

1 |  Status LEDs:

  * Module Status (top LED)
  * Fan Status LEDs 1 through 3, with Fan 1 as LED 2, Fan 2 as LED 3, and Fan 3 as LED 4. 

|  2 |  Module Ejector Handles, Left and Right  
---|---|---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For information about removing and installing the XFM's components, see [Cisco UCS X9416 X-Fabric Module Field Replaceable Unit Replacement Instructions](m-ifm-afm-xfm-fru-replacement-instructions-labels.html#cisco-ucs-x9416-x-fabric-module-field-replaceable-unit-replacement-instructions). 

* * *  
  
---|---  
  
### Cisco UCS X9516 Fabric Module

The Cisco UCS X9516 (UCSX-FS-9516) is a Cisco X-Fabric Module (XFM) that provides PCIe Gen 5 connectivity for module slots one through eight on the front of the server chassis. A total of two of these modules is required. 

Each X-Fabric Module is installed in the bottom two slots of the rear of the Cisco UCS X9508 server chassis.

Each module provides:

  * Integrated, hot-swappable active fans for optimal cooling

  * PCIe x16 connectivity and signaling between pairs of compute nodes and GPU modules, such as the available M8 series of Cisco UCS X Series Compute Nodes and the Cisco UCS X580p PCIe Node. Additional information about these products is available through the Cisco website. 


Each Cisco UCS X9516 X-Fabric Module features:

  * Two PCIe cages (numbered 1 and 2) that accept PCI cards to offer flexibility for your deployment. The XFM faceplate has identifiers for each slot at the upper left corner of the cage. For information about the supported Gen5 PCIe cards, see Cisco UCS X9516 Supported PCIe Cards. 

  * Connectivity and operational information available through the LED cluster at the left edge of the XFM. 

  * Ejector handles for tool-less installation and removal from the rear panel of the Cisco UCS X9508 server chassis that contains the XFMs. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Although the Cisco UCS X9516 Fabric Modules can be removed, the best practice is to leave them installed even during chassis installation. 

* * *  
  
---|---  

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The following illustration shows the XFM populated with PCIe cards. Filler blanks are available. If the XFM will not contain any PCIe cards, each unused card slot must be covered with a filler blank. 

* * *  
  
---|---  
  
![](/c/dam/en/us/td/i/400001-500000/490001-500000/490001-491000/490995.jpg)

**1** |  Status LEDs:

  * Module Status (top LED)
  * Fan Status LEDs 1 through 3, with Fan 1 as LED 2, Fan 2 as LED 3, and Fan 3 as LED 4. 

|  **2** |  PCIe Cage 2  
---|---|---|---  
**3** |  PCIe Card Slot 2 Supports one Gen5 x16 card |  **4** |  PCIe Card Slot 1 Supports one Gen5 x16 card  
**5** |  PCIe Cage 1 |  **6** |  Module ejectors, two One on the left of the module and one on the right  
**7** |  Module Ejector Handles, two One per ejector, left and right |  **-** |   
  
  * Cisco UCS X9516 Supported PCIe Cards


#### Cisco UCS X9516 Supported PCIe Cards

The UCS X9516 Fabric Modules offer customizable PCIe connectivity through two PCIe cages. Each cage can accept one of the following third-party PCIe Gen 5 x16 NICs for a total of two NICs per XFM: 

  * NVIDIA ConnectX®-7 200/400G Network Adapter cards


### Cisco UCS X-Fabric Module Blanks

The Cisco UCSX-9508-RBLK is Cisco UCS X-Fabric Module Blank slot which is used for providing future X-Fabric connectivity. Currently this module blank has active fans to facilitate airflow, and it is often called the Active Fan Module (AFM). 

In a typical configuration, this module blank can be installed in either of the two bottom slots in the rear of the chassis below the IFM slots. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

If your Cisco UCS X9508 server is configured so that no XFMs are installed, only XFM blanks, leave the blanks installed even during chassis installation. 

* * *  
  
---|---  
Figure 6. UCS X9508 Rear Module Blank (AFM), Faceplate View  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308982.jpg) 1 |  Status LEDs:

  * Module Status (top LED)
  * Fan Status LEDs 1 through 3, with Fan 1 as LED 2, Fan 2 as LED 3, and Fan 3 as LED 4. 

|  2 |  Module Ejector Handles, Left and Right  
---|---|---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For information about removing and installing the XFM's components, see [Cisco UCS 9508 Active Fan Module (AFM) Field Replaceable Unit Replacement Instructions](m-ifm-afm-xfm-fru-replacement-instructions-labels.html#Blankfield_Installation). 

* * *  
  
---|---  
  
## Fan Modules

The chassis contains four, 100 mm fan modules (UCSX-9508-FAN=), with the minimum configuration of 4 fan modules for optimal cooling. Fans draw air in through the front of the chassis (the cool aisle) and exhaust air through the back of the chassis (the hot aisle) 

Fans are located in the middle of the server chassis rear panel. Fans are numbered one to four starting with the leftmost fan. 

Figure 7. Fan Module  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308851.jpg) ![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Additional 40 mm fan modules are equipped on the Intelligent Fabric Modules and X-Fabric Modules installed in the chassis. These fans (UCSX-RSFAN=) are not interchangeable with the chassis fans. 

* * *  
  
---|---  
  
## Power Supplies

The chassis supports up to 6 AC power supplies (PSUs), with the minimum configuration of 2 PSUs required. They are Titanium certified 2800W capable AC Power Supply Units (PSUs) that support input power from AC sources. 

PSUs are redundant and load-sharing and can be used in the following power modes:

  * N+1 power supply configuration, where N is the number of power supplies required to support system power requirements

  * N+2 power supply configuration, where N is the number of power supplies required to support system power requirements

  * Grid configuration, which is also known as N+N power supply configuration, in which N is the amount of power supplies required to support the system power requirements. 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The chassis requires a minimum of two PSUs to operate.

* * *  
  
---|---  
Figure 8. AC Power Supply  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308931.jpg)

To determine the number of power supplies needed for a given configuration, use the [Cisco UCS Power Calculator](https://mainstayadvisor.com/Go/Cisco/Cisco-UCS-Power-Calculator.aspx) tool. 

  * LEDs
  * Buttons
  * Connectors
  * Power Supply Configuration


### LEDs

One LED indicates power connection presence, power supply operation, and fault states. See Interpreting LEDs for details. 

### Buttons

There are no buttons on a power supply.

### Connectors

The AC power connections are at the rear of the chassis on the Power Entry Module (PEM) to support AC input from the facility. The chassis has two PEMs (PEM 1 and PEM 2), and each supports 3 power supplies. 

  * PEM 1 supports PSUs 1, 2, and 3.

  * PEM 2 supports PSUs 4, 5, and 6. 


Each of the six hot-swappable power supplies is accessible from the front of the chassis. These power supplies are Titanium efficiency, and they can be configured to support non-redundant, N+1 redundant, N+2 redundant, and grid-redundant configurations. 

### Power Supply Configuration

When considering power supply configuration, you need to take several things into consideration: 

  * AC power supplies are all single phase and have a single input for connectivity to its respective PEM. The customer power source (a rack PDU or equivalent) connects input power directly to the chassis power entry module (PEM), not the actual AC power supplies. 

  * The number of power supplies required to power a chassis varies depending on the following factors: 

  * The total "Maximum Draw" required to power all the components configured within that chassis—such as intelligent fabric modules (IFMs), fans, compute nodes (CPU and memory configuration of the compute nodes). 

  * The Desired Power configuration for the chassis. The chassis supports non-redundant power supply configuration, N+1 power supply configuration, N+2 power supply configuration, and grid power supply configuration, which is also known as N+N redundancy. The system also supports an Extended Power mode. 

  * The load is balanced across all active power supplies excluding power supplies in the standby mode.

  * When connecting the chassis to facility power, make sure not to overload the capacity of a PDU or power strip, for example, by connecting all PSUs to one PDU or power strip that is not capable of carrying the total power draw of the chassis. 


  * Power Save Mode
  * Extended Power Mode
  * Non-Redundant Mode
  * N+1 Power Supply Configuration
  * N+2 Power Supply Configuration
  * Grid Configuration


#### Power Save Mode

If the Power Save mode is enabled in the Power policy of the Chassis Profile, power supplies that are not needed to meet the current power demand will be placed into standby mode and will not share the power load. Power supplies required to maintain power supply redundancy will remain active and will not enter standby. Power supplies in standby mode will automatically turn on if the power demand increases or if there is a failure in an active power supply. 

#### Extended Power Mode

The Cisco UCS X9508 Server Chassis supports an Extended Power mode that allows the chassis to utilize an additional 15% of the redundant power reserve. If a power supply fails, the extended power from that failed supply is lost. In response, the chassis limits power consumption to the remaining extended power available from the other redundant power supplies. If no redundant power supplies remain, the chassis limits power to the non-extended power value. 

To protect the system from power faults, the chassis includes a hardware mechanism known as the "emergency brake". The "emergency brake" activates if the actual power demand exceeds the non-extended power limit, and it limits power consumption faster than the remaining PSUs can reach an over-current state or cause a power distribution unit (PDU) breaker to trip. Once the power demand falls below the limit, the emergency brake is released, and normal server throttling is used to maintain power under the cap. 

#### Non-Redundant Mode

In non-redundant mode, the system may go down with the loss of any supply or power grid associated with any particular chassis. We do not recommend operating the system in non-redundant mode in a production environment. 

To operate in non-redundant mode, each chassis should have at least two power supplies installed. The supplies that are placed into standby depends on the installation order (not on the slot number). The load is balanced across active power supplies, not including any supplies in standby. 

The chassis requires a minimum of 2 power supplies. In cases of low-line operation, the total available power is 1400W each for a total of 2800W. Do not attempt to run the chassis on less than the minimum number of power supplies. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

In a non-redundant system, power supplies can be in any slot. Installing less than the required number of power supplies results in undesired behavior such as compute node shutdown. Installing more than the required amount of power supplies may result in lower power supply efficiency. At a minimum, this mode will require two power supplies. 

* * *  
  
---|---  
  
  * Consideration for Non-Redundant Power Mode


##### Consideration for Non-Redundant Power Mode

When the chassis is configured for non-redundant power mode, any PSUs you select can be put into standby mode. In this mode, the PSUs do not actively supply power. Instead, the PSUs are online standbys. For more information about non-redundant power mode, see Non-Redundant Mode. 

When the chassis is in non-redundant power mode and multiple PSUs are installed, through Intersight you can configure the server chassis for **Power Save Mode**. In this mode, any unused PSUs are put into standby mode. They are not actively providing power. 

In non-redundant mode and when **Power Save Mode** is enabled, the server chassis can have one or more active PSUs and one or more standby PSUs. In this configuration, if all active PSUs fail either simultaneously or almost simultaneously, a timing issue can prevent the server chassis from having sufficient time to activate the standby PSUs. As a result, the server chassis may experience a brownout condition. 

  * You can avoid this consideration by not enabling **Power Save Mode**. 

  * You can recover from this consideration by power cycling or rebooting the server chassis. If PSUs are powered cycled, the chassis automatically power cycles. Based on the settings in the Server Profiles for the installed servers or compute nodes, servers might or might not power on. Based on the number of servers that power on, the brownout condition can be cleared. 


#### N+1 Power Supply Configuration

In an N+1 configuration, the chassis contains a total number of power supplies to satisfy system power requirements, plus one additional power supply for redundancy. Any additional power supplies may be placed into Standby mode, if the Standby mode is enabled in the Power Policy of the Chassis Profile. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

In an N+1 configuration, a maximum power of 14kW is delivered with five PSUs configured as Active while the remaining one PSU is in standby mode. The 14kW maximum delivered power is only possible at high input voltage range (200-240VAC). In low input voltage range (100-127VAC nominal), the maximum delivered power would be 7kW. 

* * *  
  
---|---  
  
If one Active power supply should fail, the surviving supplies can provide power to the chassis, until the Standby power supply can be switched to Active status. In addition, Cisco Intersight turns on any "turned-off" power supplies to bring the system back to N+1 status. The system will continue to operate, giving you a chance to replace the failed power supply. 

#### N+2 Power Supply Configuration

In an N+2 configuration, the chassis contains a total number of power supplies to satisfy system power requirements, plus two additional power supplies for redundancy. Any additional power supplies may be placed into Standby mode, if the Standby mode is enabled in the Power Policy of the Chassis Profile. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

In N+2 redundant mode, a maximum power load of 11.2KW is supported with four active modules. The 11.2KW maximum power load is only possible at high input voltage range (200-240VAC). In low input voltage range (100-127VAC nominal), the maximum delivered power would be 5.6KW. 

* * *  
  
---|---  
  
If one or two power supplies should fail, the surviving supplies can provide power to the chassis. In addition, the Cisco Intersight interface supports turning on any "turned-off" power supplies to bring the system back to N+2 status. 

#### Grid Configuration

With grid power configuration (also called N+N redundancy), each set of three PSUs has its own input power circuit, so each set of PSUs is isolated from any failures that might affect the other set of PSUs. If one input power source fails, causing a loss of power to three power supplies, the surviving power supplies on the other power circuit continue to provide power to the chassis. The two power sources in the chassis are defined by the Power Entry Module (PEM) boundaries: PEM1 corresponds to source 1 and connects to power supplies 1-3, while PEM2 corresponds to source 2 and connects to power supplies 4-6. For Grid mode operation, it is required to have an even number of power supplies that are equally distributed across these two PEMs. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Grid redundant mode requires the chassis load to be limited to 8.4kW for high input voltage range (200-240VAC) and 4.2kW for low input power range for a maximum grid configuration (3+3). For a 2+2 minimum configuration, the chassis load is limited to 5.6kW for high line input voltage and 2.8kW for low line input voltage.  If Extended Power Mode is enabled in the Power policy of the Cisco UCS X9508 Chassis Profile, the power limit is increased by 15%. Specifically: 

  * For a 6 PSU configuration in Grid mode, the normal power limit is 8400W. With Extended Power Mode enabled, this limit increases to 9660W total, which corresponds to 1610W per PSU or 4830W per power grid (PEM) under high line/low line conditions. 
  * For a 4 PSU configuration, the power limit increases to 6440W total (3220W per power grid).


* * *  
  
---|---  
  
Grid redundant mode is configured when:

  * all six PSUs are in Active mode to provide power

  * two sets of three PSUs are each connected to separate facility input power sources, including separate cabling for each set 

  * For grid redundant mode, the total number of PSUs should always be divided equally. So, a grid power configuration supports 3+3 (maximum configuration per input power source) or 2+2 (minimum configuration per power input source). 


The grid power configuration is primarily used when you have two separate facility input power sources available to a chassis. A common reason for using this power supply configuration is if the rack power distribution is such that power is provided by two PDUs and you want redundant protection in the case of a PDU failure or to allow continued operation during power facilities maintenance. 

## LEDs

LEDs on both the chassis and the modules installed within the chassis identify operational states, both separately and in combination with other LEDs. 

  * LED Locations
  * Interpreting LEDs


### LED Locations

The UCS X9508 server chassis uses LEDs to indicate power, status, location/identification. Other LEDs on IFMs, PSUs, fans, and compute nodes indicate status information for those elements of the system. 

Figure 9. LEDs on a Cisco UCS X9508 Server Chassis—Front View  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308956.jpg) Figure 10. LEDs on the Cisco UCS X9508 Server Chassis—Rear View  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308957.jpg)

### Interpreting LEDs

Table 2. Chassis, System Fans, and Power Supply LEDs LED  |  Color  |  Description   
---|---|---  
Locator  LED and button (callout 1 on the chassis front panel) ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309096.jpg) |  Off  |  Locator not enabled.   
Blue  |  Locates a selected chassis You can initiate beaconing in UCS Intersight or with the button, which toggles the LED on and off.   
Network Status  (callout 1 on the chassis front panel)![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309098.jpg) |  Off  |  Network link state undefined.  
Solid Green  |  Network link state established on at least one IFM, but no traffic detected.   
Blinking Green  |  Network traffic detected on at least one IFM.   
System Status (callout 1 on the chassis front panel)![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309097.jpg) |  Solid amber  |  Chassis is in a degraded operational state. For example:

  * Power Supply Redundancy Lost
  * Mismatched Processors
  * 1 on N Processors Faulty
  * Memory RAS Failure
  * Failed Storage Drive/SSD

  
Solid Green |  Normal operating condition.  
Blinking Amber |  Chassis is in a critical error state. For example:

  * Boot Failure
  * Fatal Processor and/or bus error detected
  * Loss of both I/O Modules
  * Over Temperature Condition

  
Off |  System is in an undefined operational state or not receiving power.  
Fan Module  (callout 3 on the Chassis Rear Panel)![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309097.jpg) |  Off  |  No power to the chassis or the fan module was removed from the chassis.   
Amber  |  Fan module restarting.   
Green  |  Normal operation.   
Blinking amber  |  The fan module has failed.   
Power Supplies, each has one a bicolor LED (callout 2 on the Chassis Front Panel)![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309097.jpg) |  Off  |  Power supply is not fully seated, so no connection exists.  
Green  |  Normal operation.   
Blinking green  |  AC power is present, but the power supply is in Standby mode.  
Amber  |  Any fault condition is detected. Some examples:

  * Over or under voltage
  * Over temperature alarm
  * Power supply has no connection to a power cord. 

  
Blinking Amber  |  Any warning condition is detected. Some examples:

  * Over voltage warning
  * Over temperature warning

  
Table 3. Intelligent Fabric Module and Rear Module Blank LEDs  LED  |  Color  |  Description   
---|---|---  
Module Status  (callout 1 and 4 on the Chassis Rear Panel)![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309097.jpg) |  Off  |  No power.   
Green  |  Normal operation.   
Amber  |  Booting or minor temperature alarm.   
Blinking amber  |  POST error or other error condition.   
Module Fans (callout 1 and 4 the Chassis Rear Panel)![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309100.jpg) |  Off  |  Link down.   
Green  |  Link up and operationally enabled.   
Amber  |  Link up and administratively disabled.   
Blinking amber  |  POST error or other error condition.   
Table 4. Compute Node Server LEDs LED  |  Color  |  Description   
---|---|---  
Compute Node Power  (callout 3 on the Chassis Front Panel) ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309112.jpg) |  Off  |  Power off.   
Green  |  Normal operation.   
Amber  |  Standby.   
Compute Node Activity  (callout 3 on the Chassis Front Panel)![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309098.jpg) |  Off  |  None of the network links are up.   
Green  |  At least one network link is up.   
Compute Node Health (callout 3 on the Chassis Front Panel) ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309097.jpg) |  Off  |  Power off.   
Green  |  Normal operation.   
Amber  |  Degraded operation.   
Blinking Amber  |  Critical error.   
Compute Node Locator LED and button (callout 3 on the Chassis Front Panel) ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309111.jpg) |  Off  |  Locator not enabled.   
Blinking Blue 1 Hz |  Locates a selected compute node—If the LED is not blinking, the compute node is not selected.  You can initiate the LED in UCS Intersight or by pressing the button, which toggles the LED on and off.   
Drive Activity ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309102.jpg) |  Off  |  Inactive.   
Green  |  Outstanding I/O to disk drive.   
Drive Health ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309101.jpg) |  Off  |  No fault detected, the drive is not installed, or it is not receiving power.  
Amber  |  Fault detected  
Flashing Amber 4 Hz |  Rebuild drive active. If the Drive Activity LED is also flashing amber, a drive rebuild is in progress.  
  
## Optional Hardware Configuration

As an option, the server chassis can support a GPU-based PCIe node that pairs with Cisco UCS X-Series compute nodes to provide GPU acceleration. The following PCIe nodes are supported. 

  * The Cisco UCS X440p PCIe Node, which offers:

  * A GPU adapter node supporting zero, one or two GPUs through two separate GPU cages. For information about supported GPUs, go to the [Cisco UCS X440p PCIe Node Spec Sheet](https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-x-series-modular-system/x440p-specsheet.pdf). 

  * Each GPU installs directly into the GPU adapter card by a x8 Gen 4 PCI connection.

  * A storage adapter and riser card supporting zero, one, or two U.2 NVMe drives. NVMe RAID is supported through Intel VROC key on connected M6 compute nodes only. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For the Cisco UCS X9508 chassis to support any number of Cisco UCS X440p PCIe Nodes, both Cisco UCS X9416 Fabric Modules must be installed to provide proper PCIe signaling and connectivity to the node slots on the front of the server chassis. 
  * For information about the optional Cisco UCS X440p PCIe node, go to [Cisco UCS X440p PCIe Node Installation and Service Guide](https://www.cisco.com/content/en/us/td/docs/unified_computing/ucs/x/hw/x440p/install/b-cisco-ucs-x440p-gen4-pcie-install-guide.html). 
  * For information about the Cisco UCS X9416 Fabric Module, see Cisco UCS X9416 Fabric Module. 

* * *  
  
---|---  
  * The Cisco UCS X580p PCIe Node, which offers:

  * A GPU adapter node supporting zero through four GPUs through two separate PCIe cages. For information about supported GPUs, go to the [Cisco UCS X580p PCIe Node Spec Sheet](https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-x-series-modular-system/x580p-specsheet.pdf). 

  * Each GPU installs directly into a GPU cage by x16 Gen5 PCIe connection

  * Each PCIe node can connect to up to two separate M8 compute nodes. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For the Cisco UCS X9508 chassis to support any number of Cisco UCS X580p PCIe Nodes, both Cisco UCS X9516 Fabric Modules must be installed to provide proper PCIe signaling and connectivity to the node slots on the front of the server chassis. 
  * For information about the optional Cisco UCS X580p PCIe node, go to the [Cisco UCS X580p PCIe Node Installation and Service Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x580p/install/b-cisco-ucs-x580p-gen5-pcie-install-guide/m-servicing-the-node.html). 
  * For information about the Cisco UCS X9516 Fabric Module, see Cisco UCS X9516 Fabric Module. 

* * *  
  
---|---  


---

## Page 14: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x9508/install/m-installation.html

# Installation

This chapter contains the following topics:

## Installation Notes and Warnings for the Cisco UCS X9508 Server Chassis

The following notes and warnings apply to all installation tasks: 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Before you install, operate, or service the system, see the [Regulatory Compliance and Safety Information for Cisco UCS ](http://www.cisco.com/en/US/docs/unified_computing/ucs/hw/regulatory/compliance/ucs_regulatory_compliance_Information.html) for important safety information. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

The chassis can be shipped either empty or pre-populated. If the chassis is shipped pre-populated, do not remove the X-Fabric Modules in the two bottom rear slots. Other rear components, such as Intelligent Fabric Modules and fan modules should be removed to lighten the weight of the chassis.  On the front of the chassis, such as PSUs and Compute Nodes, can be removed to lessen the overall chassis weight before installation. However, even with compute nodes and PSUs removed, the chassis still has considerable weight. So, make sure to use a scissors jack, equipment lift, or other machinery to bear the weight of the chassis during installation. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/warn.gif)  
**Warning** | 

* * *

IMPORTANT SAFETY INSTRUCTIONS  This warning symbol means danger. You are in a situation that could cause bodily injury. Before you work on any equipment, be aware of the hazards involved with electrical circuitry and be familiar with standard practices for preventing accidents. Use the statement number provided at the end of each warning to locate its translation in the translated safety warnings that accompanied this device. Statement 1071  **SAVE THESE INSTRUCTIONS**

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/warn.gif)  
**Warning** | 

* * *

This unit is intended for installation in restricted access areas. A restricted access area can be accessed only through the use of a special tool, lock and key, or other means of security. Statement 1017 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/warn.gif)  
**Warning** | 

* * *

Only trained and qualified personnel must be allowed to install, replace, or service this equipment. Statement 1030

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

Watch your hands and fingers whenever you handle the chassis, modules, nodes, and components! Narrow vertical or horizontal spaces in situations like, but not limited to, moving the chassis into or out of the shipping container or equipment rack can cause pinch hazards for your hands and fingers.  Although they do not eliminate the possibility of pinching, the chassis has defined grasp points to facilitate handling and moving it. For information about chassis grasp points, see Handling the Chassis. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Do not lift or handle the chassis by the top rear sheet metal, as indicated by the DO NOT LIFT label on the top rear surface. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

The Cisco UCS X9508 Server Chassis can support the Cisco UCS X440p PCIe Nodes (Gen4) and the Cisco X580p PCIe Nodes (Gen5), but only one type per chassis. You cannot install the X440p and X580p PCIe nodes in the same chassis. If you are installing either of these PCIe nodes, each X9508 must be homogenous regarding the PCIe node type, all Gen4 PCIe nodes or all Gen5. 

* * *  
  
---|---  
  
  * Rack Requirements
  * Airflow Considerations
  * Earth Ground Considerations
  * Handling the Chassis
  * Moving Server Chassis
  * Installation Guidelines
  * Required Equipment
  * Unpacking and Inspecting the Chassis


### Rack Requirements

This section provides the requirements for installing in a standard open rack, assuming an external ambient air temperature range of 41 to 95°F (5 to 35°C): 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Do not use racks that have obstructions. These obstructions could impair access to field-replaceable units (FRUs).

* * *  
  
---|---  
  
Cisco UCS is compliant with any EIA-310-D/E compliant rack. Your equipment racks must also be compliant with EIA-310-D/E standard.

The Cisco UCS X9508 chassis can be installed in either a 9.5 mm square-hole rack or a 7.1 mm unthreaded round-hole rack. These racks require either square-hole cage nuts or round-hole cage nuts (also called spring nuts), respectively. 

  * Cage nuts are provided by Cisco as part of the accessory kit for your chassis.

  * Spring nuts are not provided by Cisco. They should have accompanied your equipment rack. 


Always use the proper cage nut or spring nut for your rack. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Some racks might be tapped, with threaded holes drilled directly into the rack's sheetmetal instead of square- or round-hole punch-outs for cage nuts. The rail kit for the server is not currently supported in tapped (threaded hole) racks. Do not attempt to install the chassis in a tapped (threaded hole) equipment rack. 

* * *  
  
---|---  
  
Also, be aware of these additional requirements:

  * The tool-less rack-mount kits (either Type 1 or Type 2) shipped with the chassis are required. The adjustable rack rails shipped with each enclosure extend from 29 inches (73.66 cm) to 35 inches (88.9 cm) 

  * Front and rear doors—If your equipment rack includes closing front and rear doors, the doors must have 65 percent open perforated area evenly distributed from top to bottom to permit adequate airflow. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Always use blanking panels to fill all remaining empty front panel U-spaces in the rack. This arrangement ensures proper airflow. Using a rack without blanking panels results in improper cooling that can lead to thermal damage. 

* * *  
  
---|---  


The rack must also meet the following requirements:

  * The minimum available vertical rack space per chassis must be seven RU (rack units), equal to 12.25 inches (31.2 cm).


### Airflow Considerations

Airflow through the chassis is from front to back. Air enters the chassis through the nodes and power supply grills at the front of the chassis and exits through the fan modules on the back of the chassis. To ensure proper airflow, follow these guidelines: 

  * Maintain ambient airflow throughout the data center to ensure normal operation. 

  * Consider the heat dissipation of all equipment when determining air-conditioning requirements. Do not allow the exhaust of one system to be the intake for another system. 

  * When evaluating airflow requirements, take into consideration that the hot air generated by equipment at the bottom of the rack can be drawn in the intake of the equipment above. 

  * Make sure that the exhaust at the rear of the chassis is unobstructed for at least 24 in. (61 cm). This includes obstruction due to messy cabling practices. 

  * If an enclosed rack is used, the front door must be 65 percent perforated to ensure adequate airflow to the nodes. 


### Earth Ground Considerations

#### Earth Ground Compliance

![](https://www.cisco.com/content/dam/en/us/td/i/templates/warn.gif)  
**Warning** | 

* * *

This equipment must be grounded. Never defeat the ground conductor or operate the equipment in the absence of a suitably installed ground conductor. Contact the appropriate electrical inspection authority or an electrician if you are uncertain that suitable grounding is available. Statement 1024 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/warn.gif)  
**Warning** | 

* * *

For Nordic countries (Norway, Finland, Sweden and Denmark) this system must be installed in a Restricted Access Location, where the voltage of the main ground connection of all equipment is the same (equipotential earth) and the system is connected to a grounded electrical outlet. Statement 328 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/warn.gif)  
**Warning** | 

* * *

High leakage current – earth connection essential before connection to system power supply. Statement 342

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/warn.gif)  
**Warning** | 

* * *

This equipment must be externally grounded using a customer-supplied ground wire before power is applied. Contact the appropriate electrical inspection authority or an electrician if you are uncertain that suitable grounding is available. Statement 366 

* * *  
  
---|---  
  
#### Ground Lug

Connecting the chassis to earth ground is completed by installing a grounding bracket, assembling the ground wire and ground lug, then screwing the ground lug and ground wire to the grounding bracket. 

The ground lug is provided in the accessory kit. If needed, additional ground lugs are available through third-party retailers, such as Panduit. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The following information is for standard AC power installations in North America. Your location might require different specifications. Make sure that you are using the correct ground lug and ground cable for your location. 

* * *  
  
---|---  
  
The ground lug must be a two-stud, copper barrel lug like the example shown below. 

  
![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309413.jpg)  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The positive and negative wires can be installed pointing either to the right or to the left as long as the terminal cover is used.  Panduit LCD4-14A-L connectors (or equivalent) may be used supply and return wires, and Panduit LCD4-14A or equivalent connectors may be used for the 90-degree ground lug wire. Both connections have double lugs with .25-inch holes measuring .625 inches from center to center. 

* * *  
  
---|---  
  
### Handling the Chassis

As a best practice, handle the chassis when it is empty, and use either a scissors jack or multiple people to bear the weight. 

The Cisco UCS X9508 has defined areas for holding the chassis (grasp points). Grasp points are not indicated on the chassis itself, but facilitate handling or moving the chassis. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

Watch your hands and fingers whenever you handle the chassis, modules, nodes, and components! Narrow vertical or horizontal spaces in situations including, but not limited to, moving the chassis into or out of the shipping container or equipment rack can cause pinch hazards for your hands and fingers. 

* * *  
  
---|---  
  
Use the following grasp points when handling the chassis. 

  * Front grasp points, horizontal

![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309700.jpg)

![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309701.jpg)

  * Rear grasp points

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Do not lift or handle the chassis by the top rear sheet metal, as indicated by the DO NOT LIFT label on the top rear surface. 

* * *  
  
---|---  
![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472423.jpg)


### Moving Server Chassis

A fully configured chassis is very heavy! Be aware of its weight, and follow these guidelines:

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Do not try to lift the chassis without mechanical assistance! The chassis weighs 400 lbs (181.43 kg) fully configured and 92 lbs (41.73 kg) empty. If available, use a scissor jack or other lifting device designed for installing heavy equipment into data center racks. 

* * *  
  
---|---  
  
  * Disconnect all power and external cables before lifting the chassis.

  * Remove all IFMs, fan modules, power supplies and compute nodes from the chassis before lifting. If XFMs are installed, do not remove them. Instead, leave them in the chassis during installation. 

  * Ensure that your footing is solid, and the weight of the system is evenly distributed between your feet.

  * If you must lift an empty chassis, do not attempt this alone. Get assistance from at least one other person. Lift the system slowly, keeping your back straight. Lift with your legs, not with your back. Bend at the knees, not at the waist. 


### Installation Guidelines

When installing the chassis, follow these guidelines: 

  * Plan your site configuration and prepare the site before installing the chassis. See [Site Planning and Maintenance Records](m-site-planning-and-maint-records.html#ID9) for the recommended site planning tasks. For details, see the [Cisco UCS Site Preparation Guide](http://www.cisco.com/en/US/docs/unified_computing/ucs/hw/site-prep-guide/ucs_site_prep.html). 

  * Record the information listed in [Site Planning and Maintenance Records](m-site-planning-and-maint-records.html#ID9) as you install and configure the chassis. 

  * Ensure that there is adequate space around the chassis to allow for servicing the chassis and for airflow. 

  * Ensure that the air-conditioning meets the heat dissipation requirements listed in [Technical Specifications](m-technical-specs.html#ID6)

  * Ensure that the cabinet or rack meets the requirements listed in Rack Requirements. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Jumper power cords are available for use in a rack. See [Specifications for the Cisco UCS X9508 Chassis Power Supply Units](m-technical-specs.html#ID256). 

* * *  
  
---|---  
  * Ensure that the site power meets the power requirements listed in [Technical Specifications](m-technical-specs.html#ID6). We recommend that you use a UPS to protect the UCS system. Using an unprotected supply exposes you to a risk of system failure due to input supply voltage variations or failures. 

Avoid UPS types that use ferroresonant technology. These UPS types can become unstable with systems such as the Cisco UCS, which can have substantial current draw fluctuations due to fluctuating data traffic patterns. 

  * Ensure that circuits are sized according to local and national codes. For North America, the power supply requires a 20 A circuit. 

To prevent loss of input power, ensure that the total maximum loads on the circuits supplying power to the chassis are within the current ratings for the wiring and breakers. 

  * Use the following torque values when installing the chassis: 

  * M6 x 20 mm screws: 48 +/- 5 in-lb 


### Required Equipment

Before you begin the installation, ensure that you have the following items:

  * Scissor jack or other lift device capable of bearing the weight of a fully loaded chassis, which is 400 lbs (181.43 kg).

  * Number 1 and number 2 Phillips-head screwdrivers with torque measuring capabilities

  * Flat-head screwdriver

  * Tape measure and level

  * ESD wrist strap or other grounding device

  * Antistatic mat or antistatic foam


### Unpacking and Inspecting the Chassis

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

When handling chassis components, wear an ESD strap and handle modules by the carrier edges only.

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/tip.gif)  
**Tip** | 

* * *

Keep the shipping container in case the chassis requires shipping in the future.

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The chassis is thoroughly inspected before shipment. If any damage occurred during transportation or any items are missing, contact your customer service representative immediately. 

* * *  
  
---|---  
  
As part of this procedure, you will be moving an empty chassis out of the shipping container. Be aware of the following precautions:

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

You will find it helpful to wear gloves when unpacking and lifting the chassis. Also, beware of hand and finger placement while unpacking, lifting, and moving the chassis to avoid possible pinch hazards. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

To lighten the weight of the chassis, remove compute nodes and PSUs from the front of the chassis. Remove the IFMs and fan modules from the rear of the chassis, but leave the XFMs installed in the lower rear slots of the chassis. Even with these parts removed, the chassis still has considerable weight. Always use a scissors jack, equipment lift, or other mechanical device to lift and support the chassis when moving or installing it. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/warn.gif)  
**Warning** | 

* * *

Use two or more people to lift the empty chassis. Do not attempt to lift the chassis by yourself! Always use safe lifting practices when lifting or moving the chassis.  Use a lift or scissors jack to support the chassis when lifting and moving it.

* * *  
  
---|---  
  
#### Procedure

* * *

**Step 1** |  Make sure to read and understand the preceding warnings in this topic, as well as the information in the following topics:

  * Installation Notes and Warnings for the Cisco UCS X9508 Server Chassis
  * Handling the Chassis
  * Moving Server Chassis

  
---|---  
**Step 2** |  Open the chassis shipping container.

  1. Remove the top and side panels so that the chassis is sitting on the bottom pallet. 
  2. Save all packaging material.

  
**Step 3** |  Do a visual inspection of the chassis to ensure there was no damage during transport.  
**Step 4** |  Compare the shipment to the equipment list provided by your customer service representative and verify that you have received the following items: 

  * Accessory kit, which contains:
  * M6 cage nuts (4) for square-hole equipment racks. Spring nuts for round-hole equipment racks are not provided by Cisco.
  * M6 x 20mmL screw (16)
  * Power Cable Management Arm (2), UCSX-9508-PCMA
  * Rail Kit, UCSX-9508-RAIL1=
  * Any printed documentation
  * Any optional items, which will be present in the accessory kit only if you ordered them with your system. 
  * Rear Mounting Brackets (1 left bracket, 1 right bracket), UCSX-9508-RACKBK. These brackets are optional. They should be ordered only if you plan to install the chassis in shippable rack. If you don't plan on shipping the rack, these brackets are not required. 
  * Compute Node Debug Cable, UCSX-C-DEBUGCBL, which is orderable as a customer option. 

  
**Step 5** |  Verify that all unused node slots and power supply bays have blank covers.  
**Step 6** |  If your chassis was shipped with hardware pre-installed, make sure to remove all compute nodes and PSUs, fans, and IFMs to reduce the chassis weight significantly before lifting it out of the shipping container. Blank faceplates can remain installed. Leave the XFMs installed in the bottom two rear chassis slots.  |  **Warning** |  Do not lift a chassis! The chassis has considerable weight even with all modules except the XFMs removed. Use a mechanical lift of scissors jack to lift and bear the weight of the chassis.   
---|---  
**Step 7** |  Locate the chassis handles, which are also the stabilizing brackets that secure the chassis to the bottom pallet.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309944.jpg)  
**Step 8** |  Using a 13-millimeter socket driver, remove the four M8 hex-head securing bolts (two per side).  |  **Note** |  Save the securing bolts.  
---|---  
  
![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540011.jpg)  
  
**Step 9** |  With two or more people, grasp the handles, lift the empty chassis off of the bottom palette, and set the chassis onto a lift or scissor jack that can support the chassis weight.   
**Step 10** |  Before installing the chassis into an equipment rack, use a #2 Phillips screwdriver to remove the two M5 screws (two per handle) that secure the handles to the chassis.  |  **Note** |  Save the handles and screws.   
---|---  
  
![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309945.jpg)

**1** |  Chassis handles, two per side |  **2** |  M5 screws, two per handle  
---|---|---|---  
  
* * *

## Rail Installation Templates

Two rail kits are available, and each shipping container will contain a left and right rail as a matched set. For each rail kit, a corresponding template is provided for reference through the following sections of this document. The templates show the locations on the rack for cage nuts, rail kit locator pegs, and screws should be installed. 

The templates facilitate installing the rail kit and chassis by ensuring proper spacing and alignment of installation hardware in both the left and right sides of the rack. The chassis has one template for the front of the rack and one for the back. 

Rail installation templates are applicable to either square-hole or round-hole equipment racks.

For each rail installation template, see: 

  * Front Install Template

  * Rear Install Template


  * Front Install Template
  * Rear Install Template


### Front Install Template

Use this installation to locate the correct spacing and alignment for chassis mounting hardware on the rack. This template shows the rack locations for mounting the front of the chassis. 

Align the Chassis Top of the template with the location in the rack where the top of the chassis will be and install the cage nuts and other hardware as shown. 

Figure 1. Rack Installation Template, Front  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308940.jpg)

### Rear Install Template

Use this installation to locate the correct spacing and alignment for chassis mounting hardware on the rack. This template shows the rack locations for mounting the rear of the chassis. 

Align the Chassis Top of the template with the location in the rack where the top of the chassis will be and install the cage nuts and other hardware as shown. 

Figure 2. Rack Installation Template, Rear  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308949.jpg) ![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The eight cage nuts shown near the top of the template (four per side) are required only when you are installing the rear tie down brackets, which are an orderable option, but not required for basic installation. 

* * *  
  
---|---  
  
## Installing Cage Nuts

The Cisco UCS X9508 chassis can be installed in standard size, untapped equipment racks that have either square or round-holes. For more information, see Rack Requirements. The X9508 server is supported on a rail kit which mounts to the square-hole or round hole cage. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

For untapped equipment racks, you must install cage nuts to provide a way for mounting screws to secure rails and the chassis to the rack. 

* * *  
  
---|---  
  
Use the appropriate option depending on your type of equipment rack:

  * Installing Cage Nuts, Square-Hole Rack

  * Installing Cage Nuts, Round-Hole Rack


  * Installing Cage Nuts, Square-Hole Rack
  * Installing Cage Nuts, Round-Hole Rack


### Installing Cage Nuts, Square-Hole Rack

Use the following task to install twelve, M6x1.00 square-hole cage nuts into a 9.5 mm unthreaded square-hole rack. Spring nuts are not supplied by Cisco. They should have accompanied your equipment rack. 

#### Before you begin

This document provides illustrations of installation templates for the front and rear of the chassis. The templates are designed to show you the proper holes within which the rails and cage nuts should be placed. Once you align the rack holes line up with the template, you should mark the holes on the rack so that they are easy to use. 

To use the rack installation templates, go to the appropriate topic:

  * Front Install Template

  * Rear Install Template


#### Procedure

* * *

**Step 1** |  Gather the M6 cage nuts and a flat head screwdriver.   
---|---  
**Step 2** |  Locate the template and refer to the chassis location in the rack and the cage nut locations on the template.   
**Step 3** |  Position one of the curled sides of the cage nut on the inside of the square cutout in the rack.   
**Step 4** |  Press the cage nut into the cutout and use the screwdriver to pinch the other curled edge inward until the cage nut clicks into place in the rack.  |  **Note** |  Cage nuts install on the inside of the rack so that most of the nut is behind the rack's sheet metal.  
---|---  
Figure 3. Cage Nut Installation  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308941.jpg)  
**Step 5** |  Verify that the cage nut is fully and correctly installed before installing the remaining cage nuts.   
  
* * *

### Installing Cage Nuts, Round-Hole Rack

Use the following task to install twelve M6x1.00 round-hole cage nuts (also called spring nuts) into a 7.1 mm unthreaded round-hole rack. Spring nuts are not supplied by Cisco. They should have accompanied your equipment rack. 

#### Before you begin

This document provides illustrations of installation templates for the front and rear of the chassis. The templates are designed to show you the proper holes within which the rails and cage nuts (spring nuts) should be placed. Once you align the rack holes line up with the template, you should mark the holes on the rack so that they are easy to use. 

To use the rack installation templates, go to the appropriate topic:

  * Front Install Template

  * Rear Install Template


#### Procedure

* * *

**Step 1** |  Gather the M6 spring nuts and a flat head screwdriver.   
---|---  
**Step 2** |  Using the rack installation template, refer to the chassis location in the rack and the spring nut locations on the template.   
**Step 3** |  Position the open end of the spring nut so that the rack's sheetmetal can slide into the gap between the spring nut's sheetmetal.   
**Step 4** |  Slide the spring nut so that its round hole lines up with the round hole in the equipment rack.  |  **Note** |  Cage nuts install so that most of the nut is behind the rack's sheet metal.  
---|---  
**Note** |  If needed, use the flat-head screwdriver to slightly pry open the gap between the spring nut's sheetmetal to allow it to slide onto the rack over the round hole.   
---|---  
![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540686.jpg)  
**Step 5** |  Verify that the cage nut is fully and correctly installed before installing the remaining cage nuts.   
  
* * *

## Rail Kits

The Cisco UCS X9508 supports two rail kits, Type 1 and Type 2.

  * Each rail kit consists of two stationary rails that facilitate rack installation of the chassis and stabilize the chassis in the rack. 

  * Each rail extends to fit the depth of the rack. The rails are not a sliding shelf that allow pulling the chassis out of the rack to gain access to the chassis' sides. 

  * Each rail kit can fit into either a 9.5 mm square hole equipment rack or a 7.1 mm round-hole equipment rack. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Some racks might be tapped, with threaded holes drilled directly into the rack's sheetmetal instead of square- or round-hole punchouts for cage nuts. The rail kit for the server is not currently supported in tapped (threaded hole) racks. Do not attempt to install the chassis in a tapped (threaded-hole) equipment rack. 

* * *  
  
---|---  


The rails are shipped in the accessory kit with each chassis, and each rail kit will contain a left and right side as a matched pair. Both sides must be installed in the rack to securely support the chassis. 

If you ordered multiple UCS X9508 chassis, you might receive both types of rail kit. For example, in a shipment of 4 chassis, the shipment might have all one type of rail kit, or a few chassis with each type of rail kit. 

Compare the two types of rail kits:

Figure 4. Two Types of Rail Kits  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308950.jpg)

The rail kits are similar in size, function, and construction with a few exceptions:

  * the type of release tab at the top corner of the rail

  * the type of locator pegs, either round or square depending on whether you have a round-hole or square-hole rack. The locator pegs temporarily hold the rail in the rack to allow free use of both hands. 

  * the positioning of the screw holes at the rear of the rails


## Installing the Chassis

This section describes how to install the chassis in either a square-hole unthreaded or round-hole unthreaded equipment rack. This two-part process consists of installing the rails into the rack, then installing the chassis into the rack and onto the rails. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

The fully configured chassis weighs approximately 400s lbs (163.29 kg)! Never attempt to lift the chassis by yourself. Instead, use a chassis lift or some other device to lift and bear the weight of the chassis while you are installing it. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

If the rack has wheels, ensure that the brakes are engaged, the stabilizing pads are extended, or that the rack is otherwise stabilized. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/warn.gif)  
**Warning** | 

* * *

The plug-socket combination must be accessible at all times, because it serves as the main disconnecting device. **Statement 1019**

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

When connecting the chassis to facility power, make sure not to overload the capacity of a PDU or power strip. For example, do not connect all PSUs to one PDU or power strip that is not capable of carrying the total power draw of the chassis. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

Watch your hands and fingers whenever you handle the chassis, modules, nodes, and components! Narrow vertical or horizontal spaces in situations including, but not limited to, moving the chassis into or out of the shipping container or equipment rack can cause pinch hazards for your hands and fingers.  Although they do not eliminate the possibility of pinching, the chassis has defined grasp points to facilitate handling and moving it. For information about chassis grasp points, see Handling the Chassis. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

To complete the installation, the chassis must be connected to earth ground, which requires a ground lug that Cisco provides, or an equivalent. See "Ground Lug" in Earth Ground Considerations. 

* * *  
  
---|---  
  
Where applicable, the following installation topics have options for square-hole and round-hole racks. Pick the appropriate topic based on your rack type. 

  * Installing the Rails, Square-Hole Rack
  * Installing the Rails, Round-Hole Rack
  * Rail Installation Layout, Square-Hole Rack
  * Rail Installation Layout, Round-Hole Rack
  * Installing the Top Cable Management Arms
  * Installing the Ground Bracket and Bottom Cable Management Arms
  * Inserting the Chassis into a Square-Hole Rack
  * Inserting the Chassis into a Round-Hole Rack
  * Installing Rear Mounting Brackets, Square-Hole Rack
  * Installing Rear Mounting Brackets, Round-Hole Rack
  * Completing Installation
  * Choosing Earth Ground Option
  * Attaching Cable Management Trays


### Installing the Rails, Square-Hole Rack

Use the following task to install the rail kit into a square-hole unthreaded equipment rack by using twelve, M6x1.00 square-hole cage nuts. 

#### Before you begin

Make sure that you have marked the correct cage nut and rail locations on the rack by using the illustrations of the rack installation templates. See Rail Installation Templates. 

#### Procedure

* * *

**Step 1** |  Adjust the length of the rail by sliding the ends of the rail back and forth until they match the depth of the rack.   
---|---  
**Step 2** |  At the front of the rack, use the front installation template to position the two locator pegs on the rail with the corresponding location in the rack. See Front Install Template.  The locator pegs will hold the rail in the rack so that you don't have to hold the rail in place.   
**Step 3** |  At the rear of the rack, use the rear installation template to position the two locator pegs on the rail with the corresponding location in the rack. See Rear Install Template.   
**Step 4** |  Repeat the previous steps to install the other rack rail.  Figure 5. Install Rails into Front of the Rack  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308937.jpg)  
**Step 5** |  (Optional) Use a tape measure and level to verify that the rack rails are horizontal and at the same height.   
**Step 6** |  At the front of the rack, refer to the template, then insert a screw in each front rail to secure each rail to the rack at the correct location.  Figure 6. Secure the Rail at the Front to the Rack  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308939.jpg)  
**Step 7** |  At the rear of the rack, refer to the template, then insert a screw in each rear rail to secure each rail to the rack at the correct location.   
**Step 8** |  Figure 7. Secure the Rail at the Rear of the Rack  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308948.jpg)  
  
* * *

#### What to do next

Verify that the rails are correctly installed. See Rail Installation Layout, Square-Hole Rack. 

### Installing the Rails, Round-Hole Rack

Use the following task to install the rail kit into a round-hole unthreaded equipment rack by using twelve, M6x1.00 round-hole spring nuts. 

#### Before you begin

Make sure that you have marked the correct cage nut (spring nut) and rail locations on the rack by using the illustrations of the rack installation templates. See Rail Installation Templates. 

#### Procedure

* * *

**Step 1** |  Adjust the length of the rail by sliding the ends of the rail back and forth until they match the depth of the rack.   
---|---  
**Step 2** |  At the front of the rack, use the front installation template to position the two locator pegs on the rail with the corresponding location in the rack. See Front Install Template.  The locator pegs will keep the rail in the rack so that you don't have to hold the rail in place.   
**Step 3** |  At the rear of the rack, use the rear installation template to position the two locator pegs on the rail with the corresponding location in the rack. See Rear Install Template.   
**Step 4** |  Repeat the previous steps to install the other rack rail.  Figure 8. Install Rails into Front of the Rack  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540665.jpg)  
**Step 5** |  (Optional) Use a tape measure and level to verify that the rack rails are horizontal and at the same height.   
**Step 6** |  At the front of the rack, refer to the template, then insert a screw in each front rail to secure each rail to the rack at the correct location.  Figure 9. Secure the Rail at the Front to the Rack  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540667.jpg)  
**Step 7** |  At the rear of the rack, refer to the template, then insert a screw in each rear rail to secure each rail to the rack at the correct location.   
**Step 8** |  Figure 10. Secure the Rail at the Rear of the Rack  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308948.jpg)  
  
* * *

#### What to do next

Verify that the rails are correctly installed. See Rail Installation Layout, Round-Hole Rack. 

### Rail Installation Layout, Square-Hole Rack

Before installing the chassis in the rack, compare the rail installation in the rack against the following layout images. If the rail installation is different than what is shown in each layout, remove the rails and reinstall them. 

Figure 11. Front Rail Layout, Both Rail Kits  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308938.jpg) ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540754.jpg) |  Cage Nut, square-hole rack  
---|---  
![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540755.jpg) |  Empty RETMA Rail Hole, square-hole rack  
![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540756.jpg) |  Locator Peg for Rail Kit  
![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540758.jpg) and ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540757.jpg) |  Mounting Screw for Rail Kit  
Figure 12. Rear Rail Layout, Both Rail Kits  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308947.jpg) ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540754.jpg) |  Cage Nut, square-hole rack  
---|---  
![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540755.jpg) |  Empty RETMA Rail Hole, square-hole rack  
![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540756.jpg) and  |  Locator Peg for Rail Kit  
![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540758.jpg) and ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540757.jpg) |  Mounting Screw for Rail Kit  
  
### Rail Installation Layout, Round-Hole Rack

Before installing the chassis in the rack, compare the rail installation in the rack against the following layout images. If the rail installation is different than what is shown in each layout, remove the rails and reinstall them. 

Figure 13. Front Rail Layout, Both Rail Kits  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540666.jpg) ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540759.jpg) |  Spring Nut for round-hole rack  
---|---  
![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540760.jpg) |  Empty RETMA Rail Hole, round-hole rack  
![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540761.jpg) |  Locator Peg for Rail Kit  
![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540762.jpg) |  Mounting Screw for Rail Kit  
Figure 14. Rear Rail Layout, Both Rail Kits  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540674.jpg) ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540759.jpg) |  Spring Nut for round-hole rack  
---|---  
![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540760.jpg) |  Empty RETMA Rail Hole, round-hole rack  
![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540761.jpg) |  Locator Peg for Rail Kit  
![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540762.jpg) |  Mounting Screw for Rail Kit  
  
### Installing the Top Cable Management Arms

The accessory kit contains two cable management assemblies, each one consisting of three cable management arms and three cable ties. The cable management assemblies facilitate gathering and organizing the chassis power cables. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The server also has cable management trays (UCSX-9508-CMA) for gathering and organizing the cables from the IFMs and X-Fabric modules. 

* * *  
  
---|---  
  
In this topic, top and bottom refer to the location on the chassis. Cable management arms are interchangeable, so there is no specific top and bottom cable arm. 

Each cable management assembly is for a set of three PSUs. The top cable management arms attach to the top set of PSUs in the chassis. The bottom cable management arms attach a grounding bracket for the bottom set of PSUs, so the installation procedure is slightly different. See Installing the Ground Bracket and Bottom Cable Management Arms. 

Use this task to attach the cable management assemblies to the chassis before installing the chassis in the rack.

#### Procedure

* * *

**Step 1** |  Align the captive screws in the cable management sheet metal with the threaded standoffs on the chassis.   
---|---  
**Step 2** |  Using a #2 Phillips-head screwdriver, attach the cable management arms to the server chassis by tightening the captive screws.  Figure 15. Attaching the Top Cable Management Arms to the Chassis  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308904.jpg)  
**Step 3** |  Adjust the cable tie horizontally to align with where you wish to grasp the power cable.  
**Step 4** |  You can use the cable ties to gather the power cables and secure the plugs in place.  Figure 16. Gathering Power Cables  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308966.jpg)  
  
* * *

#### What to do next

Attach the remaining cable management arms. See Installing the Ground Bracket and Bottom Cable Management Arms. 

### Installing the Ground Bracket and Bottom Cable Management Arms

The cable management arm (CMA) for the bottom set of PSUs contains an integrated ground lug that provides earth grounding for the chassis. The horizontal metal piece is the ground lug to which the grounding cable can be attached. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

In this topic, top and bottom refer to the specific cable management arms. Cable management arms are not interchangeable. The bottom CMA contains the integrated ground lug, but the top CMA does not. 

* * *  
  
---|---  
  
For the additional ground requirements, see Earth Ground Considerations. 

#### Procedure

* * *

Attach the bottom cable management arm to the chassis. 

  1. Align the long side of the ground bracket with the threaded standoff on the chassis.
  2. Align the captive screws in the cable management arm with the threaded standoffs on the chassis.  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472424.jpg) |  1 |  Threaded Standoffs on chassis |  2 |  Bottom CMA, long side aligned with standoffs  
---|---|---|---  
3 |  Captive Screws on CMA  |  |   
  3. Using a #2 Phillips-head screwdriver, secure the bottom cable management arms to the server chassis by tightening the captive screws. 


  
  
* * *

### Inserting the Chassis into a Square-Hole Rack

#### Before you begin

If you have not already verified that the rails are installed as indicated in the front and rear layouts, do so now. See Rail Installation Layout, Square-Hole Rack. 

Also, make sure to review Installation Notes and Warnings for the Cisco UCS X9508 Server Chassis. 

The chassis must be grounded by a ground lug that Cisco provides, or an equivalent. See "Ground Lug" in Earth Ground Considerations. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Before beginning this procedure, make sure that the rails are correctly installed, and all the rail kits' mounting screws are installed and tightened. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

Watch your hands and fingers whenever you handle the chassis, modules, nodes, and components! Narrow vertical or horizontal spaces in situations including, but not limited to, moving the chassis into or out of the shipping container or equipment rack can cause pinch hazards for your hands and fingers.  Although they do not eliminate the possibility of pinching, the chassis has defined grasp points to facilitate handling and moving it. For information about chassis grasp points, see Handling the Chassis. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/tip.gif)  
**Tip** | 

* * *

You will find it easier to move the chassis if you have additional people to help you.

* * *  
  
---|---  
  
#### Procedure

* * *

**Step 1** |  Using a scissor jack, chassis lift, or other mechanical device, lift the chassis and position it so that you can slide it into the rack.   
---|---  
**Step 2** |  Slide the chassis into the rack until the front flange is flat against the cage nuts.  Figure 17. Inserting the Chassis into the Rack  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308944.jpg)  
**Step 3** |  At the front of the chassis, remove each of the side trim panels from the chassis.  The side trim panels are attached magnetically, so you should be able to easily pull them off. Removing the side trim panels exposes the screw holes in each of the front mounting brackets. |  **Note** |  Keep the side trim panels in a safe location nearby. You will replace them when the chassis is installed.   
---|---  
Figure 18. Detach the Chassis Side Trim Panels  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308942.jpg)  
**Step 4** |  At the front of the chassis, use a #3 Phillips-head screwdriver to insert and tighten the eight M6 x 20mm screws through the front mounting flanges.  Figure 19. Securing the Front of the Chassis to the Rack  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308943.jpg)  
**Step 5** |  Choose the appropriate option:

  1. If your chassis will ship per-installed in a rack, attach the rear mounting brackets. If you plan to install and ship your chassis in a shippable rack, attach the rear mounting brackets. See Installing Rear Mounting Brackets, Square-Hole Rack. 
  2. If you will be installing the chassis in a stationary rack, continue the installation procedure. See Completing Installation. 

  
  
* * *

### Inserting the Chassis into a Round-Hole Rack

#### Before you begin

If you have not already verified that the rails are installed as indicated in the front and rear layouts, do so now. See Rail Installation Layout, Round-Hole Rack. 

Also, make sure to review Installation Notes and Warnings for the Cisco UCS X9508 Server Chassis. 

The chassis must be grounded by a ground lug that Cisco provides, or an equivalent. See "Ground Lug" in Earth Ground Considerations. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Before beginning this procedure, make sure that the rails are correctly installed, and all the rail kits' mounting screws are installed and tightened. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

Watch your hands and fingers whenever you handle the chassis, modules, nodes, and components! Narrow vertical or horizontal spaces in situations including, but not limited to, moving the chassis into or out of the shipping container or equipment rack can cause pinch hazards for your hands and fingers.  Although they do not eliminate the possibility of pinching, the chassis has defined grasp points to facilitate handling and moving it. For information about chassis grasp points, see Handling the Chassis. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/tip.gif)  
**Tip** | 

* * *

You will find it easier to move the chassis if you have additional people to help you.

* * *  
  
---|---  
  
#### Procedure

* * *

**Step 1** |  Using a scissor jack, chassis lift, or other mechanical device, lift the chassis and position it so that you can slide it into the rack.   
---|---  
**Step 2** |  Slide the chassis into the rack until the front flange is flat against the cage nuts (spring nuts).  Figure 20. Inserting the Chassis into the Rack  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540671.jpg)  
**Step 3** |  At the front of the chassis, remove each of the side trim panels from the chassis.  The side trim panels are attached magnetically, so you should be able to easily pull them off. Removing the side trim panels exposes the screw holes in each of the front mounting brackets. |  **Note** |  Keep the side trim panels in a safe location nearby. You will replace them when the chassis is installed.   
---|---  
Figure 21. Detach the Chassis Side Trim Panels  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540669.jpg)  
**Step 4** |  At the front of the chassis, use a #3 Phillips-head screwdriver to insert and tighten the eight M6 x 20mm screws through the front mounting flanges.  Figure 22. Securing the Front of the Chassis to the Rack  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540670.jpg)  
**Step 5** |  Choose the appropriate option:

  1. If your chassis will ship pre-installed in a rack, attach the rear mounting brackets. If you plan to install and ship your chassis in a shippable rack, attach the rear mounting brackets. See Installing Rear Mounting Brackets, Round-Hole Rack. 
  2. If you will be installing the chassis in a stationary rack, continue the installation procedure. See Completing Installation. 

  
  
* * *

### Installing Rear Mounting Brackets, Square-Hole Rack

Use this procedure to install the rear mounting (tie down) brackets (UCSX-9508-RACKBK) for a chassis that is not pre-installed in a rack. 

#### Before you begin

If the chassis is shipped pre-installed in a rack, the rear mounting brackets are already attached. 

#### Procedure

* * *

**Step 1** |  At the rear of the chassis, use your hands to install each rear mounting bracket, which has a folded tab at the top and a folded metal hook at the bottom. 

  1. Slide the hook the into the cutout in the chassis side wall.
  2. Slide each rear mounting bracket until the tab seats into the emboss in the chassis top.

Figure 23. Attaching Rear Mounting Brackets, Square-Hole Rack  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472425.jpg)  
---|---  
**Step 2** |  Holding the rear mounting brackets in place, use the #3 Phillips-head screwdriver to insert the 8 M6 x 20mm screws through the rear mounting brackets, then tighten the screws to secure the rear of the chassis to the rear of the rack.  Figure 24. Securing the Chassis to the Rack, Square-Hole Rack  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472426.jpg)  
  
* * *

#### What to do next

Complete installing the chassis into the rack. Go to Completing Installation. 

### Installing Rear Mounting Brackets, Round-Hole Rack

Use this procedure to install the rear mounting (tie down) brackets (UCSX-9508-RACKBK) for a chassis that is not pre-installed in a rack. 

#### Before you begin

If the chassis is shipped pre-installed in a rack, the rear mounting brackets are already attached. 

#### Procedure

* * *

**Step 1** |  At the rear of the chassis, use your hands to install each rear mounting bracket, which has a folded tab at the top and a folded metal hook at the bottom. 

  1. Slide the hook the into the cutout in the chassis side wall.
  2. Slide each rear mounting bracket until the tab seats into the emboss in the chassis top.

Figure 25. Attaching the Rear Mounting Brackets  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472427.jpg)  
---|---  
**Step 2** |  Holding the rear mounting brackets in place, use the #3 Phillips-head screwdriver to insert the 8 M6 x 20mm screws through the rear mounting brackets, then tighten the screws to secure the rear of the chassis to the rear of the rack.  Figure 26. Securing the Rear of the Chassis to the Rack  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472428.jpg)  
  
* * *

#### What to do next

Complete installing the chassis into the rack. Go to Completing Installation. 

### Completing Installation

Continue with installing the chassis.

#### Procedure

* * *

**Step 1** |  Verify that all the front and rear mounting screws for the rails and the chassis are tight, and the chassis is secured to the rack.   
---|---  
**Step 2** |  At the front of the chassis, attach the side trim panels. The side trim panels attach magnetically, so you don't need any tools.  
**Step 3** |  Making sure that all people and equipment are not under the chassis, lower and remove the lift.  
**Step 4** |  Install any additional IFMs, PSUs, nodes or other chassis components, if needed.  
**Step 5** |  To power up the chassis, connect the appropriate power cables to the inlet connector corresponding to each installed power supply, and then connect the other end of the cables to the power source. To determine the number of power supplies needed for a given configuration, use the [Cisco UCS Power Calculator](https://mainstayadvisor.com/Go/Cisco/Cisco-UCS-Power-Calculator.aspx) tool.  |  **Note** |  Both grids in a power redundant system should have the same number of power supplies. If your system is configured for grid power (N+N redundancy), slots 1, 2, and 3 are assigned to grid 1, and slots 4, 5, and 6 are assigned to grid 2. If fewer than six power supplies (PS) are configured in grid redundant mode, they should be equally distributed between the grid 1 and grid 2 slots.   
---|---  
**Step 6** |  Attach any remaining cables to provide fabric connectivity for the chassis and nodes and do a visual inspection of LEDs to ensure the chassis and its components are operating in runtime.   
  
* * *

### Choosing Earth Ground Option

The Cisco UCS X9508 server chassis supports connection to facility earth ground through either of the following options:

  * side mount, which supports connecting the ground cable directly to the chassis through a ground point on one side of the chassis. For this option, go to Connecting Side-Mount Earth Ground. 

  * rear mount, which supports connecting the ground cable to a ground bracket that attaches to one of the rear mounting brackets at the rear of the chassis. For this option, go to Connecting Rear-Mount Earth Ground. 


Choose the option that is appropriate for your installation. Both options require you to assemble the ground cable by crimping a ground lug onto the end of the ground cable. For information about the ground lug, see "Ground Lug" in Earth Ground Considerations. 

  * Connecting Side-Mount Earth Ground
  * Connecting Rear-Mount Earth Ground


#### Connecting Side-Mount Earth Ground

To connect side-mount earth ground you will connect a ground lug to a ground cable, then attach the cable to the designated earth ground point on the chassis sheet metal. The designated earth ground is on the side of the chassis. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The chassis also has a rear-mount option for earth ground by using a specific ground bracket that attaches to the rear of the chassis. For more information, see Connecting Rear-Mount Earth Ground. 

* * *  
  
---|---  
  
The facility ground cable must be terminated with the ground lug provided by Cisco, or an equivalent. For more information, see "Ground Lug" in Earth Ground Considerations. 

##### Procedure

* * *

**Step 1** |  Locate the two screw holes for the side-mount attachment point for earth ground.  The side-mount attachment point is designated with the earth ground symbol (![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309519.jpg) ).  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472429.jpg)  
---|---  
**Step 2** |  Assemble the ground cable.

  1. Use a wire-stripping tool to remove approximately 0.75 inches (19 mm) of the covering from the end of the grounding cable.
  2. Insert the stripped end of the grounding cable into the open end of the grounding lug. We recommend 6-AWG wire for the U.S. installations. Make sure to use the proper grounding cable and grounding wire as appropriate for your country or region.    
![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309378.jpg)  

  3. Use a crimping tool to secure the grounding cable in the grounding lug.
  4. Prepare the other end of the grounding cable and connect it to an appropriate ground point at the facility.  |  **Note** |  When the chassis is fully installed, the side-mount earth ground point should be in front of the rear mounting brackets. As a result, you should have enough space to attach the ground cable.   
---|---  

  
**Step 3** |  Attach the grounding cable to the grounding point on the side of the chassis.

  1. Position the ground lug.
  2. Align the terminal holes in the ground lug with the terminal holes in the side of the chassis.
  3. Using a #2 Phillips screwdriver, insert and tighten two M5 x 10mm pan-head screws to secure the grounding cable to the side of the chassis.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309496.jpg)

|  1 |  Assembled ground cable with lug positioned on chassis ground point |  2 |  Screw down ground cable to secure it to the side-mount ground point  
---|---|---|---  
  
* * *

#### Connecting Rear-Mount Earth Ground

Connecting the chassis to facility earth ground is supported through the chassis ground lug, which is installed at the side of the bottom set of PSUs. 

The facility grounding cable must be terminated with the ground lug provided by Cisco, or an equivalent. For more information, see "Ground Lug" in Earth Ground Considerations. 

Use this procedure to connect the chassis to earth ground. 

##### Before you begin

This procedure assumes that you have already attached the bottom cable management arm with the integrated grounding lug. For information, see Installing the Ground Bracket and Bottom Cable Management Arms. 

##### Procedure

* * *

**Step 1** |  Verify that the bottom CMA and ground lug is correctly installed. If not, install it now. See Installing the Ground Bracket and Bottom Cable Management Arms.  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472430.jpg) |  1 |  Bottom CMA with integrated ground lug |  2 |  Terminal holes for attaching the ground cable  
---|---|---|---  
**Step 2** |  Assemble the ground cable.

  1. Use a wire-stripping tool to remove approximately 0.75 inches (19 mm) of the covering from the end of the grounding cable.
  2. Insert the stripped end of the grounding cable into the open end of the grounding lug. We recommend 6-AWG wire for the U.S. installations. Make sure to use the proper grounding cable and grounding wire as appropriate for your country or region.    
![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309378.jpg)  

  3. Use a crimping tool to secure the grounding cable in the grounding lug.
  4. Prepare the other end of the grounding cable and connect it to an appropriate ground point at the facility. 

  
**Step 3** |  Attach the ground cable to the ground lug.

  1. Position the ground cable on top of the ground lug.
  2. Align the terminal holes in the ground lug with the terminal holes in the ground bracket.
  3. Using a #2 Phillips screwdriver, insert and tighten two M5 x 10mm pan-head screws to secure the ground cable to the ground lug.  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472431.jpg)

  
**Step 4** |  Route the ground cable out of the way of the chassis, making sure not to damage the ground cable, for example, by exceeding its bend radius.   
**Step 5** |  After the chassis is connected to earth ground, connect PSU cables to power up the chassis.   
  
* * *

### Attaching Cable Management Trays

The Cisco UCS X9508 server chassis offers up to four cable management trays (UCSX-9508-CMA) to organize the cables for the intelligent fabric module (IFM) cables. The trays are interchangeable, so you can use them for either IFM's cables. There are no specific cable management trays for the top and bottom of the chassis. 

You can use one tray for each IFM installed in the Cisco UCS X9508 server chassis but Cisco recommends that you use one tray for all IFM cables. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The chassis also has cable management arms, which organize the PSU cables. The cable management arms are different from the cable management tray, which organizes IFM cables.  Because the cable management tray sits in front of an IFM , you should remove the cable management tray to allow access to the IFM. For example, if you need to access IFM 2, you should remove the cable management tray 2 

* * *  
  
---|---  
  
Cable management trays attach to the server chassis by hooks at the top rear of each tray.

![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309497.jpg)

To install or remove the cable management tray, use the following procedures:

  * Installing the Cable Management Tray

  * Removing the Cable Management Tray


  * Installing the Cable Management Tray
  * Removing the Cable Management Tray


#### Installing the Cable Management Tray

For IFM cables, you can use the cable management tray to gather and organize the cables. The tray attaches to notches in the server chassis sheet metal. 

Use the following procedure to install the cable management tray. 

##### Procedure

* * *

**Step 1** |  Orient the cable management tray so that the hooks are at the top and facing toward the chassis.   
---|---  
**Step 2** |  Attach the cable management tray to the chassis. 

  1. Align the hooks on the cable management tray with the rectangular notches in the server chassis. 
  2. Holding the cable management tray level, insert the hooks into the notches. 
  3. When the cable management tray is flush against the chassis, push down to seat the hook into the notch. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309498.jpg)

  
**Step 3** |  Repeat this procedure as needed to install the other cable management trays, if needed.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309499.jpg)  
**Step 4** |  Attach any IFM cables as needed.   
  
* * *

#### Removing the Cable Management Tray

Use the following procedure to remove the cable management tray(s). 

##### Procedure

* * *

**Step 1** |  (Optional) Remove or lift the cables to allow easier access to the cable management tray.   
---|---  
**Step 2** |  Detach the cable management tray from the chassis. 

  1. At each corner of the cable management tray, apply equal pressure to slide the tray upward in the chassis notch until it can no longer slide up.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309501.jpg)
  2. Holding the cable management tray level, pull it towards you to detach the tray from the chassis.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309502.jpg)

  
  
* * *

## Removing the Chassis from a Rack

### Procedure

* * *

**Step 1** |  Use Cisco Intersight to do the following:

  1. Shut down the OS on all nodes in the chassis.
  2. Disable the Smart Call Home feature.
  3. Decommission the chassis.

  
---|---  
**Step 2** |  Disconnect the power cords and networking cables from the chassis.  
**Step 3** |  Remove all modules, fans, power supplies, and nodes from the chassis to lighten its weight.  
**Step 4** |  Remove the screws holding the front rack-mount flange to the rack.  
**Step 5** |  With two people holding the chassis, make sure that its weight is fully supported. |  **Important** |  Watch your hands and fingers whenever you handle the chassis, modules, compute nodes, and components! Narrow vertical or horizontal spaces in situations including, but not limited to, moving the chassis into or out of the shipping container or equipment rack can cause pinch hazards for your hands and fingers.  Although they do not eliminate the possibility of pinching, the chassis has defined grasp points to facilitate handling and moving it. For information about chassis grasp points, see Handling the Chassis.   
---|---  
**Step 6** |  Gently slide the chassis off the rails, and out of the rack.  
**Step 7** |  Replace the modules, fans, power supplies, and nodes in the server chassis. If you are returning the product, go to Repacking the Chassis.   
  
* * *

## Repacking the Chassis

If you need to repack the chassis, remove it from the rack by following the steps in the Removing the Chassis from a Rack section. 

When repacking the chassis for return shipment, be aware of the following. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/warn.gif)  
**Warning** | 

* * *

Only lift an empty chassis! Make sure that all PSUs, fans, nodes, Intelligent Fabric Modules, and X-Fabric Modules are removed from the chassis before moving it out of the rack and packing it for shipment. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/warn.gif)  
**Warning** | 

* * *

When the chassis is out of the rack, make sure to install the handles onto the chassis before putting the chassis on the bottom palette. The handles are also securing brackets that bolt the chassis onto the bottom pallet. 

* * *  
  
---|---  
  
If possible, use the original packing materials and container to pack the chassis. 

If needed, you can order spare packaging from Cisco by using PID UCSX-9508-PKG=.

If you are returning the chassis to Cisco, contact your Cisco customer service representative to arrange for return shipment to Cisco. 

---

## Page 15: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x9508/install/m-installing-and-removing-components.html

# Installing and Removing Components

This chapter contains the following topics:

##  Components

The following figure shows an empty Cisco UCS X9508 server chassis and identifies the front, back, and vertical node slots, and horizontal module slots. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Before you remove or install components, please ensure that all software applications are shut down and management software is in a good state. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Whenever you remove a module from the chassis for an extended period of time, always replace the module with the appropriate blank panel. Failing to do so can result in heating and EMI issues. Blank panels can be ordered from Cisco Systems. 

* * *  
  
---|---  
Figure 1. View of Cisco UCS X9508 Server Chassis, Right Side  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308908.jpg)

The side of the chassis has no handles because the chassis is heavy, and not intended to be lifted unless you are using a scissor lift or another type of mechanical lift device to bear the weight of the chassis. The right side of the chassis has the PSU Keying Bracket which enforces proper PSU orientation as well as proper PSU type. 

Figure 2. View of UCS X9508 Server Chassis, Left Side  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308906.jpg)

The left side of the chassis has no handles.

Figure 3. View of Empty Cisco UCS X9508 Chassis, Front  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308905.jpg) 1 |  Node slots (8). Each slot is numbered horizontally below each slot.  Compute nodes and PCIe nodes can be inserted vertically and connect to the power socket for each slot.  |  2 |  PSU bays (6). Each PSU bay is numbered vertically to the right of the bay.  Each PSU bay is keyed so that the PSU inserts only one way.   
---|---|---|---  
  
The front of the chassis accepts up to 8 single-slot or 4 dual-slot compute nodes with connections for power and basic signaling through the per-slot socket connections to the midplane. The front of the server chassis also hosts up to 6 PSUs providing power to the chassis power plane through internal connectors. PSUs are numbered one through six with PSU bay one as the topmost slot and PSU bay 6 on the bottom. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Any node slot that is not occupied must have a compute node blank panel (UCSX-9508-FSBK) installed.

* * *  
  
---|---  
Figure 4. View of the UCS X9508 Server Chassis, Rear View  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308907.jpg) 1 |  Power Entry Modules (2) Each PEM houses three IEC 320 compatible C20 power inlets inlet facility power.  |  2 |  IFM slots (2)  
---|---|---|---  
3 |  Fan Bays (4) Fans are numbered 1 through 4 with fan 1 as the leftmost.  |  4 |  Expansion Slots (2)  
  
The top of the chassis rear contains up to two Intelligent Fabric Modules (IFMs). Power connections and minimal signaling are supported through the per-slot socket connections to the midplane. Three vertically stacked Power Entry Module (PEM) connectors are also supported, which correspond with PSUs one through three, with PSU one as the topmost connector. 

The middle of the chassis rear houses up to four fan modules and power is supplied through one connector per fan module. Fans are numbered from one to four with Fan 1 being the leftmost fan, and Fan 4 being the right most. 

The bottom of the chassis rear houses two active fan modules. Power connections and minimal signaling are supported through the per-slot socket connections to the midplane. Three vertically stacked PEM connectors are also supported, which correspond with PSUs four through six, with PSU four as the topmost connector. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Before you install, operate, or service the system, see the [Regulatory Compliance and Safety Information for Cisco UCS](http://www.cisco.com/en/US/docs/unified_computing/ucs/hw/regulatory/compliance/ucs_regulatory_compliance_Information.html) for important safety information. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/warn.gif)  
**Warning** | 

* * *

IMPORTANT SAFETY INSTRUCTIONS  This warning symbol means danger. You are in a situation that could cause bodily injury. Before you work on any equipment, be aware of the hazards involved with electrical circuitry and be familiar with standard practices for preventing accidents. Use the statement number provided at the end of each warning to locate its translation in the translated safety warnings that accompanied this device. Statement 1071  **SAVE THESE INSTRUCTIONS**

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/warn.gif)  
**Warning** | 

* * *

This unit is intended for installation in restricted access areas. A restricted access area can be accessed only through the use of a special tool, lock and key, or other means of security. Statement 1017 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/warn.gif)  
**Warning** | 

* * *

Only trained and qualified personnel must be allowed to install, replace, or service this equipment. Statement 1030 

* * *  
  
---|---  
  
  * Cisco UCS 9108 25G IFM Components
  * Cisco UCS 9108 100G IFM Components
  * Cisco UCS X9416 Fabric Module Components
  * Cisco UCS X9516 Fabric Module Components
  * Cisco UCS X-Fabric Module Blank Components


### Cisco UCS 9108 25G IFM Components

The Cisco UCS 9108 25G Intelligent Fabric Module has the following board-level components.

Figure 5. UCS 9108 25G Intelligent Fabric Module, Component View  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308929.jpg) 1 |  Fans (UCSX-RSFAN=), three, which are numbered 1 through 3 starting with the left fan. |  2 |  One M.2 mini storage module slot  
---|---|---|---  
3 |  SFP28 Optical Ports.  Ports are arranged in two groups of four physical ports. Port number 1 is the left port in this group, and port number 4 is the right port in the group.  |  4 |  SFP28 Optical Ports.  Ports are arranged in two groups of four physical ports. Port number 5 is the left port in this group, and port number 8 is the right port in the group.   
5 |  IFM ejector handles, left and right |  |   
  
### Cisco UCS 9108 100G IFM Components

The Cisco UCS 9108 Intelligent Fabric Module (UCS-I-9108-100G) has the following board-level components.  Figure 6. UCS 9108 100G Intelligent Fabric Module, Component View  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308930.jpg) 1 |  Fans, (UCSX-RSFAN=), three, which are numbered 1 through 3 starting with the left fan |  2 |  One M.2 mini storage module slot  
---|---|---|---  
3 |  QSFP28 Optical Ports.  Ports are arranged in two groups of four physical ports. Ports are stacked in vertical pairs, with two ports in each vertical port stack.  Port number 1 is the top port of the left port pair in this group, and port number 3 is the top port of the right port pair in the group.  |  4 |  QSFP28 Optical Ports.  Ports are arranged in two groups of four physical ports. Ports are stacked in vertical pairs, with two ports in each vertical port stack.  Port number 5 is the top port in the left port pair of this group, and port number 7 is the top port in the right port pair of the group.   
5 |  IFM ejector handles, left and right |  |   
  
### Cisco UCS X9416 Fabric Module Components

The Cisco X9416 module (UCSX-F-9416) has the following components. 

Figure 7. UCS X9416 Fabric Module, Component View  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540442.jpg) 1 |  Fans (UCSX-RSFAN=), three, which are numbered 1 through 3 starting with the left fan |  2 |  Module Ejector Handles, Left and Right  
---|---|---|---  
  
### Cisco UCS X9516 Fabric Module Components

The Cisco UCS X9516 module (UCSX-FS-9516) X-Fabric Module has the following components. 

Figure 8. UCS X9516 Fabric Module, Component View  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525956.jpg) ![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The module has multiple heatsinks, but they are not field-serviceable.

* * *  
  
---|---  
**1** |  Fans (UCSX-RSFAN=), three, which are numbered 1 through 3 starting with the left fan |  **2** |  Module Ejector Handles, Left and Right  
---|---|---|---  
**3** |  PCIe Cage 2 Supports up to one PCIe Gen5 x16 card, or a filler blank if no card is present.  For information about valid PCIe cards, see [Cisco UCS X9516 Supported PCIe Cards](m-ucsx-9508-chassis-overview.html#r-x9516-supported-pcie-cards).  |  **Note** |  The PCIe cages are not field-replaceable. If a cage becomes damaged or needs to be replaced, you must RMA the X Fabric Module  
---|---  
**4** |  PCIe Cage 1 Supports up to one PCIe Gen5 x16 card, or a filler blank if no card is present.  For information about valid PCIe cards, see [Cisco UCS X9516 Supported PCIe Cards](m-ucsx-9508-chassis-overview.html#r-x9516-supported-pcie-cards).  |  **Note** |  The PCIe cages are not field-replaceable. If a cage becomes damaged or needs to be replaced, you must RMA the X Fabric Module  
---|---  
  
### Cisco UCS X-Fabric Module Blank Components

The Cisco X-Fabric Module Blank (UCSX-9508-RBLK) has the following components. 

Figure 9. UCS X-Fabric Module Blank, Component View  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308926.jpg) 1 |  Fans (UCSX-RSFAN=), three, which are numbered 1 through 3 starting with the left fan |  2 |  Module Ejector Handles, Left and Right  
---|---|---|---  
  
## Installing and Removing a Compute Node Blank

The UCS X9508 supports up to 8 compute nodes, with a minimum configuration of one compute node. If compute node slots do not contain a compute node, you must install a compute node blank. 

Use these procedures to replace a compute node blank:

  * Installing a Compute Node Blank

  * Removing a Compute Node Blank


  * Removing a Compute Node Blank
  * Installing a Compute Node Blank


### Removing a Compute Node Blank

Do not operate the server chassis with an empty compute node slot. Fill any empty compute node slots with either a blank (UCSX-9508-FSBK) or a compute node. 

Use this task to remove a compute node blank.

#### Procedure

* * *

**Step 1** |  Grasp the compute node by the finger holds.  Figure 10. Compute Node Blanks, Installed  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308917.jpg)  
---|---  
**Step 2** |  Pull the compute node blank towards you until it is completely removed from the chassis.  Notice that the module blank has indicators that show how to orient the blank. You will use this information when you install a blank.  Figure 11. Removing a Compute Node Blank  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309103.jpg)  
  
* * *

#### What to do next

Choose the appropriate option:

  * Installing a Compute Node

  * Installing a Compute Node Blank


### Installing a Compute Node Blank

If you remove a compute node, and you will not be installing another compute node, you must install a compute node blank. Do not operate the server with an empty compute node slot. The minimum configuration is 1 installed compute node, so in this configuration you need 7 module blanks installed. 

Compute node blanks are interchangeable within the same chassis or other chassis. 

Use this task to install a compute node blank

#### Procedure

* * *

**Step 1** |  Grasp the blank by the finger holds.   
---|---  
**Step 2** |  Hold the module blank vertically and align the module blank with the slot.  |  **Note** |  The module blank has an arrow and the word UP that show how to orient the blank. Also, if you attempt to install the blank with the wrong orientation, the module does not sit flush with the front of the chassis.   
---|---  
  
. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309104.jpg)  
  
**Step 3** |  Keeping the compute node blank vertical, slide it into the slot until the blank is flush with the face of the chassis.  Figure 12. Installing a Compute Node Blank  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308917.jpg)  
  
* * *

## Installing and Removing a Compute Node

The Cisco UCS X9508 server chassis supports full-height compute nodes. For details, see the Installation and Service Note for your compute nodes. See <http://www.cisco.com/en/US/products/ps10280/prod_installation_guides_list.html>

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

When working with the compute nodes, handle them carefully to avoid damage to the modules, connectors, and pins.

* * *  
  
---|---  
  
  * Installing a Compute Node
  * Removing a Compute Node


### Installing a Compute Node

Use this task to install a compute node in an empty slot.

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

When working with the compute nodes, handle them carefully to avoid damage to the modules, connectors, and pins! Make sure that the modules are level during insertion and slide them into the chassis slowly. 

* * *  
  
---|---  
  
#### Before you begin

If there is a module blank in the slot where you want to install a compute node, remove the blank now. See Removing a Compute Node Blank. 

Compute nodes are shipped with the ejector handles closed and locked. Each compute node has a release button in the center of the node that releases the ejectors from the locked position. 

#### Procedure

* * *

**Step 1** |  Press the release button at the center of the compute node faceplate to release the ejectors. |  **Caution** |  The ejectors have a hook at the pivoting end that attaches to the compute node. While you are inserting the compute node, keep the ejectors open as shown in the following illustration. If the ejectors are not open, the hook can be an obstruction while sliding the node into the chassis.   
---|---  
**Step 2** |  Holding the compute node vertical, align it with the empty module bay in the chassis.  The compute node is correctly aligned when the server top cover is pointing to the left.  Figure 13. Aligning and Installing a Compute Node  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309120.jpg)  
**Step 3** |  Keeping the compute node vertical, slowly slide it into the chassis. As the compute node is almost completely installed, you might feel some resistance. This resistance is normal. It occurs because the connectors at the rear of the compute node contacts the connector on the inside of the chassis.  |  **Caution** |  Make sure to apply even pressure when sliding the module into the chassis. Do not push down or pull up on the module handles, and do not apply more force to one ejector handle than the other.   
---|---  
**Step 4** |  When the compute node is almost completely installed, grasp the ejector handles and arc them toward each other.  This step seats the compute node into the connector. The compute node should power up. |  **Caution** |  Make sure to apply even pressure when closing the module ejector handles! Do not push down or pull up on the module handles, and do not apply more force to one ejector handle than the other.   
---|---  
**Step 5** |  Push the ejectors until they are parallel with the face of the compute node.  When the compute node is completely installed, the retention latches at the end of each handle click into place.   
  
* * *

### Removing a Compute Node

Use this task to remove a compute node.

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

When working with the compute nodes, handle them carefully to avoid damage to the modules, connectors, and pins! Make sure that the modules are level during removal and slide them out of the chassis slowly. 

* * *  
  
---|---  
  
#### Before you begin

Do not operate the server with an empty compute node slot. If you will not be installing a compute node in an empty slot, install a compute node blank to cover the empty slot. 

#### Procedure

* * *

**Step 1** |  Press the release button at the center of the compute node faceplate to disengage the ejector handles.   
---|---  
**Step 2** |  Grasp the ejector handles and pull them outward so that they arc vertically away from each other. While moving the compute node handles, you might feel some resistance. This resistance is normal. It occurs because the connectors at the rear of the compute node are unseating from the corresponding sockets in the chassis.  Also, when the compute node disconnects from the midplane, the server powers off. Figure 14. Removing a Compute Node  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309119.jpg)  
**Step 3** |  Grasp the compute node handles and slide the compute node partially out of the chassis.  Make sure to keep the compute node vertical while removing it.  |  **Caution** |  Make sure to apply even pressure when sliding the module out of the chassis. Do not push down or pull up on the module handles, and do not apply more force to one ejector handle than the other.   
---|---  
**Step 4** |  Place your other hand underneath the compute node to support it and slide the compute node completely out of the chassis.   
  
* * *

#### What to do next

Fill the empty compute node slot. Go to the appropriate option:

  * Installing a Compute Node

  * Installing a Compute Node Blank


## Installing and Removing Power Supplies

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The power supplies are keyed to work only with their respective power expansion module (PEM), depending on the chassis version. 

* * *  
  
---|---  
  
When in installing and removing power supplies, make sure that the minimum number of power supplies are active before replacing the other PSUs. For example, in a 3+3 grid power configuration, at least 3 PSUs must be active before replacing the other 3 units one at a time per grid. 

The PSUs are installed vertically along the side of the chassis.

![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308924.jpg)

  * PSU Population Rules
  * Installing a Power Supply
  * Removing a Power Supply


### PSU Population Rules

When you install PSUs, they must be equally divided into top and bottom PSU slots to ensure redundancy. See the following PSU population rules. 

  * For 2 PSUs: Install a PSU in slots 1 and 4. This is the minimum supported config. 

  * For 3 PSUs: Install a PSU in slots 1, 2, and 4. 

  * For 4 PSUs: Install a PSU in slots 1, 2, 4, and 5. 

  * For 5 PSUs: Install a PSU in slots 1, 2, 3, 4, and 5. 

  * For 6 PSUs: Install a PSU in all slots. 


Any slots that do not contain a PSU must be covered by a PSU blank.

### Installing a Power Supply

The Cisco UCS X9508 AC PSU does not have a discrete power switch. It powers on immediately when it is successfully connected to the power midplane. When installing a PSU, you must comply with the PSU population rules. See PSU Population Rules. 

PSUs are hot swappable with a minimum population of two in the chassis to provide redundancy. PSUs are interchangeable and none are reserved through the management software. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

When connecting the chassis to facility power, make sure not to overload the capacity of a PDU or power strip. For example, do not connect all PSUs to one PDU or power strip that is not capable of carrying the total power draw of the chassis. 

* * *  
  
---|---  
  
Use the following procedure to install the PSUs.

#### Procedure

* * *

**Step 1** |  Grasp the PSU with one hand.   
---|---  
**Step 2** |  Use your other hand to support the PSU, and holding it level, orient it with the PSU bay. The PSU is correctly oriented when the latch is facing you and parallel with the right side of the PSU bay.   
**Step 3** |  Holding the PSU level, slide it into the PSU bay.  |  **Note** |  When the PSU is almost all the way in, you will feel some resistance, which is normal. The resistance is the connector at the rear of the PSU meeting the power socket inside the chassis.  The PSU will power on when you have successfully seated it in its socket.   
---|---  
Figure 15. Installing a PSU  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308923.jpg)  
**Step 4** |  For each PSU that must be installed, repeat these steps.   
**Step 5** |  Verify the power supplies are operating by checking the power supply LEDs. See [LED Locations](m-ucsx-9508-chassis-overview.html#ID499) and [Interpreting LEDs](m-ucsx-9508-chassis-overview.html#ID544).  |  **Note** |  Both grids in a power redundant system should have the same number of power supplies. If your system is configured for grid power (N+N redundancy), slots 1, 2 and 3 are assigned to grid 1, and slots 4, 5, and 6 are assigned to grid 2. If fewer than six power supplies (PS) are configured in grid redundant mode, they should be equally distributed between the grid 1 and grid 2 slots.   
---|---  
  
* * *

### Removing a Power Supply

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

If you are using the Cisco UCS X9508 server chassis with one power supply, which is a non-redundant power configuration. Removing the power supply will cause the compute nodes and chassis to shut down. If you are using more than two power supplies, and you remove one of them (the minimum supported power configuration is 3 PSUs), the servers continue to operate as long as the other power supplies are sufficient to meet the power requirements of the number of compute nodes in the chassis. 

* * *  
  
---|---  
  
The PSU has a locking latch that secures the PSU in the chassis. You must unlock the latch to remove the PSU. You can expect some resistance as the PSU slides out due to its weight. 

#### Procedure

* * *

**Step 1** |  Place your thumb on the PSU locking latch at the vertical fingerhold on the right side of the blank's faceplate and allow your other fingers to rest along the side of the chassis.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309526.jpg)  
---|---  
**Step 2** |  Press the latch to unlock the PSU, then pull until it disengages from the power socket inside the chassis.  You will feel some resistance initially as the connector at the rear of the PSU unseats from the power socket inside the chassis.   
**Step 3** |  As you slide the PSU out of the chassis, use your other hand to support the PSU.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309528.jpg)  
**Step 4** |  Install a blank power supply filler panel if the power supply bay is to remain empty.  
  
* * *

#### What to do next

Choose the appropriate option: 

  * If you will be reinstalling a PSU, go to Installing a Power Supply

  * If you will be installing a PSU blank, go to Installing a PSU Blank. 


## Replacing a PSU Blank

PSU blanks (UCSX-9508-PSUBK) are interchangeable, but if you will be operating the server chassis without a PSU, the empty bay must be covered with a PSU blank. Replace a PSU blank when you remove a PSU but will not install another PSU in that PSU bay, or when you remove a PSU blank and need to cover the empty PSU bay. 

  * Removing a PSU Blank

  * Installing a PSU Blank


  * Removing a PSU Blank
  * Installing a PSU Blank


### Removing a PSU Blank

Use this procedure to remove a PSU blank.

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The PSU blank is a small plastic piece. It does not have a locking latch, so it slides out easily. 

* * *  
  
---|---  
  
#### Procedure

* * *

**Step 1** |  Place your thumb behind the vertical fingerhold on the right side of the blank's faceplate and allow your other fingers to rest along the side of the chassis.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309526.jpg)  
---|---  
**Step 2** |  Using your thumb, grasp the PSU blank by the vertical fingerhold and pull the PSU blank straight towards you.  The PSU should easily slide out of the chassis.  Figure 16. Removing a PSU Blank  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309527.jpg)  
  
* * *

#### What to do next

Choose the appropriate option: 

  * If you are installing a PSU, go to Installing a Power Supply. 

  * If you are installing a PSU blank, go to Installing a PSU Blank. 


### Installing a PSU Blank

The minimum supported power configuration for the UCS X9508 server chassis is three PSUs. If you will be operating the server chassis with an empty PSU bay, it must be covered with a PSU blank (UCSX-9508-PSUBK). 

Use this procedure to install a PSU blank.

#### Procedure

* * *

**Step 1** |  Grasp the PSU blank by the vertical finger hold on the right side of the blank's face.  
---|---  
**Step 2** |  Align the PSU blank so that the word UP is facing up, and the handle is parallel to the right side of the PSU bay.  
**Step 3** |  Insert the PSU blank until its faceplate is flush with the front of the server chassis.  Figure 17. Inserting a PSU Blank  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308983.jpg)  
  
* * *

## Replacing the PSU Keying Bracket

The PSU Keying bracket is attached to the right exterior side of the chassis. The bracket ensures that only the correct type of PSU can be installed, and that the PSU is inserted in correct orientation in the chassis. 

Use the following procedures to replace the PSU Keying bracket:

  * Removing the PSU Keying Bracket

  * Installing the PSU Keying Bracket


  * Removing the PSU Keying Bracket
  * Installing the PSU Keying Bracket


### Removing the PSU Keying Bracket

Use this procedure to remove the PSU Keying bracket. 

#### Before you begin

The chassis must be completely removed from the rack to provide access to the exterior of the chassis where the PSU Keying bracket will be installed. 

When the chassis is removed from the rack, make sure that you place the chassis on an ESD-safe workspace, for example, a rubberized mat. 

#### Procedure

* * *

**Step 1** |  If you have not already removed the chassis from the rack, do so now.  Go to [Removing the Chassis from a Rack](m-installation.html#ID487).  |  **Caution** |  Make sure to follow all safety requirements while uninstalling the chassis, including using a device, such as a mechanical lift, to bear the weight of the chassis.   
---|---  
**Step 2** |  With the chassis in an ESD-safe work area, locate the PSU Keying bracket on the right exterior side of the chassis. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309360.jpg)  
**Step 3** |  Using a T10 screwdriver, remove the six screws that attach the bracket to the chassis.  
**Step 4** |  Grasp the PSU keying bracket and detach it from the chassis.  
**Step 5** |  Keep the screws and bracket.   
  
* * *

#### What to do next

Installing the PSU Keying Bracket. 

### Installing the PSU Keying Bracket

Use this task to install a PSU Keying bracket (UCSX-9508-KEY-AC=).

#### Procedure

* * *

**Step 1** |  With the chassis on an ESD-safe work area, grasp the new PSU Keying Bracket, and align it with right exterior side of the chassis.   
---|---  
**Step 2** |  Place the bracket against the side of the chassis, aligning the screwholes in the bracket with the screwholes in the chassis.  
**Step 3** |  Insert the 6 screws into the screwholes. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309078.jpg)  
**Step 4** |  Using a T10 screwdriver, secure the bracket to the chassis by tightening each screw to snug.  If you have access to a torque wrench, tighten the screws to 6 in-lb.  
**Step 5** |  Reinstall the chassis:

  1. Insert the chassis into the rack.
  2. Reinstall the chassis components and reconnect any cables that were disconnected. For additional info, see [Installing the Chassis](m-installation.html#ID199). 

  
  
* * *

## Replacing the Power Entry Modules (PEMs)

The Cisco UCS X9508 chassis contains two power entry modules (PEMs). Each PEM (UCSX-9508-ACPEM=) is a grouping of 3 IEC 320 compatible C20 power inlets. The top PEM supports PSUs 1 through 3, and the bottom PEM supports PSUs 4 through 6. Each PEM is field replaceable. 

Use the following procedures to replace the PEMs:

  * Installing the Power Entry Modules

  * Removing the Power Entry Modules


  * Installing the Power Entry Modules
  * Removing the Power Entry Modules


### Installing the Power Entry Modules

Use this procedure to install a PEM (UCSX-9508-ACPEM=). 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The following task shows installing both PEMs. If you are installing only one PEM, you will need to tighten only the PEM screw for the replaced PEM, not both screws as shown in the illustrations. 

* * *  
  
---|---  
  
#### Before you begin

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**DANGER** | 

* * *

Follow all electrical safety precautions when working with facility power. Failure to do so can result in damage to the equipment or pose a risk of injury or death to personnel. 

* * *  
  
---|---  
  
#### Procedure

* * *

**Step 1** |  Grasp the PEM and orient it correctly.  The PEM is keyed so that you can insert it only one way.   
---|---  
**Step 2** |  Holding the PEM level, slide it into the PEM slot.  You might feel some resistance as the connector on the rear of the PEM meets the connector on the interior of the chassis.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309106.jpg)  
**Step 3** |  Using a T10 screwdriver, tighten the captive screws which are easily identifiable because they are next to the electrical ground icons on the chassis walls. 

  1. Tighten the exterior captive screws.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309108.jpg)
  2. Tighten the interior captive screws.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309110.jpg)

  
**Step 4** |  Reinstall the IFMs and expansion modules.

  1. Go to Installing an Intelligent Fabric Module. 
  2. Go to Installing a UCS X-Fabric Module Blank. 

  
**Step 5** |  Reconnect all power cables.  The chassis automatically powers on when it receives inlet power.   
  
* * *

### Removing the Power Entry Modules

PEMs support inlet power to the chassis from the facility. It is a best practice to remove all power from the system when replacing a PEM. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**DANGER** | 

* * *

Follow all electrical safety precautions when working with facility power. Failure to do so can result in damage to equipment or pose a risk of injury or death to personnel. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The following task shows removing both PEMs. If you are removing only one PEM, you will need to loosen only the PEM screw for the replaced PEM, not both screws as shown in the illustrations. 

* * *  
  
---|---  
  
#### Before you begin

The power entry modules (PEMs, UCSX-9508-ACPEM=) are connected to facility power, so you must disconnect facility power from the PEM that you will be removing. 

#### Procedure

* * *

**Step 1** |  Power down all compute nodes.  
---|---  
**Step 2** |  Remove any power cables that are attached to the PEM.   
**Step 3** |  Remove the IFMs and expansion modules.

  1. Go to Removing an Intelligent Fabric Module. 
  2. Go to Removing a UCS X-Fabric Module Blank. 

  
**Step 4** |  Using a T10 screwdriver, loosen the captive screws that attach the PEM to the chassis.  The captive screws are easily identifiable because they are next to the electrical ground icons on the chassis walls. 

  1. Loosen the exterior captive screws. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309107.jpg)
  2. Loosen the interior captive screws. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309109.jpg)

  
**Step 5** |  Grasp the PEM and slide it out of the chassis.  When you remove a PEM, you must replace it with another one. Do not operate the system with an empty PEM slot. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309105.jpg)  
  
* * *

#### What to do next

Install a PEM. Go to Installing the Power Entry Modules. 

## Installing and Removing a Fan Module

You can hot swap a 100 mm chassis fan module (UCSX-9508-FAN) without causing an electrical hazard or damage to the system. However, you can only remove one fan module at a time while the system is operating. Removing more than one fan module could cause overheating. 

  * Fan Module Replacement Consideration
  * Installing a Fan Module
  * Removing a Fan Module


### Fan Module Replacement Consideration

While a fan module is absent from the chassis, the pair of compute nodes physically associated with that fan may be throttled to prevent thermal overload. After the fan module is replaced in the chassis, throttling is removed and the associated blades resume normal operation. 

To minimize the impact to system performance, do not remove a fan module until a replacement fan module is available. When replacing a fan module, you must insert a new fan in less than one minute after removing the old fan. Leaving the fan module out of the chassis for longer durations of time will result in power throttling of the associated compute nodes. In extreme cases, the compute nodes might shutdown. 

The following table shows the mapping of fan modules to their associated compute nodes.

Fan Module |  Compute Node Slots  
---|---  
1 |  7, 8  
2 |  5, 6  
3 |  3, 4  
4 |  1, 2  
  
### Installing a Fan Module

#### Procedure

* * *

**Step 1** |  Hold the chassis fan module (UCSX-9508-FAN) with the handle at the bottom and place your other hand underneath the fan module to support it.   
---|---  
**Step 2** |  Align the fan with the fan bay in the rear of the chassis.  Figure 18. Aligning the Fan Module  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309077.jpg)  
**Step 3** |  Slide the fan into the chassis until it is flush with the face of the chassis.  |  **Note** |  Make sure that the latch on the handle is engaged with the chassis.  
---|---  
  
When the fan module is almost completely installed, you might feel some resistance. The resistance is normal, and it occurs when the connector at the rear of the fan contacts the corresponding socket inside the chassis. 

Figure 19. Seating the Fan into the Chassis  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308912.jpg)  
**Step 4** |  Listen for the fan to power up and verify that the LED behavior is as expected. See [LED Locations](m-ucsx-9508-chassis-overview.html#ID499) and [Interpreting LEDs](m-ucsx-9508-chassis-overview.html#ID544).   
  
* * *

### Removing a Fan Module

#### Before you begin

Removing a chassis fan module (UCSX-9508-FAN) can cause throttling of the compute nodes associated with that fan. When replacing a fan, you must insert a new fan in less than one minute after removing the old fan. You will find it helpful to have the replacement fan ready before attempting fan replacement. For more information, see Fan Module Replacement Consideration. 

#### Procedure

* * *

**Step 1** |  Grasp the chassis fan module handle and push down on the release button.  Figure 20. Disengaging the Fan Module  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308912.jpg)  
---|---  
**Step 2** |  Slide the fan module partially out of the chassis and place your hand underneath it to support it.  When the fan disconnects from the midplane, it will power down.   
**Step 3** |  Slide the fan completely out of the chassis, making sure to support its weight with your other hand.  |  **Caution** |  The fan module is relatively heavy! Do not attempt to handle or carry it by only its handle. Instead, make sure support the fan's weight with your other hand.  Figure 21. Removing the Fan Module  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308911.jpg)  
---|---  
  
* * *

#### What to do next

Insert a fan module. Go to Installing a Fan Module. 

## Installing and Removing a Rear Module's Fan

The Cisco UCS X9508 Intelligent Fabric Module (IFM) and X-Fabric Module (XFM) blanks use the same 40 mm fan (UCSX-RSFAN=), which makes the fans interchangeable between these modules and module blanks. In a typical configuration, there are three fans numbered from one to three. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The fans for IFM and XFMs (UCSX-RSFAN=) are different from the 100 mm chassis fan modules (UCSX-9508-FAN=) that provide cooling and ventilation for the entire server chassis. These two types of fans are not interchangeable. 

* * *  
  
---|---  
  
Use the following procedures to replace a fan on a Cisco UCS X9508 module or module blank. 

  * Installing a Fan for a UCS Intelligent Fabric Module (IFM) or X-Fabric Module (XFM) Blank

  * Removing a Fan for a UCS Intelligent Fabric Module (IFM) or X-Fabric Module (XFM) Blank


  * Installing a Fan for a UCS Intelligent Fabric Module (IFM) or X-Fabric Module (XFM) Blank
  * Removing a Fan for a UCS Intelligent Fabric Module (IFM) or X-Fabric Module (XFM) Blank


### Installing a Fan for a UCS Intelligent Fabric Module (IFM) or X-Fabric Module (XFM) Blank 

Use this task to install the fan (UCSX-RSFAN=) for a UCS Intelligent Fabric Module (IFM) or X-Fabric Module (XFM) Blank. 

#### Procedure

* * *

**Step 1** |  Align the fan correctly.

  1. Align the power connector on the replacement fan with power connector on the board.
  2. Align the guides on long fan side walls with the corresponding cutouts on the module. Figure 22. Aligning the Fan  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308954.jpg)

  
---|---  
**Step 2** |  Press down evenly on the fan until it is fully seated. Make sure the fan is level while you're installing it. You will feel the fan click into place when it is correctly seated on the module or module blank.   
  
* * *

### Removing a Fan for a UCS Intelligent Fabric Module (IFM) or X-Fabric Module (XFM) Blank 

Use the following procedure for removing a fan (UCSX-RSFAN=) from a UCS Intelligent Fabric Module (IFM) or X-Fabric Module (XFM) Blank. 

#### Procedure

* * *

**Step 1** |  Grasp the fan by the tabs on each long side wall.   
---|---  
**Step 2** |  Pull the fan straight up. This step disconnects the fan from the power connector and lifts the fan off of the board. Figure 23. Removing the Fan from a UCS X9508 Module or Module Blank  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309543.jpg)  
  
* * *

#### What to do next

Insert a fan module. Go to Installing a Fan for a UCS Intelligent Fabric Module (IFM) or X-Fabric Module (XFM) Blank. 

## Installing and Removing an Intelligent Fabric Module

Intelligent Fabric Modules (IFMs) install in the rear of the chassis. They are always deployed in pairs, and the minimum IFM configuration for each UCS X9508 is two. For more information, see [Intelligent Fabric Modules](m-ucsx-9508-chassis-overview.html#Cisco_Concept.dita_db0ed713-8b40-439d-aa83-c8a1e91020a5). 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

When working with the IFMs, handle them carefully to avoid damage to the modules, connectors, and pins.

* * *  
  
---|---  
  
Use the following procedures to replace an IFM:

  * Installing an Intelligent Fabric Module

  * Removing an Intelligent Fabric Module


  * Installing an Intelligent Fabric Module
  * Removing an Intelligent Fabric Module


### Installing an Intelligent Fabric Module

Intelligent Fabric Modules (IFM) must be deployed in pairs, so there are no IFM module blanks that can be installed. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

When working with the IFMs, handle them carefully to avoid damage to the modules, connectors, and pins! Make sure that the modules are level during insertion and slide them into the chassis slowly. 

* * *  
  
---|---  
  
#### Procedure

* * *

**Step 1** |  If the IFM has a cable management tray, remove it.  See [Removing the Cable Management Tray](m-installation.html#Cisco_Task_in_List_GUI.dita_377c830e-a9c3-4cf8-b274-2a3d166bd736).   
---|---  
**Step 2** |  Swing the ejector handles to the open position.   
**Step 3** |  Placing one hand underneath the IFM, align the module with the empty IFM slot on the rear of the chassis. Figure 24. Aligning the Intelligent Fabric Module  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308915.jpg)  
**Step 4** |  Holding the IFM level, slide it almost all the way into the chassis until you feel some resistance.  This resistance is normal. It occurs when the connectors at the rear of the IFM contact the socket inside the chassis.  |  **Caution** |  Make sure to apply even pressure when sliding the module into the chassis. Do not push down or pull up on the module handles, and do not apply more force to one ejector handle than the other.   
---|---  
**Step 5** |  Grasp each of the ejector handles, and keeping them level, slowly arc them inward toward the chassis. This step seats the IFM connectors into the sockets on the midplane.  |  **Caution** |  Make sure to apply even pressure when closing the module ejector handles! Do not push down or pull up on the module handles, and do not apply more force to one ejector handle than the other.   
---|---  
**Step 6** |  Push the ejector handles until both are parallel with the face of the IFM.  Make sure the ejector latch is fully inserted in the front panel  
**Step 7** |  If the IFM has a cable management tray, attach it.  See [Installing the Cable Management Tray](m-installation.html#Cisco_Task_in_List_GUI.dita_77a99c2e-2c25-4fd0-afa6-596b075668c8).   
  
* * *

### Removing an Intelligent Fabric Module

Intelligent Fabric Modules (IFM) must be deployed in pairs, so when you remove one, you must insert another IFM in its place. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

When working with the IFMs, handle them carefully to avoid damage to the modules, connectors, and pins! Make sure that the modules are level during removal and slide them out of the chassis slowly. 

* * *  
  
---|---  
  
#### Procedure

* * *

**Step 1** |  If the IFM has a cable management tray, remove it. See [Removing the Cable Management Tray](m-installation.html#Cisco_Task_in_List_GUI.dita_377c830e-a9c3-4cf8-b274-2a3d166bd736).   
---|---  
**Step 2** |  Using your fingers, pinch the interior end of both handles to disengage the ejector latch. This step unlocks the module handles so that they can move.  Figure 25. Opening the Module Handles  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308916.jpg)  
**Step 3** |  Keeping the modules handles level, pull them towards you so that they arc away from the chassis.  You might feel some resistance as the IFM disconnects from the socket inside the chassis.   
**Step 4** |  Slide the module about halfway out of the chassis, then place your other hand underneath the IFM to support it. |  **Caution** |  Make sure to apply even pressure when sliding the module out of the chassis. Do not push down or pull up on the module handles, and do not apply more force to one ejector handle than the other.   
---|---  
**Step 5** |  Continue sliding the IFM out of the chassis until it is completely removed.  Figure 26. Removing an Intelligent Fabric Module  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308984.jpg)  
  
* * *

#### What to do next

Insert an IFM. Go to Installing an Intelligent Fabric Module

## Installing and Removing an X-Fabric Module

X-Fabric Modules are required when the UCS X9508 chassis contains one or more pairs of X-Series compute nodes and X-Series PCIe Nodes. For more information, see [X-Fabric Modules](m-ucsx-9508-chassis-overview.html#Cisco_Concept.dita_44aedf58-a967-49a2-ab8d-846770a6b57a). 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Because both XFMs connect to all slots on the front of the server chassis, all pairs of compute nodes and PCIe nodes must be powered off before removing or inserting XFMs. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Although the Cisco UCS X-Fabric Modules can be removed, it is a best practice to leave them installed even during chassis installation. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

To ensure graceful/non-disruptive replacement of X-Fabric Modules, use your Cisco management tool, such as Cisco Intersight, to properly deactivate any profiles before removing the XFMs. 

* * *  
  
---|---  
  
Use the following procedures to install or remove a UCS X9416 or X9516 X-Fabric Module. 

  * Removing an X-Fabric Module

  * Installing an X-Fabric Module


For a UCS X9516 X-Fabric Module, also use the following procedures to install or remove the module's network adapters. 

  * Replacement Guidelines and Considerations for Cisco UCS X9516 X-Fabric Modules

  * Removing a PCIe Card from a UCS X9516 X-Fabric Module PCIe Cage

  * Removing a PCIe Filler Panel from a UCS X9516 X Fabric Module

  * Installing a PCIe Card into a UCS X9516 X-Fabric Module PCIe Cage

  * Installing a PCIe Filler Panel in a UCS X9516 X- Fabric Module


  * Removing an X-Fabric Module
  * Installing an X-Fabric Module
  * Replacement Guidelines and Considerations for Cisco UCS X9516 X-Fabric Modules
  * Removing a PCIe Card from a UCS X9516 X-Fabric Module PCIe Cage
  * Removing a PCIe Filler Panel from a UCS X9516 X Fabric Module
  * Installing a PCIe Card into a UCS X9516 X-Fabric Module PCIe Cage
  * Installing a PCIe Filler Panel in a UCS X9516 X- Fabric Module


### Removing an X-Fabric Module

Use the following procedure to remove a Cisco UCS X-Fabric Module.

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

When working with the XFMs, handle them carefully to avoid damage to the modules, connectors, and pins! Make sure that the modules are level during removal and slide them out of the chassis slowly. 

* * *  
  
---|---  
  
#### Before you begin

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Make sure that all pairs of compute nodes and PCIe nodes are completely powered off before removing an X-Fabric Module (XFM).

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

To ensure graceful/non-disruptive replacement of X-Fabric Modules, use your Cisco management tool, such as Cisco Intersight, to properly deactivate any profiles before removing the XFMs. 

* * *  
  
---|---  
  
#### Procedure

* * *

**Step 1** |  Using your fingers, pinch the interior end of both handles to disengage the ejector latch. This step unlocks the module handles so that they can move.   
---|---  
**Step 2** |  Keeping the modules handles level, pull them towards you so that they arc away from the chassis.  |  **Caution** |  Make sure to apply even pressure when sliding the module out of the chassis. Do not push down or pull up on the module handles, and do not apply more force to one ejector handle than the other.   
---|---  
  
You might feel some resistance as the module disconnects from the socket inside the chassis. 

Figure 27. Opening the Module Ejector Handles  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540772.jpg)  
**Step 3** |  Keeping the module level, slowly slide the module about halfway out of the chassis, then place your other hand underneath the module to support it.   
**Step 4** |  Continue sliding the module out of the chassis until it is completely removed.  Figure 28. Removing an X-Fabric Module  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540774.jpg)  
  
* * *

#### What to do next

Insert an X-Fabric Module. Go to Installing an X-Fabric Module

### Installing an X-Fabric Module

Use the following procedure to install a Cisco UCS X-Fabric Module. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

When working with the XFMs, handle them carefully to avoid damage to the modules, connectors, and pins! Make sure that the modules are level during installation and slide them into of the chassis slowly. 

* * *  
  
---|---  
  
#### Before you begin

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Make sure that all pairs of compute nodes and PCIe nodes are completely powered off before inserting XFMs.

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

After installing X-Fabric Modules, use your Cisco management tool, such as Cisco Intersight, to properly activate any profiles that include the XFMs. 

* * *  
  
---|---  
  
#### Procedure

* * *

**Step 1** |  Swing the ejector handles to the open position.   
---|---  
**Step 2** |  Placing one hand underneath the module, align the module with the empty module slot on the rear of the chassis. Figure 29. Installing an X-Fabric Module  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540773.jpg)  
**Step 3** |  Holding the module level, slowly slide it almost all the way into the chassis until you feel some resistance.  This resistance is normal. It occurs when the connectors at the rear of the module contact the socket inside the chassis.  |  **Caution** |  Make sure to apply even pressure when sliding the module into the chassis. Do not push down or pull up on the module handles, and do not apply more force to one ejector handle than the other.   
---|---  
**Step 4** |  Grasp each of the ejector handles, and keeping them level, arc them inward toward the chassis. This step seats the module connectors into the sockets on the midplane.  |  **Caution** |  Make sure to apply even pressure when closing the module ejector handles! Do not push down or pull up on the module handles, and do not apply more force to one ejector handle than the other.   
---|---  
**Step 5** |  Push the ejector handles until both are parallel with the face of the module.  Make sure the ejector latch is fully inserted in the front panel  
  
* * *

### Replacement Guidelines and Considerations for Cisco UCS X9516 X-Fabric Modules 

When replacing PCIe cages or cards, be aware of the following.

#### PCIe Cage Considerations and Guidelines

  * PCIe cages for the Cisco UCS X9516 X-Fabric Module are interchangeable. You can install either cage in slot 1 or slot 2 of the XFM. 

  * Individual PCIe cages are not field-serviceable. The only supported workflows for removing or installing a PCIe cage is to remove or install the network adapter (such as the ConnectX-7 NIC) or for product recycling. Be careful when handling PCIe cages! Because they are not field-replaceable, the entire XFM must be replaced if a PCIe cage becomes damaged. 

  * PCIe cages have alignment features consisting of guide pins that meet guide holes on each cage and a metal tab on the side of the cage near the front panel (not shown in the following illustration). These alignment features key the cages so that they ensure proper alignment with securing screws and prevent incorrect installation. You will find it helpful to know the locations of these features on the cage and the XFM itself. 

![](/c/dam/en/us/td/i/400001-500000/490001-500000/490001-491000/490996.jpg) **1** |  Guide pin on motherboard and guide hole (PCIe Cage 2).  
---|---  
**2** |  Guide pin on motherboard and guide hole (PCIe Cage 1).  
**3** |  Threaded standoff for thumbscrew (PCIe Cage 1)  
**4** |  Threaded standoff for thumbscrew (PCIe Cage 2)  
  * Both PCIe cages must be installed during normal operation. To ensure proper airflow and to minimize the amount of airborne particulates, do not operate the XFM with an empty PCIe Cage slot. 

  * Take care to keep a PCIe Cage horizontal while removing or installing it. Tipping, twisting, or rotating the cage during removal or installation increases the chance of damaging the cage's PCIe connector (golden fingers) or the XFM motherboard's PCIe socket. 


#### PCIe Card Considerations and Guidelines

  * When handling a PCIe card, always use safe ESD handling practices. 

  * Third-party PCIe cards can be installed in one, or both of the XFM's PCI cages. Although not a requirement, it is a best practice to install a PCIe card in PCIe Cage 1 if only one PCIe card is required for your deployment. 

  * Third-party PCIe cards have typical alignment features consisting of beveled tab that inserts into a slot inside the PCIe cage and a right angle tab on the card's faceplate. The XFM PCIe cage is designed to accept cards with these features. You will find it helpful to familiarize yourself with these PCIe card features and how they mate with the appropriate locations on each PCIe cage. 

  * If your deployment requires only one PCIe card, you must install a PCIe card blank (bracket). To ensure proper airflow and to minimize the amount of airborne particulates, do not operate the XFM with an uncovered PCIe card slot. 

  * Take care to keep a PCIe card horizontal while removing or installing it. Tipping, twisting, or rotating the card during removal or installation increases the chance of damaging the PCIe connector (golden fingers) on the card or the PCIe socket inside the PCIe cage. 

  * The Cisco UCS X9516 X Fabric Module has the following operational temperatures which differ depending on the network adapter installed: 

  * With ConnectX7 1x400G cards installed, the module's maximum supported ambient temperature is 82.4° F (28° C)

  * With ConnectX7 2x200G cards installed, the module's maximum supported ambient temperature is 86° F (30° C)


### Removing a PCIe Card from a UCS X9516 X-Fabric Module PCIe Cage

The UCS X9516 X-Fabric Module offers two PCIe Cages that support PCIe Cards, such as NVIDIA ConnectX-7 NICs. Each PCIe Cage (numbered 1 and 2, as indicated on the faceplate of the XFM) contains up to one network adapter. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

As part of this procedure, you will remove the PCIe cage from the XFM. Individual PCIe cages are not field-replaceable, so handle them carefully, especially when removing or installing them. If the cage or its connectors are damaged, you must RMA the entire XFM. 

* * *  
  
---|---  
  
Use this task to remove a PCIe card from the UCS X9516 XFM.

#### Before you begin

Before attempting this task, gather a #2 Phillips screwdriver. 

You will find it helpful to read Replacement Guidelines and Considerations for Cisco UCS X9516 X-Fabric Modules before attempting this task. 

#### Procedure

* * *

**Step 1** |  If you have not already removed the XFM from the chassis, do so now.  See Removing an X-Fabric Module.   
---|---  
**Step 2** |  If you have not already removed the X-Fabric Module's top cover, do so now. 

  1. Press and hold the release button down. 
  2. While holding the release button down, slide the top cover toward the rear of the module.  This step frees the catch pins on the top cover from the retaining grooves on the top of the XFM's side walls. 
  3. Lift the top cover up to remove it from the XFM. 

  
**Step 3** |  Loosen the screws.

  1. Using the #2 Phillips screwdriver, loosen two thumbscrews on the XFM faceplate.  ![](/c/dam/en/us/td/i/400001-500000/490001-500000/490001-491000/490997.jpg)
  2. Using the screwdriver, loosen the thumbscrews on the PCIe cage.  ![](/c/dam/en/us/td/i/400001-500000/490001-500000/490001-491000/490998.jpg)

  
**Step 4** |  Grasping both the front and rear edges of the PCIe cage, keep the PCIe cage level while lifting it off of the XFM.  |  **Caution** |  **_Do not tip, twist, or rotate the PCIe cage while removing it!_** Failure to keep the PCIe cage while removing it can cause damage to the connector.   
---|---  
![](/c/dam/en/us/td/i/400001-500000/490001-500000/490001-491000/490999.jpg)  
**Step 5** |  Place the PCIe Cage on an ESD-safe surface while you work on it.  
**Step 6** |  Open the PCIe Cage.

  1. Using the screwdriver, loosen the captive screw.
  2. Swing the PCIe Cage door open.  ![](/c/dam/en/us/td/i/400001-500000/490001-500000/491001-492000/491003.jpg)

  
**Step 7** |  Grasp the front and rear edges of the PCIe card, and holding it level, pull it straight out of the PCIe cage.  |  **Caution** |  **_Do not tip, twist, or rotate the PCIe card while removing it!_** Failure to keep the PCIe card level while removing it can cause damage to the card's connector or cage's socket.   
---|---  
  
![](/c/dam/en/us/td/i/400001-500000/490001-500000/491001-492000/491004.jpg)  
  
* * *

#### What to do next

Insert a NIC card and reinstall the PCIe cage onto the UCS X9516 X-Fabric Module. 

See Installing a PCIe Card into a UCS X9516 X-Fabric Module PCIe Cage. 

### Removing a PCIe Filler Panel from a UCS X9516 X Fabric Module

Use this procedure to remove a filler blank from the PCIe card slot, when needed.

#### Before you begin

Before attempting this task, gather a #2 Phillips screwdriver. 

You will find it helpful to read Replacement Guidelines and Considerations for Cisco UCS X9516 X-Fabric Modules before attempting this task. 

#### Procedure

* * *

**Step 1** |  If you have not already removed the XFM from the chassis, do so now.  See Removing an X-Fabric Module.   
---|---  
**Step 2** |  If you have not already removed the X-Fabric Module's top cover, do so now. 

  1. Press and hold the release button down. 
  2. While holding the release button down, slide the top cover toward the rear of the module.  This step frees the catch pins on the top cover from the retaining grooves on the top of the XFM's side walls. 
  3. Lift the top cover up to remove it from the XFM. 

  
**Step 3** |  Loosen the screws.

  1. Using the #2 Phillips screwdriver, loosen two thumbscrews on the XFM faceplate.  ![](/c/dam/en/us/td/i/400001-500000/490001-500000/493001-494000/493121.jpg)
  2. Using the screwdriver, loosen the thumbscrews on the PCIe cages.  ![](/c/dam/en/us/td/i/400001-500000/490001-500000/493001-494000/493122.jpg)

  
**Step 4** |  Grasping both the front and rear edges of the PCIe cage, keep the PCIe cage level while lifting it off of the XFM.  |  **Caution** |  **_Do not tip, twist, or rotate the PCIe cage while removing it!_** Failure to keep the PCIe cage while removing it can cause damage to the connector.   
---|---  
![](/c/dam/en/us/td/i/400001-500000/490001-500000/493001-494000/493123.jpg)  
**Step 5** |  Place the PCIe Cage on an ESD-safe surface while you work on it.  
**Step 6** |  Open the PCIe cage.

  1. Using the screwdriver, loosen the captive screw.
  2. Swing the PCIe Cage door open. 

  
**Step 7** |  Grasp the front edge of the filler panel, and holding it level, pull it straight out of the PCIe cage.  ![](/c/dam/en/us/td/i/400001-500000/490001-500000/493001-494000/493120.jpg)  
  
* * *

### Installing a PCIe Card into a UCS X9516 X-Fabric Module PCIe Cage

Use the following task to install a PCIe cage onto a Cisco UCS X9516 X-Fabric Module. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

As part of this procedure, you will install the PCIe cage onto the XFM. Be careful when doing so. PCIe cages are not field-replaceable. If the PCIe cage or connectors are damaged, you must RMA the entire XFM. 

* * *  
  
---|---  
  
#### Before you begin

Before attempting this procedure, gather a #2 Phillips torque driver. 

You will find it helpful to read Replacement Guidelines and Considerations for Cisco UCS X9516 X-Fabric Modules before attempting this task. 

#### Procedure

* * *

**Step 1** |  Orient the PCIe card so that the connector and the PCIe socket inside the PCIe cage are in plane with each other.   
---|---  
**Step 2** |  Holding the PCIe card level, slide it into the PCIe cage making sure that the beveled tag inserts into the slot inside the cage.  ![](/c/dam/en/us/td/i/400001-500000/490001-500000/491001-492000/491005.jpg)  
**Step 3** |  Press firmly to fully seat the card's connector into the PCIe socket inside the PCIe cage.   
**Step 4** |  Swing the PCIe cage door closed, making sure that the door closes completely and sits flush against the cage.  ![](/c/dam/en/us/td/i/400001-500000/490001-500000/491001-492000/491006.jpg)  
**Step 5** |  Using the screwdriver, tighten the captive screw to secure the door to the PCIe cage. |  **Caution** |  Do not overtighten the thumbscrews! Make sure to tighten them to finger-tight only or you risk stripping them.  
---|---  
  
![](/c/dam/en/us/td/i/400001-500000/490001-500000/491001-492000/491007.jpg)  
  
**Step 6** |  Attach the PCIe Cage to the XFM. 

  1. Locate the guide pins, threaded standoff for the thumbscrews, and the PCIe socket on the XFM. 
  2. Holding the PCIe Cage level, lower it onto the XFM so that the PCIe connector on the cage seats into the socket on the XFM.  |  **Caution** |  **_Do not tip, twist, or rotate the PCIe cage while installing it!_** Failure to keep the PCIe cage while removing it can cause damage to the PCIe connector.   
---|---  
  
![](/c/dam/en/us/td/i/400001-500000/490001-500000/490001-491000/491000.jpg)


  
**Step 7** |  Using the screwdriver, tighten the thumbscrews on the XFM. ![](/c/dam/en/us/td/i/400001-500000/490001-500000/491001-492000/491001.jpg)  
**Step 8** |  Using the screwdriver, tighten the thumbscrews on the XFM's faceplate. ![](/c/dam/en/us/td/i/400001-500000/490001-500000/491001-492000/491002.jpg)  
**Step 9** |  Attach the top cover of the X Fabric Module. 

  1. Lay the top cover on the XFM.
  2. Slide it forward, making sure that the pins on the underside of the top cover meet the grooves on the top of the XFM's sidewalls. 
  3. Making sure that the leading edge of the top cover slides under the front of the XFM, seat the top cover until it clicks into place. 

  
**Step 10** |  Insert the XFM into the chassis.  See Installing an X-Fabric Module.   
  
* * *

### Installing a PCIe Filler Panel in a UCS X9516 X- Fabric Module

Use this task to install a filler panel in the PCIe card slot, when needed. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Do not operate the system without a filler panel or PCIe card installed. 

* * *  
  
---|---  
  
#### Before you begin

Before attempting this procedure, gather a #2 Phillips screwdriver. 

You will find it helpful to read Replacement Guidelines and Considerations for Cisco UCS X9516 X-Fabric Modules before attempting this task. 

#### Procedure

* * *

**Step 1** |  If you have not already loosened the screw and opened the PCIe cage door, do so now.   
---|---  
**Step 2** |  Orient the filler panel so that the tabbed end of the filler panel lines up with the slot inside the PCIe cage.   
**Step 3** |  Holding the filler panel level, slide it into the PCIe cage making sure that the beveled tab inserts into the slot inside the cage.  ![](/c/dam/en/us/td/i/400001-500000/490001-500000/493001-494000/493119.jpg)  
**Step 4** |  Swing the PCIe cage door closed, making sure that the door closes completely and sits flush against the cage.  
**Step 5** |  Using the screwdriver, tighten the captive screw to secure the door to the PCIe cage. |  **Caution** |  Do not overtighten the thumbscrews! Make sure to tighten them to finger-tight only or you risk stripping them.  
---|---  
**Step 6** |  Attach the PCIe Cage to the XFM. 

  1. Locate the guide pins, threaded standoff for the thumbscrews, and the PCIe socket on the XFM (1). 
  2. Holding the PCIe Cage level, lower it onto the XFM so that the PCIe connector on the cage seats into the socket on the XFM (2).  |  **Caution** |  **_Do not tip, twist, or rotate the PCIe cage while installing it!_** Failure to keep the PCIe cage while removing it can cause damage to the PCIe connector.   
---|---  
  
![](/c/dam/en/us/td/i/400001-500000/490001-500000/493001-494000/493124.jpg)


  
**Step 7** |  Using the screwdriver, tighten the thumbscrews on the XFM. ![](/c/dam/en/us/td/i/400001-500000/490001-500000/493001-494000/493122.jpg)  
**Step 8** |  Using the screwdriver, tighten the thumbscrews on the XFM's faceplate. ![](/c/dam/en/us/td/i/400001-500000/490001-500000/493001-494000/493121.jpg)  
**Step 9** |  Attach the top cover of the X Fabric Module. 

  1. Lay the top cover on the XFM.
  2. Slide it forward, making sure that the pins on the underside of the top cover meet the grooves on the top of the XFM's sidewalls. 
  3. Making sure that the leading edge of the top cover slides under the front of the XFM, seat the top cover until it clicks into place. 

  
  
* * *

## Installing and Removing the UCS X-Fabric Module Blank

The UCS X-Fabric Module Blank (UCSX-9508-RBLK) is a filler module for the expansion slots on the bottom of the chassis rear. For more information, see [Cisco UCS X-Fabric Module Blanks](m-ucsx-9508-chassis-overview.html#Cisco_Concept.dita_0691f606-292d-47a3-a279-288591a892a9). 

Use the following procedures to replace the UCSX-9508-RBLK. 

  * Installing a UCS X-Fabric Module Blank

  * Removing a UCS X-Fabric Module Blank


  * Installing a UCS X-Fabric Module Blank
  * Removing a UCS X-Fabric Module Blank


### Installing a UCS X-Fabric Module Blank

Use this procedure to install an UCS X-Fabric Module Blank in the bottom two slots in the chassis rear. These module blanks must be deployed in pairs and must be installed. You cannot operate the server chassis with empty IOM bays. 

#### Procedure

* * *

**Step 1** |  Placing one hand underneath the blank, align it with the empty slot at the bottom of the rear of the chassis.  
---|---  
**Step 2** |  Holding the blank level, slowly slide it all the way into the chassis until the blank stops.  |  **Caution** |  Make sure to apply even pressure when sliding the module into the chassis. Do not push down or pull up on the module handles, and do not apply more force to one ejector handle than the other.   
---|---  
**Step 3** |  Grasp each of the module handles, and keeping them level, arc them inward toward the chassis. This step seats the blank connectors into the sockets on the midplane.  |  **Caution** |  Make sure to apply even pressure when closing the module ejector handles! Do not push down or pull up on the module handles, and do not apply more force to one ejector handle than the other.   
---|---  
**Step 4** |  Push the module handles until both are parallel with the face of the blank.  The fan modules on the blank will power up when the module is completely seated.   
  
* * *

### Removing a UCS X-Fabric Module Blank

Use this task to remove a UCS X-Fabric Module Blank (UCSX-9508-BLK). 

#### Procedure

* * *

**Step 1** |  Using your fingers, pinch the interior end of both handles to disengage the retention clip. This step unlocks the module handles so that they can move.   
---|---  
**Step 2** |  Keeping the modules handles level, pull them towards you so that they arc away from the chassis.  |  **Caution** |  Make sure to apply even pressure when sliding the blank out of the chassis. Do not push down or pull up on the module handles, and do not apply more force to one ejector handle than the other.   
---|---  
**Step 3** |  Slowly slide the blank about halfway out of the chassis, then place your other hand underneath the blank to support it.  
**Step 4** |  Continue sliding the blank out of the chassis until it is completely removed.   
**Step 5** |  Reinsert a UCS X-Fabric Module blank (UCSX-9508-RBLK).  
  
* * *

#### What to do next

Installing a UCS X-Fabric Module Blank

## Recycling Printed Circuit Boards

The Cisco UCS X9508 and some of its modules have printed circuit boards (PCBs) that must be disposed of in compliance with your appropriate recycling and e-waste regulations, including, but not limited to Commission Regulation (EU) 2019/424. 

The following procedures are not standard field-service options. They should be used only by certified or approved recyclers.

  * Recycling the UCS 9108 25G IFM PCBs

  * Recycling the UCS 9108 100G IFM PCBs

  * Recycling the Chassis PCB Assembly (PCBA)


  * Recycling the Chassis PCB Assembly (PCBA)
  * Recycling the UCS 9108 25G IFM PCBs
  * Recycling the UCS 9108 100G IFM PCBs
  * Recycling a UCS X9416 X-Fabric Module PCB
  * Recycling a UCS X9516 X-Fabric Module PCB
  * Recycling X-Fabric Module Blank PCBs


### Recycling the Chassis PCB Assembly (PCBA)

Each Cisco UCS X9508 chassis has a PCBA (motherboard) that is connected to the chassis midplane sheet metal. You must disconnect the PCBA from the chassis sheet metal to recycle the PCBA. Each PCBA is attached to the midplane sheet metal by 19 M4 screws. You will need to disassemble and remove additional parts to gain access to the PCBA. 

You will need to recycle the PCBA for each UCS X9508 chassis.

Use the following procedure to recycle the Cisco UCS X9508 motherboard.

#### Before you begin

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

**For Recyclers Only!** This procedure is not a standard field-service option. This procedure is for recyclers who will be reclaiming the electronics and sheet metal for proper disposal to comply with local eco design and e-waste regulations. 

* * *  
  
---|---  
  
To remove the chassis printed circuit board assembly (PCBA), the following requirements must be met:

  * The chassis must be disconnected from facility power.

  * The chassis must have all compute nodes and IFMs removed. If they are not removed, remove them now. Go to:

  * Removing a Compute Node

  * Removing an Intelligent Fabric Module

  * The chassis must be removed from the equipment rack.


You will find it helpful to gather a T10, T15, and T20 screwdriver before beginning this procedure.

#### Procedure

* * *

**Step 1** |  At the rear of the chassis, remove the fan modules.  See Removing a Fan Module.   
---|---  
**Step 2** |  On the left side of the chassis, use a T10 screwdriver to remove 14 M4 screws.  Figure 30. Cisco UCS X9508 Chassis, Left Side  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309213.jpg)  
**Step 3** |  On the right side of the chassis, use a T10 screwdriver to remove 14 M4 screws plus the two captive M3 screws for the PEMs.  Figure 31. Cisco UCS X9508 Chassis, Right Side  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309214.jpg)  
**Step 4** |  On the top of the chassis, use a T10 screwdriver to remove the eight M4 screws.  Figure 32. Cisco UCS X9508 Chassis, Top  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309216.jpg)  
**Step 5** |  Remove the PEMs.

  1. On the interior of the chassis, use the T10 screwdriver to remove the two M3 captive screws for the PEMs, which are indicated by the ground symbol (![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309215.jpg)). 
  2. When the screws are removed, grasp each PEM and remove it from the chassis. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309217.jpg)

  
**Step 6** |  Disconnect the rear bracket assembly:

  1. Grasp the two cables and unplug them. 
  2. Using a T20 screwdriver, remove the four M4 screws. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309218.jpg)

  
**Step 7** |  Grasp the rear bracket assembly and disconnect it from the rest of the chassis.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309219.jpg)  
**Step 8** |  With the rear bracket assembly removed, disconnect the PCB: 

  1. Grasp the cable and unplug it.
  2. Using the T15 screwdriver, remove the 19 M4 screws, and remove the PCB from the chassis midplane sheet metal.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309220.jpg)

  
**Step 9** |  Recycle the sheet metal and motherboard in compliance with your local recycling and e-waste regulations.   
  
* * *

### Recycling the UCS 9108 25G IFM PCBs

Each Cisco UCS Intelligent Fabric Module (IFM) has a printed circuit board (PCB) that is connected to the IFM's sheet metal tray. You must: 

  * Disassemble and remove additional parts to gain access to the PCB. 

  * Disconnect the PCB from the sheet metal to recycle the PCB. 

  * Recycle each IFM in the Cisco UCS X9508 chassis.


Use the following procedure to recycle the UCS IFMs.

#### Before you begin

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

**For Recyclers Only!** This procedure is not a standard field-service option. This procedure is for recyclers who will be reclaiming the electronics and sheet metal for proper disposal to comply with local eco design and e-waste regulations. 

* * *  
  
---|---  
  
You will find it helpful to gather the following tools before beginning this procedure:

  * Screwdrivers: One each of T8 and T10 screwdriver, and #1 Phillips.

  * Nut drivers: One 8mm hexagonal.


#### Procedure

* * *

**Step 1** |  Remove the following components by hand: 

  1. Grasp each fan module cable and remove it. 
  2. Grasp each fan module and remove it. 
  3. Grasp the M.2 storage module and remove it.
  4. Grasp the light pipe and remove it.

![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309257.jpg)  
---|---  
**Step 2** |  Remove the stiffener bracket.

  1. Using a T10 screwdriver, remove the M3 screws.
  2. Grasp the bracket and remove it.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309258.jpg)

  
**Step 3** |  Remove the horizontal rear bracket.

  1. Using a T8 screwdriver, remove the M3 screws on the exterior of the IFM.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309259.jpg)
  2. Using a T10 screwdriver, remove the M3 screws on the interior of the IFM. 
  3. Grasp the bracket and remove it.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309260.jpg)

  
**Step 4** |  Disconnect additional components and fasteners.

  1. Using a T8 screwdriver, remove the M3 screw on the IFM faceplate.
  2. Grasp the plastic HDMI plug and remove it. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309261.jpg)
  3. Using an 8mm hexagonal nut driver, remove the standoffs.
  4. Using a T10 screwdriver, remove the M3 screws. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309262.jpg) |  Red circles (![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309210.jpg) )  |  M3 hexagonal standoffs, 4  
---|---  
Blue circles (![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309209.jpg) )  |  M3 screws, 6  
  5. Grasp the PCBA and disconnect it from the sheet metal. 


  
**Step 5** |  Disconnect the remaining components from the PCBA.

  1. Using the T10 screwdriver, remove the M3 screws for the top heatsink.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309263.jpg)
  2. Turn the PCBA over so that the bottom is facing up.
  3. Using the #1 Phillips screwdriver and remove the M2 screws. 
  4. Using a pliers, release the four heatsink pushpins.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309264.jpg) |  Red circles (![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309210.jpg) )  |  M2 screws for plastic bracket, 4  
---|---  
Blue circles (![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309209.jpg) )  |  Heatsink pushpins, 4  
  5. Turn the PCBA over again so that the top is facing up. 

  6. Grasp the plastic bracket for the M.2 module and remove it.

  7. If the top heat sink is still attached, grasp and remove it. 

  8. Grasp the three fan baffles and remove them.

  9. Grasp the center heatsink and remove it.

![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309265.jpg)


  
**Step 6** |  Recycle the sheet metal and motherboard in compliance with your local recycling and e-waste regulations.   
  
* * *

#### What to do next

To remove the chassis motherboard, go to Recycling the Chassis PCB Assembly (PCBA). 

### Recycling the UCS 9108 100G IFM PCBs

Each Cisco UCS Intelligent Fabric Module (IFM) has a printed circuit board (PCB) that is connected to the IFM's sheet metal tray. You must: 

  * Disassemble and remove additional parts to gain access to the PCB. 

  * Disconnect the PCB from the sheet metal to recycle the PCB. 

  * Recycle each IFM in the Cisco UCS X9508 chassis.


Use the following procedure to recycle the UCS IFMs.

#### Before you begin

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

**For Recyclers Only!** This procedure is not a standard field-service option. This procedure is for recyclers who will be reclaiming the electronics and sheet metal for proper disposal to comply with local eco design and e-waste regulations. 

* * *  
  
---|---  
  
You will find it helpful to gather the following tools before beginning this procedure:

  * Screwdrivers: One each of T8 and T10 screwdriver, and #1 Phillips.

  * Nut drivers: One 8mm hexagonal.


#### Procedure

* * *

**Step 1** |  Remove the following components by hand: 

  1. Grasp each fan module cable and remove it. 
  2. Grasp each fan module and remove it. 
  3. Grasp the M.2 storage module and remove it.
  4. Grasp the light pipe and remove it.

![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540710.jpg)  
---|---  
**Step 2** |  Remove the stiffener bracket.

  1. Using a T10 screwdriver, remove the M3 screws.
  2. Grasp the bracket and remove it.  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540711.jpg)

  
**Step 3** |  Remove the horizontal rear bracket.

  1. Using a T8 screwdriver, remove the M3 screws on the exterior of the IFM.  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540712.jpg)
  2. Using a T10 screwdriver, remove the M3 screws on the interior of the IFM. 
  3. Grasp the bracket and remove it.  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540713.jpg)

  
**Step 4** |  Disconnect additional components and fasteners.

  1. Using a T8 screwdriver, remove the M3 screw on the IFM faceplate.
  2. Grasp the plastic HDMI plug and remove it. ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540714.jpg)
  3. Using an 8mm hexagonal nut driver, remove the standoffs.
  4. Using a T10 screwdriver, remove the M3 screws. ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540715.jpg) |  Red circles (![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309210.jpg) )  |  M3 hexagonal standoffs, 4  
---|---  
Blue circles (![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309209.jpg) )  |  M3 screws, 6  
  5. Grasp the PCBA and disconnect it from the sheet metal. 


  
**Step 5** |  Disconnect the remaining components from the PCBA.

  1. Using the T10 screwdriver, remove the M3 screws for the top heatsink.  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540716.jpg)
  2. Turn the PCBA over so that the bottom is facing up.
  3. Using the #1 Phillips screwdriver and remove the M2 screws. 
  4. Using a pliers, release the four heatsink pushpins.  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540717.jpg) |  Red circles (![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309210.jpg) )  |  M2 screws for plastic bracket, 4  
---|---  
Blue circles (![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309209.jpg) )  |  Heatsink pushpins, 4  
  5. Turn the PCBA over again so that the top is facing up. 

  6. Grasp the plastic bracket for the M.2 module and remove it.

  7. If the top heat sink is still attached, grasp and remove it. 

  8. Grasp the three fan baffles and remove them.

  9. Grasp the center heatsink and remove it.

![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540718.jpg)

  
**Step 6** |  Recycle the sheet metal and motherboard in compliance with your local recycling and e-waste regulations.   
  
* * *

#### What to do next

To remove the chassis motherboard, go to Recycling the Chassis PCB Assembly (PCBA). 

### Recycling a UCS X9416 X-Fabric Module PCB

Each UCS X9416 Fabric Module has a printed circuit board (PCB) that is connected to module's sheet metal tray. To recycle each module's PCB, you must: 

  * Disassemble and remove additional parts to gain access to the PCB. 

  * Disconnect the PCB from the sheet metal to recycle the PCB. 

  * Recycle each module in the Cisco UCS X9508 chassis.


Use the following task to recycle the X9416 fabric modules.

#### Before you begin

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

**For Recyclers Only!** This procedure is not a standard field-service option. This procedure is for recyclers who will be reclaiming the electronics and sheet metal for proper disposal to comply with local eco design and e-waste regulations. 

* * *  
  
---|---  
  
You will find it helpful to gather the following tools before attempting this procedure:

  * Screwdrivers: One each of T8 and T10 screwdriver 

  * Nut drivers: One 8mm hexagonal head nut driver. 


#### Procedure

* * *

**Step 1** |  Remove the following components by hand: 

  1. Grasp each fan cable and remove it. 
  2. Grasp each fan module and remove it.  For information, see Removing a Fan for a UCS Intelligent Fabric Module (IFM) or X-Fabric Module (XFM) Blank. 
  3. Grasp the light pipe and remove it. ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540806.jpg)

  
---|---  
**Step 2** |  Remove the rear fan bracket.

  1. Using a T10 screwdriver, remove the M3 screws.
  2. Grasp the bracket and remove it.  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540807.jpg)

  
**Step 3** |  Remove the rear back-panel connector bracket.

  1. Using a T8 screwdriver, remove the M3 screws (two per side) on the exterior of the module. ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540745.jpg)![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540746.jpg)
  2. Using a T10 screwdriver, remove the M3 screws on the interior of the module.
  3. Grasp the bracket and remove it.  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540808.jpg)

  
**Step 4** |  Remove additional components and fasteners. 

  1. Using an 8mm hexagonal nut driver, remove the standoffs.
  2. Using a T10 screwdriver, remove the M3 screws. ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540744.jpg) |  Red circles (![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309210.jpg) )  |  M3 hexagonal standoffs, 4  
---|---  
Blue circles (![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309209.jpg) )  |  M3 screws, 4  
  3. Grasp the PCBA and disconnect it from the sheet metal.


  
**Step 5** |  Disconnect the PCB from the sheetmetal. ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540747.jpg)  
**Step 6** |  Recycle the sheet metal and motherboard in compliance with your local recycling and e-waste regulations.   
  
* * *

#### What to do next

Choose the appropriate option:

  * To recycle an X-Fabric Module Blank motherboard, go to: Recycling X-Fabric Module Blank PCBs. 

  * To recycle a 100G UCS Intelligent Fabric Module motherboard, go to: Recycling the UCS 9108 100G IFM PCBs. 

  * To recycle a 25G UCS Intelligent Fabric Module motherboard, go to: Recycling the UCS 9108 25G IFM PCBs. 

  * To recycle the chassis motherboard, go to Recycling the Chassis PCB Assembly (PCBA). 


### Recycling a UCS X9516 X-Fabric Module PCB

Each Cisco UCS X9516 X-Fabric Module has a printed circuit board (PCB) that is connected to the module's sheet metal tray. You must: 

  * Disassemble and remove additional parts to gain access to the PCB. 

  * Disconnect the PCB from the sheet metal to recycle the PCB. 

  * Recycle each module in the Cisco UCS X9508 chassis.


Use the following procedure to recycle the UCS X9516 module.

#### Before you begin

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

**For Recyclers Only!** This procedure is not a standard field-service option. This procedure is for recyclers who will be reclaiming the electronics and sheet metal for proper disposal to comply with local eco design and e-waste regulations. 

* * *  
  
---|---  
  
You will find it helpful to gather the following tools before beginning this procedure:

  * Screwdrivers: One each of T8 and T10 screwdriver, and #1 Phillips.

  * Nut drivers: One 8mm hexagonal.


#### Procedure

* * *

**Step 1** |  Remove the fans: 

  1. Grasp each fan module cable and disconnect it from the motherboard connector. 
  2. Grasp each fan module and remove it by pinching the release tabs and lifting each fan off of the module. ![](/c/dam/en/us/td/i/500001-600000/520001-530000/526001-527000/526605.jpg)

  
---|---  
**Step 2** |  Using a #2 Phillips screwdriver, loosen the captive screws for each cage, then lift each cage up to detach it from the PCB.  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525957.jpg)  
**Step 3** |  Grasp each PCIe cage air baffle and lift it up to disconnect it from the module.  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525958.jpg)  
**Step 4** |  Remove the stiffener bracket.

  1. Using a T10 screwdriver, remove the M3 screws.
  2. Grasp the bracket and remove it.  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525959.jpg)

  
**Step 5** |  Remove the horizontal rear bracket.

  1. Using a T8 screwdriver, remove the M3 screws on the exterior of the module  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525963.jpg)
  2. Using a T10 screwdriver, remove the M3 screws on the rear bracket (1), the guide pins for the PCIe cages (2), and the air baffle screw at the front of the module (3). 
  3. Grasp the rear bracket and remove it.  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525960.jpg) |  **1** |  Rear bracket screws  
---|---  
**2** |  Securing screws, one for each PCIe cage guide-pin.  
**3** |  Front air baffle screw  

  
**Step 6** |  Disconnect additional components and fasteners.

  1. Using a T8 screwdriver, remove the M3 screw on the IFM faceplate.
  2. Grasp the plastic HDMI plug and remove it. ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525964.jpg)
  3. Using an 8mm hexagonal nut driver, remove the four M3 hexagonal standoffs (1).
  4. Using a T10 screwdriver, remove the six M3 screws (1). ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525965.jpg)
  5. Grasp the PCBA and disconnect it from the sheet metal. 

  
**Step 7** |  Disconnect the remaining components from the PCBA.

  1. Using the T10 screwdriver, remove the M3 screws for the small heatsink.  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525966.jpg)
  2. Turn the PCBA over so that the bottom is facing up.
  3. Using a pliers, release the eight heatsink pushpins.  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525967.jpg)
  4. Turn the PCBA over again so that the top is facing up. 
  5. Grasp all three heatsinks and remove them from the module's PCB. ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525968.jpg)

  
**Step 8** |  Disconnect the PCIe cage's PCB from the cage.

  1. Using a #2 Phillips screwdriver, loosen the captive thumbscrew on the PCIe cage (1).
  2. Open the cage door and remove the card (2). 
  3. Using a #2 Phillips screwdriver, remove the three M3 screws that secure the card PCB to the cage (3). 
  4. Disconnect the PCB from the sheetmetal PCIe cage (4). ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525969.jpg)

  
**Step 9** |  Recycle the sheet metal and motherboard in compliance with your local recycling and e-waste regulations.   
  
* * *

#### What to do next

To remove the chassis motherboard, go to Recycling the Chassis PCB Assembly (PCBA). 

### Recycling X-Fabric Module Blank PCBs

Each UCS X-Fabric Module Blank (module blank) has a printed circuit board (PCB) that is connected to module blank's sheet metal tray. To recycle each module blank's PCB, you must: 

  * Disassemble and remove additional parts to gain access to the PCB. 

  * Disconnect the PCB from the sheet metal to recycle the PCB. 

  * Recycle each module blank in the Cisco UCS X9508 chassis.


Use the following task to recycle the module blank.

#### Before you begin

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

**For Recyclers Only!** This procedure is not a standard field-service option. This procedure is for recyclers who will be reclaiming the electronics and sheet metal for proper disposal to comply with local eco design and e-waste regulations. 

* * *  
  
---|---  
  
You will find it helpful to gather a T10 screwdriver before attempting this procedure:

#### Procedure

* * *

**Step 1** |  Remove the following components by hand: 

  1. Grasp each fan cable and remove it. 
  2. Grasp each fan module and remove it.  For information, see Removing a Fan for a UCS Intelligent Fabric Module (IFM) or X-Fabric Module (XFM) Blank. 
  3. Grasp the light pipe and remove it. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309254.jpg)

  
---|---  
**Step 2** |  Grasp the fan module support bracket and remove it.   
**Step 3** |  Remove the vertical rear bracket.

  1. Using a T10 screwdriver, remove the M3 screws.
  2. Grasp the bracket and remove it.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309255.jpg)

  
**Step 4** |  Remove additional components and fasteners. 

  1. Using a T10 screwdriver, remove the M3 screws. ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540750.jpg)
  2. Grasp the PCB and disconnect it from the sheet metal. ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540747.jpg)

  
**Step 5** |  Recycle the sheet metal and motherboard in compliance with your local recycling and e-waste regulations.   
  
* * *

#### What to do next

Choose the appropriate option:

  * To recycle an X-Fabric Module motherboard, go to: Recycling a UCS X9416 X-Fabric Module PCB. 

  * To recycle a 100G UCS Intelligent Fabric Module motherboard, go to: Recycling the UCS 9108 100G IFM PCBs. 

  * To recycle a 25G UCS Intelligent Fabric Module motherboard, go to: Recycling the UCS 9108 25G IFM PCBs. 

  * To recycle the chassis motherboard, go to Recycling the Chassis PCB Assembly (PCBA). 


---
