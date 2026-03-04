# Intersight SaaS System Tags

| | |
|---|---|
| **URL Title** | Intersight SaaS System Tags |
| **URL** | https://intersight.com/help/saas/system/tags |
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260225095216527/docs/cloud/data/resources/tags/en/tags.html |
| **HTML Title** | Tags |
| **Source file** | `ucs-docs-raw/html/intersight-saas_system_tags.html` |
| **File type** | HTML |
| **Fetched on** | 2026-03-04 11:00:10 |

---

# Tags

## Overview

Tags in Cisco Intersight are metadata labels that help organize, search, and manage resources such as servers, chassis, Fabric Interconnects, and workload instances. There are two main types of tags supported:

  * **Key-Value Tags** : Flexible, user-defined tags that consist of a key and a value.

  * **Path Tags** : Hierarchical, centrally managed tags that represent the organization and relationships between resources.


Path tags are distinct from generic key:value tags primarily due to their hierarchical nature and propagation feature. While both can be applied to various objects, currently only path tags automatically propagate from a Unified Edge chassis to its associated blade servers. Generic key:value tags do not have this automatic propagation feature currently.

**Key-Value Tags**

Key-value tags in Cisco Intersight are generic metadata pairs that users can freely assign to resources. Each tag consists of a **key** and a **value** (for example, Environment: Production). These tags are highly flexible and allow users to:

  * Group and categorize resources based on custom criteria

  * Simplify searching and filtering for specific assets

  * Adapt resource organization to unique user or team needs


Key-value tags are managed in a decentralized manner—any user with appropriate permissions can create and apply them. However, they do **not** support hierarchical organization or automatic propagation between related resources.

**Path Tags**

Path tags provide a hierarchical method for organizing resources in Cisco Intersight. Administrators define these tags centrally, creating a structure that reflects organizational needs such as function, location, or business unit.

Path tags enable:

  * Grouping resources into meaningful, hierarchical groups (e.g., /Region/Datacenter/Rack)

  * Easier management of large, geographically distributed environments

  * Unified and consistent tagging, since definitions are managed centrally

  * Automatic propagation of tags based on hierarchy and object type

Propagation depends on the hierarchy level and object type. Unified Edge, Fabric Interconnect, Chassis, and Standalone Servers all support downward propagation to their related components, including alarms and server profiles.


Centralized management ensures that path tags are consistently applied, providing enhanced visibility and control across the entire environment. This makes path tags ideal for organizations that require structured and scalable resource management.

Note:

  * While both tag types help organize and manage resources, only path tags offer hierarchical grouping and automatic propagation.

  * Key-value tags remain useful for custom, ad-hoc organization needs.


**Example:**

  * **Key-Value Tag** : Department: Finance

  * **Path Tag** : /Location/Building/Floor/Room


## Key Features - Path Tags

  * **Centralized Path Tag Management** —All tag definitions are maintained in a centralized repository, serving as the authoritative source for creating, reading, updating, and deleting (CRUD) tag definitions. Path tags can be viewed and assigned by all users, but only those with the Account Administrator or Tag Management role can create, update, or delete tags.

  * · **Path tag Hierarchy and Structure** —Path tags in Intersight are case-sensitive and can use hierarchical names, with each level separated by a forward slash ("/").

The maximum length for a path tag is 50 characters. The colon (:) character is not allowed because it is reserved as a separator for generic tags (_key:value_).

For example, a tag like L1/L2/L3/L4/L5 represents a hierarchy, where each part indicates a different level. Although tags look hierarchical, Intersight stores them in a “flat” structure. This means that, for the example above, five individual tags are created:

  * L1,

  * L1/L2,

  * L1/L2/L3,

  * L1/L2/L3/L4,

  * L1/L2/L3/L4/L5.

This approach preserves the tag hierarchy while allowing for efficient storage and searching.

Note:

If you attempt to create a tag with the exact same name as an existing one (for example, "L1"), you cannot create another tag with that exact name. However, you can create hierarchical path tags (for example, "L1/L2") even if a parent segment (for example, "L1") already exists as a standalone tag. These are considered distinct due to their hierarchical structure.

  * **Propagation of Path Tags** —When a path tag is applied at any level within the infrastructure hierarchy, it is automatically propagated to all objects below that level. The propagation follows this order:

Fabric Interconnect → Chassis → Blades → Alarms → Server Profile

Fabric Interconnect → Rack Servers → Alarms and Server Profiles

Unified Edge Chassis → Blade → Alarms and Server Profiles

For **standalone servers** , path tags propagate to **Alarms** and **Server Profiles** linked to those servers.

If a path tag is assigned to a location, it propagates to all associated **Fabric Interconnects (FI-A and FI-B)** , **Chassis** , and **Standalone Servers** , and then continues down through the hierarchy.

However, **path tags applied directly to one Fabric Interconnect** do not synchronize to the other Fabric Interconnect. They propagate only downward from the one where they are applied.

Note:

Path tags can be assigned to any supported object. Propagation depends on the hierarchy level and object type. Unified Edge, Fabric Interconnect, Chassis, and Standalone Servers all support downward propagation to their related components.


**Path Tag Modification**

  * **Renaming** —Only one level of a path tag hierarchy can be renamed at a time. When a level is renamed, the change automatically propagates to all related sub-tags that depend on that level.

For example, if the tag `A/B/C` is changed to `AA/B/C`, the following updates occur:

  * A becomes AA

  * A/B becomes AA/B

  * A/B/C becomes AA/B/C

  * Any sub-tag, such as A/B/C/D, becomes AA/B/C/D

Note:

Adding or removing entire levels in the hierarchy is not supported.

  * **Deletion** —A path tag can be deleted only if it is not assigned to any object. When an unassigned parent tag is deleted, all of its unassigned child tags are deleted automatically. If a tag or any of its child tags are currently assigned, they must be unassigned before deletion.


## Tags Table View

Navigate to **System > Tags **to launch the Tags Table view. From this page, tag actions can be performed and navigation to the Tag details page is possible.

Click the Settings icon (the gear icon) and select the columns desired in the Table view.

![](../files/Tags_Table_View.png)

**Tags Table Summary Widget**

The following widgets are available in the Tags table view:

  * **Usage** –Displays the count of tags currently in use and the number of unused tags.

  * **Primary Tagged Object Types – Top 5** –The top 5 source object types (such as Location, Chassis Profile Template, Chassis, and so on) associated with the tags.


The following details can be viewed in the Tags Table view:

  * **Tag** –The tag name.

  * **Usage** –Indicates whether the tag is in use and shows the total number of times the tag has been applied. For hierarchical tags, the usage count is cumulative: a parent tag displays the total usage of all its child tags as well as itself.

  * **Primary Tagged Object Type** –The source object that was tagged, not including all objects tagged as a result of system propagation. Click the tag name to see all related objects.


In Cisco Intersight, clicking the ellipsis (…) icon allows tag actions to be performed. The actions enable management of the tags.

  * **Rename** –Change the name of a tag or any part of its hierarchical path.

  * **Add Subtags** –Create a new subtag beneath an existing tag to further organize resources.

  * **Delete** –Remove a tag that does not have any subtags beneath it.


In addition, the following actions can be performed:

  * **Create Tag** –Create a new tag.

  * **View Tagged Objects** –View a list of all objects associated with a specific tag.

  * **Expand All / Collapse All** –Expand All opens every level of the tag hierarchy to display all parent and child tags at once, while Collapse All hides all nested levels to return to a compact view.


## Tags Detailed View

When a tag is selected in the Tags table view, a Tag details page with information specific to the tag is displayed. In addition to the tag details, the Tagged Objects can be viewed.

## Creating Path Tags

Path tags in Intersight let you organize resources using a hierarchy within the tag name, created by separating levels with the “/” character. This makes it easy to represent complex relationships—such as location or function—when organizing your resources. For example, a tag like NorthAmerica/USWEST/CA/SJC clearly shows a structure from continent to city. Intersight supports up to five levels of hierarchy, allowing you to manage and filter resources efficiently without any added complexity in how the tags are stored or used.

![](../files/Tags.png)

To create path tags, do the following:

  1. Log in to Cisco Intersight with Tag Administrator role or privilege.

  2. Navigate to the System > Tags page.

  3. Click Create Tag.

  4. Enter the desired tag name.

Note:
  * Use the “/” character within tag keys to indicate hierarchy and nesting.

  * You can specify a maximum of five levels of hierarchy.

  5. Click Create.

The new tag appears on the screen, and you can expand or collapse its hierarchy.


## Adding a Subtag

Subtags extend the hierarchical structure of an existing tag. They allow for further categorization within a parent tag.

To create a subtag, do the following:

  1. Log in to Cisco Intersight with Tag Administrator role or privilege.

  2. Navigate to the **System > Tags** page.

  3. Select the existing tag and the hierarchy to which you want to add a subtag.

  4. Click the ellipsis **(…) > Add Subtag**.

  5. Enter the desired tag name. Use the “/” character within tag keys to indicate hierarchy and nesting.

You can specify a maximum of five levels of hierarchy.

  6. Click **Add**.


## Renaming a Path Tag

Tags can be renamed by changing the name of an existing segment. The change is automatically propagated to all managed objects where the original tag was assigned or propagated.

When a tag is renamed, the overall hierarchy (adding or removing levels) cannot be changed.

To rename a tag, do the following:

  1. Log in to Cisco Intersight with Tag Administrator role or privilege.

  2. Navigate to the **System > Tags** page.

  3. Locate the full path of the tag you want to rename.

  4. Click the ellipsis **(…) > Rename**.

  5. Enter the new name for the path tag.

When you rename a tag, you cannot add, remove, or move hierarchy levels, nor change the parent of the tag.

  6. Click **Rename**.

The update is automatically reflected on all managed objects that had the original tag assigned or propagated.


## Deleting a Path Tag

To delete a path tag, do the following:

  1. Log in to Cisco Intersight with Tag Administrator role or privilege.

  2. Navigate to the **System > Tags** page.

  3. Locate the full path of the tag you want to delete.

Note:
  * Path tags, once assigned to resources, cannot be directly deleted. Instead, they must be "unset" from each associated resource. While you can unset tags from multiple items within a specific resource's view, there is no single global action to unset a tag across all resources simultaneously. This approach ensures careful management and prevents unintended impacts, especially given varying user permissions.

  * If a tag has subtags defined under it, you must delete all of its subtags before you can delete the main tag itself. Only tags that do not have any subtags—those at the end of the hierarchy—can be deleted.

  4. Click the ellipsis **(…) > Delete**.


## Associating a Path Tag

Path tags in Cisco Intersight are centrally managed by Account Administrators or Tag Administrators, who define the hierarchical structure of these tags. Once the hierarchy is created, users can associate the appropriate path tags with relevant resources such as Fabric Interconnects, Unified Edge chassis, standalone servers, and locations—enabling centralized management with flexible usage for easier organization and control.

Path tags can be assigned to any supported resource. Propagation behavior depends on the hierarchy level and object type. Unified Edge, Fabric Interconnect, Chassis, and Standalone Servers all support downward propagation to their related components, including **alarms** and **server profiles**.

Tags must already exist in the tag management system before they can be assigned. Users with **Account Administrator** or **Tag Administrator** privileges can create new tags.

To assign a path tag to a resource, complete the following steps:

  1. Navigate to the resouce (for example Operate > Unified Edge).

  2. Click the resource for which you want to specify the tag and scroll to the Tags section on the Details page.

  3. Click **Set**.

The Set Tags dialog box appears.

  4. Enter the tag name. A list of suggested tags is displayed.

  5. Select the desired tags from the existing tag definitions.

Note:

If you have Account Administrator or Tag Administrator privileges, you can create a new tag by typing the tag name and clicking **+Create**.

You can create a tag using the "_key:value_ " format or create a path tag using the "key/" syntax, where the "/" character indicates hierarchy and nesting.

  6. Click **Save**.

