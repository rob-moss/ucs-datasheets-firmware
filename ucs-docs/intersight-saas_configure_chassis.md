# Intersight SaaS Configure Chassis guide

| | |
|---|---|
| **URL Title** | Intersight SaaS Configure Chassis guide |
| **URL** | https://intersight.com/help/saas/configure/chassis |
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260225095216527/docs/cloud/data/articles/features/chassis/Configure/en/index.html |
| **HTML Title** | Document |
| **Source file** | `ucs-docs-raw/html/intersight-saas_configure_chassis.html` |
| **File type** | HTML |
| **Fetched on** | 2026-03-04 11:11:08 |

---

Chassis policies in Cisco Intersight allow to configure various parameters of the chassis, including IP pool configuration, VLAN settings, SNMP authentication, and SNMP trap settings. A chassis policy can be assigned to any number of chassis profiles to provide a configuration baseline for a chassis.  
  
To launch the Policies Table View, choose Configure > Policies.

The Chassis Policy creation wizard in Cisco Intersight has two pages:

  * General—The general page allows to select the organization and enter a name for policy. Optionally, include a short description and tag information to help identify the policy. Tags must be in the key:value format. For example, Org:IT or Site: APJ

  * Policy Details—The policy details page has properties that are applicable to UCS Chassis Policies.


Chassis Policies can also be cloned by using the Policy Clone wizard with properties that are similar to the existing policies. The clone policy action is available on both the policies list and detailed views. For more information, see [Cloning a Policy](https://intersight.com/help/saas/resources/cloning_a_policy#cloning_a_policy).

You can compare up to five policies of the same type from the Policies List View page to identify configuration differences, maintain consistency, and simplify troubleshooting.

To compare policies, select the checkboxes next to the desired policies, click the ellipsis (…) at the top left of the page, and choose Compare. On the Compare side drawer, only the differences between the selected policies are shown by default. To display all parameters, select All from the Display drop-down menu.

Note:

You can compare a minimum of two and a maximum of five policies of the same type at a time.

The following list describes the chassis policies that you can configure in Cisco Intersight.

  * IMC Access Policy—This policy enables configuration and management of the network by mapping IP pools to the chassis profile. It allows In-Band and Out-of-Band configurations, with association to an IP address from the IP pool. The policy also permits forwarding SNMP traffic over In-Band and Out-of-Band configurations.

  * Power Policy—Enables the management of power usage for the chassis. This policy allows to configure the redundancy mode of the Chassis Power Supply Units (PSUs) and allocate power to the chassis. You can view the redundancy health, redundancy mode, input power health, and output power health of the chassis in the properties section of the General tab on the Chassis details view page. For Cisco UCS X9508 Chassis, you can configure Power Save Mode and Dynamic Power Reallocation.

  * SNMP Policy—Configures the SNMP settings for sending fault and alert information by SNMP traps from the managed devices. SNMP Users or SNMP Traps configured previously on the managed devices are removed and replaced with users or traps that you configure in this policy. If you have not added any users or traps in the policy, the existing users or traps on the input/output module (IOM) are removed.

  * Thermal Policy—Allows to set the value of the Fan Control Mode for the chassis. The Fan Control Mode controls the speed of the chassis fan to maintain optimal server cooling.

