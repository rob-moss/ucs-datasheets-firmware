# Cisco UCS 2304 Fabric Extender

| | |
|---|---|
| **URL Title** | Cisco UCS 2304 Fabric Extender |
| **URL** | https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/datasheet-c78-675243.html |
| **Long URL** |  |
| **HTML Title** | Cisco UCS 2304 Fabric Extender Data Sheet |
| **Source file** | `ucs-docs-raw/html/datasheet-c78-675243.html` |
| **File type** | HTML |
| **Fetched on** | 2026-03-19 16:14:17 |

---

## Page 1: https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/datasheet-c78-675243.html

  * Skip to content
  * Skip to search
  * Skip to footer


# Cisco UCS 2304 Fabric Extender Data Sheet

Data Sheet

Save

[Log in](/c/login/index.html?referer=/c/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/datasheet-c78-675243.html) to Save Content 

Translations

Download

Print

### Available Languages


### Download Options

  * [PDF](/c/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/datasheet-c78-675243.pdf) (1.1 MB)   
View with Adobe Reader on a variety of devices


Updated:November 13, 2021

Bias-Free Language

### Bias-Free Language

The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.

__ __ __ __

Contact Cisco

  * Contact Cisco __
  * __

  * __

[Get a call from Sales](https://www.cisco.com/site/us/en/about/contact-cisco/index.html?linkclickid=luh-contactus)

  * __

Call Sales: [ 1-800-553-6387 ](tel:18005536387)   
US/CAN | 5am-5pm PT 

  * __

[Product / Technical Support](//www.cisco.com/c/en/us/support/index.html)

  * __

[Training & Certification](https://www.cisco.com/site/us/en/learn/training-certifications/index.html)


Save

[Log in](/c/login/index.html?referer=/c/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/datasheet-c78-675243.html) to Save Content 

Translations

Download

Print

### Available Languages


### Download Options

  * [PDF](/c/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/datasheet-c78-675243.pdf) (1.1 MB)   
View with Adobe Reader on a variety of devices


Updated:November 13, 2021

#### Table of Contents

  * Cisco Unified Computing System overview
  * Product overview
  * Features and benefits
  * Product specifications
  * Physical specifications
  * Regulatory standards compliance: Safety and EMC
  * Fabric Interconnect Support
  * Transceiver and Cable Support
  * Ordering information
  * Warranty information
  * Cisco environmental sustainability
  * Cisco Unified Computing Services
  * Cisco Capital
  * For more information


` `

![Cisco UCS 2304 Fabric Extender](/c/dam/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/datasheet-c78-675243.docx/_jcr_content/renditions/datasheet-c78-675243_0.png)

Cisco Unified Computing System overview

The Cisco Unified Computing System™ (Cisco UCS™) is a next-generation data center platform that unites computing, network, storage access, and virtualization resources into a cohesive system designed to reduce Total Cost of Ownership (TCO) and increase business agility. The system integrates a low-latency, lossless 40 Gigabit Ethernet unified network fabric with enterprise-class, x86-architecture servers. The system is an integrated, scalable, multichassis platform in which all resources participate in a unified management domain (Figure 1).

![The Cisco Unified Computing System is a highly available cohesive architecture](/c/dam/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/datasheet-c78-675243.docx/_jcr_content/renditions/datasheet-c78-675243_1.png)

Figure 1. 

The Cisco Unified Computing System is a highly available cohesive architecture

Product overview

Cisco UCS 2304 Fabric Extender brings the unified fabric into the blade server enclosure, providing Gigabit Ethernet connectivity between the blade servers and the fabric interconnect, simplifying diagnostics, cabling, and management. It is a third-generation I/O Module (IOM) that shares the same form factor as the second-generation Cisco UCS 2200 Series Fabric Extenders and is backward compatible with the shipping Cisco UCS 5108 Blade Server Chassis.

The Cisco UCS 2304 connects the I/O fabric between the Cisco UCS 6300 Series Fabric Interconnects and the Cisco UCS 5100 Series Blade Server Chassis, enabling a lossless and deterministic Fibre Channel over Ethernet (FCoE) fabric to connect all blades and chassis together. Because the fabric extender is similar to a distributed line card, it does not perform any switching and is managed as an extension of the fabric interconnects. This approach removes switching from the chassis, reducing overall infrastructure complexity and enabling Cisco UCS to scale to many chassis without multiplying the number of switches needed, reducing TCO and allowing all chassis to be managed as a single, highly available management domain.

The Cisco UCS 2304 also manages the chassis environment (power supply, fans, and blades) in conjunction with the fabric interconnect. Therefore, separate chassis management modules are not required.

Cisco UCS 2304 Fabric Extenders fit into the back of the Cisco UCS 5100 Series chassis. Each Cisco UCS 5100 Series chassis can support up to two fabric extenders, allowing increased capacity and redundancy (Figure 2).

![Rear of Cisco UCS 5108 Blade Server Chassis with Two Cisco UCS 2304 Fabric Extenders Inserted](/c/dam/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/datasheet-c78-675243.docx/_jcr_content/renditions/datasheet-c78-675243_2.png)

Figure 2. 

Rear of Cisco UCS 5108 Blade Server Chassis with Two Cisco UCS 2304 Fabric Extenders Inserted

Cisco UCS 2304 Fabric Extender

The Cisco UCS 2304 Fabric Extender has four 40 Gigabit Ethernet, FCoE-capable, Quad Small Form-Factor Pluggable (QSFP+) ports that connect the blade chassis to the fabric interconnect. Each Cisco UCS 2304 can provide one 40 Gigabit Ethernet ports connected through the midplane to each half-width slot in the chassis, giving it a total eight 40G interfaces to the compute. Typically configured in pairs for redundancy, two fabric extenders provide up to 320 Gbps of I/O to the chassis.

**Note** :

There is an updated version of UCS-IOM-2304 (I.e., UCS-IOM-2304V2). 

1. You cannot mix UCS-IOM-2304V2 and UCS-IOM-2304 in the same chassis.

2. UCS-IOM-2304V2 requires Cisco UCS Manager 4.0(4) or later.

Cisco SingleConnect Technology

[Cisco® SingleConnect Technology](https://www.cisco.com/en/US/prod/ps10265/singleconnect.html) provides an easy, intelligent, and efficient way to connect and manage computing in the data center. SingleConnect unifies LAN, SAN, and systems management into one simplified link for rack servers, blade servers, and virtual machines.

SingleConnect is an end-to-end I/O architecture. It incorporates [Cisco UCS Virtual Interface Cards (VICs), Cisco UCS fabric interconnects](https://www.cisco.com/en/US/products/ps10277/prod_models_home.html), and Cisco Fabric Extender Technology (FEX Technology) to connect every server on a single network fabric and on a single network layer. SingleConnect innovations dramatically simplify IT operations and reduce data center costs and are exclusive to Cisco UCS.

SingleConnect provides one connection for:

● Rack servers and blade servers

● LAN, SAN, and systems management

● Physical servers and virtual machines

Features and benefits

Table 1 summarizes the main features and benefits of the Cisco UCS 2304.

**Table 1. **Features and benefits

Feature |  Benefit  
---|---  
**Management by Cisco UCS Manager** |  ● Reduces TCO by removing management modules from the chassis, making the chassis stateless  ● Provides a single, highly available management domain for all system chassis, reducing administrative tasks   
**Autoconfiguration** |  Simplifies operation by automatically synchronizing firmware levels between the fabric extenders and the interconnects  
**Unified fabric** |  ● Decreases TCO by reducing the number of Network Interface Cards (NICs), Host Bus Adapters (HBAs), switches, and cables needed  ● Transparently encapsulates Fibre Channel packets into Ethernet   
**Automatic failover** |  Increases availability with an active/active data plane  
**Scalable bandwidth** |  Reduces TCO by optimizing overall system capacity to match actual workload demands  
**Environmental monitoring** |  Removes the need for chassis management modules  
**Lossless fabric** |  Provides a reliable, robust foundation for unifying LAN and SAN traffic on a single transport  
**Priority Flow Control (PFC)** |  ● Simplifies management of multiple traffic flows over a single network link  ● Supports different classes of service, allowing both lossless and classic Ethernet on the same fabric   
**Systemwide bandwidth management** |  Helps enable consistent and coherent Quality-of-Service (QoS) management throughout the system  
**Cisco Data Center Virtual Machine Fabric Extender (VM-FEX) technology** |  ● Helps enable a consistent operational model between virtual and physical environments  ● Provides the same level of network visibility for virtualized and nonvirtualized environments  ● Improves diagnostic and troubleshooting capabilities in a virtual environment  ● Simplifies network and security policy enforcement when migrating virtual machines from one host to another   
**QSFP+ ports** |  ● Increases flexibility with a range of interconnect solutions, including copper Twinax cable for short runs and fiber for long runs  ● Consumes less power per port than traditional solutions  ● Helps enable cost-effective connections on fabric extenders with Cisco Fabric Extender Transceiver (FET) optics   
**Fabric port channel** |  ● Provides flexibility to bundle fabric ports in a port channel   
  
Product specifications

Performance

● Hardware forwarding at 960 Gbps

● Low-latency cut-through design, providing predictable, consistent traffic latency regardless of packet size, traffic pattern, or enabled features

Layer 2

● Layer 2 VLAN trunks

● IEEE 802.1Q VLAN encapsulation

● Support for up to 1024 VLANs and Virtual SANs (VSANs)

● Support for Data Center VM-FEX architecture

● Jumbo frames on all ports (up to 9216 bytes)

● Pause frames (IEEE 802.3x)

QoS

● Layer 2 IEEE 802.1p (Class of Service [CoS])

● CoS-based egress queuing

● Egress strict-priority queuing

● Egress port-based scheduling: Weighted Round-Robin (WRR)

● Eight hardware queues per port

High availability

● Up to two fabric extenders can work in the Cisco UCS 5100 Series Blade Server Chassis

● Active-active data-plane operation with failover

● Capability to fail over from one fabric extender to another in the event of a failure

● Active-passive management-plane operation

● Support for nonstop management-plane functions; if the active fabric extender fails, the passive fabric extender takes over the chassis management functions

Management

● Management of fabric extenders integrated into Cisco UCS Manager (please refer to the Cisco UCS Manager data sheet for more information about management interfaces)

● Capability to manage blade server chassis components such as power supplies, fans, and blades in conjunction with the fabric interconnect

● Firmware levels between the fabric extender and fabric interconnect always synchronized

Low-Latency, Lossless 40 Gigabit Ethernet Unified Network Fabric

● PFC (per-priority pause frame support)

● Data Center Bridging Exchange (DCBX) Protocol

● IEEE 802.1Qaz: Bandwidth management

Industry standards

● IEEE 802.1p: CoS prioritization

● IEEE 802.1Q: VLAN tagging

● IEEE 802.3: Ethernet

● IEEE 802.3ad: Link Aggregation Control Protocol (LACP)

● IEEE 802.3ba: 40 Gigabit Ethernet

● QSFP+ support

Physical specifications

QSFP+ optics

Cisco UCS products support 40 Gigabit Ethernet QSFP+ copper Twinax cables for short distances and QSFP+ optics for longer distances. The 40 Gigabit Ethernet cables and transceivers qualified for FI 6332 and FI 6332-16UP are supported by Cisco UCS IOM 2304.

Environment

● Physical (height x width x depth): 7.64 x 1.36 x 7.2 in. (19.4 x 3.54 cm)

● Operating temperature: 32 to 104°F (0 to 40°C)

● Nonoperating temperature: -40 to 158°F (-40 to 70°C)

● Humidity: 5 to 95% (noncondensing)

● Altitude: 0 to 10,000 ft (0 to 3000m)

Weight

● 2.8 lb (1.134 kg)

Regulatory standards compliance: Safety and EMC

Table 2 summarizes Cisco UCS 2304 regulatory compliance.

**Table 2. **Regulatory standards compliance: Safety and EMC

Specification |  Description  
---|---  
**Regulatory compliance** |  Products should comply with CE Markings according to directives 2004/108/EC and 2006/95/EC  
**Safety** |  ● UL 60950-1  ● CAN/CSA-C22.2 No. 60950-1  ● EN 60950-1  ● IEC 60950-1  ● AS/NZS 60950-1  ● GB4943   
**EMC: Emissions** |  ● 47CFR Part 15 (CFR 47) Class A  ● AS/NZS CISPR22 Class A  ● CISPR22 Class A  ● EN55022 Class A  ● ICES003 Class A  ● VCCI Class A  ● EN61000-3-2  ● EN61000-3-3  ● KN22 Class A  ● CNS13438 Class A   
EMC: Immunity |  ● EN50082-1  ● EN61000-6-1  ● EN55024  ● CISPR24  ● EN300386  ● KN 61000-4 series   
RoHS |  The product is RoHS 5-compliant with exceptions for leaded Ball Grid Array (BGA) balls and lead press-fit connectors  
  
Fabric Interconnect Support

The Cisco UCS 2304 Fabric Extender is designed to work with third generation of UCS Products.

Transceiver and Cable Support

The Cisco UCS 2304 Fabric Extender supports a variety of Ethernet connectivity options using Cisco 40-Gbps transceivers and 40-Gbs passive cables and active optical cables.

**Table 3. **Cisco UCS 2304 Fabric Extender transceiver-support matrix

Product information |  Description  
---|---  
**QSFP-40G-SR-BD** |  QSFP40G BiDi Short-reach Transceiver  
**QSFP-40G-CSR4** |  QSFP 4x10GBASE-SR Transceiver Module, MPO, 300M  
**QSFP-40G-LR4** |  QSFP 40GBASE-LR4 OTN Transceiver, LC, 10KM  
**QSFP-40G-LR4-S** |  QSFP 40GBASE-LR4 Tmscvr Mod, LC, 10KM, Enterprise-Class  
**QSFP-40G-SR4** |  40GBASE-SR4 QSFP Transceiver Module with MPO Connector  
**QSFP-40G-SR4-S** |  40GBASE-SR4 QSFP Tmscvr Module, MPO Conn, Enterprise-Class  
**FET-40G** |  40G Line Extender for FEX  
**QSFP-40/100-SRBD** |  40GBASE/100GBASE SR-BiDi QSFP transceiver  
  
**Table 4. **Cisco UCS 2304 Fabric Extender cable-support matrix

Product information |  Description  
---|---  
**QSFP-H40G-CU1M** |  40GBASE-CR4 Passive Copper Cable, 1M  
**QSFP-H40G-CU3M** |  40GBASE-CR4 Passive Copper Cable, 3M  
**QSFP-H40G-CU5M** |  40GBASE-CR4 Passive Copper Cable, 5M  
**QSFP-H40G-ACU7M** |  40G BASE-CR4 Active Copper Cable, 7m  
**QSFP-H40G-AOC1M** |  40GBASE Active Optical Cable, 1M  
**QSFP-H40G-AOC2M** |  40GBASE Active Optical Cable, 2M  
**QSFP-H40G-AOC3M** |  40GBASE Active Optical Cable, 3M  
**QSFP-H40G-AOC7M** |  40GBASE Active Optical Cable, 7M  
**QSFP-H40G-AOC10M** |  40GBASE Active Optical Cable, 10M  
**QSFP-H40G-AOC15M** |  40GBASE Active Optical Cable, 15M  
  
**Note: **This is the list of supported transceivers and cables for Cisco UCS 2304 Fabric Extender only. Cross-reference this list against the supported transceivers and cables for the device on the opposing side of the link to confirm compatibility for both the devices.

Ordering information

Table 5 presents ordering information for the Cisco UCS 2304 and UCS 2304v2 Fabric Extenders.

**Table 5. **Ordering information

Part Number |  Description  
---|---  
**UCS-IOM-2304** |  Cisco IOM 2304XP I/O Module (4 External, 8 Internal 40Gb Ports)  
**UCS-IOM-2304=** |  Cisco IOM 2304XP I/O Module (4 External, 8 Internal 40Gb Ports); Spare PID  
**UCS-IOM-2304V2** |  Cisco IOM 2304V2XP I/O Module (4 External, 8 Internal 40Gb Ports)  
**UCS-IOM-2304V2=** |  Cisco IOM 2304V2XP I/O Module (4 External, 8 Internal 40Gb Ports); Spare PID  
  
Warranty information

Find warranty information at Cisco.com on the [Product Warranties](https://www.cisco.com/en/US/products/prod_warranties_listing.html) page.

Cisco environmental sustainability

Information about Cisco’s environmental sustainability policies and initiatives for our products, solutions, operations, and extended operations or supply chain is provided in the “Environment Sustainability” section of Cisco’s [Corporate Social Responsibility](https://www-1.compliance2product.com/c2p/getAttachment.do?code=YM6Y0yThdO6Wj1FxxYPYfUG2dtFkTeFWGpzLRO8tcURFEifUCRV403Tq2ZMWP6Ai) (CSR) Report.

Reference links to information about key environmental sustainability topics (mentioned in the “Environment Sustainability” section of the CSR Report) are provided in the following table:

Sustainability topic |  Reference  
---|---  
Information on product material content laws and regulations |  [Materials](https://www.cisco.com/c/en/us/about/product-innovation-stewardship/materials.html)  
Information on electronic waste laws and regulations, including products, batteries, and packaging |  [WEEE compliance](https://www.cisco.com/c/en/us/about/product-innovation-stewardship/product-recycling/weee-compliance.html)  
  
Cisco makes the packaging data available for informational purposes only. It may not reflect the most current legal developments, and Cisco does not represent, warrant, or guarantee that it is complete, accurate, or up to date. This information is subject to change without notice.

Cisco Unified Computing Services

Using a unified view of data center resources, Cisco and our industry-leading partners deliver services that accelerate your transition to a unified computing environment. Cisco Unified Computing Services helps you quickly deploy your data center resources and optimize ongoing operations to better meet your business needs. For more information about these and other Cisco Data Center Services, visit <https://www.cisco.com/go/dcservices>.

Cisco Capital

Flexible payment solutions to help you achieve your objectives

Cisco Capital makes it easier to get the right technology to achieve your objectives, enable business transformation and help you stay competitive. We can help you reduce the total cost of ownership, conserve capital, and accelerate growth. In more than 100 countries, our flexible payment solutions can help you acquire hardware, software, services and complementary third-party equipment in easy, predictable payments. [Learn more](https://www.cisco.com/go/financing).

For more information

For more information about the Cisco UCS 2304 Fabric Extender, visit <https://www.cisco.com/c/en/us/solutions/data-center-virtualization/fabric-extender-technology-fex-technology/index.html> or contact your local Cisco representative.

### Our experts recommend

  * [Migrate to 40 Gbps with Cisco UCS Fabric Interconnects](/c/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/whitepaper-c11-736918.html "Migrate to 40 Gbps with Cisco UCS Fabric Interconnects")


### Learn more


![](//cisco.112.2o7.net/b/ss/cisco-mobile/5/12345)

---

## Page 2: https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/whitepaper-c11-736918.html

  * Skip to content
  * Skip to search
  * Skip to footer


# Migrate to 40 Gbps with Cisco UCS Fabric Interconnects

Save

[Log in](/c/login/index.html?referer=/c/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/whitepaper-c11-736918.html) to Save Content 

Download

Print

### Available Languages


### Download Options

  * [PDF](/c/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/whitepaper-c11-736918.pdf) (1.1 MB)   
View with Adobe Reader on a variety of devices


Updated:June 30, 2016

Document ID:1461021019269464

Bias-Free Language

### Bias-Free Language

The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/c/en/us/about/social-justice/inclusive-language-policy.html) about how Cisco is using Inclusive Language.

` `

The third-generation Cisco® Unified Fabric for the Cisco Unified Computing System™ (Cisco UCS®) delivers higher speeds for both Ethernet and Fibre Channel connectivity. It provides high performance, consistent latency, and a lossless fabric to address the needs of our customers deploying high-capacity data centers.

The Cisco UCS fabric interconnect is one of the main components of Cisco UCS. It provides the communication backbone for Cisco UCS B-Series Blade Servers and C-Series Rack Servers. All the servers that are attached to the interconnect are part of a single, highly available management domain. By supporting unified fabric, it provides uniform access to both network and storage connectivity for all the servers within its domain. This architecture provides simlified management and greater orchestration for lower total cost of ownership (TCO). The following are the main features that help reduce TCO:

● **Centralized management:** Cisco UCS Manager provides open and extensible embedded management of all software and hardware components of Cisco UCS across multiple chassis, rack servers, composable infrastructure, and virtulal machines through policy- and model-based management.

◦ Because the solution has only a few management touch points, deployment and provisioning processes are faster.

◦ The solution offers stateless computing that allows the use of any resource at any time.

● **Converged infrastructure:** The lossless fabric can support both Ethernet and storage traffic through flexible port configuration. 

◦ The use of less cabling allows more efficient use of power and cooling resources.

◦ The solution supports both Fibre Channel and Ethernet uplink connectivity.

● **High performance and scale:** Cisco Fabric Extender Technology (FEX Technology) enables organizations to scale up to 160 servers in a single unified system, and Cisco Data Center Virtual Machine FEX (VM-FEX) helps provide a consistent operational model and visiblity between the physical and virtual environments.

The third-generation unified fabric interconnects—Cisco UCS 6332 and 6332-16UP Fabric Interconnects—make the transition to 40 Gigabit Ethernet and 16-Gbps Fibre Channel smooth and cost effective. The new components provide investment protection; they are backward compatible with second-generation components, so they can be swapped into exisiting systems or provisioned with newer infrastructure instances.

● Cisco UCS 6300 Series Fabric Interconnects provide 40 Gigabit Ethernet connectivity upstream to access-layer switches and downstream to Cisco UCS servers.

◦ The Cisco 6332 is a 32-port 40-Gbps fabric interconnect in a 1-rack-unit (1RU) that supports both Ethernet and Fibre Channel over Ethernet (FCoE). The 40-Gbps port can also be converted to 10 Gigabit Ethernet ports through either a breakout cable that converts a Quad Small Form-Factor Pluggable (QSFP) port to four SFP ports (called a QSFP-to-4xSFP breakout cable) or a QSFP-to-SFP adapter (QSA), which converts a 40-Gbps port into a single 10-Gbps port.

◦ The Cisco 6332-16UP is 24-port 40-Gbps fabric interconnect with 16 fixed unified ports (UPs) supporting 1 and 10 Gigabit Ethernet or 4-, 8-, or 16-Gbps Fibre Channel connections in a 1RU form factor. The 40-Gbps port can also be converted to 10-Gbps ports through either a QSFP to 4xSFP breakout cable or a QSA, which converts a 40-Gbps port into a single 10-Gbps port.

● The Cisco UCS 2304 Fabric Extender is a third-generation I/O module (IOM) that brings 40-Gbps fabric to the blade server chassis. It provides four 40-Gbps connections to the fabric interconnet and eight 40-Gbps connections to the server through either a native 40-Gbps link or a port channel consisting of four 10-Gbps links. The Cisco UCS 2304 can be inserted into an existing blade chassis.

● The Cisco Nexus® 2348UPQ 40GE Fabric Extender connects up to 40 Gigabit Ethernet links to the fabric interconnects and supports 1 and 10 Gigabit Ethernet connections downstream to the rack servers.

Audience

The target audience for this document consists of system architects, system engineers, and any other technical personnel who are responsible for planning or upgrading fabric interconnects. Although every effort has been made to make this document appeal to the widest possible audience, it assumes that the audience has an understanding of Cisco UCS hardware, terminology, and configuration.

Objective

This document describes the process of upgrading from Cisco UCS 6200 Series Fabric Interconnects to fabric interconnects based on the Cisco UCS 6332. After reading this document, the reader should have a complete understanding of the upgrade process and any factors that need to be taken into consideration. Table 1 summarizes the various upgrade paths between fabric interconnects, fabric extenders and IOMs, and Cisco Nexus 2000 Series Fabric Extenders. The Cisco UCS C-Series servers are connected in a single-wire managemet configuration. Direct-connect disruption varies depending on the number of adapters that are connected to the fabric interconnect. A single-adapter configuration is less disruptive than a dual-adapter configuration. A single-adapter configuration does not require a server reacknowledgment, whereas a dual-adapter configuration does. A server reacknowledgment is also required for a direct server connection when the new port connection is different from the original.

For a Cisco UCS C-Series server located behind a Cisco Nexus 2000 Series Fabric Extender, in most cases a FEX acknowledgment is all that is required to reestablish the link. In some cases, however, a server reacknowledgment is required. 

Note:  Two server acknowledgments will be required: one for each fabric interconnect exchanged. To reduce the number of server acknowledgments, the acknowledgment process can be performed after tha last fabric interconnect has been upgraded to the Cisco UCS 6332 platform.

For Cisco UCS B-Series servers, a server acknowledgment is not required for any extraneous connection cases for either a fabric interconnect upgrade or a fabric interconnect upgrade plus IOM upgrade from the Cisco UCS 2200 Series to the Cisco UCS 2304.

**Table 1. **Migration Support Matrix for Infrastructure Hardware

From |  To |  State  
---|---|---  
Cisco UCS 6100 Series and 2100XP platform |  Cisco UCS 6332 platform and 2300 Series |  Online upgrade not supported; export and import configuration Cisco UCS Manger is possible  
Cisco UCS 6200 Series and 2200XP platform |  Cisco UCS 6332 platform and 2200 Series |  Little disruption  
Cisco UCS 6200 Series and 2200XP platform |  Cisco UCS 6332 platform and 2300 Series |  Little disruption  
Cisco UCS C-Series  
Cisco UCS 6200 Series: direct connect |  Cisco UCS 6332 platform: direct-connect |  Variable disruption  
Cisco UCS 6200 Series and Cisco Nexus 2232 |  Cisco UCS 6332 platform and Cisco Nexus 2232 |  Variable disruption  
Cisco UCS 6200 Series and Cisco Nexus 2232 |  Cisco UCS 6332 platform and Cisco Nexus 2348UPQ |  Major disruption  
  
The minimum Cisco UCS software release required for Cisco UCS 6332 platform fabric interconnects and Cisco UCS 2304 IOMs is Release 3.1(1). Therefore, you must update the Cisco UCS 6200 Series fabric interconnects and the IOMs, fabric extenders, and servers to Release 3.1(1) before you can start the upgrade process (Table 2).

**Table 2. **Software Migration from Cisco UCS 6200 Series Fabric Interconnect to Cisco UCS 6332 Platform Support Matrix for Host Firmware

Host Firmware |  Support |  Notes  
---|---|---  
Release 2.2 or earlier |  No |   
Release 3.1 or later |  Yes |  A Cisco UCS M4 server with a Cisco UCS Virtual Interface Card (VIC) 1340 and port expander that is migrated to a Cisco UCS 2304 IOM will appear as a native 40-Gbps port. All other connections will appear as port channels.  
  
Preplanning

Before beginning the migration process, be sure that your system is ready.

Inventory Check

Because the Cisco UCS 6332 platform fabric interconnects are first supported in Cisco UCS Release 3.1(1), the existing Cisco UCS domain needs to be upgraded to Release 3.1(1) before you can start the upgrade process. However, before you upgrade the existing Cisco UCS domain to Release 3.1(1), you should inventory the system. Cisco UCS Release 3.1(1) deprecates older hardware: specifically, generation-one hardware. Tables 3 and 4 list the hardware supported in Release 3.1(1). If the hardware is not listed, then it will be not recognized when you upgrade to Release 3.1(1), thus preventing successful migration to the Cisco UCS 6332 platform.

**Table 3. **Server Support for Cisco UCS Release 3.1(1)

Cisco UCS B-Series Blade Server |  M2 |  M3 |  M4 |  |  Cisco UCS C-Series Rack Server |  M2 |  M3 |  M4  
---|---|---|---|---|---|---|---|---  
Cisco UCS B22  |  |  Yes |  |  |  Cisco UCS C22  |  |  Yes |   
Cisco UCS B200  |  Yes |  Yes |  Yes |  |  Cisco UCS C24 |  |  Yes |   
Cisco UCS B230 |  Yes. |  |  |  |  Cisco UCS C220 |  |  Yes |  Yes  
Cisco UCS B250 |  Yes |  |  |  |  Cisco UCS C240 |  |  Yes |  Yes  
Cisco UCS B260  |  |  |  Yes |  |  Cisco UCS C260 |  Yes |  |   
Cisco UCS B420 |  |  Yes |  Yes |  |  Cisco UCS C420 |  |  Yes |   
Cisco UCS B440 |  Yes |  |  |  |  Cisco UCS C460 |  Yes |  |  Yes  
Cisco UCS B460 |  |  |  Yes |  |  |  |  |   
  
**Table 4. **I/O and Fabric Extender Support for Cisco UCS Release 3.1(1)

Cisco UCS B-Series Server Adapter |  IOM |  |  Cisco UCS C-Series Server |  Fabric Extender  
---|---|---|---|---  
Cisco UCS VIC 1240  |  Cisco UCS 2204 |  |  Cisco UCS VIC 1225 and 1225T |  Cisco Nexus 2232PP  
Cisco UCS VIC 1280 |  Cisco UCS 2208 |  |  Cisco UCS VIC 1227 and 1227T |  Cisco Nexus 2232TM-E  
Cisco UCS VIC 1340 |  Cisco UCS 2304 |  |  Cisco UCS VIC 1385 |  Cisco Nexus 2348UPQ  
Cisco UCS VIC 1380 |  |  |  Cisco UCS VIC 1387 |   
|  |  |  Broadcom BCM5709, BCM57712, and BCM57810 |   
|  |  |  QLogic QLE8442 and QLE8362 |   
|  |  |  QLogic 8- and 16-Gbps Fibre Channel |   
|  |  |  Intel i350, x520, and x540 |   
|  |  |  Emulex OCe14012 |   
|  |  |  Emulex 8- and 16-Gbps Fibre Channel |   
  
Port and Cabling Planning

Port schemes for the two different generations are vastly different. Thus, port mapping is an important step in the preplanning process to help ensure a smooth transition from a fabric based on the Cisco UCS 6200 Series to a fabric based on the Cisco UCS 6332 platform. The first step in port planning is to map the Fibre Channel ports, first asking:

● Will Fibre Channel be used, or are you moving to FCoE?

● How many Fibre Channel ports are needed?

Figures 1, 2, and 3 show the port numbering schemes.

**Figure 1. **Cisco UCS 6332 Port Numbering Scheme 

![whitepaper-c11-736918_0.jpg](/c/dam/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/whitepaper-c11-736918.doc/_jcr_content/renditions/whitepaper-c11-736918_0.jpg)

**Figure 2. **Cisco UCS 6332-16UP Port Numbering Scheme 

![whitepaper-c11-736918_1.jpg](/c/dam/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/whitepaper-c11-736918.doc/_jcr_content/renditions/whitepaper-c11-736918_1.jpg)

Note:  Fibre Channel ports are available only on the Cisco UCS 6332-16UP. On the 16UP, the ports can be converted from left to right from Ethernet to Fibre Channel. The first block is ports 1 to 6, the second block is ports 1 to 12, and the third block is ports 1 to 16.

**Figure 3. **Fibre Channel and Ethernet Port Schemes for the 16 Unified Ports in the Cisco UCS 6332-16UP Model 

![whitepaper-c11-736918_2.jpg](/c/dam/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/whitepaper-c11-736918.doc/_jcr_content/renditions/whitepaper-c11-736918_2.jpg)

After the Fibre Channel ports are set, you need to map the Ethernet connections. If you need 10 Gigabit Ethernet connections, whether for appliance ports, direct connections, or Cisco UCS 2200XP IOMs, then you need to consider additional factors. All the 40-Gbps ports can be converted to 10-Gbps ports through either a QSFP-to-4xSFP 40-Gbps breakout cable or a QSA module that converts the 40-Gbps port to a single 10-Gbps port. Table 5 provides a support matrix for conversion from 40-Gbps to 10-Gbps ports.

**Table 5. **Support Matrix for Conversion from 40-Gbps to 10-Gbps Ports 

FI Model |  40-Gbps Breakout Cable |  QSA  
---|---|---  
Cisco UCS 6332 |  Ports 1 to 12 and 15 to 26 |  Ports 1 to 12 and 15 to 26  
Cisco UCS 6332-16UP |  Ports 17 to 34 |  Ports 17 to 34  
  
Note:  The maximum number of 40-Gbps ports that break out to four 10-Gbps ports with a second no-drop class and jumbo maximum transmission unit (MTU) configuration is four. Otherwise, there is no limit on the number of ports that can be broken out to four 10-Gbps ports.

VSAN Considerations

Depending on the type of Cisco UCS 6332 platform fabric interconnect to which you are upgrading, the number of VSANs may need to be taken into consideration. The Cisco UCS 6332-16UP model supports only 15 VSANs, and if the current environment has more than 15, then VSAN reduction is required. The Cisco UCS 6332 model supports 32 VSANs, and thus no action is required. 

Migration Procedure

After taking the appropriate steps to move workloads and decommission any old hardware, use the steps presented here to perform the upgrade process.

Note:  Although the upgrade can be performed while the system is active, Cisco recommends that you perform the upgrade during a maintenance window.

Step 1.  If you are upgrading to the Cisco UCS 6332-16UP, verify that the environment does not exceed 15 VSANs.

Step 2.  Download Cisco UCS Release 3.1(1) from the Cisco Support site at <https://software.cisco.com/download/navigator.html> and upgrade the existing Cisco UCS 6200 Series domain to Release 3.1(1).

Step 3.  Fail over traffic from the subordinate server to the primary server. You can do this in several ways, as listed in Table 6.

**Table 6. **Traffic Failover Method

Failover Method |  Considerations  
---|---  
Disable uplink |  Individually disable the uplink ports for Ethernet, Fibre Channel, and FCoE connections. Ethernet only: A virtual network interface card (vNIC) with network control policy with a warning on “Action on Uplink Fail” will not be disabled. Thus, the NIC needs to be disabled manually for failover.  
Disable all uplink interfaces |  With a single click, this method disables all uplinks that are not in a port channel. This method needs to be implemented on Ethernet, Fibre Channel, and FCoE connections. Ethernet only: As with the disable uplink method, vNICs with network control policy with a warning on “Action on Uplink Fail” are not disabled. Manual intervention is required.  
Disable all port channels |  With a single click, this method disables all uplinks that are in a port channel, links that are not in a port channel are excluded. This method needs to be implemented on Ethernet, Fibre Channel, and FCoE connections. Ethernet only: As with the disable uplink method, vNICs with network control policy with a warning on “Action on Uplink Fail” are not disabled. Manual intervention is required.  
Fabric evacuation |  This method disables all the server ports, which disables both the vNIC and virtual host bus adapter (vHBA) for the host. This method does not disable the virtual interface (VIF) on Cisco UCS C-Series servers that are directly connected to the fabric interconnect. For those connections, you need to disable the ports manually. Figure 4 shows this method.  
  
Note:  For Cisco UCS domains that use blades only, Cisco recommends the fabric evacuation method. This approach provides the fastest way to validate proper traffic failover. It also lets you back out the failover simply by turning the fabric evacuation off.

a. If Cisco UCS C-Series servers are directly attached to the fabric interconnect, then manually disable either the port or the uplink for Ethernet, Fibre Channel, and FCoE.

**Figure 4. **Procedures and Validation for Fabric Evacuation 

![whitepaper-c11-736918_3.jpg](/c/dam/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/whitepaper-c11-736918.doc/_jcr_content/renditions/whitepaper-c11-736918_3.jpg)

Step 4.  Verify that traffic is flowing over the primary fabric interconnect.

a. If the Cisco Nexus 2232PP 10GE is being retired and replaced by Cisco Nexus 2348UPQ 10GE, then decommission and remove old fabric extender from Cisco UCS Manager.

Step 5.  As mentioned in the “Port and Cabling Planning” section, port schemes are vastly different, so you should unconfigure all the ports on the subordinate interconnect and reconfigure the ports on the new fabric interconnect after it joins the cluster.

Note:  You do not need to delete the port-channel groups because they can be reused, but you should verify that the individual ports are removed from LAN and SAN port channels, VLAN groups, etc.

Step 6.  Remove the cable from the downed subordinate fabric interconnect.

a. If you are replacing the IOM and Cisco Nexus 2232 with the Cisco UCS 2304 and Cisco Nexus 2348-UPQ, then this is the time to make the replacement.

Step 7.  Replace with the new Cisco UCS 6332 platform fabric interconnect and connect the L1 to L2 connections between the Cisco UCS 6200 Series primary interconnect to the Cisco UCS 6332 platform subordinate interconnect.

Step 8.  Reconnect the components (IOM, Cisco Nexus 2200 and 2300 Series, and Cisco UCS C-Series servers) to the Cisco UCS 6332 platform subordinate interconnect according to the port planning table.

Step 9.  Power up the Cisco UCS 6332 platform subordinate interconnect. If it is properly cabled with the correct software version, then the subordinate interconnect will recognize that it is connecting to an existing cluster (Figure 5).

**Figure 5. **Startup Screen and Topology Screen of the Cisco UCS 6332 Platform Subordinate Interconnect After Connection to the Cluster 

![whitepaper-c11-736918_4.jpg](/c/dam/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/whitepaper-c11-736918.doc/_jcr_content/renditions/whitepaper-c11-736918_4.jpg)

Step 10.  Enter **show cluster extended-state** to verify the cluster state.

B26-A# show cluster extended-state

Cluster Id: 0xac919450846211e5-0x833f002a6a923061

Start time: Wed Jan 27 22:43:01 2016

Last election time: Thu Jan 28 03:40:02 2016

A: UP, PRIMARY

B: UP, SUBORDINATE

A: memb state UP, lead state PRIMARY, mgmt services state: UP

B: memb state UP, lead state SUBORDINATE, mgmt services state: UP

heartbeat state PRIMARY_OK

INTERNAL NETWORK INTERFACES:

eth1, UP

eth2, UP

HA READY

Detailed state of the device selected for HA storage:

Chassis 1, serial: FOX1734GXB3, state: active

Server 1, serial: FCH1735V06K, state: active

Step 11.  Configure the ports (Fibre Channel ports, server ports, appliance ports, breakout ports, uplink ports, etc.) on the Cisco UCS 6332 platform subordinate fabric interconnect (Figure 6). 

The system will reboot when you change ports from Ethernet to Fibre Channel or from 40-Gbps to 10-Gbps or vice versa. To reduce the number of reboots, apply changes to multiple ports instead of one by one.

**Figure 6. **Multiple Port Configurations Applied Through Unified Ports for Fibre Channel and Internal Fabric Manager for Breakout Ports 

![whitepaper-c11-736918_5.jpg](/c/dam/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/whitepaper-c11-736918.doc/_jcr_content/renditions/whitepaper-c11-736918_5.jpg)

Step 12.  Verify server discovery. The IOM discovery process on the Cisco UCS 6332 platform subordinate interconnect may take a few minutes to complete and become operational. In certain situations, you may need to acknowledge the IOM (choose Equipment > Chassis > Chassis X > IO Modules > IO Module X), as shown in Figure 7.

**Figure 7. **If Necessary, Acknowledge the IOM 

![whitepaper-c11-736918_6.jpg](/c/dam/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/whitepaper-c11-736918.doc/_jcr_content/renditions/whitepaper-c11-736918_6.jpg)

a. Cisco UCS C-Series servers that are directly connected with dual adapters or are connected to a different port require server acknowledgment to properly update the port mapping. To reduce the number of server reboots to one, you can perform this step after the other fabric interconnect has been replaced.

b. For servers connected to the Cisco Nexus 2200 platform fabric extenders, in most cases a fabric extender reacknowledgment will reestablish a connection. Otherwise, a server reacknowledgment is needed. To verify the connection, use the command shown here.

B26-A# connect adapter 2/1

adapter 0/2/1 # connect

<output truncated>

adapter 0/2/1 (top):1# attach-mcp

<output truncated>

adapter 0/2/1 (mcp):1# vnic

<output truncated>

\------------------------------------------ --------- --------------------------

v n i c l i f v i f

id name type h:bb:dd.f state lif state uif ucsm idx vlan state

\--- -------------- ------- --------- ----- --- ----- --- ----- ----- ---- -----

15 vnic_1 enet 0:05:00.0 UP 3 UP - 0 790 110 180 UP

=>1 789 21 180 UP

Step 13.  After all port configuration processes are complete, including the process of adding ports back into LAN and SAN port channels and VLAN groups, you need to validate LAN and SAN connectivity. Use the appropriate show commands, such as the following:

● **show interface status**

● **show port-channel summary**

● **show interface trunk**

● **show flogi database**

● **show fcns database**

Note that a Cisco UCS M4 server with a Cisco UCS VIC 1340 and a port expander that is connected to a Cisco UCS 2304 IOM will be connected as a native 40-Gbps port. You can verify this connection by entering the show interface status command in the Cisco NX-OS Software shell:

B26-B(nxos)# show interface status

<output truncated>

\--------------------------------------------------------------------------------

Ethernet VLAN Type Mode Status Reason Speed Port

Interface Ch #

\--------------------------------------------------------------------------------

Eth1/1/1 1 eth access down Member port of 40G 10G(D) --

Eth1/1/2 1 eth access down Member port of 40G 10G(D) --

Eth1/1/3 1 eth access down Member port of 40G 10G(D) --

Eth1/1/4 1 eth vntag up none 40G(D) –

<output truncated>

Step 14.  Reestablish flow on the subordinate fabric interconnect, the Cisco UCS 6332 platform. In the case shown here, fabric evacuation will be turned off (Figure 8).

a. If other method used other than fabric evacuation, then enable uplinks for Ethernet, Fibre Channel, and FCoE.

**Figure 8. **Reestablishing Traffic Flow on Cisco UCS 6332 Platform Subordinate Interconnect by Turning Off Fabric Evacuation and Validating Port Connectivity 

![whitepaper-c11-736918_7.jpg](/c/dam/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/whitepaper-c11-736918.doc/_jcr_content/renditions/whitepaper-c11-736918_7.jpg)

Note:  Some backplane ports may report link down because no service profile is associated with that server or the host is powered off.

Step 15.  Verify that traffic is flowing normally on the Cisco UCS 6332 platform subordinate interconnect.

Step 16.  After verifying traffic flow, promote the Cisco UCS 6332 platform subordinate interconnect to primary status by entering the **cluster lead b** command in the local-mgmt shell on the primary fabric interconnect:

B26-A(local-mgmt)# cluster lead b

If the system is at 'infrastructure firmware' auto-install 'pending user Ack' stage, please check the outstanding faults (scope monitoring <enter> show new-faults) and make sure the data-paths on FI-B are established properly before making it primary to ensure there is no data outage.

Do you want to continue? (yes/no):yes

Cluster Id: 0xac919450846211e5-0x833f002a6a923061

Step 17.  Enter the **show cluster extended-state** command to verify that the primary role has switched to the Cisco UCS 6332 platform and that high availability (HA) is in the ready state. Figure 9 shows the results in Cisco UCS Manager.

B26-A(local-mgmt)# show cluster extended-state

Cluster Id: 0xac919450846211e5-0x833f002a6a923061

Start time: Wed Jan 27 22:43:01 2016

Last election time: Thu Jan 28 06:59:27 2016

A: UP, SUBORDINATE

B: UP, PRIMARY

A: memb state UP, lead state SUBORDINATE, mgmt services state: UP

B: memb state UP, lead state PRIMARY, mgmt services state: UP

heartbeat state PRIMARY_OK

INTERNAL NETWORK INTERFACES:

eth1, UP

eth2, UP

HA READY

Detailed state of the device selected for HA storage:

Chassis 1, serial: FOX1734GXB3, state: active

Server 1, serial: FCH1735V06K, state: active

**Figure 9. **All Servers Are Connected Correctly to the New Cisco UCS 6332 Platform Subordinate Fabric Interconnect 

![whitepaper-c11-736918_8.jpg](/c/dam/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/whitepaper-c11-736918.doc/_jcr_content/renditions/whitepaper-c11-736918_8.jpg)

  


Step 18.  Repeat the steps 3 through 14 to replace the other Cisco UCS 6200 Series Fabric Interconnect. Figure 10 shows the results.

**Figure 10. **Final Topology After Completing the Fabric Interconnect Migration 

![whitepaper-c11-736918_9.jpg](/c/dam/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/whitepaper-c11-736918.doc/_jcr_content/renditions/whitepaper-c11-736918_9.jpg)

Step 19.  (Optional) Promote fabric interconnect A to the primary role with the command cluster lead a in the local-mgmt shell of the primary fabric interconnect (B).

Step 20.  Check for faults from old configurations, policies, software packages, etc. Remove any noncompliant configurations, policies, and software packages to clear faults.

Transitioning from Cisco UCS 6100 Series Fabric Interconnect to Cisco UCS 6332 Platform 

In-service upgrade from the Cisco UCS 6100 Series to Cisco UCS 6332 platform fabric interconnects is not supported. The upgrade path requires the existing Cisco UCS instance to use Cisco UCS Software Release 3.1(1), which does not support first-generation hardware. Thus, the better approach is to set up a new pod with the current hardware and migrate the workload to that. 

You can export and import the configuration from the Cisco UCS 6100 Series to the 6300 Series, maintain the pools, policies, and service profiles. Any irrelevant or dated policies and configurations will be ignored by Cisco UCS Manager with Release 3.1(1).

If you want to perform in-service migration, this will require a multiple-upgrade path: from the Cisco UCS 6100 and 2100 Series to the Cisco UCS 6200 and 2200 Series, and then to the Cisco UCS 6332 platform and 2200 Series or the Cisco UCS 6332 and 2300 Series, with the assumption that the server hardware has been verified to support this migration.

For More Information

● Read more about Cisco UCS products at   
<http://www.cisco.com/c/en/us/products/servers-unified-computing/index.html>.

● Read more about Cisco UCS 6332 platform fabric interconnects at <http://www.cisco.com/c/en/us/products/servers-unified-computing/ucs-6300-series-fabric-interconnects/index.html>.

● Read more about the Cisco UCS 2304 Fabric Extender at <http://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/data_sheet_c78-675243.html?cachemode=refresh>.

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

## Page 3: http://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/data_sheet_c78-675243.html?cachemode=refresh

  * Skip to content
  * Skip to search
  * Skip to footer


# Cisco UCS 2200 Series Fabric Extenders Data Sheet

Save

[Log in](/c/login/index.html?referer=/c/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/data_sheet_c78-675243.html) to Save Content 

Translations

Download

Print

### Available Languages


### Download Options

  * [PDF](/c/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/data_sheet_c78-675243.pdf) (924.7 KB)   
View with Adobe Reader on a variety of devices


Updated:February 14, 2019

Document ID:348488ee-6078-4f18-9b0f-9cf7c488629d

Bias-Free Language

### Bias-Free Language

The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/c/en/us/about/social-justice/inclusive-language-policy.html) about how Cisco is using Inclusive Language.

` `

![data_sheet_c78-675243_0.jpg](/c/dam/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/data_sheet_c78-675243.docx/_jcr_content/renditions/data_sheet_c78-675243_0.jpg)

Cisco Unified Computing System Overview

The Cisco Unified Computing System™ (Cisco UCS™) is a next-generation data center platform that unites compute, network, storage access, and virtualization resources into a cohesive system designed to reduce total cost of ownership (TCO) and increase business agility. The system integrates a low-latency, lossless 10 Gigabit Ethernet unified network fabric with enterprise-class, x86-architecture servers. The system is an integrated, scalable, multichassis platform in which all resources participate in a unified management domain (Figure 1).

**Figure 1. **The Cisco Unified Computing System Is a Highly Available Cohesive Architecture 

![data_sheet_c78-675243_1.jpg](/c/dam/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/data_sheet_c78-675243.docx/_jcr_content/renditions/data_sheet_c78-675243_1.jpg)

Product Overview

Cisco UCS 2200 Series Fabric Extenders bring the unified fabric into the blade server enclosure, providing multiple 10 Gigabit Ethernet connections between blade servers and the fabric interconnect, simplifying diagnostics, cabling, and management. It is a second-generation I/O module (IOM) that shares the same form factor with the first-generation Cisco UCS 2100 Series Fabric Extenders IOM and is backward-compatible with the shipping Cisco UCS 5108 Blade Server Chassis.

The Cisco UCS 2200 Series extends the I/O fabric between the Cisco UCS 6100 and 6200 Series Fabric Interconnects and the Cisco UCS 5100 Series Blade Server Chassis, enabling a lossless and deterministic Fibre Channel over Ethernet (FCoE) fabric to connect all blades and chassis together. Since the fabric extender is similar to a distributed line card, it does not perform any switching and is managed as an extension of the fabric interconnects. This approach removes switching from the chassis, reducing overall infrastructure complexity and enabling Cisco UCS to scale to many chassis without multiplying the number of switches needed, reducing TCO and allowing all chassis to be managed as a single, highly available management domain.

The Cisco UCS 2200 Series also manages the chassis environment (the power supply and fans as well as the blades) in conjunction with the fabric interconnect. Therefore, separate chassis management modules are not required.

Cisco UCS 2200 Series Fabric Extenders fit into the back of the Cisco UCS 5100 Series chassis. Each Cisco UCS 5100 Series chassis can support up to two fabric extenders, allowing increased capacity and redundancy (Figure 2).

**Figure 2. **Rear of Cisco UCS 5108 Blade Server Chassis with Two Cisco UCS 2208XP Fabric Extenders Inserted 

![data_sheet_c78-675243_2.jpg](/c/dam/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/data_sheet_c78-675243.docx/_jcr_content/renditions/data_sheet_c78-675243_2.jpg)

**Cisco UCS 2208XP Fabric Extender**

The Cisco UCS 2208XP Fabric Extender (Figure 3) has eight 10 Gigabit Ethernet, FCoE-capable, Enhanced Small Form-Factor Pluggable (SFP+) ports that connect the blade chassis to the fabric interconnect. Each Cisco UCS 2208XP has thirty-two 10 Gigabit Ethernet ports connected through the midplane to each half-width slot in the chassis. Typically configured in pairs for redundancy, two fabric extenders provide up to 160 Gbps of I/O to the chassis.

**Figure 3. **Cisco UCS 2208XP Fabric Extender 

![data_sheet_c78-675243_3.jpg](/c/dam/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/data_sheet_c78-675243.docx/_jcr_content/renditions/data_sheet_c78-675243_3.jpg)

**Cisco UCS 2204XP Fabric Extender**

The Cisco UCS 2204XP Fabric Extender (Figure 4) has four 10 Gigabit Ethernet, FCoE-capable, SFP+ ports that connect the blade chassis to the fabric interconnect. Each Cisco UCS 2204XP has sixteen 10 Gigabit Ethernet ports connected through the midplane to each half-width slot in the chassis. Typically configured in pairs for redundancy, two fabric extenders provide up to 80 Gbps of I/O to the chassis.

**Figure 4. **Cisco UCS 2204XP Fabric Extender 

![data_sheet_c78-675243_4.jpg](/c/dam/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/data_sheet_c78-675243.docx/_jcr_content/renditions/data_sheet_c78-675243_4.jpg)

**Cisco SingleConnect Technology**

[Cisco SingleConnect Technology](//www.cisco.com/en/US/prod/ps10265/singleconnect.html) is an easy, intelligent, and efficient way to connect and manage computing in the data center. Cisco SingleConnect unifies LAN, SAN, and systems management into one simplified link for rack servers, blade servers, and virtual machines.

SingleConnect is an end-to-end I/O architecture. It incorporates [Cisco Virtual Interface Cards](//www.cisco.com/en/US/products/ps10277/prod_models_home.html), [Cisco UCS Fabric Interconnects](//www.cisco.com/en/US/products/ps11544/index.html), and Cisco Fabric Extender (FEX) Technology to connect every server on a single network fabric and on a single network layer. SingleConnect innovations dramatically simplify IT operations, reduce data center costs, and are exclusive to the Cisco Unified Computing System (Cisco UCS).

Cisco SingleConnect is one connection:

● For rack servers and blade servers

● For LAN, SAN, and systems management

● For physical servers and virtual machines

Features and Benefits

Table 1 summarizes the main features and benefits of the Cisco UCS 2200 Series.

**Table 1. **Features and Benefits

Feature |  Benefit  
---|---  
Management by Cisco UCS Manager |  ● Reduces TCO by removing management modules from the chassis, making the chassis stateless  ● Provides a single, highly available management domain for all system chassis, reducing administrative tasks   
Autoconfiguration |  Simplifies operation by automatically synchronizing firmware levels between the fabric extenders and the interconnects  
Unified fabric |  ● Decreases TCO by reducing the number of network interface cards (NICs), host bus adapters (HBAs), switches, and cables needed  ● Transparently encapsulates Fibre Channel packets into Ethernet   
Automatic failover  |  Increases availability with an active-active data plane  
Scalable bandwidth |  Reduces TCO by optimizing overall system capacity to match actual workload demands  
Environmental monitoring |  Removes the need for chassis management modules  
Lossless fabric |  Provides a reliable, robust foundation for unifying LAN and SAN traffic on a single transport  
Priority flow control (PFC) |  ● Simplifies management of multiple traffic flows over a single network link  ● Supports different classes of service, allowing both lossless and classic Ethernet on the same fabric   
Systemwide bandwidth management |  Helps enable consistent and coherent quality-of-service (QoS) management throughout the system  
Cisco Data Center Virtual Machine Fabric Extender (VM-FEX) technology |  ● Helps enable a consistent operational model between virtual and physical environments  ● Provides the same level of network visibility for virtualized and nonvirtualized environments  ● Improves diagnostic and troubleshooting capabilities in a virtual environment  ● Simplifies network and security policy enforcement when migrating virtual machines from one host to another   
SFP+ ports |  ● Increases flexibility with a range of interconnect solutions, including copper Twinax cable for short runs and fiber for long runs  ● Consumes less power per port than traditional solutions  ● Helps enable cost-effective connections on fabric extenders with Cisco Fabric Extender Transceiver (FET) optics   
Fabric PortChannel |  ● Provides flexibility to bundle fabric ports in a PortChannel   
  
Product Specifications

**Cabling**

Table 2 presents cabling specifications for the Cisco UCS 2200 Series.

**Table 2. **Cabling Specifications

Connector (Media) |  Cable |  Distance |  Power (Each Side) |  Transceiver Latency (Link) |  Standard  
---|---|---|---|---|---  
SFP+ copper (CU) |  Twinax |  1, 3, and 5m |  Approximately 0.1 watt (W) |  Approximately 0.1 microsecond |  SFF 8431  
SFP+ FET |  MM OM2 MM OM3 MM OM4 |  25 and 100m |  1W |  Approximately 0 microseconds |  IEEE 802.3ae  
SFP+ short-reach   
(SR) and multimode fiber (MMF) |  MM OM2 MM OM3 MM OM4 |  82 and 300m |  1W |  Approximately 0 microseconds |  IEEE 802.3ae  
SFP+ long-reach (LR) MMF and SR  |  SMF |  Up to 300m over SMF |  1W |  Approximately 0 microseconds |  IEEE 802.3ae  
  
**Performance**

● Hardware forwarding at 640 Gbps

● Low-latency cut-through design, providing predictable, consistent traffic latency regardless of packet size, traffic pattern, or enabled features

**Layer 2**

● Layer 2 VLAN trunks

● IEEE 802.1Q VLAN encapsulation

● Support for up to 1024 VLANs and virtual SANs (VSANs)

● Support for Cisco Data Center VM-FEX architecture

● Jumbo frames on all ports (up to 9216 bytes)

● Pause frames (IEEE 802.3x)

**QoS**

● Layer 2 IEEE 802.1p (class of service [CoS])

● CoS-based egress queuing

● Egress strict-priority queuing

● Egress port-based scheduling: Weighted Round-Robin (WRR)

● Eight hardware queues per port

**High Availability**

● Up to two fabric extenders can work in the Cisco UCS 5100 Series Blade Server Chassis

● Active-active data-plane operation with failover

● Capability to fail over from one fabric extender to another in the event of a failure

● Active-passive management-plane operation

● Support for nonstop management-plane functions; if the active fabric extender fails, the passive fabric extender takes over the chassis management functions

**Management**

● Management of fabric extenders integrated into Cisco UCS Manager (please refer to the Cisco UCS Manager data sheet for more information about management interfaces)

● Capability to manage blade server chassis components such as power supplies, fans, and blades in conjunction with the fabric interconnect

● Firmware levels between the fabric extender and fabric interconnect always synchronized

**Low-Latency, Lossless 10 Gigabit Ethernet Unified Network Fabric**

● PFC (per-priority pause frame support)

● Data Center Bridging Exchange (DCBX) Protocol

● IEEE 802.1Qaz: Bandwidth management

**Industry Standards**

● IEEE 802.1p: CoS prioritization

● IEEE 802.1Q: VLAN tagging

● IEEE 802.3: Ethernet

● IEEE 802.3ad: Link Aggregation Control Protocol (LACP)

● IEEE 802.3ae: 10 Gigabit Ethernet

● SFP+ support

Physical Specifications

**SFP+ Optics**

Cisco UCS products support 10 Gigabit Ethernet SFP+ copper Twinax cables for short distances and SFP+ optics for longer distances. SFP+ has several advantages compared to other 10 Gigabit Ethernet connectivity options, including:

● Small 10 Gigabit Ethernet form factor

● Optical interoperability with XENPAK, X2, and 10 Gigabit Small Form-Factor Pluggable (XFP) interface types

● Low power consumption

● Hot-swappable device

**Environment**

● Physical (height x width x depth): 7.64 x 1.36 x 7.2 in

● Operating temperature: 32 to 104°F (0 to 40°C)

● Nonoperating temperature: -40 to 158°F (-40 to 70°C)

● Humidity: 5 to 95% (noncondensing)

● Altitude: 0 to 10,000 ft (0 to 3000m)

**Weight**

● 2.5 lb (1.134 kg); Weight similar for Cisco UCS 2208XP and 2204XP IOMs

Regulatory Standards Compliance: Safety and EMC

Table 3 summarizes Cisco UCS 2200 Series regulatory compliance.

**Table 3. **Regulatory Standards Compliance: Safety and EMC

Specification |  Description  
---|---  
Regulatory compliance |  Products should comply with CE Markings according to directives 2004/108/EC and 2006/95/EC  
Safety |  ● UL 60950-1  ● CAN/CSA-C22.2 No. 60950-1  ● EN 60950-1  ● IEC 60950-1  ● AS/NZS 60950-1  ● GB4943   
EMC: Emissions |  ● 47CFR Part 15 (CFR 47) Class A  ● AS/NZS CISPR22 Class A  ● CISPR22 Class A  ● EN55022 Class A  ● ICES003 Class A  ● VCCI Class A  ● EN61000-3-2  ● EN61000-3-3  ● KN22 Class A  ● CNS13438 Class A   
EMC: Immunity |  ● EN50082-1  ● EN61000-6-1  ● EN55024  ● CISPR24  ● EN300386  ● KN 61000-4 series   
RoHS |  The product is RoHS 5-compliant with exceptions for leaded ball grid array (BGA) balls and lead press-fit connectors  
  
Warranty Information

Find warranty information at Cisco.com on the [Product Warranties](//www.cisco.com/en/US/products/prod_warranties_listing.html) page.

Cisco Unified Computing Services

Using a unified view of data center resources, Cisco and our industry-leading partners deliver services that accelerate your transition to a unified computing environment. Cisco Unified Computing Services helps you quickly deploy your data center resources and optimize ongoing operations to better meet your business needs. For more information about these and other Cisco Data Center Services, visit [http://www.cisco.com/go/dcservices](//www.cisco.com/go/dcservices).

For More Information

For more information about the Cisco UCS 2200 Series Fabric Extenders, visit [http://www.cisco.com/en/US/products/ps10278/index.html](//www.cisco.com/en/US/products/ps10278/index.html) or contact your local Cisco representative.

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
