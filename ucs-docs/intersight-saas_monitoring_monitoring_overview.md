# Intersight SaaS Monitoring Overview

| | |
|---|---|
| **URL Title** | Intersight SaaS Monitoring Overview |
| **URL** | https://intersight.com/help/saas/monitoring/monitoring_overview |
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260324061034657/docs/cloud/data/resources/monitoring/en/Monitoring_Overview.html |
| **HTML Title** | Overview |
| **Source file** | `ucs-docs-raw/html/intersight-saas_monitoring_monitoring_overview.html` |
| **File type** | HTML |
| **Fetched on** | 2026-03-25 11:32:45 |

---

# Overview

Intersight offers a wide array of options to monitor your data center environment. The devices connected to Intersight report inventory information, metrics, and alerts back to Intersight, which you can then view.

The information about the connected environment is also enriched with more information by Cisco:

  * [Hardware Compatibility List (HCL)](/help/resources/compliance_with_hcl#viewing_hardware_compatibility_list_status)—Checks if your server and firmware combination is validated by Cisco

  * [Advisories](/help/resources#intersight_advisories)—Lists known vulnerabilities and other information for your specific environment.

  * [Service Contract](/help/my_dashboard/dashboard_elements#contract_status_widgets)—Checks if your device has an active service contract with Cisco.

  * [Dashboards](/help/monitoring/monitoring_dashboard)— Preconfigured dashboards that give you a comprehensive overview of your environment—all of the assets, status information, and metrics. These dashboards consists of various widgets, each offering a unique perspective on your environment.

  * [Alarms](/help/my_dashboard/dashboard_management#alarms)—Provides fault monitoring capabilities to track and set up alarms for all managed targets.

  * [Metrics Explorer](/help/monitoring/monitoring_metrics_explorer)—Offers real-time and historical views of system performance to support resource management and diagnostics.

  * [Topology View](/help/monitoring/topology)—Provides intuitive visual representation of the components in an IMM domain and display the connections and relationships between these components.


Note:

The information available can vary based on device type and license level.

Intersight collectes metrics from Fabric Interconnects, Chassis, and Servers that are managed as either Intersight Managed Mode (IMM) or UCS Managed Mode (UMM) domains within Cisco Intersight. Metric collection is also supported for Intersight Standalone Mode (ISM) servers. You can use the [Metrics Explorer](/help/monitoring/monitoring_metrics_explorer) to monitor your devices, optimize performance, identify bottlenecks, and proactively address any potential issues. Intersight Monitoring serves the following primary purposes:

  * Metrics Explorer aggregate metrics data and enables you to visualize various metrics that are collected for Fabric Interconnects, Chassis, and Servers that are managed as Intersight Managed Mode (IMM) or UCSM Managed Mode (UMM) domain in Cisco Intersight

  * Provides both real-time and historical views of system performance to aid in resource management and diagnostics.

  * Query metrics for the endpoints that are part of an IMM or UMM domain, or Intersight Standalone Mode (ISM) servers.

  * Allows you to create custom metric queries to obtain specific data.

  * Customizes the visual presentation of the metric data across multiple devices, identify performance trends, and perform root cause analysis for intermittent issues.

  * Dashboards and in-built widgets.

  * Offers topology views of the components in an IMM domain.

Note:

Topology view is available only for the IMM domains.


Explore the following sections to learn more about metrics in Intersight:

  * [**Getting Started**](/help/monitoring/monitoring_get_start)

Provides information about the initial setup and first steps for Monitoring in Intersight.

  * [**Data Collection**](/help/monitoring/monitoring_data_collection)

Explains how data collection and storage work and provides information about supported systems.

  * [**Metrics Explorer**](/help/monitoring/monitoring_metrics_explorer)

Explains how you can freely explore the data stored in Intersight to create your own analysis.

  * [**Fabric Interconnects, Chassis, and Server Metrics**](/help/monitoring/monitoring_metrics_devices)

Explains how you can view and analyze the metrics directly at the device level for Fabric Interconnects, Chassis, and Servers.

  * [**Topology View**](/help/monitoring/topology)

Provides intuitive visual representation of the components in an IMM domain and display the connections and relationships between these components.

  * [**Dashboard**](/help/monitoring/monitoring_dashboard)

Provides an overview of Dashboard, how to create and manage custom dashboards, and widget references.

  * [**Metrics Tutorials**](/help/monitoring/monitoring_tutorial_user_stories)

Provides step-by-step instruction and expert tips for a few generic use cases.

  * [**Supported Metrics**](/help/monitoring/monitoring_supported_metric)

Provides details about all the metrics that are collected by Intersight.

  * [**API Documentation**](../../../../apidocs/introduction/supported-metrics-overview/)

Provides an overview of Telemetry API and how you can query time series information from Intersight.

