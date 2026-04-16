# Cisco UCS X410c M7 Compute Node Spec Sheet

| | |
|---|---|
| **URL Title** | Cisco UCS X410c M7 Compute Node Spec Sheet |
| **URL** | https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-x-series-modular-system/x410cm7-specsheet.pdf |
| **Long URL** |  |
| **HTML Title** |  |
| **Source file** | `ucs-docs-raw/pdf/x410cm7-specsheet.pdf` |
| **File type** | PDF |
| **Fetched on** | 2026-04-16 10:51:52 |

---

Spec Sheet

Cisco UCS X410c M7 
Compute Node

A printed version of this document is only a copy 
and not necessarily the latest version. Refer to 
the following link for the latest released version:

https://www.cisco.com/c/en/us/products/servers-unified-
computing/ucs-x-series-modular-system/datasheet-
listing.html

CISCO SYSTEMS
170 WEST TASMAN DR. 
SAN JOSE, CA, 95134
WWW.CISCO.COM

PUBLICATION HISTORY 

REV A.27

MARCH 10, 2026

 
STEP
STEP
STEP

STEP
STEP
STEP
STEP
STEP
STEP
STEP
STEP
STEP
STEP
STEP

   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
DETAILED VIEWS  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
Cisco UCS X410c M7 Compute Node Front View  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .4
COMPUTE NODE STANDARD CAPABILITIES and FEATURES   . . . . . . . . . . . . . . . 5
CONFIGURING the Cisco UCS X410c M7 Compute Node  . . . . . . . . . . . . . . . . . 8
1 CHOOSE BASE Cisco UCS X410c M7 Compute Node SKU . . . . . . . . . . . . . . . . . . . . . 9
2 CHOOSE CPU(S)   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
3 CHOOSE MEMORY   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
Memory configurations and mixing rules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
4 CHOOSE REAR mLOM ADAPTER   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
5 CHOOSE OPTIONAL REAR MEZZANINE VIC/BRIDGE ADAPTERS  . . . . . . . . . . . . . . . . 19
6 CHOOSE OPTIONAL FRONT MEZZANINE ADAPTER . . . . . . . . . . . . . . . . . . . . . . . . 21
7 CHOOSE OPTIONAL GPU PCIe NODE   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
8 CHOOSE OPTIONAL GPUs   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
9 CHOOSE OPTIONAL DRIVES  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
10 ORDER M.2 SATA SSDs AND RAID CONTROLLER   . . . . . . . . . . . . . . . . . . . . . . . . 26
11 ORDER NVMe BOOT (OPTIONAL)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
12 CHOOSE OPTIONAL TRUSTED PLATFORM MODULE   . . . . . . . . . . . . . . . . . . . . . . 28
13 CHOOSE OPERATING SYSTEM AND VALUE-ADDED SOFTWARE   . . . . . . . . . . . . . . . 29
14 CHOOSE OPTIONAL OPERATING SYSTEM MEDIA KIT . . . . . . . . . . . . . . . . . . . . . . 32
SUPPLEMENTAL MATERIAL  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  33
Simplified Block Diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
System Board   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
UPGRADING or REPLACING CPUs and MEMORY  . . . . . . . . . . . . . . . . . . . . . . 36
LEADERSHIP PERFORMANCE WITH 4TH GEN INTEL® XEON® PROCESSORS   . . .  37
Intel® Xeon® Processors Notices and Disclaimers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
TECHNICAL SPECIFICATIONS  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  39
Dimensions and Weight  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
Environmental Specifications  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
DISCONTINUED EOL PRODUCTS  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  40

2

Cisco UCS X410c M7 Compute Node

OVERVIEW

The Cisco UCS X-Series Modular System simplifies your data center, adapting to the unpredictable needs of 
modern applications while also providing for traditional scale-out and enterprise workloads. It reduces the 
number of server types to maintain, helping to improve operational efficiency and agility as it helps reduce 
complexity. Powered by the Cisco Intersight™ cloud operations platform, it shifts your thinking from 
administrative details to business outcomes with hybrid cloud infrastructure that is assembled from the 
cloud, shaped to your workloads, and continuously optimized.

The Cisco UCS X410c M7 Compute Node is the computing device to integrate into the Cisco UCS X-Series 
Modular System. Up to four compute nodes or two compute nodes and two GPU nodes can reside in the 
7-rack-unit (7RU) Cisco UCS X9508 Server Chassis, offering high performance and efficiency gains for a wide 
range of mission-critical enterprise applications, memory-intensive applications and bare-metal and 
virtualized workloads.

The Cisco UCS X410c M7 Compute Node harnesses the power of the latest 4th Gen Intel® Xeon® Scalable 
Processors (codenamed Sapphire Rapids), offering robust processing capabilities, extensive memory, 
flexible storage, and advanced networking options to meet the demands of diverse and evolving IT 
requirements.

NOTE:  All options listed in the Spec Sheet are compatible with Intersight Managed Mode and UCSM Managed 
Mode configurations. To see the most recent list of components that are supported in Intersight Managed 
Mode, see Supported Systems.

Figure 1 on page 4 shows a front view of the Cisco UCS X410c M7 Compute Node.

Figure 1  Cisco UCS X410c M7 Compute Node 

Front View with Drives

Cisco UCS X410c M7 Compute Node

3

DETAILED VIEWS

DETAILED VIEWS

Cisco UCS X410c M7 Compute Node Front View

Figure 2 shows a front view of the Cisco UCS X410c M7 Compute Node.

Figure 2  Cisco UCS X410c M7 Compute Node Front View (Drives option)

Storage Drives Option

1 
2

3

Power button/LED
System Activity LED

System Health LED

4
5

6

Locater LED/Switch
External Optical Connector (Oculink) that 
supports local console functionality.
Drive Bay slots 1-6

4

Cisco UCS X410c M7 Compute Node

COMPUTE NODE STANDARD CAPABILITIES and FEATURES

COMPUTE NODE STANDARD CAPABILITIES and FEATURES

Table 1 lists the capabilities and features of the base Cisco UCS X410c M7 Compute Node. Details about how 
to configure the compute node for a listed feature or capability (for example, number of processors, drives, 
or amount of memory) are provided in CONFIGURING the Cisco UCS X410c M7 Compute Node on page 8

Table 1   Capabilities and Features 

Capability/Feature

Description

Chassis

CPU

Chipset

Memory

Mezzanine Adapter 
(Rear)
Optional Mezzanine card

The Cisco UCS X410c M7 Compute Node mounts in a Cisco UCS X9508 chassis.

■ Four 4th Gen Intel® Xeon® Scalable Processors (codenamed Sapphire 

Rapids) with up to 60 cores per processor.

■ Each CPU has 8 channels with up to 2 DIMMs per channel, for up to 16 

DIMMs per CPU.

■ UPI Links: Up to Four at 16GT/s

Intel® C741 series chipset

■ 64 total DDR5 DIMM Slots, at up to 4800 MT/s
■ 50% peak bandwidth increase over DDR4-3200, all densities are 

Registered DIMMs (RDIMMs)

■ Up to 16TB with 64 x 256GB DDR5 Memory DIMMs, up to 4800 MT/s, in a 

4-sockets configuration.

■ Cisco UCS Virtual Interface Card (VIC) 15422 can occupy the server's 
mezzanine slot at the bottom rear of the chassis. An included bridge 
card extends this VIC's 100Gbps (4 x 25Gbps) of network connections 
through IFM connectors, bringing the total bandwidth to 100Gbps per VIC 
15420 and 15422 (for a total of 200Gbps per server). In addition to IFM 
connectivity, the VIC 15422 I/O connectors link to Cisco UCS X-Fabric 
technology.

■ Cisco UCS PCI Mezz card for X-Fabric can occupy the server's mezzanine 
slot at the bottom rear of the chassis. This card's I/O connectors link to 
Cisco UCS X-Fabric modules and enable connectivity to the X440p PCIe 
Node.

mLOM virtual interface 
cards

The modular LAN on motherboard (mLOM) cards (the Cisco UCS VIC 15230 
and 15420) is located at the rear of the compute node.

■ Cisco UCS Virtual Interface Card (VIC) 15420 occupies the server's 

Modular LAN on Motherboard (mLOM) slot, enabling up to 50Gbps (2 
x25Gbps) of unified fabric connectivity to each of the chassis Intelligent 
Fabric Modules (IFMs) for 100Gbps connectivity per server.

■ Cisco UCS Virtual Interface Card (VIC) 15230 occupies the server's 

modular LAN on motherboard (mLOM) slot, enabling up to 100 Gbps of 
unified fabric connectivity to each of the chassis Intelligent Fabric 
Modules (IFMs) for 200 Gbps connectivity per server with secure boot 
capability.

Cisco UCS X410c M7 Compute Node

5

COMPUTE NODE STANDARD CAPABILITIES and FEATURES

Table 1   Capabilities and Features (continued)

Capability/Feature

Description

Mezzanine Adapters 
(Front)

One front mezzanine connector that supports:

■ Up to 6 x 2.5-inch SAS and SATA RAID-compatible SSDs

■ Up to 6 x 2.5-inch NVMe PCIe drives

■ A mixture of up to six SAS/SATA or NVMe drives 

Storage

Note: Drives require a RAID or pass-through controller in the front 
mezzanine module slot

■ Up to 6 hot-pluggable, Solid-State Drives (SSDs), or Non-Volatile Memory 

Express (NVMe) 2.5-inch drives with a choice of enterprise-class 
Redundant Array of Independent Disks (RAID) or pass-through controllers 
with four lanes each of PCIe Gen 4 connectivity and 

Additional Storage

Up to 2 M.2 SATA or NVMe drives for flexible boot and local storage 
capabilities as fallows:

Security

Video

■ Dual 80 mm SATA 3.0 M.2 cards on a boot-optimized hardware RAID 

controller

■ Dual 80 mm NVMe cards on a passthrough controller

■ Includes secure boot silicon root of trust FPGA, ACT2 anti-counterfeit 

provisions, and optional Trusted Platform Model (TPM)

The Cisco Integrated Management Controller (CIMC) provides video using the 
Aspeed AST2600 video/graphics controller.

Front Panel Interfaces 

OCuLink console port. Note that an adapter cable is required to connect the 
OCuLink port to the transition serial USB and video (SUV) octopus cable.

Power subsystem 

Power is supplied from the Cisco UCS X9508 chassis power supplies.

Fans 

Integrated in the Cisco UCS X9508 chassis.

Integrated management 
processor

The built-in Cisco Integrated Management Controller enables monitoring of 
Cisco UCS X410c M7 Compute Node inventory, health, and system event logs.

Baseboard Management 
Controller (BMC)

ASPEED Pilot IV

ACPI

Front Indicators

Advanced Configuration and Power Interface (ACPI) 6.5 Standard Supported. 
ACPI states S0 and S5 are supported. There is no support for states S1 
through S4.

■ Power button and indicator
■ System activity indicator
■ Location button and indicator

Management

Cisco Intersight software (SaaS, Virtual Appliance and Private Virtual 
Appliance)

6

Cisco UCS X410c M7 Compute Node

COMPUTE NODE STANDARD CAPABILITIES and FEATURES

Table 1   Capabilities and Features (continued)

Capability/Feature

Description

Fabric Interconnect

Compatible with the Cisco UCS 6454, 64108, 6536, 6664 and 
UCSX-S9108-100G fabric interconnects. 

Chassis

Compatible with the Cisco UCS 9508 X-Series Server Chassis

Cisco UCS X410c M7 Compute Node

7

CONFIGURING the Cisco UCS X410c M7 Compute Node

CONFIGURING the Cisco UCS X410c M7 Compute Node

Follow these steps to configure the Cisco UCS X410c M7 Compute Node:

■ STEP 1 CHOOSE BASE Cisco UCS X410c M7 Compute Node SKU, page 9

■ STEP 2 CHOOSE CPU(S), page 10

■ STEP 3 CHOOSE MEMORY, page 12

■ STEP 4 CHOOSE REAR mLOM ADAPTER, page 15

■ STEP 5 CHOOSE OPTIONAL REAR MEZZANINE VIC/BRIDGE ADAPTERS, page 19

■ STEP 6 CHOOSE OPTIONAL FRONT MEZZANINE ADAPTER, page 21

■ STEP 7 CHOOSE OPTIONAL GPU PCIe NODE, page 22

■ STEP 8 CHOOSE OPTIONAL GPUs, page 23

■ STEP 9 CHOOSE OPTIONAL DRIVES, page 24

■ STEP 10 ORDER M.2 SATA SSDs AND RAID CONTROLLER, page 26

■ STEP 11 ORDER NVMe BOOT (OPTIONAL), page 27

■ STEP 12 CHOOSE OPTIONAL TRUSTED PLATFORM MODULE, page 28

■ STEP 13 CHOOSE OPERATING SYSTEM AND VALUE-ADDED SOFTWARE, page 29

■ STEP 14 CHOOSE OPTIONAL OPERATING SYSTEM MEDIA KIT, page 32

■  SUPPLEMENTAL MATERIAL, page 33

8

Cisco UCS X410c M7 Compute Node

CONFIGURING the Cisco UCS X410c M7 Compute Node

STEP 1 CHOOSE BASE Cisco UCS X410c M7 Compute Node SKU

Top Level ordering product ID (PID) of the Cisco UCS X410c M7 Compute Node as shown inTable 2

Table 2   Top level ordering PID

Product ID (PID)

UCSX-M7-MLB

Description

UCSX M7 Modular Server and Chassis MLB

Verify the product ID (PID) of the Cisco UCS X410c M7 Compute Node as shown in Table 3.

Table 3   PID of the Base Cisco UCS X410c M7 Compute Node  

Product ID (PID)

Description

UCSX-410C-M7

Cisco UCS X410c M7 Compute Node 4S Intel 4th Gen CPU without CPU, memory, 
drive bays, drives, VIC adapter, or mezzanine adapters (ordered as a UCS X9508 
chassis option)

UCSX-410C-M7-U

Cisco UCS X410c M7 Compute Node 4S Intel 4th Gen CPU without CPU, memory, 
drive bays, drives, VIC adapter, or mezzanine adapters (ordered standalone)

A base Cisco UCS X410c M7 Compute Node ordered in Table 3 does not include any components 
or options. They must be selected during product ordering.

Please follow the steps on the following pages to order components such as the following, which 
Please follow the steps on the following pages to order components such as the following, which 
are required in a functional compute node:

■ CPUs

■ Memory

■ Cisco storage RAID or passthrough controller with drives (or blank, for no local drive 

support)

■ SAS, SATA, M.2 or NVMe drives

■ Cisco adapters (such as the 15000 series VIC or Bridge)

Cisco UCS X410c M7 Compute Node

9

CONFIGURING the Cisco UCS X410c M7 Compute Node

STEP 2 CHOOSE CPU(S)

The standard CPU features are:

■ The 4th Gen Intel® Xeon® Scalable Processors (codenamed Sapphire Rapids) are paired with 

Intel® C741 series chipset

■ Up to 60 cores

■ Cache size of up to 112.50 MB

■ Power: Up to 350Watts

■ UPI Links: Up to Four at 16GT/s

With 4th Gen Intel® Xeon® processors, improve performance efficiency for critical workloads 
with the most built-in accelerators. See 4th gen intel xeon benefit pillars in LEADERSHIP 
PERFORMANCE WITH 4TH GEN INTEL® XEON® PROCESSORS.

Select CPUs

The available CPUs are listed in Table 4.

Table 4   Available CPUs

Product ID 

(PID)

8000 Series Processors

UCSX-CPU-I8490H

UCSX-CPU-I8468H

UCSX-CPU-I8460H

UCSX-CPU-I8454H

UCSX-CPU-I8450H

UCSX-CPU-I8444H

6000 Series Processors

UCSX-CPU-I6448H

UCSX-CPU-I6434H

UCSX-CPU-I6418H

UCSX-CPU-I6416H

Cores

Clock Freq

Power

Cache Size

Highest DDR5 DIMM Clock 
Support 

(C)

(GHz)

(W)

(MB)

(MT/s)

60

48

40

32

28

16

32

8

24

18

1.90

2.10

2.20

2.10

2.00

2.90

2.40

3.70

2.10

2.20

350

330

330

270

250

270

250

195

185

165

112.50

105.00

105.00

82.50

75.00

45.00

60.00

22.50

60.00

45.00

4800

4800

4800

4800

4800

4800

4800

4800

4800

4800

10

Cisco UCS X410c M7 Compute Node

CONFIGURING the Cisco UCS X410c M7 Compute Node

Supported Configurations

(1) DRAM configuration:

■ Select four identical CPUs listed in Table 4 on page 10 

(2) Configurations with NVMe PCIe drives:

■ Select four identical CPUs listed in Table 4 on page 10 

(3) Four-CPU Configuration

■ Choose four identical CPUs from any one of the rows of Table 4 Available CPUs, page 10

Cisco UCS X410c M7 Compute Node

11

CONFIGURING the Cisco UCS X410c M7 Compute Node

STEP 3 CHOOSE MEMORY

The Table 5 below describes the main memory DIMM features supported on Cisco UCS X410c M7 
Compute Node.

Table 5   X410c M7 Main Memory Features

Memory DIMM server technologies

Description

Maximum DDR5 memory clock speed

Up to 4800 MT/s 1DPC; Up to 4400 MT/S 2DPC

Operational voltage

DRAM Fab. density

DRAM DIMM type

1.1 Volts

16Gb

RDIMM (Registered DDR5 DIMM)

Memory DIMM organization

Eight memory DIMM channels per CPU; up to 2 DIMMs per channel

Maximum number of DRAM DIMM per 
server

64 (4-Socket)

DRAM DIMM densities and ranks

Refer to Table 6

Maximum system capacity (DRAM 
DIMMs only)

16TB (64x256GB)

12

Cisco UCS X410c M7 Compute Node

Figure 3  Cisco UCS X410c M7 Compute Node Memory Organization 

CONFIGURING the Cisco UCS X410c M7 Compute Node

Cisco UCS X410c M7 Compute Node

13

CONFIGURING the Cisco UCS X410c M7 Compute Node

Select DIMMs and Memory Mirroring

Select the memory configuration and whether or not you want the memory mirroring option. 
The available memory DIMMs and mirroring option are listed in Table 6.

NOTE:  When memory mirroring is enabled, the memory subsystem simultaneously 
writes identical data to two channels. If a memory read from one of the channels 
returns incorrect data due to an uncorrectable memory error, the system 
automatically retrieves the data from the other channel. A transient or soft error in 
one channel does not affect the mirrored data, and operation continues unless there 
is a simultaneous error in exactly the same location on a DIMM and its mirrored 
DIMM. Memory mirroring reduces the amount of memory available to the operating 
system by 50% because only one of the two populated channels provides data.

Table 6   Memory Options for M7 servers with Intel® Xeon® 4th Gen. CPUs

Product ID (PID)

PID Description

Ranks/DIMM

DDR5-5600MT/s PID list1

UCSX-MRX16G1RE3

16GB DDR5-5600 RDIMM 1Rx8 (16Gb)

UCSX-MRX32G1RE3

32GB DDR5-5600 RDIMM 1Rx4 (16Gb)

UCSX-MRX96G2RF3

96GB DDR5-5600 RDIMM 2Rx4 (24Gb)

UCSX-MRX64G2RE3

64GB DDR5-5600 RDIMM 2Rx4 (16Gb)

UCSX-MR128G2RG3

128GB DDR5-5600 RDIMM 2Rx4 (32Gb)

1

1

2

2

2

Memory Mirroring Option

N01-MMIRRORD

Memory mirroring option

Accessories/spare included with Memory configuration:

■ UCS-DDR5-BLK2 is auto included for the unselected DIMMs slots

Notes:

1. Memory will operate at the maximum speed of the Intel 4th Gen. CPU memory controller, ranging from 4000 

MT/s to 4800 MT/s. 

2. Any empty DIMM slot must be populated with a DIMM blank to maintain proper cooling airflow.

Memory configurations and mixing rules

GOLDEN RULE:  Memory on every CPU socket shall be configured identically. Therefore, the 
memory configuration of CPU-4 for a 4-socket system. Unbalanced populations are unsupported.

■ System speed is dependent on the CPU DIMM speed support. Refer to Available CPUs on page 10 for 

DIMM speeds.

■ For full details on supported memory configurations see the M7 Memory Guide

14

Cisco UCS X410c M7 Compute Node

CONFIGURING the Cisco UCS X410c M7 Compute Node

STEP 4 CHOOSE REAR mLOM ADAPTER

The Cisco UCS X410c M7 Compute Node must be ordered with a Cisco VIC mLOM Adapter. The 
adapter is located at the back and can operate in a single-CPU or dual-CPU configuration. 
Table 7 shows the mLOM adapter choices.

Table 7   mLOM Adapters 

Product ID (PID)

Description

Connection type

UCSX-MLV5D200GV2D

Cisco UCS VIC 15230 modular LOM w/Secure Boot X 
Compute Node

UCSX-ML-V5Q50G-D

UCS VIC 15420 4x25G secure boot mLOM for X 
Compute Node

mLOM

mLOM

NOTE:  

■ VIC 15420, or 15230 are supported with both X9108-IFM-25G and 

X9108-IFM-100G. VIC 15420 will operate at 4x 25G with both X9108-IFM-25G and 
X9108-IFM-100G. While, VIC 15230 will operate at 4x 25G with X9108-IFM-25G 
and at 2x 100G with X9108-IFM-100G.

■ The mLOM adapter is mandatory for the Ethernet connectivity to the network 
by means of the IFMs and has x16 PCIe Gen4 connectivity with Cisco UCS VIC 
15420 or x16 Gen4 connectivity with Cisco UCS VIC 15230 towards the CPU1.

■ There is no backplane in the Cisco UCS X9508 chassis; thus, the compute nodes 

directly connect to the IFMs using Orthogonal Direct connectors.

■ Figure 5 shows the location of the mLOM and rear mezzanine adapters on the 
Cisco UCS X410c M7 Compute Node. The bridge adapter connects the mLOM 
adapter to the rear mezzanine adapter.

Cisco UCS X410c M7 Compute Node

15

 
CONFIGURING the Cisco UCS X410c M7 Compute Node

Figure 4  Location of mLOM and Rear Mezzanine Adapters

mLOM Adapter

Bridge Adapter

Rear Mezzanine Adapter

16

Cisco UCS X410c M7 Compute Node

CONFIGURING the Cisco UCS X410c M7 Compute Node

Figure 5 shows the network connectivity from the mLOM out to the 25G IFMs.

Figure 5  Network Connectivity 25G IFMs

To Fabric Interconnect 

To Fabric Interconnect 

UCS X9508 Chassis

IFM-1

IFM-2

Cisco ASIC

Cisco ASIC

KR Lanes

3

2

1

0

KR Lanes

3

2

1

0

IFM OD connectors (1 for each IFM)

UCS X410c mLOM OD connectors (2)

Cisco UCS X410c Compute Node

Cisco ASIC

MAC1

MAC0

Lane 1
Lane 0
Lane 0

Lane 1

25G-KR

25G-KR
25G-KR
25G-KR

R
K
-

G
5
2

R
K
-

G
5
2

R
K
-

G
5
2

1

e
n
a
L

R
K
-

G
5
2

0

e
n
a
L

MAC1

R
K
-

G
5
2

R
K
-

G
5
2

R
K
-

G
5
2

R
K
-

G
5
2

1

e
n
a
L

0

e
n
a
L

MAC0

Cisco ASIC

Mezz Adapter

Bridge Adapter

mLOM Adapter

Cisco UCS X410c M7 Compute Node

17

 
 
 
 
CONFIGURING the Cisco UCS X410c M7 Compute Node

Figure 6 shows the network connectivity from the mLOM out to the 100G IFMs. 

Figure 6  Network Connectivity 100G IFMs

To Fabric Interconnect 

To Fabric Interconnect 

UCS X9508 Chassis

IFM-1

IFM-2

Cisco ASIC

Cisco ASIC

KR Lanes

KR Lanes

IFM OD connectors (1 for each IFM)

UCS X410c mLOM OD connectors (2)

Cisco UCS X410c Compute Node

4
R
K
-

G
0
0
1

4
R
K
-

G
0
0
1

Empty

 Mezzanine Slot

MAC1

Cisco ASIC

MAC0

Bridge Adapter

mLOM Adapter

18

Cisco UCS X410c M7 Compute Node

CONFIGURING the Cisco UCS X410c M7 Compute Node

STEP 5 CHOOSE OPTIONAL REAR MEZZANINE VIC/BRIDGE ADAPTERS

The Cisco UCS X410c M7 Compute Node has one rear mezzanine adapter connector which can 
have a UCS VIC 15422 Mezz card that can be used as a second VIC card on the compute node for 
network connectivity or as a connector to the X440p PCIe node via X-Fabric modules. The same 
mezzanine slot on the compute node can also accommodate a pass-through mezzanine adapter 
for X-Fabric which enables compute node connectivity to the X440p PCIE node. Refer to Table 8 
for supported adapters.

Table 8   Available Rear Mezzanine Adapters  

Product ID(PID)

PID Description

Connector Type

Cisco VIC Card

UCSX-V4-PCIME-D1

UCS PCI Mezz Card for X-Fabric

UCSX-ME-V5Q50G-D

UCS VIC 15422 4x25G secure boot mezz for X Compute 
Node

Rear Mezzanine 
connector on 
motherboard

Rear Mezzanine 
connector on 
motherboard

Cisco VIC Bridge Card2

UCSX-V5-BRIDGE-D

UCS VIC 15000 bridge to connect mLOM and mezz X 
Compute Node 

(This bridge to connect the Cisco VIC 15420 mLOM and 
Cisco VIC 15422 Mezz for the X410c M7 Compute Node)

One connector on 
Mezz card and one 
connector on 
mLOM card

Notes:

1. If this adapter is selected, then two CPUs are required.
2. Included with the Cisco VIC 15422 mezzanine adapter.

NOTE:  The UCSX-V4-PCIME-D rear mezzanine card for X-Fabric has PCIe Gen4 x16 
connectivity towards each CPU1 and CPU2. Additionally, the UCSX-V4-PCIME-D also 
provides two PCIe Gen4 x16 to each X-fabric. This rear mezzanine card enables 
connectivity from the X410c M7 Compute Node to the X440p PCIe node.

Cisco UCS X410c M7 Compute Node

19

CONFIGURING the Cisco UCS X410c M7 Compute Node

Table 9   Throughput Per UCS X410c M7 Server

X410c M7 Compute 
Node 

FI-6536 +  
X9108-IFM-100G

FI-6536/6400 +  
X9108-IFM-25G 

FI-6536 +  
X9108-IFM-25G/100G
or  
FI-6400 + 
X9108-IFM-25G 

FI-6536 +  
X9108-IFM-25G/100G
  or  
FI-6400 + 
X9108-IFM-25G 

X410c 
configuration 

Throughput per 
node 

vNICs needed for 
max BW 

KR connectivity 
from VIC to each 
IFM 

Single vNIC 
throughput on VIC 

Max Single flow BW 
per vNIC 

Single vHBA 
throughput on VIC 

VIC 
15231/15230 

VIC 
15231/15230 

VIC 15420 

VIC 15420 + VIC 
15422 

200G
(100G per IFM) 

100G 
(50G per IFM) 

100G 
(50G per IFM) 

200G
(100G per IFM) 

2 

2 

2 

4 

1x 100GKR 

2x 25GKR 

2x 25GKR 

4x 25GKR 

100G 
(1x100GKR) 

50G 
(2x25G KR) 

50G 
(2x25G KR) 

100G 

100G 

25G 

50G 

25G 

50G 

50G
(2x25G 
KR) 

50G  
(2x25G 
KR) 

25G 

25G 

50G 

50G 

Supported Configurations

■ One of mLOM VIC from Table 7 is always required.

■ If a UCSX-ME-V5Q50G-D rear mezzanine VIC card is installed, a UCSX-V5-BRIDGE-D VIC 

bridge card is included and connects the mLOM to the mezzanine adapter.

■ The UCSX-ME-V5Q50G-D rear mezzanine card has Ethernet connectivity to the IFM using the 
UCSX-V5-BRIDGE-D and has a PCIE Gen4 x16 connectivity towards CPU2. Additionally, the 
UCSX-ME-V5Q50G-D also provides two PCIe Gen4 x16 to each X-fabric.

■ All the connections to Cisco UCS X-Fabric 1 and Cisco UCS X-Fabric 2 are through the Molex 

Orthogonal Direct (OD) connector on the mezzanine card.

■ The rear mezzanine card has 32 x16PCIe lanes to each Cisco UCS X-Fabric for I/O expansion 

to enable resource consumption from the PCIe resource nodes.

20

Cisco UCS X410c M7 Compute Node

 
CONFIGURING the Cisco UCS X410c M7 Compute Node

STEP 6 CHOOSE OPTIONAL FRONT MEZZANINE ADAPTER

The Cisco UCS X410c M7 Compute Node has one front mezzanine connector that can 
accommodate one of the following mezzanine cards:

■ Pass-through controller for up to 6 U.2/U.3 NVMe drives.

■ RAID controller (RAID levels 0, 1, 5, 6, 10, and 50) for 6 SAS/SATA/NVMe drives.

NOTE:  

■ The Cisco UCS X410c M7 Compute Node can be ordered with or without the 

front mezzanine adapter. Refer to Table 10 Available Front Mezzanine 
Adapters

■ Only one Front Mezzanine connector per Server

■ RAID with NVMe drives is only supported with the NVMe U.3 drives as they 

connect to the RAID controller and RAID is not supported with the U.2 NVME 
drives as they directly interface with the server via the PCIe bus.

Table 10  Available Front Mezzanine Adapters  

Product ID(PID)

PID Description

Connector Type

UCSX-X10C-PT4F-D

UCS X10c Compute Pass Through Controller (Front)

Front Mezzanine

UCSX-X10C-RAIDF-D

UCS X10c Compute RAID Controller with LSI 3900 (Front) 
(SAS/SATA and NVMe drives can be mixed)

Front Mezzanine

Cisco UCS X410c M7 Compute Node

21

CONFIGURING the Cisco UCS X410c M7 Compute Node

STEP 7 CHOOSE OPTIONAL GPU PCIe NODE

 Refer to Table 11 for GPU PCIe Node

Table 11  GPU PCIe Node

Product ID(PID)

PID Description

UCSX-440P-D

UCS X-Series Gen4 PCIe node

NOTE:  If UCSX-440P-D is selected, then rear mezzanine is required.

22

Cisco UCS X410c M7 Compute Node

CONFIGURING the Cisco UCS X410c M7 Compute Node

STEP 8 CHOOSE OPTIONAL GPUs

Select GPU Options

NOTE:  

■ Windows Server 2019 is not supported with the Intel FLex 140 & 170 GPUs

■ If UCSX-440P and UCSX-X10C-GPUFM-D are selected, only GPU PID combinations 
UCSX-GPU-FLEX140 + UCSX-GPU-FLX140MZ or UCSX-GPU-L4 + UCSX-GPU-L4-MEZZ 
are allowed.

■ No mixing of GPU types is allowed; UCSX-X10C-GPUFM-D and UCSX-440P-D must 

use the same GPUs.

The available Compute node GPU options are listed in Table 12

Table 12  Available PCIe GPU Card supported on the Compute Node Front Mezz

GPU Product ID (PID) PID Description

UCSX-GPU-T4MEZZ-D NVIDIA T4 GPU PCIE 75W 16GB, MEZZ form factor
UCSX-GPU-L4-MEZZ
UCSX-GPU-FLX140MZ

NVIDIA GPU L4, Gen4x16, 1 Slot, HHHL, 70W 24GB, PCIe
Intel GPU Flex 140, Gen4x8, HHHL, 75W PCIe

The available PCIe node GPU options are listed in Table 13.

Table 13  Available PCIe GPU Cards supported on the PCIe Node

GPU Product ID (PID) PID Description

Maximum number of GPUs per node

UCSX-GPU-A16-D
UCSX-GPU-A40-D
UCSX-GPU-A100-80-D

NVIDIA A16 PCIE 250W 4X16GB
TESLA A40 RTX, PASSIVE, 300W, 48GB
TESLA A100, PASSIVE, 300W, 80GB1
TESLA H100, PASSIVE, 350W, 80GB
UCSX-GPU-H100-80
NVIDIA L40 300W, 48GB wPWR CBL
UCSX-GPU-L40
NVIDIA L40S: 350W, 48GB, 2-slot FHFL GPU
UCSX-GPU-L40S
UCSX-GPU-H100-NVL  NVIDIA H100 NVL, 400W, 94GB, 2-slot FHFL 

GPU

Notes:

1. Required power cables are included with the riser cards in the X440p PCIe node.

2
2
2

2
2
2
2

Cisco UCS X410c M7 Compute Node

23

CONFIGURING the Cisco UCS X410c M7 Compute Node

STEP 9 CHOOSE OPTIONAL DRIVES

The Cisco UCS X410c M7 Compute Node can be ordered with or without drives. The drive options 
are:

■ One to six 2.5-inch small form factor SAS/SATA SSDs or PCIe U.2/U.3 NVMe drives

— Hot-pluggable

— Sled-mounted

Select one or two drives from the list of supported drives available in Table 14.

Table 14  Available Drive Options  

Product ID (PID)

Description

Drive 
Type

Speed  Size

SAS/SATA SSDs1,2,3
Self-Encrypted Drives (SED)
SATA
1.9TB 2.5in Enter Value 6G SATA Micron G2 SSD (SED)
UCSX-SD19TEM2NK9D
SATA
3.8TB 2.5in Enter Value 6G SATA Micron G2 SSD (SED)
UCSX-SD38TEM2NK9D
SATA
7.6TB 2.5in Enter Value 6G SATA Micron G2 SSD (SED)
UCSX-SD76TEM2NK9D
SATA
960GB 2.5in Enter Value 6G SATA Micron G2 SSD (SED)
UCSX-SD960GM2NK9D
SAS
3.8TB 2.5in Enter Value 12G SAS Kioxia G2 SSD (SED-FIPS)
UCSX-SD38TBKANK9D
SAS
UCSX-SD76TBKANK9D
7.6TB 2.5in Enter Value 12G SAS Kioxia G2 SSD (SED-FIPS)
SAS
UCSXSD960GBKNK9-D   960GB 2.5in Enter Value 12G SAS Kioxia G1 SSD(SED-FIPS)
UCSX-SD16TBKANK9D
SAS
Enterprise Value SSDs (Low endurance, supports up to 1X DWPD (drive writes per day)) 
UCSXS960G6I1XEV-D
UCSX-SDB960SA1VD
UCSX-SDB1T9SA1VD
UCSX-SDB3T8SA1VD
UCSX-SDB7T6SA1VD
UCSX-SD38TS1XEV-D
UCSXSD960GS1XEV-D
Enterprise Performance SSDs (high endurance, supports up to 3X DWPD (drive writes per day))
6G
UCSXSD480G63XEP-D

SATA
960GB 2.5 inch Enterprise Value 6G SATA Intel SSD
960GB 2.5in 6G SATA Enter Value 1X Samsung G1PM893A SSD SATA
SATA
1.9TB 2.5in 6G SATA Enter Value 1X Samsung G1PM893A SSD
SATA
3.8TB 2.5in 6G SATA Enter Value 1X Samsung G1PM893A SSD
SATA
7.6TB 2.5in 6G SATA Enter Value 1X Samsung G1PM893A SSD
SAS
3.8TB 2.5in Enter Value 12G SAS Seagate SSD
960GB 2.5in Enter Value 12G SAS Seagate SSD
SAS

1.6TB 2.5in Enter Perf 12G SAS Kioxia G2 SSD (3X SED-FIPS)

6G
6G
6G
6G
12G
12G
12G
12G

6G
6G
6G
6G
6G
12G
12G

SATA

480GB 2.5in Enterprise Performance 6GSATA SSD(3X 
endurance)
1.9TB 2.5in Enterprise performance 6GSATA SSD(3X 
endurance) 
3.8TB 2.5in 15mm Solidigm S4520 Enter Perf 6G SATA 1X SSD SATA
960GB 2.5in 15mm Solidigm S4620 Enter Perf 6G SATA 3X SSD SATA
3.8TB 2.5in 15mm Solidigm S4620 Enter Perf 6G SATA 3X SSD SATA
480GB 2.5in 15mm Solidigm S4620 Enter Perf 6G SATA 3X SSD SATA
1.9TB 2.5in 15mm Solidigm S4620 Enter Perf 6G SATA 3X SSD SATA
480GB 2.5in 15mm Solidigm S4520 Enter Perf 6G SATA 1X SSD SATA
960GB 2.5in 15mm Solidigm S4520 Enter Perf 6G SATA 1X SSD SATA

SATA

6G

6G
6G
6G
6G
6G
6G
6G

UCSX-SD19T63XEP-D

UCSX-SDB3T8OA1V
UCSX-SDB960OA1P
UCSX-SDB3T8OA1P
UCSX-SDB480OA1P
UCSX-SDB1T9OA1P
UCSX-SDB480OA1V
UCSX-SDB960OA1V
NVMe4,5

1.9TB
3.8TB
7.6TB
960GB
3.8TB
7.6TB
960GB
1.6TB

960GB
960GB
1.9TB
3.8TB
7.6TB
3.8TB
960GB

480GB

1.9TB

3.8TB
960GB
3.8TB
480GB
1.9TB
480GB
960GB

24

Cisco UCS X410c M7 Compute Node

CONFIGURING the Cisco UCS X410c M7 Compute Node

Table 14  Available Drive Options (continued) 

Product ID (PID)

Description

Drive 
Type

Speed  Size

UCSX-NVMEXPI400-D

UCSX-NVMEXPI800-D

UCSX-NVMEG4M1536D

UCSX-NVMEG4M1600D
UCSX-NVMEG4M6400D
UCSX-NVMEG4M7680D

UCSX-NVB960M2V

UCSX-NVB1T9M2V

UCSX-NVB3T2M2P
UCSX-NVB3T8M2V

NVMe

NVMe

NVMe

400GB 2.5in U.2 Intel P5800X Optane NVMe Extreme 
Perform SSD
800GB 2.5in U.2Intel P5800X Optane NVMe Extreme Perform 
SSD
15.3TB 2.5in U.3 Micron 7450 NVMe High Perf Medium 
Endurance
1.6TB 2.5in U.3 Micron 7450 NVMe High Perf High Endurance NVMe
6.4TB 2.5in U.3 Micron 7450 NVMe High Perf High Endurance NVMe
NVMe
7.6TB 2.5in U.3 Micron 7450 NVMe High Perf Medium 
Endurance
960GB 2.5in U.3 15mm Micron 7500 Hg Perf Med End 1X 
NVMe
1.9TB 2.5in U.3 15mm Micron 7500 Hg Perf Med End 1X 
NVMe
3.2TB 2.5in U.3 15mm Micron 7500 Hg Perf Hg End 3X NVMe NVMe
NVMe
3.8TB 2.5in U.3 15mm Micron 7500 Hg Perf Med End 1X 
NVMe

NVMe

NVMe

U.2

400GB

U.2

800GB

U.3

15.3TB

U.3
U.3
U.3

1.6TB
6.4TB
7.6TB

U.3

960GB

U.3

1.9TB

U.3
U.3

3.2TB
3.8TB

NOTE:  Cisco uses solid state drives from several vendors. All solid state drives are subject to physical write 
limits and have varying maximum usage limitation specifications set by the manufacturer. Cisco will not replace 
any solid state drives that have exceeded any maximum usage specifications set by Cisco or the manufacturer, as 
determined solely by Cisco.

Notes:

1. SSD drives require the UCSX-X10C-RAIDF-D front mezzanine adapter
2. For SSD drives to be in a RAID group, two identical SSDs must be used in the group.
3. If SSDs are in JBOD Mode, the drives do not need to be identical.
4.  NVMe drives require a front mezzanine the UCSX-X10C-PT4F-D pass through controller or UCSX-X10C-RAIDF-D 

RAID controller.

5.  A maximum of 4 U.2 NVMe drives or 6 U.3 NVMe drives can be ordered with RAID controller.

Cisco UCS X410c M7 Compute Node

25

CONFIGURING the Cisco UCS X410c M7 Compute Node

STEP 10 ORDER M.2 SATA SSDs AND RAID CONTROLLER

■ Cisco 6GB/s SATA Boot-Optimized M.2 RAID Controller (included): Boot-Optimized RAID controller 

(UCSX-M2-HWRD-FPS) for hardware RAID across two SATA M.2 storage modules. The Boot-Optimized RAID 
controller plugs into the motherboard and the M.2 SATA drives plug into the Boot-Optimized RAID 
controller.

NOTE:  

■ The UCSX-M2-HWRD-FPS is auto included with the server configuration

■ The UCSX-M2-HWRD-FPS controller supports RAID 1 and JBOD mode and is available 

only with 240GB and 960GB M.2 SATA SSDs.

■ Cisco IMM is supported for configuring of volumes and monitoring of the controller 

and installed SATA M.2 drives

■ Hot-plug replacement is not supported. The compute node must be powered off to 

replace. 

Table 15  Boot-Optimized RAID controller (auto included)

Product ID (PID)

PID Description

UCSX-M2-HWRD-FPS

UCSX Front panel with M.2 RAID controller for SATA drives

■ Select Cisco M.2 SATA SSDs: Order one or two matching M.2 SATA SSDs. This connector accepts the 

boot-optimized RAID controller (see Table 15). Each boot-optimized RAID controller can accommodate 
up to two SATA M.2 SSDs shown in Table 16.

NOTE:  

■ Each boot-optimized RAID controller can accommodate up to two SATA M.2 SSDs 

shown in Table 16. The boot-optimized RAID controller plugs into the 
motherboard.

■ It is recommended that M.2 SATA SSDs be used as boot-only devices.

■ The SATA M.2 drives can boot in UEFI mode only. Legacy boot mode is not 

supported.

Table 16  M.2 SATA SSDs

Product ID (PID)

PID Description

UCSX-M2-240G-D
UCSX-M2-480G-D
UCSX-M2-960G-D
UCSX-M2480OA1V

240GB 2.5in M.2 SATA Micron G2 SSD
480GB 2.5in M.2 SATA Micron G2 SSD
960GB 2.5in M.2 SATA Micron G2 SSD
480GB M.2 Boot Solidigm S4520 SATA 1X SSD 

26

Cisco UCS X410c M7 Compute Node

CONFIGURING the Cisco UCS X410c M7 Compute Node

STEP 11 ORDER NVMe BOOT

 (OPTIONAL)

Table 17  NVMe BOOT

Product ID (PID)

PID Description

UCSX-M2-PT-FPN

UCSX Front Panel w/M.2 Pass Through Controller for NVME Drv

Table 18  M.2 NVMe

Product ID (PID)

PID Description

UCSX-NVM2-400GB
UCSX-NVM2-960GB

400GB M.2 Boot NVMe 
960GB M.2 Boot NVMe

Cisco UCS X410c M7 Compute Node

27

CONFIGURING the Cisco UCS X410c M7 Compute Node

STEP 12    CHOOSE OPTIONAL TRUSTED PLATFORM MODULE 

Trusted Platform Module (TPM) is a computer chip or microcontroller that can securely store 
artifacts used to authenticate the platform or Cisco UCS X410c M7 Compute Node. These 
artifacts can include passwords, certificates, or encryption keys. A TPM can also be used to 
store platform measurements that help ensure that the platform remains trustworthy. 
Authentication (ensuring that the platform can prove that it is what it claims to be) and 
attestation (a process helping to prove that a platform is trustworthy and has not been 
breached) are necessary steps to ensure safer computing in all environments.

Table 19  Available TPM Option  

Product ID (PID)

Description

UCSX-TPM-002C-D

TPM 2.0, TCG, FIPS140-2, CC EAL4+ Certified, for servers

UCSX-TPM-OPT-OUT1

OPT OUT, TPM 2.0, TCG, FIPS140-2, CC EAL4+ Certified

Notes:

1. Please note Microsoft certification requires a TPM 2.0 for bare-metal or guest VM deployments. Opt-out of the 

TPM 2.0 voids the Microsoft certification.

NOTE:  

■ The TPM module used in this system conforms to TPM v2.0 as defined by the 

Trusted Computing Group (TCG). 

■ TPM installation is supported after-factory. However, a TPM installs with a 

one-way screw and cannot be replaced, upgraded, or moved to another compute 
node. If a Cisco UCS X410c M7 Compute Node with a TPM is returned, the 
replacement Cisco UCS X410c M7 Compute Node must be ordered with a new 
TPM. If there is no existing TPM in the Cisco UCS X410c M7 Compute Node, you 
can install a TPM 2.0. Refer to the following document for Installation location 
and instructions:

https://www.cisco.com/content/en/us/td/docs/unified_computing/ucs/x/hw/x410
c-m7/install/b-cisco-ucs-x410c-m7-install-guide.html

28

Cisco UCS X410c M7 Compute Node

CONFIGURING the Cisco UCS X410c M7 Compute Node

STEP 13 CHOOSE OPERATING SYSTEM AND VALUE-ADDED SOFTWARE

■ Operating System (Table 20)

NOTE:  

■ See this link for operating system guidance: 

https://ucshcltool.cloudapps.cisco.com/public/

Table 20  Operating System 

Product ID (PID)

PID Description

Microsoft Windows Server

MSWS-25-ST16C  

Windows Server 2025 Standard (16 Cores)

MSWS-25-ST16C-NS  

Windows Server 2025 Standard (16 Cores) - No Cisco SVC

MSWS-25-ST24C  

Windows Server 2025 Standard (24 Cores)

MSWS-25-ST24C-NS  

Windows Server 2025 Standard (24 Cores) - No SVC

MSWS-25-DC16C  

Windows Server 2025 Datacenter (16 Core)

MSWS-25-DC16C-NS  

Windows Server 2025 DC (16 Cores) - No SVC

MSWS-25-DC24C  

Windows Server 2025 Datacenter (24 Core)

MSWS-25-DC24C-NS  

Windows Server 2025 Datacenter (24 Core) - No SVC

Red Hat

RHEL-2S2V-1A  

Red Hat Enterprise Linux (1-2 CPU,1-2 VN); 1-Yr Support Req

RHEL-2S2V-3A  

Red Hat Enterprise Linux (1-2 CPU,1-2 VN); 3-Yr Support Req

RHEL-2S2V-5A  

Red Hat Enterprise Linux (1-2 CPU,1-2 VN); 5-Yr Support Req

RHEL-VDC-2SUV-1A  

RHEL for Virt Datacenters (1-2 CPU, Unlim VN) 1 Yr Supp Req

RHEL-VDC-2SUV-3A  

RHEL for Virt Datacenters (1-2 CPU, Unlim VN) 3 Yr Supp Req

RHEL-VDC-2SUV-5A  

RHEL for Virt Datacenters (1-2 CPU, Unlim VN) 5 Yr Supp Req

Red Hat Ent Linux/ High Avail/ Res Strg/ Scal 

RHEL-2S2V-1S  

Red Hat Enterprise Linux (1-2 CPU,1-2 VN); Prem 1Yr SnS Reqd

RHEL-2S2V-3S  

Red Hat Enterprise Linux (1-2 CPU,1-2 VN); Prem 3Yr SnS Reqd

RHEL-2S-HA-1S  

RHEL High Availability (1-2 CPU); Premium 1-yr SnS Reqd

RHEL-2S-HA-3S  

RHEL High Availability (1-2 CPU); Premium 3-yr SnS Reqd

RHEL-2S-RS-1S  

RHEL Resilent Storage (1-2 CPU); Premium 1-yr SnS Reqd

RHEL-2S-RS-3S  

RHEL Resilent Storage (1-2 CPU); Premium 3-yr SnS Reqd

Cisco UCS X410c M7 Compute Node

29

CONFIGURING the Cisco UCS X410c M7 Compute Node

Table 20  Operating System (continued)

Product ID (PID)

PID Description

RHEL-VDC-2SUV-1S  

RHEL for Virt Datacenters (1-2 CPU, Unlim VN) 1 Yr SnS Reqd

RHEL-VDC-2SUV-3S  

RHEL for Virt Datacenters (1-2 CPU, Unlim VN) 3 Yr SnS Reqd

Red Hat SAP

RHEL-SAP-2S2V-1S  

RHEL for SAP Apps (1-2 CPU, 1-2 VN); Prem 1-Yr SnS Reqd

RHEL-SAP-2S2V-3S  

RHEL for SAP Apps (1-2 CPU, 1-2 VN); Prem 3-Yr SnS Reqd

RHEL-SAPSP-3S

RHEL SAP Solutions Premium - 3 Years

RHEL-SAPSS-3S

RHEL SAP Solutions Standard - 3 Years

SUSE

SLES-2S2V-1A

SLES-2S2V-3A

SLES-2S2V-5A

SUSE Linux Enterprise Svr (1-2 CPU,1-2 VM); 1-Yr Support Req

SUSE Linux Enterprise Svr (1-2 CPU,1-2 VM); 3-Yr Support Req

SUSE Linux Enterprise Svr (1-2 CPU,1-2 VM); 5-Yr Support Req

SLES-2S-LP-1A

SUSE Linux Live Patching Add-on (1-2 CPU); 1yr Support Req

SLES-2S-LP-3A

SUSE Linux Live Patching Add-on (1-2 CPU); 3yr Support Req

SLES-2SUVM-1A

SUSE Linux Enterprise Svr (1-2 CPU,Unl VM) LP; 1Y Supp Req

SLES-2SUVM-3A

SUSE Linux Enterprise Svr (1-2 CPU,Unl VM) LP; 3Y Supp Req

SLES-2SUVM-5A

SUSE Linux Enterprise Svr (1-2 CPU,Unl VM) LP; 5Y Supp Req

SLES-2S2V-1S 

SUSE Linux Enterprise Svr (1-2 CPU,1-2 VM); Prio 1-Yr SnS

SLES-2S2V-3S 

SUSE Linux Enterprise Svr (1-2 CPU,1-2 VM); Prio 3-Yr SnS

SLES-2S2V-5S 

SUSE Linux Enterprise Svr (1-2 CPU,1-2 VM); Prio 5-Yr SnS

SLES-2S-HA-1S

SUSE Linux High Availability Ext (1-2 CPU); 1yr SnS

SLES-2S-HA-3S  

SUSE Linux High Availability Ext (1-2 CPU); 3yr SnS

SLES-2S-HA-5S  

SUSE Linux High Availability Ext (1-2 CPU); 5yr SnS

SLES-2S-GC-1S  

SUSE Linux GEO Clustering for HA (1-2 CPU); 1yr Sns

SLES-2S-GC-3S  

SUSE Linux GEO Clustering for HA (1-2 CPU); 3yr SnS

SLES-2S-GC-5S  

SUSE Linux GEO Clustering for HA (1-2 CPU); 5yr SnS

SLES-2S-LP-1S  

SUSE Linux Live Patching Add-on (1-2 CPU); 1yr SnS Required

SLES-2S-LP-3S  

SUSE Linux Live Patching Add-on (1-2 CPU); 3yr SnS Required

SLES-2SUVM-1S  

SUSE Linux Enterprise Svr (1-2 CPU,Unl VM) LP; Prio 1Y SnS

SLES-2SUVM-3S  

SUSE Linux Enterprise Svr (1-2 CPU,Unl VM) LP; Prio 3Y SnS

30

Cisco UCS X410c M7 Compute Node

CONFIGURING the Cisco UCS X410c M7 Compute Node

Table 20  Operating System (continued)

Product ID (PID)

PID Description

SLES-2SUVM-5S  

SUSE Linux Enterprise Svr (1-2 CPU,Unl VM) LP; Prio 5Y SnS

SLES and SAP

SLES-SAP-2S2V-1S

SLES for SAP Apps (1-2 CPU, 1-2 VM); Priority 1-Yr SnS

SLES-SAP-2S2V-3S

SLES for SAP Apps (1-2 CPU, 1-2 VM); Priority 3-Yr SnS

SLES-SAP-2S2V-5S 

SLES for SAP Apps (1-2 CPU, 1-2 VM); Priority 5-Yr SnS

SLES-SAP-2S2V-1A

SLES for SAP Apps w/ HA (1-2 CPU, 1-2 VM); 1-Yr Support Reqd

SLES-SAP-2S2V-3A

SLES for SAP Apps w/ HA (1-2 CPU, 1-2 VM); 3-Yr Support Reqd

SLES-SAP-2S2V-5A

SLES for SAP Apps w/ HA (1-2 CPU, 1-2 VM); 5-Yr Support Reqd

Cisco UCS X410c M7 Compute Node

31

CONFIGURING the Cisco UCS X410c M7 Compute Node

STEP 14 CHOOSE OPTIONAL OPERATING SYSTEM MEDIA KIT

Select the optional operating system media listed in Table 21.

Table 21  OS Media  

Product ID (PID)

PID Description

MSWS-19-ST16CD-RM

Windows Server 2019 Stan (16 Cores/2 VMs) Rec Media DVD Only

MSWS-19-DC16CD-RM

Windows Server 2019 DC (16Cores/Unlim VM) Rec Media DVD Only

MSWS-22-ST16CD-RM

Windows Server 2022 Stan (16 Cores/2 VMs) Rec Media DVD Only

MSWS-22-DC16CD-RM

Windows Server 2022 DC (16Cores/Unlim VM) Rec Media DVD Only

32

Cisco UCS X410c M7 Compute Node

SUPPLEMENTAL MATERIAL

SUPPLEMENTAL MATERIAL

Simplified Block Diagram

A simplified block diagram of the Cisco UCS X410c M7 Compute Node system board is shown in Figure 7.

Figure 7  Cisco UCS X410c M7 Compute Node Simplified Block Diagram (IFMs 25G with Drives)

Cisco UCS X410c M7 Compute Node

33

SUPPLEMENTAL MATERIAL

Figure 8  Cisco UCS X410c M7 Compute Node Simplified Block Diagram (IFMs 100G with Drives)

34

Cisco UCS X410c M7 Compute Node

System Board

A top view of the Cisco UCS X410c M7 Compute Node system board is shown in Figure 9.

Figure 9  Cisco UCS X410c M7 Compute Node System Board

SUPPLEMENTAL MATERIAL

1

2

3

4

Front mezzanine module slot

CPU 1 slot

DIMM slots

CPU 2 slot

5

6

7

8

Motherboard USB connector

Rear mezzanine slot, which supports X-Series 
mezzanine cards, such as VIC 15422.

Bridge Card slot, which connects 8 rear 
mezzanine slot and the mLOM/VIC slot

mLOM/VIC slot that supports zero or one Cisco 
VIC or Cisco X-Series 100 Gbps mLOM

Please refer to the Cisco UCS X410c M7 Compute Node Installation Guide for installation 
procedures.

Cisco UCS X410c M7 Compute Node

35

 
UPGRADING or REPLACING CPUs and MEMORY

UPGRADING or REPLACING CPUs and MEMORY

■ Refer to Cisco UCS X410c M7 Server Installation and Service Guide to upgrading or replacing the CPUs

■ Refer to Cisco UCS X410c M7 Server Installation and Service Guide to upgrading or replacing the Memory

36

Cisco UCS X410c M7 Compute Node

LEADERSHIP PERFORMANCE WITH 4TH GEN INTEL® XEON® PROCESSORS

LEADERSHIP PERFORMANCE WITH 4TH GEN INTEL® 
XEON® PROCESSORS

Improve performance efficiency for critical workloads with the most built-in accelerators.

Availability of accelerators varies depending on SKU. Visit the 4th Gen Intel Product Information page for 
additional product details.

See Intel® Xeon® Processors Notices and Disclaimers in next page.

Notes:

1. Compared to prior generation Intel® Xeon® processor. See [G1] at intel.com/processorclaims: 4th Gen 
Intel® Xeon® Scalable processors. Results may vary.

2. Compared to prior generation Intel® Xeon® processor. See [A16] and [A17] at intel.com/processorclaims: 
4th Gen Intel® Xeon® Scalable processors. Results may vary.

3. Comparing benefits transitioning from Intel® Xeon® 4110 to Intel® Xeon® 5420+. See [E11] at 
intel.com/processorclaims: 4th Gen Intel® Xeon® Scalable processors. Results may vary.

4. Compared to prior generation Intel® Xeon® processor. See [E1] at intel.com/processorclaims: 4th Gen 
Intel® Xeon® Scalable processors. Results may vary.

Cisco UCS X410c M7 Compute Node

37

LEADERSHIP PERFORMANCE WITH 4TH GEN INTEL® XEON® PROCESSORS

Intel® Xeon® Processors Notices and Disclaimers

■ Performance varies by use, configuration and other factors. 

■ Performance results are based on testing as of dates shown in configurations and may not reflect all 
publicly available  updates.  See backup for configuration details.  No product or component can be 
absolutely secure. 

■ Your costs and results may vary. 

■ Intel technologies may require enabled hardware, software or service activation.

■ Intel does not control or audit third-party data. You should consult other sources to evaluate 

accuracy.

■ © Intel Corporation. Intel, the Intel logo, and other Intel marks are trademarks of Intel Corporation 

or its subsidiaries. Other names and brands may be claimed as the property of others.

■ Intel contributes to the development of benchmarks by participating in, sponsoring, and/or 

contributing technical support to various benchmarking groups, including the BenchmarkXPRT 
Development Community administered by Principled Technologies.

38

Cisco UCS X410c M7 Compute Node

TECHNICAL SPECIFICATIONS

TECHNICAL SPECIFICATIONS

Dimensions and Weight

Table 22  Cisco UCS X410c M7 Compute Node Dimensions and Weight  

Parameter

Value

Height

3.67 inches (93.22 mm)

Width

Depth

11.28 inches (286.52 mm)

23.8 inches (604.52 mm)

Weight 

The weight depends on the components installed:

■ Minimally configured compute node weight: 25 lb (11.34 kg)

■ Fully configured compute node weight: 42 lb (19.05 kg)

Environmental Specifications

Table 23  Cisco UCS X410c M7 Compute Node Environmental Specifications  

Parameter

Value

Operating temperature

Supported operating temperatures depend on the compute node's memory:

■ For 256GB DDR5 DIMMs: 50° to 89.6° F (10° to 32° C) at 0 to 10,000

■ All other memory configurations: 50° to 95° F (10° to 35° C) at 0 to 

10,000

Non-operating temperature

-40° to 149°F (–40° to 65°C)

Operating humidity

5% to 90% noncondensing

Non-operating humidity

5% to 93% noncondensing

Operating altitude

0 to 10,000 ft (0 to 3000m); maximum ambient temperature decreases by 
1°C per 300m

Non-operating altitude

40,000 ft (12,000m)

For configuration-specific power specifications, use the Cisco UCS Power Calculator at:

http://ucspowercalc.cisco.com

Cisco UCS X410c M7 Compute Node

39

DISCONTINUED EOL PRODUCTS

DISCONTINUED EOL PRODUCTS

Below is the list of parts were previously available for this product and are no longer sold. Please refer to 
the EOL Bulletin Links via table below to determine if still supported.

Table 24

  EOS

Product ID

Description

EOL/EOS link

Drives
UCSX-M2-240GB-D

240GB 2.5in M.2 SATA Micron G1 
SSD

UCSX-M2-960GB-D

960GB 2.5in M.2 SATA Micron G1 
SSD

UCSX-SD76TM1XEV-D

7.6TB 2.5in Enter Value 6G SATA 
Micron G1 SSD

UCSXSD240GM1XEV-D

240GB 2.5in Enter Value 6G 
SATA Micron G1 SSD

UCSXSD480GM1XEV-D

480 GB 2.5in Enter Value 6G 
SATA Micron G1 SSD

UCSX-SD16TM1XEV-D

1.6TB 2.5in Enter Value 6G SATA 
Micron G1 SSD

UCSX-SD38TM1XEV-D

3.8TB 2.5in Enter Value 6G SATA 
Micron G1 SSD

UCSX-NVME-W6400-D

UCSX-SD32TK3XEP-D

6.4TB 2.5in U.2 WD SN840 
NVMe Extreme Perf. High 
Endurance  
3.2TB 2.5in Enter Perf 12G SAS 
Kioxia G1 SSD (3X)

UCSX-SD38TK1XEV-D

3.8TB 2.5in Enter Value 12G 
SAS Kioxia G1 SSD

UCSX-SD76TBKNK9-D

7.6TB 2.5in Enter Value 12G 
SAS Kioxia G1 SSD (SED-FIPS)

UCSX-SD76TK1XEV-D

7.6TB 2.5in Enter Value 12G 
SAS Kioxia G1 SSD

UCSXNVMEI4I6400-D

6.4TB 2.5in U.2 Intel P5600 
NVMe High Perf High Endurance

UCSX-SD16TBKNK9-D

1.6TB 2.5in Enter Perf 12G SAS 
Kioxia G1 SSD (3X SED-FIPS)

https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-c-series-rack-serv
ers/unified-computing-accessories-eol.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-c-series-rack-serv
ers/unified-computing-accessories-eol.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-c-series-rack-serv
ers/unified-computing-accessories-eol.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-c-series-rack-serv
ers/unified-computing-accessories-eol.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-c-series-rack-serv
ers/unified-computing-accessories-eol.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-c-series-rack-serv
ers/unified-computing-accessories-eol.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-c-series-rack-serv
ers/unified-computing-accessories-eol.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-c-series-rack-serv
ers/unified-computing-accessories-eol.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-b-series-blade-ser
vers/select-ucs-accessories-eol.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-b-series-blade-ser
vers/select-ucs-accessories-eol.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-b-series-blade-ser
vers/select-ucs-accessories-eol.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-b-series-blade-ser
vers/select-ucs-accessories-eol.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-b-series-blade-ser
vers/select-ucs-accessories-eol.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-b-series-blade-ser
vers/select-ucs-accessories-eol.html

40

Cisco UCS X410c M7 Compute Node

Table 24

  EOS

UCSX-SD16TK3XEP-D

1.6TB 2.5in Enter Perf 12G SAS 
Kioxia G1 SSD (3X)

UCSX-SD19TK1XEV-D

1.9TB 2.5in Enter Value 12G 
SAS Kioxia G1 SSD

UCSXSD38T6S1XEV-D

3.8TB 2.5in Enter Value 6G SATA 
Samsung SSD

UCSXSD38T6S1XEV-D

3.8TB 2.5in Enter Value 6G SATA 
Samsung SSD

UCSXS960G6S1XEV-D

960GB 2.5 inch Enterprise Value 
6G SATA Samsung SSD

UCSX-SD19TS1XEV-D

1.9TB 2.5v Enter Value 12G SAS 
Seagate SSD

UCSX-ML-V5D200G-D

Cisco VIC 15231 2x 100G mLOM 
X-Series

UCSX-SD38TBKNK9-D

3.8TB 2.5in Enter Value 12G 
SAS Kioxia G1 SSD (SED-FIPS)

UCSX-M2-I480GB-D

480GB SATA M.2 SSD

UCSXSD960GK1XEV-D

960GB 2.5 inch Enterprise Value 
12G SAS SSD

UCSX-NVMEG4-M960D

960GB 2.5in U.3 15mm P7450 
Hg Perf Med End NVMe

UCSX-NVMEG4M1920D

1.9TB 2.5in U.3 15mm P7450 Hg 
Perf Med End NVMe

UCSX-NVMEG4M3200D

3.2TB 2.5in U.3 15mm P7450 Hg 
Perf Hg End NVMe (3X)

UCSX-NVMEG4M3840D

3.8TB 2.5in U.3 15mm P7450 Hg 
Perf Med End NVMe

UCSX-MRX16G1RE1

16GB DDR5-4800 RDIMM 1Rx8 
(16Gb)

UCSX-MRX32G1RE1

32GB DDR5-4800 RDIMM 1Rx4 
(16Gb)

UCSX-MRX64G2RE1

64GB DDR5-4800 RDIMM 2Rx4 
(16Gb)

DISCONTINUED EOL PRODUCTS

https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-b-series-blade-ser
vers/select-ucs-accessories-eol.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-b-series-blade-ser
vers/select-ucs-accessories-eol.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-c-series-rack-serv
ers/select-ucs-hci-accessories-eol.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-c-series-rack-serv
ers/select-ucs-hci-accessories-eol.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-c-series-rack-serv
ers/select-ucs-accessories-eol15371.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-c-series-rack-serv
ers/select-ucs-hci-accessories-eol.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-c-series-rack-serv
ers/select-ucs-ucsx-accessories-eol.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-c-series-rack-serv
ers/select-ucs-drives-storage-controllers-eol.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-c-series-rack-serv
ers/select-ucs-accessories-eol15502.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-c-series-rack-serv
ers/select-ucs-accessories-eol15502.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-c-series-rack-serv
ers/select-ucs-ucsx-hci-accessories-eol15818.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-c-series-rack-serv
ers/select-ucs-ucsx-hci-accessories-eol15818.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-c-series-rack-serv
ers/select-ucs-ucsx-hci-accessories-eol15818.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-c-series-rack-serv
ers/select-ucs-ucsx-hci-accessories-eol15818.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-c-series-rack-serv
ers/ucs-accessories_eol.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-c-series-rack-serv
ers/ucs-accessories_eol.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-c-series-rack-serv
ers/ucs-accessories_eol.html

Cisco UCS X410c M7 Compute Node

41

DISCONTINUED EOL PRODUCTS

Table 24

  EOS

UCSX-MR128G4RE1

128GB DDR5-4800 RDIMM 4Rx4 
(16Gb)

UCSXS480G6I1XEV-D

480 GB 2.5 inch Enterprise 
Value 6G SATA Intel SSD

https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-c-series-rack-serv
ers/ucs-accessories_eol.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-c-series-rack-serv
ers/select-ucs-accessories-eol15502.html

42

Cisco UCS X410c M7 Compute Node

