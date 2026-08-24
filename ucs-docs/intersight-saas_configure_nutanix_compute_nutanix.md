# Intersight SaaS Configure Nutanix Compute Only guide

| | |
|---|---|
| **URL Title** | Intersight SaaS Configure Nutanix Compute Only guide |
| **URL** | https://intersight.com/help/saas/configure/nutanix/compute_nutanix |
<<<<<<< HEAD
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260821153740774/docs/cloud/data/articles/features/nutanix/compute/configure/en/index.html |
| **HTML Title** | Document |
| **Source file** | `ucs-docs-raw/html/intersight-saas_configure_nutanix_compute_nutanix.html` |
| **File type** | HTML |
| **Fetched on** | 2026-08-24 09:16:15 |
=======
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260626102158280/docs/cloud/data/articles/features/nutanix/compute/configure/en/index.html |
| **HTML Title** | Document |
| **Source file** | `ucs-docs-raw/html/intersight-saas_configure_nutanix_compute_nutanix.html` |
| **File type** | HTML |
| **Fetched on** | 2026-06-30 16:42:34 |
>>>>>>> b54dc188455b65bee6c95ef06462b9c67adf0b3a

---

## Overview

Modern workloads require modern flexibility. Traditional hyperconverged solutions requires scaling compute and storage together. When you need to scale compute capacity without adding storage, Cisco Compute-only (CO) nodes provide that critical capability, empowering you to design clusters that match your exact requirements.

The Cisco compute-only node with Nutanix Cloud Platform (NCP) and Everpure FlashArray solution delivers a disaggregated infrastructure architecture that enables independent scaling of compute and storage resources. This solution combines industry-standard Cisco compute-only node servers running Nutanix AHV and AOS connected to external Everpure FlashArray. This architecture leverages Everpure's software-defined storage environment optimized for enterprise workloads. The FlashStack solution with Nutanix integration provides organizations with the agility to adapt infrastructure resources dynamically while maintaining reliability and performance.

**Key Benefits**

  * Independent Scalability: Scale compute and storage resources separately based on workload demands

  * Enterprise-Grade Protection: Built-in data protection and disaster recovery capabilities

  * Hybrid Cloud Ready: Seamlessly extend operations across on-premises and cloud environments

  * Investment protection: Enables using Nutanix Cloud Platform with existing external storage

****Attributes****| ****Cisco Compute-Only (CO) node connected to Everpure FlashArray****  
---|---  
Cisco Compute-Only nodes| Nutanix Foundation allocates the following minimum resources to the CVM:
  * CVM Logical Cores: 16
  * CPU Physical Cores per Socket: 16
  * vRAM (in GiB): 32  
M.2 boot drives with M.2 RAID controller (480GB is recommended)  
Storage protocol: NVMe over Fabrics (NVMeoF) over TCP  
<<<<<<< HEAD
25Gb Ethernet network connection recommended between Cisco Nutanix Compute cluster and Everpure FlashArray (10Gb will be supported)  
Minimum 3 CO nodes  
Hypervisor| AHV only  
Management| 
  * Intersight Managed Mode (IMM)
  * Intersight Standalone Mode (ISM)  
Everpure| FlashArray //X, //XL, and, //C  
=======
25Gb Ethernet network connection recommended between Cisco Nutanix Compute cluster and Pure Storage FlashArray (10Gb will be supported)  
Minimum 3 CO nodes  
Hypervisor| AHV only  
Management| Intersight Management Mode (IMM)  
Pure Storage| FlashArray //X, //XL, and, //C  
>>>>>>> b54dc188455b65bee6c95ef06462b9c67adf0b3a
Nutanix Cloud Platform Software| Supported Nutanix Software
  * Nutanix Cloud Infrastructure (NCI)
  * Nutanix Cloud Manager (NCM)
  * Nutanix Cloud Platform (NCP)
  * Nutanix Kubernetes Platform (NKP)  
Nutanix Licensing| Nutanix Cloud Infrastructure (NCI) licenses on a per-core basis.Nutanix Cloud Infrastructure - Compute (NCI-C) (2000 cores minimum)For more information about NCI licenses, refer to the NCI section in [Nutanix Cloud Platform Software Options](https://www.nutanix.com/products/cloud-platform/software-options)  
  
