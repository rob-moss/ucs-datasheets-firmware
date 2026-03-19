# Intersight SaaS Monitoring Dashboard

| | |
|---|---|
| **URL Title** | Intersight SaaS Monitoring Dashboard |
| **URL** | https://intersight.com/help/saas/monitoring/monitoring_dashboard |
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260316155144543/docs/cloud/data/resources/monitoring/en/Dashboard.html |
| **HTML Title** | Dashboard |
| **Source file** | `ucs-docs-raw/html/intersight-saas_monitoring_monitoring_dashboard.html` |
| **File type** | HTML |
| **Fetched on** | 2026-03-19 16:13:27 |

---

# Dashboard

## Overview

Cisco Intersight offers preconfigured dashboards that provide you a high-level view of all the network assets, inventory, and status information. The dashboards comprise a combination of widgets, with each widget that is designed to provide deeper insights into the data. You can arrange and customize widgets with ease and create personalized dashboards that are tailored to your specific requirements.

The Intersight Widget Library has an extensive list of widgets that cater to a variety of data types and ensure that you have complete control over how the data is presented. Each widget is designed to provide deeper insights into the data.

In addition, Intersight collects metrics from Fabric Interconnects, Chassis, and Servers that are managed as Intersight Managed Mode (IMM) or UCSM Managed Mode domain in Cisco Intersight. This telemetry data is transmitted securely through an encrypted channel to Intersight. You create customized metric explorations for your specific needs using the telemetry metric data and save the explorations as custom widgets in the Intersight Widget Library.

For more information on creating custom widgets, see [Metrics Queries](/help/monitoring/monitoring_metrics_explorer#metrics_queries). For more information on supported instrument types, metric, and the data point types in Cisco Intersight, see [Supported Metrics](/help/monitoring/monitoring_supported_metric).

## Managing Dashboards

Navigate to the Dashboards page. The dashboard page provides you with a high-level view of the status of all the network assets, inventory, and status information. From this page, you can also create custom dashboard views and select specific widgets from the Intersight Widget Library.

![](../files/477138.png)

No.| Dashboard Component| Description  
---|---|---  
**1**|  Dashboard Toolbar| Enables you to view dashboard data and create, clone, rename, and delete dashboard tabs.  
**2**|  Add Filter| Enables you to filter the widget data based on Organizations and Tags.  
**3**|  Widget Visualization| Provides a high-level view of the status of all the network assets, inventory, and status information.In the graphical widgets, hover over the charts or graphs to view a specific set of data. This allows you to further refine the data that is shown and can help with troubleshooting an issue.The following capabilities are available for widgets in the Widget Library:

  * Toggle between the detail and list view of the available widgets in the library.
  * Combine widgets based on type and select the source of data from the selection drawer.
  * Filter widget based on source type in corresponding drawers.

  
**4**|  Refresh icon| Click to refresh your screen and view the most up-to-date data.  
**5**|  Add Widget| Enables you to add widgets to the dashboard.Select the one or more widgets that you want to add to the dashboard, preview the details for a server or a cluster, search for a widget, and add a custom title to a widget.You can use Presets to add a group of widgets that are grouped by source type.  
  
You can create, customize, rename, and manage multiple dashboard views by adding, removing, or rearranging widgets on the dashboard.

**Adding a Dashboard tab**

  1. Choose Dashboards.

  2. Click the + icon on the far right of the Dashboard toolbar.

  3. From the Widget Library, select one or more widgets that you want to pin to the dashboard, preview the details for a server or a cluster, search for a widget, and add a custom title to a widget.

You can use Presets to add a group of widgets that are grouped by source type.

  4. Click Add Widget.


**Modifying a Dashboard tab**

  1. Choose Dashboards.

  2. To add a new widget to the dashboard, do the following:

     1. Click the Dashboard tab to which you want to add a widget.

     2. Click Add Widget to view the available widgets.

     3. From the Widget Library, you can select one or more widgets that you want to pin to the dashboard, preview the details for a server or a cluster, search for a widget, and customize the widget.

You can use Presets to add a group of widgets that are grouped by source type.

     4. Click Add Widget.

  3. To delete a widget from a dashboard view, do the following:

     1. Click the Dashboard tab that you want to delete.

     2. Click the Ellipsis (…) icon next to the widget and select Delete.

     3. Click Delete to confirm the deletion.


**Renaming a Dashboard tab**

  1. Choose Dashboards.

  2. Click the Dashboard tab that you want to rename.

  3. Click the Settings icon (the gear icon) next to the Dashboard tab name and select Rename.

  4. Enter the new name for the dashboard tab.

  5. Click Rename to save the changes.


**Cloning a Dashboard tab**

  1. Choose Dashboards.

  2. Click the Dashboard tab that you want to clone.

  3. Click the Settings icon (the gear icon) next to the Dashboard tab name and select Clone.


**Modifying the widget settings on a Dashboard tab**

  1. Choose Dashboards.

  2. Click the Dashboard tab that you want to modify.

  3. Click the Ellipsis (…) icon next to the widget and select Edit.

  4. Modify the widget setting details.

  5. Click Save Widget.


**Delete a Dashboard tab**

  1. Choose Dashboards.

  2. Click the dashboard tab that you want to delete.

  3. Click the Settings icon (the gear icon) next to the Dashboard tab name and select Delete.

  4. Click Delete to confirm the deletion.


## Widgets Reference

Dashboard widgets are standalone applications that provides information about specific data points. The widgets are designed to display concise data—in the form of charts, graphs, or tables—and enable you to quickly grasp key insights or monitor essential metrics.

![](../files/477139.png)

| Widget Library| Description  
---|---|---  
**1**|  Widgets| The widgets provide information on the health and inventory status of the managed devices in addition to reporting the following real-time data:

  * Alarm Summary—Provides a comprehensive summary of active and suppressed alarms in an account. This consolidated view allows you to monitor the alarm status in real-time, providing key information such as alarm count and severity. This widget helps to track and manage alarms, ensuring effective monitoring and prompt actions when necessary.
  * Alarm Suppression Summary—Offers a comprehensive summary of the devices Alarm Suppression enabled. This dashboard allows you to efficiently monitor the current state of Alarm Suppression.
  * Custom Metric—Real-time status of a metric that you want to view. You can choose to create a widget to display graphs/charts for a supported metric type, and select the required time interval and the level of granularity for one or more domains.
  * Health Summary—Health of all managed Fabric Interconnects, HyperFlex Clusters, and Servers.
  * Inventory—Inventory for all managed Fabric Interconnects, HyperFlex Clusters, and Servers.
  * Infrastructure Service License Status—Indicates the current state of the license and the number of servers managed. Based on the current license state, the days left on the trial period, days remaining for license expiry, or days left on the grace period are displayed.
  * Version Summary—Total number of managed targets distributed by the version.
  * Server Version Summary—Total number of managed servers distributed by the installed firmware version. The top 8 firmware versions are displayed. If there are more than 7 unique firmware versions, they are collectively reported in the Others category.
  * Fabric Interconnect Version Summary—Total number of managed Fabric Interconnects distributed by the installed firmware version.
  * HyperFlex Version Summary—Total number of HyperFlex clusters distributed by the installed HyperFlex Data Platform version.
  * Model Summary—Number of managed servers per server model. The top 7 models present in the inventory are displayed. All other models are collectively reported in the Others category.
  * Profile Summary—Summary of Profiles based on status. Attention includes profiles in the Not Deployed and Failed states, In Progress includes profiles in the Configuring and Validating states.
  * Details—Snapshot of the selected Server or HyperFlex Cluster.
  * Server Details—Details of a server, including Model, Server Profile, HCL Status, and Firmware version. From this widget, you can directly launch the corresponding Server Details page.
  * HyperFlex Cluster Details—Details of a HyperFlex cluster, including (number of) Nodes, Capacity, Utilization, and HyperFlex version. From this widget, you can directly launch the corresponding HyperFlex Cluster Details page.
  * Device Contract Coverage—Reflects the contract status for servers, chassis and Fabric Interconnects over a period of time, distributed by validity of contract.
  * Energy Consumption—The total energy consumption based on selected device types. All Devices, Fabric Interconnects, and Servers.
  * Errors—Reflects the daily total count of errors. The hover state shows the top count of errors by port and associated device for the selected time interval.
  * Total Power Consumption—Reflects cumulative power consumption state based on selected device types.
  * Power Consumption—Reflects power consumption state based on selected device types.
  * Top 5 by Alarms—Top 5 alarms for HyperFlex clusters in descending order of Critical alarm count. If there are fewer than 5 clusters with Critical alarms, clusters sorted in the descending order of the Warning alarm count are displayed.
  * Top 5 by Bandwidth Utilization—The top ports and associated devices by bandwidth utilization for Fabric Interconnects.
  * Top 5 Energy Consumption—Top 5 energy consumption based for Fabric Interconnects and Servers.
  * Top 5 by Utilization—Top 5 resource utilization for HyperFlex clusters distributed by the % of Storage Utilization.
  * Last Activity—Indicates number of requests in progress and requests completed in the last 24 hours. Completed requests could be in Successful, Failed, Terminated, or Waiting states.
  * Virtual Machines Per Device—Total number of virtual machines per device. The chart indicates the number of virtual machines per host and per storage device.
  * Contract Status—Reflects the contract status for Fabric Interconnects, HyperFlex Clusters, and Servers over a period of time, distributed by validity of contract.
  * Server HCL Status Summary—Summary of the Hardware Compatibility List (HCL) status for the managed servers.
  * HyperFlex Clusters Capacity Runway—Displays the number of HyperFlex clusters for which the storage utilization is predicted to exceed the predefined threshold of 76%.
  * Inventory—Inventory for all managed devices and hardware.
  * Last Activity—Indicates the activity completed in the last 24 hours.
  * Pending Actions—Pending actions by type, severity, and entity type.
  * Storage Device Details—Displays the top 5 storage arrays or storage volumes based on capacity utilization, and the storage version summary information. From these widgets, you can directly launch the corresponding Storage Details page.
  * Temperature—Displays the top devices by temperature.

  
**2**|  Presets| Presets provide a view of widgets grouped by source type. The following presets are available:

  * Fabric Interconnects—Displays Fabric Interconnect details including inventory, contract status, and health summary.
  * Fabric Interconnects Metrics—Displays Fabric Interconnect metrics including bandwidth utilization and count of errors. The widgets included are Top FI Uplink Ports by Network Utilization, Top FI Uplink Port Channels by Network Utilization, Top FI Server Ports by Network Utilization, Top FI Downlink Port Channels by Network Utilization, and so on.
  * HyperFlex Clusters—Displays HyperFlex cluster details including inventory, capacity runway, and health summary.
  * Power & Energy Metrics—Displays energy and power metrics including energy consumption and power consumption.
  * Servers—Displays server details including inventory, HCL status, and server profile summary.
  * Servers Metrics—Displays server metrics including average CPU temperature and inlet temperature.
  * Storage—Displays storage details including version summary, and arrays and volumes by capacity utilization.
  * Workload Optimizer—Displays Workload Optimizer details including pending actions, virtual machines by devices, and Workload Optimizer license status.

You can use Presets to add a group of widgets that are grouped by source type. For instance, you can add all the widgets available to monitor HyperFlex clusters by adding the HyperFlex Cluster Preset to the dashboard.  
**3**|  Create New Metric Widget| Enables you to create customized widgets for your specific needs using the telemetry metric data.You create customized widgets for your specific needs using the telemetry metric data and save the explorations as custom widgets. For more information on creating custom widgets, see [Metrics Queries](/help/monitoring/monitoring_metrics_explorer#metrics_queries). For more information on supported instrument types, metric, and the data point types in Cisco Intersight, see [Supported Metrics](/help/monitoring/monitoring_supported_metric).  
  
## Network Utilization Widget

The Network Utilization widget shows you historical data about your network interfaces. The columns include details such as the RX and TX utilization, as well as error counts. The columns also include the hostname, port, port type, and port role to make it easy to identify the port.

Use these instructions to add the widget to your dashboard and customize the Network Utilization widget:

  1. Choose Dashboards, and click Add Widget.

The widget library displays.

  2. Click Select on the Network Utilization widget to open the widget settings.

![](../files/NetworkUtilization.png)
  3. Add a title for the widget that you want to create.

  4. Specify Select Interval—The time interval for which data will be pulled into the widget. The available options are 4 hours, 12 hours, or 24 hours. This allows you to filter the data based on recent activity or longer-term trends.

  5. Select Display Limit—The maximum number of records that will be displayed by the widget. By limiting the number of records, you can manage the amount of data shown at once, ensuring the widget remains readable and useful.

  6. Specify Filter By—The condition or rule to filter the data displayed in the widget. The filter can be used to include or exclude certain data based on specific criteria, enabling more targeted data analysis.

For example, you can use these filters to create the following network utilization widgets:

  * FI Uplink Ports— _Filter By condition_ : Port Role as _eth_uplink_ , _fc_uplink_ , _appliance_ , or _fcoe_uplink_

  * FI Uplink Port Channels— _Filter By condition_ : Port Role as _eth_uplink_pc_ , _fc_uplink_pc_ , or _fcoe_uplink_pc_

  * FI Server Ports— _Filter By condition_ : Port Role as _server_

  * FI Downlink Port Channels— _Filter By condition_ : Port Role as _server_pc_ , or _fabric_pc_

  7. Select Statistics—The type of statistical calculation to apply to the data, either Average or Maximum. Maximum will allow you to easily identify peaks in your network utilization. Average is better suited for identifying your utilization over time. The maximum could seem very high due to single outliers, which the average will smooth out.

  8. Select Sort By Column—This field specifies which column to sort the data by. The best column to sort by for network utilization on a port is the Avg/Max % RX and Avg/Max % TX. This will sort by both directions of traffic. If you want to achieve a different goal, you can also sort by the other columns.

  9. Use Thresholds Per Endpoint toggle to specify the thresholds per endpoint—The threshold limits used to classify the utilization of each port into OK, Warning, and Critical states. These limits apply individually to each endpoint measured, rather than to a cumulative value, helping you to identify specific endpoints that may require attention.

Note:

These thresholds are specific to this widget only; they are not global and do not trigger any alarms.

  10. Click Save.

