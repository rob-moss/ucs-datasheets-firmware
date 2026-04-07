# Intersight SaaS Configure Custom HCL guide

| | |
|---|---|
| **URL Title** | Intersight SaaS Configure Custom HCL guide |
| **URL** | https://intersight.com/help/saas/configure/custom_hcl |
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260402103337138/docs/cloud/data/articles/features/custom_hcl/configure/en/index.html |
| **HTML Title** | Custom HCL Baseline |
| **Source file** | `ucs-docs-raw/html/intersight-saas_configure_custom_hcl.html` |
| **File type** | HTML |
| **Fetched on** | 2026-04-08 08:43:17 |

---

# Custom HCL Baseline

Create custom hardware compatibility list (HCL) baselines for servers, where each server is evaluated against user-defined hardware compatibility baselines and assigned a compliance status based on the defined configuration. This feature enables self-validation of servers to ensure compliance and consistency.

  * A maximum of 100 baseline configurations can be created in an account.

  * A baseline status is created at the organization level for each server when a baseline configuration is defined.

  * The compliance status is re-evaluated whenever there are changes to the server or the baseline configuration.

A periodic process runs every two minutes to detect any changes in newly created or modified baseline configurations and evaluates the baseline status of the servers accordingly.

Any modification to the server configuration, such as updates to firmware, operating system, adapter firmware, or drivers, immediately triggers a re-evaluation of the baseline status.

Note: This feature is applicable for Cisco UCS servers only.

Refer to the use cases for detailed examples and guidance. For more information, see [Use Cases](/help/configure/custom_hcl#use_cases).

  * The following Cisco servers are not supported for Custom HCL:

  * UCSXE-130C-M8-12

  * UCSXE-130C-M8-32

  * UCSXE-130C-M8-20

  * CAI-845A-M8

  * UCSC-885A-M8


## Creating Custom HCL Baseline

Create a custom HCL baseline in two ways:

  * Entering details manually in the custom HCL configuration page—This method allows you to input the hardware compatibility details manually through a dedicated custom HCL configuration page.

  * Importing HCL configuration from a server—This involves importing the configuration details from the server.


  1. Log in to Cisco Intersight as an Account Administrator or Server Administrator role.

  2. Choose Configure > Custom HCL.

  3. Click Create Custom HCL.

  4. On the General page, configure the following parameters, and then click Next.

Property| Description  
---|---  
Organization| Select the Organization.Note: To create a baseline for servers across multiple Organizations, you can establish the baseline within a shared Organization.  
Name| Enter a name for the custom HCL baseline.  
Set Tags (Optional)| Enter a tag in the key:value format. For example, Org: IT or Site: APJ.  
Description (Optional)| Provide a short description to help identify the custom HCL baseline.  
Import HCL Configuration from a Server (Optional)| 
     1. Click Select Server to open a side drawer displaying details of the available servers.
     2. Choose the server whose configuration you want to use to create the baseline.
     3. To view more information about a server, click the ![](../../../../../../../en/us/td/i/400001-500000/490001-500000/491001-492000/491173.png) icon next to it; the server details will be displayed.
     4. Click Select.
     5. To change the server selection, click Edit Selection.
     6. To remove the selected server, click the ![](../../../../../../../en/us/td/i/400001-500000/490001-500000/494001-495000/494827.png) icon.  
  
  5. On the Custom HCL Configuration page, provide the hardware, software and adapter details as required.

Note: If you choose to Import HCL Configuration from a Server on the General page, the Custom HCL details are automatically populated on the Custom HCL Configuration page. You can modify these details as needed.

Custom HCL Configuration Option| Description  
---|---  
Server Hardware Compliance  
Generation| Select the generation of server from the drop-down list.  
Server Model| Refers to a specific Cisco UCS server model being evaluated for hardware and software compatibility.Select model allows multiple models from a chosen generation to be selected if the generation has already been specified. If Generation is not specified, multiple servers across different generations can be selected.  
CPU Family| Select the family to which a specific CPU belongs.  
Firmware Version| Enter either the complete firmware version, such as 4.3(4.24xxxx), or a partial version, like 4.3(4).The firmware version selected or entered by the user does not need to match the version currently running on the server; users can customize the version as needed, even if it differs from the existing one. Alternatively, users may choose to enter only the firmware version without providing server details.  
Management Mode| Select the mode in which the server is managed.  
Server Software Compliance  
OS Vendor| Select the vendor or manufacturer of the operating system.  
OS Version| Select the exact version of the operating system detected or assigned to a host or server.Note: You can select the OS vendor and OS version from the drop-down lists provided in the interface. If the specific OS vendor or OS version you need is not available in these lists, you can type them into the corresponding fields.  
Adapter Compliance  
Add Adapter| Click Add Adapter and specify the following:
  * Type—Specifies to the specific model, GPU, SSD or category of network or storage adapters installed in a Cisco UCS system or related infrastructure.
  * Model—Specifies to the adapter model being evaluated for compatibility within Cisco UCS systems. For example, UCSC-M-V5Q50GV2.
  * Driver Protocol—Specifies the driver name used by the device driver to interact with the hardware adapter. For example, enic, fnic.
  * Driver Version—Specifies the exact version of the device driver installed for a particular hardware adapter in the Cisco UCS environment. For example, 2.0.0.105-348.0.
  * Firmware Version—Specifies the running firmware version installed on the adapter component. For example, 5.4(1.34).
  * Vendor—Specifies the manufacturer or supplier of the adapter component or device.Note: The driver protocol and driver version can be configured only when the OS version and OS vendor is configured.You can add up to 20 adapters.Either one of the six fields is enough for the adapter configuration.If a particular column is not visible, click the gear ![](../../../../../../../en/us/td/i/400001-500000/490001-500000/491001-492000/491610.png) icon to choose and show more columns in the server table. This lets you add or remove columns to customize your view.  
  
  6. Click Next.

  7. On the Summary page, verify the custom HCL baseline details and its associated configuration.

  8. Click Create.

The newly created custom HCL baseline is listed in the Custom HCL Table View.

You can edit, clone, and delete the custom HCL baselines in the Custom HCL Table View. For more info, see [Managing Custom HCL Baseline](/help/configure/custom_hcl#managing_custom_hcl_baseline).


## Custom HCL Table View

Choose Configure > Custom HCL to launch the custom HCL table view. From this page, you can review detailed information about the custom HCL status of the baselines, including whether each baseline is compliant with Cisco HCL or not. Click the settings icon (the gear icon representation), and select the columns that you want in the Table view.

You can add specific columns or custom tags to the Custom HCL Table view to sort and filter. Columns in the Custom HCL Table view can be sorted using the sort option. You can also apply filters based on any column using the Filters option to view and explore the Custom HCL inventory.

**Custom HCL Table Summary Dashboard**

All widgets except Custom HCL Conformance are dynamic and change based on the Add Filter option you select.

The following widgets are available in the Custom HCL Table view:

  * Status—Displays the status of the baseline configuration. The compliance status can be:

  * Active—This custom HCL definition has been fully evaluated, and the compliance status for all eligible servers is current.

  * Pending—The custom HCL compliance assessment is currently pending due to recent changes made to the Custom HCL Baseline.

  * In-Progress—The custom HCL compliance assessment is currently in progress and typically takes approximately 2-3 minutes to complete the baseline assessment.

  * Cisco HCL Status—Displays the number of servers grouped based on their status.

For more information, see [Viewing Hardware Compatibility List Status](/help/resources/compliance_with_hcl#viewing_hardware_compatibility_list_status).

  * Custom HCL Conformance—Displays the count of the conforming and non-confirming servers for all the defined baselines.


Below the dashboard is a tabular list displaying the following information:

  * Name—The name of the custom HCL baseline.

  * Status—The current processing state of the custom HCL definition, indicating if it is active, pending, or in-progress.

  * Cisco HCL Status—Indicates if the custom HCL baseline is compliant to Cisco HCL or not. The Cisco HCL status widget can have any of the following values:

  * Validated—Indicates that the server configuration has been validated and is found in the compliance database.

  * Not Listed—Indicates that the server configuration has not been tested and validated, or it is not listed in the compliance database.

  * Not Evaluated—Indicates that the compatibility evaluation has not been performed for that particular hardware or software combination.

  * Not Applicable—Indicates that the baseline configuration is not applicable to the server.

  * Conforming Servers—Count of servers conforming to custom HCL baseline.

  * Non-Conforming Servers—Count of servers not conforming to custom HCL baseline.

  * Last Update—The last updated date and time.

  * Organization—The organization name.


## Custom HCL Baseline Details View

From the Custom HCL, click a custom HCL name to open the Custom HCL Details view. This page has two tabs: General, and Baseline Status Details.

  * General—Displays the hardware, software, and adapter details and has two sections: Details and Configuration. The Details section displays the Name, Status, Cisco HCL Status, Last Update, Description, Organization and any configured Tags. The Configuration section displays Server Hardware Compliance, Server Software Compliance and Adapter Configuration details.

  * Baseline Status Details—Displays the baseline status of servers in relation to a defined baseline, where you can view the hardware, software, and adapter compliance.

When the baseline specifies a greater number of adapters than are installed on the specific server, the adapter compliance status is marked as non-compliant. This is because the server lacks the adapters required by the baseline configuration, resulting in a mismatch between the server's hardware and the baseline-defined adapters.

You can edit, clone, and delete the Custom HCL configuration using the ellipsis (…) in the Custom HCL Table view or using the Actions drop-down in the Custom HCL Details view.


Also you can:

  * Use the search bar to search for a specific custom HCL baseline. You can use filters to refine the displayed information.

  * You can export the displayed information in the Table view to a CSV file.

  * To export and save it in a CSV file format, click the Export icon.


Clicking the eye ![](../../../../../../../en/us/td/i/400001-500000/490001-500000/491001-492000/491173.png) icon displays the detailed information about the selected server indicating whether it is Confirming, Non Confirming, or Not Applicable.

You can export the displayed information in the Table view to a CSV file. To export and save it in a CSV file format, click the Export icon. The adapter details get exported. Also, refine the information displayed by applying various filters. Click the gear ![](../../../../../../../en/us/td/i/400001-500000/490001-500000/491001-492000/491610.png) icon to choose and show more columns or to edit the view.

Exporting a detailed Baseline Status report that includes adapter details is currently not supported from the Custom HCL Status Details page.

To fetch the OS details and adapter driver information, run the OS Discovery Tool (ODT) directly on the server. For more information, see [OS Discovery Tool](https://intersight.com/help/saas/resources/os_discovery_tool#about_os_discovery_tool) and Cisco UCS Tools for [VMware ESXi](https://intersight.com/help/saas/resources/cisco_ucs_tools#about_cisco_ucs_tools).

## Managing Custom HCL Baseline

To create your own custom view tab, click + and specify a name and then choose the required parameters that need to be displayed in the Columns, Tag Columns, and Widgets.

Note: You can export the displayed information in the Table view to a CSV file. To export and save it in a CSV file format, click the Export icon. You can use the search bar to search for custom HCL baseline. Moreover, you have the option to refine the information displayed by applying various filters tailored to your specific needs.

  1. Log in to Cisco Intersight with Account Administrator or Server Administrator role.

  2. Choose Configure > Custom HCL.

You can perform edit, clone, or delete operations from the Actions drop-down list.

  * To edit a Custom HCL Baseline:

       1. Click the ellipsis (…) next to the custom HCL baseline that you want to modify, and select Edit.

       2. In the Edit Custom HCL page, edit custom HCL name, tags, description, hardware, software, and adapter details as required, and click Next.

Note: The organization name cannot be edited.

       3. On the Summary page, verify the custom HCL baseline details.

       4. Click **Save**.

  * To clone a Custom HCL Baseline:

       1. Click the ellipsis (…) next to the custom HCL baseline that you want to clone, and select Clone.

       2. In the Clone page, enter the Name of the custom HCL baseline. Optionally, enter the Description and Tags.

       3. To clone to a different Organization, choose the desired organization from the Organization drop-down list.

Note: Skip this step if you are cloning within the same Organization.

       4. Click **Clone**.

  * To delete a Custom HCL Baseline:

       1. Click the ellipsis (…) next to the custom HCL baseline that you want to delete, and select Delete.

       2. Click **Delete**.


## Use Cases

**Scenario 1**

A server’s Cisco HCL status is marked as Not Listed when the adapter’s driver version is newer than the recommended version, causing a mismatch. This means the server’s configuration is not recognized as validated in the Cisco HCL.

**Workarounds/Solution**

Create a baseline by importing server hardware, software, and adapter info, then compare servers to this baseline to confirm they match the expected setup.

**Scenario 2**

As a server administrator, to upgrade all servers to a new firmware version such as 'firmware_2026', you can create and use a baseline configuration targeting that firmware version.

**Workarounds/Solution**

As servers are upgraded to firmware_2026, their compliance status is tracked in the baseline configuration. This compliance tracking helps monitor the upgrade progress and ensures all servers have the required firmware version.

**Scenario 3**

Support different driver versions for the same hardware, firmware, and operating system.

**Workarounds/Solution**

When a user chooses one driver version to standardize on, they can use custom HCL report to find servers that do not match their chosen driver version. This helps identify non-compliant servers.