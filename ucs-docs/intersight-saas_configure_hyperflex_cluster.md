# Intersight SaaS Configure HyperFlex Cluster guide

| | |
|---|---|
| **URL Title** | Intersight SaaS Configure HyperFlex Cluster guide |
| **URL** | https://intersight.com/help/saas/configure/hyperflex_cluster |
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260225095216527/docs/cloud/data/articles/features/hyperflex/configure/en/index.html |
| **HTML Title** | Document |
| **Source file** | `ucs-docs-raw/html/intersight-saas_configure_hyperflex_cluster.html` |
| **File type** | HTML |
| **Fetched on** | 2026-03-04 11:11:08 |

---

Cisco Intersight provides an installation wizard to install, configure, and deploy Cisco HyperFlex clusters — HyperFlex Edge, FI-attached, and HyperFlex Datacenter without Fabric Interconnect. The wizard constructs a pre-configuration definition of your cluster called an HyperFlex Cluster Profile. This definition is a logical representation of the HyperFlex nodes in your HyperFlex cluster and includes:

  * Security—credentials for HyperFlex cluster such as controller VM password, Hypervisor username, and password.

  * Configuration—server requirements, firmware, etc.

  * Connectivity—upstream network, virtual network, etc.


HyperFlex Cluster Profiles are built on policies which administrator defined sets of rules and operating characteristics such as the node identity, interfaces, and network connectivity. Every active node in your HyperFlex cluster must be associated with an HyperFlex Cluster Profile.

After gathering the node configuration settings to build the HyperFlex Cluster Profile, the installation wizard will validate and deploy the HyperFlex Cluster Profile in your HyperFlex cluster. You can clone a successfully deployed HyperFlex Cluster Profile, and then use that copy as the basis to create a new cluster. For instructions on cloning HyperFlex cluster profiles, see [Cloning HyperFlex Cluster Profiles](/help/configure/hyperflex_cluster#clone_a_hyperflex_cluster_profile) .

## Non Pre-configured Cisco HyperFlex Systems

Note: Beginning in April 2024, HyperFlex servers are shipped from the factory without VMware ESXi preinstalled. It is imperative that the ESXi hypervisor is installed before starting the HyperFlex Installation. For instructions to manually prepare factory shipped servers for the Cisco HyperFlex install, see [Cisco HyperFlex install, see Cisco HyperFlex Systems Installation Guide for VMware ESXi](https://www.cisco.com/c/en/us/td/docs/hyperconverged_systems/HyperFlex_HX_DataPlatformSoftware/Installation_VMWare_ESXi/5-5/b-hx-install-guide-for-vmware-esxi-5-5/m-hx-server-imaging-factory-shipped-servers.html).