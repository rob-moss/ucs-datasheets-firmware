# Intersight SaaS System Locations

| | |
|---|---|
| **URL Title** | Intersight SaaS System Locations |
| **URL** | https://intersight.com/help/saas/system/locations |
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260316155144543/docs/cloud/data/resources/locations/en/locations.html |
| **HTML Title** | Geolocation |
| **Source file** | `ucs-docs-raw/html/intersight-saas_system_locations.html` |
| **File type** | HTML |
| **Fetched on** | 2026-03-19 15:36:36 |

---

# Geolocation

## Overview

Geolocation Management in Cisco Intersight provides a structured way to organize and visualize infrastructure assets based on their physical locations. By associating devices with geolocation data—such as physical addresses or GPS coordinates—administrators can achieve improved filtering, grouping, and operational insight across globally distributed environments.

This feature is available for **Unified Edge systems managed through Intersight, IMM Fabric Interconnect, UCSM Managed Fabric Interconnect** and **C-Series Standalone servers** that helps establish clear, location-based boundaries for infrastructure visibility and policy application.

Geolocation details only capture the physical site of the entity and do not include details such as site, building, or rack. Locations can be added using physical addresses or GPS coordinates.

GPS coordinates must be **unique** and duplicate latitude/longitude entries are not allowed. If a server or device is physically more than **10 meters** away from the defined GPS point, you may choose to enter a **physical address** instead of precise GPS coordinates.

## Adding a Location

Follow these steps to add a location.

  1. Log in to Cisco Intersight using the Location Management or Account Administrator role.

  2. Navigate to System > Locations and then click Add Location.

  3. On the Add Location page, choose to add locations individually or in bulk via a CSV file:

  * Follow these steps to add a single location:

       1. Click Single Location.

       2. In the Name field, enter a name for the location.

       3. (Optional) In the Set Tags field, enter a tag in the `key:value` or “keys/” format.

For example, Org: IT or Site: APJ.

       4. In the Input By section, choose one of the following options to enter the location details:

  * Address

Enter the physical address or a nearby landmark name (for example, Costco or Starbucks).

Alternatively, enter the city name and select the address from the suggested list. Suggested locations appear in order of proximity. After selecting the suggestion, modify Address 1 and Address 2 by clicking the Edit button next to Address Details.

Physical addresses support flexible combinations of address fields. You may define a location using any valid set of the Country, State, City and Postal Code. Examples of acceptable combinations include:

  * Country + State

  * Country + Postal Code

  * Country + State + City

Physical addresses can be edited at any time. Duplicate address combinations (including city and country) are not permitted.

  * GPS Coordinates

Enter latitude and longitude (up to four decimal places) in the GPS Coordinates field. Suggested locations appear in order of proximity. If the system cannot suggest any address for the coordinates, it allows for manual entry of all the location details, including Address 1 through to Country.

Note:

Only decimal values are accepted for GPS coordinates. Degree–minutes–seconds (DMS) format is not supported.

       5. Click Addto save.

The Address Details section displays City, State/Province, Postal Code, Country, and GPS coordinates. The new location appears in the All Locations list.

  * Follow these steps to add multiple locations using a CSV file:

       1. Click Multiple Locations (via File).

       2. Prepare a CSV file according to the following requirements:

  * The header row of the CSV file must contain the following fields:

_Name, Address 1, Address 2, City, State/Province, Country, Postal Code, Latitude, Longitude, Tags_

  * The field names must match the order listed above.

  * The file must have a `.csv` extension.

       3. Click Browse to locate and select the CSV file from the local system.

       4. Click Add.

The location information from the file is displayed on the Add Location page.


Location assignment can occur **during the target claim process**. The Location chosen during claim is automatically applied/propagated to the Unified Edge Chassis discovered in the process. For more information, see the [Assigning Location during Target Claim](../../../../../../../../../..html#assiging_location_during_target_claim) section.

## Assigning a Location

Follow these steps to assign a location to a Unified Edge Chassis, an IMM Fabric Interconnect, a UMM Fabric Interconnect, or a C-Series standalone server.

  1. Navigate to Operate > Unified Edge.

The list of all Edge servers is displayed.

  2. Click the desired server and scroll to the Location section on the Details page.

  3. Click Set.

The Set Location dialog box appears.

  4. Enter the location name.

  5. A list of suggested locations is displayed.

  6. Select the appropriate location and click Save.


A map view of the selected location is displayed. Path Tags set on a location are propagated to the Unified Edge chassis and all the servers within that chassis. For example, to apply a path tag such as Global/AMER/US/San Jose to a chassis, all compute nodes within that chassis will inherit this tag automatically. This propagation ensures consistent tagging across the chassis and its servers.

## Assiging Location During Target Claim

During the target claim process in Cisco Intersight, a location can be assigned to a chassis or server by associating the location tag with the target as part of the claim operation.

The process involves the following key steps:

  1. Log into Cisco Intersight with appropriate privileges (Account Administrator, Device Administrator, or Device Technician).

  2. Navigate to Admin > Taget > Claim a New Target.

  3. Select the target type and click Start.

  4. Enter the required details such as Device ID, Claim Code, and Location for the target device.

  5. During this process, the location tag set on the location is propagated automatically to the Unified Edge chassis and all servers associated with it.

  6. Complete the claim by clicking Claim, which assigns the location to the chassis and servers through propagation of the location tags.


This ensures that the location tags applied during the target claim process are consistently assigned to the chassis and all associated servers, enabling business-aware boundaries and management consistency. Tags configured on a Location—either during its creation or modification—are automatically propagated when that Location is assigned to a chassis during the claim process.

**Location Propogration**

Location propagation occurs automatically during the **target claim** process. Locations assigned to a **Unified Edge Chassis** are automatically propagated to its associated **Servers** and **Workload Instances**.

  * Propagation is **hierarchical** , flowing from the top-level target down to all associated components, including IMM, Fabric Interconnects (FI), UCS domains, and individual servers. This is a **one-time configuration** , ensuring consistent location information across all downstream resources.


A map view of the selected location is displayed. Path Tags set on a location are propagated to the Unified Edge chassis and all associated servers, enabling business-aware boundaries and management consistency. Tags configured on a Location—either during its creation or modification—are automatically propagated when that Location is assigned to a chassis during the claim process.

**Sorting based on Current Browser Location**

Intersight allows sorting locations based on proximity to your **current browser location**.

  * When this option is selected, the browser prompts you to grant permission for location access.

  * After permission is granted, Intersight automatically sorts the location list based on distance from your current position.


## Location Table View

  1. Navigate to System > Locationsto launch the Location Table view.

  2. Click the Settings icon (the gear icon) and select the columns that you want in the Table view. You can also edit and clone the table view from the settings menu.

You can view the following details in the Tags Table view:

  * **Name** — Displays the name of the location.

  * **Address 1** — Shows the primary street of the location.

  * **Address 2** — Lists any additional address information.

  * **City** — Indicates the city where the location is situated.

  * **State/Province** — Specifies the state or province of the location.

  * **Country** —Shows the country in which the location is found.

  * **Postal Code** —Displays the postal or ZIP code for the location.

  * **Latitude** —Indicates the geographical latitude coordinate of the location.

  * **Longitude** —Indicates the geographical longitude coordinate of the location.

  * **Tags** —Shows the tags or objects associated with the location.

  * **Export** —Export the location details displayed in the Table view to a CSV file. To export and save location details in CSV format, click the Export icon.

  * **Filtering** — allows to filer location using Name, Address, City, State, Country and Postal Code.


Locations in Cisco Intersight can be managed by clicking the ellipsis (**…**) and choosing from the following options:

  * **Edit** —Modify all details of the selected location.

  * **Delete** —Remove the selected location.

