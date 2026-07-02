# Cisco UCS X-Series Direct Fabric Interconnect 9108 100G Installation and Service Guide

| | |
|---|---|
| **URL Title** | Cisco UCS X-Series Direct Fabric Interconnect 9108 100G Installation and Service Guide |
| **URL** | https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x-series-direct/hw/s9108/install/ucs-x-series-direct-9108-100g/m-overview.html |
| **Long URL** |  |
| **HTML Title** | Cisco UCS X-Series Direct Fabric Interconnect 9108 100G Installation and Service Guide - Overview [Cisco UCS X-Series Direct] |
| **Source file** | `ucs-docs-raw/html/m-overview.html` |
| **File type** | HTML |
| **Fetched on** | 2026-07-02 13:04:36 |

---

## Page 1: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x-series-direct/hw/s9108/install/ucs-x-series-direct-9108-100g/m-overview.html

# Overview  
  
This chapter contains the following topics:

## Cisco UCS X-Series Direct Fabric Interconnect 9108 100G Overview

The Cisco UCS X-Series Direct Fabric Interconnect 9108 100G (UCSX-S9108-100G) is a modular fabric interconnect system designed for the Cisco UCS X9508 server chassis. The Cisco UCS X-Series Direct Fabric Interconnect 9108 100G ("fabric interconnect" or "fabric interconnect module" in this document) is part of the overall Cisco UCS X-Series Direct solution, which consists of the fabric interconnect plus additional Cisco equipment that enables end-to-end connectivity. 

Deployed in pairs, the fabric interconnect offers robust and scalable networking, compute, storage, and GPU acceleration in a smaller physical form factor that can replace a standalone Cisco UCS Fabric Interconnect. The fabric interconnect module is designed for cost, power, and physical space savings in less extensive applications, for example: 

  * at the network edge

  * deployments of up to 8 blade servers or compute nodes.


The X-Series Direct supports the following: 

  * Eight QSFP ports (1 through 8) capable of up to 100 Gbps including two unified ports (1 and 2).

  * CPU: Intel Atom® C3000 processor series System on a Chip (SOC), 2.2 GHz, 8 cores. One CPU is supported per UCS X-Series Direct Fabric Interconnect. 

  * Uplink Ports: Total of eight physical ports that can be configured as a mix of Fibre Channel and Ethernet to connect to ToR switches. The first two ports are unified ports to provide flexibility between Fibre Channel and Gigabit Ethernet, and 6 ports are dedicated Ethernet. 

  * Fibre Channel: A maximum of two uplinks configured through total of 8 break-out ports supporting either 8, 16 or 32 Gbps each fibre-channel ports. Fibre Channel ports support breakout to a maximum of eight ports, four breakout ports for each physical FC port. 

  * Ethernet: Depending on the port speed configured on the physical port, Ethernet uplinks are supported as follows:

  * For 10G or 25G, a maximum of eight ports. Breakout ports or single QSA transceivers are supported.

  * For 100G, a maximum of eight ports. Because all eight ports support 100G Ethernet, Ethernet port breakout is not required. 

  * For 1G, a maximum of two ports (ports seven and eight only). QSA is supported. For information about the port locations and identifiers, see Fabric Interconnect Front Panel. 

For more information, see [Fabric Interconnect Port Configuration](m-connecting.html#Cisco_Reference.dita_af10e611-e042-4b17-88be-d494b149b461). 

  * 32 GB Flash Memory

  * 16 GB DRAM

  * Three fans for optimal cooling

  * A boot-optimized mini-storage module consisting of one M.2 240G SATA SSD, with no RAID support.

  * Local console connectivity: RS-232 Serial Console port (RJ45 connector)

  * Bootup and system firmware log retrieval: USB 2.0 port Type-A connector

  * Management connectivity: One 10/100/1000 Mbps management port 


The fabric interconnect is always deployed in pairs in a Cisco UCS X9508 modular system. The UCS X-Series Direct system cannot operate with only one fabric interconnect. 

## Fabric Interconnect Front Panel

The Cisco UCS X-Series Direct Fabric Interconnect 9108 100G front panel contains system LEDs that provide visual indicators for how the overall fabric interconnect is operating. Physical ports are also supported for network and storage connectivity through scale-out connections with ToR switches or direct connection to servers. 

![](/c/dam/en/us/td/i/400001-500000/480001-490000/481001-482000/481621.jpg)

**1** |  Status LED The LED provides a visual indicator about the status of the fabric interconnect. For more information, see Interpreting LEDs.  |  **2** |  Fan Status LEDs  LEDs are stacked vertically, with each LED corresponding to a fan. Fan 1 is the top LED, Fan 2 is the middle LED, and Fan 3 is the bottom LED.  For more information, see Interpreting LEDs.   
---|---|---|---  
**3** |  Reset Button |  **4** |  Port Link and Port Activity LEDs For more information, see Interpreting LEDs.   
**5** |  Uplink Ports one through four. Ports are numbered vertically starting with the top left port as port 1.  Ports one and two (indicated with the yellow highlighting) are 100 Gbps Unified ports which can be configured as:

  * Ethernet uplink, 10/25/40/100 Gbps
  * Fibre Channel uplink, 8/16/32 Gbps
  * Appliance
  * Fibre Channel over Ethernet (FCoE) Uplink
  * Fibre Channel storage

Ports 3 and 4 are 100 Gbps Ethernet only, which can be configured as:

  * 10/25/40/100 Gbps Ethernet Uplink
  * Appliance
  * Fibre Channel over Ethernet (FCoE) Uplink

|  **6** |  Ejector handles, one per ejector.   
**7** |  OAM Ethernet Port, 10/100/1000 Mbps RJ-45 for out-of-band (OOB) management. This port is used for Cisco UCS management applications, such as Cisco UCS Manager or Cisco Intersight. For more information, see Interpreting LEDs.  |  **8** |  RJ-45 Console Port (RS-232 Serial Console) Used for initial system configuration and troubleshooting the fabric interconnect.  For more information, see Interpreting LEDs.   
**9** |  USB 2.0 port Can be used for system booting, firmware upgrades, or log retrieval. |  **10** |  Ethernet Ports, five through eight Ports are numbered vertically starting with the top left port as port 5. 

  * Ports 5 through 8 support 10/25/40/100 Gbps Ethernet uplinks.
  * Also, ports seven and eight support 1 Gbps Ethernet uplinks 
  * Appliance

  
  
  * Interpreting LEDs


### Interpreting LEDs

Table 1. Fabric Interconnect LEDs LED  |  Color  |  Description   
---|---|---  
Fabric Interconnect Status  |  Green |  The fabric interconnect is receiving power and operational.  
Flashing Amber  |  The fabric interconnect is booting up.  
Solid Amber |  Temperature exceeds the minor alarm threshold.  
Red |  Temperature exceeds the major alarm threshold.  
Dark |  The fabric interconnect is not receiving power.  
Fan Status |  Green  |  The fan module is operational.  
Red  |  The fan module is not operational (fan is probably not functional).  
Dark  |  Fan module is not receiving power.  
Table 2. Fabric Interconnect Data Port LEDs LED  |  Color  |  Description   
---|---|---  
Ports, Ethernet and Fibre Channel |  Green |  Port admin state is 'Enabled', SFP is present, and the interface is connected (that is, cabled, and the link is up).  
Amber  |  Port admin state is 'Disabled, or the SFP is absent, or both  
Dark |  Port admin state is 'Enabled' and SFP is present, but interface is not connected.  
Table 3. Fabric Interconnect Management and Console Port LEDs LED  |  Color  |  Description   
---|---|---  
Management Port and Console Port Link LED |  Solid Green |  Physical Link detected  
Dark  |  No Physical Link Detected  
Management Port and Console Port Activity LED |  Blinking Green |  Activity  
Dark  |  No Activity  
  
## Port Type Details

The following tables show the port type, protocol support, and port role of the ports on the fabric interconnect. 

Port |  Port Type |  Protocol Support |  Port Role  
---|---|---|---  
|  1 GigE QSA |  10/25 GigE  Break- out  QSA, or QSA 28 |  40/100 GigE  |  4x 8/16/32 Gbps FC Break- out |  Ethernet |  Fibre Channel (FC) |  Fibre Channel over Ethernet (FCoE) |  Uplink, Ethernet, 10/25/ 40/100 Gbps  |  Uplink, Fibre Chanel  8/16/32 Gbps |  Uplink FCoE  10/25/ 40/100 Gbps |  Appli- ance |  Storage Port, FC  
1 to 2 |  No |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes |  Yes  
3 to 6 |  No |  Yes |  Yes |  No |  Yes |  No |  Yes | Yes |  No |  Yes |  Yes |  No  
7 to 8 |  Yes |  Yes |  Yes |  No |  Yes |  No |  Yes | Yes |  No |  Yes |  Yes |  No

---

## Page 2: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x-series-direct/hw/s9108/install/ucs-x-series-direct-9108-100g/m-preface.html

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

## Page 3: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x-series-direct/hw/s9108/install/ucs-x-series-direct-9108-100g/m-installing.html

# Installing the Fabric Interconnect

This chapter contains the following topics:

## Installation Guidelines and Limitations

Be aware of the following limitations when installing the Cisco UCS X-Series Direct Fabric Interconnect 9108 100G into the Cisco UCS X9508 chassis: 

  * The fabric interconnects are always deployed in pairs. You cannot install and operate the fabric interconnect system with only one installed in the chassis. 

  * Fabric interconnect can either be installed in the chassis or not. If no fabric interconnect is used in the Cisco UCS X9508 chassis, then you must install a pair of Cisco UCS Intelligent Fabric Modules (IFMs). The chassis cannot be used or operated without any fabric interconnects (FIs) or IFMs in place. 


## Installing and Removing the Fabric Interconnect

Each Cisco UCS X-Series Direct Fabric Interconnect 9108 100G in the rear of the chassis. They are always deployed in pairs, and the minimum fabric interconnect configuration for each UCS X9508 is two. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

When working with the fabric interconnects, handle them carefully to avoid damage to the modules, connectors, and pins.

* * *  
  
---|---  
  
Use the following procedures to replace the fabric interconnect

  * Removing the Fabric Interconnect

  * Installing the Fabric Interconnect


  * Removing the Fabric Interconnect
  * Installing the Fabric Interconnect


### Removing the Fabric Interconnect

The fabric interconnects must be deployed in pairs, so if you remove one, you must insert another fabric interconnect in its place for normal runtime operation. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

When working with the fabric interconnects, handle them carefully to avoid damage to the modules, connectors, and pins! Make sure that the modules are level during removal and slide them out of the chassis slowly. 

* * *  
  
---|---  
  
#### Before you begin

If the UCS X9508 server chassis has cable management arms attached, you might need to remove them if the cables obstruct the removal of the Cisco UCS X-Series Direct 9108 100G Fabric Interconnect. If you need to remove the cable management arms, you will need a #2 Phillps screwdriver to perform the task. 

#### Procedure

* * *

**Step 1** |  If the Cisco UCS X9508 server chassis that contains the fabric interconnects has a cable management tray, move the cables out of the way. If the cables cannot be moved sufficiently, unplug them and, if necessary, remove the cable management arms.  For reference, go to [Installing the Top Cable Management Arms](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x9508/install/b-ucs-x9508-install/m-installation.html#Cisco_Task_in_List_GUI.dita_42a15b91-234d-4247-893d-2059d848cc3d). Removing the cable management arms is the reverse of the installation procedure.   
---|---  
**Step 2** |  Using your fingers, pinch the interior end of both of the fabric interconnects' handles to disengage each ejector latch. This step unlocks the module handles so that they can move.   
**Step 3** |  Keeping the modules handles level, pull them towards you so that they arc away from the chassis.  You might feel some resistance as the fabric interconnect disconnects from the socket inside the chassis.  Figure 1. Opening the Module Handles  ![](/c/dam/en/us/td/i/400001-500000/480001-490000/483001-484000/483441.jpg)  
**Step 4** |  Slide the module about halfway out of the chassis, then place your other hand underneath the fabric interconnect to support it.  |  **Caution** |  Make sure to apply even pressure when sliding the module out of the chassis. Do not push down or pull up on the module handles, and do not apply more force to one ejector handle than the other.   
---|---  
**Step 5** |  Continue sliding the fabric interconnect out of the chassis until it is completely removed.  Figure 2. Removing a Fabric Interconnect  ![](/c/dam/en/us/td/i/400001-500000/480001-490000/483001-484000/483442.jpg)  
  
* * *

#### What to do next

Insert a fabric interconnect. Go to Installing the Fabric Interconnect. 

### Installing the Fabric Interconnect

The Cisco UCS X-Series Direct Fabric Interconnect 9108 100G must be deployed in pairs, so there are no fabric interconnect module blanks that can be installed. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

When working with the fabric interconnect, handle them carefully to avoid damage to the modules, connectors, and pins! Make sure that the modules are level during insertion and slide them into the chassis slowly. 

* * *  
  
---|---  
  
#### Procedure

* * *

**Step 1** |  If the fabric interconnect has a cable management tray, remove it.   
---|---  
**Step 2** |  Swing the ejector handles to the open position.   
**Step 3** |  Placing one hand underneath the fabric interconnect, align the module with the empty slot on the rear of the chassis. Figure 3. Aligning the Fabric Interconnect  ![](/c/dam/en/us/td/i/400001-500000/480001-490000/483001-484000/483440.jpg)  
**Step 4** |  Holding the fabric interconnect level, slide it almost all the way into the chassis until you feel some resistance.  This resistance is normal. It occurs when the connectors at the rear of the fabric interconnect contact the socket inside the chassis.  |  **Caution** |  Make sure to apply even pressure when sliding the module into the chassis. Do not push down or pull up on the module handles, and do not apply more force to one ejector handle than the other.   
---|---  
**Step 5** |  Grasp each of the ejector handles, and keeping them level, slowly arc them inward toward the chassis. This step seats the fabric interconnect connectors into the sockets on the midplane.  |  **Caution** |  Make sure to apply even pressure when closing the module ejector handles! Do not push down or pull up on the module handles, and do not apply more force to one ejector handle than the other.   
---|---  
**Step 6** |  Push the ejector handles until both are parallel with the face of the fabric interconnect.  Make sure the ejector latch is fully inserted in the front panel.  
**Step 7** |  If the Cisco UCS X9508 server chassis that contains the fabric interconnect module has a cable management tray, attach it.  Go to [Installing the Top Cable Management Arms](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x9508/install/b-ucs-x9508-install/m-installation.html#Cisco_Task_in_List_GUI.dita_42a15b91-234d-4247-893d-2059d848cc3d).   
  
* * *

## Fabric Interconnect Configuration

Cisco UCS X-Series Direct Fabric Interconnect 9108 100G can be configured and managed using the following Cisco management platforms. 

### Cisco Intersight

The fabric interconnect can be configured and managed through the Cisco Intersight management platform in Intersight Managed Mode (Cisco Intersight Managed Mode). For details, see the Cisco Intersight Managed Mode Configuration Guide, which is available at the following URL: [Cisco Intersight Managed Mode Configuration Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Intersight_Managed_Mode_Configuration_Guide.html). 

### Cisco UCS Manager

The fabric interconnect can be configured and managed through UCS Manager version 4.3(4). For details, see the latest version of the Cisco UCS Manager Administration Guide, which is available at the following URL: <https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Admin-Management/4-3/b_cisco_ucs_admin_mgmt_guide_4-3.html>

---

## Page 4: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x-series-direct/hw/s9108/install/ucs-x-series-direct-9108-100g/m-connecting.html

# Connecting the Fabric Interconnect

This chapter contains the following topics:

## Overview of Network Connections

After you install the UCS X-Series Direct in a rack and power it up, you are ready to make the following network connections:

  * Console connection—This is a direct local management connection that you use to initially configure the fabric interconnect. You must make this physical connection using RS-232 serial console cable with RJ-45 connector first, for initial configuration of the fabric interconnects. 

  * Management connection—After you complete the initial configuration using the console, you can use this connection to manage UCS X-Series Direct either through UCS Manager or Cisco Intersight. 

  * Uplink interface connections—These connections are for upstream network connectivity.


Each of these connection types is explained in one of the sections that follow. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

When running cables in overhead or subfloor cable trays, we strongly recommend that you locate power cables and other potential noise sources as far away as practical from network cabling that terminates on Cisco equipment. In situations where long parallel cable runs cannot be separated by at least 3.3 feet (1 meter), we recommend that you shield any potential noise sources by housing them in a grounded metallic conduit. 

* * *  
  
---|---  
  
## Fabric Interconnect Port Configuration

### Port Types

The fabric interconnect has the following ports which shall be configured through supported Cisco management platforms:

  * Uplink port: Also called as border-port. An uplink port is an Ethernet port connecting to a northbound LAN aggregation switch.

  * FC Uplink port: A FC port that is connected to an uplink FC fabric. For example, an FC interface of the MDS switch.

  * FCoE Uplink port: An FCoE port that is connected to an uplink FCoE fabric. For example, an FCoE interface on a Cisco MDS or Cisco Nexus switch. 

  * Appliance port: An Ethernet server-port that is directly connected to a storage appliance. This configuration requires FI to be in Ethernet-End-Host-Mode. 

  * Fibre Channel Storage Port: A port that can be used for directly connecting to a fibre-channel storage array. For example, a NetApp storage© or Pure Storage© array connected directly over an FC port. 


### Port Configuration

The following table shows the port types that can be configured. For port type definitions, see the preceding section.

Chassis Port |  Port Speed |  Supported Port Type   
---|---|---  
1 and 2 (unified ports) |  10G/25G/40G/100 G bps or 8G/16G/32 Gbps |  Ethernet or Fibre Channel | 

  * Ethernet Uplink Port
  * FCoE uplink port
  * Appliance port 
  * FC uplink port
  * FC storage port

  
3 through 6 |  10/25/40/100 Gbps Ethernet  |  Native Ethernet | 

  * Ethernet Uplink Ports
  * FCoE uplink ports
  * Appliance ports 

  
7 and 8 |  1/10/25/40/100 Gbps  |  Native Ethernet | 

  * Ethernet Uplink Ports
  * FCoE uplink ports
  * Appliance ports 

  
  
  * Port Breakout


### Port Breakout

Port breakout is supported with the following configurations. 

Breakout Level |  Ports 1 and 2 (QSFP28) |  Ports 3 - through 8 (QSFP28)  
---|---|---  
4x8G FC |  Yes on ports 1 and 2 only (DS-SFP-4x32G-SW transceiver for breakout) |  No  
4x16G FC |  Yes on ports 1 and 2 only (DS-SFP-4x32G-SW transceiver for breakout) |  No  
4x32G FC |  Yes on ports 1 and 2 only (DS-SFP-4x32G-SW transceiver for breakout) |  No  
1x100G |  Yes |  Yes  
4x10G |  Yes |  Yes  
4x25G |  Yes |  Yes  
1x40G |  Yes |  Yes  
1x25G (Cisco QSA28 with SFP28) |  Yes (QSA28) |  Yes (QSA28)  
1x10G QSA or QSA28 with SFP+ | Yes (QSA28) |  Yes (QSA28)  
1G (CVR-QSFP-SFP10G+GLC-TE) | No |  Yes, ports seven and eight only.  
  
## Example Ethernet Topologies

The following sections show supported end-to-end Ethernet topologies. 

### With VPC (Virtual Port Channel) or MCT (Multi Channel Trunking)

Refer to the following recommended topology to guide you while connecting the fabric interconnect for end-to-end Ethernet. This topology is recommended with either Cisco Nexus 9000 Series switches in VPC or any standard top of rack (ToR) Ethernet switch in MCT (multi-chassis trunking) mode. 

![](/c/dam/en/us/td/i/400001-500000/480001-490000/481001-482000/481629.jpg)

In this topology:

  * The Ethernet uplink ports on the fabric interconnect can be used for Ethernet uplinks to the redundant ToR (top of rack) Nexus switches. 

  * Port channels connect from the fabric interconnect to the ToR Nexus switches in VPC mode, or to a different ToR Ethernet switch in a multi-channel trunk. 

  * ToR switch ports should be STP (spanning-tree) edge ports.

  * This topology:

  * Provides redundancy for the fabric interconnect, the ToR switches, and uplinks. 

  * Provides bandwidth aggregation to the fabric interconnect through port channels

  * Avoids ToR-to-ToR L2 switching.

  * The ToR fabric could be 3-tier, EVPN-VxLAN, an IP Fabric, or a CLOS leaf and spine topology.


### No VPC (Virtual Port Channel) or MCT (Multi Channel Trunking)

Refer the following recommended topology to guide you while connecting the fabric interconnect for end-to-end Ethernet connectivity. 

  * This topology is recommended if your deployment does not use VPC or MCT. 

  * This topology is supported, but not recommended, if your deployment uses VPC or MCT. Instead, the previous topology is recommended for deployments that use VPC or MCT. 


![](/c/dam/en/us/td/i/400001-500000/480001-490000/481001-482000/481630.jpg)

In this topology:

  * The Ethernet uplink ports on the fabric interconnect can be used for Ethernet uplinks to the redundant ToR (top of rack) Nexus switches. 

  * Port channels connect from the fabric interconnect to the ToR Nexus switches in VPC mode, or to different ToR Ethernet switches in a multi-channel trunk. 

  * In this topology:

  * vNICs are pinned to one uplink, and distributed across multiple uplinks. 

  * ToR switches and uplinks are redundant, but vNICs will experience repinning time after a failover


### No Top of Rack Switch Redundancy

Refer to the following supported topology to guide you while connecting the fabric interconnect for end-to-end Ethernet connectivity. 

![](/c/dam/en/us/td/i/400001-500000/480001-490000/481001-482000/481631.jpg)

This topology conserves the number of overall links and ports, which can be used for additional server connectivity. 

This topology is supported, but not recommended, because of the lack of redundancy for the ToR Ethernet switches. 

## Example Fibre Channel SAN Topologies

The following sections show supported end-to-end Fibre Channel SAN (FC SAN) topologies. 

### End Host Mode 1, With Port Channel Configured

Refer to the following recommended topology to guide you while connecting the fabric interconnect for end-to-end connectivity to FC storage. This topology is recommended with either Cisco MDS switches or any standard top of rack (ToR) FC switch. 

![](/c/dam/en/us/td/i/400001-500000/480001-490000/483001-484000/483446.jpg)

This topology is recommended for a larger FC SAN domain. In this topology:

  * The fabric interconnect is in FC end-host mode. In this mode, the fabric interconnect uplink ports operate as a node ports (N-Port) while ports on the Cisco MDS switch operate as fabric ports (F-Port). 

  * Port Channel configuration is between an FI and MDS pair per side.

  * Port-Channel configuration provides high availability (HA) and uplink bandwidth aggregation (BW).

  * Virtual SANs (vSANs) are carried into the MDS fabric with vSAN trunking.

  * Four virtual HBAs (vHBAs) are configured per server for high availability.


### Switch Mode 1, With Port Channel Configuration 

Refer to the following recommended topology to guide you while connecting the fabric interconnect for end-to-end connectivity to FC storage. This topology is supported with either Cisco MDS or any standard FC switch. 

![](/c/dam/en/us/td/i/400001-500000/480001-490000/483001-484000/483447.jpg)

This topology is supported for more moderate FC SAN domains limited to a maximum of 255 FC devices. In this topology: 

  * Ports on both the FC Switch and the fabric interconnects operate in E-port mode.

  * Port Channel configuration is between an FI and MDS pair per side.

  * Port Channel configuration provides high availability (HA) and uplink bandwidth aggregation (BW).

  * Virtual SANs (vSANs) are carried into the MDS fabric with vSAN trunking.

  * Four virtual HBAs (vHBAs) are configured per server for high availability.

  * This topology supports storage array connections directly to the fabric interconnects with upstream SAN fabric connectivity.


### End-Host Mode 2, No Port Channels

Refer to the following supported topology to guide you while connecting the fabric interconnect for end-to-end connectivity to FC storage. This topology is not recommended if your deployment does not use Cisco MDS switches. 

![](/c/dam/en/us/td/i/400001-500000/480001-490000/483001-484000/483448.jpg)

This topology is supported for any standard deployment that uses third-party TOR FC switches. In this topology: 

  * The fabric interconnects are configured in FC end-host mode.

  * No port-channel configuration with non-MDS FC switches.

  * A virtual SAN (vs An) is not supported due to the absence of a Cisco MDS switch.

  * Four virtual HBAs (vHBAs) are configured per server for high availability.


### Switch Mode, FC Storage Array Direct Connected to Fabric Interconnects

Refer to the following recommended topology to guide you while connecting the fabric interconnect for end-to-end connectivity to FC storage. This topology is supported for directly connecting an FC storage array to the fabric interconnects. 

![](/c/dam/en/us/td/i/400001-500000/480001-490000/483001-484000/483449.jpg)

In this topology:

  * The fabric interconnect is configured in FC switch mode.

  * Four virtual HBAs (vHBAs) are configured per server for high availability.

  * FC SAN zones and zone management is supported through Cisco Intersight Managed Mode (IMM) or Cisco UCS Managed Mode (UMM). 


## Example IP SAN Topologies

The following sections show supported end-to-end IP SAN topologies. 

### With VPC (Virtual Port Channel) or MCT (Multi Chassis Trunking)

Refer to the following supported topology to guide you while connecting the fabric interconnect for end-to-end Ethernet-based IP SAN connectivity. This topology is supported for deployments that use Cisco Nexus TOR switches. 

![](/c/dam/en/us/td/i/400001-500000/480001-490000/483001-484000/483450.jpg)

In this topology:

  * Virtual port channeling (VPC) or multi-chassis trunking (MCT) is recommended.

  * MTU setting should be set to 9216 on the fabric interconnect system QoS.

  * TCP-based storage access can be set to best-effort QOS class. For high performance storage access, no-drop class QoS settings can also be used across fabric interconnects and the TOR switch. 

  * For ROCEv2, the no-drop QoS class is required, and PFC must be enabled on the ToR Nexus switch. 

  * Multiple vNICs must be configured on each server for redundancy.

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Connectivity best practices from the Cisco Nexus switch to vendor IP storage are different for each storage vendor.

* * *  
  
---|---  


### Direct Connection to IP Storage Array

Refer to the following recommended topology to guide you for connecting Ethernet-based IP-SAN storage array directly to the fabric interconnects. 

![](/c/dam/en/us/td/i/400001-500000/480001-490000/483001-484000/483451.jpg)

This topology is supported for smaller IP SANs. In this topology:

  * MTU setting should be set to 9216 on the fabric interconnect system QoS.

  * Ethernet based IP-SAN storage access is supported without the need of TOR switches. 

  * Port-channel configuration between the fabric interconnects and IP-SAN storage array is supported.

  * No support exists for port-channel configuration with VPC.


## Connecting a Console to the Fabric Interconnect

Before you create a network management connection for the fabric interconnect or connect the fabric interconnect to the network, you must create a local management connection through a console terminal. And then configure an IP address for the fabric interconnect. You can use the console to perform the following functions, each of which can be performed through the management interface after you make that connection: 

  * Configure the fabric interconnect using the command-line interface (CLI). 

  * Monitor network statistics and errors. 

  * Configure Simple Network Management Protocol (SNMP) agent parameters. 

  * Download software updates. 


You make this local management connection between the asynchronous serial port on a fabric interconnect module and a console device capable of asynchronous transmission. Typically, you can use a computer terminal as the console device. On the supervisor modules, you use the console serial port. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Before you can connect the console port to a computer terminal, make sure that the computer terminal supports VT100 terminal emulation. The terminal emulation software makes communication between the fabric interconnect and computer possible during setup and configuration. 

* * *  
  
---|---  
  
### Before you begin

  * The Cisco UCS X-Series Direct 9108 100G Fabric Interconnect must be fully installed in the Cisco UCS X9508 chassis, which is connected to a power source, and grounded. 

  * The necessary cabling for the console, management, and network connections must be available. 

  * An RJ-45 rollover cable provided in the fabric interconnect accessory kit. 

  * Network cabling is routed to the location of the installed fabric interconnect. 


### Procedure

* * *

**Step 1** |  Configure the console device to match the following default port characteristics: 

  * 115200 baud 
  * 8 data bits 
  * 1 stop bit 
  * No parity 

  
---|---  
**Step 2** |  Connect an RJ-45 rollover cable to the console port on the fabric interconnect.  You can find this cable in the accessory kit.   
**Step 3** |  Route the RJ-45 rollover cable to the console or modem.   
**Step 4** |  Connect the other end of the RJ-45 rollover cable to the console or to a modem.   
  
* * *

---

## Page 5: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x-series-direct/hw/s9108/install/ucs-x-series-direct-9108-100g/m-servicing.html

# Servicing the Fabric Interconnect

This chapter contains the following topics:

## Installing and Removing the Top Cover

The top cover for the Cisco UCS X-Series Direct 9108 100G Fabric Interconnect can be removed to allow access to internal components, some of which are field-replaceable. The top cover has a release button on one side and an emboss on the other side. 

  * the release button unlocks the cover so that it can be removed from the fabric interconnect

  * the emboss provides a second fingerhold so that you can apply equal force to both sides of the cover. 


![](/c/dam/en/us/td/i/400001-500000/480001-490000/481001-482000/481626.jpg) **1** |  Release Button |  **2** |  Emboss, which can be used as a fingerhold  
---|---|---|---  
  
To remove and install the top cover, use the following procedures:

  * Removing the Top Cover

  * Installing the Top Cover


  * Installing the Top Cover
  * Removing the Top Cover


### Installing the Top Cover

The top cover must be installed on the fabric interconnect during normal runtime operation. Make sure to keep the top cover in place whenever you are not actively working on the fabric interconnect. 

Use the following task to install the top cover. 

#### Before you begin

The top cover has alignment features consisting of catch pins on the inside of the top cover and cutouts in the fabric interconnect's sidewalls. The module can be installed successfully when these features meet. 

#### Procedure

* * *

**Step 1** |  Align the top cover over the fabric interconnect.   
---|---  
**Step 2** |  Lower the top cover onto the fabric interconnect while slightly tilting the front edge of the cover down.   
**Step 3** |  Making sure that the top cover sits flush on the fabric interconnect, slide the top cover towards the front panel until the catch pins insert into their cutouts.  |  **Note** |  You can use the button and emboss on the top cover to ensure you apply equal force to both sides of the top cover while sliding it into place.   
---|---  
The front edge of the top cover must slide under the edge of the front panel. When the top cover is completely installed, the release button clicks. 

![](/c/dam/en/us/td/i/400001-500000/480001-490000/481001-482000/481623.jpg)  
  
* * *

#### What to do next

When you are ready, re-install the fabric interconnect into the chassis. See [Installing the Fabric Interconnect](m-installing.html#Cisco_Task_in_List_GUI.dita_8b4b666c-e890-4d76-bba0-2720cedc21e8). 

### Removing the Top Cover

The fabric interconnect has a sheetmetal top cover that protects components and facilitates proper ventilation and cooling. Follow this procedure to remove the top cover. 

#### Before you begin

To service the fabric interconnect components, you must remove the top cover. If you have not already removed the fabric interconnect from the server chassis, remove it now. See [Removing the Fabric Interconnect](m-installing.html#Cisco_Task_in_List_GUI.dita_214ffc57-18df-4e50-90d6-d08f707177fb). 

#### Procedure

* * *

**Step 1** |  Lay the fabric interconnect flat on an ESD-safe work surface.   
---|---  
**Step 2** |  Using your fingers, press the release button until it clicks.   
**Step 3** |  Using the release button and the embossed fingerhold, slide the top cover back (away from the front panel), while slightly lifting up on the rear end of the top cover.  Gently lifting the rear end of the top cover should help release pressure on the opposite end and enable the top cover's front edge to slide out from under the fabric interconnect's sheetmetal edge.  |  **Note** |  Make sure to slide the top cover far enough that the catch pins clear the cutouts in the sheetmetal.   
---|---  
  
![](/c/dam/en/us/td/i/400001-500000/480001-490000/481001-482000/481628.jpg)

**1** |  Release Button |  **2** |  Embossed fingerhold  
---|---|---|---  
  
* * *

#### What to do next

After performing any maintenance work on the fabric interconnect, reinstall the top cover. See Installing the Top Cover. 

## Fabric Interconnect Components

The Cisco UCS X-Series Direct Fabric Interconnect 9108 100G (UCSX-S9108-100G) has the following board-level components.  Figure 1. Fabric Interconnect, Component View  ![](/c/dam/en/us/td/i/400001-500000/480001-490000/481001-482000/481624.jpg) **1** |  Heatsink, not field replaceable |  **2** |  Fans, (UCSX-RSFAN=), three, which are numbered 1 through 3 starting with the left fan  
---|---|---|---  
**3** |  Heatsink, not field replaceable |  **4** |  QSFP28 Optical Ports.  Ports are arranged in two groups of four physical ports. Ports are stacked in vertical pairs, with two ports in each vertical port stack. From left to right: Port number 1 is the top port of the left port pair in this group, and port number 3 is the top port of the right port pair in the group.  Port number 5 is the top port in the left port pair of this group, and port number 7 is the top port in the right port pair of the group.   
**5** |  M.2 240G SATA, one.  |  **6** |  Mini-storage carrier that holds the M.2 SATA SSD.   
**7** |  Ejector handles, two, one per side.  Ejector handles lock when the fabric interconnect is installed. |  |   
  
## Cisco UCS X-Series Direct Fabric Interconnect Module Field Replaceable Unit Replacement Instructions

The rear of the Cisco UCS X9508 contains two module bays for the UCS X-Series Direct Fabric Interconnect 9108 100G (fabric interconnect modules) above the fans. 

Refer to the following illustration for information about field-replacement options on the fabric interconnect module.

Figure 2. Cisco UCS X-Series Direct Fabric Interconnect 9108 100G Module (UCSX-S9108-100G) FRU Replacement Instructions  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/476001-477000/476039.jpg)

## Installing and Removing the Fabric Interconnect Fans

The Cisco UCS X-Series Direct Fabric Interconnect 9108 100G contains on-board fans (UCSX-RSFAN=). These fans are interchangeable between the fabric interconnect and the UCS Intelligent Fabric Modules (IFMs), but not interchangeable with the fans in the Cisco UCS X9508 Server Chassis. In a typical configuration, there are three fans numbered from one to three on the fabric interconnect. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The fans for the fabric interconnect (UCSX-RSFAN=) are different from the chassis fan modules (UCSX-9508-FAN) that provide cooling and ventilation for the entire server chassis. These two types of fans are not interchangeable. 

* * *  
  
---|---  
  
Use the following procedures to replace a fan on a fabric interconnect. 

  * Removing a Fabric Interconnect Fan

  * Installing a Fabric Interconnect Fan


  * Removing a Fabric Interconnect Fan
  * Installing a Fabric Interconnect Fan


### Removing a Fabric Interconnect Fan

Use the following procedure to remove a fan from the fabric interconnect.

#### Procedure

* * *

**Step 1** |  Grasp the fan by the tabs on each long side wall.   
---|---  
**Step 2** |  Pull the fan straight up. This step disconnects the fan from the power connector and lifts the fan off of the board. Figure 3. Removing the Fan from a Fabric Interconnect  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309543.jpg)  
  
* * *

#### What to do next

Insert a fan module. Go to Installing a Fabric Interconnect Fan. 

### Installing a Fabric Interconnect Fan

Use this task to install the fan (UCSX-RSFAN=) for a fabric interconnect. 

#### Procedure

* * *

**Step 1** |  Align the fan correctly.

  1. Align the power connector on the replacement fan with power connector on the board.
  2. Align the guides on long fan side walls with the corresponding cutouts on the module. Figure 4. Aligning the Fan  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308954.jpg)

  
---|---  
**Step 2** |  Press down evenly on the fan until it is fully seated. Make sure the fan is level while you're installing it. You will feel the fan click into place when it is correctly seated on the module or module blank.   
  
* * *

## Installing and Removing a Fabric Interconnect M.2 Mini Storage Module

Each fabric interconnect has its own onboard storage capability in the form of an M.2 mini storage module. Each mini storage module consists of a sled (or carrier) and a M.2 240G SATA SSD. The M.2 storage module can be interchanged between fabric interconnects in the chassis. The M.2 storage modules are field replaceable, as is the sled. 

Use the following procedures to replace an M.2 mini-storage module:

  * Installing a Fabric Interconnect M.2 Mini Storage Module

  * Removing a Fabric Interconnect M.2 Mini-Storage Module


  * Mini-Storage Considerations
  * Removing a Fabric Interconnect M.2 Mini-Storage Module
  * Installing a Fabric Interconnect M.2 Mini Storage Module


### Mini-Storage Considerations

When installing or removing the mini-storage module or its SSD, be aware of the following: 

  * The M.2 SSDs must be SATA.

  * The socket for the SSD is on the top side of the carrier. Make sure that this SSD is facing up when installing the mini-storage module onto the fabric interconnect. 


### Removing a Fabric Interconnect M.2 Mini-Storage Module

Use this task to remove the fabric interconnect's M.2 mini-storage module.

#### Procedure

* * *

**Step 1** |  Using your fingers, pull the retention clips outward to release pressure on the M.2 mini storage module, and disengage it from the carrier.   
---|---  
**Step 2** |  Grasp the M.2 module by the long sides and pull up to remove it from the carrier.  Figure 5. Detaching and Removing the M.2 Mini Storage Module  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308955.jpg)  
  
* * *

#### What to do next

Insert a new M.2 storage module. Go to Installing a Fabric Interconnect M.2 Mini Storage Module. 

### Installing a Fabric Interconnect M.2 Mini Storage Module

Use this task to install an M.2 mini storage module into the fabric interconnect's M.2 module carrier. 

#### Procedure

* * *

**Step 1** |  Holding the module by the long sides, align the two holes on the module's short side with the retention pins on the M.2 module holder.  Figure 6. Aligning and Installing the M.2 Mini Storage Module  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308958.jpg)  
---|---  
**Step 2** |  Push on the four corners of the carrier to fully seat it. Make sure the M.2 module is level while seating it into the carrier. The module is correctly seated when it clicks into place and both retention clips are engaged.   
  
* * *

## Installing and Removing a Mini-Storage SSD

The mini-storage module plugs into a motherboard socket to provide additional internal storage. The mini-storage module contains one M.2 form factor SSD. 

To install or remove the mini-storage SSD, see: 

  * Removing a Mini Storage SSD

  * Installing a Mini Storage SSD


  * Removing a Mini Storage SSD
  * Installing a Mini Storage SSD


### Removing a Mini Storage SSD

This topic describes how to remove and replace an M.2 SATA SSD in a mini-storage module. The module has one M.2 SSD socket on its top. 

#### Before you begin

To access the M.2 SSD, the mini-storage module must be removed from the fabric interconnect. If you have not already removed the mini-storage module, do so now. See Removing a Fabric Interconnect M.2 Mini-Storage Module. 

Get a #1 Phillips screwdriver.

#### Procedure

* * *

**Step 1** |  With the mini-storage module removed from the fabric interconnect, use a #1 Phillips-head screwdriver to remove the single screw that secures the M.2 SSD to the carrier.   
---|---  
**Step 2** |  Lift the M.2 SSD from its socket on the carrier. You might need to tilt and slide the SSD to clear the socket opposite the screw.   
  
* * *

#### What to do next

Install an M.2 SSD. See Installing a Mini Storage SSD. 

### Installing a Mini Storage SSD

Use this task to install or reinstall the M.2 SSD onto the mini-storage module. 

#### Before you begin

You will need a #1 Phillips screwdriver to complete this task.

#### Procedure

* * *

**Step 1** |  Position the replacement M.2 drive over the socket on the mini-storage module.  
---|---  
**Step 2** |  Angle the M.2 drive downward and insert the connector-end into the socket on the carrier. The M.2 drive's label must face up.   
**Step 3** |  Press the M.2 drive flat against the carrier.  
**Step 4** |  Install the single screw that secures the end of the M.2 SSD to the carrier. Figure 7.  Showing M.2 Drive Installation  ![](/c/dam/en/us/td/i/400001-500000/480001-490000/483001-484000/483445.jpg)  
  
* * *

---

## Page 6: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x-series-direct/hw/s9108/install/ucs-x-series-direct-9108-100g/m-recycling.html

# Recycling Fabric Interconnect Components

This chapter contains the following topics:

## Recycling the Fabric Interconnect PCBs

Each Cisco UCS X-Series Direct Fabric Interconnect 9108 100G has a printed circuit board (PCB) that is connected to a sheet metal tray. You must: 

  * Disassemble and remove additional parts to gain access to the PCB. 

  * Disconnect the PCB from the sheet metal to recycle the PCB. 

  * Recycle each fabric interconnect in the Cisco UCS X9508 chassis.


Use the following procedure to recycle the fabric interconnects.

### Before you begin

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

**For Recyclers Only!** This procedure is not a standard field-service option. This procedure is for recyclers who will be reclaiming the electronics and sheet metal for proper disposal to comply with local eco design and e-waste regulations. 

* * *  
  
---|---  
  
You will find it helpful to gather the following tools before beginning this procedure:

  * Screwdrivers: One each of T8 and T10 screwdriver, and #1 Phillips.

  * Nut drivers: One 8mm hexagonal.


### Procedure

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

  1. Using a T8 screwdriver, remove the M3 screws on the exterior of the fabric interconnect.  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540712.jpg)
  2. Using a T10 screwdriver, remove the M3 screws on the interior of the fabric interconnect. 
  3. Grasp the bracket and remove it.  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540713.jpg)

  
**Step 4** |  Disconnect additional components and fasteners.

  1. Grasp each airflow baffle and remove it from the tray.  The airflow baffles are attached to the tray by adhesive, so you must pull with enough force to break the adhesion. ![](/c/dam/en/us/td/i/400001-500000/480001-490000/483001-484000/483420.jpg)
  2. Using an 8mm hexagonal nut driver, remove the standoffs.
  3. Using a T10 screwdriver, remove the M3 screws. ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540715.jpg) |  Red circles (![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309210.jpg) )  |  M3 hexagonal standoffs, 4  
---|---  
Blue circles (![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309209.jpg) )  |  M3 screws, 6  
  4. Grasp the PCBA and disconnect it from the sheet metal. 


  
**Step 5** |  Disconnect the remaining components from the PCBA.

  1. Using the T10 screwdriver, remove the M3 screws for the top heatsink.  ![](/c/dam/en/us/td/i/400001-500000/480001-490000/483001-484000/483421.jpg)
  2. Turn the PCBA over so that the bottom is facing up.
  3. Using the #1 Phillips screwdriver and remove the M2 screws. 
  4. Using a pliers, release the four heatsink pushpins.  ![](/c/dam/en/us/td/i/400001-500000/480001-490000/483001-484000/483422.jpg) |  Red circles (![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309210.jpg) )  |  M2 screws for plastic bracket, 4  
---|---  
Blue circles (![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309209.jpg) )  |  Heatsink pushpins, 4  
  5. Turn the PCBA over again so that the top is facing up. 

  6. Grasp the plastic bracket for the M.2 module and remove it.

  7. If the top heat sink is still attached, grasp and remove it. 

  8. Grasp the center heatsink and remove it.

![](/c/dam/en/us/td/i/400001-500000/480001-490000/483001-484000/483423.jpg)

  
**Step 6** |  Recycle the sheet metal and motherboard in compliance with your local recycling and e-waste regulations.   
  
* * *

---

## Page 7: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x-series-direct/hw/s9108/install/ucs-x-series-direct-9108-100g/m-specifications.html

# Technical Specifications

This appendix contains the following topics:

## Physical Specifications for the Fabric Interconnect

The following table shows the physical specifications for the Cisco UCS X-Series Direct 9108 100G Fabric Interconnect.

Specification  |  Value   
---|---  
Height  |  1.71 in. (43.5 mm)  
Width  |  14.92 in (379 mm)  
Depth  |  10.15 in (257.8 mm)  
Weight  |  8.5 lbs. (3.86 kg)  
  
## Environmental Specifications for the Fabric Interconnect

The following table shows the environmental specifications for the Cisco UCS X-Series Direct 9108 100G Fabric Interconnect.

Specification |  Value  
---|---  
Temperature, Operating  |  50° to 95° F (10° to 35° C) at 0 to10,000 ft altitude  
Temperature, Non-Operating |  -40° to 149° F (–40° to 65° C)  
Humidity, Operating |  8% to 80% relative humidity, noncondensing  
Humidity, Non-Operating |  10% to 93% relative humidity, noncondensing  
Altitude, Operating |  0 to 10,000 ft (0 to 3000m); maximum ambient temperature of 30° C  
Altitude, Non-Operating |  40,000 ft (12,000m)

---

## Page 8: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x-series-direct/hw/s9108/install/ucs-x-series-direct-9108-100g/m-obtaining-hardware.html

# Obtaining Hardware  
  
This appendix contains the following topic:

## Obtaining Hardware

Each Cisco UCS X Series Direct 9108 100G Fabric Interconnect interoperates with other required hardware to provide end-to-end network, storage, and compute functionality. 

The following table shows the required hardware to support a fully functioning fabric interconnect. Use the following table when you want to order spares or Cisco UCS X-Series Direct modules to scale out your Cisco UCS X-Fabric deployment. 

Hardware Component |  Description |  Cisco PID  
---|---|---  
Chassis |  UCS X-Series Server Chassis, for example the Cisco UCS X9508 Server Chassis |  UCSX-9508  
ToR Switches, Ethernet |  |   
ToR Switches, Fibre Channel |  |   
Compute Nodes |  UCS X-Series Compute Nodes, for example, the Cisco UCS X210c M7 Compute Node. Cisco UCS M6 Blade Servers are also supported. |  UCSX-210C-M6 UCSX-210C-M7 UCSX-410C-M7  
PCIe Nodes |  UCS X-Series Gen4 PCIe node, for example the Cisco UCS X440p Front Mezzanine PCIe Node |  UCSX-440P  
Cisco UCS X-Fabric Modules (XFMs) |  UCS 9416 X-Fabric module for 9508 chassis Must be deployed as a pair, so two are required per Cisco UCS X9508 Server Chassis |  UCSX-F-9416

---

## Page 9: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x-series-direct/hw/s9108/install/ucs-x-series-direct-9108-100g/ucs-x-series-direct-9108-100g_index.html

> ## Contents  
>   
> C \- D \- F \- I \- L \- M \- R \- T
> 
> ## Index
> 
> C
> 
> COM1/AUX serial port [1](m-connecting.html#task_E5D40586AC324DDD9F18AAE4BDC73FA4)
> 
> console connection [1](m-connecting.html#task_E5D40586AC324DDD9F18AAE4BDC73FA4)
> 
> console serial port [1](m-connecting.html#task_E5D40586AC324DDD9F18AAE4BDC73FA4)
> 
> console settings [1](m-connecting.html#task_E5D40586AC324DDD9F18AAE4BDC73FA4)
> 
> D
> 
> DB9F/RJ-45 adapter [1](m-connecting.html#task_E5D40586AC324DDD9F18AAE4BDC73FA4)
> 
> F
> 
> fabric interconnect fan, installing [1](m-servicing.html#Cisco_Task_in_List_GUI.dita_6da08bac-e5f2-499d-8b2c-61efa38b7a85)
> 
> fabric interconnect PCB, recycling [1](m-recycling.html#Cisco_Task_in_List_GUI.dita_5667164d-680e-4432-93b5-4c21f361e414)
> 
> fabric interconnect, installing [1](m-installing.html#Cisco_Task_in_List_GUI.dita_8b4b666c-e890-4d76-bba0-2720cedc21e8)
> 
> fabric interconnect, recycling [1](m-recycling.html#Cisco_Task_in_List_GUI.dita_5667164d-680e-4432-93b5-4c21f361e414)
> 
> fabric interconnect, removing [1](m-installing.html#Cisco_Task_in_List_GUI.dita_214ffc57-18df-4e50-90d6-d08f707177fb)
> 
> fan, removing [1](m-servicing.html#Cisco_Task_in_List_GUI.dita_9c84a39b-e540-4afa-bedd-ea0f62e44b4d)
> 
> I
> 
> installing M.2 SSD [1](m-servicing.html#installing-mini-storage-ssd)
> 
> installing, fabric interconnect [1](m-installing.html#Cisco_Task_in_List_GUI.dita_8b4b666c-e890-4d76-bba0-2720cedc21e8)
> 
> installing, fabric interconnect fan [1](m-servicing.html#Cisco_Task_in_List_GUI.dita_6da08bac-e5f2-499d-8b2c-61efa38b7a85)
> 
> installing, M.2 mini storage module [1](m-servicing.html#Cisco_Task_in_List_GUI.dita_7af16001-2009-4509-8726-e82b1485260d)
> 
> installing, top cover [1](m-servicing.html#installing-the-top-cover)
> 
> L
> 
> LED
> 
> fabric interconnect status [1](m-overview.html#Cisco_Reference.dita_806ab63e-975b-457b-9da4-ea160314d43e)
> 
> fan status [1](m-overview.html#Cisco_Reference.dita_806ab63e-975b-457b-9da4-ea160314d43e)
> 
> management port status [1](m-overview.html#Cisco_Reference.dita_806ab63e-975b-457b-9da4-ea160314d43e)
> 
> M
> 
> M.2 mini storage module, installing [1](m-servicing.html#Cisco_Task_in_List_GUI.dita_7af16001-2009-4509-8726-e82b1485260d)
> 
> M.2 mini storage module, removing [1](m-servicing.html#Cisco_Task_in_List_GUI.dita_097a338b-516b-46a6-8353-9976ded47067)
> 
> M.2 SSD, installing [1](m-servicing.html#installing-mini-storage-ssd)
> 
> M.2 SSD, removing [1](m-servicing.html#removing-mini-storage-ssd)
> 
> R
> 
> recycling, fabric interconnect PCB [1](m-recycling.html#Cisco_Task_in_List_GUI.dita_5667164d-680e-4432-93b5-4c21f361e414)
> 
> removing M.2 SSD [1](m-servicing.html#removing-mini-storage-ssd)
> 
> removing, fabric interconnect [1](m-installing.html#Cisco_Task_in_List_GUI.dita_214ffc57-18df-4e50-90d6-d08f707177fb)
> 
> removing, fan [1](m-servicing.html#Cisco_Task_in_List_GUI.dita_9c84a39b-e540-4afa-bedd-ea0f62e44b4d)
> 
> removing, M.2 mini storage module [1](m-servicing.html#Cisco_Task_in_List_GUI.dita_097a338b-516b-46a6-8353-9976ded47067)
> 
> removing, top cover [1](m-servicing.html#removing-the-top-cover)
> 
> RJ-45 connectors
> 
> rollover cable [1](m-connecting.html#task_E5D40586AC324DDD9F18AAE4BDC73FA4)
> 
> T
> 
> top cover, installing [1](m-servicing.html#installing-the-top-cover)
> 
> top cover, removing [1](m-servicing.html#removing-the-top-cover)

---
