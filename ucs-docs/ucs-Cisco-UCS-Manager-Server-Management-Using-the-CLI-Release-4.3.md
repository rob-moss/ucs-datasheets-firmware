# UCS Manager CLI Server Management Guide 4.3

| | |
|---|---|
| **URL Title** | UCS Manager CLI Server Management Guide 4.3 |
| **URL** | https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Server-Mgmt/4-3/b_cisco_ucs_manager_server_mgmt_cli_guide_4_3.html |
| **Long URL** |  |
| **HTML Title** | Cisco UCS Manager Server Management Using the CLI, Release 4.3 |
| **Source file** | `ucs-docs-raw/html/b_cisco_ucs_manager_server_mgmt_cli_guide_4_3.html` |
| **File type** | HTML |
| **Fetched on** | 2026-03-19 15:35:32 |

---

## Page 1: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Server-Mgmt/4-3/b_cisco_ucs_manager_server_mgmt_cli_guide_4_3.html

![Clear Contents of Search](/etc/designs/cdc/fw/i/ic_clear_gray.png)

---

## Page 2: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Server-Mgmt/4-3/b_cisco_ucs_manager_server_mgmt_cli_guide_4_3/m_preface.html

## Audience  
  
This guide is intended primarily for data center administrators with responsibilities and expertise in one or more of the following: 

  * Server administration 

  * Storage administration 

  * Network administration 

  * Network security 


---

## Page 3: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Server-Mgmt/4-3/b_cisco_ucs_manager_server_mgmt_cli_guide_4_3/m-cli-server-new-and-changed-information-4-3.html

## New and Changed Information

This section provides information on new features and changed behaviors in Cisco UCS Manager, Release 4.3. 

Table 1. New Feature and Changed Behavior in Cisco UCS Manager, Release 4.3(6c) BIOS Tokens |  Cisco UCS Manager now has modified BIOS token values for Cisco UCS M8 servers. |  [Processor BIOS Settings](m_cli_configuring_server-related_policies1.html#reference_B158534E2FBF4F81A1D2807B80D84134)  
---|---|---  
Table 2. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(6a) Feature |  Description |  Where Documented  
---|---|---  
Support for C-Series M8 and X-Series M8 servers |  Cisco UCS Manager supports Cisco UCS C220 M8 Server, Cisco UCS C240 M8 Server, and UCS X210c M8 Compute Node.  | 

  * [Server Management Overview](m_server_management_overview-4_1.html#concept_ldd_sgd_xdb)
  * [Scrub Policy Settings](m_cli_configuring_server-related_policies1.html#concept_140F6E7B34CB4E999E444134BB160DA4)

  
Support for CPU Package Power Limit (PPL)  |  Cisco UCS Manager supports configuring the CPU Package Power Limit in Power Control Policy. |  [Creating a Power Control Policy](m_cli_managing_power_in_cisco_ucs.html#task_E14D7E00D291462A8BAF78D11C604A4C)  
Support for Maximum Cooling in Fan Speed Policy |  Cisco UCS Manager supports Maximum Cooling option in Fan Speed Policy to optimize cooling efficiency for CPU. |  [Creating a Power Control Policy](m_cli_managing_power_in_cisco_ucs.html#task_E14D7E00D291462A8BAF78D11C604A4C)  
Support for IPv6 PXE Network Boot |  Cisco UCS Manager now supports PXE Boot using UEFI mode in IPv6-only environments. |  [Creating a Boot Policy](m_cli_configuring_server_boot.html#task_3770655512861624203)  
BIOS Tokens |  Cisco UCS Manager now has new BIOS tokens for UCS X210c M8 Compute Node, Cisco UCS C240 M8 Server, and Cisco UCS C220 M8 Server.  | 

  * [Processor BIOS Settings](m_cli_configuring_server-related_policies1.html#reference_B158534E2FBF4F81A1D2807B80D84134)
  * [RAS Memory BIOS Settings](m_cli_configuring_server-related_policies1.html#reference_08F63A1A00F1470387C604B11CA9A5BF)
  * [Server Management BIOS Settings](m_cli_configuring_server-related_policies1.html#reference_97B422533FBF4539B0F91A64B08818D1)

  
Table 3. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(5c) Feature |  Description |  Where Documented  
---|---|---  
BIOS Tokens |  Cisco UCS Manager includes updates to BIOS tokens for Cisco UCS C-Series and X-Series M7 and M8 servers. | 

  * [Processor BIOS Settings](m_cli_configuring_server-related_policies1.html#reference_B158534E2FBF4F81A1D2807B80D84134)
  * [RAS Memory BIOS Settings](m_cli_configuring_server-related_policies1.html#reference_08F63A1A00F1470387C604B11CA9A5BF)

  
Table 4. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(5a) Feature |  Description |  Where Documented  
---|---|---  
BIOS Tokens |  Cisco UCS Manager now has new BIOS tokens and modifications to existing BIOS tokens and values. | 

  * [Processor BIOS Settings](m_cli_configuring_server-related_policies1.html#reference_B158534E2FBF4F81A1D2807B80D84134)
  * [RAS Memory BIOS Settings](m_cli_configuring_server-related_policies1.html#reference_08F63A1A00F1470387C604B11CA9A5BF)
  * [Server Management BIOS Settings](m_cli_configuring_server-related_policies1.html#reference_97B422533FBF4539B0F91A64B08818D1)

  
Support for C-Series M8 and X-Series M8 servers |  Cisco UCS Manager supports Cisco UCS C225 M8 Server and Cisco UCS X215c M8 Compute Node | 

  * [Power Capping in Cisco UCS](m_cli_managing_power_in_cisco_ucs.html#concept_943D968485A04A92BAA307A2FC59AD18)
  * [Server Management Overview](m_server_management_overview-4_1.html#concept_ldd_sgd_xdb)
  * [Data Sanitization](m_cli_managing_blade_servers.html#data-sanitization)
  * [Scrub Policy Settings](m_cli_configuring_server-related_policies1.html#concept_140F6E7B34CB4E999E444134BB160DA4)
  * [CIMC Secure Boot](m_cli_configuring_server_boot.html#concept_C3FF828A05BE478B88052EE502B379C5)

  
Table 5. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(4b) Feature |  Description |  Where Documented  
---|---|---  
Support for Cisco UCS Fabric Interconnects 9108 100G |  Cisco UCS Manager now supports Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct).  | 

  * [Server Management Overview](m_server_management_overview-4_1.html#concept_ldd_sgd_xdb)
  * [Licenses](m_cli_managing_licenses.html#concept_qws_wnl_xdb)
  * [Obtaining a License](m_cli_managing_licenses.html#task_54B9E7A9AA364F9FA8593A91CAC5A05C)
  * [Power Capping in Cisco UCS](m_cli_managing_power_in_cisco_ucs.html#concept_943D968485A04A92BAA307A2FC59AD18)
  * [Firmware Upgrades](m_cli_firmware_upgrades.html#concept_B9D015E54807414E873314E87B44278A)

  
Table 6. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(4b) Feature |  Description |  Where Documented  
---|---|---  
BIOS Tokens |  Cisco UCS Manager now has new BIOS tokens and modifications to existing BIOS tokens and values. | 

  * [Processor BIOS Settings](m_cli_configuring_server-related_policies1.html#reference_B158534E2FBF4F81A1D2807B80D84134)
  * [RAS Memory BIOS Settings](m_cli_configuring_server-related_policies1.html#reference_08F63A1A00F1470387C604B11CA9A5BF)
  * [Server Management BIOS Settings](m_cli_configuring_server-related_policies1.html#reference_97B422533FBF4539B0F91A64B08818D1)

  
Support Cisco UCS C-Series M8 servers |  Cisco UCS Manager now supports Cisco UCS C245 M8 Servers.  | 

  * [Power Capping in Cisco UCS](m_cli_managing_power_in_cisco_ucs.html#concept_943D968485A04A92BAA307A2FC59AD18)
  * [Server Management Overview](m_server_management_overview-4_1.html#concept_ldd_sgd_xdb)
  * [Data Sanitization](m_cli_managing_blade_servers.html#data-sanitization)
  * [Scrub Policy Settings](m_cli_configuring_server-related_policies1.html#concept_140F6E7B34CB4E999E444134BB160DA4)
  * [CIMC Secure Boot](m_cli_configuring_server_boot.html#concept_C3FF828A05BE478B88052EE502B379C5)

  
Table 7. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(4b) Feature |  Description |  Where Documented  
---|---|---  
BIOS Tokens |  Cisco UCS Manager now has new BIOS tokens and modifications to existing BIOS tokens and values. | 

  * [Processor BIOS Settings](m_cli_configuring_server-related_policies1.html#reference_B158534E2FBF4F81A1D2807B80D84134)
  * [RAS Memory BIOS Settings](m_cli_configuring_server-related_policies1.html#reference_08F63A1A00F1470387C604B11CA9A5BF)
  * [Server Management BIOS Settings](m_cli_configuring_server-related_policies1.html#reference_97B422533FBF4539B0F91A64B08818D1)

  
Support Cisco UCS C-Series M8 servers |  Cisco UCS Manager now supports Cisco UCS C245 M8 Servers.  | 

  * [Power Capping in Cisco UCS](m_cli_managing_power_in_cisco_ucs.html#concept_943D968485A04A92BAA307A2FC59AD18)
  * [Server Management Overview](m_server_management_overview-4_1.html#concept_ldd_sgd_xdb)
  * [Data Sanitization](m_cli_managing_blade_servers.html#data-sanitization)
  * [Scrub Policy Settings](m_cli_configuring_server-related_policies1.html#concept_140F6E7B34CB4E999E444134BB160DA4)
  * [CIMC Secure Boot](m_cli_configuring_server_boot.html#concept_C3FF828A05BE478B88052EE502B379C5)

  
Table 8. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(4a) Feature |  Description |  Where Documented  
---|---|---  
Support for Data Sanitization for Cisco UCS M5, M6, and M7 servers |  Cisco UCS Manager now supports data sanitization feature. Using the data sanitization process, Cisco UCS Manager erases all sensitive data, thus making extraction or recovery of customer data impossible.  |  [Data Sanitization](m_cli_managing_blade_servers.html#data-sanitization)  
BIOS Tokens |  Cisco UCS Manager now has new BIOS tokens and modifications to existing BIOS tokens and values. | 

  * [Processor BIOS Settings](m_cli_configuring_server-related_policies1.html#reference_B158534E2FBF4F81A1D2807B80D84134)
  * [RAS Memory BIOS Settings](m_cli_configuring_server-related_policies1.html#reference_08F63A1A00F1470387C604B11CA9A5BF)
  * [Server Management BIOS Settings](m_cli_configuring_server-related_policies1.html#reference_97B422533FBF4539B0F91A64B08818D1)

  
Table 9. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(2c) Feature  |  Description  |  Where Documented   
---|---|---  
Support Cisco UCS X-Series M7 servers |  Cisco UCS Manager now supports Cisco UCS X410c M7 Compute Node.  Cisco UCS X-Series servers support Intelligent Fabric Modules (IFM), which function similarly to the Input/Output Module (IOM) in Cisco UCS B-Series servers.  |  —  
Support Cisco UCS VIC |  Cisco UCS Manager now supports following VIC cards:

  * Cisco UCS VIC 15230
  * Cisco UCS VIC 15427
  * Cisco UCS VIC 15237 mLOM

|  —  
Table 10. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(6c) Feature  |  Description  |  Where Documented   
---|---|---  
Support Cisco UCS C-Series M7 servers |  Cisco UCS Manager now supportsCisco UCS C220 M7 Server and Cisco UCS C240 M7 Server.  |  —  
Support Cisco UCS X-Series M6 and M7 servers |  Cisco UCS Manager now supports Cisco UCS X210c M6 Compute Node and Cisco UCS X210c M7 Compute Node.  Cisco UCS X-Series servers support Intelligent Fabric Modules (IFM), which function similarly to the Input/Output Module (IOM) in Cisco UCS B-Series servers.  |  —  
Support for Power Capping and Power Management for Cisco UCSX-9508 Chassis |  Cisco UCS Manager now supports Power Capping and Power Management for Cisco UCSX-9508 Chassis.  |  [Power Capping in Cisco UCS](m_cli_managing_power_in_cisco_ucs.html#concept_943D968485A04A92BAA307A2FC59AD18)  
Deprecated support for Cisco Cisco UCS M4 servers. |  Cisco UCS Manager support for Cisco UCS M4 servers are deprecated. |  —  
Deprecated support for Cisco UCS 6200 series Fabric Interconnect. |  Cisco UCS Manager support for Cisco UCS 6200 Series Fabric Interconnect is deprecated. |  —

---

## Page 4: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Server-Mgmt/4-3/b_cisco_ucs_manager_server_mgmt_cli_guide_4_3/m_server_management_overview-4_1.html

## Server Management Overview  
  
Cisco UCS Manager enables you to manage general and complex server deployments. For example, you can manage a general deployment with a pair of Fabric Interconnects (FIs), which is the redundant server access layer that you get with the first chassis that can scale up to 20 chassis' and up to 160 physical servers. This can be a combination of blades and rack mount servers to support the workload in your environment. As you add more servers, you can continue to perform server provisioning, device discovery, inventory, configuration, diagnostics, monitoring, fault detection, and auditing. 

Beginning with release 4.3(6a), Cisco UCS Manager introduces support for the following Cisco UCS hardware: 

  * Cisco UCS X210c M8 Compute Node

  * UCS C240 M8 Server

  * UCS C220 M8 Server


Beginning with release 4.3(5a), Cisco UCS Manager introduces support for the following Cisco UCS hardware: 

  * Cisco UCS X215c M8 Compute Node

  * Cisco UCS C225 M8 Server


Beginning with release 4.3(4b), Cisco UCS Manager introduces support for Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct). 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For more information, see [Cisco UCS Manager Fabric Interconnects](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Getting-Started/4-3/b_ucsm_getting_started_guide_4_3/m_overview.html#d3765e974a1635). 

* * *  
  
---|---  
  
Beginning with release 4.3(4b), Cisco UCS Manager introduces support for the following Cisco UCS hardware: 

  * Cisco UCS C245 M8 Server


Beginning with release 4.3(6c), Cisco UCS Manager introduces support for the following Cisco UCS hardware: 

  * Cisco UCS VIC 15230

  * Cisco UCS VIC 15427

  * Cisco UCS VIC 15237 mLOM


Beginning with release 4.3(2b), Cisco UCS Manager introduces support for the following Cisco UCS hardware: 

  * Cisco UCS X410c M7 Compute Node

  * Cisco UCS X210c M7 Compute Node

  * Cisco UCS X210c M6 Compute Node

  * Cisco UCS C240 M7 Server

  * Cisco UCS C220 M7 Server

  * Cisco UCS VIC 15235 (PCIe) (Secure Boot) 

  * Cisco UCS VIC 14425 (PCIe) (Secure Boot) 

  * Cisco UCS VIC 15231 (mLOM) (Non-Secure Boot) 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCS VIC 15231 is not supported with Cisco UCS VIC 15422 mezzanine adapter.

* * *  
  
---|---  
  * Cisco UCS VIC 15420 (mLOM) (Secure Boot) 

  * Cisco UCS VIC 15422 (mezz) (Secure Boot) 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCS VIC 15422 is a mezzanine adapter that requires UCS VIC 15000 bridge connector (UCSX-V5-BRIDGE) and VIC 15420 mLOM on X210c M6 and X210c M7 compute node. 

* * *  
  
---|---  
  * Cisco UCS VIC 14425 (mLOM) 

  * Cisco UCS VIC 14825 (mezz) 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCS VIC 14825 is a mezzanine adapter that requires UCS 14000 bridge connector (UCSX-V4-BRIDGE) and VIC 14425 mLOM on X210c M6 compute node. 

* * *  
  
---|---  

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

  * Before inserting Cisco UCS VIC 15235 and VIC 15425 adapters into a server, upgrade the server with UCS 4.3(2a) or later release C-bundle software. If these adapters are inserted into the server which is running lower than 4.3(2a) release, upgrade the server to UCS 4.3(2a) or later release C-bundle software and then power cycle the server to recognize the adapters. 
  * Cisco UCS VIC 15000 series and Cisco UCS VIC 14000 series adapters or Cisco UCS 15000 series and Cisco UCS VIC 1400 series adapters cannot be installed together on Cisco UCS B-Series servers. 
  * Cisco UCS VIC 1400 series adapters are not supported on Cisco UCS M7 servers.


* * *  
  
---|---  
  
Beginning with release 4.2(3b), Cisco UCS Manager introduces support for the following Cisco UCS hardware: 

  * Cisco UCS VIC 15411 (mLOM) (Non-Secure Boot) 

  * Cisco UCS VIC 15238 (mLOM) (Non-Secure Boot) 

  * Cisco UCS 6536 Fabric Interconnect


Beginning with release 4.2(2a), Cisco UCS Manager introduces support for the following Cisco UCS hardware: 

  * Cisco UCS VIC 15428 (mLOM) (Non-Secure Boot) 


Beginning with release 4.2(1), Cisco UCS Manager introduces support for the following Cisco UCS hardware: 

  * Cisco UCS C220 M6 Server

  * Cisco UCS C240 M6 Server

  * Cisco UCS C225 M6 Server

  * Cisco UCS C245 M6 Server

  * Cisco UCS B200 M6 Server

  * Cisco UCS VIC 1467 (mLOM)

  * Cisco UCS VIC 1477 (mLOM)


The Cisco UCS 6536 Fabric Interconnect,  Cisco UCS 6400 Series Fabric Interconnect, and Cisco UCS 6332 Fabric Interconnects include centralized management. You can manage the UCS Blade Servers and Rack-Mount Servers that are in the same domain from one console. You can also manage the UCS Mini from the Cisco UCS Manager. 

To ensure the optimum server performance, you can configure the amount of power that you allocate to servers. You can also set the server boot policy, the location from which the server boots, and the order in which the boot devices are invoked. You can create service profiles and assign the service profiles to servers. In service profile, you can configure vNICs and vHBAs, enables BIOS settings, apply firmware policy, and other settings. When the service profile is associated to a server, the configured configurations, policies, and settings are pushed to the server. 

---

## Page 5: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Server-Mgmt/4-3/b_cisco_ucs_manager_server_mgmt_cli_guide_4_3/m_cli_managing_licenses.html

## Licenses

Cisco UCS Fabric Interconnect are equipped with pre-installed port licenses, providing the option to purchase them fully licensed, partially licensed, or add licenses after delivery. The licensing model varies across different Fabric Interconnect series, with some models adopting perpetual software licenses to simplify license management. 

**Perpetual Licensing for Cisco UCS 6500 Seriesand Cisco UCS X-Series Direct Fabric Interconnects**

Cisco UCS 6536 Fabric Interconnect (UCS-FI-6536): Starting with release 4.2(3b), all ports and software features are activated through a perpetual software license. No additional license management is required. 

**Cisco UCS 9108 100G Fabric Interconnect (X-Series Direct)** : Starting with release 4.3(4b), all ports and software features are similarly activated through a perpetual software license. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct) and UCS-FI-6536 do not use port-based licensing like previous generations of fabric interconnects. 

* * *  
  
---|---  
  
Cisco UCS 64108 Fabric Interconnect uses the following licenses: 

Table 1. Cisco UCS 64108 Fabric Interconnect Licenses Ports |  Licenses  
---|---  
Ports 1-96 |  ETH_PORT_ACTIVATION_PKG and ETH_PORT_C_ACTIVATION_PKG - Licenses used for 10/25 GB Ethernet ports  
Ports 97-108 |  100G_ETH_PORT_ACTIVATION_PKG – Licenses used for 40/100 GB Ethernet ports   
  
Cisco UCS 6454 Fabric Interconnect uses the following licenses: 

Table 2. Cisco UCS 6454 Fabric Interconnect Licenses Ports |  Licenses  
---|---  
Ports 1-48 |  ETH_PORT_ACTIVATION_PKG and ETH_PORT_C_ACTIVATION_PKG - Licenses used for 10/25 GB Ethernet ports  
Ports 49-54 |  100G_ETH_PORT_ACTIVATION_PKG – Licenses used for 40/100 GB Ethernet ports   
  
The following four licenses are for the 6300 Series FI and are only valid on the 6332 and 6332-16UP FIs. 

  * 40G_ETH_PORT_ACTIVATION_PKG – Licenses used for 40 GB Ethernet ports 

  * 40G_ETH_C_PORT_ACTIVATION_PKG – Licenses used for 40 GB Ethernet ports directly connected to rack servers (C-Direct) 

  * 10G_C_PORT_ACTIVATION_PKG – Licenses used for the first 16 10 GB unified ports on the 6332-16UP that are directly connected to rack servers (C-Direct) 

  * 10G_PORT_ACTIVATION_PKG – Licenses used for the first 16 10 GB unified ports on the 6332-16UP 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The 10G_PORT_ACTIVATION_PKG and 10G_C_PORT_ACTIVATION_PKG licenses are only valid for the 6332-16UP FIs, and can only be installed on them. 

* * *  
  
---|---  


The following licenses are used when S3260 system is connected to FI as appliance (appliance port) or Cisco UCS Manager managed node (server port): 

Table 3. S3260 system License Requirement FI Model |  License  
---|---  
Cisco UCS 6536  |  Perpetual software license.  
6454 and 64108 |  10G_PORT_ACTIVATION_PKG  
6332-16UP |  10G_PORT_ACTIVATION_PKG  
6332 |  10G_PORT_ACTIVATION_PKG  
  
Cisco UCS C125 M5 Servers support Cisco UCS 6500 Series Fabric Interconnect, Cisco UCS 6400 Series Fabric Interconnect and 6300 Series Fabric Interconnect. 

Fabric Interconnect  |  Default Base Licenses   
---|---  
Cisco UCS 9108 100G Intelligent Fabric Module (Cisco UCS X-Series Direct)  |  Perpetual software license. This license activates all the ports and software features of Cisco UCS X-Series Direct.   
Cisco UCS 6536  |  Perpetual software license. This license activates all the ports and software features of 6536 Fabric Interconnect.  
Cisco UCS 64108  |  For 36 10/25 GB ports (ports 1-96) For 4 40/100 GB ports (ports 97-108).  
Cisco UCS 6454  |  For 18 10/25 GB ports (ports 1-48) For 2 40/100 GB ports (ports 49-54).  
Cisco UCS 6332  |  For eight 40 GB ports.   
Cisco UCS 6332 16UP  |  For four 40 GB ports and eight 10 GB ports.  |  **Note** |  The first 16 ports are 10 GB. The remaining are 40 GB.   
---|---  
Cisco UCS 6324  |  For 4 non-breakout ports only. The fifth port, which does not include a license, is further broken in to four 10 GB ports.   
Port License Consumption

Port licenses are not bound to physical ports. When you disable a licensed port, that license is retained for use with the next enabled port. To use additional fixed ports, you must purchase and install licenses for those ports. All ports, regardless of their type (fibre, ethernet) consume licenses if they are enabled. 

For breakout capable ports available in the 6332 and the 6332-16UP platforms, 40 GB licenses remain applied to the main port even if that port is a breakout port, and that port continues to consume only one 40 GB license. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

Licenses are not portable across product generations. 

* * *  
  
---|---  
  
Each Cisco UCS 6324 Fabric Interconnect comes with a factory installed port license that is shipped with the hardware. The C-direct port license is factory installed with a grace period, measured from first use of the port, and can be used for Cisco UCS rack servers. If multiple ports are acting within grace periods, the license is moved to the port whose grace period is closest to expiring. 

### Grace Period

If you attempt to use a port that does not have an installed license, Cisco UCS initiates a 120 day grace period. The grace period is measured from the first use of the port without a license and is paused when a valid license file is installed. The amount of time used in the grace period is retained by the system. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Each physical port has its own grace period. Initiating the grace period on a single port does not initiate the grace period for all ports. 

* * *  
  
---|---  
  
If a licensed port is unconfigured, that license is transferred to a port functioning within a grace period. If multiple ports are acting within grace periods, the license is moved to the port whose grace period is closest to expiring. 

### High Availability Configurations

To avoid inconsistencies during failover, we recommend that both Fabric Interconnects in the cluster have the same number of ports licensed. If symmetry is not maintained and failover occurs, Cisco UCS enables the missing licenses and initiates the grace period for each port being used on the failover node. 

---

## Page 6: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Server-Mgmt/4-3/b_cisco_ucs_manager_server_mgmt_cli_guide_4_3/m_cli_registering_ucs_domains_with_ucsc.html

## Registration of Cisco UCS Domains 

You can have Cisco UCS Central manage some or all of the Cisco UCS domains in your data center. 

If you want Cisco UCS Central to manage a Cisco UCS domain, you need to register that domain. When you register, you must choose which types of policies and other configurations will be managed by Cisco UCS Central and Cisco UCS Manager. Cisco UCS Central can manage the same types of policies and configurations for all registered Cisco UCS domains. You can also choose to have different settings for each registered Cisco UCS domain. 

Perform the following before registering a Cisco UCS domain with Cisco UCS Central: 

  * Configure an NTP server and the correct time zone in both Cisco UCS Manager and Cisco UCS Central to ensure that they are in sync. If the time and date in the Cisco UCS domain and Cisco UCS Central are out of sync, the registration might fail. 

  * Obtain the hostname or IP address of Cisco UCS Central

  * Obtain the shared secret that was configured when Cisco UCS Central was deployed. 


---

## Page 7: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Server-Mgmt/4-3/b_cisco_ucs_manager_server_mgmt_cli_guide_4_3/m_cli_managing_power_in_cisco_ucs.html

## Power Capping in Cisco UCS

You can control the maximum power consumption on a server through power capping, as well as manage the power allocation in the Cisco UCS Manager for blade servers, rack servers, UCS Mini, and mixed UCS domains. 

Cisco UCS Manager supports power capping on the following: 

  * Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct) 

  * UCS 6500 Series Fabric Interconnects

  * UCS 6400 Series Fabric Interconnects

  * UCS 6300 Series Fabric Interconnects 

  * UCS 6324 Series Fabric Interconnects (Cisco UCS Mini)


You can use Policy Driven Chassis Group Power Cap, or Manual Blade Level Power Cap methods to allocate power that applies to all of the servers in a chassis. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCSX-9508 Chassis supports Policy Driven Chassis Group Cap.  When you choose to select Policy Driven Chassis Group Cap, Cisco UCS Manager calculates the power allotment for Cisco UCSX-9508 Chassis and when you choose to select Manual Blade Level Power Cap, Chassis Management Controller (CMC) calculates the power allotment for Cisco UCSX-9508 Chassis. 

* * *  
  
---|---  
  
Cisco UCS Manager provides the following power management policies to help you allocate power to your servers: 

Power Management Policies  |  Description   
---|---  
Power Policy |  Specifies the redundancy for power supplies in all chassis in a Cisco UCS domain.   
Power Control Policies |  Specifies the priority to calculate the initial power allocation for each blade in a chassis.   
Power Save Policy |  Globally manages the chassis to maximize energy efficiency or availability.  
Cisco UCSX-9508 Chassis Power Extended Policy |  Manages the chassis to maximize energy efficiency or availability.  Power Extended Policy is effective only when we have PSU Redundant Policy Mode. For example, the total power available can be extended when we have N+1, N+2 and Grid to PSU Redundancy modes.   
Cisco UCSX-9508 Chassis Fan Control Policy |  Manages you to control the fan speed to bring down server power consumption and noise levels.  
Global Power Allocation |  Specifies the Policy Driven Chassis Group Power Cap or the Manual Blade Level Power Cap to apply to all servers in a chassis.   
Global Power Profiling  |  Specifies how the power cap values of the servers are calculated. If it is enabled, the servers will be profiled during discovery through benchmarking. This policy applies when the Global Power Allocation Policy is set to Policy Driven Chassis Group Cap. 

---

## Page 8: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Server-Mgmt/4-3/b_cisco_ucs_manager_server_mgmt_cli_guide_4_3/m_cli_managing_blade_servers.html

## Blade Server Management   
  
You can manage and monitor all blade servers in a Cisco UCS domain through Cisco UCS Manager. You can perform some blade server management tasks, such as changes to the power state, from the server and service profile. 

The remaining management tasks can only be performed on the server. 

The power supply units go into power save mode when a chassis has two blades or less. When a third blade is added to the chassis and is fully discovered, the power supply units return to regular mode. 

If a blade server slot in a chassis is empty, Cisco UCS Manager provides information, errors, and faults for that slot. You can also re-acknowledge the slot to resolve server mismatch errors and to have Cisco UCS Manager rediscover the blade server in the slot. 

---

## Page 9: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Server-Mgmt/4-3/b_cisco_ucs_manager_server_mgmt_cli_guide_4_3/m_cli_managing_rack-mount_servers.html

## Rack-Mount Server Management 

You can manage and monitor all rack-mount servers that are integrated with a Cisco UCS domain through Cisco UCS Manager. All management and monitoring features are supported for rack-mount servers except power capping. Some rack-mount server management tasks, such as changes to the power state, can be performed from both the server and service profile. The remaining management tasks can only be performed on the server. 

Cisco UCS Manager provides information, errors, and faults for each rack-mount server that it has discovered. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/tip.gif)  
**Tip** | 

* * *

For information on how to integrate a supported Cisco UCS rack-mount server with Cisco UCS Manager, see the Cisco UCS C-series server integration guide or Cisco UCS S-series server integration guide for your Cisco UCS Manager release. 

* * *  
  
---|---

---

## Page 10: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Server-Mgmt/4-3/b_cisco_ucs_manager_server_mgmt_cli_guide_4_3/m_cli_3260_server_management.html

## Cisco UCS S3260 Server Node Management   
  
You can manage and monitor all Cisco UCS S3260 server nodes in a Cisco UCS domain through Cisco UCS Manager. You can perform some server management tasks, such as changes to the power state, from the server and service profile. 

The remaining management tasks can only be performed on the server. 

If a server slot in a chassis is empty, Cisco UCS Manager provides information, errors, and faults for that slot. You can also re-acknowledge the slot to resolve server mismatch errors and rediscover the server in the slot. 

---

## Page 11: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Server-Mgmt/4-3/b_cisco_ucs_manager_server_mgmt_cli_guide_4_3/m_cli_configuring_server_boot.html

##  Boot Policy

The Cisco UCS Manager enables you to create a boot policy for blade servers and rack servers. 

The Cisco UCS Manager boot policy overrides the boot order in the BIOS setup menu and determines the following: 

  * Selection of the boot device 

  * Location from which the server boots 

  * Order in which boot devices are invoked 


For example, you can have associated servers boot from a local device, such as a local disk or CD-ROM (VMedia), or you can select a SAN boot or a LAN (PXE) boot. 

You can either create a named boot policy to associate with one or more service profiles, or create a boot policy for a specific service profile. A boot policy must be included in a service profile, and that service profile must be associated with a server for it to take effect. If you do not include a boot policy in a service profile, Cisco UCS Manager applies the default boot policy. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Changes to a boot policy might be propagated to all servers created with an updating service profile template that includes that boot policy. Re-association of the service profile with the server to rewrite the boot order information in the BIOS is automatically triggered.  You can also specify the following for the boot policy: 

  * Local LUN name. The name specified is the logical name in the storage profile, not the deployed name. Specify only a primary name. Specifying a secondary name results in a configuration error. 
  * Specific JBOD disk number for booting from JBOD disks. 
  * Any LUN for backward compatibility; however, we do not recommend this. Other devices must not have bootable images to ensure a successful boot. 


* * *  
  
---|---

---

## Page 12: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Server-Mgmt/4-3/b_cisco_ucs_manager_server_mgmt_cli_guide_4_3/m_cli_configuring_service_profiles.html

## Service Profiles in UCS Manager   
  
A service profile defines a single server and its storage and networking characteristics. You can create a service profile for Cisco UCS Manager and UCS Mini. When a service profile is deployed to a server, UCS Manager automatically configures the server, adapters, fabric extenders, and fabric interconnects to match the configuration specified in the service profile. 

A service profile includes four types of information: 

  * Server definition: Defines the resources (e.g. a specific server or a blade inserted to a specific chassis) that are required to apply to the profile. 

  * Identity information: Includes the UUID, MAC address for each virtual NIC (vNIC), and WWN specifications for each HBA. 

  * Firmware revision specifications: Used when a certain tested firmware revision is required to be installed or for some other reason a specific firmware is used. 

  * Connectivity definition: Configures network adapters, fabric extenders, and parent interconnects, however this information is abstract as it does not include the details of how each network component is configured. 


The UCS system provides two types of service profiles: Service profiles that inherit server identity and service profiles that override server identity. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

A server can also show a Server Personality field in server properties. This field displays the server personality configuration of Hyperconverged Infrastructure (HCI). Cisco UCS M6 servers and later versions can function as either as a standard UCS servers or HCI servers.  The server personality field is informational cannot be reset in the UCS Manager GUI, indicating the specific configuration or role assigned to the server, and is only visible if a server personality is configured.  The UCS Manager CLI provides a command line option to revert the server back to a "no personality" state. For more information, see _Clearing the Server Personality Field_ section in [Cisco UCS Manager Server Management Using the CLI](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) guide. 

* * *  
  
---|---

---

## Page 13: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Server-Mgmt/4-3/b_cisco_ucs_manager_server_mgmt_cli_guide_4_3/m_cli_configuring_server-related_policies1.html

## Server BIOS Settings   
  
Cisco UCS provides two methods for making global modifications to the BIOS settings on servers in an Cisco UCS domain. You can create one or more BIOS policies that include a specific grouping of BIOS settings that match the needs of a server or set of servers, or you can use the default BIOS settings for a specific server platform. 

Both the BIOS policy and the default BIOS settings for a server platform enable you to fine tune the BIOS settings for a server managed by Cisco UCS Manager. 

Depending upon the needs of the data center, you can configure BIOS policies for some service profiles and use the BIOS defaults in other service profiles in the same Cisco UCS domain, or you can use only one of them. You can also use Cisco UCS Manager to view the actual BIOS settings on a server and determine whether they are meeting current needs. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCS Manager pushes BIOS configuration changes through a BIOS policy or default BIOS settings to the Cisco Integrated Management Controller (CIMC) buffer. These changes remain in the buffer and do not take effect until the server is rebooted.  We recommend that you verify the support for BIOS settings in the server that you want to configure. Some settings, such as Mirroring Mode for RAS Memory, are not supported by all Cisco UCS servers. 

* * *  
  
---|---  
  
### Main BIOS Settings 

The following table lists the main server BIOS settings that you can configure through a BIOS policy or the default BIOS settings: 

Name  | Description   
---|---  
Properties  
Reboot on BIOS Settings Change set reboot-on-update |  When the server is rebooted after you change one or more BIOS settings.  yes —If you enable this setting, the server is rebooted according to the maintenance policy in the server's service profile. For example, if the maintenance policy requires user acknowledgment, the server is not rebooted and the BIOS changes are not applied until a user acknowledges the pending activity.  no —If you do not enable this setting, the BIOS changes are not applied until the next time the server is rebooted, whether as a result of another server configuration change or a manual reboot.   
BIOS Setting  
Quiet Boot set quiet-boot-config quiet-boot |  What the BIOS displays during Power On Self-Test (POST). This can be one of the following: 

  * disabled—The BIOS displays all messages and Option ROM information during boot. 
  * enabled—The BIOS displays the logo screen, but does not display any messages or Option ROM information during boot. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
POST error pause set post-error-pause-config post-error-pause |  What happens when the server encounters a critical error during POST. This can be one of the following: 

  * disabled—The BIOS continues to attempt to boot the server. 
  * enabled—The BIOS pauses the attempt to boot the server and opens the Error Manager when a critical error occurs during POST. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Resume on AC power loss set resume-ac-on-power-loss-config resume-action |  How the server behaves when power is restored after an unexpected power loss. This can be one of the following: 

  * stay-off—The server remains off until manually powered on. 
  * last-state—The server is powered on and the system attempts to restore its last state. 
  * reset—The server is powered on and automatically reset. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Front panel lockout set front-panel-lockout-config front-panel-lockout |  Whether the power and reset buttons on the front panel are ignored by the server. This can be one of the following: 

  * disabled—The power and reset buttons on the front panel are active and can be used to affect the server. 
  * enabled—The power and reset buttons are locked out. The server can only be reset or powered on or off from the CIMC GUI. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
CDN Control  set consistent-device-name-control cdn-name |  Consistent Device Naming allows Ethernet interfaces to be named in a consistent manner. This makes Ethernet interface names more uniform, easy to identify, and persistent when adapter or other configuration changes are made.  Whether consistent device naming is enabled or not. This can be one of the following: 

  * disabled—Consistent device naming is disabled for the BIOS policy. 
  * enabled—Consistent device naming is enabled for the BIOS policy. This enables Ethernet interfaces to be named consistently. This is the default option. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
PCIe Slots CDN Control  set consistent-device-name-control pcie-slot-cdn-name |  PCIe Slots Consistent Device Naming (CDN) control allows PCIe slots to be named in a consistent manner. This makes PCIe slot names more uniform, easy to identify, and persistent when the configuration changes are made. This can be one of the following: 

  * disabled—Consistent device naming is disabled. This is the default option. 
  * enabled—Consistent device naming is enabled. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
  
### Processor BIOS Settings 

The following table lists the processor BIOS settings that you can configure through a BIOS policy or the default BIOS settings: 

Name  | Description   
---|---  
DFX OSB Configuration set DfxOsbEn |  Controls the Opportunistic Snoop Broadcast (OSB) feature. OSB is used by CHA to broadcast snoops under lightly loaded ring or Intel UPI link condition. It is used to reduce the latency due to the directory look up. This can be one of the following. 

  * enabled—The latency due to the directory look up is reduced. This is the default option. 
  * disabled—The latency due to the directory look up is not reduced. 
  * auto—Automatically controls the OSB feature. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
DLWM Support set CbsCmnGnbSMUDlwmSupport |  This value controls the Dynamic Link Width Management (DLWM) feature.  When the platform can support either an 8 lane or 16 lane xGMI operation, the dynamic adjustment feature provides power savings. This can be one of the following. 

  * enabled—Enables the DLWM feature. 
  * disabled—Disables the DLWM feature. 
  * auto—Automatically controls the DLWM feature. This is the default option. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
EDC Control Throttle set CbsCmnEdcControlThrottle |  Enables or disables the **EDC Shutdown Protection** which enhances the utilization tracking to avoid EDC shutdown responses to specific aggressive workloads. This can be one of the following. 

  * enabled—Enables the EDC Shutdown Protection. 
  * disabled—Disables the EDC Shutdown Protection. 
  * auto—This is the default option. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Local APIC Mode set CbsDbgCpuLApicMode |  Selects the APIC mode to be used. This can be one of the following.

  * Compatibility—Uses the compatibility option. 
  * XAPIC—Uses the standard xAPIC architecture. 
  * X2APIC—Uses the enhanced x2APIC architecture to support 32-bit addressability of processors. 
  * auto—Automatically uses the xAPIC architecture that is detected. This is the default option. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

|  **Note** |  For Local APIC Mode Bios token, Compatability values are not supported for the AMD EPYC 7XX2 series.   
---|---  
Memory Clock Speed 7xx3 (AMD 3rd Gen CPU)  set CbsCmnMemSpeedDdr47xx3 |  Allows the memory clock to be further reduced from the maximum platform limit. This can be one of the following:

  * auto—This is the default option. 
  * 400 MHz, 800 MHz, 933 MHz, 1067 MHz, 1200 MHz, 1333 MHz, 1467 MHz, 1600 MHz, 1633 MHz, 1667 MHz, 1700 MHz, 1767 MHz, 1800 MHz—The memory clock speed size. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Memory Clock Speed 7xx2 (AMD 2nd Gen CPU)  set CbsCmnMemSpeedDdr47xx2 |  Allows the memory clock to be further reduced from the maximum platform limit. This can be one of the following:

  * auto—This is the default option. 
  * 667 MHz, 800 MHz, 933 MHz, 1067 MHz, 1200 MHz, 1333 MHz, 1467 MHz, 1600 MHz—The memory clock speed size. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
xGMI Link Configuration set CbsDfDbgXgmiLinkCfg |  Configures the number of xGMI2 links that are used on a multi-socket system. This can be one of the following:

  * 2 xGMI Links
  * 3 xGMI Links
  * 4 xGMI Links
  * auto—Automatically configures the number of xGMI2 links. This is the default option. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Preferred IO 7xx3 (AMD 3rd Gen CPU)  set CbsCmnPreferredIO7xx3 |  Enables the feature for a preferred bus as a performance improvement. This can be one of the following:

  * auto—Automatically enables the preferred bus. This is the default option. 
  * Bus—Enables the preferred bus. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Preferred IO 7xx2 (AMD 2nd Gen CPU)  set CbsCmnPreferredIO7xx2 |  Enables the feature for a preferred bus as a performance improvement. This can be one of the following:

  * auto—This is the default option. 
  * Manual—Enables for a performance improvement. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Core Watchdog Timer Enable set CbsDbgCpuGenCpuWdt |  Enables or disables CPU watchdog timer. This can be one of the following:

  * enabled—Enables the CPU watchdog timer. 
  * disabled—Disables the CPU watchdog timer. 
  * auto—Automatically enables the CPU watchdog timer. This is the default option. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
IOAT Configuration set IOATConfigCpm |  Enables or disables the CPM (Content Processing Module) in IOAT (Intel® I/O Acceleration Technology) accelerators. This can be one of the following: 

  * enabled—Enables the CPM accelerators. This is the default option. 
  * disabled—Disables the CPM accelerators. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
PCIe Ten Bit Tag Support set CbsGnbDbgPcieTbtSupport |  Enables the PCIe ten bit tags for the supported devices. This can be one of the following: 

  * enabled—Enables the PCIe ten bit tags for the supported devices. 
  * disabled—Disables the PCIe ten bit tags for the supported devices. 
  * Auto—Automatically enables the PCIe ten bit tags for the supported devices. This is the default option. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
PRMRR Size set PrmrrSize |  Processor Reserved Memory Range Registers (PRMRR) is the size of the protected region in the systems DRAM. The maximum size of the PRMRR field in the BIOS configuration will match the amount of the SGX Enclave Capacity value for the Intel CPU being utilized.. This can be one of the following: 

  * invalid config—This is the default value. 
  * 128M, 256M, 512M, 1G, 2G, 4G, 8G, 16G, 32G, 64G, 128G, 256G, 512G —The size of the protected regions. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Intel Turbo Boost Tech set intel-turbo-boost-config turbo-boost |  Whether the processor uses Intel Turbo Boost Technology, which allows the processor to automatically increase its frequency if it is running below power, temperature, or voltage specifications. This can be one of the following: 

  * disabled—The processor does not increase its frequency automatically. 
  * enabled—The processor uses Turbo Boost Technology if required. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Enhanced Intel SpeedStep Tech set enhanced-intel-speedstep-config speed-step |  Whether the processor uses Enhanced Intel SpeedStep Technology, which allows the system to dynamically adjust processor voltage and core frequency. This technology can result in decreased average power consumption and decreased average heat production. This can be one of the following: 

  * disabled—The processor never dynamically adjusts its voltage or frequency. 
  * enabled—The processor utilizes Enhanced Intel SpeedStep Technology and enables all supported processor sleep states to further conserve power. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

We recommend that you contact your operating system vendor to make sure your operating system supports this feature.   
Intel HyperThreading Tech set hyper-threading-config hyper-threading |  Whether the processor uses Intel Hyper-Threading Technology, which allows multithreaded software applications to execute threads in parallel within each processor. This can be one of the following: 

  * disabled—The processor does not permit hyperthreading. 
  * enabled—The processor allows for the parallel execution of multiple threads. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

We recommend that you contact your operating system vendor to make sure the operating system supports this feature.   
Intel Speed Select set-IntelSpeedSelect |  Allows improved CPU performance by using Intel Speed Select technology to tune the CPU to run at one of three operating profiles, based on number of logical processor cores, frequency, and TDP thread setting, to improve performance over the basic Platform Default setting. These profiles correspond to High, Medium, and Low Core settings and can be one of the following: 

  * base—The processor uses Base. 
  * config1—The processor uses Config 1. 
  * config2—The processor uses Config 2. 
  * config3—The processor uses Config 3. 
  * config4—The processor uses Config 4.  |  **Note** |  The values config1 and config2 are not supported on Cisco UCS M6 and M7 servers.   
---|---  
**Note** |  For Cisco UCS M6 and Cisco UCS M7 servers, the values config 3 and config 4 (4th Gen Intel Xeon Scalable processors and 5th Gen Intel Xeon Scalable processors) are equivalent to the values config 1 and config 2 (3rd Gen Intel Xeon Scalable processors).   
---|---  
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 


  
Core Multi Processing set core-multi-processing-config multi-processing |  Sets the state of logical processor cores per CPU in a package. If you disable this setting, Intel Hyper Threading technology is also disabled. This can be one of the following: 

  * All—Enables multiprocessing on all logical processor cores. 
  * 1 through n—Specifies the number of logical processor cores per CPU that can run on the server. To disable multiprocessing and have only one logical processor core per CPU running on the server, choose 1. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

We recommend that you contact your operating system vendor to make sure your operating system supports this feature.   
Execute Disable Bit set execute-disable bit |  Classifies memory areas on the server to specify where the application code can execute. As a result of this classification, the processor disables code execution if a malicious worm attempts to insert code in the buffer. This setting helps to prevent damage, worm propagation, and certain classes of malicious buffer overflow attacks. This can be one of the following: 

  * disabled—The processor does not classify memory areas. 
  * enabled—The processor classifies memory areas. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

We recommend that you contact your operating system vendor to make sure your operating system supports this feature.   
Intel Virtualization Technology set intel-vt-config vt |  Whether the processor uses Intel Virtualization Technology, which allows a platform to run multiple operating systems and applications in independent partitions. This can be one of the following: 

  * disabled—The processor does not permit virtualization. 
  * enabled—The processor allows multiple operating systems in independent partitions. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

|  **Note** |  If you change this option, you must power cycle the server before the setting takes effect.   
---|---  
Hardware Prefetcher set processor-prefetch-config hardware-prefetch |  Whether the processor allows the Intel hardware prefetcher to fetch streams of data and instruction from memory into the unified second-level cache when necessary. This can be one of the following: 

  * disabled—The hardware prefetcher is not used. 
  * enabled—The processor uses the hardware prefetcher when cache issues are detected. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

|  **Note** |  CPUPerformance must be set to Custom in order to specify this value. For any value other than Custom, this option is overridden by the setting in the selected CPU performance profile.   
---|---  
Adjacent Cache Line Prefetcher set processor-prefetch-config adjacent-cache-line-prefetch |  Whether the processor fetches cache lines in even/odd pairs instead of fetching just the required line. This can be one of the following: 

  * disabled—The processor only fetches the required line. 
  * enabled—The processor fetches both the required line and its paired line. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

|  **Note** |  must be set to Custom in order to specify this value. For any value other than Custom, this option is overridden by the setting in the selected CPU performance profile.   
---|---  
DCU Streamer Prefetch set processor-prefetch-config dcu-streamer-prefetch |  Whether the processor uses the DCU IP Prefetch mechanism to analyze historical cache access patterns and preload the most relevant lines in the L1 cache. This can be one of the following: 

  * disabled—The processor does not try to anticipate cache read requirements and only fetches explicitly requested lines. 
  * enabled—The DCU prefetcher analyzes the cache read pattern and prefetches the next line in the cache if it determines that it may be needed. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
DCU IP Prefetcher set processor-prefetch-config dcu-ip-prefetch |  Whether the processor uses the DCU IP Prefetch mechanism to analyze historical cache access patterns and preload the most relevant lines in the L1 cache. This can be one of the following: 

  * disabled—The processor does not preload any cache data. 
  * enabled—The DCU IP prefetcher preloads the L1 cache with the data it determines to be the most relevant. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
KTI Prefetch |  KTI prefetch is a mechanism to get the memory read started early on a DDR bus. This can be one of the following:

  * disabled—The processor does not preload any cache data. 
  * enabled—The KTI prefetcher preloads the L1 cache with the data it determines to be the most relevant. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
LLC Prefetch |  Whether the processor uses the LLC Prefetch mechanism to fetch the date into the LLC. This can be one of the following: 

  * disabled—The processor does not preload any cache data. 
  * enabled—The LLC prefetcher preloads the L1 cache with the data it determines to be the most relevant. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
XPT Prefetch |  Whether XPT prefetch is used to enable a read request that is sent to the last level cache to issue a copy of that request to the memory controller prefetcher. This can be one of the following: 

  * disabled—The CPU does not use the XPT Prefetch option. 
  * enabled—The CPU enables the XPT prefetcher option. 
  * auto—The CPU auto enables the XPT prefetcher option. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Direct Cache Access set direct-cache-access-config access |  Allows processors to increase I/O performance by placing data from I/O devices directly into the processor cache. This setting helps to reduce cache misses. This can be one of the following: 

  * auto—The CPU determines how to place data from I/O devices into the processor cache. 
  * disabled—Data from I/O devices is not placed directly into the processor cache. 
  * enabled—Data from I/O devices is placed directly into the processor cache. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Processor C State set processor-c-state-config c-state |  Whether the system can enter a power savings mode during idle periods. This can be one of the following: 

  * disabled—The system remains in a high-performance state even when idle. 
  * enabled—The system can reduce power to system components such as the DIMMs and CPUs. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

We recommend that you contact your operating system vendor to make sure your operating system supports this feature.   
Processor C1E set processor-c1e-config c1e |  Allows the processor to transition to its minimum frequency upon entering C1. This setting does not take effect until after you have rebooted the server. This can be one of the following: 

  * disabled—The CPU continues to run at its maximum frequency in the C1 state. 
  * enabled—The CPU transitions to its minimum frequency. This option saves the maximum amount of power in the C1 state. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Processor C3 Report set processor-c3-report-config processor-c3-report |  Whether the processor sends the C3 report to the operating system. This can be one of the following: 

  * enabled—The processor sends the C3 report to the OS. 
  * disabled—The processor does not send the C3 report. 
  * acpi-c2—The processor sends the C3 report using the advanced configuration and power interface (ACPI) C2 format. 
  * acpi-c3—The processor sends the C3 report using the ACPI C3 format. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

On the Cisco UCS B440 Server, the BIOS Setup menu uses enabled and disabled for these options. If you specify acpi-c2 or acpi-c2, the server sets the BIOS value for that option to enabled.   
Processor C6 Report set processor-c6-report-config processor-c6-report |  Whether the processor sends the C6 report to the operating system. This can be one of the following: 

  * disabled—The processor does not send the C6 report. 
  * enabled—The processor sends the C6 report. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Processor C7 Report set processor-c7-report-config processor-c7-report |  Whether the processor sends the C7 report to the operating system. This can be one of the following: 

  * c7—The processor sends the report using the C7 format. 
  * c7s—The processor sends the report using the C7s format. 
  * disabled—The processor does not send the C7 report. 
  * enabled—The processor sends the C7 report. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Processor CMCI |  Enables CMCI generation. This can be one of the following:

  * disabled—The processor disables CMCI. 
  * enabled—The processor enables CMCI. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
CPU Performance set cpu-performance-config cpu-performance |  Sets the CPU performance profile for the server. This can be one of the following: 

  * Custom—All performance profile options can be configured from the BIOS setup on the server. In addition, the Hardware Prefetcher and Adjacent Cache-Line Prefetch options can be configured as well. 
  * high-throughput—Data reuse and the DCU IP prefetcher are enabled, and all other prefetchers are disabled. 
  * hpc—All prefetchers are enabled and data reuse is disabled. This setting is also known as high-performance computing. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Max Variable MTRR Setting set max-variable-mtrr-setting-config  processor-mtrr |  Allows you to select the number of mean time to repair (MTRR) variables. This can be one of the following: 

  * auto-max—BIOS uses the default value for the processor. 
  * 8—BIOS uses the number specified for the variable MTRR. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Local X2 APIC set local-x2-apic-config localx2-apic |  Allows you to set the type of Application Policy Infrastructure Controller (APIC) architecture. This can be one of the following: 

  * disabled—Processor disables Local X2 APIC. 
  * enabled—Processor enables Local X2 APIC. 
  * xapic—Uses the standard xAPIC architecture. 
  * x2apic—Uses the enhanced x2APIC architecture to support 32 bit addressability of processors. 
  * auto—Automatically uses the xAPIC architecture that is detected. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Power Technology set processor-energy-config cpu-power-management |  Enables you to configure the CPU power management settings for the following options: 

  * Enhanced Intel Speedstep Technology 
  * Intel Turbo Boost Technology 
  * Processor Power State C6 

Power Technology can be one of the following: 

  * disabled—The server does not perform any CPU power management and any settings for the BIOS parameters mentioned above are ignored. 
  * Energy_Efficient—The server determines the best settings for the BIOS parameters mentioned above and ignores the individual settings for these parameters. 
  * performance—The server automatically optimizes the performance for the BIOS parameters mentioned above. 
  * custom—The server uses the individual settings for the BIOS parameters mentioned above. You must select this option if you want to change any of these BIOS parameters. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Energy Performance  set processor-energy-config energy-performance |  Allows you to determine whether system performance or energy efficiency is more important on this server. This can be one of the following: 

  * performance — The server provides all server components with full power at all times. This option maintains the highest level of performance and requires the greatest amount of power. 
  * balanced-performance — The server provides all server components with enough power to keep a balance between performance and power. 
  * balanced-energy — The server provides all server components with enough power to keep a balance between performance and power. 
  * energy-efficient — The server provides all server components with less power to keep reduce power consumption. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

|  **Note** |  CPUPowerManagement must be set to Custom or the server ignores the setting for this parameter.   
---|---  
Frequency Floor Override set frequency-floor-override-config cpu-frequency |  Whether the CPU is allowed to drop below the maximum non-turbo frequency when idle. This can be one of the following: 

  * disabled— The CPU can drop below the maximum non-turbo frequency when idle. This option decreases power consumption but may reduce system performance. 
  * enabled— The CPU cannot drop below the maximum non-turbo frequency when idle. This option improves system performance but may increase power consumption. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
P STATE Coordination set p-state-coordination-config p-state |  Allows you to define how BIOS communicates the P-state support model to the operating system. There are 3 models as defined by the Advanced Configuration and Power Interface (ACPI) specification. 

  * hw-all—The processor hardware is responsible for coordinating the P-state among logical processors with dependencies (all logical processors in a package). 
  * sw-all—The OS Power Manager (OSPM) is responsible for coordinating the P-state among logical processors with dependencies (all logical processors in a physical package), and must initiate the transition on all of the logical processors. 
  * sw-any—The OS Power Manager (OSPM) is responsible for coordinating the P-state among logical processors with dependencies (all logical processors in a package), and may initiate the transition on any of the logical processors in the domain. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

|  **Note** |  CPUPowerManagement must be set to Custom or the server ignores the setting for this parameter.   
---|---  
DRAM Clock Throttling set dram-clock-throttling-config dram-clock-throttling |  Allows you to tune the system settings between the memory bandwidth and power consumption. This can be one of the following: 

  * auto — CPU determines the DRAM Clock Throttling settings. 
  * balanced— DRAM clock throttling is reduced, providing a balance between performance and power. 
  * performance—DRAM clock throttling is disabled, providing increased memory bandwidth at the cost of additional power. 
  * Energy_Efficient—DRAM clock throttling is increased to improve energy efficiency. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Channel Interleaving set interleave-config channel-interleave |  Whether the CPU divides memory blocks and spreads contiguous portions of data across interleaved channels to enable simultaneous read operations. This can be one of the following: 

  * auto—The CPU determines what interleaving is done. 
  * 1-way— 
  * 2-way
  * 3-way
  * 4-way—The maximum amount of channel interleaving is used. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Rank Interleaving set interleave-config rank-interleave |  Whether the CPU interleaves physical ranks of memory so that one rank can be accessed while another is being refreshed. This can be one of the following: 

  * auto—The CPU determines what interleaving is done. 
  * 1-way— 
  * 2-way
  * 4-way
  * 8-way—The maximum amount of rank interleaving is used. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Sub NUMA Clustering |  This setting determines if the CPU supports sub NUMA clustering, which keeps the tag directory and memory channel in the same region to improve memory performance for certain workloads. This can be one of the following: 

  * auto—The BIOS determines the Sub-NUMA Clustering behavior automatically. 
  * disabled—Sub NUMA Clustering is turned off, and the CPU operates using a standard memory configuration without SNC optimization. This is the default option. 
  * enabled—Sub NUMA Clustering is activated, dividing the CPU into regions where the tag directory and memory channel remain in the same region for improved performance. 
  * snc 2—Sub NUMA Clustering divides the CPU into **two NUMA regions** , optimizing memory performance for workloads benefiting from moderate NUMA segmentation. 
  * snc 4—Sub NUMA Clustering divides the CPU into **four NUMA regions** , optimizing memory performance for workloads benefiting from moderate NUMA segmentation. 
  * platform-default— The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

|  **Note** |  The values SNC 2 and SNC 4 are not supported on Cisco UCS C220 M8, C240 M8, X210c M8 servers.  
---|---  
Memory Interleaving set interleave-config memory-interleave |  Whether the CPU interleaves the physical memory so that the memory can be accessed while another is being refreshed. This controls fabric level memory interleaving. Channel, die and socket have requirements based on memory populations and will be ignored if the memory does not support the selected option. This can be one of the following: 

  * none
  * channel
  * **die**
  * socket
  * auto—This is the default option. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Demand Scrub set scrub-policies-config demand-scrub |  Whether the system corrects single bit memory errors encountered when the CPU or I/O makes a demand read. This can be one of the following: 

  * disabled— Single bit memory errors are not corrected. 
  * enabled— Single bit memory errors are corrected in memory and the corrected data is set in response to the demand read. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Patrol Scrub set scrub-policies-config patrol-scrub |  Whether the system actively searches for, and corrects, single bit memory errors even in unused portions of the memory on the server. This can be one of the following: 

  * disabled—The system checks for memory ECC errors only when the CPU reads or writes a memory address. 
  * enabled—The system periodically reads and writes memory searching for ECC errors. If any errors are found, the system attempts to fix them. This option may correct single bit errors before they become multi-bit errors, but it may adversely affect performance when the patrol scrub is running. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
DCPMM Firmware Downgrade |  This can be one of the following: 

  * disabled—Support is disabled. 
  * enabled—Support is enabled. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Configurable TDP Control |  Allows you to set customized value for Thermal Design Power (TDP). This can be one of the following: 

  * auto— Uses the rated TDP value of the processor. 
  * manual—Allows you to customize the TDP value. 

  
Altitude set altitude altitude-config |  The approximate number of meters above sea level at which the physical server is installed. This can be one of the following: 

  * auto—The CPU determines the physical elevation. 
  * 300-m—The server is approximately 300 meters above sea level. 
  * 900-m—The server is approximately 900 meters above sea level. 
  * 1500-m—The server is approximately 1500 meters above sea level. 
  * 3000-m—The server is approximately 3000 meters above sea level. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Package C State Limit set package-c-state-limit-config package-c-state-limit |  The amount of power available to the server components when they are idle. This can be one of the following:  |  **Note** |  If you are changing the Package C State Limit token from any other value to no-limit, then ensure that the Power Technology is set to custom.   
---|---  
CPU Hardware Power Management set cpu-hardware-power-management-config cpu-hardware-power-management |  Enables processor Hardware Power Management (HWPM). This can be one of the following: 

  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 
  * disabled—HWPM is disabled. 
  * hwpm-native-mode—HWPM native mode is enabled. 
  * hwpm-oob-mode—HWPM Out-Of-Box mode is enabled. 
  * Native Mode with no Legacy (only GUI) 

  
Energy Performance Tuning set power-performance-tuning-support power-performance-tuning-config |  Determines if the BIOS or Operating System can turn on the energy performance bias tuning. The options are BIOS and OS.

  * bios— 
  * os— 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Workload Configuration |  This feature allows for workload optimization. The options are Balanced and I/O Sensitive:

  * balanced
  * io-sensitive—This is the default option. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

Cisco recommends using Balanced.   
Core Performance Boost set CbsCmnCpuCpb |  Whether the AMD processor increases its frequency on some cores when it is idle or not being used much. This can be one of the following: 

  * auto—The CPU automatically determines how to boost performance. This is the default option 
  * disabled—Core performance boost is disabled. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Uncore Frequency Scaling |  Allows you configure the scaling of the uncore frequency of the processor. This can be one of the following:

  * enabled—Uncore frequency of the processor scales up or down based on the load. (Default.) 
  * disabled—Uncore frequency of the processor remains fixed. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

Refer to the Intel Dear Customer Letter (DCL) to know the fixed higher and lower values for Uncore Frequency Scaling.  
Configurable TDP Level |  Allows adjustments in processor thermal design power (TDP) values. By modifying the processor behavior and the performance levels, power consumption of a processor can be configured and TDP can be adjusted at the same time. Hence, a processor operates at higher or lower performance levels, depending on the available cooling capacities and desired power consumption.  This can be one of the following:

  * normal—The CPU operates at its normal performance level. (Default.) 
  * level1
  * level1

|  **Note** |  Refer to the Intel Dear Customer Letter (DCL) for the values for TDP level.  
---|---  
UPI Link Speed set-qpilinkspeed |  Allows you to configure the Intel Ultra Path Interconnect (UPI) link speed between multiple sockets. This can be one of the following: 

  * auto—Automatically configures the optimal link speed. (Default) 
  * 9.6gt/s (gigatransfers per second)—Configures the optimal link speed at 9.6GT/s 
  * 10.4gt/s—Configures the optimal link speed at 10.4GT/s 
  * 11.2gt/s—Configures the optimal link speed at 11.2GT/s 
  * use per link setting |  **Note** |  The value use per link setting is not supported on UCS M6 and M7servers.   
---|---  

  
Global C-state Control set CbsCmnCpuGlobalCstateCtrl |  Whether the AMD processors control IO-based C-state generation and DF C-states. This can be one of the following:

  * auto—The CPU automatically determines how to control IO-based C-state generation. 
  * disabled—Global C-state control is disabled. This is the default option. 
  * enabled—Global C-state control is enabled. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
L1 Stream HW Prefetcher set CbsCmnCpuL1StreamHwPrefetcher |  Whether the processor allows the AMD hardware prefetcher to speculatively fetch streams of data and instruction from memory into the L1 cache when necessary. This can be one of the following: 

  * auto—The CPU determines how to place data from I/O devices into the processor cache. This is the default option. 
  * disabled—The hardware prefetcher is not used. 
  * enabled—The processor uses the hardware prefetcher when cache issues are detected. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
L2 Stream HW Prefetcher set CbsCmnCpuL2StreamHwPrefetcher |  Whether the processor allows the AMD hardware prefetcher to speculatively fetch streams of data and instruction from memory into the L2 cache when necessary. This can be one of the following: 

  * auto—The CPU determines how to place data from I/O devices into the processor cache. This is the default option. 
  * disabled—The hardware prefetcher is not used. 
  * enabled—The processor uses the hardware prefetcher when cache issues are detected. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
AMD Memory Interleaving Size |  Determines the size of the memory blocks to be interleaved. It also determines the starting address of the interleave (bit 8,9,10 or 11). This can be one of the following: 

  * 1 KB
  * 2 KB
  * 256 Bytes
  * 512 Bytes
  * auto—The CPU determines the size of the memory block. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Chipselect Interleaving set CbsCmnMemMapBankInterleaveDdr4 |  Whether memory blocks across the DRAM chip selects for node 0 are interleaved. This can be one of the following: 

  * auto—The CPU automatically determines how to interleave chip selects. This is the default option. 
  * disabled—Chip selects are not interleaved within the memory controller. 
  * enabled—Chip selects are interleaved within the memory controller. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Bank Group Swap set CbsCmnMemCtrlBankGroupSwapDdr44 |  Determines how physical addresses are assigned to applications. This can be one of the following: 

  * auto—The CPU automatically determines how to assign physical addresses to applications. This is the default option. 
  * disabled—Bank group swap is not used. 
  * enabled—Bank group swap is used to improve the performance of applications. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Determinism Slider set CbsCmnDeterminismSlider |  Allows AMD processors to determine how to operate. This can be one of the following: 

  * auto—The CPU automatically uses default power determinism settings. This is the default option. 
  * performance—Processor operates at the best performance in a consistent manner. 
  * power—Processor operates at the maximum allowable performance on a per die basis. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
IOMMU set CbsCmnGnbNbIOMMU |  Input Output Memory Management Unit (IOMMU) allows AMD processors to map virtual addresses to physical addresses. This can be one of the following: 

  * auto—The CPU determines how map these addresses. This is the default option. 
  * disabled—IOMMU is not used. 
  * enabled—Address mapping takes place through the IOMMU. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SVM Mode set SvmMode |  Whether the processor uses AMD Secure Virtual Machine Technology. This can be one of the following: This can be one of the following: 

  * disabled—The processor does not use SVM Technology. 
  * enabled—The processor uses SVM Technology. This is the default option. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SMT Mode |  Whether the processor uses AMD Simultaneous MultiThreading Technology, which allows multithreaded software applications to execute threads in parallel within each processor. This can be one of the following: 

  * disabled—The processor does not use SMT Technology. 
  * enabled—The processor uses SMT Technology. This is the default option. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SMEE |  Whether the processor uses the Secure Memory Encryption Enable (SMEE) function, which provides memory encryption support. This can be one of the following: 

  * auto—This is the default option. 
  * disabled—The processor does not use the SMEE function. 
  * enabled—The processor uses the SMEE function. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
UPI Prefetch set-upi-prefetch |  UPI prefetch is a mechanism to get the memory read started early on a DDR bus. This can be one of the following:

  * enabled—The UPI prefetcher preloads the L1 cache with the data it determines to be the most relevant. 
  * disabled—The processor does not preload any cache data. 
  * auto—The processor enables the UPI prefetcher option. 

  
SGX Auto MP Registration Agent set-SgxAutoRegistrationAgent |  Allows you to enable the registration authority service to store the platform keys. This can be one of the following: 

  * enabled—Support is enabled. 
  * disabled—Support is disabled. 

  
SProcessor Epoch n scope token-feature "Processor" scope token-param SgxEpoc nh |  Allows you to define the SGX EPOCH owner value for the EPOCH number designated by n.  
SGX Factory Reset  scope token-feature "Processor" scope token-param SgxFactoryReset |  Allows the system to perform SGX factory reset on subsequent boot. This deletes all registration data. This can be one of the following: 

  * enabled—Support is enabled. 
  * disabled—Support is disabled. 

  
SGX PBUKEY HASHn scope token-feature "Processor" scope token-param SgxLePubKeyHash n |  Allows you to set the Software Guard Extensions (SGX) value. This value can be set between:

  * SGX PUBKEY HASH0—Between 7-0
  * SGX PUBKEY HASH1—Between 15-8
  * SGX PUBKEY HASH2—Between 23-16
  * SGX PUBKEY HASH3—Between 31-24

  
SGX Write Enable scope token-feature "Processor" scope token-param SgxLeWr |  Allows you to enable SGX Write feature. This can be one of the following:

  * enabled—Support is enabled. 
  * disabled—Support is disabled. 

  
SGX Pkg info In-Band Access scope token-feature "Processor" scope token-param SgxPackageInfoInBandAccess |  Allows you to enable SGX Package Info In-Band Access. This can be one of the following:

  * enabled—Support is enabled. 
  * disabled—Support is disabled. 

  
SGX QoS scope token-feature "Processor" scope token-param SgxQoS |  Allows you to enable SGX QoS. This can be one of the following:

  * enabled— Support is enabled. 
  * disabled— Support is disabled. 

  
Intel Dynamic Speed Select scope token-feature "IntelSpeedSelect Configuration" scope token-param IntelDynamicSpeedSelect |  Intel Dynamic Speed Select modes allow you to run the CPU with different speed and cores in auto mode. This can be one of the following: 

  * enabled—Intel Dynamic Speed Select is enabled. 
  * disabled—Intel Dynamic Speed Select is disabled. 

  
IIO eDPC Support scope token-feature "Processor" scope token-param EdpcEn |  The eDPC (Enhanced Downstream Port Containment) allows a downstream link to be disabled after an uncorrectable error, enabling recovery possible in a controlled and robust manner. This can be one of the following: 

  * disabled—eDPC support is turned off, and the system does not take any action to disable downstream links in response to errors. 
  * on fatal errors—eDPC is enabled only for fatal errors.  |  **Note** |  This value on fatal errors is not supported on Cisco UCS C225 M8, Cisco UCS C245 M8, and X215c M8 servers.   
---|---  
  * on fatal and non-fatal errors—eDPC is enabled for both fatal and non-fatal errors. 


  
Multikey Total Memory Encryption (MK-TME) scope token-feature "Processor" scope token-param EnableMktme |  MK-TME allows you to have multiple encryption domains with one with own key. Different memory pages can be encrypted with different keys. This can be one of the following: 

  * enabled—Support is enabled. This is the default option. 
  * disabled—Support is disabled. 

  
SW Guard Extensions (SGX) scope token-feature "Processor" scope token-param EnableSgx |  Allows you to enable Software Guard Extensions (SGX) feature. This can be one of the following:

  * enabled—Support is enabled. 
  * disabled—Support is disabled. 

  
Total Memory Encryption (TME) scope token-feature "Processor" scope token-param EnableTme |  Allows you to provide the capability to encrypt the entirety of the physical memory of a system. This can be one of the following: 

  * enabled—Support is enabled. This is the default option. 
  * disabled—Support is disabled. 

  
Select Owner EPOCH input type scope token-feature "Processor" scope token-param EpochUpdate |  Allows you to change the seed for the security key used for the locked memory region that is created. This can be one of the following: 

  * sgx owner epoch activated— Does not change the current input type. 
  * change to new random owner epochs—Changes EPOCH to a system generated random number 
  * manual user defined owner epochs—Changes the EPOCH seed to a hexadecimal value that you enter. 

  
Enhanced CPU Performance scope token-feature "CpuPerfEnhancement" scope token-param CpuPerfEnhancement |  Enhances CPU performance by adjusting server settings automatically. This can be one of the following:

  * disabled—The processor does not run with this functionality. This is the default option. 
  * auto—Allows to adjust server settings to increase the processor performance. 

|  **Note** | 

  * Enabling this functionality may increase power consumption.
  * The server should meet the following requirements in order to use this functionality:
  * The server should not contain Barlow Pass DIMMs.
  * DIMM module size present in the Cisco UCS C220 M6 server should be less than 64GB and in Cisco UCS C240 M6 server should be less than 256GB. 
  * No GPU cards are present in the server. 

  
---|---  
UPI Link Enablement scope token-feature "UPI Link Enablement" scope token-param UPILinkEnablement |  Enables the number of Ultra Path Interconnect (UPI) links required by the processor. This can be one of the following

  * auto—This is the default option. 
  * 1
  * 2

  
UPI Power Manangement scope token-feature "UPI Power Manangement" scope token-param UPIPowerManagement |  The UPI power management can be used for conserving power on the server. This can be one of the following:

  * enabled—Enables the processor to support this functionality. 
  * disabled—Disables the processor to support this functionality. This is the default option. 

  
C1 Auto UnDemotion scope token-feature "C1 Auto UnDemotion" scope token-param C1AutoDemotion |  Select whether to enable processors to automatically undemote from C1. This can be one of the following:

  * auto— This is the default option. 
  * enabled—Enables the processor to support this functionality. 
  * disabled—Disables the processor to support this functionality. 

  
C1 Auto Demotion scope token-feature "C1 Auto Demotion" scope token-param C1AutoDemotion |  If enabled, CPU automatically demotes to C1 based on un-core auto-demote information. This can be one of the following:

  * auto— This is the default option. 
  * enabled—Enables the processor to support this functionality. 
  * disabled—Disables the processor to support this functionality. 

  
CPU Downcore control 7xx3 scope token-feature "Processor" scope token-param CbsCpuCoreCtrl |  Provides the ability to remove one or more cores from operation is supported in the silicon. It may be desirable to reduce the number of cores due to OS restrictions, or power reduction requirements of the system. This item allows the control on the number of cores that are running. This setting can only reduce the number of cores from only those available in the processor. This can be one of the following: 

  * auto—The CPU determines how many cores need to be enabled. This is the default option 
  * one (1+0)—One core enabled on one CPU complex 
  * two (2+0)—Two core enabled on one CPU complex 
  * three (3+0)—Three core enabled on one CPU complex. 
  * four (4+0)—Four core enabled on one CPU complex. 
  * five (5+0)—Five core enabled on one CPU complex 
  * six (6+0)—Six core enabled on one CPU complex 
  * seven (7+0)—Seven core enabled on one CPU complex 

|  **Note** |  This token is applicable only for the servers with 7xx3 Model processors.  
---|---  
Fixed SOC P-State scope token-feature "Processor" scope token-param CbsCmnFixedSocPstate |  This option defines the target P-state when APBDIS (to disable Algorithm Performance Boost (APB)) is set. The P-x specify a valid P-state for the processor installed. This can be one of the following: 

  * auto—Sets a valid P-state suitable for the processor. This is the default option. 
  * p0—Highest-performing SOC P-state 
  * p1—Next-highest-performing SOC P-state 
  * p2—Next-highest-performing SOC P-state 
  * p3—Minimum SOC power P-state 

  
APBDIS scope token-feature "Processor" scope token-param CbsCmnApbdis |  Allows you to select the Algorithm Performance Boost (APB) Disable value for the SMU. This can be one of the following:

  * auto—Sets an auto ApbDis for the SMU. This is the default option. 
  * 0—Clear ApbDis to SMU 
  * 1—Set ApbDis to SMU 

  
CCD Control set CbsCpuCcdCtrlSsp |  Allows you to specify the number of charge-coupled device CCDs that are desired to be enable in the system. This can be one of the following: 

  * auto—The maximum CCDs provided by the processor is enabled. This is the default option. 
  * 2 ccds
  * 4 ccds
  * 6 ccds
  * 8 ccds
  * 10 ccds
  * 12 ccds
  * 14 ccds

  
Cisco xGMI Max Speed scope token-feature "Processor" scope token-param CiscoXgmiMaxSpeed |  This option enables 18 Gbps XGMI link speed. This can be one of the following:

  * disabled—The feature is disabled. This is the default option. 
  * enabled—The feature is enabled. 

  
ACPI SRAT L3 Cache As NUMA Domain scope token-feature "Processor" scope token-param CbsDfCmnAcpiSratL3Numa |  Creates a layer of virtual domains on top of the physical domains in which each CCX is declared to be in its on domain. This can be one of the following: 

  * auto—Set to auto mode. This is the default option. 
  * disabled—Use NPS settings for domain configuration. 
  * enabled—Each CCX is declared to be in its own domain. 

  
Streaming Stores Control scope token-feature "Processor" scope token-param CbsCmnCpuStreamingStoresCtrl |  Enables the streaming stores functionality. This can be one of the following:

  * auto—Set to auto mode. This is the default option. 
  * disabled—Feature is disabled. 
  * enabled—Feature is enabled. 

  
DF C-States scope token-feature "Processor" scope token-param CbsCmnGnbSMUDfCstates |  When long duration idleness is expected in a system, this control allows the system to transition into a DF Cstate which can set the system into an even lower power state. This can be one of the following: 

  * auto—Set to auto mode. This is the default option. 
  * disabled—This option is turned off, long period of idleness are not expected so no power savings would be achieved. 
  * enabled—This option is active, saving power when the system is idle. 

  
SEV-SNP Support set CbsSevSnpSupport |  Allows you to enable Secure Nested Paging feature. This can be one of the following:

  * disabled—The processor does not use the SEV-SNP function. 
  * enabled—The processor uses the SEV-SNP function. 
  * auto. This is the default option.

  
Efficiency Mode Enable scope token-feature "Processor" scope token-param CbsCmnEfficiencyModeEn |  Allows you to configure power consumption based on efficiency. This can be one of the following:

  * auto—The CPU automatically uses default settings. This is the default option. 
  * enabled—Efficiency mode is enabled. 

  
SNP Memory Coverage scope token-feature "Processor" scope token-param CbsDbgCpuSnpMemCover |  Allows you to configure SNP memory coverage. This can be one of the following:

  * auto—System decides the memory coverage. This is the default option. 
  * disabled—The processor does not use this function. 
  * enabled—This feature is enabled. 
  * custom—Custom size can be defined in SNP Memory Size to Cover. 

  
SNP Memory Size to Cover in MB scope token-feature "Processor" scope token-param CbsDbgCpuSnpMemSizeCover |  Allows you to configure SNP memory size.  The value can range from 0-1048576. The value 8192 is the default option.  
CPCC scope token-feature "Processor" scope token-param CbsCmnGnbSMUCPPC |  Allows you to configure Collaborative Processor Performance Control. This can be one of the following:

  * auto—The CPU automatically uses default CPPC settings. This is the default option. 
  * disabled—Feature is disabled. 
  * enabled—Collaborative Processor Performance is enabled. 

  
Downcore control 7xx2 scope token-feature "Processor" scope token-param CbsCmnCpuGenDowncoreCtrl |  The ability to remove one or more cores from operation is supported in the silicon. It may be desirable to reduce the number of cores due to OS restrictions, or power reduction requirements of the system. This item allows the control of how many cores are running. This setting can only reduce the number of cores from those available in the processor. This can be one of the following: 

  * auto—The CPU determines how many cores need to be enabled. This is the default option. 
  * two (1+1)—Two cores enabled on one CPU complex. 
  * four (2+2)—Four cores enabled on one CPU complex. 
  * six (3+3)—Six cores enabled on one CPU complex. 

  
Processor EPP Profile  set processor epp profile |  Allows you to determine whether system performance or energy efficiency is more important on this server. This can be one of the following: 

  * performance
  * balanced performance—This is the default option. 
  * balanced power
  * power

  
Autonomous Core C-state set processor autonomous core c-state |  Enables CPU Autonomous C-State, which converts the HALT instructions to the MWAIT instructions. This can be one of the following:

  * disabled—This is the default option. 
  * enabled

  
Energy Efficient Turbo set energy efficient turbo |  When energy efficient turbo is enabled, the optimal turbo frequency of the CPU turns dynamic based on CPU utilization. The power/performance bias setting also influences energy efficient turbo. This can be one of the following: 

  * disabled—This is the default option. 
  * enabled

  
Hardware P-States set hardware p-states |  Enables processor Hardware P-State. This can be one of the following:

  * disabled—HWPM is disabled. 
  * hwpm native modeHWPM Native Mode—HWPM native mode is enabled. This is the default option. 
  * hwpm oob modeHWPM OOB Mode—HWPM Out-of-Box mode is enabled. 
  * native mode with no legacyNative Mode with no Legacy

  
Energy/Performance Bias Config set energy/performance |  Allows you to determine whether system performance or energy efficiency is more important on this server. This can be one of the following: 

  * performance—The server provides all server components with full power at all times. This option maintains the highest level of performance and requires the greatest amount of power. 
  * balaced performanceBalanced Performance—The server provides all server components with enough power to keep a balance between performance and power. This is the default option. 
  * balaced powerBalanced Power—The server provides all server components with enough power to keep a balance between performance and power. 
  * powerPower—The server provides all server components with maximum power to keep reduce power consumption. 

  
Power Performance Tuning set power performance |  Determines if the BIOS or Operating System can turn on the energy performance bias tuning. The options are BIOS and OS. This can be one of the following: 

  * bios—Chooses BIOS for energy performance tuning. 
  * osOS—Chooses OS for energy performance tuning. This is the default option. 
  * peciPECI—Chooses PECI for energy performance tuning. 

  
Cores Enabled set cores enabled |  Allows you to disable one or more of the physical cores on the server. This can be one of the following:

  * all—Enables all physical cores. This also enables Hyper Threading on the associated logical processor cores. 
  * 1 through 481 through 48—Specifies the number of physical processor cores that can run on the server. Each physical core has an associated logical core. 

  
Hyper-Threading [All] set hyper-threading-all |  Whether the processor uses Intel Hyper-Threading Technology, which allows multithreaded software applications to execute threads in parallel within each processor. This can be one of the following: 

  * disabled—The processor does not permit hyperthreading. 
  * enabledEnabled—The processor allows for the parallel execution of multiple threads. 

  
SpeedStep (Pstates) set speedstep (pstates) |  Whether the processor uses Enhanced Intel SpeedStep Technology, which allows the system to dynamically adjust processor voltage and core frequency. This technology can result in decreased average power consumption and decreased average heat production. This can be one of the following: 

  * disabled—The processor never dynamically adjusts its voltage or frequency. 
  * enabledEnabled—The processor utilizes Enhanced Intel SpeedStep Technology and enables all supported processor sleep states to further conserve power. 

  
Boot Performance Mode set boot performance mode |  Allows the user to select the BIOS performance state that is set before the operating system handoff. This can be one of the following: 

  * max performance—Processor P-state ratio is maximum. 
  * max efficientMax Efficient—Processor P-state ratio is minimum. 
  * set by intel nmSet by Intel NM—Processor P-state ratio is set by Intel. 

  
EIST PSD Function set eist psd function |  EIST reduces the latency inherent with changing the voltage-frequency pair (P-state), thus allowing those transitions to occur more frequently. This allows for more granular, demand-based switching and can optimize the power-to-performance balance, based on the demands of the applications. This can be one of the following: 

  * hw all—The processor is coordinates the P-state among logical processors dependencies. The OS keeps the P-state request up to date on all logical processors. This is the default option. 
  * sw all—The OS Power Manager coordinates the P-state among logical processors with dependencies and initiates the transition on all of those Logical Processors. 

  
Turbo Mode set eist psd function |  Whether the processor uses Intel Turbo Boost Technology, which allows the processor to automatically increase its frequency if it is running below power, temperature, or voltage specifications. This can be one of the following: 

  * disabled—The processor does not increase its frequency automatically. 
  * enabled—The processor utilizes Turbo Boost Technology if required. This is the default option. 

  
Extended APIC set extended apic |  Allows you to enable or disable extended APIC support. This can be one of the following:

  * disabled—This is the default option. 
  * enabled. 

  
Memory Interleaving Size set memory interleaving |  Determines the size of the memory blocks to be interleaved. It also determines the starting address of the interleave (bit 8, 9 , 10 or 11). This can be one of the following: 

  * 1 KB
  * 2 KB
  * 4 KB
  * 256 Bytes
  * 512 Bytes
  * auto—The CPU determines the size of the memory block. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
UPI Link Frequency Select set upi link frequency select |  Allows you to enable or disable extended APIC support. This can be one of the following:

  * auto—This option configures the optimal link speed automatically. This is the default option. 
  * 9.6gt/s—This option configures the optimal link speed at 9.6GT/s. 
  * 10.4gt/s—This option configures the optimal link speed at 10.4GT/s. 
  * 11.2gt/s—This option configures the optimal link speed at 10.4GT/s. 
  * 12.8gt/s—This option configures the optimal link speed at 12.8GT/s. 
  * 14.4gt/s—This option configures the optimal link speed at 14.4GT/s. 
  * 16.0gt/s—This option configures the optimal link speed at 16.0GT/s. 
  * 20.0gt/s—This option configures the optimal link speed at 20.0GT/s. 

  
X2APIC Opt Out set X2ApicOptOut |  Prevents the OS from enabling extended xAPIC (x2APIC) mode when the OS is not working with x2APIC. This can be one of the following: 

  * disabled—Use the Extended xAPIC (x2APIC) mode. This is the default option. 
  * enabled—Opt out from Extended xAPIC (x2APIC) mode. 

  
Optimized Power Mode set OptimizedPowerMode |  Automatically varies processor speed and _power_ usage based on processor utilization. This can be one of the following: 

  * disabled—The processor does not vary the speed automatically. 
  * enabled—The processor varies the speed automatically. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Burst and Postponed Refresh scope token-feature "Processor" scope token-param BurstAndPostponedRefresh |  Allows the memory controller to defer the refresh cycles when the memory is active and accomplishes the refresh within a specified window. The deferred refresh cycles may run in a burst of several refresh cycles. This can be one of the following: 

  * enabled
  * disabled—This is the default option.  |  **Note** |  It is recommended to leave this setting in the default state of disabled to mitigate Rowhammer-style attacks.   
---|---  

  
NUMA Nodes per Socket set CbsDfCmnDramNps |  Allows you to configure the memory NUMA domains per socket. This can be one of the following:

  * auto—Number of channels is set to auto. This is the default option. 
  * nps0—Zero NUMA node per socket. 
  * nps1—One NUMA node per socket. 
  * nps2—Two NUMA nodes per socket, one per Left/Right Half of the SoC. 
  * nps4—Four NUMA nodes per socket, one per Quadrant. 

  
DRAM SW Thermal Throttling scope token-feature "Processor" scope token-param DramSwThermalThrottling |  Provides a protective mechanism to ensure that the software functions within the temperature limits. When the temperature exceeds the maximum threshold value, the performance is permitted to drop allowing to cool down to the minimum threshold value. This can be one of the following: 

  * enabled
  * disabled—This is the default option.  |  **Note** |  It is recommended to leave this setting in the default state of disabled to mitigate Rowhammer-style attacks.   
---|---  

  
Operation Mode scope token-feature "operation mode" |  Allows you to set the Operation Mode. This can be one of the following:

  * test only—Support is enabled. 
  * test and repair—Support is disabled. 

  
Secure Encrypted Virtualization (SEV) scope token-feature "Processor" scope token-param SEV |  Enables running encrypted virtual machines (VMs) in which the code and data of the VM are isolated. This can be one of the following: 

  * 253 ASIDs
  * 509 ASIDs
  * auto—This is the default option.  |  **Note** |  It is recommended to leave this setting in the default state of auto to mitigate Rowhammer-style attacks.   
---|---  

  
Transparent Secure Memory Encryption (TSME) set tsme |  Provides transparent hardware memory encryption of all data stored on system memory. This can be one of the following:

  * enabled
  * disabled
  * auto—This is the default option.  |  **Note** |  It is recommended to leave this setting in the default state of auto to mitigate Rowhammer-style attacks.   
---|---  

  
AVX512 set CbsCmnCpuAvx512 |  The AVX-512 BIOS setting enables or disables the use of AVX-512 instruction set extensions, which are advanced vector extensions used by certain Intel® processors to improve performance for heavy computational tasks Adjusting this setting can affect compatibility and stability with some software, as well as influence CPU power consumption and heat output. This can be one of the following: 

  * enabled
  * disabled
  * auto—This is the default option. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SEV-ES ASID Space Limit |  The SEV-ES ASID Space Limit BIOS setting determines the number of ASIDs for AMD® SEV-ES, affecting VM memory encryption and isolation. Adjusting it balances security needs with system resources.  Enter an integer between 1 and 1007.  
Power Profile Selection F19h set CbsCmnEfficiencyModeEnRs |  The Power Profile Selection F19h BIOS setting allows users to choose a predefined power management profile tailored for specific performance or energy efficiency goals on AMD® Family 19h processors. This setting optimizes the CPU power consumption and performance characteristics based on the selected profile.  This can be one of the following:

  * high performance mode—Maximizes CPU performance without prioritizing power savings. This is the default option. 
  * efficiency mode—Prioritizes energy efficiency and lower power consumption over performance. 
  * maximum io performance mode—Prioritizes the input/output (IO) performance. 
  * balanced memory performance—Offers a compromise between performance and power efficiency. 
  * balanced core performance mode—Balances core performance with power efficiency. 
  * balanced core memory performance mode—Balances both core and memory performance with power efficiency. 
  * auto—Automatically balances performance and power efficiency.  |  **Note** |  The values such as balanced core performance mode, balanced core memory performance mode, and auto are applicable only for 5th Generation AMD® EPYC® 9xx5 processors.   
---|---  
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 


  
Power Down Enable |  This setting controls whether the memory (RAM) can enter a low power state when the system is idle or during periods of low usage. Enabling this setting typically allows the RAM to consume less power, potentially saving energy and reducing heat output, while disabling it keeps the RAM fully powered for possibly quicker wake-up times at the expense of higher power consumption. This can be one of the following: 

  * enabled
  * disabled
  * auto—This is the default option. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
xGMI Force Link Width |  This setting allows users to manually specify the number of lanes used for the xGMI (Inter-chip Global Memory Interconnect) link width to x4/x8/x16.  This can be one of the following:

  * 0 \- Force xGMI link width to x4. 
  * 1 \- Force xGMI link width to x8. 
  * 2 \- Force xGMI link width to x16. 
  * Auto \- Use the default xGMI link width controller settings. This is the default option. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
DF PState Frequency Optimizer set CbsCmnGnbSMUDffoRs |  Enable or Disable DF Pstate CCLK effective frequency optimizer.

  * enabled
  * disabled
  * auto—This is the default option. 

  
Fixed SOC P-State SP5 F19h set CbsCmnApbdisDfPstateRs |  Forced P-State to be independent/Dependent, as reported by the ACPI _PSD object. It will change SOC PState if APBDIS is enable. The valid range is (0-2).  
4-link xGMI max speed set CbsDfCmn4LinkMaxXgmiSpeed |  Specifies the max frequency used for XGMI PState in a 4-link topology.

  * 20Gbps
  * 25Gbps
  * 30Gbps
  * auto—This is the default option. 

  
CPU Downcore control F19 M10h-1Fh scope CbsCpuDownCoreCtrl scope CbsCpuDownCoreCtrlf19autom10h-1fh |  Enables manage the number of active cores on AMD® Family 19h processors. This token can be used to optimize performance, power consumption, or compatibility based on specific needs. F refers to the processor family and M refers to the model. The available options include: 

  * auto—The system automatically selects the optimal number of active cores based on the current workload and system configuration. This is the default option. 
  * one (1_+_0) — Enables only one core per CPU. 
  * two (2_+_0)—Enables two cores per CPU. 
  * three (3_+_0) —Enables three cores per CPU. 
  * four (4_+_0) —Enables four cores per CPU. 
  * five (5_+_0) —Enables five cores per CPU. 
  * six_(6_+_0) —Enables six cores per CPU. 
  * seven (7_+_0) —Enables seven cores per CPU. 
  * eight (8_+_0) —Enables eight cores per CPU. 
  * nine(9_+_0) —Enables nine cores per CPU. 
  * ten(10_+_0) —Enables ten cores per CPU. 
  * eleven (11_+_0) —Enables eleven cores per CPU. 
  * twelve (12_+_0) —Enables twelve cores per CPU. 
  * thirteen (13_+_0) —Enables thirteen cores per CPU. 
  * fourteen (14_+_0) —Enables fourteen cores per CPU. 
  * fifteen (15_+_0) —Enables fifteen cores per CPU. 

|  **Note** |  The values from _Eight (8_+_0)_ to _Fifteen (15_+_0)_ are applicable only for 5th Generation AMD® EPYC® 9xx5 processors.   
---|---  
Downcore control F19 MA0h-AFh scope CbsCpuDownCoreCtrl scope CbsCpuDownCoreCtrlf19maoh-afh |  F refers to the processor family and M denotes the model.

  * auto—This is the default option. 
  * two (1_+_1)
  * four (2_+_2) 
  * six (3_+_3) 
  * eight (4_+_4) 
  * ten (5_+_5) 
  * twelve (6_+_6) 
  * fourteen (7_+_7) 

  
Latency Optimized Mode Configuration set LatencyOptimizedMode |  This setting controls the Latency Optimized Mode, which is designed to minimize latency in processing tasks on supported platforms. This can be one of the following: 

  * disabled—Activates the Latency Optimized Mode, reducing latency for processing tasks. 
  * enabled—The mode is inactive, and latency reduction is not applied. 

  
  
###  I/O BIOS Settings for Intel

The following table lists the Intel Directed I/O BIOS settings that you can configure through a BIOS policy or the default BIOS settings: 

Name  | Description   
---|---  
Intel VT for directed IO set intel-vt-directed-io-config vtd |  Whether the processor uses Intel Virtualization Technology for Directed I/O (VT-d). This can be one of the following: 

  * disabled—The processor does not use virtualization technology. 
  * enabled—The processor uses virtualization technology. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

|  **Note** |  This option must be enabled if you want to change any of the other Intel Directed I/O BIOS settings.   
---|---  
Intel VTD interrupt Remapping set intel-vt-directed-io-config interrupt-remapping |  Whether the processor supports Intel VT-d Interrupt Remapping. This can be one of the following: 

  * disabled—The processor does not support remapping. 
  * enabled—The processor uses VT-d Interrupt Remapping as required. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Intel VTD coherency support set intel-vt-directed-io-config coherency-support |  Whether the processor supports Intel VT-d Coherency. This can be one of the following: 

  * disabled—The processor does not support coherency. 
  * enabled—The processor uses VT-d Coherency as required. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Intel VTD ATS support set intel-vt-directed-io-config ats-support |  Whether the processor supports Intel VT-d Address Translation Services (ATS). This can be one of the following: 

  * disabled—The processor does not support ATS. 
  * enabled—The processor uses VT-d ATS as required. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Intel VTD pass through DMA support set intel-vt-directed-io-config passthrough-dma |  Whether the processor supports Intel VT-d Pass-through DMA. This can be one of the following: 

  * disabled—The processor does not support pass-through DMA. 
  * enabled—The processor uses VT-d Pass-through DMA as required. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
  
### I/O BIOS Settings for AMD

The following table lists the Input/Output BIOS settings that you can configure through a BIOS policy for AMD: 

Name  | Description   
---|---  
PCIe ARI Support scope token-feature "PCIe ARI Support" scope token-param "PCIeARISupport" |  The PCIe Alternative Routing ID (ARI) Interpretation feature specification supports greater numbers of virtual funtions through the implementation of ARI, which reinterprets the device number field in the PCIe header allowing for more than eight functions. This can be one of the following: 

  * disabled—PCIe ARI Support is not available. 
  * enabled—PCIe ARI Support is available. 
  * auto—PCIe ARI Support is in auto mode. This is the default option. 

  
IPv4 PXE Support scope token-feature "IPv4 PXE Support" scope token-param "IPv4PXESupport" |  Enables or disables IPv4 support for PXE. This can be one of the following:

  * disabled—IPv4 PXE support is not available. 
  * enabled—IPv4 PXE support is available. This is the default option. 

  
IPv6 HTTP Support scope token-feature "HTTP BOOT" scope token-param "IPV6HTTP" |  Enables or disables IPv6 support for HTTP. This can be one of the following:

  * disabled—IPv6 HTTP support is not available. 
  * enabled—IPv6 HTTP support is available. This is the default option. 

  
Network Stack scope token-feature "Network Stack" scope token-param "NetworkStack" |  This option allows you to monitor IPv6 and IPv4. This can be one of the following

  * disabled—Network Stack support is not available.  |  **Note** |  When disabled, the value set for IPV4 PXE Support does not impact the system.   
---|---  
  * enabled—Network Stack support is available. This is the default option. 


**Note** |  When Network Stack token value is Disabled, the below tokens and their values are also set

  * IPV4PXE - Disabled
  * IPV4HTTP - Disabled
  * IPV6HTTP - Disabled

  
---|---  
SR-IOV Support scope token-feature "sriov" scope token-param "sriov-support" |  Whether SR-IOV (Single Root I/O Virtualization) is enabled or disabled on the server. This can be one of the following:

  * enabled—SR-IOV is enabled. This is the default option. 
  * disabled—SR-IOV is disabled. 

  
Re-size BAR Support set ResizeBarSupport |  Allows to enable or disable re-sizable BAR support setup. This can be one of the following:

  * enabled—This is the default option. 
  * disabled

  
PreBoot DMA Protection Configuration drop-down list  set PreBootDMAProtection |  Controls the PreBoot Direct Memory Access (DMA) Protection feature. This feature is used for protecting the system from unauthorized DMA access during the pre-boot phase. This can be one of the following: 

  * enabled—The system is protected from unauthorized DMA access during pre-boot. 
  * disabled—The system is not protected from unauthorized DMA access during pre-boot. This is the default option. 

  
  
### RAS Memory BIOS Settings 

The following table lists the RAS memory BIOS settings that you can configure through a BIOS policy or the default BIOS settings: 

Name  | Description   
---|---  
ACPI SRAT Special Purpose Memory Flag set AcpiSratSpFlagEn |  This setting allows or disallows the ACPI SRAT special purpose memory flag to be set when the UEFI Memory Map special purpose flag is enabled. This can be one of the following: 

  * disabled
  * enabled—This is the default option. 

  
UEFI Memory Map Special Purpose Memory Flag set UefiMemMapSpFlagEn |  This setting determines the behavior of the UEFI memory map special knob, which impacts CXL cards under certain operating systems. This can be one of the following: 

  * disabled
  * enabled—This is the default option. 

  
DRAM Scrub Time set CbsDfCmnDramScrubTime |  The value that represents the number of hours to scrub the whole memory. This can be one of the following:

  * Disabled—Disables the number of hours to scrub the whole memory. 
  * 1 hour, 4 hours, 6 hours, 8 hours, 12 hours, 16 hours, 24 hours, 48 hours—The number of hours to scrub the whole memory.12 hours is the default option.
  * auto—Automatically scrubs the whole memory. 

  
MMIO High Granularity Size set MmiohSize |  The MMIO High Granularity Size. This can be one of the following:

  * 1G, 4G, 16G, 64G, 256G, 1024G—The MMIO high granularity size. 1024G is the default option. 

  
MMIO High Base set MmiohBase |  The MMIO high base. This can be one of the following:

  * 512G, 1T, 2T, 4T, 16T, 24T, 32T, 40T, 56T—The MMIO high base. 32T is the default option. 

  
Error Check Scrub set ErrorCheckScrub |  An error check and scrub (ECS) mode enables a memory device to perform error checking and correction (ECC) and count errors. This can be one of the following: 

  * disabled—Does not collect any errors. 
  * Enabled_without_Result_Collection —Collects the errors without giving the results. 
  * Enabled_with_Result_Collection —Collects the errors with the results. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Rank Margin Tool set EnableRMT |  This provides automated memory margin testing and is used to identify DDR margins at the rank level. This can be one of the following: 

  * disabled—Does not identify the margins at the rank level. 
  * enabled—Identifies the margins at the rank level. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Partial Cache Line Sparing scope token-feature "Partial Cache Line Sparing" scope token-param PartialCacheLineSparing |  Partial cache line sparing (PCLS) is an error-prevention mechanism in memory controllers. PCLS statically encodes the locations of the faulty nibbles of bits into a sparing directory along with the corresponding data content for replacement during memory accesses. This can be one of the following: 

  * disabled—Support is disabled. 
  * enabled—Support is enabled. 

  
UMA  scope token feature "UMA" scope token-param UmaBasedClustering |  Allows you to set UMA settings. This can be one of the following:

  * disable-all2-all
  * hemisphere-2-clusters

  
Memory Thermal Throttling Mode scope token-feature "Memory Thermal Throttling Mode" scope token-param MemoryThermalThrottling |  Provides a protective mechanism to ensure the memory temperature is within the limits. When the temperature exceeds the maximum threshold value, the memory access rate is reduced and Baseboard Management Controller (BMC) adjusts the fan to cool down the memory to avoid DIMM damage due to overheat. This can be one of the following: 

  * CLTT with PECI —Closed Loop Thermal Throttling (CLTT) with Platform Environment Control Interface (PECI). This is the default option. 
  * disabled. 

|  **Note** |  It is recommended to leave this setting in the default state of CLTT with PECI   
---|---  
Enhanced Memory Test scope token-feature "Advanced Memory Test" scope token-param AdvancedMemTest |  Enables enhanced memory tests during the system boot and increases the boot time based on the memory. This can be one of the following: 

  * auto—This is the default option.  |  **Note** |  It is recommended to leave this setting in the default state of auto.   
---|---  
  * enabled

  * disabled


**Note** | 

  * This BIOS token name modified from Advanced Memory Test to Enhanced Memory Test for M6 servers. 

  
---|---  
Memory Refresh Rate scope token-feature "Memory Refresh Rate" scope token-param MemoryRefreshRate |  Controls the refresh rate of the memory controller and might affect the memory performance and power depending on memory configuration and workload. This can be one of the following: 

  * 1x-refresh
  * 2x-refresh—1.9us. This is the default option.

  
Panic and High Watermark scope token-feature "Panic and High Watermark" scope token-param PanicHighWatermark |  Controls the delayed refresh capability of the memory controller. This can be one of the following:

  * High—The memory controller is allowed to postpone up to a maximum of eight refresh commands. The memory controller executes all the postponed refreshes within the refresh interval. For the ninth refresh command, the refresh priority becomes Panic and the memory controller pauses the normal memory transactions until all the postponed refresh commands are executed. 
  * Low—This is the default option. The memory controller is not allowed to postpone refresh commands.  |  **Note** |  It is recommended to leave this setting in the default state (Low) which will help to reduce susceptibility to Rowhammer-style attacks.   
---|---  

  
Memory RAS configuration set memory-ras-config ras-config |  How the memory reliability, availability, and serviceability (RAS) is configured for the server. This can be one of the following: 

  * maximum-performance—Optimizes the system performance and disables all the advanced RAS features. 
  * lockstep—If the DIMM pairs in the server have an identical type, size, and organization and are populated across the SMI channels, you can enable lockstep mode to minimize memory access latency and provide better performance. Lockstep is enabled by default for B440 servers. 
  * Mirror Mode 1LM—Mirror Mode 1LM will set the entire 1LM memory in the system to be mirrored, consequently reducing the memory capacity by half. This mode is used for UCS M5 and M6 and M7blade servers. 
  * Partial Mirror Mode 1LM—Partial Mirror Mode 1LM will set a part of the 1LM memory in the system to be mirrored, consequently reducing the memory capacity by half. This mode is used for UCS M5 and M6 and M7blade servers. 
  * sparing—System reliability is optimized by holding memory in reserve so that it can be used in case other DIMMs fail. This mode provides some memory redundancy, but does not provide as much redundancy as mirroring. 
  * adddc-sparing—System reliability is optimized by holding memory in reserve so that it can be used in case other DIMMs fail. This mode provides some memory redundancy, but does not provide as much redundancy as mirroring. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
NUMA optimized set numa-config numa-optimization |  Whether the BIOS supports NUMA. This can be one of the following: 

  * disabled—The BIOS does not support NUMA. 
  * enabled—The BIOS includes the ACPI tables that are required for NUMA-aware operating systems. If you enable this option, the system must disable Inter-Socket Memory interleaving on some platforms. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Memory Interleaving set CbsDfCmnMemIntlvControl |  Allows you to disable the memory interleaving |  **Note** |  NUMA nodes per socket will be honored regardless of this setting.  
---|---  
  
  * enabled—The BIOS support NUMA. 

  * disabled—The BIOS does not support NUMA. 

  * Auto—This is the default option. 

  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Post Package Repair  scope token-feature "PostPackageRepair" scope token-param PostPackageRepair |  Post Package Repair (PPR) provides the ability to repair faulty memory cells by replacing them with spare cells. This can be one of the following: 

  * disabled—The BIOS does not support selecting PPR Type. 
  * hard-ppr—This results in a permanent remapping of damaged storage cells. This is the default option. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Memory Size Limit in GB set memory-size-limit |  Limits the capacity in Partial Memory Mirror Mode up to 50 percent of the total memory capacity. The memory size can range from 0 GB to 65535 GB in increments of 1 GB.   
Mirroring Mode set memory-mirroring-mode mirroring-mode |  Memory mirroring enhances system reliability by keeping two identical data images in memory.  This option is only available if you choose the mirroring option for Memory RAS Config. It can be one of the following: 

  * inter-socket—Memory is mirrored between two Integrated Memory Controllers (IMCs) across CPU sockets. 
  * intra-socket—One IMC is mirrored with another IMC in the same socket. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Sparing Mode set memory-sparing-mode sparing-mode |  Sparing optimizes reliability by holding memory in reserve so that it can be used in case other DIMMs fail. This option provides some memory redundancy, but does not provide as much redundancy as mirroring. The available sparing modes depend on the current memory population.  This option is only available if you choose sparing option for Memory RAS Config. It can be one of the following: 

  * dimm-sparing—One DIMM is held in reserve. If a DIMM fails, the contents of a failing DIMM are transferred to the spare DIMM. 
  * rank-sparing—A spare rank of DIMMs is held in reserve. If a rank of DIMMs fails, the contents of the failing rank are transferred to the spare rank. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
LV DDR Mode set lv-dimm-support-config lv-ddr-mode |  Whether the system prioritizes low voltage or high frequency memory operations. This can be one of the following: 

  * auto—The CPU determines whether to prioritize low voltage or high frequency memory operations. 
  * power-saving-mode—The system prioritizes low voltage memory operations over high frequency memory operations. This mode may lower memory frequency in order to keep the voltage low. 
  * performance-mode—The system prioritizes high frequency operations over low voltage operations. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
DRAM Refresh Rate set dram-refresh-rate-config dram-refresh |  The refresh interval rate for internal memory. This can be one of the following: 

  * 1x
  * 2x
  * 3x
  * 4x
  * auto
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
DDR3 Voltage Selection set ddr3-voltage-config ddr3-voltage |  The voltage to be used by the dual-voltage RAM. This can be one of the following: 

  * ddr3-1500mv
  * ddr3-1350mv
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Partial Memory Mirror Mode set memory-mirroring-mode mirroring-mode |  Partial Memory Mirroring enables you to partially mirror by GB or by a percentage of the memory capacity. Depending on the option selected here, you can define either a partial mirror percentage or a partial mirror capacity in GB in available fields. You can partially mirror up to 50 percent of the memory capacity. It can be one of the following: 

  * Disabled—Partial Memory Mode is disabled. This is the default option. 
  * Percentage—The amount of memory to be mirrored in the Partial Memory Mode is defined as a percentage of the total memory. 
  * Value in GB—The amount of memory to be mirrored in the Partial Memory Mode is defined in GB. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

|  **Note** |  Partial Memory Mirror Mode is mutually exclusive to standard Mirroring Mode.   
---|---  
  
Partial Mirrors 1-4 can be used in any number or configuration, provided they do not exceed the capacity limit set in GB or Percentage in the related options.   
  
Partial Mirror Percentage |  Limits the amount of available memory to be mirrored as a percentage of the total memory. This can range from 0.000.01 % to 50.00 % in increments of 0.01 %.   
Partial Mirror1 Size in GB |  Limits the amount of memory in Partial Mirror1 in GB. This can range from 0 GB to 65535 GB in increments of 1 GB.  
Partial Mirror2 Size in GB |  Limits the amount of memory in Partial Mirror2 in GB. This can range from 0 GB to 65535 GB in increments of 1 GB.  
Partial Mirror3 Size in GB |  Limits the amount of memory in Partial Mirror3 in GB. This can range from 0 GB to 65535 GB in increments of 1 GB.  
Partial Mirror4 Size in GB |  Limits the amount of memory in Partial Mirror4 in GB. This can range from 0 GB to 65535 GB in increments of 1 GB.  
Volatile Memory Mode scope token-feature "VolMemoryMode" scope token-param VolMemoryMode |  Allows the memory mode configuration. This can be any of the following:

  * 1lm—Configures 1 Layer Memory(1LM) 
  * 2lm—Configures 2 Layer Memory(1LM) 

  
Memory Bandwidth Boost scope token-feature "MemoryBandwidthBoost" scope token-param MemoryBandwidthBoost |  Allows to boost the memory bandwidth. This can be one of the following:

  * enabled
  * disabled

  
LLC Dead Line scope token-feature "LLC Dead Line" scope token-param LLCAlloc |  In CPU non-inclusive cache scheme, Mid-Level Cache (MLC) evictions are filled into the Last-Level Cache (LLC). When lines are evicted from the MLC, the core can flag them as dead (not likely to be read again). The LLC has the option to drop dead lines and not fill them in the LLC. This can be one of the following: 

  * enabled—Allows the LLC to fill dead lines into the LLC if there is free space available. This is the default option. 
  * disabled—The dead lines are always dropped and are never filled into the LLC. 
  * auto—The CPU determines the LLC dead line allocation 

  
XPT Remote Prefetch scope token-feature "XPT Remote Prefetch" scope token-param XPTRemotePrefetch |  This feature allows an LLC request to be duplicated and sent to an appropriate memory controller in a remote machine based on the recent LLC history to reduce latency. This can be one of the following: 

  * enabled
  * disabled
  * auto—The CPU determines the functionality. This is the default option. 

  
Virtual NUMA scope token-feature "Virtual Numa" scope token-param VirtualNuma |  The Virtual NUMA (virtual non-uniform memory access) is a memory-access optimization method for VMware virtual machines (VMs), which helps prevent memory-bandwidth bottlenecks. This can be one of the following: 

  * enabled—The functionality is enabled. 
  * disabled—The functionality is disabled. This is the default option. 

  
Above 4G Decoding scope token-feature "Above 4G Decoding" scope token-param Above 4G Decoding |  Enables or disables MMIO above 4GB or not. This can be one of the following:

  * enabled—The server maps I/O of 64-bit PCI devices to 4GB or greater address space. This is the default option. 
  * disabled—The server does not map I/O of 64-bit PCI devices to 4GB or greater address space. 

  
Select PPR Type scope token-feature "select ppr type" |  Supports **Hard-PPR** , which permanently remaps accesses from a designated faulty row to a designated spare row. 

  * hard ppr—Support is enabled. This is the default option.  |  **Note** |  Hard PPR can be used only when **Memory RAS Configuration** is set to **ADDDC Sparing**. For other RAS selections, this setting should be set to **Disabled**.   
---|---  
  * disabled—Support is disabled. 


  
Select Memory RAS Configuration scope token-feature "select memory ras configuration" |  Determines how the memory reliability, availability, and serviceability (RAS) is configured for the server. This can be one of the following: 

  * Mirror Mode 1LM—System reliability is optimized by using half the system memory as backup. 
  * ADDDC sparing—Adaptive virtual lockstep is an algorithm implemented in the hardware and firmware to support the ADDDC mode. When selected, the system performance is optimized till the algorithm is activated. The algorithm is activated in case of DRAM device failure. Once the algorithm is activated, the virtual lockstep regions are activated to map out the failed region during run-time dynamically, and the performance impact is restricted at a region level. This is the default option. 
  * Partial Mirror Mode 1LM—Partial DIMM Mirroring creates a mirrored copy of a specific region of memory cells, rather than keeping the complete mirror copy. Partial Mirroring creates a mirrored region in memory map with the attributes of a partial mirror copy. Up to 50% of the total memory capacity can be mirrored, using up to 4 partial mirrors. 
  * maximum performance—System performance is optimized. 

  
NUMA scope token-feature "numa" |  Whether the BIOS supports Non-Uniform Memory Access (NUMA). This can be one of the following:

  * enabled—Support is enabled. 
  * disabled—Support is disabled. 

  
CR FastGo Config set CrfastgoConfig  |  CR FastGo Config improves DDRT non-temporal write bandwidth when FastGO is disabled. When FastGO is enabled, it gives faster flow of NT writes into the uncore, When FastGO is disabled, it lessens NT writes queueing up in the CPU uncore, thereby improving sequentially at DCPMM, resulting in improved bandwidth.  Applies to all Cisco UCS M5 and Cisco UCS M6 servers.  The values can be one of the following:

  * auto—Same as Option 1. Disables FastGO. Recommended for DDRT. This is the default option (not Default). 
  * default—Enables FastGO. 
  * option 1—Disables FastGO. 
  * option 2, option 3, option 4, option 5—Not applicable. 
  * enable optimization
  * disable optimization

|  **Note** |  The values enable optimization, disable optimization, and auto are supported on Cisco UCS M6 servers   
---|---  
CR QoS set crqos |  Prevents DRAM and overall system BW drop in the presence of concurrent DCPMM BW saturating threads, with minimal impact to homogenous DDRT-only usages, Good for multi-tenant use cases, VMs, etc. Targeted for App Direct, but also improves memory mode. Targets the “worst-case” degradations.  Applies to all M5 and M6 servers.  The values can be one of the following:

  * disabled—Feature disabled. This is the default option. 
  * recipe 1—6 modules, 4 modules per socket optimized 
  * recipe 2—2 modules per socket optimized 
  * recipe 3—1 module per socket optimized 
  * mode 0 - disable the pmem qos feature
  * mode 1 - m2m qos enable;cha qos disable
  * mode 2 - m2m qos enable;cha qos enable

|  **Note** |  The values disabled, recipe 1, recipe 2, and recipe 3recipe 4 are not supported on Cisco UCS M6 servers   
---|---  
eADR Support scope token-feature "EadrSupport" scope token-param EadrSupport |  Extended asynchronous DRAM refresh (eADR) ensures that CPU caches lines with data are flushed at the right time and in the desired order and are also included in the power fail protected domain. This can be any of the following: 

  * enabled
  * disabled
  * auto—This is the default option. 

  
NVM Performance Setting  set NvmdimmPerformConfig  |  NVM Performance Setting  enables efficient major mode arbitration between DDR and DDRT transactions on the DDR channel to optimize channel BW and DRAM latency.  Applies to all M5 and M6 servers.  The values can be one of the following:

  * BW Optimized—Optimized for DDR and DDRT BW. This is the default option. 
  * Latency Optimized—Better DDR latency in the presence of DDRT BW. 
  * Balanced Profile—Optimized for Memory mode. 

  
Snoopy mode for 2LM set SnoopyModeFor2LM  |  Enables snoop-mode for DCPMM accesses while maintaining directory on all DRAM accesses. Snoops maintain cache coherence between sockets. Directory reduces snoops by keeping the remote node information locally (in memory). Directory lookups and updates add memory traffic.  Directory is a good tradeoff for DRAM, but not necessarily for DCPMM. For non-NUMA workload, when the feature is enabled, directory updates to DCPMM are eliminated, thereby helping DDRT bandwidth bound workloads. Directory is disabled for far memory accesses and instead snoops remote sockets to check for ownership. Directory is used only for DRAM (near memory). 

  * enabled
  * disabled—This is the default option. 

  
Snoopy mode for AD set SnoopyModeForAD  |  Enables snoop-mode for DCPMM accesses while maintaining directory on all DRAM accesses. Snoops maintain cache coherence between sockets. Directory reduces snoops by keeping the remote node information locally (in memory). Directory lookups and updates add memory traffic.  Directory is a good tradeoff for DRAM, but not necessarily for DCPMM. For non-NUMA workload, when the feature is enabled, directory updates to DCPMM are eliminated, thereby helping DDRT bandwidth bound workloads. Directory is disabled for accesses to AD and instead snoops remote sockets to check for ownership. Directory is used only for DRAM accesses. 

  * enabled
  * disabled—This is the default option. 

  
CBS_Cmn_Cpu_Sev_Asid_Space_Limit  set CBS_Cmn_Cpu_Sev_Asid_Space_Limit  |  The SEV-ES and SNP guests must use ASIDs in the range 1 through 1007. 

  * 1—This is the default option. 
  * 1007

  
Runtime Post Package Repair  set RuntimePostPackageRepair |  Enables the soft post-package repairs of the corrected memory errors during OS runtime.

  * disabled—This is the default option. 
  * enabled

  
  
### Intel® OptaneTM DC Persistent Memory (DCPMM) BIOS Tokens 

The following table lists the Intel® OptaneTM DC Persistent Memory (DCPMM) BIOS settings that you can configure through a BIOS policy or the default BIOS settings: 

Name  | Description   
---|---  
NVM Performance Setting  set NvmdimmPerformConfig  |  NVM Performance Setting  enables efficient major mode arbitration between DDR and DDRT transactions on the DDR channel to optimize channel BW and DRAM latency.  Applies to all M5 and M6 servers.  The values can be one of the following:

  * BW Optimized—Optimized for DDR and DDRT BW. This is the default option. 
  * Latency Optimized—Better DDR latency in the presence of DDRT BW. 
  * Balanced Profile—Optimized for Memory mode. 

  
CR QoS set crqos |  Prevents DRAM and overall system BW drop in the presence of concurrent DCPMM BW saturating threads, with minimal impact to homogenous DDRT-only usages, Good for multi-tenant use cases, VMs, etc. Targeted for App Direct, but also improves memory mode. Targets the “worst-case” degradations.  Applies to all M5 and M6 servers.  The values can be one of the following:

  * disabled—Feature disabled. This is the default option. 
  * recipe 1—6 modules, 4 modules per socket optimized 
  * recipe 2—2 modules per socket optimized 
  * recipe 3—1 module per socket optimized 
  * mode 0 - disable the pmem qos feature
  * mode 1 - m2m qos enable;cha qos disable
  * mode 2 - m2m qos enable;cha qos enable

|  **Note** |  The values disabled, recipe 1, recipe 2, and recipe 3recipe 4 are not supported on Cisco UCS M6 servers   
---|---  
CR FastGo Config set CrfastgoConfig  |  CR FastGo Config improves DDRT non-temporal write bandwidth when FastGO is disabled. When FastGO is enabled, it gives faster flow of NT writes into the uncore, When FastGO is disabled, it lessens NT writes queueing up in the CPU uncore, thereby improving sequentially at DCPMM, resulting in improved bandwidth.  Applies to all Cisco UCS M5 and Cisco UCS M6 servers.  The values can be one of the following:

  * auto—Same as Option 1. Disables FastGO. Recommended for DDRT. This is the default option (not Default). 
  * default—Enables FastGO. 
  * option 1—Disables FastGO. 
  * option 2, option 3, option 4, option 5—Not applicable. 
  * enable optimization
  * disable optimization

|  **Note** |  The values enable optimization, disable optimization, and auto are supported on Cisco UCS M6 servers   
---|---  
Snoopy mode for AD set SnoopyModeForAD  |  Enables snoop-mode for DCPMM accesses while maintaining directory on all DRAM accesses. Snoops maintain cache coherence between sockets. Directory reduces snoops by keeping the remote node information locally (in memory). Directory lookups and updates add memory traffic.  Directory is a good tradeoff for DRAM, but not necessarily for DCPMM. For non-NUMA workload, when the feature is enabled, directory updates to DCPMM are eliminated, thereby helping DDRT bandwidth bound workloads. Directory is disabled for accesses to AD and instead snoops remote sockets to check for ownership. Directory is used only for DRAM accesses. 

  * enabled
  * disabled This is the default option. 

  
Snoopy mode for 2LM set SnoopyModeFor2LM  |  Enables snoop-mode for DCPMM accesses while maintaining directory on all DRAM accesses. Snoops maintain cache coherence between sockets. Directory reduces snoops by keeping the remote node information locally (in memory). Directory lookups and updates add memory traffic.  Directory is a good tradeoff for DRAM, but not necessarily for DCPMM. For non-NUMA workload, when the feature is enabled, directory updates to DCPMM are eliminated, thereby helping DDRT bandwidth bound workloads. Directory is disabled for far memory accesses and instead snoops remote sockets to check for ownership. Directory is used only for DRAM (near memory). 

  * enabled
  * disabled This is the default option. 

  
eADR Support scope token-feature "EadrSupport" scope token-param EadrSupport |  Extended asynchronous DRAM refresh (eADR) ensures that CPU caches lines with data are flushed at the right time and in the desired order and are also included in the power fail protected domain. This can be any of the following: 

  * enabled
  * disabled
  * auto—This is the default option. 

  
  
### Serial Port BIOS Settings 

The following table lists the serial port BIOS settings that you can configure through a BIOS policy or the default BIOS settings: 

Name  | Description   
---|---  
Serial port A enable set serial-port-a-config serial-port-a |  Whether serial port A is enabled or disabled. This can be one of the following: 

  * disabled—The serial port is disabled. 
  * enabled—The serial port is enabled. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
  
### USB BIOS Settings 

The following table lists the USB BIOS settings that you can configure through a BIOS policy or the default BIOS settings: 

Name  | Description   
---|---  
Make Device Non Bootable set usb-boot-config` `make-device-non-bootable |  Whether the server can boot from a USB device. This can be one of the following: 

  * disabled—The server can boot from a USB device. 
  * enabled—The server cannot boot from a USB device. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Legacy USB Support set usb-boot-config ` `legacy-support |  Whether the system supports legacy USB devices. This can be one of the following: 

  * disabled—USB devices are only available to EFI applications. 
  * enabled—Legacy USB support is always available. 
  * auto—Disables legacy USB support if no USB devices are connected. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
USB Idle Power Optimizing Setting set usb-system-idle-power-optimizing-setting-config` `usb-idle-power-optimizing |  Whether the USB Idle Power Optimizing setting is used to reduce USB EHCI idle power consumption. Depending upon the value you choose, this setting can have an impact on performance. This can be one of the following: 

  * high-performance—The USB System Idle Power Optimizing setting is disabled, because optimal performance is preferred over power savings.  Selecting this option can significantly improve performance. We recommend you select this option unless your site has server power restrictions. 
  * lower-idle-power—The USB System Idle Power Optimizing setting is enabled, because power savings are preferred over optimal performance. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
USB Front Panel Access Lock set usb-front-panel-access-lock-config` `usb-front-panel-lock |  USB front panel access lock is configured to enable or disable the front panel access to USB ports. This can be one of the following: 

  * disabled
  * enabled
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Port 60/64 Emulation set usb-port-config` ` usb-emulation |  Whether the system supports 60h/64h emulation for complete USB keyboard legacy support. This can be one of the following: 

  * disabled—60h/64 emulation is not supported. 
  * enabled—60h/64 emulation is supported.  You should select this option if you are using a non-USB aware operating system on the server. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
USB Port Front set usb-port-config` ` usb-front |  Whether the front panel USB devices are enabled or disabled. This can be one of the following: 

  * disabled—Disables the front panel USB ports. Devices connected to these ports are not detected by the BIOS and operating system. 
  * enabled—Enables the front panel USB ports. Devices connected to these ports are detected by the BIOS and operating system. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
USB Port Internal set usb-port-config` ` usb-internal  |  Whether the internal USB devices are enabled or disabled. This can be one of the following: 

  * disabled—Disables the internal USB ports. Devices connected to these ports are not detected by the BIOS and operating system. 
  * enabled—Enables the internal USB ports. Devices connected to these ports are detected by the BIOS and operating system. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
USB Port KVM set usb-port-config` ` usb-kvm |  Whether the vKVM ports are enabled or disabled. This can be one of the following: 

  * disabled—Disables the KVM keyboard and/or mouse devices. Keyboard and/or mouse will not work in the KVM window. 
  * enabled—Enables the KVM keyboard and/or mouse devices. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
USB Port Rear set usb-port-config` ` usb-rear |  Whether the rear panel USB devices are enabled or disabled. This can be one of the following: 

  * disabled—Disables the rear panel USB ports. Devices connected to these ports are not detected by the BIOS and operating system. 
  * enabled—Enables the rear panel USB ports. Devices connected to these ports are detected by the BIOS and operating system. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
USB Port SD Card set usb-port-config` ` usb-sdcard |  Whether the SD card drives are enabled or disabled. This can be one of the following: 

  * disabled—Disables the SD card drives. The SD card drives are not detected by the BIOS and operating system. 
  * enabled—Enables the SD card drives. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
USB Port VMedia set usb-port-config` ` usb-vmedia |  Whether the virtual media devices are enabled or disabled. This can be one of the following: 

  * disabled—Disables the vMedia devices. 
  * enabled—Enables the vMedia devices. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
All USB Devices set all-usb-devices-config` `all-usb |  Whether all physical and virtual USB devices are enabled or disabled. This can be one of the following: 

  * disabled—All USB devices are disabled. 
  * enabled—All USB devices are enabled. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
xHCI Mode set usb-configuration-select-config` `xhci-enable-disable |  Whether xHCI mode is enabled or disabled. This can be one of the following: 

  * disabled—xHCI mode is disabled. 
  * enabled—xHCI mode is enabled. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
USB Port:M.2 Storage set usb port:m.2 |  Whether the USB Port:M.2 Storage are enabled or disabled. This can be one of the following: 

  * disabled—Disables USB Port:M.2 Storage. 
  * enabled—Enables USB Port:M.2 Storage. This is the default option. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
  
### PCI Configuration BIOS Settings 

The following table lists the PCI configuration BIOS settings that you can configure through a BIOS policy or the default BIOS settings: 

Name  | Description   
---|---  
Maximum memory below 4GB set max-memory-below-4gb-config max-memory |  Whether the BIOS maximizes memory usage below 4GB for an operating system without PAE support, depending on the system configuration. This can be one of the following: 

  * disabled—Does not maximize memory usage. Choose this option for all operating systems with PAE support. 
  * enabled—Maximizes memory usage below 4GB for an operating system without PAE support. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Memory mapped IO above 4GB set memory-mapped-io-above-4gb-config memory-mapped-io |  Whether to enable or disable memory mapped I/O of 64-bit PCI devices to 4GB or greater address space. Legacy option ROMs are not able to access addresses above 4GB. PCI devices that are 64-bit compliant but use a legacy option ROM may not function correctly with this setting enabled. This can be one of the following: 

  * disabled—Does not map I/O of 64-bit PCI devices to 4GB or greater address space. 
  * enabled—Maps I/O of 64-bit PCI devices to 4GB or greater address space. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
VGA Priority set vga-priority-config vga-priority |  Allows you to set the priority for VGA graphics devices if multiple VGA devices are found in the system. This can be one of the following: 

  * onboard—Priority is given to the onboard VGA device. BIOS post screen and OS boot are driven through the onboard VGA port. 
  * offboard—Priority is given to the PCIE Graphics adapter. BIOS post screen and OS boot are driven through the external graphics adapter port. 
  * onboard-vga-disabled—Priority is given to the PCIE Graphics adapter, and the onboard VGA device is disabled.  |  **Note** |  The vKVM does not function when the onboard VGA is disabled.   
---|---  
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 


**Note** |  Only onboard VGA devices are supported with Cisco UCS B-Series servers.   
---|---  
ASPM Support set aspm-support-config aspm-support |  Allows you to set the level of ASPM (Active Power State Management) support in the BIOS. This can be one of the following: 

  * disabled—ASPM support is disabled in the BIOS. 
  * auto—The CPU determines the power state. 
  * forcel0—Force all links to L0 standby (L0s) state. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
BME DMA Mitigation Support set bme-dma-config  |  Allows you to disable the PCI BME bit to mitigate the threat from an unauthorized external DMA. This can be one of the following: 

  * disabled—PCI BME bit is disabled in the BIOS. 
  * enabled—PCI BME bit is enabled in the BIOS. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
  
### QPI BIOS Settings 

The following table lists the QPI BIOS settings that you can configure through a BIOS policy or the default BIOS settings: 

Name  | Description   
---|---  
QPI Link Frequency Select set qpi-link-frequency-select-config qpi-link-freqency-mt-per-sec |  The Intel QuickPath Interconnect (QPI) link frequency, in megatransfers per second (MT/s). This can be one of the following: 

  *   *   *   *   * 6400
  * 7200
  * 8000
  * 9600
  * auto—The CPU determines the QPI link frequency. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
QPI Snoop Mode set qpi-snoop-mode vpqpisnoopmode |  This can be one of the following: 

  * home-snoop—The snoop is always spawned by the home agent (centralized ring stop) for the memory controller. This mode has a higher local latency than early snoop, but it provides extra resources for a larger number of outstanding transactions. 
  * cluster-on-die—This mode is available only for processors that have 10 or more cores. It is the best mode for highly NUMA optimized workloads. 
  * home-directory-snoop-with-osb
  * early-snoop—The distributed cache ring stops can send a snoop probe or a request to another caching agent directly. This mode has lower latency and it is best for workloads that have shared data sets across threads and can benefit from a cache-to-cache transfer, or for workloads that are not NUMA optimized. 
  * auto —The CPU determines the QPI Snoop mode. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
  
### Trusted Platform BIOS Settings

The following table lists the trusted platform BIOS settings that you can configure through a BIOS policy or the default BIOS settings: 

Name  | Description   
---|---  
Trusted Platform Module (TPM) Support set trusted-platform-module-config tpm-support |  Whether to enable or disable the Trusted Platform Module (TPM), which is a component that securely stores artifacts that are used to authenticate the server. This can be one of the following: 

  * disabled—Disables TPM. 
  * enabled—Enables TPM. 
  * platform-default—Enables TPM. 

  
Intel Trusted Execution Technology (TXT) Support set intel-trusted-execution-technology-config txt-support |  Whether to enable or disable Intel Trusted Execution Technology (TXT), which provides greater protection for information that is used and stored on the business server. This can be one of the following: 

  * disabled—Disables TXT. This is default option. 
  * enabled—Enables TXT. 
  * platform-default—Disables TXT. 

When you only enable TXT, it implicitly enables TPM, VT, and VTDio.   
SHA-1 PCR Bank scope token-feature "Trusted Platform Module" scope token-param SHA1PCRBank |  The Platform Configuration Register (PCR) is a memory location in the TPM. Multiple PCRs are collectively referred to as a PCR bank. A Secure Hash Algorithm 1 or SHA-1 PCR Bank allows to enable or disable TPM security. This can be one of the following: 

  * disabled—Disables SHA-1 PCR Bank. 
  * enabled—Enables SHA-1 PCR Bank. This is the default option. 

  
SHA-256 PCR Bank scope token-feature "Trusted Platform Module" scope token-param SHA256PCRBank |  The Platform Configuration Register (PCR) is a memory location in the TPM. Multiple PCRs are collectively referred to as a PCR bank. A Secure Hash Algorithm 256-bit or SHA-256 PCR Bank allows to enable or disable TPM security. This can be one of the following: 

  * disabled—Disables SHA-256 PCR Bank. 
  * enabled—Enables SHA-256 PCR Bank. This is the default option. 

  
Trusted Platform Module State scope token-feature "Trusted Platform Module" scope token-param "Trusted Platform Module state" |  Trusted Platform Module (TPM ) is a microchip designed to provide basic security-related functions primarily involving encryption keys. This option allows you to control the TPM Security Device support for the system. This can be one of the following: 

  * disabled—The server does not use the TPM. 
  * enabled—The server uses the TPM. This is the default option. 

  
TPM Pending Operation scope token-feature "TPM Pending Operation" scope token-param "TPM Pending Operation" |  Trusted Platform Module (TPM) Pending Operation option allows you to control the status of the pending operation. This can be one of the following: 

  * none—No action. This is the default option. 
  * tpmclear—Clear the pending operations. 

  
TPM Minimal Physical Presence scope token-feature "Trusted Platform Module" # scope token-param TpmPpiRequired # show token-settings expand |  Whether to enable or disable TPM Minimal Physical Presence, which enables or disables the communication between the OS and BIOS for administering the TPM without compromising the security. This can be one of the following: 

  * disabled—Disables TPM Minimal Physical Presence. This is default option. 
  * enabled—Enables TPM Minimal Physical Presence. 
  * platform-default—Disables TPM Minimal Physical Presence. 

  
DMA Control Opt-In Flag scope token-feature "Trusted Platform Module" # scope token-param "DmaCtrlOptIn" token-param # show token-settings |  Enabling this token enables Windows 2022 Kernel DMA Protection feature. The OS treats this as a hint that the IOMMU should be enabled to prevent DMA attacks from possible malicious devices. This can be one of the following: 

  * disabled—Disables DMA Control Opt-In Flag. This is default option. 
  * enabled—Enables DMA Control Opt-In Flag. 
  * platform-default—Disables DMA Control Opt-In Flag. 

  
Security Device Support set TpmSupport |  Enables or disables BIOS support for the security device. This can be one of the following: 

  * disabled—Deactivates security device functionality for streamlined performance. 
  * enabled—Activates security device functionality for enhanced protection. 

  
Above 4G Decoding scope token-feature "Above 4G Decoding" scope token-param Above 4G Decoding |  Enables or disables MMIO above 4GB or not. This can be one of the following:

  * enabled—The server maps I/O of 64-bit PCI devices to 4GB or greater address space. This is the default option. 
  * disabled—The server does not map I/O of 64-bit PCI devices to 4GB or greater address space. 

  
  
### LOM and PCIe Slots BIOS Settings 

The following table lists the USB BIOS settings that you can configure through a BIOS policy or the default BIOS settings: 

Name  | Description   
---|---  
PCIe Slot SAS OptionROM set slot-option-rom-enable-config pcie-sas |  Whether Option ROM is available on the SAS port. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * uefi-only—The expansion slot is available for UEFI only. 
  * legacy-only—The expansion slot is available for legacy only. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
PCIe Slot n Link Speed set slot-link-speed-config pcie-slotn-link-speed |  This option allows you to restrict the maximum speed of an adapter card installed in PCIe slot n. This can be one of the following: 

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * gen4—16GT/s is the maximum speed allowed. 
  * gen5—32GT/s is the maximum speed allowed. 
  * auto—The maximum speed is set automatically. This is the default option. 
  * disabled—The maximum speed is not restricted. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
PCIe Slot n OptionROM set slot-option-rom-enable-config slotn-option-rom-enable |  Whether Option ROM is available on the port. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. This is the default option. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
PCIe Slot HBA OptionROM set slot-option-rom-enable-config pcie-hba |  Whether Option ROM is available on the HBA port. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * uefi-only—The expansion slot is available for UEFI only. 
  * legacy-only—The expansion slot is available for legacy only. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
PCIe Slot MLOM OptionROM set slot-option-rom-enable-config pcie-mlom |  Whether Option ROM is available on the MLOM port. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * uefi-only—The expansion slot is available for UEFI only. 
  * legacy-only—The expansion slot is available for legacy only. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
PCIe Slot Nx OptionROM set slot-option-rom-enable-config pcie-nx |  Whether Option ROM is available on the port. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * uefi-only—The expansion slot is available for UEFI only. 
  * legacy-only—The expansion slot is available for legacy only. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
PCIe 10G LOM 2 Link set lom-ports-config pcie-lom2-link |  Whether Option ROM is available on the 10G LOM port. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
PCI ROM CLP set pci-rom-clp-support pci-rom-clp-config |  PCI ROM Command Line Protocol (CLP) controls the execution of different Option ROMs such as PxE and iSCSI that are present in the card. By default, it is disabled. 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SIOC1 Option ROM set sioc1-optionrom-config sioc1-optionrom |  Whether the server can use Option ROM present in System IO Controller 1 (SIOC1). This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * uefi-only—The expansion slot is available for UEFI only. 
  * legacy-only—The expansion slot is available for legacy only. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SIOC2 Option ROM set sioc2-optionrom-config sioc2-optionrom |  Whether the server can use Option ROM present in System IO Controller 2 (SIOC2). This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * uefi-only—The expansion slot is available for UEFI only. 
  * legacy-only—The expansion slot is available for legacy only. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SBMEZZ1 Option ROM set sbmezz1-optionrom-config sbmezz1-optionrom |  Whether the server can use Option ROM present in SBMezz1 controller. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * uefi-only—The expansion slot is available for UEFI only. 
  * legacy-only—The expansion slot is available for legacy only. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SBMEZZ2 Option ROM set sbmezz2-optionrom-config sbmezz2-optionrom |  Whether the server can use Option ROM present in SBMezz2 controller. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * uefi-only—The expansion slot is available for UEFI only. 
  * legacy-only—The expansion slot is available for legacy only. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
IOESlot1 OptionROM set ioeslot1-optionrom-config ioeslot1-optionrom |  Whether option ROM is enabled on the IOE slot 1. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * uefi-only—The expansion slot is available for UEFI only. 
  * legacy-only—The expansion slot is available for legacy only. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
IOEMEZZ 1 OptionROM set ioemezz1-optionrom-config ioemezz1-optionrom |  Whether option ROM is enabled on the IOE Mezz1. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * uefi-only—The expansion slot is available for UEFI only. 
  * legacy-only—The expansion slot is available for legacy only. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
IOE Slot2 Option ROM set ioeslot2-optionrom-config ioeslot2-optionrom |  Whether option ROM is enabled on the IOE slot 2. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * uefi-only—The expansion slot is available for UEFI only. 
  * legacy-only—The expansion slot is available for legacy only. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
IO ENVME1 Option ROM set ioenvme1-optionrom-config ioenvme1-optionrom |  Whether option ROM is enabled on the IOE NVMe1. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * uefi-only—The expansion slot is available for UEFI only. 
  * legacy-only—The expansion slot is available for legacy only. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
IO ENVME2 Option ROM set ioenvme2-optionrom-config ioenvme2-optionrom |  Whether option ROM is enabled on the IOE NVMe2. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * uefi-only—The expansion slot is available for UEFI only. 
  * legacy-only—The expansion slot is available for legacy only. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SBNVME1 Option ROM set sbnvme1-optionrom-config sbnvme1-optionrom |  Whether the server can use Option ROM present in SBNVMe1 controller. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * uefi-only—The expansion slot is available for UEFI only. 
  * legacy-only—The expansion slot is available for legacy only. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
PCIe Slot MRAID-n OptionROM set Pcie SlotMRAID nOptionROM |  Whether Option ROM is available on the MRAID port. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
PCIe Slot RAID OptionROM set Pcie SlotRAIDOptionROM |  Whether Option ROM is available on the RAID port. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * uefi-only—The expansion slot is available for UEFI only. 
  * legacy-only—The expansion slot is available for legacy only. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Rear NVME n Link Speed set Pcie SlotRearNvme1LinkSpeed |  This option allows you to restrict the maximum speed of an NVME card installed in the rear PCIe slot n. This can be one of the following: 

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * gen4—16GT/s is the maximum speed allowed. 
  * gen5—32GT/s is the maximum speed allowed. 
  * enabled—The maximum speed is restricted.  |  **Note** | 
  * For _Rear NVME 1 Link Speed_ and _Rear NVME 2Link Speed_, the value enabled is not supported on Cisco UCS M6 and M8 servers. 
  * For _Rear NVME 3 Link Speed_ and _Rear NVME 4Link Speed_, the value enabled is available but has no effect at the BIOS level if selected.   
---|---  
  * auto—The maximum speed is set automatically. 

  * disabled—The maximum speed is not restricted. 

  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 


  
Front NVME n Link Speed set Pcie SlotFrontNvmenLinkSpeed |  This option allows you to restrict the maximum speed of an NVME card installed in the front PCIe slot. This can be one of the following: 

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * gen4—16GT/s is the maximum speed allowed. 
  * gen5—32GT/s is the maximum speed allowed. 
  * auto—The maximum speed is set automatically. This is the default option. 
  * enabled—The maximum speed is restricted.  |  **Note** |  For _Front NVME 1 Link Speed_ and _Front NVME 2 Link Speed_, the value enabled is available but not supported on Cisco UCS M6 and M8 servers.   
---|---  
  * disabled—The maximum speed is not restricted. 

  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 


**Note** |  For _Front Nvme 13 Link Speed_ to _Front Nvme 24 Link Speed_ , the BIOS tokens and values are available but have no effect at the BIOS level if selected.   
---|---  
HBA Link Speed set HBALinkSpeed |  This option allows you to restrict the maximum speed of an HBA card. This can be one of the following: 

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * auto—The maximum speed is set automatically. 
  * disabled—The maximum speed is not restricted. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
MLOM Link Speed set Pcie SlotMLOMLinkSpeed |  This option allows you to restrict the maximum speed of an MLOM adapter. This can be one of the following: 

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * gen4—16GT/s is the maximum speed allowed. 
  * gen5—16GT/s is the maximum speed allowed. 
  * auto—The maximum speed is set automatically. This is the default option. 
  * disabled—The maximum speed is not restricted. 
  * enabled—The maximum speed is restricted.  |  **Note** |  The value enabled is not supported on Cisco UCS M6 and M8 servers.   
---|---  
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 


  
MRAID Link Speed scope token-feature "Pcie Slot Link Speed" scope token-param PcieSlotMRAIDLinkSpeed |  This option allows you to restrict the maximum speed of MRAID. This can be one of the following:

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * gen4—16GT/s is the maximum speed allowed. 
  * gen5—32GT/s is the maximum speed allowed. 
  * auto—The maximum speed is set automatically. 
  * enabled—The maximum speed is not restricted.  |  **Note** |  The value enabled is not supported on Cisco UCS M6 servers.   
---|---  
  * disabled—The maximum speed is not restricted. 

  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 


  
RAID-n Link Speed set Pcie SlotRAIDLinkSpeed |  This option allows you to restrict the maximum speed of RAID. This can be one of the following: 

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * gen4—16GT/s is the maximum speed allowed. 
  * auto—The maximum speed is set automatically. 
  * disabled—The maximum speed is not restricted. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
All Onboard LOM set AllLomPortControl |  Whether all onboard LOM ports are enabled or disabled. This can be one of the following:

  * enabled—All onboard LOM are enabled. 
  * disabled—All onboard LOM are disabled. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
LOM Port 1 OptionRom set LomOpromControlPort0 |  Whether Option ROM is available on the LOM port 1. This can be one of the following:

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * uefi-only—The expansion slot is available for UEFI only. 
  * legacy-only—The expansion slot is available for legacy only. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
LOM Port 2 OptionRom set LomOpromControlPort1 |  Whether Option ROM is available on the LOM port 2. This can be one of the following:

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * uefi-only—The expansion slot is available for UEFI only. 
  * legacy-only—The expansion slot is available for legacy only. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Slot n State set SlotnState |  The state of the adapter card installed in PCIe slot n. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * uefi-only—The expansion slot is available for UEFI only. 
  * legacy-only—The expansion slot is available for legacy only. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SBNVMe1 OptionROM set SBNVMe1OptionROM |  Whether the server can use Option ROM present in SBNVMe1 controller. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SBNVMe2 OptionROM set SBNVMe2OptionROM |  Whether the server can use Option ROM present in SBNVMe2 controller. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SIOCNVMe1 OptionROM set SIOCNVMe1OptionROM |  Whether the server can use Option ROM present in SIOCNVMe1 controller. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SIOCNVMe2 OptionROM set SIOCNVMe2OptionROM |  Whether the server can use Option ROM present in SIOCNVMe2 controller. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SBLom1 OptionROM set SBLom1OptionROM |  Whether the server can use Option ROM present in the SBLom1 controller. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SBNVMen Link Speed set SBNVMenLinkSpeed |  Link speed for SBNVMe slot n. This can be one of the following: 

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * enabled—The maximum speed is restricted. 
  * disabled—The maximum speed is not restricted. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SIOCNVMen Link Speed set SIOCNVMenLinkSpeed |  Link speed for SIOCNVMe slot n. This can be one of the following: 

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * enabled—The maximum speed is restricted. 
  * disabled—The maximum speed is not restricted. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SIOCn Link Speed set SIOCnLinkSpeed |  Link speed for SIOC slot n. This can be one of the following: 

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * enabled—The maximum speed is restricted. 
  * disabled—The maximum speed is not restricted. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SBMezzn Link Speed set SBMezznLinkSpeed |  Link speed for SBMezz slot n. This can be one of the following: 

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * enabled—The maximum speed is restricted. 
  * disabled—The maximum speed is not restricted. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
IOESlotn Link Speed set IOESlotnLinkSpeed |  Link speed for IOE slot n. This can be one of the following: 

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * enabled—The maximum speed is restricted. 
  * disabled—The maximum speed is not restricted. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
IOEMezzn Link Speed set IOEMezznLinkSpeed |  Link speed for IOEMezz slot n. This can be one of the following: 

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * enabled—The maximum speed is restricted. 
  * disabled—The maximum speed is not restricted. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
IOENVMen Link Speed set IOENVMenLinkSpeed |  Link speed for IOENVMe slot n. This can be one of the following: 

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * enabled—The maximum speed is restricted. 
  * disabled—The maximum speed is not restricted. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
CDN Support for LOMs set CdnSupport |  Whether the Ethernet Networking Identifier naming convention is according to Consistent Device Naming (CDN) or the traditional way of naming conventions. This can be one of the following: 

  * enabled—OS Ethernet Network Identifier is named in a consistent device naming (CDN) convention according to the physical LAN on Motherboard (LOM) port numbering; LOM Port 0, LOM Port 1 and so on. 
  * disabled—OS Ethernet Networking Identifier is named in a default convention as ETH0, ETH1 and so on. By default, CDN option is disabled. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
VMD Enable set VMDEnable |  Whether NVMe SSDs that are connected to the PCIe bus can be hot swapped. It also standardizes the LED status light on these drives. LED status lights can be optionally programmed to display specific Failure indicator patterns. This can be one of the following:

  * enabled—Hot swap of NVMe SSDs that are connected to the PCIe bus is allowed. 
  * disabled—Hot swap of NVMe SSDs that are connected to the PCIe bus is not allowed. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
ACS Control SLOT-n set ACSCtlSlotn n = 11 to 14 |  Access Control Services (ACS) allow the processor to enable or disable peer-to-peer communication between multiple devices for Control Slot n. This can be one of the following: 

  * enabled— Enables peer-to-peer communication between multiple devices for Control Slot n. 
  * disabled— Disables peer-to-peer communication between multiple devices for Control Slot n. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
PCIe Slot GPUn OptionROM Only for Cisco UCS C480 M5 ML Server |  Whether the Option ROM is enabled on GPU slot n. n is the slot number, which can be numbered 1 through 8. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
ACS Control GPU-n set ACSCtlGpun n = 1 to 8 |  Access Control Services (ACS) allow the processor to enable or disable peer-to-peer communication between multiple devices for GPUs. This can be one of the following: 

  * disabled— Enables peer-to-peer communication between multiple devices for GPUs. 
  * enabled— Disables peer-to-peer communication between multiple devices for GPUs. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
PCIe PLL SSC |  Reduces EMI interference by down-spreading the clock by 0.5%. Disable this feature to centralize the clock without spreading. For all Cisco UCS M5 and M6 servers, this option is Disabled by default. 

  * disabled— Clock is centralized without spreading. 
  * auto— EMI interference is auto adjusted. 
  * zeropointfive— EMI interference us reduced by down-spreading the clock by 0.5%. 
  * platform-default— The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Front Nvme n OptionROM scope token-feature "PCI Slot OptionROM Enable" scope token-param PcieSlotFrontNvme nOptionROM |  This options allows you to control the Option ROM execution of the PCIe adapter connected to the SSD:NVMe slot n. This can be one of the following: 

  * enabled—This is the default option. 
  * disabled

  
PCIe Slot n Link Speed scope token-feature "PCI Slot LINK Speed" scope token-param PcieSlotLinkSpeed |  Link speed for PCIe Slot designated by slot n. This can be one of the following: 

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * gen4—16GT/s is the maximum speed allowed. 
  * gen5—16GT/s is the maximum speed allowed. 
  * auto—The maximum speed is set automatically. 
  * disabled—The maximum speed is not restricted. 

  
MSTOR-RAID Link Speed sc token-feature "PCI Slot LINK Speed" sc token-param PcieSlotMSTORRAIDLinkSpeed |  This option allows you to restrict the maximum speed of an MSTOR adapter. This can be one of the following: 

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * gen4—16GT/s is the maximum speed allowed. 
  * auto—The maximum speed is set automatically. 
  * disabled—The maximum speed is not restricted. 

|  **Note** |  In this BIOS setting _MSTOR-RAID Link Speed_ , the token and values are available but have no effect at the BIOS level if selected.   
---|---  
MSTOR-RAID OptionROM sc token-feature "MSTOR-RAID OptionROM" sc token-param PcieSlotMSTORRAIDoptionROM |  Whether the server can use the Option ROMs present in the PCIe MSTOR RAID. This can be any of the following:

  * disabled—Option ROM is available. 
  * enabled—Option ROM is not available. This is the default option. 

  
MLOM OptionROM set slot-option-rom-enable-config pcie-mlom |  Whether Option ROM is available on the MLOM port. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. This is the default option. 

  
MRAID OptionROM set Pcie SlotMRAID OptionROM |  Whether Option ROM is available on the MRAID port. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. This is the default option. 

  
Rear Nvme n OptionRom set RearNvmenOptionROM |  Whether Option ROM is available on the Rear NVMEn port. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. This is the default option. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
PCIe slot MSTOR Link Speed sc token-feature "PCI Slot LINK Speed" sc token-param PcieSlotMSTORRAIDLinkSpeed |  This option allows you to restrict the maximum speed of an MSTOR adapter. This can be one of the following: 

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * gen4—16GT/s is the maximum speed allowed. 
  * gen5—32GT/s is the maximum speed allowed. 
  * auto—The maximum speed is set automatically. This is the default option. 
  * disabled—The maximum speed is not restricted. 

  
PCIe Slot MSTOR RAID OptionROM scope token-feature "pcie MSTOR-RAID OptionROM" sc token-param PcieSlotMSTORRAIDoptionROM |  Whether the server can use the Option ROMs present in the PCIe MSTOR RAID. This can be any of the following:

  * disabled—Option ROM is available. 
  * enabled—Option ROM is not available. This is the default option. 

  
PCIe RAS Support sc token-feature "pcie ras-support" |  Whether PCIe RAS Support is available on the PCIe slot. This can be one of the following:

  * disabled—PCIe RAS is available on the slot. 
  * enabled—PCIe RAS is not available on the slot. This is the default option. 

  
MRAID n Link Speed scope token-feature "Pcie Slot Link Speed" scope token-param PcieSlotMRAIDLinkSpeed |  This option allows you to restrict the maximum speed of MRAID. This can be one of the following:

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * gen4—16GT/s is the maximum speed allowed. 
  * gen5—32GT/s is the maximum speed allowed. 
  * auto—The maximum speed is set automatically. This is the default option. 
  * disabled—The maximum speed is not restricted. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
MRAIDn OptionROM scope token-feature "Pcie Slot OptionROM" scope token-param PcieSlotOptionROM |  Whether Option ROM is available on the MRAID port. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. This is the default option. 

  
NVME-n OptionROM scope token-feature "Pcie Slot OptionROM" scope token-param PcieSlotOptionROM |  Whether Option ROM is available on the NVME port. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. This is the default option. 

  
PCIe Slot OCP Link Speed scope token-feature "Pcie Slot ocp Link Speed" scope token-param PcieSlotocpLinkSpeed |  This option allows you to restrict the maximum speed of OCP. This can be one of the following:

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * auto—The maximum speed is set automatically. This is the default option. 
  * disabled—The maximum speed is not restricted. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
RAIDn OptionROM scope token-feature "raid optionrom" scope token-param raidoptionrom |  Whether Option ROM is available on the RAID port. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. This is the default option. 

  
IOENVMen OptionROM scope token-feature "ioenvme optionrom" scope token-param ioenvmeoptionrom |  Whether Option ROM is available on the IOENVMe port. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. This is the default option. 

  
GPUn OptionRom scope token-feature "ioemezz1 optionrom" scope token-param ioemezz1optionrom |  Whether Option ROM is available on the GPU port. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. This is the default option. 

  
RAID Link Speed scope token-feature "raid link speed" scope token-param RAIDLinkSpeed |  This option allows you to restrict the maximum speed of RAID. This can be one of the following:

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * auto—The maximum speed is set automatically. This is the default option. 
  * enabled—The maximum speed is not restricted.  |  **Note** |  The value enabled is not supported on Cisco UCS M6and M8 servers.   
---|---  
  * disabled—The maximum speed is not restricted. 

  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 


  
External SSC enable |  This option allows you to Enable/Disable the Clock Spread Spectrum of the external clock generators. For Cisco B-Series M5 and M6servers and S-Series M5 servers, this option is Disabled by default. For Cisco C-Series rack servers, it is enabled by default. 

  * disabled— Clock Spread Spectrum support is not available. 
  * enabled— Clock Spread Spectrum support is always available. 
  * platform-default — The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Re-size BAR Support set ResizeBarSupport |  Allows to enable or disable re-sizable BAR support setup.

  * enabled—This is the default option. 
  * disabled

  
SR-IOV Support scope token-feature "sriov" scope token-param "sriov-support" |  Whether SR-IOV (Single Root I/O Virtualization) is enabled or disabled on the server. This can be one of the following:

  * enabled—SR-IOV is enabled. This is the default option. 
  * disabled—SR-IOV is disabled. 

  
  
### Graphics Configuration BIOS Settings 

The following tables list the graphics configuration BIOS settings that you can configure through a BIOS policy or the default BIOS settings: 

Name  | Description   
---|---  
Integrated Graphics set integrated-graphics-config integrated-graphics |  Enables integrated graphics. This can be one of the following: 

  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 
  * enabled—Integrated graphic is enabled. 
  * disabled—Integrated graphics is disabled. 

  
Integrated Graphics Aperture Size set integrated-graphics-aperture-config integrated-graphics-aperture |  Allows you to set the size of mapped memory for the integrated graphics controller. This can be one of the following: 

  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 
  * 128mb
  * 256mb
  * 512mb
  * 1024mb
  * 2048mb
  * 4096mb

  
Onboard Graphics set onboard-graphics-config onboard-graphics |  Enables onboard graphics (KVM). This can be one of the following: 

  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 
  * enabled—Onboard graphics is enabled. 
  * disabled—Onboard graphics is disabled. 

  
  
### Boot Options BIOS Settings 

The following table lists the boot options BIOS settings that you can configure through a BIOS policy or the default BIOS settings: 

Name  | Description   
---|---  
Boot option retry set boot-option-retry-config retry |  Whether the BIOS retries NON-EFI based boot options without waiting for user input. This can be one of the following: 

  * disabled—Waits for user input before retrying NON-EFI based boot options. This is the default option. 
  * enabled—Continually retries NON-EFI based boot options without waiting for user input. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SAS RAID set intel-entry-sas-raid-config sas-raid |  Whether the Intel SAS Entry RAID Module is enabled. This can be one of the following: 

  * disabled—The Intel SAS Entry RAID Module is disabled. 
  * enabled—The Intel SAS Entry RAID Module is enabled. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SAS RAID module set intel-entry-sas-raid-config sas-raid-module |  How the Intel SAS Entry RAID Module is configured. This can be one of the following: 

  * it-ir-raid—Configures the RAID module to use Intel IT/IR RAID. 
  * intel-esrtii—Configures the RAID module to use Intel Embedded Server RAID Technology II. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Onboard SCU Storage Support set onboard-sas-storage-config onboard-sas-ctrl |  Whether the onboard software RAID controller is available to the server. This can be one of the following: 

  * disabled—The software RAID controller is not available. 
  * enabled—The software RAID controller is available. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Cool Down Time (sec) |  The time to wait (in seconds) before the next boot attempt. This can be one of the following:

  * 15—System waits for 15 seconds before the next boot attempt. 
  * 45—System waits for 45 seconds before the next boot attempt. 
  * 90—System waits for 90 seconds before the next boot attempt. This is the default option. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

This token is valid only when the Boot Option Retry token has been enabled.  
Number of Retries |  Number of attempts to boot. This can be one of the following:

  * infinite—System tries all options to boot up. 
  * 13—System tries 13 times to boot up. This is the default option. 
  * 5—System tries 5 times to boot up 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
P-SATA mode |  This options allows you to select the P-SATA mode. This can be one of the following:

  * disabled—P-SATA mode is disabled. 
  * lsi-sw-raid—Sets both SATA and sSATA controllers to RAID mode for LSI SW RAID. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Power On Password |  This token requires that you set a BIOS password before using the F2 BIOS configuration. If enabled, password needs to be validated before you access BIOS functions such as IO configuration, BIOS set up, and booting to an operating system using BIOS. It can be one of the following: 

  * disabled—Power On Password is disabled. 
  * enabled—Power On Password is enabled. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Adaptive Memory Training |  When this token is enabled, the BIOS saves the memory training results (optimized timing/voltage values) along with CPU/memory configuration information and reuses them on subsequent reboots to save boot time. The saved memory training results are used only if the reboot happens within 24 hours of the last save operation. This can be one of the following: 

  * disabled—Adaptive Memory Training is disabled. 
  * enabled—Adaptive Memory Training is enabled. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
BIOS Tech Message Level Control (for C125 M5)  |  Enabling this token allows the BIOS Tech log output to be controlled at more a granular level. This reduces the number of BIOS Tech log messages that are redundant, or of little use. This can be one of the following: 

  * disabled—BIOS Techlog Level is disabled. 
  * enabled—BIOS Techlog Level is enabled. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
OptionROM Launch Optimization |  The Option ROM launch is controlled at the PCI Slot level, and is enabled by default. In configurations that consist of a large number of network controllers and storage HBAs having Option ROMs, all the Option ROMs may get launched if the PCI Slot Option ROM Control is enabled for all. However, only a subset of controllers may be used in the boot process. When this token is enabled, Option ROMs are launched only for those controllers that are present in boot policy. This can be one of the following: 

  * disabled—OptionROM Launch Optimization is disabled. 
  * enabled—OptionROM Launch Optimization is enabled. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
BIOS Techlog Level BIOSTechlogLevel |  This option denotes the type of messages in BIOS tech log file. The log file can be any of the following types: 

  * minimum—Critical messages will be displayed in the log file. This is the default option. 
  * normal—Warning and loading messages will be displayed in the log file. 
  * maximum—Normal and information related messages will be displayed in the log file. 

  
P-SATA OptionROM |  This options allows you to select the P-SATA mode. This can be one of the following:

  * lsi-sw-raid—Sets both SATA and sSATA controllers to RAID mode for LSI SW RAID. This is the default option. 
  * disabled—P-SATA mode is disabled. 
  * ahci—Sets the controllers to AHCI mode. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
M.2 SATA OptionROM |  This options allows you to select the P-SATA mode. This can be one of the following:

  * lsi-sw-raid—Sets both SATA and sSATA controllers to RAID mode for LSI SW RAID. This is the default option. 
  * disabled—P-SATA mode is disabled. 
  * ahci—Sets the controllers to AHCI mode. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
UEFI Boot Mode |  This options allows you to select the UEFI Boot mode. This can be one of the following:

  * disabled—UEFI Boot mode is disabled. 
  * enabled—UEFI Boot mode is enabled. 

  
VGA Priority set vga-priority-config vga-priority |  Allows you to set the priority for VGA graphics devices if multiple VGA devices are found in the system. This can be one of the following: 

  * onboard—Priority is given to the onboard VGA device. BIOS post screen and OS boot are driven through the onboard VGA port. 
  * offboard—Priority is given to the PCIE Graphics adapter. BIOS post screen and OS boot are driven through the external graphics adapter port. 
  * onboard-vga-disabled—Priority is given to the PCIE Graphics adapter, and the onboard VGA device is disabled.  |  **Note** |  The vKVM does not function when the onboard VGA is disabled.   
---|---  
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 


**Note** |  Only onboard VGA devices are supported with Cisco UCS B-Series servers.   
---|---  
IPv4 PXE Support scope token-feature "IPv4 PXE Support" scope token-param "IPv4PXESupport" |  Enables or disables IPv4 support for PXE. This can be one of the following:

  * disabled—IPv4 PXE support is not available. 
  * enabled—IPv4 PXE support is available. This is the default option. 

  
IPv6 PXE Support scope token-feature "IPv6 PXE Support" scope token-param "IPv6PXESupport" |  Enables or disables IPv6 support for PXE. This can be one of the following:

  * disabled—IPv6 PXE support is not available. 
  * enabled—IPv6 PXE support is available. This is the default option. 

  
IPv6 HTTP Support scope token-feature "HTTP BOOT" scope token-param "IPV6HTTP" |  Enables or disables IPv6 support for HTTP. This can be one of the following:

  * disabled—IPv6 HTTP support is not available. 
  * enabled—IPv6 HTTP support is available. This is the default option. 

  
Network Stack scope token-feature "Network Stack" scope token-param "NetworkStack" |  This option allows you to monitor IPv6 and IPv4. This can be one of the following

  * disabled—Network Stack support is not available.  |  **Note** |  When disabled, the value set for IPV4 PXE Support does not impact the system.   
---|---  
  * enabled—Network Stack support is available. This is the default option. 


**Note** |  When Network Stack token value is Disabled, the below tokens and their values are also set

  * IPV4PXE - Disabled
  * IPV4HTTP - Disabled
  * IPV6HTTP - Disabled

  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

BIOS parameter virtualization capability in Cisco UCS Manager maps a unified set of BIOS settings in a service profile to the actual BIOS supporting parameters. However, not all BIOS setting items are applicable to every server model/platform. When you create a custom BIOS policy and have the Boot Option Retry selected, and when there is no bootable option available, the reboot fails and Cisco UCS Manager displays this message : Reboot and Select proper Boot device or Insert Boot Media in selected Boot device and press a key. You must manually set a boot option after the boot path is corrected, in order to enable the servers to reboot after a power outage. For more information about BIOS default server policies and the BIOS options and their default settings, see BIOS Policy and Server BIOS Settings. 

* * *  
  
---|---  
  
### Server Management BIOS Settings 

The following tables list the server management BIOS settings that you can configure through a BIOS policy or the default BIOS settings: 

#### General Settings 

Name  | Description   
---|---  
Serial Mux set SerialMux |  Enables or disables the serial mux configuration. This can be one of the following: 

  * enabled—Enables the serial mux configuration. 
  * disabled—Disables the serial mux configuration. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Assert NMI on SERR set assert-nmi-on-serr-config assertion |  Whether the BIOS generates a non-maskable interrupt (NMI) and logs an error when a system error (SERR) occurs. This can be one of the following: 

  * disabled—The BIOS does not generate an NMI or log an error when a SERR occurs. 
  * enabled—The BIOS generates an NMI and logs an error when a SERR occurs. You must enable this setting if you want to enable Assert NMI on PERR. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Assert NMI on PERR set assert-nmi-on-perr-config assertion |  Whether the BIOS generates a non-maskable interrupt (NMI) and logs an error when a processor bus parity error (PERR) occurs. This can be one of the following: 

  * disabled—The BIOS does not generate an NMI or log an error when a PERR occurs. 
  * enabled—The BIOS generates an NMI and logs an error when a PERR occurs. You must enable Assert NMI on SERR to use this setting. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
OS Boot Watchdog Timer Policy set os-boot-watchdog-timer-policy-config os-boot-watchdog-timer-policy |  What action the system takes if the watchdog timer expires. This can be one of the following: 

  * power-off—The server is powered off if the watchdog timer expires during OS boot. 
  * reset—The server is reset if the watchdog timer expires during OS boot. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

This option is only available if you enable the OS Boot Watchdog Timer.   
OS Boot Watchdog Timer Timeout set os-boot-watchdog-timer-timeout-config os-boot-watchdog-timer-timeout  |  What timeout value the BIOS uses to configure the watchdog timer. This can be one of the following: 

  * 5-minutes—The watchdog timer expires 5 minutes after the OS begins to boot. 
  * 10-minutes—The watchdog timer expires 10 minutes after the OS begins to boot. 
  * 15-minutes—The watchdog timer expires 15 minutes after the OS begins to boot. 
  * 20-minutes—The watchdog timer expires 20 minutes after the OS begins to boot. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

This option is only available if you enable the OS Boot Watchdog Timer.   
FRB-2 Timer set frb-2-timer-config frb-2-timer  |  Whether the FRB-2 timer is used to recover the system if it hangs during POST. This can be one of the following: 

  * disabled—The FRB-2 timer is not used. 
  * enabled—The FRB-2 timer is started during POST and used to recover the system if necessary. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
  
#### Console Redirection Settings 

Name  | Description   
---|---  
Console redirection set console-redir-config console-redir |  Allows a serial port to be used for console redirection during POST and BIOS booting. After the BIOS has booted and the operating system is responsible for the server, console redirection is irrelevant and has no effect. This can be one of the following: 

  * disabled—No console redirection occurs during POST. 
  * com 0—Enables serial port for console redirection during POST. This option is valid only for M6 blade servers and rack-mount servers.  |  **Note** |  The value serial-port-a is not supported on M6 servers.   
---|---  
  * serial-port-b or COM 1—Enables serial port B for console redirection and allows it to perform server management tasks. This option is only valid for rack-mount servers. 

  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 


**Note** |  If you enable this option, you also disable the display of the Quiet Boot logo screen during POST.   
---|---  
Flow Control set console-redir-config flow-control |  Whether a handshake protocol is used for flow control. Request to Send / Clear to Send (RTS/CTS) helps to reduce frame collisions that can be introduced by a hidden terminal problem. This can be one of the following: 

  * none—No flow control is used. 
  * rts-cts—RTS/CTS is used for flow control. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

|  **Note** |  This setting must match the setting on the remote terminal application.   
---|---  
Baud rate set console-redir-config baud-rate |  What Baud rate is used for the serial port transmission speed. If you disable Console Redirection, this option is not available. This can be one of the following: 

  * 9600—A 9600 Baud rate is used. 
  * 19200—A 19200 Baud rate is used. 
  * 38400—A 38400 Baud rate is used. 
  * 57600—A 57600 Baud rate is used. 
  * 115200—A 115200 Baud rate is used. This is the default option. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

|  **Note** |  This setting must match the setting on the remote terminal application.   
---|---  
Terminal type set console-redir-config terminal-type |  What type of character formatting is used for console redirection. This can be one of the following: 

  * pc-ansi—The PC-ANSI terminal font is used. 
  * vt100—A supported vt100 video terminal and its character set are used. 
  * vt100-plus—A supported vt100-plus video terminal and its character set are used. 
  * vt-utf8—A video terminal with the UTF-8 character set is used. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

|  **Note** |  This setting must match the setting on the remote terminal application.   
---|---  
Legacy OS redirection set console-redir-config legacy-os-redir |  Whether redirection from a legacy operating system, such as DOS, is enabled on the serial port. This can be one of the following: 

  * disabled—The serial port enabled for console redirection is hidden from the legacy operating system. 
  * enabled— The serial port enabled for console redirection is visible to the legacy operating system. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Putty KeyPad set console-redir-config putty-function-keypad |  Allows you to change the action of the PuTTY function keys and the top row of the numeric keypad. This can be one of the following: 

  * vt100—The function keys generate `ESC OP` through `ESC O[.`
  * linux—Mimics the Linux virtual console. Function keys F6 to F12 behave like the default mode, but F1 to F5 generate `ESC [[A` through `ESC [[E`. 
  * xtermr6—Function keys F5 to F12 behave like the default mode. Function keys F1 to F4 generate ESC OP through ESC OS, which are the sequences produced by the top row of the keypad on Digital terminals. 
  * sco—The function keys F1 to F12 generate `ESC [M` through `ESC [X`. The function and shift keys generate `ESC [Y` through `ESC [j`. The control and function keys generate `ESC [k` through `ESC [v`. The shift, control and function keys generate `ESC [w` through `ESC [{`. 
  * escn—The default mode. The function keys match the general behavior of Digital terminals. The function keys generate sequences such as `ESC [11~` and `ESC [12~`. 
  * vt400—The function keys behave like the default mode. The top row of the numeric keypad generates `ESC OP` through `ESC OS`. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Out of Band Management |  Used for Windows Special Administration Control (SAC). This option allows you to configure the COM port 0 that can be used for Windows Emergency Management services. ACPI SPCR table is reported based on this setup option. This can be one of the following: 

  * disabled—Configures the COM port 0 as a general purpose port for use with the Windows Operating System. 
  * enabled—Configures the COM port 0 as a remote management port for Windows Emergency Management services. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Redirection After BIOS POST set console-redir-config putty-function-keypad |  Whether BIOS console redirection should be active after BIOS POST is complete and control given to the OS bootloader. This can be one of the following: 

  * always_enable—BIOS Legacy console redirection is active during the OS boot and run time. 
  * bootloader—BIOS Legacy console redirection is disabled before giving control to the OS boot loader. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
OS Watchdog Timer Policy scope token-feature "OS Boot Watchdog Timer Policy" scope token-param "OS Boot Watchdog Timer Policy" |  What action the system takes if the watchdog timer expires. This can be one of the following:

  * power_off—The server is powered off if the watchdog timer expires during OS boot. This is the default option. 
  * reset—The server is reset if the watchdog timer expires during OS boot. 

  
FRB 2 Timer scope token-feature "FRB 2 Timer" scope token-param "FRB 2 Timer" |  Whether the FRB2 timer is used for recovering the system if it hangs during POST. This can be one of the following:

  * disabled—The FRB2 timer is not used. 
  * enabled—The FRB2 timer is started during POST and used to recover the system if necessary. This is the default option. 

  
OS Watchdog Timer scope token-feature "OS Boot Watchdog Timer" scope token-param "OS Boot Watchdog Timer" |  Whether the BIOS programs the watchdog timer with a specified timeout value. This can be one of the following:

  * disabled—The watchdog timer is not used to track how long the server takes to boot. This is the default option. 
  * enabled—The watchdog timer tracks how long the server takes to boot. This is the default option. 

  
OS Watchdog Timer Timeout scope token-feature "OS Boot Watchdog Timer Timeout" scope token-param "OS Boot Watchdog Timer Timeout" |  If OS does not boot within the specified time, OS watchdog timer expires and system takes action according to timer policy. This can be one of the following: 

  * 5 minutes—The OS watchdog timer expires 5 minutes after it begins to boot. 
  * 10 minutes—The OS watchdog timer expires 10 minutes after it begins to boot. This is the default option. 
  * 15 minutes—The OS watchdog timer expires 15 minutes after it begins to boot. 
  * 20 minutes—The OS watchdog timer expires 20 minutes after it begins to boot. 

|  **Note** |  This option is applicable only when you enable the OS Boot Watchdog Timer.  
---|---

---

## Page 14: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Server-Mgmt/4-3/b_cisco_ucs_manager_server_mgmt_cli_guide_4_3/m_cli_firmware_upgrades.html

## Firmware Upgrades   
  
Beginning with Cisco UCS Manager Release 4.2(3), Cisco is releasing unified Cisco UCS Manager software and firmware upgrades for the following platforms with every release of Cisco UCS Manager: 

  * Cisco UCS Fabric Interconnects 9108 100G with Cisco UCS X-Series servers. 

  * Cisco UCS 6500 Series Fabric Interconnect with Cisco UCS B-Series, C-Series, and S-Series servers. 

  * Cisco UCS 6400 Series Fabric Interconnect with Cisco UCS B-Series, C-Series, and S-Series servers. 

  * Cisco UCS 6300 Series Fabric Interconnect with Cisco UCS B-Series, C-Series, and S-Series servers.

  * Cisco UCS 6324 Fabric Interconnect with Cisco UCS B-Series Servers and C-Series Servers, which is also known as UCS Mini.


You can upgrade the firmware through Auto Install, packages in service profiles, using the firmware automatic synchronization server policy, and directly at endpoints. For more information on guidelines and installing firmware, see the Cisco UCS Firmware Management Guide. 

---

## Page 15: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Server-Mgmt/4-3/b_cisco_ucs_manager_server_mgmt_cli_guide_4_3/m_cli_managing_diagnostics.html

## Overview of Cisco UCS Manager Diagnostics

The Cisco UCS Manager diagnostics tool enables you to verify the health of the hardware components on your servers. The diagnostics tool provides a variety of tests to exercise and stress the various hardware subsystems on the servers, such as memory and CPU. You can use the tool to run a sanity check on the state of your servers after you fix or replace a hardware component. You can also use this tool to run comprehensive burn-in tests before you deploy a new server in your production environment. 

When a system is new, a default diagnostics policy is created in org scope. This default policy is named default and it cannot be deleted. The user will receive an error message if they try to delete it. The default diagnostic policy is the preferred way to execute the same set of tests across all servers. Any diagnostic policy, including the default can be customized. 

The default policy only has one memory test. The default parameters of the memory test can be modified. In addition, the memory test within the default diagnostics policy can be deleted. If it does not have a memory test, the diagnostic policy will not run. 

---

## Page 16: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Server-Mgmt/4-3/m_cli_configuring_server-related_policies1.html

## Server BIOS Settings 

Cisco UCS provides two methods for making global modifications to the BIOS settings on servers in an Cisco UCS domain. You can create one or more BIOS policies that include a specific grouping of BIOS settings that match the needs of a server or set of servers, or you can use the default BIOS settings for a specific server platform. 

Both the BIOS policy and the default BIOS settings for a server platform enable you to fine tune the BIOS settings for a server managed by Cisco UCS Manager. 

Depending upon the needs of the data center, you can configure BIOS policies for some service profiles and use the BIOS defaults in other service profiles in the same Cisco UCS domain, or you can use only one of them. You can also use Cisco UCS Manager to view the actual BIOS settings on a server and determine whether they are meeting current needs. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCS Manager pushes BIOS configuration changes through a BIOS policy or default BIOS settings to the Cisco Integrated Management Controller (CIMC) buffer. These changes remain in the buffer and do not take effect until the server is rebooted.  We recommend that you verify the support for BIOS settings in the server that you want to configure. Some settings, such as Mirroring Mode for RAS Memory, are not supported by all Cisco UCS servers. 

* * *  
  
---|---  
  
### Main BIOS Settings 

The following table lists the main server BIOS settings that you can configure through a BIOS policy or the default BIOS settings: 

Name  | Description   
---|---  
Properties  
Reboot on BIOS Settings Change set reboot-on-update |  When the server is rebooted after you change one or more BIOS settings.  yes —If you enable this setting, the server is rebooted according to the maintenance policy in the server's service profile. For example, if the maintenance policy requires user acknowledgment, the server is not rebooted and the BIOS changes are not applied until a user acknowledges the pending activity.  no —If you do not enable this setting, the BIOS changes are not applied until the next time the server is rebooted, whether as a result of another server configuration change or a manual reboot.   
BIOS Setting  
Quiet Boot set quiet-boot-config quiet-boot |  What the BIOS displays during Power On Self-Test (POST). This can be one of the following: 

  * disabled—The BIOS displays all messages and Option ROM information during boot. 
  * enabled—The BIOS displays the logo screen, but does not display any messages or Option ROM information during boot. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
POST error pause set post-error-pause-config post-error-pause |  What happens when the server encounters a critical error during POST. This can be one of the following: 

  * disabled—The BIOS continues to attempt to boot the server. 
  * enabled—The BIOS pauses the attempt to boot the server and opens the Error Manager when a critical error occurs during POST. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Resume on AC power loss set resume-ac-on-power-loss-config resume-action |  How the server behaves when power is restored after an unexpected power loss. This can be one of the following: 

  * stay-off—The server remains off until manually powered on. 
  * last-state—The server is powered on and the system attempts to restore its last state. 
  * reset—The server is powered on and automatically reset. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Front panel lockout set front-panel-lockout-config front-panel-lockout |  Whether the power and reset buttons on the front panel are ignored by the server. This can be one of the following: 

  * disabled—The power and reset buttons on the front panel are active and can be used to affect the server. 
  * enabled—The power and reset buttons are locked out. The server can only be reset or powered on or off from the CIMC GUI. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
CDN Control  set consistent-device-name-control cdn-name |  Consistent Device Naming allows Ethernet interfaces to be named in a consistent manner. This makes Ethernet interface names more uniform, easy to identify, and persistent when adapter or other configuration changes are made.  Whether consistent device naming is enabled or not. This can be one of the following: 

  * disabled—Consistent device naming is disabled for the BIOS policy. 
  * enabled—Consistent device naming is enabled for the BIOS policy. This enables Ethernet interfaces to be named consistently. This is the default option. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
PCIe Slots CDN Control  set consistent-device-name-control pcie-slot-cdn-name |  PCIe Slots Consistent Device Naming (CDN) control allows PCIe slots to be named in a consistent manner. This makes PCIe slot names more uniform, easy to identify, and persistent when the configuration changes are made. This can be one of the following: 

  * disabled—Consistent device naming is disabled. This is the default option. 
  * enabled—Consistent device naming is enabled. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
  
### Processor BIOS Settings 

The following table lists the processor BIOS settings that you can configure through a BIOS policy or the default BIOS settings: 

Name  | Description   
---|---  
DFX OSB Configuration set DfxOsbEn |  Controls the Opportunistic Snoop Broadcast (OSB) feature. OSB is used by CHA to broadcast snoops under lightly loaded ring or Intel UPI link condition. It is used to reduce the latency due to the directory look up. This can be one of the following. 

  * enabled—The latency due to the directory look up is reduced. This is the default option. 
  * disabled—The latency due to the directory look up is not reduced. 
  * auto—Automatically controls the OSB feature. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
DLWM Support set CbsCmnGnbSMUDlwmSupport |  This value controls the Dynamic Link Width Management (DLWM) feature.  When the platform can support either an 8 lane or 16 lane xGMI operation, the dynamic adjustment feature provides power savings. This can be one of the following. 

  * enabled—Enables the DLWM feature. 
  * disabled—Disables the DLWM feature. 
  * auto—Automatically controls the DLWM feature. This is the default option. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
EDC Control Throttle set CbsCmnEdcControlThrottle |  Enables or disables the **EDC Shutdown Protection** which enhances the utilization tracking to avoid EDC shutdown responses to specific aggressive workloads. This can be one of the following. 

  * enabled—Enables the EDC Shutdown Protection. 
  * disabled—Disables the EDC Shutdown Protection. 
  * auto—This is the default option. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Local APIC Mode set CbsDbgCpuLApicMode |  Selects the APIC mode to be used. This can be one of the following.

  * Compatibility—Uses the compatibility option. 
  * XAPIC—Uses the standard xAPIC architecture. 
  * X2APIC—Uses the enhanced x2APIC architecture to support 32-bit addressability of processors. 
  * auto—Automatically uses the xAPIC architecture that is detected. This is the default option. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

|  **Note** |  For Local APIC Mode Bios token, Compatability values are not supported for the AMD EPYC 7XX2 series.   
---|---  
Memory Clock Speed 7xx3 (AMD 3rd Gen CPU)  set CbsCmnMemSpeedDdr47xx3 |  Allows the memory clock to be further reduced from the maximum platform limit. This can be one of the following:

  * auto—This is the default option. 
  * 400 MHz, 800 MHz, 933 MHz, 1067 MHz, 1200 MHz, 1333 MHz, 1467 MHz, 1600 MHz, 1633 MHz, 1667 MHz, 1700 MHz, 1767 MHz, 1800 MHz—The memory clock speed size. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Memory Clock Speed 7xx2 (AMD 2nd Gen CPU)  set CbsCmnMemSpeedDdr47xx2 |  Allows the memory clock to be further reduced from the maximum platform limit. This can be one of the following:

  * auto—This is the default option. 
  * 667 MHz, 800 MHz, 933 MHz, 1067 MHz, 1200 MHz, 1333 MHz, 1467 MHz, 1600 MHz—The memory clock speed size. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
xGMI Link Configuration set CbsDfDbgXgmiLinkCfg |  Configures the number of xGMI2 links that are used on a multi-socket system. This can be one of the following:

  * 2 xGMI Links
  * 3 xGMI Links
  * 4 xGMI Links
  * auto—Automatically configures the number of xGMI2 links. This is the default option. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Preferred IO 7xx3 (AMD 3rd Gen CPU)  set CbsCmnPreferredIO7xx3 |  Enables the feature for a preferred bus as a performance improvement. This can be one of the following:

  * auto—Automatically enables the preferred bus. This is the default option. 
  * Bus—Enables the preferred bus. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Preferred IO 7xx2 (AMD 2nd Gen CPU)  set CbsCmnPreferredIO7xx2 |  Enables the feature for a preferred bus as a performance improvement. This can be one of the following:

  * auto—This is the default option. 
  * Manual—Enables for a performance improvement. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Core Watchdog Timer Enable set CbsDbgCpuGenCpuWdt |  Enables or disables CPU watchdog timer. This can be one of the following:

  * enabled—Enables the CPU watchdog timer. 
  * disabled—Disables the CPU watchdog timer. 
  * auto—Automatically enables the CPU watchdog timer. This is the default option. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
IOAT Configuration set IOATConfigCpm |  Enables or disables the CPM (Content Processing Module) in IOAT (Intel® I/O Acceleration Technology) accelerators. This can be one of the following: 

  * enabled—Enables the CPM accelerators. This is the default option. 
  * disabled—Disables the CPM accelerators. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
PCIe Ten Bit Tag Support set CbsGnbDbgPcieTbtSupport |  Enables the PCIe ten bit tags for the supported devices. This can be one of the following: 

  * enabled—Enables the PCIe ten bit tags for the supported devices. 
  * disabled—Disables the PCIe ten bit tags for the supported devices. 
  * Auto—Automatically enables the PCIe ten bit tags for the supported devices. This is the default option. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
PRMRR Size set PrmrrSize |  Processor Reserved Memory Range Registers (PRMRR) is the size of the protected region in the systems DRAM. The maximum size of the PRMRR field in the BIOS configuration will match the amount of the SGX Enclave Capacity value for the Intel CPU being utilized.. This can be one of the following: 

  * invalid config—This is the default value. 
  * 128M, 256M, 512M, 1G, 2G, 4G, 8G, 16G, 32G, 64G, 128G, 256G, 512G —The size of the protected regions. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Intel Turbo Boost Tech set intel-turbo-boost-config turbo-boost |  Whether the processor uses Intel Turbo Boost Technology, which allows the processor to automatically increase its frequency if it is running below power, temperature, or voltage specifications. This can be one of the following: 

  * disabled—The processor does not increase its frequency automatically. 
  * enabled—The processor uses Turbo Boost Technology if required. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Enhanced Intel SpeedStep Tech set enhanced-intel-speedstep-config speed-step |  Whether the processor uses Enhanced Intel SpeedStep Technology, which allows the system to dynamically adjust processor voltage and core frequency. This technology can result in decreased average power consumption and decreased average heat production. This can be one of the following: 

  * disabled—The processor never dynamically adjusts its voltage or frequency. 
  * enabled—The processor utilizes Enhanced Intel SpeedStep Technology and enables all supported processor sleep states to further conserve power. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

We recommend that you contact your operating system vendor to make sure your operating system supports this feature.   
Intel HyperThreading Tech set hyper-threading-config hyper-threading |  Whether the processor uses Intel Hyper-Threading Technology, which allows multithreaded software applications to execute threads in parallel within each processor. This can be one of the following: 

  * disabled—The processor does not permit hyperthreading. 
  * enabled—The processor allows for the parallel execution of multiple threads. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

We recommend that you contact your operating system vendor to make sure the operating system supports this feature.   
Intel Speed Select set-IntelSpeedSelect |  Allows improved CPU performance by using Intel Speed Select technology to tune the CPU to run at one of three operating profiles, based on number of logical processor cores, frequency, and TDP thread setting, to improve performance over the basic Platform Default setting. These profiles correspond to High, Medium, and Low Core settings and can be one of the following: 

  * base—The processor uses Base. 
  * config1—The processor uses Config 1. 
  * config2—The processor uses Config 2. 
  * config3—The processor uses Config 3. 
  * config4—The processor uses Config 4.  |  **Note** |  The values config1 and config2 are not supported on Cisco UCS M6 and M7 servers.   
---|---  
**Note** |  For Cisco UCS M6 and Cisco UCS M7 servers, the values config 3 and config 4 (4th Gen Intel Xeon Scalable processors and 5th Gen Intel Xeon Scalable processors) are equivalent to the values config 1 and config 2 (3rd Gen Intel Xeon Scalable processors).   
---|---  
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 


  
Core Multi Processing set core-multi-processing-config multi-processing |  Sets the state of logical processor cores per CPU in a package. If you disable this setting, Intel Hyper Threading technology is also disabled. This can be one of the following: 

  * All—Enables multiprocessing on all logical processor cores. 
  * 1 through n—Specifies the number of logical processor cores per CPU that can run on the server. To disable multiprocessing and have only one logical processor core per CPU running on the server, choose 1. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

We recommend that you contact your operating system vendor to make sure your operating system supports this feature.   
Execute Disable Bit set execute-disable bit |  Classifies memory areas on the server to specify where the application code can execute. As a result of this classification, the processor disables code execution if a malicious worm attempts to insert code in the buffer. This setting helps to prevent damage, worm propagation, and certain classes of malicious buffer overflow attacks. This can be one of the following: 

  * disabled—The processor does not classify memory areas. 
  * enabled—The processor classifies memory areas. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

We recommend that you contact your operating system vendor to make sure your operating system supports this feature.   
Intel Virtualization Technology set intel-vt-config vt |  Whether the processor uses Intel Virtualization Technology, which allows a platform to run multiple operating systems and applications in independent partitions. This can be one of the following: 

  * disabled—The processor does not permit virtualization. 
  * enabled—The processor allows multiple operating systems in independent partitions. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

|  **Note** |  If you change this option, you must power cycle the server before the setting takes effect.   
---|---  
Hardware Prefetcher set processor-prefetch-config hardware-prefetch |  Whether the processor allows the Intel hardware prefetcher to fetch streams of data and instruction from memory into the unified second-level cache when necessary. This can be one of the following: 

  * disabled—The hardware prefetcher is not used. 
  * enabled—The processor uses the hardware prefetcher when cache issues are detected. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

|  **Note** |  CPUPerformance must be set to Custom in order to specify this value. For any value other than Custom, this option is overridden by the setting in the selected CPU performance profile.   
---|---  
Adjacent Cache Line Prefetcher set processor-prefetch-config adjacent-cache-line-prefetch |  Whether the processor fetches cache lines in even/odd pairs instead of fetching just the required line. This can be one of the following: 

  * disabled—The processor only fetches the required line. 
  * enabled—The processor fetches both the required line and its paired line. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

|  **Note** |  must be set to Custom in order to specify this value. For any value other than Custom, this option is overridden by the setting in the selected CPU performance profile.   
---|---  
DCU Streamer Prefetch set processor-prefetch-config dcu-streamer-prefetch |  Whether the processor uses the DCU IP Prefetch mechanism to analyze historical cache access patterns and preload the most relevant lines in the L1 cache. This can be one of the following: 

  * disabled—The processor does not try to anticipate cache read requirements and only fetches explicitly requested lines. 
  * enabled—The DCU prefetcher analyzes the cache read pattern and prefetches the next line in the cache if it determines that it may be needed. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
DCU IP Prefetcher set processor-prefetch-config dcu-ip-prefetch |  Whether the processor uses the DCU IP Prefetch mechanism to analyze historical cache access patterns and preload the most relevant lines in the L1 cache. This can be one of the following: 

  * disabled—The processor does not preload any cache data. 
  * enabled—The DCU IP prefetcher preloads the L1 cache with the data it determines to be the most relevant. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
KTI Prefetch |  KTI prefetch is a mechanism to get the memory read started early on a DDR bus. This can be one of the following:

  * disabled—The processor does not preload any cache data. 
  * enabled—The KTI prefetcher preloads the L1 cache with the data it determines to be the most relevant. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
LLC Prefetch |  Whether the processor uses the LLC Prefetch mechanism to fetch the date into the LLC. This can be one of the following: 

  * disabled—The processor does not preload any cache data. 
  * enabled—The LLC prefetcher preloads the L1 cache with the data it determines to be the most relevant. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
XPT Prefetch |  Whether XPT prefetch is used to enable a read request that is sent to the last level cache to issue a copy of that request to the memory controller prefetcher. This can be one of the following: 

  * disabled—The CPU does not use the XPT Prefetch option. 
  * enabled—The CPU enables the XPT prefetcher option. 
  * auto—The CPU auto enables the XPT prefetcher option. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Direct Cache Access set direct-cache-access-config access |  Allows processors to increase I/O performance by placing data from I/O devices directly into the processor cache. This setting helps to reduce cache misses. This can be one of the following: 

  * auto—The CPU determines how to place data from I/O devices into the processor cache. 
  * disabled—Data from I/O devices is not placed directly into the processor cache. 
  * enabled—Data from I/O devices is placed directly into the processor cache. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Processor C State set processor-c-state-config c-state |  Whether the system can enter a power savings mode during idle periods. This can be one of the following: 

  * disabled—The system remains in a high-performance state even when idle. 
  * enabled—The system can reduce power to system components such as the DIMMs and CPUs. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

We recommend that you contact your operating system vendor to make sure your operating system supports this feature.   
Processor C1E set processor-c1e-config c1e |  Allows the processor to transition to its minimum frequency upon entering C1. This setting does not take effect until after you have rebooted the server. This can be one of the following: 

  * disabled—The CPU continues to run at its maximum frequency in the C1 state. 
  * enabled—The CPU transitions to its minimum frequency. This option saves the maximum amount of power in the C1 state. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Processor C3 Report set processor-c3-report-config processor-c3-report |  Whether the processor sends the C3 report to the operating system. This can be one of the following: 

  * enabled—The processor sends the C3 report to the OS. 
  * disabled—The processor does not send the C3 report. 
  * acpi-c2—The processor sends the C3 report using the advanced configuration and power interface (ACPI) C2 format. 
  * acpi-c3—The processor sends the C3 report using the ACPI C3 format. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

On the Cisco UCS B440 Server, the BIOS Setup menu uses enabled and disabled for these options. If you specify acpi-c2 or acpi-c2, the server sets the BIOS value for that option to enabled.   
Processor C6 Report set processor-c6-report-config processor-c6-report |  Whether the processor sends the C6 report to the operating system. This can be one of the following: 

  * disabled—The processor does not send the C6 report. 
  * enabled—The processor sends the C6 report. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Processor C7 Report set processor-c7-report-config processor-c7-report |  Whether the processor sends the C7 report to the operating system. This can be one of the following: 

  * c7—The processor sends the report using the C7 format. 
  * c7s—The processor sends the report using the C7s format. 
  * disabled—The processor does not send the C7 report. 
  * enabled—The processor sends the C7 report. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Processor CMCI |  Enables CMCI generation. This can be one of the following:

  * disabled—The processor disables CMCI. 
  * enabled—The processor enables CMCI. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
CPU Performance set cpu-performance-config cpu-performance |  Sets the CPU performance profile for the server. This can be one of the following: 

  * Custom—All performance profile options can be configured from the BIOS setup on the server. In addition, the Hardware Prefetcher and Adjacent Cache-Line Prefetch options can be configured as well. 
  * high-throughput—Data reuse and the DCU IP prefetcher are enabled, and all other prefetchers are disabled. 
  * hpc—All prefetchers are enabled and data reuse is disabled. This setting is also known as high-performance computing. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Max Variable MTRR Setting set max-variable-mtrr-setting-config  processor-mtrr |  Allows you to select the number of mean time to repair (MTRR) variables. This can be one of the following: 

  * auto-max—BIOS uses the default value for the processor. 
  * 8—BIOS uses the number specified for the variable MTRR. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Local X2 APIC set local-x2-apic-config localx2-apic |  Allows you to set the type of Application Policy Infrastructure Controller (APIC) architecture. This can be one of the following: 

  * disabled—Processor disables Local X2 APIC. 
  * enabled—Processor enables Local X2 APIC. 
  * xapic—Uses the standard xAPIC architecture. 
  * x2apic—Uses the enhanced x2APIC architecture to support 32 bit addressability of processors. 
  * auto—Automatically uses the xAPIC architecture that is detected. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Power Technology set processor-energy-config cpu-power-management |  Enables you to configure the CPU power management settings for the following options: 

  * Enhanced Intel Speedstep Technology 
  * Intel Turbo Boost Technology 
  * Processor Power State C6 

Power Technology can be one of the following: 

  * disabled—The server does not perform any CPU power management and any settings for the BIOS parameters mentioned above are ignored. 
  * Energy_Efficient—The server determines the best settings for the BIOS parameters mentioned above and ignores the individual settings for these parameters. 
  * performance—The server automatically optimizes the performance for the BIOS parameters mentioned above. 
  * custom—The server uses the individual settings for the BIOS parameters mentioned above. You must select this option if you want to change any of these BIOS parameters. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Energy Performance  set processor-energy-config energy-performance |  Allows you to determine whether system performance or energy efficiency is more important on this server. This can be one of the following: 

  * performance — The server provides all server components with full power at all times. This option maintains the highest level of performance and requires the greatest amount of power. 
  * balanced-performance — The server provides all server components with enough power to keep a balance between performance and power. 
  * balanced-energy — The server provides all server components with enough power to keep a balance between performance and power. 
  * energy-efficient — The server provides all server components with less power to keep reduce power consumption. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

|  **Note** |  CPUPowerManagement must be set to Custom or the server ignores the setting for this parameter.   
---|---  
Frequency Floor Override set frequency-floor-override-config cpu-frequency |  Whether the CPU is allowed to drop below the maximum non-turbo frequency when idle. This can be one of the following: 

  * disabled— The CPU can drop below the maximum non-turbo frequency when idle. This option decreases power consumption but may reduce system performance. 
  * enabled— The CPU cannot drop below the maximum non-turbo frequency when idle. This option improves system performance but may increase power consumption. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
P STATE Coordination set p-state-coordination-config p-state |  Allows you to define how BIOS communicates the P-state support model to the operating system. There are 3 models as defined by the Advanced Configuration and Power Interface (ACPI) specification. 

  * hw-all—The processor hardware is responsible for coordinating the P-state among logical processors with dependencies (all logical processors in a package). 
  * sw-all—The OS Power Manager (OSPM) is responsible for coordinating the P-state among logical processors with dependencies (all logical processors in a physical package), and must initiate the transition on all of the logical processors. 
  * sw-any—The OS Power Manager (OSPM) is responsible for coordinating the P-state among logical processors with dependencies (all logical processors in a package), and may initiate the transition on any of the logical processors in the domain. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

|  **Note** |  CPUPowerManagement must be set to Custom or the server ignores the setting for this parameter.   
---|---  
DRAM Clock Throttling set dram-clock-throttling-config dram-clock-throttling |  Allows you to tune the system settings between the memory bandwidth and power consumption. This can be one of the following: 

  * auto — CPU determines the DRAM Clock Throttling settings. 
  * balanced— DRAM clock throttling is reduced, providing a balance between performance and power. 
  * performance—DRAM clock throttling is disabled, providing increased memory bandwidth at the cost of additional power. 
  * Energy_Efficient—DRAM clock throttling is increased to improve energy efficiency. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Channel Interleaving set interleave-config channel-interleave |  Whether the CPU divides memory blocks and spreads contiguous portions of data across interleaved channels to enable simultaneous read operations. This can be one of the following: 

  * auto—The CPU determines what interleaving is done. 
  * 1-way— 
  * 2-way
  * 3-way
  * 4-way—The maximum amount of channel interleaving is used. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Rank Interleaving set interleave-config rank-interleave |  Whether the CPU interleaves physical ranks of memory so that one rank can be accessed while another is being refreshed. This can be one of the following: 

  * auto—The CPU determines what interleaving is done. 
  * 1-way— 
  * 2-way
  * 4-way
  * 8-way—The maximum amount of rank interleaving is used. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Sub NUMA Clustering |  This setting determines if the CPU supports sub NUMA clustering, which keeps the tag directory and memory channel in the same region to improve memory performance for certain workloads. This can be one of the following: 

  * auto—The BIOS determines the Sub-NUMA Clustering behavior automatically. 
  * disabled—Sub NUMA Clustering is turned off, and the CPU operates using a standard memory configuration without SNC optimization. This is the default option. 
  * enabled—Sub NUMA Clustering is activated, dividing the CPU into regions where the tag directory and memory channel remain in the same region for improved performance. 
  * snc 2—Sub NUMA Clustering divides the CPU into **two NUMA regions** , optimizing memory performance for workloads benefiting from moderate NUMA segmentation. 
  * snc 4—Sub NUMA Clustering divides the CPU into **four NUMA regions** , optimizing memory performance for workloads benefiting from moderate NUMA segmentation. 
  * platform-default— The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

|  **Note** |  The values SNC 2 and SNC 4 are not supported on Cisco UCS C220 M8, C240 M8, X210c M8 servers.  
---|---  
Memory Interleaving set interleave-config memory-interleave |  Whether the CPU interleaves the physical memory so that the memory can be accessed while another is being refreshed. This controls fabric level memory interleaving. Channel, die and socket have requirements based on memory populations and will be ignored if the memory does not support the selected option. This can be one of the following: 

  * none
  * channel
  * **die**
  * socket
  * auto—This is the default option. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Demand Scrub set scrub-policies-config demand-scrub |  Whether the system corrects single bit memory errors encountered when the CPU or I/O makes a demand read. This can be one of the following: 

  * disabled— Single bit memory errors are not corrected. 
  * enabled— Single bit memory errors are corrected in memory and the corrected data is set in response to the demand read. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Patrol Scrub set scrub-policies-config patrol-scrub |  Whether the system actively searches for, and corrects, single bit memory errors even in unused portions of the memory on the server. This can be one of the following: 

  * disabled—The system checks for memory ECC errors only when the CPU reads or writes a memory address. 
  * enabled—The system periodically reads and writes memory searching for ECC errors. If any errors are found, the system attempts to fix them. This option may correct single bit errors before they become multi-bit errors, but it may adversely affect performance when the patrol scrub is running. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
DCPMM Firmware Downgrade |  This can be one of the following: 

  * disabled—Support is disabled. 
  * enabled—Support is enabled. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Configurable TDP Control |  Allows you to set customized value for Thermal Design Power (TDP). This can be one of the following: 

  * auto— Uses the rated TDP value of the processor. 
  * manual—Allows you to customize the TDP value. 

  
Altitude set altitude altitude-config |  The approximate number of meters above sea level at which the physical server is installed. This can be one of the following: 

  * auto—The CPU determines the physical elevation. 
  * 300-m—The server is approximately 300 meters above sea level. 
  * 900-m—The server is approximately 900 meters above sea level. 
  * 1500-m—The server is approximately 1500 meters above sea level. 
  * 3000-m—The server is approximately 3000 meters above sea level. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Package C State Limit set package-c-state-limit-config package-c-state-limit |  The amount of power available to the server components when they are idle. This can be one of the following:  |  **Note** |  If you are changing the Package C State Limit token from any other value to no-limit, then ensure that the Power Technology is set to custom.   
---|---  
CPU Hardware Power Management set cpu-hardware-power-management-config cpu-hardware-power-management |  Enables processor Hardware Power Management (HWPM). This can be one of the following: 

  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 
  * disabled—HWPM is disabled. 
  * hwpm-native-mode—HWPM native mode is enabled. 
  * hwpm-oob-mode—HWPM Out-Of-Box mode is enabled. 
  * Native Mode with no Legacy (only GUI) 

  
Energy Performance Tuning set power-performance-tuning-support power-performance-tuning-config |  Determines if the BIOS or Operating System can turn on the energy performance bias tuning. The options are BIOS and OS.

  * bios— 
  * os— 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Workload Configuration |  This feature allows for workload optimization. The options are Balanced and I/O Sensitive:

  * balanced
  * io-sensitive—This is the default option. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

Cisco recommends using Balanced.   
Core Performance Boost set CbsCmnCpuCpb |  Whether the AMD processor increases its frequency on some cores when it is idle or not being used much. This can be one of the following: 

  * auto—The CPU automatically determines how to boost performance. This is the default option 
  * disabled—Core performance boost is disabled. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Uncore Frequency Scaling |  Allows you configure the scaling of the uncore frequency of the processor. This can be one of the following:

  * enabled—Uncore frequency of the processor scales up or down based on the load. (Default.) 
  * disabled—Uncore frequency of the processor remains fixed. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

Refer to the Intel Dear Customer Letter (DCL) to know the fixed higher and lower values for Uncore Frequency Scaling.  
Configurable TDP Level |  Allows adjustments in processor thermal design power (TDP) values. By modifying the processor behavior and the performance levels, power consumption of a processor can be configured and TDP can be adjusted at the same time. Hence, a processor operates at higher or lower performance levels, depending on the available cooling capacities and desired power consumption.  This can be one of the following:

  * normal—The CPU operates at its normal performance level. (Default.) 
  * level1
  * level1

|  **Note** |  Refer to the Intel Dear Customer Letter (DCL) for the values for TDP level.  
---|---  
UPI Link Speed set-qpilinkspeed |  Allows you to configure the Intel Ultra Path Interconnect (UPI) link speed between multiple sockets. This can be one of the following: 

  * auto—Automatically configures the optimal link speed. (Default) 
  * 9.6gt/s (gigatransfers per second)—Configures the optimal link speed at 9.6GT/s 
  * 10.4gt/s—Configures the optimal link speed at 10.4GT/s 
  * 11.2gt/s—Configures the optimal link speed at 11.2GT/s 
  * use per link setting |  **Note** |  The value use per link setting is not supported on UCS M6 and M7servers.   
---|---  

  
Global C-state Control set CbsCmnCpuGlobalCstateCtrl |  Whether the AMD processors control IO-based C-state generation and DF C-states. This can be one of the following:

  * auto—The CPU automatically determines how to control IO-based C-state generation. 
  * disabled—Global C-state control is disabled. This is the default option. 
  * enabled—Global C-state control is enabled. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
L1 Stream HW Prefetcher set CbsCmnCpuL1StreamHwPrefetcher |  Whether the processor allows the AMD hardware prefetcher to speculatively fetch streams of data and instruction from memory into the L1 cache when necessary. This can be one of the following: 

  * auto—The CPU determines how to place data from I/O devices into the processor cache. This is the default option. 
  * disabled—The hardware prefetcher is not used. 
  * enabled—The processor uses the hardware prefetcher when cache issues are detected. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
L2 Stream HW Prefetcher set CbsCmnCpuL2StreamHwPrefetcher |  Whether the processor allows the AMD hardware prefetcher to speculatively fetch streams of data and instruction from memory into the L2 cache when necessary. This can be one of the following: 

  * auto—The CPU determines how to place data from I/O devices into the processor cache. This is the default option. 
  * disabled—The hardware prefetcher is not used. 
  * enabled—The processor uses the hardware prefetcher when cache issues are detected. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
AMD Memory Interleaving Size |  Determines the size of the memory blocks to be interleaved. It also determines the starting address of the interleave (bit 8,9,10 or 11). This can be one of the following: 

  * 1 KB
  * 2 KB
  * 256 Bytes
  * 512 Bytes
  * auto—The CPU determines the size of the memory block. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Chipselect Interleaving set CbsCmnMemMapBankInterleaveDdr4 |  Whether memory blocks across the DRAM chip selects for node 0 are interleaved. This can be one of the following: 

  * auto—The CPU automatically determines how to interleave chip selects. This is the default option. 
  * disabled—Chip selects are not interleaved within the memory controller. 
  * enabled—Chip selects are interleaved within the memory controller. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Bank Group Swap set CbsCmnMemCtrlBankGroupSwapDdr44 |  Determines how physical addresses are assigned to applications. This can be one of the following: 

  * auto—The CPU automatically determines how to assign physical addresses to applications. This is the default option. 
  * disabled—Bank group swap is not used. 
  * enabled—Bank group swap is used to improve the performance of applications. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Determinism Slider set CbsCmnDeterminismSlider |  Allows AMD processors to determine how to operate. This can be one of the following: 

  * auto—The CPU automatically uses default power determinism settings. This is the default option. 
  * performance—Processor operates at the best performance in a consistent manner. 
  * power—Processor operates at the maximum allowable performance on a per die basis. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
IOMMU set CbsCmnGnbNbIOMMU |  Input Output Memory Management Unit (IOMMU) allows AMD processors to map virtual addresses to physical addresses. This can be one of the following: 

  * auto—The CPU determines how map these addresses. This is the default option. 
  * disabled—IOMMU is not used. 
  * enabled—Address mapping takes place through the IOMMU. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SVM Mode set SvmMode |  Whether the processor uses AMD Secure Virtual Machine Technology. This can be one of the following: This can be one of the following: 

  * disabled—The processor does not use SVM Technology. 
  * enabled—The processor uses SVM Technology. This is the default option. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SMT Mode |  Whether the processor uses AMD Simultaneous MultiThreading Technology, which allows multithreaded software applications to execute threads in parallel within each processor. This can be one of the following: 

  * disabled—The processor does not use SMT Technology. 
  * enabled—The processor uses SMT Technology. This is the default option. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SMEE |  Whether the processor uses the Secure Memory Encryption Enable (SMEE) function, which provides memory encryption support. This can be one of the following: 

  * auto—This is the default option. 
  * disabled—The processor does not use the SMEE function. 
  * enabled—The processor uses the SMEE function. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
UPI Prefetch set-upi-prefetch |  UPI prefetch is a mechanism to get the memory read started early on a DDR bus. This can be one of the following:

  * enabled—The UPI prefetcher preloads the L1 cache with the data it determines to be the most relevant. 
  * disabled—The processor does not preload any cache data. 
  * auto—The processor enables the UPI prefetcher option. 

  
SGX Auto MP Registration Agent set-SgxAutoRegistrationAgent |  Allows you to enable the registration authority service to store the platform keys. This can be one of the following: 

  * enabled—Support is enabled. 
  * disabled—Support is disabled. 

  
SProcessor Epoch n scope token-feature "Processor" scope token-param SgxEpoc nh |  Allows you to define the SGX EPOCH owner value for the EPOCH number designated by n.  
SGX Factory Reset  scope token-feature "Processor" scope token-param SgxFactoryReset |  Allows the system to perform SGX factory reset on subsequent boot. This deletes all registration data. This can be one of the following: 

  * enabled—Support is enabled. 
  * disabled—Support is disabled. 

  
SGX PBUKEY HASHn scope token-feature "Processor" scope token-param SgxLePubKeyHash n |  Allows you to set the Software Guard Extensions (SGX) value. This value can be set between:

  * SGX PUBKEY HASH0—Between 7-0
  * SGX PUBKEY HASH1—Between 15-8
  * SGX PUBKEY HASH2—Between 23-16
  * SGX PUBKEY HASH3—Between 31-24

  
SGX Write Enable scope token-feature "Processor" scope token-param SgxLeWr |  Allows you to enable SGX Write feature. This can be one of the following:

  * enabled—Support is enabled. 
  * disabled—Support is disabled. 

  
SGX Pkg info In-Band Access scope token-feature "Processor" scope token-param SgxPackageInfoInBandAccess |  Allows you to enable SGX Package Info In-Band Access. This can be one of the following:

  * enabled—Support is enabled. 
  * disabled—Support is disabled. 

  
SGX QoS scope token-feature "Processor" scope token-param SgxQoS |  Allows you to enable SGX QoS. This can be one of the following:

  * enabled— Support is enabled. 
  * disabled— Support is disabled. 

  
Intel Dynamic Speed Select scope token-feature "IntelSpeedSelect Configuration" scope token-param IntelDynamicSpeedSelect |  Intel Dynamic Speed Select modes allow you to run the CPU with different speed and cores in auto mode. This can be one of the following: 

  * enabled—Intel Dynamic Speed Select is enabled. 
  * disabled—Intel Dynamic Speed Select is disabled. 

  
IIO eDPC Support scope token-feature "Processor" scope token-param EdpcEn |  The eDPC (Enhanced Downstream Port Containment) allows a downstream link to be disabled after an uncorrectable error, enabling recovery possible in a controlled and robust manner. This can be one of the following: 

  * disabled—eDPC support is turned off, and the system does not take any action to disable downstream links in response to errors. 
  * on fatal errors—eDPC is enabled only for fatal errors.  |  **Note** |  This value on fatal errors is not supported on Cisco UCS C225 M8, Cisco UCS C245 M8, and X215c M8 servers.   
---|---  
  * on fatal and non-fatal errors—eDPC is enabled for both fatal and non-fatal errors. 


  
Multikey Total Memory Encryption (MK-TME) scope token-feature "Processor" scope token-param EnableMktme |  MK-TME allows you to have multiple encryption domains with one with own key. Different memory pages can be encrypted with different keys. This can be one of the following: 

  * enabled—Support is enabled. This is the default option. 
  * disabled—Support is disabled. 

  
SW Guard Extensions (SGX) scope token-feature "Processor" scope token-param EnableSgx |  Allows you to enable Software Guard Extensions (SGX) feature. This can be one of the following:

  * enabled—Support is enabled. 
  * disabled—Support is disabled. 

  
Total Memory Encryption (TME) scope token-feature "Processor" scope token-param EnableTme |  Allows you to provide the capability to encrypt the entirety of the physical memory of a system. This can be one of the following: 

  * enabled—Support is enabled. This is the default option. 
  * disabled—Support is disabled. 

  
Select Owner EPOCH input type scope token-feature "Processor" scope token-param EpochUpdate |  Allows you to change the seed for the security key used for the locked memory region that is created. This can be one of the following: 

  * sgx owner epoch activated— Does not change the current input type. 
  * change to new random owner epochs—Changes EPOCH to a system generated random number 
  * manual user defined owner epochs—Changes the EPOCH seed to a hexadecimal value that you enter. 

  
Enhanced CPU Performance scope token-feature "CpuPerfEnhancement" scope token-param CpuPerfEnhancement |  Enhances CPU performance by adjusting server settings automatically. This can be one of the following:

  * disabled—The processor does not run with this functionality. This is the default option. 
  * auto—Allows to adjust server settings to increase the processor performance. 

|  **Note** | 

  * Enabling this functionality may increase power consumption.
  * The server should meet the following requirements in order to use this functionality:
  * The server should not contain Barlow Pass DIMMs.
  * DIMM module size present in the Cisco UCS C220 M6 server should be less than 64GB and in Cisco UCS C240 M6 server should be less than 256GB. 
  * No GPU cards are present in the server. 

  
---|---  
UPI Link Enablement scope token-feature "UPI Link Enablement" scope token-param UPILinkEnablement |  Enables the number of Ultra Path Interconnect (UPI) links required by the processor. This can be one of the following

  * auto—This is the default option. 
  * 1
  * 2

  
UPI Power Manangement scope token-feature "UPI Power Manangement" scope token-param UPIPowerManagement |  The UPI power management can be used for conserving power on the server. This can be one of the following:

  * enabled—Enables the processor to support this functionality. 
  * disabled—Disables the processor to support this functionality. This is the default option. 

  
C1 Auto UnDemotion scope token-feature "C1 Auto UnDemotion" scope token-param C1AutoDemotion |  Select whether to enable processors to automatically undemote from C1. This can be one of the following:

  * auto— This is the default option. 
  * enabled—Enables the processor to support this functionality. 
  * disabled—Disables the processor to support this functionality. 

  
C1 Auto Demotion scope token-feature "C1 Auto Demotion" scope token-param C1AutoDemotion |  If enabled, CPU automatically demotes to C1 based on un-core auto-demote information. This can be one of the following:

  * auto— This is the default option. 
  * enabled—Enables the processor to support this functionality. 
  * disabled—Disables the processor to support this functionality. 

  
CPU Downcore control 7xx3 scope token-feature "Processor" scope token-param CbsCpuCoreCtrl |  Provides the ability to remove one or more cores from operation is supported in the silicon. It may be desirable to reduce the number of cores due to OS restrictions, or power reduction requirements of the system. This item allows the control on the number of cores that are running. This setting can only reduce the number of cores from only those available in the processor. This can be one of the following: 

  * auto—The CPU determines how many cores need to be enabled. This is the default option 
  * one (1+0)—One core enabled on one CPU complex 
  * two (2+0)—Two core enabled on one CPU complex 
  * three (3+0)—Three core enabled on one CPU complex. 
  * four (4+0)—Four core enabled on one CPU complex. 
  * five (5+0)—Five core enabled on one CPU complex 
  * six (6+0)—Six core enabled on one CPU complex 
  * seven (7+0)—Seven core enabled on one CPU complex 

|  **Note** |  This token is applicable only for the servers with 7xx3 Model processors.  
---|---  
Fixed SOC P-State scope token-feature "Processor" scope token-param CbsCmnFixedSocPstate |  This option defines the target P-state when APBDIS (to disable Algorithm Performance Boost (APB)) is set. The P-x specify a valid P-state for the processor installed. This can be one of the following: 

  * auto—Sets a valid P-state suitable for the processor. This is the default option. 
  * p0—Highest-performing SOC P-state 
  * p1—Next-highest-performing SOC P-state 
  * p2—Next-highest-performing SOC P-state 
  * p3—Minimum SOC power P-state 

  
APBDIS scope token-feature "Processor" scope token-param CbsCmnApbdis |  Allows you to select the Algorithm Performance Boost (APB) Disable value for the SMU. This can be one of the following:

  * auto—Sets an auto ApbDis for the SMU. This is the default option. 
  * 0—Clear ApbDis to SMU 
  * 1—Set ApbDis to SMU 

  
CCD Control set CbsCpuCcdCtrlSsp |  Allows you to specify the number of charge-coupled device CCDs that are desired to be enable in the system. This can be one of the following: 

  * auto—The maximum CCDs provided by the processor is enabled. This is the default option. 
  * 2 ccds
  * 4 ccds
  * 6 ccds
  * 8 ccds
  * 10 ccds
  * 12 ccds
  * 14 ccds

  
Cisco xGMI Max Speed scope token-feature "Processor" scope token-param CiscoXgmiMaxSpeed |  This option enables 18 Gbps XGMI link speed. This can be one of the following:

  * disabled—The feature is disabled. This is the default option. 
  * enabled—The feature is enabled. 

  
ACPI SRAT L3 Cache As NUMA Domain scope token-feature "Processor" scope token-param CbsDfCmnAcpiSratL3Numa |  Creates a layer of virtual domains on top of the physical domains in which each CCX is declared to be in its on domain. This can be one of the following: 

  * auto—Set to auto mode. This is the default option. 
  * disabled—Use NPS settings for domain configuration. 
  * enabled—Each CCX is declared to be in its own domain. 

  
Streaming Stores Control scope token-feature "Processor" scope token-param CbsCmnCpuStreamingStoresCtrl |  Enables the streaming stores functionality. This can be one of the following:

  * auto—Set to auto mode. This is the default option. 
  * disabled—Feature is disabled. 
  * enabled—Feature is enabled. 

  
DF C-States scope token-feature "Processor" scope token-param CbsCmnGnbSMUDfCstates |  When long duration idleness is expected in a system, this control allows the system to transition into a DF Cstate which can set the system into an even lower power state. This can be one of the following: 

  * auto—Set to auto mode. This is the default option. 
  * disabled—This option is turned off, long period of idleness are not expected so no power savings would be achieved. 
  * enabled—This option is active, saving power when the system is idle. 

  
SEV-SNP Support set CbsSevSnpSupport |  Allows you to enable Secure Nested Paging feature. This can be one of the following:

  * disabled—The processor does not use the SEV-SNP function. 
  * enabled—The processor uses the SEV-SNP function. 
  * auto. This is the default option.

  
Efficiency Mode Enable scope token-feature "Processor" scope token-param CbsCmnEfficiencyModeEn |  Allows you to configure power consumption based on efficiency. This can be one of the following:

  * auto—The CPU automatically uses default settings. This is the default option. 
  * enabled—Efficiency mode is enabled. 

  
SNP Memory Coverage scope token-feature "Processor" scope token-param CbsDbgCpuSnpMemCover |  Allows you to configure SNP memory coverage. This can be one of the following:

  * auto—System decides the memory coverage. This is the default option. 
  * disabled—The processor does not use this function. 
  * enabled—This feature is enabled. 
  * custom—Custom size can be defined in SNP Memory Size to Cover. 

  
SNP Memory Size to Cover in MB scope token-feature "Processor" scope token-param CbsDbgCpuSnpMemSizeCover |  Allows you to configure SNP memory size.  The value can range from 0-1048576. The value 8192 is the default option.  
CPCC scope token-feature "Processor" scope token-param CbsCmnGnbSMUCPPC |  Allows you to configure Collaborative Processor Performance Control. This can be one of the following:

  * auto—The CPU automatically uses default CPPC settings. This is the default option. 
  * disabled—Feature is disabled. 
  * enabled—Collaborative Processor Performance is enabled. 

  
Downcore control 7xx2 scope token-feature "Processor" scope token-param CbsCmnCpuGenDowncoreCtrl |  The ability to remove one or more cores from operation is supported in the silicon. It may be desirable to reduce the number of cores due to OS restrictions, or power reduction requirements of the system. This item allows the control of how many cores are running. This setting can only reduce the number of cores from those available in the processor. This can be one of the following: 

  * auto—The CPU determines how many cores need to be enabled. This is the default option. 
  * two (1+1)—Two cores enabled on one CPU complex. 
  * four (2+2)—Four cores enabled on one CPU complex. 
  * six (3+3)—Six cores enabled on one CPU complex. 

  
Processor EPP Profile  set processor epp profile |  Allows you to determine whether system performance or energy efficiency is more important on this server. This can be one of the following: 

  * performance
  * balanced performance—This is the default option. 
  * balanced power
  * power

  
Autonomous Core C-state set processor autonomous core c-state |  Enables CPU Autonomous C-State, which converts the HALT instructions to the MWAIT instructions. This can be one of the following:

  * disabled—This is the default option. 
  * enabled

  
Energy Efficient Turbo set energy efficient turbo |  When energy efficient turbo is enabled, the optimal turbo frequency of the CPU turns dynamic based on CPU utilization. The power/performance bias setting also influences energy efficient turbo. This can be one of the following: 

  * disabled—This is the default option. 
  * enabled

  
Hardware P-States set hardware p-states |  Enables processor Hardware P-State. This can be one of the following:

  * disabled—HWPM is disabled. 
  * hwpm native modeHWPM Native Mode—HWPM native mode is enabled. This is the default option. 
  * hwpm oob modeHWPM OOB Mode—HWPM Out-of-Box mode is enabled. 
  * native mode with no legacyNative Mode with no Legacy

  
Energy/Performance Bias Config set energy/performance |  Allows you to determine whether system performance or energy efficiency is more important on this server. This can be one of the following: 

  * performance—The server provides all server components with full power at all times. This option maintains the highest level of performance and requires the greatest amount of power. 
  * balaced performanceBalanced Performance—The server provides all server components with enough power to keep a balance between performance and power. This is the default option. 
  * balaced powerBalanced Power—The server provides all server components with enough power to keep a balance between performance and power. 
  * powerPower—The server provides all server components with maximum power to keep reduce power consumption. 

  
Power Performance Tuning set power performance |  Determines if the BIOS or Operating System can turn on the energy performance bias tuning. The options are BIOS and OS. This can be one of the following: 

  * bios—Chooses BIOS for energy performance tuning. 
  * osOS—Chooses OS for energy performance tuning. This is the default option. 
  * peciPECI—Chooses PECI for energy performance tuning. 

  
Cores Enabled set cores enabled |  Allows you to disable one or more of the physical cores on the server. This can be one of the following:

  * all—Enables all physical cores. This also enables Hyper Threading on the associated logical processor cores. 
  * 1 through 481 through 48—Specifies the number of physical processor cores that can run on the server. Each physical core has an associated logical core. 

  
Hyper-Threading [All] set hyper-threading-all |  Whether the processor uses Intel Hyper-Threading Technology, which allows multithreaded software applications to execute threads in parallel within each processor. This can be one of the following: 

  * disabled—The processor does not permit hyperthreading. 
  * enabledEnabled—The processor allows for the parallel execution of multiple threads. 

  
SpeedStep (Pstates) set speedstep (pstates) |  Whether the processor uses Enhanced Intel SpeedStep Technology, which allows the system to dynamically adjust processor voltage and core frequency. This technology can result in decreased average power consumption and decreased average heat production. This can be one of the following: 

  * disabled—The processor never dynamically adjusts its voltage or frequency. 
  * enabledEnabled—The processor utilizes Enhanced Intel SpeedStep Technology and enables all supported processor sleep states to further conserve power. 

  
Boot Performance Mode set boot performance mode |  Allows the user to select the BIOS performance state that is set before the operating system handoff. This can be one of the following: 

  * max performance—Processor P-state ratio is maximum. 
  * max efficientMax Efficient—Processor P-state ratio is minimum. 
  * set by intel nmSet by Intel NM—Processor P-state ratio is set by Intel. 

  
EIST PSD Function set eist psd function |  EIST reduces the latency inherent with changing the voltage-frequency pair (P-state), thus allowing those transitions to occur more frequently. This allows for more granular, demand-based switching and can optimize the power-to-performance balance, based on the demands of the applications. This can be one of the following: 

  * hw all—The processor is coordinates the P-state among logical processors dependencies. The OS keeps the P-state request up to date on all logical processors. This is the default option. 
  * sw all—The OS Power Manager coordinates the P-state among logical processors with dependencies and initiates the transition on all of those Logical Processors. 

  
Turbo Mode set eist psd function |  Whether the processor uses Intel Turbo Boost Technology, which allows the processor to automatically increase its frequency if it is running below power, temperature, or voltage specifications. This can be one of the following: 

  * disabled—The processor does not increase its frequency automatically. 
  * enabled—The processor utilizes Turbo Boost Technology if required. This is the default option. 

  
Extended APIC set extended apic |  Allows you to enable or disable extended APIC support. This can be one of the following:

  * disabled—This is the default option. 
  * enabled. 

  
Memory Interleaving Size set memory interleaving |  Determines the size of the memory blocks to be interleaved. It also determines the starting address of the interleave (bit 8, 9 , 10 or 11). This can be one of the following: 

  * 1 KB
  * 2 KB
  * 4 KB
  * 256 Bytes
  * 512 Bytes
  * auto—The CPU determines the size of the memory block. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
UPI Link Frequency Select set upi link frequency select |  Allows you to enable or disable extended APIC support. This can be one of the following:

  * auto—This option configures the optimal link speed automatically. This is the default option. 
  * 9.6gt/s—This option configures the optimal link speed at 9.6GT/s. 
  * 10.4gt/s—This option configures the optimal link speed at 10.4GT/s. 
  * 11.2gt/s—This option configures the optimal link speed at 10.4GT/s. 
  * 12.8gt/s—This option configures the optimal link speed at 12.8GT/s. 
  * 14.4gt/s—This option configures the optimal link speed at 14.4GT/s. 
  * 16.0gt/s—This option configures the optimal link speed at 16.0GT/s. 
  * 20.0gt/s—This option configures the optimal link speed at 20.0GT/s. 

  
X2APIC Opt Out set X2ApicOptOut |  Prevents the OS from enabling extended xAPIC (x2APIC) mode when the OS is not working with x2APIC. This can be one of the following: 

  * disabled—Use the Extended xAPIC (x2APIC) mode. This is the default option. 
  * enabled—Opt out from Extended xAPIC (x2APIC) mode. 

  
Optimized Power Mode set OptimizedPowerMode |  Automatically varies processor speed and _power_ usage based on processor utilization. This can be one of the following: 

  * disabled—The processor does not vary the speed automatically. 
  * enabled—The processor varies the speed automatically. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Burst and Postponed Refresh scope token-feature "Processor" scope token-param BurstAndPostponedRefresh |  Allows the memory controller to defer the refresh cycles when the memory is active and accomplishes the refresh within a specified window. The deferred refresh cycles may run in a burst of several refresh cycles. This can be one of the following: 

  * enabled
  * disabled—This is the default option.  |  **Note** |  It is recommended to leave this setting in the default state of disabled to mitigate Rowhammer-style attacks.   
---|---  

  
NUMA Nodes per Socket set CbsDfCmnDramNps |  Allows you to configure the memory NUMA domains per socket. This can be one of the following:

  * auto—Number of channels is set to auto. This is the default option. 
  * nps0—Zero NUMA node per socket. 
  * nps1—One NUMA node per socket. 
  * nps2—Two NUMA nodes per socket, one per Left/Right Half of the SoC. 
  * nps4—Four NUMA nodes per socket, one per Quadrant. 

  
DRAM SW Thermal Throttling scope token-feature "Processor" scope token-param DramSwThermalThrottling |  Provides a protective mechanism to ensure that the software functions within the temperature limits. When the temperature exceeds the maximum threshold value, the performance is permitted to drop allowing to cool down to the minimum threshold value. This can be one of the following: 

  * enabled
  * disabled—This is the default option.  |  **Note** |  It is recommended to leave this setting in the default state of disabled to mitigate Rowhammer-style attacks.   
---|---  

  
Operation Mode scope token-feature "operation mode" |  Allows you to set the Operation Mode. This can be one of the following:

  * test only—Support is enabled. 
  * test and repair—Support is disabled. 

  
Secure Encrypted Virtualization (SEV) scope token-feature "Processor" scope token-param SEV |  Enables running encrypted virtual machines (VMs) in which the code and data of the VM are isolated. This can be one of the following: 

  * 253 ASIDs
  * 509 ASIDs
  * auto—This is the default option.  |  **Note** |  It is recommended to leave this setting in the default state of auto to mitigate Rowhammer-style attacks.   
---|---  

  
Transparent Secure Memory Encryption (TSME) set tsme |  Provides transparent hardware memory encryption of all data stored on system memory. This can be one of the following:

  * enabled
  * disabled
  * auto—This is the default option.  |  **Note** |  It is recommended to leave this setting in the default state of auto to mitigate Rowhammer-style attacks.   
---|---  

  
AVX512 set CbsCmnCpuAvx512 |  The AVX-512 BIOS setting enables or disables the use of AVX-512 instruction set extensions, which are advanced vector extensions used by certain Intel® processors to improve performance for heavy computational tasks Adjusting this setting can affect compatibility and stability with some software, as well as influence CPU power consumption and heat output. This can be one of the following: 

  * enabled
  * disabled
  * auto—This is the default option. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SEV-ES ASID Space Limit |  The SEV-ES ASID Space Limit BIOS setting determines the number of ASIDs for AMD® SEV-ES, affecting VM memory encryption and isolation. Adjusting it balances security needs with system resources.  Enter an integer between 1 and 1007.  
Power Profile Selection F19h set CbsCmnEfficiencyModeEnRs |  The Power Profile Selection F19h BIOS setting allows users to choose a predefined power management profile tailored for specific performance or energy efficiency goals on AMD® Family 19h processors. This setting optimizes the CPU power consumption and performance characteristics based on the selected profile.  This can be one of the following:

  * high performance mode—Maximizes CPU performance without prioritizing power savings. This is the default option. 
  * efficiency mode—Prioritizes energy efficiency and lower power consumption over performance. 
  * maximum io performance mode—Prioritizes the input/output (IO) performance. 
  * balanced memory performance—Offers a compromise between performance and power efficiency. 
  * balanced core performance mode—Balances core performance with power efficiency. 
  * balanced core memory performance mode—Balances both core and memory performance with power efficiency. 
  * auto—Automatically balances performance and power efficiency.  |  **Note** |  The values such as balanced core performance mode, balanced core memory performance mode, and auto are applicable only for 5th Generation AMD® EPYC® 9xx5 processors.   
---|---  
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 


  
Power Down Enable |  This setting controls whether the memory (RAM) can enter a low power state when the system is idle or during periods of low usage. Enabling this setting typically allows the RAM to consume less power, potentially saving energy and reducing heat output, while disabling it keeps the RAM fully powered for possibly quicker wake-up times at the expense of higher power consumption. This can be one of the following: 

  * enabled
  * disabled
  * auto—This is the default option. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
xGMI Force Link Width |  This setting allows users to manually specify the number of lanes used for the xGMI (Inter-chip Global Memory Interconnect) link width to x4/x8/x16.  This can be one of the following:

  * 0 \- Force xGMI link width to x4. 
  * 1 \- Force xGMI link width to x8. 
  * 2 \- Force xGMI link width to x16. 
  * Auto \- Use the default xGMI link width controller settings. This is the default option. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
DF PState Frequency Optimizer set CbsCmnGnbSMUDffoRs |  Enable or Disable DF Pstate CCLK effective frequency optimizer.

  * enabled
  * disabled
  * auto—This is the default option. 

  
Fixed SOC P-State SP5 F19h set CbsCmnApbdisDfPstateRs |  Forced P-State to be independent/Dependent, as reported by the ACPI _PSD object. It will change SOC PState if APBDIS is enable. The valid range is (0-2).  
4-link xGMI max speed set CbsDfCmn4LinkMaxXgmiSpeed |  Specifies the max frequency used for XGMI PState in a 4-link topology.

  * 20Gbps
  * 25Gbps
  * 30Gbps
  * auto—This is the default option. 

  
CPU Downcore control F19 M10h-1Fh scope CbsCpuDownCoreCtrl scope CbsCpuDownCoreCtrlf19autom10h-1fh |  Enables manage the number of active cores on AMD® Family 19h processors. This token can be used to optimize performance, power consumption, or compatibility based on specific needs. F refers to the processor family and M refers to the model. The available options include: 

  * auto—The system automatically selects the optimal number of active cores based on the current workload and system configuration. This is the default option. 
  * one (1_+_0) — Enables only one core per CPU. 
  * two (2_+_0)—Enables two cores per CPU. 
  * three (3_+_0) —Enables three cores per CPU. 
  * four (4_+_0) —Enables four cores per CPU. 
  * five (5_+_0) —Enables five cores per CPU. 
  * six_(6_+_0) —Enables six cores per CPU. 
  * seven (7_+_0) —Enables seven cores per CPU. 
  * eight (8_+_0) —Enables eight cores per CPU. 
  * nine(9_+_0) —Enables nine cores per CPU. 
  * ten(10_+_0) —Enables ten cores per CPU. 
  * eleven (11_+_0) —Enables eleven cores per CPU. 
  * twelve (12_+_0) —Enables twelve cores per CPU. 
  * thirteen (13_+_0) —Enables thirteen cores per CPU. 
  * fourteen (14_+_0) —Enables fourteen cores per CPU. 
  * fifteen (15_+_0) —Enables fifteen cores per CPU. 

|  **Note** |  The values from _Eight (8_+_0)_ to _Fifteen (15_+_0)_ are applicable only for 5th Generation AMD® EPYC® 9xx5 processors.   
---|---  
Downcore control F19 MA0h-AFh scope CbsCpuDownCoreCtrl scope CbsCpuDownCoreCtrlf19maoh-afh |  F refers to the processor family and M denotes the model.

  * auto—This is the default option. 
  * two (1_+_1)
  * four (2_+_2) 
  * six (3_+_3) 
  * eight (4_+_4) 
  * ten (5_+_5) 
  * twelve (6_+_6) 
  * fourteen (7_+_7) 

  
Latency Optimized Mode Configuration set LatencyOptimizedMode |  This setting controls the Latency Optimized Mode, which is designed to minimize latency in processing tasks on supported platforms. This can be one of the following: 

  * disabled—Activates the Latency Optimized Mode, reducing latency for processing tasks. 
  * enabled—The mode is inactive, and latency reduction is not applied. 

  
  
###  I/O BIOS Settings for Intel

The following table lists the Intel Directed I/O BIOS settings that you can configure through a BIOS policy or the default BIOS settings: 

Name  | Description   
---|---  
Intel VT for directed IO set intel-vt-directed-io-config vtd |  Whether the processor uses Intel Virtualization Technology for Directed I/O (VT-d). This can be one of the following: 

  * disabled—The processor does not use virtualization technology. 
  * enabled—The processor uses virtualization technology. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

|  **Note** |  This option must be enabled if you want to change any of the other Intel Directed I/O BIOS settings.   
---|---  
Intel VTD interrupt Remapping set intel-vt-directed-io-config interrupt-remapping |  Whether the processor supports Intel VT-d Interrupt Remapping. This can be one of the following: 

  * disabled—The processor does not support remapping. 
  * enabled—The processor uses VT-d Interrupt Remapping as required. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Intel VTD coherency support set intel-vt-directed-io-config coherency-support |  Whether the processor supports Intel VT-d Coherency. This can be one of the following: 

  * disabled—The processor does not support coherency. 
  * enabled—The processor uses VT-d Coherency as required. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Intel VTD ATS support set intel-vt-directed-io-config ats-support |  Whether the processor supports Intel VT-d Address Translation Services (ATS). This can be one of the following: 

  * disabled—The processor does not support ATS. 
  * enabled—The processor uses VT-d ATS as required. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Intel VTD pass through DMA support set intel-vt-directed-io-config passthrough-dma |  Whether the processor supports Intel VT-d Pass-through DMA. This can be one of the following: 

  * disabled—The processor does not support pass-through DMA. 
  * enabled—The processor uses VT-d Pass-through DMA as required. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
  
### I/O BIOS Settings for AMD

The following table lists the Input/Output BIOS settings that you can configure through a BIOS policy for AMD: 

Name  | Description   
---|---  
PCIe ARI Support scope token-feature "PCIe ARI Support" scope token-param "PCIeARISupport" |  The PCIe Alternative Routing ID (ARI) Interpretation feature specification supports greater numbers of virtual funtions through the implementation of ARI, which reinterprets the device number field in the PCIe header allowing for more than eight functions. This can be one of the following: 

  * disabled—PCIe ARI Support is not available. 
  * enabled—PCIe ARI Support is available. 
  * auto—PCIe ARI Support is in auto mode. This is the default option. 

  
IPv4 PXE Support scope token-feature "IPv4 PXE Support" scope token-param "IPv4PXESupport" |  Enables or disables IPv4 support for PXE. This can be one of the following:

  * disabled—IPv4 PXE support is not available. 
  * enabled—IPv4 PXE support is available. This is the default option. 

  
IPv6 HTTP Support scope token-feature "HTTP BOOT" scope token-param "IPV6HTTP" |  Enables or disables IPv6 support for HTTP. This can be one of the following:

  * disabled—IPv6 HTTP support is not available. 
  * enabled—IPv6 HTTP support is available. This is the default option. 

  
Network Stack scope token-feature "Network Stack" scope token-param "NetworkStack" |  This option allows you to monitor IPv6 and IPv4. This can be one of the following

  * disabled—Network Stack support is not available.  |  **Note** |  When disabled, the value set for IPV4 PXE Support does not impact the system.   
---|---  
  * enabled—Network Stack support is available. This is the default option. 


**Note** |  When Network Stack token value is Disabled, the below tokens and their values are also set

  * IPV4PXE - Disabled
  * IPV4HTTP - Disabled
  * IPV6HTTP - Disabled

  
---|---  
SR-IOV Support scope token-feature "sriov" scope token-param "sriov-support" |  Whether SR-IOV (Single Root I/O Virtualization) is enabled or disabled on the server. This can be one of the following:

  * enabled—SR-IOV is enabled. This is the default option. 
  * disabled—SR-IOV is disabled. 

  
Re-size BAR Support set ResizeBarSupport |  Allows to enable or disable re-sizable BAR support setup. This can be one of the following:

  * enabled—This is the default option. 
  * disabled

  
PreBoot DMA Protection Configuration drop-down list  set PreBootDMAProtection |  Controls the PreBoot Direct Memory Access (DMA) Protection feature. This feature is used for protecting the system from unauthorized DMA access during the pre-boot phase. This can be one of the following: 

  * enabled—The system is protected from unauthorized DMA access during pre-boot. 
  * disabled—The system is not protected from unauthorized DMA access during pre-boot. This is the default option. 

  
  
### RAS Memory BIOS Settings 

The following table lists the RAS memory BIOS settings that you can configure through a BIOS policy or the default BIOS settings: 

Name  | Description   
---|---  
ACPI SRAT Special Purpose Memory Flag set AcpiSratSpFlagEn |  This setting allows or disallows the ACPI SRAT special purpose memory flag to be set when the UEFI Memory Map special purpose flag is enabled. This can be one of the following: 

  * disabled
  * enabled—This is the default option. 

  
UEFI Memory Map Special Purpose Memory Flag set UefiMemMapSpFlagEn |  This setting determines the behavior of the UEFI memory map special knob, which impacts CXL cards under certain operating systems. This can be one of the following: 

  * disabled
  * enabled—This is the default option. 

  
DRAM Scrub Time set CbsDfCmnDramScrubTime |  The value that represents the number of hours to scrub the whole memory. This can be one of the following:

  * Disabled—Disables the number of hours to scrub the whole memory. 
  * 1 hour, 4 hours, 6 hours, 8 hours, 12 hours, 16 hours, 24 hours, 48 hours—The number of hours to scrub the whole memory.12 hours is the default option.
  * auto—Automatically scrubs the whole memory. 

  
MMIO High Granularity Size set MmiohSize |  The MMIO High Granularity Size. This can be one of the following:

  * 1G, 4G, 16G, 64G, 256G, 1024G—The MMIO high granularity size. 1024G is the default option. 

  
MMIO High Base set MmiohBase |  The MMIO high base. This can be one of the following:

  * 512G, 1T, 2T, 4T, 16T, 24T, 32T, 40T, 56T—The MMIO high base. 32T is the default option. 

  
Error Check Scrub set ErrorCheckScrub |  An error check and scrub (ECS) mode enables a memory device to perform error checking and correction (ECC) and count errors. This can be one of the following: 

  * disabled—Does not collect any errors. 
  * Enabled_without_Result_Collection —Collects the errors without giving the results. 
  * Enabled_with_Result_Collection —Collects the errors with the results. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Rank Margin Tool set EnableRMT |  This provides automated memory margin testing and is used to identify DDR margins at the rank level. This can be one of the following: 

  * disabled—Does not identify the margins at the rank level. 
  * enabled—Identifies the margins at the rank level. 
  * platform-default —The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Partial Cache Line Sparing scope token-feature "Partial Cache Line Sparing" scope token-param PartialCacheLineSparing |  Partial cache line sparing (PCLS) is an error-prevention mechanism in memory controllers. PCLS statically encodes the locations of the faulty nibbles of bits into a sparing directory along with the corresponding data content for replacement during memory accesses. This can be one of the following: 

  * disabled—Support is disabled. 
  * enabled—Support is enabled. 

  
UMA  scope token feature "UMA" scope token-param UmaBasedClustering |  Allows you to set UMA settings. This can be one of the following:

  * disable-all2-all
  * hemisphere-2-clusters

  
Memory Thermal Throttling Mode scope token-feature "Memory Thermal Throttling Mode" scope token-param MemoryThermalThrottling |  Provides a protective mechanism to ensure the memory temperature is within the limits. When the temperature exceeds the maximum threshold value, the memory access rate is reduced and Baseboard Management Controller (BMC) adjusts the fan to cool down the memory to avoid DIMM damage due to overheat. This can be one of the following: 

  * CLTT with PECI —Closed Loop Thermal Throttling (CLTT) with Platform Environment Control Interface (PECI). This is the default option. 
  * disabled. 

|  **Note** |  It is recommended to leave this setting in the default state of CLTT with PECI   
---|---  
Enhanced Memory Test scope token-feature "Advanced Memory Test" scope token-param AdvancedMemTest |  Enables enhanced memory tests during the system boot and increases the boot time based on the memory. This can be one of the following: 

  * auto—This is the default option.  |  **Note** |  It is recommended to leave this setting in the default state of auto.   
---|---  
  * enabled

  * disabled


**Note** | 

  * This BIOS token name modified from Advanced Memory Test to Enhanced Memory Test for M6 servers. 

  
---|---  
Memory Refresh Rate scope token-feature "Memory Refresh Rate" scope token-param MemoryRefreshRate |  Controls the refresh rate of the memory controller and might affect the memory performance and power depending on memory configuration and workload. This can be one of the following: 

  * 1x-refresh
  * 2x-refresh—1.9us. This is the default option.

  
Panic and High Watermark scope token-feature "Panic and High Watermark" scope token-param PanicHighWatermark |  Controls the delayed refresh capability of the memory controller. This can be one of the following:

  * High—The memory controller is allowed to postpone up to a maximum of eight refresh commands. The memory controller executes all the postponed refreshes within the refresh interval. For the ninth refresh command, the refresh priority becomes Panic and the memory controller pauses the normal memory transactions until all the postponed refresh commands are executed. 
  * Low—This is the default option. The memory controller is not allowed to postpone refresh commands.  |  **Note** |  It is recommended to leave this setting in the default state (Low) which will help to reduce susceptibility to Rowhammer-style attacks.   
---|---  

  
Memory RAS configuration set memory-ras-config ras-config |  How the memory reliability, availability, and serviceability (RAS) is configured for the server. This can be one of the following: 

  * maximum-performance—Optimizes the system performance and disables all the advanced RAS features. 
  * lockstep—If the DIMM pairs in the server have an identical type, size, and organization and are populated across the SMI channels, you can enable lockstep mode to minimize memory access latency and provide better performance. Lockstep is enabled by default for B440 servers. 
  * Mirror Mode 1LM—Mirror Mode 1LM will set the entire 1LM memory in the system to be mirrored, consequently reducing the memory capacity by half. This mode is used for UCS M5 and M6 and M7blade servers. 
  * Partial Mirror Mode 1LM—Partial Mirror Mode 1LM will set a part of the 1LM memory in the system to be mirrored, consequently reducing the memory capacity by half. This mode is used for UCS M5 and M6 and M7blade servers. 
  * sparing—System reliability is optimized by holding memory in reserve so that it can be used in case other DIMMs fail. This mode provides some memory redundancy, but does not provide as much redundancy as mirroring. 
  * adddc-sparing—System reliability is optimized by holding memory in reserve so that it can be used in case other DIMMs fail. This mode provides some memory redundancy, but does not provide as much redundancy as mirroring. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
NUMA optimized set numa-config numa-optimization |  Whether the BIOS supports NUMA. This can be one of the following: 

  * disabled—The BIOS does not support NUMA. 
  * enabled—The BIOS includes the ACPI tables that are required for NUMA-aware operating systems. If you enable this option, the system must disable Inter-Socket Memory interleaving on some platforms. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Memory Interleaving set CbsDfCmnMemIntlvControl |  Allows you to disable the memory interleaving |  **Note** |  NUMA nodes per socket will be honored regardless of this setting.  
---|---  
  
  * enabled—The BIOS support NUMA. 

  * disabled—The BIOS does not support NUMA. 

  * Auto—This is the default option. 

  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Post Package Repair  scope token-feature "PostPackageRepair" scope token-param PostPackageRepair |  Post Package Repair (PPR) provides the ability to repair faulty memory cells by replacing them with spare cells. This can be one of the following: 

  * disabled—The BIOS does not support selecting PPR Type. 
  * hard-ppr—This results in a permanent remapping of damaged storage cells. This is the default option. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Memory Size Limit in GB set memory-size-limit |  Limits the capacity in Partial Memory Mirror Mode up to 50 percent of the total memory capacity. The memory size can range from 0 GB to 65535 GB in increments of 1 GB.   
Mirroring Mode set memory-mirroring-mode mirroring-mode |  Memory mirroring enhances system reliability by keeping two identical data images in memory.  This option is only available if you choose the mirroring option for Memory RAS Config. It can be one of the following: 

  * inter-socket—Memory is mirrored between two Integrated Memory Controllers (IMCs) across CPU sockets. 
  * intra-socket—One IMC is mirrored with another IMC in the same socket. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Sparing Mode set memory-sparing-mode sparing-mode |  Sparing optimizes reliability by holding memory in reserve so that it can be used in case other DIMMs fail. This option provides some memory redundancy, but does not provide as much redundancy as mirroring. The available sparing modes depend on the current memory population.  This option is only available if you choose sparing option for Memory RAS Config. It can be one of the following: 

  * dimm-sparing—One DIMM is held in reserve. If a DIMM fails, the contents of a failing DIMM are transferred to the spare DIMM. 
  * rank-sparing—A spare rank of DIMMs is held in reserve. If a rank of DIMMs fails, the contents of the failing rank are transferred to the spare rank. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
LV DDR Mode set lv-dimm-support-config lv-ddr-mode |  Whether the system prioritizes low voltage or high frequency memory operations. This can be one of the following: 

  * auto—The CPU determines whether to prioritize low voltage or high frequency memory operations. 
  * power-saving-mode—The system prioritizes low voltage memory operations over high frequency memory operations. This mode may lower memory frequency in order to keep the voltage low. 
  * performance-mode—The system prioritizes high frequency operations over low voltage operations. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
DRAM Refresh Rate set dram-refresh-rate-config dram-refresh |  The refresh interval rate for internal memory. This can be one of the following: 

  * 1x
  * 2x
  * 3x
  * 4x
  * auto
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
DDR3 Voltage Selection set ddr3-voltage-config ddr3-voltage |  The voltage to be used by the dual-voltage RAM. This can be one of the following: 

  * ddr3-1500mv
  * ddr3-1350mv
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Partial Memory Mirror Mode set memory-mirroring-mode mirroring-mode |  Partial Memory Mirroring enables you to partially mirror by GB or by a percentage of the memory capacity. Depending on the option selected here, you can define either a partial mirror percentage or a partial mirror capacity in GB in available fields. You can partially mirror up to 50 percent of the memory capacity. It can be one of the following: 

  * Disabled—Partial Memory Mode is disabled. This is the default option. 
  * Percentage—The amount of memory to be mirrored in the Partial Memory Mode is defined as a percentage of the total memory. 
  * Value in GB—The amount of memory to be mirrored in the Partial Memory Mode is defined in GB. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

|  **Note** |  Partial Memory Mirror Mode is mutually exclusive to standard Mirroring Mode.   
---|---  
  
Partial Mirrors 1-4 can be used in any number or configuration, provided they do not exceed the capacity limit set in GB or Percentage in the related options.   
  
Partial Mirror Percentage |  Limits the amount of available memory to be mirrored as a percentage of the total memory. This can range from 0.000.01 % to 50.00 % in increments of 0.01 %.   
Partial Mirror1 Size in GB |  Limits the amount of memory in Partial Mirror1 in GB. This can range from 0 GB to 65535 GB in increments of 1 GB.  
Partial Mirror2 Size in GB |  Limits the amount of memory in Partial Mirror2 in GB. This can range from 0 GB to 65535 GB in increments of 1 GB.  
Partial Mirror3 Size in GB |  Limits the amount of memory in Partial Mirror3 in GB. This can range from 0 GB to 65535 GB in increments of 1 GB.  
Partial Mirror4 Size in GB |  Limits the amount of memory in Partial Mirror4 in GB. This can range from 0 GB to 65535 GB in increments of 1 GB.  
Volatile Memory Mode scope token-feature "VolMemoryMode" scope token-param VolMemoryMode |  Allows the memory mode configuration. This can be any of the following:

  * 1lm—Configures 1 Layer Memory(1LM) 
  * 2lm—Configures 2 Layer Memory(1LM) 

  
Memory Bandwidth Boost scope token-feature "MemoryBandwidthBoost" scope token-param MemoryBandwidthBoost |  Allows to boost the memory bandwidth. This can be one of the following:

  * enabled
  * disabled

  
LLC Dead Line scope token-feature "LLC Dead Line" scope token-param LLCAlloc |  In CPU non-inclusive cache scheme, Mid-Level Cache (MLC) evictions are filled into the Last-Level Cache (LLC). When lines are evicted from the MLC, the core can flag them as dead (not likely to be read again). The LLC has the option to drop dead lines and not fill them in the LLC. This can be one of the following: 

  * enabled—Allows the LLC to fill dead lines into the LLC if there is free space available. This is the default option. 
  * disabled—The dead lines are always dropped and are never filled into the LLC. 
  * auto—The CPU determines the LLC dead line allocation 

  
XPT Remote Prefetch scope token-feature "XPT Remote Prefetch" scope token-param XPTRemotePrefetch |  This feature allows an LLC request to be duplicated and sent to an appropriate memory controller in a remote machine based on the recent LLC history to reduce latency. This can be one of the following: 

  * enabled
  * disabled
  * auto—The CPU determines the functionality. This is the default option. 

  
Virtual NUMA scope token-feature "Virtual Numa" scope token-param VirtualNuma |  The Virtual NUMA (virtual non-uniform memory access) is a memory-access optimization method for VMware virtual machines (VMs), which helps prevent memory-bandwidth bottlenecks. This can be one of the following: 

  * enabled—The functionality is enabled. 
  * disabled—The functionality is disabled. This is the default option. 

  
Above 4G Decoding scope token-feature "Above 4G Decoding" scope token-param Above 4G Decoding |  Enables or disables MMIO above 4GB or not. This can be one of the following:

  * enabled—The server maps I/O of 64-bit PCI devices to 4GB or greater address space. This is the default option. 
  * disabled—The server does not map I/O of 64-bit PCI devices to 4GB or greater address space. 

  
Select PPR Type scope token-feature "select ppr type" |  Supports **Hard-PPR** , which permanently remaps accesses from a designated faulty row to a designated spare row. 

  * hard ppr—Support is enabled. This is the default option.  |  **Note** |  Hard PPR can be used only when **Memory RAS Configuration** is set to **ADDDC Sparing**. For other RAS selections, this setting should be set to **Disabled**.   
---|---  
  * disabled—Support is disabled. 


  
Select Memory RAS Configuration scope token-feature "select memory ras configuration" |  Determines how the memory reliability, availability, and serviceability (RAS) is configured for the server. This can be one of the following: 

  * Mirror Mode 1LM—System reliability is optimized by using half the system memory as backup. 
  * ADDDC sparing—Adaptive virtual lockstep is an algorithm implemented in the hardware and firmware to support the ADDDC mode. When selected, the system performance is optimized till the algorithm is activated. The algorithm is activated in case of DRAM device failure. Once the algorithm is activated, the virtual lockstep regions are activated to map out the failed region during run-time dynamically, and the performance impact is restricted at a region level. This is the default option. 
  * Partial Mirror Mode 1LM—Partial DIMM Mirroring creates a mirrored copy of a specific region of memory cells, rather than keeping the complete mirror copy. Partial Mirroring creates a mirrored region in memory map with the attributes of a partial mirror copy. Up to 50% of the total memory capacity can be mirrored, using up to 4 partial mirrors. 
  * maximum performance—System performance is optimized. 

  
NUMA scope token-feature "numa" |  Whether the BIOS supports Non-Uniform Memory Access (NUMA). This can be one of the following:

  * enabled—Support is enabled. 
  * disabled—Support is disabled. 

  
CR FastGo Config set CrfastgoConfig  |  CR FastGo Config improves DDRT non-temporal write bandwidth when FastGO is disabled. When FastGO is enabled, it gives faster flow of NT writes into the uncore, When FastGO is disabled, it lessens NT writes queueing up in the CPU uncore, thereby improving sequentially at DCPMM, resulting in improved bandwidth.  Applies to all Cisco UCS M5 and Cisco UCS M6 servers.  The values can be one of the following:

  * auto—Same as Option 1. Disables FastGO. Recommended for DDRT. This is the default option (not Default). 
  * default—Enables FastGO. 
  * option 1—Disables FastGO. 
  * option 2, option 3, option 4, option 5—Not applicable. 
  * enable optimization
  * disable optimization

|  **Note** |  The values enable optimization, disable optimization, and auto are supported on Cisco UCS M6 servers   
---|---  
CR QoS set crqos |  Prevents DRAM and overall system BW drop in the presence of concurrent DCPMM BW saturating threads, with minimal impact to homogenous DDRT-only usages, Good for multi-tenant use cases, VMs, etc. Targeted for App Direct, but also improves memory mode. Targets the “worst-case” degradations.  Applies to all M5 and M6 servers.  The values can be one of the following:

  * disabled—Feature disabled. This is the default option. 
  * recipe 1—6 modules, 4 modules per socket optimized 
  * recipe 2—2 modules per socket optimized 
  * recipe 3—1 module per socket optimized 
  * mode 0 - disable the pmem qos feature
  * mode 1 - m2m qos enable;cha qos disable
  * mode 2 - m2m qos enable;cha qos enable

|  **Note** |  The values disabled, recipe 1, recipe 2, and recipe 3recipe 4 are not supported on Cisco UCS M6 servers   
---|---  
eADR Support scope token-feature "EadrSupport" scope token-param EadrSupport |  Extended asynchronous DRAM refresh (eADR) ensures that CPU caches lines with data are flushed at the right time and in the desired order and are also included in the power fail protected domain. This can be any of the following: 

  * enabled
  * disabled
  * auto—This is the default option. 

  
NVM Performance Setting  set NvmdimmPerformConfig  |  NVM Performance Setting  enables efficient major mode arbitration between DDR and DDRT transactions on the DDR channel to optimize channel BW and DRAM latency.  Applies to all M5 and M6 servers.  The values can be one of the following:

  * BW Optimized—Optimized for DDR and DDRT BW. This is the default option. 
  * Latency Optimized—Better DDR latency in the presence of DDRT BW. 
  * Balanced Profile—Optimized for Memory mode. 

  
Snoopy mode for 2LM set SnoopyModeFor2LM  |  Enables snoop-mode for DCPMM accesses while maintaining directory on all DRAM accesses. Snoops maintain cache coherence between sockets. Directory reduces snoops by keeping the remote node information locally (in memory). Directory lookups and updates add memory traffic.  Directory is a good tradeoff for DRAM, but not necessarily for DCPMM. For non-NUMA workload, when the feature is enabled, directory updates to DCPMM are eliminated, thereby helping DDRT bandwidth bound workloads. Directory is disabled for far memory accesses and instead snoops remote sockets to check for ownership. Directory is used only for DRAM (near memory). 

  * enabled
  * disabled—This is the default option. 

  
Snoopy mode for AD set SnoopyModeForAD  |  Enables snoop-mode for DCPMM accesses while maintaining directory on all DRAM accesses. Snoops maintain cache coherence between sockets. Directory reduces snoops by keeping the remote node information locally (in memory). Directory lookups and updates add memory traffic.  Directory is a good tradeoff for DRAM, but not necessarily for DCPMM. For non-NUMA workload, when the feature is enabled, directory updates to DCPMM are eliminated, thereby helping DDRT bandwidth bound workloads. Directory is disabled for accesses to AD and instead snoops remote sockets to check for ownership. Directory is used only for DRAM accesses. 

  * enabled
  * disabled—This is the default option. 

  
CBS_Cmn_Cpu_Sev_Asid_Space_Limit  set CBS_Cmn_Cpu_Sev_Asid_Space_Limit  |  The SEV-ES and SNP guests must use ASIDs in the range 1 through 1007. 

  * 1—This is the default option. 
  * 1007

  
Runtime Post Package Repair  set RuntimePostPackageRepair |  Enables the soft post-package repairs of the corrected memory errors during OS runtime.

  * disabled—This is the default option. 
  * enabled

  
  
### Intel® OptaneTM DC Persistent Memory (DCPMM) BIOS Tokens 

The following table lists the Intel® OptaneTM DC Persistent Memory (DCPMM) BIOS settings that you can configure through a BIOS policy or the default BIOS settings: 

Name  | Description   
---|---  
NVM Performance Setting  set NvmdimmPerformConfig  |  NVM Performance Setting  enables efficient major mode arbitration between DDR and DDRT transactions on the DDR channel to optimize channel BW and DRAM latency.  Applies to all M5 and M6 servers.  The values can be one of the following:

  * BW Optimized—Optimized for DDR and DDRT BW. This is the default option. 
  * Latency Optimized—Better DDR latency in the presence of DDRT BW. 
  * Balanced Profile—Optimized for Memory mode. 

  
CR QoS set crqos |  Prevents DRAM and overall system BW drop in the presence of concurrent DCPMM BW saturating threads, with minimal impact to homogenous DDRT-only usages, Good for multi-tenant use cases, VMs, etc. Targeted for App Direct, but also improves memory mode. Targets the “worst-case” degradations.  Applies to all M5 and M6 servers.  The values can be one of the following:

  * disabled—Feature disabled. This is the default option. 
  * recipe 1—6 modules, 4 modules per socket optimized 
  * recipe 2—2 modules per socket optimized 
  * recipe 3—1 module per socket optimized 
  * mode 0 - disable the pmem qos feature
  * mode 1 - m2m qos enable;cha qos disable
  * mode 2 - m2m qos enable;cha qos enable

|  **Note** |  The values disabled, recipe 1, recipe 2, and recipe 3recipe 4 are not supported on Cisco UCS M6 servers   
---|---  
CR FastGo Config set CrfastgoConfig  |  CR FastGo Config improves DDRT non-temporal write bandwidth when FastGO is disabled. When FastGO is enabled, it gives faster flow of NT writes into the uncore, When FastGO is disabled, it lessens NT writes queueing up in the CPU uncore, thereby improving sequentially at DCPMM, resulting in improved bandwidth.  Applies to all Cisco UCS M5 and Cisco UCS M6 servers.  The values can be one of the following:

  * auto—Same as Option 1. Disables FastGO. Recommended for DDRT. This is the default option (not Default). 
  * default—Enables FastGO. 
  * option 1—Disables FastGO. 
  * option 2, option 3, option 4, option 5—Not applicable. 
  * enable optimization
  * disable optimization

|  **Note** |  The values enable optimization, disable optimization, and auto are supported on Cisco UCS M6 servers   
---|---  
Snoopy mode for AD set SnoopyModeForAD  |  Enables snoop-mode for DCPMM accesses while maintaining directory on all DRAM accesses. Snoops maintain cache coherence between sockets. Directory reduces snoops by keeping the remote node information locally (in memory). Directory lookups and updates add memory traffic.  Directory is a good tradeoff for DRAM, but not necessarily for DCPMM. For non-NUMA workload, when the feature is enabled, directory updates to DCPMM are eliminated, thereby helping DDRT bandwidth bound workloads. Directory is disabled for accesses to AD and instead snoops remote sockets to check for ownership. Directory is used only for DRAM accesses. 

  * enabled
  * disabled This is the default option. 

  
Snoopy mode for 2LM set SnoopyModeFor2LM  |  Enables snoop-mode for DCPMM accesses while maintaining directory on all DRAM accesses. Snoops maintain cache coherence between sockets. Directory reduces snoops by keeping the remote node information locally (in memory). Directory lookups and updates add memory traffic.  Directory is a good tradeoff for DRAM, but not necessarily for DCPMM. For non-NUMA workload, when the feature is enabled, directory updates to DCPMM are eliminated, thereby helping DDRT bandwidth bound workloads. Directory is disabled for far memory accesses and instead snoops remote sockets to check for ownership. Directory is used only for DRAM (near memory). 

  * enabled
  * disabled This is the default option. 

  
eADR Support scope token-feature "EadrSupport" scope token-param EadrSupport |  Extended asynchronous DRAM refresh (eADR) ensures that CPU caches lines with data are flushed at the right time and in the desired order and are also included in the power fail protected domain. This can be any of the following: 

  * enabled
  * disabled
  * auto—This is the default option. 

  
  
### Serial Port BIOS Settings 

The following table lists the serial port BIOS settings that you can configure through a BIOS policy or the default BIOS settings: 

Name  | Description   
---|---  
Serial port A enable set serial-port-a-config serial-port-a |  Whether serial port A is enabled or disabled. This can be one of the following: 

  * disabled—The serial port is disabled. 
  * enabled—The serial port is enabled. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
  
### USB BIOS Settings 

The following table lists the USB BIOS settings that you can configure through a BIOS policy or the default BIOS settings: 

Name  | Description   
---|---  
Make Device Non Bootable set usb-boot-config` `make-device-non-bootable |  Whether the server can boot from a USB device. This can be one of the following: 

  * disabled—The server can boot from a USB device. 
  * enabled—The server cannot boot from a USB device. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Legacy USB Support set usb-boot-config ` `legacy-support |  Whether the system supports legacy USB devices. This can be one of the following: 

  * disabled—USB devices are only available to EFI applications. 
  * enabled—Legacy USB support is always available. 
  * auto—Disables legacy USB support if no USB devices are connected. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
USB Idle Power Optimizing Setting set usb-system-idle-power-optimizing-setting-config` `usb-idle-power-optimizing |  Whether the USB Idle Power Optimizing setting is used to reduce USB EHCI idle power consumption. Depending upon the value you choose, this setting can have an impact on performance. This can be one of the following: 

  * high-performance—The USB System Idle Power Optimizing setting is disabled, because optimal performance is preferred over power savings.  Selecting this option can significantly improve performance. We recommend you select this option unless your site has server power restrictions. 
  * lower-idle-power—The USB System Idle Power Optimizing setting is enabled, because power savings are preferred over optimal performance. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
USB Front Panel Access Lock set usb-front-panel-access-lock-config` `usb-front-panel-lock |  USB front panel access lock is configured to enable or disable the front panel access to USB ports. This can be one of the following: 

  * disabled
  * enabled
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Port 60/64 Emulation set usb-port-config` ` usb-emulation |  Whether the system supports 60h/64h emulation for complete USB keyboard legacy support. This can be one of the following: 

  * disabled—60h/64 emulation is not supported. 
  * enabled—60h/64 emulation is supported.  You should select this option if you are using a non-USB aware operating system on the server. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
USB Port Front set usb-port-config` ` usb-front |  Whether the front panel USB devices are enabled or disabled. This can be one of the following: 

  * disabled—Disables the front panel USB ports. Devices connected to these ports are not detected by the BIOS and operating system. 
  * enabled—Enables the front panel USB ports. Devices connected to these ports are detected by the BIOS and operating system. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
USB Port Internal set usb-port-config` ` usb-internal  |  Whether the internal USB devices are enabled or disabled. This can be one of the following: 

  * disabled—Disables the internal USB ports. Devices connected to these ports are not detected by the BIOS and operating system. 
  * enabled—Enables the internal USB ports. Devices connected to these ports are detected by the BIOS and operating system. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
USB Port KVM set usb-port-config` ` usb-kvm |  Whether the vKVM ports are enabled or disabled. This can be one of the following: 

  * disabled—Disables the KVM keyboard and/or mouse devices. Keyboard and/or mouse will not work in the KVM window. 
  * enabled—Enables the KVM keyboard and/or mouse devices. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
USB Port Rear set usb-port-config` ` usb-rear |  Whether the rear panel USB devices are enabled or disabled. This can be one of the following: 

  * disabled—Disables the rear panel USB ports. Devices connected to these ports are not detected by the BIOS and operating system. 
  * enabled—Enables the rear panel USB ports. Devices connected to these ports are detected by the BIOS and operating system. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
USB Port SD Card set usb-port-config` ` usb-sdcard |  Whether the SD card drives are enabled or disabled. This can be one of the following: 

  * disabled—Disables the SD card drives. The SD card drives are not detected by the BIOS and operating system. 
  * enabled—Enables the SD card drives. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
USB Port VMedia set usb-port-config` ` usb-vmedia |  Whether the virtual media devices are enabled or disabled. This can be one of the following: 

  * disabled—Disables the vMedia devices. 
  * enabled—Enables the vMedia devices. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
All USB Devices set all-usb-devices-config` `all-usb |  Whether all physical and virtual USB devices are enabled or disabled. This can be one of the following: 

  * disabled—All USB devices are disabled. 
  * enabled—All USB devices are enabled. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
xHCI Mode set usb-configuration-select-config` `xhci-enable-disable |  Whether xHCI mode is enabled or disabled. This can be one of the following: 

  * disabled—xHCI mode is disabled. 
  * enabled—xHCI mode is enabled. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
USB Port:M.2 Storage set usb port:m.2 |  Whether the USB Port:M.2 Storage are enabled or disabled. This can be one of the following: 

  * disabled—Disables USB Port:M.2 Storage. 
  * enabled—Enables USB Port:M.2 Storage. This is the default option. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
  
### PCI Configuration BIOS Settings 

The following table lists the PCI configuration BIOS settings that you can configure through a BIOS policy or the default BIOS settings: 

Name  | Description   
---|---  
Maximum memory below 4GB set max-memory-below-4gb-config max-memory |  Whether the BIOS maximizes memory usage below 4GB for an operating system without PAE support, depending on the system configuration. This can be one of the following: 

  * disabled—Does not maximize memory usage. Choose this option for all operating systems with PAE support. 
  * enabled—Maximizes memory usage below 4GB for an operating system without PAE support. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Memory mapped IO above 4GB set memory-mapped-io-above-4gb-config memory-mapped-io |  Whether to enable or disable memory mapped I/O of 64-bit PCI devices to 4GB or greater address space. Legacy option ROMs are not able to access addresses above 4GB. PCI devices that are 64-bit compliant but use a legacy option ROM may not function correctly with this setting enabled. This can be one of the following: 

  * disabled—Does not map I/O of 64-bit PCI devices to 4GB or greater address space. 
  * enabled—Maps I/O of 64-bit PCI devices to 4GB or greater address space. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
VGA Priority set vga-priority-config vga-priority |  Allows you to set the priority for VGA graphics devices if multiple VGA devices are found in the system. This can be one of the following: 

  * onboard—Priority is given to the onboard VGA device. BIOS post screen and OS boot are driven through the onboard VGA port. 
  * offboard—Priority is given to the PCIE Graphics adapter. BIOS post screen and OS boot are driven through the external graphics adapter port. 
  * onboard-vga-disabled—Priority is given to the PCIE Graphics adapter, and the onboard VGA device is disabled.  |  **Note** |  The vKVM does not function when the onboard VGA is disabled.   
---|---  
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 


**Note** |  Only onboard VGA devices are supported with Cisco UCS B-Series servers.   
---|---  
ASPM Support set aspm-support-config aspm-support |  Allows you to set the level of ASPM (Active Power State Management) support in the BIOS. This can be one of the following: 

  * disabled—ASPM support is disabled in the BIOS. 
  * auto—The CPU determines the power state. 
  * forcel0—Force all links to L0 standby (L0s) state. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
BME DMA Mitigation Support set bme-dma-config  |  Allows you to disable the PCI BME bit to mitigate the threat from an unauthorized external DMA. This can be one of the following: 

  * disabled—PCI BME bit is disabled in the BIOS. 
  * enabled—PCI BME bit is enabled in the BIOS. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
  
### QPI BIOS Settings 

The following table lists the QPI BIOS settings that you can configure through a BIOS policy or the default BIOS settings: 

Name  | Description   
---|---  
QPI Link Frequency Select set qpi-link-frequency-select-config qpi-link-freqency-mt-per-sec |  The Intel QuickPath Interconnect (QPI) link frequency, in megatransfers per second (MT/s). This can be one of the following: 

  *   *   *   *   * 6400
  * 7200
  * 8000
  * 9600
  * auto—The CPU determines the QPI link frequency. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
QPI Snoop Mode set qpi-snoop-mode vpqpisnoopmode |  This can be one of the following: 

  * home-snoop—The snoop is always spawned by the home agent (centralized ring stop) for the memory controller. This mode has a higher local latency than early snoop, but it provides extra resources for a larger number of outstanding transactions. 
  * cluster-on-die—This mode is available only for processors that have 10 or more cores. It is the best mode for highly NUMA optimized workloads. 
  * home-directory-snoop-with-osb
  * early-snoop—The distributed cache ring stops can send a snoop probe or a request to another caching agent directly. This mode has lower latency and it is best for workloads that have shared data sets across threads and can benefit from a cache-to-cache transfer, or for workloads that are not NUMA optimized. 
  * auto —The CPU determines the QPI Snoop mode. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
  
### Trusted Platform BIOS Settings

The following table lists the trusted platform BIOS settings that you can configure through a BIOS policy or the default BIOS settings: 

Name  | Description   
---|---  
Trusted Platform Module (TPM) Support set trusted-platform-module-config tpm-support |  Whether to enable or disable the Trusted Platform Module (TPM), which is a component that securely stores artifacts that are used to authenticate the server. This can be one of the following: 

  * disabled—Disables TPM. 
  * enabled—Enables TPM. 
  * platform-default—Enables TPM. 

  
Intel Trusted Execution Technology (TXT) Support set intel-trusted-execution-technology-config txt-support |  Whether to enable or disable Intel Trusted Execution Technology (TXT), which provides greater protection for information that is used and stored on the business server. This can be one of the following: 

  * disabled—Disables TXT. This is default option. 
  * enabled—Enables TXT. 
  * platform-default—Disables TXT. 

When you only enable TXT, it implicitly enables TPM, VT, and VTDio.   
SHA-1 PCR Bank scope token-feature "Trusted Platform Module" scope token-param SHA1PCRBank |  The Platform Configuration Register (PCR) is a memory location in the TPM. Multiple PCRs are collectively referred to as a PCR bank. A Secure Hash Algorithm 1 or SHA-1 PCR Bank allows to enable or disable TPM security. This can be one of the following: 

  * disabled—Disables SHA-1 PCR Bank. 
  * enabled—Enables SHA-1 PCR Bank. This is the default option. 

  
SHA-256 PCR Bank scope token-feature "Trusted Platform Module" scope token-param SHA256PCRBank |  The Platform Configuration Register (PCR) is a memory location in the TPM. Multiple PCRs are collectively referred to as a PCR bank. A Secure Hash Algorithm 256-bit or SHA-256 PCR Bank allows to enable or disable TPM security. This can be one of the following: 

  * disabled—Disables SHA-256 PCR Bank. 
  * enabled—Enables SHA-256 PCR Bank. This is the default option. 

  
Trusted Platform Module State scope token-feature "Trusted Platform Module" scope token-param "Trusted Platform Module state" |  Trusted Platform Module (TPM ) is a microchip designed to provide basic security-related functions primarily involving encryption keys. This option allows you to control the TPM Security Device support for the system. This can be one of the following: 

  * disabled—The server does not use the TPM. 
  * enabled—The server uses the TPM. This is the default option. 

  
TPM Pending Operation scope token-feature "TPM Pending Operation" scope token-param "TPM Pending Operation" |  Trusted Platform Module (TPM) Pending Operation option allows you to control the status of the pending operation. This can be one of the following: 

  * none—No action. This is the default option. 
  * tpmclear—Clear the pending operations. 

  
TPM Minimal Physical Presence scope token-feature "Trusted Platform Module" # scope token-param TpmPpiRequired # show token-settings expand |  Whether to enable or disable TPM Minimal Physical Presence, which enables or disables the communication between the OS and BIOS for administering the TPM without compromising the security. This can be one of the following: 

  * disabled—Disables TPM Minimal Physical Presence. This is default option. 
  * enabled—Enables TPM Minimal Physical Presence. 
  * platform-default—Disables TPM Minimal Physical Presence. 

  
DMA Control Opt-In Flag scope token-feature "Trusted Platform Module" # scope token-param "DmaCtrlOptIn" token-param # show token-settings |  Enabling this token enables Windows 2022 Kernel DMA Protection feature. The OS treats this as a hint that the IOMMU should be enabled to prevent DMA attacks from possible malicious devices. This can be one of the following: 

  * disabled—Disables DMA Control Opt-In Flag. This is default option. 
  * enabled—Enables DMA Control Opt-In Flag. 
  * platform-default—Disables DMA Control Opt-In Flag. 

  
Security Device Support set TpmSupport |  Enables or disables BIOS support for the security device. This can be one of the following: 

  * disabled—Deactivates security device functionality for streamlined performance. 
  * enabled—Activates security device functionality for enhanced protection. 

  
Above 4G Decoding scope token-feature "Above 4G Decoding" scope token-param Above 4G Decoding |  Enables or disables MMIO above 4GB or not. This can be one of the following:

  * enabled—The server maps I/O of 64-bit PCI devices to 4GB or greater address space. This is the default option. 
  * disabled—The server does not map I/O of 64-bit PCI devices to 4GB or greater address space. 

  
  
### LOM and PCIe Slots BIOS Settings 

The following table lists the USB BIOS settings that you can configure through a BIOS policy or the default BIOS settings: 

Name  | Description   
---|---  
PCIe Slot SAS OptionROM set slot-option-rom-enable-config pcie-sas |  Whether Option ROM is available on the SAS port. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * uefi-only—The expansion slot is available for UEFI only. 
  * legacy-only—The expansion slot is available for legacy only. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
PCIe Slot n Link Speed set slot-link-speed-config pcie-slotn-link-speed |  This option allows you to restrict the maximum speed of an adapter card installed in PCIe slot n. This can be one of the following: 

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * gen4—16GT/s is the maximum speed allowed. 
  * gen5—32GT/s is the maximum speed allowed. 
  * auto—The maximum speed is set automatically. This is the default option. 
  * disabled—The maximum speed is not restricted. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
PCIe Slot n OptionROM set slot-option-rom-enable-config slotn-option-rom-enable |  Whether Option ROM is available on the port. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. This is the default option. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
PCIe Slot HBA OptionROM set slot-option-rom-enable-config pcie-hba |  Whether Option ROM is available on the HBA port. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * uefi-only—The expansion slot is available for UEFI only. 
  * legacy-only—The expansion slot is available for legacy only. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
PCIe Slot MLOM OptionROM set slot-option-rom-enable-config pcie-mlom |  Whether Option ROM is available on the MLOM port. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * uefi-only—The expansion slot is available for UEFI only. 
  * legacy-only—The expansion slot is available for legacy only. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
PCIe Slot Nx OptionROM set slot-option-rom-enable-config pcie-nx |  Whether Option ROM is available on the port. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * uefi-only—The expansion slot is available for UEFI only. 
  * legacy-only—The expansion slot is available for legacy only. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
PCIe 10G LOM 2 Link set lom-ports-config pcie-lom2-link |  Whether Option ROM is available on the 10G LOM port. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
PCI ROM CLP set pci-rom-clp-support pci-rom-clp-config |  PCI ROM Command Line Protocol (CLP) controls the execution of different Option ROMs such as PxE and iSCSI that are present in the card. By default, it is disabled. 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SIOC1 Option ROM set sioc1-optionrom-config sioc1-optionrom |  Whether the server can use Option ROM present in System IO Controller 1 (SIOC1). This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * uefi-only—The expansion slot is available for UEFI only. 
  * legacy-only—The expansion slot is available for legacy only. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SIOC2 Option ROM set sioc2-optionrom-config sioc2-optionrom |  Whether the server can use Option ROM present in System IO Controller 2 (SIOC2). This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * uefi-only—The expansion slot is available for UEFI only. 
  * legacy-only—The expansion slot is available for legacy only. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SBMEZZ1 Option ROM set sbmezz1-optionrom-config sbmezz1-optionrom |  Whether the server can use Option ROM present in SBMezz1 controller. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * uefi-only—The expansion slot is available for UEFI only. 
  * legacy-only—The expansion slot is available for legacy only. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SBMEZZ2 Option ROM set sbmezz2-optionrom-config sbmezz2-optionrom |  Whether the server can use Option ROM present in SBMezz2 controller. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * uefi-only—The expansion slot is available for UEFI only. 
  * legacy-only—The expansion slot is available for legacy only. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
IOESlot1 OptionROM set ioeslot1-optionrom-config ioeslot1-optionrom |  Whether option ROM is enabled on the IOE slot 1. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * uefi-only—The expansion slot is available for UEFI only. 
  * legacy-only—The expansion slot is available for legacy only. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
IOEMEZZ 1 OptionROM set ioemezz1-optionrom-config ioemezz1-optionrom |  Whether option ROM is enabled on the IOE Mezz1. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * uefi-only—The expansion slot is available for UEFI only. 
  * legacy-only—The expansion slot is available for legacy only. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
IOE Slot2 Option ROM set ioeslot2-optionrom-config ioeslot2-optionrom |  Whether option ROM is enabled on the IOE slot 2. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * uefi-only—The expansion slot is available for UEFI only. 
  * legacy-only—The expansion slot is available for legacy only. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
IO ENVME1 Option ROM set ioenvme1-optionrom-config ioenvme1-optionrom |  Whether option ROM is enabled on the IOE NVMe1. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * uefi-only—The expansion slot is available for UEFI only. 
  * legacy-only—The expansion slot is available for legacy only. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
IO ENVME2 Option ROM set ioenvme2-optionrom-config ioenvme2-optionrom |  Whether option ROM is enabled on the IOE NVMe2. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * uefi-only—The expansion slot is available for UEFI only. 
  * legacy-only—The expansion slot is available for legacy only. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SBNVME1 Option ROM set sbnvme1-optionrom-config sbnvme1-optionrom |  Whether the server can use Option ROM present in SBNVMe1 controller. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * uefi-only—The expansion slot is available for UEFI only. 
  * legacy-only—The expansion slot is available for legacy only. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
PCIe Slot MRAID-n OptionROM set Pcie SlotMRAID nOptionROM |  Whether Option ROM is available on the MRAID port. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
PCIe Slot RAID OptionROM set Pcie SlotRAIDOptionROM |  Whether Option ROM is available on the RAID port. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * uefi-only—The expansion slot is available for UEFI only. 
  * legacy-only—The expansion slot is available for legacy only. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Rear NVME n Link Speed set Pcie SlotRearNvme1LinkSpeed |  This option allows you to restrict the maximum speed of an NVME card installed in the rear PCIe slot n. This can be one of the following: 

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * gen4—16GT/s is the maximum speed allowed. 
  * gen5—32GT/s is the maximum speed allowed. 
  * enabled—The maximum speed is restricted.  |  **Note** | 
  * For _Rear NVME 1 Link Speed_ and _Rear NVME 2Link Speed_, the value enabled is not supported on Cisco UCS M6 and M8 servers. 
  * For _Rear NVME 3 Link Speed_ and _Rear NVME 4Link Speed_, the value enabled is available but has no effect at the BIOS level if selected.   
---|---  
  * auto—The maximum speed is set automatically. 

  * disabled—The maximum speed is not restricted. 

  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 


  
Front NVME n Link Speed set Pcie SlotFrontNvmenLinkSpeed |  This option allows you to restrict the maximum speed of an NVME card installed in the front PCIe slot. This can be one of the following: 

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * gen4—16GT/s is the maximum speed allowed. 
  * gen5—32GT/s is the maximum speed allowed. 
  * auto—The maximum speed is set automatically. This is the default option. 
  * enabled—The maximum speed is restricted.  |  **Note** |  For _Front NVME 1 Link Speed_ and _Front NVME 2 Link Speed_, the value enabled is available but not supported on Cisco UCS M6 and M8 servers.   
---|---  
  * disabled—The maximum speed is not restricted. 

  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 


**Note** |  For _Front Nvme 13 Link Speed_ to _Front Nvme 24 Link Speed_ , the BIOS tokens and values are available but have no effect at the BIOS level if selected.   
---|---  
HBA Link Speed set HBALinkSpeed |  This option allows you to restrict the maximum speed of an HBA card. This can be one of the following: 

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * auto—The maximum speed is set automatically. 
  * disabled—The maximum speed is not restricted. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
MLOM Link Speed set Pcie SlotMLOMLinkSpeed |  This option allows you to restrict the maximum speed of an MLOM adapter. This can be one of the following: 

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * gen4—16GT/s is the maximum speed allowed. 
  * gen5—16GT/s is the maximum speed allowed. 
  * auto—The maximum speed is set automatically. This is the default option. 
  * disabled—The maximum speed is not restricted. 
  * enabled—The maximum speed is restricted.  |  **Note** |  The value enabled is not supported on Cisco UCS M6 and M8 servers.   
---|---  
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 


  
MRAID Link Speed scope token-feature "Pcie Slot Link Speed" scope token-param PcieSlotMRAIDLinkSpeed |  This option allows you to restrict the maximum speed of MRAID. This can be one of the following:

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * gen4—16GT/s is the maximum speed allowed. 
  * gen5—32GT/s is the maximum speed allowed. 
  * auto—The maximum speed is set automatically. 
  * enabled—The maximum speed is not restricted.  |  **Note** |  The value enabled is not supported on Cisco UCS M6 servers.   
---|---  
  * disabled—The maximum speed is not restricted. 

  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 


  
RAID-n Link Speed set Pcie SlotRAIDLinkSpeed |  This option allows you to restrict the maximum speed of RAID. This can be one of the following: 

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * gen4—16GT/s is the maximum speed allowed. 
  * auto—The maximum speed is set automatically. 
  * disabled—The maximum speed is not restricted. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
All Onboard LOM set AllLomPortControl |  Whether all onboard LOM ports are enabled or disabled. This can be one of the following:

  * enabled—All onboard LOM are enabled. 
  * disabled—All onboard LOM are disabled. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
LOM Port 1 OptionRom set LomOpromControlPort0 |  Whether Option ROM is available on the LOM port 1. This can be one of the following:

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * uefi-only—The expansion slot is available for UEFI only. 
  * legacy-only—The expansion slot is available for legacy only. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
LOM Port 2 OptionRom set LomOpromControlPort1 |  Whether Option ROM is available on the LOM port 2. This can be one of the following:

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * uefi-only—The expansion slot is available for UEFI only. 
  * legacy-only—The expansion slot is available for legacy only. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Slot n State set SlotnState |  The state of the adapter card installed in PCIe slot n. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * uefi-only—The expansion slot is available for UEFI only. 
  * legacy-only—The expansion slot is available for legacy only. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SBNVMe1 OptionROM set SBNVMe1OptionROM |  Whether the server can use Option ROM present in SBNVMe1 controller. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SBNVMe2 OptionROM set SBNVMe2OptionROM |  Whether the server can use Option ROM present in SBNVMe2 controller. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SIOCNVMe1 OptionROM set SIOCNVMe1OptionROM |  Whether the server can use Option ROM present in SIOCNVMe1 controller. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SIOCNVMe2 OptionROM set SIOCNVMe2OptionROM |  Whether the server can use Option ROM present in SIOCNVMe2 controller. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SBLom1 OptionROM set SBLom1OptionROM |  Whether the server can use Option ROM present in the SBLom1 controller. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SBNVMen Link Speed set SBNVMenLinkSpeed |  Link speed for SBNVMe slot n. This can be one of the following: 

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * enabled—The maximum speed is restricted. 
  * disabled—The maximum speed is not restricted. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SIOCNVMen Link Speed set SIOCNVMenLinkSpeed |  Link speed for SIOCNVMe slot n. This can be one of the following: 

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * enabled—The maximum speed is restricted. 
  * disabled—The maximum speed is not restricted. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SIOCn Link Speed set SIOCnLinkSpeed |  Link speed for SIOC slot n. This can be one of the following: 

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * enabled—The maximum speed is restricted. 
  * disabled—The maximum speed is not restricted. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SBMezzn Link Speed set SBMezznLinkSpeed |  Link speed for SBMezz slot n. This can be one of the following: 

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * enabled—The maximum speed is restricted. 
  * disabled—The maximum speed is not restricted. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
IOESlotn Link Speed set IOESlotnLinkSpeed |  Link speed for IOE slot n. This can be one of the following: 

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * enabled—The maximum speed is restricted. 
  * disabled—The maximum speed is not restricted. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
IOEMezzn Link Speed set IOEMezznLinkSpeed |  Link speed for IOEMezz slot n. This can be one of the following: 

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * enabled—The maximum speed is restricted. 
  * disabled—The maximum speed is not restricted. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
IOENVMen Link Speed set IOENVMenLinkSpeed |  Link speed for IOENVMe slot n. This can be one of the following: 

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * enabled—The maximum speed is restricted. 
  * disabled—The maximum speed is not restricted. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
CDN Support for LOMs set CdnSupport |  Whether the Ethernet Networking Identifier naming convention is according to Consistent Device Naming (CDN) or the traditional way of naming conventions. This can be one of the following: 

  * enabled—OS Ethernet Network Identifier is named in a consistent device naming (CDN) convention according to the physical LAN on Motherboard (LOM) port numbering; LOM Port 0, LOM Port 1 and so on. 
  * disabled—OS Ethernet Networking Identifier is named in a default convention as ETH0, ETH1 and so on. By default, CDN option is disabled. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
VMD Enable set VMDEnable |  Whether NVMe SSDs that are connected to the PCIe bus can be hot swapped. It also standardizes the LED status light on these drives. LED status lights can be optionally programmed to display specific Failure indicator patterns. This can be one of the following:

  * enabled—Hot swap of NVMe SSDs that are connected to the PCIe bus is allowed. 
  * disabled—Hot swap of NVMe SSDs that are connected to the PCIe bus is not allowed. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
ACS Control SLOT-n set ACSCtlSlotn n = 11 to 14 |  Access Control Services (ACS) allow the processor to enable or disable peer-to-peer communication between multiple devices for Control Slot n. This can be one of the following: 

  * enabled— Enables peer-to-peer communication between multiple devices for Control Slot n. 
  * disabled— Disables peer-to-peer communication between multiple devices for Control Slot n. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
PCIe Slot GPUn OptionROM Only for Cisco UCS C480 M5 ML Server |  Whether the Option ROM is enabled on GPU slot n. n is the slot number, which can be numbered 1 through 8. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
ACS Control GPU-n set ACSCtlGpun n = 1 to 8 |  Access Control Services (ACS) allow the processor to enable or disable peer-to-peer communication between multiple devices for GPUs. This can be one of the following: 

  * disabled— Enables peer-to-peer communication between multiple devices for GPUs. 
  * enabled— Disables peer-to-peer communication between multiple devices for GPUs. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
PCIe PLL SSC |  Reduces EMI interference by down-spreading the clock by 0.5%. Disable this feature to centralize the clock without spreading. For all Cisco UCS M5 and M6 servers, this option is Disabled by default. 

  * disabled— Clock is centralized without spreading. 
  * auto— EMI interference is auto adjusted. 
  * zeropointfive— EMI interference us reduced by down-spreading the clock by 0.5%. 
  * platform-default— The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Front Nvme n OptionROM scope token-feature "PCI Slot OptionROM Enable" scope token-param PcieSlotFrontNvme nOptionROM |  This options allows you to control the Option ROM execution of the PCIe adapter connected to the SSD:NVMe slot n. This can be one of the following: 

  * enabled—This is the default option. 
  * disabled

  
PCIe Slot n Link Speed scope token-feature "PCI Slot LINK Speed" scope token-param PcieSlotLinkSpeed |  Link speed for PCIe Slot designated by slot n. This can be one of the following: 

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * gen4—16GT/s is the maximum speed allowed. 
  * gen5—16GT/s is the maximum speed allowed. 
  * auto—The maximum speed is set automatically. 
  * disabled—The maximum speed is not restricted. 

  
MSTOR-RAID Link Speed sc token-feature "PCI Slot LINK Speed" sc token-param PcieSlotMSTORRAIDLinkSpeed |  This option allows you to restrict the maximum speed of an MSTOR adapter. This can be one of the following: 

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * gen4—16GT/s is the maximum speed allowed. 
  * auto—The maximum speed is set automatically. 
  * disabled—The maximum speed is not restricted. 

|  **Note** |  In this BIOS setting _MSTOR-RAID Link Speed_ , the token and values are available but have no effect at the BIOS level if selected.   
---|---  
MSTOR-RAID OptionROM sc token-feature "MSTOR-RAID OptionROM" sc token-param PcieSlotMSTORRAIDoptionROM |  Whether the server can use the Option ROMs present in the PCIe MSTOR RAID. This can be any of the following:

  * disabled—Option ROM is available. 
  * enabled—Option ROM is not available. This is the default option. 

  
MLOM OptionROM set slot-option-rom-enable-config pcie-mlom |  Whether Option ROM is available on the MLOM port. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. This is the default option. 

  
MRAID OptionROM set Pcie SlotMRAID OptionROM |  Whether Option ROM is available on the MRAID port. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. This is the default option. 

  
Rear Nvme n OptionRom set RearNvmenOptionROM |  Whether Option ROM is available on the Rear NVMEn port. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. This is the default option. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
PCIe slot MSTOR Link Speed sc token-feature "PCI Slot LINK Speed" sc token-param PcieSlotMSTORRAIDLinkSpeed |  This option allows you to restrict the maximum speed of an MSTOR adapter. This can be one of the following: 

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * gen4—16GT/s is the maximum speed allowed. 
  * gen5—32GT/s is the maximum speed allowed. 
  * auto—The maximum speed is set automatically. This is the default option. 
  * disabled—The maximum speed is not restricted. 

  
PCIe Slot MSTOR RAID OptionROM scope token-feature "pcie MSTOR-RAID OptionROM" sc token-param PcieSlotMSTORRAIDoptionROM |  Whether the server can use the Option ROMs present in the PCIe MSTOR RAID. This can be any of the following:

  * disabled—Option ROM is available. 
  * enabled—Option ROM is not available. This is the default option. 

  
PCIe RAS Support sc token-feature "pcie ras-support" |  Whether PCIe RAS Support is available on the PCIe slot. This can be one of the following:

  * disabled—PCIe RAS is available on the slot. 
  * enabled—PCIe RAS is not available on the slot. This is the default option. 

  
MRAID n Link Speed scope token-feature "Pcie Slot Link Speed" scope token-param PcieSlotMRAIDLinkSpeed |  This option allows you to restrict the maximum speed of MRAID. This can be one of the following:

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * gen4—16GT/s is the maximum speed allowed. 
  * gen5—32GT/s is the maximum speed allowed. 
  * auto—The maximum speed is set automatically. This is the default option. 
  * disabled—The maximum speed is not restricted. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
MRAIDn OptionROM scope token-feature "Pcie Slot OptionROM" scope token-param PcieSlotOptionROM |  Whether Option ROM is available on the MRAID port. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. This is the default option. 

  
NVME-n OptionROM scope token-feature "Pcie Slot OptionROM" scope token-param PcieSlotOptionROM |  Whether Option ROM is available on the NVME port. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. This is the default option. 

  
PCIe Slot OCP Link Speed scope token-feature "Pcie Slot ocp Link Speed" scope token-param PcieSlotocpLinkSpeed |  This option allows you to restrict the maximum speed of OCP. This can be one of the following:

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * auto—The maximum speed is set automatically. This is the default option. 
  * disabled—The maximum speed is not restricted. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
RAIDn OptionROM scope token-feature "raid optionrom" scope token-param raidoptionrom |  Whether Option ROM is available on the RAID port. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. This is the default option. 

  
IOENVMen OptionROM scope token-feature "ioenvme optionrom" scope token-param ioenvmeoptionrom |  Whether Option ROM is available on the IOENVMe port. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. This is the default option. 

  
GPUn OptionRom scope token-feature "ioemezz1 optionrom" scope token-param ioemezz1optionrom |  Whether Option ROM is available on the GPU port. This can be one of the following: 

  * disabled—The expansion slot is not available. 
  * enabled—The expansion slot is available. This is the default option. 

  
RAID Link Speed scope token-feature "raid link speed" scope token-param RAIDLinkSpeed |  This option allows you to restrict the maximum speed of RAID. This can be one of the following:

  * gen1—2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * gen2—5GT/s is the maximum speed allowed. 
  * gen3—8GT/s is the maximum speed allowed. 
  * auto—The maximum speed is set automatically. This is the default option. 
  * enabled—The maximum speed is not restricted.  |  **Note** |  The value enabled is not supported on Cisco UCS M6and M8 servers.   
---|---  
  * disabled—The maximum speed is not restricted. 

  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 


  
External SSC enable |  This option allows you to Enable/Disable the Clock Spread Spectrum of the external clock generators. For Cisco B-Series M5 and M6servers and S-Series M5 servers, this option is Disabled by default. For Cisco C-Series rack servers, it is enabled by default. 

  * disabled— Clock Spread Spectrum support is not available. 
  * enabled— Clock Spread Spectrum support is always available. 
  * platform-default — The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Re-size BAR Support set ResizeBarSupport |  Allows to enable or disable re-sizable BAR support setup.

  * enabled—This is the default option. 
  * disabled

  
SR-IOV Support scope token-feature "sriov" scope token-param "sriov-support" |  Whether SR-IOV (Single Root I/O Virtualization) is enabled or disabled on the server. This can be one of the following:

  * enabled—SR-IOV is enabled. This is the default option. 
  * disabled—SR-IOV is disabled. 

  
  
### Graphics Configuration BIOS Settings 

The following tables list the graphics configuration BIOS settings that you can configure through a BIOS policy or the default BIOS settings: 

Name  | Description   
---|---  
Integrated Graphics set integrated-graphics-config integrated-graphics |  Enables integrated graphics. This can be one of the following: 

  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 
  * enabled—Integrated graphic is enabled. 
  * disabled—Integrated graphics is disabled. 

  
Integrated Graphics Aperture Size set integrated-graphics-aperture-config integrated-graphics-aperture |  Allows you to set the size of mapped memory for the integrated graphics controller. This can be one of the following: 

  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 
  * 128mb
  * 256mb
  * 512mb
  * 1024mb
  * 2048mb
  * 4096mb

  
Onboard Graphics set onboard-graphics-config onboard-graphics |  Enables onboard graphics (KVM). This can be one of the following: 

  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 
  * enabled—Onboard graphics is enabled. 
  * disabled—Onboard graphics is disabled. 

  
  
### Boot Options BIOS Settings 

The following table lists the boot options BIOS settings that you can configure through a BIOS policy or the default BIOS settings: 

Name  | Description   
---|---  
Boot option retry set boot-option-retry-config retry |  Whether the BIOS retries NON-EFI based boot options without waiting for user input. This can be one of the following: 

  * disabled—Waits for user input before retrying NON-EFI based boot options. This is the default option. 
  * enabled—Continually retries NON-EFI based boot options without waiting for user input. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SAS RAID set intel-entry-sas-raid-config sas-raid |  Whether the Intel SAS Entry RAID Module is enabled. This can be one of the following: 

  * disabled—The Intel SAS Entry RAID Module is disabled. 
  * enabled—The Intel SAS Entry RAID Module is enabled. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
SAS RAID module set intel-entry-sas-raid-config sas-raid-module |  How the Intel SAS Entry RAID Module is configured. This can be one of the following: 

  * it-ir-raid—Configures the RAID module to use Intel IT/IR RAID. 
  * intel-esrtii—Configures the RAID module to use Intel Embedded Server RAID Technology II. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Onboard SCU Storage Support set onboard-sas-storage-config onboard-sas-ctrl |  Whether the onboard software RAID controller is available to the server. This can be one of the following: 

  * disabled—The software RAID controller is not available. 
  * enabled—The software RAID controller is available. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Cool Down Time (sec) |  The time to wait (in seconds) before the next boot attempt. This can be one of the following:

  * 15—System waits for 15 seconds before the next boot attempt. 
  * 45—System waits for 45 seconds before the next boot attempt. 
  * 90—System waits for 90 seconds before the next boot attempt. This is the default option. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

This token is valid only when the Boot Option Retry token has been enabled.  
Number of Retries |  Number of attempts to boot. This can be one of the following:

  * infinite—System tries all options to boot up. 
  * 13—System tries 13 times to boot up. This is the default option. 
  * 5—System tries 5 times to boot up 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
P-SATA mode |  This options allows you to select the P-SATA mode. This can be one of the following:

  * disabled—P-SATA mode is disabled. 
  * lsi-sw-raid—Sets both SATA and sSATA controllers to RAID mode for LSI SW RAID. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Power On Password |  This token requires that you set a BIOS password before using the F2 BIOS configuration. If enabled, password needs to be validated before you access BIOS functions such as IO configuration, BIOS set up, and booting to an operating system using BIOS. It can be one of the following: 

  * disabled—Power On Password is disabled. 
  * enabled—Power On Password is enabled. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Adaptive Memory Training |  When this token is enabled, the BIOS saves the memory training results (optimized timing/voltage values) along with CPU/memory configuration information and reuses them on subsequent reboots to save boot time. The saved memory training results are used only if the reboot happens within 24 hours of the last save operation. This can be one of the following: 

  * disabled—Adaptive Memory Training is disabled. 
  * enabled—Adaptive Memory Training is enabled. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
BIOS Tech Message Level Control (for C125 M5)  |  Enabling this token allows the BIOS Tech log output to be controlled at more a granular level. This reduces the number of BIOS Tech log messages that are redundant, or of little use. This can be one of the following: 

  * disabled—BIOS Techlog Level is disabled. 
  * enabled—BIOS Techlog Level is enabled. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
OptionROM Launch Optimization |  The Option ROM launch is controlled at the PCI Slot level, and is enabled by default. In configurations that consist of a large number of network controllers and storage HBAs having Option ROMs, all the Option ROMs may get launched if the PCI Slot Option ROM Control is enabled for all. However, only a subset of controllers may be used in the boot process. When this token is enabled, Option ROMs are launched only for those controllers that are present in boot policy. This can be one of the following: 

  * disabled—OptionROM Launch Optimization is disabled. 
  * enabled—OptionROM Launch Optimization is enabled. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
BIOS Techlog Level BIOSTechlogLevel |  This option denotes the type of messages in BIOS tech log file. The log file can be any of the following types: 

  * minimum—Critical messages will be displayed in the log file. This is the default option. 
  * normal—Warning and loading messages will be displayed in the log file. 
  * maximum—Normal and information related messages will be displayed in the log file. 

  
P-SATA OptionROM |  This options allows you to select the P-SATA mode. This can be one of the following:

  * lsi-sw-raid—Sets both SATA and sSATA controllers to RAID mode for LSI SW RAID. This is the default option. 
  * disabled—P-SATA mode is disabled. 
  * ahci—Sets the controllers to AHCI mode. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
M.2 SATA OptionROM |  This options allows you to select the P-SATA mode. This can be one of the following:

  * lsi-sw-raid—Sets both SATA and sSATA controllers to RAID mode for LSI SW RAID. This is the default option. 
  * disabled—P-SATA mode is disabled. 
  * ahci—Sets the controllers to AHCI mode. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
UEFI Boot Mode |  This options allows you to select the UEFI Boot mode. This can be one of the following:

  * disabled—UEFI Boot mode is disabled. 
  * enabled—UEFI Boot mode is enabled. 

  
VGA Priority set vga-priority-config vga-priority |  Allows you to set the priority for VGA graphics devices if multiple VGA devices are found in the system. This can be one of the following: 

  * onboard—Priority is given to the onboard VGA device. BIOS post screen and OS boot are driven through the onboard VGA port. 
  * offboard—Priority is given to the PCIE Graphics adapter. BIOS post screen and OS boot are driven through the external graphics adapter port. 
  * onboard-vga-disabled—Priority is given to the PCIE Graphics adapter, and the onboard VGA device is disabled.  |  **Note** |  The vKVM does not function when the onboard VGA is disabled.   
---|---  
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 


**Note** |  Only onboard VGA devices are supported with Cisco UCS B-Series servers.   
---|---  
IPv4 PXE Support scope token-feature "IPv4 PXE Support" scope token-param "IPv4PXESupport" |  Enables or disables IPv4 support for PXE. This can be one of the following:

  * disabled—IPv4 PXE support is not available. 
  * enabled—IPv4 PXE support is available. This is the default option. 

  
IPv6 PXE Support scope token-feature "IPv6 PXE Support" scope token-param "IPv6PXESupport" |  Enables or disables IPv6 support for PXE. This can be one of the following:

  * disabled—IPv6 PXE support is not available. 
  * enabled—IPv6 PXE support is available. This is the default option. 

  
IPv6 HTTP Support scope token-feature "HTTP BOOT" scope token-param "IPV6HTTP" |  Enables or disables IPv6 support for HTTP. This can be one of the following:

  * disabled—IPv6 HTTP support is not available. 
  * enabled—IPv6 HTTP support is available. This is the default option. 

  
Network Stack scope token-feature "Network Stack" scope token-param "NetworkStack" |  This option allows you to monitor IPv6 and IPv4. This can be one of the following

  * disabled—Network Stack support is not available.  |  **Note** |  When disabled, the value set for IPV4 PXE Support does not impact the system.   
---|---  
  * enabled—Network Stack support is available. This is the default option. 


**Note** |  When Network Stack token value is Disabled, the below tokens and their values are also set

  * IPV4PXE - Disabled
  * IPV4HTTP - Disabled
  * IPV6HTTP - Disabled

  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

BIOS parameter virtualization capability in Cisco UCS Manager maps a unified set of BIOS settings in a service profile to the actual BIOS supporting parameters. However, not all BIOS setting items are applicable to every server model/platform. When you create a custom BIOS policy and have the Boot Option Retry selected, and when there is no bootable option available, the reboot fails and Cisco UCS Manager displays this message : Reboot and Select proper Boot device or Insert Boot Media in selected Boot device and press a key. You must manually set a boot option after the boot path is corrected, in order to enable the servers to reboot after a power outage. For more information about BIOS default server policies and the BIOS options and their default settings, see BIOS Policy and Server BIOS Settings. 

* * *  
  
---|---  
  
### Server Management BIOS Settings 

The following tables list the server management BIOS settings that you can configure through a BIOS policy or the default BIOS settings: 

#### General Settings 

Name  | Description   
---|---  
Serial Mux set SerialMux |  Enables or disables the serial mux configuration. This can be one of the following: 

  * enabled—Enables the serial mux configuration. 
  * disabled—Disables the serial mux configuration. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Assert NMI on SERR set assert-nmi-on-serr-config assertion |  Whether the BIOS generates a non-maskable interrupt (NMI) and logs an error when a system error (SERR) occurs. This can be one of the following: 

  * disabled—The BIOS does not generate an NMI or log an error when a SERR occurs. 
  * enabled—The BIOS generates an NMI and logs an error when a SERR occurs. You must enable this setting if you want to enable Assert NMI on PERR. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Assert NMI on PERR set assert-nmi-on-perr-config assertion |  Whether the BIOS generates a non-maskable interrupt (NMI) and logs an error when a processor bus parity error (PERR) occurs. This can be one of the following: 

  * disabled—The BIOS does not generate an NMI or log an error when a PERR occurs. 
  * enabled—The BIOS generates an NMI and logs an error when a PERR occurs. You must enable Assert NMI on SERR to use this setting. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
OS Boot Watchdog Timer Policy set os-boot-watchdog-timer-policy-config os-boot-watchdog-timer-policy |  What action the system takes if the watchdog timer expires. This can be one of the following: 

  * power-off—The server is powered off if the watchdog timer expires during OS boot. 
  * reset—The server is reset if the watchdog timer expires during OS boot. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

This option is only available if you enable the OS Boot Watchdog Timer.   
OS Boot Watchdog Timer Timeout set os-boot-watchdog-timer-timeout-config os-boot-watchdog-timer-timeout  |  What timeout value the BIOS uses to configure the watchdog timer. This can be one of the following: 

  * 5-minutes—The watchdog timer expires 5 minutes after the OS begins to boot. 
  * 10-minutes—The watchdog timer expires 10 minutes after the OS begins to boot. 
  * 15-minutes—The watchdog timer expires 15 minutes after the OS begins to boot. 
  * 20-minutes—The watchdog timer expires 20 minutes after the OS begins to boot. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

This option is only available if you enable the OS Boot Watchdog Timer.   
FRB-2 Timer set frb-2-timer-config frb-2-timer  |  Whether the FRB-2 timer is used to recover the system if it hangs during POST. This can be one of the following: 

  * disabled—The FRB-2 timer is not used. 
  * enabled—The FRB-2 timer is started during POST and used to recover the system if necessary. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
  
#### Console Redirection Settings 

Name  | Description   
---|---  
Console redirection set console-redir-config console-redir |  Allows a serial port to be used for console redirection during POST and BIOS booting. After the BIOS has booted and the operating system is responsible for the server, console redirection is irrelevant and has no effect. This can be one of the following: 

  * disabled—No console redirection occurs during POST. 
  * com 0—Enables serial port for console redirection during POST. This option is valid only for M6 blade servers and rack-mount servers.  |  **Note** |  The value serial-port-a is not supported on M6 servers.   
---|---  
  * serial-port-b or COM 1—Enables serial port B for console redirection and allows it to perform server management tasks. This option is only valid for rack-mount servers. 

  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 


**Note** |  If you enable this option, you also disable the display of the Quiet Boot logo screen during POST.   
---|---  
Flow Control set console-redir-config flow-control |  Whether a handshake protocol is used for flow control. Request to Send / Clear to Send (RTS/CTS) helps to reduce frame collisions that can be introduced by a hidden terminal problem. This can be one of the following: 

  * none—No flow control is used. 
  * rts-cts—RTS/CTS is used for flow control. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

|  **Note** |  This setting must match the setting on the remote terminal application.   
---|---  
Baud rate set console-redir-config baud-rate |  What Baud rate is used for the serial port transmission speed. If you disable Console Redirection, this option is not available. This can be one of the following: 

  * 9600—A 9600 Baud rate is used. 
  * 19200—A 19200 Baud rate is used. 
  * 38400—A 38400 Baud rate is used. 
  * 57600—A 57600 Baud rate is used. 
  * 115200—A 115200 Baud rate is used. This is the default option. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

|  **Note** |  This setting must match the setting on the remote terminal application.   
---|---  
Terminal type set console-redir-config terminal-type |  What type of character formatting is used for console redirection. This can be one of the following: 

  * pc-ansi—The PC-ANSI terminal font is used. 
  * vt100—A supported vt100 video terminal and its character set are used. 
  * vt100-plus—A supported vt100-plus video terminal and its character set are used. 
  * vt-utf8—A video terminal with the UTF-8 character set is used. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

|  **Note** |  This setting must match the setting on the remote terminal application.   
---|---  
Legacy OS redirection set console-redir-config legacy-os-redir |  Whether redirection from a legacy operating system, such as DOS, is enabled on the serial port. This can be one of the following: 

  * disabled—The serial port enabled for console redirection is hidden from the legacy operating system. 
  * enabled— The serial port enabled for console redirection is visible to the legacy operating system. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Putty KeyPad set console-redir-config putty-function-keypad |  Allows you to change the action of the PuTTY function keys and the top row of the numeric keypad. This can be one of the following: 

  * vt100—The function keys generate `ESC OP` through `ESC O[.`
  * linux—Mimics the Linux virtual console. Function keys F6 to F12 behave like the default mode, but F1 to F5 generate `ESC [[A` through `ESC [[E`. 
  * xtermr6—Function keys F5 to F12 behave like the default mode. Function keys F1 to F4 generate ESC OP through ESC OS, which are the sequences produced by the top row of the keypad on Digital terminals. 
  * sco—The function keys F1 to F12 generate `ESC [M` through `ESC [X`. The function and shift keys generate `ESC [Y` through `ESC [j`. The control and function keys generate `ESC [k` through `ESC [v`. The shift, control and function keys generate `ESC [w` through `ESC [{`. 
  * escn—The default mode. The function keys match the general behavior of Digital terminals. The function keys generate sequences such as `ESC [11~` and `ESC [12~`. 
  * vt400—The function keys behave like the default mode. The top row of the numeric keypad generates `ESC OP` through `ESC OS`. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Out of Band Management |  Used for Windows Special Administration Control (SAC). This option allows you to configure the COM port 0 that can be used for Windows Emergency Management services. ACPI SPCR table is reported based on this setup option. This can be one of the following: 

  * disabled—Configures the COM port 0 as a general purpose port for use with the Windows Operating System. 
  * enabled—Configures the COM port 0 as a remote management port for Windows Emergency Management services. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
Redirection After BIOS POST set console-redir-config putty-function-keypad |  Whether BIOS console redirection should be active after BIOS POST is complete and control given to the OS bootloader. This can be one of the following: 

  * always_enable—BIOS Legacy console redirection is active during the OS boot and run time. 
  * bootloader—BIOS Legacy console redirection is disabled before giving control to the OS boot loader. 
  * platform-default—The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

  
OS Watchdog Timer Policy scope token-feature "OS Boot Watchdog Timer Policy" scope token-param "OS Boot Watchdog Timer Policy" |  What action the system takes if the watchdog timer expires. This can be one of the following:

  * power_off—The server is powered off if the watchdog timer expires during OS boot. This is the default option. 
  * reset—The server is reset if the watchdog timer expires during OS boot. 

  
FRB 2 Timer scope token-feature "FRB 2 Timer" scope token-param "FRB 2 Timer" |  Whether the FRB2 timer is used for recovering the system if it hangs during POST. This can be one of the following:

  * disabled—The FRB2 timer is not used. 
  * enabled—The FRB2 timer is started during POST and used to recover the system if necessary. This is the default option. 

  
OS Watchdog Timer scope token-feature "OS Boot Watchdog Timer" scope token-param "OS Boot Watchdog Timer" |  Whether the BIOS programs the watchdog timer with a specified timeout value. This can be one of the following:

  * disabled—The watchdog timer is not used to track how long the server takes to boot. This is the default option. 
  * enabled—The watchdog timer tracks how long the server takes to boot. This is the default option. 

  
OS Watchdog Timer Timeout scope token-feature "OS Boot Watchdog Timer Timeout" scope token-param "OS Boot Watchdog Timer Timeout" |  If OS does not boot within the specified time, OS watchdog timer expires and system takes action according to timer policy. This can be one of the following: 

  * 5 minutes—The OS watchdog timer expires 5 minutes after it begins to boot. 
  * 10 minutes—The OS watchdog timer expires 10 minutes after it begins to boot. This is the default option. 
  * 15 minutes—The OS watchdog timer expires 15 minutes after it begins to boot. 
  * 20 minutes—The OS watchdog timer expires 20 minutes after it begins to boot. 

|  **Note** |  This option is applicable only when you enable the OS Boot Watchdog Timer.  
---|---

---

## Page 17: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Server-Mgmt/4-3/m_server_management_overview-4_1.html

## Server Management Overview  
  
Cisco UCS Manager enables you to manage general and complex server deployments. For example, you can manage a general deployment with a pair of Fabric Interconnects (FIs), which is the redundant server access layer that you get with the first chassis that can scale up to 20 chassis' and up to 160 physical servers. This can be a combination of blades and rack mount servers to support the workload in your environment. As you add more servers, you can continue to perform server provisioning, device discovery, inventory, configuration, diagnostics, monitoring, fault detection, and auditing. 

Beginning with release 4.3(6a), Cisco UCS Manager introduces support for the following Cisco UCS hardware: 

  * Cisco UCS X210c M8 Compute Node

  * UCS C240 M8 Server

  * UCS C220 M8 Server


Beginning with release 4.3(5a), Cisco UCS Manager introduces support for the following Cisco UCS hardware: 

  * Cisco UCS X215c M8 Compute Node

  * Cisco UCS C225 M8 Server


Beginning with release 4.3(4b), Cisco UCS Manager introduces support for Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct). 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For more information, see [Cisco UCS Manager Fabric Interconnects](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Getting-Started/4-3/b_ucsm_getting_started_guide_4_3/m_overview.html#d3765e974a1635). 

* * *  
  
---|---  
  
Beginning with release 4.3(4b), Cisco UCS Manager introduces support for the following Cisco UCS hardware: 

  * Cisco UCS C245 M8 Server


Beginning with release 4.3(6c), Cisco UCS Manager introduces support for the following Cisco UCS hardware: 

  * Cisco UCS VIC 15230

  * Cisco UCS VIC 15427

  * Cisco UCS VIC 15237 mLOM


Beginning with release 4.3(2b), Cisco UCS Manager introduces support for the following Cisco UCS hardware: 

  * Cisco UCS X410c M7 Compute Node

  * Cisco UCS X210c M7 Compute Node

  * Cisco UCS X210c M6 Compute Node

  * Cisco UCS C240 M7 Server

  * Cisco UCS C220 M7 Server

  * Cisco UCS VIC 15235 (PCIe) (Secure Boot) 

  * Cisco UCS VIC 14425 (PCIe) (Secure Boot) 

  * Cisco UCS VIC 15231 (mLOM) (Non-Secure Boot) 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCS VIC 15231 is not supported with Cisco UCS VIC 15422 mezzanine adapter.

* * *  
  
---|---  
  * Cisco UCS VIC 15420 (mLOM) (Secure Boot) 

  * Cisco UCS VIC 15422 (mezz) (Secure Boot) 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCS VIC 15422 is a mezzanine adapter that requires UCS VIC 15000 bridge connector (UCSX-V5-BRIDGE) and VIC 15420 mLOM on X210c M6 and X210c M7 compute node. 

* * *  
  
---|---  
  * Cisco UCS VIC 14425 (mLOM) 

  * Cisco UCS VIC 14825 (mezz) 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCS VIC 14825 is a mezzanine adapter that requires UCS 14000 bridge connector (UCSX-V4-BRIDGE) and VIC 14425 mLOM on X210c M6 compute node. 

* * *  
  
---|---  

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

  * Before inserting Cisco UCS VIC 15235 and VIC 15425 adapters into a server, upgrade the server with UCS 4.3(2a) or later release C-bundle software. If these adapters are inserted into the server which is running lower than 4.3(2a) release, upgrade the server to UCS 4.3(2a) or later release C-bundle software and then power cycle the server to recognize the adapters. 
  * Cisco UCS VIC 15000 series and Cisco UCS VIC 14000 series adapters or Cisco UCS 15000 series and Cisco UCS VIC 1400 series adapters cannot be installed together on Cisco UCS B-Series servers. 
  * Cisco UCS VIC 1400 series adapters are not supported on Cisco UCS M7 servers.


* * *  
  
---|---  
  
Beginning with release 4.2(3b), Cisco UCS Manager introduces support for the following Cisco UCS hardware: 

  * Cisco UCS VIC 15411 (mLOM) (Non-Secure Boot) 

  * Cisco UCS VIC 15238 (mLOM) (Non-Secure Boot) 

  * Cisco UCS 6536 Fabric Interconnect


Beginning with release 4.2(2a), Cisco UCS Manager introduces support for the following Cisco UCS hardware: 

  * Cisco UCS VIC 15428 (mLOM) (Non-Secure Boot) 


Beginning with release 4.2(1), Cisco UCS Manager introduces support for the following Cisco UCS hardware: 

  * Cisco UCS C220 M6 Server

  * Cisco UCS C240 M6 Server

  * Cisco UCS C225 M6 Server

  * Cisco UCS C245 M6 Server

  * Cisco UCS B200 M6 Server

  * Cisco UCS VIC 1467 (mLOM)

  * Cisco UCS VIC 1477 (mLOM)


The Cisco UCS 6536 Fabric Interconnect,  Cisco UCS 6400 Series Fabric Interconnect, and Cisco UCS 6332 Fabric Interconnects include centralized management. You can manage the UCS Blade Servers and Rack-Mount Servers that are in the same domain from one console. You can also manage the UCS Mini from the Cisco UCS Manager. 

To ensure the optimum server performance, you can configure the amount of power that you allocate to servers. You can also set the server boot policy, the location from which the server boots, and the order in which the boot devices are invoked. You can create service profiles and assign the service profiles to servers. In service profile, you can configure vNICs and vHBAs, enables BIOS settings, apply firmware policy, and other settings. When the service profile is associated to a server, the configured configurations, policies, and settings are pushed to the server. 

---

## Page 18: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Server-Mgmt/4-3/m_cli_managing_power_in_cisco_ucs.html

## Power Capping in Cisco UCS

You can control the maximum power consumption on a server through power capping, as well as manage the power allocation in the Cisco UCS Manager for blade servers, rack servers, UCS Mini, and mixed UCS domains. 

Cisco UCS Manager supports power capping on the following: 

  * Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct) 

  * UCS 6500 Series Fabric Interconnects

  * UCS 6400 Series Fabric Interconnects

  * UCS 6300 Series Fabric Interconnects 

  * UCS 6324 Series Fabric Interconnects (Cisco UCS Mini)


You can use Policy Driven Chassis Group Power Cap, or Manual Blade Level Power Cap methods to allocate power that applies to all of the servers in a chassis. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCSX-9508 Chassis supports Policy Driven Chassis Group Cap.  When you choose to select Policy Driven Chassis Group Cap, Cisco UCS Manager calculates the power allotment for Cisco UCSX-9508 Chassis and when you choose to select Manual Blade Level Power Cap, Chassis Management Controller (CMC) calculates the power allotment for Cisco UCSX-9508 Chassis. 

* * *  
  
---|---  
  
Cisco UCS Manager provides the following power management policies to help you allocate power to your servers: 

Power Management Policies  |  Description   
---|---  
Power Policy |  Specifies the redundancy for power supplies in all chassis in a Cisco UCS domain.   
Power Control Policies |  Specifies the priority to calculate the initial power allocation for each blade in a chassis.   
Power Save Policy |  Globally manages the chassis to maximize energy efficiency or availability.  
Cisco UCSX-9508 Chassis Power Extended Policy |  Manages the chassis to maximize energy efficiency or availability.  Power Extended Policy is effective only when we have PSU Redundant Policy Mode. For example, the total power available can be extended when we have N+1, N+2 and Grid to PSU Redundancy modes.   
Cisco UCSX-9508 Chassis Fan Control Policy |  Manages you to control the fan speed to bring down server power consumption and noise levels.  
Global Power Allocation |  Specifies the Policy Driven Chassis Group Power Cap or the Manual Blade Level Power Cap to apply to all servers in a chassis.   
Global Power Profiling  |  Specifies how the power cap values of the servers are calculated. If it is enabled, the servers will be profiled during discovery through benchmarking. This policy applies when the Global Power Allocation Policy is set to Policy Driven Chassis Group Cap. 

---

## Page 19: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Server-Mgmt/4-3/m_cli_configuring_server_boot.html

##  Boot Policy  
  
The Cisco UCS Manager enables you to create a boot policy for blade servers and rack servers. 

The Cisco UCS Manager boot policy overrides the boot order in the BIOS setup menu and determines the following: 

  * Selection of the boot device 

  * Location from which the server boots 

  * Order in which boot devices are invoked 


For example, you can have associated servers boot from a local device, such as a local disk or CD-ROM (VMedia), or you can select a SAN boot or a LAN (PXE) boot. 

You can either create a named boot policy to associate with one or more service profiles, or create a boot policy for a specific service profile. A boot policy must be included in a service profile, and that service profile must be associated with a server for it to take effect. If you do not include a boot policy in a service profile, Cisco UCS Manager applies the default boot policy. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Changes to a boot policy might be propagated to all servers created with an updating service profile template that includes that boot policy. Re-association of the service profile with the server to rewrite the boot order information in the BIOS is automatically triggered.  You can also specify the following for the boot policy: 

  * Local LUN name. The name specified is the logical name in the storage profile, not the deployed name. Specify only a primary name. Specifying a secondary name results in a configuration error. 
  * Specific JBOD disk number for booting from JBOD disks. 
  * Any LUN for backward compatibility; however, we do not recommend this. Other devices must not have bootable images to ensure a successful boot. 


* * *  
  
---|---

---

## Page 20: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Server-Mgmt/4-3/m_cli_managing_blade_servers.html

## Blade Server Management   
  
You can manage and monitor all blade servers in a Cisco UCS domain through Cisco UCS Manager. You can perform some blade server management tasks, such as changes to the power state, from the server and service profile. 

The remaining management tasks can only be performed on the server. 

The power supply units go into power save mode when a chassis has two blades or less. When a third blade is added to the chassis and is fully discovered, the power supply units return to regular mode. 

If a blade server slot in a chassis is empty, Cisco UCS Manager provides information, errors, and faults for that slot. You can also re-acknowledge the slot to resolve server mismatch errors and to have Cisco UCS Manager rediscover the blade server in the slot. 

---

## Page 21: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Server-Mgmt/4-3/m_cli_managing_licenses.html

## Licenses

Cisco UCS Fabric Interconnect are equipped with pre-installed port licenses, providing the option to purchase them fully licensed, partially licensed, or add licenses after delivery. The licensing model varies across different Fabric Interconnect series, with some models adopting perpetual software licenses to simplify license management. 

**Perpetual Licensing for Cisco UCS 6500 Seriesand Cisco UCS X-Series Direct Fabric Interconnects**

Cisco UCS 6536 Fabric Interconnect (UCS-FI-6536): Starting with release 4.2(3b), all ports and software features are activated through a perpetual software license. No additional license management is required. 

**Cisco UCS 9108 100G Fabric Interconnect (X-Series Direct)** : Starting with release 4.3(4b), all ports and software features are similarly activated through a perpetual software license. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct) and UCS-FI-6536 do not use port-based licensing like previous generations of fabric interconnects. 

* * *  
  
---|---  
  
Cisco UCS 64108 Fabric Interconnect uses the following licenses: 

Table 1. Cisco UCS 64108 Fabric Interconnect Licenses Ports |  Licenses  
---|---  
Ports 1-96 |  ETH_PORT_ACTIVATION_PKG and ETH_PORT_C_ACTIVATION_PKG - Licenses used for 10/25 GB Ethernet ports  
Ports 97-108 |  100G_ETH_PORT_ACTIVATION_PKG – Licenses used for 40/100 GB Ethernet ports   
  
Cisco UCS 6454 Fabric Interconnect uses the following licenses: 

Table 2. Cisco UCS 6454 Fabric Interconnect Licenses Ports |  Licenses  
---|---  
Ports 1-48 |  ETH_PORT_ACTIVATION_PKG and ETH_PORT_C_ACTIVATION_PKG - Licenses used for 10/25 GB Ethernet ports  
Ports 49-54 |  100G_ETH_PORT_ACTIVATION_PKG – Licenses used for 40/100 GB Ethernet ports   
  
The following four licenses are for the 6300 Series FI and are only valid on the 6332 and 6332-16UP FIs. 

  * 40G_ETH_PORT_ACTIVATION_PKG – Licenses used for 40 GB Ethernet ports 

  * 40G_ETH_C_PORT_ACTIVATION_PKG – Licenses used for 40 GB Ethernet ports directly connected to rack servers (C-Direct) 

  * 10G_C_PORT_ACTIVATION_PKG – Licenses used for the first 16 10 GB unified ports on the 6332-16UP that are directly connected to rack servers (C-Direct) 

  * 10G_PORT_ACTIVATION_PKG – Licenses used for the first 16 10 GB unified ports on the 6332-16UP 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The 10G_PORT_ACTIVATION_PKG and 10G_C_PORT_ACTIVATION_PKG licenses are only valid for the 6332-16UP FIs, and can only be installed on them. 

* * *  
  
---|---  


The following licenses are used when S3260 system is connected to FI as appliance (appliance port) or Cisco UCS Manager managed node (server port): 

Table 3. S3260 system License Requirement FI Model |  License  
---|---  
Cisco UCS 6536  |  Perpetual software license.  
6454 and 64108 |  10G_PORT_ACTIVATION_PKG  
6332-16UP |  10G_PORT_ACTIVATION_PKG  
6332 |  10G_PORT_ACTIVATION_PKG  
  
Cisco UCS C125 M5 Servers support Cisco UCS 6500 Series Fabric Interconnect, Cisco UCS 6400 Series Fabric Interconnect and 6300 Series Fabric Interconnect. 

Fabric Interconnect  |  Default Base Licenses   
---|---  
Cisco UCS 9108 100G Intelligent Fabric Module (Cisco UCS X-Series Direct)  |  Perpetual software license. This license activates all the ports and software features of Cisco UCS X-Series Direct.   
Cisco UCS 6536  |  Perpetual software license. This license activates all the ports and software features of 6536 Fabric Interconnect.  
Cisco UCS 64108  |  For 36 10/25 GB ports (ports 1-96) For 4 40/100 GB ports (ports 97-108).  
Cisco UCS 6454  |  For 18 10/25 GB ports (ports 1-48) For 2 40/100 GB ports (ports 49-54).  
Cisco UCS 6332  |  For eight 40 GB ports.   
Cisco UCS 6332 16UP  |  For four 40 GB ports and eight 10 GB ports.  |  **Note** |  The first 16 ports are 10 GB. The remaining are 40 GB.   
---|---  
Cisco UCS 6324  |  For 4 non-breakout ports only. The fifth port, which does not include a license, is further broken in to four 10 GB ports.   
Port License Consumption

Port licenses are not bound to physical ports. When you disable a licensed port, that license is retained for use with the next enabled port. To use additional fixed ports, you must purchase and install licenses for those ports. All ports, regardless of their type (fibre, ethernet) consume licenses if they are enabled. 

For breakout capable ports available in the 6332 and the 6332-16UP platforms, 40 GB licenses remain applied to the main port even if that port is a breakout port, and that port continues to consume only one 40 GB license. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

Licenses are not portable across product generations. 

* * *  
  
---|---  
  
Each Cisco UCS 6324 Fabric Interconnect comes with a factory installed port license that is shipped with the hardware. The C-direct port license is factory installed with a grace period, measured from first use of the port, and can be used for Cisco UCS rack servers. If multiple ports are acting within grace periods, the license is moved to the port whose grace period is closest to expiring. 

### Grace Period

If you attempt to use a port that does not have an installed license, Cisco UCS initiates a 120 day grace period. The grace period is measured from the first use of the port without a license and is paused when a valid license file is installed. The amount of time used in the grace period is retained by the system. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Each physical port has its own grace period. Initiating the grace period on a single port does not initiate the grace period for all ports. 

* * *  
  
---|---  
  
If a licensed port is unconfigured, that license is transferred to a port functioning within a grace period. If multiple ports are acting within grace periods, the license is moved to the port whose grace period is closest to expiring. 

### High Availability Configurations

To avoid inconsistencies during failover, we recommend that both Fabric Interconnects in the cluster have the same number of ports licensed. If symmetry is not maintained and failover occurs, Cisco UCS enables the missing licenses and initiates the grace period for each port being used on the failover node. 

---

## Page 22: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Server-Mgmt/4-3/m_cli_firmware_upgrades.html

## Firmware Upgrades 

Beginning with Cisco UCS Manager Release 4.2(3), Cisco is releasing unified Cisco UCS Manager software and firmware upgrades for the following platforms with every release of Cisco UCS Manager: 

  * Cisco UCS Fabric Interconnects 9108 100G with Cisco UCS X-Series servers. 

  * Cisco UCS 6500 Series Fabric Interconnect with Cisco UCS B-Series, C-Series, and S-Series servers. 

  * Cisco UCS 6400 Series Fabric Interconnect with Cisco UCS B-Series, C-Series, and S-Series servers. 

  * Cisco UCS 6300 Series Fabric Interconnect with Cisco UCS B-Series, C-Series, and S-Series servers.

  * Cisco UCS 6324 Fabric Interconnect with Cisco UCS B-Series Servers and C-Series Servers, which is also known as UCS Mini.


You can upgrade the firmware through Auto Install, packages in service profiles, using the firmware automatic synchronization server policy, and directly at endpoints. For more information on guidelines and installing firmware, see the Cisco UCS Firmware Management Guide. 

---

## Page 23: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Server-Mgmt/4-3/m_cli_configuring_service_profiles.html

## Service Profiles in UCS Manager 

A service profile defines a single server and its storage and networking characteristics. You can create a service profile for Cisco UCS Manager and UCS Mini. When a service profile is deployed to a server, UCS Manager automatically configures the server, adapters, fabric extenders, and fabric interconnects to match the configuration specified in the service profile. 

A service profile includes four types of information: 

  * Server definition: Defines the resources (e.g. a specific server or a blade inserted to a specific chassis) that are required to apply to the profile. 

  * Identity information: Includes the UUID, MAC address for each virtual NIC (vNIC), and WWN specifications for each HBA. 

  * Firmware revision specifications: Used when a certain tested firmware revision is required to be installed or for some other reason a specific firmware is used. 

  * Connectivity definition: Configures network adapters, fabric extenders, and parent interconnects, however this information is abstract as it does not include the details of how each network component is configured. 


The UCS system provides two types of service profiles: Service profiles that inherit server identity and service profiles that override server identity. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

A server can also show a Server Personality field in server properties. This field displays the server personality configuration of Hyperconverged Infrastructure (HCI). Cisco UCS M6 servers and later versions can function as either as a standard UCS servers or HCI servers.  The server personality field is informational cannot be reset in the UCS Manager GUI, indicating the specific configuration or role assigned to the server, and is only visible if a server personality is configured.  The UCS Manager CLI provides a command line option to revert the server back to a "no personality" state. For more information, see _Clearing the Server Personality Field_ section in [Cisco UCS Manager Server Management Using the CLI](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) guide. 

* * *  
  
---|---

---
