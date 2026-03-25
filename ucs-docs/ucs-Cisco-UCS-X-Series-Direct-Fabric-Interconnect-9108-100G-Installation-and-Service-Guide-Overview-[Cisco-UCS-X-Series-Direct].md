# Cisco UCS X-Series Direct Fabric Interconnect 9108 100G Installation and Service Guide

| | |
|---|---|
| **URL Title** | Cisco UCS X-Series Direct Fabric Interconnect 9108 100G Installation and Service Guide |
| **URL** | https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x-series-direct/hw/s9108/install/ucs-x-series-direct-9108-100g/m-overview.html |
| **Long URL** |  |
| **HTML Title** | Cisco UCS X-Series Direct Fabric Interconnect 9108 100G Installation and Service Guide - Overview [Cisco UCS X-Series Direct] |
| **Source file** | `ucs-docs-raw/html/m-overview.html` |
| **File type** | HTML |
| **Fetched on** | 2026-03-25 11:33:17 |

---

## Page 1: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x-series-direct/hw/s9108/install/ucs-x-series-direct-9108-100g/m-overview.html

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

---

## Page 2: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x-series-direct/hw/s9108/install/ucs-x-series-direct-9108-100g/m-preface.html

## Bias-Free Documentation

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The documentation set for this product strives to use bias-free language. For purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on standards documentation, or language that is used by a referenced third-party product. 

* * *  
  
---|---

---

## Page 3: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x-series-direct/hw/s9108/install/ucs-x-series-direct-9108-100g/m-installing.html

## Installation Guidelines and Limitations  
  
Be aware of the following limitations when installing the Cisco UCS X-Series Direct Fabric Interconnect 9108 100G into the Cisco UCS X9508 chassis: 

  * The fabric interconnects are always deployed in pairs. You cannot install and operate the fabric interconnect system with only one installed in the chassis. 

  * Fabric interconnect can either be installed in the chassis or not. If no fabric interconnect is used in the Cisco UCS X9508 chassis, then you must install a pair of Cisco UCS Intelligent Fabric Modules (IFMs). The chassis cannot be used or operated without any fabric interconnects (FIs) or IFMs in place. 


---

## Page 4: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x-series-direct/hw/s9108/install/ucs-x-series-direct-9108-100g/m-connecting.html

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

---

## Page 5: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x-series-direct/hw/s9108/install/ucs-x-series-direct-9108-100g/m-servicing.html

## Installing and Removing the Top Cover  
  
The top cover for the Cisco UCS X-Series Direct 9108 100G Fabric Interconnect can be removed to allow access to internal components, some of which are field-replaceable. The top cover has a release button on one side and an emboss on the other side. 

  * the release button unlocks the cover so that it can be removed from the fabric interconnect

  * the emboss provides a second fingerhold so that you can apply equal force to both sides of the cover. 


![](/c/dam/en/us/td/i/400001-500000/480001-490000/481001-482000/481626.jpg) **1** |  Release Button |  **2** |  Emboss, which can be used as a fingerhold  
---|---|---|---  
  
To remove and install the top cover, use the following procedures:

  * Removing the Top Cover

  * Installing the Top Cover


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

---

## Page 6: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x-series-direct/hw/s9108/install/ucs-x-series-direct-9108-100g/m-recycling.html

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

## Physical Specifications for the Fabric Interconnect

The following table shows the physical specifications for the Cisco UCS X-Series Direct 9108 100G Fabric Interconnect.

Specification  |  Value   
---|---  
Height  |  1.71 in. (43.5 mm)  
Width  |  14.92 in (379 mm)  
Depth  |  10.15 in (257.8 mm)  
Weight  |  8.5 lbs. (3.86 kg)

---

## Page 8: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x-series-direct/hw/s9108/install/ucs-x-series-direct-9108-100g/m-obtaining-hardware.html

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

  * [Preface](/c/en/us/td/docs/unified_computing/ucs/x-series-direct/hw/s9108/install/ucs-x-series-direct-9108-100g/m-preface.html)  
  * [Overview](/c/en/us/td/docs/unified_computing/ucs/x-series-direct/hw/s9108/install/ucs-x-series-direct-9108-100g/m-overview.html)
  * [Installing the Fabric Interconnect](/c/en/us/td/docs/unified_computing/ucs/x-series-direct/hw/s9108/install/ucs-x-series-direct-9108-100g/m-installing.html)
  * [Connecting the Fabric Interconnect](/c/en/us/td/docs/unified_computing/ucs/x-series-direct/hw/s9108/install/ucs-x-series-direct-9108-100g/m-connecting.html)
  * [Servicing the Fabric Interconnect](/c/en/us/td/docs/unified_computing/ucs/x-series-direct/hw/s9108/install/ucs-x-series-direct-9108-100g/m-servicing.html)
  * [Recycling Fabric Interconnect Components](/c/en/us/td/docs/unified_computing/ucs/x-series-direct/hw/s9108/install/ucs-x-series-direct-9108-100g/m-recycling.html)
  * [Technical Specifications](/c/en/us/td/docs/unified_computing/ucs/x-series-direct/hw/s9108/install/ucs-x-series-direct-9108-100g/m-specifications.html)
  * [Obtaining Hardware](/c/en/us/td/docs/unified_computing/ucs/x-series-direct/hw/s9108/install/ucs-x-series-direct-9108-100g/m-obtaining-hardware.html)
  * [Index](/c/en/us/td/docs/unified_computing/ucs/x-series-direct/hw/s9108/install/ucs-x-series-direct-9108-100g/ucs-x-series-direct-9108-100g_index.html)


---
