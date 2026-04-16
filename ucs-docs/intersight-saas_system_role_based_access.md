# Intersight SaaS System Role Based Access

| | |
|---|---|
| **URL Title** | Intersight SaaS System Role Based Access |
| **URL** | https://intersight.com/help/saas/system/role_based_access |
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260414151805446/docs/cloud/data/resources/settings/en/Role_Based_Access_Control.html |
| **HTML Title** | Role-Based Access Control in Intersight |
| **Source file** | `ucs-docs-raw/html/intersight-saas_system_role_based_access.html` |
| **File type** | HTML |
| **Fetched on** | 2026-04-16 10:49:32 |

---

# Role-Based Access Control in Intersight

Intersight provides Role-Based Access Control (RBAC) to authorize or restrict system access to a user based on user roles and privileges. A user role in Intersight represents a collection of the privileges a user has to perform a set of operations and provides granular access to resources. Intersight provides role-based access to individual users or a set of users under Groups.

A User represents an entity that can log into a specific role in Intersight with a Cisco ID or a Single Sign-On credential configured on Intersight. A user is granted write or read-only access to the required system resources only if the specific role grants the access privileges to the role. For example, a user with the Server Administrator role can update server configurations, create and deploy a server profile, or perform server actions on the managed servers. However, the user cannot perform similar actions for a HyperFlex Cluster.

A Group represents a collection of users with a specific role, permission, and privileges. You can create multiple user groups to assign common roles and privileges to a set of users. If you make changes to a role or a privilege in a group, all users in a group inherit the same privileges.

A Resource Group is a logical container of resources which enables you to group and manage the resources. Resource Group allows you to divide the physical infrastructure or resources into groups without requiring dedicated physical infrastructure for each resource.

An Organization is a logical entity which enables multi-tenancy through separation of resources. Organization allows you to divide the physical infrastructure or resources through Resource Groups, without requiring dedicated physical infrastructure for each organization.

## Roles in Intersight

All user roles in Intersight are tied to a set of privileges, and enable a user to perform operations specific to the role. Based on your user role, you can claim a target, view or perform an action related to a Server, HyperFlex Cluster, Fabric Interconnect, or manage User Access and Permissions.

An Intersight Account Administrator or a User Access Administrator can add a user to an Intersight account and assign one or more roles to a User or a Group. You can view a list of users with the corresponding details of their roles in the Users table view, accessible from the Settings > Users.

A system-defined role is created by default in an account. Apart from the system-defined roles in Intersight, you can create a user-defined (custom) role. Each system-defined role has only one privilege associated with it whereas a user-defined role can comprise of multiple privileges. Intersight currently supports the following system-defined roles:

  * Device Technician

  * Device Administrator

  * HyperFlex Cluster Administrator

  * Server Administrator

  * User Access Administrator

  * Storage Administrator

  * Virtualization Administrator

  * Support Services


\- For a detailed description of the supported roles in Intersight and their associated privileges, how to add a User or Group, Create a Role or an Organization, and switch between roles, see [Role Based Access Control (RBAC) in Intersight](/help/resources#role_based_access_control_\(rbac\)_in_intersight).

\- To watch a demonstration of how to create an organization, create a custom role, define a privilege for an organization, and assign a target to one or multiple organizations, see [Introduction to Organizations](https://www.youtube.com/watch?v=2XzQi-0OUOo&feature=youtu.be).

\- For information about security in the Intersight platform, see [Security in the Cisco Intersight Platform](https://www.cisco.com/c/en/us/products/collateral/cloud-systems-management/intersight/solution-overview-c22-744638.html).

\- For frequently asked questions on Organizations and Roles, see [FAQs](/help/faqs).