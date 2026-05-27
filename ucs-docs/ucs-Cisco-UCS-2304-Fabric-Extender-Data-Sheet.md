# Cisco UCS 2304 Fabric Extender

| | |
|---|---|
| **URL Title** | Cisco UCS 2304 Fabric Extender |
| **URL** | https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/datasheet-c78-675243.html |
| **Long URL** |  |
| **HTML Title** | Cisco UCS 2304 Fabric Extender Data Sheet |
| **Source file** | `ucs-docs-raw/html/datasheet-c78-675243.html` |
| **File type** | HTML |
| **Fetched on** | 2026-05-27 11:00:33 |

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
