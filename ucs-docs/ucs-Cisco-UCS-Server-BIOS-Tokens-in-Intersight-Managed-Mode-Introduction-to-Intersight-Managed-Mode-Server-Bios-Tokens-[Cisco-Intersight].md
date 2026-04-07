# IMM UCS Server BIOS tokens

| | |
|---|---|
| **URL Title** | IMM UCS Server BIOS tokens |
| **URL** | https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/b_UCS_BIOS_Tokens_Guide_chapter_01.html |
| **Long URL** |  |
| **HTML Title** | Cisco UCS Server BIOS Tokens in Intersight Managed Mode - Introduction to Intersight Managed Mode Server Bios Tokens [Cisco Intersight] |
| **Source file** | `ucs-docs-raw/html/b_UCS_BIOS_Tokens_Guide_chapter_01.html` |
| **File type** | HTML |
| **Fetched on** | 2026-04-08 08:43:03 |

---

## Page 1: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/b_UCS_BIOS_Tokens_Guide_chapter_01.html

## Introduction to Intersight Managed Mode Server BIOS Tokens

Intersight Managed Mode provides two methods for making global modifications to the BIOS settings on servers in Cisco UCS domain. You can create one or more BIOS policies that include a specific grouping of BIOS settings that match the needs of a server or set of servers, or you can use the Cisco provided predefined BIOS policy settings which are optimized for particular server platforms and use cases. 

Both the BIOS policy and the default BIOS settings for a server platform enables you to fine tune the BIOS settings for a server managed by IMM. 

Depending on the specific workload requirements of a data center such as CPU-intensive, I/O-intensive, or energy-efficient operations and so on, Cisco provides optimized, ready-to-use BIOS token configurations. These configurations are designed to streamline policy deployment and enhance system performance by aligning BIOS settings with workload demands. Additionally, custom policies can be created to meet unique requirements. 

Cisco Intersight Managed Mode supports the following M5, M6, M7, and M8 servers: 

  * Cisco UCS C220 M8, Cisco UCS C240 M8, Cisco UCS X210c M8, and Cisco UCS X410c M8 Compute Node

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The platforms are supported from the following firmware versions onwards: 
  * For Cisco UCS C220 M8 and Cisco UCS C240 M8 from 4.3(6.250039)
  * For Cisco UCS X210c M8 from 5.4(0.250037)
  * Cisco UCS X410c M8 from 6.0(2.260040)

* * *  
  
---|---  
  * Cisco UCS C225 M8 and Cisco UCS X215c M8 Compute Node

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The platforms are supported from the following firmware versions onwards: 
  * For Cisco UCS C225 M8 from 4.3(5.240021)
  * For Cisco UCS X215c M8 from 5.3(0.240016)

* * *  
  
---|---  
  * Cisco UCS C245 M8

  * Cisco UCS X210c M7 Compute Node

  * Cisco UCS X410c M7 Compute Node

  * Cisco UCS X210c M6 Compute Node

  * Cisco UCS C220 M7

  * Cisco UCS C240 M7

  * Cisco UCS C220 M6

  * Cisco UCS C225 M6

  * Cisco UCS C240 M6

  * Cisco UCS C245 M6

  * Cisco UCS C220 M5

  * Cisco UCS C240 M5

  * Cisco UCS C480 M5

  * Cisco UCS B200 M6

  * Cisco UCS B200 M5

  * Cisco UCS B480 M5


![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The Version column in the table denotes the minimum firmware version where the BIOS token is supported and its consecutive version support. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For tokens having long value description, the Values column can be seen blank. In this case, you can scroll down the column to see their values. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

All tokens also include a 'Platform default' option. The Platform default is identified by the setting in bold font. The BIOS uses the value for this attribute contained in the BIOS defaults for the server type and vendor. 

* * *  
  
---|---  
  
### What's New

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

This document includes BIOS token information starting from 4.3(3a) and continue to cover all subsequent versions. It does not cover any versions prior to 4.3(3a). 

* * *  
  
---|---  
Table 1. **New/Changed BIOS Tokens for 6.0(2.260040)** BIOS Token |  Platform |  New/Changed  
---|---|---  
Speculative Lock |  C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8 |  New  
CPU Frequency Control |  C245 M8, C225 M8, X215c M8 |  New  
Uncore Frequency Scaling IO |  C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8 |  New  
Uncore Frequency Scaling |  X410c M8 |  New  
GPU Direct CPU1 |  X410c M8 |  New  
GPU Direct CPU2 |  X410c M8 |  New  
GPU Direct CPU3 |  X410c M8 |  New  
GPU Direct CPU4 |  X410c M8 |  New  
IIO eDPC Support |  X410c M8 |  New  
Total Memory Encryption (TME) |  X410c M8 |  New  
Multikey Total Memory Encryption (MK-TME) |  X410c M8 |  New  
SW Guard Extensions (SGX) |  X410c M8 |  New  
SGX Factory Reset |  X410c M8 |  New  
SGX Package info In-Band Access |  X410c M8 |  New  
SGX QoS |  X410c M8 |  New  
Select Owner EPOCH Input type |  X410c M8 |  New  
SGX Write Enable |  X410c M8 |  New  
SGX Auto MP Registration Agent |  X410c M8 |  New  
SProcessor Epoch 0 |  X410c M8 |  New  
SProcessor Epoch 1 |  X410c M8 |  New  
SGX PUBKEY HASH0 |  X410c M8 |  New  
SGX PUBKEY HASH1 |  X410c M8 |  New  
SGX PUBKEY HASH2 |  X410c M8 |  New  
SGX PUBKEY HASH3 |  X410c M8 |  New  
UMA |  X410c M8 |  New  
Virtual Numa |  X410c M8 |  New  
XPT Remote Prefetch |  X410c M8 |  New  
LLC Dead Line |  X410c M8 |  New  
Enhanced CPU Performance |  X410c M8 |  New  
UPI Link Enablement |  X410c M8 |  New  
UPI Power Manangement |  X410c M8 |  New  
UPI Link Speed |  X410c M8 |  New  
UPI Link Frequency Select |  X410c M8 |  New  
LIMIT CPU PA to 46 Bits |  X410c M8 |  New  
Adaptive Refresh Management Level |  X410c M8 |  New  
Rank Margin Tool |  X410c M8 |  New  
Trust Domain Extension (TDX) |  X410c M8 |  New  
TDX Secure Arbitration Mode (SEAM) Loader |  X410c M8 |  New  
MMIO High Base |  X410c M8 |  New  
MMIO High Granularity Size |  X410c M8 |  New  
IOAT Configuration |  X410c M8 |  New  
DFX OSB |  X410c M8 |  New  
Re-Size BAR Support |  X410c M8 |  New  
PreBoot DMA Protection |  X410c M8 |  New  
UEFI Memory Map Special Purpose Memory Flag |  X410c M8 |  New  
ACPI SRAT Special Purpose Memory Flag |  X410c M8 |  New  
Latency Optimized Mode |  X410c M8 |  New  
Run Time Post Package Repair |  X410c M8 |  New  
USB Port Front |  X410c M8 |  New  
USB Port KVM |  X410c M8 |  New  
USB Port:M.2 Storage |  X410c M8 |  New  
Memory Thermal Throttling Mode |  X410c M8 |  New  
Enhanced Memory Test |  X410c M8 |  New  
IPv4 HTTP Support |  X410c M8 |  New  
IPv6 HTTP Support |  X410c M8 |  New  
DMA Control Opt-In Flag |  X410c M8 |  New  
Error Check Scrub |  X410c M8 |  New  
PRMRR Size |  X410c M8 |  New  
FRB 2 Timer |  X410c M8 |  New  
OS Boot Watchdog Timer Policy |  X410c M8 |  New  
OS Watchdog Timer Timeout |  X410c M8 |  New  
OS Boot Watchdog Timer |  X410c M8 |  New  
Flow Control |  X410c M8 |  New  
Baud rate |  X410c M8 |  New  
Terminal type |  X410c M8 |  New  
Console redirection |  X410c M8 |  New  
Security Device Support |  X410c M8 |  New  
Trusted Platform Module State |  X410c M8 |  New  
SHA-1 PCR Bank |  X410c M8 |  New  
SHA256 PCR Bank |  X410c M8 |  New  
SHA384 PCR Bank |  X410c M8 |  New  
TPM Pending Operation |  X410c M8 |  New  
TPM Minimal Physical Presence |  X410c M8 |  New  
Intel(R) VT |  X410c M8 |  New  
NUMA |  X410c M8 |  New  
Select Memory RAS Configuration |  X410c M8 |  New  
Select PPR Type |  X410c M8 |  New  
Memory Mapped IO above 4GB |  X410c M8 |  New  
Hardware Prefetcher |  X410c M8 |  New  
Adjacent Cache Line Prefetcher |  X410c M8 |  New  
DCU Streamer Prefetch |  X410c M8 |  New  
DCU IP Prefetcher |  X410c M8 |  New  
Processor C1E |  X410c M8 |  New  
Processor C6 Report |  X410c M8 |  New  
Intel Turbo Boost Tech |  X410c M8 |  New  
P STATE Coordination |  X410c M8 |  New  
Boot Performance Mode |  X410c M8 |  New  
Enhanced Intel Speedstep(R) Technology |  X410c M8 |  New  
Enhanced Memory Test |  X410c M8 |  New  
Configurable TDP Level |  X410c M8 |  New  
Intel HyperThreading Tech |  X410c M8 |  New  
CDN Control |  X410c M8 |  New  
Processor CMCI |  X410c M8 |  New  
Adaptive Memory Training |  X410c M8 |  New  
OptionROM Launch Optimization |  X410c M8 |  New  
BIOS Techlog Level |  X410c M8 |  New  
VMD Enable |  X410c M8 |  New  
Core Multi Processing |  X410c M8 |  New  
Workload Configuration |  X410c M8 |  New  
Sub Numa Clustering |  X410c M8 |  New  
KTI Prefetch |  X410c M8 |  New  
XPT Prefetch |  X410c M8 |  New  
Power Performance Tuning |  X410c M8 |  New  
Energy Performance |  X410c M8 |  New  
Package C State Limit |  X410c M8 |  New  
LLC Prefetch |  X410c M8 |  New  
IPV6 PXE Support |  X410c M8 |  New  
Energy Efficient Turbo |  X410c M8 |  New  
Processor EPP Profile |  X410c M8 |  New  
Patrol Scrub |  X410c M8 |  New  
Intel Speed Select |  X410c M8 |  New  
Intel Dynamic Speed Select |  X410c M8 |  New  
BME DMA Mitigation |  X410c M8 |  New  
Partial Memory Mirror Mode |  X410c M8 |  New  
Partial Mirror percentage |  X410c M8 |  New  
Memory Size Limit in GB |  X410c M8 |  New  
Network Stack |  X410c M8 |  New  
IPV4 PXE Support |  X410c M8 |  New  
IPV6 PXE Support |  X410c M8 |  New  
xGMI Link Configuration |  C245M6, C225M6 |  Updated  
Table 2. **New/Changed BIOS Tokens for 6.0(1.250229)** BIOS Token |  Platform |  New/Changed  
---|---|---  
GPU Direct CPU1 |  X210c M8 |  New  
GPU Direct CPU2 |  X210c M8 |  New  
Table 3. **New/Changed BIOS Tokens for 6.0(1a.0)** BIOS Token |  Platform |  New/Changed  
---|---|---  
Uncore Frequency Scaling |  XE1X0M8 |  New  
Uncore Frequency Scaling IO |  XE1X0M8 |  New  
C1 Auto Demotion |  XE1X0M8 | New  
C1 Auto UnDemotion |  XE1X0M8 |  New  
Partial Mirror percentage  |  XE1X0M8 |  New  
PCIe Slot MSTOR RAID OptionROM |  XE1X0M8 |  New  
PCIe Slots CDN Control |  XE1X0M8 |  New  
PCIe Slot n Link Speed |  XE1X0M8 |  New  
PCIe Slot n Option ROM |  XE1X0M8 |  New  
PCIe RAS Support |  XE1X0M8 |  New  
Power ON Password |  XE1X0M8 |  New  
Multikey Total Memory Encryption (MK-TME) |  XE1X0M8 |  New  
Total Memory Encryption (TME) |  XE1X0M8 |  New  
SGX Auto MP Registration Agent |  XE1X0M8 |  New  
SGX QoS |  XE1X0M8 |  New  
SGX Write Enable |  XE1X0M8 |  New  
Sgx-Epoch |  XE1X0M8 |  New  
SProcessor Epoch 0 |  XE1X0M8 |  New  
SProcessor Epoch 1 |  XE1X0M8 |  New  
SGX PubKey Hashn |  XE1X0M8 |  New  
UMA |  XE1X0M8 |  New  
NUMA |  XE1X0M8 |  New  
Virtual Numa |  XE1X0M8 |  New  
LLC Dead Line |  XE1X0M8 |  New  
IPV6 HTTP Support |  XE1X0M8 |  New  
IPV4 HTTP Support |  XE1X0M8 |  New  
DMA Control Opt-In Flag |  XE1X0M8 |  New  
Error Check Scrub |  XE1X0M8 |  New  
PRMRR Size |  XE1X0M8 |  New  
Core Multi Processing |  XE1X0M8 |  New  
Select Owner EPOCH Input Type |  XE1X0M8 |  New  
IPV4 PXE Support |  XE1X0M8 |  New  
IPV6 PXE Support |  XE1X0M8 |  New  
Network Stack |  XE1X0M8 |  New  
Consistent Device Naming (CDN) Control |  XE1X0M8 |  New  
Enhanced Memory Test  |  XE1X0M8 |  New  
BME DMA Mitigation |  XE1X0M8 |  New  
MMIO High Granularity Size |  XE1X0M8 |  New  
MMIO High Base  |  XE1X0M8 |  New  
Select Memory RAS Configuration |  XE1X0M8 |  New  
Memory mapped IO above 4GB  |  XE1X0M8 |  New  
Adjacent Cache Line Prefetcher  |  XE1X0M8 |  New  
DFX OSB |  XE1X0M8 |  New  
Processor CMCI |  XE1X0M8 |  New  
Configurable TDP Level  |  XE1X0M8 |  New  
Energy Performance |  XE1X0M8 |  New  
Enhanced Intel SpeedStep Tech  |  XE1X0M8 |  New  
Processor EPP Profile  |  XE1X0M8 |  New  
IOAT Configuration |  XE1X0M8 |  New  
Hardware Prefetcher  |  XE1X0M8 |  New  
CPU Hardware Power Management |  XE1X0M8 |  New  
Intel Dynamic Speed Select  |  XE1X0M8 |  New  
Intel HyperThreading Tech |  XE1X0M8 |  New  
Intel Turbo Boost Tech |  XE1X0M8 |  New  
Intel Speed Select |  XE1X0M8 |  New  
Intel Trusted Execution Technology Support |  XE1X0M8 |  New  
Intel(R) VT |  XE1X0M8 |  New  
DCU IP Prefetcher |  XE1X0M8 |  New  
KTI Prefetch |  XE1X0M8 |  New  
LLC Prefetch |  XE1X0M8 |  New  
XPT Prefetch  |  XE1X0M8 |  New  
XPT Remote Prefetch |  XE1X0M8 |  New  
DCU Streamer Prefetch |  XE1X0M8 |  New  
Package C State |  XE1X0M8 |  New  
Patrol Scrub Configuration  |  XE1X0M8 |  New  
Processor C1E |  XE1X0M8 |  New  
Processor C6 Report  |  XE1X0M8 |  New  
EIST PSD Function |  XE1X0M8 |  New  
Sub Numa Clustering |  XE1X0M8 |  New  
Workload Configuration |  XE1X0M8 |  New  
USB Port Front |  XE1X0M8 |  New  
USB Port KVM |  XE1X0M8 |  New  
USB Port:M.2 Storage |  XE1X0M8 |  New  
Sha-1 |  XE1X0M8 |  New  
Sha256 |  XE1X0M8 |  New  
Sha384 |  XE1X0M8 |  New  
Trusted Platform Module State |  XE1X0M8 |  New  
Trust Domain Extension |  XE1X0M8 |  New  
TDX Secure Arbitration Mode (SEAM) Loader |  XE1X0M8 |  New  
TPM Pending Operation |  XE1X0M8 |  New  
TPM Minimal Physical Presence |  XE1X0M8 |  New  
Front NVME n Link Speed  |  XE1X0M8 |  New  
Front NVME n Option rom  |  XE1X0M8 |  New  
Baud Rate |  XE1X0M8 |  New  
CDN Control |  XE1X0M8 |  New  
Adaptive Memory Training |  XE1X0M8 |  New  
Adaptive Refresh Management Level |  XE1X0M8 |  New  
BIOS Techlog Level |  XE1X0M8 |  New  
OptionROM Launch Optimization |  XE1X0M8 |  New  
Console Redirection |  XE1X0M8 |  New  
Flow Control |  XE1X0M8 |  New  
FRB 2 Timer |  XE1X0M8 |  New  
OS Boot Watchdog Timer Policy |  XE1X0M8 |  New  
OS Watchdog Timer Timeout |  XE1X0M8 |  New  
OS Watchdog Timer Policy |  XE1X0M8 |  New  
Terminal Type |  XE1X0M8 |  New  
Boot Performance Mode |  XE1X0M8 |  New  
Select PPR Type |  XE1X0M8 |  New  
Memory Thermal Throttling Mode  |  XE1X0M8 |  New  
Memory Size Limit in GB |  XE1X0M8 |  New  
QPI Link Frequency Select |  XE1X0M8 |  New  
IIO eDPC Support |  XE1X0M8 |  New  
P STATE Coordination |  XE1X0M8 |  New  
SGX Factory Reset |  XE1X0M8 |  New  
SGX Package Information In-Band Access |  XE1X0M8 |  New  
Security Device Support |  XE1X0M8 |  New  
LIMIT CPU PA to 46 Bits |  XE1X0M8 |  New  
Turbo Mode |  XE1X0M8 |  New  
Power Performance Tuning |  XE1X0M8 |  New  
CDN Support for LOM |  XE1X0M8 |  New  
Software Guard Extensions (SGX) |  XE1X0M8 |  New  
NUMA Optimized |  XE1X0M8 |  New  
Above 4G Decoding |  XE1X0M8 |  New  
Cores Enabled |  XE1X0M8 |  New  
Latency Optimized Mode |  XE1X0M8 |  New  
Runtime Post Package Repair |  XE1X0M8 |  New  
ACPI SRAT Special Purpose Memory Flag |  XE1X0M8 |  New  
UEFI Memory Map Special Purpose Memory Flag |  XE1X0M8 |  New  
Energy Efficient Turbo |  XE1X0M8 |  New  
Rank Margin Tool |  XE1X0M8 |  New  
Re-Size BAR Support |  XE1X0M8 |  New  
PreBoot DMA Protection |  XE1X0M8 |  New  
CPU Performance |  XE1X0M8 |  New  
Security Device Support |  XE1X0M8 |  New  
Table 4. **New/Changed BIOS Tokens for 6.0(1b)/6.0(1.250120)** BIOS Token |  Platform |  New/Changed  
---|---|---  
IIO eDPC Support |  X210c M8, X210c M7, X410c M7 |  New  
CDN Support for LOM |  C220 M8, C240 M8, X210c M8, X210c M7, X410c M7 |  Changed |  **Note** |  Support for the bios discontinued.   
---|---  
Table 5. **New/Changed BIOS Tokens for 4.3(6c)** BIOS Token |  Platform |  New/Changed  
---|---|---  
IIO eDPC Support |  C225 M8, C245 M8, X215c M8 |  New  
Sub NUMA Clustering |  C220 M8, C240 M8, X210c M8 |  Changed  
Table 6. **New/Changed BIOS Tokens for 4.3(6a)** BIOS Token |  Platform |  New/Changed  
---|---|---  
Latency Optimized Mode |  C220 M8, C240 M8, X210c M8 |  New  
PreBoot DMA Protection |  C220 M8, C240 M8, X210c M8 |  New  
Runtime Post Package Repair |  C220 M8, C240 M8, X210c M8 |  New  
MLOM OptionROM |  C220 M8, C240 M8 |  New  
MLOM Link Speed |  C220 M8, C240 M8 |  New  
Rear NVME n Link Speed |  C240 M8 |  New  
Rear NVME n OptionROM |  C240 M8 |  New  
PCIe Slot MSTOR RAID OptionROM |  C220 M8, C240 M8 |  New  
PCIe Slots CDN Control |  C220 M8, C240 M8 |  New  
Power ON Password |  C220 M8, C240 M8 |  New  
VGA Priority |  C220 M8, C240 M8 |  New  
USB Port Rear |  C220 M8, C240 M8 |  New  
USB Port Front |  X210c M8 |  New  
Multikey Total Memory Encryption (MK-TME) |  C220 M8, C240 M8, X210c M8 |  New  
Total Memory Encryption (TME) |  C220 M8, C240 M8, X210c M8 |  New  
SGX QoS |  C220 M8, C240 M8, X210c M8 |  New  
Select Owner EPOCH Input Type |  C220 M8, C240 M8, X210c M8 |  New  
SGX Write Enable |  C220 M8, C240 M8, X210c M8 |  New  
SGX Auto MP Registration Agent |  C220 M8, C240 M8, X210c M8 |  New  
Sgx-Epoch |  C220 M8, C240 M8, X210c M8 |  New  
SProcessor Epoch 1 |  C220 M8, C240 M8, X210c M8 |  New  
SGX PubKey Hashn |  C220 M8, C240 M8, X210c M8 |  New  
UMA |  C220 M8, C240 M8, X210c M8 |  New  
NUMA Optimized |  C220 M8, C240 M8, X210c M8 |  New  
UPI Link Enablement |  C220 M8, C240 M8, X210c M8 |  New  
UPI Power Manangement |  C220 M8, C240 M8, X210c M8 |  New  
LLC Dead Line |  C220 M8, C240 M8, X210c M8 |  New  
Enhanced CPU Performance |  C240 M8, X210c M8  |  New  
IPV6 HTTP Support |  C220 M8, C240 M8, X210c M8 |  New  
IPV4 HTTP Support |  C220 M8, C240 M8, X210c M8 |  New  
DMA Control Opt-In Flag | C220 M8, C240 M8, X210c M8 |  New  
Error Check Scrub | C220 M8, C240 M8, X210c M8 |  New  
PRMRR Size | C220 M8, C240 M8, X210c M8 |  New  
UEFI Memory Map Special Purpose Memory Flag |  C220 M8, C240 M8, X210c M8 |  New  
ACPI SRAT Special Purpose Memory Flag |  C220 M8, C240 M8, X210c M8 |  New  
Re-Size BAR Support |  C220 M8, C240 M8, X210c M8 |  New  
Core Multi Processing |  C220 M8, C240 M8, X210c M8 |  New  
Select Owner EPOCH Input Type |  C220 M8, C240 M8 |  New  
VMD Enablement |  C220 M8, C240 M8, X210c M8 |  New  
IPV4 PXE Support |  C220 M8, C240 M8, X210c M8 |  New  
IPV6 PXE Support |  C220 M8, C240 M8, X210c M8 |  New  
Network Stack |  C220 M8, C240 M8, X210c M8 |  New  
MRAIDn Link Speed |  C240 M8 |  New  
MRAID n OptionROM |  C240 M8 |  New  
MRAID Option ROM |  C220 M8 |  New  
MRAID Link Speed |  C220 M8 |  New  
Consistent Device Naming (CDN) Control |  C220 M8, C240 M8, X210c M8 |  New  
Enhanced Memory Test  | C220 M8, C240 M8, X210c M8 |  New  
BME DMA Mitigation |  C220 M8, C240 M8, X210c M8 |  New  
MMIO High Granularity Size |  C220 M8, C240 M8, X210c M8 |  New  
MMIO High Base  |  C220 M8, C240 M8, X210c M8 |  New  
Partial Mirror percentage  |  C220 M8, C240 M8, X210c M8 |  New  
Memory RAS Configuration |  C220 M8, C240 M8, X210c M8 |  New  
Memory mapped IO above 4GB  | C220 M8, C240 M8, X210c M8 |  New  
PRMRR Size |  C220 M8, C240 M8, X210c M8 |  New  
Adjacent Cache Line Prefetcher  |  C220 M8, C240 M8, X210c M8 |  New  
DFX OSB | X210c M8 |  New  
Processor CMCI |  C220 M8, C240 M8, X210c M8 |  New  
Configurable TDP Level  |  C220 M8, C240 M8, X210c M8 |  New  
Energy Performance |  C220 M8, C240 M8, X210c M8 |  New  
Enhanced Intel SpeedStep Tech  |  C220 M8, C240 M8, X210c M8 |  New  
Processor EPP Profile  |  C220 M8, C240 M8, X210c M8 |  New  
IOAT Configuration |  C220 M8, C240 M8, X210c M8 |  New  
Hardware Prefetcher  |  C220 M8, C240 M8, X210c M8 |  New  
CPU Hardware Power Management |  C220 M8, C240 M8, X210c M8 |  New  
Intel Dynamic Speed Select  |  C220 M8, C240 M8, X210c M8 |  New  
Intel HyperThreading Tech |  C220 M8, C240 M8, X210c M8 |  New  
Intel Turbo Boost Tech |  C220 M8, C240 M8, X210c M8 |  New  
Intel(R) VT |  C220 M8, C240 M8, X210c M8 |  New  
DCU IP Prefetcher |  C220 M8, C240 M8, X210c M8 |  New  
KTI Prefetch |  C220 M8, C240 M8, X210c M8 |  New  
LLC Prefetch |  C220 M8, C240 M8, X210c M8 |  New  
Package C State | C220 M8, C240 M8, X210c M8  |  New  
Patrol Scrub Configuration  | C220 M8, C240 M8, X210c M8  |  New  
Processor C1E |  C220 M8, C240 M8, X210c M8  |  New  
Processor C6 Report  |  C220 M8, C240 M8, X210c M8  |  New  
P STATE Coordination |  C220 M8, C240 M8, X210c M8  |  New  
UPI Link Speed  |  C220 M8, C240 M8, X210c M8  |  New  
Sub Numa Clustering |  C220 M8, C240 M8, X210c M8  |  New  
Uncore Frequency Scaling  |  C220 M8, C240 M8, X210c M8  |  New  
Workload Configuration |  C220 M8, C240 M8, X210c M8  |  New  
XPT Prefetch  |  C220 M8, C240 M8, X210 M8  |  New  
Intel Speed Select |  C220 M8, C240 M8, X210c M8  |  New  
USB Port KVM | X210c M8 |  New  
USB Port:M.2 Storage |  X210 M8 |  New  
Sha-1 |  C220 M8, C240 M8, X210c M8  |   
Sha256 |  C220 M8, C240 M8, X210c M8  |  New  
Sha384 |  C220 M8, C240 M8, X210c M8  |  New  
Trusted Platform Module State |  C220 M8, C240 M8, X210c M8  |  New  
Trust Domain Extension |  C220 M8, C240 M8, X210c M8  |  New  
TDX Secure Arbitration Mode (SEAM) Loader |  C220 M8, C240 M8, X210c M8  |  New  
TPM Pending Operation |  C220 M8, C240 M8, X210c M8  |  New  
TPM Minimal Physical Presence |  C220 M8, C240 M8, X210c M8  |  New  
Intel Trusted Execution Technology Support |  C220 M8, C240 M8, X210c M8  |  New  
Rear NVME nLink Speed  |  C240 M8 |  New  
Rear NVME noption rom  |  C240 M8 |  New  
Front NVME n Link Speed  |  C220 M8, C240 M8 |  New  
Front NVME n ption rom  |  C220 M8, C240 M8 |  New  
Baud Rate | C220 M8, C240 M8, X210c M8 |  New  
CDN Control | C220 M8, C240 M8, X210c M8 |  New  
Adaptive Memory Training | C220 M8, C240 M8, X210c M8 |  New  
BIOS Techlog Level | C220 M8, C240 M8, X210c M8 |  New  
OptionROM Launch Optimization | C220 M8, C240 M8, X210c M8 |  New  
Console Redirection | C220 M8, C240 M8, X210c M8 |  New  
Flow Control | C220 M8, C240 M8, X210c M8 |  New  
FRB 2 Timer | C220 M8, C240 M8, X210c M8 |  New  
OS Boot Watchdog Timer Policy | C220 M8, C240 M8, X210c M8 |  New  
OS Watchdog Timer Timeout | C220 M8, C240 M8, X210c M8 |  New  
OS Watchdog Timer | C220 M8, C240 M8, X210c M8 |  New  
Terminal Type | C220 M8, C240 M8, X210c M8 |  New  
PCIe Slot:MLOM Link Speed |  C220 M8, C240 M8 |  New  
PCIe Slot n Link Speed |  C220 M8, C240 M8 |  New  
PCIe Slot n Option ROM |  C220 M8, C240 M8 |  New  
PCIe Slot:MLOM OptionROM |  C220 M8, C240 M8 |  New  
Boot Performance Mode |  C220 M8, C240 M8, X210c M8 |  New  
Select PPR Type |  C220 M8, C240 M8, X210c M8 |  New  
PCIe RAS support |  C220 M8, C240 M8, X210c M8 |  New  
Memory Thermal Throttling Mode  |  C220 M8, C240 M8, X210c M8 |  New  
Memory Size Limit in GB |  C220 M8, C240 M8, X210c M8 |  New  
External SSC Enable |  C220 M8, C240 M8, X210c M8 |  New  
QPI Link Frequency Select |  C220 M8, C240 M8, X210c M8 |  New  
IIO eDPC Support |  C220 M8, C240 M8 |  New  
DCU Streamer Prefetch |  C220 M8, C240 M8, X210c M8  |  New  
P STATE Coordination |  C220 M8, C240 M8, X210c M8 |  New  
SGX Factory Reset |  C220 M8, C240 M8, X210c M8 |  New  
SGX Package Information In-Band Access |  C220 M8, C240 M8, X210c M8 |  New  
Security Device Support |  C220 M8, C240 M8, X210c M8 |  New  
LIMIT CPU PA to 46 Bits |  C220 M8, C240 M8, X210c M8 |  New  
Table 7. **New/Changed BIOS Tokens for 4.3(5c)** BIOS Token |  Platform |  New/Changed  
---|---|---  
UEFI Memory Map Special Purpose Memory Flag |  C220 M7, C240 M7, X210c M7, X410c M7 | New  
ACPI SRAT Special Purpose Memory Flag | C220 M7, C240 M7, X210c M7, X410c M7 | New  
CCD Control | C245 M8, C225 M8, X215c M8 | Changed  
Power Profile Selection F19h | C245 M8, C225 M8, X215c M8 | Changed  
CPU Downcore control F19 M10h-1Fh | C245 M8, C225 M8, X215c M8 | Changed  
Table 8. **New/Changed BIOS Tokens for 4.3(5a)** BIOS Token |  Platform |  New/Changed  
---|---|---  
PCIe Slot:MLOM Link Speed | C225 M8 | New  
PCIe Slot:MLOM OptionROM | C225 M8 | New  
PCIe Slot n OptionROM | C225 M8 | New  
PCIe Slot MSTOR Link Speed | C225 M8 | New  
PCIe Slot MSTOR RAID OptionRO | C225 M8 | New  
MRAID n Link Speed | C225 M8 | New  
MRAID n OptionROM | C225 M8 | New  
Front NVME n Link Speed | C225 M8 | New  
Front NVME n OptionROM | C225 M8 | New  
Rear NVME n Link Speed | C225 M8 | New  
Rear NVME n OptionROM | C225 M8 | New  
VGA Priority | C225 M8 | New  
FRB 2 Timer | C225 M8, X215c M8 | New  
OS Watchdog Timer Policy | C225 M8, X215c M8 | New  
OS Watchdog Timer Timeout | C225 M8, X215c M8 | New  
OS Watchdog Timer | C225 M8, X215c M8 | New  
Flow Control | C225 M8, X215c M8 | New  
Baud rate | C225 M8, X215c M8 | New  
Terminal type | C225 M8, X215c M8 | New  
Console redirection | C225 M8, X215c M8 | New  
Security Device Support | C225 M8, X215c M8 | New  
Trusted Platform Module State | C225 M8, X215c M8 | New  
SHA-1 PCR Bank | C225 M8, X215c M8 | New  
SHA256-PCR-Bank | C225 M8, X215c M8 | New  
SHA384 PCR Bank | C225 M8, X215c M8 | New  
Above 4G Decoding | C225 M8, X215c M8 | New  
CDN Control | C225 M8, X215c M8 | New  
PCIe Slots CDN Control | C225 M8, X215c M8 | New  
Power ON Password | C225 M8, X215c M8 | New  
Core Performance Boost | C225 M8, X215c M8 | New  
Ln Stream HW Prefetcher | C225 M8, X215c M8 | New  
NUMA Nodes per Socket | C225 M8, X215c M8 | New  
Chipselect Interleaving | C225 M8, X215c M8 | New  
Bank Group Swap | C225 M8, X215c M8 | New  
Determinism Slider | C225 M8, X215c M8 | New  
IPv4 PXE Support | C225 M8, X215c M8 | New  
IPV6 PXE Support | C225 M8, X215c M8 | New  
IOMMU | C225 M8, X215c M8 | New  
SMT Mode | C225 M8, X215c M8 | New  
CPU Downcore control F19 M10h-1Fh | C225 M8, X215c M8 | New  
Downcore control F19 MA0h-AFh | C225 M8, X215c M8 | New  
SR-IOV Support | C225 M8, X215c M8 | New  
SMEE | C225 M8, X215c M8 | New  
BIOS Techlog Level | C225 M8, X215c M8 | New  
OptionROM Launch Optimization | C225 M8, X215c M8 | New  
PCIe ARI Support | C225 M8, X215c M8 | New  
Re-Size BAR Support | C225 M8, X215c M8 | New  
TSME | C225 M8, X215c M8 | New  
IPv4 HTTP Support | C225 M8, X215c M8 | New  
IPv6 HTTP Support | C225 M8, X215c M8 | New  
Network Stack | C225 M8, X215c M8 | New  
SEV-SNP Support | C225 M8, X215c M8 | New  
CPPC | C225 M8, X215c M8 | New  
Power Profile Selection F19h | C225 M8, X215c M8 | New  
SNP Memory Coverage | C225 M8, X215c M8 | New  
SNP Memory Size to Cover in MB | C225 M8, X215c M8 | New  
BME DMA Mitigation | C225 M8, X215c M8 | New  
Post Package Repair | C225 M8, X215c M8 | New  
Runtime Post Package Repair | C225 M8, X215c M8 | New  
APBDIS | C225 M8, X215c M8 | New  
CCD Control | C225 M8, X215c M8 | New  
Streaming Stores Control | C225 M8, X215c M8 | New  
ACPI SRAT L3 Cache As NUMA Domain | C225 M8, X215c M8 | New  
DF C-States | C225 M8, X215c M8 | New  
SEV-ES ASID Space Limit | C225 M8, X215c M8 | New  
Local APIC Mode | C225 M8, X215c M8 | New  
DRAM Scrub Time | C225 M8, X215c M8 | New  
PCIe Ten Bit Tag Support | C225 M8, X215c M8 | New  
4-link xGMI max speed | C225 M8, X215c M8 | New  
Memory Interleaving | C225 M8, X215c M8 | New  
DF PState Frequency Optimizer | C225 M8, X215c M8 | New  
AVX512 | C225 M8, X215c M8 | New  
Power Down Enable | C225 M8, X215c M8 | New  
xGMI Force Link Width | C225 M8, X215c M8 | New  
Memory Refresh Rate | C225 M8, X215c M8 | New  
TPM Pending Operation | C225 M8, C245 M8, X215c M8 | New  
Enhanced Memory Test | C225 M8, C245 M8, X215c M8 | New  
Enhanced CPU Performance | C225 M8, C245 M8, X215c M8 | New  
Burst and Postponed Refresh | C225 M8, C245 M8, X215c M8 | New  
Global C State Control | C225 M8, C245 M8, X215c M8 | Changed  
Table 9. **New/Changed BIOS Tokens for 4.3(4b)** BIOS Token |  Platform |  New/Changed  
---|---|---  
DF PState Frequency Optimizer  |  C245 M8 | New  
AVX512 |  C245 M8 | New  
Power Down Enable |  C245 M8 | New  
Fixed SOC P-State SP5 F19h |  C245 M8 | New  
xGMI Force Link Width |  C245 M8 | New  
4-link xGMI max speed |  C245 M8 | New  
SEV-ES ASID Space Limit |  C245 M8 | New  
Runtime Post Package Repair |  C245 M8 | New  
Re-Size BAR Support |  C245 M8 | New  
Power Profile Selection F19h |  C245 M8 | New  
CPU Downcore control F19 M10h-1Fh |  C245 M8 | New  
Downcore control F19 MA0h-AFh |  C245 M8 | New  
CPPC |  C245 M8 | New  
SMT Mode |  C245 M8 |  New  
SVM Mode |  C245 M8 |  New  
IPV4 HTTP Support |  C245 M8 |  New  
IPV6 HTTP Support |  C245 M8 |  New  
IPV4 PXE Support |  C245 M8 |  New  
IPV6 PXE Support |  C245 M8 |  New  
PCIe ARI Support |  C245 M8 |  New  
MRAID n Link Speed |  C245 M8 |  New  
MRAID n OptionROM |  C245 M8 |  New  
PCIe Slot MSTOR Link Speed |  C245 M8 |  New  
PCIe Slot n Link Speed |  C245 M8 |  New  
Front NVME n Link Speed |  C245 M8 |  New  
Front NVME n OptionROM |  C245 M8 |  New  
PCIe Slot:MLOM Link Speed |  C245 M8 |  New  
PCIe Slot:MLOM OptionROM |  C245 M8 |  New  
PCIe Slot n OptionROM |  C245 M8 | New  
Rear NVME n Link Speed |  C245 M8 | New  
Rear NVME n OptionROM |  C245 M8 |  New  
Single Root I/O Virtualization (SR-IOV) Support |  C245 M8 |  New  
PCIe Slots CDN Control |  C245 M8 |  New  
Consistent Device Naming |  C245 M8 |  New  
BME DMA Mitigation |  C245 M8 |  New  
Burst and Postponed Refresh |  C245 M8 |  New  
IOMMU |  C245 M8 |  New  
Bank Group Swap |  C245 M8 | New  
Chipset Interleave |  C245 M8 |  New  
DRAM Scrub Time |  C245 M8 |  New  
Post Package Repair |  C245 M8 |  New  
SMEE |  C245 M8 |  New  
Memory Mapped IO above 4GB |  C245 M8 | New  
VGA Priority |  C245 M8 |  New  
Core Performance Boost |  C245 M8 |  New  
Global C State Control |  C245 M8 |  New  
Ln Stream HW |  C245 M8 |  New  
Determinism Slider |  C245 M8 |  New  
Transparent Secure Memory Encryption |  C245 M8 |  New  
Burst and Postponed Refresh |  C245 M8 |  New  
APBDIS |  C245 M8 |  New  
Streaming Stores Control |  C245 M8 |  New  
DF C-States |  C245 M8 |  New  
CCD Control |  C245 M8 |  New  
ACPI SRAT L3 Cache As NUMA Domain |  C245 M8 |  New  
Local APIC Mode |  C245 M8 |  New  
PCIe Ten Bit Tag Support |  C245 M8 |  New  
SMT Mode |  C245 M8 |  New  
Baud Rate |  C245 M8 |  New  
BIOS Techlog Level |  C245 M8 |  New  
OptionROM Launch Optimization |  C245 M8 |  New  
Console Redirection |  C245 M8 |  New  
Flow Control |  C245 M8 |  New  
FRB-2 Timer |  C245 M8 |  New  
OS Boot Watchdog Timer |  C245 M8 |  New  
OS Boot Watchdog Timer Policy |  C245 M8 |  New  
OS Boot Watchdog Timer Timeout |  C245 M8 |  New  
Terminal Type |  C245 M8 |  New  
SHA-1 PCR Bank |  C245 M8 |  New  
SHA256 PCR Bank |  C245 M8 |  New  
SHA384 PCR Bank |  C245 M8 |  New  
Trusted Platform Module State |  C245 M8 |  New  
Security Device Support |  C245 M8 |  New  
Memory Interleaving |  C245 M8 |  Changed  
Dram Scrub Time |  C245 M8 |  Changed  
CCD Control |  C245 M8 |  Changed  
SEV-SNP Support |  C245 M8 |  Changed  
Memory Refresh Rate  |  C245 M8 |  Changed  
Table 10. **New/Changed/Deprecated BIOS Tokens for 4.3(4a)** BIOS Token |  Platform |  New/Changed  
---|---|---  
DFX OSB |  X410c M7, X210c M7 |  New  
SHA384 PCR Bank* |  C225 M6, C245 M6, C220 M6, C240 M6, x210 M6, B200 M6 |  New  
Local APIC Mode* |  C245 M6, C225 M6 |  New  
DRAM Scrub Time |  C245 M6, C225 M6 |  New  
Memory Interleaving |  C245 M6, C225 M6 |  New  
PCIe Ten Bit Tag Support |  C245 M6, C225 M6 |  New  
EDC Control Throttle |  C245 M6, C225 M6 |  New  
DLWM Support |  C245 M6, C225 M6 |  New  
Memory Clock Speed 7xx3 (AMD 3rd Gen CPU)  |  C245 M6, C225 M6 |  New  
Memory Clock Speed 7xx2 (AMD 2nd Gen CPU)  |  C245 M6, C225 M6 |  New  
xGMI Link Configuration |  C245 M6, C225 M6 |  New  
Preferred IO 7xx3 (AMD 3rd Gen CPU)  |  C245 M6, C225 M6 |  New  
Preferred IO 7xx2 (AMD 2nd Gen CPU)  |  C245 M6, C225 M6 |  New  
Core Watchdog Timer Enable |  C245 M6, C225 M6 |  New  
Serial Mux |  C245 M6, C225 M6 |  New  
Memory Refresh Rate |  C245 M6, C225 M6 |  New  
Power Performance Tuning |  X410c M7, X210c M7, C220 M7, C240 M7 |  New  
PRMRR Size |  X410c M7, X210c M7, C220 M7, C240 M7 |  Changed  
DCPMM Firmware Downgrade |  X410c M7, X210c M7, C220 M7, C240 M7 |  Deprecated  
CR QoS |  X410c M7, X210c M7, C220 M7, C240 M7 |  Deprecated  
NVM Performance Setting |  X410c M7, X210c M7, C220 M7, C240 M7 |  Deprecated  
CR FastGo Config |  X410c M7, X210c M7, C220 M7, C240 M7 |  Deprecated  
Snoopy mode for AD |  X410c M7, X210c M7, C220 M7, C240 M7 |  Deprecated  
Snoopy for 2LM |  X410c M7, X210c M7, C220 M7, C240 M7 |  Deprecated  
Volatile Memory Mode |  X410c M7, X210c M7, C220 M7, C240 M7 |  Deprecated  
eADR  |  X410c M7, X210c M7, C220 M7, C240 M7 |  Deprecated  
Memory Bandwidth Boost |  X410c M7, X210c M7, C220 M7, C240 M7 |  Deprecated  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

SHA384 PCR Bank Bios token supports PID models UCS-TPM-002D and UCS-TPM-002D-D. 

* * *  
  
---|---  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For Local APIC Mode Bios token, Compatability values are not supported for AMD EPYC 7XX2 series. 

* * *  
  
---|---  
Table 11. **New/Changed BIOS Tokens for 4.3(3c)** BIOS Token |  Platform |  New/Changed  
---|---|---  
MMIO High Granularity Size |  X410c M7, X210c M7, C220 M7, C240 M7 |  New  
MMIO High Base |  X410c M7, X210c M7, C220 M7, C240 M7 |  New  
IOAT Configuration |  X410c M7, X210c M7, C220 M7, C240 M7 |  New  
Table 12. **New/Changed BIOS Tokens for 4.3(3a)** BIOS Token |  Platform |  New/Changed  
---|---|---  
Trust Domain Extension (TDX) |  X410c M7, X210c M7, C220 M7, C240 M7 |  New  
TDX Secure Arbitration Mode (SEAM) Loader |  X410c M7, X210c M7, C220 M7, C240 M7 |  New  
SHA384 PCR Bank |  X410c M7, X210c M7, C220 M7, C240 M7 |  New  
QpiLinkSpeed |  X410c M7, X210c M7, C220 M7, C240 M7 |  Changed  
C1 Auto demotion |  X410c M7, X210c M7, C220 M7, C240 M7 |  Changed  
C1 Auto UnDemotion |  X410c M7, X210c M7, C220 M7, C240 M7 |  Changed  
  
For more information on BIOS tokens, see [Cisco UCS Server BIOS Tokens in Intersight Managed Mode](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide.html). 

---

## Page 2: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/preface.html

  * [Communications, Services, Bias-free Language, and Additional Information](/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/preface.html)
  * [Introduction to Intersight Managed Mode Server Bios Tokens](/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/b_UCS_BIOS_Tokens_Guide_chapter_01.html)
  * [Supported Platforms](/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-supported-platforms-and-bios-tokens.html)
  * [Boot Options BIOS Settings](/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-boot-options-bios-settings.html)
  * [Intel Directed IO](/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-intel-directed-io.html)
  * [LOM and PCIe Slots](/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-lom-and-pcie-slots.html)
  * [Main](/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-main.html)
  * [Memory](/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-memory.html)
  * [PCI](/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-pci.html)
  * [Power and Performance](/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-power-and-performance.html)
  * [Processor](/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-processor.html)
  * [QPI](/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-qpi.html)
  * [Server Management](/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-server-management.html)
  * [Trusted Platform](/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-trusted-platform.html)
  * [USB](/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-usb.html)


---

## Page 3: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-supported-platforms-and-bios-tokens.html

## Intel Supported Platforms

BIOS tokens applicable for Intel (**B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8**) Platforms 

Name |  Description |  Versions |  Values  
---|---|---|---  
Number of Retries |  Number of attempts to boot. |  **Note** |  Applicable for B200 M5, B480 M5, C480 M5 platforms only.  
---|---  
4.1(1) and later |  Infinite. **13** , 5 

  * **Infinite** —The system attempts all configured boot options and repeats until the system boots or is interrupted manually. 
  * **5, 13** —The system attempts all configured boot options and repeats the selected number of times until the system boots or is interrupted. If all attempts fail, the system prompts to continue. Value 13 is the default value for Cisco UCS B200 M5 and 5 is the default value for Cisco UCS B480 M5. 

  
**Cool Down Time (sec)** |  The time to wait (in seconds) before the next boot attempt. This can be one of the following: |  **Note** |  Applicable for B200 M5, B480 M5, C480 M5 platforms only.  
---|---  
4.1(1) and later |  15 sec, 45 sec, **90 sec**

  * **15, 45, 90** —System waits for the selected time in seconds before the next boot attempt. 

  
Boot Option Retry |  Whether the BIOS retries NON-EFI based boot options without waiting for user input. |  **Note** |  Applicable for B200 M5, B480 M5, C480 M5 platforms only.  
---|---  
4.1(1) and later |  **Disabled** , Enabled 

  * **Disabled** —Waits for user input before retrying NON-EFI based boot options. 
  * **Enabled** —Continually retries NON-EFI based boot options without waiting for user input. 

  
IPV4 HTTP Support |  Enables or disables IPv4 support for HTTP.  |  4.2(1) and later |  Disabled, **Enabled**

  * **Disabled** —IPv4 HTTP support is not available. 
  * **Enabled** —IPv4 HTTP support is made available. 

  
IPV6 HTTP Support | Enables or disables IPv6 support for HTTP. |  4.2(1) and later |  Disabled, **Enabled**

  * **Disabled** —IPv6 HTTP support is not available. 
  * **Enabled** —IPv6 HTTP support is made available. 

  
IPV4 PXE Support |  Enables or disables IPv4 support for PXE.  |  4.2(1) and later |  Disabled, **Enabled**

  * **Disabled** —IPv4 PXE support is not available. 
  * **Enabled** —IPv4 PXE support is made available. 

  
IPV6 PXE Support |  Enables or disables IPv6 support for PXE.  |  4.2(1) and later |  Disabled, **Enabled**

  * **Disabled** —IPv6 PXE support is not available. 
  * **Enabled** —IPv6 PXE support is made available. 

  
Network Stack |  This option allows you to enable or disable the complete network style of the system. |  4.1(1) and later |  Disabled,**Enabled**

  * **Disabled** —Network Stack support is not available. 
  * **Enabled** —Network Stack support is available. 

  
Power ON Password |  This token requires that you set a BIOS password before using the F2 BIOS configuration. If enabled, password needs to be validated before you access BIOS functions such as IO configuration, BIOS set up, and booting to an operating system using BIOS.  |  **Note** |  Applicable for B200 M5, B480 M5, C480 M5 platforms only.  
---|---  
4.1(1) and later |  **Disabled** , Enabled 

  * **Disabled** —Power On Password is disabled. 
  * **Enabled** —Power On Password is enabled. 

  
P-SATA OptionROM |  This options allows you to select the P-SATA mode. |  4.1(1) and later |  Disabled, **LSI SW RAID** , AHCI 

  * Disabled—P-SATA mode is disabled 
  * LSI SW RAID—Sets both SATA and sSATA controllers to RAID mode for LSI SW RAID. 
  * AHCI—The controller enables the Advanced Host Controller Interface (AHCI) and disables RAID. 

  
SATA Mode |  This options allows you to select the SATA mode. |  4.1(1) and later |  **AHCI** , LSISW RAID, Disabled 

  * Disabled—SATA mode is disabled 
  * LSI SW RAID—Sets both SATA and sSATA controllers to RAID mode for LSI SW RAID 
  * AHCI—The controller enables the Advanced Host Controller Interface (AHCI) and disables RAID. 

  
VMD Enablement |  Whether NVMe SSDs that are connected to the PCIe bus can be hot swapped. It also standardizes the LED status light on these drives. LED status lights can be optionally programmed to display specific Failure indicator patterns.  |  **Note** |  Not applicable on S3260 M5 platform.  
---|---  
4.1(1) and later |  **Disabled** , Enabled 

  * Disabled—Hot swap of NVMe SSDs that are connected to the PCIe bus is not allowed. 
  * Enabled—Hot swap of NVMe SSDs that are connected to the PCIe bus is allowed. 

  
Intel VT for directed IO |  Whether the processor uses Intel Virtualization Technology for Directed I/O (VT-d).  |  4.1(1) and later |  **Enabled** , Disabled 

  * **Disabled** —The processor does not use virtualization technology. 
  * **Enabled** —The processor uses virtualization technology. 

  
**Intel(R) VT-d Coherency Support** |  Whether the processor supports Intel VT-d Coherency.  |  4.1(1) and later |  Enabled, **Disabled**

  * **Disabled** —The processor does not support coherency. 
  * **Enabled** —The processor uses VT-d Coherency as required. 

  
Intel VTD ATS Support |  Whether the processor supports Intel VT-d Address Translation Services (ATS).  |  4.1(1) and later |  Disabled,**Enabled**

  * **Disabled** —The processor does not support ATS. 
  * **Enabled** —The processor uses VT-d ATS as required. 

  
PreBoot DMA Protection | The BIOS setting that aims to prevent unauthorized Direct Memory Access (DMA) during the boot process, potentially protecting against malicious devices from gaining access to system memory.  |  4.3(6a) |  Disabled,**Enabled**

  * Disabled—Options are Disabled. 
  * Enabled—Options are Enabled. 

  
ACS Control GPU n where _n_ varies from 1-14  |  Access Control Services (ACS) allow the processor to enable or disable peer-to-peer communication between multiple devices for GPUs.  |  **Note** |  Applicable for C480 M5 platform only.  
---|---  
4.0(4) and later |  Enabled, **Disabled**

  * **Disabled** Disables peer-to-peer communication between multiple devices for GPUs. 
  * **Enabled** Enables peer-to-peer communication between multiple devices for GPUs. 

  
**CDN Support for LOM** |  Whether the Ethernet Networking Identifier naming convention is according to Consistent Device Naming (CDN) or the traditional way of naming conventions.  |  4.0(4) and later |  Enabled, **Disabled**

  * **Disabled** OS Ethernet Networking Identifier is named in a default convention as ETH0, ETH1 and so on. 
  * **Enabled** OS Ethernet Network Identifier is named in a consistent device naming (CDN) convention according to the physical LAN on Motherboard (LOM) port numbering; LOM Port 0, LOM Port 1 and so on. 

  
External SSC Enable |  This option allows you to Enable/Disable the Clock Spread Spectrum of the external clock generators. |  4.1(2) and later |  **Enabled** , Disabled, 0P3_Percent, 0P5_Percent, Hardware, Off  |  **Note** |  0P3_Percent, 0P5_Percent, Hardware, Off options are available for M7 servers only.  
---|---  
IIO eDPC Support |  This option allows a downstream link to be disabled after an uncorrectable error, making recovery possible in a controlled and robust manner.  |  4.2(1) and later |  Disabled, On fatal error, **On fatal and non-fatal error**  
LOM Port n OptionROM, where _n_ ranges from 0-3.  |  Whether Option ROM is available on the LOM port _n_ |  **Note** |  Applicable for C220 M6 and C240 M6 platforms only.  
---|---  
4.0(4) and later |  Disabled, **Enabled,** Legacy only, UEFI only 

  * **Disabled** —The expansion slot is not available. 
  * **Enabled** —The expansion slot is available. 
  * **UEFI only** —The expansion slot is available only for UEFI. 
  * **Legacy only** —The expansion slot is available only for legacy. 

  
PCIe PLL SSC Percent |  Whether all PCIe PLL SSC ports are enabled or disabled. |  4.1(2) and later |  0–255 (Unit is (n/10)%)   
MRAIDn Link Speed where n ranges from 1-2.  |  This option allows you to restrict the maximum speed of MRAID.  |  **Note** |  Applicable for C220 M5, C240 M5, C220 M6, C220 M7, and C240 M8 platforms only.  
---|---  
4.0(2) and later |  **Auto** , Disabled, GEN 1, GEN 2, GEN 3, GEN 4, GEN 5 

  * **Disabled** —The maximum speed is not restricted. 
  * **Enabled** —The maximum speed is restricted. 
  * **Auto** —The maximum speed is set automatically. 
  * **GEN 1** —2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * **GEN 2** —5GT/s is the maximum speed allowed. 
  * **GEN 3** —8GT/s is the maximum speed allowed. 
  * **GEN 4** —16GT/s is the maximum speed allowed.  |  **Note** |  Applicable for M7, M8 servers only.  
---|---  
  * **GEN 5** —32GT/s is the maximum speed allowed. 

**Note** |  Applicable for M7, M8 servers only.  
---|---  

  
MRAID n OptionROM  where n ranges from 1-2.  |  Whether Option ROM is available on the MRAID port.  |  **Note** |  Applicable for C220 M5, C240 M5, C220 M6, C220 M7, and C240 M8 platforms only.  
---|---  
4.0(2) and later |  Disabled,**Enabled**

  * **Disabled** —The expansion slot is not available. 
  * **Enabled** —The expansion slot is available. . 

  
PCIe Slot MSTOR RAID OptionROM |  Whether the server can use the Option ROMs present in the PCIe MSTOR RAID. |  **Note** |  Applicable for B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, C220 M6, C240 M6, C220 M7, C240 M7, C220 M8, and C240 M8 platforms only.   
---|---  
4.2(1) and later |  Disabled, **Enabled**

  * **Disabled** —Option ROM is not available. 
  * **Enabled** —Option ROM is available. 

  
NVME n Link Speed where _n_ ranges from 0-6 and 13-24.  |  This option allows you to restrict the maximum speed of an NVME card installed in the PCIe slot. |  **Note** |  NVME 24 Link Speed supports C220 M7 and C240 M7 servers, and X210c M7 server.   
---|---  
4.0(2) and later |  Disabled, **Auto** , GEN1, GEN2, GEN3, GEN4, GEN5 

  * **Disabled** —Maximum speed is not restricted. 
  * **Auto** —The maximum speed is set automatically. 
  * **GEN 1** —2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * **GEN 2** —5GT/s is the maximum speed allowed 
  * **GEN 3** —8GT/s is the maximum speed allowed 
  * **GEN 4** —16GT/s is the maximum speed allowed 
  * **GEN 5** —32GT/s is the maximum speed allowed 

  
NVME n OptionROM where _n_ ranges from 0-6.  |  This options allows you to control the Option ROM execution of the PCIe adapter connected to the SSD:NVMe slot n. |  4.0(2) and later |  Enabled, Disabled

  * **Disabled** —Option is not restricted. 
  * **Enabled** —Option is restricted. 

  
PCIe Slot n Link Speed where _n_ ranges from 1 to 8 .  |  Link speed for PCIe Slot designated by slot n. |  4.0(1) and later |  Disabled, **Auto** , GEN1, GEN2, GEN3, GEN4, GEN5  GEN5 is supported only for speeds 1 to 6.

  * **Disabled** —Maximum speed is not restricted. 
  * **Auto** —The maximum speed is set automatically. 
  * **GEN 1** —2GT/s (gigatransfers per second) is the maximum speed allowed. 
  * **GEN 2** —5GT/s is the maximum speed allowed 
  * **GEN 3** —8GT/s is the maximum speed allowed 
  * **GEN 4** —16GT/s is the maximum speed allowed 
  * **GEN 5** —32 GT/s is the maximum speed allowed 

  
PCIe Slot:LOM Link Speed |  To configure link speed for PCIe Slot:LOM. |  4.0(1) and later |  Disabled, **Auto** , GEN1, GEN2, GEN3 

  * **Disabled** —Maximum speed is not restricted. 
  * **Auto** —The maximum speed is set automatically. 
  * **GEN 1** —2GT/s (gigatransfers per second) is the maximum speed allowed. 
  * **GEN 2** —5GT/s is the maximum speed allowed 
  * **GEN 3** —8GT/s is the maximum speed allowed 

  
PCIe Slot nOptionROM , where n ranges from 1 to 8  |  Whether Option ROM is available on the port. |  4.0(2) and later |  Disabled, **Enabled** , Legacy only, UEFI only 

  * **Disabled** —The expansion slot is not available. 
  * **Enabled** —The expansion slot is available. 

  
Front NVME n Link Speed where _n_ ranges from 1 to 12. For C245 M8 platform, _n_ ranges from 1 to 4.  |  This option allows you to restrict the maximum speed of an NVME card installed in the front PCIe slot. |  4.0(4) and later |  Disabled, **Auto** , GEN1, GEN2, GEN3, GEN4, GEN5 

  * **Disabled** —Maximum speed is not restricted. 
  * **Auto** —The maximum speed is set automatically. 
  * **GEN 1** —2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * **GEN 2** —5GT/s is the maximum speed allowed 
  * **GEN 3** —8GT/s is the maximum speed allowed 
  * **GEN 4** —16GT/s is the maximum speed allowed 
  * **GEN 5** —32GT/s is the maximum speed allowed 

  
Front NVME n OptionROM where _n_ ranges from 1 to 24. For C245 M8 platform, _n_ ranges from 1 to 4.  |  This options allows you to control the Option ROM execution of the PCIe adapter connected to the SSD:NVMe slot n. |  4.2(1) and later |  **Enabled** , Disabled 

  * **Disabled** —Option is not restricted. 
  * **Enabled** —Option is restricted. 

  
PCIe LOM:1 and 2 Link |  This option allows you to restrict the maximum speed of an adapter card installed in PCIe slot 1 and 2. |  4.0(1) and later |  Enabled, Disabled

  * **Disabled** —Option is not restricted. 
  * **Enabled** —Option is restricted. 

  
Slot Mezz State |  This option allows you to configure the Mezz state for PCIe slot. |  4.0(1) and later |  Disabled, **Enabled** , Legacy only, UEFI only 

  * **Disabled** —The expansion slot is not available. 
  * **Enabled** —The expansion slot is available. 
  * **UEFI only** —The expansion slot is available only for UEFI. 
  * **Legacy only** —The expansion slot is available only for legacy. 

  
PCIe Slot:MLOM Link Speed |  This option allows you to restrict the maximum speed of an MLOM adapter. |  4.0 (1) and later |  **Auto** , Disabled, GEN 1, GEN 2, GEN 3, GEN 4, GEN 5 

  * **Disabled** —The maximum speed is not restricted. 
  * **Auto** —The maximum speed is set automatically. 
  * **GEN 1** —2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * **GEN 2** —5GT/s is the maximum speed allowed. 
  * **GEN 3** —8GT/s is the maximum speed allowed. 
  * **GEN 4** —16GT/s is the maximum speed allowed. 
  * **GEN 5** —32GT/s is the maximum speed allowed. 

  
PCIe Slot:MLOM OptionROM |  Whether Option ROM is available on the MLOM port. |  4.0(1) and later |  Disabled, **Enabled** , Legacy only, UEFI only 

  * **Disabled** —The expansion slot is not available. 
  * **Enabled** —The expansion slot is available. 
  * **UEFI only** —The expansion slot is available only for UEFI. 
  * **Legacy only** —The expansion slot is available only for legacy. 

  
MRAID Link Speed |  This option allows you to restrict the maximum speed of MRAID.  |  4.0(2) and later |  **Auto** , Disabled, GEN 1, GEN 2, GEN 3, GEN 4, GEN 5 

  * **Disabled** —The maximum speed is not restricted. 
  * **Auto** —The maximum speed is set automatically. 
  * **GEN 1** —2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * **GEN 2** —5GT/s is the maximum speed allowed. 
  * **GEN 3** —8GT/s is the maximum speed allowed. 
  * **GEN 4** —16GT/s is the maximum speed allowed. 
  * **GEN 5** —32GT/s is the maximum speed allowed. 

  
PCIe Slot:MRAID OptionROM |  Whether Option ROM is available on the MLOM port. |  4.0(2) and later |  Disabled, **Enabled** , Legacy only, UEFI only 

  * **Disabled** —The expansion slot is not available. 
  * **Enabled** —The expansion slot is available. 

  
PCIe Slot nOptionROM , where n ranges from 1 to 8  |  Whether Option ROM is available on the port. |  4.0(2) and later |  Disabled, **Enabled** , Legacy only, UEFI only 

  * **Disabled** —The expansion slot is not available. 
  * **Enabled** —The expansion slot is available. 

  
RAID Link Speed |  This option allows you to restrict the maximum speed of RAID.  |  4.0(1) and later |  Disabled, **Auto** , GEN1, GEN2, GEN3 

  * **Disabled** —Maximum speed is not restricted. 
  * **Auto** —The maximum speed is set automatically. 
  * **GEN 1** —2GT/s (gigatransfers per second) is the maximum speed allowed. 
  * **GEN 2** —5GT/s is the maximum speed allowed 
  * **GEN 3** —8GT/s is the maximum speed allowed 

  
PCIe Slot RAID OptionROM |  Whether Option ROM is available on the RAID slot or not. |  4.0(1) and later |  **Enabled** , Disabled 

  * **Disabled** —Option is not restricted. 
  * **Enabled** —Option is restricted. 

  
Rear NVME n Link Speed, where n ranges from 1 to 4.  |  This option allows you to restrict the maximum speed of rear NVME.  |  **Note** |  NVME 4 Link Speed supports C240 M7 servers, X210c M7, and C240 M8 server.  
---|---  
4.0(4) and later |  **Auto** , Disabled, GEN 1, GEN 2, GEN 3, GEN 4, GEN 5 

  * **Disabled** —The maximum speed is not restricted. 
  * **Auto** —The maximum speed is set automatically. 
  * **GEN 1** —2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * **GEN 2** —5GT/s is the maximum speed allowed. 
  * **GEN 3** —8GT/s is the maximum speed allowed. 
  * **GEN 4** —16GT/s is the maximum speed allowed. 
  * **GEN 5** —32GT/s is the maximum speed allowed. 

  
Rear NVME n OptionROM, where n ranges from 1 to 4.  |  Whether Option ROM is available on the rear NVME or not. |  4.0(4) and later |  **Enabled** , Disabled 

  * **Disabled** —Option is not restricted. 
  * **Enabled** —Option is restricted. 

  
PCIe Slot:Riser Link Speedn, where n is 1 and 2.  |  This option allows you to restrict the maximum speed of Riser. |  4.0(4) and later |  Disabled, **Auto** , GEN1, GEN2, GEN3 

  * **Disabled** —Maximum speed is not restricted. 
  * **Auto** —The maximum speed is set automatically. 
  * **GEN 1** —2GT/s (gigatransfers per second) is the maximum speed allowed. 
  * **GEN 2** —5GT/s is the maximum speed allowed 
  * **GEN 3** —8GT/s is the maximum speed allowed 

  
PCIe Slot:Riser nSlotx Link Speed, where _n_ is 1 and 2 and _x_ is from 1 to 6.  |  This option allows you to restrict the maximum speed of Riser in the _x_ slot .  |  4.0(2) and later |  Disabled, **Auto** , GEN1, GEN2, GEN3 

  * **Disabled** —Maximum speed is not restricted. 
  * **Auto** —The maximum speed is set automatically. 
  * **GEN 1** —2GT/s (gigatransfers per second) is the maximum speed allowed. 
  * **GEN 2** —5GT/s is the maximum speed allowed 
  * **GEN 3** —8GT/s is the maximum speed allowed 

  
PCIe Slot:SAS OptionROM |  Whether Option ROM is available on SAS slot or not. |  4.0(2) and later |  Disabled, **Enabled** , Legacy only, UEFI only 

  * **Disabled** —The expansion slot is not available. 
  * **Enabled** —The expansion slot is available. 
  * **UEFI only** —The expansion slot is available only for UEFI. 
  * **Legacy only** —The expansion slot is available only for legacy. 

  
PCIe Slot:FrontSSD nLink Speed, where _n_ is 1 and 2.  |  This option allows you to restrict the maximum speed of Front SSD. |  4.0(2) and later |  Disabled, **Auto** , GEN1, GEN2, GEN3 

  * **Disabled** —Maximum speed is not restricted. 
  * **Auto** —The maximum speed is set automatically. 
  * **GEN 1** —2GT/s (gigatransfers per second) is the maximum speed allowed. 
  * **GEN 2** —5GT/s is the maximum speed allowed 
  * **GEN 3** —8GT/s is the maximum speed allowed 

  
Re-Size BAR Support |  Allows to enable or disable Re-sizable BAR support setup item.  |  4.3(4b) and later |  Enabled, **Disabled** |  **Note** |  By default it is **Enabled** for AMD platforms and **Disabled** for Intel platforms.   
---|---  
PCIe Slots CDN Control where, CDN refers to Consistent Device Naming  |  PCIe Slots Consistent Device Naming (CDN) control allows PCIe slots to be named in a consistent manner. This makes PCIe slot names more uniform, easy to identify, and persistent when the configuration changes are made.  |  **Note** |  Applicable for C240 M5, C220 M6, C240 M6, C220 M7, C240 M7, C220 M8, C240 M8 platforms only.  
---|---  
4.0(2) and later |  Enabled, **Disabled**

  * **Disabled** —Option is not restricted. 
  * **Enabled** —Option is restricted. 

  
Consistent Device Naming (CDN) Control |  PCIe Slots Consistent Device Naming (CDN) control allows PCIe slots to be named in a consistent manner. This makes PCIe slot names more uniform, easy to identify, and persistent when the configuration changes are made.  |  **Note** |  Applicable for B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, and X210c M8 platforms only.   
---|---  
4.0(2) and later  |  **Enabled** , Disabled 

  * **Disabled** —Option is not restricted. 
  * **Enabled** —Option is restricted. 

  
ACPI SRAT Special Purpose Memory Flag |  Enables or disables the ACPI SRAT SP Memory flag when the UEFI Memory Map Special Purpose Flag is enabled. |  **Note** |  Applicable tor C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, and X410c M8 platforms only.  
---|---  
4.3(5b) and later |  Disabled, Enabled

  * **Disabled** —Options are Disabled. 
  * **Enabled** —Options are enabled. 

  
UEFI Memory Map Special Purpose Memory Flag |  Changing the UEFI Memory Map Special knob settings impacts CXL cards on certain operating systems. |  **Note** |  Applicable tor C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, and X410c M8, platforms only.  
---|---  
4.3(5b) and later |  Disabled, Enabled

  * **Disabled** —Options are Disabled. 
  * **Enabled** —Options are enabled. 

  
Enhanced Memory Test | Enables enhanced memory tests during the system boot and increases the boot time based on the memory.  |  **Note** |  Applicable for B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6,C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, and X210c M8   
---|---  
4.0(1) and later |  Disabled, Enabled, **Auto**

  * **Disabled** —Options are Disabled. 
  * **Enabled** —Options are enabled. 
  * **Auto** —Option is in auto mode. 

  
BME DMA Mitigation |  Allows you to disable the PCI BME bit to mitigate the threat from an unauthorized external DMA |  **Note** |  Applicable for B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5,B200 M6, C220 M6, C240 M6, X210c M6,C225 M6, C245 M6,C220 M7, C240 M7, X210c M7, X410c M7,M8, C220 M8, C240 M8, X210c M8 platforms only.   
---|---  
4.0(1), 4.0(2), 4.0(4), 4.1(1), 4.2(1), 4.3(4b). 4.3(5a) |  Enabled, **Disabled**

  * Disabled—Option is not restricted. 
  * Enabled—Option is restricted. 

  
MMIO High Granularity Size |  Selects the allocation size that is used to assign memory-mapped I/O (MMIO) resources. |  4.3(3c) and later |  1G, 4G, 16G, 32G, 64G, **256G** , 1024G, Auto  |  **Note** |  Auto and 32G option is applicable to M8 intel platforms only.  
---|---  
MMIO High Base |  The base memory size according to memory-address mapping for the I/O (MMIO resources) |  4.3(3c) and later |  512G, 1T, 2T, 4T, 16T, 24T, **32T** , 40T, 56T, Auto  |  **Note** |  Auto option is applicable to M8 intel platforms only.  
---|---  
CR QoS |  Prevents DRAM and overall system BW drop in the presence of concurrent DCPMM BW saturating threads, with minimal impact to homogenous DDRT-only usages, Good for multi-tenant use cases, VMs, and so on. Targeted for App Direct, but also improves memory mode. Targets the “worst-case” degradations.  |  **Note** |  Applicable for B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, and X210c M6 platforms only.  
---|---  
4.1(2) and later |  **Disabled** , Recipe 1, Recipe 2, Recipe 3, Mode 0, Mode 1, Mode 2 

  * Disabled—Feature disabled. 
  * Recipe 1—6 modules, 4 modules per socket optimized 
  * Recipe 2—2 modules per socket optimized 
  * Recipe 3—1 module per socket optimized 
  * Mode 0—Disable the PMem QoS Feature 
  * Mode 1—M2M QoS Enable;CHA QoS Disable 
  * Mode 2— M2M QoS Enable; CHA QoS Enable 

|  **Note** |  Mode 0, Mode 1, Mode 2 options are applicable for M6 servers only.  
---|---  
CR FastGo Config |  CR FastGo Config improves DDRT non-temporal write bandwidth when FastGO is disabled. When FastGO is enabled, it gives a faster flow of NT writes into the uncore, When FastGO is disabled, it lessens NT writes queueing up in the CPU uncore, thereby improving sequentially at DCPMM, resulting in improved bandwidth.  |  4.1(2) and later |  **Auto** , Option 1—5, Enable Optimization, Disable Optimization  |  **Note** |  Enable Optimization, Disable Optimization options are available for M6 servers only.  
---|---  
DCPMM Firmware Downgrade | To configure DCPMM Firmware Downgrade.  |  **Note** |  Applicable for B480 M5, C220 M5, C240 M5, C480 M5,S3260 M5, B200 M6, C220 M6, C240 M6, and X210c M6 platforms only.  
---|---  
4.0(1) and later |  **Disabled** , Enabled 

  * Disabled—Options are Disabled. 
  * Enabled—Options are enabled. 

  
Memory Refresh Rate |  To configure the refresh interval rate for internal memory. |  **Note** |  Applicable for B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5,B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, and X410c M7 platforms only.   
---|---  
4.0(1) and later |  Auto, **1x Refresh** , 2x Refresh, 3x, 4x  |  **Note** |  1x Refresh is the default for M5, M7, M8 servers.  
---|---  
eADR Support |  Extended asynchronous DRAM refresh (eADR) ensures that CPU caches lines with data are flushed at the right time and in the desired order and are also included in the power fail protected domain.  |  **Note** |  Applicable for B200 M6, C220 M6, C240 M6, X210c M6,C220 M7, C240 M7, X210c M7, and X410c M7 platforms only.  
---|---  
4.2(1) and later |  **Disabled** , Enabled, Auto 

  * Disabled—Options are Disabled. 
  * Enabled—Options are enabled. 
  * Auto—Option is in auto mode. 

  
Memory Bandwidth Boost |  Allows to boost the memory bandwidth. |  **Note** |  Applicable for C220 M6, C240 M6, B200 M6, and X210c M6 platforms only.  
---|---  
4.2(1) and later |  Disabled, **Enabled**

  * Disabled—Options are Disabled. 
  * Enabled—Options are enabled. 

  
Memory Size Limit in GB |  Limits the capacity in Partial Memory Mirror Mode up to 50 percent of the total memory capacity. The memory size can range from 0 GB to 65535 GB in increments of 1 GB.  |  **Note** |  Applicable for B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, and X210c M8 platforms only.   
---|---  
4.0(2) and later |  **0** \- 65535 with a step size of 1   
Memory Thermal Throttling Mode |  Provides a protective mechanism to ensure the memory temperature is within the limits. When the temperature exceeds the maximum threshold value, the memory access rate is reduced and Baseboard Management Controllerf (BMC) adjusts the fan to cool down the memory to avoid DIMM damage due to overheat  |  **Note** |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8   
---|---  
4.0(1) and later |  **CLTT with PECI** , Disabled 

  * Disabled—Options are Disabled.
  * CLTT with PECI—Closed Loop Thermal Throttling (CLTT) with Platform Environment Control Interface (PECI). 

  
NUMA Optimized |  Whether the BIOS supports NUMA.  |  **Note** |  Applicable for B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, and X210c M8 platforms only.   
---|---  
4.0(1) and later |  **Enabled** , Disabled 

  * Disabled—The BIOS does not support NUMA. 
  * Enabled—The BIOS includes the ACPI tables that are required for NUMA-aware operating systems. If you enable this option, the system must disable Inter-Socket Memory interleaving on some platforms. 

  
NVM Performance Setting |  enables efficient major mode arbitration between DDR and DDRT transactions on the DDR channel to optimize channel BW and DRAM latency.  |  4.0(2) and later |  **BW Optimized** , Latency Optimized, Balanced Profile 

  * BW Optimized—Optimized for DDR and DDRT BW. This is the default option. 
  * Latency Optimized—Better DDR latency in the presence of DDRT BW. Available for M5 servers only. 
  * Balanced Profile—Optimized for Memory mode. 

  
Operation Mode |  This option allows you to configure Operation Mode. |  4.2(1) and later |  **Test-Only** , Test and Repair   
Panic and High Watermark |  Controls the delayed refresh capability of the memory controller. |  **Note** |  Applicable for B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, and X410c M7 platforms.   
---|---  
4.2(1) and later |  High, **Low**

  * High—The memory controller is allowed to postpone up to a maximum of eight refresh commands. The memory controller executes all the postponed refreshes within the refresh interval. For the ninth refresh command, the refresh priority becomes Panic and the memory controller pauses the normal memory transactions until all the postponed refresh commands are executed. 
  * Low—The memory controller is not allowed to postpone refresh commands.  |  **Note** |  It is recommended to leave this setting in the default state (Low) which will help to reduce susceptibility to Rowhammer-style attacks.   
---|---  

  
Partial Cache Line Sparing |  Partial cache line sparing (PCLS) is an error-prevention mechanism in memory controllers. PCLS statically encodes the locations of the faulty nibbles of bits into a sparing directory along with the corresponding data content for replacement during memory accesses.  |  **Note** |  Applicable for B200 M6, C240 M6, C220 M6, X210c M6, C220 M7, C240 M7, X210c M7, and X410c M7 platforms only.  
---|---  
4.2(1) and later |  Disabled, **Enabled** |  **Note** |  For M7 servers, Disabled is the default value.   
---|---  
  
  * Disabled—Options are Disabled. 

  * Enabled—Options are enabled. 


  
Partial Memory Mirror Mode |  enables you to partially mirror by GB or by a percentage of the memory capacity. Depending on the option selected here, you can define either a partial mirror percentage or a partial mirror capacity in GB in available fields. You can partially mirror up to 50 percent of the memory capacity.  |  **Note** |  Applicable for B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, and X210c M8 platforms only.   
---|---  
4.1(1) and later |  **Disabled** , Percentage, Value in GB 

  * Disabled—Options are Disabled. 
  * Percentage—The amount of memory to be mirrored in the Partial Memory Mode is defined as a percentage of the total memory. 
  * Value in GB—The amount of memory to be mirrored in the Partial Memory Mode is defined in GB.  |  **Note** |  Partial Memory Mirror Mode is mutually exclusive to standard Mirroring Mode. Partial Mirrors 1-4 can be used in any number or configuration, provided they do not exceed the capacity limit set in GB or Percentage in the related options.   
---|---  

**Note** |  Value in GB option is not applicable for M8 platforms.  
---|---  
Partial Mirror Percentage |  Limits the amount of available memory to be mirrored as a percentage of the total memory. This can range from 0.000.01 % to 50.00 % in increments of 0.01 %.  |  **Note** |  Applicable for B200 M5, B480 M5, C220 M5, C240 M5, C480 M5,S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, and X210c M8 platforms only.   
---|---  
4.1(1) and later |  **0.00** \- 50.00 with a step size of 0.01   
Partial Mirrorn Size in GB, where _n_ ranges from 1 to 4.  |  Limits the amount of memory in Partial Mirror _n_ in GB. This can range from 0 GB to 65535 GB in increments of 1 GB.  |  **Note** |  Applicable for B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, and X410c M7 platforms only.   
---|---  
4.1(1) and later |  **0** \- 65535 with a step size of 1   
PCIe RAS Support | Whether the PCIe RAS port is enabled or disabled.  |  **Note** |  Applicable for B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6,C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, and X210c M8 platforms only.   
---|---  
4.0(1) and later |  Disabled, **Enabled**

  * Disabled—This option is Disabled. 
  * Enabled—This option is enabled. 

  
Runtime Post Package Repair |  Enables the soft post-package repairs of the corrected memory errors during OS runtime.  |  **Note** |  Applicable for C220 M8, C240 M8, X210c M8, and X410c M8 platforms only.  
---|---  
4.3(4b) and later |   
Memory RAS Configuration |  How the memory reliability, availability, and serviceability (RAS) is configured for the server. |  4.0(1) and later |  Maximum Performance, Mirroring, Lockstep, Mirror Mode 1LM, Partial Mirror Mode 1LM, Sparing, **ADDDC Sparing**

  * Maximum Performance—Optimizes the system performance and disables all the advanced RAS features. 
  * Mirroring—System reliability is optimized by using half the system memory as backup. This mode is used for UCS M4 and lower blade servers 
  * Lockstep—If the DIMM pairs in the server have an identical type, size, and organization and are populated across the SMI channels, you can enable lockstep mode to minimize memory access latency and provide better performance. Lockstep is enabled by default for B440 servers. 
  * Mirror Mode 1LM—Mirror Mode 1LM will set the entire 1LM memory in the system to be mirrored, consequently reducing the memory capacity by half. This mode is used for UCS M5 and M6 blade servers. 
  * Partial Mirror Mode 1LM—Partial Mirror Mode 1LM will set a part of the 1LM memory in the system to be mirrored, consequently reducing the memory capacity by half. This mode is used for UCS M5 and M6 blade servers. 
  * Sparing—System reliability is optimized by holding memory in reserve so that it can be used in case other DIMMs fail. This mode provides some memory redundancy, but does not provide as much redundancy as mirroring. 
  * ADDDC Sparing—System reliability is optimized by holding memory in reserve so that it can be used in case other DIMMs fail. This mode provides some memory redundancy, but does not provide as much redundancy as mirroring. 

  
Select PPR Type |  Post Package Repair (PPR) provides the ability to repair faulty memory cells by replacing them with spare cells. |  **Note** |  Applicable for B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6,C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, and X210c M8 platforms only.   
---|---  
4.1(1) and later |  Disabled, **Hard PPR**

  * Disabled—Options are Disabled. 
  * Hard PPR—This results in a permanent remapping of damaged storage cells. 

  
Snoopy Mode for 2LM |  Enables snoop-mode for DCPMM accesses while maintaining directory on all DRAM accesses. Snoops maintain cache coherence between sockets. Directory reduces snoops by keeping the remote node information locally (in memory). Directory lookups and updates add memory traffic  Directory is a good tradeoff for DRAM, but not necessarily for DCPMM. For non-NUMA workloads, when the feature is enabled, directory updates to DCPMM are eliminated, thereby helping DDRT bandwidth bound workloads. The directory is disabled for far memory accesses and instead snoops remote sockets to check for ownership. Directory is used only for DRAM (near memory).  |  4.0(1) and later |  **Disabled** , Enabled 

  * Disabled—This option is Disabled. 
  * Enabled—This option is enabled. 

  
Snoopy Mode for AD |  Enables snoop-mode for DCPMM accesses while maintaining directory on all DRAM accesses. Snoops maintain cache coherence between sockets. Directory reduces snoops by keeping the remote node information locally (in memory). Directory lookups and updates add memory traffic.  Directory is a good tradeoff for DRAM, but not necessarily for DCPMM. For non-NUMA workloads, when the feature is enabled, directory updates to DCPMM are eliminated, thereby helping DDRT bandwidth bound workloads. The directory is disabled for accesses to AD and instead snoops remote sockets to check for ownership. Directory is used only for DRAM accesses.  |  4.0(1) and later |  **Disabled** , Enabled 

  * Disabled—This option is Disabled. 
  * Enabled—This option is enabled. 

  
UMA |  As the name implies, UMA based clustering is the suggested clustering mode when the processor is configured as Uniform Memory Access (UMA) node, i.e. SNC is disabled.  |  **Note** |  Applicable for C220 M6, C240 M6, B200 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, and X210c M8 platforms only.   
---|---  
4.2(1) and later |  Disable-All-2All, **Hemisphere-2-clusters** , Quadrant-4-clusters  |  **Note** |  For M7 servers, the default value is Quadrant-4-clusters.   
---|---  
**Note** |  Quadrant-4-clusters option is not applicable for M8 platforms.  
---|---  
Volatile Memory Mode |  Allows the memory mode configuration. |  **Note** |  Applicable for C220 M6, C240 M6, B200 M6, X210c M6 platforms only.  
---|---  
4.0(2) and later |  1LM, **2LM**

  * 1LM—Configures 1 Layer Memory(1LM).This is the default value for M7 servers. 
  * 2LM—Configures 2 Layer Memory(1LM). 

  
Error Check Scrub |  Allows you to enable a memory device to perform memory checking, correction and count errors. |  **Note** |  Applicable for C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, and X210c M8 platforms only.  
---|---  
4.0(2) and later |  Disabled, Enabled with result collection, Enabled without result collection   
Rank Margin Tool |  Allows automated memory margin testing and is used to identify DDR margins at the rank level. |  **Note** |  Applicable for C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, and X210c M8 platforms only.  
---|---  
4.0(2) and later |  Enabled, Disabled  
Adaptive Refresh Management Level |  Selects Adaptive Refresh Management (ARFM) Level when refresh management (RFM) is required. |  **Note** |  Applicable for C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, and X210c M8 platforms only.   
---|---  
4.0(2) and later | **Default** , Level A, Level B, Level C   
Memory Mapped IO above 4GB |  Whether to enable or disable memory mapped I/O of 64-bitPCI devices to 4GB or greater address space. Legacy option ROMs are not able to access addresses above 4GB. PCI devices that are 64-bit compliant but use a legacy option ROM may not function correctly with this setting enabled.  |  **Note** |  Applicable for B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, C125 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, and X210c platforms only. M8   
---|---  
4.0(1) and later |  Disabled, **Enabled**

  * **Disabled** —This option is Disabled. 
  * **Enable** —This options is enabled. 

  
VGA Priority |  Allows you to set the priority for VGA graphics devices if multiple VGA devices are found in the system. |  **Note** |  Applicable for C220 M5, C240 M5, C220 M6, C240 M6, C220 M7, C240 M7, C220 M8, amd C240 M8 platforms only.  
---|---  
4.0(2) and later |  Offboard, **Onboard** , Onboard VGA Disabled 

  * **Onboard** —Priority is given to the onboard VGA device. BIOS post screen and OS boot are driven through the onboard VGA port 
  * **Offboard** ——Priority is given to thePCIE Graphics adapter. BIOS post screen and OS boot are driven through the external graphics adapter port. 
  * **Onboard VGA Disabled** —Priority is given to the PCIE Graphics adapter, and the onboard VGA device is disabled  |  **Note** |  The vKVM does not function when the onboard VGA is disabled.  
---|---  

  
Optimized Power Mode |  Automatically varies processor speed and power usage based on processor utilization to increase performance per watt. Most effective under moderate utilization.  |  **Note** |  Applicable for C220 M7, C240 M7, X210c M7, and X410c M7 platforms only.  
---|---  
4.3(2) and later |  Disabled, Enabled 

  * Disabled—This option is Disabled. 
  * Enable—This options is enabled. 

  
C1 Auto Demotion |  If enabled, CPU automatically demotes to C1 based on un-core auto-demote information. |  **Note** |  Applicable for C220 M6, C240 M6, B200 M6, X210c M6, C220 M7, C240 M7, X210c M7, and X410c M7 platforms only.  
---|---  
4.0(2) and later |  Disabled, Enabled, **Auto**

  * Disabled—This option is Disabled. 
  * Enable—This options is enabled. 

  
C1 Auto UnDemotion |  Select whether to enable processors to automatically undemote from C1. |  **Note** |  Applicable for C220 M6, C240 M6, B200 M6, X210c M6, C220 M7, C240 M7, X210c M7, and X410c M7 platforms only.  
---|---  
4.0(2) and later |  Disabled, Enabled, **Auto**

  * Disabled—This option is Disabled. 
  * Enable—This options is enabled. 

  
Enhanced CPU Performance |  Enhances CPU performance by adjusting server settings automatically.  |  **Note** |  Applicable for C220 M6, C240 M6, B200 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, and X210c M8 platforms only.   
---|---  
4.0(2) and later |  Disabled, **Auto**

  * Disabled—This option is Disabled. 
  * Auto—Allows to adjust server settings to increase the processor performance. 

|  **Note** |  Enabling this functionality may increase power consumption.  
---|---  
LLC Dead Line |  In CPU non-inclusive cache scheme, Mid-Level Cache (MLC) evictions are filled into the Last-Level Cache (LLC). When lines are evicted from the MLC, the core can flag them as dead (not likely to be read again). The LLC has the option to drop dead lines and not fill them in the LLC.  |  **Note** |  Applicable for C220 M6, C240 M6, B200 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, and X210c M8 platforms only.   
---|---  
4.0(2) and later |  Disabled, Enabled, **Auto**

  * **Disabled** —The dead lines are always dropped and are never filled into the LLC. 
  * **Enable** —Allows the LLC to fill dead lines into the LLC if there is free space available. This is the default option. 
  * Auto—The CPU determines the LLC dead line allocation. 

  
UPI Link Enablement |  Enables the number of Ultra Path Interconnect (UPI) links required by the processor. |  **Note** |  Applicable for C220 M6, C240 M6, B200 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, and X210c M8 platforms only.   
---|---  
4.0(2) and later |  **Auto** , 1, 2, 3   
UPI Power Manangement |  The UPI power management can be used for conserving power on the server. |  **Note** |  Applicable for C220 M6, C240 M6, B200 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, and X210c M8 platforms only.   
---|---  
4.0(2) and later |  Disabled, **Enabled**

  * **Disabled** —This option is Disabled. 
  * **Enable** —This options is enabled. 

  
XPT Remote Prefetch |  This feature allows an LLC request to be duplicated and sent to an appropriate memory controller in a remote machine based on the recent LLC history to reduce latency.  |  **Note** |  Applicable for C220 M6, C240 M6, B200 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, and X210c M8 platforms only.   
---|---  
4.0(2) and later |  **Disabled** , Enabled 

  * **Disabled** —This option is Disabled. 
  * **Enable** —This options is enabled. 
  * **Auto** —The CPU determines the functionality. 

  
Latency Optimized Mode |  A set of BIOS settings that prioritize low latency and consistent performance over energy efficiency or other optimizations. |  **Note** |  Applicable for C220 M8, C240 M8, X210c M8, and X410c M8 platforms only.  
---|---  
4.3(6a) |  **Disabled** , Enabled 

  * **Disabled** —Options are Disabled. 
  * **Enabled** —Options are enabled. 

  
QPI Link Frequency Select | The Intel QuickPath Interconnect (QPI) link frequency, in megatransfers per second (MT/s). |  4.0(4) and later |  **Auto** , 9.6 GT/s, 10.4 GT/s, 11.2GT/s, 12.8GT/s, 14.4GT/s, 16.0GT/s, 20.0GT/s, 16.0GT/s, 20.0GT/s,24.0GT/s, Auto, Use Per Link Setting  |  **Note** |  9.6 GT/s, 10.4 GT/s options available for M5 and M6 servers only. 11.2GT/s for M6 and 12.8GT/s, 14.4GT/s, 16.0GT/s, 20.0GT/s for M7.   
---|---  
**Note** |  16.0GT/s, 20.0GT/s,24.0GT/s, Auto, Use Per Link Setting is applicable for M8 servers only.  
---|---  
Legacy USB Support |  Whether the system supports legacy USB devices. |  **Note** |  Applicable for B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, C240 M6, C220 M6, B200 M6, and X210c M6 platforms only.  
---|---  
4.2(1) and later |  Auto,**Enabled** , Disabled   
USB Port Front |  Whether the front panel USB devices are enabled or disabled. |  **Note** |  Applicable for C240 M5, C220 M5, C480 M5, B200 M6, X210c M6, X210c M7, X410c M7, X210c M8, and X410c M8 platforms only.  
---|---  
4.2(1) and later |  **Enabled** , Disabled   
USB Port Internal |  Whether the internal USB devices are enabled or disabled. |  **Note** |  Applicable for C240 M5, C220 M5, C480 M5, C220 M6, and C240 M6 platforms only.  
---|---  
4.2(1) and later |  **Enabled** , Disabled   
USB Port KVM |  Whether the USB Port KVM devices are enabled or disabled. |  **Note** |  Applicable for C240 M5, C220 M5, C480 M5, B200 M6, X210c M6, X210c M7, X410c M7, X210c M8, and X410c M8 platforms only.  
---|---  
4.2(1) and later |  **Enabled** , Disabled   
USB Port Rear |  Whether the USB port rear devices are enabled or disabled. |  **Note** |  Applicable for C240 M5, C220 M5, C480 M5, C220 M6, C240 M6, C220 M7, C240 M7, C220 M8, and C240 M8 platforms only.  
---|---  
4.2(1) and later |  **Enabled** , Disabled   
USB Port:M.2 Storage |  Whether the SD card drives are enabled or disabled. |  **Note** |  Applicable for C220 M5, C240 M5, C480 M5, B200 M6, X210c M6, X210c M7, X410c M7, X210c M8, and X410c M8 platforms only.   
---|---  
4.2(1) and later |  **Enabled** , Disabled   
PRMRR Size |  Processor Reserved Memory Range Registers (PRMRR) is the size of the protected region in the system DRAM.  |  4.3(2) and later |  Invalid Config, 1G, 2G, 4G, 8G, 16G, 32G, 64G, 128G, 256G, 512G, 128M, Auto, 256M, 512M  |  **Note** |  128M, Auto, 256M, 512M options are available only for M7 servers.  
---|---  
Adjacent Cache Line Prefetcher |  Whether the processor fetches cache lines in even/odd pairs instead of fetching just the required line. |  4.0(2) and later |  Disabled, **Enabled**

  * Disabled—This option is Disabled. 
  * Enable—This option is enabled. 

  
Autonomous Core C State |  Enables CPU Autonomous C-State, which converts the HALT instructions to the MWAIT instructions. |  4.0(2) and later |  **Disabled** , Enabled   
Boot Performance Mode |  Allows the user to select the BIOS performance state that is set before the operating system handoff. |  4.0(2) and later | **Max Performance** , Max Efficient, Set by Intel NM  |  **Note** |  Set by Intel NM option is not applicable for M8 intel platforms.  
---|---  
DFX OSB |  Controls the Opportunistic Snoop Broadcast (OSB) feature. OSB is used by CHA to broadcast snoops under lightly loaded ring or Intel UPI link condition. It is used to reduce the latency due to the directory lookup.  | 4.3(4a) and later |  Auto, **Enabled** , Disabled   
Processor CMCI |  Allows the CPU to trigger interrupts on corrected machine check events. The corrected machine check interrupt (CMCI) allows faster reaction than the traditional polling timer.  |  4.0(2) and later |  **Disabled** , Enabled   
Configurable TDP Level |  Allows you to set a customized value for Thermal Design Power (TDP). |  4.0(2) and later |  **Normal** , Level 1, Level 2   
Core Multi Processing |  Sets the state of logical processor cores per CPU in a package. If you choose All as the value, Intel Hyper Threading technology is also enabled.  |  4.0(2) and later |  **All** , 1 through 86 

  * All— Enables multiprocessing on all logical processor cores.
  * 1 through 86—Specifies the number of logical processor cores per CPU that can run on the server. To disable multiprocessing and have only one logical processor core per CPU running on the server, choose 1.  |  **Note** |  For M6 servers, it ranges from 1 through 48.   
---|---  
**Note** |  1, 2, and 3 options are not applicable for M8 servers.  
---|---  
**Note** |  From 65 to 86 is applicable for M8 servers only.  
---|---  
**Note** |  From 1 to 64 is applicable for M7 servers only.  
---|---  

  
Energy Performance |  Allows you to determine whether system performance or energy efficiency is more important on this server. |  4.0(2) and later |  Performance, **Balanced Performance,** Balanced power, power   
CPU Performance |  CPU performance by adjusting server settings automatically. |  4.0(2) and later |  **Disabled** , Enabled   
Energy Efficient Turbo |  When energy efficient turbo is enabled, the optimal turbo frequency of the CPU turns dynamic based on CPU utilization. The power/performance bias setting also influences the energy efficient turbo.  |  4.0(2) and later |  **Disabled** , Enabled   
Enhanced Intel Speedstep(R) Technology |  Whether the processor uses Enhanced Intel SpeedStep Technology, which allows the system to dynamically adjust processor voltage and core frequency. This technology can result in decreased average power consumption and decreased average heat production.  |  4.0(2) and later |  Disabled, **Enabled**  
Processor EPP Enable |  Allows you to determine whether system performance or energy efficiency is more important on this server.  |  4.0(2) and later |  Disabled, **Enabled**  
Processor EPP Profile |  Allows you to determine whether system performance or energy efficiency is more important on this server.  |  4.0(2) and later |  Performance, Balanced Performance, Balanced power, power   
Execute Disable Bit |  Classifies memory areas on the server to specify where the application code can execute. As a result of this classification, the processor disables code execution if a malicious worm attempts to insert code in the buffer. This setting helps to prevent damage, worm propagation, and certain classes of malicious buffer overflow attacks.  |  4.0(2) and later |  Disabled, **Enabled**  
IOAT Configuration |  Enables or disables the CPM (Content Processing Module) in IOAT (Intel® I/O Acceleration Technology) accelerators. |  4.3(3c) and later |  Disabled, Enabled  
Local X2 Apic |  Allows you to set the type of Advanced Processor Interrupt controller (APIC) architecture. |  4.0(2) and later |  Disabled, Enabled  
Hardware Prefetcher |  Whether the processor allows the Intel hardware prefetcher to fetch streams of data and instructions from memory into the unified second-level cache when necessary.  |  4.0(2) and later |  Disabled, Enabled  
CPU Hardware Power Management |  Enables processor Hardware Power Management (HWPM). |  4.0(2) and later |  Disabled, **HWPM Native Mode** , HWPM OOB Mode, Native Mode with no Legacy   
IMC Interleaving |  This BIOS option controls the interleaving between the Integrated Memory Controllers (IMCs). |  4.0(2) and later |  **Auto** , 1-way Interleave, 2-way Interleave   
Intel Dynamic Speed Select |  Intel Dynamic Speed Select modes allow you to run the CPU with different speeds and cores in auto mode. |  4.0(2) and later |  **Disabled** , Enabled   
Intel HyperThreading Tech |  Whether the processor uses Intel Hyper-Threading Technology, which allows multithreaded software applications to execute threads in parallel within each processor.  |  4.0(2) and later |  Disabled, **Enabled**  
Intel Turbo Boost Tech |  Whether the processor uses Intel Turbo Boost Technology, which allows the processor to automatically increase its frequency if it is running below power, temperature, or voltage specifications.  |  4.0(2) and later |  **Disabled** , Enabled   
Intel(R) VT |  Whether the processor uses Intel Virtualization Technology for Directed I/O (VT-R) |  4.0(2) and later |  Disabled, **Enabled**  
DCU IP Prefetcher |  Whether the processor uses the DCU IP Prefetch mechanism to analyze historical cache access patterns and preload the most relevant lines in the L1 cache.  |  4.0(2) and later |  Disabled, **Enabled**  
KTI Prefetch |  KTI prefetch is a mechanism to get the memory read started early on a DDR bus.  |  4.0(2) and later |  Disabled, **Enabled** , Auto  |  **Note** |  Auto option is not applicable for M5 servers.  
---|---  
LLC Prefetch |  Whether the processor uses the LLC Prefetch mechanism to fetch the date into the LLC. |  4.0(2) and later |  Disabled, **Enabled**  
Package C State Limit |  The amount of power available to the server components when they are idle. |  4.0(2) and later |  No Limit, Auto, **C0 C1 State** , C2, C6 Non Retention, C6 Retention  |  **Note** |  C6 Retention option is not applicable for M8 servers.  
---|---  
Patrol Scrub |  It sets the interval for a full memory scan. |  4.0(2) and later |  Disabled, **Enabled**

  * Enable—The system periodically reads and writes memory searching for ECC errors. If any errors are found, the system attempts to fix them. This option may correct single bit errors before they become multi-bit errors, but it may adversely affect performance when the patrol scrub is running. 
  * Disable—The system checks for memory ECC errors only when the CPU reads or writes a memory address. 

  
Patrol Scrub Configuration |  It sets the interval for a full memory scan. |  4.0(2) and later |  Enabled, Disabled, Enable at End of POST

  * Enable—The system periodically reads and writes memory searching for ECC errors. If any errors are found, the system attempts to fix them. This option may correct single bit errors before they become multi-bit errors, but it may adversely affect performance when the patrol scrub is running. 
  * Disable—The system checks for memory ECC errors only when the CPU reads or writes a memory address. 

|  **Note** |  Enabled option is applicable for M6 servers only.  
---|---  
Processor C1E |  Allows the processor to transition to its minimum frequency upon entering C1. This setting does not take effect until after you have rebooted the server.  |  4.0(2) and later |  **Disabled** , Enabled   
Processor C6 Report |  Whether the processor sends the C6 report to the operating system. |  4.0(2) and later |  **Disabled** , Enabled   
P STATE Coordination |  **Note** |  It is also called EIST PSD Function in UCSM.  
---|---  
Allows you to define how BIOS communicates the P-state support model to the operating system. There are 3 models as defined by the Advanced Configuration and Power Interface (ACPI) specification.  |  4.0(2) and later |  **SW All** , HW All, SW Any  |  **Note** |  SW Any option is available for M5 servers only.  
---|---  
Power Performance Tuning |  Determines if the BIOS or Operating System can turn on the energy performance bias tuning. The options are BIOS and operating system.  |  4.0(2) and later |  BIOS, **OS** , PECI  |  **Note** |  PECI option is available for M6 and M7 servers only.  
---|---  
UPI Link Frequency Select |  Allows you to select different UPI link frequency running. |  4.0(2) and later |  **Auto** , 9.6GT/S, 10.4GT/S, 11.2GT/S, 12.8GT/s, 14.4GT/s, 16.0GT/s, 20.0GT/s, 24.0GT/s, Use Per Link Setting  |  **Note** | 

  * 12.8GT/s, 14.4GT/s, 16.0GT/s, 20.0GT/s options are available for M7 servers only.
  * 11.2GT/S option is available for M6 server only.
  * 16,20, 24, Auto, Use Per Link Setting is applicable for M8 servers only

  
---|---  
Sub Numa Clustering |  Whether the CPU supports sub NUMA clustering, in which the tag directory and the memory channel are always in the same region. |  4.0(2) and later |  **Disabled** , Enabled, Auto, SNC2, SNC4  |  **Note** | 

  * Auto option is available for M5, M7, and M8 servers only. 
  * Enabled option is available for M6 and M8 servers only. 
  * Disabled option is available for M6, M7, and M8 servers only. 
  * SNC2, SNC4 options are available for M7 servers only. 

  
---|---  
DCU Streamer Prefetch |  Whether the processor uses the DCU IP Prefetch mechanism to analyze historical cache access patterns and preload the most relevant lines in the L1 cache.  |  4.0(2) and later |  Disabled, **Enabled** , Auto  |  **Note** |  Auto option is applicable to M8 intel platforms only.  
---|---  
Uncore Frequency Scaling |  Allows you to configure the scaling of the uncore frequency of the processor. |  4.0(2) and later |  Disabled, **Enabled** , Mode 0, and Mode 1  |  **Note** |  Mode 0 and Mode 1 is applicable for M8 servers only with Mode 1 being default.  
---|---  
Uncore Frequency Scaling IO |  Adjusts the frequency of processor uncore components responsible for I/O operations to optimize power and performance.  |  6.0(1a.0) and later |  **Mode 1** , Mode 0   
Workload Configuration |  This feature allows for workload optimization. |  4.0(2) and later |  Balanced, IO Sensitive  
XPT Prefetch |  Whether XPT prefetch is used to enable a read request that is sent to the last level cache to issue a copy of that request to the memory controller prefetcher.  |  4.0(2) and later |  **Auto** , Disabled, Enabled   
X2APIC Opt-Out Flag |  Prevents the operating system from enabling extended xAPIC (x2APIC) mode when the OS is not working with x2APIC. |  4.2(3) and later |  **Disabled** , Enabled   
Intel Speed Select |  Allows you to adjust different cores to operate in different frequencies to have a better power efficiency. The values **Config 1** and **Config 2** are not supported on Cisco UCS M6 and M7 servers.  For Cisco UCS M6 and Cisco UCS M7 servers, the values **Config 3** and **Config 4** (4th Gen Intel Xeon Scalable processors and 5th Gen Intel Xeon Scalable processors) are equivalent to the values **Config 1** and **Config 2** (3rd Gen Intel Xeon Scalable processors).  |  4.0(2) and later |  **Auto** , Base, Config 1, Config 2, Config 3, Config 4 

  * Config 1 and Config 2 are options available for M5 servers only with Base as the default.
  * Auto is the default for M8.

  
IIO eDPC Support |  The eDPC (Enhanced Downstream Port Containment) allows a downstream link to be disabled after an uncorrectable error, enabling recovery possible in a controlled and robust manner. This can be one of the following:  |  4.3(6c) and later |  Disabled, On Fatal Error, **On Fatal and Non-Fatal Errors**

  * **Disabled** —eDPC support is turned off, and the system does not take any action to disable downstream links in response to errors. 
  * **On Fatal Error** —eDPC is enabled only for fatal errors.is not supported on Cisco UCS C225 M8, Cisco UCS C245 M8, and X215c M8 servers. 
  * **On Fatal and Non-Fatal Errors** —eDPC is enabled for both fatal and non-fatal errors. 

  
Baud Rate |  What Baud rate is used for the serial port transmission speed. If you disable Console Redirection, this option is not available. |  4.2(1) and later |  9.6k, 19.2k, 38.4k, 57.6k, **115.2k**  
CDN Control |  Consistent Device Naming allows Ethernet interfaces to be named in a consistent manner. This makes Ethernet interface names more uniform, easy to identify, and persistent when adapter or other configuration changes are made.  |  4.2(1) and later |  **Enabled** , Disabled   
Adaptive Memory Training |  When this token is enabled, the BIOS saves the memory training results (optimized timing/voltage values) along with CPU/memory configuration information and reuses them on subsequent reboots to save boot time. The saved memory training results are used only if the reboot happens within 24 hours of the last save operation.  |  4.2(1) and later |  **Enabled** , Disabled   
BIOS Techlog Level |  This option denotes the type of messages in BIOS tech log file. |  4.2(1) and later |  Maximum, **Minimum** , Normal 

  * Maximum—Critical messages will be displayed in the log file. This is the default option 
  * Minimum—Warning and loading messages will be displayed in the log file. 
  * Normal—Normal and information related messages will be displayed in the log file. 

  
OptionROM Launch Optimization |  The Option ROM launch is controlled at the PCI Slot level, and is enabled by default. In configurations that consist of a large number of network controllers and storage HBAs having Option ROMs, all the Option ROMs may get launched if the PCI Slot Option ROM Control is enabled for all. However, only a subset of controllers may be used in the boot process. When this token is enabled, Option ROMs are launched only for those controllers that are present in boot policy.  |  4.2(1) and later |  **Enabled** , Disabled   
Console Redirection |  Allows a serial port to be used for console redirection during POST and BIOS booting. After the BIOS has booted and the operating system is responsible for the server, console redirection is irrelevant and has no effect  |  4.2(1) and later |  **Disabled** , COM 0, COM 1 

  * COM 0 enables serial port for console redirection during POST. This option is valid only for M6 blade servers and rack-mount servers. 
  * COM 1 or serial-port-b enables serial port B for console redirection and allows it to perform server management tasks. This option is only valid for rack-mount servers. 

  
Flow Control |  Whether a handshake protocol is used for flow control. Request to Send / Clear to Send (RTS/CTS) helps to reduce frame collisions that can be introduced by a hidden terminal problem.  |  4.2(1) and later |  **None** , RTC-CTS   
FRB 2 Timer |  Whether the FRB2 timer is used for recovering the system if it hangs during POST. |  4.2(1) and later |  **Enabled** , Disabled   
OS Boot Watchdog Timer  |  Whether the BIOS programs the watchdog timer with a predefined timeout value. If the operating system does not complete booting before the timer expires, the CIMC resets the system and an error is logged.  |  4.2(1) and later |  Enabled, **Disabled**  
OS Boot Watchdog Timer Policy |  What action the system takes if the watchdog timer expires. |  4.2(1) and later |  **Power-off** , Reset   
OS Watchdog Timer Timeout |  What timeout value the BIOS uses to configure the watchdog timer. |  4.2(1) and later |  5 minutes, **10 minutes** , 15 minutes, 20 minutes   
Terminal Type |  What type of character formatting is used for console redirection. |  4.2(1) and later |  PC-ANSI, **VT100** , VT100-PLUS, VT-UTF8   
Multikey Total Memory Encryption (MK-TME) |  MK-TME allows you to have multiple encryption domains with one with own key. Different memory pages can be encrypted with different keys.  |  4.2(1) nnd later |  Enabled, **Disabled**  
Software Guard Extensions (SGX) |  Allows you to enable Software Guard Extensions(SGX) feature. |  4.2(1) and later |  Enabled, **Disabled**  
Total Memory Encryption (TME) |  Allows you to provide the capability to encrypt the entirety of the physical memory of a system. |  4.2(1) and later |  **Enabled** , Disabled   
Select Owner EPOCH Input Type |  Allows you to change the seed for the security key used for the locked memory region that is created. |  4.2(1) and later |  SGX Owner EPOCH activated, Change to New Random Owner EPOCHs, **Manual User Defined Owner EPOCHs** , SGX Owner EPOCH deactivated  |  **Note** |  SGX Owner EPOCH deactivated option is applicable for M8 servers only.  
---|---  
SGX Auto MP Registration Agent |  Allows you to enable the registration authority service to store the platform keys. |  4.2(1) and later |  Enabled, **Disabled**  
SGX Epoch 0 |  Allows you to define the SGX EPOCH owner value for the EPOCH number designated by 0. |  4.2(1) and later |  0 - ffffffffffffffff with a step size of 1  
SGX Epoch 1 |  Allows you to define the SGX EPOCH owner value for the EPOCH number designated by 1. |  4.2(1) and later |  0 - ffffffffffffffff with a step size of 1  
SGX Factory Reset |  Allows the system to perform SGX factory reset on subsequent boot. |  4.2(1) and later |  Enabled, **Disabled**  
SGX PubKey Hashn where _n_ ranges from 0 to 3.  |  Allows you to set the Software Guard Extensions (SGX) value. |  4.2(1) and later |  **SGX PUBKEY HASH0** , SGX PUBKEY HASH1, SGX PUBKEY HASH2, SGX PUBKEY HASH3 

  * SGX PUBKEY HASH0—Between 7-0. 
  * SGX PUBKEY HASH1—Between 15-8. 
  * SGX PUBKEY HASH2—Between 23-16. 
  * SGX PUBKEY HASH3—Between 31-24. 

  
SGX Write Enable |  Allows you to enable SGX Write feature. |  4.2(1) and later |  **Enabled** , Disabled   
SGX Package Information In-Band Access |  Allows you to enable SGX Package Info In-Band Access. |  4.2(1) and later |  Enabled, **Disabled**  
SGX QoS |  Allows you to enable SGX QoS. |  4.2(1) and later |  **Enabled** , Disabled   
SHA-1 PCR Bank |  The Platform Configuration Register (PCR) is a memory location in the TPM. Multiple PCRs are collectively referred to as a PCR bank. A Secure Hash Algorithm 1 or SHA-1 PCR Bank allows to enable or disable TPM security.  |  4.2(1) and later |  **Enabled** , Disabled  |  **Note** |  For C245 M8, it is Disabled by default.   
---|---  
SHA256 PCR Bank |  The Platform Configuration Register (PCR) is a memory location in the TPM. Multiple PCRs are collectively referred to as a PCR bank. A Secure Hash Algorithm 256-bit or SHA-256PCR Bank allows to enable or disable TPM security.  |  4.2(1) and later |  **Enabled** , Disabled   
SHA384 PCR Bank* |  The Platform Configuration Register (PCR) is a memory location in the TPM. Multiple PCRs are collectively referred to as a PCR bank. A Secure Hash Algorithm 384-bit or SHA-384PCR Bank allows to enable or disable TPM security.  |  4.3(3a) and later |  Enabled, **Disabled**  
Trusted Platform Module State |  Whether to enable or disable the Trusted Platform Module (TPM), which is a component that securely stores artifacts that are used to authenticate the server.  |  4.2(1) and later |  **Enabled** , Disabled   
Trust Domain Extension  |  Whether to enable or disable the Trust Domain Extension (TDX), which protects the sensitive data and applications from unauthorized access.  |  4.3(3a) and later |  Enabled, **Disabled**  
TDX Secure Arbitration Mode (SEAM) Loader |  Whether to enable or disable the TDX Secure Arbitration Mode (SEAM) Loader, which helps to verify the digital signature on the Intel TDX module and load it into the SEAM-memory range.  |  4.3(3a) and later |  TDX Secure Arbitration Mode (SEAM) Loader  
TPM Pending Operation |  Trusted Platform Module (TPM) Pending Operation option allows you to control the status of the pending operation. |  4.2(1) and later |  **None** , TpmClear   
TPM Minimal Physical Presence |  Whether to enable or disable TPM Minimal Physical Presence, which enables or disables the communication between the OS and BIOS for administering the TPM without compromising the security.  |  4.2(1) and later |  Enabled, **Disabled**  
Intel Trusted Execution Technology Support |  Whether to enable or disable Intel Trusted Execution Technology (TXT), which provides greater protection for information that is used and stored on the business server.  |  4.2(1) and later |  **Enabled** , Disabled   
Security Device Support |  It controls the entire TPM functionality. |  4.2(3) and later |  **Enabled** , Disabled   
DMA Control Opt-In Flag |  Enabling this token enables Windows 2022 Kernel DMA Protection feature. The OS treats this as a hint that the IOMMU should be enabled to prevent DMA attacks from possible malicious devices.  |  4.2(2) and later |  Enabled, **Disabled**  
LIMIT CPU PA to 46 Bits |  Limits CPU physical address to 46 bits to support the older Hyper-v CPU platform. |  4.2(2) and later |  **Enabled** , Disabled   
GPU Direct CPU1 |  When enabled, ACS is disabled for GPUs on the specified CPU in systems using the UCXS-580P. | 6.0(1.250229) |  Enabled, **Disabled**  
GPU Direct CPU2 |  When enabled, ACS is disabled for GPUs on the specified CPU in systems using the UCXS-580P. |  6.0(1.250229) |  Enabled, **Disabled**  
GPU Direct CPU3 |  When enabled, ACS is disabled for GPUs on the specified CPU in systems using the UCXS-580P. |  6.0(2x) |  Enabled, **Disabled**  
GPU Direct CPU4 |  When enabled, ACS is disabled for GPUs on the specified CPU in systems using the UCXS-580P. |  6.0(2x) |  Enabled, **Disabled**  
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

SHA384 PCR Bank Bios token supports PID models UCS-TPM-002D and UCS-TPM-002D-D. 

* * *  
  
---|---

---

## Page 4: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-boot-options-bios-settings.html

## Boot Options BIOS Settings  
  
The following table lists the boot options BIOS settings that you can configure through a BIOS policy or the default BIOS settings: 

Name |  Description |  Supported Attributes  
---|---|---  
Version |  Platform |  Values |  Dependencies  
Number of Retries |  Number of attempts to boot.  |  4.1(1) and later |  B200 M5, B480 M5, C480 M5 |  Infinite. **13** , 5 

  * **Infinite** —The system attempts all configured boot options and repeats until the system boots or is interrupted manually. 
  * **5, 13** —The system attempts all configured boot options and repeats the selected number of times until the system boots or is interrupted. If all attempts fail, the system prompts to continue. Value 13 is the default value for Cisco UCS B200 M5 and 5 is the default value for Cisco UCS B480 M5. 

| Applicable only when Boot Option Retry is Enabled.  
**Cool Down Time (sec)** |  The time to wait (in seconds) before the next boot attempt. This can be one of the following: |  4.1(1) and later |  B200 M5, B480 M5, C480 M5 |  15 sec, 45 sec, **90 sec**

  * **15, 45, 90** —System waits for the selected time in seconds before the next boot attempt. 

|  Applicable only when Boot Option Retry is Enabled.  
Boot Option Retry |  Whether the BIOS retries NON-EFI based boot options without waiting for user input. |  4.1(1) and later |  B200 M5, B480 M5, C480 M5 |  **Disabled** , Enabled 

  * **Disabled** —Waits for user input before retrying NON-EFI based boot options. 
  * **Enabled** —Continually retries NON-EFI based boot options without waiting for user input. 

|   
IPV4 HTTP Support |  Enables or disables IPv4 support for HTTP.  |  4.2(1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, C125 M5, B200 M6, C225 M6, C245 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C225 M8, C245 M8, X215c M8, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  Disabled, **Enabled**

  * **Disabled** —IPv4 HTTP support is not available. 
  * **Enabled** —IPv4 HTTP support is made available. 

|  The Network Stack token value should be Enabled.  
IPV6 HTTP Support |  Enables or disables IPv6 support for HTTP.  |  4.2(1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, C125 M5, B200 M6, C225 M6, C245 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C225 M8, C245 M8, X215c M8, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  Disabled, **Enabled**

  * **Disabled** —IPv6 HTTP support is not available. 
  * **Enabled** —IPv6 HTTP support is made available. 

|  The Network Stack token value should be Enabled.  
IPV4 PXE Support |  Enables or disables IPv4 support for PXE.  |  4.2(1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, C125 M5, B200 M6, C225 M6, C245 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  Disabled, **Enabled**

  * **Disabled** —IPv4 PXE support is not available. 
  * **Enabled** —IPv4 PXE support is made available. 

|   
IPV6 PXE Support |  Enables or disables IPv6 support for PXE.  |  4.2(1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, C125 M5, B200 M6, C225 M6, C245 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  Disabled, **Enabled**

  * **Disabled** —IPv6 PXE support is not available. 
  * **Enabled** —IPv6 PXE support is made available. 

|  The Network Stack token value should be Enabled.  
Network Stack |  This option allows you to enable or disable the complete network style of the system. |  4.1(1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, C125 M5, B200 M6, C225 M6, C245 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  Disabled,**Enabled**

  * **Disabled** —Network Stack support is not available. 
  * **Enabled** —Network Stack support is available. 

|  When disabled, the value set for IPV6 PXE, IPV4HTTP, and IPV6HTTP Support does not impact the system.  
Power ON Password |  This token requires that you set a BIOS password before using the F2 BIOS configuration. If enabled, password needs to be validated before you access BIOS functions such as IO configuration, BIOS set up, and booting to an operating system using BIOS.  |  4.1(1) and later |  C220 M5, C240 M5, C480 M5, C125 M5, C220 M6, C240 M6, C245 M6, C225 M6, C220 M7, C240 M7, C225 M8, C245 M8, C220 M8, C240 M8, XE1X0M8  |  **Disabled** , Enabled 

  * **Disabled** —Power On Password is disabled. 
  * **Enabled** —Power On Password is enabled. 

|   
P-SATA OptionROM |  This options allows you to select the P-SATA mode. |  4.1(1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5 |  Disabled, **LSI SW RAID** , AHCI 

  * Disabled—P-SATA mode is disabled
  * LSI SW RAID—Sets both SATA and sSATA controllers to RAID mode for LSI SW RAID. 
  * AHCI—The controller enables the Advanced Host Controller Interface (AHCI) and disables RAID. 

|   
SATA Mode |  This options allows you to select the SATA mode. |  4.1(1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5 |  **AHCI** , LSISW RAID, Disabled 

  * Disabled—SATA mode is disabled
  * LSI SW RAID—Sets both SATA and sSATA controllers to RAID mode for LSI SW RAID
  * AHCI—The controller enables the Advanced Host Controller Interface (AHCI) and disables RAID. 

|   
VMD Enablement |  Whether NVMe SSDs that are connected to the PCIe bus can be hot swapped. It also standardizes the LED status light on these drives. LED status lights can be optionally programmed to display specific Failure indicator patterns.  |  4.1(1) and later |  C220 M5, C240 M5, C480 M5, B200 M5, B480 M5,B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8  |  **Disabled** , Enabled 

  * Disabled—Hot swap of NVMe SSDs that are connected to the PCIe bus is not allowed.
  * Enabled—Hot swap of NVMe SSDs that are connected to the PCIe bus is allowed.

|  |  **Note** |  Not applicable for XE1X0M8.  
---|---

---

## Page 5: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-intel-directed-io.html

## Intel Directed IO  
  
The following table lists the Intel directed IO BIOS settings that you can configure through a BIOS policy or the default BIOS settings: 

Name |  Description |  Supported Attributes  
---|---|---  
|  Versions |  Platforms |  Values |  Dependencies  
Intel VT for directed IO |  Whether the processor uses Intel Virtualization Technology for Directed I/O (VT-d).  |  4.1(1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7  |  **Enabled** , Disabled 

  * **Disabled** —The processor does not use virtualization technology. 
  * **Enabled** —The processor uses virtualization technology. 

|   
**Intel(R) VT-d Coherency Support** |  Whether the processor supports Intel VT-d Coherency.  |  4.1(1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7  |  Enabled, **Disabled**

  * **Disabled** —The processor does not support coherency. 
  * **Enabled** —The processor uses VT-d Coherency as required. 

|  |  **Note** |  This is not applicable to XE1X0M8.  
---|---  
Intel VTD ATS Support |  Whether the processor supports Intel VT-d Address Translation Services (ATS).  |  4.1(1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6 |  Disabled,**Enabled**

  * **Disabled** —The processor does not support ATS. 
  * **Enabled** —The processor uses VT-d ATS as required. 

|   
PreBoot DMA Protection | The BIOS setting that aims to prevent unauthorized Direct Memory Access (DMA) during the boot process, potentially protecting against malicious devices from gaining access to system memory.  |  4.3(6a) and later |  C220 M8, C240M8, X210c M8, X410c M8, XE1X0M8 |  Disabled,**Enabled**

  * Disabled——Options are Disabled. 
  * Enabled——Options are Enabled. 

| 

---

## Page 6: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-lom-and-pcie-slots.html

## LOM and PCIe Slots  
  
The following table lists the LOM and PCIe BIOS settings that you can configure through a BIOS policy or the default BIOS settings: 

Name |  Description |  Supported Attributes  
---|---|---  
Versions |  Platforms |  Values |  Dependencies  
ACS Control GPU n where _n_ varies from 1-14  |  Access Control Services (ACS) allow the processor to enable or disable peer-to-peer communication between multiple devices for GPUs.  |  4.0(4) and later |  C480 M5 |  Enabled, **Disabled**

  * **Disabled** Disables peer-to-peer communication between multiple devices for GPUs. 
  * **Enabled** Enables peer-to-peer communication between multiple devices for GPUs. 

|   
**CDN Support for LOM** |  Whether the Ethernet Networking Identifier naming convention is according to Consistent Device Naming (CDN) or the traditional way of naming conventions.  |  4.0(4) and later |  C480 M5, B200 M6, X210 M6 |  Enabled, **Disabled**

  * **Disabled** OS Ethernet Networking Identifier is named in a default convention as ETH0, ETH1 and so on. 
  * **Enabled** OS Ethernet Network Identifier is named in a consistent device naming (CDN) convention according to the physical LAN on Motherboard (LOM) port numbering; LOM Port 0, LOM Port 1 and so on. 

|  |  **Note** |  Not applicable for XE1X0M8.  
---|---  
External SSC Enable |  This option allows you to Enable/Disable the Clock Spread Spectrum of the external clock generators. |  4.1(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8  |  **Enabled** , Disabled, 0P3_Percent, 0P5_Percent, Hardware, Off  |  **Note** |  0P3_Percent, 0P5_Percent, Hardware, Off options are available for M7 servers only.  
---|---  
IIO eDPC Support |  This option allows a downstream link to be disabled after an uncorrectable error, making recovery possible in a controlled and robust manner.  |  4.2(1) and later |  C220 M6, C240 M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, C245 M8, C225 M8, X215c M8, XE1X0M8 |  Disabled, On fatal error, **On fatal and non-fatal error** |   
LOM Port n OptionROM, where _n_ ranges from 0-3.  |  Whether Option ROM is available on the LOM port _n_ |  4.0(4) and later |  C220 M5, C240 M5, C480 M5,C220 M6, C240 M6 |  Disabled, **Enabled,** Legacy only, UEFI only 

  * **Disabled** —The expansion slot is not available. 
  * **Enabled** —The expansion slot is available. 
  * **UEFI only** —The expansion slot is available only for UEFI. 
  * **Legacy only** —The expansion slot is available only for legacy. 

|   
PCIe ARI Support |  Whether all ARI support ports are enabled or disabled. |  4.2(1) and later |  C125 M5, C225 M6, C245 M6, C225 M8, C245 M8, X215c M8 |  Disabled, **Enabled** , Auto 

  * **Disabled** —This option is Disabled. 
  * **Enabled** —This options is enabled. 
  * **Auto** —PCIe ARI Support is in auto mode. 

|   
PCIe PLL SSC Percent |  Whether all PCIe PLL SSC ports are enabled or disabled. |  4.1(2) and later |  C220 M7, C240 M7, X210c M7, X410c M7 |  0–255 (Unit is (n/10)%)  |  |  **Note** |  This is not applicable to XE1X0M8.  
---|---  
MRAIDn Link Speed where n ranges from 1-2.  |  This option allows you to restrict the maximum speed of MRAID.  |  4.0(2) and later |  C220 M5, C240 M5, C220 M6, C225 M6, C220 M7, C240 M8 |  **Auto** , Disabled, Gen 1, Gen 2, Gen 3, Gen 4, Gen 5 

  * **Disabled** —The maximum speed is not restricted. 
  * **Enabled** —The maximum speed is restricted. 
  * **Auto** —The maximum speed is set automatically. 
  * **Gen 1** —2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * **Gen 2** —5GT/s is the maximum speed allowed. 
  * **Gen 3** —8GT/s is the maximum speed allowed. 
  * **Gen 4** —16GT/s is the maximum speed allowed.  |  **Note** |  Applicable for M7, M8 servers only.  
---|---  
  * **Gen 5** —32GT/s is the maximum speed allowed. 

**Note** |  Applicable for M7, M8 servers only.  
---|---  

  
MRAID n OptionROM  where n ranges from 1-2.  |  Whether Option ROM is available on the MRAID port.  |  4.0(2) and later |  C220 M5, C240 M5, C220 M6, C225 M6, C220 M7, C225 M8, C240 M8 |  Disabled,**Enabled**

  * **Disabled** —The expansion slot is not available. 
  * **Enabled** —The expansion slot is available. . 

|   
PCIe Slot MSTOR Link Speed |  This option allows you to restrict the maximum speed of an MSTOR adapter. |  4.2(1) and later |  C225 M6, C245 M6. C245 M8, C225 M8, XE1X0M8 |  **Auto** , Disabled, Gen 1, Gen 2, Gen 3, Gen 4, Gen 5 

  * **Disabled** —The maximum speed is not restricted. 
  * **Auto** —The maximum speed is set automatically. 
  * **Gen 1** —2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * **Gen 2** —5GT/s is the maximum speed allowed. 
  * **Gen 3** —8GT/s is the maximum speed allowed. 
  * **Gen 4** —16GT/s is the maximum speed allowed. 
  * **Gen 5** —32GT/s is the maximum speed allowed.  |  **Note** |  Applicable for M8 servers only.  
---|---  

  
PCIe Slot MSTOR RAID OptionROM |  Whether the server can use the Option ROMs present in the PCIe MSTOR RAID. |  4.2(1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5,C125 M5, C220 M6, C240 M6, C225 M6, C245 M6, C220 M7, C240 M7, C225 M8, C245 M8, C220 M8, C240 M8, XE1X0M8  |  Disabled, **Enabled**

  * **Disabled** —Option ROM is not available. 
  * **Enabled** —Option ROM is available. 

|   
NVME n Link Speed where _n_ ranges from 0-6 and 13-24.  |  This option allows you to restrict the maximum speed of an NVME card installed in the PCIe slot. |  4.0(2) and later |  C240 M5, C225 M8, C245 M8  |  **Note** |  NVME 24 Link Speed supports C220 M7 and C240 M7 servers, and X210c M7 server.   
---|---  
Disabled, **Auto** , GEN1, GEN2, GEN3, GEN4, GEN5 

  * **Disabled** —Maximum speed is not restricted. 
  * **Auto** —The maximum speed is set automatically. 
  * **Gen 1** —2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * **Gen 2** —5GT/s is the maximum speed allowed 
  * **Gen 3** —8GT/s is the maximum speed allowed 
  * **Gen 4** —16GT/s is the maximum speed allowed 
  * **Gen 5** —32GT/s is the maximum speed allowed 

|   
NVME n OptionROM where _n_ ranges from 0-6.  |  This options allows you to control the Option ROM execution of the PCIe adapter connected to the SSD:NVMe slot n. |  4.0(2) and later |  C220 M5, C240 M5, C225 M6, C245 M6 |  Enabled, Disabled

  * **Disabled** —Option is not restricted. 
  * **Enabled** —Option is restricted. 

|   
PCIe Slot n Link Speed where _n_ ranges from 1 to 8 .  |  **Note** |  For C245 M8 platform, _n_ ranges from 1 to 8.   
---|---  
Link speed for PCIe Slot designated by slot n. |  4.0(1) and later |  C220 M5, C240 M5, C480 M5, C125 M5, C220 M6, C240 M6, C225 M6, C245 M6, C220 M7, C240 M7 (Slots 4–8), C225 M8, C245 M8, C220 M8(1-3), C240 M8(1-8), XE1X0M8 (n ranges 1 to 3)  |  Disabled, **Auto** , GEN1, GEN2, GEN3, GEN4, GEN5  GEN5 is supported only for speeds 1 to 6.

  * **Disabled** —Maximum speed is not restricted. 
  * **Auto** —The maximum speed is set automatically. 
  * **Gen 1** —2GT/s (gigatransfers per second) is the maximum speed allowed. 
  * **Gen 2** —5GT/s is the maximum speed allowed 
  * **Gen 3** —8GT/s is the maximum speed allowed 
  * **Gen 4** —16GT/s is the maximum speed allowed 
  * **Gen 5** —32 GT/s is the maximum speed allowed 

|   
PCIe Slot nOptionROM , where n ranges from 1 to 8  |  Whether Option ROM is available on the port. |  4.0(2) and later |  C220 M5, C240 M5, C480 M5, C125 M5, C220 M6, C240 M6, C220 M7, C240 M7 (Slots 4–8), C245 M8, C220 M8 (Slots 1 to 3), C240 M8 (Slots 1-8), XE1X0M8 (n ranges 1 to 3)  |  Disabled, **Enabled** , Legacy only, UEFI only 

  * **Disabled** —The expansion slot is not available. 
  * **Enabled** —The expansion slot is available. 

|   
PCIe Slot:LOM Link Speed |  To configure link speed for PCIe Slot:LOM. |  4.0 (1) and later |  C220 M5, C240 M5, C220 M6, C240 M6, C225 M6, C245 M6 |  Disabled, **Auto** , GEN1, GEN2, GEN3 

  * **Disabled** —Maximum speed is not restricted. 
  * **Auto** —The maximum speed is set automatically. 
  * **Gen 1** —2GT/s (gigatransfers per second) is the maximum speed allowed. 
  * **Gen 2** —5GT/s is the maximum speed allowed 
  * **Gen 3** —8GT/s is the maximum speed allowed 

|   
Front NVME n Link Speed where _n_ ranges from 1 to 12. For C245 M8 platform, _n_ ranges from 1 to 4.  |  This option allows you to restrict the maximum speed of an NVME card installed in the front PCIe slot. |  4.0(4) and later |  C220 M5, C240 M5, C225 M6, C245 M6, C220 M7, C240 M7 (Slots 11–24), C225 M8, C245 M8, C220 M8 (slots 1-16), C240 M8 (slots 1-32), XE1X0M8. (n ranges from 1 to 4)  |  Disabled, **Auto** , GEN1, GEN2, GEN3, GEN4, GEN5 

  * **Disabled** —Maximum speed is not restricted. 
  * **Auto** —The maximum speed is set automatically. 
  * **Gen 1** —2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * **Gen 2** —5GT/s is the maximum speed allowed 
  * **Gen 3** —8GT/s is the maximum speed allowed 
  * **Gen 4** —16GT/s is the maximum speed allowed 
  * **Gen 5** —32GT/s is the maximum speed allowed 

|  |  **Note** |  For UCSC-C225-M8N SKU, the front NVMe drive slots (1-10) do not support Gen5 speeds. The Front NVMe Link Speed tokens for these slots cannot be set to **Gen5**. If you attempt to set these tokens to **Gen5** , the system will automatically revert to the default state **Auto**.   
---|---  
Front NVME n OptionROM where _n_ ranges from 1 to 24. For C245 M8 platform, _n_ ranges from 1 to 4.  |  This options allows you to control the Option ROM execution of the PCIe adapter connected to the SSD:NVMe slot n. |  4.2(1) and later |  C225 M6, C245 M6, C220 M7, C240 M7(Slots 11–24), C245 M8, C220 M8 (slots 1-16), C240 M8 (slots 1 - 32), XE1X0M8. (n ranges from 1 to 4)  |  **Enabled** , Disabled 

  * **Disabled** —Option is not restricted. 
  * **Enabled** —Option is restricted. 

|   
PCIe LOM:1 and 2 Link |  This option allows you to restrict the maximum speed of an adapter card installed in PCIe slot 1 and 2. |  4.0 (1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5 |  Enabled, Disabled

  * **Disabled** —Option is not restricted. 
  * **Enabled** —Option is restricted. 

|   
Slot Mezz State |  This option allows you to configure the Mezz state for PCIe slot. |  4.0 (1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5 |  Disabled, **Enabled** , Legacy only, UEFI only 

  * **Disabled** —The expansion slot is not available. 
  * **Enabled** —The expansion slot is available. 
  * **UEFI only** —The expansion slot is available only for UEFI. 
  * **Legacy only** —The expansion slot is available only for legacy. 

|   
PCIe Slot:MLOM Link Speed |  This option allows you to restrict the maximum speed of an MLOM adapter. |  4.0 (1) and later |  C220 M5, C240 M5, C220 M6, C240 M6, C225 M6, C245 M6, C220 M7, C240 M7, C225 M8, C245 M8, C220 M8, C240 M8 |  **Auto** , Disabled, Gen 1, Gen 2, Gen 3, Gen 4, Gen 5 

  * **Disabled** —The maximum speed is not restricted. 
  * **Auto** —The maximum speed is set automatically. 
  * **Gen 1** —2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * **Gen 2** —5GT/s is the maximum speed allowed. 
  * **Gen 3** —8GT/s is the maximum speed allowed. 
  * **Gen 4** —16GT/s is the maximum speed allowed. 
  * **Gen 5** —32GT/s is the maximum speed allowed. 

|   
PCIe Slot:MLOM OptionROM |  Whether Option ROM is available on the MLOM port. |  4.0 (1) and later |  C220 M5, C240 M5, C220 M6, C240 M6, C225 M6, C245 M6, C220 M7, C240 M7, C225 M8, C245 M8, C220 M8, C240 M8 |  Disabled, **Enabled** , Legacy only, UEFI only 

  * **Disabled** —The expansion slot is not available. 
  * **Enabled** —The expansion slot is available. 
  * **UEFI only** —The expansion slot is available only for UEFI. 
  * **Legacy only** —The expansion slot is available only for legacy. 

|   
MRAID Link Speed |  This option allows you to restrict the maximum speed of MRAID.  |  4.0(2) and later |  C220 M5, C240 M5, C220 M6, C225 M6, C220 M7, C225 M8, C220 M8 |  **Auto** , Disabled, Gen 1, Gen 2, Gen 3, Gen 4, Gen 5 

  * **Disabled** —The maximum speed is not restricted. 
  * **Auto** —The maximum speed is set automatically. 
  * **Gen 1** —2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * **Gen 2** —5GT/s is the maximum speed allowed. 
  * **Gen 3** —8GT/s is the maximum speed allowed. 
  * **Gen 4** —16GT/s is the maximum speed allowed. 
  * **Gen 5** —32GT/s is the maximum speed allowed. 

|   
PCIe Slot:MRAID OptionROM |  Whether Option ROM is available on the MLOM port. |  4.0(2) and later |  C220 M5, C240 M5, C220 M6, C225 M6, C220 M7, C220 M8 |  Disabled, **Enabled** , Legacy only, UEFI only 

  * **Disabled** —The expansion slot is not available. 
  * **Enabled** —The expansion slot is available. 

|   
RAID Link Speed |  This option allows you to restrict the maximum speed of RAID.  |  4.0 (1) and later |  C480 M5 |  Disabled, **Auto** , GEN1, GEN2, GEN3 

  * **Disabled** —Maximum speed is not restricted. 
  * **Auto** —The maximum speed is set automatically. 
  * **Gen 1** —2GT/s (gigatransfers per second) is the maximum speed allowed. 
  * **Gen 2** —5GT/s is the maximum speed allowed 
  * **Gen 3** —8GT/s is the maximum speed allowed 

|   
PCIe Slot RAID OptionROM |  Whether Option ROM is available on the RAID slot or not. |  4.0 (1) and later |  C480 M5 |  **Enabled** , Disabled 

  * **Disabled** —Option is not restricted. 
  * **Enabled** —Option is restricted. 

|   
Rear NVME n Link Speed, where n ranges from 1 to 4.  |  This option allows you to restrict the maximum speed of rear NVME.  |  4.0(4) and later |  C240 M5, C240 M6, C245 M6, C220 M7, C240 M7, C245 M8, C240 M8 |  **Note** |  NVME 4 Link Speed supports C240 M7 servers, X210c M7, and C240 M8 server.   
---|---  
**Auto** , Disabled, Gen 1, Gen 2, Gen 3, Gen 4, Gen 5 

  * **Disabled** —The maximum speed is not restricted. 
  * **Auto** —The maximum speed is set automatically. 
  * **Gen 1** —2.5GT/s (gigatransfers per second) is the maximum speed allowed. 
  * **Gen 2** —5GT/s is the maximum speed allowed. 
  * **Gen 3** —8GT/s is the maximum speed allowed. 
  * **Gen 4** —16GT/s is the maximum speed allowed. 
  * **Gen 5** —32GT/s is the maximum speed allowed. 

|   
Rear NVME n OptionROM, where n ranges from 1 to 4.  |  Whether Option ROM is available on the rear NVME or not. |  4.0(4) and later |  C240 M5, C480 M5, C240 M6, C245 M6, C220 M7, C240 M7, C245 M8, C240 M8 |  **Enabled** , Disabled 

  * **Disabled** —Option is not restricted. 
  * **Enabled** —Option is restricted. 

|   
PCIe Slot:Riser Link Speedn, where n is 1 and 2.  |  This option allows you to restrict the maximum speed of Riser. |  4.0(4) and later |  C240 M5, C480 M5, C240 M6  |  Disabled, **Auto** , GEN1, GEN2, GEN3 

  * **Disabled** —Maximum speed is not restricted. 
  * **Auto** —The maximum speed is set automatically. 
  * **Gen 1** —2GT/s (gigatransfers per second) is the maximum speed allowed. 
  * **Gen 2** —5GT/s is the maximum speed allowed 
  * **Gen 3** —8GT/s is the maximum speed allowed 

|   
PCIe Slot:Riser nSlotx Link Speed, where _n_ is 1 and 2 and _x_ is from 1 to 6.  |  This option allows you to restrict the maximum speed of Riser in the _x_ slot .  |  4.0(2) and later |  C220 M5, C240 M5, C480 M5, C125 M5 |  Disabled, **Auto** , GEN1, GEN2, GEN3 

  * **Disabled** —Maximum speed is not restricted. 
  * **Auto** —The maximum speed is set automatically. 
  * **Gen 1** —2GT/s (gigatransfers per second) is the maximum speed allowed. 
  * **Gen 2** —5GT/s is the maximum speed allowed 
  * **Gen 3** —8GT/s is the maximum speed allowed 

|   
PCIe Slot:SAS OptionROM |  Whether Option ROM is available on SAS slot or not. |  4.0(2) and later |  C220 M5, C240 M5, C480 M5, C125 M5 |  Disabled, **Enabled** , Legacy only, UEFI only 

  * **Disabled** —The expansion slot is not available. 
  * **Enabled** —The expansion slot is available. 
  * **UEFI only** —The expansion slot is available only for UEFI. 
  * **Legacy only** —The expansion slot is available only for legacy. 

|   
PCIe Slot:FrontSSD nLink Speed, where _n_ is 1 and 2.  |  This option allows you to restrict the maximum speed of Front SSD. |  4.0(2) and later |  C220 M5, C240 M5, C480 M5, S3260 M5, C125 M5, C220 M6, C240 M6, C225 M6, C245 M6, C220 M7, C240 M7, C225 M8, C245 M8 |  Disabled, **Auto** , GEN1, GEN2, GEN3 

  * **Disabled** —Maximum speed is not restricted. 
  * **Auto** —The maximum speed is set automatically. 
  * **Gen 1** —2GT/s (gigatransfers per second) is the maximum speed allowed. 
  * **Gen 2** —5GT/s is the maximum speed allowed 
  * **Gen 3** —8GT/s is the maximum speed allowed 

|   
Single Root I/O Virtualization (SR-IOV) Support | Controls the Single Root I/O Virtualization. SR-IOV allows a device, such as a network adapter, to separate access to its resources among various PCIe hardware functions.  |  4.3(4b) and later |  C125 M5, C225 M6, C245 M6, C225 M8, C245 M8, X215c M8 |  **Enabled** , Disabled  |   
Re-Size BAR Support |  Allows to enable or disable Re-sizable BAR support setup item.  |  4.3(4b) and later |  C220 M7, C240 M7, X210 M7, X410 M7, C225 M8, C245 M8, X215c M8, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8 |  Enabled, **Disabled** |  **Note** |  By default it is **Enabled** for AMD platforms and **Disabled** for Intel platforms.   
---|---

---

## Page 7: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-main.html

## Main  
  
The following table lists the main BIOS settings that you can configure through a BIOS policy or the default BIOS settings:

Name |  Description |  Supported Attributes  
---|---|---  
Versions |  Platforms |  Values |  Dependencies  
PCIe Slots CDN Control where, CDN refers to Consistent Device Naming  |  PCIe Slots Consistent Device Naming (CDN) control allows PCIe slots to be named in a consistent manner. This makes PCIe slot names more uniform, easy to identify, and persistent when the configuration changes are made.  |  4.0(2) and later | C240 M5, C220 M6, C240 M6, C225 M6, C245 M6, C220 M7, C240 M7, C225 M8, C245 M8, X215c M8, C220 M8, C240 M8, XE1X0M8 |  Enabled, **Disabled**

  * **Disabled** —Option is not restricted. 
  * **Enabled** —Option is restricted. 

|  Consistent Device Naming is same as CDN Control in the UCSM Manager.  
Consistent Device Naming (CDN) Control |  PCIe Slots Consistent Device Naming (CDN) control allows PCIe slots to be named in a consistent manner. This makes PCIe slot names more uniform, easy to identify, and persistent when the configuration changes are made.  |  4.0(2) and later  | B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, C125 M5, S3260 M5, B200 M6, C220 M6, C240 M6, C225 M6, C245 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C225 M8, C245 M8, X215c M8, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  **Enabled** , Disabled 

  * **Disabled** —Option is not restricted. 
  * **Enabled** —Option is restricted. 

|  Consistent Device Naming is same as CDN Control in the UCSM Manager.

---

## Page 8: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-memory.html

## Memory  
  
The following table lists the memory BIOS settings that you can configure through a BIOS policy or the default BIOS settings:

Name |  Description |  Supported Attributes  
---|---|---  
Versions |  Platforms |  Values |  Dependencies  
ACPI SRAT Special Purpose Memory Flag |  Enables or disables the ACPI SRAT SP Memory flag when the UEFI Memory Map Special Purpose Flag is enabled. |  4.3(5b) and later |  C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8 |  Disabled, Enabled

  * **Disabled** —Options are Disabled. 
  * **Enabled** —Options are enabled. 

|  It is recommended to leave this setting in the default state of Enabled.  
UEFI Memory Map Special Purpose Memory Flag |  Changing the UEFI Memory Map Special knob settings impacts CXL cards on certain operating systems. |  4.3(5b) and later |  C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8 |  Disabled, Enabled

  * **Disabled** —Options are Disabled. 
  * **Enabled** —Options are enabled. 

|  It is recommended to leave this setting in the default state of Enabled.  
Enhanced Memory Test | Enables enhanced memory tests during the system boot and increases the boot time based on the memory. |  4.0 (1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6,C220 M7, C240 M7, X210c M7, X410c M7, C225 M8, C245 M8, X215 M8, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  Disabled, Enabled, **Auto**

  * **Disabled** —Options are Disabled. 
  * **Enabled** —Options are enabled. 
  * **Auto** —Option is in auto mode. 

|  It is recommended to leave this setting in the default state of Auto.  
BME DMA Mitigation |  Allows you to disable the PCI BME bit to mitigate the threat from an unauthorized external DMA |  4.0 (1), 4.0(2), 4.0(4), 4.1(1), 4.2(1), 4.3(4b). 4.3(5a) |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5,B200 M6, C220 M6, C240 M6, X210c M6,C225 M6, C245 M6,C220 M7, C240 M7, X210c M7, X410c M7, C225 M8, C245 M8, X215c M8, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  Enabled, **Disabled**

  * Disabled—Option is not restricted.
  * Enabled—Option is restricted.

|   
Burst and Postponed Refresh |  Allows the memory controller to defer the refresh cycles when the memory is active and accomplishes the refresh within a specified window. The deferred refresh cycles may run in a burst of several refresh cycles.  |  4.0 (1) and later |  C225 M6, C245 M6, C245 M8, C225 M8, X215c M8 |  Enabled, **Disabled**

  * Disabled—Option is not restricted.
  * Enabled—Option is restricted.

|   
CPU SMEE |  Whether the processor uses the Secure Memory Encryption Enable (SMEE) function, which provides memory encryption support. |  4.0(2) and later |  C125 M5, C225 M6, C245 M6, C225 M8, C245 M8, X215c M8 |  Disabled, **Enabled** , Auto 

  * Disabled—Options are Disabled.
  * Enabled—Options are enabled.
  * **Auto** —Option is in auto mode. 

|   
IOMMU |  Input Output Memory Management Unit(IOMMU) allows AMD processors to map virtual addresses to physical addresses. |  4.0(2) and later |  C125 M5, C225 M6, C245 M6, C225 M8, C245 M8 X215c M8 |  Disabled, Enabled, **Auto**

  * Disabled—Options are Disabled.
  * Enabled—Options are enabled.
  * Auto—Option is in auto mode.

|  **Note** |  To disable IOMMU, the system must be configured with Local APIC Mode set to xAPIC.   
---|---  
Bank Group Swap |  Determines how physical addresses are assigned to applications. |  4.0 (1) and later |  C125 M5, C225 M6, C245 M6, C245 M8, C225 M8, X215c M8  |  Disabled, Enabled, **Auto**

  * Disabled—Options are Disabled.
  * Enabled—Options are enabled.
  * Auto—Option is in auto mode.

|   
Chipset Interleave |  Whether memory blocks across the DRAM chip selects for node 0 are interleaved. |  4.2(1) and later |  C125 M5, C225 M6, C245 M6, C245 M8, C225 M8, X215c M8  |  Disabled, Enabled, **Auto**

  * Disabled—Options are Disabled.
  * Enabled—Options are enabled.
  * Auto—Option is in auto mode.

|  **Note** |  Enabled option is available for M8 servers only.  
---|---  
DRAM Scrub Time |  The value that represents the number of hours to scrub the whole memory. |  4.3(4a) and later |  C245 M6, C225 M6, C245 M8, C225 M8, X215c M8 |  Disabled, 1 hour, 4 hours, 6 hours, 8 hours, 12 hours, 16 hours, **24 hours** , 48 hours, Auto  |  **Note** |  12 hours option is available for M8 servers only.  
---|---  
SNP Memory Coverage |  This option selects the operating mode of the Secured Nested Paging (SNP) Memory and the reverse Map Table (RMP). The RMP is used to ensure a one-to-one mapping between system physical addresses and guest physical addresses.  |  4.2(1) and later |  C225 M6, C245 M6, C245 M8, C225 M8, X215c M8  |  Disabled, Enabled, **Auto** , Custom 

  * Disabled—Options are Disabled.
  * Enabled—Options are enabled.
  * Auto—Option is in auto mode.
  * Custom—Options are customized.

|   
SNP Memory Size to Cover in MiB |  Allows you to configure SNP memory size. | 4.2(1), 4.3(4b), 4.3(5a) | C225 M6, C245 M6, C225 M8, C245 M8, X215c M8 | 0 - 1048576, with 8192 as the default. |   
MMIO High Granularity Size |  Selects the allocation size that is used to assign memory-mapped I/O (MMIO) resources. |  4.3(3c) and later |  X410c M7, X210c M7, C220 M7, C240 M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8 |  1G, 4G, 16G, 32G, 64G, **256G** , 1024G, Auto  |  **Note** |  Auto and 32G option is applicable to M8 intel platforms only. For XE1X0M8, the default value is 1024G.  
---|---  
MMIO High Base |  The base memory size according to memory-address mapping for the I/O (MMIO resources) |  4.3(3c) and later |  X410c M7, X210c M7, C220 M7, C240 M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8 |  512G, 1T, 2T, 4T, 16T, 24T, 30T, **32T** , 40T, 56T, 60T, Auto 

  * Auto option is applicable for M8 intel platforms only.
  * 30T and 60T options are supported for XE1X0M8 only.

|   
NUMA Nodes per Socket |  Allows you to configure the number of NUMA (Non-Uniform Memory Access) nodes per CPU socket. |  4.2(1) and later |  C225 M6, C245 M6, C225 M8, C245 M8, X215c M8  |  **Auto** , NPS0, NPS1, NPS2, NPS4 

  * NPS0—Zero NUMA node per socket.
  * NPS1—One NUMA node per socket.
  * NPS2—Two NUMA nodes per socket.
  * NPS4—Four NUMA nodes per socket.
  * Auto—Number of channels are set to auto.

|   
Memory Interleaving |  Determines the memory blocks to be interleaved. It also determines the starting address of the interleave (bit 8, 9, 10 or 11).  |  4.0(2) and later |  C125 M5, C225 M6, C245 M6, C225 M8, C245 M8, X215c M8  |  **Auto** , Channel, Die, none, Socket, Disabled, Enabled 

  * Avaialble options for M5:**Auto** , Channel, Die, none, Socket 
  * Avaialble options for M6:**Auto** , Disabled 
  * Avaialble options for M8:**Auto** , Enabled, Disabled 

|   
Memory Interleaving Size |  Determines the size of the memory blocks to be interleaved. It also determines the starting address of the interleave (bit 8, 9, 10 or 11).  |  4.0(2) and later |  C125 M5, C225 M6, C245 M6  |  1 KB, 2 KB, 4KB, 256 Bytes, 512 Bytes, **Auto** |  **Note** |  4KB option is available for M6 server only.  
---|---  
SEV-SNP Support |  Allows you to enable the Secure Nested Paging feature. |  4.2(1) and later |  C225 M6, C245 M6, C225 M8, C245 M8, X215c M8 |  Disabled, Enabled, **Auto**

  * Disabled—Options are Disabled.
  * Enabled—Options are enabled.

|   
CR QoS |  Prevents DRAM and overall system BW drop in the presence of concurrent DCPMM BW saturating threads, with minimal impact to homogenous DDRT-only usages, Good for multi-tenant use cases, VMs, and so on. Targeted for App Direct, but also improves memory mode. Targets the “worst-case” degradations.  |  4.1(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6  |  **Disabled** , Recipe 1, Recipe 2, Recipe 3, Mode 0, Mode 1, Mode 2 

  * Disabled—Feature disabled.
  * Recipe 1—6 modules, 4 modules per socket optimized 
  * Recipe 2—2 modules per socket optimized
  * Recipe 3—1 module per socket optimized
  * Mode 0 - Disable the PMem QoS Feature
  * Mode 1 - M2M QoS Enable;CHA QoS Disable
  * Mode 2 - M2M QoS Enable; CHA QoS Enable

|  **Note** |  Mode 0, Mode 1, Mode 2 options are applicable for M6 servers only.  
---|---  
CR FastGo Config |  CR FastGo Config improves DDRT non-temporal write bandwidth when FastGO is disabled. When FastGO is enabled, it gives a faster flow of NT writes into the uncore, When FastGO is disabled, it lessens NT writes queueing up in the CPU uncore, thereby improving sequentially at DCPMM, resulting in improved bandwidth.  |  4.1(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6 |  **Auto** , Option 1—5, Enable Optimization, Disable Optimization  |  **Note** |  Enable Optimization, Disable Optimization options are available for M6 servers only.  
---|---  
DCPMM Firmware Downgrade | To configure DCPMM Firmware Downgrade. |  4.0 (1) and later |  B480 M5, C220 M5, C240 M5, C480 M5,S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6 |  **Disabled** , Enabled 

  * Disabled—Options are Disabled.
  * Enabled—Options are enabled.

|   
Memory Refresh Rate |  To configure the refresh interval rate for internal memory. |  4.0 (1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5,B200 M6, C220 M6, C240 M6, X210c M6, C225 M6, C245 M6, C220 M7, C240 M7, X210c M7, X410c M7, C225 M8, C245 M8, X215c M8  |  Auto, **1x Refresh** , 2x Refresh, 3x, 4x  |  **Note** |  1x Refresh is the default for M5, M7, M8 servers. 2x Refresh is the default for AMD M6 servers.  
---|---  
|  **Note** |  Not applicable for XE1X0M8.  
---|---  
DRAM SW Thermal Throttling |  To configure DRAM SW thermal throttling. |  4.0 (1) and later |  C125 M5 |  **Disabled** , Enabled 

  * Disabled—Options are Disabled.
  * Enabled—Options are enabled.

|   
eADR Support |  Extended asynchronous DRAM refresh (eADR) ensures that CPU caches lines with data are flushed at the right time and in the desired order and are also included in the power fail protected domain.  |  4.2(1) and later |  B200 M6, C220 M6, C240 M6, X210c M6,C220 M7, C240 M7, X210c M7, X410c M7  |  **Disabled** , Enabled, Auto 

  * Disabled—Options are Disabled.
  * Enabled—Options are enabled.
  * Auto—Option is in auto mode.

|   
Memory Bandwidth Boost |  Allows to boost the memory bandwidth. |  4.2(1) and later |  C220 M6, C240 M6, B200 M6, X210c M6  |  Disabled, **Enabled**

  * Disabled—Options are Disabled.
  * Enabled—Options are enabled.

|   
Memory Size Limit in GB |  Limits the capacity in Partial Memory Mirror Mode up to 50 percent of the total memory capacity. The memory size can range from 0 GB to 65535 GB in increments of 1 GB.  |  4.0(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  **0** \- 65535 with a step size of 1  |   
Memory Thermal Throttling Mode |  Provides a protective mechanism to ensure the memory temperature is within the limits. When the temperature exceeds the maximum threshold value, the memory access rate is reduced and Baseboard Management Controllerf (BMC) adjusts the fan to cool down the memory to avoid DIMM damage due to overheat  |  4.0 (1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, XE1X0M8  |  **CLTT with PECI** , Disabled 

  * Disabled—Options are Disabled.
  * CLTT with PECI—Closed Loop Thermal Throttling (CLTT) with Platform Environment Control Interface (PECI). 

|  This token is not supported on C125 M5 servers.  
NUMA Optimized |  Whether the BIOS supports NUMA.  |  4.0 (1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  **Enabled** , Disabled 

  * Disabled—The BIOS does not support NUMA.
  * Enabled—The BIOS includes the ACPI tables that are required for NUMA-aware operating systems. If you enable this option, the system must disable Inter-Socket Memory interleaving on some platforms. 

|   
NVM Performance Setting |  enables efficient major mode arbitration between DDR and DDRT transactions on the DDR channel to optimize channel BW and DRAM latency.  |  4.0(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6 |  **BW Optimized** , Latency Optimized, Balanced Profile 

  * BW Optimized—Optimized for DDR and DDRT BW. This is the default option.
  * Latency Optimized—Better DDR latency in the presence of DDRT BW. Available for M5 servers only.
  * Balanced Profile—Optimized for Memory mode.

|   
Operation Mode |  This option allows you to configure Operation Mode. |  4.2(1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5 |  **Test-Only** , Test and Repair  |   
Panic and High Watermark |  Controls the delayed refresh capability of the memory controller. |  4.2(1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7  |  High, **Low**

  * High—The memory controller is allowed to postpone up to a maximum of eight refresh commands. The memory controller executes all the postponed refreshes within the refresh interval. For the ninth refresh command, the refresh priority becomes Panic and the memory controller pauses the normal memory transactions until all the postponed refresh commands are executed. 
  * Low—The memory controller is not allowed to postpone refresh commands.  |  **Note** |  It is recommended to leave this setting in the default state (Low) which will help to reduce susceptibility to Rowhammer-style attacks.   
---|---  

It is recommended to leave this setting in the default state (**Low**) which will help to reduce susceptibility to Rowhammer-style attacks.  |  **Note** |  This is not applicable to XE1X0M8.  
---|---  
Partial Cache Line Sparing |  Partial cache line sparing (PCLS) is an error-prevention mechanism in memory controllers. PCLS statically encodes the locations of the faulty nibbles of bits into a sparing directory along with the corresponding data content for replacement during memory accesses.  |  4.2(1) and later |  B200 M6, C240 M6, C220 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7 |  Disabled, **Enabled** |  **Note** |  For M7 servers, Disabled is the default value.   
---|---  
  
  * Disabled—Options are Disabled.

  * Enabled—Options are enabled.


  
Partial Memory Mirror Mode |  enables you to partially mirror by GB or by a percentage of the memory capacity. Depending on the option selected here, you can define either a partial mirror percentage or a partial mirror capacity in GB in available fields. You can partially mirror up to 50 percent of the memory capacity.  |  4.1(1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8  |  **Disabled** , Percentage, Value in GB 

  * Disabled—Options are Disabled.
  * Percentage—The amount of memory to be mirrored in the Partial Memory Mode is defined as a percentage of the total memory.
  * Value in GB—The amount of memory to be mirrored in the Partial Memory Mode is defined in GB. |  **Note** |  Partial Memory Mirror Mode is mutually exclusive to standard Mirroring Mode. Partial Mirrors 1-4 can be used in any number or configuration, provided they do not exceed the capacity limit set in GB or Percentage in the related options.   
---|---  

**Note** |  Value in GB option is not applicable for M8 platforms.  
---|---  
Partial Mirror Percentage |  Limits the amount of available memory to be mirrored as a percentage of the total memory. This can range from 0.000.01 % to 50.00 % in increments of 0.01 %.  |  4.1(1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5,S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8 , X410c M8, XE1X0M8  |  **5.00** \- 40.00 with a step size of 0.01  |  |  **Note** |  Applicable only when partial mirror mode is set to a value in GB.   
---|---  
  
  * In Memory RAS Configuration, select Partial Mirror Mode 1LM

  * Partial Memory Mirror Mode configuration should be set to Percentage. 


  
Partial Mirrorn Size in GB, where _n_ ranges from 1 to 4.  |  Limits the amount of memory in Partial Mirror _n_ in GB. This can range from 0 GB to 65535 GB in increments of 1 GB.  |  4.1(1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7  |  **0** \- 65535 with a step size of 1  |  |  **Note** |  Applicable only when partial mirror mode is set to a value in GB.   
---|---  
  
When _n=2:_

  * In Memory RAS Configuration, select Partial Mirror Mode 1LM

  * Partial Memory Mirror Mode configuration should be set to Percentage. 


  
PCIe RAS Support | Whether the PCIe RAS port is enabled or disabled. |  4.0 (1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6,C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  Disabled, **Enabled**

  * Disabled—This option is Disabled.
  * Enabled—This option is enabled.

|   
Post Package Repair |  Post Package Repair (PPR) provides the ability to repair faulty memory cells by replacing them with spare cells. |  4.2(1) and later |  C225 M6, C245 M6, C225 M8, C245 M8, X215c M8 |  Disabled, **Hard PPR**

  * Disabled—This option is Disabled.
  * Hard PPR—This results in a permanent remapping of damaged storage cells.

|   
Runtime Post Package Repair |  Enables the soft post-package repairs of the corrected memory errors during OS runtime.  |  4.3(4b) and later |  C225 M8, C245 M8, X215c M8, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8 |  **Disabled** , Enabled  |   
Memory RAS Configuration |  How the memory reliability, availability, and serviceability (RAS) is configured for the server. |  4.0 (1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5,B200 M6, C220 M6, C240 M6, X210c M6,C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  Maximum Performance, Mirroring, Lockstep, Mirror Mode 1LM, Partial Mirror Mode 1LM, Sparing, **ADDDC Sparing**

  * Maximum Performance—Optimizes the system performance and disables all the advanced RAS features.
  * Mirroring—System reliability is optimized by using half the system memory as backup. This mode is used for UCS M4 and lower blade servers 
  * Lockstep—If the DIMM pairs in the server have an identical type, size, and organization and are populated across the SMI channels, you can enable lockstep mode to minimize memory access latency and provide better performance. Lockstep is enabled by default for B440 servers. 
  * Mirror Mode 1LM—Mirror Mode 1LM will set the entire 1LM memory in the system to be mirrored, consequently reducing the memory capacity by half. This mode is used for UCS M5 and M6 blade servers. 
  * Partial Mirror Mode 1LM—Partial Mirror Mode 1LM will set a part of the 1LM memory in the system to be mirrored, consequently reducing the memory capacity by half. This mode is used for UCS M5 and M6 blade servers. 
  * Sparing—System reliability is optimized by holding memory in reserve so that it can be used in case other DIMMs fail. This mode provides some memory redundancy, but does not provide as much redundancy as mirroring. 
  * ADDDC Sparing—System reliability is optimized by holding memory in reserve so that it can be used in case other DIMMs fail. This mode provides some memory redundancy, but does not provide as much redundancy as mirroring. 

|   
Select PPR Type |  Post Package Repair (PPR) provides the ability to repair faulty memory cells by replacing them with spare cells. |  4.1(1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6,C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  Disabled, **Hard PPR**

  * Disabled—Options are Disabled.
  * Hard PPR—This results in a permanent remapping of damaged storage cells.

|   
Secured Encrypted Virtualization |  Enables running encrypted virtual machines (VMs) in which the code and data of the VM are isolated. |  4.2(1) and later |  C125 M5, C225 M6, C245 M6, C225 M8, C245 M8, X215c M8 |  253 ASIDs, 509 ASIDs, **Auto**

  * 253 ASIDs
  * 509 ASIDs
  * Auto |  **Note** |  It is recommended to leave this setting in the default state of Auto to mitigate Rowhammer-style attacks.  
---|---  

  
SMEE |  Whether the processor uses the Secure Memory Encryption Enable (SMEE) function, which provides memory encryption support. |  4.0(4) and later |  C125 M5, C225 M6, C245 M6, C225 M8, C245 M8, X215c M8 |  Disabled, **Enabled** , Auto 

  * Disabled—This option is Disabled.
  * Enabled—This option is enabled.
  * Auto—This option is set to auto mode.

|  **Note** |  Auto is the default for M6 and M8 servers.  
---|---  
Snoopy Mode for 2LM |  Enables snoop-mode for DCPMM accesses while maintaining directory on all DRAM accesses. Snoops maintain cache coherence between sockets. Directory reduces snoops by keeping the remote node information locally (in memory). Directory lookups and updates add memory traffic  Directory is a good tradeoff for DRAM, but not necessarily for DCPMM. For non-NUMA workloads, when the feature is enabled, directory updates to DCPMM are eliminated, thereby helping DDRT bandwidth bound workloads. The directory is disabled for far memory accesses and instead snoops remote sockets to check for ownership. Directory is used only for DRAM (near memory).  |  4.0 (1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5,B200 M6, C220 M6, C240 M6, X210c M6 |  **Disabled** , Enabled 

  * Disabled—This option is Disabled.
  * Enabled—This option is enabled.

|   
Snoopy Mode for AD |  Enables snoop-mode for DCPMM accesses while maintaining directory on all DRAM accesses. Snoops maintain cache coherence between sockets. Directory reduces snoops by keeping the remote node information locally (in memory). Directory lookups and updates add memory traffic.  Directory is a good tradeoff for DRAM, but not necessarily for DCPMM. For non-NUMA workloads, when the feature is enabled, directory updates to DCPMM are eliminated, thereby helping DDRT bandwidth bound workloads. The directory is disabled for accesses to AD and instead snoops remote sockets to check for ownership. Directory is used only for DRAM accesses.  |  4.0 (1) and later |  AB200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5,B200 M6, C220 M6, C240 M6, X210c M6  |  **Disabled** , Enabled 

  * Disabled—This option is Disabled.
  * Enabled—This option is enabled.

|   
Transparent Secure Memory Encryption |  Provides transparent hardware memory encryption of all data stored on system memory.  |  4.1(3) and later |  C125 M5, C225 M6, C245 M6, C225 M8, C245 M8, X215c M8 |  Disabled, Enabled, **Auto**

  * Disabled—This option is Disabled.
  * Auto—This option is set to auto mode.

|   
UMA |  As the name implies, UMA based clustering is the suggested clustering mode when the processor is configured as Uniform Memory Access (UMA) node, i.e. SNC is disabled.  |  4.2(1) and later |  C220 M6, C240 M6, B200 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8 |  Disable-All-2All, **Hemisphere-2-clusters** , Quadrant-4-clusters  |  **Note** |  For M7 servers, the default value is Quadrant-4-clusters.   
---|---  
**Note** |  Quadrant-4-clusters option is not applicable for M8 platforms.  
---|---  
Volatile Memory Mode |  Allows the memory mode configuration. |  4.0(2) and later |  C220 M6, C240 M6, B200 M6, X210c M6  |  1LM, **2LM**

  * 1LM—Configures 1 Layer Memory(1LM).This is the default value for M7 servers.
  * 2LM—Configures 2 Layer Memory(1LM).

|   
Error Check Scrub |  Allows you to enable a memory device to perform memory checking, correction and count errors. |  4.0(2) and later |  C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8 |  Disabled, Enabled with result collection, Enabled without result collection  |   
Rank Margin Tool |  Allows automated memory margin testing and is used to identify DDR margins at the rank level. |  4.0(2) and later |  C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8 |  Enabled, Disabled |   
Adaptive Refresh Management Level |  Selects Adaptive Refresh Management (ARFM) Level when refresh management (RFM) is required. |  4.0(2) and later |  C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8,XE1X0M8  | **Default** , Level A, Level B, Level C  | 

---

## Page 9: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-pci.html

## PCI  
  
The following table lists the PCI BIOS settings that you can configure through a BIOS policy or the default BIOS settings:

Name |  Description |  Supported Attributes  
---|---|---  
Versions |  Platforms |  Values |  Dependencies  
Memory Mapped IO above 4GB |  Whether to enable or disable memory mapped I/O of 64-bitPCI devices to 4GB or greater address space. Legacy option ROMs are not able to access addresses above 4GB. PCI devices that are 64-bit compliant but use a legacy option ROM may not function correctly with this setting enabled.  |  4.0 (1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, C125 M5, B200 M6, C220 M6, C240 M6, C225 M6, C245 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C225 M8, C245 M8, X215c M8, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  Disabled, **Enabled**

  * **Disabled** —This option is Disabled. 
  * **Enable** —This options is enabled. 

|   
VGA Priority |  Allows you to set the priority for VGA graphics devices if multiple VGA devices are found in the system. |  4.0(2) and later |  C220 M5, C240 M5, C220 M6, C240 M6, C220 M7, C240 M7, C225 M8, C245 M8, C220 M8, C240 M8 |  Offboard, **Onboard** , Onboard VGA Disabled 

  * **Onboard** —Priority is given to the onboard VGA device. BIOS post screen and OS boot are driven through the onboard VGA port 
  * **Offboard** ——Priority is given to thePCIE Graphics adapter. BIOS post screen and OS boot are driven through the external graphics adapter port. 
  * **Onboard VGA Disabled** —Priority is given to the PCIE Graphics adapter, and the onboard VGA device is disabled  |  **Note** |  The vKVM does not function when the onboard VGA is disabled.  
---|---  

|  **Note** |  This is not applicable to XE1X0M8.  
---|---

---

## Page 10: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-power-and-performance.html

## Power and Performance  
  
The following table lists the power and performance BIOS settings that you can configure through a BIOS policy or the default BIOS settings: 

Name |  Description |  Supported Attributes  
---|---|---  
Versions |  Platforms |  Values |  Dependencies  
Optimized Power Mode |  Automatically varies processor speed and power usage based on processor utilization to increase performance per watt. Most effective under moderate utilization.  |  4.3(2) and later |  C220 M7, C240 M7, X210c M7, X410c M7 |  Disabled, Enabled 

  * Disabled—This option is Disabled.
  * Enable—This options is enabled.

|  |  **Note** |  Not applicable for XE1X0M8.  
---|---  
C1 Auto Demotion |  If enabled, CPU automatically demotes to C1 based on un-core auto-demote information. |  4.0(2) and later |  C220 M6, C240 M6, B200 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, XE1X0M8  |  Disabled, Enabled, **Auto**

  * Disabled—This option is Disabled.
  * Enable—This options is enabled.

|  **Note** |  For XE1X0M8, its only Enabled and **Disabled**.   
---|---  
C1 Auto UnDemotion |  Select whether to enable processors to automatically undemote from C1. |  4.0(2) and later |  C220 M6, C240 M6, B200 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, XE1X0M8  |  Disabled, Enabled, **Auto**

  * Disabled—This option is Disabled.
  * Enable—This options is enabled.

For XE1X0M8, its only Enabled and **Disabled**.  |   
Core Performance Boost |  Whether the AMD processor increases its frequency on some cores when it is idle or not being used much |  4.0(2) and later |  C125 M5, C225 M6, C245 M6, C225 M8, C245 M8, X215c M8 |  Disabled, **Auto**

  * Disabled—This option is Disabled.
  * Auto—The CPU automatically determines how to boost performance.

|   
Global C State Control |  Whether the AMD processors control IO-based C-state generation and DF C-states. |  4.0(2) and later |  C125 M5, C225 M6, C245 M6, C225 M8, C245 M8, X215c M8 |  Auto, **Disabled** , Enabled 

  * Auto—This options is set to auto mode.
  * Disabled—This option is Disabled.
  * Enable—This options is enabled.

|   
Ln Stream HW Prefetcher, where n value is 1 and 2.  |  Whether the processor allows the AMD hardware prefetcher to speculatively fetch streams of data and instruction from memory into the L1 or L2 cache when necessary.  |  4.0(2) and later |  C125 M5, C225 M6, C245 M6, C225 M8, C245 M8, X215c M8 |  **Auto** , Disabled, Enabled 

  * Auto—This options is set to auto mode.
  * Disabled—This option is Disabled.
  * Enable—This options is enabled.

|   
Determinism Slider |  Allows AMD processors to determine how to operate. |  4.0(2) and later |  C125 M5, C225 M6, C245 M6,C225 M8, C245 M8, X215c M8 |  **Auto** , Performance, Power 

  * Auto—The CPU automatically uses default power determinism settings.
  * Performance—Processor operates at the best performance in a consistent manner.
  * Power—Processor operates at the maximum allowable performance on a per die basis.

|   
Efficiency Mode Enable |  Allows you to configure power consumption based on efficiency. |  4.0(2) and later |  C225 M6, C245 M6 |  **Auto** , Enabled 

  * Enabled—This option is enabled.
  * Auto—The CPU automatically uses default settings.

|   
CPPC |  Allows you to configure Collaborative Processor Performance Control. |  4.0(2) and later |  C225 M6, C245 M6, C225 M8, C245 M8, X215c M8 |  **Auto** , Disabled, Enabled 

  * Enabled—This option is enabled.
  * Disbled—This option is disabled.
  * Auto—The CPU automatically uses default settings.

|   
Enhanced CPU Performance |  Enhances CPU performance by adjusting server settings automatically.  |  4.0(2) and later |  C220 M6, C240 M6, B200 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C245 M8, X215c M8, C240 M8, X210c M8, X410c M8 |  Disabled, **Auto**

  * Disabled—This option is Disabled.
  * Auto—Allows to adjust server settings to increase the processor performance.

|  **Note** |  Enabling this functionality may increase power consumption.  
---|---  
The server should meet the following requirements in order to use this functionality:

  * The server should not contain Barlow Pass DIMMs.
  * DIMM module size present in the Cisco UCS C220 M6 server should be less than 64GB and in Cisco UCS C240 M6 server should be less than 256GB. 
  * No GPU cards are present in the server.

|  **Note** |  Not applicable for XE1X0M8.  
---|---  
LLC Dead Line |  In CPU non-inclusive cache scheme, Mid-Level Cache (MLC) evictions are filled into the Last-Level Cache (LLC). When lines are evicted from the MLC, the core can flag them as dead (not likely to be read again). The LLC has the option to drop dead lines and not fill them in the LLC.  |  4.0(2) and later |  C220 M6, C240 M6, B200 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8 |  Disabled, Enabled, **Auto**

  * **Disabled** —The dead lines are always dropped and are never filled into the LLC. 
  * **Enable** —Allows the LLC to fill dead lines into the LLC if there is free space available. This is the default option. 
  * Auto—The CPU determines the LLC dead line allocation.

|   
UPI Link Enablement |  Enables the number of Ultra Path Interconnect (UPI) links required by the processor. |  4.0(2) and later |  C220 M6, C240 M6, B200 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8 |  **Auto** , 1, 2, 3  |   
UPI Power Manangement |  The UPI power management can be used for conserving power on the server. |  4.0(2) and later |  C220 M6, C240 M6, B200 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8 |  Disabled, **Enabled**

  * **Disabled** —This option is Disabled. 
  * **Enable** —This options is enabled. 

|  |  **Note** |  Not applicable for XE1X0M8.  
---|---  
XPT Remote Prefetch |  This feature allows an LLC request to be duplicated and sent to an appropriate memory controller in a remote machine based on the recent LLC history to reduce latency.  |  4.0(2) and later |  C220 M6, C240 M6, B200 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8 |  **Disabled** , Enabled 

  * **Disabled** —This option is Disabled. 
  * **Enable** —This options is enabled. 
  * **Auto** —The CPU determines the functionality. 

|   
Latency Optimized Mode |  A set of BIOS settings that prioritize low latency and consistent performance over energy efficiency or other optimizations. |  4.3(6a) |  C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8 |  **Disabled** , Enabled 

  * **Disabled** —Options are Disabled. 
  * **Enabled** —Options are enabled. 

|   
Virtual Numa |  Simulates the Non-Uniform Memory Access (NUMA) architecture inside a virtual machine (VM) to optimize memory and processor resource allocation.  |  6.0(1a.0) and later |  C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8 |  **Disabled** , Enabled 

  * **Disabled** —Options are Disabled. 
  * **Enabled** —Options are enabled. 

| 

---

## Page 11: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-processor.html

## Processor  
  
The following table lists the Processor BIOS settings that you can configure through a BIOS policy or the default BIOS settings:

Name |  Description |  Supported Attributes  
---|---|---  
Versions |  Platforms |  Values |  Dependencies  
AVX512 |  The 512-bit extension of the 256-bit Advanced Vector Extensions (AVX) SIMD instructions.  |  4.3(4b) and later |  C225 M8, C245 M8, X215c M8 |  **Auto** , Enabled, Disabled  |   
Power Down Enable  |  Enable or disable the DDR power down mode.  |  4.3(4b) and later |  C225 M8, C245 M8, X215c M8 |  **Auto** , Enabled, Disabled  |   
Power Profile Selection F19h |  The DF P-state selection in the profile policy is overridden by the P-state range, the BIOS option or the APB_DIS BIOS option.where, F refers to the processor family and M denotes the model.  |  **Note** |  F19 tokens are expanding support to include F1A family processors.  
---|---  
4.3(4b) and later |  C245 M8, C225 M8, X215c M8 |  **High Performance Mode** , Efficiency Mode, Maximum IO Performance Mode, Balanced Memory Performance Mode  |   
SEV-ES ASID Space Limit |  The SEV-ES and SNP guests must use ASIDs in the range of 1 through 1007. |  4.3(4b) and later |  C245 M8, C225 M8, X215c M8 | 1-1007, with **1** as the default  |   
xGMI Force Link Width | The force xGMI link width.  |  4.3(4b) and later |  C245 M8, C225 M8, X215c M8 |  **Auto** , 0, 1, 2  |   
TSME  |  Provides hardware memory encryption of all the data stored on system DIMMs that is invisible to the OS and slightly increases the memory latency.  |  4.3(4b) and later |  C125 M5, C225 M6, C245 M6, C225 M8, C245 M8, X215c M8 |  Enabled, Disabled, **Auto** |   
4-link xGMI max speed |  Specifies the maximum frequency used for XGMI P-state in a 4-link topology. |  4.3(4b) and later |  C245 M8, C225 M8, X215c M8 |  20 Gbps, 25 Gbps, 32 Gbps, **Auto** |   
Fixed SOC P-State SP5 F19h |  Forced P-State to be independent or dependent, as reported by the ACPI _PSD object. It changes the SOC P-State if APBDIS is enabled. where, F refers to the processor family.  |  **Note** |  F19 tokens are expanding support to include F1A family processors.  
---|---  
4.3(4b) and later |  C245 M8, C225 M8, X215c M8 |  0 - 2 with 0 as the default.  |   
Fixed SOC P-State |  Forced P-State to be independent or dependent, as reported by the ACPI _PSD object. It changes the SOC P-State if APBDIS is enabled.  |  4.3(4b) and later |  C225 M6, C245 M6 |  **Po** , P1, P2,P3  |   
DF PState Frequency Optimizer |  Enable or Disable the DF P-state CCLK effective frequency optimizer. |  4.3(4b) and later |  C245 M8, C225 M8, X215c M8 |  **Auto** , Enabled, Disabled  |   
PRMRR Size |  Processor Reserved Memory Range Registers (PRMRR) is the size of the protected region in the system DRAM.  |  4.3(2) and later |  B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7 , C220 M8, C240 M8, X210c M8, X410c M8, C225 M8, C245 M8, X215c M8, XE1X0M8  |  Invalid Config, 1G, 2G, 4G, 8G, 16G, 32G, 64G, 128G, 256G, 512G, 128M, Auto, 256M, 512M  |  **Note** |  128M, Auto, 256M, 512M options are available only for M7 servers.  
---|---  
Adjacent Cache Line Prefetcher |  Whether the processor fetches cache lines in even/odd pairs instead of fetching just the required line. |  4.0(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  Disabled, **Enabled**

  * Disabled—This option is Disabled.
  * Enable—This option is enabled.

|  **CPU Performance** must be set to **Custom** to specify this value. For any value other than **Custom** , this option is overridden by the setting in the selected CPU performance profile.   
Autonomous Core C State |  Enables CPU Autonomous C-State, which converts the HALT instructions to the MWAIT instructions. |  4.0(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7  |  **Disabled** , Enabled  |  |  **Note** |  This is not applicable to XE1X0M8.  
---|---  
Boot Performance Mode |  Allows the user to select the BIOS performance state that is set before the operating system handoff. |  4.0(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7 , C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  | **Max Performance** , Max Efficient, Set by Intel NM  |  **Note** |  Set by Intel NM option is not applicable for M8 intel platforms.  
---|---  
Burst and Postponed Refresh |  Allows the memory controller to defer the refresh cycles when the memory is active and accomplishes the refresh within a specified window. The deferred refresh cycles may run in a burst of several refresh cycles.  |  4.0(2) and later |  C225 M6, C245 M6, C225 M8, C245 M8, X215c M8 |  **Disabled** , Enabled  |  We recommend you to leave this setting in the default state of **Disabled** to mitigate Rowhammer-style attacks.   
APBDIS |  Allows you to select the Algorithm Performance Boost (APB) Disable value for the SMU.  |  4.0(2) and later |  C225 M6, C245 M6,C225 M8, C245 M8, X215c M8 |  **Auto** , 0, 1 

  * **Auto** —Sets an auto ApbDis for the SMU. This is the default option. 
  * **0** —Clear ApbDis to SMU 
  * **1** —Set ApbDis to SMU 

|   
DFX OSB |  Controls the Opportunistic Snoop Broadcast (OSB) feature. OSB is used by CHA to broadcast snoops under lightly loaded ring or Intel UPI link condition. It is used to reduce the latency due to the directory lookup.  | 4.3(4a) and later |  X410c M7, X210c M7, X210c M8, X410c M8, XE1X0M8  |  Auto, **Enabled** , Disabled  |   
Downcore control F19 MA0h-AFh |  Provides the ability to remove one or more cores from operation is supported in the silicon. It may be desirable to reduce the number of cores due to operating system restrictions, or power reduction requirements of the system. This item allows the control on the number of cores that are running. This setting can only reduce the number of cores from only those available in the processor.  |  **Note** |  This is applicable only for AMD processors of family 19h and for models A0h-AFh. where, F refers to the processor family and M denotes the model   
---|---  
4.0(2) and later |  C225 M8, C245 M8, X215c M8 |  **Auto** , TWO (1 + 1), TWO (2 + 0), THREE (3 + 0), FOUR (2 + 2), FOUR (4 + 0)",  "SIX (3 + 3)" ONE (1 + 0), TWO (2 + 0), THREE (3 + 0), FOUR (4 + 0), FIVE (5 + 0), SIX (6 + 0), SEVEN (7 + 0), EIGHT (8 + 0), NINE (9 + 0), TEN (10 + 0), ELEVEN (11 + 0), TWELVE (12 + 0), THIRTEEN (13 + 0), FOURTEEN (14 + 0), FIFTEEN (15 + 0) 

  * Auto—The CPU determines how many cores must be enabled. This is the default option. 
  * ONE (1 + 0)—One core enabled on one CPU complex. 
  * TWO (2 + 0)—Two cores enabled on one CPU complex. 
  * **THREE (3 + 0)** —Three cores enabled on one CPU complex. 
  * **FOUR (4 + 0)** —Four cores enabled on one CPU complex. 
  * FIVE (5 + 0)—Five cores enabled on one CPU complex. 
  * **SIX (6 + 0)** —Six cores enabled on one CPU complex. 
  * SEVEN (7 + 0)—Seven cores enabled on one CPU complex. 
  * EIGHT (8 + 0)—Eight cores enabled on one CPU complex. 
  * NINE (9 + 0)—Nine cores enabled on one CPU complex. 
  * TEN (10 + 0)—Ten cores enabled on one CPU complex. 
  * ELEVEN (11 + 0)—Eleven cores enabled on one CPU complex. 
  * TWELVE (12 + 0)—Twelve cores enabled on one CPU complex. 
  * THIRTEEN (13 + 0)—Thirteen cores enabled on one CPU complex. 
  * FOURTEEN (14 + 0)—Fourteen cores enabled on one CPU complex. 
  * FIFTEEN (15 + 0)—Fifteen cores enabled on one CPU complex. 

|  This token is applicable only for the servers with 7xx2 and 7xx3 Model processors.  
Downcore control  |  Provides the ability to remove one or more cores from operation is supported in the silicon. It may be desirable to reduce the number of cores due to operating system restrictions, or power reduction requirements of the system. This item allows the control on the number of cores that are running. This setting can only reduce the number of cores from only those available in the processor.  |  4.0(2) and later |  C125 M5, C225 M6, C245 M6 |  **Auto** , TWO (1 + 1), TWO (2 + 0), THREE (3 + 0), FOUR (2 + 2), FOUR (4 + 0), SIX (3 + 3) 

  * Auto—The CPU determines how many cores must be enabled. This is the default option. 
  * TWO (1 + 1)—One core enabled on one CPU complex. 
  * TWO (2 + 0)—Two cores enabled on one CPU complex. 
  * **THREE (3 + 0)** —Three cores enabled on one CPU complex. 
  * **FOUR (4 + 0)** —Four cores enabled on one CPU complex. 
  * FIVE (5 + 0)—Five cores enabled on one CPU complex. 
  * **SIX (3 + 3)** —Six cores enabled on one CPU complex. 

|   
CPU Downcore control F19 M10h-1Fh |  Provides the ability to remove one or more cores from operation is supported in the silicon. It may be desirable to reduce the number of cores due to operating system restrictions, or power reduction requirements of the system. This item allows the control on the number of cores that are running. This setting can only reduce the number of cores from only those available in the processor.  |  **Note** |  This is applicable only for AMD processors of family 19h and for models 10h-1Fh. where, F refers to the processor family and M denotes the model   
---|---  
**Note** |  F19 tokens are expanding support to include F1A family processors.  
---|---  
4.3(4b) and later  |  C245 M8, C225 M8, X215c M8 |  **Auto** , ONE (1 + 0), TWO (2 + 0), THREE (3 + 0), FOUR (4 + 0), FIVE (5 + 0), SIX (6 + 0), SEVEN (7 + 0), EIGHT (8 + 0), NINE (9 \+ 0), TEN (10 + 0), ELEVEN (11 + 0), TWELVE (12 + 0), THIRTEEN (13 + 0), FOURTEEN (14 + 0), FIFTEEN (15 + 0)  |   
Streaming Stores Control |  Enables the streaming store functionality. |  4.0(2) and later |  C225 M6, C245 M6, C245 M8, C225 M8, X215c M8 |  **Auto** , Disabled, Enabled  |   
Fixed SOC P-State |  This option defines the target P-state when APBDIS (to disable Algorithm Performance Boost (APB)) is set. The **P-x** specify a valid P-state for the processor installed.  |  4.0(2) and later |  C225 M6, C245 M6, C245 M8, C225 M8, X215c M8 |  **Auto** , P0, P1, P2, P3 

  * **Auto** —Sets a valid P-state suitable for the processor. This is the default option. 
  * **P0 to P3** —Highest-performing SOC P-state to lowest-performing SOC P-state. 

|   
DF C-States |  When long duration idleness is expected in a system, this control allows the system to transition into a DF C-state which can set the system into an even lower power state.  |  4.0(2) and later |  C225 M6, C245 M6, C245 M8, C225 M8, X215c M8 |  **Auto** , Disabled, Enabled  |   
CCD Control |  Allows you to specify the number of charge-coupled device CCDs that are desired to be enable in the system. |  4.0(2) and later |  C225 M6, C245 M6,C245 M8, C225 M8, X215c M8 |  **Auto** , 2 CCDs, 3 CCDs, 4 CCDs, 6 CCDs, 8 CCDs, 10 CCDs  |  **Note** | 

  * 2 CCDs, 3 CCDs, 4 CCDs, 6 CCDs options are available only for M6 servers.
  * 2 CCDs, 4 CCDs, 6 CCDs, 8 CCDs, and 10 CCDs options are available only for M8 servers.

  
---|---  
CPU Downcore control 7xx3chk m5 and m6 and update  |  Provides the ability to remove one or more cores from operation is supported in the silicon. It may be desirable to reduce the number of cores due to operating system restrictions, or power reduction requirements of the system. This item allows the control on the number of cores that are running. This setting can only reduce the number of cores from only those available in the processor.  |  4.0(2) and later |  C225 M6, C245 M6 |  **Auto** , ONE (1 + 0), TWO (2 + 0), THREE (3 + 0), FOUR (4 + 0), FIVE (5 + 0), SIX (6 + 0), SEVEN (7 + 0)  |   
Downcore control |  Provides the ability to remove one or more cores from operation is supported in the silicon. It may be desirable to reduce the number of cores due to operating system restrictions, or power reduction requirements of the system. This item allows the control on the number of cores that are running. This setting can only reduce the number of cores from only those available in the processor.  |  4.0(2) and later |  C125 M5 |  **Auto** , TWO (1 + 1),TWO (2 + 0), THREE (3 + 0), FOUR (2 + 2), SIX (3 + 3)  |   
ACPI SRAT L3 Cache As NUMA Domain |  Creates a layer of virtual domains on top of the physical domains in which each Cisco Compatible Extensions is declared to be in its on domain.  |  4.2(1) and later |  C225 M6, C245 M6,C245 M8, C225 M8, X215c M8 |  **Auto** , Disabled, Enabled  |   
Cisco xGMI Max Speed |  This option enables 18 Gbps XGMI link speed. |  4.0(2) |  C225 M6, C245 M6 |  **Disabled** , Enabled  |   
Processor CMCI |  Allows the CPU to trigger interrupts on corrected machine check events. The corrected machine check interrupt (CMCI) allows faster reaction than the traditional polling timer.  |  4.0(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, X210c M7, C220 M6, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  Disabled, **Enabled** |   
Configurable TDP Level |  Allows you to set a customized value for Thermal Design Power (TDP). |  4.0(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  **Normal** , Level 1, Level 2  |   
Core Multi Processing |  Sets the state of logical processor cores per CPU in a package. If you choose All as the value, Intel Hyper Threading technology is also enabled.  |  4.0(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  **All** , 1 through 86 

  * All— Enables multiprocessing on all logical processor cores.
  * 1 through 86—Specifies the number of logical processor cores per CPU that can run on the server. To disable multiprocessing and have only one logical processor core per CPU running on the server, choose 1. 

|  **Note** |  1, 2, and 3 options are not applicable for M8 servers.  
---|---  
**Note** |  From 65 to 86 is applicable for M8 servers only.  
---|---  
**Note** |  From 1 to 64 is applicable for M7 servers only.  
---|---  
**Note** |  From 1 to 42 is applicable for XE1X0M8 server only.  
---|---  
We recommend that you contact your operating system vendor to make sure your operating system supports this feature.  
Energy Performance |  Allows you to determine whether system performance or energy efficiency is more important on this server. |  4.0(2) and later |  B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8 |  Performance, **Balanced Performance,** Balanced power, power  |  **Power Technology** must be set to **Custom** or the server ignores the setting for this parameter.   
CPU Performance |  CPU performance by adjusting server settings automatically. |  4.0(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, XE1X0M8 |  **Disabled** , Enabled  |   
EDC Control Throttle |  Enables or disables the EDC Shutdown Protection which enhances the utilization tracking to avoid EDC shutdown responses to specific aggressive workloads.  |  4.3(4a) and later | C245 M6, C225 M6 |  **Auto** , Enabled, Disabled  |   
DLWM Support |  This value controls the Dynamic Link Width Management (DLWM) feature. When the platform can support either an 8 lane or 16 lane xGMI operation, the dynamic adjustment feature provides power savings. |  4.3(4a) and later | C245 M6, C225 M6 |  **Auto** , Enabled, Disabled  |   
Energy Efficient Turbo |  When energy efficient turbo is enabled, the optimal turbo frequency of the CPU turns dynamic based on CPU utilization. The power/performance bias setting also influences the energy efficient turbo.  |  4.0(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  **Disabled** , Enabled  |   
Enhanced Intel Speedstep(R) Technology |  Whether the processor uses Enhanced Intel SpeedStep Technology, which allows the system to dynamically adjust processor voltage and core frequency. This technology can result in decreased average power consumption and decreased average heat production.  |  4.0(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  Disabled, **Enabled** |   
Processor EPP Enable |  Allows you to determine whether system performance or energy efficiency is more important on this server.  |  4.0(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5 |  Disabled, **Enabled** |   
Processor EPP Profile |  Allows you to determine whether system performance or energy efficiency is more important on this server.  |  4.0(2) and later |  C220 M6, C240 M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  | Performance, **Balanced Performance,** Balanced power, power  |   
Execute Disable Bit |  Classifies memory areas on the server to specify where the application code can execute. As a result of this classification, the processor disables code execution if a malicious worm attempts to insert code in the buffer. This setting helps to prevent damage, worm propagation, and certain classes of malicious buffer overflow attacks.  |  4.0(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5 |  Disabled, **Enabled** |   
IOAT Configuration |  Enables or disables the CPM (Content Processing Module) in IOAT (Intel® I/O Acceleration Technology) accelerators. |  4.3(3c) and later |  C220 M7, C240 M7, X210 M7, X410 M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8 |  Disabled, Enabled |   
Local APIC Mode* |  Selects the APIC mode to be used. |  4.3(4a) and later |  C245 M6, C225 M6, C225 M8, C245 M8, X215c M8 | Compatibility, XAPIC, X2APIC, **Auto** |   
Local X2 Apic |  Allows you to set the type of Advanced Processor Interrupt controller (APIC) architecture. |  4.0(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7  |  **Disabled** , Enabled  |   
Hardware Prefetcher |  Whether the processor allows the Intel hardware prefetcher to fetch streams of data and instructions from memory into the unified second-level cache when necessary.  |  4.0(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  Disabled, **Enabled** |   
CPU Hardware Power Management |  Enables processor Hardware Power Management (HWPM). |  4.0(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, XE1X0M8  |  Disabled, **HWPM Native Mode** , HWPM OOB Mode, Native Mode with no Legacy  |   
IMC Interleaving |  This BIOS option controls the interleaving between the Integrated Memory Controllers (IMCs). |  4.0(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5 |  **Auto** , 1-way Interleave, 2-way Interleave  |   
Intel Dynamic Speed Select |  Intel Dynamic Speed Select modes allow you to run the CPU with different speeds and cores in auto mode. |  4.0(2) and later |  B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  **Disabled** , Enabled  |   
Intel HyperThreading Tech |  Whether the processor uses Intel Hyper-Threading Technology, which allows multithreaded software applications to execute threads in parallel within each processor.  |  4.0(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  Disabled, **Enabled** |   
Intel Turbo Boost Tech |  Whether the processor uses Intel Turbo Boost Technology, which allows the processor to automatically increase its frequency if it is running below power, temperature, or voltage specifications.  |  4.0(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  **Disabled** , Enabled  |   
Intel(R) VT |  Whether the processor uses Intel Virtualization Technology for Directed I/O (VT-R) |  4.0(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  Disabled, **Enabled** |   
DCU IP Prefetcher |  Whether the processor uses the DCU IP Prefetch mechanism to analyze historical cache access patterns and preload the most relevant lines in the L1 cache.  |  4.0(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  Disabled, **Enabled** |   
KTI Prefetch |  KTI prefetch is a mechanism to get the memory read started early on a DDR bus.  |  4.0(2) and later |  B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8 |  Disabled, **Enabled** , Auto  |  **Note** |  Auto option is not applicable for M5 servers.  
---|---  
LLC Prefetch |  Whether the processor uses the LLC Prefetch mechanism to fetch the date into the LLC. |  4.0(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  Disabled, **Enabled** |   
Package C State Limit |  The amount of power available to the server components when they are idle. |  4.0(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  No Limit, Auto, **C0 C1 State** , C2, C6 Non Retention, C6 Retention  |  **Note** |  C6 Retention option is not applicable for M8 servers.  
---|---  
If you are changing the **Package C State Limit** token then ensure that the **Power Technology** is set to **Custom**.   
Patrol Scrub |  It sets the interval for a full memory scan. |  4.0(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  Disabled, **Enabled**

  * Enable—The system periodically reads and writes memory searching for ECC errors. If any errors are found, the system attempts to fix them. This option may correct single bit errors before they become multi-bit errors, but it may adversely affect performance when the patrol scrub is running. 
  * Disable—The system checks for memory ECC errors only when the CPU reads or writes a memory address.

|  The lower the interval, the more memory bandwidth is used for scrubbing.  
Patrol Scrub Configuration |  It sets the interval for a full memory scan. |  4.0(2) and later |  B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7 |  Enabled, Disabled, Enable at End of POST

  * Enable—The system periodically reads and writes memory searching for ECC errors. If any errors are found, the system attempts to fix them. This option may correct single bit errors before they become multi-bit errors, but it may adversely affect performance when the patrol scrub is running. 
  * Disable—The system checks for memory ECC errors only when the CPU reads or writes a memory address.

|  **Note** |  Enabled option is applicable for M6 servers only.  
---|---  
Processor C1E |  Allows the processor to transition to its minimum frequency upon entering C1. This setting does not take effect until after you have rebooted the server.  |  4.0(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  **Disabled** , Enabled  |  **Note** |  It is Enabled by default for XE1X0M8.  
---|---  
Processor C6 Report |  Whether the processor sends the C6 report to the operating system. |  4.0(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  **Disabled** , Enabled  |   
PCIe Ten Bit Tag Support |  Enables the PCIe ten bit tags for the supported devices. |  4.3(4a) and later | C225 M6, C245 M6, C225 M8, C245 M8, X215c M8 |  **Auto** , Enabled, Disabled  |   
P STATE Coordination |  **Note** |  It is also called EIST PSD Function in UCSM.  
---|---  
Allows you to define how BIOS communicates the P-state support model to the operating system. There are 3 models as defined by the Advanced Configuration and Power Interface (ACPI) specification.  |  4.0(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  **SW All** , HW All, SW Any  |  **Note** |  SW Any option is available for M5 servers only.  
---|---  
**Power Technology** must be set to **Custom** or the server ignores the setting for this parameter.   
Power Performance Tuning |  Determines if the BIOS or Operating System can turn on the energy performance bias tuning. The options are BIOS and operating system.  |  4.0(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7,C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  BIOS, **OS** , PECI  |  **Note** |  PECI option is available for M6 and M7 servers only.  
---|---  
UPI Link Frequency Select |  Allows you to select different UPI link frequency running. |  4.0(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8  |  **Auto** , 9.6GT/S, 10.4GT/S, 11.2GT/S, 12.8GT/s, 14.4GT/s, 16.0GT/s, 20.0GT/s, 24.0GT/s, Use Per Link Setting  |  **Note** | 

  * 12.8GT/s, 14.4GT/s, 16.0GT/s, 20.0GT/s options are available for M7 servers only.
  * 11.2GT/S option is available for M6 server only.
  * 16,20, 24, Auto, Use Per Link Setting is applicable for M8 servers only

  
---|---  
|  **Note** |  Not applicable for XE1X0M8.  
---|---  
SMT Mode |  Whether the processor uses AMD Simultaneous MultiThreading Technology, which allows multithreaded software applications to execute threads in parallel within each processor.  |  4.0(2) and later |  C125 M5, C225 M6, C245 M6, C225 M8, C245 M8, X215c M8 |  Disabled, **Enabled** , Auto, Off  |  **Note** |  **Off** options are available for M5 servers only with Auto as the default.   
---|---  
Sub Numa Clustering |  Whether the CPU supports sub NUMA clustering, in which the tag directory and the memory channel are always in the same region. |  4.0(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  **Disabled** , Enabled, Auto, SNC2, SNC4  |  **Note** | 

  * Auto option is available for M5, M7, and M8 servers only.
  * Enabled option is available for M6 and M8 servers only.
  * Disabled option is available for M6, M7, and M8 servers only.
  * SNC2, SNC4 options are available for M7 and M8 servers only.

  
---|---  
DCU Streamer Prefetch |  Whether the processor uses the DCU IP Prefetch mechanism to analyze historical cache access patterns and preload the most relevant lines in the L1 cache.  |  4.0(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  Disabled, **Enabled** , Auto  |  **Note** |  Auto option is applicable to M8 intel platforms only.  
---|---  
SVM Mode |  Whether the processor uses AMD Secure Virtual Machine Technology.  |  4.0(2) and later |  C215 M5, C225 M6, C245 M6, C225 M8, C245 M8, X215c M8 |  Disabled, **Enabled** |   
Uncore Frequency Scaling |  Allows you to configure the scaling of the uncore frequency of the processor. |  4.0(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  Disabled, **Enabled** , Mode 0, and Mode 1  |  **Note** |  Mode 0 and Mode 1 is applicable for M8 servers only with Mode 1 being default. Mode 1 is the default for XE1X0M8.  
---|---  
Uncore Frequency Scaling IO |  Adjusts the frequency of processor uncore components responsible for I/O operations to optimize power and performance.  |  6.0(1a.0) and later |  C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8 |  **Mode 1** , Mode 0  |   
Workload Configuration |  This feature allows for workload optimization. |  4.0(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  Balanced, **IO Sensitive** |   
XPT Prefetch |  Whether XPT prefetch is used to enable a read request that is sent to the last level cache to issue a copy of that request to the memory controller prefetcher.  |  4.0(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7 , C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  **Auto** , Disabled, Enabled  |   
X2APIC Opt-Out Flag |  Prevents the operating system from enabling extended xAPIC (x2APIC) mode when the OS is not working with x2APIC. |  4.2(3) and later |  C220 M6, C240 M6, B200 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7  |  **Disabled** , Enabled  |   
Intel Speed Select |  Allows you to adjust different cores to operate in different frequencies to have a better power efficiency. The values **Config 1** and **Config 2** are not supported on Cisco UCS M6 and M7 servers.  For Cisco UCS M6 and Cisco UCS M7 servers, the values **Config 3** and **Config 4** (4th Gen Intel Xeon Scalable processors and 5th Gen Intel Xeon Scalable processors) are equivalent to the values **Config 1** and **Config 2** (3rd Gen Intel Xeon Scalable processors).  |  4.0(2) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, C220 M6, C240 M6, B200 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7 , C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  **Auto** , Base, Config 1, Config 2, Config 3, Config 4 

  * Config 1 and Config 2 are options available for M5 servers only with Base as the default.
  * Auto is the default for M8.

|   
Memory Clock Speed 7xx3 (AMD 3rd Gen CPU)  |  Allows the memory clock to be further reduced from the maximum platform limit. |  4.3(4a) and later |  C245 M6, C225 M6 |  **Auto** , 800 MHz, 933 MHz, 1067 MHz, 1200 MHz, 1333 MHz, 1467MHz, 1600 MHz, 1633 MHz, 1667MHz, 1700 MHz, 1733 MHz, 1767 MHz, 1800 MHz, 400 MHz  |   
Memory Clock Speed 7xx2 (AMD 2nd Gen CPU)  |  Allows the memory clock to be further reduced from the maximum platform limit. |  4.3(4a) and later |  C245 M6, C225 M6 |  **Auto** , 667 MHz, 800 MHz, 933 MHz, 1067 MHz, 1200 MHz, 1333 MHz, 1467 MHz, 1600 MHz  |   
xGMI Link Configuration | Configures the number of xGMI2 links used on a multi-socket system. |  4.3(4a) and later |  C245 M6, C225 M6 |  **Auto** , 2 xGMI Links, 3 xGMI Links, 4 xGMI Links  |  **Note** |  2 xGMI Links is not supported for C245 M6, C225 M6 platforms.  
---|---  
Preferred IO 7xx3(AMD 3rd Gen CPU)  |  Enables the feature for a _preferred bus_ as a performance improvement.  |  4.3(4a) and later |  C245 M6, C225 M6 |  **Auto** , Bus  |   
Preferred IO 7xx2 (AMD 2nd Gen CPU)  |  Enables the feature for a _preferred bus_ as a performance improvement.  |  4.3(4a) and later |  C245 M6, C225 M6 |  **Auto** , Manual  |   
Core Watchdog Timer Enable |  Enables or disables CPU watchdog timer. |  4.3(4a) and later |  C245 M6, C225 M6 |  **Auto** , Enabled, Disabled  |   
IIO eDPC Support |  The eDPC (Enhanced Downstream Port Containment) allows a downstream link to be disabled after an uncorrectable error, enabling recovery possible in a controlled and robust manner. This can be one of the following:  |  4.3(6c) and later |  C220 M8, C240 M8, C225 M8, C245 M8, X215c M8, C220 M7, C240 M7, C220 M6, C240 M6 |  Disabled, On Fatal Error, **On Fatal and Non-Fatal Errors** |  **Note** |  The value _On Fatal Error_ is not supported on C225 M8, C245 M8, and X215c M8 servers.   
---|---  
  
  * **Disabled** —eDPC support is turned off, and the system does not take any action to disable downstream links in response to errors. 

  * **On Fatal Error** —eDPC is enabled only for fatal errors.is not supported on Cisco UCS C225 M8, Cisco UCS C245 M8, and X215c M8 servers. 

  * **On Fatal and Non-Fatal Errors** —eDPC is enabled for both fatal and non-fatal errors. 


  
Speculative Lock |  The confl_lock metric counts how many times lock conflicts occur. |  6.0(2x) |  C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8 |  Enabled, Disabled  |   
CPU Frequency Control |  Indicates adjusting the speed of the CPU to find a good balance between how fast it works and how much power it uses.  |  6.0(2x) |  C245 M8, C225 M8, X215c M8 |  Auto, Enabled, Disabled  |   
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

For Local APIC Mode Bios token, Compatability values are not supported for AMD EPYC 7XX2 series. 

* * *  
  
---|---

---

## Page 12: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-qpi.html

## QPI  
  
The following table lists the QPI BIOS settings that you can configure through a BIOS policy or the default BIOS settings:

Name |  Description |  Supported Attributes  
---|---|---  
Versions |  Platforms |  Values |  Dependencies  
QPI Link Frequency Select |  The Intel QuickPath Interconnect (QPI) link frequency, in megatransfers per second (MT/s). |  4.0(4) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8  |  **Auto** , 9.6 GT/s, 10.4 GT/s, 11.2GT/s, 12.8GT/s, 14.4GT/s, 16.0GT/s, 20.0GT/s, 16.0GT/s, 20.0GT/s,24.0GT/s, Auto, Use Per Link Setting  |  **Note** |  9.6 GT/s, 10.4 GT/s options available for M5 and M6 servers only. 11.2GT/s for M6 and 12.8GT/s, 14.4GT/s, 16.0GT/s, 20.0GT/s for M7.   
---|---  
**Note** |  16.0GT/s, 20.0GT/s,24.0GT/s, Auto, Use Per Link Setting is applicable for M8 servers only.  
---|---

---

## Page 13: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-server-management.html

## Server Management  
  
The following table lists the server management BIOS settings that you can configure through a BIOS policy or the default BIOS settings: 

Name |  Description |  Supported Attributes  
---|---|---  
Versions |  Platforms |  Values |  Dependencies  
Baud Rate |  What Baud rate is used for the serial port transmission speed. If you disable Console Redirection, this option is not available. |  4.2(1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, C125 M5, B200 M6, C220 M6, C240 M6, X210c M6, C225 M6, C245 M6, C220 M7, C240 M7, X210c M7, X410c M7, C225 M8, C245 M8, X215c M8, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  9.6k, 19.2k, 38.4k, 57.6k, **115.2k** |  This setting must match the setting on the remote terminal application.  
CDN Control |  Consistent Device Naming allows Ethernet interfaces to be named in a consistent manner. This makes Ethernet interface names more uniform, easy to identify, and persistent when adapter or other configuration changes are made.  |  4.2(1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, C125 M5, B200 M6, C220 M6, C240 M6, X210c M6, C225 M6, C245 M6, C220 M7, C240 M7, X210c M7, X410c M7, C225 M8, C245 M8, X215c M8, C220 M8, C240 M8, X210c M8, XE1X0M8  |  **Enabled** , Disabled  |   
Adaptive Memory Training |  When this token is enabled, the BIOS saves the memory training results (optimized timing/voltage values) along with CPU/memory configuration information and reuses them on subsequent reboots to save boot time. The saved memory training results are used only if the reboot happens within 24 hours of the last save operation.  |  4.2(1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  **Enabled** , Disabled  |   
BIOS Techlog Level |  This option denotes the type of messages in BIOS tech log file. |  4.2(1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, C125 M5, B200 M6, C220 M6, C240 M6, X210c M6, C225 M6, C245 M6, C220 M7, C240 M7, X210c M7, X410c M7, C225 M8, C245 M8, X215c M8, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  Maximum, **Minimum** , Normal 

  * Maximum—Critical messages will be displayed in the log file. This is the default option
  * Minimum—Warning and loading messages will be displayed in the log file.
  * Normal—Normal and information related messages will be displayed in the log file.

|   
OptionROM Launch Optimization |  The Option ROM launch is controlled at the PCI Slot level, and is enabled by default. In configurations that consist of a large number of network controllers and storage HBAs having Option ROMs, all the Option ROMs may get launched if the PCI Slot Option ROM Control is enabled for all. However, only a subset of controllers may be used in the boot process. When this token is enabled, Option ROMs are launched only for those controllers that are present in boot policy.  |  4.2(1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, C125 M5, B200 M6, C220 M6, C240 M6, X210c M6, C225 M6, C245 M6, C220 M7, C240 M7, X210c M7, X410c M7, C225 M8, C245 M8, X215c M8, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  **Enabled** , Disabled  |   
Console Redirection |  Allows a serial port to be used for console redirection during POST and BIOS booting. After the BIOS has booted and the operating system is responsible for the server, console redirection is irrelevant and has no effect  |  4.2(1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, C125 M5, B200 M6, C220 M6, C240 M6, X210c M6, C225 M6, C245 M6, C220 M7, C240 M7, X210c M7, X410c M7, C225 M8, C245 M8, X215c M8, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  **Disabled** , COM 0, COM 1 

  * COM 0 enables serial port for console redirection during POST. This option is valid only for M6 blade servers and rack-mount servers. 
  * COM 1 or serial-port-b enables serial port B for console redirection and allows it to perform server management tasks. This option is only valid for rack-mount servers. 

|  If you enable this option, you also disable the display of the Quiet Boot logo screen during POST.  
Flow Control |  Whether a handshake protocol is used for flow control. Request to Send / Clear to Send (RTS/CTS) helps to reduce frame collisions that can be introduced by a hidden terminal problem.  |  4.2(1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, C125 M5, B200 M6, C220 M6, C240 M6, X210c M6, C225 M6, C245 M6, C220 M7, C240 M7, X210c M7, X410c M7, C225 M8, C245 M8, X215c M8, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  **None** , RTC-CTS  |  This setting must match the setting on the remote terminal application.  
FRB 2 Timer |  Whether the FRB2 timer is used for recovering the system if it hangs during POST. |  4.2(1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, C125 M5 , B200 M6, C220 M6, C240 M6, X210c M6, C225 M6, C245 M6, C220 M7, C240 M7, X210c M7, X410c M7 C225 M8, C245 M8, X215c M8, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  **Enabled** , Disabled  |   
OS Boot Watchdog Timer  |  Whether the BIOS programs the watchdog timer with a predefined timeout value. If the operating system does not complete booting before the timer expires, the CIMC resets the system and an error is logged.  |  4.2(1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, C125 M5, B200 M6, C220 M6, C240 M6, X210c M6, C225 M6, C245 M6, C220 M7, C240 M7, X210c M7, X410c M7, C225 M8, C245 M8, X215c M8, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  Enabled, **Disabled** |   
OS Boot Watchdog Timer Policy |  What action the system takes if the watchdog timer expires. |  4.2(1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, C125 M5, B200 M6, C220 M6, C240 M6, X210c M6, C225 M6, C245 M6, C220 M7, C240 M7, X210c M7, X410c M7, C225 M8, C245 M8, X215c M8, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  **Power-off** , Reset  |   
OS Watchdog Timer Timeout |  What timeout value the BIOS uses to configure the watchdog timer. |  4.2(1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, C125 M5, B200 M6, C220 M6, C240 M6, X210c M6, C225 M6, C245 M6, C220 M7, C240 M7, X210c M7, X410c M7, C225 M8, C245 M8, X215c M8, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  5 minutes, **10 minutes** , 15 minutes, 20 minutes  |   
Serial Mux |  Enables or disables the serial mux configuration. |  4.3(4a) and later |  C245 M6, C225 M6 |  Enabled, Disabled |   
Terminal Type |  What type of character formatting is used for console redirection. |  4.2(1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, C125 M5, B200 M6, C220 M6, C240 M6, X210c M6, C225 M6, C245 M6, C220 M7, C240 M7, X210c M7, X410c M7, C225 M8, C245 M8, X215c M8, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  PC-ANSI, **VT100** , VT100-PLUS, VT-UTF8  |  This setting must match the setting on the remote terminal application.  
GPU Direct CPU1 |  When enabled, ACS is disabled for GPUs on the specified CPU in systems using the UCXS-580P. |  6.0(1.250229) |  X210c M7, X410c M7, X210c M8, X410c M8 |  Enabled, **Disabled** |   
GPU Direct CPU2 |  When enabled, ACS is disabled for GPUs on the specified CPU in systems using the UCXS-580P. |  6.0(1.250229) |  X210c M7, X410c M7,X210c M8, X410c M8 |  Enabled, **Disabled** |   
GPU Direct CPU3 |  When enabled, ACS is disabled for GPUs on the specified CPU in systems using the UCXS-580P. |  6.0(2.x) |  X410c M7, X410c M8 |  Enabled, **Disabled** |   
GPU Direct CPU4 |  When enabled, ACS is disabled for GPUs on the specified CPU in systems using the UCXS-580P. |  6.0(2.x) |  X410c M7, X410c M8 |  Enabled, **Disabled** | 

---

## Page 14: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-trusted-platform.html

## Trusted Platform  
  
The following table lists the trusted platform BIOS settings that you can configure through a BIOS policy or the default BIOS settings: 

Name |  Description |  Supported Attributes  
---|---|---  
Versions |  Platforms |  Values |  Dependencies  
Multikey Total Memory Encryption (MK-TME) |  MK-TME allows you to have multiple encryption domains with one with own key. Different memory pages can be encrypted with different keys.  |  4.2(1) nnd later |  C220 M6, C240 M6, B200 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8 |  Enabled, **Disabled** |   
Software Guard Extensions (SGX) |  Allows you to enable Software Guard Extensions(SGX) feature. |  4.2(1) and later |  C240 M6, C220 M6, B200 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  Enabled, **Disabled** |   
Total Memory Encryption (TME) |  Allows you to provide the capability to encrypt the entirety of the physical memory of a system. |  4.2(1) and later |  C220 M6, C240 M6, B200 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, XE1X0M8 |  **Enabled** , Disabled  |   
Select Owner EPOCH Input Type |  Allows you to change the seed for the security key used for the locked memory region that is created. |  4.2(1) and later |  C240 M6, C220 M6, B200 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8 |  SGX Owner EPOCH activated, Change to New Random Owner EPOCHs, **Manual User Defined Owner EPOCHs** , SGX Owner EPOCH deactivated  |  **Note** |  SGX Owner EPOCH deactivated option is applicable for M8 servers only.  
---|---  
SGX Auto MP Registration Agent |  Allows you to enable the registration authority service to store the platform keys. |  4.2(1) and later |  C240 M6, C220 M6, B200 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8 |  Enabled, **Disabled** |   
SGX Epoch 0 |  Allows you to define the SGX EPOCH owner value for the EPOCH number designated by 0. |  4.2(1) and later |  C240 M6, C220 M6, B200 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, XE1X0M8  |  0 - ffffffffffffffff with a step size of 1 |   
SGX Epoch 1 |  Allows you to define the SGX EPOCH owner value for the EPOCH number designated by 1. |  4.2(1) and later |  C240 M6, C220 M6, B200 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, XE1X0M8  |  0 - ffffffffffffffff with a step size of 1 |   
SGX Factory Reset |  Allows the system to perform SGX factory reset on subsequent boot. |  4.2(1) and later |  C240 M6, C220 M6, B200 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, XE1X0M8  |  Enabled, **Disabled** |   
SGX PubKey Hashn where _n_ ranges from 0 to 3.  |  Allows you to set the Software Guard Extensions (SGX) value. |  4.2(1) and later |  C240 M6, C220 M6, B200 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  **SGX PUBKEY HASH0** , SGX PUBKEY HASH1, SGX PUBKEY HASH2, SGX PUBKEY HASH3 

  * SGX PUBKEY HASH0—Between 7-0.
  * SGX PUBKEY HASH1—Between 15-8.
  * SGX PUBKEY HASH2—Between 23-16.
  * SGX PUBKEY HASH3—Between 31-24.

|   
SGX Write Enable |  Allows you to enable SGX Write feature. |  4.2(1) and later |  C240 M6, C220 M6, B200 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  **Enabled** , Disabled  |   
SGX Package Information In-Band Access |  Allows you to enable SGX Package Info In-Band Access. |  4.2(1) and later |  C240 M6, C220 M6, B200 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8 |  Enabled, **Disabled** |   
SGX QoS |  Allows you to enable SGX QoS. |  4.2(1) and later |  C240 M6, C220 M6, B200 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  **Enabled** , Disabled  |   
SHA-1 PCR Bank |  The Platform Configuration Register (PCR) is a memory location in the TPM. Multiple PCRs are collectively referred to as a PCR bank. A Secure Hash Algorithm 1 or SHA-1 PCR Bank allows to enable or disable TPM security.  |  4.2(1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, C125 M5, B200 M6, C220 M6, C240 M6, X210c M6, C225 M6, C245 M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M7, C240 M7, X210c M7, X410c M7, C225 M8, C245 M8, X215c M8, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  **Enabled** , Disabled  |  **Note** |  For C245 M8, it is Disabled by default.   
---|---  
If the Security Device Support is disabled then the entire TPM operation will fail.  
SHA256 PCR Bank |  The Platform Configuration Register (PCR) is a memory location in the TPM. Multiple PCRs are collectively referred to as a PCR bank. A Secure Hash Algorithm 256-bit or SHA-256PCR Bank allows to enable or disable TPM security.  |  4.2(1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, C125 M5, B200 M6, C220 M6, C240 M6, X210c M6,C225 M6, C245 M6,C220 M7, C240 M7, X210c M7, X410c M7,C220 M7, C240 M7, X210c M7, X410c M7,C225 M8, C245 M8, X215c M8,C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  **Enabled** , Disabled  |  If the Security Device Support is disabled then the entire TPM operation will fail.  
SHA384 PCR Bank* |  The Platform Configuration Register (PCR) is a memory location in the TPM. Multiple PCRs are collectively referred to as a PCR bank. A Secure Hash Algorithm 384-bit or SHA-384PCR Bank allows to enable or disable TPM security.  |  4.3(3a) and later |  B200 M6, C220 M6, C240 M6, X210c M6, C225 M6, C245 M6, C220 M7, C240 M7, X210c M7, X410c M7,C220 M7, C240 M7, X210c M7, X410c M7,C225 M8, C245 M8, X215c M8, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  Enabled, **Disabled** |  If the Security Device Support is disabled then the entire TPM operation will fail.  
Trusted Platform Module State |  Whether to enable or disable the Trusted Platform Module (TPM), which is a component that securely stores artifacts that are used to authenticate the server.  |  4.2(1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, C125 M5, B200 M6, C220 M6, C240 M6, X210c M6, C225 M6, C245 M6, C220 M7, C240 M7, X210c M7, X410c M7,C225 M8, C245 M8, X215c M8, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  **Enabled** , Disabled  |  If the Security Device Support is disabled then the entire TPM operation will fail.  
Trust Domain Extension  |  Whether to enable or disable the Trust Domain Extension (TDX), which protects the sensitive data and applications from unauthorized access.  |  4.3(3a) and later |  C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8 |  Enabled, **Disabled** |  To enable Trust Domain Extension, ensure that:

  * Total Memory Encryption (TME) is Enabled.
  * Software Guard Extensions (SGX) is Enabled.
  * Multikey Total Memory Encryption (MK-TME) is Enabled.
  * LIMIT CPU PA to 46 Bits token is Disabled.

  
TDX Secure Arbitration Mode (SEAM) Loader |  Whether to enable or disable the TDX Secure Arbitration Mode (SEAM) Loader, which helps to verify the digital signature on the Intel TDX module and load it into the SEAM-memory range.  |  4.3(3a) and later |  X410c M7, X210c M7, C220 M7, C240 M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8 |  Enabled, **Disabled** |  To enable TDX Secure Arbitration Mode Loader, ensure that:

  * Total Memory Encryption (TME) is Enabled.
  * Software Guard Extensions (SGX) is Enabled.
  * Multikey Total Memory Encryption (MK-TME) is Enabled.
  * LIMIT CPU PA to 46 Bits token is Disabled.
  * Trust Domain Extension (TDX) is Enabled.

  
TPM Pending Operation |  Trusted Platform Module (TPM) Pending Operation option allows you to control the status of the pending operation. |  4.2(1) and later |  C240 M6, C220 M6, B200 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C225 M8, C245 M8, X215c M8, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  **None** , TpmClear  |  If the Security Device Support is disabled then the entire TPM operation will fail.  
TPM Minimal Physical Presence |  Whether to enable or disable TPM Minimal Physical Presence, which enables or disables the communication between the OS and BIOS for administering the TPM without compromising the security.  |  4.2(1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, B200 M6, C220 M6, C240 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  Enabled, **Disabled** |  If the Security Device Support is disabled then the entire TPM operation will fail.  
Intel Trusted Execution Technology Support |  Whether to enable or disable Intel Trusted Execution Technology (TXT), which provides greater protection for information that is used and stored on the business server.  |  4.2(1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5,C240 M6, C220 M6, B200 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  **Enabled** , Disabled  |  TPM cannot be disabled unless TXT is disabled.   
Security Device Support |  It controls the entire TPM functionality. |  4.2(3) and later |  C220M6, C240M6, C225M6, C245M6, B200M6, X210c M6, C225 M6, C245 M6, C220 M7, C240 M7, X210c M7, X410c M7, C225 M8, C245 M8, X215c M8,C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  **Enabled** , Disabled  |   
DMA Control Opt-In Flag |  Enabling this token enables Windows 2022 Kernel DMA Protection feature. The OS treats this as a hint that the IOMMU should be enabled to prevent DMA attacks from possible malicious devices.  |  4.2(2) and later |  C220 M6, C240 M6, B200 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  Enabled, **Disabled** |   
LIMIT CPU PA to 46 Bits |  Limits CPU physical address to 46 bits to support the older Hyper-v CPU platform. |  4.2(2) and later |  C220 M6, C240 M6, B200 M6, X210c M6, C220 M7, C240 M7, X210c M7, X410c M7, C220 M8, C240 M8, X210c M8, X410c M8, XE1X0M8  |  **Enabled** , Disabled  |   
SProcessor Epoch 0 |  Allows you to define the SGX EPOCH owner value for the EPOCH number designated by n. |  6.0(1a.0) and later |  C220 M8, C240 M8, X210c M8, X410c M8,XE1X0M8 | Values are: 

  * The Minimum value is 0.
  * The Maximum value is ffffffffffffffff. 
  * The Unit is Hash byte 7-0, 

|   
SProcessor Epoch 1 |  Allows you to define the SGX EPOCH owner value for the EPOCH number designated by n. |  6.0(1a.0) and later |  C220 M8, C240 M8, X210c M8, X410c M8,XE1X0M8 | Values are: 

  * The Minimum value is 0.
  * The Maximum value is ffffffffffffffff. 
  * The Unit is Hash byte 7-0, 

|   
![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

SHA384 PCR Bank Bios token supports PID models UCS-TPM-002D and UCS-TPM-002D-D. 

* * *  
  
---|---

---

## Page 15: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/Intersight/IMM_BIOS_Tokens_Guide/b_IMM_Server_BIOS_Tokens_Guide/m-usb.html

## USB  
  
The following table lists the USB BIOS settings that you can configure through a BIOS policy or the default BIOS settings:

Name |  Description |  Supported Attributes  
---|---|---  
|  |  Versions |  Platforms |  Values |  Dependencies  
Legacy USB Support |  Whether the system supports legacy USB devices. |  4.2(1) and later |  B200 M5, B480 M5, C220 M5, C240 M5, C480 M5, S3260 M5, C240 M6, C220 M6, B200 M6, X210c M6 |  Auto,**Enabled** , Disabled  |   
USB Port Front |  Whether the front panel USB devices are enabled or disabled. |  4.2(1) and later |  C240 M5, C220 M5, C480 M5, B200 M6, X210c M6, X210c M7, X410c M7, X210c M8, X410c M8, XE1X0M8 |  **Enabled** , Disabled  |   
USB Port Internal |  Whether the internal USB devices are enabled or disabled. |  4.2(1) and later |  C240 M5, C220 M5, C480 M5, C220 M6, C240 M6 |  **Enabled** , Disabled  |   
USB Port KVM |  Whether the USB Port KVM devices are enabled or disabled. |  4.2(1) and later |  C240 M5, C220 M5, C480 M5, B200 M6, X210c M6, X210c M7, X410c M7, X210c M8, X410c M8, XE1X0M8 |  **Enabled** , Disabled  |   
USB Port Rear |  Whether the USB port rear devices are enabled or disabled. |  4.2(1) and later |  C240 M5, C220 M5, C480 M5, C220 M6, C240 M6, C220 M7, C240 M7, C220 M8, C240 M8 |  **Enabled** , Disabled  |  |  **Note** |  This is not applicable to XE1X0M8.  
---|---  
USB Port:M.2 Storage |  Whether the SD card drives are enabled or disabled. |  4.2(1) and later |  C220 M5, C240 M5, C480 M5, B200 M6, X210c M6, X210c M7, X410c M7, X210c M8, X410c M8 |  **Enabled** , Disabled  | 

---
