# Intersight SaaS Settings

| | |
|---|---|
| **URL Title** | Intersight SaaS Settings |
| **URL** | https://intersight.com/help/saas/settings |
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260402103337138/docs/cloud/data/articles/features/cisco_intersight/settings/en/index.html |
| **HTML Title** | Document |
| **Source file** | `ucs-docs-raw/html/intersight-saas_settings.html` |
| **File type** | HTML |
| **Fetched on** | 2026-04-08 08:43:34 |

---

To view or configure the account details, click Systems > Account Details. The following details displayed are:

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


You can modify the account details by clicking Configure. The Account ID and Creation Date cannot be modified. For more information on Account Settings Configuration, see [Account Settings Configuration](/help/system/settings#account_settings_configuration).

## Account Administrator

When configuring your Intersight Account, a user with the Account Administrator role is automatically created. In this case, the Account Administrator role is predefined by the system and allows you to perform all management and administration tasks in Intersight. The assignment of the Account Administrator role is not limited to the automated process; you can also assign this role to other users. For more information, see [Role-Based Access Control in Intersight](/help/resources/RBAC#role-based_access_control_in_intersight).

Cisco Intersight strongly recommends that you have at least two Account Administrators to enhance user management, configuration, and security. The importance of having more than one Account Administrator is communicated through a banner message and alarms displayed on the Account Details page for all accounts that have only one Account Administrator.

Examples of scenarios in which this approach will prove beneficial include:

  * The only registered Account Administrator is no longer available to log into Cisco Intersight.

  * The registered Account Administrator email ID is no longer accessible.

  * There are only third-party users in the Account and they are locked out from Identity Providers (IdP) due to any IdP misconfiguration.

  * The Account Administrator's account is locked after too many failed login attempts and the Admin does not want to wait for cool-off period.


To mitigate these risks, an account with a single Account Administrator role must add another User or User Group. For more information, see [Adding a User](/help/resources/Managing_Roles_and_Privileges#adding_a_user) and [Adding a Group](/help/resources/Managing_Roles_and_Privileges#adding_a_group).