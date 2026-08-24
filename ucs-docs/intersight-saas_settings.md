# Intersight SaaS Settings

| | |
|---|---|
| **URL Title** | Intersight SaaS Settings |
| **URL** | https://intersight.com/help/saas/settings |
<<<<<<< HEAD
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260821153740774/docs/cloud/data/articles/features/cisco_intersight/settings/en/index.html |
| **HTML Title** | Document |
| **Source file** | `ucs-docs-raw/html/intersight-saas_settings.html` |
| **File type** | HTML |
| **Fetched on** | 2026-08-24 09:16:31 |
=======
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260626102158280/docs/cloud/data/articles/features/cisco_intersight/settings/en/index.html |
| **HTML Title** | Document |
| **Source file** | `ucs-docs-raw/html/intersight-saas_settings.html` |
| **File type** | HTML |
| **Fetched on** | 2026-06-30 16:42:42 |
>>>>>>> b54dc188455b65bee6c95ef06462b9c67adf0b3a

---

To view or configure account details, click **Systems** > **Account Details**. The following details are displayed:

  * **Account Name** : Name of the Intersight account.

  * **Account ID** : ID of the Intersight account.

  * **Access Link** : Link used to log in to the account. You can log in using either the Account ID URL or the Account Name URL.

> **Note:**
> 
> If you logged in using the Account Name URL and modify the Account Name by using the Configure option, sessions opened using the previous Account Name URL are terminated. You must log in again using the new Account Name URL.

  * **Region** : The region associated with the account. Claimed targets are also associated with this region, and data from those targets is stored in the region.

  * **Created Time** : The account creation timestamp.

  * **Default Idle Timeout** : The idle timeout interval for the web session. When a session is not refreshed for this duration, the session is marked as idle and removed. The minimum value is 300 seconds and the maximum value is 5 hours. The system default value is 30 minutes. The value specified here will be used as the default setting during role creation.

  * **Maximum Concurrent Sessions per User** : The maximum number of sessions allowed per user. The default value is 32. The value specified here will be used as the default value during role creation.

  * **Default Session Timeout** : The time interval after which the session expires. The minimum value is 350 seconds and the maximum value is 1 year. The system default value is 16 hours. This value will be used as the default value during role creation.

  * **Audit Log Retention Period** : The time, in months, for which audit logs are retained. Audit logs older than the specified retention period are automatically deleted.

  * **OAuth Applications without Expiry** : Enables Account Admin to allow the creation of OAuth applications that do not have an expiration date. By default, this option is disabled, as a never-expiring OAuth application is a security threat.

  * **OAuth Applications Maximum Expiration Time** : The maximum allowed expiration period for an OAuth 2.0 application in this account. The maximum allowed expiration period is 360 days. The default expiration period is 180 days.

  * **API Keys without Expiry** : Enables Account Admin to allow the creation of API keys that do not have an expiration date. By default, this option is disabled, as a never-expiring API key is a security threat.

  * **API Keys Maximum Expiration Time** : The maximum allowed expiration period for an API key in this account. The maximum allowed expiration period is 360 days. The default expiration period is 180 days.

  * **Tags** : The tags created for the account.


You can modify account details by clicking **Configure**. The Account ID and Creation Date cannot be modified. For more information about configuring account settings, refer to [Account Settings Configuration](/help/system/settings#account_settings_configuration).

## Account Administrator

When you configure your Intersight account, a user with the Account Administrator role is automatically created. This predefined system role allows the user to perform all management and administration tasks in Intersight. You can also assign the Account Administrator role to other users. For more information, refer to [Role-Based Access Control in Intersight](/help/resources/RBAC#role-based_access_control_in_intersight).

Cisco Intersight strongly recommends having at least two Account Administrators to improve user management, configuration, and security. For accounts with only one Account Administrator, a banner message and alarms on the **Account Details** page emphasize the importance of adding another administrator.

This approach is beneficial in the following scenarios:

  * The only registered Account Administrator is no longer available to log in to Cisco Intersight.
  * The registered Account Administrator email ID is no longer accessible.
  * The account contains only third-party users, and an Identity Provider (IdP) misconfiguration prevents them from logging in.
  * The Account Administrator's account is locked after too many failed login attempts, and the administrator does not want to wait for the lockout period to end.


To mitigate these risks, an account with a single Account Administrator must add another user or user group. For more information, refer to [Adding a User](/help/resources/Managing_Roles_and_Privileges#adding_a_user) and [Adding a Group](/help/resources/Managing_Roles_and_Privileges#adding_a_group).