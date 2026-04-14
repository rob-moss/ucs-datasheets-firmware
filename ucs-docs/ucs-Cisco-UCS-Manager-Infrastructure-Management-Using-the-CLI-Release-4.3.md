# UCS Manager CLI Infrastructure Management Guide 4.3

| | |
|---|---|
| **URL Title** | UCS Manager CLI Infrastructure Management Guide 4.3 |
| **URL** | https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_4_3.html |
| **Long URL** |  |
| **HTML Title** | Cisco UCS Manager Infrastructure Management Using the CLI, Release 4.3 |
| **Source file** | `ucs-docs-raw/html/b_UCSM_CLI_Infrastructure_Management_Guide_4_3.html` |
| **File type** | HTML |
| **Fetched on** | 2026-04-13 13:30:43 |

---

## Page 1: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_4_3.html

![Clear Contents of Search](/etc/designs/cdc/fw/i/ic_clear_gray.png)

---

## Page 2: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_4_3/b_UCSM_CLI_Infrastructure_Management_Guide_4_1_preface_00.html

## Audience  
  
This guide is intended primarily for data center administrators with responsibilities and expertise in one or more of the following: 

  * Server administration 

  * Storage administration 

  * Network administration 

  * Network security 


---

## Page 3: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_4_3/b_UCSM_CLI_Infrastructure_Management_Guide_chapter_01101.html

## New and Changed Information

This section provides information on new feature and changed behavior in Release 4.3.

Table 1. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(6a) Feature |  Description |  Where Documented  
---|---|---  
Support for Package Power Limit (PPL) |  Cisco UCS Manager supports configuring the Package Power Limit for Power Control Policy. |  [Creating a Power Control Policy](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_0111.html#task_E14D7E00D291462A8BAF78D11C604A4C)  
Support for Maximum Cooling in Fan Speed Policy |  Cisco UCS Manager supports Maximum Cooling option in Fan Speed Policy to optimize cooling efficiency for CPU. |  [Creating a Power Control Policy](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_0111.html#task_E14D7E00D291462A8BAF78D11C604A4C)  
Table 2. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(5a) Feature |  Description |  Where Documented  
---|---|---  
Support for Cisco UCS C-Series M8 server |  Cisco UCS Manager now supports Cisco UCS C225 M8 Server.  |  [Data Sanitization](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_01000.html#data-sanitization)  
Support for Cisco UCS X-Series M8 server |  Cisco UCS Manager now supports Cisco UCS X215c M8 Compute Node.  | 

  * [Overview of Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct)](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_01110.html#overview-of-cisco-ucs-x-direct)
  * [Data Sanitization](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_01000.html#data-sanitization)

  
Table 3. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(4b) Feature |  Description |  Where Documented  
---|---|---  
Support for Cisco UCS X-Series Direct |  Cisco UCS Manager now supports Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct).  | 

  * [Cisco UCS Building Blocks and Connectivity](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_01110.html#concept_uxd_4pl_3jb)
  * [Overview of Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct)](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_01110.html#overview-of-cisco-ucs-x-direct)
  * [Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct) Architecture](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_01110.html#cisco-ucs-x-direct-architecture)
  * [Port Breakout Functionality on Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct)](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_01110.html#port-breakout-functionality-on-cisco-ucs-x-direct)
  * [Chassis/FEX Discovery Policy](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_011.html#concept_40AFE09861FA4D02A9879856A1411FAC)
  * [Configuring the Chassis/FEX Discovery Policy](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_011.html#task_4984141203506035088)
  * [Chassis Connectivity Policy](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_011.html#concept_4E5E1F56073248329020AC2927156A9F)
  * [Configuring a Chassis Connectivity Policy](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_011.html#task_D41B14E4E5524F53845D38A6C8FF2C50)
  * [Power Capping in Cisco UCS](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_0111.html#concept_943D968485A04A92BAA307A2FC59AD18)

  
Table 4. New Features and Changed Behavior in Cisco UCS Manager, Release4.3(4b) Feature |  Description |  Where Documented  
---|---|---  
Support for Cisco UCS C-Series M8 servers |  Cisco UCS Manager now supports Cisco UCS C245 M8 Servers.  | 

  * [Power Capping in Cisco UCS](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_0111.html#concept_943D968485A04A92BAA307A2FC59AD18)
  * [Data Sanitization](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_01000.html#data-sanitization)

  
Table 5. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(2c) Feature |  Description |  Where Documented  
---|---|---  
Support for Cisco UCS X-Series servers |  Cisco UCS Manager supports Cisco UCS X410c M7 Compute Node.  Cisco UCS X-Series servers support Intelligent Fabric Modules (IFM), which function similarly to the Input/Output Module (IOM) in Cisco UCS B-Series servers.  |  —   
Support for Cisco UCS VIC cards |  Cisco UCS Manager supports the following Cisco UCS VIC cards:

  * Cisco UCS VIC 15230
  * Cisco UCS VIC 15237 mLOM
  * Cisco UCS VIC 15427

|  —  
Table 6. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(2b) Feature |  Description |  Where Documented  
---|---|---  
Support for Power Capping and Power Management for Cisco UCSX-9508 Chassis |  Cisco UCS Manager now supports Power Capping and Power Management for Cisco UCSX-9508 Chassis. |  [Power Capping in Cisco UCS](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_0111.html#concept_943D968485A04A92BAA307A2FC59AD18)  
Support for Cisco UCS X9508 server chassis with Cisco UCS X-Series servers |  Cisco UCS Manager supports Cisco UCSX-9508 Chassis with the following Cisco UCS X-Series servers:

  * Cisco UCS X210c M7 Compute Node
  * Cisco UCS X210c M6 Compute Node

Cisco UCS X-Series servers support Intelligent Fabric Modules (IFM), which function similarly to the Input/Output Module (IOM) in Cisco UCS B-Series servers.  |  —   
Support Cisco UCS C-Series M7 servers |  Cisco UCS Manager now supports the following C-Series M7 servers:

  * Cisco UCS C240 M7 Server
  * Cisco UCS C220 M7 Server

|  [Power Capping in Cisco UCS](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_0111.html#concept_943D968485A04A92BAA307A2FC59AD18)  
Support for Cisco UCS X9508 Server Chassis equipped with X-Fabric Module (XFM) |  Cisco UCS Manager introduces inventory support for Cisco UCS X9508 Server Chassis equipped with X-Fabric Module (XFM) |  [Viewing X-Fabric Module (XFM) Fan Status](b_UCSM_CLI_Infrastructure_Management_Guide_chapter_0111.html#viewing-xfm-fan-overall-status)  
Support for Cisco UCS 6200 Series Fabric Interconnect is deprecated |  Cisco UCS Manager deprecates support for Cisco UCS 6200 Series Fabric Interconnects. |  —   
Support for Cisco UCS M4 servers are deprecated |  Cisco UCS Manager deprecates support for UCS B-series, C-series, and S-series M4 servers. |  — 

---

## Page 4: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_4_3/b_UCSM_CLI_Infrastructure_Management_Guide_chapter_01110.html

## Cisco UCS Manager User CLI Documentation  
  
Cisco UCS Manager offers you a new set of smaller, use-case based documentation described in the following table: 

Guide  |  Description   
---|---  
[Cisco UCS Manager Getting Started Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses Cisco UCS architecture and Day 0 operations, including Cisco UCS Manager initial configuration, and configuration best practices.   
[Cisco UCS Manager Administration Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses password management, role-based access configuration, remote authentication, communication services, CIMC session management, organizations, backup and restore, scheduling options, BIOS tokens and deferred deployments.   
[Cisco UCS Manager Infrastructure Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses physical and virtual infrastructure components used and managed by Cisco UCS Manager.   
[Cisco UCS Manager Firmware Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses downloading and managing firmware, upgrading through Auto Install, upgrading through service profiles, directly upgrading at endpoints using firmware auto sync, managing the capability catalog, deployment scenarios, and troubleshooting.   
[Cisco UCS Manager Server Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses the new licenses, registering Cisco UCS domains with Cisco UCS Central, power capping, server boot, server profiles and server-related policies.   
[Cisco UCS Manager Storage Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses all aspects of storage management such as SAN and VSAN in Cisco UCS Manager.   
[Cisco UCS Manager Network Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses all aspects of network management such as LAN and VLAN connectivity in Cisco UCS Manager.   
[Cisco UCS Manager System Monitoring Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses all aspects of system and health monitoring including system statistics in Cisco UCS Manager.   
[Cisco UCS S3260 Server Integration with Cisco UCS Manager](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses all aspects of management of UCS S-Series servers that are managed through Cisco UCS Manager. 

---

## Page 5: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_4_3/b_UCSM_CLI_Infrastructure_Management_Guide_chapter_011.html

## Chassis/FEX Discovery Policy   
  
The chassis/FEX discovery policy determines how the system reacts when you add a new chassis or FEX. Cisco UCS Manager uses the settings in the chassis/FEX discovery policy to determine the minimum threshold for the number of links between the chassis or FEX and the fabric interconnect and whether to group links from the IOM to the fabric interconnect in a fabric port channel. 

In a Cisco UCS Mini (Cisco UCS 6324 Fabric Interconnect) setup, chassis discovery policy is supported only on the extended chassis. 

### Chassis Links

If you have a Cisco UCS domain with some of the chassis' wired with one link, some with two links, some with four links, and some with eight links, Cisco recommends configuring the chassis/FEX discovery policy for the minimum number links in the domain so that Cisco UCS Manager can discover all chassis. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/tip.gif)  
**Tip** | 

* * *

To establish the highest available chassis connectivity in a Cisco UCS domain where Fabric Interconnect is connected to different types of IO Modules supporting different max number of uplinks, select platform max value. Setting the platform max ensures that Cisco UCS Manager discovers the chassis including the connections and servers only when the maximum supported IOM uplinks are connected per IO Module. 

* * *  
  
---|---  
  
After the initial discovery of a chassis, if chassis/FEX discovery policy changes are done, acknowledge IO Modules rather than the entire Chassis to avoid disruption. The discovery policy changes can include increasing the number of links between Fabric Interconnect and IO Module, or changes to the Link Grouping preference. 

Make sure that you monitor for faults before and after the IO Module acknowledgement to ensure that the connectivity is restored before proceeding to the other IO Module for the chassis. 

Cisco UCS Manager cannot discover any chassis that is wired for fewer links than are configured in the chassis/FEX discovery policy. For example, if the chassis/FEX discovery policy is configured for four links, Cisco UCS Manager cannot discover any chassis that is wired for one link or two links. Re-acknowledgement of the chassis resolves this issue. 

The following table provides an overview of how the chassis/FEX discovery policy works in a multi-chassis Cisco UCS domain: 

Table 1. Chassis/FEX Discovery Policy and Chassis Links Number of Links Wired for the Chassis  | 1-Link Discovery Policy  | 2-Link Discovery Policy  | 4-Link Discovery Policy  | 8-Link Discovery Policy  | Platform-Max Discovery Policy   
---|---|---|---|---|---  
**1 link between IOM and fabric interconnects** |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 1 link.  |  Chassis connections and servers cannot be discovered by Cisco UCS Manager and are not added to the Cisco UCS domain.  |  Chassis connections and servers cannot be discovered by Cisco UCS Manager and are not added to the Cisco UCS domain.  |  Chassis connections and servers cannot be discovered by Cisco UCS Manager and are not added to the Cisco UCS domain.  |  Chassis connections and servers cannot be discovered by Cisco UCS Manager and are not added to the Cisco UCS domain.   
**2 links between IOM and fabric interconnects** |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 1 link.  After initial discovery, reacknowledge the chassis and Cisco UCS Manager recognizes and uses the additional links.  |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 2 link.  |  Chassis connections and servers cannot be discovered by Cisco UCS Manager and are not added to the Cisco UCS domain.  |  Chassis connections and servers cannot be discovered by Cisco UCS Manager and are not added to the Cisco UCS domain.  |  Chassis connections and servers cannot be discovered by Cisco UCS Manager and are not added to the Cisco UCS domain.   
**4 links between IOM and fabric interconnects** |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 1 link.  After initial discovery, reacknowledge the chassis and Cisco UCS Manager recognizes and uses the additional links.  |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 2 links.  After initial discovery, reacknowledge the chassis and Cisco UCS Manager recognizes and uses the additional links.  |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 4 link.  |  Chassis connections and servers cannot be discovered by Cisco UCS Manager and are not added to the Cisco UCS domain.  |  If the IOM has 4 links, the chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 4 links.  |  **Note** |  If the FEX status shows accessibility problem then reacknowledge the chassis after decommissioning/recommissioning FEX.  
---|---  
  
If the IOM has 8 links, the chassis is not fully discovered by Cisco UCS Manager.   
  
**8 links between IOM and fabric interconnects** |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 1 link.  After initial discovery, reacknowledge the chassis and Cisco UCS Manager recognizes and uses the additional links.  |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 2 links.  After initial discovery, reacknowledge the chassis and Cisco UCS Manager recognizes and uses the additional links.  |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 4 links.  After initial discovery, reacknowledge the chassis and Cisco UCS Manager recognizes and uses the additional links.  |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 8 links.  |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 8 links.   
  
### Link Grouping

For hardware configurations that support fabric port channels, link grouping determines whether all of the links from the IOM to the fabric interconnect are grouped in to a fabric port channel during chassis discovery. If the link grouping preference is set to Port Channel, all of the links from the IOM to the fabric interconnect are grouped in a fabric port channel. If set to None, links from the IOM are pinned to the fabric interconnect. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

For Cisco UCS X-Series Direct, Cisco UCS 6500 Series Fabric Interconnects, Cisco UCS 6400 Series Fabric Interconnect, the link grouping preference is always set to Port Channel. 

* * *  
  
---|---  
  
After a fabric port channel is created through Cisco UCS Manager, you can add or remove links by changing the link group preference and re-acknowledging the chassis, or by enabling or disabling the chassis from the port channel. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The link grouping preference only takes effect if both sides of the links between an IOM and IFM (IOM for Cisco UCS X-Series Servers) or FEX and the fabric interconnect support fabric port channels. If one side of the links does not support fabric port channels, this preference is ignored and the links are not grouped in a port channel. 

* * *  
  
---|---  
  
### Multicast Hardware Hash

In a port channel, by default, ingress multicast traffic on any port in the fabric interconnect (FI) selects a particular link between the IOM and the fabric interconnect to egress the traffic. To reduce potential issues with the bandwidth, and to provide effective load balancing of the ingress multicast traffic, hardware hashing is used for multicast traffic. When multicast hardware hashing is enabled, all links between the IOM and the fabric interconnect in a port channel can be used for multicast traffic. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCS X-Series Direct, Cisco UCS 6500 Series Fabric Interconnects, andCisco UCS 6400 Series Fabric Interconnect do not support multicast hardware hashing. 

* * *  
  
---|---  
  
### Pinning

Pinning in Cisco UCS is only relevant to uplink ports. If you configure Link Grouping Preference as None during chassis discovery, the IOM forwards traffic from a specific server to the fabric interconnect through its uplink ports by using static route pinning. 

The following table showcases how pinning is done between an IOM and the fabric interconnect based on the number of active fabric links between the IOM and the fabric interconnect. 

Table 2. Pinning on an IOM Number of Active Fabric Links  |  Server slot pinned to fabric link   
---|---  
1-Link  |  All the HIF ports are pinned to the active link   
2-Link  |  1,3,5,7 to link-1  2,4,6,8 to link-2   
4-Link  |  1,5 to link-1  2,6 to link-2  3,7 to link-3  4,8 to link-4   
8-Link (Applies only to 2208XP )  |  1 to link-1  2 to link-2  3 to link-3  4 to link-4  5 to link-5  6 to link-6  7 to link-7  8 to link-8   
  
Only 1,2,4 and 8 links are supported. 3,5,6, and 7 links are not valid configurations. 

### Port-Channeling

While pinning traffic from a specific server to an uplink port provides you with greater control over the unified fabric and ensures optimal utilization of uplink port bandwidth, it could also mean excessive traffic over certain circuits. This issue can be overcome by using port channeling. Port channeling groups all links between the IOM and the fabric interconnect into one port channel. The port channel uses a load balancing algorithm to decide the link over which to send traffic. This results in optimal traffic management. 

Cisco UCS supports port-channeling only through the Link Aggregation Control Protocol (LACP). For hardware configurations that support fabric port channels, link grouping determines whether all of the links from the IOM to the fabric interconnect are grouped into a fabric port channel during chassis discovery. If the Link Grouping Preference is set to Port Channel, all of the links from the IOM to the fabric interconnect are grouped in a fabric port channel. If this parameter is set to None, links from the IOM to the fabric interconnect are not grouped in a fabric port channel. 

Once a fabric port channel is created, links can be added or removed by changing the link group preference and reacknowledging the chassis, or by enabling or disabling the chassis from the port channel. 

### Configuring the Chassis/FEX Discovery Policy 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

In a setup with Cisco UCS 6400 Series Fabric Interconnects, the Link Grouping Preference value for Chassis/FEX Discovery Policy is not user configurable. The value is set to Port Channel. 

* * *  
  
---|---  
  
#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope org / |  Enters the root organization mode.  |  **Note** |  The chassis/FEX discovery policy can be accessed only from the root organization.   
---|---  
**Step 2** |  UCS-A /org #  scope chassis-disc-policy |  Enters organization chassis/FEX discovery policy mode.   
**Step 3** |  UCS-A /org/chassis-disc-policy #  set action ` `{1-link | 2-link | 4-link | 8-link | platform-max}  |  Specifies the minimum threshold for the number of links between the chassis or FEX and the fabric interconnect.   
**Step 4** |  (Optional) UCS-A /org/chassis-disc-policy # set descr ` ` description | (Optional)  Provides a description for the chassis/FEX discovery policy.  |  **Note** |  If your description includes spaces, special characters, or punctuation, you must begin and end your description with quotation marks. The quotation marks will not appear in the description field of any  show command output.   
---|---  
**Step 5** |  UCS-A /org/chassis-disc-policy #  set link-aggregation-pref ` `{none | port-channel}  |  Specifies whether the links from the IOMs or FEXes to the fabric interconnects are grouped in a port channel.  |  **Note** |  The link grouping preference only takes effect if both sides of the links between an IOM and IFM (IOM for Cisco UCS X-Series Servers) or FEX and the fabric interconnect support fabric port channels. If one side of the links does not support fabric port channels, this preference is ignored and the links are not grouped in a port channel.   
---|---  
**Note** |  For UCS manager to discover VIC 1455 and VIC 1457, Link Grouping Preference must be configured as Port Channel.   
---|---  
**Step 6** |  UCS-A /org/chassis-disc-policy # set multicast-hw-hash {disabled | enabled}  |  Specifies whether the all the links between the IOM and the fabric interconnect in a port channel can be used for multicast traffic. 

  * disabled —Only one link between the IOM and the fabric interconnect is used for multicast traffic 
  * enabled —All links between the IOM and the fabric interconnect can be used for multicast traffic 

  
**Step 7** |  (Optional) UCS-A /org/chassis-disc-policy #  set qualifier ` ` qualifier | (Optional)  Uses the specified server pool policy qualifications to associate this policy with a server pool.   
**Step 8** |  UCS-A /org/chassis-disc-policy #  commit-buffer |  Commits the transaction to the system configuration.   
  
#### Example

The following example scopes to the default chassis/FEX discovery policy, sets it to discover chassis with four links to a fabric interconnect, provides a description for the policy, specifies the server pool policy qualifications that will be used to qualify the chassis, and commits the transaction: 
    
    
    UCS-A# **scope org /**
    UCS-A /org # **scope chassis-disc-policy**
    UCS-A /org/chassis-disc-policy* # **set action 4-link**
    UCS-A /org/chassis-disc-policy* # **set descr "This is an example chassis/FEX discovery policy."**
    UCS-A /org/chassis-disc-policy* # **set qualifier ExampleQual**
    UCS-A /org/chassis-disc-policy* # **commit-buffer**
    UCS-A /org/chassis-disc-policy # 
    
    
    

The following example scopes to the default chassis/FEX discovery policy, sets it to discover chassis with eight links to a fabric interconnect, provides a description for the policy, sets the link grouping preference to port channel, specifies the server pool policy qualifications that will be used to qualify the chassis, and commits the transaction: 
    
    
    UCS-A# **scope org /**
    UCS-A /org # **scope chassis-disc-policy**
    UCS-A /org/chassis-disc-policy* # **set action 8-link**
    UCS-A /org/chassis-disc-policy* # **set descr "This is an example chassis/FEX discovery policy."**
    UCS-A /org/chassis-disc-policy* # **set link-aggregation-pref port-channel**
    UCS-A /org/chassis-disc-policy* # **set qualifier ExampleQual**
    UCS-A /org/chassis-disc-policy* # **commit-buffer**
    UCS-A /org/chassis-disc-policy # 
    
    
    

The following example scopes to the default chassis/FEX discovery policy, sets it to discover chassis with four links to a fabric interconnect, provides a description for the policy, sets the link grouping preference to port channel, enables multicast hardware hashing, specifies the server pool policy qualifications that will be used to qualify the chassis, and commits the transaction: 
    
    
    UCS-A# scope org /
    UCS-A /org # scope chassis-disc-policy
    UCS-A /org/chassis-disc-policy* # set action 4-link
    UCS-A /org/chassis-disc-policy* # set descr "This is an example chassis/FEX discovery
    policy."
    UCS-A /org/chassis-disc-policy* # set link-aggregation-pref port-channel
    UCS-A /org/chassis-disc-policy* # set multicast-hw-hash enabled
    UCS-A /org/chassis-disc-policy* # set qualifier ExampleQual
    UCS-A /org/chassis-disc-policy* # commit-buffer
    UCS-A /org/chassis-disc-policy #
    
    

#### What to do next

To customize fabric port channel connectivity for a specific chassis, configure the chassis connectivity policy. 

---

## Page 6: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_4_3/b_UCSM_CLI_Infrastructure_Management_Guide_4_1_chapter_0100.html

## Chassis Management in Cisco UCS Manager CLI

You can manage and monitor all chassis in a Cisco UCS domain through Cisco UCS Manager CLI. 

### Cisco UCS X9508 Series Chassis

The Cisco UCS X-Series Modular System begins with the Cisco UCS X9508 Chassis. With a midplane-free design, I/O connectivity for the X9508 chassis is accomplished with frontloading, vertically oriented compute nodes intersecting with horizontally oriented I/O connectivity modules in the rear of the chassis. A unified Ethernet fabric is supplied with the Cisco UCS 9108 Intelligent Fabric Modules. 

The system is primed with Cisco UCS 9108 Intelligent Fabric Modules that provide a robust Ethernet fabric and is set to accommodate emerging protocols with the innovative Cisco UCS X-Fabric Technology, ensuring easy upgrades with new modules as they become available. 

The major feature of the chasssi include:

  * 7-Rack-Unit (7RU) chassis has 8x front-facing flexible slots. These can house a combination of compute nodes and a pool of future I/O resources that may include GPU accelerators, disk storage, and nonvolatile memory. 

  * 2x Cisco UCS 9108 Intelligent Fabric Modules (IFMs) at the top of the chassis that connect the chassis to upstream Cisco UCS 6400 Series Fabric Interconnects. Each IFM features. 

  * Up to 100 Gbps of unified fabric connectivity per compute node

  * 8x 25-Gbps SFP28 uplink ports. The unified fabric carries management traffic to the Cisco Intersight cloud-operations platform, Fibre Channel over Ethernet (FCoE) traffic, and production Ethernet traffic to the fabric interconnects. 

  * At the bottom are slots ready to house future I/O modules that can flexibly connect the compute modules with I/O devices. We call this connectivity Cisco UCS X-Fabric technology because “X” is a variable that can evolve with new technology developments. 

  * Six 2800W Power Supply Units (PSUs) provide 54V power to the chassis with N, N+1, and N+N redundancy. A higher voltage allows efficient power delivery with less copper and reduced power loss. 

  * Efficient, 4x100mm, dual counter-rotating fans deliver industry-leading airflow and power efficiency. Optimized thermal algorithms enable different cooling modes to best support the network environment. Cooling is modular so that future enhancements can potentially handle open- or closed-loop liquid cooling to support even higher-power processors. 


This Cisco UCS X9508 Chassis supports Cisco UCS X-Series Direct, Cisco UCS 6536, UCS 6454, UCS 64108 fabric interconnects.

The Cisco UCS X-Series Direct, identified as UCSX-S9108-100G, enhances the Cisco UCS X-Series Modular System by incorporating a pair of internal Cisco UCS Fabric Interconnects S9108 100G. This integration creates a self-contained system that connects up to eight server nodes with unified fabric, IP, and Fibre Channel connectivity, all managed by Cisco UCS Manager. The X-Series Direct is compatible with all components of the X-Series Modular System. 

For more information, see [Cisco UCS X9508 Chassis Data Sheet](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-x-series-modular-system/datasheet-c78-2472574.html). 

### The Cisco UCS S3260 Chassis

Cisco UCS Manager Release 4.2(3) introduces support for the Cisco UCS S3260 chassis on Cisco UCS 6536 Fabric Interconnect. 

Cisco UCS Manager Release 4.1(1) introduces support for the Cisco UCS S3260 chassis on Cisco UCS 64108 Fabric Interconnect. 

Cisco UCS Manager Release 4.0(1) introduces support for the Cisco UCS S3260 chassis on Cisco UCS 6454 Fabric Interconnect. 

Cisco UCS Manager Release 3.1(2) introduces support for the Cisco UCS S3260 chassis on Cisco UCS 6300 Series fabric interconnect setups. 

The Cisco UCS S3260 chassis is a 4U chassis that is designed to operate in a standalone environment and also as part of the Cisco Unified Computing System. It has the following main components: 

  * Four 1050 Watt AC modular power supplies (2 + 2 shared and redundant mode of operation) 

  * Two System IO Controller (SIOC) slots 

  * Two storage server slots out of which one can be used for storage expansion 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The second server slot in the chassis can be utilized by an HDD expansion tray module for an additional four 3.5” drives. 

* * *  
  
---|---  
  * 56 3.5” drive bays with an optional 4 x 3.5” HDD expansion tray module instead of the second server 

  * Up to 360 TB storage capacity by using 6 TB HDDs 

  * Serial Attached SCSI (SAS) expanders that can be configured to assign the 3.5” drives to individual server modules 

  * The two servers in the chassis can be replaced by a single, dual-height server with an IO expander 


### Cisco UCS 5108 Blade Server Chassis 

The Cisco UCS 5100 Series Blade Server Chassis is logically part of the fabric interconnects, thus creating a single, coherent management domain and decreasing management complexity. In the management domain, server management is handled by the fabric interconnect, while I/O and network management is extended to every chassis and blade server. Basing the I/O infrastructure on a unified fabric allows the Cisco Unified Computing System to have a simple and streamlined chassis yet offer a comprehensive set of I/O options. This results in the chassis having only five basic components: 

  * The physical chassis with passive midplane and active environmental monitoring circuitry 

  * Four power-supply bays with power entry in the rear, and redundant-capable, hot-swappable power supply units accessible from the front panel 

  * Eight hot-swappable fan trays, each with two fans 

  * Two fabric extender slots accessible from the back panel 

  * Eight blade server slots accessible from the front panel 


The blade server chassis has flexible partitioning with removable dividers to handle two blade server form factors: 

  * Half-width blade servers have access to power and two 10GBASE-KR connections, one to each fabric extender slot. 

  * Full-width blade servers connect to power and two connections to each fabric extender. 


### Extended Chassis for UCS Mini 

Cisco UCS Manager Release 3.1(1) introduces support for an extended UCS 5108 chassis to an existing single-chassis Cisco UCS 6324 fabric interconnect setup. This extended chassis enables you to configure an additional 8 servers. Unlike the primary chassis, the extended chassis supports IOMs. Currently, it supports UCS-IOM-2204XP and UCS-IOM-2208XP IOMs. The extended chassis can only be connected through the scalability port on the FI-IOM. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

Currently, Cisco UCS Manager supports only one extended chassis for UCS Mini. 

* * *  
  
---|---  
To use a extended chassis, do the following: 

  * Connect the second Cisco UCS 5108 chassis to the existing single-chassis Cisco UCS 6324 Series fabric interconnect configuration through the scalability port. 

  * Configure the chassis discovery policy. 

  * Configure the server ports and wait for the second chassis to be discovered. 


---

## Page 7: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_4_3/b_UCSM_CLI_Infrastructure_Management_Guide_chapter_0101.html

## I/O Module Management in Cisco UCS Manager CLI

You can manage and monitor all I/O modules in a Cisco UCS domain through Cisco UCS Manager CLI. 

Cisco UCS Manager Release 4.1(1) extends support for the Cisco 2408 IO module to the Cisco UCS 64108 Fabric Interconnect. 

Cisco UCS Manager Release 4.0(4c) introduces the Cisco 2408 IO module. This IO Module has 32 25-Gigabit backplane ports and 4 100-Gigabit uplink ports, and is supported only on the Cisco UCS 6454 Fabric Interconnect. 

Cisco UCS Manager Release 4.0(4a) introduces the Cisco UCS-IOM-2304V2 I/O module which is based on Cisco UCS-IOM-2304 I/O module. 

Cisco UCS Manager Release 3.1(1) introduces the Cisco UCS-IOM-2304 I/O module with 40 GbE connectivity to the Cisco UCS 6300 Series Fabric Interconnect. The Cisco UCS Manager Getting Started Guide provides more information about this functionality. 

---

## Page 8: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_4_3/b_UCSM_CLI_Infrastructure_Management_Guide_chapter_0110.html

## SIOC Management in Cisco UCS Manager

You can manage and monitor all System Input/Output Controllers (SIOC) in a Cisco UCS domain through Cisco UCS Manager. 

### SIOC Removal or Replacement 

You can remove or replace an SIOC from a chassis. Removal or replacement of an SIOC is a service-affecting operation, which requires you to power down the entire chassis. 

#### Guidelines for SIOC Removal 

  * To remove the active SIOC, or both SIOCs, shut down and remove power from the entire chassis. You must disconnect all power cords to completely remove power. 

  * Removal of SIOCs from a chassis results in the entire chassis being disconnected from Cisco UCS Manager. 


#### SIOC Removal 

Do the following to remove an SIOC from the system: 

  1. Shut down and remove power from the entire chassis. You must disconnect all power cords to completely remove power.

  2. Disconnect the cables connecting the SIOC to the system. 

  3. Remove the SIOC from the system. 


#### SIOC Replacement 

Do the following to remove an SIOC from the system and replace it with another SIOC: 

  1. Shut down and remove power from the entire chassis. You must disconnect all power cords to completely remove power.

  2. Disconnect the cables connecting the SIOC to the system. 

  3. Remove the SIOC from the system. 

  4. Connect the new SIOC to the system. 

  5. Connect the cables to the SIOC. 

  6. Connect power cords and then power on the system.

  7. Acknowledge the new SIOC. 

The server connected to the replaced SIOC is rediscovered. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

If the firmware of the replaced SIOC is not the same version as the peer SIOC, then it is recommended to update the firmware of the replaced SIOC by re-triggering chassis profile association. 

* * *  
  
---|---  


---

## Page 9: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_4_3/b_UCSM_CLI_Infrastructure_Management_Guide_chapter_0111.html

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

## Page 10: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_4_3/b_UCSM_CLI_Infrastructure_Management_Guide_chapter_01000.html

## Blade Server Management   
  
You can manage and monitor all blade servers in a Cisco UCS domain through Cisco UCS Manager. You can perform some blade server management tasks, such as changes to the power state, from the server and service profile. 

The remaining management tasks can only be performed on the server. 

The power supply units go into power save mode when a chassis has two blades or less. When a third blade is added to the chassis and is fully discovered, the power supply units return to regular mode. 

If a blade server slot in a chassis is empty, Cisco UCS Manager provides information, errors, and faults for that slot. You can also re-acknowledge the slot to resolve server mismatch errors and to have Cisco UCS Manager rediscover the blade server in the slot. 

---

## Page 11: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_4_3/b_UCSM_CLI_Infrastructure_Management_Guide_chapter_01001.html

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

## Page 12: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_4_3/b_UCSM_CLI_Infrastructure_Management_Guide_chapter_01010.html

## Cisco UCS S3260 Server Node Management   
  
You can manage and monitor all Cisco UCS S3260 server nodes in a Cisco UCS domain through Cisco UCS Manager. You can perform some server management tasks, such as changes to the power state, from the server and service profile. 

The remaining management tasks can only be performed on the server. 

If a server slot in a chassis is empty, Cisco UCS Manager provides information, errors, and faults for that slot. You can also re-acknowledge the slot to resolve server mismatch errors and rediscover the server in the slot. 

---

## Page 13: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_4_3/b_UCSM_CLI_Infrastructure_Management_Guide_chapter_01011.html

## Virtual Circuits 

A virtual circuit or virtual path refers to the path that a frame takes from its source vNIC to its destination virtual switch port (vEth) or from a source virtual switch port to its destination vNIC. There are many possible virtual circuits that traverse through a physical cable. Cisco UCS Manager uses virtual network tags (VN-TAG) to identify these virtual circuits and differentiate between them. The OS decides the virtual circuit that a frame must traverse on a basis of a series of decisions. 

In the server, the OS decides the Ethernet interface from which to send the frame. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

During service profile configuration, you can select the fabric interconnect to be associated with a vNIC. You can also choose whether fabric failover is enabled for the vNIC. If fabric failover is enabled, the vNIC can access the second fabric interconnect when the default fabric interconnect is unavailable. Cisco UCS Manager Server Management Guide provides more details about vNIC configuration during service profile creation. 

* * *  
  
---|---  
  
After the host vNIC is selected, the frame exits the selected vNIC and, through the host interface port (HIF), enters the IOM to which the vNIC is pinned. The frame is then forwarded to the corresponding network Interface port (NIF) and then to the Fabric Interconnect to which the IOM is pinned. 

The NIF is selected based on the number of physical connections between the IOM and the Fabric Interconnect, and on the server ID from which the frame originated. 

---

## Page 14: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_4_3/b_UCSM_CLI_Infrastructure_Management_Guide_chapter_01100.html

## Recovering the Corrupt BIOS on a Blade Server 

On rare occasions, an issue with a blade server may require you to recover the corrupted BIOS. This procedure is not part of the normal maintenance of a server. After you recover the BIOS, the blade server boots with the running version of the firmware for that server. 

### Before you begin

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

Remove all attached or mapped USB storage from a server before you attempt to recover the corrupt BIOS on that server. If an external USB drive is attached or mapped from vMedia to the server, BIOS recovery fails. 

* * *  
  
---|---  
  
### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope server ` ` chassis-id / server-id |  Enters chassis server mode for the specified blade server in the specified chassis.   
**Step 2** |  UCS-A /chassis/server #  recover-bios ` ` version |  Loads and activates the specified BIOS version.   
**Step 3** |  UCS-A /chassis/server #  commit-buffer |  Commits the transaction.   
  
### Example

The following example shows how to recover the BIOS: 
    
    
    UCS-A# **scope server 1/7**
    UCS-A /chassis/server # **recover-bios S5500.0044.0.3.1.010620101125**
    UCS-A /chassis/server* # **commit-buffer**
    UCS-A /chassis/server # 
    

---

## Page 15: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_chapter_0111.html

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

## Page 16: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_chapter_01000.html

## Blade Server Management   
  
You can manage and monitor all blade servers in a Cisco UCS domain through Cisco UCS Manager. You can perform some blade server management tasks, such as changes to the power state, from the server and service profile. 

The remaining management tasks can only be performed on the server. 

The power supply units go into power save mode when a chassis has two blades or less. When a third blade is added to the chassis and is fully discovered, the power supply units return to regular mode. 

If a blade server slot in a chassis is empty, Cisco UCS Manager provides information, errors, and faults for that slot. You can also re-acknowledge the slot to resolve server mismatch errors and to have Cisco UCS Manager rediscover the blade server in the slot. 

---

## Page 17: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_chapter_01110.html

## Cisco UCS Manager User CLI Documentation

Cisco UCS Manager offers you a new set of smaller, use-case based documentation described in the following table: 

Guide  |  Description   
---|---  
[Cisco UCS Manager Getting Started Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses Cisco UCS architecture and Day 0 operations, including Cisco UCS Manager initial configuration, and configuration best practices.   
[Cisco UCS Manager Administration Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses password management, role-based access configuration, remote authentication, communication services, CIMC session management, organizations, backup and restore, scheduling options, BIOS tokens and deferred deployments.   
[Cisco UCS Manager Infrastructure Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses physical and virtual infrastructure components used and managed by Cisco UCS Manager.   
[Cisco UCS Manager Firmware Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses downloading and managing firmware, upgrading through Auto Install, upgrading through service profiles, directly upgrading at endpoints using firmware auto sync, managing the capability catalog, deployment scenarios, and troubleshooting.   
[Cisco UCS Manager Server Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses the new licenses, registering Cisco UCS domains with Cisco UCS Central, power capping, server boot, server profiles and server-related policies.   
[Cisco UCS Manager Storage Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses all aspects of storage management such as SAN and VSAN in Cisco UCS Manager.   
[Cisco UCS Manager Network Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses all aspects of network management such as LAN and VLAN connectivity in Cisco UCS Manager.   
[Cisco UCS Manager System Monitoring Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses all aspects of system and health monitoring including system statistics in Cisco UCS Manager.   
[Cisco UCS S3260 Server Integration with Cisco UCS Manager](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html) |  Discusses all aspects of management of UCS S-Series servers that are managed through Cisco UCS Manager. 

---

## Page 18: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_chapter_011.html

## Chassis/FEX Discovery Policy   
  
The chassis/FEX discovery policy determines how the system reacts when you add a new chassis or FEX. Cisco UCS Manager uses the settings in the chassis/FEX discovery policy to determine the minimum threshold for the number of links between the chassis or FEX and the fabric interconnect and whether to group links from the IOM to the fabric interconnect in a fabric port channel. 

In a Cisco UCS Mini (Cisco UCS 6324 Fabric Interconnect) setup, chassis discovery policy is supported only on the extended chassis. 

### Chassis Links

If you have a Cisco UCS domain with some of the chassis' wired with one link, some with two links, some with four links, and some with eight links, Cisco recommends configuring the chassis/FEX discovery policy for the minimum number links in the domain so that Cisco UCS Manager can discover all chassis. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/tip.gif)  
**Tip** | 

* * *

To establish the highest available chassis connectivity in a Cisco UCS domain where Fabric Interconnect is connected to different types of IO Modules supporting different max number of uplinks, select platform max value. Setting the platform max ensures that Cisco UCS Manager discovers the chassis including the connections and servers only when the maximum supported IOM uplinks are connected per IO Module. 

* * *  
  
---|---  
  
After the initial discovery of a chassis, if chassis/FEX discovery policy changes are done, acknowledge IO Modules rather than the entire Chassis to avoid disruption. The discovery policy changes can include increasing the number of links between Fabric Interconnect and IO Module, or changes to the Link Grouping preference. 

Make sure that you monitor for faults before and after the IO Module acknowledgement to ensure that the connectivity is restored before proceeding to the other IO Module for the chassis. 

Cisco UCS Manager cannot discover any chassis that is wired for fewer links than are configured in the chassis/FEX discovery policy. For example, if the chassis/FEX discovery policy is configured for four links, Cisco UCS Manager cannot discover any chassis that is wired for one link or two links. Re-acknowledgement of the chassis resolves this issue. 

The following table provides an overview of how the chassis/FEX discovery policy works in a multi-chassis Cisco UCS domain: 

Table 1. Chassis/FEX Discovery Policy and Chassis Links Number of Links Wired for the Chassis  | 1-Link Discovery Policy  | 2-Link Discovery Policy  | 4-Link Discovery Policy  | 8-Link Discovery Policy  | Platform-Max Discovery Policy   
---|---|---|---|---|---  
**1 link between IOM and fabric interconnects** |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 1 link.  |  Chassis connections and servers cannot be discovered by Cisco UCS Manager and are not added to the Cisco UCS domain.  |  Chassis connections and servers cannot be discovered by Cisco UCS Manager and are not added to the Cisco UCS domain.  |  Chassis connections and servers cannot be discovered by Cisco UCS Manager and are not added to the Cisco UCS domain.  |  Chassis connections and servers cannot be discovered by Cisco UCS Manager and are not added to the Cisco UCS domain.   
**2 links between IOM and fabric interconnects** |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 1 link.  After initial discovery, reacknowledge the chassis and Cisco UCS Manager recognizes and uses the additional links.  |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 2 link.  |  Chassis connections and servers cannot be discovered by Cisco UCS Manager and are not added to the Cisco UCS domain.  |  Chassis connections and servers cannot be discovered by Cisco UCS Manager and are not added to the Cisco UCS domain.  |  Chassis connections and servers cannot be discovered by Cisco UCS Manager and are not added to the Cisco UCS domain.   
**4 links between IOM and fabric interconnects** |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 1 link.  After initial discovery, reacknowledge the chassis and Cisco UCS Manager recognizes and uses the additional links.  |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 2 links.  After initial discovery, reacknowledge the chassis and Cisco UCS Manager recognizes and uses the additional links.  |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 4 link.  |  Chassis connections and servers cannot be discovered by Cisco UCS Manager and are not added to the Cisco UCS domain.  |  If the IOM has 4 links, the chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 4 links.  |  **Note** |  If the FEX status shows accessibility problem then reacknowledge the chassis after decommissioning/recommissioning FEX.  
---|---  
  
If the IOM has 8 links, the chassis is not fully discovered by Cisco UCS Manager.   
  
**8 links between IOM and fabric interconnects** |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 1 link.  After initial discovery, reacknowledge the chassis and Cisco UCS Manager recognizes and uses the additional links.  |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 2 links.  After initial discovery, reacknowledge the chassis and Cisco UCS Manager recognizes and uses the additional links.  |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 4 links.  After initial discovery, reacknowledge the chassis and Cisco UCS Manager recognizes and uses the additional links.  |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 8 links.  |  Chassis is discovered by Cisco UCS Manager and added to the Cisco UCS domain as a chassis wired with 8 links.   
  
### Link Grouping

For hardware configurations that support fabric port channels, link grouping determines whether all of the links from the IOM to the fabric interconnect are grouped in to a fabric port channel during chassis discovery. If the link grouping preference is set to Port Channel, all of the links from the IOM to the fabric interconnect are grouped in a fabric port channel. If set to None, links from the IOM are pinned to the fabric interconnect. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Important** | 

* * *

For Cisco UCS X-Series Direct, Cisco UCS 6500 Series Fabric Interconnects, Cisco UCS 6400 Series Fabric Interconnect, the link grouping preference is always set to Port Channel. 

* * *  
  
---|---  
  
After a fabric port channel is created through Cisco UCS Manager, you can add or remove links by changing the link group preference and re-acknowledging the chassis, or by enabling or disabling the chassis from the port channel. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The link grouping preference only takes effect if both sides of the links between an IOM and IFM (IOM for Cisco UCS X-Series Servers) or FEX and the fabric interconnect support fabric port channels. If one side of the links does not support fabric port channels, this preference is ignored and the links are not grouped in a port channel. 

* * *  
  
---|---  
  
### Multicast Hardware Hash

In a port channel, by default, ingress multicast traffic on any port in the fabric interconnect (FI) selects a particular link between the IOM and the fabric interconnect to egress the traffic. To reduce potential issues with the bandwidth, and to provide effective load balancing of the ingress multicast traffic, hardware hashing is used for multicast traffic. When multicast hardware hashing is enabled, all links between the IOM and the fabric interconnect in a port channel can be used for multicast traffic. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCS X-Series Direct, Cisco UCS 6500 Series Fabric Interconnects, andCisco UCS 6400 Series Fabric Interconnect do not support multicast hardware hashing. 

* * *  
  
---|---  
  
### Pinning

Pinning in Cisco UCS is only relevant to uplink ports. If you configure Link Grouping Preference as None during chassis discovery, the IOM forwards traffic from a specific server to the fabric interconnect through its uplink ports by using static route pinning. 

The following table showcases how pinning is done between an IOM and the fabric interconnect based on the number of active fabric links between the IOM and the fabric interconnect. 

Table 2. Pinning on an IOM Number of Active Fabric Links  |  Server slot pinned to fabric link   
---|---  
1-Link  |  All the HIF ports are pinned to the active link   
2-Link  |  1,3,5,7 to link-1  2,4,6,8 to link-2   
4-Link  |  1,5 to link-1  2,6 to link-2  3,7 to link-3  4,8 to link-4   
8-Link (Applies only to 2208XP )  |  1 to link-1  2 to link-2  3 to link-3  4 to link-4  5 to link-5  6 to link-6  7 to link-7  8 to link-8   
  
Only 1,2,4 and 8 links are supported. 3,5,6, and 7 links are not valid configurations. 

### Port-Channeling

While pinning traffic from a specific server to an uplink port provides you with greater control over the unified fabric and ensures optimal utilization of uplink port bandwidth, it could also mean excessive traffic over certain circuits. This issue can be overcome by using port channeling. Port channeling groups all links between the IOM and the fabric interconnect into one port channel. The port channel uses a load balancing algorithm to decide the link over which to send traffic. This results in optimal traffic management. 

Cisco UCS supports port-channeling only through the Link Aggregation Control Protocol (LACP). For hardware configurations that support fabric port channels, link grouping determines whether all of the links from the IOM to the fabric interconnect are grouped into a fabric port channel during chassis discovery. If the Link Grouping Preference is set to Port Channel, all of the links from the IOM to the fabric interconnect are grouped in a fabric port channel. If this parameter is set to None, links from the IOM to the fabric interconnect are not grouped in a fabric port channel. 

Once a fabric port channel is created, links can be added or removed by changing the link group preference and reacknowledging the chassis, or by enabling or disabling the chassis from the port channel. 

### Configuring the Chassis/FEX Discovery Policy 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

In a setup with Cisco UCS 6400 Series Fabric Interconnects, the Link Grouping Preference value for Chassis/FEX Discovery Policy is not user configurable. The value is set to Port Channel. 

* * *  
  
---|---  
  
#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope org / |  Enters the root organization mode.  |  **Note** |  The chassis/FEX discovery policy can be accessed only from the root organization.   
---|---  
**Step 2** |  UCS-A /org #  scope chassis-disc-policy |  Enters organization chassis/FEX discovery policy mode.   
**Step 3** |  UCS-A /org/chassis-disc-policy #  set action ` `{1-link | 2-link | 4-link | 8-link | platform-max}  |  Specifies the minimum threshold for the number of links between the chassis or FEX and the fabric interconnect.   
**Step 4** |  (Optional) UCS-A /org/chassis-disc-policy # set descr ` ` description | (Optional)  Provides a description for the chassis/FEX discovery policy.  |  **Note** |  If your description includes spaces, special characters, or punctuation, you must begin and end your description with quotation marks. The quotation marks will not appear in the description field of any  show command output.   
---|---  
**Step 5** |  UCS-A /org/chassis-disc-policy #  set link-aggregation-pref ` `{none | port-channel}  |  Specifies whether the links from the IOMs or FEXes to the fabric interconnects are grouped in a port channel.  |  **Note** |  The link grouping preference only takes effect if both sides of the links between an IOM and IFM (IOM for Cisco UCS X-Series Servers) or FEX and the fabric interconnect support fabric port channels. If one side of the links does not support fabric port channels, this preference is ignored and the links are not grouped in a port channel.   
---|---  
**Note** |  For UCS manager to discover VIC 1455 and VIC 1457, Link Grouping Preference must be configured as Port Channel.   
---|---  
**Step 6** |  UCS-A /org/chassis-disc-policy # set multicast-hw-hash {disabled | enabled}  |  Specifies whether the all the links between the IOM and the fabric interconnect in a port channel can be used for multicast traffic. 

  * disabled —Only one link between the IOM and the fabric interconnect is used for multicast traffic 
  * enabled —All links between the IOM and the fabric interconnect can be used for multicast traffic 

  
**Step 7** |  (Optional) UCS-A /org/chassis-disc-policy #  set qualifier ` ` qualifier | (Optional)  Uses the specified server pool policy qualifications to associate this policy with a server pool.   
**Step 8** |  UCS-A /org/chassis-disc-policy #  commit-buffer |  Commits the transaction to the system configuration.   
  
#### Example

The following example scopes to the default chassis/FEX discovery policy, sets it to discover chassis with four links to a fabric interconnect, provides a description for the policy, specifies the server pool policy qualifications that will be used to qualify the chassis, and commits the transaction: 
    
    
    UCS-A# **scope org /**
    UCS-A /org # **scope chassis-disc-policy**
    UCS-A /org/chassis-disc-policy* # **set action 4-link**
    UCS-A /org/chassis-disc-policy* # **set descr "This is an example chassis/FEX discovery policy."**
    UCS-A /org/chassis-disc-policy* # **set qualifier ExampleQual**
    UCS-A /org/chassis-disc-policy* # **commit-buffer**
    UCS-A /org/chassis-disc-policy # 
    
    
    

The following example scopes to the default chassis/FEX discovery policy, sets it to discover chassis with eight links to a fabric interconnect, provides a description for the policy, sets the link grouping preference to port channel, specifies the server pool policy qualifications that will be used to qualify the chassis, and commits the transaction: 
    
    
    UCS-A# **scope org /**
    UCS-A /org # **scope chassis-disc-policy**
    UCS-A /org/chassis-disc-policy* # **set action 8-link**
    UCS-A /org/chassis-disc-policy* # **set descr "This is an example chassis/FEX discovery policy."**
    UCS-A /org/chassis-disc-policy* # **set link-aggregation-pref port-channel**
    UCS-A /org/chassis-disc-policy* # **set qualifier ExampleQual**
    UCS-A /org/chassis-disc-policy* # **commit-buffer**
    UCS-A /org/chassis-disc-policy # 
    
    
    

The following example scopes to the default chassis/FEX discovery policy, sets it to discover chassis with four links to a fabric interconnect, provides a description for the policy, sets the link grouping preference to port channel, enables multicast hardware hashing, specifies the server pool policy qualifications that will be used to qualify the chassis, and commits the transaction: 
    
    
    UCS-A# scope org /
    UCS-A /org # scope chassis-disc-policy
    UCS-A /org/chassis-disc-policy* # set action 4-link
    UCS-A /org/chassis-disc-policy* # set descr "This is an example chassis/FEX discovery
    policy."
    UCS-A /org/chassis-disc-policy* # set link-aggregation-pref port-channel
    UCS-A /org/chassis-disc-policy* # set multicast-hw-hash enabled
    UCS-A /org/chassis-disc-policy* # set qualifier ExampleQual
    UCS-A /org/chassis-disc-policy* # commit-buffer
    UCS-A /org/chassis-disc-policy #
    
    

#### What to do next

To customize fabric port channel connectivity for a specific chassis, configure the chassis connectivity policy. 

---
