---
name: query-manager
description: >
  Use this prompt to query Cisco UCS firmware compatibility and generate compatibility matrices.
  Provide firmware parameters (mode, infra version, server FW generation, blade model, FI model, IOM)
  and get back a detailed compatibility matrix with recommended versions and upgrade paths.
  Example: "Mode: IMM, Infra: 4.3(6), Server: latest recommended, B200-M5, FI-64108, IOM-2204"
argument-hint: "Provide: Mode (IMM/UCSM), Infra version, Server FW, Blade model, FI model, IOM model (e.g., 'IMM, 4.3(6), latest recommended, B200-M5, FI-64108, 2204')"
---

# UCS Firmware Compatibility Matrix Builder

You are querying the **VersionManager** agent to build a compatibility matrix for Cisco UCS firmware.

## Input Parameters

Extract and clarify these from the user's request:

| Parameter | Example | Purpose |
|-----------|---------|---------|
| **Mode** | IMM or UCSM | Management mode |
| **Infrastructure FW** | 4.3(6), 6.0(2) | Fabric Interconnect firmware version |
| **Server FW** | 4.3(6), 6.0(1), latest recommended | Server firmware version or label |
| **Blade/Server Model** | B200-M5, C240-M8, X210C-M7 | Server hardware model |
| **FI Model** | FI-6454, FI-64108, FI-6536 | Fabric Interconnect model |
| **IOM Model** | 2204, 2208, 2304, 2308 | I/O Module model (if applicable) |

If any parameter is missing, ask the user to clarify before proceeding.

---

## Query the VersionManager Agent

Use the VersionManager agent with this structured query:

```
Management Mode: [IMM/UCSM]
Infrastructure Firmware: [version]
Server Firmware Target: [version or "latest recommended"]
Hardware:
  - Blade/Server: [model]
  - FI: [model]
  - IOM: [model]

Generate a compatibility matrix showing:
1. Is this configuration supported?
2. Compatible infrastructure FW versions (range)
3. Compatible server FW versions (range)
4. Recommended versions from official sources
5. Any known limitations or deprecations
```

---

## Output Format

After VersionManager responds, format the compatibility matrix as:

### Configuration Summary
| Component | Model | Current Version | Recommended | Status |
|-----------|-------|-----------------|-------------|--------|
| Blade/Server | [model] | [version] | [recommended] | ✓ Supported / ⚠ EOL / ✗ Not Supported |
| FI | [model] | [version] | [recommended] | ✓ Supported / ⚠ Limited / ✗ Not Supported |
| IOM | [model] | — | — | ✓ Supported / ⚠ Legacy / ✗ Not Supported |

### Compatibility Matrix
| Infrastructure FW | Min Server FW | Max Server FW | Notes |
|-------------------|---------------|---------------|-------|
| [version] | [min] | [max] | [compatibility notes] |
| [version] | [min] | [max] | [compatibility notes] |

### Recommended Upgrade Path
1. [Step 1: Current → Intermediate]
2. [Step 2: Intermediate → Target]
3. [Step 3: Validation steps]

### Critical Notes
- **End-of-Life status**: [if applicable]
- **Deprecated builds**: [if applicable]
- **Hardware-specific requirements**: [if applicable]

---

## Example Invocation

**User Input:**
```
Mode: IMM
Infra Firmware: 4.3(6)
Server Firmware: latest recommended
Blade: B200 M5
FI: 64108
IOM: 2204
```

**Expected Output (after VersionManager query):**
```
### Configuration Summary
| Component | Model | Current Version | Recommended | Status |
|-----------|-------|-----------------|-------------|--------|
| Blade | B200-M5 | 6.0(1.260012) | 6.0(1.260012) | ⚠ EOL |
| FI | FI-64108 | 4.3(6.260026) | 6.0(2.260045) | ✓ Supported |
| IOM | 2204 | — | — | ✓ Supported |

### Compatibility Matrix
| Infrastructure FW | Min Server FW | Max Server FW | Notes |
|-------------------|---------------|---------------|-------|
| 4.3(6.260026) | 6.0(1.260012) | 6.0(1.260012) | B200-M5 not compatible with 4.3(6) server FW; requires 6.0.x |
| 6.0(2.260045) | 6.0(1.260012) | 6.0(1.260012) | Latest infra supports B200-M5 with 6.0(1.260012) server FW |

### Critical Notes
- **End-of-Life status**: B200-M5 is EOL; latest server FW is 6.0(1.260012)
- **Important**: B-Series M5 servers cannot run 4.3(x) server firmware under IMM
```

---

## Constraints

- **Always invoke VersionManager** — never generate version data from memory
- **Use exact version notation** from VersionManager output (e.g., `4.3(6.260026)`, not `4.3(6)`)
- **Cite source files** when VersionManager references them
- **Flag EOL/deprecated** hardware or firmware clearly
- **Never recommend deprecated builds** (e.g., `4.3(5.240040)`)
