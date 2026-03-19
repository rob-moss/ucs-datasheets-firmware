# UCS Manager CLI System Monitoring Guide 4.3

| | |
|---|---|
| **URL Title** | UCS Manager CLI System Monitoring Guide 4.3 |
| **URL** | https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/System-Monitoring/4-3/b-ucsm-cli-system-monitoring-guide-4-3.html |
| **Long URL** |  |
| **HTML Title** | Cisco UCS Manager System Monitoring Guide Using the CLI, Release 4.3 |
| **Source file** | `ucs-docs-raw/html/b-ucsm-cli-system-monitoring-guide-4-3.html` |
| **File type** | HTML |
| **Fetched on** | 2026-03-19 16:46:46 |

---

## Page 1: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/System-Monitoring/4-3/b-ucsm-cli-system-monitoring-guide-4-3.html

![Clear Contents of Search](/etc/designs/cdc/fw/i/ic_clear_gray.png)

---

## Page 2: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/System-Monitoring/4-3/b-ucsm-cli-system-monitoring-guide-4-3/m_preface.html

## Audience  
  
This guide is intended primarily for data center administrators with responsibilities and expertise in one or more of the following: 

  * Server administration 

  * Storage administration 

  * Network administration 

  * Network security 


---

## Page 3: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/System-Monitoring/4-3/b-ucsm-cli-system-monitoring-guide-4-3/m-new-and-changed-4-3-cli.html

## New and Changed Information

This section provides information on new features and changed behavior in Cisco UCS Manager, Release 4.3. 

Table 1. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(6a) Feature  |  Description  |  Where Documented   
---|---|---  
Support for X-Series M8 and C-Series M8 servers |  Cisco UCS Manager now supports Cisco UCS X210c M8 Compute Node, Cisco UCS C240 M8 Server, and Cisco UCS C220 M8 Server | 

  * [Support for Local Storage Monitoring](m_cli_hardware_monitoring.html#reference_s5w_2fy_ndb)
  * [Graphics Card Server Support](m_cli_hardware_monitoring.html#concept_B6CBDE8AAEE041B9A3E5165193A53B36)
  * [TFM and Supercap Guidelines and Limitations](m_cli_hardware_monitoring.html#concept_ED653EA1CAA349739E8BF2616A29C645)

  
Table 2. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(5a) Feature  |  Description  |  Where Documented   
---|---|---  
Support for X-Series M8 server |  Cisco UCS Manager now supports Cisco UCS X215c M8 Compute Node | 

  * [Support for Local Storage Monitoring](m_cli_hardware_monitoring.html#reference_s5w_2fy_ndb)
  * [Graphics Card Server Support](m_cli_hardware_monitoring.html#concept_B6CBDE8AAEE041B9A3E5165193A53B36)
  * [TFM and Supercap Guidelines and Limitations](m_cli_hardware_monitoring.html#concept_ED653EA1CAA349739E8BF2616A29C645)

  
Support for C-Series M8 server |  Cisco UCS Manager now supports Cisco UCS C225 M8 Server | 

  * [Support for Local Storage Monitoring](m_cli_hardware_monitoring.html#reference_s5w_2fy_ndb)
  * [Graphics Card Server Support](m_cli_hardware_monitoring.html#concept_B6CBDE8AAEE041B9A3E5165193A53B36)
  * [TFM and Supercap Guidelines and Limitations](m_cli_hardware_monitoring.html#concept_ED653EA1CAA349739E8BF2616A29C645)

  
Support for monitoring port status |  Cisco UCS Manager now supports dynamic polling to monitor the port status |  [Monitoring the Host Ethernet Interface status for a Rack-Mount Server](m_cli_hardware_monitoring.html#monitoring-host-ethernet-interface-status)  
Table 3. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(4b) Feature  |  Description  |  Where Documented   
---|---|---  
Support for Cisco UCS Fabric Interconnects 9108 100G |  Cisco UCS Manager now supports Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct)  | 

  * [Enabling Syslog Messages to Store In a Local File](m_cli_syslog.html#task_87ADF499A8214D25B146B67A0CC13C6A)
  * [NetFlow Monitoring](m_cli_netflow_monitoring-4-0.html#concept_k2x_dxz_22b)

  
Table 4. New Features and Changed Behavior in Cisco UCS Manager, 4.3(4a) Release Feature  |  Description  |  Where Documented   
---|---|---  
Traffic Monitoring | Cisco UCS Manager guidelines for configuring ERSPAN Traffic Monitoring on Cisco UCS 64108 Fabric Interconnects and Cisco UCS 6532 Fabric Interconnects.  |  [Traffic Monitoring](m_cli_traffic_monitoring-4-0.html#concept_hcj_z1r_tdb)  
PCIe Node Monitoring |  PCIe node inventory monitoring |  [Monitoring PCIe Node](m_cli_hardware_monitoring.html#monitoring-pcie-node)

---

## Page 4: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/System-Monitoring/4-3/b-ucsm-cli-system-monitoring-guide-4-3/m_system_monitoring_overview-4_3.html

## System Monitoring Overview   
  
This guide describes how to configure and use system monitoring to manage a Cisco UCS Manager environment. 

Cisco UCS Manager can detect system faults: critical, major, minor, and warnings. We recommend that: 

  * You monitor all faults of either critical or major severity status, as immediate action is not required for minor faults and warnings. 

  * You monitor faults that are not of type Finite State Machine (FSM), as FSM faults will transition over time and resolve. 


This guide covers the following information: 

  * System Log 

  * System logs including faults, failures, and alarm thresholds (Syslog) 

  * The three types of Syslogs: Fault, Event, and Audit logs 

  * The Global Fault Policy and settings that control Syslogs 


  * System Event Log 

  * System hardware events for servers and chassis components and their internal components (System Event Log [SEL] logs) 

  * The SEL policy that controls SEL logs 

  * Simple Network Management Protocol 

  * SNMP for monitoring devices from a central network management station and the host and user settings 

  * Fault suppression policies for SNMP traps, Call Home notifications, and specific devices 

  * Core File Exporter and logs, such as Syslog, Audit Log, and the System Event Log 

  * Statistics Collection and Threshold Policies for adapters, chassis, host, ports, and servers 

  * Call Home and Smart Call Home Cisco embedded device support 

  * Hardware monitoring using the Cisco UCS Manager user interface 

  * Traffic Monitoring sessions for analysis by a network analyzer 

  * Cisco Netflow Monitor for IP network traffic accounting, usage-based network billing, network planning, security, Denial of Service monitoring capabilities, and network monitoring 


---

## Page 5: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/System-Monitoring/4-3/b-ucsm-cli-system-monitoring-guide-4-3/m_cli_syslog.html

## Syslog

Cisco UCS Manager generates system log, or syslog messages to record the following incidents that take place in the Cisco UCS Manager system: 

  * Routine system operations 

  * Failures and errors 

  * Critical and emergency conditions 


There are three kinds of syslog entries: Fault, Event, and Audit. 

Each syslog message identifies the Cisco UCS Manager process that generated the message and provides a brief description of the operation or error that occurred. The syslog is useful both in routine troubleshooting, incident handling, and management. 

Cisco UCS Manager collects and logs syslog messages internally. You can send them to external syslog servers running a syslog daemon. Logging to a central syslog server helps in aggregation of logs and alerts. Some syslog messages to monitor include, DIMM problems, equipment failures, thermal problems, voltage problems, power problems, high availability (HA) cluster problems, and link failures. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The FSM faults, threshold faults, and unresolved policy events are not sent to syslog server. However, SNMP traps are generated for the threshold fault events. 

* * *  
  
---|---  
  
Syslog messages contain an event code and fault code. To monitor syslog messages, you can define syslog message filters. These filters can parse the syslog messages based on the criteria you choose. You can use the following criteria to define a filter: 

  * By event or fault codes: Define a filter with a parsing rule to include only the specific codes that you intend to monitor. Messages that do not match these criteria are discarded. 

  * By severity level: Define a filter with a parsing rule to monitor syslog messages with specific severity levels. You can set syslog severity levels individually for OS functions, to facilitate logging and display of messages ranging from brief summaries to detailed information for debugging. 


Cisco devices can send their log messages to a Unix-style syslog service. A syslog service simply accepts messages, then stores them in files or prints them according to a simple configuration file. This form of logging is the best available for Cisco devices because it can provide protected long-term storage of logs. 

---

## Page 6: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/System-Monitoring/4-3/b-ucsm-cli-system-monitoring-guide-4-3/m_cli_system_event_log_management.html

## System Event Log 

The System Event Log (SEL) resides on the CIMC in NVRAM. The SEL is used for troubleshooting system health. It records most server-related events, such as instances of over or under voltage, temperature events, fan events, and BIOS events. The types of events supported by SEL include BIOS events, memory unit events, processor events, and motherboard events. 

The SEL logs are stored in the CIMC NVRAM, through a SEL log policy. It is best practice to periodically download and clear the SEL logs. The SEL file is approximately 40KB in size, and no further events can be recorded once it is full. It must be cleared before additional events can be recorded. 

You can use the SEL policy to back up the SEL to a remote server, and optionally to clear the SEL after a backup operation occurs. Backup operations can be triggered based on specific actions, or they can be set to occur at regular intervals. You can also manually back up or clear the SEL. 

The backup file is automatically generated. The filename format is sel-SystemName-ChassisID-ServerID-ServerSerialNumber-Timestamp. 

For example, sel-UCS-A-ch01-serv01-QCI12522939-20091121160736. 

---

## Page 7: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/System-Monitoring/4-3/b-ucsm-cli-system-monitoring-guide-4-3/m_cli_audit_logs.html

## Audit Logs

Audit Logs record system events that occurred, where they occurred, and which users initiated them. 

---

## Page 8: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/System-Monitoring/4-3/b-ucsm-cli-system-monitoring-guide-4-3/m_cli_log_file_exporter.html

## Log File Exporter 

Cisco UCS Manager generates log files for each executable. The log files can be up to 20 MB in size, and up to five backups can be stored on the server. The log file exporter allows you to export the log files to a remote server before they are deleted. The log file names contain the following information: 

  * The name of the process 

  * Timestamp 

  * The name and ID of the fabric interconnect 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

If you do not enable log exporting, the oldest log files are deleted whenever the maximum backup file limit is reached. 

* * *  
  
---|---  
  
### Guidelines and Limitations

  * We recommend that you use tftp or password-less scp or sftp for log export. When standard scp or sftp is used, the user password is stored in the configuration file in encrypted format. 

  * On a HA setup, the log files from each side are exported separately. If one side fails to export logs, the other side does not compensate. 


---

## Page 9: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/System-Monitoring/4-3/b-ucsm-cli-system-monitoring-guide-4-3/m_cli_core_file_exporter.html

## Core File Exporter 

Critical failures in the Cisco UCS components, such as a fabric interconnect or an I/O module, can cause the system to create a core dump file. Cisco UCS Manager uses the Core File Exporter to immediately export the core dump files to a specified location on the network through TFTP. This functionality allows you to export the tar file with the contents of the core dump file. The Core File Exporter provides system monitoring and automatic export of core dump files that need to be included in TAC cases. 

---

## Page 10: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/System-Monitoring/4-3/b-ucsm-cli-system-monitoring-guide-4-3/m-system-monitoring-and-debugging.html

## Load Debug Plugin

### Load Debug Plugin

The `load-debug-plugin` command is intended for use by Technical Assistance Center (TAC) personnel. This command enables the loading of debug plugins, which provide enhanced visibility and diagnostic capabilities during critical fault and error conditions in Cisco UCS Manager. It is applicable only for Cisco UCS 6300 Series Fabric Interconnects and lower versions. 

**Procedure**

**Command or Action** | **Purpose**  
---|---  
UCS-A# **load _debug-plugin_** |  Loads the debug-plugin image. This debug plugin image is copied by TAC and  loaded for the purpose of monitoring and debugging.

---

## Page 11: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/System-Monitoring/4-3/b-ucsm-cli-system-monitoring-guide-4-3/m_cli_fault_collection_and_suppression.html

## Global Fault Policy   
  
The global fault policy controls the lifecycle of a fault in a Cisco UCS domain, including when faults are cleared, the flapping interval (the length of time between the fault being raised and the condition being cleared), and the retention interval (the length of time a fault is retained in the system). 

A fault in Cisco UCS has the following lifecycle: 

  1. A condition occurs in the system and Cisco UCS Manager raises a fault. This is the active state. 

  2. When the fault is alleviated, it enters a flapping or soaking interval that is designed to prevent flapping. Flapping occurs when a fault is raised and cleared several times in rapid succession. During the flapping interval, the fault retains its severity for the length of time specified in the global fault policy. 

  3. If the condition reoccurs during the flapping interval, the fault returns to the active state. If the condition does not reoccur during the flapping interval, the fault is cleared. 

  4. The cleared fault enters the retention interval. This interval ensures that the fault reaches the attention of an administrator even if the condition that caused the fault has been alleviated and the fault has not been deleted prematurely. The retention interval retains the cleared fault for the length of time specified in the global fault policy. 

  5. If the condition reoccurs during the retention interval, the fault returns to the active state. If the condition does not reoccur, the fault is deleted. 


### Configuring the Fault Collection Policy

#### Procedure

| Command or Action | Purpose  
---|---|---  
**Step 1** |  UCS-A#  scope monitoring |  Enters monitoring mode.   
**Step 2** |  UCS-A /monitoring #  scope fault policy |  Enters monitoring fault policy mode.   
**Step 3** |  UCS-A /monitoring/fault-policy #  set clear-action {delete | retain}  |  Specifies whether to retain or delete all cleared messages. If the  retain option is specified, then the length of time that the messages are retained is determined by the  set retention-interval command.   
**Step 4** |  UCS-A /monitoring/fault-policy #  set flap-interval seconds |  Specifies the time interval (in seconds) the system waits before changing a fault state. Flapping occurs when a fault is raised and cleared several times in rapid succession. To prevent this, the system does not allow a fault to change state until the flapping interval has elapsed after the last state change. If the fault is raised again during the flapping interval, it returns to the active state, otherwise, the fault is cleared.   
**Step 5** |  UCS-A /monitoring/fault-policy #  set retention-interval {days hours minutes seconds | forever}  |  Specifies the time interval the system retains all cleared fault messages before deleting them. The system can retain cleared fault messages forever, or for the specified number of days, hours, minutes, and seconds.   
**Step 6** |  UCS-A /monitoring/fault-policy #  commit-buffer |  Commits the transaction.  
  
#### Example

This example configures the fault collection policy to retain cleared fault messages for 30 days, sets the flapping interval to 10 seconds, and commits the transaction. 
    
    
    UCS-A# **scope monitoring**
    UCS-A /monitoring # **scope fault policy**
    UCS-A /monitoring/fault-policy # **set clear-action retain**
    UCS-A /monitoring/fault-policy* # **set flap-interval 10**
    UCS-A /monitoring/fault-policy* # **set retention-interval 30 0 0 0**
    UCS-A /monitoring/fault-policy* # **commit-buffer**
    UCS-A /monitoring/fault-policy # 

---

## Page 12: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/System-Monitoring/4-3/b-ucsm-cli-system-monitoring-guide-4-3/m_cli_snmp_configuration.html

## SNMP Overview 

The Simple Network Management Protocol (SNMP) is an application-layer protocol that provides a message format for communication between SNMP managers and agents. SNMP provides a standardized framework and a common language for monitoring and managing devices in a network. 

---

## Page 13: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/System-Monitoring/4-3/b-ucsm-cli-system-monitoring-guide-4-3/m_cli_statistics_collection_policies.html

## Statistics Collection Policy 

A statistics collection policy defines how frequently statistics are collected (collection interval) and how frequently the statistics are reported (reporting interval). Reporting intervals are longer than collection intervals so that multiple statistical data points can be collected during the reporting interval. This provides Cisco UCS Manager with sufficient data to calculate and report minimum, maximum, and average values. 

For NIC statistics, Cisco UCS Manager displays the average, minimum, and maximum of the change since the last collection of statistics. If the values are 0, there has been no change since the last collection. 

Statistics can be collected and reported for the following five functional areas of the Cisco UCS system: 

  * Adapter — Statistics related to the adapters 

  * Chassis — Statistics related to the chassis 

  * Host — This policy is a placeholder for future support 

  * Port — Statistics related to the ports, including server ports, uplink Ethernet ports, and uplink Fibre Channel ports 

  * Server — Statistics related to servers 


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Cisco UCS Manager has one default statistics collection policy for each of the five functional areas. You cannot create additional statistics collection policies and you cannot delete the existing default policies. You can only modify the default policies.  The values that are displayed for delta counter in Cisco UCS Manager are calculated as the difference between the last two samples in a collection interval. In addition, Cisco UCS Manager displays the average, minimum, and maximum delta values of the samples in the collection interval. 

* * *  
  
---|---

---

## Page 14: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/System-Monitoring/4-3/b-ucsm-cli-system-monitoring-guide-4-3/m_cli_call_home_and_smart_call_home.html

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

## Page 15: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/System-Monitoring/4-3/b-ucsm-cli-system-monitoring-guide-4-3/m_database_health_monitoring.html

## Cisco UCS Manager Database Health Monitoring  
  
Cisco UCS Manager uses a SQLite database stored on the Fabric Interconnects to persist configuration and inventory. Data corruption on both the Flash and NVRAM storage devices can cause failures and loss of customer configuration data. Cisco UCS Manager provides several proactive health check and recovery mechanisms to improve the integrity of the Cisco UCS Manager database. These mechanisms enable active monitoring of the database health. 

  * Periodic Health Check— A periodic check of database integrity ensures that any corruption is caught and recovered proactively. See Triggering Health Check, and Changing Health Check Interval. 

  * Periodic Backup— A periodic internal full state backup of the system ensures a smoother route to recovery in the case of any unrecoverable errors. See Changing Internal Backup Interval. 


---

## Page 16: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/System-Monitoring/4-3/b-ucsm-cli-system-monitoring-guide-4-3/m_cli_hardware_monitoring.html

## System Monitoring CLI Command Cheat Sheet 

The following table provides a brief summary of Cisco UCS Manager CLI commands you use to monitor managed objects in the system. 

Managed Object  |  Monitoring Command  |  Description   
---|---|---  
**Hardware**  
Chassis  |  show chassis [adaptor | cmc | decommissioned | detail | environment | fabric | fi-iom | firmware | fsm | inventory | psu | version]  |  Displays chassis information.   
Fabric Interconnect  |  show fabric-interconnect [a | b ] [detail | environment | firmware | fsm | inventory | mac-aging | mode | version]  |  Displays Fabric Interconnect information.   
FEX  |  show fex [detail | firmware | fsm | inventory | version]  |  Displays Fabric Extender information   
IOM  |  show iom [firmware | health | version]  |  Displays Fabric Input/Output Module information.   
Server  |  show server [actual-boot-order adapter | assoc | bios | boot-order | cpu | decommissioned | environment | firmware | health | identity | inventory | memory | status | storage | version]  |  Displays server information .   
System  |  show system [detail | firmware | version]  |  Displays system information.   
System  | scope monitoring [show] [baseline-faults | callhome | event | fault | fault-suppress-policy | fsm | mgmt-if-mon-policy | new-faults | snmp | snmp-trap | snmp-user | stats-collection-policy | stats-threshold-policy | syslog]  |  Displays information about commands in Monitoring mode.   
**Logs**  
Event  |  show event [event-id | detail]  |  Displays the Event log.   
Fault  | show fault [fault-id | cause | detail | severity | suppressed]  |  Displays the Fault log.   
SEL  | show sel [chassis-id/blade-id | rack-id]  |  Displays the System Event Log for the chassis, blade, or rack-mount server.   
Syslog  | scope monitoring [show ] [syslog]  |  Displays the Syslog. 

---

## Page 17: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/System-Monitoring/4-3/b-ucsm-cli-system-monitoring-guide-4-3/m_cli_netflow_monitoring-4-0.html

## NetFlow Monitoring  
  
NetFlow is a standard network protocol for collecting IP traffic data. NetFlow enables you to define a flow in terms of unidirectional IP packets that share certain characteristics. All packets that match the flow definition are collected and exported to one or more external NetFlow Collectors, where they can be further aggregated, analyzed, and used for application-specific processing. 

Cisco UCS Manager uses NetFlow-capable adapters (Cisco UCS Cisco UCS VIC 1300 series, Cisco UCS VIC 1400 series, Cisco UCS VIC 14000 series, and Cisco UCS VIC 15000 series) to communicate with the routers and switches that collect and export flow information. 

Starting from 4.3(2b) release, NetFlow monitoring is supported on Cisco UCS 6400 and 6500 series Fabric Interconnects. 

Starting from 4.3(4b) release, NetFlow monitoring is supported on Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct). 

### Network Flows

A flow is a set of unidirectional IP packets that have common properties such as, the source or destination of the traffic, routing information, and protocol used. Flows are collected when they match the definitions in the flow record definition. 

### Flow Record Definitions

A flow record definition contains information about the properties used to define the flow, which can include both characteristic properties or measured properties. Characteristic properties, also called flow keys, are the properties that define the flow. Cisco UCS Manager supports IPv4, IPv6, and Layer 2 keys. Measured characteristics, also called flow values or non-keys, measurable values such as the number of bytes contained in all packets of the flow, or the total number of packets. 

A flow record definition is a specific combination of flow keys and flow values. The two types of flow record definitions are: 

  * System-defined—Default flow record definitions supplied by Cisco UCS Manager. 

  * User-defined—Flow record definitions that you can create yourself. 


### Flow Exporters, Flow Exporter Profiles, and Flow Collectors

Flow exporters transfer the flows to the flow connector based on the information in a flow exporter profile. The flow exporter profile contains the networking properties used to export NetFlow packets. The networking properties include a VLAN, the source IP address, and the subnet mask for each fabric interconnect. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

In the Cisco UCS Manager GUI, the networking properties are defined in an exporter interface that is included in the profile. In the Cisco UCS Manager CLI, the properties are defined in the profile. 

* * *  
  
---|---  
  
Flow collectors receive the flows from the flow exporter. Each flow collector contains an IP address, port, external gateway IP, and VLAN that defines where the flows are sent. 

### Flow Monitors and Flow Monitor Sessions

A flow monitor consists of a flow definition, one or two flow exporters, and a timeout policy. You can use a flow monitor to specify which flow information you want to gather, and where you want to collect it from. Each flow monitor operates in either the egress or ingress direction. 

A flow monitor session contains up to four flow monitors: two flow monitors in the ingress direction and two flow monitors in the egress direction. A flow monitor session can also be associated with a vNIC. 

---

## Page 18: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/System-Monitoring/4-3/b-ucsm-cli-system-monitoring-guide-4-3/m_cli_traffic_monitoring-4-0.html

## Traffic Monitoring

Traffic monitoring copies traffic from one or more source ports and sends the copied traffic to a dedicated destination port for analysis by a network analyzer. This feature is also known as Switched Port Analyzer (SPAN). 

However, this traffic monitoring is limited to one switch. SPAN can send the traffic between switches, but this traffic cannot be routed. To overcome this problem, support for ERSPAN (Encapsulated Remote Switched Port Analyzer) is provided from Cisco UCS Manager 4.3(4a). 

ERSPAN uses GRE encapsulation, which allows you to route SPAN traffic from a source to a destination in the L3 network.

ERSPAN is used to transport mirrored traffic in an IP network. An origin interface will be created on each Fabric Interconnect with a configured source IP address to forward the packets on the L3 network. A unique IP address per fabric is captured along with the VLAN information. 

### Types of Traffic Monitoring Sessions

There are two types of monitoring sessions: 

  * Ethernet

  * Fibre Channel


The type of destination port determines what kind of monitoring session you need. For an Ethernet traffic monitoring session, the destination port must be an unconfigured physical port. For a Fibre Channel traffic monitoring session, the destination port must be a Fibre Channel uplink port except when you are using Cisco UCS 6500 Series Fabric Interconnect, Cisco UCS 6400 Series Fabric Interconnect, and 6300 Series Fabric Interconnects. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For Cisco UCS 6332, 6332-16UP, 64108, 6454, and 6536 Fabric Interconnects, you cannot choose Fibre Channel destination ports. The destination port must be an unconfigured physical Ethernet port. 

* * *  
  
---|---  
  
### Traffic Monitoring Across Ethernet

An Ethernet traffic monitoring session can monitor any of the following traffic source and destination ports: 

Source Ports  |  Destination Ports   
---|---  
  
  * Uplink Ethernet port 
  * Ethernet port channel 
  * VLAN 
  * Service profile vNIC 
  * Service profile vHBA 
  * FCoE port 
  * Port channels 
  * Unified uplink port 
  * VSAN 

|  Unconfigured Ethernet Port   
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

All traffic sources must be located within the same switch as the destination port. A port configured as a destination port cannot also be configured as a source port. A member port of a port channel cannot be configured individually as a source. If the port channel is configured as a source, all member ports are source ports. 

* * *  
  
---|---  
  
A server port can be a source, only if it is a non-virtualized rack server adapter-facing port. 

### Traffic Monitoring for Cisco UCS 6500,6400 Series Fabric Interconnects 

  * Cisco UCS 6500, 6400 Series Fabric Interconnects do not support a Fibre Channel port as a destination port. Therefore, an Ethernet port is the only option for configuring any traffic monitoring session on this Fabric Interconnect. 

  * Cisco UCS 6500, 6400 Series Fabric Interconnects support monitoring traffic in the transmit direction for more than two sources per Fabric Interconnect. 

  * You can monitor or use SPAN on port channels sources for traffic in the transmit and receive directions.

  * You can configure a port as a destination port for only one monitor session.

  * You can monitoring Port-Channel as a source in the transmit direction.

  * You cannot monitor vEth as a source in the transmit direction.


### Traffic Monitoring for Cisco UCS 6300 Fabric Interconnects

  * Cisco UCS 6300 Fabric Interconnect supports port-based mirroring.

  * Cisco UCS 6300 Fabric Interconnects support VLAN SPAN only in the receive direction. 

  * Ethernet SPAN is port based on the Cisco UCS 6300 Fabric Interconnect. 


### Traffic Monitoring Across Fibre Channel

You can monitor Fibre Channel traffic using either a Fibre Channel traffic analyzer or an Ethernet traffic analyzer. When Fibre Channel traffic is monitored with an Ethernet traffic monitoring session, at an Ethernet destination port, the destination traffic is FCoE. The Cisco UCS 6300 Fabric Interconnect supports FC SPAN only on the ingress side.

A Fibre Channel traffic monitoring session can monitor any of the following traffic source and destination ports: 

Source Ports  |  Destination Ports   
---|---  
  
  * FC Port 
  * FC Port Channel 
  * Uplink Fibre Channel port 
  * SAN port channel 
  * VSAN 
  * Service profile vHBA 
  * Fibre Channel storage port 

| 

  * Fibre Channel uplink port 
  * Unconfigured Ethernet Port (Cisco UCS 6536, 64108, 6454, 6332, and 6332-16UP Fabric Interconnects) 


---

## Page 19: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/System-Monitoring/4-3/m_cli_hardware_monitoring.html

## System Monitoring CLI Command Cheat Sheet   
  
The following table provides a brief summary of Cisco UCS Manager CLI commands you use to monitor managed objects in the system. 

Managed Object  |  Monitoring Command  |  Description   
---|---|---  
**Hardware**  
Chassis  |  show chassis [adaptor | cmc | decommissioned | detail | environment | fabric | fi-iom | firmware | fsm | inventory | psu | version]  |  Displays chassis information.   
Fabric Interconnect  |  show fabric-interconnect [a | b ] [detail | environment | firmware | fsm | inventory | mac-aging | mode | version]  |  Displays Fabric Interconnect information.   
FEX  |  show fex [detail | firmware | fsm | inventory | version]  |  Displays Fabric Extender information   
IOM  |  show iom [firmware | health | version]  |  Displays Fabric Input/Output Module information.   
Server  |  show server [actual-boot-order adapter | assoc | bios | boot-order | cpu | decommissioned | environment | firmware | health | identity | inventory | memory | status | storage | version]  |  Displays server information .   
System  |  show system [detail | firmware | version]  |  Displays system information.   
System  | scope monitoring [show] [baseline-faults | callhome | event | fault | fault-suppress-policy | fsm | mgmt-if-mon-policy | new-faults | snmp | snmp-trap | snmp-user | stats-collection-policy | stats-threshold-policy | syslog]  |  Displays information about commands in Monitoring mode.   
**Logs**  
Event  |  show event [event-id | detail]  |  Displays the Event log.   
Fault  | show fault [fault-id | cause | detail | severity | suppressed]  |  Displays the Fault log.   
SEL  | show sel [chassis-id/blade-id | rack-id]  |  Displays the System Event Log for the chassis, blade, or rack-mount server.   
Syslog  | scope monitoring [show ] [syslog]  |  Displays the Syslog. 

---

## Page 20: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/System-Monitoring/4-3/m_cli_syslog.html

## Syslog  
  
Cisco UCS Manager generates system log, or syslog messages to record the following incidents that take place in the Cisco UCS Manager system: 

  * Routine system operations 

  * Failures and errors 

  * Critical and emergency conditions 


There are three kinds of syslog entries: Fault, Event, and Audit. 

Each syslog message identifies the Cisco UCS Manager process that generated the message and provides a brief description of the operation or error that occurred. The syslog is useful both in routine troubleshooting, incident handling, and management. 

Cisco UCS Manager collects and logs syslog messages internally. You can send them to external syslog servers running a syslog daemon. Logging to a central syslog server helps in aggregation of logs and alerts. Some syslog messages to monitor include, DIMM problems, equipment failures, thermal problems, voltage problems, power problems, high availability (HA) cluster problems, and link failures. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The FSM faults, threshold faults, and unresolved policy events are not sent to syslog server. However, SNMP traps are generated for the threshold fault events. 

* * *  
  
---|---  
  
Syslog messages contain an event code and fault code. To monitor syslog messages, you can define syslog message filters. These filters can parse the syslog messages based on the criteria you choose. You can use the following criteria to define a filter: 

  * By event or fault codes: Define a filter with a parsing rule to include only the specific codes that you intend to monitor. Messages that do not match these criteria are discarded. 

  * By severity level: Define a filter with a parsing rule to monitor syslog messages with specific severity levels. You can set syslog severity levels individually for OS functions, to facilitate logging and display of messages ranging from brief summaries to detailed information for debugging. 


Cisco devices can send their log messages to a Unix-style syslog service. A syslog service simply accepts messages, then stores them in files or prints them according to a simple configuration file. This form of logging is the best available for Cisco devices because it can provide protected long-term storage of logs. 

---

## Page 21: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/System-Monitoring/4-3/m_cli_netflow_monitoring-4-0.html

## NetFlow Monitoring

NetFlow is a standard network protocol for collecting IP traffic data. NetFlow enables you to define a flow in terms of unidirectional IP packets that share certain characteristics. All packets that match the flow definition are collected and exported to one or more external NetFlow Collectors, where they can be further aggregated, analyzed, and used for application-specific processing. 

Cisco UCS Manager uses NetFlow-capable adapters (Cisco UCS Cisco UCS VIC 1300 series, Cisco UCS VIC 1400 series, Cisco UCS VIC 14000 series, and Cisco UCS VIC 15000 series) to communicate with the routers and switches that collect and export flow information. 

Starting from 4.3(2b) release, NetFlow monitoring is supported on Cisco UCS 6400 and 6500 series Fabric Interconnects. 

Starting from 4.3(4b) release, NetFlow monitoring is supported on Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct). 

### Network Flows

A flow is a set of unidirectional IP packets that have common properties such as, the source or destination of the traffic, routing information, and protocol used. Flows are collected when they match the definitions in the flow record definition. 

### Flow Record Definitions

A flow record definition contains information about the properties used to define the flow, which can include both characteristic properties or measured properties. Characteristic properties, also called flow keys, are the properties that define the flow. Cisco UCS Manager supports IPv4, IPv6, and Layer 2 keys. Measured characteristics, also called flow values or non-keys, measurable values such as the number of bytes contained in all packets of the flow, or the total number of packets. 

A flow record definition is a specific combination of flow keys and flow values. The two types of flow record definitions are: 

  * System-defined—Default flow record definitions supplied by Cisco UCS Manager. 

  * User-defined—Flow record definitions that you can create yourself. 


### Flow Exporters, Flow Exporter Profiles, and Flow Collectors

Flow exporters transfer the flows to the flow connector based on the information in a flow exporter profile. The flow exporter profile contains the networking properties used to export NetFlow packets. The networking properties include a VLAN, the source IP address, and the subnet mask for each fabric interconnect. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

In the Cisco UCS Manager GUI, the networking properties are defined in an exporter interface that is included in the profile. In the Cisco UCS Manager CLI, the properties are defined in the profile. 

* * *  
  
---|---  
  
Flow collectors receive the flows from the flow exporter. Each flow collector contains an IP address, port, external gateway IP, and VLAN that defines where the flows are sent. 

### Flow Monitors and Flow Monitor Sessions

A flow monitor consists of a flow definition, one or two flow exporters, and a timeout policy. You can use a flow monitor to specify which flow information you want to gather, and where you want to collect it from. Each flow monitor operates in either the egress or ingress direction. 

A flow monitor session contains up to four flow monitors: two flow monitors in the ingress direction and two flow monitors in the egress direction. A flow monitor session can also be associated with a vNIC. 

---

## Page 22: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/System-Monitoring/4-3/m_cli_traffic_monitoring-4-0.html

## Traffic Monitoring

Traffic monitoring copies traffic from one or more source ports and sends the copied traffic to a dedicated destination port for analysis by a network analyzer. This feature is also known as Switched Port Analyzer (SPAN). 

However, this traffic monitoring is limited to one switch. SPAN can send the traffic between switches, but this traffic cannot be routed. To overcome this problem, support for ERSPAN (Encapsulated Remote Switched Port Analyzer) is provided from Cisco UCS Manager 4.3(4a). 

ERSPAN uses GRE encapsulation, which allows you to route SPAN traffic from a source to a destination in the L3 network.

ERSPAN is used to transport mirrored traffic in an IP network. An origin interface will be created on each Fabric Interconnect with a configured source IP address to forward the packets on the L3 network. A unique IP address per fabric is captured along with the VLAN information. 

### Types of Traffic Monitoring Sessions

There are two types of monitoring sessions: 

  * Ethernet

  * Fibre Channel


The type of destination port determines what kind of monitoring session you need. For an Ethernet traffic monitoring session, the destination port must be an unconfigured physical port. For a Fibre Channel traffic monitoring session, the destination port must be a Fibre Channel uplink port except when you are using Cisco UCS 6500 Series Fabric Interconnect, Cisco UCS 6400 Series Fabric Interconnect, and 6300 Series Fabric Interconnects. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For Cisco UCS 6332, 6332-16UP, 64108, 6454, and 6536 Fabric Interconnects, you cannot choose Fibre Channel destination ports. The destination port must be an unconfigured physical Ethernet port. 

* * *  
  
---|---  
  
### Traffic Monitoring Across Ethernet

An Ethernet traffic monitoring session can monitor any of the following traffic source and destination ports: 

Source Ports  |  Destination Ports   
---|---  
  
  * Uplink Ethernet port 
  * Ethernet port channel 
  * VLAN 
  * Service profile vNIC 
  * Service profile vHBA 
  * FCoE port 
  * Port channels 
  * Unified uplink port 
  * VSAN 

|  Unconfigured Ethernet Port   
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

All traffic sources must be located within the same switch as the destination port. A port configured as a destination port cannot also be configured as a source port. A member port of a port channel cannot be configured individually as a source. If the port channel is configured as a source, all member ports are source ports. 

* * *  
  
---|---  
  
A server port can be a source, only if it is a non-virtualized rack server adapter-facing port. 

### Traffic Monitoring for Cisco UCS 6500,6400 Series Fabric Interconnects 

  * Cisco UCS 6500, 6400 Series Fabric Interconnects do not support a Fibre Channel port as a destination port. Therefore, an Ethernet port is the only option for configuring any traffic monitoring session on this Fabric Interconnect. 

  * Cisco UCS 6500, 6400 Series Fabric Interconnects support monitoring traffic in the transmit direction for more than two sources per Fabric Interconnect. 

  * You can monitor or use SPAN on port channels sources for traffic in the transmit and receive directions.

  * You can configure a port as a destination port for only one monitor session.

  * You can monitoring Port-Channel as a source in the transmit direction.

  * You cannot monitor vEth as a source in the transmit direction.


### Traffic Monitoring for Cisco UCS 6300 Fabric Interconnects

  * Cisco UCS 6300 Fabric Interconnect supports port-based mirroring.

  * Cisco UCS 6300 Fabric Interconnects support VLAN SPAN only in the receive direction. 

  * Ethernet SPAN is port based on the Cisco UCS 6300 Fabric Interconnect. 


### Traffic Monitoring Across Fibre Channel

You can monitor Fibre Channel traffic using either a Fibre Channel traffic analyzer or an Ethernet traffic analyzer. When Fibre Channel traffic is monitored with an Ethernet traffic monitoring session, at an Ethernet destination port, the destination traffic is FCoE. The Cisco UCS 6300 Fabric Interconnect supports FC SPAN only on the ingress side.

A Fibre Channel traffic monitoring session can monitor any of the following traffic source and destination ports: 

Source Ports  |  Destination Ports   
---|---  
  
  * FC Port 
  * FC Port Channel 
  * Uplink Fibre Channel port 
  * SAN port channel 
  * VSAN 
  * Service profile vHBA 
  * Fibre Channel storage port 

| 

  * Fibre Channel uplink port 
  * Unconfigured Ethernet Port (Cisco UCS 6536, 64108, 6454, 6332, and 6332-16UP Fabric Interconnects) 


---
