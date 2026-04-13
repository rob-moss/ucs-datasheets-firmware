# Intersight Appliance PVA Whats New

| | |
|---|---|
| **URL Title** | Intersight Appliance PVA Whats New |
| **URL** | https://intersight.com/help/appliance/whats_new/private_appliance/ |
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260402103337138/docs/onprem/data/articles/private_appliance/new_2026/en/index.html |
| **HTML Title** | What's New in Cisco Intersight |
| **Source file** | `ucs-docs-raw/html/intersight-appliance_whats_new_private_appliance.html` |
| **File type** | HTML |
| **Fetched on** | 2026-04-10 12:48:41 |

---

# What's New in Cisco Intersight

## March 19, 2026 – Appliance Software Release Version: 1.1.6-0

  * **When upgrading to this software release, ensure that your appliance is running on software release version 1.1.3-0 or higher.**

**If your appliance is running on a software release version prior to 1.1.3-0, first upgrade to software release version 1.1.3-0 or higher, before upgrading to 1.1.6-0.**

  * Added support for Cisco Unified Edge in Intersight Managed Mode. Unified Edge is a modular platform that combines compute, networking, storage, and security in a single chassis. For more information, see [Cisco Unified Edge](/help/operate/unified_edge).

  * Added support for managing Cisco Unified Edge as a fleet—a logical grouping of multiple servers, devices, or clusters managed collectively—which enables centralized automation and consistent configuration across all resources, resulting in simplified and scalable administration. For more information, see [Fleet Management](/help/resources/about_fm).

  * Added support for location feature that allows adding geolocations to resources for improved organization and filtering. You can add locations using either a physical address or GPS coordinates. For more information, see [Locations](/help/system/locations).

  * Added support for applying and propagating Path Tags across Fabric Interconnects, Unified Edge, Chassis, and Standalone Servers. Propagation depends on the hierarchy level and object type—Unified Edge, Fabric Interconnect, Chassis, and Standalone Servers, all support downward propagation to their related components. For more information, see [Tags](/help/system/tags).

  * Added the ability to perform diagnostics on one or more servers and their components, enabling identification of server issues, detection of faulty components, and troubleshooting of basic problems. This feature is supported on Cisco UCS M6 and later servers in both Intersight Managed Mode and Intersight Standalone Mode. For more information, see [Performing Server Diagnostics](/help/resources/performing_server_diagnostics) and [Server Actions](/help/operate/servers#server_actions).

  * Added the ability to create custom privilege sets. This feature allows administrators to manage user privileges, ensuring that users have access only to the resources and actions necessary for their roles. Granting only the necessary privilege to each user helps improve security, reduce risk, and maintain compliance. For more information, see [Privilege Sets](/help/resources/Privilege_Sets).

  * Added support for email notifications on security advisories, field notices, and end-of-life (EOL) updates. Administrators can now customize alerts by severity or key milestones, making it easier to stay informed without manually checking Advisory pages. For more information, see [Create a Notification Rule](/help/settings#configuring_smtp_settings_for_email_notifications).

  * Added support for 50 Gbps speed on the unified Ethernet ports of the Cisco UCS 6664 Fabric Interconnect, enabling greater bandwidth and improved connectivity. For more information, see [Port Policy](/help/resources/domain_policies#port_policy).

  * Added support for Cisco UCS X410c M8 Compute Nodes in Intersight Managed Mode and UCSM Managed Mode. For more information, see [Supported Systems](/help/supported_systems).

  * Added support for Cisco UCS 6652 Fabric Interconnects in Intersight Managed Mode and UCSM Managed Mode. For more information, see [Supported Systems](/help/supported_systems).

  * Added support for 4*32G LR Optics on Cisco UCS 6536 Fabric Interconnect and UCSX-Direct Fabric Interconnect in Intersight Managed Mode. This enhancement enables Fibre Channel connectivity beyond 150 meters, providing extended reach for SAN environments.

  * Added support for E3.S FIPS drives on Cisco UCS M8 servers in IMM, providing enhanced compliance and security.

  * Added support for the Cisco UCS 2408 I/O Module with the Cisco UCS 6664 FI when used with the Cisco UCS 5108 chassis in Intersight Managed Mode (IMM). For more information, see [Supported Systems](/help/supported_systems).

  * Added support for NetFlow policy on Cisco UCS 6600 Series, 6500 Series, 6400 Series, and Cisco UCS X-Series Direct Fabric Interconnects. This feature enables you to collect and analyze IP traffic metadata to monitor bandwidth, detect security anomalies, and troubleshoot performance issues.

  * Added the ability to view real-time visual representation of appliance health status, including CPU, memory, and disk utilization. This feature enables proactive monitoring of performance trends, identification of potential capacity limitations, and optimization of resource allocation. For more information, see [Intersight Virtual Appliance Monitoring](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide/m_settings_dashboard.html#reference_rzp_xp5_kgb).

  * Added support for deploying Intersight Virtual Appliance in a small configuration with 8 vCPUs, 32 GiB memory, and 600 GB storage. For more information, see [VM Resource Requirements for Intersight Virtual Appliance Deployments](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide/m_appliance_overview.html#Cisco_Reference.dita_a6ea1ddc-e212-4367-9579-e9320b64f1b5).

  * Added support for deploying Intersight Assist in a tiny configuration with 4 vCPUs and 8 GiB memory. For more information, see [VM Resource Requirements for Intersight Assist](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide/m_appliance_overview.html#Cisco_Concept.dita_7663b259-3058-49e2-b27c-0282007dda2a_new).

  * The following API specifications, SDKs, Terraform provider, and PowerShell modules are applicable to this Private Appliance release.

Appliance Version| API Spec Version| Python SDK| Terraform Provider| PowerShell Module  
---|---|---|---|---  
1.1.6| 1.0.11-20260320211357036| [intersight · PyPI 1.0.11.2026030507](https://pypi.org/project/intersight/)| [1.0.77](https://registry.terraform.io/providers/CiscoDevNet/intersight/latest)| [Intersight.PowerShell 1.0.11.2026022006](https://www.powershellgallery.com/packages/Intersight.PowerShell/)  


## March 13, 2026 – Appliance Intelligence Bundle Release

  * Added support for the following Security Advisories:

  * _CVE-2026-20010: Cisco NX-OS Software Link Layer Discovery Protocol Denial of Service Vulnerability_.

  * _CVE-2026-20036: Cisco UCS Manager Software Command Injection Vulnerability_.

  * _CVE-2026-20037: Cisco UCS Manager Software Privilege Escalation Vulnerability_.

  * _CVE-2026-20091: Cisco FXOS and UCS Manager Software Stored Cross-Site Scripting Vulnerability_.

  * _CVE-2026-20099: Cisco FXOS and UCS Manager Software Command Injection Vulnerability_.

For more information, see [Cisco Security Advisories](/help/resources/cisco_security_advisories).

  * Added updates to the Hardware Compatibility List (HCL). For more information, see [Compliance with Hardware Compatibility List](/help/resources#compliance_with_hardware_compatibility_list_\(hcl\)).


## February 25, 2026 – Appliance Intelligence Bundle Release

  * Added Field Notice _FN74355: Cisco UCS M7 or Cisco HCI M7 Host May Lock Up Due to Error-Correcting Code During Runtime_ for select UCS models. For more information, see [Cisco Field Notices](/help/resources/cisco_field_notices).

  * Added updates to the Hardware Compatibility List (HCL). For more information, see [Compliance with Hardware Compatibility List](/help/resources#compliance_with_hardware_compatibility_list_\(hcl\)).


## February 5, 2026 – Appliance Patch Release Version: 1.1.5-1

  * **When upgrading to this patch release, ensure that your appliance is running major release version 1.1.5-0. For more information, see[Intersight Virtual Appliance Patch Releases](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide/m_updating_the_intersight_virtual_appliance_software.html#appliance-versioning-scheme).**

This patch release includes bug fixes. For more information, see [Bugs](/help/appliance/bugs).

  * Added support for the Cisco UCS X580p PCIe Node and Cisco UCS X9516 X-Fabric Module in Intersight Managed Mode. For more information, see [Supported Hardware for Intersight Managed Mode](/help/supported_systems#supported_hardware_for_intersight_managed_mode) and [Chassis Inventory View](/help/operate/chassis#chassis_inventory_view).

  * Added support for the Cisco UCS X580p PCIe Node and Cisco UCS X9516 X-Fabric Module on UCS X-Series Direct (9108-100G) Fabric Interconnects. For more information, see [PCIe Connectivity Policy](/help/resources/server_policies#pcie_connectivity_policy).

  * Added the ability to map individual IP blocks within an IP pool to specific **Organizations** or **Resource Groups**. This mapping is achieved using an **ID Mapping** policy, enabling granular control over IP address allocation based on the organization or resource group where the server is deployed, while also ensuring consistent pool usage across organizations and resource groups. For more information, see [Configuring Pools](/help/resources/cisco_intersight_managed_mode_configuration#configuring_pools).

  * Added support for creating IPMI user accounts in the Local User Policy. This allows non-admin users to run IPMI API commands on the server, such as performing OS installations without administrator access. For more information, see _Creating a Local User Policy_ section in [Supported UCS Server Policies](/help/resources/cisco_intersight_managed_mode_configuration#supported_ucs_server_policies).

  * Added support for Code Generator to record the Intersight UI actions to instantly generate corresponding PowerShell and Python SDK scripts. This feature helps you accelerate API-based automation for Intersight tasks. For more information, see [Cisco Intersight Code Generator](/help/resources/cisco_intersight_code_generator).

  * Increased policy scalability, performance and reliability across server profiles for all supported servers in both Intersight Managed and Standalone modes. Also, a new server profile status has been added. For more information, see _Server Profile List View_ section in [Server Profiles](/help/configure/servers#server_profiles).

  * Cisco UCS Tools versions 2.0.2-1OEM and 2.1.2-1OEM support UCS C845A and UCS C885A M8 servers and includes enhancements to security and resource management. These releases are available for download on [Cisco Software Download site](https://software.cisco.com/download/home/286305108/type). For more information, see [Cisco UCS Tools](/help/appliance/resources/cisco_ucs_tools).

  * Added support for GPU and environment metrics collection for Cisco UCS X580p PCIe Nodes. This feature is available for Cisco UCS X580p PCIe Nodes in an Intersight Managed Mode (IMM) domain. For more information, see [Supported Devices](/help/monitoring/supported_devices_monitoring) and [Supported Metrics](/help/monitoring/monitoring_supported_metric).

  * Added support for metrics collection on Intersight Standalone Mode (ISM) servers. This feature is available for Cisco UCS C-Series M7 and M8 servers. For more information, see [Supported Devices](/help/monitoring/supported_devices_monitoring).

  * Added support for metrics collection for physical VIC adapter cards, including network traffic and error metrics, and PFC Wait time metrics. This support is available for UCS C-Series and UCS X-Series servers that are part of an Intersight Managed Mode (IMM) domain. For more information, see [Supported Devices](/help/monitoring/supported_devices_monitoring) and [Supported Metrics](/help/monitoring/monitoring_supported_metric).

  * Added support for Nutanix Prism Central in the Intersight Virtualization view, along with a new overview that summarizes inventory across both VMware vCenter and Prism Central. For more information, see [Intersight Virtualization](/help/operate/virtualization#intersight_virtualization).

  * Added the following support to the Cisco Compute Hyperconverged with Nutanix solution:

  * **Expanding Cisco Compute Hyperconverged node cluster with Compute-Only node** \- Cisco Compute-Only node solution enables you to expand the compute resources of Cisco HCI cluster running Nutanix by adding UCS certified servers without additional storage. For more information, see [Expand an Existing Cluster](/help/configure/nutanix/hci_nutanix#expand_an_existing_cluster).

  * Nutanix Compute-only cluster with Cisco UCS Servers connected to Pure Storage FlashArray solution delivers a disaggregated infrastructure architecture that enables independent scaling of compute and storage resources. For more information, see [Deploying Nutanix Compute-Only Cluster on Cisco UCS Servers](/help/configure/nutanix/compute_nutanix#deploying_nutanix_compute-only_cluster_on_cisco_ucs_servers).

  * Cluster deployment with multiple vNIC pairs for IMM clusters. This enhances network configuration flexibility with L2 network segmentation, dedicated network segment (for example, backup traffic), Traffic type segregation, and QoS. For more information, see [Foundation Central Support for Multiple vNICs](/help/configure/nutanix/hci_nutanix#foundation_central_support_for_multiple_vnics).

  * Intel M8 Large Form Factor (LFF) servers and E3.S drives for AMD M8 X215c modular servers. For more information, see [Supported Hardware Platforms](/help/configure/nutanix/hci_nutanix#supported_hardware_platforms).

  * Added the ability to monitor and track user activity on Cisco UCS Fabric Interconnects (6400, 6500, and 6600 series). The AuditD policy for Fabric Interconnect provides detailed logging of user activities, configuration changes, and operational commands within Unified Computing System (UCS) environments. For more information, see the _Creating an AuditD Policy_ section in [Configuring UCS Domain Policies](/help/resources/cisco_intersight_managed_mode_configuration#configuring_ucs_domain_policies).

