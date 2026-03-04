# Intersight SaaS Configure Nutanix Compute Only guide

| | |
|---|---|
| **URL Title** | Intersight SaaS Configure Nutanix Compute Only guide |
| **URL** | https://intersight.com/help/saas/configure/nutanix/compute_nutanix |
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260225095216527/docs/cloud/data/articles/features/nutanix/compute/configure/en/index.html |
| **HTML Title** | Document |
| **Source file** | `ucs-docs-raw/html/intersight-saas_configure_nutanix_compute_nutanix.html` |
| **File type** | HTML |
| **Fetched on** | 2026-03-04 11:00:10 |

---

## Overview

Modern workloads require modern flexibility. Traditional hyperconverged solutions requires scaling compute and storage together. When you need to scale compute capacity without adding storage, Cisco Compute-Only (CO) nodes provide that critical capability, empowering you to design clusters that match your exact requirements.

The Cisco compute-only node with Nutanix Cloud Platform (NCP) and Pure Storage FlashArray solution delivers a disaggregated infrastructure architecture that enables independent scaling of compute and storage resources. This solution combines industry-standard Cisco compute-only node servers running Nutanix AHV and AOS connected to external Pure Storage FlashArray. This architecture leverages Pure software-defined storage environment optimized for enterprise workloads. The FlashStack solution with Nutanix integration provides organizations with the agility to adapt infrastructure resources dynamically while maintaining enterprise-level reliability and performance.

**Key Benefits**

  * Independent Scalability: Scale compute and storage resources separately based on workload demands

  * Enterprise-Grade Protection: Built-in data protection and disaster recovery capabilities

  * Hybrid Cloud Ready: Seamlessly extend operations across on-premises and cloud environments

  * Investment protection – enables using Nutanix Cloud Platform with existing external storage

****Attributes****| ****Cisco Compute-Only (CO) node connected to Pure Storage FlashArray****  
---|---  
Cisco Compute-Only nodes| Minimum total physical CPU core count per node - 24  
Minimum memory – 64GB  
M.2 boot drives with M.2 RAID controller (480GB is recommended)  
Storage protocol: NVMe over Fabrics (NVMeoF) over TCP  
25Gb Ethernet network connection recommended between Cisco Nutanix Compute cluster and Pure Storage FlashArray (10Gb will be supported)  
Minimum 5 CO nodes  
Hypervisor| AHV only  
Management| Intersight Management Mode (IMM)  
Pure Storage| FlashArray //X and FlashArray //XL  
Nutanix Cloud Platform Software| Supported Nutanix Software
  * Nutanix Cloud Infrastructure (NCI)
  * Nutanix Cloud Manager (NCM)
  * Nutanix Cloud Platform (NCP)
  * Nutanix Kubernetes Platform (NKP)  
Nutanix Licensing| Nutanix Cloud Infrastructure (NCI) licenses on a per-core basis.Nutanix Cloud Infrastructure - Compute (NCI-C) (2000 cores minimum)For more information about NCI licenses, see NCI section in [Nutanix Cloud Platform Software Options](https://www.nutanix.com/products/cloud-platform/software-options)  
  
