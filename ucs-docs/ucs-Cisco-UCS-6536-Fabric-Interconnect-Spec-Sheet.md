# Cisco UCS 6536 Fabric Interconnect Spec Sheet

| | |
|---|---|
| **URL Title** | Cisco UCS 6536 Fabric Interconnect Spec Sheet |
| **URL** | https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-x-series-modular-system/cisco-ucs-6536-fabric-interconnect-spec-sheet.pdf |
| **Long URL** |  |
| **HTML Title** |  |
| **Source file** | `ucs-docs-raw/pdf/cisco-ucs-6536-fabric-interconnect-spec-sheet.pdf` |
| **File type** | PDF |
| **Fetched on** | 2026-04-13 13:35:48 |

---

Spec Sheet

Cisco UCS 6536
Fabric Interconnect

 (FI)

CISCO UCS 6536 FABRIC INTERCONNECT

CISCO SYSTEMS
170 WEST TASMAN DR.
SAN JOSE, CA, 95134
WWW.CISCO.COM

PUBLICATION HISTORY

REV A.26

JANUARY 30, 2026

CONTENTS

STEP
STEP
STEP
STEP
STEP
STEP
STEP
STEP
STEP

Overview  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
Cisco UCS 6536 Fabric Interconnect   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
Detailed Front View  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .3
Power Supply LEDs  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
Management Port LEDs  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
Beacon and System Status LEDs   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
L1/L2 Port LEDs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
Detailed Rear View   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .6
Rear LED Indicators   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .7
System Environment LED  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
Ethernet Port (ports 1—36) LEDs  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
Cisco UCS 6536 Fabric Interconnect Capabilities And Features  . . . . . . . . . . . 8
CONFIGURING the FABRIC INTERCONNECT   . . . . . . . . . . . . . . . . . . . . . . . .  10
1 CHOOSE FABRIC INTERCONNECT SKU . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2 SOFTWARE IMAGE OPTIONS (INCLUDED)   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
3 SOFTWARE LICENSE (INCLUDED)   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
4 POWER SUPPLIES (INCLUDED)   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
5 SELECT AC POWER CORDS   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
6 CHOOSE TRANSCEIVERS AND CABLE OPTIONS (OPTIONAL)  . . . . . . . . . . . . . . . . . . 18
7 CHOOSE QSFP CABLE OPTIONS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
8 ACCESSORY KIT (INCLUDED)   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
9 FAN MODULE (INCLUDED)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
6536 FI Fan Module   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
10 CHOOSE SERVICE AND SUPPORT LEVEL   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
SUPPLEMENTAL MATERIAL  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  33
Cisco UCS 6536 FI Port Numbering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
Cisco UCS 6536 FI Supported Speeds   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
Connectivity  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
9508 Chassis Server Connectivity   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
5108 Blade Chassis Server Connectivity   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
C-Series Rack-Mounted Server Connectivity   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
FI 6536 Fibre channel connectivity   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
UCS 6536 FI Break Out Connectivity   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
UCS 5108 and X9508 Chassis Connection Types   . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
TECHNICAL SPECIFICATIONS (s)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  46
Physical and Environmental Specifications   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46

STEP

Cisco UCS 6500 Series Fabric Interconnect

1

Overview

Overview 

The Cisco 6536 Fabric Interconnects are a core part of the Cisco Unified Computing System, providing both 
network connectivity and management capabilities for the system. The Cisco 6536 offer line-rate, 
low-latency, lossless 10/25/40/100 Gigabit Ethernet, Fibre Channel over Ethernet (FCoE), and Fibre 
Channel functions.

The Cisco UCS 6536 Fabric Interconnect provide the management and communication backbone for the 
Cisco UCS X-Series compute nodes, UCS X9508 X-series chassis, UCS B-Series Blade Servers, UCS 5108 
B-Series Server Chassis and UCS C-Series Rack Servers. All servers attached to a Cisco UCS 6536 Fabric 
Interconnect become part of a single, highly available management domain. In addition, by supporting a 
unified fabric, Cisco UCS 6536 Fabric Interconnect provides both the LAN and SAN connectivity for all 
servers within its domain.

From a networking perspective, the Cisco UCS 6536 uses a cut-through architecture, supporting 
deterministic, low-latency, line-rate 10/25/40/100 Gigabit Ethernet ports, a switching capacity of 7.42 
Tbps per FI and 14.84 Tbps per unified fabric domain, independent of packet size and enabled services. It 
enables 1600Gbps bandwidth per X9508 chassis per domain with a X9108-IFM-100G in addition to enabling 
end-to-end 100G ethernet and 200G aggregate bandwidth per X210c compute node. With X9108-IFM-25G 
and IOM 2408, it enables 400Gbps bandwidth per chassis per FI domain. The product family supports Cisco 
low-latency, lossless 10/25/40/100 Gigabit Ethernet unified network fabric capabilities, which increase the 
reliability, efficiency, and scalability of Ethernet networks. The fabric interconnect supports multiple 
traffic classes over a lossless Ethernet fabric from the server through the fabric interconnect. Significant 
TCO savings come from Cisco's unified fabric design in which Network Interface Cards (NICs), Host Bus 
Adapters (HBAs), cables, and switches can be consolidated.

Cisco UCS 6536 Fabric Interconnect

1

Cisco UCS 6536 Fabric Interconnect

Cisco UCS 6536 Fabric Interconnect

The Cisco UCS 6536 36-Port Fabric Interconnect (Figure 1) is a One-Rack-Unit (1RU) 10/25/40/100 Gigabit 
Ethernet, FCoE, and Fibre Channel switch offering up to 7.42 Tbps throughput and up to 36 ports. The 
switch has 32 40/100-Gbps Ethernet ports and 4 unified ports that can support 40/100-Gbps Ethernet ports 
or 16 Fiber Channel ports after break-out at 8/16/32-Gbps FC speeds. The 16 FC ports after breakout can 
either operate as an FC uplink port or as an FC storage port. The switch supports 2 1-Gbps speed after 
breakout and all 36 ports can breakout for 10/25-Gbps Ethernet connectivity. All Ethernet ports are capable 
of supporting FCoE.

The Cisco UCS 6536 Fabric Interconnect also has one network management port, one console port for 
setting the initial configuration, and one USB port for saving or loading configurations. The FI also includes 
L1/L2 ports for connecting two fabric interconnects for high availability.

The 36-port chassis is shown in Figure 1.

Figure 1

  Cisco UCS Fabric Interconnect 6536 (1RU)

Front View

Rear View

2

Cisco UCS 6536 Fabric Interconnect

Cisco UCS 6536 Fabric Interconnect

Detailed Front View

The Cisco UCS 6536 front view shown in Figure 2.

Figure 2

  Front View of 6536

3

4

5

6

7

8

9

4
5
3
0
4
5

1

2

1

1

3

5

7

9

AC/DC power supplies power supply 
modules (1 or 2)

Layer 2 (L2) Ethernet port, 10/100/1000 Mb 
autonegotiating.

Supports high availability (HA) or clustering

Ethernet network management port (RJ45), 
10/100/1000Mb autonegotiating

USB 3.0/2.0 port

Supports booting the system and 
downloading scripts.

Status (STS) LED

2

4

6

8

-

Six fan modules (hot swappable)

Layer 1 (L1) Ethernet port, 10/100/1000Mb 
autonegotiating.

Supports high availability (HA) or clustering.

RS-232 Serial Console port (RJ45 connector), 
9600 baud.

Beacon (BCN) LED

-

The front LED indicators are described in the following sections

Cisco UCS 6536 Fabric Interconnect

3

Cisco UCS 6536 Fabric Interconnect

Power Supply LEDs

The power supply LEDs are located on the left front portion of the power supply. Combinations of states 

indicated by the Power On (

)and Error (

)LEDs indicate the status for the module as shown in Table 1

Table 1   Power Supply LED States

Power on LED

Error LED 

Status

Green

Flashing green

Off

Green

Off

Off

Off

Flashing 
amber

Power supply is on and outputting power to the switch.

Power supply is connected to a power source but not outputting power 
to the switch—power supply might not be installed in the chassis.

Power supply is not receiving power.

Power supply warning—possibly one of the following conditions:

■ High voltage

■ High power

Low voltage

Power supply installed in chassis but not connected to a power 
source

Slow power supply fan

Flashing green

Amber

Power supply failure—possibly one of the following conditions:

■ Over voltage

■ Over current

■ Over temperature

Power supply fan failure

4

Cisco UCS 6536 Fabric Interconnect

■
■
■
■
Management Port LEDs

The management port LED states (see Figure 2 on page 3) are shown in Table 2.

Cisco UCS 6536 Fabric Interconnect

Table 2   Management Port LED States

LED Position

LED State

Description

Left

Off

No link

Solid green

Physical link

Right

Off

No activity

Blinking green

Activity

Beacon and System Status LEDs

The beacon and system status LED states (see Figure 2 on page 3) are shown in Table 3.

Table 3   Beacon and System Status LED States

LED

Location

Function

Color

State

Description

Beacon LED

Front 
and rear

Identify 
selected 
chassis

System 
status LED

Front 
and rear

System 
power/health 
during boot up 
and run time

Blue

Green

Amber

Red

Solid on 

Chassis is selected

Off

Chassis is not selected

Solid on

Normal operation

Off

On

System is powered off

System fault

Solid on

Power shut down by software

Blinking

Secure boot validation has failed

L1/L2 Port LEDs

The L1/L2 port LED states (see Figure 4 on page 7) are shown in Table 4.

Table 4   L1/L2 Port LED States

LED Position

LED State

Description

Left

Off

No link

Solid green

Physical link

Right

Off

No activity

Blinking green

Activity

Cisco UCS 6536 Fabric Interconnect

5

Cisco UCS 6536 Fabric Interconnect

Detailed Rear View

Figure 3 is an overall rear view of the Cisco UCS 6536 Fabric Interconnect.

Figure 3

  6536 36-port Fabric Interconnect Chassis Overall Rear View

11

2

3

4

1

Ports 1-8

2

Ports 9-10

40/100 Gbps Ethernet or FCoE ports 
only 

10/25 Gbps Ethernet via breakout, 
QSA or QSA28

1 Gbps Ethernet via QSA

40/100 Gbps Ethernet or FCoE ports only

10/25 Gbps Ethernet via breakout, QSA or 
QSA28

3

Ports 11-32

4

Unified 33-36

40/100 Gbps Ethernet or FCoE ports 
only 

10/25 Gbps Ethernet via breakout or 
QSA28

16 x 8/16/32G FC port via breakout

10/25/40/100 Gbps Ethernet or FCoE

10/25 Gbps Ethernet via breakout, QSA or 
QSA28

NOTE:  Breakout is supported on all 36 ports and after breakout the UCS 6536 Fabric 
Interconnect can support a maximum of 128 server ports. There is also support for 
QSA and QSA-28 to support 1G/10G/25G speeds without using a breakout cable. In 
terms of rack-server connectivity with FI 6536, 25G/40G/100G ethernet for 
direct-connect rack-servers, 25G ethernet for rack-server with 93180YC-FX3 FEX, 
and 10G ethernet for rack-server with FEX 2348 UPQ are supported. Note that the 
1G/10G ethernet are primarily for FI uplink connectivity

6

Cisco UCS 6536 Fabric Interconnect

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
Cisco UCS 6536 Fabric Interconnect

Rear LED Indicators

The rear LED indicators are described in the following sections

System Environment LED

The system environment LED is located on the left rear of the chassis (see Figure 3 on page 6). The LED 
states are shown in Table 5.

Table 5   System Environment LED States

LED State

Description

Solid Amber

Minor fan alarm (one fan missing or failure

Solid red

Major fan alarm (two more fans missing or failed, or fan direction mismatch)

Ethernet Port (ports 1—36) LEDs

Figure 4 is an detailed view of one of the 40/100 Gbps Ethernet or FCoE ports and its LEDs.

Figure 4

  Ethernet Port LEDs (ports 1-36)

33

34

Upper port LED

Lower port LED

The port 1—36 LED states are shown in Table 6.

Table 6   Port 1 to 36 LED States

LED Position

LED State

Description

Left

Off

No link

Solid green

Physical link

Right

Off

No activity

Blinking green

Activity

Cisco UCS 6536 Fabric Interconnect

7

Cisco UCS 6536 Fabric Interconnect Capabilities And Features

Cisco UCS 6536 Fabric Interconnect Capabilities And 
Features

Table 7 lists the capabilities and features of the Cisco UCS 6536 Fabric Interconnect. Details about how to 
configure this Fabric Interconnect series for a particular feature or capability are provided in CONFIGURING 
the FABRIC INTERCONNECT on page 10. 

Table 7   Capabilities and Features  

Capability/Feature

Cisco UCS 6536 (36 Ports)

Chassis

Throughput

Fan Modules

Unified Ports

Power Supply

1RU 36-port Fabric Interconnect

7.42 Tbps switching performance

Six variable speed fans

4 (33-36)

Two Power Supplies (AC or DC)

Management by Cisco 
Intersight

Allows all elements connected to the interconnects to participate in a 
single, highly available management domain

Unified Fabric

Fabric Extender 
Architecture

Decreases total cost of ownership (TCO) by reducing the number of 
NICs, HBAs, switches, and cables needed

Support Fibre Channel and Ethernet traffic concurrently in a Unified 
Fabric

Increases flexibility with a range of interconnect solutions, including 
copper Twinax cable for short runs and fiber for long runs

Consumes less power per port than traditional solution

Scales to 20 chassis without adding complexity by eliminating the need 
for dedicated chassis management and blade switches and by reducing 
the number of cables needed

Provides deterministic latency for optimized application performance

QSFP28-compatible 
Ports

Allows all ports to be configured to operate in 40/100 Gigabit Ethernet 
mode with the transceiver options specified for use with 
QSFP28-compatible ports (see Table 14 on page 18).

Transceivers

The Cisco UCS 6536 series FIs support a wide variety of 10/25/40/100 
Gigabit Ethernet connectivity options using Cisco 10/25/40/100 Gbps 
modules. Unified Ports (UP) on the Cisco UCS 6536 support 10/25/40G/100G 
Gigabit Ethernet connectivity or a 128G FC-QSFP28 which can breakout into 
four 8/16/32 Gigabit Fibre Channel connection. Cisco UCS 6536 provides 
flexible uplink port connectivity at 1G/10G/25G/40G/100G via Gigabit 
Ethernet transceivers and cables. Table 3 lists the supported transceiver 
options. 

Front-to-Back Cooling

Fan side intake, port side exhaust

8

Cisco UCS 6536 Fabric Interconnect

■
■
■
■
■
■
Cisco UCS 6536 Fabric Interconnect Capabilities And Features

Table 7   Capabilities and Features  (continued)

Capability/Feature

Cisco UCS 6536 (36 Ports)

Redundant 
hot-swappable fans and 
power supplies

■ Helps enable high availability in multiple configurations

Increases serviceability

Provides uninterrupted service during maintenance

Rear Ports

Performance

Helps keep cable lengths short and efficient

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

Helps enable consistent and coherent quality of service (QoS) throughout 
the system

Cisco UCS 6536 Fabric Interconnect

9

■
■
■
■
■
■
CONFIGURING the FABRIC INTERCONNECT

CONFIGURING the FABRIC INTERCONNECT

Follow these steps to configure the Cisco UCS 6536 Fabric Interconnect:

STEP 1 CHOOSE FABRIC INTERCONNECT SKU, page 11

STEP 2 SOFTWARE IMAGE OPTIONS (INCLUDED), page 12

STEP 3 SOFTWARE LICENSE (INCLUDED), page 13

STEP 4 POWER SUPPLIES (INCLUDED), page 14

STEP 5 SELECT AC POWER CORDS, page 15

STEP 6 CHOOSE TRANSCEIVERS AND CABLE OPTIONS (OPTIONAL), page 18

STEP 7 CHOOSE QSFP CABLE OPTIONS, page 20

STEP 8 ACCESSORY KIT (INCLUDED), page 23

STEP 9 FAN MODULE (INCLUDED), page 24

STEP 10 CHOOSE SERVICE AND SUPPORT LEVEL, page 25

10

Cisco UCS 6536 Fabric Interconnect

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
CONFIGURING the FABRIC INTERCONNECT

STEP 1

CHOOSE FABRIC INTERCONNECT SKU

Select the product ID (PID) of the 6536 Fabric Interconnects as shown in Table 8.

NOTE:  When ordering Cisco UCS Fabric Interconnect 6536, the PIDs with “-D” 
suffix are ordering PIDs to be used with UCS M7 series of servers and the PIDs 
without “-D” are for the previous UCS M5/M6 generation of servers. There is no 
difference in functionality and operation of FI with and without “-D”.

Table 8   PID of the Base 6536 Fabric Interconnects 

Product ID (PID)

Description

UCSX-FI-6536-U

Standalone FI ordering PID, Fabric Interconnect 6536 for IMM

UCSX-FI-6536-D-U

UCS-FI-6536-U

(Can also configure under X-series UCSX-M6-MLB)
Standalone FI ordering PID, Fabric Interconnect 6536 for IMM

(Can also configure under X-series UCSX-M7-MLB)
Standalone FI ordering PID, Fabric Interconnect 6536 for UCSM

UCS-FI-6536-D-U

Standalone FI ordering PID, Fabric Interconnect 6536 for UCSM

The base Cisco UCS 6536 Fabric Interconnect do not include the following components. They 
must be selected during product ordering:

Transceivers

Cables

Power cords

Warranty Service

NOTE:  Use the steps on the following pages to configure the FI with the 
components that you want to include.

Table 9   Cisco UCS FI 6536 supported IFM, IOM, FEX, VIC, and servers

Item

Chassis

Supported Chassis, IFM, IOM, FEX, VIC, Servers

UCSX-9508 and UCSB-5108

Intelligent Fabric Module

UCSX-9108-25G, UCSX-9108-100G

I/O Module

IOM 2304v1/v2, IOM 2408

Fabric Extender

N9K-C93180YC-FX3 in FEX mode, Nexus 2348UPQ

I/O Adapter

Servers

VIC 1300 series, VIC 1400/14000 series, VIC 15000 series

X-Series M6/M7, B-Series M4/M5/M6, C-Series M4/M5/M6/M7, S-series M5

Cisco UCS 6536 Fabric Interconnect

11

■
■
■
■
CONFIGURING the FABRIC INTERCONNECT

STEP 2 SOFTWARE IMAGE OPTIONS (INCLUDED)

Table 10 shows the Software Image Options. this included as a default line item under 
standalone FI ordering PID

Table 10  Software Image Options 

Product ID (PID)

Description

N10-MGT018

UCS Manager v4.2 and Intersight Managed Mode v4.2

12

Cisco UCS 6536 Fabric Interconnect

CONFIGURING the FABRIC INTERCONNECT

STEP 3 SOFTWARE LICENSE (INCLUDED)

Table 11 shows the Software License Options. This included as a default line item under 
standalone FI ordering PID

.

Table 11  Software License

Product ID (PID)

Description

Software License
UCS-FI-6500-SW

Perpetual software license for the 6500 series Fabric Interconnect. This license 
activates all the ports and software features of 6500 series Fabric Interconnect

Cisco UCS 6536 Fabric Interconnect

13

CONFIGURING the FABRIC INTERCONNECT

STEP 4 POWER SUPPLIES (INCLUDED)

Table 12 shows the Supported 6536 FI Power Supplies. This included as a default line item under 
standalone FI ordering PID

Table 12  Power Supplies

Product ID (PID)

Description

UCS-PSU-6536-AC

UCS 6536 Power Supply/100-240VAC (1100 W)

UCS-PSU-6536-AC=

Spare, UCS 6536 Power Supply/100-240VAC (1100 W)

UCS-PSU-6536-AC-D

UCS 6536 Power Supply/100-240VAC (1100 W)

UCS-PSU-6536-AC-D=

Spare, UCS 6536 Power Supply/100-240VAC (1100 W)

14

Cisco UCS 6536 Fabric Interconnect

 
CONFIGURING the FABRIC INTERCONNECT

STEP 5 SELECT AC POWER CORDS

Select the appropriate AC power cords listed in Table 13. You must select two identical power 
cords. If you select the option R2XX-DMYMPWRCORD, no power cord is shipped with the server.

Table 13  Available Power Cords  

Product ID (PID)

PID Description

Images

NO-POWER-CORD

CAB-AC-L620-C13

ECO friendly green option, no 
power cable will be shipped

Not applicable

AC Power Cord, NEMA L6-20 - C13, 
2M/6.5ft

CAB-250V-10A-AR

Power Cord, 250V, 10A, Argentina

 2500 mm

Cordset rating: 10 A, 250/500 V MAX
Length: 8.2 ft

Plug:
EL 219
(IRAM 2073)

Connector:
EL 701
 (IEC60320/C13)

1
7
5
6
8
1

CAB-250V-10A-BR

Power Cord - 250V, 10A - Brazil

CAB-9K10A-AU

Power Cord, 250VAC 10A 3112 Plug, 
Australia

CAB-250V-10A-CN

AC Power Cord - 250V, 10A - PRC

Cordset rating: 10 A, 250 V/500 V MAX
Length: 2500mm

Plug:
EL 210
(BS 1363A) 13 AMP fuse

Connector:
EL 701C
(EN 60320/C15)

0
8
5
6
8
1

CAB-9K10A-EU

Power Cord, 250VAC 10A CEE 7/7 
Plug, EU

Cisco UCS 6536 Fabric Interconnect

Plug:
M2511

Cordset rating: 10A/16 A, 250 V
Length: 8 ft 2 in. (2.5 m)

Connector:
VSCC15

6
7
5
6
8
1

15

CONFIGURING the FABRIC INTERCONNECT

Table 13  Available Power Cords  (continued)

Product ID (PID)

PID Description

Images

CAB-250V-10A-ID

Power Cord, 250V, 10A, India

CAB-IND-10A

10A Power cable for India

CAB-250V-10A-IS

Power Cord, 250V, 10A, Israel

CAB-9K10A-IT

Power Cord, 250VAC 10A CEI 
23-16/VII Plug, Italy

CAB-9K10A-SW

Power Cord, 250VAC 10A MP232 
Plug, Switzerland

CAB-9K10A-UK

Power Cord, 250VAC 10A BS1363 
Plug (13 A fuse), UK

CAB-C13-C14-2M 

CABASY,WIRE,JUMPER CORD, PWR, 
2 Meter, C13/C14,10A/250V

Plug:
EL 208

O
V
E

Cordset rating 16A, 250V
(2500mm)

Connector:
EL 701

0
9
4
7
8
1

EL-212
16A
250V

Plug:
EL 212
(SI-32)

Cordset rating 10A, 250V/500V MAX
(2500 mm) 

Connector:
EL 701B
 (IEC60320/C13)

Cordset rating: 10 A, 250 V
Length: 8 ft 2 in. (2.5 m)

Plug: 
I/3G
(CEI 23-16)

Connector
 C15M
(EN60320/C15 )

Cordset rating: 10 A, 250 V
Length: 8 ft. 2 in (2.5 m)

Plug:
MP232-R

Connector:
IEC 60320 C15

Cordset rating: 10 A, 250 V/500 V MAX
Length: 2500mm

Plug:
EL 210
(BS 1363A) 13 AMP fuse

Connector:
EL 701C
(EN 60320/C15)

4
7
5
6
8
1

5
7
5
6
8
1

8
7
5
6
8
1

0
8
5
6
8
1

16

Cisco UCS 6536 Fabric Interconnect

 
CONFIGURING the FABRIC INTERCONNECT

Table 13  Available Power Cords  (continued)

Product ID (PID)

PID Description

Images

CAB-9K12A-NA

Power Cord, 125VAC 13A NEMA 
5-15 Plug, North America

CAB-N5K6A-NA

Power Cord, 200/240V 6A North 
America

CAB-C13-C14-AC

Power cord, C13 to C14 (recessed 
receptacle), 10A

CAB-C13-CBN

CABASY,WIRE,JUMPER CORD, 27" L, 
C13/C14, 10A/250V 

CAB-JPN-3PIN

Power Cord 3PIN, Japan

Image not available

CAB-C13-C14-2M

CAB-C13-C14-2M-JP

CAB-C13-C14-IN

Power Cord C13-C14, 2M/6.5ft 
Japan PSE mark

Power Cord C13-C14, 2M/6.5ft 
Japan PSE mark

Image not available

Image not available

Power Cord Jumper,C13-C14 
Connectors,1.4 Meter Length, India 

Image not available

CAB-C13-C14-3M-IN

Power Cord Jumper, C13-C14 
Connectors, 3 Meter Length, India 

Image not available

Cisco UCS 6536 Fabric Interconnect

17

CONFIGURING the FABRIC INTERCONNECT

STEP 6 CHOOSE TRANSCEIVERS AND CABLE OPTIONS (OPTIONAL)

The Cisco UCS 6536 supports a wide variety of 10/25/40/100 Gigabit Ethernet connectivity 
options using Cisco 10/25/40/100 Gbps modules. Unified ports (UP) on the Cisco UCS 6536 
support 10/25 Gigabit Ethernet connectivity or 8/16/32 Gigabit Fibre Channel modules.

Choose Transceivers

The supported transceivers are for the UCS 6536 are listed in Table 14.

Table 14  UCS 6536 FI Supported Transceivers 

Product ID (PID)

Description

SFP 1-Gigabit Transceivers

GLC-TE

1000 BASE-T SFP transceiver module for Category 5 copper wire

GLC-SX-MMD

1000BASE-SX short wavelength; with DOM

SFP+ 10-Gbps Transceivers

SFP-10G-SR

10GBASE-SR SFP Module

SFP-10G-SR-S

10GBASE-SR SFP Module, Enterprise-Class

SFP-10G-LR

10GBASE-LR SFP Module

SFP-10G-LR-S

10GBASE-LR SFP Module, Enterprise-Class

CVR-QSFP-SFP10G

QSFP 40G to SFP+ 10G adapter

SFP28 25-Gbps Transceivers

SFP-25G-SR-S

25GBASE-SR SFP Module

SFP-10/25G-LR-S

10/25GBASE-LR SFP28 Module

SFP-10/25G-CSR-S

Dual Rate 10/25GBASE-CSR SFP Module

SFP-25G-SL

25GBASE-SR SFP SL Module

CVR-QSFP28-SFP25G

100G to SFP25G adapter

Notes:

The 6536 FI supports 1G optics on ports 9 and 10. 

Transceiver modules and cables that are supported on a specific fabric interconnect are not always 
supported on all VIC adapters, I/O modules, or fabric extenders that are compatible with that fabric 
interconnect. Detailed compatibility matrices for the transceiver modules are available here: 
https://www.cisco.com/c/en/us/support/interfaces-modules/transceiver-modules/products-devi
ce-support-tables-list.html

SFP-10/25G-LR-S and SFP-10/25G-CSR-S are supported only at 25G speed. 

S-class transceivers do not support FCoE at 10G and 40G speeds.

18

Cisco UCS 6536 Fabric Interconnect

■
■
■
■
Caveats

CONFIGURING the FABRIC INTERCONNECT

The maximum length of fiber optic runs is limited to 300 meters. This is imposed by our use 
of 802.3X/802.1Qbb Priority Pauses.

NOTE:  

Transceiver modules and cables that are supported on a specific Fabric Interconnect are not 
always supported on all VIC adapters, IOMs, or FEXs that are compatible with that Fabric 
Interconnect. Detailed compatibility matrices for the transceiver modules are available 
here: 
https://www.cisco.com/c/en/us/support/interfaces-modules/transceiver-modules/product
s-device-support-tables-list.html

S-Class transceivers, (for example QSFP-40G-SR4-S), do not support FCoE.

Also For transceiver specifications, see the following link: 
http://www.cisco.com/c/en/us/td/docs/interfaces_modules/transceiver_modules/compati
bility/matrix/GE_Tx_Matrix.html

Refer to below data sheet for the complete details. 
https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs6536-fa
bric-interconnect-ds.html

Cisco UCS 6536 Fabric Interconnect

19

■
■
■
■
■
CONFIGURING the FABRIC INTERCONNECT

STEP 7 CHOOSE QSFP CABLE OPTIONS

The Cisco UCS 6536 supports a wide variety of 10/25/40/100 Gigabit Ethernet connectivity 
options using Cisco 10/25/40/100 Gbps modules. Unified ports (UP) on the Cisco UCS 6536 
support 10/25 Gigabit Ethernet connectivity or 8/16/32 Gigabit Fibre Channel modules.

Choose Transceivers

The supported transceivers are for the UCS 6536 are listed in Table 15.

Table 15  UCS 6536 FI Supported Transceivers 

Product ID (PID)

Description

QSFP+ 40Gbps Transceivers

QSFP-40G-SR4

40GBASE-SR4 QSFP Transceiver Module with MPO Connector

QSFP-40G-SR4-S

40GBASE-SR4 QSFP Transceiver Module, MPO Conn, Enterprise-Class

QSFP-40G-CSR4

QSFP 4x10GBASE-SR Transceiver Module, MPO, 300M

QSFP-40G-CSR-S

40GBASE-CSR QSFP Transceiver Module with LC Connector

QSFP-40G-SR-BD

40GBASE-SR-BiDi, duplex MMF (LC)

QSFP-40G-LR4

QSFP 40GBASE-LR4 OTN Transceiver, LC, 10KM

QSFP-40G-LR4-S

QSFP 40GBASE-LR4 Transceiver Module, LC, 10km, Enterprise-Class

FET-40G

40G Line Extender for FEX

QSFP 40G cables with integrated transceivers

QSFP-H40G-AOC1M

40GBASE active optical cable, 1M

QSFP-H40G-AOC2M

40GBASE Active Optical Cable, 2m

QSFP-H40G-AOC3M

40GBASE active optical cable, 3M

QSFP-H40G-AOC5M

40GBASE Active Optical Cable, 5m

QSFP-H40G-AOC7M

40GBASE Active Optical Cable, 7m

QSFP-H40G-AOC10M

40GBASE Active Optical Cable, 10m

QSFP-H40G-AOC15M

40GBASE Active Optical Cable, 15m

QSFP-H40G-AOC25M

40GBASE Active Optical Cable, 25m

QSFP-H40G-CU1M

40GBASE-CR4 Passive Copper Cable, 1m

QSFP-H40G-CU2M

40GBASE-CR4 Passive Copper Cable, 2m

QSFP-H40G-CU3M

40GBASE-CR4 Passive Copper Cable, 3m

QSFP-H40G-CU5M

40GBASE-CR4 Passive Copper Cable, 5m

QSFP-H40G-ACU10M

40GBASE-CR4 Active Copper Cable, 10m

20

Cisco UCS 6536 Fabric Interconnect

CONFIGURING the FABRIC INTERCONNECT

Table 15  UCS 6536 FI Supported Transceivers (continued)

Product ID (PID)

Description

QSFP-4X10G-AOC1M

40GBASE Active Optical QSFP to 4SFP breakout Cable, 1m

QSFP-4X10G-AOC3M

40GBASE Active Optical QSFP to 4SFP breakout Cable, 3m

QSFP-4X10G-AOC5M

40GBASE Active Optical QSFP to 4SFP breakout Cable, 5m

QSFP-4X10G-AOC7M

40GBASE Active Optical QSFP to 4SFP breakout Cable, 7m

QSFP-4X10G-AOC10M

40GBASE Active Optical QSFP to 4SFP breakout Cable, 10m

QSFP-4SFP10G-CU1M

QSFP to 4xSFP10G Passive Copper Splitter Cable, 1m

QSFP-4SFP10G-CU3M

QSFP to 4xSFP10G Passive Copper Splitter Cable, 3m

QSFP-4SFP10G-CU5M

QSFP to 4xSFP10G Passive Copper Splitter Cable, 5m

QSFP28 100G Transceivers

QSFP-100G-SR4-S

100GBASE SR4 QSFP Transceiver, MPO, 100m over OM4 MMF

QSFP-100G-LR4-S

100GBASE LR4 QSFP Transceiver, LC, 10km over SMF

QSFP-40/100-SRBD1,2

100GBASE/40GBASE SR-BiDi QSFP Transceiver, LC, 100m over OM4 MMF

QSFP-100G-SM-SR

100GBASE CWDM4 lite QSFP transceiver, 2KM over SMF, 10-60C

QSFP-100G-SL4

100GBASE SL4 for up to 30M over OM4 MMF

QSFP-100G-DR-S

100G QSFP28 Transceiver 100GBASE-DR, 500m SMF, duplex, LC

QSFP-100G-FR-S

100G QSFP28 Transceiver 100G-FR, 2km SMF, duplex, LC

QSFP-100G-PSM4-S

100GBASE PSM4 QSFP Transceiver, MPO, 500m over SMF

QSFP-100G-SR1.2

100G SR1.2 BiDi QSFP Transceiver, LC, 100m OM4 MMF

QSFP28 100G cables with integrated transceivers

QSFP-100G-CU1M

QSFP-100G-CU2M

QSFP-100G-CU3M

QSFP-100G-CU5M

QSFP-100G-AOC1M

QSFP-100G-AOC2M

QSFP-100G-AOC3M

QSFP-100G-AOC5M

QSFP-100G-AOC7M

100GBASE-CR4 passive copper cable, 1M

100GBASE-CR4 passive copper cable, 2M

100GBASE-CR4 passive copper cable, 3M

100GBASE-CR4 passive copper cable, 5M

100GBASE QSFP active optical cable, 1M

100GBASE QSFP active optical cable, 2M

100GBASE QSFP active optical cable, 3M

100GBASE QSFP active optical cable, 5M

100GBASE QSFP active optical cable, 7M

QSFP-100G-AOC10M

100GBASE QSFP active optical cable, 10M

Cisco UCS 6536 Fabric Interconnect

21

CONFIGURING the FABRIC INTERCONNECT

Table 15  UCS 6536 FI Supported Transceivers (continued)

Product ID (PID)

Description

QSFP-100G-AOC15M

QSFP-100G-AOC20M

QSFP-100G-AOC25M

QSFP-100G-AOC30M

QSFP-4SFP25G-CU1M

QSFP-4SFP25G-CU2M

QSFP-4SFP25G-CU3M

QSFP-4SFP25G-CU5M

100GBASE QSFP active optical cable, 15M

100GBASE QSFP active optical cable, 20M

100GBASE QSFP active optical cable, 25M

100GBASE QSFP active optical cable, 30M

100GBASE QSFP to 4xSFP25G passive copper splitter cable, 1M

100GBASE QSFP to 4xSFP25G passive copper splitter cable, 2M

100GBASE QSFP to 4xSFP25G passive copper splitter cable, 3M

100GBASE QSFP to 4xSFP25G passive copper splitter cable, 5M

Fibre Channel transceivers

DS-SFP-4X32G-SW3

128 Gbps FC-SW QSFP, MPO for 4 x 8/16/32G fibre channel breakout, 100M

Notes

1. QSFP-40/100-SRBD is supported at 40 or 100G speed on uplink and for all other connectivity like 

server-port for IFM, FEX or VIC it supports only 100G speed. 

2. QSFP 40/100 SRBD optic is not supported with 2304v2 IOM
3.  The Cisco 128G FC QSPF (PID: DS-SFP-4x32G-SW) on the UCS 6536 Fabric Interconnect unified ports 

(33-36) will be used to connect to a SAN switch or storage array at 8/16/32G speeds using a 
multi-mode OM4 MPO female to 4x LC 8-fiber type-B breakout cable. The breakout cable for 
DS-SFP-4x32G-SW QSFP transceiver can use one of the Cisco breakout & patch-panel solution 
referenced in Table 27 & Table 28.

22

Cisco UCS 6536 Fabric Interconnect

CONFIGURING the FABRIC INTERCONNECT

STEP 8 ACCESSORY KIT (INCLUDED)

An accessory kit is included for the Cisco 6536 Fabric Interconnects.

Choose Accessory Kit

The supported accessory kits for the Cisco UCS 6536 Fabric Interconnects are listed in Table 16.

Table 16   6536 FI Accessory Kit 

Product ID (PID)

Description

UCS-ACC-6536

UCS 6536 Chassis Accessory Kit

UCS-ACC-6536=

Spare, UCS 6536 Chassis Accessory Kit

UCS-ACC-6536-D

UCS 6536 Chassis Accessory Kit

UCS-ACC-6536-D=

Spare, UCS 6536 Chassis Accessory Kit

The Cisco UCS 6536 Fabric Interconnect accessory kit includes the following items:

2 slider rails

2 rack-mount guides

2 rack-mount brackets

12 M4 x 0.7 x 8-mm Phillips countersunk screws

10 10-32 rack nuts

10 10-32 x 3/4-inch Phillips pan-head screws

1 console cable with an RJ-45-RS-232 adapter and a DB9 adapter

1 ground lug kit

1 ESD wrist strap

1 power cord clip (a wire clip that is used to retain the power cord)

1 pointer document (specifies where to find the online product documentation)

Cisco UCS 6536 Fabric Interconnect

23

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
CONFIGURING the FABRIC INTERCONNECT

STEP 9 FAN MODULE (INCLUDED)

6536 FI Fan Module

These are hot-swappable 6 x fan modules. And each fan module consists of two fan rotors. Redundancy of 
the fan is implanted in rotor level, and when the rotor fails, the system continues to operate with 9 fan 
rotors.

Table 17  6536 FI Fan Module

Product ID (PID)

UCS-FAN-6536

UCS-FAN-6536-D

Description

UCS 6536 Fan Module

UCS 6536 Fan Module

24

Cisco UCS 6536 Fabric Interconnect

CONFIGURING the FABRIC INTERCONNECT

STEP 10 CHOOSE SERVICE AND SUPPORT LEVEL

A variety of service options are available, as described in this section.

Unified Computing Warranty, No Contract

If you have noncritical implementations and choose to have no service contract, the following 
coverage is supplied:

Three-year parts coverage.

Next business day (NBD) onsite parts replacement eight hours a day, five days a week.

90-day software warranty on media.

Ongoing downloads of BIOS, drivers, and firmware updates.

Smart Net Total Care (SNTC) for UCS 

For support of the entire Unified Computing System, Cisco offers the Cisco Smart Net Total Care 
for UCS  Service. This service provides expert software and hardware support to help sustain 
performance and high availability of the unified computing environment. Access to Cisco 
Technical Assistance Center (TAC) is provided around the clock, from anywhere in the world

For systems that include Unified Computing System Manager, the support service includes 
downloads of UCSM upgrades. The Cisco Smart Net Total Care for UCS Service  includes flexible 
hardware replacement options, including replacement in as little as two hours.  There is also 
access to Cisco's extensive online technical resources to help maintain optimal  efficiency and 
uptime of the unified computing environment. For more information please refer to the following 
url: http://www.cisco.com/c/en/us/services/technical/smart-net-total-care.html?stickynav=1

You can choose a desired service  listed in Table 18.

Table 18  Cisco SNTC for UCS Service (PID UCSX-FI-6536-U) 

Service SKU

Service Level GSP

On Site?

Description

CON-PREM-UCSXUUFI

C2P

CON-UCSD8-UCSXUUFI

UCSD8

CON-OSP-UCSXUUFI

C4P

CON-UCSD7-UCSXUUFI

UCSD7

CON-C4PL-UCSXUUFI

C4PL

CON-USD7L-UCSXUUFI

USD7L

CON-OSE-UCSXUUFI

C4S

CON-UCSD6-UCSXUUFI

UCSD6

CON-SNCO-UCSXUUFI

SNCO

CON-OS-UCSXUUFI

CS

CON-UCSD5-UCSXUUFI

UCSD5

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

SNTC 24X7X2OS 

UC SUPP DR 24X7X2OS*

SNTC 24X7X4OS 

UCS DR 24X7X4OS*

LL 24X7X4OS**

LLUCS HW DR 24X7X4OS***

SNTC 8X5X4OS 

UC SUPP DR 8X5X4OS*

SNTC 8x7xNCDOS****

SNTC 8X5XNBDOS 

UCS DR 8X5XNBDOS*

Cisco UCS 6536 Fabric Interconnect

25

■
■
■
■
CONFIGURING the FABRIC INTERCONNECT

Table 18  Cisco SNTC for UCS Service (PID UCSX-FI-6536-U) 

Service SKU

Service Level GSP

On Site?

Description

CON-S2P-UCSXUUFI

S2P

CON-SNTP-UCSXUUFI

SNTP

CON-SNTPL-UCSXUUFI

SNTPL

CON-SNTE-UCSXUUFI

SNTE

CON-SNC-UCSXUUFI

CON-SNT-UCSXUUFI

CON-SW-UCSXUUFI

SNC

SNT

SW

No

No

No

No

No

No

No

SNTC 24X7X2 

SNTC 24X7X4 

LL 24X7X4**

SNTC 8X5X4 

SNTC 8x7xNCD****

SNTC 8X5XNBD

SNTC NO RMA

Note: For PID UCSX-6536-CH, select Service SKU with UCSIXFI6 suffix (Example: CON-OSP-UCSIXFI6)

*Includes Drive Retention (see below for full description)

**Includes Local Language Support (see below for full description) – Only available in China and Japan

***Includes Local Language Support and Drive Retention – Only available in China and Japan

Smart Net Total Care (SNTC) for Cisco UCS Onsite Troubleshooting Service

An enhanced offer over traditional Smart Net Total Care which provides onsite-troubleshooting 
expertise to aid in the diagnostics and isolation of hardware issue within our customers’ Cisco 
Unified Computing System (UCS) environment. It is delivered by a Cisco Certified field engineer 
(FE) in collaboration with remote TAC engineer and Virtual Internet working Support Engineer 
(VISE). You can choose a desired service listed in 

Table 19

Table 19   SNTC for Cisco UCS Onsite Troubleshooting Service (PID UCSX-FI-6536-U)

Service SKU

Service Level GSP

On Site?

Description

CON-OSPT-UCSXUUFI

OSPT

CON-OSPTD-UCSXUUFI

OSPTD

Yes

Yes

24X7X4OS Trblshtg

24X7X4OS TrblshtgDR*

Note: For PID UCSX-6536-CH, select Service SKU with UCSIXFI6 suffix (Example: CON-OSPT-UCSIXFI6)

*Includes Drive Retention (see below for full description)

**Includes Local Language Support (see below for full description) – Only available in China and Japan

***Includes Local Language Support and Drive Retention – Only available in China and Japan

Solution Support for UCS

26

Cisco UCS 6536 Fabric Interconnect

CONFIGURING the FABRIC INTERCONNECT

Solution Support (SSPT) for UCS

Solution Support includes both Cisco product support and solution-level support, resolving 
complex issues in multivendor environments, on average, 43% more quickly than product 
support alone.  Solution Support is a critical element in data center administration, to help 
rapidly resolve any issue encountered, while maintaining performance, reliability, and return on 
investment. 

This service centralizes support across your multivendor Cisco environment for both our 
products and solution partner products you’ve deployed in your ecosystem.  Whether there is an 
issue with a Cisco or solution partner product, just call us. Our experts are the primary point of 
contact and own the case from first call to resolution.  For more information please refer to the 
following url:
http://www.cisco.com/c/en/us/services/technical/solution-support.html?stickynav=1
You can choose a desired service  listed in 

Table 20

Table 20  Solution Support for UCS Service (PID UCSX-FI-6536-U) 

Service SKU

Service Level GSP

On Site?

Description

CON-SSC2P-UCSXUUFI

SSC2P

CON-SSC4P-UCSXUUFI

SSC4P

CON-SSC4S-UCSXUUFI

SSC4S

CON-SSCS-UCSXUUFI

SSCS

CON-SSDR7-UCSXUUFI

SSDR7

CON-SSDR5-UCSXUUFI

SSDR5

CON-SSS2P-UCSXUUFI

SSS2P

CON-SSSNP-UCSXUUFI

SSSNP

CON-SSSNE-UCSXUUFI

SSSNE

CON-SSSNC-UCSXUUFI

SSSNC

CON-SSSNT-UCSXUUFI

SSSNT

Yes

Yes

Yes

Yes

Yes

Yes

No

No

No

No

No

SOLN SUPP 24X7X2OS

SOLN SUPP 24X7X4OS

SOLN SUPP 8X5X4OS

SOLN SUPP 8X5XNBDOS

SSPT DR 24X7X4OS*

SSPT DR 8X5XNBDOS*

SOLN SUPP 24X7X2

SOLN SUPP 24X7X4

SOLN SUPP 8X5X4

SOLN SUPP NCD**

SOLN SUPP 8X5XNBD

Note: For PID UCSX-6536-CH, select Service SKU with UCSIXFI6 suffix (Example: CON-SSC4P-UCSIXFI6)

*Includes Drive Retention (see below for full description)

**Includes Local Language Support (see below for full description) – Only available in China and Japan

***Includes Local Language Support and Drive Retention – Only available in China and Japan

Cisco UCS 6536 Fabric Interconnect

27

CONFIGURING the FABRIC INTERCONNECT

Solution Support for Service Providers

You can choose a desired service  listed in Table 20

Table 21  Solution Support for Service Providers UCS Service (PID UCSX-FI-6536-U)

Service SKU

Service Level GSP

On Site?

Description

SP-SSC2P-UCSXUUFI

SPSSC2P

SP-SSC4P-UCSXUUFI

SPSSC4P

SP-SSC4S-UCSXUUFI

SPSSC4S

SP-SSCS-UCSXUUFI

SPSSCS

SP-SSS2P-UCSXUUFI

SP-SSS4P-UCSXUUFI

SPSSS2P

SPSSS4P

SP-SSSNE-UCSXUUFI

SPSSSNE

SP-SSSNT-UCSXUUFI

SPSSSNT

SP-SSSPB-UCSXUUFI

SPSSSPB

Yes

Yes

Yes

Yes

Yes

Yes

No

No

No

SP SOLN SUPP 24X7X2OS

SP SOLN SUPP 24X7X4OS

SP SOLN SUPP 8X5X4OS

SP SOLN SUPP 8X5XNBDOS

SP SOLN SUPP 24X7X2

SP SOLN SUPP 24X7X4

SP SOLN SUPP 8X5X4

SP SOLN SUPP 8X5XNBD

SP SOLN SUPP NO HW RPL

Note: For PID UCSX-6536-CH, select Service SKU with UCSIXFI6 suffix (Example: CON-SPSSC4P-UCSIXFI6)

Smart Net Total Care for UCS Hardware Only Service

For faster parts replacement than is provided with the standard Cisco Unified Computing System 
warranty, Cisco offers the Cisco Smart Net Total Care for UCS Hardware Only Service. You can 
choose from two levels of advanced onsite parts replacement coverage in as little as four hours. 
Smart Net Total Care for UCS Hardware Only Service provides remote access any time to Cisco 
support professionals who can determine if a return materials authorization (RMA) is required. 
You can choose a desired service listed in Table 22

Table 22  SNTC for UCS Hardware Only Service (PID UCSX-FI-6536-U)

Service SKU

Service Level GSP

On Site?

Description

CON-UCW7-UCSXUUFI

UCW7

CON-UCWD7-UCSXUUFI

UCWD7

CON-UCW5-UCSXUUFI

UCW5

CON-UCWD5-UCSXUUFI

UCWD5

Yes

Yes

Yes

Yes

UCS HW 24X7X4OS

UCS HW+DR 24X7X4OS*

UCS HW 8X5XNBDOS

UCS HW+DR 8X5XNBDOS*

Note: For PID UCSX-6536-CH, select Service SKU with UCSIXFI6 suffix (Example: CON-UCW7-UCSIXFI6)

*Includes Drive Retention (see below for full description)

**Includes Local Language Support (see below for full description) – Only available in China and Japan

28

Cisco UCS 6536 Fabric Interconnect

Table 22  SNTC for UCS Hardware Only Service (PID UCSX-FI-6536-U)

***Includes Local Language Support and Drive Retention – Only available in China and Japan

CONFIGURING the FABRIC INTERCONNECT

Partner Support Service for UCS

Cisco Partner Support Service (PSS) is a Cisco Collaborative Services service offering that is 
designed for partners to deliver their own branded support and managed services to enterprise 
customers. Cisco PSS provides partners with access to Cisco's support infrastructure and assets 
to help them:

Expand their service portfolios to support the most complex network environments

Lower delivery costs

Deliver services that increase customer loyalty

PSS options enable eligible Cisco partners to develop and consistently deliver high-value 
technical support that capitalizes on Cisco intellectual assets. This helps partners to realize 
higher margins and expand their practice. 

PSS is available to all Cisco PSS partners.

The two Partner Unified Computing Support Options include: 

Partner Support Service for UCS

Partner Support Service for UCS Hardware Only

PSS for UCS provides hardware and software support, including triage support for third party 
software, backed by Cisco technical resources and level three support.You can choose a desired 
service listed in Table 23.

Table 23  PSS for UCS (PID UCSX-FI-6536-U)

Service SKU

Service Level GSP

On Site?

Description

CON-PSJ8-UCSXUUFI

CON-PSJ7-UCSXUUFI

PSJ8

PSJ7

CON-PSJD7-UCSXUUFI

PSJD7

CON-PSJ6-UCSXUUFI

PSJ6

CON-PSJD6-UCSXUUFI

PSJD6

CON-PSJ4-UCSXUUFI

CON-PSJ3-UCSXUUFI

CON-PSJ2-UCSXUUFI

CON-PSJ1-UCSXUUFI

PSJ4

PSJ3

PSJ2

PSJ1

Yes

Yes

Yes

Yes

Yes

No

No

No

No

UCS PSS 24X7X2 OS

UCS PSS 24X7X4 OS

UCS PSS 24X7X4 DR*

UCS PSS 8X5X4 OS

UCS PSS 8X5X4 DR*

UCS SUPP PSS 24X7X2 

UCS SUPP PSS 24X7X4 

UCS SUPP PSS 8X5X4 

UCS SUPP PSS 8X5XNBD 

Note: For PID UCSX-6536-CH, select Service SKU with UCSIXFI6 suffix (Example: CON-PSJ7-UCSIXFI6)

*Includes Drive Retention (see below for description)

Cisco UCS 6536 Fabric Interconnect

29

■
■
■
■
■
CONFIGURING the FABRIC INTERCONNECT

PSS for UCS Hardware Only

PSS for UCS Hardware Only provides customers with replacement parts in as little as two hours 
and provides remote access any time to Partner Support professionals who can determine if a 
return materials authorization (RMA) is required. You can choose a desired service listed in 
Table 24

Table 24  PSS for UCS Hardware Only (PID UCSX-FI-6536-U)

Service SKU

Service Level GSP

On Site?

Description

CON-PSW7-UCSXUUFI

PSW7

CON-PSWD7-UCSXUUFI

PSWD7

CON-PSW6-UCSXUUFI

PSW6

CON-PSWD6-UCSXUUFI

PSWD6

CON-PSW4-UCSXUUFI

CON-PSW3-UCSXUUFI

CON-PSW2-UCSXUUFI

PSW4

PSW3

PSW2

Yes

Yes

Yes

Yes

No

No

No

UCS W PSS 24X7X4 OS

UCS W PSS 24X7X4 DR*

UCS W PSS 8X5X4 OS

UCS W PSS 8X5X4 DR*

UCS W PL PSS 24X7X2 

UCS W PL PSS 24X7X4 

UCS W PL PSS 8X5X4 

Note: For PID UCSX-6536-CH, select Service SKU with UCSIXFI6 suffix (Example: CON-PSW7-UCSIXFI6)

*Includes Drive Retention (see below for description)

Distributor Support Service (DSS)

You can choose a desired service listed in 

Table 25

Table 25  DSS for UCS Service (PID UCSX-FI-6536-U)

Service SKU

Service Level GSP

On Site?

Description

CON-DSCO-UCSXUUFI

DSCO

CON-DSO-UCSXUUFI

DSO

CON-DSNO-UCSXUUFI

DSNO

CON-DSCC-UCSXUUFI

DSCC

CON-DCP-UCSXUUFI

CON-DSE-UCSXUUFI

CON-DSN-UCSXUUFI

DCP

DSE

DSN

Yes

Yes

Yes

No

No

No

No

DSS CORE 24X7X2OS

DSS CORE 24X7X4

DSS CORE 8X5XNBDOS

DSS CORE 24X7X2

DSS CORE 24X7X4

DSS CORE 8X5X4

DSS CORE 8X5XNBD

Note: For PID UCSX-6536-CH, select Service SKU with UCSIXFI6 suffix (Example: CON-DSO-UCSIXFI6)

30

Cisco UCS 6536 Fabric Interconnect

CONFIGURING the FABRIC INTERCONNECT

Unified Computing Combined Support Service

Combined Services makes it easier to purchase and manage required services under one 
contract. SNTC services for UCS help increase the availability of your vital data center 
infrastructure and realize the most value from your unified computing investment. The more 
benefits you realize from the Cisco Unified Computing System (Cisco UCS), the more important 
the technology becomes to your business. These services allow you to:

Optimize the uptime, performance, and efficiency of your UCS

Protect your vital business applications by rapidly identifying and addressing issues

Strengthen in-house expertise through knowledge transfer and mentoring

Improve operational efficiency by allowing UCS experts to augment your internal staff 
resources

Enhance business agility by diagnosing potential issues before they affect your operations,

You can choose a desired service listed in 

Table 26.

Table 26  Combined Support Service for UCS (PID UCSX-FI-6536-U)

Service SKU

Service Level GSP

On Site?

Description

CON-NCF2P-UCSXUUFI

NCF2P

CON-NCF4P-UCSXUUFI

NCF4P

CON-NCF4S-UCSXUUFI

NCF4S

CON-NCFCS-UCSXUUFI

NCFCS

CON-NCF2-UCSXUUFI

CON-NCFP-UCSXUUFI

CON-NCFE-UCSXUUFI

CON-NCFT-UCSXUUFI

NCF2

NCFP

NCFE

NCFT

CON-NCFW-UCSXUUFI

NCFW

Yes

Yes

Yes

Yes

No

No

No

No

No

CMB SVC 24X7X2OS

CMB SVC 24X7X4OS

CMB SVC 8X5X4OS

CMB SVC 8X5XNBDOS

CMB SVC 24X7X2

CMB SVC 24X7X4

CMB SVC 8X5X4

CMB SVC 8X5XNBD

CMB SVC SW

Note: For PID UCSX-6536-CH, select Service SKU with UCSIXFI6 suffix (Example: CON-NCF4P-UCSIXFI6)

UCS Drive Retention Service

With the Cisco Unified Computing Drive Retention Service, you can obtain a new disk drive in 
exchange for a faulty drive without returning the faulty drive. 

Sophisticated data recovery techniques have made classified, proprietary, and confidential 
information vulnerable, even on malfunctioning disk drives. The Drive Retention service enables 
you to  retain your drives and ensures that the sensitive data on those drives is not compromised, 

Cisco UCS 6536 Fabric Interconnect

31

■
■
■
■
■
CONFIGURING the FABRIC INTERCONNECT

which reduces the risk of any potential liabilities. This service also enables you to comply with 
regulatory, local, and federal requirements.

If your company has a need to control confidential, classified, sensitive, or proprietary data, you 
might want to consider one of the Drive Retention Services listed in the above tables (where 
available)

NOTE:  Cisco does not offer a certified drive destruction service as part of this 
service.

Local Language Technical Support for UCS

Where available, and subject to an additional fee, local language support for calls on all 
assigned severity levels may be available for specific product(s) – see tables above.

For a complete listing of available services for Cisco Unified Computing System, see this URL: 
http://www.cisco.com/en/US/products/ps10312/serv_group_home.html

32

Cisco UCS 6536 Fabric Interconnect

SUPPLEMENTAL MATERIAL

SUPPLEMENTAL MATERIAL

Cisco UCS 6536 FI Port Numbering

Each port on the Cisco UCS 6536 Fabric Interconnect is numbered, and groups of ports are numbered based 
on their function. The ports are numbered top to bottom and left to right.

Figure 5 shows how ports are numbered and the table below explains how each port group functions.

Figure 5

  Port Numbering of the Cisco UCS 6536

 FI

1

Ports 1—32:

2

Ports 33-36:

Ethernet uplink port at 1/10/25/40/100G, 
Server port will operate only at 25/40/100G 
speeds, FCoE uplink port, Appliance port 
(EHM only), Monitor Port operate either as 
100G/40G/25G/10G QSFP28 Ethernet

FC uplink port operate either as 
8G/16G/32G Gbps Fibre channel

Ethernet uplink port, Server port, FCoE 
uplink port, Appliance port (EHM only), 
Monitor Port operate either as 
100G/40G/25G/10G QSFP28 Ethernet

Cisco UCS 6536 FI Supported Speeds

Speed

1 Gbps

10/25 Gbps

40/100 Gbps

8/16/32 Gbps FC

1-8

No

Yes

Yes

No

Port Range

9-10

11-32

33-36

Yes

Yes

Yes

No

No           

Yes          

Yes          

No

No

Yes

Yes

Yes

Cisco UCS 6536 Fabric Interconnect

33

■
■
SUPPLEMENTAL MATERIAL

Connectivity

This section explains the connectivity between the Fabric Interconnects (FIs) and Fabric Extenders (FEX). 
The Fabric Extenders are extensions of the Fabric Interconnects and act as remote line cards to form a 
distributed modular fabric system. The fabric extension is accomplished through the FEX fabric link, which 
is the connection between the Fabric Interconnect and the FEX.

A minimum of one connection between the FI and FEX is required to provide server connectivity. Depending 
on the FEX model, subsequent connections can be up to eight links, which provides added bandwidth to the 
servers.

9508 Chassis Server Connectivity

For the X9508 chassis, the Fabric Extender modules (up to two) plug into the back of the UCS X9508 chassis. 
There is no backplane in the Cisco UCS X9508 chassis; the compute nodes directly connect to the IFMs using 
Orthogonal Direct connectors. The X9508 chassis accommodates the following IFMs:

Cisco IFM 9108-25G (Figure 6)
Cisco IFM 9108-100G (Figure 7)

The connectivity from the X9108-IFM-25G to 6536 Fabric Interconnects is shown in Figure 6.

Figure 6

X9108-IFM-25G to 6536 Fabric Interconnect Connectivity

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

34

Cisco UCS 6536 Fabric Interconnect

■
■
  
SUPPLEMENTAL MATERIAL

The connectivity from the X9108-IFM-100G to 6536 Fabric Interconnects is shown in Figure 7.

Figure 7

X9108-IFM-100G to 6536 Fabric Interconnect Connectivity

= QSFP28 Links

1600G Per X9508 Chassis
100G E2E single-flow
200G Per x210 with 1:1  oversubsription

IFM A-100G  (8 x 100GB) 
IFM B-100G  (8 x 100GB) 

IFM  A

IFM  B

Cisco UCS 6536 Fabric Interconnect

35

  
SUPPLEMENTAL MATERIAL

5108 Blade Chassis Server Connectivity

For the 5108 blade chassis, the Fabric Extender modules (up to two) plug into the back of the UCS 5108 
series blade server chassis. A midplane connects the blade servers to the Fabric Extenders. The 5108 chassis 
accommodates the following FEX:

Cisco UCS 2304 
Cisco UCS 2408 (Figure 8)

Figure 8 shows how the FEX modules in the blade chassis connect to the FIs.

Figure 8

  Connecting Blade Chassis Fabric Extenders to Fabric Interconnect Chassis
Fabric Interconnect A (6536)

Fabric Interconnect B (6536)

Fabric Extender 1 (2408)
                  8 x 25Gb

Fabric Extender 2 (2408)
            8 x 25Gb

NOTE:  Cisco UCS 5108 rev 1 and rev 2 chassis are both supported with FI 6536

36

Cisco UCS 6536 Fabric Interconnect

■
■
SUPPLEMENTAL MATERIAL

C-Series Rack-Mounted Server Connectivity

C-Series servers connect to external FEXs and FIs as summarized in this section. Single-Wire Management 
interconnection methods are possible:

Single-Wire Management

Cisco UCS Intersight supports an additional option to integrate the C-Series Rack-Mount Server with Cisco 
UCS Manager using the NCSI. This option enables Cisco Intersight to manage the C-Series Rack-Mount 
Servers using a single-wire for both management traffic and data traffic. When you use the single-wire 
management mode, one host facing port on the FEX is sufficient to manage one rack-mount server, instead 
of the two ports you would use in the Shared-LOM mode. This connection method allows you to connect 
more rack-mount servers for integrated server management.

C-Series Rack-Mounted Server Connectivity has two options:

Single-wire Management With 93180YC-FX3 in FEX mode and FEX 2348 UPQ (Figure 10)

Single-wire Management Without FEX (Figure 11 & Figure 12)

Figure 9 shows how the C-Series rack mount chassis connect to the FEXs and FIs for single-wire 
management.

Figure 9

  Connecting C-Series Rack Chassis (single-wire management with Nexus Switches)

1

Fabric A

3

Fabric B

40-Gbps

2

40-Gbps

4

10-Gbps

6

10-Gbps

5

1
2
3

Cisco UCS 6536 FI (Fabric A)
Cisco Nexus 93180YC-FX3 (Fabric A)
Cisco UCS 6536 FI (Fabric B)

4
5
6

Cisco Nexus 93180YC-FX3 (Fabric B)
Cisco UCS C-series M5/M6/M7 server
Cisco UCS VIC 1455/1457/1467/15428

Cisco UCS 6536 Fabric Interconnect

37

■
■
SUPPLEMENTAL MATERIAL

Figure 10 shows how the C-Series rack mount chassis connect to the FEXs and FIs for single-wire 
management.

Figure 10

  Connecting C-Series Rack Chassis (single-wire management with Nexus Switches)

1

Fabric A

3

Fabric B

40-Gbps

2

40-Gbps

4

10-Gbps

6

10-Gbps

5

1
2
3

Cisco UCS 6536 FI (Fabric A)
Cisco Nexus 2348 UPQ (Fabric A)
Cisco UCS 6536 FI (Fabric B)

4
5
6

Cisco Nexus 2348 UPQ (Fabric B)
Cisco UCS C-series M4/M5/M6/M7 server
Cisco UCS VIC 
1385/1387/1455/1457/1467/15428

38

Cisco UCS 6536 Fabric Interconnect

SUPPLEMENTAL MATERIAL

Figure 11 shows how the C-Series rack mount chassis connect to FIs for single-wire management.

Figure 11

  Connecting C-Series Rack Chassis (single-wire management without FEX)

1

Fabric A

4x 25G
breakout

2

Fabric B

4x 25G
breakout

4

3

1
2

Cisco UCS 6536 FI (Fabric A)
Cisco UCS 6536 FI (Fabric B)

3
4

Cisco UCS C-series M5/M6/M7 server
Cisco UCS VIC 1455/1457/1467/15428

Cisco UCS 6536 Fabric Interconnect

39

SUPPLEMENTAL MATERIAL

Figure 12

  Connecting C-Series Rack Chassis (single-wire management without FEX)

1

Fabric A

2

Fabric B

40/100G

4

40/100G

3

1
2

Cisco UCS 6536 FI (Fabric A)
Cisco UCS 6536 FI (Fabric B)

3
4

Cisco UCS C-series M4/M5/M6/M7 server
Cisco UCS VIC 1385/13871477/1497/1495/15238

40

Cisco UCS 6536 Fabric Interconnect

SUPPLEMENTAL MATERIAL

FI 6536 Fibre channel connectivity

The Cisco 128G FC QSPF (PID: DS-SFP-4x32G-SW) is required to connect to a SAN switch or storage array at 
8/16/32G speeds using a multi-mode OM4, 8 fiber MPO to LC breakout cable.

Figure 13

  FC Connectivity

FI 6536

Ports 33-36

128G FC QSFP
Cisco PID: DS-SFP-4X32G-SW

Mul(cid:2)mode OM4 ﬁber,
8 ﬁber MPO to LC breakout c

8/16/32G FC SW SFP

SAN switch or Storage Array

Cisco UCS 6536 Fabric Interconnect

41

SUPPLEMENTAL MATERIAL

UCS 6536 FI Break Out Connectivity 

The UCS 6536 Fabric Interconnect has been qualified with the new TMG offerings of MPO-LC breakout cable 
and the patch panel solution.

The breakout cable or the patch panel solution can be used for the following connectivity:

100G to 4x25G breakout for FI 6536 server ports with IFM-25G, IOM-2408 and 
VIC-15428/1455/1457/1467.

100G to 4x25G or 40G to 4x10G Ethernet breakout for FI 6536 uplink port.

4x32G or 4x 16G or 4x 8G FC breakout using “DS-SFP-4X32G-SW” QSFP transceivers on the FI 6536 
unified ports.

The following are the supported cable and patch panels PIDs that are qualified with UCS 6536 Fabric 
Interconnect:

Table 27  MPO to LC breakout cables

Cisco PID

Cisco Description

MPO to LC Breakout cable only, No patch panel

CB-M12-4LC-MMF1.5=

 CABLE, MPO12-4X DUPLEX LC, BREAKOUT CABLE, MMF, 1.5M

CB-M12-4LC-MMF2M=

 CABLE, MPO12-4X DUPLEX LC, BREAKOUT CABLE, MMF, 2M

CB-M12-4LC-MMF3M=

 CABLE, MPO12-4X DUPLEX LC, BREAKOUT CABLE, MMF, 3M

CB-M12-4LC-MMF4M=

 CABLE, MPO12-4X DUPLEX LC, BREAKOUT CABLE, MMF, 4M

CB-M12-4LC-MMF5M=

 CABLE, MPO12-4X DUPLEX LC, BREAKOUT CABLE, MMF, 5M

CB-M12-4LC-MMF7M=

 CABLE, MPO12-4X DUPLEX LC, BREAKOUT CABLE, MMF, 7M

CB-M12-4LC-MMF10M=

 CABLE, MPO12-4X DUPLEX LC, BREAKOUT CABLE, MMF, 10M

CB-M12-4LC-MMF15M=

 CABLE, MPO12-4X DUPLEX LC, BREAKOUT CABLE, MMF, 15M

CB-M12-4LC-MMF20M=

 CABLE, MPO12-4X DUPLEX LC, BREAKOUT CABLE, MMF, 20M

CB-M12-4LC-MMF25M=

 CABLE, MPO12-4X DUPLEX LC, BREAKOUT CABLE, MMF, 25M

CB-M12-4LC-MMF30M=

 CABLE, MPO12-4X DUPLEX LC, BREAKOUT CABLE, MMF, 30M

NOTE:  In addition to the above cables, customers could also use a breakout-solution 
from any good cable vendor or use the qualified breakout cables from the vendor 
Panduit (Part Num#: FZ8RP5NLSQNM003, M005)

42

Cisco UCS 6536 Fabric Interconnect

■
■
■
SUPPLEMENTAL MATERIAL

Table 28  Cisco patch panel solution

Cisco PID

Cisco Description

Patch Panel + Cassette + patch cord

PP-72X100G-MMF=

PATCH PANEL, 1RU, 18 MPO12 - 72 DUPLEX LC, MMF

PP-144X100G-MMF=

PATCH PANEL, 2RU, MPO12 - 144 DUPLEX LC, MMF

PP-216X100G-MMF=

PATCH PANEL, 3RU, 54 MPO12 - 216 DUPLEX LC, MMF

PP-1RU-CHAS

PP-2RU-CHAS

PP-3RU-CHAS

PATCH PANEL, 1RU, EMPTY CHASSIS

PATCH PANEL, 2RU, EMPTY CHASSIS

PATCH PANEL, 3RU, EMPTY CHASSIS

PP-CAS-L-12LC-MMF= 

PATCH PANEL, LEFT CASSETTE, 3 MPO12 - 12 DUPLEX LC, MMF

PP-CAS-R-12LC-MMF=

PATCH PANEL, RIGHT CASSETTE, 3 MPO12 - 12 DUPLEX LC, MMF

MPO to MPO

CB-M12-M12-MMF1M=

 CABLE, MPO12-MPO12, TRUNK CABLE, TYPE B, MMF, 1M

CB-M12-M12-MMF1.5=

 CABLE, MPO12-MPO12, TRUNK CABLE, TYPE B, MMF, 1.5M

CB-M12-M12-MMF2M=

 CABLE, MPO12-MPO12, TRUNK CABLE, TYPE B, MMF, 2M

CB-M12-M12-MMF3M=

 CABLE, MPO12-MPO12, TRUNK CABLE, TYPE B, MMF, 3M

CB-M12-M12-MMF4M=

 CABLE, MPO12-MPO12, TRUNK CABLE, TYPE B, MMF, 4M

CB-M12-M12-MMF5M=

 CABLE, MPO12-MPO12, TRUNK CABLE, TYPE B, MMF, 5M

CB-M12-M12-MMF7M=

 CABLE, MPO12-MPO12, TRUNK CABLE, TYPE B, MMF, 7M

CB-M12-M12-MMF10M=

 CABLE, MPO12-MPO12, TRUNK CABLE, TYPE B, MMF, 10M

CB-M12-M12-MMF15M=

 CABLE, MPO12-MPO12, TRUNK CABLE, TYPE B, MMF, 15M

CB-M12-M12-MMF20M=

 CABLE, MPO12-MPO12, TRUNK CABLE, TYPE B, MMF, 20M

CB-M12-M12-MMF25M=

 CABLE, MPO12-MPO12, TRUNK CABLE, TYPE B, MMF, 25M

CB-M12-M12-MMF30M=

 CABLE, MPO12-MPO12, TRUNK CABLE, TYPE B, MMF, 30M

LC to LC

CB-LC-LC-MMF1M=

 CABLE, DUPLEX LC-LC PATCH CORD, MMF, 1M

CB-LC-LC-MMF2M=

 CABLE, DUPLEX LC-LC PATCH CORD, MMF, 2M

CB-LC-LC-MMF3M=

 CABLE, DUPLEX LC-LC PATCH CORD, MMF, 3M

CB-LC-LC-MMF4M=

 CABLE, DUPLEX LC-LC PATCH CORD, MMF, 4M

CB-LC-LC-MMF5M=

 CABLE, DUPLEX LC-LC PATCH CORD, MMF, 5M

CB-LC-LC-MMF7M=

 CABLE, DUPLEX LC-LC PATCH CORD, MMF, 7M

Cisco UCS 6536 Fabric Interconnect

43

SUPPLEMENTAL MATERIAL

Table 28  Cisco patch panel solution

CB-LC-LC-MMF10M=

 CABLE, DUPLEX LC-LC PATCH CORD, MMF, 10M

CB-LC-LC-MMF15M=

 CABLE, DUPLEX LC-LC PATCH CORD, MMF, 15M

CB-LC-LC-MMF20M=

 CABLE, DUPLEX LC-LC PATCH CORD, MMF, 20M

CB-LC-LC-MMF25M=

 CABLE, DUPLEX LC-LC PATCH CORD, MMF, 25M

CB-LC-LC-MMF30M=

 CABLE, DUPLEX LC-LC PATCH CORD, MMF, 30M

Refer to Cisco High-Density Fiber Patch Panel, Simplex, MPO and Breakout Cables Portfolio Data Sheet 
for more information.

44

Cisco UCS 6536 Fabric Interconnect

SUPPLEMENTAL MATERIAL

UCS 5108 and X9508 Chassis Connection Types

In a 5108 and X9508 Chassis, Only port-channel mode is supported for connectivity from IOM-2408/2304 to 
FI or IFM-25G to FI or IFM-100G to FIs:

Port Channel Mode

In port channel mode, the FEX fabric links are bundled into a single logical link (see Figure 14) to provide 
higher bandwidth to the servers. Up to 8 links can be port-channeled.

Figure 14

  FEX Fabric Links in Port Channel Mode

Blade Chassis

Blade Half-Width Slot Numbers

Slot 1

Slot 2

Slot 3

Slot 4

Slot 5

Slot 6

Slot 7

Slot 8

Fabric Extender (FEX)

Fabric Interconnect

Cisco UCS 6536 Fabric Interconnect

45

■
TECHNICAL SPECIFICATIONS (s)

TECHNICAL SPECIFICATIONS (s)

Physical and Environmental Specifications

Table 29   Physical and Environmental Specifications

Description

Cisco UCS 6536 FI

Specification

Dimensions (H x W x D)

1.72 in. x 17.3 in x 24.7 in (4.4 cm x 43.9 cm x 62.7 cm)

Weight 
(with two power supplies and fans installed)

25.5 lb (11.6 kg) 

Temperature, operating

32 to 104°F (0 to 40°C)

Temperature, non-operating

-40 to 158°F (-40 to 70°C)

Humidity (RH), non-condensing

5 to 95%

Altitude

0 to 13,123 ft (0 to 4000 m)

For configuration-specific power specifications, use the Cisco UCS Power Calculator at:

https://ucspowercalc.cloudapps.cisco.com/public/index.jsp#eula

46

Cisco UCS 6536 Fabric Interconnect

 
