# Cisco UCS X215c M8 Compute Node Spec Sheet

| | |
|---|---|
| **URL Title** | Cisco UCS X215c M8 Compute Node Spec Sheet |
| **URL** | https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-x-series-modular-system/ucs-x215c-m8-compute-node.pdf |
| **Long URL** |  |
| **HTML Title** |  |
| **Source file** | `ucs-docs-raw/pdf/ucs-x215c-m8-compute-node.pdf` |
| **File type** | PDF |
| **Fetched on** | 2026-04-16 10:51:16 |

---

Spec Sheet

Cisco UCS X215c M8 
Compute Node

A printed version of this document is only a copy 
and not necessarily the latest version. Refer to 
the following link for the latest released version:

https://www.cisco.com/c/en/us/products/servers-unified-
computing/ucs-x-series-modular-system/datasheet-
listing.html

CISCO SYSTEMS
170 WEST TASMAN D 
SAN JOSE, CA, 95134
WWW.CISCO.COM

PUBLICATION HISTORY 

V.20

MARCH 02, 2026

 
CONTENTS

STEP
STEP
STEP

OVERVIEW  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
DETAILED VIEWS  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
Cisco UCS X215c M8 Compute Node Front View   . . . . . . . . . . . . . . . . . . . . . . . . . . . .4
COMPUTE NODE STANDARD CAPABILITIES and FEATURES   . . . . . . . . . . . . . . . 6
CONFIGURING the Cisco UCS X215c M8 Compute Node  . . . . . . . . . . . . . . . . . 9
1 CHOOSE BASE CISCO UCS X215c M8 COMPUTE NODE SKU   . . . . . . . . . . . . . . . . . . 10
2 CHOOSE CPU(S)   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3 CHOOSE MEMORY   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
Memory configurations and mixing rules  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
4 CHOOSE REAR mLOM ADAPTER   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
5 CHOOSE OPTIONAL REAR MEZZANINE VIC/BRIDGE ADAPTERS  . . . . . . . . . . . . . . . . 22
6 CHOOSE OPTIONAL FRONT MEZZANINE ADAPTER . . . . . . . . . . . . . . . . . . . . . . . . 24
7 CHOOSE OPTIONAL GPU PCIe NODE   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
8 CHOOSE OPTIONAL GPUs   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
9 CHOOSE OPTIONAL DRIVES  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
10 Order Boot-optimized M.2 Front Panel Module and Drives . . . . . . . . . . . . . . . . . 31
11 ORDER NVMe BOOT (OPTIONAL)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
12 CHOOSE OPTIONAL TRUSTED PLATFORM MODULE   . . . . . . . . . . . . . . . . . . . . . . 33
13 CHOOSE OPERATING SYSTEM AND VALUE-ADDED SOFTWARE   . . . . . . . . . . . . . . . 34
14 CHOOSE OPTIONAL OPERATING SYSTEM MEDIA KIT . . . . . . . . . . . . . . . . . . . . . . 37
SUPPLEMENTAL MATERIAL  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  38
Simplified Block Diagram  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
SPARE PARTS  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  42
UPGRADING or REPLACING CPUs and Memory   . . . . . . . . . . . . . . . . . . . . . .  43
TECHNICAL SPECIFICATIONS  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  44
Dimensions and Weight  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
Environmental Specifications  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
DISCONTINUED EOL PRODUCTS  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  45

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

2

Cisco UCS X215c M8 Compute Node

OVERVIEW

OVERVIEW

The Cisco UCS X-Series Modular System simplifies your data center, adapting to the unpredictable needs of 
modern applications while also providing for traditional scale-out and enterprise workloads. It reduces the 
number of server types to maintain, helping to improve operational efficiency and agility as it helps reduce 
complexity. Powered by the Cisco Intersight™ cloud operations platform, it shifts your thinking from 
administrative details to business outcomes with hybrid cloud infrastructure that is assembled from the 
cloud, shaped to your workloads, and continuously optimized.

The Cisco UCS X215c M8 Compute Node is integrated into the Cisco Compute Hyperconverged X-Series 
Modular System. Up to eight Cisco Compute Hyperconverged Nodes can reside in the 7-Rack-Unit (7RU) 
Cisco Compute Hyperconverged 9508 Chassis, offering one of the highest densities of compute, IO, and 
storage per rack unit in the industry.

The Cisco UCS X215c M8 Compute Node harnesses the power of the AMD EPYC™ Series Processors. Refer to 
the COMPUTE NODE STANDARD CAPABILITIES and FEATURES on page 6

NOTE:  All options listed in the Spec Sheet are compatible with Intersight Managed Mode and 
UCSM Managed Mode configurations. To see the most recent list of components that are 
supported in Intersight Managed Mode, see Supported Systems.

Figure 1 on page 4 shows a front view of the Cisco UCS X215c M8 Compute Node.

Figure 1  Cisco UCS X215c M8 Compute Node 

Front View with Drives

Front View with Drives and GPU

Cisco UCS X215c M8 Compute Node

3

DETAILED VIEWS

DETAILED VIEWS

Cisco UCS X215c M8 Compute Node Front View

Figure 2 & Figure 3 is a front view of the Cisco UCS X215c M8 Compute Node.

Figure 2  Cisco UCS X215c M8 Compute Node Front View (Drives option)

Storage Drives Option

5

6

8

15

10

14

16

1

12

13

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

7

9

11

1 
2
3
4
5

6
7
8

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

Notes:

1. An adapter cable (PID UCSX-C-DEBUGCBL) is required to connect the OCuLink port to the transition serial USB 

and video (SUV) octopus cable.

4

Cisco UCS X215c M8 Compute Node

Figure 3  Cisco UCS X215c M8 Compute Node Front View

 (Drives and GPU option)

Storage Drives and GPU Option

DETAILED VIEWS

1 
2
3
4
5

Drive slot 1
GPU slot 1
GPU slot 2
Drive slot 2
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

Cisco UCS X215c M8 Compute Node

5

COMPUTE NODE STANDARD CAPABILITIES and FEATURES

COMPUTE NODE STANDARD CAPABILITIES and FEATURES

Table 1 lists the capabilities and features of the base Cisco UCS X215c M8 Compute Node. Details about how 
to configure the compute node for a listed feature or capability (for example, number of processors, disk 
drives, or amount of memory) are provided in CONFIGURING the Cisco UCS X215c M8 Compute Node on 
page 9.

Table 1   Capabilities and Features 

Capability/Feature

Description

Chassis

CPU

The Cisco UCS X215c M8 Compute Node mounts in a Cisco UCS X9508 chassis.

■ One or two AMD EPYC™ 97x4, 9004 Series, and 9004 Series with 3D V-Cache™ 

Technology Processors or

■ One or two AMD EPYC™ 9005 Series Processors

Memory

24 slots for registered DIMMs (RDIMMs)

Mezzanine Adapters 
(Front)

One front mezzanine connector that supports:
■ EDSFF E3.S NVMe passthrough controller

■ NVMe passthrough controller (for U.2/U.3 NVMe drives only)

■ RAID controller with 4GB cache (for SSD and mix of SSD and NVMe)

■ GPU front mezzanine

■ No front mezzanine

Internal Storage and 
GPU

■ Front mezzanine storage options (hot-swappable): 

• Up to 8x EDSFF E3.S NVMe drives 

• Up to 6x 2.5-inch SAS and SATA RAID-compatible SSDs

• Up to 6x 2.5-inch NVMe PCIe drives

• A mixture of up to six SAS/SATA or NVMe drives 

NOTE:  Drives require a RAID or passthrough controller in the front mezzanine 
module slot.

■ Boot drive options:

• Mini storage module with 2x M.2 (up to 960GB per drive) SATA drives with 

Hardware RAID 

• Mini storage module with 2x M.2 (up to 960GB per drive) NVMe drives in 

pass-through mode (Non-RAID).

■ GPU options: 

• GPU front mezzanine module with 2x 2.5-inch NVMe drives and 2 HHHL x 

GPUs

■ Cisco UCS 15422 mezzanine card with UCS VIC 15000 bridge connector 

compatible with Cisco UCS VIC 15420

■ UCS PCI Mezz Card for X-Fabric

Mezzanine Adapter 
(Rear)

6

Cisco UCS X215c M8 Compute Node

COMPUTE NODE STANDARD CAPABILITIES and FEATURES

Table 1   Capabilities and Features (continued)

Capability/Feature

Description

mLOM

The modular LAN on motherboard (mLOM) cards (the Cisco UCS VIC 15230 and 
15420) is located at the rear of the compute node.

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

Video uses a Matrox G200e video/graphics controller.

■ Integrated 2D graphics core with hardware acceleration
■ DDR4 memory interface supports up to 512 MB of addressable memory (16 

MB is allocated by default to video memory)

■ Supports display resolutions up to 1920 x 1200 32 bpp@ 60Hz
■ Video is available with an Oculink connector on the front panel. An adapter 
cable (PID UCSX-C-DEBUGCBL) is required to connect the OCuLink port to the 
transition serial USB and video (SUV) octopus cable. 

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
UCS X215c M8 Compute Node inventory, health, and system event logs.

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

■ Starting with UCS Manager (UCSM) 4.3(4) or later

Firmware standards

■ UEFI Spec         2.9

■ ACPI                 6.5

■ SMBIOS Ver       3.6

Security

 Includes secure boot silicon root of trust FPGA, ACT2 anti-counterfeit provisions, 
and optional Trusted Platform Model (TPM).

Cisco UCS X215c M8 Compute Node

7

COMPUTE NODE STANDARD CAPABILITIES and FEATURES

Table 1   Capabilities and Features (continued)

Capability/Feature

Description

Fabric Interconnect

Compatible with the Cisco UCS 6454, 64108, 6536 and 6664 fabric interconnects

8

Cisco UCS X215c M8 Compute Node

CONFIGURING the Cisco UCS X215c M8 Compute Node

CONFIGURING the Cisco UCS X215c M8 Compute Node

Follow these steps to configure the Cisco UCS X215c M8 Compute Node:

■ STEP 1 CHOOSE BASE CISCO UCS X215c M8 COMPUTE NODE SKU, page 10

■ STEP 2 CHOOSE CPU(S), page 11

■ STEP 3 CHOOSE MEMORY, page 15

■ STEP 4 CHOOSE REAR mLOM ADAPTER, page 18

■ STEP 5 CHOOSE OPTIONAL REAR MEZZANINE VIC/BRIDGE ADAPTERS, page 22

■ STEP 6 CHOOSE OPTIONAL FRONT MEZZANINE ADAPTER, page 24

■ STEP 7 CHOOSE OPTIONAL GPU PCIe NODE, page 26

■ STEP 8 CHOOSE OPTIONAL GPUs, page 27

■ STEP 9 CHOOSE OPTIONAL DRIVES, page 28

■ STEP 10 Order Boot-optimized M.2 Front Panel Module and Drives, page 31

■ STEP 11 ORDER NVMe BOOT (OPTIONAL), page 32

■ STEP 12 CHOOSE OPTIONAL TRUSTED PLATFORM MODULE, page 33

■ STEP 13 CHOOSE OPERATING SYSTEM AND VALUE-ADDED SOFTWARE, page 34

■ STEP 14 CHOOSE OPTIONAL OPERATING SYSTEM MEDIA KIT, page 37

■  SUPPLEMENTAL MATERIAL, page 38

Cisco UCS X215c M8 Compute Node

9

CONFIGURING the Cisco UCS X215c M8 Compute Node

STEP 1 CHOOSE BASE CISCO UCS X215c M8 COMPUTE NODE SKU

Top Level ordering product ID (PID) of the Cisco UCS X215c M8 Compute Node as shown inTable 2

Table 2   Top level ordering PID

Product ID (PID)

Description

UCSX-M8-MLB

UCSX M8 Modular Server and Chassis MLB

Select the product ID (PID) of the Cisco UCS X215c M8 Compute Node as shown in Table 3.

CAUTION:  This product may not be purchased outside of the approved bundles (must be 
ordered under the MLB)

Table 3   PID of the Base Cisco UCS X215c M8 Compute Node  

Product ID (PID)

Description

UCSX-215C-M8

Cisco UCS X215c M8 Compute Node without CPU, memory, drive bays, drives, VIC 
adapter, or mezzanine adapters (ordered as a UCS X9508 chassis option)

UCSX-215C-M8-U

Cisco UCS X215c M8 Compute Node without CPU, memory, drive bays, drives, VIC 
adapter, or mezzanine adapters (ordered standalone)

A base Cisco UCS X215c M8 Compute Node ordered in Table 3 does not include any components 
or options. They must be selected during product ordering.

Please follow the steps on the following pages to order components such as the following, which 
are required in a functional compute node:

■ CPUs

■ Memory

■ Cisco storage RAID or passthrough controller with drives

■ Drives

■ Cisco adapters

10

Cisco UCS X215c M8 Compute Node

CONFIGURING the Cisco UCS X215c M8 Compute Node

STEP 2 CHOOSE CPU(S)

■ 5th Gen. AMD EPYC™ processors highlights are:

— CPU-to-CPU communication using Infinity Fabric Interconnect

— Cache size of up to 512 MB

— Up to 160 cores

— Power: Up to 400Watts

■ 4th Gen. AMD EPYC™ processors highlights are:

— CPU-to-CPU communication using Infinity Fabric Interconnect

— Cache size of up to 1152 MB

— Up to 128 cores

— Power: Up to 400Watts

Select CPUs

■ The available 5th Gen. AMD EPYC™ processors are listed in Table 4.

■ The available 4th Gen. AMD EPYC™ processors are listed in Table 5.

CAUTION:  For systems configured with processors operating above 28o C  
[82.4o F], a fan fault or executing workloads with extensive use of heavy 
instructions sets may assert thermal and/or performance faults with an associated 
event recorded in the System Event Log (SEL).

Table 4   Available 5th Gen. AMD EPYC™ CPUs

Product ID (PID)1

Maximum 
Socket 

Core

CPU Base 
Frequency

CPU Boost 
Frequency

Default 
TDP

Cache 
Size

Highest DDR5 
DIMM Clock

(S)

(C)

(GHz)

(GHz)

(W)

(MB)

(MT/s)2

5th Gen EPYC 9005 Series Processors

UCSX-CPU-A9845

UCSX-CPU-A9825

UCSX-CPU-A9745

UCSX-CPU-A9655

UCSX-CPU-A9645

UCSX-CPU-A9565

UCSX-CPU-A9555

UCSX-CPU-A9535 

UCSX-CPU-A9455

UCSX-CPU-A9365

UCSX-CPU-A9355

UCSX-CPU-A9335

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

160

144

128

96

96

72

64

64

48

36

32

32

2.10

2.20

2.40

2.60

2.30

3.15

3.20

2.40

3.15

3.40

3.55

3.00

3.70

3.70

3.70

4.50

3.70

4.30

4.40

4.30

4.40

4.30

4.40

4.40

390

390

400

400

320

400

360

300

300

300

280

210

320

384

256

384

256

384

256

256

256

192

256

128

6000

6000

6000

6000

6000

6000

6000

6000

6000

6000

6000

6000

Cisco UCS X215c M8 Compute Node

11

CONFIGURING the Cisco UCS X215c M8 Compute Node

Table 4   Available 5th Gen. AMD EPYC™ CPUs

Maximum 
Socket 

Core

CPU Base 
Frequency

CPU Boost 
Frequency

Default 
TDP

Cache 
Size

Highest DDR5 
DIMM Clock

(S)

(C)

(GHz)

(GHz)

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

1S

1S

1S

24

16

16

8

64

48

32

24

16

96

64

48

32

3.20

3.65

2.60

3.60

3.30

3.65

3.80

4.10

4.20

2.60

3.20

3.15

3.55

4.30

4.30

4.10

4.10

5.00

4.80

4.80

4.80

5.00

4.50

4.40

4.40

4.40

(W)

200

200

125

125

400

400

320

320

320

400

360

300

280

(MB)

128

64

64

64

256

256

256

256

512

384

256

256

256

(MT/s)2

6000

6000

6000

6000

6000

6000

6000

6000

6000

6000

6000

6000

6000

Product ID (PID)1

UCSX-CPU-A9255

UCSX-CPU-A9135

UCSX-CPU-A9115

UCSX-CPU-A9015

UCSX-CPU-A9575F

UCSX-CPU-A9475F

UCSX-CPU-A9375F

UCSX-CPU-A9275F

UCSX-CPU-A9175F

UCSX-CPU-A9655P

UCSX-CPU-A9555P

UCSX-CPU-A9455P

UCSX-CPU-A9355P

Notes:

1. Any CPU PID ending in “P” cannot be used in a 2-CPU system. They can only be used in a 1-CPU 
system.The X215c M8 is IO optimized for 1 CPU configurations.  All storage and network options 
can be used with one CPU. X-Fabric options for connecting to PCIe nodes require a two CPU 
configuration.

2. If higher or lower speed DIMMs are selected than what is shown in Table 9 on page 17 for a given 
CPU speed, the DIMMs will be clocked at the lowest common denominator of CPU clock and DIMM 
clock.

Table 5   Available 4th Gen. AMD EPYC™ CPUs

Product ID (PID)1

Maximum 
Socket 

(S)

4th Gen EPYC 97x4 Processors

UCSX-CPU-A9754

UCSX-CPU-A9734

2S

2S

Core

(C)

128

112

4th Gen EPYC 9004 Series Processor
96
UCSX-CPU-A9654

2S

UCSX-CPU-A9634

UCSX-CPU-A9554

UCSX-CPU-A9534

UCSX-CPU-A9454

UCSX-CPU-A9354

2S

2S

2S

2S

2S

84

64

64

48

32

CPU Base 
Frequency

CPU Boost 
Frequency

Default 
TDP

Cache 
Size

Highest DDR5 
DIMM Clock

(GHz)

(GHz)

(W)

(MB)

(MT/s)2

2.25

2.20

2.40

2.25

3.10

2.45

2.75

3.25

3.10

3.00

3.70

3.70

3.75

3.70

3.80

3.80

360

340

360

290

360

280

290

280

256

256

384

384

256

256

256

256

4800

4800

4800

4800

4800

4800

4800

4800

12

Cisco UCS X215c M8 Compute Node

Table 5   Available 4th Gen. AMD EPYC™ CPUs

CONFIGURING the Cisco UCS X215c M8 Compute Node

CPU Base 
Frequency

CPU Boost 
Frequency

Default 
TDP

Cache 
Size

Highest DDR5 
DIMM Clock

(GHz)

(GHz)

Product ID (PID)1

Maximum 
Socket 

UCSX-CPU-A9334

UCSX-CPU-A9254

UCSX-CPU-A9224

UCSX-CPU-A9124

UCSX-CPU-A9474F

UCSX-CPU-A9374F

UCSX-CPU-A9274F

UCSX-CPU-A9174F

UCSX-CPU-A9654P

UCSX-CPU-A9554P

UCSX-CPU-A9454P

UCSX-CPU-A9354P

(S)

2S

2S

2S

2S

2S

2S

2S

2S

1S

1S

1S

1S

Core

(C)

32

24

24

16

48

32

24

16

96

64

48

32

2.70

2.90

2.50

3.00

3.60

3.85

4.05

4.10

2.40

3.10

2.75

3.25

4th Gen EPYC 9004 Series with 3D V-Cache™ Technology
UCSX-CPU-A9684X

2.55

96

2S

UCSX-CPU-A9384X

UCSX-CPU-A9184X

2S

2S

32

16

3.10

3.55

Notes:

3.90

4.15

3.70

3.70

4.10

4.30

4.30

4.40

3.70

3.75

3.80

3.80

3.70

3.90

4.20

(W)

210

200

200

200

360

320

320

320

360

360

290

280

400

320

320

(MB)

(MT/s)2

128

128

64

64

256

256

256

256

384

256

256

256

1152

768

768

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

1. Any CPU PID ending in “P” cannot be used in a 2-CPU system. They can only be used in a 1-CPU system.The 

X215c M8 is IO optimized for 1 CPU configurations.  All storage and network options can be used with one CPU.  
X-Fabric options for connecting to PCIe nodes require a two CPU configuration.

2. If higher or lower speed DIMMs are selected than what is shown in Table 8 on page 16 for a given CPU 

speed, the DIMMs will be clocked at the lowest common denominator of CPU clock and DIMM clock.

Supported Configurations

(1) Configurations with NVMe PCIe drives:

■ Select one or two identical CPUs from Table 4 on page 11 or Table 5 on page 12

(2) Configurations with GPUs:

■ Select one or two identical CPUs from Table 4 on page 11 or Table 5 on page 12

(3) One-CPU Configuration

■ Choose one CPU from any one of the rows of Table 4 on page 11 or Table 5 on page 12

(4) Two-CPU Configuration

■ Choose two identical CPUs from any one of the rows of Table 4 on page 11 or Table 5 on 

page 12

Cisco UCS X215c M8 Compute Node

13

CONFIGURING the Cisco UCS X215c M8 Compute Node

■ When upgrading a single CPU server to two CPUs a rear heatsink is required in addition to 

the new CPU. See Table 6 on page 14 for heatsink PIDs.

Table 6   CPU Accessories

Product ID (PID)

Description

UCSX-M8A-HS-F=

Front Heatsink for AMD X series servers

UCSX-M8A-HS-R=

Rear Heatsink for AMD X series servers

14

Cisco UCS X215c M8 Compute Node

CONFIGURING the Cisco UCS X215c M8 Compute Node

STEP 3 CHOOSE MEMORY

The Table 7 below describes the main memory DIMM features supported on Cisco UCS X215c M8 
rack server.

Table 7   X215c M8 Main Memory Features

Memory DIMM server technologies

Description

DDR5 memory clock speed

Operational voltage

DRAM fab density

DRAM DIMM type

4th Gen. AMD EPYC™ CPUs: Up to 4800 MT/s 1DPC

5th Gen. AMD EPYC™ CPUs: Up to 6000 MT/s 1DPC

1.1 Volts

16Gb, 24Gb, and 32Gb

RDIMM (Registered DDR5 DIMM)

Memory DIMM organization

Twelve memory DIMM channels per CPU; 1 DIMM per channel only

Maximum number of DRAM DIMM per 
server

DRAM DIMM Densities and Ranks

Maximum system capacity (DRAM 
DIMMs only)

Up to 24 (2-Socket)

16GB 1Rx8, 32GB 1Rx4, 48GB 1Rx4, 64GB 2Rx4, 
96GB 2Rx4, 128GB 4Rx4, 128GB (32Gb) 2Rx4

6TB (24x256GB)

Figure 4

  12-Channel Memory Organization 

Cisco UCS X215c M8 Compute Node

15

CONFIGURING the Cisco UCS X215c M8 Compute Node

Select DIMMs

The supported memory DIMMs are listed in Table 8 and Table 9. 

NOTE:  

■ When paired with 4th Gen. AMD EPYC™ CPUs, all memory DIMMs must be Cisco 
DDR5-5600 memory PIDs, although the memory will operate at the maximum 
speed of the 4th Gen. AMD EPYC™ CPUs memory controller, up to 4800 MT/s.

■ When paired with 5th Gen. AMD EPYC™ CPUs, all memory DIMMs must be Cisco 
DDR5-6400 memory PIDs, although the memory will operate at the maximum 
speed of the 5th Gen. AMD EPYC™ CPUs memory controller, up to 6000 MT/s.

■ If UCSX-580P PCIe Node is selected, the server memory quantity must be at 

least three times the total GPU memory size.

Table 8   Available DDR5 DIMMs for 4th Gen. AMD EPYC™ CPUs

Product ID (PID)

PID Description

Ranks/DIMM

DDR5-5600 MT/s PIDs list1
UCSX-MR128G4RE32
UCSX-MR128G2RG3

128GB DDR5-5600 RDIMM 4Rx4 (16Gb)

128GB DDR5-5600 RDIMM 2Rx4 (32Gb)

UCSX-MRX96G2RF3

96GB DDR5-5600 RDIMM 2Rx4 (24Gb)

UCSX-MRX64G2RE3

64GB DDR5-5600 RDIMM 2Rx4 (16Gb)

UCSX-MRX48G1RF3

48GB DDR5-5600 RDIMM 1Rx4 (24Gb)

UCSX-MRX32G1RE3

32GB DDR5-5600 RDIMM 1Rx4 (16Gb)

UCSX-MRX16G1RE3

16GB DDR5-5600 RDIMM 1Rx8 (16Gb)

DIMM Blank3
UCSX-DIMM-BLK

Notes:

UCS DIMM Blank

4

2

2

2

1

1

1

1. If higher or lower speed DIMMs are selected than for a given CPU speed, the DIMMs will be clocked at the lowest 
common denominator of CPU clock and DIMM clock. check the Table 5 column “Highest DDR5 DIMM Clock 
Support”

2. 128GB 4Rx4 (16Gb) is now End-Of-Life and is replaced by 128GB 2Rx4 (32Gb).
3. Any empty DIMM slot must be populated with a DIMM blank to maintain proper cooling airflow. 

16

Cisco UCS X215c M8 Compute Node

CONFIGURING the Cisco UCS X215c M8 Compute Node

Table 9   Available DDR5 DIMMs for 5th Gen. AMD EPYC™ CPUs

Product ID (PID)

PID Description

Ranks/DIMM

DDR5-6400 MT/s PIDs list1
UCSX-MR256G4RG5

256GB DDR5-6400 RDIMM 4Rx4 (32Gb)

UCSX-MR128G2RG5

128GB DDR5-6400 RDIMM 2Rx4 (32Gb)

UCSX-MRX96G2RF5 

96GB DDR5-6400 RDIMM 2Rx4 (24Gb)

UCSX-MRX64G2RE5

64GB DDR5-6400 RDIMM 2Rx4 (16Gb)

UCSX-MRX48G1RF5 

48GB DDR5-6400 RDIMM 1Rx4 (24Gb)

UCSX-MRX32G1RE5 

32GB DDR5-6400 RDIMM 1Rx4 (16Gb)

UCSX-MRX16G1RE5 

16GB DDR5-6400 RDIMM 1Rx8 (16Gb)

DIMM Blank2
UCSX-DIMM-BLK

Notes:

UCS DIMM Blank

4

2

2

2

1

1

1

1. If higher or lower speed DIMMs are selected than for a given CPU speed, the DIMMs will be clocked at the lowest 
common denominator of CPU clock and DIMM clock. check the Table 4 column “Highest DDR5 DIMM Clock 
Support”

2. Any empty DIMM slot must be populated with a DIMM blank to maintain proper cooling airflow. 

Memory configurations and mixing rules

GOLDEN RULE:  Memory on every CPU socket shall be configured identically. Therefore, the 
memory configuration of CPU-1 will be identical to CPU-2 for a 2-Socket system. Unbalanced 
populations are unsupported.

NOTE:  For full details on supported memory configurations see the M8 Memory 
Guide.

Cisco UCS X215c M8 Compute Node

17

CONFIGURING the Cisco UCS X215c M8 Compute Node

STEP 4 CHOOSE REAR mLOM ADAPTER

The Cisco UCS X215c M8 Compute Node must be ordered with a Cisco VIC mLOM Adapter. The 
adapter is located at the back and can operate in a single-CPU or dual-CPU configuration. 
Table 10 shows the mLOM adapter choices.

Table 10  mLOM Adapters 

Product ID (PID)

Description

Connection Type

UCSX-MLV5D200GV2D

Cisco UCS VIC 15230 modular LOM w/Secure Boot X 
Compute Node

mLOM

■ VIC 15420 are supported with both X9108-IFM-25G and 

X9108-IFM-100G.

■ VIC 15420 will operate at 4x 25G with both 

X9108-IFM-25G and X9108-IFM-100G.

■ Cannot be selected with UCSX-ML-V5Q50G-D or 

UCSX-ME-V5Q50G-D

UCSX-ML-V5Q50G-D

UCS VIC 15420 4x25G secure boot mLOM for X Compute 
Node

mLOM

■ VIC 15230 will operate at 4x 25G with X9108-IFM-25G 

and at 2x 100G with X9108-IFM-100G.

■ Cannot be selected with UCSX-ML-V5D200G-D or 

UCSX-MLV5D200GV2D

NOTE:  

■ There is no backplane in the Cisco UCS X9508 chassis; thus, the compute nodes 

directly connect to the IFMs using Orthogonal Direct connectors.

■ Figure 5 shows the location of the mLOM and rear mezzanine adapters on the 
Cisco UCS X215c M8 Compute Node. The bridge adapter connects the mLOM 
adapter to the rear mezzanine adapter.

18

Cisco UCS X215c M8 Compute Node

Figure 5  Location of mLOM and Rear Mezzanine Adapters

CONFIGURING the Cisco UCS X215c M8 Compute Node

Rear Mezzanine Adapter

Bridge Adapter

mLOM Adapter

Cisco UCS X215c M8 Compute Node

19

CONFIGURING the Cisco UCS X215c M8 Compute Node

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

Cisco UCS X215c Compute Node

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

20

Cisco UCS X215c M8 Compute Node

 
 
 
 
CONFIGURING the Cisco UCS X215c M8 Compute Node

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

Cisco UCS X215c Compute Node

Empty

 Mezzanine Slot

MAC1

Cisco ASIC

MAC0

Bridge Adapter

mLOM Adapter

Cisco UCS X215c M8 Compute Node

21

CONFIGURING the Cisco UCS X215c M8 Compute Node

STEP 5 CHOOSE OPTIONAL REAR MEZZANINE VIC/BRIDGE ADAPTERS

The Cisco UCS X215c M8 Compute Node has one rear mezzanine adapter connector which can 
have a UCS VIC 15422 Mezz card that can be used as a second VIC card on the compute node for 
network connectivity or as a connector to the X440p PCIe node via X-Fabric modules. The same 
mezzanine slot on the compute node can also accommodate a pass-through mezzanine adapter 
for X-Fabric which enables compute node connectivity to the X440p PCIE node. Refer to 
Table 11 for supported adapters.

Table 11  Available Rear Mezzanine Adapters  

Product ID(PID)

PID Description

Cisco VIC Card

UCSX-V4-PCIME-D1

UCS PCIe Mezz Card for X-Fabric

UCSX-V5-PCIME2

UCS PCI Mezz card for X-Fabric Gen5

CPUs 
Required

Connector Type

Two CPUs 
required

Rear Mezzanine 
connector on 
motherboard

Two 5th Gen 
CPUs are 
required

Rear Mezzanine 
connector on 
motherboard

UCSX-ME-V5Q50G-D3

UCS VIC 15422 4x25G secure boot mezz for 
X Compute Node

Two CPUs 
required

Cisco VIC Bridge Card4

UCSX-V5-BRIDGE-D5

UCS VIC 15000 bridge to connect mLOM and 
mezz X Compute Node 

Rear Mezzanine 
connector on 
motherboard

One connector on 
Mezz card and 
one connector on 
mLOM card

Notes:

1. The UCSX-V4-PCIME-D rear mezzanine card for X-Fabric has PCIe Gen4 x16 connectivity towards each 
CPU1 and CPU2. Additionally, the card also provides two PCIe Gen4 x16 to each X-fabric. This rear 
mezzanine card enables connectivity from the X215c M8 Compute Node to the X440p PCIe node.
2. The UCSX-V5-PCIME rear mezzanine card for X-Fabric has PCIe Gen5 x16 connectivity towards each 

CPU1 and CPU2. Additionally, the card also provides two PCIe Gen5 x16 to each X-fabric.

3. UCSX-ME-V5Q50G-D only requires 2 CPUs if being used with a PCIe node.
4. Included with the Cisco VIC 15422 mezzanine adapter.
5. This bridge to connect the Cisco VIC mLOM and Cisco VIC mezzanine adapters for the X215c M8 

Compute Node.

22

Cisco UCS X215c M8 Compute Node

CONFIGURING the Cisco UCS X215c M8 Compute Node

Table 12  Throughput Per UCS X215c M8 Server

X215c M8 Compute 
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

X215c 
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

■ All the connections to Cisco UCS X-Fabric 1 and Cisco UCS X-Fabric 2 are through the Molex 

Orthogonal Direct (OD) connector on the mezzanine card.

Cisco UCS X215c M8 Compute Node

23

 
CONFIGURING the Cisco UCS X215c M8 Compute Node

STEP 6 CHOOSE OPTIONAL FRONT MEZZANINE ADAPTER

The Cisco UCS X215c M8 Compute Node has one front mezzanine connector that can 
accommodate one of the following mezzanine cards form the 

Table 13.

NOTE:  

■ The Cisco UCS X215c M8 Compute Node can be ordered with or without the 

front mezzanine adapter. 

■ Only one Front Mezzanine connector or Front GPU can be selected per Server.

■ RAID with NVMe drives is only supported with the NVMe U.2/U.3 drives as they 
connect to the RAID controller and RAID is not supported with the NVMe drives as 
they directly interface with the server via the PCIe bus

Table 13  Available Front Mezzanine Adapters 1

Product ID(PID)

PID Description

Connector 
Type

UCSX-X10C-PT4F-D

Cisco UCS X215c M8 Compute Node pass through controller for up 
to 6 NVMe drives

Front 
Mezzanine

■ Supports up to 6 U.2/U.3 NVMe drives

■ Mixing of U.2 and U.3 NVMe drives are allowed

UCSX-X10C-RAIDF-D

Cisco UCS X215c M8 Compute Node RAID controller w/4GB Cache, 
with LSI 3900 for up to 6 SAS/SATA/NVMe drives (SAS/SATA and 
NVMe drives can be mixed)

Front 
Mezzanine

■ If SAS/SATA drives are s selected, then this controller must 

also be selected.

■ If UCSX-X10C-RAIDF-D is selected, it supports a maximum 
quantity of 6 SAS/SATA drives, or 4 NVMe U.2 drives, or 6 
NVMe U.3 drives.

■ Mixing SAS/SATA/NVMe U.2/U.3 drives is allowed.

UCSX-RAID-M1L6

24G Tri-Mode M1 RAID Controller w/4GB FBWC 6Drv

■ Supports up to 6 U.3 NVMe drives

■ RAID levels 0, 1, 5, 6, 10, and 50) for 6 SAS/SATA/U.3 NVMe 
drives or optionally up to 2 U.3 NVMe drives (drive slots 5-6) 
in pass-through

Front 
Mezzanine

UCSX-X10C-PTE3

Cisco UCS X215c M8 Compute Node Pass Through Controller for 
E3.S (Front)

Front 
Mezzanine

■ It supports a maximum of 8 E3.S drives

■ Cannot mix with 2.5in SATA/SAS/U.2/U.3 drives

■ Not supporting drive in drive slot 5

24

Cisco UCS X215c M8 Compute Node

CONFIGURING the Cisco UCS X215c M8 Compute Node

Table 13  Available Front Mezzanine Adapters (continued)2

UCSX-X10C-GPUFM-D

UCS X10c Compute Node GPU Front Mezz

■ Supports configurations with either 1 or 2 CPUs.

■ If selected, supports a maximum of 2 NVMe U.2/U.3 drives. 

Mixing of U.2 and U.3 drives are allowed.

■ If GPU PCIe Node is selected, this mezzanine is only 

compatible with the UCSX-GPU-L4-MEZZ GPU.

■ Drive blanks are included, if no drives are selected.

Front 
Mezzanine

Cisco UCS X215c M8 Compute Node

25

CONFIGURING the Cisco UCS X215c M8 Compute Node

STEP 7 CHOOSE OPTIONAL GPU PCIe NODE

 Refer to Table 14 for GPU PCIe Node

Table 14  GPU PCIe Node

Product ID(PID)

PID Description

UCSX-440P-D

UCS X-Series Gen4 PCIe node

UCSX-580P

UCS X-Series Gen5 PCIe node

NOTE:  

■ If PCIe Node is selected, then rear mezzanine is required.

26

Cisco UCS X215c M8 Compute Node

CONFIGURING the Cisco UCS X215c M8 Compute Node

STEP 8 CHOOSE OPTIONAL GPUs

Select GPU Options

The available Compute node GPU options are listed in Table 15

NOTE:  

The available PCIe node GPU options are listed in:

■ For the supported GPU card supported on the x580P PCIe Node is listed on the 
https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-com
puting/ucs-x-series-modular-system/x580p-specsheet.pdf, Step 2, Order GPU 
Cards

■ For the supported GPU card supported on the x4400P PCIe Node is listed on the 
https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-com
puting/ucs-x-series-modular-system/x440p-specsheet.pdf, Step 3, Order GPU 
Cards

Table 15  Available PCIe GPU Card supported on the Compute Node Front Mezz

GPU Product ID (PID) PID Description

UCSX-GPU-L4-MEZZ

NVIDIA GPU L4, Gen4x16, 1 Slot, HHHL, 70W 24GB, PCIe

Cisco UCS X215c M8 Compute Node

27

CONFIGURING the Cisco UCS X215c M8 Compute Node

STEP 9 CHOOSE OPTIONAL DRIVES

The standard storage drive features are:

■ 2.5-inch small form factor drives or E3.S 1T NVMe drives

■ Hot-pluggable

■ Drives come mounted in sleds

Select Drives Table 16.

NOTE:  

■ The Cisco UCS X215c M8 Compute Node can be ordered with or without drives. 

■ Select one to six 2.5-inch small form factor SAS/SATA SSDs or PCIe U.2/U.3 

NVMe drives

■ Select one to eight E3.S 1T NVMe drives

■ If SAS/SATA/SED drives are selected, then UCSX-X10C-RAIDF-D must also be 

selected.

■ Drive slot 5 is not supported for E3.S drives on the compute node and must 

include a drive filler (UCSC-E3S1T-F)

Table 16  Available Drive Options  

Product ID (PID)

Description

Drive 
Type

Speed  Size

12G
12G
6G

1.6TB 2.5in Enter Perf 12G SAS Kioxia G2 SSD (3X SED-FIPS) SAS
SAS
3.8TB 2.5in Enter Value 12G SAS Kioxia G2 SSD (SED-FIPS)
SATA
960GB 2.5in Enter Value 6G SATA Micron G2 SSD (SED)

SAS/SATA SSDs
Self-Encrypted Drives (SED)
UCSX-SD16TBKANK9D
UCSX-SD38TBKANK9D 
UCSX-SD960GM2NK9D
Enterprise Performance SSDs (high endurance, supports up to 3X DWPD (drive writes per day))
1.6TB 2.5in Enter Perf 24G SAS Kioxia PM7 SSD (3X)
UCSX-SD16TKA3XEPD
3.2TB 2.5in Enter Perf 24G SAS Kioxia PM7 SSD (3X)
UCSXSD32TKA3XEP-D
1.9TB 2.5 inch Enterprise performance 6G SATA SSD 
UCSX-SD19T63XEP-D
(3X endurance)
480GB 2.5in Enterprise performance 6G SATA SSD 
(3X endurance)
1.9TB 2.5in Enter Perf 6G SATA Micron G2 SSD (3X)
480GB 2.5in Enter Perf 6G SATA Micron G2 SSD (3X)
960GB 2.5in Enter Perf 6G SATA Micron G2 SSD (3X)
480GB 2.5in 15mm Solidigm S4620 Enter Perf 6G SATA 3X 
SSD
1.9TB 2.5in 15mm Solidigm S4620 Enter Perf 6G SATA 3X 
SSD
960GB 2.5in 15mm Solidigm S4620 Enter Perf 6G SATA 3X 
SSD

UCSX-SD19TBM3XEPD
UCSXSD480GBM3XEPD
UCSXSD960GBM3XEPD
UCSX-SDB480OA1P

SATA
SATA
SATA
SATA

UCSXSD480G63XEP-D

UCSX-SDB1T9OA1P

UCSX-SDB960OA1P

SAS
SAS
SATA

12G
12G
6G

6G
6G
6G
6G

SATA

SATA

SATA

6G

6G

6G

1.6TB
3.8TB
960GB

1.6TB
3.2TB
1.9TB

480GB

1.9TB
480GB
960GB
480GB

1.9TB

960GB

28

Cisco UCS X215c M8 Compute Node

CONFIGURING the Cisco UCS X215c M8 Compute Node

Table 16  Available Drive Options (continued) 

Product ID (PID)

Description

UCSX-SDB3T8OA1P

UCSX-SDB480OA1V

UCSX-SDB960OA1V

UCSX-SDB3T8OA1V

3.8TB 2.5in 15mm Solidigm S4620 Enter Perf 6G SATA 3X 
SSD
480GB 2.5in 15mm Solidigm S4520 Enter Perf 6G SATA 1X 
SSD
960GB 2.5in 15mm Solidigm S4520 Enter Perf 6G SATA 1X 
SSD
3.8TB 2.5in 15mm Solidigm S4520 Enter Perf 6G SATA 1X 
SSD

Drive 
Type

Speed  Size

SATA

6G

3.8TB

SATA

6G

480GB

SATA

6G

960GB

SATA

6G

3.8TB

Enterprise Value SSDs (Low endurance, supports up to 1X DWPD (drive writes per day)) 
UCSXSD240GBM1XEVD
UCSXSD480GBM1XEVD
UCSX-SD19TBM1XEVD
UCSX-SDB960SA1VD

SATA
SATA
SATA
SATA

6G
6G
6G
6G

240GB
480GB
1.9TB
960GB

240GB 2.5in Enter Value 6G SATA Micron G2 SSD
480 GB 2.5in Enter Value 6G SATA Micron G2 SSD
1.9TB 2.5in Enter Value 6G SATA Micron G2 SSD
960GB 2.5in 6G SATA Enter Value 1X Samsung G1PM893A 
SSD
1.9TB 2.5in 6G SATA Enter Value 1X Samsung G1PM893A 
SSD
3.8TB 2.5in 6G SATA Enter Value 1X Samsung G1PM893A 
SSD
7.6TB 2.5in 6G SATA Enter Value 1X Samsung G1PM893A 
SSD
3.8TB 2.5in Enter Value 24G SAS Kioxia PM7 SSD

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

12G

3.8TB

UCSX-SDB1T9SA1VD

UCSX-SDB3T8SA1VD

UCSX-SDB7T6SA1VD

UCSXSD38TKA1XEV-D
NVMe

UCSX-NVMEG4M1536D 15.3TB 2.5in U.3 Micron 7450 NVMe High Perf Medium 

NVMe

U.3

15.3TB

Endurance

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

UCSX-NVB960M2V

UCSX-NVB1T9M2V

UCSX-NVB3T2M2P

UCSX-NVB3T8M2V

UCSX-NVB3T8M2V9

UCSX-NVB1T9M2V9

UCSX-NVB7T6M2V9

Endurance
960GB 2.5in U.3 15mm Micron 7500 Hg Perf Med End 1X 
NVMe
1.9TB 2.5in U.3 15mm Micron 7500 Hg Perf Med End 1X 
NVMe
3.2TB 2.5in U.3 15mm Micron 7500 Hg Perf Hg End 3X 
NVMe
3.8TB 2.5in U.3 15mm Micron 7500 Hg Perf Med End 1X 
NVMe
3.8TB 2.5in U.3 15mm Micron 7500 HgPerf MedEnd 1X 
NVMe FIPS
1.9TB 2.5in U.3 15mm Micron 7500 HgPerf MedEnd 1X 
NVMe FIPS
7.6TB 2.5in U.3 15mm Micron 7500 HgPerf MedEnd 1X 
NVMe FIPS

NVMe

U.3

960GB

NVMe

U.3

1.9TB

NVMe

U.3

3.2TB

NVMe

U.3

3.8TB

NVMe

U.3

3.8 TB

NVMe

U.3

1.9 TB

NVMe

U.3

7.6 TB

Cisco UCS X215c M8 Compute Node

29

CONFIGURING the Cisco UCS X215c M8 Compute Node

Table 16  Available Drive Options (continued) 

Product ID (PID)

Description

UCSX-NVB15T3M2V9

UCSX-NVB12T8M2P

UCSX-NVB7T6M2V

UCSX-NVB15T3M2V

E3.S
UCSX-NVE112T8K1P

UCSX-NVE11T6K1P

UCSX-NVE13T2K1P

UCSX-NVE16T4K1P

UCSX-NVE115T3K1V

UCSX-NVE11T9K1V

UCSX-NVE13T8K1V

UCSX-NVE17T6K1V

UCSX-NVE11T6S1P

UCSX-NVE13T2S1P

UCSX-NVE16T4S1P

UCSX-NVE112T8S1P

UCSX-NVE11T9S1V

UCSX-NVE13T8S1V

UCSX-NVE17T6S1V

UCSX-NVE115T3S1V

15.3TB 2.5in U.3 15mm Micron 7500 HgPerf MedEnd 1X 
NVMe FIPS
12.8TB 2.5in U.3 15mm Micron 7500 Hg Perf Hg End 3X 
NVMe
7.6TB 2.5in U.3 15mm Micron 7500 Hg Perf Med End 1X 
NVMe
15.3TB 2.5in U.3 15mm Micron 7500 Hg Perf Med End 1X 
NVMe

Drive 
Type

Speed  Size

NVMe

U.3

15.3 TB

NVMe

U.3

12.8TB

NVMe

U.3

7.6 TB

NVMe

U.3

15.3 TB

12.8TB E3.S1T KCD8XPJE HgPerf HgEnd Gen5 3X NVMe (SIE 
SCEF)
1.6TB E3.S1T KCD8XPJE HgPerf HgEnd Gen5 3X NVMe (SIE 
SCEF)
3.2TB E3.S1T KCD8XPJE HgPerf HgEnd Gen5 3X NVMe (SIE 
SCEF)
6.4TB E3.S1T KCD8XPJE HgPerf HgEnd Gen5 3X NVMe (SIE 
SCEF)
15.3TB E3.S1T KCD8XPJE HgPerf MedEnd Gen5 1X NVMe 
(SIE SCEF)
1.9TB E3.S1T KCD8XPJE HgPerf MedEnd Gen5 1X NVMe (SIE 
SCEF)
3.8TB E3.S1T KCD8XPJE HgPerf MedEnd Gen5 1X NVMe (SIE 
SCEF)
7.6TB E3.S1T KCD8XPJE HgPerf MedEnd Gen5 1X NVMe (SIE 
SCEF)
1.6TB E3.S1T PM1745 HgPerf HgEnd Gen5 3X NVMe (TCG 
OPAL)
3.2TB E3.S1T PM1745 HgPerf HgEnd Gen5 3X NVMe (TCG 
OPAL)
6.4TB E3.S1T PM1745 HgPerf HgEnd Gen5 3X NVMe (TCG 
OPAL)
12.8TB E3.S1T PM1745 HgPerf HgEnd Gen5 3X NVMe (TCG 
OPAL)
1.9TB E3.S1T PM1743 HgPerf MedEnd Gen5 1X NVMe (TCG 
OPAL)
3.8TB E3.S1T PM1743 HgPerf MedEnd Gen5 1X NVMe (TCG 
OPAL)
7.6TB E3.S1T PM1743 HgPerf MedEnd Gen5 1X NVMe (TCG 
OPAL)
15.3TB E3.S1T PM1743 HgPerf MedEnd Gen5 1X NVMe (TCG 
OPAL)

NVMe

E3.S

12.8TB

NVMe

E3.S

1.6TB

NVMe

E3.S

3.2TB

NVMe

E3.S

6.4TB

NVMe

E3.S

15.3TB

NVMe

E3.S

1.9TB

NVMe

E3.S

3.8TB

NVMe

E3.S

7.6TB

NVMe

E3.S

1.6TB

NVMe

E3.S

3.2TB

NVMe

E3.S

6.4TB

NVMe

E3.S

12.8TB

NVMe

E3.S

1.9TB

NVMe

E3.S

3.8TB

NVMe

E3.S

7.6TB

NVMe

E3.S

15.3TB

NOTE:  Cisco uses solid state drives from several vendors. All solid state drives are subject to physical write 
limits and have varying maximum usage limitation specifications set by the manufacturer. Cisco will not 
replace any solid state drives that have exceeded any maximum usage specifications set by Cisco or the 
manufacturer, as determined solely by Cisco.

30

Cisco UCS X215c M8 Compute Node

CONFIGURING the Cisco UCS X215c M8 Compute Node

STEP 10 Order Boot-optimized M.2 Front Panel Module and Drives

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

■ The Boot-Optimized RAID controller supports VMware, Windows, and Linux Operating 

Systems

Table 17  Boot-Optimized RAID controller (auto included)

Product ID (PID)

PID Description

UCSX-M2-HWRD-FPS

UCSX Front panel with M.2 RAID controller for SATA drives

■ Select Cisco M.2 SATA SSDs: Order one or two matching M.2 SATA SSDs. This connector accepts the 

boot-optimized RAID controller (see Table 17). Each boot-optimized RAID controller can accommodate 
up to two SATA M.2 SSDs shown in Table 18.

NOTE:  

■ Each boot-optimized RAID controller can accommodate up to two SATA M.2 SSDs 

shown in Table 18. The boot-optimized RAID controller plugs into the 
motherboard.

■ It is recommended that M.2 SATA SSDs be used as boot-only devices.

■ The SATA M.2 drives can boot in UEFI mode only. Legacy boot mode is not 

supported.

Table 18  M.2 SATA SSDs

Product ID (PID)

PID Description

UCSX-M2-240G-D

UCSX-M2-480G-D

UCSX-M2-960G-D
UCSX-M2240OA1V
UCSX-M2480OA1V 

240GB 2.5in M.2 SATA Micron G2 SSD

480GB 2.5in M.2 SATA Micron G2 SSD

960GB 2.5in M.2 SATA Micron G2 SSD
240GB M.2 Boot Solidigm S4520 SATA 1X SSD
480GB M.2 Boot Solidigm S4520 SATA 1X SSD

Cisco UCS X215c M8 Compute Node

31

CONFIGURING the Cisco UCS X215c M8 Compute Node

STEP 11 ORDER NVMe BOOT

 (OPTIONAL)

Table 19  NVMe BOOT

Product ID (PID)

PID Description

UCSX-M2-PT-FPN

UCSX Front Panel w/M.2 Pass Through Controller for NVME Drv

Table 20  M.2 NVMe

Product ID (PID)

PID Description

UCSX-NVM2-400GB
UCSX-NVM2-960GB

400GB M.2 Boot NVMe 
960GB M.2 Boot NVMe

32

Cisco UCS X215c M8 Compute Node

CONFIGURING the Cisco UCS X215c M8 Compute Node

STEP 12    CHOOSE OPTIONAL TRUSTED PLATFORM MODULE 

Trusted Platform Module (TPM) is a computer chip or microcontroller that can securely store 
artifacts used to authenticate the platform or Cisco UCS X215c M8 Compute Node. These 
artifacts can include passwords, certificates, or encryption keys. A TPM can also be used to 
store platform measurements that help ensure that the platform remains trustworthy. 
Authentication (ensuring that the platform can prove that it is what it claims to be) and 
attestation (a process helping to prove that a platform is trustworthy and has not been 
breached) are necessary steps to ensure safer computing in all environments.

Table 21  Available TPM Option  

Product ID (PID)

Description

UCSX-TPM2-002D-D

TPM 2.0 FIPS 140-2 MSW2022 compliant AMD M8 servers

UCSX-TPM-OPT-OUT-D1

OPT OUT, TPM 2.0, TCG, FIPS140-2, CC EAL4+ Certified

Notes:

1. Please note Microsoft certification requires a TPM 2.0 for bare-metal or guest VM deployments. Opt-out of the 

TPM 2.0 voids the Microsoft certification.

NOTE:  

■ The TPM module used in this system conforms to TPM v2.0 as defined by the 

Trusted Computing Group (TCG). 

■ TPM installation is supported after-factory. However, a TPM installs with a 

one-way screw and cannot be replaced, upgraded, or moved to another compute 
node. If a Cisco UCS X215c M8 Compute Node with a TPM is returned, the 
replacement Cisco UCS X215c M8 Compute Node must be ordered with a new 
TPM. If there is no existing TPM in the Cisco UCS X215c M8 Compute Node, you 
can install a TPM 2.0. Refer to the following document for Installation location 
and instructions:

https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/x/hw/x215c-m8/i
nstall/b-cisco-ucs-x215c-m8-install/b-cisco-ucs-x215c-m8-install_index.html

Cisco UCS X215c M8 Compute Node

33

CONFIGURING the Cisco UCS X215c M8 Compute Node

STEP 13 CHOOSE OPERATING SYSTEM AND VALUE-ADDED SOFTWARE

■ Operating System (Table 22)

NOTE:  

■ See this link for operating system guidance: 

https://ucshcltool.cloudapps.cisco.com/public/

Table 22  Operating System 

Product ID (PID)

PID Description

Microsoft Windows Server

MSWS-22-ST16CD 

Windows Server 2022 Standard (16 Cores/2 VMs)

MSWS-22-ST16CD-NS

Windows Server 2022 Standard (16 Cores/2 VMs) - No Cisco SVC

MSWS-22-DC16CD

Windows Server 2022 Data Center (16 Cores/Unlimited VMs)

MSWS-22-DC16CD-NS

Windows Server 2022 DC (16 Cores/Unlim VMs) - No Cisco SVC

MSWS-19-ST16CD

Windows Server 2019 Standard (16 Cores/2 VMs)

MSWS-19-ST16CD-NS

Windows Server 2019 Standard (16 Cores/2 VMs) - No Cisco SVC

MSWS-19-DC16CD

Windows Server 2019 Data Center (16 Cores/Unlimited VMs)

MSWS-19-DC16CD-NS

Windows Server 2019 DC (16 Cores/Unlim VMs) - No Cisco SVC

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

34

Cisco UCS X215c M8 Compute Node

CONFIGURING the Cisco UCS X215c M8 Compute Node

Table 22  Operating System (continued)

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

Cisco UCS X215c M8 Compute Node

35

CONFIGURING the Cisco UCS X215c M8 Compute Node

Table 22  Operating System (continued)

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

36

Cisco UCS X215c M8 Compute Node

CONFIGURING the Cisco UCS X215c M8 Compute Node

STEP 14 CHOOSE OPTIONAL OPERATING SYSTEM MEDIA KIT

Select the optional operating system media listed in Table 23.

Table 23  OS Media  

Product ID (PID)

PID Description

MSWS-22-ST16CD-RM

Windows Server 2022 Stan (16 Cores/2 VMs) Rec Media DVD Only

MSWS-22-DC16CD-RM

Windows Server 2022 DC (16Cores/Unlim VM) Rec Media DVD Only

Cisco UCS X215c M8 Compute Node

37

SUPPLEMENTAL MATERIAL

SUPPLEMENTAL MATERIAL

Simplified Block Diagram

A simplified block diagram of the Cisco UCS X215c M8 Compute Node system board is shown in Figure 8.

Figure 8  

Cisco UCS X215c M8 Compute Node Simplified Block Diagram (VIC 25G with Drives)

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

38

Cisco UCS X215c M8 Compute Node

 
 
 
 
 
 
Figure 9  

Cisco UCS X215c M8 Compute Node Simplified Block Diagram (VIC 100G with Drives)

SUPPLEMENTAL MATERIAL

Disk 1

. . . . . . .

Disk n

Local Storage

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

Cisco UCS X215c M8 Compute Node

39

 
 
 
 
SUPPLEMENTAL MATERIAL

Figure 10  

Cisco UCS X215c M8 Compute Node Simplified Block Diagram (VIC 25G with Drives and GPUs)

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

40

Cisco UCS X215c M8 Compute Node

 
 
 
 
 
 
Figure 11  Cisco UCS X215c M8 Compute Node Simplified Block Diagram (VIC 100G with Drives and GPUs) 

SUPPLEMENTAL MATERIAL

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

1

2

3

4

Front mezzanine slot for SAS/SATA or 
NVMe drives and M.2 Controllers.

DIMM slots (32 maximum)

CPU 1 slot (shown populated)

CPU 2 slot (shown populated)

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

Please refer to the Cisco UCS X215c M8 Compute Node Installation Guide for installation procedures.

Cisco UCS X215c M8 Compute Node

41

 
 
 
 
SPARE PARTS

SPARE PARTS

This section lists the upgrade and service-related parts for the Cisco UCS X215c M8 Compute Node. Some of 
these parts are configured with every server.

■ Spare parts for the Cisco UCS X215c M8 Compute Node use the same Product IDs (PIDs) as the regular 
components, with the addition of an equals sign (=) at the end of the PID. For example, if the 
regular PID for a component is UCS-CPU-I6760P, its corresponding spare PID would be 
UCS-CPU-I6760P=

■ Therefore, to find the full list of available spare parts and their descriptions, refer to the relevant 
sections for each component (e.g., Risers, CPUs, Memory, Drive Controllers, Drives, PCIe Cards, 
Power Supplies, etc.) and append an = to the listed PIDs.

NOTE:  Some spare parts you order may also require accessories for full 
functionality. For example, drives or RAID controllers may need accompanying 
cables. CPUs may need heatsinks, thermal paste, and installation tools. The spares 
and their accessory parts are listed in Table 24.

However, the Table 24 below lists the spare parts and their descriptions. These are different from the main 
components described in previous sections. This table is the complete list for all spare part IDs (they end 
with an '=' sign), as these specific spare parts are not listed individually in those earlier sections.

Table 24  Spare Parts

Product ID (PID)

PID Description

UCSX-M8A-HS-F
UCSX-M8A-HS-R
UCS-DDR5-BLK
UCSX-M8A-FMEZZBLK
UCSC-BBLKD-M7
UCSX-V5-BRIDGE-D
UCSX-M2-PT-FPN 
UCSC-E3S1T-F 

Front Heatsink for AMD X series servers
Rear Heatsink for AMD X series servers
UCS DDR5 DIMM Blanks
Front Mezzanine Blank for AMD X series servers
UCS C-Series M7 SFF drive blanking panel
UCS VIC 15000 bridge to connect mLOM and mezz X Compute Node 
UCSX Front Panel w/M.2 Pass Through Controller for NVME Drv
UCS C-Series E3.S 1T Drive Filler

42

Cisco UCS X215c M8 Compute Node

UPGRADING or REPLACING CPUs and Memory

UPGRADING or REPLACING CPUs and Memory

■ Refer to Cisco UCS X215c M8 Server Installation and Service Guide for upgrading or replacing the CPUs 

and Memory Devices.

Cisco UCS X215c M8 Compute Node

43

TECHNICAL SPECIFICATIONS

TECHNICAL SPECIFICATIONS

Dimensions and Weight

Table 25  Cisco UCS X215c M8 Compute Node Dimensions and Weight  

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

Table 26  Cisco UCS X215c M8 Compute Node Environmental Specifications  

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

44

Cisco UCS X215c M8 Compute Node

DISCONTINUED EOL PRODUCTS

DISCONTINUED EOL PRODUCTS

Below is the list of parts were previously available for this product and are no longer sold. Please refer to 
the EOL Bulletin Links via table below to determine if still supported.

Table 27

  EOS

Product ID

Description

EOL/EOS link

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

UCSX-M2-I480GB-D

480GB SATA M.2 SSD

UCSXSD480G63XEP-D

480GB 2.5in Enter Perf 6G SATA 
Intel SSD (3X)

UCSX-SD19T63XEP-D

1.9TB 2.5in Enter Perf 6G SATA 
Intel SSD (3X)

UCSX-M2-I240GB-D

240GB M.2 Boot SATA Intel SSD

UCSX-MR256G8RE3

256GB DDR5-5600 RDIMM 8Rx4 
(16Gb)

https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-c-series-rack-ser
vers/select-ucs-ucsx-hci-accessories-eol15818.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-c-series-rack-ser
vers/select-ucs-ucsx-hci-accessories-eol15818.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-c-series-rack-ser
vers/select-ucs-ucsx-hci-accessories-eol15818.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-c-series-rack-ser
vers/select-ucs-ucsx-hci-accessories-eol15818.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-c-series-rack-ser
vers/select-ucs-accessories-eol15502.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-c-series-rack-ser
vers/select-ucs-accessories-eol15502.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-c-series-rack-ser
vers/select-ucs-accessories-eol15502.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-c-series-rack-ser
vers/select-ucs-accessories-eol15502.html
https://www.cisco.com/c/en/us/products/collater
al/servers-unified-computing/ucs-c-series-rack-ser
vers/ucs-accessories_eol.html

Cisco UCS X215c M8 Compute Node

45

DISCONTINUED EOL PRODUCTS

46

Cisco UCS X215c M8 Compute Node

