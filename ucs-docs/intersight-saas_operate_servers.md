# Intersight SaaS Servers guide

| | |
|---|---|
| **URL Title** | Intersight SaaS Servers guide |
| **URL** | https://intersight.com/help/saas/operate/servers |
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260402103337138/docs/cloud/data/articles/features/servers/operate/en/index.html |
| **HTML Title** | Document |
| **Source file** | `ucs-docs-raw/html/intersight-saas_operate_servers.html` |
| **File type** | HTML |
| **Fetched on** | 2026-04-10 12:48:23 |

---

Choose Operate > Servers, to launch the Server Table view. From this page, you can launch device endpoints, perform bulk server actions, and navigate to the server details page. Click the settings icon (the gear icon representation), and select the columns that you want in the Table view.

You can add specific columns or custom tags to the Servers Table view to sort and filter.

Columns in the Servers Table view can be sorted using the sort option. You can also apply filters based on any column using the Filters option to view and explore the server inventory.

**Servers Table Summary Dashboard**

The following widgets are available in the Servers table view:

Note:

All widgets except Server Profiles are dynamic and change based on the Add Filter option you select.

  * Health—The pie chart provides a visual representation of the health of the servers.

  * Power—The badges display the number of servers powered off or on.

  * HCL Status—The badges display the HCL status for the servers.

  * Bundle Version—The pie chart displays the total number of servers distributed by the bundle version.

  * Firmware Version—The pie chart displays the total number of servers distributed by the firmware version.

  * Models—The pie chart displays the total number of servers distributed by server models.

  * Contract Status—The badges display the status of the service contract of the managed UCS and HyperFlex servers distributed by the current validity of their associated contracts.

  * Profile Status—The pie chart displays the total number of servers distributed by the status of the server profile deployment.

  * Requests (last 24h)—The pie chart displays the number of completed and failed tasks for the last 24 hours.

  * Alarm Suppression—The badges display the number of servers categorized by their alarm suppression status: active (Yes) or inactive (No).


You can view the following details in the Servers Table view:

  * Name—Displays the name of the server.

Important:
  * For Intersight Standalone servers, the name is a combination of server model and server serial number.

  * For B-Series and X-Series servers running in UCSM Managed Mode (UMM) and Intersight Managed Mode (IMM), the name is a combination of UCS domain name, chassis ID, and server ID. The server ID is automatically assigned by the platform when a server is registered or claimed.

  * For C-Series servers running in UMM and IMM mode, the name is a combination of the UCS domain name, and server ID. To configure the server ID, decommission the server and recommission it. During recommission, you can assign the server an ID of your choice.

  * The power icon displays the server power status **On** or **Off**.

  * The connection icon appears only for disconnected servers and indicates that the server is not currently connected to Intersight.

  * Health—Displays the server health status, based only on the server's known alarms. Hover over the status to view the top three active alarms. An icon ![](../../../../../../../../en/us/td/i/400001-500000/470001-480000/479567.jpg) next to the Health status indicates that the server's alarm notifications are currently suppressed. For more information, see [Alarm Suppression](/help/my_dashboard/dashboard_management#alarm_suppression).

  * Contract Status—Displays the status of service contract for the managed UCS and HyperFlex servers based on the current validity of their associated contracts. You can identify the SmartNet Contract ID details of the server, and cross launch the [Cisco Commerce Software Subscriptions and Service Portal](https://www.cisco.com/c/en/us/services/ordering/ccw-r.html).

  * Alarm Suppression—Displays the alarm suppression status on the server as _Yes_ for active or _No_ for inactive. For more information, see [Alarm Suppression](/help/my_dashboard/dashboard_management#alarm_suppression).

  * Management IP—Displays the management IP address of the server, which is used by Cisco Intersight for management purposes. The management IP address is assigned through the IMC Access Policy. After you create a server profile, attach the IMC Access Policy with an IP address pool, assign the profile to a server, and deploy it, the management IP address is automatically assigned to the server.

Note:

For Out-of-Band configuration, all IP addresses in the management IP pool must be in the same IPv4 subnet, or have the same IPv6 network prefix as the IP address of the fabric interconnect.

  * Model—Displays the server model.

  * CPU Capacity (GHz)—The aggregated speed of the CPUs on this server. CPU capacity is calculated as the Number of CPU Sockets x Enabled Cores x Speed.

  * Memory Capacity (GB)—The amount of RAM installed on the server in Gigabytes.

  * UCS Domain—Displays the name of the UCS Domain the server belongs to. For standalone server, this column is not applicable.

  * HX Cluster—Displays the name of the HyperFlex cluster the server belongs to.

  * HCL Status—Displays the compliance status with the Hardware Compatibility List (HCL) after checking the compatibility of the server model, processor, firmware, adapters, operating system and drivers. For more information, see [Compliance with Hardware Compatibility List (HCL)](/help/my_dashboard/dashboard_elements#compliance_with_hardware_compatibility_list_\(hcl\)).

  * Management Mode—Displays the management mode of the server (Standalone, Intersight, UCSM)

  * Server Profile—Displays the server profile that is associated with the server.

  * Utility Storage—Displays the storage utility that is associated with the server and whether it is in the OK state.

  * Bundle Version—Displays the firmware bundle version to which the server is running.

  * Firmware Version—Displays the running server firmware version at the endpoint.

  * Serial—Displays the host ID/serial number of the server.

  * User Label—Displays the assigned user label that helps in identification of the server.

  * Lifecycle—Displays the logical state of the server. This is applicable only for Intersight Managed Mode servers. The various possible values are:

  * Active — Server has been successfully discovered in the chassis or slot.

  * Migration In Progress — The discovered server is being physically moved into a different slot in the same chassis, or into a different chassis.

  * Moved — The discovered blade server has been physically moved from its original location to a new location within the same domain, leaving the old location empty.

  * Moved + Replaced — The discovered blade server has been physically moved from its original location to a new location within the same domain, and the old location has been populated with other blade servers.

  * Removed — A discovered blade server has been physically removed from its original location, leaving that location empty.

  * Replaced — The discovered blade server has been physically removed from its original location, which is now populated with other blade server.

  * Decommissioned — The server is being decommissioned and removed from the Cisco UCS configuration. However, the server hardware remains physically present in the Cisco UCS environment.

  * Discovery In Progress — The server is being discovered in the chassis or slot.

  * Discovery Failed — Discovery of the server was attempted in the chassis or slot, but it failed.

  * Firmware Upgrade In Progress — The firmware on the discovered server is being upgraded.

  * Slot Mismatch — Blade server was discovered or partially discovered in a chassis or slot but is now detected in another chassis or slot.

For more information on the allowed and blocked actions in the above cases, see [OIR for Blade Server](/help/resources/cisco_intersight_managed_mode_configuration#oir_for_blade_server).


  * License Tier—Displays the current license tier on the server. You can update one or more servers to a new license tier. From the ellipsis (…) on the far right column for a server, you can choose a new license tier from the drop-down. For updating multiple servers at once, select the desired servers, click the ellipsis (…) at the top left of the table and select Set License Tier. For more information, see [Multiple Licensing Tiers](/help/getting_started/licensing_requirements/lic_intro#multiple_licensing_tiers).

  * Asset Tag—A tag that identifies the server.

  * CPU—Displays the number of CPUs in the server.

  * CPU Cores—Displays the number of CPU cores in the server.

  * Cooling Method—Displays the cooling method for the server. The available methods are Air or Immersion.

Note:

Liquid immersion cooling is supported only on the following servers in Intersight Managed Mode (IMM) and Intersight Standalone Mode (ISM):

  * C220 M7 with minimum server firmware 4.3(6.250040)

  * C220 M8 and C240 M8 with minimum server firmware 6.0(2.260044).


## Properties

The Properties area displays a graphical view of the front, rear, and top sections of the server. Toggling on the Health Overlay function allows you to monitor the health of the server ports. The bottom section displays the Power On/Off status, Locator LED status, number of CPUs, threads, CPU cores, enabled CPU cores, and adapters. You can also view memory capacity, CPU capacity, ID, UUID, and cooling method.

Note: The dynamic display of riser configurations is supported across all server models in the rear view section of the server.

## Alarms

Intersight provides fault monitoring capabilities to track alarms for all managed UCS and HyperFlex systems. For more information, see [Alarms](/help/my_dashboard/dashboard_management#alarms).