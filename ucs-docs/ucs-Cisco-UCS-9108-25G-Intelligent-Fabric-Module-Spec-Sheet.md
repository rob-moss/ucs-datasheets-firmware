# Cisco UCS 9108 25G Intelligent Fabric Module Spec Sheet

| | |
|---|---|
| **URL Title** | Cisco UCS 9108 25G Intelligent Fabric Module Spec Sheet |
| **URL** | https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-x-series-modular-system/9108-25g-specsheet.pdf |
| **Long URL** |  |
| **HTML Title** |  |
| **Source file** | `ucs-docs-raw/pdf/9108-25g-specsheet.pdf` |
| **File type** | PDF |
| **Fetched on** | 2026-04-16 10:50:43 |

---

Spec Sheet

Cisco UCS 9108 25G 
Intelligent Fabric Module
A printed version of this document is only a 
copy and not necessarily the latest version. 
Refer to the following link for the latest 
released version:

https://www.cisco.com/c/en/us/products/servers-
unified-computing/ucs-x-series-modular-system/
datasheet-listing.html

UCSX-I-9108-25G INTELLIGENT FABRIC MODULE (IFM)

CISCO SYSTEMS
170 WEST TASMAN DR.
SAN JOSE, CA, 95134
WWW.CISCO.COM

PUBLICATION HISTORY

REV A.10

FEBRUARY 18, 2025



STEP
STEP

Overview  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
LED Indicators   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
Capabilities and Features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
CONFIGURING the INTELLIGENT FABRIC MODULE  . . . . . . . . . . . . . . . . . . . . . 9
1 VERIFY INTELLIGENT FABRIC MODULE SKU  . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2 CHOOSE TRANSCEIVERS (OPTIONAL)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
SUPPLEMENTAL MATERIAL  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  12
Port Numbering  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
Fabric Interconnect Compatibility . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
Connectivity  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
TECHNICAL SPECIFICATIONS  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  14
Physical and Environmental Specifications   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
ACCESSORIES/SPARE PARTS   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  15

2

Cisco UCS 9108 25G IFM

Overview

Overview

The Cisco UCS 9108 25G Intelligent Fabric Module (IFM) brings the unified fabric into the blade server 
enclosure, providing connectivity between the blade servers and the fabric interconnect, simplifying 
diagnostics, cabling, and management.

The Cisco UCS 9108 25G IFM connects the I/O fabric between the Cisco UCS 6400/6500/6600 series Fabric 
Interconnect and Cisco UCS 64108 Fabric Interconnect and the Cisco UCS X9508 Chassis, enabling a lossless 
and deterministic converged fabric to connect all blades and chassis together. Because the fabric extender 
is similar to a distributed line card, it does not perform any switching and is managed as an extension of the 
fabric interconnects. This approach removes switching from the chassis, reducing overall infrastructure 
complexity and enabling Cisco UCS to scale to many chassis without multiplying the number of switches 
needed, reducing TCO, and allowing all chassis to be managed as a single, highly available management 
domain.

The Cisco UCS 9108 25G IFM also manages the chassis environment (power supply, fans, and blades) in 
conjunction with the fabric interconnect. Therefore, separate chassis-management modules are not 
required.

The IFM plugs into the rear side of the Cisco UCS X9508 chassis. The IFM provides a data path from the 
chassis compute nodes to the Cisco UCS 6400/6500/6600 series Fabric Interconnect. Up to two Intelligent 
Fabric Modules (IFMs) plug into the back of the Cisco UCS X9508 chassis.

The IFMs serve as line cards in the chassis and multiplex data from the compute nodes to the Fabric 
Interconnect (FI). They also monitor and manage chassis components such as fan units, power supplies, 
environmental data, LED status panel, and other chassis resources. The server compute node 
Keyboard-Video-Mouse (KVM) data, Serial over LAN (SoL) data, and Intelligent Platform Management 
Interface (IPMI) data also travel to the IFMs for monitoring and management purposes. In order to provide 
redundancy and failover, the IFMs are always used in pairs.

There are 8 x SFP28 external connectors on an IFM to interface with a FI 6400/6500/6600 series Fabric 
Interconnect. The IFM internally provides 4 x 25 Gbps connections towards each UCS X210c Compute Node 
in the Cisco X9508 chassis.

When a compute node is inserted into the chassis, the compute node’s mezzanine card (mLOM) connects to 
the IFMs using orthogonal direct connectors. Figure 1 shows the IFM front view characteristics.

Cisco UCS 9108 25G IFM

3

Overview

Figure 1

  Cisco UCS 9108 25G IFM (front view)

7

8

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

6

5

1 

IFM status LED

Fan #1 - #3 status LEDs

Reset button

SFP28 ports 1 - 4 (25 Gbps per port)

2

3

4

4

5

6

7

8

SFP28 ports 5 - 8 (25 Gbps per port)

Ejector handle

Link/port status LED (one per port)

Port activity LED (one per port)

Cisco UCS 9108 25G IFM

 
Figure 2

  Cisco UCS 9108 25G IFM (top view)

1

2

3

Overview

7

4

5

6

5

1 

Fan #1

2

3

4

Fan #2

Fan #3

Mini storage connector

5

6

7

-

Ejector handle

Cisco switch ASIC

CPU 
(Intel Denverton, 4-core, 2.1 GHz)

-

Cisco UCS 9108 25G IFM

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

FAN status LED #  
1, 2, 3

SFP Port LED status 
1 LED per port per 
color

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

Cisco UCS 9108 25G IFM

 
Capabilities and Features

Capabilities and Features

Table 2 lists the capabilities and features of the Cisco UCS 9108 25G Intelligent Fabric Module. Details 
about how to configure the IFM for a particular feature or capability are provided in CONFIGURING the 
INTELLIGENT FABRIC MODULE on page 9. 

Table 2   Capabilities and Features  

Capability/Feature

Description

Server data path 
bandwidth

800 Gb/s for 8 compute nodes

(4 x 25Gb/s lanes per compute node, for a total of 100 Gb/s per compute 
node)

Network data path 
bandwidth

200Gb/s

25 Gb/s per port x 8 SFP28 ports

CPU complex

Intel Atom® Processor C3558 (4 core, 2.1GHz, 15W)

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

SFP28-compatible ports

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

Allows the 8 fixed ports to operate in 25 Gigabit Ethernet mode with the 
transceiver options specified for use with SFP28-compatible ports in Table 4 
on page 11. The SFP28 ports on the IFM are bound to a port-channel towards 
the fabric-interconnect and any number of links between 1 thru 8 could be 
active on this port-channel between FI and IFM.

Cisco UCS 9108 25G IFM

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

The Cisco UCS 9108 25G IFM supports a 25 Gigabit Ethernet connectivity 
options using Cisco 25 Gbps modules.

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

Cisco UCS 9108 25G IFM

■
■
■
■
CONFIGURING the INTELLIGENT FABRIC MODULE

CONFIGURING the INTELLIGENT FABRIC MODULE

Follow these steps to configure the Cisco UCS 9108 25G IFM:

STEP 1 VERIFY INTELLIGENT FABRIC MODULE SKU, page 10

STEP 2 CHOOSE TRANSCEIVERS (OPTIONAL), page 11

 The supported transceivers are for the UCS 9108 25G IFM are listed in Table 4., page 11

Cisco UCS 9108 25G IFM

9

■
■
■
CONFIGURING the INTELLIGENT FABRIC MODULE

STEP 1

VERIFY INTELLIGENT FABRIC MODULE SKU

Verify the product ID (PID) of the IFM as shown in Table 3.

Table 3   Available Intelligent Fabric Modules 

Product ID (PID)

Description

Number of 
25 GbE/FCoE 
Ports to ToR

Number of Internal 
GbE/FCoE Ports 

Total Chassis 
I/O per IFM

M6

UCSX-I-9108-25G

M7

UCSX-I-9108-25G-D

UCS 9108 25G IFM for 
X9508 chassis

UCS 9108 25G IFM for 
X9508 chassis

8

8

32

32

2 Tbps

2 Tbps

NOTE:  Use the steps on the following pages to order the desired 
Intelligent Fabric Module with the components that you want configured 
in your order.

10

Cisco UCS 9108 25G IFM

CONFIGURING the INTELLIGENT FABRIC MODULE

STEP 2 CHOOSE TRANSCEIVERS (OPTIONAL)

The Cisco UCS 9108 25G IFM supports a a wide variety of 25 Gigabit Ethernet connectivity 
options using Cisco 25 Gbps modules.

Choose Transceivers

The supported transceivers are for the UCS 9108 25G IFM are listed in Table 4.

Table 4   UCS 9108 25G Supported Transceivers 

Product ID (PID)

Description

 SFP28 25-Gbps Transceivers

SFP-25G-SR-S

25GBASE-SR SFP+, 850nm, MMF, 300m, S-Clas

SFP-10/25G-LR-S

10/25GBASE-LR SFP28 Module for SMF

SFP-10/25G-CSR-S

Dual-rate 10/25GBASE-CSR SFP module

SFP-25G-SL

25GBASE-SL SFP module

SFP28 25G Copper Cables with Integrated Transceivers

SFP-H25G-CU1M

25GBASE-CU SFP28 Cable 1 Meter

SFP-H25G-CU2M

25GBASE-CU SFP28 Cable 2 Meter

SFP-H25G-CU3M

25GBASE-CU SFP28 Cable 3 Meter

SFP-H25G-CU4M

25GBASE-CU SFP28 Cable 4 Meter

SFP-H25G-CU5M

25GBASE-CU SFP28 Cable 5 Meter

SFP-25G-AOC1M

25GBASE Active Optical SFP28 Cable, 1M

SFP-25G-AOC2M

25GBASE Active Optical SFP28 Cable, 2M

SFP-25G-AOC3M

25GBASE Active Optical SFP28 Cable, 3M

SFP-25G-AOC4M

25GBASE Active Optical SFP28 Cable, 4M

SFP-25G-AOC5M

25GBASE Active Optical SFP28 Cable, 5M

SFP-25G-AOC7M

25GBASE Active Optical SFP28 Cable, 7M

SFP-25G-AOC10M

25GBASE Active Optical SFP28 Cable, 10M

QSFP 100GBASE

QSFP-4SFP25G-CU1M

QSFP-4SFP25G-CU2M
QSFP-4SFP25G-CU3M
QSFP-4SFP25G-CU5M

100GBASE QSFP to 4xSFP25G passive copper splitter cable, 1M
100GBASE QSFP to 4xSFP25G passive copper splitter cable, 2M
100GBASE QSFP to 4xSFP25G passive copper splitter cable, 3M
100GBASE QSFP to 4xSFP25G passive copper splitter cable, 5M

Cisco UCS 9108 25G IFM

11

SUPPLEMENTAL MATERIAL

SUPPLEMENTAL MATERIAL

Port Numbering

Each port on the Cisco UCS 9108 25G IFM is numbered. The ports are numbered left to right.

Figure 3 shows how ports are numbered and the table below explains how each port functions.

Figure 3

  Port Numbering of the Cisco UCS 9108 25G IFM

1

2

3

UCSBX-I-9108-25G

1

2

3

4

1

5

6

7

8

2

1

Port 1-4 (operate as 25 Gbps SFP28 fabric 
ports)

2

Port 5-8 (operate as 25 Gbps SFP28 fabric ports)

Fabric Interconnect Compatibility

The Cisco UCS 9108 25G IFM is designed to work with both the Cisco UCS 6400/6500/6600 series and Cisco 
UCS 64108 Fabric Interconnects only at 25 Gbps

12

Cisco UCS 9108 25G IFM

SUPPLEMENTAL MATERIAL

Connectivity

This section shown the connectivity from the Cisco UCS 9108 25G IFM to an external Fabric Interconnect 
(FI).

The connectivity from the IFMs to a 6400 series Fabric Interconnect is shown in Figure 4.

Figure 4

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

Cisco UCS 9108 25G IFM

13

  
TECHNICAL SPECIFICATIONS

TECHNICAL SPECIFICATIONS

Physical and Environmental Specifications

Table 5    Physical and Environmental Specifications

Description

Specification

Cisco UCS 9108 25G IFM

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

14

Cisco UCS 9108 25G IFM

ACCESSORIES/SPARE PARTS

ACCESSORIES/SPARE PARTS

This section lists the upgrade and service-related parts for the IFM. 

Table 6   Spare Parts

Spare Product ID (PID)

Description

UCSX-RSFAN=

UCS 9508 Rear Slot Fan Spare (IFM and FEM)

Cisco UCS 9108 25G IFM

15

ACCESSORIES/SPARE PARTS

16

Cisco UCS 9108 25G IFM

