# Intersight SaaS Upgrading Firmware guide

| | |
|---|---|
| **URL Title** | Intersight SaaS Upgrading Firmware guide |
| **URL** | https://intersight.com/help/saas/resources/upgrading_server_firmware_using_firmware_policy |
| **Long URL** |  |
| **HTML Title** | Resources |
| **Source file** | `upgrading_server_firmware_using_firmware_policy` |
| **File type** | HTML |
| **Fetched on** | 2026-04-08 08:43:04 |

---

## Role Based Access Control (RBAC) in Intersight
Cisco Intersight uses Role-Based Access Control (RBAC) and Organizations to provide secure, flexible access management for infrastructure. This section explains how to configure roles, manage privileges, organize resources, and leverage advanced features like guest access, sub-target assignments, and policy integration. The following topics describe how these features support multi-tenancy, granular user management, and streamlined operations:
- [en/RBAC.html](RBAC)
- [en/config_sharing_across_orgs.html](config_sharing_across_orgs)
- [en/Managingrolesandprivileges.html](Managing_Roles_and_Privileges)
- [en/r_privilege_sets.html](Privilege_Sets)
- [en/organizationsanduserdefinedroles.html](Using_Organizations_and_User_Defined_Roles)
- [en/r-guest-access.html](Guest_Access_and_User_Management)
- [en/r_understanding-sub-targets.html](Understanding_Sub_Targets)
- [en/r_assigning-individual-server-s-to-a-resource-group.html](Assigning_Individual_servers_to_Resource_Group)
- [en/organizationspolicyandprofile.html](Using_Organizations_with_Policies_and_Profiles)
- [en/organizationinhyperflex.html](Organization_in_HyperFlex_Cluster_Profile)

## Single Sign-On with Intersight
Single Sign-On (SSO) authentication enables you to use a single set of credentials to log in to multiple applications. With SSO authentication, you can log in to Intersight with your corporate credentials instead of your Cisco ID. Intersight supports SSO through SAML 2.0, and acts as a service provider (SP), and enables integration with Identity Providers (IdPs) for SSO authentication. You can configure your account to sign in to Intersight with your Cisco ID and SSO. Learn more about SSO with Intersight here:
- [en/SSOwithIntersight.html](sso_in_intersight_overview)
- [en/creatingIdoktaapplication.html](creating_an_idp_application_with_okta)
- [en/creatingIdPOneLoginapplication.html](creating_an_idp_application_with_onelogin)
- [en/addingarelyingpartytrustinADFS.html](adding_a_relying_party_trust_in_ADFS)
- [en/addingSimpleSAMLasIdPinIntersight.html](adding_SimpleSAML_as_IdP_in_Intersight)
- [en/addingShibbolethIdPinIntersight.html](adding_Shibboleth_as_IdP_in_Intersight)
- [en/ConfiguringSSOwithAzureAD.html](configuring_SSO_with_Azure_AD)

## Multi-Factor Authentication in Intersight
Multi-Factor Authentication provides an extra layer of security to your Intersight account by requiring another security factor in addition to the Cisco ID. Use the instructions in this document to set up Multi-Factor Authentication:
- [en/SettingUpTwo-StepAuthenticationinIntersight.html](two-Step_Authentication)

## IP Access Management
Cisco Intersight offers the capability to manage and restrict access to Intersight only to users from Trusted IP addresses. You can define the IP addresses or IP ranges which are allowed to access Intersight. For guidelines and limitations, procedure for adding/editing Trusted IP ranges, and managing IP based access to Intersight, see:
- [en/IP_Access_Management_in_Intersight.html](ip_access_management_in_intersight)

## Search and Filter Functions in Intersight List View
Cisco Intersight displays a list of Servers, Fabric Interconnects, HyperFlex Clusters, Profiles, Policies, Alarms, and so on in the respective list views by default. You can use the search bar to search for Servers, Fabric Interconnects, HyperFlex Clusters, Profiles, Policies, Alarms and so on. Moreover, you have the option to refine the information displayed by applying various filters tailored to your specific needs.
- [en/Global_Search_in_Cisco_Intersight.html](global_search_in_intersight)

## Cisco Intersight Code Generator
The Cisco Intersight Code Generator is a feature designed to streamline automation by capturing user interactions in the Intersight UI and translating them into equivalent Python and PowerShell SDK code. For more information, see:
- [en/r-cisco-intersight-code-generator.html](cisco_intersight_code_generator)

## Configuring Device Connector
Intersight Device Connector provides a secure way for the connected targets to send information and receive control instructions from the Cisco Intersight portal, using a secure Internet connection. When an Intersight-enabled target or application starts, the Device connector starts at boot by default, and attempts to connect to the cloud service. Learn more about the device connector and configure it using the instructions available here:
- [en/ConfiguringDeviceConnector.html](configuring_device_connector)

## Cisco Unified Edge
Cisco Unified Edge provides a powerful and modular platform for organizations that require computing and AI inferencing at the edge locations. It uniquely combines compute, networking, storage, and security capabilities within a single, integrated chassis. This modular design simplifies deployment and reduces complexity at the edge. For more information, see:
- [en/components_ue.html](components_ue)
- [en/setting_up_ue.html](setting_up_ue)
- [en/ue_chassis_policies.html](ue_chassis_policies)
- [en/ue_servers_policies.html](ue_servers_policies)
- [en/fw_mgmnt_ue.html](fw_mgmnt_ue)
- [en/ue_ecmc_reset_replace.html](ue_ecmc_reset_replace)

## Fleet Management
Fleet management offers an automated solution that allows standardized configurations to be applied to one or more systems. This ensures consistent and repeatable configurations across deployment locations, simplifying Unified Edge management at scale. For more information, see:
- [en/about_fm.html](about_fm)

## Intersight Virtual Appliance
Cisco Intersight Virtual Appliance delivers the management features of Intersight in an easy to deploy VMware OVA, Microsoft Hyper-V Server VM, and KVM hypervisor on Linux, that allows you to control what system details leave your premises. The virtual appliance form factor enables additional data locality, security, or compliance needs that are not completely met by intersight.com. Learn more about Intersight Virtual Appliance here:
- [https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide.pdf]()

## Intersight Assist to Claim Endpoints
Cisco Intersight Assist helps you add endpoint targets to Cisco Intersight. Cisco Intersight Assist is typically a virtual machine (VM) running in your datacenter. You can install Intersight Assist using the bootstrap OVA that is available on Cisco.com. Currently, you can add Pure Storage devices, Hitachi Virtual Storage Platform devices, NetApp storage controllers, and VMware vCenter devices into Intersight after claiming them using Cisco Intersight Assist. For information on Intersight Assist, see:
- [en/Intersight_Assist.html](Intersight_Assist)
- [en/Cloud_Connection.html](Cloud_Connection)
- [en/Assist_View.html](Assist_View)
- [en/Software_View.html](Software_View)
- [en/Viewing_Audit_Logs_for_Intersight_Assist.html](Viewing_Audit_Logs_for_Intersight_Assist)

## Intersight New Look
The general look of Intersight is updated to deliver an improved experience for our users.
- [en/New_UI_Look.html](new_ui_look)

## Intersight Status Page
The Intersight status page is a communication tool that allows you to stay informed about outages, current and past incidents, and scheduled maintenance that might affect you. For details on the Intersight components tracked on the status and the status of an incident, see:
- [en/Intersight_Status_Page.html](intersight_status_page)

## Intersight Accessibility Support Features
Cisco recognizes international standards when assessing and documenting the accessibility of its products, services, and websites. For details, see:
- [en/Intersight_Accessibility.html](intersight_accessibility)

## Intersight Managed Mode
Intersight Managed Mode introduces a new implementation of concepts previously introduced with Cisco UCS Manager and moves ownership of the policy model into Cisco Intersight. For more information, see:
- [en/Cisco_Intersight_Managed_Mode_Configuration.html](cisco_intersight_managed_mode_configuration)
- [en/server_policies.html](server_policies)
- [en/domain_policies.html](domain_policies)
- [en/chassis_policies.html](chassis_policies)
- [en/IMM_Checklist.pdf](checklist_for_configuring_intersight_managed_mode)

## Intersight Standalone Mode Policies
In Intersight Standalone Mode, policies define configuration settings and operational behaviors for Cisco UCS C-Series servers that are connected directly to Intersight, without using Fabric Interconnects.   For more information, see:
- [en/r-ism-specific-policies.html](intersight_standalone_mode_policies)

## Cisco UCS X-Series Direct
Integrating Cisco UCS Fabric Interconnects 9108 100G with Cisco UCS X9508 Chassis and pairing them with Cisco UCS X-Series Compute Nodes delivers the Cisco UCS X-Series Direct solution. UCS X-Series Direct brings all the benefits of modular system to customers needing smaller server environments. For more information, see:
- [Cisco_UCS_X-Series_Direct.html](cisco_ucs_x_series_direct)

## Creating Network Policies
Network policies enable you to configure the Ethernet and Fibre Channel settings, assign connection and network communication resources between the server and the LAN, and assign storage resources and connections between the server and the SAN on the network. Learn more about the Network Policies here:
- [en/CreatingNetworkPolicies.html](creating_network_policies)
- [en/configuring_roce_v2_policy_properties.html](configuring_roce_v2_policy_properties)
- [en/configuring_access_policies_for_an_imc_file.html](configuring_access_policies_for_an_imc_file)

## Importing a Server Profile
Intersight provides the capability to import configuration details of Cisco UCS C-Series in standalone mode and FI-attached servers in Intersight Managed Mode (IMM), directly from Cisco IMC. The Server Profile import enables you to migrate the configuration of your existing servers to Intersight without having to create a profile and the policies manually. The Server Profile import operation creates the profile and the associated policies based on the server configuration. Learn more about importing a server profile here:
- [en/Importingserverprofile.html](Importing_Server_profile)

## Cloning a Policy
You can clone a policy for UCS Domain, UCS Server, UCS Chassis, or HyperFlex Cluster by using the Policy Clone wizard with properties that are similar to the existing policies. For more information, see:
- [cloning_a_policy.html](cloning_a_policy)

## Compliance with Hardware Compatibility List (HCL)
Cisco Intersight evaluates the compatibility of your Cisco UCS systems, HyperFlex systems, Intersight Managed Mode (IMM) servers, and Cisco UCS S-Series servers to check if the hardware and software have been tested and validated by Cisco or Cisco partners. Intersight reports validation issues after checking the compatibility of the server model, processor, firmware, adapters, operating system and drivers, and displays the compliance status with the Hardware Compatibility List (HCL). For more information about Hardware Compatibility Status, a detailed description and instructions on how to download Cisco UCS Tools, and for instructions on how to use the OS Discovery Tool, see:
- [en/Compliance_with_HCL.html](compliance_with_hcl)
- [en/Cisco_UCS_Tools.html](cisco_ucs_tools)
- [en/OS_Discovery_Tool.html](os_discovery_tool)

## Managing Firmware in Intersight Managed Mode
Managing firmware in Intersight Managed mode requires a Cisco Intersight Essentials or higher tier license. You can upgrade the firmware for Cisco Fabric Interconnect-attached UCS B-Series M5, M6 and C-Series M5, M6, M7, M8 servers, UCS X-Series M6, M7, M8 servers, and Cisco UCS Fabric Interconnects Series 6400, 6500, 6600, and Cisco UCS Fabric Interconnects 9108 100G in Intersight Managed mode. You can also upgrade the Cisco UCS X9508 chassis and Cisco UCS X580p PCIe Nodes in IMM. For detailed instructions, see:
- [en/Upgrading_Chassis_Firmware.html](Upgrading_Chassis_Firmware)
- [en/Upgrading_PCIe_Firmware.html](Upgrading_PCIe_Firmware)
- [en/Upgrading_Fabric_Interconnect_Firmware_imm.html](Upgrading_Fabric_Interconnect_Firmware_imm)
- [en/Enabling_Secure_FPGA_6400FI.html](Enabling_Secure_FPGA_6400FI)
- [en/Upgrading_Fabric_Interconnect-attached_Server_Firmware.html](Upgrading_Fabric_Interconnect-attached_Server_Firmware)
- [en/Upgrading_Server_Firmware_Using_Firmware_Policy.html](Upgrading_Server_Firmware_Using_Firmware_Policy)

## Managing Firmware in UCSM Managed Mode
Managing firmware in UCSM Managed mode requires a Cisco Intersight Essentials or above license. You can perform firmware upgrade for the following UCSM Managed Mode devices: •) Cisco UCS Fabric Interconnect-attached UCS B-Series and C-Series M3, M4, M5, and M6 servers •) Cisco Fabric Interconnect-attached Cisco UCS S3260 M3, M4, and M5 servers •) Cisco Fabric Interconnect-attached Cisco UCS S3260 chassis •) Cisco UCS 6200, 6300, 6400, 6500, 6600, and Cisco UCS Fabric Interconnects 9108 100G Series Fabric Interconnects For detailed instructions, see:
- [en/Upgrading_Fabric_Interconnect_Firmware_umm.html](Upgrading_Fabric_Interconnect_Firmware_umm)
- [en/Upgrading_Fabric_Interconnects-attached_Cisco_UCS_S3260_Chassis_Firmware.html](Upgrading_Fabric_Interconnects-attached_Cisco_UCS_S3260_Chassis_Firmware)
- [en/Upgrading_Server_Firmware.html](Upgrading_Server_Firmware)

## Managing Firmware in Standalone Mode
Managing firmware in Standalone mode requires a Cisco Intersight Essentials or above license. You can upgrade the firmware for Cisco UCS C-Series M4, M5, M6, M7, M8 and UCS S-Series M4, M5 servers in Standalone mode. For detailed instructions, see:
- [en/add_firmware_link.html](add_firmware_link)
- [en/Upgrading_UCS_C-Series_Standalone_Servers_Firmware.html](Upgrading_UCS_C-Series_Standalone_Servers_Firmware)
- [en/Upgrading_UCS_S-Series_Standalone_Servers_Firmware.html](Upgrading_UCS_S-Series_Standalone_Servers_Firmware)

## Managing Firmware Using Hardware Support Manager
Managing firmware using Hardware Support Manager (HSM) requires Cisco Intersight Advantage license. You must enable HSM in Cisco Intersight (ADMIN > Targets) to allow vSphere Lifecycle Manager (vLCM) plug-in manage firmware upgrade operations on Cisco UCS C-Series Standalone servers, Intersight Managed Mode (IMM) servers, and UCSM Managed Mode (UMM) servers. For detailed instructions, see:
- [en/Upgrading_Server_Firmware_Using_Hardware_Support_Manager.html](Upgrading_Server_Firmware_Using_Hardware_Support_Manager)

## UCS Server BIOS Tokens in Intersight Managed Mode
Intersight Managed Mode provides two methods for making global modifications to the BIOS settings on servers in Cisco UCS domain. You can create one or more BIOS policies that include a specific grouping of BIOS settings that match the needs of a server or set of servers, or you can use the default BIOS settings for a specific server platform. For more information, see:
- [https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide.pdf]()

## Cisco Intersight VIC Configuration
A Cisco UCS network adapter can be installed to provide options for I/O consolidation and virtualization support. This guide contains configuration details on RDMA over Converged Ethernet version 2 (RoCEv2) and Single Root I/O Virtualization (SR-IOV). For more information, see:
- [https://www.cisco.com/content/en/us/td/docs/unified_computing/Intersight/IMM-VIC-Config-Guide/imm-vic-configuration-guide.pdf]()

## Secure Data Deletion
Cisco Intersight provides the ability to securely erase all data on Cisco UCS C-Series Standalone and Intersight Managed Mode servers in accordance with EU Lot 9 regulations and NIST SP 800-88 standards. This feature ensures the protection of customer data privacy by permanently deleting all data, thus eliminating the possibility of data retrieval or recovery. For more information, see:
- [secure_data_deletion.html](secure_data_deletion)

## Performing Server Diagnostics
Cisco Intersight enables you to perform diagnostic tests on one or more servers and their components. You can identify the server issues, detect faulty components, and troubleshoot basic problems. This action is supported on Cisco UCS M6 and later servers in both Intersight Managed Mode and Intersight Standalone Mode. For more information, see:
- [en/performing-server-diagnostics.html](performing_server_diagnostics)

## Secure Self-Encrypting Drives
Intersight supports secure Self-Encrypting Drives (SEDs) on Intersight Managed Mode and UCS C-Series Standalone servers. SEDs have special hardware that encrypts incoming data and decrypts outgoing data in real time. The data on a SED is encrypted in the disk and stored in the encrypted form. A Media Encryption Key (MEK) controls this encryption and decryption. For more information, see:
- [r_secure-self-encrypting-drives.html](Secure_Self_Encrypting_Drives)

## Virtual Drive Configuration
Configuring Virtual Drives for M.2 RAID Controllers is now part of the Storage Policy. For more information, see the Creating a Storage Policy section in:
- [Cisco_Intersight_Managed_Mode_Configuration.html](cisco_intersight_managed_mode_configuration)

## Virtual Media Mount options
While creating a Virtual Media volume as part of a Virtual Media policy in Cisco Intersight, various file mount options are available based on the mount type (NFS, CIFS, HTTP/HTTPS) you choose. You can leave the Mount Options field (in the HDD or CDD grouping) empty or enter a comma-separated list of the mount options listed here:
- [en/vMedia_mount_options.html](vMedia_mount_options)

## Intersight Supported Product Identification Standards (PIDs)
This document provides information about the Product Identification Standards (PIDs) that are supported by Cisco Intersight.
- [en/Intersight_Supported_PIDs.html](intersight_supported_pids)

## Intersight Managed Mode SNMP Monitoring
The Simple Network Management Protocol (SNMP) is an application-layer protocol that provides a message format for communication between SNMP managers and agents. SNMP provides a standardized framework and a common language for monitoring and managing devices in a network. In Intersight Managed Mode (IMM) UCS domains, the monitored end-points are Fabric Interconnect (FI), Chassis Management Controller (CMC) on Chassis IOM/IFM, and Cisco Integrated Management Controller (CIMC) on the compute node or server. For more information, see:
- [https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/IMM_SNMP_Monitoring/b_imm_snmp_monitoring_guide.pdf]()

## Conversion Procedures for Modes(Standalone, IMM, UMM)
In Cisco Intersight, you can convert domains and servers from one mode to another. You can also move a server from one Intersight domain to another. For more information, see:
- [en/conversion_procedures.html](conversion_procedures)

## Intersight Managed Mode Transition Tool
Cisco Intersight Managed Mode (IMM) Transition Tool helps bootstrap new IMM deployments by replicating the configuration attributes of the existing Cisco UCS Manager (UCSM) and Cisco UCS Central infrastructure, and by converting the existing Service Profile and Templates to IMM Server Profile and Templates to accelerate deployment of new servers and to migrate existing servers to IMM. For more information, see:
- [https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/IMM-Transition-Tool/User-Guide-5-0/b_imm_transition_tool_user_guide_5_0.pdf]()
- [https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/IMM-Transition-Tool/b_imm_tt_rn.pdf]()

## Installing an Operating System
Cisco Intersight enables you to install vMedia-based operating systems managed servers in a data center. With this capability, you can perform an unattended OS installation on one or more Cisco UCS C-Series Standalone servers and Cisco Intersight Managed Mode (IMM) servers (C-Series, B-Series, and X-Series) from your centralized data center through a simple process. Before you install the operating system, you must add the images for the operating system and the server configuration utility in the software repository. For detailed instructions about adding the images to the software repository and installing the OS, see:
- [en/OSinstallguide.html](OSinstallguide)
- [en/osInstallOverview.html](operating_system_installation_overview)
- [en/installing_an_operating_system.html](installing_an_operating_system)
- [en/installOSCSV.html](installos_csv)
- [en/addingOSimage.html](adding_OSimage)
- [en/addingSCU.html](adding_scu)
- [en/adding_an_operating_system_file.html](adding_an_operating_system_file)
- [en/validating_image.html](validating_image)
- [en/osTargets.html](install_target_selection)
- [en/osPasswdEncrypt.html](password_encryption_in_an_operating_system_install)
- [en/osTroubleshooting.html](troubleshooting_an_operating_system_installation)
- [en/DriverInstallationUnifiedEdge.pdf](driver_installation_procedure_on_unified_edge)

## UCS C890 M5 Target Management in Intersight
The Cisco UCS C890 M5 Rack Server provides high-reliability, intensive compute operations, and seamless network infrastructure integration. For more information, see:
- [claiming_ucs_c890_m5_targets.html](claiming_ucs_c890_m5_targets)

## UCS C885A M8 Server Management in Intersight
The Cisco UCS C885A M8 rack server provides powerful performance for demanding artificial intelligence tasks, enabling faster results with easy deployment. For more information, see:
- [managing_ucs_c885a_m8_server.html](managing_ucs_c885a_m8_server)

## UCS C845A M8 Server Management in Intersight
The Cisco UCS C845A M8 Rack Server is a scalable, flexible, and customizable AI platform built on the NVIDIA® MGX reference design for accelerated computing. For more information, see:
- [managing_ucs_c845a_m8_server.html](managing_ucs_c845a_m8_server)

## HyperFlex Cluster Deployment
Cisco Intersight provides an installation wizard to install, configure, and deploy Cisco HyperFlex Edge, HyperFlex with FI, and Cisco HyperFlex without Fabric Interconnect clusters. The wizard constructs a pre-configuration definition of your cluster, called a HyperFlex Cluster Profile. This definition is a logical representation of the HyperFlex nodes in your HyperFlex cluster. For more information, see:
- [https://www.cisco.com/c/en/us/td/docs/hyperconverged_systems/HyperFlex_HX_DataPlatformSoftware/HyperFlex_Installation_Guide_for_Intersight/b_HyperFlex_Installation_Guide_for_Intersight.pdf]()

## Expand HyperFlex Clusters in Intersight
Starting from HyperFlex Data Platform version 4.0(2e), you can expand ESXi based 10/25 GbE HyperFlex Edge, Fabric Interconnect attached, and HyperFlex Data Platform without Fabric Interconnect clusters with a minimum of 3 nodes. For detailed instructions about expanding HyperFlex Clusters, see:
- [en/Expand_Cisco_HyperFlex_System_Clusters.html](expand_cisco_hyperflex_clusters_in_intersight)

## Upgrade HyperFlex Systems in Intersight
Starting HyperFlex Data Platform Release 4.0(1b), you can perform multi-site remote upgrade of HyperFlex Edge clusters installed using Intersight. Intersight based upgrade for HyperFlex Edge clusters provides an efficient and scalable way to upgrade single or multiple HyperFlex Edge clusters. You can upgrade Cisco HyperFlex Edge 2-Node, 3-Node, and 4-Node clusters. Starting HX Data Platform Release 4.0(2a), Intersight supports combined upgrade of VMware ESXi and HyperFlex Data Platform. Starting HyperFlex Data Platform Release 4.5(2b), you can perform upgrade of DC-No-FI clusters. For detailed upgrade prerequisites and instructions about upgrading HyperFlex Clusters, see:
- [en/hxcluster_upgrade.html](upgrade_cisco_hyperflex_systems_with_cisco_intersight)

## HyperFlex Systems Administration Guide for Intersight
Cisco Intersight provides the ability to view hosts, virtual machines, datastores, storage containers, and drives. You can create and manage datastores and storage containers. For more information, see:
- [en/Cisco_HyperFlex_Systems_Administration_Guide.html](cisco_hyperflex_systems_administration_guide)

## HyperFlex Software Encryption
Starting HyperFlex Data Platform 5.0(1b), you can configure software encryption on HyperFlex clusters. HyperFlex software encryption provides file level end-to-end data Encryption to provide confidentiality of data at-rest from theft of storage media and unauthorized access. Intersight manages the keys natively with Intersight Key Manager which increases both security and simplicity by eliminating the overhead of key management. For more information, see:
- [en/HyperFlex_Software_Encryption.html](hyperflex_software_encryption)

## Health Check for HyperFlex Clusters
Cisco Intersight provides the ability to view finer details about the health of HyperFlex clusters. You can run pre-defined health checks on HyperFlex clusters and gather reports on the various health checks. For more information, see:
- [en/hyperflex_cluster_health_check.html](hyperflex_cluster_health_check)
- [en/HyperFlex_Cluster_Health_Check_Causes_and_Resolution.html](hyperflex_cluster_health_check_causes_and_resolution)

## HyperFlex Cluster Capacity Planning
Cisco Intersight provides the ability to predict the storage utilization for HyperFlex Clusters. Using the historical data of used storage capacity along with the predicted storage utilization per HyperFlex cluster, you can proactively scale the storage utilization on the HyperFlex Clusters. In addition, Cluster Capacity Planning provides expansion recommendations and can be used to generate a cost estimate using Cisco Commerce Workspace (CCW). For more information, see:
- [en/HyperFlex_Cluster_Capacity_Planning.html](hyperflex_cluster_capacity_planning)

## HyperFlex Cluster Witness Service
The Invisible Cloud Witness powered by the Cisco Intersight platform is an innovation that eliminates the need of a third site or infrastructure to run the witness services that helps in avoiding the split brain scenarios. This can significantly ease the burden of deploying and managing two-node HCI clusters at a large scale without having to manage and operate the witness service. Going further, to avoid the dependency on WAN links in remote sites, Cisco developed HyperFlex Local Containerized Witness server which is a web application that allows end user to deploy the witness service locally on any networking device that supports containers. This completely eliminates the need of WAN or Intersight connectivity during normal operations to tolerate a node failure. For more information, see:
- [en/Deploy_Local_Container_Witness_Servers.html](deploy_local_container__hyperflex_witness_servers)
- [https://www.cisco.com/c/dam/en/us/products/collateral/hyperconverged-infrastructure/hyperflex-hx-series/whitepaper-c11-741999.pdf]()

## N:1 Replication for HyperFlex Clusters
Cisco Intersight provides the ability for HyperFlex clusters to take snapshots of Virtual Machines and restore using Intersight. Users can configure multiple HyperFlex clusters at different sites with backup policies to create snapshots of virtual machine data which is replicated to a centralized HyperFlex backup target cluster. The VM snapshots are retained locally on the cluster and a backup target cluster. These VMs snapshots are critical tools in the event that you need to recover from logical corruption, accidental deletion of data, a cluster or site outage, or planned VM migration from one edge cluster to another. For more information, see:
- [en/replication_for_cisco_hyperFlex_clusters.html](replication_for_cisco_hyperFlex_clusters)

## HyperFlex Node Redeployment Workflow
Cisco Intersight provides a node redeployment workflow for HyperFlex clusters. For more information, see:
- [en/Node_Redeployment_Workflow.html](node_redeployment_workflow)

## Intersight Advisories
Cisco Intersight alerts users about the endpoint targets that are impacted by supported security advisories, field notices, and End of Life (EOL) advisories. EOL advisories are available for UCS product family and HyperFlex Data Platform software releases. These alerts are displayed as Advisories in Intersight. Two-Tiered Intersight Advisory Processing Tier 1: 30-Minute Processing Cycle : Field Notices and Security Advisories published less than three years on Cisco.com ago are processed every 30 minutes, and any updates on the devices with respect to those advisories will be displayed within 30 minutes. Tier-2: 4-12 Hour Processing Cycle :  Field Notices and Security Advisories published more than three years ago, and all End-of-Life Advisories, continue to be processed every 4-12 hours, and updated status for the device is displayed within 12 hours. Note : A newly published Security Advisory or Field Notice is initially placed in Tier-2 until it has been successfully processed for all Intersight accounts. It is then moved to Tier-1 to enable faster processing. For information on processing times, please refer to the banner on the specific advisory details page within the Intersight UI. You can create custom subscriptions for security advisories, field notices, end-of-sale/support announcements, software updates, and updates to known bugs for Cisco products. For more information, see https://cway.cisco.com/mynotifications . Note: Advisories are supported with Essentials tier license. Advisories are digitized and published in Intersight within 1 week of being published on cisco.com. For a complete list of supported security advisories, field notices, and EOL advisories, see:
- [en/cisco_security_advisories.html](cisco_security_advisories)
- [en/cisco_field_notices.html](cisco_field_notices)
- [en/Cisco_End_of_Life_Advisories.html](cisco_end_of_life_advisories)
- [en/acknowledge_advisory.html](acknowledge_advisory)

## Viewing Storage Information In Intersight
Cisco Intersight provides the ability to view information on storage targets that have been claimed using Cisco Intersight Assist. After claiming these storage targets, you can view general information and inventory information. You can view inventory information only if you have installed the Intersight Advantage license. You also need to be logged in as an account administrator, read-only user or a storage administrator. For more information and instructions on viewing information on storage targets, see:
- [en/Storage_Table_View.html](Storage_Table_View)
- [en/Storage_Inventory_View.html](Storage_Inventory_View)

## Viewing Virtualized Objects in Intersight
Cisco Intersight provides the ability to view information on virtualized objects (VMware vCenter targets) that have been claimed using Cisco Intersight Assist. After claiming these targets, you can view general information and inventory information. You can view device inventory information only if you have installed the Intersight Advantage license. You also need to be logged in as an account administrator, read-only user or a virtualization administrator. For detailed information and instructions on viewing information on virtualized objects, see:
- [en/Cluster_General_View.html](Cluster_General_View)
- [en/Datacenter_General_View.html](Datacenter_General_View)
- [en/Datastore_General_View.html](Datastore_General_View)
- [en/Datastore_Cluster_General_View.html](Datastore_Cluster_General_View)
- [en/Virtual_Machine_General_View.html](Virtual_Machine_General_View)
- [en/Virtual_Machine_Template_General_View.html](Virtual_Machine_Template_General_View)
- [en/Host_General_View.html](Host_General_View)

## Intersight Virtualization Service
Intersight Virtualization Service (IVS) is a fully curated, lightweight cloud management platform that provides a way to managing virtualization infrastructure for VMware. Intersight Virtualization Service is a part of the larger Intersight platform.Intersight Virtualization Service is a part of the larger Intersight platform. For detailed information, see:
- [intersight_virtualization_service.html](intersight_virtualization_service)

## Redfish Server Target Management in Intersight
Cisco Intersight provides the ability to claim and monitor Dell PowerEdge and HPE ProLiant servers as Redfish servers. For more information, see:
- [en/claiming_redfish_server_targets.html](claiming_redfish_server_targets)

## Nexus Switch and MDS Switch Support
Cisco Nexus Switches provide the foundation for Application Centric Infrastructure, delivering scalability, performance, and exceptional energy efficiency. Cisco MDS Switches offer multiple layers of network and storage-management intelligence, to help lower total cost of ownership. For more information, see:
- [Nexus_MDS.html](Nexus_MDS)

## Intersight Cloud Orchestrator
Cisco Intersight Cloud Orchestrator provides a Workflow Designer and Task Designer that helps you create new workflows and tasks respectively to manage targets in Cisco Intersight. You can also edit existing workflows and tasks to manage targets in Cisco Intersight. For detailed information and instructions on managing workflows, tasks, and data types, see:
- [en/Workflow_Designer.html](Workflow_Designer)
- [en/Task_Designer.html](Task_Designer)
- [en/Data_Types.html](Data_Types)

## Rollback Execution
Intersight Orchestration allows use cases to be realized as workflows composed of reusable tasks. Rollback Execution helps you to revert the entities created or modified during workflow execution. For more information, see:
- [en/Rollback_Execution.html](Rollback_Execution)

## Task Executors
Intersight Orchestrator allows workflow designers to perform executor tasks on endpoint in workflows. For more information, see:
- [en/Web_API_Request.html](web_api_request)
- [en/Executor_Ansible.html](Executor_Ansible)
- [en/Executor_Ansible_Reusable.html](Executor_Ansible_Reusable)
- [en/Executor_SSH.html](Executor_SSH)
- [en/Executor_SSH_Reusable.html](Executor_SSH_Reusable)
- [en/Executor_PowerShell.html](Executor_PowerShell)

## Adding Orchestration Targets to Resource Groups
Intersight Orchestration enables automation through workflows, supporting Ansible, HTTP, PowerShell, and SSH endpoints, with API-based target inclusion for resource groups.
- [en/ico_resource_group.html](Adding_Orchestration_Targets_Resource_Groups)

## Intersight Workload Optimizer
Cisco Intersight Workload Optimizer radically simplifies application resource management with a single tool that dynamically optimizes resources in real time to ensure application performance. It continuously optimizes critical IT resources, resulting in more efficient use of existing infrastructure and lower operational costs on premises and in the cloud. Cisco Intersight Workload Optimizer analytics engine matches real-time workload demand to the underlying infrastructure supply. It dynamically recommends and initiates the necessary automated actions, ensuring application performance.
- [en/Cisco_Intersight_Workload_Optimizer_Getting_Started_Guide.pdf]()
- [en/Cisco_Intersight_Workload_Optimizer_User_and_Target_Guide.pdf]()
- [https://developer.cisco.com/docs/intersight-workload-optimizer/]()

## Intersight Mobile App
The Intersight mobile app complements the Intersight platform by providing a mobility-optimized connection to the resources managed in your account. The mobile app enables you to stay up-to-date with the status of your environment and connect with members of your IT organization to address critical issues on the go.
- [en/MobileApp.html](mobile)

## VCF Operations Management Pack for Cisco Intersight
The VCF Operations Management Pack for Cisco Intersight allows you to use VCF Operations to monitor, manage, and troubleshoot infrastructure running on Cisco Intersight Managed Mode (IMM) servers.
- [en/r_vcf_op-aria.html](VCF_Operations_Management_Pack)

## vSphere/vCenter Plugin
The VMware vSphere/vCenter plugins provided by Cisco Intersight allow VMware vCenter users to manage and monitor UCS servers in Intersight directly from the VMware vCenter interface.
- [Upgrading_Server_Firmware_Using_Hardware_Support_Manager.html](Upgrading_Server_Firmware_Using_Hardware_Support_Manager)
- [en/r_vSphere_vCenter.html](plugin_vsphere)
- [en/r_vSphere_vCenter_ts.html](plugin_vsphere_ts)

## Installing VMware ESXi 9 with the Latest Cisco Drivers
This document provides detailed instructions for UCS customers on how to use one of the following options to include Cisco add-on drivers with the ESXi image on servers: Manually install Cisco drivers on each VMware host. Create a custom ISO using VMware vSphere Lifecycle Manager (vLCM) in VMware vCenter.
- [en/Installing_VMware_ESXi_9_with_Latest_Cisco_Drivers.pdf]()

## Deploy VMware Clusters
Simplify the deployment of VMware vSphere, VCF Management, and VCF Workload clusters on Cisco UCS servers managed in Cisco Intersight Managed Mode (IMM). These workflows, powered by Cisco Intersight Cloud Orchestrator (ICO), automate key deployment tasks after users input necessary information.
- [deploy_vsphere_cluster.html](deploy_vsphere_cluster)
- [deploy_vcf_cluster.html](deploy_vcf_cluster)

## Intersight Add-on for Splunk
Cisco Intersight Add-on for Splunk is a Cisco supported extension to Splunk platform designed to integrate Cisco Intersight's powerful infrastructure management capabilities with Splunk's robust data analysis platform. This add-on enables IT administrators and engineers to collect, monitor, and analyze data from Cisco Intersight, providing deep insights into their data center operations and enhancing their ability to manage infrastructure efficiently. The Cisco Intersight Add-on for Splunk is available for download on Splunkbase marketplace.
- [en/Cisco_Intersight_add_on_for_splunk_Release_Notes.pdf]()
- [en/Cisco_Intersight_Add-on _for_Splunk_User_Guide.pdf]()

## ServiceNow Plugins
The ServiceNow plugins import and synchronize your Intersight inventory and alarms so they can be tracked along with existing inventories. Use the plugins to monitor incidents raised on alarms for Servers and Fabric Interconnects. The Service Graph Connector also displays relationships between configuration items in ServiceNow's Service Graph Connector framework.
- [en/r_sevicenow_plugin_incident.html](plugin_servicenow_incident)
- [en/r_service_graph_connector.html](plugin_servicenow_graph)

## Backup and Restore for UCS Director
Cisco Intersight provides the ability to take backups and restore backups for the claimed UCS Director instances. For detailed information and instructions about taking backups and restoring UCS Director, see:
- [en/backuprestoreoverview.html](backup_and_restore)

## Connector Pack Upgrades for UCS Director
Cisco Intersight provides the ability to upgrade connector pack versions on claimed UCS Director instances. Only an account administrator can upgrade connector pack versions on UCS Director instances. For information on prerequisites and instructions on upgrading connector packs, see:
- [en/connector-pack-upgrade-UCSD.html](connector-pack-upgrade-UCSD)