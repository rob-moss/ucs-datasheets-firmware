# Intersight SaaS Monitoring SFP Metric

| | |
|---|---|
| **URL Title** | Intersight SaaS Monitoring SFP Metric |
| **URL** | https://intersight.com/help/saas/monitoring/sfp_metric |
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260225095216527/docs/cloud/data/resources/monitoring/en/sfp_metrics.html |
| **HTML Title** | Metric Collection for Transceivers |
| **Source file** | `ucs-docs-raw/html/intersight-saas_monitoring_sfp_metric.html` |
| **File type** | HTML |
| **Fetched on** | 2026-03-04 12:48:06 |

---

# Metric Collection for Transceivers

Cisco Intersight collects metrics from Fabric Interconnects that are part of an Intersight Managed Mode (IMM) or UCSM Managed Mode (UMM) domain. For transceivers that are plugged into Fabric Interconnects, the following metrics are collected–temperature, Tx power, Rx power, current, and voltage. These metrics collectively can help you understand the health and performance of transceiver modules, enabling you to proactively identify and resolve issues, ensuring reliable and efficient network operations.

Here are some key uses of temperature and signal power monitoring information:

* Preventing overheating and thermal damage
* Ensuring signal integrity and link stability
* Troubleshooting network issues
* Optimizing network performance
* Compliance and reporting

Note:

* The transceiver metrics require an Advantage tier license and is available only if a transceiver is present and Digital Optical Monitoring (DOM) is supported and enabled by the transceiver.
* Transceiver metrics are available only for Ethernet ports and not for FC ports.

The transceiver metrics collected for Fabric Interconnects are:

* **Signal Power > Rx Power: **The Rx Power metric measures the optical power received by the transceiver module. It is critical for ensuring that the signal strength is adequate for reliable data transmission. Low Rx power levels can indicate issues such as dirty connectors or faulty cables, potentially leading to data corruption and CRC errors. The unit of signal power is in decibels per milliwatt (dBm) at which a sensor receives its signal.
* **Signal Power > Tx Power:** The Tx Power metric measures the optical power transmitted by the transceiver module. This metric is essential for ensuring that the signal being sent out is strong enough to reach the receiver without significant degradation. Abnormal Tx power levels can suggest problems with the transceiver module or indicate issues with the connected hardware.
* **Electric Current:** The Transceiver Current metric measures the electrical current drawn by the transceiver module. Monitoring this metric helps identify potential hardware issues, as abnormal current levels can indicate faulty components or electrical problems within the module.
* **Temperature:** The Temperature metric measures the operating temperature of the transceiver module. Maintaining an optimal temperature range is crucial for the performance and longevity of the transceiver module. High temperatures can lead to thermal stress and eventual hardware failure, while low temperatures can affect performance.
* **Voltage:** The Voltage metric measures the electrical voltage supplied to the transceiver module. Proper voltage levels are essential for stable operation. Deviations from the expected voltage range can cause unstable performance and may indicate electrical issues that need to be addressed.

The Metric Explorer allows you to create a visual representation of the transceiver metrics collected for Fabric Interconnects. It allows you to create custom metric queries tailored to your specific needs, enabling you to focus on the most relevant metrics. For more information, see [Metrics Explorer](/help/monitoring/monitoring_metrics_explorer).

In addition, you can specify a filter by condition when you want to focus on a filtered subset of data rather than the entire dataset.

To view metrics specifically for transceivers, set the filter to _Sensor Name = Transceivers_. This allows you to focus on data related to transceivers. For example, if you want to see the _Temperature_ metric, set the filter with _Sensor Name_ as the attribute, _Equals_ as the condition, and _Transceiver_ as the value. This will display the relevant data points on the chart. The transceiver parent name is the port on Fabric Interconnects to which transceiver is connected to. Additionally, you can use _Sensor Location_ or _Parent Name_ as the Group by condition to aggregate the data based on your chosen criteria.

## Use Case: Using Transceiver Metrics for Troubleshooting CRC Issues

A key use case for the transceiver metrics gathered in Intersight is troubleshooting Cyclic Redundancy Check (CRC) errors. The transceiver Rx (Received) and Tx (Transmitted) power metrics are crucial for diagnosing CRC errors. Identifying CRC errors that occur alongside fluctuating Rx or Tx power levels can help pinpoint the root cause of the issue.

Here is how these metrics can help identify and resolve issues that might be causing CRC errors:

Note:

For additional details on the Rx and Tx power for transceiver, see [Cisco Optics-to-Device Compatibility Matrix](https://tmgmatrix.cisco.com/) or [Cisco Optics Product Information](https://copi.cisco.com/).

1. **Identifying Signal Strength Issues:**
* **Low Rx Power:**
* **Symptom:** If the received optical power (Rx power) is lower than the acceptable threshold, it indicates weak signal strength at the receiver end.
* **Impact:** Weak signals can lead to data corruption, resulting in CRC errors.
* **High Tx Power:**
* **Symptom:** Transmitted optical power (Tx power) being higher than the specified range can cause the receiver to be overwhelmed, leading to data errors.
* **Impact:** Overloaded receivers can fail to correctly interpret the incoming signal, leading to CRC errors.
2. **Detecting Fiber Optic Degradation:**
* **Consistent Decline in Rx Power:**
* **Symptom:** A gradual decline in Rx power over time may indicate fiber degradation or increasing attenuation.
* **Impact:** Degraded fibers can cause intermittent signal loss and data corruption, resulting in CRC errors.
3. **Ensuring Proper Optical Link Budget:**
* **Mismatch Between Tx and Rx Power:**
* **Symptom:** Significant discrepancies between Tx power at the transmitter and Rx power at the receiver can suggest issues with the optical link budget.
* **Impact:** Poor optical link budgets can lead to insufficient signal strength, causing CRC errors.
4. **Isolating Faulty Components:**
* **Unstable Power Levels:**
* **Symptom:** Fluctuating Tx or Rx power levels can indicate faulty transceiver modules or unstable connections.
* **Impact:** Unstable power levels can cause inconsistent signal quality, leading to CRC errors.