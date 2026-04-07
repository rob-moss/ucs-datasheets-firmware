# Intersight SaaS Supported Metrics for Monitoring

| | |
|---|---|
| **URL Title** | Intersight SaaS Supported Metrics for Monitoring |
| **URL** | https://intersight.com/help/saas/monitoring/monitoring_supported_metric |
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260402103337138/docs/cloud/data/resources/monitoring/en/Supported_Metrices.html |
| **HTML Title** | Data Export |
| **Source file** | `ucs-docs-raw/html/intersight-saas_monitoring_monitoring_supported_metric.html` |
| **File type** | HTML |
| **Fetched on** | 2026-04-08 08:43:26 |

---

# Supported Metrics  
  
The page lists the IMM metrics that are supported in Intersight currently. APIDocs contain a detailed description for each of the metrics. For detailed information about each metric, click the metric hyperlink below to navigate to APIDocs.

## Physical Processor

**Name:**[hw.cpu](../../../../apidocs/introduction/hw-cpu)

Physical processor (as opposed to the logical processor seen by the operating system for multicore systems). A physical processor may include many individual cores.Label| Name| Description| Instrument Type  
| Value Type| Units  
---|---|---|---|---|---  
[Active CPU Utilization](../../../../apidocs/introduction/hw-cpu/#metric-active-cpu-utilization)| [hw.cpu.utilization_c0](../../../../apidocs/introduction/hw-cpu/#metric-active-cpu-utilization)| The percentage of CPU time that was spent in C0 (active) power state. This metric represents a single aggregated value across all CPUs.| Gauge| float64| %  
  
## Electric Current

**Name:**[hw.current](../../../../apidocs/introduction/hw-current)

An electric current sensor, either numeric or discrete.Label| Name| Description| Instrument Type  
| Value Type| Units  
---|---|---|---|---|---  
[Electric Current](../../../../apidocs/introduction/hw-current/#metric-electric-current)| [hw.current](../../../../apidocs/introduction/hw-current/#metric-electric-current)| Electric current measured by the sensor in Ampere. In case of a transceiver, this is the laser bias current, which is the amount of electrical current supplied to the laser diode within the transceiver to generate the optical signal for transmission. Transceiver electric current metric requires advantage license and is available only if transceiver is present and DOM(Digital optical monitoring) is enabled.| Gauge| float64| A  
  
## Fan

**Name:**[hw.fan](../../../../apidocs/introduction/hw-fan)

A fan in a Server, Chassis, Fabric Interconnect or PSU.Label| Name| Description| Instrument Type  
| Value Type| Units  
---|---|---|---|---|---  
[Fan Speed](../../../../apidocs/introduction/hw-fan/#metric-fan-speed)| [hw.fan.speed](../../../../apidocs/introduction/hw-fan/#metric-fan-speed)| Fan speed in revolutions per minute (rpm).| Gauge| int64| rpm  
[Lower Critical Fan Speed Limit](../../../../apidocs/introduction/hw-fan/#metric-lower-critical-fan-speed-limit)| [hw.fan.speed.limit_low_critical](../../../../apidocs/introduction/hw-fan/#metric-lower-critical-fan-speed-limit)| The lower critical fan speed limit.| Gauge| int64| rpm  
[Lower Non Critical Fan Speed Limit](../../../../apidocs/introduction/hw-fan/#metric-lower-non-critical-fan-speed-limit)| [hw.fan.speed.limit_low_degraded](../../../../apidocs/introduction/hw-fan/#metric-lower-non-critical-fan-speed-limit)| The lower non critical fan speed limit.| Gauge| int64| rpm  
[Max Fan Speed Limit](../../../../apidocs/introduction/hw-fan/#metric-max-fan-speed-limit)| [hw.fan.speed.limit_max](../../../../apidocs/introduction/hw-fan/#metric-max-fan-speed-limit)| The maximum speed of the fan.| Gauge| int64| rpm  
[Fan Speed Ratio](../../../../apidocs/introduction/hw-fan/#metric-fan-speed-ratio)| [hw.fan.speed_ratio](../../../../apidocs/introduction/hw-fan/#metric-fan-speed-ratio)| Fan speed expressed as a percentage of its maximum speed.| Gauge| float64| %  
[Hardware Status](../../../../apidocs/introduction/hw-fan/#metric-hardware-status)| [hw.status](../../../../apidocs/introduction/hw-fan/#metric-hardware-status)| The operational status: 1 (true) or 0 (false) for each of the possible states. At query time, you can use the following aggregation functions: 1. Use longMax aggregation to determine if the component was up at least once during each rollup interval. 2. Use longMin aggregation to determine if the component was down at least once during each rollup interval. 3. Use ( longSum / count ) to determine the percentage of time when the component was up during each rollup interval.| UpDownCounter| int64| 1  
  
## Graphical Processing Unit

**Name:**[hw.gpu](../../../../apidocs/introduction/hw-gpu)

A Graphical Processing Unit in a Server. Certain GPU metrics are available only when the GPU drivers are installed on the host system.Label| Name| Description| Instrument Type  
| Value Type| Units  
---|---|---|---|---|---  
[GPU Clockspeed](../../../../apidocs/introduction/hw-gpu/#metric-gpu-clockspeed)| [hw.gpu.clockspeed](../../../../apidocs/introduction/hw-gpu/#metric-gpu-clockspeed)| Operating clockspeed of GPU.| Gauge| int64| Hz  
[GPU Total Bytes](../../../../apidocs/introduction/hw-gpu/#metric-gpu-total-bytes)| [hw.gpu.io_all](../../../../apidocs/introduction/hw-gpu/#metric-gpu-total-bytes)| Received and transmitted bytes by the GPU.| Gauge| int64| By  
[GPU RX Bytes](../../../../apidocs/introduction/hw-gpu/#metric-gpu-rx-bytes)| [hw.gpu.io_receive](../../../../apidocs/introduction/hw-gpu/#metric-gpu-rx-bytes)| Received bytes by the GPU.| Gauge| int64| By  
[GPU TX Bytes](../../../../apidocs/introduction/hw-gpu/#metric-gpu-tx-bytes)| [hw.gpu.io_transmit](../../../../apidocs/introduction/hw-gpu/#metric-gpu-tx-bytes)| Transmitted bytes by the GPU.| Gauge| int64| By  
[GPU Memory Clockspeed](../../../../apidocs/introduction/hw-gpu/#metric-gpu-memory-clockspeed)| [hw.gpu.memory.clockspeed](../../../../apidocs/introduction/hw-gpu/#metric-gpu-memory-clockspeed)| Operating clockspeed of GPU memory.| Gauge| int64| Hz  
[GPU Memory Limit](../../../../apidocs/introduction/hw-gpu/#metric-gpu-memory-limit)| [hw.gpu.memory.limit](../../../../apidocs/introduction/hw-gpu/#metric-gpu-memory-limit)| Size of the GPU memory.| UpDownCounter| int64| By  
[GPU Memory Utilization](../../../../apidocs/introduction/hw-gpu/#metric-gpu-memory-utilization)| [hw.gpu.memory.utilization](../../../../apidocs/introduction/hw-gpu/#metric-gpu-memory-utilization)| Percentage of GPU memory utilization.| Gauge| float64| %  
[GPU PCIe Link Generation](../../../../apidocs/introduction/hw-gpu/#metric-gpu-pcie-link-generation)| [hw.gpu.pcie_link_gen](../../../../apidocs/introduction/hw-gpu/#metric-gpu-pcie-link-generation)| PCIe generation in use for given GPU.| Gauge| int64| 1  
[Maximum GPU PCIe Link Generation](../../../../apidocs/introduction/hw-gpu/#metric-maximum-gpu-pcie-link-generation)| [hw.gpu.pcie_link_gen_limit](../../../../apidocs/introduction/hw-gpu/#metric-maximum-gpu-pcie-link-generation)| Maximum PCIe generation supported in GPU.| Gauge| int64| 1  
[GPU PCIe Link Width](../../../../apidocs/introduction/hw-gpu/#metric-gpu-pcie-link-width)| [hw.gpu.pcie_link_width](../../../../apidocs/introduction/hw-gpu/#metric-gpu-pcie-link-width)| Number of PCIe lanes in use for given GPU.| Gauge| int64| {count}  
[Maximum GPU PCIe Link Width](../../../../apidocs/introduction/hw-gpu/#metric-maximum-gpu-pcie-link-width)| [hw.gpu.pcie_link_width_limit](../../../../apidocs/introduction/hw-gpu/#metric-maximum-gpu-pcie-link-width)| Maximum Number of PCIe lanes present in GPU.| Gauge| int64| {count}  
[GPU Power Consumption](../../../../apidocs/introduction/hw-gpu/#metric-gpu-power-consumption)| [hw.gpu.power](../../../../apidocs/introduction/hw-gpu/#metric-gpu-power-consumption)| GPU instantaneous power consumption in Watts.| Gauge| float64| W  
[GPU Utilization](../../../../apidocs/introduction/hw-gpu/#metric-gpu-utilization)| [hw.gpu.utilization](../../../../apidocs/introduction/hw-gpu/#metric-gpu-utilization)| Percentage of overall GPU utilization.| Gauge| float64| %  
[Hardware Status](../../../../apidocs/introduction/hw-gpu/#metric-hardware-status)| [hw.status](../../../../apidocs/introduction/hw-gpu/#metric-hardware-status)| The operational status: 1 (true) or 0 (false) for each of the possible states. At query time, you can use the following aggregation functions: 1. Use longMax aggregation to determine if the component was up at least once during each rollup interval. 2. Use longMin aggregation to determine if the component was down at least once during each rollup interval. 3. Use ( longSum / count ) to determine the percentage of time when the component was up during each rollup interval.| UpDownCounter| int64| 1  
  
## Host Power and Status

**Name:**[hw.host](../../../../apidocs/introduction/hw-host)

A Server or Fabric Interconnect.Label| Name| Description| Instrument Type  
| Value Type| Units  
---|---|---|---|---|---  
[Host Energy](../../../../apidocs/introduction/hw-host/#metric-host-energy)| [hw.host.energy](../../../../apidocs/introduction/hw-host/#metric-host-energy)| Total energy consumed by the entire physical host, in joules.| Counter| float64| J  
[Host Power](../../../../apidocs/introduction/hw-host/#metric-host-power)| [hw.host.power](../../../../apidocs/introduction/hw-host/#metric-host-power)| Instantaneous power consumed by the entire physical host, in Watts.| Gauge| float64| W  
[Host Power State](../../../../apidocs/introduction/hw-host/#metric-host-power-state)| [hw.host.power_state](../../../../apidocs/introduction/hw-host/#metric-host-power-state)| The power state of the host: 1 (on) or 0 (off). At query time, you can use the following aggregation functions: 1. Use longMax aggregation to determine if the host was on at least once during each rollup interval. 2. Use longMin aggregation to determine if the host was off at least once during each rollup interval. 3. Use ( longSum / hw.host.power_state_count ) to determine the percentage of time when the host was on during each rollup interval.| UpDownCounter| int64| 1  
  
## Memory Module

**Name:**[hw.memory](../../../../apidocs/introduction/hw-memory)

A memory module in a Server or Fabric Interconnect.Label| Name| Description| Instrument Type  
| Value Type| Units  
---|---|---|---|---|---  
[Correctable ECC Errors](../../../../apidocs/introduction/hw-memory/#metric-correctable-ecc-errors)| [hw.errors_correctable_ecc_errors](../../../../apidocs/introduction/hw-memory/#metric-correctable-ecc-errors)| Number of correctable ECC errors that were detected on the memory module. This metric is only available when the host is in a powered-on state.| Counter| int64| {errors}  
[Uncorrectable ECC Errors](../../../../apidocs/introduction/hw-memory/#metric-uncorrectable-ecc-errors)| [hw.errors_uncorrectable_ecc_errors](../../../../apidocs/introduction/hw-memory/#metric-uncorrectable-ecc-errors)| Number of uncorrectable ECC errors that were detected on the memory module. This metric is only available when the host is in a powered-on state.| Counter| int64| {errors}  
[Memory Size](../../../../apidocs/introduction/hw-memory/#metric-memory-size)| [hw.memory.size](../../../../apidocs/introduction/hw-memory/#metric-memory-size)| The size of the memory module. This metric is only available when the host is in a powered-on state.| UpDownCounter| int64| By  
[Hardware Status](../../../../apidocs/introduction/hw-memory/#metric-hardware-status)| [hw.status](../../../../apidocs/introduction/hw-memory/#metric-hardware-status)| The operational status of the memory module.| UpDownCounter| int64| 1  
  
## Network Interface

**Name:**[hw.network](../../../../apidocs/introduction/hw-network)

A physical or logical network interface on a Server, IOM or Fabric Interconnect.Label| Name| Description| Instrument Type  
| Value Type| Units  
---|---|---|---|---|---  
[Network Carrier Sense Errors](../../../../apidocs/introduction/hw-network/#metric-network-carrier-sense-errors)| [hw.errors_network_carrier_sense](../../../../apidocs/introduction/hw-network/#metric-network-carrier-sense-errors)| Number of times the absence of a carrier signal is detected on the interface before attempting to transmit data.| Counter| int64| {errors}  
[Network Late Collision Errors](../../../../apidocs/introduction/hw-network/#metric-network-late-collision-errors)| [hw.errors_network_late_collisions](../../../../apidocs/introduction/hw-network/#metric-network-late-collision-errors)| Number of times collisions are detected after the collision window has elapsed on the network interface.| Counter| int64| {errors}  
[Network Link Failure Errors](../../../../apidocs/introduction/hw-network/#metric-network-link-failure-errors)| [hw.errors_network_link_failures](../../../../apidocs/introduction/hw-network/#metric-network-link-failure-errors)| Number of times the loss of connectivity has been detected on the network interface.| Counter| int64| {errors}  
[Total Network RX Errors](../../../../apidocs/introduction/hw-network/#metric-total-network-rx-errors)| [hw.errors_network_receive_all](../../../../apidocs/introduction/hw-network/#metric-total-network-rx-errors)| Number of errors encountered during the reception of data by the network interface which is reported as the summation of all the receive errors.| Counter| int64| {errors}  
[Network RX CRC Errors](../../../../apidocs/introduction/hw-network/#metric-network-rx-crc-errors)| [hw.errors_network_receive_crc](../../../../apidocs/introduction/hw-network/#metric-network-rx-crc-errors)| Number of received packets (or frames) that have failed the CRC check on the network interface.| Counter| int64| {errors}  
[Network RX Discard Errors](../../../../apidocs/introduction/hw-network/#metric-network-rx-discard-errors)| [hw.errors_network_receive_discard](../../../../apidocs/introduction/hw-network/#metric-network-rx-discard-errors)| Number of packets (or frames) that are received but not processed and discarded by the network interface.| Counter| int64| {errors}  
[Network No Buffer Errors](../../../../apidocs/introduction/hw-network/#metric-network-no-buffer-errors)| [hw.errors_network_receive_no_buffer](../../../../apidocs/introduction/hw-network/#metric-network-no-buffer-errors)| Number of received frames that were dropped due to unavailability of the buffer on the network interface.| Counter| int64| {errors}  
[Network Receive Oversize Bad CRC Errors](../../../../apidocs/introduction/hw-network/#metric-network-receive-oversize-bad-crc-errors)| [hw.errors_network_receive_oversize_bad_crc](../../../../apidocs/introduction/hw-network/#metric-network-receive-oversize-bad-crc-errors)| Number of oversized packets (or frames) with bad CRC status received on the network interface.| Counter| int64| {errors}  
[Network Receive Oversize Good CRC Errors](../../../../apidocs/introduction/hw-network/#metric-network-receive-oversize-good-crc-errors)| [hw.errors_network_receive_oversize_good_crc](../../../../apidocs/introduction/hw-network/#metric-network-receive-oversize-good-crc-errors)| Number of oversized packets (or frames) with good CRC status received on the network interface.| Counter| int64| {errors}  
[Network RX Pause Frames](../../../../apidocs/introduction/hw-network/#metric-network-rx-pause-frames)| [hw.errors_network_receive_pause](../../../../apidocs/introduction/hw-network/#metric-network-rx-pause-frames)| Number of received pause packets (or frames) on the network interface.| Counter| int64| {errors}  
[Network Runt Errors](../../../../apidocs/introduction/hw-network/#metric-network-runt-errors)| [hw.errors_network_receive_runt](../../../../apidocs/introduction/hw-network/#metric-network-runt-errors)| Number of received ethernet frames with a size smaller than the IEEE 802.3's minimum length of 64 octets.| Counter| int64| {errors}  
[Network Too Long Errors](../../../../apidocs/introduction/hw-network/#metric-network-too-long-errors)| [hw.errors_network_receive_too_long](../../../../apidocs/introduction/hw-network/#metric-network-too-long-errors)| Number of oversized packets (or frames) received on the network interface.| Counter| int64| {errors}  
[Network Too Short Errors](../../../../apidocs/introduction/hw-network/#metric-network-too-short-errors)| [hw.errors_network_receive_too_short](../../../../apidocs/introduction/hw-network/#metric-network-too-short-errors)| Number of undersized packets (or frames) received on the network interface.| Counter| int64| {errors}  
[Network Receive Undersize Bad CRC Errors](../../../../apidocs/introduction/hw-network/#metric-network-receive-undersize-bad-crc-errors)| [hw.errors_network_receive_undersize_bad_crc](../../../../apidocs/introduction/hw-network/#metric-network-receive-undersize-bad-crc-errors)| Number of undersized packets (or frames) with bad CRC status received on the network interface.| Counter| int64| {errors}  
[Network Receive Undersize Good CRC Errors](../../../../apidocs/introduction/hw-network/#metric-network-receive-undersize-good-crc-errors)| [hw.errors_network_receive_undersize_good_crc](../../../../apidocs/introduction/hw-network/#metric-network-receive-undersize-good-crc-errors)| Number of undersized packets (or frames) with good CRC status received on the network interface.| Counter| int64| {errors}  
[Network Signal Loss Errors](../../../../apidocs/introduction/hw-network/#metric-network-signal-loss-errors)| [hw.errors_network_signal_losses](../../../../apidocs/introduction/hw-network/#metric-network-signal-loss-errors)| Number of times the loss of signal has been detected on the network interface.| Counter| int64| {errors}  
[Network Sync Loss Errors](../../../../apidocs/introduction/hw-network/#metric-network-sync-loss-errors)| [hw.errors_network_sync_losses](../../../../apidocs/introduction/hw-network/#metric-network-sync-loss-errors)| Number of times the synchronization between the transmitting and receiving devices is lost during data transmission on the network interface.| Counter| int64| {errors}  
[Total Network TX Errors](../../../../apidocs/introduction/hw-network/#metric-total-network-tx-errors)| [hw.errors_network_transmit_all](../../../../apidocs/introduction/hw-network/#metric-total-network-tx-errors)| Number of errors encountered during the transmission of data from the network interface which is reported as the summation of all the transmit errors.| Counter| int64| {errors}  
[Network TX Deferred Errors](../../../../apidocs/introduction/hw-network/#metric-network-tx-deferred-errors)| [hw.errors_network_transmit_deferred](../../../../apidocs/introduction/hw-network/#metric-network-tx-deferred-errors)| Number of packets (or frames) that have been temporarily postponed or delayed from immediate transmission by the network interface.| Counter| int64| {errors}  
[Network TX Discard Errors](../../../../apidocs/introduction/hw-network/#metric-network-tx-discard-errors)| [hw.errors_network_transmit_discard](../../../../apidocs/introduction/hw-network/#metric-network-tx-discard-errors)| Number of packets (or frames) that are not successfully transmitted and are instead discarded by the network interface.| Counter| int64| {errors}  
[Network Jabber Errors](../../../../apidocs/introduction/hw-network/#metric-network-jabber-errors)| [hw.errors_network_transmit_jabber](../../../../apidocs/introduction/hw-network/#metric-network-jabber-errors)| Number of transmitted ethernet frames with a size more than the length allowed by the Ethernet standard.| Counter| int64| {errors}  
[Network TX Pause Frames](../../../../apidocs/introduction/hw-network/#metric-network-tx-pause-frames)| [hw.errors_network_transmit_pause](../../../../apidocs/introduction/hw-network/#metric-network-tx-pause-frames)| Number of transmitted pause packets (or frames) on the network interface.| Counter| int64| {errors}  
[Network Receive Drop Errors](../../../../apidocs/introduction/hw-network/#metric-network-receive-drop-errors)| [hw.errors_receive_drops](../../../../apidocs/introduction/hw-network/#metric-network-receive-drop-errors)| Number of receive packets (or frames) that were dropped.| Counter| int64| {errors}  
[Network Transmit Drop Errors](../../../../apidocs/introduction/hw-network/#metric-network-transmit-drop-errors)| [hw.errors_transmit_drops](../../../../apidocs/introduction/hw-network/#metric-network-transmit-drop-errors)| Number of transmit packets (or frames) that were dropped.| Counter| int64| {errors}  
[Operational Link Speed](../../../../apidocs/introduction/hw-network/#metric-operational-link-speed)| [hw.network.bandwidth.limit](../../../../apidocs/introduction/hw-network/#metric-operational-link-speed)| The operational speed of the network interface, in bytes per second.| UpDownCounter| int64| By/s  
[Network Utilization](../../../../apidocs/introduction/hw-network/#metric-network-utilization)| [hw.network.bandwidth.utilization_all](../../../../apidocs/introduction/hw-network/#metric-network-utilization)| Utilization of the network bandwidth as a percentage.| Gauge| float64| %  
[Network RX Utilization](../../../../apidocs/introduction/hw-network/#metric-network-rx-utilization)| [hw.network.bandwidth.utilization_receive](../../../../apidocs/introduction/hw-network/#metric-network-rx-utilization)| RX Utilization of the network bandwidth as a percentage.| Gauge| float64| %  
[Network TX Utilization](../../../../apidocs/introduction/hw-network/#metric-network-tx-utilization)| [hw.network.bandwidth.utilization_transmit](../../../../apidocs/introduction/hw-network/#metric-network-tx-utilization)| TX Utilization of the network bandwidth as a percentage.| Gauge| float64| %  
[Network TX Buffer Credit Left](../../../../apidocs/introduction/hw-network/#metric-network-tx-buffer-credit-left)| [hw.network.bb_credit_left_transmit](../../../../apidocs/introduction/hw-network/#metric-network-tx-buffer-credit-left)| The available buffer credits for the network interface. This ensures that the sender never transmits a packet that the network interface does not have a buffer to hold it in.| UpDownCounter| int64| {packets}  
[Network RX Buffer Credit Limit](../../../../apidocs/introduction/hw-network/#metric-network-rx-buffer-credit-limit)| [hw.network.bb_credit_limit_receive](../../../../apidocs/introduction/hw-network/#metric-network-rx-buffer-credit-limit)| The maximum number of buffer credits that the network interface can have. The sender never transmits a packet to the network interface beyond this limit.| UpDownCounter| int64| {packets}  
[Network TX Buffer Credit Limit](../../../../apidocs/introduction/hw-network/#metric-network-tx-buffer-credit-limit)| [hw.network.bb_credit_limit_transmit](../../../../apidocs/introduction/hw-network/#metric-network-tx-buffer-credit-limit)| The maximum number of buffer credits that the network interface can have. The network interface never transmits a packet to the receiver beyond this limit.| UpDownCounter| int64| {packets}  
[Network Interface Resets](../../../../apidocs/introduction/hw-network/#metric-network-interface-resets)| [hw.network.interface_resets](../../../../apidocs/introduction/hw-network/#metric-network-interface-resets)| Number of times the interface is reset.| Counter| int64| 1  
[Network Bytes](../../../../apidocs/introduction/hw-network/#metric-network-bytes)| [hw.network.io_all](../../../../apidocs/introduction/hw-network/#metric-network-bytes)| Received and transmitted network traffic in bytes.| Counter| int64| By  
[Network RX Bytes](../../../../apidocs/introduction/hw-network/#metric-network-rx-bytes)| [hw.network.io_receive](../../../../apidocs/introduction/hw-network/#metric-network-rx-bytes)| Received network traffic in bytes.| Counter| int64| By  
[Network RX Broadcast Bytes](../../../../apidocs/introduction/hw-network/#metric-network-rx-broadcast-bytes)| [hw.network.io_receive_broadcast](../../../../apidocs/introduction/hw-network/#metric-network-rx-broadcast-bytes)| Received broadcast network traffic in bytes.| Counter| int64| By  
[Network RX Multicast Bytes](../../../../apidocs/introduction/hw-network/#metric-network-rx-multicast-bytes)| [hw.network.io_receive_multicast](../../../../apidocs/introduction/hw-network/#metric-network-rx-multicast-bytes)| Received multicast network traffic in bytes.| Counter| int64| By  
[Network RX Unicast Bytes](../../../../apidocs/introduction/hw-network/#metric-network-rx-unicast-bytes)| [hw.network.io_receive_unicast](../../../../apidocs/introduction/hw-network/#metric-network-rx-unicast-bytes)| Received unicast network traffic in bytes.| Counter| int64| By  
[Network TX Bytes](../../../../apidocs/introduction/hw-network/#metric-network-tx-bytes)| [hw.network.io_transmit](../../../../apidocs/introduction/hw-network/#metric-network-tx-bytes)| Transmitted network traffic in bytes.| Counter| int64| By  
[Network TX Broadcast Bytes](../../../../apidocs/introduction/hw-network/#metric-network-tx-broadcast-bytes)| [hw.network.io_transmit_broadcast](../../../../apidocs/introduction/hw-network/#metric-network-tx-broadcast-bytes)| Transmitted broadcast network traffic in bytes.| Counter| int64| By  
[Network TX Multicast Bytes](../../../../apidocs/introduction/hw-network/#metric-network-tx-multicast-bytes)| [hw.network.io_transmit_multicast](../../../../apidocs/introduction/hw-network/#metric-network-tx-multicast-bytes)| Transmitted multicast network traffic in bytes.| Counter| int64| By  
[Network TX Unicast Bytes](../../../../apidocs/introduction/hw-network/#metric-network-tx-unicast-bytes)| [hw.network.io_transmit_unicast](../../../../apidocs/introduction/hw-network/#metric-network-tx-unicast-bytes)| Transmitted unicast network traffic in bytes.| Counter| int64| By  
[Network RX Packets](../../../../apidocs/introduction/hw-network/#metric-network-rx-packets)| [hw.network.packets_receive](../../../../apidocs/introduction/hw-network/#metric-network-rx-packets)| Received network traffic in packets (or frames).| Counter| int64| {packets}  
[RX Packets Size 1024 to 1518](../../../../apidocs/introduction/hw-network/#metric-rx-packets-size-1024-to-1518)| [hw.network.packets_receive_1024_to_1518](../../../../apidocs/introduction/hw-network/#metric-rx-packets-size-1024-to-1518)| Received network traffic in packets (or frames) with size between 1024 and 1518.| Counter| int64| {packets}  
[RX Packets Size 128 to 255](../../../../apidocs/introduction/hw-network/#metric-rx-packets-size-128-to-255)| [hw.network.packets_receive_128_to_255](../../../../apidocs/introduction/hw-network/#metric-rx-packets-size-128-to-255)| Received network traffic in packets (or frames) with size between 128 and 255.| Counter| int64| {packets}  
[RX Packets Size 1519 or Above](../../../../apidocs/introduction/hw-network/#metric-rx-packets-size-1519-or-above)| [hw.network.packets_receive_1519_to_max](../../../../apidocs/introduction/hw-network/#metric-rx-packets-size-1519-or-above)| Received network traffic in packets (or frames) with size of 1519 or above.| Counter| int64| {packets}  
[RX Packets Size Less Than 64](../../../../apidocs/introduction/hw-network/#metric-rx-packets-size-less-than-64)| [hw.network.packets_receive_1_to_63](../../../../apidocs/introduction/hw-network/#metric-rx-packets-size-less-than-64)| Received network traffic in packets (or frames) with size less than 64.| Counter| int64| {packets}  
[RX Packets Size 256 to 511](../../../../apidocs/introduction/hw-network/#metric-rx-packets-size-256-to-511)| [hw.network.packets_receive_256_to_511](../../../../apidocs/introduction/hw-network/#metric-rx-packets-size-256-to-511)| Received network traffic in packets (or frames) with size between 256 and 511.| Counter| int64| {packets}  
[RX Packets Size 512 to 1023](../../../../apidocs/introduction/hw-network/#metric-rx-packets-size-512-to-1023)| [hw.network.packets_receive_512_to_1023](../../../../apidocs/introduction/hw-network/#metric-rx-packets-size-512-to-1023)| Received network traffic in packets (or frames) with size between 512 and 1023.| Counter| int64| {packets}  
[RX Packets Size 64](../../../../apidocs/introduction/hw-network/#metric-rx-packets-size-64)| [hw.network.packets_receive_64](../../../../apidocs/introduction/hw-network/#metric-rx-packets-size-64)| Received network traffic in packets (or frames) with size of 64.| Counter| int64| {packets}  
[RX Packets Size 65 to 127](../../../../apidocs/introduction/hw-network/#metric-rx-packets-size-65-to-127)| [hw.network.packets_receive_65_to_127](../../../../apidocs/introduction/hw-network/#metric-rx-packets-size-65-to-127)| Received network traffic in packets (or frames) with size between 65 and 127.| Counter| int64| {packets}  
[Network RX Broadcast Packets](../../../../apidocs/introduction/hw-network/#metric-network-rx-broadcast-packets)| [hw.network.packets_receive_broadcast](../../../../apidocs/introduction/hw-network/#metric-network-rx-broadcast-packets)| Received broadcast network traffic in packets (or frames).| Counter| int64| {packets}  
[Network RX Multicast Packets](../../../../apidocs/introduction/hw-network/#metric-network-rx-multicast-packets)| [hw.network.packets_receive_multicast](../../../../apidocs/introduction/hw-network/#metric-network-rx-multicast-packets)| Received multicast network traffic in packets (or frames).| Counter| int64| {packets}  
[Network RX Priority Pause Frames](../../../../apidocs/introduction/hw-network/#metric-network-rx-priority-pause-frames)| [hw.network.packets_receive_ppp](../../../../apidocs/introduction/hw-network/#metric-network-rx-priority-pause-frames)| Received priority pause frames on the network interface.| Counter| int64| {packets}  
[Network RX RSS Packets](../../../../apidocs/introduction/hw-network/#metric-network-rx-rss-packets)| [hw.network.packets_receive_rss](../../../../apidocs/introduction/hw-network/#metric-network-rx-rss-packets)| Received network traffic in packets (or frames) that were processed using RSS.| Counter| int64| {packets}  
[Network RX Unicast Packets](../../../../apidocs/introduction/hw-network/#metric-network-rx-unicast-packets)| [hw.network.packets_receive_unicast](../../../../apidocs/introduction/hw-network/#metric-network-rx-unicast-packets)| Received unicast network traffic in packets (or frames).| Counter| int64| {packets}  
[Network RX VLAN Packets](../../../../apidocs/introduction/hw-network/#metric-network-rx-vlan-packets)| [hw.network.packets_receive_vlan](../../../../apidocs/introduction/hw-network/#metric-network-rx-vlan-packets)| Received network traffic in packets (or frames) with VLAN tag.| Counter| int64| {packets}  
[Network TX Packets](../../../../apidocs/introduction/hw-network/#metric-network-tx-packets)| [hw.network.packets_transmit](../../../../apidocs/introduction/hw-network/#metric-network-tx-packets)| Transmitted network traffic in packets (or frames).| Counter| int64| {packets}  
[TX Packets Size 1024 to 1518](../../../../apidocs/introduction/hw-network/#metric-tx-packets-size-1024-to-1518)| [hw.network.packets_transmit_1024_to_1518](../../../../apidocs/introduction/hw-network/#metric-tx-packets-size-1024-to-1518)| Transmitted network traffic in packets (or frames) with size between 1024 and 1518.| Counter| int64| {packets}  
[TX Packets Size 128 to 255](../../../../apidocs/introduction/hw-network/#metric-tx-packets-size-128-to-255)| [hw.network.packets_transmit_128_to_255](../../../../apidocs/introduction/hw-network/#metric-tx-packets-size-128-to-255)| Transmitted network traffic in packets (or frames) with size between 128 and 255.| Counter| int64| {packets}  
[TX Packets Size 1519 to 2047](../../../../apidocs/introduction/hw-network/#metric-tx-packets-size-1519-to-2047)| [hw.network.packets_transmit_1519_to_2047](../../../../apidocs/introduction/hw-network/#metric-tx-packets-size-1519-to-2047)| Transmitted network traffic in packets (or frames) with size between 1519 and 2047.| Counter| int64| {packets}  
[TX Packets Size Less Than 64](../../../../apidocs/introduction/hw-network/#metric-tx-packets-size-less-than-64)| [hw.network.packets_transmit_1_to_63](../../../../apidocs/introduction/hw-network/#metric-tx-packets-size-less-than-64)| Transmitted network traffic in packets (or frames) with size less than 64.| Counter| int64| {packets}  
[TX Packets Size 2048 to 4095](../../../../apidocs/introduction/hw-network/#metric-tx-packets-size-2048-to-4095)| [hw.network.packets_transmit_2048_to_4095](../../../../apidocs/introduction/hw-network/#metric-tx-packets-size-2048-to-4095)| Transmitted network traffic in packets (or frames) with size between 2048 and 4095.| Counter| int64| {packets}  
[TX Packets Size 256 to 511](../../../../apidocs/introduction/hw-network/#metric-tx-packets-size-256-to-511)| [hw.network.packets_transmit_256_to_511](../../../../apidocs/introduction/hw-network/#metric-tx-packets-size-256-to-511)| Transmitted network traffic in packets (or frames) with size between 256 and 511.| Counter| int64| {packets}  
[TX Packets Size 4096 to 8191](../../../../apidocs/introduction/hw-network/#metric-tx-packets-size-4096-to-8191)| [hw.network.packets_transmit_4096_to_8191](../../../../apidocs/introduction/hw-network/#metric-tx-packets-size-4096-to-8191)| Transmitted network traffic in packets (or frames) with size between 4096 and 8191.| Counter| int64| {packets}  
[TX Packets Size 512 to 1023](../../../../apidocs/introduction/hw-network/#metric-tx-packets-size-512-to-1023)| [hw.network.packets_transmit_512_to_1023](../../../../apidocs/introduction/hw-network/#metric-tx-packets-size-512-to-1023)| Transmitted network traffic in packets (or frames) with size between 512 and 1023.| Counter| int64| {packets}  
[TX Packets Size 64](../../../../apidocs/introduction/hw-network/#metric-tx-packets-size-64)| [hw.network.packets_transmit_64](../../../../apidocs/introduction/hw-network/#metric-tx-packets-size-64)| Transmitted network traffic in packets (or frames) with size of 64.| Counter| int64| {packets}  
[TX Packets Size 65 to 127](../../../../apidocs/introduction/hw-network/#metric-tx-packets-size-65-to-127)| [hw.network.packets_transmit_65_to_127](../../../../apidocs/introduction/hw-network/#metric-tx-packets-size-65-to-127)| Transmitted network traffic in packets (or frames) with size between 65 and 127.| Counter| int64| {packets}  
[TX Packets Size 8192 to 9215](../../../../apidocs/introduction/hw-network/#metric-tx-packets-size-8192-to-9215)| [hw.network.packets_transmit_8192_to_9215](../../../../apidocs/introduction/hw-network/#metric-tx-packets-size-8192-to-9215)| Transmitted network traffic in packets (or frames) with size between 8192 and 9215.| Counter| int64| {packets}  
[TX Packets Size 9216 or Above](../../../../apidocs/introduction/hw-network/#metric-tx-packets-size-9216-or-above)| [hw.network.packets_transmit_9216_to_max](../../../../apidocs/introduction/hw-network/#metric-tx-packets-size-9216-or-above)| Transmitted network traffic in packets (or frames) with size of 9216 or above.| Counter| int64| {packets}  
[Network TX Broadcast Packets](../../../../apidocs/introduction/hw-network/#metric-network-tx-broadcast-packets)| [hw.network.packets_transmit_broadcast](../../../../apidocs/introduction/hw-network/#metric-network-tx-broadcast-packets)| Transmitted broadcast network traffic in packets (or frames).| Counter| int64| {packets}  
[Network TX Multicast Packets](../../../../apidocs/introduction/hw-network/#metric-network-tx-multicast-packets)| [hw.network.packets_transmit_multicast](../../../../apidocs/introduction/hw-network/#metric-network-tx-multicast-packets)| Transmitted multicast network traffic in packets (or frames).| Counter| int64| {packets}  
[Network TX Priority Pause Frames](../../../../apidocs/introduction/hw-network/#metric-network-tx-priority-pause-frames)| [hw.network.packets_transmit_ppp](../../../../apidocs/introduction/hw-network/#metric-network-tx-priority-pause-frames)| Transmitted priority pause frames on the network interface.| Counter| int64| {packets}  
[Network TX TSO Packets](../../../../apidocs/introduction/hw-network/#metric-network-tx-tso-packets)| [hw.network.packets_transmit_tso](../../../../apidocs/introduction/hw-network/#metric-network-tx-tso-packets)| Transmitted network traffic in packets (or frames) that were processed using TSO.| Counter| int64| {packets}  
[Network TX Unicast Packets](../../../../apidocs/introduction/hw-network/#metric-network-tx-unicast-packets)| [hw.network.packets_transmit_unicast](../../../../apidocs/introduction/hw-network/#metric-network-tx-unicast-packets)| Transmitted unicast network traffic in packets (or frames).| Counter| int64| {packets}  
[Network TX VLAN Packets](../../../../apidocs/introduction/hw-network/#metric-network-tx-vlan-packets)| [hw.network.packets_transmit_vlan](../../../../apidocs/introduction/hw-network/#metric-network-tx-vlan-packets)| Transmitted network traffic in packets (or frames) with VLAN tag.| Counter| int64| {packets}  
[Network RX PFC Wait Time Priority 0](../../../../apidocs/introduction/hw-network/#metric-network-rx-pfc-wait-time-priority-0)| [hw.network.pfc_waittime_receive_priority0](../../../../apidocs/introduction/hw-network/#metric-network-rx-pfc-wait-time-priority-0)| Receive PFC wait time of port for packets with priority 0 in microseconds.| Counter| float64| s  
[Network RX PFC Wait Time Priority 1](../../../../apidocs/introduction/hw-network/#metric-network-rx-pfc-wait-time-priority-1)| [hw.network.pfc_waittime_receive_priority1](../../../../apidocs/introduction/hw-network/#metric-network-rx-pfc-wait-time-priority-1)| Receive PFC wait time of port for packets with priority 1 in microseconds.| Counter| float64| s  
[Network RX PFC Wait Time Priority 2](../../../../apidocs/introduction/hw-network/#metric-network-rx-pfc-wait-time-priority-2)| [hw.network.pfc_waittime_receive_priority2](../../../../apidocs/introduction/hw-network/#metric-network-rx-pfc-wait-time-priority-2)| Receive PFC wait time of port for packets with priority 2 in microseconds.| Counter| float64| s  
[Network RX PFC Wait Time Priority 3](../../../../apidocs/introduction/hw-network/#metric-network-rx-pfc-wait-time-priority-3)| [hw.network.pfc_waittime_receive_priority3](../../../../apidocs/introduction/hw-network/#metric-network-rx-pfc-wait-time-priority-3)| Receive PFC wait time of port for packets with priority 3 in microseconds.| Counter| float64| s  
[Network RX PFC Wait Time Priority 4](../../../../apidocs/introduction/hw-network/#metric-network-rx-pfc-wait-time-priority-4)| [hw.network.pfc_waittime_receive_priority4](../../../../apidocs/introduction/hw-network/#metric-network-rx-pfc-wait-time-priority-4)| Receive PFC wait time of port for packets with priority 4 in microseconds.| Counter| float64| s  
[Network RX PFC Wait Time Priority 5](../../../../apidocs/introduction/hw-network/#metric-network-rx-pfc-wait-time-priority-5)| [hw.network.pfc_waittime_receive_priority5](../../../../apidocs/introduction/hw-network/#metric-network-rx-pfc-wait-time-priority-5)| Receive PFC wait time of port for packets with priority 5 in microseconds.| Counter| float64| s  
[Network RX PFC Wait Time Priority 6](../../../../apidocs/introduction/hw-network/#metric-network-rx-pfc-wait-time-priority-6)| [hw.network.pfc_waittime_receive_priority6](../../../../apidocs/introduction/hw-network/#metric-network-rx-pfc-wait-time-priority-6)| Receive PFC wait time of port for packets with priority 6 in microseconds.| Counter| float64| s  
[Network RX PFC Wait Time Priority 7](../../../../apidocs/introduction/hw-network/#metric-network-rx-pfc-wait-time-priority-7)| [hw.network.pfc_waittime_receive_priority7](../../../../apidocs/introduction/hw-network/#metric-network-rx-pfc-wait-time-priority-7)| Receive PFC wait time of port for packets with priority 7 in microseconds.| Counter| float64| s  
[Network TX PFC Wait Time Priority 0](../../../../apidocs/introduction/hw-network/#metric-network-tx-pfc-wait-time-priority-0)| [hw.network.pfc_waittime_transmit_priority0](../../../../apidocs/introduction/hw-network/#metric-network-tx-pfc-wait-time-priority-0)| Transmit PFC wait time of port for packets with priority 0 in microseconds.| Counter| float64| s  
[Network TX PFC Wait Time Priority 1](../../../../apidocs/introduction/hw-network/#metric-network-tx-pfc-wait-time-priority-1)| [hw.network.pfc_waittime_transmit_priority1](../../../../apidocs/introduction/hw-network/#metric-network-tx-pfc-wait-time-priority-1)| Transmit PFC wait time of port for packets with priority 1 in microseconds.| Counter| float64| s  
[Network TX PFC Wait Time Priority 2](../../../../apidocs/introduction/hw-network/#metric-network-tx-pfc-wait-time-priority-2)| [hw.network.pfc_waittime_transmit_priority2](../../../../apidocs/introduction/hw-network/#metric-network-tx-pfc-wait-time-priority-2)| Transmit PFC wait time of port for packets with priority 2 in microseconds.| Counter| float64| s  
[Network TX PFC Wait Time Priority 3](../../../../apidocs/introduction/hw-network/#metric-network-tx-pfc-wait-time-priority-3)| [hw.network.pfc_waittime_transmit_priority3](../../../../apidocs/introduction/hw-network/#metric-network-tx-pfc-wait-time-priority-3)| Transmit PFC wait time of port for packets with priority 3 in microseconds.| Counter| float64| s  
[Network TX PFC Wait Time Priority 4](../../../../apidocs/introduction/hw-network/#metric-network-tx-pfc-wait-time-priority-4)| [hw.network.pfc_waittime_transmit_priority4](../../../../apidocs/introduction/hw-network/#metric-network-tx-pfc-wait-time-priority-4)| Transmit PFC wait time of port for packets with priority 4 in microseconds.| Counter| float64| s  
[Network TX PFC Wait Time Priority 5](../../../../apidocs/introduction/hw-network/#metric-network-tx-pfc-wait-time-priority-5)| [hw.network.pfc_waittime_transmit_priority5](../../../../apidocs/introduction/hw-network/#metric-network-tx-pfc-wait-time-priority-5)| Transmit PFC wait time of port for packets with priority 5 in microseconds.| Counter| float64| s  
[Network TX PFC Wait Time Priority 6](../../../../apidocs/introduction/hw-network/#metric-network-tx-pfc-wait-time-priority-6)| [hw.network.pfc_waittime_transmit_priority6](../../../../apidocs/introduction/hw-network/#metric-network-tx-pfc-wait-time-priority-6)| Transmit PFC wait time of port for packets with priority 6 in microseconds.| Counter| float64| s  
[Network TX PFC Wait Time Priority 7](../../../../apidocs/introduction/hw-network/#metric-network-tx-pfc-wait-time-priority-7)| [hw.network.pfc_waittime_transmit_priority7](../../../../apidocs/introduction/hw-network/#metric-network-tx-pfc-wait-time-priority-7)| Transmit PFC wait time of port for packets with priority 7 in microseconds.| Counter| float64| s  
[Link Status](../../../../apidocs/introduction/hw-network/#metric-link-status)| [hw.network.up](../../../../apidocs/introduction/hw-network/#metric-link-status)| Link status: 1 (up) or 0 (down).| UpDownCounter| int64| 1  
  
## Power Supply

**Name:**[hw.power_supply](../../../../apidocs/introduction/hw-power_supply)

A PSU on a Server, Chassis or Fabric Interconnect.Label| Name| Description| Instrument Type  
| Value Type| Units  
---|---|---|---|---|---  
[Energy](../../../../apidocs/introduction/hw-power_supply/#metric-energy)| [hw.energy](../../../../apidocs/introduction/hw-power_supply/#metric-energy)| Energy consumed by a hardware component, in joules.| Counter| float64| J  
[Output Energy](../../../../apidocs/introduction/hw-power_supply/#metric-output-energy)| [hw.energy_out](../../../../apidocs/introduction/hw-power_supply/#metric-output-energy)| Output energy delivered by the power supply, in Joules.| Counter| float64| J  
[Power](../../../../apidocs/introduction/hw-power_supply/#metric-power)| [hw.power](../../../../apidocs/introduction/hw-power_supply/#metric-power)| Instantaneous power consumed by a hardware component, in Watts.| Gauge| float64| W  
[Output Power](../../../../apidocs/introduction/hw-power_supply/#metric-output-power)| [hw.power_out](../../../../apidocs/introduction/hw-power_supply/#metric-output-power)| Output power delivered by the power supply, in Watts.| Gauge| float64| W  
[Upper Critical Power Limit](../../../../apidocs/introduction/hw-power_supply/#metric-upper-critical-power-limit)| [hw.power_supply.limit_high_critical](../../../../apidocs/introduction/hw-power_supply/#metric-upper-critical-power-limit)| The upper critical power limit.| UpDownCounter| int64| W  
[Max Power Limit](../../../../apidocs/introduction/hw-power_supply/#metric-max-power-limit)| [hw.power_supply.limit_max](../../../../apidocs/introduction/hw-power_supply/#metric-max-power-limit)| The maximum output power of the power supply.| UpDownCounter| int64| W  
[Throttled Power Limit](../../../../apidocs/introduction/hw-power_supply/#metric-throttled-power-limit)| [hw.power_supply.limit_throttled](../../../../apidocs/introduction/hw-power_supply/#metric-throttled-power-limit)| The throttled output power of the power supply.| UpDownCounter| int64| W  
[Power Supply Utilization](../../../../apidocs/introduction/hw-power_supply/#metric-power-supply-utilization)| [hw.power_supply.utilization](../../../../apidocs/introduction/hw-power_supply/#metric-power-supply-utilization)| Utilization of the power supply as a percentage of its maximum output.| Gauge| float64| %  
[Hardware Status](../../../../apidocs/introduction/hw-power_supply/#metric-hardware-status)| [hw.status](../../../../apidocs/introduction/hw-power_supply/#metric-hardware-status)| The operational status: 1 (true) or 0 (false) for each of the possible states. At query time, you can use the following aggregation functions: 1. Use longMax aggregation to determine if the component was up at least once during each rollup interval. 2. Use longMin aggregation to determine if the component was down at least once during each rollup interval. 3. Use ( longSum / count ) to determine the percentage of time when the component was up during each rollup interval.| UpDownCounter| int64| 1  
  
## Signal Power

**Name:**[hw.signal_power](../../../../apidocs/introduction/hw-signal_power)

A signal power sensor, either numeric or discrete.Label| Name| Description| Instrument Type  
| Value Type| Units  
---|---|---|---|---|---  
[Rx Power](../../../../apidocs/introduction/hw-signal_power/#metric-rx-power)| [hw.signal_power_receive](../../../../apidocs/introduction/hw-signal_power/#metric-rx-power)| Power in decibels per milliwatt (dBm) at which a sensor receives its signal. Transceiver receive power metric requires an advantage license and is available only if a transceiver is present and DOM (Digital optical monitoring) is enabled.| Gauge| float64| B[W]  
[Tx Power](../../../../apidocs/introduction/hw-signal_power/#metric-tx-power)| [hw.signal_power_transmit](../../../../apidocs/introduction/hw-signal_power/#metric-tx-power)| Power in decibels per milliwatt (dBm) at which a sensor transmits its signal. Transceiver transmit power metric requires an advantage license and is available only if a transceiver is present and DOM (Digital optical monitoring) is enabled.| Gauge| float64| B[W]  
  
## Temperature

**Name:**[hw.temperature](../../../../apidocs/introduction/hw-temperature)

A temperature sensor, either numeric or discrete.Label| Name| Description| Instrument Type  
| Value Type| Units  
---|---|---|---|---|---  
[Hardware Status](../../../../apidocs/introduction/hw-temperature/#metric-hardware-status)| [hw.status](../../../../apidocs/introduction/hw-temperature/#metric-hardware-status)| The operational status: 1 (true) or 0 (false) for each of the possible states. At query time, you can use the following aggregation functions: 1. Use longMax aggregation to determine if the component was up at least once during each rollup interval. 2. Use longMin aggregation to determine if the component was down at least once during each rollup interval. 3. Use ( longSum / count ) to determine the percentage of time when the component was up during each rollup interval.| UpDownCounter| int64| 1  
[Temperature](../../../../apidocs/introduction/hw-temperature/#metric-temperature)| [hw.temperature](../../../../apidocs/introduction/hw-temperature/#metric-temperature)| Temperature in degrees Celsius. Server CPU temperature metrics are available only when the host is in a powered-on state. In case of a transceiver, it is the operating temperature. Transceiver temperature metric requires an advantage license and is available only if a transceiver is present and DOM (Digital optical monitoring) is enabled.| Gauge| float64| Cel  
[Upper Critical Temperature Limit](../../../../apidocs/introduction/hw-temperature/#metric-upper-critical-temperature-limit)| [hw.temperature.limit_high_critical](../../../../apidocs/introduction/hw-temperature/#metric-upper-critical-temperature-limit)| The upper critical temperature limit.| Gauge| float64| Cel  
[Upper Non Critical Temperature Limit](../../../../apidocs/introduction/hw-temperature/#metric-upper-non-critical-temperature-limit)| [hw.temperature.limit_high_degraded](../../../../apidocs/introduction/hw-temperature/#metric-upper-non-critical-temperature-limit)| The upper non critical temperature limit.| Gauge| float64| Cel  
[Lower Critical Temperature Limit](../../../../apidocs/introduction/hw-temperature/#metric-lower-critical-temperature-limit)| [hw.temperature.limit_low_critical](../../../../apidocs/introduction/hw-temperature/#metric-lower-critical-temperature-limit)| The lower critical temperature limit.| Gauge| float64| Cel  
  
## Voltage

**Name:**[hw.voltage](../../../../apidocs/introduction/hw-voltage)

A voltage sensor, either numeric or discrete.Label| Name| Description| Instrument Type  
| Value Type| Units  
---|---|---|---|---|---  
[Voltage](../../../../apidocs/introduction/hw-voltage/#metric-voltage)| [hw.voltage](../../../../apidocs/introduction/hw-voltage/#metric-voltage)| Voltage measured by the sensor in Volts. Transceiver voltage metric requires an advantage license and is available only if a transceiver is present and DOM (Digital optical monitoring) is enabled. In storage systems, this metric displays the current electrical voltage level of the chassis or its components, helping monitor hardware health and power conditions.| Gauge| float64| V  
  
## System CPU

**Name:**[system.cpu](../../../../apidocs/introduction/system-cpu)

System-level processor metrics. The value of the 'host.id' attribute identifies the host resource.Label| Name| Description| Instrument Type  
| Value Type| Units  
---|---|---|---|---|---  
[Idle CPU Utilization](../../../../apidocs/introduction/system-cpu/#metric-idle-cpu-utilization)| [system.cpu.utilization_idle](../../../../apidocs/introduction/system-cpu/#metric-idle-cpu-utilization)| The percentage of CPU capacity unused during periods of inactivity.| Gauge| float64| %  
[System CPU Utilization](../../../../apidocs/introduction/system-cpu/#metric-system-cpu-utilization)| [system.cpu.utilization_system](../../../../apidocs/introduction/system-cpu/#metric-system-cpu-utilization)| The percentage of CPU time consumed by the operating system's kernel processes.| Gauge| float64| %  
[User CPU Utilization](../../../../apidocs/introduction/system-cpu/#metric-user-cpu-utilization)| [system.cpu.utilization_user](../../../../apidocs/introduction/system-cpu/#metric-user-cpu-utilization)| The percentage of CPU time utilized by user-launched applications and processes.| Gauge| float64| %  
  
## System Memory

**Name:**[system.memory](../../../../apidocs/introduction/system-memory)

System-level memory metrics.Label| Name| Description| Instrument Type  
| Value Type| Units  
---|---|---|---|---|---  
[Cached System Memory](../../../../apidocs/introduction/system-memory/#metric-cached-system-memory)| [system.memory.usage_cached](../../../../apidocs/introduction/system-memory/#metric-cached-system-memory)| The cached memory of the system, in bytes.| UpDownCounter| int64| By  
[Free System Memory](../../../../apidocs/introduction/system-memory/#metric-free-system-memory)| [system.memory.usage_free](../../../../apidocs/introduction/system-memory/#metric-free-system-memory)| The free memory of the system, in bytes.| UpDownCounter| int64| By  
[Used System Memory](../../../../apidocs/introduction/system-memory/#metric-used-system-memory)| [system.memory.usage_used](../../../../apidocs/introduction/system-memory/#metric-used-system-memory)| The memory usage of the system, in bytes.| UpDownCounter| int64| By  
[Memory Utilization](../../../../apidocs/introduction/system-memory/#metric-memory-utilization)| [system.memory.utilization](../../../../apidocs/introduction/system-memory/#metric-memory-utilization)| The memory utilization of the system, as a percentage.| Gauge| float64| %