# Intersight Appliance Supported Systems

| | |
|---|---|
| **URL Title** | Intersight Appliance Supported Systems |
| **URL** | https://intersight.com/help/appliance/supported_systems |
| **Long URL** | https://cdn.intersight.com/components/an-hulk/1.0.11-20260225095216527/docs/onprem/data/articles/supported_systems/en/index.html |
| **HTML Title** | Supported Systems |
| **Source file** | `ucs-docs-raw/html/intersight-appliance_supported_systems.html` |
| **File type** | HTML |
| **Fetched on** | 2026-03-04 12:48:07 |

---

# Supported Systems

This section provides information about the hardware systems that are supported by Cisco Intersight, and their corresponding software requirements and supported features. For the Product Identification Standards (PIDs) that are supported by Cisco Intersight, see [Intersight Supported Product Identification Standards](/help/resources/intersight_supported_pids).

## Supported Hardware for Intersight Managed Mode

This section includes the supported hardware for Intersight Managed Mode.

Table 1 lists the hardware components and the minimum required infrastructure firmware version.

Table 2 lists the supported server models.

Table 3 includes the supported hardware components for servers along with the supported server firmware and infrastructure firmware versions.

Table 4 shows the supported combination of components.

**Platform Release** : At the initial release, the firmware supports all available components. For subsequent hardware updates, higher firmware versions may be required.

**Documentation Resources** :

* Refer to the [X-Series Compute Nodes Spec Sheet](https://www.cisco.com/c/en/us/products/servers-unified-computing/ucs-x-series-modular-system/datasheet-listing.html#anchor722), [C-Series Servers Spec Sheet](https://www.cisco.com/c/en/us/products/servers-unified-computing/ucs-c-series-rack-servers/datasheet-listing.html#anchor969), and [B-Series Servers Spec Sheet](https://www.cisco.com/c/en/us/products/servers-unified-computing/ucs-b-series-blade-servers/datasheet-listing.html) for supported hardware and configuration rules.
* Check the [**Firmware Release Notes** ](https://www.cisco.com/c/en/us/support/servers-unified-computing/intersight/products-release-notes-list.html)for new hardware compatibility with specific firmware versions.

Table 1. Supported Hardware Components with Required Minimum Infrastructure VersionsFabric Components  
---  
Component| Model| Sub-Component| Sub-Component Model| Minimum Infrastructure Firmware Versions  
Fabric Interconnect| UCS-FI-6664| | | 6.0(1.250198)  
UCSX-S9108-100G| | | 4.3(4.240078)  
UCS-FI-6454|  |  | 4.1(3b)  
UCS-FI-64108|  |  | 4.1(3b)  
UCS-FI-6536|  |  | 4.2(2b)  
Chassis| N20-C6508UCSB-5108-AC2|  |  | 4.1(3b)  
Input/Output Module (IOM)| UCS-IOM-2204XPUCS-IOM-2208XPUCS-IOM-2408| 4.1(3b)  
UCS-IOM-2304UCS-IOM-2304V2| 4.2(3c)  
UCSX-9508|  |  | 4.2(1e)  
X-Fabric Modules (XFM)| UCSX-F-9416| 4.2(2a)  
Intelligent Fabric Module (IFM)| UCSX-I-9108-25G| 4.2(1e)  
UCSX-I-9108-100G| 4.2(2a)  
Fabric Extender (FEX)| Cisco Nexus 2232PP|  |  | 4.1(3b)  
N9K-C93180YC-FX3|  |  | 4.2(2a)  
  
Note:

* The Intersight Managed Mode (IMM) supports up to 20 chassis and 160 servers.
* Cisco UCS 6454 and 64108 Fabric Interconnects, require the port-based licensing in IMM but will not be enforced until further notice.

Beginning with UCS software release version 4.2(3), Cisco UCS 6536, Cisco UCS 6664, and UCS X-Direct Fabric Interconnects support a perpetual software license, activating all ports and features.

* Swapping or moving cable connections on rack network adapters, whether between VIC ports on the same Fabric Interconnect or between different Fabric Interconnects, is not supported while the server is powered on after server discovery. Such actions are only permitted when the server is powered off through a soft shutdown.
* The minimum supported Infrastructure firmware version for Intersight Managed Mode is 4.1(3).

Supported Servers

The following table lists the server models supported in Intersight Managed Mode across different generations. For more information on specific components of the servers, see (Table 3).

Table 2. Supported Server ModelsServer Generation| Supported Model  
---|---  
M8| Cisco UCS X210c M8 Compute Node  
Cisco UCS X215c M8 Compute Node  
Cisco UCS C220 M8 Server  
Cisco UCS C240 M8 Server  
Cisco UCS C225 M8 Server  
Cisco UCS C245 M8 Server  
M7| Cisco UCS X210c M7 Compute Node  
Cisco UCS X410c M7 Compute Node  
Cisco UCS C220 M7 Server  
Cisco UCS C240 M7 Server  
M6| Cisco UCS X210c M6 Compute Node  
Cisco UCS B200 M6 Server  
Cisco UCS C220 M6 Server  
Cisco UCS C240 M6 Server  
Cisco UCS C225 M6 Server  
Cisco UCS C245 M6 Server  
M5*| Cisco UCS B200 M5 Server  
Cisco UCS B480 M5 Server  
Cisco UCS C220 M5 Server  
Cisco UCS C240 M5 Server, Cisco UCS C240 SD M5 Server  
Cisco UCS C480 M5 Server *  
  
* Cisco UCS C480 ML M5, Cisco UCS C125 M5, and Cisco UCS S3260 M5 servers are not supported in Intersight Managed Mode.

Table 3. Supported Hardware Components with Required Minimum Firmware VersionsFabric Components  
---  
Component| Model| Sub-Component| Sub-Component Model| Minimum Infrastructure Firmware Versions| Minimum Server Firmware Versions| Minimum Appliance Release Version  
X-Series Intel M8 Compute Node| Cisco UCS X210c M8 Compute Node|  | 

* 6664 FI: 6.0(1.250198)
* X-Direct FI: 4.3(6.250094)
* 6400 Series and 6536 FI: 4.3(6.250048)

| 5.4(0.250037)| 1.1.2-1  
X-Series AMD M8 Compute Node| Cisco UCS X215c M8 Compute Node|  | 

* 6664 FI: 6.0(1.250198)
* X-Direct FI - 4.3(5.240162)
* 6400 Series and 6536 FI: 4.3(2.230117)

| 5.3(0.240016)| 1.1.1-0  
New Hardware Supported Since Initial Release  
CPU| 5th Generation AMD EPYC CPU:

* UCSX-CPU-A9655
* UCSX-CPU-A9555
* UCSX-CPU-A9355
* UCSX-CPU-A9135
* UCSX-CPU-A95755

Note:For more information, see the [Cisco UCS X215c M8 Compute Node Spec Sheet](https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-x-series-modular-system/ucs-x215c-m8-compute-node.pdf).| Not Applicable| 5.3(0.250001)| 1.1.2-0  
GPU| UCSC-GPU-MI210| Not Applicable| 5.3(0.250001)| 1.1.2-0  
DIMMs| DDR5-5600 MT/s:

* UCSX-MR128G2RG3

DDR5-6400 MT/s:

* UCS-MRX32G1RE5
* UCS-MRX64G2RE5

| Not Applicable| 5.3(0.250001)| 1.1.2-0  
Storage Controller| UCSX-X10C-GPUFM| Not Applicable| 5.3(0.240016)|   
X-Series M7 Server| Cisco UCS X410c M7 Compute Node|  | 

* 6664 FI: 6.0(1.250198)
* X-Direct FI - 4.3(4.240078)
* 6400 Series and 6536 FI: 4.2(3e)

| 5.1(1.230052)| 1.0.9-615  
CPU| 4th Generation Intel® Xeon® Scalable ProcessorsNote:For more information, see the [Cisco UCS X410c M7 Compute Node Spec Sheet](https://www.cisco.com/c/en/us/products/servers-unified-computing/ucs-x-series-modular-system/datasheet-listing.html).| Not Applicable| 5.1(1.230052)|   
DIMMs| UCSX-MRX16G1RE1UCSX-MRX32G1RE1UCSX-MRX64G2RE1UCSX-MR128G4RE1UCSX-MR256G8RE1| Not Applicable| 5.1(1.230052)|   
UCSX-MRX96G2RF3| Not Applicable| 5.2(2.240053)|   
Adapters| UCSX-ML-V5Q50G (Secure Boot)UCSX-ME-V5Q50G (Secure Boot)UCSX-ML-V5D200G| Not Applicable| 5.1(1.230052)|   
UCSX-ML-V5D200GV2 (Secure Boot)| Not Applicable| 5.2(0.230061)|   
Trusted Platform Module (TPM)| UCSX-TPM-002C| Not Applicable| 5.1(1.230052)|   
UCS-TPM-002D| Not Applicable| 5.2(2.240053)|   
Graphics processing unit (GPU)| UCSX-GPU-A16UCSX-GPU-A40UCSX-GPU-A100-80| Not Applicable| 5.1(1.230052)|   
UCSX-GPU-H100-80UCSX-GPU-L40UCSX-GPU-L4UCSX-GPU-FLEX140UCSX-GPU-FLEX170| Not Applicable| 5.2(0.230127)|   
UCSX-GPU-L40S| Not Applicable| 5.2(2.240053)|   
Storage Controller| UCSX-M2-HWRAIDUCSX-X10C-RAIDF| Not Applicable| 5.1(1.230052)|   
UCSX-M2-PT-FPN| Not Applicable| 5.2(0.230127)|   
UCSX-X10C-GPUFM| Not Applicable| 5.2(0.230041)|   
X-Series M7 Compute Node| Cisco UCS X210c M7 Compute Node|  | 

* 6664 FI: 6.0(1.250198)
* X-Direct FI - 4.3(4.240078)
* 6400 Series and 6536 FI: 4.2(3b)

| 5.1(0.230096)| 1.0.9-558  
CPU| 4th Generation Intel® Xeon® Scalable Processors.| Not Applicable| 5.1(0.230096)|   
5th Generation Intel® Xeon® Scalable ProcessorsNote:For more information, see the [Cisco UCS X210c M7 Compute Node Spec Sheet](https://www.cisco.com/c/en/us/products/servers-unified-computing/ucs-x-series-modular-system/datasheet-listing.html).| Not Applicable| 5.2(1.240010)|   
Additional 5th Generation Intel® Xeon® Scalable Processors:

* UCSX-CPU-I4510T
* UCSX-CPU-I4510
* UCSX-CPU-I4509Y
* UCSX-CPU-I3508U

| Not Applicable| 5.2(2.240053)|   
DIMMs| DDR5-4800MT/s:

* UCSX-MRX16G1RE1
* UCSX-MRX32G1RE1
* UCSX-MRX64G2RE1
* UCSX-MR128G4RE1
* UCSX-MR256G8RE1

| Not Applicable| 5.2(1.240010)|   
DDR5-5600MT/s:

* UCSX-MRX16G1RE3
* UCSX-MRX32G1RE3
* UCSX-MRX48G1RF3
* UCSX-MRX64G2RE3
* UCSX-MRX96G2RF3
* UCSX-MR128G4RE3
* UCSX-MR256G8RE3

| Not Applicable| 5.2(1.240010)|   
Adapters| UCSX-ML-V5Q50G (Secure Boot)UCSX-ME-V5Q50G (Secure Boot)UCSX-ML-V5D200G| Not Applicable| 5.1(0.230096)|   
UCSX-ML-V5D200GV2 (Secure Boot)| Not Applicable| 5.2(0.230061)|   
Trusted Platform Module (TPM)| UCSX-TPM-002C| Not Applicable| 5.1(0.230096)|   
UCS-TPM-002D| Not Applicable| 5.2(2.240053)|   
Graphics Processing Unit (GPU)| UCSX-GPU-T4-MEZZUCSX-GPU-A16UCSX-GPU-A40| Not Applicable| 5.1(0.230096)|   
UCSX-GPU-A100-80| Not Applicable| 5.1(0.230096)|   
UCSX-GPU-H100-80UCSX-GPU-L40UCSX-GPU-L4UCSX-GPU-FLEX140UCSX-GPU-FLEX170| Not Applicable| 5.2(0.230127)|   
UCSX-GPU-L40S| Not Applicable| 5.2(2.240053)|   
UCSX-GPU-H100-NVL| Not Applicable| 5.3(0.240016)|   
UCSX-GPU-L4-Mezz| Not Applicable|   
UCSX-GPU-FLX140MZ| Not Applicable| 5.2(2.240053)|   
Storage Controller| UCSX-X10C-PT4FUCSX-X10C-RAIDFUCSX-M2-HWRAID| Not Applicable| 5.1(0.230096)|   
UCSX-M2-PT-FPN| Not Applicable| 5.2(0.230041)|   
UCSX-X10C-GPUFM| Not Applicable| 5.3(0.250021)|   
X-Series M6 Server| Cisco UCS X210c M6 Compute Node| | 

* X-Direct FI - 4.3(4.240078)
* 6400 Series and 6536 FI: 4.2(1a)

| 5.0(1b)| 1.0.9-456  
Adapters| UCSX-V4-Q25GMLUCSX-V4-Q25GME| Not Applicable| 5.0(1b)|   
UCSX-ML-V5Q50G (Secure Boot)UCSX-ME-V5Q50G (Secure Boot)| Not Applicable| 5.1(0.230054)|   
UCSX-ML-V5D200G| Not Applicable| 5.0(2b)|   
UCSX-ML-V5D200GV2 (Secure Boot)| Not Applicable| 5.2(0.230061)|   
Rear Mezzanine Adapters| UCSX-V4-PCIME| Not Applicable| 5.0(2d)|   
Trusted Platform Module (TPM)| UCSX-TPM-002C| Not Applicable| 5.0(1b)|   
UCS-TPM-002D| Not Applicable| 4.3(4.240152)|   
Graphics processing unit (GPU)| UCSX-GPU-A100-80| Not Applicable| 5.0(2e)|   
UCSX-GPU-T4-MEZZUCSX-GPU-T4-16UCSX-GPU-A16UCSX-GPU-A40| Not Applicable| 5.0(2d)|   
Storage Controller| UCSX-X10C-PT4FUCSX-X10C-RAIDFUCSX-M2-HWRAID| Not Applicable| 5.0(4b)|   
UCSX-X10C-GPUFM| Not Applicable| 5.2(0.230040)|   
B-Series M6 Server| Cisco UCS B200 M6 Server|  | 6400 Series and 6536 FI: 4.1(3b)| 4.2(1d)| 1.0.9-319  
Adapters| UCSB-ML-V5Q10G| Not Applicable| 4.2(1d)|   
UCSB-MLOM-40G-04UCSB-VIC-M84-4P| 4.1(3b)| 4.2(1d)|   
Trusted Platform Module (TPM)| UCSX-TPM-002C| Not Applicable| 4.2(1d)|   
UCS-TPM-002D| Not Applicable| 4.3(4.240152)|   
Storage Controller| UCS-M2-HWRAIDUCSB-RAID12G-M6UCSB-MSTOR-M6UCSB-LSTOR-PT-M6| Not Applicable| 4.2(1d)|   
B-Series M5 Server| Cisco UCS B200 M5 ServerCisco UCS B480 M5 Server| | 6400 Series and 6536 FI: 4.1(3b)| 4.1(3b)| 1.0.9-302  
Adapters| UCSB-MLOM-40G-03UCSB-VIC-M83-8P| 4.1(3b)| 4.2(2e)|   
UCSB-MLOM-40G-04UCSB-VIC-M84-4P| 4.1(3b)| 4.1(3b)|   
UCSB-MLOM-PT-01| 4.1(3b)| Not Applicable|   
Trusted Platform Module (TPM)| UCSX-TPM2-001UCSX-TPM2-002| Not Applicable| 4.1(3b)|   
Storage Controller| UCS-M2-HWRAIDUCSB-MRAID12GUCSB-MRAID12G-HEUCSB-LSTOR-PT| Not Applicable| 4.1(3c)|   
C-Series Intel M8 Server| Cisco UCS C220 M8 Server|  | 

* 6664 and X-Direct FI: 6.0(1.250198)
* 6400 Series and 6536 FI: 4.3(6.250048)

| 4.3(6.250039)| 1.1.2-1  
Cisco UCS C240 M8 Server|  | 

* 6664 and X-Direct FI: 6.0(1.250198)
* 6400 Series and 6536 FI: 4.3(6.250048)

| 4.3(6.250039)| 1.1.2-1  
Storage Controller| UCSC-RAID-M1L16| 

* 6400 Series, 6536, 6664, and X-Direct FI: 6.0(1.250198)

| 6.0(1.250127)|   
C-Series AMD M8 Server| Cisco UCS C225 M8 Server|  | 

* 6664 and X-Direct FI: 6.0(1.250198)
* 6400 Series and 6536 FI: 4.2(3b)

| 4.3(5.240021)| 1.1.1-0  
New Hardware Supported Since Initial Release  
CPU| 5th Generation AMD EPYC CPU:

* UCS-CPU-A9655P
* UCS-CPU-A9555P
* UCS-CPU-A9355
* UCS-CPU-A9135
* UCS-CPU-A9575F

Note:For more information, see the [Cisco UCS C225 M8 Server Spec Sheet](https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/ucs-c225-m8-sff-rack-server.pdf).| 4.2(3b)| 4.3(5.250001)| 1.1.2-0  
Storage Controller| UCSC-RAID-M1L16UCSC-RAID-MP1L32| 4.2(3b)| 4.3(5.250001)| 1.1.2-0  
UCSC-HBA-M1L16| 4.2(3b)| 4.3(5.250001)| 1.1.2-0  
DIMMs| DDR5-5600 MT/s:

* UCS-MR128G2RG3

DDR5-6400 MT/s

* UCS-MRX32G1RE5
* UCS-MRX64G2RE5

| Not Applicable| 4.3(5.250001)| 1.1.2-0  
Cisco UCS C245 M8 Server|  | 

* 6664 and X-Direct FI: 6.0(1.250198)
* 6400 Series and 6536 FI: 4.2(3b)

| 4.3(4.241014)| 1.1.1-0  
New Hardware Supported Since Initial Release  
Graphics processing unit (GPU)| UCSC-GPU-H100-NVL| Not Applicable| 4.3(5.240021)|   
UCSC-GPU-MI210| Not Applicable| 4.3(5.250001)| 1.1.2-0  
CPU| 5th Generation AMD EPYC CPU:

* UCS-CPU-A9655
* UCS-CPU-A9555
* UCS-CPU-A9355
* UCS-CPU-A9135
* UCS-CPU-A9575F

Note:For more information, see the [Cisco UCS C245 M8 Spec Sheet](https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/ucs-c245-m8-sff-rack-server.pdf).| Not Applicable| 4.3(5.250001)| 1.1.2-0  
Storage Controller| UCSC-RAID-M1L16UCSC-RAID-MP1L32| 4.2(3b)| 4.3(5.250001)| 1.1.2-0  
UCSC-HBA-M1L16| 4.2(3b)| 4.3(5.250001)| 1.1.2-0  
DIMMs| DDR5-5600 MT/s:

* UCS-MR128G2RG

DDR5-6400 MT/s:

* UCS-MRX32G1RE5
* UCS-MRX64G2RE5
* UCS-MRX96G2RF5

| Not Applicable| 4.3(5.250001)| 1.1.2-0  
C-Series M7 Server| Cisco UCS C220 M7 Server|  | 

* 6664 and X-Direct FI: 6.0(1.250198)
* 6400 Series and 6536 FI: 4.2(3b)

| 4.3(1.230097)| 1.0.9-558  
CPU| 4th Generation Intel® Xeon® Scalable Processors.| Not Applicable| 4.3(1.230097)|   
5th Generation Intel® Xeon® Scalable ProcessorsNote:For more information, see the [Cisco UCSC C220 M7 SFF Rack Server Spec Sheet](https://www.cisco.com/c/en/us/products/servers-unified-computing/ucs-c-series-rack-servers/datasheet-listing.html).| Not Applicable| 4.3(3.240022)|   
Additional 5th Generation Intel® Xeon® Scalable Processors:

* UCS-CPU-I4510T
* UCS-CPU-I4510
* UCS-CPU-I4509Y
* UCS-CPU-I3508U

| Not Applicable| 4.3(4.240152)|   
DIMMs| DDR5-4800MT/s:

* UCS-MRX16G1RE1
* UCS-MRX32G1RE1
* UCS-MRX64G2RE1
* UCS-MR128G4RE1

| Not Applicable| 4.3(3.240022)|   
DDR5-5600MT/s:

* UCS-MRX16G1RE3
* UCS-MRX32G1RE3
* UCS-MRX48G1RF3
* UCS-MRX64G2RE3
* UCS-MRX96G2RF3
* UCS-MR128G4RE3

Note:48GB and 96GB memory DIMMs are not supported on UCS-CPU-I3508U, UCS-CPU-I4509Y, UCS-CPU-I4510, UCS-CPU-I4510T| Not Applicable| 4.3(3.240022)|   
Adapters| UCSC-M-V5Q50GUCSC-M-V5D200G| Not Applicable| 4.3(1.230097)|   
UCSC-P-V5D200G (Secure Boot)UCSC-P-V5Q50G (Secure Boot)| 4.3(2.230117)| 4.3(2.230184)|   
UCSC-M-V5D200GV2 (Secure Boot)UCSC-M-V5Q50GV2 (Secure Boot)| Not Applicable| 4.3(2.230258)|   
Trusted Platform Module (TPM)| UCSX-TPM-002C| Not Applicable| 4.3(1.230097)|   
UCS-TPM-002D| Not Applicable| 4.3(4.240152)|   
Graphics processing unit (GPU)| UCSC-GPU-A16UCSC-GPU-A100-80| Not Applicable| 4.3(1.230097)|   
UCSC-GPU-L4UCSC-GPU-FLEX140| Not Applicable| 4.3(2.230207)|   
Storage Controller| UCS-M2-NVRAID| 4.3(2.230117)| 4.3(2.230207)|   
UCSC-HBA-M1L16UCSC-RAID-M1L16| 4.3(2.230117)| 4.3(4.242038)|   
Virtual Drives| UCS-SD16TKA3X-EPUCS-SD32TKA3X-EPUCS-SD16TBKANK9UCS-SD19TKA1X-EVUCS-SD38TKA1X-EVUCS-SD76TKA1X-EVUCS-SD15TKA1X-EVUCS-SD38TBKANK9UCS-SD76TBKANK9| 4.3(2.230117)| 4.3(2.230207)|   
Cisco UCS C240 M7 Server|  | 

* 6664 and X-Direct FI: 6.0(1.250198)
* 6400 Series and 6536 FI: 4.2(3b)

| 4.3(1.230097)| 1.0.9-558  
CPU| 4th Generation Intel® Xeon® Scalable Processors.| Not Applicable| 4.3(1.230097)|   
5th Generation Intel® Xeon® Scalable ProcessorsNote:For more information, see the [Cisco UCS C240 M7 SFF Rack Server Spec Sheet](https://www.cisco.com/c/en/us/products/servers-unified-computing/ucs-c-series-rack-servers/datasheet-listing.html).| Not Applicable| 4.3(3.240022)|   
Additional 5th Generation Intel® Xeon® Scalable Processors:

* UCS-CPU-I4510T
* UCS-CPU-I4510
* UCS-CPU-I4509Y
* UCS-CPU-I3508U

| Not Applicable| 4.3(4.240152)|   
DIMMs| DDR5-4800MT/s:

* UCS-MRX16G1RE1
* UCS-MRX32G1RE1
* UCS-MRX64G2RE1
* UCS-MR128G4RE1
* UCS-MR256G8RE1

| Not Applicable| 4.3(3.240022)|   
DDR5-5600MT/s:

* UCS-MRX16G1RE3
* UCS-MRX32G1RE3
* UCS-MRX48G1RF3
* UCS-MRX64G2RE3
* UCS-MRX96G2RF3
* UCS-MR128G4RE3
* UCS-MR256G8RE3

| Not Applicable| 4.3(3.240022)|   
Trusted Platform Module (TPM)| UCSX-TPM-002C| Not Applicable| 4.3(1.230097)|   
UCS-TPM-002D| Not Applicable| 4.3(4.240152)|   
Adapters| UCSC-M-V5Q50GUCSC-M-V5D200G| Not Applicable| 4.3(1.230097)|   
UCSC-P-V5D200G (Secure Boot)UCSC-P-V5Q50G (Secure Boot)| 4.3(2.230117)| 4.3(2.230184)|   
UCSC-M-V5D200GV2 (Secure Boot)UCSC-M-V5Q50GV2 (Secure Boot)| Not Applicable| 4.3(2.230258)|   
Graphics processing unit (GPU)| UCSC-GPU-A16UCSC-GPU-A100-80| Not Applicable| 4.3(1.230097)|   
UCSC-GPU-H100-80UCSC-GPU-L40UCSC-GPU-L4UCSC-GPU-FLEX140UCSC-GPU-FLEX170| Not Applicable| 4.3(2.230207)|   
UCSC-GPU-L40S| Not Applicable| 4.3(4.240152)|   
UCSC-GPU-H100-NVL| Not Applicable| 4.3(5.240021)|   
Storage Controller| UCS-M2-NVRAID| 4.3(2.230117)| 4.3(2.230207)|   
UCSC-HBA-M1L16UCSC-RAID-MP1L32| 4.3(2.230117)| 4.3(4.242038)|   
Virtual Drives| UCS-SD16TKA3X-EPUCS-SD32TKA3X-EPUCS-SD16TBKANK9UCS-SD19TKA1X-EVUCS-SD38TKA1X-EVUCS-SD76TKA1X-EVUCS-SD15TKA1X-EVUCS-SD38TBKANK9UCS-SD76TBKANK9| 4.3(2.230117)| 4.3(2.230207)|   
C-Series M6 Server| Cisco UCS C220 M6 ServerCisco UCS C240 M6 Server|  | 6400 Series and 6536 FI: 4.1(3b)| 4.2(1e)| 1.0.9-319  
Adapters| UCSC-PCIE-C25Q-04UCSC-PCIE-C100-04| 4.1(3b)| 4.2(1e)|   
UCSC-M-V100-04UCSC-M-V25-04| 4.1(3b)| 4.2(1e)|   
UCSC-M-V5D200G| Not Applicable| 4.2(2f)|   
UCSC-M-V5Q50G| Not Applicable| 4.2(2b)|   
UCSC-P-V5D200G (Secure Boot)UCSC-P-V5Q50G (Secure Boot)| 4.3(2.230117)| 4.3(2.230184)|   
UCSC-M-V5D200GV2 (Secure Boot)UCSC-M-V5Q50GV2 (Secure Boot)| Not Applicable| 4.3(2.230258)|   
Trusted Platform Module (TPM)| UCSX-TPM-002C| Not Applicable| 4.2(1e)|   
UCS-TPM-002D| Not Applicable| 4.3(4.240152)|   
Graphics processing unit (GPU)| UCSC-GPU-A16UCSC-GPU-A100-80| Not Applicable| 4.2(3b)|   
UCSC-GPU-L4| Not Applicable| 4.3(4.240152)|   
Storage Controller| UCS-M2-HWRAIDUCSC-RAID-M6TUCSC-RAID-M6SDUCSC-RAID-M6HDUCSC-SAS-M6HDUCSC-SAS-M6T| Not Applicable| 4.2(1e)|   
Cisco UCS C245 M6 ServerCisco UCS C225 M6 Server|  | 6400 Series and 6536 FI: 4.1(3b)| 4.2(1e)| 1.0.9-360  
Adapters| UCSC-PCIE-C25Q-04UCSC-PCIE-C100-04| 4.1(3b)| 4.2(1e)|   
UCSC-M-V100-04UCSC-M-V25-04| 4.1(3b)| 4.2(1e)|   
UCSC-M-V5D200G| Not Applicable| 4.2(2f)|   
UCSC-M-V5Q50G| Not Applicable| 4.2(2b)|   
UCSC-P-V5D200G (Secure Boot)UCSC-P-V5Q50G (Secure Boot)| 4.3(2.230117)| 4.3(2.230184)|   
UCSC-M-V5D200GV2 (Secure Boot)UCSC-M-V5Q50GV2 (Secure Boot)| Not Applicable| 4.3(2.230258)|   
Trusted Platform Module (TPM)| UCSX-TPM2-002B-C| Not Applicable| 4.2(1e)|   
UCS-TPM2-002D| Not Applicable| 4.3(4.240152)|   
Graphics processing unit (GPU)| UCSC-GPU-A16UCSC-GPU-A100-80| Not Applicable| 4.2(3b)|   
Storage Controller| UCS-M2-HWRAIDUCSC-RAID-M6TUCSC-RAID-M6SDUCSC-RAID-M6HDUCSC-SAS-M6HDUCSC-SAS-M6T| Not Applicable| 4.2(1e)|   
C-Series M5 Server| Cisco UCS C220 M5 ServerCisco UCS C240 M5 ServerCisco UCS C480 M5 Server|  | 6400 Series and 6536 FI: 4.1(3b)| 4.1(3b)| 1.0.9-302  
Adapters| UCSC-MLOM-C40Q-03UCSC-PCIE-C40Q-03| 4.1(3b)| 4.2(2g)|   
UCSC-PCIE-C25Q-04UCSC-MLOM-C25Q-04UCSC-PCIE-C100-04UCSC-MLOM- C100-04| 4.1(3b)| 4.1(3b)|   
Trusted Platform Module (TPM)| UCSX-TPM2-001UCSX-TPM2-002| Not Applicable| 4.1(3b)|   
Graphics processing unit (GPU)| UCSC-GPU-A100-80| Not Applicable| 4.2(3b)|   
Storage Controller| UCS-M2-HWRAIDUCSC-RAID-M5HDUCSC-RAID-M5UCSC-SAS-M5,UCSC-SAS-M5HDUCSC-SAS12GHBAUCSC-9400-8E| Not Applicable| 4.1(3b)|   
  
Note:

**Change in Firmware Version Schema** :

* **X-Series M6 Server Firmware Bundle** : Post server firmware release 5.0(4g), the version number is in a number format instead of a letter format.
* **C-Series M5 and M6 Server Firmware Bundle** : Post server firmware release 4.2(3m), the version number is in a number format instead of a letter format.
* **B-Series M5 and M6 Server Firmware Bundle** : Post server firmware release 4.2(3j), the version number is in the 5.x series and in a number format instead of a letter format.
* **Infrastructure Firmware Bundle** : With infra firmware release 4.3(2) and later, the version number is in a number format instead of a letter format.

For example: 4.3(2.230117) , where 23 represents year, 0117 shows the incremental build number.​

For more information on Cisco Intersight Infrastructure Firmware release notes, Server Firmware release notes, and Release Bundle Content document see [Release Notes](https://www.cisco.com/c/en/us/support/servers-unified-computing/intersight/products-release-notes-list.html).

Table 4. Supported Combination of Hardware Components in IMMComponent| Supported Combination  
---|---  
Cisco UCS X-Series Direct| 

* Integrated FI: UCSX-S9108-100G
* Cisco UCS X-Series Direct supports all components that are compatible with Cisco UCS X-Series modular system.
* Starting with Infrastructure firmware release 6.0(1.250198):
* Secondary chassis is supported.
* Rack servers are supported.
* UCS X-Series Direct currently does not support Fabric Extender.

  
Topologies| Direct-Attached Racks through 10G/25G/100G connectionsBreak-out port configuration through 10G/25G connectionsFEX-Attached Racks through 10GE connectionsChassis through 10G/25G/100G connectionsN9K-C93108YC-FX3 FEX through 10G/25G connections  
Fabric Interconnects| 

* UCS-FI-6536 and direct-attached rack server are supported at 40G and 100G on Cisco UCS 1400 and 15000 series VIC adapters.
* Cisco UCS 6664 FI is supported with the UCSX-9508 chassis using UCSX-I-9108-25G and UCSX-I-9108-100G IFMs.

  
Input/Output Module (IOM)| 

* UCS-IOM-2204XP and UCS-IOM-2208XP are not supported on Cisco UCS 6500 Series Fabric Interconnects.
* UCS-IOM-2304 and UCS-IOM-2304V2 are supported only with Cisco UCS 6500 series Fabric Interconnect.
* When there is a mixed IOM configuration, Access Policy deployment can fail resulting in Server Profile deployment failure. It will recover once both the IOMs are replaced.

  
X-Fabric Modules (XFM)| UCS 9416 X-Fabric module is supported only on UCSX-9508 chassis and required for Peripheral Component Interconnect Express (PCIe) node and GPU discovery or inventory support in IMM.  
Fabric Extender (FEX)| Cisco Nexus 2232PP is not supported on Cisco UCS 6500 Series Fabric Interconnects.  
Rear Mezzanine Adapters| 

* UCS PCI mezz card for X‐Fabric connectivity.
* The UCSX-210C Compute Node must include a UCSX-V4-PCIME or a supported mezz card when paired with a X440p PCIe node.

  
Adapters| 

* UCSX-X10C-GPUFM is an adapter that supports the GPU, UCSX-GPU-T4-MEZZ. For more information, see [Cisco UCS X10c Front Mezzanine GPU Module Installation and Service Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-x-series-modular-system/products-installation-guides-list.html).
* UCSX-V4-Q25GME is a mezz card requires UCS VIC 14000 bridge connector (UCSX-V4-BRIDGE) and UCSX-V4-Q25GML mLOM support in the X210c Compute Node. For more information, see [Cisco UCS X210c M6 Compute Node](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-x-series-modular-system/products-installation-guides-list.html).
* The UCSX-210C Compute Node must include a UCSX-V4-PCIME or a supported mezz card when paired with a X440p PCIe node.
* UCSX-ML-V5D200G adapter is supported on Cisco UCS 6500 series Fabric Interconnect at 40G and 100G speed, as well as on Cisco UCS 6400 series Fabric Interconnect at 25G speed.
* Cisco UCS C-Series and X-Series M7 servers support only Cisco UCS 15000 series VIC adapters.
* UCSX-ME-V5Q50G is a mezz card that requires UCS VIC 15000 bridge connector (UCSX-V5-BRIDGE) and UCSX-ML-V5Q50G mLOM support in the X210c Compute Node. However, this mezz adapter is not supported with UCSX-ML-V5D200G mLOM.
* On a B-series server, installing a combination of Cisco UCS 1400 and UCS 15000 series VIC adapters is not supported.
* Cisco UCS VIC 1300 Series adapters are supported on B-Series and C-Series M5 servers with the following combination.
* UCS-FI-6454 and UCS-IOM-2408
* UCS-FI-6536 and UCS-IOM-2408
* UCS-FI-6454 and UCS-IOM-2204XP
* UCS-FI-6454 and UCS-IOM-2208XP
* UCS-FI-6536 and direct-attached rack server at 40G
* UCS-FI-6454 and rack server connected through FEX
* UCS-FI-6454 and direct-attached rack server with 10G QSA
* UCS-FI-6536 and UCS-IOM-2304 or UCS-IOM-2304V2
* UCS-FI-64108 and UCS-IOM-2408
* UCS-FI-64108 and UCS-IOM-2204XP
* UCS-FI-64108 and UCS-IOM-2208XP
* UCS-FI-64108 and direct-attached rack server
* UCS-FI-64108 and rack server connected through FEX
* UCSC-M-V100-04, UCSC-PCIE-C100-04, UCSC-MLOM-C100-04 are supported only on Cisco UCS 6500 Series Fabric Interconnects.
* The following combinations are not supported on UCS C series M6 servers:
* 1400 Series MLOM adapters with 15000 Series PCIE adapters
* UCSC-M-V5Q50GV2 and UCSC-M-V5D200GV2 are not supported with 14xx PCIE adapters
* Ensure that you have upgraded servers to the VIC supported release versions before installing the VIC adapters into the server. If you install VIC adapters on servers running an earlier release and later decide to upgrade the servers to the supported version, you need to perform A/C power cycle for the servers to enable the adapters.

  
Graphics processing unit (GPU)| 

* Mixing of GPU models is not supported in the server. For more information, see [Cisco UCS X440p PCIe Node Installation and Service Guide](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-x-series-modular-system/products-installation-guides-list.html).
* Specific GPUs are also supported on the X210c Compute Nodes. They require the UCSX-X10C-GPUFM adapter to support a GPU in the Front Mezz.Note:Contact NVIDIA directly for software support related to NVIDIA products used with GPUs. The Cisco Technical Assistance Center (TAC) does not provide support for NVIDIA software. For more information, see [Engage Support for Cisco AI UCS Servers Containing Nvidia GPUs](https://www.cisco.com/c/en/us/support/docs/servers-unified-computing/unified-computing-system/225449-engage-support-for-cisco-ai-ucs-servers.html).

  
  
## Supported Hardware for Standalone and UCSM Managed Mode

System| Minimum Supported Version  
---|---  
Cisco UCS Fabric Interconnects| For Cisco UCS 6200 and 6300 Series Fabric Interconnects: Cisco UCS Manager 3.2 and later versionFor Cisco UCS Mini 6324 Fabric Interconnects: Cisco UCS Manager 3.2 and later version.For Cisco UCS 6454 Fabric Interconnects: Cisco UCS Manager 4.0 and later versionFor Cisco UCS 64108 Fabric Interconnects: Cisco UCS Manager 4.1 and later versionFor Cisco UCS 6500 Series Fabric Interconnects: Cisco UCS Manager 4.2(3d) and later versionFor Cisco UCS 9108 100G Fabric Interconnect: Cisco UCS Manager 4.3(4b) and later versionFor Cisco UCS 6600 Series Fabric Interconnects: Cisco UCS Manager 6.0(1b) and later version  
UCSM Managed Mode servers and HyperFlex HX-Series servers| **M8 Servers:** For Cisco UCS C220 M8 servers: Cisco UCS Manager release 4.3(6a) and later versionFor Cisco UCS C240 M8 servers: Cisco UCS Manager release 4.3(6a) and later versionFor Cisco UCS C245 M8 servers - Support for 4th Generation AMD EPYC Processors: Cisco UCS Manager release 4.3(4b) and later versionFor Cisco UCS C225 M8, C245 M8 servers, and X215c M8 Compute Nodes - Support for 5th Generation AMD EPYC Processors: Cisco UCS Manager release 4.3(5c) and later version.For Cisco UCS C225 M8 servers and X215c M8 Compute Nodes - Support for 4th Generation AMD EPYC Processors: Cisco UCS Manager release 4.3(5a) and later version.For Cisco X210c M8 servers: Cisco UCS Manager release 4.3(6a) and later version**M7 Servers:** For Cisco UCS C220 M7 and C240 M7 servers and Cisco UCS X210c and UCS X410c Compute Nodes - Support for 4th Generation Intel® Xeon® Scalable Processors: 4.2(3b) and later versionFor Cisco UCS C220 M7 and C240 M7 servers and UCS X210c M7 Compute Nodes - Support for 5th Generation Intel® Xeon® Scalable Processors: 4.3(3a) and later versionFor Cisco UCS X210c M7 Compute Nodes : Cisco UCS Manager release 4.3(2b) and later version.For Cisco X410c M7 Compute Nodes: Cisco UCS Manager release 4.3(2c) and later version.**M6 Servers:** For Cisco UCS B-Series, C-Series M6 servers: Cisco UCS Manager release 4.2(1) and later version.For Cisco UCS X210c M6 Compute Node: Cisco UCS Manager release 4.3(2b) and later version.**M5 Servers:** For Cisco UCS B-Series, C-Series, and S-Series, and HX Series M5 Servers: Cisco UCS Manager release 3.2(1) and later version.For Cisco UCS B-Series, C-Series, and S-Series M4 Servers: Cisco UCS Manager release 3.1(1) and later version.  
Cisco UCS C-Series Standalone and HyperFlex HX-Series Edge Servers| **M8 Servers:** For C220 M8 Servers:Cisco IMC Software 4.3(6.250048) and later version.For C240 M8 Servers:Cisco IMC Software 4.3(6.250048) and later version.For C225 M8 Servers:Cisco IMC Software 4.3(5.240021) and later version.For C245 M8 Servers:Cisco IMC Software 4.3(4.241014) and later version.**M7 Servers** :For C220 and C240 M7 Servers:Cisco IMC Software 4.3(1.230097) and later version.**M6 Servers** :For Cisco UCS C220M6, C240 M6, C245 M6, and C225 M6 Servers: Servers: Cisco IMC Software 4.2 and later version**M5 Servers:** Cisco IMC Software 3.1 and later version**M4 Servers** :Cisco IMC Software 3.0(4) and later version  
Cisco UCS S3260 Standalone Servers| Cisco IMC Software 4.0(4e) and later  
Dense GPU Server| **Cisco UCS C885A M8 Server** Server firmware version: 1.1(0.250016) and later versionFor more information, see [Cisco Baseboard Management Controller Release Notes for Cisco UCS C885A M8 Rack Server, Release 1.1](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/release/notes/Cisco-BMC-Release-Notes/1-1-0/b_cisco-openbmc-release-notes-1_1.html).**Cisco UCS C845A M8 Server** Server firmware version: 2.0(1.250096) and later versionFor more information, see [Cisco Baseboard Management Controller 2.0 Release Notes, Release 2.0](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/release/notes/Cisco-BMC-Release-Notes/2-0-1/b_cisco-bmc-2-0-release-notes.html).  
Cisco HyperFlex Clusters| Cisco HyperFlex HX Data Platform 5.0(2a) and later *1  
Dell PowerEdge Servers| iDRAC v5.10.00.0 and later version  
HPE ProLiant Servers| iLO 5 version 2.55 and later version  
Cisco UCS Director| Cisco UCS Director 6.7.3.0  
NetApp AFF-Series, FAS-Series, All SAN Arrays| ONTAP version 9.8 and later version  
NetApp Active IQ Unified Manager| Latest version of AIQUM is required (9.14RC1)  
Pure Storage FlashArray| Purity version FA 4.8 to FA 6.0.2 (REST API 1.x only)Purity version FA 6.0.3 or later (REST API 1.x and REST API 2.x)  
VMware vCenter| 7.0 and 8.0  
Hitachi Virtual Storage Platform| For VSP One Block (B20): A3-02-21-x0/01 and laterFor VSP 5000 series: 90-03-01-00/00 and laterFor VSP G1000, G1500 and F1500: 80-06-75-00/00 and laterFor VSP G/F 350,370,700,900: 88-05-01-x0/00 and laterFor VSP E series: 93-02-02-60/00 and later  
Hitachi Ops Center API Configuration Manager| 10.1.0-00 and later *2  
  
*1 Some HyperFlex features require higher minimum versions.

*2 Some Hitachi Virtual Storage Platform models require higher minimum versions.

*3 Supported M6 servers: Cisco UCS C220 M6, C240 M6, C245 M6, and C225 M6 Servers.

*4 Supported M7 servers: Cisco UCS C220 M7 and C240 M7 Servers.

Important:

To use vCenter 7.0, you must update to the latest version for Intersight Assist. For more information, see [Updating the Intersight Connected Virtual Appliance Software](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/b_Cisco_Intersight_Appliance_Getting_Started_Guide/m_updating_the_intersight_virtual_appliance_software.html#Cisco_Task_in_List_GUI.dita_43af1cc4-8230-4d44-a643-5c5baabf78d0).

## Supported Hardware for Switches

System| Minimum Supported Version  
---|---  
Cisco Nexus Switch| The list of supported devices when the Claim Target option is used to claim the targets:

* Cisco Nexus 9200 Series
* Cisco Nexus 9300 Series
* Cisco Nexus 9400 Series
* Cisco Nexus 9500 Series
* Cisco Nexus 9800 Series

Requires NX-OS Release 10.2(3)F or later. For more information, see [Recommended Cisco NX-OS Releases for Cisco Nexus 9000 Series Switches](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/recommended_release/b_Minimum_and_Recommended_Cisco_NX-OS_Releases_for_Cisco_Nexus_9000_Series_Switches.html).The list of supported devices when the Claim Target with Assist option is used to the claim the targets:

* Cisco Nexus 9200 Series
* Cisco Nexus 9300 Series
* Cisco Nexus 9400 Series
* Cisco Nexus 9500 Series
* Cisco Nexus 9800 Series

The list of certified devices when the Claim Target with Assist option is used to the claim the targets:

* N9K-C9332PQ
* N9K-C9336C-FX2
* N9K-C9372PX
* N9K-C9396TX
* N9K-C93108TC-EX
* N9K-C93120TX
* N9K-C93128TX
* N9K-93180YC-EX
* N9K-C93180YC-FX
* N9K-C93600CD-GX
* N9K-C93360YC-FX2
* N9K-C9316D-GX
* N9K-C9516
* N9K-C9504

Requires NX-OS Release 9.3(9) or later. For more information, see [Recommended Cisco NX-OS Releases for Cisco Nexus 9000 Series Switches](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/recommended_release/b_Minimum_and_Recommended_Cisco_NX-OS_Releases_for_Cisco_Nexus_9000_Series_Switches.html).For the recommended release of Nexus Switches for the Fabric Interconnects, see [Fabric Interconnect and Nexus Switch Support Matrix](/help/supported_systems#fabric_interconnect_and_nexus_switch_support_matrix).  
Cisco MDS Switch| The list of supported devices when the Claim Target option is used to the claim the targets:

* Cisco MDS 9100 Series
* Cisco MDS 9200 Series
* Cisco MDS 9300 Series
* Cisco MDS 9700 Series

Requires NX-OS Release 9.3(2) or later. For more information, see [Recommended Releases for Cisco MDS 9000 Series Switches](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/mds9000/sw/b_MDS_NX-OS_Recommended_Releases.html).The list of supported devices when the Claim Target with Assist option is used to the claim the targets:

* Cisco MDS 9100 Series
* Cisco MDS 9200 Series
* Cisco MDS 9300 Series
* Cisco MDS 9700 Series

The list of certified devices when the Claim Target with Assist option is used to the claim the targets:

* DS-C9132T-MEK9
* DS-C9132T-MIK9
* DS-C9148S-K9
* DS-C9148T-K9
* DS-C9396S-K9
* DS-C9396T-K9

Requires NX-OS Release 8.4(2a) or later. For more information, see [Recommended Releases for Cisco MDS 9000 Series Switches](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/mds9000/sw/b_MDS_NX-OS_Recommended_Releases.html).For the recommended release of MDS for the Fabric Interconnects, see [Fabric Interconnect and MDS Switch Support Matrix](/help/supported_systems#fabric_interconnect_and_mds_switch_support_matrix).  
  
## Fabric Interconnect and Nexus Switch Support Matrix

* For information on the support matrix for FI and Nexus switches in Cisco Intersight Infrastructure firmware release 6.0, see [Release Notes for Cisco Intersight Managed Mode Infrastructure Firmware, Release 6.0](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/6-0/b-intersight-infrastructure-fw-rn-6-0/m-compatibility.html#r_fi_mds_support_matrix).
* For information on the support matrix for FI and Nexus switches in Cisco Intersight Infrastructure firmware release 4.3, see [Release Notes for Cisco Intersight Managed Mode Infrastructure Firmware, Release 4.3](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/imm_infra_fw_rn_4_3/b_imm_infra_fw_rn_lb.html#r_fi_mds_support_matrix).

## Fabric Interconnect and MDS Switch Support Matrix

* For information on the support matrix for FI and MDS switches in release 6.0, see [Release Notes for Cisco Intersight Managed Mode Infrastructure Firmware, Release 6.0](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/6-0/b-intersight-infrastructure-fw-rn-6-0/m-compatibility.html#r_fi_mds_support_matrix).
* For information on the support matrix for FI and MDS switches in release 4.3, see [Release Notes for Cisco Intersight Managed Mode Infrastructure Firmware, Release 4.3](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/imm_infra_fw_rn_4_3/b_imm_infra_fw_rn_lb.html#r_fi_mds_support_matrix).

Note:

For older supported release only MDS recommended minor version are supported [Recommended Releases for Cisco MDS 9000 Series Switches](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/mds9000/sw/b_MDS_NX-OS_Recommended_Releases.html).

## Intersight Essentials Features

Cisco Intersight Essentials license tier includes all the features listed below:

table_essentials.html

* * For the details on the list of server sctions, see [Server Actions](/help/operate/servers#server_actions).
* ** When you navigate to the individual Server Details page from the Servers table view, you can view additional details including full inventory, HCL status, status of the server profiles, and a graphical view of the server. You can also view details of the alarms on a particular server.
* *** Chassis storage disk images for the Cisco UCS S-Series M4/M5 Servers are not displayed in the Images panel on the **Server Details** page, but the **Inventory** tab displays the disks when they are assigned to a server.
* *b Supports HyperFlex Data Platform versions:
* 6.0(1b)
* 5.5(1a), 5.5(2a)
* 5.0(2e), 5.0(2g)

HXDP versions 5.0(2d), 5.0(2c), 5.0(2b), 5.0(2a), 4.5(2a), 4.5(2b), 4.5(2c), 4.5(2d), and 4.5(2e) are supported for cluster expansion only.

Upgrades from HXDP 4.0.2x are supported provided the ESXi version is compatible with 4.5(2x). You can upgrade both at the same time. For example, upgrade HXDP 4.0.2x + ESXi 6.0 to HXDP 4.5 + ESXi 6.5.

* *1 Cisco UCS Manager 3.1(2c) and later on all platforms.
* *2 Enabled by the **OS Discovery Tool**.
* *3 Requires HyperFlex Data Platform 4.0(1a) and later for HyperFlex cluster upgrade.
* *4 Cisco UCS C220 M6, C240 M6, C225 M6, and C245 M6 servers are supported in all modes.
* *5 Cisco UCS B200 M6 servers are supported.
* *6M2 servers are supported till Cisco UCS Manager Release 3.2(3).
* *7 M3 servers are supported till Cisco UCS Manager Release 4.1(3)

M4 servers running in UCS Manager Mode are supported until Cisco UCS Manager Release 4.2(3).

* *8 Server firmware upgrade is supported as part of HyperFlex cluster upgrade operation
* *9 Cisco UCS C480 ML M5 server, Cisco UCS C125 M5, and S3260 M5 servers are not supported in Intersight Managed Mode.

For more information about features that do not require extra licensing, see [Cisco UCS Servers | License Lifecycle](/help/getting_started/licensing_requirements/lic_infra#cisco_ucs_servers_%7C_license_lifecycle).

Note:

Cisco UCS-based appliances such as CSP 2100, CSP 5000, CDE 280, and CDE 220 are not supported in Intersight. They cannot be claimed or managed by Intersight.

## Intersight Advantage Features

Cisco Intersight Advantage license tier includes all the features of the Essentials license and the following additional features.

table_advantage.html

* *1 Requires a minimum of one UCS target with Advantage tier license.
* *2 M2 servers are supported till Cisco UCS Manager Release 3.2(3).
* *3 M3 servers are supported till Cisco UCS Manager Release 4.1(3).

M4 servers running in UCS Manager Managed Mode are supported until Cisco UCS Manager Release 4.2(3).

* *4 Cisco UCS C480 ML M5 server and Cisco UCS C125 M5 server are not supported in Intersight Managed Mode.

For more information about features that do not require extra licensing, see [Cisco UCS Servers | License Lifecycle](/help/getting_started/licensing_requirements/lic_infra#cisco_ucs_servers_%7C_license_lifecycle).

Legend

table_legend.html

## Supported Maximum Limits

Cisco Intersight imposes the maximum limits for the following features per Intersight account:

* HyperFlex Cluster deployment from Intersight—4 concurrent deployments
* Context-launch Cisco UCS Manager and Cisco IMC GUI and CLI sessions and the number of entries in the Users table—32
* Launch vKVM session from Intersight—Four sessions (Logged in with the KVM credentials)
* Session timeout for the Intersight GUI (Web browser) and API Sessions—Default idle timeout period is 30 minutes
* GUI and API sessions per user for an Intersight account—32 concurrent sessions
* Maximum number of entries in the Users table per Intersight account—200
* Maximum number of simultaneous Server Firmware Upgrades that can be triggered—100
* Maximum number of Tunneled vKVM Sessions per server—1
* Maximum number of concurrent OS Install requests per account—75

## Validated Identity Providers

Cisco Intersight has validated the following IdPs:

* Okta
* Microsoft Azure AD
* AD FS
* OneLogin
* SimpleSAMLphp
* Shibboleth
* WSO2
* PingFederate

Note:

For more information about IdPs, see [Single Sign-On](/help/appliance/settings#single_sign-on_\(sso\)).

## Firmware Requirements for Launching IMC from Device Console

Supported Server| Minimum Firmware Version  
---|---  
Cisco UCS C-Series servers in Intersight Managed Mode| 4.3(6.250039)  
  
For more information, see the Servers Subtab section in [Device Console](https://intersight.com/help/saas/device_console#servers_subtab).

## **Firmware Requirements for Scrub Policy**

Supported Server| Minimum Firmware Version  
---|---  
Cisco UCS C-Series M5 servers in Intersight Managed Mode| 4.3(2.240053)  
Cisco UCS C-Series M6 and later servers in Intersight Managed Mode| 4.3(4.240152)  
Cisco UCS B-Series servers in Intersight Managed Mode| 5.2(2.240051)  
Cisco UCS X-Series servers in Intersight Managed Mode| 5.2(2.240053)  
  
For more information, see the _Creating a Scrub Policy_ section in [Configuring UCS Server Policies](/help/resources/cisco_intersight_managed_mode_configuration#configuring_ucs_server_policies).

## **Firmware Requirements for LDAP and Certificate Management Policies**

The minimum infrastructure firmware version required to support the LDAP policy and Certificate Management policy for a UCS domain is as follows:

Fabric Interconnect| Minimum Infrastructure Firmware Version  
---|---  
Cisco UCS 6400 Series| 4.3(4.240066)  
Cisco UCS 6500 Series| 4.3(4.240066)  
Cisco UCS X-Series Direct| 4.3(4.240078)  
  
For more information, see the _Creating an LDAP Policy_ and _Creating a Certificate Management Policy_ sections in [Configuring UCS Server Policies](/help/resources/cisco_intersight_managed_mode_configuration#configuring_ucs_server_policies).

## Firmware Requirements for Secure Self-Encrypting Drives

Category| Requirement  
---|---  
Supported modes| Intersight Managed Mode and Cisco UCS C-Series Standalone mode  
Minimum firmware version for Cisco UCS C-Series Standalone servers| Cisco IMC release 4.1(2a)  
Key Management Interoperability Protocol (KMIP) servers| Validated KMIP server is Thales® [CipherTrust Manager](https://cpl.thalesgroup.com/resources/encryption/ciphertrust-manager-product-brief).Note:Ensure that you configure the following settings:

* While setting up the Thales® Cipher Trust KMIP manager, on the KMIP Manager UI, enable the Auto-registration setting under Admin settings with the Registration Token.
* While generating the Certificate Signing Request (CSR) certificate in the KMIP server, ensure that the same Common Name (server hostname) is used (see [Configuring KMIP Client Certificate](/help/resources/Securing_Data_on_Self_Encrypting_Drives#configuring_kmip_client_certificate)).

  
  
For more information, see [Securing Data on Self-Encrypting Drives using KMIP](/help/resources/Securing_Data_on_Self_Encrypting_Drives).

## Firmware Requirements for Chassis and Server–Limit and Utilization Metrics Collection

Supported Server| Minimum Firmware Version  
---|---  
UCS X-Series Blade servers in Intersight Managed Mode| X-Series: 5.2(2.240053)  
UCS M6+ Rack Server servers in Intersight Managed Mode| C-Series (M6+): 4.3(4.240152)  
UCS X-Series Chassis servers in Intersight Managed Mode| X-IFMs: 4.3(4a)  
  
## Firmware Requirements for VIC Metrics Collection

Supported Server| Minimum Firmware Version  
---|---  
UCS C-Series servers in Intersight Managed Mode| Server firmware version 4.3(2.230207)  
UCS X-Series servers in Intersight Managed Mode| 

* UCSX-210C-M6: Server firmware version 5.2(0.230039)
* UCSX-210C-M7 or UCSX-410C-M7: Server firmware version 5.2(0.230041)

  
  
Note:

The VIC metrics are collected for only logical interfaces, and this data collection occurs when the servers are in the powered on state.

## Firmware Requirements for Power Policy

Supported Server| Minimum Firmware Version  
---|---  
Cisco UCS X-Series servers in Intersight Managed Mode in Cisco-UCSX-9508 chassis| Server firmware version 4.2(1e)  
Cisco UCS B-Series servers in Intersight Managed Mode in Cisco-UCSB-5108 chassis| Server firmware version 4.2(1d)  
Cisco UCS C-Series M5 and later servers in Intersight Managed Mode| Server firmware version 4.2(1e)  
Cisco UCS C-Series M5 and later servers in Standalone mode| Server firmware version 4.2(1e)  
  
For more information, see the _Creating a Power Policy for a Server_ section in [Supported UCS Server Policies](/help/resources/cisco_intersight_managed_mode_configuration#configuring_ucs_server_policies).

## Firmware Requirements for iSCSI Boot Option

Supported Server| Minimum Firmware Version  
---|---  
Cisco UCS B-Series, C-Series, and X-Series servers in Intersight Managed Mode| Infrastructure firmware version 4.1(3b)  
  
For more information, see the _Configuring an iSCSI Boot Policy_ section in [Supported UCS Server Policies](/help/resources/cisco_intersight_managed_mode_configuration#supported_ucs_server_policies).

## Firmware Requirements for FlexMMC Boot Option

Supported Server| Firmware Version  
---|---  
Cisco UCS C-Series servers in Standalone mode and Intersight Managed Mode| Server firmware version 4.3(3.240028) and later  
  
For more information, see the _Creating a Boot Order Policy_ section in [Supported UCS Server Policies](/help/resources/cisco_intersight_managed_mode_configuration#configuring_ucs_server_policies).

## Firmware Requirements for HTTP Boot Option

Supported Server| Firmware Version  
---|---  
Cisco UCS B-Series, C-Series servers in Intersight Managed Mode| Infrastructure firmware version 4.2(2a) or later  
Cisco UCS C-Series M5 and later servers in Standalone mode| Infrastructure firmware version 4.2(2a) or later  
Cisco UCS X-Series M6 and later servers in Intersight Managed Mode| Server firmware version 5.0(2a) or laterInfrastructure firmware version 4.2(2a) or later  
  
For more information, see the _Creating a Boot Order Policy_ section in [Supported UCS Server Policies](/help/resources/cisco_intersight_managed_mode_configuration#supported_ucs_server_policies).

## Firmware Requirements for Memory Policy

Supported Server| Minimum Firmware Version  
---|---  
Intersight Managed Mode:Cisco UCS B-Series M5 and laterCisco UCS C220, C240, and C480 M5Cisco UCS C220, C240 M6 and later| Server firmware version 4.2(2a)  
Standalone ModeCisco UCS C220, C240, C480 M5Cisco UCS C220, C240 M6 and later| Server firmware version 4.2(2a)  
Intersight Managed Mode:Cisco UCS X210c M6 and laterCisco UCS X410c M7| Server firmware version 5.0(2a)  
  
For more information, see the _Configuring a memory policy for a server_ section in [Supported UCS Server Policies](/help/resources/cisco_intersight_managed_mode_configuration#supported_ucs_server_policies).

## Firmware Requirements for Core Files Management

Supported Server| Minimum Firmware Version  
---|---  
Cisco UCS B-Series and X-Series servers| Server firmware version 5.2(2a)Infrastructure firmware version 4.3(4a)  
Cisco UCS C-Series servers| Server firmware version 4.3(4a)Infrastructure firmware version 4.3(4a)  
  
For more information, see [Core Files](/help/system/diagnostic_data#core_files).

## Supported Hardware and Software Versions For Third-Party Devices

* Hitachi Virtual Storage Platform
* VSP One Block (B20): A3-02-21-x0/01 and later
* VSP 5000 series: 90-03-01-00/00 and later
* VSP G1000, G1500 and F1500: 80-06-75-00/00 and later
* VSP G/F 350,370,700,900: 88-05-01-x0/00 and later
* VSP E Series: 93-02-02-60/00 and later
* Hitachi Ops Center API Configuration Manager
* 10.1.0-00 and later*1

*1 Some Hitachi Virtual Storage Platform models require higher minimum versions.

* Pure Storage FlashArray with Purity version FA 4.8 to FA 6.0.2 (REST API 1.x only) or Purity version FA 6.0.3 or later (REST API 1.x and REST API 2.x).
* VMware vCenter versions 7.0 and 8.0
* Dell PowerEdge and HPE ProLiant servers which support Redfish APIs.

## Cisco UCS NVMeoF Support Matrix for Third-Party Storage Vendors

* For information on Cisco UCS NVMeoF Support Matrix for Third-Party Storage Vendors in Cisco Intersight Infrastructure firmware release 6.0, see [Release Notes for Cisco Intersight Managed Mode Infrastructure Firmware, Release 6.0](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/6-0/b-intersight-infrastructure-fw-rn-6-0/m-compatibility.html#r_third_party_storage_6_0).
* For information on Cisco UCS NVMeoF Support Matrix for Third-Party Storage Vendors in Cisco Intersight Infrastructure firmware release 4.3, see [Release Notes for Cisco Intersight Managed Mode Infrastructure Firmware, Release 4.3](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/imm_infra_fw_rn_4_3/b_imm_infra_fw_rn_lb.html#r_third_party_storage_matrix).