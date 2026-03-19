# Overview

This is a help reference for the UCS CLI based on previous experience and screen output from real UCS CLI sessions. It is not an official document from Cisco, but it may be useful for users who want to learn how to use the UCS CLI.



# Sections
There are several sections in this help reference, each subesquent section is a deep dive in to the issue, the problem statement and how to resolve it.




### Connecting to FI NXOS mode
From Intersight -> Operate -> Fabric Interconnects -> Select the FI
Actions -> Launch CLI

```
nsd5-static-ucsx-A# connect help

Connect to an endpoint


Commands:
  adapter               Connect to the adapter
  cimc                  Connect to the cimc
  device-connector      Connect to the device connector shell
  fex                   Connect to the fabric extender
  iom                   Connect to the iom
  nxos                  Connect to the NXOS shell
  xfm                   Connect to the xfm


nsd5-static-ucsx-A# connect nxos
Bad terminal type: "". Will assume vt100.
Cisco Nexus Operating System (NX-OS) Software
TAC support: http://www.cisco.com/tac
Copyright (C) 2002-2023, Cisco and/or its affiliates.
All rights reserved.
The copyrights to certain works contained in this software are
owned by other third parties and used and distributed under their own
licenses, such as open source.  This software is provided "as is," and unless
otherwise stated, there is no warranty, express or implied, including but not
limited to warranties of merchantability and fitness for a particular purpose.
Certain components of this software are licensed under
the GNU General Public License (GPL) version 2.0 or 
GNU General Public License (GPL) version 3.0  or the GNU
Lesser General Public License (LGPL) Version 2.1 or 
Lesser General Public License (LGPL) Version 2.0. 
A copy of each such license is available at
http://www.opensource.org/licenses/gpl-2.0.php and
http://opensource.org/licenses/gpl-3.0.html and
http://www.opensource.org/licenses/lgpl-2.1.php and
http://www.gnu.org/licenses/old-licenses/library.txt.
nsd5-static-ucsx-A(nx-os)# ?
  attach        Connect to a specific linecard
  clear         Reset functions
  cli           CLI commands
  debug         Debugging functions
  debug         Debug aclqos
  debug-filter  Enable filtering for debugging functions
  ethanalyzer   Configure cisco packet analyzer
  no            Negate a command or set its defaults
  ntp           NTP configuration
  poll-period   Stats poll period
  run           Execute/run debug shell
  show          Show running system information
  switchto      Goto specific Virtual Device Context <vdc-name> | <vdc-id>
  system        System management commands
  terminal      Set terminal line parameters
  test          Test command
  undebug       Disable Debugging functions (See also debug)
  vdc-all       For all active VDCs
  end           Go to exec mode
  exit          Exit from command interpreter
  pop           Pop mode from stack or restore from name
  push          Push current mode to stack or save it under name
  where         Shows the cli context you are in

nsd5-static-ucsx-A(nx-os)#   
```


### NXOS mode show commands
Below are the NXOS mode show commands for a 6400 series FI runnning firmware 4.2(3d)

```
nsd5-static-ucsx-A(nx-os)# show ?
  aaa                  Show aaa information
  access-lists         List access lists
  accounting           Show Accounting Information
  banner               Show current banner message
  boot                 Show boot information
  boot                 Show Bootvar Variables
  callhome             Show callhome information
  cdp                  Show Cisco Discovery Protocol information
  cfs                  CFS Show Command handler
  class-map            Show class maps
  cli                  Show CLI information
  clock                Display current Date
  cluster-state        View cluster state
  configuration        Show information about configuration sessions
  consistency-checker  Consistency Checker
  copyright            Copyright information
  debug                Show debug flags
  diagnostic           Diagnostic commands
  environment          System environment information
  fc2                  Show fc2 tables and statistics
  fcdroplatency        Show switch or network latency
  fcoe                 Show FCOE paramaters
  fctimer              Show Fibre Channel timers
  fex                  Show FEX information
  forwarding           Forwarding information
  hardware             Show hardware information
  hostname             Show the system's hostname
  hosts                Show information about DNS
  incompatibility      Show incompatible configurations
  install              Show the software install impact between two images
  interface            Show interface status and information
  inventory            System inventory information
  ip                   Display IP information
  ipv6                 Display IPv6 information
  l2                   Layer2 information
  l2protocol           Layer 2 Protocol
  l2rib                Layer 2 routing information base
  l2route              Layer 2 routing information base
  lacp                 LACP protocol
  ldap-server          Show LDAP configuration information
  line                 Show the line configuration
  lldp                 Show information about lldp
  locator-led          Blink locator led on device
  logging              Show logging configuration and contents of logfile
  mac                  MAC configuration commands
  module               Show module information
  monitor              Show Ethernet SPAN information
  npv                  Show information about NPV
  ntp                  Show NTP information
  pinning              End Node pinning command
  platform             Shows list of events received by Platform Manager
  policy-map           Show policy maps
  port                 Show port information
  port-channel         Configure port channel parameters
  port-profile         Show port-profile
  port-security        Port security related command
  queuing              Queuing related information
  radius-server        Show RADIUS configuration information
  redundancy           Show system redundancy status
  resource             Show resource configuration for VDC
  rmon                 Display RMON statistics
  role                 Show role configuration
  routing-context      Display the current routing context
  running-config       Show running system information
  san-port-channel     Show port-channel information
  scsi-target          Show discovered scsi target information
  service-pack         Service-pack related show commands
  snmp                 Show snmp information
  sprom                Show SPROM contents
  ssh                  Show SSH information
  startup-config       Show startup system information
  switchname           Show the system's hostname
  system               System-related show commands
  tacacs-server        Show TACACS+ configuration information
  tech-support         Gather information for troubleshooting
  telnet               Show telnet server configuration
  terminal             Display terminal configuration parameters
  track                Tracking information
  trunk                Show trunk information
  udld                 UDLD protocol
  user-account         Show user information
  users                Show the current users logged in the system
  vdc                  Show Virtual Device Contexts
  version              Show the software version
  vlan                 VLAN status
  vrf                  Display VRF information
  vsan                 Vsan commands
  wwn                  Show wwn information
  xml                  Xml agent

nsd5-static-ucsx-A(nx-os)# 
```

### Showing LDAP configuration
In nxos mode you can `show ldap` and it will show you the config

The example below is from a 6400 series FI running firmware 4.2(3d) with no LDAP configuration

```
nsd5-static-ucsx-A(nx-os)# show ldap
     timeout : 0
        port : 0
      baseDN : 
user profile attribute : 
search filter : 
  use groups : 0
recurse groups : 0
group attribute : 
total number of servers : 0
nsd5-static-ucsx-A(nx-os)#  
```


### Debugging LDAP and AAA authentication issues

At the CLI type these commands:

```
connect nxos
debug aaa all
debug ldap all
term mon 
```


Debug output example
```
sd5-static-ucsx-A(nx-os)# debug aaa all
Terminal monitor is currently disabled on this terminal.
 To observe Debugs/Syslogs, please run the command "terminal monitor"
nsd5-static-ucsx-A(nx-os)# term mon
nsd5-static-ucsx-A(nx-os)# 2026 Mar 13 11:27:26.426306 aaa: aaa_process_fd_set
2026 Mar 13 11:27:26.426327 aaa: aaa_process_fd_set: mtscallback on aaa_accounting_q
2026 Mar 13 11:27:26.426387 aaa: Src: 0x00000101/53232  Dst: 0x00000101/0  ID: 0x00E6EED1  Size: 48 [REQ] Opc: 151 (MTS_OPC_ACCOUNTING_INTERIM_UPDATE) RR: 0x00E6EED1  HA_SEQNO: 0x00000000  TS: Fri Mar 13 11:27:43 2026  at msecs 921  REJ:0  SYNC:1 OPTIONS:0x0 Trx Id: 0  
2026 Mar 13 11:27:26.426401 aaa: 73 74 61 72 73 68 69 70 40 70 74 73 2F 31 00 61  
2026 Mar 13 11:27:26.426410 aaa: 64 6D 69 6E 00 74 65 72 6D 69 6E 61 6C 20 6D 6F  
2026 Mar 13 11:27:26.426426 aaa: 6E 69 74 6F 72 20 28 53 55 43 43 45 53 53 29 00  
2026 Mar 13 11:27:26.426438 aaa: OLD OPCODE: accounting_interim_update
2026 Mar 13 11:27:26.426450 aaa: aaa_create_local_acct_req: user=admin, session_id=starship@pts/1, log=terminal monitor (SUCCESS) 
2026 Mar 13 11:27:26.426463 aaa: aaa_req_process for accounting. session no 0 
2026 Mar 13 11:27:26.426472 aaa: MTS request reference is NULL. LOCAL request 
2026 Mar 13 11:27:26.426479 aaa: Setting AAA_REQ_RESPONSE_NOT_NEEDED
2026 Mar 13 11:27:26.426487 aaa: aaa_req_process: DEBUG:  Directed SERVER IP is: 0, Server Name is :  
2026 Mar 13 11:27:26.426495 aaa: aaa_req_process: General AAA request from appln: default appln_subtype: default 
2026 Mar 13 11:27:26.426505 aaa: try_next_aaa_method
2026 Mar 13 11:27:26.426515 aaa: aaa_method_config: GET request for accounting default default 
2026 Mar 13 11:27:26.426535 aaa: got back the return value of aaa method configuration operation:no methods configured 
2026 Mar 13 11:27:26.426545 aaa: no methods configured for default default
2026 Mar 13 11:27:26.426552 aaa: no configuration available for this request 
2026 Mar 13 11:27:26.426558 aaa: try_fallback_method 
2026 Mar 13 11:27:26.426565 aaa: handle_req_using_method
2026 Mar 13 11:27:26.426571 aaa: local_method_handler 
2026 Mar 13 11:27:26.426578 aaa: aaa_local_accounting_msg
2026 Mar 13 11:27:26.426586 aaa: update:starship@pts/1:admin:terminal monitor (SUCCESS)
2026 Mar 13 11:27:26.426595 aaa: av list is null. No vsan id
2026 Mar 13 11:27:26.426763 aaa: Returning aaa_read_next_seqnum_for_logflash : 987386
2026 Mar 13 11:27:26.426779 aaa: logging into acc_handle
2026 Mar 13 11:27:26.426812 aaa: Written successfully to Logflash
2026 Mar 13 11:27:26.426823 aaa: Entering aaa_inc_seqnum_for_logflash
2026 Mar 13 11:27:26.426854 aaa: Returning aaa_read_next_seqnum_for_logflash : 987386
2026 Mar 13 11:27:26.426931 aaa: Exiting aaa_inc_seqnum_for_logflash
2026 Mar 13 11:27:26.426953 aaa: aaa_send_client_response for accounting. session->flags=254. aaa_resp->flags=0. 
2026 Mar 13 11:27:26.426962 aaa: response for accounting request of old library will be sent as SUCCESS 
2026 Mar 13 11:27:26.426968 aaa: response not needed for this request
2026 Mar 13 11:27:26.426975 aaa: AAA_REQ_FLAG_LOCAL_RESP  
2026 Mar 13 11:27:26.426981 aaa: aaa_cleanup_session 
2026 Mar 13 11:27:26.426987 aaa: aaa_req should be freed.  
2026 Mar 13 11:27:26.426995 aaa: Fall back method local succeeded   
```

