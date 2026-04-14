# Intersight Appliance Settings

| | |
|---|---|
| **URL Title** | Intersight Appliance Settings |
| **URL** | https://intersight.com/help/appliance/settings |
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260402103337138/docs/onprem/data/articles/settings/en/index.html |
| **HTML Title** | Appliance Settings |
| **Source file** | `ucs-docs-raw/html/intersight-appliance_settings.html` |
| **File type** | HTML |
| **Fetched on** | 2026-04-13 13:33:17 |

---

# Appliance Settings

You can monitor the appliance status, backup and restore data, upgrade the appliance software, configure network settings, add users and groups, and more on the Intersight Virtual Appliance Settings screen. The following sections describe the actions that you can perform in the Settings screen.

## Configuring a Banner Message for Displaying Before the Login Screen

You can configure a banner message in Intersight Virtual Appliance. When enabled, the configured banner message will be displayed before the user login screen.

To configure a banner message, do the following:

  1. Log into Intersight Virtual Appliance as a user with account administrator role.

  2. Choose Settings > System > Banners.

  3. Click Configure.

The Configure Banner Message window displays.

  4. Update the following fields as needed.

  * Show banner message before login—Enable this option.

  * Banner Title—Enter a title for the banner message. The length of the title cannot exceed 128 characters.

  * Banner Content—Enter the contents for the banner message. The content in this field has to be less than 2000 characters.

  5. Click Save.

The configured banner message content along with the title is displayed in the Banners preview window.


## Updating the Intersight Connected Virtual Appliance Software

Intersight Connected Virtual Appliance provides a way to either update automatically when new versions are made available by the update service, or to manually update to any available version that is higher than the running version.

When Connected Virtual Appliance is configured to update in the **Automatic** mode, it obtains bundles directly from the cloud to update the service packages, OS packages including the kernel, and other security fixes. Based on the selection made during the configuration, installation will occur as per the system default or custom installation settings. In the automatic mode, if there are no new updates available for more than 90 days, ensure that the appliance is connected to Intersight.

When the appliance is configured to update in the Manual mode, you have a choice of either uploading the software image from the local machine or from a network share server, depending on where you saved the software image. Once the software image is uploaded, you can choose to install the update immediately, or you can schedule a date and time for the installation. Note that you need to download the required software packages from the Appliance Portal for manually updating your Connected Virtual Appliance. For more information, see [Creating an Appliance Account](/help/appliance/getting_started/software_downloads/creating_an_appliance_account) and [Downloading Software Packages for Intersight Virtual Appliance](/help/appliance/getting_started/software_downloads/downloading_software_packages_for_appliance).

You can switch between the two software update modes at any time. However, if an update is pending, switching to a different mode will cancel the pending update. For example, if you have a pending update in **Automatic** mode and switch to **Manual** mode, the pending update will be canceled.

Note:

  * It is recommended that you use the Automatic mode for updating the appliance.

  * It is highly recommended that you check the Appliance Account regularly for updates and remain on the latest version of the Intersight Virtual Appliance software, which is continuously enhanced with new features and improvements.

It is also important to note that only the latest major release version ("N") and the three previous major versions ("N-1," "N-2," and "N-3") are supported. Additionally, patch release versions for each supported major release are also supported. For example, if the latest major release is version 1.1.3-0, then:

  * Supported major release versions include 1.1.3-0, 1.1.2-0, 1.1.1-0, and 1.1.0-0.

  * Supported patch release versions include 1.1.3-x, 1.1.2-x, and 1.1.1-x.

  * Ensure that the version of the appliance that you are manually uploading for installation is always higher than the running version.

  * There is no difference between an upgrade on a multi-node appliance versus an upgrade on a single-node appliance as the upgrade is done at the cluster-level and not at the node-level.

  * Intersight Virtual Appliance patch bundles are supported for specific software versions only. For more information about appliance release versioning scheme, see [Intersight Virtual Appliance Patch Releases](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide/m_updating_the_intersight_virtual_appliance_software.html#appliance-versioning-scheme).


Before you begin: Ensure that Intersight Connected Virtual Appliance is connected to Intersight.

Use the following instructions to update Connected Virtual Appliance:

  1. Log into Intersight Virtual Appliance as a user with account administrator role.

  2. Choose Settings > System > Appliance Updates.

In the Automatic mode of configuration, the following details are displayed:

  * Running Version—The current software version number

  * Update Mode—Automatic

  * Installation Schedule—Displays the date and time when the update is scheduled

In the Manual mode of configuration, the following details are displayed:

  * Running Version—The current software version number

  * Update Mode—Manual

In both the modes, you may see the following details about the Pending Update:

  * Version—Indicates the software version that is scheduled to be updated

  * Update Impact Type—This could be Disruptive, Disruptive-reboot, or None. The impact could be disruptive because of an infrastructure upgrade or upgrade of other Intersight services. A disruptive update may cause Intersight to be unavailable for the duration specified in Update Impact Duration. The disruptive reboot of the appliance could be caused by kernel updates and restarting of services. A grace period is provided to help you plan and manage the update better. The UI displays appropriate messages to guide you if there is a disruptive reboot.

Attention:

An appliance update could take about 90 minutes to complete.

During this time, some features will be temporarily unavailable.

It is recommended that you take a backup prior to triggering the update and do not reboot your appliance. If there is a requirement to reboot, Intersight Appliance does it automatically.

  * Installation Date/Time —Displays the date and time when the update is scheduled. You can click on the pencil icon to edit the installation date and time.

  * Release Notes—Includes a link to the "What's New" information in the Appliance Help Center.

The Appliance Updates screen also displays a table view of the appliance software updates under Update History. This table lists the installation date, appliance software Version, a description of the software version, and the status of the installation of the update. From this table view, you can search for a specific version of the software and the date it was installed on and the status of the installation.

  3. Click Update Settings to configure a software update.

  4. On the Appliance Updates screen, make your selections for the update mode of configuration by choosing either the automatic or the manual mode.

For the Automatic mode:

     1. Select Automatic mode for updates.

     2. Select either System Default or Custom for the installation schedule.

**System Default** —Appliance updates are installed according to default appliance settings and customized configurations.

        1. **[Optional]** Enable Block Update Dates and specify the start and end of the block dates. During this period, the appliance will not be updated.

        2. Choose a strategy to update Intersight intelligence. For more information, see [Updating Intersight Intelligence for Intersight Connected Virtual Appliance](/help/settings#updating_intersight_intelligence_for_intersight_connected_virtual_appliance).

        3. Click Save.

**Custom** —Appliance updates are installed automatically based on the settings configured by you.

        1. **[Optional]** Enable Custom Grace Period and set your preferred grace period (1—6 weeks) for updates that require a reboot and for updates that do not require a reboot. This setting applies only to updates received subsequent to the setting of the custom grace period and not to any existing updates that are already pending.

        2. **[Optional]** Enable Block Update Dates and specify the start and end of the block dates. During this period, the appliance will not be updated.

        3. Choose a strategy to update Intersight intelligence. For more information, see [Updating Intersight Intelligence for Intersight Connected Virtual Appliance](/help/settings#updating_intersight_intelligence_for_intersight_connected_virtual_appliance).

        4. Click Save.

For the Manual mode:

     1. Select Manual mode of update.

Choose a strategy to update Intersight intelligence. For more information, see [Updating Intersight Intelligence for Intersight Connected Virtual Appliance](/help/settings#updating_intersight_intelligence_for_intersight_connected_virtual_appliance).

     2. Click Save.

     3. Navigate to Settings > System > Appliance Updates, and click Install Updates.

The Upload Appliance Software screen is displayed.

     4. Select either Local Machine or Network Share, depending on where you saved the software image.

        1. For the Local Machine option, browse to the location from where you want to upload the image and click Next.

        2. For the Network Share option, enter the protocol and enter details of the remote server from where you want to copy the file, and click Next.

  * Protocol—Communication protocol used for file transfer. Intersight Virtual Appliance currently supports CIFS (Common Internet File System), SCP (Secure Copy Protocol), and SFTP (Secure File Transfer Protocol).

  * Server IP/Hostname—The network share server from where the file is copied

  * Port—TCP port to use

  * Location—Directory where the file to be copied is stored

  * Filename—Name of the file to be copied from the network share

  * Username—Username for authenticating with the network share

  * Password—Password for authenticating with the network share

        3. Select to install immediately or schedule the installation for a later date and time.

        4. Click Apply.

You can track the upload progress by clicking on the Requests icon.

When the upload completes, you will see details about the Pending Update on the Software screen. From the Pending Update Details section, you will be able to cancel an update, update immediately, or edit the installation date and time.

Note:

In the Manual mode, if you cancel a pending update, you will need to upload the appliance software again to be able to initiate an update.


Note:

If the update fails and if the update is recoverable, the Update History shows the installation as Failed, and the existing Pending Update Details remains as-is. You can try the upgrading process again. For more information about the update errors and possible resolutions, see [Troubleshooting Appliance Update Failure Issues](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide/m_updating_the_intersight_virtual_appliance_software.html#Cisco_Reference.dita_b1e630cc-e864-4635-97d8-076604a10894).

If the update fails and if the update is non-recoverable, the Update History shows the installation as Failed, and you will no longer see any existing Pending Update Details. However, all existing features and functionality continues to work as before. You can try the upgrade process again. For more information about the update errors and possible resolutions, see [Troubleshooting Appliance Update Failure Issues](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide/m_updating_the_intersight_virtual_appliance_software.html#Cisco_Reference.dita_b1e630cc-e864-4635-97d8-076604a10894).

After the update, if you use the same browser to log into the appliance, you might encounter an Error code: SEC_ERROR_REUSED_ISSUER_AND_SERIAL. To fix this issue, you will need to remove the system-generated certificate of the server from the same browser that you are using to log into the appliance. For example, to remove the system-generated certificate of the server from Google Chrome, navigate to Settings > Privacy and security > Manage certificate. Select the system-generated certificate that you want to remove, click Remove, and click Close. Close the browser, and then log into the application from a new browser. For more information about certificate, see [Add Certificates](/help/settings#add_certificate).

## Updating Intersight Intelligence for Intersight Connected Virtual Appliance

Intersight Connected Virtual Appliance allows you to update Intersight intelligence such as Hardware Compatibility List (HCL) and Advisories as soon as it becomes available, independent of the appliance software upgrade schedule.

Updates for HCL include the compatibility validation results and compliance status for server model, processor, firmware, adapters, operating system and drivers. For more information about HCL, see [Compliance with Hardware Compatibility List (HCL)](/help/appliance/resources#compliance_with_hardware_compatibility_list_\(hcl\)).

Intersight alerts users about the endpoint targets that are impacted by supported security advisories and field notices. These alerts are displayed as Advisories in Intersight. For a complete list of supported security advisories and field notices, and acknowledging advisories, see [Intersight Advisories](/help/appliance/resources#intersight_advisories).

To update Intersight intelligence for Connected Virtual Appliance, do the following:

  1. Log into Intersight Connected Virtual Appliance as a user with account administrator role.

  2. Choose Settings > System > Appliance Updates.

  3. Click Update Settings .

The Update Settings window displays.

  4. Select Update Intersight Intelligence Immediately and click Save.


## Updating the Intersight Private Virtual Appliance Software

Intersight Private Virtual Appliance provides a way to manually update the software to any available version that is higher than the running version. You have a choice of either uploading the software image from the local machine or from a network share server, depending on where you saved the software image. Once the software image is uploaded, you can choose to install the update immediately, or you can schedule a date and time for the installation.

You can download the required software packages from the Appliance Portal for manually updating your Private Virtual Appliance. For more information, see [Creating an Appliance Account](/help/appliance/getting_started/software_downloads/creating_an_appliance_account) and [Downloading Software Packages for Intersight Virtual Appliance](/help/appliance/getting_started/software_downloads/downloading_software_packages_for_appliance).

Note:

It is highly recommended that you check the Appliance Account regularly for updates and remain on the latest version of the Intersight Virtual Appliance software as it is continuously improved to include new features and enhancements. It is also important to note that only "N-3" software versions of the product are supported, with "N" being the latest version of appliance software.

Ensure that the version of the software that you are manually uploading for installation is always higher than the running version.

Before you begin: Ensure that you have downloaded the required software packages from the Appliance Account for upgrading your Intersight Private Virtual Appliance. For more information on how to create the Private Appliance Account, see [Creating an Appliance Account](/help/appliance/getting_started/software_downloads/creating_an_appliance_account).

To configure a software update for Private Virtual Appliance, do the following:

  1. Log into Intersight Virtual Appliance as a user with account administrator role.

  2. Choose Settings > System > Appliance Updates.

The following details are displayed:

  * Running Version—The current software version number

  * Update Mode—Manual

You may see the following details about the Pending Update:

  * Version—Indicates the software version that is scheduled to be updated

  * Update Impact Type—This could be Disruptive, Disruptive-reboot, or None. The impact could be disruptive because of an infrastructure upgrade or upgrade of other Intersight services. A disruptive update may cause Intersight to be unavailable for the duration specified in Update Impact Duration. The disruptive reboot of the appliance could be caused by kernel updates and restarting of services. A grace period is provided to help you plan and manage the update better. The UI displays appropriate messages to guide you if there is a disruptive reboot.

Attention:

An appliance update could take about 90 minutes to complete.

During this time, some features will be temporarily unavailable.

It is recommended that you take a backup prior to triggering the update and do not reboot your appliance. If there is a requirement to reboot, Intersight Appliance does it automatically.

  * Installation Date/Time —Displays the date and time when the update is scheduled. You can click on the pencil icon to edit the installation date and time.

  * Release Notes—Link to the release notes for the pending software update

The Software screen also displays a table view of the appliance software updates under Update History. This table lists the installation date, appliance software Version, a description of the software version, and the status of the installation of the update. From this table view, you can search for a specific version of the software and the date it was installed on and the status of the installation.

  3. Click Install Updates

The Upload Software screen is displayed.

  4. Select either Local Machine or Network Share, depending on where you saved the software image.

     1. For Local Machine, browse to where you saved the software image, and then click Next.

     2. For the Network Share option, enter the protocol and enter the details of the remote server from where you want to copy the file.

  * Protocol—Communication protocol used for the file transfer. SCP (Secure Copy Protocol) and SFTP (Secure File Transfer Protocol) are supported.

  * Server IP/Hostname—The network share server from where the file is copied

  * Port—TCP port to use

  * Location—Directory where the file to be copied is stored

  * Filename—Name of the file to be copied from the network share

  * Username—Username for authenticating with the network share

  * Password—Password for authenticating with the network share

     3. Select to install immediately or to schedule the installation to a later date and time.

     4. Click Apply.

You can track the upload progress by clicking on the Requests icon.

When the upload completes, you will see details about the Pending Update on the Software screen. From the Pending Update Details section, you will be able to cancel an update, update immediately, or edit the installation date and time.

Note:

If you cancel a pending update, you will need to upload the appliance software again to be able to initiate an update.


Note:

If the update fails and if the update is recoverable, the Update History shows the installation as Failed, and the existing Pending Update Details remains as-is. You can try the upgrading process again. Contact Cisco TAC if you are unable to update successfully.

If the update fails and if the update is non-recoverable, the Update History shows the installation as Failed, and you will no longer see any existing Pending Update Details. However, all existing features and functionality continues to work as before. Contact Cisco TAC if you encounter an update failure.

After the update, if you use the same browser to log into the appliance, you might encounter an Error code: SEC_ERROR_REUSED_ISSUER_AND_SERIAL. To fix this issue, you will need to remove the system-generated certificate of the server from the same browser that you are using to log into the appliance. For example, to remove the system-generated certificate of the server from Google Chrome, navigate to Settings > Privacy and security > Manage certificate. Select the system-generated certificate that you want to remove, click Remove, and click Close. Close the browser, and then log into the application from a new browser. For more information about certificate, see [Add Certificates](/help/settings#add_certificate).

## Updating Intersight Intelligence for Intersight Private Virtual Appliance

Intersight Private Virtual Appliance allows you to update Intersight intelligence such as Hardware Compatibility List (HCL) and Advisories as soon as it becomes available, independent of the appliance software upgrade schedule.

Updates for HCL include the compatibility validation results and compliance status for server model, processor, firmware, adapters, operating system and drivers. For more information about HCL, see [Compliance with Hardware Compatibility List (HCL)](/help/appliance/resources#compliance_with_hardware_compatibility_list_\(hcl\)).

Intersight alerts users about the endpoint targets that are impacted by supported security advisories and field notices. These alerts are displayed as Advisories in Intersight. For a complete list of supported security advisories and field notices, and acknowledging advisories, see [Intersight Advisories](/help/appliance/resources#intersight_advisories).

To update Intersight intelligence for Private Virtual Appliance, do the following:

  1. Download the Intersight Intelligence software packages by following the instructions [here](/help/appliance/getting_started/software_downloads/downloading_software_packages_for_appliance).

  2. Log into Intersight Private Virtual Appliance as a user with account administrator role.

  3. Choose Settings > System > Appliance Updates.

  4. Click Install Updates.

The Upload Appliance Software screen displays.

  5. Select either Local Machine or Network Share, depending on where you saved the software image.

     1. For Local Machine, browse to where you saved the software image, and then click Next.

     2. For the Network Share option, enter the protocol and enter the details of the remote server from where you want to copy the file.

  * Protocol—Communication protocol used for the file transfer. SCP (Secure Copy Protocol) and SFTP (Secure File Transfer Protocol) are supported.

  * Server IP/Hostname—The network share server from where the file is copied

  * Port—TCP port to use

  * Location—Directory where the file to be copied is stored

  * Filename—Name of the file to be copied from the network share

  * Username—Username for authenticating with the network share

  * Password—Password for authenticating with the network share

     3. Select Install Now to install immediately or Install Later to schedule the installation to a later date and time.

     4. Click Apply.


You can track the upload progress by clicking on the Requests icon. Once the installation completes, you can view the status of the installation in the table under the Intelligence Update History tab by navigating to Settings > Software.

## Configuring Email Notifications for Intersight Virtual Appliance Software Updates

Intersight Virtual Appliance allows you to configure email notifications when a new software update or a new patch update becomes available for installation and when a new software update or a patch update is completed.

Note:

Ensure that you have configured SMTP settings before proceeding to configure email notifications for software updates. For information on how to configure SMTP settings, see [Configuring SMTP Settings for Email Notifications](/help/appliance/settings#configuring_smtp_settings_for_email_notifications).

  1. Log into Intersight Virtual Appliance as a user with an account administrator role.

  2. Choose Settings > System > Appliance Updates.

  3. Click Update Settings.

  4. Enable Email Notifications under Software Update Notifications.

  5. Choose when to send email notifications from the following options:

  * Updates Are Ready to Install

  * Updates Are Complete

  6. Enter up to 3 valid emails.

  7. Click Save.


Based on your selection for the notifications, emails are sent when an appliance software update or a patch update becomes available for installation and when a software update or a patch update is completed. To ensure that the configured users receive email notifications, and the emails do not end up in their Spam folder, it is recommended that the recipients add the sender's email address as per the SMTP configuration settings, to their "**approved senders** " list within their email client.

## Backing Up Data

Backing up of Intersight Virtual Appliance regularly is essential. Without regular backups, there is no automatic way to reconstruct the configuration settings, and recreating the profiles and policies. You can perform a backup once a day using a scheduled backup or create a backup on demand. Intersight Virtual Appliance enables you to take a full state backup of the data in the appliance and store it on a remote server. If there is a total site failure or other disaster recovery scenarios, the restore capability enables you to do a full state system restore from the backed-up system data.

Note:

An appliance installer is required to restore the appliance from a backup. If a backup is taken from appliance release version N, it can only be restored using the latest installer that is older than or equal to version N. For example:

  * If the backup of your appliance release version is 1.1.0-0, you need the latest appliance installer version that is older than or equal to 1.1.0-0, which is 1.1.0-0.

  * If the backup of your appliance release version is 1.1.1-1, you need the latest appliance installer version that is older than or equal to 1.1.1-1, which is 1.1.1-0.


Hence, it is recommended that you retain the appliance installer for the backup that you are creating. For more information, see [Recovering Intersight Connected Virtual Appliance](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide/m_setting_up_appliance.html#Cisco_Task_in_List_GUI.dita_e1993fc2-9060-4dac-be2f-da5b8480cdc7) and [Recovering Intersight Private Virtual Appliance](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide/m_setting_up_appliance.html#Cisco_Task_in_List_GUI.dita_5a821d1e-fe70-4d56-afb2-531b3261ba18).

You can select one of the following options for backing up data:

  * Create Backup—Creates a full state backup of the data on demand. You can save the backed-up data on a remote server. For detailed instructions, see the Creating Backup section.

  * Schedule Backup—Schedules a full state periodic backup of the data in the appliance, based on the schedule. You can save the backed-up data on a remote server. For detailed instructions, see the Scheduling Backup section.


Note:

There is no difference between a backup that is running on a multi-node appliance versus one that is running on a single-node appliance. The backup is done at the cluster level and not at the node level. The backup originates from one node, but there is no restriction on which node the backup originates from.

Note:

  * When you take a backup of the Intersight Virtual Appliance, the metrics collection data is not backed up. Take a snapshot of the metrics node VM to back up the metrics data.

  * When you capture a snapshot of the Intersight Virtual Appliance VM, note the following storage size specifications:

  * **Without Metrics Collection** : The snapshot size on disk is 180 GB.

  * **With Metrics Collection Enabled** : The snapshot size on disk exceeds 1 TB.

For more information, see the Resource Requirements section in [Cisco Intersight Virtual Appliance and Intersight Assist Getting Started Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide/m_appliance_overview.html#Cisco_Reference.dita_a6ea1ddc-e212-4367-9579-e9320b64f1b5).


## Creating a Backup

You can create a full state periodic backup of the Intersight Virtual Appliance, and save the backed-up file on a remote server.

To create a backup, do the following:

  1. Log into Intersight Virtual Appliance as a user with account administrator role.

  2. Choose Settings > System > Backups.

  3. Click Create Backup.

The Backup window displays.

  4. Enter the following details:

  * Protocol—Communication protocol option used in the backup process. Intersight Virtual Appliance currently supports CIFS (Common Internet File System), SCP (Secure Copy Protocol) and SFTP (Secure File Transfer Protocol) for backup. Enter the details of the remote server where you want to save the backed-up data.

  * Remote Port—Remote TCP port on the backup server (applicable only for SCP and SFTP).

  * Remote Host—The remote host for saving the backup files. Both Hostname and IP address are supported.

  * Remote Path—Directory where the backup files are saved.

Note:

CIFS share names must contain alpha-numeric characters only and must conform to the regular expression such as ^(\w+)(/\w+)*/?$. It cannot contain spaces. In addition, when specifying folders under the CIFS share, forward slash (/) must be used as a separator. For example, backupshare/Intersight/Daily and backupshare/Monthly.

Also, since the regular expression share names does not include a preceding forward slash, ensure that you enter the CIFs share name without an initial forward slash. For example, <share1/subdirectory1>.

  * Filename—Name of the backup file.

  * Username—Username for authenticating with the backup server.

  * Password—Password for authenticating with the backup server.

  * Password Confirmation—Reenter the password to complete validation.

  5. Click Start Backup.


## Scheduling Backup

Schedule Backup enables you to schedule a periodic weekly backup of the data in the Intersight Appliance.

  1. Log into Intersight Virtual Appliance as a user with account administrator role.

  2. Choose Settings > System > Backups.

  3. Click Schedule Backup.

The Schedule Backup window displays.

  4. On the Schedule Backup window, enable Use Backup Schedule.

If you disable this option, you must re-enable the Use Backup Schedule option to schedule a backup.

  5. Provide the following details to complete creating the Backup Schedule:

  * Backup Schedule

  * Day of Week—Specify the day of the week when you want to schedule a data backup or select Daily.

  * Time of Day—Specify the time on the selected day when you want to schedule a data backup. The Time of Day follows the browser time of your session and displays your local time of the day.

  * Backup Destination

  * Protocol—Communication protocol used in the backup process. Intersight Virtual Appliance currently supports CIFS (Common Internet File System), SCP (Secure Copy Protocol) and SFTP (Secure File Transfer Protocol) for backup.

  * Remote Port—Remote TCP port on the backup server (applicable only for SCP and SFTP).

  * Remote Host—The remote host for saving the backup files. Both Hostname and IP address are supported.

  * Remote Path—Directory location where the backup files are saved.

Note:

CIFS share names must contain alpha-numeric characters only and must conform to the regular expression such as ^(\w+)(/\w+)*/?$. It cannot contain spaces. In addition, when specifying folders under the CIFS share, forward slash (/) must be used as a separator. For example, backupshare/Intersight/Daily and backupshare/Monthly.

Also, since the regular expression share names does not include a preceding forward slash, ensure that you enter the CIFs share name without an initial forward slash. For example, <share1/subdirectory1>.

  * Filename—Name of the backup file

  * Username—Username for authenticating with the backup server.

  * Password—Password for authenticating with the backup server.

  * Password Confirmation—Reenter the password

  * Backup Retention—Number of backups to retain

Click Enable Backups Retention to enter the number of backups to retain on the remote server. The default number is 15. You can enter a number from 1 to 100.

Note:

In order for the backup retention limits to function properly while using the SCP protocol, ensure that the SFTP protocol is also enabled on your remote host.

For more information regarding the various backup retention scenarios, see [Backup Retention Scenarios](c_ia_backup_retention_scenarios.html).

  6. Click Schedule Backup to complete the process.


## Backup Retention Scenarios

The following table describes the various backup retention scenarios and the expected outcomes.

Table 1. Backup Retention ScenariosBackup Retention Scenarios| Expected Outcomes  
---|---  
You enable backup retention, allow backups to accrue, and then disable backup retention.| The backups taken under the retention policy will not be deleted.  
You enable backup retention, allow backups to accrue, and then disable backup retention. Now, you re-enable backup retention again.| The backups taken when retention was originally enabled will not be affected. Only backups taken after retention has been re-enabled will be part of the retention policy.  
You change the file path or hostname in the retention policy.| The backups taken before the change will not be affected. Only backups taken after the policy change will be part of the latest retention policy.  
You increase the number of backups| Backups will continue to accumulate as part of the retention policy until the maximum number of backups is reached and then the oldest backup will be deleted.  
You decrease the maximum number of backups from X to Y.| The older backups in the original retention policy will no longer be part of the policy. This means that the retention policy will be implemented only on the most recent backups for the number, Y. The backups before that will remain as-is.For example: Suppose you had a retention count of 5 and then you decrease the retention count to 3. In this case, the oldest 2 backups in the original retention policy will not be affected. Retention policy will be enabled only on the 3 backups.  
  
## Configuring Metrics Collection

Metrics collection within the Intersight Virtual Appliance is disabled by default. After you install or upgrade Intersight Virtual Appliance, to start metrics collection, you must enable metrics collection in the Intersight Virtual Appliance on the Settings > System > Metrics screen.

The **Metrics** screen provides an overview of system utilization and configuration options related to metrics collection. It displays the following information:

  * **Metrics Collection** –Indicates whether metrics collection is Enabled or Disabled, along with the date of the last status change.

  * **Collect Metrics for New Servers** –If automatically collects metrics for any new servers added to an IMM or UMM domain is enabled.

  * **Disk Usage** –Shows current disk utilization by metrics for the appliance.

  * **Metrics Processing Rate** –Displays the percentage of metrics processed against the available CPU and memory capacity of the virtual appliance. The value updates every 1-hour and reflects the metrics data ingestion rate.

Note:

The Metrics Processing Rate provides a visual indication of metrics data ingestion. A red critical banner appears when utilization (metrics processing rate or disk usage) reaches 90%. When utilization reaches this critical level, metrics collection is automatically disabled.

To resume collection, you must re-enable metrics collection after taking corrective actions—such as extending the disk capacity (for high disk usage) or unselecting servers (to reduce the processing rate below 90%).


After metrics collection is enabled for the Virtual Appliance, you can choose to enable or disable metrics collection on individual servers or all the servers in an IMM or UMM domains. You can select the **Collect metrics for new servers** checkbox to automatically enable metrics collection for any new servers added to the domain.

Note:

UMM devices collect only environmental metrics. For more information on metrics collection, see [Supported Metrics Overview](https://intersight.com/apidocs/introduction/supported-metrics-overview/).

To configure metrics collection, do the following:

  1. Log into Intersight Virtual Appliance as a user with the account administrator role.

  2. Choose Settings > System > Metrics.

  3. Click Configure.

  4. Toggle Enable Metrics to enable metrics collection.

Note:
  * Enabling metrics collection results in the immediate triggering of metrics gathering from the endpoints.

  * Disabling metrics collection may result in a delay of up to one hour before the configuration changes are complete and the collection of metrics stops.

  5. Select the Collect metrics for new servers checkbox to automatically enable metric collection for new servers added to the IMM or UMM domains.

  6. To enable metrics collection for all the servers of the IMM domain, select the corresponding checkbox.

  7. To select individual servers of a domain:

     1. Click the Edit icon, in the Domains column.

     2. In the Select Servers screen, select the desired servers.

     3. Click Save.


## Data Collected from Intersight Connected Virtual Appliance

Cisco Intersight Connected Virtual Appliance works in a connected mode and requires connectivity to hosted Intersight services. You must register the appliance with Intersight to manage your UCS or HyperFlex infrastructure.

If you enable the option to allow collecting additional information, Intersight may collect other details about the managed systems, beyond what is listed in the table Minimum Data Collected. When any of the options under Data Collection in the Security & Privacy screen of the appliance UI is enabled, Cisco reserves the right to collect more data for diagnosis and proactive troubleshooting purposes.

The tables below list the details of the minimum data collected by Intersight:

Table 2. Minimum Data CollectedComponent| Details of Data Collected  
---|---  
From Intersight Virtual Appliance| 

  * The appliance ID (Serial Number)
  * The IP address of the appliance
  * The hostname of the appliance
  * The device connector version and public key on the appliance

  
Appliance Software Auto-Upgrade| Version of software components or the services running on the appliance  
Appliance Health| 

  * CPU usage
  * Memory usage
  * Disk usage
  * Service statistics

  
Licensing| Server count  
Information about the endpoint target| 

  * Serial number and PID (to support Connected TAC)
  * UCS Domain ID
  * Platform Type

  
  
Table 3. Data Collected During One-time Device Connector UpgradeComponent| Details of Data Collected  
---|---  
From the endpoint target, only if the one-time device connector upgrade is used| 

  * The endpoint target type - Cisco UCS Fabric Interconnect, Integrated Management Controller, Cisco HyperFlex System
  * One or more firmware versions of the endpoint
  * The serial number of the endpoint target
  * The IP address of the endpoint target
  * The hostname of the endpoint target
  * The endpoint device connector version and the public key

  
  
For information about Proactive Support, see [Proactive Support enabled through Intersight](https://intersight.com/help/appliance/features/cisco_intersight/settings#proactive_support_enabled_through_intersight).

For detailed information about the Proactive Support workflow, supported faults, configuring the advanced options, setting tags, and caveats, see [Proactive RMA for Intersight Connected Devices](https://www.cisco.com/c/en/us/support/docs/servers-unified-computing/intersight/215172-proactive-rma-for-intersight-connected-d.html).

## Cloud Connection for Intersight Connected Virtual Appliance

Intersight Connected Virtual Appliance is connected to Cisco Intersight through an embedded device connector. The device connector provides a secure way for the connected targets to send information and receive control instructions from Cisco Intersight, using a secure Internet connection.

To view the details of the connection to the Cloud and also configure the settings from the Device Connector screen, do the following:

  1. Choose Settings > Networking > Cloud Connection. The Cloud Connection screen displays.

You can view details such as Device ID, Claim Code, Access Mode, and device connector status. For more information about configuring the device connector, status, and error conditions, see Configuring Device Connector in Resources.

  2. Click Settings and configure the following settings.

  * General—Enable Device Connector so that you can claim the appliance and leverage the capabilities of Cisco Intersight, and select an Access Mode. If the Device Connector option is disabled, no communication is allowed to Cisco Intersight. Click Save.

  * Proxy Configuration

  * Enable Enable Proxy. Add the Proxy Hostname or IP Address, and the Proxy Port. The proxy port must be in the range from 1 and 65535.

  * Enable Authentication and add a Username and Password for Authenticated Proxy. The proxy setting is automatically reset after restore, and you must manually reset the appliance proxy.

Click Save.

  * Certificate Manager—Import proxy certificates.

  * Connection—Check North America and EMEA connection details.


## Configuring DNS

This task provide details on how to configure DNS settings in the appliance.

Note:

Wildcard DNS sinkholing is not supported in Intersight Virtual Appliance.

  1. Log into Intersight Virtual Appliance as a user with account administrator role.

  2. Choose Settings > Networking > DNS. The details of the existing DNS settings display.

  3. Click Configure. The Configure DNS window displays.

  4. Update the following properties:

  * Preferred IPv4 DNS Server—Provide the IP address of the primary DNS server.

  * Alternate IPv4 DNS Server—Provide the IP address of the secondary DNS server.

  * Click Save.


## Configuring NTP

It is mandatory to have at least one Network Time Protocol (NTP) server configured in Cisco Intersight Virtual Appliance to enable synchronizing the time on the appliance with the NTP servers. The authentication schema for the NTP servers can be either unauthenticated or authenticated. You can add up to 4 unauthenticated NTP servers and 4 authenticated NTP servers during the initial setup of the appliance and edit them later, if necessary.

To configure a NTP server, do the following:

  1. Log into Intersight Virtual Appliance as a user with account administrator role.

  2. Choose Settings > Networking > NTP.

The details of the existing NTP settings displays.

  3. Click Configure.

The Configure NTP window displays.

  4. Click Add NTP Server, to add a new NTP server.

     1. Click \+ New Server.

     2. Enter a server hostname or an IP address for the Server Name and click Save to save the NTP server as an unauthenticated one.

     3. Enable the Enable NTP Authentication button to add the NTP server as an authenticated one.

Enter the following information.

  * Server Name—Server hostname or IP address

  * Symmetric Key Type—Type of symmetric key to use for this server

  * Symmetric Key ID—Positive integer that identifies a cryptographic key used to authenticate NTP messages

  * Symmetric Key Value—Value of the symmetric key

     4. Click Save.


To edit existing NTP server configurations, click + on any of the configured NTP servers, make your edits as needed, and save the edited configurations.

## Configuring Syslog

Intersight Virtual Appliance provides you the ability to configure up to five syslog servers. When you enable syslog server in Intersight Virtual Appliance, you can export the following types of logs and alarms based on the details provided when configuring the syslog server.

  * Web Server Access Logs—Web server access logs for all transactions involving user session activities.

  * Audit Logs—Audit logs for events such as login, logout, created, modified, and deleted, that are displayed in the Audit Logs screen in Intersight Virtual Appliance.

  * Alarms —All Intersight alarms including appliance alarms that provide alerts about a failure (fault) in the managed target or when a threshold has been crossed. For information about alarms in Intersight, see [Alarms](/help/appliance/my_dashboard/dashboard_management#alarms). For more information about alarms in Intersight Virtual Appliance, see the Alarms in Intersight Virtual Appliance table in [Appliance Monitoring](/help/appliance/settings#appliance_monitoring).


Attention:

  * In Intersight Virtual Appliance, you can use the TLS, UDP, and TCP protocols to provide secure communication to the syslog server. However, it is strongly recommended that you use **only** TLS in your production environment.

  * UCS C-Series server-related faults such as power supply and fan failures are not forwarded by Intersight Virtual Appliance to a syslog server. Please configure the syslog server on the UCS C-Series CIMC side to handle forwarding of the UCS C-Series events and faults.


**Before you begin:** Ensure that you have added the certificate for the syslog server where you want to send the web server log, audit logs, and alarms in Intersight Virtual Appliance. This certificate is used to verify TLS communication with the syslog server. For more information about how to add certificates, see [Add Certificates](/help/settings#add_certificate).

Attention:

  * If you plan on using FQDN in the Hostname/IP Address field while configuring the syslog server, set up the certificate for the syslog server with a proper FQDN entry in the Common Name or the DNS entry in the Subject Alternative Names. Enter this information in the Hostname/IP Address field while configuring the syslog server.

  * If you plan on using either IPv4 or IPv6 address in the Hostname/IP Address field while configuring the syslog server, set up the certificate for the syslog server with the IP address in the Common Name. Enter this information in the Hostname/IP Address field while configuring the syslog server.


To configure a syslog server in Intersight Virtual Appliance, do the following:

  1. Log into Intersight Virtual Appliance as a user with account administrator role.

  2. Choose Settings > Networking > Syslog.

You can view the details of the existing syslog server settings.

  3. Click Add Syslog Server.

The Add Syslog Server window displays.

  4. Update the following fields as needed.

  * Enable Syslog Server—When enabled, the Web Server Access Logs, Audit Logs, and Alarms are sent to the configured syslog server as per the configuration details provided in the Hostname/IP Address, Port, Protocol, and Minimum Severity of Alarms to Report fields. Note that the Minimum Severity of Alarms to Report field is applicable only for Alarms.

  * Web Server Access Logs—When enabled, you will be able to export the web server access logs for all transactions involving user session activities.

Note:

It is highly recommended that you do not enable this option as it will quickly overpopulate your log files. This option is mainly made available for customers that require the ability to export web server access logs.

  * Audit Logs—When enabled, the audit logs for events such as login, logout, created, modified, and deleted, that are displayed on the Audit Logs screen are sent to the configured syslog server.

  * Alarms—When enabled, the Intersight alarms including appliance alarms that provide alerts about a failure (fault) in the managed target or when a threshold has been crossed are sent to the configured syslog server.

  * Hostname/IP Address—Enter either FQDN, an IPv4 address, or an IPv6 address. This information must match the details that you provided in the certificate for the syslog server.

  * Port—Port to use for the syslog server

  * Protocol—Select a protocol from the drop-down list. It is strongly recommended that you use **only** TLS in your production environment.

  * Minimum Severity of Alarms to Report (Applicable for Alarms Only) —Select either Info, Critical, or Warning as the minimum severity level for alarms to get reported. When the alarms of selected severity and above are cleared at the endpoints, the notification for the same also gets exported to the syslog server.

  5. Click Add.


## Understanding Syslog Messages

As an Account Administrator, you can configure a syslog server for an Intersight Appliance to receive syslog messages for the following:

  * Web Server Access logs

  * Audit logs

  * Alarm logs


To configure the syslog server:

  1. Log in as an Account Administrator.

  2. Choose Settings > Networking Syslog.

  3. Configure the syslog server to include WebServer Access logs, Audit logs and/or Alarm logs.


You may export these logs as a CSV file.

**Syslog Message Format**

![](file:/Users/roopraja/Documents/SysLogImages/481397.jpg)

**Header Description**

Table 4. Header DescriptionField| Description  
---|---  
Timestamp| The date and time at the source when the syslog message is created. The format varies based on the configuration defined in the syslog server.For example: `Aug 24 19:11:58`  
Hostname| The hostname of the Intersight Appliance that sent the syslog message.For example: `example01.intersight.vapp`  
Tag| Determines the type of the syslog message.Possible values are:

  * Intersight-OnPrem [Web Server]: For the Web Server Access logs.
  * Intersight-OnPrem [Admin Shell]: For the Intersight Appliance Admin Shell Audit logs.
  * Intersight-OnPrem: For Audit and Alarm logs.

  
  
**Payload Description**

The Payload section contains the body of the syslog message. The format of the Payload section varies for each event type. The Tag field in the Header determines the type of the syslog message.

The following sections contain examples of syslog messages along with the description for the Payload for each event type.

**Sample Syslog Message from Web Server Access Logs**

**Format:**

`<Header:> $remote_addr ($http_user_agent) [$time_local] $ssl_protocol $ssl_cipher $request_method $scheme://$host$request_uri`

**Sample message:**

`Aug 24 20:42:38 example01.intersight.vapp Intersight-OnPrem [WebServer]: ----10.155.160.177 (Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36) [24/Aug/2023:20:42:38 +0000] TLSv1.3 TLS_AES_256_GCM_SHA384 GET https://example01.intersight.vapp.domain.com/`

Where, _Aug 24 20:42:38 example01.intersight.vapp Intersight- OnPrem [WebServer]_ is the Header. For more information, see the **Header Description** section.

The following table describes the fields used in the Payload of Web Server Access logs.

Field| Description  
---|---  
`$remote_addr`| The client address.  
`$http_user_agent`| Information about the client browser used to access Intersight.  
`$time_local`| The local time in the Common Log Format.  
`$ssl_protocol`| The protocol of an established SSL connection.  
`$ssl_cipher`| The name of the cipher used for the SSL connection.  
`$request_method`| The request method used. For example, GET or POST.  
`$scheme`| The request scheme used. For example, `http` or `https`.  
`$host`| The name of the host.  
`$request_uri`| The Full Original Request URI, with arguments.  
  
**Sample Syslog Message from Audit Logs**

Syslog messages for Audit Logs are generated as a result of one of the following operations:

  * User operations in Intersight Appliance, such as creating a policy, creating a profile, or claiming a target.

  * Admin user operations on the Intersight Appliance Maintenance Shell.

  * Internal system activity, such as Admin login, system reboot, or shutdown.


**Example 1:**

The following example describes an Audit log message generated due to a user operation in Intersight Appliance.

**Format:** `<Timestamp> <Hostname> <Process_name>[PID]: <Intersight_timestamp> Object Type: <object type> Object: <Object_ID> Event: <Event_type> Request: <inputs> User ID:<username> Client IP: <IP_address> Session ID: <Session_ID>`

**Sample message:**

`Aug 24 19:11:58 example01.intersight.vapp Intersight-OnPrem: Aug 24 19:11:58 example01.intersight.vapp Intersight[13235]: 2023-08-24 19:11:48.697 +0000 UTC Object Type: power.Policy Object: 64e7ab74627572301ec09bbd Event: Created Request: {"AllocatedBudget":0,"DynamicRebalancing":"Enabled","ExtendedPowerCapacity":"Enabled","Name":"port-policy1", "Organization":{"Moid":"64e4fa50697265301ec8a7a6","ObjectType": "organization.Organization"},"PowerPriority":"Low","PowerProfiling":"Enabled","PowerRestoreState":"AlwaysOff","PowerSaveMode":"Enabled","RedundancyMode":"Grid","Tags":[]} User ID: admin@local Client IP: 10.157.130.72 Session ID: 64e7a453756461301e172f1b`

Where, _Aug 24 19:11:58 example01.intersight.vapp Intersight-OnPrem_ is the Header. For more information, see the **Header Description** section.

The following table describes the fields used in the Payload of an Audit log message generated due to a user operation in Intersight Appliance:

Field| Description  
---|---  
Timestamp| The date and time at which the syslog message is generated at source. It is the data and time of the event collected by the syslog client running in the Intersight Appliance.  
Hostname| The name of the appliance that sent the syslog message.  
Process_name| Indicates that the syslog message is collected by Intersight.  
PID| The process ID that collected the message from Intersight.  
Intersight_timestamp| The date and time at which the operation was performed in the Intersight Appliance.  
Object Type| The managed object type on which the operation is performed. It is an Intersight object type.  
Object| The unique identifier of the Intersight object on which the create, update, or delete operation is performed. The `Object` and `Object Type` fields together can be used to query the managed object through the Intersight API.  
Event| The type of event performed by the user.Possible values are:

  * Login—When a user logs in to Intersight.
  * Logout—When a user logs out from Intersight.
  * Created—When an object is created in Intersight.
  * Modified—When an existing object is updated in Intersight.
  * Deleted—When an object is deleted in Intersight.

  
Request| [Optional] Input arguments used while creating or modifying the object.Note: This field is unavailable for the Deleted event type.  
User ID| [Optional] The name or email ID of the user who initiated the change.Note: This field is unavailable if the change is initiated by the system.  
Client IP| [Optional] The IP address of the machine from which the request or change is initiated.Note: This field is unavailable if the change is initiated by the system.  
Session ID| [Optional] The unique ID of the Intersight UI session on which the change is requested.Note: This field is unavailable if the change is initiated by the system.  
  
**Example 2:**

The following example describes an Audit log generated due to a Admin user operation on the Intersight Appliance Maintenance Shell.

**Format:**

<Timestamp> <Log_level> [Process:PID] <Command>

**Sample**
    
    
    Aug 24 19:28:39 example01.intersight.vapp Intersight-OnPrem
    [Admin Shell]: 2023-08-24 19:28:39,644 INFO [diag.py:1673]
    RUN_PING
    

Where, _Aug 24 19:28:39 example01.intersight.vapp Intersight-OnPrem [Admin Shell]_ is the Header. For more information, see the **Header Description** section.

The following table describes the fields used in the Payload of an Audit log generated due to a user operation on Intersight Appliance Maintenance Shell.

Field| Description  
---|---  
Timestamp| The date and time when the action is performed.  
Log_level| The severity of the log.The default value is INFO.  
Process| The name of the process that handles the Maintenance Shell operation.The default value is `diag.py`.  
PID| The process ID which created the event.  
Command| The type of operation performed in Intersight Appliance Maintenance Shell.For example:

  * RUN_PING
  * RUN_CONNECTIVITY_TEST

  
  
**Example 3:**

The following example describes the Audit Log generated by Intersight Appliance.

**Format:**

`<Timestamp> <Hostname> <Process>: <Description>`

**Sample message:**
    
    
    Aug 25 00:30:11 example01.intersight.vapp Intersight-OnPrem: Aug
    25 00:30:11 example01.intersight.vapp systemd-logind: New
    session 5468 of user admin.

Where, _Aug 25 00:30:11 example01.intersight.vapp Intersight-OnPrem_ is the Header. For more information, see the **Header Description** section.

The following table describes the fields used in the Payload of an Audit log generated by Intersight Appliance.

Field| Description  
---|---  
Timestamp| The date and time when the event occurred.  
Hostname| The hostname of the Intersight Appliance on which the event occurred.  
Process| The process which created the syslog event.  
Description| The unique ID of the process which created the event.  
  
**Sample Syslog Message from Alarms Logs**
    
    
    <Header>: <Timestamp> <Hostname> <Process_name>[PID]: 
    <Intersight_timestamp> Severity:<Severity type> Affected Object:<Object_name> 
    Description:<Description>

**Sample message:**
    
    
    Aug 24 18:26:36 example01.intersight.vapp Intersight-OnPrem: Aug
    24 18:26:36 example01.intersight.vapp Intersight[64799]: 2023-
    08-24 18:26:22.298 +0000 UTC Severity: Critical Affected Object:
    64e2f9cd6f7261301e04b24b/sys/chassis-1/fan-module-1-7/fan-
    1/fault-F0373 Description: Fan 1 in Fan Module 1-7 under chassis
    1 operability: inoperable

Where, _Aug 24 18:26:36 example01.intersight.vapp Intersight-OnPrem_ is the Header. For more information, see the **Header Description** section.

The following table describes the fields used in the Payload of an Alarms log.

Field| Description  
---|---  
Timestamp| The date and time at the source when the syslog message is generated. It is the date and time of the event collected by the syslog client running in the Intersight Appliance.  
Hostname| The name of the appliance which sends the syslog message.  
Process_name| Indicates that the syslog message is collected by Intersight.  
PID| The process ID that collected message from Intersight.  
Intersight_timestamp| The date and time at which the respective action is performed by the user or the system. In case of an alarm, it is the date and time at which the alarm is created or updated by the Intersight.  
Severity type| The severity level of the alarm. The possible values are Critical, Warning, or Info.  
Object_name| The name of the object on which the alarm is created.  
Description| A short description about the alarm message.  
  
## Configuring SMTP Settings for Email Notifications

Networking systems and software frequently create alarms that indicate a concerning event or a trend has been detected. Email notifications automatically poll for recent alarms, determine their severity, and direct concerning ones to a user's email address based on a rule you create.

To configure email notifications in Intersight Virtual Appliance, perform the following two tasks:

  * Configure Simple Mail Transfer Protocol (SMTP) settings

  * Create notification rules


**Configuring SMTP settings**

This task provide details on how to configure SMTP settings.

  1. Log into Intersight Virtual Appliance as a user with account administrator role.

  2. Choose Settings > Networking > SMTP.

You can view the details of the existing SMTP settings. If this session is your first instance of configuring SMTP for email notifications, the appliance displays default or no values in the fields.

  3. Click Configure.

  4. Enable the SMTP toggle button to configure email notifications.

  5. In the SMTP Server Address field, type the IP address or domain name of the server in your domain that sends email notifications.

  6. In the SMTP Port list, type or select the port number of the server that performs the email notification forwarding.

Port 25 is the standard SMTP Relay port. Ports 465 or 587 are secure mail routing ports. The value range for port selection is 1 through 65535, and the default is 25.

  7. In the SMTP Sender Name field, type the email address of the user that sends email notifications.

  8. (Optional) Enable the TLS toggle button.

TLS is a form of authorization that provides security by verifying the certificate authority (CA) of the SMTP email server. To apply TLS security, select the CA you want to apply from the list in the TLS region.

  9. (Optional) Enable the Authentication toggle button, if your SMTP server requires authentication, and provide the username and password used to authenticate to the SMTP server.

  10. Click Configure.


Once the configuration completes, you can verify the SMTP settings by sending a test email.

  1. Click Test on the SMTP configuration screen.

  2. Add a valid email address in the Test pop-up screen for sending a test email.

  3. Click Send.


The result of trying to send a test email is displayed on the screen. If it is successful, you can confirm that you received the test email with the subject Cisco Intersight SMTP Configuration Test Email at the specified email address.

Note:

The Test button is enabled only after the SMTP settings are configured. Also, emails are sent only for successful validations.

Next, complete the steps for creating notification rules.

**Email Notifications List View**

When you select **Settings > Email Notifications** in the Intersight UI, the **Email Notifications** list view appears.

The list view shows each notification rule in a tabular format. The table includes the following key details:

  * **Name** —The name of the rule.

  * **Status** —The administrative state of the rule. A setting of **Enabled** indicates the rule is active and will generate email notifications when the rule conditions are met. A setting of **Disabled** indicates the rule is inactive and will not generate email notifications.

  * **Notify About** —Displays whether the notification rule configured to send notifications for Advisories, Alarms, or both, based on its configuration.

When you click the eye icon next to Notify About, a details panel shows the specific criteria configured for that notification rule.

For Advisories, it lists the advisory types and filters, such as security advisory severity, field notice impact rating, and EOL advisory milestone types (for example, _End of Life Announcement_ or _Last Date of Support_). For Alarms, it shows the alarm severity, whether cleared alarms are included, the configured conditions (for example, _UCS Domain = US-East_), and the condition operator (such as _All_).

  * **Email** —The email address(es) to which notifications will be sent.

  * **Created On** —The date and time when the rule was created.

  * **Last Updated** —The last time the notification rule was updated.


**Email Notifications Actions**

On the **Email Notifications** page, click the **ellipsis (…)** icon next to an email notification rule to:

  * **Edit** —Modify the email notification rule.

  * **Enable/Disable** —Turn the email notification rule on or off.

  * **Delete** —Remove the email notification rule.


You can also click the **information (eye) icon** in the Notify About column for a rule to:

  * **View Details** —Display a read-only summary of the advisory and alarm configuration for that rule, including advisory types, severities or impact ratings, EOL milestone selections, alarm severities, and filter conditions.


**Create a Notification Rule**

Notification rules in Cisco Intersight let you receive email notifications for important **advisories** and **alarms** affecting your environment. You can create rules that notify only for advisories, only for alarms, or for both in a single rule. Intersight sends notification emails when new Cisco advisories matching your selections are published, or when existing advisories begin to impact additional devices in your account. This ensures you're proactively notified of both newly identified risks and expanding impacts. Alarm notifications are based on alarm severity and detailed filter conditions you configure.

**Notification Rules for Advisories**

Use advisory notification rules to receive proactive email alerts when new advisories that match your criteria affect devices in your Intersight account. Advisories include security advisories (PSIRTs), field notices, and end-of-life (EOL) announcements.

Advisory emails are **aggregated over a 30-minute processing window** , so multiple new advisory instances are combined into a single email instead of sending one email per advisory. Each advisory email typically includes the advisory name, advisory ID, advisory type (security advisory, field notice, or EOL), severity/impact rating, the count of affected devices, and a link to view the advisory details in Intersight.

**Notification Rules for Alarms**

Use alarm notification rules to receive email alerts for alarms that match specific severity levels and **filter conditions**. You can use alarm-only rules, or combine alarm and advisory notifications in a single rule.

Alarm notifications are based on rules you configure for incoming alarms, allowing you to define filter conditions so that email alerts are sent only when certain criteria are met—ensuring the right individuals or teams are notified.

Filter conditions consist of three components:

  * **Filter Option** – The field to filter, such as _Host Type_ or _Organization_.

  * **Operator** – The logical condition, such as _Equals_ or _Not Equals_.

  * **Value** – The specific criteria, such as _Blade Server_ , _Rack Server_ , or _Chassis_.


For example, with:

  * Filter Option: **Host Type**

  * Operator: **Equals**

  * Value: **Blade Server**


This configuration ensures that email notifications are triggered only for alarms related to blade servers.

To configure a notification rule, perform the following steps:

  1. Log into Intersight as a user with an **Account Administrator** role.

  2. Navigate to **Settings > Email Notifications**.

You can view the details of the existing email notifications.

  3. Click **Create Notification** in the upper-right portion of the screen.

The Create Notification screen displays.

  4. In the **Name** field, type a string to identify the rule.

  5. In the **Description** field, optionally type a brief description for the rule.

  6. In the **Email** field, use the drop-down menu to select the email address(es) to which advisory notification emails will be sent.

     1. If the required email address is not available in the list, type the email address into the drop-down field and click **+Add**.

     2. You can add up to three email addresses for email notifications.

Note: Email notifications generated by the system can contain sensitive information such as advisory type, severity/impact rating, source type, source name, and affected device counts. Ensure that only authorized individuals have access to these notifications.

  7. Click **Next**.

  8. To enable email notifications for Advisories, toggle the **Enable** button.

  9. Select one or more Security Advisories levels for which you want to receive notifications:

  * **Critical** : (CVSS score above 9.0) Indicates vulnerabilities that can lead to severe impact and typically require immediate remediation.

  * **High** : (CVSS score 7.0-8.9) Indicates vulnerabilities that may cause significant impact but are generally more difficult to exploit than Critical issues.

  * **Medium** : (CVSS score 4.0-6.9) Indicates vulnerabilities that may affect specific functions or configurations and are exploitable in more limited scenarios.

  * **Info** : (CVSS score below 4.0) Indicates vulnerabilities with low impact and limited effect on system functionality.

For more information, see [Security Vulnerability Policy.](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html)

  10. Select one or more Field Notice impact ratings for which you want to receive notifications:

  * **Critical** – May cause service downtime or significant risk to operations; requires urgent action.

  * **High** – May cause noticeable performance degradation or operational impact, depending on deployment; requires timely attention.

  * **Medium** – May affect performance or behavior but is less likely to cause immediate operational risk; can be addressed as part of planned maintenance.

  * **Low** – Unlikely to affect normal operation; minor issues that can be handled at your convenience.

For more information, see [Field Notice Rating Guide](https://www.cisco.com/c/en/us/support/web/field-notice-rating.html).

  11. Select one or more End-of-Life (EOL) advisory milestone types for which you want to receive notifications:

  * **End of Life Announcement** – Date Cisco publishes the formal end-of-sale and end-of-life notice for the product.

  * **End** **of Software Maintenance** – Last date on which Cisco Engineering may provide software maintenance releases or bug fixes; after this date, only critical security updates may be provided.

  * **Last Date of Support** – Final date on which service and support are available; after this date, the product is no longer supported and is considered obsolete.

For more information, see [Cisco EOL Policy](https://www.cisco.com/c/en/us/products/eos-eol-policy.html).

Intersight sends advisory emails only when new advisory instances matching these selections are created for devices in your account. Advisories that do not impact your inventory, or that have already been acknowledged do not generate emails.

  12. To enable email notifications for Alarms, toggle the **Enable** button.

  13. Select the severity level of the alarm that should trigger a notification email. The available severity levels are Critical (the most urgent), Warning (second-least urgent), or Info (no urgency). You can select one or multiple severity levels. If multiple severity levels are selected, the least severity level among them will trigger the notification email when it is reached.

For more information on severity levels, see the Alarms in Intersight section in [Cisco Intersight Alarms Reference Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/IMM_Alarms_Guide/b_cisco_intersight_alarms_reference_guide/m_intro_intersight_alarms_guide.html).

  14. To receive notifications when alarms are resolved and marked as cleared, toggle the Include Cleared Alarms option to on. Notifications for the cleared alarms correspond to the severity level that you have selected for the active alarms.

  15. (Optional) Use the Add Filter field to select a filter option from the available built-in options. The filter option can be one of the following: Affected Name, Affected Type, Code, Organization, Parent Name, Parent Type, Profile Name, and UCS Domain.

  16. After selecting a filter option, specify the operator to define the logical condition for the filter. The available operators are:

  * **Equals (=):** Matches entries where the value in the selected field exactly matches the specified value. This comparison is case-sensitive. Example: _Host Type = Blade_

  * **Not Equals (!=):** Excludes entries where the value in the selected field matches the specified value. Example: _Host Name != TestServer_

  * **Contains (:):** Matches entries where the specified value appears as part of the field. This comparison is case-insensitive. Example: _Domain : prod_

  * **In:** Matches entries where the field value is one of multiple specified values. Example: _Host Type In Blade Server, Rack Server_

  17. Enter the value for the filter condition. The value must correspond to the selected filter option and operator. Example: If the filter option is Host Type and the operator is Equals (=), the value could be Blade Server.

  18. Repeat these steps to specify additional conditions.

Note: You can specify a total of five filter conditions.

For example, a complete configuration for alarm email notifications could be:

     1. Set the filter option to Host Type, with the operator as Equals and the value as Blade Server.

     2. Additionally, configure another filter with the option Organization, the operator as Contains, and the value as Engineering.

This configuration ensures that email notifications are sent only for alarms related to Blade Servers in the Engineering organization.

  19. If you specify multiple filters, use the Notifications will be sent when field to choose whether email notifications should be sent when Any condition is met or only when All conditions are satisfied.

  20. Click **Next**.

  21. Review the Summary step and click **Create**.

Intersight returns to the Notifications screen displaying the new rule in the list.


**Example API Configuration:**

This section explains how to set up email notification rules using the Intersight APIs. The example below, named 'AdvancedApiFilter', configures an email notification to be sent to [__abc@example.com_ _](mailto:abc@example.com)for alarms or advisories that meet specific criteria defined by the Conditions property. The Conditions property specifies the circumstances under which an email notification is triggered.

An email notification rule can contain multiple condition objects within its Conditions array. When multiple conditions are present, they are treated with an 'OR' logic across different MoTypes (Managed Object Types). This means if _any_ of the specified conditions (for example, an alarm condition OR an advisory condition) are met, the notification action is triggered.

To set up an email notification subscription named "AdvancedApiFilter" with custom rules, use the following POST request:
    
    
    POST /api/v1/notification/AccountSubscriptions
    
    
    { 
    
      "Name": "AdvancedApiFilter", 
    
      "Description": "User-defined email notification for alarms and advisories", 
    
      "Enabled": true, 
    
      "Type": "email", 
    
      "ObjectType": "notification.AccountSubscription", 
    
      "ClassId": "notification.AccountSubscription", 
    
      "Actions": [ 
    
        { 
    
          "ObjectType": "notification.SendEmail", 
    
          "ClassId": "notification.SendEmail", 
    
          "Email": "abc@example.com" 
    
        } 
    
      ], 
    
      "ConditionOperator": "All", 
    
      "Conditions": [ 
    
        // Conditions will be defined here 
    
      ] 
    
    }

The Conditions array allows you to define various criteria for triggering notifications. Different ObjectType values within the Conditions array cater to specific filtering needs.

**1\. Advisory Conditions (notification.AdvisoryMoCondition)**

This condition type is used to filter for security advisories, field notices, and end-of-life advisories. It is important to note that notification.AdvisoryMoCondition is _only_ applicable when the associated action is notification.SendEmail.

**Example Condition for Advisories:**
    
    
    { 
    
      "Enabled": true, 
    
      "ObjectType": "notification.AdvisoryMoCondition", 
    
      "advisoryFilters": [ 
    
        { 
    
          "ObjectType": "notification.SecurityAdvisoryFilter", 
    
          "severity": [ 
    
            "critical", 
    
            "high", 
    
            "medium", 
    
            "info" 
    
          ] 
    
        }, 
    
        { 
    
          "ObjectType": "notification.FieldNoticeAdvisoryFilter", 
    
          "severity": [ 
    
            "critical", 
    
            "high", 
    
            "medium", 
    
            "low" 
    
          ] 
    
        }, 
    
        { 
    
          "ObjectType": "notification.EolAdvisoryFilter", 
    
          "milestoneType": [ 
    
            "endOfSoftwareMaintenanceDate", 
    
            "lastDateOfSupport", 
    
            "endOfLifeAnnouncementDate" 
    
          ] 
    
        } 
    
      ] 
    
    }

**2\. Alarm Conditions**

Alarm conditions can be defined in two ways:

  * **Basic Alarm Filtering (notification.AlarmMoCondition):** This condition allows filtering alarms based on their severity levels.

  * **Advanced Alarm Filtering by Property (notification.SimpleMoCondition):** This condition allows for more granular filtering of alarms based on specific properties and their values, such as the Domain of an alarm.


**Example Conditions for Alarms (combined):**
    
    
    [ 
    
      { 
    
        "Enabled": true, 
    
        "ObjectType": "notification.AlarmMoCondition", 
    
        "OdataFilter": "", 
    
        "Severity": [ 
    
          "Critical", 
    
          "Warning", 
    
          "Info" 
    
        ] 
    
      }, 
    
      { 
    
        "Enabled": true, 
    
        "ObjectType": "notification.SimpleMoCondition", 
    
        "MoType": "cond.Alarm", 
    
        "Filter": { 
    
          "Operator": "eq", 
    
          "Property": "Domain", 
    
          "Value": [ 
    
            "dcemulator-6d6cb35277cd00fc" 
    
          ] 
    
        } 
    
      } 
    
    ]

**3\. Advanced Conditions (notification.MoCondition)**

For highly flexible and complex filtering, the notification.MoCondition allows you to specify criteria using OData syntax.

Note: If notification.MoCondition is used, _no other conditions can be specified_ for that AccountSubscription Managed Object (Mo). It acts as a standalone, comprehensive filter.

**Example Condition for Advanced Filtering:**
    
    
    { 
    
      "Enabled": true, 
    
      "ObjectType": "notification.MoCondition", 
    
      "MoType": "cond.Alarm", 
    
      "OdataFilter": "(Severity eq 'medium')" 
    
    }

**Complete API Example with Multiple Conditions**

Here is a full example demonstrating how to combine different condition types within a single _AccountSubscription_ to trigger email notifications:
    
    
    { 
    
      "Enabled": true, 
    
      "Name": "adv", 
    
      "Actions": [ 
    
        { 
    
          "ObjectType": "notification.SendEmail", 
    
          "ClassId": "notification.SendEmail", 
    
          "Email": "nagsivak@cisco.com" 
    
        } 
    
      ], 
    
      "ConditionOperator": "All", 
    
      "Conditions": [ 
    
        { 
    
          "Enabled": true, 
    
          "ObjectType": "notification.AlarmMoCondition", 
    
          "OdataFilter": "", 
    
          "Severity": [ 
    
            "Critical" 
    
          ] 
    
        }, 
    
        { 
    
          "Enabled": true, 
    
          "ObjectType": "notification.SimpleMoCondition", 
    
          "MoType": "cond.Alarm", 
    
          "Filter": { 
    
            "Operator": "eq", 
    
            "Property": "Domain", 
    
            "Value": [ 
    
              "dcemulator-6d6cb35277cd00fc" 
    
            ] 
    
          } 
    
        }, 
    
        { 
    
          "Enabled": true, 
    
          "ObjectType": "notification.AdvisoryMoCondition", 
    
          "advisoryFilters": [ 
    
            { 
    
              "ObjectType": "notification.SecurityAdvisoryFilter", 
    
              "severity": [ 
    
                "critical", 
    
                "high", 
    
                "medium", 
    
                "info" 
    
              ] 
    
            }, 
    
            { 
    
              "ObjectType": "notification.FieldNoticeAdvisoryFilter", 
    
              "severity": [ 
    
                "critical", 
    
                "high", 
    
                "medium", 
    
                "low" 
    
              ] 
    
            } 
    
          ] 
    
        } 
    
      ] 
    
    }

  * An Alarm with "Critical" severity is raised AND the ‘Domain’ is equal to "dcemulator-6d6cb35277cd00fc". **OR**

  * A new advisory (Security Advisory or Field Notice) affects the customer environment and matches the specified severity filters.


**Limitations**

Note the following restrictions for configuring email notifications.

  * You can configure up to three emails per rule.

  * You can configure up to five rules per account.

  * You can specify a total of five filter conditions.

  * Events are collected in a sliding time window of 10 seconds. Intersight initially waits a 10-second period where it polls for alarms. If an alarm or multiple alarms are detected in this initial period, Intersight waits an additional 10-second period to detect alarms. If it detects alarms in this period, additional periods occur until no alarms are detected. Once an additional 10-second period elapses with no alarms detected, Intersight bundles the discovered alarms into an alarm group and sends an email containing the alarms to the specified address.

  * An email address can be associated with up to 100 alarms and the number of emails sent depends on how large the alarm group is. If an alarm group contains more than 100 alarms, then an additional email is sent. Some events may generate 1,000 alarms. In that case, 10 emails are sent.


## Single Sign-On (SSO)

Single sign-on (SSO) authentication enables you to use a single set of credentials to log into multiple applications. With SSO authentication, you can log into the Intersight Virtual Appliance with your corporate credentials. Intersight Virtual Appliance supports SSO through SAML 2.0, and acts as a Service Provider (SP), and enables integration with Identity Providers (IdPs) for SSO authentication.

To set up SSO through the appliance, you must log into Intersight Virtual Appliance as a user with administrator role, download the SP metadata, and register your Identity Provider (IdP) in Intersight Virtual Appliance.

IdP Requirements

The IdP you add to Intersight must support SAML 2.0 and a service provider initiated SSO. The most commonly used IdPs have different instructions to complete the setup.

Note:

If you have a multi-node cluster setup for Intersight Virtual Appliance or if you are expanding from a single-node configuration to a multi-node cluster configuration, for some IdPs such as Okta you must manually configure the three SSOs, while for other IdPs such as ADFS you can directly import the xml file. For IdPs where the SSO configuration is a manual one, you must configure the three different SSO URLs specified in the metadata file downloaded from the appliance SSO screen. Once the three URLs are configured, you can proceed with the SSO login from any one of the three nodes.

Additional requirements for a multi-node cluster setup in appliance:

  * SLO (Single Logout) is supported for a multi-node setup in appliance, but there is only one SLO endpoint. If the node specified in the SLO URL is down, then SLO will not work. In this case, you will only be logged out of Intersight.

  * The IDP initiated SSO works only for the entity node.


For more information about setting up SSO with Intersight and examples of adding an Identity Provider, see, [Single Sign On with Intersight](https://intersight.com/help/appliance/resources#single_sign-on_with_intersight). Click [here](https://intersight.com/help/appliance/video#intersight_single_sign-on) to watch a video that shows how to enable Intersight Single Sign-On and set up a custom SAML 2.0 application in an external Identity Provider (IdP) with Intersight.

## Certificates

To provide secure authentication to external targets (such as LDAP servers), you can add a third-party certificate from a trusted source that affirms the identity of your targets or add a self-signed certificate for secure HTTPS access of the appliance through the browser.

Note:

  * In a future release, Intersight Virtual Appliance will be phasing out support for certificates signed with the SHA-1 hash functions. It is strongly recommended that you upgrade your certificates to use signature algorithms with hash functions that are stronger than SHA-1, such as SHA-256, SHA-384, or SHA-512.

  * Certificates created for the LDAP server must include Subject Alternative Names (SANs) since the use of Common Name has been deprecated. Certificates without SANs will fail verification, resulting in connectivity issues.


## Trusted Certificates

To provide secure authentication while connecting to external targets, you can add a third-party certificate from a trusted source or a self-signed certificate that affirms the identity of your targets. The third-party certificate is signed by the issuing trusted point, which can be a root certificate authority (CA), an intermediate CA, or a trust anchor that is part of a trust chain that leads to a root CA.

The Trusted Certificates table view that is accessible from Settings > Authentication > Certificates >Trusted displays the list of certificates that you added in Intersight.

## Add Certificate

The following task provides details on how to add trusted certificates in Intersight Virtual Appliance.

  1. Log into Intersight Virtual Appliance as a user with account administrator role.

  2. Choose Settings > Authentication > Certificates > Trusted.

The following details about the Trusted Certificates are displayed in the table view:

  * Name—Common name of the CA certificate

  * Issued By—Certificate issuing authority

  * Usage—Displays the number of targets using the certificate

  * Expires—The expiry date of the certificate

  3. Click Add Certificate to add a trusted certificate.

  4. Click Browse to select the certificate that is stored in your system and click Save.

After the certificate is successfully imported, it is displayed in the Trusted Certificates table view. You can select trusted certificates from this table while claiming targets using Intersight Assist. For information on how to claim targets using Intersight Assist, see [Target Claim Using Intersight Assist](/help/appliance/getting_started/claim_targets#target_claim_using_intersight_assist).

Important:

The trusted certificate that you want to import must be in base64 encoded X.509(PEM) format.


## Adding SSL Certificates

To enable secure HTTPS access of the appliance through the browser, you can generate a Certificate Signing Request and import a certificate or you can switch to a self-signed certificate. You can access these tasks by navigating to Settings > Authentication > Certificates > SSL.

To create a Certificate Signing Request (CSR):

  1. In the appliance UI, choose Settings > Authentication > Certificates > SSL.

The following details about the **Current Certificate** are displayed:

  * Name—Common name of the CA certificate

  * Added By—User that added the certificate to the account

  * Issued By—Certificate issuing authority

  * Expires—Expiration date of the certificate

Click View All to display the View Certificate window. In addition to the details listed above, you can also view these details about the certificate: Fingerprints, Country, Locality, Organization, Organizational Unit, and the details of the Issuer Name, Organization, Common Name, and the Signature Algorithm.

  2. From the **Action** drop-down menu, select Create CSR.

The Create Certificate Signing Request wizard displays. Enter the following details as required.

  * Organization—The legal name of your organization

  * Organizational Unit—The subdivision of your organization that handles the certificate. For example HR, IT etc

  * Locality—The city/town where your organization is located

  * State—The state where your organization is located

  * Country—The two-letter country code where your organization is located. For a complete list of the country codes, see [ISO 3166](https://www.iso.org/iso-3166-country-codes.html)

  * Email Address—An email address used to contact your organization

  * Modulus—Modulus of the RSA private key used to sign the CSR

  3. Click Create CSR.


When you click Create CSR, a new Certificate Signing Request (CSR) is generated. You can select one of the following options:

  * **Download CSR** —Allows you to download and store the CSR locally to use it to obtain a trusted certificate from a Certificate Authority (CA).

Note:

Use only the appliance FQDN in the Subject Alternative Names (SAN) field during the certificate-issue request process. Do not enter hostnames or IP addresses in the SAN field while obtaining a trusted certificate for Intersight Appliance and Intersight Assist from a Certificate Authority.

  * **Delete CSR** —Delete the CSR if you do not want to use it to generate a trusted certificate.

  * **Apply Certificate** —After the CA issues a certificate, click Apply to paste the contents of the certificate in the **Certificate** field in the Apply Certificate window. You can also click the Upload button and upload a certificate. Click Apply to complete the process. The CA-issued certificate can be in .csr, .pem or .crt format.


To switch to a self-signed certificate:

  1. In the appliance UI, choose Settings > Authentication > Certificates > SSL.

  2. From the **Action** drop-down menu, select Switch to Self-Signed.

A popup window appears warning you that switching to self-signed certificates will take a few minutes.

  3. Click Apply to proceed.


  * Cisco recommends that you use CA signed certificates to access the appliance. The latest browsers may disable access to the appliance if self-signed certificates are used. Intersight Virtual Appliance provides the option to switch to self-signed certificate to extend the validity of the certificate, if the self-signed certificate provided by Cisco expires.

  * When you choose to switch to a self-signed certificate, the current SSL certificate will be replaced by the newly generated self-signed certificate. You can verify if the new certificate is applied by clicking the lock or the warning icon preceding the URL in the address (location) bar of your browser. After the refresh, you will be taken directly to the Settings > Certificates screen without having to log into the appliance once again.


## Configuring LDAP/AD

Intersight Virtual Appliance supports LDAP/AD based remote authentication. You can configure the appliance to authenticate a user login using LDAP. You can configure multiple LDAP domains and choose a domain for the login.

An LDAP user can log into Intersight Virtual Appliance with email ID or username, and select the corresponding domain in which the LDAP user is configured. You can add up to 6 LDAP domains per Intersight Account. You can view the list of configured LDAP domains. Click [here](/help/video#cisco_intersight_virtual_appliance_ldap/ad_setup) to watch a video about how to integrate your virtual appliance with the LDAP/AD services.

To set up LDAP authentication from Settings in Intersight Virtual Appliance, do the following:

  1. Log into Intersight Virtual Appliance as a user with account administrator role.

  2. Choose Settings > Networking > LDAP/AD.

  3. Click Create LDAP. The Configure LDAP window displays.

  4. On the Configure LDAP screen, add the corresponding details in the fields that are listed below, and click Save.

  * Name—Enter a name to easily identify the LDAP domain that you are configuring.

  * Base DN—Enter a Base Distinguished Name (DN) for the server. For example, DC=Intersight, DC=com.

  * Bind DN—Enter a DN used to authenticate against the LDAP server and the password for the user.

  * Group Attribute—Enter the Group member attribute to which an LDAP entry belongs. Intersight Virtual Appliance uses this Group attribute to map/assign Intersight roles to the user. The default value is member and you can change it from Edit LDAP settings.

  * Password—Enter a DN password for the user.

  * Nested Group Search—When enabled, an extended search runs through the chain of ancestry all the way to the root and returns all the groups and subgroups that each of the groups and subgroups belong to, recursively.

  * Enable Encryption—You must enable Encryption to secure the communication over the LDAP server. If encryption is enabled, a trusted root certificate has to be added. For more information, see [Add Certificates](/help/settings#add_certificate).

Note:
  * In a future release, Intersight Virtual Appliance will be phasing out support for certificates signed with the SHA-1 hash functions. It is strongly recommended that you upgrade your certificates to use signature algorithms with hash functions that are stronger than SHA-1, such as SHA-256, SHA-384, or SHA-512.

  * Certificates created for the LDAP server must include Subject Alternative Names (SANs) since the use of Common Name has been deprecated. Certificates without SANs will fail verification, resulting in connectivity issues.

  * Configure LDAP Servers—Add up to three LDAP Server IP addresses or hostnames, and a corresponding LDAP Server port for each LDAP Server.


Attention:

  * LDAPS is supported on Port 636 and Port 3269. All other ports support LDAP on TLS.

  * **Intersight Virtual Appliance uses the email ID or username to log in an LDAP user**. If you want to use email ID to log into the appliance, configure the mail attribute in the LDAP server. If you want to use the username, use the sAMAccountName configured for that user in the LDAP server.

  * **After you configure the LDAP settings, you must add a Group to assign appropriate roles to the users in the LDAP Group . For more information, see Adding a Group.**

  * **If you are using the Intersight API to configure the Appliance LDAP login, ensure that the LDAP policies are tagged appliance.management:true. This is automatically done for the users configuring the LDAP under Settings.**


After you add the required details to configure LDAP settings, wait for the DeployApplianceLDAP workflow to complete before verifying the configuration settings or logging in as an LDAP user. You can check the status of the workflow in **Requests**.

To verify the LDAP configuration settings:

  1. Click on the ellipsis in the row for which you want to verify the LDAP configuration settings.

  2. Click Test Configuration.

The Test LDAP/AD Configuration pop-up screen appears.

  3. Add a valid username or email address and password.

  4. Click Test.


Once the test completes, the results displayed in the Configuration Status column are as follows:

  * Verified—Indicates that the LDAP configuration has been verified successfully. Hover on it to see the number of user groups of the test user.

  * Failed—Indicates that the LDAP configuration verification test failed. Hover on it to read the error message.

  * Unverified—Indicates that a test has not been run for a configured LDAP server.


## Configuring Password Policy for Local Users

This task provides details on how to configure password policy for local users in Intersight Virtual Appliance.

  1. Log into Intersight Virtual Appliance as a user with account administrator role.

  2. Choose Settings > Authentication > Local Users Password Policy.

You can view the details of the existing password policy.

  3. Click Configure.

The Configure Local Users window displays.

  4. Configure the password policy by updating the following password policy options as needed.

Password Policy Options| Allowed Range/Default Value  
---|---  
Minimum Length of Password| 8-127 charactersDefault is 8  
Minimum Number of Required Upper Case Characters| 1-64 charactersDefault is 1  
Minimum Number of Required Lower Case Characters| 1-64 charactersDefault is 1  
Minimum Number of Required Numeric Characters| 1-64 charactersDefault is 1  
Minimum Number of Special Characters| 0-64 charactersDefault is 0Note:Special characters include punctuation and symbol characters.  
Number of Previous Passwords Disallowed| 0-10Default is 0  
Minimum Number of Characters Different From Previous Password| 0-15Default is 0Note:Differences from the previous password are verified based on the same character location within the specified password.  
Minimum Days Allowed Between Password Changes| 0-7 daysDefault is 0Note:If you specify a value of 0 for this password policy option, then the user is not limited on time between password changes.  
Time Duration for Incorrect Login Attempts (Seconds)| 300 - 3600 seconds (5 – 60 minutes)Default is 1800 seconds (30 minutes)Time duration is tracked for consecutive incorrect login attempts. Users will be locked out if they exceed the configured number of max incorrect login attempts during this duration.For more information about the lockout capability, see [Locking Out Local User Accounts](/help/appliance/settings#locking_out_local_users_accounts).  
Max Consecutive Incorrect Login Attempts Allowed| 3 -10Default is 5Users will be locked out after exceeding the max consecutive incorrect login attempts allowed within the configured time duration.  
Enable Lockout for Admin User| Default is false.Determines if the user lockout feature must be enabled for the local “admin” user. This option is always enabled for other local users.For more information about the lockout capability, see [Locking Out Local User Accounts](/help/appliance/settings#locking_out_local_users_accounts).  
Lockout Time Period (Seconds)| 60 – 3600 seconds (1 – 60 minutes)Default is 900 (15 minutes)Duration, in seconds, during which a local user account will remain locked. The account is automatically unlocked after the configured lockout time period elapses.  
  
  5. Click Save.

You can verify the password policy changes on the next password change.


## Adding Users

Intersight Virtual Appliance allows you to override Group role assignments to users. On the User screen, you can view a list of the Users added to an account. The list displays the Name, Identity Provider, Email, Role, and the Last Login Time for a user. You can add Remote Users as well as Local Users. Note that you can add up to 100 Local Users.

  * Remote Users—authenticated via IDP (LDAP and SSO)

  * Local Users—authenticated via Intersight Virtual Appliance


To add a user in Intersight Virtual Appliance, do the following:

  1. Log into Intersight Virtual Appliance as a user with account administrator role or User Access Administrator role.

  2. Choose Settings > User Permissions > Users.

  3. Click the Add User button. The Add User window displays.

You have the option of adding a Remote User or a Local User. Note that you can add up to 100 Local Users.

**To add a Remote User, enter the following details:**

  * Identity Provider—Select the Identity Provider that you want to add to this account. This can be any one of the Intersight validated Identity Providers. For more information, see Validated Identity Providers in the Supported Systems page in <Your FQDN>/help.

If you add an LDAP user, you must add them under the appropriate Identity Provider (IDP). The name of the IDP will be the same as the LDAP Domain Name that you have configured in LDAP Settings.

  * User ID—Enter a valid email ID or username used to register the account with the Identity Provider. **The username must be the same as the sAMAccountName that is configured on the LDAP server**. If you are using email to log in, ensure that the email ID is the same as configured in the mail attribute in the LDAP server.

  * Role—You can assign one role for a remote user account. For more information, see [Roles and Privileges](/help/appliance/resources/RBAC#roles_and_privileges).

**To add a local user, enter the following details:**

  * First Name—First name of the local user

  * Last Name—Last name of the local user

  * User ID—Enter an email ID or username which is used by the local user to log into the appliance.

  * Password—Enter a valid password as per the local user password policy.

  * Role—You can assign multiple roles for a local user account. For more information, see [Roles and Privileges](/help/appliance/resources/RBAC#roles_and_privileges).

  4. Click Add to add the new user, remote or local, as the case may be.


Attention:

The UserID and password that is entered while adding the new local user must be conveyed to the new local user directly as there is no mechanism currently in Intersight Virtual Appliance to automatically notify the login credentials to the new local user. Once the new local user logs in using these credentials, a prompt appears that mandates the new local user to change the password.

Local users can change their passwords any time by navigating to Profile Menu in the top right of the screen and then clicking Change Password.

## Locking Out Local Users Accounts

Consecutive incorrect login attempts within a configured time duration are tracked for local users and the accounts will be locked out if they exceed the configured number of maximum incorrect login attempts during this duration. Once the local user account is locked, the Local User table displays a warning icon next to the user. The account is automatically unlocked after the configured lockout period elapses. The Account Administrator or the User Access Administrator can unlock the account by resetting the password, during the configured lockout period.

Note:

The lockout capability:

  * Applies to only local users and does not apply to remote users.

  * Applies to local “admin” user only if the setting is enabled.


## Resetting the Password of Local Users

Account Administrators can reset the password of local users. User Access Administrators can also reset the password of local users except for users with the role of Account Administrator.

To reset the password of a local user:

  1. Log into Intersight Virtual Appliance as a user with account administrator role.

  2. Choose Settings > User Permissions > Users.

  3. Select the local user that you want to reset the password.

  4. Click the pencil icon and change the password.

  5. Click Save.


Attention:

When an Account Administrator resets the password for the local “admin” user, only the GUI password is changed. The SSH password of the local “admin” user remains unchanged. The local “admin” user must log into the appliance using the newly reset password. Once the local “admin” user is logged in, a prompt appears that mandates the local “admin” user to change the password, which then resets both the GUI and the SSH passwords.

## Adding Groups

A Group represents a collection of users with a specific role, permission, and privileges. You can create multiple user groups to assign common roles and privileges to a set of users. On the Group screen, you can view a list of the Groups added to an account. The list displays the Name, Identity Provider, Role, and the Group Name in Identity Provider.

Attention:

**You must be an Account Administrator or User Access Administrator to create a group or assign user roles.**

To add a group, do the following:

  1. Log into Intersight Virtual Appliance as a user with account administrator role.

  2. Choose Settings > User Permissions > Groups.

  3. Click the Add Group button at the top right.

The Add Group window displays.

  4. In the Add Group window, add the following details:

  * Identity Provider—Select the Identity Provider that you want to add to this account. This can be any one of the Intersight validated Identity Providers. For more information, see [Validated Identity Providers](/help/appliance/supported_systems#validated_identity_providers).

If you are adding an LDAP group, you must add it under the appropriate Identity Provider (IDP). You must select the appropriate LDAP domain for groups that would log in with their LDAP credentials. The name of the IDP will be the same as the LDAP Domain Name that you have configured in LDAP Settings.

  * Name—Enter a name to identify the group in Intersight.

  * Group Name in Identity Provider—Enter the user group name you have added in the Identity Provider. Group name must be in the LDAP distinguished name (DN) format. For example:

cn=Finance,cn=Users,dc=example,dc=com

  * Role—You can assign one of following roles for a user group.

  * Account Administrator—As an Account Administrator, members of the group can claim targets, cross launch element managers, create profiles and policies, collect tech support bundles, and make configuration changes to the claimed targets or the account.

  * Read-Only—In this role, members of the group can view details, and status of the claimed targets within the account. However, you cannot make any configuration changes to the claimed targets or the account.

  * Device Technician—In this role, members of the group can claim a target in Intersight and view a list of the claimed targets in the Targets table view.

  * Device Administrator—In this role, members of the group can claim a target in Intersight, view a list of the claimed targets, and delete (unclaim) a target.

  * Server Administrator—In this role, members of the group can perform all server actions including firmware upgrade, view server details, collect tech support bundles, set server tags, create, edit, and deploy a server profile or policy.

  * HyperFlex Cluster Administrator—In this role, members of the group can create, edit, and deploy a HyperFlex cluster profile, upgrade a cluster, set cluster tags, view cluster dashboard and summary, monitor alarms, collect tech support bundles, and launch and manage HX Connect.

  * User Access Administrator—In this role, members of the group can view account details, perform all User Access related actions, including adding a User, adding a Group, setting up Identity Providers and Single Sign-On, generate API keys related to the account.

  5. Click Save to add the new group to the account.


## Creating a Role

In addition to the system-defined roles in Intersight, you can create a user-defined role. On the Roles screen, you can view a list of the roles added to an account. This list displays the Name, Type, Usage, Scope, and a Description of the roles.

Attention:

**Only users with Account Administrator or User Access Administrator privileges can create a user-defined role.**

To create a user-defined role, do the following:

  1. Log into Cisco Intersight.

  2. Choose Settings > User Permissions > Groups.

  3. From Roles, click Create Role.

  4. Enter a Name to identify the role in Intersight and a Description about the usage of the role.

You can choose to retain the default account level settings for Session Timeout, Idle Timeout, and Concurrent Sessions, or you can choose to customize these settings.

  5. Under Session & Idle Timeout settings, you can choose to do one of the following:

  * Enable Use Account Default Settings—This option is enabled by default. You can inherit the session timeout values from the Account level settings. The values will be used as the default settings during role creation. To check the account level Session Timeout and Idle Timeout details, navigate to the System > Account Details.

  * Disable Use Account Default Settings—You can disable this option to set values for the following fields at the Role level.

  * Session Timeout (Seconds) is the session expiry duration in seconds. The minimum value is 300 seconds and the maximum value is 31536000 seconds (1 year). The system default value is 57600 seconds.

  * Idle Timeout (Seconds) is the interval for the web session in seconds. When a session is not refreshed for this duration, the session is marked as idle and removed. The minimum value is 300 seconds and the maximum value is 18000 seconds (5 hours). The system default value is 1800 seconds.

  * Maximum Number of Concurrent Sessions (Sessions) is the number of concurrent sessions allowed in an account or permission. The minimum number of sessions is 1 and maximum number of sessions is 128. The default value is 128.

  6. Click Next.

  7. Select a Scope to delegate the user access to resources in the account. You can choose to give a user access to the entire account or restrict access to a selected organization.

  * All—User has access to all account resources. Add Privileges to assign roles to the user. The selected privileges will be applied to the entire account.

  * Organization—User has access to the specified organizations only. Select one or more Organizations from the drop-down list and Add Privileges to assign roles to the user. For more information on Privileges, see the Roles section.

  8. Click Create to add the new User Defined Role to the account.


## Switching an Account or Role

You can switch between accounts or roles in Intersight Virtual Appliance without logging out of the application. If you are logged into multiple accounts or roles, the Profile menu in the Intersight dashboard provides the option to Switch Account or Role.

![](../../../../../../../en/us/td/i/300001-400000/300001-310000/306001-307000/306921.jpg)

Note:

  * The Switch Account or Role option is not available if you are authorized to access a single account and have only one role mapped to that account.

  * If you use the account URL to log into Intersight, the Switch Account and Role option enables you to switch only between roles within the same account.

  * At the time of switching, accounts are re-evaluated based on the attributes returned by the Identity Provider (IdP) after authentication. The users added to the account are also re-authenticated for their roles by the Identity Provider. Therefore, before you switch between accounts, if Intersight detects that there is a change in your account or role, it appears in the Select Account and Role list.

  * For Intersight Virtual Appliance, you must configure LDAP or log in with SSO to view the Switch Account or Role option.


To switch accounts, do the following:

  1. Navigate to Profile > Switch Account or Role. The Select Account and Role window displays.

  2. In the Select Account and Role window, select the account (or role) that you want to switch to. You will be logged in to the new account.

  3. To change the role, navigate to Settings > User Permissions > Users, and select the user that you want to change the role for, and click the Edit icon.

  4. In the Edit User window, select the role and click Save.


## Generating and Managing API Keys

An API key is used to register your application with Intersight.

To generate and manage API keys, do the following:

  1. Log into Intersight Virtual Appliance as a user with account administrator role.

  2. Choose Settings > API Settings > Keys.

  3. Click Generate API Keys.

  4. In the Generate New API Key screen, enter the purpose for the API Key, and click Generate. The API Key ID and RSA Private Key are displayed.

  5. Save the private key information in a .pem file.

Note:

Make sure to save it in a location accessible from your scripts.


## REST APIs

To become familiar with REST APIs, review the API resource information and functionality at [API Docs](/apidocs).

## OAUth2 Tokens

In Intersight, you can create an OAuth 2.0 Client Credentials Grant Type application.

To create an OAuth 2.0 application:

  1. Navigate to Settings > OAuth2 Tokens .

  2. Click Create OAuth 2.0.

  3. In the Create OAuth 2.0 screen:

     1. In the App Name field, enter a name for the application. This is a mandatory requirement.

     2. In the Description field, enter a description for the application. This is a mandatory requirement.

     3. Do one of the following to configure the validity of the OAuth application:

  * In the Expiration Time field, use the calendar to choose a date up to the maximum expiration period allowed. The calendar shows the period available for expiration time based on the creation date and maximum expiration period configured by the Account Admin.

  * Use the OAuth Application Never Expires toggle button to configure the OAuth application with no expiration date.

Note:
  * If the OAuth Application Never Expires toggle button is not visible, it indicates that the Account Admin has not permitted the creation of an OAuth 2.0 application that does not have an expiration date.

  * You can edit the expiration date at any time, provided the selected date is up to the maximum expiration period configured by the admin at the account level.

  4. Click Create.

The View OAuth 2.0 screen displays the Client ID and Client Secret.

  5. Save the Client ID and Client Secret, select the confirmation check box, and then click Close.

Note:

The Client Secret for the application cannot be recovered after you close this screen. If you misplace the Client Secret, you can create a new OAuth 2.0 application to generate a new client ID.

The OAuth application is displayed in the OAuth 2.0 Details Table View.


To edit an OAuth 2.0 application:

  1. From the OAuth 2.0 Details Table View, select the OAuth 2.0 application that you want to edit.

  2. Click the ellipsis (…) icon of the application, and then choose Edit.

The Edit OAuth 2.0 screen is displayed.

  3. Edit the name, description, or expiration time of the OAuth 2.0 application:

Note:
  * While editing the expiration time, you are limited to selecting a date that is within the maximum expiration time set by the Account Admin at the account level.

  * Changing a never-expiring OAuth 2.0 application to one with an expiration date initiates the countdown from that time. Once set as an expiring OAuth application, it cannot be reverted to a never-expiring OAuth Application.

  * You can also edit the name and description of an expired OAuth 2.0 application.

  4. Click Save.

The updated OAuth application is displayed in the OAuth 2.0 Details Table View.


To disable an OAuth 2.0 application:

  1. From the OAuth 2.0 Details Table View, select the OAuth 2.0 application that you want to disable.

  2. Click the ellipsis (…) icon of the application, and then choose Disable.

Note:

The expiration date will continue to count down even if the OAuth 2.0 application is disabled.


To delete an OAuth 2.0 application:

Note:

Before deletion, active OAuth applications need to be disabled. However, disabled and expired OAuth applications can be deleted directly without requiring additional steps.

  1. From the OAuth 2.0 Details Table View, select the OAuth 2.0 application that you want to delete.

  2. Click the ellipsis (…) icon of the application, and then choose Disable.

  3. Click the ellipsis (…) icon of the application, and then choose Delete.


## Access Token

Upon registration of a Client Credentials application, the user will be issued a unique Client ID and Client Secret. These credentials are required to obtain an access token from Intersight. Obtaining this token is a prerequisite for utilizing Intersight's API services or accessing secured resources.

Token requests can be initiated by the client through the dedicated token endpoint (iam/token) by using the client credentials via one of the following methods:

  1. Client Secret Post:

Clients may authenticate with the authorization server by incorporating their client credentials directly within the request body.

  2. Client Secret Basic:

Clients may authenticate with the authorization server by adhering to the HTTP Basic Authentication scheme as specified in RFC 6717. This involves constructing a string that concatenates the Client ID, a colon, and the Client Secret. This string is then encoded using BASE64 and subsequently inserted into the Authorization header of the token request.


Obtaining an Access Token via Client Secret Post Authentication

Below is an example of the request and response format for acquiring an access token using the Client Secret Post method. Note that the Content-Type header of the POST request should be ‘application/json’.

Request Endpoint:

**https:// <your appliance fqdn>/iam/token**

HTTP POST Request Body:
    
    
    { 
      "grant_type": "client_credentials", 
      "client_id": "<client-id>", 
      "client_secret": "<client-secret>" 
    } 
    

Expected Response:
    
    
    { 
      "access_token": "<access_token>", 
      "expires_in": 600, 
      "token_type": "Bearer" 
    } 
    

This JSON response contains the following elements:

  * access_token: The token utilized for API authentication

  * expires_in: The duration, expressed in seconds, for which the access token remains valid. This value is 600 (10 minutes) and is non-configurable.

  * token_type: The classification of the token, which is "Bearer" in this instance.


Obtaining an Access Token via Client Secret Basic Authentication

Perform the following steps for authenticating against the Intersight API using the client_secret_basic method.

  1. Construct the Token String

Concatenate the assigned client_id and client_secret with a single colon (:) separating the two, resulting in a string of the form client-id:client-secret.

  2. Encode the Token String

Encode the concatenated string using BASE64 encoding to produce the required token value for authentication.

  3. Prepare the Authorization Header

Compose an Authorization header by prefixing the word "Basic" with a space, and then appending the BASE64-encoded token value.

Format of Authorization Header:

`Authorization: Basic <BASE64-encoded token value>`

  4. Execute the POST Request

Send an HTTP POST request to the Intersight token endpoint at the following URL:

Token Endpoint URL:

**https:// <your appliance fqdn>/iam/token**

The POST request must include the Authorization header created in the previous step. The body of the request should specify the grant type as client_credentials. Additionally, the Content-Type header of the POST request should be ‘application/json’.


Example of HTTP POST Request Body:
    
    
    { 
      "grant_type": "client_credentials" 
    } 
    

Expected Response:

The Intersight authorization server will validate the provided credentials and, upon successful authentication, will issue a JSON-formatted response containing the access token and its properties.

Format of Expected JSON Response:
    
    
    { 
      "access_token": "<access_token>", 
      "expires_in": 600, 
      "token_type": "Bearer" 
    } 
    

The response includes the following elements:

  * access_token: The token to be used for bearer authentication when accessing protected Intersight API endpoints.

  * expires_in: The duration, expressed in seconds, for which the access token remains valid. This value is 600 (10 minutes) and is non-configurable.

  * token_type: The classification of the token, which is "Bearer" in this instance.


It is important that the access token be securely stored and appropriately utilized within the validity period to ensure uninterrupted access to Intersight’s API services.

## Configuring Webhooks

Webhooks are notifications that set up integration between software in your local environment and Intersight. Once you establish integration, you can configure a subscription in your local Intersight account to notify you of events detected on [Intersight.com](http://Intersight.com) or on your appliance, as the case may be. When an event is triggered, Intersight sends an HTTP POST (create) request with a payload containing event content to the webhook server payload URL destination.

In SaaS environments, if you use restrictive firewall or proxy server settings, you need to allow-list either the following IP address or Domain Name to ensure that Webhooks work as expected:

  * **Intersight North America Accounts** —IP address ([34.198.174.38](https://us-east-1.console.aws.amazon.com/vpc/home?region=us-east-1#Addresses:public-ip=34.198.174.38)) or Domain Name ([outbound.intersight.com](https://outbound.intersight.com) or [outbound.us-east-1.intersight.com](https://outbound.us-east-1.intersight.com))

  * **Intersight EMEA Accounts** —IP address ([18.156.131.186](https://eu-central-1.console.aws.amazon.com/vpc/home?region=us-east-1#Addresses:public-ip=18.156.131.186)) or Domain Name ([outbound.eu-central-1.intersight.com](http://outbound.eu-central-1.intersight.com%7Csmart-link))


The IP address does not change frequently but may change over long periods. Therefore, a periodic refresh of the configuration is required.

To begin configuring a webhook, perform the following steps:

  1. Log into Intersight as an Account Administrator. To change your role, click the Profile menu in the system name area in the upper right of the Webhooks page. Select Account Administrator.

  2. Click the gear icon in the upper right portion of the Intersight home screen. A popup with options appears.

  3. Click Settings. A secondary navigation bar in the central part of the home screen appears.

  4. At the bottom of the secondary navigation bar, click Webhooks. The Webhooks page appears with a list of current webhook objects.

  5. Click Add Webhook. The Add Webhook dialog box appears.

  6. From the General portion of the Add Webhook screen, provide values for the following items:

  * Name — The string you want to assign as the name of the webhook.

  * Payload URL — The URL of the site from which changes will be evaluated by the webhook.

  * Secret — The string that gives Intersight access to examine the URL for changes.


## Adding an Event

To add an event, perform the following steps:

  1. From the Events portion of the Add Webhook screen, click Add Event to configure an event type that will trigger the webhook.

  2. Ensure the Enable slider is in the right position so that you can expand the Event region.

  3. Click the plus (+) symbol to the left of the Event label to expand the Event region. The Event region expands.

  4. Click the Object Type down arrow to display the event Object Type list. A list of available object types that can be evaluated by the webhook appear. The object type represents an event for which Intersight will send to the webhook server.


## Understanding Event Object Types

In the Object Type list, click an object type that you want the webhook to evaluate. The following table details each event object type.

Server/Software| System/Versions  
---|---  
cond.Alarm| This object type tracks events in your device or software, behaving as a stateful entity. Alarms can be reported by the managed system firmware or can be determined by Intersight.  
workflow.WorkflowInfo| This object type contains information for a workflow execution. This object is a runtime instance of a workflow.  
tam.SecurityAdvisory| This object type is an Intersight representation of a [Cisco Product Security Incident Response Team (PSIRT) advisory definition](https://tools.cisco.com/security/center/publicationListing.x). It includes the description of the security advisory and a corresponding reference to the published advisory.It also includes the Intersight data sources that evaluates how applicable the advisory is to relevant Intersight managed objects. A PSIRT definition is evaluated against all managed objects referenced using the included data sources.Only Cisco TAC and Intersight Developer Operations (DevOps) engineers have the ability to create PSIRT definitions in Intersight.  
tam.AdvisoryInfo| This object type indicates the state of an advisory in the context of a given account. The object type is used to capture a given account's preferences regarding the associated advisory.  
tam.AdvisoryInstance| This object type is an Intersight advisory instance applicable to an Intersight managed object. The advisory instance is created when it is applicable to an Intersight managed object.An advisory instance is retained for a configurable retention period after being cleared to create a history of the instance. A cleared advisory instance is deleted after the retention period elapses.  
compute.Blade| This object type indicates the server housed in a chassis and the hardware shared with other servers in the chassis.  
compute.RackUnit| This object type describes a standalone or Fabric Interconnect (FI)-attached rack-mounted server.  
  
## Creating the Webhook

Note:

Webhook notifications from the Intersight Appliance bypass the configured proxy settings. Therefore, if the appliance requires a proxy to access the internet, webhook delivery might be disrupted despite the proxy configuration.

To complete the webhook creation process, perform the following steps:

  1. Under the Operation region, click Create to add a webhook. Click Update to edit properties of an existing webhook.

  2. In the Filters region, provide an OData filter. For more information, see [API Description of OData Filter](https://intersight.com/apidocs/introduction/query/).

A sample OData filter for the cond/Alarms object type is (Severity eq 'Warning') and (Acknowledge eq 'None'). The OData filter directs Intersight to notify your specific webhook payload URL of any unacknowledged Warning-level alarm.

The following list details available severity levels you can apply to the OData filter.

  * None — No event exists.

  * Info — The least critical severity level, used mostly for descriptive detail on a non-invasive event.

  * Warning — A more serious severity level than Info, indicating a prospective error. It is preventive, preparing you before any significant impact has occurred.

  * Critical — The most elevated severity level, indicating a serious problem has occurred and requires a timely response.

  * Cleared — The event severity has been cleared.

  3. Click Preview API.

The Preview API pane displays in the right side of the screen. It contains a list of API objects and object properties with their values associated with the created OData filter mapped to the current object type. In the example provided above, the Severity property for the OData filter in the cond.Alarm object type has a "Warning" value.

The Preview API pane enables you to verify that the information you created in OData filter is correct.

  4. You can alter the OData filter object property values. For example, the Code property enables you to specify a value that the filter associates with events that have that value.

  5. Click Add.

Intersight displays the new webhook in the Webhook page list.


## Editing a Webhook

You can alter the values originally provided for a webhook.

  1. From the webhook list in the Webhook page, identify an existing webhook for which you want to make changes.

  2. Click the ellipsis (... ) in the far right column of the webhook for which you want to make changes. An options popup appears.

  3. Click Edit. The Edit Webhook screen appears.

  4. Insert changes in the appropriate fields and navigate through the remaining webhook configuration screens to make other changes.

  5. When you are finished, click Update.

The webhook list in the Webhook page appears. The webhook you edited will have new properties.


## Limitations

The following are limitations with webhooks:

  * You can create up to 10 webhooks per account.

  * You can create up to three events per webhook.


## Webhooks Secret

Setting a webhook secret ensures that POST requests sent to the payload URL are from Intersight. When you set a secret, you receive the Authorization header in the webhook POST request.

## Webhooks Alarms

If your webhook is not able to receive notifications, a Warning alarm is generated. Intersight continues to send notifications to your server for the next 48 hours. If the webhooks server is not recovered in this period, a Critical alarm is generated and your webhook becomes inactive, blocking notification transmission.

To manually recover your webhook server, click Verify Connection on your webhook in the Intersight user interface. This function sends a Ping event operation to your server.

## Working with a Ping Event

When you create a new webhook, Intersight sends you a simple ping event to let you know you correctly set up the webhook.

Ping Section| Content  
---|---  
Ping Headers| 
    
    
    User-Agent Intersight/1.0.9-100
    
    
    Content-Length 417
    
    
    Content-Type application/json
    
    
    Digest SHA-256=tybkrJXZydIpn34R8WH7UuiWa7demggZeBpCY7VEM5M=
    
    
    Authorization Signature keyId="61659e337375732d3138592d", algorithm="hmac-sha256", headers="(request-target) host date digest content-type content-length", signature="dmKaKKIfLVskLsbnlSQYLxFIZ07EwMpWqFo+/rNfpKQ=”  
  
Body| 
    
    
    {"ObjectType":"mo.WebhookResult","ClassId":"mo.WebhookResult","AccountMoid":"5f3a32827564612d30a10374","DomainGroupMoid":"5f3a32827564612d30a1037c","MoType":"","Event":null,"Operation":"None","Subscription":{"ObjectType":"notification.AccountSubscription","ClassId":"mo.MoRef","Moid":"61659e337375732d3138592d","link":"https://dev.starshipcloud.com/api/v1/notification/AccountSubscriptions/61659e337375732d3138592d"}}  
  
## Account Details

The Appliance Account Details screen provides an overview of the account, license types, and the user details. In the appliance UI, choose System, and navigate to System > Account Details to view the following details:

  * Account Name—Name of the Intersight account.

  * Account ID—ID of the Intersight account.

  * Access Link—Link that is used to log into the account. You can log in using either the Account ID URL, or the Account Name URL.

Note:

If you have logged in using the Account Name URL and modify the Account Name using the Configure option, the sessions that were opened using the Account Name URL will be terminated. You will have to log in using the new Account Name URL.

  * Region—The region associated with the account. Claimed targets are also associated with this region, and data from those targets is stored in the region.

  * Created Time—The account creation timestamp.

  * Default Idle Timeout—The idle timeout interval for the web session. When a session is not refreshed for this duration, the session is marked as idle and removed. The minimum value is 300 seconds and the maximum value is 5 hours. The system default value is 30 minutes. The value specified here will be used as the default setting during role creation.

  * Maximum Concurrent Sessions per User—The maximum number of sessions allowed per user. The default value is 32. The value specified here will be used as the default value during role creation.

  * Default Session Timeout—The time interval after which the session expires. The minimum value is 350 seconds and the maximum value is 1 year. The system default value is 16 hours. This value will be used as the default value during role creation.

  * Audit Log Retention Period—The time, in months, for which Audit Logs are retained. Audit Logs older than the specified retention period are automatically deleted.

  * OAuth Applications without Expiry—Enables Account Admin to allow the creation of OAuth applications that do not have an expiration date. By default, this option is disabled, as a never-expiring OAuth application is a security threat.

  * OAuth Applications Maximum Expiration Time—The maximum allowed expiration period for an OAuth 2.0 application in this account. The maximum allowed expiration period is 360 days. The default expiration period is 180 days.

  * API Keys without Expiry—Enables Account Admin to allow the creation of API keys that do not have an expiration date. By default, this option is disabled, as a never-expiring API key is a security threat.

  * API Keys Maximum Expiration Time—The maximum allowed expiration period for an API key in this account. The maximum allowed expiration period is 360 days. The default expiration period is 180 days.

  * Tags—The tags created for the account.


## Account Administrator

When configuring your Intersight Account, a user with the Account Administrator role is automatically created. In this case, the Account Administrator role is predefined by the system and allows you to perform all management and administration tasks in Intersight. The assignment of the Account Administrator role is not limited to the automated process; you can also assign this role to other users.

Cisco Intersight strongly recommends that you have at least two Account Administrators to enhance user management, configuration, and security. The importance of having more than one Account Administrator is communicated through a banner message and alarms displayed on the Account Details screen for all accounts that have only one Account Administrator.

Examples of scenarios in which this approach will prove beneficial include:

  * The only registered Account Administrator is no longer available to log into Cisco Intersight.

  * The registered Account Administrator email ID is no longer accessible.

  * There are only third-party users in the Account and they are locked out from Identity Providers (IdP) due to any IdP misconfiguration.

  * The Account Administrator's account is locked after too many failed login attempts and the Admin does not want to wait for cool-off period.


To mitigate these risks, an account with a single Account Administrator role must add another User or User Group.

## Access Details

The Appliance Access Details screen provides an overview of the User Details including the account name, email ID, and the user role. In the appliance UI, choose System > Access Details to view the following details:

  * Name—Name of the user

  * Account Name—Name of the account

  * Email—Email address used to log into the account

  * Role—Role of the user. This role may be a system-defined or a user-defined role.

  * Idle Timeout—The idle timeout interval for the web session in seconds

  * Session Timeout—The session expiry duration in seconds

  * Maximum Concurrent Sessions per User—The maximum number of concurrent sessions per user

  * Login Time—The time when the user logged-in

  * Role Description—Displays a brief description of the user role on the right pane

  * Access—A table view of the users and their privileges is displayed in the bottom pane of this screen


## Appliance Monitoring

The Appliance screen provides an overview of the appliance and health status, and displays alarms when predefined limits are exceeded or when a threshold is raised.

In the appliance UI, choose System > Appliance Details to view the following details:

  * Health—Overall status of the appliance

  * Hostname—Your FQDN or hostname

  * Version—Installed version of the appliance software

  * Cluster Status—Indicates Single-node or Multi-node appliance setup

  * Nodes—A table view of the list of appliance nodes in Cisco Intersight Virtual Appliance. You can search for a specific node by the IP Address, Deployment Size, Node type (node types include HA Management, Standalone, or Metrics), Operational Status, Gateway, Netmask, and more. You can view the alarms on the right pane and filter them by their severity.

  * Resource Monitoring—Visual representation of the appliance’s health status, offers real-time and historical insights into CPU, memory, and disk utilization.

  * CPU Usage and Memory Usage—Line charts display historical resource usage trends over a rolling 7-day window, showing hourly utilization percentages. Data can be filtered by individual cluster nodes.

  * Disk Usage—Table view presents the usage for disks 1 through 8.

Note:
  * Disk 1 contains multiple filesystems. The filesystem with the highest usage is displayed in the table.

  * The filesystem information is included in the alarm when an alarm is triggered.


**Alarms in Intersight Virtual Appliance**

Intersight Virtual Appliance monitors certain critical parameters and raises alarms when predefined limits are exceeded or when a threshold is raised. The appliance currently reports System-level and Node-level alarms. The following table shows the alarm levels and their descriptions.

Table 5. Alarms in Intersight Virtual ApplianceLevel| Component| Description| Comments  
---|---|---|---  
System| Node| Critical: A node is down| One alarm per node  
System| Node| Critical: A node is not ready for service deployment.| One alarm per node  
Node| CPU Usage| Warning: CPU usage above threshold| One alarm per node. Threshold: 75%  
Node| Memory Usage| Warning: Memory usage above threshold| One alarm per node. Threshold: 75%  
Node| File System Disk Usage| Warning: File System disk usage above threshold| One alarm per file system. Threshold: 75%  
Node| File System Disk Usage| Critical: File System disk usage above threshold| One alarm per file system. Threshold: 90%  
System| Number of service instances running| Warning: Number of service instances running less than expected| One alarm per service  
System| Number of service instances ready| Warning: Number of service instances ready less than expected| One alarm per service  
System| Web certificate| Warning: Web certificate expires within 120 daysCritical: Web certificate expires within 90 days| One alarm per appliance  
System| Device certificate| Warning: Device certificate expires within 120 daysCritical: Device certificate expires within 90 days| One alarm per appliance  
System| Appliance Backup| Warning: An Intersight Appliance backup has not been created within the past week. Please schedule or create a new backup.| One alarm per appliance  
System| Appliance Backup| Critical: The most recent Intersight Appliance backup failed. Please schedule or create another backup.| One alarm per appliance  
System| Cloud Connectivity| Warning: Connection to Intersight cloud has been down for more than 30 daysCritical: Connection to Intersight cloud has been down for more than 60 daysHighly Critical: Connection to Intersight cloud has been down for more than 90 days;claiming new devices is not permitted until connection is restored.| One alarm per appliance  
Node| Network Link Connectivity| Warning: The latency between cluster nodes is greater than 10ms| One alarm per link per node  
  
Note:

UCS C-Series server-related faults such as power supply and fan failures are not forwarded by Intersight Virtual Appliance to a syslog server. Please configure the syslog server on the UCS C-Series CIMC side to handle forwarding of the UCS C-Series events and faults.

## Configuring Account Settings

This task provides details on how to configure account settings in the appliance.

  1. Log into Intersight Virtual Appliance as a user with account administrator role.

  2. Choose System > Account Details.

You can view the details of the existing account settings.

  3. Click Configure.

The Configure Account Settings window displays.

  4. Update the following fields as needed.

  * Account Name—Name of the account.

  * Default Idle Timeout (Seconds)—Provide the idle timeout interval for the web session in seconds. The system default value is 18,000 seconds (5 hours).

  * Default Session Timeout (Seconds)—Provide the session expiry duration in seconds. The system default is 57,600 (16 hours).

  * Maximum Concurrent Sessions per User (Sessions)—Provide the maximum number of concurrent sessions allowed per user. The system default as well as the maximum number of concurrent sessions is 32.

  * Audit Logs Retention Period (Months)—Provide the time-period for audit logs retention. The system default is 48 months. The allowed range is between 6 months and 48 months. The Audit logs deletion task is set to run on a daily basis at 6.00 AM UTC, and all the audit logs that meet the retention period set in this field will automatically start getting deleted at this time. Once deleted, audit logs cannot be retrieved.

  * Default Authentication Method—Choose from Local, SSO, and LDAP.

  * Default LDAP Domain—Choose from the available appliance LDAP configurations.

  * OAuth Applications without Expiry—Enables Account Admin to allow the creation of OAuth applications that do not have an expiration date. By default, this option is disabled, as a never-expiring OAuth application is a security threat.

  * OAuth Applications Maximum Expiration Time—The maximum allowed expiration period for an OAuth 2.0 application in this account. The maximum allowed expiration period is 360 days. The default expiration period is 180 days.

  * API Keys without Expiry—Enables Account Admin to allow the creation of API keys that do not have an expiration date. By default, this option is disabled, as a never-expiring API key is a security threat.

  * API Keys Maximum Expiration Time—The maximum allowed expiration period for an API key in this account. The maximum allowed expiration period is 360 days. The default expiration period is 180 days.

  * Tags—The tags created for the account.

  5. Click Save.


## Creating an Organization

On the Organizations screen, you can view a list of organizations added to an account. This list displays the Name, Memberships, Usage, and Description.

Attention:

**Only users with Account Administrator privileges can create organizations. Users with User Access Administrator privileges cannot create organizations but can view them in the User Account and assign the organizations to roles.**

To add an organization, do the following:

  1. Log into Cisco Intersight.

  2. Choose System > Organizations.

  3. Click Create Organization.

  4. Enter a Name to identify the organization in Intersight and a Description about the usage of the organization.

  5. Under Memberships, you can choose to assign access to all resources or restrict access to a selective group of resources. Select one of the following options for memberships:

  * Custom—From the list of targets available in the account, select the required targets, to allocate a set of physical resources to the organization.

Important:

Profiles and Policies that are created within a custom organization are applicable only to the targets in the same organization.

  * All—All the targets available in the account will be included in this organization.

  6. Click Create to add the new organization to the account.


To learn more about Organizations and how to leverage them to support multi-tenancy in an account, see the Role Based Access Control under [Resources](/help/resources#role_based_access_control_\(rbac\)_in_intersight) in the [Help Center](/help/home) or _< http://your fqdn.com>_/help.

## Tech Support Diagnostic File Collection

When you open a case with Cisco TAC, Intersight collects Tech Support diagnostic files to assist with an open support case. The data collected could include (but is not limited to) hardware telemetry, system configuration, and any other details which aid in active troubleshooting of the TAC case. Tech Support collection is allowed to occur regardless of data collection options you specify. However, this information is not collected arbitrarily, but only when you open a case against a system, requiring assistance with the system support.

## Proactive Return Material Authorization (RMA)

Intersight leverages telemetry obtained from the connected targets to start the replacement process when a target encounters failures. When an eligible hardware failure occurs, Intersight automatically raises a Service Request (SR) and proactively authorizes a Return Material Authorization (RMA), thus reducing the time from failure to replacement significantly. This feature is available to all Intersight accounts that meet the requirements listed below and have not explicitly opted-out of the program.

Attention:

This feature is currently supported on SaaS and Connected Virtual Appliance.

Proactive RMA support provides the following benefits:

  * Significant reduction in time and effort to receive a replacement part

  * Automatic creation of a service request and preauthorization of the RMA

  * Automatic collection of specific diagnostic data

  * Prevention of RMAs created erroneously for software failures


**Requirements**

  * The target must be connected and claimed either to Intersight Cloud directly or to a Connected Virtual Appliance. For information on how to claim a target, see [Target Claim](/help/getting_started/claim_targets).

  * The target must be covered under a valid support contract (for example: [Smart Net Total Care](https://www.cisco.com/c/m/en_us/customer-experience/support/smart-net-total-care.html)).

  * For Connected Virtual Appliances, Proactive RMA must be enabled. When Proactive RMA is enabled, ensure that you enable the Allow Tech Support Bundle Collection option as well.


**How does Proactive RMA work?**

When the fault event occurs:

  * A support case is created with either the configured email or the last entitled user that logged into Intersight.

  * An RMA is automatically generated and will await confirmation of shipping details.

  * An email containing the complete SR and RMA details, along with information about the impacted device, is sent from sherholm@cisco.com to the user on whose behalf the SR was created. Additionally, any other users configured via tags are copied on this email.

Note:
  * Ensure that you add the sherholm@cisco.com email address in your allowed list.

  * Any entitled user can transfer ownership of the RMA to themselves and fill out the necessary details. Customers can manage and view entitled users for a contract in the Service Access Management Tool (SAMT) if they are an SAMT Admin for their contract.

  * After the shipping and delivery details are confirmed, the replacement part will be sent in accordance with the entitled Service Level Objective (SLO).


Following faults are currently in scope for Proactive RMA:

  * Memory errors

  * C-Series fan failures

  * Fabric Interconnect fan failures

  * UCS Drive Failures

  * HyperFlex drive failures

  * Nutanix drive failures


For details on the specific fault codes and failure requirements, see the [Proactive RMA Documentation](https://www.cisco.com/c/en/us/support/docs/servers-unified-computing/intersight/215172-proactive-rma-for-intersight-connected-d.html).

**Configuration Options**

In Intersight, configuration options for this feature are set using tags either in the user interface or through the API. You can explicitly configure the email address that you want to associate with the service request and the RMA. Proactive RMA may also be disabled at the Intersight account level. For specific instructions see the [Advanced Configuration](https://www.cisco.com/c/en/us/support/docs/servers-unified-computing/intersight/215172-proactive-rma-for-intersight-connected-d.html#toc-hId--1677922521) section of the Proactive RMA Documentation, and the documentation on [how to set tags](https://www.cisco.com/c/en/us/support/docs/servers-unified-computing/intersight/215171-setting-tags-on-intersight-account-via-a.html).

In Intersight Connected Virtual Appliance, use the following instructions to enable or disable the necessary telemetry for this feature:

  1. Log into Intersight Virtual Appliance as a user with account administrator role.

  2. Navigate to Settings > Security and Privacy.

The existing configuration details for data collection is displayed.

  3. Click Configure.

You can enable or disable the Proactive RMA option as needed.

If you enable Proactive RMA, ensure that you enable the Allow Tech Support Bundle Collection option as well.

  4. Click Save.


Note:

  * If the data collection option had been enabled on your appliance before an appliance upgrade, then the Proactive RMA setting will be enabled by default after the upgrade completes.

  * Fault data is collected, if you enable the Proactive RMA option under Data Collection in the Security & Privacy screen.


For detailed information about the Proactive Support workflow, supported faults, configuring the advanced options, setting tags, and caveats, see [Proactive RMA for Intersight Connected Devices](https://www.cisco.com/c/en/us/support/docs/servers-unified-computing/intersight/215172-proactive-rma-for-intersight-connected-d.html).