# Intersight SaaS Monitoring User Case CPU Utilization

| | |
|---|---|
| **URL Title** | Intersight SaaS Monitoring User Case CPU Utilization |
| **URL** | https://intersight.com/help/saas/monitoring/monitoring_usercase_cpu_Utilization |
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260324061034657/docs/cloud/data/resources/monitoring/en/Tutorial-C0-CPU-Utilization.html |
| **HTML Title** | Tutorial: Active CPU Utilization Metrics for Monitoring Server Performance |
| **Source file** | `ucs-docs-raw/html/intersight-saas_monitoring_monitoring_usercase_cpu_Utilization.html` |
| **File type** | HTML |
| **Fetched on** | 2026-03-25 11:32:51 |

---

# Tutorial: Active CPU Utilization Metrics for Monitoring Server Performance

This use case highlights the advantages of monitoring server CPU utilization using the Active CPU Utilization metric. By leveraging this metric, you gain valuable insights into system performance, enabling the identification of unusual patterns and potential bottlenecks. Notably, the Active CPU Utilization metric does not require an OS agent, as it monitors directly from the hardware. This means that you can monitor servers that do not provide any monitoring from their operating system. This metric is particularly useful for detecting servers that are heavily overloaded (approaching 100% usage) or identifying those that are underutilized (approaching 0% usage).

Further analyzing the Active CPU Utilization metrics allows you to pinpoint peak usage times often linked to specific tasks or user activities that demand more resources. By investigating workloads during these peaks, you can identify and optimize resource-intensive applications, adjusting resource allocation or rescheduling tasks to off-peak hours for a balanced load and smooth server operation.

This proactive approach ensures optimal server performance, aids in planning for future growth and upgrades, and helps maintain a robust network environment.

To view the Active CPU Utilization metrics, do the following:

  1. Navigate to **Metrics Explorer**.

  2. In the Metrics Explorer, select instrument type as **Physical Processor** , metrics as **Active CPU Utilization**.

  3. Choose the statistic for the metrics. Depending on the type of metrics you wish to view, select the statistics as follows:

  * **Maximum** : The highest percentage of time the CPU is in the active state over the monitoring period. This is crucial for identifying peak usage times and potential bottlenecks.

  * **Minimum** : The lowest percentage of time the CPU is in the active state during the monitoring period. This helps identify periods of minimal activity.

  * **Average** : The average percentage of time the CPU remains in the active state over a specified period.

The Metric Explorer displays the Active CPU Utilization line graph across all devices.

  4. To view the data for the hosts, in the **Group By** condition, select **Host Name**. The Metric Explorer displays the Active CPU Utilization line graph for each host.

  5. Specify the **Filter By** condition to view the Active CPU Utilization metrics for a specific domain. Use the **Domain Name** to do so. Our final filter should then look like this:

![](../files/CPU_utilization.png)
