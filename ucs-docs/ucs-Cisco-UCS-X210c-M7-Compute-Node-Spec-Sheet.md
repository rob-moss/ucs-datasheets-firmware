# Cisco UCS X210c M7 Compute Node Spec Sheet

| | |
|---|---|
| **URL Title** | Cisco UCS X210c M7 Compute Node Spec Sheet |
| **URL** | https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-x-series-modular-system/x210cm7-specsheet.pdf |
| **Long URL** |  |
| **HTML Title** |  |
| **Source file** | `ucs-docs-raw/pdf/x210cm7-specsheet.pdf` |
| **File type** | PDF |
| **Fetched on** | 2026-04-08 08:47:18 |

---

Spec Sheet

Cisco UCS X210c M7 
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

REV A.47

MARCH 10, 2026 

OVERVIEW  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
DETAILED VIEWS  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
Cisco UCS X210c M7 Compute Node Front View  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .5
COMPUTE NODE STANDARD CAPABILITIES and FEATURES   . . . . . . . . . . . . . . . 7
CONFIGURING the Cisco UCS X210c M7 Compute Node  . . . . . . . . . . . . . . . . . 9
1 CHOOSE BASE CISCO UCS X210C M7 COMPUTE NODE SKU   . . . . . . . . . . . . . . . . . . 10
STEP
2 CHOOSE CPU(S)   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
STEP
STEP
3 CHOOSE MEMORY   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
Memory configurations and mixing rules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
4 CHOOSE REAR mLOM ADAPTER   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
STEP
5 CHOOSE OPTIONAL REAR MEZZANINE VIC/BRIDGE ADAPTERS  . . . . . . . . . . . . . . . . 25
STEP
6 CHOOSE OPTIONAL FRONT MEZZANINE ADAPTER . . . . . . . . . . . . . . . . . . . . . . . . 27
STEP
7 CHOOSE OPTIONAL GPU PCIe NODE   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
STEP
8 CHOOSE OPTIONAL GPUs   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
STEP
9 CHOOSE OPTIONAL DRIVES  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
STEP
10 ORDER M.2 SATA SSDs AND RAID CONTROLLER   . . . . . . . . . . . . . . . . . . . . . . . . 33
STEP
11 ORDER NVMe BOOT (OPTIONAL)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
STEP
12 CHOOSE OPTIONAL TRUSTED PLATFORM MODULE   . . . . . . . . . . . . . . . . . . . . . . 35
STEP
13 CHOOSE OPERATING SYSTEM AND VALUE-ADDED SOFTWARE   . . . . . . . . . . . . . . . 36
STEP
14 CHOOSE OPTIONAL OPERATING SYSTEM MEDIA KIT . . . . . . . . . . . . . . . . . . . . . . 39
STEP
SUPPLEMENTAL MATERIAL  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  40
Simplified Block Diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
System Board   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
UPGRADING or REPLACING CPUs and Memory   . . . . . . . . . . . . . . . . . . . . . .  45
5TH GEN INTEL XEON BENEFIT PILLARS   . . . . . . . . . . . . . . . . . . . . . . . . . .  46
Intel® Xeon® Processors Notices and Disclaimers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
LEADERSHIP PERFORMANCE WITH 4TH GEN INTEL® XEON® PROCESSORS   . . .  48
Intel® Xeon® Processors Notices and Disclaimers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
SPARE PARTS  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  50
TECHNICAL SPECIFICATIONS  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  59
Dimensions and Weight  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
Environmental Specifications  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
DISCONTINUED EOL PRODUCTS  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  60

2

Cisco UCS X210c M7 Compute Node

OVERVIEW

OVERVIEW

The Cisco UCS X-Series Modular System simplifies your data center, adapting to the unpredictable needs of 
modern applications while also providing for traditional scale-out and enterprise workloads. It reduces the 
number of server types to maintain, helping to improve operational efficiency and agility as it helps reduce 
complexity. Powered by the Cisco Intersight™ cloud operations platform, it shifts your thinking from 
administrative details to business outcomes with hybrid cloud infrastructure that is assembled from the 
cloud, shaped to your workloads, and continuously optimized.

The Cisco UCS X210c M7 Compute Node is the computing device to integrate into the Cisco UCS X-Series 
Modular System. Up to eight compute nodes can reside in the 7-Rack-Unit (7RU) Cisco UCS X9508 Chassis, 
offering one of the highest densities of compute, IO, and storage per rack unit in the industry. 

The Cisco UCS X210c M7 Compute Node harnesses the power of the latest Intel® Xeon® Scalable Processors, 
and offers the following:

■ CPU: 

■ Up to 2x 5th Generation Intel® Xeon® Scalable Processors with up to 64 cores per processor or 

■ Up to 2x 4th Generation Intel® Xeon® Scalable Processors with up to 60 cores per processor. 

■ Memory: 

■ Up to 8TB with 32 x 256GB DDR5-5600 DIMMs, in a 2-socket configuration with 5th Gen. Intel® 

Xeon® Scalable Processors or 

■ Up to 8TB with 32 x 256GB DDR5-4800 DIMMs, in a 2-socket configuration with 4th Gen. Intel® 

Xeon® Scalable Processors.

■ Storage: Up to 6 hot-pluggable, Solid-State Drives (SSDs), or Non-Volatile Memory Express (NVMe) 
2.5-inch drives with a choice of enterprise-class Redundant Array of Independent Disks (RAID) or 
pass-through controllers with four lanes each of PCIe Gen 4 connectivity and up to 2 M.2 SATA or 
NVMe drives for flexible boot and local storage capabilities.

■ Optional Front Mezzanine GPU module: The Cisco UCS Front Mezzanine GPU module is a passive 

PCIe Gen 4 front mezzanine option with support for up to two U.2 or U.3 NVMe drives and two GPUs.

■ mLOM virtual interface cards: 

■ Cisco UCS Virtual Interface Card (VIC) 15420 occupies the server's Modular LAN on 

Motherboard (mLOM) slot, enabling up to 50Gbps (2 x25Gbps) of unified fabric connectivity 
to each of the chassis Intelligent Fabric Modules (IFMs) for 100Gbps connectivity per server.

■ Cisco UCS Virtual Interface Card (VIC) 15230 occupies the server's modular LAN on 

motherboard (mLOM) slot, enabling up to 100 Gbps of unified fabric connectivity to each of 
the chassis Intelligent Fabric Modules (IFMs) for 100 Gbps connectivity per server with 
secure boot capability.

■ Optional Mezzanine card: 

■ Cisco UCS Virtual Interface Card (VIC) 15422 can occupy the server's mezzanine slot at the 
bottom rear of the chassis. An included bridge card extends this VIC's 100Gbps (4 x 25Gbps) 
of network connections through IFM connectors, bringing the total bandwidth to 100Gbps 
per VIC 15420 and 15422 (for a total of 200Gbps per server). In addition to IFM connectivity, 
the VIC 15422 I/O connectors link to Cisco UCS X-Fabric technology.

Cisco UCS X210c M7 Compute Node

3

OVERVIEW

■ Cisco UCS PCI Mezz card for X-Fabric can occupy the server's mezzanine slot at the bottom 
rear of the chassis. This card's I/O connectors link to Cisco UCS X-Fabric modules and enable 
connectivity to the X440p PCIe Node.

■ Security: Includes secure boot silicon root of trust FPGA, ACT2 anti-counterfeit provisions, and 

optional Trusted Platform Model (TPM).

NOTE:  All options listed in the Spec Sheet are compatible with Intersight Managed Mode and UCSM Managed 
Mode configurations. To see the most recent list of components that are supported in Intersight Managed 
Mode, see Supported Systems.

Figure 1 on page 5 shows a front view of the Cisco UCS X210c M7 Compute Node.

Figure 1  Cisco UCS X210c M7 Compute Node 

Front View with Drives

Front View with Drives and GPU

4

Cisco UCS X210c M7 Compute Node

DETAILED VIEWS

DETAILED VIEWS

Cisco UCS X210c M7 Compute Node Front View

Figure 2 & Figure 3 is a front view of the Cisco UCS X210c M7 Compute Node.

Figure 2  Cisco UCS X210c M7 Compute Node Front View (Drives option)

Storage Drives Option

7

9

1.6 TB

1.6 TB

UCSC-NVME2H-I1600

UCSC-NVME2H-I1600

NVMe SSD

NVMe SSD

1.6 TB

1.6 TB

UCSC-NVME2H-I1600

UCSC-NVME2H-I1600

NVMe SSD

NVMe SSD

5

6

8

15

10

14

16

1

13

11

12

1.6 TB

1.6 TB

UCSC-NVME2H-I1600

UCSC-NVME2H-I1600

NVMe SSD

NVMe SSD

Locate button/LED
Power button/LED
Status LED
Network activity LED
Warning LED (one per drive)

Disk drive activity LED (one per drive)
Drive Bay 1 (shown populated)
Drive Bay 2 (shown populated)

1 
2
3
4
5

6
7
8

Notes:

2

3

4

9
10
11
12
13

14
15
16

Drive Bay 3 (shown populated)
Drive Bay 4 (shown populated)
Drive Bay 5 (shown populated)
Drive Bay 6 (shown populated)
OCuLink console port1
Ejector handle retention button
Upper ejector handle
Lower ejector handle

1. An adapter cable (PID UCSX-C-DEBUGCBL) is required to connect the OCuLink port to the transition serial USB 

and video (SUV) octopus cable.

Cisco UCS X210c M7 Compute Node

5

DETAILED VIEWS

Figure 3  Cisco UCS X210c M7 Compute Node Front View

 (Drives and GPU option)

Storage Drives and GPU Option

1 
2
3
4
5

U.2/U.3 NVMe drive slot 1
GPU slot 1
GPU slot 2
U.2/U.3 NVMe drive slot 2
Power Button/LED

6
7
8
9
-

Activity LED
Health LED
Locator LED
Console port
-

6

Cisco UCS X210c M7 Compute Node

COMPUTE NODE STANDARD CAPABILITIES and FEATURES

COMPUTE NODE STANDARD CAPABILITIES and FEATURES

Table 1 lists the capabilities and features of the base Cisco UCS X210c M7 Compute Node. Details about how 
to configure the compute node for a listed feature or capability (for example, number of processors, drives, 
or amount of memory) are provided in CONFIGURING the Cisco UCS X210c M7 Compute Node on page 9.

Table 1   Capabilities and Features 

Capability/Feature

Description

Chassis

CPU

Chipset

Memory

Storage

The Cisco UCS X210c M7 Compute Node mounts in a Cisco UCS X9508 chassis.

■ One or two 5th Gen. Intel® Xeon® Scalable Processors or One or two 4th Gen. 

Intel® Xeon® Scalable Processors. 

■ Each CPU has 8 channels with up to 2 DIMMs per channel, for up to 16 DIMMs 

per CPU.

■ UPI Links: Up to 4 at 20GT/s

Intel® C741 series chipset

■ 32 total DDR5-5600 MT/s DIMM slots with 5th Gen. Intel® Xeon® Scalable 

Processors (16 per CPU) or 32 total DDR5-4800 MT/s DIMM slots with 4th Gen. 
Intel® Xeon® Scalable Processors

■ Up to 8TB DDR5-5600 DIMM memory capacity (32x 256GB DIMMs) with 5th 

Gen. Intel® Xeon® Scalable Processors or Up to 8TB DDR5-4800 DIMM memory 
capacity (32x 256GB DIMMs) with 4th Gen. Intel® Xeon® Scalable Processors
■ 75% peak bandwidth increase over DDR4-3200, with on-die ECC; all densities 

are Registered DIMMs (RDIMMs)

Up to 6 hot-pluggable, Solid-State Drives (SSDs), or Non-Volatile Memory Express 
(NVMe) 2.5-inch drives with a choice of enterprise-class Redundant Array of 
Independent Disks (RAID) or pass-through controllers with four lanes each of PCIe 
Gen 4 connectivity and up to 2 M.2 SATA or NVMe drives for flexible boot and 
local storage capabilities.

Additional Storage

■ Dual 80 mm SATA 3.0 M.2 cards (up to 960GB per card) on a boot-optimized 

hardware RAID controller

■ Dual 80 mm NVMe cards (up to 960GB per card) on a passthrough controller

Mezzanine Adapters 
(Front)

One front mezzanine connector that supports:

■ Up to 6 x 2.5-inch SAS and SATA RAID-compatible SSDs
■ Up to 6 x 2.5-inch NVMe PCIe drives
■ A mixture of up to six SAS/SATA or NVMe drives 
■ A mixture of up to two GPUs and up to two NVMe drives

Note: Drives require a RAID or pass-through controller in the front mezzanine 
module slot or a front mezzanine GPU module.

Cisco UCS X210c M7 Compute Node

7

COMPUTE NODE STANDARD CAPABILITIES and FEATURES

Table 1   Capabilities and Features (continued)

Capability/Feature

Description

Mezzanine Adapter 
(Rear)

■ An optional Cisco UCS Virtual Interface Card 15422 can occupy the server’s 
mezzanine slot at the bottom of the chassis. A bridge card extends this VIC’s 
2x 50Gbps of network connections up to the mLOM slot and out through the 
mLOM’s IFM connectors, bringing the total bandwidth to 100Gbps per fabric—
a total of 200Gbps per server. 

■ An optional UCS PCIe Mezz card for X-Fabric is also supported in the server’s 
mezzanine slot. This card’s I/O connectors link to the Cisco UCS X-Fabric 
modules for UCS X-series Gen4 PCIe node access.

mLOM

The modular LAN on motherboard (mLOM) cards (the Cisco UCS VIC 15420) is 
located at the rear of the compute node.

■ The Cisco UCS Virtual Interface Card VIC 15420 is a Cisco designed PCI 

Express (PCIe) based card that supports two 2x25G-KR network interfaces to 
provide Ethernet communication to the network by means of the Intelligent 
Fabric Modules (IFMs) in the Cisco UCS X9508 chassis. The Cisco UCS VIC 
15420 mLOM can connect to the rear mezzanine adapter card with a bridge 
connector.

■ The Cisco UCS Virtual Interface Card (VIC) 15230 occupies the server's 
modular LAN on motherboard (mLOM) slot, enabling up to 100 Gbps of 
unified fabric connectivity to each of the chassis Intelligent Fabric Modules 
(IFMs) for 100 Gbps connectivity per server with secure boot capability.

Video

The Cisco Integrated Management Controller (CIMC) provides video using the 
Aspeed AST2600 video/graphics controller.

Front Panel Interfaces 

OCuLink console port. Note that an adapter cable is required to connect the 
OCuLink port to the transition serial USB and video (SUV) octopus cable.

Power subsystem 

Power is supplied from the Cisco UCS X9508 chassis power supplies. 

Fans 

Integrated in the Cisco UCS X9508 chassis.

Integrated 
management processor

The built-in Cisco Integrated Management Controller enables monitoring of Cisco 
UCS X210c M7 Compute Node inventory, health, and system event logs.

Baseboard 
Management 
Controller (BMC)

ACPI

Front Indicators

ASPEED Pilot IV

Advanced Configuration and Power Interface (ACPI) 6.5 Standard Supported. ACPI 
states S0 and S5 are supported. There is no support for states S1 through S4.

■ Power button and indicator
■ System activity indicator
■ Location button and indicator

Management

■ Cisco Intersight software (SaaS, Virtual Appliance and Private Virtual 

Appliance)

■ Starting with UCS Manager (UCSM) 4.3(2) or later

Fabric Interconnect

Compatible with the Cisco UCS 6454, 64108, 6536, 6664 and UCSX-S9108-100G 
fabric interconnects. 

Chassis

Compatible with the Cisco UCS 9508 X-Series Server Chassis

8

Cisco UCS X210c M7 Compute Node

CONFIGURING the Cisco UCS X210c M7 Compute Node

CONFIGURING the Cisco UCS X210c M7 Compute Node

Follow these steps to configure the Cisco UCS X210c M7 Compute Node:

■ STEP 1 CHOOSE BASE CISCO UCS X210C M7 COMPUTE NODE SKU, page 10

■ STEP 2 CHOOSE CPU(S), page 11

■ STEP 3 CHOOSE MEMORY, page 17

■ STEP 4 CHOOSE REAR mLOM ADAPTER, page 21

■ STEP 5 CHOOSE OPTIONAL REAR MEZZANINE VIC/BRIDGE ADAPTERS, page 25

■ STEP 6 CHOOSE OPTIONAL FRONT MEZZANINE ADAPTER, page 27

■ STEP 7 CHOOSE OPTIONAL GPU PCIe NODE, page 28

■ STEP 8 CHOOSE OPTIONAL GPUs, page 29

■ STEP 9 CHOOSE OPTIONAL DRIVES, page 30

■ STEP 10 ORDER M.2 SATA SSDs AND RAID CONTROLLER, page 33

■ STEP 11 ORDER NVMe BOOT (OPTIONAL), page 34

■ STEP 12 CHOOSE OPTIONAL TRUSTED PLATFORM MODULE, page 35

■ STEP 13 CHOOSE OPERATING SYSTEM AND VALUE-ADDED SOFTWARE, page 36

■ STEP 14 CHOOSE OPTIONAL OPERATING SYSTEM MEDIA KIT, page 39

■  SUPPLEMENTAL MATERIAL, page 40

Cisco UCS X210c M7 Compute Node

9

CONFIGURING the Cisco UCS X210c M7 Compute Node

STEP 1 CHOOSE BASE CISCO UCS X210C M7 COMPUTE NODE SKU

Top Level ordering product ID (PID) of the Cisco UCS X210c M7 Compute Node as shown inTable 3

Table 2   Top level ordering PID

Product ID (PID)

Description

UCSX-M7-MLB

UCSX M7 Modular Server and Chassis MLB

Select the product ID (PID) of the Cisco UCS X210c M7 Compute Node as shown in Table 5.

Table 3   PID of the Base Cisco UCS X210c M7 Compute Node  

Product ID (PID)

Description

UCSX-210C-M7

Cisco UCS X210c M7 Compute Node without CPU, memory, drive bays, drives, VIC 
adapter, or mezzanine adapters (ordered as a UCS X9508 chassis option)

UCSX-210C-M7-U

Cisco UCS X210c M7 Compute Node without CPU, memory, drive bays, drives, VIC 
adapter, or mezzanine adapters (ordered standalone)

A base Cisco UCS X210c M7 Compute Node ordered in Table 3 does not include any components 
or options. They must be selected during product ordering.

Please follow the steps on the following pages to order components such as the following, which 
are required in a functional compute node:

■ CPUs

■ Memory

■ Cisco storage RAID or passthrough controller with drives (or blank, for no local drive 

support)

■ SAS, SATA, NVMe, M.2, or U.2/U.3 drives

■ Cisco adapters (such as the 15000 series VIC or Bridge)

10

Cisco UCS X210c M7 Compute Node

CONFIGURING the Cisco UCS X210c M7 Compute Node

STEP 2 CHOOSE CPU(S)

The standard CPU features are:

■ The 5th Gen Intel® Xeon® Scalable Processors are paired with Intel® C741 series chipset:

— Up to 64 cores

— Cache size of up to 320 MB

— Power: Up to 350Watts

— UPI Links: Up to 4 at 20GT/s

With 5th Gen Intel® Xeon® Processors, improve performance and efficiency while reducing 
costs. See 5TH GEN INTEL XEON BENEFIT PILLARS

■ The 4th Gen Intel® Xeon® Scalable Processors are paired with Intel® C741 series chipset:

— Up to 60 cores

— Cache size of up to 112.50 MB

— Power: Up to 350Watts

— UPI Links: Up to 4 at 16GT/s

With 4th Gen Intel® Xeon® processors, improve performance efficiency for critical workloads 
with the most built-in accelerators. See 4th gen Intel® Xeon® benefit pillars in LEADERSHIP 
PERFORMANCE WITH 4TH GEN INTEL® XEON® PROCESSORS.

Select CPUs

■ The available 5th Gen Intel® Xeon® Scalable CPUs are listed in Table 4. See Table 6 on page 

15 for CPU suffix notations.

■ The available 4th Gen Intel® Xeon® Scalable CPUs are listed in Table 5. See Table 6 on page 

15 for CPU suffix notations.

Table 4   Available 5th Gen. Intel® Xeon® Scalable CPUs

Product ID 

Segment/Workload

Maximum 
Socket 

Cores

Clock 
Freq

Power

Cache 
Size

Highest DDR5 DIMM 
Clock Support 

(PID)

(S)

(C)

(GHz)

(W)

(MB)

(MT/s)

8000 Series Processors

UCSX-CPU-I8592V

Cloud/SaaS/IaaS

UCSX-CPU-I8592+

2S Performance

UCSX-CPU-I8581V1

1-S Cloud/SaaS

UCSX-CPU-I8580

2S Performance

UCSX-CPU-I8571N1

1-S Networking

UCSX-CPU-I8570

2S Performance

UCSX-CPU-I8568Y+

2S Performance

2S

2S

1S

2S

1S

2S

2S

64

64

60

60

52

56

48

2.00

1.90

2.00

2.00

2.40

2.10

2.30

330

350

270

350

300

350

350

320.00

320.00

300.00

300.00

300.00

300.00

300.00

4800

5600

4800

5600

4800

5600

5600

Cisco UCS X210c M7 Compute Node

11

CONFIGURING the Cisco UCS X210c M7 Compute Node

Table 4   Available 5th Gen. Intel® Xeon® Scalable CPUs

Product ID 

Segment/Workload

Maximum 
Socket 

Cores

Clock 
Freq

Power

Cache 
Size

Highest DDR5 DIMM 
Clock Support 

(PID)

UCSX-CPU-I8562Y+

2S Performance

UCSX-CPU-I8558U1

1-Socket 
Optimized

UCSX-CPU-I8558P

Cloud/SaaS/IaaS

UCSX-CPU-I8558

2S Mainline

6000 Series Processors

UCSX-CPU-I6554S

Storage

UCSX-CPU-I6548Y+

2S Performance

UCSX-CPU-I6548N

Networking

UCSX-CPU-I6544Y

2S Performance

UCSX-CPU-I6542Y

2S Performance

UCSX-CPU-I6538Y+

2S Mainline

UCSX-CPU-I6538N

Networking

UCSX-CPU-I6534

2S Performance

UCSX-CPU-I6530

2S Mainline

UCSX-CPU-I6526Y

2S Performance

5000 Series Processors

UCSX-CPU-I5520+

2S Mainline

UCSX-CPU-I5515+

2S Performance

UCSX-CPU-I5512U1

1-Socket 
Optimized

4000 Series Processors

UCSX-CPU-I4516Y+

2S Mainline

UCSX-CPU-I4514Y

2S Mainline

UCSX-CPU-I4510T2

EDGE (IOT)

UCSX-CPU-I45102

2S Mainline

UCSX-CPU-I4509Y2

2S Mainline

3000 Series Processors

UCSX-CPU-I3508U1,2 1-Socket 
Optimized

(S)

2S

1S

2S

2S

2S

2S

2S

2S

2S

2S

2S

2S

2S

2S

2S

2S

1S

2S

2S

2S

2S

2S

1S

(C)

(GHz)

32

48

48

48

36

32

32

16

24

32

32

8

32

16

28

8

28

24

16

12

12

8

2.80

2.00

2.70

2.10

2.20

2.50

2.80

3.60

2.90

2.20

2.10

3.90

2.10

2.80

2.20

3.20

2.10

2.20

2.00

2.00

2.40

2.60

(W)

300

300

350

330

270

250

250

270

250

225

205

195

270

195

205

165

185

185

150

115

150

125

(MB)

60.00

260.00

260.00

260.00

180.00

60.00

60.00

45.00

60.00

60.00

60.00

22.50

160.00

37.50

52.50

22.50

52.50

45.00

30.00

30.00

30.00

22.50

(MT/s)

5600

4800

5600

5200

5200

5200

5200

5200

5200

5200

5200

4800

4800

5200

4800

4800

4800

4400

4400

4400

4400

4400

8

2.10

125

22.50

4400

12

Cisco UCS X210c M7 Compute Node

CONFIGURING the Cisco UCS X210c M7 Compute Node

Notes:

1. You cannot have two of these CPUs in a two-CPU configuration and you cannot later upgrade to a 2-CPU 

system with two of these CPUs.

2. 48GB and 96GB memory DIMMs not supported on UCSX-CPU-I3508U, UCSX-CPU-I4509Y, UCSX-CPU-I4510, 

UCSX-CPU-I4510T

Table 5   Available 4th Gen. Intel® Xeon® Scalable CPUs 

Product ID 

Segment/Workload

Maximum 
Socket 

Cores

Clock 
Freq

Power

Cache 
Size

Highest DDR5 DIMM 
Clock Support 

(PID)

(S)

(C)

(GHz)

(W)

(MB)

(MT/s)

8000 Series Processors

UCSX-CPU-I8490H

IMDB/Analytics

UCSX-CPU-I8480+

2S Performance

UCSX-CPU-I8471N1

5G/Networking

UCSX-CPU-I8470N

5G/Networking

UCSX-CPU-I8470

2S Performance

UCSX-CPU-I8468V

Cloud/SaaS/Media

UCSX-CPU-I8468H

IMDB/Analytics

UCSX-CPU-I8468

2S Performance

UCSX-CPU-I8462Y+

2S Performance

UCSX-CPU-I8461V1

Cloud/SaaS/Media

UCSX-CPU-I8460Y+

2S Performance

UCSX-CPU-I8460H

IMDB/Analytics

UCSX-CPU-I8458P

Cloud/SaaS/Media

UCSX-CPU-I8454H

IMDB/Analytics

UCSX-CPU-I8452Y

2S Mainline

UCSX-CPU-I8450H

IMDB/Analytics

UCSX-CPU-I8444H

IMDB/Analytics

6000 Series Processors

UCSX-CPU-I6454S

Storage

UCSX-CPU-I6448Y

2S Performance

UCSX-CPU-I6448H

IMDB/Analytics

UCSX-CPU-I6444Y

2S Performance

UCSX-CPU-I6442Y

2S Performance

UCSX-CPU-I6438Y+

2S Mainline

UCSX-CPU-I6438N

5G/Networking

2S

2S

1S

2S

2S

2S

2S

2S

2S

1S

2S

2S

2S

2S

2S

2S

2S

2S

2S

2S

2S

2S

2S

2S

60

56

52

52

52

48

48

48

32

48

40

40

44

32

36

28

16

32

32

32

16

24

32

32

1.90

2.00

1.80

1.70

2.00

2.40

2.10

2.10

2.80

2.20

2.00

2.20

2.70

2.10

2.00

2.00

2.90

2.20

2.10

2.40

3.60

2.60

2.00

2.00

350

350

300

300

350

330

330

350

300

300

300

330

350

270

300

250

270

270

225

250

270

225

205

205

112.50

105.00

97.50

97.50

105.00

97.50

105.00

105.00

60.00

97.50

105.00

105.00

82.50

82.50

67.50

75.00

45.00

60.00

60.00

60.00

45.00

60.00

60.00

60.00

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

4800

4800

4800

4800

Cisco UCS X210c M7 Compute Node

13

CONFIGURING the Cisco UCS X210c M7 Compute Node

Table 5   Available 4th Gen. Intel® Xeon® Scalable CPUs 

Product ID 

Segment/Workload

Maximum 
Socket 

Cores

Clock 
Freq

Power

Cache 
Size

Highest DDR5 DIMM 
Clock Support 

(PID)

UCSX-CPU-I6438M

Cloud/SaaS/Media

UCSX-CPU-I6434H

IMDB/Analytics

UCSX-CPU-I6434

2S Performance

UCSX-CPU-I6430

2S Mainline

UCSX-CPU-I6428N

5G/Networking

UCSX-CPU-I6426Y

2S Performance

UCSX-CPU-I6421N1

5G/Networking

UCSX-CPU-I6418H

IMDB/Analytics

UCSX-CPU-I6416H

IMDB/Analytics

UCSX-CPU-I6414U1

1S gen. purpose

5000 Series Processors

UCSX-CPU-I5420+

2S Mainline

UCSX-CPU-I5418Y

2S Mainline

UCSX-CPU-I5418N

5G/Networking

UCSX-CPU-I5416S

Storage

UCSX-CPU-I5415+

2S Performance

UCSX-CPU-I5412U1

1S gen. purpose

UCSX-CPU-I5411N1

5G/Networking

4000 Series Processors

UCSX-CPU-I4416+

2S Mainline

UCSX-CPU-I4410Y

2S Mainline

UCSX-CPU-I4410T

IOT

3000 Series Processors

UCSX-CPU-I3408U1

1S gen. purpose

Notes:

(S)

2S

2S

2S

2S

2S

2S

1S

2S

2S

1S

2S

2S

2S

2S

2S

1S

1S

2S

2S

2S

1S

(C)

32

8

8

32

32

16

32

24

18

32

28

24

24

16

8

24

24

20

12

10

(GHz)

(W)

(MB)

(MT/s)

2.20

3.70

3.70

2.10

1.80

2.50

1.80

2.10

2.20

2.00

2.00

2.00

1.80

2.00

2.90

2.10

1.90

2.00

2.00

2.70

205

195

195

270

185

185

185

185

165

250

205

185

165

150

150

185

165

165

150

150

60.00

22.50

22.50

60.00

60.00

37.50

60.00

60.00

45.00

60.00

52.50

45.00

45.00

30.00

22.50

45.00

45.00

37.50

30.00

26.25

4800

4800

4800

4400

4000

4800

4400

4800

4800

4800

4400

4400

4000

4400

4400

4400

4400

4000

4000

4000

8

1.80

125

22.50

4000

1. You cannot have two of these CPUs in a two-CPU configuration and you cannot later upgrade to a 

2-CPU system with two of these CPUs.

14

Cisco UCS X210c M7 Compute Node

CONFIGURING the Cisco UCS X210c M7 Compute Node

Table 6   CPU Suffixes

CPU Suffix

Description

Features

P

V

M

H

N

S

T

U

Y

+

Cloud (IaaS)

Cloud (SaaS)

Designed for cloud IaaS environments to deliver higher frequencies 
at constrained TDPs

Designed for high rack density, maximize VM/core, and lower 
power VM environment

Media Transcode

Designed for Media processing, AI, and HPC workloads

DB and Analytics

Designed for Data Analytics and Big Data usages

Network/5G/Edge 
(High TDP/Low 
latency)

Designed and optimized for a range of broadly-deployed network 
and 5G workload environments from Edge to the Data Center

Storage & HCI

Designed for Storage usages and workloads

Long-life Use/High 
Tcase

Designed for Network Environment-Building System (NEBS) and IoT 
market

1-Socket

Optimized for targeted platforms adequately served by the cores, 
memory bandwidth and IO capacity available from a single 
processor

General SKU with 
SST-PP

Designator is used for general SKU stack to highlight SST-PP  (Speed 
Select Technology Performance Profile) feature enabled

Feature Plus SKU

Designed to enable 1 instance of each DSA, IAA, QAT, DLB 
embedded accelerator

Cisco UCS X210c M7 Compute Node

15

CONFIGURING the Cisco UCS X210c M7 Compute Node

Supported Configurations

(1) DRAM configuration:

■ Select one or two identical CPUs from Table 4 on page 11 or Table 5 on page 13

(2) Configurations with NVMe PCIe drives:

■ Select one or two identical CPUs from Table 4 on page 11 or Table 5 on page 13 

(3) Configurations with GPUs:

■ Select one or two identical CPUs from Table 4 on page 11 or Table 5 on page 13 

(4) One-CPU Configuration

■ Choose one CPU from any one of the rows of Table 4 on page 11 or Table 5 on page 13

(5) Two-CPU Configuration

■ Choose two identical CPUs from any one of the rows of Table 4 on page 11 or Table 5 on 

page 13

16

Cisco UCS X210c M7 Compute Node

CONFIGURING the Cisco UCS X210c M7 Compute Node

STEP 3 CHOOSE MEMORY

The Table 7 below describes the main memory DIMM features supported on Cisco UCS X210c M7 
Compute Node.

CAUTION:  When populating 256GB DIMMs, the ambient temperature shall be limited to a 
maximum of 320C.

Table 7   X210c M7 Main Memory Features

Memory DIMM server technologies

Description

DDR5 memory clock speed

Operational voltage

DRAM fab density

DRAM DIMM type

4th Gen. CPU: Up to 4800MT/s 1DPC; Up to 4400MT/s 2DPC

5th Gen. CPU: Up to 5600MT/s 1DPC; Up to 4400MT/s 2DPC

1.1 Volts

16Gb, 24Gb and 32Gb

RDIMM (Registered DDR5 DIMM with on die ECC)

Memory DIMM organization

Eight memory DIMM channels per CPU; up to 2 DIMMs per channel

Maximum number of DRAM DIMM per 
server

32 (2-Socket)

DRAM DIMM Densities and Ranks

Refer to Table 8 and Table 9

Maximum system capacity (DRAM 
DIMMs only)

8TB (32x256GB)

Cisco UCS X210c M7 Compute Node

17

CONFIGURING the Cisco UCS X210c M7 Compute Node

Figure 4

  X210c M7 SFF Memory Organization

1
t
o
S

l

A1

2
t
o
S

l

A2

B1

B2

Chan A

Chan B

2
t
o
S

l

1
t
o
S

l

A2

A1

B2

B1

Chan A

Chan B

C1

C2

Chan C

Chan C

C2 C1

D1 D2

Chan D

Chan D

D2 D1

E1

E2

F1

F2

G1 G2

H1 H2

CPU 1

CPU 2

Chan E

Chan E

Chan F

Chan F

Chan G

Chan G

Chan H

Chan H

8 memory channels per CPU, 
up to 2 DIMMs per channel

32 DIMMS total (16 per CPU) 

E2

E1

F2

F1

G2

G1

H2 H1

18

Cisco UCS X210c M7 Compute Node

 
 
 
 
Select DIMMs and Memory Mirroring

CONFIGURING the Cisco UCS X210c M7 Compute Node

Select the memory configuration and whether or not you want the memory mirroring option. 
The available memory DIMMs and mirroring option are listed in Table 8. 

NOTE:  When memory mirroring is enabled, the memory subsystem simultaneously 
writes identical data to two channels. If a memory read from one of the channels 
returns incorrect data due to an uncorrectable memory error, the system 
automatically retrieves the data from the other channel. A transient or soft error in 
one channel does not affect the mirrored data, and operation continues unless there 
is a simultaneous error in exactly the same location on a DIMM and its mirrored 
DIMM. Memory mirroring reduces the amount of memory available to the operating 
system by 50% because only one of the two populated channels provides data.

Table 8   Memory Options for M7 servers with Intel® Xeon® 4th Gen. CPUs

Product ID (PID)

PID Description

Ranks/DIMM

DDR5-5600MT/s PID list1

UCSX-MRX16G1RE3

16GB DDR5-5600 RDIMM 1Rx8 (16Gb)

UCSX-MRX32G1RE3

32GB DDR5-5600 RDIMM 1Rx4 (16Gb)

UCSX-MRX64G2RE3

64GB DDR5-5600 RDIMM 2Rx4 (16Gb)

UCSX-MR128G2RG3

128GB DDR5-5600 RDIMM 2Rx4 (32Gb)

1

1

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

Table 9   Memory Options for M7 servers with Intel® Xeon® 5th Gen. CPUs1

Product ID (PID)

PID Description

Ranks/DIMM

DDR5-5600MT/s PID list

UCSX-MRX16G1RE3

16GB DDR5-5600 RDIMM 1Rx8 (16Gb)

UCSX-MRX32G1RE3

32GB DDR5-5600 RDIMM 1Rx4 (16Gb)

UCSX-MRX48G1RF32

48GB DDR5-5600 RDIMM 1Rx4 (24Gb)

UCSX-MRX96G2RF32

96GB DDR5-5600 RDIMM 2Rx4 (24Gb)

UCSX-MR128G2RG3

128GB DDR5-5600 RDIMM 2Rx4 (32Gb)

1

1

1

2

2

Cisco UCS X210c M7 Compute Node

19

CONFIGURING the Cisco UCS X210c M7 Compute Node

Table 9   Memory Options for M7 servers with Intel® Xeon® 5th Gen. CPUs1

Product ID (PID)

PID Description

Ranks/DIMM

UCSX-MR128G4RE33

128GB DDR5-5600 RDIMM 4Rx4 (16Gb)

DDR5-6400MT/s PID list

UCSX-MR256G4RG54

256GB DDR5-6400 RDIMM 4Rx4 (32Gb)

Memory Mirroring Option

N01-MMIRRORD

Memory mirroring option

Accessories/spare included with Memory configuration:

■ UCS-DDR5-BLK5 is auto included for the unselected DIMMs slots

4

4

Notes:

1. Memory will operate at the maximum speed of the Intel 5th Gen. CPU memory controller, ranging from 4400 MT/s to 

5600 MT/s.

2. 48GB and 96GB cannot be paired with Intel 5th Gen. CPUs 3508U, 4509Y, 4510, and 4510T SKUs.
3. 128GB 4Rx4 (16Gb) is now End-Of-Life and is replaced by 128GB 2Rx4 (32Gb).
4. Available in Q2’CY26
5. Any empty DIMM slot must be populated with a DIMM blank to maintain proper cooling airflow.

Memory configurations and mixing rules

■ Golden Rule: Memory on every CPU socket shall be configured identically.
■ System speed is dependent on the CPU DIMM speed support. Refer to Available 4th Gen. Intel® Xeon® 
Scalable CPUs on page 13 and Available 5th Gen. Intel® Xeon® Scalable CPUs on page 11 for DIMM 
speeds.

■ For full details on supported memory configurations see the M7 Memory Guide.

NOTE:  For full details on supported memory configurations see the M7 Memory Guide.

20

Cisco UCS X210c M7 Compute Node

CONFIGURING the Cisco UCS X210c M7 Compute Node

STEP 4 CHOOSE REAR mLOM ADAPTER

The Cisco UCS X210c M7 Compute Node must be ordered with a Cisco VIC mLOM Adapter. The 
adapter is located at the back and can operate in a single-CPU or dual-CPU configuration. 
Table 10 shows the mLOM adapter choices.

Table 10  mLOM Adapters 

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

■ VIC 15420 are supported with both X9108-IFM-25G and X9108-IFM-100G. VIC 
15420 will operate at 4x 25G with both X9108-IFM-25G and X9108-IFM-100G. 
While, VIC 15230 will operate at 4x 25G with X9108-IFM-25G and at 2x 100G with 
X9108-IFM-100G.

■ The mLOM adapter is mandatory for the Ethernet connectivity to the network 
by means of the IFMs and has x16 PCIe Gen4 connectivity with Cisco UCS VIC 
15420 or x16 Gen4 connectivity with Cisco UCS VIC 15230 towards the CPU1.

■ There is no backplane in the Cisco UCS X9508 chassis; thus, the compute nodes 

directly connect to the IFMs using Orthogonal Direct connectors.

■ Figure 5 shows the location of the mLOM and rear mezzanine adapters on the 
Cisco UCS X210c M7 Compute Node. The bridge adapter connects the mLOM 
adapter to the rear mezzanine adapter.

Cisco UCS X210c M7 Compute Node

21

CONFIGURING the Cisco UCS X210c M7 Compute Node

Figure 5  Location of mLOM and Rear Mezzanine Adapters

mLOM Adapter

Bridge Adapter

Rear Mezzanine Adapter

22

Cisco UCS X210c M7 Compute Node

CONFIGURING the Cisco UCS X210c M7 Compute Node

Figure 6 shows the network connectivity from the mLOM out to the 25G IFMs.

Figure 6  Network Connectivity 25G IFMs

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

UCS X210c mLOM OD connectors (2)

Cisco UCS X210c Compute Node

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

Cisco UCS X210c M7 Compute Node

23

 
 
 
 
CONFIGURING the Cisco UCS X210c M7 Compute Node

Figure 7 shows the network connectivity from the mLOM out to the 100G IFMs. 

Figure 7  Network Connectivity 100G IFMs

To Fabric Interconnect 

To Fabric Interconnect 

UCS X9508 Chassis

IFM-1

IFM-2

Cisco ASIC

Cisco ASIC

KR Lanes

IFM OD connectors (1 for each IFM)

UCS 210c mLOM OD connectors (2)

4
R
K
-

G
0
0
1

KR Lanes

4
R
K
-

G
0
0
1

Cisco UCS X210c Compute Node

Empty

 Mezzanine Slot

MAC1

Cisco ASIC

MAC0

Bridge Adapter

mLOM Adapter

24

Cisco UCS X210c M7 Compute Node

CONFIGURING the Cisco UCS X210c M7 Compute Node

STEP 5 CHOOSE OPTIONAL REAR MEZZANINE VIC/BRIDGE ADAPTERS

The Cisco UCS X210c M7 Compute Node has one rear mezzanine adapter connector which can 
have a UCS VIC 15422 Mezz card that can be used as a second VIC card on the compute node for 
network connectivity or as a connector to the X440p PCIe node via X-Fabric modules. The same 
mezzanine slot on the compute node can also accommodate a pass-through mezzanine adapter 
for X-Fabric which enables compute node connectivity to the X440p PCIE node. Refer to 
Table 11 for supported adapters.

Table 11  Available Rear Mezzanine Adapters  

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

NOTE:  The UCSX-V4-PCIME-D rear mezzanine card for X-Fabric has PCIe Gen4 x16 
connectivity towards each CPU1 and CPU2. Additionally, the UCSX-V4-PCIME-D also 
provides two PCIe Gen4 x16 to each X-fabric. This rear mezzanine card enables 
connectivity from the X210c M7 Compute Node to the X440p PCIe node.

Cisco UCS X210c M7 Compute Node

25

CONFIGURING the Cisco UCS X210c M7 Compute Node

Table 12  Throughput Per UCS X210c M7 Server

X210c M7 Compute 
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

X210c 
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

VIC 15230

VIC 15230

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

■ One of mLOM VIC from Table 10 is always required.

■ If a UCSX-ME-V5Q50G-D rear mezzanine VIC card is installed, a UCSX-V5-BRIDGE-D VIC 

bridge card is included and connects the mLOM to the mezzanine adapter.

■ The UCSX-ME-V5Q50G-D rear mezzanine card has Ethernet connectivity to the IFM using the 
UCSX-V5-BRIDGE-D and has a PCIE Gen4 x16 connectivity towards CPU2. Additionally, the 
UCSX-ME-V5Q50G-D also provides two PCIe Gen4 x16 to each X-fabric.

■ All the connections to Cisco UCS X-Fabric 1 and Cisco UCS X-Fabric 2 are through the Molex 

Orthogonal Direct (OD) connector on the mezzanine card.

■ The rear mezzanine card has 32 x16PCIe lanes to each Cisco UCS X-Fabric for I/O expansion 

to enable resource consumption from the PCIe resource nodes.

26

Cisco UCS X210c M7 Compute Node

 
CONFIGURING the Cisco UCS X210c M7 Compute Node

STEP 6 CHOOSE OPTIONAL FRONT MEZZANINE ADAPTER

The Cisco UCS X210c M7 Compute Node has one front mezzanine connector that can 
accommodate one of the following mezzanine cards:

■ Pass-through controller for up to 6 U.2/U.3 NVMe drives

■ RAID controller (RAID levels 0, 1, 5, 6, 10, and 50) for 6 SAS/SATA/U.3 NVMe drives or up to 

4 U.2 NVMe drives (drive slots 1-4) and SAS/SATA/U.3 NVMe (drive slots 5-6)

■ GPU Front Mezz to Support up to 2 U.2/U.3 NVMe drives and 2 NVIDIA T4 GPUs.

NOTE:  

■ The Cisco UCS X210c M7 Compute Node can be ordered with or without the 

front mezzanine adapter. Refer to Table 13 Available Front Mezzanine 
Adapters

■ Only one Front Mezzanine connector or Front GPU can be selected per Server.

■ RAID with NVMe drives is only supported with the NVMe U.3 drives as they 

connect to the RAID controller and RAID is not supported with the U.2 NVME 
drives as they directly interface with the server via the PCIe bus.

Table 13  Available Front Mezzanine Adapters  

Product ID(PID)

PID Description

UCSX-X10C-PT4F-D

Cisco UCS X210c M7 Compute Node compute pass through 
controller for up to 6 NVMe drives

UCSX-X10C-RAIDF-D

Cisco UCS X210c M7 Compute Node RAID controller w/4GB 
Cache, with LSI 3900 for up to 6 SAS/SATA/NVMe drives 
(SAS/SATA and NVMe drives can be mixed)

Connector Type

Front Mezzanine

Front Mezzanine

UCSX-X10C-GPUFM-D

UCS X10c Compute Node GPU Front Mezz

Front Mezzanine

Cisco UCS X210c M7 Compute Node

27

CONFIGURING the Cisco UCS X210c M7 Compute Node

STEP 7 CHOOSE OPTIONAL GPU PCIe NODE

 Refer to Table 14 for GPU PCIe Node

Table 14  GPU PCIe Node

Product ID(PID)

PID Description

UCSX-440P-D

UCS X-Series Gen4 PCIe node

NOTE:  

■ If UCSX-440P-D (GPU Node) is selected, the Rear MEZZ PID (UCSX-ME-V5Q50G or 

UCSX-V4-PCIME) must also be included for UCSX-210C-M7-U.

■ If UCSX-X10C-GPUFM-D is selected, the Riser PID UCSX-RIS-B-440P is required.

■ If both UCSX-X10C-GPUFM-D and UCSX-GPU-T4MEZZ-D are selected, GPUs 

cannot be selected on UCSX-440P-D (GPU Node).

■ UCSX-440P not offered with standalone compute node UCSX-210C-M7-U

28

Cisco UCS X210c M7 Compute Node

CONFIGURING the Cisco UCS X210c M7 Compute Node

STEP 8 CHOOSE OPTIONAL GPUs

Select GPU Options

NOTE:  

■ Windows Server 2019 is not supported with the Intel FLex 140 & 170 GPUs

■ If UCSX-440P and UCSX-X10C-GPUFM-D are selected, only GPU PID combinations 
UCSX-GPU-FLEX140 + UCSX-GPU-FLX140MZ or UCSX-GPU-L4 + UCSX-GPU-L4-MEZZ 
are allowed.

■ No mixing of GPU types is allowed; UCSX-X10C-GPUFM-D and UCSX-440P-D must 

use the same GPUs.

The available Compute node GPU options are listed in Table 15

Table 15  Available PCIe GPU Card supported on the Compute Node Front Mezz

GPU Product ID (PID) PID Description

UCSX-GPU-T4MEZZ-D NVIDIA T4 GPU PCIE 75W 16GB, MEZZ form factor
UCSX-GPU-L4-MEZZ
UCSX-GPU-FLX140MZ

NVIDIA GPU L4, Gen4x16, 1 Slot, HHHL, 70W 24GB, PCIe
Intel GPU Flex 140, Gen4x8, HHHL, 75W PCIe

The available PCIe node GPU options are listed in Table 16.

Table 16  Available PCIe GPU Cards supported on the PCIe Node (UCSX-440P-D)

GPU Product ID (PID) PID Description

Maximum number of GPUs per node

UCSX-GPU-A16-D
UCSX-GPU-A40-D
UCSX-GPU-A100-80-D

UCSX-GPU-H100-80
UCSX-GPU-L4
UCSX-GPU-L40
UCSX-GPU-L40S
UCSX-GPU-FLEX1402
UCSX-GPU-FLEX1702

NVIDIA A16 PCIE 250W 4X16GB
TESLA A40 RTX, PASSIVE, 300W, 48GB
TESLA A100, PASSIVE, 300W, 80GB1
TESLA H100, PASSIVE, 350W, 80GB
NVIDIA L4 Tensor Core, 70W, 24GB
NVIDIA L40 300W, 48GB wPWR CBL
NVIDIA L40S: 350W, 48GB, 2-slot FHFL GPU
Intel GPU Flex 140, Gen4x8, HHHL, 75W PCIe

Intel GPU Flex 170, Gen4x16, HHFL, 150W 
PCIe

UCSX-GPU-H100-NVL3 NVIDIA H100 NVL, 400W, 94GB, 2-slot FHFL 

GPU

Notes:

1. Required power cables are included with the riser cards in the X440p PCIe node.
2. Windows Server 2019 is not supported with the Intel Flex 140 & 170 GPUs.
3. NVIDIA NVLink Bridge is not supported.

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

Cisco UCS X210c M7 Compute Node

29

CONFIGURING the Cisco UCS X210c M7 Compute Node

STEP 9 CHOOSE OPTIONAL DRIVES

The Cisco UCS X210c M7 Compute Node can be ordered with or without drives. The drive options 
are:

■ One to six 2.5-inch small form factor SAS/SATA SSDs or PCIe U.2/U.3 NVMe drives

— Hot-pluggable

— Sled-mounted

Select one or two drives from the list of supported drives available in Table 17.

Table 17  Available Drive Options  

Product ID (PID)

Description

Drive 
Type

Speed  Size

SAS/SATA SSDs1,2,3
Self-Encrypted Drives (SED)
UCSXSD960GBKNK9-D

12G

960GB

SAS

UCSXSD800GBKNK9-D
UCSX-SD16TBKANK9D

960GB 2.5" Enterprise value 12G SAS SSD (1X endurance, 
FIPS)
800GB Enterprise performance SAS SSD (3X DWPD, SED)
1.6TB 2.5in Enter Perf 24G SAS Kioxia PM7 SSD (3X 
SED-FIPS)
3.8TB 2.5in Enter Value 24G SAS Kioxia PM7 SSD (SED-FIPS) SAS
7.6TB 2.5in Enter Value 24G SAS Kioxia PM7 SSD (SED-FIPS) SAS
960GB 2.5in Enter Value 6G SATA Micron G2 SSD (SED)
1.9TB 2.5in Enter Value 6G SATA Micron G2 SSD (SED)
3.8TB 2.5in Enter Value 6G SATA Micron G2 SSD (SED)
7.6TB 2.5in Enter Value 6G SATA Micron G2 SSD (SED)

UCSX-SD38TBKANK9D 
UCSX-SD76TBKANK9D
UCSX-SD960GM2NK9D
UCSX-SD19TEM2NK9D
UCSX-SD38TEM2NK9D
UCSX-SD76TEM2NK9D
Enterprise Performance SSDs (high endurance, supports up to 3X DWPD (drive writes per day))
UCSX-SD16TKA3XEPD

1.6TB 2.5in Enter Perf 24G SAS Kioxia PM7 SSD 

12G
12G
6G
6G
6G
6G

SATA
SATA
SATA
SATA

SAS
SAS

12G

12G

SAS

800GB
1.6TB

3.8TB
7.6TB
960GB
1.6TB
3.8TB
7.6TB

1.6TB

UCSXSD32TKA3XEP-D

(3X endurance)
3.2TB 2.5in Enter Perf 24G SAS Kioxia PM7 SSD 

UCSX-SD19T63XEP-D

UCSXSD480G63XEP-D

UCSXSD480GBM3XEPD

UCSXSD960GBM3XEPD

UCSX-SD19TBM3XEPD

UCSX-SDB960OA1P

(3X endurance)
1.9TB 2.5 inch Enterprise performance 6G SATA SSD 
(3X endurance)
480GB 2.5in Enterprise performance 6G SATA SSD 
(3X endurance)
480GB 2.5in Enter Perf 6G SATA Micron G2 SSD 

(3X)
960GB 2.5in Enter Perf 6G SATA Micron G2 SSD 

(3X)
1.9TB 2.5in Enter Perf 6G SATA Micron G2 SSD 

(3X)
960GB 2.5in 15mm Solidigm S4620 Enter Perf 6G SATA 3X 
SSD

SAS

12G

3.2TB

SATA

6G

1.9TB

SATA

6G

480GB

SATA

6G

480GB

SATA

6G

960GB

SATA

6G

1.9TB

SATA

6G

960GB

30

Cisco UCS X210c M7 Compute Node

CONFIGURING the Cisco UCS X210c M7 Compute Node

Table 17  Available Drive Options (continued) 

Product ID (PID)

Description

UCSX-SDB3T8OA1P

3.8TB 2.5in 15mm Solidigm S4620 Enter Perf 6G SATA 3X 
SSD

Drive 
Type

Speed  Size

SATA

6G

3.8TB

SATA
SATA
SATA
SATA
SATA
SATA
SATA
SATA

Enterprise Value SSDs (Low endurance, supports up to 1X DWPD (drive writes per day)) 
UCSXSD240GBM1XEVD
UCSXSD480GBM1XEVD
UCSXSD960GBM1XEVD
UCSX-SD16TBM1XEVD
UCSX-SD19TBM1XEVD
UCSX-SD38TBM1XEVD
UCSX-SD76TBM1XEVD
UCSX-SDB960SA1VD

240GB 2.5in Enter Value 6G SATA Micron G2 SSD
480 GB 2.5in Enter Value 6G SATA Micron G2 SSD
960GB 2.5in Enter Value 6G SATA Micron G2 SSD
1.6TB 2.5in Enter Value 6G SATA Micron G2 SSD
1.9TB 2.5in Enter Value 6G SATA Micron G2 SSD
3.8TB 2.5in Enter Value 6G SATA Micron G2 SSD
7.6TB 2.5in Enter Value 6G SATA Micron G2 SSD
960GB 2.5in 6G SATA Enter Value 1X Samsung G1PM893A 
SSD
1.9TB 2.5in 6G SATA Enter Value 1X Samsung G1PM893A 
SSD
3.8TB 2.5in 6G SATA Enter Value 1X Samsung G1PM893A 
SSD
7.6TB 2.5in 6G SATA Enter Value 1X Samsung G1PM893A 
SSD
1.9TB 2.5in Enter Value 24G SAS Kioxia PM7 SSD
3.8TB 2.5in Enter Value 24G SAS Kioxia PM7 SSD
7.6TB 2.5in Enter Value 24G SAS Kioxia PM7 SSD
15.3TB 2.5in Enter Value 24G SAS Kioxia PM7 SSD

UCSX-SDB1T9SA1VD

UCSX-SDB3T8SA1VD

UCSX-SDB7T6SA1VD

UCSX-SD19TKA1XEVD
UCSXSD38TKA1XEV-D
UCSX-SD76TKA1XEVD
UCSX-SD15TKA1XEVD
NVMe4,5,6
UCSX-NVB1T6O1P

UCSX-NVB3T8O1V

UCSX-NVB7T6O1V

UCSX-NVB15TO1V

UCSX-NVB3T2O1P

UCSX-NVB6T4O1P

UCSX-NVB1T9O1V 

UCSX-NVB15T3O1L

UCSX-NVB12T8O1P

1.6TB 2.5in U.2 15mm Solidigm P5620 Hg Perf Hg End 3X 
NVMe
3.8TB 2.5in U.2 15mm Solidigm P5520 Hg Perf Med End 1X 
NVMe
7.6TB 2.5in U.2 15mm Solidigm P5520 Hg Perf Med End 1X 
NVMe
15.3TB 2.5in U.2 15mm Solidigm P5520 Hg Perf Med End 
1X NVMe
3.2TB 2.5in U.2 15mm Solidigm P5620 Hg Perf Hg End 3X 
NVMe
6.4TB 2.5in U.2 15mm Solidigm P5620 Hg Perf Hg End 3X 
NVMe
1.9TB 2.5in U.2 15mm Solidigm P5520 Hg Perf Med End 1X 
NVMe
15.3TB 2.5in U.2 15mm SolidigmP5316 HgPerf LowEnd 
<0.5X NVMe
12.8TB 2.5in U.2 15mm Solidigm P5620 Hg Perf Hg End 3X 
NVMe

6G
6G
6G
6G
6G
6G
6G
6G

240GB
480GB
960GB
1.6TB
1.9TB
3.8TB
7.6TB
960GB

SATA

6G

1.9TB

SATA

6G

3.8TB

SATA

6G

7.6TB

SAS
SAS
SAS
SAS

12G
12G
12G
12G

1.9TB
3.8TB
7.6TB
15.3TB

NVMe

U.2

1.6 TB

NVMe

U.2

3.8 TB

NVMe

U.2

7.6 TB

NVMe

U.2

15.3TB

NVMe

U.2

3.2TB

NVMe

U.2

6.4TB

NVMe

U.2

1.9TB

NVMe

U.2

15.3TB

NVMe

U.2

12.8TB

UCSX-NVMEG4M1536D 15.3TB 2.5in U.3 Micron 7450 NVMe High Perf Medium 

NVMe

U.3

15.3TB

Endurance

Cisco UCS X210c M7 Compute Node

31

CONFIGURING the Cisco UCS X210c M7 Compute Node

Table 17  Available Drive Options (continued) 

Product ID (PID)

Description

Drive 
Type

Speed  Size

UCSX-NVMEG4M1600D 1.6TB 2.5in U.3 Micron 7450 NVMe High Perf High 

NVMe

U.3

1.6TB

Endurance

UCSX-NVMEG4M6400D 6.4TB 2.5in U.3 Micron 7450 NVMe High Perf High 

NVMe

U.3

6.4TB

Endurance

UCSX-NVMEG4M7680D 7.6TB 2.5in U.3 Micron 7450 NVMe High Perf Medium 

NVMe

U.3

7.6TB

UCSX-NVB3T8M2V97

UCSX-NVB1T9M2V97

UCSX-NVB7T6M2V97

UCSX-NVB15T3M2V97

UCSX-NVB960M2V

UCSX-NVB1T9M2V

UCSX-NVB3T2M2P

UCSX-NVB3T8M2V

Endurance
3.8TB 2.5in U.3 15mm Micron 7500 HgPerf MedEnd 1X 
NVMe FIPS
1.9TB 2.5in U.3 15mm Micron 7500 HgPerf MedEnd 1X 
NVMe FIPS
7.6TB 2.5in U.3 15mm Micron 7500 HgPerf MedEnd 1X 
NVMe FIPS
15.3TB 2.5in U.3 15mm Micron 7500 HgPerf MedEnd 1X 
NVMe FIPS
960GB 2.5in U.3 15mm Micron 7500 Hg Perf Med End 1X 
NVMe
1.9TB 2.5in U.3 15mm Micron 7500 Hg Perf Med End 1X 
NVMe
3.2TB 2.5in U.3 15mm Micron 7500 Hg Perf Hg End 3X 
NVMe
3.8TB 2.5in U.3 15mm Micron 7500 Hg Perf Med End 1X 
NVMe

NVMe

U.3

3.8 TB

NVMe

U.3

1.9 TB

NVMe

U.3

7.6 TB

NVMe

U.3

15.3 TB

NVMe

U.3

960GB

NVMe

U.3

1.9 TB

NVMe

U.3

3.2TB

NVMe

U.3

3.8 TB

NOTE:  Cisco uses solid state drives from several vendors. All solid state drives are subject to physical write 
limits and have varying maximum usage limitation specifications set by the manufacturer. Cisco will not 
replace any solid state drives that have exceeded any maximum usage specifications set by Cisco or the 
manufacturer, as determined solely by Cisco.

Notes:

1. SSD drives require the UCSX-X10C-RAIDF-D front mezzanine adapter
2. For SSD drives to be in a RAID group, two identical SSDs must be used in the group.
3. If SSDs are in JBOD Mode, the drives do not need to be identical.
4.  NVMe drives require a front mezzanine the UCSX-X10C-PT4F-D pass through controller or UCSX-X10C-RAIDF-D 

RAID controller for RAID support

5. A maximum of 4 U.2 NVMe drives or 6 U.3 NVMe drives can be ordered with RAID controller.
6. A maximum of 2 NVMe drives can be ordered with Front Mezzanine GPU module.
7. Micron 7500 SED-FIPS cannot be used for boot in direct attach mode. They can be used for boot via RAID 
controller. Micron 7500 SED-FIPS are supported with 5th Gen Intel® Xeon® processors configurations only.

32

Cisco UCS X210c M7 Compute Node

CONFIGURING the Cisco UCS X210c M7 Compute Node

STEP 10 ORDER M.2 SATA SSDs AND RAID CONTROLLER

■ Cisco 6GB/s SATA Boot-Optimized M.2 RAID Controller (included): Boot-Optimized RAID controller 

(UCSX-M2-HWRD-FPS) for hardware RAID across two SATA M.2 storage modules. The Boot-Optimized RAID 
controller plugs into the motherboard and the M.2 SATA drives plug into the Boot-Optimized RAID 
controller.

NOTE:  

■ The UCSX-M2-HWRD-FPS is auto included with the server configuration

■ The UCSX-M2-HWRD-FPS controller supports RAID 1 and JBOD mode and is available 

only with 240GB, 480GB, and 960GB M.2 SATA SSDs.

■ Cisco IMM is supported for configuring of volumes and monitoring of the controller 

and installed SATA M.2 drives

■ Hot-plug replacement is not supported. The compute node must be powered off to 

replace. 

■ The Boot-Optimized RAID controller supports Windows and Linux Operating Systems

Table 18  Boot-Optimized RAID controller (auto included)

Product ID (PID)

PID Description

UCSX-M2-HWRD-FPS

UCSX Front panel with M.2 RAID controller for SATA drives

■ Select Cisco M.2 SATA SSDs: Order one or two matching M.2 SATA SSDs. This connector accepts the 

boot-optimized RAID controller (see Table 18). Each boot-optimized RAID controller can accommodate 
up to two SATA M.2 SSDs shown in Table 19.

NOTE:  

■ Each boot-optimized RAID controller can accommodate up to two SATA M.2 SSDs 

shown in Table 19. The boot-optimized RAID controller plugs into the 
motherboard.

■ It is recommended that M.2 SATA SSDs be used as boot-only devices.

■ The SATA M.2 drives can boot in UEFI mode only. Legacy boot mode is not 

supported.

Table 19  M.2 SATA SSDs

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

Cisco UCS X210c M7 Compute Node

33

CONFIGURING the Cisco UCS X210c M7 Compute Node

STEP 11 ORDER NVMe BOOT

 (OPTIONAL)

Table 20  NVMe BOOT

Product ID (PID)

PID Description

UCSX-M2-PT-FPN

UCSX Front Panel w/M.2 Pass Through Controller for NVME Drv

Table 21  M.2 NVMe

Product ID (PID)

PID Description

UCSX-NVM2-400GB
UCSX-NVM2-960GB

400GB M.2 Boot NVMe 
960GB M.2 Boot NVMe

34

Cisco UCS X210c M7 Compute Node

CONFIGURING the Cisco UCS X210c M7 Compute Node

STEP 12    CHOOSE OPTIONAL TRUSTED PLATFORM MODULE 

Trusted Platform Module (TPM) is a computer chip or microcontroller that can securely store 
artifacts used to authenticate the platform or Cisco UCS X210c M7 Compute Node. These 
artifacts can include passwords, certificates, or encryption keys. A TPM can also be used to 
store platform measurements that help ensure that the platform remains trustworthy. 
Authentication (ensuring that the platform can prove that it is what it claims to be) and 
attestation (a process helping to prove that a platform is trustworthy and has not been 
breached) are necessary steps to ensure safer computing in all environments.

Table 22  Available TPM Option  

Product ID (PID)

Description

UCSX-TPM-002C-D

UCSX-TPM-002D-D

TPM 2.0, TCG, FIPS140-2, CC EAL4+ Certified, for servers

TPM 2.0 TCG FIPS140-2 CC+ Cert M7 Intel MSW2022 Compliant

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
node. If a Cisco UCS X210c M7 Compute Node with a TPM is returned, the 
replacement Cisco UCS X210c M7 Compute Node must be ordered with a new 
TPM. If there is no existing TPM in the Cisco UCS X210c M7 Compute Node, you 
can install a TPM 2.0. Refer to the following document for Installation location 
and instructions:

https://www.cisco.com/content/en/us/td/docs/unified_computing/ucs/x/hw/210c
-m6/install/b-cisco-ucs-x210c-m7-install.html

Cisco UCS X210c M7 Compute Node

35

CONFIGURING the Cisco UCS X210c M7 Compute Node

STEP 13 CHOOSE OPERATING SYSTEM AND VALUE-ADDED SOFTWARE

■ Operating System (Table 23)

NOTE:  

■ See this link for operating system guidance: 

https://ucshcltool.cloudapps.cisco.com/public/

Table 23  Operating System 

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

36

Cisco UCS X210c M7 Compute Node

CONFIGURING the Cisco UCS X210c M7 Compute Node

Table 23  Operating System (continued)

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

Cisco UCS X210c M7 Compute Node

37

CONFIGURING the Cisco UCS X210c M7 Compute Node

Table 23  Operating System (continued)

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

38

Cisco UCS X210c M7 Compute Node

CONFIGURING the Cisco UCS X210c M7 Compute Node

STEP 14 CHOOSE OPTIONAL OPERATING SYSTEM MEDIA KIT

Select the optional operating system media listed in Table 24.

Table 24  OS Media  

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

Cisco UCS X210c M7 Compute Node

39

SUPPLEMENTAL MATERIAL

SUPPLEMENTAL MATERIAL

Simplified Block Diagram

A simplified block diagram of the Cisco UCS X210c M7 Compute Node system board is shown in Figure 8.

Figure 8  

Cisco UCS X210c M7 Compute Node Simplified Block Diagram (VIC 25G with Drives)

Cisco UCS X210c M7 Node

Disk 1

. . . . . . .

Disk n

Local Storage

Front  MEZZ Adapter

RAID 
Controller

PCIe Gen4x24

PCIe Gen4x16

CPU 1 (front CPU)

PCIe Gen4x16

Rear MEZZ Adapter

SGMII

Main ASIC

r
o
t
c
e
n
n
o
C
Z
Z
E
M
e
d
o
N

PCIe Gen4x16

PCIe Gen4x16

PCIe Gen4x16

2x25G-KR

2x25G-KR

UPI Link

PCIe Gen4x16

CPU 2  (rear CPU)

PCIe Gen4x16

PCIe Gen4x16

Rear mLOM Adapter

Bridge Adapter

r
o
t
c
e
n
n
o
C
e
g
d
i
r
B

r
o
t
c
e
n
n
o
C
e
g
d
i
r
B

SGMII

Main ASIC

PCIe Gen4x16

PCIe Gen4x16

r
o
t
c
e
n
n
o
C
M
O
L
m
e
d
o
N

R
K
-
G
5
2
x
2

R
K
-
G
5
2
x
2

R
K
-
G
5
2
x
2

R
K
-
G
5
2
x
2

FEM-1 OD
Connector

FEM-2 OD
Connector

IFM-1 OD
Connector

IFM-2 OD
Connector

40

Cisco UCS X210c M7 Compute Node

 
 
 
 
 
 
Figure 9  

Cisco UCS X210c M7 Compute Node Simplified Block Diagram (VIC 100G with Drives)

Cisco UCS X210c M7 Node

Disk 1

. . . . . . .

Disk n

Local Storage

SUPPLEMENTAL MATERIAL

Front  MEZZ Adapter

PCIe Gen4x24

PCIe Gen4x16

CPU 1 (front CPU)

PCIe Gen4x16

Rear MEZZ Adapter

PCIe Mezz Card for X-Fabric

PCIe Gen4x16

PCIe Gen4x16

r
o
t
c
e
n
n
o
C
M
O
L
m
e
d
o
N

UPI Links

PCIe Gen4x16

CPU 2  (rear CPU)

Rear mLOM Adapter

SGMII

Main ASIC

PCIe Gen4x16

r
o
t
c
e
n
n
o
C
M
O
L
m
e
d
o
N

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

IFM-1 OD
Connector

IFM-2 OD
Connector

IFM-1 OD
Connector

IFM-2 OD
Connector

Cisco UCS X210c M7 Compute Node

41

 
 
 
 
SUPPLEMENTAL MATERIAL

Figure 10  

Cisco UCS X210c M7 Compute Node Simplified Block Diagram (VIC 25G with Drives and GPUs)

Cisco UCS X210c M7 Node

Disk 1
Disk 1

Disk 2

GPU 1

GPU 2

Local Storage

GPUs

Front  MEZZ Adapter

PCIe Gen4x24

PCIe Gen4x16

CPU 1 (front CPU)

PCIe Gen4x16

Rear MEZZ Adapter

SGMII

Main ASIC

r
o
t
c
e
n
n
o
C
Z
Z
E
M
e
d
o
N

PCIe Gen4x16

PCIe Gen4x16

PCIe Gen4x16

2x25G-KR

2x25G-KR

UPI Links

PCIe Gen4x16

CPU 2  (rear CPU)

PCIe Gen4x16

PCIe Gen4x16

Rear mLOM Adapter

Bridge Adapter

r
o
t
c
e
n
n
o
C
e
g
d
i
r
B

r
o
t
c
e
n
n
o
C
e
g
d
i
r
B

SGMII

Main ASIC

PCIe Gen4x16

PCIe Gen4x16

r
o
t
c
e
n
n
o
C
M
O
L
m
e
d
o
N

R
K
-
G
5
2
x
2

R
K
-
G
5
2
x
2

R
K
-
G
5
2
x
2

R
K
-
G
5
2
x
2

FEM-1 OD
Connector

FEM-2 OD
Connector

IFM-1 OD
Connector

IFM-2 OD
Connector

42

Cisco UCS X210c M7 Compute Node

 
 
 
 
 
 
Figure 11  Cisco UCS X210c M7 Compute Node Simplified Block Diagram (VIC 100G with Drives and GPUs) 

SUPPLEMENTAL MATERIAL

Cisco UCS X210c M7 Node

Disk 1
Disk 1

Disk 2

GPU 1

GPU 2

Local Storage

GPUs

Front  MEZZ Adapter

PCIe Gen4x24

PCIe Gen4x16

CPU 1 (front CPU)

PCIe Gen4x16

Rear MEZZ Adapter

PCIe Mezz Card for X-Fabric

PCIe Gen4x16

PCIe Gen4x16

r
o
t
c
e
n
n
o
C
M
O
L
m
e
d
o
N

UPI Links

PCIe Gen4x16

CPU 2  (rear CPU)

PCIe Gen4x16

PCIe Gen4x16

Rear mLOM Adapter

SGMII

Main ASIC

PCIe Gen4x16

r
o
t
c
e
n
n
o
C
M
O
L
m
e
d
o
N

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

IFM-1 OD
Connector

IFM-2 OD
Connector

IFM-1 OD
Connector

IFM-2 OD
Connector

Cisco UCS X210c M7 Compute Node

43

 
 
 
 
SUPPLEMENTAL MATERIAL

System Board

A top view of the Cisco UCS X210c M7 Compute Node system board is shown in Figure 12.

Figure 12  Cisco UCS X210c M7 Compute Node System Board

1

3

2

4

P1 F1

P1 F2

P1 E1

P1 E2

P1 H1

P1 H2

P1 G1

P1 G2

P1 C2

P1 C1

P1 D2

P1 D1

P1 A2

P1 A1

P1 B2

P1 B1

P2 B1

P2 B2

P2 A1

P2 A2

P2 D1

P2 D2

P2 C1

P2 C2

P2 G2

P2 G1

P2 H2

P2 H1

P2 E2

P2 E1

P2 F2

P2 F1

5

6

7

4
7
9
8
0
3

1

2

3

4

Front mezzanine slot for SAS/SATA or 
NVMe drives and M.2 Controllers.

DIMM slots (32 maximum)

CPU 1 slot (shown populated)

CPU 2 slot (shown populated)

2

5

6

7

-

Rear mezzanine slot, which supports a 
mezzanine card with standard or extended 
mLOM. 

If an extended mLOM slot is used, it occupies 
this slot, such that no rear mezzanine card can 
be installed.

Bridge adapter (for connecting the mLOM to the 
rear mezzanine card)

mLOM slot for a standard or extended mLOM

-

Please refer to the Cisco UCS X210c M7 Compute Node Installation Guide for installation procedures.

44

Cisco UCS X210c M7 Compute Node

 
UPGRADING or REPLACING CPUs and Memory

UPGRADING or REPLACING CPUs and Memory

■ Refer to Cisco UCS X210c M7 Server Installation and Service Guide to upgrading or replacing the CPUs

■ Refer to Cisco UCS X210c M7 Server Installation and Service Guide to upgrading or replacing the Memory

Cisco UCS X210c M7 Compute Node

45

5TH GEN INTEL XEON BENEFIT PILLARS

5TH GEN INTEL XEON BENEFIT PILLARS

INTEL® XEON® PROCESSORS

5TH GEN INTEL® XEON® PROCESSORS

INTEL XEON HEADLINE: Trusted performance. Exceptional efficiency.

5TH GEN INTEL XEON VALUE PROPOSITION:

Get impressive performance per watt gains across all your workloads,1 plus outsized performance and TCO 
in AI, database, networking, and HPC.2 5th Gen Intel® Xeon® processors deliver more compute and faster 
memory3 at the same TDP as the previous generation. It’s software- and platform-compatible with the 
previous generation, so you can minimize testing and validation when deploying new systems.

AI-FOCUSED LEAD MESSAGE: The processor designed for AI

The processor designed for AI With AI acceleration in every core, 5th Gen Intel® Xeon® processors are ready 
to handle your demanding AI workloads—including inference and fine tuning on models up to 20 billion 
parameters4—before you need to add discrete accelerators.

5TH GEN INTEL XEON BENEFIT PILLARS

:

Performance

AI

Efficiency

Quality and security

■  21% average 

■  Less than 100 ms 

■  Up to 10x higher 

■  Software- and 

performance gain at 
the same TDP as 4th 
Gen Intel® Xeon® 
processors1,2

second-token latency 
on LLMs under 20 
billion parameters6

performance per watt 
using built-in 
accelerators9

pin-compatible with 
4th Gen Intel® Xeon® 
processors

■  Up to 2.7x better AI 

■   Up to 3x higher 

performance per watt 
with built-in 
accelerators vs. 4th 
Gen AMD EPYC 
processors10

■  Up to 16% memory 

bandwidth 
improvement3 and 2.7x 
increased last level 
cache4 vs. 4th Gen 
Intel® Xeon® 
processors

■  84% average 

performance gain over 
3rd Gen Intel® Xeon® 
processors5

■  Out-of-box software 
performance using 
accelerators

inference performance 
vs. 4th Gen AMD EPYC 
processors7

■  Up to 14x better AI 

training and inference 
performance vs. 3rd 
Gen Intel® Xeon® 
processors8

■  Software tools and 

ecosystem to 
accelerate AI

■  Confidential computing 

to help protect AI 
models

■  Silicon-based security 
features, confidential 
computing, and trust 
services

■  Leading quality and 
enhanced telemetry

■  Largest ecosystem of 

hardware and software 
vendors

Availability of accelerators varies depending on SKU. Visit the 5th Gen Intel Product Information page for 
additional product details.

See Intel® Xeon® Processors Notices and Disclaimers in next page.

Notes:

1. Average performance gain as measured by the geomean of SPEC CPU rate, STREAM Triad, and LINPACK 

compared to 4th Gen Intel® Xeon® processor. See G1 at intel.com/processorclaims: 5th Gen Intel Xeon 
Scalable processors. Results may vary.

46

Cisco UCS X210c M7 Compute Node

5TH GEN INTEL XEON BENEFIT PILLARS

2. As measured by performance per watt on a range of AI, database, networking, and HPC workloads compared to 
4th Gen Intel® Xeon® processor. See A2, A19-A25, D1, D2, D5, H1, N16 at intel.com/processorclaims: 5th Gen 
Intel Xeon Scalable processors. Results may vary.

3. See G12 at intel.com/processor claims: 5th Gen Intel Xeon Scalable processors. Results may vary
4. See G11 at intel.com/processorclaims: 5th Gen Intel Xeon Scalable processors. Results may vary.
5. Average performance gain as measured by the geomean of SPEC CPU rate, STREAM Triad, and LINPACK 

compared to 3rd Gen Intel® Xeon® processor. See G3 at intel.com/processorclaims: 5th Gen Intel Xeon 
Scalable processors. Results may vary.

6. Based on Intel internal modelling as of December 2023.
7. Based on performance gains of 1.19x to 2.69x with Intel® Advanced Matrix Extensions (Intel® AMX) for 

inference on GPT-J, LLaMA-2 13B, DLRM, DistilBERT, BERT-Large, and ResNet50v1.5 compared to AMD EYPC 
9654 and 9754. See A201, A202, A208-A211 at intel.com/processorclaims: 5th Gen Intel Xeon Scalable 
processors. Results may vary.

8. Based on performance gains of 4.4x to 14.2x for training (ResNet50v1.5, BERT-Large, SSD-ResNet34, RNN-T, 
MaskRCNN, and DLRM) and 2.9x to14x for inference (ResNet50v1.5, BERT-Large, SSD-ResNet34, RNN-T (BF16 
only), Resnext101 32x16d, MaskRCNN (BF16 only), DistilBERT) compared to 3rd Gen Intel® Xeon® processor. 
See A15-A16 at intel.com/processorclaims: 5th Gen Intel Xeon Scalable processors. Results may vary.

9. Based on performance per watt gains of 1.46x to 10.6x with built-in accelerators on a range of AI, database, 
and networking workloads. See A19-A25, D1, D2, D5, N16 at intel.com/processorclaims: 5th Gen Intel Xeon 
Scalable processors. Results may vary.

10. Based on performance per watt gains of 1.11x to 2.96x with built-in accelerators on a range of AI, database, 
networking, and HPC workloads compared to AMD EYPC 9554, 9654, and 9754. See A208-A211, D201-D204, 
H201, N201 at intel.com/processorclaims: 5th Gen Intel Xeon Scalable processors. Results may vary

Intel® Xeon® Processors Notices and Disclaimers

■ Availability of accelerators varies depending on SKU. Visit the Intel Product Information page for 

additional product details.

■ Performance varies by use, configuration and other factors. 

■ Performance results are based on testing as of dates shown in configurations and may not reflect all 
publicly available updates.  See backup for configuration details.  No product or component can be 
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

Cisco UCS X210c M7 Compute Node

47

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

48

Cisco UCS X210c M7 Compute Node

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

Cisco UCS X210c M7 Compute Node

49

SPARE PARTS

SPARE PARTS 

This section lists the upgrade and service-related parts for the Cisco UCS X210c M7 Compute Node. Some of 
these parts are configured with every compute node or with every Cisco UCS X9508 chassis.

Table 25  Spare Parts  

Product ID (PID)

PID Description

Debug Cable

UCSX-C-DEBUGCBL=

UCSX Compute Node Debug Cable

CPUs

Note: If you are ordering a second CPU, see the CPU Accessories section in this table for additional parts 
you may need to order for the second CPU.

Available 5th Gen. Intel® Xeon® Scalable CPUs

8000 Series Processors

UCSX-CPU-I8592V=

Intel I8592V 2GHz/330W 64C/320MB DDR5 4800MT/s

UCSX-CPU-I8592+=

Intel I8592+ 1.9GHz/350W 64C/320MB DDR5 5600MT/s

UCSX-CPU-I8581V=

Intel I8581V 1.8GHz/270W 60C/300MB DDR5 4800MT/s

UCSX-CPU-I8580=

Intel I8580 2GHz/350W 60C/300MB DDR5 5600MT/s

UCSX-CPU-I8571N=

Intel I8571N 2.4GHz/300W 52C/300MB DDR5 4800MT/s

UCSX-CPU-I8570=

Intel I8570 2GHz/350W 56C/300MB DDR5 5600MT/s

UCSX-CPU-I8568Y+=

Intel I8568Y+ 2.3GHz/350W 48C/300MB DDR5 5600MT/s

UCSX-CPU-I8562Y+=

Intel I8562Y+ 2.9GHz/300W 32C/60MB DDR5 5600MT/s

UCSX-CPU-I8558U=

Intel I8558U 2GHz/300W 48C/260MB DDR5 4800MT/s

UCSX-CPU-I8558P=

Intel I8558P 2.7GHz/350W 48C/260MB DDR5 5600MT/s

UCSX-CPU-I8558=

Intel I8558 2GHz/330W 48C/260MB DDR5 5200MT/s

6000 Series Processors

UCSX-CPU-I6554S=

Intel I6554S 2.2GHz/270W 36C/180MB DDR5 5200MT/s

UCSX-CPU-I6548Y+=

Intel I6548Y+ 2.5GHz/250W 32C/60MB DDR5 5200MT/s

UCSX-CPU-I6548N=

Intel I6548N 2.8GHz/250W 32C/60MB DDR5 5200MT/s

UCSX-CPU-I6538Y+=

Intel I6538Y+ 2.3GHz/225W 32C/60MB DDR5 5200MT/s

UCSX-CPU-I6538N=

Intel I6538N 2.2GHz/205W 32C/60MB DDR5 5200MT/s

UCSX-CPU-I6526Y=

Intel I6526Y 2.9GHz/195W 16C/37.5MB DDR5 5200MT/s

50

Cisco UCS X210c M7 Compute Node

SPARE PARTS

Table 25  Spare Parts  (continued)

Product ID (PID)

PID Description

5000 Series Processors

UCSX-CPU-I5515+=

Intel I5515+ 3.2GHz/165W 8C/22.5MB DDR5 4800MT/s

UCSX-CPU-I5512U=

Intel I5512U 2.2GHz/185W 28C/52.5MB DDR5 4800MT/s

4000 Series Processors

UCSX-CPU-I4516Y+=

Intel I4516Y+ 2.2GHz/185W 24C/45MB DDR5 4400MT/s

UCSX-CPU-I4514Y=

Intel I4514Y 2GHz/150W 16C/30MB DDR5 4400MT/s

UCSX-CPU-I4510T=

Intel I4510T 1.9GHz/115W 12C/30MB DDR5 4400MT/s

UCSX-CPU-I4510=

Intel I4510 2.4GHz/150W 12C/30MB DDR5 4400MT/s

UCSX-CPU-I4509Y=

Intel I4509Y 2.6GHz/125W 8C/22.5MB DDR5 4400MT/s

3000 Series Processors

UCSX-CPU-I3508U

Intel I3508U 2GHz/125W 8C/22.5MB DDR5 4400MT/s

Available 4th Gen. Intel® Xeon® Scalable CPUs

8000 Series Processors

UCSX-CPU-I8444H=

Intel I8444H 2.9GHz/270W 16C/45MB DDR5 4800MT/s

UCSX-CPU-I8450H=

Intel I8450H 2GHz/250W 28C/75MB DDR5 4800MT/s

UCSX-CPU-I8452Y=

Intel I8452Y 2GHz/300W 36C/67.5MB DDR5 4800MT/s

UCSX-CPU-I8454H=

Intel I8454H 2.1GHz/270W 32C/82.5MB DDR5 4800MT/s

UCSX-CPU-I8458P=

Intel I8458P 2.7GHz/350W 44C/82.5MB DDR5 4800MT/s

UCSX-CPU-I8460H=

Intel I8460H 2.2GHz/330W 40C/105MB DDR5 4800MT/s

UCSX-CPU-I8460Y+=

Intel I8460Y+ 2GHz/300W 40C/105MB DDR5 4800MT/s

UCSX-CPU-I8461V=

Intel I8461V 2.2GHz/300W 48C/97.5MB DDR5 4800MT/s

UCSX-CPU-I8468=

Intel I8468 2.1GHz/350W 48C/105MB DDR5 4800MT/s

UCSX-CPU-I8468H=

Intel I8468H 2.1GHz/330W 48C/105MB DDR5 4800MT/s

UCSX-CPU-I8468V=

Intel I8468V 2.4GHz/330W 48C/97.5MB DDR5 4800MT/s

UCSX-CPU-I8470=

Intel I8470 2GHz/350W 52C/105MB DDR5 4800MT/s

UCSX-CPU-I8470N=

Intel I8470N 1.7GHz/300W 52C/97.5MB DDR5 4800MT/s

UCSX-CPU-I8471N=

Intel I8471N 1.8GHz/300W 52C/97.5MB DDR5 4800MT/s

UCSX-CPU-I8480+=

Intel I8480+ 2GHz/350W 56C/105MB DDR5 4800MT/s

UCSX-CPU-I8490H=

Intel I8490H 1.9GHz/350W 60C/112.5MB DDR5 4800MT/s

Cisco UCS X210c M7 Compute Node

51

SPARE PARTS

Table 25  Spare Parts  (continued)

Product ID (PID)

PID Description

UCSX-CPU-I8462Y+=

Intel I8462Y+ 2.8GHz/300W 32C/60MB DDR5 4800MT/s

6000 Series Processors

UCSX-CPU-I6414U=

Intel I6414U 2GHz/250W 32C/60MB DDR5 4800MT/s

UCSX-CPU-I6430=

Intel I6430 1.9GHz/270W 32C/60MB DDR5 4400MT/s

UCSX-CPU-I6454S=

Intel I6454S 2.2GHz/270W 32C/60MB DDR5 4800MT/s

UCSX-CPU-I6416H=

Intel I6416H 2.2GHz/165W 18C/45MB DDR5 4800MT/s

UCSX-CPU-I6418H=

Intel I6418H 2.1GHz/185W 24C/60MB DDR5 4800MT/s

UCSX-CPU-I6421N=

Intel I6421N 1.8GHz/185W 32C/60MB DDR5 4400MT/s

UCSX-CPU-I6426Y=

Intel I6426Y 2.5GHz/185W 16C/37.5MB DDR5 4800MT/s

UCSX-CPU-I6428N=

Intel I6428N 1.8GHz/185W 32C/60MB DDR5 4000MT/s

UCSX-CPU-I6434=

Intel I6434 3.7GHz/195W 8C/22.5MB DDR5 4800MT/s

UCSX-CPU-I6434H=

Intel I6434H 3.7GHz/195W 8C/22.5MB DDR5 4800MT/s

UCSX-CPU-I6438M=

Intel I6438M 2.2GHz/205W 32C/60MB DDR5 4800MT/s

UCSX-CPU-I6438N=

Intel I6438N 2GHz/205W 32C/60MB DDR5 4800MT/s

UCSX-CPU-I6438Y+=

Intel I6438Y+ 2GHz/205W 32C/60MB DDR5 4800MT/s

UCSX-CPU-I6442Y=

Intel I6442Y 2.6GHz/225W 24C/60MB DDR5 4800MT/s

UCSX-CPU-I6444Y=

Intel I6444Y 3.6GHz/270W 16C/45MB DDR5 4800MT/s

UCSX-CPU-I6448H=

Intel I6448H 2.4GHz/250W 32C/60MB DDR5 4800MT/s

UCSX-CPU-I6448Y=

Intel I6448Y 2.1GHz/225W 32C/60MB DDR5 4800MT/s

5000 Series Processors

UCSX-CPU-I5411N=

Intel I5411N 1.9GHz/165W 24C/45MB DDR5 4400MT/s

UCSX-CPU-I5412U=

Intel I5412U 2.1GHz/185W 24C/45MB DDR5 4400MT/s

UCSX-CPU-I5415+=

Intel I5415+ 2.9GHz/150W 8C/22.5MB DDR5 4400MT/s

UCSX-CPU-I5416S=

Intel I5416S 2GHz/150W 16C/30MB DDR5 4400MT/s

UCSX-CPU-I5418N=

Intel I5418N 1.8GHz/165W 24C/45MB DDR5 4000MT/s

UCSX-CPU-I5418Y=

Intel I5418Y 2GHz/185W 24C/45MB DDR5 4400MT/s

UCSX-CPU-I5420+=

Intel I5420+ 2GHz/205W 28C/52.5MB DDR5 4400MT/s

4000 Series Processors

UCSX-CPU-I4410T=

Intel I4410T 2.7GHz/150W 10C/26.25MB DDR5 4000MT/s

52

Cisco UCS X210c M7 Compute Node

SPARE PARTS

Table 25  Spare Parts  (continued)

Product ID (PID)

PID Description

UCSX-CPU-I4410Y=

Intel I4410Y 2GHz/150W 12C/30MB DDR5 4000MT/s

UCSX-CPU-I4416+=

Intel I4416+ 2GHz/165W 20C/37.5MB DDR5 4000MT/s

3000 Series Processors

UCSX-CPU-I3408U=

CPU Accessories

Intel I3408U 1.8GHz/125W 8C/22.5MB DDR5 4000MT/s

UCSX-C-M7-HS-F=

UCS X210c M7 Compute Node Front CPU Heat Sink

UCSX-C-M7-HS-R=

UCS X210c M7 Compute Node Rear CPU Heat Sink

UCSX-CPU-TIM=

Single CPU thermal interface material syringe for M7 server HS seal

UCSX-HSCK=

UCSX-CPUAT=

UCS Processor Heat Sink Cleaning Kit (when replacing a CPU)

CPU Assembly Tool for M7 Servers

UCSX-CPUATI-4=

CPX-4 CPU Assembly tool for M7 Servers

UCSX-CPUATI-3=

ICX CPU Assembly Tool for M7 Servers

Memory

DDR5-5600MT/s PID list1

UCSX-MRX16G1RE3=

16GB DDR5-5600 RDIMM 1Rx8 (16Gb)

UCSX-MRX32G1RE3=

32GB DDR5-5600 RDIMM 1Rx4 (16Gb)

UCSX-MRX48G1RF3=

48GB DDR5-5600 RDIMM 1Rx4 (24Gb)

UCSX-MRX96G2RF3=

96GB DDR5-5600 RDIMM 2Rx4 (24Gb)

UCSX-MR128G2RG3=

128GB DDR5-5600 RDIMM 2Rx4 (32Gb)

DIMM Blank

UCSX-DIMM-BLK=

Cisco UCS DIMM Blank

Rear mLOM Adapters

UCSX-MLV5D200GV2D=

Cisco UCS VIC 15230 modular LOM w/Secure Boot X Compute Node

UCSX-ML-V5Q50G-D=

UCS VIC 15420 4x25G secure boot mLOM for X Compute Node

Rear Mezzanine Adapters

Cisco VIC Card

UCSX-V4-PCIME-D=

UCS PCI Mezz Card for X-Fabric

UCSX-ME-V5Q50G-D=

UCS VIC 15422 4x25G secure boot mezz for X Compute Node

Cisco VIC Bridge Card

Cisco UCS X210c M7 Compute Node

53

SPARE PARTS

Table 25  Spare Parts  (continued)

Product ID (PID)

PID Description

UCSX-V5-BRIDGE-D=

UCS VIC 15000 bridge to connect mLOM and mezz X Compute Node 

(This bridge to connect the Cisco VIC 15420 mLOM and Cisco VIC 15422 
Mezz for the X210c M7 Compute Node)

Front Mezzanine Adapters

UCSX-X10C-PT4F-D=

UCSX-X10C-RAIDF-D=

Cisco UCS X210c M7 Compute Node compute pass through controller for 
up to 6 NVMe drives

Cisco UCS X210c M7 Compute Node RAID controller w/4GB Cache, with 
LSI 3900 for up to 6 SAS/SATA/NVMe drives (SAS/SATA and NVMe drives 
can be mixed)

UCSX-X10C-GPUFM-D=

UCS X10c Compute Node GPU Front Mezz

UCSX-MRAID-SC=

Supercap for Cisco 12G SAS Modular Raid controller on Blades

GPUs

UCSX-GPU-T4MEZZ-D=

NVIDIA T4 GPU PCIE 75W 16GB, MEZZ form factor

UCSX-GPU-FLX140MZ=

Intel GPU Flex 140, Gen4x8, HHHL, 75W PCIe

Drives

SAS/SATA SSDs

Self-Encrypted Drives (SED)

UCSXSD960GBKNK9-D=

960GB 2.5" Enterprise value 12G SAS SSD (1X endurance, FIPS)

UCSXSD800GBKNK9-D=

800GB Enterprise performance SAS SSD (3X DWPD, SED)

UCSX-SD16TBKANK9D=

1.6TB 2.5in Enter Perf 24G SAS Kioxia PM7 SSD (3X SED-FIPS)

UCSX-SD38TBKANK9D=

3.8TB 2.5in Enter Value 24G SAS Kioxia PM7 SSD (SED-FIPS)

UCSX-SD76TBKANK9D=

7.6TB 2.5in Enter Value 24G SAS Kioxia PM7 SSD (SED-FIPS)

UCSX-SD960GM2NK9D

960GB 2.5in Enter Value 6G SATA Micron G2 SSD (SED)

UCSX-SD19TEM2NK9D=

1.9TB 2.5in Enter Value 6G SATA Micron G2 SSD (SED)

UCSX-SD38TEM2NK9D=

3.8TB 2.5in Enter Value 6G SATA Micron G2 SSD (SED)

UCSX-SD76TEM2NK9D=

7.6TB 2.5in Enter Value 6G SATA Micron G2 SSD (SED)

Enterprise Performance SSDs (high endurance, supports up to 3X DWPD (drive writes per day))

UCSX-SD16TKA3XEPD=

1.6TB 2.5in Enter Perf 24G SAS Kioxia PM7 SSD (3X)

UCSXSD32TKA3XEP-D=

3.2TB 2.5in Enter Perf 24G SAS Kioxia PM7 SSD (3X)

UCSX-SD19T63XEP-D=

1.9TB 2.5 inch Enterprise performance 6G SATA SSD (3X endurance)

UCSXSD480G63XEP-D=

480GB 2.5in Enterprise performance 6G SATA SSD (3X endurance)

54

Cisco UCS X210c M7 Compute Node

SPARE PARTS

Table 25  Spare Parts  (continued)

Product ID (PID)

PID Description

UCSXSD480GBM3XEPD=

480GB 2.5in Enter Perf 6G SATA Micron G2 SSD (3X)

UCSXSD960GBM3XEPD=

960GB 2.5in Enter Perf 6G SATA Micron G2 SSD (3X)

UCSX-SD19TBM3XEPD=

1.9TB 2.5in Enter Perf 6G SATA Micron G2 SSD (3X)

UCSX-SDB960OA1P=

960GB 2.5in 15mm Solidigm S4620 Enter Perf 6G SATA 3X SSD

UCSX-SDB3T8OA1P=

3.8TB 2.5in 15mm Solidigm S4620 Enter Perf 6G SATA 3X SSD

Enterprise Value SSDs (Low endurance, supports up to 1X DWPD (drive writes per day)) 

UCSXSD240GBM1XEVD=

240GB 2.5in Enter Value 6G SATA Micron G2 SSD

UCSXSD480GBM1XEVD=

480 GB 2.5in Enter Value 6G SATA Micron G2 SSD

UCSXSD960GBM1XEVD=

960GB 2.5in Enter Value 6G SATA Micron G2 SSD

UCSX-SD16TBM1XEVD=

1.6TB 2.5in Enter Value 6G SATA Micron G2 SSD

UCSX-SD19TBM1XEVD=

1.9TB 2.5in Enter Value 6G SATA Micron G2 SSD

UCSX-SD38TBM1XEVD=

3.8TB 2.5in Enter Value 6G SATA Micron G2 SSD

UCSX-SD76TBM1XEVD=

7.6TB 2.5in Enter Value 6G SATA Micron G2 SSD

UCSX-SDB960SA1VD=

960GB 2.5in 6G SATA Enter Value 1X Samsung G1PM893A SSD

UCSX-SDB1T9SA1VD=

1.9TB 2.5in 6G SATA Enter Value 1X Samsung G1PM893A SSD

UCSX-SDB3T8SA1VD=

3.8TB 2.5in 6G SATA Enter Value 1X Samsung G1PM893A SSD

UCSX-SDB7T6SA1VD=

7.6TB 2.5in 6G SATA Enter Value 1X Samsung G1PM893A SSD

UCSX-SD19TKA1XEVD=

1.9TB 2.5in Enter Value 24G SAS Kioxia PM7 SSD

UCSXSD38TKA1XEV-D=

3.8TB 2.5in Enter Value 24G SAS Kioxia PM7 SSD

UCSX-SD76TKA1XEVD=

7.6TB 2.5in Enter Value 24G SAS Kioxia PM7 SSD

UCSX-SD15TKA1XEVD=

15.3TB 2.5in Enter Value 24G SAS Kioxia PM7 SSD

NVMe

UCSX-NVMEG4M1536D=

15.3TB 2.5in U.3 Micron 7450 NVMe High Perf Medium Endurance

UCSX-NVMEG4M1600D=

1.6TB 2.5in U.3 Micron 7450 NVMe High Perf High Endurance

UCSX-NVMEG4M6400D=

6.4TB 2.5in U.3 Micron 7450 NVMe High Perf High Endurance

UCSX-NVMEG4M7680D=

7.6TB 2.5in U.3 Micron 7450 NVMe High Perf Medium Endurance

UCSX-NVB3T8M2V9=

3.8TB 2.5in U.3 15mm Micron 7500 HgPerf MedEnd 1X NVMe FIPS

UCSX-NVB1T9M2V9=

1.9TB 2.5in U.3 15mm Micron 7500 HgPerf MedEnd 1X NVMe FIPS

UCSX-NVB7T6M2V9=

7.6TB 2.5in U.3 15mm Micron 7500 HgPerf MedEnd 1X NVMe FIPS

Cisco UCS X210c M7 Compute Node

55

SPARE PARTS

Table 25  Spare Parts  (continued)

Product ID (PID)

PID Description

UCSX-NVB15T3M2V9=

15.3TB 2.5in U.3 15mm Micron 7500 HgPerf MedEnd 1X NVMe FIPS

UCSX-NVB960M2V=

960GB 2.5in U.3 15mm Micron 7500 Hg Perf Med End 1X NVMe

UCSX-NVB1T9M2V=

1.9TB 2.5in U.3 15mm Micron 7500 Hg Perf Med End 1X NVMe

UCSX-NVB3T2M2P=

3.2TB 2.5in U.3 15mm Micron 7500 Hg Perf Hg End 3X NVMe

UCSX-NVB3T8M2V=

3.8TB 2.5in U.3 15mm Micron 7500 Hg Perf Med End 1X NVMe

SATA M.2 Storage Modules

UCSX-M2-240G-D=

240GB 2.5in M.2 SATA Micron G2 SSD

UCSX-M2-480G-D=

480GB 2.5in M.2 SATA Micron G2 SSD

UCSX-M2-960G-D=

960GB 2.5in M.2 SATA Micron G2 SSD

UCSX-M2-I240GB-D=

240GB SATA M.2 SSD

Boot-Optimized RAID Controller

UCSX-M2-HWRD-FPS=

UCSX Front panel with M.2 RAID controller for SATA drives

NVMe M.2 Storage Modules

UCSX-NVM2-400GB=

400GB M.2 Boot NVMe 

UCSX-NVM2-960GB=

960GB M.2 Boot NVMe

NVMe Boot

UCSX-M2-PT-FPN=

UCSX Front Panel w/M.2 Pass Through Controller for NVME Drv

Drive Blank

UCSC-BBLKD-S2=

Cisco UCS X210c M6 Compute Node 7mm Front Drive Blank

TPM

UCSX-TPM-002C-D=

TPM 2.0, TCG, FIPS140-2, CC EAL4+ Certified, for servers

UCSX-TPM-002D-D=

TPM 2.0 TCG FIPS140-2 CC+ Cert M7 Intel MSW2022 Compliant

UCSX-TPM-OPT-OUT=

OPT OUT, TPM 2.0, TCG, FIPS140-2, CC EAL4+ Certified

Operating System

Microsoft Windows Server

MSWS-22-ST16CD=

Windows Server 2022 Standard (16 Cores/2 VMs)

MSWS-22-ST16CD-NS=

Windows Server 2022 Standard (16 Cores/2 VMs) - No Cisco SVC

MSWS-22-DC16CD=

Windows Server 2022 Data Center (16 Cores/Unlimited VMs)

MSWS-22-DC16CD-NS=

Windows Server 2022 DC (16 Cores/Unlim VMs) - No Cisco SVC

56

Cisco UCS X210c M7 Compute Node

SPARE PARTS

Table 25  Spare Parts  (continued)

Product ID (PID)

PID Description

MSWS-19-ST16CD=

Windows Server 2019 Standard (16 Cores/2 VMs)

MSWS-19-ST16CD-NS=

Windows Server 2019 Standard (16 Cores/2 VMs) - No Cisco SVC

MSWS-19-DC16CD=

Windows Server 2019 Data Center (16 Cores/Unlimited VMs)

MSWS-19-DC16CD-NS=

Windows Server 2019 DC (16 Cores/Unlim VMs) - No Cisco SVC

Red Hat

RHEL-2S2V-D1A=

Red Hat Enterprise Linux (1-2 CPU,1-2 VN); 1-Yr Support Req

RHEL-2S2V-D3A=

Red Hat Enterprise Linux (1-2 CPU,1-2 VN); 3-Yr Support Req

RHEL-2S2V-D5A=

Red Hat Enterprise Linux (1-2 CPU,1-2 VN); 5-Yr Support Req

RHEL-VDC-2SUV-D1A=

RHEL for Virt Datacenters (1-2 CPU, Unlim VN) 1 Yr Supp Req

RHEL-VDC-2SUV-D3A=

RHEL for Virt Datacenters (1-2 CPU, Unlim VN) 3 Yr Supp Req

RHEL-VDC-2SUV-D5A=

RHEL for Virt Datacenters (1-2 CPU, Unlim VN) 5 Yr Supp Req

Red Hat Ent Linux/ High Avail/ Res Strg/ Scal 

RHEL-2S2V-D1S=

Red Hat Enterprise Linux (1-2 CPU,1-2 VN); Prem 1Yr SnS Reqd

RHEL-2S2V-D3S=

Red Hat Enterprise Linux (1-2 CPU,1-2 VN); Prem 3Yr SnS Reqd

RHEL-2S-HA-D1S=

RHEL High Availability (1-2 CPU); Premium 1-yr SnS Reqd

RHEL-2S-HA-D3S=

RHEL High Availability (1-2 CPU); Premium 3-yr SnS Reqd

RHEL-2S-RS-D1S=

RHEL Resilent Storage (1-2 CPU); Premium 1-yr SnS Reqd

RHEL-2S-RS-D3S=

RHEL Resilent Storage (1-2 CPU); Premium 3-yr SnS Reqd

RHEL-VDC-2SUV-D1S=

RHEL for Virt Datacenters (1-2 CPU, Unlim VN) 1 Yr SnS Reqd

RHEL-VDC-2SUV-D3S=

RHEL for Virt Datacenters (1-2 CPU, Unlim VN) 3 Yr SnS Reqd

Red Hat SAP

RHEL-SAP-2S2V-D1S=

RHEL for SAP Apps (1-2 CPU, 1-2 VN); Prem 1-Yr SnS Reqd

RHEL-SAP-2S2V-D3S=

RHEL for SAP Apps (1-2 CPU, 1-2 VN); Prem 3-Yr SnS Reqd

RHEL-SAPSP-D3S=

RHEL SAP Solutions Premium - 3 Years

RHEL-SAPSS-D3S=

RHEL SAP Solutions Standard - 3 Years

SUSE

SLES-2S2V-D1A  =

SUSE Linux Enterprise Svr (1-2 CPU,1-2 VM); 1-Yr Support Req

SLES-2S2V-D3A  =

SUSE Linux Enterprise Svr (1-2 CPU,1-2 VM); 3-Yr Support Req

SLES-2S2V-D5A=

SUSE Linux Enterprise Svr (1-2 CPU,1-2 VM); 5-Yr Support Req

Cisco UCS X210c M7 Compute Node

57

SPARE PARTS

Table 25  Spare Parts  (continued)

Product ID (PID)

PID Description

SLES-2SUVM-D1A=

SUSE Linux Enterprise Svr (1-2 CPU,Unl VM) LP; 1Y Supp Req

SLES-2SUVM-D3A=

SUSE Linux Enterprise Svr (1-2 CPU,Unl VM) LP; 3Y Supp Req

SLES-2SUVM-D5A=

SUSE Linux Enterprise Svr (1-2 CPU,Unl VM) LP; 5Y Supp Req

SLES-2S-LP-D1A=

SUSE Linux Live Patching Add-on (1-2 CPU); 1yr Support Req

SLES-2S-LP-D3A=

SUSE Linux Live Patching Add-on (1-2 CPU); 3yr Support Req

SLES-2S2V-D1S= 

SUSE Linux Enterprise Svr (1-2 CPU,1-2 VM); Prio 1-Yr SnS

SLES-2S2V-D3S=

SLES-2S2V-D5S=

SUSE Linux Enterprise Svr (1-2 CPU,1-2 VM); Prio 3-Yr SnS

SUSE Linux Enterprise Svr (1-2 CPU,1-2 VM); Prio 5-Yr SnS

SLES-2SUVM-D1S=

SUSE Linux Enterprise Svr (1-2 CPU,Unl VM) LP; Prio 1Y SnS

SLES-2SUVM-D3S=

SUSE Linux Enterprise Svr (1-2 CPU,Unl VM) LP; Prio 3Y SnS

SLES-2SUVM-D5S=

SUSE Linux Enterprise Svr (1-2 CPU,Unl VM) LP; Prio 5Y SnS

SLES-2S-HA-D1S=

SUSE Linux High Availability Ext (1-2 CPU); 1yr SnS

SLES-2S-HA-D3S=

SUSE Linux High Availability Ext (1-2 CPU); 3yr SnS

SLES-2S-HA-D5S=

SUSE Linux High Availability Ext (1-2 CPU); 5yr SnS

SLES-2S-GC-D1S=

SUSE Linux GEO Clustering for HA (1-2 CPU); 1yr Sns

SLES-2S-GC-D3S=

SUSE Linux GEO Clustering for HA (1-2 CPU); 3yr SnS

SLES-2S-GC-D5S= 

SUSE Linux GEO Clustering for HA (1-2 CPU); 5yr SnS

SLES-2S-LP-D1S=

SUSE Linux Live Patching Add-on (1-2 CPU); 1yr SnS Required

SLES-2S-LP-D3S=

SUSE Linux Live Patching Add-on (1-2 CPU); 3yr SnS Required

SLES and SAP

SLES-SAP-2S2V-D1S=

SLES for SAP Apps (1-2 CPU, 1-2 VM); Priority 1-Yr SnS

SLES-SAP-2S2V-D3S= 

SLES for SAP Apps (1-2 CPU, 1-2 VM); Priority 3-Yr SnS

SLES-SAP-2S2V-D5S= 

SLES for SAP Apps (1-2 CPU, 1-2 VM); Priority 5-Yr SnS

SLES-SAP-2S2V-D1A=

SLES for SAP Apps w/ HA (1-2 CPU, 1-2 VM); 1-Yr Support Reqd

SLES-SAP-2S2V-D3A=

SLES for SAP Apps w/ HA (1-2 CPU, 1-2 VM); 3-Yr Support Reqd

SLES-SAP-2S2V-D5A=

SLES for SAP Apps w/ HA (1-2 CPU, 1-2 VM); 5-Yr Support Reqd

Notes:

1. DDR5-5600 supported on Intel® Xeon® 5th generation only.

58

Cisco UCS X210c M7 Compute Node

TECHNICAL SPECIFICATIONS

TECHNICAL SPECIFICATIONS

Dimensions and Weight

Table 26  Cisco UCS X210c M7 Compute Node Dimensions and Weight  

Parameter

Value

Height

1.80 in. (45.7 mm)

Width

Depth

11.28 in. (286.5 mm)

23.7 in. (602 mm)

Weight 

■ Minimally configured node weight = 12.84 lbs. (5.83 kg)

■ Fully configured compute node weight = 25.1 lbs. (11.39 kg)

Environmental Specifications

Table 27  Cisco UCS X210c M7 Compute Node Environmental Specifications  

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

NOTE:  The ambient temperature must be less than 35 oC (95 oF).

Cisco UCS X210c M7 Compute Node

59

DISCONTINUED EOL PRODUCTS

DISCONTINUED EOL PRODUCTS

Below is the list of parts were previously available for this product and are no longer sold. Please refer to 
the EOL Bulletin Links via table below to determine if still supported.

Table 28

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

240GB 2.5in Enter Value 6G SATA 
Micron G1 SSD

UCSXSD480GM1XEV-D

480 GB 2.5in Enter Value 6G SATA 
Micron G1 SSD

UCSX-SD16TM1XEV-D

1.6TB 2.5in Enter Value 6G SATA 
Micron G1 SSD

UCSX-SD38TM1XEV-D

3.8TB 2.5in Enter Value 6G SATA 
Micron G1 SSD

UCSX-NVME-W6400-D

6.4TB 2.5in U.2 WD SN840 NVMe 
Extreme Perf. High Endurance  

UCSX-SD32TK3XEP-D

3.2TB 2.5in Enter Perf 12G SAS 
Kioxia G1 SSD (3X)

UCSX-SD38TK1XEV-D

3.8TB 2.5in Enter Value 12G SAS 
Kioxia G1 SSD

UCSX-SD76TBKNK9-D

7.6TB 2.5in Enter Value 12G SAS 
Kioxia G1 SSD (SED-FIPS)

UCSX-SD76TK1XEV-D

7.6TB 2.5in Enter Value 12G SAS 
Kioxia G1 SSD

UCSXNVMEI4I6400-D

6.4TB 2.5in U.2 Intel P5600 NVMe 
High Perf High Endurance

UCSX-SD15TK1XEV-D

15.3TB 2.5in Enter Value 12G SAS 
Kioxia G1 SSD

https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/unified-computing-accessories-eol.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/unified-computing-accessories-eol.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/unified-computing-accessories-eol.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/unified-computing-accessories-eol.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/unified-computing-accessories-eol.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/unified-computing-accessories-eol.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/unified-computing-accessories-eol.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/unified-computing-accessories-eol.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-b-series-blade-s
ervers/select-ucs-accessories-eol.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-b-series-blade-s
ervers/select-ucs-accessories-eol.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-b-series-blade-s
ervers/select-ucs-accessories-eol.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-b-series-blade-s
ervers/select-ucs-accessories-eol.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-b-series-blade-s
ervers/select-ucs-accessories-eol.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-b-series-blade-s
ervers/select-ucs-accessories-eol.html

60

Cisco UCS X210c M7 Compute Node

Table 28

  EOS

UCSX-SD16TBKNK9-D

1.6TB 2.5in Enter Perf 12G SAS 
Kioxia G1 SSD (3X SED-FIPS)

UCSX-SD16TK3XEP-D

1.6TB 2.5in Enter Perf 12G SAS 
Kioxia G1 SSD (3X)

UCSX-SD19TK1XEV-D

1.9TB 2.5in Enter Value 12G SAS 
Kioxia G1 SSD

UCSXNVMEI4I1920-D

1.9TB 2.5in U.2 Intel P5500 NVMe 
High Perf Medium Endurance

UCSX-ML-V5D200G-D

Cisco VIC 15231 2x 100G mLOM 
X-Series

UCSX-SD19TS1XEV-D

1.9TB 2.5v Enter Value 12G SAS 
Seagate SSD

UCSXNVMEXPBI375-D

375GB 2.5in Intel Optane NVMe 
Extreme Performance SSD

UCSXSD960GS1XEV-D

960GB 2.5in Enter Value 12G SAS 
Seagate SSD

UCSX-SD38TS1XEV-D 

3.8TB 2.5in Enter Value 12G SAS 
Seagate SSD

UCS-MR128G4RE3

128GB DDR5-5600 RDIMM 4Rx4 
(16Gb)

UCSXSD19T6S1XEV-D

1.9TB 2.5in Enter Value 6G SATA 
Samsung SSD

UCSXSD76T6S1XEV-D

7.6TB 2.5in Enter Value 6G SATA 
Samsung SSD

UCSXSD960G63XEP-D

960GB 2.5in Enter Perf 6G SATA 
Intel SSD (3X)

UCSX-NVME4-1600-D

1.6TB 2.5in U.2 15mm P5620 Hg 
Perf Hg End NVMe (3X)

UCSX-NVME4-3840-D

3.8TB 2.5in U.2 15mm P5520 Hg 
Perf Med End NVMe

UCSX-NVME4-7680-D

7.6TB 2.5in U.2 15mm P5520 Hg 
Perf Med End NVMe

UCSX-NVME4-1920-D

1.9TB 2.5in U.2 15mm P5520 Hg 
Perf Med End NVMe

DISCONTINUED EOL PRODUCTS

https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-b-series-blade-s
ervers/select-ucs-accessories-eol.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-b-series-blade-s
ervers/select-ucs-accessories-eol.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-b-series-blade-s
ervers/select-ucs-accessories-eol.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-access-eol-15074.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-ucsx-accessories-eol.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-hci-accessories-eol.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-hci-accessories-eol.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-hci-accessories-eol.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-hci-accessories-eol.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-accessories-eol15570.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-hci-accessories-eol.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-hci-accessories-eol.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-accessories-eol15502.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-accessories-eol15502.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-accessories-eol15502.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-accessories-eol15502.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-accessories-eol15502.html

Cisco UCS X210c M7 Compute Node

61

DISCONTINUED EOL PRODUCTS

Table 28

  EOS

UCSX-NVME4-3200-D

3.2TB 2.5in U.2 15mm P5620 Hg 
Perf Hg End NVMe (3X)

UCSX-NVME4-6400-D

6.4TB 2.5in U.2 15mm P5620 Hg 
Perf Hg End NVMe (3X)

UCSX-SD19TM1XEV-D

1.9TB 2.5in Enter Value 6G SATA 
Micron G1 SSD

UCSX-SD38T63XEP-D

3.8TB 2.5in Enter Perf 6G SATA 
Intel SSD (3X)

UCSXSD38T6I1XEV-D

3.8TB 2.5in Enter Value 6G SATA 
Intel SSD

UCSXSD800GK3XEP-D

800GB 2.5in Enter Perf 12G SAS 
Kioxia G1 SSD (3X)

UCSXNVMEI4I1600-D

1.6TB 2.5in U.2 Intel P5600 NVMe 
High Perf High Endurance

UCSX-M2-I480GB-D

480GB M.2 Boot SATA Intel SSD

UCSX-NVME-W3200-D

3.2TB 2.5in U.2 WD SN840 NVMe 
Extreme Perf. High Endurance  

UCSX-NVME4-15360D

15.3TB 2.5in U.2 15mm P5520 Hg 
Perf Med End NVMe

UCSX-NVME4-1920-D

1.9TB 2.5in U.2 15mm P5520 Hg 
Perf Med End NVMe

UCSX-NVME4-3200-D

3.2TB 2.5in U.2 15mm P5620 Hg 
Perf Hg End NVMe (3X)

UCSX-NVME4-6400-D

6.4TB 2.5in U.2 15mm P5620 Hg 
Perf Hg End NVMe (3X)

UCSX-SD19TM1XEV-D

1.9TB 2.5in Enter Value 6G SATA 
Micron G1 SSD

UCSX-SD38T63XEP-D

3.8TB 2.5in Enter Perf 6G SATA 
Intel SSD (3X)

UCSXSD38T6I1XEV-D

3.8TB 2.5in Enter Value 6G SATA 
Intel SSD

UCSX-MR256G8RE3

256GB DDR5-5600 RDIMM 8Rx4 
(16Gb)

https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-accessories-eol15502.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-accessories-eol15502.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-b-series-blade-s
ervers/select-ucs-accessories-eol.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-accessories-eol15502.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-accessories-eol15502.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-accessories-eol15502.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-b-series-blade-s
ervers/select-ucs-accessories-eol.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-accessories-eol15502.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-ac-eol.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-accessories-eol15502.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-accessories-eol15502.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-accessories-eol15502.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-accessories-eol15502.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-b-series-blade-s
ervers/select-ucs-accessories-eol.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-accessories-eol15502.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-accessories-eol15502.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/ucs-accessories_eol.html

62

Cisco UCS X210c M7 Compute Node

Table 28

  EOS

UCSX-NVME-W7680-D

7.6TB 2.5in U.2 WD SN840 NVMe 
Extreme Perf. Value Endurance

UCSX-NVME-W7680-D

7.6TB 2.5in U.2 WD SN840 NVMe 
Extreme Perf. Value Endurance

UCSX-NVMEXPI400-D

400GB 2.5in U.2 15mm P5800X 
Optane Ext Perf NVMe (30/100X)

UCSX-NVMEXPI800-D

800GB 2.5in U.2 15mm P5800X 
Optane Ext Perf NVMe (30/100X)

UCSXS960G6I1XEV-D

960GB 2.5 inch Enterprise Value 
6G SATA Intel SSD

UCSX-SD38TBKNK9-D

3.8TB Enterprise Value SAS SSD 
(1X DWPD, SED)

UCSXSD960GK1XEV-D

960GB 2.5in Enter Value 12G SAS 
Kioxia G1 SSD

UCSX-MRX16G1RE1S

16GB DDR5-4800 RDIMM 1Rx8 
(16Gb)

UCSX-NVMEG4-M960D

960GB 2.5in U.3 15mm P7450 Hg 
Perf Med End NVMe

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

DISCONTINUED EOL PRODUCTS

https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/ucs-accessories_eol.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/ucs-accessories_eol.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-drives-storage-controllers-eol.ht
ml
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-drives-storage-controllers-eol.ht
ml
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-drives-storage-controllers-eol.ht
ml
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-drives-storage-controllers-eol.ht
ml
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-drives-storage-controllers-eol.ht
ml
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/ucs-accessories_eol.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-ucsx-hci-accessories-eol15818.ht
ml
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-ucsx-hci-accessories-eol15818.ht
ml
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-ucsx-hci-accessories-eol15818.ht
ml
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-ucsx-hci-accessories-eol15818.ht
ml
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/ucs-accessories_eol.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/ucs-accessories_eol.html

Cisco UCS X210c M7 Compute Node

63

DISCONTINUED EOL PRODUCTS

Table 28

  EOS

UCSX-MRX64G2RE1

64GB DDR5-4800 RDIMM 2Rx4 
(16Gb)

UCSX-MR128G4RE1

128GB DDR5-4800 RDIMM 4Rx4 
(16Gb)

UCSXS480G6I1XEV-D

480 GB 2.5 inch Enterprise Value 
6G SATA Intel SSD

https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/ucs-accessories_eol.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/ucs-accessories_eol.html
https://www.cisco.com/c/en/us/products/collate
ral/servers-unified-computing/ucs-c-series-rack-se
rvers/select-ucs-accessories-eol15502.html

64

Cisco UCS X210c M7 Compute Node

