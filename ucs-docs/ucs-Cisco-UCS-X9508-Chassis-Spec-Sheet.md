# Cisco UCS X9508 Chassis Spec Sheet

| | |
|---|---|
| **URL Title** | Cisco UCS X9508 Chassis Spec Sheet |
| **URL** | https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-x-series-modular-system/x9508-specsheet.pdf |
| **Long URL** |  |
| **HTML Title** |  |
| **Source file** | `ucs-docs-raw/pdf/x9508-specsheet.pdf` |
| **File type** | PDF |
| **Fetched on** | 2026-04-10 13:01:06 |

---

Spec Sheet

Cisco UCS X9508 Chassis

A printed version of this document is only a 
copy and not necessarily the latest version. 
Refer to the following link for the latest 
released version:

https://www.cisco.com/c/en/us/products/servers-
unified-computing/ucs-x-series-modular-system/
datasheet-listing.html

CISCO SYSTEMS
170 WEST TASMAN DR. 
SAN JOSE, CA, 95134
WWW.CISCO.COM

PUBLICATION HISTORY 

REV A.17

APRIL 04, 2026 

STEP
STEP
STEP
STEP
STEP
STEP
STEP
STEP

OVERVIEW  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
Intelligent Fabric Modules  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .7
Fabric Interconnect Module  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
X-Fabric Modules  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
BASE CHASSIS STANDARD CAPABILITIES and FEATURES  . . . . . . . . . . . . . . . .  15
CONFIGURING the CHASSIS  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  17
1 VERIFY BASE CHASSIS SKU . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
2 SELECT COMPUTE NODES  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
3 SELECT INTELLIGENT FABRIC MODULES  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
4 SELECT FABRIC INTERCONNECTS MODULES   . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
5 SELECT X-FABRIC (Optional)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
6 SELECT CISCO PCIE NODE (Optional) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
7 CHOOSE POWER SUPPLIES   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
8 SELECT INPUT POWER CORD(s)   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
SUPPLEMENTAL MATERIAL  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  27
9508 Chassis Server Connectivity   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
9508 Chassis Direct Server Connectivity  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
ACCESSORIES/SPARE PARTS   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  34
TECHNICAL SPECIFICATIONS  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  35
Physical Dimensions and Specifications   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
Power Supply Specifications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
Compliance Specifications  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
System Requirements  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39

2

Cisco UCS X9508 Chassis

CONTENTS

Cisco UCS X9508 Chassis

3

OVERVIEW

OVERVIEW

The Cisco UCS® X-Series Modular System begins with the Cisco UCS X9508 chassis, engineered to be 
adaptable and future ready. It is a standard, open system designed to deploy and automate faster in concert 
with your hybrid cloud environment.

With a midplane-free design, I/O connectivity for the X9508 chassis is accomplished with front-loading, 
vertically oriented compute nodes intersecting with horizontally oriented I/O connectivity modules in the 
rear of the chassis. A Unified Ethernet fabric is supplied with the Cisco UCS 9108 Intelligent Fabric Modules. 
Cisco UCS X-Fabric Technology interconnects enable connectivity between the compute and resource nodes 
using PCIe Gen4 and will supply other industry-standard protocols as standards emerge. Interconnections 
can be easily updated with new modules.

The 7 rack-unit (7RU) Cisco UCS X9508 chassis has 8 flexible slots that can house a combination of compute 
nodes and a pool of current and future I/O resources that may include GPU accelerators, disk storage, and 
nonvolatile memory.

At the top rear of the chassis are two intelligent fabric modules that connect the chassis to upstream Cisco 
6400/6500/6600 series Fabric Interconnects. At the bottom are slots housing XFM modules that can flexibly 
connect the compute modules with I/O devices and ready for future modules. This Cisco UCS X-Fabric 
technology uses ‘X’ to denote a variable that can evolve with new technology developments. 

Six 2800 W power supply units (PSUs) provide 54 VDC power to the chassis with N, N+1, N+2, and N+N 
redundancy. The higher voltage allows efficient power delivery with less copper and reduced power loss. 
Efficient, 100 mm, dual counter-rotating fans deliver industry-leading airflow and power efficiency. 
Optimized thermal algorithms enable different cooling modes to best support your environment. Cooling is 
modular so that future enhancements can potentially handle open- or closed-loop liquid cooling to support 
even higher-power processors.

In addition to the Cisco UCS® X-Series Modular System there is the Cisco UCS® X-Series Direct. Cisco UCS 
X-Series Direct transforms the Cisco UCS X-Series Modular System into a self-contained system with pair of 
internal Cisco UCS Fabric Interconnects 9108 100G that integrate each of up to eight server nodes with Cisco 
unified fabric connectivity, upstream IP and Fibre Channel connectivity, all managed through Cisco Intersight 
or the time-proven Cisco UCS Manager.

The main benefits of the Cisco UCS X-Series Modular System and the Cisco UCS X-Series Direct are as follows:

■ Cloud-operated infrastructure

Management is moved from the on-premise network to the cloud so that you can respond at the 
speed and scale of your business and manage all of your infrastructure. You can shape Cisco UCS 
X Series Modular System resources to workload requirements with the Cisco Intersight cloud- 
operations platform.

■ An adaptable system designed for modern applications

Because requirements change often, you need a system that does not lock you into one set of 
resources when you find that you need another. For hybrid applications, and a range of 
traditional data center applications, with the Cisco UCS X Series Modular System, you can 
consolidate onto a single platform that combines the density and efficiency of blade servers 
with the expandability of rack servers. The result is better performance, automation, and 
efficiency.

■ A system engineered for the future

Cisco UCS X9508 Chassis 

3

OVERVIEW

The Cisco UCS X Series Modular System is emerging technology that reduces risk with a modular 
system designed to support future generations of processors, storage, nonvolatile memory, 
accelerators, and interconnects.

■ Support a broader range of workloads

A single server type supporting a broader range of workloads means fewer different products to 
support, reduced training costs, and increased flexibility.

Figure 1 and Figure 2 show the front view and Figure 3 & Figure 4 & Figure 5 shows the rear views of a 
populated X9508 chassis. 
Note: Figure 1 shows eight slots populated with compute nodes and Figure 2 shows four slots populated 
with PCIe nodes. Figure 3 & Figure 4 shows X-Fabric Modules populated horizontally behind the chassis 
with Different IFMs. Figure 5 shows the rear view of a populated X9508 X-Series Direct chassis.

Figure 1

  Cisco UCS X9508 Chassis Front View (populated)

Front Panel

Asset Pull
Tag

Power Supplies 1 - 6

Device Slots 1 - 8

4

Cisco UCS X9508 Chassis

Figure 2

  Cisco UCS X9508 Chassis Front View with PCIe Nodes (populated)

PCIe Nodes

Front Panel

OVERVIEW

Asset Pull
Tag

Power Supplies 1 - 6

Device Slots 1 - 8

Figure 3

  Cisco UCS X9508 Chassis Rear View with X9108-IFM-100G (top) and 2 Fabric Module Slots 
(bottom)

Power Entry 
Modules (PEM) 1 - 3

Fan Modules 1 - 2

Power Entry 
Modules (PEM) 4 - 6

Intelligent Fabric 
Module 1 (X9108-IFM-100G)

Intelligent Fabric 
Module 2 (X9108-IFM-100G)

Fan Modules 3 - 4

Cisco UCS X Fabric 
Module Slot 1

Cisco UCS X Fabric 
Module Slot 2

Cisco UCS X9508 Chassis 

5

OVERVIEW

Figure 4

  Cisco UCS X9508 Chassis Rear View with X9108-IFM-25G (top) and 2 Fabric Module Slots 
(bottom)

Power Entry 
Modules (PEM) 1 - 3

Fan Modules 1 - 2

Power Entry 
Modules (PEM) 4 - 6

Intelligent Fabric 
Module 1 (X9108-IFM-25G)

Intelligent Fabric 
Module 2 (X9108-IFM-25G)

Fan Modules 3 - 4

Cisco UCS X Fabric 
Module Slot 1

Cisco UCS X Fabric 
Module Slot 2

Figure 5

  Cisco UCS X9508 X-Series Direct Rear View with UCSX-S9108-100G (top) and 2 Fabric Module 
Slots (bottom)

y 
Power Entry 
3
Modules (PEM) 1 - 3

2
Fan Modules 1 - 2

Power Entry 
y 
Modules (PEM) 4 - 6
6

UCS Fabric Interconnect 9108 100G
Module 1 (UCSX-S9108-100G)

UCS Fabric Interconnect 9108 100G
Module 2 (UCSX-S9108-100G)

Fan Modules 3 - 4

Cisco UCS X Fabric 
Module Slot 1

Cisco UCS X Fabric 
Module Slot 2

6

Cisco UCS X9508 Chassis

OVERVIEW

Intelligent Fabric Modules

Network connectivity is provided by a pair of Cisco UCS 9108 Intelligent Fabric Modules (IFMs). Similar to the 
fabric extenders used in the Cisco UCS 5108 Blade Server Chassis, these modules carry all network traffic to 
a pair of Cisco UCS 6400/6500/6600 series Fabric Interconnects (FIs). Having a single point of network 
connectivity and control in a system provides deterministic latency. This, in turn, frees you to place 
workloads without regard to whether the compute nodes are in the same chassis. Each IFM features the 
following:

Cisco UCS 9108-25G IFM:

■ Server ports: Up to 50 Gbps of unified fabric connectivity per compute node with two IFMs.

■ Uplink ports: 8x 25-Gbps SFP28 ports. 

Cisco UCS 9108-100G IFM:

■ Server ports: Up to 200 Gbps of unified fabric connectivity per compute node with two IFMs.

■ Uplink ports: 8x 100-Gbps QSFP8 ports.

The unified fabric carries management, application data traffic using Ethernet and/or Fibre Channel over 
FCoE protocols to the fabric interconnects. There, management traffic connects to the Cisco Intersight 
cloud operations platform; FCoE traffic is passed to native Fibre Channel interfaces through universal ports 
on the fabric interconnects, and production Ethernet traffic is passed upstream to the data center network.

Up to two Intelligent Fabric Modules (IFMs) plug into the back of the UCS X9508 chassis.

The IFMs serve as line cards in the chassis and multiplex data from the Cisco UCS X210c, X215c or X410c 
compute nodes to the Fabric Interconnect (FI). They also monitor and manage chassis components such as 
fan units, power supplies, environmental data, LED status panel, and other chassis resources. The compute 
node’s Keyboard-Video-Mouse (KVM) data, Serial over LAN (SoL) data, and Intelligent Platform Management 
Interface (IPMI) data also travel to the IFMs for monitoring and management purposes. In order to provide 
redundancy and failover, the IFMs are always used in pairs.

There are 8 x SFP28 or 8 X QSFP28 connectors on an IFM to interface with a Fabric Interconnect (FI). The 
IFM provides up to 8x 25 Gbit/s links for the UCS 9108-25G IFM and 8X 100 Gbit/s links for the UCS 
9108-100G IFM. The links provide the end-to-end interface from a compute node in the X9508 chassis to the 
connections on a Fabric Interconnect (FI). When a compute node is inserted into the chassis, the compute 
node’s upper mezzanine card (mLOM) plugs directly into the two IFMs using two orthogonal connectors 
(ODs). The X9508 chassis accommodates either two Cisco UCS 9108-25G IFMs, two Cisco UCS 9108-100G IFM, 
or Cisco UCS Fabric Interconnect 9108 100G.

Cisco UCS X9508 Chassis 

7

OVERVIEW

Figure 6 shows the IFM front view characteristics.

Figure 6

  Cisco UCS 9108-25G IFM (front view)

8

9

1

2

1

2

3

UCSBX-I-9108-25G

1

2

3

4

5

6

7

8

3

4

6

7

6

5

1 

IFM status LED

2

3

4

5

Fan #1 - #3 status LEDs

Reset button

SFP28 ports 1 - 4

SFP28 ports 5 - 8

6

7

8

9

-

Ejector handle

HDMI port (for factory use only)

Link/port status LED (one per port)

Port activity LED (one per port)

-

Figure 7 shows the IFM front view characteristics.

Figure 7

  Cisco UCS 9108-100G IFM (front view)

1 

Status LEDs:

3

QSFP28 Optical Ports. 

■ IFM Status (top LED)

■ Fan Status LEDs 1 through 3, with 

Fan 1 as LED 2, Fan 2 as LED 3, and 
Fan 3 as LED 4. 

Ports are arranged in two groups of four 
physical ports. Ports are stacked in vertical 
pairs, with two ports in each vertical port 
stack. 

2

IFM Reset Button

4

IFM Ejector Handles, left and right

Figure 8 shows the IFM top view characteristics. 

8

Cisco UCS X9508 Chassis

Figure 8

  Cisco UCS 9108-25G IFM (top view) 

1

2

3

OVERVIEW

7

4

5

6

5

1 

Fan #1

2

3

7

Fan #2

Fan #3

CPU

Mini storage connector (future)

Ejector Handles

Cisco switch ASIC

4

5

6

-

(Intel Denverton, 4-core, 2.1 GHz, 15W)

Figure 9 shows the IFM top view characteristics.

Cisco UCS X9508 Chassis 

9

OVERVIEW

Figure 9

  Cisco UCS 9108-100G IFM (top view)

1 

Fans (3) which are numbered 1 through 3 
starting with the left fan

4

QSFP28 Optical Ports 5-8

Ports are arranged in two groups of four 
physical ports. Ports are stacked in vertical 
pairs, with two ports in each vertical port 
stack. 

IFM ejector handles, left and right

-

2

3

One M.2 mini storage module slot

QSFP28 Optical Ports 1-4

Ports are arranged in two groups of four 
physical ports. Ports are stacked in 
vertical pairs, with two ports in each 
vertical port stack. 

5

-

10

Cisco UCS X9508 Chassis

OVERVIEW

Fabric Interconnect Module

The Cisco UCS Fabric Interconnect 9108 100G (Figure 10) is an integrated 1/10/25/40/100 Gigabit 
Ethernet, FCoE, and Fibre Channel switch offering up to 1.6 Tbps throughput and up to 8 ports. The switch 
has 6 40/100-Gbps Ethernet ports and 2 unified ports that can support 40/100-Gbps Ethernet ports or 8 
Fiber Channel ports after break-out at 8/16/32-Gbps FC speeds. The 8 FC ports after breakout can either 
operate as an FC uplink port or as an FC storage port. The switch supports 2 1-Gbps speed after breakout 
and all 8 ports can breakout for 10/25-Gbps Ethernet connectivity. All Ethernet ports are capable of 
supporting FCoE. Beyond the 8 external facing 100G ports, the Fabric Interconnect 9108 100G also provides 
eight 100G or thirty-two 25G backplane ethernet ports connectivity towards the X-series compute nodes 
depending on 100G or 25G VIC. The rear-view image shows the ortho-direct connectors that will connect to 
the VIC on the X-series compute node.

The Cisco UCS Fabric Interconnect 9108 100G also has one network management port, one console port for 
setting the initial configuration, and one USB port for saving or loading configuration.

Figure 10 shows the 8-port FI.

Figure 10

  Cisco UCS Fabric Interconnect 9108 100G.

Front View

Rear View

The Cisco UCS Fabric Interconnect 9108 100G front detailed view shown in Figure 11.

Cisco UCS X9508 Chassis 

11

OVERVIEW

Figure 11

  Cisco UCS Fabric Interconnect 9108 100G (front view)

1 

Status LEDs:

2

QSFP28 Optical Ports. 

■ FI Status (top LED)

■ Fan Status LEDs 1 through 3, with 

Fan 1 as LED 2, Fan 2 as LED 3, and 
Fan 3 as LED 4. 

Ports are arranged in two groups of four physical 
ports. Ports are stacked in vertical pairs, with 
two ports in each vertical port stack. 

3

5

Management Port

USB Port

Console Port

4

-

12

Cisco UCS X9508 Chassis

Figure 12

  Cisco UCS Fabric Interconnect 9108 100G (top view)

OVERVIEW

1 

Fans (3) which are numbered 1 through 3 
starting with the left fan

4

QSFP28 Optical Ports 5-8

Ports are arranged in two groups of four 
physical ports. Ports are stacked in vertical 
pairs, with two ports in each vertical port 
stack. 

FI ejector handles, left and right

-

2

3

One M.2 mini storage module slot

QSFP28 Optical Ports 1-4

5

-

Ports are arranged in two groups of four 
physical ports. Ports are stacked in vertical 
pairs, with two ports in each vertical port 
stack. 

Cisco UCS X9508 Chassis 

13

OVERVIEW

X-Fabric Modules

Configuring your Cisco UCS X210c, X215c or X410c Compute Nodes in the X9508 chassis with both mLOM and 
mezzanine-form-factor virtual interface cards delivers up to 200 Gbps of network bandwidth to the node 
and prepares it for connectivity to Cisco UCS PCIe node and future devices with Cisco UCS X-Fabric 
technology. The PCIe I/O devices are configured on demand and connects to the Cisco UCS X210c, X215c or 
X410c Compute Nodes through Cisco UCS X-Fabric modules in the Cisco UCS X9508 Chassis.

Following combinations can be used to connect the Cisco UCS X210c, X215c or X410c node to the Cisco UCS 
PCIe node via Cisco UCS X9416 X-Fabric.

■ UCS VIC 14425 mLOM card and mezzanine-form-factor virtual interface card or the Cisco UCS PCIe 

Mezz card for X-Fabric.

■ UCS VIC 15230 mLOM card and mezzanine-form-factor virtual interface card or the Cisco UCS PCIe 

Mezz card for X-Fabric.

Fabric Modules slots provide an alternative path to bridging/switching within the chassis and interconnect 
compute node CPUs, storage devices, and communication devices so that all these components 
interoperate directly without any need to translate PCIe to Ethernet. The result is a significant reduction in 
cost, power, and latency.

With the Cisco UCS X9416 X-Fabric there are x16 high speed links (PCIe Gen 4 is supported) connected from 
each X-Fabric Module slot to each compute node.

The X-Fabric Module slots are located at the rear of the UCS X9508 chassis. When a compute node is 
inserted into the chassis, the compute node’s mezzanine card plugs directly into the two Fabric Module slots 
(with no midplane).

Figure 13

  Front view of Cisco UCS X9416 X-Fabric.

Front View

14

Cisco UCS X9508 Chassis

BASE CHASSIS STANDARD CAPABILITIES and FEATURES

BASE CHASSIS STANDARD CAPABILITIES and FEATURES

Table 1 lists the capabilities and features of the base X9508 chassis. Details about how to configure the 
chassis for a particular feature or capability are provided in CONFIGURING the CHASSIS, page 17. 

Table 1   Capabilities and Features  

Capability/Feature

Description

7 RU Chassis

The X9508 chassis has 8x front-facing flexible slots. These can house a 
combination of compute nodes and a pool of future I/O resources that may 
include GPU accelerators, disk storage, and nonvolatile memory.

Compute Node Support

■ General

• Support for 2-CPU single slot and 4-CPU dual slot compute nodes

■ Compute Nodes

• Supports CPUs and future GPUs with 300W+ TDP, and 900W+ per 

compute node TDP

• Support for highest end DDR/persistent memory configurations

• Support for a minimum of 2 Mezzanine slots for premium VIC, GPU, 

and FPGA expansion

Intelligent Fabric 
Module

2x Cisco UCS 9108 Intelligent Fabric Modules (IFMs) at the top of the chassis 
that connect the chassis to upstream Cisco UCS 6400/6500/6600 series 
Fabric Interconnects. Each IFM features the following:

■ Up to 100 Gbps of unified fabric connectivity per compute node.

■ 8x 25-Gbps SFP28 or 8X 100-Gbps QSFP28 uplink ports. The unified 
fabric carries management traffic to the Cisco Intersight cloud- 
operations platform, Fibre Channel over Ethernet (FCoE) traffic, and 
production Ethernet traffic to the fabric interconnects. 

Fabric Interconnect 
Module

2x Cisco UCS Fabric Interconnect 9108 100G Modules (FIs) at the top of the 
chassis that connect the chassis to upstream Top-of-Rack (ToR) switches. 
Each FI features the following:

Cisco UCS X-Fabric 
technology 

Next Generation Power 
and Thermal Capability

■ Up to 100 Gbps of unified fabric connectivity per compute node.

■ Integrated 1/10/25/40/100 Gigabit Ethernet, FCoE, and Fibre Channel 
switch offering up to 1.6 Tbps throughput and up to 8 ports. The switch 
has 6 40/100-Gbps Ethernet ports and 2 unified ports that can support 
40/100-Gbps Ethernet ports or 8 Fiber Channel ports after break-out at 
8/16/32-Gbps FC speeds.

At the bottom rear of the X9508 chassis are slots ready to house X-Fabric 
modules that can flexibly connect the compute modules with I/O devices. 
The “X” in Cisco UCS X-Fabric technology denotes a variable that can evolve 
with new technology developments.

■ Power supplies

• Six 2800-Watt power supplies providing 54 V power

• 4x 100 mm dual counter-rotating fans 

• N, N+1, N+2, and N+N redundancy

• 300 Watt+ total power dissipation for compute nodes

Cisco UCS X9508 Chassis 

15

BASE CHASSIS STANDARD CAPABILITIES and FEATURES

Table 1   Capabilities and Features  (continued)

Capability/Feature

Description

Density and Form Factor

■ Industry-leading socket density per RU

■ Minimum of 8 compute slots

■ 32 DIMM socket support on a 2-socket compute node (beginning with the 
Ice Lake CPU family) and 64 DIMM socket support on a 4-socket compute 
node (beginning with the Sapphire Rapids CPU family)

■ Power, thermal, and form factor support for smart NICs, FPGA 

accelerators, and GPU cards

Fabric Bandwidth

■ Data fabric connectivity to compute nodes of 200 Gbps Ethernet speeds 

per compute node

■ Provision for future fabric expansion

Chassis Storage Support

■ Local storage

Virtual Card Interface 
(VIC) Support

■ Cisco VIC ASIC

■ 25G throughput

■ 100G throughput

16

Cisco UCS X9508 Chassis

CONFIGURING the CHASSIS

CONFIGURING the CHASSIS

Follow these steps to configure the Cisco UCS X9508 chassis:

■ STEP 1 VERIFY BASE CHASSIS SKU, page 18

■ STEP 2 SELECT COMPUTE NODES, page 19

■ STEP 3 SELECT INTELLIGENT FABRIC MODULES, page 20

■ STEP 4 SELECT FABRIC INTERCONNECTS MODULES, page 21

■ STEP 6 SELECT CISCO PCIE NODE (Optional), page 23

■ STEP 7 CHOOSE POWER SUPPLIES, page 24

■ STEP 8 SELECT INPUT POWER CORD(s), page 25

■ SUPPLEMENTAL MATERIAL, page 27

Cisco UCS X9508 Chassis 

17

CONFIGURING the CHASSIS

STEP 1

VERIFY BASE CHASSIS SKU

Top level ordering product ID (PID) is shown inTable 2.

Table 2   Top Level Major Line Bundle ordering PIDs (MLB)

Product ID (PID)

Description

UCSX-M6-MLB

UCS M6 Rack, Blade, Chassis MLB

UCSX-M7-MLB

UCS M7 Rack, Blade, Chassis MLB

UCSX-M8-MLB

UCS M8 Rack, Blade, Chassis MLB

Verify the product ID (PID) of the base X9508 chassis as shown in Table 3.

Table 3   PID of the Base Cisco UCS X9508 Chassis 

Product ID (PID)

Description

Usage

M6

UCSX-9508=

UCS X9508 Chassis

Chassis with or without IFM, PSU - Nodes are not 
offered/configurable in this SKU

UCSX-9508-U

UCS X9508 Chassis Configured

Chassis configured with Node, IFM, PSU etc

UCSX-9508-CH

DISTI: UCS X9508 Chassis

M7/M8

UCSX-9508-D=

UCS X9508 Chassis

Chassis SKU used for Cisco approved 
Distributor’s: this SKU is not configurable -Bare 
Chassis with Blanks, Brackets and Accessory Kit

Chassis with or without IFM, PSU - Nodes are not 
offered/configurable in this SKU

UCSX-9508-D-U

UCS X9508 Chassis Configured

Chassis configured with Node, IFM, PSU etc

UCSX-9508-D-CH

DISTI: UCS X9508 Chassis

Chassis SKU used for Cisco approved 
Distributor’s: this SKU is not configurable -Bare 
Chassis with Blanks, Brackets and Accessory Kit

Items included with the chassis:

Items not included with the chassis (but may be 
ordered separately):

■ Fans

■ Chassis accessory kit

■ Compute nodes

■ IFMs

■ Compute node blank panels (where needed)

■ FIs

■ X-Fabric module blank panels (two)

■ X-Fabric modules

■ Power supply blanks (where needed)

■ PCI Nodes, Risers and GPU

■ Chassis Rear AC Power Expansion Module (two)

■ Transceivers and cables

■ AC power supply keying bracket

■ Power supplies

18

Cisco UCS X9508 Chassis

CONFIGURING the CHASSIS

STEP 2 SELECT COMPUTE NODES

Choose Compute Nodes

The available single-slot compute nodes for the chassis is shown in Table 4. 

Table 4   Available Compute Nodes 

Product ID (PID)

Description

UCSX-210C-M6

UCSX-210C-M7

UCSX-410C-M7

UCSX-210C-M8

UCSX-215C-M8

UCSX-410C-M8

UCS 210c M6 Compute Node without CPU, Memory, Storage, Mezz

UCS 210c M7 Compute Node without CPU, Memory, Storage, Mezz

UCS 410c M7 Compute Node without CPU, Memory, Storage, Mezz

UCS 210c M8 Compute Node without CPU, Memory, Storage, Mezz

UCS 215c M8 Compute Node without CPU, Memory, Storage, Mezz

UCSX 410c M8 Compute Node w/o CPU, Memory, Storage, Mezz

Approved Configurations

(1) Choose from one to eight compute nodes

Caveats

The chassis can accommodate up to eight single-slot or four dual-slot compute nodes or a mix of 
single- and dual-slot compute nodes. If any PCIe nodes are used in the chassis, then fewer 
compute nodes can be installed in the chassis.

NOTE:  Refer to the compute node specification sheets below for more details on the 
components and PIDs:

■ Cisco UCS X210c M8 Compute Node Spec Sheet

■ Cisco UCS X215c M8 Compute Node Spec Sheet

■ Cisco UCS X410c M7 Compute Node Spec Sheet

■ Cisco UCS X210c M6 Compute Node Spec Sheet 

■ Cisco UCS X210c M7 Compute Node Spec Sheet 

Cisco UCS X9508 Chassis 

19

CONFIGURING the CHASSIS

STEP 3 SELECT INTELLIGENT FABRIC MODULES

Choose Intelligent Fabric Modules

The available Intelligent Fabric Modules are listed in Table 5. Each IFM connects to external 
Fabric Interconnects using 8x 25G ports or 8x 100G ports

Table 5   Available Intelligent Fabric Modules (IFMs) 

Product ID (PID)

Description

M6

UCSX-I-9108-25G

UCS 9108-25G IFM for X9508 chassis

UCSX-I-9108-100G

UCS 9108-100G IFM for X9508 chassis

M7/M8

UCSX-I-9108-25G-D

UCS 9108-25G IFM for 9508 Chassis

UCSX-I9108-100G-D

UCS 9108-100G IFM for X9508 chassis

Approved Configurations

(1) Choose two IFMs of same type

(2) You can not mix IFM and integrated FI in the same chassis

NOTE:  Refer to the IFM specification sheets below for more details on the 
components and PIDs:

■ Cisco UCS 9108 25G Intelligent Fabric Module Spec Sheet 

■ Cisco UCS 9108 100G Intelligent Fabric Module Spec Sheet

20

Cisco UCS X9508 Chassis

CONFIGURING the CHASSIS

STEP 4

SELECT FABRIC INTERCONNECTS MODULES

Choose Fabric Interconnect Modules

The available Fabric Interconnect Modules are listed in Table 6. Each FI connects to external 
Top-of-Rack switch using 8x 100G ports.

Table 6   Available Fabric Interconnect

Product ID (PID)

Description

M6

UCSX-S9108-100GM6 

UCS X-Series Direct Fabric Interconnect 9108 100G

UCSX-S9108-SW

Perpetual SW License for UCS X-Series Direct FI 9108-100G

M7/M8

UCSX-S9108-100G

UCS X-Series Direct Fabric Interconnect 9108 100G

UCSX-S9108-SW

Perpetual SW License for UCS X-Series Direct FI 9108-100G

Approved Configurations

(1) Choose two FI

(2) You can not mix IFM and integrated FI in the same chassis

NOTE:  Refer to the Fabric Interconnect specification sheets below for more details 
on the components and PIDs:

■ Cisco UCS Fabric Interconnect 9108 100G Spec Sheet

Cisco UCS X9508 Chassis 

21

CONFIGURING the CHASSIS

STEP 5 SELECT X-FABRIC (Optional)

Choose X-Fabric Modules

The available X- Fabric Modules are listed in Table 7. Each X-Fabric module provides native PCIe 
Gen4 x16 connectivity to the X210c, X215c or X410c Compute node and the Cisco UCS X440p and 
X580p PCIe Node.

Table 7   Available X- Fabric Modules (XFMs)  

Product ID (PID)

Description

UCSX-F-9416-D

UCS 9416 X-Fabric module for 9508 chassis

Choose X-Fabric PCIE ETX

Table 8   Available X- Fabric PCIe ETX

Product ID (PID)

Description

UCSX-FS-9516

UCS 9516 X-Fabric PCIe Gen5 switch module for 9508 chassis

Approved Configurations

(1) Choose two XFMs or PCIE ETX

22

Cisco UCS X9508 Chassis

CONFIGURING the CHASSIS

STEP 6 SELECT CISCO PCIE NODE (Optional)

The available PCIe Nodes

Table 9   Available PCIe Node Option

Product ID (PID)

Description

M6

UCSX-440P

UCS X-Series Gen4 PCIe node

M7/M8

UCSX-440P-D

UCS X-Series Gen4 PCIe node

UCSX-580P

UCS X-series PCIe Gen5 node

Approved Configuration

The PCIe node requires both the risers to be configured and doesn’t support orderability without 
both risers included.

NOTE:  Refer to the below spec sheet for the list of components such as riser cards 
and available GPUs under the PCIe Nodes:

■ Cisco UCS X440p PCIe Node Spec Sheet

23

Cisco UCS X9508 Chassis

CONFIGURING the CHASSIS

STEP 7 CHOOSE POWER SUPPLIES

The X9508 chassis accommodates up to six power supplies. The six dual feed power supplies 
provide an overall chassis power capability of greater than 9000 W, and can be configured as N, 
N+1, N+2, or N+N redundant.

Choose Power Supplies

The available power supplies are listed in Table 10

.

Table 10  Available Power Supplies

Product ID (PID)

PID Description

UCSX-PSU-2800AC

UCS 9508 Chassis 2800 VAC Dual Voltage PSU

UCSX-PSU-2800AC-D

UCS 9508 Chassis 2800 VAC Dual Voltage PSU

Approved Configurations

Choose from 2 to 6 power supplies

■ If node quantity 1 is selected, then minimum 2 quantity of PSU is required

■ If node quantity 2 to 6 is selected, then minimum 4 quantity of PSU is required

■ If node quantity 7 or 8 is selected, then minimum 6 quantity of PSU is required

NOTE:  

■ Two PSUs minimum are required for chassis operation. Four PSUs are 

recommended and the maximum number of PSUs is six.

■ Use the Power Calculator to determine the correct number of power supplies. 

The Power Calculator can be found at this link:

http://ucspowercalc.cisco.com\

Cisco UCS X9508 Chassis 

24

CONFIGURING the CHASSIS

STEP 8 SELECT INPUT POWER CORD(s)

Select the appropriate AC power cords listed in Table 11. You may select up to 6 power cords.

Table 11  Available Power Cords

Product ID (PID)

PID Description

CAB-AC-16A-AUS

CAB-9K16A-BRZ

16A, 250 VAC

16A, 250 VAC

UCSB-CABL-C19-BRZ

C19, 14', 16A, 250V

CAB-AC16A-CH

CAB-AC-2500W-EU

16A, 250 VAC

16A, 250 VAC

Comment

Australia

Brazil

Brazil

China

Europe

CAB-AC-2500W-INT

16A, 250 VAC

International

CAB-AC-2500W-ISRL

16A, 250 VAC

CAB-US620P-C19-US 

16A, 250VAC

NEMA L6-20P to IEC C19

CAB-AC-C6K-TWLK

20A, 250VAC

NEMA L6-20 (Twist Lock) to IEC C19

Israel

USA

USA

CAB-ACS-16

CAB-C19-CBN

CAB-US515P-C19-US 

CAB-US520-C19-US

16A, 250 VAC

16A, 250 VAC

15A, 125 VAC 
NEMA 5-15 to IEC-C19

20A, 125 VAC 
NEMA 5-20 to IEC-C19

CAB-BS1363-C19-UK

13A, 250 VAC 

BS1363 to IEC C19

Switzerland

Jumper cord C19/C20

USA

USA

UK

CAB-9K16A-KOR

16A, 250 VAC 

South Korea

CEE 7/7 to IEC C19

CAB-C19-C20-3M-JP

16A, 250 VAC

CAB-AC-C19-TW

250.0 V, 16.0 A

CAB-IR2073-C19-AR

20A, 250 VAC

IRSM 2073 to IEC C19

CAB-SABS-C19-IND

16A, 250 VAC 

SABS 164-1 to IEC C19

CAB-C19-C20-IND

14 AWG, 250.0 V, 16.0 A, 9' L

Japan

Taiwan

Argentina

India

India

25

Cisco UCS X9508 Chassis

CONFIGURING the CHASSIS

Table 11  Available Power Cords

Product ID (PID)

PID Description

Comment

CAB-S132-C19-ISRL

16A, 250 VAC 

S132 to IEC C19

CAB-C2316-C19-IT

16A, 250 VAC 

CEI 23-16 to IEC C19

R2XX-DMYMPWRCORD 

No power cord

Israel

Italy

Cisco UCS X9508 Chassis 

26

SUPPLEMENTAL MATERIAL

SUPPLEMENTAL MATERIAL

9508 Chassis Server Connectivity

The connectivity from the IFMs to 6400 series Fabric Interconnects is shown in Figure 14.

Figure 14

IFM to 6400 Series Fabric Interconnect Connectivity

= SFP28 Links
= QSFP28 Links

Uplink Ports

1

2 3

4 5

6 7

8 9

10 11

12 13

14 15

16

17

18 19

20 21

22 23

24 25

26 27

28 29

30 31

32

33

34 35

36 37

38 39

40 41

42 43

44 45

46 47

48

49

50

51

52

53

54

CISCO UCS-FI-6454

CISCO UCS-FI-6454

6454 Fabric Interconnect #2

17

18 19

20 21

22 23

24 25

26 27

28 29

30 31

32

33

34 35

36 37

38 39

40 41

42 43

44 45

46 47

48

6454 Fabric Interconnect #1

IFM #1

IFM #2

Cisco UCS X9508 Chassis

27

Cisco UCS X9508 Chassis

  
SUPPLEMENTAL MATERIAL

For the X9508 chassis, the Fabric Extender modules (up to two) plug into the back of the UCS X9508 chassis. 
The X9508 chassis accommodates the following IFMs:

■ Cisco IFM 9108-25G (Figure 15)
■ Cisco IFM 9108-100G (Figure 16)

The connectivity from the X9108-IFM-25G to 6536 series Fabric Interconnects is shown in Figure 15.

Figure 15

X9108-IFM-25G to 6536 Series Fabric Interconnects Connectivity

100G

100G

100G

100G

= QSFP28 Links
400G Per X9508 Chassis
25G E2E single-flow
200G Per x210 with 4:1  oversubsription

6536 FI

6536 FI

IFM A-25G  (8 x 25GB) 

IFM B-25G  (8 x 25GB) 

IFM A

IFM  B

Cisco UCS X9508 Chassis

The connectivity from the X9108-IFM-100G to 6536 series Fabric Interconnects is shown in Figure 16.

Cisco UCS X9508 Chassis 

28

  
SUPPLEMENTAL MATERIAL

Figure 16

X9108-IFM-100G to 6536 Series Fabric Interconnect Connectivity

 QSFP28 Links

1600G Per X9508 Chassis
100G E2E single-flow
200G Per x210 with 1:1  oversubsription

IFM A-100G  (8 x 100GB) 
IFM B-100G  (8 x 100GB) 

IFM  A

IFM  B

29

Cisco UCS X9508 Chassis

  
SUPPLEMENTAL MATERIAL

9508 Chassis Direct Server Connectivity 

The LAN connectivity from the Cisco UCS Fabric Interconnect 9108 100G to the ToR switch is shown in 
Figure 17 and Figure 18

Figure 17

  LAN Connectivity with Cisco UCS Fabric Interconnect 9108 100G and vPC in End-Host mode

Figure 18

  LAN Connectivity with Cisco UCS Fabric Interconnect 9108 100G but without vPC in end-host 
mode

Cisco UCS X9508 Chassis 

30

SUPPLEMENTAL MATERIAL

The SAN connectivity from the Cisco UCS Fabric Interconnect 9108 100G to a Cisco MDS or non-MDS switch is 
shown in Figure 19, Figure 20 and Figure 21

Figure 19

  SAN Connectivity with Cisco UCS Fabric Interconnect 9108 100G and FC end-host or switch 
mode (Cisco MDS)

Figure 20

  SAN Connectivity with Cisco UCS Fabric Interconnect 9108 100G and FC end-host mode 
(non-Cisco MDS)

31

Cisco UCS X9508 Chassis

Figure 21

  SAN Connectivity with Cisco UCS Fabric Interconnect 9108 100G and FC switch mode 
(direct attached)

SUPPLEMENTAL MATERIAL

Cisco UCS X9508 Chassis 

32

SUPPLEMENTAL MATERIAL

The IP-SAN connectivity from the Cisco UCS Fabric Interconnect 9108 100G is shown in, Figure 22 and 
Figure 23

Figure 22

  IP-SAN Connectivity with Cisco UCS Fabric Interconnect 9108 100G

Figure 23

  IP-SAN Connectivity with Cisco UCS Fabric Interconnect 9108 100G and Appliance Port 
through ToRs in vPC Port Channel configuration

33

Cisco UCS X9508 Chassis

ACCESSORIES/SPARE PARTS

This section lists the upgrade and service-related parts for the Cisco UCS X9508 chassis. Some of these parts 
are configured with every compute node or with every Cisco UCS X9508 chassis.

ACCESSORIES/SPARE PARTS

Table 12  Spare Parts for Cisco UCS X9508 chassis

Spare Product ID (PID)

Description

UCSX-C-DEBUGCBL=
UCSX-9508-FSBK=
UCSX-9508-PSUBK=
UCSX-9508-CAK=
UCSX-9508-RBLK=
UCSX-9508-ACPEM=
UCSX-9508-KEY-AC=
UCSX-9508-FAN=

UCSX Compute Node KVM dongle cable
UCS 9508 Chassis Front Node Slot Blank
UCS 9508 Chasiss PSU Blank
UCS 9508 Chassis Accessory Kit
UCS 9508 Chassis Active Cooling Module (XFM slot)
UCS 9508 Chassis Rear AC Power Expansion Module 
UCS 9508 AC PSY Keying Bracket 
UCS 9508 Fan Module

Cisco UCS X9508 Chassis 

34

TECHNICAL SPECIFICATIONS

TECHNICAL SPECIFICATIONS

Physical Dimensions and Specifications

The physical specifications for the Cisco UCS X9508 chassis are listed in Table 13

Table 13  Cisco UCS X9508 Chassis Specifications  

Parameter

Value

Height

Width

Depth

Weight

12.05 in (30.6 cm); 7 RU

17.55 (44.6 cm); fits standard 19-inch square-hole rack

35.8 in (90.932 cm)

Empty chassis: 95 lb (43.09 kg)

Fully populated chassis: Approximately 400 lb (163.29 kg) depending 
on models and options selected

Compute node slots

8 full-width slots.

Intelligent Fabric Modules (IFMs)

2 x Cisco UCS 9108 Intelligent Fabric Module with 8x 25G SFP28 ports 
or or 8x 100G QSFP28 ports.

Fabric Interconnect Modules (FI)

2 x Cisco UCS 9108 100G Fabric Interconnect Module with 8x 100G 
QSFP28 ports

X-Fabric Module slots

2x Cisco UCS X-Fabric module rear blank slots (for future expansion)

Fan modules

Power supply bays

Power supplies

4 x 100mm hot-swappable dual rotor fans

6

2800 W Titanium certified

Input voltage

100 to 127 V AC

200 to 240V AC

Each power supply can be 
connected to a different 
phase

Maximum input VA

3200 VA at 230 VAC

Maximum output power per 
power supply

2800 W @200-240 VAC 
Nominal

1400 W @100-127 VAC 
Nominal

Frequency

Output voltage

50 to 60 Hz

54 VDC

Power redundancy

Nonredundant, N+1, N+2 and Grid (N+N)

Power entry module (PEM)

2x PEM for AC inputs, PEM1 (PSU1,2,3), PEM2 (PSU4,5,6)

35

Cisco UCS X9508 Chassis

TECHNICAL SPECIFICATIONS

Table 13  Cisco UCS X9508 Chassis Specifications  (continued)

Parameter

Management

Value

■ Cisco Intersight Software

 (SaaS, Virtual Appliance and Private Virtual Appliance)

■ Cisco UCS Manager

Temperature: operating

50 to 95°F (10 to 35°C) (as altitude increases, maximum 
temperature decreases by 1°C per 300m)

Temperature: non-operating

-40 to 149°F (-40 to 65°C); maximum altitude is 40,000 ft

Humidity: operating

10% to 90% noncondensing, 28°C max

Humidity: non-operating

5% to 93% noncondensing, 38°C max

Altitude: operating

0 to 10,000 ft (0 to 3000m); maximum ambient temperature 
decreases by 1°C per 300m

Altitude: non-operating

40,000 ft (12,000m)

Sound pressure level

83 dBA (at normal operating temperature)

For configuration-specific power specifications, use the Cisco UCS Power Calculator at:

https://ucspowercalc.cisco.com

Cisco UCS X9508 Chassis 

36

TECHNICAL SPECIFICATIONS

Power Supply Specifications

Detailed specifications for the Cisco UCS X9508 power supplies are listed in Table 14

Table 14  Cisco UCS X9508 Power Supply Specifications  

Parameter

AC input voltage

Value

Voltage Range 100-127 VAC, 200-240 VAC nominal  
(range: 90-140 VAC, 180-264 VAC)

Each power supply can be connected to a different phase

AC input frequency

50 to 60 Hz nominal (range: 47 to 63 Hz

Maximum AC input current

Maximum input VA

18 A @ 90 VAC 

18 A @ 180 VAC

3200 VA at 230 VAC

Maximum output power per power 
supply

2800 W @ 200-240 VAC nominal 

1400 W @ 100-127 VAC nominal

Maximum inrush current

35 A (sub cycle duration)

Minimum holdup time

10 ms @ 1400 W 

10 ms @ 2800 W

Power supply main output voltage

54 VDC

Efficiency rating

Input connector

80+ Titanium Certified

IEC320 C20

System input power connectors are located in the chassis 
PEMs, not on the power supply

37

Cisco UCS X9508 Chassis

TECHNICAL SPECIFICATIONS

Compliance Specifications

The regulatory standards compliance (safety and EMC) specifications for the Cisco UCS X9508 chassis are 
listed in Table 15.

Table 15  Cisco UCS X9508 Chassis Compliance Specifications

Parameter

Description

Regulatory compliance

Products comply with CE Markings per directives 2004/108/EC and 
2006/108/EC

Safety

■ UL 60950-1

■ CAN/CSA-C22.2 No. 60950-1

■ EN 60950-1

■ IEC 60950-1

■ AS/NZS 60950-1

■ GB4943

EMC: Emissions

■ 47CFR Part 15 (CFR 47) Class A (FCC Class A)

■ AS/NZS CISPR22 Class A

■ CISPR2 2 Class A

■ EN55022 Class A

■ ICES003 Class A

■ VCCI Class A

■ EN61000-3-2

■ EN61000-3-3

■ KN22 Class A

■ CNS13438 Class A

■ EN50082-1

■ EN61000-6-1

■ EN55024

■ CISPR24

■ EN300386

■ KN 61000-4 Series

EMC: Immunity

Cisco UCS X9508 Chassis 

38

TECHNICAL SPECIFICATIONS

System Requirements

The system requirements for the Cisco UCS X9508 chassis are listed in Table 16.

Table 16  Cisco UCS X9508 Chassis Compliance Specifications

Item

Requirement

X-Series chassis

Cisco UCS X9508 Chassis

Fabric interconnect

Cisco UCS 6400/6500/6600 series Fabric Interconnects1

Cisco Intersight or Cisco 
UCS Manager

Cisco Intersight Managed Mode or Cisco UCS Manager for management

Notes:

1. Only when configured with IFMs

39

Cisco UCS X9508 Chassis

TECHNICAL SPECIFICATIONS

Cisco UCS X9508 Chassis 

40

