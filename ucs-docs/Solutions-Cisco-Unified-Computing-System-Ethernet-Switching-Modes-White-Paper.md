# Cisco Unified Computing System Ethernet Switching Modes White Paper

| | |
|---|---|
| **URL Title** | Cisco Unified Computing System Ethernet Switching Modes White Paper |
| **URL** | https://www.cisco.com/c/en/us/solutions/collateral/data-center-virtualization/unified-computing/whitepaper_c11-701962.html |
| **Long URL** |  |
| **HTML Title** | Solutions - Cisco Unified Computing System Ethernet Switching Modes White Paper |
| **Source file** | `ucs-docs-raw/html/whitepaper_c11-701962.html` |
| **File type** | HTML |
| **Fetched on** | 2026-07-02 13:04:45 |

---

## Page 1: https://www.cisco.com/c/en/us/solutions/collateral/data-center-virtualization/unified-computing/whitepaper_c11-701962.html

` `

What you will learn

In Cisco Unified Computing System™ (Cisco UCS®) environments, the Ethernet switching mode determines how a fabric interconnect behaves as a switching device between the servers and the network. The fabric interconnect operates in either of the following Ethernet switching modes, end-host more or switch mode, discussed below. 

End-host mode

End-host mode allows the fabric interconnect to act as an end host to the network, representing all servers (hosts) connected to it through vNICs. This is achieved by pinning (either dynamically pinning or hard pinning) vNICs to uplink ports, which provides redundancy in the network and makes the uplink ports appear as server ports to the rest of the fabric. When in end- by disallowing uplink ports from forwarding traffic to each other and by ensuring that server egress traffic is sent out through only one uplink port at a time. End-host mode is the default Ethernet switching mode and should be used if either of the following is used upstream: 

● Layer-2 switching for L2 aggregation 

● Virtual Switching System (VSS) aggregation layer 

**Note:** When end-host mode is enabled, if a vNIC is hard pinned to an uplink port and this uplink port goes down, the system cannot re-pin the vNIC, and the vNIC remains down. 

Switch mode

Switch mode is the traditional Ethernet switching mode. The fabric interconnect runs STP to avoid loops, and broadcast and multicast packets are handled in the traditional way. Switch mode is not the default Ethernet switching mode, and should be used only if the fabric interconnect is directly connected to a router or if either of the following is used upstream: 

● Layer-3 aggregation 

● VLAN in a box 

**Note:** For both Ethernet switching modes, even when vNICs are hard pinned to uplink ports, all server-to-server unicast traffic in the server array is sent only through the fabric interconnect and is never sent through uplink ports. Server-to-server multicast and broadcast traffic is sent through all uplink ports in the same VLAN. 

This document describes these two switching modes and discusses how and when to implement each mode. 

This document will describe how to configure each Ethernet switching mode using the Cisco Intersight® management platform. 

The example configurations of the fabric interconnects will be done using Intersight. 

This document does not discuss the operating mode available on the Fibre Channel ports.

Cisco UCS architectural overview

A fully redundant Cisco Unified Computing System (Cisco UCS) consists of two independent fabric planes: fabric A and fabric B. Each plane consists of a central fabric interconnect connected to an Intelligent Fabric Module (IFM) of the Cisco UCS X-Series chassis. 

Cisco® rack servers can be directly connected to the fabric interconnects with or without the need for a Cisco Nexus® FEX 93180 YC-FX3. 

The two fabric interconnects are completely independent from the perspective of the data plane; Cisco UCS can function with a single fabric interconnect if the other fabric is offline or not provisioned (Figure 1).

![A diagram of a machineAI-generated content may be incorrect.](/c/dam/en/us/solutions/collateral/data-center-virtualization/unified-computing/whitepaper_c11-701962.doc/_jcr_content/renditions/whitepaper_c11-701962_0.png)

Figure 1. 

Cisco UCS components (logical) 

All network endpoints, such as Host Bus Adapters (HBAs), and management entities such as Cisco Integrated Management Controllers (IMCs; formerly referred to as baseboard management controllers, or BMCs), are dual-connected to both fabric planes and thus can work in an active/active configuration. 

Virtual Port Channels (vPCs) are not supported on the fabric interconnects, although the upstream LAN switches to which they connect can be vPC or Virtual Switching System (VSS) peers.

Cisco UCS fabric interconnect switching modes

As shown in Figure 1, Cisco UCS supports connectivity to Ethernet LANs and Fibre Channel SANs to enable network and storage I/O from servers. The external interface-operating modes to the LAN and the SAN balance the goals of administrative simplicity and utility in common deployment scenarios. The two operating modes supported on the fabric interconnect for Ethernet are the following: 

● Ethernet end-host mode, sometimes referred to as Ethernet host virtualizer 

● Traditional Ethernet switch mode 

For Ethernet, end-host mode is the default mode of operation. To change the Switching Mode in Intersight, a **switch control policy** in the **UCS Domain Profile** should be created. A change in the operating mode requires a fabric interconnect reboot to effect the change (Figure 2).

![A screenshot of a computerAI-generated content may be incorrect.](/c/dam/en/us/solutions/collateral/data-center-virtualization/unified-computing/whitepaper_c11-701962.doc/_jcr_content/renditions/whitepaper_c11-701962_1.png)

Figure 2. 

Setting the Switching Mode 

Ethernet ports on the fabric interconnects are unconfigured by default. The ports can be configured to be any of the following: 

● Ethernet uplink ports 

● FCoE uplink ports 

● Server ports 

● Appliance ports 

A port must be explicitly defined as a specific type, and this type defines the port behavior. For example, the discovery of components such as fabric extenders or blades is performed only on server ports. Similarly, uplink ports are automatically configured as IEEE 802.1Q trunks for all VLANs defined on the fabric interconnect. 

**Note:** In either Ethernet switching mode, a fabric interconnect does not require an upstream switch for Layer-2 traffic between two servers connected to it on the same fabric.

An external switch is required for switching Layer-2 traffic between servers if virtual Network Interface Cards (vNICs) belonging to the same VLAN are mapped to different fabric interconnects (Figure 3).

![A computer screen shot of a computer networkAI-generated content may be incorrect.](/c/dam/en/us/solutions/collateral/data-center-virtualization/unified-computing/whitepaper_c11-701962.doc/_jcr_content/renditions/whitepaper_c11-701962_2.png)

Figure 3. 

External switch required for switching Layer-2 traffic between vNICs on different fabric interconnects 

Fabric failover for Ethernet: high-availability vNIC

To understand the switching mode behavior, you need to understand the fabric-based failover feature for Ethernet in Cisco UCS. 

Each adapter in Cisco UCS is a dual-port adapter that connects to both fabrics (A and B). The two fabrics in Cisco UCS provide failover protection in the event of planned or unplanned component downtime in one of the fabrics. Typically, host software, such as NIC teaming for Ethernet, provides failover across the two fabrics (Figure 4). 

A vNIC in Cisco UCS is a host-presented PCI device that is centrally managed by Cisco Intersight. The fabric-based failover feature, which you enable by selecting the high-availability vNIC option in the service profile definition, allows Network Interface Virtualization (NIV) and the fabric interconnects to provide active/standby failover for Ethernet vNICs without any NIC-teaming software on the host.

![A diagram of a connectionAI-generated content may be incorrect.](/c/dam/en/us/solutions/collateral/data-center-virtualization/unified-computing/whitepaper_c11-701962.doc/_jcr_content/renditions/whitepaper_c11-701962_3.png)

Figure 4. 

Cisco UCS fabric-based failover 

For unicast traffic failover, the fabric interconnect in the new path sends gratuitous Address Resolution Protocols (gARPs). This process refreshes the forwarding tables on the upstream switches. 

For multicast traffic, the new active fabric interconnect sends an Internet Group Management Protocol (IGMP) global leave message to the upstream multicast router. The upstream multicast router responds by sending an IGMP query that is flooded to all vNICs. The host OS responds to these IGMP queries by rejoining all relevant multicast groups. This process forces the hosts to refresh the multicast state in the network in a timely manner. 

Cisco UCS fabric failover is an important feature because it reduces the complexity of defining NIC teaming software for failover on the host. It does this transparently in the fabric, based on the network property that is defined in the service profile.

Ethernet end-host mode

In end-host mode, Cisco UCS presents an end host to an external Ethernet network. The external LAN sees the Cisco UCS fabric interconnect as an end host with multiple adapters (Figure 5).

![A computer server with several white boxesAI-generated content may be incorrect.](/c/dam/en/us/solutions/collateral/data-center-virtualization/unified-computing/whitepaper_c11-701962.doc/_jcr_content/renditions/whitepaper_c11-701962_4.png)

Figure 5. 

Active/active links in end-host mode 

Characteristics and features of end-host mode include the following: 

● Spanning Tree Protocol is not run on both the uplink ports and the server ports 

● MAC address learning occurs only on the server ports; MAC address movement is fully supported 

● Links are active/active regardless of the number of uplink switches 

● The system is highly scalable because the control plane is not occupied 

Server links (vNICs on the blades) are associated with a single uplink port, which may also be a port channel. This association process is called pinning, and the selected external interface is called a pinned uplink port. The pinning process can be statically configured when the vNIC is defined or dynamically configured by the system. In end-host mode, pinning is required for traffic flow to a server.

Figure 6 shows an example of dynamic pinning.

![A computer server with many portsAI-generated content may be incorrect.](/c/dam/en/us/solutions/collateral/data-center-virtualization/unified-computing/whitepaper_c11-701962.doc/_jcr_content/renditions/whitepaper_c11-701962_5.png)

Figure 6. 

Dynamic pinning 

Dynamic pinning is the default pin-group setting in Cisco UCS. With dynamic pinning, the fabric interconnect automatically assigns server vNICs to its active uplink ports based on the current configuration. The mapping adjusts as uplink availability changes, ensuring optimal connectivity. Using dynamic pinning is considered best practice.

Static pinning is performed by defining a pin group and associating the pin group with a vNIC (see Figures 7 and 8).

![A screenshot of a computer programAI-generated content may be incorrect.](/c/dam/en/us/solutions/collateral/data-center-virtualization/unified-computing/whitepaper_c11-701962.doc/_jcr_content/renditions/whitepaper_c11-701962_6.png)

Figure 7. 

Creating a LAN pin group for static pinning

![A screenshot of a computerAI-generated content may be incorrect.](/c/dam/en/us/solutions/collateral/data-center-virtualization/unified-computing/whitepaper_c11-701962.doc/_jcr_content/renditions/whitepaper_c11-701962_7.png)

Figure 8. 

Static pinning: associating a pin group with a vNIC

Static pinning should be used in scenarios in which a deterministic path is required. When the target (as shown in Figure 7) on fabric interconnect A goes down, the corresponding failover mechanism of the vNIC goes into effect, and traffic is redirected to the target port on fabric interconnect B.

![Related image, diagram or screenshot](/c/dam/en/us/solutions/collateral/data-center-virtualization/unified-computing/whitepaper_c11-701962.doc/_jcr_content/renditions/whitepaper_c11-701962_8.png)

Figure 9. 

Pin groups 

If the pinning is not static, then the vNIC is pinned to an operational uplink port on the same fabric interconnect, and the vNIC failover mechanisms are not invoked until all uplink ports on that fabric interconnect fail. In the absence of Spanning Tree Protocol, the fabric interconnect uses various mechanisms for loop prevention while preserving an active/active topology. 

Unicast traffic summary

Unicast traffic paths in Cisco UCS are shown in Figure 10. Characteristics of unicast traffic in Cisco UCS include the following: 

● Each server link is pinned to exactly one uplink port (or port channel) 

● Server-to-server Layer-2 traffic is locally switched 

● Server-to-network traffic goes out on its pinned uplink port 

● Network-to-server unicast traffic is forwarded to the server only if it arrives on a pinned uplink port. This feature is called the Reverse Path Forwarding (RPF) check 

● Server traffic received on any uplink port, except its pinned uplink port, is dropped. (This is called the deja-vu check.) 

● The server MAC address must be learned before traffic can be forwarded to it

![A blue and pink lines and arrowsAI-generated content may be incorrect.](/c/dam/en/us/solutions/collateral/data-center-virtualization/unified-computing/whitepaper_c11-701962.doc/_jcr_content/renditions/whitepaper_c11-701962_9.png)

Figure 10. 

Unicast traffic paths 

Multicast and broadcast forwarding summary

Multicast traffic paths in Cisco UCS are shown in Figure 11. Characteristics of multicast traffic in Cisco UCS include the following: 

● Broadcast traffic is pinned on exactly one uplink port in Cisco UCS Manager Release 1.4 and earlier and is dropped when received on the other uplink ports. In Cisco UCS Manager Release 2.0 and higher, the incoming broadcast traffic is pinned on a per-VLAN basis, depending on uplink port VLAN membership 

● IGMP multicast groups are pinned based on IGMP snooping. Each group is pinned to exactly one uplink port 

● Server-to-server multicast traffic is locally switched 

● RPF and deja-vu checks also apply to multicast traffic

![A diagram of a triangle with arrows and circlesAI-generated content may be incorrect.](/c/dam/en/us/solutions/collateral/data-center-virtualization/unified-computing/whitepaper_c11-701962.doc/_jcr_content/renditions/whitepaper_c11-701962_10.png)

Figure 11. 

Multicast and broadcast traffic summary

Ethernet switching mode

In Ethernet switching mode (see Figure 12), the Cisco fabric interconnects act like traditional Ethernet switches with support for Spanning Tree Protocol on the uplink ports.

![A computer server with many white boxesAI-generated content may be incorrect.](/c/dam/en/us/solutions/collateral/data-center-virtualization/unified-computing/whitepaper_c11-701962.doc/_jcr_content/renditions/whitepaper_c11-701962_11.png)

Figure 12. 

Forwarding paths in switch mode without VSS or vPC upstream 

Characteristics and features of Ethernet switching mode include the following: 

● Spanning Tree Protocol is run on the uplink ports per VLAN as defined by Cisco Per-VLAN Spanning Tree Plus (PVST+) 

● Configuration of Spanning Tree Protocol parameters (bridge priority, hello timers, etc.) is not supported 

● VLAN Trunk Protocol (VTP) is not supported 

● MAC address learning and aging occur on both the server and uplink ports as in a typical Layer-2 switch 

● Upstream links are blocked according to Spanning Tree Protocol rules

Design considerations for running switch or end-host mode

In most cases, end-host mode is preferable because it offers scalability and simplicity for server administrators when connecting to an upstream network. However, there are other factors to consider when selecting the appropriate switching mode, including: 

● Scalability 

● Efficient use of bandwidth 

● Fabric failover 

● Active/active link utilization 

● Disjoint Layer-2 domain or a loop-free topology 

● Optimal network behavior for the existing network topology 

● Application-specific requirements 

Scalability

Without Spanning Tree Protocol running, end-host mode provides the most scalability because the control plane is not occupied. Additionally, because there is no MAC address learning on the uplink ports, the MAC address table can support as many virtual machines as the number of entries available in the MAC address forwarding table. 

For scalability, the recommended Ethernet switching mode is end-host mode. 

The configuration limits of the fabric interconnect can be found here. 

Efficient bandwidth use

Using static pin groups in end-host mode, an administrator can explicitly define the upstream port for a particular vNIC. This approach provides control over bandwidth and deterministic behavior for a vNIC. 

For efficient bandwidth use, the recommended Ethernet switching mode is end-host mode. 

Fabric failover

Cisco UCS fabric failover, depending on the status of the uplink ports, is available only in end-host mode. In switch mode, OS-based teaming (active/passive) software is required to provide failover. The pinning feature provides the association between the uplink port and the vNIC that is used for tracking and for providing failovers. 

For fabric failover, the recommended Ethernet switching mode is end-host mode. 

Active/active link utilization

Without the use of technologies such as vPC or VSS upstream, switch mode blocks ports that depend on spanning root selection. By using pin groups in end-host mode, effective upstream bandwidth utilization is possible. 

**Note:** Pinning is applicable only in end-host mode.

For active/active links without vPC or VSS upstream, the recommended switching mode is end-host mode. When vPC or VSS is available upstream (see Figure 13), either end-host mode or switch mode can be used.

![A computer server with many white boxesAI-generated content may be incorrect.](/c/dam/en/us/solutions/collateral/data-center-virtualization/unified-computing/whitepaper_c11-701962.doc/_jcr_content/renditions/whitepaper_c11-701962_12.png)

Figure 13. 

Forwarding paths with VSS or vPC upstream 

Optimal network behavior for the network topology

In some commonly deployed LAN topologies, switch mode provides the best network behavior. A typical example is a switch directly connected to a pair of Hot Standby Router Protocol (HSRP) routers that are the Spanning Tree Protocol roots on different VLANs. Switch mode provides the optimal path because of the use of Spanning Tree Protocol. For example, a vNIC belonging to an odd-numbered VLAN can be dynamically pinned to link X on fabric interconnect A (see Figure 14). As a result of this process, traffic traverses an extra hop (the Inter-Switch Link [ISL]) to the HSRP or VRRP primary.

![A computer screen shot of a computerAI-generated content may be incorrect.](/c/dam/en/us/solutions/collateral/data-center-virtualization/unified-computing/whitepaper_c11-701962.doc/_jcr_content/renditions/whitepaper_c11-701962_13.png)

Figure 14. 

VLANs load balanced across a pair of switches 

When a switch is directly connected to a pair of HRSP or VRRP routers, the recommended Ethernet switching mode is switch mode, because it provides the optimal path. End-host mode can be used if static pinning is employed. 

Application-specific requirements

Certain applications, such as Microsoft network load balancing in unicast mode, require unknown unicast flooding to operate. In end-host mode, unknown unicast broadcasts are not flooded. In this case switch mode is required. 

In applications that require load balancing in unicast mode, the recommended Ethernet switching mode is switch mode. 

Conclusion

The external interface switching modes to a LAN that are supported in Cisco UCS provides the flexibility that server and network architects need to meet the most complex data center connectivity challenges. End-host mode provides a simple, scalable, and nondisruptive approach in most cases when integrating Cisco UCS into a network. In contrast, switch mode allows the fabric interconnects to operate as traditional Layer-2 switches, enabling features such as spanning tree participation and supporting a wider range of network topologies.

### Learn more


---
