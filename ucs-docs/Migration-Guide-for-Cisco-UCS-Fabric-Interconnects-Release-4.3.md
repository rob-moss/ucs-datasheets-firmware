# Documentation: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Fabric-Interconnect-Migration/4-3_1/b_migration_guide_for_cisco_ucs_fabric_interconnects_4-3.html

*Fetched on: 2026-03-02 15:08:35*

---

## Page 1: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Fabric-Interconnect-Migration/4-3_1/b_migration_guide_for_cisco_ucs_fabric_interconnects_4-3.html

![Clear Contents of Search](/etc/designs/cdc/fw/i/ic_clear_gray.png)


---

## Page 2: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Fabric-Interconnect-Migration/4-3_1/b_migration_guide_for_cisco_ucs_fabric_interconnects_4-3/m-new-and-changed-information.html

## New and Changed Information for This Release

The following table provides an overview of the changes to this guide for Cisco UCS Manager, Release 4.3.

Table 1. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(6a) Feature  |  Description  |  Where Documented   
---|---|---  
Support for Cisco UCS C-Series and X-Series M8 servers |  Cisco UCS Manager now supports Cisco UCS C240 M8 Server, Cisco UCS C220 M8 Server, and Cisco UCS X210c M8 Compute Node.  |  [Cisco UCS Fabric Interconnect Server Compatibility Matrix - Release 4.3(6b)](m-migrating-and-upgrading-cisco-ucs-hardware-components-for-6500-series-fabric-interconnect_4_3.html#matrix)  
Table 2. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(5a) Feature  |  Description  |  Where Documented   
---|---|---  
Support for Cisco UCS C-Series M8 servers |  Cisco UCS Manager now supports Cisco UCS C225 M8 Server and Cisco UCS X215c M8 Compute Node.  |  [Cisco UCS Fabric Interconnect Server Compatibility Matrix - Release 4.3(6b)](m-migrating-and-upgrading-cisco-ucs-hardware-components-for-6500-series-fabric-interconnect_4_3.html#matrix)  
Table 3. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(4b) Feature  |  Description  |  Where Documented   
---|---|---  
Support for Cisco UCS Fabric Interconnects 9108 100G |  Cisco UCS Manager now supports Cisco UCS Fabric Interconnects 9108 100G (Cisco UCS X-Series Direct).  |  [Ports on the Cisco UCS Fabric Interconnects](m_overview-4-1.html#id_118320)  
Table 4. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(4b) Feature  |  Description  |  Where Documented   
---|---|---  
Support for Cisco UCS C-Series M8 servers |  Cisco UCS Manager now supports Cisco UCS C245 M8 Servers.  |  [Cisco UCS Fabric Interconnect Server Compatibility Matrix - Release 4.3(6b)](m-migrating-and-upgrading-cisco-ucs-hardware-components-for-6500-series-fabric-interconnect_4_3.html#matrix)  
Table 5. New Features and Changed Behavior in Cisco UCS Manager, Release 4.3(2b) Feature  |  Description  |  Where Documented   
---|---|---  
Migrating Cisco UCS 6400 Series Fabric Interconnects to Cisco UCS 6500 Series Fabric Interconnects |  Cisco UCS Manager supports migration of UCS 6400 series Fabric Interconnects to Cisco UCS 6536 Fabric Interconnect. | 

  * [Cisco UCS 6400 Series Fabric Interconnect Migration Considerations](m-migrating-and-upgrading-cisco-ucs-hardware-components-for-6500-series-fabric-interconnect_4_3.html#concept_vxm_lxc_zdb)
  * [Validating Feature Configurations for Cisco UCS 6536 before Upgrade](m-migrating-and-upgrading-cisco-ucs-hardware-components-for-6500-series-fabric-interconnect_4_3.html#Cisco_Concept.dita_b1378d74-eba6-45d0-86c5-e5013b19d78d)
  * [Migrating from UCS 6400 Series Fabric Interconnects to UCS 6536 Fabric Interconnects](m-migrating-and-upgrading-cisco-ucs-hardware-components-for-6500-series-fabric-interconnect_4_3.html#task_i25_zkc_zdb)

  
Migrating Cisco UCS 6400 Series Fabric Interconnects to Cisco UCS 6500 Series Fabric Interconnects with UCS Central |  Cisco UCS Manager supports migration of UCS 6400 series Fabric Interconnects to Cisco UCS 6536 Fabric Interconnects with UCS Central.  | 

  * [Considerations for migrating Cisco UCS 6400 Series Fabric Interconnects to Cisco UCS 6500 Series Fabric Interconnects with Cisco UCS Central](m-migrating-and-upgrading-cisco-ucs-hardware-components-for-6500-series-fabric-interconnect_4_3.html#considerations-for-6454-fi-to-64108-fi-migration-with-ucs-central)
  * [Validating Feature Configurations for Cisco UCS 6536 before Upgrade](m-migrating-and-upgrading-cisco-ucs-hardware-components-for-6500-series-fabric-interconnect_4_3.html#Cisco_Concept.dita_b1378d74-eba6-45d0-86c5-e5013b19d78d)
  * [Migrating from UCS 6400 Series Fabric Interconnects to UCS 6536 Fabric Interconnects](m-migrating-and-upgrading-cisco-ucs-hardware-components-for-6500-series-fabric-interconnect_4_3.html#task_i25_zkc_zdb)


---

## Page 3: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Fabric-Interconnect-Migration/4-3_1/b_migration_guide_for_cisco_ucs_fabric_interconnects_4-3/m_overview-4-1.html

##  Cisco UCS 6536 Fabric Interconnect Overview   
  
The Cisco UCS 6536 Fabric Interconnect is a core part of the Cisco Unified Computing System, providing both network connectivity and management capabilities for the system. The Cisco UCS 6536 Fabric Interconnect provides the communication backbone and management connectivity for UCS B-series blade servers and UCS C-series rack servers. 

Cisco UCS 6500 Series Fabric Interconnects currently include Cisco UCS 6536 Fabric Interconnect. All servers attached to a Cisco UCS 6536 Fabric Interconnect become part of a single, highly available management domain. In addition, by supporting a unified fabric, Cisco UCS 6536 Fabric Interconnect provides both LAN and SAN connectivity for all servers within its domain. 

The Cisco UCS 6536 Fabric Interconnect supports multiple traffic classes over a lossless Ethernet fabric from the server through the fabric interconnect. 


---

## Page 4: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Fabric-Interconnect-Migration/4-3_1/b_migration_guide_for_cisco_ucs_fabric_interconnects_4-3/m-migrating-and-upgrading-cisco-ucs-hardware-components-for-6500-series-fabric-interconnect_4_3.html

## Cisco UCS Fabric Interconnect Server Compatibility Matrix - Release 4.3(6b)

### Cisco UCS 6536 FI

Table 1. Cisco UCS 6536 FI - Cisco UCS Rack Servers Cisco VIC |  Direct Attach  (40/100G) |  Direct Attach  (4x25G or 25G QSA28) |  FEX  
---|---|---|---  
93180YC-FX3  (25G server ports) |  93180YC-FX3  (10G server ports) |  2348 UPQ  (10G server ports)  
15427 (UCSC-M-V5Q50GV2) |  Not Supported  |  All Cisco UCS C-Series M8, M7, and M6 servers. |  **Note** |  Reverse breakout is not supported.  
---|---  
All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M8, M7, and M6 servers.  
15237 (UCSC-M-V5D200GV2) |  All Cisco UCS C-Series M8, M7, and M6 servers. |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
15235 (UCSC-P-V5D200G)  |  All Cisco UCS C-Series M8, M7, and M6 servers. |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
15238 (UCSC-M-V5D200G)  |  All Cisco UCS C-Series M6 and M7 servers  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
15425 (UCSC-P-V5Q50G) |  Not Supported |  All Cisco UCS C-Series M8, M7, and M6 servers. |  **Note** |  No reverse breakout supported   
---|---  
All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M8, M7, and M6 servers.  
15428 (UCSC-M-V5Q50G)  |  Not Supported |  All Cisco UCS C-Series M6 and M7 servers  |  **Note** |  No reverse breakout supported   
---|---  
All Cisco UCS C-Series M6 and M7 servers  |  All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M6 and M7 servers   
1497-40G/100G (UCSC-MLOMC100-04)  |  All Cisco UCS C-series M5 servers. |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
1495-40G/100G (UCSC-PCIEC100-04)  |  All Cisco UCS C-Series M6, C-Series M5, and S-series M5 servers  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
1477-40G/100G (UCSC-MV100-04)  |  All Cisco UCS C-series M6 servers. |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
1467-10G/25G (UCSC-MV25-04)  |  Not Supported  |  All Cisco UCS C-Series M6 servers |  All Cisco UCS C-Series M6 servers |  All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M6 servers  
1457-10G/25G (UCSC-MLOMC25Q-04)  |  Not Supported  |  All Cisco UCS C-series M5 servers. |  All Cisco UCS C-series M5 servers. |  All Cisco UCS C-series M5 servers. |  All Cisco UCS C-series M5 servers.  
1455-10G/25G (UCSC-PCIEC25Q-04)  |  Not Supported  |  All Cisco UCS C-Series M6 and M5, and S-Series M5 servers. |  All Cisco UCS C-Series M6 and M5, and S-Series M5 servers. |  All Cisco UCS C-Series M6 and M5, and S-Series M5 servers. |  All Cisco UCS C-Series M6 and M5, and S-Series M5 servers.  
1387 - 40G (UCSC-MLOM-C40Q-03)  |  All Cisco UCS C-Series M5 Servers (40G)  |  Not Supported  |  Not Supported  |  All Cisco UCS C-Series M5 servers with QSA and SFP-10G-SR/LR, SFP-H10GB-CU1/3/5M, SFP-H10GB-ACU7M only. |  All Cisco UCS C-Series M5 servers with QSA and SFP-10G-SR only.  
1385 - 40G (UCSC-PCIE-C40Q-03)  |  All Cisco UCS C-Series M5 Servers (40G)  |  Not Supported  |  Not Supported  |  All Cisco UCS C-Series M5 servers with QSA and SFP-10G-SR/LR, SFP-H10GB-CU1/3/5M, SFP-H10GB-ACU7M only. |  All Cisco UCS C-Series M5 servers with QSA and SFP-10G-SR only.  
Table 2. Cisco UCS 6536 FI - Cisco UCS Blade Servers Cisco VIC |  IOM  
---|---  
2304v1/v2 & /2408 |  UCSX-I-9108-25G or UCSX-I-9108-100G  
15230 (UCSX-ML-V5D200GV2) |  - |  Cisco UCS X210c M8 Cisco UCS X215c M8 Cisco UCS X210c M6, X210c M7, and X410c M7  
15420 + UCS VIC 15000 bridge connector + 15422 (UCSX-ML-V5Q50G + UCSX-V5-BRIDGE + UCSX-ME-V5Q50G) |  \-  |  Cisco UCS X210c M8 Cisco UCS X215c M8 Cisco UCS X210c M6, X210c M7, and X410c M7  
15420 (UCSX-ML-V5Q50G)  |  \-  |  Cisco UCS X210c M8 Cisco UCS X215c M8 Cisco UCS X210c M6, X210c M7, and X410c M7  
15231 (UCSX-ML-V5D200G)  |  \-  |  Cisco UCS X210c M6, X210c M7, and X410c M7  
14425 + UCS VIC 14000 bridge connector + 14825 (UCSX-V4-Q25GML + UCSX-V4-BRIDGE + UCSX-V4-Q25GME) |  \-  |  Cisco UCS X210c M6   
14425 (UCSX-V4-Q25GML)  |  \-  |  Cisco UCS X210c M6   
15411 + Port Expander (UCSB-ML-V5Q10G + UCSB-MLOM-PT-01)  |  Cisco UCS B200 M6  |  \-   
15411 (UCSB-ML-V5Q10G)  |  Cisco UCS B200 M6  |  \-   
1440 + 1480 + Port Expander (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P + UCSB-MLOM-PT-01) |  Cisco UCS B480 M5  |  \-   
1440 + 1480 + 1480 (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P +UCSB-VIC-M84-4P)  |  Cisco UCS B480 M5  |  \-   
1440 + 1480 (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P)  |  Cisco UCS B200 M6, B200 M5, B480 M5  |  \-   
1440 + Port Expander (UCSB-MLOM-40G-04 + UCSB-MLOM-PT-01)  |  Cisco UCS B200 M6, B200 M5, B480 M5  |  \-   
1440 (UCSB-MLOM-40G-04)  |  Cisco UCS B200 M6, B200 M5, B480 M5  |  \-   
1340 + 1380 + Port Expander (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P + UCSB-MLOM-PT-01) |  Cisco UCS B480 M5  |  \-   
1340 + 1380 + 1380 (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P + UCSB-VIC-M83-8P) |  Cisco UCS B480 M5  |  \-   
1340 + 1380 (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P)  |  Cisco UCS B200 M5 and B480 M5  |  \-   
1340 + Port Expander - 10G/40G (UCSB-MLOM-40G-03 + UCSB-MLOM-PT-01)  |  Cisco UCS B200 M5 and B480 M5  |  \-   
1340 - 10G/40G (UCSB-MLOM-40G-03)  |  Cisco UCS B200 M5 and B480 M5  |  \-   
  
### Cisco UCS 6400 and 64108 FIs

Table 3. Cisco UCS 6400 and 64108 FIs - Cisco UCS Rack Servers Cisco VIC |  Direct Attach  (10G/25G)  |  Direct Attach  (4x10G/4x25)  |  Direct Attach  (40G/100G)  |  FEX  
---|---|---|---|---  
2232 PP (10G)  |  93180YC-FX3  (25G server ports)  |  93180YC-FX3  (10G server ports)   
15427 (UCSC-M-V5Q50GV2) |  All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M8, M7, and M6 servers. |  Not Supported |  Not Supported |  All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M8, M7, and M6 servers with SFP-10G-SR/SR-S only.  
15237 (UCSC-M-V5D200GV2) |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
15235 (UCSC-P- V5D200G) |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
15238 (UCSC-M -V5D200G)  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
15425 (UCSC-P- V5Q50G) |  All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M8, M7, and M6 servers. |  Not Supported  |  Not Supported  |  All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M8, M7, and M6 servers with SFP-10G-SR/SR-S only.  
15428 (UCSC-M -V5Q50G)  |  All Cisco UCS C-Series M6 and M7 servers. |  All Cisco UCS C-Series M6 and M7 servers. |  Not Supported  |  Not Supported  |  All Cisco UCS C-Series M6 and M7 servers. |  All Cisco UCS C-Series M8, M7, and M6 servers with SFP-10G-SR/SR-S only.  
|  **Note** |  Break-out is supported (6400 side QSFP, on adapter side two ports can be connected to 1 VIC ( like ports 1 and 2) Reverse-breakout : Not supported  
---|---  
1495-40G/100G  (UCSC -PCIEC100 -04)  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
1497-40G/100G  (UCSC -MLOMC100 -04)  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
1477-40G/100G  (UCSC-MV100 -04)  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
1467-10G/25G (UCSC -MV25-04)  |  All Cisco UCS C-Series M6 servers. |  All Cisco UCS C-Series M6 servers. |  Not Supported  |  All Cisco UCS C-Series M6 servers. |  All Cisco UCS C-Series M6 servers. |  All Cisco UCS C-Series M6 servers with SFP-10G-SR/SR-S only.  
1457-10G/25G (UCSC-MLOM C25Q-04)  |  All Cisco UCS C-Series M5 servers. |  All Cisco UCS C-Series M5 servers. |  Not Supported  |  All Cisco UCS C-Series M5 servers. |  All Cisco UCS C-Series M5 servers. |  All Cisco UCS C-Series M5 servers with SFP-10G-SR/SR-S only.  
1455-10G/25G  (UCSC-PCIEC 25Q-04)  |  All Cisco UCS C-Series M6 and M5, and S-Series M5 servers. |  All Cisco UCS C-Series M6 and M5, and S-Series M5 servers. |  Not Supported  |  All Cisco UCS C-Series M6 and M5, and S-Series M5 servers. |  All Cisco UCS C-Series M6 and M5, and S-Series M5 servers. |  All Cisco UCS C-Series M6 and M5, and S-Series M5 servers with SFP-10G-SR/SR-S only.  
1387 - 40G  (UCSC-MLOM -C40Q-03)  |  All Cisco UCS C-Series M5 servers with QSA at adapter. |  Not Supported  |  Not Supported  |  All Cisco UCS C-Series M5 servers with QSA at adapter. |  Not Supported  |  All Cisco UCS C-Series M5 servers  with QSA and SFP-10G-SR/LR, SFP-H10GB-CU1/3/5M, or SFP-H10GB-ACU7M only.  
1385 - 40G  (UCSC-PCIE -C40Q-03)  |  All Cisco UCS C-Series M5 except C125 M5 and S-Series M5 servers  with QSA at the adapter. |  Not Supported  |  Not Supported  |  All Cisco UCS C-Series M5 except C125 M5 and S-Series M5 servers  with QSA at the adapter. |  Not Supported  |  All Cisco UCS C-Series M5 except C125 M5 and S-Series M5 servers  with QSA and SFP-10G-SR/LR, SFP-H10GB-CU1/3/5M, or SFP-H10GB-ACU7M only.  
Table 4. Cisco UCS 6400 and 64108 FIs - Cisco UCS Blade Servers Cisco VIC |  IOM  
---|---  
2204/2208/2408 |  UCSX-I-9108-25G  
15230 (UCSX-ML-V5D200GV2) |  Not Supported  |  Cisco UCS X210c M8 Cisco UCS X215c M8 Cisco UCS X210c M6, X210c M7, and X410c M7  
15420 +  UCS VIC 15000 bridge connector +  (15422 (UCSX-ML-V5Q50G + UCSX-V5-BRIDGE + UCSX-ME-V5Q50G) |  Not Supported  |  Cisco UCS X210c M8 Cisco UCS X215c M8 Cisco UCS X210c M6, X210c M7, and X410c M7  
15420  (UCSX-ML-V5Q50G) |  Not Supported  |  Cisco UCS X210c M8 Cisco UCS X215c M8 Cisco UCS X210c M6, X210c M7, and X410c M7  
15231  (UCSX-ML-V5D200G) |  Not Supported  |  Cisco UCS X210c M6, X210c M7, and X410c M7  
14425 +  UCS VIC 14000 bridge connector + (14825 (UCSX-V4-Q25GML + UCSX-V4-BRIDGE + UCSX-V4-Q25GME) |  Not Supported  |  Cisco UCS X210c M6  
14425  (UCSX-V4-Q25GML) |  Not Supported  |  Cisco UCS X210c M6  
15411 + Port Expander (UCSB-ML -V5Q10G + UCSB-MLOM -PT-01)  |  B200 M6  |  Not Supported   
15411 (UCSB-ML -V5Q10G)  |  B200 M6  |  Not Supported   
1440 + 1480 + Port Expander  (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P + UCSB-MLOM-PT-01) |  Cisco UCS B480 M5  |  Not Supported   
1440 + 1480 + Port Expander  (UCSB-MLOM-40G-04 +  UCSB-VIC- M84-4P) +  UCSB-MLOM-PT-01) |  Cisco UCS B480 M5  |  Not Supported   
1440 + 1480  (UCSB-MLOM-40G-04 +  UCSB-VIC-M84-4P)  |  Cisco UCS B200 M6, B200 M5, B480 M5  |  Not Supported   
1440 + Port Expander  (UCSB-MLOM-40G-04 +  UCSB-MLOM-PT-01)  |  Cisco UCS B200 M6, B200 M5, B480 M5  |  Not Supported   
1440  (UCSB-MLOM-40G-04)  |  Cisco UCS B200 M6, B200 M5, B480 M5  |  Not Supported   
1340 + 1380 + 1380  (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P + UCSB-VIC-M83-8P) |  Cisco UCS B480 M5  |  Not Supported  
1340 + 1380 + Port Expander  (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P + UCSB-MLOM-PT-01) |  Cisco UCS B480 M5  |  Not Supported  
1340 + Port Expander - 10G/40G  (UCSB-MLOM-40G-03 +  UCSB-MLOM-PT-01)  |  Cisco UCS B200 M5 and B480 M5  |  Not Supported  
1340 + 1380  (UCSB-MLOM-40G-03 +  UCSB-VIC-M83-8P)  |  Cisco UCS B200 M5 and B480 M5  |  Not Supported  
1340 - 10G/40G (UCSB-MLOM-40G-03)  |  Cisco UCS B200 M5 and B480 M5  |  Not Supported  
  
### Cisco UCS 6300 FI

Table 5. Cisco UCS 6300 FI - Cisco UCS Rack Servers Cisco VIC |  Direct Attach |  Direct Attach  (Break-out) |  FEX  
---|---|---|---  
2232 PP |  2348  
15427 (UCSC-M-V5Q50GV2) |  All Cisco UCS C-Series M6 servers. |  All Cisco UCS C-Series M6 servers. |  Not Supported  |  All Cisco UCS C-Series M6 servers.  
15237 (UCSC-M-V5D200GV2) |  All Cisco UCS C-Series M6 servers. |  Not Supported  |  Not Supported  |  Not Supported   
15235 (UCSC-P-V5D200G) |  All Cisco UCS C-Series M6 servers. |  Not Supported  |  Not Supported  |  Not Supported   
15425 (UCSC-P-V5Q50G) |  All Cisco UCS C-Series M6 servers. |  All Cisco UCS C-Series M6 servers. |  Not Supported  |  All Cisco UCS C-Series M6 servers.  
15428 (UCSC-M-V5Q50G)  |  All Cisco UCS C-Series M6 servers. |  All Cisco UCS C-Series M6 servers. |  Not Supported  |  All Cisco UCS C-Series M6 servers.  
15238 (UCSC-M-V5D200G)  |  All Cisco UCS C-Series M6 servers. |  Not Supported  |  Not Supported  |  Not Supported   
1497-40G/100G (UCSC-MLOMC100-04)  |  All Cisco UCS C-Series M5 servers. |  Not Supported  |  Not Supported  |  Not Supported   
1495-40G/100G (UCSC-PCIEC100-04)  |  All Cisco UCS C-Series M6, M5, and S-Series M5 servers. |  Not Supported  |  Not Supported  |  Not Supported   
1477-40G/100G (UCSC-MV100-04)  |  All Cisco UCS C-Series M6 servers. |  Not Supported  |  Not Supported  |  Not Supported   
1467-10G/25G (UCSC-MV25-04)  |  All Cisco UCS C-Series M6 servers (10G speed with 6332-16UP). |  All Cisco UCS C-Series M6 servers. |  All Cisco UCS C-Series M6 servers. |  All Cisco UCS C-Series M6 servers.  
1457-10G/25G (UCSC-MLOMC25Q-04)  |  Cisco UCS C220 M5 and C240 M5 (10G speed with 6332-16UP). |  Cisco UCS C220 M5 and C240 M5 servers. |  Cisco UCS C220 M5 and C240 M5 servers. |  Cisco UCS C220 M5 and C240 M5 servers.  
1455-10G/25G (UCSC-PCIEC25Q-04)  |  All Cisco UCS C-Series M6, M5, and S-Series M5 servers (10G speed with 6332-16UP). |  All Cisco UCS C-Series M6, M5, and S-Series M5 servers. |  All Cisco UCS C-Series M6, M5, and S-Series M5 servers. |  All Cisco UCS C-Series M6, M5, and S-Series M5 servers.  
1387 - 40G (UCSC-MLOM-C40Q-03)  |  All Cisco UCS C-Series M5 servers (40G or 10G using QSA) |  Not Supported  |  All Cisco UCS C-Series M5 servers (QSA at adapter)  |  All Cisco UCS C-Series M5 servers (QSA at adapter)   
1385 - 40G (UCSC-PCIE-C40Q-03)  |  All Cisco UCS C-Series M5 servers (except UCS C125 M5) and S-Series M5 servers (40G or 10G using QSA) |  Not Supported  |  All Cisco UCS C-Series M5 servers (except UCS C125 M5) and S-Series M5 servers (40G or 10G using QSA) |  All Cisco UCS C-Series M5 servers (except UCS C125 M5) and S-Series M5 servers (40G or 10G using QSA)  
Table 6. Cisco UCS 6300 FI - Cisco UCS Blade Servers Cisco VIC |  IOM  
---|---  
2304v1/v2 2204/2208  
15411 + Port Expander  (UCSB-ML-V5Q10G + UCSB-MLOM-PT-01)  |  Cisco UCS B200 M6   
15411 (UCSB-ML-V5Q10G)  |  Cisco UCS B200 M6   
1440 + 1480 + 1480  (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P + UCSB-VIC-M84-4P) |  Cisco UCS B480 M5   
1440 + 1480 + Port Expander (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P + UCSB-MLOM-PT-01) |  Cisco UCS B480 M5   
1440 + 1480 (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P)  |  Cisco UCS B200 M5, B480 M5 and B200 M6 servers   
1440 + Port Expander (UCSB-MLOM-40G-04 + UCSB-MLOM-PT-01)  |  Cisco UCS B200 M5, B480 M5 and B200 M6 servers   
1440 (UCSB-MLOM-40G-04)  |  Cisco UCS B200 M5, B480 M5 and B200 M6 servers   
1340 + 1380 + 1380  (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P +  UCSB-VIC-M83-8P) |  Cisco UCS B480 M5   
1340 + 1380 + Port Expander  (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P +  UCSB-MLOM-PT-01) |  Cisco UCS B480 M5   
1340 + Port Expander - 10G/40G (UCSB-MLOM-40G-03 + UCSB-MLOM-PT-01)  |  Cisco UCS B200 M5 and B480 M5 servers   
1340 + 1380 (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P)  |  Cisco UCS B200 M5 and B480 M5 servers   
1340 - 10G/40G (UCSB-MLOM-40G-03)  |  Cisco UCS B200 M5 and B480 M5 servers   
  
### Cisco UCS 6324 FI

Table 7. Cisco UCS 6324 FI - Cisco UCS Rack Servers Cisco VIC |  Direct Attach (10G)  |  Direct Attach  (Break-out)  
---|---|---  
15428 (UCSC-M-V5Q50G)  |  Not Supported  |  Not Supported   
15238 (UCSC-M-V5D200G)  |  Not Supported  |  Not Supported   
1497-40G/100G (UCSC-MLOMC100-04)  |  Not Supported  |  Not Supported   
1495-40G/100G (UCSC-PCIEC100-04)  |  Not Supported  |  Not Supported   
1477-40G/100G (UCSC-MV100-04)  |  Not Supported  |  Not Supported   
1467-10G/25G (UCSC-MV25-04)  |  Not Supported  |  Not Supported   
1457-10G/25G (UCSC-MLOMC25Q-04)  |  Cisco UCS C220 M5 and C240 M5 servers. |  Cisco UCS C220 M5 and C240 M5 servers.  
1455-10G/25G (UCSC-PCIEC25Q-04)  |  All Cisco UCS C-Series and S-Series M5 servers. |  All Cisco UCS C-Series and S-Series M5 servers.  
1387 - 40G (UCSC-MLOM-C40Q-03)  |  All Cisco UCS C-Series M5 servers. (QSA at the adapter) |  Not Supported   
1385 - 40G (UCSC-PCIE-C40Q-03)  |  All Cisco UCS C-Series M5 servers. (QSA at the adapter) |  Not Supported   
Table 8. Cisco UCS 6324 FI - Cisco UCS Blade Servers Cisco VIC |  IOM |  6324 (Primary Chassis)  
---|---|---  
2204/2208  
15411 (UCSB-ML-V5Q10G)  |  Not Supported  |  Not Supported   
15411 + Port Expander (UCSB-ML-V5Q10G + UCSB-MLOM-PT-01)  |  Not Supported  |  Not Supported   
1440 + 1480 + 1480 (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P +UCSB-VIC-M84-4P)  |  Not Supported  |  Cisco UCS B480 M5  
1440 + 1480 + Port Expander (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P) + UCSB-MLOM-PT-01) |  Not Supported  |  Cisco UCS B480 M5  
1440 + 1480 (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P)  |  Not Supported  |  Cisco UCS B200 M5, B480 M5, and B200 M6  
1440 + Port Expander (UCSB-MLOM-40G-04 + UCSB-MLOM-PT-01)  |  Not Supported  |  Cisco UCS B200 M5, B480 M5, and B200 M6  
1440 (UCSB-MLOM-40G-04)  |  Not Supported  |  Cisco UCS B200 M5, B480 M5, and B200 M6  
1340 + 1380 + 1380  (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P +  UCSB-VIC-M83-8P) |  Cisco UCS B480 M5  |  Cisco UCS B480 M5   
1340 + 1380 + Port Expander  (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P +  UCSB-MLOM-PT-01) |  Cisco UCS B480 M5  |  Cisco UCS B480 M5   
1340 + 1380  (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P)  |  Cisco UCS B200 M5 and B480 M5  |  Cisco UCS B200 M5 and B480 M5   
1340 + Port Expander - 10G/40G  (UCSB-MLOM-40G-03 + UCSB-MLOM-PT-01)  |  Cisco UCS B200 M5 and B480 M5  |  Cisco UCS B200 M5 and B480 M5   
1340 - 10G/40G (UCSB-MLOM-40G-03)  |  Cisco UCS B200 M5 and B480 M5  |  Cisco UCS B200 M5 and B480 M5   
  
### Cisco UCS Fabric Interconnect 9108 100G

Table 9. Cisco UCS FI 9108 100G - Cisco UCS Blade Servers Cisco VIC |  UCSX-S9108-100G (Primary Chassis)  
---|---  
14425 (UCSX-V4-Q25GML) |  Cisco UCS X210c M6  
14425 + UCS VIC 14000 bridge connector + 14825  (UCSX-V4-Q25GML + UCSX-V4-BRIDGE +  UCSX-V4-Q25GME) |  Cisco UCS X210c M6  
15231 (UCSX-ML-V5D200G) |  Cisco UCS X410c M7, X210c M7, X210c M6  
15230 (UCSX-ML-V5D200GV2) |  Cisco UCS X210c M8, X215c M8, X410c M7, X210c M7, and X210c M6   
15420 (UCSX-ML-V5Q50G) |  Cisco UCS X210c M8, X215c M8, X410c M7, X210c M7, and X210c M6   
15420 + UCS VIC 15000 bridge connector + 15422  (UCSX-ML-V5Q50G + UCSX-V5-BRIDGE +  UCSX-ME-V5Q50G) |  Cisco UCS X210c M8, X215c M8, X410c M7, X210c M7, and X210c M6 


---

## Page 5: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Fabric-Interconnect-Migration/4-3_1/b_migration_guide_for_cisco_ucs_fabric_interconnects_4-3/m_migrating_from_6200_to_64108.html

## Cisco UCS 6400 Series Fabric Interconnect Migration Considerations  
  
Cisco UCS Manager provides support for migrating Cisco UCS 6454 Fabric Interconnect to Cisco UCS 64108 Fabric Interconnect with B-Series servers, C-Series, or S-Series servers. 

To migrate from Cisco UCS 6454 Fabric Interconnect to Cisco UCS 64108 Fabric Interconnect, both the Fabric Interconnect must be loaded with the same Infrastructure Firmware version. 

Prerequisites

Before performing the migration from Cisco UCS 6454 Fabric Interconnects to Cisco UCS 64108 Fabric Interconnect, ensure that the following prerequisites are met for a successful migration: 

  * Back up and export Cisco UCS Manager configuration before initiating the upgrade.

  * Take an inventory of the Cisco UCS domain and remove any unsupported hardware.

  * Ensure to enable the cluster failover.

  * Do not attempt to implement new software features from the new Cisco UCS software version until all required hardware is installed. 

  * Make sure both Cisco UCS 6400 series Fabric Interconnects are on the same UCSM build before migration.

  * Standalone installations should expect down time. In a cluster configuration, migrating the Fabric Interconnects can result in a small traffic disruption when the traffic fails over from one Fabric Interconnect to another. To avoid that there is no permanent traffic loss during migration, ensure that there is redundancy in the UCS domain on both Fabric Interconnects before migration and test the redundancy before starting the migration. 

  * Ensure the latest firmware bundle is downloaded and upgraded through GUI or CLI. Incase of attempting to upgrade the firmware bundle using other methods (loader prompt/erase configuration) can result in missing package version. 

  * Before migration, make sure that the FC Speed is 8Gbps on Cisco UCS 6454 Fabric Interconnects or the connected switch supports 8Gbps speed. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

Post migration, you can configure the FC Port (Scalability Port) speed on Cisco UCS 64108 Fabric Interconnects.

* * *  
  
---|---  
  * Migrating to different IOM models can result in peer communication issue between IOMs of the Primary and Secondary Fabric Interconnects. 

  * Make a detailed record of the cabling between FEX and fabric interconnects. You must preserve the physical port mapping to maintain the server pinning already configured and minimize down time. 

  * For a cluster configuration, both fabric interconnects must have symmetrical connection topologies between fabric interconnect and FEX. 

  * Use the same speed cables on all the adapter ports that are connected to same Fabric Interconnect. Cisco UCS VIC adapter ports connected to Cisco UCS 64108 fabric interconnect through a mix of 10G and 25G cables can result in UCS rack-mount server discovery failure and ports moving to suspended state. 

  * A WWN pool can include only WWNNs or WWPNs in the ranges from 20:00:00:00:00:00:00:00 to 20:FF:00:FF:FF:FF:FF:FF or from 50:00:00:00:00:00:00:00 to 5F:FF:00:FF:FF:FF:FF:FF. All other WWN ranges are reserved. When fibre channel traffic is sent through the UCS infrastructure the source WWPN is converted to a MAC address. You cannot use WWPN pool which can translate to source multicast MAC addresses. To ensure the uniqueness of the Cisco UCS WWNNs and WWPNs in the SAN fabric, Cisco recommends using the following WWN prefix for all blocks in a pool: 20:00:00:25:B5:XX:XX:XX 


Recommendations

Following are the best practices for a successful migration:

  * For minimal disruption during migration, ensure that there is redundancy for Ethernet and FC traffic from the servers in the UCS domain across both 6454 Fabric Interconnects before migration. 

  * Changes to the topology, such as the number of servers or uplink connections, should be performed after the fabric interconnect migration is complete. 

  * During the migration of Fabric Interconnects, ensure the Cluster ID is not changed.

  * During the migration, image synchronization between fabric interconnects is not allowed. This is done to prevent incompatible images from getting synchronized. It is necessary to download B-Series, C-Series, and S-Series server software bundles again after migration is complete. 

  * Unconfigure the fibre channel ports on the migrating subordinate Cisco UCS 6454 Fabric Interconnect and reconfigure on the Cisco UCS 64108 Fabric Interconnect. 

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For more information on migrating Cisco UCS 6454 Fabric Interconnect to Cisco UCS 64108 Fabric Interconnect with UCS Central, see Considerations for migrating Cisco UCS 6454 Fabric Interconnects to Cisco UCS 64108 Fabric Interconnects with Cisco UCS Central. 

* * *  
  
---|---  


### Validating Feature Configurations for Cisco UCS 64108 Fabric Interconnect before Upgrade

Table 1. Features that needs special attention prior to upgrading Feature |  Remediation  
---|---  
Chassis and fabric extender I/O port channel |  Select a port channel to the I/O module (IOM).  
Multicast optimization |  Verify that multicast optimization is not enabled under the LAN quality-of-service (QoS) system classes  
Fabric forwarding mode for Ethernet |  Verify that the Ethernet forwarding mode is set to End Host Mode Only.   
Fabric forwarding mode for Fibre Channel |  Verify that Fibre Channel forwarding mode is set to End Host Mode or FC Switching Mode.   
Cisco NetFlow |  Unconfigure NetFlow.  
MAC Security  |  Select Allow for MAC security.   
VM-FEX |  Remove port profiles and Cisco UCS Manager ESXi or SCVMM related configurations.  
Dynamic vNIC connection policies |  Set the dynamic vNIC connection policy in the vNIC profile to Not set.   
Cisco Switched Port Analyzer (SPAN) |  Use receive (RX) direction only. The installer will change SPAN to the RX direction and send an alert indicating that this setting is being changed.   
  
Failure to comply with these remediation steps will result in a migration warning alert during the migration process and prevent the fabric interconnects from synchronizing. 

### Considerations for migrating Cisco UCS 6454 Fabric Interconnects to Cisco UCS 64108 Fabric Interconnects with Cisco UCS Central

In addition to Cisco UCS 6400 Series Fabric Interconnect Migration Considerations, consider the following prerequisites when migrating with Cisco UCS Central: 

  * Before initiating the migration, ensure to have a complete backup of Cisco UCS Manager and UCS Central configurations.

  * To avoid any configuration issues during migration, make sure the following policies on Policy Resolution Control is set to Local in Cisco UCS Manager: 

  * Infrastructure and Catalog Firmware Policy

  * Equipment Policy

  * Port Configuration Policy


---

## Page 6: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Fabric-Interconnect-Migration/4-3_1/b_migration_guide_for_cisco_ucs_fabric_interconnects_4-3/m-appendix.html

## Appendix

This section provides a list of terminologies that are used in this document.

Name | Description  
---|---  
Direct-Connect  |  C-Series VIC connections that are plugged directly into the Fabric Interconnect port.  
Ethernet Port |  A generic term for the opening on the side of any Ethernet node, typically in an Ethernet NIC or LAN switch, into which an Ethernet cable can be connected.   
Fabric Port Channel |  Fibre Channel uplinks defined in a Cisco UCS Fabric Interconnect, bundled together and configured as a port channel, allowing increased bandwidth and redundancy.   
FCoE |  Fibre Channel over Ethernet. A computer network technology that encapsulates Fibre Channel frames over Ethernet networks.   
KVM |  Keyboard, video, and mouse  
MAC address |  A standardized data link layer address that is required for every device that connects to a Logical Area Network (LAN).   
Port Mappings |  Identifies the ports that are used for specific cable connections between the Fabric Interconnect and other devices.


---

## Page 7: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Fabric-Interconnect-Migration/4-3_1/m-migrating-and-upgrading-cisco-ucs-hardware-components-for-6500-series-fabric-interconnect_4_3.html

## Cisco UCS Fabric Interconnect Server Compatibility Matrix - Release 4.3(6b)  
  
### Cisco UCS 6536 FI

Table 1. Cisco UCS 6536 FI - Cisco UCS Rack Servers Cisco VIC |  Direct Attach  (40/100G) |  Direct Attach  (4x25G or 25G QSA28) |  FEX  
---|---|---|---  
93180YC-FX3  (25G server ports) |  93180YC-FX3  (10G server ports) |  2348 UPQ  (10G server ports)  
15427 (UCSC-M-V5Q50GV2) |  Not Supported  |  All Cisco UCS C-Series M8, M7, and M6 servers. |  **Note** |  Reverse breakout is not supported.  
---|---  
All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M8, M7, and M6 servers.  
15237 (UCSC-M-V5D200GV2) |  All Cisco UCS C-Series M8, M7, and M6 servers. |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
15235 (UCSC-P-V5D200G)  |  All Cisco UCS C-Series M8, M7, and M6 servers. |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
15238 (UCSC-M-V5D200G)  |  All Cisco UCS C-Series M6 and M7 servers  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
15425 (UCSC-P-V5Q50G) |  Not Supported |  All Cisco UCS C-Series M8, M7, and M6 servers. |  **Note** |  No reverse breakout supported   
---|---  
All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M8, M7, and M6 servers.  
15428 (UCSC-M-V5Q50G)  |  Not Supported |  All Cisco UCS C-Series M6 and M7 servers  |  **Note** |  No reverse breakout supported   
---|---  
All Cisco UCS C-Series M6 and M7 servers  |  All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M6 and M7 servers   
1497-40G/100G (UCSC-MLOMC100-04)  |  All Cisco UCS C-series M5 servers. |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
1495-40G/100G (UCSC-PCIEC100-04)  |  All Cisco UCS C-Series M6, C-Series M5, and S-series M5 servers  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
1477-40G/100G (UCSC-MV100-04)  |  All Cisco UCS C-series M6 servers. |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
1467-10G/25G (UCSC-MV25-04)  |  Not Supported  |  All Cisco UCS C-Series M6 servers |  All Cisco UCS C-Series M6 servers |  All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M6 servers  
1457-10G/25G (UCSC-MLOMC25Q-04)  |  Not Supported  |  All Cisco UCS C-series M5 servers. |  All Cisco UCS C-series M5 servers. |  All Cisco UCS C-series M5 servers. |  All Cisco UCS C-series M5 servers.  
1455-10G/25G (UCSC-PCIEC25Q-04)  |  Not Supported  |  All Cisco UCS C-Series M6 and M5, and S-Series M5 servers. |  All Cisco UCS C-Series M6 and M5, and S-Series M5 servers. |  All Cisco UCS C-Series M6 and M5, and S-Series M5 servers. |  All Cisco UCS C-Series M6 and M5, and S-Series M5 servers.  
1387 - 40G (UCSC-MLOM-C40Q-03)  |  All Cisco UCS C-Series M5 Servers (40G)  |  Not Supported  |  Not Supported  |  All Cisco UCS C-Series M5 servers with QSA and SFP-10G-SR/LR, SFP-H10GB-CU1/3/5M, SFP-H10GB-ACU7M only. |  All Cisco UCS C-Series M5 servers with QSA and SFP-10G-SR only.  
1385 - 40G (UCSC-PCIE-C40Q-03)  |  All Cisco UCS C-Series M5 Servers (40G)  |  Not Supported  |  Not Supported  |  All Cisco UCS C-Series M5 servers with QSA and SFP-10G-SR/LR, SFP-H10GB-CU1/3/5M, SFP-H10GB-ACU7M only. |  All Cisco UCS C-Series M5 servers with QSA and SFP-10G-SR only.  
Table 2. Cisco UCS 6536 FI - Cisco UCS Blade Servers Cisco VIC |  IOM  
---|---  
2304v1/v2 & /2408 |  UCSX-I-9108-25G or UCSX-I-9108-100G  
15230 (UCSX-ML-V5D200GV2) |  - |  Cisco UCS X210c M8 Cisco UCS X215c M8 Cisco UCS X210c M6, X210c M7, and X410c M7  
15420 + UCS VIC 15000 bridge connector + 15422 (UCSX-ML-V5Q50G + UCSX-V5-BRIDGE + UCSX-ME-V5Q50G) |  \-  |  Cisco UCS X210c M8 Cisco UCS X215c M8 Cisco UCS X210c M6, X210c M7, and X410c M7  
15420 (UCSX-ML-V5Q50G)  |  \-  |  Cisco UCS X210c M8 Cisco UCS X215c M8 Cisco UCS X210c M6, X210c M7, and X410c M7  
15231 (UCSX-ML-V5D200G)  |  \-  |  Cisco UCS X210c M6, X210c M7, and X410c M7  
14425 + UCS VIC 14000 bridge connector + 14825 (UCSX-V4-Q25GML + UCSX-V4-BRIDGE + UCSX-V4-Q25GME) |  \-  |  Cisco UCS X210c M6   
14425 (UCSX-V4-Q25GML)  |  \-  |  Cisco UCS X210c M6   
15411 + Port Expander (UCSB-ML-V5Q10G + UCSB-MLOM-PT-01)  |  Cisco UCS B200 M6  |  \-   
15411 (UCSB-ML-V5Q10G)  |  Cisco UCS B200 M6  |  \-   
1440 + 1480 + Port Expander (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P + UCSB-MLOM-PT-01) |  Cisco UCS B480 M5  |  \-   
1440 + 1480 + 1480 (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P +UCSB-VIC-M84-4P)  |  Cisco UCS B480 M5  |  \-   
1440 + 1480 (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P)  |  Cisco UCS B200 M6, B200 M5, B480 M5  |  \-   
1440 + Port Expander (UCSB-MLOM-40G-04 + UCSB-MLOM-PT-01)  |  Cisco UCS B200 M6, B200 M5, B480 M5  |  \-   
1440 (UCSB-MLOM-40G-04)  |  Cisco UCS B200 M6, B200 M5, B480 M5  |  \-   
1340 + 1380 + Port Expander (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P + UCSB-MLOM-PT-01) |  Cisco UCS B480 M5  |  \-   
1340 + 1380 + 1380 (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P + UCSB-VIC-M83-8P) |  Cisco UCS B480 M5  |  \-   
1340 + 1380 (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P)  |  Cisco UCS B200 M5 and B480 M5  |  \-   
1340 + Port Expander - 10G/40G (UCSB-MLOM-40G-03 + UCSB-MLOM-PT-01)  |  Cisco UCS B200 M5 and B480 M5  |  \-   
1340 - 10G/40G (UCSB-MLOM-40G-03)  |  Cisco UCS B200 M5 and B480 M5  |  \-   
  
### Cisco UCS 6400 and 64108 FIs

Table 3. Cisco UCS 6400 and 64108 FIs - Cisco UCS Rack Servers Cisco VIC |  Direct Attach  (10G/25G)  |  Direct Attach  (4x10G/4x25)  |  Direct Attach  (40G/100G)  |  FEX  
---|---|---|---|---  
2232 PP (10G)  |  93180YC-FX3  (25G server ports)  |  93180YC-FX3  (10G server ports)   
15427 (UCSC-M-V5Q50GV2) |  All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M8, M7, and M6 servers. |  Not Supported |  Not Supported |  All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M8, M7, and M6 servers with SFP-10G-SR/SR-S only.  
15237 (UCSC-M-V5D200GV2) |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
15235 (UCSC-P- V5D200G) |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
15238 (UCSC-M -V5D200G)  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
15425 (UCSC-P- V5Q50G) |  All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M8, M7, and M6 servers. |  Not Supported  |  Not Supported  |  All Cisco UCS C-Series M8, M7, and M6 servers. |  All Cisco UCS C-Series M8, M7, and M6 servers with SFP-10G-SR/SR-S only.  
15428 (UCSC-M -V5Q50G)  |  All Cisco UCS C-Series M6 and M7 servers. |  All Cisco UCS C-Series M6 and M7 servers. |  Not Supported  |  Not Supported  |  All Cisco UCS C-Series M6 and M7 servers. |  All Cisco UCS C-Series M8, M7, and M6 servers with SFP-10G-SR/SR-S only.  
|  **Note** |  Break-out is supported (6400 side QSFP, on adapter side two ports can be connected to 1 VIC ( like ports 1 and 2) Reverse-breakout : Not supported  
---|---  
1495-40G/100G  (UCSC -PCIEC100 -04)  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
1497-40G/100G  (UCSC -MLOMC100 -04)  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
1477-40G/100G  (UCSC-MV100 -04)  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported  |  Not Supported   
1467-10G/25G (UCSC -MV25-04)  |  All Cisco UCS C-Series M6 servers. |  All Cisco UCS C-Series M6 servers. |  Not Supported  |  All Cisco UCS C-Series M6 servers. |  All Cisco UCS C-Series M6 servers. |  All Cisco UCS C-Series M6 servers with SFP-10G-SR/SR-S only.  
1457-10G/25G (UCSC-MLOM C25Q-04)  |  All Cisco UCS C-Series M5 servers. |  All Cisco UCS C-Series M5 servers. |  Not Supported  |  All Cisco UCS C-Series M5 servers. |  All Cisco UCS C-Series M5 servers. |  All Cisco UCS C-Series M5 servers with SFP-10G-SR/SR-S only.  
1455-10G/25G  (UCSC-PCIEC 25Q-04)  |  All Cisco UCS C-Series M6 and M5, and S-Series M5 servers. |  All Cisco UCS C-Series M6 and M5, and S-Series M5 servers. |  Not Supported  |  All Cisco UCS C-Series M6 and M5, and S-Series M5 servers. |  All Cisco UCS C-Series M6 and M5, and S-Series M5 servers. |  All Cisco UCS C-Series M6 and M5, and S-Series M5 servers with SFP-10G-SR/SR-S only.  
1387 - 40G  (UCSC-MLOM -C40Q-03)  |  All Cisco UCS C-Series M5 servers with QSA at adapter. |  Not Supported  |  Not Supported  |  All Cisco UCS C-Series M5 servers with QSA at adapter. |  Not Supported  |  All Cisco UCS C-Series M5 servers  with QSA and SFP-10G-SR/LR, SFP-H10GB-CU1/3/5M, or SFP-H10GB-ACU7M only.  
1385 - 40G  (UCSC-PCIE -C40Q-03)  |  All Cisco UCS C-Series M5 except C125 M5 and S-Series M5 servers  with QSA at the adapter. |  Not Supported  |  Not Supported  |  All Cisco UCS C-Series M5 except C125 M5 and S-Series M5 servers  with QSA at the adapter. |  Not Supported  |  All Cisco UCS C-Series M5 except C125 M5 and S-Series M5 servers  with QSA and SFP-10G-SR/LR, SFP-H10GB-CU1/3/5M, or SFP-H10GB-ACU7M only.  
Table 4. Cisco UCS 6400 and 64108 FIs - Cisco UCS Blade Servers Cisco VIC |  IOM  
---|---  
2204/2208/2408 |  UCSX-I-9108-25G  
15230 (UCSX-ML-V5D200GV2) |  Not Supported  |  Cisco UCS X210c M8 Cisco UCS X215c M8 Cisco UCS X210c M6, X210c M7, and X410c M7  
15420 +  UCS VIC 15000 bridge connector +  (15422 (UCSX-ML-V5Q50G + UCSX-V5-BRIDGE + UCSX-ME-V5Q50G) |  Not Supported  |  Cisco UCS X210c M8 Cisco UCS X215c M8 Cisco UCS X210c M6, X210c M7, and X410c M7  
15420  (UCSX-ML-V5Q50G) |  Not Supported  |  Cisco UCS X210c M8 Cisco UCS X215c M8 Cisco UCS X210c M6, X210c M7, and X410c M7  
15231  (UCSX-ML-V5D200G) |  Not Supported  |  Cisco UCS X210c M6, X210c M7, and X410c M7  
14425 +  UCS VIC 14000 bridge connector + (14825 (UCSX-V4-Q25GML + UCSX-V4-BRIDGE + UCSX-V4-Q25GME) |  Not Supported  |  Cisco UCS X210c M6  
14425  (UCSX-V4-Q25GML) |  Not Supported  |  Cisco UCS X210c M6  
15411 + Port Expander (UCSB-ML -V5Q10G + UCSB-MLOM -PT-01)  |  B200 M6  |  Not Supported   
15411 (UCSB-ML -V5Q10G)  |  B200 M6  |  Not Supported   
1440 + 1480 + Port Expander  (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P + UCSB-MLOM-PT-01) |  Cisco UCS B480 M5  |  Not Supported   
1440 + 1480 + Port Expander  (UCSB-MLOM-40G-04 +  UCSB-VIC- M84-4P) +  UCSB-MLOM-PT-01) |  Cisco UCS B480 M5  |  Not Supported   
1440 + 1480  (UCSB-MLOM-40G-04 +  UCSB-VIC-M84-4P)  |  Cisco UCS B200 M6, B200 M5, B480 M5  |  Not Supported   
1440 + Port Expander  (UCSB-MLOM-40G-04 +  UCSB-MLOM-PT-01)  |  Cisco UCS B200 M6, B200 M5, B480 M5  |  Not Supported   
1440  (UCSB-MLOM-40G-04)  |  Cisco UCS B200 M6, B200 M5, B480 M5  |  Not Supported   
1340 + 1380 + 1380  (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P + UCSB-VIC-M83-8P) |  Cisco UCS B480 M5  |  Not Supported  
1340 + 1380 + Port Expander  (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P + UCSB-MLOM-PT-01) |  Cisco UCS B480 M5  |  Not Supported  
1340 + Port Expander - 10G/40G  (UCSB-MLOM-40G-03 +  UCSB-MLOM-PT-01)  |  Cisco UCS B200 M5 and B480 M5  |  Not Supported  
1340 + 1380  (UCSB-MLOM-40G-03 +  UCSB-VIC-M83-8P)  |  Cisco UCS B200 M5 and B480 M5  |  Not Supported  
1340 - 10G/40G (UCSB-MLOM-40G-03)  |  Cisco UCS B200 M5 and B480 M5  |  Not Supported  
  
### Cisco UCS 6300 FI

Table 5. Cisco UCS 6300 FI - Cisco UCS Rack Servers Cisco VIC |  Direct Attach |  Direct Attach  (Break-out) |  FEX  
---|---|---|---  
2232 PP |  2348  
15427 (UCSC-M-V5Q50GV2) |  All Cisco UCS C-Series M6 servers. |  All Cisco UCS C-Series M6 servers. |  Not Supported  |  All Cisco UCS C-Series M6 servers.  
15237 (UCSC-M-V5D200GV2) |  All Cisco UCS C-Series M6 servers. |  Not Supported  |  Not Supported  |  Not Supported   
15235 (UCSC-P-V5D200G) |  All Cisco UCS C-Series M6 servers. |  Not Supported  |  Not Supported  |  Not Supported   
15425 (UCSC-P-V5Q50G) |  All Cisco UCS C-Series M6 servers. |  All Cisco UCS C-Series M6 servers. |  Not Supported  |  All Cisco UCS C-Series M6 servers.  
15428 (UCSC-M-V5Q50G)  |  All Cisco UCS C-Series M6 servers. |  All Cisco UCS C-Series M6 servers. |  Not Supported  |  All Cisco UCS C-Series M6 servers.  
15238 (UCSC-M-V5D200G)  |  All Cisco UCS C-Series M6 servers. |  Not Supported  |  Not Supported  |  Not Supported   
1497-40G/100G (UCSC-MLOMC100-04)  |  All Cisco UCS C-Series M5 servers. |  Not Supported  |  Not Supported  |  Not Supported   
1495-40G/100G (UCSC-PCIEC100-04)  |  All Cisco UCS C-Series M6, M5, and S-Series M5 servers. |  Not Supported  |  Not Supported  |  Not Supported   
1477-40G/100G (UCSC-MV100-04)  |  All Cisco UCS C-Series M6 servers. |  Not Supported  |  Not Supported  |  Not Supported   
1467-10G/25G (UCSC-MV25-04)  |  All Cisco UCS C-Series M6 servers (10G speed with 6332-16UP). |  All Cisco UCS C-Series M6 servers. |  All Cisco UCS C-Series M6 servers. |  All Cisco UCS C-Series M6 servers.  
1457-10G/25G (UCSC-MLOMC25Q-04)  |  Cisco UCS C220 M5 and C240 M5 (10G speed with 6332-16UP). |  Cisco UCS C220 M5 and C240 M5 servers. |  Cisco UCS C220 M5 and C240 M5 servers. |  Cisco UCS C220 M5 and C240 M5 servers.  
1455-10G/25G (UCSC-PCIEC25Q-04)  |  All Cisco UCS C-Series M6, M5, and S-Series M5 servers (10G speed with 6332-16UP). |  All Cisco UCS C-Series M6, M5, and S-Series M5 servers. |  All Cisco UCS C-Series M6, M5, and S-Series M5 servers. |  All Cisco UCS C-Series M6, M5, and S-Series M5 servers.  
1387 - 40G (UCSC-MLOM-C40Q-03)  |  All Cisco UCS C-Series M5 servers (40G or 10G using QSA) |  Not Supported  |  All Cisco UCS C-Series M5 servers (QSA at adapter)  |  All Cisco UCS C-Series M5 servers (QSA at adapter)   
1385 - 40G (UCSC-PCIE-C40Q-03)  |  All Cisco UCS C-Series M5 servers (except UCS C125 M5) and S-Series M5 servers (40G or 10G using QSA) |  Not Supported  |  All Cisco UCS C-Series M5 servers (except UCS C125 M5) and S-Series M5 servers (40G or 10G using QSA) |  All Cisco UCS C-Series M5 servers (except UCS C125 M5) and S-Series M5 servers (40G or 10G using QSA)  
Table 6. Cisco UCS 6300 FI - Cisco UCS Blade Servers Cisco VIC |  IOM  
---|---  
2304v1/v2 2204/2208  
15411 + Port Expander  (UCSB-ML-V5Q10G + UCSB-MLOM-PT-01)  |  Cisco UCS B200 M6   
15411 (UCSB-ML-V5Q10G)  |  Cisco UCS B200 M6   
1440 + 1480 + 1480  (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P + UCSB-VIC-M84-4P) |  Cisco UCS B480 M5   
1440 + 1480 + Port Expander (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P + UCSB-MLOM-PT-01) |  Cisco UCS B480 M5   
1440 + 1480 (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P)  |  Cisco UCS B200 M5, B480 M5 and B200 M6 servers   
1440 + Port Expander (UCSB-MLOM-40G-04 + UCSB-MLOM-PT-01)  |  Cisco UCS B200 M5, B480 M5 and B200 M6 servers   
1440 (UCSB-MLOM-40G-04)  |  Cisco UCS B200 M5, B480 M5 and B200 M6 servers   
1340 + 1380 + 1380  (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P +  UCSB-VIC-M83-8P) |  Cisco UCS B480 M5   
1340 + 1380 + Port Expander  (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P +  UCSB-MLOM-PT-01) |  Cisco UCS B480 M5   
1340 + Port Expander - 10G/40G (UCSB-MLOM-40G-03 + UCSB-MLOM-PT-01)  |  Cisco UCS B200 M5 and B480 M5 servers   
1340 + 1380 (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P)  |  Cisco UCS B200 M5 and B480 M5 servers   
1340 - 10G/40G (UCSB-MLOM-40G-03)  |  Cisco UCS B200 M5 and B480 M5 servers   
  
### Cisco UCS 6324 FI

Table 7. Cisco UCS 6324 FI - Cisco UCS Rack Servers Cisco VIC |  Direct Attach (10G)  |  Direct Attach  (Break-out)  
---|---|---  
15428 (UCSC-M-V5Q50G)  |  Not Supported  |  Not Supported   
15238 (UCSC-M-V5D200G)  |  Not Supported  |  Not Supported   
1497-40G/100G (UCSC-MLOMC100-04)  |  Not Supported  |  Not Supported   
1495-40G/100G (UCSC-PCIEC100-04)  |  Not Supported  |  Not Supported   
1477-40G/100G (UCSC-MV100-04)  |  Not Supported  |  Not Supported   
1467-10G/25G (UCSC-MV25-04)  |  Not Supported  |  Not Supported   
1457-10G/25G (UCSC-MLOMC25Q-04)  |  Cisco UCS C220 M5 and C240 M5 servers. |  Cisco UCS C220 M5 and C240 M5 servers.  
1455-10G/25G (UCSC-PCIEC25Q-04)  |  All Cisco UCS C-Series and S-Series M5 servers. |  All Cisco UCS C-Series and S-Series M5 servers.  
1387 - 40G (UCSC-MLOM-C40Q-03)  |  All Cisco UCS C-Series M5 servers. (QSA at the adapter) |  Not Supported   
1385 - 40G (UCSC-PCIE-C40Q-03)  |  All Cisco UCS C-Series M5 servers. (QSA at the adapter) |  Not Supported   
Table 8. Cisco UCS 6324 FI - Cisco UCS Blade Servers Cisco VIC |  IOM |  6324 (Primary Chassis)  
---|---|---  
2204/2208  
15411 (UCSB-ML-V5Q10G)  |  Not Supported  |  Not Supported   
15411 + Port Expander (UCSB-ML-V5Q10G + UCSB-MLOM-PT-01)  |  Not Supported  |  Not Supported   
1440 + 1480 + 1480 (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P +UCSB-VIC-M84-4P)  |  Not Supported  |  Cisco UCS B480 M5  
1440 + 1480 + Port Expander (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P) + UCSB-MLOM-PT-01) |  Not Supported  |  Cisco UCS B480 M5  
1440 + 1480 (UCSB-MLOM-40G-04 + UCSB-VIC-M84-4P)  |  Not Supported  |  Cisco UCS B200 M5, B480 M5, and B200 M6  
1440 + Port Expander (UCSB-MLOM-40G-04 + UCSB-MLOM-PT-01)  |  Not Supported  |  Cisco UCS B200 M5, B480 M5, and B200 M6  
1440 (UCSB-MLOM-40G-04)  |  Not Supported  |  Cisco UCS B200 M5, B480 M5, and B200 M6  
1340 + 1380 + 1380  (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P +  UCSB-VIC-M83-8P) |  Cisco UCS B480 M5  |  Cisco UCS B480 M5   
1340 + 1380 + Port Expander  (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P +  UCSB-MLOM-PT-01) |  Cisco UCS B480 M5  |  Cisco UCS B480 M5   
1340 + 1380  (UCSB-MLOM-40G-03 + UCSB-VIC-M83-8P)  |  Cisco UCS B200 M5 and B480 M5  |  Cisco UCS B200 M5 and B480 M5   
1340 + Port Expander - 10G/40G  (UCSB-MLOM-40G-03 + UCSB-MLOM-PT-01)  |  Cisco UCS B200 M5 and B480 M5  |  Cisco UCS B200 M5 and B480 M5   
1340 - 10G/40G (UCSB-MLOM-40G-03)  |  Cisco UCS B200 M5 and B480 M5  |  Cisco UCS B200 M5 and B480 M5   
  
### Cisco UCS Fabric Interconnect 9108 100G

Table 9. Cisco UCS FI 9108 100G - Cisco UCS Blade Servers Cisco VIC |  UCSX-S9108-100G (Primary Chassis)  
---|---  
14425 (UCSX-V4-Q25GML) |  Cisco UCS X210c M6  
14425 + UCS VIC 14000 bridge connector + 14825  (UCSX-V4-Q25GML + UCSX-V4-BRIDGE +  UCSX-V4-Q25GME) |  Cisco UCS X210c M6  
15231 (UCSX-ML-V5D200G) |  Cisco UCS X410c M7, X210c M7, X210c M6  
15230 (UCSX-ML-V5D200GV2) |  Cisco UCS X210c M8, X215c M8, X410c M7, X210c M7, and X210c M6   
15420 (UCSX-ML-V5Q50G) |  Cisco UCS X210c M8, X215c M8, X410c M7, X210c M7, and X210c M6   
15420 + UCS VIC 15000 bridge connector + 15422  (UCSX-ML-V5Q50G + UCSX-V5-BRIDGE +  UCSX-ME-V5Q50G) |  Cisco UCS X210c M8, X215c M8, X410c M7, X210c M7, and X210c M6 


---

## Page 8: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Fabric-Interconnect-Migration/4-3_1/m_overview-4-1.html

##  Cisco UCS 6536 Fabric Interconnect Overview   
  
The Cisco UCS 6536 Fabric Interconnect is a core part of the Cisco Unified Computing System, providing both network connectivity and management capabilities for the system. The Cisco UCS 6536 Fabric Interconnect provides the communication backbone and management connectivity for UCS B-series blade servers and UCS C-series rack servers. 

Cisco UCS 6500 Series Fabric Interconnects currently include Cisco UCS 6536 Fabric Interconnect. All servers attached to a Cisco UCS 6536 Fabric Interconnect become part of a single, highly available management domain. In addition, by supporting a unified fabric, Cisco UCS 6536 Fabric Interconnect provides both LAN and SAN connectivity for all servers within its domain. 

The Cisco UCS 6536 Fabric Interconnect supports multiple traffic classes over a lossless Ethernet fabric from the server through the fabric interconnect. 


---

