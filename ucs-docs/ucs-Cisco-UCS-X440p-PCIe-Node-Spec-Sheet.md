# Cisco UCS X440p PCIe Node Spec Sheet

| | |
|---|---|
| **URL Title** | Cisco UCS X440p PCIe Node Spec Sheet |
| **URL** | https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-x-series-modular-system/x440p-specsheet.pdf |
| **Long URL** |  |
| **HTML Title** |  |
| **Source file** | `ucs-docs-raw/pdf/x440p-specsheet.pdf` |
| **File type** | PDF |
| **Fetched on** | 2026-04-13 13:38:43 |

---

Spec Sheet

Cisco UCS X440p PCIe 
Node

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

REV A.15

AUGUST 04, 2025



STEP
STEP
STEP
STEP
STEP

OVERVIEW  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
DETAILED VIEWS  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
Cisco UCS X440p PCIe Node Front View   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .4
PCIe Node STANDARD CAPABILITIES and FEATURES   . . . . . . . . . . . . . . . . . . . 5
CONFIGURING the Cisco UCS X440p PCIe Node   . . . . . . . . . . . . . . . . . . . . . . 6
1 CHOOSE BASE CISCO UCS X440p PCIe NODE SKU  . . . . . . . . . . . . . . . . . . . . . . . . . 7
2 SELECT RISER CARDS (REQUIRED)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
3 ORDER GPU CARDS   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
4 ORDER CISCO UCS X9416 X-FABRIC MODULES   . . . . . . . . . . . . . . . . . . . . . . . . . . 11
5 CHOOSE OPTIONAL REAR MEZZANINE VIC/BRIDGE ADAPTERS  . . . . . . . . . . . . . . . . 12
Cisco UCS X440p PCIe node under UCSX-M7-MLB:  . . . . . . . . . . . . . . . . . . . . . . . . . . 12
Cisco UCS X440p PCIe node under UCSX-M6-MLB:  . . . . . . . . . . . . . . . . . . . . . . . . . . 13
SUPPLEMENTAL MATERIAL  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  14
Simplified Block Diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
System Board   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
SPARE PARTS  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  16
TECHNICAL SPECIFICATIONS  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  17
Dimensions and Weight  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
Environmental Specifications  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17

2

Cisco UCS X440P M6 PCIe Node

OVERVIEW

OVERVIEW

The Cisco UCS X-Series Modular System simplifies your data center, adapting to the unpredictable needs of 
modern applications while also providing for traditional scale-out and enterprise workloads. It reduces the 
number of server types to maintain, helping to improve operational efficiency and agility as it helps reduce 
complexity. Powered by the Cisco Intersight™ cloud operations platform, it shifts your thinking from 
administrative details to business outcomes with hybrid cloud infrastructure that is assembled from the 
cloud, shaped to your workloads, and continuously optimized.

The Cisco UCS X440p Gen4 PCIe Node is a new node type that is now supported in the UCS X9508 chassis. 
This can be attached to X-Series compute node in the UCS X9508 chassis to provide GPU accelerators 
support using the UCS 9416 X-Fabric modules for UCS X9508 chassis.

The Cisco UCS X440p PCIe Node is the first PCIe resource node to integrate into the Cisco UCS X-Series 
Modular System. Up to four PCIe Nodes can reside in the 7-Rack-Unit (7RU) Cisco UCS X9508 Chassis and can 
be paired with one compute node each, offering up to four GPUs to a Cisco X-Series Compute Node with 
Cisco UCS X-Fabric Technology.

The UCS X-Fabric Technology solution is a combination of two products: the Cisco UCS X9416 X-Fabric 
Module which provides a PCIe Gen 4 fabric and the Cisco UCS X440p PCIe Node which hosts the GPUs.

The Cisco UCS X9508 Chassis has eight node slots, up to four of which can be X440p PCIe Nodes when paired 
with a Cisco X-Series compute node. This provides up to 16 GPUs per chassis to accelerate your 
applications. If your application needs even more GPU acceleration, up to two additional GPUs can be 
added on each compute node using optional GPU front mezz on X-Series Compute Node.

Cisco UCS X440p supports several GPUs please refer to STEP 3 ORDER GPU CARDS, page 9 for the available 
GPUs

Figure 1  Front views of Cisco UCS X440p PCIe Node 

Front View

Rear View

Cisco UCSX-440P PCIe Node

3

DETAILED VIEWS

DETAILED VIEWS

Cisco UCS X440p PCIe Node Front View

Figure 2 is a front view of the Cisco UCS X440p PCIe Node.

Figure 2  Cisco UCS X440p PCIe Node Front View

GPUs Option

1 
2

Locate LED & Status LED
PCI Node Ejector Handles

3
-

PCI Node Ejector Button
-

4

Cisco UCSX-440P PCIe Node

 
PCIe Node STANDARD CAPABILITIES and FEATURES

PCIe Node STANDARD CAPABILITIES and FEATURES

Table 1 lists the capabilities and features of the base Cisco UCS X440p PCIe Node. Details about how to 
configure the PCIe Node for a listed feature or capability (for example, number of processors, disk drives, 
or amount of memory) are provided in CONFIGURING the Cisco UCS X440p PCIe Node on page 6

.

Table 1   Capabilities and Features 

Capability/Feature

Description

Chassis

GPU slots

The Cisco UCS X440p PCIe Node mounts in a Cisco UCS X9508 chassis.

Riser Type A (1 PCIe slots) for 1x dual slot GPU per riser

Riser Type B (2 PCIe slots) for 2x single slot GPU per riser

Note: Not all risers are available in every server configuration option.

Please refer Table 3 for the complete GPU Cards PID lists

Available GPUs

■ NVIDIA

TESLA

Intel 

AMD

Please refer Table 4 for the complete GPU Cards PID lists

Power subsystem 

Power is supplied from the Cisco UCS X9508 chassis power supplies. The 
Cisco UCS X440p PCIe Node consumes a maximum of 1300 W.

Fans 

Integrated in the Cisco UCS X9508 chassis.

Integrated management 
processor

The built-in Cisco Integrated Management Controller enables monitoring of 
Cisco UCS X440p PCIe Node inventory, health, and system event logs.

ACPI

Front Indicators

Management

Advanced Configuration and Power Interface (ACPI) 4.0 Standard Supported. 
ACPI states S0 and S5 are supported. There is no support for states S1 
through S4.

Status indicator

Location indicator

Cisco Intersight software (SaaS, Virtual Appliance and Private Virtual 
Appliance)

■ UCS Manager (UCSM) 4.3(4) or later

Chassis

Compatible with the Cisco UCS 9508 X-Series Server Chassis

Cisco UCSX-440P PCIe Node

5

■
■
■
■
■
■
■
■
CONFIGURING the Cisco UCS X440p PCIe Node

CONFIGURING the Cisco UCS X440p PCIe Node

Follow these steps to configure the Cisco UCS X440p PCIe Node:

STEP 1 CHOOSE BASE CISCO UCS X440p PCIe NODE SKU, page 7

STEP 2 SELECT RISER CARDS (REQUIRED), page 8

STEP 3 ORDER GPU CARDS, page 9

STEP 4 ORDER CISCO UCS X9416 X-FABRIC MODULES, page 11

STEP 5 CHOOSE OPTIONAL REAR MEZZANINE VIC/BRIDGE ADAPTERS, page 12

6

Cisco UCSX-440P PCIe Node

■
■
■
■
■
CONFIGURING the Cisco UCS X440p PCIe Node

STEP 1 CHOOSE BASE CISCO UCS X440p PCIe NODE SKU

Verify the product ID (PID) of the Cisco UCS X440p PCIe Node as shown in Table 2.

Table 2   PIDs of the Base Cisco UCS X440p PCIe Node  

Product ID (PID)

Description

UCSX-M6-MLB (Top Level Ordering PID)

UCSX-440P-U

UCS X-Series Gen4 PCIe node

UCSX-M7-MLB (Top Level Ordering PID)

UCSX-440P-D-U

UCS X-Series Gen4 PCIe node

UCSX-M8-MLB (Top Level Ordering PID)

UCSX-440P-D-U

UCS X-Series Gen4 PCIe node

A base Cisco Gen4 PCIe Node ordered in Table 2 does not include any components or options. 
They must be selected during product ordering.

Please follow the steps on the following pages to order components such as the following, which 
are required in a functional PCIe Node:

GPUs

Riser Cards

Cisco UCS X9416 X-Fabric Modules

Cisco UCSX-440P PCIe Node

7

■
■
■
CONFIGURING the Cisco UCS X440p PCIe Node

STEP 2

SELECT RISER CARDS (REQUIRED)

Select risers from Table 3.

Table 3   PIDs of the Risers

Product ID (PID)

Description

UCSX-M6-MLB (Top Level Ordering PID)

UCSX-RIS-A-440P

Riser A for 1x dual slot GPU per riser, 440P PCIe node

Riser1A (controlled with CPU1)

Riser2A (controlled with CPU2)

UCSX-RIS-B-440P

Riser B for 2x single slot GPUs per riser, 440P PCIe node

Riser1B (controlled with CPU1)

Riser2B (controlled with CPU2)

UCSX-M7-MLB (Top Level Ordering PID)

UCSX-RIS-A-440P-D

Riser A for 1x dual slot GPU per riser, 440P PCIe node

Riser1A (controlled with CPU1)

Riser2A (controlled with CPU2)

UCSX-RIS-B-440P-D

Riser B for 2x single slot GPUs per riser, 440P PCIe node

Riser1B (controlled with CPU1)

Riser2B (controlled with CPU2)

UCSX-M8-MLB (Top Level Ordering PID)

UCSX-RIS-A-440P-D

Riser A for 1x dual slot GPU per riser, 440P PCIe node

Riser1A (controlled with CPU1)

Riser2A (controlled with CPU2)

UCSX-RIS-B-440P-D

Riser B for 2x single slot GPUs per riser, 440P PCIe node

Riser1B (controlled with CPU1)

Riser2B (controlled with CPU2)

NOTE:  The PCIe Node requires both the risers to be configured and doesn't support 
orderability without both risers included. Riser cards include all required power cables for 
supported GPUs.

8

Cisco UCSX-440P PCIe Node

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
■
CONFIGURING the Cisco UCS X440p PCIe Node

STEP 3 ORDER GPU CARDS

Select GPU Options

.
The available GPU PCIe options and their riser slot compatibilities are listed in Table 4

Table 4   Available PCIe GPU Cards

GPU Product ID (PID) PID Description

Riser Slot Compatibility

Maximum 
Number of GPUs 
Per node

UCSX-440P (M6 Servers)
UCSX-GPU-T4-16
UCSX-GPU-A16
UCSX-GPU-A100-80

NVIDIA T4 PCIE 75W 16GB
NVIDIA A16 PCIE 250W 4X16GB
TESLA A100, PASSIVE, 300W, 
80GB

UCSX-440P-D (M7 Severs)
UCSX-GPU-A16-D
UCSX-GPUA100-80-D

NVIDIA A16 PCIE 250W 4X16GB
TESLA A100, PASSIVE, 300W, 
80GB3
TESLA H100, PASSIVE, 350W, 
80GB
NVIDIA L4 Tensor Core, 70W, 
24GB
NVIDIA L40 300W, 48GB wPWR 
CBL
NVIDIA L40S: 350W, 48GB, 
2-slot FHFL GPU
Intel GPU Flex 140, Gen4x8, 
HHHL, 75W PCIe
 Intel GPU Flex 170, Gen4x16, 
HHFL, 150W PCIe
NVIDIA H100 NVL, 400W, 94GB, 
2-slot FHFL GPU

NVIDIA A16 PCIE 250W 4X16GB
NVIDIA L4 Tensor Core, 70W, 
24GB
NVIDIA L40 300W, 48GB wPWR 
CBL
NVIDIA L40S: 350W, 48GB, 
2-slot FHFL GPU

2-slot FHFL GPU
AMD Instinct MI210:300W, 
64GB, 2-slot FHFL GPU

UCSX-GPU-H100-80

UCSX-GPU-L4

UCSX-GPU-L40

UCSX-GPU-L40S

UCSX-GPU-FLEX1401

UCSX-GPU-FLEX1701

UCSX-GPU-H100-NVL

UCSX-440P-D (M8 Severs)
UCSX-GPU-A16-D
UCSX-GPU-L4

UCSX-GPU-L402

UCSX-GPU-L40S

UCSX-GPU-MI2102

Notes:

UCSX-GPU-H100-NVL3 NVIDIA H100 NVL, 400W, 94GB, 

Riser 1B (Gen 4), Riser 2B (Gen 4)
Riser 1A (Gen 4), Riser 2A (Gen 4)
Riser 1A (Gen 4), Riser 2A (Gen 4)

Riser 1A (Gen 4), Riser 2A (Gen 4)
Riser 1A (Gen 4), Riser 2A (Gen 4)

Riser 1A (Gen 4), Riser 2A (Gen 4)

Riser 1B (Gen 4), Riser 2B (Gen 4)

Riser 1A (Gen 4), Riser 2A (Gen 4)

Riser 1A (Gen 4), Riser 2A (Gen 4)

Riser 1B (Gen 4), Riser 2B (Gen 4)

Riser 1A (Gen 4), Riser 2A (Gen 4)

Riser 1A (Gen 4), Riser 2A (Gen 4)

Riser 1A (Gen 4), Riser 2A (Gen 4)
Riser 1B (Gen 4), Riser 2B (Gen 4)

Riser 1A (Gen 4), Riser 2A (Gen 4)

Riser 1A (Gen 4), Riser 2A (Gen 4)

Riser 1A (Gen 4), Riser 2A (Gen 4)

Riser 1A (Gen 4), Riser 2A (Gen 4)

4
2
2

2
2

2

4

2

2

4

2

2

2
4

2

2

2

2

1. Windows Server 2019 is not supported on 210C M7 and 410C M7 servers with Intel Flex 140 and 170 GPUs.

Cisco UCSX-440P PCIe Node

9

CONFIGURING the Cisco UCS X440p PCIe Node

2. Not supported with X210c compute node
3. Not supported with X410c compute node

Caveats

Riser cards and GPUs cannot be mixed.

NOTE:  Following Step 4 and Step 5 are optional only if the Cisco UCS X9508 Chassis 
already has the UCS X9416 X-Fabric modules installed and the X-Series compute node 
has one of the supported mezzanine adapters to connect to Cisco UCS X440p PCIe 
node 

10

Cisco UCSX-440P PCIe Node

CONFIGURING the Cisco UCS X440p PCIe Node

STEP 4 ORDER CISCO UCS X9416 X-FABRIC MODULES

The Cisco UCS X440p connectivity to the Cisco UCS X-Series compute node is enabled with the X 
Fabric Module. When a compute node is inserted into the chassis, the compute node's mezzanine 
card plugs directly into the two Fabric Module slots (with no midplane) for PCIe connectivity to 
the Cisco UCS X440p PCIe Node.

Select X-Fabric Modules on the UCS X9508 chassis Table 5.

Table 5   PIDs of the Risers

Product ID (PID)1

Description

UCSX-F-9416-D

UCS 9416 X-Fabric module for 9508 chassis

Notes:

1. The X-Fabric modules are required on the X9508 chassis

Cisco UCSX-440P PCIe Node

11

CONFIGURING the Cisco UCS X440p PCIe Node

STEP 5 CHOOSE OPTIONAL REAR MEZZANINE VIC/BRIDGE ADAPTERS

Cisco UCS X440p PCIe node under UCSX-M7-MLB:

The Cisco UCS X210c M7 Compute Node has one rear mezzanine adapter connector which can 
have a UCS VIC 15422 Mezz card that can be used as a second VIC card on the compute node for 
network connectivity or as a connector to the X440p PCIe node via X-Fabric modules. The same 
mezzanine slot on the compute node can also accommodate a pass-through mezzanine adapter 
for X-Fabric which enables compute node connectivity to the X440p PCIE node. Refer to Table 6 
for supported adapters.

Table 6   Available Rear Mezzanine Adapters  

Product ID(PID)

PID Description

Cisco VIC Card

UCSX-V4-PCIME-D

UCS PCI Mezz Card for X-Fabric

CPUs 
Required

2 CPUs 
required

UCSX-ME-V5Q50G-D

UCS VIC 15422 4x25G secure boot mezz for 
X Compute Node

2 CPUs 
required

Cisco VIC Bridge Card1

UCSX-V5-BRIDGE-D

UCS VIC 15000 bridge to connect mLOM 
and mezz X Compute Node 

2 CPUs 
required

(This bridge to connect the Cisco VIC 15420 
mLOM and Cisco VIC 15422 Mezz for the 
X210c M7 Compute Node)

Notes:

1. Included with the Cisco VIC 15422 mezzanine adapter.

Connector Type

Rear Mezzanine 
connector on 
motherboard

Rear Mezzanine 
connector on 
motherboard

One connector on 
Mezz card and 
one connector on 
mLOM card

12

Cisco UCSX-440P PCIe Node

CONFIGURING the Cisco UCS X440p PCIe Node

Cisco UCS X440p PCIe node under UCSX-M6-MLB:

The Cisco UCS X210c M6 Compute Node has one rear mezzanine adapter connector which can 
have a UCS VIC 14825/15422 Mezz card that can be used as a second VIC card on the compute 
node for network connectivity or as a connector to the X440p PCIe node via X-Fabric modules. 
The same mezzanine slot on the compute node can also accommodate a pass-through mezzanine 
adapter for X-Fabric which enables compute node connectivity to the X440p PCIE node. Refer to 
Table 6 for supported adapters.

Table 7   Available Rear Mezzanine Adapters  

Product ID(PID)

PID Description

CPUs 
Required

Connector Type

Cisco VIC Card

UCSX-V4-Q25GME

UCS VIC 148251 4x25G mezz for X Compute 
Node

2 CPUs 
required

UCSX-ME-V5Q50G

UCS VIC 154202 4x25G secure boot mLOM for 
X Compute Node

2 CPUs 
required

UCSX-V4-PCIME

UCS PCI Mezz Card for X-Fabric

2 CPUs 
required

Cisco VIC Bridge Card

UCSX-V4-BRIDGE3

UCS VIC 14000 bridge connect mLOM and 
mezz X Compute Node

2 CPUs 
required

UCSX-V5-BRIDGE4

UCS VIC 15000 bridge to connect mLOM and 
mezz X Compute Node 

2 CPUs 
required

(This bridge to connect the Cisco VIC 15420 
mLOM and Cisco VIC 15422 Mezz for the 
X210c M6 Compute Node)

Notes:

1. Cisco UCS VIC 14825 can only be used with the Cisco UCS VIC 14425 mLOM
2. Cisco UCS VIC 15420 can only be used with the Cisco UCS VIC 15422 mLOM
3. Included with the Cisco VIC 14825
4. Included with the Cisco VIC 15422

Rear Mezzanine 
connector on 
motherboard

Rear Mezzanine 
connector on 
motherboard

Rear Mezzanine 
connector on 
motherboard

One connector on 
Mezz card and one 
connector on 
mLOM card

One connector on 
Mezz card and one 
connector on 
mLOM card

Cisco UCSX-440P PCIe Node

13

SUPPLEMENTAL MATERIAL

SUPPLEMENTAL MATERIAL 

Simplified Block Diagram

A simplified block diagram of the Cisco UCS X440p PCIe Node system board is shown in Figure 3 with riser A.

Figure 3  Cisco UCS X440p PCIe Node Simplified Block Diagram with Riser A

A simplified block diagram of the Cisco UCS X440p PCIe Node system board is shown in Figure 4 with riser B.

Figure 4  Cisco UCS X440p PCIe Node Simplified Block Diagram with Riser B

14

Cisco UCSX-440P PCIe Node

System Board

A top view of the Cisco UCS X440p PCIe Node system board is shown in Figure 5. 

Figure 5  Cisco UCS X440p PCIe Node System Board

SUPPLEMENTAL MATERIAL

1

3

5

Riser slot 1

Supports both Type A and Type B risers.
GPU slot 1 (FHFL GPU shown)

Supports either FHFL or HHHL GPU 
depending on the riser type.
mezzanine connector (included)

2

4

-

Riser slot 2

Supports both Type A and Type B risers.
GPU slot 2 (FHFL GPU shown)

Supports either FHFL or HHHL GPU depending 
on the riser type.
-

Cisco UCSX-440P PCIe Node

15

SPARE PARTS

SPARE PARTS 

This section lists the upgrade and service-related parts for the Cisco UCS X440p PCIe Node. 

Table 8   Spare Parts  

Product ID (PID)

PID Description

Riser Blank

UCSX-RIS-BLK-440P= 

PCIe blank for UCS X-series 440P PCIe node 

UCSX-RIS-BLK-440P-D= 

PCIe blank for UCS X-series 440P PCIe node 

X-Fabric Module

UCSX-F-9416=

UCS 9416 X-Fabric module for 9508 chassis

UCSX-F-9416-D=

UCS 9416 X-Fabric module for 9508 chassis

GPU Cards

UCSX-GPU-T4-16=

NVIDIA T4 PCIE 75W 16GB

UCSX-GPU-A16=

NVIDIA A16 PCIE 250W 4X16GB

UCSX-GPU-A100-80=

TESLA A100, PASSIVE, 300W, 80GB

UCSX-GPU-A16-D=

NVIDIA A16 PCIE 250W 4X16GB

UCSX-GPU-A100-80-D=

TESLA A100, PASSIVE, 300W, 80GB3

UCSX-GPU-L4=

NVIDIA L4 Tensor Core, 70W, 24GB

UCSX-GPU-L40=

NVIDIA L40 300W, 48GB wPWR CBL

UCSX-GPU-L40S=

NVIDIA L40S: 350W, 48GB, 2-slot FHFL GPU

UCSX-GPU-H100-80=

TESLA H100, PASSIVE, 350W, 80GB

UCSX-GPU-FLEX140=

Intel GPU Flex 140, Gen4x8, HHHL, 75W PCIe

UCSX-GPU-FLEX170=

 Intel GPU Flex 170, Gen4x16, HHFL, 150W PCIe

UCSX-GPU-H100-NVL=

NVIDIA H100 NVL, 400W, 94GB, 2-slot FHFL GPU

UCSX-GPU-MI210=

AMD Instinct MI210:300W, 64GB, 2-slot FHFL GPU

Riser

UCSX-440P-A=

UCSX-440P-B= 

UCS X-Series Gen4 PCIe node w/ Riser type A (1FHFL)

UCS X-Series Gen4 PCIe node with Riser type B (2HHHL)

16

Cisco UCSX-440P PCIe Node

TECHNICAL SPECIFICATIONS

TECHNICAL SPECIFICATIONS

Dimensions and Weight

Table 9   Cisco UCS X440p PCIe Node Dimensions and Weight  

Parameter Value

Height

1.80 in. (45.7 mm)

Width

Depth

11.28 in.(286.5 mm)

24 in. (602 mm)

Weight 

■ Minimally configured node weight = 12.84 lbs (5.83 kg)

Fully loaded PCIe Node with T4 GPU = 14.9 lb; minimum config with 1x T4 GPU = 12.9 lb

Fully loaded PCIe Node with A16 GPU = 17.1 lb; minimum config with 1X A16 GPU = 14.6 lb

Fully loaded PCIe Node with A40 GPU = 16.6 lb; minimum config with 1X A40 GPU = 14.4 lb

Fully loaded PCIe Node with A100 GPU = 17.9 lb; minimum config with 1X A100 GPU = 15 lb

Environmental Specifications

Table 10  Cisco UCS X440p PCIe Node Environmental Specifications  

Parameter

Value

Operating temperature

50° to 95°F (10° to 35°C)

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

NOTE:  The Cisco UCS X440p PCIe Node has a power cap of 1300 Watts for all 
combinations of components. Also, the ambient temperature must be less than 35 oC 
(95 oF).

Cisco UCSX-440P PCIe Node

17

■
■
■
■
TECHNICAL SPECIFICATIONS

18

Cisco UCSX-440P PCIe Node

