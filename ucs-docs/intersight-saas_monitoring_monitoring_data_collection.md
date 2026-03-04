# Intersight SaaS Monitoring Data Collection

| | |
|---|---|
| **URL Title** | Intersight SaaS Monitoring Data Collection |
| **URL** | https://intersight.com/help/saas/monitoring/monitoring_data_collection |
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260225095216527/docs/cloud/data/resources/monitoring/en/Data_Collection.html |
| **HTML Title** | Data Collection |
| **Source file** | `ucs-docs-raw/html/intersight-saas_monitoring_monitoring_data_collection.html` |
| **File type** | HTML |
| **Fetched on** | 2026-03-04 11:00:10 |

---

# Data Collection

Intersight collects inventory information and metrics from devices that are claimed and connected. The connection of these devices is established through device connectors—logical components of each device, which establishes a secure connection to Intersight. The device connectors collect the inventory and metrics locally, and then use the already established secure connection to send the data back to Intersight. For more information on device connectors, see [About Device Connector](/help/resources/configuring_device_connector#about_device_connector).

Note:

Metrics are only collected from Intersight Managed Mode (IMM) or UCSM Managed Mode (UMM) domains. Only environmental metrics are collected for UMM devices. Metric collection is also supported for Intersight Standalone Mode (ISM) servers. For more information, see [Supported Hardware for Intersight Managed Mode](/help/supported_systems#supported_hardware_for_intersight_managed_mode) and [Supported Hardware for Standalone and UCSM Managed Mode](/help/supported_systems#supported_hardware_for_standalone_and_ucsm_managed_mode).

## Supported Devices

Cisco Intersight supports metrics collection from devices that are managed as an IMM or UMM domain. Only environmental metrics are collected for UMM devices. Metric collection is also supported for Intersight Standalone Mode (ISM) servers. For more information on supported Fabric Interconnects, Chassis, and Servers and supported firmware, see [Supported Hardware for Intersight Managed Mode](/help/supported_systems#supported_hardware_for_intersight_managed_mode).

Important:

Metric collection for blade servers is only supported for the following Input/Output Module (IOM) models: UCS-IOM-2408, UCSX-I-9108-25G, and UCSX-I-9108-100G.

Note:

  * For metrics collection in IMM domains, all servers must have a valid Intersight license. In UMM domains, at least one server needs a valid Intersight license for metrics collection. For more information, see [Introduction to Intersight Licensing](/help/getting_started/licensing_requirements/lic_intro).

  * Metric collection on Fabric Interconnects (FIs) is supported only if a valid NTP configuration is in place.

  * Metrics data collection is enabled automatically and cannot be disabled.


## Metrics Collection Process

A metric is a measurement for a specific entity on an endpoint. To learn more about the terminology, see [Terminology](/help/monitoring/monitoring_get_start#terminology). Metrics provide a view of the state, performance, or behavior of instruments. For example, the measurement of CPU temperature for a specific device is a metric. The device connector gathers metrics from the endpoint and then aggregates data points based on the data type. After the metrics are collated, the device connector streams them to Intersight over a secure Internet connection.

For more information on supported instrument types, metrics, and data point types in Cisco Intersight, see [Supported Metrics](/help/monitoring/monitoring_supported_metric).

![](../files/477131.png)

During an outage when the device connector cannot communicate with Intersight, the device connector locally rolls up the data with a lower granularity. As the available memory or storage on the device connector decreases, the rollup interval is gradually increased. For example, instead of retaining measurements at 10-minute intervals, the roll-up interval is gradually increased, which makes it possible to retain data for a longer period of time.

## Metrics Storage

Cisco Intersight collects various metrics for Fabric Interconnects, Chassis, and Servers that are managed as Intersight Managed Mode (IMM) or UCSM Managed Mode domains in Cisco Intersight. Metric collection is also supported for Intersight Standalone Mode (ISM) servers. The frequency of metrics collection, retention period, and down-sampling are managed according to domain type (IMM or UMM) and license tier of the device.

Note:

During down-sampling, data from multiple timestamps is aggregated into a single timestamp. Instead of retaining just one datapoint, down-sampling preserves key statistical measures such as the minimum, maximum, and average (or sum, depending on the metric). This approach ensures that significant details, such as peaks and averages, remain visible even after the data is compressed. The earliest timestamp within the aggregated data is assigned as the new timestamp.

**Metrics Collection for IMM Domain or Intersight Standalone Mode (ISM) Servers**

**Essentials License Tier**

Metrics are collected in 10-minute intervals and then stored at this original granularity. For long-term storage, the metrics are aggregated.

  * First 15 days: Metrics are stored at their original granularity of 10 minutes.

  * From 16 to 63 days: Metrics are down-sampled, in which the existing historical data is re-sampled to a lower frequency and stored at a 30-minute time interval.

  * From 64 to 90 days: Metrics are down-sampled, in which historical data is re-sampled to a lower frequency and stored at a 60-minute time intervals.


For example, if the data is collected at intervals of 10 minutes, the data remains available for 15 days with a 10-minute resolution. After 16 days, this data is still available, but the data is aggregated and is retrievable only with a resolution of 30 minutes. After 64 days to 90 days, the data is further aggregated and is available with a resolution of 60 minutes. After 90 days, the historical data will not be available in Cisco Intersight.

**Advantage License Tier**

Metrics are collected in 1-minute intervals and then stored at this original granularity. For long-term storage, the metrics are aggregated.

  * First 63 days: Metrics are stored at their original granularity of 1 minute.

  * From 63 to 125 days: Metrics are down-sampled, in which the existing historical data is re-sampled to a lower frequency and stored at a 5-minute time interval.

  * From 125 days to 2 years: Metrics are down-sampled, in which historical data is re-sampled to a lower frequency and stored at a 10-minute time intervals.


For example, the data is collected at intervals of 1 minute, the data remains available for 63 days with a 1-minute resolution. After 63 days, this data is still available, but the data is aggregated and is retrievable only with a resolution of 5 minutes. After 125 days to 2 years, the data is further aggregated and is available with a resolution of 10 minutes.

Note:

When an endpoint is removed from Intersight, the corresponding metrics for the endpoint are retained in the metric datastore. However, if the endpoint is claimed again in Intersight it is processed as a new endpoint. To access the historical metric data of a device that is claimed again in Intersight, you must filter the metric query based on a parameter that stays consistent for the end point. For example, you can filter the metric query based on the Serial Number of the endpoint.

**Metrics Collection for UMM Domain**

**Essentials or Advantage License Tier**

Metrics are collected in 10-minute intervals and then stored at this original granularity. For long-term storage, the metrics are aggregated.

  * First 15 days: Metrics are stored at their original granularity of 10 minutes.

  * From 16 to 63 days: Metrics are down-sampled, in which the existing historical data is re-sampled to a lower frequency and stored at a 30-minute time interval.

  * From 64 to 90 days: Metrics are down-sampled, in which historical data is re-sampled to a lower frequency and stored at a 60-minute time intervals.


For example, if the data is collected at intervals of 10 minutes, the data remains available for 15 days with a 10-minute resolution. After 16 days, this data is still available, but the data is aggregated and is retrievable only with a resolution of 30 minutes. After 64 days to 90 days, the data is further aggregated and is available with a resolution of 60 minutes. After 90 days, the historical data will not be available in Cisco Intersight.

## Troubleshooting

For more information about troubleshooting device connector and device connection, see [Troubleshooting Scenarios](https://intersight.com/help/saas/resources/cisco_intersight_managed_mode_configuration#troubleshooting_scenarios).