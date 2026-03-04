# Cisco UCS Manager VIC Configuration Guide, Release 4.3 - Cisco

| | |
|---|---|
| **URL Title** | Cisco UCS Manager VIC Configuration Guide, Release 4.3 - Cisco |
| **URL** | https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/VIC-Configuration-Guide/4-3/b-vic-configuration-guide-4-3.html |
| **Long URL** |  |
| **HTML Title** | Cisco UCS Manager VIC Configuration Guide, Release 4.3 |
| **Source file** | `ucs-docs-raw/html/b-vic-configuration-guide-4-3.html` |
| **File type** | HTML |
| **Fetched on** | 2026-03-04 12:47:56 |

---

## Page 1: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/VIC-Configuration-Guide/4-3/b-vic-configuration-guide-4-3.html

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

## Page 4: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/VIC-Configuration-Guide/4-3/b-vic-configuration-guide-4-3/m_guidelines-and-limitations.html

## Guidelines for Using SMB Direct support using RoCEv2

### General Guidelines and Limitations

* Cisco UCS Manager release 4.1.x and later releases support Microsoft SMB Direct with RoCEv2 on Microsoft Windows Server 2019 and later. Cisco recommends that you have all KB updates from Microsoft for your Windows Server release. See Windows Requirements. 

  
**Note** | 

* * *

RoCEv2 is not supported on Microsoft Windows Server 2016.

* * *  
  
---|---  
* Cisco recommends you check [UCS Hardware and Software Compatibility](https://ucshcltool.cloudapps.cisco.com/public/) specific to your Cisco UCS Manager release to determine support for Microsoft SMB Direct with RoCEv2 on Microsoft Windows. 
* Microsoft SMB Direct with RoCEv2 is supported only with Cisco UCS VIC 1400 Series, 14000 Series, and 15000 Series adapters. It is not supported with UCS VIC 1200 Series and 1300 Series adapters. SMB Direct with RoCEv2 is supported on all UCS Fabric Interconnects. 

  
**Note** | 

* * *

RoCEv1 is not supported with Cisco UCS VIC 1400 Series, Cisco UCS VIC 14000 Series, and Cisco UCS VIC 15000 Series.

* * *  
  
---|---  
* RoCEv2 configuration is supported only between Cisco adapters. Interoperability between Cisco adapters and third party adapters is not supported. 
* RoCEv2 supports two RoCEv2 enabled vNIC per adapter and four virtual ports per adapter interface, independent of SET switch configuration. 
* RoCEv2 cannot be used on the same vNIC interface as NVGRE, NetFlow, and VMQ features.
* Support for RoCEv2 protocol for Windows 2019 NDKPI mode 1 and mode 2, with both IPV4 and IPV6.
* RoCEv2-enabled vNIC interfaces must have the no-drop QoS system class enabled in Cisco UCS Manager. 
* The RoCE Properties queue pairs setting must for be a minimum of 4 queue pairs.
* Maximum number of queue pairs per adapter is 2048.
* The maximum number of memory regions per rNIC interface is 131072.
* Cisco UCS Manager does not support fabric failover for vNICs with RoCEv2 enabled. 
* SMB Direct with RoCEv2 is supported on both IPv4 and IPv6.
* RoCEv2 cannot be used with GENEVE offload.
* The QoS No Drop class configuration must be properly configured on upstream switches such as Cisco Nexus 9000 series switches. QoS configurations may vary between different upstream switches. 
* RoCEv2 cannot be used with usNIC.

### MTU Properties

* In older versions of the VIC driver, the MTU was derived from either a Cisco UCS Manager service profile or from the Cisco IMC vNIC MTU setting in non-cluster setup. This behavior changes on Cisco UCS VIC 1400 Series and later adapters, where MTU is controlled from the Windows OS Jumbo Packet advanced property. A value configured from Cisco UCS Manager or Cisco IMC has no effect. 
* The RoCEv2 MTU value is always power-of-two and the maximum limit is 4096.
* RoCEv2 MTU is derived from the Ethernet MTU.
* RoCEv2 MTU is the highest power-of-two that is less than the Ethernet MTU. For example:
* if the Ethernet value is 1500, then the RoCEv2 MTU value is 1024 
* if the Ethernet value is 4096, then the RoCEv2 MTU value is 4096 
* if the Ethernet value is 9000, then the RoCEv2 MTU value is 4096 

### Windows NDPKI Modes of Operation

* The implementation of Network Direct Kernel Provider Interface (NDPKI) supports two modes of operation: Mode 1 and Mode 2. Mode 1 and Mode 2 relate to the implementation of Network Direct Kernel Provider Interface (NDKPI): Mode 1 is native RDMA, and Mode 2 involves configuration for the virtual port with RDMA. Cisco does not support NDPKI Mode 3 operation. 
* The recommended default adapter policy for RoCEv2 Mode 1 is Win-HPN-SMBd . 
* The recommended default adapter policy for RoCEv2 Mode 2 is MQ-SMBd. 
* RoCEv2 enabled vNICs for Mode2 operation require the QoS host control policy set to full. 
* Mode 2 is inclusive of Mode 1: Mode 1 must be enabled to operate Mode 2.
* On Windows, the RoCEv2 interface supports MSI & MSIx interrupt modes. By default, it is in MSIx interrupt mode. Cisco recommends you avoid changing interrupt mode when the interface is configured with RoCEv2 properties. 

### Downgrade Limitations

Cisco recommends you remove the RoCEv2 configuration before downgrading to any non-supported RoCEv2 release. If the configuration is not removed or disabled, downgrade will fail.

---

## Page 5: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/VIC-Configuration-Guide/4-3/b-vic-configuration-guide-4-3/m-rdma-over-converged-ethernet--roce--version-2.html

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

## Page 6: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/VIC-Configuration-Guide/4-3/b-vic-configuration-guide-4-3/m-single-root-i-o-virtualization.html

## Enabling BIOS Parameters

### Before you begin

* Ensure your BIOS policy is set up with the following options:
* For Intel based servers, enable Intel VT for directed IO under Intel Directed IO tab. 
* For AMD based servers, enable IOMMU and SVM Mode under Processor tab and enable SR-IOV under LOM and PCIe Slots BIOS Settings tab. 

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