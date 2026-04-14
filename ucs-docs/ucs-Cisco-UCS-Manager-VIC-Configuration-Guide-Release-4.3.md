# Cisco UCS Manager VIC Configuration Guide, Release 4.3 - Cisco

| | |
|---|---|
| **URL Title** | Cisco UCS Manager VIC Configuration Guide, Release 4.3 - Cisco |
| **URL** | https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/VIC-Configuration-Guide/4-3/b-vic-configuration-guide-4-3.html |
| **Long URL** |  |
| **HTML Title** | Cisco UCS Manager VIC Configuration Guide, Release 4.3 |
| **Source file** | `ucs-docs-raw/html/b-vic-configuration-guide-4-3.html` |
| **File type** | HTML |
| **Fetched on** | 2026-04-13 13:30:25 |

---

## Page 1: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/VIC-Configuration-Guide/4-3/b-vic-configuration-guide-4-3.html

![Clear Contents of Search](/etc/designs/cdc/fw/i/ic_clear_gray.png)

---

## Page 2: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/VIC-Configuration-Guide/4-3/b-vic-configuration-guide-4-3/b_RoCE_Config_Guide_Test_preface_00.html

## Audience

This guide is intended primarily for data center administrators with responsibilities and expertise in one or more of the following: 

  * Server administration 

  * Storage administration 

  * Network administration 

  * Network security 


---

## Page 3: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/VIC-Configuration-Guide/4-3/b-vic-configuration-guide-4-3/m_overview-of-vic-configuration-guide.html

## Overview of VIC Configuration Guide 

A Cisco UCS network adapter can be installed to provide options for I/O consolidation and virtualization support. This guide contains configuration details on RDMA over Converged Ethernet version 2 (RoCEv2) and Single Root I/O Virtualization (SR-IOV). 

---

## Page 4: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/VIC-Configuration-Guide/4-3/b-vic-configuration-guide-4-3/m-rdma-over-converged-ethernet--roce--version-2.html

## Configuring RoCEv2 Modes 1 and 2 in Windows

Configuration of RoCEv2 on the Windows platform requires first configuring RoCEv2 Mode 1, then configuring RoCEv2 Mode 2. Modes 1 and 2 relate to the implementation of Network Direct Kernel Provider Interface (NDKPI): Mode 1 is native RDMA, and Mode 2 involves configuration for the virtual port with RDMA. 

To configure RoCEv2 mode 1, you must:

  * Configure a no-drop class in CoS System Class. By default, Platinum with CoS 5 is a default in Cisco UCS Manager.

  * Configure an Ethernet adapter policy for Mode 1 in Cisco UCS Manager.

  * Configure Mode 1 on the host system.


RoCEv2 Mode 1 must be configured before configuring Mode 2. 

To configure RoCEv2 mode 2, you will:

  * Either create an Ethernet VMQ connection policy for RoCEv2 or use the Cisco UCS Manager MQ-SMBd policy.


---

## Page 5: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/VIC-Configuration-Guide/4-3/b-vic-configuration-guide-4-3/m-single-root-i-o-virtualization.html

## Enabling BIOS Parameters

### Before you begin

  * You must have a BIOS policy that is already created with the following options enabled:

  * For Intel based servers, Intel VT for directed IO under Intel Directed IO tab. 

  * For AMD based servers, IOMMU and SVM Mode under Processor tab. 

To update BIOS options, see, [Cisco UCS Manager Server Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html). 

  * You must have a service profile already created for SR-IOV configuration. To create a Service Profile see [Cisco UCS Manager Server Management Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html). Once the Service Profile is created, follow the steps in this procedure to enable the BIOS policy. 


### Procedure

* * *

**Step 1** |  In the Navigation pane, click Servers.   
---|---  
**Step 2** |  Expand Servers > Service Profiles.   
**Step 3** |  Expand the node for the organization that includes the service profile for which you want to enable SR-IOV BIOS parameters.  If the system does not include multi-tenancy, expand the root node.   
**Step 4** |  Click the service profile for which you want to enable SR-IOV BIOS parameters.   
**Step 5** |  In the Work pane, click the Policies tab.   
**Step 6** |  On the Policies tab, expand BIOS Policy.   
**Step 7** |  From the BIOS Policy drop-down list, select the BIOS policy that you have created for SR-IOV configuration.  Ensure that the BIOS policy selected satisfies the pre-requisites for this procedure.  
**Step 8** |  Save changes and click Yes to reboot the server.   
  
* * *

---
