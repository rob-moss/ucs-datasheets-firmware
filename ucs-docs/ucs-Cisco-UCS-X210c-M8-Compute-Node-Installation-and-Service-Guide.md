# Cisco UCS X210c M8 Installation Guide

| | |
|---|---|
| **URL Title** | Cisco UCS X210c M8 Installation Guide |
| **URL** | https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x210c-m8/install/b-x210c-m8-install.html |
| **Long URL** |  |
| **HTML Title** | Cisco UCS X210c M8 Compute Node Installation and Service Guide |
| **Source file** | `ucs-docs-raw/html/b-x210c-m8-install.html` |
| **File type** | HTML |
| **Fetched on** | 2026-08-24 09:16:53 |

---

## Page 1: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x210c-m8/install/b-x210c-m8-install.html

![Clear Contents of Search](/etc/designs/cdc/fw/i/ic_clear_gray.png)

---

## Page 2: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x210c-m8/install/b-x210c-m8-install/m-preface.html

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

## Page 3: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x210c-m8/install/b-x210c-m8-install/m-overview.html

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

## Page 4: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x210c-m8/install/b-x210c-m8-install/m-installing-the-compute-node.html

# Installing the Compute Node  
  
This chapter contains the following topics:

## Removing a Compute Node Blank

Do not operate the Cisco UCS X9508 chassis with an empty compute node slot. Fill any empty compute node slots with either a blank or a compute node. 

Use this task to remove a compute node blank.

### Procedure

* * *

**Step 1** |  Grasp the compute node blank by the finger holds.   
---|---  
**Step 2** |  Pull the blank towards you until it is completely removed from the chassis.  Notice that the module blank has indicators that show how to orient the blank. You will use this information when you install a blank.  Figure 1. Removing a Compute Node Blank  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309103.jpg)  
  
* * *

## Installing a Compute Node Blank

If you remove a compute node, and you will not be installing another compute node, you must install a node blank (UCSX-9508-FSBK). Do not operate the UCS X9508 chassis with an empty compute node slot. The minimum configuration is 1 installed compute node, so in this configuration you need 7 module blanks installed. 

Compute node blanks are interchangeable within the same chassis or other Cisco UCS X9508 chassis. 

Use this task to install a compute node blank

### Procedure

* * *

**Step 1** |  Grasp the blank by the finger holds.   
---|---  
**Step 2** |  Hold the module blank vertically and align the module blank with the slot.  The module blank has indicators that show how to orient the blank. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309104.jpg)  
**Step 3** |  Keeping the compute node blank vertical, slide it into the slot until the blank is flush with the face of the chassis.  Figure 2. Installing a Compute Node Blank  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308917.jpg)  
  
* * *

## Removing a Compute Node

You must decommission the compute node using Cisco UCS management software (Cisco Intersight or Cisco UCS Manager) before physically removing the compute node. 

Do not operate the chassis with an empty compute node slot. If you will not be installing a compute node in an empty slot, install a compute node blank (UCSX-9508-FSBK) to cover the empty slot. 

### Procedure

* * *

**Step 1** |  Turn off the compute node by using Cisco UCS management software.   
---|---  
**Step 2** |  Press the release button at the center of the compute node's faceplate to disengage the ejector handles.   
**Step 3** |  Grasp the ejector handles and pull them outward so that they arc vertically away from each other. While moving the compute node handles, you might feel some resistance. This resistance is normal. It occurs because the connectors at the rear of the compute node are unseating from the corresponding sockets in the chassis.  Also, when the compute node disconnects from the midplane, the compute node powers off. |  **Caution** |  Whenever a compute node is removed, you must wait at least 20 seconds before inserting the compute node back into the chassis.  
---|---  
Figure 3. Removing a Compute Node  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309119.jpg)  
**Step 4** |  Grasp the compute node handles and slide it partially out of the chassis.  Make sure to keep the compute node vertical while removing it.  
**Step 5** |  Place your other hand underneath the compute node to support it and slide the compute node completely out of the chassis.   
**Step 6** |  Once removed, place the compute node on an antistatic mat or antistatic foam if you are not immediately reinstalling it.   
**Step 7** |  Do one of the following: 

  1. If you will be installing another compute node, see Installing a Compute Node. 
  2. If the compute node slot is to remain empty, reinstall the compute node blank panels (UCSX-9508-FSBK) to maintain proper thermal temperatures and to keep dust out of the chassis. 

  
  
* * *

## Installing a Compute Node

### Before you begin

The compute node must have its cover installed before installing it into the chassis to ensure adequate airflow.

### Procedure

* * *

**Step 1** |  Remove a compute node blank. See Removing a Compute Node.  |  **Caution** |  Whenever a compute node is removed, you must wait at least 20 seconds before inserting the compute node back into the chassis.  
---|---  
**Step 2** |  Press the release button at the center of the compute node faceplate to release the ejectors. |  **Note** |  While you are inserting the compute node, keep the ejectors open.  
---|---  
**Step 3** |  Holding the compute node vertical, align it with the empty module bay in the chassis.  The compute node is correctly aligned when the compute node top cover is pointing to the left.  Figure 4. Aligning and Installing a Compute Node  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309120.jpg)  
**Step 4** |  When the compute node is almost completely installed, grasp the ejector handles and arc them toward each other.  This step seats the compute node into the connector. The compute node should power up.  
**Step 5** |  Push the ejectors until they are parallel with the face of the compute node.  When the compute node is completely installed, the retention latches at the end of each handle click into place.   
**Step 6** |  Configure the compute node as needed through Cisco UCS management software. See Compute Node Configuration.   
  
* * *

## Compute Node Configuration

Cisco UCS M8 compute nodes, such as the Cisco UCS X210c M8, can be configured and managed using the Cisco UCS management software, either: 

  * Cisco Intersight management platform in Intersight Managed Mode (Cisco Intersight Managed Mode). For details, see the Cisco Intersight Managed Mode Configuration Guide, which is available at the following URL: [Cisco Intersight Managed Mode Configuration Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Intersight_Managed_Mode_Configuration_Guide.html)

  * Cisco UCS Manager (UCSM), version 4.3(2) or later. For details, see the latest version of the Cisco UCS Manager Administration Management Guide 4.3 which is available at the following URL: [Cisco UCS Manager Administration Management Guide 4.3](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Admin-Management/4-3/b_cisco_ucs_admin_mgmt_guide_4-3.html)


---

## Page 5: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x210c-m8/install/b-x210c-m8-install/m-servicing-the-compute-node.html

# Servicing the Compute Node

This chapter contains the following topics:

## Removing and Installing the Compute Node Cover

The top cover of the Cisco UCS X210c M8 Compute Node can be removed to allow access to internal components, some of which are field-replaceable. The green button on the top cover releases the compute node so that it can be removed from the compute node. 

  * Removing a Compute Node Cover

  * Installing a Compute Node Cover


  * Removing a Compute Node Cover
  * Installing a Compute Node Cover


### Removing a Compute Node Cover

To remove the cover of the Cisco UCS X210c M8 Compute Node, follow these steps: 

#### Procedure

* * *

**Step 1** |  Press and hold the button down (1, in the figure below).   
---|---  
**Step 2** |  While holding the back end of the cover, slide it back, then pull it up (2).  By sliding the cover back, you enable the front edge to clear the metal lip on the rear of the front mezzanine module.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308975.jpg)  
  
* * *

### Installing a Compute Node Cover 

Use this task to install a removed top cover for the UCS X210c M8 compute node. 

#### Procedure

* * *

**Step 1** |  Insert the cover angled so that it hits the stoppers on the base.  
---|---  
**Step 2** |  Lower the compute node's cover until it reaches the bottom.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309646.jpg)  
**Step 3** |  Keeping the compute node's cover flat, slide it forward until the release button clicks.   
  
* * *

## Internal Components

The following illustration shows the location of internal components on the compute node. 

![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472725.png)

1 |  Front mezzanine module slot |  2 |  Mini-Storage module connector, which supports one mini-storage module with up to two M.2 SATA or M.2 NVMe drives.  
---|---|---|---  
3 |  Front mezzanine slot connectors |  4 |  CPU 1, which supports Sixth Generation Intel Xeon Scalable Processors.  
5 |  DIMM Slots |  6 |  Debug connector Only for use by Cisco personnel.  
7 |  CPU 2, which supports Sixth Generation Intel Xeon Scalable Processors. |  8 |  Motherboard USB Connector  
9 |  TPM Connector |  10 |  Rear mezzanine slot.  
11 |  Bridge Card slot, which connects rear mezzanine slot and the mLOM/VIC slot |  12 |  mLOM/VIC slot that supports zero or one Cisco VIC or Cisco X-Series 100 Gbps mLOM  
  
## Replacing a Drive

You can remove and install some drives without removing the compute node from the chassis. All drives have front-facing access, and they can be removed and inserted by using the ejector handles. 

The SAS/SATA or NVMe drives supported in this compute node come with the drive sled attached. Spare drive sleds are not available. 

Before upgrading or adding a drive to a running compute node, check the service profile through Cisco UCS management software and make sure the new hardware configuration will be within the parameters allowed by the management software. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

To prevent ESD damage, wear grounding wrist straps during these procedures. 

* * *  
  
---|---  
  
  * NVMe SSD Requirements and Restrictions
  * Enabling Hot Plug Support
  * Removing a Drive
  * Installing a Drive
  * Basic Troubleshooting: Reseating a SAS/SATA Drive


### NVMe SSD Requirements and Restrictions

For 2.5-inch NVMe SSDs, be aware of the following:

  * NVMe 2.5 SSDs support booting only in UEFI mode. Legacy boot is not supported. 

UEFI boot mode can be configured through Cisco UCS management software. For information about Cisco UCS management software, see [Compute Node Configuration](m-installing-the-compute-node.html#Cisco_Reference.dita_d5beb410-8b0c-44e7-836c-7a86d663e54e). 

  * NVME U.3 SSDs connect to the RAID controller so RAID is supported for these drives. 

  * UEFI boot is supported in all supported operating systems. 


### Enabling Hot Plug Support

Surprise and OS-informed hot plug is supported with the following conditions:

  * VMD must be enabled to support hot plug. 

  * VMD must be enabled before installing an OS on the drive. 

  * If VMD is not enabled, surprise hot plug is not supported, and you must do OS-informed hotplug instead.

  * VMD is required for both surprise hot plug and drive LED support. 


### Removing a Drive

Use this task to remove a SAS/SATA or NVMe drive from the compute node. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Do not operate the system with an empty drive bay. If you remove a drive, you must reinsert a drive or cover the empty drive bay with a drive blank. 

* * *  
  
---|---  
  
#### Procedure

* * *

**Step 1** |  Push the release button to open the ejector, and then pull the drive from its slot.  |  **Caution** |  To prevent data loss, make sure that you know the state of the system before removing a drive.  
---|---  
  
![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308996.jpg)  
  
**Step 2** |  Place the drive on an antistatic mat or antistatic foam if you are not immediately reinstalling it in another compute node.  
**Step 3** |  Install a drive blanking panel to maintain proper airflow and keep dust out of the drive bay if it will remain empty.   
  
* * *

#### What to do next

Cover the empty drive bay. Choose the appropriate option:

  * Installing a Drive

  * Installing a Drive Blank


### Installing a Drive

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

For hot installation of drives, after the original drive is removed, you must wait for 20 seconds before installing a drive. Failure to allow this 20-second wait period causes the Cisco UCS management software to display incorrect drive inventory information. If incorrect drive information is displayed, remove the affected drive(s), wait for 20 seconds, then reinstall them. 

* * *  
  
---|---  
  
To install a SAS/SATA or NVMe drive in the compute node, follow this procedure:

#### Procedure

* * *

**Step 1** |  Place the drive ejector into the open position by pushing the release button.   
---|---  
**Step 2** |  Gently slide the drive into the empty drive bay until it seats into place.  
**Step 3** |  Push the drive ejector into the closed position. You should feel the ejector click into place when it is in the closed position. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309002.jpg)  
  
* * *

### Basic Troubleshooting: Reseating a SAS/SATA Drive

Sometimes it is possible for a false positive UBAD error to occur on SAS/SATA HDDs installed in the compute node. 

  * Only drives that are managed by the UCS MegaRAID controller are affected. 

  * Both SFF and LFF form factor drives can be affected.

  * Drives can be affected regardless of whether they are configured for hot plug or not.

  * The UBAD error is not always terminal, so the drive is not always defective or in need of repair or replacement. However, it is also possible that the error is terminal, and the drive will need replacement. 


**Before submitting the drive to the RMA process** , it is a best practice to reseat the drive. If the false UBAD error exists, reseating the drive can clear it. If successful, reseating the drive reduces inconvenience, cost, and service interruption, and optimizes your compute node uptime. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Reseat the drive only if a UBAD error occurs. Other errors are transient, and you should not attempt diagnostics and troubleshooting without the assistance of Cisco personnel. Contact Cisco TAC for assistance with other drive errors. 

* * *  
  
---|---  
  
To reseat the drive, see Reseating a SAS/SATA Drive. 

  * Reseating a SAS/SATA Drive


#### Reseating a SAS/SATA Drive

Sometimes, SAS/SATA drives can throw a false UBAD error, and reseating the drive can clear the error. 

Use the following procedure to reseat the drive. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

This procedure might require powering down the server. Powering down the server will cause a service interruption.

* * *  
  
---|---  
  
##### Before you begin

Before attempting this procedure, be aware of the following:

  * Before reseating the drive, it is a best practice to back up any data on it.

  * When reseating the drive, make sure to reuse the same drive bay.

  * Do not move the drive to a different slot.

  * Do not move the drive to a different server.

  * If you do not reuse the same slot, the Cisco UCS management software (for example, Cisco IMM) might require a rescan/rediscovery of the server. 

  * When reseating the drive, allow 20 seconds between removal and reinsertion.


##### Procedure

* * *

**Step 1** |  Attempt a hot reseat of the affected drive(s). For a front-loading drive, see Removing a Drive.  |  **Note** |  While the drive is removed, it is a best practice to perform a visual inspection. Check the drive bay to ensure that no dust or debris is present. Also, check the connector on the back of the drive and the connector on the inside of the server for any obstructions or damage.  Also, when reseating the drive, allow 20 seconds between removal and reinsertion.   
---|---  
**Step 2** |  During boot up, watch the drive's LEDs to verify correct operation.  See [Interpreting LEDs](m-overview.html#Cisco_Reference.dita_806ab63e-975b-457b-9da4-ea160314d43e).   
**Step 3** |  If the error persists, cold reseat the drive, which requires a server power down. Choose the appropriate option:

  1. Use your server management software to gracefully power down the server.  See the appropriate Cisco UCS management software documentation.
  2. If server power down through software is not available, you can power down the server by pressing the power button. See [Compute Node Front Panel](m-overview.html#Cisco_Concept.dita_e57757cc-ebfe-45bc-94ca-21d942b7ac07). 
  3. Reseat the drive as documented in Step 1. 
  4. When the drive is correctly reseated, restart the server, and check the drive LEDs for correct operation as documented in Step 2. 

  
**Step 4** |  If hot and cold reseating the drive (if necessary) does not clear the UBAD error, choose the appropriate option: 

  1. Contact Cisco Systems for assistance with troubleshooting.
  2. Begin an RMA of the errored drive.

  
  
* * *

## Removing a Drive Blank

A maximum of six SAS/SATA or NVMe drives are contained in the front mezzanine storage module as part of the drive housing. The drives are front facing, so removing them does not require any disassembly. 

Use this procedure to remove a drive blank from the compute node. 

### Procedure

* * *

**Step 1** |  Grasp the drive blank handle.   
---|---  
**Step 2** |  Slide the drive blank out of the slot.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308990.jpg)  
  
* * *

### What to do next

Cover the empty drive bay. Choose the appropriate option: 

  * Installing a Drive

  * Installing a Drive Blank


## Installing a Drive Blank

Use this task to install a drive blank. 

### Procedure

* * *

**Step 1** |  Align the drive blank so that the sheet metal is facing down.   
---|---  
**Step 2** |  Holding the blank level, slide it into the empty drive bay.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308999.jpg)  
  
* * *

## Replacing the Front Mezzanine Module

The front mezzanine module is a steel cage that contains the compute node's storage devices or a mix of GPUs and drives. The front mezzanine storage module can contain any of the following storage configurations: 

  * NVMe U.3 drives 

  * SAS/SATA drives

  * Cisco L4-MEZZ GPUs plus up to two U.3 NVMe drives

  * E3.S 1TB PCIe drives


In the front mezzanine slot, the compute node can use one of the following front storage module options:

  * A front mezzanine blank (UCSX-M8A-FMEZZBLK ) for systems without local disk requirements.

  * Compute Pass Through Controller (UCSX-X10C-PT4F-D): supports up to six hot pluggable 15mm NVMe drives directly connected to CPU 1. 

  * MRAID Storage Controller Module (UCSX-X10C-RAIDF):

  * Supports a mixed drive configuration of up to six SAS, SATAdrives. With a mix of SAS/SATA and NVMe drives are supported in slots one through four only. 

  * Provides HW RAID support for SAS/SATA drives in multiple RAID groups and levels.

  * Supports NVMe U.3 drives in slots 1 through 6 and can be configured into multiple RAID groups and levels similar to SAS/SATA drives. 

  * Supports a mix of SAS/SATA and NVMe U.3 drives behind the MRAID controller. However, these NVMe drives and SAS/SATA drives cannot be combined in the same RAID group. 

NVME U.3 drives can be combined to make RAID groups separately. Also, SAS/SATA drives can be formed into different RAID groups, and the different RAID groups can co-exist in the same MRAID storage setup. 

  * The front mezzanine module also contains the SuperCap module. For information about replacing the SuperCap module, see Replacing the SuperCap Module. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The SuperCap module is only needed when the MRAID Storage Controller module (UCSX-RAID-M1L6) or Compute RAID Controller (UCSX-X10C-RAIDF) is installed. 

* * *  
  
---|---  
  * A compute and storage option (UCSX-X10C-GPUFM) consisting of a GPU adapter supporting zero, one, or two Cisco L4-MEZZ GPUs (UCSX-GPU-L4-MEZZ) plus zero, one, or two U.3 NVMe SSDs. 

  * A Tri-mode M1 front mezzanine module (UCSX-RAID-M1L6). Each Tri-mode M1 front mezzanine module consists of the following components:

  * Up to six (6) SAS/SATA/NVMe SSD drives. Each drive slot supports either SAS, SATA or NVMe U.3 SSDs (RAID Controller)

  * A Front Mezzanine Pass Through Controller for E3.S drives (UCSX-X10C-PTE3).

  * The front mezzanine E3.S module supports up to nine E3.S PCIe drives.


The front mezzanine module can be removed and installed as a whole unit to give easier access to the storage drives that it holds. Or, you can leave the front mezzanine module installed because SAS/SATA and the NVMe drives are accessible directly through the front of the front mezzanine panel and are hot pluggable. 

To replace the front mezzanine module, use the following topics: 

  * Removing the Front Mezzanine Module

  * Installing the Front Mezzanine Module


  * Front Mezzanine Module Guidelines
  * Removing the Front Mezzanine Module
  * Installing the Front Mezzanine Module


### Front Mezzanine Module Guidelines

Be aware of the following guidelines for the front mezzanine slot:

  * The compute node supports the following configuration options:

  * For MRAID Storage Controller Module (UCSX-X10C-RAIDF), M.2 Mini Storage, and NVMe storage, only UEFI boot mode is supported.

  * (UCSX-X10C-GPUFM) that supports up to two Cisco L4-MEZZ GPUs 

  * (UCSX-GPU-L4-MEZZ) and up to two NVMe U.3 drives in the front mezzanine slot. For information about the GPU-based front mezzanine option, see the [Cisco UCS X10c Front Mezzanine GPU Module Installation and Service Guide](https://www-author3.cisco.com/content/en/us/td/docs/unified_computing/ucs/x/hw/x10c-gpu-module/install/cisco-ucs-x10c-front-mezzanine-gpu-install-guide.html). 

  * (UCSX-RAID-M1L6) front mezzinne that supports up to six (6) SAS/SATA/NVMe SSD drives. 

  * Each drive slot supports either SAS, SATA or NVMe U.3 SSDs (RAID Controller). For more information about RAID controller based front mezzanine option, see the [Cisco UCS X10c Front Mezzanine GPU Module Installation and Service Guide](https://www-author3.cisco.com/content/en/us/td/docs/unified_computing/ucs/x/hw/x10c-gpu-module/install/cisco-ucs-x10c-front-mezzanine-gpu-install-guide.html). 

  * (UCSX-X10C-PTE3) front mezzznine that supports up to six (9) Nine E3.S 1T PCIe5 drives. 

  * Each drive slot supports either SAS, SATA or NVMe U.3 SSDs (RAID Controller). For more information about E3.S drives based front mezzanine option, see the [Cisco UCS X10c Pass Through Controller for E3.S Installation and Service Guide](https://www-author3.cisco.com/content/en/us/td/docs/unified_computing/ucs/x/hw/x10c-e3s/install/b-cisco-ucs-x10c-compute-pass-through-controller-e3s.html). 

. 
  * (UCSX-X10C-PT4F) Computer Pass Through Controller. The front mezzanine supports:

  * Up to 6 x 2.5-inch SAS and SATA RAID-compatible SSDs or NVMe PCIe drives. 

  * A mixture of up to six SAS/SATA or NVMe drives or up to two GPUs and up to two NVMe drives. 

For more information about E3.S drives based front mezzanine option, see the [Cisco UCS X210c M7 Compute Node Installation and Service Guide](https://www-author3.cisco.com/content/en/us/td/docs/unified_computing/ucs/x/hw/x210c-m7/install/b-cisco-ucs-x210c-m7-install-guide/m-servicing-the-compute-node.html). 


### Removing the Front Mezzanine Module

Use the following procedure to remove the front mezzanine module. This procedure applies to the following modules:

  * Computer Pass Through Controller (UCSX-X10C-PT4F)

  * Compute RAID Controller with LSI 3900 (UCSX-X10C-RAIDF)

  * Compute Node GPU Front Mezz (UCSX-X10C-GPUFM)

  * Compute Pass Through Controller for E3.S (UCSX-X10C-PTE3)

  * 24G Tri-Mode M1 RAID Controller (UCSX-RAID-M1L6)


#### Before you begin

To remove the front mezzanine module, you need a T8 screwdriver and a #2 Phillips screwdriver. 

#### Procedure

* * *

**Step 1** |  If the compute node's cover is not already removed, remove it now. Remove the compute node cover.  See Removing a Compute Node Cover.   
---|---  
**Step 2** |  Remove the securing screws:

  1. Using a #2 Phillips screwdriver, loosen the two captive screws on the top of the front mezzanine module.  |  **Note** |  This step may be skipped if removing the front mezzanine blank (UCSX-M8A-FMEZZBLK).  
---|---  
  2. Using a T8 screwdriver, remove the two screws on each side of the compute node that secure the front mezzanine module to the sheet metal. 

![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308992.jpg)


  
**Step 3** |  Making sure that all the screws are removed, lift the front mezzanine module to remove it from the compute node.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/309000.jpg)  
  
* * *

#### What to do next

To install the front mezzanine module, see Installing the Front Mezzanine Module

### Installing the Front Mezzanine Module

Use the following procedure to install the front mezzanine module. This procedure applies to the following modules:

  * Front mezzanine blank (UCSX-M8A-FMEZZBLK)

  * Compute Pass Through Controller (UCSX-X10C-PT4F-D)

  * MRAID Storage Controller Module (UCSX-X10C-RAIDF)

  * Compute and storage option (UCSX-X10C-GPUFM-D) 

  * Tri-mode RAID Controller(UCSX-RAID-M1L6)

  * E3.S Pass Through Controller (UCSX-X10C-PTE3)


#### Before you begin

To install the front mezzanine module, you need a T8 screwdriver and a #2 Phillips screwdriver.

#### Procedure

* * *

**Step 1** |  Align the front mezzanine module with its slot on the compute node.   
---|---  
**Step 2** |  Lower the front mezzanine module onto the compute node, making sure that the screws and screwholes line up.  
**Step 3** |  Secure the front mezzanine module to the compute node. 

  1. Using a #2 Phillips screwdriver, tighten the captive screws on the top of the front mezzanine module.  |  **Note** |  This step may be skipped if installing the front mezzanine blank (UCSX-M8A-FMEZZBLK).  
---|---  
![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308992.jpg)
  2. Using a T8 screwdriver, insert and tighten the four screws, two on each side of the sever node. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308993.jpg)


  
  
* * *

#### What to do next

If you removed the drives from the front mezzanine module, reinstall them now. See Installing a Drive. 

## Servicing the Mini Storage Module

The compute node has a mini-storage module option that plugs into a motherboard socket to provide additional internal storage. The module sits vertically behind the left side front panel. See Internal Components. 

Two configurations of mini storage module are supported, one with an integrated RAID controller card, and one without.

  * Replacing a Boot-Optimized M.2 RAID Controller Module or NVMe Pass-Through Module
  * Replacing an M.2 SATA or M.2 NVMe SSD


### Replacing a Boot-Optimized M.2 RAID Controller Module or NVMe Pass-Through Module

The Cisco Boot-Optimized M.2 RAID Controller for M.2 SATA drives or the NVMe Pass-Through Controller for M.2 NVMe drives connects to the mini-storage module socket on the motherboard. Each of the following components contains two module slots for M.2 drives: 

  * The Cisco UCSX Front panel with M.2 RAID controller for SATA drives (UCSX-M2I-HWRD-FPS). This component has an integrated 6-Gbps SATA RAID controller that can control the SATA M.2 drives in a RAID 1 array. 

  * The Cisco UCSX Front panel with M.2 Pass Through controller for NVME drives (UCSX-M2-PT-FPN). The M.2 NVMe drives are not configurable in a RAID group. 


  * Cisco Boot-Optimized M.2 RAID Controller Considerations
  * Removing the M.2 RAID Controller Module or NVMe Pass-Through Module
  * Installing the M.2 RAID Controller Module or NVMe Pass-Through Controller Module


#### Cisco Boot-Optimized M.2 RAID Controller Considerations

Review the following considerations:

  * This controller supports RAID 1 (single volume) and JBOD mode.

  * A SATA M.2 drive in slot 1 is located on the right side, or front, of the module when installed. This drive faces the interior of the compute node. This drive is the first SATA device. 

  * A SATA M.2 drive in slot 2 is located on the left side, or back, of the module when installed. This drive faces the compute node's sheet metal wall. This drive is the second SATA device. 

  * The name of the controller in the software is MSTOR-RAID.

  * A drive in slot 1 is mapped as drive 253; a drive in slot 2 is mapped as drive 254.

  * When using RAID, we recommend that both SATA M.2 drives are the same capacity. If different capacities are used, the smaller capacity of the two drives is used to create a volume and the rest of the drive space is unusable. 

JBOD mode supports mixed capacity SATA M.2 drives.

  * Hot-plug replacement is _not_ supported. The compute node must be powered off. 

  * Monitoring of the controller and installed SATA M.2 drives can be done using Cisco UCS management software. They can also be monitored using other utilities such as UEFI HII, and Redfish. 

  * The SATA M.2 drives can boot in UEFI mode only. Legacy boot mode is not supported.

  * If you replace a single SATA M.2 drive that was part of a RAID volume, rebuild of the volume is auto-initiated after the user accepts the prompt to import the configuration. If you replace both drives of a volume, you must create a RAID volume and manually reinstall any OS. 

  * We recommend that you erase drive contents before creating volumes on used drives from another compute node. The configuration utility in the compute node BIOS includes a SATA secure-erase function. 


#### Removing the M.2 RAID Controller Module or NVMe Pass-Through Module

This topic describes how to remove a Cisco Boot-Optimized M.2 RAID Controller or a Cisco NVMe Pass-Through Controller:

  * The Cisco UCSX Front panel with M.2 RAID controller for SATA drives (UCSX-M2I-HWRD-FPS). 

  * The Cisco UCSX Front panel with M.2 Pass-Through module for NVME drives (UCSX-M2-PT-FPN). 


Both types of controller board have two slots, one for each M.2 drive:

  * one M.2 slot (Slot 1) for either a SATA drive (in UCSX-M2I-HWRD-FPS) or an NVMe drive (in UCSX-M2-PT-FPN). The drive in this slot faces the interior of the compute node. 

  * one M.2 slot (Slot 2) for either a SATA drive (in UCSX-M2I-HWRD-FPS) or an NVMe drive (in UCSX-M2-PT-FPN). The drive in this slot faces the chassis sheetmetal wall. 

  * Drive slot numbering differs depending on which Cisco management tool you are using and which component is being managed.

Component |  Cisco Management Tool  
---|---  
Intersight (IMM) |  UCS Manager (UCSM)  
RAID Controller |  Slot 1 contains Drive 253 Slot 2 contains Drive 254 |  Slot 1 contains Drive 253 Slot 2 contains Drive 254  
NVMe Pass-Through Controller |  Slot 1 contains Drive 253 Slot 2 contains Drive 254 |  Slot 1 contains Drive 32 Slot 2 contains Drive 33  


Each controller can be populated with up to two M.2 drives of the correct type, either SATA for the RAID controller or NVMe for the Pass-Through controller. Single M.2 SATA or NVMe drives are supported. You cannot mix M.2 drive types in the same controller. 

To remove the controller or the M.2 drives, the front mezzanine module must be removed first. 

##### Procedure

* * *

**Step 1** |  Remove the controller from the compute node:

  1. Decommission, power off, and remove the compute node from the chassis. 
  2. Remove the top cover from the compute node as described in Removing and Installing the Compute Node Cover. 

  
---|---  
**Step 2** |  If you have not already done so, remove the front mezzanine module.  See Removing the Front Mezzanine Module.   
**Step 3** |  Remove the controller.

  1. Locate the controller in the front corner of the server along the compute node's sidewall.
  2. Using a #2 Phillips screwdriver, loosen the captive screw that secures the module to the motherboard. 
  3. At the end opposite the front panel, grasp the module and pull up in an arc to disconnect the controller from its motherboard socket. 
  4. Holding the controller at an angle, slide it away from the front panel and lift it up to disengage the LEDs and buttons from their cutouts in the front panel.  |  **Caution** |  If you feel resistance while lifting the controller, make sure that the LEDs and buttons are not still seated in the front panel.   
---|---  
  
![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472285.jpg)


  
**Step 4** |  If you are transferring M.2 drives from the old controller to a replacement controller, do that before installing the replacement controller:  |  **Note** |  Any previously configured volume and data on the drives are preserved when the M.2 drives are transferred to the new controller. The system will boot the existing OS that is installed on the drives.   
---|---  
  
  1. Use a #1 Phillips-head screwdriver to remove the single screw that secures the M.2 drive to the carrier.

  2. Lift the M.2 drive from its slot on the carrier.

  3. Position the replacement M.2 drive over the slot on the controller board.

  4. Angle the M.2 drive downward and insert the connector-end into the slot on the carrier. The M.2 drive's label must face up.

  5. Press the M.2 drive flat against the carrier.

  6. Install the single screw that secures the end of the M.2 SSD to the carrier.

  7. Turn the controller over and install the second M.2 drive.


  
  
* * *

#### Installing the M.2 RAID Controller Module or NVMe Pass-Through Controller Module

Use this task to install the RAID controller or NVME Pass-through controller module. 

##### Before you begin

This topic describes how to remove a Cisco Boot-Optimized M.2 RAID Controller or a Cisco NVMe Pass-Through Controller:

  * The Cisco UCSX Front panel with M.2 RAID controller for SATA drives (UCSX-M2I-HWRD-FPS). 

  * The Cisco UCSX Front panel with M.2 Pass-Through module for NVME drives (UCSX-M2-PT-FPN). 


Each type of controller mounts vertically on the motherboard, and the M.2 drive sockets are positioned vertically on the controller. 

##### Procedure

* * *

**Step 1** |  Install the controller to its socket on the motherboard:

  1. Position the controller over the socket, making sure the golden fingers on the connector are facing down. 
  2. Lower the controller into the chassis at an angle and insert the LEDs and buttons into their cutouts on the front panel.
  3. Holding the controller level, align the captive screw with its screwhole and the golden fingers with their socket on the motherboard. 
  4. Carefully push down on the controller to seat the golden fingers into the socket. 
  5. Use a #2 Phillips screwdriver to tighten the controller onto the threaded standoff.  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472286.jpg)

  
---|---  
**Step 2** |  Reinstall the front mezzanine module.  
**Step 3** |  Return the compute node to service:

  1. Replace the top cover on the compute node.
  2. Reinstall the compute node and allow it to power up and be automatically reacknowledged, reassociated, and recommissioned.

  
  
* * *

### Replacing an M.2 SATA or M.2 NVMe SSD

M.2 SATA and NVMe SSD cards can be installed in vertical drive bays. One drive bay, or slot, is on each side of the M.2 module carrier. 

There are some specific rules for populating mini-storage M.2 SSD cards: 

  * Each carrier supports a maximum of two M.2 cards. Do not mix SATA and NVMe SSD cards in the same mini-storage module. Replacement cards are available from Cisco as pairs. 

  * When installed in the compute node, the M.2 SSDs are mounted vertically.

  * M.2 slot 1 is located on the right side, or front, of the module when installed. This drive faces inward towards the interior the compute node. 

  * M.2 slot 2 is located on the left side, or back, of the module when installed. This drive faces outward towards the compute node sheetmetal wall. 

  * Drive slot numbering depends on the M.2 SSD type and which Cisco Management tool you are using.

  * **M.2 SATA SSD** : Slot 1 contains Drive 253 in both Intersight (IMM) and UCS Manager (UCSM). 

  * **M.2 SATA SSD** : Slot 2 contains Drive 254 in both IMM and UCSM. 

  * **M.2 NVMe SSD** : Slot 1 contains Drive 253 in IMM, but Slot 1 contains Drive 32 in UCSM. 

  * **M.2 NVMe SSD** : Slot 2 contains Drive 254 in IMM, but Slot 2 contains Drive 33 in UCSM. 

  * If your compute node contains only one M.2 SATA or NVMe SSD, it can be installed in either slot. 

  * Dual SATA M.2 SSDs can be configured in a RAID 1 array through the BIOS Setup Utility's embedded SATA RAID interface and configured through IMM. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The M.2 SSDs are managed by the MSTOR-RAID controller. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The embedded SATA RAID controller requires that the compute node is set to boot in UEFI mode rather than Legacy mode.

* * *  
  
---|---  


  * Removing an M.2 SATA or M.2 NVMe SSD
  * Installing an M.2 SATA or M.2 NVMe SSD


#### Removing an M.2 SATA or M.2 NVMe SSD

Each M.2 card plugs into a slot on the carrier, which mounts vertically to the motherboard.

  * One slot is on the front of the carrier, which faces inwards towards the rest of the compute node.

  * One slot is on the back of the carrier, which faces towards the compute node sheetmetal wall. 


Each M.2 SSD is secured to the carrier by the slot at one end, and a small retaining screw at the other end. The carrier is installed on the same component that has the compute node LEDs and buttons on the node's front panel. 

Use the following procedure for any type of mini-storage module carrier. 

##### Procedure

* * *

**Step 1** |  Remove the controller.  See Removing the M.2 RAID Controller Module or NVMe Pass-Through Module.   
---|---  
**Step 2** |  Using a #1 Phillips screwdriver, remove the screws that secure the M.2 SSD to the carrier.  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472284.jpg)  
**Step 3** |  Grasping the M.2 card by its edges, gently lift the end that held the screws at an angle, then slide the card out of its connector.  
  
* * *

##### What to do next

Installing an M.2 SATA or M.2 NVMe SSD

#### Installing an M.2 SATA or M.2 NVMe SSD

Each M.2 SATA or NVMe SSD plugs into a slot on the carrier and is held in place by a retaining screw for each SSD. 

Use the following procedure to install the M.2 SATA or NVMe SSD onto the carrier 

##### Procedure

* * *

**Step 1** |  Install the M.2 SATA or NVMe SSD. 

  1. Orient the SSD correctly.  |  **Note** |  When correctly oriented, the end of the SSD with two alignment holes lines up with the two alignment pins on the carrier.   
---|---  
  2. Angle the end opposite the screw into the connector 

  3. Press down on the end of the SSD that holds the screws until the SSD snaps into place. 

  4. Reinsert and tighten the retaining screw to secure the M.2 module to the carrier.

![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472283.jpg)


  
**Step 2** |  When you are ready, reinstall the controller onto the motherboard.  Installing the M.2 RAID Controller Module or NVMe Pass-Through Controller Module.   
**Step 3** |  Reinstall the compute node cover  
**Step 4** |  Reapply power and return the compute node to service.   
  
* * *

## Replacing the SuperCap Module

The SuperCap module (UCSB-MRAID-SC) is a battery bank which connects to the front mezzanine storage module board and provides power to the RAID controller if facility power is interrupted. The front mezzanine with the SuperCap module installed is UCSX-X10C-RAIDF. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The SuperCap module is only needed when the MRAID Storage Controller module (UCSX-X10C-RAIDF) or (UCSX-RAID-M1L6) is installed.

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

To remove the SuperCap Module you must remove the front mezzanine module.

* * *  
  
---|---  
  
To replace the SuperCap module, use the following topics:

  * Removing the SuperCap Module

  * Installing the SuperCap Module


  * Removing the SuperCap Module
  * Installing the SuperCap Module


### Removing the SuperCap Module

The SuperCap module is part of the Front Mezzanine Module, so the Front Mezzanine Module must be removed from the compute node to provide access to the SuperCap module. 

The SuperCap module sits in a plastic tray on the underside of the front mezzanine module. The SuperCap module connects to the board through a ribbon cable with one connector to the module.  Figure 1. Location of the SuperCap Module  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309003.jpg)

To replace the SuperCap module, follow these steps:

#### Procedure

* * *

**Step 1** |  If you have not already removed the Front Mezzanine module, do so now.  See Removing the Front Mezzanine Module.   
---|---  
**Step 2** |  Before removing the SuperCap module, note its orientation in the tray as shown in the previous image.  When correctly oriented, the SuperCap connection faces downward so that it easily plugs into the socket on the board. You will need to install the new SuperCap module with the same orientation.   
**Step 3** |  Grasp the cable connector at the board and gently pull to disconnect the connector. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309004.jpg)  
**Step 4** |  Grasp the sides of the SuperCap module, but not the connector, and lift the SuperCap module out of the tray. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309005.jpg)You might feel some resistance because the tray is curved to secure the module.  
**Step 5** |  Disconnect the ribbon cable from the SuperCap module:

  1. On the SuperCap module, locate the lever that secures the ribbon cable to the battery pack.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309006.jpg)
  2. Gently pivot the securing lever downward to release the ribbon cable connection from the SuperCap module. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309007.jpg)

  
**Step 6** |  Remove the existing battery pack from its case, and insert a new one, making sure to align the new battery pack so that the connector aligns with the ribbon cable.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309008.jpg)  
  
* * *

#### What to do next

Installing the SuperCap Module

### Installing the SuperCap Module

If you removed the SuperCap module, use this procedure to reinstall and reconnect it. 

#### Procedure

* * *

**Step 1** |  Insert the Super Cap module into its case.

  1. Align the SuperCap module so that the connector will meet the connector. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309009.jpg)
  2. Before seating the SuperCap module, make sure that the ribbon cable is not in the way. You do not want to pinch the ribbon cable when you install the SuperCap. 
  3. When the ribbon cables are clear of the case, press the SuperCap module until it is seated in the case. You might feel some resistance as the SuperCap snaps into place. 

  
---|---  
**Step 2** |  When the SuperCap module is completely seated in its plastic case, pivot the securing lever to connect the ribbon cable to the SuperCap module.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309010.jpg)  
**Step 3** |  Align the SuperCap module with its slot on the module and seat the module into the slot.  |  **Caution** |  Make sure not to pinch the ribbon cable while inserting the SuperCap module into the slot.   
---|---  
![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309011.jpg)

When the SuperCap is securely seated in the slot, the module does not rock or twist.   
  
**Step 4** |  After the SuperCap module is seated, reconnect the ribbon cable to the board.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309012.jpg)  
  
* * *

## Replacing CPUs and Heatsinks

This topic describes the configuration rules and procedure for replacing CPUs and heatsinks.

  * CPU Configuration Rules
  * Tools Required for CPU Replacement
  * CPU and Heatsink Alignment Features
  * Removing the CPU and Heatsink
  * Installing the CPU and Heatsink


### CPU Configuration Rules

This server has two CPU sockets on the motherboard. Each CPU supports 8 DIMM channels (16 DIMM slots). See Memory Population Guidelines. 

  * Fourth and Fifth Generation Intel Xeon Scalable Processors have the same physical dimensions, CPU alignment features, and use the same heatsinks, so field-replacement procedures are the same regardless of which generation of CPU is installed. 

  * The server can operate with either one or two CPUs installed. In a dual-CPU configuration, both CPUs must be identical.

  * The minimum configuration is at least CPU 1 installed. 

The following restrictions apply when using a dual-CPU configuration:

  * Any unused CPU socket must have the protective dust cover from the factory installed.

  * The maximum number of DIMMs is 32 (installed in slots A through H).

  * Mezzanine slots 1 and 2 are unavailable.


### Tools Required for CPU Replacement

You need the following tools and equipment for this procedure:

  * T-30 Torx driver—Supplied with replacement CPU. 

  * #1 flat-head screwdriver—Supplied with replacement CPU.

  * CPU assembly tool for M8 processors—Supplied with replacement CPU. The assembly tool can be ordered separately as Cisco PID UCS-CPUATI-6=. 

  * Heatsink cleaning kit—Supplied with replacement CPU. Can be ordered separately for the front or rear heatsink:

  * Front heatsink kit: UCSX-M8I-HS-F

  * Rear heatsink kit: UCSX-M8I-HS-R

One cleaning kit can clean up to four CPUs.

  * Thermal interface material (TIM)—Syringe supplied with replacement CPU. Use only if you are reusing your existing heatsink (new heatsinks have pre-applied TIM). Can be ordered separately as Cisco PID UCS-CPU-TIM=. 

One TIM kit covers one CPU.


### CPU and Heatsink Alignment Features

For installation and field-replacement procedures, the heatsink, the CPU carrier, and the CPU motherboard socket must all be properly aligned to the pin 1 location. 

Each of these parts has a visual indicator to ensure they are properly aligned. 

#### Heatsink Alignment Feature

Each heatsink has a yellow triangle labeled on one corner. The tip of the triangle points to the pin 1 location on the heatsink. Use the triangle to align the heatsink with the pin 1 location on other parts, such as the CPU carrier and CPU socket. 

![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472292.png)

Also note that the orientation of each CPU is different between CPU socket 1 and CPU socket 2, as indicated by the different position of the alignment feature on each heatsink. 

#### CPU Carrier Alignment Feature

Each CPU carrier has a triangular cutout in the carrier's plastic. The tip of the triangle points to the pin1 location on the carrier. Use the triangular cutout to align the CPU carrier with the pin 1 location on other parts, such as the heatsink and the CPU socket. The X210c M8 compute node supports two CPU carriers, E2A and E2B. Carrier E2A is shown in ther illustration in this guide. 

![](/c/dam/en/us/td/i/400001-500000/480001-490000/488001-489000/488777.jpg)

![](/c/dam/en/us/td/i/400001-500000/480001-490000/488001-489000/488776.jpg)

#### CPU Socket Alignment Feature

Each CPU socket has a triangle on the rectangular bolster plate around the CPU socket. The tip of the triangle points to the pin 1 location on the motherboard socket. Use the triangular cutout to align the CPU carrier with the pin 1 location on other parts, such as the heatsink and the CPU carrier. 

![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472294.jpg)

### Removing the CPU and Heatsink

Use the following procedure to remove an installed CPU and heatsink from the blade server. With this procedure, you will remove the CPU from the motherboard, disassemble individual components, then place the CPU and heatsink into the fixture that came with the CPU. 

Sixth Generation Intel Xeon Scalable Processors have the same dimensions, CPU alignment features, and use the same heatsinks. Replacement procedures are the same regardless of which processor generation is installed, and the same heatsink(s) can be reused wherever possible. 

#### Procedure

* * *

**Step 1** |  Detach the CPU and heatsink (the CPU assembly) from the CPU socket.

  1. Using the T30 Torx driver, loosen all the securing nuts in a diagonal pattern, you can start at any nut.  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472432.jpg)
  2. Using your fingers, push the rotating wires towards each other to move them to the unlocked position. |  **Caution** |  Make sure that the rotating wires are as far inward as possible. When fully unlocked, the bottom of the rotating wire disengages and allows the removal of the CPU assembly. If the rotating wires are not fully in the unlocked position, you can feel resistance when attempting to remove the CPU assembly.   
---|---  
  
![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472433.jpg)


  
**Step 2** |  Remove the CPU assembly from the motherboard.

  1. Grasp the heatsink along the edge of the carrier and lift the CPU assembly off of the motherboard.  |  **Caution** |  Do not grasp the heatsink by its fins. Only handle the carrier! Also, if you feel any resistance when lifting the CPU assembly, verify that the rotating wires are completely in the unlocked position.   
---|---  
  
![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472438.jpg)

  2. Put the CPU assembly on a rubberized mat or other ESD-safe work surface.

When placing the CPU on the work surface, the heatsink label should be facing up. Do not rotate the CPU assembly upside down.

  3. Ensure that the CPU assembly sits level on the work surface. 


  
**Step 3** |  Attach a CPU dust cover to the CPU socket.

  1. Align the posts on the CPU bolstering plate with the cutouts at the corners of the dust cover.
  2. Lower the dust cover and simultaneously press down on the edges until it snaps into place over the CPU socket. |  **Caution** |  Do not press down in the center of the dust cover!  
---|---  
  
![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472440.jpg)


  
**Step 4** |  Detach the heatsink from the CPU carrier by disengaging the CPU clips and using the TIM breaker.

  1. Turn the CPU assembly upside down, so that the heatsink is pointing down.  This step enables access to the CPU securing clips.
  2. Gently rotate up on the outer edge of the CPU carrier (1 in the following illustration) at the edge opposite the TIM breaker.  |  **Caution** |  Be careful when flexing the CPU carrier! If you apply too much force you can damage the CPU carrier. Flex the carrier only enough to release the CPU clips. Make sure to watch the clips while performing this step so that you can see when they disengage from the CPU carrier.   
---|---  
  3. Gently lift the TIM breaker (2 ) in a 90-degree upward arc to partially disengage the CPU clips on this end of the CPU carrier.

  4. Lower the TIM breaker into the u-shaped securing clip to allow easier access to the CPU carrier. 

**Note** |  Make sure that the TIM breaker is completely seated in the securing clip.  
---|---  
  5. Gently pull up on the outer edge of the CPU carrier nearest to the TIM breaker so that you can disengage the pair of CPU clips (3 in the following illustration). 

  6. Grasp the CPU carrier along the short edges and lift it straight up to remove it from the heatsink.

![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472728.jpg)


  
**Step 5** |  Transfer the CPU and carrier to the fixture.

  1. When all the CPU clips are disengaged, grasp the carrier and lift it and the CPU to detach them from the heatsink. |  **Caution** |  Handle the carrier only! Do not touch the CPU gold contacts. Do not separate the CPU from the carrier.  
---|---  
**Note** |  If the carrier and CPU do not lift off of the heatsink, attempt to disengage the CPU clips again.  
---|---  
  2. Use the provided cleaning kit (UCSX-HSCK) to remove all of the thermal interface barrier (thermal grease) from the CPU, CPU carrier, and heatsink. 

**Important** |  Make sure to use only the Cisco-provided cleaning kit, and make sure that no thermal grease is left on any surfaces, corners, or crevices. The CPU, CPU carrier, and heatsink must be completely clean.   
---|---  
  3. Flip the CPU and carrier right-side up so that the word PRESS is visible. 

  4. Align the posts on the fixture, and the pin 1 locations on the CPU carrier and the fixture. 

The pin 1 location on the CPU is indicated by the triangle, and the pin 1 location on the fixture is the angled corner. 

  5. Lower the CPU and carrier onto the fixture. 

![](/c/dam/en/us/td/i/400001-500000/480001-490000/488001-489000/488767.jpg)


  
  
* * *

#### What to do next

  * If you will not be installing a CPU, verify that a CPU socket cover is installed. This option is valid only for CPU socket 2 because CPU socket 1 must always be populated in a runtime deployment. 


### Installing the CPU and Heatsink

Use this procedure to install a CPU if you have removed one, or if you are installing a CPU in an empty CPU socket. 

If you are installing or adding a new CPU to a single-CPU compute node, make sure that the new CPU is identical to the existing CPU. If you are replacing a CPU, reuse the existing heatsink. 

#### Before you begin

The CPU socket, CPU carrier, and heatsink must be correctly aligned to be installed. For information about the alignment features of these parts, see CPU and Heatsink Alignment Features. 

#### Procedure

* * *

**Step 1** |  Remove the CPU socket dust cover on the server motherboard. 

  1. Push the two vertical tabs inward to disengage the dust cover.
  2. While holding the tabs in, lift the dust cover up to remove it.  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472441.jpg)
  3. Store the dust cover for future use.  |  **Caution** |  Do not leave an empty CPU socket uncovered. If a CPU socket does not contain a CPU, you must install a CPU dust cover.  
---|---  

  
**Step 2** |  Grasp the CPU carrier on the edges, lift it out of the tray, and place the CPU carrier on an ESD-safe work surface.![](/c/dam/en/us/td/i/400001-500000/480001-490000/488001-489000/488766.jpg)  
**Step 3** |  Apply new TIM. |  **Note** |  The heatsink must have new TIM on the heatsink-to-CPU surface to ensure proper cooling and performance.   
---|---  
  
  * If you are installing a new heatsink, it is shipped with a pre-applied pad of TIM. Go to step 4.

  * If you are reusing a heatsink, you must remove the old TIM from the heatsink and then apply new TIM to the CPU surface from the supplied syringe. Continue with step **a** below. 


  1. Apply the Bottle #1 cleaning solution that is included with the heatsink cleaning kit (UCSX-HSCK=), as well as the spare CPU package, to the old TIM on the heatsink and let it soak for a least 15 seconds. 

  2. Wipe all of the TIM off the heatsink using the soft cloth that is included with the heatsink cleaning kit. Be careful to avoid scratching the heatsink surface. 

  3. Completely clean the bottom surface of the heatsink using Bottle #2 to prepare the heatsink for installation.

  4. Using the syringe of TIM provided with the new CPU, apply 1.5 cubic centimeters (1.5 ml) of thermal interface material to the top of the CPU. Use the pattern shown in the following figure to ensure even coverage. 

Figure 2. Thermal Interface Material Application Pattern  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/306001-307000/306154.jpg) **Caution** |  Use only the correct heatsink for your CPU. CPU 1 uses heatsink UCSX-M8I-HS-F and CPU 2 uses heatsink UCSX-M8I-HS-R.  
---|---  

  
**Step 4** |  Attach the heatsink to the CPU and carrier. 

  1. Using your finger, push the retaining wires to the unlocked position to prevent obstruction when seating the CPU.
  2. Grasp the heatsink by the short edges.
  3. Align the pin 1 location of the heatsink with the pin 1 location on the CPU carrier, then lower the heatsink onto the CPU carrier.  The heatsink is correctly oriented when the embossed triangle points to the CPU pin 1 location. 

  
**Step 5** |  Install the CPU assembly onto the CPU motherboard socket. 

  1. Push the rotating wires inward to the unlocked position so that they do not obstruct installation. 
  2. Grasp the heatsink by the carrier, align the pin 1 location on the heatsink with the pin 1 location on the CPU socket, then seat the heatsink onto the CPU socket.  The heatsink is correctly oriented when the embossed triangle points to the CPU pin 1 location, as shown.  |  **Caution** |  Make sure the rotating wires are in the unlocked position so that the feet of the wires do not impede installing the heatsink.  
---|---  
  
![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472439.png)


  
**Step 6** |  Secure the CPU and heatsink to the socket.

  1. Push the rotating wires away from each other to lock the CPU assembly into the CPU socket. |  **Caution** |  Make sure that you close the rotating wires completely before using the Torx driver to tighten the securing nuts.   
---|---  
  2. Set the T30 Torx driver to 12 in-lb of torque and tighten the 4 securing nuts to secure the CPU to the motherboard. You can start with any nut, but make sure to tighten the securing nuts in a diagonal pattern. 

![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472437.png)


  
  
* * *

## Replacing Memory DIMMs

The DIMMs that this compute node supports are updated frequently. A list of supported and available DIMMs is in _Cisco UCS X210c M8 Specification Sheet_ or the _Cisco UCS Intel M8 Memory Guide_. 

Do not use any DIMMs other than those listed in the specification sheet. Doing so may irreparably damage the compute node and result in down time. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The maximum memory configuration for the compute node is 32 256 GB DDR5 DIMMs.

  * When the compute node is configured with 256 GB DDR5 DIMMs, the compute node's supported operating temperature is 50° F to 89.6° F (10° C to 32 ° C).  When this operating range is exceeded, the compute node can throttle down in an attempt to cool the compute node. If throttling does not sufficiently cool the compute node, the node shuts down. 
  * When the compute node is configured without 256 GB DDR5 DIMMs, the compute node's supported operating temperature is 50° F to 95° F (10° C to 35 ° C). 


* * *  
  
---|---  
  
  * Memory Population Guidelines
  * Installing a DIMM or DIMM Blank


### Memory Population Guidelines

For detailed information about supported memory, memory population guidelines, and configuration and performance, download the PDF of the [Cisco UCS/UCSX M8 Memory Guide](https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/ucs-intel-m8-memory-guide.pdf). 

#### DIMM Identification

To assist with identification, each DIMM slot displays its memory processor and slot ID on the motherboard. The entire enumeration string consists of <Processor-ID>_ <channel> <DIMM slot-ID>. 

For example, P1 A1 indicates CPU 1, DIMM channel A, Slot 1. 

Also, you can further identify which DIMM slot connects to which CPU by dividing the blade in half vertically. With the compute node front panel facing left: 

  * All DIMM slots on the left, above and below CPU 1 are connected to CPU 1

  * All DIMM slots on the right, above and below CPU 2 are connected to CPU 2. 


For each CPU, each set of 16 DIMMs is arranged into 8 channels, where each channel has two DIMMs. Each DIMM slot is numbered 1 or 2, and each DIMM slot 1 is blue and each DIMM slot 2 is black. Each channel is identified by two pairs of letters and numbers where the first pair indicates the processor, and the second pair indicates the memory channel and slot in the channel. 

  * Each DIMM is assigned to a CPU, either CPU 1 (P1) or CPU 2 (P2). 

  * Each CPU has memory channels A through H. 

  * Each memory channel has two slots 1 and 2. 

  * DIMM slot identifiers for CPU1 are P1 A1, P1 A2, P1 B1, P1 B2, P1 C1, P1 C2, P1 D1, P1 D2, P1 E1, P1 E2, P1 F1, P1 F2, P1 G1, P1 G2, P1 H1, and P1 H2. 

  * DIMM slot identifiers for CPU 2 are P2 A1, P2 A2, P2 B1, P2 B2, P2 C1, P2 C2, P2 D1, P2 D2, P2 E1, P2 E2, P2 F1, P2 F2, P2 G1, P2 G2, P2 H1, and P2 H2. 


The following illustration shows the memory slot and channel IDs. 

  
![](/c/dam/en/us/td/i/400001-500000/480001-490000/488001-489000/488768.jpg)  


#### Memory Population Order

Memory slots are color coded, blue and black. The color-coded channel population order is blue slots first, then black.

For optimal performance, populate DIMMs in the order shown in the following table, depending on the number of CPUs and the number of DIMMs per CPU. If your server has two CPUs, balance DIMMs evenly across the two CPUs as shown in the table. 

Be aware of the following DIMM population rules:

  * There should be at least one DDR5 DIMM per socket. 

If only one DIMM is populated in a channel, then populate it in the slot furthest away from CPU of that channel

Always populate DIMMs with a higher electrical loading in DIMM0 followed by DIMM1. 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The table below lists recommended configurations. Using 3, 5, 7, 9, 10, 11, or 13-15 DIMMs per CPU is not recommended. Other configurations results in reduced performance. 

* * *  
  
---|---  
  
The following table shows the memory population order for DDR5 DIMMs.

Table 1. DIMMs Population Order **Number of DDR5 DIMMs per CPU (Recommended Configurations)** |  **Populate CPU 1 Slot** |  **Populate CPU2 Slots**  
---|---|---  
**P1 Blue #1 Slots** **P1 slot-ID** |  **P1 Black #2 Slots** ****P1_slot-ID**** |  **P2 Blue #1 Slots** ****P2 slot-ID**** |  **P2 Black #2 Slots** ******P2 slot-ID******  
1 |  A1 |  - |  A1 |  -  
4 | A1, C1, E1, G1 |  - | A1, C1, E1, G1 |  -  
8 |  A1, B1, C1, D1, E1, F1, G1, H1 |  - |  A1, B1, C1, D1, E1, F1, G1, H1 | -  
12 |  A1, B1, C1, D1, E1, F1,G1, H1 |  A2, C2, E2, G2 |  A1, B1, C1, D1, E1, F1,G1, H1 |  A2, C2, E2, G2  
16 |  All populated (A1 through H1) |  All populated (A2 through H2) |  All populated (A1 through H1) |  All populated (A2 through H2)  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For configurations with 1, 2, 4, 6 and 8 DIMMs, install higher capacity followed by lower capacity DIMMs in alternating fashion. For example, the 4 DIMMs configuration is installed with 64GB on A1, E1 on both CPUs and 16GB on C1, G1 on both CPUs.  For configurations with 12 and 16 DIMMs, install all higher capacity DIMMs in blue slots and all lower capacity DIMMs in black slots. 

* * *  
  
---|---  
  
#### DIMM Slot Keying Consideration

DIMM slots that connect to each CPU socket are oriented 180 degrees from each other. So, when you compare the DIMM slots for CPU 1 and the DIMM slots for CPU 2, the DIMMs do not install the same way. Instead, when you install DIMM attached to both CPUs, the DIMM orientation must change 180 degrees. 

To facilitate installation, DIMMs are keyed to ensure correct installation. When you install a DIMM, always make sure that the key in the DIMM slot lines up with the notch in the DIMM. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

If you feel resistance while seating a DIMM into its socket, do not force the DIMM or you risk damaging the DIMM or the slot. Check the keying on the slot and verify it against the keying on the bottom of the DIMM. When the slot's key and the DIMM's notch are aligned, reinstall the DIMM. 

* * *  
  
---|---  
  
### Installing a DIMM or DIMM Blank

To install a DIMM or a DIMM blank (UCS-DDR5-BLK=) into a slot on the compute node, follow these steps:

#### Procedure

* * *

**Step 1** |  Open both DIMM connector latches.  
---|---  
**Step 2** |  Press evenly on both ends of the DIMM until it clicks into place in its slot. |  **Note** |  Ensure that the notch in the DIMM aligns with the slot. If the notch is misaligned, it is possible to damage the DIMM, the slot, or both.   
---|---  
**Step 3** |  Press the DIMM connector latches inward slightly to seat them fully.  
**Step 4** |  Populate all slots with a DIMM or DIMM blank. A slot cannot be empty. Figure 3. Installing Memory ![](/c/dam/en/us/td/i/300001-400000/300001-310000/306001-307000/306040.jpg)  
  
* * *

## Servicing the mLOM

The Cisco UCS X210c M8 Compute Node supports a modular LOM (mLOM) card to provide additional rear-panel connectivity. The mLOM socket is on the rear corner of the motherboard. 

The mLOM socket provides a Gen-4 x16 PCIe lane. The socket remains powered when the compute node is in 12 V standby power mode, and it supports the network communications services interface (NCSI) protocol. 

The following mLOM cards are supported on the compute node.

Table 2. Supported mLOM VICs on Cisco UCS X210c M8 UCSX-ML-V5Q50G-D |  Cisco UCS Virtual Interface Card (VIC) 15420, Quad-Port 25G  
---|---  
UCSX-MLV5D200GV2D |  Cisco UCS Vitual Interface Card (VIC) 15230, Dual-Port 40/100/200G mLOM  
  
To service the mLOM card, use the following procedures:

  * Removing the mLOM

  * Installing an mLOM Card


  * Removing the mLOM
  * Installing an mLOM Card


### Removing the mLOM

The compute node supports an mLOM in the rear mezzanine slot. Use this procedure to remove an mLOM.

#### Procedure

* * *

**Step 1** |  Remove the compute node.

  1. Shut down and remove power from the compute node.
  2. Remove the compute node from the chassis. You might have to detach cables from the rear panel to provide clearance. 
  3. Remove the top cover from the compute node. See Removing a Compute Node Cover. 

  
---|---  
**Step 2** |  If the compute node has a UCS VIC 15000 Series Bridge Card, remove the card.  See Removing the Bridge Card.   
**Step 3** |  Remove the MLOM.

  1. Using a #2 Phillips head screwdriver, loosen the two captive thumbscrews.
  2. Lift the MLOM off of its socket.  You might need to gently rock the mLOM card while lifting it to disengage it from the socket. ![](/c/dam/en/us/td/i/400001-500000/480001-490000/488001-489000/488764.jpg)

  
  
* * *

#### What to do next

After completing service, reinstall the VIC. See Installing a Rear Mezzanine Card in Addition to the mLOM VIC. 

### Installing an mLOM Card

Use this task to install an mLOM onto the compute node.

#### Before you begin

If the compute node is not already removed from the chassis, power it down and remove it now. You might need to disconnect cables to remove the compute node. 

Gather a torque screwdriver. 

#### Procedure

* * *

**Step 1** |  Remove the top cover. See Removing a Compute Node Cover.   
---|---  
**Step 2** |  Orient the mLOM card so that the socket is facing down.   
**Step 3** |  Align the mLOM card with the motherboard socket so that the bridge connector is facing inward. ![](/c/dam/en/us/td/i/400001-500000/480001-490000/488001-489000/488770.jpg)  
**Step 4** |  Keeping the card level, lower it and press firmly to seat the card into the socket.  
**Step 5** |  Using a #2 Phillips torque screwdriver, tighten the captive thumbscrews to 4 in-lb of torque to secure the card.  
**Step 6** |  If your compute node has a bridge card (Cisco UCS VIC 15000 Series Bridge), reattach the bridge card.  See Installing a Bridge Card.   
**Step 7** |  Replace the top cover of the compute node.  
**Step 8** |  Reinsert the compute node into the chassis. replace cables, and then power on the compute node by pressing the Power button.  
  
* * *

## Servicing the VIC

The Cisco UCS X210c M8 Compute Node supports a virtual interface card (VIC) in the rear mezzanine slot. The VIC can be either half-slot or full-slot in size. 

The following VICs are supported on the compute node.

Table 3. Supported VICs UCSX-ME-V5Q50G-D |  Cisco UCS Virtual Interface Card (VIC) 15422, Quad-Port 25G  
---|---  
UCSX-ML-V5D200GV2 |  Cisco UCS Virtual Interface Card (VIC) 15420, Quad-Port 25G  
UCSX-MLV5D200GV2D |  Cisco UCS Virtual Interface Card (VIC) 15230, Dual-Port 100G  
UCSX-V4-PCIME-D |  UCS PCI Mezz card for X-Fabric Connectivity  
  
  * Cisco Virtual Interface Card (VIC) Considerations
  * Removing a Rear Mezzanine
  * Installing a Rear Mezzanine Card in Addition to the mLOM VIC


### Cisco Virtual Interface Card (VIC) Considerations

This section describes VIC card support and special considerations for this compute node.

  * A blade with only one mezzanine card is an unsupported configuration. With this configuration, blade discovery does not occur through Cisco UCS management software. No error is displayed. 


### Removing a Rear Mezzanine

The compute node supports a Rear Mezzanine Card in the rear of the compute node. Use this procedure to remove the Rear Mezzanine Card. 

#### Procedure

* * *

**Step 1** |  Remove the compute node.

  1. Decommission the compute node by using Cisco UCS management software. 
  2. Remove the compute node from the chassis. You might have to detach cables from the rear panel to provide clearance. 
  3. Remove the top cover from the compute node. See Removing a Compute Node Cover. 

  
---|---  
**Step 2** |  If the compute node has a UCS VIC 15000 Series Bridge Card, remove the card.  See Removing the Bridge Card.   
**Step 3** |  Remove the Rear Mezzanine.

  1. Using a #2 Phillips head screwdriver, loosen the captive thumbscrews.
  2. Lift the VIC off of its socket.  You might need to gently rock the Rear Mezzanine card while lifting it to disengage it from the socket. ![](/c/dam/en/us/td/i/400001-500000/470001-480000/476001-477000/476302.jpg)

  
  
* * *

### Installing a Rear Mezzanine Card in Addition to the mLOM VIC

The compute node has a rear mezzanine slot which can accept a virtual interface card (VIC) unless the compute node has a full size mLOM. In the case of a separate mLOM and VIC, another component (the UCS VIC 15000 Series Bridge is required to provide data connectivity between the mLOM and VIC. See Installing a Bridge Card. 

Use this task to install a VIC in the rear mezzanine slot. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The VIC installs upside down so that the connectors meet with the sockets on the compute node. 

* * *  
  
---|---  
  
#### Before you begin

Gather a torque screwdriver.

#### Procedure

* * *

**Step 1** |  Orient the VIC with the captive screws facing up and the connectors facing down.   
---|---  
**Step 2** |  Align the VIC so that the captive screws line up with their threaded standoffs, and the connector for the bridge card is facing inward.   
**Step 3** |  Holding the VIC level, lower it and press firmly to seat the connectors into the sockets.  ![](/c/dam/en/us/td/i/400001-500000/480001-490000/488001-489000/488769.jpg)  
**Step 4** |  Using a #2 Phillips torque screwdriver, tighten the captive screws to 4 in-lb of torque to secure the VIC to the compute node.  
  
* * *

#### What to do next

  * If the mLOM card is already installed, install a bridge card. Go to Installing a Bridge Card. 

  * If not, install the mLOM, which must be installed before the bridge card can be attached. Go to Installing an mLOM Card. 


## Servicing the Bridge Card

The compute node supports a Cisco UCS Series 15000 Bridge Card (UCSX-V5-BRIDGE-D) that spans between the rear mezzanine MLOM slot and the VIC slot. The bridge card connects the UCS X-Series Blade Server to the following Intelligent Fabric Modules (IFMs) in the server chassis that contains the compute nodes: 

  * Cisco UCS X9108 25G Intelligent Fabric Module (UCSX-I-9108-25G) 

  * Cisco UCS X9108 100G Intelligent Fabric Module (UCSX-I-9108-100G)


See the following topics:

  * Removing the Bridge Card

  * Installing a Bridge Card


  * Removing the Bridge Card
  * Installing a Bridge Card


### Removing the Bridge Card

Use the following procedure to remove the bridge card. 

#### Procedure

* * *

**Step 1** |  Remove the compute node.

  1. Shut down and remove power from the compute node.
  2. Remove the compute node from the chassis. You might have to detach cables from the rear panel to provide clearance. 
  3. Remove the top cover from the compute node. See Removing a Compute Node Cover. 

  
---|---  
**Step 2** |  Remove the bridge card from the motherboard. 

  1. Using a #2 Phillips screwdriver, loosen the two captive screws.
  2. Lift the bridge card off of the socket.  |  **Note** |  You might need to gently rock the bridge card to disconnect it.  
---|---  
  
![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472416.jpg)


  
  
* * *

#### What to do next

Choose the appropriate option:

  * Perform service on the MLOM. See Servicing the mLOM. 

  * Perform service on the VIC. See Servicing the VIC. 

  * Reinstall the bridge card. See .


### Installing a Bridge Card

The Cisco UCS VIC 14000 Series Bridge is a physical card that provides data connection between the mLOM and VIC. Use this procedure to install the bridge card. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The bridge card installs upside down so that the connectors meet with the sockets on the MLOM and VIC. 

* * *  
  
---|---  
  
#### Before you begin

To install the bridge card, the compute node must have an mLOM and a VIC installed. The bridge card ties these two cards together to enable communication between them. 

If these components are not already installed, install them now. See:

  * Installing a Rear Mezzanine Card in Addition to the mLOM VIC


#### Procedure

* * *

**Step 1** |  Orient the bridge card so that the Press Here to Install  text is facing you.   
---|---  
**Step 2** |  Align the bridge card so that the connectors line up with the sockets on the MLOM and VIC.  When the bridge card is correctly oriented, the hole in the part's sheet metal lines up with the alignment pin on the VIC.  
**Step 3** |  Keeping the bridge card level lower it onto the MLOM and VIC cards and press evenly on the part where the Press Here to Install  text is.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308991.jpg)  
**Step 4** |  When the bridge card is correctly seated, use a #2 Phillips screwdriver to secure the captive screws. |  **Caution** |  Make sure the captive screws are snug, but do not overdrive them or you risk stripping the screw.   
---|---  
  
* * *

## Servicing the Trusted Platform Module (TPM)

The Trusted Platform Module (TPM) is a component that can securely store artifacts used to authenticate the compute node. These artifacts can include passwords, certificates, or encryption keys. A TPM can also be used to store platform measurements that help ensure that the platform remains trustworthy. Authentication (ensuring that the platform can prove that it is what it claims to be) and attestation (a process helping to prove that a platform is trustworthy and has not been breached) are necessary steps to ensure safer computing in all environments. It is a requirement for the Intel Trusted Execution Technology (TXT) security feature, which must be enabled in the BIOS settings for a compute node equipped with a TPM. 

The Cisco UCS X210c M8 Compute Node supports the Trusted Platform Module 2.0, which is FIPS140-2 compliant and CC EAL4+ certified (UCSX-TPM-002D= (or UCSX-TPM-002D-D). 

To install and enable the TPM, go to SEnabling the Trusted Platform Module. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Removing the TPM is supported only for recycling and e-waste purposes. Removing the TPM will destroy the part so that it cannot be reinstalled. 

* * *  
  
---|---  
  
  * Enabling the Trusted Platform Module


### Enabling the Trusted Platform Module

The Trusted Platform Module (TPM) is a component that can securely store artifacts used to authenticate the server. These artifacts can include passwords, certificates, or encryption keys. A TPM can also be used to store platform measurements that help ensure that the platform remains trustworthy. Authentication (ensuring that the platform can prove that it is what it claims to be) and attestation (a process helping to prove that a platform is trustworthy and has not been breached) are necessary steps to ensure safer computing in all environments. It is a requirement for the Intel Trusted Execution Technology (TXT) security feature, which must be enabled in the BIOS settings for a server equipped with a TPM. 

#### Procedure

* * *

**Step 1** |  Install the TPM hardware. 

  1. Decommission, power off, and remove the blade server from the chassis. 
  2. Remove the top cover from the server as described in Removing a Compute Node Cover
  3. Install the TPM to the TPM socket on the server motherboard and secure it using the one-way screw that is provided. See the figure below for the location of the TPM socket. 
  4. Return the blade server to the chassis and allow it to be automatically reacknowledged, reassociated, and recommissioned. 
  5. Continue with enabling TPM support in the server BIOS in the next step. 

![](/c/dam/en/us/td/i/400001-500000/480001-490000/488001-489000/488778.jpg)  
---|---  
**Step 2** |  Enable TPM Support in the BIOS. 

  1. In the Cisco UCS Manager Navigation pane, click the Servers tab. 
  2. On the Servers tab, expand Servers > Policies. 
  3. Expand the node for the organization where you want to configure the TPM. 
  4. Expand BIOS Policies and select the BIOS policy for which you want to configure the TPM. 
  5. In the Work pane, click the Advanced tab. 
  6. Click the Trusted Platform sub-tab. 
  7. To enable TPM support, click Enable or Platform Default. 
  8. Click Save Changes. 
  9. Continue with the next step. 

  
  
* * *

---

## Page 6: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x210c-m8/install/b-x210c-m8-install/m-recycling-components.html

# Recycling Compute Node Components

This chapter contains the following topics:

## Compute Node Recycling Overview

This chapter documents the procedures to disassemble key compute node components for recycling and e-waste. When recycling your Cisco UCS hardware, always make sure to follow local e-waste and recycling regulations. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

**For Recyclers Only!** The procedures in this chapter are not standard field-service options. These procedures are for recyclers who will be reclaiming the electronics for proper disposal to comply with local eco design and e-waste regulations. 

* * *  
  
---|---  
  
To disassemble compute node component parts, see the following topics: 

  * Removing the Trusted Platform Module (TPM)

  * Recycling the Motherboard PCBA


## Removing the Trusted Platform Module (TPM)

The TPM module is attached to the printed circuit board assembly (PCBA). You must disconnect the TPM module from the PCBA before recycling the PCBA. The TPM module is secured to a threaded standoff by a tamper-resistant screw. If you do not have the correct tool for the screw, you can use a pair of pliers to remove the screw. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Removing the TPM destroys the part so that it cannot be reinstalled or reused!

* * *  
  
---|---  
  
### Before you begin

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

**For Recyclers Only!** This procedure is not a standard field-service option. This procedure is for recyclers who will be reclaiming the electronics for proper disposal to comply with local eco design and e-waste regulations. 

* * *  
  
---|---  
  
To remove the Trusted Platform Module (TPM), the following requirements must be met for the compute node:

  * It must be disconnected from facility power. 

  * It must be removed from the equipment rack. 

  * The top cover must be removed. If the top cover is not removed, see [Removing a Compute Node Cover](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_cbf2ee70-df1d-4095-b066-db7268a991b7). 


### Procedure

* * *

**Step 1** |  Locate the TPM module. ![](/c/dam/en/us/td/i/400001-500000/480001-490000/488001-489000/488771.jpg)  
---|---  
**Step 2** |  Using the pliers, grip the head of the screw and turn it counterclockwise until the screw releases.  
**Step 3** |  Remove the TPM module and dispose of it properly.  
  
* * *

### What to do next

Remove and dispose of the PCB Assembly. See Recycling the Motherboard PCBA. 

## Recycling the Component PCB Assemblies (PCBAs)

In addition to the main motherboard PCBA, some key components also contain PCBAs that need to be recycled. Always comply with your local regulations governing recycling and e-waste. 

Use the following procedures to recycle the appropriate components.

  * Recycling the Motherboard PCBA

  * Recycling the Front Mezzanine Module PCBA


  * Recycling the Motherboard PCBA
  * Recycling the Front Mezzanine Module PCBA
  * Recycling the Front Mezzanine GPU Module's PCBA


### Recycling the Motherboard PCBA

Each compute node has a PCBA that is connected to the compute node's faceplate and sheet metal tray. You must disconnect the PCBA from the faceplate and tray to recycle the PCBA. Each compute node is attached to the sheet metal tray be the following: 

  * Four M3 screws

  * Two hexagonal standoffs.


For this procedure you will need the following tools: 

  * Screwdrivers: #2 Phillips, one 6mm slotted, one T8, T10, and T30. 

  * Nut driver: One 6mm hex 


You will need to recycle the PCBA for each compute node.

#### Before you begin

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

**For Recyclers Only!** This procedure is not a standard field-service option. This procedure is for recyclers who will be reclaiming the electronics for proper disposal to comply with local eco design and e-waste regulations. 

* * *  
  
---|---  
  
To remove the printed circuit board assembly (PCBA), the following requirements must be met:

  * The compute node must be disconnected from facility power.

  * The compute node must be removed from the equipment rack.

  * The compute node's top cover must be removed. See [Removing a Compute Node Cover](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_cbf2ee70-df1d-4095-b066-db7268a991b7). 


#### Procedure

* * *

**Step 1** |  (Optional) If the CPUs and heat sinks are still installed, remove them. See [Removing the CPU and Heatsink](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_38f14d54-eda9-4b1d-b72c-39b2ef89c1f1).   
---|---  
**Step 2** |  (Optional) If the front mezzanine module is installed, remove it. See [Removing the Front Mezzanine Module](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_ae651cb7-9fa9-4e8c-a698-45ea0eee9ee9).   
**Step 3** |  (Optional) If the rear bridge card is installed, remove it.  See [Removing the Bridge Card](m-servicing-the-compute-node.html#removing-the-bridge-card).   
**Step 4** |  (Optional) If the rear mezzanine card is installed, use a #2 screwdriver to remove the four captive screws, then remove the card.  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472295.png)  
**Step 5** |  (Optional) If the MLOM VIC is installed, remove it. See [Removing the mLOM](m-servicing-the-compute-node.html#removing-the-mlom).   
**Step 6** |  Remove the M.2 module.  See [Removing the M.2 RAID Controller Module or NVMe Pass-Through Module](m-servicing-the-compute-node.html#removing-the-m.2-raid-controller-module).   
**Step 7** |  Remove the compute node's rear frame.

  1. Use the T8 screwdriver to remove the M3 bottom mounting screw on each exterior side of the compute node.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309229.jpg)
  2. Turn the compute node upside down and use the T10 screwdriver to remove the two M3 mounting screws on the bottom of the sheet metal.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309230.jpg)
  3. Turn the compute node component side up and use the T10 screwdriver to remove the six M3 mounting screws at the rear of the compute node.  ![](/c/dam/en/us/td/i/400001-500000/480001-490000/488001-489000/488772.jpg)

  
**Step 8** |  If the TPM is installed, remove it.  See Removing the Trusted Platform Module (TPM).   
**Step 9** |  Disconnect the motherboard from the compute node's sheet metal. 

  1. Use the 6mm hex nut driver to remove the two standoffs. 
  2. Use the #2 Phillips screwdriver to remove the front mezzanine cage retaining screw, then remove the cage. 
  3. Use the T10 screwdriver to remove the four M3 screws.  ![](/c/dam/en/us/td/i/400001-500000/480001-490000/488001-489000/488775.jpg) |  Red circles (![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309210.jpg))  |  6 mm standoffs (2)  
---|---  
Blue circles (![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309209.jpg))  |  M3 screws (4)  
Purple circle (![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309212.jpg))  |  Front mezzanine cage retaining screw (1)  

  
**Step 10** |  Recycle the sheet metal and motherboard in compliance with your local recycling and e-waste regulations.   
  
* * *

### Recycling the Front Mezzanine Module PCBA

The compute node's front mezzanine module contains one PCBA, which sits horizontally and connects the drive backplane to the main motherboard. The PCBA is attached to the front mezzanine module's sheetmetal by four T8 screws. 

You must disconnect the PCBA from the sheetmetal before recycling the PCBA. 

#### Before you begin

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

**For Recyclers Only!** This procedure is not a standard field-service option. This procedure is for recyclers who will be reclaiming the electronics for proper disposal to comply with local eco design and e-waste regulations. 

* * *  
  
---|---  
  
To remove the printed circuit board assembly (PCBA), the following requirements must be met:

  * The compute node must be removed from the chassis.

  * The compute node's top cover must be removed.


Gather the following tools: 

  * A T8 Torx screwdriver

  * A #2 Phillips screwdriver


#### Procedure

* * *

**Step 1** |  Remove the front mezzanine module from the compute node.

  1. Place the front mezzanine module upside down on a rubberized mat or other ESD-safe work surface. 

  
---|---  
**Step 2** |  Disconnect the drive backplane.

  1. Using a #2 Phillips screwdriver, remove the two screws on the drive backplane. ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472720.jpg)
  2. Grasp the drive backplane and lift it off of the sheetmetal frame. ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472721.jpg)

  
**Step 3** |  Disconnect the PCBA from the sheetmetal frame.

  1. Locate the PCBA and use a T8 Torx screwdriver to remove the four screws that secure the PCBA to the sheetmetal frame.  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472723.jpg)
  2. Grasp the PCBA and detach it from the front mezzanine module. ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472724.jpg)

  
**Step 4** |  Dispose of the PCBA properly in accordance with your local recycling and e-waste laws.  
  
* * *

### Recycling the Front Mezzanine GPU Module's PCBA

The compute node supports an optional front mezzanine module configuration of one or two Cisco L4-MEZZ GPUs. The X10c Front Mezzanine GPU Module, UCSX-X10C-GPUFM, has a PCBA that must be recycled. 

For information about recycling the PCBA in the X10c Front Mezzanine GPU Module, go to [Recycling the Front Mezzanine GPU Module PCBA](https://www-author3.cisco.com/content/en/us/td/docs/unified_computing/ucs/x/hw/x10c-gpu-module/install/cisco-ucs-x10c-front-mezzanine-gpu-install-guide/m-servicing-gpu-module.html#Cisco_Task_in_List_GUI.dita_69d5ccb6-d922-428e-90b2-62019008eff7). 

---

## Page 7: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x210c-m8/install/b-x210c-m8-install/m-specifications.html

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

## Page 8: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x210c-m8/install/b-x210c-m8-install/b-x210c-m8-install_index.html

> ## Contents  
>   
> B \- C \- D \- F \- H \- I \- L \- M \- N \- R \- S \- T \- V
> 
> ## Index
> 
> B
> 
> bridge card, installing [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_5ef0f92f-3491-4e58-b811-aafac6faf585)
> 
> bridge card, removing [1](m-servicing-the-compute-node.html#removing-the-bridge-card)
> 
> C
> 
> compute node blank, installing [1](m-installing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_25761031-a2b9-4377-ab11-95b70fdade99)
> 
> compute node blank, removing [1](m-installing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_c3949737-3f5e-491c-bd83-2c3732c3a107)
> 
> compute node cover, installing [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_0d8487b0-299e-4d9d-8693-a657818cda90)
> 
> compute node cover, removing [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_cbf2ee70-df1d-4095-b066-db7268a991b7)
> 
> compute node, installing [1](m-installing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_f863fd96-b47b-429f-84dd-096085fa347a)
> 
> compute node, removing [1](m-installing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_3efa87f6-969a-4184-b80f-1b05e284a66a)
> 
> CPU, removing [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_38f14d54-eda9-4b1d-b72c-39b2ef89c1f1)
> 
> D
> 
> drive (SAS/SATA), reseating [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_332bc01b-5a75-48ab-b23f-444faf066e4c)
> 
> drive blank, installing [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_1b2583d0-a446-4ff2-8e35-f6f1ff2ec29e)
> 
> drive, installing [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_d2f6a981-2c02-4397-a0a8-63b9d2f9f33e)
> 
> drive, removing [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_96280739-0120-489f-9e06-87c93e6e43b1) [2](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_f61655a9-46ad-4e41-b324-8928ed94f135)
> 
> F
> 
> front mezzanine module, installing [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_5de7ce00-e27e-4a07-9b9f-c2d161504a04)
> 
> front mezzanine module, removing [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_ae651cb7-9fa9-4e8c-a698-45ea0eee9ee9)
> 
> front mezzanine PCBAs, recycling [1](m-recycling-components.html#recycling-the-front-mezzanine-module-pcbas)
> 
> H
> 
> heatsink, removing [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_38f14d54-eda9-4b1d-b72c-39b2ef89c1f1)
> 
> I
> 
> installing an M.2 NVMe SSD [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_fbba6b1f-1489-4765-b4fe-a8b9eee4cba1)
> 
> installing an M.2 SATA SSD [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_fbba6b1f-1489-4765-b4fe-a8b9eee4cba1)
> 
> installing bridge card [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_5ef0f92f-3491-4e58-b811-aafac6faf585)
> 
> installing compute node cover [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_0d8487b0-299e-4d9d-8693-a657818cda90)
> 
> installing CPU and heatsink [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_825e3c4c-7a2e-4ebb-9ef6-f3eea00f4180)
> 
> installing drive [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_d2f6a981-2c02-4397-a0a8-63b9d2f9f33e)
> 
> installing front mezzanine module [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_5de7ce00-e27e-4a07-9b9f-c2d161504a04)
> 
> installing rear mezzanine card [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_17b00f2d-65a9-4995-b732-2a2d6cc78d3a)
> 
> installing SuperCap module [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_f9c25723-d884-46b5-a7a2-e715f20386a6)
> 
> installing, compute node [1](m-installing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_f863fd96-b47b-429f-84dd-096085fa347a)
> 
> installing, compute node blank [1](m-installing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_25761031-a2b9-4377-ab11-95b70fdade99)
> 
> installing, CPU [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_825e3c4c-7a2e-4ebb-9ef6-f3eea00f4180)
> 
> installing, drive blank [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_1b2583d0-a446-4ff2-8e35-f6f1ff2ec29e)
> 
> installing, heatsink [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_825e3c4c-7a2e-4ebb-9ef6-f3eea00f4180)
> 
> installing, mLOM [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_afb2a49b-2968-415a-8aa4-081cfc4e16a9)
> 
> installing, NVMe pass-through controller [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_2c18b61c-d83b-48f9-a8d6-1ecc3669d409)
> 
> installing, RAID controller [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_2c18b61c-d83b-48f9-a8d6-1ecc3669d409)
> 
> L
> 
> LED
> 
> compute node activity [1](m-overview.html#Cisco_Reference.dita_806ab63e-975b-457b-9da4-ea160314d43e)
> 
> compute node health [1](m-overview.html#Cisco_Reference.dita_806ab63e-975b-457b-9da4-ea160314d43e)
> 
> compute node locator [1](m-overview.html#Cisco_Reference.dita_806ab63e-975b-457b-9da4-ea160314d43e)
> 
> compute node power [1](m-overview.html#Cisco_Reference.dita_806ab63e-975b-457b-9da4-ea160314d43e)
> 
> drive activity [1](m-overview.html#Cisco_Reference.dita_806ab63e-975b-457b-9da4-ea160314d43e)
> 
> drive health [1](m-overview.html#Cisco_Reference.dita_806ab63e-975b-457b-9da4-ea160314d43e)
> 
> M
> 
> M.2 NVMe SSD, installing [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_fbba6b1f-1489-4765-b4fe-a8b9eee4cba1)
> 
> M.2 NVMe SSD, removing [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_f281420e-222a-4bb5-ba50-d59ac9793fe7)
> 
> M.2 SATA SSD, installing [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_fbba6b1f-1489-4765-b4fe-a8b9eee4cba1)
> 
> M.2 SATA SSD, removing [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_f281420e-222a-4bb5-ba50-d59ac9793fe7)
> 
> mezzanine module, front [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_ae651cb7-9fa9-4e8c-a698-45ea0eee9ee9)
> 
> mLOM, installing [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_afb2a49b-2968-415a-8aa4-081cfc4e16a9)
> 
> mLOM, removing [1](m-servicing-the-compute-node.html#removing-the-mlom)
> 
> mLOM, servicing [1](m-servicing-the-compute-node.html#Cisco_Concept.dita_44ff6f11-6884-4feb-8166-77625469db36)
> 
> motherboard PCB, recycling [1](m-recycling-components.html#Cisco_Task_in_List_GUI.dita_d85086d0-4d89-49f5-979d-e16d31fa6102)
> 
> N
> 
> NVMe pass-through controller, installing [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_2c18b61c-d83b-48f9-a8d6-1ecc3669d409)
> 
> NVMe pass-through module, removing [1](m-servicing-the-compute-node.html#removing-the-m.2-raid-controller-module)
> 
> R
> 
> RAID controller, installing [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_2c18b61c-d83b-48f9-a8d6-1ecc3669d409)
> 
> RAID controller, removing [1](m-servicing-the-compute-node.html#removing-the-m.2-raid-controller-module)
> 
> rear mezzanine card, installing [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_17b00f2d-65a9-4995-b732-2a2d6cc78d3a)
> 
> recycling, front mezzanine PCBAs [1](m-recycling-components.html#recycling-the-front-mezzanine-module-pcbas)
> 
> recycling, motherboard PCB [1](m-recycling-components.html#Cisco_Task_in_List_GUI.dita_d85086d0-4d89-49f5-979d-e16d31fa6102)
> 
> removing an M.2 NVMe SSD [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_f281420e-222a-4bb5-ba50-d59ac9793fe7)
> 
> removing an M.2 SATA SSD [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_f281420e-222a-4bb5-ba50-d59ac9793fe7)
> 
> removing compute node [1](m-installing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_3efa87f6-969a-4184-b80f-1b05e284a66a)
> 
> removing compute node cover [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_cbf2ee70-df1d-4095-b066-db7268a991b7)
> 
> removing CPU and heatsink [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_38f14d54-eda9-4b1d-b72c-39b2ef89c1f1)
> 
> removing drive [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_96280739-0120-489f-9e06-87c93e6e43b1) [2](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_f61655a9-46ad-4e41-b324-8928ed94f135)
> 
> removing SuperCap module [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_375b9517-6c92-48de-9ba8-8c0592647809)
> 
> removing, bridge card [1](m-servicing-the-compute-node.html#removing-the-bridge-card)
> 
> removing, compute node blank [1](m-installing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_c3949737-3f5e-491c-bd83-2c3732c3a107)
> 
> removing, front mezzanine module [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_ae651cb7-9fa9-4e8c-a698-45ea0eee9ee9)
> 
> removing, mLOM [1](m-servicing-the-compute-node.html#removing-the-mlom)
> 
> removing, NVME pass-through module [1](m-servicing-the-compute-node.html#removing-the-m.2-raid-controller-module)
> 
> removing, RAID controller [1](m-servicing-the-compute-node.html#removing-the-m.2-raid-controller-module)
> 
> removing, trusted platform module (TPM) [1](m-recycling-components.html#Cisco_Task_in_List_GUI.dita_2380527b-5143-4b42-9af4-f31bb70d7e1e)
> 
> removing, VIC [1](m-servicing-the-compute-node.html#removing-a-vic)
> 
> reseating drives, SAS/SATA [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_332bc01b-5a75-48ab-b23f-444faf066e4c)
> 
> S
> 
> SAS/SATA drive, reseating [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_332bc01b-5a75-48ab-b23f-444faf066e4c)
> 
> servicing, mLOM [1](m-servicing-the-compute-node.html#Cisco_Concept.dita_44ff6f11-6884-4feb-8166-77625469db36)
> 
> SuperCap module, installing [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_f9c25723-d884-46b5-a7a2-e715f20386a6)
> 
> SuperCap module, removing [1](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_375b9517-6c92-48de-9ba8-8c0592647809)
> 
> T
> 
> trusted platform module (TPM), removing [1](m-recycling-components.html#Cisco_Task_in_List_GUI.dita_2380527b-5143-4b42-9af4-f31bb70d7e1e)
> 
> V
> 
> VIC, removing [1](m-servicing-the-compute-node.html#removing-a-vic)

---

## Page 9: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x210c-m8/install/m-connecting.html

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

## Page 10: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x210c-m8/install/m-installing-the-compute-node.html

# Installing the Compute Node

This chapter contains the following topics:

## Removing a Compute Node Blank

Do not operate the Cisco UCS X9508 chassis with an empty compute node slot. Fill any empty compute node slots with either a blank or a compute node. 

Use this task to remove a compute node blank.

### Procedure

* * *

**Step 1** |  Grasp the compute node blank by the finger holds.   
---|---  
**Step 2** |  Pull the blank towards you until it is completely removed from the chassis.  Notice that the module blank has indicators that show how to orient the blank. You will use this information when you install a blank.  Figure 1. Removing a Compute Node Blank  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309103.jpg)  
  
* * *

## Installing a Compute Node Blank

If you remove a compute node, and you will not be installing another compute node, you must install a node blank (UCSX-9508-FSBK). Do not operate the UCS X9508 chassis with an empty compute node slot. The minimum configuration is 1 installed compute node, so in this configuration you need 7 module blanks installed. 

Compute node blanks are interchangeable within the same chassis or other Cisco UCS X9508 chassis. 

Use this task to install a compute node blank

### Procedure

* * *

**Step 1** |  Grasp the blank by the finger holds.   
---|---  
**Step 2** |  Hold the module blank vertically and align the module blank with the slot.  The module blank has indicators that show how to orient the blank. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309104.jpg)  
**Step 3** |  Keeping the compute node blank vertical, slide it into the slot until the blank is flush with the face of the chassis.  Figure 2. Installing a Compute Node Blank  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308917.jpg)  
  
* * *

## Removing a Compute Node

You must decommission the compute node using Cisco UCS management software (Cisco Intersight or Cisco UCS Manager) before physically removing the compute node. 

Do not operate the chassis with an empty compute node slot. If you will not be installing a compute node in an empty slot, install a compute node blank (UCSX-9508-FSBK) to cover the empty slot. 

### Procedure

* * *

**Step 1** |  Turn off the compute node by using Cisco UCS management software.   
---|---  
**Step 2** |  Press the release button at the center of the compute node's faceplate to disengage the ejector handles.   
**Step 3** |  Grasp the ejector handles and pull them outward so that they arc vertically away from each other. While moving the compute node handles, you might feel some resistance. This resistance is normal. It occurs because the connectors at the rear of the compute node are unseating from the corresponding sockets in the chassis.  Also, when the compute node disconnects from the midplane, the compute node powers off. |  **Caution** |  Whenever a compute node is removed, you must wait at least 20 seconds before inserting the compute node back into the chassis.  
---|---  
Figure 3. Removing a Compute Node  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309119.jpg)  
**Step 4** |  Grasp the compute node handles and slide it partially out of the chassis.  Make sure to keep the compute node vertical while removing it.  
**Step 5** |  Place your other hand underneath the compute node to support it and slide the compute node completely out of the chassis.   
**Step 6** |  Once removed, place the compute node on an antistatic mat or antistatic foam if you are not immediately reinstalling it.   
**Step 7** |  Do one of the following: 

  1. If you will be installing another compute node, see Installing a Compute Node. 
  2. If the compute node slot is to remain empty, reinstall the compute node blank panels (UCSX-9508-FSBK) to maintain proper thermal temperatures and to keep dust out of the chassis. 

  
  
* * *

## Installing a Compute Node

### Before you begin

The compute node must have its cover installed before installing it into the chassis to ensure adequate airflow.

### Procedure

* * *

**Step 1** |  Remove a compute node blank. See Removing a Compute Node.  |  **Caution** |  Whenever a compute node is removed, you must wait at least 20 seconds before inserting the compute node back into the chassis.  
---|---  
**Step 2** |  Press the release button at the center of the compute node faceplate to release the ejectors. |  **Note** |  While you are inserting the compute node, keep the ejectors open.  
---|---  
**Step 3** |  Holding the compute node vertical, align it with the empty module bay in the chassis.  The compute node is correctly aligned when the compute node top cover is pointing to the left.  Figure 4. Aligning and Installing a Compute Node  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309120.jpg)  
**Step 4** |  When the compute node is almost completely installed, grasp the ejector handles and arc them toward each other.  This step seats the compute node into the connector. The compute node should power up.  
**Step 5** |  Push the ejectors until they are parallel with the face of the compute node.  When the compute node is completely installed, the retention latches at the end of each handle click into place.   
**Step 6** |  Configure the compute node as needed through Cisco UCS management software. See Compute Node Configuration.   
  
* * *

## Compute Node Configuration

Cisco UCS M8 compute nodes, such as the Cisco UCS X210c M8, can be configured and managed using the Cisco UCS management software, either: 

  * Cisco Intersight management platform in Intersight Managed Mode (Cisco Intersight Managed Mode). For details, see the Cisco Intersight Managed Mode Configuration Guide, which is available at the following URL: [Cisco Intersight Managed Mode Configuration Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Intersight_Managed_Mode_Configuration_Guide.html)

  * Cisco UCS Manager (UCSM), version 4.3(2) or later. For details, see the latest version of the Cisco UCS Manager Administration Management Guide 4.3 which is available at the following URL: [Cisco UCS Manager Administration Management Guide 4.3](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Admin-Management/4-3/b_cisco_ucs_admin_mgmt_guide_4-3.html)


---

## Page 11: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x210c-m8/install/m-overview.html

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

## Page 12: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x210c-m8/install/m-servicing-the-compute-node.html

# Servicing the Compute Node  
  
This chapter contains the following topics:

## Removing and Installing the Compute Node Cover

The top cover of the Cisco UCS X210c M8 Compute Node can be removed to allow access to internal components, some of which are field-replaceable. The green button on the top cover releases the compute node so that it can be removed from the compute node. 

  * Removing a Compute Node Cover

  * Installing a Compute Node Cover


  * Removing a Compute Node Cover
  * Installing a Compute Node Cover


### Removing a Compute Node Cover

To remove the cover of the Cisco UCS X210c M8 Compute Node, follow these steps: 

#### Procedure

* * *

**Step 1** |  Press and hold the button down (1, in the figure below).   
---|---  
**Step 2** |  While holding the back end of the cover, slide it back, then pull it up (2).  By sliding the cover back, you enable the front edge to clear the metal lip on the rear of the front mezzanine module.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308975.jpg)  
  
* * *

### Installing a Compute Node Cover 

Use this task to install a removed top cover for the UCS X210c M8 compute node. 

#### Procedure

* * *

**Step 1** |  Insert the cover angled so that it hits the stoppers on the base.  
---|---  
**Step 2** |  Lower the compute node's cover until it reaches the bottom.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309646.jpg)  
**Step 3** |  Keeping the compute node's cover flat, slide it forward until the release button clicks.   
  
* * *

## Internal Components

The following illustration shows the location of internal components on the compute node. 

![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472725.png)

1 |  Front mezzanine module slot |  2 |  Mini-Storage module connector, which supports one mini-storage module with up to two M.2 SATA or M.2 NVMe drives.  
---|---|---|---  
3 |  Front mezzanine slot connectors |  4 |  CPU 1, which supports Sixth Generation Intel Xeon Scalable Processors.  
5 |  DIMM Slots |  6 |  Debug connector Only for use by Cisco personnel.  
7 |  CPU 2, which supports Sixth Generation Intel Xeon Scalable Processors. |  8 |  Motherboard USB Connector  
9 |  TPM Connector |  10 |  Rear mezzanine slot.  
11 |  Bridge Card slot, which connects rear mezzanine slot and the mLOM/VIC slot |  12 |  mLOM/VIC slot that supports zero or one Cisco VIC or Cisco X-Series 100 Gbps mLOM  
  
## Replacing a Drive

You can remove and install some drives without removing the compute node from the chassis. All drives have front-facing access, and they can be removed and inserted by using the ejector handles. 

The SAS/SATA or NVMe drives supported in this compute node come with the drive sled attached. Spare drive sleds are not available. 

Before upgrading or adding a drive to a running compute node, check the service profile through Cisco UCS management software and make sure the new hardware configuration will be within the parameters allowed by the management software. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

To prevent ESD damage, wear grounding wrist straps during these procedures. 

* * *  
  
---|---  
  
  * NVMe SSD Requirements and Restrictions
  * Enabling Hot Plug Support
  * Removing a Drive
  * Installing a Drive
  * Basic Troubleshooting: Reseating a SAS/SATA Drive


### NVMe SSD Requirements and Restrictions

For 2.5-inch NVMe SSDs, be aware of the following:

  * NVMe 2.5 SSDs support booting only in UEFI mode. Legacy boot is not supported. 

UEFI boot mode can be configured through Cisco UCS management software. For information about Cisco UCS management software, see [Compute Node Configuration](m-installing-the-compute-node.html#Cisco_Reference.dita_d5beb410-8b0c-44e7-836c-7a86d663e54e). 

  * NVME U.3 SSDs connect to the RAID controller so RAID is supported for these drives. 

  * UEFI boot is supported in all supported operating systems. 


### Enabling Hot Plug Support

Surprise and OS-informed hot plug is supported with the following conditions:

  * VMD must be enabled to support hot plug. 

  * VMD must be enabled before installing an OS on the drive. 

  * If VMD is not enabled, surprise hot plug is not supported, and you must do OS-informed hotplug instead.

  * VMD is required for both surprise hot plug and drive LED support. 


### Removing a Drive

Use this task to remove a SAS/SATA or NVMe drive from the compute node. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Do not operate the system with an empty drive bay. If you remove a drive, you must reinsert a drive or cover the empty drive bay with a drive blank. 

* * *  
  
---|---  
  
#### Procedure

* * *

**Step 1** |  Push the release button to open the ejector, and then pull the drive from its slot.  |  **Caution** |  To prevent data loss, make sure that you know the state of the system before removing a drive.  
---|---  
  
![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308996.jpg)  
  
**Step 2** |  Place the drive on an antistatic mat or antistatic foam if you are not immediately reinstalling it in another compute node.  
**Step 3** |  Install a drive blanking panel to maintain proper airflow and keep dust out of the drive bay if it will remain empty.   
  
* * *

#### What to do next

Cover the empty drive bay. Choose the appropriate option:

  * Installing a Drive

  * Installing a Drive Blank


### Installing a Drive

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

For hot installation of drives, after the original drive is removed, you must wait for 20 seconds before installing a drive. Failure to allow this 20-second wait period causes the Cisco UCS management software to display incorrect drive inventory information. If incorrect drive information is displayed, remove the affected drive(s), wait for 20 seconds, then reinstall them. 

* * *  
  
---|---  
  
To install a SAS/SATA or NVMe drive in the compute node, follow this procedure:

#### Procedure

* * *

**Step 1** |  Place the drive ejector into the open position by pushing the release button.   
---|---  
**Step 2** |  Gently slide the drive into the empty drive bay until it seats into place.  
**Step 3** |  Push the drive ejector into the closed position. You should feel the ejector click into place when it is in the closed position. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309002.jpg)  
  
* * *

### Basic Troubleshooting: Reseating a SAS/SATA Drive

Sometimes it is possible for a false positive UBAD error to occur on SAS/SATA HDDs installed in the compute node. 

  * Only drives that are managed by the UCS MegaRAID controller are affected. 

  * Both SFF and LFF form factor drives can be affected.

  * Drives can be affected regardless of whether they are configured for hot plug or not.

  * The UBAD error is not always terminal, so the drive is not always defective or in need of repair or replacement. However, it is also possible that the error is terminal, and the drive will need replacement. 


**Before submitting the drive to the RMA process** , it is a best practice to reseat the drive. If the false UBAD error exists, reseating the drive can clear it. If successful, reseating the drive reduces inconvenience, cost, and service interruption, and optimizes your compute node uptime. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Reseat the drive only if a UBAD error occurs. Other errors are transient, and you should not attempt diagnostics and troubleshooting without the assistance of Cisco personnel. Contact Cisco TAC for assistance with other drive errors. 

* * *  
  
---|---  
  
To reseat the drive, see Reseating a SAS/SATA Drive. 

  * Reseating a SAS/SATA Drive


#### Reseating a SAS/SATA Drive

Sometimes, SAS/SATA drives can throw a false UBAD error, and reseating the drive can clear the error. 

Use the following procedure to reseat the drive. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

This procedure might require powering down the server. Powering down the server will cause a service interruption.

* * *  
  
---|---  
  
##### Before you begin

Before attempting this procedure, be aware of the following:

  * Before reseating the drive, it is a best practice to back up any data on it.

  * When reseating the drive, make sure to reuse the same drive bay.

  * Do not move the drive to a different slot.

  * Do not move the drive to a different server.

  * If you do not reuse the same slot, the Cisco UCS management software (for example, Cisco IMM) might require a rescan/rediscovery of the server. 

  * When reseating the drive, allow 20 seconds between removal and reinsertion.


##### Procedure

* * *

**Step 1** |  Attempt a hot reseat of the affected drive(s). For a front-loading drive, see Removing a Drive.  |  **Note** |  While the drive is removed, it is a best practice to perform a visual inspection. Check the drive bay to ensure that no dust or debris is present. Also, check the connector on the back of the drive and the connector on the inside of the server for any obstructions or damage.  Also, when reseating the drive, allow 20 seconds between removal and reinsertion.   
---|---  
**Step 2** |  During boot up, watch the drive's LEDs to verify correct operation.  See [Interpreting LEDs](m-overview.html#Cisco_Reference.dita_806ab63e-975b-457b-9da4-ea160314d43e).   
**Step 3** |  If the error persists, cold reseat the drive, which requires a server power down. Choose the appropriate option:

  1. Use your server management software to gracefully power down the server.  See the appropriate Cisco UCS management software documentation.
  2. If server power down through software is not available, you can power down the server by pressing the power button. See [Compute Node Front Panel](m-overview.html#Cisco_Concept.dita_e57757cc-ebfe-45bc-94ca-21d942b7ac07). 
  3. Reseat the drive as documented in Step 1. 
  4. When the drive is correctly reseated, restart the server, and check the drive LEDs for correct operation as documented in Step 2. 

  
**Step 4** |  If hot and cold reseating the drive (if necessary) does not clear the UBAD error, choose the appropriate option: 

  1. Contact Cisco Systems for assistance with troubleshooting.
  2. Begin an RMA of the errored drive.

  
  
* * *

## Removing a Drive Blank

A maximum of six SAS/SATA or NVMe drives are contained in the front mezzanine storage module as part of the drive housing. The drives are front facing, so removing them does not require any disassembly. 

Use this procedure to remove a drive blank from the compute node. 

### Procedure

* * *

**Step 1** |  Grasp the drive blank handle.   
---|---  
**Step 2** |  Slide the drive blank out of the slot.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308990.jpg)  
  
* * *

### What to do next

Cover the empty drive bay. Choose the appropriate option: 

  * Installing a Drive

  * Installing a Drive Blank


## Installing a Drive Blank

Use this task to install a drive blank. 

### Procedure

* * *

**Step 1** |  Align the drive blank so that the sheet metal is facing down.   
---|---  
**Step 2** |  Holding the blank level, slide it into the empty drive bay.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308999.jpg)  
  
* * *

## Replacing the Front Mezzanine Module

The front mezzanine module is a steel cage that contains the compute node's storage devices or a mix of GPUs and drives. The front mezzanine storage module can contain any of the following storage configurations: 

  * NVMe U.3 drives 

  * SAS/SATA drives

  * Cisco L4-MEZZ GPUs plus up to two U.3 NVMe drives

  * E3.S 1TB PCIe drives


In the front mezzanine slot, the compute node can use one of the following front storage module options:

  * A front mezzanine blank (UCSX-M8A-FMEZZBLK ) for systems without local disk requirements.

  * Compute Pass Through Controller (UCSX-X10C-PT4F-D): supports up to six hot pluggable 15mm NVMe drives directly connected to CPU 1. 

  * MRAID Storage Controller Module (UCSX-X10C-RAIDF):

  * Supports a mixed drive configuration of up to six SAS, SATAdrives. With a mix of SAS/SATA and NVMe drives are supported in slots one through four only. 

  * Provides HW RAID support for SAS/SATA drives in multiple RAID groups and levels.

  * Supports NVMe U.3 drives in slots 1 through 6 and can be configured into multiple RAID groups and levels similar to SAS/SATA drives. 

  * Supports a mix of SAS/SATA and NVMe U.3 drives behind the MRAID controller. However, these NVMe drives and SAS/SATA drives cannot be combined in the same RAID group. 

NVME U.3 drives can be combined to make RAID groups separately. Also, SAS/SATA drives can be formed into different RAID groups, and the different RAID groups can co-exist in the same MRAID storage setup. 

  * The front mezzanine module also contains the SuperCap module. For information about replacing the SuperCap module, see Replacing the SuperCap Module. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The SuperCap module is only needed when the MRAID Storage Controller module (UCSX-RAID-M1L6) or Compute RAID Controller (UCSX-X10C-RAIDF) is installed. 

* * *  
  
---|---  
  * A compute and storage option (UCSX-X10C-GPUFM) consisting of a GPU adapter supporting zero, one, or two Cisco L4-MEZZ GPUs (UCSX-GPU-L4-MEZZ) plus zero, one, or two U.3 NVMe SSDs. 

  * A Tri-mode M1 front mezzanine module (UCSX-RAID-M1L6). Each Tri-mode M1 front mezzanine module consists of the following components:

  * Up to six (6) SAS/SATA/NVMe SSD drives. Each drive slot supports either SAS, SATA or NVMe U.3 SSDs (RAID Controller)

  * A Front Mezzanine Pass Through Controller for E3.S drives (UCSX-X10C-PTE3).

  * The front mezzanine E3.S module supports up to nine E3.S PCIe drives.


The front mezzanine module can be removed and installed as a whole unit to give easier access to the storage drives that it holds. Or, you can leave the front mezzanine module installed because SAS/SATA and the NVMe drives are accessible directly through the front of the front mezzanine panel and are hot pluggable. 

To replace the front mezzanine module, use the following topics: 

  * Removing the Front Mezzanine Module

  * Installing the Front Mezzanine Module


  * Front Mezzanine Module Guidelines
  * Removing the Front Mezzanine Module
  * Installing the Front Mezzanine Module


### Front Mezzanine Module Guidelines

Be aware of the following guidelines for the front mezzanine slot:

  * The compute node supports the following configuration options:

  * For MRAID Storage Controller Module (UCSX-X10C-RAIDF), M.2 Mini Storage, and NVMe storage, only UEFI boot mode is supported.

  * (UCSX-X10C-GPUFM) that supports up to two Cisco L4-MEZZ GPUs 

  * (UCSX-GPU-L4-MEZZ) and up to two NVMe U.3 drives in the front mezzanine slot. For information about the GPU-based front mezzanine option, see the [Cisco UCS X10c Front Mezzanine GPU Module Installation and Service Guide](https://www-author3.cisco.com/content/en/us/td/docs/unified_computing/ucs/x/hw/x10c-gpu-module/install/cisco-ucs-x10c-front-mezzanine-gpu-install-guide.html). 

  * (UCSX-RAID-M1L6) front mezzinne that supports up to six (6) SAS/SATA/NVMe SSD drives. 

  * Each drive slot supports either SAS, SATA or NVMe U.3 SSDs (RAID Controller). For more information about RAID controller based front mezzanine option, see the [Cisco UCS X10c Front Mezzanine GPU Module Installation and Service Guide](https://www-author3.cisco.com/content/en/us/td/docs/unified_computing/ucs/x/hw/x10c-gpu-module/install/cisco-ucs-x10c-front-mezzanine-gpu-install-guide.html). 

  * (UCSX-X10C-PTE3) front mezzznine that supports up to six (9) Nine E3.S 1T PCIe5 drives. 

  * Each drive slot supports either SAS, SATA or NVMe U.3 SSDs (RAID Controller). For more information about E3.S drives based front mezzanine option, see the [Cisco UCS X10c Pass Through Controller for E3.S Installation and Service Guide](https://www-author3.cisco.com/content/en/us/td/docs/unified_computing/ucs/x/hw/x10c-e3s/install/b-cisco-ucs-x10c-compute-pass-through-controller-e3s.html). 

. 
  * (UCSX-X10C-PT4F) Computer Pass Through Controller. The front mezzanine supports:

  * Up to 6 x 2.5-inch SAS and SATA RAID-compatible SSDs or NVMe PCIe drives. 

  * A mixture of up to six SAS/SATA or NVMe drives or up to two GPUs and up to two NVMe drives. 

For more information about E3.S drives based front mezzanine option, see the [Cisco UCS X210c M7 Compute Node Installation and Service Guide](https://www-author3.cisco.com/content/en/us/td/docs/unified_computing/ucs/x/hw/x210c-m7/install/b-cisco-ucs-x210c-m7-install-guide/m-servicing-the-compute-node.html). 


### Removing the Front Mezzanine Module

Use the following procedure to remove the front mezzanine module. This procedure applies to the following modules:

  * Computer Pass Through Controller (UCSX-X10C-PT4F)

  * Compute RAID Controller with LSI 3900 (UCSX-X10C-RAIDF)

  * Compute Node GPU Front Mezz (UCSX-X10C-GPUFM)

  * Compute Pass Through Controller for E3.S (UCSX-X10C-PTE3)

  * 24G Tri-Mode M1 RAID Controller (UCSX-RAID-M1L6)


#### Before you begin

To remove the front mezzanine module, you need a T8 screwdriver and a #2 Phillips screwdriver. 

#### Procedure

* * *

**Step 1** |  If the compute node's cover is not already removed, remove it now. Remove the compute node cover.  See Removing a Compute Node Cover.   
---|---  
**Step 2** |  Remove the securing screws:

  1. Using a #2 Phillips screwdriver, loosen the two captive screws on the top of the front mezzanine module.  |  **Note** |  This step may be skipped if removing the front mezzanine blank (UCSX-M8A-FMEZZBLK).  
---|---  
  2. Using a T8 screwdriver, remove the two screws on each side of the compute node that secure the front mezzanine module to the sheet metal. 

![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308992.jpg)


  
**Step 3** |  Making sure that all the screws are removed, lift the front mezzanine module to remove it from the compute node.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/309000.jpg)  
  
* * *

#### What to do next

To install the front mezzanine module, see Installing the Front Mezzanine Module

### Installing the Front Mezzanine Module

Use the following procedure to install the front mezzanine module. This procedure applies to the following modules:

  * Front mezzanine blank (UCSX-M8A-FMEZZBLK)

  * Compute Pass Through Controller (UCSX-X10C-PT4F-D)

  * MRAID Storage Controller Module (UCSX-X10C-RAIDF)

  * Compute and storage option (UCSX-X10C-GPUFM-D) 

  * Tri-mode RAID Controller(UCSX-RAID-M1L6)

  * E3.S Pass Through Controller (UCSX-X10C-PTE3)


#### Before you begin

To install the front mezzanine module, you need a T8 screwdriver and a #2 Phillips screwdriver.

#### Procedure

* * *

**Step 1** |  Align the front mezzanine module with its slot on the compute node.   
---|---  
**Step 2** |  Lower the front mezzanine module onto the compute node, making sure that the screws and screwholes line up.  
**Step 3** |  Secure the front mezzanine module to the compute node. 

  1. Using a #2 Phillips screwdriver, tighten the captive screws on the top of the front mezzanine module.  |  **Note** |  This step may be skipped if installing the front mezzanine blank (UCSX-M8A-FMEZZBLK).  
---|---  
![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308992.jpg)
  2. Using a T8 screwdriver, insert and tighten the four screws, two on each side of the sever node. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308993.jpg)


  
  
* * *

#### What to do next

If you removed the drives from the front mezzanine module, reinstall them now. See Installing a Drive. 

## Servicing the Mini Storage Module

The compute node has a mini-storage module option that plugs into a motherboard socket to provide additional internal storage. The module sits vertically behind the left side front panel. See Internal Components. 

Two configurations of mini storage module are supported, one with an integrated RAID controller card, and one without.

  * Replacing a Boot-Optimized M.2 RAID Controller Module or NVMe Pass-Through Module
  * Replacing an M.2 SATA or M.2 NVMe SSD


### Replacing a Boot-Optimized M.2 RAID Controller Module or NVMe Pass-Through Module

The Cisco Boot-Optimized M.2 RAID Controller for M.2 SATA drives or the NVMe Pass-Through Controller for M.2 NVMe drives connects to the mini-storage module socket on the motherboard. Each of the following components contains two module slots for M.2 drives: 

  * The Cisco UCSX Front panel with M.2 RAID controller for SATA drives (UCSX-M2I-HWRD-FPS). This component has an integrated 6-Gbps SATA RAID controller that can control the SATA M.2 drives in a RAID 1 array. 

  * The Cisco UCSX Front panel with M.2 Pass Through controller for NVME drives (UCSX-M2-PT-FPN). The M.2 NVMe drives are not configurable in a RAID group. 


  * Cisco Boot-Optimized M.2 RAID Controller Considerations
  * Removing the M.2 RAID Controller Module or NVMe Pass-Through Module
  * Installing the M.2 RAID Controller Module or NVMe Pass-Through Controller Module


#### Cisco Boot-Optimized M.2 RAID Controller Considerations

Review the following considerations:

  * This controller supports RAID 1 (single volume) and JBOD mode.

  * A SATA M.2 drive in slot 1 is located on the right side, or front, of the module when installed. This drive faces the interior of the compute node. This drive is the first SATA device. 

  * A SATA M.2 drive in slot 2 is located on the left side, or back, of the module when installed. This drive faces the compute node's sheet metal wall. This drive is the second SATA device. 

  * The name of the controller in the software is MSTOR-RAID.

  * A drive in slot 1 is mapped as drive 253; a drive in slot 2 is mapped as drive 254.

  * When using RAID, we recommend that both SATA M.2 drives are the same capacity. If different capacities are used, the smaller capacity of the two drives is used to create a volume and the rest of the drive space is unusable. 

JBOD mode supports mixed capacity SATA M.2 drives.

  * Hot-plug replacement is _not_ supported. The compute node must be powered off. 

  * Monitoring of the controller and installed SATA M.2 drives can be done using Cisco UCS management software. They can also be monitored using other utilities such as UEFI HII, and Redfish. 

  * The SATA M.2 drives can boot in UEFI mode only. Legacy boot mode is not supported.

  * If you replace a single SATA M.2 drive that was part of a RAID volume, rebuild of the volume is auto-initiated after the user accepts the prompt to import the configuration. If you replace both drives of a volume, you must create a RAID volume and manually reinstall any OS. 

  * We recommend that you erase drive contents before creating volumes on used drives from another compute node. The configuration utility in the compute node BIOS includes a SATA secure-erase function. 


#### Removing the M.2 RAID Controller Module or NVMe Pass-Through Module

This topic describes how to remove a Cisco Boot-Optimized M.2 RAID Controller or a Cisco NVMe Pass-Through Controller:

  * The Cisco UCSX Front panel with M.2 RAID controller for SATA drives (UCSX-M2I-HWRD-FPS). 

  * The Cisco UCSX Front panel with M.2 Pass-Through module for NVME drives (UCSX-M2-PT-FPN). 


Both types of controller board have two slots, one for each M.2 drive:

  * one M.2 slot (Slot 1) for either a SATA drive (in UCSX-M2I-HWRD-FPS) or an NVMe drive (in UCSX-M2-PT-FPN). The drive in this slot faces the interior of the compute node. 

  * one M.2 slot (Slot 2) for either a SATA drive (in UCSX-M2I-HWRD-FPS) or an NVMe drive (in UCSX-M2-PT-FPN). The drive in this slot faces the chassis sheetmetal wall. 

  * Drive slot numbering differs depending on which Cisco management tool you are using and which component is being managed.

Component |  Cisco Management Tool  
---|---  
Intersight (IMM) |  UCS Manager (UCSM)  
RAID Controller |  Slot 1 contains Drive 253 Slot 2 contains Drive 254 |  Slot 1 contains Drive 253 Slot 2 contains Drive 254  
NVMe Pass-Through Controller |  Slot 1 contains Drive 253 Slot 2 contains Drive 254 |  Slot 1 contains Drive 32 Slot 2 contains Drive 33  


Each controller can be populated with up to two M.2 drives of the correct type, either SATA for the RAID controller or NVMe for the Pass-Through controller. Single M.2 SATA or NVMe drives are supported. You cannot mix M.2 drive types in the same controller. 

To remove the controller or the M.2 drives, the front mezzanine module must be removed first. 

##### Procedure

* * *

**Step 1** |  Remove the controller from the compute node:

  1. Decommission, power off, and remove the compute node from the chassis. 
  2. Remove the top cover from the compute node as described in Removing and Installing the Compute Node Cover. 

  
---|---  
**Step 2** |  If you have not already done so, remove the front mezzanine module.  See Removing the Front Mezzanine Module.   
**Step 3** |  Remove the controller.

  1. Locate the controller in the front corner of the server along the compute node's sidewall.
  2. Using a #2 Phillips screwdriver, loosen the captive screw that secures the module to the motherboard. 
  3. At the end opposite the front panel, grasp the module and pull up in an arc to disconnect the controller from its motherboard socket. 
  4. Holding the controller at an angle, slide it away from the front panel and lift it up to disengage the LEDs and buttons from their cutouts in the front panel.  |  **Caution** |  If you feel resistance while lifting the controller, make sure that the LEDs and buttons are not still seated in the front panel.   
---|---  
  
![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472285.jpg)


  
**Step 4** |  If you are transferring M.2 drives from the old controller to a replacement controller, do that before installing the replacement controller:  |  **Note** |  Any previously configured volume and data on the drives are preserved when the M.2 drives are transferred to the new controller. The system will boot the existing OS that is installed on the drives.   
---|---  
  
  1. Use a #1 Phillips-head screwdriver to remove the single screw that secures the M.2 drive to the carrier.

  2. Lift the M.2 drive from its slot on the carrier.

  3. Position the replacement M.2 drive over the slot on the controller board.

  4. Angle the M.2 drive downward and insert the connector-end into the slot on the carrier. The M.2 drive's label must face up.

  5. Press the M.2 drive flat against the carrier.

  6. Install the single screw that secures the end of the M.2 SSD to the carrier.

  7. Turn the controller over and install the second M.2 drive.


  
  
* * *

#### Installing the M.2 RAID Controller Module or NVMe Pass-Through Controller Module

Use this task to install the RAID controller or NVME Pass-through controller module. 

##### Before you begin

This topic describes how to remove a Cisco Boot-Optimized M.2 RAID Controller or a Cisco NVMe Pass-Through Controller:

  * The Cisco UCSX Front panel with M.2 RAID controller for SATA drives (UCSX-M2I-HWRD-FPS). 

  * The Cisco UCSX Front panel with M.2 Pass-Through module for NVME drives (UCSX-M2-PT-FPN). 


Each type of controller mounts vertically on the motherboard, and the M.2 drive sockets are positioned vertically on the controller. 

##### Procedure

* * *

**Step 1** |  Install the controller to its socket on the motherboard:

  1. Position the controller over the socket, making sure the golden fingers on the connector are facing down. 
  2. Lower the controller into the chassis at an angle and insert the LEDs and buttons into their cutouts on the front panel.
  3. Holding the controller level, align the captive screw with its screwhole and the golden fingers with their socket on the motherboard. 
  4. Carefully push down on the controller to seat the golden fingers into the socket. 
  5. Use a #2 Phillips screwdriver to tighten the controller onto the threaded standoff.  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472286.jpg)

  
---|---  
**Step 2** |  Reinstall the front mezzanine module.  
**Step 3** |  Return the compute node to service:

  1. Replace the top cover on the compute node.
  2. Reinstall the compute node and allow it to power up and be automatically reacknowledged, reassociated, and recommissioned.

  
  
* * *

### Replacing an M.2 SATA or M.2 NVMe SSD

M.2 SATA and NVMe SSD cards can be installed in vertical drive bays. One drive bay, or slot, is on each side of the M.2 module carrier. 

There are some specific rules for populating mini-storage M.2 SSD cards: 

  * Each carrier supports a maximum of two M.2 cards. Do not mix SATA and NVMe SSD cards in the same mini-storage module. Replacement cards are available from Cisco as pairs. 

  * When installed in the compute node, the M.2 SSDs are mounted vertically.

  * M.2 slot 1 is located on the right side, or front, of the module when installed. This drive faces inward towards the interior the compute node. 

  * M.2 slot 2 is located on the left side, or back, of the module when installed. This drive faces outward towards the compute node sheetmetal wall. 

  * Drive slot numbering depends on the M.2 SSD type and which Cisco Management tool you are using.

  * **M.2 SATA SSD** : Slot 1 contains Drive 253 in both Intersight (IMM) and UCS Manager (UCSM). 

  * **M.2 SATA SSD** : Slot 2 contains Drive 254 in both IMM and UCSM. 

  * **M.2 NVMe SSD** : Slot 1 contains Drive 253 in IMM, but Slot 1 contains Drive 32 in UCSM. 

  * **M.2 NVMe SSD** : Slot 2 contains Drive 254 in IMM, but Slot 2 contains Drive 33 in UCSM. 

  * If your compute node contains only one M.2 SATA or NVMe SSD, it can be installed in either slot. 

  * Dual SATA M.2 SSDs can be configured in a RAID 1 array through the BIOS Setup Utility's embedded SATA RAID interface and configured through IMM. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The M.2 SSDs are managed by the MSTOR-RAID controller. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The embedded SATA RAID controller requires that the compute node is set to boot in UEFI mode rather than Legacy mode.

* * *  
  
---|---  


  * Removing an M.2 SATA or M.2 NVMe SSD
  * Installing an M.2 SATA or M.2 NVMe SSD


#### Removing an M.2 SATA or M.2 NVMe SSD

Each M.2 card plugs into a slot on the carrier, which mounts vertically to the motherboard.

  * One slot is on the front of the carrier, which faces inwards towards the rest of the compute node.

  * One slot is on the back of the carrier, which faces towards the compute node sheetmetal wall. 


Each M.2 SSD is secured to the carrier by the slot at one end, and a small retaining screw at the other end. The carrier is installed on the same component that has the compute node LEDs and buttons on the node's front panel. 

Use the following procedure for any type of mini-storage module carrier. 

##### Procedure

* * *

**Step 1** |  Remove the controller.  See Removing the M.2 RAID Controller Module or NVMe Pass-Through Module.   
---|---  
**Step 2** |  Using a #1 Phillips screwdriver, remove the screws that secure the M.2 SSD to the carrier.  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472284.jpg)  
**Step 3** |  Grasping the M.2 card by its edges, gently lift the end that held the screws at an angle, then slide the card out of its connector.  
  
* * *

##### What to do next

Installing an M.2 SATA or M.2 NVMe SSD

#### Installing an M.2 SATA or M.2 NVMe SSD

Each M.2 SATA or NVMe SSD plugs into a slot on the carrier and is held in place by a retaining screw for each SSD. 

Use the following procedure to install the M.2 SATA or NVMe SSD onto the carrier 

##### Procedure

* * *

**Step 1** |  Install the M.2 SATA or NVMe SSD. 

  1. Orient the SSD correctly.  |  **Note** |  When correctly oriented, the end of the SSD with two alignment holes lines up with the two alignment pins on the carrier.   
---|---  
  2. Angle the end opposite the screw into the connector 

  3. Press down on the end of the SSD that holds the screws until the SSD snaps into place. 

  4. Reinsert and tighten the retaining screw to secure the M.2 module to the carrier.

![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472283.jpg)


  
**Step 2** |  When you are ready, reinstall the controller onto the motherboard.  Installing the M.2 RAID Controller Module or NVMe Pass-Through Controller Module.   
**Step 3** |  Reinstall the compute node cover  
**Step 4** |  Reapply power and return the compute node to service.   
  
* * *

## Replacing the SuperCap Module

The SuperCap module (UCSB-MRAID-SC) is a battery bank which connects to the front mezzanine storage module board and provides power to the RAID controller if facility power is interrupted. The front mezzanine with the SuperCap module installed is UCSX-X10C-RAIDF. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The SuperCap module is only needed when the MRAID Storage Controller module (UCSX-X10C-RAIDF) or (UCSX-RAID-M1L6) is installed.

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

To remove the SuperCap Module you must remove the front mezzanine module.

* * *  
  
---|---  
  
To replace the SuperCap module, use the following topics:

  * Removing the SuperCap Module

  * Installing the SuperCap Module


  * Removing the SuperCap Module
  * Installing the SuperCap Module


### Removing the SuperCap Module

The SuperCap module is part of the Front Mezzanine Module, so the Front Mezzanine Module must be removed from the compute node to provide access to the SuperCap module. 

The SuperCap module sits in a plastic tray on the underside of the front mezzanine module. The SuperCap module connects to the board through a ribbon cable with one connector to the module.  Figure 1. Location of the SuperCap Module  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309003.jpg)

To replace the SuperCap module, follow these steps:

#### Procedure

* * *

**Step 1** |  If you have not already removed the Front Mezzanine module, do so now.  See Removing the Front Mezzanine Module.   
---|---  
**Step 2** |  Before removing the SuperCap module, note its orientation in the tray as shown in the previous image.  When correctly oriented, the SuperCap connection faces downward so that it easily plugs into the socket on the board. You will need to install the new SuperCap module with the same orientation.   
**Step 3** |  Grasp the cable connector at the board and gently pull to disconnect the connector. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309004.jpg)  
**Step 4** |  Grasp the sides of the SuperCap module, but not the connector, and lift the SuperCap module out of the tray. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309005.jpg)You might feel some resistance because the tray is curved to secure the module.  
**Step 5** |  Disconnect the ribbon cable from the SuperCap module:

  1. On the SuperCap module, locate the lever that secures the ribbon cable to the battery pack.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309006.jpg)
  2. Gently pivot the securing lever downward to release the ribbon cable connection from the SuperCap module. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309007.jpg)

  
**Step 6** |  Remove the existing battery pack from its case, and insert a new one, making sure to align the new battery pack so that the connector aligns with the ribbon cable.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309008.jpg)  
  
* * *

#### What to do next

Installing the SuperCap Module

### Installing the SuperCap Module

If you removed the SuperCap module, use this procedure to reinstall and reconnect it. 

#### Procedure

* * *

**Step 1** |  Insert the Super Cap module into its case.

  1. Align the SuperCap module so that the connector will meet the connector. ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309009.jpg)
  2. Before seating the SuperCap module, make sure that the ribbon cable is not in the way. You do not want to pinch the ribbon cable when you install the SuperCap. 
  3. When the ribbon cables are clear of the case, press the SuperCap module until it is seated in the case. You might feel some resistance as the SuperCap snaps into place. 

  
---|---  
**Step 2** |  When the SuperCap module is completely seated in its plastic case, pivot the securing lever to connect the ribbon cable to the SuperCap module.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309010.jpg)  
**Step 3** |  Align the SuperCap module with its slot on the module and seat the module into the slot.  |  **Caution** |  Make sure not to pinch the ribbon cable while inserting the SuperCap module into the slot.   
---|---  
![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309011.jpg)

When the SuperCap is securely seated in the slot, the module does not rock or twist.   
  
**Step 4** |  After the SuperCap module is seated, reconnect the ribbon cable to the board.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309012.jpg)  
  
* * *

## Replacing CPUs and Heatsinks

This topic describes the configuration rules and procedure for replacing CPUs and heatsinks.

  * CPU Configuration Rules
  * Tools Required for CPU Replacement
  * CPU and Heatsink Alignment Features
  * Removing the CPU and Heatsink
  * Installing the CPU and Heatsink


### CPU Configuration Rules

This server has two CPU sockets on the motherboard. Each CPU supports 8 DIMM channels (16 DIMM slots). See Memory Population Guidelines. 

  * Fourth and Fifth Generation Intel Xeon Scalable Processors have the same physical dimensions, CPU alignment features, and use the same heatsinks, so field-replacement procedures are the same regardless of which generation of CPU is installed. 

  * The server can operate with either one or two CPUs installed. In a dual-CPU configuration, both CPUs must be identical.

  * The minimum configuration is at least CPU 1 installed. 

The following restrictions apply when using a dual-CPU configuration:

  * Any unused CPU socket must have the protective dust cover from the factory installed.

  * The maximum number of DIMMs is 32 (installed in slots A through H).

  * Mezzanine slots 1 and 2 are unavailable.


### Tools Required for CPU Replacement

You need the following tools and equipment for this procedure:

  * T-30 Torx driver—Supplied with replacement CPU. 

  * #1 flat-head screwdriver—Supplied with replacement CPU.

  * CPU assembly tool for M8 processors—Supplied with replacement CPU. The assembly tool can be ordered separately as Cisco PID UCS-CPUATI-6=. 

  * Heatsink cleaning kit—Supplied with replacement CPU. Can be ordered separately for the front or rear heatsink:

  * Front heatsink kit: UCSX-M8I-HS-F

  * Rear heatsink kit: UCSX-M8I-HS-R

One cleaning kit can clean up to four CPUs.

  * Thermal interface material (TIM)—Syringe supplied with replacement CPU. Use only if you are reusing your existing heatsink (new heatsinks have pre-applied TIM). Can be ordered separately as Cisco PID UCS-CPU-TIM=. 

One TIM kit covers one CPU.


### CPU and Heatsink Alignment Features

For installation and field-replacement procedures, the heatsink, the CPU carrier, and the CPU motherboard socket must all be properly aligned to the pin 1 location. 

Each of these parts has a visual indicator to ensure they are properly aligned. 

#### Heatsink Alignment Feature

Each heatsink has a yellow triangle labeled on one corner. The tip of the triangle points to the pin 1 location on the heatsink. Use the triangle to align the heatsink with the pin 1 location on other parts, such as the CPU carrier and CPU socket. 

![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472292.png)

Also note that the orientation of each CPU is different between CPU socket 1 and CPU socket 2, as indicated by the different position of the alignment feature on each heatsink. 

#### CPU Carrier Alignment Feature

Each CPU carrier has a triangular cutout in the carrier's plastic. The tip of the triangle points to the pin1 location on the carrier. Use the triangular cutout to align the CPU carrier with the pin 1 location on other parts, such as the heatsink and the CPU socket. The X210c M8 compute node supports two CPU carriers, E2A and E2B. Carrier E2A is shown in ther illustration in this guide. 

![](/c/dam/en/us/td/i/400001-500000/480001-490000/488001-489000/488777.jpg)

![](/c/dam/en/us/td/i/400001-500000/480001-490000/488001-489000/488776.jpg)

#### CPU Socket Alignment Feature

Each CPU socket has a triangle on the rectangular bolster plate around the CPU socket. The tip of the triangle points to the pin 1 location on the motherboard socket. Use the triangular cutout to align the CPU carrier with the pin 1 location on other parts, such as the heatsink and the CPU carrier. 

![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472294.jpg)

### Removing the CPU and Heatsink

Use the following procedure to remove an installed CPU and heatsink from the blade server. With this procedure, you will remove the CPU from the motherboard, disassemble individual components, then place the CPU and heatsink into the fixture that came with the CPU. 

Sixth Generation Intel Xeon Scalable Processors have the same dimensions, CPU alignment features, and use the same heatsinks. Replacement procedures are the same regardless of which processor generation is installed, and the same heatsink(s) can be reused wherever possible. 

#### Procedure

* * *

**Step 1** |  Detach the CPU and heatsink (the CPU assembly) from the CPU socket.

  1. Using the T30 Torx driver, loosen all the securing nuts in a diagonal pattern, you can start at any nut.  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472432.jpg)
  2. Using your fingers, push the rotating wires towards each other to move them to the unlocked position. |  **Caution** |  Make sure that the rotating wires are as far inward as possible. When fully unlocked, the bottom of the rotating wire disengages and allows the removal of the CPU assembly. If the rotating wires are not fully in the unlocked position, you can feel resistance when attempting to remove the CPU assembly.   
---|---  
  
![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472433.jpg)


  
**Step 2** |  Remove the CPU assembly from the motherboard.

  1. Grasp the heatsink along the edge of the carrier and lift the CPU assembly off of the motherboard.  |  **Caution** |  Do not grasp the heatsink by its fins. Only handle the carrier! Also, if you feel any resistance when lifting the CPU assembly, verify that the rotating wires are completely in the unlocked position.   
---|---  
  
![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472438.jpg)

  2. Put the CPU assembly on a rubberized mat or other ESD-safe work surface.

When placing the CPU on the work surface, the heatsink label should be facing up. Do not rotate the CPU assembly upside down.

  3. Ensure that the CPU assembly sits level on the work surface. 


  
**Step 3** |  Attach a CPU dust cover to the CPU socket.

  1. Align the posts on the CPU bolstering plate with the cutouts at the corners of the dust cover.
  2. Lower the dust cover and simultaneously press down on the edges until it snaps into place over the CPU socket. |  **Caution** |  Do not press down in the center of the dust cover!  
---|---  
  
![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472440.jpg)


  
**Step 4** |  Detach the heatsink from the CPU carrier by disengaging the CPU clips and using the TIM breaker.

  1. Turn the CPU assembly upside down, so that the heatsink is pointing down.  This step enables access to the CPU securing clips.
  2. Gently rotate up on the outer edge of the CPU carrier (1 in the following illustration) at the edge opposite the TIM breaker.  |  **Caution** |  Be careful when flexing the CPU carrier! If you apply too much force you can damage the CPU carrier. Flex the carrier only enough to release the CPU clips. Make sure to watch the clips while performing this step so that you can see when they disengage from the CPU carrier.   
---|---  
  3. Gently lift the TIM breaker (2 ) in a 90-degree upward arc to partially disengage the CPU clips on this end of the CPU carrier.

  4. Lower the TIM breaker into the u-shaped securing clip to allow easier access to the CPU carrier. 

**Note** |  Make sure that the TIM breaker is completely seated in the securing clip.  
---|---  
  5. Gently pull up on the outer edge of the CPU carrier nearest to the TIM breaker so that you can disengage the pair of CPU clips (3 in the following illustration). 

  6. Grasp the CPU carrier along the short edges and lift it straight up to remove it from the heatsink.

![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472728.jpg)


  
**Step 5** |  Transfer the CPU and carrier to the fixture.

  1. When all the CPU clips are disengaged, grasp the carrier and lift it and the CPU to detach them from the heatsink. |  **Caution** |  Handle the carrier only! Do not touch the CPU gold contacts. Do not separate the CPU from the carrier.  
---|---  
**Note** |  If the carrier and CPU do not lift off of the heatsink, attempt to disengage the CPU clips again.  
---|---  
  2. Use the provided cleaning kit (UCSX-HSCK) to remove all of the thermal interface barrier (thermal grease) from the CPU, CPU carrier, and heatsink. 

**Important** |  Make sure to use only the Cisco-provided cleaning kit, and make sure that no thermal grease is left on any surfaces, corners, or crevices. The CPU, CPU carrier, and heatsink must be completely clean.   
---|---  
  3. Flip the CPU and carrier right-side up so that the word PRESS is visible. 

  4. Align the posts on the fixture, and the pin 1 locations on the CPU carrier and the fixture. 

The pin 1 location on the CPU is indicated by the triangle, and the pin 1 location on the fixture is the angled corner. 

  5. Lower the CPU and carrier onto the fixture. 

![](/c/dam/en/us/td/i/400001-500000/480001-490000/488001-489000/488767.jpg)


  
  
* * *

#### What to do next

  * If you will not be installing a CPU, verify that a CPU socket cover is installed. This option is valid only for CPU socket 2 because CPU socket 1 must always be populated in a runtime deployment. 


### Installing the CPU and Heatsink

Use this procedure to install a CPU if you have removed one, or if you are installing a CPU in an empty CPU socket. 

If you are installing or adding a new CPU to a single-CPU compute node, make sure that the new CPU is identical to the existing CPU. If you are replacing a CPU, reuse the existing heatsink. 

#### Before you begin

The CPU socket, CPU carrier, and heatsink must be correctly aligned to be installed. For information about the alignment features of these parts, see CPU and Heatsink Alignment Features. 

#### Procedure

* * *

**Step 1** |  Remove the CPU socket dust cover on the server motherboard. 

  1. Push the two vertical tabs inward to disengage the dust cover.
  2. While holding the tabs in, lift the dust cover up to remove it.  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472441.jpg)
  3. Store the dust cover for future use.  |  **Caution** |  Do not leave an empty CPU socket uncovered. If a CPU socket does not contain a CPU, you must install a CPU dust cover.  
---|---  

  
**Step 2** |  Grasp the CPU carrier on the edges, lift it out of the tray, and place the CPU carrier on an ESD-safe work surface.![](/c/dam/en/us/td/i/400001-500000/480001-490000/488001-489000/488766.jpg)  
**Step 3** |  Apply new TIM. |  **Note** |  The heatsink must have new TIM on the heatsink-to-CPU surface to ensure proper cooling and performance.   
---|---  
  
  * If you are installing a new heatsink, it is shipped with a pre-applied pad of TIM. Go to step 4.

  * If you are reusing a heatsink, you must remove the old TIM from the heatsink and then apply new TIM to the CPU surface from the supplied syringe. Continue with step **a** below. 


  1. Apply the Bottle #1 cleaning solution that is included with the heatsink cleaning kit (UCSX-HSCK=), as well as the spare CPU package, to the old TIM on the heatsink and let it soak for a least 15 seconds. 

  2. Wipe all of the TIM off the heatsink using the soft cloth that is included with the heatsink cleaning kit. Be careful to avoid scratching the heatsink surface. 

  3. Completely clean the bottom surface of the heatsink using Bottle #2 to prepare the heatsink for installation.

  4. Using the syringe of TIM provided with the new CPU, apply 1.5 cubic centimeters (1.5 ml) of thermal interface material to the top of the CPU. Use the pattern shown in the following figure to ensure even coverage. 

Figure 2. Thermal Interface Material Application Pattern  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/306001-307000/306154.jpg) **Caution** |  Use only the correct heatsink for your CPU. CPU 1 uses heatsink UCSX-M8I-HS-F and CPU 2 uses heatsink UCSX-M8I-HS-R.  
---|---  

  
**Step 4** |  Attach the heatsink to the CPU and carrier. 

  1. Using your finger, push the retaining wires to the unlocked position to prevent obstruction when seating the CPU.
  2. Grasp the heatsink by the short edges.
  3. Align the pin 1 location of the heatsink with the pin 1 location on the CPU carrier, then lower the heatsink onto the CPU carrier.  The heatsink is correctly oriented when the embossed triangle points to the CPU pin 1 location. 

  
**Step 5** |  Install the CPU assembly onto the CPU motherboard socket. 

  1. Push the rotating wires inward to the unlocked position so that they do not obstruct installation. 
  2. Grasp the heatsink by the carrier, align the pin 1 location on the heatsink with the pin 1 location on the CPU socket, then seat the heatsink onto the CPU socket.  The heatsink is correctly oriented when the embossed triangle points to the CPU pin 1 location, as shown.  |  **Caution** |  Make sure the rotating wires are in the unlocked position so that the feet of the wires do not impede installing the heatsink.  
---|---  
  
![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472439.png)


  
**Step 6** |  Secure the CPU and heatsink to the socket.

  1. Push the rotating wires away from each other to lock the CPU assembly into the CPU socket. |  **Caution** |  Make sure that you close the rotating wires completely before using the Torx driver to tighten the securing nuts.   
---|---  
  2. Set the T30 Torx driver to 12 in-lb of torque and tighten the 4 securing nuts to secure the CPU to the motherboard. You can start with any nut, but make sure to tighten the securing nuts in a diagonal pattern. 

![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472437.png)


  
  
* * *

## Replacing Memory DIMMs

The DIMMs that this compute node supports are updated frequently. A list of supported and available DIMMs is in _Cisco UCS X210c M8 Specification Sheet_ or the _Cisco UCS Intel M8 Memory Guide_. 

Do not use any DIMMs other than those listed in the specification sheet. Doing so may irreparably damage the compute node and result in down time. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The maximum memory configuration for the compute node is 32 256 GB DDR5 DIMMs.

  * When the compute node is configured with 256 GB DDR5 DIMMs, the compute node's supported operating temperature is 50° F to 89.6° F (10° C to 32 ° C).  When this operating range is exceeded, the compute node can throttle down in an attempt to cool the compute node. If throttling does not sufficiently cool the compute node, the node shuts down. 
  * When the compute node is configured without 256 GB DDR5 DIMMs, the compute node's supported operating temperature is 50° F to 95° F (10° C to 35 ° C). 


* * *  
  
---|---  
  
  * Memory Population Guidelines
  * Installing a DIMM or DIMM Blank


### Memory Population Guidelines

For detailed information about supported memory, memory population guidelines, and configuration and performance, download the PDF of the [Cisco UCS/UCSX M8 Memory Guide](https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/ucs-intel-m8-memory-guide.pdf). 

#### DIMM Identification

To assist with identification, each DIMM slot displays its memory processor and slot ID on the motherboard. The entire enumeration string consists of <Processor-ID>_ <channel> <DIMM slot-ID>. 

For example, P1 A1 indicates CPU 1, DIMM channel A, Slot 1. 

Also, you can further identify which DIMM slot connects to which CPU by dividing the blade in half vertically. With the compute node front panel facing left: 

  * All DIMM slots on the left, above and below CPU 1 are connected to CPU 1

  * All DIMM slots on the right, above and below CPU 2 are connected to CPU 2. 


For each CPU, each set of 16 DIMMs is arranged into 8 channels, where each channel has two DIMMs. Each DIMM slot is numbered 1 or 2, and each DIMM slot 1 is blue and each DIMM slot 2 is black. Each channel is identified by two pairs of letters and numbers where the first pair indicates the processor, and the second pair indicates the memory channel and slot in the channel. 

  * Each DIMM is assigned to a CPU, either CPU 1 (P1) or CPU 2 (P2). 

  * Each CPU has memory channels A through H. 

  * Each memory channel has two slots 1 and 2. 

  * DIMM slot identifiers for CPU1 are P1 A1, P1 A2, P1 B1, P1 B2, P1 C1, P1 C2, P1 D1, P1 D2, P1 E1, P1 E2, P1 F1, P1 F2, P1 G1, P1 G2, P1 H1, and P1 H2. 

  * DIMM slot identifiers for CPU 2 are P2 A1, P2 A2, P2 B1, P2 B2, P2 C1, P2 C2, P2 D1, P2 D2, P2 E1, P2 E2, P2 F1, P2 F2, P2 G1, P2 G2, P2 H1, and P2 H2. 


The following illustration shows the memory slot and channel IDs. 

  
![](/c/dam/en/us/td/i/400001-500000/480001-490000/488001-489000/488768.jpg)  


#### Memory Population Order

Memory slots are color coded, blue and black. The color-coded channel population order is blue slots first, then black.

For optimal performance, populate DIMMs in the order shown in the following table, depending on the number of CPUs and the number of DIMMs per CPU. If your server has two CPUs, balance DIMMs evenly across the two CPUs as shown in the table. 

Be aware of the following DIMM population rules:

  * There should be at least one DDR5 DIMM per socket. 

If only one DIMM is populated in a channel, then populate it in the slot furthest away from CPU of that channel

Always populate DIMMs with a higher electrical loading in DIMM0 followed by DIMM1. 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The table below lists recommended configurations. Using 3, 5, 7, 9, 10, 11, or 13-15 DIMMs per CPU is not recommended. Other configurations results in reduced performance. 

* * *  
  
---|---  
  
The following table shows the memory population order for DDR5 DIMMs.

Table 1. DIMMs Population Order **Number of DDR5 DIMMs per CPU (Recommended Configurations)** |  **Populate CPU 1 Slot** |  **Populate CPU2 Slots**  
---|---|---  
**P1 Blue #1 Slots** **P1 slot-ID** |  **P1 Black #2 Slots** ****P1_slot-ID**** |  **P2 Blue #1 Slots** ****P2 slot-ID**** |  **P2 Black #2 Slots** ******P2 slot-ID******  
1 |  A1 |  - |  A1 |  -  
4 | A1, C1, E1, G1 |  - | A1, C1, E1, G1 |  -  
8 |  A1, B1, C1, D1, E1, F1, G1, H1 |  - |  A1, B1, C1, D1, E1, F1, G1, H1 | -  
12 |  A1, B1, C1, D1, E1, F1,G1, H1 |  A2, C2, E2, G2 |  A1, B1, C1, D1, E1, F1,G1, H1 |  A2, C2, E2, G2  
16 |  All populated (A1 through H1) |  All populated (A2 through H2) |  All populated (A1 through H1) |  All populated (A2 through H2)  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For configurations with 1, 2, 4, 6 and 8 DIMMs, install higher capacity followed by lower capacity DIMMs in alternating fashion. For example, the 4 DIMMs configuration is installed with 64GB on A1, E1 on both CPUs and 16GB on C1, G1 on both CPUs.  For configurations with 12 and 16 DIMMs, install all higher capacity DIMMs in blue slots and all lower capacity DIMMs in black slots. 

* * *  
  
---|---  
  
#### DIMM Slot Keying Consideration

DIMM slots that connect to each CPU socket are oriented 180 degrees from each other. So, when you compare the DIMM slots for CPU 1 and the DIMM slots for CPU 2, the DIMMs do not install the same way. Instead, when you install DIMM attached to both CPUs, the DIMM orientation must change 180 degrees. 

To facilitate installation, DIMMs are keyed to ensure correct installation. When you install a DIMM, always make sure that the key in the DIMM slot lines up with the notch in the DIMM. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

If you feel resistance while seating a DIMM into its socket, do not force the DIMM or you risk damaging the DIMM or the slot. Check the keying on the slot and verify it against the keying on the bottom of the DIMM. When the slot's key and the DIMM's notch are aligned, reinstall the DIMM. 

* * *  
  
---|---  
  
### Installing a DIMM or DIMM Blank

To install a DIMM or a DIMM blank (UCS-DDR5-BLK=) into a slot on the compute node, follow these steps:

#### Procedure

* * *

**Step 1** |  Open both DIMM connector latches.  
---|---  
**Step 2** |  Press evenly on both ends of the DIMM until it clicks into place in its slot. |  **Note** |  Ensure that the notch in the DIMM aligns with the slot. If the notch is misaligned, it is possible to damage the DIMM, the slot, or both.   
---|---  
**Step 3** |  Press the DIMM connector latches inward slightly to seat them fully.  
**Step 4** |  Populate all slots with a DIMM or DIMM blank. A slot cannot be empty. Figure 3. Installing Memory ![](/c/dam/en/us/td/i/300001-400000/300001-310000/306001-307000/306040.jpg)  
  
* * *

## Servicing the mLOM

The Cisco UCS X210c M8 Compute Node supports a modular LOM (mLOM) card to provide additional rear-panel connectivity. The mLOM socket is on the rear corner of the motherboard. 

The mLOM socket provides a Gen-4 x16 PCIe lane. The socket remains powered when the compute node is in 12 V standby power mode, and it supports the network communications services interface (NCSI) protocol. 

The following mLOM cards are supported on the compute node.

Table 2. Supported mLOM VICs on Cisco UCS X210c M8 UCSX-ML-V5Q50G-D |  Cisco UCS Virtual Interface Card (VIC) 15420, Quad-Port 25G  
---|---  
UCSX-MLV5D200GV2D |  Cisco UCS Vitual Interface Card (VIC) 15230, Dual-Port 40/100/200G mLOM  
  
To service the mLOM card, use the following procedures:

  * Removing the mLOM

  * Installing an mLOM Card


  * Removing the mLOM
  * Installing an mLOM Card


### Removing the mLOM

The compute node supports an mLOM in the rear mezzanine slot. Use this procedure to remove an mLOM.

#### Procedure

* * *

**Step 1** |  Remove the compute node.

  1. Shut down and remove power from the compute node.
  2. Remove the compute node from the chassis. You might have to detach cables from the rear panel to provide clearance. 
  3. Remove the top cover from the compute node. See Removing a Compute Node Cover. 

  
---|---  
**Step 2** |  If the compute node has a UCS VIC 15000 Series Bridge Card, remove the card.  See Removing the Bridge Card.   
**Step 3** |  Remove the MLOM.

  1. Using a #2 Phillips head screwdriver, loosen the two captive thumbscrews.
  2. Lift the MLOM off of its socket.  You might need to gently rock the mLOM card while lifting it to disengage it from the socket. ![](/c/dam/en/us/td/i/400001-500000/480001-490000/488001-489000/488764.jpg)

  
  
* * *

#### What to do next

After completing service, reinstall the VIC. See Installing a Rear Mezzanine Card in Addition to the mLOM VIC. 

### Installing an mLOM Card

Use this task to install an mLOM onto the compute node.

#### Before you begin

If the compute node is not already removed from the chassis, power it down and remove it now. You might need to disconnect cables to remove the compute node. 

Gather a torque screwdriver. 

#### Procedure

* * *

**Step 1** |  Remove the top cover. See Removing a Compute Node Cover.   
---|---  
**Step 2** |  Orient the mLOM card so that the socket is facing down.   
**Step 3** |  Align the mLOM card with the motherboard socket so that the bridge connector is facing inward. ![](/c/dam/en/us/td/i/400001-500000/480001-490000/488001-489000/488770.jpg)  
**Step 4** |  Keeping the card level, lower it and press firmly to seat the card into the socket.  
**Step 5** |  Using a #2 Phillips torque screwdriver, tighten the captive thumbscrews to 4 in-lb of torque to secure the card.  
**Step 6** |  If your compute node has a bridge card (Cisco UCS VIC 15000 Series Bridge), reattach the bridge card.  See Installing a Bridge Card.   
**Step 7** |  Replace the top cover of the compute node.  
**Step 8** |  Reinsert the compute node into the chassis. replace cables, and then power on the compute node by pressing the Power button.  
  
* * *

## Servicing the VIC

The Cisco UCS X210c M8 Compute Node supports a virtual interface card (VIC) in the rear mezzanine slot. The VIC can be either half-slot or full-slot in size. 

The following VICs are supported on the compute node.

Table 3. Supported VICs UCSX-ME-V5Q50G-D |  Cisco UCS Virtual Interface Card (VIC) 15422, Quad-Port 25G  
---|---  
UCSX-ML-V5D200GV2 |  Cisco UCS Virtual Interface Card (VIC) 15420, Quad-Port 25G  
UCSX-MLV5D200GV2D |  Cisco UCS Virtual Interface Card (VIC) 15230, Dual-Port 100G  
UCSX-V4-PCIME-D |  UCS PCI Mezz card for X-Fabric Connectivity  
  
  * Cisco Virtual Interface Card (VIC) Considerations
  * Removing a Rear Mezzanine
  * Installing a Rear Mezzanine Card in Addition to the mLOM VIC


### Cisco Virtual Interface Card (VIC) Considerations

This section describes VIC card support and special considerations for this compute node.

  * A blade with only one mezzanine card is an unsupported configuration. With this configuration, blade discovery does not occur through Cisco UCS management software. No error is displayed. 


### Removing a Rear Mezzanine

The compute node supports a Rear Mezzanine Card in the rear of the compute node. Use this procedure to remove the Rear Mezzanine Card. 

#### Procedure

* * *

**Step 1** |  Remove the compute node.

  1. Decommission the compute node by using Cisco UCS management software. 
  2. Remove the compute node from the chassis. You might have to detach cables from the rear panel to provide clearance. 
  3. Remove the top cover from the compute node. See Removing a Compute Node Cover. 

  
---|---  
**Step 2** |  If the compute node has a UCS VIC 15000 Series Bridge Card, remove the card.  See Removing the Bridge Card.   
**Step 3** |  Remove the Rear Mezzanine.

  1. Using a #2 Phillips head screwdriver, loosen the captive thumbscrews.
  2. Lift the VIC off of its socket.  You might need to gently rock the Rear Mezzanine card while lifting it to disengage it from the socket. ![](/c/dam/en/us/td/i/400001-500000/470001-480000/476001-477000/476302.jpg)

  
  
* * *

### Installing a Rear Mezzanine Card in Addition to the mLOM VIC

The compute node has a rear mezzanine slot which can accept a virtual interface card (VIC) unless the compute node has a full size mLOM. In the case of a separate mLOM and VIC, another component (the UCS VIC 15000 Series Bridge is required to provide data connectivity between the mLOM and VIC. See Installing a Bridge Card. 

Use this task to install a VIC in the rear mezzanine slot. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The VIC installs upside down so that the connectors meet with the sockets on the compute node. 

* * *  
  
---|---  
  
#### Before you begin

Gather a torque screwdriver.

#### Procedure

* * *

**Step 1** |  Orient the VIC with the captive screws facing up and the connectors facing down.   
---|---  
**Step 2** |  Align the VIC so that the captive screws line up with their threaded standoffs, and the connector for the bridge card is facing inward.   
**Step 3** |  Holding the VIC level, lower it and press firmly to seat the connectors into the sockets.  ![](/c/dam/en/us/td/i/400001-500000/480001-490000/488001-489000/488769.jpg)  
**Step 4** |  Using a #2 Phillips torque screwdriver, tighten the captive screws to 4 in-lb of torque to secure the VIC to the compute node.  
  
* * *

#### What to do next

  * If the mLOM card is already installed, install a bridge card. Go to Installing a Bridge Card. 

  * If not, install the mLOM, which must be installed before the bridge card can be attached. Go to Installing an mLOM Card. 


## Servicing the Bridge Card

The compute node supports a Cisco UCS Series 15000 Bridge Card (UCSX-V5-BRIDGE-D) that spans between the rear mezzanine MLOM slot and the VIC slot. The bridge card connects the UCS X-Series Blade Server to the following Intelligent Fabric Modules (IFMs) in the server chassis that contains the compute nodes: 

  * Cisco UCS X9108 25G Intelligent Fabric Module (UCSX-I-9108-25G) 

  * Cisco UCS X9108 100G Intelligent Fabric Module (UCSX-I-9108-100G)


See the following topics:

  * Removing the Bridge Card

  * Installing a Bridge Card


  * Removing the Bridge Card
  * Installing a Bridge Card


### Removing the Bridge Card

Use the following procedure to remove the bridge card. 

#### Procedure

* * *

**Step 1** |  Remove the compute node.

  1. Shut down and remove power from the compute node.
  2. Remove the compute node from the chassis. You might have to detach cables from the rear panel to provide clearance. 
  3. Remove the top cover from the compute node. See Removing a Compute Node Cover. 

  
---|---  
**Step 2** |  Remove the bridge card from the motherboard. 

  1. Using a #2 Phillips screwdriver, loosen the two captive screws.
  2. Lift the bridge card off of the socket.  |  **Note** |  You might need to gently rock the bridge card to disconnect it.  
---|---  
  
![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472416.jpg)


  
  
* * *

#### What to do next

Choose the appropriate option:

  * Perform service on the MLOM. See Servicing the mLOM. 

  * Perform service on the VIC. See Servicing the VIC. 

  * Reinstall the bridge card. See .


### Installing a Bridge Card

The Cisco UCS VIC 14000 Series Bridge is a physical card that provides data connection between the mLOM and VIC. Use this procedure to install the bridge card. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The bridge card installs upside down so that the connectors meet with the sockets on the MLOM and VIC. 

* * *  
  
---|---  
  
#### Before you begin

To install the bridge card, the compute node must have an mLOM and a VIC installed. The bridge card ties these two cards together to enable communication between them. 

If these components are not already installed, install them now. See:

  * Installing a Rear Mezzanine Card in Addition to the mLOM VIC


#### Procedure

* * *

**Step 1** |  Orient the bridge card so that the Press Here to Install  text is facing you.   
---|---  
**Step 2** |  Align the bridge card so that the connectors line up with the sockets on the MLOM and VIC.  When the bridge card is correctly oriented, the hole in the part's sheet metal lines up with the alignment pin on the VIC.  
**Step 3** |  Keeping the bridge card level lower it onto the MLOM and VIC cards and press evenly on the part where the Press Here to Install  text is.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/308001-309000/308991.jpg)  
**Step 4** |  When the bridge card is correctly seated, use a #2 Phillips screwdriver to secure the captive screws. |  **Caution** |  Make sure the captive screws are snug, but do not overdrive them or you risk stripping the screw.   
---|---  
  
* * *

## Servicing the Trusted Platform Module (TPM)

The Trusted Platform Module (TPM) is a component that can securely store artifacts used to authenticate the compute node. These artifacts can include passwords, certificates, or encryption keys. A TPM can also be used to store platform measurements that help ensure that the platform remains trustworthy. Authentication (ensuring that the platform can prove that it is what it claims to be) and attestation (a process helping to prove that a platform is trustworthy and has not been breached) are necessary steps to ensure safer computing in all environments. It is a requirement for the Intel Trusted Execution Technology (TXT) security feature, which must be enabled in the BIOS settings for a compute node equipped with a TPM. 

The Cisco UCS X210c M8 Compute Node supports the Trusted Platform Module 2.0, which is FIPS140-2 compliant and CC EAL4+ certified (UCSX-TPM-002D= (or UCSX-TPM-002D-D). 

To install and enable the TPM, go to SEnabling the Trusted Platform Module. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Removing the TPM is supported only for recycling and e-waste purposes. Removing the TPM will destroy the part so that it cannot be reinstalled. 

* * *  
  
---|---  
  
  * Enabling the Trusted Platform Module


### Enabling the Trusted Platform Module

The Trusted Platform Module (TPM) is a component that can securely store artifacts used to authenticate the server. These artifacts can include passwords, certificates, or encryption keys. A TPM can also be used to store platform measurements that help ensure that the platform remains trustworthy. Authentication (ensuring that the platform can prove that it is what it claims to be) and attestation (a process helping to prove that a platform is trustworthy and has not been breached) are necessary steps to ensure safer computing in all environments. It is a requirement for the Intel Trusted Execution Technology (TXT) security feature, which must be enabled in the BIOS settings for a server equipped with a TPM. 

#### Procedure

* * *

**Step 1** |  Install the TPM hardware. 

  1. Decommission, power off, and remove the blade server from the chassis. 
  2. Remove the top cover from the server as described in Removing a Compute Node Cover
  3. Install the TPM to the TPM socket on the server motherboard and secure it using the one-way screw that is provided. See the figure below for the location of the TPM socket. 
  4. Return the blade server to the chassis and allow it to be automatically reacknowledged, reassociated, and recommissioned. 
  5. Continue with enabling TPM support in the server BIOS in the next step. 

![](/c/dam/en/us/td/i/400001-500000/480001-490000/488001-489000/488778.jpg)  
---|---  
**Step 2** |  Enable TPM Support in the BIOS. 

  1. In the Cisco UCS Manager Navigation pane, click the Servers tab. 
  2. On the Servers tab, expand Servers > Policies. 
  3. Expand the node for the organization where you want to configure the TPM. 
  4. Expand BIOS Policies and select the BIOS policy for which you want to configure the TPM. 
  5. In the Work pane, click the Advanced tab. 
  6. Click the Trusted Platform sub-tab. 
  7. To enable TPM support, click Enable or Platform Default. 
  8. Click Save Changes. 
  9. Continue with the next step. 

  
  
* * *

---

## Page 13: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x210c-m8/install/m-recycling-components.html

# Recycling Compute Node Components

This chapter contains the following topics:

## Compute Node Recycling Overview

This chapter documents the procedures to disassemble key compute node components for recycling and e-waste. When recycling your Cisco UCS hardware, always make sure to follow local e-waste and recycling regulations. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

**For Recyclers Only!** The procedures in this chapter are not standard field-service options. These procedures are for recyclers who will be reclaiming the electronics for proper disposal to comply with local eco design and e-waste regulations. 

* * *  
  
---|---  
  
To disassemble compute node component parts, see the following topics: 

  * Removing the Trusted Platform Module (TPM)

  * Recycling the Motherboard PCBA


## Removing the Trusted Platform Module (TPM)

The TPM module is attached to the printed circuit board assembly (PCBA). You must disconnect the TPM module from the PCBA before recycling the PCBA. The TPM module is secured to a threaded standoff by a tamper-resistant screw. If you do not have the correct tool for the screw, you can use a pair of pliers to remove the screw. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Removing the TPM destroys the part so that it cannot be reinstalled or reused!

* * *  
  
---|---  
  
### Before you begin

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

**For Recyclers Only!** This procedure is not a standard field-service option. This procedure is for recyclers who will be reclaiming the electronics for proper disposal to comply with local eco design and e-waste regulations. 

* * *  
  
---|---  
  
To remove the Trusted Platform Module (TPM), the following requirements must be met for the compute node:

  * It must be disconnected from facility power. 

  * It must be removed from the equipment rack. 

  * The top cover must be removed. If the top cover is not removed, see [Removing a Compute Node Cover](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_cbf2ee70-df1d-4095-b066-db7268a991b7). 


### Procedure

* * *

**Step 1** |  Locate the TPM module. ![](/c/dam/en/us/td/i/400001-500000/480001-490000/488001-489000/488771.jpg)  
---|---  
**Step 2** |  Using the pliers, grip the head of the screw and turn it counterclockwise until the screw releases.  
**Step 3** |  Remove the TPM module and dispose of it properly.  
  
* * *

### What to do next

Remove and dispose of the PCB Assembly. See Recycling the Motherboard PCBA. 

## Recycling the Component PCB Assemblies (PCBAs)

In addition to the main motherboard PCBA, some key components also contain PCBAs that need to be recycled. Always comply with your local regulations governing recycling and e-waste. 

Use the following procedures to recycle the appropriate components.

  * Recycling the Motherboard PCBA

  * Recycling the Front Mezzanine Module PCBA


  * Recycling the Motherboard PCBA
  * Recycling the Front Mezzanine Module PCBA
  * Recycling the Front Mezzanine GPU Module's PCBA


### Recycling the Motherboard PCBA

Each compute node has a PCBA that is connected to the compute node's faceplate and sheet metal tray. You must disconnect the PCBA from the faceplate and tray to recycle the PCBA. Each compute node is attached to the sheet metal tray be the following: 

  * Four M3 screws

  * Two hexagonal standoffs.


For this procedure you will need the following tools: 

  * Screwdrivers: #2 Phillips, one 6mm slotted, one T8, T10, and T30. 

  * Nut driver: One 6mm hex 


You will need to recycle the PCBA for each compute node.

#### Before you begin

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

**For Recyclers Only!** This procedure is not a standard field-service option. This procedure is for recyclers who will be reclaiming the electronics for proper disposal to comply with local eco design and e-waste regulations. 

* * *  
  
---|---  
  
To remove the printed circuit board assembly (PCBA), the following requirements must be met:

  * The compute node must be disconnected from facility power.

  * The compute node must be removed from the equipment rack.

  * The compute node's top cover must be removed. See [Removing a Compute Node Cover](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_cbf2ee70-df1d-4095-b066-db7268a991b7). 


#### Procedure

* * *

**Step 1** |  (Optional) If the CPUs and heat sinks are still installed, remove them. See [Removing the CPU and Heatsink](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_38f14d54-eda9-4b1d-b72c-39b2ef89c1f1).   
---|---  
**Step 2** |  (Optional) If the front mezzanine module is installed, remove it. See [Removing the Front Mezzanine Module](m-servicing-the-compute-node.html#Cisco_Task_in_List_GUI.dita_ae651cb7-9fa9-4e8c-a698-45ea0eee9ee9).   
**Step 3** |  (Optional) If the rear bridge card is installed, remove it.  See [Removing the Bridge Card](m-servicing-the-compute-node.html#removing-the-bridge-card).   
**Step 4** |  (Optional) If the rear mezzanine card is installed, use a #2 screwdriver to remove the four captive screws, then remove the card.  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472295.png)  
**Step 5** |  (Optional) If the MLOM VIC is installed, remove it. See [Removing the mLOM](m-servicing-the-compute-node.html#removing-the-mlom).   
**Step 6** |  Remove the M.2 module.  See [Removing the M.2 RAID Controller Module or NVMe Pass-Through Module](m-servicing-the-compute-node.html#removing-the-m.2-raid-controller-module).   
**Step 7** |  Remove the compute node's rear frame.

  1. Use the T8 screwdriver to remove the M3 bottom mounting screw on each exterior side of the compute node.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309229.jpg)
  2. Turn the compute node upside down and use the T10 screwdriver to remove the two M3 mounting screws on the bottom of the sheet metal.  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309230.jpg)
  3. Turn the compute node component side up and use the T10 screwdriver to remove the six M3 mounting screws at the rear of the compute node.  ![](/c/dam/en/us/td/i/400001-500000/480001-490000/488001-489000/488772.jpg)

  
**Step 8** |  If the TPM is installed, remove it.  See Removing the Trusted Platform Module (TPM).   
**Step 9** |  Disconnect the motherboard from the compute node's sheet metal. 

  1. Use the 6mm hex nut driver to remove the two standoffs. 
  2. Use the #2 Phillips screwdriver to remove the front mezzanine cage retaining screw, then remove the cage. 
  3. Use the T10 screwdriver to remove the four M3 screws.  ![](/c/dam/en/us/td/i/400001-500000/480001-490000/488001-489000/488775.jpg) |  Red circles (![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309210.jpg))  |  6 mm standoffs (2)  
---|---  
Blue circles (![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309209.jpg))  |  M3 screws (4)  
Purple circle (![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309212.jpg))  |  Front mezzanine cage retaining screw (1)  

  
**Step 10** |  Recycle the sheet metal and motherboard in compliance with your local recycling and e-waste regulations.   
  
* * *

### Recycling the Front Mezzanine Module PCBA

The compute node's front mezzanine module contains one PCBA, which sits horizontally and connects the drive backplane to the main motherboard. The PCBA is attached to the front mezzanine module's sheetmetal by four T8 screws. 

You must disconnect the PCBA from the sheetmetal before recycling the PCBA. 

#### Before you begin

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

**For Recyclers Only!** This procedure is not a standard field-service option. This procedure is for recyclers who will be reclaiming the electronics for proper disposal to comply with local eco design and e-waste regulations. 

* * *  
  
---|---  
  
To remove the printed circuit board assembly (PCBA), the following requirements must be met:

  * The compute node must be removed from the chassis.

  * The compute node's top cover must be removed.


Gather the following tools: 

  * A T8 Torx screwdriver

  * A #2 Phillips screwdriver


#### Procedure

* * *

**Step 1** |  Remove the front mezzanine module from the compute node.

  1. Place the front mezzanine module upside down on a rubberized mat or other ESD-safe work surface. 

  
---|---  
**Step 2** |  Disconnect the drive backplane.

  1. Using a #2 Phillips screwdriver, remove the two screws on the drive backplane. ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472720.jpg)
  2. Grasp the drive backplane and lift it off of the sheetmetal frame. ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472721.jpg)

  
**Step 3** |  Disconnect the PCBA from the sheetmetal frame.

  1. Locate the PCBA and use a T8 Torx screwdriver to remove the four screws that secure the PCBA to the sheetmetal frame.  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472723.jpg)
  2. Grasp the PCBA and detach it from the front mezzanine module. ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472724.jpg)

  
**Step 4** |  Dispose of the PCBA properly in accordance with your local recycling and e-waste laws.  
  
* * *

### Recycling the Front Mezzanine GPU Module's PCBA

The compute node supports an optional front mezzanine module configuration of one or two Cisco L4-MEZZ GPUs. The X10c Front Mezzanine GPU Module, UCSX-X10C-GPUFM, has a PCBA that must be recycled. 

For information about recycling the PCBA in the X10c Front Mezzanine GPU Module, go to [Recycling the Front Mezzanine GPU Module PCBA](https://www-author3.cisco.com/content/en/us/td/docs/unified_computing/ucs/x/hw/x10c-gpu-module/install/cisco-ucs-x10c-front-mezzanine-gpu-install-guide/m-servicing-gpu-module.html#Cisco_Task_in_List_GUI.dita_69d5ccb6-d922-428e-90b2-62019008eff7). 

---
