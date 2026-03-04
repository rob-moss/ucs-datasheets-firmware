# Intersight Appliance Device Console

| | |
|---|---|
| **URL Title** | Intersight Appliance Device Console |
| **URL** | https://intersight.com/help/appliance/device_console |
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260225095216527/docs/onprem/data/articles/device_console/en/index.html |
| **HTML Title** | Device Console |
| **Source file** | `ucs-docs-raw/html/intersight-appliance_device_console.html` |
| **File type** | HTML |
| **Fetched on** | 2026-03-04 11:00:11 |

---

# Device Console

## Overview

The Device Console is a user interface that provides a limited ability to manage the system, even when Intersight is not connected. The Device Console provides both a Command-Line Interface (CLI) and a Web User Interface (UI) and can connect remotely to Fabric Interconnects (FI) of Intersight Managed Mode domains.

This interface provides system information, including the model, serial number, and firmware version of the Fabric Interconnects. It facilitates Device Connector configuration. Inventory details for Fabric Extenders (for FIs only), Servers, and Chassis are displayed. Additionally, tech support bundles containing diagnostic information can be generated for troubleshooting and analysis, and power and LED operations for servers are supported.

## Accessing the Device Console

To access the Device Console user interface, log in to the Fabric Interconnect using a management IP address or DNS hostname if available. Administrator privileges are required to access Device Console UI.

You can also log into the Device Console of a Fabric Interconnect in Intersight Managed Mode using your enterprise LDAP account. To enable LDAP authentication attach the following policies:

  * An LDAP policy for HTTP and SSH access.

  * Certificate Management policy (optional) for secure access.


For more information, see the Creating an LDAP Policy and Creating a Certificate Management Policy sections in [Configuring Domain Policies](/help/resources/cisco_intersight_managed_mode_configuration#configuring_ucs_domain_policies).

## User Interface of Device Console

The FI Device Console UI consists of the following main elements:

  * A central pane that includes four tabs:

  * [System Information](/help/device_console#system_information_\(fabric_interconnects\))

  * [Device Connector](/help/device_console#device_connector) (Common)

  * [Inventory](/help/device_console#inventory_\(fabric_interconnects\))

  * [Diagnostic Data](/help/device_console#diagnostic_data_\(fabric_interconnect\))

  * A top navigation menu that contains the Help menu and Logout button.


## Device Connector

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
  
## System Information

The following table describes the system information parameters.

Details| Description  
---|---  
Management IPs| Displays the Cisco UCS management IP address.  
Model| Displays the Cisco UCS Fabric Interconnect series model.  
Serial| Displays the host ID/serial number of the server.  
Firmware Version| Displays the current firmware version running on the Fabric Interconnect.  
Available Memory| Displays the available memory.  
Total Memory| Displays the total allocated memory.  
  
## Inventory

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

  * None — When the server has been recommissioned but discovery is yet to start.
  * Active — When the server is discovered.
  * Decommissioned — When the server is removed from the Cisco UCS configuration. However, the server hardware physically remains in the Cisco UCS instance.
  * DiscoveryFailed — When the server discovery has failed.
  * SlotMismatch — When the configuration of a blade server is not correct and server rediscovery is required in the slot.

  
PID| Displays the Product ID (PID) of the server.  
Serial| Displays the host ID/serial number of the server.  
Server Profile| Displays the server profile that is associated with the server.  
User Label| Displays the user label that is set for the server.  
  
You can perform the following server actions:

  * Power On/Off

  * Turn On Locator

  * Launch KVM

  * Launch IMC

For more information on firmware requirements, see Firmware Requirements for Launching IMC from Device Console section in [Supported Systems](https://intersight.com/help/saas/supported_systems).
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

  * Active — When the chassis is discovered.
  * Decommissioned —When the Chassis is physically present and connected, but temporarily removed from the Cisco UCS configuration.
  * DiscoveryFailed — When the chassis discovery has failed.

  
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

  * Online — When the FEX is connected.
  * Decommissioned — When the FEX is physically present and connected, but temporarily removed from the Cisco UCS configuration.
  * Unclaimed — When the FEX has not been claimed to the Intersight account.
  * Discovery Failure — When the discovery of FEX has failed.

  
Model| Displays the FEX model.  
Serial| Displays the host ID/serial number of the FEX.  
Description| Displays the description for the FEX, if any.  
  
**PCIe Nodes Tab**

The PCIe Nodes subtab provides detailed information about all the PCIe Node connected through the Fabric Interconnect.

Details| Description  
---|---  
Name| Displays the name for the FEX.  
Status| Displays the status of the PCIe node. The values can be:

  * Active — When the PCIe node is discovered.
  * Decommissioned —When the PCIe node is physically present and connected, but temporarily removed from the Cisco UCS configuration.
  * DiscoveryFailed — When the PCIe node discovery has failed.

  
Model| Displays the hardware model of the PCIe node.  
Serial| Displays the host ID/serial number of the PCIe node.  
Address| Display the network address assigned to the PCIe node.  
Locator LED| Displays the state of the locator LED of this PCIe node.  
  
We can perform these operation on PCIe node from the Device Console:

  * Turn On/Off Locator

  * Generate Tech Support Bundle


## Diagnostic Data

From the Diagnostic Data tab, you can collect diagnostic data for severs, chassis, and Fabric Interconnects for troubleshooting and further analysis.

**Tech Support Bundles**

You can generate tech support bundles for the following:

  * Server—Contains technical support data for blade and rack servers including all adapters. For blade severs, tech support data is collected for IOMs.

  * Chassis—Contains technical support data for a given chassis including IOMs.

  * Fabric Interconnect—Contains technical support data for Fabric Interconnect. The data can be for either the local or both the local and peer switches.

  * PCIe Node—Contains technical support data for PCIe nodes.


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
`**update-device-connector workspace:/**` | `**volatile:/**` filename| Updates the Device Connector image.Note:Images are generally not accessible to customers. This operation is used by TAC for recovery purpose.| —  
  
**System Information**

These commands allow you to view general system information.

Command| Description| Note  
---|---|---  
`**show clock**`|  Displays the system date and time.| Setting the time on the FI requires NTP. NTP should be configured in the Device Console and in the NTP Policy of the Domain Profile.  
`**show cli history**`|  Displays the history of CLI commands run in the session.| —  
`**show sshkey**`|  Displays the list of SSH public key of the host.| —  
`**show mgmt-ip-debug**`|  Displays the IP address and the interfaces on both the management and default namespaces.| —  
`**show mgmt-ip-tables**`|  Displays the IP table entries on both the management and default namespaces.| —  
`**show file**` file-path| Displays the contents of a file.| —  
`**show processes**`|  Displays a list of all processes that are currently running.| —  
`**show audit**`|  Displays the audit log of the Fabric Interconnect.| —  
`**show self-signed-certificate**`|  Shows self signed certificate.| —  
  
**Servers/Chassis/Switch**

These commands enable connecting to and managing the connected components.

Command| Description| Note  
---|---|---  
`**show chassis**` chassis-id| Displays the chassis details including IOM and XFM details.| —  
`**show pcie-node**` chassis-id/slot-id| Displays the PCIe node details.| —  
`**connect iom**` chassis-id| Connects to an IO module or to an Intelligent Fabric module.| Not available for Cisco UCS X-Series Direct.  
`**connect xfm**` chassis-id/xfm-id| Connects to the X-Fabric module.| —  
`**connect cimc**` chassis-id/blade-id | rack-id | chassis id/PCIe-node-id | chassis-id/slot-id| Connects to the CIMC (Cisco Integrated Management Controller).| For C-series servers, use rack-id.For X-series, B-series, and Cisco UCS X-Series Direct, use chassis-id.For PCIe node, use chassis-id/ PCIe-node-id or chassis-id/slot-id.  
`**connect adapter**` chassis-id/blade-id/adapter-id | rack-id/adapter-id| Connects to an adapter on B-series, X-series, or C-series servers.| For B-series/X-series servers, use chassis-id/blade-id/adapter-id.For C-series, use rack-id/adapter-id.  
`**pcie-node led**` chassis-id/slot-id | on/off| Turns on or off the PCIe node LED locator.| —  
`**pcie-node led-status**` chassis-id/slot-id| Displays the PCIe node LED locator status.| —  
`**reset_all_memory_errors**`|  Clears the memory counters using the reset memory error command.| —  
`**connect switch**`|  Connect to the switch shell.| —  
  
Note:

The id represents the identification number the component.

**PMON Processes**

Process Monitor (PMON) processes includes all the internal processes associated with the **mgmt plugin**. PMON processes help in restarting the processes during FI recovery/troubleshooting.

These commands enable managing PMON and connector processes.

Command| Description| Note  
---|---|---  
`**pmon**` { `**start**` | `**stop**` | `**state**` } [ `**connector**` ]| Allows you to start, stop, or view the current status of the PMON or connector processes.| —  
  
**Technical Support**

These commands help in fetching diagnostic data files.

Command| Description| Note  
---|---|---  
`**show-tech-support server**` blade-id| Displays the contents of the tech-support bundle for a specific server blade.| For Fabric Interconnects, use blade-id.  
`**show tech-support chassis**` chassis-id| Displays the contents of the tech-support bundle for a specific chassis.| —  
`**show tech-support fex**` fex-id| Displays the contents of the tech-support bundle for a specific FEX.| This command applies only to IMM.  
`**show tech-support switch**` switch-id| Displays the contents of the tech-support bundle for a specific switch.| —  
`**show tech-support pcie-node**` chassis-id/slot-id| Displays the contents of the tech-support bundle for a specific PCIe node.| —  
`**show core-files**`|  Displays the core files.| —  
  
**Directory Operations**

These commands allow for file system navigation and manipulation within the CLI.

Command| Description| Note  
---|---|---  
`**cd**` { `**workspace:/**` | [path] `**| volatile:/**` | [path] `**|**` | [path] `**| usbdrive1:/ | usbdrive2:/**` }| Changes directory.| —  
`**pwd**`|  Displays the current working directory.| —  
`**Is**`|  Lists the contents of the current working directory.| —  
`**mkdir**` { `**workspace:/**` | [path] `**| volatile:/**` | [path] `**|**` | [path] `**| usbdrive1:/ | usbdrive2:/**` }| Creates a directory under allowed directories.| —  
`**rmdir**` { `**workspace:/**` | [path] `**| volatile:/**` | [path] `**|**` | [path] `**| usbdrive1:/ | usbdrive2:/**` }| Removes the directory.| —  
`**cp**` [from-filesystem:] [from-path] filename [to-filesystem:] to-path [dest-filename]| Copies a file from one directory to another.| —  
`**mv**` [from-filesystem:] [from-path] filename [to-filesystem:] to-path [dest-filename]| Moves a file from one directory to another.| —  
`**rm**` { `**workspace:/**` | [path] `**| volatile:/**` | [path] `**|**` | [path] `**| usbdrive1:/ | usbdrive2:/**` }| Removes a file from a directory.| —  
  
**Other Operations**

These commands cover various networking diagnostics, system management, and configuration tasks.

Command| Description| Note  
---|---|---  
`**set management-network**` ip-address netmask/preix_length gateway| Configures management IP address, network mask, and gateway address on a Fabric Interconnect.| —  
`**tail-mgmt-log**` module_name| Displays the management log of the services running on a Fabric Interconnect.| —  
`**ssh**` host-name| Logs in to a host that supports SSH.| —  
`**telnet**` host-name [port-num]| Logs in to a host that supports Telnet.| —  
`**traceroute**` [ `**-s**` source-address ] address| Displays the route to an IPv4 network host.| —  
`**traceroute6**` [ `**-s**` source-address ] address| Displays the route to an IPv6 network host.| —  
`**ping**` [ `**-c**` count ] [ `**-s**` packet-size ] [ `**-i**` interval ] [ `**-w**` timeout ] { host-ip-address | | | host-name }| Diagnoses basic network connectivity for IPv4 addresses.| —  
`**ping6**` [ `**-c**` count ] [ `**-s**` packet-size ] [ `**-i**` interval ] [ `**-w**` timeout ] { host-ip-address | | | host-name }| Diagnoses basic network connectivity for IPv6 addresses.| —  
`**reboot**`|  Reboots the system.| —  
`**connect nxos**`|  Connects to NX-OS.| —  
`**erase-configuration**`|  Erases configuration on the Fabric Interconnect.| Erase configuration will not affect or delete any existing data on the Fabric Interconnect.  
`**fi-secure-erase**` [-preserveImage]| Erases all data and configuration on the Fabric Interconnect, run the command.Use the preserveImage flag to keep the system image while deleting all other data from the Fabric Interconnect.| FI Secure Erase may take 20 to 40 minutes to complete.For information on minimum firmware version requirement, see [Firmware Requirements for FI Secure Erase](/help/supported_systems#firmware_requirements_for_launching_imc_from_device_console).  
`**change-password**`|  Changes the administrator password on the Fabric Interconnect.| —  
`**clear-sshkey**` host-name| Clears the SSH public key of a remote host from cache.| —  
`**change-domain-name**`|  Updates the name of the Fabric Interconnect and the peer FI.| —  
`**change-mode**`|  Changes the management mode of the server.| —  
`**clear**`|  Clears the screen.| —  
`**clear-firmware-cache**`|  Clears an entry from the Intersight firmware cache.| —  
`**cluster-start**`|  For initial HA setup, starts cluster server.| The cluster-start command is used in the backend as part of the developer script when adding an FI to a cluster.—  
`**connect**`|  Connects to an endpoint.| —  
`**generate-self-signed-certificate**`|  Generates a new self-signed certificate.| After generating the self-signed certificate, the command restarts the web server.  
`**list-firmware-cache**`|  Displays the list of entries in the Intersight firmware cache.| —  
`**server**`|  Displays the list of server operations and their usage (led-status, power, power-status, led).| —  
`**update-management-package workspace:/**` | `**volatile:/**` filename| Updates the Device management package on Fabric Interconnect.| Packages are not accessible to the customers. This operation is used by Cisco TAC for recovery purpose.  
`**help**`|  Displays help.| —  
`**exit**`|  Exits the program.| —