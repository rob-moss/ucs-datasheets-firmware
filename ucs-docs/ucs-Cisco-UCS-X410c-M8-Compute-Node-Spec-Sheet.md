# Cisco UCS X410c M8 Compute Node Spec Sheet

| | |
|---|---|
| **URL Title** | Cisco UCS X410c M8 Compute Node Spec Sheet |
| **URL** | https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-x-series-modular-system/x410cm8-specsheet.pdf |
| **Long URL** |  |
| **HTML Title** |  |
| **Source file** | `ucs-docs-raw/pdf/x410cm8-specsheet.pdf` |
| **File type** | PDF |
| **Fetched on** | 2026-03-25 11:36:50 |

---

Specification Sheet

Cisco UCS X410c M8 
Compute Node

A printed version of this document is only a copy 
and not necessarily the latest version. Refer to 
the following link for the latest released version:

https://www.cisco.com/c/en/us/products/servers-unified-
computing/ucs-x-series-modular-system/datasheet-
listing.html

CISCO SYSTEMS
170 WEST TASMAN DR.
SAN JOSE, CA, 95134
WWW.CISCO.COM

PUBLICATION HISTORY

REV A.02

DECEMBER 05, 2025



OVERVIEW  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
DETAILED VIEWS  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
Cisco UCS X410c M8 Compute Node Front View  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .4
COMPUTE NODE STANDARD CAPABILITIES and FEATURES   . . . . . . . . . . . . . . . 5
CONFIGURING THE CISCO UCS X410C M8 COMPUTE NODE  . . . . . . . . . . . . . . . 7
1 CHOOSE BASE SYSTEM  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
STEP
2 CHOOSE CPU(S)   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
STEP
STEP
3 CHOOSE MEMORY   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
Memory configurations and mixing rules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
4 CHOOSE OPTIONAL FRONT MEZZANINE ADAPTER . . . . . . . . . . . . . . . . . . . . . . . . 13
STEP
5 CHOOSE REAR MEZZANINE ADAPTER  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
STEP
6 CHOOSE OPTIONAL DRIVES  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
STEP
7 CHOOSE M.2 MODULE SSDs AND OPTIONAL DRIVES . . . . . . . . . . . . . . . . . . . . . . . 21
STEP
8 CHOOSE OPTIONAL TRUSTED PLATFORM MODULE  . . . . . . . . . . . . . . . . . . . . . . . 23
STEP
9 CHOOSE OPERATING SYSTEM AND VALUE-ADDED SOFTWARE  . . . . . . . . . . . . . . . . 24
STEP
10 CHOOSE OPTIONAL OPERATING SYSTEM MEDIA KIT . . . . . . . . . . . . . . . . . . . . . . 27
STEP
SUPPLEMENTAL MATERIAL  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  28
Simplified Block Diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
System Board   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
UPGRADING or REPLACING CPUs and MEMORY  . . . . . . . . . . . . . . . . . . . . . . 31
TECHNICAL SPECIFICATIONS  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  32
Dimensions and Weight  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
Environmental Specifications  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32

2

Cisco UCS X410c M8 Compute Node

OVERVIEW

OVERVIEW

The Cisco UCS X-Series Modular System simplifies your data center, adapting to the unpredictable needs of 
modern applications while also providing for traditional scale-out and enterprise workloads. It reduces the 
number of server types to maintain, helping to improve operational efficiency and agility as it helps reduce 
complexity. Powered by the Cisco Intersight™ cloud operations platform, it shifts your thinking from 
administrative details to business outcomes with hybrid cloud infrastructure that is assembled from the 
cloud, shaped to your workloads, and continuously optimized.

The Cisco UCS X410c M8 Compute Node is the second-generation of 4-socket compute node purpose-built 
for the Cisco UCS X-Series Modular System. Powered by Intel® Xeon® 6 Scalable Processors, it delivers 
outstanding performance and efficiency for a wide range of mission-critical enterprise applications, 
memory-intensive workloads, and both bare-metal and virtualized environments. Up to four X410c M8 
Compute Nodes can reside in the 7-Rack-Unit (7RU) Cisco UCS X9508 Server Chassis, offering you the 
flexibility to adapt to diverse workloads.

The Cisco UCS X410c M8 Compute Node harnesses the power of the latest Intel® Xeon® 6 Scalable 
Processors, offering robust processing capabilities, extensive memory, flexible storage, and advanced 
networking options to meet the demands of diverse and evolving IT requirements. Refer to COMPUTE NODE 
STANDARD CAPABILITIES and FEATURES on page 5.

NOTE:  All options listed in the Spec Sheet are compatible with Intersight Managed Mode and UCSM Managed 
Mode configurations. To see the most recent list of components that are supported in Intersight Managed 
Mode, see Supported Systems.

Figure 1 shows a front view of the Cisco UCS X410c M8 Compute Node.

Figure 1  Cisco UCS X410c M8 Compute Node 

Front View with Drives

Cisco UCS X410c M8 Compute Node

3

DETAILED VIEWS

DETAILED VIEWS

Cisco UCS X410c M8 Compute Node Front View

Figure 2 shows a front view of the Cisco UCS X410c M8 Compute Node.

Figure 2  Cisco UCS X410c M8 Compute Node Front View

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
External Optical Connector (OCuLink) that 
supports local console functionality.
Drive Bay slots 1-6

4

Cisco UCS X410c M8 Compute Node

COMPUTE NODE STANDARD CAPABILITIES and FEATURES

COMPUTE NODE STANDARD CAPABILITIES and FEATURES

Table 1 lists the capabilities and features of the base Cisco UCS X410c M8 Compute Node. Details about how 
to configure the compute node for a listed feature or capability (for example, number of processors, disk 
drives, or amount of memory) are provided in CONFIGURING THE CISCO UCS X410C M8 COMPUTE NODE on 
page 7

Table 1   Capabilities and Features 

Capability/Feature

Description

Chassis

CPU

Memory

Rear Mezzanine Adapter 
(Optional)

The Cisco UCS X410c M8 Compute Node mounts in a Cisco UCS X9508 chassis.

Four Intel® Xeon® 6 Scalable Processors with up to 86 cores per 
processor
Each CPU has 8 channels with up to 2 DIMMs per channel, for up to 16 
DIMMs per CPU.

■ UPI Links: Up to 3 at up to 24GT/s

64 total DDR5-6400 MT/s DIMM slots (16 per CPU) with Intel® Xeon® 6 
Scalable Processors

■ Up to 16TB of main memory with 64x 256 GB DDR5-6400 Memory DIMMs

Cisco UCS 5th Gen VIC 15422 can occupy the server's mezzanine slot at 
the bottom rear of the chassis. An included bridge card extends this VIC's 
two 50 Gbps of network connections through IFM connectors, bringing 
the total bandwidth to 100 Gbps per fabric (for a total of 200 Gbps per 
server) with secure boot capability.

mLOM virtual interface 
cards

The modular LAN on motherboard (mLOM) cards is located at the rear of the 
compute node.

Cisco UCS VIC (Virtual Interface Card) 15420 occupies the server's 
modular LAN on motherboard (mLOM) slot, enabling up to 50 Gbps (two 
25Gbps) of unified fabric connectivity to each of the chassis’ Intelligent 
Fabric Modules (IFMs) for 100 Gbps connectivity per server with secure 
boot technology.
Cisco UCS VIC 15230 occupies the server's modular LAN on motherboard 
(mLOM) slot, enabling up to 100 Gbps of unified fabric connectivity to 
each of the chassis’ Intelligent Fabric Modules (IFMs) for 100 Gbps 
connectivity per server with secure boot technology.

Front Mezzanine 
Adapters

One front mezzanine connector that supports:

EDSFF E3.S NVMe pass-through controller

■ NVMe pass-through controller for U.3 NVMe drives

RAID controller with 4GB cache for SSD and mix of SSD and NVMe drives

■ No front mezzanine

Note: Drives require a RAID or pass-through controller in the front 
mezzanine module slot

Cisco UCS X410c M8 Compute Node

5

■
■
■
■
■
■
■
■
COMPUTE NODE STANDARD CAPABILITIES and FEATURES

Table 1   Capabilities and Features (continued)

Capability/Feature

Description

Storage

■ Up to nine hot-pluggable EDSFF E3.S NVMe drives with a new 

pass-through front mezzanine controller option

■ Up to six hot-pluggable, solid-state drives (SSDs), or non-volatile 

memory express (NVMe) 2.5-inch drives with a choice of enterprise-class 
redundant array of independent disks (RAIDs).

■ Up to two M.2 SATA drives or two M.2 NVMe drives for flexible boot and 

local storage capabilities.

The server supports an optional Trusted Platform Module (TPM). Additional 
features include a secure boot FPGA and ACT2 anti-counterfeit provisions.

The Cisco Integrated Management Controller (CIMC) provides video using the 
ASPEED AST2600 video/graphics controller.

Security

Video

Front Panel Interfaces 

OCuLink console port. Note that an adapter cable is required to connect the 
OCuLink port to the transition serial USB and video (SUV) octopus cable.

Power subsystem 

Power is supplied from the Cisco UCS X9508 chassis power supplies. The 
Cisco UCS X410c M8 Compute Node consumes a maximum of 2500 W.

Fans 

Integrated in the Cisco UCS X9508 chassis.

Integrated management 
processor

The built-in Cisco Integrated Management Controller enables monitoring of 
Cisco UCS X410c M8 Compute Node inventory, health, and system event logs.

Firmware standards

■ UEFI Spec       2.9

ACPI               6.5

SMBIOS Ver     3.7

Baseboard Management 
Controller (BMC)

ASPEED Pilot IV

ACPI

Front Indicators

Advanced Configuration and Power Interface (ACPI) 6.5 Standard Supported. 
ACPI states S0 and S5 are supported. There is no support for states S1 
through S4.

Power button and indicator
System activity indicator
Location button and indicator

Management

Cisco Intersight software (SaaS, Virtual Appliance and Private Virtual 
Appliance)

Fabric Interconnect

Compatible with the Cisco UCS 6454, 64108, 6536, 6664 and 
UCSX-S9108-100G fabric interconnects. 

6

Cisco UCS X410c M8 Compute Node

■
■
■
■
■
CONFIGURING THE CISCO UCS X410C M8 COMPUTE NODE

CONFIGURING THE CISCO UCS X410C M8 COMPUTE NODE

Follow these steps to configure the Cisco UCS X410c M8 Compute Node:

STEP 1 CHOOSE BASE SYSTEM, page 8

STEP 2 CHOOSE CPU(S), page 9

STEP 3 CHOOSE MEMORY, page 10

STEP 4 CHOOSE OPTIONAL FRONT MEZZANINE ADAPTER, page 13

STEP 5 CHOOSE REAR MEZZANINE ADAPTER, page 14

STEP 6 CHOOSE OPTIONAL DRIVES, page 19

STEP 7 CHOOSE M.2 MODULE SSDs AND OPTIONAL DRIVES, page 21

STEP 8 CHOOSE OPTIONAL TRUSTED PLATFORM MODULE, page 23

STEP 9 CHOOSE OPERATING SYSTEM AND VALUE-ADDED SOFTWARE, page 24

STEP 10 CHOOSE OPTIONAL OPERATING SYSTEM MEDIA KIT, page 27

 SUPPLEMENTAL MATERIAL, page 28

Cisco UCS X410c M8 Compute Node

7

■
■
■
■
■
■
■
■
■
■
■
CONFIGURING THE CISCO UCS X410C M8 COMPUTE NODE

STEP 1 CHOOSE BASE SYSTEM

Select MLB

Top-level ordering product ID (PID) is shown in Table 2

Table 2   Top-Level Major Line Bundle ordering PIDs (MLB)

Product ID (PID)

Description

UCSX-M8-MLB

UCSX M8 Modular Server and Chassis MLB

Select Base Compute Node

Base compute node shown in Table 3.

CAUTION:  This product may not be purchased outside of the approved bundles (must be 
ordered under the MLB)

Table 3   PID of the Base Compute Node  

Product ID (PID)

Description

UCSX-410C-M8

UCSX 410c M8 Compute Node without CPU, Memory, Storage, VIC adapter, or 
mezzanine adapters.

(ordered as a UCS X9508 chassis option)

UCSX-410C-M8-U

(standalone)

UCSX 410c M8 Compute Node without CPU, Memory, Storage, VIC adapter, or 
mezzanine adapters.

(ordered standalone)

NOTE:  

A base Cisco UCS X410c M8 Compute Node ordered in Table 3 does not include any 
components or options. These must be selected during product ordering.

Please follow the CONFIGURING THE CISCO UCS X410C M8 COMPUTE NODE on page 7, 
which are required in a functional compute node.

8

Cisco UCS X410c M8 Compute Node

■
■
CONFIGURING THE CISCO UCS X410C M8 COMPUTE NODE

STEP 2 CHOOSE CPU(S)

The standard CPU features are:

Up to 86 cores

Cache size of up to 336 MB

Power: Up to 350 Watts

UPI Links: Up to 3 at up to 24GT/s

Select CPUs

The available CPUs are listed in Table 4.

Table 4   Available Intel® Xeon® 6 Scalable CPUs

Product ID 

Cores

Clock Frequency

Power

Cache Size

Highest DDR5 
DIMM Clock 

(PID)

UCSX-CPU-I6788P

UCSX-CPU-I6768P

UCSX-CPU-I6748P

UCSX-CPU-I6738P

UCSX-CPU-I6728P

UCSX-CPU-I6724P

UCSX-CPU-I6714P

(C)

86

64

48

32

24

16

8

Approved Configurations

(GHz)

2.00

2.40

2.50

2.90

2.70

3.60

4.00

(W)

350

330

300

270

210

210

165

(MB)

(MT/s)

336

336

192

144

144

72

48

6400

6400

6400

6400

6400

6400

6400

— For all configurations (DRAM and NVMe PCIe drives), select four identical CPUs listed 

in Table 4

Cisco UCS X410c M8 Compute Node

9

■
■
■
■
CONFIGURING THE CISCO UCS X410C M8 COMPUTE NODE

STEP 3 CHOOSE MEMORY

The Table 5 below describes the main memory DIMM features supported on the server.

Table 5   Server Main Memory Features

Memory server technologies

Description

DIMM

Intel® Xeon® CPU generation

Intel® Xeon® 6 CPUs

DDR5 memory clock speed

Up to 6400 MT/s 1DPC; Up to 5200 MT/s 2DPC

Operational voltage

DRAM fab density

Memory type

Memory DRAM DIMM/MRDIMM 
organization

Maximum number of DRAM 
DIMM/MRDIMM per server

DRAM DIMM/MRDIMM Densities 
and Ranks

Maximum system memory 
capacity 

1.1 Volts

16Gb, 24Gb and 32Gb

RDIMM (Registered DDR5 DIMM)

Eight memory DIMM channels per CPU; up to 2 DIMMs Per Channel

64 (4-Socket)

64GB 2Rx4, 96GB 2Rx4, 128GB 2Rx4, 256GB 4Rx4

16TB (64x256GB)

10

Cisco UCS X410c M8 Compute Node

Figure 3  Cisco UCS X410c M8 Compute Node Memory Organization 

CONFIGURING THE CISCO UCS X410C M8 COMPUTE NODE

Cisco UCS X410c M8 Compute Node

11

CONFIGURING THE CISCO UCS X410C M8 COMPUTE NODE

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

Table 6   Available Memory Options

Product ID (PID)

PID Description

DDR5-6400 MT/s Cisco Memory PIDs list

UCSX-MRX64G2RE5

64GB RDIMM 2Rx4 1.1Volts (16Gb)

UCSX-MRX96G2RF5

96GB RDIMM 2Rx4 1.1Volts (24Gb)

UCSX-MR128G2RG5

128GB RDIMM 2Rx4 1.1Volts (32Gb)

UCSX-MR256G4RG51

256GB DDR5-6400 RDIMM 4Rx4 (32Gb)

Memory Mirroring Option2

N01-MMIRRORD

Memory mirroring option

Accessories/spare included with Memory configuration:

■ UCS-DDR5-BLK3 is auto included for the unpopulated DIMMs slots

Ranks/DIMM

2

2

2

4

Notes:

1. Available post-GA.
2. If N01-MMIRROR is selected and Processor quantity is 4, then the total memory DIMMs must be 16, 32, or 64 

identical DIMMs per CPU.

3. Any empty DIMM slot must be populated with a DIMM blank to maintain proper cooling airflow.

Memory configurations and mixing rules

■ Golden Rule: Memory on every CPU socket shall be configured identically.

For full details on supported memory configurations, count rules, population rules and mixing rules see 
the Intel M8 Memory guide.

12

Cisco UCS X410c M8 Compute Node

■
CONFIGURING THE CISCO UCS X410C M8 COMPUTE NODE

STEP 4 CHOOSE OPTIONAL FRONT MEZZANINE ADAPTER

The Cisco UCS X410c M8 Compute Node has one front mezzanine connector that can 
accommodate one of the following mezzanine cards from the 

Table 7

Table 7   Available Front Mezzanine Adapters  

Product ID (PID)

PID Description

Connector Type

UCSX-X10C-PT4F-D

UCS X10c Compute Pass-Through Controller (Front)

Front Mezzanine

Supports up to 6 NVMe drives only

Does not support RAID controller

UCSX-RAID-M1L6

24G Tri-Mode M1 RAID Controller w/4GB FBWC 6 Drives

Front Mezzanine

If SAS/SATA is selected, then this controller must be 
selected

Supports up to 6 U.3 NVMe drives

RAID levels (0, 1, 5, 6, 10, and 50) for 6 SAS/SATA/U.3 
NVMe drives**, or optionally up to 2 U.3 NVMe drives 
(drive slots 5-6) in pass-through mode

UCSX-X10C-PTE3

UCS X10c Compute Pass Through Controller for E3.S (Front)

Front Mezzanine

Supports a maximum of 9 E3.S drives

Cannot mix with SATA/SAS/NVMe drives

Approved Configurations

— Only one Front Mezzanine connector per Server

— The Front Mezzanine Adapter from Table 7 is optional

Cisco UCS X410c M8 Compute Node

13

■
■
■
■
■
■
■
CONFIGURING THE CISCO UCS X410C M8 COMPUTE NODE

STEP 5 CHOOSE REAR MEZZANINE ADAPTER

The Cisco UCS X410c M8 Compute Node must be ordered with a Cisco VIC mLOM Adapter. The 
adapter is located at the back.

Select Rear mLOM Adapter from Table 8

 (Required)

Table 8   mLOM Adapters 

Product ID (PID)

Description

Connection 
type

UCSX-MLV5D200GV2D

Cisco UCS VIC 15230 modular LOM w/Secure Boot X Compute Node

mLOM

■  Supported with both IFM 25G and IFM 100G

■  Operates at 4x 25G with both IFM 25G and IFM 100G

UCSX-ML-V5Q50G-D

Cisco UCS VIC 15420 modular LOM for X Compute Node

mLOM

■  Supported with both IFM 25G and IFM 100G

■  Operates at 4x 25G with both IFM 25G

■  Operates at 2x 25G with IFM 100G

NOTE:  

There is no backplane in the Cisco UCS X9508 chassis; thus, the compute nodes 
directly connect to the IFMs using Orthogonal Direct connectors.

Figure 8 shows the location of the mLOM and rear mezzanine adapters on the 
Cisco UCS X410c M8 Compute Node. The bridge adapter connects the mLOM 
adapter to the rear mezzanine adapter.

Approved Configurations

— One mLOM VIC from Table 8 is always required.

14

Cisco UCS X410c M8 Compute Node

■
■
■
CONFIGURING THE CISCO UCS X410C M8 COMPUTE NODE

The Cisco UCS X410c M8 Compute Node has one rear mezzanine adapter connector which can 
accommodate a UCS VIC 15422 Mezz card that can be used as a second VIC card on the compute 
node for network connectivity.

Select Rear Mezzanine Adapter from Table 9

 (Optional)

Table 9   Available Rear Mezzanine Adapters  

Product ID(PID)

PID Description

Connector Type

Cisco VIC Card

UCSX-ME-V5Q50G-D

Cisco VIC Bridge Card

UCSX-V5-BRIDGE-D

UCS VIC 15422 4x25G secure boot mezz for X Compute 
Node

Rear Mezzanine 
connector on 
motherboard

UCS VIC 15000 bridge to connect mLOM and mezz X 
Compute Node 
■  Included with the Cisco VIC 15422 mezzanine 
adapter.

■  This bridge connects the Cisco VIC 15420 mLOM and 
Cisco VIC 15422 Mezz for the compute node, and has 
PCIe Gen4 x16 connectivity towards CPU2.

■  UCSX-V5-BRIDGE-D and has a PCIe Gen4 x16 
connectivity towards CPU2

One connector on Mezz 
card and one connector 
on mLOM card

NOTE:  

■  If a UCSX-ME-V5Q50G-D rear mezzanine VIC card is installed, a 
UCSX-V5-BRIDGE-D VIC bridge card is included and connects the mLOM to the 
mezzanine adapter.

■  The UCSX-ME-V5Q50G-D rear mezzanine card has Ethernet connectivity to the IFM 
using the UCSX-V5-BRIDGE-D and has a PCIe Gen4 x16 connectivity towards CPU2. 

Approved Configurations

— UCS VIC adapter from Table 9 is optional.

Cisco UCS X410c M8 Compute Node

15

■
CONFIGURING THE CISCO UCS X410C M8 COMPUTE NODE

Table 10  Throughput Per UCS X410c M8 Server

X410c M8 Compute 
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

16

Cisco UCS X410c M8 Compute Node

 
CONFIGURING THE CISCO UCS X410C M8 COMPUTE NODE

Figure 4 shows the network connectivity from the mLOM out to the 25G IFMs.

Figure 4  Network Connectivity 25G IFMs

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

Cisco UCS X410c M8 Compute Node

17

 
 
 
 
CONFIGURING THE CISCO UCS X410C M8 COMPUTE NODE

Figure 5 shows the network connectivity from the mLOM out to the 100G IFMs. 

Figure 5  Network Connectivity 100G IFMs

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

Cisco UCS X410c M8 Compute Node

CONFIGURING THE CISCO UCS X410C M8 COMPUTE NODE

STEP 6 CHOOSE OPTIONAL DRIVES

The standard storage drive features are:

2.5-inch small form factor drives or E3.S 1T NVMe drives

Hot-pluggable

Drives come mounted in sleds

Select Drives

Select drives from the list of supported drives available in Table 11.

NOTE:  The Cisco UCS X410c M8 Compute Node can be ordered with or without 
drives.

CAUTION:  Cisco uses solid state drives (SSDs) from a number of vendors. All solid state 
drives (SSDs) are subject to physical write limits and have varying maximum usage limitation 
specifications set by the manufacturer. Cisco will not replace any solid state drives (SSDs) that 
have exceeded any maximum usage specifications set by Cisco or the manufacturer, as 
determined solely by Cisco.

Table 11  Available Drive Options  

Product ID (PID)

Description

Drive 
Type

Speed  Size

SATA

480GB 2.5in 15mm Solidigm S4620 Enter Perf 6G SATA 3X SSD
960GB 2.5in 15mm Solidigm S4620 Enter Perf 6G SATA 3X SSD
3.8TB 2.5in 15mm Solidigm S4520 Enter Perf 6G SATA 1X SSD
480GB 2.5in 15mm Solidigm S4520 Enter Perf 6G SATA 1X SSD
960GB 2.5in 15mm Solidigm S4520 Enter Perf 6G SATA 1X SSD

SAS/SATA SSDs1,2
Self-Encrypted Drives (SED)
UCSX-SD960GM2NK9D 960GB 2.5in Enter Value 6G SATA Micron G2 SSD (SED)
Enterprise Performance SSDs (high endurance, supports up to 3X DWPD (drive writes per day))
UCSX-SDB480OA1P
UCSX-SDB960OA1P
UCSX-SDB3T8OA1V
UCSX-SDB480OA1V
UCSX-SDB960OA1V
Enterprise Value SSDs (Low endurance, supports up to 1X DWPD (drive writes per day)) 
UCSXSD240GBM1XEVD 240GB 2.5in Enter Value 6G SATA Micron G2 SSD
UCSX-SD19TBM1XEVD
1.9TB 2.5in Enter Value 6G SATA Micron G2 SSD
E3.S
UCSX-NVE112T8K1P
UCSX-NVE11T6K1P
UCSX-NVE13T2K1P
UCSX-NVE16T4K1P

12.8TB E3.S1T KCD8XPJE HgPerf HgEnd Gen5 3X NVMe (SIE SCEF)
1.6TB E3.S1T KCD8XPJE HgPerf HgEnd Gen5 3X NVMe (SIE SCEF)
3.2TB E3.S1T KCD8XPJE HgPerf HgEnd Gen5 3X NVMe (SIE SCEF)
6.4TB E3.S1T KCD8XPJE HgPerf HgEnd Gen5 3X NVMe (SIE SCEF)

SATA
SATA
SATA
SATA
SATA

NVMe
NVMe
NVMe
NVMe

SATA
SATA

6G

960GB

6G
6G
6G
6G
6G

6G
6G

480GB
960GB
3.8TB
480GB
960GB

240GB
1.9TB

E3.S
E3.S
E3.S
E3.S

12.8TB
1.6TB
3.2TB
6.4TB

Cisco UCS X410c M8 Compute Node

19

■
■
■
CONFIGURING THE CISCO UCS X410C M8 COMPUTE NODE

Table 11  Available Drive Options (continued) 

Product ID (PID)

Description

Drive 
Type

Speed  Size

Accessories/spare included with drives: Drive blanks, either UCSC-BBLKD-M7 for 2.5" modules or 
UCSC-E3S1T-F for the E3.S mezzanine are included for unpopulated drive slots on configured systems.  
They must be ordered separately when ordering a front mezzanine as a spare.

Notes:

1. For SSD drives to be in a RAID group, two or more identical SSDs must be used in the group.
2. If SSDs are in JBOD Mode, the drives do not need to be identical.

Approved Configuration

— Up to nine hot-pluggable EDSFF E3.S NVMe drives with a new pass-through front 

mezzanine controller

— Up to six hot-pluggable, solid-state drives (SSDs), or Non-Volatile Memory Express 

(NVMe) 2.5-inch drives with a choice of enterprise-class redundant array of 
independent disks (RAIDs).

20

Cisco UCS X410c M8 Compute Node

CONFIGURING THE CISCO UCS X410C M8 COMPUTE NODE

STEP 7 CHOOSE M.2 MODULE SSDs AND OPTIONAL DRIVES

Cisco 6 GB/s SATA Boot-Optimized M.2 RAID Controller (included): Boot-Optimized RAID controller 
(UCSX-M2I-HWRD-FPS) for hardware RAID across two SATA M.2 storage modules. The Boot-Optimized 
RAID controller plugs into the motherboard and the M.2 SATA drives plug into the Boot-Optimized RAID 
controller.

Instead of RAID Controller

:

NOTE:  

The UCSX-M2-HWRD-FPS is automatically included with the server configuration

The UCSX-M2-HWRD-FPS controller supports RAID 1 and JBOD mode and is available 
only with 240GB, 480GB, and 960GB M.2 SATA SSDs.

Cisco IMM is supported for configuring volumes and monitoring of the controller and 
installed SATA M.2 drives

■ Hot-plug replacement is not supported. The compute node must be powered off to 

replace. 

If selected, the M.2 NVMe module replaces the M.2 RAID Controller.

The NVMe module does not support RAID

Table 12  Front Panel with M.2 options

Product ID (PID)

PID Description

UCSX-M2I-HWRD-FPS

UCSX Front Panel w/M.2 RAID controller Included for SATA drive

UCSX-M2-PT-FPN

UCSX Front Panel w/M.2 Pass Through Controller for NVME drive

Select Cisco M.2 drives: Order one or two matching M.2 drives. This connector accepts the 
boot-optimized RAID controller (see Table 12). Each boot-optimized RAID controller can accommodate 
up to two M.2 drives shown in Table 13.

NOTE:  

Each boot-optimized RAID controller can accommodate up to two M.2 drives 
shown in Table 13. The boot-optimized RAID controller plugs into the 
motherboard.

It is recommended that M.2 drives be used as boot-only devices.

The M.2 drives can boot in UEFI mode only. Legacy boot mode is not supported.

Table 13  M.2 Drives

Product ID (PID)

PID Description

UCSX-M2-240G-D
UCSX-M2-480G-D
UCSX-M2-960G-D
UCSX-M2240OA1V
UCSX-M2480OA1V

240GB M.2 SATA Micron G2 SSD
480GB M.2 SATA Micron G2 SSD
960GB M.2 SATA Micron G2 SSD
240GB M.2 Boot Solidigm S4520 SATA 1X SSD
480GB M.2 Boot Solidigm S4520 SATA 1X SSD

Protocol

SATA
SATA
SATA
SATA
SATA

Cisco UCS X410c M8 Compute Node

21

■
■
■
■
■
■
■
■
■
■
■
CONFIGURING THE CISCO UCS X410C M8 COMPUTE NODE

Table 13  M.2 Drives

Product ID (PID)

PID Description

UCSX-NVM2-400GB
UCSX-NVM2-960GB

400GB M.2 Boot NVMe 
960GB M.2 Boot NVMe

Protocol

NVMe
NVMe

22

Cisco UCS X410c M8 Compute Node

CONFIGURING THE CISCO UCS X410C M8 COMPUTE NODE

STEP 8    CHOOSE OPTIONAL TRUSTED PLATFORM MODULE 

Trusted Platform Module (TPM) is a computer chip or microcontroller that can securely store 
artifacts used to authenticate the platform or Cisco UCS X410c M8 Compute Node. These 
artifacts can include passwords, certificates, or encryption keys. A TPM can also be used to 
store platform measurements that help ensure that the platform remains trustworthy. 
Authentication (ensuring that the platform can prove that it is what it claims to be) and 
attestation (a process helping to prove that a platform is trustworthy and has not been 
breached) are necessary steps to ensure safer computing in all environments.

Table 14  Available TPM Option  

Product ID (PID)

Description

UCSX-TPM-002D-D

TPM 2.0 TCG FIPS140-2 CC+ Cert M7 Intel MSW2022 Compliant

UCSX-TPM-OPT-OUT1

OPT OUT, TPM 2.0, TCG, FIPS140-2, CC EAL4+ Certified

Notes:

1. Please note Microsoft certification requires a TPM 2.0 for bare-metal or guest VM deployments. Opt-out of the 

TPM 2.0 voids the Microsoft certification.

NOTE:  

The TPM module used in this system conforms to TPM v2.0 as defined by the 
Trusted Computing Group (TCG). 

TPM installation is supported after factory. However, a TPM is installed with a 
one-way screw and cannot be replaced, upgraded, or moved to another compute 
node. 

If a Cisco UCS X410c M8 Compute Node with a TPM is returned, the replacement 
Cisco UCS X410c M8 Compute Node must be ordered with a new TPM. If there is 
no existing TPM in the Cisco UCS X410c M8 Compute Node, you can install a TPM 
2.0. Refer to the following document for Installation location and instructions:

https://www.cisco.com/content/en/us/td/docs/unified_computing/ucs/x/hw/x410
c-M8/install/b-cisco-ucs-x410c-M8-install-guide.html

Cisco UCS X410c M8 Compute Node

23

■
■
■
CONFIGURING THE CISCO UCS X410C M8 COMPUTE NODE

STEP 9 CHOOSE OPERATING SYSTEM AND VALUE-ADDED SOFTWARE

Operating System (Table 15)

NOTE:  

See this link for operating system guidance: 
https://ucshcltool.cloudapps.cisco.com/public/

Table 15  Operating System 

Product ID (PID)

PID Description

Microsoft Options

MSWS-25-ST16C 

Windows Server 2025 Standard, 16 Cores

MSWS-25-ST16C-NS 

Windows Server 2025 Standard, 16 Cores - No Cisco SVC

MSWS-25-ST24C 

Windows Server 2025 Standard, 24 Cores

MSWS-25-ST24C-NS 

Windows Server 2025 Standard, 24 Cores - No SVC

MSWS-25-DC16C 

Windows Server 2025 Datacenter, 16 Cores

MSWS-25-DC16C-NS 

Windows Server 2025 Datacenter, 16 Cores - No SVC

MSWS-25-DC24C 

Windows Server 2025 Datacenter, 24 Cores

MSWS-25-DC24C-NS 

Windows Server 2025 Datacenter, 24 Cores - No SVC

Red Hat

RHEL-2S2V-D1A

Red Hat Enterprise Linux (1-2 CPU,1-2 VN); 1-Yr Support Req

RHEL-2S2V-D3A

Red Hat Enterprise Linux (1-2 CPU,1-2 VN); 3-Yr Support Req

RHEL-2S2V-D5A

Red Hat Enterprise Linux (1-2 CPU,1-2 VN); 5-Yr Support Req

RHEL-VDC-2SUV-D1A

RHEL for Virt Datacenters (1-2 CPU, Unlim VN) 1 Yr Supp Req

RHEL-VDC-2SUV-D3A

RHEL for Virt Datacenters (1-2 CPU, Unlim VN) 3 Yr Supp Req

RHEL-VDC-2SUV-D5A

RHEL for Virt Datacenters (1-2 CPU, Unlim VN) 5 Yr Supp Req

Red Hat Ent Linux/ High Avail/ Res Strg/ Scal 

RHEL-2S2V-D1S

Red Hat Enterprise Linux (1-2 CPU,1-2 VN); Prem 1Yr SnS Reqd

RHEL-2S2V-D3S

Red Hat Enterprise Linux (1-2 CPU,1-2 VN); Prem 3Yr SnS Reqd

RHEL-2S-HA-D1S

RHEL High Availability (1-2 CPU); Premium 1-yr SnS Reqd

RHEL-2S-HA-D3S

RHEL High Availability (1-2 CPU); Premium 3-yr SnS Reqd

RHEL-2S-RS-D1S

RHEL Resilent Storage (1-2 CPU); Premium 1-yr SnS Reqd

RHEL-2S-RS-D3S

RHEL Resilent Storage (1-2 CPU); Premium 3-yr SnS Reqd

24

Cisco UCS X410c M8 Compute Node

■
■
CONFIGURING THE CISCO UCS X410C M8 COMPUTE NODE

Table 15  Operating System (continued)

Product ID (PID)

PID Description

RHEL-VDC-2SUV-D1S

RHEL for Virt Datacenters (1-2 CPU, Unlim VN) 1 Yr SnS Reqd

RHEL-VDC-2SUV-D3S

RHEL for Virt Datacenters (1-2 CPU, Unlim VN) 3 Yr SnS Reqd

Red Hat SAP

RHEL-SAP-2S2V-D1S

RHEL for SAP Apps (1-2 CPU, 1-2 VN); Prem 1-Yr SnS Reqd

RHEL-SAP-2S2V-D3S

RHEL for SAP Apps (1-2 CPU, 1-2 VN); Prem 3-Yr SnS Reqd

RHEL-SAPSP-D3S

RHEL SAP Solutions Premium - 3 Years

RHEL-SAPSS-D3S

RHEL SAP Solutions Standard - 3 Years

SUSE

SLES-2S2V-D1A  

SUSE Linux Enterprise Svr (1-2 CPU,1-2 VM); 1-Yr Support Req

SLES-2S2V-D3A  

SUSE Linux Enterprise Svr (1-2 CPU,1-2 VM); 3-Yr Support Req

SLES-2S2V-D5A

SUSE Linux Enterprise Svr (1-2 CPU,1-2 VM); 5-Yr Support Req

SLES-2SUVM-D1A

SUSE Linux Enterprise Svr (1-2 CPU,Unl VM) LP; 1Y Supp Req

SLES-2SUVM-D3A

SUSE Linux Enterprise Svr (1-2 CPU,Unl VM) LP; 3Y Supp Req

SLES-2SUVM-D5A

SUSE Linux Enterprise Svr (1-2 CPU,Unl VM) LP; 5Y Supp Req

SLES-2S-LP-D1A

SUSE Linux Live Patching Add-on (1-2 CPU); 1yr Support Req

SLES-2S-LP-D3A

SUSE Linux Live Patching Add-on (1-2 CPU); 3yr Support Req

SLES-2S2V-D1S   

SUSE Linux Enterprise Svr (1-2 CPU,1-2 VM); Prio 1-Yr SnS

SLES-2S2V-D3S   

SUSE Linux Enterprise Svr (1-2 CPU,1-2 VM); Prio 3-Yr SnS

SLES-2S2V-D5S   

SUSE Linux Enterprise Svr (1-2 CPU,1-2 VM); Prio 5-Yr SnS

SLES-2SUVM-D1S   

SUSE Linux Enterprise Svr (1-2 CPU,Unl VM) LP; Prio 1Y SnS

SLES-2SUVM-D3S   

SUSE Linux Enterprise Svr (1-2 CPU,Unl VM) LP; Prio 3Y SnS

SLES-2SUVM-D5S   

SUSE Linux Enterprise Svr (1-2 CPU,Unl VM) LP; Prio 5Y SnS

SLES-2S-HA-D1S   

SUSE Linux High Availability Ext (1-2 CPU); 1yr SnS

SLES-2S-HA-D3S   

SUSE Linux High Availability Ext (1-2 CPU); 3yr SnS

SLES-2S-HA-D5S   

SUSE Linux High Availability Ext (1-2 CPU); 5yr SnS

SLES-2S-GC-D1S   

SUSE Linux GEO Clustering for HA (1-2 CPU); 1yr Sns

SLES-2S-GC-D3S   

SUSE Linux GEO Clustering for HA (1-2 CPU); 3yr SnS

SLES-2S-GC-D5S   

SUSE Linux GEO Clustering for HA (1-2 CPU); 5yr SnS

SLES-2S-LP-D1S   

SUSE Linux Live Patching Add-on (1-2 CPU); 1yr SnS Required

Cisco UCS X410c M8 Compute Node

25

CONFIGURING THE CISCO UCS X410C M8 COMPUTE NODE

Table 15  Operating System (continued)

Product ID (PID)

PID Description

SLES-2S-LP-D3S   

SUSE Linux Live Patching Add-on (1-2 CPU); 3yr SnS Required

SLES and SAP

SLES-SAP-2S2V-D1S   

SLES for SAP Apps (1-2 CPU, 1-2 VM); Priority 1-Yr SnS

SLES-SAP-2S2V-D3S   

SLES for SAP Apps (1-2 CPU, 1-2 VM); Priority 3-Yr SnS

SLES-SAP-2S2V-D5S   

SLES for SAP Apps (1-2 CPU, 1-2 VM); Priority 5-Yr SnS

SLES-SAP-2S2V-D1A

SLES for SAP Apps w/ HA (1-2 CPU, 1-2 VM); 1-Yr Support Reqd

SLES-SAP-2S2V-D3A

SLES for SAP Apps w/ HA (1-2 CPU, 1-2 VM); 3-Yr Support Reqd

SLES-SAP-2S2V-D5A

SLES for SAP Apps w/ HA (1-2 CPU, 1-2 VM); 5-Yr Support Reqd

26

Cisco UCS X410c M8 Compute Node

CONFIGURING THE CISCO UCS X410C M8 COMPUTE NODE

STEP 10 CHOOSE OPTIONAL OPERATING SYSTEM MEDIA KIT

Select the optional operating system media listed in Table 16.

Table 16  OS Media  

Product ID (PID)

PID Description

MSWS-22-ST16CD-RM

Windows Server 2022 Stan (16 Cores/2 VMs) Rec Media DVD Only

MSWS-22-DC16CD-RM

Windows Server 2022 DC (16Cores/Unlim VM) Rec Media DVD Only

Cisco UCS X410c M8 Compute Node

27

SUPPLEMENTAL MATERIAL

SUPPLEMENTAL MATERIAL

Simplified Block Diagram

A simplified block diagram of the Cisco UCS X410c M8 Compute Node system board is shown in Figure 6.

Figure 6  Cisco UCS X410c M8 Compute Node Simplified Block Diagram (IFMs 25G with Drives)

28

Cisco UCS X410c M8 Compute Node

Figure 7  Cisco UCS X410c M8 Compute Node Simplified Block Diagram (IFMs 100G with Drives)

SUPPLEMENTAL MATERIAL

Cisco UCS X410c M8 Compute Node

29

SUPPLEMENTAL MATERIAL

System Board

A top view of the Cisco UCS X410c M8 Compute Node system board is shown in Figure 8.

Figure 8  Cisco UCS X410c M8 Compute Node System Board

1

2

3

4

30

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

Bridge Card slot, which connects the 8 rear 
mezzanine slot and the mLOM/VIC slot

mLOM/VIC slot that supports zero or one Cisco 
VIC or Cisco X-Series 100 Gbps mLOM

Please refer to the Cisco UCS X410c M8 Compute Node Installation Guide for installation 
procedures.

Cisco UCS X410c M8 Compute Node

 
UPGRADING or REPLACING CPUs and MEMORY

UPGRADING or REPLACING CPUs and MEMORY

Refer to Cisco UCS X410c M8 Server Installation and Service Guide to upgrading or replacing CPUs.

Refer to Cisco UCS X410c M8 Server Installation and Service Guide to upgrading or replacing Memory.

Cisco UCS X410c M8 Compute Node

31

■
■
TECHNICAL SPECIFICATIONS

TECHNICAL SPECIFICATIONS

Dimensions and Weight

Table 17  Cisco UCS X410c M8 Compute Node Dimensions and Weight  

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

Fully configured compute node weight: 42 lb (19.05 kg)

Environmental Specifications

Table 18  Cisco UCS X410c M8 Compute Node Environmental Specifications  

Parameter

Value

Operating temperature

Supported operating temperatures depend on the compute node's memory:

For 256GB DDR5 DIMMs: 50° to 89.6° F (10° to 32° C) at 0 to 10,000

All other memory configurations: 50° to 95° F (10° to 35° C) at 0 to 
10,000

Non-operating temperature

-40° to 149°F (–40° to 65°C)

Operating humidity

5% to 90% non-condensing

Non-operating humidity

5% to 93% non-condensing

Operating altitude

0 to 10,000 ft (0 to 3000m); maximum ambient temperature decreases by 
1°C per 300m

Non-operating altitude

40,000 ft (12,000m)

For configuration-specific power specifications, use the Cisco UCS Power Calculator at:

http://ucspowercalc.cisco.com

32

Cisco UCS X410c M8 Compute Node

■
■
■
TECHNICAL SPECIFICATIONS

Cisco UCS X410c M8 Compute Node

33

TECHNICAL SPECIFICATIONS

34

Cisco UCS X410c M8 Compute Node

