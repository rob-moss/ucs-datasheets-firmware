# Intersight SaaS Configure Nutanix HCI guide

| | |
|---|---|
| **URL Title** | Intersight SaaS Configure Nutanix HCI guide |
| **URL** | https://intersight.com/help/saas/configure/nutanix/hci_nutanix |
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260316155144543/docs/cloud/data/articles/features/nutanix/hci/configure/en/index.html |
| **HTML Title** | Document |
| **Source file** | `ucs-docs-raw/html/intersight-saas_configure_nutanix_hci_nutanix.html` |
| **File type** | HTML |
| **Fetched on** | 2026-03-19 16:46:51 |

---

Cisco Compute Hyperconverged with Nutanix is a hyperconverged infrastructure (HCI) solution integrating Cisco’s best-in-class Unified Computing System (UCS), datacenter networking, and SaaS Intersight infrastructure management platform with market-leading hyperconverged software from the Nutanix Cloud Platform. This solution supports Nutanix cluster configuration in Intersight for:

  * Cisco HCI X-Series Modular Server with Intelligent Fabric Module (IFM) or Fabric Interconnect Module (X series Direct) in Intersight Managed Mode (IMM).

  * Cisco HCI standalone rack servers in Intersight Standalone Mode (ISM) and Intersight Managed Mode (IMM).

  * A mix of modular servers and rack servers is supported in the same Nutanix cluster, but they must be connected to the same pair of Fabric interconnects. This mix is not supported when using HCI-X Direct.


The Cisco HCI X-Series delivers performance, flexibility, and optimization for deployments in data centers, in the cloud, and at remote sites. This enterprise-class server offers market-leading performance, versatility, and density without compromise for workloads. Up to eight hyperconverged nodes can reside in the 7-Rack-Unit (7RU) Cisco Compute Hyperconverged X9508 Chassis, offering one of the highest densities of compute, I/O, and storage per rack unit in the industry. Cisco Compute Hyperconverged X-Series Direct module simplifies your data center, adapting to the unpredictable needs of modern applications while also providing an edge scaled for remote branch office workloads. It minimizes the IT infrastructure deployed at edge locations to achieve desired business outcomes.

Supported Cisco HCI servers claimed in Intersight can be deployed as a Nutanix cluster with policies and profiles defined in Intersight. The supported HCI servers can be added to an existing UCS-X 9508 chassis. HCI servers can co-exist with non-HCI servers in the same chassis. The co-engineered integration between Nutanix Prism Central and Cisco Intersight enables seamless zero-touch remote deployment of Nutanix clusters with Nutanix AHV or VMware ESXi hypervisors.

All the required policies for node identity, network connectivity, BIOS, boot order, and more are automatically built based on Nutanix and Cisco recommended best practices. The resulting server profile is associated with each HCI server. After gathering the cluster configuration details, Nutanix Foundation Central (FC) orchestrates the end-to-end remote cluster deployment through Cisco Intersight without any manual intervention.

Note:

Nutanix Foundation Central (FC) is a service component of Nutanix Prism Central.

Cisco Compute Hyperconverged with Nutanix software delivers pre-configured Cisco HCI servers that are ready to be deployed as nodes to form Nutanix clusters in a variety of configurations. Each server contains three software layers:

  * UCS server firmware

  * Hypervisor (Nutanix AHV or VMware ESXi)

  * Hyperconverged software (Nutanix AOS)


Cisco Intersight provides integration support with Nutanix Prism Central to deploy Nutanix HCI clusters on Cisco UCS rack mount servers and X-series modular servers. This brings the HCI into remote edge and branch offices (ROBO) with cluster size starting from as low as one node and enterprise data centers for maximum scale. The solution provides maximum flexibility with choice of either a Cisco VIC or an Intel NIC for network connectivity leveraging existing network infrastructure without the need for additional networking gear.

This document covers prerequisites, supported network topologies and post-installation operations to:

  * Deploy Nutanix clusters in Intersight.

  * Expand existing clusters.

  * Upgrade clusters using Nutanix Life Cycle Manager (LCM).

