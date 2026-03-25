# Intersight SaaS Monitoring Metrics Explorer

| | |
|---|---|
| **URL Title** | Intersight SaaS Monitoring Metrics Explorer |
| **URL** | https://intersight.com/help/saas/monitoring/monitoring_metrics_explorer |
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260324061034657/docs/cloud/data/resources/monitoring/en/Metrics_Explorer.html |
| **HTML Title** | Metrics Exploration |
| **Source file** | `ucs-docs-raw/html/intersight-saas_monitoring_monitoring_metrics_explorer.html` |
| **File type** | HTML |
| **Fetched on** | 2026-03-25 11:32:47 |

---

# Metrics Exploration

## Overview

Intersight Metrics Explorer empowers you to aggregate and visualize various metrics that are collected for Fabric Interconnects, Chassis, and Servers that are managed as Intersight Managed Mode (IMM) or UCSM Managed Mode (UMM) domain in Cisco Intersight. Metric collection is also supported for Intersight Standalone Mode (ISM) servers. You can use the Metrics Explorer queries to monitor your devices, optimize performance, identify bottlenecks, and proactively address any potential issues. For more information on IMM Domains, see [Cisco Intersight Managed Mode Configuration Guide.](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Intersight_Managed_Mode_Configuration_Guide/b_intersight_managed_mode_guide_chapter_01010.html)

The key features of Intersight Metrics Explorer are:

  * **Customizable Metric Queries** —Enables you to create custom metric queries that are tailored to your specific needs, making it easier for you to focus on the metrics that matter most to you. You can create metrics queries with the user interface that enables you to effortlessly construct queries without the need to write complex code.

  * **Interactive Data Visualization** —Allows you to transform raw data into visualizations with interactive charts and graphs that enable you to identify patterns, anomalies, and trends to gain deeper insights.

  * **Real-time Data** —Provides real-time insights into the performance metrics. Interactive charts and graphs enable you to track crucial metrics, such as network power consumption, CPU temperature, resource utilization, and so on. This enables you to spot trends and anomalies as they happen.

  * **Historical Data** —Enables you to analyze the historical data and identify long-term performance trends and make data-driven decisions for future optimizations.


## Understanding Metrics Explorer

Cisco Intersight collects metrics for Fabric Interconnects, Chassis, and Servers that are part of an Intersight Managed Domain. The Metrics Explorer interface helps you to transform raw metrics data into actionable intelligence. This simplified and accelerated data exploration empowers you to unearth meaningful patterns, identify trends, and make informed decisions.

Choose Analyze > Explorer. From this page, you can create metrics exploration queries, view metrics explorations, and create dashboard widgets.

![](../files/477132.png)

No.| Component| Description  
---|---|---  
**1**| **Add Metrics**|  Enables you to create or modify the metric query.

  * Metrics—Create custom metric queries that are tailored to your specific needs. You specify the metric as a combination of the instrument, metric data point type, and statistics.Cisco Intersight supports the following statistics for metrics:
  * **Average** —the mean value of sum either during the specified time interval or within the granularity period.
  * **Minimum** —the lowest value measured either during the specified time interval or within the granularity period.
  * **Maximum** —the highest value measured either during the specified time interval or within the granularity period.
  * **Sum** —the total of all data points collected either during the time interval or within the granularity period.Note:The statistics list above are not applicable to all the metrics. For more information on statistic applicable for each metric, see [Supported Metrics](/help/monitoring/monitoring_supported_metric).
  * Filter By—(Optional) The condition or rule based on which the metric data is selected or excluded. The Filter By rule is specified on an attribute of the metric, combined with a condition and a value. If you have Tags defined on the element monitored by Intersight, they will also be available for filtering.
  * Group By—(Optional) The metric attribute(s) that you want to use to group the metric.The key attributes for the metric are highlighted in the Group by drop-down, which are prominently listed at the top of the drop-down menu with a tick symbol next to each. To group the metrics by all the key attributes, Select All Key Attributes.
  * Display—(Optional) The display options:
  * To show all records in the chart, select All .
  * To limit the number of records shown in the chart, select Top N and specify the number.
  * **Aggregate Time Series** —(Optional) Combine all displayed time series into a single time series using the selected aggregation. The options are:
  * **Average** —the mean value of sum either during the specified time interval or within the granularity period.
  * **Minimum** —the lowest value measured either during the specified time interval or within the granularity period.
  * **Maximum** —the highest value measured either during the specified time interval or within the granularity period.
  * **Sum** —the total of all data points collected either during the time interval or within the granularity period.

  
**2**| **Metrics Visualization**|  Enables you to choose the way in which you want to visualize the results of the metric queries.

  * **Chart Type** —You can select the charts based on the following options: Bar, Line, Table, Pie, or Count.
  * **Time Interval** —Time period for which the data points should be displayed in the chart. For example, when you select the time interval as Last Month, the chart displays the aggregated data points collected in the last one month.
  * **Granularity** —Determines how many data points are retrieved within the chosen time interval. For example, if you have selected a time interval of _Last 24 Hours_ , a granularity of _1 hour_ , it will result in 24 aggregated data points. If you had chosen _15 minutes_ instead, you would get 360 aggregated data points for all the 15 minute periods during the day.

  
**3**| **Metrics Query Data and Results**|  Displays the details about the results obtained from the metric query.

  * **Raw Data** —Displays the read-only API response as a table.
  * **Distinct Endpoints** —Displays a list of endpoints for which the metrics are available. To view metrics for a specific endpoint, select it from the list and click ellipses (…) > Add to Metrics Filter. For example, when examining the Fan-Speed-Average metric, you can select an endpoint from the list and add it to Metrics Filter. This sets the Filter by condition for the metrics, using the "Domain Name," "Host Name," and "Name" of the endpoint. Consequently, it presents data specifically for that chosen endpoint.
  * **Display Options** —Enables you to customize the orientation of the Y-axis for a bar or line chart.
  * **Code** —Displays the read-only API request for the metric query.
  * **Result** —Displays the read-only API response as raw JSON.

  
  
Note:

Customize your network metrics display by selecting either bits per second (bps) or bytes per second (Bps). To change units, go to Profile Menu > User Settings > Network Units toggle and choose your preferred option. The default unit is bits per second.

Your selection applies across Metrics Explorer, Dashboard widgets (including bandwidth utilization), topology, and the Metrics tab, and will persist across sessions. Metric names, descriptions, and units update automatically—for example, Network RX Bytes becomes Network RX Bits.

## Metrics Queries

To create a metric query, do the following:

  1. Choose Analyze.

  2. Select the metric for which you want to review the data. You specify the metric as a combination of the instrument type, metric or attribute, and the data point types or statistics. For example, you can select the metrics as _Host Power and Status_ (Instrument Type), _Host Power_ (Metric) and _Minimum_ (Statistics).

The Explorer screen displays the metrics as a single line chart for all the endpoints.

For more information on supported instrument types, metric, and statistics in Cisco Intersight, see [Supported Metrics](/help/monitoring/monitoring_supported_metric).

  3. (Optional) Select the condition by which you want to filter the metrics. The Filter By rule is specified on an attribute of the metric, combined with a condition and a value. If you have Tags defined on the element monitored by Intersight, they will also be available for filtering.

You specify filter condition when you want to focus on a filtered subset of data rather than the entire dataset. For example, for _Temperature - Average_ metric, when you select the Filter by condition with attribute as _Host Type_ , condition as _include_ , and value as _Fabric Interconnect_ , the corresponding chart displays the data points for a single metric—Average Temperature for Fabric Interconnect and is shown as a single line on the chart.

![](../files/477133.png)

Alternately, for Temperature - Average metric, when you select the Filter by condition with attribute as _Host Type_ , condition as _exclude_ , and value as _Fabric Interconnect_ , the corresponding chart displays the metric for _Blade Server_ and _Rack Server_.

![](../files/477134.png)
  4. (Optional) In the Group by field, specify the metric attribute you want to use for grouping the metric.

You specify the Group by condition when you want to focus on data for specific entities or groups of entities. For example, for _Temperature - Average_ metric, for Fabric Interconnect, when you select the Group by condition as _Sensor Location_ , the metric is aggregated based on the sensor location— _Server_back_ , _Server_CPU_ , and _Server_front_ —and the corresponding chart displays the metric for each sensor location separately.

The key attributes for the metric are highlighted in the Group by drop-down, which are prominently listed at the top of the drop-down menu with a tick symbol next to each. To group the metrics by all the key attributes, Select All Key Attributes.

For example, for the _Fan - Fan Speed - Average_ metric includes _Domain Name_ , _Host Name_ , and _Name_ as its key attributes.

![](../files/477135.png)
  5. To specify the display options, do one of the following:

  * To show all records in the chart, select All .

  * To limit the number of records shown in the chart, select Top N and specify the number.

Note:

Top N uses the same selected statistic across the entire interval.

  6. Select the Aggregate Time Series option to aggregate the time series data. The options are:

  * **Average** —the mean value of sum either during the specified time interval or within the granularity period.

  * **Minimum** —the lowest value measured either during the specified time interval or within the granularity period.

  * **Maximum** —the highest value measured either during the specified time interval or within the granularity period.

  * **Sum** —the total of all data points collected either during the time interval or within the granularity period.

  7. Select one of the following chart types for the metric:

  * **Bar** —Bar or column charts display discontinuous events and show the differences between events rather than trends. Bar charts are oriented vertically and are stacked vertically.

  * **Line** —Line charts show continuous quantities over time against a common scale and are good for viewing trends.

  * **Table** —Table charts shows the time series data in rows and columns.

  * **Pie** —Pie charts present a count of numbers in the query.

  * **Count** —Count chart shows the number of occurrences of each category in a data set. It is a simple and effective way to visualize the distribution of data.

  8. Select the time interval for which the data points need to be displayed on the chart.

For example, when you select the time interval as Last Month, the chart displays the aggregated data points collected in the last one week.

![](../files/477136.png)
  9. Select the time period for which the data is considered for generating a single, aggregated data point.

For example, if you select the time interval as Last 24 Hours and set the granularity to 1 hour, the chart will contain 24 aggregated data points.

![](../files/477137.png)
  10. To add an additional metric, click the Clone metric icon or click the Add Metrics button and repeat the steps _3-10_ for the newly added metric.

  11. Click **Save** to save the exploration.

  12. From the Organization drop-down list, choose the organization for the metric.

  13. Specify the display name and description.

  14. To add the metric as a widget to Intersight Widget Library, do the following:

  * Toggle **ON** the Add to Dashboard button.

  * Select the Dashboard to which the metric widget needs to be added.

  15. Click **Save**.


## Metrics Visualization

**Viewing Metric**

To view the metric, do the following:

  1. Choose Analyze.

  2. Click View my Explorations.

  3. Select the metric exploration for which you want to view the data.

  4. Select the options to visualize the results of the metric queries.

The following table describes the options available :

Option| Description  
---|---  
**Chart Type**| 
  * **Bar** —Bar or column charts display discontinuous events and show the differences between events rather than trends. Bar charts are oriented vertically and are stacked vertically.
  * **Line** —Line charts show continuous quantities over time against a common scale and are good for viewing trends.
  * **Table** —Table charts shows the time series data in rows and columns.
  * **Pie** —Pie charts present a count of numbers in the query.
  * **Count** —Count chart shows the number of occurrences of each category in a data set. It is a simple and effective way to visualize the distribution of data.  
**Time Interval**|  The time interval for which the data points are displayed in the chart. For example, when you select the time interval as Last 24 Hours the chart displays the aggregated data points collected in the last 24 hours.  
**Granularity**|  Select the time period for which data is considered for generating a single, aggregated data point.  
**Raw Data**|  Displays the read-only raw data for the metric definition.Click Export to export and download the metric as a CSV file.  
**Distinct Endpoints**| **Distinct Endpoints** —Displays a list of endpoints for which the metrics are available. To view metrics for a specific endpoint, select it from the list and click ellipses (…) > Add to Metrics Filter. For example, when examining the Fan-Speed-Average metric, you can select an endpoint from the list and add it to Metrics Filter. This sets the Filter by condition for the metrics, using the "Domain Name," "Host Name," and "Name" of the endpoint. Consequently, it presents data specifically for that chosen endpoint.  
**Display Options**|  Enables you to customize the display options for a bar or line chart.To customize the orientation of the Y-Axis, do the following:
     1. Click Display Options tab.
     2. Toggle ON the Customize Y-Axis button.
     3. Select the orientation of the Y-Axis.  
**Code**|  Displays the read-only API request for the metric query.For example:
    
    [
      {
        "queryType": "groupBy",
        "dataSource": "PhysicalEntities",
        "granularity": {
          "type": "period",
          "period": "PT30M",
          "timeZone": "Asia/Calcutta"
        },
        "intervals": [
          "2023-07-17T12:10:00.000Z/2023-07-18T12:10:00.000Z"
        ],
        "dimensions": [
          "sensor_location",
          "airflow_location"
        ],
        "filter": {
          "type": "and",
          "fields": [
            {
              "type": "selector",
              "dimension": "instrument.name",
              "value": "hw.temperature"
            }
          ]
        },
        "aggregations": [
          {
            "type": "doubleMin",
            "name": "hw-temperature_min-Min",
            "fieldName": "hw.temperature_min"
          }
        ]
      }
    ]  
  
**Result**|  Displays the read-only API response for the metric query.For example:
    
    [
      {
        "status": "fulfilled",
        "value": [
          {
            "version": "v1",
            "timestamp": "2023-07-14T12:00:00.000+05:30",
            "event": {
              "hw-temperature-Avg": 32.04262295081967,
              "count": 1220,
              "hw.temperature-Sum": 39092
            }
          },
          {
            "version": "v1",
            "timestamp": "2023-07-15T00:00:00.000+05:30",
            "event": {
              "hw-temperature-Avg": 32.23125,
              "count": 1440,
              "hw.temperature-Sum": 46413
            }
          },
       ...  
  
