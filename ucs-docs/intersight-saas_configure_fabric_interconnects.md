# Intersight SaaS Configure Fabric Interconnects guide

| | |
|---|---|
| **URL Title** | Intersight SaaS Configure Fabric Interconnects guide |
| **URL** | https://intersight.com/help/saas/configure/fabric_interconnects |
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260225095216527/docs/cloud/data/articles/features/fabric_interconnects/configure/en/index.html |
| **HTML Title** | Document |
| **Source file** | `ucs-docs-raw/html/intersight-saas_configure_fabric_interconnects.html` |
| **File type** | HTML |
| **Fetched on** | 2026-03-04 12:48:05 |

---

Domain policies in Cisco Intersight allow to configure various parameters for UCS Fabric Interconnects, including port configuration, network control settings, and VLAN and VSAN settings. A domain policy can be assigned to any number of domain profiles to provide a configuration baseline. Domain policies in Cisco Intersight are a new feature, and native to the application. Policy-based configuration with Domain Profiles is a Cisco Intersight Essentials feature, and is supported on Cisco UCS B-Series M5 and M6 servers and Cisco UCS C-Series M5, M6, M7, and M8 servers that are in a UCS Domain.

To launch the Policies Table View, choose Configure > Policies.

The Domain Policy creation wizard in Cisco Intersight has two pages:

* General—The general page allows to select the organization and enter a name for policy. Optionally, include a short description and tag information to help identify the policy. Tags must be in the key:value format. For example, Org:IT or Site: APJ
* Policy Details—The policy details page has properties that are applicable to UCS Domain Policies.

Domain Policies can also be cloned by using the Policy Clone wizard with properties that are similar to the existing policies. The clone policy action is available on both the policies list and detailed views. For more information, see [Cloning a Policy](/help/resources#cloning_a_policy).

You can compare up to five policies of the same type from the Policies List View page to identify configuration differences, maintain consistency, and simplify troubleshooting.

To compare policies, select the checkboxes next to the desired policies, click the ellipsis (…) at the top left of the page, and choose Compare. On the Compare side drawer, only the differences between the selected policies are shown by default. To display all parameters, select All from the Display drop-down menu.

Note:

You can compare a minimum of two and a maximum of five policies of the same type at a time.

The following list describes the domain policies that you can configure in Cisco Intersight.

* Port Policy—Configures the ports and port roles for the Fabric Interconnect. Each Fabric Interconnect has a set of ports in a fixed port module that you can configure. You can enable or disable a port or a port channel.

The port policy is associated with a switch model. The network configuration limits also vary with the switch model.

The maximum number of ports and port channels supported on Cisco UCS 6400 Series and 6500 Series Fabric Interconnects are:

* Ethernet Uplink, Fibre Channel over Ethernet (FCoE) Uplink port channels, and Appliance port channels (combined) — 12
* Ethernet Uplink ports per port channel — 16
* FC uplink port channel — 4
* FCoE Uplink ports per port channel —16
* Ethernet Uplink and FCoE Uplink ports (combined) —31
* Server ports—54 ports for Cisco UCS 6454, 108 ports for Cisco UCS 64108 Fabric Interconnects, and 64 ports for 6664 Fabric Interconnect.

The maximum number of ports and port channels supported for Cisco UCS Fabric Interconnects 9108 100G are:

* Ethernet uplink, Fibre Channel over Ethernet (FCoE) uplink, Ethernet uplink port channels, FCoE uplink port channels, and Appliance port channels (combined) —8
* Ethernet uplink ports per port channel —8
* FC uplink port channel —4
* FC uplink count —8
* FC uplink per SAN port —8
* FCoE Uplink ports per port channel —8
* Ethernet Uplink and FCoE uplink ports (combined) —8
* Ethernet Network Control Policy—Configures the network control settings for appliance ports, appliance port channels, or vNICs.
* Ethernet Network Group Policy—Configures the allowed VLANs and native VLAN for ethernet uplink ports, ethernet uplink port channels, appliance ports, or appliance port channels.

Note:

When Ethernet Network Group Policies are assigned to an ethernet uplink port or ethernet uplink port channel in a Port Policy, the specified Ethernet Network Group Policies across Ethernet Network Group Policies must be either identical to or disjoint from the VLAN sets specified on other uplink interfaces Ensure that the VLANs are defined in the VLAN Policy and that Auto Allow on Uplinks is disabled.

You can add multiple Ethernet Network Group Policies (ENGPs) on ethernet uplink port and ethernet uplink port channels in port policies. For more information, see [Ethernet Network Group Policy](/help/resources/domain_policies#ethernet_network_group_policy).

* VLAN Configuration Policy—Creates a connection to a specific external LAN or to a Private VLAN.
* VSAN Configuration Policy—Partitions the Fibre Channel fabric into one or more zones. Each zone defines the set of Fibre Channel initiators and Fibre Channel targets that can communicate with each other in a VSAN.
* NTP Policy—Enables the NTP service to configure a UCS system that is managed by Cisco Intersight to synchronize the time with an NTP server. You must enable and configure the NTP service by specifying the IP/DNS address of at least one server or a maximum of four servers that function as NTP servers. When you enable the NTP service, Cisco Intersight configures the NTP details on the endpoint. For more information, see [Creating an NTP policy](../../../../../../../../../../help/resources/cisco_intersight_managed_mode_configuration#creating_an_ntp_policy).
* Network Connectivity Policy—Specifies the DNS Domain settings that are used to add or update the resource records on the DNS server from the endpoints, and the DNS server settings for IPv4 and IPv6 on an endpoint.
* System QoS Policy —Implements network traffic prioritization based on the importance of the connected network by assigning system classes for individual vNICs. Intersight uses Data Center Ethernet (DCE) to handle all traffic inside a Cisco UCS domain. This industry standard enhancement to Ethernet divides the bandwidth of the Ethernet pipe into eight virtual lanes. Two virtual lanes are reserved for internal system and management traffic. You can configure quality of service (QoS) for the other six virtual lanes. System classes determine how the DCE bandwidth in these six virtual lanes is allocated across the entire Cisco UCS domain.

Each system class reserves a specific segment of the bandwidth for a specific type of traffic, which provides a level of traffic management, even in an oversubscribed system. For example, you can configure the Fibre Channel Priority system class to determine the percentage of DCE bandwidth allocated to FCoE traffic. The configuration setup validates each input on the system class to prevent duplicate or invalid entries.

The following list describes the system classes that you can configure.

* Platinum, Gold, Silver, and Bronze—A configurable set of system classes that you can include in the QoS policy for a UCS domain profile. Each system class manages one lane of traffic. All properties of these system classes are available for you to assign custom settings and policies.
* Best Effort—A system class that sets the quality of service for the lane reserved for basic Ethernet traffic. Some properties of this system class are preset and cannot be modified. For example, this class has a drop policy that allows it to drop data packets if required. You cannot disable this system class.
* Fibre Channel—A system class that sets the quality of service for the lane reserved for Fibre Channel over Ethernet traffic. Some properties of this system class are preset and cannot be modified. For example, this class has a no-drop policy that ensures it never drops data packets. You cannot disable this system class.
* Multicast Policy—Configures Internet Group Management Protocol (IGMP) snooping and IGMP querier. IGMP Snooping dynamically determines hosts in a VLAN that should be included in multicast transmissions.

You can create, modify, and delete a multicast policy that can be associated to one or more VLANs. When a multicast policy is modified, all VLANs associated with that multicast policy are re-processed to apply the changes. By default, IGMP snooping is enabled and IGMP querier is disabled. On enabling IGMP querier, you can configure the IPv4 addresses for the local and peer IGMP snooping querier interfaces.

* Simple Network Management Protocol (SNMP) Policy—Configures the SNMP settings for sending fault and alert information by SNMP traps from the managed devices. Any existing SNMP Users or SNMP Traps configured previously on the managed devices are removed and replaced with users or traps that you configure in this policy.
* Syslog Policy—Enables to configure the local logging and remote logging (minimum severity) for an endpoint. This policy also provides configuration support to store the syslog messages in the local file and the remote syslog server.
* Switch Control Policy—Enables to configure and manage multiple network operations on the Fabric Interconnects (FI) that include:
* Port Count Optimization—If the VLAN port count optimization is enabled, the Virtual Port (VP) groups are configured on the Fabric Interconnect (FI) and if VLAN port count optimization is disabled, the configured VP groups are removed from the FI.
* MAC Aging Time—Allows to set the MAC aging time for the MAC address table entries. The MAC aging time specifies the time before a MAC entry expires and discards the entry from the MAC address table.
* Link Control Global Settings—Enables configurations of message interval time in seconds and allows to reset the recovery action of an error-disabled port.
* Flow Control Policy—Enables configurations for Priority Flow Control for ports and port channels.
* Link Control Policy—Enables configurations of Link Control administrative state and configuration (normal or aggressive) mode for ports.
* Link Aggregation Policy— Enables to configure Link Aggregation properties. Link Aggregation combines multiple network connections in parallel to increase throughput and to provide redundancy.
* LDAP Policy—Specifies the LDAP configuration settings and preferences for an endpoint. The endpoints support LDAP to store and maintain directory information in a network. The LDAP policy determines configuration settings for LDAP Servers, DNS parameters including options to obtain a domain name used for the DNS SRV request, Binding methods, Search parameters, and Group Authorization preferences. Through an LDAP policy, you can also create multiple LDAP groups and add them to the LDAP server database.
* Certificate Management Policy— Allows you to specify the certificate details for an external certificate and attach the policy to domain profile. Cisco Intersight currently supports Root CA certificates for Fabric Interconnect in Intersight Managed Mode. For more information, see [Certificate Management Policy](/help/resources/server_policies#certificate_management_policy).
* MACsec Policy— Media Access Control Security (MACsec), an IEEE 802.1AE standard, along with the MACsec Key Agreement (MKA) protocol, provide secure communications on Ethernet links. The MKA protocol discovers MACsec peers and negotiates the keys used by MACsec, as defined in IEEE 802.1x-2010. The Advanced Encryption Standard (AES) feature enables secure storage of MACsec keys in NXOS using a master key.

MACsec feature offers the following benefits:

* Provides line-rate encryption capabilities.
* Ensures data confidentiality through strong encryption at Layer 2.
* Provides integrity checking to prevent data modification during transit.
* Provides replay protection.

A MACsec policy configures the cipher suite for data encryption and other related attributes.

For details on creating a MACsec policy, see [MACsec Policy](/help/resources/domain_policies#macsec_policy).