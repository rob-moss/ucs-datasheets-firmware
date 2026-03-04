# Intersight SaaS Monitoring Get Started

| | |
|---|---|
| **URL Title** | Intersight SaaS Monitoring Get Started |
| **URL** | https://intersight.com/help/saas/monitoring/monitoring_get_started |
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260225095216527/docs/cloud/data/resources/monitoring/en/Getting_Started.html |
| **HTML Title** | Getting Started |
| **Source file** | `ucs-docs-raw/html/intersight-saas_monitoring_monitoring_get_started.html` |
| **File type** | HTML |
| **Fetched on** | 2026-03-04 11:11:08 |

---

# Getting Started

Cisco Intersight collects metrics for devices that are part of an Intersight Manage Mode (IMM) or UCSM Managed (UMM) domain. Only environmental metrics are collected for UMM devices. Metric collection is also supported for Intersight Standalone Mode (ISM) servers. The collected metrics are then exposed as widgets on [dashboards](/help/monitoring/monitoring_dashboard#managing_dashboards), and can also be analyzed using custom metrics [explorations](/help/monitoring/monitoring_metrics_explorer). Before you can use the metric explorations, you must have an [IMM or UMM domain](/help/monitoring/monitoring_get_start#terminology) set up.

Note:

  * To use Intersight Monitoring, you need a Cisco Intersight account. For more information on creating a Cisco Intersight account, see [Account Creation](/help/getting_started/create_cisco_intersight_account#create_an_account).

  * You can view the metric details for the endpoints that have the Intersight Essentials or higher license. For more information, see [Introduction to Intersight Licensing](/help/getting_started/licensing_requirements/lic_intro).

  * Intersight Monitoring is available to users with Account Administrator, Server Administrator, UCS Domain Administrator, Network Administrator, Support Services, or read-only privileges.

  * Intersight enables the logged-in user to access the metrics explorations in only the current organization.


## Setup Guide

  1. **Fabric Interconnects Initial Configuration** —The initial configuration for a Fabric Interconnect is done either using the serial console or graphical user interface (GUI). For more information, see [Setting Up Fabric Interconnects](/help/resources/cisco_intersight_managed_mode_configuration#setting_up_fabric_interconnects).

  2. ****Claim Fabric Interconnects in Intersight** **—To know more about the target claim, see [Target Claim in Intersight Managed Mode](/help/getting_started/claim_targets#target_claim_in_intersight_managed_mode).

  3. ****Configure UCS Domain Profile** **—To know more about the process of configuring a UCS Domain profile, see [Configuring UCS Domain Profiles](/help/resources/cisco_intersight_managed_mode_configuration#creating_domain_profile_template_and_deriving_profiles).

  4. Activate the Intersight Essentials or higher tier license on the servers in the domain.


## Terminology

  * **Instrument** —Instruments are used to report measurements. Each instrument emits measurements, which can then be used as metrics. For example, an instrument can calculate the port utilization and sends the port utilization as a metric.

  * **Metric** —Measurement of the endpoint captured at specific collection intervals. Metrics give you a view of the state, performance, or behavior of the instrument. Metrics are numerical values that can be stored in an aggregated form, which is useful when roll-up is applied at ingestion or query time. For example, the measurement of the CPU temperature is a metric. When the CPU temperature metric is collected for a specific device at a specific point in time it is a metric event.

  * **Timeseries** —Sequence of data points that occur in successive order over a period of time.

  * **Statistics** —Metric data aggregations over specified periods of time. For example, if the _Time Interval_ is 60 minutes, the _Sum_ is the sum of all data points collected during the 60 minute time interval, while the _Minimum_ is the lowest value collected during the 60 minute time interval.

Cisco Intersight supports the following statistics for metrics:

  * **Average** —mean value of sum during the specified time interval.

  * **Latest** —most recent measurement.

  * **Minimum** —lowest value measured during the specified time interval.

  * **Maximum** —highest value measured during the specified time interval.

  * **Sum** —sum of the values of the all data points collected during the time interval.

