# Intersight Appliance PVA Whats New

| | |
|---|---|
| **URL Title** | Intersight Appliance PVA Whats New |
| **URL** | https://intersight.com/help/appliance/whats_new/private_appliance/ |
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260626102158280/docs/onprem/data/articles/private_appliance/new_2026/en/index.html |
| **HTML Title** | What's New in Cisco Intersight |
| **Source file** | `ucs-docs-raw/html/intersight-appliance_whats_new_private_appliance.html` |
| **File type** | HTML |
| **Fetched on** | 2026-07-02 13:04:32 |

---

# What's New in Cisco Intersight

## June 25, 2026 – Appliance Software Release Version: 1.1.7-0

  * **When upgrading to this software release, ensure that your appliance is running on software release version 1.1.4-0 or higher.**

**If your appliance is running on a software release version prior to 1.1.4-0, first upgrade to software release version 1.1.4-0 or higher, before upgrading to 1.1.7-0.**

  * Enhancements to the Intersight Managed Mode:

  * Added support for NVIDIA OEM BlueField-3 B3220 Data Processing Unit (DPU) 2x200G QSFP112, Crypto Disabled (UCSC-P-N3220) on Cisco UCS C245 M8, C240 M8, and C240 M7 servers.

  * Added support for NVIDIA BlueField-3 B3220L SuperNIC 2x200G QSFP112, PCIe Gen5.0 x16, Crypto Disabled (UCSC-P-N3220L) on Cisco UCS C225 M8, C245 M8, C220 M8, C240 M8, and C240 M7 servers.

  * Added support for NVIDIA Crypto B3220 Data Processing Unit (DPU) (UCSC-P-NC3220) on Cisco UCS C245 and C240 M8 servers.

  * Added support for 30 TB E3.S TLC Micron 9550 drive on Cisco UCS C240, C220, X215c, and X210c M8 servers.

  * Added support for E3.S FIPS (Kioxia CM-7) on Cisco UCS C240, C220, X215c, and X210c M8 servers.

For more information, refer to [Supported Systems](/help/supported_systems/Intersight_Managed_Mode).

  * Added support for claiming Unified Edge devices in Intersight Virtual Appliance using a claim token. This method supports environments where the appliance cannot initiate a direct connection to the target, but the target can connect to the appliance. This feature simplifies device onboarding in restricted network environments, such as distributed edge sites. For more information, refer to [Target Claim for Cisco Unified Edge Using Tokens](/help/appliance/getting_started/claim_targets#target_claim_for_cisco_unified_edge_using_tokens).

  * Added support for selecting an uploaded certificate while configuring webhooks in Intersight Virtual Appliance. This enhancement accommodates scenarios where the receiving webhook server utilizes a self-signed certificate or a certificate signed by a private certificate authority. For more information, refer to [Configuring Webhooks](/help/appliance/settings#configuring_webhooks).

  * Intersight Virtual Appliance now provides consistent, structured audit logs for maintenance and admin read-only shells, capturing the terminal, user, remote IP, and command executed in a single line. Additionally, all commands from the admin read-only shell are now forwarded to configured remote syslog servers. For more information, refer to [Configuring Syslog](/help/appliance/settings#configuring_syslog).

  * Intersight Virtual Appliance now supports high availability and a metrics node when deployed on KVM Hypervisor. For more information, refer to [Installing Cisco Intersight Virtual Appliance and Intersight Assist on KVM Hypervisor](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide/m_installation.html#Cisco_Task_in_List_GUI.dita_bb0eaad2-db9a-4b07-9bd3-7efbe5f8b11a).

  * Added support for a medium or a large metrics node in combination with a small management node. For more information, refer to [Supported Configuration Limits for Intersight Virtual Appliance](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide/m_appliance_overview.html#reference_d1b_nhj_sjb).

  * Added support in Intersight Virtual Appliance for initiating the local admin password reset from the hypervisor console without contacting Cisco TAC. The reset process generates a temporary password, which facilitates updating the admin password for both the web UI and SSH access within the appliance UI. For more information, refer to [Resetting the Password for the Local Admin User](/help/appliance/settings#resetting_the_password_for_the_local_admin_user).

  * Intersight Virtual Appliance now supports local backups without requiring a remote file server. After the local backup completion, the browser provides the backup file for download, and the restore workflow accepts backup file uploads from a local machine. For more information, refer to [Creating a Backup](/help/appliance/settings#creating_a_backup).

  * Enhanced LDAP functionality in Intersight Virtual Appliance by adding customizable user search attributes and an optional LDAP filter for advanced user searches. Supported attributes will include standard values such as uid, mail, and sAMAccountName, as well as custom attributes from the LDAP directory. For more information, refer to [Configuring LDAP/AD](/help/appliance/settings#configuring_ldap/ad).

  * Added support in Intersight Virtual Appliance for configuring the maximum number of days a local user password remains valid in Intersight Virtual Appliance. For more information, refer to [Configuring Password Policy for Local Users](/help/appliance/settings#configuring_password_policy_for_local_users).

  * Added support for a 90-day evaluation license. A one-time trial can be started during initial setup or from the Licensing page, with access to Advantage tier features available without immediate license registration. For more information, refer to [Starting a Trial License](/help/appliance/getting_started/licensing_requirements/lic_intro#starting_a_trial_license).

  * Added support for custom metric alarms with threshold definition. You can set thresholds for metrics like Host Power and Energy and Network Interface to trigger alarms when conditions are met. For more information, refer to [Metrics Alarm Rules and Threshold Definitions](/help/configure/rules/metric_alarms_rules).

  * Added support for HTTP, SSH, Ansible, and PowerShell endpoint targets in resource groups. Administrators can now group non-server targets (such as IPAM) into resource groups, enabling simplified management, assignment, and sharing of access across organizations. For more information, refer to [Target Claim for HTTP, SSH, Ansible, and PowerShell Endpoint](/help/getting_started/claim_targets#target_claim_for_http_ssh_ansible_and_powershell_endpoint).

  * Enhanced IPv6 address assignment to include the Stateless Address Auto-Configuration (SLAAC) support in Intersight Managed Mode. For more information, refer to [Fabric Interconnects Through Console](/help/resources/cisco_intersight_managed_mode_configuration#configuring_fabric_interconnects_through_console) and [Device Console](/help/device_console#device_console_common_cli_commands).

  * Enhanced Email Notifications to configure up to 20 email addresses for each notification rule. For more information, refer to [Email Notifications](/help/appliance/settings#configuring_smtp_settings_for_email_notifications).

  * Added the ability to directly configure KMIP servers with IPv6 addresses, in addition to existing policy-level IPv6 support within the Drive Security Policy in Intersight Managed Mode and Intersight Standalone Mode. This enhancement enables you to specify IPv6 addresses for KMIP servers, ensuring access to a significantly expanded available address space. For more information, refer to [Configuring KMIP Server Access Using a Drive Security Policy](/help/resources/Secure_Self_Encrypting_Drives#configuring_kmip_server_access_using_a_drive_security_policy).

  * Added support for read-only users to launch the Command Line Interface (CLI) for Fabric Interconnects in Intersight Managed Mode domains directly from Cisco Intersight. For more information, refer to [Fabric Interconnect Actions](/help/operate/fabric_interconnects#fabric_interconnect_actions).

  * Starting with Infrastructure Firmware release 6.0(2), added support for viewing traffic rates when executing the `show interface vethernet` and `show interface vfc` Fabric Interconnect Device Console CLI commands. This enhancement simplifies network troubleshooting.

  * Added the ability to assign a Fabric Interconnect pair to a domain profile from the Domain Profile Actions menu and a chassis to a chassis profile from the Chassis Profile Actions menu. This feature enables you to add or update a domain assignment or chassis assignment before deploying the profile. For more information, refer to _UCS Domain Profile Details_ section in [Domain Profile](/help/configure/fabric_interconnects#domain_profile) and _UCS Chassis Profile Details_ section in [Chassis Profile](/help/configure/chassis#chassis_profiles).

  * Enhanced the Device Console for Unified Edge servers

  * Added support for file and directory management for the Edge Chassis Management Controller (eCMC). For more information, refer to [Device Console](/help/device_console#inventory_\(unified_edge\)).

  * Added support for multiple languages (Japanese, Korean, and Simplified Chinese). For more information, refer to [Device Console](/help/device_console#user_interface_of_device_console_\(unified_edge\)).

  * Added support for configuring account lockout settings. For more information, refer to [Administration (Unified Edge)](/help/device_console#administration_\(unified_edge\)).

  * Added support for Return Material Authorization (RMA) for sleds and eCMC modules managed as a fleet, enabling a single component to be seamlessly detached, replaced, and reattached—all in a controlled and automated manner. This process ensures that the behavior and operation of the remaining fleet components are unaffected and consistent during and after replacement, with minimal intervention. For more information, refer to [RMA in Fleet](/help/resources/about_fm#rma_in_fleet).

  * Added support for workload instance health monitoring and alarms. This enhancement enables you to monitor the health of instances and take prompt action to remediate any identified issues. For more information, refer to [Instances Table View](/help/configure/Workloads#instances_table_view).

  * Added the ability to edit the name of the workload definitions and deployments. For more information, refer to [Rename Workload Definition](/help/configure/Workloads#rename_workload_definition) and [Rename Workload Deployment](/help/configure/Workloads#rename_workload_deployment).

  * Added support for automatic deployment of a server profile when it is assigned to a server for the first time after creation. This enhancement reduces the number of steps required to deploy a profile. For more information, refer to [Initial Automatic Deployment of Server Profiles](/help/resources/cisco_intersight_managed_mode_configuration#initial_automatic_deployment_of_server_profiles).

  * Added support for automated firmware synchronization of eCMCs in Cisco Unified Edge, enabling seamless upgrades and recovery scenarios. This ensures both eCMCs in a chassis run consistent firmware versions, improving reliability and reducing manual intervention. For more information, refer to [eCMC Firmware Synchronization](/help/resources/fw_mgmnt_ue#ecmc_firmware_synchronization).

  * Added the ability to disable MAC address for a specific VLAN. This feature allows the Fabric Interconnect (FI), when operating in switching mode, to forward the RSPAN traffic to a VM located behind the FI. For more information, refer to [Switch Control Policy](/help/resources/domain_policies#switch_control_policy).

  * Added the ability for Unified Edge Administrators to explicitly configure 25 Gigabit Ethernet (25G) on eCMC SFP ports via Port Policy. This enhancement supports higher bandwidth and improves scalability to accommodate future network growth. For more information, refer to [Port Policy](/help/resources/ue_chassis_policies#port_policy).

  * Added detailed fan module information to the Server Inventory for Intersight Managed Mode and Intersight Standalone Mode servers, helping ensure uninterrupted cooling and optimal operating temperatures without requiring system downtime. For more information, refer to [Server Inventory View](/help/operate/servers#server_inventory_view).

  * Added the ability to configure a Priority Flow Control (PFC) watchdog timer that helps prevent data loss caused by network congestion. A faulty Network Interface Card (NIC) or switch can cause a PFC storm by continuously sending pause signals (PFC pause frames) to the network. For more information, refer to [System QoS Policy](/help/resources/domain_policies#system_qos_policy).

  * Added support to display a warning when UEFI Secure Boot mode is configured without enabling Secure Boot. For more information, refer to [Boot Order Policy](/help/resources/server_policies#boot_order_policy).

  * Added support for stronger SNMPv3 AuthPriv authentication using SHA-2 algorithms. For more information, refer to [SNMP Policy](/help/resources/server_policies#snmp_policy).

  * Added support to display a warning message when HTTP option is enabled, alerting that this option uses the unencrypted HTTP protocol, which transmits data in clear text and exposes communications to interception and attacks. For more information, refer to [Virtual Media Policy](/help/resources/server_policies#virtual_media_policy), [Boot Order Policy](/help/resources/server_policies#boot_order_policy), and [Software Repository](/help/system/software_repo).

  * Added support for custom hardware compatibility lists (HCL) for servers to help organizations meet internal hardware compliance needs. You can now create baselines using criteria such as server model, firmware version, OS vendor and version, and adapter details. Compare server inventory against these custom baselines to ensure consistent hardware standards across your environment. For more information, refer to [Custom HCL](/help/configure/custom_hcl).

  * Added support for iSCSI boot with IPv4 (M5 and later) and IPv6 (M6 and later) for Intersight Standalone Mode servers. For more information, refer to [Boot Order Policy](/help/resources/server_policies#boot_order_policy).

  * Support for MTU sizes up to 9158 bytes per vNIC is now available on Cisco UCS Virtual Interface Card (VIC) 15000 series adapters with supported firmware (5.4.2.15). For more information, refer to [Ethernet QoS Policy](/help/resources/server_policies#ethernet_qos_policy).

  * Added support for 16,384 LUNs per vHBA configured as a Fibre Channel (FC) initiator when used with supported Linux operating systems and the 6.0(2) server firmware version. For more information, refer to [Fibre Channel Adapter Policy](/help/resources/server_policies#fibre_channel_adapter_policy).

  * Ability to provide server profile migration between Cisco UCS servers while maintaining the ESXi-generated recovery key, which binds the operating system to specific hardware through the Trusted Platform Module (TPM). For more information, refer to [Boot Order Policy](/help/resources/server_policies#boot_order_policy).

  * Added enhanced password security for Fabric Interconnect users. Complex password requirements, which were previously optional, are now enforced when creating new user accounts or updating existing passwords. For more information, refer to [Fabric Interconnect Password Guidelines](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Intersight_Managed_Mode_Configuration_Guide/b_intersight_managed_mode_guide_chapter_00a.html#Cisco_Reference.dita_c6555b5b-d467-4ce5-90a7-558ac17ffd19).

  * Added support for granular alarm suppression rules, allowing you to filter and hide specific alarms for enhanced control over alarm visibility in the Intersight UI and email notifications. For more information, refer to [Granular Alarm Suppression Rules](/help/configure/rules/suppression_rules).

  * Cisco Intersight Add-on for Splunk version 3.1.1 is now available on the Splunkbase marketplace. For more information, refer to [Intersight Add-on for Splunk](/help/resources#intersight_add-on_for_splunk).

  * Added support for the Cisco Intersight Plugin for Red Hat OpenShift, integrating Intersight capabilities directly into the Red Hat OpenShift web console. This enables OpenShift administrators to monitor server health, metrics, security advisories, Hardware Compatibility List (HCL) status, and contract information, while providing direct KVM access to prevent production outages through proactive alerts. For more information, refer to [Cisco Intersight Plugin for Red Hat OpenShift](/help/resources/plugin_openshift).


## June 10, 2026 – Appliance Intelligence Bundle Release

  * Added End of Life Advisory _EOL15913: End-of-Sale and End-of-Life Announcement for the Cisco UCS C885A M8 Rack Servers with AMD MI300X and NVIDIA HGX H200 GPUs_. For more information, refer to [UCS Product Family End of Life Advisories](/help/resources/cisco_security_advisoriesresources/cisco_end_of_life_advisories#ucs_product_family_end_of_life_advisories).

  * Added support for Field Notice _FN74391: When Adding Large Numbers of VLANs to a vNIC, Redundant Fabric Interconnects May Both Restart - Software Upgrade Recommended_. For more information, refer to [Cisco Field Notices](/help/resources/cisco_field_notices).


## April 20, 2026 – Appliance Patch Release Version: 1.1.6-1

  * **When upgrading to this patch release, ensure that your appliance is running major release version 1.1.6-0. For more information, refer to[Intersight Virtual Appliance Patch Releases](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide/m_updating_the_intersight_virtual_appliance_software.html#appliance-versioning-scheme).**

This patch release includes bug fix for CSCwt69190. For more information, refer to [Bugs](/help/appliance/bugs).


## April 16, 2026 – Appliance Intelligence Bundle Release

  * Added support for the following Security Advisories:

  * _CVE-2026-20087,CVE-2026-20088,CVE-2026-20089, CVE-2026-20090: Cisco Integrated Management Controller Cross-Site Scripting Vulnerabilities._

  * _CVE-2026-20093: Cisco Integrated Management Controller Authentication Bypass Vulnerability_.

  * _CVE-2026-20094: Cisco Integrated Management Controller Command Injection and Remote Code Execution Vulnerabilities_.

For more information, refer to [Cisco Security Advisories](/help/resources/cisco_security_advisories).

  * Added updates to the Hardware Compatibility List (HCL). For more information, refer to [Compliance with Hardware Compatibility List](/help/resources#compliance_with_hardware_compatibility_list_\(hcl\)).


## March 19, 2026 – Appliance Software Release Version: 1.1.6-0

  * **When upgrading to this software release, ensure that your appliance is running on software release version 1.1.3-0 or higher.**

**If your appliance is running on a software release version prior to 1.1.3-0, first upgrade to software release version 1.1.3-0 or higher, before upgrading to 1.1.6-0.**

  * Added support for Cisco Unified Edge in Intersight Managed Mode. Unified Edge is a modular platform that combines compute, networking, storage, and security in a single chassis. For more information, refer to [Cisco Unified Edge](/help/operate/unified_edge).

  * Added support for managing Cisco Unified Edge as a fleet—a logical grouping of multiple servers, devices, or clusters managed collectively—which enables centralized automation and consistent configuration across all resources, resulting in simplified and scalable administration. For more information, refer to [Fleet Management](/help/resources/about_fm).

  * Added support for location feature that allows adding geolocations to resources for improved organization and filtering. You can add locations using either a physical address or GPS coordinates. For more information, refer to [Locations](/help/system/locations).

  * Added support for applying and propagating Path Tags across Fabric Interconnects, Unified Edge, Chassis, and Standalone Servers. Propagation depends on the hierarchy level and object type—Unified Edge, Fabric Interconnect, Chassis, and Standalone Servers, all support downward propagation to their related components. For more information, refer to [Tags](/help/system/tags).

  * Added the ability to perform diagnostics on one or more servers and their components, enabling identification of server issues, detection of faulty components, and troubleshooting of basic problems. This feature is supported on Cisco UCS M6 and later servers in both Intersight Managed Mode and Intersight Standalone Mode. For more information, refer to [Performing Server Diagnostics](/help/resources/performing_server_diagnostics) and [Server Actions](/help/operate/servers#server_actions).

  * Added the ability to create custom privilege sets. This feature allows administrators to manage user privileges, ensuring that users have access only to the resources and actions necessary for their roles. Granting only the necessary privilege to each user helps improve security, reduce risk, and maintain compliance. For more information, refer to [Privilege Sets](/help/resources/Privilege_Sets).

  * Added support for email notifications on security advisories, field notices, and end-of-life (EOL) updates. Administrators can now customize alerts by severity or key milestones, making it easier to stay informed without manually checking Advisory pages. For more information, refer to [Create a Notification Rule](/help/settings#configuring_smtp_settings_for_email_notifications).

  * Added support for 50 Gbps speed on the unified Ethernet ports of the Cisco UCS 6664 Fabric Interconnect, enabling greater bandwidth and improved connectivity. For more information, refer to [Port Policy](/help/resources/domain_policies#port_policy).

  * Added support for Cisco UCS X410c M8 Compute Nodes in Intersight Managed Mode and UCSM Managed Mode. For more information, refer to [Supported Systems](/help/supported_systems/overview).

  * Added support for Cisco UCS 6652 Fabric Interconnects in Intersight Managed Mode and UCSM Managed Mode. For more information, refer to [Supported Systems](/help/supported_systems/overview).

  * Added support for 4*32G LR Optics on Cisco UCS 6536 Fabric Interconnect and UCSX-Direct Fabric Interconnect in Intersight Managed Mode. This enhancement enables Fibre Channel connectivity beyond 150 meters, providing extended reach for SAN environments.

  * Added support for E3.S FIPS drives on Cisco UCS M8 servers in IMM, providing enhanced compliance and security.

  * Added support for the Cisco UCS 2408 I/O Module with the Cisco UCS 6664 FI when used with the Cisco UCS 5108 chassis in Intersight Managed Mode (IMM). For more information, refer to [Supported Systems](/help/supported_systems/overview).

  * Added support for the Cisco UCS X580p PCIe Node and Cisco UCS X9516 X-Fabric Module on Cisco UCS X210c M7 servers. For more information, refer to [Supported Systems](/help/supported_systems/Intersight_Managed_Mode).

  * Added support for NetFlow policy on Cisco UCS 6600 Series, 6500 Series, 6400 Series, and Cisco UCS X-Series Direct Fabric Interconnects. This feature enables you to collect and analyze IP traffic metadata to monitor bandwidth, detect security anomalies, and troubleshoot performance issues.

  * Added the ability to view real-time visual representation of appliance health status, including CPU, memory, and disk utilization. This feature enables proactive monitoring of performance trends, identification of potential capacity limitations, and optimization of resource allocation. For more information, refer to [Intersight Virtual Appliance Monitoring](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide/m_settings_dashboard.html#reference_rzp_xp5_kgb).

  * Added support for deploying Intersight Virtual Appliance in a small configuration with 8 vCPUs, 32 GiB memory, and 600 GB storage. For more information, refer to [VM Resource Requirements for Intersight Virtual Appliance Deployments](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide/m_appliance_overview.html#Cisco_Reference.dita_a6ea1ddc-e212-4367-9579-e9320b64f1b5).

  * Added support for deploying Intersight Assist in a tiny configuration with 4 vCPUs and 8 GiB memory. For more information, refer to [VM Resource Requirements for Intersight Assist](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide/m_appliance_overview.html#Cisco_Concept.dita_7663b259-3058-49e2-b27c-0282007dda2a_new).

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

For more information, refer to [Cisco Security Advisories](/help/resources/cisco_security_advisories).

  * Added updates to the Hardware Compatibility List (HCL). For more information, refer to [Compliance with Hardware Compatibility List](/help/resources#compliance_with_hardware_compatibility_list_\(hcl\)).


## February 25, 2026 – Appliance Intelligence Bundle Release

  * Added Field Notice _FN74355: Cisco UCS M7 or Cisco HCI M7 Host May Lock Up Due to Error-Correcting Code During Runtime_ for select UCS models. For more information, refer to [Cisco Field Notices](/help/resources/cisco_field_notices).

  * Added updates to the Hardware Compatibility List (HCL). For more information, refer to [Compliance with Hardware Compatibility List](/help/resources#compliance_with_hardware_compatibility_list_\(hcl\)).


## February 5, 2026 – Appliance Patch Release Version: 1.1.5-1

  * **When upgrading to this patch release, ensure that your appliance is running major release version 1.1.5-0. For more information, refer to[Intersight Virtual Appliance Patch Releases](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide/m_updating_the_intersight_virtual_appliance_software.html#appliance-versioning-scheme).**

This patch release includes bug fixes. For more information, refer to [Bugs](/help/appliance/bugs).

  * Added support for the Cisco UCS X580p PCIe Node and Cisco UCS X9516 X-Fabric Module in Intersight Managed Mode. For more information, refer to [Supported Hardware for Intersight Managed Mode](/help/supported_systems/Intersight_Managed_Mode) and [Chassis Inventory View](/help/operate/chassis#chassis_inventory_view).

  * Added support for the Cisco UCS X580p PCIe Node and Cisco UCS X9516 X-Fabric Module on UCS X-Series Direct (9108-100G) Fabric Interconnects. For more information, refer to [PCIe Connectivity Policy](/help/resources/server_policies#pcie_connectivity_policy).

  * Added support for upgrading Cisco UCS X9508 chassis firmware in Intersight Managed Mode (IMM) through the Intersight UI. The chassis firmware upgrade also includes firmware upgrades for Cisco UCS X9516 X-Fabric Modules (XFMs) and Power Supply Units (PSUs). For more information, refer to [Upgrading Chassis Firmware in IMM](/help/resources/Upgrading_Chassis_Firmware).

  * Added the ability to map individual IP blocks within an IP pool to specific **Organizations** or **Resource Groups**. This mapping is achieved using an **ID Mapping** policy, enabling granular control over IP address allocation based on the organization or resource group where the server is deployed, while also ensuring consistent pool usage across organizations and resource groups. For more information, refer to [Configuring Pools](/help/resources/cisco_intersight_managed_mode_configuration#configuring_pools).

  * Added support for creating IPMI user accounts in the Local User Policy. This allows non-admin users to run IPMI API commands on the server, such as performing OS installations without administrator access. For more information, refer to _Creating a Local User Policy_ section in [Supported UCS Server Policies](/help/resources/cisco_intersight_managed_mode_configuration#supported_ucs_server_policies).

  * Added support for Code Generator to record the Intersight UI actions to instantly generate corresponding PowerShell and Python SDK scripts. This feature helps you accelerate API-based automation for Intersight tasks. For more information, refer to [Cisco Intersight Code Generator](/help/resources/cisco_intersight_code_generator).

  * Increased policy scalability, performance and reliability across server profiles for all supported servers in both Intersight Managed and Standalone modes. Also, a new server profile status has been added. For more information, refer to _Server Profile List View_ section in [Server Profiles](/help/configure/servers#server_profiles).

  * Cisco UCS Tools versions 2.0.2-1OEM and 2.1.2-1OEM support UCS C845A and UCS C885A M8 servers and includes enhancements to security and resource management. These releases are available for download on [Cisco Software Download site](https://software.cisco.com/download/home/286305108/type). For more information, refer to [Cisco UCS Tools](/help/appliance/resources/cisco_ucs_tools).

  * Added support for GPU and environment metrics collection for Cisco UCS X580p PCIe Nodes. This feature is available for Cisco UCS X580p PCIe Nodes in an Intersight Managed Mode (IMM) domain. For more information, refer to [Supported Devices](/help/monitoring/supported_devices_monitoring) and [Supported Metrics](/help/monitoring/monitoring_supported_metric).

  * Added support for metrics collection on Intersight Standalone Mode (ISM) servers. This feature is available for Cisco UCS C-Series M7 and M8 servers. For more information, refer to [Supported Devices](/help/monitoring/supported_devices_monitoring).

  * Added support for metrics collection for physical VIC adapter cards, including network traffic and error metrics, and PFC Wait time metrics. This support is available for UCS C-Series and UCS X-Series servers that are part of an Intersight Managed Mode (IMM) domain. For more information, refer to [Supported Devices](/help/monitoring/supported_devices_monitoring) and [Supported Metrics](/help/monitoring/monitoring_supported_metric).

  * Added support for Nutanix Prism Central in the Intersight Virtualization view, along with a new overview that summarizes inventory across both VMware vCenter and Prism Central. For more information, refer to [Intersight Virtualization](/help/operate/virtualization#intersight_virtualization).

  * Added the following support to the Cisco Compute Hyperconverged with Nutanix solution:

  * **Expanding Cisco Compute Hyperconverged node cluster with Compute-Only node** \- Cisco Compute-Only node solution enables you to expand the compute resources of Cisco HCI cluster running Nutanix by adding UCS certified servers without additional storage. For more information, refer to [Expand an Existing Cluster](/help/configure/nutanix/hci_nutanix#expand_an_existing_cluster).

  * Nutanix Compute-only cluster with Cisco UCS Servers connected to Pure Storage FlashArray solution delivers a disaggregated infrastructure architecture that enables independent scaling of compute and storage resources. For more information, refer to [Deploying Nutanix Compute-Only Cluster on Cisco UCS Servers](/help/configure/nutanix/compute_nutanix#deploying_nutanix_compute-only_cluster_on_cisco_ucs_servers).

  * Cluster deployment with multiple vNIC pairs for IMM clusters. This enhances network configuration flexibility with L2 network segmentation, dedicated network segment (for example, backup traffic), Traffic type segregation, and QoS. For more information, refer to [Foundation Central Support for Multiple vNICs](/help/configure/nutanix/hci_nutanix#foundation_central_support_for_multiple_vnics).

  * Intel M8 Large Form Factor (LFF) servers and E3.S drives for AMD M8 X215c modular servers. For more information, refer to [Supported Hardware Platforms](/help/configure/nutanix/hci_nutanix#supported_hardware_platforms).

  * Added the ability to monitor and track user activity on Cisco UCS Fabric Interconnects (6400, 6500, and 6600 series). The AuditD policy for Fabric Interconnect provides detailed logging of user activities, configuration changes, and operational commands within Unified Computing System (UCS) environments. For more information, refer to the _Creating an AuditD Policy_ section in [Configuring UCS Domain Policies](/help/resources/cisco_intersight_managed_mode_configuration#configuring_ucs_domain_policies).

