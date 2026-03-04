# Intersight SaaS Monitoring Metrics Devices

| | |
|---|---|
| **URL Title** | Intersight SaaS Monitoring Metrics Devices |
| **URL** | https://intersight.com/help/saas/monitoring/monitoring_metrics_devices |
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260225095216527/docs/cloud/data/resources/monitoring/en/Metrics_FI_Server_Chassis.html |
| **HTML Title** | Fabric Interconnects, Chassis, Unified Edge, and Server Metrics |
| **Source file** | `ucs-docs-raw/html/intersight-saas_monitoring_monitoring_metrics_devices.html` |
| **File type** | HTML |
| **Fetched on** | 2026-03-04 12:48:06 |

---

# Fabric Interconnects, Chassis, Unified Edge, and Server Metrics

## Overview

Cisco Intersight collects metrics for Fabric Interconnects, Chassis, and Servers that are part of an Intersight Managed Mode (IMM) or UCSM Managed Mode (UMM) domain. Metric collection is also supported for Intersight Standalone Mode (ISM) and Unified Edge servers. The raw metrics from these devices are transformed into actionable insights in the form of explorations, dashboards, visualizations, and so on.

Note:

For UMM domains, only the Fabric Interconnects are claimed. Metrics for the Fabric Interconnects, chassis, and servers are reported by the device connector running on the Fabric Interconnects.

You can view and analyze the metrics directly at the device-level, allowing for more detailed, device specific data examination. The device details view for Fabric Interconnects, Chassis, and Servers displays the corresponding metrics for the devices that are part of an IMM or UMM domain. The device-level view provides a more granular insight into the data and enables you to monitor each device directly, assisting in spotting potential issues and simplifying troubleshooting.

Note:

You must claim the Fabric Interconnects, Chassis, and Servers devices as part of an IMM or UMM domain to view the metrics.

## Fabric Interconnects Metrics

The Metrics tab on the Fabric Interconnects Details View page provides you with a comprehensive list of metrics that are collected for the Fabric Interconnects device. The Metrics tab lists all the available metrics and helps you understand and analyze the performance of the device, usage patterns, and overall health.

To view the device-level metrics for Fabric Interconnects, do the following:

1. Log in to Cisco Intersight with your Cisco ID.
2. Choose **Operate** > **Fabric Interconnects** , to launch the Fabric Interconnects Table view.
3. Click the Fabric Interconnects for which you want to view the metrics.

The Fabric Interconnects Details View page is displayed.

4. Click the **Metrics** tab.

Note:

Each column in the Metrics view can be sorted with the Sort option. You can also add filters based on any columns using the Add Filter option to view and explore metrics.

5. To view the metrics for a specific time period, select the time interval for which the data is considered for generating the metrics.

For example, if you select the time interval as Last 24 Hours, the data is displayed for all metrics for the last 24 hours.

6. To gain a detailed perspective of the metrics, do the following:
1. To get a granular view of a metric, click Sparkline for the metric.

The View Metrics page is displayed.

2. To view the granular view for multiple metrics at once, select the desired metrics, click the ellipsis (…) at the top left of the table and select View Metrics.

Note:
  * You can select the time interval and the granularity for which the data points need to be displayed on the chart.

For example, if you select the time interval as Last 24 Hours and set the granularity to 1 hour, the chart will contain 24 aggregated data points.

  * To view the metric in the Metrics Explorer, click View in Explorer.

The following metrics are available for Fabric Interconnects:

* Environmental Metrics
* Network Metrics (applicable only for IMM domain)
* Errors Metrics (applicable only for IMM domain)

For Cisco UCS Fabric Interconnects 9108 100G, Environmental Metrics do not display fan and thermal metrics. The Network Metrics view captures metrics for the fabric ports and the backplane ports.

Note:

* You may need to refresh your screen to view the most up-to-date metrics. To refresh, click the Refresh icon.
* You can export metrics displayed in the Table view to a CSV file. To export and save metrics in a CSV file format, click the Export icon.

You can view the following information for Fabric Interconnects in the Metrics tab:

* Metric—Measurement of the endpoint captured at specific collection intervals. Metrics are numerical values that can be stored in an aggregated form, which is useful when roll-up is applied at ingestion or query time. For example, the measurement of the CPU temperature is a metric.
* Endpoint—The point of origin or source of information for the particular metric.
* Sparkline—A compact chart that provides a visual representation of the metric. The sparkline can help to spot trends, variations, and patterns in the metric.
* Average— The mean value of the sum during the specified time interval.
* Minimum—Lowest value measured during the specified time interval.
* Maximum—Highest value measured during the specified time interval.
* Sum—Sum of the values of all the data points collected during the time interval.
* Last—Most recent measurement of the metric.

## Chassis Metrics

The Metrics tab on the Chassis Details View page provides you with a comprehensive list of metrics that are collected for the chassis. The Metrics tab lists all the available metrics and helps you understand and analyze the performance of the chassis, usage patterns, and overall health.

To view the device-level metrics for Chassis, do the following:

1. Log in to Cisco Intersight with your Cisco ID.
2. Choose **Operate** > **Chassis** , to launch the Chassis Table view.
3. Click the chassis for which you want to view the metrics.

The Chassis Details View page is displayed.

4. Click the **Metrics** tab.

Note:

Each column in the Metrics view can be sorted with the Sort option. You can also add filters based on any columns using the Add Filter option to view and explore metrics.

5. To view the metrics for specific time period, select the time interval for which the data is considered for generating the metrics.

For example, if you select the time interval as Last 24 Hours, the data is displayed for all metrics for the last 24 hours.

6. To gain a detailed perspective of the metrics, do the following:
1. To get a granular view of a metric, click Sparkline for the metric.

The View Metrics page is displayed.

2. To view the granular view for multiple metrics at once, select the desired metrics, click the ellipsis (…) at the top left of the table and select View Metrics.

Note:
  * You can select the time interval and the granularity for which the data points need to be displayed on the chart.

For example, if you select the time interval as Last 24 Hours and set the granularity to 1 hour, the chart will contain 24 aggregated data points.

  * To view the metric in the Metrics Explorer, click View in Explorer.

Note:

* You may need to refresh your screen to view the most up-to-date metrics. To refresh, click the Refresh icon.
* You can export metrics displayed in the Table view to a CSV file. To export and save metrics in a CSV file format, click the Export icon.

You can view the following information for Chassis in the Metrics tab:

* Metric—Measurement of the endpoint captured at specific collection intervals. Metrics are numerical values that can be stored in an aggregated form, which is useful when roll-up is applied at ingestion or query time. For example, the measurement of the CPU temperature is a metric.
* Endpoint—The point of origin or source of information for the particular metric.
* Sparkline—A compact chart that provides a visual representation of the metric. The sparkline can help to spot trends, variations, and patterns in the metric.
* Average— The mean value of the sum during the specified time interval.
* Minimum—Lowest value measured during the specified time interval.
* Maximum—Highest value measured during the specified time interval.
* Sum—Sum of the values of all the data points collected during the time interval.
* Last—Most recent measurement of the metric.

## Server Metrics

The Metrics tab on the Server Details View page provides you with a comprehensive list of metrics that are collected for the server. The Metrics tab lists all the available metrics and helps you understand and analyze the performance of the device, usage patterns, and overall health.

To view the device-level metrics for server, do the following:

1. Log in to Cisco Intersight with your Cisco ID.
2. Choose **Operate** > **Server** , to launch the Server Table view.
3. Click the server for which you want to view the metrics.

The Server Details View page is displayed.

4. Click the **Metrics** tab.

Note:

Each column in the Metrics view can be sorted with the Sort option. You can also add filters based on any columns using the Add Filter option to view and explore metrics.

5. To view the metrics for specific time period, select the time interval for which the data is considered for generating the metrics.

For example, if you select the time interval as Last 24 Hours, the data is displayed for all metrics for the last 24 hours.

6. To gain a detailed perspective of the metrics, do the following:
1. To get a granular view of a metric, click Sparkline for the metric.

The View Metrics page is displayed.

2. To view the granular view for multiple metrics at once, select the desired metrics, click the ellipsis (…) at the top left of the table and select View Metrics.

Note:
  * You can select the time interval and the granularity for which the data points need to be displayed on the chart.

For example, if you select the time interval as Last 24 Hours and set the granularity to 1 hour, the chart will contain 24 aggregated data points.

  * To view the metric in the Metrics Explorer, click View in Explorer.

The following metrics are available for Servers:

* Environmental Metrics
* Errors Metrics (applicable only for IMM domain)

Note:

* You may need to refresh your screen to view the most up-to-date metrics. To refresh, click the Refresh icon.
* You can export metrics displayed in the Table view to a CSV file. To export and save metrics in a CSV file format, click the Export icon.

You can view the following information for Servers in the Metrics tab:

* Metric—Measurement of the endpoint captured at specific collection intervals. Metrics are numerical values that can be stored in an aggregated form, which is useful when roll-up is applied at ingestion or query time. For example, the measurement of the CPU temperature is a metric.
* Endpoint—The point of origin or source of information for the particular metric.
* Sparkline—A compact chart that provides a visual representation of the metric. The sparkline can help to spot trends, variations, and patterns in the metric.
* Average— The mean value of the sum during the specified time interval.
* Minimum—Lowest value measured during the specified time interval.
* Maximum—Highest value measured during the specified time interval.
* Sum—Sum of the values of all the data points collected during the time interval.
* Last—Most recent measurement of the metric.

## Unified Edge

The Metrics tab on the Unified Edge Details View page provides you with a comprehensive list of metrics that are collected for the unified edge server. The Metrics tab lists all the available metrics and helps you understand and analyze the performance of the unified edge server, usage patterns, and overall health.

To view the device-level metrics, do the following:

1. Log in to Cisco Intersight with your Cisco ID.
2. Choose **Operate** > **Unified Edge** , to launch the Unified Edge Table view.
3. Click the unified edge server for which you want to view the metrics.

The Unified Edge Details View page is displayed.

4. Click the **Metrics** tab.

Note:

Each column in the Metrics view can be sorted with the Sort option. You can also add filters based on any columns using the Add Filter option to view and explore metrics.

5. To view the metrics for specific time period, select the time interval for which the data is considered for generating the metrics.

For example, if you select the time interval as Last 24 Hours, the data is displayed for all metrics for the last 24 hours.

6. To gain a detailed perspective of the metrics, do the following:
1. To get a granular view of a metric, click Sparkline for the metric.

The View Metrics page is displayed.

2. To view the granular view for multiple metrics at once, select the desired metrics, click the ellipsis (…) at the top left of the table and select View Metrics.

Note:
  * You can select the time interval and the granularity for which the data points need to be displayed on the chart.

For example, if you select the time interval as Last 24 Hours and set the granularity to 1 hour, the chart will contain 24 aggregated data points.

  * To view the metric in the Metrics Explorer, click View in Explorer.

The following metrics are available:

* Environmental Metrics
* Network Metrics
* Errors Metrics

Note:

* You may need to refresh your screen to view the most up-to-date metrics. To refresh, click the Refresh icon.
* You can export metrics displayed in the Table view to a CSV file. To export and save metrics in a CSV file format, click the Export icon.

You can view the following information for Servers in the Metrics tab:

* Metric—Measurement of the endpoint captured at specific collection intervals. Metrics are numerical values that can be stored in an aggregated form, which is useful when roll-up is applied at ingestion or query time. For example, the measurement of the CPU temperature is a metric.
* Endpoint—The point of origin or source of information for the particular metric.
* Sparkline—A compact chart that provides a visual representation of the metric. The sparkline can help to spot trends, variations, and patterns in the metric.
* Average— The mean value of the sum during the specified time interval.
* Minimum—Lowest value measured during the specified time interval.
* Maximum—Highest value measured during the specified time interval.
* Sum—Sum of the values of all the data points collected during the time interval.
* Last—Most recent measurement of the metric.