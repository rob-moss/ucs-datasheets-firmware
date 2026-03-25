# Cisco UCS Fabric Interconnect 9108 100G Spec Sheet

| | |
|---|---|
| **URL Title** | Cisco UCS Fabric Interconnect 9108 100G Spec Sheet |
| **URL** | https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-x-series-modular-system/ucs-fabric-interconnect-9108-100g.pdf |
| **Long URL** |  |
| **HTML Title** |  |
| **Source file** | `ucs-docs-raw/pdf/ucs-fabric-interconnect-9108-100g.pdf` |
| **File type** | PDF |
| **Fetched on** | 2026-03-25 11:35:59 |

---

Spec Sheet

Cisco UCS Fabric 
Interconnect 9108 100G

CISCO SYSTEMS
170 WEST TASMAN DR.
SAN JOSE, CA, 95134
WWW.CISCO.COM

PUBLICATION HISTORY

REV A.14, OCTOBER 30, 2025

 
CONTENTS

OVERVIEW  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
Detailed View . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
LED Indicators   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
FABRIC INTERCONNECT 9108 100G (FIs) STANDARD CAPABILITIES AND FEATURES 8
SUPPORTED FEATURES AND CONFIGURATIONS   . . . . . . . . . . . . . . . . . . . . .  11
CONFIGURING the FABRIC INTERCONNECT   . . . . . . . . . . . . . . . . . . . . . . . .  12
1 SELECT FABRIC INTERCONNECTS   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
2 SOFTWARE LICENSE (INCLUDED)   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
3 CHOOSE TRANSCEIVERS AND CABLES (OPTIONAL)   . . . . . . . . . . . . . . . . . . . . . . . 15
SUPPLEMENTAL MATERIAL  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  22
Cisco UCS X-Series Direct Connectivity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
Connectivity Between M6/M7/M8 Compute Node and UCS Fabric Interconnect 9108 100G  . . . 26
TECHNICAL SPECIFICATIONS  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  29
Physical Dimensions and Specifications   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
Compliance Specifications  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
System Requirements  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31

STEP
STEP
STEP

2

Cisco UCS Fabric Interconnect 9108 100G

OVERVIEW

OVERVIEW

Cisco UCS X-Series Direct transforms the Cisco UCS X-Series Modular System into a self-contained system 
with pair of internal Cisco UCS Fabric Interconnects 9108 100G that integrate each of up to 20 server nodes 
with Cisco unified fabric connectivity, upstream IP and Fibre Channel connectivity, all managed through 
Cisco Intersight or the time-proven Cisco UCS Manager.

The platform supports two- and four-socket compute nodes of which up to eight and four (respectively) can 
populate a chassis. Each node can support up to nine NVMe drives, two M.2 drives, two VICs, and up to six 
GPU accelerators. The platform's capabilities can be extended through the Cisco UCS X-Fabric. With the 
ability to have a second Cisco UCS X9508 Chassis with up to eight compute nodes and up to four UCS 
C-Series rack servers connected to UCS X-Series Direct, it expands the size of a UCS domain to a total of up 
to 20 compute nodes, managed either by Cisco Intersight or Cisco UCS Manager.

The fabric interconnects create a self-contained system connecting IP, storage, and management networks 
with two 100-Gbps connections to each of eight slots in the chassis. Within each compute node, Cisco 
virtual interface cards provide the number and type of I/O devices that you create depending on your 
application.

The fabric interconnects connect upstream to switches or storage appliances with eight 100- Gbps ports 
that can carry 1, 10, 25, 40, and 100 Gigabit Ethernet to upstream switches. these ports can be used to 
connect to a second Cisco UCS X9508 chassis equipped with intelligent fabric modules and to up to four 
C-Series Rack Server, with the primary chassis serving as a single point of connectivity and management for 
the edge location. The Fabric Interconnect can also provide eight Fibre Channel uplink or storage ports (8-, 
16- or 32-Gbps FC) that can connect directly to a FC SAN switch (Cisco MDS or non-Cisco) or an FC storage 
array. 

The Cisco UCS X-Series Direct is designed to shift your thinking from administrative details to business 
outcomes-with infrastructure that is assembled from the cloud, shaped to your workloads, and continuously 
optimized. Now that hardware can think and change like software, you are free to think like tomorrow. This 
brings about immense simplification to edge applications:

Simplify with cloud-operated infrastructure: By shaping system resources to workload 
requirements with Cisco Intersight, you can deliver intelligent visualization, optimization, and 
orchestration to all your applications and infrastructure.

Simplify with an adaptable platform: Edge applications have widely varying requirements. At the 
edge, you can use a single platform that combines the density and efficiency of blade servers with 
the expandability of rack servers for better performance, automation, and efficiency.

Simplify with a system engineered for the future: Embrace emerging technology and reduce risk 
with a modular system engineered to support future generations of processor, accelerator, and 
interconnects with management enabled by a constant stream of new capabilities delivered as 
Software-as-a-Service (SaaS).

The Cisco UCS Fabric Interconnect 9108 100G (Figure 1) is an integrated 1/10/25/40/100 Gigabit Ethernet, 
FCoE, and Fibre Channel switch offering up to 1.6 Tbps throughput and up to 8 ports. The switch has 6 
40/100-Gbps Ethernet ports and 2 unified ports that can support either 40/100-Gbps Ethernet speed per 
port or 32/64/128-Gbps FC speed per port by break-out into 4 8/16/32-Gbps FC ports. The 8 FC ports after 
breakout can either operate as an FC uplink port or as an FC storage port. The switch supports 2 1-Gbps 
speed after breakout and all 8 ports can breakout for 10/25-Gbps Ethernet connectivity. All Ethernet ports 
are capable of supporting FCoE. Beyond the 8 external facing 100G ports, the Fabric Interconnect 9108 
100G also provides eight 100G or thirty-two 25G backplane ethernet ports connectivity towards the X-series 

Cisco UCS Fabric Interconnect 9108 100G

3

■
■
■
OVERVIEW

compute nodes depending on 100G or 25G VIC. The rear-view image shows the ortho-direct connectors that 
will connect to the VIC on the X-series compute node.

The Cisco UCS Fabric Interconnect 9108 100G also has one network management port, one console port for 
setting the initial configuration, and one USB port for saving or loading configurations. 

Figure 1 shows the 8-port FI.

Figure 1

  Cisco UCS Fabric Interconnect 9108 100G.

Front View

Rear View

4

Cisco UCS Fabric Interconnect 9108 100G

Detailed View

The Cisco UCS Fabric Interconnect 9108 100G front view shown in Figure 2.

Figure 2

  Cisco UCS Fabric Interconnect 9108 100G (front view)

Detailed View

1 

Status LEDs:

2

QSFP28 Optical Ports. 

FI Status (top LED)

Fan Status LEDs 1 through 3, with 
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

Figure 3 shows the FI top view characteristics.

Cisco UCS Fabric Interconnect 9108 100G

5

■
■
Detailed View

Figure 3

  Cisco UCS Fabric Interconnect 9108 100G (top view)

1 

Fans (3) which are numbered 1 through 3 
starting with the left fan

4

QSFP28 Optical Ports 5-8

One M.2 mini storage module slot

QSFP28 Optical Ports 1-4

5

-

Ports are arranged in two groups of four 
physical ports. Ports are stacked in vertical 
pairs, with two ports in each vertical port 
stack. 

2

3

6

Ports are arranged in two groups of four 
physical ports. Ports are stacked in vertical 
pairs, with two ports in each vertical port 
stack. 

FI ejector handles, left and right

-

Cisco UCS Fabric Interconnect 9108 100G

LED Indicators

LED Indicators

The LED indicators are described in Table 1 (see Figure 2 on page 5 for LED locations)

Table 1   FI LED States

LED

FI Status

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

Cisco UCS Fabric Interconnect 9108 100G

7

 
FABRIC INTERCONNECT 9108 100G (FIs) STANDARD CAPABILITIES AND FEATURES

FABRIC INTERCONNECT 9108 100G (FIs) STANDARD 
CAPABILITIES AND FEATURES

Network connectivity is provided by a pair of Cisco UCS Fabric Interconnect 9108 100G (FIs). These modules 
carry all network traffic to the Top-of-Rack (ToR) switches. Having a single point of network connectivity 
and control in a system provides deterministic low latency. This, in turn, frees you to place workloads 
without regard to whether the compute nodes are in the same chassis. Each FI features the following:

UCS Fabric Interconnect 9108 100G:

Server ports: Up to 200 Gbps of unified fabric connectivity per compute node with two FIs.

Uplink and connectivity ports: 8x 100-Gbps QSFP28 ports.

The unified fabric carries management, production, and Fibre Channel over Ethernet (FCoE) traffic to the 
fabric interconnects. There, management traffic connects to the Cisco Intersight cloud operations 
platform; FC traffic is passed to native Fibre Channel interfaces through unified ports on the fabric 
interconnects, and production Ethernet traffic is passed upstream to the data center network.

Up to two Fabric Interconnect (FIs) 9108 100G plug into the back of the UCS X9508 chassis.

The Fabric Interconnect 9108 100G monitors and manages chassis components such as fan units, power 
supplies, environmental data, LED status panel, and other chassis resources. The compute node's 
Keyboard-Video-Mouse (KVM) data, Serial over LAN (SoL) data, and Intelligent Platform Management 
Interface (IPMI) data also travel to the FIs for monitoring and management purposes. In order to provide 
redundancy and failover, the FIs are always used in pairs.

There are 8x QSFP28 connectors on a FI to interface with the ToR switch. The FI provides up to 8x 100 
Gbit/s links for the UCS Fabric Interconnect 9108 100G. The links provide the end-to-end interface from a 
compute node in the X9508 X-Series chassis to the connections on a ToR switch. When a compute node is 
inserted into the chassis, the compute node's upper mezzanine card (mLOM) plugs directly into the two FIs 
using two orthogonal connectors (ODs). The X9508 X-Series chassis accommodates two Cisco UCS Fabric 
Interconnects 9108 100G.

Table 2 lists the capabilities and features of the Cisco UCS Fabric Interconnect 9108 100G. 

Table 2   Capabilities and Features  

Capability/Feature

Description

Server data path 
bandwidth

Network data path 
bandwidth

1.6 Tbps for 8 compute nodes

(1x 100 Gbps or 4x25 Gbps per compute-node per UCSX-S9108-100G, for a 
total of 200 Gbps per compute node with dual UCSX-S9108-100G per X9508 
Chassis)

1.6Tbps

8x 100Gbps per UCSX-S9108-100G, with two FI per chassis.

CPU complex

Intel® Denverton Processor (8 core, 2.2GHz, 15W)

DDR4 memory: 16GB max @ 2133 MHz

8

Cisco UCS Fabric Interconnect 9108 100G

■
■
■
■
■
■
FABRIC INTERCONNECT 9108 100G (FIs) STANDARD CAPABILITIES AND FEATURES

Table 2   Capabilities and Features  (continued)

Capability/Feature

Description

Fans

The FI 9108 100G has three dual-rotor on board fans. The air flow direction is 
aligned with chassis air flow direction, which is front to rear. 

The FI 9108 100G Fans have minimum RPM requirements to be compatible 
with the chassis/system main fans. The fans are powered from 
54VDC/48VDC. Fan speed is controlled and monitored by the FI CPU using a 
fan controller IC.

Fibre Channel

Unified Ports

Power Supply

FC + FCoE

2 (1-2)

Power supplied by chassis

Power consumption

237W

 Management

Cisco Intersight software (SaaS, Virtual Appliance and Private Virtual 
Appliance) 

Unified Fabric

Expandability

■ UCS Manager (UCSM) 4.3(4b) or later

Intersight Managed Mode (IMM) 4.3(4) or later

Decreases total cost of ownership (TCO) by reducing the number of 
NICs, HBAs, switches, and cables needed

Support Fibre Channel and Ethernet traffic concurrently in a Unified 
Fabric

Increases flexibility with a range of interconnect solutions, including 
copper Twinax cable for short runs and fiber for long runs

Consumes less power per port than traditional solution

1x Cisco UCS X9508 Chassis with UCS 9108-100G Intelligent Fabric 
Module and up to 8x compute nodes M6/M7/M8 + 4x Cisco UCS C2xx 
M7/M8 Rack Server.

SW version for 2nd chassis and rack server support 6.0(1b) or later

QSFP28-compatible 
ports

Allows all ports to be configured to operate in 40/100 Gigabit Ethernet mode 
with the transceiver options specified for use with

Transceivers

■ QSFP28-compatible ports

The Cisco UCS Fabric Interconnect 9108 100G supports a wide variety of 
1/10/25/40/100 Gigabit Ethernet connectivity options using Cisco 
1/10/25/40/100 Gbps modules. Unified Ports (UP) on the Cisco UCS Fabric 
Interconnect 9108 100G supports 10/25/40G/100G Gigabit Ethernet 
connectivity or a 128G FC-QSFP28 which can breakout into four 8/16/32 
Gigabit Fibre Channel connection. Cisco UCS Fabric Interconnect 9108 100G 
provides flexible uplink port connectivity at 1G/10G/25G/40G/100G via 
Gigabit Ethernet transceivers and cables. Table 3 lists the supported 
transceiver options.

Cisco UCS Fabric Interconnect 9108 100G

9

■
■
■
■
■
■
■
■
FABRIC INTERCONNECT 9108 100G (FIs) STANDARD CAPABILITIES AND FEATURES

Table 2   Capabilities and Features  (continued)

Capability/Feature

Description

Performance

Provides high-speed, low-latency connectivity to the Cisco UCS X-Series 
chassis

Provides approximately 50% reduction in end-to-end system latency 
(latency is less than 1 microseconds)

Lossless Fabric

Provides a reliable, robust foundation for unifying LAN and SAN traffic 
on a single transport

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

10

Cisco UCS Fabric Interconnect 9108 100G

■
■
■
■
■
SUPPORTED FEATURES AND CONFIGURATIONS

SUPPORTED FEATURES AND CONFIGURATIONS

Table 3 lists the supported features and configurations of the Cisco UCS Fabric Interconnect 9108 100G with 
the Cisco UCS X-Series Direct.

Table 3   Supported Features and Configurations 

Capability/Feature

Description

Compute Nodes

The UCS X-Series Direct supports the X210c M6/M7/M8, X410c M7 and X215c 
M8 compute nodes in the primary and secondary chassis.

PCIe Node

Port Usage

Supports a mix of up to four Cisco UCS C-Series Rack servers, either C220 
M7/M8, C240 M7/M8, C225 M8, or C245 M8.

The UCS X-Series Direct supports the X440p PCIe node as well as the UCS 
9416 X-Fabric modules

The UCS Fabric Interconnect 9108 100G has eight QSFP ports. The eight QSFP 
ports can be configured as:

■ Uplink ports

Appliance ports

1, 10, 25, 40, 100 Gbit ports

Number of UCS X-Series 
Chassis

Licensing

■ Unified port 1 + 2 with 32/64/128-Gbps FC speed per port by break-out 

into 4 8/16/32-Gbps FC ports (FC end-host and FC switch mode)

FCoE ports

Overall, up to two UCS X-Series chassis are supported, including X-Direct.

All QSFP ports are enabled by default and included in the perpetual license 
UCSX-S9108-SW.

Cisco UCS Fabric 
Interconnect 9108 100G

Two Cisco UCS Fabric Interconnect 9108 100G are required for production 
operation in the UCS X-Series chassis.

Cisco UCS Fabric Interconnect 9108 100G

11

■
■
■
 
CONFIGURING the FABRIC INTERCONNECT

CONFIGURING the FABRIC INTERCONNECT

Follow these steps to configure the Fabric Interconnect 9108 100G:

STEP 1 SELECT FABRIC INTERCONNECTS, page 13

STEP 2 SOFTWARE LICENSE (INCLUDED), page 14

STEP 3 CHOOSE TRANSCEIVERS AND CABLES (OPTIONAL), page 15

SUPPLEMENTAL MATERIAL on page 22

12

Cisco UCS Fabric Interconnect 9108 100G

■
■
■
■
CONFIGURING the FABRIC INTERCONNECT

STEP 1

SELECT FABRIC INTERCONNECTS

Choose Fabric Interconnect

The available Fabric Interconnects are listed in Table 4. Each FI connects to external ToR using 
8x 100G ports

Table 4   Available Fabric Interconnect

Product ID (PID)

Description

Under UCSX-M6-MLB

UCSX-S9108-100G

UCS X-Series Direct Fabric Interconnect 9108 100G

Under UCSX-M7-MLB

UCSX-S9108-100G

UCS X-Series Direct Fabric Interconnect 9108 100G

Under UCSX-M8-MLB

UCSX-S9108-100G

UCS X-Series Direct Fabric Interconnect 9108 100G

The base Cisco UCS Fabric Interconnect 9108 100G does not include the following components. 
They must be selected during product ordering:

Transceivers

Cables

Warranty Service as part of the overall Cisco UCS X-Series Direct

.

NOTE:  Use the steps on the following pages to configure the FI with the components 
that you want to include.

Cisco UCS Fabric Interconnect 9108 100G

13

■
■
■
CONFIGURING the FABRIC INTERCONNECT

STEP 2 SOFTWARE LICENSE (INCLUDED)

Table 5 shows the Software License Options. This included as a default line item under FI 
ordering PID

.

Table 5   Software License

Product ID (PID)

Description

Software License
UCSX-S9108-SW

Perpetual software license for the Cisco UCS Fabric Interconnect 9108 100G. This 
license activates all the ports and software features of the Cisco UCS Fabric 
Interconnect 9108 100G

14

Cisco UCS Fabric Interconnect 9108 100G

CONFIGURING the FABRIC INTERCONNECT

STEP 3 CHOOSE TRANSCEIVERS AND CABLES (OPTIONAL)

The Cisco UCS Fabric Interconnect 9108 100G supports a wide variety of 1/10/25/40/100 Gigabit Ethernet 
connectivity options using Cisco 1/10/25/40/100 Gbps modules. Unified ports (UP) on the Cisco UCS Fabric 
Interconnect 9108 100G support 10/25/40/100 Gigabit Ethernet connectivity or 32/64/128 Gigabit FC 
connectivity by breakout into 4 8/16/32-Gbps FC ports.

The supported transceivers are for the UCS Fabric Interconnect 9108 100G is listed in Table 6

Table 6   UCS Fabric Interconnect 9108 100G Supported Transceivers  For Uplink Connectivity

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

QSFP-100G-AOC30M

100GBASE QSFP Active Optical Cable, 30m

Cisco UCS Fabric Interconnect 9108 100G

15

CONFIGURING the FABRIC INTERCONNECT

Table 6   UCS Fabric Interconnect 9108 100G Supported Transceivers (continued) For Uplink 

Product ID (PID)

Description

QSFP28 40G Transceivers

QSFP-40G-SR4

40GBASE-SR4 QSFP Transceiver Module with MPO Connector

QSFP-40G-SR4-S

40GBASE-SR4 QSFP Transceiver Module, MPO Conn, Enterprise-Class

QSFP-40G-CSR4

QSFP 4x10GBASE-SR Transceiver Module, MPO, 300M

QSFP-40G-SR-BD

40GBASE-SR-BiDi, duplex MMF (LC)

QSFP 40G Cables

QSFP-H40G-ACU10M

40GBASE-CR4 Active Copper Cable, 10m

QSFP-H40G-AOC2M

40GBASE Active Optical Cable, 2m

QSFP-H40G-AOC3M

40GBASE Active Optical Cable, 3m

QSFP-H40G-AOC5M

40GBASE Active Optical Cable, 5m

QSFP-H40G-CU1M

40GBASE-CR4 Passive Copper Cable, 1m

QSFP-H40G-CU2M

40GBASE-CR4 Passive Copper Cable, 2m

QSFP-H40G-CU3M

40GBASE-CR4 Passive Copper Cable, 3m

QSFP-H40G-CU5M

40GBASE-CR4 Passive Copper Cable, 5m

QSFP28 100G Breakout Cables with Integrated Transceivers

QSFP-4SFP25G-CU1M

100GBASE QSFP to 4xSFP25G passive copper splitter cable, 1M

QSFP-4SFP25G-CU2M

100GBASE QSFP to 4xSFP25G passive copper splitter cable, 2M

QSFP-4SFP25G-CU3M

100GBASE QSFP to 4xSFP25G passive copper splitter cable, 3M

QSFP-4SFP25G-CU5M

100GBASE QSFP to 4xSFP25G passive copper splitter cable, 5M

QSFP-4SFP10G-CU3M

QSFP to 4xSFP10G Passive Copper Splitter Cable, 3m

QSFP-4SFP10G-CU5M

QSFP to 4xSFP10G Passive Copper Splitter Cable, 5m

QSFP-4SFP10G-CU10M

QSFP to 4xSFP10G Passive Copper Splitter Cable, 10m

QSFP-4X10G-AOC3M

40GBASE Active Optical QSFP to 4SFP breakout Cable, 3m

QSFP-4X10G-AOC5M

40GBASE Active Optical QSFP to 4SFP breakout Cable, 5m

QSFP-4X10G-AOC7M

40GBASE Active Optical QSFP to 4SFP breakout Cable, 10m

SFP28 25G Cables with Integrated Transceivers

SFP-25G-SR-S

25GBASE-SR SFP Module

SFP-10/25G-LR-S

10/25GBASE-LR SFP28 Module

SFP-10/25G-CSR-S

Dual Rate 10/25GBASE-CSR SFP Module

16

Cisco UCS Fabric Interconnect 9108 100G

Table 6   UCS Fabric Interconnect 9108 100G Supported Transceivers (continued) For Uplink 

CONFIGURING the FABRIC INTERCONNECT

Product ID (PID)

Description

SFP-25G-SL

SFP-10G-SR

SFP-10G-SR-S

SFP-10G-LR

SFP-10G-LR-S

25GBASE-SR SFP SL Module

10GBASE-SR SFP Module

10GBASE-SR SFP Module, Enterprise-Class

10GBASE-LR SFP Module

10GBASE-LR SFP Module, Enterprise-Class

CVR-QSFP28-SFP25G

100G to SFP25G adapter

CVR-QSFP-SFP10G

QSFP 40G to SFP+ 10G adapter

CVR-QSFP-SFP10G + GLC-TE

100m

DS-SFP-4X32G-SW 

4X 32G Optic SFP+

NOTE:  

The Fabric Interconnect 9108 100G supports 1G optics on ports 7 and 8.

Transceiver modules and cables that are supported on a specific fabric 
interconnect are not always supported on all VIC adapters, I/O modules, or 
fabric extenders that are compatible with that fabric interconnect. Detailed 
compatibility matrices for the transceiver modules are available here: 
https://www.cisco.com/c/en/us/support/interfaces-modules/transceiver-mod
ules/products-devi ce-support-tables-list.html

SFP-10/25G-LR-S and SFP-10/25G-CSR-S are supported only at 25G speed.

S-class transceivers do not support FCoE at 10G and 40G speeds.

There is no link-up when connecting X-Direct (UCSX-S9108-100G) with 
SFP-H25GB-CU5M/QSA28 to some of the 25G ports on N9K (C93180YC-FX). The 
N9K ports without link-up are 1,2,3,5,7,9, while trying all other ports on N9K 
will have link up. Please see 
https://cdetsng.cisco.com/summary/#/defect/CSCwj87577

Caveats

The maximum length of fiber optic runs is limited to 300 meters. This is imposed by our use 
of 802.3X/802.1Qbb Priority Pauses.

NOTE:  For transceiver specifications, see the following link: 
https://tmgmatrix.cisco.com/?npid=6841&npid=6842&npid=6843

You should order enough transceivers and cables to accommodate your maximum 
foreseeable needs.
In order to work with DS-SFP-4x32G-SW you need to have Multimode OM4 fiber, MTP/MPO 
female to 4x LC 8-fiber type-b breakout cable and 8/16/32G FC SW SFP 

Cisco UCS Fabric Interconnect 9108 100G

17

■
■
■
■
■
■
■
■
CONFIGURING the FABRIC INTERCONNECT

The supported transceivers and cables for connectivity from UCS FI 9108 100G to second X-Series chassis 
with UC S9108 100G IFM are listed in Table 7

Table 7   UCS Fabric Interconnect 9108 100G Supported Transceivers and Cables for second chassis 

support

Product ID (PID)

Description

QSFP-100G-SR4-S

100GBASE SR4 QSFP Transceiver, MPO, 100m over OM4 MMF

QSFP-100G-LR4-S

100GBASE LR4 QSFP Transceiver, LC, 10km over SMF

QSFP-100G-SM-SR

100GBASE CWDM4 Lite QSFP Transceiver, 2km over SMF, 10-60C

QSFP-100G-SL4

100GBASE QSFP Short Link Transceivers, 30m reach over OM4 MMF

QSFP-100G-SR1.2

100G SR-BiDi QSFP Transceiver, LC, 100m OM4 MMF

QSFP-40/100-SRBD

100G and 40GBASE SR-BiDi QSFP Transceiver, LC, 100m OM4 MMF

QSFP-100G-DR-S

100GBASE DR QSFP Transceiver, 500m over SMF

QSFP-100G-FR-S

100GBASE-FR1 QSFP Transceiver, 2km over SMF

QSFP-100G-PSM4-S

100GBASE PSM4 QSFP Transceiver, MPO, 500m over SMF

QSFP-100G-CU1M

100GBASE-CR4 Passive Copper Cable, 1-meter

QSFP-100G-CU2M

100GBASE-CR4 Passive Copper Cable, 2-meter

QSFP-100G-CU3M

100GBASE-CR4 Passive Copper Cable, 3-meter

QSFP-100G-CU5M

100GBASE-CR4 Passive Copper Cable, 5-meter

QSFP-100G-AOC2M

100G QSFP Active Optical Cable, 2-meter

QSFP-100G-AOC3M

100G QSFP Active Optical Cable, 3-meter

QSFP-100G-AOC5M

100G QSFP Active Optical Cable, 5-meter

QSFP-100G-AOC7M

100G QSFP Active Optical Cable, 7-meter

QSFP-100G-AOC10M

100G QSFP Active Optical Cable, 10-meter

QSFP-100G-AOC15M

100G QSFP Active Optical Cable, 15-meter

QSFP-100G-AOC20M

100G QSFP Active Optical Cable, 20-meter

QSFP-100G-AOC25M

100G QSFP Active Optical Cable, 25-meter

QSFP-100G-AOC30M

100G QSFP Active Optical Cable, 30-meter

18

Cisco UCS Fabric Interconnect 9108 100G

CONFIGURING the FABRIC INTERCONNECT

The supported transceivers and cables for connectivity from UCS FI 9108 100G to Cisco UCS C-Series Rack 
Servers are listed in Table 8.

Table 8   UCS Fabric Interconnect 9108 100G Supported Transceivers and Cables for rack server support

Product ID (PID)

Description

QSFP-100G-SR4-S (25G 
default rate)

100G QSFP28 SR4, MPO-12 connector, 100m reach on MMF 
(OM3/OM4/OM5), 4x25G optical breakout via MPO12-x4LC external MMF 
cable to SFP-25G-SR-S/SFP-25G-SL/SFP-10/25G-CSR-S

QSFP-100G-SL4 (25G 
default rate)

100G QSFP28 SL4, MPO-12 connector, 30m reach on MMF, 4x25G optical 
breakout via MPO12-x4LC external MMF cable to 
SFP-25G-SR-S/SFP-25G-SL/SFP-10/25G-CSR-S

QSFP-100G-PSM4-S (25G 
default rate)

100G QSFP28 PSM4, MPO-12 connector, 500m reach on SMF, 4x25G optical 
breakout via MPO12-x4LC external SMF cable to SFP-25G-LR-S 

QSFP-40/100G-SRBD

QSFP-100G-SR1.2

40/100G SR BiDi, duplex LC connector, 100m reach on MMF, supports dual 
40/100G operation (100G default rate)

100G SR1.2 BiDi, duplex LC connector, 100m reach on MMF, supports 
breakout to 4x25G, reuses duplex LC MMF infrastructure

QSFP-100G-LR4-S

100G LR4, duplex LC connector, 10km reach on SMF

QSFP-100G-DR-S

100G DR, single-mode fiber, 500m reach

QSFP-100G-FR-S

100G FR, single-mode fiber, 2km reach

QSFP-100G-SM-SR

100G SM SR, single-mode fiber, short reach

QSFP-100G-CU1M

100G Passive Copper Twinax cable, 1 meter length

QSFP-100G-CU2M

100G Passive Copper Twinax cable, 2 meters length

QSFP-100G-CU3M

100G Passive Copper Twinax cable, 3 meters length

QSFP-100G-CU5M

100G Passive Copper Twinax cable, 5 meters length

QSFP-4SFP25G-CU1M

QSFP to 4x SFP25G Passive Copper breakout cable, 1 meter length

QSFP-4SFP25G-CU2M

QSFP to 4x SFP25G Passive Copper breakout cable, 2 meters length

QSFP-4SFP25G-CU3M

QSFP to 4x SFP25G Passive Copper breakout cable, 3 meters length

QSFP-4SFP25G-CU5M

QSFP to 4x SFP25G Passive Copper breakout cable, 5 meters length

QSFP-100G-AOC1M

100G Active Optical Cable (AOC), 1 meter length

QSFP-100G-AOC2M

100G Active Optical Cable (AOC), 2 meters length

QSFP-100G-AOC3M

100G Active Optical Cable (AOC), 3 meters length

QSFP-100G-AOC5M

100G Active Optical Cable (AOC), 5 meters length

QSFP-100G-AOC7M

100G Active Optical Cable (AOC), 7 meters length

QSFP-100G-AOC10M

100G Active Optical Cable (AOC), 10 meters length

Cisco UCS Fabric Interconnect 9108 100G

19

CONFIGURING the FABRIC INTERCONNECT

Table 8   UCS Fabric Interconnect 9108 100G Supported Transceivers and Cables for rack server support

Product ID (PID)

Description

QSFP-100G-AOC15M

100G Active Optical Cable (AOC), 15 meters length

QSFP-100G-AOC20M

100G Active Optical Cable (AOC), 20 meters length

QSFP-100G-AOC25M

100G Active Optical Cable (AOC), 25 meters length

QSFP-100G-AOC30M

100G Active Optical Cable (AOC), 30 meters length

SFP-25G-SR-S

SFP-25G-SL

SFP-25G-CSR-S

SFP-25G-LR-S

25G SFP28 SR, multimode fiber, 100m reach

25G SFP28 SL, multimode fiber, 30m reach

25G SFP28 CSR, multimode fiber, 300m/400m reach

25G SFP28 LR, single-mode fiber, 10km reach

SFP-H25G-CU1M

25G Passive Copper Twinax cable, 1 meter length

SFP-H25G-CU2M

25G Passive Copper Twinax cable, 2 meters length

SFP-H25G-CU3M

25G Passive Copper Twinax cable, 3 meters length

SFP-H25G-CU4M

25G Passive Copper Twinax cable, 4 meters length

SFP-H25G-CU5M

25G Passive Copper Twinax cable, 5 meters length

SFP-25G-AOC1M

25G Active Optical Cable (AOC), 1 meter length

SFP-25G-AOC2M

25G Active Optical Cable (AOC), 2 meters length

SFP-25G-AOC3M

25G Active Optical Cable (AOC), 3 meters length

SFP-25G-AOC4M

25G Active Optical Cable (AOC), 4 meters length

SFP-25G-AOC5M

25G Active Optical Cable (AOC), 5 meters length

SFP-25G-AOC7M

25G Active Optical Cable (AOC), 7 meters length

SFP-25G-AOC10M

25G Active Optical Cable (AOC), 10 meters length

20

Cisco UCS Fabric Interconnect 9108 100G

CONFIGURING the FABRIC INTERCONNECT

NOTE:  

The 100G QSFP transceivers such as QSFP-100G-SR4-S, QSFP-100G-SL4, and 
QSFP-100G-PSM4-S support both QSFP-to-QSFP (Q to Q) and QSFP-to-4xSFP25G 
(Q to 4S) breakout modes using MPO12-x4LC external cables to corresponding 
25G SFP transceivers at the breakout end.

The QSFP-100G-SR1.2 BiDi transceiver allows reuse of existing duplex LC MMF 
infrastructure and supports breakout to 4x25G.

Passive copper cables (CU) are available in various fixed lengths for direct 
attach copper connections.

Active Optical Cables (AOC) provide longer reach and lighter weight compared 
to copper cables, available in multiple lengths.

25G transceivers and cables are designed for connectivity from JP (line card) 
with QSA28 adapters to VIC (server or leaf), supporting smooth migration and 
breakout from 100G QSFP ports.

Cisco UCS Fabric Interconnect 9108 100G

21

■
■
■
■
■
SUPPLEMENTAL MATERIAL

SUPPLEMENTAL MATERIAL

Cisco UCS X-Series Direct Connectivity

The LAN connectivity from the Cisco UCS Fabric Interconnect 9108 100G to the ToR switch is shown in 
Figure 4 and Figure 5

Figure 4

  LAN Connectivity with Cisco UCS Fabric Interconnect 9108 100G and vPC in End-Host mode

Figure 5

  LAN Connectivity with Cisco UCS Fabric Interconnect 9108 100G but without vPC in end-host 
mode

22

Cisco UCS Fabric Interconnect 9108 100G

The SAN connectivity from the Cisco UCS Fabric Interconnect 9108 100G to a Cisco MDS or non-MDS switch is 
shown in Figure 6, Figure 7 and Figure 8

Figure 6

  SAN Connectivity with Cisco UCS Fabric Interconnect 9108 100G and FC end-host or switch 
mode (Cisco MDS)

SUPPLEMENTAL MATERIAL

Figure 7

  SAN Connectivity with Cisco UCS Fabric Interconnect 9108 100G and FC end-host mode 
(non-Cisco MDS)

Cisco UCS Fabric Interconnect 9108 100G

23

SUPPLEMENTAL MATERIAL

Figure 8

  SAN Connectivity with Cisco UCS Fabric Interconnect 9108 100G and FC switch mode 
(direct attached)

24

Cisco UCS Fabric Interconnect 9108 100G

The IP-SAN connectivity from the Cisco UCS Fabric Interconnect 9108 100G is shown in, Figure 9 and 
Figure 10

Figure 9

  IP-SAN Connectivity with Cisco UCS Fabric Interconnect 9108 100G

SUPPLEMENTAL MATERIAL

Figure 10

  IP-SAN Connectivity with Cisco UCS Fabric Interconnect 9108 100G and Appliance Port 
through ToRs in vPC Port Channel configuration

Cisco UCS Fabric Interconnect 9108 100G

25

SUPPLEMENTAL MATERIAL

Connectivity Between M6/M7/M8 Compute Node and UCS Fabric 
Interconnect 9108 100G

Figure 11 and Figure 12 shows the network connectivity from the 25G mLOM out to the Cisco 
UCS Fabric Interconnect 9108 100G.

Figure 11  Dual-VIC Network Connectivity mLOM 25G to FI

26

Cisco UCS Fabric Interconnect 9108 100G

Figure 12  Single-VIC Network Connectivity mLOM 25G to FI

SUPPLEMENTAL MATERIAL

Cisco UCS Fabric Interconnect 9108 100G

27

SUPPLEMENTAL MATERIAL

Figure 13 shows the network connectivity from the 100G mLOM out to the Cisco UCS Fabric 
Interconnect 9108 100G. 

Figure 13  Network Connectivity mLOM 100G to FI

28

Cisco UCS Fabric Interconnect 9108 100G

TECHNICAL SPECIFICATIONS

TECHNICAL SPECIFICATIONS

Physical Dimensions and Specifications

The physical and Environmental specifications for the for the Cisco UCS Fabric Interconnect 9108 100G are 
listed in listed in Table 9

Table 9    Physical and Environmental Specifications

Description

Specification

Cisco UCS Fabric Interconnect 9108 100G

Dimensions (H x W x D)

1.67 in, x 14.93 in x 11.76 in. (4.2 cm x 37.9 cm x 29.9 cm)

Weight

8.42 lb (3.82 kg)

Temperature, operating

50° to 95°F (10 to 35°C)

Temperature, non-operating

-40 to 158°F (-40 to 70°C)

Humidity (RH), non-condensing

5 to 95%

Altitude

0 to 13,123 ft (0 to 4000 m)

Cisco UCS Fabric Interconnect 9108 100G

29

TECHNICAL SPECIFICATIONS

Compliance Specifications

The regulatory standards compliance (safety and EMC) specifications Table 10.

Table 10  The regulatory standards compliance (safety and EMC) specifications

Parameter

Description

Regulatory compliance

Products comply with CE Markings per directives 2004/108/EC and 
2006/108/EC

Safety

■ UL 60950-1

CAN/CSA-C22.2 No. 60950-1

EN 60950-1

IEC 60950-1

AS/NZS 60950-1

■ GB4943

EMC: Emissions

47CFR Part 15 (CFR 47) Class A (FCC Class A)

AS/NZS CISPR22 Class A

EMC: Immunity

CISPR2 2 Class A

EN55022 Class A

ICES003 Class A

VCCI Class A

EN61000-3-2

EN61000-3-3

KN22 Class A

CNS13438 Class A

EN50082-1

EN61000-6-1

EN55024

CISPR24

EN300386

KN 61000-4 Series

30

Cisco UCS Fabric Interconnect 9108 100G

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
■
■
■
■
■
■
■
■
TECHNICAL SPECIFICATIONS

System Requirements

The system requirements are listed in Table 11.

Table 11  System requirements

Item

Requirement

X-Series chassis

Cisco UCS X9508 Chassis for Compute resources

Cisco Intersight or Cisco 
UCS Manager

Cisco Intersight Managed Mode or Cisco UCS Manager for management

Cisco UCS Fabric Interconnect 9108 100G

31

TECHNICAL SPECIFICATIONS

32

Cisco UCS Fabric Interconnect 9108 100G

