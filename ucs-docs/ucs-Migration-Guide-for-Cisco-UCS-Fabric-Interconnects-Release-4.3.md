# Migration Guide for Cisco UCS Fabric Interconnects, Release 4.3 - Cisco

| | |
|---|---|
| **URL Title** | Migration Guide for Cisco UCS Fabric Interconnects, Release 4.3 - Cisco |
| **URL** | https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Fabric-Interconnect-Migration/4-3_1/b_migration_guide_for_cisco_ucs_fabric_interconnects_4-3.html |
| **Long URL** |  |
| **HTML Title** | Migration Guide for Cisco UCS Fabric Interconnects, Release 4.3 |
| **Source file** | `ucs-docs-raw/html/b_migration_guide_for_cisco_ucs_fabric_interconnects_4-3.html` |
| **File type** | HTML |
| **Fetched on** | 2026-07-02 13:02:00 |

---

## Page 1: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Fabric-Interconnect-Migration/4-3_1/b_migration_guide_for_cisco_ucs_fabric_interconnects_4-3.html

![Clear Contents of Search](/etc/designs/cdc/fw/i/ic_clear_gray.png)

---

## Page 2: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Fabric-Interconnect-Migration/4-3_1/b_migration_guide_for_cisco_ucs_fabric_interconnects_4-3/m-new-and-changed-information.html

# New and Changed Information

## New and Changed Information for This Release

The following table provides an overview of the changes to this guide for Cisco UCS Manager, Release 4.3.

Table 1. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(6a) Feature  |  Description  |  Where Documented   
---|---|---  
Support for Cisco UCS C-Series and X-Series M8 servers |  Cisco UCS Manager now supports Cisco UCS C240 M8 Server, Cisco UCS C220 M8 Server, and Cisco UCS X210c M8 Compute Node.  |  [Cisco UCS Fabric Interconnect Server Compatibility Matrix - Release 4.3(6b)](m-migrating-and-upgrading-cisco-ucs-hardware-components-for-6500-series-fabric-interconnect_4_3.html#matrix)  
Table 2. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(5a) Feature  |  Description  |  Where Documented   
---|---|---  
Support for Cisco UCS C-Series M8 servers |  Cisco UCS Manager now supports Cisco UCS C225 M8 Server and Cisco UCS X215c M8 Compute Node.  |  [Cisco UCS Fabric Interconnect Server Compatibility Matrix - Release 4.3(6b)](m-migrating-and-upgrading-cisco-ucs-hardware-components-for-6500-series-fabric-interconnect_4_3.html#matrix)  
Table 3. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(4b) Feature  |  Description  |  Where Documented   
---|---|---  
Support for Cisco UCS Fabric Interconnects 9108 100G |  Cisco UCS Manager now supports Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct).  |  [Ports on the Cisco UCS Fabric Interconnects](m_overview-4-1.html#id_118320)  
Table 4. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(4b) Feature  |  Description  |  Where Documented   
---|---|---  
Support for Cisco UCS C-Series M8 servers |  Cisco UCS Manager now supports Cisco UCS C245 M8 Servers.  |  [Cisco UCS Fabric Interconnect Server Compatibility Matrix - Release 4.3(6b)](m-migrating-and-upgrading-cisco-ucs-hardware-components-for-6500-series-fabric-interconnect_4_3.html#matrix)  
Table 5. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(2b) Feature  |  Description  |  Where Documented   
---|---|---  
Migrating Cisco UCS 6400 Series Fabric Interconnects to Cisco UCS 6500 Series Fabric Interconnects |  Cisco UCS Manager supports migration of UCS 6400 series Fabric Interconnects to Cisco UCS 6536 Fabric Interconnect. | 

  * [Cisco UCS 6400 Series Fabric Interconnect Migration Considerations](m-migrating-and-upgrading-cisco-ucs-hardware-components-for-6500-series-fabric-interconnect_4_3.html#concept_vxm_lxc_zdb)
  * [Validating Feature Configurations for Cisco UCS 6536 before Upgrade](m-migrating-and-upgrading-cisco-ucs-hardware-components-for-6500-series-fabric-interconnect_4_3.html#Cisco_Concept.dita_b1378d74-eba6-45d0-86c5-e5013b19d78d)
  * [Migrating from UCS 6400 Series Fabric Interconnects to UCS 6536 Fabric Interconnects](m-migrating-and-upgrading-cisco-ucs-hardware-components-for-6500-series-fabric-interconnect_4_3.html#task_i25_zkc_zdb)

  
Migrating Cisco UCS 6400 Series Fabric Interconnects to Cisco UCS 6500 Series Fabric Interconnects with UCS Central |  Cisco UCS Manager supports migration of UCS 6400 series Fabric Interconnects to Cisco UCS 6536 Fabric Interconnects with UCS Central.  | 

  * [Considerations for migrating Cisco UCS 6400 Series Fabric Interconnects to Cisco UCS 6500 Series Fabric Interconnects with Cisco UCS Central](m-migrating-and-upgrading-cisco-ucs-hardware-components-for-6500-series-fabric-interconnect_4_3.html#considerations-for-6454-fi-to-64108-fi-migration-with-ucs-central)
  * [Validating Feature Configurations for Cisco UCS 6536 before Upgrade](m-migrating-and-upgrading-cisco-ucs-hardware-components-for-6500-series-fabric-interconnect_4_3.html#Cisco_Concept.dita_b1378d74-eba6-45d0-86c5-e5013b19d78d)
  * [Migrating from UCS 6400 Series Fabric Interconnects to UCS 6536 Fabric Interconnects](m-migrating-and-upgrading-cisco-ucs-hardware-components-for-6500-series-fabric-interconnect_4_3.html#task_i25_zkc_zdb)


---

## Page 3: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Fabric-Interconnect-Migration/4-3_1/b_migration_guide_for_cisco_ucs_fabric_interconnects_4-3/m_overview-4-1.html

# Overview of Cisco UCS Fabric Interconnects  
  
Cisco UCS 6500 Series Fabric Interconnects

##  Cisco UCS 6536 Fabric Interconnect Overview 

The Cisco UCS 6536 Fabric Interconnect is a core part of the Cisco Unified Computing System, providing both network connectivity and management capabilities for the system. The Cisco UCS 6536 Fabric Interconnect provides the communication backbone and management connectivity for UCS B-series blade servers and UCS C-series rack servers. 

Cisco UCS 6500 Series Fabric Interconnects currently include Cisco UCS 6536 Fabric Interconnect. All servers attached to a Cisco UCS 6536 Fabric Interconnect become part of a single, highly available management domain. In addition, by supporting a unified fabric, Cisco UCS 6536 Fabric Interconnect provides both LAN and SAN connectivity for all servers within its domain. 

The Cisco UCS 6536 Fabric Interconnect supports multiple traffic classes over a lossless Ethernet fabric from the server through the fabric interconnect. 

## **Cisco UCS 6536 Fabric Interconnect**

The Cisco UCS 6536 Fabric Interconnect (UCSC-FI-6536) is a One-rack unit (1RU), top of rack (TOR), fixed-port data center platform that provides both network connectivity and management capabilities to the Cisco UCS system. 

The fabric interconnect can provide Ethernet and Fibre Channel connectivity to the servers in the system. The servers connect to the fabric interconnect, and then to the LAN or SAN. 

Cisco UCS Manager on UCS 6536 Fabric Interconnect supports Cisco UCS X-Series Compute Nodes, B-Series Blade Servers and C-Series Rack Servers, Cisco UCS S-Series Storage Servers, as well as the associated storage resources and networks. 

High availability and redundancy can be achieved by connecting a pair of fabric interconnects to each other through L1 or L2 ports in cluster mode configuration. 

Each Cisco UCS 6536 Fabric Interconnect offers the following features: 

  * Thirty-six QSFP28 ports capable of 100G including 4 unified ports (33-36). Ports also support: 

  * Autonegotiating with peer devices to speeds of 100G, 40G, 25G, 10G, and 1G.

  * Port breakout is supported for Ethernet ports (1-32) and Unified ports (33-36). 

  * Ethernet breakout is supported on switch ports 1 through 36 when each port is configured with a breakout cable. 

  * The Dynamic Ethernet Breakout feature enables converting a standard Ethernet port to a breakout port on-the-fly so that you do not need to reboot the Fabric Interconnect. Dynamic Ethernet Breakout also supports converting breakout ports back to a standard Ethernet port without a reboot. 

  * FC breakout is supported on ports 33 through 36 wherein each port is configured with a four-port breakout cable. For example 1/33/1, 1/33/2, 1/33/3, and 1/33/4 are the four FC breakout ports on the physical port 33. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Fibre Channel support is only available through the configuration of Unified Ports (33-36) as FC breakout port.

* * *  
  
---|---  
  * FC breakout ports support peer communication at fixed speeds of 8Gbs, 16 Gbps, and 32 Gbps. 

  * All four FC breakout ports must be configured with the same speed. Mixed speeds on a QSFP port's FC breakout ports are not supported. 

  * Using breakout ports enables the fabric interconnect to support the maximum 16 FC ports supported by Fibre Channel.

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

  * Converting from Ethernet to FC breakout ports, or FC breakout ports back to Ethernet, requires a reboot/reload after changing the breakout type. 
  * FCoE storage ports are not supported. 

* * *  
  
---|---  
  * One management port (one 10/100/1000BASE-T port)

  * Two L1/L2 Ethernet RJ-45 ports for high availability or cluster configurations. Ethernet ports support 10/100/1000Mb speed.

  * One console port (RS-232)

  * One USB 3.0 port

  * CPU: 4 Core, 1.8GHz, Intel 5th-Generation core processor

  * Memory: 

  * 32 GB DDR4 DIMMs

  * 128 GB M.2 SSD Flash Drive

  * 32 GB Boot Flash (16 MB primary, and 16 MB standby/golden)


This fabric interconnect includes the following user-replaceable components:

  * Fan modules (6), each is a port-side exhaust fan module with dark grey latch coloring (UCS-FAN-6536).

  * Power supply modules (2). One power supply module (PSU) is the active module for operations, and the second PSU is the standby for redundancy [1+1]) with the following choices: 

  * 1100-W AC power supply with dark grey latch coloring (UCS-PSU-6536-AC)

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

All fan modules and power supplies must use the same airflow direction.

* * *  
  
---|---  


The following figure shows the fabric interconnect features on the port side of the chassis. 

![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540351.jpg) 1  |  LEDs  |  3  |  36 40/100-Gigabit QSFP28 ports  
---|---|---|---  
2  |  Lane Select button  |  |   
  
To determine which transceivers, adapters, and cables are support the fabric interconnect, see the [Cisco Transceiver Modules Compatibility Information](http://www.cisco.com/c/en/us/support/interfaces-modules/transceiver-modules/products-device-support-tables-list.html) document. 

The following figure shows the fabric interconnect features on the power supply side of the chassis. 

![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540354.jpg) 1  |  Power supply modules (1 or 2) (AC power supplies shown) with slots numbered 1 (left) and 2 (right). |  2  |  Fan modules (6) with slots numbered from 1 (left) to 6 (right).  
---|---|---|---  
3  |  Layer 2 (L2) Ethernet port, 10/100/100Mb autonegotiating. Supports high availability (HA) or clustering through an RJ-45 port. |  4  |  Layer 1 (L1) Ethernet port, 10/100/100Mb autonegotiating.  Supports high availability (HA) or clustering through an RJ-45 port.  
5 |  Ethernet network management port (RJ45), 10/100/1000Mb autonegotiating  |  6  |  Serial Console port (RJ45), 9600 baud.  
7 |  USB 3.0/2.0 port Supports booting the system and downloading scripts. |  8 |  Beacon (BCN) LED  
9 |  Status (STS) LED |  - |   
  
The following figure shows the side of the chassis. 

![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540353.jpg) 1  |  Screw holes for mounting brackets |  2  |  Grounding pad  
---|---|---|---  
  
Plan to position the ports in a hot aisle so that fans and power supplies intake air from the cold aisle, blow the cool air through the fabric interconnect, and exhaust the heated air into the hot aisle. 

The fan and power supply modules are field replaceable. You can replace one fan module or one power supply module during operations so long as the other modules are installed and operating. If you have only one power supply installed, you can install the replacement power supply in the open slot before removing the original power supply. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

All fan and power supply modules must have the same direction of airflow. Otherwise, the fabric interconnect can overheat and shut down. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Because fans and power supply modules have port-side exhaust airflow (blue coloring for fan modules), you must locate the ports in the hot aisle. If you locate the air intake in a hot aisle, the fabric interconnect can overheat and shut down. 

* * *  
  
---|---  
  
Cisco UCS 6400 Series Fabric Interconnects

## Cisco UCS 6400 Series Fabric Interconnect Overview 

Cisco UCS 6400 Series Fabric Interconnect provides both network connectivity and management capabilities to the Cisco UCS system. The fabric interconnect provides Ethernet and Fibre Channel to the servers in the system, the servers connect to the fabric interconnect, and then to the LAN or SAN. 

Each Cisco UCS 6400 Series Fabric Interconnect runs Cisco UCS Manager to fully manage all Cisco UCS elements. The fabric interconnect supports 10/25 Gigabit ports in the fabric with 40/100 Gigabit uplink ports. High availability can be achieved when a Cisco UCS 6400 Series Fabric Interconnect is connected to another Cisco UCS 6400 Series Fabric Interconnect through the L1 or L2 port on each device. 

Cisco UCS 6400 Series Fabric Interconnect consists of: 

  * Cisco UCS 6454 Fabric Interconnects 

  * Cisco UCS 64108 Fabric Interconnects 


The Cisco UCS 6400 Series fabric interconnect supports Cisco UCS B-Series Blade Servers, UCS 5108 B-Series Server Chassis, C-Series Rack Servers, and UCS S-Series Storage Servers. 

## Cisco UCS 64108 Fabric Interconnect

The Cisco UCS 64108 Fabric Interconnect is a 2 RU top-of-rack (TOR) switch that mounts in a standard 19-inch rack such as the Cisco R Series rack. 

The high-density Cisco UCS 64108 Fabric Interconnect has 96 10/25 Gb SFP28 ports and 12 40/100 Gb QSFP28 ports. Each 40/100 Gb port can break out into 4 x 10/25 Gb uplink ports. Ports 1 - 16 are unified ports that support 10/25 GbE or 8/16/32G Fibre Channel speeds. Ports 89-96 support 1Gbps Ethernet speeds. 

The Cisco UCS 64108 Fabric Interconnect supports either: 

  * Eight FCoE port channels

  * Or Four SAN port channels

  * or Four SAN port channels and four FCoE port channels


The Cisco UCS 64108 Fabric Interconnect also has one network management port, one RS-232 serial console port for setting the initial configuration, and one USB port for saving or loading configurations. The FI also includes L1/L2 ports for connecting two fabric interconnects in a high-availability configuration. 

The Cisco UCS 64108 Fabric Interconnect also contains a CPU board that consists of: 

  * Intel Xeon Processor, 6 core

  * 64 GB of RAM 

  * 8 MB of NVRAM (4 x NVRAM chips)

  * 128 GB SSD (bootflash)


Figure 1. Cisco UCS 64108 Fabric Interconnect Rear View ![](/c/dam/en/us/td/i/300001-400000/300001-310000/307001-308000/307644.jpg) 1  |  Ports 1-16  Unified ports:

  * 10/25 Gbps Ethernet or FCoE
  * 8/16/32 Gbps Fibre Channel

|  2  |  Ports 17-88 (10/25 Gbps Ethernet or FCoE)  
---|---|---|---  
3  |  Ports 89-96

  * 10/25 Gbps Ethernet or FCoE
  * 1 Gbps Ethernet

|  4 |  Uplink Ports 97-108 (40/100 Gbps Ethernet or FCoE) Each of these ports can be 4 x 10/25 Gbps Ethernet or FCoE uplink ports when using a breakout cable.  
5 |  System environment (fan fault) LED |  6 |  System status LED  
7 |  Beacon LED |  |   
  
The Cisco UCS 64108 Fabric Interconnect has two power supplies (redundant as 1+1) and three fans (redundant as 2+1). 

Figure 2. Cisco UCS 64108 Fabric Interconnect Front View ![](/c/dam/en/us/td/i/300001-400000/300001-310000/307001-308000/307645.jpg) **1** |  Cooling fans (hot swappable, 2+1 redundancy) |  **2** |  RS-232 serial console port (RJ-45 connector)  
---|---|---|---  
**3** |  Network management port (RJ-45 connector) |  4 |  USB port  
5 |  Grounding pad for two-hole grounding lug (under protective label) |  6 |  Power supplies Two identical AC or DC PSUs, hot-swappable, 1+1 redundancy)  
7 |  L1/L2 high-availability ports (RJ-45 connector) |  8 |  Beacon LED  
9 |  System status LED |  |   
  
## Cisco UCS 6454 Fabric Interconnect

The Cisco UCS 6454 Fabric Interconnect (FI) is a 1-RU top-of-rack switch that mounts in a standard 19-inch rack such as the Cisco R Series rack. 

The Cisco UCS 6454 Fabric Interconnect has 48 10/25 Gb SFP28 ports (16 unified ports) and 6 40/100 Gb QSFP28 ports. Each 40/100 Gb port can break out into 4 x 10/25 Gb uplink ports. The sixteen unified ports support 10/25 GbE or 8/16/32G Fibre Channel speeds. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The Cisco UCS 6454 Fabric Interconnect supported 8 unified ports (ports 1 - 8) with Cisco UCS Manager 4.0(1) and 4.0(2), but with release 4.0(4) and later it supports 16 unified ports (ports 1 - 16). 

* * *  
  
---|---  
  
The Cisco UCS 6454 Fabric Interconnect supports: 

  * Maximum of 8 FCoE port channels

  * Or 4 SAN port channels

  * Or a maximum of 8 SAN port channels and FCoE port channels (4 each)


The Cisco UCS 6454 Fabric Interconnect also has one network management port, one console port for setting the initial configuration, and one USB port for saving or loading configurations. The FI also includes L1/L2 ports for connecting two fabric interconnects for high availability. 

The Cisco UCS 6454 Fabric Interconnect also contains a CPU board that consists of: 

  * Intel Xeon D-1528 v4 Processor, 1.6 GHz

  * 64 GB of RAM 

  * 8 MB of NVRAM (4 x NVRAM chips)

  * 128 GB SSD (bootflash)


Figure 3. Cisco UCS 6454 Fabric Interconnect Rear View ![](/c/dam/en/us/td/i/300001-400000/300001-310000/306001-307000/306755.jpg) 1  |  Ports 1-16 (Unified Ports 10/25 Gbps Ethernet or FCoE or 8/16/32 Gbps Fibre Channel) |  **Note** |  When using Cisco UCS Manager releases earlier than 4.0(4), only ports 1-8 are Unified Ports.  
---|---  
2  |  Ports 17-44 (10/25 Gbps Ethernet or FCoE) |  **Note** |  When using Cisco UCS Manager releases earlier than 4.0(4), ports 9-44 are 10/25 Gbps Ethernet or FCoE.  
---|---  
3  |  Ports 45-48 (1/10/25 Gbps Ethernet or FCoE)  |  4 |  Uplink Ports 49-54 (40/100 Gbps Ethernet or FCoE) Each of these ports can be 4 x 10/25 Gbps Ethernet or FCoE uplink ports when using an appropriate breakout cable.  
  
The Cisco UCS 6454 Fabric Interconnect chassis has two power supplies and four fans. Two of the fans provide front to rear airflow. 

Figure 4. Cisco UCS 6454 Fabric Interconnect Front View ![](/c/dam/en/us/td/i/300001-400000/300001-310000/306001-307000/306354.jpg) **1** |  Power supply and power cord connector  |  **2** |  Fans 1 through 4, numbered left to right, when facing the front of the chassis.  
---|---|---|---  
**3** |  L1 port, L2 port, RJ45, console, USB port, and LEDs |  |   
  
## Ports on the Cisco UCS Fabric Interconnects

Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct) has eight ports that include: 

  * Ports 1 & 2 that are unified ports to manage all SAN features and configurations.

  * The 100G Ethernet ports [1-8] can also be configured as 25Gx4 SFP28 compatible breakout ports or 4x10G ports, offering flexible networking solutions to accommodate a range of data center needs. 

  * The 32G Fibre Channel ports [1 & 2] can also be configured as 8Gx4 SFP28 compatible breakout ports offering flexible networking solutions to accommodate a range of data center needs. 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Migration of any previous generation Fabric Interconnects to the Cisco UCS 9108 100G Intelligent Fabric Module is currently not supported. 

* * *  
  
---|---  
  
Ports on the Cisco UCS 6536 Fabric Interconnects can be configured to carry either Ethernet or Fibre Channel traffic. You can configure only ports 33-36 to carry Fibre Channel traffic. The ports cannot be used by a Cisco UCS domain until you configure them. 

Ports on the Cisco UCS 6400 Series Fabric Interconnects can be configured to carry either Ethernet or Fibre Channel traffic. You can configure only ports 1-16 to carry Fibre Channel traffic. The ports cannot be used by a Cisco UCS domain until you configure them. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

  * The Cisco UCS 6454 Fabric Interconnect supported 8 unified ports (ports 1 - 8) with Cisco UCS Manager 4.0(1) and 4.0(2), but with Release 4.0(4) and later releases, it supports 16 unified ports (ports 1 - 16).  When you configure a port on a Fabric Interconnect, the administrative state is automatically set to enabled. If the port is connected to another device, this may cause traffic disruption. The port can be disabled and enabled after it has been configured. 


* * *  
  
---|---  
  
The following table summarizes the port support for third, fourth, fifth generation of Cisco UCS Fabric Interconnects, and Cisco UCS Fabric Interconnects 9108 100G.

|  Third Generation  |  Fourth Generation |  Fifth Generation |  Cisco UCS X-Series Direct  
---|---|---|---|---  
Item  |  Cisco UCS 6332  |  Cisco UCS 6332-16UP  |  Cisco UCS 6454 |  Cisco UCS 64108 |  Cisco UCS 6536 |  Cisco UCS 9108 100G FI  
Description  |  32-Port Fabric Interconnect  |  40-Port Fabric Interconnect  |  54-Port Fabric Interconnect  |  108-Port Fabric Interconnect |  36-Port Fabric Interconnect |  8 Ports  
Form factor  |  1 RU  |  1 RU  |  1 RU  |  2 RU |  1 RU |  1 RU  
Number of fixed 10 GB Interfaces  |  96 (40G to 4 x 10G breakout cables), QSA, Port 13 and 14 do not support 40G to 10G breakout  |  88 (40G to 4 x 10G breakout cables)  |  48 10G/25G interfaces |  96 10G/25G interfaces |  36 10G/25G/40G/100G interfaces |  **Note** |  144 breakout ports (36x4)  
---|---  
—   
Number of Unified Ports |  —  |  16  |  16 This FI supported 8 unified ports (ports 1 - 8) with Cisco UCS Manager 4.0(1) and 4.0(2), but with Release 4.0(4) and later it supports 16 unified ports (ports 1 - 16).  |  16 ports 1-16 |  4 |  **Note** |  16 breakout ports (4x4)  
---|---  
Ports 1-2  
Unified Port Speeds in Gbps |  —  |  1G/10G or 4G/8G/16G-FC  |  10G/25G or 8G/16G/32G-FC  |  10G/25G or 8G/16G/32G-FC |  10G/25G/40G/100G FC |  8G/16G/32G FC  
Number of 40-Gbps ports  |  32  |  24  |  6 40G/100G  |  12 40G/100G  |  36 |  —   
Unified Port Range  |  None  |  Ports 1-16  |  Ports 1-16  |  Ports 1-16  |  Ports 33-36 |  Ports 1-2  
Compatibility with the IOM  |  UCS 2204, UCS 2208, UCS 2304, UCS 2304V2 |  UCS 2204, UCS 2208, UCS 2304, UCS 2304V2 |  UCS 2204, UCS 2208, UCS 2408 |  UCS 2204, UCS 2208, UCS 2408 |  UCS 2408, UCS 2304, UCS 2304V2 |  —   
Compatibility with the FEX |  Cisco Nexus 2232PP Cisco Nexus 2232TM-E Cisco Nexus 2348UPQ |  Cisco Nexus 2232PP Cisco Nexus 2232TM-E Cisco Nexus 2348UPQ |  Cisco Nexus 2232PP Cisco Nexus 2232TM-E Cisco Nexus 93180YC-FX3 |  Cisco Nexus 2232PP Cisco Nexus 2232TM-E Cisco Nexus 93180YC-FX3 |  Cisco Nexus 93180YC-FX3 N2K-C2348UPQ |  —   
Expansion Slots  |  None  |  None  |  None  |  None |  None |  —   
Fan Modules  |  4  |  4  |  4 |  3 |  6 |  3  
Power Supplies  |  2 (AC/DC)  |  2 (AC/DC)  |  2 (AC/DC)  |  2 (AC/DC)  |  2 (AC) |  Supplied by chassis

---

## Page 4: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Fabric-Interconnect-Migration/4-3_1/b_migration_guide_for_cisco_ucs_fabric_interconnects_4-3/m-migrating-and-upgrading-cisco-ucs-hardware-components-for-6500-series-fabric-interconnect_4_3.html

# Migrating to Cisco UCS 6500 Series Fabric Interconnects  
  
## Cisco UCS Fabric Interconnect Server Compatibility Matrix - Release 4.3(6b)

### Cisco UCS 6536 FI

Table 1. Cisco UCS 6536 FI - Cisco UCS Rack Servers Cisco VIC |  Direct Attach  (40/100G) |  Direct Attach  (4x25G or 25G QSA28) |  FEX  
---|---|---|---  
93180YC-FX3  (25G server ports) |  93180YC-FX3  (10G server ports) |  2348 UPQ  (10G server ports)  
15427 (UCSC-M-V5Q50GV2) |  Not Supported  |  All Cisco UCS C-Series M8, M7, and M6 servers. |  **Note** |  Reverse breakout is not supported.  
---|---  
All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M8, M7, and M6 servers.  
15237 (UCSC-M-V5D200GV2) |  All Cisco UCS C-Series M8, M7, and M6 servers. |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
15235 (UCSC-P-V5D200G)  |  All Cisco UCS C-Series M8, M7, and M6 servers. |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
15238 (UCSC-M-V5D200G)  |  All Cisco UCS C-Series M6 and M7 servers  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
15425 (UCSC-P-V5Q50G) |  Not Supported |  All Cisco UCS C-Series M8, M7, and M6 servers. |  **Note** |  No reverse breakout supported   
---|---  
All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M8, M7, and M6 servers.  
15428 (UCSC-M-V5Q50G)  |  Not Supported |  All Cisco UCS C-Series M6 and M7 servers  |  **Note** |  No reverse breakout supported   
---|---  
All Cisco UCS C-Series M6 and M7 servers  |  All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M6 and M7 servers   
1497-40G/100G (UCSC-MLOMC100-04)  |  All Cisco UCS C-series M5 servers. |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
1495-40G/100G (UCSC-PCIEC100-04)  |  All Cisco UCS C-Series M6, C-Series M5, and S-series M5 servers  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
1477-40G/100G (UCSC-MV100-04)  |  All Cisco UCS C-series M6 servers. |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
1467-10G/25G (UCSC-MV25-04)  |  Not Supported  |  All Cisco UCS C-Series M6 servers |  All Cisco UCS C-Series M6 servers |  All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M6 servers  
1457-10G/25G (UCSC-MLOMC25Q-04)  |  Not Supported  |  All Cisco UCS C-series M5 servers. |  All Cisco UCS C-series M5 servers. |  All Cisco UCS C-series M5 servers. |  All Cisco UCS C-series M5 servers.  
1455-10G/25G (UCSC-PCIEC25Q-04)  |  Not Supported  |  All Cisco UCS C-Series M6 and M5, and S-Series M5 servers. |  All Cisco UCS C-Series M6 and M5, and S-Series M5 servers. |  All Cisco UCS C-Series M6 and M5, and S-Series M5 servers. |  All Cisco UCS C-Series M6 and M5, and S-Series M5 servers.  
1387 - 40G (UCSC-MLOM-C40Q-03)  |  All Cisco UCS C-Series M5 Servers (40G)  |  Not Supported  |  Not Supported  |  All Cisco UCS C-Series M5 servers with QSA and SFP-10G-SR/LR, SFP-H10GB-CU1/3/5M, SFP-H10GB-ACU7M only. |  All Cisco UCS C-Series M5 servers with QSA and SFP-10G-SR only.  
1385 - 40G (UCSC-PCIE-C40Q-03)  |  All Cisco UCS C-Series M5 Servers (40G)  |  Not Supported  |  Not Supported  |  All Cisco UCS C-Series M5 servers with QSA and SFP-10G-SR/LR, SFP-H10GB-CU1/3/5M, SFP-H10GB-ACU7M only. |  All Cisco UCS C-Series M5 servers with QSA and SFP-10G-SR only.  
Table 2. Cisco UCS 6536 FI - Cisco UCS Blade Servers Cisco VIC |  IOM  
---|---  
2304v1/v2 & /2408 |  UCSX-I-9108-25G or UCSX-I-9108-100G  
15230 (UCSX-ML-V5D200GV2) |  - |  Cisco UCS X210c M8 Cisco UCS X215c M8 Cisco UCS X210c M6, X210c M7, and X410c M7  
15420 + UCS VIC 15000 bridge connector + 15422 (UCSX-ML-V5Q50G + UCSX-V5-BRIDGE + UCSX-ME-V5Q50G) |  \-  |  Cisco UCS X210c M8 Cisco UCS X215c M8 Cisco UCS X210c M6, X210c M7, and X410c M7  
15420 (UCSX-ML-V5Q50G)  |  \-  |  Cisco UCS X210c M8 Cisco UCS X215c M8 Cisco UCS X210c M6, X210c M7, and X410c M7  
15231 (UCSX-ML-V5D200G)  |  \-  |  Cisco UCS X210c M6, X210c M7, and X410c M7  
14425 + UCS VIC 14000 bridge connector + 14825 (UCSX-V4-Q25GML + UCSX-V4-BRIDGE + UCSX-V4-Q25GME) |  \-  |  Cisco UCS X210c M6   
14425 (UCSX-V4-Q25GML)  |  \-  |  Cisco UCS X210c M6   
15411 + Port Expander (UCSB-ML-V5Q10G + UCSB-MLOM-PT-01)  |  Cisco UCS B200 M6  |  \-   
15411 (UCSB-ML-V5Q10G)  |  Cisco UCS B200 M6  |  \-   
1440 + 1480 + Port Expander (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P + UCSB-MLOM-PT-01) |  Cisco UCS B480 M5  |  \-   
1440 + 1480 + 1480 (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P +UCSB-VIC-M84-4P)  |  Cisco UCS B480 M5  |  \-   
1440 + 1480 (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P)  |  Cisco UCS B200 M6, B200 M5, B480 M5  |  \-   
1440 + Port Expander (UCSB-MLOM-40G-04 + UCSB-MLOM-PT-01)  |  Cisco UCS B200 M6, B200 M5, B480 M5  |  \-   
1440 (UCSB-MLOM-40G-04)  |  Cisco UCS B200 M6, B200 M5, B480 M5  |  \-   
1340 + 1380 + Port Expander (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P + UCSB-MLOM-PT-01) |  Cisco UCS B480 M5  |  \-   
1340 + 1380 + 1380 (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P + UCSB-VIC-M83-8P) |  Cisco UCS B480 M5  |  \-   
1340 + 1380 (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P)  |  Cisco UCS B200 M5 and B480 M5  |  \-   
1340 + Port Expander - 10G/40G (UCSB-MLOM-40G-03 + UCSB-MLOM-PT-01)  |  Cisco UCS B200 M5 and B480 M5  |  \-   
1340 - 10G/40G (UCSB-MLOM-40G-03)  |  Cisco UCS B200 M5 and B480 M5  |  \-   
  
### Cisco UCS 6400 and 64108 FIs

Table 3. Cisco UCS 6400 and 64108 FIs - Cisco UCS Rack Servers Cisco VIC |  Direct Attach  (10G/25G)  |  Direct Attach  (4x10G/4x25)  |  Direct Attach  (40G/100G)  |  FEX  
---|---|---|---|---  
2232 PP (10G)  |  93180YC-FX3  (25G server ports)  |  93180YC-FX3  (10G server ports)   
15427 (UCSC-M-V5Q50GV2) |  All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M8, M7, and M6 servers. |  Not Supported |  Not Supported |  All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M8, M7, and M6 servers with SFP-10G-SR/SR-S only.  
15237 (UCSC-M-V5D200GV2) |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
15235 (UCSC-P- V5D200G) |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
15238 (UCSC-M -V5D200G)  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
15425 (UCSC-P- V5Q50G) |  All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M8, M7, and M6 servers. |  Not Supported  |  Not Supported  |  All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M8, M7, and M6 servers with SFP-10G-SR/SR-S only.  
15428 (UCSC-M -V5Q50G)  |  All Cisco UCS C-Series M6 and M7 servers. |  All Cisco UCS C-Series M6 and M7 servers. |  Not Supported  |  Not Supported  |  All Cisco UCS C-Series M6 and M7 servers. |  All Cisco UCS C-Series M8, M7, and M6 servers with SFP-10G-SR/SR-S only.  
|  **Note** |  Break-out is supported (6400 side QSFP, on adapter side two ports can be connected to 1 VIC ( like ports 1 and 2) Reverse-breakout : Not supported  
---|---  
1495-40G/100G  (UCSC -PCIEC100 -04)  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
1497-40G/100G  (UCSC -MLOMC100 -04)  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
1477-40G/100G  (UCSC-MV100 -04)  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
1467-10G/25G (UCSC -MV25-04)  |  All Cisco UCS C-Series M6 servers. |  All Cisco UCS C-Series M6 servers. |  Not Supported  |  All Cisco UCS C-Series M6 servers. |  All Cisco UCS C-Series M6 servers. |  All Cisco UCS C-Series M6 servers with SFP-10G-SR/SR-S only.  
1457-10G/25G (UCSC-MLOM C25Q-04)  |  All Cisco UCS C-Series M5 servers. |  All Cisco UCS C-Series M5 servers. |  Not Supported  |  All Cisco UCS C-Series M5 servers. |  All Cisco UCS C-Series M5 servers. |  All Cisco UCS C-Series M5 servers with SFP-10G-SR/SR-S only.  
1455-10G/25G  (UCSC-PCIEC 25Q-04)  |  All Cisco UCS C-Series M6 and M5, and S-Series M5 servers. |  All Cisco UCS C-Series M6 and M5, and S-Series M5 servers. |  Not Supported  |  All Cisco UCS C-Series M6 and M5, and S-Series M5 servers. |  All Cisco UCS C-Series M6 and M5, and S-Series M5 servers. |  All Cisco UCS C-Series M6 and M5, and S-Series M5 servers with SFP-10G-SR/SR-S only.  
1387 - 40G  (UCSC-MLOM -C40Q-03)  |  All Cisco UCS C-Series M5 servers with QSA at adapter. |  Not Supported  |  Not Supported  |  All Cisco UCS C-Series M5 servers with QSA at adapter. |  Not Supported  |  All Cisco UCS C-Series M5 servers  with QSA and SFP-10G-SR/LR, SFP-H10GB-CU1/3/5M, or SFP-H10GB-ACU7M only.  
1385 - 40G  (UCSC-PCIE -C40Q-03)  |  All Cisco UCS C-Series M5 except C125 M5 and S-Series M5 servers  with QSA at the adapter. |  Not Supported  |  Not Supported  |  All Cisco UCS C-Series M5 except C125 M5 and S-Series M5 servers  with QSA at the adapter. |  Not Supported  |  All Cisco UCS C-Series M5 except C125 M5 and S-Series M5 servers  with QSA and SFP-10G-SR/LR, SFP-H10GB-CU1/3/5M, or SFP-H10GB-ACU7M only.  
Table 4. Cisco UCS 6400 and 64108 FIs - Cisco UCS Blade Servers Cisco VIC |  IOM  
---|---  
2204/2208/2408 |  UCSX-I-9108-25G  
15230 (UCSX-ML-V5D200GV2) |  Not Supported  |  Cisco UCS X210c M8 Cisco UCS X215c M8 Cisco UCS X210c M6, X210c M7, and X410c M7  
15420 +  UCS VIC 15000 bridge connector +  (15422 (UCSX-ML-V5Q50G + UCSX-V5-BRIDGE + UCSX-ME-V5Q50G) |  Not Supported  |  Cisco UCS X210c M8 Cisco UCS X215c M8 Cisco UCS X210c M6, X210c M7, and X410c M7  
15420  (UCSX-ML-V5Q50G) |  Not Supported  |  Cisco UCS X210c M8 Cisco UCS X215c M8 Cisco UCS X210c M6, X210c M7, and X410c M7  
15231  (UCSX-ML-V5D200G) |  Not Supported  |  Cisco UCS X210c M6, X210c M7, and X410c M7  
14425 +  UCS VIC 14000 bridge connector + (14825 (UCSX-V4-Q25GML + UCSX-V4-BRIDGE + UCSX-V4-Q25GME) |  Not Supported  |  Cisco UCS X210c M6  
14425  (UCSX-V4-Q25GML) |  Not Supported  |  Cisco UCS X210c M6  
15411 + Port Expander (UCSB-ML -V5Q10G + UCSB-MLOM -PT-01)  |  B200 M6  |  Not Supported   
15411 (UCSB-ML -V5Q10G)  |  B200 M6  |  Not Supported   
1440 + 1480 + Port Expander  (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P + UCSB-MLOM-PT-01) |  Cisco UCS B480 M5  |  Not Supported   
1440 + 1480 + Port Expander  (UCSB-MLOM-40G-04 +  UCSB-VIC- M84-4P) +  UCSB-MLOM-PT-01) |  Cisco UCS B480 M5  |  Not Supported   
1440 + 1480  (UCSB-MLOM-40G-04 +  UCSB-VIC-M84-4P)  |  Cisco UCS B200 M6, B200 M5, B480 M5  |  Not Supported   
1440 + Port Expander  (UCSB-MLOM-40G-04 +  UCSB-MLOM-PT-01)  |  Cisco UCS B200 M6, B200 M5, B480 M5  |  Not Supported   
1440  (UCSB-MLOM-40G-04)  |  Cisco UCS B200 M6, B200 M5, B480 M5  |  Not Supported   
1340 + 1380 + 1380  (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P + UCSB-VIC-M83-8P) |  Cisco UCS B480 M5  |  Not Supported  
1340 + 1380 + Port Expander  (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P + UCSB-MLOM-PT-01) |  Cisco UCS B480 M5  |  Not Supported  
1340 + Port Expander - 10G/40G  (UCSB-MLOM-40G-03 +  UCSB-MLOM-PT-01)  |  Cisco UCS B200 M5 and B480 M5  |  Not Supported  
1340 + 1380  (UCSB-MLOM-40G-03 +  UCSB-VIC-M83-8P)  |  Cisco UCS B200 M5 and B480 M5  |  Not Supported  
1340 - 10G/40G (UCSB-MLOM-40G-03)  |  Cisco UCS B200 M5 and B480 M5  |  Not Supported  
  
### Cisco UCS 6300 FI

Table 5. Cisco UCS 6300 FI - Cisco UCS Rack Servers Cisco VIC |  Direct Attach |  Direct Attach  (Break-out) |  FEX  
---|---|---|---  
2232 PP |  2348  
15427 (UCSC-M-V5Q50GV2) |  All Cisco UCS C-Series M6 servers. |  All Cisco UCS C-Series M6 servers. |  Not Supported  |  All Cisco UCS C-Series M6 servers.  
15237 (UCSC-M-V5D200GV2) |  All Cisco UCS C-Series M6 servers. |  Not Supported  |  Not Supported  |  Not Supported   
15235 (UCSC-P-V5D200G) |  All Cisco UCS C-Series M6 servers. |  Not Supported  |  Not Supported  |  Not Supported   
15425 (UCSC-P-V5Q50G) |  All Cisco UCS C-Series M6 servers. |  All Cisco UCS C-Series M6 servers. |  Not Supported  |  All Cisco UCS C-Series M6 servers.  
15428 (UCSC-M-V5Q50G)  |  All Cisco UCS C-Series M6 servers. |  All Cisco UCS C-Series M6 servers. |  Not Supported  |  All Cisco UCS C-Series M6 servers.  
15238 (UCSC-M-V5D200G)  |  All Cisco UCS C-Series M6 servers. |  Not Supported  |  Not Supported  |  Not Supported   
1497-40G/100G (UCSC-MLOMC100-04)  |  All Cisco UCS C-Series M5 servers. |  Not Supported  |  Not Supported  |  Not Supported   
1495-40G/100G (UCSC-PCIEC100-04)  |  All Cisco UCS C-Series M6, M5, and S-Series M5 servers. |  Not Supported  |  Not Supported  |  Not Supported   
1477-40G/100G (UCSC-MV100-04)  |  All Cisco UCS C-Series M6 servers. |  Not Supported  |  Not Supported  |  Not Supported   
1467-10G/25G (UCSC-MV25-04)  |  All Cisco UCS C-Series M6 servers (10G speed with 6332-16UP). |  All Cisco UCS C-Series M6 servers. |  All Cisco UCS C-Series M6 servers. |  All Cisco UCS C-Series M6 servers.  
1457-10G/25G (UCSC-MLOMC25Q-04)  |  Cisco UCS C220 M5 and C240 M5 (10G speed with 6332-16UP). |  Cisco UCS C220 M5 and C240 M5 servers. |  Cisco UCS C220 M5 and C240 M5 servers. |  Cisco UCS C220 M5 and C240 M5 servers.  
1455-10G/25G (UCSC-PCIEC25Q-04)  |  All Cisco UCS C-Series M6, M5, and S-Series M5 servers (10G speed with 6332-16UP). |  All Cisco UCS C-Series M6, M5, and S-Series M5 servers. |  All Cisco UCS C-Series M6, M5, and S-Series M5 servers. |  All Cisco UCS C-Series M6, M5, and S-Series M5 servers.  
1387 - 40G (UCSC-MLOM-C40Q-03)  |  All Cisco UCS C-Series M5 servers (40G or 10G using QSA) |  Not Supported  |  All Cisco UCS C-Series M5 servers (QSA at adapter)  |  All Cisco UCS C-Series M5 servers (QSA at adapter)   
1385 - 40G (UCSC-PCIE-C40Q-03)  |  All Cisco UCS C-Series M5 servers (except UCS C125 M5) and S-Series M5 servers (40G or 10G using QSA) |  Not Supported  |  All Cisco UCS C-Series M5 servers (except UCS C125 M5) and S-Series M5 servers (40G or 10G using QSA) |  All Cisco UCS C-Series M5 servers (except UCS C125 M5) and S-Series M5 servers (40G or 10G using QSA)  
Table 6. Cisco UCS 6300 FI - Cisco UCS Blade Servers Cisco VIC |  IOM  
---|---  
2304v1/v2 2204/2208  
15411 + Port Expander  (UCSB-ML-V5Q10G + UCSB-MLOM-PT-01)  |  Cisco UCS B200 M6   
15411 (UCSB-ML-V5Q10G)  |  Cisco UCS B200 M6   
1440 + 1480 + 1480  (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P + UCSB-VIC-M84-4P) |  Cisco UCS B480 M5   
1440 + 1480 + Port Expander (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P + UCSB-MLOM-PT-01) |  Cisco UCS B480 M5   
1440 + 1480 (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P)  |  Cisco UCS B200 M5, B480 M5 and B200 M6 servers   
1440 + Port Expander (UCSB-MLOM-40G-04 + UCSB-MLOM-PT-01)  |  Cisco UCS B200 M5, B480 M5 and B200 M6 servers   
1440 (UCSB-MLOM-40G-04)  |  Cisco UCS B200 M5, B480 M5 and B200 M6 servers   
1340 + 1380 + 1380  (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P +  UCSB-VIC-M83-8P) |  Cisco UCS B480 M5   
1340 + 1380 + Port Expander  (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P +  UCSB-MLOM-PT-01) |  Cisco UCS B480 M5   
1340 + Port Expander - 10G/40G (UCSB-MLOM-40G-03 + UCSB-MLOM-PT-01)  |  Cisco UCS B200 M5 and B480 M5 servers   
1340 + 1380 (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P)  |  Cisco UCS B200 M5 and B480 M5 servers   
1340 - 10G/40G (UCSB-MLOM-40G-03)  |  Cisco UCS B200 M5 and B480 M5 servers   
  
### Cisco UCS 6324 FI

Table 7. Cisco UCS 6324 FI - Cisco UCS Rack Servers Cisco VIC |  Direct Attach (10G)  |  Direct Attach  (Break-out)  
---|---|---  
15428 (UCSC-M-V5Q50G)  |  Not Supported  |  Not Supported   
15238 (UCSC-M-V5D200G)  |  Not Supported  |  Not Supported   
1497-40G/100G (UCSC-MLOMC100-04)  |  Not Supported  |  Not Supported   
1495-40G/100G (UCSC-PCIEC100-04)  |  Not Supported  |  Not Supported   
1477-40G/100G (UCSC-MV100-04)  |  Not Supported  |  Not Supported   
1467-10G/25G (UCSC-MV25-04)  |  Not Supported  |  Not Supported   
1457-10G/25G (UCSC-MLOMC25Q-04)  |  Cisco UCS C220 M5 and C240 M5 servers. |  Cisco UCS C220 M5 and C240 M5 servers.  
1455-10G/25G (UCSC-PCIEC25Q-04)  |  All Cisco UCS C-Series and S-Series M5 servers. |  All Cisco UCS C-Series and S-Series M5 servers.  
1387 - 40G (UCSC-MLOM-C40Q-03)  |  All Cisco UCS C-Series M5 servers. (QSA at the adapter) |  Not Supported   
1385 - 40G (UCSC-PCIE-C40Q-03)  |  All Cisco UCS C-Series M5 servers. (QSA at the adapter) |  Not Supported   
Table 8. Cisco UCS 6324 FI - Cisco UCS Blade Servers Cisco VIC |  IOM |  6324 (Primary Chassis)  
---|---|---  
2204/2208  
15411 (UCSB-ML-V5Q10G)  |  Not Supported  |  Not Supported   
15411 + Port Expander (UCSB-ML-V5Q10G + UCSB-MLOM-PT-01)  |  Not Supported  |  Not Supported   
1440 + 1480 + 1480 (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P +UCSB-VIC-M84-4P)  |  Not Supported  |  Cisco UCS B480 M5  
1440 + 1480 + Port Expander (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P) + UCSB-MLOM-PT-01) |  Not Supported  |  Cisco UCS B480 M5  
1440 + 1480 (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P)  |  Not Supported  |  Cisco UCS B200 M5, B480 M5, and B200 M6  
1440 + Port Expander (UCSB-MLOM-40G-04 + UCSB-MLOM-PT-01)  |  Not Supported  |  Cisco UCS B200 M5, B480 M5, and B200 M6  
1440 (UCSB-MLOM-40G-04)  |  Not Supported  |  Cisco UCS B200 M5, B480 M5, and B200 M6  
1340 + 1380 + 1380  (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P +  UCSB-VIC-M83-8P) |  Cisco UCS B480 M5  |  Cisco UCS B480 M5   
1340 + 1380 + Port Expander  (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P +  UCSB-MLOM-PT-01) |  Cisco UCS B480 M5  |  Cisco UCS B480 M5   
1340 + 1380  (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P)  |  Cisco UCS B200 M5 and B480 M5  |  Cisco UCS B200 M5 and B480 M5   
1340 + Port Expander - 10G/40G  (UCSB-MLOM-40G-03 + UCSB-MLOM-PT-01)  |  Cisco UCS B200 M5 and B480 M5  |  Cisco UCS B200 M5 and B480 M5   
1340 - 10G/40G (UCSB-MLOM-40G-03)  |  Cisco UCS B200 M5 and B480 M5  |  Cisco UCS B200 M5 and B480 M5   
  
### Cisco UCS Fabric Interconnect 9108 100G

Table 9. Cisco UCS FI 9108 100G - Cisco UCS Blade Servers Cisco VIC |  UCSX-S9108-100G (Primary Chassis)  
---|---  
14425 (UCSX-V4-Q25GML) |  Cisco UCS X210c M6  
14425 + UCS VIC 14000 bridge connector + 14825  (UCSX-V4-Q25GML + UCSX-V4-BRIDGE +  UCSX-V4-Q25GME) |  Cisco UCS X210c M6  
15231 (UCSX-ML-V5D200G) |  Cisco UCS X410c M7, X210c M7, X210c M6  
15230 (UCSX-ML-V5D200GV2) |  Cisco UCS X210c M8, X215c M8, X410c M7, X210c M7, and X210c M6   
15420 (UCSX-ML-V5Q50G) |  Cisco UCS X210c M8, X215c M8, X410c M7, X210c M7, and X210c M6   
15420 + UCS VIC 15000 bridge connector + 15422  (UCSX-ML-V5Q50G + UCSX-V5-BRIDGE +  UCSX-ME-V5Q50G) |  Cisco UCS X210c M8, X215c M8, X410c M7, X210c M7, and X210c M6   
  
Cisco UCS 6400 Series Fabric Interconnect Migration

## Cisco UCS 6400 Series Fabric Interconnect Migration Considerations

Beginning with Cisco UCS Manager, Release 4.3(2b), You can migrate Cisco UCS 6400 Series Fabric Interconnects to Cisco UCS 6536 Fabric Interconnect with B-Series servers, C-Series, or S-Series servers. 

To migrate from Cisco UCS 6400 Series Fabric Interconnects to Cisco UCS 6536 Fabric Interconnect: 

  * Cisco UCS 6400 Series Fabric Interconnects must be on Cisco UCS Manager 4.3(2b) or a later release. 

  * Cisco UCS 6536 Fabric Interconnect must be loaded with the same Infrastructure Firmware version that is on the Cisco UCS 6400 Series Fabric Interconnect that it will replace. 


Prerequisites

Before performing the migration from Cisco UCS 6400 Series Fabric Interconnects to Cisco UCS 6536 Fabric Interconnect, ensure that the following prerequisites are met for a successful migration: 

  * Back up and export Cisco UCS Manager configuration before initiating the upgrade. 

  * Take an inventory of the Cisco UCS domain and remove any unsupported hardware. 

  * Ensure to enable the cluster failover.

  * Do not attempt to implement new software features from the new Cisco UCS software version until all required hardware is installed. 

  * Validate the software features and configurations between Cisco UCS 6400 series and UCS 6536 Fabric Interconnects. Before migration, ensure that 6400 series Fabric Interconnect is reconfigured to only have features that are supported with 6536 Fabric Interconnects. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

This is one of the most common reasons for migration failures.

* * *  
  
---|---  
  * Make sure both Cisco UCS 6400 series and 6500 series Fabric Interconnects are on the same UCSM build before migration.

  * Licenses from Cisco UCS 6400 Series Fabric Interconnects are not transferable to Cisco UCS 6500 Series Fabric Interconnects. Cisco UCS 6500 Series Fabric Interconnects has perpetual license enabled by default. 

  * Standalone installations should expect down time. In a cluster configuration, migrating the Fabric Interconnects can result in a small traffic disruption when the traffic fails over from one Fabric Interconnect to another. To avoid that there is no permanent traffic loss during migration, ensure that there is redundancy in the UCS domain on both Fabric Interconnects before migration and test the redundancy before starting the migration. 

  * Cisco UCS 6536 Fabric Interconnect use the IDLE fill pattern for FC uplink ports and FC storage ports when using 8 Gbps speed. 

When migrating to Cisco UCS 6536 Fabric Interconnect and configuring FC Uplink Ports or FC Storage Ports at 8Gbps speed, ensure that the fill pattern is set as IDLE on the corresponding FC switch ports and the direct-attached FC storage array ports. If the fill pattern is not set as IDLE, FC uplink ports and FC storage ports operating at 8 Gbps might go to an errDisabled state, lose SYNC intermittently, or receive errors or bad packets. 

Cisco UCS 6536 Fabric Interconnects supports 8 Gbps only with fill-pattern set to IDLE for direct-attached FC connectivity (FC uplink ports or FC storage ports). This limitation is not applicable for Cisco UCS 6536 Fabric Interconnects with Fibre Channel (FC) ports at 16 Gbps and 32 Gbps. When migrating to Cisco UCS 6536 Fabric Interconnect for direct-attached storage arrays that don’t support IDLE fill-pattern at 8 Gbps do one of the following: 

  * Use a SAN switch between the Cisco UCS 6536 Fabric Interconnect and the storage array with 8 GB FC connectivity. 

  * Upgrade the storage array to 16 GB or 32 GB FC connectivity.

  * Ensure the latest firmware bundle is downloaded and upgraded through GUI or CLI. Incase of attempting to upgrade the firmware bundle using other methods (loader prompt/erase configuration) can result in missing package version. 

  * Before migration, make sure that the FC Speed is 8Gbps on Cisco UCS 6400 Fabric Interconnects or the connected switch supports 8Gbps speed. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Post migration, you can configure the FC Port (Scalability Port) speed on Cisco UCS 6500 Fabric Interconnects.

* * *  
  
---|---  
  * Migrating to different IOM models can result in peer communication issue between IOMs of the Primary and Secondary Fabric Interconnects. 

  * Make a detailed record of the cabling between FEX and fabric interconnects. You must preserve the physical port mapping to maintain the server pinning already configured and minimize down time. 

  * For a cluster configuration, both fabric interconnects must have symmetrical connection topologies between fabric interconnect and FEX. 

  * Use the same speed cables on all the adapter ports that are connected to same Fabric Interconnect. Cisco UCS VIC adapter ports connected to Cisco UCS 6536 fabric interconnect through a mix of 10G and 25G cables can result in UCS rack-mount server discovery failure and ports moving to suspended state. 

  * Cisco UCS 6536 Fabric Interconnect only supports 25/40/100G direct connectivity for C-series rack servers and 10G direct-connect is not supported on C-series rack servers. The Cisco UCS 6536 Fabric Interconnect supports 10G server connectivity only with 2348-UPQ FEX. 

  * A WWN pool can include only WWNNs or WWPNs in the ranges from 20:00:00:00:00:00:00:00 to 20:FF:00:FF:FF:FF:FF:FF or from 50:00:00:00:00:00:00:00 to 5F:FF:00:FF:FF:FF:FF:FF. All other WWN ranges are reserved. When fibre channel traffic is sent through the UCS infrastructure the source WWPN is converted to a MAC address. You cannot use WWPN pool which can translate to source multicast MAC addresses. To ensure the uniqueness of the Cisco UCS WWNNs and WWPNs in the SAN fabric, Cisco recommends using the following WWN prefix for all blocks in a pool: 20:00:00:25:B5:XX:XX:XX 

  * Unconfigure the fibre channel ports on the migrating subordinate Cisco UCS 6400 series Fabric Interconnect and reconfigure on the Cisco UCS 6536 Fabric Interconnect. 


Recommendations

Following are the best practices for a successful migration:

  * For minimal disruption during migration, ensure that there is redundancy for Ethernet and FC traffic from the servers in the UCS domain across both 6400 series fabric interconnects before migration. 

  * Changes to the topology, such as the number of servers or uplink connections, should be performed after the fabric interconnect migration is complete. 

  * During the migration of Fabric Interconnects, ensure the Cluster ID is not changed.

  * During the migration, image synchronization between fabric interconnects is not allowed. This is done to prevent incompatible images from getting synchronized. It is necessary to download B-Series, C-Series, and S-Series server software bundles again after migration is complete. 

  * During the migration, ensure that VLAN is not created in the range of 3915 to 4042 which are the reserved VLAN range for Cisco UCS 6536 Fabric Interconnects. 

  * The Cisco UCS 6536 Fabric Interconnect supports only port-channel mode for chassis-discovery. Hence, before starting migration, change the chassis/FEX discovery policy on the Cisco UCS 6400 series Fabric Interconnect to port-channel and immediately re-acknowledge the chassis. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The migration can fail when the chassis is not immediately re-acknowledged.

* * *  
  
---|---  

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For more information on migrating Cisco UCS 6400 series Fabric Interconnects to Cisco UCS 6500 series Fabric Interconnect with UCS Central, see Considerations for migrating Cisco UCS 6400 Series Fabric Interconnects to Cisco UCS 6500 Series Fabric Interconnects with Cisco UCS Central. 

* * *  
  
---|---  
  
  * Validating Feature Configurations for Cisco UCS 6536 before Upgrade
  * Considerations for migrating Cisco UCS 6400 Series Fabric Interconnects to Cisco UCS 6500 Series Fabric Interconnects with Cisco UCS Central


### Validating Feature Configurations for Cisco UCS 6536 before Upgrade

Cisco UCS 6536 Fabric Interconnect does not support some software features that were allowed with Cisco UCS 6400 Series Fabric Interconnect. Some of these features will become available at a later software release. 

Table 10. Features that needs special attention prior to upgrading Feature |  Remediation  
---|---  
License Management |  Licensing for Cisco UCS 6536 Fabric Interconnect is not a port-based license like in previous generation Fabric Interconnects.  All ports are enabled through a perpetual license in Cisco UCS 6536 Fabric Interconnect and no license installation is required.  
Chassis and fabric extender I/O port channel |  Select a port channel to the I/O module (IOM).  
Multicast optimization |  Verify that multicast optimization is not enabled under the LAN quality-of-service (QoS) system classes  
Fabric forwarding mode for Ethernet |  Verify that the Ethernet forwarding mode is set to End Host Mode Only.   
Fabric forwarding mode for Fibre Channel |  Verify that Fibre Channel forwarding mode is set to End Host Mode or FC Switching Mode.   
Cisco NetFlow |  Unconfigure NetFlow.  
MAC Security  |  Select Allow for MAC security.   
VM-FEX |  Remove port profiles and Cisco UCS Manager ESXi or SCVMM related configurations.  
Dynamic vNIC connection policies |  Set the dynamic vNIC connection policy in the vNIC profile to Not set.   
Cisco Switched Port Analyzer (SPAN) |  Use receive (RX) direction only. The installer will change SPAN to the RX direction and send an alert indicating that this setting is being changed.   
  
Failure to comply with these remediation steps will result in a migration warning alert during the migration process and prevent the fabric interconnects from synchronizing. 

### Considerations for migrating Cisco UCS 6400 Series Fabric Interconnects to Cisco UCS 6500 Series Fabric Interconnects with Cisco UCS Central 

In addition to Cisco UCS 6400 Series Fabric Interconnect Migration Considerations, consider the following prerequisites when migrating with Cisco UCS Central: 

  * Before initiating the migration, ensure to have a complete backup of Cisco UCS Manager and UCS Central configurations.

  * To avoid any configuration issues during migration, make sure the following policies on Policy Resolution Control is set to Local in Cisco UCS Manager: 

  * Infrastructure and Catalog Firmware Policy

  * Equipment Policy

  * Port Configuration Policy


## Migrating from UCS 6400 Series Fabric Interconnects to UCS 6536 Fabric Interconnects

Cisco UCS 6400 Series Fabric Interconnects include Cisco UCS 6454 and Cisco UCS 64108. You can migrate from Cisco UCS 6400 Series Fabric Interconnects to Cisco UCS 6536 Fabric Interconnect. After migrating to Cisco UCS 6536 Fabric Interconnect, Cisco recommends not to migrate back to UCS 6400 Series Fabric Interconnect. 

The Cisco UCS 6536 Fabric Interconnect supports only port-channel mode for chassis-discovery. On changing the chassis or FEX discovery policy to port-channel, the chassis needs to be re-acknowledged before proceeding with the migration. 

To acknowledge the chassis in Cisco UCS Manager, do the following:

  1. In the Navigation pane of Cisco UCS Manager, click Equipment. 

  2. Click the Equipment node. 

  3. In the Work pane, click the Policies tab. 

  4. Click the Global Policies subtab. 

  5. In the Chassis/FEX Discovery Policy area, set the Link Grouping Preference field to Port Channel. 

  6. Expand Equipment > Chassis, and choose the chassis that you want to acknowledge. 

  7. In the Work pane, click the General tab. 

  8. In the Actions area, click Acknowledge Chassis. 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For more information about how to perform configuration procedures in Cisco UCS Manager, see the appropriate [Cisco UCS Manager Configuration Guide](http://www.cisco.com/en/US/products/ps10281/products_installation_and_configuration_guides_list.html). 

* * *  
  
---|---  
  
### Procedure

* * *

**Step 1** |  Move the traffic to the primary fabric interconnect. This can be performed in two ways: fabric evacuation and uplink disablement. Use the below flowchart to choose between the two based on your Cisco UCS domain server and connectivity.![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472394.png) |  **Note** |  For direct-attached rack servers, only uplink disablement is supported.  
---|---  
**Step 2** |  Verify that all traffic has failed over to the primary fabric interconnect. Unconfigure all server ports or fibre channel ports on the subordinate fabric interconnect.  For more information, see the _Fabric Interconnect Traffic Evacuation_ section in the _Guidelines and Prerequisites_ chapter of the [Cisco UCS Manager Firmware Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html).   
**Step 3** |  Power down the old subordinate fabric interconnect and disconnect the power and the L1/L2 cables. If you are monitoring the migration using a KVM session to a server host, you may need to reconnect it after you powered down the secondary fabric interconnect.   
**Step 4** |  Mount the replacement Cisco UCS 6536 Fabric Interconnect into either the same rack or an adjacent rack. |  **Note** |  As a best practice, you should label the cables.  
---|---  
**Step 5** |  Connect the L1/L2 cables and the server ports according to your port mapping plan.  
**Step 6** |  Power up the new fabric interconnect. If it is connected correctly, the new subordinate fabric interconnect will detect that it is being added to an existing cluster.   
**Step 7** |  The subordinate Cisco UCS 6536 Fabric Interconnect will automatically synchronize the configuration and database/state information from the primary UCS 6400 Series Fabric Interconnect.  Synchronization between primary and subordinate fabric interconnects can take several minutes. You may see an error message that will persist until the server ports are enabled.  The port configuration is copied from the subordinate Fabric Interconnect to the new Fabric Interconnect. |  **Note** |  Skip to Step 10 incase of replacing with a different IOM or FEX during migration. For more information on the compatibility matrix of supported IOM or FEX on the Fabric Interconnect, see [Ports on the Cisco UCS Fabric Interconnects](m_overview-4-1.html#id_118320)  
---|---  
**Step 8** |  Unified ports on the 6500 series fabric interconnect are different from the unified port ordering on the 6400 series Fabric Interconnect.  |  **Note** | 

  * When you convert from ethernet ports to fibre channel ports, a reboot is required. Fibre channel ports are converted in blocks of four (breakout ports). 
  * For more information on _Configuring FC Uplink port_ or _Converting FC storage port to FC uplink port_ , see the _LAN Ports and Port Channels_ chapter in [Cisco UCS Manager Network Management Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Network-Mgmt/4-2/b_UCSM_Network_Mgmt_Guide_4_2/b_UCSM_Network_Mgmt_Guide_chapter_0100.html#task_A7ED517EE3C9482FA063827E4CBD25AE). 

  
---|---  
**Step 9** |  Configure the network uplink ports on the new Cisco UCS 6536 fabric interconnect.  
**Step 10** |  Match the old configuration from Cisco UCS 6400 Fabric Interconnect for the port-channel. Add uplink ports to the necessary port-channel or any other previous configuration required for the port-channel. Wait for configuration to complete before proceeding to the next step.  |  **Note** |  Waiting to enable the server ports prevents the svc_sam_bladeAG service from communicating with chassis and servers. In previous migrations, when enabling server ports at the same time as the uplink ports, it would cause topping out (pinning) the CPU to near 100% on the primary fabric interconnect. When there is high CPU usage, the user interface becomes unresponsive and the svc_sam_bladeAG service must be restarted to recover.   
---|---  
**Step 11** |  Reconfigure the server ports or fibre channel ports.

  1. If you have changed port mappings, you may need to reacknowledge the IOM, FEX, or direct-connect rack server connected to the subordinate fabric interconnect. 
  2. Verify and if necessary, you can reconfigure ethernet ports as server ports.
  3. Skip to Step 13 to verify the data path.

  
**Step 12** |  To remove and replace the new IOM or FEX and reconfigure the server ports, do the following:

  1. Remove the existing IOM connected to the subordinate Fabric Interconnect and replace it with a supported IOM of Cisco UCS 6536 Fabric Interconnect. 
  2. Verify if any modifications are required for the cable connections. |  **Note** |  For more information, see Cisco UCS Fabric Interconnect Server Compatibility Matrix - Release 4.3(6b).   
---|---  
  3. Reconfigure the new IOM to maintain the same port mappings. If port mapping were not preserved, configure the server ports accordingly. 

  4. Reacknowledge the IOM connected to the subordinate Fabric Interconnect.


**Note** |  When migrating from Cisco UCS 6400 to Cisco UCS 6536, IOM-220x can be replaced with IOM-2304v2 or IOM-2408.  
---|---  
**Step 13** |  Verify that the data path is ready. For more information, see the _Verifying that Dynamic vNICs Are Up and Running_ section in the _Guidelines and Prerequisites_ chapter of the [Cisco UCS Manager Firmware Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html).  Ensure that all faults are resolved before proceeding with next step.

  1. Verify, and if necessary, reconfigure the SAN pin group for fibre channel ports in the associated service profile.
  2. Verify, and if necessary, reconfigure the LAN pin group for ethernet ports in the associated service profile.
  3. Verify, and if necessary, reconfigure the port channel for uplink ethernet ports.

  
**Step 14** |  Move the traffic back to the new subordinate fabric interconnect. If you used the fabric evacuation method, then deselect fabric evacuation. If you disabled the uplinks (Ethernet and Fibre Channel), then re-enable the uplinks. Verify that traffic is flowing correctly on the new subordinate fabric interconnect.   
**Step 15** |  After verifying that traffic is flowing on the subordinate fabric interconnect, promote the subordinate fabric interconnect to primary using the below commands: 

  * UCS-A #connect local-mgmt: This command connects to the local management interface of the cluster.
  * UCS-A (local-mgmt) #cluster{lead {a|b}} or UCS-A (local-mgmt) #cluster{force primary{a|b}}: The cluster lead command and cluster force primary command are two separate commands that can be used for promoting the fabric interconnect. 

|  **Note** |  Ensure that the primary fabric interconnect is Cisco UCS 6536 Fabric Interconnect.  
---|---  
**Step 16** |  Cable the second new fabric interconnect identically to the first and repeat the steps for the other fabric interconnect replacements to complete the migration.   
  
* * *

Cisco UCS 6300 Series Fabric Interconnect Migration

## Cisco UCS 6300 Series Fabric Interconnect Migration Considerations

Beginning with Cisco UCS Manager, Release 4.2(3b), Cisco UCS Manager provides support for Cisco UCS 6536 Fabric Interconnect. You can migrate Cisco UCS 6300 Series Fabric Interconnects to Cisco UCS 6536 Fabric Interconnect with B-Series servers, C-Series, or S-Series servers. 

To migrate from Cisco UCS 6300 Series Fabric Interconnects to Cisco UCS 6536 Fabric Interconnect: 

  * Cisco UCS 6300 Series Fabric Interconnects must be on Cisco UCS Manager 4.2(3b) or a later release. 

  * Cisco UCS 6536 Fabric Interconnect must be loaded with the same Infrastructure Firmware version that is on the Cisco UCS 6300 Series Fabric Interconnect that it will replace. 


Prerequisites

Before performing the migration from Cisco UCS 6300 Series Fabric Interconnects to Cisco UCS 6536 Fabric Interconnect, ensure that the following prerequisites are met for a successful migration: 

  * Back up and export Cisco UCS Manager configuration before initiating the upgrade. Ensure that the backup file from the 6300 Series Fabric Interconnects is compatible with the 6536 Fabric Interconnects. You can follow any of the backup methods: 

  * **Online Migration:** This method allows for backing up the configuration while the Fabric Interconnect is operational. It ensures minimal disruption and maintains continuous availability during the migration process. 

  * **Offline Migration:** This method involves taking the fabric interconnect offline to perform the backup, which may result in downtime. 

  * Take an inventory of the Cisco UCS domain and remove any unsupported hardware. 

  * Ensure to enable the cluster failover.

  * Do not attempt to implement new software features from the new Cisco UCS software version until all required hardware is installed. 

  * Validate the software features and configurations between Cisco UCS 6300 series and UCS 6536 Fabric Interconnects. Before migration, ensure that 6300 series Fabric Interconnect is reconfigured to only have features that are supported with 6536 Fabric Interconnects. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

This is one of the most common reasons for migration failures. 

* * *  
  
---|---  
  * Make sure both Cisco UCS 6300 series and 6500 series Fabric Interconnects are on the same UCSM build before migration.

  * Licenses from Cisco UCS 6300 Series Fabric Interconnects are not transferable to Cisco UCS 6500 Series Fabric Interconnects.

  * Standalone installations should expect down time. In a cluster configuration, migrating the Fabric Interconnects can result in a small traffic disruption when the traffic fails over from one Fabric Interconnect to another. To avoid that there is no permanent traffic loss during migration, ensure that there is redundancy in the UCS domain on both Fabric Interconnects before migration and test the redundancy before starting the migration. 

  * Cisco UCS 6536 Fabric Interconnect use the IDLE fill pattern for FC uplink ports and FC storage ports when using 8 Gbps speed. 

When migrating to Cisco UCS 6536 Fabric Interconnect and configuring FC Uplink Ports or FC Storage Ports at 8Gbps speed, ensure that the fill pattern is set as IDLE on the corresponding FC switch ports and the direct-attached FC storage array ports. If the fill pattern is not set as IDLE, FC uplink ports and FC storage ports operating at 8 Gbps might go to an errDisabled state, lose SYNC intermittently, or receive errors or bad packets. 

Cisco UCS 6536 Fabric Interconnects supports 8 Gbps only with fill-pattern set to IDLE for direct-attached FC connectivity (FC uplink ports or FC storage ports). This limitation is not applicable for Cisco UCS 6536 Fabric Interconnects with Fibre Channel (FC) ports at 16 Gbps and 32 Gbps. When migrating to Cisco UCS 6536 Fabric Interconnect for direct-attached storage arrays that don’t support IDLE fill-pattern at 8 Gbps do one of the following: 

  * Use a SAN switch between the Cisco UCS 6536 Fabric Interconnect and the storage array with 8 GB FC connectivity. 

  * Upgrade the storage array to 16 GB or 32 GB FC connectivity.

  * Ensure the latest firmware bundle is downloaded and upgraded through GUI or CLI. Incase of attempting to upgrade the firmware bundle using other methods (loader prompt/erase configuration) can result in missing package version. 

  * Before migration, make sure that the FC Speed is 8Gbps on Cisco UCS 6300 Fabric Interconnects or the connected switch supports 8Gbps speed. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Post migration, you can configure the FC Port (Scalability Port) speed on Cisco UCS 6500 Fabric Interconnects.

* * *  
  
---|---  
  * Migrating to different IOM models can result in peer communication issue between IOMs of the Primary and Secondary Fabric Interconnects. 

  * Make a detailed record of the cabling between FEX and fabric interconnects. You must preserve the physical port mapping to maintain the server pinning already configured and minimize down time. 

  * For a cluster configuration, both fabric interconnects must have symmetrical connection topologies between fabric interconnect and FEX. 

  * Use the same speed cables on all the adapter ports that are connected to same Fabric Interconnect. Cisco UCS VIC adapter ports connected to Cisco UCS 6536 fabric interconnect through a mix of 10G and 25G cables can result in UCS rack-mount server discovery failure and ports moving to suspended state. 

  * Cisco UCS 6536 Fabric Interconnect only supports 25/40/100G direct connectivity for C-series rack servers and 10G direct-connect is not supported on C-series rack servers. The Cisco UCS 6536 Fabric Interconnect supports 10G server connectivity only with 2348-UPQ FEX. 

  * A WWN pool can include only WWNNs or WWPNs in the ranges from 20:00:00:00:00:00:00:00 to 20:FF:00:FF:FF:FF:FF:FF or from 50:00:00:00:00:00:00:00 to 5F:FF:00:FF:FF:FF:FF:FF. All other WWN ranges are reserved. When fibre channel traffic is sent through the UCS infrastructure the source WWPN is converted to a MAC address. You cannot use WWPN pool which can translate to source multicast MAC addresses. To ensure the uniqueness of the Cisco UCS WWNNs and WWPNs in the SAN fabric, Cisco recommends using the following WWN prefix for all blocks in a pool: 20:00:00:25:B5:XX:XX:XX 

  * Unconfigure the fibre channel ports on the migrating subordinate Cisco UCS 6300 series Fabric Interconnect and reconfigure on the Cisco UCS 6536 Fabric Interconnect. 


Recommendations

Following are the best practices for a successful migration:

  * For minimal disruption during migration, ensure that there is redundancy for Ethernet and FC traffic from the servers in the UCS domain across both 6300 series fabric interconnects before migration. 

  * Changes to the topology, such as the number of servers or uplink connections, should be performed after the fabric interconnect migration is complete. 

  * During the migration of Fabric Interconnects, ensure the Cluster ID is not changed.

  * During the migration, image synchronization between fabric interconnects is not allowed. This is done to prevent incompatible images from getting synchronized. It is necessary to download B-Series, C-Series, and S-Series server software bundles again after migration is complete. 

  * During the migration, ensure that VLAN is not created in the range of 3915 to 4042 which are the reserved VLAN range for Cisco UCS 6536 Fabric Interconnects. 

  * The Cisco UCS 6536 Fabric Interconnect supports only port-channel mode for chassis-discovery. Hence change the Chassis/FEX discovery policy on the Cisco UCS 6300 series Fabric Interconnect to port-channel and immediately re-acknowledge the Cisco UCS 5108 chassis. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The migration can fail when the chassis is not immediately re-acknowledged.

* * *  
  
---|---  


### Validating Feature Configurations for Cisco UCS 6536 before Upgrade

Cisco UCS 6536 Fabric Interconnect does not support some software features that were allowed with Cisco UCS 6300 Fabric Interconnect. Some of these features will become available at a later software release. 

Table 11. Features that needs special attention prior to upgrading Feature |  Remediation  
---|---  
License Management |  Licensing for Cisco UCS 6536 Fabric Interconnect is not a port-based license like in previous generation Fabric Interconnects.  All ports are enabled through a perpetual license in Cisco UCS 6536 Fabric Interconnect and no license installation is required.  
Chassis and fabric extender I/O port channel |  Select a port channel to the I/O module (IOM).  
Multicast optimization |  Verify that multicast optimization is not enabled under the LAN quality-of-service (QoS) system classes  
Fabric forwarding mode for Ethernet |  Verify that the Ethernet forwarding mode is set to End Host Mode Only.   
Fabric forwarding mode for Fibre Channel |  Verify that Fibre Channel forwarding mode is set to End Host Mode or FC Switching Mode.   
Cisco NetFlow |  Unconfigure NetFlow.  
MAC Security  |  Select Allow for MAC security.   
VM-FEX |  Remove port profiles and Cisco UCS Manager ESXi or SCVMM related configurations.  
Dynamic vNIC connection policies |  Set the dynamic vNIC connection policy in the vNIC profile to Not set.   
Cisco Switched Port Analyzer (SPAN) |  Use receive (RX) direction only. The installer will change SPAN to the RX direction and send an alert indicating that this setting is being changed.   
  
Failure to comply with these remediation steps will result in a migration warning alert during the migration process and prevent the fabric interconnects from synchronizing. 

## Migrating from UCS 6300 Series Fabric Interconnects to UCS 6536 Fabric Interconnects

Cisco UCS 6300 Series Fabric Interconnects include Cisco UCS 6332 and Cisco UCS 6332-16UP. You can migrate from Cisco UCS 6300 Series Fabric Interconnects to Cisco UCS 6536 Fabric Interconnect. 

The Cisco UCS 6536 Fabric Interconnect supports only port-channel mode for chassis-discovery. On changing the chassis or FEX discovery policy to port-channel, the chassis needs to be re-acknowledged before proceeding with the migration. 

To acknowledge the chassis in Cisco UCS Manager, do the following:

  1. In the Navigation pane of Cisco UCS Manager, click Equipment. 

  2. Click the Equipment node. 

  3. In the Work pane, click the Policies tab. 

  4. Click the Global Policies subtab. 

  5. In the Chassis/FEX Discovery Policy area, set the Link Grouping Preference field to Port Channel. 

  6. Expand Equipment > Chassis, and choose the chassis that you want to acknowledge. 

  7. In the Work pane, click the General tab. 

  8. In the Actions area, click Acknowledge Chassis. 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For more information about how to perform configuration procedures in Cisco UCS Manager, see the appropriate [Cisco UCS Manager Configuration Guide](http://www.cisco.com/en/US/products/ps10281/products_installation_and_configuration_guides_list.html). 

* * *  
  
---|---  
  
### Procedure

* * *

**Step 1** |  Move the traffic to the primary fabric interconnect. This can be performed in two ways: fabric evacuation and uplink disablement. Use the below flowchart to choose between the two based on your Cisco UCS domain server and connectivity.![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472394.png) |  **Note** |  For direct-attached rack servers, only uplink disablement is supported.  
---|---  
**Step 2** |  Verify that all traffic has failed over to the primary fabric interconnect. Unconfigure all server ports or fibre channel ports on the subordinate fabric interconnect.  |  **Note** |  For more information, see the _Fabric Interconnect Traffic Evacuation_ section in the _Guidelines and Prerequisites_ chapter of the [Cisco UCS Manager Firmware Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html).   
---|---  
**Step 3** |  Power down the old subordinate fabric interconnect and disconnect the power and the L1/L2 cables. If you are monitoring the migration using a KVM session to a server host, you may need to reconnect it after you powered down the secondary fabric interconnect.   
**Step 4** |  Mount the replacement Cisco UCS 6536 Fabric Interconnect into either the same rack or an adjacent rack. |  **Note** |  As a best practice, you should label the cables.  
---|---  
**Step 5** |  Connect the L1/L2 cables and the server ports according to your port mapping plan.  
**Step 6** |  Power up the new fabric interconnect. If it is connected correctly, the new subordinate fabric interconnect will detect that it is being added to an existing cluster.   
**Step 7** |  The subordinate Cisco UCS 6536 Fabric Interconnect will automatically synchronize the configuration and database/state information from the primary UCS 6300 Series Fabric Interconnect.  Synchronization between primary and subordinate fabric interconnects can take several minutes. You may see an error message that will persist until the server ports are enabled.  The port configuration is copied from the subordinate Fabric Interconnect to the new Fabric Interconnect. |  **Note** |  Skip to Step 10 incase of replacing with a different IOM or FEX during migration. For more information on the compatibility matrix of supported IOM or FEX on the Fabric Interconnect, see [Ports on the Cisco UCS Fabric Interconnects](m_overview-4-1.html#id_118320)  
---|---  
**Step 8** |  Unified ports on the 6500 series fabric interconnect are different from the unified port ordering on the 6300 series Fabric Interconnect.  |  **Note** | 

  * When you convert from ethernet ports to fibre channel ports, a reboot is required. Fibre channel ports are converted in blocks of four (breakout ports). 
  * For more information on _Configuring FC Uplink port_ or _Converting FC Storage Port to FC Uplink port_ , refer the _LAN Ports and Port Channels_ chapter in [Cisco UCS Manager Network Management Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Network-Mgmt/4-2/b_UCSM_Network_Mgmt_Guide_4_2/b_UCSM_Network_Mgmt_Guide_chapter_0100.html#task_A7ED517EE3C9482FA063827E4CBD25AE). 

  
---|---  
**Step 9** |  Reconfigure the server ports or fibre channel ports that were unconfigured in Step 2.

  1. If you have changed port mappings, you may need to reacknowledge the IOM, FEX, or direct-connect rack server connected to the subordinate fabric interconnect. 
  2. Verify and if necessary, you can reconfigure ethernet ports as server ports.
  3. Skip to Step 11 to verify the data path.

  
**Step 10** |  To remove and replace the new IOM or FEX and reconfigure the server ports, do the following:

  1. Remove the existing IOM connected to the subordinate Fabric Interconnect and replace it with a supported IOM of Cisco UCS 6536 Fabric Interconnect. 
  2. Verify if any modifications are required for the cable connections. |  **Note** |  For more information, see Cisco UCS Fabric Interconnect Server Compatibility Matrix - Release 4.3(6b).   
---|---  
  3. Reconfigure the new IOM to maintain the same port mappings. If port mapping were not preserved, configure the server ports accordingly. 

  4. Reacknowledge the IOM connected to the subordinate Fabric Interconnect.


**Note** |  When migrating from Cisco UCS 6300 to Cisco UCS 6536, IOM-220x can be replaced with IOM-2304v2 or IOM-2408 and IOM-2304v1/v2 with IOM-2408.   
---|---  
**Step 11** |  Verify that the data path is ready. For more information, see the _Verifying that Dynamic vNICs Are Up and Running_ section in the _Guidelines and Prerequisites_ chapter of the [Cisco UCS Manager Firmware Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html).  Ensure that all faults are resolved before proceeding with next step.

  1. Verify, and if necessary, reconfigure the SAN pin group for Fibre Channel ports in the associated service profile.
  2. Verify, and if necessary, reconfigure the LAN pin group for Ethernet ports in the associated service profile.
  3. Verify, and if necessary, reconfigure the port channel for uplink Ethernet ports.

  
**Step 12** |  Move the traffic back to the new subordinate fabric interconnect. If you used the fabric evacuation method, then deselect fabric evacuation. If you disabled the uplinks (Ethernet and Fibre Channel), then re-enable the uplinks. Verify that traffic is flowing correctly on the new subordinate fabric interconnect.   
**Step 13** |  After verifying that traffic is flowing on the subordinate fabric interconnect, promote the subordinate fabric interconnect to primary using the below commands: 

  * UCS-A #connect local-mgmt: This command connects to the local management interface of the cluster.
  * UCS-A (local-mgmt) #cluster{lead {a|b}} or UCS-A (local-mgmt) #cluster{force primary{a|b}}: The cluster lead command and cluster force primary command are two separate commands that can be used for promoting the fabric interconnect. 

|  **Note** |  Ensure that the primary fabric interconnect is Cisco UCS 6536 Fabric Interconnect.  
---|---  
**Step 14** |  Cable the second new fabric interconnect identically to the first and repeat the steps for the other fabric interconnect replacements to complete the migration.  |  **Important** |  Migrating from Cisco UCS 6200 Series Fabric Interconnects to Cisco UCS 6500 Series Fabric Interconnect is supported with Cisco UCS Manager Release 4.2(3a). For more information, see [Migration Guide for Cisco UCS Fabric Interconnects, 4.2](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html).   
---|---  
  
* * *

---

## Page 5: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Fabric-Interconnect-Migration/4-3_1/b_migration_guide_for_cisco_ucs_fabric_interconnects_4-3/m_migrating_from_6200_to_64108.html

# Migrating to UCS 6400 Series Fabric Interconnects

Cisco UCS 6454 Fabric Interconnect to Cisco UCS 64108 Fabric Interconnect Migration

## Cisco UCS 6400 Series Fabric Interconnect Migration Considerations

Cisco UCS Manager provides support for migrating Cisco UCS 6454 Fabric Interconnect to Cisco UCS 64108 Fabric Interconnect with B-Series servers, C-Series, or S-Series servers. 

To migrate from Cisco UCS 6454 Fabric Interconnect to Cisco UCS 64108 Fabric Interconnect, both the Fabric Interconnect must be loaded with the same Infrastructure Firmware version. 

Prerequisites

Before performing the migration from Cisco UCS 6454 Fabric Interconnects to Cisco UCS 64108 Fabric Interconnect, ensure that the following prerequisites are met for a successful migration: 

  * Back up and export Cisco UCS Manager configuration before initiating the upgrade.

  * Take an inventory of the Cisco UCS domain and remove any unsupported hardware.

  * Ensure to enable the cluster failover.

  * Do not attempt to implement new software features from the new Cisco UCS software version until all required hardware is installed. 

  * Make sure both Cisco UCS 6400 series Fabric Interconnects are on the same UCSM build before migration.

  * Standalone installations should expect down time. In a cluster configuration, migrating the Fabric Interconnects can result in a small traffic disruption when the traffic fails over from one Fabric Interconnect to another. To avoid that there is no permanent traffic loss during migration, ensure that there is redundancy in the UCS domain on both Fabric Interconnects before migration and test the redundancy before starting the migration. 

  * Ensure the latest firmware bundle is downloaded and upgraded through GUI or CLI. Incase of attempting to upgrade the firmware bundle using other methods (loader prompt/erase configuration) can result in missing package version. 

  * Before migration, make sure that the FC Speed is 8Gbps on Cisco UCS 6454 Fabric Interconnects or the connected switch supports 8Gbps speed. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Post migration, you can configure the FC Port (Scalability Port) speed on Cisco UCS 64108 Fabric Interconnects.

* * *  
  
---|---  
  * Migrating to different IOM models can result in peer communication issue between IOMs of the Primary and Secondary Fabric Interconnects. 

  * Make a detailed record of the cabling between FEX and fabric interconnects. You must preserve the physical port mapping to maintain the server pinning already configured and minimize down time. 

  * For a cluster configuration, both fabric interconnects must have symmetrical connection topologies between fabric interconnect and FEX. 

  * Use the same speed cables on all the adapter ports that are connected to same Fabric Interconnect. Cisco UCS VIC adapter ports connected to Cisco UCS 64108 fabric interconnect through a mix of 10G and 25G cables can result in UCS rack-mount server discovery failure and ports moving to suspended state. 

  * A WWN pool can include only WWNNs or WWPNs in the ranges from 20:00:00:00:00:00:00:00 to 20:FF:00:FF:FF:FF:FF:FF or from 50:00:00:00:00:00:00:00 to 5F:FF:00:FF:FF:FF:FF:FF. All other WWN ranges are reserved. When fibre channel traffic is sent through the UCS infrastructure the source WWPN is converted to a MAC address. You cannot use WWPN pool which can translate to source multicast MAC addresses. To ensure the uniqueness of the Cisco UCS WWNNs and WWPNs in the SAN fabric, Cisco recommends using the following WWN prefix for all blocks in a pool: 20:00:00:25:B5:XX:XX:XX 


Recommendations

Following are the best practices for a successful migration:

  * For minimal disruption during migration, ensure that there is redundancy for Ethernet and FC traffic from the servers in the UCS domain across both 6454 Fabric Interconnects before migration. 

  * Changes to the topology, such as the number of servers or uplink connections, should be performed after the fabric interconnect migration is complete. 

  * During the migration of Fabric Interconnects, ensure the Cluster ID is not changed.

  * During the migration, image synchronization between fabric interconnects is not allowed. This is done to prevent incompatible images from getting synchronized. It is necessary to download B-Series, C-Series, and S-Series server software bundles again after migration is complete. 

  * Unconfigure the fibre channel ports on the migrating subordinate Cisco UCS 6454 Fabric Interconnect and reconfigure on the Cisco UCS 64108 Fabric Interconnect. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For more information on migrating Cisco UCS 6454 Fabric Interconnect to Cisco UCS 64108 Fabric Interconnect with UCS Central, see Considerations for migrating Cisco UCS 6454 Fabric Interconnects to Cisco UCS 64108 Fabric Interconnects with Cisco UCS Central. 

* * *  
  
---|---  


  * Validating Feature Configurations for Cisco UCS 64108 Fabric Interconnect before Upgrade
  * Considerations for migrating Cisco UCS 6454 Fabric Interconnects to Cisco UCS 64108 Fabric Interconnects with Cisco UCS Central


### Validating Feature Configurations for Cisco UCS 64108 Fabric Interconnect before Upgrade

Table 1. Features that needs special attention prior to upgrading Feature |  Remediation  
---|---  
Chassis and fabric extender I/O port channel |  Select a port channel to the I/O module (IOM).  
Multicast optimization |  Verify that multicast optimization is not enabled under the LAN quality-of-service (QoS) system classes  
Fabric forwarding mode for Ethernet |  Verify that the Ethernet forwarding mode is set to End Host Mode Only.   
Fabric forwarding mode for Fibre Channel |  Verify that Fibre Channel forwarding mode is set to End Host Mode or FC Switching Mode.   
Cisco NetFlow |  Unconfigure NetFlow.  
MAC Security  |  Select Allow for MAC security.   
VM-FEX |  Remove port profiles and Cisco UCS Manager ESXi or SCVMM related configurations.  
Dynamic vNIC connection policies |  Set the dynamic vNIC connection policy in the vNIC profile to Not set.   
Cisco Switched Port Analyzer (SPAN) |  Use receive (RX) direction only. The installer will change SPAN to the RX direction and send an alert indicating that this setting is being changed.   
  
Failure to comply with these remediation steps will result in a migration warning alert during the migration process and prevent the fabric interconnects from synchronizing. 

### Considerations for migrating Cisco UCS 6454 Fabric Interconnects to Cisco UCS 64108 Fabric Interconnects with Cisco UCS Central

In addition to Cisco UCS 6400 Series Fabric Interconnect Migration Considerations, consider the following prerequisites when migrating with Cisco UCS Central: 

  * Before initiating the migration, ensure to have a complete backup of Cisco UCS Manager and UCS Central configurations.

  * To avoid any configuration issues during migration, make sure the following policies on Policy Resolution Control is set to Local in Cisco UCS Manager: 

  * Infrastructure and Catalog Firmware Policy

  * Equipment Policy

  * Port Configuration Policy


## Migrating from UCS 6454 Fabric Interconnects to UCS 64108 Fabric Interconnects

Beginning with Cisco UCS Manager Release 4.1, you can migrate from Cisco UCS 6454 Fabric Interconnect to Cisco UCS 64108 Fabric Interconnect. 

To acknowledge the chassis in Cisco UCS Manager, do the following:

  1. In the Navigation pane of Cisco UCS Manager, click Equipment. 

  2. Click the Equipment node. 

  3. In the Work pane, click the Policies tab. 

  4. Click the Global Policies subtab. 

  5. In the Chassis/FEX Discovery Policy area, set the Link Grouping Preference field to Port Channel. 

  6. Expand Equipment > Chassis, and choose the chassis that you want to acknowledge. 

  7. In the Work pane, click the General tab. 

  8. In the Actions area, click Acknowledge Chassis. 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For more information about how to perform configuration procedures in Cisco UCS Manager, see the appropriate [Cisco UCS Manager Configuration Guide](http://www.cisco.com/en/US/products/ps10281/products_installation_and_configuration_guides_list.html). 

* * *  
  
---|---  
  
### Procedure

* * *

**Step 1** |  Move the traffic to the primary fabric interconnect (Cisco UCS 6454). This can be performed in two ways: fabric evacuation and uplink disablement. Use the below flowchart to choose between the two based on your Cisco UCS domain server and connectivity.  ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472394.png) |  **Note** |  For direct-attached rack servers, only uplink disablement is supported.  
---|---  
**Step 2** |  Verify that all traffic has failed over to the primary fabric interconnect. Unconfigure all the server ports or fibre channel ports on the subordinate fabric interconnect.  |  **Note** |  For more information, see the _Fabric Interconnect Traffic Evacuation_ section in the _Guidelines and Prerequisites_ chapter of the [Cisco UCS Manager Firmware Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html).   
---|---  
**Step 3** |  Power down the UCS 6454 subordinate fabric interconnect and disconnect the power and the L1/L2 cables.  
**Step 4** |  Mount the replacement UCS 64108 Fabric Interconnect into either the same rack or an adjacent rack. |  **Note** |  As a best practice, you should label the cables.  
---|---  
**Step 5** |  Connect the L1/L2 cables and the server ports according to your port mapping plan.  
**Step 6** |  Power up the new fabric interconnect. If it is connected correctly, the new subordinate fabric interconnect will detect that it is being added to an existing cluster.   
**Step 7** |  Enter the IP address information for the new subordinate fabric interconnect.   
**Step 8** |  Unified ports on the UCS 6454 fabric interconnect are similar to the unified port ordering on the 64108 fabric interconnect. |  **Note** | 

  * When you convert from ethernet ports to fibre channel ports, a reboot is required.
  * For more information on _Configuring FC Uplink port_ or _Converting FC Storage Port to FC Uplink port_ , refer the _LAN Ports and Port Channels_ chapter in [Cisco UCS Manager Network Management Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Network-Mgmt/4-2/b_UCSM_Network_Mgmt_Guide_4_2/b_UCSM_Network_Mgmt_Guide_chapter_0100.html#task_A7ED517EE3C9482FA063827E4CBD25AE). 

  
---|---  
**Step 9** |  Configure the network uplink ports on the new Cisco UCS 64108 fabric interconnect.  
**Step 10** |  Match the old configuration from 6454 for the port-channel. Add uplink ports to the necessary port-channel or any other previous configuration required for the port-channel. Wait for configuration to complete before proceeding to the next step.  |  **Note** |  Waiting to enable the server ports prevents the svc_sam_bladeAG service from communicating with chassis and servers. In previous migrations, when enabling server ports at the same time as the uplink ports, it would cause topping out (pinning) the CPU to near 100% on the primary fabric interconnect. When there is high CPU usage, the user interface becomes unresponsive and the svc_sam_bladeAG service must be restarted to recover.   
---|---  
**Step 11** |  Reconfigure the server ports or fibre channel ports.

  1. If you have changed port mappings, you may need to reacknowledge the IOM, FEX, or direct-connect rack server connected to the subordinate fabric interconnect. 
  2. Verify and if necessary, you can reconfigure ethernet ports as server ports.

  
**Step 12** |  The 64108 subordinate fabric interconnect will automatically synchronize the configuration and database/state information from the primary UCS 6454 fabric interconnect.  Synchronization between primary and subordinate fabric interconnects can take several minutes. You may see an error message that will persist until the server ports are enabled.  The port configuration is copied from the subordinate fabric interconnect to the new fabric interconnect.  
**Step 13** |  Reconfigure the Ethernet ports, Fibre Channel ports, or unified ports.

  1. If you have changed port mappings for direct-attach rack server, reacknowledge the server.
  2. It is recommended to reacknowledge the IOM or FEX.

|  **Note** |  You should login directly to the new Cisco UCS 6454 Fabric Interconnect GUI to configure the unified ports during the migration.  
---|---  
**Step 14** |  Verify that the data path is ready. For more information, see the _Verifying that Dynamic vNICs Are Up and Running_ section in the _Guidelines and Prerequisites_ chapter of the [Cisco UCS Manager Firmware Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html).  Ensure that all faults are resolved before proceeding with next step.

  1. Verify, and if necessary, reconfigure the SAN pin group for Fibre Channel ports in the associated service profile.
  2. Verify, and if necessary, reconfigure the LAN pin group for Ethernet ports in the associated service profile.
  3. Verify, and if necessary, reconfigure the port channel for uplink Ethernet ports.

  
**Step 15** |  Move the traffic back to the new subordinate fabric interconnect. If you used the fabric evacuation method, then deselect fabric evacuation. If you disabled the uplinks (Ethernet and Fibre Channel), then reenable the uplinks. Verify that traffic is flowing correctly on the new subordinate fabric interconnect.   
**Step 16** |  After verifying that traffic is flowing on the subordinate fabric interconnect, promote the subordinate fabric interconnect to primary using the below commands: 

  * UCS-A #connect local-mgmt: This command connects to the local management interface of the cluster.
  * UCS-A (local-mgmt) #cluster{lead {a|b}} or UCS-A (local-mgmt) #cluster{force primary{a|b}}: The cluster lead command and cluster force primary command are two separate commands that can be used for promoting the fabric interconnect. 

|  **Note** |  Ensure that the primary fabric interconnect is Cisco UCS 64108 fabric interconnect.  
---|---  
**Step 17** |  Cable the second new fabric interconnect identically to the first and repeat the steps for the other fabric interconnect replacement to complete the migration.   
  
* * *

---

## Page 6: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Fabric-Interconnect-Migration/4-3_1/b_migration_guide_for_cisco_ucs_fabric_interconnects_4-3/m-appendix.html

# Appendix

## Appendix

This section provides a list of terminologies that are used in this document.

Name | Description  
---|---  
Direct-Connect  |  C-Series VIC connections that are plugged directly into the Fabric Interconnect port.  
Ethernet Port |  A generic term for the opening on the side of any Ethernet node, typically in an Ethernet NIC or LAN switch, into which an Ethernet cable can be connected.   
Fabric Port Channel |  Fibre Channel uplinks defined in a Cisco UCS Fabric Interconnect, bundled together and configured as a port channel, allowing increased bandwidth and redundancy.   
FCoE |  Fibre Channel over Ethernet. A computer network technology that encapsulates Fibre Channel frames over Ethernet networks.   
KVM |  Keyboard, video, and mouse  
MAC address |  A standardized data link layer address that is required for every device that connects to a Logical Area Network (LAN).   
Port Mappings |  Identifies the ports that are used for specific cable connections between the Fabric Interconnect and other devices.

---

## Page 7: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Fabric-Interconnect-Migration/4-3_1/m-migrating-and-upgrading-cisco-ucs-hardware-components-for-6500-series-fabric-interconnect_4_3.html

# Migrating to Cisco UCS 6500 Series Fabric Interconnects  
  
## Cisco UCS Fabric Interconnect Server Compatibility Matrix - Release 4.3(6b)

### Cisco UCS 6536 FI

Table 1. Cisco UCS 6536 FI - Cisco UCS Rack Servers Cisco VIC |  Direct Attach  (40/100G) |  Direct Attach  (4x25G or 25G QSA28) |  FEX  
---|---|---|---  
93180YC-FX3  (25G server ports) |  93180YC-FX3  (10G server ports) |  2348 UPQ  (10G server ports)  
15427 (UCSC-M-V5Q50GV2) |  Not Supported  |  All Cisco UCS C-Series M8, M7, and M6 servers. |  **Note** |  Reverse breakout is not supported.  
---|---  
All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M8, M7, and M6 servers.  
15237 (UCSC-M-V5D200GV2) |  All Cisco UCS C-Series M8, M7, and M6 servers. |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
15235 (UCSC-P-V5D200G)  |  All Cisco UCS C-Series M8, M7, and M6 servers. |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
15238 (UCSC-M-V5D200G)  |  All Cisco UCS C-Series M6 and M7 servers  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
15425 (UCSC-P-V5Q50G) |  Not Supported |  All Cisco UCS C-Series M8, M7, and M6 servers. |  **Note** |  No reverse breakout supported   
---|---  
All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M8, M7, and M6 servers.  
15428 (UCSC-M-V5Q50G)  |  Not Supported |  All Cisco UCS C-Series M6 and M7 servers  |  **Note** |  No reverse breakout supported   
---|---  
All Cisco UCS C-Series M6 and M7 servers  |  All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M6 and M7 servers   
1497-40G/100G (UCSC-MLOMC100-04)  |  All Cisco UCS C-series M5 servers. |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
1495-40G/100G (UCSC-PCIEC100-04)  |  All Cisco UCS C-Series M6, C-Series M5, and S-series M5 servers  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
1477-40G/100G (UCSC-MV100-04)  |  All Cisco UCS C-series M6 servers. |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
1467-10G/25G (UCSC-MV25-04)  |  Not Supported  |  All Cisco UCS C-Series M6 servers |  All Cisco UCS C-Series M6 servers |  All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M6 servers  
1457-10G/25G (UCSC-MLOMC25Q-04)  |  Not Supported  |  All Cisco UCS C-series M5 servers. |  All Cisco UCS C-series M5 servers. |  All Cisco UCS C-series M5 servers. |  All Cisco UCS C-series M5 servers.  
1455-10G/25G (UCSC-PCIEC25Q-04)  |  Not Supported  |  All Cisco UCS C-Series M6 and M5, and S-Series M5 servers. |  All Cisco UCS C-Series M6 and M5, and S-Series M5 servers. |  All Cisco UCS C-Series M6 and M5, and S-Series M5 servers. |  All Cisco UCS C-Series M6 and M5, and S-Series M5 servers.  
1387 - 40G (UCSC-MLOM-C40Q-03)  |  All Cisco UCS C-Series M5 Servers (40G)  |  Not Supported  |  Not Supported  |  All Cisco UCS C-Series M5 servers with QSA and SFP-10G-SR/LR, SFP-H10GB-CU1/3/5M, SFP-H10GB-ACU7M only. |  All Cisco UCS C-Series M5 servers with QSA and SFP-10G-SR only.  
1385 - 40G (UCSC-PCIE-C40Q-03)  |  All Cisco UCS C-Series M5 Servers (40G)  |  Not Supported  |  Not Supported  |  All Cisco UCS C-Series M5 servers with QSA and SFP-10G-SR/LR, SFP-H10GB-CU1/3/5M, SFP-H10GB-ACU7M only. |  All Cisco UCS C-Series M5 servers with QSA and SFP-10G-SR only.  
Table 2. Cisco UCS 6536 FI - Cisco UCS Blade Servers Cisco VIC |  IOM  
---|---  
2304v1/v2 & /2408 |  UCSX-I-9108-25G or UCSX-I-9108-100G  
15230 (UCSX-ML-V5D200GV2) |  - |  Cisco UCS X210c M8 Cisco UCS X215c M8 Cisco UCS X210c M6, X210c M7, and X410c M7  
15420 + UCS VIC 15000 bridge connector + 15422 (UCSX-ML-V5Q50G + UCSX-V5-BRIDGE + UCSX-ME-V5Q50G) |  \-  |  Cisco UCS X210c M8 Cisco UCS X215c M8 Cisco UCS X210c M6, X210c M7, and X410c M7  
15420 (UCSX-ML-V5Q50G)  |  \-  |  Cisco UCS X210c M8 Cisco UCS X215c M8 Cisco UCS X210c M6, X210c M7, and X410c M7  
15231 (UCSX-ML-V5D200G)  |  \-  |  Cisco UCS X210c M6, X210c M7, and X410c M7  
14425 + UCS VIC 14000 bridge connector + 14825 (UCSX-V4-Q25GML + UCSX-V4-BRIDGE + UCSX-V4-Q25GME) |  \-  |  Cisco UCS X210c M6   
14425 (UCSX-V4-Q25GML)  |  \-  |  Cisco UCS X210c M6   
15411 + Port Expander (UCSB-ML-V5Q10G + UCSB-MLOM-PT-01)  |  Cisco UCS B200 M6  |  \-   
15411 (UCSB-ML-V5Q10G)  |  Cisco UCS B200 M6  |  \-   
1440 + 1480 + Port Expander (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P + UCSB-MLOM-PT-01) |  Cisco UCS B480 M5  |  \-   
1440 + 1480 + 1480 (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P +UCSB-VIC-M84-4P)  |  Cisco UCS B480 M5  |  \-   
1440 + 1480 (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P)  |  Cisco UCS B200 M6, B200 M5, B480 M5  |  \-   
1440 + Port Expander (UCSB-MLOM-40G-04 + UCSB-MLOM-PT-01)  |  Cisco UCS B200 M6, B200 M5, B480 M5  |  \-   
1440 (UCSB-MLOM-40G-04)  |  Cisco UCS B200 M6, B200 M5, B480 M5  |  \-   
1340 + 1380 + Port Expander (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P + UCSB-MLOM-PT-01) |  Cisco UCS B480 M5  |  \-   
1340 + 1380 + 1380 (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P + UCSB-VIC-M83-8P) |  Cisco UCS B480 M5  |  \-   
1340 + 1380 (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P)  |  Cisco UCS B200 M5 and B480 M5  |  \-   
1340 + Port Expander - 10G/40G (UCSB-MLOM-40G-03 + UCSB-MLOM-PT-01)  |  Cisco UCS B200 M5 and B480 M5  |  \-   
1340 - 10G/40G (UCSB-MLOM-40G-03)  |  Cisco UCS B200 M5 and B480 M5  |  \-   
  
### Cisco UCS 6400 and 64108 FIs

Table 3. Cisco UCS 6400 and 64108 FIs - Cisco UCS Rack Servers Cisco VIC |  Direct Attach  (10G/25G)  |  Direct Attach  (4x10G/4x25)  |  Direct Attach  (40G/100G)  |  FEX  
---|---|---|---|---  
2232 PP (10G)  |  93180YC-FX3  (25G server ports)  |  93180YC-FX3  (10G server ports)   
15427 (UCSC-M-V5Q50GV2) |  All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M8, M7, and M6 servers. |  Not Supported |  Not Supported |  All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M8, M7, and M6 servers with SFP-10G-SR/SR-S only.  
15237 (UCSC-M-V5D200GV2) |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
15235 (UCSC-P- V5D200G) |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
15238 (UCSC-M -V5D200G)  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
15425 (UCSC-P- V5Q50G) |  All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M8, M7, and M6 servers. |  Not Supported  |  Not Supported  |  All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M8, M7, and M6 servers with SFP-10G-SR/SR-S only.  
15428 (UCSC-M -V5Q50G)  |  All Cisco UCS C-Series M6 and M7 servers. |  All Cisco UCS C-Series M6 and M7 servers. |  Not Supported  |  Not Supported  |  All Cisco UCS C-Series M6 and M7 servers. |  All Cisco UCS C-Series M8, M7, and M6 servers with SFP-10G-SR/SR-S only.  
|  **Note** |  Break-out is supported (6400 side QSFP, on adapter side two ports can be connected to 1 VIC ( like ports 1 and 2) Reverse-breakout : Not supported  
---|---  
1495-40G/100G  (UCSC -PCIEC100 -04)  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
1497-40G/100G  (UCSC -MLOMC100 -04)  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
1477-40G/100G  (UCSC-MV100 -04)  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
1467-10G/25G (UCSC -MV25-04)  |  All Cisco UCS C-Series M6 servers. |  All Cisco UCS C-Series M6 servers. |  Not Supported  |  All Cisco UCS C-Series M6 servers. |  All Cisco UCS C-Series M6 servers. |  All Cisco UCS C-Series M6 servers with SFP-10G-SR/SR-S only.  
1457-10G/25G (UCSC-MLOM C25Q-04)  |  All Cisco UCS C-Series M5 servers. |  All Cisco UCS C-Series M5 servers. |  Not Supported  |  All Cisco UCS C-Series M5 servers. |  All Cisco UCS C-Series M5 servers. |  All Cisco UCS C-Series M5 servers with SFP-10G-SR/SR-S only.  
1455-10G/25G  (UCSC-PCIEC 25Q-04)  |  All Cisco UCS C-Series M6 and M5, and S-Series M5 servers. |  All Cisco UCS C-Series M6 and M5, and S-Series M5 servers. |  Not Supported  |  All Cisco UCS C-Series M6 and M5, and S-Series M5 servers. |  All Cisco UCS C-Series M6 and M5, and S-Series M5 servers. |  All Cisco UCS C-Series M6 and M5, and S-Series M5 servers with SFP-10G-SR/SR-S only.  
1387 - 40G  (UCSC-MLOM -C40Q-03)  |  All Cisco UCS C-Series M5 servers with QSA at adapter. |  Not Supported  |  Not Supported  |  All Cisco UCS C-Series M5 servers with QSA at adapter. |  Not Supported  |  All Cisco UCS C-Series M5 servers  with QSA and SFP-10G-SR/LR, SFP-H10GB-CU1/3/5M, or SFP-H10GB-ACU7M only.  
1385 - 40G  (UCSC-PCIE -C40Q-03)  |  All Cisco UCS C-Series M5 except C125 M5 and S-Series M5 servers  with QSA at the adapter. |  Not Supported  |  Not Supported  |  All Cisco UCS C-Series M5 except C125 M5 and S-Series M5 servers  with QSA at the adapter. |  Not Supported  |  All Cisco UCS C-Series M5 except C125 M5 and S-Series M5 servers  with QSA and SFP-10G-SR/LR, SFP-H10GB-CU1/3/5M, or SFP-H10GB-ACU7M only.  
Table 4. Cisco UCS 6400 and 64108 FIs - Cisco UCS Blade Servers Cisco VIC |  IOM  
---|---  
2204/2208/2408 |  UCSX-I-9108-25G  
15230 (UCSX-ML-V5D200GV2) |  Not Supported  |  Cisco UCS X210c M8 Cisco UCS X215c M8 Cisco UCS X210c M6, X210c M7, and X410c M7  
15420 +  UCS VIC 15000 bridge connector +  (15422 (UCSX-ML-V5Q50G + UCSX-V5-BRIDGE + UCSX-ME-V5Q50G) |  Not Supported  |  Cisco UCS X210c M8 Cisco UCS X215c M8 Cisco UCS X210c M6, X210c M7, and X410c M7  
15420  (UCSX-ML-V5Q50G) |  Not Supported  |  Cisco UCS X210c M8 Cisco UCS X215c M8 Cisco UCS X210c M6, X210c M7, and X410c M7  
15231  (UCSX-ML-V5D200G) |  Not Supported  |  Cisco UCS X210c M6, X210c M7, and X410c M7  
14425 +  UCS VIC 14000 bridge connector + (14825 (UCSX-V4-Q25GML + UCSX-V4-BRIDGE + UCSX-V4-Q25GME) |  Not Supported  |  Cisco UCS X210c M6  
14425  (UCSX-V4-Q25GML) |  Not Supported  |  Cisco UCS X210c M6  
15411 + Port Expander (UCSB-ML -V5Q10G + UCSB-MLOM -PT-01)  |  B200 M6  |  Not Supported   
15411 (UCSB-ML -V5Q10G)  |  B200 M6  |  Not Supported   
1440 + 1480 + Port Expander  (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P + UCSB-MLOM-PT-01) |  Cisco UCS B480 M5  |  Not Supported   
1440 + 1480 + Port Expander  (UCSB-MLOM-40G-04 +  UCSB-VIC- M84-4P) +  UCSB-MLOM-PT-01) |  Cisco UCS B480 M5  |  Not Supported   
1440 + 1480  (UCSB-MLOM-40G-04 +  UCSB-VIC-M84-4P)  |  Cisco UCS B200 M6, B200 M5, B480 M5  |  Not Supported   
1440 + Port Expander  (UCSB-MLOM-40G-04 +  UCSB-MLOM-PT-01)  |  Cisco UCS B200 M6, B200 M5, B480 M5  |  Not Supported   
1440  (UCSB-MLOM-40G-04)  |  Cisco UCS B200 M6, B200 M5, B480 M5  |  Not Supported   
1340 + 1380 + 1380  (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P + UCSB-VIC-M83-8P) |  Cisco UCS B480 M5  |  Not Supported  
1340 + 1380 + Port Expander  (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P + UCSB-MLOM-PT-01) |  Cisco UCS B480 M5  |  Not Supported  
1340 + Port Expander - 10G/40G  (UCSB-MLOM-40G-03 +  UCSB-MLOM-PT-01)  |  Cisco UCS B200 M5 and B480 M5  |  Not Supported  
1340 + 1380  (UCSB-MLOM-40G-03 +  UCSB-VIC-M83-8P)  |  Cisco UCS B200 M5 and B480 M5  |  Not Supported  
1340 - 10G/40G (UCSB-MLOM-40G-03)  |  Cisco UCS B200 M5 and B480 M5  |  Not Supported  
  
### Cisco UCS 6300 FI

Table 5. Cisco UCS 6300 FI - Cisco UCS Rack Servers Cisco VIC |  Direct Attach |  Direct Attach  (Break-out) |  FEX  
---|---|---|---  
2232 PP |  2348  
15427 (UCSC-M-V5Q50GV2) |  All Cisco UCS C-Series M6 servers. |  All Cisco UCS C-Series M6 servers. |  Not Supported  |  All Cisco UCS C-Series M6 servers.  
15237 (UCSC-M-V5D200GV2) |  All Cisco UCS C-Series M6 servers. |  Not Supported  |  Not Supported  |  Not Supported   
15235 (UCSC-P-V5D200G) |  All Cisco UCS C-Series M6 servers. |  Not Supported  |  Not Supported  |  Not Supported   
15425 (UCSC-P-V5Q50G) |  All Cisco UCS C-Series M6 servers. |  All Cisco UCS C-Series M6 servers. |  Not Supported  |  All Cisco UCS C-Series M6 servers.  
15428 (UCSC-M-V5Q50G)  |  All Cisco UCS C-Series M6 servers. |  All Cisco UCS C-Series M6 servers. |  Not Supported  |  All Cisco UCS C-Series M6 servers.  
15238 (UCSC-M-V5D200G)  |  All Cisco UCS C-Series M6 servers. |  Not Supported  |  Not Supported  |  Not Supported   
1497-40G/100G (UCSC-MLOMC100-04)  |  All Cisco UCS C-Series M5 servers. |  Not Supported  |  Not Supported  |  Not Supported   
1495-40G/100G (UCSC-PCIEC100-04)  |  All Cisco UCS C-Series M6, M5, and S-Series M5 servers. |  Not Supported  |  Not Supported  |  Not Supported   
1477-40G/100G (UCSC-MV100-04)  |  All Cisco UCS C-Series M6 servers. |  Not Supported  |  Not Supported  |  Not Supported   
1467-10G/25G (UCSC-MV25-04)  |  All Cisco UCS C-Series M6 servers (10G speed with 6332-16UP). |  All Cisco UCS C-Series M6 servers. |  All Cisco UCS C-Series M6 servers. |  All Cisco UCS C-Series M6 servers.  
1457-10G/25G (UCSC-MLOMC25Q-04)  |  Cisco UCS C220 M5 and C240 M5 (10G speed with 6332-16UP). |  Cisco UCS C220 M5 and C240 M5 servers. |  Cisco UCS C220 M5 and C240 M5 servers. |  Cisco UCS C220 M5 and C240 M5 servers.  
1455-10G/25G (UCSC-PCIEC25Q-04)  |  All Cisco UCS C-Series M6, M5, and S-Series M5 servers (10G speed with 6332-16UP). |  All Cisco UCS C-Series M6, M5, and S-Series M5 servers. |  All Cisco UCS C-Series M6, M5, and S-Series M5 servers. |  All Cisco UCS C-Series M6, M5, and S-Series M5 servers.  
1387 - 40G (UCSC-MLOM-C40Q-03)  |  All Cisco UCS C-Series M5 servers (40G or 10G using QSA) |  Not Supported  |  All Cisco UCS C-Series M5 servers (QSA at adapter)  |  All Cisco UCS C-Series M5 servers (QSA at adapter)   
1385 - 40G (UCSC-PCIE-C40Q-03)  |  All Cisco UCS C-Series M5 servers (except UCS C125 M5) and S-Series M5 servers (40G or 10G using QSA) |  Not Supported  |  All Cisco UCS C-Series M5 servers (except UCS C125 M5) and S-Series M5 servers (40G or 10G using QSA) |  All Cisco UCS C-Series M5 servers (except UCS C125 M5) and S-Series M5 servers (40G or 10G using QSA)  
Table 6. Cisco UCS 6300 FI - Cisco UCS Blade Servers Cisco VIC |  IOM  
---|---  
2304v1/v2 2204/2208  
15411 + Port Expander  (UCSB-ML-V5Q10G + UCSB-MLOM-PT-01)  |  Cisco UCS B200 M6   
15411 (UCSB-ML-V5Q10G)  |  Cisco UCS B200 M6   
1440 + 1480 + 1480  (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P + UCSB-VIC-M84-4P) |  Cisco UCS B480 M5   
1440 + 1480 + Port Expander (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P + UCSB-MLOM-PT-01) |  Cisco UCS B480 M5   
1440 + 1480 (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P)  |  Cisco UCS B200 M5, B480 M5 and B200 M6 servers   
1440 + Port Expander (UCSB-MLOM-40G-04 + UCSB-MLOM-PT-01)  |  Cisco UCS B200 M5, B480 M5 and B200 M6 servers   
1440 (UCSB-MLOM-40G-04)  |  Cisco UCS B200 M5, B480 M5 and B200 M6 servers   
1340 + 1380 + 1380  (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P +  UCSB-VIC-M83-8P) |  Cisco UCS B480 M5   
1340 + 1380 + Port Expander  (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P +  UCSB-MLOM-PT-01) |  Cisco UCS B480 M5   
1340 + Port Expander - 10G/40G (UCSB-MLOM-40G-03 + UCSB-MLOM-PT-01)  |  Cisco UCS B200 M5 and B480 M5 servers   
1340 + 1380 (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P)  |  Cisco UCS B200 M5 and B480 M5 servers   
1340 - 10G/40G (UCSB-MLOM-40G-03)  |  Cisco UCS B200 M5 and B480 M5 servers   
  
### Cisco UCS 6324 FI

Table 7. Cisco UCS 6324 FI - Cisco UCS Rack Servers Cisco VIC |  Direct Attach (10G)  |  Direct Attach  (Break-out)  
---|---|---  
15428 (UCSC-M-V5Q50G)  |  Not Supported  |  Not Supported   
15238 (UCSC-M-V5D200G)  |  Not Supported  |  Not Supported   
1497-40G/100G (UCSC-MLOMC100-04)  |  Not Supported  |  Not Supported   
1495-40G/100G (UCSC-PCIEC100-04)  |  Not Supported  |  Not Supported   
1477-40G/100G (UCSC-MV100-04)  |  Not Supported  |  Not Supported   
1467-10G/25G (UCSC-MV25-04)  |  Not Supported  |  Not Supported   
1457-10G/25G (UCSC-MLOMC25Q-04)  |  Cisco UCS C220 M5 and C240 M5 servers. |  Cisco UCS C220 M5 and C240 M5 servers.  
1455-10G/25G (UCSC-PCIEC25Q-04)  |  All Cisco UCS C-Series and S-Series M5 servers. |  All Cisco UCS C-Series and S-Series M5 servers.  
1387 - 40G (UCSC-MLOM-C40Q-03)  |  All Cisco UCS C-Series M5 servers. (QSA at the adapter) |  Not Supported   
1385 - 40G (UCSC-PCIE-C40Q-03)  |  All Cisco UCS C-Series M5 servers. (QSA at the adapter) |  Not Supported   
Table 8. Cisco UCS 6324 FI - Cisco UCS Blade Servers Cisco VIC |  IOM |  6324 (Primary Chassis)  
---|---|---  
2204/2208  
15411 (UCSB-ML-V5Q10G)  |  Not Supported  |  Not Supported   
15411 + Port Expander (UCSB-ML-V5Q10G + UCSB-MLOM-PT-01)  |  Not Supported  |  Not Supported   
1440 + 1480 + 1480 (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P +UCSB-VIC-M84-4P)  |  Not Supported  |  Cisco UCS B480 M5  
1440 + 1480 + Port Expander (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P) + UCSB-MLOM-PT-01) |  Not Supported  |  Cisco UCS B480 M5  
1440 + 1480 (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P)  |  Not Supported  |  Cisco UCS B200 M5, B480 M5, and B200 M6  
1440 + Port Expander (UCSB-MLOM-40G-04 + UCSB-MLOM-PT-01)  |  Not Supported  |  Cisco UCS B200 M5, B480 M5, and B200 M6  
1440 (UCSB-MLOM-40G-04)  |  Not Supported  |  Cisco UCS B200 M5, B480 M5, and B200 M6  
1340 + 1380 + 1380  (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P +  UCSB-VIC-M83-8P) |  Cisco UCS B480 M5  |  Cisco UCS B480 M5   
1340 + 1380 + Port Expander  (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P +  UCSB-MLOM-PT-01) |  Cisco UCS B480 M5  |  Cisco UCS B480 M5   
1340 + 1380  (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P)  |  Cisco UCS B200 M5 and B480 M5  |  Cisco UCS B200 M5 and B480 M5   
1340 + Port Expander - 10G/40G  (UCSB-MLOM-40G-03 + UCSB-MLOM-PT-01)  |  Cisco UCS B200 M5 and B480 M5  |  Cisco UCS B200 M5 and B480 M5   
1340 - 10G/40G (UCSB-MLOM-40G-03)  |  Cisco UCS B200 M5 and B480 M5  |  Cisco UCS B200 M5 and B480 M5   
  
### Cisco UCS Fabric Interconnect 9108 100G

Table 9. Cisco UCS FI 9108 100G - Cisco UCS Blade Servers Cisco VIC |  UCSX-S9108-100G (Primary Chassis)  
---|---  
14425 (UCSX-V4-Q25GML) |  Cisco UCS X210c M6  
14425 + UCS VIC 14000 bridge connector + 14825  (UCSX-V4-Q25GML + UCSX-V4-BRIDGE +  UCSX-V4-Q25GME) |  Cisco UCS X210c M6  
15231 (UCSX-ML-V5D200G) |  Cisco UCS X410c M7, X210c M7, X210c M6  
15230 (UCSX-ML-V5D200GV2) |  Cisco UCS X210c M8, X215c M8, X410c M7, X210c M7, and X210c M6   
15420 (UCSX-ML-V5Q50G) |  Cisco UCS X210c M8, X215c M8, X410c M7, X210c M7, and X210c M6   
15420 + UCS VIC 15000 bridge connector + 15422  (UCSX-ML-V5Q50G + UCSX-V5-BRIDGE +  UCSX-ME-V5Q50G) |  Cisco UCS X210c M8, X215c M8, X410c M7, X210c M7, and X210c M6   
  
Cisco UCS 6400 Series Fabric Interconnect Migration

## Cisco UCS 6400 Series Fabric Interconnect Migration Considerations

Beginning with Cisco UCS Manager, Release 4.3(2b), You can migrate Cisco UCS 6400 Series Fabric Interconnects to Cisco UCS 6536 Fabric Interconnect with B-Series servers, C-Series, or S-Series servers. 

To migrate from Cisco UCS 6400 Series Fabric Interconnects to Cisco UCS 6536 Fabric Interconnect: 

  * Cisco UCS 6400 Series Fabric Interconnects must be on Cisco UCS Manager 4.3(2b) or a later release. 

  * Cisco UCS 6536 Fabric Interconnect must be loaded with the same Infrastructure Firmware version that is on the Cisco UCS 6400 Series Fabric Interconnect that it will replace. 


Prerequisites

Before performing the migration from Cisco UCS 6400 Series Fabric Interconnects to Cisco UCS 6536 Fabric Interconnect, ensure that the following prerequisites are met for a successful migration: 

  * Back up and export Cisco UCS Manager configuration before initiating the upgrade. 

  * Take an inventory of the Cisco UCS domain and remove any unsupported hardware. 

  * Ensure to enable the cluster failover.

  * Do not attempt to implement new software features from the new Cisco UCS software version until all required hardware is installed. 

  * Validate the software features and configurations between Cisco UCS 6400 series and UCS 6536 Fabric Interconnects. Before migration, ensure that 6400 series Fabric Interconnect is reconfigured to only have features that are supported with 6536 Fabric Interconnects. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

This is one of the most common reasons for migration failures.

* * *  
  
---|---  
  * Make sure both Cisco UCS 6400 series and 6500 series Fabric Interconnects are on the same UCSM build before migration.

  * Licenses from Cisco UCS 6400 Series Fabric Interconnects are not transferable to Cisco UCS 6500 Series Fabric Interconnects. Cisco UCS 6500 Series Fabric Interconnects has perpetual license enabled by default. 

  * Standalone installations should expect down time. In a cluster configuration, migrating the Fabric Interconnects can result in a small traffic disruption when the traffic fails over from one Fabric Interconnect to another. To avoid that there is no permanent traffic loss during migration, ensure that there is redundancy in the UCS domain on both Fabric Interconnects before migration and test the redundancy before starting the migration. 

  * Cisco UCS 6536 Fabric Interconnect use the IDLE fill pattern for FC uplink ports and FC storage ports when using 8 Gbps speed. 

When migrating to Cisco UCS 6536 Fabric Interconnect and configuring FC Uplink Ports or FC Storage Ports at 8Gbps speed, ensure that the fill pattern is set as IDLE on the corresponding FC switch ports and the direct-attached FC storage array ports. If the fill pattern is not set as IDLE, FC uplink ports and FC storage ports operating at 8 Gbps might go to an errDisabled state, lose SYNC intermittently, or receive errors or bad packets. 

Cisco UCS 6536 Fabric Interconnects supports 8 Gbps only with fill-pattern set to IDLE for direct-attached FC connectivity (FC uplink ports or FC storage ports). This limitation is not applicable for Cisco UCS 6536 Fabric Interconnects with Fibre Channel (FC) ports at 16 Gbps and 32 Gbps. When migrating to Cisco UCS 6536 Fabric Interconnect for direct-attached storage arrays that don’t support IDLE fill-pattern at 8 Gbps do one of the following: 

  * Use a SAN switch between the Cisco UCS 6536 Fabric Interconnect and the storage array with 8 GB FC connectivity. 

  * Upgrade the storage array to 16 GB or 32 GB FC connectivity.

  * Ensure the latest firmware bundle is downloaded and upgraded through GUI or CLI. Incase of attempting to upgrade the firmware bundle using other methods (loader prompt/erase configuration) can result in missing package version. 

  * Before migration, make sure that the FC Speed is 8Gbps on Cisco UCS 6400 Fabric Interconnects or the connected switch supports 8Gbps speed. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Post migration, you can configure the FC Port (Scalability Port) speed on Cisco UCS 6500 Fabric Interconnects.

* * *  
  
---|---  
  * Migrating to different IOM models can result in peer communication issue between IOMs of the Primary and Secondary Fabric Interconnects. 

  * Make a detailed record of the cabling between FEX and fabric interconnects. You must preserve the physical port mapping to maintain the server pinning already configured and minimize down time. 

  * For a cluster configuration, both fabric interconnects must have symmetrical connection topologies between fabric interconnect and FEX. 

  * Use the same speed cables on all the adapter ports that are connected to same Fabric Interconnect. Cisco UCS VIC adapter ports connected to Cisco UCS 6536 fabric interconnect through a mix of 10G and 25G cables can result in UCS rack-mount server discovery failure and ports moving to suspended state. 

  * Cisco UCS 6536 Fabric Interconnect only supports 25/40/100G direct connectivity for C-series rack servers and 10G direct-connect is not supported on C-series rack servers. The Cisco UCS 6536 Fabric Interconnect supports 10G server connectivity only with 2348-UPQ FEX. 

  * A WWN pool can include only WWNNs or WWPNs in the ranges from 20:00:00:00:00:00:00:00 to 20:FF:00:FF:FF:FF:FF:FF or from 50:00:00:00:00:00:00:00 to 5F:FF:00:FF:FF:FF:FF:FF. All other WWN ranges are reserved. When fibre channel traffic is sent through the UCS infrastructure the source WWPN is converted to a MAC address. You cannot use WWPN pool which can translate to source multicast MAC addresses. To ensure the uniqueness of the Cisco UCS WWNNs and WWPNs in the SAN fabric, Cisco recommends using the following WWN prefix for all blocks in a pool: 20:00:00:25:B5:XX:XX:XX 

  * Unconfigure the fibre channel ports on the migrating subordinate Cisco UCS 6400 series Fabric Interconnect and reconfigure on the Cisco UCS 6536 Fabric Interconnect. 


Recommendations

Following are the best practices for a successful migration:

  * For minimal disruption during migration, ensure that there is redundancy for Ethernet and FC traffic from the servers in the UCS domain across both 6400 series fabric interconnects before migration. 

  * Changes to the topology, such as the number of servers or uplink connections, should be performed after the fabric interconnect migration is complete. 

  * During the migration of Fabric Interconnects, ensure the Cluster ID is not changed.

  * During the migration, image synchronization between fabric interconnects is not allowed. This is done to prevent incompatible images from getting synchronized. It is necessary to download B-Series, C-Series, and S-Series server software bundles again after migration is complete. 

  * During the migration, ensure that VLAN is not created in the range of 3915 to 4042 which are the reserved VLAN range for Cisco UCS 6536 Fabric Interconnects. 

  * The Cisco UCS 6536 Fabric Interconnect supports only port-channel mode for chassis-discovery. Hence, before starting migration, change the chassis/FEX discovery policy on the Cisco UCS 6400 series Fabric Interconnect to port-channel and immediately re-acknowledge the chassis. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The migration can fail when the chassis is not immediately re-acknowledged.

* * *  
  
---|---  

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For more information on migrating Cisco UCS 6400 series Fabric Interconnects to Cisco UCS 6500 series Fabric Interconnect with UCS Central, see Considerations for migrating Cisco UCS 6400 Series Fabric Interconnects to Cisco UCS 6500 Series Fabric Interconnects with Cisco UCS Central. 

* * *  
  
---|---  
  
  * Validating Feature Configurations for Cisco UCS 6536 before Upgrade
  * Considerations for migrating Cisco UCS 6400 Series Fabric Interconnects to Cisco UCS 6500 Series Fabric Interconnects with Cisco UCS Central


### Validating Feature Configurations for Cisco UCS 6536 before Upgrade

Cisco UCS 6536 Fabric Interconnect does not support some software features that were allowed with Cisco UCS 6400 Series Fabric Interconnect. Some of these features will become available at a later software release. 

Table 10. Features that needs special attention prior to upgrading Feature |  Remediation  
---|---  
License Management |  Licensing for Cisco UCS 6536 Fabric Interconnect is not a port-based license like in previous generation Fabric Interconnects.  All ports are enabled through a perpetual license in Cisco UCS 6536 Fabric Interconnect and no license installation is required.  
Chassis and fabric extender I/O port channel |  Select a port channel to the I/O module (IOM).  
Multicast optimization |  Verify that multicast optimization is not enabled under the LAN quality-of-service (QoS) system classes  
Fabric forwarding mode for Ethernet |  Verify that the Ethernet forwarding mode is set to End Host Mode Only.   
Fabric forwarding mode for Fibre Channel |  Verify that Fibre Channel forwarding mode is set to End Host Mode or FC Switching Mode.   
Cisco NetFlow |  Unconfigure NetFlow.  
MAC Security  |  Select Allow for MAC security.   
VM-FEX |  Remove port profiles and Cisco UCS Manager ESXi or SCVMM related configurations.  
Dynamic vNIC connection policies |  Set the dynamic vNIC connection policy in the vNIC profile to Not set.   
Cisco Switched Port Analyzer (SPAN) |  Use receive (RX) direction only. The installer will change SPAN to the RX direction and send an alert indicating that this setting is being changed.   
  
Failure to comply with these remediation steps will result in a migration warning alert during the migration process and prevent the fabric interconnects from synchronizing. 

### Considerations for migrating Cisco UCS 6400 Series Fabric Interconnects to Cisco UCS 6500 Series Fabric Interconnects with Cisco UCS Central 

In addition to Cisco UCS 6400 Series Fabric Interconnect Migration Considerations, consider the following prerequisites when migrating with Cisco UCS Central: 

  * Before initiating the migration, ensure to have a complete backup of Cisco UCS Manager and UCS Central configurations.

  * To avoid any configuration issues during migration, make sure the following policies on Policy Resolution Control is set to Local in Cisco UCS Manager: 

  * Infrastructure and Catalog Firmware Policy

  * Equipment Policy

  * Port Configuration Policy


## Migrating from UCS 6400 Series Fabric Interconnects to UCS 6536 Fabric Interconnects

Cisco UCS 6400 Series Fabric Interconnects include Cisco UCS 6454 and Cisco UCS 64108. You can migrate from Cisco UCS 6400 Series Fabric Interconnects to Cisco UCS 6536 Fabric Interconnect. After migrating to Cisco UCS 6536 Fabric Interconnect, Cisco recommends not to migrate back to UCS 6400 Series Fabric Interconnect. 

The Cisco UCS 6536 Fabric Interconnect supports only port-channel mode for chassis-discovery. On changing the chassis or FEX discovery policy to port-channel, the chassis needs to be re-acknowledged before proceeding with the migration. 

To acknowledge the chassis in Cisco UCS Manager, do the following:

  1. In the Navigation pane of Cisco UCS Manager, click Equipment. 

  2. Click the Equipment node. 

  3. In the Work pane, click the Policies tab. 

  4. Click the Global Policies subtab. 

  5. In the Chassis/FEX Discovery Policy area, set the Link Grouping Preference field to Port Channel. 

  6. Expand Equipment > Chassis, and choose the chassis that you want to acknowledge. 

  7. In the Work pane, click the General tab. 

  8. In the Actions area, click Acknowledge Chassis. 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For more information about how to perform configuration procedures in Cisco UCS Manager, see the appropriate [Cisco UCS Manager Configuration Guide](http://www.cisco.com/en/US/products/ps10281/products_installation_and_configuration_guides_list.html). 

* * *  
  
---|---  
  
### Procedure

* * *

**Step 1** |  Move the traffic to the primary fabric interconnect. This can be performed in two ways: fabric evacuation and uplink disablement. Use the below flowchart to choose between the two based on your Cisco UCS domain server and connectivity.![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472394.png) |  **Note** |  For direct-attached rack servers, only uplink disablement is supported.  
---|---  
**Step 2** |  Verify that all traffic has failed over to the primary fabric interconnect. Unconfigure all server ports or fibre channel ports on the subordinate fabric interconnect.  For more information, see the _Fabric Interconnect Traffic Evacuation_ section in the _Guidelines and Prerequisites_ chapter of the [Cisco UCS Manager Firmware Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html).   
**Step 3** |  Power down the old subordinate fabric interconnect and disconnect the power and the L1/L2 cables. If you are monitoring the migration using a KVM session to a server host, you may need to reconnect it after you powered down the secondary fabric interconnect.   
**Step 4** |  Mount the replacement Cisco UCS 6536 Fabric Interconnect into either the same rack or an adjacent rack. |  **Note** |  As a best practice, you should label the cables.  
---|---  
**Step 5** |  Connect the L1/L2 cables and the server ports according to your port mapping plan.  
**Step 6** |  Power up the new fabric interconnect. If it is connected correctly, the new subordinate fabric interconnect will detect that it is being added to an existing cluster.   
**Step 7** |  The subordinate Cisco UCS 6536 Fabric Interconnect will automatically synchronize the configuration and database/state information from the primary UCS 6400 Series Fabric Interconnect.  Synchronization between primary and subordinate fabric interconnects can take several minutes. You may see an error message that will persist until the server ports are enabled.  The port configuration is copied from the subordinate Fabric Interconnect to the new Fabric Interconnect. |  **Note** |  Skip to Step 10 incase of replacing with a different IOM or FEX during migration. For more information on the compatibility matrix of supported IOM or FEX on the Fabric Interconnect, see [Ports on the Cisco UCS Fabric Interconnects](m_overview-4-1.html#id_118320)  
---|---  
**Step 8** |  Unified ports on the 6500 series fabric interconnect are different from the unified port ordering on the 6400 series Fabric Interconnect.  |  **Note** | 

  * When you convert from ethernet ports to fibre channel ports, a reboot is required. Fibre channel ports are converted in blocks of four (breakout ports). 
  * For more information on _Configuring FC Uplink port_ or _Converting FC storage port to FC uplink port_ , see the _LAN Ports and Port Channels_ chapter in [Cisco UCS Manager Network Management Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Network-Mgmt/4-2/b_UCSM_Network_Mgmt_Guide_4_2/b_UCSM_Network_Mgmt_Guide_chapter_0100.html#task_A7ED517EE3C9482FA063827E4CBD25AE). 

  
---|---  
**Step 9** |  Configure the network uplink ports on the new Cisco UCS 6536 fabric interconnect.  
**Step 10** |  Match the old configuration from Cisco UCS 6400 Fabric Interconnect for the port-channel. Add uplink ports to the necessary port-channel or any other previous configuration required for the port-channel. Wait for configuration to complete before proceeding to the next step.  |  **Note** |  Waiting to enable the server ports prevents the svc_sam_bladeAG service from communicating with chassis and servers. In previous migrations, when enabling server ports at the same time as the uplink ports, it would cause topping out (pinning) the CPU to near 100% on the primary fabric interconnect. When there is high CPU usage, the user interface becomes unresponsive and the svc_sam_bladeAG service must be restarted to recover.   
---|---  
**Step 11** |  Reconfigure the server ports or fibre channel ports.

  1. If you have changed port mappings, you may need to reacknowledge the IOM, FEX, or direct-connect rack server connected to the subordinate fabric interconnect. 
  2. Verify and if necessary, you can reconfigure ethernet ports as server ports.
  3. Skip to Step 13 to verify the data path.

  
**Step 12** |  To remove and replace the new IOM or FEX and reconfigure the server ports, do the following:

  1. Remove the existing IOM connected to the subordinate Fabric Interconnect and replace it with a supported IOM of Cisco UCS 6536 Fabric Interconnect. 
  2. Verify if any modifications are required for the cable connections. |  **Note** |  For more information, see Cisco UCS Fabric Interconnect Server Compatibility Matrix - Release 4.3(6b).   
---|---  
  3. Reconfigure the new IOM to maintain the same port mappings. If port mapping were not preserved, configure the server ports accordingly. 

  4. Reacknowledge the IOM connected to the subordinate Fabric Interconnect.


**Note** |  When migrating from Cisco UCS 6400 to Cisco UCS 6536, IOM-220x can be replaced with IOM-2304v2 or IOM-2408.  
---|---  
**Step 13** |  Verify that the data path is ready. For more information, see the _Verifying that Dynamic vNICs Are Up and Running_ section in the _Guidelines and Prerequisites_ chapter of the [Cisco UCS Manager Firmware Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html).  Ensure that all faults are resolved before proceeding with next step.

  1. Verify, and if necessary, reconfigure the SAN pin group for fibre channel ports in the associated service profile.
  2. Verify, and if necessary, reconfigure the LAN pin group for ethernet ports in the associated service profile.
  3. Verify, and if necessary, reconfigure the port channel for uplink ethernet ports.

  
**Step 14** |  Move the traffic back to the new subordinate fabric interconnect. If you used the fabric evacuation method, then deselect fabric evacuation. If you disabled the uplinks (Ethernet and Fibre Channel), then re-enable the uplinks. Verify that traffic is flowing correctly on the new subordinate fabric interconnect.   
**Step 15** |  After verifying that traffic is flowing on the subordinate fabric interconnect, promote the subordinate fabric interconnect to primary using the below commands: 

  * UCS-A #connect local-mgmt: This command connects to the local management interface of the cluster.
  * UCS-A (local-mgmt) #cluster{lead {a|b}} or UCS-A (local-mgmt) #cluster{force primary{a|b}}: The cluster lead command and cluster force primary command are two separate commands that can be used for promoting the fabric interconnect. 

|  **Note** |  Ensure that the primary fabric interconnect is Cisco UCS 6536 Fabric Interconnect.  
---|---  
**Step 16** |  Cable the second new fabric interconnect identically to the first and repeat the steps for the other fabric interconnect replacements to complete the migration.   
  
* * *

Cisco UCS 6300 Series Fabric Interconnect Migration

## Cisco UCS 6300 Series Fabric Interconnect Migration Considerations

Beginning with Cisco UCS Manager, Release 4.2(3b), Cisco UCS Manager provides support for Cisco UCS 6536 Fabric Interconnect. You can migrate Cisco UCS 6300 Series Fabric Interconnects to Cisco UCS 6536 Fabric Interconnect with B-Series servers, C-Series, or S-Series servers. 

To migrate from Cisco UCS 6300 Series Fabric Interconnects to Cisco UCS 6536 Fabric Interconnect: 

  * Cisco UCS 6300 Series Fabric Interconnects must be on Cisco UCS Manager 4.2(3b) or a later release. 

  * Cisco UCS 6536 Fabric Interconnect must be loaded with the same Infrastructure Firmware version that is on the Cisco UCS 6300 Series Fabric Interconnect that it will replace. 


Prerequisites

Before performing the migration from Cisco UCS 6300 Series Fabric Interconnects to Cisco UCS 6536 Fabric Interconnect, ensure that the following prerequisites are met for a successful migration: 

  * Back up and export Cisco UCS Manager configuration before initiating the upgrade. Ensure that the backup file from the 6300 Series Fabric Interconnects is compatible with the 6536 Fabric Interconnects. You can follow any of the backup methods: 

  * **Online Migration:** This method allows for backing up the configuration while the Fabric Interconnect is operational. It ensures minimal disruption and maintains continuous availability during the migration process. 

  * **Offline Migration:** This method involves taking the fabric interconnect offline to perform the backup, which may result in downtime. 

  * Take an inventory of the Cisco UCS domain and remove any unsupported hardware. 

  * Ensure to enable the cluster failover.

  * Do not attempt to implement new software features from the new Cisco UCS software version until all required hardware is installed. 

  * Validate the software features and configurations between Cisco UCS 6300 series and UCS 6536 Fabric Interconnects. Before migration, ensure that 6300 series Fabric Interconnect is reconfigured to only have features that are supported with 6536 Fabric Interconnects. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

This is one of the most common reasons for migration failures. 

* * *  
  
---|---  
  * Make sure both Cisco UCS 6300 series and 6500 series Fabric Interconnects are on the same UCSM build before migration.

  * Licenses from Cisco UCS 6300 Series Fabric Interconnects are not transferable to Cisco UCS 6500 Series Fabric Interconnects.

  * Standalone installations should expect down time. In a cluster configuration, migrating the Fabric Interconnects can result in a small traffic disruption when the traffic fails over from one Fabric Interconnect to another. To avoid that there is no permanent traffic loss during migration, ensure that there is redundancy in the UCS domain on both Fabric Interconnects before migration and test the redundancy before starting the migration. 

  * Cisco UCS 6536 Fabric Interconnect use the IDLE fill pattern for FC uplink ports and FC storage ports when using 8 Gbps speed. 

When migrating to Cisco UCS 6536 Fabric Interconnect and configuring FC Uplink Ports or FC Storage Ports at 8Gbps speed, ensure that the fill pattern is set as IDLE on the corresponding FC switch ports and the direct-attached FC storage array ports. If the fill pattern is not set as IDLE, FC uplink ports and FC storage ports operating at 8 Gbps might go to an errDisabled state, lose SYNC intermittently, or receive errors or bad packets. 

Cisco UCS 6536 Fabric Interconnects supports 8 Gbps only with fill-pattern set to IDLE for direct-attached FC connectivity (FC uplink ports or FC storage ports). This limitation is not applicable for Cisco UCS 6536 Fabric Interconnects with Fibre Channel (FC) ports at 16 Gbps and 32 Gbps. When migrating to Cisco UCS 6536 Fabric Interconnect for direct-attached storage arrays that don’t support IDLE fill-pattern at 8 Gbps do one of the following: 

  * Use a SAN switch between the Cisco UCS 6536 Fabric Interconnect and the storage array with 8 GB FC connectivity. 

  * Upgrade the storage array to 16 GB or 32 GB FC connectivity.

  * Ensure the latest firmware bundle is downloaded and upgraded through GUI or CLI. Incase of attempting to upgrade the firmware bundle using other methods (loader prompt/erase configuration) can result in missing package version. 

  * Before migration, make sure that the FC Speed is 8Gbps on Cisco UCS 6300 Fabric Interconnects or the connected switch supports 8Gbps speed. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Post migration, you can configure the FC Port (Scalability Port) speed on Cisco UCS 6500 Fabric Interconnects.

* * *  
  
---|---  
  * Migrating to different IOM models can result in peer communication issue between IOMs of the Primary and Secondary Fabric Interconnects. 

  * Make a detailed record of the cabling between FEX and fabric interconnects. You must preserve the physical port mapping to maintain the server pinning already configured and minimize down time. 

  * For a cluster configuration, both fabric interconnects must have symmetrical connection topologies between fabric interconnect and FEX. 

  * Use the same speed cables on all the adapter ports that are connected to same Fabric Interconnect. Cisco UCS VIC adapter ports connected to Cisco UCS 6536 fabric interconnect through a mix of 10G and 25G cables can result in UCS rack-mount server discovery failure and ports moving to suspended state. 

  * Cisco UCS 6536 Fabric Interconnect only supports 25/40/100G direct connectivity for C-series rack servers and 10G direct-connect is not supported on C-series rack servers. The Cisco UCS 6536 Fabric Interconnect supports 10G server connectivity only with 2348-UPQ FEX. 

  * A WWN pool can include only WWNNs or WWPNs in the ranges from 20:00:00:00:00:00:00:00 to 20:FF:00:FF:FF:FF:FF:FF or from 50:00:00:00:00:00:00:00 to 5F:FF:00:FF:FF:FF:FF:FF. All other WWN ranges are reserved. When fibre channel traffic is sent through the UCS infrastructure the source WWPN is converted to a MAC address. You cannot use WWPN pool which can translate to source multicast MAC addresses. To ensure the uniqueness of the Cisco UCS WWNNs and WWPNs in the SAN fabric, Cisco recommends using the following WWN prefix for all blocks in a pool: 20:00:00:25:B5:XX:XX:XX 

  * Unconfigure the fibre channel ports on the migrating subordinate Cisco UCS 6300 series Fabric Interconnect and reconfigure on the Cisco UCS 6536 Fabric Interconnect. 


Recommendations

Following are the best practices for a successful migration:

  * For minimal disruption during migration, ensure that there is redundancy for Ethernet and FC traffic from the servers in the UCS domain across both 6300 series fabric interconnects before migration. 

  * Changes to the topology, such as the number of servers or uplink connections, should be performed after the fabric interconnect migration is complete. 

  * During the migration of Fabric Interconnects, ensure the Cluster ID is not changed.

  * During the migration, image synchronization between fabric interconnects is not allowed. This is done to prevent incompatible images from getting synchronized. It is necessary to download B-Series, C-Series, and S-Series server software bundles again after migration is complete. 

  * During the migration, ensure that VLAN is not created in the range of 3915 to 4042 which are the reserved VLAN range for Cisco UCS 6536 Fabric Interconnects. 

  * The Cisco UCS 6536 Fabric Interconnect supports only port-channel mode for chassis-discovery. Hence change the Chassis/FEX discovery policy on the Cisco UCS 6300 series Fabric Interconnect to port-channel and immediately re-acknowledge the Cisco UCS 5108 chassis. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The migration can fail when the chassis is not immediately re-acknowledged.

* * *  
  
---|---  


### Validating Feature Configurations for Cisco UCS 6536 before Upgrade

Cisco UCS 6536 Fabric Interconnect does not support some software features that were allowed with Cisco UCS 6300 Fabric Interconnect. Some of these features will become available at a later software release. 

Table 11. Features that needs special attention prior to upgrading Feature |  Remediation  
---|---  
License Management |  Licensing for Cisco UCS 6536 Fabric Interconnect is not a port-based license like in previous generation Fabric Interconnects.  All ports are enabled through a perpetual license in Cisco UCS 6536 Fabric Interconnect and no license installation is required.  
Chassis and fabric extender I/O port channel |  Select a port channel to the I/O module (IOM).  
Multicast optimization |  Verify that multicast optimization is not enabled under the LAN quality-of-service (QoS) system classes  
Fabric forwarding mode for Ethernet |  Verify that the Ethernet forwarding mode is set to End Host Mode Only.   
Fabric forwarding mode for Fibre Channel |  Verify that Fibre Channel forwarding mode is set to End Host Mode or FC Switching Mode.   
Cisco NetFlow |  Unconfigure NetFlow.  
MAC Security  |  Select Allow for MAC security.   
VM-FEX |  Remove port profiles and Cisco UCS Manager ESXi or SCVMM related configurations.  
Dynamic vNIC connection policies |  Set the dynamic vNIC connection policy in the vNIC profile to Not set.   
Cisco Switched Port Analyzer (SPAN) |  Use receive (RX) direction only. The installer will change SPAN to the RX direction and send an alert indicating that this setting is being changed.   
  
Failure to comply with these remediation steps will result in a migration warning alert during the migration process and prevent the fabric interconnects from synchronizing. 

## Migrating from UCS 6300 Series Fabric Interconnects to UCS 6536 Fabric Interconnects

Cisco UCS 6300 Series Fabric Interconnects include Cisco UCS 6332 and Cisco UCS 6332-16UP. You can migrate from Cisco UCS 6300 Series Fabric Interconnects to Cisco UCS 6536 Fabric Interconnect. 

The Cisco UCS 6536 Fabric Interconnect supports only port-channel mode for chassis-discovery. On changing the chassis or FEX discovery policy to port-channel, the chassis needs to be re-acknowledged before proceeding with the migration. 

To acknowledge the chassis in Cisco UCS Manager, do the following:

  1. In the Navigation pane of Cisco UCS Manager, click Equipment. 

  2. Click the Equipment node. 

  3. In the Work pane, click the Policies tab. 

  4. Click the Global Policies subtab. 

  5. In the Chassis/FEX Discovery Policy area, set the Link Grouping Preference field to Port Channel. 

  6. Expand Equipment > Chassis, and choose the chassis that you want to acknowledge. 

  7. In the Work pane, click the General tab. 

  8. In the Actions area, click Acknowledge Chassis. 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For more information about how to perform configuration procedures in Cisco UCS Manager, see the appropriate [Cisco UCS Manager Configuration Guide](http://www.cisco.com/en/US/products/ps10281/products_installation_and_configuration_guides_list.html). 

* * *  
  
---|---  
  
### Procedure

* * *

**Step 1** |  Move the traffic to the primary fabric interconnect. This can be performed in two ways: fabric evacuation and uplink disablement. Use the below flowchart to choose between the two based on your Cisco UCS domain server and connectivity.![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472394.png) |  **Note** |  For direct-attached rack servers, only uplink disablement is supported.  
---|---  
**Step 2** |  Verify that all traffic has failed over to the primary fabric interconnect. Unconfigure all server ports or fibre channel ports on the subordinate fabric interconnect.  |  **Note** |  For more information, see the _Fabric Interconnect Traffic Evacuation_ section in the _Guidelines and Prerequisites_ chapter of the [Cisco UCS Manager Firmware Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html).   
---|---  
**Step 3** |  Power down the old subordinate fabric interconnect and disconnect the power and the L1/L2 cables. If you are monitoring the migration using a KVM session to a server host, you may need to reconnect it after you powered down the secondary fabric interconnect.   
**Step 4** |  Mount the replacement Cisco UCS 6536 Fabric Interconnect into either the same rack or an adjacent rack. |  **Note** |  As a best practice, you should label the cables.  
---|---  
**Step 5** |  Connect the L1/L2 cables and the server ports according to your port mapping plan.  
**Step 6** |  Power up the new fabric interconnect. If it is connected correctly, the new subordinate fabric interconnect will detect that it is being added to an existing cluster.   
**Step 7** |  The subordinate Cisco UCS 6536 Fabric Interconnect will automatically synchronize the configuration and database/state information from the primary UCS 6300 Series Fabric Interconnect.  Synchronization between primary and subordinate fabric interconnects can take several minutes. You may see an error message that will persist until the server ports are enabled.  The port configuration is copied from the subordinate Fabric Interconnect to the new Fabric Interconnect. |  **Note** |  Skip to Step 10 incase of replacing with a different IOM or FEX during migration. For more information on the compatibility matrix of supported IOM or FEX on the Fabric Interconnect, see [Ports on the Cisco UCS Fabric Interconnects](m_overview-4-1.html#id_118320)  
---|---  
**Step 8** |  Unified ports on the 6500 series fabric interconnect are different from the unified port ordering on the 6300 series Fabric Interconnect.  |  **Note** | 

  * When you convert from ethernet ports to fibre channel ports, a reboot is required. Fibre channel ports are converted in blocks of four (breakout ports). 
  * For more information on _Configuring FC Uplink port_ or _Converting FC Storage Port to FC Uplink port_ , refer the _LAN Ports and Port Channels_ chapter in [Cisco UCS Manager Network Management Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Network-Mgmt/4-2/b_UCSM_Network_Mgmt_Guide_4_2/b_UCSM_Network_Mgmt_Guide_chapter_0100.html#task_A7ED517EE3C9482FA063827E4CBD25AE). 

  
---|---  
**Step 9** |  Reconfigure the server ports or fibre channel ports that were unconfigured in Step 2.

  1. If you have changed port mappings, you may need to reacknowledge the IOM, FEX, or direct-connect rack server connected to the subordinate fabric interconnect. 
  2. Verify and if necessary, you can reconfigure ethernet ports as server ports.
  3. Skip to Step 11 to verify the data path.

  
**Step 10** |  To remove and replace the new IOM or FEX and reconfigure the server ports, do the following:

  1. Remove the existing IOM connected to the subordinate Fabric Interconnect and replace it with a supported IOM of Cisco UCS 6536 Fabric Interconnect. 
  2. Verify if any modifications are required for the cable connections. |  **Note** |  For more information, see Cisco UCS Fabric Interconnect Server Compatibility Matrix - Release 4.3(6b).   
---|---  
  3. Reconfigure the new IOM to maintain the same port mappings. If port mapping were not preserved, configure the server ports accordingly. 

  4. Reacknowledge the IOM connected to the subordinate Fabric Interconnect.


**Note** |  When migrating from Cisco UCS 6300 to Cisco UCS 6536, IOM-220x can be replaced with IOM-2304v2 or IOM-2408 and IOM-2304v1/v2 with IOM-2408.   
---|---  
**Step 11** |  Verify that the data path is ready. For more information, see the _Verifying that Dynamic vNICs Are Up and Running_ section in the _Guidelines and Prerequisites_ chapter of the [Cisco UCS Manager Firmware Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html).  Ensure that all faults are resolved before proceeding with next step.

  1. Verify, and if necessary, reconfigure the SAN pin group for Fibre Channel ports in the associated service profile.
  2. Verify, and if necessary, reconfigure the LAN pin group for Ethernet ports in the associated service profile.
  3. Verify, and if necessary, reconfigure the port channel for uplink Ethernet ports.

  
**Step 12** |  Move the traffic back to the new subordinate fabric interconnect. If you used the fabric evacuation method, then deselect fabric evacuation. If you disabled the uplinks (Ethernet and Fibre Channel), then re-enable the uplinks. Verify that traffic is flowing correctly on the new subordinate fabric interconnect.   
**Step 13** |  After verifying that traffic is flowing on the subordinate fabric interconnect, promote the subordinate fabric interconnect to primary using the below commands: 

  * UCS-A #connect local-mgmt: This command connects to the local management interface of the cluster.
  * UCS-A (local-mgmt) #cluster{lead {a|b}} or UCS-A (local-mgmt) #cluster{force primary{a|b}}: The cluster lead command and cluster force primary command are two separate commands that can be used for promoting the fabric interconnect. 

|  **Note** |  Ensure that the primary fabric interconnect is Cisco UCS 6536 Fabric Interconnect.  
---|---  
**Step 14** |  Cable the second new fabric interconnect identically to the first and repeat the steps for the other fabric interconnect replacements to complete the migration.  |  **Important** |  Migrating from Cisco UCS 6200 Series Fabric Interconnects to Cisco UCS 6500 Series Fabric Interconnect is supported with Cisco UCS Manager Release 4.2(3a). For more information, see [Migration Guide for Cisco UCS Fabric Interconnects, 4.2](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html).   
---|---  
  
* * *

---

## Page 8: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Fabric-Interconnect-Migration/4-3_1/m_overview-4-1.html

# Overview of Cisco UCS Fabric Interconnects

Cisco UCS 6500 Series Fabric Interconnects

##  Cisco UCS 6536 Fabric Interconnect Overview 

The Cisco UCS 6536 Fabric Interconnect is a core part of the Cisco Unified Computing System, providing both network connectivity and management capabilities for the system. The Cisco UCS 6536 Fabric Interconnect provides the communication backbone and management connectivity for UCS B-series blade servers and UCS C-series rack servers. 

Cisco UCS 6500 Series Fabric Interconnects currently include Cisco UCS 6536 Fabric Interconnect. All servers attached to a Cisco UCS 6536 Fabric Interconnect become part of a single, highly available management domain. In addition, by supporting a unified fabric, Cisco UCS 6536 Fabric Interconnect provides both LAN and SAN connectivity for all servers within its domain. 

The Cisco UCS 6536 Fabric Interconnect supports multiple traffic classes over a lossless Ethernet fabric from the server through the fabric interconnect. 

## **Cisco UCS 6536 Fabric Interconnect**

The Cisco UCS 6536 Fabric Interconnect (UCSC-FI-6536) is a One-rack unit (1RU), top of rack (TOR), fixed-port data center platform that provides both network connectivity and management capabilities to the Cisco UCS system. 

The fabric interconnect can provide Ethernet and Fibre Channel connectivity to the servers in the system. The servers connect to the fabric interconnect, and then to the LAN or SAN. 

Cisco UCS Manager on UCS 6536 Fabric Interconnect supports Cisco UCS X-Series Compute Nodes, B-Series Blade Servers and C-Series Rack Servers, Cisco UCS S-Series Storage Servers, as well as the associated storage resources and networks. 

High availability and redundancy can be achieved by connecting a pair of fabric interconnects to each other through L1 or L2 ports in cluster mode configuration. 

Each Cisco UCS 6536 Fabric Interconnect offers the following features: 

  * Thirty-six QSFP28 ports capable of 100G including 4 unified ports (33-36). Ports also support: 

  * Autonegotiating with peer devices to speeds of 100G, 40G, 25G, 10G, and 1G.

  * Port breakout is supported for Ethernet ports (1-32) and Unified ports (33-36). 

  * Ethernet breakout is supported on switch ports 1 through 36 when each port is configured with a breakout cable. 

  * The Dynamic Ethernet Breakout feature enables converting a standard Ethernet port to a breakout port on-the-fly so that you do not need to reboot the Fabric Interconnect. Dynamic Ethernet Breakout also supports converting breakout ports back to a standard Ethernet port without a reboot. 

  * FC breakout is supported on ports 33 through 36 wherein each port is configured with a four-port breakout cable. For example 1/33/1, 1/33/2, 1/33/3, and 1/33/4 are the four FC breakout ports on the physical port 33. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Fibre Channel support is only available through the configuration of Unified Ports (33-36) as FC breakout port.

* * *  
  
---|---  
  * FC breakout ports support peer communication at fixed speeds of 8Gbs, 16 Gbps, and 32 Gbps. 

  * All four FC breakout ports must be configured with the same speed. Mixed speeds on a QSFP port's FC breakout ports are not supported. 

  * Using breakout ports enables the fabric interconnect to support the maximum 16 FC ports supported by Fibre Channel.

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

  * Converting from Ethernet to FC breakout ports, or FC breakout ports back to Ethernet, requires a reboot/reload after changing the breakout type. 
  * FCoE storage ports are not supported. 

* * *  
  
---|---  
  * One management port (one 10/100/1000BASE-T port)

  * Two L1/L2 Ethernet RJ-45 ports for high availability or cluster configurations. Ethernet ports support 10/100/1000Mb speed.

  * One console port (RS-232)

  * One USB 3.0 port

  * CPU: 4 Core, 1.8GHz, Intel 5th-Generation core processor

  * Memory: 

  * 32 GB DDR4 DIMMs

  * 128 GB M.2 SSD Flash Drive

  * 32 GB Boot Flash (16 MB primary, and 16 MB standby/golden)


This fabric interconnect includes the following user-replaceable components:

  * Fan modules (6), each is a port-side exhaust fan module with dark grey latch coloring (UCS-FAN-6536).

  * Power supply modules (2). One power supply module (PSU) is the active module for operations, and the second PSU is the standby for redundancy [1+1]) with the following choices: 

  * 1100-W AC power supply with dark grey latch coloring (UCS-PSU-6536-AC)

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

All fan modules and power supplies must use the same airflow direction.

* * *  
  
---|---  


The following figure shows the fabric interconnect features on the port side of the chassis. 

![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540351.jpg) 1  |  LEDs  |  3  |  36 40/100-Gigabit QSFP28 ports  
---|---|---|---  
2  |  Lane Select button  |  |   
  
To determine which transceivers, adapters, and cables are support the fabric interconnect, see the [Cisco Transceiver Modules Compatibility Information](http://www.cisco.com/c/en/us/support/interfaces-modules/transceiver-modules/products-device-support-tables-list.html) document. 

The following figure shows the fabric interconnect features on the power supply side of the chassis. 

![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540354.jpg) 1  |  Power supply modules (1 or 2) (AC power supplies shown) with slots numbered 1 (left) and 2 (right). |  2  |  Fan modules (6) with slots numbered from 1 (left) to 6 (right).  
---|---|---|---  
3  |  Layer 2 (L2) Ethernet port, 10/100/100Mb autonegotiating. Supports high availability (HA) or clustering through an RJ-45 port. |  4  |  Layer 1 (L1) Ethernet port, 10/100/100Mb autonegotiating.  Supports high availability (HA) or clustering through an RJ-45 port.  
5 |  Ethernet network management port (RJ45), 10/100/1000Mb autonegotiating  |  6  |  Serial Console port (RJ45), 9600 baud.  
7 |  USB 3.0/2.0 port Supports booting the system and downloading scripts. |  8 |  Beacon (BCN) LED  
9 |  Status (STS) LED |  - |   
  
The following figure shows the side of the chassis. 

![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540353.jpg) 1  |  Screw holes for mounting brackets |  2  |  Grounding pad  
---|---|---|---  
  
Plan to position the ports in a hot aisle so that fans and power supplies intake air from the cold aisle, blow the cool air through the fabric interconnect, and exhaust the heated air into the hot aisle. 

The fan and power supply modules are field replaceable. You can replace one fan module or one power supply module during operations so long as the other modules are installed and operating. If you have only one power supply installed, you can install the replacement power supply in the open slot before removing the original power supply. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

All fan and power supply modules must have the same direction of airflow. Otherwise, the fabric interconnect can overheat and shut down. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Because fans and power supply modules have port-side exhaust airflow (blue coloring for fan modules), you must locate the ports in the hot aisle. If you locate the air intake in a hot aisle, the fabric interconnect can overheat and shut down. 

* * *  
  
---|---  
  
Cisco UCS 6400 Series Fabric Interconnects

## Cisco UCS 6400 Series Fabric Interconnect Overview 

Cisco UCS 6400 Series Fabric Interconnect provides both network connectivity and management capabilities to the Cisco UCS system. The fabric interconnect provides Ethernet and Fibre Channel to the servers in the system, the servers connect to the fabric interconnect, and then to the LAN or SAN. 

Each Cisco UCS 6400 Series Fabric Interconnect runs Cisco UCS Manager to fully manage all Cisco UCS elements. The fabric interconnect supports 10/25 Gigabit ports in the fabric with 40/100 Gigabit uplink ports. High availability can be achieved when a Cisco UCS 6400 Series Fabric Interconnect is connected to another Cisco UCS 6400 Series Fabric Interconnect through the L1 or L2 port on each device. 

Cisco UCS 6400 Series Fabric Interconnect consists of: 

  * Cisco UCS 6454 Fabric Interconnects 

  * Cisco UCS 64108 Fabric Interconnects 


The Cisco UCS 6400 Series fabric interconnect supports Cisco UCS B-Series Blade Servers, UCS 5108 B-Series Server Chassis, C-Series Rack Servers, and UCS S-Series Storage Servers. 

## Cisco UCS 64108 Fabric Interconnect

The Cisco UCS 64108 Fabric Interconnect is a 2 RU top-of-rack (TOR) switch that mounts in a standard 19-inch rack such as the Cisco R Series rack. 

The high-density Cisco UCS 64108 Fabric Interconnect has 96 10/25 Gb SFP28 ports and 12 40/100 Gb QSFP28 ports. Each 40/100 Gb port can break out into 4 x 10/25 Gb uplink ports. Ports 1 - 16 are unified ports that support 10/25 GbE or 8/16/32G Fibre Channel speeds. Ports 89-96 support 1Gbps Ethernet speeds. 

The Cisco UCS 64108 Fabric Interconnect supports either: 

  * Eight FCoE port channels

  * Or Four SAN port channels

  * or Four SAN port channels and four FCoE port channels


The Cisco UCS 64108 Fabric Interconnect also has one network management port, one RS-232 serial console port for setting the initial configuration, and one USB port for saving or loading configurations. The FI also includes L1/L2 ports for connecting two fabric interconnects in a high-availability configuration. 

The Cisco UCS 64108 Fabric Interconnect also contains a CPU board that consists of: 

  * Intel Xeon Processor, 6 core

  * 64 GB of RAM 

  * 8 MB of NVRAM (4 x NVRAM chips)

  * 128 GB SSD (bootflash)


Figure 1. Cisco UCS 64108 Fabric Interconnect Rear View ![](/c/dam/en/us/td/i/300001-400000/300001-310000/307001-308000/307644.jpg) 1  |  Ports 1-16  Unified ports:

  * 10/25 Gbps Ethernet or FCoE
  * 8/16/32 Gbps Fibre Channel

|  2  |  Ports 17-88 (10/25 Gbps Ethernet or FCoE)  
---|---|---|---  
3  |  Ports 89-96

  * 10/25 Gbps Ethernet or FCoE
  * 1 Gbps Ethernet

|  4 |  Uplink Ports 97-108 (40/100 Gbps Ethernet or FCoE) Each of these ports can be 4 x 10/25 Gbps Ethernet or FCoE uplink ports when using a breakout cable.  
5 |  System environment (fan fault) LED |  6 |  System status LED  
7 |  Beacon LED |  |   
  
The Cisco UCS 64108 Fabric Interconnect has two power supplies (redundant as 1+1) and three fans (redundant as 2+1). 

Figure 2. Cisco UCS 64108 Fabric Interconnect Front View ![](/c/dam/en/us/td/i/300001-400000/300001-310000/307001-308000/307645.jpg) **1** |  Cooling fans (hot swappable, 2+1 redundancy) |  **2** |  RS-232 serial console port (RJ-45 connector)  
---|---|---|---  
**3** |  Network management port (RJ-45 connector) |  4 |  USB port  
5 |  Grounding pad for two-hole grounding lug (under protective label) |  6 |  Power supplies Two identical AC or DC PSUs, hot-swappable, 1+1 redundancy)  
7 |  L1/L2 high-availability ports (RJ-45 connector) |  8 |  Beacon LED  
9 |  System status LED |  |   
  
## Cisco UCS 6454 Fabric Interconnect

The Cisco UCS 6454 Fabric Interconnect (FI) is a 1-RU top-of-rack switch that mounts in a standard 19-inch rack such as the Cisco R Series rack. 

The Cisco UCS 6454 Fabric Interconnect has 48 10/25 Gb SFP28 ports (16 unified ports) and 6 40/100 Gb QSFP28 ports. Each 40/100 Gb port can break out into 4 x 10/25 Gb uplink ports. The sixteen unified ports support 10/25 GbE or 8/16/32G Fibre Channel speeds. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The Cisco UCS 6454 Fabric Interconnect supported 8 unified ports (ports 1 - 8) with Cisco UCS Manager 4.0(1) and 4.0(2), but with release 4.0(4) and later it supports 16 unified ports (ports 1 - 16). 

* * *  
  
---|---  
  
The Cisco UCS 6454 Fabric Interconnect supports: 

  * Maximum of 8 FCoE port channels

  * Or 4 SAN port channels

  * Or a maximum of 8 SAN port channels and FCoE port channels (4 each)


The Cisco UCS 6454 Fabric Interconnect also has one network management port, one console port for setting the initial configuration, and one USB port for saving or loading configurations. The FI also includes L1/L2 ports for connecting two fabric interconnects for high availability. 

The Cisco UCS 6454 Fabric Interconnect also contains a CPU board that consists of: 

  * Intel Xeon D-1528 v4 Processor, 1.6 GHz

  * 64 GB of RAM 

  * 8 MB of NVRAM (4 x NVRAM chips)

  * 128 GB SSD (bootflash)


Figure 3. Cisco UCS 6454 Fabric Interconnect Rear View ![](/c/dam/en/us/td/i/300001-400000/300001-310000/306001-307000/306755.jpg) 1  |  Ports 1-16 (Unified Ports 10/25 Gbps Ethernet or FCoE or 8/16/32 Gbps Fibre Channel) |  **Note** |  When using Cisco UCS Manager releases earlier than 4.0(4), only ports 1-8 are Unified Ports.  
---|---  
2  |  Ports 17-44 (10/25 Gbps Ethernet or FCoE) |  **Note** |  When using Cisco UCS Manager releases earlier than 4.0(4), ports 9-44 are 10/25 Gbps Ethernet or FCoE.  
---|---  
3  |  Ports 45-48 (1/10/25 Gbps Ethernet or FCoE)  |  4 |  Uplink Ports 49-54 (40/100 Gbps Ethernet or FCoE) Each of these ports can be 4 x 10/25 Gbps Ethernet or FCoE uplink ports when using an appropriate breakout cable.  
  
The Cisco UCS 6454 Fabric Interconnect chassis has two power supplies and four fans. Two of the fans provide front to rear airflow. 

Figure 4. Cisco UCS 6454 Fabric Interconnect Front View ![](/c/dam/en/us/td/i/300001-400000/300001-310000/306001-307000/306354.jpg) **1** |  Power supply and power cord connector  |  **2** |  Fans 1 through 4, numbered left to right, when facing the front of the chassis.  
---|---|---|---  
**3** |  L1 port, L2 port, RJ45, console, USB port, and LEDs |  |   
  
## Ports on the Cisco UCS Fabric Interconnects

Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct) has eight ports that include: 

  * Ports 1 & 2 that are unified ports to manage all SAN features and configurations.

  * The 100G Ethernet ports [1-8] can also be configured as 25Gx4 SFP28 compatible breakout ports or 4x10G ports, offering flexible networking solutions to accommodate a range of data center needs. 

  * The 32G Fibre Channel ports [1 & 2] can also be configured as 8Gx4 SFP28 compatible breakout ports offering flexible networking solutions to accommodate a range of data center needs. 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Migration of any previous generation Fabric Interconnects to the Cisco UCS 9108 100G Intelligent Fabric Module is currently not supported. 

* * *  
  
---|---  
  
Ports on the Cisco UCS 6536 Fabric Interconnects can be configured to carry either Ethernet or Fibre Channel traffic. You can configure only ports 33-36 to carry Fibre Channel traffic. The ports cannot be used by a Cisco UCS domain until you configure them. 

Ports on the Cisco UCS 6400 Series Fabric Interconnects can be configured to carry either Ethernet or Fibre Channel traffic. You can configure only ports 1-16 to carry Fibre Channel traffic. The ports cannot be used by a Cisco UCS domain until you configure them. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

  * The Cisco UCS 6454 Fabric Interconnect supported 8 unified ports (ports 1 - 8) with Cisco UCS Manager 4.0(1) and 4.0(2), but with Release 4.0(4) and later releases, it supports 16 unified ports (ports 1 - 16).  When you configure a port on a Fabric Interconnect, the administrative state is automatically set to enabled. If the port is connected to another device, this may cause traffic disruption. The port can be disabled and enabled after it has been configured. 


* * *  
  
---|---  
  
The following table summarizes the port support for third, fourth, fifth generation of Cisco UCS Fabric Interconnects, and Cisco UCS Fabric Interconnects 9108 100G.

|  Third Generation  |  Fourth Generation |  Fifth Generation |  Cisco UCS X-Series Direct  
---|---|---|---|---  
Item  |  Cisco UCS 6332  |  Cisco UCS 6332-16UP  |  Cisco UCS 6454 |  Cisco UCS 64108 |  Cisco UCS 6536 |  Cisco UCS 9108 100G FI  
Description  |  32-Port Fabric Interconnect  |  40-Port Fabric Interconnect  |  54-Port Fabric Interconnect  |  108-Port Fabric Interconnect |  36-Port Fabric Interconnect |  8 Ports  
Form factor  |  1 RU  |  1 RU  |  1 RU  |  2 RU |  1 RU |  1 RU  
Number of fixed 10 GB Interfaces  |  96 (40G to 4 x 10G breakout cables), QSA, Port 13 and 14 do not support 40G to 10G breakout  |  88 (40G to 4 x 10G breakout cables)  |  48 10G/25G interfaces |  96 10G/25G interfaces |  36 10G/25G/40G/100G interfaces |  **Note** |  144 breakout ports (36x4)  
---|---  
—   
Number of Unified Ports |  —  |  16  |  16 This FI supported 8 unified ports (ports 1 - 8) with Cisco UCS Manager 4.0(1) and 4.0(2), but with Release 4.0(4) and later it supports 16 unified ports (ports 1 - 16).  |  16 ports 1-16 |  4 |  **Note** |  16 breakout ports (4x4)  
---|---  
Ports 1-2  
Unified Port Speeds in Gbps |  —  |  1G/10G or 4G/8G/16G-FC  |  10G/25G or 8G/16G/32G-FC  |  10G/25G or 8G/16G/32G-FC |  10G/25G/40G/100G FC |  8G/16G/32G FC  
Number of 40-Gbps ports  |  32  |  24  |  6 40G/100G  |  12 40G/100G  |  36 |  —   
Unified Port Range  |  None  |  Ports 1-16  |  Ports 1-16  |  Ports 1-16  |  Ports 33-36 |  Ports 1-2  
Compatibility with the IOM  |  UCS 2204, UCS 2208, UCS 2304, UCS 2304V2 |  UCS 2204, UCS 2208, UCS 2304, UCS 2304V2 |  UCS 2204, UCS 2208, UCS 2408 |  UCS 2204, UCS 2208, UCS 2408 |  UCS 2408, UCS 2304, UCS 2304V2 |  —   
Compatibility with the FEX |  Cisco Nexus 2232PP Cisco Nexus 2232TM-E Cisco Nexus 2348UPQ |  Cisco Nexus 2232PP Cisco Nexus 2232TM-E Cisco Nexus 2348UPQ |  Cisco Nexus 2232PP Cisco Nexus 2232TM-E Cisco Nexus 93180YC-FX3 |  Cisco Nexus 2232PP Cisco Nexus 2232TM-E Cisco Nexus 93180YC-FX3 |  Cisco Nexus 93180YC-FX3 N2K-C2348UPQ |  —   
Expansion Slots  |  None  |  None  |  None  |  None |  None |  —   
Fan Modules  |  4  |  4  |  4 |  3 |  6 |  3  
Power Supplies  |  2 (AC/DC)  |  2 (AC/DC)  |  2 (AC/DC)  |  2 (AC/DC)  |  2 (AC) |  Supplied by chassis

---
