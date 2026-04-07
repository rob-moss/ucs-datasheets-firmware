# Intersight SaaS Monitoring Topology

| | |
|---|---|
| **URL Title** | Intersight SaaS Monitoring Topology |
| **URL** | https://intersight.com/help/saas/monitoring/topology |
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260402103337138/docs/cloud/data/resources/monitoring/en/Topology.html |
| **HTML Title** | Topology View |
| **Source file** | `ucs-docs-raw/html/intersight-saas_monitoring_topology.html` |
| **File type** | HTML |
| **Fetched on** | 2026-04-08 08:43:27 |

---

# Topology View  
  
## Overview

The Topology views offer a visual representation of the components in an Intersight-Managed UCS Domain (IMM domain) and Unified Edge server. The view also displays the connections and relationships between these components. The view uses pop-ups and color codes to provide more detailed information on the health status of each component, port, and connection. This view enables you to verify the cabling and troubleshoot connectivity issues effectively.

To view the hardware components in the Topology view, you need to first claim the FIs and deploy the Domain Profile to the FIs.

Note:

  * The Topology view displays only the hardware that is deployed in the Intersight Managed Mode or Unified Edge servers. For more information on supported hardware in IMM mode, see [Supported Hardware for Intersight Managed Mode](/help/supported_systems#supported_hardware_for_intersight_managed_mode).

  * To view error metrics in the Topology view, all servers in a UCS domain must have an Advantage license. If the UCS domain contains a mix of Essentials and Advantage licenses, the error metrics will not be displayed.


The Topology views are added as a new tab in the details view of **Unified Edge** , **Servers** , **Chassis** , and **Fabric Interconnects**. The topology views available are as follows:

  * **Fabric Interconnects Topology:** This topology displays a high-level view that shows all connections within a single IMM domain. For more information, see [Viewing fabric interconnects Topology](/help/monitoring/topology#viewing_fabric_interconnect_topology).

  * **Chassis Topology:** This topology displays a detailed view of the connections within a single chassis in the IMM domain, including visibility to internal ports. For more information, see [Viewing Chassis Topology](/help/monitoring/topology#viewing_chassis_topology).

  * **Server Topology:** This topology displays a detailed view of the connections from a single server, including visibility to internal ports. For more information, see [Viewing Server Topology](/help/monitoring/topology#viewing_server_topology).

  * **Unified Edge Topology:** This topology displays a detailed view of a standalone Unified Edge server, including Edge Chassis Management Controllers (eCMC), servers, and all internal and external port connections. For more information, see [Viewing Chassis Topology](/help/monitoring/topology#viewing_unified_edge_topology).


Although they are separate views, these views are interconnected. For instance, by selecting and double-clicking on the desired component from a **fabric interconnects Topology** , you can drill down to its connected **Server** or **Chassis Topology** , and also navigate back to the initial view.

## Understanding Topology UI Elements

When you hover over the components or ports, it displays pop-ups that show their respective details. You can move connected devices by clicking and dragging them. A single click on a component will highlight its individual connections. For example, a single click on a chassis will highlight the FI ports used by the IO Modules of the chassis. Similarly, a single click on the server will highlight the FI ports used by the VIC of the server.

The Topology views offer a visual depiction of alarms, error metrics, and the operational status of devices. Icons representing Alarms and Error Metrics display the count of associated issues. Hovering over these icons activates a pop-up that presents the relevant statistics.

If changes were made to a physical cable connection or if there have been modifications within Intersight, it is necessary to refresh the topology view to obtain the most up-to-date changes.

The connections in the views do not always represent individual cables. They just show that there is a connection between the two devices. A connection can represent a single link, multiple links, or a port channel. The following scenarios are possible:

  * Connection links between IOM and FI are physical connections

  * Connection links between servers and FI are physical connections

  * Connection links between servers and FEX, as well as between FEX and FI are physical connections

  * Connection links between B-Series or X-Series servers and IOM HIF ports are logical connections (Only for Chassis Topology)

  * Connection links between L1/L2 Ethernet ports is a logical connection, where a single line represents the status of both L1 and L2.


Action| Description  
---|---  
![](../../../../../../../../en/us/td/i/400001-500000/470001-480000/477038.jpg)| To toggle between full-screen and normal mode.  
![](../../../../../../../../en/us/td/i/400001-500000/470001-480000/477039.jpg)| To auto-align the components.  
![](../../../../../../../../en/us/td/i/400001-500000/470001-480000/477040.jpg)| To adjust the view of the topology by zooming in or zooming out.  
.![](../../../../../../../../en/us/td/i/400001-500000/470001-480000/477041.jpg)| To open the legend for the current topology for better comprehension of the graphical representation.  
.![](../../../../../../../../en/us/td/i/400001-500000/470001-480000/477042.jpg)| To select a component.When you select a component from the **Search** dropdown list, the selected component is highlighted with a blue outline in the topology view.  
![](../../../../../../../../en/us/td/i/400001-500000/470001-480000/477043.jpg)| 

  * To show or hide connections between components connections between components. In a large domain with numerous connections, it becomes easier to view popups when you hide the connections.
  * To show or hide error metrics for the devices.

  
  
## Legend Details

The table below details the icons shown in the legend of the Fabric Interconnects and Server Topology views:

Note:

The Link Status legend displayed change based on the metric type (Operational Status or Network Utilization) you have selected.

Icon| Description  
---|---  
**Link Status - Operational Status**  
![](../files/Oper_UP.png)|  Indicates that all the connections in the group are up. The connection is stable and operational.  
![](../files/Oper_PartiallyDown.png)| Indicates that the group of links has a mix of links in the Up and Down state.

  * Consider a Chassis with four ports. If one port is down, but the remaining ports are up, the FI topology displays the connection link between the chassis and FI as Yellow.

  
![](../files/Oper_Down.png)| Indicates that all connections in group are down.  
**Link Status - Network Utilization** Network utilization limits can be adjusted to suit specific requirements, enabling you to set custom thresholds. The health of each connection link is evaluated based on the highest TX/RX utilization between the source and target ports. In addition, the size of the port channel link is defined by the combined bandwidth of its individual links. For more information, see [Network Utilization Threshold](/help/monitoring/topology#network_utilization_threshold).Network utilization data is calculated by averaging the RX and TX values over a 10-minute interval, ensuring that the resulting metrics are both reliable and informative.  
![](../files/LS_OK.png)| Indicates that all underlying links are operating with optimal utilization levels.  
![](../files/LS_Warning.png)| Indicates that some underlying links exhibit warning-level utilization, excluding scenarios where there is only a combination of critical and no-data links.  
![](../files/LS_Critical.png)| Indicates that all underlying links have reached critical utilization levels, or there is a combination of critical and no-data links.  
![](../files/LS_No_Data.png)| Indicates that data is unavailable or the links are down for all underlying connections.  
**FI Port Status**  
![](../files/FI_UP.png)|  Indicates that the operational status of the port is **Up**.  
![](../files/FI_Down.png)| Indicates that the operational status of the port is **Down** and the port has critical alarms.  
![](../files/FI_Warning.png)| Indicates that the operational status of the port is **Down** and the port has warning alarms.  
![](../files/FI_D_W_I_A.png)| Indicates one of the following:

  * The operational status of the port is **Down** , the port is configured, and has info alarms.
  * The port is connected, the operational status of the port is **Down** and the port does not have any alarms.

  
![](../files/FI_UnConfig.png)| Indicates that the port is not configured and not connected.  
**Device Type**  
![](../../../../../../../../en/us/td/i/400001-500000/470001-480000/477047.jpg)|  This icon represents a chassis.  
![](../../../../../../../../en/us/td/i/400001-500000/470001-480000/477048.jpg)| This icon represents a Fabric Extender (FEX).  
![](../../../../../../../../en/us/td/i/400001-500000/470001-480000/477049.jpg)| This icon represents a C-Series server.  
![](../files/Server_Group.png)| This icon represents a group of components. For example, a group of C-Series servers connected to a FEX.  
![](../files/Network_Switch.png)| This icon represents a networking or a storage switch.  
![](../files/Storage_Array.png)| The icon represents a storage array.  
**Metrics**  
![](../files/ErrorMetrics.png)|  The icon represents the count of error metrics for the last 24 hours.  
  
The table below details the icons shown in the legend of the Unified Edge, Server, or Chassis topology view:

Icon| Description  
---|---  
![](../../../../../../../../en/us/td/i/400001-500000/470001-480000/477044.jpg)| Green line indicates that the physical connection between the two devices is established and functioning correctly.  
![](../../../../../../../../en/us/td/i/400001-500000/470001-480000/477045.jpg)| Red line indicates that the devices at either end of the connection cannot communicate with each other due to a physical disconnection, cable issues, hardware problems, or some other connectivity-related problem.  
![](../../../../../../../../en/us/td/i/400001-500000/470001-480000/477046.jpg)| Yellow line indicates that the group of links has a mix of links in the **Up** and **Down** state.  
![](../files/ErrorMetrics.png)| The icon represents the count of error metrics for the last 24 hours.  
  
Note:

Customize your network metrics display by selecting either bits per second (bps) or bytes per second (Bps). To change units, go to Profile Menu > User Settings > Network Units toggle and choose your preferred option. The default unit is bits per second.

Your selection applies across Metrics Explorer, Dashboard widgets (including bandwidth utilization), topology, and the Metrics tab, and will persist across sessions. Metric names, descriptions, and units update automatically—for example, Network RX Bytes becomes Network RX Bits.

## Alarms, Error Metrics for Devices, and Connection Link Operational Status in Topology View

The Topology views also provide you with a visual representation of alarms, error metrics, and link operational status for devices that are a part of Intersight-Managed UCS Domain (IMM domain) or Unified Edge servers. The view uses icons, color codes, and pop-ups to provide detailed information for each component, port, and connection. When you hover over the links, or the Alarm or Error Metrics icon next to the devices, the pop-ups display detailed information.

![](../files/image1.png)

**Alarms**

When a device has warning or critical alarms, an Alarm icon appears next to the device icons in the Fabric Interconnects Topology view. This Alarms icon shows the number of error or warning alarms, with the color indicating the severity level: critical or warning. Hovering over the Alarm icon triggers a pop-up that provides the following details:

  * Count of alarms categorized by type: error, warning, and information.

  * The most recent three error, warning, and/or information alarms.

  * To access detailed information about a specific alarm, click on the alarm to navigate to the Alarms page.

  * To view a comprehensive list of all alarms for the device, select Show All.


Note:

The Alarms icon does not appear for information alarms on the devices.

![](../files/image2.png)

For more information on Intersight alarms, alarm suppression, and alarm classifications, see [Alarms](/help/my_dashboard/dashboard_management#alarms).

**Error Metrics**

When a device or FI port has errors, an Error Metrics icon appears next to the device icon in the Fabric Interconnects Topology view. The Error Metrics icon show the count of errors for the last 24 hours. Hovering over an Error Metrics icon triggers a pop-up that provides the following details:

  * The top error metrics by count for a specific time interval.

  * A compact chart offering a visual representation of error metrics. The chart can help to spot trends, variations, and patterns in the metric.

  * To access detailed information about a specific error metric, click on the error metric to navigate to the Metric Explorer page.

  * To view a comprehensive list of all error metrics for the device, select View in Explorer.


Note:

To view error metrics in the Fabric Interconnects Topology view, all servers in a UCS domain must have an Advantage license. If the UCS domain contains a mix of Essentials and Advantage licenses, the error metrics will not be displayed.

![](../files/image3.png)

**Note** : To enable Error Metrics in the Fabric Interconnects Topology view Advantage license is required for all servers in the UCS domain.

For more information on error metrics, see [Fabric Interconnects, Chassis, and Server Metrics](/help/monitoring/monitoring_metrics_devices).

**Link Operational Status**

In the Fabric Interconnects Topology view, the operational status of the connection links is displayed. Hovering over the connection link triggers a pop-up that provides the following details:

  * Count of ports and the health status.

  * Details about each port member involved in the link, including the individual statuses.

  * To access the details for a port member, click the respective hyperlink.


![](../files/image4.png)

## Environmental Metrics

In the Topology view, you can directly access the environmental metrics for Fabric Interconnects, Chassis, Servers, and FI ports that are a part of Intersight-Managed UCS Domain (IMM domain). Instead of navigating to the Metrics Explorer and selecting metrics beforehand, you can simply select a device within the topology view to view the relevant environmental metrics.

To access the environmental metrics in the Topology tab for Fabric Interconnects, Servers, or Chassis, or FI port hover over the device to display pop-up, then click **View Metrics**. Alternatively, you can click on the device icon to view the environmental metrics.

Metrics are presented in the widget drawer within the interface, offering a clear and organized way to access data. Each widget includes a direct link to the Metrics Explorer, enabling you to refine and customize the view as needed. This provides a seamless experience, combining convenience with flexibility for monitoring and analyzing environmental metrics.

Note:

In the Topology view, the environmental metrics are displayed with a 10-minute granularity for a 4-hour time interval.

The environmental metrics displayed vary for each device type, such as Fabric Interconnects, Chassis, Servers, and FI ports. The list below outlines the environmental metrics available for each device type:

**Environmental Metrics for Fabric Interconnects**

  * Host Energy

  * Host Power

  * Memory Utilization

  * Temperature


**Environmental Metrics for Chassis**

  * Host Power

  * Host Energy

  * Temperature


**Environmental Metrics for Blade Servers**

  * Host Energy

  * Host Power

  * Host Power State

  * Temperature


**Environmental Metrics for Rack Servers**

  * Host Energy

  * Host Power

  * Temperature

  * Host Power State


**Environmental Metrics for Unified Edge Servers**

  * Host Energy

  * Host Power

  * Memory Utilization (only eCMC)

  * Temperature


**Environmental metrics for FI Ports and Unified Edge eCMC**

  * Network TX/RX Utilization

  * Network TX/RX Pause Frames

  * Network TX/RX Priority Pause Frames

  * Network RX CRC Errors

  * Network No Buffer Errors

  * Network Late Collision Errors


**Example 1: Environmental Metrics for Fabric Interconnects**

![](../files/Env_Metrics.png)

**Example 2: Environmental Metrics for Chassis**

![](../files/Env_Metrics1.png)

**Example 3: Environmental Metrics for Servers**

![](../files/Env_Metrics2.png)

**Example 4: Environmental Metrics for FI Ports**

![](../files/Env_Metrics3.png)

## Viewing Fabric Interconnects Topology

The Fabric Interconnects (FI) Topology provides a high-level visualization of all connections within a single IMM domain, including Fabric Interconnects and connected devices such as servers, chassis, and networking infrastructure. The view displays northbound neighbors across two distinct protocols—Ethernet and Fibre Channel (FC)—with discovery and display behavior determined by the specific FI operating mode.

  * **Ethernet Protocol Connectivity:** In both End-Host and Switching modes, the topology discovers Cisco and third-party Ethernet switches using the Cisco Discovery Protocol (CDP) and Link Layer Discovery Protocol (LLDP). These connections are displayed as one line per active uplink. Hovering over these connections allows users to view the FI mode, the switch name and model, the traffic type (Ethernet or FCoE), and specific port IDs.

  * **Fibre Channel (FC) Protocol Connectivity:** For Fibre Channel, the topology supports End Host mode (NPV) and Switch mode (Core Switching). This view displays upstream or core FC switches (including Cisco MDS/Nexus and supported third-party switches) and, when in Switch mode, directly attached storage arrays. FC port channels are visualized as an aggregated link, while directly attached storage arrays are shown as separate icons. Hovering over these connections provides detailed metadata, including the FI mode, source and destination WWNs, peerPortWWN, VSAN, and, when available, the neighbor type (switch or storage) and vendor name.

  * **Operational Insights and Clarity:** To maintain protocol-level clarity, Ethernet and Fibre Channel connections are displayed separately within the topology. Consequently, a single physical device that supports both protocols will appear twice in the view—once as an Ethernet neighbor and once as a Fibre Channel neighbor. The interface provides real-time operational status for connection links, network utilization data, and health status indicators for all claimed devices. By providing enhanced details—such as WWN, vendor information, and device capabilities—the topology view enables administrators to effectively isolate problematic links and verify configurations across various switching modes.


To view fabric interconnects Topology:

  1. Choose **Operate** > **Fabric Interconnects** , to launch the Fabric Interconnects Table view.

  2. Click the fabric interconnects for which you want to view the topology, and then click the **Topology** tab.

The fabric interconnects Topology is displayed.

  3. From the drop-down menu, choose either **Operational Status** or **Network Utilization** to filter the metrics accordingly


The following information is available in the FI Topology view:

  * Based on your selection (Operational Status or Network Utilization) , you can view different types of connection links within the domain. Select one of the following:

  * **All Connection Links** —Displays every connection within the domain, providing a complete overview of the network topology.

  * **Problematic Links** —Based on the metrics type selected, displays:

  * **For Operational Status metrics** —only the connection links that are either partially down or down.

![](../files/Oper_Status_Problem.png)
  * **For Network Utilization metrics** —only connection links that are either critical, warning or No Data / Link Down

![](../files/Net_Utli_Problem.png)

Using a slider you can set the threshold for network bandwidth utilization. This threshold determines when a connection is considered critical (red), problematic (yellow), or normal (green). For more information, see [Network Utilization Threshold](/help/monitoring/topology#network_utilization_threshold).

  * **Critical Links** —Based on the metrics type selected, displays:

  * **For Operational Status metrics** —only connection links that are down.

![](../files/Oper_Status_Crit.png)
  * **For Network Utilization metrics** —only connection links that are critical. If a group of links contains any single critical link, then the yellow connect link is displayed.

  * **No Link** —Opt not to display any connection links within the domain.

  * The Fabric Interconnects Topology view displays the networking switches and storage arrays directly connected to the fabric interconnects (FI).

  * **Ethernet Neighbors:** Devices are discovered using the Cisco Discovery Protocol (CDP) and Link Layer Discovery Protocol (LLDP). These protocols must be enabled on both the FI and the connected devices via the CLI.

  * **Fibre Channel (FC) Neighbors:** Storage switches and storage arrays are discovered using specific CLI-based retrieval methods.

Note:
  * To view CDP or LLDP neighbors in the Topology view, Advantage license is required for all LLDP or CDP neighbors.

  * If both LLDP and CDP are enabled on a device, CDP takes precedence. Accordingly, information from CDP is displayed in the Topology view and returned by the API.

  * If an Ethernet neighboring device does not have LLDP or CDP enabled, it will be displayed as "unknown" in the Topology view. For Fibre Channel devices, ensure the device is correctly configured and connected to the FI to populate the topology accurately.

![](../files/Network_Switch_UI.png)

The topology view supports Ethernet uplink ports for networking switches and storage systems. Third-party storage devices are represented as appliance ports. The user interface uses icons and legends to indicate device types and their network roles.

![](../files/Network_Switch_Operational_Status.png)

To retrieve details of discovered neighboring devices, send a GET request to the `/api/v1/network/DiscoveredNeighbors` endpoint. The response includes information based on the currently active protocol.

Note:

If both LLDP and CDP are enabled on a device, CDP takes precedence. Accordingly, information from CDP is displayed in the Topology view and returned by the API.

  * The FI topology includes northbound Fibre Channel (FC) neighbors, so that UCS server administrators can see how FI uplink ports connect to:

  * Cisco and third party ethernet networking switches

  * Cisco and third party Fibre Channel storage switches

  * Storage arrays connected through appliance ports

  * Storage arrays connected through Fibre Channel storage ports

For each FI uplink, Topology shows both device level and port level relationships, allowing you to view exactly which FI ports are connected to which upstream ports on your switches and storage arrays.


  * Hover over the Info icon for an FI to:

  * **General Details** : Health, Type, Model, Serial, and Switch ID.

  * **Configuration** : Management Mode, Intersight status, Bundle Version, Ethernet Switching Mode, Fc Switching Mode, and UCS Domain Profile.

  * **Performance** : Click **View Metrics** to access environmental metrics for the FI.

  * Hover over the Alarms icon to:

  * View the critical, warning, and information alarms for the device.

  * Navigate to the Alarms View by clicking **Show All**. For more information, see [Alarms](/help/my_dashboard/dashboard_management#alarms).

Note:

The Fabric Interconnect (FI) alarm icon displays the count of alarms for the highest-severity active alarm type only (Critical, Warning, or Info). For example, if there are 3 Critical and 5 Warning alarms, the badge will show "3" with a red (Critical) icon. The tooltip provides the full breakdown of alarm counts by severity.


  * Hover over an FI port to:

  * View the port details on the Inventory page by clicking the link.

  * View the health and details of the FI ports.

  * Enable or disable an FI port as needed using the toggle button.

  * View the port details on the Inventory page by clicking the link.

  * View the environmental metrics for the FI port by clicking **View Metrics**.

  * Hover over the Error Metrics icon:

  * View the error metrics for the device.

  * Navigate to the Metrics Explorer by clicking **View in Explorer**.

  * Hover over the L1/L2 Ethernet link connecting the FIs:

  * View the operational status of the L1/L2 link. The L1/L2 link status can be in three possible states—Up, Down, or Partially down. Partially down indicates that there is a mix of links in the **Up** and **Down** state.

  * Hover over the Info icon for a chassis to:

  * View the health and details of the connected Chassis.

  * View the chassis details on the Inventory page by clicking the link.

  * Navigate to the Chassis Topology View by clicking **View Topology**.

  * View the environmental metrics for the chassis by clicking **View Metrics**.

  * Hover over the Info icon for a server to:

  * View the health and details of the connected Servers.

  * View the server details on the Inventory page by clicking the link.

  * Navigate to the Server Topology View by clicking **View Topology**.

  * View the environmental metrics for the server by clicking **View Metrics**.

  * Hover over the Info icon for a Networking Switch to:

  * View the platform, vendor, model, serial number, management IP, and native VLAN details of the Networking Switch or Storage Array.

![](../files/StorageSwitch.png)
  * Hover over the Info icon for a Storage Switch to:

  * View the platform, traffic type, management IP, and VSAN details of the Storage Switch or Storage Array.

Note:

In the Topology view, connections are represented as distinct icons to ensure protocol-level clarity. Switches operating with both Ethernet (CDP/LLDP) and Fibre Channel protocols are displayed separately. Similarly, each FI-to-storage controller connection is displayed as a unique icon, as there is no definitive physical property available to link multiple port connections to a single physical device.


Note:

For Cisco UCS Fabric Interconnects 9108 100G:

  * The Fabric Interconnects are depicted outside of the chassis for enhanced visualization.

  * A 10G inter-cluster link is visible between the two Fabric Interconnects.

  * Virtual links between the chassis and the integrated FI are shown.


For more information, see the following examples.

****Example 5: Topology with Blade chassis and multiple C-series servers connected to FIs****

![](../files/BladeMultipleC_Series.png)

**Example 6: Topology with multiple C-Series servers and FEX connected to FIs**

![](../files/C_Series_FEX.png)

## Network Bandwidth

In the Fabric Interconnects view, when you select the Network Utilization metrics from the drop-down, the connection link lines are represented based on the bandwidth (link thickness) and utilization (link coloring) metrics for each link.

The thicker connection lines represent higher bandwidth, and thinner lines represent lower bandwidth. A dynamic legend accompanies this feature, explaining that line sizes are determined by bandwidth, displaying minimum and maximum bandwidth with corresponding line sizes.

![](../files/LinkBandwidth.png)

The health of network connection links is determined by the highest TX and RX utilization of source or target ports, with customizable utilization limits. Connection link statuses—OK, warning, critical, or no-data/operational status down—are indicated by colors: green, yellow, red, and gray, respectively.

Network utilization data is calculated by averaging the RX and TX values over a 10-minute interval, ensuring that the resulting metrics are both reliable and informative.

Hover over the connection links to view the health and details of the connections.

![](../files/LinkBandwidth_2.png)

## Network Utilization Threshold

In the Fabric Interconnects view, you can set thresholds for network utilization metrics by moving the adjustable sliders. This threshold determines when a connection is considered critical (red), problematic (yellow), or normal (green). This visual representation simplifies the monitoring process and aids in maintaining optimal network performance.

To set the threshold for network utilization, do the following:

  1. Choose **Operate** > **Fabric Interconnects** , to launch the Fabric Interconnects Table view.

  2. Click the Fabric Interconnects for which you want to set the network bandwidth, and then click the **Topology** tab.

The fabric interconnects Topology is displayed.

  3. In the Topology tab, select **Network Utilization** from the drop-down options.

The Network Utilization Threshold and Link Bandwidth pop-ups appear.

![](../files/NetworkBandwidth.png)

Note:

The link color is determined based on the highest utilization among the ports.

  4. In the Network Utilization Threshold pop-up, use the sliders for setting thresholds for OK, Warning, and Critical levels.

  5. Click **Save**.


## Viewing Chassis Topology

The Chassis Topology provides a detailed view of the connections within a single chassis in the IMM domain, which includes IO Modules, FIs, and blade adapters.

To view a Chassis Topology:

  1. Choose **Operate** > **Chassis** , to launch the Chassis Table view.

  2. Click the Chassis for which you want to view the topology, and then click the **Topology** tab.

The Chassis Topology is displayed.


The following information is available in the Chassis Topology view:

  * Hover over the Info icon for an FI to:

  * View the health and details of the FI.

  * Click **View Topology** to navigate to the fabric interconnects Topology View.

  * View the environmental metrics for the FI by clicking **View Metrics**.

  * Hover over an FI port to:

  * View the health and details of an FI port.

  * View the port details on the Inventory page by clicking the link.

  * Enable or disable an FI port as needed using the toggle button.

  * View the environmental metrics for the FI port by clicking **View Metrics**.

  * Hover over the L1/L2 Ethernet link connecting the FIs:

  * View the status of the L1/L2 link. The L1/L2 link status can be in three possible states—Up, Down, or Partially down. Partially down indicates that there is a mix of links in the **Up** and **Down** state.

  * Hover over the HIF ports of an IO Module to:

  * View the health and details of the HIF port.

  * Hover over a VIC adapter box to:

  * View the details of the VIC and port expander if available.

  * Hover over an Adapter port to:

  * View the health and details of the adapter port.

  * Hover over a Chassis to:

  * View the health and details of the chassis.

  * Navigate to the Chassis Topology View by clicking **View Topology.**

  * View the environmental metrics for the chassis by clicking **View Metrics**.

  * Hover over the Alarms icon to:

  * View the critical, warning, or information alarms for the chassis.

  * Navigate to the Alarms View by clicking **Show All**. For more information, see [Alarms](/help/my_dashboard/dashboard_management#alarms).


For more information, see the following examples.

**Example 7: Topology with UCSX-9508 chassis within a single chassis**

![](../files/UCSX_9508_Single_Chassis.png)

**Example 8: Topology with UCSB-5108-AC2** **chassis within a single chassis**

![](../files/UCSX_9508_Single_Chassis.png)

## Viewing Server Topology

The Server Topology provides a detailed view of the connections from a single Server.

To view a Server Topology:

  1. Choose **Operate** > **Servers** to launch the Servers Table view.

  2. Click the Server for which you want to view the topology, and then click the **Topology** tab.


The Server Topology is displayed.

The following information is available in the Server Topology view:

  * Hover over the Info icon for an FI to:

  * View the health and details of the FI.

  * Navigate to the fabric interconnects Topology View by clicking **View Topology**.

  * View the environmental metrics for the FI by clicking **View Metrics**.

  * Hover over an FI port to:

  * View the health and details of the FI port.

  * View the port details on the Inventory page by clicking the link.

  * Enable or disable an FI port as needed using the toggle button.

  * View the environmental metrics for the FI port by clicking **View Metrics**.

  * Hover over the L1/L2 Ethernet link connecting the FIs:

  * View the status of the L1/L2 link. The L1/L2 link status can be in three possible states—Up, Down, or Partially down. Partially down indicates that there is a mix of links in the **Up** and **Down** state.

  * Hover over the Alarms icon to:

  * View the critical, warning, or information alarms for the server.

  * Navigate to the Alarms View by clicking **Show All**. For more information, see [Alarms](/help/my_dashboard/dashboard_management#alarms).

  * Hover over the Info icon for a FEX to:

  * View the health and details of the FEX.

  * View the FEX on the Inventory page by clicking the link.

  * Hover over a FEX port to:

  * View the health and details of the FEX port.

  * View the port details on the Inventory page by clicking the link.

  * Hover over a VIC Adapter port to:

Note:

The information displayed in these pop-ups is specific to Cisco VICs; details about third-party NICs are not included in this context.

  * View the health and details of the VIC adapter port.

  * View the port details on the Inventory page by clicking the link.


For more information, see the following examples.

**Example 9: C-Series Server connected to a FEX and then to FI**

![](../../../../../../../../en/us/td/i/400001-500000/470001-480000/477055.jpg)

**Example 10: C-Series Server connected directly to FI**

![](../files/C_SeriesServer_FI.png)

## Viewing Unified Edge Topology

The Unified Edge Topology provides a detailed view of the connections within the Unified Edge server.

To view a Unified Edge server topology:

  1. Choose Operate > Unified Edge, to launch the Unified Edge Table view.

  2. Click the Unified Edge server for which you want to view the topology, and then click the Topology tab.

The Unified Edge Topology is displayed.


![](../files/Unified_Edge_Topology.png)

The following information is available in the Unified Edge Topology view:

  * Hover over the Info icon of the Unified Edge server to:

  * View the health and details of the Unified Edge.

  * View the environmental metrics for the Unified Edge by clicking **View Metrics**.

  * Hover over the Alarms icon of the Unified Edge server to:

  * View the critical, warning, or information alarms for the server.

  * Navigate to the Alarms View by clicking **Show All**. For more information, see [Alarms](/help/my_dashboard/dashboard_management#alarms).

  * Hover over the Info icon of eCMC (Edge Chassis Management Controller) to:

  * View the health and details of eCMC. You can also enable or disable admin state of eCMC using the toggle button.

  * View the environmental metrics for the eCMC by clicking **View Metrics**.

  * Hover over the eCMC port to:

  * View the health and details of the eCMC port.

  * View the environmental and network metrics for the eCMC port by clicking **View Metrics**.

  * Hover over a Server to:

  * View the health and details of the server.

  * To highlight the selected server in the foreground in the Topology view, click **View Topology**.

  * View the environmental metrics for the server by clicking **View Metrics**.

  * Hover over the L1/L2 Ethernet links:

  * View the status of the L1/L2 link. The L1/L2 link status can be in three possible states—Up, Down, or Partially down. Partially down indicates that there is a mix of links in the **Up** and **Down** state.


## User Story: Verifying Domain Connectivity

Let us assume that you have just cabled your new UCS domain and claimed your devices in Intersight. You now want to verify the cabling and ensure that all connections are working properly. To get an overview of the entire domain, you can navigate to the topology view of a Fabric Interconnect. This will show you the fabric interconnects pair, as well as all chassis, FEX, and servers that are connected to the domain.

To verify the domain connectivity:

  1. Go to the fabric interconnects topology view.

The fabric interconnects topology view allows you to see if there are any problems at a quick glance. Connections shown in yellow or red indicate that there are connectivity problems between the devices and the Fabric Interconnect.

Note:

Even if the physical connectivity is intact, the connections could be shown in yellow or red if there are alarms generated for the FI port.

![](../files/FabricInterconnectTopology.png)

  2. If problems are detected on any of the links or to verify if cabling is correct, you can double-click the component (chassis or server) to get further details. Alternatively, you can hover over the device and then click on the **View Topology** button to navigate to the detailed view for that specific chassis or server.

For example: Go to Chassis Topology from fabric interconnects Topology.

![](../files/Chassis_Topology.png)

From the Chassis view, you can get better visibility of the ports on the fabric interconnects that are connected to the IO Module on the chassis (IOM or IFM depending on chassis type). You can use this to check the links that have problems. You can also compare your cabling plan with this graphic. You can also view the pinning of the IO Module internal connections to the blades.

