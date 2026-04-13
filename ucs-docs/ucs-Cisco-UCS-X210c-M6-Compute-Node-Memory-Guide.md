# Cisco UCS X210c M6 Compute Node Memory Guide

| | |
|---|---|
| **URL Title** | Cisco UCS X210c M6 Compute Node Memory Guide |
| **URL** | https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-x-series-modular-system/x210c-m6-memory-guide.pdf |
| **Long URL** |  |
| **HTML Title** |  |
| **Source file** | `ucs-docs-raw/pdf/x210c-m6-memory-guide.pdf` |
| **File type** | PDF |
| **Fetched on** | 2026-04-10 12:56:41 |

---

Spec Sheet

Cisco UCS X210c M6 
Compute Node Memory 
Guide

CISCO SYSTEMS
170 WEST TASMAN DR
SAN JOSE, CA, 95134
WWW.CISCO.COM

PUBLICATION HISTORY

REV A.3

MARCH 13, 2023

CONTENTS

Memory Organization   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
Memory Devices (DIMMs and PMem) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
DIMM Guidelines  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
PMem Guidelines   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  10
Memory Modes   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
App Direct Mode   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
Memory Mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
Intel CPU Support   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
Physical Layout   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  13
Recommended DIMM Configurations For Best Performance . . . . . . . . . . . . .  14
Supported DIMM Configurations   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  16
Allowed Memory Configurations   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  19
DRAM-Only Configurations for 3rd Gen Intel® Xeon® Scalable Processors (Ice Lake)  . . . . . . . 19
Mixed DRAM/PMem Configurations for 3rd Gen Intel® Xeon® Scalable Processors (Ice Lake)   . 20
Installing a DIMM or DIMM Blank   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  25

1

Cisco UCS X210c M6 Compute Node Memory Guide

Memory Organization

Memory Organization

The standard memory features are:

Clock speed: 3200 MHz

Ranks per DIMM: 1, 2, 4, or 8

Operational voltage: 1.2 V

Registered ECC DDR4 DIMMS (RDIMMs), Load-reduced DIMMs (LRDIMMs), or Intel® OptaneTM 
Persistent Memory (PMem).

Memory is organized with eight memory channels per CPU, with up to two DIMMs per channel, as 
shown in Figure 1.

Figure 1  Cisco UCS X210c M6 Compute Node Memory Organization

1
t
o
S

l

2
t
o
S

l

A1

A2

B1

B2

Chan A

Chan B

2
t
o
S

l

1
t
o
S

l

A2

A1

B2

B1

Chan A

Chan B

C1

C2

Chan C

Chan C

C2 C1

D1 D2

Chan D

Chan D

D2 D1

E1

E2

F1

F2

G1 G2

H1 H2

CPU 1

CPU 2

Chan E

Chan E

Chan F

Chan F

Chan G

Chan G

E2

E1

F2

F1

G2

G1

H2 H1

Chan H

Chan H

8 memory channels per CPU, 
up to 2 DIMMs per channel
32 DIMMS total (16 DIMMs per CPU) 
8 TB maximum memory (with 256 GB DIMMs)

Cisco UCS X210c M6 Compute Node Memory Guide

3

■
■
■
■
 
 
 
 
Memory Devices (DIMMs and PMem)

Memory Devices (DIMMs and PMem)

The available memory devices are listed in Table 1.

Table 1   Available DDR4 DIMMs and PMem 

Product ID (PID)

PID Description

3200-MHz DIMMS

UCSX-MR-X16G1RW

16 GB RDIMM SRx4 3200 (8Gb)

UCSX-MR-X32G1RW 

32 GB RDIMM SRx4 3200 (16Gb) 

UCSX-MR-X32G2RW

32 GB RDIMM DRx4 3200 (8Gb)

UCSX-MR-X64G2RW

64 GB RDIMM DRx4 3200 (16Gb)

UCSX-ML-128G4RW

128 GB LRDIMM QRx4 3200 (16Gb) (non-3DS)

UCSX-ML-256G8RW1

256 GB LRDIMM 8Rx4 3200 (16Gb) (3DS)

Intel® OptaneTM Persistent Memory (PMem) 

UCSX-MP-128GS-B0

Intel® OptaneTM DC Persistent Memory, 128GB, 3200 MHz

UCSX-MP-256GS-B0

Intel® OptaneTM DC Persistent Memory, 256 GB, 3200 MHz

UCSX-MP-512GS-B0

Intel® OptaneTM DC Persistent Memory, 512 GB, 3200 MHz

Intel® OptaneTM Persistent Memory (PMem) Operational Modes

UCSX-DCPMM-AD

App Direct Mode

UCSX-DCPMM-MM

Memory Mode

Memory Mirroring Option

N01-MMIRROR

Memory mirroring option

Notes:

1. Review the X210c M6 Compute Node Spec Sheet for additional 256GB DIMM usage condition.

Voltage

Ranks
/DIMM

1.2 V

1.2 V

1.2 V

1.2 V

1.2 V 

1.2 V

1

1

2

2

4

8

4

Cisco UCS X210c M6 Compute Node Memory Guide

DIMM Guidelines

DIMM Guidelines

System speed is dependent on the CPU DIMM speed support. Refer to Table 1 on page 4 for 
DIMM speeds.

The servers support the following memory reliability, availability, and serviceability (RAS) 
BIOS options (only one option can be chosen):

— Adaptive Double Device Data Correction (ADDDC) (default)

— Maximum performance

— Full mirroring

— Partial mirroring

DIMM Count Rules:

— Allowed DIMM count for 1-CPU:

• Minimum DIMM count = 1; Maximum DIMM count = 16

• 1, 2, 4, 6, 8, 12, or 16 DIMMs allowed

•  3, 5, 7, 9, 10, 11, 13, 14, 15 DIMMs not allowed.

— Allowed DIMM count for 2-CPUs

• Minimum DIMM count = 2; Maximum DIMM count = 32

• 2, 4, 8, 12, 16, 24, or 32 DIMMs allowed

• 6, 10, 14, 18, 20, 22, 26, 28, 30 DIMMs not allowed.

Mixing Rules:

— Mixing different types of DIMM (RDIMM with any type of LRDIMM or 3DS LRDIMM with 

non-3DS LRDIMM) is not supported within a server.

— Mixing RDIMM with RDIMM types is allowed if they are mixed in same quantities, in a 

balanced configuration.

— Mixing 16 GB, 32 GB, and 64 GB RDIMMs is supported.

— 128 GB and 256 GB LRDIMMs1 cannot be mixed with other RDIMMs

— 128 GB non-3DS LRDIMMs cannot be mixed with 256 GB 3DS LRDIMMs1

— Single-rank DIMMs can be mixed with dual-rank DIMMs in the same channel

— Allowed mixing must be in numbered “pairs” (for example, 8x32 GB and 8x64 GB). 

Such pairs as 10x32 GB and 6x64 GB are not allowed.

— RDIMMs of different sizes can be mixed within a channel. When mixing RDIMMs of 
different densities (sizes), populate DIMMs with the highest density first. For 
example, if you have to mix 32 GB RDIMMs with 16 GB RDIMMs, then populate the 32 
GB DIMMs in blue slots (or slot 1) and then 16 GB DIMMs in black slots (or slot 2).

— Do not mix DIMM types (size, speed, ranks) in a system that uses PMem. In these 

cases, all DIMMs must be the same type and size.

— RDIMMs of different ranks can be mixed within a channel. When mixing RDIMMs with 
different ranks, populate RDIMMs with the higher rank first. For example, when 

Notes

1. Review the X210c M6 Compute Node Spec Sheet for additional 256GB DIMM usage condition.

Cisco UCS X210c M6 Compute Node Memory Guide

5

■
■
■
■
DIMM Guidelines

mixing dual-rank RDIMMs with single-rank RDIMMs populate the dual-rank RDIMMs in 
blue slots first and then single-rank RDIMMs in black slots.

Observe the DIMM mixing rules shown in Table 2

Table 2   DIMM Rules for Cisco UCS X210c M6 Compute Node

DIMM Parameter

DIMM Capacity

RDIMM = 16, 32, 64 GB

LRDIMM = 128, 256 GB2
DIMM Speed 

3200-MHz
DIMM Type

RDIMMs, or LRDIMMs

Notes:

DIMMs in the Same Channel

DIMM in the Same Slot1

DIMMs in the same channel (for 
example, A1 and A2) can have 
different capacities.

For best performance, DIMMs in the 
same slot (for example, A1, B1, C1, 
D1, E1, F1) should have the same 
capacity.

DIMMs will run at the lowest 
speed of the CPU installed

DIMMs will run at the lowest speed 
of the CPU installed

Do not mix LRDIMMs with RDIMMs 
in a channel

Do not mix LRDIMMs with RDIMMs in 
a slot

1. Although different DIMM capacities can exist in the same slot, this will result in less than optimal performance. 

For optimal performance, all DIMMs in the same slot should be identical.

2. Review the X210c M6 Compute Node Spec Sheet for additional 256GB DIMM usage condition.

Population Rules

— Each channel has two memory slots (for example, channel A = slots A1 and A2).

• A channel can operate with one or two DIMMs installed.

• If a channel has only one DIMM, populate slot 1 first (the blue slot).

— When both CPUs are installed, populate the memory slots of each CPU identically. 

Fill the blue slots (slot 1) in the memory channels first according to the 
recommended DIMM populations in Table 3. The table gives the DIMM populations 
for both mirrored and non-mirrored configurations.

Table 3   Cisco UCS X210c M6 Compute Node DIMM Population Order

#DIMMs 
per CPU

Populate CPU1 Slot

Populate CPU2 Slot

Blue Slots

Black slots

Blue slots

Black slots

DIMM Configuration Without Memory Mirroring

1
2
4
6

8

12

16

(A1)
(A1, E1)
(A1, C1); (E1, G1)
(A1, C1); (D1, E1); 
(G1, H1)
(A1, B1); (C1, D1); 
(E1, F1); (G1,H1)
(A1, C1); (D1, E1); 
(G1, H1)
(A1, B1); (C1, D1); 
(E1, F1); (G1, H1)

-
-
-
-

-

(A2, C2); (D2, E2); 
(G2, H2)
(A2, B2); (C2, D2); 
(E2, F2); (G2, H2)

(A1)
(A1, E1)
(A1, C1); (E1, G1)
(A1, C1); (D1, E1); 
(G1, H1)
(A1, B1); (C1, D1); 
(E1, F1); (G1,H1)
(A1, C1); (D1, E1); 
(G1, H1)
(A1, B1); (C1, D1); 
(E1, F1); (G1, H1)

-
-
-
-

-

(A2, C2); (D2, E2); 
(G2, H2)
(A2, B2); (C2, D2); 
(E2, F2); (G2, H2)

DIMM Configuration With Memory Mirroring1

6

Cisco UCS X210c M6 Compute Node Memory Guide

■
DIMM Guidelines

Table 3   Cisco UCS X210c M6 Compute Node DIMM Population Order

8
16

Notes:

(A1, B1); (C1, D1); (E1, F1); (G1,H1)
(A1, B1); (C1, D1); (E1, F1); (G1, H1); (A2,
B2); (C2, D2); (E2, F2); (G2, H2)

(A1, B1); (C1, D1); (E1, F1); (G1,H1)
(A1,  B1);  (C1,  D1);  (E1,  F1);  (G1,  H1);  (A2,
B2); (C2, D2); (E2, F2); (G2, H2)

1. Memory mirroring reduces the amount of memory available by 50 percent because only one of the two 

populated channels provides data. When memory mirroring is enabled, you must install DIMMs in even numbers 
of channels.

Memory Limitations

— The maximum combined memory allowed in the 16 DIMM slots controlled by any one 

CPU is 6 TB (for 8 x 512 GB PMem and 8 x 256 GB DIMMs1).

— The maximum combined memory allowed in the 32 DIMM slots controlled by two 

CPUs is 12 TB (for 16 x 512 GB PMem and 16 x 256 GB DIMMs1).

For best performance, observe the following:

— For optimum performance, populate at least one DIMM per memory channel per 

CPU. When one DIMM is used, it must be populated in DIMM slot 1 (blue slot farthest 
away from the CPU) of a given channel.

— For populations of 1 DIMM per channel (DPC) and 2DPC, all supported DIMMs on Cisco 
UCS M6 servers run at their labeled speed provided the processor supports that 
speed.

— When populating DIMM slots for optimal performance, multiples of 16 DIMMs are 
best because there are 8 memory channels per CPU socket and 2-CPUs must be 
populated.

— At the same memory speed, 2 DPC may perform slightly better than 1 DPC for 

RDIMMs (workload dependent).

— For optimum performance, use dual rank RDIMMs preferably, then single rank 

RDIMMs, and lastly LRDIMMs. Larger size LRDIMMs provide large capacity memory 
configurations but the performance of these DIMMs is lower than standard RDIMMs.

— For small to medium memory capacities, whenever possible, install dual rank 

RDIMMs for optimal performance. Dual rank RDIMMs perform better than single rank 
RDIMMs. Single rank DIMMs limit the performance of memory-intensive workloads in 
1 DIMM per channel configurations.

— 256 GB RDIMMs1 should be used for the largest memory capacity requirement. These 
DIMMs provide the maximum memory size supported for 2-socket UCS M6 servers.

DIMMs for both CPUs must always be configured identically

All DIMMs must be DDR4 DIMMs that support ECC. Non-buffered UDIMMs and non-ECC DIMMs 
are not supported.

Notes

1. Review the X210c M6 Compute Node Spec Sheet for additional 256GB DIMM usage condition.

Cisco UCS X210c M6 Compute Node Memory Guide

7

■
■
■
■
DIMM Guidelines

Cisco memory from previous generation servers (DDR3 and DDR4) is not supported with the 
Cisco UCS X210c M6 Compute Node.

NOTE:  System performance is optimized when the DIMM type and quantity are equal 
for both CPUs, and when all channels are filled equally across the CPUs in the server.

8

Cisco UCS X210c M6 Compute Node Memory Guide

■
DIMM Guidelines

Table 4 shows the Cisco-supported all-DIMM configurations. These configurations are a subset of the 
Intel-supported configurations.

Table 4   3rd Gen Intel® Xeon® Scalable Processors (Ice Lake) All DIMM Physical Configuration

DIMM + 
PMem 
Count

CPU 1 or CPU 2

ICX: IMC2

ICX: IMC3

ICX: IMC1

ICX: IMC0

Chan 0 (F)

Chan 1 (E)

Chan 0 (H)

Chan 1 (G)

Chan 0 (C)

Chan 1 (D)

Chan 0 (A)

Chan 1 (B)

Slot 
1

Slot 
2

Slot 
1

Slot 
2

Slot 
1

Slot 
2

Slot 
1

Slot 
2

Slot 
2

Slot 
1

Slot 
2

Slot 
1

Slot 
2

Slot 
1

Slot 
2

Slot 
1

1 + 0

2 + 0

4 + 0

6 + 0

8 + 0

DIMM

DIMM

DIMM

DIMM

DIMM

DIMM

DIMM

DIMM

DIMM

DIMM

DIMM

DIMM

DIMM

DIMM

DIMM

DIMM

DIMM

DIMM

DIMM

DIMM

DIMM

12 + 0

DIMM DIMM DIMM DIMM DIMM DIMM DIMM DIMM DIMM DIMM DIMM DIMM

16 + 0

DIMM DIMM DIMM DIMM DIMM DIMM DIMM DIMM DIMM DIMM DIMM DIMM DIMM DIMM DIMM DIMM

Cisco UCS X210c M6 Compute Node Memory Guide

9

PMem Guidelines

PMem Guidelines

All installed PMem must be the same size. Mixing PMem of different capacities is not supported.

When PMem are installed, all DIMMs installed must be identical (same speed, size and ranks).

PMem and DIMMs must be populated as shown in Table 5.

NOTE:  In Table 5, all DIMMs must be identical to each other and all PMem must also 
be identical to each other. The table shows the Cisco-supported configurations (it is 
a subset of the Intel-supported configurations).

Table 5   3rd Gen Intel® Xeon® Scalable Processors (Ice Lake) DIMM and PMem1 Physical Configuration

DIMM + 
PMem 
Count

CPU 1 or CPU 2

ICX: IMC2

ICX: IMC3

ICX: IMC1

ICX: IMC0

Chan 0 (F)

Chan 1 (E)

Chan 0 (H

Chan 1 (G)

Chan 0 (C)

Chan 1 (D)

Chan 0 (A)

Chan 1 (B)

Slot 
1

Slot 
2

Slot 
1

Slot 
2

Slot 
1

Slot 
2

Slot 
1

Slot 
2

Slot 
2

Slot 
1

Slot 
2

Slot 
1

Slot 
2

Slot 
1

Slot 
2

Slot 
1

4 + 42

PMem

8 + 13

DIMM

DIMM

DIMM

PMem

DIMM

DIMM

DIMM

DIMM

DIMM

PMem

DIMM

PMem

DIMM PMem DIMM

8 + 44

DIMM

DIMM PMem DIMM

DIMM PMem PMem DIMM

DIMM PMem DIMM

8 + 85

DIMM PMem DIMM PMem DIMM PMem DIMM PMem PMem DIMM PMem DIMM PMem DIMM PMem DIMM

NOTE: AD = App Direct Mode, MM = Memory Mode

Notes:

1. All systems must be fully populated with two CPUs when using PMem at this time.
2. AD, MM
3. AD
4. AD, MM
5. AD, MM

Two CPUs must be installed when using PMem.For each memory channel with both a PMem and a 
DIMM installed, the PMem is installed in channel slot 2 (black slot closest to the CPU) and the DIMM is 
installed in channel slot 1 (blue slot farthest from CPU).

To maximize performance, balance all memory channels

For best memory performance, use identical DIMM and PMem types within a server (same speed, size 

and ranks).

In configurations with PMem installed, memory mirroring is supported, with two restrictions: 

Mirroring is only enabled on the DIMMs installed in the server; the PMem themselves do not 
support mirroring.

Only App Direct mode is supported. Memory mirroring cannot be enabled when PMem are in 
Memory Mode.

10

Cisco UCS X210c M6 Compute Node Memory Guide

DIMM

DIMM

■
■
■
■
■
■
■
■
■
PMem Guidelines

Memory sparing is not supported with PMem installed.

Memory Modes

The Ice Lake CPUs support two memory modes:

App Direct Mode

Memory Mode

App Direct Mode

PMem operates as a solid-state disk storage device. Data is saved and is non-volatile. Both DCPMM and DIMM 
capacities count towards the CPU capacity limit.

For example, if App Direct mode is configured and the DIMM sockets for a CPU are populated with 8 x 256 
GB DRAMs1 (2 TB total DRAM) and 8 x 512 GB PMem (4 TB total PMem), then 6 TB total counts towards the 
CPU capacity limit.

Memory Mode

PMem operates as a 100% memory module. Data is volatile and DRAM acts as a cache for PMem. Only the 
PMem capacity counts towards the CPU capacity limit. This is the factory default mode.

For example, if Memory mode is configured and the DIMM sockets for a CPU are populated with 8 x 256 GB 
DRAMs1 (2 TB total DRAM) and 8 x 512 GB PMem (4 TB total PMem), then only 4 TB total (the PMem memory) 
counts towards the CPU capacity limit. All of the DRAM capacity (2 TB) is used as cache and does not factor 
into CPU capacity. The recommended Intel DRAM:PMem ratio for Memory Mode is from 1:4, 1:8 and 1:16.

Notes

1. Review the X210c M6 Compute Node Spec Sheet for additional 256GB DIMM usage condition.

Cisco UCS X210c M6 Compute Node Memory Guide

11

■
■
■
PMem Guidelines

Intel CPU Support

For 3rd Generation Intel® Xeon® Scalable Processors (Ice Lake):

DRAMs and PMem are supported

Each CPU has 16 DIMM sockets and supports the following maximum memory capacities:

4 TB using 16 x 256 GB DRAMs1 or

6 TB using 8 x 256 GB DRAMs1 and 8 x 512 GB Persistent Memory Modules (PMem)

Only the following mixed DRAM/PMem memory configurations are supported per CPU socket:

4 DRAMs and 4 PMem, or

8 DRAMs and 4 PMem, or

8 DRAMs and 1 PMem, or

8 DRAMs and 8 PMem

The available DRAM capacities are 16 GB, 32 GB, 64 GB, 128 GB, or 256 GB1.

The available PMem capacities are 128 GB, 256 GB, or 512 GB.

Notes

1. Review the X210c M6 Compute Node Spec Sheet for additional 256GB DIMM usage condition.

12

Cisco UCS X210c M6 Compute Node Memory Guide

■
■
■
■
■
■
■
■
Physical Layout

Physical Layout

Each CPU has eight memory channels:

CPU1 has channels A, B, C, D, E, F, G and H

CPU2 has channels A, B, C, D, E, F, G and H

Each memory channel has two slots: slot 1 and slot 2. The blue-colored slots are for slot 1 and the black 
slots for slot 2.

As an example, slots A1, B1, C1, D1, E1, F1, G1, and H1 belong to slot 1, while A2, B2, C2, D2, E2, F2, G2 
and H2 belong to slot 2.

Figure 2 show how slots and channels are physically laid out on the motherboards for the servers. Each CPU 
has channels A, B, C, D, E, F, G, and H. The slot 1 (blue) slots are always located farther away from a CPU 
than the corresponding slot 2 (black) slots. Slot 1 slots (blue) are populated before slot 2 slots (black).

Figure 2  Physical Layout of Cisco UCS X210c M6 Compute Node CPU Memory Channels and Slots

P1 F1

P1 F2

P1 E1

P1 E2

P1 H1

P1 H2

P1 G1

P1 G2

P1 C2

P1 C1

P1 D2

P1 D1

P1 A2

P1 A1

P1 B2

P1 B1

P2 B1

P2 B2

P2 A1

P2 A2

P2 D1

P2 D2

P2 C1

P2 C2

P2 G2

P2 G1

P2 H2

P2 H1

P2 E2

P2 E1

P2 F2

P2 F1

Cisco UCS X210c M6 Compute Node Memory Guide

13

■
■
Recommended DIMM Configurations For Best Performance

Recommended DIMM Configurations For Best Performance 

This section explains the recommended DIMM population order rules for best performance. Table 6 shows 
the recommended configurations for 3rd Gen Intel® Xeon® Scalable Processors (Ice Lake). The rows 
highlighted in yellow indicate configurations with optimum performance.

Table 6   Recommended Memory Configurations for 3rd Gen Intel® Xeon® Scalable Processors (Ice Lake) 

For Best Performance

CPU-1

CPU-2

Total System 
Memory Size

Blue Slots 

Black Slots

Blue Slots

Black Slots 

Bank 1

Bank 2

Bank 1

Bank 2

DIMM Type

Total DIMMs in 
the system

(A1,B1,C1,D1,
E1, F1,G1,H1)

(A2, B2, C2, D2, 
E2, F2,G2,H2)

(A1,B1,C1,D1,
E1, F1,G1,H1)

(A2, B2, C2, D2, 
E2, F2,G2,H2)

256 GB

8x16 GB

-

8x16 GB

-

512 GB

8x16 GB

8x16 GB

8x16 GB

8x16 GB

512 GB

8x32 GB

-

8x32 GB

-

768 GB

8x32 GB

8x16 GB

8x32 GB

8x16 GB

1024 GB

8x32 GB

8x32 GB

8x32 GB

8x32 GB

1024 GB

8x64 GB

-

8x64 GB

-

1280 GB

8x64 GB

8x16 GB

8x64 GB

8x16 GB

1536 GB

8x64 GB

8x32 GB

8x64 GB

8x32 GB

2048 GB

8x64 GB

8x64 GB

8x64 GB

8x64 GB

2048 GB

8x128 GB

-

8x128 GB

-

4096 GB

8x128 GB

8x128 GB

8x128 GB

8x128 GB

4096 GB1

8x256 GB

-

8x256 GB

-

8192 GB1

8x256 GB

8x256 GB

8x256 GB

8x256 GB

Notes:

1. Review the X210c M6 specsheet for additional 256GB DIMM usage condition.

R

R

R

R

R

R

R

R

R

LR

LR

LR

LR

16

32

16

32

32

16

32

32

32

16

32

16

32

14

Cisco UCS X210c M6 Compute Node Memory Guide

Recommended DIMM Configurations For Best Performance

NOTE:  

This Table 6 lists only best recommended memory configurations based on memory 
performance data.

Yellow Highlighted Cells represent Sweet Spot configurations for achieving optimum 
performance in a system.

These memory configurations will yield the best performance since the memory is 
populated equally for both the CPUs across all the eight memory channels. 

The recommendations of Table 6 are based on memory performance measurements, done 
for a X210c M6 configured with two 3rd Generation Intel Xeon Scalable 8380 processors. 

32GB dual rank and 64GB dual rank RDIMMs provide the highest memory bandwidth at 1 DPC 
and 2 DPC.

Among all mixing configurations, 8x32 GB + 8x64 GB mix per CPU (1536 GB total system 
capacity for 2-sockets) provides the highest memory bandwidth.

128 GB LRDIMMs with up to 4096 GB total system capacity for 2-Sockets, and 256 GB1 
LRDIMMs with up to 8192 GB total system capacity for 2-Sockets provide the largest memory 
capacities. Note: these LRDIMMs cannot be mixed with any RDIMMs;

Notes:

1. Review the X210c M6 specsheet for additional 256GB DIMM usage condition.

Cisco UCS X210c M6 Compute Node Memory Guide

15

■
■
■
■
■
■
■
Supported DIMM Configurations

Supported DIMM Configurations

Table 7 below show some (not all) of the alternative DIMM configurations for configurations with 1, 2, 4, 6, 
8, 12, and 16 DIMMs per CPU. The only DIMM mixing allowed is:

16 GB and 32 GB RDIMMS

16 GB and 64 GB RDIMMs

32 GB and 64 GB RDIMMs

DIMM mixing configurations are shown at the end of Table 7.

Table 7   Supported Memory Configurations for 3rd Gen Intel® Xeon® Scalable Processors (Ice Lake)

CPU-1

CPU-2

Total 
System 
Memory 
Size

Blue Slots 

Black Slots

Blue Slots

Black Slots 

Bank 1

Bank2

Bank 1

Bank 2

DIMM 
Type

Total DIMMs in 
the system

(A1,B1,C1,D1,
E1, F1, G1, H1)

(A2, B2, C2, D2 
E2, F2, G2, H2)

(A1,B1,C1,D1,
E1, F1, G1, H1)

(A2, B2, C2, D2 
E2, F2, G2, H2)

16 GB RDIMMs

32 GB

64 GB

1x16 GB

2x16 GB

128 GB

4x16 GB

192 GB

6x16 GB

256 GB

8x16 GB

-

-

-

-

-

1x16 GB

2x16 GB

4x16 GB

6x16 GB

8x16 GB

-

-

-

-

-

384 GB

6x16GB

6x16 GB

6x16 GB

6x16 GB

512 GB

8x16 GB

8x16 GB

8x16 GB

8x16 GB

32 GB RDIMMs

64 GB

1x32 GB

128 GB

2x32 GB

256 GB

4x32 GB

384 GB

6x32 GB

512 GB

8x32 GB

-

-

-

-

-

1x32 GB

2x32 GB

4x32 GB

6x32 GB

8x32 GB

-

-

-

-

-

768 GB

6x32 GB

6x32 GB

6x32 GB

6x32 GB

1024 GB

8x32 GB

8x32 GB

8x32 GB

8x32 GB

R

R

R

R

R

R

R

R

R

R

R

R

R

R

2

4

8

12

16

24

32

2

4

8

12

16

24

32

16

Cisco UCS X210c M6 Compute Node Memory Guide

■
■
■
Supported DIMM Configurations

Table 7   Supported Memory Configurations for 3rd Gen Intel® Xeon® Scalable Processors (Ice Lake) 

CPU-1

CPU-2

Total 
System 
Memory 
Size

Blue Slots 

Black Slots

Blue Slots

Black Slots 

Bank 1

Bank2

Bank 1

Bank 2

DIMM 
Type

Total DIMMs in 
the system

(A1,B1,C1,D1,
E1, F1, G1, H1)

(A2, B2, C2, D2 
E2, F2, G2, H2)

(A1,B1,C1,D1,
E1, F1, G1, H1)

(A2, B2, C2, D2 
E2, F2, G2, H2)

64 GB RDIMMs

128 GB

1x64 GB

256 GB

2x64 GB

512 GB

4x64 GB

768 GB

6x64 GB

1024 GB

8x64 GB

-

-

-

-

-

1x64 GB

2x64 GB

4x64 GB

6x64 GB

8x64 GB

-

-

-

-

-

1536 GB

6x64 GB

6x64 GB

6x64 GB

6x64 GB

2048 GB

8x64 GB

8x64 GB

8x64 GB

8x64 GB

128 GB LRDIMMs

256 GB

1x128 GB

512 GB

2x128 GB

1024 GB

4x128 GB

1536 GB

6x128 GB

2048 GB

8x128 GB

-

-

-

-

-

1x128 GB

2x128 GB

4x128 GB

6x128 GB

8x128 GB

-

-

-

-

-

3072 GB

6x128 GB

6x128 GB

6x128 GB

6x128 GB

4096 GB

8x128 GB

8x128 GB

8x128 GB

8x128 GB

256 GB LRDIMMs1

512 GB

1x256 GB

1024 GB

2x256 GB

2048 GB

4x256 GB

3072 GB

6x256 GB

4096 GB

8x256 GB

-

-

-

-

-

1x256 GB

2x256 GB

4x256 GB

6x256 GB

8x256 GB

-

-

-

-

-

6144 GB1

6x256 GB

6x256 GB

6x256 GB

6x256 GB

R

R

R

R

R

R

R

LR

LR

LR

LR

LR

LR

LR

LR

LR

LR

LR

LR

LR

2

4

8

12

16

24

32

2

4

8

12

16

24

32

2

4

8

12

16

24

Cisco UCS X210c M6 Compute Node Memory Guide

17

Supported DIMM Configurations

Table 7   Supported Memory Configurations for 3rd Gen Intel® Xeon® Scalable Processors (Ice Lake) 

CPU-1

CPU-2

Total 
System 
Memory 
Size

Blue Slots 

Black Slots

Blue Slots

Black Slots 

Bank 1

Bank2

Bank 1

Bank 2

DIMM 
Type

Total DIMMs in 
the system

(A1,B1,C1,D1,
E1, F1, G1, H1)

(A2, B2, C2, D2 
E2, F2, G2, H2)

(A1,B1,C1,D1,
E1, F1, G1, H1)

(A2, B2, C2, D2 
E2, F2, G2, H2)

8192 GB1

8x256 GB

8x256 GB

8x256 GB

8x256 GB

LR

16GB RDIMMs + 32GB RDIMMs

576 GB

6x16 GB

6x32 GB

6x16 GB

6x32 GB

768 GB

8x16 GB

8x32 GB

8x16 GB

8x32 GB

16GB RDIMMs + 64GB RDIMMs

960 GB

6x16 GB

6x64 GB

6x16 GB

6x64 GB

1280 GB

8x16 GB

8x64 GB

8x16 GB

8x64 GB

32GB RDIMMs + 64GB RDIMMs

1152 GB

6x32 GB

6x64 GB

6x32 GB

6x64 GB

1536 GB

8x32 GB

8x64 GB

8x32 GB

8x64 GB

Notes:

1. Review the X210c M6 spec sheet for additional 256GB DIMM usage condition.

R

R

R

R

R

R

32

24

32

24

32

24

32

NOTE:  1-CPU configuration, with identical mix of DIMMs as 2-CPUs shown on Table 7 
above, is possible but not recommended for performance reason.

18

Cisco UCS X210c M6 Compute Node Memory Guide

Allowed Memory Configurations

Allowed Memory Configurations

This following material describes the configurable memory capacities using DRAMS only or mixes of DRAMs 
and PMem for 3rd Gen Intel® Xeon® Scalable Processors (Ice Lake) used in X210c M6 servers.

DRAM-Only Configurations for 3rd Gen Intel® Xeon® Scalable Processors 
(Ice Lake)

Table 8 shows the possible configurations for 3rd Gen Intel® Xeon® Scalable Processors (Ice Lake) 
populated with all DIMMs.

Table 8    All DRAM Memory Allowed Configurations (per CPU)

Capacity Per DIMM (GB)

Number of DIMMs 
per CPU

16

32

64

128

2561

Total Capacity per CPU (GB)

1

2

4

6

8

12

16

Notes:

16

32

64

96

128

192

2561

32

64

128

192

256

384

512

64

128

256

384

512

768

1024

128

256

512

768

1024

1536

2048

256

512

1024

1536

2048

3072

4096

1. Review the X210c M6 specsheet for additional 256GB DIMM usage condition.

Cisco UCS X210c M6 Compute Node Memory Guide

19

Allowed Memory Configurations

Mixed DRAM/PMem Configurations for 3rd Gen Intel® Xeon® Scalable 
Processors (Ice Lake)

When PMem are selected, there are several allowable combinations of DRAMs and PMem per CPU as shown 
in Table 5 on page 10 and Table 9:

Table 9   Mixed DIMM/PMem Allowed Configurations (per CPU)

Number of DRAMs per CPU

Number of PMem per CPU

4

8

81
8

4

4

11
8

Notes:

1. The 8:1 DRAM:PMem ratio is valid for App Direct mode only.

Selection of PMem also requires that all CPUs be fully populated. The rules of mixed DIMM and PMem 
configurations are as follows.

Only the number of DIMMs and PMem allowed per CPU are as shown in Table 9.

All PMem must be equal in size

All DIMMs must be equal in size and type

For the App Direct Mode, both DCPMM and DIMM capacities count towards the CPU capacity limit

For the Memory Mode only the PMem capacity counts towards the CPU capacity limit. DIMMs are 
used for cache only and do not counts toward the CPU capacity limit.

20

Cisco UCS X210c M6 Compute Node Memory Guide

■
■
■
■
■
Table 10 through Table 13 show all the possible combinations of DRAMs and PMem possible in each of the 
four supported DRAM/PMem 2-CPU mixed configurations.

Allowed Memory Configurations

2-CPU Configuration

DRAM

PMem

8

8

Table 10  2-CPU Mixed Configuration: (8xDRAMs + 8xPMem)

CPU1

CPU2

Total System (2-CPUs)
Memory Capacity1

DRAM
N#

DRAM 
Capacity
2

Total 
DRAM
Capacity

PMem
N#

PMem
Capacity

Total 
PMem 
Capacity

DRAM
N#

DRAM 
Capacity
2

Total 
DRAM
Capacity

PMem
N#

PMem
Capacity

Total 
PMem 
Capacity

DRAM:
PMem
Ratio

Memory 
Mode

App 
Direct 
Mode

PMem Capacity: 128GB

PMem Capacity: 128GB

PMem Capacity: 128GB

4

4

4

4

4

4

4

4

4

4

4

4

4

4

4

16 GB

64 GB

32 GB

128 GB

64 GB

256 GB

128 GB 512 GB

256 GB 1024 GB

4

4

4

4

4

128 GB 512 GB

128 GB 512 GB

128 GB 512 GB

128 GB 512 GB

128 GB 512 GB

PMem Capacity: 256GB

16 GB

64 GB

32 GB

128 GB

64 GB

256 GB

128 GB 512 GB

256 GB 1024 GB

4

4

4

4

4

256 GB 1024 GB

256 GB 1024 GB

256 GB 1024 GB

256 GB 1024 GB

256 GB 1024 GB

PMem Capacity: 512GB

16 GB

64 GB

32 GB

128 GB

64 GB

256 GB

128 GB 512 GB

256 GB 1024 GB

4

4

4

4

4

512 GB 2048 GB

512 GB 2048 GB

512 GB 2048 GB

512 GB 2048 GB

512 GB 2048 GB

4

4

4

4

4

4

4

4

4

4

4

4

4

4

4

16 GB

64 GB

32 GB

128 GB

64 GB

256 GB

128 GB

512 GB

256 GB 1024 GB

4

4

4

4

4

128 GB

512 GB

128 GB

512 GB

128 GB

512 GB

128 GB

512 GB

128 GB

512 GB

1:8

1:4

1:2

1:1

2:1

1024 GB 1152 GB

1024 GB 1280 GB

N/A

N/A

N/A

1536 GB

2048 GB

3072 GB

PMem Capacity: 256GB

PMem Capacity: 256GB

16 GB

64 GB

32 GB

128 GB

64 GB

256 GB

128 GB

512 GB

256 GB 1024 GB

4

4

4

4

4

256 GB 1024 GB

1:16

2048 GB 2176 GB

256 GB 1024 GB

256 GB 1024 GB

256 GB 1024 GB

256 GB 1024 GB

1:8

1:4

1:2

1:1

2048 GB 2304 GB

2048 GB 2560 GB

N/A

N/A

3072 GB

4096 GB

PMem Capacity: 512GB

PMem Capacity: 512GB

16 GB

64 GB

32 GB

128 GB

64 GB

256 GB

128 GB

512 GB

256 GB 1024 GB

4

4

4

4

4

512 GB 2048 GB

1:32

N/A

4224 GB

512 GB 2048 GB

1:16

4096 GB 4352 GB

512 GB 2048 GB

512 GB 2048 GB

512 GB 2048 GB

1:8

1:4

1:2

4096 GB 4608 GB

4096 GB 5120 GB

N/A

6144 GB

Notes:

1. Red cells represent the unsupported configurations and ratio for Memory Mode.
2. Review the X210c M6 specsheet for additional 256GB DIMM usage condition.

Cisco UCS X210c M6 Compute Node Memory Guide

21

Allowed Memory Configurations

2-CPU Configuration

DRAM

PMem

16

8

Table 11  2-CPU Mixed Configuration: (16xDRAMs + 8xPMem)

CPU1

CPU2

Total System (2-CPUs)
Memory Capacity1

DRAM
N#

DRAM 
Capacity
2

Total 
DRAM
Capacity

PMem
N#

PMem
Capacity

Total 
PMem 
Capacity

DRAM
N#

DRAM 
Capacity
2

Total 
DRAM
Capacity

PMem
N#

PMem
Capacity

Total 
PMem 
Capacity

DRAM:
PMem
Ratio

Memory 
Mode

App 
Direct 
Mode

PMem Capacity: 128GB

PMem Capacity: 128GB

PMem Capacity: 128GB

8

8

8

8

8

8

8

8

8

8

8

8

8

8

8

16 GB

128 GB

32 GB

256 GB

64 GB

512 GB

128 GB 1024 GB

256 GB 2048 GB

4

4

4

4

4

128 GB 512 GB

128 GB 512 GB

128 GB 512 GB

128 GB 512 GB

128 GB 512 GB

PMem Capacity: 256GB

16 GB

128 GB

32 GB

256 GB

64 GB

512 GB

128 GB 1024 GB

256 GB 2048 GB

4

4

4

4

4

256 GB 1024 GB

256 GB 1024 GB

256 GB 1024 GB

256 GB 1024 GB

256 GB 1024 GB

PMem Capacity: 512GB

16 GB

128 GB

32 GB

256 GB

64 GB

512 GB

128 GB 1024 GB

256 GB 2048 GB

4

4

4

4

4

512 GB 2048 GB

512 GB 2048 GB

512 GB 2048 GB

512 GB 2048 GB

512 GB 2048 GB

8

8

8

8

8

8

8

8

8

8

8

8

8

8

8

16 GB

128 GB

32 GB

256 GB

64 GB

512 GB

128 GB 1024 GB

256 GB 2048 GB

4

4

4

4

4

128 GB

512 GB

128 GB

512 GB

128 GB

512 GB

128 GB

512 GB

128 GB

512 GB

1:4

1:2

1:1

2:1

4:1

1024 GB 1280 GB

N/A

N/A

N/A

N/A

1536 GB

2048 GB

3072 GB

5120 GB

PMem Capacity: 256GB

PMem Capacity: 256GB

16 GB

128 GB

32 GB

256 GB

64 GB

512 GB

128 GB 1024 GB

256 GB 2048 GB

4

4

4

4

4

256 GB 1024 GB

256 GB 1024 GB

256 GB 1024 GB

256 GB 1024 GB

256 GB 1024 GB

1:8

1:4

1:2

1:1

2:1

2048 GB 2304 GB

2048 GB 2560 GB

N/A

N/A

N/A

3072 GB

4096 GB

6144 GB

PMem Capacity: 512GB

PMem Capacity: 512GB

16 GB

128 GB

32 GB

256 GB

64 GB

512 GB

128 GB 1024 GB

256 GB 2048 GB

4

4

4

4

4

512 GB 2048 GB

1:16

4096 GB 4352 GB

512 GB 2048 GB

512 GB 2048 GB

512 GB 2048 GB

512 GB 2048 GB

1:8

1:4

1:2

1:1

4096 GB 4608 GB

4096 GB 5120 GB

N/A

N/A

6144 GB

8192 GB

Notes:

1. Red cells represent the unsupported configurations and ratio for Memory Mode.
2. Review the X210c M6 specsheet for additional 256GB DIMM usage condition.

22

Cisco UCS X210c M6 Compute Node Memory Guide

Allowed Memory Configurations

2-CPU Configuration

DRAM

PMem

16

2

Table 12  2-CPU Mixed Configuration: (16xDRAMs + 2xPMem)

CPU1

CPU2

Total System (2-CPUs)
Memory Capacity1

DRAM
N#

DRAM 
Capacity
2

Total 
DRAM
Capacity

PMem
N#

PMem
Capacity

Total 
PMem 
Capacity

DRAM
N#

DRAM 
Capacity
2

Total 
DRAM
Capacity

PMem
N#

PMem
Capacity

Total 
PMem 
Capacity

DRAM:
PMem
Ratio

Memory 
Mode

App 
Direct 
Mode

PMem Capacity: 128GB

PMem Capacity: 128GB

PMem Capacity: 128GB

8

8

8

8

8

8

8

8

8

8

8

8

8

8

8

16 GB

128 GB

32 GB

256 GB

64 GB

512 GB

128 GB 1024 GB

256 GB 2048 GB

1

1

1

1

1

128 GB 128 GB

128 GB 128 GB

128 GB 128 GB

128 GB 128 GB

128 GB 128 GB

PMem Capacity: 256GB

16 GB

128 GB

32 GB

256 GB

64 GB

512 GB

128 GB 1024 GB

256 GB 2048 GB

1

1

1

1

1

256 GB 256 GB

256 GB 256 GB

256 GB 256 GB

256 GB 256 GB

256 GB 256 GB

PMem Capacity: 512GB

16 GB

128 GB

32 GB

256 GB

64 GB

512 GB

128 GB 1024 GB

256 GB 2048 GB

1

1

1

1

1

512 GB 512 GB

512 GB 512 GB

512 GB 512 GB

512 GB 512 GB

512 GB 512 GB

8

8

8

8

8

8

8

8

8

8

8

8

8

8

8

16 GB

128 GB

32 GB

256 GB

64 GB

512 GB

128 GB 1024 GB

256 GB 2048 GB

1

1

1

1

1

128 GB

128 GB

128 GB

128 GB

128 GB

128 GB

128 GB

128 GB

128 GB

128 GB

N/A

N/A

N/A

N/A

N/A

N/A

N/A

N/A

N/A

N/A

512 GB

768 GB

1280 GB

2304 GB

4352 GB

PMem Capacity: 256GB

PMem Capacity: 256GB

16 GB

128 GB

32 GB

256 GB

64 GB

512 GB

128 GB 1024 GB

256 GB 2048 GB

1

1

1

1

1

256 GB

256 GB

256 GB

256 GB

256 GB

256 GB

256 GB

256 GB

256 GB

256 GB

N/A

N/A

N/A

N/A

N/A

N/A

N/A

N/A

N/A

N/A

768 GB

1024 GB

1536 GB

2560 GB

4608 GB

PMem Capacity: 512GB

PMem Capacity: 512GB

16 GB

128 GB

32 GB

256 GB

64 GB

512 GB

128 GB 1024 GB

256 GB 2048 GB

1

1

1

1

1

512 GB

512 GB

512 GB

512 GB

512 GB

512 GB

512 GB

512 GB

512 GB

512 GB

N/A

N/A

N/A

N/A

N/A

N/A

N/A

N/A

N/A

N/A

1280 GB

1536 GB

2048 GB

3072 GB

5120 GB

Notes:

1. Red cells represent the unsupported configurations and ratio for Memory Mode.
2. Review the X210c M6 specsheet for additional 256GB DIMM usage condition.

Cisco UCS X210c M6 Compute Node Memory Guide

23

Allowed Memory Configurations

2-CPU Configuration

DRAM

PMem

16

16

Table 13  2-CPU Mixed Configuration: (16xDRAMs + 16xPMem)

CPU1

CPU2

Total System (2-CPUs)
Memory Capacity1

DRAM
N#

DRAM 
Capacity
2

Total 
DRAM
Capacity

PMem
N#

PMem
Capacity

Total 
PMem 
Capacity

DRAM
N#

DRAM 
Capacity
2

Total 
DRAM
Capacity

PMem
N#

PMem
Capacity

Total 
PMem 
Capacity

DRAM:
PMem
Ratio

Memory 
Mode

App 
Direct 
Mode

PMem Capacity: 128GB

PMem Capacity: 128GB

PMem Capacity: 128GB

8

8

8

8

8

8

8

8

8

8

8

8

8

8

8

16 GB

128 GB

32 GB

256 GB

64 GB

512 GB

128 GB 1024 GB

256 GB 2048 GB

8

8

8

8

8

128 GB 1024 GB

128 GB 1024 GB

128 GB 1024 GB

128 GB 1024 GB

128 GB 1024 GB

PMem Capacity: 256GB

16 GB

128 GB

32 GB

256 GB

64 GB

512 GB

128 GB 1024 GB

256 GB 2048 GB

8

8

8

8

8

256 GB 2048 GB

256 GB 2048 GB

256 GB 2048 GB

256 GB 2048 GB

256 GB 2048 GB

PMem Capacity: 512GB

16 GB

128 GB

32 GB

256 GB

64 GB

512 GB

128 GB 1024 GB

256 GB 2048 GB

8

8

8

8

8

512 GB 4096 GB

512 GB 4096 GB

512 GB 4096 GB

512 GB 4096 GB

512 GB 4096 GB

8

8

8

8

8

8

8

8

8

8

8

8

8

8

8

16 GB

128 GB

32 GB

256 GB

64 GB

512 GB

128 GB 1024 GB

256 GB 2048 GB

8

8

8

8

8

128 GB 1024 GB

128 GB 1024 GB

128 GB 1024 GB

128 GB 1024 GB

128 GB 1024 GB

1:8

1:4

1:2

1:1

2:1

2048 GB 2304 GB

2048 GB 2560 GB

N/A

N/A

N/A

3072 GB

4096 GB

6144 GB

PMem Capacity: 256GB

PMem Capacity: 256GB

16 GB

128 GB

32 GB

256 GB

64 GB

512 GB

128 GB 1024 GB

256 GB 2048 GB

8

8

8

8

8

256 GB 2048 GB

1:16

4096 GB 4352 GB

256 GB 2048 GB

256 GB 2048 GB

256 GB 2048 GB

256 GB 2048 GB

1:8

1:4

1:2

1:1

4096 GB 4608 GB

4096 GB 5120 GB

N/A

N/A

6144 GB

8192 GB

PMem Capacity: 512GB

PMem Capacity: 512GB

16 GB

128 GB

32 GB

256 GB

64 GB

512 GB

128 GB 1024 GB

256 GB 2048 GB

8

8

8

8

8

512 GB 4096 GB

1:32

N/A

8448 GB

512 GB 4096 GB

1:16

8192 GB 8704 GB

512 GB 4096 GB

512 GB 4096 GB

512 GB 4096 GB

1:8

1:4

1:2

8192 GB 9216 GB

8192 GB 10240 GB

N/A

12288 GB

Notes:

1. Red cells represent the unsupported configurations and ratio for Memory Mode.
2. Review the X210c M6 specsheet for additional 256GB DIMM usage condition.

NOTE:  All 3rd Generation Intel® Xeon® Scalable Processors (Ice Lake) support PMem 
products, except 4309Y, 4310, 4310T, and 4316 processors.

24

Cisco UCS X210c M6 Compute Node Memory Guide

Installing a DIMM or DIMM Blank

Installing a DIMM or DIMM Blank

To install a DIMM or a DIMM blank into a slot on the blade server, follow these steps. 

Procedure

Step 1 Open both DIMM connector latches.

Step 2 Press evenly on both ends of the DIMM until it clicks into place in its slot

Note: Ensure that the notch in the DIMM aligns with the slot. If the notch is misaligned, it is 

possible to damage the DIMM, the slot, or both.

Step 3 Press the DIMM connector latches inward slightly to seat them fully.

Step 4 Populate all slots with a DIMM or DIMM blank. A slot cannot be empty.

Figure 3  Installing Memory

2

1

3

4

0
4
0
6
0
3

2

1

3

Cisco UCS X210c M6 Compute Node Memory Guide

25

26

Cisco UCS X210c M6 Compute Node Memory Guide

