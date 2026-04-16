# Cisco Intersight Virtual Appliance and Intersight Assist Getting Started Guide

| | |
|---|---|
| **URL Title** | Cisco Intersight Virtual Appliance and Intersight Assist Getting Started Guide |
| **URL** | https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide/m_setting_up_appliance.html |
| **Long URL** |  |
| **HTML Title** | Cisco Intersight Virtual Appliance and Intersight Assist Getting Started Guide - Set Up [Cisco Intersight] |
| **Source file** | `ucs-docs-raw/html/m_setting_up_appliance.html` |
| **File type** | HTML |
| **Fetched on** | 2026-04-16 10:49:06 |

---

## Page 1: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide/m_setting_up_appliance.html

## Setting Up Single-Node Intersight Connected Virtual Appliance  
  
Cisco Intersight Virtual Appliance is distributed as a deployable virtual machine contained in an Open Virtual Appliance (OVA) file format, ZIP file format, or TAR file format. 

Before You Begin: Ensure that you have installed Intersight Virtual Appliance software as per the instructions in [Installing Cisco Intersight Virtual Appliance and Intersight Assist on VMware vSphere](m_installation.html#id_95741). 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

An appliance installer is required to restore the appliance from a backup. If a backup is taken from appliance release version N, it can only be restored using an installer version N or higher. For example: 

  * If the backup of your appliance is version 1.1.0-0, then you need appliance installer version 1.1.0-0 or higher.
  * If the backup of your appliance is patch release version 1.1.1-1, then you need appliance installer version 1.1.1-1 or higher.

A limited number of appliance installer versions are available on [Cisco Software Central](https://software.cisco.com/). If the required version of the installer is not present, contact Cisco TAC. 

* * *  
  
---|---  
  
After the Cisco Intersight Virtual Appliance software deployment is complete, and the VM is powered on, access your VM using the <<https://your fqdn.com>> URL. The Intersight Appliance Installer screen appears and allows you to complete the setup for either a new install, recover the appliance software from backup, or add a node to the appliance. 

The wizard runs through a series of steps to download and install software packages. You can view the progress of the installation. 

Use the following instructions to complete the Intersight Connected Virtual Appliance setup:

### Procedure

* * *

**Step 1** |  On the Intersight Appliance Installer screen, select Install Connected Virtual Appliance and click Start.   
---|---  
**Step 2** |  Log in to the Intersight Virtual Appliance Connect page using your Cisco ID. If you do not have a Cisco ID, you can create one [here](https://id.cisco.com/ui/v1.0/profile-ui). 

  1. (Optional) Click Settings  to enable HTTPS Proxy Settings.  If an HTTP/S proxy is required to connect your Intersight Virtual Appliance to the internet, you must configure proxy settings before you complete the connection step. 
  * Click Settings and enable the HTTPS Proxy option. 
  * Add the Proxy Hostname or IP Address, and the Proxy Port.  The proxy port must be in the range between 1 and 65535. You can edit the Proxy settings from the appliance UI, Settings > Networking > Cloud Connection. 
  2. Use the Device ID and Claim Code  that is displayed on the Connect page to complete connecting to Intersight. 
  3. Ensure that the Connection status displays Claimed.  |  **Note** |  A new browser tab appears to display the status of the target claim in Intersight. If you do not have an Intersight account, you can create one in the Account Creation window and claim a target. If the target connection is successful, a success message is displayed. Click Close to exit the tab and return to the Intersight Appliance Installer setup wizard. If the target claim is unsuccessful, you will be taken to the Intersight login screen to restart target claim workflow.   
---|---  

  
**Step 3** |  In the Intersight Appliance Installer setup wizard, do the following: 

  1. Connect—Click Continue to proceed to the Check Network Requirements step. 
  2. Check Network Requirements—View the results and click Next to proceed to the Configure Internal Network step.  Note that if any of the DNS test fails during the network requirements check, you cannot proceed with the configuration.
  3. Configure Internal Network—If necessary, change the default Internal Network IP address and click Next to proceed to the Select Software Version step.  **Note:** This IP address range is used for internal communications within Intersight Virtual Appliance. This range must be within the 172.16.0.0/12 subnet, but can be a smaller range (up to a subnet prefix size of 20). In most cases, the default value can be used. One reason to change the default value would be if the Appliance needs to communicate directly with other devices in the same subnet, that is without traversing IP translation mechanisms such as NAT. 
  4. Select Software Version—You have the option to download the latest version of the appliance software, or upload a supported version of the appliance software that is either the same as, or newer than, the installer version. 


  1. To download the latest version of the appliance software, select the Download Latest Version button and click Finish to proceed to the Installation Result screen. 
  2. To upload a version of the appliance software, select either Local Machine or Network Share, depending on where you saved the software packages.  |  **Note** | 
  * To manually update, install, or restore Intersight Connected Virtual Appliance, you will need to access the Appliance Account so that you can download the required software packages. For information, see Creating an Appliance Account for Downloading Software Packages and Downloading Software Packages for Intersight Virtual Appliance. 
  * If you are using a major version installer, select the major version Intersight appliance bundle. If you are using a patch version installer, provide the major version Intersight appliance bundle and, optionally, a patch version Intersight appliance bundle. You must ensure that the patch bundle is compatible with the major bundle. 
  * The appliance bundle version must be equal to or higher than the installer version. If you are using a patch installer, the combined version of the patch and major appliance bundles must be equal to or higher than the patch installer version.   
---|---  
  * For Local Machine, browse to where you saved the software images, and then click Finish to proceed to the Installation Result screen. 

  * For the Network Share option, enter the protocol and enter details of the remote server from where you want to copy the file, and click Finish to proceed to the Installation Result screen. 

  * Protocol—Communication protocol used for file transfer. Intersight Virtual Appliance currently supports CIFS (Common Internet File System), SCP (Secure Copy Protocol) and SFTP (Secure File Transfer Protocol). 

  * Server IP/Hostname—The host server from where the file is copied 

  * Port—TCP port to use 

  * Location—Directory where the file to be copied is stored 

  * Software Bundle File Name for Appliance—Name of the file to be copied from the network share 

  * Patch Bundle File Name for Appliance (Optional)—Name of the file to be copied from the network share. This is only applicable for patch version installers. 

  * Username—Username for authenticating with the network share 

  * Password—Password for authenticating with the network share 

  3. Installation Results—You can view the progress of the installation on this screen. 


  
**Step 4** |  Specify Data Collection.  Specify your preference to allow Intersight to send additional system information to Cisco. This option is enabled by default. For more information about what data is collected by Intersight, see [Data Collected from Intersight Connected Virtual Appliance](m_settings_dashboard.html#reference_wdb_3ss_4gb).   
**Step 5** |  Click Register License.  Obtain a license registration token from Cisco Smart License Manager and apply the token to activate your license. The license registration process could take a few minutes to complete. For more information about registering your Intersight license, watch [Cisco Intersight Licensing Tiers and Registration](https://intersight.com/help/video#cisco_intersight_licensing_tiers_and_registration).  After you click Finish, the Intersight Connected Virtual Appliance dashboard displays.   
  
* * *

### What to do next

Once you have successfully completed the initial set up of the single-node Intersight Virtual Appliance: 

  * You can add additional nodes to create a multi-node cluster for High Availability. For more information, see Configuring a Multi-Node Cluster for High Availability in Intersight Virtual Appliance. 

  * You can add a metrics node to create a multi-node cluster for advantage tier metrics data collection. For more information, see Configuring a Multi-Node Cluster for Increased Metrics Scalability in Intersight Virtual Appliance. 


---

## Page 2: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide/preface.html

  * [Communications, Services, Bias-free Language, and Additional Information](/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/preface.html)
  * [Introduction to Intersight Managed Mode Server Bios Tokens](/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/b_UCS_BIOS_Tokens_Guide_chapter_01.html)
  * [Supported Platforms](/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-supported-platforms-and-bios-tokens.html)
  * [Boot Options BIOS Settings](/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-boot-options-bios-settings.html)
  * [Intel Directed IO](/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-intel-directed-io.html)
  * [LOM and PCIe Slots](/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-lom-and-pcie-slots.html)
  * [Main](/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-main.html)
  * [Memory](/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-memory.html)
  * [PCI](/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-pci.html)
  * [Power and Performance](/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-power-and-performance.html)
  * [Processor](/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-processor.html)
  * [QPI](/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-qpi.html)
  * [Server Management](/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-server-management.html)
  * [Trusted Platform](/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-trusted-platform.html)
  * [USB](/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-usb.html)


---

## Page 3: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide/m_about_this_guide.html

## Introduction

Cisco Intersight offers flexible deployment either as Software as a Service (SaaS) on Intersight.com or running on your premises as Cisco Intersight Virtual Appliance. The virtual appliance provides the benefits of Cisco Intersight while allowing more flexibility for those with additional data locality and security requirements. The Cisco Intersight connected Virtual Appliance software can be deployed on premises, allowing users to take advantage of the SaaS functionality. The Private Virtual Appliance can be deployed on premises with further security restrictions. 

Cisco Intersight Assist helps you add endpoint devices to Cisco Intersight. A datacenter could have multiple devices that do not connect directly with Cisco Intersight. Any device that is supported by Cisco Intersight but does not connect directly with it, will need a connection mechanism. Cisco Intersight Assist provides that connection mechanism, and helps you add devices into Cisco Intersight. 

The guide provides an overview of how to install and set up Cisco Intersight Virtual Appliance and Cisco Intersight Assist in your environment. 

---

## Page 4: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide/m_appliance_overview.html

## About Cisco Intersight Virtual Appliance

Cisco Intersight Virtual Appliance delivers the management features of Intersight in an easy to deploy VMware OVA, Microsoft Hyper-V Server VM, KVM hypervisor, and Nutanix AHV hypervisor. Intersight Virtual Appliance provides the benefits of Cisco Intersight that offers an intelligent level of management to enable customers to analyze, simplify, and automate their environments in more advanced ways than the previous generations of tools, while allowing more flexibility with additional data locality, security, and compliance requirements. 

You can deploy Intersight Virtual Appliance in one of the following modes:

  * Intersight Connected Virtual Appliance

  * Intersight Private Virtual Appliance

  * Intersight Assist


Intersight Connected Virtual Appliance delivers the management features of Intersight while allowing you to control what system details leave your premises. Intersight Connected Virtual Appliance deployments require a connection back to Cisco and Intersight services for automatic updates and access to services for full functionality. 

Intersight Private Virtual Appliance delivers the management features of Intersight and allows you to ensure that no system details leave your premises. Intersight Private Virtual Appliance deployments is intended for an environment where you operate data centers in a disconnected (air gapped) mode. 

For an overview of Intersight Assist, see About Cisco Intersight Assist. 

Deployment options available for Intersight Virtual Appliance are as follows:

  * You can deploy Intersight Virtual Appliance as a single-node virtual machine. In the standalone configuration, you can opt-in to enable the essential tier metrics data collection. For more information about the supported configuration, see Supported Configuration Limits for Intersight Virtual Appliance. For more information about data collection, see [Data Collection](https://intersight.com/help/appliance/monitoring/monitoring_data_collection#supported_devices). 

  * You can deploy Intersight Virtual Appliance on VMware vSphere as a multi-node cluster which allows for advantage tier metrics data collection. This deployment option is a two-node cluster that includes an appliance management node and a metrics node. Once you have completed the initial set up of the single-node appliance, you can add a metric node. For more information about configuring an advantage tier metrics node, see [Configuring a Multi-Node Cluster for Increased Metrics Scalability in Intersight Virtual Appliance](m_setting_up_appliance.html#configuring-metrics-node). For more information about the supported configurations, see Supported Configuration Limits for Intersight Virtual Appliance. 

  * You can deploy Intersight Virtual Appliance on VMware vSphere as a multi-node cluster which allows for high availability. This deployment option is a three-node cluster that includes three High Availability (HA) management nodes. Once you have completed the initial set up of the single-node appliance, you can add additional High Availability (HA) management nodes. After you successfully add the two additional HA management nodes, you can create a multi-node cluster in Intersight Virtual Appliance for HA. Note that metrics data collection is not supported in the three-node cluster deployment. For more information, see, [Configuring a Multi-Node Cluster for High Availability in Intersight Virtual Appliance](m_setting_up_appliance.html#Cisco_Task_in_List_GUI.dita_a18a1d2e-5c8e-42c8-a7de-6bb01b218fde). 

  * You can deploy Intersight Virtual Appliance on VMware vSphere as a multi-node cluster which allows for metrics data collection. This deployment option is a four-node cluster that includes HA management cluster and a metrics node. Once you have completed the initial set up of the HA management cluster, you can add a metric node. For more information about configuring an advantage tier metrics node, see [Configuring a Multi-Node Cluster for Increased Metrics Scalability in Intersight Virtual Appliance](m_setting_up_appliance.html#configuring-metrics-node). For more information about the supported configurations, see Supported Configuration Limits for Intersight Virtual Appliance. 


The following table summarizes the deployment options in Intersight Virtual Appliance.

Table 1. Deployments Options in Intersight Virtual Appliance Deployment Option |  Number of Nodes |  Functionality |  Metrics Data Collection |  Supported Hypervisors  
---|---|---|---|---  
Single-node |  Standalone |  Intersight Virtual Appliance management capability.  |  Yes - option to enable the essential tier metrics data collection. | 

  * VMware vSphere
  * Microsoft Hyper-V
  * KVM Hypervisor
  * Nutanix AHV

  
Multi-node |  Two-node cluster |  Intersight Virtual Appliance management capability and a separate metrics node for metrics data collection. |  Yes - metrics node is required to enable essential and advantage tier metrics data collection.  |  VMware vSphere  
Multi-node |  Three-node cluster |  Intersight Virtual Appliance management capability for high availability. |  No - metrics data collection is not supported in a three-node cluster configuration. |  VMware vSphere  
Multi-node |  Four-node cluster |  Intersight Virtual Appliance management capability for high availability and a separate metrics node for metrics data collection.  |  Yes - metrics node is required to enable essential and advantage tier metrics data collection. |  VMware vSphere  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Attention** | 

* * *

Before installing and setting up Intersight Virtual Appliance, it is strongly recommended that you read the information provided in the System Requirements section.  Intersight Virtual Appliance supports TLS 1.3 protocol for HTTPS communication for improved Transport Layer Security.

* * *  
  
---|---  
  
This guide provides an overview of how to install and set up Intersight Virtual Appliance in your environment.

For latest updates on Intersight Virtual Appliance features and functionality, see [Intersight Appliance Help Center](https://intersight.com/help/appliance). 

---

## Page 5: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide/m_installation.html

## Installing Cisco Intersight Virtual Appliance and Intersight Assist on VMware vSphere

Cisco Intersight Virtual Appliance is distributed as a deployable virtual machine contained in an Open Virtual Appliance (OVA) file format, ZIP file format, or a TAR file format. Cisco Intersight Virtual Appliance supports VMware High Availability (VMHA) to ensure non-disruptive operation of the virtual appliance. For more information about VMHA, please refer to the documentation on vmware.com.  ![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Attention** | 

* * *

Intersight Virtual Appliance and Intersight Assist OVA must be deployed using VMware vCenter. The OVA cannot be directly deployed on ESXi servers.  By default, VMware vCenter does not include a Certificate Authority (CA) that validates the Cisco digital signature on the Intersight Virtual Appliance OVA file. The VMware vCenter GUI will indicate that the OVA’s certificate is invalid and is not trusted. Although possible, it is recommended that you **_do not ignore this warning_** and proceed with the installation. Instead, download and install the appropriate root CA from the table below that will validate the digital signature on the Intersight Virtual Appliance OVA file. Validating the signature ensures that the OVA was both issued by Cisco and has not been modified by a 3rd party. 

* * *  
  
---|---  
  
The root CA certificates listed in the following table are available on [Cisco's PKI page](https://www.cisco.com/security/pki/codesign/). 

OVA version  |  CA Issuer  |  CA Serial Number  |  CA Expiration   
---|---|---|---  
1.1.0-0 and later |  TrustID EV Code Signing CA 4  |  40:01:7f:9e:01:04:d0:f0:da:98:8d:43:d8:97:43:03  |  March 18, 2030   
1.0.9-630  |  TrustID EV Code Signing CA 4  |  40:01:7f:9e:01:04:d0:f0:da:98:8d:43:d8:97:43:03  |  March 18, 2030   
1.0.9-588  |  DigiCert Trusted G4 Code Signing 2021 CA1  |  08:ad:40:b2:60:d2:9c:4c:9f:5e:cd:a9:bd:93:ae:d9  |  April 28, 2036  
1.0.9-499  |  None  |  None  |  None   
1.0.9-342  |  DigiCert Trusted G4 Code Signing 2021 CA1  |  08:ad:40:b2:60:d2:9c:4c:9f:5e:cd:a9:bd:93:ae:d9  |  April 28, 2036  
  
Use the steps in the following task to install and deploy the appliance on VMware vSphere. To install and deploy a multi-node cluster for high availability for Intersight Virtual Appliance on VMware vSphere, repeat the steps in the following task three times.

### Before you begin

Ensure the following:

  * Download the latest version of the Cisco Intersight Virtual Appliance and Assist installer package from the [Cisco Software Download](https://software.cisco.com/download/home/286319499/type) site. 

  * If you are installing Private Virtual Appliance, also download the latest Cisco Intersight Private Virtual Appliance software package (intersight-appliance-bundle) from the Intersight Software Downloads Portal. For more information, see [Downloading Software Packages from Intersight Virtual Appliance](m_setting_up_appliance.html#Cisco_Task_in_List_GUI.dita_a1922fb8-cac5-42c4-90e1-8370efd7e7e5). 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Attention** | 

* * *

  * Before installing and setting up Intersight Virtual Appliance, it is strongly recommended that you read the information provided in the [System Requirements](m_appliance_overview.html#Cisco_Reference.dita_a6ea1ddc-e212-4367-9579-e9320b64f1b5) section. 
  * Setting up a single-node Intersight Virtual Appliance requires an IP address and two DNS records for that IP address. For more information about IP addresses and Hostname requirements, see [IP Address and Hostname Requirements](m_appliance_overview.html#Cisco_Reference.dita_196c5c81-10b1-4bef-a3de-39375a05a75e). 
  * Setting up a multi-node for advantage tier metrics data collection in Intersight Virtual Appliance (two-node cluster) requires an IPv4 address and 2 DNS records for that IP address for the single-node (appliance management node) and requires an IPv4 address and one DNS record for that IP address for the metrics node. For more information about IP addresses and Hostname requirements, see [IP Address and Hostname Requirements](m_appliance_overview.html#Cisco_Reference.dita_196c5c81-10b1-4bef-a3de-39375a05a75e). 
  * Setting up a multi-node cluster for high availability in Intersight Virtual Appliance requires three hostnames, three IP addresses, and one DC-CNAME for each hostname. For more information about IP addresses and Hostname requirements, see [IP Address and Hostname Requirements](m_appliance_overview.html#Cisco_Reference.dita_196c5c81-10b1-4bef-a3de-39375a05a75e). 
  * Setting up a multi-node for advantage tier metrics data collection in Intersight Virtual Appliance (four-node cluster) requires three hostnames, three IP addresses, and one DC-CNAME for each hostname for the HA management cluster. It also requires an IPv4 address and one DNS record for that IP address for the metrics node. For more information about IP addresses and Hostname requirements, see [IP Address and Hostname Requirements](m_appliance_overview.html#Cisco_Reference.dita_196c5c81-10b1-4bef-a3de-39375a05a75e). 
  * Use only HTTPS protocol and fully qualified domain name to access the appliance via the Web user interface.


* * *  
  
---|---  
  
### Procedure

* * *

**Step 1** |  Log in to VMware vSphere Web Client with administrator credentials.  
---|---  
**Step 2** |  Right-click on the appropriate vCenter object (datacenter, cluster or ESXi host), and select Deploy OVF Template.   
**Step 3** |  On the Deploy OVF Template wizard Select template page, specify the source location, and click Next. You can specify a URL or browse to any accessible location..   
**Step 4** |  On the OVF Template Details page, verify the OVF template details and click Next. No input is necessary.   
**Step 5** |  On the Select a name and location page, add/edit the Name and Location for the Virtual appliance and click Next.   
**Step 6** |  On the Select a resource page, select the specific Host  (ESX station), Cluster, or Resource Pool on which you want to deploy and click Next.  Each VM must be assigned to a specific host on clusters that are configured with vSphere HA or Manual mode vSphere DRS.  
**Step 7** |  On the Review details page, verify the OVA template details and click Next.   
**Step 8** |  On the Configuration page, select a deployment configuration and click Next.   
**Step 9** |  On the Select storage page, select a destination storage for the VM files in the selected ESX host and click Next. Select the Disk Format for the virtual machine virtual disks.  Cisco recommends that you use thick provisioning. While it is possible to use thin provisioning, over-commitment of storage can lead to a lack of storage capacity resulting in degradation and loss of service and might require a restore from backup.   
**Step 10** |  On the Select networks page, select a source network and map it to a destination network, and click Next.   
**Step 11** |  On the Customize Template page, customize the deployment properties of the OVF template, and click Next.  |  OVF Property |  Description  
---|---  
Enable DHCP (only for single-node appliance) |  Enables the appliance to obtain IP addresses from the DHCP server running on the same network to avoid using static IP addresses. If you select this option, all static parameters will be ignored. For more information about DHCP, see the Enabling DHCP section after this table.   
Appliance FQDN _(Values you input will be ignored if you Enable DHCP)_ |  Enter the Appliance’s fully qualified domain name (FQDN). For example: _appliance.example.com_  
IP Address(Values you input will be ignored if you Enable DHCP) |  Enter the IPv4 address of the node. For example: 10.0.0.100  
Net Mask(Values you input will be ignored if you Enable DHCP) |  This field is pre-populated with the IPv4 Net Mask 255.255.255.0  
Default Gateway(Values you input will be ignored if you Enable DHCP) |  Enter the IPv4 Default Gateway. For example: 10.0.1.254  
DNS Domain(Values you input will be ignored if you Enable DHCP) |  Enter the DNS Search Domain.  
DNS Servers(Values you input will be ignored if you Enable DHCP) |  Enter a comma-separated list of IPv4 addresses for your DNS servers. A maximum of two DNS servers are supported.  
Admin Password |  Enter the admin password. This is the same password that you use to log in to the appliance. Set Password—Before you register the appliance with Intersight, you must create an admin password. The password can contain 0-9, A-Z, a-z, and all special characters except a colon (:) and space.   
NTP Servers |  Enter a comma-separated list of hostnames or IPv4 addresses for your NTP servers. You may add up to three unauthenticated NTP servers at this stage. Once the appliance is fully installed, you can edit the NTP server settings to include any combination of authenticated and unauthenticated NTP servers (up to three total). This setting is required even if you use DHCP to obtain IP addresses.   
Disk Size |  Attention: Do not change the value of the disk size as it is computed based on the deployment configuration.   
**Attention** |  **If the password you set at the time of registering your appliance is weak, Intersight prompts you to change your password to a stronger one. After a successful reset to a strong password, you are directly logged into the appliance. For more information about logging in, see[Logging In to Intersight Virtual Appliance](m_setting_up_appliance.html#id_93446)**.   
---|---  
  
Enabling DHCP

Dynamic Host Configuration Protocol (DHCP) allows the Cisco Intersight Virtual Appliance VM to obtain an IP address through a DHCP server running on the network that it is installed on. When this option is enabled, the Cisco Intersight Virtual Appliance is equipped to handle IP address updates through DHCP, subject to lease requirements. 

**Attention** |  DHCP is not supported on multi-node Intersight Virtual Appliance. For a single-node appliance, ensure that the following requirements are met for using DHCP:  
---|---  
  
  * If you use DHCP, ensure that the IP address returned to the appliance VM resolves to the same FQDN you use to set up the appliance. Cisco strongly recommends configuring DHCP to assign a static IP address to the Appliance VM. Although the Appliance can handle changes when its DHCP lease is renewed, it operates more efficiently—especially when communicating with claimed devices—if its IP address remains constant. 

  * The appliance only reads the IP address, netmask, gateway, and DNS-Servers from the DHCP lease information. NTP information is mandatory and must be input into the OVF parameters at the time of deployment. 


Limitations

  * Frequent lease renewal could impact the VM configuration settings and could render the appliance unusable.


  
**Step 12** |  On the Ready to Complete page, select Power On After Deployment and click Finish.   
**Step 13** |  Proceed to <https://fqdn-of-your-appliance> to complete the post-install set-up of your appliance.  For information on how to complete the set-up of your appliance, see [Setting Up Intersight Virtual Appliance](m_setting_up_appliance.html#Cisco_Task_in_List_GUI.dita_266a2c35-69a4-4a04-89c2-b9c0339b905a).   
  
* * *

Troubleshooting Tip: After providing the OVF parameters, if you notice that your VM does not respond when you visit <https://fqdn-of-your-appliance> after about 15 minutes since power-on, you may use the Intersight Appliance Maintenance Shell to troubleshoot networking or misconfiguration issues. 

Troubleshooting Tip: If the diag shell displays a hostname such as 192:, then it is possible that while deploying the appliance, the input for one or more network parameters (such as IP address, netmask, gateway, DNS servers, etc.) was entered incorrectly. It is also possible that the appliance VM is connected to a portgroup/vswitch that does not allow it to connect to the network and perform a successful DNS lookup. If you encounter this issue, check the inputs to the OVA as well as other network parameters. You can rectify the incorrect inputs using the maintenance shell. 

The diagnostic tool aims to:

  * Detect and display issues with the installation prerequisites.

  * Enable editing the inputs that are provided during OVA deployment. 

  * Assist with continuing the installation after you fix the settings, or set network interface properties such as IP addresses, subnet mask, and default gateway during the OVA deployment. 


For more information, see [Maintenance Shell for Intersight Virtual Appliance and Intersight Assist](m_troubleshooting.html#reference_fjp_2qs_shb) and [Intersight Virtual Appliance Console UI](m_troubleshooting.html#intersight-virtual-appliance-console-ui). 

For a demonstration of the Intersight Virtual Appliance Installation and troubleshooting, watch [Cisco Intersight Appliance Installation and Debug](https://www.youtube.com/watch?v=vHoDfixdi4g&feature=youtu.be). 

---

## Page 6: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide/m_updating_the_intersight_virtual_appliance_software.html

## Intersight Virtual Appliance 1.1.0-0 Upgrade Behavior — Impact of CentOS 7 to AlmaLinux 9 Migration

Starting with Intersight Virtual Appliance Release Version 1.1.0-0, the underlying operating system is AlmaLinux 9.

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

It is highly recommended that you take a snapshot of the appliance VM as well as a backup of the appliance before you start the upgrade process. 

* * *  
  
---|---  
  
The following information highlights the key aspects of this migration:

  * Starting with Intersight Virtual Appliance Release Version 1.1.0-0, all new Appliance and Assist installations will be based on AlmaLinux 9. 

  * Existing Appliance and Assist installations on version 1.0.9-631 or later that upgrade to version 1.1.0-0 or later will upgrade in-place to AlmaLinux 9. 

  * Upgrading to version 1.1.0-0 directly from version 1.0.9-615 or older will fail. Therefore, while upgrading to version 1.1.0-0 from version 1.0.9-615 or older, do the following: 

  * Ensure that the appliance meets the disk requirements. For more information, see [Resource Requirements](m_appliance_overview.html#Cisco_Reference.dita_a6ea1ddc-e212-4367-9579-e9320b64f1b5). 

  * Upgrade to one of the following versions before upgrading to version 1.1.0-0.

  * 1.0.9-631

  * 1.0.9-655

  * 1.0.9-675

  * 1.0.9-677

  * **Three-node cluster deployment** —If your three-node cluster deployment runs appliance version 1.0.9-631, upgrade to version 1.0.9-675 before updating to version 1.1.0-0 or 1.1.1-0. 

  * When an existing Appliance or Assist upgrades to version 1.1.0-0, expect the following behavior: 

  * The upgrade will take at least 4 hours to complete and will reboot multiple times.

  * The Appliance web UI, REST API, and CLI interfaces may not be available. You can monitor the progress of the upgrade on the VM console. 

  * It is STRONGLY RECOMMENDED that you DO NOT manually reboot the Appliance or Assist VM during the upgrade process as it may damage the VM and potentially disrupt the upgrade process. 

  * Installation and upgrade bundle sizes for release version 1.1.0-0 are larger than the ones for the previous releases due to the switch to AlmaLinux. 


---

## Page 7: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide/m_settings_dashboard.html

## Configuring a Banner Message for Displaying Before the Login Screen

You can configure a banner message in Intersight Virtual Appliance. When enabled, the configured banner message will be displayed before the user login screen. 

### Procedure

* * *

**Step 1** |  Log into Intersight Virtual Appliance as a user with account administrator role.  
---|---  
**Step 2** |  Choose Settings > System > Banners.   
**Step 3** |  Click Configure.  The Configure Banner Message window displays.   
**Step 4** |  Update the following fields.

  * Show banner message before login—Enable this option. 
  * Banner Title—Enter a title for the banner message. The length of the title cannot exceed 128 characters. 
  * Banner Content—Enter the content for the banner message. The content in this field has to be less than 2000 characters. 

  
**Step 5** |  Click Save.  The configured banner message content along with the title is displayed in the Banners preview window.   
  
* * *

---

## Page 8: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide/m_troubleshooting.html

## Maintenance Shell for Intersight Virtual Appliance and Intersight Assist

Cisco Intersight Virtual Appliance provides a diagnostic utility to monitor the installation and provide remediation steps to install the appliance successfully. This console-based utility helps in troubleshooting and addressing misconfiguration or networking issues during the appliance installation. The Maintenance Shell aims to: 

  * Detect and display issues with the installation prerequisites. 

  * Enable editing the inputs that are provided during the initial appliance deployment. 

  * Assist with continuing the installation after you fix the settings or change inputs during the appliance deployment.


Check the status of your installation by visiting <https://fqdn-of-your-appliance> after the VM is powered ON. If you notice that your VM does not respond after about 15 minutes since power-on, use the Intersight Virtual Appliance Maintenance Shell to troubleshoot networking or misconfiguration issues. When the login prompt appears, the diagnostic account is ready. Use the following instructions to troubleshoot: 

  1. Launch the Intersight Virtual Appliance Maintenance Shell using one of the following three options:

  * **Open an SSH session**

       1. SSH to the IP address of your Intersight Virtual Appliance.

       2. Log in as the admin user with username admin and enter the administrator password that you used during the appliance deployment. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The use of SHA-1 for any cryptographic functionality in SSH is no longer supported.

* * *  
  
---|---  
  * **Open a console window in your hypervisor**

       1. From either VMWare vCenter or Microsoft Hyper-V Manager, navigate to your virtual machine and open a console window.

       2. Hit Alt-F2 to get the login screen.

       3. Log in as the admin user with username admin and enter the administrator password that you used during the appliance deployment. 

  * **Open a telnet session to a serial console**

       1. In cases where opening an SSH session to the Intersight Virtual Appliance is not possible, use the information described in [Configuring Cisco TAC Support Using a Serial Console](m-technical-assistance.html#Cisco_Reference.dita_b2778427-6c95-45f4-a027-a88c2a6aac0a) to add a serial console to your Intersight Virtual Appliance VM. 

       2. Telnet to the vCenter host IP at the PORT_NUMBER specified in the serial console setup. 

       3. Log in as the admin user with username admin and enter the administrator password that you used during the appliance deployment. 

  2. Select one of the options listed in the following table to learn more about the command and the outcome of the command: 


Intersight Appliance Maintenance Shell Options |  Description  
---|---  
Diagnostic Options | 

  * [1] Ping a Host—This option lets you ping a host to check why the installation is unsuccessful even after all properties and requirements are entered correctly. 
  * [2] Traceroute a host—This option displays all IP addresses that the host has traversed through. 
  * [3] Run connectivity test—This option runs a connectivity test and pings every host in the path from your host to the DNS server. The tool runs a few tests to verify if the IP address is valid, and checks for duplicate IPs to determine if it is used in multiple instances. The Run connectivity test option reaches the DNS server to resolve any connectivity issues. 

  
Configuration Options | 

  * [a] Show current network configuration—This option displays the existing configuration settings such as IP address, subnet mask, Default Gateway, DNS servers, Hostname, and NTP connection status to help you verify that all configuration settings are entered correctly. You can run the connectivity test (Option 3) to determine the status of the connectivity. ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472762.jpg) ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309381.jpg)
  * [b] Set network interface properties—This option displays the network interface properties that you have set. You can click enter to retain the existing properties or provide a different set of inputs. This option detects issues (if any) with the following properties: 
  * An invalid or duplicate IP address—The IP address could be incorrect even if you have configured your hostname with the correct credentials. 
  * Invalid subnet mask—An invalid subnet mask might allow you to navigate inside your own network, but could impact external traffic. 
  * Incorrect or invalid Default Gateway—If the DNS server is outside your network, an invalid default gateway impacts the connectivity to external hosts.  **Changing IP Address** —Using this option, an **admin** user (with username admin) can make the following changes: 
  * Assign a new IP address on the same network, connect the appliance VM to a different network and assign an IP on that network.
  * Change the IP address of an appliance VM after migrating it to a different vCenter or Hyper-V Manager deployment.  |  **Attention** |  You must ensure that the DNS server records (A and CNAME) are updated before the change is initiated and the new IP address resolves to the same FQDN as before.  You can choose to change either just the IPv4 address or the IPv6 address, or change both at the same time. Note that the appliance VM itself continues to be managed with the DNS name assigned to the IPv4 address of the appliance when it was first deployed. When you configure IPv6 addresses, it enables only the target claim of IPv6 endpoints.  The IP change can take up to 15 minutes. Cisco recommends that you do not reboot the appliance VM during this time. After waiting for about 15 minutes, log back into the appliance from the UI.   
---|---  
![](/c/dam/en/us/td/i/300001-400000/300001-310000/307001-308000/307807.jpg) ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309028.jpg)
  * For Multi-Node setup Only: For more information on how to change IPv4 address for a node in a multi-node cluster, see [Changing IPv4 Address of HA Management Nodes in the Multi-Node Cluster](m_setting_up_appliance.html#change-ipv4-address-in-multinode-clusters) and[ Changing IPv4 Address of Metrics Node in the Multi-Node Cluster](m_setting_up_appliance.html#changing-ipv4-for-metrics-node). 

  * [c] Restart installation services 

This option is useful when you fix the configuration on your network that was previously assumed to be working. A few examples are: 

  * VM connected to incorrect portgroup/vSwitch.

  * DHCP server not running when you chose an IP assignment via DHCP.

  * You can check the progress of the installation by visiting the url <fqdn-of-your-appliance-vm>. 

  * [d] Run Debug (requires authentication)—This utility is intended only for Cisco TAC to troubleshoot installation issues. 

  * [e] Configure Logon Banner—This option enables you to configure a new banner message or edit an existing one to be displayed before the login screen. 

  * [f] Generate and upload tech support—This option enables you to generate and upload tech support bundles. 

  * [g] Manage SSL Certificate—[**For Intersight Assist Only**] This option allows you to view certificate details, use a self-signed certificate, view or generate a Certificate Signing Request (CSR), and upload a signed certificate. 


  
Maintenance Options |  **Options in this sub-menu are intended for debugging and recovery and must be used as instructed by Cisco TAC**. You can access this option as an **admin** user.  [4] Show system service status—This option provides a summary of the running/pending services and reports any errors. This option enables you to monitor the status of the appliance if the system is unresponsive or if there is a service disruption at any time.  [5] Restart system services—This option enables you to troubleshoot the appliance and restart the services running on it.  [6] Reboot virtual appliance node—This option stops services, reboots the appliance, and restores the services when the appliance reboots.  [7] Show node status—This option displays the fully qualified domain name of the appliance VM and their operational status.  [8] Launch console UI—This option enables you to launch the console UI from the maintenance shell.  [9] Shutdown appliance node—This option gracefully stops services and shuts down the appliance node from the maintenance shell.  [10] Read-only maintenance shell—This option launches a Linux bash shell in a primarily read-only environment. You cannot make changes to the Appliance from this shell, but you can perform read-only diagnostic actions to validate the appliance within your network environment. Common Linux commands such as curl, wget, dig, nslookup, ssh, scp, ping, and traceroute are available to help troubleshoot local networking issues.   
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For [10] Read-only maintenance shell, tcpdump command is not directly available. Use the public-tcpdump command instead. To save packet captures, run public-tcpdump -w FILENAME.pcap to write PCAP files to your home directory, which you can then transfer to another machine for analysis using scp.  **Relevant Log Files:**

  * /var/log/ansible—Install and upgrade logs
  * /var/log/andro—Service logs from the application
  * /var/log/equinox—Device connector and first service to start


* * *  
  
---|---  
  
For a demonstration of the Intersight Connected Virtual Appliance Installation and troubleshooting, watch [Cisco Intersight Appliance Installation and Debug](https://www.youtube.com/watch?v=Uj_9wIX-vGU). 

### Monitoring Virtual Appliance Sizing Option Messages

The Intersight Appliance Maintenance Shell displays the status updates about the deployment size determination and the subsequent action. You can monitor the status of the deployment in the console and take remedial actions as required. The messages listed in the table below explain the scenario and the particular resource requirements for deployment. 

Initial Message |  Final Message  
---|---  
Deploying <size> deployment size. This message is displayed when the required resources are adequate, and the desired size is being deployed.  |  **Note** |  After evaluating the resources requirement, you can choose to deploy in small, medium, or large configurations.  
---|---  
Deployed <size> deployment size.  
Deploying <size > deployment size, after being under resourced. This message is displayed when the existing deployment is under-resourced for the current deployment size, and upon restarting the VM after the necessary resources have been added. This deployment could be in either size.  |  Deployed <size> deployment size, after being under resourced.  
Deployed <size> deployment size. This message is displayed when the existing resources and the required resources are similar, and no upgrade is required. |  No change in deployment size during reboot. Current running deployment size is Small.  
Downgrading deployment size from Medium to Small. This message is deployed when a medium deployment size is downgraded to a small deployment size. |  Downgraded deployment size from Medium to Small.  
Upgrading from Small to Medium. This message is displayed when the deployment size is upgraded from small to medium deployment size. |  Upgraded from Small to Medium.

---

## Page 9: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide/m-technical-assistance.html

## Technical Assistance   
  
Technical support offered by Cisco Technical Assistance Center (TAC) is included in your Intersight License. If you face any issue with the installation, set up, or operations of Cisco Intersight Virtual Appliance, open a case with Cisco TAC for assistance. 

The Cisco Technical Support website provides online documents and tools for troubleshooting and resolving technical issues with Cisco products and technologies: 

<https://www.cisco.com/c/en/us/support/index.html>

Using the TAC Support Case Manager online tool is the fastest way to open S3 and S4 support cases. (S3 and S4 support cases consist of minimal network impairment issues and product information requests.) After you describe your situation, the TAC Support Case Manager automatically provides recommended solutions. If your issue is not resolved by using the recommended resources, TAC Support Case Manager assigns your support case to a Cisco TAC engineer. You can access the TAC Support Case Manager from this location: 

<https://mycase.cloudapps.cisco.com/case>

For S1 or S2 support cases or if you do not have Internet access, contact the Cisco TAC by telephone. (S1 or S2 support cases consist of production network issues, such as a severe degradation or outage.) S1 and S2 support cases have Cisco TAC engineers assigned immediately to ensure your business operations continue to run smoothly. 

To open a support case by telephone, use one of the following numbers:

· Asia-Pacific: +61 2 8446 7411

· Australia: 1 800 805 227

· EMEA: +32 2 704 5555

· USA: 1 800 553 2447

For a complete list of Cisco TAC contacts for Enterprise and Service Provider products, see <https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html> . 

For a complete list of Cisco Small Business Support Center (SBSC) contacts, see <https://www.cisco.com/c/en/us/support/web/tsd-cisco-small-business-support-center-contacts.html>. 

### Opening a TAC Case directly from Intersight Virtual Appliance

After completing your setup and claiming a target, you can create a Cisco TAC Service Request (SR) directly from Cisco Intersight Virtual Appliance. 

Before you open a case, ensure that the following requirements are met: 

  * A valid service contract (entitlement) exists.

  * Your Cisco ID is associated with the service contract.


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Your browser must be connected to the internet so that you can access Cisco Technical Assistance Center (TAC) and create a service request. 

* * *  
  
---|---  
  
To open a Cisco TAC case directly from Cisco Intersight Virtual Appliance:

  1. Navigate to the Help Icon and click I Need Support. 

The Open TAC Case pop-up window displays. 

  2. Select a support topic from the drop-down list. 

  3. Click Open TAC Case to launch [Cisco Support Case Manager](https://mycase.cloudapps.cisco.com/case). 

  4. In the Cisco Support Case Manager UI, verify the auto-populated details of your case, add a description and a title for your TAC Case, and click Submit. 


### Collecting a Tech Support Bundle from Intersight Virtual Appliance

After completing your appliance setup and claiming a target, you can collect a tech support bundle for Intersight Virtual Appliance as well as for target claimed into the appliance and attach it to your Cisco TAC Service Request (SR). You can collect tech support bundles from Cisco UCS Fabric Interconnects and connected UCS B, C, S Series Servers, Cisco UCS C-Series Standalone Servers, Cisco UCS X-Series Servers, Cisco HyperFlex Clusters, and Cisco UCS Director. 

**To collect tech support bundles for targets claimed into your Appliance, do the following:**

  1. Log into the Appliance as a user with one of the following roles:

  * Account administrator

  * Server administrator

  * HyperFlex administrator

  2. From the Appliance dashboard, navigate to the target for which you want to collect a tech support bundle.

  * In the case of **Servers** , **Fabric Interconnects** , and **UCS Director** , click the ellipsis (**...**) button for your selection and then select Collect Tech Support Bundle. 

  * In the case of **HyperFlex Clusters** , after selecting a cluster and a corresponding node for the cluster, click the ellipsis (**...**) button for your selection and then select Collect Tech Support Bundle. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

You may have to provide tech support bundles for all the nodes in the cluster while creating a service request in Cisco Technical Assistance Center (TAC). 

* * *  
  
---|---  
  3. Choose System > Tech Support Bundles and download your tech support bundle for the target after the generation is complete. 


**To collect a tech support bundle for your Appliance, do the following:**

  1. Log into the Appliance as a user with an administrative role.

  2. Choose System > Tech Support Bundles. 

  3. Click Collect Appliance Tech Support Bundle on the Tech Support Bundle page. 

You can download the tech support bundle for your appliance after the generation is complete.


You can now proceed to [Cisco Support Case Manager](https://mycase.cloudapps.cisco.com/case) and create a service request. 

---

## Page 10: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide/m_related_documentation.html

## Links to Related Documentation

  * Cisco Intersight provides a cloud-based RESTful API to manage Cisco UCS and Cisco HyperFlex systems across multiple Data Centers. To learn more about the Intersight API, see [API Docs](https://intersight.com/apidocs). 

  * Learn more about the Faults and Alarms in Intersight:

  * [UCS Faults and Error Messages](https://www.cisco.com/c/en/us/support/servers-unified-computing/unified-computing-system/products-system-message-guides-list.html)

  * [HyperFlex HX Data Platform Events](https://www.cisco.com/c/en/us/td/docs/hyperconverged_systems/HyperFlex_HX_DataPlatformSoftware/HX_TroubleshootingGuide/3_5/b_HyperFlexSystems_TroubleshootingGuide_3_5/b_HyperFlexSystems_TroubleshootingGuide_3_0_chapter_011.html#reference_y1m_bnm_wbb)


For more information about Enabling Intersight Management on the Management Interfaces, see the appropriate guide listed below:

  * [Cisco UCS Manager Administration Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Admin-Management/3-2/b_Cisco_UCS_Admin_Mgmt_Guide_3_2/b_Cisco_UCS_Admin_Mgmt_Guide_3_2_chapter_010000.html?bookSearch=true)

  * [Cisco UCS C-Series Integrated Management Controller GUI Configuration Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/c/sw/gui/config/guide/3_1/b_Cisco_UCS_C-series_GUI_Configuration_Guide_31/b_Cisco_UCS_C-series_GUI_Configuration_Guide_31_chapter_010001.html?bookSearch=true#task_D1C22EDEC0BA41A59475EDA920AB6B13)

  * [Cisco HyperFlex Systems Installation Guide for Cisco Intersight](https://www.cisco.com/c/en/us/td/docs/hyperconverged_systems/HyperFlex_HX_DataPlatformSoftware/HyperFlex_Installation_Guide_for_Intersight/b_HyperFlex_Installation_Guide_for_Intersight/b_HyperFlex_Installation_Guide_for_Intersight_chapter_011.html?bookSearch=true)


---

## Page 11: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide/b_Cisco_Intersight_Appliance_Getting_Started_Guide_chapter_01000.html

## Maintenance Shell for Intersight Virtual Appliance and Intersight Assist

Cisco Intersight Virtual Appliance provides a diagnostic utility to monitor the installation and provide remediation steps to install the appliance successfully. This console-based utility helps in troubleshooting and addressing misconfiguration or networking issues during the appliance installation. The Maintenance Shell aims to: 

  * Detect and display issues with the installation prerequisites. 

  * Enable editing the inputs that are provided during the initial appliance deployment. 

  * Assist with continuing the installation after you fix the settings or change inputs during the appliance deployment.


Check the status of your installation by visiting <https://fqdn-of-your-appliance> after the VM is powered ON. If you notice that your VM does not respond after about 15 minutes since power-on, use the Intersight Virtual Appliance Maintenance Shell to troubleshoot networking or misconfiguration issues. When the login prompt appears, the diagnostic account is ready. Use the following instructions to troubleshoot: 

  1. Launch the Intersight Virtual Appliance Maintenance Shell using one of the following three options:

  * **Open an SSH session**

       1. SSH to the IP address of your Intersight Virtual Appliance.

       2. Log in as the admin user with username admin and enter the administrator password that you used during the appliance deployment. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The use of SHA-1 for any cryptographic functionality in SSH is no longer supported.

* * *  
  
---|---  
  * **Open a console window in your hypervisor**

       1. From either VMWare vCenter or Microsoft Hyper-V Manager, navigate to your virtual machine and open a console window.

       2. Hit Alt-F2 to get the login screen.

       3. Log in as the admin user with username admin and enter the administrator password that you used during the appliance deployment. 

  * **Open a telnet session to a serial console**

       1. In cases where opening an SSH session to the Intersight Virtual Appliance is not possible, use the information described in [Configuring Cisco TAC Support Using a Serial Console](m-technical-assistance.html#Cisco_Reference.dita_b2778427-6c95-45f4-a027-a88c2a6aac0a) to add a serial console to your Intersight Virtual Appliance VM. 

       2. Telnet to the vCenter host IP at the PORT_NUMBER specified in the serial console setup. 

       3. Log in as the admin user with username admin and enter the administrator password that you used during the appliance deployment. 

  2. Select one of the options listed in the following table to learn more about the command and the outcome of the command: 


Intersight Appliance Maintenance Shell Options |  Description  
---|---  
Diagnostic Options | 

  * [1] Ping a Host—This option lets you ping a host to check why the installation is unsuccessful even after all properties and requirements are entered correctly. 
  * [2] Traceroute a host—This option displays all IP addresses that the host has traversed through. 
  * [3] Run connectivity test—This option runs a connectivity test and pings every host in the path from your host to the DNS server. The tool runs a few tests to verify if the IP address is valid, and checks for duplicate IPs to determine if it is used in multiple instances. The Run connectivity test option reaches the DNS server to resolve any connectivity issues. 

  
Configuration Options | 

  * [a] Show current network configuration—This option displays the existing configuration settings such as IP address, subnet mask, Default Gateway, DNS servers, Hostname, and NTP connection status to help you verify that all configuration settings are entered correctly. You can run the connectivity test (Option 3) to determine the status of the connectivity. ![](/c/dam/en/us/td/i/400001-500000/470001-480000/472001-473000/472762.jpg) ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309381.jpg)
  * [b] Set network interface properties—This option displays the network interface properties that you have set. You can click enter to retain the existing properties or provide a different set of inputs. This option detects issues (if any) with the following properties: 
  * An invalid or duplicate IP address—The IP address could be incorrect even if you have configured your hostname with the correct credentials. 
  * Invalid subnet mask—An invalid subnet mask might allow you to navigate inside your own network, but could impact external traffic. 
  * Incorrect or invalid Default Gateway—If the DNS server is outside your network, an invalid default gateway impacts the connectivity to external hosts.  **Changing IP Address** —Using this option, an **admin** user (with username admin) can make the following changes: 
  * Assign a new IP address on the same network, connect the appliance VM to a different network and assign an IP on that network.
  * Change the IP address of an appliance VM after migrating it to a different vCenter or Hyper-V Manager deployment.  |  **Attention** |  You must ensure that the DNS server records (A, CNAME, and PTR) are updated before the change is initiated and the new IP address resolves to the same FQDN as before.  You can choose to change either just the IPv4 address or the IPv6 address, or change both at the same time. Note that the appliance VM itself continues to be managed with the DNS name assigned to the IPv4 address of the appliance when it was first deployed. When you configure IPv6 addresses, it enables only the target claim of IPv6 endpoints.  The IP change can take up to 15 minutes. Cisco recommends that you do not reboot the appliance VM during this time. After waiting for about 15 minutes, log back into the appliance from the UI.   
---|---  
![](/c/dam/en/us/td/i/300001-400000/300001-310000/307001-308000/307807.jpg) ![](/c/dam/en/us/td/i/300001-400000/300001-310000/309001-310000/309028.jpg)
  * For Multi-Node setup Only: For more information on how to change IPv4 address for a node in a multi-node cluster, see [Changing IPv4 Address of HA Management Nodes in the Multi-Node Cluster](b_Cisco_Intersight_Appliance_Install_and_Upgrade_Guide_chapter_01.html#change-ipv4-address-in-multinode-clusters) and[ Changing IPv4 Address of Metrics Node in the Multi-Node Cluster](b_Cisco_Intersight_Appliance_Install_and_Upgrade_Guide_chapter_01.html#changing-ipv4-for-metrics-node). 

  * [c] Restart installation services 

This option is useful when you fix the configuration on your network that was previously assumed to be working. A few examples are: 

  * Missing PTR record for the IP you have chosen (static IP assignment).

  * VM connected to incorrect portgroup/vSwitch.

  * DHCP server not running when you chose an IP assignment via DHCP.

  * You can check the progress of the installation by visiting the url <fqdn-of-your-appliance-vm>. 

  * [d] Run Debug (requires authentication)—This utility is intended only for Cisco TAC to troubleshoot installation issues. 

  * [e] Configure Logon Banner—This option enables you to configure a new banner message or edit an existing one to be displayed before the login screen. 

  * [f] Generate and upload tech support—This option enables you to generate and upload tech support bundles. 


  
Maintenance Options |  **Options in this sub-menu are intended for debugging and recovery and must be used as instructed by Cisco TAC**. You can access this option as an **admin** user.  [4] Show system service status—This option provides a summary of the running/pending services and reports any errors. This option enables you to monitor the status of the appliance if the system is unresponsive or if there is a service disruption at any time.  [5] Restart system services—This option enables you to troubleshoot the appliance and restart the services running on it.  [6] Reboot virtual appliance node—This option stops services, reboots the appliance, and restores the services when the appliance reboots.  [7] Show node status—This option displays the fully qualified domain name of the appliance VM and their operational status.  [8] Launch console UI—This option enables you to launch the console UI from the maintenance shell.  [9] Shutdown appliance node—This option gracefully stops services and shuts down the appliance node from the maintenance shell.  [10] Read-only maintenance shell—This option launches a Linux bash shell in a primarily read-only environment. You cannot make changes to the Appliance from this shell, but you can perform read-only diagnostic actions to validate the appliance within your network environment. Common Linux commands such as curl, wget, dig, nslookup, ssh, scp, ping, and traceroute are available to help troubleshoot local networking issues.   
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For [10] Read-only maintenance shell, tcpdump command is not directly available. Use the public-tcpdump command instead. To save packet captures, run public-tcpdump -w FILENAME.pcap to write PCAP files to your home directory, which you can then transfer to another machine for analysis using scp.  **Relevant Log Files:**

  * /var/log/ansible—Install and upgrade logs
  * /var/log/andro—Service logs from the application
  * /var/log/equinox—Device connector and first service to start


* * *  
  
---|---  
  
For a demonstration of the Intersight Connected Virtual Appliance Installation and troubleshooting, watch [Cisco Intersight Appliance Installation and Debug](https://www.youtube.com/watch?v=Uj_9wIX-vGU). 

### Monitoring Virtual Appliance Sizing Option Messages

The Intersight Appliance Maintenance Shell displays the status updates about the deployment size determination and the subsequent action. You can monitor the status of the deployment in the console and take remedial actions as required. The messages listed in the table below explain the scenario and the particular resource requirements for deployment. 

Initial Message |  Final Message  
---|---  
Deploying <size> deployment size. This message is displayed when the required resources are adequate, and the desired size is being deployed.  |  **Note** |  After evaluating the resources requirement, you can choose to deploy in small, medium, or large configurations.  
---|---  
Deployed <size> deployment size.  
Deploying <size > deployment size, after being under resourced. This message is displayed when the existing deployment is under-resourced for the current deployment size, and upon restarting the VM after the necessary resources have been added. This deployment could be in either size.  |  Deployed <size> deployment size, after being under resourced.  
Deployed <size> deployment size. This message is displayed when the existing resources and the required resources are similar, and no upgrade is required. |  No change in deployment size during reboot. Current running deployment size is Small.  
Downgrading deployment size from Medium to Small. This message is deployed when a medium deployment size is downgraded to a small deployment size. |  Downgraded deployment size from Medium to Small.  
Upgrading from Small to Medium. This message is displayed when the deployment size is upgraded from small to medium deployment size. |  Upgraded from Small to Medium.

---

## Page 12: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide/b_Cisco_Intersight_Appliance_Install_and_Upgrade_Guide_chapter_00.html

## Installing Cisco Intersight Virtual Appliance and Intersight Assist on VMware vSphere  
  
Cisco Intersight Virtual Appliance is distributed as a deployable virtual machine contained in an Open Virtual Appliance (OVA) file format, ZIP file format, or a TAR file format. Cisco Intersight Virtual Appliance supports VMware High Availability (VMHA) to ensure non-disruptive operation of the virtual appliance. For more information about VMHA, please refer to the documentation on vmware.com.  ![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Attention** | 

* * *

Intersight Virtual Appliance and Intersight Assist OVA must be deployed using VMware vCenter. The OVA cannot be directly deployed on ESXi servers.  By default, VMware vCenter does not include a Certificate Authority (CA) that validates the Cisco digital signature on the Intersight Virtual Appliance OVA file. The VMware vCenter GUI will indicate that the OVA’s certificate is invalid and is not trusted. Although possible, it is recommended that you **_do not ignore this warning_** and proceed with the installation. Instead, download and install the appropriate root CA from the table below that will validate the digital signature on the Intersight Virtual Appliance OVA file. Validating the signature ensures that the OVA was both issued by Cisco and has not been modified by a 3rd party. 

* * *  
  
---|---  
  
The root CA certificates listed in the following table are available on [Cisco's PKI page](https://www.cisco.com/security/pki/codesign/). 

OVA version  |  CA Issuer  |  CA Serial Number  |  CA Expiration   
---|---|---|---  
1.1.0-0 and later |  TrustID EV Code Signing CA 4  |  40:01:7f:9e:01:04:d0:f0:da:98:8d:43:d8:97:43:03  |  March 18, 2030   
1.0.9-630  |  TrustID EV Code Signing CA 4  |  40:01:7f:9e:01:04:d0:f0:da:98:8d:43:d8:97:43:03  |  March 18, 2030   
1.0.9-588  |  DigiCert Trusted G4 Code Signing 2021 CA1  |  08:ad:40:b2:60:d2:9c:4c:9f:5e:cd:a9:bd:93:ae:d9  |  April 28, 2036  
1.0.9-499  |  None  |  None  |  None   
1.0.9-342  |  DigiCert Trusted G4 Code Signing 2021 CA1  |  08:ad:40:b2:60:d2:9c:4c:9f:5e:cd:a9:bd:93:ae:d9  |  April 28, 2036  
  
Use the steps in the following task to install and deploy the appliance on VMware vSphere. To install and deploy a multi-node cluster for high availability for Intersight Virtual Appliance on VMware vSphere, repeat the steps in the following task three times.

### Before you begin

Ensure that you have downloaded the latest Cisco Intersight Virtual Appliance software package from the Intersight Software Downloads Portal. For more information, see [Downloading Software Packages from Intersight Virtual Appliance.](b_Cisco_Intersight_Appliance_Install_and_Upgrade_Guide_chapter_01.html#Cisco_Task_in_List_GUI.dita_a1922fb8-cac5-42c4-90e1-8370efd7e7e5)

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Attention** | 

* * *

  * Before installing and setting up Intersight Virtual Appliance, it is strongly recommended that you read the information provided in the [System Requirements](b_Cisco_Intersight_Appliance_Getting_Started_Guide_chapter_0111.html#Cisco_Reference.dita_a6ea1ddc-e212-4367-9579-e9320b64f1b5) section. 
  * Setting up a single-node Intersight Virtual Appliance requires an IP address and two DNS records for that IP address. For more information about IP addresses and Hostname requirements, see [IP Address and Hostname Requirements](b_Cisco_Intersight_Appliance_Getting_Started_Guide_chapter_0111.html#Cisco_Reference.dita_196c5c81-10b1-4bef-a3de-39375a05a75e). 
  * Setting up a multi-node for advantage tier metrics data collection in Intersight Virtual Appliance (two-node cluster) requires an IPv4 address and 2 DNS records for that IP address for the single-node (appliance management node) and requires an IPv4 address and one DNS record for that IP address for the metrics node. For more information about IP addresses and Hostname requirements, see [IP Address and Hostname Requirements](b_Cisco_Intersight_Appliance_Getting_Started_Guide_chapter_0111.html#Cisco_Reference.dita_196c5c81-10b1-4bef-a3de-39375a05a75e). 
  * Setting up a multi-node cluster for high availability in Intersight Virtual Appliance requires three hostnames, three IP addresses, and one DC-CNAME for each hostname. For more information about IP addresses and Hostname requirements, see [IP Address and Hostname Requirements](b_Cisco_Intersight_Appliance_Getting_Started_Guide_chapter_0111.html#Cisco_Reference.dita_196c5c81-10b1-4bef-a3de-39375a05a75e). 
  * Setting up a multi-node for advantage tier metrics data collection in Intersight Virtual Appliance (four-node cluster) requires three hostnames, three IP addresses, and one DC-CNAME for each hostname for the HA management cluster. It also requires an IPv4 address and one DNS record for that IP address for the metrics node. For more information about IP addresses and Hostname requirements, see [IP Address and Hostname Requirements](b_Cisco_Intersight_Appliance_Getting_Started_Guide_chapter_0111.html#Cisco_Reference.dita_196c5c81-10b1-4bef-a3de-39375a05a75e). 
  * Use only HTTPS protocol and fully qualified domain name to access the appliance via the Web user interface.


* * *  
  
---|---  
  
### Procedure

* * *

**Step 1** |  Log in to VMware vSphere Web Client with administrator credentials.  
---|---  
**Step 2** |  Right-click on the appropriate vCenter object (datacenter, cluster or ESXi host), and select Deploy OVF Template.   
**Step 3** |  On the Deploy OVF Template wizard Select template page, specify the source location, and click Next. You can specify a URL or browse to any accessible location..   
**Step 4** |  On the OVF Template Details page, verify the OVF template details and click Next. No input is necessary.   
**Step 5** |  On the Select a name and location page, add/edit the Name and Location for the Virtual appliance and click Next.   
**Step 6** |  On the Select a resource page, select the specific Host  (ESX station), Cluster, or Resource Pool on which you want to deploy and click Next.  Each VM must be assigned to a specific host on clusters that are configured with vSphere HA or Manual mode vSphere DRS.  
**Step 7** |  On the Review details page, verify the OVA template details and click Next.   
**Step 8** |  On the Configuration page, select a deployment configuration and click Next.   
**Step 9** |  On the Select storage page, select a destination storage for the VM files in the selected ESX host and click Next. Select the Disk Format for the virtual machine virtual disks.  Cisco recommends that you use thick provisioning. While it is possible to use thin provisioning, over-commitment of storage can lead to a lack of storage capacity resulting in degradation and loss of service and might require a restore from backup.   
**Step 10** |  On the Select networks page, select a source network and map it to a destination network, and click Next.   
**Step 11** |  On the Customize Template page, customize the deployment properties of the OVF template, and click Next.  |  OVF Property |  Description  
---|---  
Enable DHCP (only for single-node appliance) |  Enables the appliance to obtain IP addresses from the DHCP server running on the same network to avoid using static IP addresses. If you select this option, all static parameters will be ignored. For more information about DHCP, see the Enabling DHCP section after this table.   
IP Address(Values you input will be ignored if you Enable DHCP) |  Enter the IPv4 address of the node. For example: 10.0.0.100  
Net Mask(Values you input will be ignored if you Enable DHCP) |  This field is pre-populated with the IPv4 Net Mask 255.255.255.0  
Default Gateway(Values you input will be ignored if you Enable DHCP) |  Enter the IPv4 Default Gateway. For example: 10.0.1.254  
DNS Domain(Values you input will be ignored if you Enable DHCP) |  Enter the DNS Search Domain.  
DNS Servers(Values you input will be ignored if you Enable DHCP) |  Enter a comma-separated list of IPv4 addresses for your DNS servers. A maximum of 2 DNS servers are supported.  
Admin Password |  Enter the admin password. This is the same password that you use to log in to the appliance. Set Password—Before you register the appliance with Intersight, you must create an admin password. The password can contain 0-9, A-Z, a-z, and all special characters except a colon (:) and space.   
NTP Servers |  Enter a comma-separated list of hostnames or IPv4 addresses for your NTP servers. You can add up to 3 NTP servers (any combination of authenticated and unauthenticated NTP servers). This setting is still required even if you use DHCP to obtain IP addresses.   
Disk Size |  Attention: Do not change the value of the disk size as it is computed based on the deployment configuration.   
**Attention** |  **If the password you set at the time of registering your appliance is weak, Intersight prompts you to change your password to a stronger one. After a successful reset to a strong password, you are directly logged into the appliance. For more information about logging in, see[Logging In to Intersight Virtual Appliance](b_Cisco_Intersight_Appliance_Install_and_Upgrade_Guide_chapter_01.html#id_93446)**.   
---|---  
  
Enabling DHCP

Dynamic Host Configuration Protocol (DHCP) allows the Cisco Intersight Virtual Appliance VM to obtain an IP address through a DHCP server running on the network that it is installed on. When this option is enabled, the Cisco Intersight Virtual Appliance is equipped to handle IP address updates through DHCP, subject to lease requirements. 

**Attention** |  DHCP is not supported on multi-node Intersight Virtual Appliance. For a single-node appliance, ensure that the following requirements are met for using DHCP:  
---|---  
  
  * If you use DHCP, ensure that the IP address returned to the appliance VM resolves to the same FQDN you use to set up the appliance. Cisco strongly recommends configuring DHCP to assign a static IP address to the Appliance VM. Although the Appliance can handle changes when its DHCP lease is renewed, it operates more efficiently—especially when communicating with claimed devices—if its IP address remains constant. 

  * The appliance only reads the IP address, netmask, gateway, and DNS-Servers from the DHCP lease information. NTP information is mandatory and must be input into the OVF parameters at the time of deployment. 


Limitations

  * Frequent lease renewal could impact the VM configuration settings and could render the appliance unusable.


  
**Step 12** |  On the Ready to Complete page, select Power On After Deployment and click Finish.   
**Step 13** |  Proceed to <https://fqdn-of-your-appliance> to complete the post-install set-up of your appliance.  For information on how to complete the set-up of your appliance, see [Setting Up Intersight Virtual Appliance](b_Cisco_Intersight_Appliance_Install_and_Upgrade_Guide_chapter_01.html#Cisco_Task_in_List_GUI.dita_266a2c35-69a4-4a04-89c2-b9c0339b905a).   
  
* * *

Troubleshooting Tip: After providing the OVF parameters, if you notice that your VM does not respond when you visit <https://fqdn-of-your-appliance> after about 15 minutes since power-on, you may use the Intersight Appliance Maintenance Shell to troubleshoot networking or misconfiguration issues. 

Troubleshooting Tip: If the diag shell displays a hostname such as 192:, then it is possible that while deploying the appliance, the input for one or more network parameters (such as IP address, netmask, gateway, DNS servers, etc.) was entered incorrectly. It is also possible that the appliance VM is connected to a portgroup/vswitch that does not allow it to connect to the network and perform a successful DNS lookup. If you encounter this issue, check the inputs to the OVA as well as other network parameters. You can rectify the incorrect inputs using the maintenance shell. 

The diagnostic tool aims to:

  * Detect and display issues with the installation prerequisites.

  * Enable editing the inputs that are provided during OVA deployment. 

  * Assist with continuing the installation after you fix the settings, or set network interface properties such as IP addresses, subnet mask, and default gateway during the OVA deployment. 


For more information, see [Maintenance Shell for Intersight Virtual Appliance and Intersight Assist](b_Cisco_Intersight_Appliance_Getting_Started_Guide_chapter_01000.html#reference_fjp_2qs_shb) and [Intersight Virtual Appliance Console UI](b_Cisco_Intersight_Appliance_Getting_Started_Guide_chapter_01000.html#intersight-virtual-appliance-console-ui). 

For a demonstration of the Intersight Virtual Appliance Installation and troubleshooting, watch [Cisco Intersight Appliance Installation and Debug](https://www.youtube.com/watch?v=vHoDfixdi4g&feature=youtu.be). 

---

## Page 13: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide/b_Cisco_Intersight_Appliance_Install_and_Upgrade_Guide_chapter_010.html

## Device Connector Requirements

You can claim a target in Cisco Intersight Virtual Appliance through the embedded device connector. Before you claim a target, ensure that the device connector requirements are met. The following table lists the software compatibility and the supported device connector versions for Intersight Virtual Appliance: 

Table 1. Device Connector Requirements Component |  Minimum software version for Connected Virtual Appliance |  Minimum software version for Private Virtual Appliance |  Supported Device Connector version  |  Minimum supported versions that include supported Device Connectors  
---|---|---|---|---  
Cisco UCS Manager |  3.2(1) |  4.0(2a) |  1.0.9-2290 |  4.0(2a)  
Cisco IMC Software |  For M5 Servers: 3.1(3a) For M4 Servers: 3.0(4) |  4.0(2d) |  1.0.9-335 |  4.0(2d)  
HyperFlex Connect and Data Platform |  2.6 |  3.5(2a)  |  1.0.9-1335 |  3.5(2a)  
CIsco UCS Director |  6.7.2.0 |  6.7.2.0 |  1.0.9-911 |  6.7.2.0  
  
### Device Connector Upgrade

When the Device Connector on an endpoint is not at the compatible version, you can upgrade it in the following ways: 

  * Perform a complete firmware upgrade to the version that has the supported Device Connector. This process could involve updating your configuration settings. 

  * Manually upgrade the Device Connector. This option is supported only on Cisco UCS Manager. For more information, See Manual Upgrade. 

  * Cisco Intersight Virtual Appliance supports upgrading the device connector from the cloud. When the target claim process detects that the device connector at the endpoint is not at the compatible version, it triggers an upgrade of the device connector from Intersight cloud. To facilitate this upgrade, port 80 must be open between the appliance and the endpoint target. The HTTPS proxy running on port 80 requires that your firewall settings allow communication through port 80. 

Device Connector upgrade from Intersight cloud is optional. During the upgrade from the cloud, some target data (server inventory) from the appliance leaves your premise. When you choose this option the following data leaves your premises: 

  * The endpoint target type - Cisco UCS Fabric Interconnect, Integrated Management Controller, Cisco HyperFlex System, Cisco UCS Director 

  * The firmware version(s) of the endpoint

  * The serial number(s) of the endpoint target

  * The IP address of the endpoint target

  * The hostname of the endpoint target

  * The endpoint device connector version and the public key 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Attention** | 

* * *

Target claim could fail if the device connector is at an older version that does not support the appliance, and you have disabled the data collection option during the initial setup. This failure is caused due to details about the endpoint being required to leave the premises for the one time upgrade to work. To avoid a target claim failure, select the Enable Data Collection option temporarily or upgrade the device connector in the other methods mentioned above. 

* * *  
  
---|---  


### Manual Upgrade of Device Connector (applicable only to Cisco UCS Fabric Interconnect)

If you do not want to share the target data as part of the automatic device connector upgrade, you can choose to manually upgrade the device connector on a Cisco UCS Fabric Interconnect. Use these instructions to upgrade the device connector: 
    
    
    Log in to your UCS Fabric Interconnect as an admin user and run the following command:
    UCS-A# connect local-mgmt
    UCS-A(local-mgmt)# copy scp://username@10.100.100.100/filepath/filename.bin workspace:/
    UCS-A(local-mgmt)# update-device-connector workspace:/filename.bin 
    Update Started
    Updating Device Connector on local Fabric interconnect
    Successfully updated device connector on local Fabric interconnect
    UCS-A(local-mgmt)#

---

## Page 14: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide/b_Cisco_Intersight_Appliance_Install_and_Upgrade_Guide_chapter_01.html

## Setting Up Single-Node Intersight Connected Virtual Appliance

Cisco Intersight Virtual Appliance is distributed as a deployable virtual machine contained in an Open Virtual Appliance (OVA) file format, ZIP file format, or TAR file format. 

Before You Begin: Ensure that you have installed Intersight Virtual Appliance software as per the instructions in [Installing Cisco Intersight Virtual Appliance and Intersight Assist on VMware vSphere](b_Cisco_Intersight_Appliance_Install_and_Upgrade_Guide_chapter_00.html#id_95741). 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

An appliance installer is required to restore the appliance from a backup. If a backup is taken from appliance release version N, it can only be restored using the latest installer that is less than or equal to version N. For example: 

  * If you backup your appliance release version 1.1.0-0, you need the latest appliance installer version that is less than or equal to 1.1.0-0, which is 1.1.0-0. 
  * If you backup your appliance release version 1.1.1-1, you need the latest appliance installer version that is less than or equal to 1.1.1-1, which is 1.1.1-0. 

Hence, it is recommended that you retain the required downloaded appliance installer for the backup that you are creating. For more information, see Recovering Intersight Connected Virtual Appliance. 

* * *  
  
---|---  
  
After the Cisco Intersight Virtual Appliance software deployment is complete, and the VM is powered on, access your VM using the <<https://your fqdn.com>> URL. The Intersight Appliance Installer screen appears and allows you to complete the setup for either a new install, recover the appliance software from backup, or add a node to the appliance. 

The wizard runs through a series of steps to download and install software packages. You can view the progress of the installation. 

Use the following instructions to complete the Intersight Connected Virtual Appliance setup:

### Procedure

* * *

**Step 1** |  On the Intersight Appliance Installer screen, select Install Connected Virtual Appliance and click Start.   
---|---  
**Step 2** |  Log in to the Intersight Virtual Appliance Connect page using your Cisco ID. If you do not have a Cisco ID, you can create one [here](https://id.cisco.com/ui/v1.0/profile-ui). 

  1. (Optional) Click Settings  to enable HTTPS Proxy Settings.  If an HTTP/S proxy is required to connect your Intersight Virtual Appliance to the internet, you must configure proxy settings before you complete the connection step. 
  * Click Settings and enable the HTTPS Proxy option. 
  * Add the Proxy Hostname or IP Address, and the Proxy Port.  The proxy port must be in the range between 1 and 65535. You can edit the Proxy settings from the appliance UI, Settings > Networking > Cloud Connection. 
  2. Use the Device ID and Claim Code  that is displayed on the Connect page to complete connecting to Intersight. 
  3. Ensure that the Connection status displays Claimed.  |  **Note** |  A new browser tab appears to display the status of the target claim in Intersight. If you do not have an Intersight account, you can create one in the Account Creation window and claim a target. If the target connection is successful, a success message is displayed. Click Close to exit the tab and return to the Intersight Appliance Installer setup wizard. If the target claim is unsuccessful, you will be taken to the Intersight login screen to restart target claim workflow.   
---|---  

  
**Step 3** |  In the Intersight Appliance Installer setup wizard, do the following: 

  1. Connect—Click Continue to proceed to the Check Network Requirements step. 
  2. Check Network Requirements—View the results and click Next to proceed to the Configure Internal Network step.  Note that if any of the DNS test fails during the network requirements check, you cannot proceed with the configuration.
  3. Configure Internal Network—If necessary, change the default Internal Network IP address and click Next to proceed to the Select Software Version step.  **Note:** This IP address range is used for internal communications within Intersight Virtual Appliance. This range must be within the 172.16.0.0/12 subnet, but can be a smaller range (up to a subnet prefix size of 20). In most cases, the default value can be used. One reason to change the default value would be if the Appliance needs to communicate directly with other devices in the same subnet, that is without traversing IP translation mechanisms such as NAT. 
  4. Select Software Version—You have the option to download the latest version of the appliance software, or upload a supported version of the appliance software that is either the same as, or newer than, the installer version. 


  1. To download the latest version of the appliance software, select the Download Latest Version button and click Finish to proceed to the Installation Result screen. 
  2. To upload a version of the appliance software, select either Local Machine or Network Share, depending on where you saved the software packages.  |  **Note** | 
  * To manually update, install, or restore Intersight Connected Virtual Appliance, you will need to access the Appliance Account so that you can download the required software packages. For information, see Creating an Appliance Account for Downloading Software Packages and Downloading Software Packages for Intersight Virtual Appliance. 
  * Select Intersight Appliance Software Bundle only. Intersight Appliance Patch Bundle cannot be used for new installations.   
---|---  
  * For Local Machine, browse to where you saved the software image, and then click Finish to proceed to the Installation Result screen. 

  * For the Network Share option, enter the protocol and enter details of the remote server from where you want to copy the file, and click Finish to proceed to the Installation Result screen. 

  * Protocol—Communication protocol used for file transfer. Intersight Virtual Appliance currently supports CIFS (Common Internet File System), SCP (Secure Copy Protocol) and SFTP (Secure File Transfer Protocol). 

  * Server IP/Hostname—The host server from where the file is copied 

  * Port—TCP port to use 

  * Location—Directory where the file to be copied is stored 

  * Software Bundle File Name for Appliance—Name of the file to be copied from the network share 

  * Username—Username for authenticating with the network share 

  * Password—Password for authenticating with the network share 

  3. Installation Results—You can view the progress of the installation on this screen. 


  
**Step 4** |  Specify Data Collection.  Specify your preference to allow Intersight to send additional system information to Cisco. This option is enabled by default. For more information about what data is collected by Intersight, see [Data Collected from Intersight Connected Virtual Appliance](b_Cisco_Intersight_Appliance_Install_and_Upgrade_Guide_chapter_0110.html#reference_wdb_3ss_4gb).   
**Step 5** |  Click Register License.  Obtain a license registration token from Cisco Smart License Manager and apply the token to activate your license. The license registration process could take a few minutes to complete. For more information about registering your Intersight license, watch [Cisco Intersight Licensing Tiers and Registration](https://intersight.com/help/video#cisco_intersight_licensing_tiers_and_registration).  After you click Finish, the Intersight Connected Virtual Appliance dashboard displays.   
  
* * *

### What to do next

Once you have successfully completed the initial set up of the single-node Intersight Virtual Appliance: 

  * You can add additional nodes to create a multi-node cluster for High Availability. For more information, see Configuring a Multi-Node Cluster for High Availability in Intersight Virtual Appliance. 

  * You can add a metrics node to create a multi-node cluster for advantage tier metrics data collection. For more information, see Configuring a Multi-Node Cluster for Increased Metrics Scalability in Intersight Virtual Appliance. 


---

## Page 15: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide/b_Cisco_Intersight_Appliance_Getting_Started_Guide_chapter_0111.html

## About Cisco Intersight Virtual Appliance

Cisco Intersight Virtual Appliance delivers the management features of Intersight in an easy to deploy VMware OVA, Microsoft Hyper-V Server VM, KVM hypervisor, and Nutanix AHV hypervisor. Intersight Virtual Appliance provides the benefits of Cisco Intersight that offers an intelligent level of management to enable customers to analyze, simplify, and automate their environments in more advanced ways than the previous generations of tools, while allowing more flexibility with additional data locality, security, and compliance requirements. 

You can deploy Intersight Virtual Appliance in one of the following modes:

  * Intersight Connected Virtual Appliance

  * Intersight Private Virtual Appliance

  * Intersight Assist


Intersight Connected Virtual Appliance delivers the management features of Intersight while allowing you to control what system details leave your premises. Intersight Connected Virtual Appliance deployments require a connection back to Cisco and Intersight services for automatic updates and access to services for full functionality. 

Intersight Private Virtual Appliance delivers the management features of Intersight and allows you to ensure that no system details leave your premises. Intersight Private Virtual Appliance deployments is intended for an environment where you operate data centers in a disconnected (air gapped) mode. 

For an overview of Intersight Assist, see About Cisco Intersight Assist. 

Deployment options available for Intersight Virtual Appliance are as follows:

  * You can deploy Intersight Virtual Appliance as a single-node virtual machine. In the standalone configuration, you can opt-in to enable the essential tier metrics data collection. For more information about the supported configuration, see Supported Configuration Limits for Intersight Virtual Appliance. For more information about data collection, see [Data Collection](https://intersight.com/help/appliance/monitoring/monitoring_data_collection#supported_devices). 

  * You can deploy Intersight Virtual Appliance on VMware vSphere as a multi-node cluster which allows for advantage tier metrics data collection. This deployment option is a two-node cluster that includes an appliance management node and a metrics node. Once you have completed the initial set up of the single-node appliance, you can add a metric node. For more information about configuring an advantage tier metrics node, see [Configuring a Multi-Node Cluster for Increased Metrics Scalability in Intersight Virtual Appliance](b_Cisco_Intersight_Appliance_Install_and_Upgrade_Guide_chapter_01.html#configuring-metrics-node). For more information about the supported configurations, see Supported Configuration Limits for Intersight Virtual Appliance. 

  * You can deploy Intersight Virtual Appliance on VMware vSphere as a multi-node cluster which allows for high availability. This deployment option is a three-node cluster that includes three High Availability (HA) management nodes. Once you have completed the initial set up of the single-node appliance, you can add additional High Availability (HA) management nodes. After you successfully add the two additional HA management nodes, you can create a multi-node cluster in Intersight Virtual Appliance for HA. Note that metrics data collection is not supported in the three-node cluster deployment. For more information, see, [Configuring a Multi-Node Cluster for High Availability in Intersight Virtual Appliance](b_Cisco_Intersight_Appliance_Install_and_Upgrade_Guide_chapter_01.html#Cisco_Task_in_List_GUI.dita_a18a1d2e-5c8e-42c8-a7de-6bb01b218fde). 

  * You can deploy Intersight Virtual Appliance on VMware vSphere as a multi-node cluster which allows for metrics data collection. This deployment option is a four-node cluster that includes HA management cluster and a metrics node. Once you have completed the initial set up of the HA management cluster, you can add a metric node. For more information about configuring an advantage tier metrics node, see [Configuring a Multi-Node Cluster for Increased Metrics Scalability in Intersight Virtual Appliance](b_Cisco_Intersight_Appliance_Install_and_Upgrade_Guide_chapter_01.html#configuring-metrics-node). For more information about the supported configurations, see Supported Configuration Limits for Intersight Virtual Appliance. 


The following table summarizes the deployment options in Intersight Virtual Appliance.

Table 1. Deployments Options in Intersight Virtual Appliance Deployment Option |  Number of Nodes |  Functionality |  Metrics Data Collection |  Supported Hypervisors  
---|---|---|---|---  
Single-node |  Standalone |  Intersight Virtual Appliance management capability.  |  Yes - option to enable the essential tier metrics data collection. | 

  * VMware vSphere
  * Microsoft Hyper-V
  * KVM Hypervisor
  * Nutanix AHV

  
Multi-node |  Two-node cluster |  Intersight Virtual Appliance management capability and a separate metrics node for metrics data collection. |  Yes - metrics node is required to enable essential and advantage tier metrics data collection.  |  VMware vSphere  
Multi-node |  Three-node cluster |  Intersight Virtual Appliance management capability for high availability. |  No - metrics data collection is not supported in a three-node cluster configuration. |  VMware vSphere  
Multi-node |  Four-node cluster |  Intersight Virtual Appliance management capability for high availability and a separate metrics node for metrics data collection.  |  Yes - metrics node is required to enable essential and advantage tier metrics data collection. |  VMware vSphere  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Attention** | 

* * *

Before installing and setting up Intersight Virtual Appliance, it is strongly recommended that you read the information provided in the System Requirements section.  Intersight Virtual Appliance supports TLS 1.3 protocol for HTTPS communication for improved Transport Layer Security.

* * *  
  
---|---  
  
This guide provides an overview of how to install and set up Intersight Virtual Appliance in your environment.

For latest updates on Intersight Virtual Appliance features and functionality, see [Intersight Appliance Help Center](https://intersight.com/help/appliance). 

---

## Page 16: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide/b_Cisco_Intersight_Appliance_Install_and_Upgrade_Guide_chapter_0110.html

## Configuring a Banner Message for Displaying Before the Login Screen

You can configure a banner message in Intersight Virtual Appliance. When enabled, the configured banner message will be displayed before the user login screen. 

### Procedure

* * *

**Step 1** |  Log into Intersight Virtual Appliance as a user with account administrator role.  
---|---  
**Step 2** |  Choose Settings > System > Banners.   
**Step 3** |  Click Configure.  The Configure Banner Message window displays.   
**Step 4** |  Update the following fields.

  * Show banner message before login—Enable this option. 
  * Banner Title—Enter a title for the banner message. The length of the title cannot exceed 128 characters. 
  * Banner Content—Enter the content for the banner message. The content in this field has to be less than 2000 characters. 

  
**Step 5** |  Click Save.  The configured banner message content along with the title is displayed in the Banners preview window.   
  
* * *

---

## Page 17: https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide/b_Cisco_Intersight_Appliance_Install_and_Upgrade_Guide_chapter_02.html

## Intersight Virtual Appliance 1.1.0-0 Upgrade Behavior — Impact of CentOS 7 to AlmaLinux 9 Migration

Starting with Intersight Virtual Appliance Release Version 1.1.0-0, the underlying operating system is AlmaLinux 9.

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

It is highly recommended that you take a snapshot of the appliance VM as well as a backup of the appliance before you start the upgrade process. 

* * *  
  
---|---  
  
The following information highlights the key aspects of this migration:

  * Starting with Intersight Virtual Appliance Release Version 1.1.0-0, all new Appliance and Assist installations will be based on AlmaLinux 9. 

  * Existing Appliance and Assist installations on version 1.0.9-631 or later that upgrade to version 1.1.0-0 or later will upgrade in-place to AlmaLinux 9. 

  * Upgrading to version 1.1.0-0 directly from version 1.0.9-615 or older will fail. Therefore, while upgrading to version 1.1.0-0 from version 1.0.9-615 or older, do the following: 

  * Ensure that the appliance meets the disk requirements. For more information, see [Resource Requirements](b_Cisco_Intersight_Appliance_Getting_Started_Guide_chapter_0111.html#Cisco_Reference.dita_a6ea1ddc-e212-4367-9579-e9320b64f1b5). 

  * Upgrade to one of the following versions before upgrading to version 1.1.0-0.

  * 1.0.9-631

  * 1.0.9-655

  * 1.0.9-675

  * 1.0.9-677

  * When an existing Appliance or Assist upgrades to version 1.1.0-0, expect the following behavior: 

  * The upgrade will take at least 4 hours to complete and will reboot multiple times.

  * The Appliance web UI, REST API, and CLI interfaces may not be available. You can monitor the progress of the upgrade on the VM console. 

  * It is STRONGLY RECOMMENDED that you DO NOT manually reboot the Appliance or Assist VM during the upgrade process as it may damage the VM and potentially disrupt the upgrade process. 

  * Installation and upgrade bundle sizes for release version 1.1.0-0 are larger than the ones for the previous releases due to the switch to AlmaLinux. 


---
