# IFMS Installation Instructions - Cisco

| | |
|---|---|
| **URL Title** | IFMS Installation Instructions - Cisco |
| **URL** | https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x9508/install/b-ucs-x9508-install/m_ifms-installation-instructions.html |
| **Long URL** |  |
| **HTML Title** | Cisco UCS X9508 Server Chassis Installation Guide - Intelligent Fabric Module (IFM) Field Replaceable Unit Instructions [Cisco UCS X-Series Modular System] |
| **Source file** | `ucs-docs-raw/html/m_ifms-installation-instructions.html` |
| **File type** | HTML |
| **Fetched on** | 2026-06-24 11:18:22 |

---

## Page 1: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x9508/install/b-ucs-x9508-install/m_ifms-installation-instructions.html

## Intelligent Fabric Module (IFM) Field Replaceable Unit Instructions

There are two IFM options for the UCS X9508 Server Chassis:

  * Cisco UCS 9108 25G Intelligent Fabric Module

  * Cisco UCS 9108 100G Fabric Module


Refer to the relevant section below for the specific IFM installed in your system.

Figure 1. Cisco UCS 9108 25G IFMs (UCSX-I-9108-25G) Replacement Instructions  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/473001-474000/473982.jpg)

Figure 2. Cisco UCS 9108 100G IFMs (UCSX-I-9108-100G) Replacement Instructions  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/473001-474000/473981.jpg)

---

## Page 2: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x9508/install/b-ucs-x9508-install/m-preface.html

## Bias-Free Documentation

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The documentation set for this product strives to use bias-free language. For purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on standards documentation, or language that is used by a referenced third-party product. 

* * *  
  
---|---

---

## Page 3: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x9508/install/b-ucs-x9508-install/m-ucsx-9508-chassis-overview.html

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

---

## Page 4: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x9508/install/b-ucs-x9508-install/m-installation.html

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

---

## Page 5: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x9508/install/b-ucs-x9508-install/m-installing-and-removing-components.html

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

---

## Page 6: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x9508/install/b-ucs-x9508-install/m-technical-specs.html

## KVM Cable  
  
The KVM cable (UCSX-C-DEBUGCBL) provides a connection into a Cisco UCS compute node, providing a DB-9 serial connector, a DB-15 connector, and a USB ports for a keyboard and mouse. With this cable you can create a direct connection to the operating system and the BIOS running on a compute node. 

Figure 1. KVM Cable for Compute Nodes    
![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309412.jpg)  
**1** |  Oculink Connector to compute node |  **2** |  DB-9 serial connector to host Console port  
---|---|---|---  
**3** |  USB connector to connect to single USB 3.0 port (keyboard or mouse) |  **4** |  DB-15 connector to connect to a host VGA monitor 

---

## Page 7: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x9508/install/b-ucs-x9508-install/m-ifm-afm-xfm-fru-replacement-instructions-labels.html

## Cisco UCS 9108 25G IFM Field Replaceable Unit Replacement Instructions  
  
The rear of the Cisco UCS X9508 can contain a pair of UCS 9108 Intelligent Fabric Modules (IFMs), which come in either 25G or 100G speeds. 

Refer to the following illustration for information about field-replacement options on the UCS 9108 25G IFM (UCSX-I-9108-25G).

Figure 1. Cisco UCS 9108 25G IFMs (UCSX-I-9108-25G) Replacement Instructions  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/473001-474000/473982.jpg)

---

## Page 8: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x9508/install/b-ucs-x9508-install/m-site-planning-and-maint-records.html

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

---

## Page 9: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x9508/install/b-ucs-x9508-install/b-ucs-x9508-install_index.html

  * [Preface](/c/en/us/td/docs/unified_computing/ucs/x/hw/x9508/install/b-ucs-x9508-install/m-preface.html)
  * [Overview](/c/en/us/td/docs/unified_computing/ucs/x/hw/x9508/install/b-ucs-x9508-install/m-ucsx-9508-chassis-overview.html)
  * [Installation](/c/en/us/td/docs/unified_computing/ucs/x/hw/x9508/install/b-ucs-x9508-install/m-installation.html)
  * [Installing and Removing Components](/c/en/us/td/docs/unified_computing/ucs/x/hw/x9508/install/b-ucs-x9508-install/m-installing-and-removing-components.html)
  * [Technical Specifications](/c/en/us/td/docs/unified_computing/ucs/x/hw/x9508/install/b-ucs-x9508-install/m-technical-specs.html)
  * [Intelligent Fabric Module (IFM), X-Fabric Module, and Active Fan Module Field Replaceable Unit Instructions](/c/en/us/td/docs/unified_computing/ucs/x/hw/x9508/install/b-ucs-x9508-install/m-ifm-afm-xfm-fru-replacement-instructions-labels.html)
  * [Site Planning and Maintenance Records](/c/en/us/td/docs/unified_computing/ucs/x/hw/x9508/install/b-ucs-x9508-install/m-site-planning-and-maint-records.html)
  * [Index](/c/en/us/td/docs/unified_computing/ucs/x/hw/x9508/install/b-ucs-x9508-install/b-ucs-x9508-install_index.html)


---
