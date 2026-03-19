# Intersight SaaS Configure Servers guide

| | |
|---|---|
| **URL Title** | Intersight SaaS Configure Servers guide |
| **URL** | https://intersight.com/help/saas/configure/servers |
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260316155144543/docs/cloud/data/articles/features/servers/configure/en/index.html |
| **HTML Title** | Document |
| **Source file** | `ucs-docs-raw/html/intersight-saas_configure_servers.html` |
| **File type** | HTML |
| **Fetched on** | 2026-03-19 15:36:13 |

---

In Cisco Intersight, a Server Profile enables resource management by streamlining policy alignment, and server configuration. To view the Server Profiles table view, choose Configure > Profiles > UCS Server Profiles. You can create Server Profiles using the Server Profile wizard or you can import the configuration details of C-series servers in standalone mode and FI-attached servers in Intersight Managed Mode (IMM), directly from Cisco IMC. You can create Server Profiles using the Server Profile wizard to provision servers, create policies to ensure smooth deployment of servers, and eliminate failures that are caused by inconsistent configuration. The Server Profiles wizard groups the server policies into the following four categories to provide a quick Summary View of the policies that are attached to a profile:

  * Compute Policies—BIOS, Boot Order, Firmware, Persistent Memory, Memory, Power, Scrub, Thermal, and Virtual Media.

  * Network Policies—Adapter Configuration, iSCSI Boot, LAN Connectivity, and SAN Connectivity policies.

  * The LAN Connectivity policy requires you to create Ethernet Network Policy, Ethernet Adapter Policy, and Ethernet QoS Policy. When you attach a LAN Connectivity policy to a server profile, the addresses of the MAC address Pool, or the static MAC address, are automatically assigned.

Note: A LAN Connectivity policy that has a static MAC address can be attached to only one server profile.

  * The SAN Connectivity policy requires you to create Fibre Channel Network Policy, Fibre Channel Adapter Policy, and Fiber Channel QoS Policy. When you attach a SAN Connectivity policy to a server profile, the addresses of the WWPN and WWNN Pools, or the static WWPN and WWNN addresses, are automatically assigned.

Note: A SAN Connectivity policy that has a static WWPN, or a static WWNN can be attached to only one server profile.

  * Storage Policies—Drive Security, SD Card, and Storage policies.

  * Management Policies—Certificate Management, Device Connector, IPMI Over LAN, LDAP, Local User, Network Connectivity, NTP, Serial over LAN, SMTP, SNMP, SSH, Syslog, and Virtual KVM policies.


Certain server configurations applied through policies are automatically cleared and reset to default settings in Intersight Managed Mode servers. This occurs under the following conditions: when policies are detached and the profile is re-deployed, when a server is unassigned from a profile, during first-time discovery, decommissioning, or during recommissioning of a server. For more information, see [Clearing and Resetting Server Configurations](../../../../../../../../../../help/configure/servers#clearing_and_resetting_server_configurations).

For more information and descriptions of the policies, see the Server Policies section. For an example of the policy creation workflow, see [Creating Network Policies](../../../../../../../../../../../help/resources#creating_network_policies).

## Server Profile List View

When you select Profiles > UCS Server Profiles in the Intersight UI, the UCS server profile list view is seen.

The list view shows the following details in a tabular format:

  * Name—The name of the server profile.

  * Status—The deployment status of the server profile.

The Status of the profiles can have any of the following values:

  * Activating—A transient state is observed during the Activation workflow**.**

  * Analyzing—A transient state that occurs when the policy impact estimation is in progress.

  * Configuring—A transient state that occurs during the Deploy workflow when the deploy tasks for the various policies are in progress.

  * Evaluating—A transient state is observed during the policy change evaluation workflow.

  * Failed—Server profile validation, configuration, or deployment has failed.

  * Inconsistent—Indicates that the policy configuration has changes that have not yet been deployed or activated. It may also indicate that the policy configuration at the endpoint is not in sync with the last deployed policy configuration in the server profile. If the endpoint settings are altered manually after a server profile is deployed, Intersight automatically detects the configuration changes and they will be shown on the server profile as Inconsistent. For more information, see the _Server Profile Drift_ and the _Deploying and Activating a Server Profile_ sections.

  * Not Assigned—Server is not assigned to the server profile.

Note:
  * Once you deploy policies to the server profile, the status changes automatically from _Not Assigned_ to the new status depending on the outcome. You may need to refresh your screen to view the updated status.

  * You must do the Power Cycle/Power ON after each profile deployment.

  * Not Complete—The configuration import for the profile has not been completed.

  * Not Deployed—The server is assigned to the profile, but the configuration has not yet been applied to the endpoint.

  * OK—Policies deployed successfully on the server profile.

  * Unconfiguring—A transient state occurs during the Undeploy workflow for FI-attached servers only.

  * Validating—A transient state is currently in progress during policy validation for the server assigned to the profile.

  * Waiting for Resources—The profile is pending resource allocation.

  * Inconsistency Reason—The reason for the status being shown as _Inconsistent_. Example—Not Deployed, Not Activated, Out of Sync.

  * Target Platform—Indicates if the platform for which the profile is applicable is a Standalone UCS server or FI-attached UCS server.

  * UCS Server Profile Template—The template attached to the server profile or from which the profile has been derived.

  * Template Sync Status—The sync status between the server profile and the template from which the server profile has been derived.

  * Server—The name of the server to which the profile is attached.

  * Resource Pool—The pool to which the profile belongs.

  * User Label—Displays the assigned user label that helps in identification of the server profiles.

  * Last Update—The date on which the profile was last updated.

  * Organization—The name of the organization.


Note:

Some of the columns are not included by default, such as, User Label. To view such columns in the server profiles table view, you need to enable them while customizing the table view.

## Server Profile Actions

After creating server profiles, actions that can be performed on a server profile are as follows:

  * Deploy—Deploy the profile to the attached server.

  * Activate—Activate the profile on the attached server. The server gets power cycled on activation.

  * Assign Server—Assign a server to the server profile.

  * Edit Assignment—Modify the assigned server in the server profile, provided that the profile has not yet been deployed.

Note:

To modify the server assignment for a deployed profile, first unassign the existing server, and then assign the new server using the Server Profile Actions menu.

  * Unassign Server—Unassign the server from the profile. This action will cause the server configurations to reset to defaults. For more information, see [Clearing and Resetting Server Configurations](../../../../../../../../../../help/configure/servers#clearing_and_resetting_server_configurations).

  * Clone—Clone the profile.

  * Edit—Edit the profile.

  * Delete—Delete the profile.

  * Set User Label—Allows you to set, update, or delete user labels for each server. It must be between 1 and 64 alphanumeric characters, containing only the following special characters: ! # $ % & * + , ( ) [ ] { } | / . ? @ _ : ; ~

  * Attach to Template—Attach the server profile to any of the available templates.

Note:
  * While template creation, if you toggle ON the Attach UCS Server Profile to Profile Template button, the selected profile gets attached to the template under creation.

  * If you keep the toggle button OFF, the selected profile's properties are carried to the template but the profile does not get attached to it.

  * Create a Template—A server profile can be used to create a template. This template can then be used to create multiple profiles with same configurations and deployed on multiple servers.

  * Detach from Template—Detach the profile from the template.

Note:
  * Create a Template and Attach to Template actions can be performed only if a server profile is not attached to any template.

  * A server profile can be attached to an existing template. This attachment overrides the config properties of the profile and replaces them with the template properties.

  * A server profile attached to a template cannot be modified. The modifications can only be done in the associated template.

  * A server profile can be detached from a template and modified as per the requirements.

  * A detached server profile can always be reattached to a template.

  * Sync With Template—Synchronize the Out of Sync profiles to ensure alignment with template configurations.

  * Server Actions—Allows you to perform following actions on the assigned server:

  * Power

  * Install Operating System

  * Launch vKVM

  * Launch Tunneled vKVM

For a detailed description of these actions, refer to [Server Actions](../../../../../../../../../../help/operate/servers#server_actions).


## Server Profile Details View

From the Server Profile List View, click a profile name to open the Server Profile Details View. This page has four tabs: General, Server, Inventory, and Connectivity. The General tab shows profile information and real-time status of any pending changes from previous server deployments. The other three tabs display detailed information about the assigned server.

General — The General tab has two sections: Details and Configuration.

  * Details section displays the Status, Name, Description, User Label, Target Platform, Template Name, and Organization. You can also view Server Assignment fields (Assigned Server and Assignment Type) and any configured Tags.

  * Configuration section displays Policies (attached policies), Identifiers (UUID assignments), vNICs/vHBAs (placement details), and any Errors & Warnings.


You can edit Server Profile configurations directly from this tab, in addition to using the Edit action under Server Profile Actions. This method simplifies the workflow and saves time by eliminating the need to navigate through the wizard.

Editing a Server Profile

To edit a server profile from Server Profile Details View:

  1. Log in to Cisco Intersight with Account Administrator or Server Administrator role.

  2. Choose Configure > Profiles > UCS Server Profiles.

  3. Select the desired profile to edit by clicking its Name. The Server Profile Details View appears.

Note:

You can also modify the Server Profile by using the Edit action under Server Profile Actions. This will guide you through the full wizard to apply your changes. For more information, see [Configuring UCS Server Profiles](../../../../../../../../../../help/resources/cisco_intersight_managed_mode_configuration#configuring_ucs_server_profiles).

  4. To modify the general information, under Details section:

     1. Click Edit next to General.

     2. On the Edit General Details page, edit the Name, Description, or User Label as required.

     3. Click Save.

  5. To modify the server assignment, scroll down to Server Assignment under Details section:

     1. Click on Assign to assign a server to the server profile.

     2. On Assign Server to UCS Server Profile: <Profile Name> page, choose to assign a specific server, either from a resource pool, by chassis slot location or by serial number.

     3. Click **Assign**.

Note:

If a server is already assigned to a UCS Server Profile and the profile is deployed, you cannot modify the server assignment. To change the server assignment, first unassign the server from the profile, then assign the new server. However, if the profile has not been deployed, you can modify the server assignment.

  6. To modify the policies attached, go to Configuration > Policies:

     1. Toggle off the Show Attached Policies button. All the available policies under Compute, Management, Storage, and Network categories appears.

Note:

The Show Attached Policies toggle is enabled by default, displaying only the list of attached policies.

     2. To attach a policy, hover over the policy name and click Select Policy ![](491175.png). Select the required policy or create a new policy in the side navigation window. For more information on the Server Policies, see [Server Policies](/help/configure/servers#server_policies).

     3. To detach a policy, hover over the attached policy name and click Detach ![](491172.png). A confirmation message “ _Policy <policy name> will be detached, and default configuration will be applied_.” appears. Click Detach to confirm.

     4. Click Preview ![](491173.png) to view the details of the attached policy.

     5. Click Edit ![](491174.png) to edit the attached policy.

Note:

If you modify or add a policy to a deployed Server Profile, its Status changes to Inconsistent, indicating pending changes that differ from the previously deployed configuration.

  7. To modify the UUID, go to Configuration > Identifiers:

     1. In Identifiers section, hover over the UUID and click Assign. The Assign UUID page appears.

     2. Choose the appropriate UUID from Pool or Static options:

  * Pool— Allows UUID Pool association to the server. Select the required pool from the list available. For more information on pools, see [Pools](/help/configure/servers#pools).

  * Static— Allows UUID association to the server using Static UUID address, by entering the full UUID address for the server. It must include both the UUID prefix and the UUID suffix. For example, the prefix could be 69F8FB36-67F3-4BC3 and the suffix could be 0002-000000000001.

     3. Click Assign.

     4. To detach a UUID, hover over the Assigned UUID Pool and click ![](491172.png) to detach. A confirmation message “ _UUID pool <pool name> will be detached from the profile_.” appears. Click Detach to confirm. For more information, see [UUID Pools](../../../../../../../../../../help/resources/cisco_intersight_managed_mode_configuration#configuring_pools).

Note:

If you modify or add a UUID pool to a deployed Server Profile, its Status changes to Inconsistent, indicating pending changes that differ from the previously deployed configuration.

  8. To modify vNIC/vHBA placements, go to Configuration > vNICs / vHBAs:

     1. In vNICs/vHBAs section, scroll down to Auto Placement Configuration and click Edit Placement. Make the required changes in vNICs & vHBAs and click Save.

  * Auto Placement Configuration is available only for IMM Servers.

  * Graphical representation of vNICs & vHBAs placement is only applicable for Auto Configuration mode.

  9. To view errors and warnings, go to Configuration > Errors/Warnings, and review the listed items.


**Server** —The Server tab displays the details of the assigned server and its properties.

**Inventory** —The Inventory tab displays the inventory details of the assigned server.

**Connectivity** — The Connectivity tab displays the network connectivity details such as vNIC/vHBA, Network Adapter, Virtual Circuit, FI details and so on.

For more information, see [Servers Details View](../../../../../../../../../../help/operate/servers#servers_details_view).

## Server Profile Drift

A server profile drift occurs when the policy configuration at the endpoint is not in sync with the last deployed policy configuration in the Server Profile.

Cisco Intersight supports Server Profile Drift detection for standalone servers and Intersight Managed Mode servers. For Intersight Managed Mode servers, the firmware versions required for drift detection are:

  * For 4.2 release, the Cisco IMC version must be 4.2(1b) or above.

  * For 4.1 release, the Cisco IMC versions must be:

  * For rack servers - 4.1(3d) or above

  * For blade servers - 4.1(33e) or above


The check to look up for any configuration change at the endpoint is performed every 30 min.

To see the policy configurations that have changed at the endpoint relative to the currently deployed policy configuration in Intersight, navigate to server profile details view and click View Changes. You can choose to view the Changes Only or All the policy configuration details.

Property| Essential Information  
---|---  
Saved Settings| Displays the policy settings in Intersight.  
Last Deployed Settings| Displays the latest policy settings deployed on the server profile.  
Endpoint Settings| Displays the configuration at the endpoint.  
  
To move the Server Profile status back to **OK** , you can either redeploy the profile or change the values at the endpoint. You can use the Device Connector Policy in Intersight to control configuration changes allowed from Cisco IMC. In the Device Connector Policy, choose Configuration from Intersight only to stop allowing configuration changes from Cisco IMC directly.

Limitations of Server Profile Drift - Standalone Servers

For standalone servers, configuration changes at the endpoint will not be detected for the following policies under the specified conditions:

Policy| Configuration at the endpoint  
---|---  
SD Card Policy| If an SD card is removed.  
Storage Policy| 

  * If Expand to Available is set for any of the virtual drives in the policy.
  * If the Power Cycle is not done after every deployment.
  * If there are additional drive groups that are not configured from Intersight

  
Boot Order Policy| If the Power Cycle is not done after every deployment.In SAN boot devices, Intersight does not detect drift for Interface Name and Target WWPNNote:Cisco recommends using a SAN boot, because it offers the server profile mobility within the system. If you boot from the SAN when you move a server profile from one server to another, the new server boots from the same operating system image. Therefore, the new server appears as the same server to the network.To use a SAN boot, ensure that the following is configured:

  * The Cisco UCS domain must be able to communicate with the SAN storage device that hosts the operating system image.
  * A boot target LUN (Logical Unit Number) on the device where the operating system image is located.

Starting with Cisco UCS B-Series server firmware version 4.2(3d) and Cisco UCS X-Series server firmware version 5.0(2e), you must configure zoning on the Fibre Channel switches and LUN masking on the storage arrays before deploying SAN Boot. Otherwise, the initiators may not remain logged into the SAN switch fabric continuously.  
Local User, SNMP, LDAP, and IPMI over LAN Policy| If there are changes to the Password at the endpoint.  
Virtual Media policy| If there are changes to the Password, Mount Options, or Authentication Protocols at the endpoint.  
BIOS Policy| 

  * BIOS token values configured as 'platform-default' are changed to the default value for that platform. Drift detection does not occur for such BIOS tokens. For more details, see Table 16 of the Creating a BIOS Policy section in [Supported UCS Server Policies](/help/resources/cisco_intersight_managed_mode_configuration#supported_ucs_server_policies).
  * BIOS tokens whose values depend on other BIOS token values are not considered for drift detection. Drift may get reported for a BIOS token whose value is not supported by the server on which the policy is being deployed. For more details, see [Cisco UCS Server BIOS Tokens](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-technical-reference-list.html).

  
IPMI over LAN policy| 'Privilege Level’ field will not be considered.  
Network Connectivity Policy| ‘Preferred IPv6 DNS Server’ and ‘Alternate IPv6 DNS Server’ fields in the policy will not be considered. Server Profile may move to Out of Sync status temporarily.  
Adapter Configuration Policy| This policy will not be considered for drift calculation.  
Ethernet Adapter Policy| If a usNIC or VMMQ has a different Ethernet Adapter policy, then the configuration changes will not be calculated for usNIC or VMMQ attached Ethernet Adapter policy.Due to VMQ configuration restrictions, VMQ Number of Interrupts will override the value of Interrupts in Ethernet Adapter Policy, and VMQ Number of Virtual Machine Queues will override the value of Receive Queue Count, Transmit Queue Count, and Completion Queue Count (Receive+Transmit) of Ethernet Adapter Policy. Drift will not be detected for Number of Interrupts, Number of Virtual Machine Queues, Receive Queue Count, Transmit Queue Count, and Completion Queue Count.Intersight does not detect drift for `Number of Interrupts', 'Number of Virtual Machine Queues', 'Receive Queue Count', 'Transmit Queue Count', and 'Completion Queue Count'.  
LAN Connectivity Policy| The CDN and PCI Order fields will not be considered.  
IMC Access Policy| If both In-Band IPv6 and IPv4 configurations are available, the IPv6 DNS configuration is prioritized.  
  
Limitations of Server Profile Drift - Intersight Managed Mode Servers

For Intersight Managed Mode servers, server configuration changes at the endpoint will not be detected for the following policies under the specified conditions:

Note:

The Name field is not supported for any policy because Name is not an endpoint setting.

Note:

Drift detection is not supported for pools and IDs.

Policy| Configuration at the endpoint  
---|---  
SD Card Policy| Drift detection is not supported if an SD card is removed.  
Storage Policy, Boot Order Policy, BIOS Policy, Virtual Media Policy, Syslog Policy| Drift detection is not supported for Storage policy, Boot Order Policy, BIOS Policy, Virtual Media Policy, and Syslog Policy on Intersight Managed Mode servers.  
Local User Policy, SNMP Policy, Certificate Management Policy| Drift detection is not supported if there are changes to secure fields such as Password, Community Strings, and Private Key at the endpoint.  
LAN Connectivity Policy| Drift detection is not supported for:

  * VMQ connection
  * Number of interrupts
  * Number of Virtual Machine Queues
  * Consistent Device Naming (CDN)
  * Auto vNICs Placement IDs
  * PCI Order
  * Ethernet Adapter Policy
  * Interrupts Settings - Interrupts
  * Completion - Completion Queue Count, Completion Ring Size
  * VMMQ Adapter Policy
  * usNIC Adapter Policy

Note:Drift detection is supported only when the servers are powered on.  
IMC Access Policy| Drift detection is not supported for Out-of-Band configuration.  
SAN Connectivity Policy| Drift detection is not supported for Auto vNICs Placement IDs.Note:Drift detection is supported only when the servers are powered on.  
Power Policy| Drift detection is not supported for the Power Priority property.  
  
## Server Profile Import

Intersight provides the capability to import configuration details of C-series servers in standalone mode and FI-attached servers in Intersight Managed Mode (IMM), directly from Cisco IMC. The Server Profile import enables you to migrate the configuration of your existing servers to Intersight without having to create a profile and the policies manually. The Server Profile import operation creates a profile and the associated policies based on the server configuration. You can create a golden configuration profile and clone it and apply to another server already claimed in Intersight.

You can import a server profile configuration from the following locations in Intersight:

  * Servers table view—Select a Cisco UCS C-Series Standalone server in Intersight Managed Mode (IMM) from the table view and click the ellipses (…) and select Import Server Profile.

  * Click a C-series server in standalone mode in Intersight Managed Mode (IMM) in the Servers table view to access the Server details page. Click Actions on the top-right corner and select Import Server Profile. This option is enabled only when no server profile is associated with the server.


Note:

A partially imported server profile cannot be attached to a template or cannot be used for creating a template.

For more information on how to import a Server Profile Import and about the detection of manual configuration changes at the endpoint, see [Importing a Server Profile](/help/resources/Importing_Server_profile) in [Resources](/help/resources).

## Estimate Impact

The Estimate Impact workflow, for standalone and Intersight Managed Mode servers, analyzes the disruptions that would be caused by the various policies attached to a server profile, when the server profile is deployed. The analyze impact workflow is triggered when a policy is attached, detached, or updated. The Disruption is indicated against each policy. The disruptions, which could be caused by the policies, are:

  * Immediate reboot is required for standalone server policies such as Persistent Memory policy or Adapter policy. In such cases, the disruption indicated against the policy is Immediate Reboot.

  * An Activate action on the server profile needs the server to reboot and activate the policy configuration on the server. In such cases, the disruption indicated against the policy is Activate Requires Reboot.

  * Some policies, such as IMC Access policy, cause a brief outage of the server management network. In such cases, the disruption indicated against the policy is Network Management Outage.


**Deploying and Activating a Server Profile**

Deploy and Activate are two explicit actions that can be performed on server profiles. Policy configuration staging happens as a part of server profile deployment. Policy staging allows you to stage the policy configurations and get an idea of the pending actions for activating the policies. You can activate the policy by rebooting servers manually or using the Activate action of the Server Profile during a maintenance window. Policy activation failures are identified when the Activate action is triggered.

The Status widget in the Server Profiles table view shows the number of profiles in Inconsistent state. A server profile will be in the Inconsistent state when it has policy changes that have not yet been deployed or activated. The Inconsistency Reason widget shows the reason why a profile is in the Inconsistent state. A server profile could be in an Inconsistent state because:

  * There are changes in the policies attached to the server profile assigned to the server.

  * The policy configuration is out-of-sync with the configuration deployed in the endpoints.

  * The policy is in Not Activated state.


You can use Deploy action to stage the configuration changes. By default, only the modified policies along with any dependent policies are deployed. For more information on dependent policies, see the Policy Dependency Matrix below.

  * You can check the Deploy all associated policies whether modified or not check box to deploy all the policies attached to the server profile.

  * You can check the Reboot Immediately to Activate check box to enable the server to reboot and activate the server profile immediately. If unchecked, the policy configuration changes are activated at the next reboot.

  * You must check the I understand that potential disruption may occur during profile deployment check box to proceed.

Note:

The third check box appears when profile changes might lead to potential disruptions, such as reboots or network outages. If this checkbox appears, you must acknowledge it to proceed.


Click Deploy to proceed.

The Activate action reboots the server and activates the configuration on the server. You can also opt to trigger Deploy to stage the configuration changes and later trigger Activate, during the maintenance window, to activate the deployed configuration.

Note:

The "Deploy" API call deploys only the policies that have been modified since the last deployment.

On the Policy Edit page, when you edit a policy, the Save & Deploy option, deploys only the edited policy and its dependents from where the deployment is initiated, by default. This action applies the changes to all server profiles associated with the policy.

  * You can check the Deploy all associated policies whether modified or not check box to deploy all the policies attached to the server profile.

  * You can check the Reboot Immediately to Activate check box to enable the server to reboot and activate the server profile immediately. If unchecked, the policy configuration changes are activated at the next reboot.

  * You must check the I understand that potential disruption may occur during profile deployment check box to proceed.

Note:

The third check box appears when profile changes might lead to potential disruptions, such as reboots or network outages. If this checkbox appears, you must acknowledge it to proceed.


**Policy Dependency Matrix**

Policy| Dependent Policies (automatically deployed)  
---|---  
SNMP Policy| Access Policy, Syslog Policy  
vMedia Policy| Access Policy  
LAN Connectivity Policy (LCP)| SAN Connectivity Policy (SCP), Boot Policy  
SAN Connectivity Policy (SCP)| Boot Policy, LCP  
Boot Policy| LCP, SCP  
Drive Security Policy| Access Policy  
Local User Policy| SNMP Policy, Syslog Policy