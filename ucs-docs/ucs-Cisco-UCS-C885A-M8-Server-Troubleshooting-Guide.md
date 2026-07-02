# Cisco UCS C885A M8 Server Troubleshooting Guide

| | |
|---|---|
| **URL Title** | Cisco UCS C885A M8 Server Troubleshooting Guide |
| **URL** | https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/c/hw/c885A/install/b_c885a-m8-server-troubleshooting-guide.html |
| **Long URL** |  |
| **HTML Title** | Cisco UCS C885A M8 Server Troubleshooting Guide |
| **Source file** | `ucs-docs-raw/html/b_c885a-m8-server-troubleshooting-guide.html` |
| **File type** | HTML |
| **Fetched on** | 2026-07-02 13:08:28 |

---

## Page 1: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/c/hw/c885A/install/b_c885a-m8-server-troubleshooting-guide.html

![Clear Contents of Search](/etc/designs/cdc/fw/i/ic_clear_gray.png)

---

## Page 2: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/c/hw/c885A/install/b_c885a-m8-server-troubleshooting-guide/m-preface.html

# Preface

This preface contains the following topics:

## Bias-Free Documentation

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The documentation set for this product strives to use bias-free language. For purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on standards documentation, or language that is used by a referenced third-party product. 

* * *  
  
---|---  
  
## Full Cisco Trademarks with Hardware License

THE SPECIFICATIONS AND INFORMATION REGARDING THE PRODUCTS IN THIS MANUAL ARE SUBJECT TO CHANGE WITHOUT NOTICE. ALL STATEMENTS, INFORMATION, AND RECOMMENDATIONS IN THIS MANUAL ARE BELIEVED TO BE ACCURATE BUT ARE PRESENTED WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. USERS MUST TAKE FULL RESPONSIBILITY FOR THEIR APPLICATION OF ANY PRODUCTS. 

THE SOFTWARE LICENSE AND LIMITED WARRANTY FOR THE ACCOMPANYING PRODUCT ARE SET FORTH IN THE INFORMATION PACKET THAT SHIPPED WITH THE PRODUCT AND ARE INCORPORATED HEREIN BY THIS REFERENCE. IF YOU ARE UNABLE TO LOCATE THE SOFTWARE LICENSE OR LIMITED WARRANTY, CONTACT YOUR CISCO REPRESENTATIVE FOR A COPY. 

The following information is for FCC compliance of Class A devices: This equipment has been tested and found to comply with the limits for a Class A digital device, pursuant to part 15 of the FCC rules. These limits are designed to provide reasonable protection against harmful interference when the equipment is operated in a commercial environment. This equipment generates, uses, and can radiate radio-frequency energy and, if not installed and used in accordance with the instruction manual, may cause harmful interference to radio communications. Operation of this equipment in a residential area is likely to cause harmful interference, in which case users will be required to correct the interference at their own expense. 

The following information is for FCC compliance of Class B devices: This equipment has been tested and found to comply with the limits for a Class B digital device, pursuant to part 15 of the FCC rules. These limits are designed to provide reasonable protection against harmful interference in a residential installation. This equipment generates, uses and can radiate radio frequency energy and, if not installed and used in accordance with the instructions, may cause harmful interference to radio communications. However, there is no guarantee that interference will not occur in a particular installation. If the equipment causes interference to radio or television reception, which can be determined by turning the equipment off and on, users are encouraged to try to correct the interference by using one or more of the following measures: 

  * Reorient or relocate the receiving antenna. 

  * Increase the separation between the equipment and receiver. 

  * Connect the equipment into an outlet on a circuit different from that to which the receiver is connected. 

  * Consult the dealer or an experienced radio/TV technician for help. 


Modifications to this product not authorized by Cisco could void the FCC approval and negate your authority to operate the product. 

The Cisco implementation of TCP header compression is an adaptation of a program developed by the University of California, Berkeley (UCB) as part of UCB’s public domain version of the UNIX operating system. All rights reserved. Copyright © 1981, Regents of the University of California. 

NOTWITHSTANDING ANY OTHER WARRANTY HEREIN, ALL DOCUMENT FILES AND SOFTWARE OF THESE SUPPLIERS ARE PROVIDED "AS IS" WITH ALL FAULTS. CISCO AND THE ABOVE-NAMED SUPPLIERS DISCLAIM ALL WARRANTIES, EXPRESSED OR IMPLIED, INCLUDING, WITHOUT LIMITATION, THOSE OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT OR ARISING FROM A COURSE OF DEALING, USAGE, OR TRADE PRACTICE. 

IN NO EVENT SHALL CISCO OR ITS SUPPLIERS BE LIABLE FOR ANY INDIRECT, SPECIAL, CONSEQUENTIAL, OR INCIDENTAL DAMAGES, INCLUDING, WITHOUT LIMITATION, LOST PROFITS OR LOSS OR DAMAGE TO DATA ARISING OUT OF THE USE OR INABILITY TO USE THIS MANUAL, EVEN IF CISCO OR ITS SUPPLIERS HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. 

Any Internet Protocol (IP) addresses and phone numbers used in this document are not intended to be actual addresses and phone numbers. Any examples, command display output, network topology diagrams, and other figures included in the document are shown for illustrative purposes only. Any use of actual IP addresses or phone numbers in illustrative content is unintentional and coincidental. 

All printed copies and duplicate soft copies of this document are considered uncontrolled. See the current online version for the latest version. 

Cisco has more than 200 offices worldwide. Addresses and phone numbers are listed on the Cisco website at www.cisco.com/go/offices.

Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries. To view a list of Cisco trademarks, go to this URL: <https://www.cisco.com/c/en/us/about/legal/trademarks.html>. Third-party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (1721R) 

## Communications, Services, and Additional Information

  * To receive timely, relevant information from Cisco, sign up at [Cisco Profile Manager](https://www.cisco.com/offer/subscribe). 

  * To get the business impact you’re looking for with the technologies that matter, visit [Cisco Services](https://www.cisco.com/go/services). 

  * To submit a service request, visit [Cisco Support](https://www.cisco.com/c/en/us/support/index.html). 

  * To discover and browse secure, validated enterprise-class apps, products, solutions and services, visit [Cisco Marketplace](https://developer.cisco.com/site/marketplace/). 

  * To obtain general networking, training, and certification titles, visit [Cisco Press](http://www.ciscopress.com). 

  * To find warranty information for a specific product or product family, access [Cisco Warranty Finder](http://www.cisco-warrantyfinder.com). 


### Cisco Bug Search Tool

[Cisco Bug Search Tool](https://www.cisco.com/c/en/us/support/web/tools/bst/bsthelp/index.html) (BST) is a web-based tool that acts as a gateway to the Cisco bug tracking system that maintains a comprehensive list of defects and vulnerabilities in Cisco products and software. BST provides you with detailed defect information about your products and software. 

---

## Page 3: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/c/hw/c885A/install/b_c885a-m8-server-troubleshooting-guide/m-Chapter-1.html

# Introduction

This introduction contains the following topics:

## Introduction

**Component** |  **Description**  
---|---  
GPU |  Support HGX 8-GPU SXM5 with GPU BB Sled AMD: MI300X 750W CPU-GPU Interconnect: 8xPCIe Gen5x16 (Refer to the PCIe topology in Figure 4 and 5)  
CPU |  2 x AMD SP5 sockets, LGA6096 Compatible with AMD EPYC™ 9004 and 9005 Series CPU  
Storage (OS) |  1 x PCIe Gen3 NVMe M.2 (on board/HPM) + Dual M.2 PCIe Gne4 NVME SSD  
Storage (Data Cache) | Up to 16x 2.5” NVMe U.2 (PCIe SW) + 8X2.5” SAS/SATA (optional by SAS RAID card)   
Network (Cluster) card |  8 x Gen 5 x16 HHHL Slots compatible with InfiniBand and Ethernet  InfiniBand (default): Up to 400Gbps Ethernet: 400GbE, 200GbE, 100GbE, 50GbE, 40GbE, 25GbE, and 10GbE   
Network (North-South) card |  5 x Gen5 x16 FHHL Slots compatible with Infini Band and Ethernet  Ethernet (default): 400GbE, 200GbE, 100GbE, 50GbE, 40GbE, 25GbE, and 10GbE  InfiniBand: Up to 400Gbps  
System Memory (DIMM) | 24 x DDR5 DIMM Slots, up to 4800 / 6400 MHz, depends on CPU Model, Total capacity up to 6TB   
DC-SCM (out-of-band system management) |  1 GbE RJ45 interface Supports IPMI 2.0, KVM, and Watchdog  
OCP NIC 3.0 | 1 x OCP 3.0 SFF Slot, supporting Ethernet from 1G to 10G  
Power Supply | 6 x 3 kW + 2 x 2.4 kW  
Figure 1. System Exploded Drawing  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525343.jpg) 1 |  Front Bezel  
---|---  
2 |  Fan 12x Storage 16+8  
3 |  19``@800mm Main Chassis  
4 |  PSU  
5 |  CPU Sled  
6 |  HGBB Sled  
Figure 2. System Front View  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525344.jpg) 1 |  80105 Fan X 12  
---|---  
2 |  Power Button with LED  
3 |  UID Button with LED  
4 |  USB2.0 X 2  
5 |  NVMe SSD X 8  
6 |  SAS / SATA SSD X 8  
7 |  NVMe SSD X 8  
Figure 3. System Rear View  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525345.jpg) 1 |  FHHL PCIe X 2 (Max.)  
---|---  
2 |  LP PCIe X 8 (Max.)  
3 |  FHHL PCIe X 3 (Max.)  
4 |  2400W PSU  
5 |  OCP Module  
6 |  3000W*6 PSU  
7 |  DC-SCM  
Figure 4. Block diagram (8U GPU Server with NV H100 and H200)  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525346.jpg) Figure 5. Block diagram (8U GPU Server w/ AMD MI300)  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525347.jpg)

  * Terminology


### Terminology

Term | Definition  
---|---  
CPU | Central Processing Unit. Common reference to both CISC (complex instruction set computer) and RISC (reduced instruction set computer) processors   
FHHL | PCIe card form factor, Full Height Half Length  
GPU | Graphics Processing Unit  
NIC | Network Interface Card  
NVMe | Non-Volatile Memory Express  
OCP | Open Compute Project  
PCIe | Peripheral Component Interconnect Express. Refers to a communication like defined within PCISIG standards body.   
BMC | Baseboard Management Controller  
FRU | Field Replace Unit  
DCSCM | Datacenter Secure control Module Specification  
IPMI | Intelligent Platform Management Interface

---

## Page 4: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/c/hw/c885A/install/b_c885a-m8-server-troubleshooting-guide/m-Chapter-2-Diagnostic-Indicator.html

# Diagnostic Indicator  
  
This diagnostic indicator contains the following topics:

## Power Supply and DC-SCM Module

Figure 1. 2400W *2 CRPS Power Supply  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525348.jpg) 1 |  2400W CRPS Power Supply LED  
---|---  
2 |  2400W CRPS Power Supply LED  
Indicator code | Condition  
---|---  
*Off | Failure – PSU is not detected or installed / PSU fail  
Green | Active  
*Amber | Failure – AC cord unplugged / No AC Power input  
Figure 2. DC-SCM  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525349.jpg) 1 |  Power and Fault Indicator  
---|---  
2 |  ID Indicator  
3 |  RJ-45 with LED  
Indicator code | Condition  
---|---  
Power and Fault Indicator  
Off | Power Off  
Green Fast Blink | Pre-S5  
Green Slow Blink | S5  
Green Solid On | S0  
Amber Solid On | Warning  
ID Indicator  
Off | UID is off  
Blue Solid On | UID is on  
RJ-45 with LED  
Left and Right - off | No connection  
Left – Amber Blinking | Link and Active on network  
Right – Amber | Link and run in 100Mbps  
Right – Green | Link and run in 1Gbps  
Figure 3. 3000W Power Supply LED  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525350.jpg) 1 |  3000W Power Supply In LED  
---|---  
2 |  3000W Power Supply Out LED  
Indicator code  | Condition   
---|---  
LED Off  | Failure – PSU is not detected or installed / PSU fail   
In LED – Green Solid  | AC Input Active   
Out LED – Amber Blinking  | Output power Standby   
Out LED – Amber Solid  | AC Output Active   
  
## System Fan LED 

Figure 4. System Fan LED  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525351.jpg) 1 |  System Fan LED  
---|---  
Indicator code | Condition  
---|---  
Off | Fan active  
Amber solid | Fan fail  
  
## SSD/NVMe Drivers

Figure 5. SSD/NVMe Drivers  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525352.jpg) 1 |  Activity LED  
---|---  
2 |  Status LED  
**Indicator** |  **Color** |  **Blinking Pattern** |  **Behavior for Device**  
---|---|---|---  
Activity LED | OFF | OFF | Drive Not Present  
Green | Solid ON | Drive Present, But no activity  
Green | Blinking 4Hz | Drive Present, I/O Activity  
Status LED | Amber | Blinking 4Hz | Locate (Identify)  
RED | Solid ON | Fail  
RED | Blinking 1Hz | Rebuild  
  
## Front panel LED Indicators

Figure 6. Front panel LED Indicators  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525353.jpg) 1 |  Power Button with LED  
---|---  
2 |  UID Button with LED  
3 |  USB2.0 X 2  
Table 1. UID Button with LED Indicator code | Condition  
---|---  
Off | UID is off  
Blue | UID is on  
Table 2. Power Button with LED Indicator code | Condition  
---|---  
Off | Power off  
Green slow blink | Before BMC initial done(S5)  
Green fast blink | After BMC initial done to power button(S5)  
Green solid | After power button triggered(S0)  
Amber slow blink | Temperature abnormal, fan quantity abnormal, fan speed abnormal  
  
*If any of the warning condition occurs, you will need to re-plug or change the device.

---

## Page 5: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/c/hw/c885A/install/b_c885a-m8-server-troubleshooting-guide/m-Chapter-3-Running-diagnostic.html

# Running Diagnostic

This running diagnostic contains the following topics:

## Running diagnostic

The Self-Diagnostic Test is used to perform function coverage testing. Running on Linux, it is a UI framework to merge/involve different test diagnostic programs including Open-Source tools (included BSD/GPL v2.0 license), Vendor Tools/Drivers, and some diagnostic tools from ODM. 

The user can utilize selftest.py to merge various diagnostic utilities, packages, and scripts for conducting function testing. ODM can set up and build a package that includes selftest.py and diagnostic utilities for customers to perform interaction testing. 

  * Environment requirement
  * User interface


### Environment requirement

No. | Item | Version  
---|---|---  
1 | Ubuntu® | 22.04.2  
2 | Python | 3.10.12  
3 | smartctl | 7.2  
4 | xterm | 372  
  
#### How to execute test program in Linux console

Execute the following Self-Diagnostic test commands:

  * sudo chmod -R +x *

  * sudo ./selftest


### User interface

#### Main window

![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525354.jpg)

#### System Summary

It displays system, memory, CPU, Hard Disk information. 

![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525355.jpg)

#### Test

Switch to the Test path, press Start button to start the testing. 

![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525354.jpg) ![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

You will need to perform all the test items defined in the sequence.xml. 

* * *  
  
---|---  
  
#### Test Status

Switch to the Status path. 

You can check the test status and press Cancel button to stop the test during testing. 

Figure 1. Test Status  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525356.jpg)

#### Test Log

Switch to the Log path to review the test log directly and find the complete Logs from the selftest tool path. 

![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525357.jpg)

#### Log - Process Log 

![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525358.jpg)

#### Log - Error Log

![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525359.jpg)

---

## Page 6: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/c/hw/c885A/install/b_c885a-m8-server-troubleshooting-guide/m-Chapter-4-Troubleshooting-hardware-issues.html

# Troubleshooting hardware issues

This troubleshooting hardware issues contains the following topics:

## Mother board

  * G3 to S5
  * FPGA postcode error code check
  * S5 to S0(POST)


### G3 to S5

After providing AC power, you can refer to postcode debug LED (**Figure 13**) on dual M.2 riser card and check if the LED has been lighting on or not. 

If yes, you can refer to the FPGA power-on error code (check LED bit 2 and 1) and check the corresponding post code number. 

Figure 1. Postcode debug LED on dual M.2 riser card  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525360.jpg) ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525361.jpg) ![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Postcode debug LED bit (4,3,2,1)

  * Solid on – Display BIOS 80, 81 port data at LED bit (4,3,2,1). (Refer to **BIOS Related Issue** > **POST Issue**) 
  * Flashing – Display PFR post code data at LED bit (4,3) with 2 dots on
  * – Display FPGA power seq and error codes or Board ID at LED bit (2,1). (Refer to **Table 3: FPGA power-on error code (check LED bit 2 & 1)**) 


* * *  
  
---|---  
  
### FPGA postcode error code check

When system post hang occurs, please note the number on postcode debug LED and refer to the **Table 3: FPGA power-on error code (check LED bit 2 and 1) - Power-Up error condition** , **Table 4: FPGA power-down error code (check LED bit 2 and 1)** , and **Table 5: Thermal error postcode (check LED bit 2 and 1)** , and below to check the root cause. 

Table 1. FPGA power-on error code (check LED bit 2 and 1) - Power-Up error condition Postcode | Item  
---|---  
10 | LTPI PHY aligned  
11 | FM_HPM_STBY_EN (LTPI Link-Up)  
12 | BMC Ready  
13 | CPU0 Not Present  
14 | PWRGD_CPU_PVDD3V3_STBY  
15 | PWRGD_CPU0_PVDD1V8_STBY  
16 | PWRGD_CPU1_PVDD1V8_STBY  
17 | FM_HPM_STBY_RST  
18 | PWRGD_PSU1_PWROK  
19 | PWRGD_PSU2_PWROK  
22 | PWRGD_GPU_P54V (provide by HIB)  
21 | PWRGD_P3V3  
31 | PWRGD_PVDD1V1_P0  
32 | PWRGD_PVDDIO_P0  
33 | PWRGD_PVDDCR_SOC_P0  
34 | PWRGD_PVDDCR_CPU0_P0  
35 | PWRGD_PVDDCR_CPU1_P0  
41 | PWRGD_PVDD1V1_P1  
42 | PWRGD_PVDDIO_P1  
43 | PWRGD_PVDDCR_SOC_P1  
44 | PWRGD_PVDDCR_CPU0_P1  
45 | PWRGD_PVDDCR_CPU1_P1  
46 | SYS_POWER_ON_READY  
Table 2. FPGA power-down error code (check LED bit 2 and 1) Postcode | Item  
---|---  
51 | FM_HPM_STBY_EN  
52 | BMC Ready  
53 | CPU0 Not Present  
54 | PWRGD_CPU_PVDD3V3_STBY  
55 | PWRGD_CPU0_PVDD1V8_STBY  
56 | PWRGD_CPU1_PVDD1V8_STBY  
57 | FM_HPM_STBY_RST  
62 | PWRGD_GPU_P54V (provide by HIB)  
61 | PWRGD_P3V3  
71 | PWRGD_PVDD1V1_P0  
72 | PWRGD_PVDDIO_P0  
73 | PWRGD_PVDDCR_SOC_P0  
74 | PWRGD_PVDDCR_CPU0_P0  
75 | PWRGD_PVDDCR_CPU1_P0  
81 | PWRGD_PVDD1V1_P1  
82 | PWRGD_PVDDIO_P1  
83 | PWRGD_PVDDCR_SOC_P1  
84 | PWRGD_PVDDCR_CPU0_P1  
85 | PWRGD_PVDDCR_CPU1_P1  
86 | SYS_POWER_ON_READY  
Table 3. Thermal error postcode (check LED bit 2 and 1) Postcode | Item  
---|---  
91 | FM_CPU0_THERMTRIP_N  
92 | FM_CPU1_THERMTRIP_N  
9F | Universal thermal Error  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

  1. Please check if all the fans work normally.
  2. If any of the fans stop working or work strange, please re-plugin again.
  3. If re-plug of the fan does not work, please change the fan directly.


* * *  
  
---|---  
  
### S5 to S0(POST)

Please refer to the **Chapter 7: BIOS Related Issue** and check 80/81 postcode LED notes. 

Check 80/81 port LED

(BIOS provide decode)

## System Failure

Troubleshooting under OS issue

  * Loss PCIE Device check
  * SAS/SATA Issue


### Loss PCIE Device check

#### Prerequisite

PCIE Device not detect under OS.

#### Troubleshooting step:

  1. Execute the command in OS to check the device lost and its corresponding slot location:

  * Check PCIe Tree and device address: lspci -tv | less

  * Check which slot ID cannot recognize: _lspci -v | grep -i “slot:”|sort “_

  2. Apply the system PCIE Topology Mapping table to check the path of lost device after you get the lost slot location.


#### PCIE Topology Mapping Table

**PCIE Root Port** |  **Source** |  **Cable ID** |  **Switch** |  **Cable** |  **Board** |  **Connector** |  **END Device Category** |  **Device Name** |  **System** **Slot Name**  
---|---|---|---|---|---|---|---|---|---  
**[0000:40] [0000:60]** |  **MB** |  **#A #B** |  **SW1 HIB Board** |  **#J** |  **CEMBB** |  |  **PCIE Slot (x16)** |  **LP2** |  **202**  
**#I** |  **PCIE Slot (x16)** |  **LP1** |  **201**  
|  **MIDPLANE** |  **CNHIB1** |  **NVME SSD (x4)** |  **SSD1** |  **301**  
**NVME SSD (x4)** |  **SSD2** |  **302**  
**NVME SSD (x4)** |  **SSD3** |  **303**  
**NVME SSD (x4)** |  **SSD4** |  **304**  
**MEDPLANE to HGBB** |  **CNHIB3,** **CNHIB4, CNUBBJ9,** **CNUBBJ10** |  **GPU (OAM)** |  **GPU2** |  **102**  
**GPU (OAM)** |  **GPU3** |  **103**  
**#Q** |  **CEM_L** |  |  **PCIE Slot (x16)** |  **FHHL11** |  **211**  
**PCIE Root Port** |  **Source** |  **Cable ID** |  **Switch** |  **Cable** |  **Board** |  **Connector** |  **END Device Category** |  **Device Name** |  **System Slot Name**  
---|---|---|---|---|---|---|---|---|---  
**[0000:00] [0000:20]** |  **MB** |  **#C #D** |  **SW2 HIB Board** |  **#L** |  **CEMBB** |  **** |  **PCIE Slot (x16)** |  **LP4** |  **204**  
**#K** |  **PCIE Slot (x16)** |  **LP3** |  **203**  
**** |  **MIDPLANE** |  **CNHIB5** |  **NVME SSD (x4)** |  **SSD5** |  **305**  
**NVME SSD (x4)** |  **SSD6** |  **306**  
**NVME SSD (x4)** |  **SSD7** |  **307**  
**NVME SSD (x4)** |  **SSD8** |  **308**  
**MEDPLANE to HGBB** |  **CNHIB6,** **CNHIB7, CNUBBJ7,** **CNUBBJ8** |  **GPU (OAM)** |  **GPU0** |  **100**  
**GPU (OAM)** |  **GPU1** |  **101**  
**#R #U** |  **CEM_L** |  **** |  **PCIE Slot (x16)** |  **FHHL13** |  **213**  
**#Y #U** |  **CEM_L** |  **PCIE Slot (x16)** |  **FHHL15** |  **215**  
**** |  **Riser-M.2 (x4)** |  **M.2** |  ****  
**PCIE Root Port** |  **Source** |  **Cable ID** |  **Switch** |  **Cable** |  **Board** |  **Connector** |  **END Device Category** |  **Device Name** |  **System Slot Name**  
---|---|---|---|---|---|---|---|---|---  
**[0000:c0] [0000:e0]** |  **MB** |  **#E #F** |  **SW3 HIB Board** |  **#N** |  **CEMBB** |  **** |  **PCIE Slot (x16)** |  **LP6** |  **206**  
**#M** |  **PCIE Slot (x16)** |  **LP5** |  **205**  
**** |  **MIDPLANE** |  **CNHIB10** |  **NVME SSD (x4)** |  **SSD9** |  **309**  
**NVME SSD (x4)** |  **SSD10** |  **310**  
**NVME SSD (x4)** |  **SSD11** |  **311**  
**NVME SSD (x4)** |  **SSD12** |  **312**  
**MEDPLANE to HGBB** |  **CNHIB8** **CNHIB9 CNUBBJ5** **CNUBBJ6** |  **GPU (OAM)** |  **GPU7** |  **107**  
**GPU (OAM)** |  **GPU6** |  **106**  
**#S #X** |  **CEM_R** |  **** |  **PCIE Slot (x16)** |  **FHHL12** |  **212**  
**#Z** |  **** |  **M.2 Adapt Card** |  **** |  **Riser-M.2 (x4)** |  **M.2** |  ****  
**** |  **Riser-M.2 (x4)** |  **M.2** |  ****  
**OCP Card** |  **** |  **OCP** |  **OCP1** |  ****  
**PCIE Root Port** |  **Source** |  **Cable ID** |  **Switch** |  **Cable** |  **Board** |  **Connector** |  **END Device Category** |  **Device Name** |  **System Slot Name**  
---|---|---|---|---|---|---|---|---|---  
**[0000:80] [0000:a0]** |  **MB** |  **#G #H** |  **SW4 HIB Board** |  **#P** |  **CEMBB** |  **** |  **PCIE Slot (x16)** |  **LP8** |  **208**  
**#O** |  **PCIE Slot (x16)** |  **LP7** |  **207**  
**** |  **MIDPLANE** |  **CNHIB11** |  **NVME SSD (x4)** |  **SSD13** |  **313**  
**NVME SSD (x4)** |  **SSD14** |  **314**  
**CNHIB14** |  **NVME SSD (x4)** |  **SSD15** |  **315**  
**NVME SSD (x4)** |  **SSD16** |  **316**  
**MEDPLANE to HGBB** |  **CNHIB12,** **CNHIB13, CNUBBJ3** **CNUBBJ4** |  **GPU (OAM)** |  **GPU4** |  **104**  
**GPU (OAM)** |  **GPU5** |  **105**  
**#T #X** |  **CEM_R** |  **** |  **PCIE Slot (x16)** |  **FHHL14** |  **214**  
  
![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525370.jpg)

### SAS/SATA Issue

#### Cannot detect single SAS or SATA device

  1. Re-plug the SAS or SATA card.

  2. If you still cannot read the device, change the new SAS or SATA card.

  3. If you still cannot read the device, change to a new Midplane.


#### Cannot detect all SAS or SATA device

  1. Check the Raid Card in the Bios setup menu. 

![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525381.jpg)

You will be able to view the "Healthy" screen under normal circumstances.

  2. If the Raid card displays Fail or card not showing, re-plug the Raid card or change to a new one.

  3. If the issue still exists, replace to a new CEM_L(R) Card.

  4. If the SSD Driver displays Fail or not showing, re-plug the SAS IO cable and make sure that there are no bent pins.

  5. If you still cannot detect the device, re-plug the SAS IO card.

  6. If the issue occurs again, change the SAS IO cable and SAS IO card.


#### NVMe/SAS/SATA device abnormal or show Fail LED

  1. Check the drive LED, the active LED lights up Green when the drive is present.

**Drive Carrier LED Indicators**  
---  
**Indicator** |  **Color** |  **Blinking Pattern** |  **Behavior for Device**  
Activity LED | OFF | OFF | Drive Not Present  
Green | Solid ON | Drive Present, But no activity  
Green | Blinking 4Hz | Drive Present, I/O Activity  
Locate LED | Amber | Blinking 4Hz | Locate (Identify)  
Fail LED | RED | Solid ON | Fail  
RED | Blinking 1Hz | Rebuild  
  2. If the fail LED lights up Red, enter the BIOS Menu to check if the device is healthy or not.

  3. Enter the RAID card settings in the BIOS and check whether the status of all the devices are normal and confirm the number. If there is an abnormality in the hard disk, please open a case with TAC. 


---

## Page 7: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/c/hw/c885A/install/b_c885a-m8-server-troubleshooting-guide/m-Chapter-6-Troubleshooting-operating-system-issues.html

# Troubleshooting Operating System Issues

This Troubleshooting operating system issues contains the following topics:

## Troubleshooting operating system issues 

This section helps you troubleshoot operating system issues in your system. 

**NOTE:** If the problem persists, contact Wistron Technical Support for further assistance. 

Topics:

  * How to install the operation system via Virtual media – Ubuntu 22.04 

  * AMD GPU

  * How to add amdgpu driver to blacklist in Linux

  * How to Install and Reinstall AMD MI300X ROCm and Driver in Ubuntu 

  * AMDGPU driver cause fatal error with AMD platform

  * How to uninstall ROCm

  * Why do AMD Applications hang on Multi-GPU systems

  * How to update AMD MI300X UBB Firmware via BMC Console


  * How to install the operation system using Virtual media - Ubuntu 22.04
  * AMD GPU


### How to install the operation system using Virtual media - Ubuntu 22.04 

**Before you begin**

  1. Ensure that the server supports the operating system you intend to install.

  2. Make sure you have the OS source media available for the server.

  3. Prepare a storage location where you can store the necessary installation files.


### SUMMARY STEPS

  1. Access the OpenBMC Web UI interface by entering the server's IP address in a web browser. 
  2. Mount OS Source media into the Virtual Media drive.
  3. Click **Add file** (such as an ISO file) to add the virtual media device. 
  4. Click **Start** to start the virtual media after the file is added. 
  5. After mount iso image success.
  6. Save the changes, reboot the server, and boot into the OS installation image.
  7. In the BIOS setup utility or boot menu, navigate to the Save & Exit section or a similar option. 
  8. Select the UEFI: Linux File-CD Gadget 0515 or similar entry from the available boot devices. 
  9. Save the changes and exit the BIOS setup utility or boot menu.
  10. The server will now boot from the selected boot device, which is the OS installation image on the virtual media drive.
  11. Once the installation completes, the server reboots again, this time booting from the installed operating system on the server's local disk. 


### DETAILED STEPS

| Command or Action | Purpose  
---|---|---  
**Step 1** |  Access the OpenBMC Web UI interface by entering the server's IP address in a web browser.  |  |  **Note** |  The default username is **root** and password is **0penBmc**.   
---|---  
Figure 1. Login BMC WebGUI  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525943.jpg)  
**Step 2** |  Mount OS Source media into the Virtual Media drive. |   
**Step 3** |  Click **Add file** (such as an ISO file) to add the virtual media device.  |  Figure 2. Add media file  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525945.jpg)  
**Step 4** |  Click **Start** to start the virtual media after the file is added.  |  Figure 3. Start the ISO image  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525947.jpg)  
**Step 5** |  After mount iso image success. |  Figure 4. Mounted the ISO  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525479.jpg)  
**Step 6** |  Save the changes, reboot the server, and boot into the OS installation image. |   
**Step 7** |  In the BIOS setup utility or boot menu, navigate to the Save & Exit section or a similar option.  |   
**Step 8** |  Select the UEFI: Linux File-CD Gadget 0515 or similar entry from the available boot devices.  |   
**Step 9** |  Save the changes and exit the BIOS setup utility or boot menu. |   
**Step 10** |  The server will now boot from the selected boot device, which is the OS installation image on the virtual media drive. |  Figure 5. Boot the Virtual Media from BIOS  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525480.jpg)  
**Step 11** |  Once the installation completes, the server reboots again, this time booting from the installed operating system on the server's local disk.  |   
  
### AMD GPU

  * How to add amdgpu driver to blacklist in Linux
  * How to Install AMD MI300X ROCm and Driver in Ubuntu
  * AMDGPU driver cause fatal error with AMD platform
  * Why does the AMD application become unresponsive on multi-GPU systems


#### How to add amdgpu driver to blacklist in Linux

**Cause:** If the amdgpu driver or firmware have some issues, it can result in the system shutting down or rebooting when the user loads the amdgpu driver. Therefore, it is necessary for the user to blacklist the amdgpu driver to prevent it from being automatically loaded. If the user forgets to set up the blacklist, the issue may persist. 

**Solution:**

To add the parameter behind GRUB_CMDLINE_LINUX in /etc/default/grub, perform the following: 

### SUMMARY STEPS

  1. Run the following command to open the GRUB configuration file in a text editor: `$ sudo nano /etc/default/grub`
  2. Locate the line that starts with GRUB_CMDLINE_LINUX in the file. 
  3. Save the changes by pressing `Ctrl + X`, followed by `Y`, and then `Enter`. 
  4. Update the GRUB configuration by running the following command:
  5. Reboot your system for the changes to take effect: 
  6. When the amdgpu is added to blacklist, you should manually load the module using the following command:


### DETAILED STEPS

| Command or Action | Purpose  
---|---|---  
**Step 1** |  Run the following command to open the GRUB configuration file in a text editor: `$ sudo nano /etc/default/grub` |   
**Step 2** |  Locate the line that starts with GRUB_CMDLINE_LINUX in the file.  |  For example, if you need to add the parameter " modprobe.blacklist=amdgpu iommu=pt pci=noats ", the line would look like:
    
    
    GRUB_CMDLINE_LINUX=”modprobe.blacklist=amdgpu iommu=pt
    pci=noats”  
  
**Step 3** |  Save the changes by pressing `Ctrl + X`, followed by `Y`, and then `Enter`.  |   
**Step 4** |  Update the GRUB configuration by running the following command: | 
    
    
    $sudo grub-mkconfig -o
    /boot/efi/EFI/ubuntu/grub.cfg$sudo update-grub  
  
**Step 5** |  Reboot your system for the changes to take effect:  | 
    
    
    $sudo
    reboot  
  
**Step 6** |  When the amdgpu is added to blacklist, you should manually load the module using the following command: |  `$modprobe amdgpu`  
  
##### What to do next

**NOTE** : After rebooting, the amdgpu driver will be loaded with the specified parameters or options. Be aware that manually loading the driver may introduce potential issues or conflicts. If you experience any problems, consider reviewing the parameters or options added in Step 2 or consult AMD technical support for further assistance. 

#### How to Install AMD MI300X ROCm and Driver in Ubuntu

**Installation prerequisites**

Before installing ROCm, complete the following prerequisites. 

### SUMMARY STEPS

  1. Confirm the system has a supported Linux version. 
  2. Verify the kernel version.


### DETAILED STEPS

| Command or Action | Purpose  
---|---|---  
**Step 1** |  Confirm the system has a supported Linux version.  | 

  * To obtain the Linux distribution information, use the following command: `$ uname -m && cat /etc/*release`
  * Confirm that your Linux distribution matches a [ _supported distribution_ ](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html#supported-distributions).  **Example:** Running the preceding command on an Ubuntu system produces the following output: 
        
        x86_64
        DISTRIB_ID=Ubuntu
        DISTRIB_RELEASE=20.04
        DISTRIB_CODENAME=focal
        DISTRIB_DESCRIPTION="Ubuntu 20.04.5 LTS"


  
**Step 2** |  Verify the kernel version. |   
  
##### What to do next

  * To check the kernel version of your Linux system, type the following command:

`$uname -srmv`

Example: The preceding command lists the kernel version in the following format:
        
        Linux 5.15.0-46-generic #44~20.04.5-Ubuntu SMP Fri Jun 24
        13:27:29 UTC 2022 x86_64

  * Confirm that your kernel version matches the system requirements, as listed in [Supported operating systems](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html#supported-distributions). 

  * **Install ROCm Method:**

For a quick summary on installing ROCm on Linux, choose your preferred operating system and installation method and follow the steps listed in the table. If you want more in-depth installation instructions, refer to [ROCm installation options](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/tutorial/install-overview.html#rocm-install-overview). 


**Method 1:**

  * **Ubuntu 22.04**

**Native package manager**
        
        sudo apt install "linux-headers-$(uname -r)"
        "linux-modules-extra-$(uname -r)"sudo usermod -a -G render,video
        $LOGNAME # Adding current user to Video, Render groups. See
        prerequisites.wget
        https://repo.radeon.com/amdgpu-install/6.1.1/ubuntu/jammy/amdgpu-install_6.1.60101-1_all.debsudo
        apt install ./amdgpu-install_6.1.60101-1_all.debsudo apt updatesudo
        apt install amdgpu-dkmssudo apt install rocmecho "Please reboot
        system for all settings to take effect."  
  
---  
  * **Install AMDGPU Method:**

**AMDGPU installer**
        
        sudo apt install "linux-headers-$(uname -r)"
        "linux-modules-extra-$(uname -r)"sudo usermod -a -G render,video
        $LOGNAME # Adding current user to Video, Render groups. See
        prerequisites.sudo apt updatewget
        https://repo.radeon.com/amdgpu-install/6.1.1/ubuntu/jammy/amdgpu-install_6.1.60101-1_all.debsudo
        apt install ./amdgpu-install_6.1.60101-1_all.debsudo amdgpu-install
        --usecase=graphics,rocm  
  
---  

**Method 2:**

  1. Before installing ROCm, ensure that your operating system is clean or uninstall any old versions of ROCm.

  2. Check your kernel version by running the command uname -r to confirm that it matches the requirements specified in the ROCm README or documentation. 

  3. Extract the ROCm package by running the command:
         
         $ tar -xvzf $ROCm_FILE

Replace $ROCm_FILE with the name of the downloaded ROCm file. 

  4. Change to the ROCm directory by running the command:
         
         $ cd $ROCm_DIR

Replace $ROCm_DIR with the name of the extracted ROCm directory. 

  5. Give execute permissions to the amdgpu-install script by running the command:
         
         $chmod u+x amdgpu-install

Begin the installation process by running the command:
         
         $./amdgpu-install --usecase=hiplibsdk,rocm

Follow the prompts and provide any necessary inputs during the installation process.

Once the ROCm installation is complete, it is recommended to blacklist the amdgpu driver to prevent auto-probing upon booting into the operating system, before rebooting the system. 

You can refer to the **How to Add amdgpu to Blacklist in Ubuntu** section for instructions on how to blacklist the amdgpu driver. 

Please note that the steps provided are general guidelines, and the exact commands or procedures may vary depending on your specific OS and ROCm version. For detailed instructions specific to your setup, consult the ROCm documentation or official resources. 


#### AMDGPU driver cause fatal error with AMD platform

**Cause:** Some versions of the amdgpu driver may have issues that can result in fatal errors on AMD platforms. 

**Solution:** To avoid potentially fatal errors caused by the amdgpu driver, you can try the following two methods: 

**Method 1: Add amdgpu driver to blacklist in Linux**

  1. Run the following command to open the GRUB configuration file in a text editor:

$ **sudo nano /etc/default/grub**

  2. Locate the line that starts with "GRUB_CMDLINE_LINUX" in the file.

Add the “**modprobe.blacklist=amdgpu** ” "**iommu=pt** " and "**pci=noats** " parameters behind the existing content within the quotation marks (""). 

For example, if the line is:

$ **GRUB_CMDLINE_LINUX=" modprobe.blacklist=amdgpu iommu=pt pci=noats "**

  3. Save the changes by pressing Ctrl + X, then Y, and finally Enter.

  4. Update the GRUB configuration by running the following command:

$sudo grub-mkconfig -o /boot/efi/EFI/ubuntu/grub.cfg

$sudo update-grub

  5. Reboot your system for the changes to take effect:

$sudo reboot

Figure 6. After updated the grub configuration  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525481.jpg) ![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

After rebooting, the iommu=pt and pci=noats parameters will be added to the kernel command line. These parameters may help address certain issues or improve compatibility for your AMD platform.  Please note that modifying the GRUB configuration can have potential consequences on system behavior. If you experience any further issues or instabilities, consider reverting the changes or seeking assistance from AMD technical support or your distribution's support channels. 

* * *  
  
---|---  

**Method 2: Disable IOMMU under BIOS.**

  1. Set IOMMU to disable in BIOS: Advance > AMD CBS > NBIO Common Options > IOMMU disable

Figure 7. Disable IOMMU  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525482.jpg)


  * How to uninstall ROCm


##### How to uninstall ROCm

**Solution** : 

To uninstall ROCm, please follow the steps below:

### SUMMARY STEPS

  1. Open a terminal window.
  2. Run the following command to uninstall the ROCm packages from your system:
  3. Next, clean the ROCm repository configuration by running the following command:
  4. Use the following command to remove the amdgpu-install package:
  5. Finally, remove the amd-nonfree-radeon package by running the following command:


### DETAILED STEPS

| Command or Action | Purpose  
---|---|---  
**Step 1** |  Open a terminal window. |   
**Step 2** |  Run the following command to uninstall the ROCm packages from your system: |  **$sudo amdgpu-uninstall**  
**Step 3** |  Next, clean the ROCm repository configuration by running the following command: |  **$sudo amdgpu-repo –clean**  
**Step 4** |  Use the following command to remove the amdgpu-install package: |  **$sudo apt-get -y purge amdgpu-install**  
**Step 5** |  Finally, remove the amd-nonfree-radeon package by running the following command: |  **$sudo apt-get -y purge amd-nonfree-radeon** These steps will uninstall the ROCm packages and related components from your system.  
  
###### What to do next

**Note:** Please note that the specific commands provided are suitable for Ubuntu or Debian-based systems. If you are using a different Linux distribution, the package manager commands may vary. Adjust the commands accordingly or refer to the documentation provided by your distribution for the correct package management commands. 

After completing these steps, it is recommended to reboot your system to ensure any remaining ROCm components are fully cleared. 

#### Why does the AMD application become unresponsive on multi-GPU systems

**Cause:** Running on a system with multiple GPUs the application hangs with the GPU use at 100%, but without the expected GPU temperature buildup 

This issue often results in the following message in the application transcript: 

NCCL WARN Missing "iommu=pt" from kernel command line which can lead to system instability or hang!   
---  
  
**Solution:**

To resolve this issue add iommu=pt to GRUB_CMDLINE_LINUX_DEFAULT in /etc/default/grub. 

Then run the following command:

**$ sudo update-grub**

Reboot the system, and run the following command:

**$ cat /proc/cmdline**

The returned information should reflect the addition of iommu: 

BOOT_IMAGE=/vmlinuz-5.15.0-101-generic root=/dev/mapper/ubuntu--vg-ubuntu--lv ro iommu=pt   
---

---

## Page 8: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/c/hw/c885A/install/b_c885a-m8-server-troubleshooting-guide/m-Chapter-7-BIOS-Related-Issue.html

# BIOS Related Issue  
  
This BIOS Related Issue contains the following topics:

## BIOS Related Issue 

When an issue occurs (error or loss), please refer to the following sections for initial troubleshooting. 

  * System Power-on issue
  * POST issue
  * Boot with no display
  * OS boot issue
  * Error occur after a BIOS setting is changed
  * Failure occurs during ROM flash via BMC web
  * PCIe Slot
  * Post
  * Agesa POST code
  * BIOS POST code


### System Power-on issue

**Symptom:**

  * The system has no response when the power button is pressed.

  * The system power/health LED is abnormal.


**Action:**

  * Check if there’s improperly seated component (e.g., PSU, CPU, DIMMs, cables..) 

  * Ensure the system FWs comply with the FW table. If not, please do firmware update. 

  * If the issue still exists, please contact TAC.


### POST issue

**Symptom:**

  * The system hangs in POST.

  * The system can’t complete POST.


**Action:**

  * Check the 80 port and POST error messages, refer to POST code table to do the initial troubleshooting. 

  * Shut down the system and try to break the system down to the minimum hardware configuration first, then power on the system. 

  * Clear CMOS and reboot the system.

  * Ensure the system FWs comply with the FW table. If not, please do firmware update. 

  * If the issue still exists, please contact TAC.


### Boot with no display

**Symptom:**

  * The system boots, but has no video output.


**Action:**

  * Unplug mini-DP and plug again.

  * If the issue still exists, please contact TAC.


### OS boot issue

**Symptom:**

  * The system cannot boot an installed OS.


**Action:**

  * Check if the OS is corrupted, replace it with another OS device.

  * System only supports UEFI mode, check if the user uses the legacy OS.

  * Check if the secure boot is enabled, if yes, please disable it in BIOS menu and reboot the system.

  * If system cannot boot using the OS path in Boot Override, try from the embedded EFI SHELL as below:

    1. Find your OS partition and access it

ex. Shell> fs1:

    2. Access to the EFI folder

ex. FS1> cd EFI

    3. Access to the BOOT folder

ex. FS1\EFI> cd BOOT

    4. Execute the OS boot path

ex. FS1\EFI\BOOT> BOOTX64.EFI


### Error occur after a BIOS setting is changed 

**Symptom:**

  * The system cannot boot normally after settings were changed


**Action:**

  * Clear CMOS to load default settings, and reboot system.

  * Flash BIOS to restore the system to default settings.

  * Check the system logs to determine what changes were made, and then change the settings back to the original configuration. 

  * If the issue still exists, please contact TAC.


### Failure occurs during ROM flash via BMC web 

**Symptom:**

  * Any abnormal/error windows pop up during flash.


**Action:**

  * Check if the BMC connection is normal.

  * Check if the network cable is loose.

  * Make sure to use the right ROM file.

  * If there’s an interrupted during a ROM flash, or the ROM image is corrupted and the server does not start, re-flash the BIOS. 

  * If the issue still exists, please contact TAC.


### PCIe Slot

  * Fixed PFA for PCIE Slots
  * NVME
  * CEM PCIE Slot
  * GPU Slot
  * OCP Slot
  * PCIE information in the Setup Page
  * PCIE information for the M.2s in the Setup


#### Fixed PFA for PCIE Slots

When an issue occurs (error or loss), please refer to the table below to find out the problematic device. 

#### NVME

![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525483.jpg)

1 |  0x6D  
---|---  
2 |  0x44  
3 |  0x6C  
4 |  0x43  
5 |  0x0D  
6 |  0x24  
7 |  0x0C  
8 |  0x23  
9 |  0xE3  
10 |  0xC3  
11 |  0xE4  
12 |  0xC4  
13 |  0xAA  
14 |  0x8D  
15 |  0xA3  
16 |  0x86  
16 |  NVMe SSD X 8  
17 |  SAS / SATA SSD X 8  
18 |  NVMe SSD X 8  
  
![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525484.jpg)

#### CEM PCIE Slot

![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525485.jpg)

1 |  FHHL12; 0xE8 ~ 0xED  
---|---  
2 |  FHHL14; 0x8E or 0x93  
3 |  (None)  
4 |  0xA4 ~ 0xA9  
5 |  0x94 ~ 0x99  
6 |  0xC5 ~ 0xCA  
7 |  0xEE ~ 0xF5  
8 |  0x06 ~ 0x0B  
9 |  0x2B ~ 0x30  
10 |  0x4B ~ 0x50  
11 |  0x66 ~ 0x6B  
12 |  FHHL11; 0x45 ~ 0x4A  
13 |  FHHL13; 0x25 ~ 0x2A  
14 |  FHHL15; 0x35  
15 |  MB_PSU2  
16 |  DC-SCM  
17 |  OCP2  
18 |  OCP1  
19 |  MB_PSU1  
  
![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525486.jpg)

#### GPU Slot

![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525487.jpg)

![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525488.jpg)

#### OCP Slot

![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525489.jpg)

1 |  M.2: 0xD0, 0xD1 OCP2: 0xD0  
---|---  
2 |  With M.2: 0xCF With OCP2: 0xD2  
  
![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525490.jpg)

**PCIE information in the Setup Page**

#### PCIE information in the Setup Page 

The GPU server provides the status of all PCIe slots so that users can easily see if a PCIe device is plugged in or not. 

![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525492.jpg)

![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525493.jpg)

![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525494.jpg)

#### PCIE information for the M.2s in the Setup 

The GPU server provides an M.2 index to help users easily know which M.2 they have installed or will be accessed.

![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525494.jpg)

![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525495.jpg)

![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525496.jpg)

### Post

When system post hang occurs, please note the number on debug panel (**Figure 6: 2400W *2 CRPS Power Supply**) and refer to the table below to check the root cause. For more information, please contact TAC. 

Figure 1. Debug Panel  ![](/c/dam/en/us/td/i/500001-600000/520001-530000/525001-526000/525361.jpg)

Note: We have both Agesa and BIOS Post codes during POST. The Agesa Post code is sent by the Agesa code and consists of 2 bytes, such as 0xE000. On the other hand, the BIOS Post Code is sent from an AMI-based BIOS and is only one byte. This implies that the high byte is not relevant for the BIOS Post code, such as 0xXX00. 

### Agesa POST code

  * StartProcessorTestPoints
  * Memory test points
  * PMU Test Points
  * Original Post code
  * CPU test points
  * Extended memory test point
  * Gnb Earlier init
  * PMU test points
  * ABL0 test points
  * ABL5 test points


#### StartProcessorTestPoints

0xE000 | Entry used for range testing for @b Processor related TPs  
---|---  
****  
  
#### Memory test points

0xE001 | Memory structure initialization (Public interface)  
---|---  
0xE002 | SPD Data processing (Public interface)  
0xE003 | Memory configuration (Public interface) Phase 1  
|   
0xE004 | DRAM initialization  
0xE005 | ProcMemSPDChecking  
0xE006 | ProcMemModeChecking  
0xE007 | Speed and TCL configuration  
0xE008 | ProcMemSpdTiming  
0xE009 | ProcMemDramMapping  
0xE00A | ProcMemPlatformSpecificConfig  
0xE00B | ProcMemPhyCompensation  
0xE00C | ProcMemStartDcts  
0xE00D | ProcMemBeforeDramInit (Public interface)  
0xE00E | ProcMemPhyFenceTraining  
0xE00F | ProcMemSynchronizeDcts  
0xE010 | ProcMemSystemMemoryMapping  
0xE011 | ProcMemMtrrConfiguration  
0xE012 | ProcMemDramTraining  
0xE013 | ProcMemBeforeAnyTraining(Public interface)  
  
#### PMU Test Points

0xE014 | ABL Mem - PMU - Before PMU Firmware load  
---|---  
0xE015 | ABL Mem - PMU - After PMU Firmware load  
0xE016 | ABL Mem - PMU Populate SRAM Timing  
0xE017 | ABL Mem - PMU Populate SRAM Config  
0xE018 | ABL Mem - PMU Write SRAM Msg Block  
0xE019 | ABL Mem - Wait for Phy Cal Complete  
0xE01A | ABL Mem - Phy Cal Complete  
0xE01B | ABL Mem - PMU Start  
0xE01C | ABL Mem - PMU Started  
0xE01D | ABL Mem - PMU Waiting for Complete  
0xE01E | ABL Mem - PMU Stage Dec Init  
0xE01F | ABL Mem - PMU Stage Training Wr Lvl  
0xE020 | ABL Mem - PMU Stage Training Rx En  
0xE021 | ABL Mem - PMU Stage Training Rd Dqs  
0xE022 | ABL Mem - PMU Stage Traning Rd 2D  
0xE023 | ABL Mem - PMU Stage Training Wr 2D  
0xE024 | ABL Mem - PMU Queue Empty  
0xE025 | ABL Mem - PMU US message Start  
0xE026 | ABL Mem - PMU US message End  
0xE027 | ABL Mem - PMU Complete  
0xE028 | ABL Mem - PMU - After PMU Training  
0xE029 | ABL Mem - PMU - Before Disable PMU  
  
#### Original Post code

0xE02A | ABL Mem - ProcMemTransmitDqsTraining  
---|---  
0xE02B | ABL Mem - Start write sweep  
0xE02C | ABL Mem - Set Transmit DQ delay  
0xE02D | ABL Mem - Write test pattern  
0xE02E | ABL Mem - Read Test pattern  
0xE02F | ABL Mem - Compare Test pattern  
0xE030 | ABL Mem - Update results  
0xE031 | ABL Mem - Start Find passing window  
0xE032 | ABL Mem - ProcMemMaxRdLatencyTraining  
0xE033 | ABL Mem - Start sweep  
0xE034 | ABL Mem - Set delay  
0xE035 | ABL Mem - Write test pattern  
0xE036 | ABL Mem - Read Test pattern  
0xE037 | ABL Mem - Compare Test pattern  
0xE038 | ABL Mem - Online Spare init  
0xE039 | ABL Mem - Chip select Interleave Init  
0xE03A | ABL Mem - Node Interleave Init  
0xE03B | ABL Mem - Channel Interleave Init  
0xE03C | ABL Mem - ECC initialization  
0xE03D | ABL Mem - Platform Specific Init  
0xE03E | ABL Mem - Before callout for "AgesaReadSpd"  
0xE03F | ABL Mem - After callout for "AgesaReadSpd"  
0xE040 | ABL Mem - Before optional callout "AgesaHookBeforeDramInit"  
0xE041 | ABL Mem - After optional callout "AgesaHookBeforeDramInit"  
0xE042 | ABL Mem - Before optional callout "AgesaHookBeforeDQSTraining"   
0xE043 | ABL Mem - After optional callout "AgesaHookBeforeDQSTraining"   
0xE044 | ABL Mem - Before optional callout "AgesaHookBeforeDramInit"  
0xE045 | ABL Mem - After optional callout "AgesaHookBeforeDramInit"  
0xE046 | ABL Mem - After MemDataInit  
0xE047 | ABL Mem - Before InitializeMCT  
0xE048 | ABL Mem - Before LV DDR3  
0xE049 | ABL Mem - Before InitMCT  
0xE04A | ABL Mem - Before OtherTiming  
0xE04B | ABL Mem - Before UMAMemTyping  
0xE04C | ABL Mem - Before SetDqsEccTmgs  
0xE04D | ABL Mem - Before MemClr  
0xE04E | ABL Mem - Before On DIMM Thermal  
0xE04F | ABL Mem - Before DMI  
0xE050 | ABL MEM - End of phase 3 memory code  
  
#### CPU test points

0xE051 | Entry point CPU init after training  
---|---  
0xE052 | Exit point CPU init after training  
0xE053 | Entry point CPU APOB data init  
0xE054 | Exit point CPU APOB data init  
0xE055 | Entry point CPU Optimized boot init  
0xE056 | Exit point CPU Optimized boot init  
0xE057 | Entry point CPU APOB EDC info init  
0xE058 | Exit point CPU APOB EDC info init  
0xE059 | Entry point CPU APOB CCD map data init  
0xE05A | Exit point CPU APOB CCD map data init  
  
#### Extended memory test point

0xE080 | ProcMemSendMRS2  
---|---  
0xE081 | Sedding MRS3  
0xE082 | Sending MRS1  
0xE083 | Sending MRS0  
0xE084 | Continuous Pattern Read  
0xE085 | Continuous Pattern Write  
0xE086 | Mem: 2d RdDqs Training begin  
0xE087 | Mem: Before optional callout to platform BIOS to change External Vref during 2d Training   
0xE088 | Mem: After optional callout to platform BIOS to change External Vref during 2d Training   
0xE089 | Configure DCT For General use begin  
0xE08A | Configure DCT For training begin  
0xE08B | Configure DCT For Non-Explicit  
0xE08C | Configure to Sync channels  
0xE08D | Allocate C6 Storage  
0xE08E | Before LV DDR4  
0xE08F | Before LV DDR3  
  
#### Gnb Earlier init

0xE090 | TP0x90  
---|---  
0xE091 | GNB earlier interface  
0xE092 | GNB Early VGA entry  
0xE093 | GNB Early VGA exit  
0xE094 | GNB Initialization entry  
0xE095 | GNB Initialization exit  
0xE096 | GNB internal debug code  
0xE097 | GNB internal debug code  
0xE098 | GNB internal debug code  
0xE099 | GNB internal debug code  
0xE09A | GNB internal debug code  
0xE09B | GNB internal debug code  
0xE09C | GNB internal debug code  
0xE09D | GNB internal debug code  
0xE09E | GNB internal debug code  
0xE09F | GNB internal debug code  
0xE0A0 | TP0xA0  
0xE0A1 | GNB internal debug code  
0xE0A2 | GNB internal debug code  
0xE0A3 | GNB internal debug code  
0xE0A4 | GNB internal debug code  
0xE0A5 | GNB internal debug code  
0xE0A6 | GNB internal debug code  
0xE0A7 | GNB internal debug code  
0xE0A8 | GNB internal debug code  
0xE0A9 | GNB internal debug code  
0xE0AA | GNB internal debug code  
0xE0AB | GNB internal debug code  
0xE0AC | GNB internal debug code  
0xE0AD | GNB internal debug code  
0xE0AE | GNB internal debug code  
0xE0AF | GNB internal debug code  
0xEA00 | ABL Begin  
0xEA01 | ABL End  
0xEA10 | ABL Debug Synchronization  
0xE0B0 | Abl1Begin  
0xE0B1 | ABL 1 Initialization  
0xE0B2 | ABL 1 DF Early  
0xE0B3 | ABL 1 DF Pre Training  
0xE0B4 | ABL 1 Debug Synchronization  
0xE0B5 | ABL 1 Error Detected  
0xE0B6 | ABL 1 Global memory error detected  
0xE0B7 | ABL 1 End  
0xE0B8 | ABL 2 Begin  
0xE0B9 | ABL 2 Initialization  
0xE0BA | ABL 2 After Training  
0xE0BB | ABL 2 Debug Synchronization  
0xE0BC | ABL 2 Error detected  
0xE0BD | ABL 2 Global memory error detected  
0xE0BE | ABL 2 End  
0xE0BF | ABL 3 Begin  
0xE0C0 | ABL 3 Initialziation  
0xE1C0 | ABL 3 GMI/xGMI Initialization Stage 1  
0xB1C0 | ABL 3 GMI/xGMI Initialization Stage 1 Warning  
0xF1C0 | ABL 3 GMI/xGMI Initialization Stage 2 Error  
0xE2C0 | ABL 3 GMI/xGMI Initialization Stage 2  
0xB2C0 | ABL 3 GMI/xGMI Initialization Stage 2 Warning  
0xF2C0 | ABL 3 GMI/xGMI Initialization Stage 2 Error  
0xE3C0 | ABL 3 GMI/xGMI Initialization Stage 3  
0xB3C0 | ABL 3 GMI/xGMI Initialization Stage 3 Warning  
0xF3C0 | ABL 3 GMI/xGMI Initialization Stage 3 Error  
0xE4C0 | ABL 3 GMI/xGMI Initialization Stage 4  
0xB4C0 | ABL 3 GMI/xGMI Initialization Stage 4 Warning  
0xF4C0 | ABL 3 GMI/xGMI Initialization Stage 4 Error  
0xE5C0 | ABL 3 GMI/xGMI Initialization Stage 5  
0xB5C0 | ABL 3 GMI/xGMI Initialization Stage 5 Warning  
0xF5C0 | ABL 3 GMI/xGMI Initialization Stage 5 Error  
0xE6C0 | ABL 3 GMI/xGMI Initialization Stage 6  
0xB6C0 | ABL 3 GMI/xGMI Initialization Stage 6 Warning  
0xF6C0 | ABL 3 GMI/xGMI Initialization Stage 6 Error  
0xE7C0 | ABL 3 GMI/xGMI Initialization Stage 7  
0xE8C0 | ABL 3 GMI/xGMI Initialization Stage 8  
0xE9C0 | ABL 3 GMI/xGMI Initialization Stage 9  
0xF9C0 | ABL 3 GMI/xGMI Initialization Stage 9 Error  
0xEAC0 | ABL 3 GMI/xGMI Initialization Stage 10  
0xFAC0 | ABL 3 GMI/xGMI Initialization Stage 10 Error  
0xE0C1 | Abl3ProgramUmcKeys  
0xE0C2 | ABL 3 DF Final Initalization  
0xE0C3 | ABL 3 Execute Synchronization Function  
0xE0C4 | ABL 3 Debug Synchronization Function  
0xE0C5 | ABL 3 Error Detected  
0xE0C6 | ABL 3 Global memroy error detected  
0xE0C7 | ABL 4 Initialiation - cold boot  
0xE0C8 | ABL 4 Memory test - cold boot  
0xE0C9 | ABL 4 APOB Initialization - cold boot  
0xE0CA | ABL 4 Finalize memory settings - cold boot  
0xE0CB | ABL 4 CPU Initialize Optimized Boot - cold boot  
0xE0CC | ABL 4 Gmi Pcie Training - cold boot  
0xE0CD | ABL 4 Cold boot End  
0xE0CE | ABL 4 Initialization - Resume boot  
0xE0CF | ABL 4 Resume End  
0xE0D0 | ABL 4 End Cold/Resume boot  
0xE0D1 | ABL 2 memory initialization  
0xE0D2 | ABL 3 memory initialization  
0xE0D3 | ABL 3 End  
0xE0D4 | ABL 1 Enter Memory Flow  
0xE0D5 | Memory flow memory clock synchronization  
0xE0E0 | Before IDS calls out to get IDS data  
0xE0E1 | After IDS calls out to get IDS data  
  
#### PMU test points

0xE0F9 | Failed PMU training.  
---|---  
0xE0FA | End of phase 1 memory code  
0xE0FB | End of phase 2 memory code  
  
#### ABL0 test points

0xE0FC | Abl0Begin  
---|---  
0xE0FD | ABL 0 End  
0xE0FE | Abl0 Begin with Fatal Mode  
0xE0FF | ABL 0 End with Fatal Mode  
  
#### ABL5 test points

0xE100 | ABL 7 End  
---|---  
0xE101 | ABL 7 Resume boot  
0xE102 | ABL 6 End  
0xE103 | ABL 6 Initialization  
0xE104 | End of phase 1b memory code  
0xE105 | ABL 1b memory initialization  
0xE106 | ABL 6 Global memory error detected  
0xE107 | ABL 1b Debug Synchroniza0ion Function  
0xE108 | ABL 4b Debug Synchronization Function  
0xE109 | AblbBegin  
0xE10A | Ab4bBegin  
0xE10B | BSP encountered HMAC fail on APOB Header  
0xE10C | ABL 18 End  
0xE10D | ABL 18 Resume boot  
0xE10E | ABL 15 End  
0xE10F | ABL 15 Initialization  
0xE110 | Before UMC based device initialization  
0xE111 | After UMC based device initialization  
0xE2A0 | ABL Error General ASSERT  
0xE2A1 | Unknown Error  
0xE2A3 | ABL Error Log Inig Error  
0xE2A4 | ABL Error for On DIMM thermal Heap allocation error  
0xE2A5 | ABL Error for memory test error  
0xE2A6 | ABL Error while executing memory test error  
0xE2A7 | ABL Error DDR Post Packge Repair Mem Auto Heap Alloc error  
0xE2A8 | ABL Error for DDR Post Package repair Apob Heap Alloc error  
0xE2A9 | ABL Error for DDR Post Package Repair No PPR Table Heap Aloc error   
0xE2AA | ABL Error for Ecc Mem Auto Aloc Error error  
0xE2AB | ABL Error for Soc Scan Heap Aloc error  
0xE2AC | ABL Error for Soc Scan No Die error  
0xE2AD | ABL Error for Nb Tech Heap Aloc error  
0xE2AE | ABL Error for No Nb Constructor error  
0xE2B0 | ABL Error for No Tech Constructor error  
0xE2B1 | ABL Error for ABL1b Auto Alocation error  
0xE2B2 | ABL Error for ABL1b No NB Constructor error  
0xE2B3 | ABL Error for ABL2 No Nb Constructor error  
0xE2B4 | ABL Error for ABL3 Auto Allocation error  
0xE2B5 | ABL Error for ABL3 No Nb Constructor error  
0xE2B6 | ABL Error for ABL1b General error  
0xE2B7 | ABL Error for ABL2 General error  
0xE2B8 | ABL Error for ABL3 General error  
0xE2B9 | ABL Error for Get Target Speed error  
0xE2BA | ABL Error for Flow P1 Family Support error  
0xE2BB | ABL Error for No Valid Ddr4 Dimms error  
0xE2BC | ABL Error for No Dimm Present error  
0xE2BD | ABL Error for Flow P2 Family Support error  
0xE2BE | ABL Error for Heap Deallocation for PMU Sram Msg Block error  
0xE2BF | ABL Error for DDR Recovery error  
0xEBC0 | ABL Error for RRW Test error  
0xE2C1 | ABL Error for On Die Thermal error  
0xE2C2 | ABL Error for Heap Allocation For Dct Struct Amd Ch Def structure error   
0xE2C3 | ABL Error for Heap Allocation for PMU SRAM Msg block error  
0xE2C4 | ABL Error for Heap Phy PLL lock Flure error  
0xE2C5 | ABL Error for Pmu Training error  
0xE2C6 | ABL Error for Failure to Load or Verify PMU FW error  
0xE2C7 | ABL Error for Allocate for PMU SRAM Msg Block No Init error  
0xE2C8 | ABL Error for Failure BIOS PMU FW Mismatch AGESA PMU FW version error   
0xE2C9 | ABL Error for Agesa memory test error  
0xE2CA | ABL Error for Deallocate for PMU SRAM Msg Block error  
0xE2CB | ABL Error for Module Type Mismatch RDIMM error  
0xE2CC | ABL Error for Module type Mismatch LRDIMM error  
0xE2CD | ABL Error for MEm Auto NVDIM error  
0xE2CE | ABL Error for Unknown Response error  
0xE2CF | ABL Error for Over Clock Error RRW Test Results Error  
0xE2D0 | ABL Error for Over Clock Error PMU Training Error  
0xE2D1 | ABL Error for ABL1 General Error  
0xE2D2 | ABL Error for ABL2 General Error  
0xE2D3 | ABL Error for ABL3 General Error  
0xE2D4 | ABL Error for ABL4 General Error  
0xE2D5 | ABL Error over clock Mem Init Error  
0xE2D6 | ABL Error over clock Mem Other Error  
0xE2D7 | ABL Error for ABL6 General Error  
0xE2D8 | ABL Error Event Log Error  
0xE2D9 | ABL Error FATAL ABL1 Log Error  
0xE2DA | ABL Error FATAL ABL2 Log Error  
0xE2DB | ABL Error FATAL ABL3 Log Error  
0xE2DC | ABL Error FATAL ABL4 Log Error  
0xE2DD | ABL Error Slave Sync function execution Error  
0xE2DE | ABL Error Slave Sync communication with data set to master Error   
0xE2DF | ABL Error Slave broadcast communication from master to slave Error   
0xE2E0 | ABL Error FATAL ABL6 Log Error  
0xE2E1 | ABL Error Slave Offline Error  
0xE2E2 | ABL Error Slave Informs Master Error Info Error  
0xE2E3 | ABL Error Heap Locate for PMU SRAM Msg Block Error  
0xE2E4 | ABL Error ABL2 Auto Error  
0xE2E5 | ABL Error Flow P3 Family support Error  
0xE2E5 | ABL Error Abl 4 Gen Error  
0xE2E7 | ABL Error Mix RDIMM & LRDIMM in a channel  
0xE2E8 | ABL Error Memory Present on Disconnected Channel  
0xE2EB | ABL Error MBIST Heap Allocation Error  
0xE2EC | ABL Error MBIST Results Error  
0xE2ED | ABL Error NO Dimm Smcus Info Error  
0xE2EE | ABL Error Por Max Freq Table Error  
0xE2EF | ABL Error Unsupported DIMM Config Error  
0xE2F0 | ABL Error No Ps Table Error  
0xE2F1 | ABL Error Cad Bus Timing Not Found Error  
0xE2F2 | ABL Error Data Bus Timing Not Found Error  
0xE2F3 | ABL Error LrDIMM IBT Not Found Error  
0xE2F4 | ABL Error Unsupported Dimm Config Max Freq Error Error  
0xE2F5 | ABL Error Mr0 Not Found Error  
0xE2F6 | ABL Error Obt Pattern Not found Error  
0xE2F7 | ABL Error Rc10 Op Speed Not FOund Error  
0xE2F8 | ABL Error Rc2 Ibt Not Found Error  
0xE2F9 | ABL Error Rtt Not Found Error  
0xE2FA | ABL Error Checksum ReStrt Results Error  
0xE2FB | ABL Error No Chipselect Results Error  
0xE2FC | ABL Error No Common Cas Latency Results Error  
0xE2FD | ABL Error Cas Latency exceeds Taa Max Error  
0xE2FE | ABL Error Nvdimm Arm Mismatch Power Policy Error  
0xE2FF | ABL Error Nvdimm Arm Mismatch Power Source Error  
0xE300 | ABL Error ABL 1 Mem Init Error  
0xE301 | ABL Error ABL 2 Mem Init Error  
0xE302 | ABL Error ABL 4 Mem Init Error  
0xE303 | ABL Error ABL 6 Mem Init Error  
0xE304 | ABL Error ABL 1 error repor Error  
0xE305 | ABL Error ABL 2 error repor Error  
0xE306 | ABL Error ABL 3 error repor Error  
0xE307 | ABL Error ABL 4 error repor Error  
0xE308 | ABL Error ABL 6 error repor Error  
0xE30A | ABL Error message slave sync function execution Error  
0xE30B | ABL Error slave offline Error  
0xE30C | ABL Error Sync Master Error  
0xE30D | ABL Error Slave Informs Master Info Message Error  
0xE30E | ABL Error Mix Hynix LRDIMM with other vendor LRDIMM in a channel   
0xE30F | ABL Error General Assert Error  
0xE310 | ABL ErrorNo Dimms On Any Channel in system  
0xE311 | ABL Error for Shared Heap Aloc error  
0xE312 | ABL Error for Main Heap Aloc error  
0xE313 | ABL Error for Shared Heap loc error  
0xE314 | ABL Error for Main Heap loc error  
0xE316 | ABL Error No memory available in system  
0xE320 | ABL Error Mixed Ecc and Non-Ecc DIMM in a channel  
0xE321 | ABL Error Mixed 3DS and Non-3DS DIMM in a channel  
0xE322 | ABL Error Mixed x4 and x8 DIMM in a channel  
0xE323 | ABL Memory MBIST Rrw default test  
0xE324 | ABL Memory MBIST Interface test  
0xE325 | ABL Memory MBIST DataEye  
0xE326 | ABL Memory Post Package Repair  
0xE327 | ABL Error S0i3 DF restore buffer Error  
0xE328 | ABL Error CPU OPN Mismatch in case of Multi Socket population   
0xE329 | Recoverable APCB Checksum Error  
0xE32A | Fatal APCB Checksum Error  
0xE32B | ABL Error BIST Failure  
0xE32C | ABL Error DDR Type Mismatch DDR5 Error  
0xE32D | ABL Error Mix DIMM with different ECC bit size in a channel  
0xE32E | ABL Error No ability to recover I2C bus without power cycling the platform   
0xE32F | ABL Error I2C reset failure  
0xE330 | ABL Error DDR Module Type Mismatch  
0xE331 | ABL Error PMIC Error  
0xE332 | ABL Error Incompatible OPN  
0xE333 | ABL Error No ability to recover I3C bus without power cycling the platform   
0xE334 | ABL Error I3C reset failure  
0xE335 | ABL Error Absence of either or both AC-Power GPIO or WLAN GPIO Apcb Data   
0xE336 | ABL Memory Heal BIST Start  
0xE337 | ABL Memory Heal BIST End  
0xE338 | ABL Memory Heal BIST Write  
0xE339 | ABL Memory Heal BIST Read  
0xE33A | ABL Memory Heal BIST Repair  
0xE33B | Timeout at PMFW SwitchToMemoryTrainingState  
0xE33C | DIMM with RCD Montage version B1 detected  
0xE33D | ABL DDR PMU training complete  
0xE33E | Timeout at PMFW SwitchToMemoryTrainingState  
0xE33F | DIMM with TI PMIC revision 1.1 (XTPS) detected  
0xE343 | ABL DDR DIMM SPD verify CRC failure  
0xE344 | ABL DDR DIMM SPD Invalid Field Value  
0xE345 | ABL Timeout to detect CPU OPN Mismatch in case of Multi Socket population   
0xE346 | ABL Error 3DS DIMM in a SP6 system  
0xE350 | ABL DDR Runtime Post Package Repair Begin  
0xE351 | ABL DDR Runtime Post Package Repair End  
0xE60B | ABL Functions execute Before  
0xE60C | ABL Functions execute  
0xEFFF | EndAgesas  
  
### BIOS POST code

  * SEC Phase
  * PEI Phase
  * DXE Phase


#### SEC Phase

0xXX00 | Not used  
---|---  
**Progress Codes**  
0xXX01 | Power on. Reset type detection (soft/hard).  
0xXX02 | AP initialization before microcode loading  
0xXX03 | North Bridge initialization before microcode loading  
0xXX04 | South Bridge initialization before microcode loading  
0xXX05 | OEM initialization before microcode loading  
0xXX06 | Microcode loading  
0xXX07 | AP initialization after microcode loading  
0xXX08 | North Bridge initialization after microcode loading  
0xXX09 | South Bridge initialization after microcode loading  
0xXX0A | OEM initialization after microcode loading  
0xXX0B | Cache initialization  
**SEC Error Codes**  
0xXX0C - 0xXX0D | Reserved for future AMI SEC error codes  
0xXX0E | Microcode not found  
0xXX0F | Microcode not loaded  
  
#### PEI Phase

**Progress Codes**  
---  
0xXX10 | PEI Core is started  
0xXX11 | Pre-memory CPU initialization is started.  
0xXX15 | Pre-memory NB Initialization  
0xXX19 | Pre-memory SB Initialization.  
0xXX2B | Memory Initialization - SPD Read  
0xXX2C | Memory presence detection  
0xXX2D | Gather Remaining SPD Data  
0xXX2E | Train DDR  
0xXX2F | Memory Initialization Start  
0xXX31 | Memory Initialization Complete  
0xXX32 | CPU POST-Memory Initialization  
0xXX33 | CPU Cache initialization  
0xXX34 | Application Processor(s) (AP) initialization  
0xXX35 | BSP Selection  
0xXX36 | SMM Initialization.  
0xXX37 | POST-Memory NB Initialization  
0xXX3B | POST-Memory SB Initialization  
0xXX4F | DXE IPL is started  
**PEI Error Codes**  
0xXX50 | Memory initialization error. Invalid memory type or incompatible memory speed   
0xXX51 | Memory initialization error. SPD reading has failed  
0xXX52 | Memory initialization error. Invalid memory size or memory modules do not match.   
0xXX53 | Memory initialization error. No usable memory detected  
0xXX54 | Unspecified memory initialization error.  
0xXX55 | Memory not installed  
0xXX56 | Invalid CPU Type / Speed  
0xXX57 | CPU Mismatch (SIMULATED)  
0xXX58 | CPU self test failed or possible CPU cache error  
0xXX59 | No MicroCode / MicroCode Update Failed  
0xXX5B | reset PPI is not available  
0xXX5C - 0xXX5F | Reserved for future AMI error codes  
**S3 Resume Progress Codes**  
0xXXE1 | S3 Boot Script execution  
0xXXE3 | OS S3 wake vector call  
0xXXE4-0xXXE7 | Reserved for future AMI progress codes  
**S3 Resume Error Codes**  
0xXXE8 | S3 Resume Failed  
0xXXE9 | S3 Resume PPI not Found  
0xXXEA | S3 Resume Boot Script Error  
0xXXEB | S3 OS Wake Error  
0xXXEC-0xXXEF | Reserved for future AMI error codes  
**Recovery Progress Codes**  
0xXXF0 | Recovery condition triggered by firmware (Auto recovery)  
0xXXF1 | Recovery condition triggered by user (Forced recovery)  
0xXXF2 | Recovery process started  
0xXXF3 | Recovery firmware image is found  
0xXXF4 | Recovery Capsule Loaded  
**Recovery Error Codes**  
0xXXF8 | Recovery PPI is not available  
0xXXF9 | Recovery capsule is not found  
0xXXFA | Invalid recovery capsule  
0xXXFB-0xXXFF | Reserved for future AMI error codes  
  
#### DXE Phase

**Progress Codes**  
---  
0xXX60 | DXE Core is started  
0xXX61 | NVRAM initialization  
0xXX62 | Install SB Runtime  
0xXX63 | CPU DXE Initialization  
0xXX68 | PCI HB Initialization  
0xXX69 | NB DXE Initialization  
0xXX6A | NB DXE SMM Initialization  
0xXX70 | SB DXE Initialization  
0xXX71 | SB DXE SMM Initialization.  
0xXX72 | SB DEVICES Initialization  
0xXX78 | ACPI Module Initialization  
0xXX79 | CSM Driver Entry point  
0xXX7A – 0xXX7F | Reserved for future AMI DXE codes  
0xXX80 – 0xXX8F | OEM DXE initialization codes  
0xXX90 | BDS Started.  
0xXX91 | Driver connecting is started  
0xXX92 | PCI Bus initialization is started  
0xXX93 | PCI Bus Hot Plug Controller Initialization  
0xXX94 | PCI Bus Enumeration  
0xXX95 | PCI Bus Request Resources  
0xXX96 | PCI Bus Assign Resources  
0xXX97 | Console Output devices connect  
0xXX98 | Console input devices connect  
0xXX99 | Super IO Initialization  
0xXX9A | USB initialization is started  
0xXX9B | USB Reset  
0xXX9C | USB Detect  
0xXX9D | USB Enable  
0xXX9E – 0xXX9F | Reserved for future AMI codes  
0xXXA0 | IDE initialization is started  
0xXXA1 | IDE Reset  
0xXXA2 | IDE Detect  
0xXXA3 | IDE Enable  
0xXXA4 | SCSI Initialization  
0xXXA5 | SCSI Reset  
0xXXA6 | SCSI Detect  
0xXXA7 | SCSI Enable  
0xXXA8 | Setup Verifying Password  
0xXXA9 | Start of Setup  
0xXXAA | Reserved for ASL (see ASL Status Codes section below)  
0xXXAB | Setup Key Press Wait  
0xXXAC | Reserved for ASL (see ASL Status Codes section below)  
0xXXAD | Ready To Boot event  
0xXXAE | Legacy Boot event  
0xXXAF | Exiting Boot Services  
0xXXB0 | Virtual Address Begin  
0xXXB1 | Virtual Address End  
0xXXB2 | Legacy Option ROM Initialization  
0xXXB3 | System Reset Initiated  
0xXXB4 | USB hot plug  
0xXXB5 | PCI Bus Hot Plug  
0xXXB6 | Clean-up of NVRAM  
0xXXB7 | Configuration Reset (reset of NVRAM settings)  
0xXXB8 – 0xXXBF | Reserved for future AMI codes  
0xXXC0 – 0xXXCF | OEM BDS initialization codes  
**DXE Error Codes**  
0xXXD0 | DXE CPU initialization error  
0xXXD1 | DXE NB initialization error  
0xXXD2 | South Bridge initialization error  
0xXXD3 | Some Architectural Protocols are not available  
0xXXD4 | PCI resource allocation error. Out of Resources  
0xXXD5 | Not enough space for legacy OpROM  
0xXXD6 | No Console Output Devices are found  
0xXXD7 | No Console Input Devices are found  
0xXXD8 | Invalid password  
0xXXD9 | Error loading Boot Option (LoadImage returned error)  
0xXXDA | Boot Option is failed (StartImage returned error)  
0xXXDB | Flash update is failed  
0xXXDC | Reset protocol is not available

---

## Page 9: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/c/hw/c885A/install/b_c885a-m8-server-troubleshooting-guide/b_c885a-m8-server-troubleshooting-guide_index.html

> ## Contents  
>   
> ## Index

---
