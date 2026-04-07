# UCS Manager CLI Network Management Guide 4.3

| | |
|---|---|
| **URL Title** | UCS Manager CLI Network Management Guide 4.3 |
| **URL** | https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Network-Mgmt/4-3/b_cli_ucsm_network_management_guide_4_3.html |
| **Long URL** |  |
| **HTML Title** | Cisco UCS Manager Network Management Guide Using the CLI, Release 4.3 |
| **Source file** | `ucs-docs-raw/html/b_cli_ucsm_network_management_guide_4_3.html` |
| **File type** | HTML |
| **Fetched on** | 2026-04-08 08:42:02 |

---

## Page 1: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Network-Mgmt/4-3/b_cli_ucsm_network_management_guide_4_3.html

![Clear Contents of Search](/etc/designs/cdc/fw/i/ic_clear_gray.png)

---

## Page 2: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Network-Mgmt/4-3/b_cli_ucsm_network_management_guide_4_3/b_CLI_UCSM_Network_Management_Guide_preface_00.html

## Audience

This guide is intended primarily for data center administrators with responsibilities and expertise in one or more of the following: 

  * Server administration 

  * Storage administration 

  * Network administration 

  * Network security 


---

## Page 3: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Network-Mgmt/4-3/b_cli_ucsm_network_management_guide_4_3/b_CLI_UCSM_Network_Management_Guide_chapter_01.html

## New and Changed Information

This section provides information on new features and changed behavior in Cisco UCS Manager, Release 4.3. 

Table 1. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(6c) Feature  |  Description  |  Where Documented   
---|---|---  
Support for RS Cons 16 and RS 1eee configuration options |  Cisco UCS Manager now supports RS Cons 16 and RS 1eee configuration options for Ethernet Port Forward Error Correction. | 

  * [Configuring an Uplink Ethernet Port for Forward Error Correction](b_CLI_UCSM_Network_Management_Guide_chapter_0100.html#task_ftg_gvm_d2b)
  * [Configuring an Appliance Port for Forward Error Correction](b_CLI_UCSM_Network_Management_Guide_chapter_0100.html#task_ftg_gvm_d2b_app)

  
Table 2. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(5a) Feature  |  Description  |  Where Documented   
---|---|---  
Configuring MACsec Key with Type 6 |  Cisco UCS Manager adds support for configuring Media Access Control Security (MACsec) with Type 6 encryption, utilizing the Advanced Encryption Standard (AES).  |  [Creating a MACsec Key](m-cli-macsec-4-3.html#configuring-a-macsec-keychain-and-keys)  
Table 3. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(4b) Feature  |  Description  |  Where Documented   
---|---|---  
Support for Cisco UCS Fabric Interconnects 9108 100G | Cisco UCS Manager now supports Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct)  | 

  * [Guidelines for Configuring Unified Ports](b_CLI_UCSM_Network_Management_Guide_chapter_0100.html#concept_0249934662D1439AA5E926A503AC8B4B)
  * [Fabric Interconnect Port Types](b_CLI_UCSM_Network_Management_Guide_4_1_chapter_011.html#concept_551C21C9FE2F45E9BFE81361FA47E42C)
  * [Unified Ports on 6300 Series Fabric Interconnects](b_CLI_UCSM_Network_Management_Guide_chapter_0100.html#concept_EBA4291165434774AB50F91C74633538)
  * [Port Breakout Functionality on Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct)](b_CLI_UCSM_Network_Management_Guide_chapter_0100.html#port-breakout-functionality-on-cisco-ucs-x-direct)
  * [Configuring Multiple Breakout Ports](b_CLI_UCSM_Network_Management_Guide_chapter_0100.html#task_36B159CB4E204986A5692F4D645F8F2C)
  * [Configuring Breakout Appliance Ports](b_CLI_UCSM_Network_Management_Guide_chapter_0100.html#task_A85F71DFA78543959CA64713660A591B)
  * [Configuring Ethernet Breakout Ports on Cisco UCS Fabric Interconnects 9108 100G](b_CLI_UCSM_Network_Management_Guide_chapter_0100.html#Cisco_Task_in_List_GUI.dita_2eb4b4d0-ea28-4eac-98bc-153d9574a3b6)
  * [Configuring Breakout Appliance Ports](b_CLI_UCSM_Network_Management_Guide_chapter_0100.html#task_A85F71DFA78543959CA64713660A591B)
  * [Configuring Q-in-Q Forwarding](b_CLI_UCSM_Network_Management_Guide_chapter_0100.html#Cisco_Task.dita_f1691856-af85-42a8-83d0-ce75909c4c23)
  * [Unconfiguring Q-in-Q Forwarding](b_CLI_UCSM_Network_Management_Guide_chapter_0100.html#Cisco_Task.dita_91fe934d-6ded-4a29-81b2-548512392ff9)
  * [Configuring FCoE Uplink for Forward Error Correction](b_CLI_UCSM_Network_Management_Guide_chapter_0100.html#task_c5p_rqt_k2b)
  * [Named VLANs](b_CLI_UCSM_Network_Management_Guide_chapter_0101.html#concept_D1DA6EF2EF0446099CFC3FAD4AEBDB87)
  * [VLAN Port Count Optimization](b_CLI_UCSM_Network_Management_Guide_chapter_0101.html#concept_4BA5803EA5134951BAB8C42025832137)
  * [VIC QinQ Tunneling - Supported Combinations and Limitations](b_CLI_UCSM_Network_Management_Guide_chapter_0101.html#receive-side-scaling-version-2-limitations)
  * [Quality of Service](b_CLI_UCSM_Network_Management_Guide_chapter_01000.html#concept_ED0A5836EDCB4F3C9128AB453351698A)
  * [Multicast Policy](b_CLI_UCSM_Network_Management_Guide_chapter_01011.html#concept_84AC40A047CC4E10B4CD2FBFCDFC6262)
  * [Guidelines and Limitations for MACsec](m-cli-macsec-4-3.html#c-guidelines-and-limitations-for-macsec)

  
Table 4. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(4b) Feature  |  Description  |  Where Documented   
---|---|---  
Support for Cisco UCS C-Series M8 servers | Cisco UCS Manager now supports Cisco UCS C245 M8 Servers.  | 

  * [Receive Side Scaling Version 2 (RSSv2)](b_CLI_UCSM_Network_Management_Guide_chapter_01011.html#rssv2)
  * [Single Root I/O Virtualization HPN Connection Policy](b_CLI_UCSM_Network_Management_Guide_chapter_01011.html#sriov-hpn-policy-cli)

  
Table 5. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(4a) Feature  |  Description  |  Where Documented   
---|---|---  
Configuring MACsec | Cisco UCS Manager introduces support for configuring Media Access Control Security (MACsec) encryption. | [About MACsec](m-cli-macsec-4-3.html#c-about-macsec)  
Table 6. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(2c) Feature  |  Description  |  Where Documented   
---|---|---  
Support Cisco UCS X-Series Servers |  Cisco UCS Manager supports Cisco UCS X410c M7 Compute Node.  Cisco UCS X-Series servers support Intelligent Fabric Modules (IFM), which function similarly to the Input/Output Module (IOM) in Cisco UCS B-Series servers.  |  —  
Support for Cisco UCS VIC cards |  Cisco UCS Manager supports the following Cisco UCS VIC cards:

  * Cisco UCS VIC 15230
  * Cisco UCS VIC 15427
  * Cisco UCS VIC 15237 mLOM

|  —  
Table 7. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(2b) Feature  |  Description  |  Where Documented   
---|---|---  
Support Cisco UCS C-Series M7 servers |  Cisco UCS Manager supports the following C-Series M7 servers:

  * Cisco UCS C240 M7 Server
  * Cisco UCS C220 M7 Server

|  —  
Support Cisco UCS X-Series chassis and servers |  Cisco UCS Manager supports Cisco UCS X9508 server chassis with the following Cisco UCS X-Series servers:

  * Cisco UCS X210c M7 Compute Node
  * Cisco UCS X210c M6 Compute Node

Cisco UCS X-Series servers support Intelligent Fabric Modules (IFM), which function similarly to the Input/Output Module (IOM) in Cisco UCS B-Series servers.  |  —  
Support for Receive Side Scaling Version 2 | Cisco UCS Manager introduces support for Receive Side Scaling Version 2 | 

  * [Receive Side Scaling Version 2 (RSSv2)](b_CLI_UCSM_Network_Management_Guide_chapter_01011.html#rssv2)
  * [Configuring an Ethernet Adapter Policy to Enable RSS on Windows Operating Systems](b_CLI_UCSM_Network_Management_Guide_chapter_01011.html#task_5DD4B30A2263454D95C6C38881F009F0)

  
Support for VIC QinQ Tunneling | Cisco UCS Manager introduces support for VIC QinQ Tunneling. | 

  * [VIC QinQ Tunneling](b_CLI_UCSM_Network_Management_Guide_chapter_0101.html#vic-qinq-tunneling)
  * [Enabling QinQ on a vNIC of LAN Connectivity Policy](b_CLI_UCSM_Network_Management_Guide_chapter_0101.html#creating-a-qinq-offload)
  * [Enabling QinQ on a vNIC of a Service Profile](b_CLI_UCSM_Network_Management_Guide_chapter_0101.html#creating-a-qinq-offload)
  * [Enabling QinQ on a vNIC Template](b_CLI_UCSM_Network_Management_Guide_chapter_0101.html#creating-a-qinq-offload)
  * [Viewing QinQ](b_CLI_UCSM_Network_Management_Guide_chapter_0101.html#creating-a-qinq-offload)
  * [Disabling QinQ on a vNIC of a Service Profile](b_CLI_UCSM_Network_Management_Guide_chapter_0101.html#creating-a-qinq-offload)
  * [Disabling QinQ on a vNIC Template](b_CLI_UCSM_Network_Management_Guide_chapter_0101.html#creating-a-qinq-offload)
  * [Disabling QinQ on a vNIC of LAN Connectivity Policy](b_CLI_UCSM_Network_Management_Guide_chapter_0101.html#creating-a-qinq-offload)
  * [Adding a VLAN on a vNIC Template](b_CLI_UCSM_Network_Management_Guide_chapter_0101.html#configuring-a-vnic-template)
  * [Adding a VLAN on a vNIC of LAN Connectivity Policy](b_CLI_UCSM_Network_Management_Guide_chapter_0101.html#create-vlan)
  * [Adding a VLAN on a vNIC of a Service Profile](b_CLI_UCSM_Network_Management_Guide_chapter_0101.html#create-vlan)
  * [Deleting a VLAN in a VNIC template](b_CLI_UCSM_Network_Management_Guide_chapter_0101.html#create-vlan)
  * [Deleting a VLAN on a vNIC of LAN Connectivity Policy](b_CLI_UCSM_Network_Management_Guide_chapter_0101.html#create-vlan)
  * [Deleting a VLAN on a vNIC of a Service Profile](b_CLI_UCSM_Network_Management_Guide_chapter_0101.html#create-vlan)
  * [VIC QinQ Tunneling - Supported Combinations and Limitations](b_CLI_UCSM_Network_Management_Guide_chapter_0101.html#receive-side-scaling-version-2-limitations)

  
Support for SR-IOV | Cisco UCS Manager provides Single Root I/O Virtualization High Performance Networking (SRIOV-HPN) Connection Policy support. | 

  * [Single Root I/O Virtualization HPN Connection Policy](b_CLI_UCSM_Network_Management_Guide_chapter_01011.html#sriov-hpn-policy-cli)
  * [Configuring SRIOV HPN Connection Policy](b_CLI_UCSM_Network_Management_Guide_chapter_01011.html#configuring-sriov-hpn-connection-policy)
  * [Assigning SRIOV-HPN Connection Policy to a vNIC](b_CLI_UCSM_Network_Management_Guide_chapter_01011.html#assigning-sriov-hpn-connection-policy-to-a-vnic)
  * [Deleting SRIOV HPN Connection Policy](b_CLI_UCSM_Network_Management_Guide_chapter_01011.html#deleting-sriov-hpn-connection-policy)

  
Deprecated support for Cisco UCS B-Series and C-Series M4 servers |  Cisco UCS Manager deprecates support for Cisco UCS B-Series and C-Series M4 servers. |  —  
Deprecated support for Cisco UCS 6200 series Fabric Interconnect |  Cisco UCS Manager deprecates support for Cisco UCS 6200 series Fabric Interconnects. |  —

---

## Page 4: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Network-Mgmt/4-3/b_cli_ucsm_network_management_guide_4_3/b_CLI_UCSM_Network_Management_Guide_chapter_010.html

## Overview  
  
This guide includes the following information: 

  * Configure/Enable Server Ports; Configure/Enable Uplink Ports; Configure/Enable FC Ports. 

  * Create LAN Pin Groups 

  * Create VLANs and VLAN groups 

  * Create Server Links 

  * Configure QoS System Class 

  * Configure Global Policies 

  * Monitor Network Health 

  * Traffic Monitoring 


---

## Page 5: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Network-Mgmt/4-3/b_cli_ucsm_network_management_guide_4_3/b_CLI_UCSM_Network_Management_Guide_4_1_chapter_011.html

## Fabric Interconnect Overview 

The fabric interconnect is the core component of Cisco UCS. The Cisco UCS Fabric Interconnects provide uplink access to LAN, SAN, and out-of-band management segment. Cisco UCS infrastructure management is through the embedded management software, Cisco UCS Manager, for both hardware and software management. The Cisco UCS Fabric Interconnects are Top-of-Rack devices, and provide unified access to the Cisco UCS domain. 

The Cisco UCS FIs provide network connectivity and management for the connected servers. The Cisco UCS Fabric Interconnects run the Cisco UCS Manager control software and consist of expansion modules for the Cisco UCS Manager software. 

For more information about Cisco UCS Fabric Interconnects, see the Cisco UCS Manager Getting Started Guide. 

---

## Page 6: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Network-Mgmt/4-3/b_cli_ucsm_network_management_guide_4_3/b_CLI_UCSM_Network_Management_Guide_chapter_0100.html

## Unified Ports on 6300 Series Fabric Interconnects 

Unified ports are ports on the Cisco UCS 6300 Series Fabric Interconnects that you can configure to carry either Ethernet or Fibre Channel traffic. A Cisco UCS domain cannot use these un-reserved ports until you configure them. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

When you configure a port on a fabric interconnect, the administrative state is automatically set to enabled. If the port is connected to another device, this may cause traffic disruption. You can disable the port after configuring it. Configurable beacon LEDs indicate which unified ports are configured for the selected port mode. 

* * *  
  
---|---  
  
### Port Modes

The port mode determines whether a unified port on the fabric interconnect is configured to carry Ethernet or Fibre Channel traffic. You configure the port mode in Cisco UCS Manager. However, the fabric interconnect does not automatically discover the port mode. 

Changing the port mode deletes the existing port configuration and replaces it with a new logical port. Any objects associated with that port configuration, such as VLANs and VSANS, are also removed. There is no restriction on the number of times you can change the port mode for a unified port. 

### Port Types

The port type defines the type of traffic carried over a unified port connection. 

By default, unified ports changed to Ethernet port mode are set to the Ethernet uplink port type. Unified ports changed to Fibre Channel port mode are set to the Fibre Channel uplink port type. You cannot unconfigure Fibre Channel ports. 

Changing the port type does not require a reboot. 

Ethernet Port Mode

When you set the port mode to Ethernet, you can configure the following port types: 

  * Server ports 

  * Ethernet uplink ports 

  * Ethernet port channel members 

  * FCoE ports 

  * Appliance ports 

  * Appliance port channel members 

  * SPAN destination ports 

  * SPAN source ports 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For SPAN source ports, configure one of the port types and then configure the port as SPAN source. 

* * *  
  
---|---  


Fibre Channel Port Mode

When you set the port mode to Fibre Channel, you can configure the following port types: 

  * Fibre Channel uplink ports 

  * Fibre Channel port channel members

  * Fibre Channel storage ports 

  * SPAN source ports 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For SPAN source ports, configure one of the port types and then configure the port as SPAN source. 

* * *  
  
---|---  


### Data Traffic Interruption from Port Mode Changing 

Port mode changes can cause an interruption to the data traffic for the Cisco UCS domain. The length of the interruption and the affected traffic depend upon the configuration of the Cisco UCS domain and the module on which you made the port mode changes. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/tip.gif)  
**Tip** | 

* * *

To minimize traffic disruption during system changes, form a Fibre Channel uplink port-channel across the fixed and expansion modules. 

* * *  
  
---|---  
  
#### Impact of Port Mode on an Expansion Module 

After you make port mode changes on an expansion module, the module reboots. All traffic through port on the expansion module is interrupted for approximately 1 minute while the module reboots. 

#### Impact of Port Mode Changes on the Fixed Module in a Cluster Configuration 

A cluster configuration has two fabric interconnects. After you make port changes to the fixed module, the fabric interconnect reboots. The impact on the data traffic depends upon whether or not you have configured the server vNICs to failover to the other fabric interconnect when one fails. 

If you change the port modes on the expansion module of one fabric interconnect and then wait for that to reboot before changing the port modes on the second fabric interconnect, the following occurs: 

  * With server vNIC failover, traffic fails over to the other fabric interconnect and no interruption occurs. 

  * Without server vNIC failover, all data traffic through the fabric interconnect on which you changed the port modes is interrupted for approximately eight minutes while the fabric interconnect reboots. 


When you change the port modes on the fixed modules of both fabric interconnects simultaneously, all data traffic through the fabric interconnects are interrupted for approximately eight minutes while the fabric interconnects reboot. 

#### Impact of Port Mode Changes on the Fixed Module in a Standalone Configuration 

A standalone configuration has only one fabric interconnect. After you make port changes to the fixed module, the fabric interconnect reboots. All data traffic through the fabric interconnect is interrupted for approximately eight minutes while the fabric interconnect reboots. 

### Guidelines for Configuring Unified Ports 

Consider the following guidelines and restrictions when configuring unified ports: 

#### Port Mode Placement 

Because the Cisco UCS Manager GUI interface uses a slider to configure the port mode for unified ports on a fixed or expansion module, it automatically enforces the following restrictions which limits how port modes can be assigned to unified ports. When using the Cisco UCS Manager CLI interface, these restrictions are enforced when you commit the transaction to the system configuration. If the port mode configuration violates any of the following restrictions, the Cisco UCS Manager CLI displays an error: 

  * Ethernet ports must be grouped together in a block. For each module (fixed or expansion), the Ethernet port block must start with the first port and end with an even numbered port. 

  * Fibre Channel ports must be grouped together in a block. For each module (fixed or expansion), the first port in the Fibre Channel port block must follow the last Ethernet port and extend to include the rest of the ports in the module. For configurations that include only Fibre Channel ports, the Fibre Channel block must start with the first port on the fixed or expansion module. 

  * Alternating Ethernet and Fibre Channel ports is not supported. 


**Example of a valid configuration** — Might include unified ports 1–16 on the fixed module configured in Ethernet port mode and ports 17–32 in Fibre Channel port mode. On the expansion module you could configure ports 1–4 in Ethernet port mode and then configure ports 5–16 in Fibre Channel mode. The rule about alternating Ethernet and Fibre Channel port types is not violated because this port arrangement complies with the rules on each individual module. 

**Example of an invalid configuration** — Might include a block of Fibre Channel ports starting with port 16. Because each block of ports has to start with an odd-numbered port, you would have to start the block with port 17. 

The total number of uplink Ethernet ports and uplink Ethernet port channel members that can be configured on each fabric interconnect is limited to 31. This limitation includes uplink Ethernet ports and uplink Ethernet port channel members configured on the expansion module. 

#### Special Considerations for UCS Manager CLI Users 

Because the Cisco UCS Manager CLI does not validate port mode changes until you commit the buffer to the system configuration, it is easy to violate the grouping restrictions if you attempt to commit the buffer before creating at least two new interfaces. To prevent errors, we recommend that you wait to commit your changes to the system configuration until you have created new interfaces for all of the unified ports changing from one port mode to another. 

Commiting the buffer before configuring multiple interfaces will result in an error, but you do not need to start over. You can continue to configure unified ports until the configuration satisfies the aforementioned requirements. 

### Cautions and Guidelines for Configuring Unified Uplink Ports and Unified Storage Ports 

The following are cautions and guidelines to follow while working with unified uplink ports and unified storage ports: 

  * In an unified uplink port, if you enable one component as a SPAN source, the other component will automatically become a SPAN source. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

If you create or delete a SPAN source under the Ethernet uplink port, Cisco UCS Manager automatically creates or deletes a SPAN source under the FCoE uplink port. The same happens when you create a SPAN source on the FCOE uplink port. 

* * *  
  
---|---  
  * You must configure a non default native VLAN on FCoE and unified uplink ports. This VLAN is not used for any traffic. Cisco UCS Manager will reuse an existing fcoe-storage-native-vlan for this purpose. This fcoe-storage-native-vlan will be used as a native VLAN on FCoE and unified uplinks. 

  * In an unified uplink port, if you do not specify a non default VLAN for the Ethernet uplink port the fcoe-storage-native-vlan will be assigned as the native VLAN on the unified uplink port. If the Ethernet port has a non default native VLAN specified as native VLAN, this will be assigned as the native VLAN for unified uplink port. 

  * When you create or delete a member port under an Ethernet port channel, Cisco UCS Manager automatically creates or deletes the member port under FCoE port channel. The same happens when you create or delete a member port in FCoE port channel. 

  * When you configure an Ethernet port as a standalone port, such as server port, Ethernet uplink, FCoE uplink or FCoE storage and make it a member port for an Ethernet or FCoE port channel, Cisco UCS Manager automatically makes this port a member of both Ethernet and FCoE port channels. 

  * When you remove the membership for a member port from being a member of server uplink, Ethernet uplink, FCoE uplink or FCoE storage, Cisco UCS Manager deletes the corresponding members ports from Ethernet port channel and FCoE port channel and creates a new standalone port. 

  * If you downgrade Cisco UCS Manager from release 2.1 to any of the prior releases, all unified uplink ports and port channels will be converted to Ethernet ports and Ethernet port channels when the downgrade is complete. Similarly, all the unified storage ports will be converted to appliance ports. 

  * For unified uplink ports and unified storage ports, when you create two interfaces, only one license is checked out. As long as either interface is enabled, the license remains checked out. The license will be released only if both the interfaces are disabled for a unified uplink port or a unified storage port. 


### Configuring the Port Mode 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Changing the port mode can cause an interruption in data traffic because changes to the fixed module require a reboot of the fabric interconnect.  If the Cisco UCS domain has a cluster configuration that is set up for high availability and servers with service profiles that are configured for failover, traffic fails over to the other fabric interconnect and data traffic is not interrupted when the port mode is changed on the fixed module. 

* * *  
  
---|---  
  
In the Cisco UCS Manager CLI, there are no new commands to support Unified Ports. Instead, you change the port mode by scoping to the mode for the desired port type and then creating a new interface. When you create a new interface for an already configured slot ID and port ID, UCS Manager deletes the previously configured interface and creates a new one. If a port mode change is required because you configure a port that previously operated in Ethernet port mode to a port type in Fibre Channel port mode, UCS Manager notes the change. 

Expansions modules are not supported with Cisco UCS Mini. 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope` `port-type-mode |  Enters the specified port type mode for one of the following port types: 

eth-server 
     For configuring server ports. 

eth-storage 
     For configuring Ethernet storage ports and Ethernet storage port channels. 

eth-traffic-mon 
     For configuring Ethernet SPAN ports. 

eth-uplink 
     For configuring Ethernet uplink ports. 

fc-storage 
     For configuring Fibre Channel storage ports. 

fc-traffic-mon 
     For configuring Fibre Channel SPAN ports. 

fc-uplink 
     For configuring Fibre Channel uplink ports and Fibre Channel uplink port channels.   
**Step 2** |  UCS-A /port-type-mode # scope fabric` `{a | b}  |  Enters the specified port type mode for the specified fabric.   
**Step 3** |  UCS-A /port-type-mode/fabric # create interface` `slot-id` `port-id |  Creates an interface for the specified port type.  If you are changing the port type from Ethernet port mode to Fibre Channel port mode, or vice-versa, the following warning appears:  `Warning: This operation will change the port mode (from Ethernet to FC or vice-versa). When committed, this change will require the module to restart.`  
**Step 4** |  Create new interfaces for other ports belonging to the Ethernet or Fibre Channel port block.  |  There are several restrictions that govern how Ethernet and Fibre Channel ports can be arranged on a fixed or expansion module. Among other restrictions, it is required that you change ports in groups of two. Violating any of the restrictions outlined in the Guidelines and Recommendations for Configuring Unified Ports section will result in an error.   
**Step 5** |  UCS-A /port-type-mode/fabric/interface # commit-buffer |  Commits the transaction to the system configuration.   
  
Based on the module for which you configured the port modes, data traffic for the Cisco UCS domain is interrupted as follows: 

  * Fixed module—The fabric interconnect reboots. All data traffic through that fabric interconnect is interrupted. In a cluster configuration that provides high availability and includes servers with vNICs that are configured for failover, traffic fails over to the other fabric interconnect and no interruption occurs. Changing the port mode for both sides at once results in both fabric interconnects rebooting simultaneously and a complete loss of traffic until both fabric interconnects are brought back up.

It takes about 8 minutes for the fixed module to reboot. 

  * Expansion module—The module reboots. All data traffic through ports in that module is interrupted. 

It takes about 1 minute for the expansion module to reboot. 


#### Example

The following example changes ports 3 and 4 on slot 1 from Ethernet uplink ports in Ethernet port mode to uplink Fibre Channel ports in Fibre Channel port mode: 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

This example is not applicable for Cisco UCS 6500 Series Fabric Interconnect. 

* * *  
  
---|---  
      
    
    UCS-A# **scope fc-uplink**
    UCS-A /fc-uplink # **scope fabric a**
    UCS-A /fc-uplink/fabric # **create interface 1 3**
    Warning: This operation will change the port mode (from Ethernet to FC or vice-versa). 
    When committed, this change will require the fixed module to restart.
    UCS-A /fc-uplink/fabric/interface* # **up**
    UCS-A /fc-uplink/fabric* #**create interface 1 4**
    Warning: This operation will change the port mode (from Ethernet to FC or vice-versa). 
    When committed, this change will require the fixed module to restart.
    UCS-A /fc-uplink/fabric/interface* #**commit-buffer**

Configuring Breakout Ports

### Port Breakout Functionality on Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct) 

The Cisco UCS Fabric Interconnects 9108 100G is equipped with advanced port breakout functionality, which allows network administrators to subdivide a single high-bandwidth port into multiple lower-bandwidth ports. This feature is particularly beneficial for optimizing port utilization, managing cabling complexity, and adapting to various bandwidth requirements. 

Physical Port |  Breakout Options |  Logical Ports After Breakout |  Supported Speeds through breakout cables  
---|---|---|---  
Ethernet 1/1 - Ethernet 1/8 |  4x25G |  Ethernet 1/1/1 to Ethernet 1/8/4 |  Up to 8x100 Gbps  
Fibre Channel 1/1 and 1/2 |  4x8G, 4x16G, 4x32G |  Fibre Channel 1/1/1 to Fibre Channel 1/2/4 |  Up to 8x32Gbps  
  
#### Breakout Port Guidelines

Breakout ports are supported as destinations for traffic monitoring. The following are the guidelines for breakout functionality for Cisco UCS Fabric Interconnects 9108 100G: 

  * Breakout Availability: Breakout functionality is available for physical ports 1-8. 

  * Ethernet Breakout: Ethernet breakout ports can be configured on physical ports 1 through 8, resulting in 32 logical ports. 

  * Fibre Channel Breakout: Fibre Channel breakout ports can be configured on unified ports 1/1 and 1/2, resulting in 8 logical ports. 

  * Port Configurations: Physical Ports 1-8 can be configured as Uplink Ports, FCoE Uplink Ports, FCoE Storage Ports, and Appliance Ports. 

  * Port Conversions: All port conversions support up to 8 standard ports or 8 breakout ports. 

  * Server Ports: Configuration as Server Ports is not supported.

  * Fibre Channel Direct Ports: Direct ports for Fibre Channel are not supported. 

  * Traffic Monitoring: Breakout ports can be utilized as destinations for traffic monitoring. 


### Port Breakout Functionality on Cisco UCS 6536 Fabric Interconnects

The Cisco UCS 6536 36-Port Fabric Interconnect is a One-Rack-Unit (1RU) 1/10/25/40/100 Gigabit Ethernet, FCoE, and Fibre Channel switch offering up to 7.42 Tbps throughput and up to 36 ports. 

Cisco UCS 6536 Fabric Interconnect supports splitting a single 40 Gigabit(G)/100G Quad Small Form-factor Pluggable (QSFP) port into four 10G/25G ports using a supported breakout cable. The switch has 32 40/100-Gbps Ethernet ports and four unified ports that can support 40/100-Gbps Ethernet ports or 16 Fiber Channel (FC) ports after breakout at 8/16/32-Gbps FC speeds. The 16 FC ports after breakout can operate as an FC Uplink or FC storage port. The switch also supports two ports (Port 9 and Port 10) at 1-Gbps speed using QSA, and all 36 ports can breakout for 10 or 25 Gbps Ethernet connectivity. All Ethernet ports can support FCoE. 

Port breakout is supported for Ethernet ports (1-32) and Unified ports (33-36). These 40/100G ports are numbered in a 2-tuple naming convention. The process of changing the configuration from 40G to 10G, or from 100G to 25G is called breakout, and the process of changing the configuration from [4X]10G to 40G or from [4X]25G to 100G is called unconfigure. 

When you break out a 40G port into 10G ports or a 100G port into 25G ports, the resulting ports are numbered using a 3-tuple naming convention. For example, the breakout ports of the second 40-Gigabit Ethernet port are numbered as 1/31/1, 1/31/2, 1/31/3, and 1/31/4. 

FC breakout is supported on ports 36 through 33 when each port is configured with a four-port breakout cable. For example: Four FC breakout ports on the physical port 33 are numbered as 1/33/1, 1/33/2, 1/33/3, and 1/33/4. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Fibre Channel support is only available through the configuration of the Unified Ports (36-33) as Fibre Channel breakout port.

* * *  
  
---|---  
  
The following image shows the rear view of the Cisco UCS 6536 fabric interconnect:

Figure 1. Cisco UCS 6536 Fabric Interconnect Rear View  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540805.jpg)

The following image shows the rear view of the Cisco UCS 6536 fabric interconnect that include Ports and LEDs:

Figure 2. Cisco UCS 6536 Fabric Interconnect Rear View  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540989.jpg) 1  |  Ports 1-32. Uplink ports are Ethernet port that can operate with the port speed of 10 Gbps/25 Gbps/40 Gbps/100 Gbps. When using a breakout cable, each of these ports can operate as: 4 x 10 Gbps/4x 25 Gbps/1 x 40 Gbps/1 x 100 Gbps Ethernet or FCoE ports.  |  2  |  Ports 33-36. Unified Ports can operate with port speed of 10 Gbps/25 Gbps/ 40 Gbps/100 Gbps Ethernet. or  8 Gbps/16 Gbps/32 Gbps Fibre Channel (FC). When using a breakout cable, each of these ports can operate as 4 x 10 Gbps/4 x 25 Gbps Ethernet or 4x8Gbps/4x16Gbps/4x32Gbps FC ports.   
---|---|---|---  
3  |  Ports 1-36. Uplink ports and Unified ports that can be configured as Ethernet Breakout Port and can operate with the port speed of 10 Gbps/25 Gbps/40 Gbps/100 Gbps.  When using a breakout cable, each of these ports can operate as: 4 x 10 Gbps/4x 25 Gbps/1 x 40 Gbps/1 x 100 Gbps Ethernet or FCoE ports.  |  4 | System environment (fan fault) LED  
5 |  System status (STS) LED |  6 |  Beacon (BCN) LED  
  
#### Breakout Port Guidelines

The following are the guidelines for breakout functionality for Cisco UCS 6536 Fabric Interconnects: 

  * The configurable breakout ports are from port 1-36.

  * You can configure the speed for each breakout port. Each breakout port can be configured at the speed of 4 x 8 Gbps/ 4 x 16 Gbps/ 4 x 32 Gbps for Fibre Channel. 

  * For Fibre Channel breakout, each breakout port can be configured at the speed of 4 x 8 Gbps/ 4 x 16 Gbps/ 4 x 32 Gbps.

  * For Ethernet breakout, each breakout port can be configured at the speed of 4 x 10 Gbps/4 x 25 Gbps.

  * Fibre Channel breakout ports are supported, and Fiber Channel direct ports are not supported.

  * FC breakout port can be configured from 1/36 through 1/33. FC breakout ports (36-33) cannot be configured unless the previous ports are FC breakout ports. Configuration of a single (individual) FC breakout port is also supported. 

  * If the breakout mode for any of the supported Fabric Interconnect ports (1-36) is an Ethernet breakout, the Fabric Interconnect does not lead to a reboot. 

  * If the breakout mode for any of the supported Fabric Interconnect ports (36-33) is a Fibre Channel uplink breakout, the Fabric Interconnect leads to a reboot. 

  * Breakout ports are supported as destinations for traffic monitoring.

  * Ports 1-36 can be configured as Server Port, FCoE Uplink Port, Appliance Port, and Monitor Port.

  * Port 36-33 can be configured also as FC Uplink Port or FC Storage Port when configured as unified port.


### Port Breakout Functionality on Cisco UCS 64108 Fabric Interconnects

#### About Breakout Ports

Cisco UCS 64108 fabric interconnects support splitting a single 40/100G QSFP port into four 10/25G ports using a supported breakout cable. On the UCS 64108 fabric interconnect, by default, there are 12 ports in the 40/100G mode. These are ports 97 to 108. These 40/100G ports are numbered in a 2-tuple naming convention. For example, the second 40G port is numbered as 1/99. The process of changing the configuration from 40G to 10 G, or from 100G to 25G is called breakout, and the process of changing the configuration from [4X]10G to 40G or from [4X]25G to 100G is called unconfigure. These ports can be used as uplink port, appliance port, server port (using FEX), and FCoE storage port. 

When you break out a 40G port into 10G ports or a 100G port into 25G ports, the resulting ports are numbered using a 3-tuple naming convention. For example, the breakout ports of the second 40-Gigabit Ethernet port are numbered as 1/99/1, 1/99/2, 1/99/3, 1/99/4. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCS Manager does not support connection of FEX, chassis, blade, IOM, or adapters (other than VIC adapters) to the uplink ports of Fabric Interconnect. 

* * *  
  
---|---  
  
Starting with Cisco UCS Manager Release 4.2(3b), configuring the Ethernet breakout ports will not lead to Fabric Interconnect reboot. 

The following image shows the rear view of the Cisco UCS 64108 fabric interconnect, and includes the ports that support breakout port functionality: 

Figure 3. Cisco UCS 64108 Fabric Interconnect Rear View ![](/c/dam/en/us/td/i/300001-400000/300001-310000/307001-308000/307644.jpg) 1  |  Ports 1-16. Unified Ports can operate as 10/25 Gbps Ethernet or 8/16/32 Gbps Fibre Channel. FC ports are converted in groups of four.  Unified ports:

  * 10/25 Gbps Ethernet or FCoE
  * 8/16/32 Gbps Fibre Channel

|  2  |  Ports 1-96. Each port can operate as either a 10 Gbps or 25 Gbps Ethernet or FCoE SFP28 port.   
---|---|---|---  
3  |  Uplink Ports 97-108. Each port can operate as either a 40 Gbps or 100 Gbps Ethernet or FCoE port. When using a breakout cable, each of these ports can operate as 4 x 10 Gbps or 4 x 25 Gbps Ethernet or FCoE ports.  Ports 97 - 108 can be used to connect to Ethernet or FCoE uplink ports, and not to UCS server ports. |  4 |  Ports 89-96

  * 10/25 Gbps Ethernet or FCoE
  * 1 Gbps Ethernet

  
5 |  System environment (fan fault) LED |  6 |  System status LED  
7 |  Beacon LED |  |   
  
#### Breakout Port Guidelines

The following are the guidelines for breakout functionality for Cisco UCS 64108 fabric interconnects: 

  * The breakout configurable ports are ports 97-108.

  * You cannot configure the speed for each breakout port. Each breakout port is in auto mode.

  * Breakout ports are not supported as destinations for traffic monitoring.

  * Ports 97-108 at 40/100G can be configured as uplink, FCoE, or appliance port. Ports 97-108 after breakout to 10/25G can be configured as uplink, appliance, FCoE, or for direct-connect rack server connectivity. 


### Port Breakout Functionality on Cisco UCS 6454 Fabric Interconnects

#### About Breakout Ports

Cisco UCS 6454 fabric interconnects support splitting a single 40/100G QSFP port into four 10/25G ports using a supported breakout cable. These ports can be used only as uplink ports connecting to a 10/25G switch. On the UCS 6454 fabric interconnect, by default, there are 6 ports in the 40/100G mode. These are ports 49 to 54. These 40/100G ports are numbered in a 2-tuple naming convention. For example, the second 40G port is numbered as 1/50. The process of changing the configuration from 40G to 10 G, or from 100G to 25G is called breakout, and the process of changing the configuration from [4X]10G to 40G or from [4X]25G to 100G is called unconfigure. 

When you break out a 40G port into 10G ports or a 100G port into 25G ports, the resulting ports are numbered using a 3-tuple naming convention. For example, the breakout ports of the second 40-Gigabit Ethernet port are numbered as 1/50/1, 1/50/2, 1/50/3, 1/50/4. 

Starting with Cisco UCS Manager Release 4.2(3b), Ethernet breakout ports configuration will not lead to Fabric Interconnect reboot. 

Starting with Cisco UCS Manager Release 4.1(3a), you can connect Cisco UCS Rack servers with VIC 1455 and 1457 adapters, to the uplink ports 49 to 54 (40/100 Gbps Ethernet or FCoE) in Cisco UCS 6454 Fabric Interconnects. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCS Manager does not support connection of FEX, chassis, blade, IOM, or adapters (other than VIC 1455 and 1457 adapters) to the uplink ports of Fabric Interconnect. 

* * *  
  
---|---  
  
The following image shows the rear view of the Cisco UCS 6454 fabric interconnect, and includes the ports that support breakout port functionality: 

Figure 4. Cisco UCS 6454 Fabric Interconnect Rear View ![](/c/dam/en/us/td/i/300001-400000/300001-310000/306001-307000/306755.jpg) 1  |  Ports 1-16 (Unified Ports 10/25 Gbps Ethernet or FCoE or 8/16/32 Gbps Fibre Channel) |  2  |  Ports 17-44 (10/25 Gbps Ethernet or FCoE)  
---|---|---|---  
3  |  Ports 45-48 (1/10/25 Gbps Ethernet or FCoE)  |  4 |  Uplink Ports 49-54 (40/100 Gbps Ethernet or FCoE)   
  
#### Breakout Port Guidelines

The following are the guidelines for breakout functionality for Cisco UCS 6454 fabric interconnects: 

  * The breakout configurable ports are ports 49-54.

  * You cannot configure the speed for each breakout port. Each breakout port is in auto mode.

  * In Cisco UCS Manager Release 4.0(2), breakout ports are not supported as destinations for traffic monitoring.

  * Ports 49-54 at 40/100G can be configured as uplink, FCoE, or appliance port. Ports 49-54 after breakout to 10/25G can be configured as uplink, appliance, FCoE, or for direct-connect rack server connectivity. 


### Port Breakout Functionality on Cisco UCS 6300 Series Fabric Interconnects 

#### About Breakout Ports 

Cisco UCS fabric interconnect 6300 series supports splitting a single QSFP port into four 10G ports using a supported breakout cable. By default, there are 32 ports in the 40G mode. These 40G ports are numbered in a 2-tuple naming convention. For example, the second 40G port is numbered as 1/2. The process of changing the configuration from 40G to 10G is called breakout and the process of changing the configuration from [4X]10G to 40G is called unconfigure. 

When you break out a 40G port into 10G ports, the resulting ports are numbered using a 3-tuple naming convention. For example, the breakout ports of the second 40-Gigabit Ethernet port are numbered as 1/2/1, 1/2/2, 1/2/3, 1/2/4. 

The following image shows the front view for the Cisco UCS 6332 series fabric interconnects, and includes the ports that may support breakout port functionality: 

Figure 5. Cisco UCS 6332 Series Fabric Interconnects Front View  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/305001-306000/305235.jpg) 1  |  L1 and L2 high availability ports   
---|---  
2  |  28 X 40G QSFP ports ( 98 X 10G SFP ports)  |  **Note** | 

  * QSA module is required on ports 13–14 
  * A QSFP to 4XSFP breakout cable is required for 10G support. 

  
---|---  
3  |  6 X 40G QSFP ports   
  
The following image shows the front view for the Cisco UCS 6332-16UP series fabric interconnects, and includes the ports that may support breakout port functionality: 

Figure 6. Cisco UCS 6332-16UP Series Fabric Interconnects Front View  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/305001-306000/305236.jpg) 1  |  L1 and L2 high availability ports   
---|---  
2  |  16 X 1/10G SFP (16 X 4/8/16G FC ports)   
3  |  18 X 40G QSFP(72 X 10G SFP+)  |  **Note** | 

  * A QSFP to 4XSFP breakout cable is required for 10G support. 

  
---|---  
4  |  6 X 40G QSFP ports   
  
The following image shows the rear view of the Cisco UCS 6300 series fabric interconnects. 

Figure 7. Cisco UCS 6300 Series Fabric Interconnects Rear View  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/305001-306000/305237.jpg) 1  |  Power supply   
---|---  
2  |  Four fans   
3  |  Power supply   
4  |  Serial ports   
  
#### Breakout Port Constraints 

The following table summarizes the constraints for breakout functionality for Cisco UCS 6300 series fabric interconnects: 

Cisco UCS 6300 Series Fabric Interconnect Series  |  Breakout Configurable Ports  |  Ports without breakout functionality support   
---|---|---  
Cisco UCS 6332  |  1–12, 15–26  |  13–14, 27–32  |  **Note** | 

  * Auto-negotiate behavior is not supported on ports 27–32. 

  
---|---  
Cisco UCS 6332-16UP  |  17–34  |  1–16, 35–40  |  **Note** | 

  * Auto-negotiate behavior is not supported on ports 35–40 

  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

Up to four breakout ports are allowed if QoS jumbo frames are used. 

* * *  
  
---|---  
  
### Configuring Multiple Breakout Ports 

On a UCS 6300 Fabric Interconnect, you can specify a 40 Gigabit Ethernet port and create four 10 Gigabit Ethernet unconfigured breakout ports. On a UCS 6454 Fabric Interconnect, you can specify a 40 or 100 Gigabit Ethernet port and create four 10 or 25 Gigabit Ethernet unconfigured breakout ports. 

On a Cisco UCS Fabric Interconnects 9108 100G and Cisco UCS 6536 Fabric Interconnect, you can specify a 40 or 100 Gigabit Ethernet port and create four 10 or 25 Gigabit Ethernet unconfigured breakout ports. Also, configuring breakout ports on a port do no require Fabric Interconnect reebot.

#### Before you begin

Before configuring a breakout port, view the port status using the show port command. 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A # scope cabling  |  Enters the cabling mode.   
**Step 2** |  UCS-A /cabling # scope fabric {a | b}  |  Enters cabling fabric mode for the specified fabric.   
**Step 3** |  UCS-A /cabling/fabric # create breakout slot-id port-id |  Creates the breakout port on the selected slot and port.   
**Step 4** |  UCS-A /cabling/fabric/breakout* # set breakouttype {10g-4x | 25g-4x}  |  Specifies the type of breakout port on UCS 6454 and UCS 6536 Fabric Interconnects.  
**Step 5** |  UCS-A /cabling/fabric/breakout* # up |  Returns you to fabric mode.  Repeat steps 3 and 5 for each breakout port on UCS 6300 Fabric Interconnect Repeat steps 3, 4, and 5 for each breakout port on Cisco UCS Fabric Interconnects 9108 100G, Cisco UCS 6500 Series, and Cisco UCS 6400 Series Fabric Interconnects.   
**Step 6** |  UCS-A /cabling/fabric/breakout* # commit-buffer |  Commits the transaction to the server.   
  
#### Example

The following example creates breakout ports 1/1 through 1/4 on a UCS 6300 Fabric Interconnect and commits the transaction: 
    
    
    UCS-A# **scope cabling** 
    UCS-A /cabling # **scope fabric a**
    UCS-A /cabling/fabric # **create breakout 1 1**
    Warning: Port breakout create action reboots FI and any existing configurations on 40G port will be erased.!
    UCS-A /cabling/fabric/breakout* # **up**
    UCS-A /cabling/fabric* # **create breakout 1 2**
    Warning: Port breakout create action reboots FI and any existing configurations on 40G port will be erased.!
    UCS-A /cabling/fabric/breakout* # **up**
    UCS-A /cabling/fabric* # **create breakout 1 3**
    Warning: Port breakout create action reboots FI and any existing configurations on 40G port will be erased.!
    UCSM--A /cabling/fabric/breakout* # **up**
    UCSM-shiva-a-A /cabling/fabric* # **create breakout 1 4**
    Warning: Port breakout create action reboots FI and any existing configurations on 40G port will be erased.!
    UCSM--A /cabling/fabric/breakout* # **commit-buffer**
    
    
    

The following example creates breakout ports 1/49 through 1/52 on a UCS 6454 Fabric Interconnect, sets the breakout type, and commits the transaction: 
    
    
    UCS-A# **scope cabling** 
    UCS-A /cabling # **scope fabric a**
    UCS-A /cabling/fabric # **create breakout 1 49**
    UCS-A /cabling/fabric/breakout* # **set breakouttype 10g-4x**
    UCS-A /cabling/fabric/breakout* # **up**
    UCS-A /cabling/fabric* # **create breakout 1 50**
    UCS-A /cabling/fabric/breakout* # **set breakouttype 10g-4x**
    UCS-A /cabling/fabric/breakout* # **up**
    UCS-A /cabling/fabric* # **create breakout 1 51**
    UCS-A /cabling/fabric/breakout* # **set breakouttype 10g-4x**
    UCSM--A /cabling/fabric/breakout* # **up**
    UCSM-shiva-a-A /cabling/fabric* # **create breakout 1 52**
    UCS-A /cabling/fabric/breakout* # **set breakouttype 10g-4x**
    UCS-A /cabling/fabric/breakout* # **commit-buffer**
    

The following example creates breakout ports 1/50 through 1/53 on a UCS 64108 Fabric Interconnect, sets the breakout type, and commits the transaction: 
    
    
    UCS-A# **scope cabling** 
    UCS-A /cabling # **scope fabric a**
    UCS-A /cabling/fabric # **create breakout 1 50**
    UCS-A /cabling/fabric/breakout* # **set breakouttype 10g-4x**
    UCS-A /cabling/fabric/breakout* # **up**
    UCS-A /cabling/fabric* # **create breakout 1 51**
    UCS-A /cabling/fabric/breakout* # **set breakouttype 10g-4x**
    UCS-A /cabling/fabric/breakout* # **up**
    UCS-A /cabling/fabric* # **create breakout 1 52**
    UCS-A /cabling/fabric/breakout* # **set breakouttype 10g-4x**
    UCSM--A /cabling/fabric/breakout* # **up**
    UCSM-shiva-a-A /cabling/fabric* # **create breakout 1 53**
    UCS-A /cabling/fabric/breakout* # **set breakouttype 10g-4x**
    UCS-A /cabling/fabric/breakout* # **commit-buffer**
    

The following example creates breakout ports 1/17 through 1/20 on a UCS 6536 Fabric Interconnect, sets the breakout type, and commits the transaction: 
    
    
    UCS-A# **scope cabling** 
    UCS-A /cabling # **scope fabric a**
    UCS-A /cabling/fabric # **create breakout 1 17**
    UCS-A /cabling/fabric/breakout* # **set breakouttype 25g-4x**
    UCS-A /cabling/fabric/breakout* # **up**
    UCS-A /cabling/fabric* # **create breakout 1 18**
    UCS-A /cabling/fabric/breakout* # **set breakouttype 25g-4x**
    UCS-A /cabling/fabric/breakout* # **up**
    UCS-A /cabling/fabric* # **create breakout 1 19**
    UCS-A /cabling/fabric/breakout* # **set breakouttype 25g-4x**
    UCSM--A /cabling/fabric/breakout* # **up**
    UCSM-shiva-a-A /cabling/fabric* # **create breakout 1 20**
    UCS-A /cabling/fabric/breakout* # **set breakouttype 25g-4x**
    UCS-A /cabling/fabric/breakout* # **commit-buffer**
    

The following example creates breakout ports 1/1 through 1/4 Cisco UCS Fabric Interconnects 9108 100G and commits the transaction: 
    
    
    UCS-A# **scope cabling** 
    UCS-A /cabling # **scope fabric a**
    UCS-A /cabling/fabric # create breakout 1 1
    UCS-A /cabling/fabric/breakout* # set breakouttype 25g-4x
    UCS-A /cabling/fabric/breakout* # up
    UCS-A /cabling/fabric* # create breakout 1 2
    UCS-A /cabling/fabric/breakout* # set breakouttype 25g-4x
    UCS-A /cabling/fabric/breakout* # up
    UCS-A /cabling/fabric* # create breakout 1 3
    UCS-A /cabling/fabric/breakout* # set breakouttype 25g-4x
    UCSM--A /cabling/fabric/breakout* # up
    UCSM-shiva-a-A /cabling/fabric* # create breakout 1 4
    UCS-A /cabling/fabric/breakout* # set breakouttype 25g-4x
    UCS-A /cabling/fabric/breakout* # commit-buffer
    
    
    
    

#### What to do next

Verify that you created breakout ports on the fabric interconnect and on the NXOS switch. On the fabric interconnect use the show breakout command in cabling fabric mode for the specified fabric. In NXOS, use the show interface brief  command. 

### Configuring a Breakout Ethernet Uplink Port 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope eth-uplink |  Enters Ethernet uplink mode.   
**Step 2** |  UCS-A /eth-uplink #  scope fabric{a | b}  |  Enters Ethernet uplink fabric mode for the specified fabric.   
**Step 3** |  UCS-A /eth-uplink/fabric #  create aggr-interface slot-numaggregate port-num |  Creates the interface for the specified aggregate (main) Ethernet uplink port.   
**Step 4** |  UCS-A /eth-uplink/fabric/aggr-interface* #  create br-interface breakout-port-num |  Creates an interface for the specified breakout Ethernet uplink port.   
**Step 5** |  UCS-A /eth-uplink/fabric/aggr-interface/br-interface #  commit-buffer  |  Commits the transaction to the server.   
  
#### Example

The following example shows how to create an interface for breakout Ethernet uplink port 1 of the aggregate port 21 on slot 1 of fabric A: 
    
    
    UCS-A# **scope eth-uplink**
    UCS-A /eth-uplink # **scope fabric a**
    UCS-A /eth-uplink/fabric # **enter aggr-interface 1 21**
    UCS-A /eth-uplink/fabric/aggr-interface # **create br-interface 1**
    UCS-A /eth-uplink/fabric/aggr-interface/br-interface*# **commit-buffer**
    
    

The following example shows how to create interfaces for breakout Ethernet uplink ports 1-4 of the aggregate port 49 on slot 1 of fabric A on a UCS 6454 fabric interconnect, and commit the transaction: 
    
    
    UCS-A# **scope eth-uplink**
    UCS-A /eth-uplink # **scope fabric a**
    UCS-A /eth-uplink/fabric # **create aggr-interface 1 49**
    UCS-A /eth-uplink/fabric/aggr-interface* # **create br-interface 1**
    UCS-A /eth-uplink/fabric/aggr-interface/br-interface* # **up**
    UCS-A /eth-uplink/fabric/aggr-interface* # **create br-interface 2**
    UCS-A /eth-uplink/fabric/aggr-interface/br-interface* # **up**
    UCS-A /eth-uplink/fabric/aggr-interface* # **create br-interface 3**
    UCS-A /eth-uplink/fabric/aggr-interface/br-interface* # **up**
    UCS-A /eth-uplink/fabric/aggr-interface* # **create br-interface 4**
    UCS-A /eth-uplink/fabric/aggr-interface/br-interface* # **up**
    UCS-A /eth-uplink/fabric/aggr-interface* # **commit-buffer**
    UCS-A /eth-uplink/fabric/aggr-interface # 
    

The following example shows the breakout configuration for ports 1/49/1 to 1/49/4 of fabric A on a UCS 6454 fabric interconnect: 
    
    
    UCS-A# **scope fabric-interconnect a** 
    UCS-A /fabric-interconnect # **show port**
    Ether Port: 
    Slot  Aggr       Port  Port Oper State  Mac                  Role    Xcvr 
    ----- ---------- ----- ---------------- -------------------- ------- ---- 
    1     49         1     Sfp Not Present  8C:60:4F:BC:C4:D4    Unknown N/A 
    1     49         2     Sfp Not Present  8C:60:4F:BC:C4:D5    Unknown N/A 
    1     49         3     Sfp Not Present  8C:60:4F:BC:C4:D6    Unknown N/A 
    1     49         4     Sfp Not Present  8C:60:4F:BC:C4:D7    Unknown N/A 
    

### Configuring a Breakout Ethernet Uplink Port Channel Member 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope eth-uplink |  Enters Ethernet uplink mode.   
**Step 2** |  UCS-A# /eth-uplink # scope fabric{a | b}  |  Enters Ethernet uplink mode for the specified fabric.   
**Step 3** |  UCS-A# /eth-uplink/fabric # scope fcoe-port-channel fcoe-port-channel |  Enters port channel for the specified FCoE uplink port.   
**Step 4** |  UCS-A /eth-uplink/fabric/port-channe/fcoe-port-channel # enter aggr-interface slot-id port-id |  Enters the interface for the specified aggregate(main) FCoE uplink port.   
**Step 5** |  UCS-A /eth-uplink/fabric/port-channel/member-aggr-port # create br-member-portbreakout-port-num |  Creates the FCoE uplink port channel member.   
**Step 6** |  UCS-A /eth-uplink/fabric/port-channel/member-aggr-port/br-member-port # commit-buffer 

#### Example:

The following example creates an Ethernet uplink port channel member for an Ethernet port on port 2, and commits the transaction: 
    
    
    UCS-A# **scope eth-storage** 
    UCS-A /eth-uplink # **scope fabric a**
    UCS-A /eth-uplink/fabric # **scope fcoe-port-channel 51**
    UCS-A /eth-uplink/fabric/port-channel/member-aggr-port # **create br-member-port 2**
    UCS-A /eth-uplink/fabric/port-channel/member-aggr-port/br-member-port* # **commit-buffer**
    

|  Commits the transaction to the server.   
  
### Configuring Ethernet Uplink Breakout Port as a Pin Group Target 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope eth-uplink |  Enters Ethernet uplink mode.   
**Step 2** |  UCS-A# /eth-uplink/pin-group #  enter pin-group pin-group-name |  Enters the pin group with the specified name.   
**Step 3** |  UCS-A# /et h-uplink/pin-group # set target{a|b} breakout-portslot-numaggregate-port-numbreakout-port-num |  Sets the selected target as the breakout port.   
**Step 4** |  UCS-A # /eth-uplink/pin-group #  commit-buffer

#### Example:

The following example sets the pin group target to breakout port 2 of the aggregate port 1 on slot 1, on fabric A , and commits the transaction: 
    
    
    UCS-A# scope **eth-uplink**
    UCS-A /eth-uplink # **enter pin-group test**
    UCS-A /eth-uplink/pin-group # **set target a breakout-port 1 1 2**
    UCS-A /eth-uplink/pin-group* # **commit-buffer**
     
    

|  Commits the transaction to the server.   
  
### Configuring Breakout Appliance Ports

You can follow the below steps to configure appliance breakout ports for both Cisco UCS Fabric Interconnects 9108 100G, Cisco UCS 6500 Series Fabric Interconnect, , and Cisco UCS 6400 Series Fabric Interconnect: 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope eth-storage |  Enters Ethernet storage mode.   
**Step 2** |  UCS-A# /eth-storage # scope fabric{a | b}  |  Enters Ethernet storage mode for the specified fabric.   
**Step 3** |  UCS-A# /eth-storage/fabric # enter aggr-interface slot-numaggregate-port-num |  Enters the interface for the specified aggregate(main) appliance port.   
**Step 4** |  UCS-A# /eth-storage/fabric/port-channel/member-aggr-port #  create br -interfacebreakout-port-num |  Creates an interface for the specified breakout appliance port.   
**Step 5** |  UCS-A# /eth-storage/fabric/port-channel/member-aggr-port/br-member-port #  commit-buffer

#### Example:

The following example creates an interface for an appliance port 1 of the aggregate port 20 on slot 1 of fabric B, and commits the transaction: 
    
    
    UCS-A# **scope eth-storage** 
    UCS-A /eth-storage # **scope fabric a** 
    UCS-A /eth-storage/fabric # **enter aggr-interface 1 20**
    UCS-A /eth-storage/fabric/aggr-interface # **create br-interface 1**
    UCS-A /eth-storage/fabric/aggr-interface/br-interface* # **commit-buffer** 
    
    
    
    
    

#### Example:

|  **Note** |  If the port is only connected to 100G SFP which is broken out in 25x4 breakout port then when creating an appliance port, the default speed for a breakout port would be Auto.   
---|---  
Commits the transaction to the server.   
  
### Configuring a Breakout Appliance Port Channel Member 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope eth-storage |  Enters Ethernet storage mode.   
**Step 2** |  UCS-A# /eth-storage # scope fabric{a | b}  |  Enters Ethernet storage mode for the specified fabric.   
**Step 3** |  UCS-A# /eth-storage # scope port-channelport-channel-num |  Enters Ethernet storage mode for the specified port-channel.   
**Step 4** |  UCS-A# /eth-storage/fabric # enter aggr-interface slot-numaggregate-port-num |  Enters the interface for the specified aggregate(main) appliance port.   
**Step 5** |  UCS-A /eth-storage/fabric/port-channel # enter member-aggr-port  slot-id port-id |  Enters the appliance port channel member port.   
**Step 6** |  UCS-A /eth-storage/fabric/port-channel/member-aggr-port # create br-member-portbreakout-port-num |  Creates the appliance port channel member.   
**Step 7** |  UCS-A /eth-storage/fabric/port-channel/member-aggr-port/br-member-port # commit-buffer

#### Example:

The following example creates an appliance port channel member for an appliance port 2, and commits the transaction: 
    
    
    UCS-A# **scope eth-storage** 
    UCS-A /eth-storage # **scope fabric a**
    UCS-A /eth-storage/fabric # **scope port-channel 21**
    UCS-A /eth-storage/fabric/port-channel # **enter member-aggr-port 1 2**
    UCS-A /eth-storage/fabric/port-channel/member-aggr-port # **create br-member-port 2**
    UCS-A /eth-storage/fabric/port-channel/member-aggr-port/br-member-port* # **commit-buffer**
    

|  Commits the transaction to the server.   
  
### Configuring Breakout FCoE Storage Ports 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope fc-storage |  Enters Fibre Channel storage mode.   
**Step 2** |  UCS-A# /fc-storage scope fabric{a | b |  Enters Fibre Channel storage mode for the specified fabric.   
**Step 3** |  UCS-A# /fc-storage/fabric enter aggr-interface slot-numaggregate port-num |  Enter the interface for the specified aggregate(main) Fibre Channel storage port.   
**Step 4** |  UCS-A# /fc-storage/fabric/aggr-interface #  create br-interface br-fcoe breakout-port-num |  Creates an interface for the specified breakout Fibre Channel storage port.   
**Step 5** |  UCS-A# /fc-storage/fabric/aggr-interface/br-interface/br-fcoe #  commit-buffer 

#### Example:

The following example creates an interface for a breakout Fibre Channel storage port 1 of the aggregate port 21 on slot 1 of fabric a, and commits the transaction: 
    
    
    UCS-A# **scope fc-storage**
    UCS-A /fc-storage # **scope fabric a**
    UCS-A /fc-storage/fabric # **enter aggr-interface 1 21**
    UCS-A /fc-storage/fabric/aggr-interface # **create br-interface 1**
    UCS-A /eth-uplink/fabric/aggr-interface/br-interface/br-fcoe **# commit-buffer**
    
    

|  Commits the transaction to the server.   
  
### Configuring a Breakout FCoE Uplink Port 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope fc-uplink |  Enters FC Uplink mode.   
**Step 2** |  UCS-A# /fc-uplink scope fabric{a | b |  Enters FC - Uplink mode for the specific fabric.   
**Step 3** |  UCS-A# /fc-uplink/fabric enter aggr-interface slot-numaggregate port-num |  Enters interface for the specified aggregate(main) FCoE uplink port.   
**Step 4** |  UCS-A# /fc-uplink/fabric/aggr-interface #  create br-fcoeinterface breakout-port-num |  Creates an interface for the specified breakout FCoE uplink port.   
**Step 5** |  UCS-A# /fc-uplink/fabric/aggr-interface/ br-fcoeinterface #  commit-buffer 

#### Example:

The following example shows how to create an interface for breakout FCoE uplink port 1 of the aggregate port 20 on slot 1 of fabric A: 
    
    
    UCS-A# **scope eth-uplink**
    UCS-A /fc-uplink # **scope fabric a**
    UCS-A /fc-uplink/fabric # **enter aggr-interface 1 20**
    UCS-A /fc-uplink/fabric/aggr-interface # **create br-fcoeinterface 1**
    UCS-A /fc-uplink/fabric/aggr-interface/br-fcoeinterface**# commit-buffer**
    
    

|  Commits the transaction to the server.   
  
### Configuring an FCoE Port Channel Member 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope fc-uplink |  Enters Ethernet storage mode.   
**Step 2** |  UCS-A# /fc-uplink # scope fabric{a | b}  |   
**Step 3** |  UCS-A# /fc-uplink/fabric # scope fcoe-port-channel fcoe-port-num |   
**Step 4** |  UCS-A /fc-uplink/fabric/port-channel # enter aggr-interface slot-num port-numaggregate-port-num |  Enters the FCoE port channel member port.   
**Step 5** |  UCS-A /fc-uplink/fabric/port-channel/member-aggr-port # create br-member-portbreakout-port-num |  Creates the FCoE port channel member for the specified breakout port.   
**Step 6** |  UCS-A /fc-uplink/fabric/port-channel/member-aggr-port/br-member-port # commit-buffer

#### Example:

The following example creates a breakout FCoE port channel member port 4 on aggregate port 21, and commits the transaction: 
    
    
    UCS-A# **scope eth-storage** 
    UCS-A /fc-uplink # **scope fabric a**
    UCS-A /fc-uplink/fabric # **scope port-channel 51**
    UCS-A /fc-uplink/fabric/port-channel # **enter member-aggr-port 1 21**
    UCS-A /fc-uplink/fabric/port-channel/member-aggr-port # **create br-member-port 4**
    UCS-A /fc-uplink/fabric/port-channel/member-aggr-port/br-member-port* # **commit-buffer**
    

|  Commits the transaction to the server.   
  
### Configuring a Breakout VLAN Member Port 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  USA-A# scope eth-uplink |  Enters Ethernet uplink mode for the specified fabric.   
**Step 2** |  USA-A /eth-uplink # scope vlan  id |  Enters VLAN mode.   
**Step 3** |  USA-A /eth-uplink/vlan # enter member-aggr-port {a|b} slot-id port id |  Enters an interface for the specified fabric, main aggregate port, and subport. breakout VLAN member port.   
**Step 4** |  USA-A /eth-uplink/vlan/member-aggr-port # create br-member-port breakout-port-name |  Creates an interface for the specified breakout VLAN member port.   
**Step 5** |  USA-A /eth-uplink/vlan/member-aggr-port/br-member-port # commit-buffer 

#### Example:

The following example creates an interface for a VLAN member on the aggregate port 4 on slot 1 of breakout Ethernet uplink port 1, and commits the transaction: 
    
    
    USA-A# **scope eth-uplink** 
    USA-A /eth-uplink # **scope vlan id**
    USA-A /eth-uplink/vlan # **enter member-aggr-port a 1 1**
    USA-A /eth-uplink/vlan/member-aggr-port* # **create br-member-port 4**
    USA-A /eth-uplink/vlan/member-aggr-port/br-member-port* # **commit-buffer**  
     

|  Commits the transaction to the server.   
  
#### What to do next

Verify that you created the breakout VLAN Member port using the show command. 

### Modifying a Breakout Port 

The following table describes how to modify the supported breakout ports. 

Breakout Port Type  |  Scope  |  CLI Location From Which To Modify  |  Modify Options   
---|---|---|---  
Ethernet Uplink  |  eth-uplink  |  UCS-A eth-uplink/fabric/aggr-interface/br-interface # create |  mon-src — Creates a monitor source session.   
UCS-A /eth-uplink/fabric/aggr-interface/br-interface # set |  eth-link-profile — Sets the Ethernet Link profile name.  flow-control-policy  — Sets the flow control policy that configures the receive and send flow control parameters for the LAN and Ethernet uplink ports.  speed — Sets the speed for an Ethernet uplink port.  user-label — Assigns an identifying label to the Ethernet Uplink port.   
UCS-A /eth-uplink/fabric/aggr-interface/br-interface #  |  disable — Disables the aggregate interface for the Ethernet Uplink breakout port.  enable — Enables the aggregate interface for the Ethernet Uplink breakout port.   
Ethernet Uplink port-channel member  |  fc-storage  |  UCS-A /eth-uplink/fabric/port-channel/aggr-interface/br-member-port # set |  eth-link-profile — Sets the Ethernet Link profile name.   
UCS-A /eth-uplink/fabric/port-channel/aggr-interface/br-member-port #  |  disable — Disables the aggregate interface for the breakout Ethernet Uplink port-channel member.  enable — Enables the aggregate interface for the breakout Ethernet Uplink port-channel member.   
FCoE Uplink  |  fc-uplink  |  UCS-A /fc-uplink/fabric/aggr-interface/br-fcoeinterface # create |  mon-src — Creates a monitor source session.   
UCS-A /fc-uplink/fabric/aggr-interface/br-fcoeinterface # set |  eth-link-profile — Sets the Ethernet Link profile name.  user-label  — Assigns an identifying label to the FCoE uplink breakout port.   
UCS-A /fc-uplink/fabric/aggr-interface/br-fcoeinterface #  |  disable —Disables the aggregate interface for the FCoE uplink breakout port.  enable — Enables the aggregate interface for the FCoE uplink breakout port.   
FCoE Uplink port-channel member  |  eth-uplink  |  UCS-A /fc-uplink/fabric/fcoe-port-channel/aggr-interface/br-member-port # set |  eth-link-profile — Sets the Ethernet Link profile name.   
A /fc-uplink/fabric/fcoe-port-channel/aggr-interface/br-member-port #  |  disable — Disables the aggregate interface for the breakout FCoE uplink port-channel member.  enable — Enables the aggregate interface for the breakout FCoE uplink port-channel member.   
FCoE Storage port  |  fc-storage  |  UCS-A fc-storage/fabric/aggr-interface/br-fcoe # create |  mon-src — Creates a monitor source session.   
UCS-A /fc-storage/fabric/aggr-interface/br-fcoe # set |  user-label — Assigns an identifying label to the server.   
UCS-A /fc-storage/fabric/aggr-interface/br-fcoe #  |  disable — Disables the aggregate interface for the breakout FCoE Storage port  enable — Enables the aggregate interface for the breakout FCoE Storage port.   
Appliance Port  |  eth-storage  |  UCS-A /eth-storage/fabric/aggr-interface/br-interface # set |  adminspeed — Sets the speed for a fabric interface.  flowctrlpolicy —Sets the flow control policy that configures the receive and send flow control parameters for the appliance ports.  nw-control-policy  — Creates a network control policy for the appliance port.  pingroupname — Sets the pin group name for the fabric interface.  portmode — Sets the appliance port mode.  prio — Sets the QoS (Quality of Service) priority level.  user-label — Assigns an identifying label to the appliance port.   
UCS-A /eth-storage/fabric/aggr-interface/br-interface # create |  eth-target — Creates the Ethernet target endpoint.  mon-src — Creates a monitor source session.   
UCS-A /eth-storage/fabric/aggr-interface/br-interface #  |  disable — Disables the aggregate interface for the appliance breakout port.  enable —Enables the aggregate interface for the appliance breakout port.   
Appliance port-channel member  |  eth-storage |  UCS-A /eth-storage/fabric/port-channel/member-aggr-port #  |  disable — Disables the aggregate interface for the breakout appliance port-channel member.  enable —Enables the aggregate interface for the breakout appliance port-channel member.   
VLAN Member  |  eth-uplink  |  A /eth-uplink/vlan/member-aggr-port/br-member-port # set |  isnative — Marks a member-port as a native VLAN.   
Pin Group - Pin Target  |  eth-uplink  |  N/A  |  N/A   
SPAN (Traffic Monitoring) Destination Port  |  eth-traffic-mon  |  A /eth-traffic-mon/fabric/eth-mon-session/dest-aggr-interface/br-dest-interface # set |  speed — Sets the speed for the SPAN (Traffic Monitoring) destination port.   
  
#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope eth-uplink .  |  Enters Ethernet uplink mode.   
**Step 2** |  UCS-A /eth-uplink # scope fabric  {a | b} .  |  Enters Ethernet uplink fabric mode for the specified fabric.   
**Step 3** |  UCS-A /eth-uplink/fabric # scope aggr-interface port-number port-id .  |  Enters the interface for the specified aggregate(main) Ethernet uplink port.   
**Step 4** |  UCS-A /eth-uplink/fabric/aggr-interface # scope br-interface port-id .  |  Enters the breakout Ethernet port for the specified port number.   
**Step 5** |  UCS-A /eth-uplink/fabric/aggr-interface/br-interface # create mon-src . 

#### Example:

The following example shows how to modify a Ethernet uplink port as a monitor source in breakout port 1 of the aggregate (main) interface in port 1 with an ID of 21. 
    
    
    UCS-A# **scope eth-uplink**
    UCS-A /eth-uplink # **scope fabric a**
    UCS-A /eth-uplink/fabric # **scope aggr-interface 1 21**
    UCS-A /eth-uplink/fabric/aggr-interface # **scope br-interface 1**
    UCS-A /eth-uplink/fabric/aggr-interface/br-interface # **create** 
    	UCS-A /eth-uplink/fabric/aggr-interface/br-interface # **create mon-src**
    

|  Modifies the interface as a monitoring source.   
  
#### Modifying the Breakout Ethernet Uplink Port Speed and User Label 
    
    
    pranspat-3gfi-A /eth-uplink/fabric/aggr-interface/br-interface # set      
    	eth-link-profile     Ethernet Link Profile name   
    	flow-control-policy  flow control policy   
    	speed                 Speed   
    	user-label           User Label 
    
    
    
    pranspat-3gfi-A /eth-uplink/fabric/aggr-interface/br-interface # 
    	disable      Disables services   
    	enable       Enables services
    

###  Un-configuring Breakout Ports 

If you have a breakout on port 2 in slot 1, you can un-configure the breakout port. 

#### Before you begin

You can use the  show port  command to list the ports for the Fabric Interconnect (FI), and select the port that you want to breakout. 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# / fabric-interconnect #  show port 

#### Example:

The following example lists the ports. 
    
    
    Slot  Aggr Port  Port  Oper State       Mac                  Role    Xcvr
    ----- ---------- ----- ---------------- -------------------- ------- ----
        1          0     1 Link Down        84:B8:02:CA:37:56    Network 1000base T
        1          2     1 Sfp Not Present  84:B8:02:CA:37:57    Unknown N/A
        1          2     2 Sfp Not Present  84:B8:02:CA:37:57    Unknown N/A
        1          2     3 Sfp Not Present  84:B8:02:CA:37:57    Unknown N/A
        1          2     4 Sfp Not Present  84:B8:02:CA:37:57    Unknown N/A
        1          0     3 Sfp Not Present  84:B8:02:CA:37:58    Unknown N/A
    
    

|  Displays the ports for the Fabric Interconnect.   
**Step 2** |  UCS-A#  scope cabling  |  Enters the cabling mode.   
**Step 3** |  UCS-A# /cabling # scope fabric {a | b }  |  Specifies fabric a or b.   
**Step 4** |  UCS-A #/ cabling # delete breakout  {1 | 2 |   
**Step 5** |  UCS-A /cabling/fabric/breakout* #  commit .  |  Commits the transaction to the system configuration.   
  
#### What to do next

You can use the  show port  to view the unconfigured breakouts ports. 

### Deleting Breakout Ports 

You can delete 10 Gig Ethernet breakout ports. Use the br-interface or br-member-port  scopes to select breakout sub-ports 1-4. You must provide the sub-port id for this scope. For example, scope br-interface sub_port_id . 

The example described in this topic describes how to delete a breakout Ethernet uplink port. The following table describes how to delete the supported Ethernet breakout ports. 

Breakout Port Type  |  Scope  |  CLI Location From Which To Delete   
---|---|---  
Ethernet Uplink  |  eth-uplink  |  UCS-A /eth-uplink/fabric/aggr-interface # delete br-interface number  
Ethernet Uplink port-channel member  |  eth-uplink  |  UCS-A /eth-uplink/fabric/port-channel/aggr-interface # delete br-member-port number  
FCoE Uplink  |  fc-uplink  |  UCS-A /fc-uplink/fabric/aggr-interface # delete br-fcoeinterface number  
FCoE Uplink port-channel member  |  eth-uplink  |  UCS-A /fc-uplink/fabric/fcoe-port-channel/aggr-interface # delete br-member-port number  
FCoE Storage port  |  fc-storage  |  UCS-A /fc-storage/fabric/aggr-interface # delete br-interface br-fcoe number  
Appliance Port  |  eth-storage  |  UCS--A /eth-storage/fabric/port-channel/member-aggr-port # delete br-member-port number  
Appliance port-channel member  |  eth-storage  |  UCS-A /eth-storage/fabric/aggr-interface # delete br-interface number  
VLAN Member  |  eth-uplink  |  UCS-A /eth-uplink/vlan/member-aggr-port # delete br-member-port number  
Pin Group - Pin Target  |  eth-uplink  |  UCS-A /eth-uplink/pin-group # delete target number  
SPAN (Traffic Monitoring) Destination Port  |  eth-traffic-mon  |  UCS-A /eth-traffic-mon/fabric/eth-mon-session/dest-aggr-interface # delete br-dest-interface   
  
#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope eth-uplink  |  Enters the Ethernet uplink mode.   
**Step 2** |  UCS-A# /eth-storage #  scope fabric{a | b}  |  Enters Ethernet storage mode for the specified fabric.   
**Step 3** |  UCS-A /eth-uplink/fabric # scope port-channel  number |  Enters Ethernet uplink fabric port channel mode for the specified port channel.   
**Step 4** |  UCS-A /eth-uplink/fabric/port-channel/aggr-interface # delete br-member-port  number |  Deletes the specified breakout port.   
**Step 5** |  UCS-A /eth-uplink/fabric/port-channel/aggr-interface # commit-buffer

#### Example:

This example deletes an Ethernet Uplink port-channel member in breakout port 1 of the aggregate (main) interface port 1 slot 1. 
    
    
    UCS-A# **scope eth-uplink** 
    UCS-A /eth-uplink # **scope fabric a**
    UCS-A /eth-uplink/fabric # **scope port-channel 1**
    UCS-A /eth-uplink/fabric/port-channel # **enter aggr-interface 1 1**
    UCS-A /eth-uplink/fabric/port-channel/aggr-interface # **delete br-member-port 1**
    UCS-A /eth-uplink/fabric/port-channel/aggr-interface* # **commit-buffer**

|  Commits the transaction to the server.   
  
#### What to do next

Verify that you deleted the specified breakout port using the show command. 

### Cisco UCS Mini Scalability Ports 

The Cisco UCS 6324 Fabric Interconnect contains a scalability port as well as four unified ports. The scalability port is a 40GB QSFP+ breakout port that, with proper cabling, can support four 1G or 10G SFP+ ports. The scalability ports can be used as a licensed server port for supported Cisco UCS rack servers, an appliance port, or a FCoE port. 

In the Cisco UCS Manager GUI, the scalability port is displayed as Scalability Port 5 below the Ethernet Ports node. The individual breakout ports are displayed as Port 1 through Port 4. 

In the Cisco UCS Manager CLI, the scalability port is not displayed, but the individual breakout ports are displayed as Br-Eth1/5/1 through Br-Eth1/5/4 . 

#### Configuring Scalability Ports

To configure ports, port channel members or SPAN members on the scalability port, scope into the scalability port first, then follow the steps for a standard unified port. 

##### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope eth-server |  Enters Ethernet server mode.   
**Step 2** |  UCS-A /eth-server #  scope fabric {a | b}  |  Enters Ethernet server fabric mode for the specified fabric.   
**Step 3** |  UCS-A /eth-server/fabric #  scope aggr-interface slot-num port-num |  Enters ethernet server fabric aggregate interface mode for the scalability port.   
**Step 4** |  UCS-A /eth-server/fabric/aggr-interface #  show interface |  Displays the interfaces on the scalability port.   
**Step 5** |  UCS-A /eth-server/fabric/aggr-interface #  create interface slot-num port-num |  Creates an interface for the specified Ethernet server port.   
**Step 6** |  UCS-A /eth-server/fabric/aggr-interface #  commit-buffer |  Commits the transaction to the system configuration.   
  
##### Example

The following example shows how to create an interface for Ethernet server port 3 on the fabric A scalability port and commit the transaction: 
    
    
    UCS-A# **scope eth-server**
    UCS-A /eth-server # **scope fabric a**
    UCS-A /eth-server/fabric # **scope aggr-interface 1 5**
    UCS-A /eth-server/fabric/aggr-interface # **show interface**
    Interface:
    
    Slot Id Aggr-Port ID Port Id  Admin State Oper State    State Reason
    ------- ------------ -------- ----------- ------------- ------------
          1            5        1 Enabled     Up
          1            5        2 Enabled     Up     
          1            5        3 Enabled     Admin Down    Administratively Down
          1            5        4 Enabled     Admin Down    Administratively Down
    
    UCS-A /eth-server/fabric/aggr-interface # **create interface 1 3**
    UCS-A /eth-server/fabric/aggr-interface* # **commit-buffer**
    UCS-A /eth-server/fabric/aggr-interface # 
    

### Beacon LEDs for Unified Ports 

Each port fabric interconnect has a corresponding beacon LED. When the Beacon LED property is configured, the beacon LEDs illuminate, showing you which ports are configured in a given port mode. 

You can configure the Beacon LED property to show you which ports are grouped in one port mode: either Ethernet or Fibre Channel. By default, the Beacon LED property is set to Off. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For unified ports on the expansion module, you can reset the Beacon LED property to the default value of Off during expansion module reboot. 

* * *  
  
---|---  
  
#### Configuring the Beacon LEDs for Unified Ports

Complete the following task for each module for which you want to configure beacon LEDs. 

##### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope fabric-interconnect` `{a | b}  |  Enters fabric interconnect mode for the specified fabric.  
**Step 2** |  UCS-A /fabric # scope card` `slot-id |  Enters card mode for the specified fixed or expansion module.  
**Step 3** |  UCS-A /fabric/card # scope beacon-led |  Enters beacon LED mode.  
**Step 4** |  UCS-A /fabric/card/beacon-led # set admin-state` `{eth | fc | off}  |  Specifies which port mode is represented by illuminated beacon LED lights.

eth
     All of the Unified Ports configured in Ethernet mode illuminate.

fc
     All of the Unified Ports configured in Fibre Channel mode illuminate.

off
     Beacon LED lights for all ports on the module are turned off.  
**Step 5** |  UCS-A /fabric/card/beacon-led # commit-buffer |  Commits the transaction to the system configuration.  
  
##### Example

The following example illuminates all of the beacon lights for Unified Ports in Ethernet port mode and commits the transaction:
    
    
    UCS-A# **scope fabric-interconnect a**
    UCS-A /fabric # **scope card 1**
    UCS-A /fabric/card # **scope beacon-led**
    UCS-A /fabric/card/beacon-led # **set admin-state eth**
    UCS-A /fabric/card/beacon-led* # **commit-buffer**
    UCS-A /fabric/card/beacon-led #

---

## Page 7: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Network-Mgmt/4-3/b_cli_ucsm_network_management_guide_4_3/b_CLI_UCSM_Network_Management_Guide_chapter_0101.html

## VLANs

A VLAN is a switched network that is logically segmented by function, project team, or application, without regard to the physical locations of the users. VLANs have the same attributes as physical LANs, but you can group end stations even if they are not physically located on the same LAN segment. 

Any switch port can belong to a VLAN. Unicast, broadcast, and multicast packets are forwarded and flooded only to end stations in the VLAN. Each VLAN is considered a logical network, and packets destined for stations that do not belong to the VLAN must be forwarded through a router or bridge. 

VLANs are typically associated with IP subnetworks. For example, all of the end stations in a particular IP subnet belong to the same VLAN. To communicate between VLANs, you must route the traffic. By default, a newly created VLAN is operational. Additionally, you can configure VLANs to be in the active state, which is passing traffic, or in the suspended state, in which the VLANs are not passing packets. By default, the VLANs are in the active state and pass traffic. 

---

## Page 8: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Network-Mgmt/4-3/b_cli_ucsm_network_management_guide_4_3/b_CLI_UCSM_Network_Management_Guide_chapter_0110.html

## LAN Pin Groups 

Cisco UCS uses LAN pin groups to pin Ethernet traffic from a vNIC on a server to an uplink Ethernet port or port channel on the fabric interconnect. You can use this pinning to manage the distribution of traffic from the servers. 

To configure pinning for a server, you must include the LAN pin group in a vNIC policy. The vNIC policy is then included in the service profile assigned to that server. All traffic from the vNIC travels through the I/O module to the specified uplink Ethernet port. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

If you do not assign a pin group to a server interface through a vNIC policy, Cisco UCS Manager chooses an uplink Ethernet port or port channel for traffic from that server interface dynamically. This choice is not permanent. A different uplink Ethernet port or port channel may be used for traffic from that server interface after an interface flap or a server reboot.  If an uplink is part of a LAN pin group, the uplink is not necessarily reserved for only that LAN pin group. Other vNIC's policies that do not specify a LAN pin group can use the uplink as a dynamic uplink. 

* * *  
  
---|---

---

## Page 9: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Network-Mgmt/4-3/b_cli_ucsm_network_management_guide_4_3/b_CLI_UCSM_Network_Management_Guide_chapter_0111.html

## MAC Pools  
  
A MAC pool is a collection of network identities, or MAC addresses, that are unique in their Layer 2 environment and are available to be assigned to vNICs on a server. If you use MAC pools in service profiles, you do not have to manually configure the MAC addresses to be used by the server associated with the service profile. 

In a system that implements multitenancy, you can use the organizational hierarchy to ensure that MAC pools can be used only by specific applications or business services. Cisco UCS uses the name resolution policy to assign MAC addresses from the pool. 

To assign a MAC address to a server, you must include the MAC pool in a vNIC policy. The vNIC policy is then included in the service profile assigned to that server. 

You can specify your own MAC addresses or use a group of MAC addresses provided by Cisco. 

---

## Page 10: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Network-Mgmt/4-3/b_cli_ucsm_network_management_guide_4_3/b_CLI_UCSM_Network_Management_Guide_chapter_01000.html

## Quality of Service 

Cisco UCS provides the following methods to implement quality of service: 

  * System classes that specify the global configuration for certain types of traffic across the entire system 

  * QoS policies that assign system classes for individual vNICs 

  * Flow control policies that determine how uplink Ethernet ports handle pause frames 


Global QoS changes made to the QoS system class may result in brief data-plane interruptions for all traffic. Some examples of such changes are: 

  * Changing the MTU size for an enabled class 

  * Changing packet drop for an enabled class 

  * Changing the CoS value for an enabled class 


###  Guidelines and Limitations for Quality of Service on Cisco UCS Fabric Interconnects 9108 100G, Cisco UCS 6536 Fabric Interconnects, Cisco UCS 6400 Series Fabric Interconnects 

  * Multicast optimization is not supported.

  * For all QoS system classes except for Fibre Channel, the default MTU is 1500 bytes. The MTU for Fiber Channel class is not configurable and is set to 2240 bytes internally. All classes (excluding Fibre Channel) allow for MTU configuration up to a maximum of 9216 bytes. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The maximum MTU for a QoS class on the Fabric Interconnect is 9216 bytes, while the maximum MTU that can be set on a vNIC is 9000 bytes. The vNIC MTU is configured through the adapter policy. 

* * *  
  
---|---  
  * The MTU size for fibre channel is always 2240 bytes.

  * Multicast is not supported on any no-drop QoS class.


###  Guidelines and Limitations for Quality of Service on Cisco UCS 6300 Series Fabric Interconnect

  * Cisco UCS 6300 Series Fabric Interconnect uses a shared buffer for all system classes. 

  * Multicast optimization is not supported. 

  * Multicast is not supported on any no-drop QoS class.

  * When you change the QoS parameters for any class causes traffic disruption to all classes. The following table lists the changes in the QoS system class and the conditions that trigger a system reboot. 

QoS System class status  |  Condition  |  FI Reboot Status   
---|---|---  
Enabled  |  Change between drop and no drop  |  Yes   
No-drop  |  Change between enable and disable  |  Yes   
Enable and no-drop  |  Change in MTU size  |  Yes   
  * The subordinate FI reboots first as a result of the change in the QoS system class. The primary FI reboots only after you acknowledge it in Pending Activities. 


###  Guidelines and Limitations for Quality of Service on Cisco UCS Mini

  * Cisco UCS Mini uses a shared buffer for all system classes. 

  * The bronze class shares the buffer with SPAN. We recommend using either SPAN or the bronze class. 

  * Multicast optimization is not supported. 

  * Multicast is not supported on any no-drop QoS class.

  * Changing the QoS parameters for any class causes traffic disruption to all classes. 

  * When mixing Ethernet and FC or FCoE traffic, the bandwidth distribution is not equal. 

  * Multiple streams of traffic from the same class may not be distributed equally. 

  * Use the same CoS values for all no-drop policies to avoid any FC or FCoE performance issues. 

  * Only the platinum and gold classes support no-drop policies. 


---

## Page 11: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Network-Mgmt/4-3/b_cli_ucsm_network_management_guide_4_3/m_cli_port_security.html

## Port Security Overview

The port security feature allows you to restrict input to an interface by limiting and identifying MAC addresses of the workstations that are allowed to access the port. It helps you to control the learning and storing of MAC addresses for each interface. It is used to protect against CAM overflow attacks and rogue equipment, such as hubs and switches, being plugged in. A port security enabled port is called a secure port, and the MAC addresses allowed on that port are called secure MAC addresses.When you assign secure MAC addresses to a secure port, the port does not forward packets with source addresses outside the group of defined addresses. If you limit the number of secure MAC addresses to one and assign a single secure MAC address to a secure port, the workstation attached to that port is assured the full bandwidth of the port. 

After you have set the maximum number of secure MAC addresses on a port, you can include secure MAC addresses in an address table in one of these ways: 

  * Configure all secure MAC addresses by using the switchport port-security mac-address mac_address interface configuration command. 

  * Allow the port to dynamically configure secure MAC addresses with the MAC addresses of connected devices.

  * Configure a number of addresses and allow the rest to be dynamically configured.

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

If the port shuts down, all dynamically learned addresses are removed.

* * *  
  
---|---  
  * Configure MAC addresses to be sticky. These can be dynamically learned or manually configured, stored in the address table, and added to the running configuration. If these addresses are saved in the configuration file, the interface does not need to dynamically relearn them when the switch restarts. Although sticky secure addresses can be manually configured, it is not recommended. 


### MAC Learning

After port security is enabled on an interface and a new MAC address is seen on the interface, a security validation is done for the new MAC address. Based on this validation, the MAC address will be added to the address table - either as a normal entry or a drop entry. 

---

## Page 12: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Network-Mgmt/4-3/b_cli_ucsm_network_management_guide_4_3/b_CLI_UCSM_Network_Management_Guide_chapter_01001.html

## Upstream Disjoint Layer-2 Networks 

Upstream disjoint layer-2 networks (disjoint L2 networks) are required if you have two or more Ethernet clouds that never connect, but must be accessed by servers or virtual machines located in the same Cisco UCS domain. For example, you could configure disjoint L2 networks if you require one of the following: 

  * Servers or virtual machines to access a public network and a backup network 

  * Servers or virtual machines for more than one customer are located in the same Cisco UCS domain, and that need to access the L2 networks for both customers in a multi-tenant system 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

By default, data traffic in Cisco UCS works on a principle of mutual inclusion. All traffic for all VLANs and upstream networks travels along all uplink ports and port channels. If you have upgraded from a release that does not support upstream disjoint layer-2 networks, you must assign the appropriate uplink interfaces to your VLANs, or traffic for those VLANs continues to flow along all uplink ports and port channels. 

* * *  
  
---|---  
  
The configuration for disjoint L2 networks works on a principle of selective exclusion. Traffic for a VLAN that is designated as part of a disjoint network can only travel along an uplink Ethernet port or port channel that is specifically assigned to that VLAN, and is selectively excluded from all other uplink ports and port channels. However, traffic for VLANs that are not specifically assigned to an uplink Ethernet port or port channel can still travel on all uplink ports or port channels, including those that carry traffic for the disjoint L2 networks. 

In Cisco UCS, the VLAN represents the upstream disjoint L2 network. When you design your network topology for disjoint L2 networks, you must assign uplink interfaces to VLANs not the reverse. 

For information about the maximum number of supported upstream disjoint L2 networks, see the appropriate Cisco UCS Configuration Limits for Cisco UCS Manager Guide. 

---

## Page 13: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Network-Mgmt/4-3/b_cli_ucsm_network_management_guide_4_3/b_CLI_UCSM_Network_Management_Guide_chapter_01011.html

## vNIC Template 

The vNIC LAN connectivity policy defines how a vNIC on a server connects to the LAN. 

Cisco UCS Manager does not automatically create a VM-FEX port profile with the correct settings when you create a vNIC template. If you want to create a VM-FEX port profile, you must configure the target of the vNIC template as a VM. You must include this policy in a service profile for it to take effect. 

You can select VLAN groups in addition to any individual VLAN while creating a vNIC template.

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

If your server has two Emulex or QLogic NICs (Cisco UCS CNA M71KR-E or Cisco UCS CNA M71KR-Q), you must configure vNIC policies for both adapters in your service profile to get a user-defined MAC address for both NICs. If you do not configure policies for both NICs, Windows still detects both of them in the PCI bus. Then because the second eth is not part of your service profile, Windows assigns it a hardware MAC address. If you then move the service profile to a different server, Windows sees additional NICs because one NIC did not have a user-defined MAC address. 

* * *  
  
---|---  
  
### Creating vNIC Template Pairs 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A/ org # create vnic-templ  vnic-primary .  |  Creates a Primary vNIC template.   
**Step 2** |  UCS-A/ # org vnic-templ set type updating-template .  |  Set the template type to updating, which drives the configurations in the Primary vNIC template for shared configurations to the peer vNIC template. See the shared configurations listed below.   
**Step 3** |  UCS-A/ # org vnic-templ  [set fabric {a | b}]  .  |  Specifies the fabric for the Primary vNIC template. If you specify Fabric A for the Primary vNIC template, the Secondary vNIC template must be Fabric B or vice versa.   
**Step 4** |  UCS-A/ # org vnic-templ set descr primaryinredundancypair .  |  Sets the template as the Primary vNIC template.   
**Step 5** |  UCS-A/ # org vnic-templ set redundancy-type  primary .  |  Sets the redundancy template type as the Primary vNIC template.  Following are descriptions of the Redundancy Types:  Primary—Creates configurations that can be shared with the Secondary vNIC template. Any shared changes on the Primary vNIC template are automatically synchronized to the Secondary vNIC template.  Secondary — All shared configurations are inherited from the Primary template.  No Redundancy— Legacy vNIC template behavior.  Following is a list of shared configurations: 

  * Network Control Policy
  * QoS Policy 
  * Stats Threshold Policy 
  * Template Type
  * Connection Policies
  * VLANS
  * MTU

Following is a list of non-shared configurations: 

  * Fabric ID
  * CDN Source
  * MAC Pool 
  * Description
  * Pin Group Policy

  
**Step 6** |  UCS-A/ # org vnic-templ exit .  |  Exits creating the redundancy template pairing.  |  **Note** |  Ensure to commit the transaction after linking the Primary vNIC template to a peer Secondary vNIC template to create the redundancy pair.   
---|---  
**Step 7** |  UCS-A/ # org vnic-templ create vNIC-templ  vNICsecondary .  |  Creates the Secondary vNIC template.   
**Step 8** |  UCS-A/ # org vnic-templ set type updating-template .  |  Sets the template type to updating, which automatically inherits the configurations from the Primary vNIC template.   
**Step 9** |  UCS-A/ org # vnic-templ  [set fabric {a | b}]  .  |  Specifies the fabric for the Secondary vNIC template. If you specify Fabric A for the Primary vNIC template, the Secondary vNIC template must be Fabric B or vice versa.   
**Step 10** |  UCS-A/ # org vnic-templ set descr secondaryredundancypair .  |  Sets the secondary vNIC template as a redundancy pair template.   
**Step 11** |  UCS-A/ # org vnic-templ set redundancy-type  secondary .  |  Sets the vNIC template type as Secondary.   
**Step 12** |  UCS-A/ # org vnic-templ set peer-template-name  vNIC-primary .  |  Sets the Primary vNIC template as the peer to the Secondary vNIC template.   
**Step 13** |  UCS-A/ # org vnic-templ  commit-buffer .  |  Commits the transaction to the system configuration.   
  
#### Example

The following example configures a vNIC redundancy template pair and commits the transaction: 
    
    
    UCS-A /org* # **create vnic-template vnic-primary**
    UCS-A /org/vnic-templ* # **set type updating-template**
    UCS-A /org/vnic-templ* # **set fabric a**
    UCS-A /org/vnic-templ* # **set descr primaryinredundancypair**
    UCS-A /org/vnic-templ* # **set redundancy-type primary**
    UCS-A /org/vnic-templ* # **exit**
    UCS-A /org* # **create vnic-templ vnicsecondary**
    UCS-A /org/vnic-templ* # **set fabric b**
    UCS-A /org/vnic-templ* # **set descr secondaryinredundancypair**
    UCS-A /org/vnic-templ* # **set redundancy-type secondary**
    UCS-A /org/vnic-templ* # **set peer-template-name vnic-primary**
    UCS-A /org/vnic-templ* # **commit-buffer**
    UCS-A /org/vnic-templ # 
    

#### What to do next

After you create the vNIC redundancy template pair, you can use the redundancy template pair to create redundancy vNIC pairs for any service profile in the same organization or sub- organization. 

### Undo vNIC Template Pairs 

You can undo the vNIC template pair by changing the Peer Redundancy Template so that there is no peer template for the Primary or the Secondary template. When you undo a vNIC template pair, the corresponding vNIC pairs also becomes undone. 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A /org #  scope vnic-templ template1 .  |  Specifies the name of the vNIc template that you want to undo from the template pair.   
**Step 2** |  UCS-A /org/ vnic-templ #  set redundancy-type no redundancy .  |  Removes the paring between the peer Primary or Secondary redundancy template used to perform the template pairing.   
**Step 3** |  UCS-A /org/vnic-templ* #  commit-buffer .  |  Commits the transaction to the system configuration.   
  
#### Example

The following example shows how to undo a template pairing: 
    
    
    UCS-A /org # **scope vnic-templ template1**
    UCS-A /org/vnic-templ # **set redundancy-type no-redundancy**
    UCS-A /org/vnic-templ* # commit buffer
    

### Configuring a vNIC Template

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope org org-name |  Enters the organization mode for the specified organization. To enter the root organization mode, enter / as the org-name .   
**Step 2** |  UCS-A /org # create vnic-templ vnic-templ-name [eth-if vlan-name] [fabric {a | b}] [target [adapter | vm]]  |  Creates a vNIC template and enters organization vNIC template mode.  The target you choose determines whether or not Cisco UCS Manager automatically creates a VM-FEX port profile with the appropriate settings for the vNIC template. This can be one of the following: 

  * Adapter—The vNICs apply to all adapters. No VM-FEX port profile is created if you choose this option. 
  * VM—The vNICs apply to all virtual machines. A VM-FEX port profile is created if you choose this option. 

  
**Step 3** |  (Optional) UCS-A /org/vnic-templ # set descr description | (Optional)  Provides a description for the vNIC template.   
**Step 4** |  (Optional) UCS-A /org/vnic-templ # set fabric {a | a-b | b | b-a}  | (Optional)  Specifies the fabric to use for the vNIC. If you did not specify the fabric when creating the vNIC template in Step 2, you have the option to specify it with this command.  If you want this vNIC to be able to access the second fabric interconnect if the default one is unavailable, choose a-b (A is the primary) or b-a (B is the primary) .  |  **Note** |  Do not enable fabric failover for the vNIC under the following circumstances: 

  * If the Cisco UCS domain is running in Ethernet Switch Mode. vNIC fabric failover is not supported in that mode. If all Ethernet uplinks on one fabric interconnect fail, the vNICs do not fail over to the other. 
  * If you plan to associate this vNIC to a server with an adapter that does not support fabric failover, such as the Cisco UCS 82598KR-CI 10-Gigabit Ethernet Adapter. If you do so, Cisco UCS Manager generates a configuration fault when you associate the service profile with the server. 

  
---|---  
**Step 5** |  UCS-A /org/vnic-templ # set mac-pool mac-pool-name |  The MAC address pool that vNICs created from this vNIC template should use.  
**Step 6** |  UCS-A /org/vnic-templ # set mtu mtu-value |  The maximum transmission unit, or packet size, that vNICs created from this vNIC template should use. Enter an integer between 1500 and 9000.  |  **Note** |  If the vNIC template has an associated QoS policy, the MTU specified here must be equal to or less than the MTU specified in the associated QoS system class. If this MTU value exceeds the MTU value in the QoS system class, packets may be dropped during data transmission.  For VIC 1400 Series, VIC 14000 Series, and VIC 15000 Series adapters, you can change the MTU size of the vNIC from the host interface settings. When the Overlay network is configured, make sure that the new value is equal to or less than the MTU specified in the associated QoS system class or packets could be dropped during data transmission.   
---|---  
**Step 7** |  UCS-A /org/vnic-templ # set nw-control-policy policy-name |  The network control policy that vNICs created from this vNIC template should use.  
**Step 8** |  UCS-A /org/vnic-templ # set pin-group group-name |  The LAN pin group that vNICs created from this vNIC template should use.  
**Step 9** |  UCS-A /org/vnic-templ # set qos-policy policy-name |  The quality of service policy that vNICs created from this vNIC template should use.  
**Step 10** |  UCS-A /org/vnic-templ # set stats-policy policy-name |  The statistics collection policy that vNICs created from this vNIC template should use.  
**Step 11** |  UCS-A /org/vnic-templ # set type {initial-template | updating-template}  |  Specifies the vNIC template update type. If you do not want vNIC instances created from this template to be automatically updated when the template is updated, use the initial-template keyword; otherwise, use the  updating-template keyword to ensure that all vNIC instances are updated when the vNIC template is updated.   
**Step 12** |  UCS-A /org/vnic-templ #  commit-buffer |  Commits the transaction to the system configuration.   
  
#### Example

The following example configures a vNIC template and commits the transaction: 
    
    
    UCS-A# **scope org /**
    UCS-A /org* # **create vnic template VnicTempFoo**
    UCS-A /org/vnic-templ* # **set descr "This is a vNIC template example."**
    UCS-A /org/vnic-templ* # **set fabric a**
    UCS-A /org/vnic-templ* # **set mac-pool pool137**
    UCS-A /org/vnic-templ* # **set mtu 8900**
    UCS-A /org/vnic-templ* # **set nw-control-policy ncp5**
    UCS-A /org/vnic-templ* # **set pin-group PinGroup54**
    UCS-A /org/vnic-templ* # **set qos-policy QosPol5**
    UCS-A /org/vnic-templ* # **set stats-policy ServStatsPolicy**
    UCS-A /org/vnic-templ* # **set type updating-template**
    UCS-A /org/vnic-templ* # **commit-buffer**
    UCS-A /org/vnic-templ # 
    

### Deleting a vNIC Template

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope org org-name |  Enters the organization mode for the specified organization. To enter the root organization mode, enter / as the org-name .   
**Step 2** |  UCS-A /org #  delete vnic-templ ` ` vnic-templ-name |  Deletes the specified vNIC template.   
**Step 3** |  UCS-A /org #  commit-buffer |  Commits the transaction to the system configuration.   
  
#### Example

The following example deletes the vNIC template named VnicTemp42 and commits the transaction: 
    
    
    UCS-A# **scope org /**
    UCS-A /org # **delete vnic template VnicTemp42**
    UCS-A /org* # **commit-buffer**
    UCS-A /org # 
    

---

## Page 14: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Network-Mgmt/4-3/b_cli_ucsm_network_management_guide_4_3/m-cli-macsec-4-3.html

## About MACsec

MACsec is an IEEE 802.1AE standards-based Layer 2 hop-by-hop encryption that provides data confidentiality and integrity for media access independent protocols. 

MACsec provides MAC-layer encryption over wired networks by using out-of-band methods for encryption keying. The MACsec Key Agreement (MKA) Protocol provides the required session keys and manages the required encryption keys. 

MACsec encrypts the entire data except for the Source and Destination MAC addresses of an Ethernet packet. It offers the following capabilities: 

  * Provides line rate encryption.

  * Ensures data confidentiality by providing strong encryption at Layer 2. 

  * Provides integrity checking to help ensure that data cannot be modified in transit. 

  * Key Lifetime and Hitless Key Rollover

  * Fallback Key


### Key Lifetime and Hitless Key Rollover

A MACsec keychain can have multiple pre-shared keys (PSKs), each configured with a key ID and an optional lifetime. A key lifetime specifies at which time the key activates and expires. In the absence of a lifetime configuration, the default lifetime is unlimited. When a lifetime is configured, MKA rolls over to the next configured pre-shared key in the keychain after the lifetime is expired. The time zone of the key can be local or UTC. The default time zone is UTC. 

To configure a MACsec keychain, see Creating a MACsec Keychain

A key can roll over to a second key within the same keychain by configuring the second key (in the keychain) and configuring a lifetime for the first key. When the lifetime of the first key expires, it automatically rolls over to the next key in the list. If the same key is configured on both sides of the link at the same time, then the key rollover is hitless (that is, the key rolls over without traffic interruption). 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The lifetime of the keys are overlapped to achieve hitless key rollover.

* * *  
  
---|---  
  
### Fallback Key

A MACsec session can fail due to a key/key ID (CKN) mismatch or a finite key duration between the Fabric Interconnect and the peer. If a MACsec session fails, a fallback session can take over if a fallback key is configured. A fallback session prevents downtime due to primary session failure and allows a user time to fix the key issue causing the failure. A fallback key also provides a backup session if the primary session fails to start. This feature is optional. 

For more information, see Creating a MACsec Keychain. 

---

## Page 15: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Network-Mgmt/4-3/b_CLI_UCSM_Network_Management_Guide_chapter_0100.html

## Unified Ports on 6300 Series Fabric Interconnects 

Unified ports are ports on the Cisco UCS 6300 Series Fabric Interconnects that you can configure to carry either Ethernet or Fibre Channel traffic. A Cisco UCS domain cannot use these un-reserved ports until you configure them. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

When you configure a port on a fabric interconnect, the administrative state is automatically set to enabled. If the port is connected to another device, this may cause traffic disruption. You can disable the port after configuring it. Configurable beacon LEDs indicate which unified ports are configured for the selected port mode. 

* * *  
  
---|---  
  
### Port Modes

The port mode determines whether a unified port on the fabric interconnect is configured to carry Ethernet or Fibre Channel traffic. You configure the port mode in Cisco UCS Manager. However, the fabric interconnect does not automatically discover the port mode. 

Changing the port mode deletes the existing port configuration and replaces it with a new logical port. Any objects associated with that port configuration, such as VLANs and VSANS, are also removed. There is no restriction on the number of times you can change the port mode for a unified port. 

### Port Types

The port type defines the type of traffic carried over a unified port connection. 

By default, unified ports changed to Ethernet port mode are set to the Ethernet uplink port type. Unified ports changed to Fibre Channel port mode are set to the Fibre Channel uplink port type. You cannot unconfigure Fibre Channel ports. 

Changing the port type does not require a reboot. 

Ethernet Port Mode

When you set the port mode to Ethernet, you can configure the following port types: 

  * Server ports 

  * Ethernet uplink ports 

  * Ethernet port channel members 

  * FCoE ports 

  * Appliance ports 

  * Appliance port channel members 

  * SPAN destination ports 

  * SPAN source ports 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For SPAN source ports, configure one of the port types and then configure the port as SPAN source. 

* * *  
  
---|---  


Fibre Channel Port Mode

When you set the port mode to Fibre Channel, you can configure the following port types: 

  * Fibre Channel uplink ports 

  * Fibre Channel port channel members

  * Fibre Channel storage ports 

  * SPAN source ports 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For SPAN source ports, configure one of the port types and then configure the port as SPAN source. 

* * *  
  
---|---  


### Data Traffic Interruption from Port Mode Changing 

Port mode changes can cause an interruption to the data traffic for the Cisco UCS domain. The length of the interruption and the affected traffic depend upon the configuration of the Cisco UCS domain and the module on which you made the port mode changes. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/tip.gif)  
**Tip** | 

* * *

To minimize traffic disruption during system changes, form a Fibre Channel uplink port-channel across the fixed and expansion modules. 

* * *  
  
---|---  
  
#### Impact of Port Mode on an Expansion Module 

After you make port mode changes on an expansion module, the module reboots. All traffic through port on the expansion module is interrupted for approximately 1 minute while the module reboots. 

#### Impact of Port Mode Changes on the Fixed Module in a Cluster Configuration 

A cluster configuration has two fabric interconnects. After you make port changes to the fixed module, the fabric interconnect reboots. The impact on the data traffic depends upon whether or not you have configured the server vNICs to failover to the other fabric interconnect when one fails. 

If you change the port modes on the expansion module of one fabric interconnect and then wait for that to reboot before changing the port modes on the second fabric interconnect, the following occurs: 

  * With server vNIC failover, traffic fails over to the other fabric interconnect and no interruption occurs. 

  * Without server vNIC failover, all data traffic through the fabric interconnect on which you changed the port modes is interrupted for approximately eight minutes while the fabric interconnect reboots. 


When you change the port modes on the fixed modules of both fabric interconnects simultaneously, all data traffic through the fabric interconnects are interrupted for approximately eight minutes while the fabric interconnects reboot. 

#### Impact of Port Mode Changes on the Fixed Module in a Standalone Configuration 

A standalone configuration has only one fabric interconnect. After you make port changes to the fixed module, the fabric interconnect reboots. All data traffic through the fabric interconnect is interrupted for approximately eight minutes while the fabric interconnect reboots. 

### Guidelines for Configuring Unified Ports 

Consider the following guidelines and restrictions when configuring unified ports: 

#### Port Mode Placement 

Because the Cisco UCS Manager GUI interface uses a slider to configure the port mode for unified ports on a fixed or expansion module, it automatically enforces the following restrictions which limits how port modes can be assigned to unified ports. When using the Cisco UCS Manager CLI interface, these restrictions are enforced when you commit the transaction to the system configuration. If the port mode configuration violates any of the following restrictions, the Cisco UCS Manager CLI displays an error: 

  * Ethernet ports must be grouped together in a block. For each module (fixed or expansion), the Ethernet port block must start with the first port and end with an even numbered port. 

  * Fibre Channel ports must be grouped together in a block. For each module (fixed or expansion), the first port in the Fibre Channel port block must follow the last Ethernet port and extend to include the rest of the ports in the module. For configurations that include only Fibre Channel ports, the Fibre Channel block must start with the first port on the fixed or expansion module. 

  * Alternating Ethernet and Fibre Channel ports is not supported. 


**Example of a valid configuration** — Might include unified ports 1–16 on the fixed module configured in Ethernet port mode and ports 17–32 in Fibre Channel port mode. On the expansion module you could configure ports 1–4 in Ethernet port mode and then configure ports 5–16 in Fibre Channel mode. The rule about alternating Ethernet and Fibre Channel port types is not violated because this port arrangement complies with the rules on each individual module. 

**Example of an invalid configuration** — Might include a block of Fibre Channel ports starting with port 16. Because each block of ports has to start with an odd-numbered port, you would have to start the block with port 17. 

The total number of uplink Ethernet ports and uplink Ethernet port channel members that can be configured on each fabric interconnect is limited to 31. This limitation includes uplink Ethernet ports and uplink Ethernet port channel members configured on the expansion module. 

#### Special Considerations for UCS Manager CLI Users 

Because the Cisco UCS Manager CLI does not validate port mode changes until you commit the buffer to the system configuration, it is easy to violate the grouping restrictions if you attempt to commit the buffer before creating at least two new interfaces. To prevent errors, we recommend that you wait to commit your changes to the system configuration until you have created new interfaces for all of the unified ports changing from one port mode to another. 

Commiting the buffer before configuring multiple interfaces will result in an error, but you do not need to start over. You can continue to configure unified ports until the configuration satisfies the aforementioned requirements. 

### Cautions and Guidelines for Configuring Unified Uplink Ports and Unified Storage Ports 

The following are cautions and guidelines to follow while working with unified uplink ports and unified storage ports: 

  * In an unified uplink port, if you enable one component as a SPAN source, the other component will automatically become a SPAN source. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

If you create or delete a SPAN source under the Ethernet uplink port, Cisco UCS Manager automatically creates or deletes a SPAN source under the FCoE uplink port. The same happens when you create a SPAN source on the FCOE uplink port. 

* * *  
  
---|---  
  * You must configure a non default native VLAN on FCoE and unified uplink ports. This VLAN is not used for any traffic. Cisco UCS Manager will reuse an existing fcoe-storage-native-vlan for this purpose. This fcoe-storage-native-vlan will be used as a native VLAN on FCoE and unified uplinks. 

  * In an unified uplink port, if you do not specify a non default VLAN for the Ethernet uplink port the fcoe-storage-native-vlan will be assigned as the native VLAN on the unified uplink port. If the Ethernet port has a non default native VLAN specified as native VLAN, this will be assigned as the native VLAN for unified uplink port. 

  * When you create or delete a member port under an Ethernet port channel, Cisco UCS Manager automatically creates or deletes the member port under FCoE port channel. The same happens when you create or delete a member port in FCoE port channel. 

  * When you configure an Ethernet port as a standalone port, such as server port, Ethernet uplink, FCoE uplink or FCoE storage and make it a member port for an Ethernet or FCoE port channel, Cisco UCS Manager automatically makes this port a member of both Ethernet and FCoE port channels. 

  * When you remove the membership for a member port from being a member of server uplink, Ethernet uplink, FCoE uplink or FCoE storage, Cisco UCS Manager deletes the corresponding members ports from Ethernet port channel and FCoE port channel and creates a new standalone port. 

  * If you downgrade Cisco UCS Manager from release 2.1 to any of the prior releases, all unified uplink ports and port channels will be converted to Ethernet ports and Ethernet port channels when the downgrade is complete. Similarly, all the unified storage ports will be converted to appliance ports. 

  * For unified uplink ports and unified storage ports, when you create two interfaces, only one license is checked out. As long as either interface is enabled, the license remains checked out. The license will be released only if both the interfaces are disabled for a unified uplink port or a unified storage port. 


### Configuring the Port Mode 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/caut.gif)  
**Caution** | 

* * *

Changing the port mode can cause an interruption in data traffic because changes to the fixed module require a reboot of the fabric interconnect.  If the Cisco UCS domain has a cluster configuration that is set up for high availability and servers with service profiles that are configured for failover, traffic fails over to the other fabric interconnect and data traffic is not interrupted when the port mode is changed on the fixed module. 

* * *  
  
---|---  
  
In the Cisco UCS Manager CLI, there are no new commands to support Unified Ports. Instead, you change the port mode by scoping to the mode for the desired port type and then creating a new interface. When you create a new interface for an already configured slot ID and port ID, UCS Manager deletes the previously configured interface and creates a new one. If a port mode change is required because you configure a port that previously operated in Ethernet port mode to a port type in Fibre Channel port mode, UCS Manager notes the change. 

Expansions modules are not supported with Cisco UCS Mini. 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope` `port-type-mode |  Enters the specified port type mode for one of the following port types: 

eth-server 
     For configuring server ports. 

eth-storage 
     For configuring Ethernet storage ports and Ethernet storage port channels. 

eth-traffic-mon 
     For configuring Ethernet SPAN ports. 

eth-uplink 
     For configuring Ethernet uplink ports. 

fc-storage 
     For configuring Fibre Channel storage ports. 

fc-traffic-mon 
     For configuring Fibre Channel SPAN ports. 

fc-uplink 
     For configuring Fibre Channel uplink ports and Fibre Channel uplink port channels.   
**Step 2** |  UCS-A /port-type-mode # scope fabric` `{a | b}  |  Enters the specified port type mode for the specified fabric.   
**Step 3** |  UCS-A /port-type-mode/fabric # create interface` `slot-id` `port-id |  Creates an interface for the specified port type.  If you are changing the port type from Ethernet port mode to Fibre Channel port mode, or vice-versa, the following warning appears:  `Warning: This operation will change the port mode (from Ethernet to FC or vice-versa). When committed, this change will require the module to restart.`  
**Step 4** |  Create new interfaces for other ports belonging to the Ethernet or Fibre Channel port block.  |  There are several restrictions that govern how Ethernet and Fibre Channel ports can be arranged on a fixed or expansion module. Among other restrictions, it is required that you change ports in groups of two. Violating any of the restrictions outlined in the Guidelines and Recommendations for Configuring Unified Ports section will result in an error.   
**Step 5** |  UCS-A /port-type-mode/fabric/interface # commit-buffer |  Commits the transaction to the system configuration.   
  
Based on the module for which you configured the port modes, data traffic for the Cisco UCS domain is interrupted as follows: 

  * Fixed module—The fabric interconnect reboots. All data traffic through that fabric interconnect is interrupted. In a cluster configuration that provides high availability and includes servers with vNICs that are configured for failover, traffic fails over to the other fabric interconnect and no interruption occurs. Changing the port mode for both sides at once results in both fabric interconnects rebooting simultaneously and a complete loss of traffic until both fabric interconnects are brought back up.

It takes about 8 minutes for the fixed module to reboot. 

  * Expansion module—The module reboots. All data traffic through ports in that module is interrupted. 

It takes about 1 minute for the expansion module to reboot. 


#### Example

The following example changes ports 3 and 4 on slot 1 from Ethernet uplink ports in Ethernet port mode to uplink Fibre Channel ports in Fibre Channel port mode: 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

This example is not applicable for Cisco UCS 6500 Series Fabric Interconnect. 

* * *  
  
---|---  
      
    
    UCS-A# **scope fc-uplink**
    UCS-A /fc-uplink # **scope fabric a**
    UCS-A /fc-uplink/fabric # **create interface 1 3**
    Warning: This operation will change the port mode (from Ethernet to FC or vice-versa). 
    When committed, this change will require the fixed module to restart.
    UCS-A /fc-uplink/fabric/interface* # **up**
    UCS-A /fc-uplink/fabric* #**create interface 1 4**
    Warning: This operation will change the port mode (from Ethernet to FC or vice-versa). 
    When committed, this change will require the fixed module to restart.
    UCS-A /fc-uplink/fabric/interface* #**commit-buffer**

Configuring Breakout Ports

### Port Breakout Functionality on Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct) 

The Cisco UCS Fabric Interconnects 9108 100G is equipped with advanced port breakout functionality, which allows network administrators to subdivide a single high-bandwidth port into multiple lower-bandwidth ports. This feature is particularly beneficial for optimizing port utilization, managing cabling complexity, and adapting to various bandwidth requirements. 

Physical Port |  Breakout Options |  Logical Ports After Breakout |  Supported Speeds through breakout cables  
---|---|---|---  
Ethernet 1/1 - Ethernet 1/8 |  4x25G |  Ethernet 1/1/1 to Ethernet 1/8/4 |  Up to 8x100 Gbps  
Fibre Channel 1/1 and 1/2 |  4x8G, 4x16G, 4x32G |  Fibre Channel 1/1/1 to Fibre Channel 1/2/4 |  Up to 8x32Gbps  
  
#### Breakout Port Guidelines

Breakout ports are supported as destinations for traffic monitoring. The following are the guidelines for breakout functionality for Cisco UCS Fabric Interconnects 9108 100G: 

  * Breakout Availability: Breakout functionality is available for physical ports 1-8. 

  * Ethernet Breakout: Ethernet breakout ports can be configured on physical ports 1 through 8, resulting in 32 logical ports. 

  * Fibre Channel Breakout: Fibre Channel breakout ports can be configured on unified ports 1/1 and 1/2, resulting in 8 logical ports. 

  * Port Configurations: Physical Ports 1-8 can be configured as Uplink Ports, FCoE Uplink Ports, FCoE Storage Ports, and Appliance Ports. 

  * Port Conversions: All port conversions support up to 8 standard ports or 8 breakout ports. 

  * Server Ports: Configuration as Server Ports is not supported.

  * Fibre Channel Direct Ports: Direct ports for Fibre Channel are not supported. 

  * Traffic Monitoring: Breakout ports can be utilized as destinations for traffic monitoring. 


### Port Breakout Functionality on Cisco UCS 6536 Fabric Interconnects

The Cisco UCS 6536 36-Port Fabric Interconnect is a One-Rack-Unit (1RU) 1/10/25/40/100 Gigabit Ethernet, FCoE, and Fibre Channel switch offering up to 7.42 Tbps throughput and up to 36 ports. 

Cisco UCS 6536 Fabric Interconnect supports splitting a single 40 Gigabit(G)/100G Quad Small Form-factor Pluggable (QSFP) port into four 10G/25G ports using a supported breakout cable. The switch has 32 40/100-Gbps Ethernet ports and four unified ports that can support 40/100-Gbps Ethernet ports or 16 Fiber Channel (FC) ports after breakout at 8/16/32-Gbps FC speeds. The 16 FC ports after breakout can operate as an FC Uplink or FC storage port. The switch also supports two ports (Port 9 and Port 10) at 1-Gbps speed using QSA, and all 36 ports can breakout for 10 or 25 Gbps Ethernet connectivity. All Ethernet ports can support FCoE. 

Port breakout is supported for Ethernet ports (1-32) and Unified ports (33-36). These 40/100G ports are numbered in a 2-tuple naming convention. The process of changing the configuration from 40G to 10G, or from 100G to 25G is called breakout, and the process of changing the configuration from [4X]10G to 40G or from [4X]25G to 100G is called unconfigure. 

When you break out a 40G port into 10G ports or a 100G port into 25G ports, the resulting ports are numbered using a 3-tuple naming convention. For example, the breakout ports of the second 40-Gigabit Ethernet port are numbered as 1/31/1, 1/31/2, 1/31/3, and 1/31/4. 

FC breakout is supported on ports 36 through 33 when each port is configured with a four-port breakout cable. For example: Four FC breakout ports on the physical port 33 are numbered as 1/33/1, 1/33/2, 1/33/3, and 1/33/4. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Fibre Channel support is only available through the configuration of the Unified Ports (36-33) as Fibre Channel breakout port.

* * *  
  
---|---  
  
The following image shows the rear view of the Cisco UCS 6536 fabric interconnect:

Figure 1. Cisco UCS 6536 Fabric Interconnect Rear View  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540805.jpg)

The following image shows the rear view of the Cisco UCS 6536 fabric interconnect that include Ports and LEDs:

Figure 2. Cisco UCS 6536 Fabric Interconnect Rear View  ![](/c/dam/en/us/td/i/500001-600000/540001-550000/540001-541000/540989.jpg) 1  |  Ports 1-32. Uplink ports are Ethernet port that can operate with the port speed of 10 Gbps/25 Gbps/40 Gbps/100 Gbps. When using a breakout cable, each of these ports can operate as: 4 x 10 Gbps/4x 25 Gbps/1 x 40 Gbps/1 x 100 Gbps Ethernet or FCoE ports.  |  2  |  Ports 33-36. Unified Ports can operate with port speed of 10 Gbps/25 Gbps/ 40 Gbps/100 Gbps Ethernet. or  8 Gbps/16 Gbps/32 Gbps Fibre Channel (FC). When using a breakout cable, each of these ports can operate as 4 x 10 Gbps/4 x 25 Gbps Ethernet or 4x8Gbps/4x16Gbps/4x32Gbps FC ports.   
---|---|---|---  
3  |  Ports 1-36. Uplink ports and Unified ports that can be configured as Ethernet Breakout Port and can operate with the port speed of 10 Gbps/25 Gbps/40 Gbps/100 Gbps.  When using a breakout cable, each of these ports can operate as: 4 x 10 Gbps/4x 25 Gbps/1 x 40 Gbps/1 x 100 Gbps Ethernet or FCoE ports.  |  4 | System environment (fan fault) LED  
5 |  System status (STS) LED |  6 |  Beacon (BCN) LED  
  
#### Breakout Port Guidelines

The following are the guidelines for breakout functionality for Cisco UCS 6536 Fabric Interconnects: 

  * The configurable breakout ports are from port 1-36.

  * You can configure the speed for each breakout port. Each breakout port can be configured at the speed of 4 x 8 Gbps/ 4 x 16 Gbps/ 4 x 32 Gbps for Fibre Channel. 

  * For Fibre Channel breakout, each breakout port can be configured at the speed of 4 x 8 Gbps/ 4 x 16 Gbps/ 4 x 32 Gbps.

  * For Ethernet breakout, each breakout port can be configured at the speed of 4 x 10 Gbps/4 x 25 Gbps.

  * Fibre Channel breakout ports are supported, and Fiber Channel direct ports are not supported.

  * FC breakout port can be configured from 1/36 through 1/33. FC breakout ports (36-33) cannot be configured unless the previous ports are FC breakout ports. Configuration of a single (individual) FC breakout port is also supported. 

  * If the breakout mode for any of the supported Fabric Interconnect ports (1-36) is an Ethernet breakout, the Fabric Interconnect does not lead to a reboot. 

  * If the breakout mode for any of the supported Fabric Interconnect ports (36-33) is a Fibre Channel uplink breakout, the Fabric Interconnect leads to a reboot. 

  * Breakout ports are supported as destinations for traffic monitoring.

  * Ports 1-36 can be configured as Server Port, FCoE Uplink Port, Appliance Port, and Monitor Port.

  * Port 36-33 can be configured also as FC Uplink Port or FC Storage Port when configured as unified port.


### Port Breakout Functionality on Cisco UCS 64108 Fabric Interconnects

#### About Breakout Ports

Cisco UCS 64108 fabric interconnects support splitting a single 40/100G QSFP port into four 10/25G ports using a supported breakout cable. On the UCS 64108 fabric interconnect, by default, there are 12 ports in the 40/100G mode. These are ports 97 to 108. These 40/100G ports are numbered in a 2-tuple naming convention. For example, the second 40G port is numbered as 1/99. The process of changing the configuration from 40G to 10 G, or from 100G to 25G is called breakout, and the process of changing the configuration from [4X]10G to 40G or from [4X]25G to 100G is called unconfigure. These ports can be used as uplink port, appliance port, server port (using FEX), and FCoE storage port. 

When you break out a 40G port into 10G ports or a 100G port into 25G ports, the resulting ports are numbered using a 3-tuple naming convention. For example, the breakout ports of the second 40-Gigabit Ethernet port are numbered as 1/99/1, 1/99/2, 1/99/3, 1/99/4. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCS Manager does not support connection of FEX, chassis, blade, IOM, or adapters (other than VIC adapters) to the uplink ports of Fabric Interconnect. 

* * *  
  
---|---  
  
Starting with Cisco UCS Manager Release 4.2(3b), configuring the Ethernet breakout ports will not lead to Fabric Interconnect reboot. 

The following image shows the rear view of the Cisco UCS 64108 fabric interconnect, and includes the ports that support breakout port functionality: 

Figure 3. Cisco UCS 64108 Fabric Interconnect Rear View ![](/c/dam/en/us/td/i/300001-400000/300001-310000/307001-308000/307644.jpg) 1  |  Ports 1-16. Unified Ports can operate as 10/25 Gbps Ethernet or 8/16/32 Gbps Fibre Channel. FC ports are converted in groups of four.  Unified ports:

  * 10/25 Gbps Ethernet or FCoE
  * 8/16/32 Gbps Fibre Channel

|  2  |  Ports 1-96. Each port can operate as either a 10 Gbps or 25 Gbps Ethernet or FCoE SFP28 port.   
---|---|---|---  
3  |  Uplink Ports 97-108. Each port can operate as either a 40 Gbps or 100 Gbps Ethernet or FCoE port. When using a breakout cable, each of these ports can operate as 4 x 10 Gbps or 4 x 25 Gbps Ethernet or FCoE ports.  Ports 97 - 108 can be used to connect to Ethernet or FCoE uplink ports, and not to UCS server ports. |  4 |  Ports 89-96

  * 10/25 Gbps Ethernet or FCoE
  * 1 Gbps Ethernet

  
5 |  System environment (fan fault) LED |  6 |  System status LED  
7 |  Beacon LED |  |   
  
#### Breakout Port Guidelines

The following are the guidelines for breakout functionality for Cisco UCS 64108 fabric interconnects: 

  * The breakout configurable ports are ports 97-108.

  * You cannot configure the speed for each breakout port. Each breakout port is in auto mode.

  * Breakout ports are not supported as destinations for traffic monitoring.

  * Ports 97-108 at 40/100G can be configured as uplink, FCoE, or appliance port. Ports 97-108 after breakout to 10/25G can be configured as uplink, appliance, FCoE, or for direct-connect rack server connectivity. 


### Port Breakout Functionality on Cisco UCS 6454 Fabric Interconnects

#### About Breakout Ports

Cisco UCS 6454 fabric interconnects support splitting a single 40/100G QSFP port into four 10/25G ports using a supported breakout cable. These ports can be used only as uplink ports connecting to a 10/25G switch. On the UCS 6454 fabric interconnect, by default, there are 6 ports in the 40/100G mode. These are ports 49 to 54. These 40/100G ports are numbered in a 2-tuple naming convention. For example, the second 40G port is numbered as 1/50. The process of changing the configuration from 40G to 10 G, or from 100G to 25G is called breakout, and the process of changing the configuration from [4X]10G to 40G or from [4X]25G to 100G is called unconfigure. 

When you break out a 40G port into 10G ports or a 100G port into 25G ports, the resulting ports are numbered using a 3-tuple naming convention. For example, the breakout ports of the second 40-Gigabit Ethernet port are numbered as 1/50/1, 1/50/2, 1/50/3, 1/50/4. 

Starting with Cisco UCS Manager Release 4.2(3b), Ethernet breakout ports configuration will not lead to Fabric Interconnect reboot. 

Starting with Cisco UCS Manager Release 4.1(3a), you can connect Cisco UCS Rack servers with VIC 1455 and 1457 adapters, to the uplink ports 49 to 54 (40/100 Gbps Ethernet or FCoE) in Cisco UCS 6454 Fabric Interconnects. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCS Manager does not support connection of FEX, chassis, blade, IOM, or adapters (other than VIC 1455 and 1457 adapters) to the uplink ports of Fabric Interconnect. 

* * *  
  
---|---  
  
The following image shows the rear view of the Cisco UCS 6454 fabric interconnect, and includes the ports that support breakout port functionality: 

Figure 4. Cisco UCS 6454 Fabric Interconnect Rear View ![](/c/dam/en/us/td/i/300001-400000/300001-310000/306001-307000/306755.jpg) 1  |  Ports 1-16 (Unified Ports 10/25 Gbps Ethernet or FCoE or 8/16/32 Gbps Fibre Channel) |  2  |  Ports 17-44 (10/25 Gbps Ethernet or FCoE)  
---|---|---|---  
3  |  Ports 45-48 (1/10/25 Gbps Ethernet or FCoE)  |  4 |  Uplink Ports 49-54 (40/100 Gbps Ethernet or FCoE)   
  
#### Breakout Port Guidelines

The following are the guidelines for breakout functionality for Cisco UCS 6454 fabric interconnects: 

  * The breakout configurable ports are ports 49-54.

  * You cannot configure the speed for each breakout port. Each breakout port is in auto mode.

  * In Cisco UCS Manager Release 4.0(2), breakout ports are not supported as destinations for traffic monitoring.

  * Ports 49-54 at 40/100G can be configured as uplink, FCoE, or appliance port. Ports 49-54 after breakout to 10/25G can be configured as uplink, appliance, FCoE, or for direct-connect rack server connectivity. 


### Port Breakout Functionality on Cisco UCS 6300 Series Fabric Interconnects 

#### About Breakout Ports 

Cisco UCS fabric interconnect 6300 series supports splitting a single QSFP port into four 10G ports using a supported breakout cable. By default, there are 32 ports in the 40G mode. These 40G ports are numbered in a 2-tuple naming convention. For example, the second 40G port is numbered as 1/2. The process of changing the configuration from 40G to 10G is called breakout and the process of changing the configuration from [4X]10G to 40G is called unconfigure. 

When you break out a 40G port into 10G ports, the resulting ports are numbered using a 3-tuple naming convention. For example, the breakout ports of the second 40-Gigabit Ethernet port are numbered as 1/2/1, 1/2/2, 1/2/3, 1/2/4. 

The following image shows the front view for the Cisco UCS 6332 series fabric interconnects, and includes the ports that may support breakout port functionality: 

Figure 5. Cisco UCS 6332 Series Fabric Interconnects Front View  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/305001-306000/305235.jpg) 1  |  L1 and L2 high availability ports   
---|---  
2  |  28 X 40G QSFP ports ( 98 X 10G SFP ports)  |  **Note** | 

  * QSA module is required on ports 13–14 
  * A QSFP to 4XSFP breakout cable is required for 10G support. 

  
---|---  
3  |  6 X 40G QSFP ports   
  
The following image shows the front view for the Cisco UCS 6332-16UP series fabric interconnects, and includes the ports that may support breakout port functionality: 

Figure 6. Cisco UCS 6332-16UP Series Fabric Interconnects Front View  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/305001-306000/305236.jpg) 1  |  L1 and L2 high availability ports   
---|---  
2  |  16 X 1/10G SFP (16 X 4/8/16G FC ports)   
3  |  18 X 40G QSFP(72 X 10G SFP+)  |  **Note** | 

  * A QSFP to 4XSFP breakout cable is required for 10G support. 

  
---|---  
4  |  6 X 40G QSFP ports   
  
The following image shows the rear view of the Cisco UCS 6300 series fabric interconnects. 

Figure 7. Cisco UCS 6300 Series Fabric Interconnects Rear View  ![](/c/dam/en/us/td/i/300001-400000/300001-310000/305001-306000/305237.jpg) 1  |  Power supply   
---|---  
2  |  Four fans   
3  |  Power supply   
4  |  Serial ports   
  
#### Breakout Port Constraints 

The following table summarizes the constraints for breakout functionality for Cisco UCS 6300 series fabric interconnects: 

Cisco UCS 6300 Series Fabric Interconnect Series  |  Breakout Configurable Ports  |  Ports without breakout functionality support   
---|---|---  
Cisco UCS 6332  |  1–12, 15–26  |  13–14, 27–32  |  **Note** | 

  * Auto-negotiate behavior is not supported on ports 27–32. 

  
---|---  
Cisco UCS 6332-16UP  |  17–34  |  1–16, 35–40  |  **Note** | 

  * Auto-negotiate behavior is not supported on ports 35–40 

  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

Up to four breakout ports are allowed if QoS jumbo frames are used. 

* * *  
  
---|---  
  
### Configuring Multiple Breakout Ports 

On a UCS 6300 Fabric Interconnect, you can specify a 40 Gigabit Ethernet port and create four 10 Gigabit Ethernet unconfigured breakout ports. On a UCS 6454 Fabric Interconnect, you can specify a 40 or 100 Gigabit Ethernet port and create four 10 or 25 Gigabit Ethernet unconfigured breakout ports. 

On a Cisco UCS Fabric Interconnects 9108 100G and Cisco UCS 6536 Fabric Interconnect, you can specify a 40 or 100 Gigabit Ethernet port and create four 10 or 25 Gigabit Ethernet unconfigured breakout ports. Also, configuring breakout ports on a port do no require Fabric Interconnect reebot.

#### Before you begin

Before configuring a breakout port, view the port status using the show port command. 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A # scope cabling  |  Enters the cabling mode.   
**Step 2** |  UCS-A /cabling # scope fabric {a | b}  |  Enters cabling fabric mode for the specified fabric.   
**Step 3** |  UCS-A /cabling/fabric # create breakout slot-id port-id |  Creates the breakout port on the selected slot and port.   
**Step 4** |  UCS-A /cabling/fabric/breakout* # set breakouttype {10g-4x | 25g-4x}  |  Specifies the type of breakout port on UCS 6454 and UCS 6536 Fabric Interconnects.  
**Step 5** |  UCS-A /cabling/fabric/breakout* # up |  Returns you to fabric mode.  Repeat steps 3 and 5 for each breakout port on UCS 6300 Fabric Interconnect Repeat steps 3, 4, and 5 for each breakout port on Cisco UCS Fabric Interconnects 9108 100G, Cisco UCS 6500 Series, and Cisco UCS 6400 Series Fabric Interconnects.   
**Step 6** |  UCS-A /cabling/fabric/breakout* # commit-buffer |  Commits the transaction to the server.   
  
#### Example

The following example creates breakout ports 1/1 through 1/4 on a UCS 6300 Fabric Interconnect and commits the transaction: 
    
    
    UCS-A# **scope cabling** 
    UCS-A /cabling # **scope fabric a**
    UCS-A /cabling/fabric # **create breakout 1 1**
    Warning: Port breakout create action reboots FI and any existing configurations on 40G port will be erased.!
    UCS-A /cabling/fabric/breakout* # **up**
    UCS-A /cabling/fabric* # **create breakout 1 2**
    Warning: Port breakout create action reboots FI and any existing configurations on 40G port will be erased.!
    UCS-A /cabling/fabric/breakout* # **up**
    UCS-A /cabling/fabric* # **create breakout 1 3**
    Warning: Port breakout create action reboots FI and any existing configurations on 40G port will be erased.!
    UCSM--A /cabling/fabric/breakout* # **up**
    UCSM-shiva-a-A /cabling/fabric* # **create breakout 1 4**
    Warning: Port breakout create action reboots FI and any existing configurations on 40G port will be erased.!
    UCSM--A /cabling/fabric/breakout* # **commit-buffer**
    
    
    

The following example creates breakout ports 1/49 through 1/52 on a UCS 6454 Fabric Interconnect, sets the breakout type, and commits the transaction: 
    
    
    UCS-A# **scope cabling** 
    UCS-A /cabling # **scope fabric a**
    UCS-A /cabling/fabric # **create breakout 1 49**
    UCS-A /cabling/fabric/breakout* # **set breakouttype 10g-4x**
    UCS-A /cabling/fabric/breakout* # **up**
    UCS-A /cabling/fabric* # **create breakout 1 50**
    UCS-A /cabling/fabric/breakout* # **set breakouttype 10g-4x**
    UCS-A /cabling/fabric/breakout* # **up**
    UCS-A /cabling/fabric* # **create breakout 1 51**
    UCS-A /cabling/fabric/breakout* # **set breakouttype 10g-4x**
    UCSM--A /cabling/fabric/breakout* # **up**
    UCSM-shiva-a-A /cabling/fabric* # **create breakout 1 52**
    UCS-A /cabling/fabric/breakout* # **set breakouttype 10g-4x**
    UCS-A /cabling/fabric/breakout* # **commit-buffer**
    

The following example creates breakout ports 1/50 through 1/53 on a UCS 64108 Fabric Interconnect, sets the breakout type, and commits the transaction: 
    
    
    UCS-A# **scope cabling** 
    UCS-A /cabling # **scope fabric a**
    UCS-A /cabling/fabric # **create breakout 1 50**
    UCS-A /cabling/fabric/breakout* # **set breakouttype 10g-4x**
    UCS-A /cabling/fabric/breakout* # **up**
    UCS-A /cabling/fabric* # **create breakout 1 51**
    UCS-A /cabling/fabric/breakout* # **set breakouttype 10g-4x**
    UCS-A /cabling/fabric/breakout* # **up**
    UCS-A /cabling/fabric* # **create breakout 1 52**
    UCS-A /cabling/fabric/breakout* # **set breakouttype 10g-4x**
    UCSM--A /cabling/fabric/breakout* # **up**
    UCSM-shiva-a-A /cabling/fabric* # **create breakout 1 53**
    UCS-A /cabling/fabric/breakout* # **set breakouttype 10g-4x**
    UCS-A /cabling/fabric/breakout* # **commit-buffer**
    

The following example creates breakout ports 1/17 through 1/20 on a UCS 6536 Fabric Interconnect, sets the breakout type, and commits the transaction: 
    
    
    UCS-A# **scope cabling** 
    UCS-A /cabling # **scope fabric a**
    UCS-A /cabling/fabric # **create breakout 1 17**
    UCS-A /cabling/fabric/breakout* # **set breakouttype 25g-4x**
    UCS-A /cabling/fabric/breakout* # **up**
    UCS-A /cabling/fabric* # **create breakout 1 18**
    UCS-A /cabling/fabric/breakout* # **set breakouttype 25g-4x**
    UCS-A /cabling/fabric/breakout* # **up**
    UCS-A /cabling/fabric* # **create breakout 1 19**
    UCS-A /cabling/fabric/breakout* # **set breakouttype 25g-4x**
    UCSM--A /cabling/fabric/breakout* # **up**
    UCSM-shiva-a-A /cabling/fabric* # **create breakout 1 20**
    UCS-A /cabling/fabric/breakout* # **set breakouttype 25g-4x**
    UCS-A /cabling/fabric/breakout* # **commit-buffer**
    

The following example creates breakout ports 1/1 through 1/4 Cisco UCS Fabric Interconnects 9108 100G and commits the transaction: 
    
    
    UCS-A# **scope cabling** 
    UCS-A /cabling # **scope fabric a**
    UCS-A /cabling/fabric # create breakout 1 1
    UCS-A /cabling/fabric/breakout* # set breakouttype 25g-4x
    UCS-A /cabling/fabric/breakout* # up
    UCS-A /cabling/fabric* # create breakout 1 2
    UCS-A /cabling/fabric/breakout* # set breakouttype 25g-4x
    UCS-A /cabling/fabric/breakout* # up
    UCS-A /cabling/fabric* # create breakout 1 3
    UCS-A /cabling/fabric/breakout* # set breakouttype 25g-4x
    UCSM--A /cabling/fabric/breakout* # up
    UCSM-shiva-a-A /cabling/fabric* # create breakout 1 4
    UCS-A /cabling/fabric/breakout* # set breakouttype 25g-4x
    UCS-A /cabling/fabric/breakout* # commit-buffer
    
    
    
    

#### What to do next

Verify that you created breakout ports on the fabric interconnect and on the NXOS switch. On the fabric interconnect use the show breakout command in cabling fabric mode for the specified fabric. In NXOS, use the show interface brief  command. 

### Configuring a Breakout Ethernet Uplink Port 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope eth-uplink |  Enters Ethernet uplink mode.   
**Step 2** |  UCS-A /eth-uplink #  scope fabric{a | b}  |  Enters Ethernet uplink fabric mode for the specified fabric.   
**Step 3** |  UCS-A /eth-uplink/fabric #  create aggr-interface slot-numaggregate port-num |  Creates the interface for the specified aggregate (main) Ethernet uplink port.   
**Step 4** |  UCS-A /eth-uplink/fabric/aggr-interface* #  create br-interface breakout-port-num |  Creates an interface for the specified breakout Ethernet uplink port.   
**Step 5** |  UCS-A /eth-uplink/fabric/aggr-interface/br-interface #  commit-buffer  |  Commits the transaction to the server.   
  
#### Example

The following example shows how to create an interface for breakout Ethernet uplink port 1 of the aggregate port 21 on slot 1 of fabric A: 
    
    
    UCS-A# **scope eth-uplink**
    UCS-A /eth-uplink # **scope fabric a**
    UCS-A /eth-uplink/fabric # **enter aggr-interface 1 21**
    UCS-A /eth-uplink/fabric/aggr-interface # **create br-interface 1**
    UCS-A /eth-uplink/fabric/aggr-interface/br-interface*# **commit-buffer**
    
    

The following example shows how to create interfaces for breakout Ethernet uplink ports 1-4 of the aggregate port 49 on slot 1 of fabric A on a UCS 6454 fabric interconnect, and commit the transaction: 
    
    
    UCS-A# **scope eth-uplink**
    UCS-A /eth-uplink # **scope fabric a**
    UCS-A /eth-uplink/fabric # **create aggr-interface 1 49**
    UCS-A /eth-uplink/fabric/aggr-interface* # **create br-interface 1**
    UCS-A /eth-uplink/fabric/aggr-interface/br-interface* # **up**
    UCS-A /eth-uplink/fabric/aggr-interface* # **create br-interface 2**
    UCS-A /eth-uplink/fabric/aggr-interface/br-interface* # **up**
    UCS-A /eth-uplink/fabric/aggr-interface* # **create br-interface 3**
    UCS-A /eth-uplink/fabric/aggr-interface/br-interface* # **up**
    UCS-A /eth-uplink/fabric/aggr-interface* # **create br-interface 4**
    UCS-A /eth-uplink/fabric/aggr-interface/br-interface* # **up**
    UCS-A /eth-uplink/fabric/aggr-interface* # **commit-buffer**
    UCS-A /eth-uplink/fabric/aggr-interface # 
    

The following example shows the breakout configuration for ports 1/49/1 to 1/49/4 of fabric A on a UCS 6454 fabric interconnect: 
    
    
    UCS-A# **scope fabric-interconnect a** 
    UCS-A /fabric-interconnect # **show port**
    Ether Port: 
    Slot  Aggr       Port  Port Oper State  Mac                  Role    Xcvr 
    ----- ---------- ----- ---------------- -------------------- ------- ---- 
    1     49         1     Sfp Not Present  8C:60:4F:BC:C4:D4    Unknown N/A 
    1     49         2     Sfp Not Present  8C:60:4F:BC:C4:D5    Unknown N/A 
    1     49         3     Sfp Not Present  8C:60:4F:BC:C4:D6    Unknown N/A 
    1     49         4     Sfp Not Present  8C:60:4F:BC:C4:D7    Unknown N/A 
    

### Configuring a Breakout Ethernet Uplink Port Channel Member 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope eth-uplink |  Enters Ethernet uplink mode.   
**Step 2** |  UCS-A# /eth-uplink # scope fabric{a | b}  |  Enters Ethernet uplink mode for the specified fabric.   
**Step 3** |  UCS-A# /eth-uplink/fabric # scope fcoe-port-channel fcoe-port-channel |  Enters port channel for the specified FCoE uplink port.   
**Step 4** |  UCS-A /eth-uplink/fabric/port-channe/fcoe-port-channel # enter aggr-interface slot-id port-id |  Enters the interface for the specified aggregate(main) FCoE uplink port.   
**Step 5** |  UCS-A /eth-uplink/fabric/port-channel/member-aggr-port # create br-member-portbreakout-port-num |  Creates the FCoE uplink port channel member.   
**Step 6** |  UCS-A /eth-uplink/fabric/port-channel/member-aggr-port/br-member-port # commit-buffer 

#### Example:

The following example creates an Ethernet uplink port channel member for an Ethernet port on port 2, and commits the transaction: 
    
    
    UCS-A# **scope eth-storage** 
    UCS-A /eth-uplink # **scope fabric a**
    UCS-A /eth-uplink/fabric # **scope fcoe-port-channel 51**
    UCS-A /eth-uplink/fabric/port-channel/member-aggr-port # **create br-member-port 2**
    UCS-A /eth-uplink/fabric/port-channel/member-aggr-port/br-member-port* # **commit-buffer**
    

|  Commits the transaction to the server.   
  
### Configuring Ethernet Uplink Breakout Port as a Pin Group Target 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope eth-uplink |  Enters Ethernet uplink mode.   
**Step 2** |  UCS-A# /eth-uplink/pin-group #  enter pin-group pin-group-name |  Enters the pin group with the specified name.   
**Step 3** |  UCS-A# /et h-uplink/pin-group # set target{a|b} breakout-portslot-numaggregate-port-numbreakout-port-num |  Sets the selected target as the breakout port.   
**Step 4** |  UCS-A # /eth-uplink/pin-group #  commit-buffer

#### Example:

The following example sets the pin group target to breakout port 2 of the aggregate port 1 on slot 1, on fabric A , and commits the transaction: 
    
    
    UCS-A# scope **eth-uplink**
    UCS-A /eth-uplink # **enter pin-group test**
    UCS-A /eth-uplink/pin-group # **set target a breakout-port 1 1 2**
    UCS-A /eth-uplink/pin-group* # **commit-buffer**
     
    

|  Commits the transaction to the server.   
  
### Configuring Breakout Appliance Ports

You can follow the below steps to configure appliance breakout ports for both Cisco UCS Fabric Interconnects 9108 100G, Cisco UCS 6500 Series Fabric Interconnect, , and Cisco UCS 6400 Series Fabric Interconnect: 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope eth-storage |  Enters Ethernet storage mode.   
**Step 2** |  UCS-A# /eth-storage # scope fabric{a | b}  |  Enters Ethernet storage mode for the specified fabric.   
**Step 3** |  UCS-A# /eth-storage/fabric # enter aggr-interface slot-numaggregate-port-num |  Enters the interface for the specified aggregate(main) appliance port.   
**Step 4** |  UCS-A# /eth-storage/fabric/port-channel/member-aggr-port #  create br -interfacebreakout-port-num |  Creates an interface for the specified breakout appliance port.   
**Step 5** |  UCS-A# /eth-storage/fabric/port-channel/member-aggr-port/br-member-port #  commit-buffer

#### Example:

The following example creates an interface for an appliance port 1 of the aggregate port 20 on slot 1 of fabric B, and commits the transaction: 
    
    
    UCS-A# **scope eth-storage** 
    UCS-A /eth-storage # **scope fabric a** 
    UCS-A /eth-storage/fabric # **enter aggr-interface 1 20**
    UCS-A /eth-storage/fabric/aggr-interface # **create br-interface 1**
    UCS-A /eth-storage/fabric/aggr-interface/br-interface* # **commit-buffer** 
    
    
    
    
    

#### Example:

|  **Note** |  If the port is only connected to 100G SFP which is broken out in 25x4 breakout port then when creating an appliance port, the default speed for a breakout port would be Auto.   
---|---  
Commits the transaction to the server.   
  
### Configuring a Breakout Appliance Port Channel Member 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope eth-storage |  Enters Ethernet storage mode.   
**Step 2** |  UCS-A# /eth-storage # scope fabric{a | b}  |  Enters Ethernet storage mode for the specified fabric.   
**Step 3** |  UCS-A# /eth-storage # scope port-channelport-channel-num |  Enters Ethernet storage mode for the specified port-channel.   
**Step 4** |  UCS-A# /eth-storage/fabric # enter aggr-interface slot-numaggregate-port-num |  Enters the interface for the specified aggregate(main) appliance port.   
**Step 5** |  UCS-A /eth-storage/fabric/port-channel # enter member-aggr-port  slot-id port-id |  Enters the appliance port channel member port.   
**Step 6** |  UCS-A /eth-storage/fabric/port-channel/member-aggr-port # create br-member-portbreakout-port-num |  Creates the appliance port channel member.   
**Step 7** |  UCS-A /eth-storage/fabric/port-channel/member-aggr-port/br-member-port # commit-buffer

#### Example:

The following example creates an appliance port channel member for an appliance port 2, and commits the transaction: 
    
    
    UCS-A# **scope eth-storage** 
    UCS-A /eth-storage # **scope fabric a**
    UCS-A /eth-storage/fabric # **scope port-channel 21**
    UCS-A /eth-storage/fabric/port-channel # **enter member-aggr-port 1 2**
    UCS-A /eth-storage/fabric/port-channel/member-aggr-port # **create br-member-port 2**
    UCS-A /eth-storage/fabric/port-channel/member-aggr-port/br-member-port* # **commit-buffer**
    

|  Commits the transaction to the server.   
  
### Configuring Breakout FCoE Storage Ports 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope fc-storage |  Enters Fibre Channel storage mode.   
**Step 2** |  UCS-A# /fc-storage scope fabric{a | b |  Enters Fibre Channel storage mode for the specified fabric.   
**Step 3** |  UCS-A# /fc-storage/fabric enter aggr-interface slot-numaggregate port-num |  Enter the interface for the specified aggregate(main) Fibre Channel storage port.   
**Step 4** |  UCS-A# /fc-storage/fabric/aggr-interface #  create br-interface br-fcoe breakout-port-num |  Creates an interface for the specified breakout Fibre Channel storage port.   
**Step 5** |  UCS-A# /fc-storage/fabric/aggr-interface/br-interface/br-fcoe #  commit-buffer 

#### Example:

The following example creates an interface for a breakout Fibre Channel storage port 1 of the aggregate port 21 on slot 1 of fabric a, and commits the transaction: 
    
    
    UCS-A# **scope fc-storage**
    UCS-A /fc-storage # **scope fabric a**
    UCS-A /fc-storage/fabric # **enter aggr-interface 1 21**
    UCS-A /fc-storage/fabric/aggr-interface # **create br-interface 1**
    UCS-A /eth-uplink/fabric/aggr-interface/br-interface/br-fcoe **# commit-buffer**
    
    

|  Commits the transaction to the server.   
  
### Configuring a Breakout FCoE Uplink Port 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope fc-uplink |  Enters FC Uplink mode.   
**Step 2** |  UCS-A# /fc-uplink scope fabric{a | b |  Enters FC - Uplink mode for the specific fabric.   
**Step 3** |  UCS-A# /fc-uplink/fabric enter aggr-interface slot-numaggregate port-num |  Enters interface for the specified aggregate(main) FCoE uplink port.   
**Step 4** |  UCS-A# /fc-uplink/fabric/aggr-interface #  create br-fcoeinterface breakout-port-num |  Creates an interface for the specified breakout FCoE uplink port.   
**Step 5** |  UCS-A# /fc-uplink/fabric/aggr-interface/ br-fcoeinterface #  commit-buffer 

#### Example:

The following example shows how to create an interface for breakout FCoE uplink port 1 of the aggregate port 20 on slot 1 of fabric A: 
    
    
    UCS-A# **scope eth-uplink**
    UCS-A /fc-uplink # **scope fabric a**
    UCS-A /fc-uplink/fabric # **enter aggr-interface 1 20**
    UCS-A /fc-uplink/fabric/aggr-interface # **create br-fcoeinterface 1**
    UCS-A /fc-uplink/fabric/aggr-interface/br-fcoeinterface**# commit-buffer**
    
    

|  Commits the transaction to the server.   
  
### Configuring an FCoE Port Channel Member 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope fc-uplink |  Enters Ethernet storage mode.   
**Step 2** |  UCS-A# /fc-uplink # scope fabric{a | b}  |   
**Step 3** |  UCS-A# /fc-uplink/fabric # scope fcoe-port-channel fcoe-port-num |   
**Step 4** |  UCS-A /fc-uplink/fabric/port-channel # enter aggr-interface slot-num port-numaggregate-port-num |  Enters the FCoE port channel member port.   
**Step 5** |  UCS-A /fc-uplink/fabric/port-channel/member-aggr-port # create br-member-portbreakout-port-num |  Creates the FCoE port channel member for the specified breakout port.   
**Step 6** |  UCS-A /fc-uplink/fabric/port-channel/member-aggr-port/br-member-port # commit-buffer

#### Example:

The following example creates a breakout FCoE port channel member port 4 on aggregate port 21, and commits the transaction: 
    
    
    UCS-A# **scope eth-storage** 
    UCS-A /fc-uplink # **scope fabric a**
    UCS-A /fc-uplink/fabric # **scope port-channel 51**
    UCS-A /fc-uplink/fabric/port-channel # **enter member-aggr-port 1 21**
    UCS-A /fc-uplink/fabric/port-channel/member-aggr-port # **create br-member-port 4**
    UCS-A /fc-uplink/fabric/port-channel/member-aggr-port/br-member-port* # **commit-buffer**
    

|  Commits the transaction to the server.   
  
### Configuring a Breakout VLAN Member Port 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  USA-A# scope eth-uplink |  Enters Ethernet uplink mode for the specified fabric.   
**Step 2** |  USA-A /eth-uplink # scope vlan  id |  Enters VLAN mode.   
**Step 3** |  USA-A /eth-uplink/vlan # enter member-aggr-port {a|b} slot-id port id |  Enters an interface for the specified fabric, main aggregate port, and subport. breakout VLAN member port.   
**Step 4** |  USA-A /eth-uplink/vlan/member-aggr-port # create br-member-port breakout-port-name |  Creates an interface for the specified breakout VLAN member port.   
**Step 5** |  USA-A /eth-uplink/vlan/member-aggr-port/br-member-port # commit-buffer 

#### Example:

The following example creates an interface for a VLAN member on the aggregate port 4 on slot 1 of breakout Ethernet uplink port 1, and commits the transaction: 
    
    
    USA-A# **scope eth-uplink** 
    USA-A /eth-uplink # **scope vlan id**
    USA-A /eth-uplink/vlan # **enter member-aggr-port a 1 1**
    USA-A /eth-uplink/vlan/member-aggr-port* # **create br-member-port 4**
    USA-A /eth-uplink/vlan/member-aggr-port/br-member-port* # **commit-buffer**  
     

|  Commits the transaction to the server.   
  
#### What to do next

Verify that you created the breakout VLAN Member port using the show command. 

### Modifying a Breakout Port 

The following table describes how to modify the supported breakout ports. 

Breakout Port Type  |  Scope  |  CLI Location From Which To Modify  |  Modify Options   
---|---|---|---  
Ethernet Uplink  |  eth-uplink  |  UCS-A eth-uplink/fabric/aggr-interface/br-interface # create |  mon-src — Creates a monitor source session.   
UCS-A /eth-uplink/fabric/aggr-interface/br-interface # set |  eth-link-profile — Sets the Ethernet Link profile name.  flow-control-policy  — Sets the flow control policy that configures the receive and send flow control parameters for the LAN and Ethernet uplink ports.  speed — Sets the speed for an Ethernet uplink port.  user-label — Assigns an identifying label to the Ethernet Uplink port.   
UCS-A /eth-uplink/fabric/aggr-interface/br-interface #  |  disable — Disables the aggregate interface for the Ethernet Uplink breakout port.  enable — Enables the aggregate interface for the Ethernet Uplink breakout port.   
Ethernet Uplink port-channel member  |  fc-storage  |  UCS-A /eth-uplink/fabric/port-channel/aggr-interface/br-member-port # set |  eth-link-profile — Sets the Ethernet Link profile name.   
UCS-A /eth-uplink/fabric/port-channel/aggr-interface/br-member-port #  |  disable — Disables the aggregate interface for the breakout Ethernet Uplink port-channel member.  enable — Enables the aggregate interface for the breakout Ethernet Uplink port-channel member.   
FCoE Uplink  |  fc-uplink  |  UCS-A /fc-uplink/fabric/aggr-interface/br-fcoeinterface # create |  mon-src — Creates a monitor source session.   
UCS-A /fc-uplink/fabric/aggr-interface/br-fcoeinterface # set |  eth-link-profile — Sets the Ethernet Link profile name.  user-label  — Assigns an identifying label to the FCoE uplink breakout port.   
UCS-A /fc-uplink/fabric/aggr-interface/br-fcoeinterface #  |  disable —Disables the aggregate interface for the FCoE uplink breakout port.  enable — Enables the aggregate interface for the FCoE uplink breakout port.   
FCoE Uplink port-channel member  |  eth-uplink  |  UCS-A /fc-uplink/fabric/fcoe-port-channel/aggr-interface/br-member-port # set |  eth-link-profile — Sets the Ethernet Link profile name.   
A /fc-uplink/fabric/fcoe-port-channel/aggr-interface/br-member-port #  |  disable — Disables the aggregate interface for the breakout FCoE uplink port-channel member.  enable — Enables the aggregate interface for the breakout FCoE uplink port-channel member.   
FCoE Storage port  |  fc-storage  |  UCS-A fc-storage/fabric/aggr-interface/br-fcoe # create |  mon-src — Creates a monitor source session.   
UCS-A /fc-storage/fabric/aggr-interface/br-fcoe # set |  user-label — Assigns an identifying label to the server.   
UCS-A /fc-storage/fabric/aggr-interface/br-fcoe #  |  disable — Disables the aggregate interface for the breakout FCoE Storage port  enable — Enables the aggregate interface for the breakout FCoE Storage port.   
Appliance Port  |  eth-storage  |  UCS-A /eth-storage/fabric/aggr-interface/br-interface # set |  adminspeed — Sets the speed for a fabric interface.  flowctrlpolicy —Sets the flow control policy that configures the receive and send flow control parameters for the appliance ports.  nw-control-policy  — Creates a network control policy for the appliance port.  pingroupname — Sets the pin group name for the fabric interface.  portmode — Sets the appliance port mode.  prio — Sets the QoS (Quality of Service) priority level.  user-label — Assigns an identifying label to the appliance port.   
UCS-A /eth-storage/fabric/aggr-interface/br-interface # create |  eth-target — Creates the Ethernet target endpoint.  mon-src — Creates a monitor source session.   
UCS-A /eth-storage/fabric/aggr-interface/br-interface #  |  disable — Disables the aggregate interface for the appliance breakout port.  enable —Enables the aggregate interface for the appliance breakout port.   
Appliance port-channel member  |  eth-storage |  UCS-A /eth-storage/fabric/port-channel/member-aggr-port #  |  disable — Disables the aggregate interface for the breakout appliance port-channel member.  enable —Enables the aggregate interface for the breakout appliance port-channel member.   
VLAN Member  |  eth-uplink  |  A /eth-uplink/vlan/member-aggr-port/br-member-port # set |  isnative — Marks a member-port as a native VLAN.   
Pin Group - Pin Target  |  eth-uplink  |  N/A  |  N/A   
SPAN (Traffic Monitoring) Destination Port  |  eth-traffic-mon  |  A /eth-traffic-mon/fabric/eth-mon-session/dest-aggr-interface/br-dest-interface # set |  speed — Sets the speed for the SPAN (Traffic Monitoring) destination port.   
  
#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope eth-uplink .  |  Enters Ethernet uplink mode.   
**Step 2** |  UCS-A /eth-uplink # scope fabric  {a | b} .  |  Enters Ethernet uplink fabric mode for the specified fabric.   
**Step 3** |  UCS-A /eth-uplink/fabric # scope aggr-interface port-number port-id .  |  Enters the interface for the specified aggregate(main) Ethernet uplink port.   
**Step 4** |  UCS-A /eth-uplink/fabric/aggr-interface # scope br-interface port-id .  |  Enters the breakout Ethernet port for the specified port number.   
**Step 5** |  UCS-A /eth-uplink/fabric/aggr-interface/br-interface # create mon-src . 

#### Example:

The following example shows how to modify a Ethernet uplink port as a monitor source in breakout port 1 of the aggregate (main) interface in port 1 with an ID of 21. 
    
    
    UCS-A# **scope eth-uplink**
    UCS-A /eth-uplink # **scope fabric a**
    UCS-A /eth-uplink/fabric # **scope aggr-interface 1 21**
    UCS-A /eth-uplink/fabric/aggr-interface # **scope br-interface 1**
    UCS-A /eth-uplink/fabric/aggr-interface/br-interface # **create** 
    	UCS-A /eth-uplink/fabric/aggr-interface/br-interface # **create mon-src**
    

|  Modifies the interface as a monitoring source.   
  
#### Modifying the Breakout Ethernet Uplink Port Speed and User Label 
    
    
    pranspat-3gfi-A /eth-uplink/fabric/aggr-interface/br-interface # set      
    	eth-link-profile     Ethernet Link Profile name   
    	flow-control-policy  flow control policy   
    	speed                 Speed   
    	user-label           User Label 
    
    
    
    pranspat-3gfi-A /eth-uplink/fabric/aggr-interface/br-interface # 
    	disable      Disables services   
    	enable       Enables services
    

###  Un-configuring Breakout Ports 

If you have a breakout on port 2 in slot 1, you can un-configure the breakout port. 

#### Before you begin

You can use the  show port  command to list the ports for the Fabric Interconnect (FI), and select the port that you want to breakout. 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# / fabric-interconnect #  show port 

#### Example:

The following example lists the ports. 
    
    
    Slot  Aggr Port  Port  Oper State       Mac                  Role    Xcvr
    ----- ---------- ----- ---------------- -------------------- ------- ----
        1          0     1 Link Down        84:B8:02:CA:37:56    Network 1000base T
        1          2     1 Sfp Not Present  84:B8:02:CA:37:57    Unknown N/A
        1          2     2 Sfp Not Present  84:B8:02:CA:37:57    Unknown N/A
        1          2     3 Sfp Not Present  84:B8:02:CA:37:57    Unknown N/A
        1          2     4 Sfp Not Present  84:B8:02:CA:37:57    Unknown N/A
        1          0     3 Sfp Not Present  84:B8:02:CA:37:58    Unknown N/A
    
    

|  Displays the ports for the Fabric Interconnect.   
**Step 2** |  UCS-A#  scope cabling  |  Enters the cabling mode.   
**Step 3** |  UCS-A# /cabling # scope fabric {a | b }  |  Specifies fabric a or b.   
**Step 4** |  UCS-A #/ cabling # delete breakout  {1 | 2 |   
**Step 5** |  UCS-A /cabling/fabric/breakout* #  commit .  |  Commits the transaction to the system configuration.   
  
#### What to do next

You can use the  show port  to view the unconfigured breakouts ports. 

### Deleting Breakout Ports 

You can delete 10 Gig Ethernet breakout ports. Use the br-interface or br-member-port  scopes to select breakout sub-ports 1-4. You must provide the sub-port id for this scope. For example, scope br-interface sub_port_id . 

The example described in this topic describes how to delete a breakout Ethernet uplink port. The following table describes how to delete the supported Ethernet breakout ports. 

Breakout Port Type  |  Scope  |  CLI Location From Which To Delete   
---|---|---  
Ethernet Uplink  |  eth-uplink  |  UCS-A /eth-uplink/fabric/aggr-interface # delete br-interface number  
Ethernet Uplink port-channel member  |  eth-uplink  |  UCS-A /eth-uplink/fabric/port-channel/aggr-interface # delete br-member-port number  
FCoE Uplink  |  fc-uplink  |  UCS-A /fc-uplink/fabric/aggr-interface # delete br-fcoeinterface number  
FCoE Uplink port-channel member  |  eth-uplink  |  UCS-A /fc-uplink/fabric/fcoe-port-channel/aggr-interface # delete br-member-port number  
FCoE Storage port  |  fc-storage  |  UCS-A /fc-storage/fabric/aggr-interface # delete br-interface br-fcoe number  
Appliance Port  |  eth-storage  |  UCS--A /eth-storage/fabric/port-channel/member-aggr-port # delete br-member-port number  
Appliance port-channel member  |  eth-storage  |  UCS-A /eth-storage/fabric/aggr-interface # delete br-interface number  
VLAN Member  |  eth-uplink  |  UCS-A /eth-uplink/vlan/member-aggr-port # delete br-member-port number  
Pin Group - Pin Target  |  eth-uplink  |  UCS-A /eth-uplink/pin-group # delete target number  
SPAN (Traffic Monitoring) Destination Port  |  eth-traffic-mon  |  UCS-A /eth-traffic-mon/fabric/eth-mon-session/dest-aggr-interface # delete br-dest-interface   
  
#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope eth-uplink  |  Enters the Ethernet uplink mode.   
**Step 2** |  UCS-A# /eth-storage #  scope fabric{a | b}  |  Enters Ethernet storage mode for the specified fabric.   
**Step 3** |  UCS-A /eth-uplink/fabric # scope port-channel  number |  Enters Ethernet uplink fabric port channel mode for the specified port channel.   
**Step 4** |  UCS-A /eth-uplink/fabric/port-channel/aggr-interface # delete br-member-port  number |  Deletes the specified breakout port.   
**Step 5** |  UCS-A /eth-uplink/fabric/port-channel/aggr-interface # commit-buffer

#### Example:

This example deletes an Ethernet Uplink port-channel member in breakout port 1 of the aggregate (main) interface port 1 slot 1. 
    
    
    UCS-A# **scope eth-uplink** 
    UCS-A /eth-uplink # **scope fabric a**
    UCS-A /eth-uplink/fabric # **scope port-channel 1**
    UCS-A /eth-uplink/fabric/port-channel # **enter aggr-interface 1 1**
    UCS-A /eth-uplink/fabric/port-channel/aggr-interface # **delete br-member-port 1**
    UCS-A /eth-uplink/fabric/port-channel/aggr-interface* # **commit-buffer**

|  Commits the transaction to the server.   
  
#### What to do next

Verify that you deleted the specified breakout port using the show command. 

### Cisco UCS Mini Scalability Ports 

The Cisco UCS 6324 Fabric Interconnect contains a scalability port as well as four unified ports. The scalability port is a 40GB QSFP+ breakout port that, with proper cabling, can support four 1G or 10G SFP+ ports. The scalability ports can be used as a licensed server port for supported Cisco UCS rack servers, an appliance port, or a FCoE port. 

In the Cisco UCS Manager GUI, the scalability port is displayed as Scalability Port 5 below the Ethernet Ports node. The individual breakout ports are displayed as Port 1 through Port 4. 

In the Cisco UCS Manager CLI, the scalability port is not displayed, but the individual breakout ports are displayed as Br-Eth1/5/1 through Br-Eth1/5/4 . 

#### Configuring Scalability Ports

To configure ports, port channel members or SPAN members on the scalability port, scope into the scalability port first, then follow the steps for a standard unified port. 

##### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope eth-server |  Enters Ethernet server mode.   
**Step 2** |  UCS-A /eth-server #  scope fabric {a | b}  |  Enters Ethernet server fabric mode for the specified fabric.   
**Step 3** |  UCS-A /eth-server/fabric #  scope aggr-interface slot-num port-num |  Enters ethernet server fabric aggregate interface mode for the scalability port.   
**Step 4** |  UCS-A /eth-server/fabric/aggr-interface #  show interface |  Displays the interfaces on the scalability port.   
**Step 5** |  UCS-A /eth-server/fabric/aggr-interface #  create interface slot-num port-num |  Creates an interface for the specified Ethernet server port.   
**Step 6** |  UCS-A /eth-server/fabric/aggr-interface #  commit-buffer |  Commits the transaction to the system configuration.   
  
##### Example

The following example shows how to create an interface for Ethernet server port 3 on the fabric A scalability port and commit the transaction: 
    
    
    UCS-A# **scope eth-server**
    UCS-A /eth-server # **scope fabric a**
    UCS-A /eth-server/fabric # **scope aggr-interface 1 5**
    UCS-A /eth-server/fabric/aggr-interface # **show interface**
    Interface:
    
    Slot Id Aggr-Port ID Port Id  Admin State Oper State    State Reason
    ------- ------------ -------- ----------- ------------- ------------
          1            5        1 Enabled     Up
          1            5        2 Enabled     Up     
          1            5        3 Enabled     Admin Down    Administratively Down
          1            5        4 Enabled     Admin Down    Administratively Down
    
    UCS-A /eth-server/fabric/aggr-interface # **create interface 1 3**
    UCS-A /eth-server/fabric/aggr-interface* # **commit-buffer**
    UCS-A /eth-server/fabric/aggr-interface # 
    

### Beacon LEDs for Unified Ports 

Each port fabric interconnect has a corresponding beacon LED. When the Beacon LED property is configured, the beacon LEDs illuminate, showing you which ports are configured in a given port mode. 

You can configure the Beacon LED property to show you which ports are grouped in one port mode: either Ethernet or Fibre Channel. By default, the Beacon LED property is set to Off. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For unified ports on the expansion module, you can reset the Beacon LED property to the default value of Off during expansion module reboot. 

* * *  
  
---|---  
  
#### Configuring the Beacon LEDs for Unified Ports

Complete the following task for each module for which you want to configure beacon LEDs. 

##### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope fabric-interconnect` `{a | b}  |  Enters fabric interconnect mode for the specified fabric.  
**Step 2** |  UCS-A /fabric # scope card` `slot-id |  Enters card mode for the specified fixed or expansion module.  
**Step 3** |  UCS-A /fabric/card # scope beacon-led |  Enters beacon LED mode.  
**Step 4** |  UCS-A /fabric/card/beacon-led # set admin-state` `{eth | fc | off}  |  Specifies which port mode is represented by illuminated beacon LED lights.

eth
     All of the Unified Ports configured in Ethernet mode illuminate.

fc
     All of the Unified Ports configured in Fibre Channel mode illuminate.

off
     Beacon LED lights for all ports on the module are turned off.  
**Step 5** |  UCS-A /fabric/card/beacon-led # commit-buffer |  Commits the transaction to the system configuration.  
  
##### Example

The following example illuminates all of the beacon lights for Unified Ports in Ethernet port mode and commits the transaction:
    
    
    UCS-A# **scope fabric-interconnect a**
    UCS-A /fabric # **scope card 1**
    UCS-A /fabric/card # **scope beacon-led**
    UCS-A /fabric/card/beacon-led # **set admin-state eth**
    UCS-A /fabric/card/beacon-led* # **commit-buffer**
    UCS-A /fabric/card/beacon-led #

---

## Page 16: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Network-Mgmt/4-3/m-cli-macsec-4-3.html

## About MACsec

MACsec is an IEEE 802.1AE standards-based Layer 2 hop-by-hop encryption that provides data confidentiality and integrity for media access independent protocols. 

MACsec provides MAC-layer encryption over wired networks by using out-of-band methods for encryption keying. The MACsec Key Agreement (MKA) Protocol provides the required session keys and manages the required encryption keys. 

MACsec encrypts the entire data except for the Source and Destination MAC addresses of an Ethernet packet. It offers the following capabilities: 

  * Provides line rate encryption.

  * Ensures data confidentiality by providing strong encryption at Layer 2. 

  * Provides integrity checking to help ensure that data cannot be modified in transit. 

  * Key Lifetime and Hitless Key Rollover

  * Fallback Key


### Key Lifetime and Hitless Key Rollover

A MACsec keychain can have multiple pre-shared keys (PSKs), each configured with a key ID and an optional lifetime. A key lifetime specifies at which time the key activates and expires. In the absence of a lifetime configuration, the default lifetime is unlimited. When a lifetime is configured, MKA rolls over to the next configured pre-shared key in the keychain after the lifetime is expired. The time zone of the key can be local or UTC. The default time zone is UTC. 

To configure a MACsec keychain, see Creating a MACsec Keychain

A key can roll over to a second key within the same keychain by configuring the second key (in the keychain) and configuring a lifetime for the first key. When the lifetime of the first key expires, it automatically rolls over to the next key in the list. If the same key is configured on both sides of the link at the same time, then the key rollover is hitless (that is, the key rolls over without traffic interruption). 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The lifetime of the keys are overlapped to achieve hitless key rollover.

* * *  
  
---|---  
  
### Fallback Key

A MACsec session can fail due to a key/key ID (CKN) mismatch or a finite key duration between the Fabric Interconnect and the peer. If a MACsec session fails, a fallback session can take over if a fallback key is configured. A fallback session prevents downtime due to primary session failure and allows a user time to fix the key issue causing the failure. A fallback key also provides a backup session if the primary session fails to start. This feature is optional. 

For more information, see Creating a MACsec Keychain. 

---

## Page 17: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Network-Mgmt/4-3/b_CLI_UCSM_Network_Management_Guide_4_1_chapter_011.html

## Fabric Interconnect Overview 

The fabric interconnect is the core component of Cisco UCS. The Cisco UCS Fabric Interconnects provide uplink access to LAN, SAN, and out-of-band management segment. Cisco UCS infrastructure management is through the embedded management software, Cisco UCS Manager, for both hardware and software management. The Cisco UCS Fabric Interconnects are Top-of-Rack devices, and provide unified access to the Cisco UCS domain. 

The Cisco UCS FIs provide network connectivity and management for the connected servers. The Cisco UCS Fabric Interconnects run the Cisco UCS Manager control software and consist of expansion modules for the Cisco UCS Manager software. 

For more information about Cisco UCS Fabric Interconnects, see the Cisco UCS Manager Getting Started Guide. 

---

## Page 18: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Network-Mgmt/4-3/b_CLI_UCSM_Network_Management_Guide_chapter_0101.html

## VLANs

A VLAN is a switched network that is logically segmented by function, project team, or application, without regard to the physical locations of the users. VLANs have the same attributes as physical LANs, but you can group end stations even if they are not physically located on the same LAN segment. 

Any switch port can belong to a VLAN. Unicast, broadcast, and multicast packets are forwarded and flooded only to end stations in the VLAN. Each VLAN is considered a logical network, and packets destined for stations that do not belong to the VLAN must be forwarded through a router or bridge. 

VLANs are typically associated with IP subnetworks. For example, all of the end stations in a particular IP subnet belong to the same VLAN. To communicate between VLANs, you must route the traffic. By default, a newly created VLAN is operational. Additionally, you can configure VLANs to be in the active state, which is passing traffic, or in the suspended state, in which the VLANs are not passing packets. By default, the VLANs are in the active state and pass traffic. 

---

## Page 19: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Network-Mgmt/4-3/b_CLI_UCSM_Network_Management_Guide_chapter_01000.html

## Quality of Service 

Cisco UCS provides the following methods to implement quality of service: 

  * System classes that specify the global configuration for certain types of traffic across the entire system 

  * QoS policies that assign system classes for individual vNICs 

  * Flow control policies that determine how uplink Ethernet ports handle pause frames 


Global QoS changes made to the QoS system class may result in brief data-plane interruptions for all traffic. Some examples of such changes are: 

  * Changing the MTU size for an enabled class 

  * Changing packet drop for an enabled class 

  * Changing the CoS value for an enabled class 


###  Guidelines and Limitations for Quality of Service on Cisco UCS Fabric Interconnects 9108 100G, Cisco UCS 6536 Fabric Interconnects, Cisco UCS 6400 Series Fabric Interconnects 

  * Multicast optimization is not supported.

  * For all QoS system classes except for Fibre Channel, the default MTU is 1500 bytes. The MTU for Fiber Channel class is not configurable and is set to 2240 bytes internally. All classes (excluding Fibre Channel) allow for MTU configuration up to a maximum of 9216 bytes. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The maximum MTU for a QoS class on the Fabric Interconnect is 9216 bytes, while the maximum MTU that can be set on a vNIC is 9000 bytes. The vNIC MTU is configured through the adapter policy. 

* * *  
  
---|---  
  * The MTU size for fibre channel is always 2240 bytes.

  * Multicast is not supported on any no-drop QoS class.


###  Guidelines and Limitations for Quality of Service on Cisco UCS 6300 Series Fabric Interconnect

  * Cisco UCS 6300 Series Fabric Interconnect uses a shared buffer for all system classes. 

  * Multicast optimization is not supported. 

  * Multicast is not supported on any no-drop QoS class.

  * When you change the QoS parameters for any class causes traffic disruption to all classes. The following table lists the changes in the QoS system class and the conditions that trigger a system reboot. 

QoS System class status  |  Condition  |  FI Reboot Status   
---|---|---  
Enabled  |  Change between drop and no drop  |  Yes   
No-drop  |  Change between enable and disable  |  Yes   
Enable and no-drop  |  Change in MTU size  |  Yes   
  * The subordinate FI reboots first as a result of the change in the QoS system class. The primary FI reboots only after you acknowledge it in Pending Activities. 


###  Guidelines and Limitations for Quality of Service on Cisco UCS Mini

  * Cisco UCS Mini uses a shared buffer for all system classes. 

  * The bronze class shares the buffer with SPAN. We recommend using either SPAN or the bronze class. 

  * Multicast optimization is not supported. 

  * Multicast is not supported on any no-drop QoS class.

  * Changing the QoS parameters for any class causes traffic disruption to all classes. 

  * When mixing Ethernet and FC or FCoE traffic, the bandwidth distribution is not equal. 

  * Multiple streams of traffic from the same class may not be distributed equally. 

  * Use the same CoS values for all no-drop policies to avoid any FC or FCoE performance issues. 

  * Only the platinum and gold classes support no-drop policies. 


---

## Page 20: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Network-Mgmt/4-3/b_CLI_UCSM_Network_Management_Guide_chapter_01011.html

## vNIC Template 

The vNIC LAN connectivity policy defines how a vNIC on a server connects to the LAN. 

Cisco UCS Manager does not automatically create a VM-FEX port profile with the correct settings when you create a vNIC template. If you want to create a VM-FEX port profile, you must configure the target of the vNIC template as a VM. You must include this policy in a service profile for it to take effect. 

You can select VLAN groups in addition to any individual VLAN while creating a vNIC template.

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

If your server has two Emulex or QLogic NICs (Cisco UCS CNA M71KR-E or Cisco UCS CNA M71KR-Q), you must configure vNIC policies for both adapters in your service profile to get a user-defined MAC address for both NICs. If you do not configure policies for both NICs, Windows still detects both of them in the PCI bus. Then because the second eth is not part of your service profile, Windows assigns it a hardware MAC address. If you then move the service profile to a different server, Windows sees additional NICs because one NIC did not have a user-defined MAC address. 

* * *  
  
---|---  
  
### Creating vNIC Template Pairs 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A/ org # create vnic-templ  vnic-primary .  |  Creates a Primary vNIC template.   
**Step 2** |  UCS-A/ # org vnic-templ set type updating-template .  |  Set the template type to updating, which drives the configurations in the Primary vNIC template for shared configurations to the peer vNIC template. See the shared configurations listed below.   
**Step 3** |  UCS-A/ # org vnic-templ  [set fabric {a | b}]  .  |  Specifies the fabric for the Primary vNIC template. If you specify Fabric A for the Primary vNIC template, the Secondary vNIC template must be Fabric B or vice versa.   
**Step 4** |  UCS-A/ # org vnic-templ set descr primaryinredundancypair .  |  Sets the template as the Primary vNIC template.   
**Step 5** |  UCS-A/ # org vnic-templ set redundancy-type  primary .  |  Sets the redundancy template type as the Primary vNIC template.  Following are descriptions of the Redundancy Types:  Primary—Creates configurations that can be shared with the Secondary vNIC template. Any shared changes on the Primary vNIC template are automatically synchronized to the Secondary vNIC template.  Secondary — All shared configurations are inherited from the Primary template.  No Redundancy— Legacy vNIC template behavior.  Following is a list of shared configurations: 

  * Network Control Policy
  * QoS Policy 
  * Stats Threshold Policy 
  * Template Type
  * Connection Policies
  * VLANS
  * MTU

Following is a list of non-shared configurations: 

  * Fabric ID
  * CDN Source
  * MAC Pool 
  * Description
  * Pin Group Policy

  
**Step 6** |  UCS-A/ # org vnic-templ exit .  |  Exits creating the redundancy template pairing.  |  **Note** |  Ensure to commit the transaction after linking the Primary vNIC template to a peer Secondary vNIC template to create the redundancy pair.   
---|---  
**Step 7** |  UCS-A/ # org vnic-templ create vNIC-templ  vNICsecondary .  |  Creates the Secondary vNIC template.   
**Step 8** |  UCS-A/ # org vnic-templ set type updating-template .  |  Sets the template type to updating, which automatically inherits the configurations from the Primary vNIC template.   
**Step 9** |  UCS-A/ org # vnic-templ  [set fabric {a | b}]  .  |  Specifies the fabric for the Secondary vNIC template. If you specify Fabric A for the Primary vNIC template, the Secondary vNIC template must be Fabric B or vice versa.   
**Step 10** |  UCS-A/ # org vnic-templ set descr secondaryredundancypair .  |  Sets the secondary vNIC template as a redundancy pair template.   
**Step 11** |  UCS-A/ # org vnic-templ set redundancy-type  secondary .  |  Sets the vNIC template type as Secondary.   
**Step 12** |  UCS-A/ # org vnic-templ set peer-template-name  vNIC-primary .  |  Sets the Primary vNIC template as the peer to the Secondary vNIC template.   
**Step 13** |  UCS-A/ # org vnic-templ  commit-buffer .  |  Commits the transaction to the system configuration.   
  
#### Example

The following example configures a vNIC redundancy template pair and commits the transaction: 
    
    
    UCS-A /org* # **create vnic-template vnic-primary**
    UCS-A /org/vnic-templ* # **set type updating-template**
    UCS-A /org/vnic-templ* # **set fabric a**
    UCS-A /org/vnic-templ* # **set descr primaryinredundancypair**
    UCS-A /org/vnic-templ* # **set redundancy-type primary**
    UCS-A /org/vnic-templ* # **exit**
    UCS-A /org* # **create vnic-templ vnicsecondary**
    UCS-A /org/vnic-templ* # **set fabric b**
    UCS-A /org/vnic-templ* # **set descr secondaryinredundancypair**
    UCS-A /org/vnic-templ* # **set redundancy-type secondary**
    UCS-A /org/vnic-templ* # **set peer-template-name vnic-primary**
    UCS-A /org/vnic-templ* # **commit-buffer**
    UCS-A /org/vnic-templ # 
    

#### What to do next

After you create the vNIC redundancy template pair, you can use the redundancy template pair to create redundancy vNIC pairs for any service profile in the same organization or sub- organization. 

### Undo vNIC Template Pairs 

You can undo the vNIC template pair by changing the Peer Redundancy Template so that there is no peer template for the Primary or the Secondary template. When you undo a vNIC template pair, the corresponding vNIC pairs also becomes undone. 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A /org #  scope vnic-templ template1 .  |  Specifies the name of the vNIc template that you want to undo from the template pair.   
**Step 2** |  UCS-A /org/ vnic-templ #  set redundancy-type no redundancy .  |  Removes the paring between the peer Primary or Secondary redundancy template used to perform the template pairing.   
**Step 3** |  UCS-A /org/vnic-templ* #  commit-buffer .  |  Commits the transaction to the system configuration.   
  
#### Example

The following example shows how to undo a template pairing: 
    
    
    UCS-A /org # **scope vnic-templ template1**
    UCS-A /org/vnic-templ # **set redundancy-type no-redundancy**
    UCS-A /org/vnic-templ* # commit buffer
    

### Configuring a vNIC Template

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope org org-name |  Enters the organization mode for the specified organization. To enter the root organization mode, enter / as the org-name .   
**Step 2** |  UCS-A /org # create vnic-templ vnic-templ-name [eth-if vlan-name] [fabric {a | b}] [target [adapter | vm]]  |  Creates a vNIC template and enters organization vNIC template mode.  The target you choose determines whether or not Cisco UCS Manager automatically creates a VM-FEX port profile with the appropriate settings for the vNIC template. This can be one of the following: 

  * Adapter—The vNICs apply to all adapters. No VM-FEX port profile is created if you choose this option. 
  * VM—The vNICs apply to all virtual machines. A VM-FEX port profile is created if you choose this option. 

  
**Step 3** |  (Optional) UCS-A /org/vnic-templ # set descr description | (Optional)  Provides a description for the vNIC template.   
**Step 4** |  (Optional) UCS-A /org/vnic-templ # set fabric {a | a-b | b | b-a}  | (Optional)  Specifies the fabric to use for the vNIC. If you did not specify the fabric when creating the vNIC template in Step 2, you have the option to specify it with this command.  If you want this vNIC to be able to access the second fabric interconnect if the default one is unavailable, choose a-b (A is the primary) or b-a (B is the primary) .  |  **Note** |  Do not enable fabric failover for the vNIC under the following circumstances: 

  * If the Cisco UCS domain is running in Ethernet Switch Mode. vNIC fabric failover is not supported in that mode. If all Ethernet uplinks on one fabric interconnect fail, the vNICs do not fail over to the other. 
  * If you plan to associate this vNIC to a server with an adapter that does not support fabric failover, such as the Cisco UCS 82598KR-CI 10-Gigabit Ethernet Adapter. If you do so, Cisco UCS Manager generates a configuration fault when you associate the service profile with the server. 

  
---|---  
**Step 5** |  UCS-A /org/vnic-templ # set mac-pool mac-pool-name |  The MAC address pool that vNICs created from this vNIC template should use.  
**Step 6** |  UCS-A /org/vnic-templ # set mtu mtu-value |  The maximum transmission unit, or packet size, that vNICs created from this vNIC template should use. Enter an integer between 1500 and 9000.  |  **Note** |  If the vNIC template has an associated QoS policy, the MTU specified here must be equal to or less than the MTU specified in the associated QoS system class. If this MTU value exceeds the MTU value in the QoS system class, packets may be dropped during data transmission.  For VIC 1400 Series, VIC 14000 Series, and VIC 15000 Series adapters, you can change the MTU size of the vNIC from the host interface settings. When the Overlay network is configured, make sure that the new value is equal to or less than the MTU specified in the associated QoS system class or packets could be dropped during data transmission.   
---|---  
**Step 7** |  UCS-A /org/vnic-templ # set nw-control-policy policy-name |  The network control policy that vNICs created from this vNIC template should use.  
**Step 8** |  UCS-A /org/vnic-templ # set pin-group group-name |  The LAN pin group that vNICs created from this vNIC template should use.  
**Step 9** |  UCS-A /org/vnic-templ # set qos-policy policy-name |  The quality of service policy that vNICs created from this vNIC template should use.  
**Step 10** |  UCS-A /org/vnic-templ # set stats-policy policy-name |  The statistics collection policy that vNICs created from this vNIC template should use.  
**Step 11** |  UCS-A /org/vnic-templ # set type {initial-template | updating-template}  |  Specifies the vNIC template update type. If you do not want vNIC instances created from this template to be automatically updated when the template is updated, use the initial-template keyword; otherwise, use the  updating-template keyword to ensure that all vNIC instances are updated when the vNIC template is updated.   
**Step 12** |  UCS-A /org/vnic-templ #  commit-buffer |  Commits the transaction to the system configuration.   
  
#### Example

The following example configures a vNIC template and commits the transaction: 
    
    
    UCS-A# **scope org /**
    UCS-A /org* # **create vnic template VnicTempFoo**
    UCS-A /org/vnic-templ* # **set descr "This is a vNIC template example."**
    UCS-A /org/vnic-templ* # **set fabric a**
    UCS-A /org/vnic-templ* # **set mac-pool pool137**
    UCS-A /org/vnic-templ* # **set mtu 8900**
    UCS-A /org/vnic-templ* # **set nw-control-policy ncp5**
    UCS-A /org/vnic-templ* # **set pin-group PinGroup54**
    UCS-A /org/vnic-templ* # **set qos-policy QosPol5**
    UCS-A /org/vnic-templ* # **set stats-policy ServStatsPolicy**
    UCS-A /org/vnic-templ* # **set type updating-template**
    UCS-A /org/vnic-templ* # **commit-buffer**
    UCS-A /org/vnic-templ # 
    

### Deleting a vNIC Template

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A# scope org org-name |  Enters the organization mode for the specified organization. To enter the root organization mode, enter / as the org-name .   
**Step 2** |  UCS-A /org #  delete vnic-templ ` ` vnic-templ-name |  Deletes the specified vNIC template.   
**Step 3** |  UCS-A /org #  commit-buffer |  Commits the transaction to the system configuration.   
  
#### Example

The following example deletes the vNIC template named VnicTemp42 and commits the transaction: 
    
    
    UCS-A# **scope org /**
    UCS-A /org # **delete vnic template VnicTemp42**
    UCS-A /org* # **commit-buffer**
    UCS-A /org # 
    

---

## Page 21: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Network-Mgmt/4-3/b_CLI_UCSM_Network_Management_Guide_chapter_0110.html

## LAN Pin Groups 

Cisco UCS uses LAN pin groups to pin Ethernet traffic from a vNIC on a server to an uplink Ethernet port or port channel on the fabric interconnect. You can use this pinning to manage the distribution of traffic from the servers. 

To configure pinning for a server, you must include the LAN pin group in a vNIC policy. The vNIC policy is then included in the service profile assigned to that server. All traffic from the vNIC travels through the I/O module to the specified uplink Ethernet port. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

If you do not assign a pin group to a server interface through a vNIC policy, Cisco UCS Manager chooses an uplink Ethernet port or port channel for traffic from that server interface dynamically. This choice is not permanent. A different uplink Ethernet port or port channel may be used for traffic from that server interface after an interface flap or a server reboot.  If an uplink is part of a LAN pin group, the uplink is not necessarily reserved for only that LAN pin group. Other vNIC's policies that do not specify a LAN pin group can use the uplink as a dynamic uplink. 

* * *  
  
---|---

---
