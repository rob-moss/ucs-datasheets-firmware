# Intersight SaaS Configure Unified Edge guide

| | |
|---|---|
| **URL Title** | Intersight SaaS Configure Unified Edge guide |
| **URL** | https://intersight.com/help/saas/configure/unified_edge |
<<<<<<< HEAD
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260821153740774/docs/cloud/data/articles/features/unified_edge/configure/en/index.html |
| **HTML Title** | Unified Edge |
| **Source file** | `ucs-docs-raw/html/intersight-saas_configure_unified_edge.html` |
| **File type** | HTML |
| **Fetched on** | 2026-08-24 09:16:10 |
=======
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260626102158280/docs/cloud/data/articles/features/unified_edge/configure/en/index.html |
| **HTML Title** | Unified Edge |
| **Source file** | `ucs-docs-raw/html/intersight-saas_configure_unified_edge.html` |
| **File type** | HTML |
| **Fetched on** | 2026-06-30 16:42:31 |
>>>>>>> b54dc188455b65bee6c95ef06462b9c67adf0b3a

---

# Unified Edge

Unified Edge configurations are defined by policies that contain all the server and chassis settings. It is recommended to create the required policies in advance so that they are available when you create profiles. For more information, see [Configuring Policies for Unified Edge Chassis (eCMCs)](/help/resources/ue_chassis_policies) and [Configuring Policies for Unified Edge Servers](/help/resources/ue_servers_policies).

Profiles consolidate these policies for a device, allowing you to apply consistent configurations. To create Unified Edge profiles, do one of these:

  * Create profiles directly:

If you only need one or a few profiles, or if each profile will be unique, you can create each profile individually. For more information, see [Unified Edge Profiles and Server Profiles](/help/configure/unified_edge#unified_edge_profiles_and_server_profiles) and [Creating and Deploying Unified Edge Profile](/help/configure/unified_edge#creating_and_deploying_unified_edge_profile).

  * Clone:

If you want to replicate an existing profile without starting from scratch, you can clone it to create a new profile that retains the original configuration.

  * Use templates:

If you need to create several profiles that will have the same settings, you can first create a template. Then, derive multiple profiles from this template. For more information, see [Unified Edge Profile Templates](https://qa.starshipcloud.com/help/saas/configure/unified_edge#unified_edge_profile_templates) and [Creating a Template and Deriving Profiles](/help/configure/unified_edge#creating_a_template_and_deriving_unified_edge_profiles).


Lastly, Unified Edge profiles and server profiles should be created and assigned to Unified Edge and compute nodes respectively. For more information, see

[Creating and Deploying Unified Edge Profile](/help/configure/unified_edge#creating_and_deploying_unified_edge_profile) and [Creating and Deploying UCS Server Profile](/help/resources/cisco_intersight_managed_mode_configuration#configuring_ucs_server_profiles) respectively.

Note:

Configuration drift is not supported for Unified Edge profile.

## Unified Edge Profiles and Server Profiles

Unified Edge includes both chassis and servers, each managed through Unified Edge profiles and server profiles, respectively:

  * Unified Edge profiles: These profiles are used to configure and manage the chassis components. When deployed, these profiles configure the eCMCs to match the configuration of the Unified Edge profile. For more information, see [Creating and Deploying Unified Edge Profile](/help/configure/unified_edge#creating_and_deploying_unified_edge_profile).

  * Server profiles: Server profiles are focused on the configuration and management of individual servers within the Unified Edge Chassis. They are deployed directly to the server and ensure that the server configuration matches the configuration of the server profile. For more information, see [Server Profiles](/help/configure/servers#server_profiles).


Profiles can be created directly or derived from templates. Each profile can be deployed and managed individually.

## Creating and Deploying Unified Edge Profile

Note:

A Unified Edge profile can also be derived from Unified Edge profile templates. For more details, see [Creating Template and Deriving Profiles](/help/configure/unified_edge#creating_a_template_and_deriving_unified_edge_profiles).

To create and assign a Unified Edge profile:

  1. Log in to Cisco Intersight as an Account Administrator or a user with Unified Edge Administrator privilege.

  2. Choose Configure > Profiles > Unified Edge Profiles.

  3. Click Create Unified Edge Profile.

  4. On the General page, configure the necessary parameters, and then click Next.

  5. On the Unified Edge Assignment page, do one of these:

  * Choose Assign Now, select the unified edge you want to deploy, and then click Next.

  * Choose Assign Later and click Next to select and associate policies.

  6. Configure the required General, Chassis, Switch, and Management settings by selecting existing policies or creating new ones as needed in the side navigation window. For more information on the policies, see [Policy Configuration](/help/configure/unified_edge#policy_configuration).

  7. On the Summary page, verify the Unified Edge profile details and the attached policies.

  8. Click Deploy to create the Unified Edge profile and deploy it to the assigned Unified Edge.

The profile will be listed in the Unified Edge profiles table view.


## Policy Configuration

Policy Category| Policy Name  
---|---  
Chassis Configuration| 

  * [Power Policy](/help/resources/ue_chassis_policies#power_policy)
  * [Thermal Policy](/help/resources/ue_chassis_policies#thermal_policy)

  
Switch Configuration| Edge Chassis Management Controller A/B:

  * [VLAN Policy](/help/resources/ue_chassis_policies#vlan_policy)

Switching Configuration:

  * [System QoS Policy](/help/resources/ue_chassis_policies#system_qos_policy) (Mandatory)
  * [Switch Control Policy](/help/resources/ue_chassis_policies#switch_control_policy)

  
Management Configuration| 

  * [NTP Policy](/help/resources/ue_chassis_policies#ntp_policy)
  * [Syslog Policy](/help/resources/ue_chassis_policies#syslog_policy)
  * [Network Connectivity Policy](/help/resources/ue_chassis_policies#network_connectivity_policy)
  * [Local User Policy](/help/resources/ue_chassis_policies#local_user_policy)

  
  
## Unified Edge Profile Templates

Unified Edge profile templates enable you to create reusable configurations from which multiple Unified Edge profiles can be derived. Updates made to a template are applied to all derived profiles through a synchronization workflow. If a profile becomes out of sync with its template, the Template **Sync Status** indicates this condition, and you can use the available synchronization actions to review and synchronize the profile to bring it back in sync. Each derived profile can then be deployed and managed individually. Using templates allows multiple profiles to be created and modified at once, simplifying and speeding up configuration tasks. For more information, refer to [Creating a Template and Deriving Unified Edge Profiles](/help/configure/unified_edge#creating_a_template_and_deriving_unified_edge_profiles).

## Unified Edge Template List View

When you select **Templates** in the Intersight UI, the Unified Edge Profile Templates list view is seen.

The list view shows the following details in a tabular format:

  * Name: The name of the Unified Edge Profile Template.

  * Sync Status: The sync status between the template and its derived profiles. The status of the template changes to Out of Sync, even if one of its derived profile is out of sync.

  * Usage: The count of the Unified Edge profiles derived from the template.

  * Description: The description of the template provided during template creation.

  * Last Update: The date on which the template was last updated.

  * Organization: The name of the organization.


For more information on how to create a UCS Unified Edge Profile Template, [Creating a Template and Deriving Unified Edge Profiles](/help/configure/unified_edge#creating_a_template_and_deriving_unified_edge_profiles).

## Creating a Template and Deriving Unified Edge Profiles

To create a Unified Edge profile template and then derive multiple profiles:

  1. Go to Configure > Templates, and click Create Unified Edge Profile Template.

  2. Configure the required General, Chassis, Switch, and Management settings by selecting existing policies or creating new ones as needed in the side navigation window. For more information on the policies, see [Policy Configuration](/help/configure/unified_edge#policy_configuration).

  3. On the Summary page:

  * To create the template and derive profiles immediately, click Derive Profiles.

  * To create the template only (and derive profiles later), click Close and exit the wizard.

When ready to derive the profiles, go to Configure > Templates > Unified Edge Profile Templates, select the template name, click the ellipsis (…) icon, and choose the Derive Profiles action.

  4. On the Derive > General page, select Unified Edges required to be assigned to the derived Unified Edge profiles.

     1. You can choose one of these options for the server assignment:

  * Choose Assign Now, to select the Unified Edges for which profiles should be created using this template. Use this option to immediately assign the Unified Edges to the profiles.

  * Choose Assign Later, enter the number of profiles to be derived. Use this option to assign a Unified Edge to the profile at a later time.

     2. Click Next.

  5. On the Derive > Details page:

     1. Under the General section, edit the description, tags, and auto-generated names of the derived profile as necessary.

     2. Under the Derive section:

Specify these parameters:

        1. Profile Name Prefix: The profile name prefix auto-populates the source profile name, differentiates the derived profile from the source for identification. Modify and manage the name as required.

Note:

This field is displayed only when you choose to derive more than one profile.

        2. Digits Count: You can include a digit to further differentiate the derived profiles. The digit automatically appends a numerical count to the derived name prefix, incrementing with each subsequent derived profile.

Note:

This field is displayed only when you choose to create more than one clone.

        3. Start Index for Suffix: You can choose the initial number for the suffix that will be appended to the derived name prefix. With a defined start index, each derived profile will have a unique suffix based on an incrementing count.

Note:

This field is displayed only when you choose to create more than one derived profile.

     3. Click **Next**.

  6. On the Summary page, verify the details of the profiles that need to be derived from the template.

  7. Click Derive.

Unified Edge profiles get successfully derived from the template.


## Unified Edge Profile Table View

The table view shows the following details in a tabular format:

  * Description: The description for Unified Edge.

  * Last Update: The date and time that the Unified Edge profile was last updated.

  * Name: The name of the Unified Edge profile.

  * Organization: The name of the organization.

  * Status: The deployment status of the profile. It can be OK, Not Deployed, Not Assigned, or Evaluating.

  * Template Sync Status: The values are **Scheduled** , **Syncing** , **OK** , and **Out of Sync**.

  * **Scheduled and Syncing** : Represents the transient states that occur while the Template Update Workflow is actively in progress.

  * **OK** : The profile configuration is fully synchronized with the template; no differences exist.

  * **Out of Sync** : The profile configuration differs from the template, indicating that updates or changes in the template have not yet been applied to the profile.

  * Unified Edge: The name of the Unified Edge to which the profile is attached.

  * Unified Edge Template: The name of the Unified Edge template to which the profile is attached. Each template can derive a maximum of 25 profiles in a single action. Maximum number of Unified Edge profiles supported per template is 500.

  * User Label: Displays the assigned user label that helps identify the Unified Edge profiles.


## **Unified Edge Profile Actions**

Profile Action| Description  
---|---  
Edit| Edits the profile properties.  
Clone| Clones the profile properties.  
Delete| Deletes the profile properties.  
Set User Label| To set, update, or delete user labels for each server.It must be between 1 and 64 alphanumeric characters and can contain only these special characters: `! # $ % & * + , ( ) [ ] { } | / . ? @ _ : ; ~`  
Attach to Template| Attach the Unified Edge profile to an existing template.This attachment overrides the config properties of the profile and replaces them with the template properties.A server profile attached to a template cannot be modified. The modifications can only be done in the associated template.  
Create Template| Create a template from the profile.  
Detach from Template| Detach the profile from the template.A server profile can be detached from a template and modified as per the requirements.A detached server profile can always be reattached to a template.  
Sync with Template| Synchronize the profile with its template.  
  
## Learn More

  * [Operating Unified Edge](/help/operate/unified_edge)

  * [Cisco Unified Edge](/help/resources#cisco_unified_edge)

