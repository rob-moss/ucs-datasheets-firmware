# Cisco UCS 9108 100G Intelligent Fabric Module Spec Sheet

| | |
|---|---|
| **URL Title** | Cisco UCS 9108 100G Intelligent Fabric Module Spec Sheet |
| **URL** | https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-x-series-modular-system/cisco-ucs-9108-100g-intelligent-fabric-module-spec-sheet.pdf |
| **Long URL** |  |
| **HTML Title** |  |
| **Source file** | `ucs-docs-raw/pdf/cisco-ucs-9108-100g-intelligent-fabric-module-spec-sheet.pdf` |
| **File type** | PDF |
| **Fetched on** | 2026-03-25 11:35:46 |

---

Spec Sheet

Cisco UCS 9108 100G 
Intelligent Fabric Module
A printed version of this document is only a 
copy and not necessarily the latest version. 
Refer to the following link for the latest 
released version:

https://www.cisco.com/c/en/us/products/servers-
unified-computing/ucs-x-series-modular-system/
datasheet-listing.html 

CISCO SYSTEMS
170 WEST TASMAN DR.
SAN JOSE, CA, 95134
WWW.CISCO.COM

PUBLICATION HISTORY

REV A.11

FEBRUARY 18, 2026



STEP
STEP

Overview  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
LED Indicators   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
Capabilities and Features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
CONFIGURING the INTELLIGENT FABRIC MODULE (IFM)  . . . . . . . . . . . . . . . . . 9
1 VERIFY INTELLIGENT FABRIC MODULE SKU  . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2 CHOOSE TRANSCEIVERS (OPTIONAL)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
SUPPLEMENTAL MATERIAL  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  13
Port Numbering  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
Fabric Interconnect Compatibility . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
Connectivity  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
TECHNICAL SPECIFICATIONS  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  15
Physical and Environmental Specifications   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
ACCESSORIES/SPARE PARTS   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  16

2

Cisco UCS 9108 100G IFM

Overview

Overview

The Cisco UCS 9108 100G Intelligent Fabric Module (IFM) brings the unified fabric into the blade server 
enclosure, providing connectivity between the blade servers and the fabric interconnect, simplifying 
diagnostics, cabling, and management.

The Cisco UCS 9108 100G IFM connects the I/O fabric between the 6500/6600 series Fabric Interconnect and 
the Cisco UCS X9508 Chassis, enabling a lossless and deterministic converged fabric to connect all blades 
and chassis together. Because the fabric extender is similar to a distributed line card, it does not perform 
any switching and is managed as an extension of the fabric interconnects. This approach removes switching 
from the chassis, reducing overall infrastructure complexity and enabling Cisco UCS to scale to many chassis 
without multiplying the number of switches needed, reducing TCO, and allowing all chassis to be managed 
as a single, highly available management domain.

The Cisco UCS 9108 100G IFM also manages the chassis environment (power supply, fans, and blades) in 
conjunction with the fabric interconnect. Therefore, separate chassis-management modules are not 
required.

The IFM plugs into the rear side of the Cisco UCS X9508 chassis. The IFM provides a data path from the 
chassis compute nodes to the Cisco UCS 6500/6600 series Fabric Interconnect. Up to two Intelligent Fabric 
Modules (IFMs) plug into the back of the Cisco UCS X9508 chassis.

The IFMs serve as line cards in the chassis and multiplex data from the compute nodes to the Fabric 
Interconnect (FI). They also monitor and manage chassis components such as fan units, power supplies, 
environmental data, LED status panel, and other chassis resources. The server compute node 
Keyboard-Video-Mouse (KVM) data, Serial over LAN (SoL) data, and Intelligent Platform Management 
Interface (IPMI) data also travel to the IFMs for monitoring and management purposes. In order to provide 
redundancy and failover, the IFMs are always used in pairs.

There are 8 x QSFP28 external connectors on an IFM to interface with a Cisco UCS 6500/6600 series Fabric 
Interconnect. The IFM internally provides 1 x 100G or 4 x 25G connections towards each UCS X210c Compute 
Node in the Cisco X9508 chassis.

When a compute node is inserted into the chassis, the compute node’s mezzanine card (mLOM) connects to 
the IFMs using orthogonal direct connectors. Figure 1 shows the IFM front view characteristics.

Cisco UCS 9108 100G IFM

3

Overview

Figure 1

  Cisco UCS 9108-100G IFM (front view)

1 

Status LEDs:

2

IFM Reset Button

IFM Status (top LED)

Fan Status LEDs 1 through 3, with 
Fan 1 as LED 2, Fan 2 as LED 3, and 
Fan 3 as LED 4. 

3

QSFP28 Optical Ports. 

4

IFM Ejector Handles, left and right

Ports are arranged in two groups of four 
physical ports. Ports are stacked in 
vertical pairs, with two ports in each 
vertical port stack. 

Figure 2 shows the IFM top view characteristics.

4

Cisco UCS 9108 100G IFM

■
■
Figure 2

  Cisco UCS 9108-100G IFM (top view)

Overview

1 

3

Fans (3) which are numbered 1 through 3 
starting with the left fan

QSFP28 Optical Ports 1-4

Ports are arranged in two groups of four 
physical ports. Ports are stacked in vertical 
pairs, with two ports in each vertical port 
stack. 

5

IFM ejector handles, left and right

2

4

-

One M.2 mini storage module slot

QSFP28 Optical Ports 5-8

Ports are arranged in two groups of four 
physical ports. Ports are stacked in vertical 
pairs, with two ports in each vertical port 
stack. 

Cisco UCS 9108 100G IFM

5

LED Indicators

LED Indicators

The LED indicators are described in Table 1 (see Figure 1 on page 4 for LED locations)

Table 1   IFM LED States

LED

IFM Status

State

OFF

GREEN

AMBER

Description

Power OFF

Normal Operation

Booting or minor Temperature Alarm

BLINKING AMBER

Stopped in uboot or unable to come online, or major 
temperature alarm

FAN status LED # 1, 
2, 3

QSFP Port LED 
status 1 LED per 
port per color

OFF

GREEN

AMBER

OFF

GREEN

AMBER

Power OFF

Normal Operation

Fan fault (low fan speed or fan not running)

Link enabled but not connected

Link connected

Operator disabled 

BLINKING AMBER

Disabled due to error

6

Cisco UCS 9108 100G IFM

 
Capabilities and Features

Capabilities and Features

Table 2 lists the capabilities and features of the Cisco UCS 9108 100G Intelligent Fabric Module. Details 
about how to configure the IFM for a particular feature or capability are provided in CONFIGURING the 
INTELLIGENT FABRIC MODULE (IFM) on page 9. 

Table 2   Capabilities and Features  

Capability/Feature

Description

Server data path 
bandwidth

800 Gb/s for 8 compute nodes

(1 x 100 Gb/s or 4 x 25 Gb/s lanes per compute node, for a total of 100 Gb/s 
per compute node)

Network data path 
bandwidth

800Gb/s

100 Gb/s per port x 8 QSFP28 ports

CPU complex

Intel® Denverton Processor (4 core, 2.2GHz, 15W)

DDR4 memory: 8GB max @ 2133 MHz

Fibre Channel

FCoE

Fans

The IFM has three dual-rotor on board fans. The air flow direction is aligned 
with chassis air flow direction, which is front to rear. 

The IFM Fans have minimum RPM requirements to be compatible with the 
chassis/system main fans. The fans are powered from 54VDC/48VDC. Fan 
speed is controlled and monitored by the IFM CPU using a fan controller IC.

Power Supply

Power supplied by chassis

Power consumption

237W

Cisco Intersight 
Management

Unified Fabric

Fabric Extender 
Architecture

QSFP28-compatible 
ports

Allows all elements connected to the interconnects to participate in a 
single, highly available management domain

Decreases total cost of ownership (TCO) by reducing the number of 
NICs, HBAs, switches, and cables needed

Transparently encapsulates Fibre Channel packets into Ethernet

Increases flexibility with a range of interconnect solutions, including 
copper Twinax cable for short runs and fiber for long runs

Consumes less power per port than traditional solution

Scales without adding complexity by eliminating the need for dedicated 
chassis management and compute nodes and by reducing the number of 
cables needed

Provides deterministic latency for optimized application performance

Allows the 8 fixed ports to operate in 100 Gigabit Ethernet mode with the 
transceiver options specified for use with QSFP28-compatible ports in 
Table 4 on page 11. The QSFP28 ports on the IFM are bound to a 
port-channel towards the fabric-interconnect and any number of links 
between 1 thru 8 could be active on this port-channel between FI and IFM.

Cisco UCS 9108 100G IFM

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
Capabilities and Features

Table 2   Capabilities and Features  (continued)

Capability/Feature

Description

Transceivers

The Cisco UCS 9108-100G IFM supports 100G connectivity using Cisco 100 
Gbps modules.

Performance

Provides high-speed, low-latency connectivity to the chassis

Provides approximately 50% reduction in end-to-end system latency 
(latency is less than 1 microseconds)

Lossless Fabric

Provides a reliable, robust foundation for unifying LAN and SAN traffic on a 
single transport

Priority Flow Control 
(PFC)

Simplifies management of multiple traffic flows over a single network 
link

Supports different classes of service, helping enable both lossless and 
classic Ethernet on the same fabric

Systemwide Bandwidth 
Management

Helps enable consistent and coherent quality of service (QoS) throughout the 
system

8

Cisco UCS 9108 100G IFM

■
■
■
■
CONFIGURING the INTELLIGENT FABRIC MODULE (IFM)

CONFIGURING the INTELLIGENT FABRIC MODULE (IFM)

Follow these steps to configure the Cisco UCS 9108 100G IFM:

STEP 1 VERIFY INTELLIGENT FABRIC MODULE SKU, page 10

STEP 2 CHOOSE TRANSCEIVERS (OPTIONAL), page 11

 SUPPLEMENTAL MATERIAL, page 13

Cisco UCS 9108 100G IFM

9

■
■
■
CONFIGURING the INTELLIGENT FABRIC MODULE (IFM)

STEP 1

VERIFY INTELLIGENT FABRIC MODULE SKU

Verify the product ID (PID) of the IFM as shown in Table 3.

Table 3   Available Intelligent Fabric Modules 

Product ID (PID)

Description

Number of 
100 GbE/FCoE 
Ports to ToR

Number of Internal GbE/FCoE 
Ports 

UCSX-I-9108-100G

UCS 9108 100G IFM 
for X9508 chassis

UCSX-I9108-100G-D

UCS 9108 100G IFM 
for X9508 chassis

8

8

8 x 100G or 32 x 25G or a 
combination of 100G and 25G 
depending on the VIC 
15000/14000 series in the 
compute node.

8 x 100G or 32 x 25G or a 
combination of 100G and 25G 
depending on the VIC 
15000/14000 series in the 
compute node.

Total 
Chassis I/O 
per IFM

3.2 Tbps

3.2 Tbps

NOTE:  Use the steps on the following pages to order the Intelligent 
Fabric Module with the components that you want configured in your 
order.

10

Cisco UCS 9108 100G IFM

CONFIGURING the INTELLIGENT FABRIC MODULE (IFM)

STEP 2 CHOOSE TRANSCEIVERS (OPTIONAL)

The Cisco UCS 9108 100G IFM supports a wide variety of 100 Gigabit Ethernet connectivity 
options using Cisco 100 Gbps modules.

Choose Transceivers

The supported transceivers are for the UCS 9108 100G IFM are listed in Table 4.

Table 4   UCS 9108 100G Supported Transceivers 

Product ID (PID)

Description

QSFP28 100G Transceivers

QSFP-100G-SR4-S

100GBASE SR4 QSFP Transceiver, MPO, 100m over OM4 MMF

QSFP-100G-LR4-S

100GBASE LR4 QSFP Transceiver, LC, 10km over SMF

QSFP-40/100-SRBD

100GBASE/40GBASE SR-BiDi QSFP Transceiver, LC, 100m over OM4 MMF

QSFP-100G-SM-SR

100GBASE CWDM4 Lite QSFP Transceiver, 2km over SMF, 10-60C

QSFP-100G-SL4

100GBASE SL4 for up to 30M over OM4 MMF

QSFP-100G-DR-S

100G QSFP28 Transceiver 100GBASE-DR, 500m SMF, duplex, LC

QSFP-100G-FR-S

100G QSFP28 Transceiver 100G-FR, 2km SMF, duplex, LC

QSFP-100G-SR1.2

100G SR1.2 BiDi QSFP Transceiver, LC, 100m OM4 MMF

QSFP28 100G Cables with Integrated Transceivers

QSFP-100G-CU1M

100GBASE-CR4 Passive Copper Cable, 1m

QSFP-100G-CU2M

100GBASE-CR4 Passive Copper Cable, 2m

QSFP-100G-CU3M

100GBASE-CR4 Passive Copper Cable, 3m

QSFP-100G-CU5M

100GBASE-CR4 Passive Copper Cable, 5m

QSFP-100G-AOC1M

100GBASE QSFP Active Optical Cable, 1m

QSFP-100G-AOC2M

100GBASE QSFP Active Optical Cable, 2m

QSFP-100G-AOC3M

100GBASE QSFP Active Optical Cable, 3m

QSFP-100G-AOC5M

100GBASE QSFP Active Optical Cable, 5m

QSFP-100G-AOC7M

100GBASE QSFP Active Optical Cable, 7m

QSFP-100G-AOC10M

100GBASE QSFP Active Optical Cable, 10m

QSFP-100G-AOC15M

100GBASE QSFP Active Optical Cable, 15m

QSFP-100G-AOC20M

100GBASE QSFP Active Optical Cable, 20m

QSFP-100G-AOC25M

100GBASE QSFP Active Optical Cable, 25m

Cisco UCS 9108 100G IFM

11

CONFIGURING the INTELLIGENT FABRIC MODULE (IFM)

Table 4   UCS 9108 100G Supported Transceivers (continued)

Product ID (PID)

Description

QSFP-100G-AOC30M

100GBASE QSFP Active Optical Cable, 30m

12

Cisco UCS 9108 100G IFM

SUPPLEMENTAL MATERIAL

SUPPLEMENTAL MATERIAL

Port Numbering

Each port on the Cisco UCS 9108 100G IFM is numbered. The ports are numbered left to right.

Figure 3 shows how ports are numbered and the table below explains how each port functions.

Figure 3

  Port Numbering of the Cisco UCS 9108 100G IFM

1

Port 1-4 (operate as 100 Gbps QSFP28 fabric 
ports)

2

Port 5-8 (operate as 100 Gbps QSFP28 fabric 
ports)

Fabric Interconnect Compatibility

The Cisco UCS 9108 100G IFM is designed to work with the Cisco UCS 6500/6600 series Fabric Interconnects.

Cisco UCS 9108 100G IFM

13

SUPPLEMENTAL MATERIAL

Connectivity

This section shown the connectivity from the Cisco UCS 9108 100G IFMs to an external Fabric Interconnect 
(FI). 

The connectivity from the IFMs 100G to Fabric Interconnects is shown in Figure 4.

Figure 4

IFMs 100G to Fabric Interconnect Connectivity

= QSFP28 Links

1600G Per X9508 Chassis
100G E2E single-flow
200G Per x210 with 1:1  oversubsription

IFM A-100G  (8 x 100GB) 
IFM B-100G  (8 x 100GB) 

IFM  A

IFM  B

14

Cisco UCS 9108 100G IFM

  
TECHNICAL SPECIFICATIONS

TECHNICAL SPECIFICATIONS

Physical and Environmental Specifications

Table 5    Physical and Environmental Specifications

Description

Specification

Cisco UCS 9108 100G IFM

Dimensions (H x W x D)

1.67 in, x 14.93 in x 11.76 in. (4.2 cm x 37.9 cm x 29.9 cm)

Weight

8.42 lb (3.82 kg)

Temperature, operating

32 to 104°F (0 to 40°C)

Temperature, non-operating

-40 to 158°F (-40 to 70°C)

Humidity (RH), non-condensing

5 to 95%

Altitude

0 to 13,123 ft (0 to 4000 m)

Cisco UCS 9108 100G IFM

15

ACCESSORIES/SPARE PARTS

ACCESSORIES/SPARE PARTS

This section lists the upgrade and service-related parts for the IFM. 

Table 6   Spare Parts

Spare Product ID (PID)

Description

UCSX-RSFAN=

UCS 9508 Rear Slot Fan Spare (IFM and FEM)

16

Cisco UCS 9108 100G IFM

