# Intersight SaaS Device Console

| | |
|---|---|
| **URL Title** | Intersight SaaS Device Console |
| **URL** | https://intersight.com/help/saas/device_console |
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260316155144543/docs/cloud/data/articles/device_console/en/index.html |
| **HTML Title** | Device Console |
| **Source file** | `ucs-docs-raw/html/intersight-saas_device_console.html` |
| **File type** | HTML |
| **Fetched on** | 2026-03-19 16:46:51 |

---

# Device Console

## Overview

The Device Console is a user interface that provides a limited ability to manage the system, even when Intersight is not connected. The Device Console provides both a Command-Line Interface (CLI) and a Web User Interface (UI) and can connect remotely to:

  * Edge Chassis Management Controllers (eCMC) of Unified Edge chassis

  * Fabric Interconnects (FI) of Intersight Managed Mode domains


Note:

This page describes the Unified Edge Device Console and the FI Device Console. Most of the user interface is the same; any differences are specifically highlighted.

This interface provides system information, including the model, serial number, and firmware version of the Unified Edge or Fabric Interconnects. It facilitates Device Connector configuration. Inventory details for Fabric Extenders (for FIs only), Servers, and Chassis are displayed. Additionally, tech support bundles containing diagnostic information can be generated for troubleshooting and analysis, and power and LED operations for servers are supported.

## Accessing the Device Console (Unified Edge)

**Obtaining an IP Address for eCMC (Unified Edge)**

  1. The eCMC will automatically set its hostname to `UCSXE-<serial number>-<A|B>`.

  2. The eCMC will first attempt to obtain an IP address via DHCP on its management port.

  3. If Dynamic DNS (DDNS) is configured, the IP address will be accessible via `https://<hostname>`.

  4. Link-Local Fallback (if DHCP fails):

  * If a DHCP server is not present, or if a network failure is detected (defined as 5 or more pings failing within 30 seconds), the eCMC will fall back to a link-local IP address.

  * eCMC A will assign itself `169.254.254.1`

  * eCMC B will assign itself `169.254.254.2`

  * This fallback typically occurs 30-90 seconds after network failure detection


**Connecting to the eCMC**

  1. If DHCP is used, check the DHCP server logs or interface to find the IP address assigned to the eCMC, using its hostname `(UCSXE-<serial number>-<A|B)`

.
  2. If DDNS is configured, access the eCMC using `https://<hostname>`

.
  3. If the eCMC has fallen back to a link-local IP address (For example, due to no DHCP or network failure), you will need to:

     1. Connect a laptop directly to the management port of the eCMC.

     2. Configure the laptop's network adapter with an IP address in the same `169.254.254.x` subnet (e.g., `169.254.254.3`) to access the device UI via the eCMC's link-local IP.


## Logging in to Device Console and Resetting Default Password

  1. To log in to the Device Console for the first time, use the default credentials—admin as the username and password as the password.

  2. Reset the default password:

     1. Enter a new username and select a new role.

     2. Do one of these:

  * To have a password generated automatically, enable Generate Password.

  * To set your own password, enter a new password.

     3. Save the password and then click Submit.

Note:

The password cannot be recovered after you click Submit. If the password is lost, a factory reset will be required to regain access.

  3. Log in using the updated credentials and verify access to the Device Console tabs.


## User Interface of Device Console (Unified Edge)

The Device Console UI consists of the following main elements:

  * A central pane that includes the following tabs:

  * [Device Connector](/help/device_console#device_connector)

  * [System Information](/help/device_console#system_information_\(unified_edge\))

  * [Network Settings](/help/device_console#network_settings_\(unified_edge\))

  * [Inventory](/help/device_console#inventory_\(unified_edge\))

  * [Diagnostic Data](/help/device_console#diagnostic_data_\(unified_edge\))

  * A top navigation menu that contains the Help menu and Logout button.


## Device Connector

Note:

This section is common for Unified Edge and FIs.

The Device Connector is an embedded management controller that enables secure communication between the system and Cisco Intersight.

When enabled, devices can be claimed, and Intersight can be used for managing and monitoring the devices.

The following table describes the parameters shown on the Device Connector tab.

Property| Description  
---|---  
Device Connector| Displays the following:

  * The Access Mode of the Device Connector.
  * The status of the connection between the Device Connector, the Internet, and Cisco Intersight.
  * The claim status of the device.

  
Settings| Click Settings to configure the Device Connector settings to enable the capabilities of Cisco Intersight.For more information, see [Configuring Device Connector](/help/resources/configuring_device_connector).  
Refresh| Click Refresh to update the displayed information.  
Device ID| Displays the unique serial number of the device.  
Claim Code| Displays the claim code of the device.  
Claimed to Account| Displays the ID of the Intersight user who claimed the device.  
Unclaim| Click Unclaim to unclaim a device.Use the Unclaim option on the Device Connector only when access to the original claiming account is unavailable, or when Intersight connectivity is lost and unclaiming locally from the endpoint is required. For more details on unclaiming a target see [Unclaim Target](/help/getting_started/claim_targets#unclaim_targets).  
  
## System Information (Unified Edge)

The System Information tab displays the system information for two Edge Chassis Management Controllers designated Edge Chassis Management Controller A and Edge Chassis Management Controller B.

The following table describes the parameters shown on the System Information tab.

Parameter| Description  
---|---  
Edge Chassis Management Controller A / B| Identifies two distinct eCMCs within a Unified Edge Chassis. They are typically redundant components for high availability.  
Hostname| Displays the unique network name assigned to each eCMC for identification.  
Slot number| Displays thephysical slot or position where the eCMC is installed within the chassis.  
Health| Displays the current operational status of the eCMC. Healthy indicates that the eCMC is functioning correctly. The other states are Warning and Critical.  
Management IPs| Displays theIP address for network access, configuration, monitoring, and control of the eCMC.  
Firmware Version| Displays the version of the firmware running on the eCMC.  
Hardware Version| Displays theversion of the eCMC hardware.  
Serial Number| Displays theHost ID/serial number of the eCMC.  
Model| Displays the Product ID (PID) identifying the eCMC model.  
  
## Network Settings (Unified Edge)

The current network settings for each eCMC is displayed on Network Settings.

The following table describes the parameters shown on the Network Settings tab.

Parameter| Description  
---|---  
Edge Chassis Management Controller A / B| Identifies two distinct eCMCs within a Unified Edge Chassis. They are typically redundant components for high availability.  
IPv4/IPv6| Displays the IP protocol type:

  * Static: When the IP addresses are configured to be manually assigned.
  * DHCP: When the IP address are configured to be automatically assigned from the DHCP server.The DHCP configuration will be applied to both Edge Chassis Management Controller A and Edge Chassis Management Controller B.

  
Hostname| Displays the unique network name assigned to each eCMC for identification.  
Management IP| Displays theIP address for network access, configuration, monitoring, and control of the eCMC.  
Gateway IP| Displays the IP address of the router or device that serves as a default gateway for traffic leaving the local network segment.  
Subnet Mask| Displays the IP address that defines the network portion of an IP address and separates it from the host portion.  
Prefix Length| Displays the number that indicates the number of bits in the network portion of an IP address.  
DNS IP| Displays the IP address of the Domain Name System server, which translates domain names into IP addresses.  
NTP IP/Domain Name| Displays the IP address or domain name of the Network Time Protocol server, used for synchronizing the device's clock.  
  
For configuration details, see Configuring Network Settings.

Configuring Network Settings

When a DHCP server is available, it can be configured to automatically assign the DNS server and NTP server IP addresses. For manual network configuration, click Edit and adjust settings according to the network requirements.

Note:

Any changes made to the network settings will be applied to both eCMC A and eCMC B.

To configure the network settings:

  1. Go to Device Console > Network Settings tab.

The current network settings are displayed.

  2. Click Edit.

  3. To configure the hostname:

  * In the Hostname field, update the hostname of the Unified Edge device to uniquely identify the device within the network.

  * The suffix -A or -B will be automatically appended to the hostname for each eCMC. (e.g., If you type EdgeDevice, it becomes EdgeDevice-A for eCMC A and EdgeDevice-B for eCMC B).

  4. To configure the DNS:

  * In the DNS IP field, configure the IP address for the DNS server.

  * You can configure up to four DNS IPs.

  * DNS IP can be IPv4 or IPv6 addresses.

  5. To configure NTP Server for time synchronization:

  * In the NTP IP/Hostname field, configure the IP address for the NTP server.

  * You can configure up to four NTP servers.

  * NTP IP can be hostname, IPv4, or IPv6 addresses.

  6. Enable and configure IPv4 and/or IPv6 addressing and choose one of the following options for IP assignment:

  * DHCP: Obtain IP addresses automatically from the DHCP server.

The DHCP configuration will be applied to both Edge Chassis Management Controller A and Edge Chassis Management Controller B.

  * Static: Manually configure IP addresses for the Management IP, Gateway IP, Subnet Mask (for IPv4), and Prefix Length (for IPv6).

  7. Click Save.


## Inventory (Unified Edge)

Inventory provides detailed inventory information for the Unified Edge servers and chassis.

**Servers Tab**

The Servers tab provides detailed information about the servers connected to the Unified Edge chassis. This information is based on the live data obtained from the Unified Edge chassis.

Details| Description  
---|---  
Name| Displays the name of the server, with a prefixed icon indicating whether the server is powered on or off.  
Status| Displays the lifecycle state of the server. The values can be:

  * None — When the server has been recommissioned but discovery is yet to start.
  * Active — When the server is discovered.
  * Decommissioned — When the server is removed from the Unified Edge chassis.
  * DiscoveryFailed — When the server discovery has failed.
  * SlotMismatch — When the configuration of a blade server is not correct and server rediscovery is required in the slot.

  
PID| Displays the Product ID (PID) of the server.  
Serial| Displays the host ID/serial number of the server.  
Server Profile| Displays the server profile that is associated with the server.  
User Label| Displays the user label that is set for the server.  
  
The following server actions are available:

  * Power On/Off

  * Launch KVM

  * Generate Tech Support Bundle

The resulting Tech Support Bundles can be downloaded from the Diagnostic Data tab.

  * Locator LED On/Off


**Chassis Tab**

The Chassis tab provides detailed information about the connected Unified Edge chassis.

Details| Description  
---|---  
Name| Displays the name for the chassis.  
ID| Displays the unique ID for the chassis.  
Status| Displays the status of the chassis. The values can be:

  * Active — When the chassis is discovered.
  * Decommissioned —When the Chassis is physically present and connected.
  * DiscoveryFailed — When the chassis discovery has failed.

  
Model| Displays the chassis model.  
Serial| Displays the host ID/serial number of the chassis.  
  
## Diagnostic Data (Unified Edge)

From the Diagnostic Data tab, you can collect diagnostic data for servers and Edge Chassis Management Controller (eCMC) for troubleshooting and further analysis.

**Tech Support Bundles**

You can generate tech support bundles for the following:

  * eCMC: Contains technical support data for eCMC A and eCMC B.

  * Server: Contains technical support data for Unified Edge servers.


**Generating and downloading tech support bundles**

To generate and download a tech support bundle:

  1. Log in to Device Console.

  2. Go to Diagnostic Data.

  3. Click Generate Tech Support Bundle.

  4. In the Generate Tech Support Bundle dialog box:

     1. To generate the relevant tech support bundles, from the Device Type drop-down, select Edge Chassis Management Controller or Server.

     2. Select the device for which the tech support bundle needs to be generated.

     3. Click Generate to initiate the process.

Monitor the tech support bundle generation status in the Oper State column. Upon completion, the status will update from In Progress to Available.

     4. To download the bundle, click ellipsis (...) next to the bundle, then select Download.

This operation may take several minutes to complete. The downloaded file is saved in the default download location.

     5. To delete any bundle, click ellipsis (...) next to the bundle, then select Delete.


## Administration (Unified Edge)

Account lockout is a security feature that monitors consecutive incorrect login attempts for an account. This feature helps to keep the account secure by slowing down unauthorized access attempts. When the maximum allowed number of consecutive incorrect login attempts is reached, the account locks for the configured lockout duration. After this lockout duration, the account automatically unlocks. The count of incorrect attempts resets after the lockout duration.

Note:

The account lockout feature cannot be disabled.

**Configure the account lockout settings**

  1. Log in to the Device Console.

  2. Select the Administration tab.

  3. Review the current account lockout configuration.

  * Allowed Attempts: The number of consecutive incorrect login attempts that will lock the account. The default value is 5.

  * Lockout Period (minutes): The duration the account remains locked after reaching the maximum number of consecutive incorrect login attempts. The default value is 15.

  4. Select Edit.

  5. Perform these substeps on the Account Lockout page.

     1. Enter the number of Allowed Attempts. The valid range is from 1 to 20.

     2. Enter the Lockout Period in minutes. The valid range is from 1 to 60.

  6. Select Save.


## Accessing the Device Console (Fabric Interconnects)

To access the Device Console user interface, log in to the Fabric Interconnect using a management IP address or DNS hostname if available. Administrator privileges are required to access Device Console UI.

You can also log into the Device Console of a Fabric Interconnect in Intersight Managed Mode using your enterprise LDAP account. To enable LDAP authentication attach the following policies:

  * An LDAP policy for HTTP and SSH access.

  * Certificate Management policy (optional) for secure access.


For more information, see the Creating an LDAP Policy and Creating a Certificate Management Policy sections in [Configuring Domain Policies](/help/resources/cisco_intersight_managed_mode_configuration#configuring_ucs_domain_policies).

## User Interface of Device Console (Fabric Interconnects)

The FI Device Console UI consists of the following main elements:

  * A central pane that includes four tabs:

  * [System Information](/help/device_console#system_information_\(fabric_interconnects\))

  * [Device Connector](/help/device_console#device_connector) (Common)

  * [Inventory](/help/device_console#inventory_\(fabric_interconnects\))

  * [Diagnostic Data](/help/device_console#diagnostic_data_\(fabric_interconnect\))

  * A top navigation menu that contains the Help menu and Logout button.


## Device Connector (Fabric Interconnects)

This tab is common for FI and Unified Edge. For more information, see [Device Connector](/help/device_console#device_connector).

## System Information (Fabric Interconnects)

The following table describes the system information parameters.

Details| Description  
---|---  
Management IPs| Displays the Cisco UCS management IP address.  
Model| Displays the Cisco UCS Fabric Interconnect series model.  
Serial| Displays the host ID/serial number of the server.  
Firmware Version| Displays the current firmware version running on the Fabric Interconnect.  
Available Memory| Displays the available memory.  
Total Memory| Displays the total allocated memory.  
  
## Inventory (Fabric Interconnects)

The Inventory screen provides comprehensive details for managed components within its subtabs. These subtabs (except PCIe Nodes) also provide access to the API Explorer, enabling you to perform Redfish™-based operations such as power cycling and retrieving BIOS tokens.

**Subtabs of the Inventory screen:**

  * Servers

  * Chassis

  * Fabric Extender (applies to Fabric Interconnects only)

  * PCIe Nodes


**Servers Tab**

The Servers tab provides detailed information about all the servers connected through the Fabric Interconnect. This information is based on the data stored in the local database on the Fabric Interconnect.

Details| Description  
---|---  
Name| Displays the name of the server, with a prefixed icon indicating whether the server is powered on or off.  
Status| Displays the lifecycle state of the server. The values can be:

  * None: When the server has been recommissioned but discovery is yet to start.
  * Active: When the server is discovered.
  * Decommissioned: When the server is removed from the Cisco UCS configuration. However, the server hardware physically remains in the Cisco UCS instance.
  * DiscoveryFailed: When the server discovery has failed.
  * SlotMismatch: When the configuration of a blade server is not correct and server rediscovery is required in the slot.

  
PID| Displays the Product ID (PID) of the server.  
Serial| Displays the host ID/serial number of the server.  
Server Profile| Displays the server profile that is associated with the server.  
User Label| Displays the user label that is set for the server.  
  
You can perform the following server actions:

  * Power On/Off

  * Turn On Locator

  * Launch KVM

  * Launch IMC

Note:

Minimum C-Series IMM server firmware version required for launching IMC: 4.3(6.250039).

  * Launch API Explorer

  * Generate Tech Support Bundle

Note:

The resulting Tech Support Bundles can be downloaded from the Diagnostic Data tab.


Performing Redfish™ Based Server Operations from the API Explorer.

Redfish ™ Based Server Operations - Examples.

For an overview of Redfish™ based server operations and examples, see <https://intersight.com/apidocs/introduction/overview/>.

**Launching the API Explorer**

To perform Redfish™ Based server operations from the API Explorer, do the following:

  1. On the Servers table view, select the server and click the ellipsis (…).

  2. From the ellipsis (…), select Launch API Explorer.


**Chassis Tab**

The Chassis subtab provides detailed information about all the chassis connected through the Fabric Interconnect.

Details| Description  
---|---  
Name| Displays the name for the chassis.  
ID| Displays the unique ID for the chassis.  
Status| Displays the status of the chassis. The values can be:

  * Active: When the chassis is discovered.
  * Decommissioned: When the Chassis is physically present and connected, but temporarily removed from the Cisco UCS configuration.
  * DiscoveryFailed: When the chassis discovery has failed.

  
Model| Displays the chassis model.  
Serial| Displays the host ID/serial number of the chassis.  
  
You can perform the following chassis operations:

  * Launch API Explorer (IOM 1)

  * Launch API Explorer (IOM 2)

  * Generate Tech Support Bundle


Performing Redfish™ Based Chassis Operations from the API Explorer

Redfish™ Based Chassis Operations - Examples.

For an overview of Redfish™ based chassis operations and examples, see <https://intersight.com/apidocs/introduction/overview/>.

**Launching the API Explorer**

To perform Redfish™ Based chassis operations from the API Explorer, do the following:

  1. On the Chassis table view, select the chassis and click the ellipsis (…).

  2. From the ellipsis (…), select Launch API Explorer.


**Fabric Extender Tab**

The Fabric Extender subtab provides detailed information about all the Fabric Extender (FEX) connected through the Fabric Interconnect.

Details| Description  
---|---  
Name| Displays the name for the FEX.  
Identifier| Displays the unique ID for the FEX.  
Lifecycle| Displays the current state of the FEX lifecycle. The values can be:

  * Online: When the FEX is connected.
  * Decommissioned: When the FEX is physically present and connected, but temporarily removed from the Cisco UCS configuration.
  * Unclaimed: When the FEX has not been claimed to the Intersight account.
  * Discovery Failure: When the discovery of FEX has failed.

  
Model| Displays the FEX model.  
Serial| Displays the host ID/serial number of the FEX.  
Description| Displays the description for the FEX, if any.  
  
**PCIe Nodes Tab**

The PCIe Nodes subtab provides detailed information about all the PCIe Node connected through the Fabric Interconnect.

Details| Description  
---|---  
Name| Displays the name for the FEX.  
Status| Displays the status of the PCIe node. The values can be:

  * Active: When the PCIe node is discovered.
  * Decommissioned: When the PCIe node is physically present and connected, but temporarily removed from the Cisco UCS configuration.
  * DiscoveryFailed: When the PCIe node discovery has failed.

  
Model| Displays the hardware model of the PCIe node.  
Serial| Displays the host ID/serial number of the PCIe node.  
Address| Display the network address assigned to the PCIe node.  
Locator LED| Displays the state of the locator LED of this PCIe node.  
  
We can perform these operation on PCIe node from the Device Console:

  * Turn On/Off Locator

  * Generate Tech Support Bundle


## Diagnostic Data (Fabric Interconnect)

From the Diagnostic Data tab, you can collect diagnostic data for servers, chassis, and Fabric Interconnects for troubleshooting and further analysis.

**Tech Support Bundles**

You can generate tech support bundles for the following:

  * Server: Contains technical support data for blade and rack servers including all adapters. For blade servers, tech support data is collected for IOMs.

  * Chassis: Contains technical support data for a given chassis including IOMs.

  * Fabric Interconnect: Contains technical support data for Fabric Interconnect. The data can be for either the local or both the local and peer switches.

  * PCIe Node: Contains technical support data for PCIe nodes.


**Generating and Downloading Tech Support Bundles**

To generate and download a tech support bundle:

  1. Log in to Device Console.

  2. Go to Diagnostic Data > Tech Support Bundles.

  3. Click Generate Tech Support Bundle in the right side of the screen above the table view.

  4. In the Generate Tech Support Bundle dialog box:

     1. Select a Device Type—Chassis, Fabric Interconnect, Fabric Extenders, Server, or PCIe Node—to generate the corresponding tech support bundle.

     2. If you select Fabric Interconnect as the device type, choose either Local Switch or Local and Peer Switches and proceed to step 4d. Otherwise, continue to the next step.

     3. From the second drop-down menu, select the device for which the tech support bundle needs to be generated.

     4. Click Generate to initiate the process.

You can see the download status for the tech support bundle generation under the Oper State column. Once the generation is complete, the status changes from In Progress to Available.

     5. In the relevant row for the device, from the ellipsis (…), click Download to start the download.

This operation may take several minutes to complete. The downloaded file is saved in your default download location. You can manually delete any file by selecting Delete from the ellipsis (**…**) menu located next to each record.


**Core Files**

Core files get generated on Cisco Integrated Management Controller, Chassis Management Controller, adapters, and switches. You can view, download, and delete the core files from the Device Console interface.

**Downloading Core Files**

To generate and download a core file, do the following:

  1. Log in to Device Console.

  2. Go to Diagnostic Data > Core Files.

  3. In the relevant row for the file, from the ellipsis (…), click Download to start the download

The downloaded file is saved in your default download location.


You can manually delete any file by selecting Delete from the ellipsis (…) menu located next to each record.

For details on the auto-deletion of files, see [Core Files](/help/system/diagnostic_data#core_files).

## Device Console Common CLI Commands

You can use the Device Console CLI interface to troubleshoot the devices, or if the devices are not connecting to Cisco Intersight.

Below are the commands that you can use:

**Device Connector**

These commands relate to the Device Connector component.

Command| Description| Note  
---|---|---  
`**connect device-connector**`|  Connects to the Device Connector through the Intersight CLI shell.| —  
`**show version**`|  Shows the Device Connector version.| —  
`**update-device-connector workspace:/**` | `**volatile:/**` filename| Updates the Device Connector image.Note:Images are generally not accessible to customers. This operation is used by TAC for recovery purpose.| The volatile: option is not available for Unified Edge.  
  
**System Information**

These commands allow you to view general system information.

Command| Description| Note  
---|---|---  
`**show clock**`|  Displays the system date and time.| Setting the time on the FI requires NTP. NTP should be configured in the Device Console and in the NTP Policy of the Domain Profile.  
`**show cli history**`|  Displays the history of CLI commands run in the session.| —  
`**show sshkey**`|  Displays the list of SSH public key of the host.| Not available for Unified Edge.  
`**show mgmt-ip-debug**`|  Displays the IP address and the interfaces on both the management and default namespaces.| Not available for Unified Edge.  
`**show mgmt-ip-tables**`|  Displays the IP table entries on both the management and default namespaces.| Not available for Unified Edge.  
`**show file**` file-path| Displays the contents of a file.| Not available for Unified Edge.  
`**show processes**`|  Displays a list of all processes that are currently running.| Not available for Unified Edge.  
`**show audit**`|  Displays the audit log of the Fabric Interconnect.| —  
`**show self-signed-certificate**`|  Shows self signed certificate.| —  
`**scope**` <scope-name>| Changes scope.| Available only for Unified Edge.  
  
**Servers/Chassis/Switch/eCMC**

These commands enable connecting to and managing the connected components.

Command| Description| Note  
---|---|---  
`**show chassis**` chassis-id| Displays the chassis details including IOM and XFM details.| —  
`**show pcie-node**` chassis-id/slot-id| Displays the PCIe node details.| —  
`**connect iom**` chassis-id| Connects to an IO module or to an Intelligent Fabric module.| Not available for Unified Edge and Cisco UCS X-Series Direct.  
`**connect xfm**` chassis-id/xfm-id| Connects to the X-Fabric module.| —  
`**connect cimc**` chassis-id/blade-id | rack-id | sled-id | chassis id/PCIe-node-id | chassis-id/slot-id| Connects to the CIMC (Cisco Integrated Management Controller).| For C-series servers, use rack-id.For X-series, B-series, and Cisco UCS X-Series Direct, use chassis-id.For Unified Edge, use sled-id.For PCIe node, use chassis-id/ PCIe-node-id or chassis-id/slot-id.  
`**connect adapter**` chassis-id/blade-id/adapter-id | rack-id/adapter-id| Connects to an adapter on B-series, X-series, or C-series servers.| For B-series/X-series servers, use chassis-id/blade-id/adapter-id.For C-series, use rack-id/adapter-id.Not available for Unified Edge.  
`**pcie-node led**` chassis-id/slot-id | on/off| Turns on or off the PCIe node LED locator.| —  
`**pcie-node led-status**` chassis-id/slot-id| Displays the PCIe node LED locator status.| —  
`**reset_all_memory_errors**`|  Clears the memory counters using the reset memory error command.| Not available for Unified Edge.  
`**connect switch**`|  Connect to the switch shell.| —  
`**connect ecmc**` ecmc-id| Connect to the edge chassis management controller.| Available only for Unified Edge.  
  
Note:

The id represents the identification number the component.

**PMON Processes**

Process Monitor (PMON) processes includes all the internal processes associated with the **mgmt plugin**. PMON processes help in restarting the processes during FI recovery/troubleshooting.

These commands enable managing PMON and connector processes.

Command| Description| Note  
---|---|---  
`**pmon**` { `**start**` | `**stop**` | `**state**` } [ `**connector**` ]| Allows you to start, stop, or view the current status of the PMON or connector processes.| Not available for Unified Edge.  
  
**Technical Support**

These commands help in fetching diagnostic data files.

Command| Description| Note  
---|---|---  
`**show-tech-support server**` blade-id | sled-id| Displays the contents of the tech-support bundle for a specific server blade.| For Fabric Interconnects, use blade-id.For Unified Edge, use sled-id.  
`**show tech-support chassis**` chassis-id| Displays the contents of the tech-support bundle for a specific chassis.| Not available for Unified Edge.  
`**show tech-support fex**` fex-id| Displays the contents of the tech-support bundle for a specific FEX.| This command applies only to IMM.Not available for Unified Edge.  
`**show tech-support switch**` switch-id| Displays the contents of the tech-support bundle for a specific switch.| Not available for Unified Edge.  
`**show tech-support pcie-node**` chassis-id/slot-id| Displays the contents of the tech-support bundle for a specific PCIe node.| —  
`**show core-files**`|  Displays the core files.| Not available for Unified Edge.  
  
**Directory Operations**

These commands allow for file system navigation and manipulation within the CLI.

Command| Description| Note  
---|---|---  
`**cd**` { `**workspace:/**` | [path] `**| volatile:/**` | [path] `**|**` | [path] `**| usbdrive1:/ | usbdrive2:/**` }| Changes directory.| The volatile:, usbdrive1:, and usbdrive2: options are not available for Unified Edge.  
`**pwd**`|  Displays the current working directory.| —  
`**Is**`|  Lists the contents of the current working directory.| —  
`**mkdir**` { `**workspace:/**` | [path] `**| volatile:/**` | [path] `**|**` | [path] `**| usbdrive1:/ | usbdrive2:/**` }| Creates a directory under allowed directories.| The volatile:, usbdrive1:, and usbdrive2: options are not available for Unified Edge.  
`**rmdir**` { `**workspace:/**` | [path] `**| volatile:/**` | [path] `**|**` | [path] `**| usbdrive1:/ | usbdrive2:/**` }| Removes the directory.| The volatile:, usbdrive1:, and usbdrive2: options are not available for Unified Edge.  
`**cp**` [from-filesystem:] [from-path] filename [to-filesystem:] to-path [dest-filename]| Copies a file from one directory to another.| —  
`**mv**` [from-filesystem:] [from-path] filename [to-filesystem:] to-path [dest-filename]| Moves a file from one directory to another.| —  
`**rm**` { `**workspace:/**` | [path] `**| volatile:/**` | [path] `**|**` | [path] `**| usbdrive1:/ | usbdrive2:/**` }| Removes a file from a directory.| The volatile:, usbdrive1:, and usbdrive2: options are not available for Unified Edge.  
  
**Other Operations**

These commands cover various networking diagnostics, system management, and configuration tasks.

Command| Description| Note  
---|---|---  
`**set management-network**` ip-address netmask/preix_length gateway| Configures management IP address, network mask, and gateway address on a Fabric Interconnect.| Not available for Unified Edge.  
`**tail-mgmt-log**` module_name| Displays the management log of the services running on a Fabric Interconnect.| —  
`**ssh**` host-name| Logs in to a host that supports SSH.| —  
`**telnet**` host-name [port-num]| Logs in to a host that supports Telnet.| —  
`**traceroute**` [ `**-s**` source-address ] address| Displays the route to an IPv4 network host.| —  
`**traceroute6**` [ `**-s**` source-address ] address| Displays the route to an IPv6 network host.| —  
`**ping**` [ `**-c**` count ] [ `**-s**` packet-size ] [ `**-i**` interval ] [ `**-w**` timeout ] { host-ip-address | | | host-name }| Diagnoses basic network connectivity for IPv4 addresses.| —  
`**ping6**` [ `**-c**` count ] [ `**-s**` packet-size ] [ `**-i**` interval ] [ `**-w**` timeout ] { host-ip-address | | | host-name }| Diagnoses basic network connectivity for IPv6 addresses.| —  
`**reboot**`|  Reboots the system.| —  
`**connect nxos**`|  Connects to NX-OS.| Not available for Unified Edge.  
`**erase-configuration**`|  Erases configuration on the Fabric Interconnect.| Erase configuration will not affect or delete any existing data on the Fabric Interconnect.Not available for Unified Edge.  
`**fi-secure-erase**` [-preserveImage]| Erases all data and configuration on the Fabric Interconnect, run the command.Use the preserveImage flag to keep the system image while deleting all other data from the Fabric Interconnect.| FI Secure Erase may take 20 to 40 minutes to complete.For information on minimum firmware version requirement, see the Firmware Requirements for FI Secure Erase table below.Not available for Unified Edge.  
`**change-password**`|  Changes the administrator password on the Fabric Interconnect.| —  
`**clear-sshkey**` host-name| Clears the SSH public key of a remote host from cache.| Not available for Unified Edge.  
`**change-domain-name**`|  Updates the name of the Fabric Interconnect and the peer FI.| Not available for Unified Edge.  
`**change-mode**`|  Changes the management mode of the server.| Not available for Unified Edge.  
`**clear**`|  Clears the screen.| —  
`**clear-firmware-cache**`|  Clears an entry from the Intersight firmware cache.| —  
`**cluster-start**`|  For initial HA setup, starts cluster server.| The cluster-start command is used in the backend as part of the developer script when adding an FI to a cluster.Not available for Unified Edge.  
`**connect**`|  Connects to an endpoint.| —  
`**generate-self-signed-certificate**`|  Generates a new self-signed certificate.| After generating the self-signed certificate, the command restarts the web server.Not available for Unified Edge.  
`**list-firmware-cache**`|  Displays the list of entries in the Intersight firmware cache.| —  
`**server**`|  Displays the list of server operations and their usage (led-status, power, power-status, led).| Not available for Unified Edge.  
`**update-management-package workspace:/**` | `**volatile:/**` filename| Updates the Device management package on Fabric Interconnect.| Packages are not accessible to the customers. This operation is used by Cisco TAC for recovery purpose.The volatile: option is not available for Unified Edge.  
`**help**`|  Displays help.| —  
`**exit**`|  Exits the program.| —  
`**list-storage-drives**`|  Lists storage drives.| Available only for Unified Edge.  
`**md5sum**`|  Shows MD5 hash of the given file.| Available only for Unified Edge.  
`**top**`|  Changes scope to default scope.| Available only for Unified Edge.  
  
Firmware Requirements for FI Secure Erase

Fabric Interconnect| Minimum Infrastructure Firmware Version  
---|---  
Cisco UCS 6400 Series| 6.0(1.250198)  
Cisco UCS 6500 Series| 6.0(1.250198)  
Cisco UCS 6600 Series| 6.0(1.250198)  
Cisco UCS X-Series Direct| 6.0(1.250198)  
  
## Device Console CLI Commands (Unified Edge)

This section outlines the CLI commands specific to Unified Edge components, categorized by their functional scope.

Note:

The top, exit, clear, and help commands are available across all scopes. For detailed information on their usage, see the Other Operations section on this page.

**Server Configuration Commands**

Command| Description  
---|---  
`**scope servers**`|  Enters server scope.  
`**show servers**`|  Shows the attached server details.  
`**power**` server-id `**on/off**`|  Powers On/Off the server.  
`**show tech-support server**` server-id| Fetchs Tech support files from server.  
  
**Chassis Configuration Commands**

Command| Description  
---|---  
`**scope chassis**`|  Enters chassis scope.  
`**show chassis**`|  Shows chassis details.  
  
**Edge Chassis Management Controller Configuration Commands**

Command| Description  
---|---  
`**scope ecmcs**`|  Enters eCMC scope.  
`**show ecmcs**`|  Shows attached edge chassis management controller details.  
`**reboot**`|  Reboots the current running eCMC system.  
`**factory-reset**`|  Resets both eCMCs to the default factory settings.  
`**show tech-support ecmc**` ecmc-id/full| Fetch Tech support files from eCMCs.  
  
**Firmware Configuration Commands**

Command| Description  
---|---  
`**scope firmware**`|  Enters firmware scope.  
`**clear-firmware-cache**` <IDENTIFIER>| Clears an entry from the Intersight firmware cache.  
`**list-firmware-cache**`|  Lists entries in the Intersight firmware cache.  
`**update-device-connector**` <absolute_file_path>| Updates Device Connector of eCMC.  
`**update-ecmc-firmware**` <absolute_file_path>| Updates eCMC firmware.  
`**update-management-package**` <absolute_file_path>| Updates Management Package of eCMC.  
`**update-server-firmware**` <absolute_file_path>| Updates server firmware.  
`**show version**`|  Displays system version.  
`**show firmware-update-status**` ecmc/server ecmc-id/server-id [detail]| Shows firmware update status.  
`**show firmware-version**` ecmc/server ecmc-id/server-id| Shows firmware version.  
  
**Network Configuration Commands**

Command| Description  
---|---  
`**scope network**`|  Enters network scope.  
`**show management-network**`|  Shows management network configuration.  
`**configure-mgmt-network chassis**`|  Configures management network settings of the chassis.  
`**configure-mgmt-network ecmc**` ecmc-id| Configures eCMC management network configuration.  
  
The ping, ping6, traceroute, traceroute6 commands are supported on Unified Edge. For more information on their usage, see the Other Operations section on this page.

Administration Configuration Commands

Command| Description  
---|---  
`**scope administration**`|  Enters administration scope.  
`**change-password**`|  Changes password of admin user.  
`**tail-mgmt-log**`|  Prints management log of a given module.  
  
**OS Install Configuration Commands**

Command| Description  
---|---  
`**scope osinstall**`|  Enters OS Install scope.  
`**clear-osinstall-cache**` <IDENTIFIER>| Clears an entry from the Intersight OS install cache.  
`**list-osinstall-cache**`|  Lists entries in the Intersight OS install cache.  
  
## Updating eCMC and Server Firmware using CLI (Unified Edge)

The CLI serves as an essential tool for emergency firmware upgrades, especially when Intersight access is unavailable and a firmware update is critical for restoring system functionality or access.

eCMCs must be updated serially (one after the other), not in parallel. This is crucial because components such as Power Supply Units (PSUs) and Power Distribution Board Field Programmable Gate Array (PDB FPGA) are shared between the two eCMCs. Attempting parallel updates will result in errors.

To update the firmware:

  1. Update the eCMC firmware using one of these methods:

  * **Method 1:** Using firmware from the workspace:/

Before initiating a firmware update, the firmware bundle (ESU and HUU images) must be copied to the /workspace directory on the eCMC.

       1. SSH to eCMC-CLI:

`**ssh admin@**` <eCMC-CLI IP>

       2. Copy the ESU bundle for eCMC firmware to the workspace directory:

`**cp**` scp://[username@]<SOURCE_SERVER_IP>:<path_to_esu_bundle_file> `**workspace:/**` <esu_bundle_filename>

Example:

`**cp**` scp://[username@]<SOURCE_SERVER_IP>:/var/www/html/Utils/esu-firmware-6.0.X.XX00XX.tar.gz `**workspace:/**` <esu_bundle_filename>

Note:
  * [username@] is optional; omit if the source server doesn't require a username for scp.

  * Replace <SOURCE_SERVER_IP> with the actual IP address of your source server.

  * Replace <path_to_esu_bundle_file> with the full path to the ESU bundle on the source server.

  * Replace <esu_bundle_filename> with the desired name for the file in the eCMC's workspace:/.

       3. Copy the HUU bundle for Compute Node firmware to the workspace directory:

`**cp**` scp://[username@]<SOURCE_SERVER_IP>:<path_to_huu_bundle_file> `**workspace:/**` <huu_bundle_filename>

Example:

`**cp**` scp://root@<SOURCE_SERVER_IP>:/var/www/html/Utils/ucs-xe130cm8-huu-6.0.99.250099D.iso `**workspace:/**` ucs-xe130cm8-huu-6.0.X.XX00XX.iso

Note:

Replace the placeholders as described for the ESU bundle.

       4. Update eCMC Firmware:

          1. SSH to eCMC-CLI:

`**ssh admin@**` <eCMC-CLI IP>

          2. Enter firmware scope:

`**scope firmware**`

          3. Update eCMC-A firmware:

`**update-ecmc-firmware workspace:/**` <esu_bundle_filename>

Example:

`**update-ecmc-firmware workspace:/**` esu-firmware-6.0.X.XX00XX.tar.gz
                 
                 eCMC firmware update successfully triggered....

       5. Update Compute Node firmware:

          1. SSH to eCMC-CLI:

`**ssh admin@**` <eCMC-CLI IP>

          2. Enter firmware scope:

`**scope firmware**`

          3. Update the compute node firmware:

`**update-server-firmware**` <server-ID> `**workspace:/**` <huu_bundle_filename>

Example:

`**update-server-firmware**` 2 `**workspace:/**` ucs-xe130cm8-huu-6.0.1.XX00XX.iso

Note:

Replace <server-ID> with the appropriate server number (For example:2 for Server 2).

  * **Method 2:** Using firmware from a USB drive

Before initiating a firmware update, the firmware bundle (ESU and HUU images) must be copied to the USB drive.

       1. Connect the USB drive to the eCMC.

       2. List the USBs connected to the eCMC.

`**list-storage-drives**`
              
              Name                      Location
              eMMC                      workspace:/
              USB Drive1                media/sda1:/

       3. Update the eCMC firmware:

`**update-ecmc-firmware**` media/sda1:/esu-firmware-6.0.1.XX00XX.tar.gz.

       4. Update the compute node using a firmware bundle from a USB drive:

          1. Copy the HSU bundle from the USB to the **workspace:/** directory.

          2. Execute the command for updating the compute node.

`**update-server-firmware**` <absolute_file_path>

  2. Check firmware update status for eCMC A:

`**show firmware-update-status**` ecmc A

**Example Output:**
         
         ECMC A:
                 Status: Completed
                 Complete: 100%

  3. Check firmware update status for the server:

`**show firmware-update-server**` <server-ID>

  4. Repeat steps 1-4 by logging into the eCMC-B with the eCMC-B <IP-Address>.

  5. Check servers populated in the chassis:

     1. SSH to eCMC-CLI: 

`**ssh admin@**` <eCMC-CLI IP>

     2. Enter server's scope:

`**scope servers**`

     3. Display servers:

`**show servers**`

  6. Check firmware versions running on eCMCs:

     1. Enter firmware scope:

`**scope firmware**`

     2. Display the firmware version running on eCMC A:

`**show firmware-version**` ecmc A

     3. Display the firmware version running on eCMC B:

`**show firmware-version**` ecmc B

  7. Check firmware version running on server nodes:

     1. Enter firmware scope:

`**scope firmware**`

     2. Display the firmware version running on the Unified Edge server:

`**show firmware-version server**` <server-id>

  8. Check Device Console, Management Package and Bundle version of eCMC:

     1. Enter firmware scope:

`**scope firmware**`

     2. Display Device Console, Management Package and Bundle version of eCMC:

`**Show version**`

