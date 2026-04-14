# Cisco UCS VIC 1340

| | |
|---|---|
| **URL Title** | Cisco UCS VIC 1340 |
| **URL** | https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/ucs-virtual-interface-card-1340/datasheet-c78-732517.html |
| **Long URL** |  |
| **HTML Title** | Cisco UCS Virtual Interface Card 1340 Data Sheet |
| **Source file** | `ucs-docs-raw/html/datasheet-c78-732517.html` |
| **File type** | HTML |
| **Fetched on** | 2026-04-13 13:40:43 |

---

## Page 1: https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/ucs-virtual-interface-card-1340/datasheet-c78-732517.html

  * Skip to content
  * Skip to search
  * Skip to footer


# Cisco UCS Virtual Interface Card 1340 Data Sheet

Save

[Log in](/c/login/index.html?referer=/c/en/us/products/collateral/interfaces-modules/ucs-virtual-interface-card-1340/datasheet-c78-732517.html) to Save Content 

Translations

Download

Print

### Available Languages


### Download Options

  * [PDF](/c/en/us/products/collateral/interfaces-modules/ucs-virtual-interface-card-1340/datasheet-c78-732517.pdf) (648.7 KB)   
View with Adobe Reader on a variety of devices


Updated:June 16, 2019

Document ID:474c2142-fe38-482c-b2f6-082c3e198544

Bias-Free Language

### Bias-Free Language

The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.

` `

Cisco Unified Computing System Overview

The Cisco Unified Computing System™ (Cisco UCS®) is a next-generation, 40-Gbps data center platform that unites computing, network, storage access, and virtualization resources into a cohesive system designed to reduce total cost of ownership (TCO) and increase business agility. The system integrates a low-latency, lossless 40/10- Gbps Ethernet unified network fabric with enterprise-class, x86-architecture servers. The system is an integrated, scalable, multichassis platform in which all resources participate in a unified management domain.

Product Overview

The Cisco UCS Virtual Interface Card (VIC) 1340 (Figure 1) is a 2-port 40-Gbps Ethernet or dual 4 x 10-Gbps Ethernet, Fibre Channel over Ethernet (FCoE)-capable modular LAN on motherboard (mLOM) designed exclusively for the M4 generation of Cisco UCS B-Series Blade Servers. When used in combination with an optional port expander, the Cisco UCS VIC 1340 capabilities is enabled for two ports of 40-Gbps Ethernet.

The Cisco UCS VIC 1340 enables a policy-based, stateless, agile server infrastructure that can present over 256 PCIe standards-compliant interfaces to the host that can be dynamically configured as either network interface cards (NICs) or host bus adapters (HBAs). In addition, the Cisco UCS VIC 1340 supports Cisco® Data Center Virtual Machine Fabric Extender (VM-FEX) technology, which extends the Cisco UCS fabric interconnect ports to virtual machines, simplifying server virtualization deployment and management.

**Figure 1. **Cisco UCS VIC 1340 

![datasheet-c78-732517_0.gif](/c/dam/en/us/products/collateral/interfaces-modules/ucs-virtual-interface-card-1340/datasheet-c78-732517.doc/_jcr_content/renditions/datasheet-c78-732517_0.gif)

Features and Benefits

Stateless and Agile

The personality of the card is determined dynamically at boot time using the service profile associated with the server. The number, type (NIC or HBA), identity (MAC address and World Wide Name [WWN]), failover policy, bandwidth, and quality-of-service (QoS) policies of the PCIe interfaces are all determined using the service profile. The capability to define, create, and use interfaces on demand provides a stateless and agile server infrastructure (Figure 2).

**Figure 2. **Cisco UCS VIC 1340 Architecture 

![datasheet-c78-732517_1.jpg](/c/dam/en/us/products/collateral/interfaces-modules/ucs-virtual-interface-card-1340/datasheet-c78-732517.doc/_jcr_content/renditions/datasheet-c78-732517_1.jpg)

![datasheet-c78-732517_2.jpg](/c/dam/en/us/products/collateral/interfaces-modules/ucs-virtual-interface-card-1340/datasheet-c78-732517.doc/_jcr_content/renditions/datasheet-c78-732517_2.jpg)

Next-Generation Data Center Features

Hardware classification engine provides support for advanced data center requirements including stateless network offloads for NVGRE and VXLAN (VMware only), low-latency features for usNIC and RDMA, and performance optimization applications such as VMQ, DPDK, and Cisco NetFlow.

**Network interface virtualization:** Each PCIe interface created on the VIC is associated with an interface on the Cisco UCS fabric interconnect, providing complete network separation for each virtual cable between a PCIe device on the VIC and the interface on the fabric interconnect.

Cisco SingleConnect Technology

Cisco SingleConnect technology provides an exceptionally easy, intelligent, and efficient way to connect and manage computing in the data center. Cisco SingleConnect technology is an exclusive Cisco innovation that dramatically simplifies the way that data centers connect to:

● Rack and blade servers

● Physical servers and virtual machines

● LAN, SAN, and management networks

The solution addresses the challenges of today’s data center, and the result is a simple, intelligent, and efficient fabric:

● **Easy:** Cisco SingleConnect technology provides a “wire once and walk away” solution that eliminates traditional manual, time-consuming, error-prone processes and instead makes connecting servers to Cisco UCS fast and easy.

● **Intelligent:** The technology is intelligent because it uses a zero-touch model to allocate I/O connectivity (LAN, SAN, and management) across any type of server: physical rack and blade servers and virtual machines. The network intelligence helps Cisco UCS adapt to the needs of applications. Rather than limiting applications to specific servers, Cisco UCS makes it easy to run any workload on any server.

● **Efficient:** The technology is highly efficient because LAN, SAN, and management connections are shared over a single network, increasing utilization while reducing the number of moving parts compared to traditional approaches with multiple networks.

Cisco SingleConnect technology is implemented with an end-to-end system I/O architecture that uses Cisco Unified Fabric and Cisco Fabric Extender Technology (FEX Technology) to connect every Cisco UCS component with a single network and a single network layer. As customers expect from Cisco, the Cisco UCS I/O architecture is based on open standards and is reliable, available, and secure.

Cisco Data Center VM-FEX Technology

Cisco Data Center VM-FEX technology extends fabric interconnect ports directly to virtual machines, eliminating software-based switching in the hypervisor. Cisco Data Center VM-FEX technology collapses virtual and physical networking infrastructure into a single infrastructure that is fully aware of the virtual machines’ locations and networking policies (Figure 3). Cisco Data Center VM FEX technology is implemented by Cisco VICs with a prestandard implementation of the IEEE 802.1BR Port Extender standard.

**Figure 3. **Cisco Data Center VM-FEX with Cisco UCS VIC 1340 

![datasheet-c78-732517_3.jpg](/c/dam/en/us/products/collateral/interfaces-modules/ucs-virtual-interface-card-1340/datasheet-c78-732517.doc/_jcr_content/renditions/datasheet-c78-732517_3.jpg)

Table 1 summarizes the main features and benefits of the Cisco UCS VIC 1340.

**Table 1. **Features and Benefits

Feature |  Benefit  
---|---  
x16 PCIe Gen3 interfaces |  Delivers greater throughput  
2 ports of 40-Gbps unified I/O or 2 sets of 4 x 10-Gbps unified I/O |  ● Delivers 80 Gbps to the server  ● Helps reduce TCO by consolidating the overall number of NICs, HBAs, cables, and switches because LAN and SAN traffic runs over the same mezzanine card and fabric  ● Adapts to either 10-Gbps or 40-Gbps fabric connections   
Over 256 dynamic virtual adapters and interfaces |  Creates fully functional unique and independent PCIe adapters and interfaces (NICs or HBAs) without requiring single-root I/O virtualization (SR-IOV) support from OSs or hypervisors ● Allows these virtual interfaces and adapters to be configured and operated independently, just like physical interfaces and adapters  ● Creates a highly flexible I/O environment needing only one card for all I/O configurations  **Note:** Cisco UCS VIC 1340 hardware is SR-IOV capable, and you can enable SR-IOV after SR-IOV is broadly supported by the popular operating systems. Please refer to UCS Manager configuration limits for your specific OS and environment in the [configuration guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/sw/configuration_limits/2-2/b_UCS_Configuration_Limits_2_2.html#reference_6A3C0158393549E5A3E3F87002234145).  
Cisco SingleConnect technology |  A single unified network: the same network brings LAN, SAN, and management connectivity to each server  
Cisco Data Center VM-FEX technology |  ● Unifies virtual and physical networking into a single infrastructure  ● Provides virtual machine visibility from the physical network and a consistent network operations model for physical and virtual servers  ● Enables configurations and policies to follow the virtual machine during virtual machine migration   
Centralized management |  Enables the mezzanine card to be centrally managed and configured by Cisco UCS Manager and Cisco Intersight™  
Advanced features support |  ● Cisco Adapter FEX  ● DPDK  ● Enic and Fnic  ● Extended RX-ring  ● iSCSI and iSCSI Boot  ● Multi RQ  ● Cisco NetFlow  ● NetQueue  ● N-Port ID Virtualization  ● Receive-Flow Steering  ● Receive-Segment Coalescing  ● Receive-Side Scaling  ● Microsoft SCVMM  ● SR-IOV  ● usNIC  ● Cisco Data Center VM-FEX  ● VM DirectPath  ● VMQ  ● VXLAN/NVGRE   
Network architecture |  Provides a redundant path to the fabric interconnect using hardware-based fabric failover  
More than 900,000 I/O operations per second (IOPS) |  Provides high I/O performance for demanding applications  
Support for lossless Ethernet |  Uses Priority Flow Control (PFC) to enable FCoE as part of the Cisco unified fabric  
Broad OS and hypervisor support |  Supports customer requirements for Microsoft Windows, Red Hat Enterprise Linux, CentOS and Ubuntu, VMware vSphere, and Citrix XenServer  
  
Table 2 summarizes the specifications for the Cisco UCS VIC 1340.

**Table 2. **Product Specifications

Item |  Specification  
---|---  
Standards |  10 Gigabit Ethernet, IEEE 802.3ae, IEEE 802.3x, IEEE 802.1q VLAN, IEEE 802.1p, IEEE 802.1Qaz, IEEE 802.1Qbb, prestandard IEEE 802.1BR jumbo frames up to 9 KB, Fibre Channel Protocol (FCP) (Small Computer System Interface [SCSI-FCP]), and T11 FCoE  
Ports |  ● 2 x 40-Gbps Ethernet ports, with optional port expander card   
Performance |  40-Gbps line rate per port  
Management |  Cisco UCS Manager Release 2.2(3)  
Number of interfaces |  Over 256 virtual interfaces (approximately 8 are reserved for internal use; other factors such as the OS and hypervisor may limit this number further)  
Physical dimensions |  ● Length = 7.25 in. (18.4 cm)  ● Width = 3.65 in. (9.3 cm)   
Typical power |  12 watts (W) 15W with the port expander card  
Inlet operating temperature range |  50 to 95°F (10 to 35°C)  
  
System Requirements

The Cisco UCS VIC 1340 is designed to be used on the Cisco UCS B200 M3 and all M4 Blade Servers.

Warranty Information

Find warranty information at Cisco.com on the [Product Warranties](https://www.cisco.com/en/US/products/prod_warranties_listing.html) page.

Cisco Unified Computing Services

Cisco and our industry-leading partners deliver services that accelerate your transition to a unified computing architecture. Cisco Unified Computing Services can help you create an agile infrastructure, accelerate time to value, reduce costs and risks, and maintain availability during deployment and migration. After deployment, our services can help you improve performance, availability, and resiliency as your business needs evolve, and mitigate risk further. For more information, visit <https://www.cisco.com/go/unifiedcomputingservices>.

Why Cisco?

Cisco UCS continues Cisco’s long history of innovation in delivering integrated systems for improved business results based on industry standards and using the network as the platform. Recent examples include IP telephony, LAN switching, unified communications, and unified I/O. Cisco began the unified computing phase of our Data Center 3.0 strategy several years ago by assembling an experienced team from the computing and virtualization industries to augment our own networking and storage access expertise. As a result, Cisco delivered foundational technologies, including the Cisco Nexus® Family, supporting unified fabric and server virtualization. Cisco UCS completes this phase, delivering innovation in architecture, technology, partnerships, and services. Cisco is well positioned to deliver this innovation by taking a systems approach to computing that unifies network intelligence and scalability with innovative ASICs, integrated management, and standard computing components.

Cisco Capital

Financing to Help You Achieve Your Objectives

Cisco Capital can help you acquire the technology you need to achieve your objectives and stay competitive. We can help you reduce CapEx. Accelerate your growth. Optimize your investment dollars and ROI. Cisco Capital financing gives you flexibility in acquiring hardware, software, services, and complementary third-party equipment. And there’s just one predictable payment. Cisco Capital is available in more than 100 countries. [Learn more](https://www.cisco.com/web/ciscocapital/americas/us/index.html).

For More Information

For more information about the Cisco UCS VIC, visit <https://www.cisco.com/en/US/products/ps12377/index.html>.

### Contact Cisco

  *   * [Get a call from Sales](https://www.cisco.com/site/us/en/about/contact-cisco/index.html?linkclickid=luh-contactus)

##### Call Sales:

  * [ 1-800-553-6387 ](tel:18005536387)
  * US/CAN | 5am-5pm PT
  * [Product / Technical Support](//www.cisco.com/c/en/us/support/index.html)

  * [Training & Certification](https://www.cisco.com/site/us/en/learn/training-certifications/index.html)


### Was this Document Helpful?

Yes No [ ![Feedback](//www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript: void\(0\);)

![](//cisco.112.2o7.net/b/ss/cisco-mobile/5/12345)

---
