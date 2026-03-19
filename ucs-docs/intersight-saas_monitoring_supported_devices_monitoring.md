# Intersight SaaS Supported Devices for Monitoring

| | |
|---|---|
| **URL Title** | Intersight SaaS Supported Devices for Monitoring |
| **URL** | https://intersight.com/help/saas/monitoring/supported_devices_monitoring |
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260316155144543/docs/cloud/data/resources/monitoring/en/Supported_Devices.html |
| **HTML Title** | Supported Devices |
| **Source file** | `ucs-docs-raw/html/intersight-saas_monitoring_supported_devices_monitoring.html` |
| **File type** | HTML |
| **Fetched on** | 2026-03-19 16:13:28 |

---

# Supported Devices

## Supported Devices

Cisco Intersight supports metrics collection from devices that are managed as an IMM or UMM domain. Only environmental metrics are collected for UMM devices. For more information on supported Fabric Interconnects, Chassis, and Servers and supported firmware, see [Supported Hardware for Intersight Managed Mode](/help/supported_systems#supported_hardware_for_intersight_managed_mode).

Important:

Metric collection for blade servers is only supported for the following Input/Output Module (IOM) models: UCS-IOM-2408, UCSX-I-9108-25G, and UCSX-I-9108-100G.

Note:

  * For metrics collection in IMM domains, all servers must have a valid Intersight license. In UMM domains, at least one server needs a valid Intersight license for metrics collection. For more information, see [Introduction to Intersight Licensing](/help/getting_started/licensing_requirements/lic_intro).

  * Metrics data collection is enabled automatically and cannot be disabled.


## Utilization and Limits Metrics

The following table lists the utilization and limits metrics and the corresponding platforms on which it is supported:

**Servers:**

Supported Server| Instrument| Metrics  
---|---|---  
UCS Blades and Rack Server in Intersight Managed Mode| Physical Processor| Active CPU Utilization  
| Temperature| Upper Non Critical Temperature LimitUpper Critical Temperature Limit  
UCS Racks in Intersight Managed Mode| Fan| Lower Non Critical LimitLower Critical Limit  
| Power Supply| Throttled Power LimitUpper Critical Power Limit  
  
**Chassis:**

Supported Chassis| Instrument| Metrics  
---|---|---  
UCS X-Series Chassis in Intersight Managed Mode| Fan| Max Fan Speed LimitLower Non Critical Fan Speed Limit Lower Critical Fan Speed LimitFan Speed Ratio  
| Power Supply| Upper Critical Power Limit Throttled Power LimitMax Power Limit Power Supply Utilization  
  
For more information on supported Chassis and Servers and supported firmware, see Firmware Requirements for Chassis and Server–Limit and Utilization Metrics Collection.

## Firmware Requirements for VIC Metrics Collection

Note:

The VIC metrics are collected for physical and logical interfaces, and this data collection occurs when the servers are in the powered on state.

The table below shows the minimum server firmware versions required for logical VIC interfaces.

Supported Server| Minimum Server Firmware Version  
---|---  
UCS C-Series servers in Intersight Managed Mode| Server firmware version 4.3(2.230207)  
UCS X-Series servers in Intersight Managed Mode| 

  * UCSX-210C-M6: Server firmware version 5.2(0.230039)
  * UCSX-210C-M7 or UCSX-410C-M7: Server firmware version 5.2(0.230041)

  
  
The table below shows the minimum server firmware versions required to support Network Traffic and Error metrics, and PFC Wait Time metrics for physical VIC interfaces.

Supported Server| Minimum Server Firmware Version  
---|---  
UCS C-Series servers in Intersight Managed Mode| 

  * For 4.3.4.X: 4.3(4.252002) or higher
  * For 4.3.5.X: Not supported
  * For 4.3.6.X: 4.3(6.250077) or higher
  * For 6.0.X: 6.0(1.250127) or higher

  
UCS X-Series servers in Intersight Managed Mode| 

  * For 5.2.X: Not supported
  * For 5.3.X: 5.3(0.250049D) or higher
  * For 5.4.X: 5.4(0.250075) or higher
  * For 6.0.X: 6.0(1.250127) or higher

  
  
## Hardware Requirements for Chassis Metrics Collection

Metrics collection for IMM Chassis is supported only for UCS-IOM-2408 and all models of UCS X-Series Intelligent Fabric Module (IFM).

## Firmware Requirements for Chassis and Server–Limit and Utilization Metrics Collection

Supported Server| Minimum Firmware Version  
---|---  
UCS X-Series Blade servers in Intersight Managed Mode| X-Series: 5.2(2.240053)  
UCS M6+ Rack Server in Intersight Managed Mode| C-Series (M6+): 4.3(4.240152)  
UCS X-Series Chassis in Intersight Managed Mode| X-IFMs: 4.3(4a)  
UCS M7+ Rack Servers in Intersight Standalone Mode| C-Series (M7+): 4.3(4.240152)  
  
Note:

The CPU metrics are not supported for M8 (AMD) C225 and C245.

## Metrics for Supported for the Cisco UCS X580p PCIe Nodes

The following table lists the metrics for the UCS X580p PCIe Nodes:

Supported PCIe Node| Metrics  
---|---  
UCSX-580P in Intersight Managed Mode| 

  * Host Energy
  * Host Power State (PCIe node power on/off status)
  * Hardware Status (Temperature sensor status)
  * Temperature

  
  
Note:

  * The "Host Type" attribute for a PCIe Node is pci.Node.

  * GPU metrics for GPUs present on the PCIe node are collected only when the node is mapped to a server.


## Metrics for Supported GPUs

The following table lists the metrics and the corresponding supported GPUs on which it is supported:

Note:

  * The GPU metrics are supported on Blade and Rack servers managed by an Intersight Managed Mode (IMM) domain.

  * GPU metrics for GPUs present on the PCIe node are collected only when the node is mapped to a server.


Metric| Supported GPUs  
---|---  
GPU Temperature| Nvidia, Intel, AMD  
GPU Power Consumption| Nvidia, Intel, AMD1  
GPU Utilization| Nvidia1  
GPU Memory Utilization| Nvidia1  
GPU Clock Speed| Nvidia  
GPU Memory Clock Speed| Nvidia  
GPU Memory Total| Nvidia  
GPU PCIe Link Width| Nvidia  
GPU PCIe Link Generation| Nvidia  
  
1—Available only after the appropriate drivers are installed. The required drivers depend on both the specific GPUand the operating system installed on the host. You can download the drivers from the [Software Download](https://software.cisco.com/download/home) page.

Note:

The available metrics are determined by the GPU model; newer GPUs provide support for more metrics than older models.

## Firmware Requirements for GPU Metric Collection

Supported Server| Minimum Firmware Version  
---|---  
Cisco UCS X-Series servers in Intersight Managed Mode| 

  * X-Series M8 (X210c): 5.4(0.250037)
  * X-Series M8 (X215c): 5.4(0.250035)
  * X-Series M7 (X210c, X410c): 5.4(0.250035)

  
Cisco UCS C-Series M7 and later servers in Intersight Managed or Intersight Standalone Mode| 

  * C-Series M8 (C240, C220): 4.3(6.250039)
  * C-Series M8 (C885A): 1.1(0.250016)
  * C-Series M8 (C845A): 2.0(1.250096)
  * C-Series M8 (C245, C225): 4.3(6.250040)
  * C-Series M7 (C220, C240): 4.3(6.250040)
