# UCS Manager CLI Administration Management Guide 4.3

| | |
|---|---|
| **URL Title** | UCS Manager CLI Administration Management Guide 4.3 |
| **URL** | https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Admin-Management/4-3/b_cisco_ucs_manager_cli_administration_mgmt_guide_4-3.html |
| **Long URL** |  |
| **HTML Title** | Cisco UCS Manager Administration Management Using the CLI, Release 4.3 |
| **Source file** | `ucs-docs-raw/html/b_cisco_ucs_manager_cli_administration_mgmt_guide_4-3.html` |
| **File type** | HTML |
| **Fetched on** | 2026-03-19 16:46:40 |

---

## Page 1: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Admin-Management/4-3/b_cisco_ucs_manager_cli_administration_mgmt_guide_4-3.html

![Clear Contents of Search](/etc/designs/cdc/fw/i/ic_clear_gray.png)

---

## Page 2: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Admin-Management/4-3/b_cisco_ucs_manager_cli_administration_mgmt_guide_4-3/m_preface.html

## Audience

This guide is intended primarily for data center administrators with responsibilities and expertise in one or more of the following: 

  * Server administration 

  * Storage administration 

  * Network administration 

  * Network security 


---

## Page 3: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Admin-Management/4-3/b_cisco_ucs_manager_cli_administration_mgmt_guide_4-3/m-new-and-changed-information-cli.html

## New and Changed Information

This section provides information on new features and changed behaviors in Cisco UCS Manager, Release 4.3. 

Table 1. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(5d) Feature |  Description |  Where Documented  
---|---|---  
Enhanced Login Profile settings |  Cisco UCS Manager includes the enhanced the Login Profile settings by allowing administrators to configure user blocking either a global level for all users or individually per user.  |  [Login Profile](m_cli_configuring_role-based_access_control.html#id_100976 "Login Profile Configuration for Cisco UCS Manager")  
Table 2. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(5a) Feature |  Description |  Where Documented  
---|---|---  
Support for Security Management |  Cisco UCS Manager introduces security management and supports AES encryption for enhanced security. | 

  * [Security Management](m-security-management.html#security-management)
  * [Encryption Management](m-security-management.html#security-manamgent)
  * [AES Encryption Management](m-security-management.html#security-management)

  
Support for Cisco UCS C-Series M8 servers |  Cisco UCS Manager now supports Cisco UCS C225 M8 Server.  |  [Intersight Management Mode](m_cli_device_connector.html#Cisco_Concept.dita_f855267a-6ca0-4bb9-a5fd-30d7734a374c)  
Support for Cisco UCS X-Series M8 servers |  Cisco UCS Manager now supports Cisco UCS X215c M8 Compute Node.  |  [Intersight Management Mode](m_cli_device_connector.html#Cisco_Concept.dita_f855267a-6ca0-4bb9-a5fd-30d7734a374c)  
Table 3. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(4b) Feature |  Description |  Where Documented  
---|---|---  
Support for Cisco UCS X-Series Direct |  Cisco UCS Manager now supports Cisco UCS X-Series Direct.  | 

  * [Administration Management Overview](m_administration_management_overview-3_2.html#concept_A90BF0B92ED24B61A3F1832BDD1F50D0)
  * [Password Recovery for the Admin Account](m-cli-password-management.html#concept_g4x_hh5_42b)
  * [Recovering the Admin Account Password in a Non-Cluster Configuration for Cisco UCS Fabric Interconnects 9108 100G](m-cli-password-management.html#recovering-the-admin-account-password-in-a-cluster-configuration-for-cisco-ucs-6400-series-fabric-interconnects)
  * [Recovering the Admin Account Password in a Standalone Configuration for Cisco UCS Fabric Interconnects 9108 100G](m-cli-password-management.html#recovering-the-admin-account-password-in-a-standalone-configuration-for-cisco-ucs-x-series-direct-fabric-interconnect)
  * [Recovering the Admin Account Password in a Cluster Configuration for Cisco UCS Fabric Interconnects 9108 100G](m-cli-password-management.html#recovering-the-admin-account-password-in-a-cluster-configuration-for-cisco-ucs-x-series-direct-fabric-interconnect)

  
Table 4. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(4b) Feature |  Description |  Where Documented  
---|---|---  
Support for Cisco UCS C-Series M8 servers |  Cisco UCS Manager now supports Cisco UCS C245 M8 Servers.  |  [Device Connector](m_cli_device_connector.html#concept_BBBDE52F9AFB484B880F625B14CE6483)  
Table 5. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(4a) Feature |  Description |  Where Documented  
---|---|---  
Support for TLS 1.3 |  Cisco UCS Manager now supports Only TLSv1.3 as allowed SSL protocol for configuring HTTPS communication.  |  [Configuring HTTPS](m_cli_configuring_communication_services.html#task_4330891533622977577)  
Table 6. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(2c) Feature  |  Description  |  Where Documented   
---|---|---  
Support for Cisco UCS X-Series M7 servers |  Cisco UCS Manager now supports Cisco UCS X410c M7 Compute Node.  Cisco UCS X-Series servers support Intelligent Fabric Modules (IFM), which function similarly to the Input/Output Module (IOM) in Cisco UCS B-Series servers.  |  —  
Table 7. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(2b) Feature  |  Description  |  Where Documented   
---|---|---  
Support for Cisco UCS C-Series M7 servers |  Cisco UCS Manager now supports Cisco UCS C220 M7 Server and Cisco UCS C240 M7 Server servers .  |  —  
Support for Cisco UCS X-Series M6 and M7 servers |  Cisco UCS Manager now supports Cisco UCS X210c M6 Compute Node and Cisco UCS X210c M7 Compute Node.  Cisco UCS X-Series servers support Intelligent Fabric Modules (IFM), which function similarly to the Input/Output Module (IOM) in Cisco UCS B-Series servers.  |  —  
Support for IIS Soft Check License |  Cisco UCS Manager now supports IIS Soft Check License for Cisco UCS Manager X-Series and/or Cisco UCS Manager M7 Rack servers. |  [Device Connector](m_cli_device_connector.html#concept_BBBDE52F9AFB484B880F625B14CE6483)  
Deprecated support for Cisco UCS C-Series M4 server. |  Cisco UCS Manager support for Cisco UCS M4 server is deprecated. |  —  
Deprecated support for Cisco UCS 6200 series Fabric Interconnect. |  Cisco UCS Manager support for Cisco UCS 6200 Series Fabric Interconnect is deprecated. |  —

---

## Page 4: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Admin-Management/4-3/b_cisco_ucs_manager_cli_administration_mgmt_guide_4-3/m_administration_management_overview-3_2.html

## Administration Management Overview   
  
Cisco UCS Manager provides a comprehensive set of administration features to effectively manage user access and system configurations in your environment. 

You can configure the mandatory user access features from the Cisco UCS Manager to manage the Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct), Cisco UCS 6500 Series Fabric Interconnect, Cisco UCS 6400 Series Fabric Interconnects,Cisco UCS 6332 40 GB Fabric Interconnects that are in the same domain from one console. 

If your environment is using a UCS 6324 40 GB Mini, you can also manage the user access features using the same Cisco UCS Manager capabilities. 

You can configure the following basic administration configurations to manage user access in your environment: 

  * Passwords—Choose a password during the initial setup for the default admin user account, and create a unique username and password for each user account to access the system. 

  * RBAC—Delegate and control user access privileges according to the role and restrict user access within an organization boundary defined for the tenant, such as multi-tenancy. 

  * Authentication—Create UCS Manager local user accounts, and remote user accounts using the LDAP, RADIUS, and TACACS+ protocols. 

  * Communication Services—Configure CIM XML, HTTP, HTTPS, SMASH CLP, SNMP, SSH, and Telnet to interface third-party applications with Cisco UCS. 

  * Organizations—Create organizations for policies, pools, and service profiles. You can create multiple sub-organizations under the default Root organization, and nest sub-organization under a different sub-organization. 

  * CIMC—Close the KVM, vMedia, and SOL sessions of any user. When UCS Manager receives an event from CIMC, it updates its session table and displays the information to all users. 

  * Backup and Restore —Take a snapshot of all or part of the system configuration and export the file to a location on your network. You can configure a full state, all configuration, system configuration, and logical configuration backup. 

  * Call Home—Configure e-mail alert notifications for UCS errors and faults. You can configure the e-mail notifications for Cisco TAC (predefined) or any other recipient. 

  * Deferred Deployments—Configure deployments for a service profile to deploy immediately or during a specified maintenance window. Use this to control when disruptive configuration changes to a service profile or a service profile template are implemented. 

  * Scheduling—Schedule a one time occurrence for a schedule, a recurring occurrence for a schedule, and delete schedules. 

  * Fault Suppression—Enable fault suppression to suppress SNMP trap and Call Home notifications during a planned maintenance time. 


---

## Page 5: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Admin-Management/4-3/b_cisco_ucs_manager_cli_administration_mgmt_guide_4-3/m-cli-password-management.html

## Guidelines for Cisco UCS Passwords 

Each locally authenticated user account requires a password. A user with admin or aaa privileges can configure Cisco UCS Manager to perform a password strength check on user passwords. Listed in Table 1 are the allowed ASCII characters for UCS passwords. 

Table 1. ASCII Table of Allowed Characters for UCS Passwords ASCII Printable Characters |  Description  
---|---  
A-Z |  uppercase letters A to Z  
a-z |  lowercase letters a to z  
0-9 |  digits 0 to 9  
! |  exclamation mark  
" |  quotation mark  
# |  hash or pound sign  
% |  percent sign  
& |  ampersand  
' |  apostrophe  
( |  left parenthesis  
) |  right parenthesis  
* |  asterisk  
+ |  plus sign  
, |  comma  
- |  hyphen  
. |  period  
/ |  slash  
: |  colon  
; |  semicolon  
< |  less-than  
> |  greater-than  
@ |  at sign  
[ |  left square bracket  
\ |  backslash  
] |  right square bracket  
^ |  caret  
_ |  underscore  
` |  grave accent  
{ |  left curly brace  
| |  vertical bar  
} |  right curly brace  
~ |  tilde  
  
Cisco recommends using a strong password; otherwise, the password strength check for locally authenticated users, Cisco UCS Manager rejects any password that does not meet the following requirements: 

  * If the Password Strength Check option is checked, passwords must be between 8 to 127 characters. 

  * If the Password Strength Check option is unchecked, administrators can create user accounts without a password as a placeholder, but a password containing 1 to 127 characters is required for successful authentication. 

  * Must contain at least three of the following: 

  * Lower case letters 

  * Upper case letters 

  * Digits 

  * Special characters 

  * Must not contain a character that is repeated more than three times consecutively, such as aaabbb. 

  * Must not be identical to the username or the reverse of the username. 

  * Must pass a password dictionary check. For example, the password must not be based on a standard dictionary word. 

  * Must not contain the following symbols: $ (dollar sign), ? (question mark), and = (equals sign). 

  * Should not be blank for local user and admin accounts. 


---

## Page 6: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Admin-Management/4-3/b_cisco_ucs_manager_cli_administration_mgmt_guide_4-3/m-security-management.html

## Security Management

The Cisco UCS Manager 4.3(5a) release introduces the Security Management tab in the Admin section. This section aims to offer multiple security management options to protect sensitive data and ensure network integrity. The tab currently includes Encryption Management and assists administrators in effectively managing security settings. 

---

## Page 7: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Admin-Management/4-3/b_cisco_ucs_manager_cli_administration_mgmt_guide_4-3/m_cli_configuring_role-based_access_control.html

## Role-Based Access Control Overview 

Role-Based Access Control (RBAC) is a method of restricting or authorizing system access for users based on user roles and locales. A role defines the privileges of a user in the system and a locale defines the organizations (domains) that a user is allowed access. Because users are not directly assigned privileges, you can manage individual user privileges by assigning the appropriate roles and locales. 

A user is granted write access to the required system resources only if the assigned role grants the access privileges and the assigned locale allows access. For example, a user with the Server Administrator role in the engineering organization can update server configurations in the Engineering organization. They cannot, however, update server configurations in the Finance organization, unless the locales assigned to the user include the Finance organization. 

---

## Page 8: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Admin-Management/4-3/b_cisco_ucs_manager_cli_administration_mgmt_guide_4-3/m_cli_configuring_authentication.html

##  Authentication Services 

Cisco UCS supports the following two methods to authenticate user logins: 

  * Local user authentication - uses user accounts that exist locally in the Cisco UCS Manager

  * Remote user authentication - uses one of the following protocols: 

  * LDAP 

  * RADIUS 

  * TACACS+ 


---

## Page 9: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Admin-Management/4-3/b_cisco_ucs_manager_cli_administration_mgmt_guide_4-3/m_cli_configuring_call_home.html

##  Call Home in UCS Overview 

Call Home provides an email-based notification for critical system policies. A range of message formats are available for compatibility with pager services or XML-based automated parsing applications. You can use this feature to page a network support engineer, email a Network Operations Center, or use Cisco Smart Call Home services to generate a case with the Technical Assistance Center. 

The Call Home feature can deliver alert messages containing information about diagnostics and environmental faults and events. 

The Call Home feature can deliver alerts to multiple recipients, referred to as Call Home destination profiles. Each profile includes configurable message formats and content categories. A predefined destination profile is provided for sending alerts to the Cisco TAC, but you also can define your own destination profiles. 

When you configure Call Home to send messages, Cisco UCS Manager executes the appropriate CLI show command and attaches the command output to the message. 

Cisco UCS delivers Call Home messages in the following formats: 

  * Short text format which provides a one or two line description of the fault that is suitable for pagers or printed reports. 

  * Full text format which provides fully formatted message with detailed information that is suitable for human reading. 

  * XML machine-readable format that uses Extensible Markup Language (XML) and Adaptive Messaging Language (AML) XML Schema Definition (XSD). The AML XSD is published on the [Cisco.com website](http://www.cisco.com). The XML format enables communication with the Cisco Systems Technical Assistance Center. 


For information about the faults that can trigger Call Home email alerts, see the Cisco UCS Faults and Error Messages Reference. 

The following figure shows the flow of events after a Cisco UCS fault is triggered in a system with Call Home configured: 

Figure 1. Flow of Events after a Fault is Triggered  ![Flowchart showing events that can occur after a fault is triggered in a Cisco UCS domain](/c/dam/en/us/td/i/100001-200000/190001-200000/196001-197000/196367.jpg)

### SMTP Authentication

Beginning with release 4.2(3b), UCS Manager supports secured authentication for the transport email with the SMTP server. 

You can toggle SMTP Authentication between 

  * Off—SMTP Authentication is not used for this Cisco UCS domain. 

  * On—SMTP Authentication is used for this Cisco UCS domain. 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

SMTP server should be capable of supporting STARTTLS, SSL based SMTP communication.  You should also install the server root CA certificate on the SMTP-Client (switch) for succesfull connection between SSL to SMTP-AUTH server. 

* * *  
  
---|---

---

## Page 10: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Admin-Management/4-3/b_cisco_ucs_manager_cli_administration_mgmt_guide_4-3/m_cli_configuring_communication_services.html

## Communication Services   
  
You can use the communication services defined below to interface third-party applications with Cisco UCS. 

Cisco UCS Manager supports IPv4 and IPv6 address access for the following services: 

  * CIM XML 

  * HTTP 

  * HTTPS 

  * SNMP 

  * SSH 

  * Telnet 


Cisco UCS Manager supports out-of-band IPv4 address access to the Cisco UCS KVM Direct launch page from a web browser. To provide this access, you must enable the following service: 

  * CIMC Web Service 

Communication Service  |  Description   
---|---  
CIM XML  |  The Common Information Model (CIM) XML) service is disabled by default and is only available in read-only mode. The default port is 5988. The CIM XML is a standards-based protocol for exchanging CIM information that the Distributed Management Task Force defines.   
CIMC Web Service  |  This service is disabled by default.  When this service is enabled, users can directly access a server CIMC using one of the out-of-band management IP addresses assigned directly to the server, or associated with the server through a service profile.  |  **Note** |  CIMC Web Service can only be enabled or disabled globally. You cannot configure KVM direct access for individual CIMC IP addresses.   
---|---  
HTTP  |  By default, HTTP is enabled on port 80. You can run the Cisco UCS Manager GUI in an HTTP or HTTPS browser. If you select HTTP, all data is exchanged in clear text mode.  For a secure browser session, we recommend that you enable HTTPS and disable HTTP.  By default, Cisco UCS implements a browser redirects to an HTTPS equivalent and recommends that you do not change this behavior.  |  **Note** |  If you are upgrading to Cisco UCS, version 1.4(1), the browser redirect to a secure browser does not occur by default. To redirect the HTTP browser to an HTTPS equivalent, enable the Redirect HTTP to HTTPS in Cisco UCS Manager.   
---|---  
HTTPS  |  By default, HTTPS is enabled on port. With HTTPS, all data is exchanged in encrypted mode through a secure server.  For a secure browser session, We recommend that you only use HTTPS and either disable or redirect HTTP communications.   
SMASH CLP  |  This service is enabled for read-only access and supports a limited subset of the protocols, such as the show command. You cannot disable it.  This shell service is one of the standards that the Distributed Management Task Force defines.   
SNMP  |  By default, this service is disabled. If enabled, the default port is 161. You must configure the community and at least one SNMP trap.  Enable this service only if your system includes integration with an SNMP server.   
SSH  |  This service is enabled on port 22. You cannot disable it, and you cannot change the default port.  This service provides access to the Cisco UCS Manager CLI.   
Telnet  |  By default, this service is disabled.  This service provides access to the Cisco UCS Manager CLI. 

---

## Page 11: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Admin-Management/4-3/b_cisco_ucs_manager_cli_administration_mgmt_guide_4-3/m_cli_cimc_session_management.html

## CIMC Session Management   
  
You can view and close any KVM, vMedia, and SOL sessions in Cisco UCS Manager. If you have administrator privileges, you can discontinue the KVM, vMedia, and SoL sessions of any user. . Cisco Integrated Management Controller (CIMC) provides session information to Cisco UCS Manager. When Cisco UCS Manager gets an event from CIMC, it updates its session table and displays the information to all users. 

The session information consists of the following information: 

  * Name—The name of the user who launched the session. 

  * Session ID—The ID associated with the session. The format of the session ID for blades is [unique identifier] _ [chassis id] _ [Blade id]. The format of the session ID for racks is [unique identifier] _ 0 _ [Rack id]. 

  * Type of session—KVM, vMedia, or SoL. 

  * Privilege level of the user—Read-Write, Read Only, or Granted. 

  * Administrative state—Active or Inactive. The value is active if the session is active. The value is inactive if the session terminate command has been issued but the session has not been terminated. This situation occurs when FSM of the server is in progress with another operation or when the connectivity to CIMC is lost. 

  * Source Address—The IP address of the computer from which the session was opened. 

  * Service Profile—The service profile associated with the session. The service profile attribute value for a CIMC session is displayed only if the session is opened on an IP address that is provided from the service profile. 

  * Server—The name of the server associated with the session. 

  * Login time—The date and time the session started. 

  * Last Update Time—The last time the session information was updated by CIMC. 


A new session is generally added when a user connects to KVM, vMedia, or SOL. A Pnuos vMedia session will be displayed in the session table during the server discovery with the user name __vmediausr__. 

The CIMC session data is available under the CIMC Sessions tab in Cisco UCS Manager GUI. Any CIMC session terminated by the user is audit logged with proper details. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

To perform the GUI and CLI tasks that are described in this guide, a CIMC image version of 2.1(2a) or above is required for the session management support for the blade servers. The latest CIMC image version of 1.5(1l) and above is required for the rack-servers. 

* * *  
  
---|---  
  
### Viewing the CIMC Sessions Opened by the Local Users

Follow this task to view all the CIMC sessions opened by the local users or the CIMC sessions opened by a specific local user.  ![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Viewing CIMC sessions of a specific server or a service-profile option is not present in CLI. It is available in GUI. 

* * *  
  
---|---  
  
#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A # scope security |  Enters security configuration mode.  
**Step 2** |  UCS-A /security # show cimc-sessions local |  Displays all CIMC sessions opened by the local users.  
**Step 3** |  UCS-A /security # show cimc-sessions local user-name |  Displays all CIMC sessions opened by a specific local user.  
  
#### Example

The following examples show how to view:

  * All CIMC sessions opened by local users 

  * CIMC session opened by a specific local user

  * Details of the CIMC session opened by a specific local user.


    
    
    **All sessions opened by local users** :
    UCS-A # **scope security**
    UCS-A /security # **show cimc-sessions local**
    
    Session ID   Type     User      Source Addr     Admin State
    ----------   ------ --------- --------------- ------------
    42_1_1       Kvm      admin     10.106.22.117     Active
    4_1_5        Kvm      admin     10.106.22.117     Active
    5_1_5        Vmedia   admin     10.106.22.117     Active
    
    **Session opened by a specific local user** :
    UCS-A /security # **show cimc-sessions local admin**
    Session ID   Type     User      Source Addr     Admin State
    ----------   ------ --------- --------------- ------------
    42_1_1       Kvm      admin     10.106.22.117     Active
    
    **Details of session opened by a specific local user** :
    UCS-A /security # **show cimc-sessions local admin detail**
    Session ID 42_1_1
       Type: Kvm
       User: admin
       Source Addr: 10.106.22.117
       Login Time: 2013-06-28T06:09:53.000
    			Last Updated Time: 2013-06-28T06:21:52.000
       Admin State: Active
       Priv: RW
       Server: sys/chassis-1/blade-1
    			Service Profile: 
    
    

### Viewing the CIMC Sessions Opened by the Remote Users

Follow this task to view all the CIMC sessions opened by the remote users or the CIMC sessions opened by a specific remote user. 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A # scope security |  Enters security configuration mode.  
**Step 2** |  UCS-A /security # show cimc-sessions remote |  Displays all CIMC sessions opened by the remote users.  
**Step 3** |  UCS-A /security # show cimc-sessions remote user-name |  Displays all CIMC sessions opened by a specific remote user.  
  
#### Example

The following examples show how to view:

  * All CIMC sessions opened by remote users 

  * CIMC session opened by a specific remote user

  * Details of the CIMC session opened by a specific remote user.


    
    
    **All sessions opened by remote users** :
    UCS-A # **scope security**
    UCS-A /security # **show cimc-sessions remote**
    
    Session ID   Type     User             Source Addr      Admin State
    ----------   ------ ---------        ---------------   ------------
    43_1_1       Kvm     administrator     10.106.22.117     Active
    6_1_5        Kvm     test-remote       10.106.22.117     Active
    7_1_5        Vmedia  test-remote       10.106.22.117     Active
    
    **Session opened by a specific remote user** :
    UCS-A /security # **show cimc-sessions remote administrator**
    
    Session ID   Type     User             Source Addr      Admin State
    ----------   ------ ---------        ---------------   ------------
    43_1_1       Kvm     administrator     10.106.22.117     Active
    
    **Details of session opened by a specific remote user** :
    UCS-A /security # **show cimc-sessions remote administrator detail**
    Session ID 43_1_1
       Type: Kvm
       User: administrator
       Source Addr: 10.106.22.117
       Login Time: 2013-06-28T06:09:53.000
       Last Updated Time: 2013-06-28T06:21:52.000   
       Admin State: Active
       Priv: RW
       Server: sys/chassis-1/blade-1
    			Service Profile: 
    
    

### Viewing the CIMC Sessions Opened by an IPMI User

To view the CIMC sessions opened by an IPMI user, complete the following steps: 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A #  scope org  org-name |  Enters the root organization mode.  
**Step 2** |  UCS-A /org # scope ipmi-access-profile  profile-name |  Enters the IPMI access profile name.  
**Step 3** |  UCS-A /org/ipmi-access-profile #  scope ipmi-user user-name |  Enters an IPMI user name.  
**Step 4** |  UCS-A /org/ipmi-access-profile/ipmi-user #  show cimc-sessions  |  Displays all CIMC sessions opened by the specified IPMI User.  
  
#### Example

The following example shows how to view all the CIMC sessions opened by an IPMI user:
    
    
    UCS-A # **scope org Finance**
    UCS-A /org* # **scope ipmi-access-profile ReadOnly**
    UCS-A /org/ipmi-access-profile* # **scope ipmi-user alice**
    UCS-A /org/ipmi-access-profile/ipmi-user # **show cimc-sessions**
    
    Session ID    Type    User        Source Addr       Admin State
    ----------   ------  ---------   ---------------   --------------
    45_1_1        sol     alice       10.106.22.117     Active
    
    

### Clearing the CIMC Sessions of a Server

This task shows how to clear all CIMC sessions opened on a server. You can also clear the CIMC sessions on a server based on the session type and the user name. 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A # scope security |  Enters security configuration mode.  
**Step 2** |  UCS-A /security #  terminate cimc-sessions server  chassis-id/blade-id |  Clears the CIMC sessions on a specific blade server of a chassis.   
**Step 3** |  UCS-A /security #  terminate cimc-sessions server  Rack-server-id |  Clears the CIMC sessions on a specific rack server.  
**Step 4** |  UCS-A /security #  terminate cimc-sessions server  server-id type session-type |  Clears the CIMC sessions of a specific type on a server.  
**Step 5** |  UCS-A /security #  terminate cimc-sessions server  server-id user-name user-name |  Clears the CIMC sessions of a specific user on a server.  
  
#### Example

The first example shows how to clear all CIMC sessions on a server. The second example shows how to clear the CIMC sessions of a specific type on a server. The third example shows how to clear the CIMC sessions of a specific user on a server: 
    
    
    UCS-A /security # **scope security**
    UCS-A /security # **terminate cimc-sessions server 2/1**
    This will close KVM sessions. Are you sure? (yes/no):**yes**
    UCS-A /security
    
    UCS-A # **scope security**
    UCS-A /security # **terminate cimc-sessions server 2/1 type kvm**
    This will close KVM sessions. Are you sure? (yes/no):**yes**
    
    UCS-A # **scope security**
    UCS-A /security # **terminate cimc-sessions server 2/1 user-name test-user**
    This will close KVM sessions. Are you sure? (yes/no):**yes**
    

### Clearing the CIMC Sessions of a Modular Server 

This task shows how to clear all CIMC sessions opened on a server. You can also clear the CIMC sessions on a server based on the session type and the user name. 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A # scope security |  Enters security configuration mode.   
**Step 2** |  UCS-A /security #  terminate cimc-sessions server  chassis-id / cartridge-id / server-id |  Clears the CIMC sessions on a specific modular server of a cartridge on a chassis.   
**Step 3** |  UCS-A /security #  terminate cimc-sessions server  chassis-id / cartridge-id / server-id type session-type |  Clears the CIMC sessions of a specific type on a server.   
**Step 4** |  UCS-A /security #  terminate cimc-sessions server  chassis-id / cartridge-id / server-id user-name user-name |  Clears the CIMC sessions of a specific user on a server.   
  
#### Example

The first example shows how to clear all CIMC sessions on a server. The second example shows how to clear the CIMC sessions of a specific type on a server. The third example shows how to clear the CIMC sessions of a specific user on a server: 
    
    
    UCS-A /security # **scope security**
    UCS-A /security # **terminate cimc-sessions server 1/2/1**
    This will close cimc sessions. Are you sure? (yes/no):**yes**
    UCS-A /security
    
    UCS-A # **scope security**
    UCS-A /security # **terminate cimc-sessions server 1/2/1 type kvm**
    This will close KVM sessions. Are you sure? (yes/no):**yes**
    
    UCS-A # **scope security**
    UCS-A /security # **terminate cimc-sessions server 1/2/1 user-name test-user**
    This will close cimc sessions. Are you sure? (yes/no):**yes**
    

### Clearing All CIMC Sessions Opened by a Local User

This task shows how to clear the sessions opened by a local user.

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A # scope security |  Enters security configuration mode.  
**Step 2** |  UCS-A /security #  terminate cimc-sessions local-user user-name |  Clears all CIMC sessions opened by a local user.  
**Step 3** |  UCS-A /security #  terminate cimc-sessions local-user user-name type {kvm | vmedia sol | all}  |  Clears all CIMC sessions of specific session type opened by a local user.  
  
#### Example

The following example shows how to clear the CIMC sessions opened by a local user:
    
    
    UCS-A /security# **scope security**
    UCS-A /security# **terminate cimc-sessions local-user testuser**
    This will close cimc sessions. Are you sure? (yes/no):**yes**
    UCS-A /security#
    
    

### Clearing All CIMC Sessions Opened by a Remote User 

This task shows how to clear CIMC sessions opened by a remote user. 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A # scope security |  Enters security configuration mode.  
**Step 2** |  UCS-A /security #  terminate cimc-sessions remote-user  user-name |  Clears all CIMC sessions opened by a remote user.  
**Step 3** |  UCS-A /security #  terminate cimc-sessions remote-user user-name type {kvm | vmedia sol | all}  |  Clears all CIMC sessions of specific session type opened by a remote user.  
  
#### Example

The following example shows how to clear all CIMC sessions opened by a remote user:
    
    
    UCS-A /security# **scope security**
    UCS-A /security# **terminate cimc-sessions remote-user testuser**
    This will close cimc sessions. Are you sure? (yes/no):**yes**
    UCS-A /security#
    
    

### Clearing a Specific CIMC Session Opened by a Local User 

This task shows how to clear a specific CIMC session opened by a local user.

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A # scope security |  Enters security configuration mode.  
**Step 2** |  UCS-A /security # scope local-user user-name |  Enters local user mode.  
**Step 3** |  UCS-A /security/local user # terminate cimc-session session-id |  Clears the chosen CIMC session.  
**Step 4** |  UCS-A /security/local user* # commit-buffer |  Commits the transaction.  
  
#### Example

The following example shows how to clear a specific CIMC session opened by a local user and commits the transaction:
    
    
    UCS-A /security# **scope security**
    UCS-A /security# **scope local-user admin**
    UCS-A /security/local user # **terminate cimc-session 6_1_2**
    UCS-A /security/local user*# **commit-buffer**
    UCS-A /security/local user#
    
    

### Clearing a Specific CIMC Session Opened by a Remote User 

This task shows how to clear a specific CIMC session opened by a remote user.

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A # scope security |  Enters security configuration mode.  
**Step 2** |  UCS-A /security # scope remote -user user-name |  Enters remote user mode.   
**Step 3** |  UCS-A /security/remote user # terminate cimc-session session-id |  Clears the chosen CIMC session.  
**Step 4** |  UCS-A /security/remote user* # commit-buffer |  Commits the transaction.  
  
#### Example

The following example shows how to clear a specific CIMC session opened by a remote user and commits the transaction: 
    
    
    UCS-A /security# **scope security**
    UCS-A /security# **scope remote-user admin**
    UCS-A /security/remote user # **terminate cimc-session 6_1_3**
    UCS-A /security/remote user*# **commit-buffer**
    UCS-A /security/remote user#
    
    

### Clearing a CIMC Session Opened by an IPMI User

To clear a CIMC session opened by an IPMI user, complete the following steps: 

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A #  scope org  org-name |  Enters the root organization mode.  
**Step 2** |  UCS-A /org # scope ipmi-access-profile  profile-name |  Enters the IPMI access profile name.  
**Step 3** |  UCS-A /org/ipmi-access-profile # scope ipmi-user  user-name |  Enters the IPMI user.  
**Step 4** |  UCS-A /org/ipmi-access-profile/ipmi-user #  terminate cimc-sessions session-id |  Terminates a specific CIMC session opened by an IPMI user.  
**Step 5** |  UCS-A /org/ipmi-access-profile/ipmi-user * commit-buffer  |  Commits the changes.  
  
#### Example

The following example displays how to clear a specific CIMC session opened by an IPMI user and commits the changes:
    
    
    UCS-A # **scope org Finance**
    UCS-A /org* # **scope ipmi-access-profile ReadOnly**
    UCS-A /org/ipmi-access-profile* # **scope ipmi-user alice**
    UCS-A /org/ipmi-access-profile/ipmi-user # **terminate cimc-sessions 5_1_2**
    UCS-A /org/ipmi-access-profile/ipmi-user* # **commit-buffer**
    
    

---

## Page 12: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Admin-Management/4-3/b_cisco_ucs_manager_cli_administration_mgmt_guide_4-3/m_m_series_cli_setting_the_cimc_ip_address.html

## Management IP Address 

Each server in a Cisco UCS domain must have a one or more management IP addresses assigned to its Cisco Integrated Management Controller (CIMC) or to the service profile associated with the server. Cisco UCS Manager uses these IP addresses for external access that terminates in the CIMC. This external access can be through one of the following services: 

  * KVM console 

  * Serial over LAN 

  * An IPMI tool 


The management IP addresses used to access the CIMC on a server can be out-of-band (OOB) addresses, through which traffic traverses the fabric interconnect via the management port, or inband addresses, through which traffic traverses the fabric interconnect via the fabric uplink port. Up to six IP addresses can be configured to access the CIMC on a server, two out-of-band (OOB) and four inband. 

You can configure the following management IP addresses: 

  * A static OOB IPv4 address assigned directly to the server 

  * An OOB IPv4 address assigned to the server from a global ext-mgmt pool 

  * An inband IPv4 address derived from a service profile associated with the server 

  * An inband IPv4 address drawn from a management IP pool and assigned to a service profile or service profile template 

  * An static inband IPv6 address assigned directly to the server 

  * An inband IPv6 address derived from a service profile associated with the server 


You can assign multiple management IP addresses to each CIMC on the server and to the service profile associated with the server. If you do so, you must use different IP addresses for each of them. 

A management IP address that is assigned to a service profile moves with that service profile. If KVM or SoL sessions are active when you migrate the service profile to another server, Cisco UCS Manager terminates the sessions and does not restart them after the migration is completed. You configure the IP address when you create or modify a service profile. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

You cannot assign a static IP address to a server or service profile if that IP address has already been assigned to a server or service profile in the Cisco UCS domain. If you attempt to do so, Cisco UCS Manager warns you that the IP address is already in use and rejects the configuration. 

* * *  
  
---|---  
  
A unicast Internet Control Message Protocol (ICMP) request will be sent to the gateway IP address every second from each server that is configured with an inband IP address. This request is to check if connectivity for the inband traffic through the current Fabric Interconnect (FI) is up, and to initiate a failover to the other FI if it is down. The path selected for inband and the failover operations are completely independent of the server data traffic. The default polling interval is 1 second and the polling interval is configurable to a maximum of 5 seconds. After three failed polls, the CIMC will failover to the other FI. During failover, the CIMC will issue a Gratuitous Address Resolution Protocol (GARP) on the newly selected uplinks to notify the network that the MAC has been moved to a new location. 

---

## Page 13: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Admin-Management/4-3/b_cisco_ucs_manager_cli_administration_mgmt_guide_4-3/m_cli_configuring_organizations.html

## Organizations in a Multitenancy Environment 

Multi-tenancy allows you to divide the large physical infrastructure of an Cisco UCS domain into logical entities known as organizations. As a result, you can achieve a logical isolation between organizations without providing a dedicated physical infrastructure for each organization. 

You can assign unique resources to each tenant through the related organization in the multi-tenant environment. These resources can include different policies, pools, and quality of service definitions. You can also implement locales to assign or restrict user privileges and roles by organization, if you do not want all users to have access to all organizations. 

If you set up a multi-tenant environment, all organizations are hierarchical. The top-level organization is always root. The policies and pools that you create in root are system-wide and are available to all organizations in the system. However, any policies and pools created in other organizations are only available to organizations that are above it in the same hierarchy. For example, if a system has organizations named Finance and HR that are not in the same hierarchy, Finance cannot use any policies in the HR organization, and HR cannot access any policies in the Finance organization. However, both Finance and HR can use policies and pools in the root organization. 

If you create organizations in a multi-tenant environment, you can also set up one or more of the following for each organization or for a sub-organization in the same hierarchy: 

  * Resource pools 

  * Policies 

  * Service profiles 

  * Service profile templates 


The root organization is always the top level organization. 

---

## Page 14: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Admin-Management/4-3/b_cisco_ucs_manager_cli_administration_mgmt_guide_4-3/m_cli_backing_up_and_restoring_the_configuration.html

## Backup Operations in UCS 

When you perform a backup through Cisco UCS Manager, you take a snapshot of all or part of the system configuration and export the file to a location on your network. You cannot use Cisco UCS Manager to back up data on the servers. 

You can perform a backup while the system is up and running. The backup operation only saves information from the management plane. It does not have any impact on the server or network traffic. 

---

## Page 15: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Admin-Management/4-3/b_cisco_ucs_manager_cli_administration_mgmt_guide_4-3/m_cli_scheduling_options.html

## Creating a Schedule 

### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope system |  Enters system mode.   
**Step 2** |  UCS-A /system #  create scheduler ` ` sched-name |  Creates a scheduler and enters scheduler mode.   
**Step 3** |  UCS-A /system/scheduler #  commit-buffer |  Commits the transaction to the system configuration.   
  
### Example

The following example creates a scheduler named maintenancesched and commits the transaction: 
    
    
    UCS-A# **scope system**
    UCS-A /system # **create scheduler maintenancesched**
    UCS-A /system/scheduler* # **commit-buffer**
    UCS-A /system/scheduler #

### What to do next

Create a one time occurrence or recurring occurrence for the schedule. 

---

## Page 16: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Admin-Management/4-3/b_cisco_ucs_manager_cli_administration_mgmt_guide_4-3/m_cli_deferring_deployment_of_service_profile_updates.html

## Service Profile Deferred Deployments 

Some modifications to a service profile or to an updating service profile template can be disruptive and require a reboot of the server. You can, however, configure deferred deployment to control when those disruptive configuration changes are implemented. For example, you can choose to deploy the service profile changes immediately or have them deployed during a specified maintenance window. You can also choose whether or not a service profile deployment requires explicit user acknowledgment. 

Deferred deployment is available for all configuration changes that occur through the association of a service profile with a server. These configuration changes can be prompted by a change to a service profile, to a policy that is included in a service profile, or to an updating service profile template. For example, you can defer the upgrade and activation of firmware through host firmware packages and management firmware packages, such as server BIOS, RAID controller, host HBA, and network adapters. However, you cannot defer the direct deployment of firmware images for components that do not use either of the firmware packages, such as Cisco UCS Manager, fabric interconnects, I/O modules, and FI-IO modules.. 

Deferred deployment is not available for the following actions which require the reboot of a server: 

  * Initial association of a service profile with a server 

  * Final disassociation of a service profile from a server, without associating the service profile with a different server 

  * Decommissioning a server 

  * Re-acknowledging a server 

  * Resetting a server 


If you want to defer the deployment of service profile changes, you must configure one or more maintenance policies and configure each service profile with a maintenance policy. If you want to define the time period when the deployment should occur, you also need to create at least one schedule with one or more recurring occurrences or one time occurrences, and include that schedule in a maintenance policy. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The Cisco UCS X-Series Direct does not support I/O Module operations; it utilizes the FI-I/O Module instead.

* * *  
  
---|---  
  
###  Schedules for Deferred Deployments 

A schedule contains a set of occurrences. These occurrences can be one time only or can recur at a specified time and day each week. The options defined in the occurrence, such as the duration of the occurrence or the maximum number of tasks to be run, determine whether a service profile change is deployed. For example, if a change cannot be deployed during a given maintenance window because the maximum duration or number of tasks was reached, that deployment is carried over to the next maintenance window. 

Each schedule checks periodically to see whether the Cisco UCS domain entered one or more maintenance windows. If so, the schedule executes the deployments that are eligible according to the constraints specified in the maintenance policy. 

A schedule contains one or more occurrences, which determine the maintenance windows associated with that schedule. An occurrence can be one of the following: 

One Time Occurrence 
    

One time occurrences define a single maintenance window. These windows continue until the maximum duration of the window or the maximum number of tasks that can be run in the window is reached. 

Recurring Occurrence 
    

Recurring occurrences define a series of maintenance windows. These windows continue until the maximum number of tasks or the end of the day specified in the occurrence was reached. 

###  Pending Activities for Deferred Deployments 

If you configure a deferred deployment in a Cisco UCS domain, Cisco UCS Manager enables you to view all pending activities. You can see activities that are waiting for user acknowledgement and those that are scheduled. 

If a Cisco UCS domain has pending activities, Cisco UCS Manager GUI notifies users with admin privileges when they log in. 

Cisco UCS Manager displays information about all pending activities, including the following: 

  * Name of the service profile to deploy and associate with a server 

  * Server affected by the deployment 

  * Disruption caused by the deployment 

  * Change performed by the deployment 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

You cannot specify the maintenance window in which a specific pending activity is applied to the server. The maintenance window depends upon how many activities are pending and which maintenance policy is assigned to the service profile. However, any user with admin privileges can manually initiate a pending activity and reboot the server immediately, whether it is waiting for user acknowledgment or for a maintenance window. 

* * *  
  
---|---  
  
### Guidelines and Limitations for Deferred Deployments 

#### Service Profile Association Changes and Maintenance Policy Options

When changing service profile association, the following maintenance policy options can affect how the changes are applied: 

  * If the On Next Boot and User Ack options are enabled in a maintenance policy, the service profile association change displays a warning that an acknowledgement is required. However, association will happen immediately. 

  * If the On Next Boot and User Ack options are not enabled in a maintenance policy, the service profile association change displays a warning that an acknowledgement is required, and will remain pending until acknowledged. 


#### Cannot Undo All Changes to Service Profiles or Service Profile Templates 

If you cancel a pending change, Cisco UCS Manager attempts to roll back the change without rebooting the server. However, for complex changes, Cisco UCS Manager may have to reboot the server a second time to roll back the change. For example, if you delete a vNIC, Cisco UCS Manager reboots the server according to the maintenance policy included in the service profile. You cannot cancel this reboot and change, even if you restore the original vNIC in the service profile. Instead, Cisco UCS Manager schedules a second deployment and reboot of the server. 

#### Association of Service Profile Can Exceed Boundaries of Maintenance Window 

After Cisco UCS Manager begins the association of the service profile, the scheduler and maintenance policy do not have any control over the procedure. If the service profile association does not complete within the allotted maintenance window, the process continues until it is completed. For example, this can occur if the association does not complete in time because of retried stages or other issues. 

#### Cannot Specify Order of Pending Activities 

Scheduled deployments run in parallel and independently. You cannot specify the order in which the deployments occur. You also cannot make the deployment of one service profile change dependent upon the completion of another. 

#### Cannot Perform Partial Deployment of Pending Activity 

Cisco UCS Manager applies all changes made to a service profile in the scheduled maintenance window. You cannot make several changes to a service profile at the same time and then have those changes be spread across several maintenance windows. When Cisco UCS Manager deploys the service profile changes, it updates the service profile to match the most recent configuration in the database. 

---

## Page 17: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Admin-Management/4-3/b_cisco_ucs_manager_cli_administration_mgmt_guide_4-3/m_cli_ucs_fault_suppression.html

## Global Fault Policy 

The global fault policy controls the lifecycle of a fault in a Cisco UCS domain, including when faults are cleared, the flapping interval (the length of time between the fault being raised and the condition being cleared), and the retention interval (the length of time a fault is retained in the system). 

A fault in Cisco UCS has the following lifecycle: 

  1. A condition occurs in the system and Cisco UCS Manager raises a fault. This is the active state. 

  2. When the fault is alleviated, it enters a flapping or soaking interval that is designed to prevent flapping. Flapping occurs when a fault is raised and cleared several times in rapid succession. During the flapping interval, the fault retains its severity for the length of time specified in the global fault policy. 

  3. If the condition reoccurs during the flapping interval, the fault returns to the active state. If the condition does not reoccur during the flapping interval, the fault is cleared. 

  4. The cleared fault enters the retention interval. This interval ensures that the fault reaches the attention of an administrator even if the condition that caused the fault has been alleviated and the fault has not been deleted prematurely. The retention interval retains the cleared fault for the length of time specified in the global fault policy. 

  5. If the condition reoccurs during the retention interval, the fault returns to the active state. If the condition does not reoccur, the fault is deleted. 


---

## Page 18: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Admin-Management/4-3/b_cisco_ucs_manager_cli_administration_mgmt_guide_4-3/m_cli_device_connector.html

## Intersight Management Mode

Cisco Intersight™ is a management platform delivered as a service with embedded analytics for your Cisco and 3rd party IT infrastructure. Intersight Managed Mode (IMM) is a new architecture that manages the UCS Fabric Interconnected systems through a Redfish-based standard model. Intersight Managed Mode unifies the capabilities of the UCS Systems and the cloud-based flexibility of Intersight, thus unifying the management experience for the standalone and Fabric Interconnect attached systems. Intersight Management Model standardizes policy and operation management for Cisco UCS 6600 Series Fabric Interconnect, UCSX-S9108-100G, UCS-FI-6454, UCS-FI-64108, UCS-FI-6536 and Cisco UCS B-Series (M5, M6), Cisco UCS C-Series (M5, M6, M7,M8), and Cisco UCS X-Series (M6 ,M7 ,M8) servers. 

You can choose between the native UCSM Managed Mode (UMM) or Intersight Managed Mode (IMM) for the Fabric attached UCS Systems during initial setup of the Fabric Interconnects. If you choose to switch back between UMM and IMM, you must erase the present configuration and start from initial setup. Before erasing the configuration, you must ensure to unclaim the device from Intersight and decommission all rack servers. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For more information, see <https://intersight.com/help/resources#intersight_managed_mode>. 

* * *  
  
---|---  
  
Cisco Intersight Managed Mode (IMM) transition tool helps bootstrap new IMM deployments by replicating the configuration attributes of the existing Cisco UCS Manager (UCSM) infrastructure and by converting the existing Service Profile Templates to IMM Server Profile Templates to accelerate deployment of new servers in IMM. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For more information, see the latest Cisco Intersight Managed Mode Transition Tool User Guide: [https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_cisco_intersight_managed_mode_transition_tool_user_guide.pdf](https://www.cisco.com/c/en/us/support/servers-unified-computing/intersight/products-installation-guides-list.html)

* * *  
  
---|---

---

## Page 19: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Admin-Management/4-3/m_cli_configuring_role-based_access_control.html

## Role-Based Access Control Overview   
  
Role-Based Access Control (RBAC) is a method of restricting or authorizing system access for users based on user roles and locales. A role defines the privileges of a user in the system and a locale defines the organizations (domains) that a user is allowed access. Because users are not directly assigned privileges, you can manage individual user privileges by assigning the appropriate roles and locales. 

A user is granted write access to the required system resources only if the assigned role grants the access privileges and the assigned locale allows access. For example, a user with the Server Administrator role in the engineering organization can update server configurations in the Engineering organization. They cannot, however, update server configurations in the Finance organization, unless the locales assigned to the user include the Finance organization. 

---

## Page 20: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Admin-Management/4-3/m-security-management.html

## Security Management

The Cisco UCS Manager 4.3(5a) release introduces the Security Management tab in the Admin section. This section aims to offer multiple security management options to protect sensitive data and ensure network integrity. The tab currently includes Encryption Management and assists administrators in effectively managing security settings. 

---

## Page 21: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Admin-Management/4-3/m_cli_device_connector.html

## Intersight Management Mode

Cisco Intersight™ is a management platform delivered as a service with embedded analytics for your Cisco and 3rd party IT infrastructure. Intersight Managed Mode (IMM) is a new architecture that manages the UCS Fabric Interconnected systems through a Redfish-based standard model. Intersight Managed Mode unifies the capabilities of the UCS Systems and the cloud-based flexibility of Intersight, thus unifying the management experience for the standalone and Fabric Interconnect attached systems. Intersight Management Model standardizes policy and operation management for Cisco UCS 6600 Series Fabric Interconnect, UCSX-S9108-100G, UCS-FI-6454, UCS-FI-64108, UCS-FI-6536 and Cisco UCS B-Series (M5, M6), Cisco UCS C-Series (M5, M6, M7,M8), and Cisco UCS X-Series (M6 ,M7 ,M8) servers. 

You can choose between the native UCSM Managed Mode (UMM) or Intersight Managed Mode (IMM) for the Fabric attached UCS Systems during initial setup of the Fabric Interconnects. If you choose to switch back between UMM and IMM, you must erase the present configuration and start from initial setup. Before erasing the configuration, you must ensure to unclaim the device from Intersight and decommission all rack servers. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For more information, see <https://intersight.com/help/resources#intersight_managed_mode>. 

* * *  
  
---|---  
  
Cisco Intersight Managed Mode (IMM) transition tool helps bootstrap new IMM deployments by replicating the configuration attributes of the existing Cisco UCS Manager (UCSM) infrastructure and by converting the existing Service Profile Templates to IMM Server Profile Templates to accelerate deployment of new servers in IMM. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For more information, see the latest Cisco Intersight Managed Mode Transition Tool User Guide: [https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_cisco_intersight_managed_mode_transition_tool_user_guide.pdf](https://www.cisco.com/c/en/us/support/servers-unified-computing/intersight/products-installation-guides-list.html)

* * *  
  
---|---

---

## Page 22: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Admin-Management/4-3/m_administration_management_overview-3_2.html

## Administration Management Overview   
  
Cisco UCS Manager provides a comprehensive set of administration features to effectively manage user access and system configurations in your environment. 

You can configure the mandatory user access features from the Cisco UCS Manager to manage the Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct), Cisco UCS 6500 Series Fabric Interconnect, Cisco UCS 6400 Series Fabric Interconnects,Cisco UCS 6332 40 GB Fabric Interconnects that are in the same domain from one console. 

If your environment is using a UCS 6324 40 GB Mini, you can also manage the user access features using the same Cisco UCS Manager capabilities. 

You can configure the following basic administration configurations to manage user access in your environment: 

  * Passwords—Choose a password during the initial setup for the default admin user account, and create a unique username and password for each user account to access the system. 

  * RBAC—Delegate and control user access privileges according to the role and restrict user access within an organization boundary defined for the tenant, such as multi-tenancy. 

  * Authentication—Create UCS Manager local user accounts, and remote user accounts using the LDAP, RADIUS, and TACACS+ protocols. 

  * Communication Services—Configure CIM XML, HTTP, HTTPS, SMASH CLP, SNMP, SSH, and Telnet to interface third-party applications with Cisco UCS. 

  * Organizations—Create organizations for policies, pools, and service profiles. You can create multiple sub-organizations under the default Root organization, and nest sub-organization under a different sub-organization. 

  * CIMC—Close the KVM, vMedia, and SOL sessions of any user. When UCS Manager receives an event from CIMC, it updates its session table and displays the information to all users. 

  * Backup and Restore —Take a snapshot of all or part of the system configuration and export the file to a location on your network. You can configure a full state, all configuration, system configuration, and logical configuration backup. 

  * Call Home—Configure e-mail alert notifications for UCS errors and faults. You can configure the e-mail notifications for Cisco TAC (predefined) or any other recipient. 

  * Deferred Deployments—Configure deployments for a service profile to deploy immediately or during a specified maintenance window. Use this to control when disruptive configuration changes to a service profile or a service profile template are implemented. 

  * Scheduling—Schedule a one time occurrence for a schedule, a recurring occurrence for a schedule, and delete schedules. 

  * Fault Suppression—Enable fault suppression to suppress SNMP trap and Call Home notifications during a planned maintenance time. 


---

## Page 23: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Admin-Management/4-3/m-cli-password-management.html

## Guidelines for Cisco UCS Passwords 

Each locally authenticated user account requires a password. A user with admin or aaa privileges can configure Cisco UCS Manager to perform a password strength check on user passwords. Listed in Table 1 are the allowed ASCII characters for UCS passwords. 

Table 1. ASCII Table of Allowed Characters for UCS Passwords ASCII Printable Characters |  Description  
---|---  
A-Z |  uppercase letters A to Z  
a-z |  lowercase letters a to z  
0-9 |  digits 0 to 9  
! |  exclamation mark  
" |  quotation mark  
# |  hash or pound sign  
% |  percent sign  
& |  ampersand  
' |  apostrophe  
( |  left parenthesis  
) |  right parenthesis  
* |  asterisk  
+ |  plus sign  
, |  comma  
- |  hyphen  
. |  period  
/ |  slash  
: |  colon  
; |  semicolon  
< |  less-than  
> |  greater-than  
@ |  at sign  
[ |  left square bracket  
\ |  backslash  
] |  right square bracket  
^ |  caret  
_ |  underscore  
` |  grave accent  
{ |  left curly brace  
| |  vertical bar  
} |  right curly brace  
~ |  tilde  
  
Cisco recommends using a strong password; otherwise, the password strength check for locally authenticated users, Cisco UCS Manager rejects any password that does not meet the following requirements: 

  * If the Password Strength Check option is checked, passwords must be between 8 to 127 characters. 

  * If the Password Strength Check option is unchecked, administrators can create user accounts without a password as a placeholder, but a password containing 1 to 127 characters is required for successful authentication. 

  * Must contain at least three of the following: 

  * Lower case letters 

  * Upper case letters 

  * Digits 

  * Special characters 

  * Must not contain a character that is repeated more than three times consecutively, such as aaabbb. 

  * Must not be identical to the username or the reverse of the username. 

  * Must pass a password dictionary check. For example, the password must not be based on a standard dictionary word. 

  * Must not contain the following symbols: $ (dollar sign), ? (question mark), and = (equals sign). 

  * Should not be blank for local user and admin accounts. 


---

## Page 24: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Admin-Management/4-3/m_cli_configuring_communication_services.html

## Communication Services 

You can use the communication services defined below to interface third-party applications with Cisco UCS. 

Cisco UCS Manager supports IPv4 and IPv6 address access for the following services: 

  * CIM XML 

  * HTTP 

  * HTTPS 

  * SNMP 

  * SSH 

  * Telnet 


Cisco UCS Manager supports out-of-band IPv4 address access to the Cisco UCS KVM Direct launch page from a web browser. To provide this access, you must enable the following service: 

  * CIMC Web Service 

Communication Service  |  Description   
---|---  
CIM XML  |  The Common Information Model (CIM) XML) service is disabled by default and is only available in read-only mode. The default port is 5988. The CIM XML is a standards-based protocol for exchanging CIM information that the Distributed Management Task Force defines.   
CIMC Web Service  |  This service is disabled by default.  When this service is enabled, users can directly access a server CIMC using one of the out-of-band management IP addresses assigned directly to the server, or associated with the server through a service profile.  |  **Note** |  CIMC Web Service can only be enabled or disabled globally. You cannot configure KVM direct access for individual CIMC IP addresses.   
---|---  
HTTP  |  By default, HTTP is enabled on port 80. You can run the Cisco UCS Manager GUI in an HTTP or HTTPS browser. If you select HTTP, all data is exchanged in clear text mode.  For a secure browser session, we recommend that you enable HTTPS and disable HTTP.  By default, Cisco UCS implements a browser redirects to an HTTPS equivalent and recommends that you do not change this behavior.  |  **Note** |  If you are upgrading to Cisco UCS, version 1.4(1), the browser redirect to a secure browser does not occur by default. To redirect the HTTP browser to an HTTPS equivalent, enable the Redirect HTTP to HTTPS in Cisco UCS Manager.   
---|---  
HTTPS  |  By default, HTTPS is enabled on port. With HTTPS, all data is exchanged in encrypted mode through a secure server.  For a secure browser session, We recommend that you only use HTTPS and either disable or redirect HTTP communications.   
SMASH CLP  |  This service is enabled for read-only access and supports a limited subset of the protocols, such as the show command. You cannot disable it.  This shell service is one of the standards that the Distributed Management Task Force defines.   
SNMP  |  By default, this service is disabled. If enabled, the default port is 161. You must configure the community and at least one SNMP trap.  Enable this service only if your system includes integration with an SNMP server.   
SSH  |  This service is enabled on port 22. You cannot disable it, and you cannot change the default port.  This service provides access to the Cisco UCS Manager CLI.   
Telnet  |  By default, this service is disabled.  This service provides access to the Cisco UCS Manager CLI. 

---
