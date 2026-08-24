# Intersight SaaS Configure Chassis guide

| | |
|---|---|
| **URL Title** | Intersight SaaS Configure Chassis guide |
| **URL** | https://intersight.com/help/saas/configure/chassis |
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260821153740774/docs/cloud/data/articles/features/chassis/Configure/en/index.html |
| **HTML Title** | Document |
| **Source file** | `ucs-docs-raw/html/intersight-saas_configure_chassis.html` |
| **File type** | HTML |
| **Fetched on** | 2026-08-24 09:16:08 |

---

Chassis policies in Cisco Intersight allow you to configure various chassis parameters, including IP pool configuration, VLAN settings, SNMP authentication, and SNMP trap settings. A chassis policy can be assigned to any number of chassis profiles to provide a configuration baseline for a chassis.  
  
To launch the Policies Table View, choose **Configure** > **Policies**.

The chassis policy creation wizard in Cisco Intersight has two pages:

  * **General** —The General page allows you to select the organization and enter a name for the policy. Optionally, include a short description and tag information to help identify the policy. Tags must use the `key:value` format. For example, `Org:IT` or `Site:APJ`.
  * **Policy Details** —The Policy Details page contains properties that apply to UCS chassis policies.


The **Policy Clone** wizard allows you to clone chassis policies with properties similar to those of existing policies. The clone policy action is available in both the policy list and detail views. For more information, see [Cloning a Policy](/help/saas/resources/cloning_a_policy#cloning_a_policy).

You can compare up to five policies of the same type from the **Policies List View** page to identify configuration differences, maintain consistency, and simplify troubleshooting.

To compare policies, select the checkboxes next to the desired policies, click the ellipsis (**…**) at the top left of the page, and choose **Compare**. On the **Compare** side drawer, only the differences between the selected policies are shown by default. To display all parameters, select **All** from the **Display** drop-down menu.

> **Note:** You can compare a minimum of two and a maximum of five policies of the same type at a time.

The following list describes the chassis policies that you can configure in Cisco Intersight.

  * **IMC Access Policy** —This policy enables network configuration and management by mapping IP pools to the chassis profile. It allows In-Band and Out-of-Band configurations that are associated with an IP address from the IP pool. The policy also permits forwarding SNMP traffic over In-Band and Out-of-Band configurations.
  * **Power Policy** —Enables the management of chassis power usage. This policy allows you to configure the redundancy mode of the chassis Power Supply Units (PSUs) and allocate power to the chassis. You can view the redundancy health, redundancy mode, input power health, and output power health of the chassis in the properties section of the **General** tab on the Chassis Details View page. For the Cisco UCS X9508 chassis, you can configure Power Save Mode and Dynamic Power Reallocation.
  * **SNMP Policy** —Configures the SNMP settings for sending fault and alert information through SNMP traps from managed devices. SNMP users or SNMP traps previously configured on the managed devices are removed and replaced with the users or traps that you configure in this policy. If you have not added any users or traps to the policy, the existing users or traps on the input/output module (IOM) are removed.
  * **Thermal Policy** —Allows you to set the Fan Control Mode for the chassis. The Fan Control Mode controls the chassis fan speed to maintain optimal server cooling.
