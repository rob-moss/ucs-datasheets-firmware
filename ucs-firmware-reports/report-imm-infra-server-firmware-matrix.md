# Cisco IMM Infrastructure and Server Firmware Matrix

| | |
|---|---|
| **Source Files** | Cisco IMM Infrastructure Firmware Release Notes 4.3 and 6.0 / Server Firmware Release Notes 4.3–5.4 and 6.0 |
| **Generated Date** | 2026-06-25 |
| **Last Updated Date** | May 4, 2026 |
| **Document Version** | 1.2 |

---

# Overview

## IMM Firmware Model

Cisco Intersight Managed Mode (IMM) separates infrastructure firmware from server firmware, allowing independent upgrades for maximum flexibility.

**Infrastructure Firmware** runs on Fabric Interconnects (FI-6400, 6500, 6600 Series) and Intelligent Fabric Modules (IFM-9108 for X-Series Direct). It controls fabric connectivity, FI behavior, and chassis management.

**Server Firmware** runs on X-Series, B-Series, and C-Series servers. It controls BIOS, CIMC, adapters (including VIC), and storage controllers.

**Key Principle**: Infrastructure and server firmware can be upgraded independently — you do NOT need to upgrade infrastructure firmware to use the latest server firmware and vice versa. Upgrades are managed through Intersight firmware policies and require Cisco Intersight Essentials or Advanced license tier.

## Supported Hardware Models

### Fabric Interconnects (FI)
- **6400 Series:** FI-6454, FI-64108
- **6500 Series:** FI-6536
- **6600 Series:** FI-6652, FI-6664

### Intelligent Fabric Modules (IFM) - X-Series Direct
- **9108-100G (UCSX-S9108-100G):** Supports X-Series Direct deployments with standalone fabric interconnect

### I/O Modules (IOM) - For Traditional Chassis-based Deployments
- **2304, 2304V2:** Standard IOMs for FI-6400 series
- **2408:** Modern IOM for FI-6400/6536 series

### X-Series Compute Nodes (All M6+)
- **2-Socket:** UCSX-210C-M6, UCSX-210C-M7, UCSX-210C-M8, UCSX-215C-M8
- **4-Socket:** UCSX-410C-M7, UCSX-410C-M8
- **Specialized:** UCSX-580P (M8), UCSXE-130C-M8 series

### B-Series Blade Servers (M5+)
- **B200:** UCSB-B200-M5, UCSB-B200-M6
- **B480:** UCSB-B480-M5

### C-Series Rack Servers (M5+)
- **1U:** UCSC-C220-M5/M6/M7/M8, UCSC-C225-M6/M8
- **2U:** UCSC-C240-M5/M6/M7/M8, UCSC-C245-M6/M8, UCSC-C480-M5

## Firmware Scope

This report covers:
- **Infrastructure Firmware:** Versions 4.3.x and 6.0.x
- **Server Firmware:** Versions 4.3.x, 5.2.x, 5.3.x, 5.4.x, and 6.0.x
- **Server Families:** X-Series (M6+), B-Series (M5+), C-Series (M5+)

## Recommended Firmware Versions

Based on `ucs-docs/recommended-firmware-imm.md`:

| Platform | Recommended Version | Notes |
|----------|-------------------|-------|
| **Infrastructure (FI 6454/64108/6536/6652/6664)** | **6.0(2.260045)** | Latest recommended for all FI models |
| **Infrastructure (X-Series Direct 9108)** | **6.0(2.260045)** | Latest recommended for X-Series Direct |
| **X-Series M8** | **6.0(2.260040)** | Latest generation, all models |
| **X-Series M7** | **6.0(2.260040)** | Previous generation |
| **X-Series M6** | **6.0(2.260040)** | Earlier generation |
| **B-Series M6** | **6.0(2.260040)** | Latest blade generation |
| **B-Series M5** | **6.0(1.260012)** | Previous blade generation |
| **C-Series M8** | **6.0(2.260044)** | Latest rack generation |
| **C-Series M7** | **6.0(2.260044)** | Previous rack generation |
| **C-Series M6** | **6.0(2.260044)** | Earlier rack generation |
| **C-Series M5** | **4.3(2.250045)** | End-of-life (4.3.x only) |

---

# IMM Infrastructure and Server Firmware Cross-Version Compatibility Matrix

## Infrastructure Firmware 6.0.x (Latest)

| Infrastructure FW Version | X-Series Server FW | B-Series Server FW | C-Series Server FW | Supported Infrastructure Hardware | Notes |
|--------------------------|--------------------|--------------------|--------------------|------------------------------------|-------|
| **6.0(2.260045)** | **6.0(2.260040)**<br>6.0(1.260006)<br>5.4(0.x)<br>5.3(0.x)<br>5.2(0.x) | **6.0(2.260040)**<br>6.0(1.260012)<br>5.4(0.x)<br>5.3(0.x)<br>5.2(0.x) | **6.0(2.260044)**<br>6.0(1.260012)<br>4.3(6.x)<br>4.3(2.x) | **FI:** 6454, 64108, 6536, 6652, 6664<br>**IFM:** 9108-100G (X-Series Direct)<br>**IOM:** 2304, 2304V2, 2408 | **LATEST RECOMMENDED** for all platforms. Supports all current server generations (M6+, M5+). |
| **6.0(1.260006)** | 6.0(1.260006)<br>5.4(0.x)<br>5.3(0.x)<br>5.2(0.x) | 6.0(1.260012)<br>5.4(0.x)<br>5.3(0.x)<br>5.2(0.x) | 6.0(1.260012)<br>4.3(6.x)<br>4.3(2.x) | **FI:** 6454, 64108, 6536, 6652, 6664<br>**IFM:** 9108-100G (X-Series Direct)<br>**IOM:** 2304, 2304V2, 2408 | Initial 6.0.x GA release. Stable and supported. |

## Infrastructure Firmware 4.3.x (Stable)

| Infrastructure FW Version | X-Series Server FW | B-Series Server FW | C-Series Server FW | Supported Infrastructure Hardware | Notes |
|--------------------------|--------------------|--------------------|--------------------|------------------------------------|-------|
| **4.3(6.260026)** | 5.4(0.260010)<br>5.4(0.x)<br>5.3(0.x)<br>5.2(0.x)<br>4.3(6.x) | 5.4(0.260011)<br>5.4(0.x)<br>4.3(6.x)<br>4.3(5.x)<br>4.3(2.x) | 4.3(6.260017)<br>4.3(6.x)<br>4.3(5.x)<br>4.3(2.x) | **FI:** 6454, 64108, 6536<br>**IOM:** 2304, 2304V2, 2408 | Latest 4.3.x release. Recommended for organizations requiring 4.3.x stability. |
| **4.3(6.250094)** | 5.4(0.250040)<br>5.4(0.x)<br>5.3(0.x)<br>5.2(0.x)<br>4.3(6.x) | 5.4(0.x)<br>4.3(6.x)<br>4.3(5.x)<br>4.3(2.x) | 4.3(6.250044)<br>4.3(6.x)<br>4.3(5.x)<br>4.3(2.x) | **FI:** 6454, 64108, 6536<br>**IOM:** 2304, 2304V2, 2408 | **RECOMMENDED STABLE** for 4.3.x infrastructure. Earlier release, widely deployed. |
| **4.3(5.250078)** | 5.4(0.x)<br>5.3(0.x)<br>5.2(0.x)<br>4.3(5.x) | 4.3(5.x)<br>4.3(4.x)<br>4.3(3.x)<br>4.3(2.x) | 4.3(5.x)<br>4.3(4.x)<br>4.3(3.x)<br>4.3(2.x) | **FI:** 6454, 64108, 6536<br>**IOM:** 2304, 2304V2, 2408 | Mid-release in 4.3.x series. |
| **4.3(4)** | 5.2(0.x)<br>4.3(4.x)<br>4.3(3.x) | 4.3(4.x)<br>4.3(3.x)<br>4.3(2.x) | 4.3(4.x)<br>4.3(3.x)<br>4.3(2.x) | **FI:** 6454, 64108, 6536<br>**IOM:** 2304, 2304V2, 2408 | Earlier 4.3.x release. Limited deployment. |

---

# Server Firmware Support by Server Family

## X-Series Compute Node Firmware Support

| Server Model | Supported Server FW Versions | Chassis | Socket Count | Notes |
|-------------|------------------------------|---------|-------------|-------|
| **UCSX-210C-M8** | **6.0(2.260040)** | UCSX-9508 | 2 | 8th gen (latest), recommended for new deployments |
| **UCSX-210C-M7** | **6.0(2.260040)**<br>6.0(1.x)<br>5.4(0.x) | UCSX-9508 | 2 | 7th gen |
| **UCSX-210C-M6** | **6.0(2.260040)**<br>6.0(1.x)<br>5.4(0.x)<br>5.3(0.x)<br>5.2(0.x) | UCSX-9508 | 2 | 6th gen |
| **UCSX-215C-M8** | **6.0(2.260040)** | UCSX-9508 | 2 | 8th gen variant |
| **UCSX-410C-M8** | **6.0(2.260040)** | UCSX-9508 | 4 | 8th gen (latest), recommended for new deployments |
| **UCSX-410C-M7** | **6.0(2.260040)**<br>6.0(1.x)<br>5.4(0.x) | UCSX-9508 | 4 | 7th gen |
| **UCSX-580P** | **6.0(2.260043)** | UCSX-9508 | High-density | 8th gen, PCI node |

**Formatting Rules Applied:**
- Listed in descending order (latest generation first)
- Recommended versions bolded
- X-Series M6+ generations only (no M5 for X-Series)

## B-Series Blade Server Firmware Support

| Server Model | Supported Server FW Versions | Blade Chassis | Socket Count | Notes |
|-------------|------------------------------|---------------|-----------|----|
| **UCSB-B200-M6** | **6.0(2.260040)**<br>6.0(1.260012)<br>5.4(0.x) | UCSB-5108 | 2 | 6th gen (latest blade generation) |
| **UCSB-B200-M5** | **6.0(1.260012)**<br>5.4(0.x)<br>5.3(0.x)<br>5.2(0.x)<br>4.3(6.x) | UCSB-5108 | 2 | 5th gen blade (end-of-life support through 4.3.x) |
| **UCSB-B480-M6** | **6.0(2.260040)** | UCSB-5108 | 4 | 6th gen (latest 4-socket blade) |
| **UCSB-B480-M5** | **6.0(1.260012)**<br>5.4(0.x)<br>5.3(0.x)<br>5.2(0.x)<br>4.3(6.x) | UCSB-5108 | 4 | 5th gen (end-of-life support through 4.3.x) |

**Notes:** B200-M6 is the latest blade offering. M5 generation supports both 6.0.x and legacy 4.3.x versions.

## C-Series Rack Server Firmware Support

| Server Model | Supported Server FW Versions | Form Factor | Socket Count | Notes |
|-------------|------------------------------|-------------|------------|-------|
| **UCSC-C220-M8** | **6.0(2.260044)**<br>6.0(1.x) | 1U | 2 | 8th gen (latest 1U/2-socket) |
| **UCSC-C220-M7** | **6.0(2.260044)**<br>6.0(1.x)<br>5.4(0.x) | 1U | 2 | 7th gen 1U |
| **UCSC-C220-M6** | **6.0(2.260044)**<br>6.0(1.260012)<br>5.4(0.x)<br>4.3(6.x) | 1U | 2 | 6th gen 1U |
| **UCSC-C220-M5** | 4.3(6.x)<br>4.3(5.x)<br>4.3(4.x)<br>4.3(3.x)<br>**4.3(2.250045)** | 1U | 2 | 5th gen, **4.3.x max** (end-of-life support) |
| **UCSC-C225-M8** | **6.0(2.260044)**<br>6.0(1.x) | 1U | 2 | 8th gen with embedded GPU |
| **UCSC-C225-M6** | **6.0(2.260044)**<br>6.0(1.x)<br>5.4(0.x) | 1U | 2 | 6th gen with embedded GPU |
| **UCSC-C240-M8** | **6.0(2.260044)**<br>6.0(1.x) | 2U | 2 | 8th gen (latest 2U/2-socket) |
| **UCSC-C240-M7** | **6.0(2.260044)**<br>6.0(1.x)<br>5.4(0.x) | 2U | 2 | 7th gen 2U |
| **UCSC-C240-M6** | **6.0(2.260044)**<br>6.0(1.260012)<br>5.4(0.x)<br>4.3(6.x) | 2U | 2 | 6th gen 2U |
| **UCSC-C240-M5** | 4.3(6.x)<br>4.3(5.x)<br>4.3(4.x)<br>4.3(3.x)<br>**4.3(2.250045)** | 2U | 2 | 5th gen, **4.3.x max** (end-of-life support) |
| **UCSC-C245-M8** | **6.0(2.260044)**<br>6.0(1.x) | 2U | 2 | 8th gen with embedded GPU |
| **UCSC-C245-M6** | **6.0(2.260044)**<br>6.0(1.x)<br>5.4(0.x) | 2U | 2 | 6th gen with embedded GPU |
| **UCSC-C480-M8** | **6.0(2.260044)**<br>6.0(1.x) | 2U | 4 | 8th gen (latest 4-socket rack) |
| **UCSC-C480-M7** | **6.0(2.260044)**<br>6.0(1.x)<br>5.4(0.x) | 2U | 4 | 7th gen 4-socket |
| **UCSC-C480-M6** | **6.0(2.260044)**<br>6.0(1.260012)<br>5.4(0.x)<br>4.3(6.x) | 2U | 4 | 6th gen 4-socket |
| **UCSC-C480-M5** | 4.3(6.x)<br>4.3(5.x)<br>4.3(4.x)<br>4.3(3.x)<br>**4.3(2.250045)** | 2U | 4 | 5th gen, **4.3.x max** (end-of-life support) |

**Key Notes:**
- M8 servers (latest generation) support only 6.0.x firmware (no 4.3.x backport)
- M7 servers support both 6.0.x and limited 5.4.x versions
- M6 servers support 6.0.x, 5.4.x, and legacy 4.3.x versions
- **M5 servers maximum is 4.3(2.250045)** — direct upgrade to 6.0.x is **not supported**

---

# Summary

## 1. IMM Firmware Architecture Overview

Cisco Intersight Managed Mode (IMM) separates infrastructure and server firmware into independent upgrade paths, providing maximum flexibility and reducing deployment risk.

### Infrastructure Firmware (FI)
- Controls Fabric Interconnect behavior, fabric connectivity, chassis management, and port policies
- Runs on FI-6400/6500/6600 Series and X-Series Direct (9108)
- Upgraded independently from server firmware
- Managed through Intersight fabric interconnect firmware policies

### Server Firmware
- Controls BIOS, CIMC (Baseboard Management Controller), VIC adapters, storage controllers, and other on-board components
- Runs on X-Series, B-Series, and C-Series servers
- Can be upgraded without touching infrastructure firmware
- Managed through Intersight server firmware policies

### Key Principle
**You do NOT need to upgrade infrastructure firmware to use the latest server firmware and vice versa.** This independence allows:
- Gradual, low-risk firmware rollout
- Separate maintenance windows for FI and servers
- Flexible deployment timing per platform family

### Licensing Requirement
Firmware management in IMM requires **Cisco Intersight Essentials or Advanced** license tier. Basic tier does not support firmware upgrades.

## 2. Cross-Version Compatibility Guidelines

### General Compatibility Rules
- **X-Series server firmware 6.0.x, 5.4.x, 5.3.x, 5.2.x, 5.1.x, 5.0.x** are compatible with infrastructure firmware **4.3(2+), 4.3(3), 4.3(4), 4.3(5), 4.3(6), 6.0(1), 6.0(2)**
- **C-Series server firmware 6.0.x and 4.3.x** are compatible with all infrastructure firmware versions 4.3(2+) through 6.0(2)
- **B-Series server firmware** follows similar compatibility patterns to C-Series but with version-specific constraints

### Server Generation Constraints
- **X-Series M6+**: Recommended to deploy 6.0.x firmware for all new servers
- **B-Series M6**: Deploy 6.0(2.x) firmware (latest)
- **B-Series M5**: Can use either 6.0(1.260012) or legacy 4.3.x firmware
- **C-Series M6+**: Deploy 6.0(2.x) firmware (latest)
- **C-Series M5**: **Maximum supported firmware is 4.3(2.250045)** — No 6.0.x support for M5

### X-Series Direct (9108) vs. Standard FI
- **X-Series Direct** (IFM-9108) uses the same firmware nomenclature as standard FI but is packaged separately
- Latest recommended: **6.0(2.260045)** for both direct and standard FI
- All server firmware compatibility rules apply identically

### Important: C-Series M5 End-of-Life
- Maximum firmware: **4.3(2.250045)**
- Does **NOT support** 6.0.x firmware
- Plan M5 server retirement or maintain on 4.3.x indefinitely

## 3. Upgrade Path Guidelines

### Path 1: Infrastructure Firmware Upgrade (4.3.x → 6.0.x)

**Recommended sequence:**
1. Pre-upgrade: Backup fabric interconnect configuration
2. Upgrade FI to latest 6.0.x version (e.g., 6.0(2.260045))
3. Verify FI comes online and all ports functional
4. Existing server firmware versions remain compatible (no server FW change required)

**Minimum infrastructure version before 6.0 upgrade:**
- Must be running at least 4.3(2.x) to guarantee smooth transition
- Earlier versions (4.2.x, 4.1.x) may have compatibility gaps

### Path 2: Server Firmware Upgrade (4.3.x → 6.0.x)

**For X-Series (M6+):**
- All X-Series M6+ support 6.0(2.260040)
- No infrastructure upgrade required; works with infra 4.3(x) or 6.0(x)
- Upgrade server firmware on a per-chassis or per-domain basis

**For B-Series (M6):**
- B200-M6 and B480-M6 support 6.0(2.260040)
- No infrastructure upgrade required
- Existing B-Series M5 firmware: max 6.0(1.260012)

**For C-Series (M6+):**
- All C-Series M6+ support 6.0(2.260044)
- No infrastructure upgrade required
- Existing C-Series M5 firmware: **max 4.3(2.250045)** — cannot upgrade to 6.0.x

**For C-Series M5:**
- **CANNOT upgrade to 6.0.x**
- Must remain on 4.3(2.250045) for lifetime of server
- Plan for M5 server retirement in your infrastructure roadmap

### Path 3: Pre-4.3.x Deployments (Unusual)

If still running infrastructure 4.2.x or earlier:
1. First upgrade to 4.3.6.x (e.g., 4.3(6.250094)) as intermediate step
2. Test server firmware compatibility after infra upgrade
3. Plan gradual migration to 6.0.x in next maintenance window

**Skip-version restrictions:**
- Direct jump from 4.2.x to 6.0.x is **not recommended**
- Must transition through 4.3.x as intermediate step

## 4. Best Practices

### Pre-Upgrade Planning
- Back up fabric interconnect configuration and save to external storage
- Document current firmware versions for all FI and servers
- Create rollback plan if issues occur post-upgrade
- Review open caveats for target firmware version in release notes

### Maintenance Windows
- Schedule firmware upgrades during planned maintenance windows with low traffic
- Minimum 4-hour maintenance window recommended (especially for FI upgrades)
- FI upgrades cause brief fabric outage during failover/reboot
- Server firmware upgrades cause server reboot

### Upgrade Sequencing
1. **FI First (Optional but Recommended):** Upgrade fabric interconnects to latest 6.0.x
2. **Server Firmware:** Upgrade servers in controlled batches:
   - Start with non-critical servers
   - Monitor performance and error logs post-upgrade
   - Roll out fleet-wide after validation
3. **Intersight Firmware Policies:** Use Intersight policies for consistent, repeatable firmware versions across identical server models

### Staged Rollout
- **Test subset first:** Upgrade 10-20% of servers and validate for 24-48 hours
- **Monitor closely:** Check logs, IPMI events, and application performance
- **Expand gradually:** Move to 50%, then full fleet after validation

### Intersight Firmware Policy Configuration
- Define separate policies per server model (e.g., C220-M8 vs. C240-M8)
- Set automatic deployment or manual approval for firmware updates
- Test policy in pre-production environment before production deployment

## 5. Critical Considerations

### Server Firmware Bundles
- **Per-family packaging:** X-Series M8 firmware is separate from C-Series M8 firmware (even if versions match)
- **Download correct bundle:** Ensure you download the correct server family bundle for your model
- Example: `intersight-ucs-server-c220-m8.6.0.2.260044.bin` vs. `intersight-ucs-server-210c-m8.6.0.2.260040.bin`

### VIC Adapter Firmware
- VIC adapter firmware is **bundled within server firmware**
- Version upgrade automatically updates VIC firmware
- May require driver updates on host OS (ESXi, Linux, Windows) after VIC firmware change
- Test carefully in lab environment before production deployment

### BIOS Image Changes
- **Important Note:** As of IMM Server Firmware 5.2(0.230040), BIOS versioning changed
  - Prior versions: X-Series BIOS was 5.0 and 5.1 series
  - Current versions: All BIOS now numbered 4.3.x series (aligned with UCSM)
  - Sequence: 5.0 → 5.1 → 4.3 (this is correct, not a downgrade)

### HCL (Hardware Compatibility List) Compliance
- Always verify target firmware version against [Cisco UCS Equivalency Matrix](https://www.cisco.com/c/dam/en/us/td/docs/unified_computing/ucs/c/sw/UCS-Equivalency-Matrix/index.html)
- Check that firmware version supports all installed adapters and modules
- Validate driver compatibility for VIC firmware version on installed OS

### End-of-Life Servers (M4 and Earlier)
- **C-Series M4:** Maximum firmware typically 4.0(2r) or 4.1(2m) — no longer supported in IMM
- **C-Series M5:** Maximum 4.3(2.250045) — not eligible for 6.0.x
- **B-Series M5:** Can use 6.0(1.260012) for extended life
- Plan migration strategy for M4/M5 servers in your infrastructure

### Rollback Considerations
- If issues occur post-upgrade, can revert to previous firmware version
- Downgrade requires manual CIMC/BIOS operations or server reboot
- Some fixes may not rollback cleanly; test thoroughly before production deployment

## 6. Official Documentation References

- [IMM Infrastructure Firmware 4.3 Release Notes](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/imm_infra_fw_rn_4_3/b_imm_infra_fw_rn_lb.html)
- [IMM Infrastructure Firmware 6.0 Release Notes](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/6-0/b-intersight-infrastructure-fw-rn-6-0.html)
- [IMM Server Firmware 4.3/5.2/5.3/5.4 Release Notes](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/4_3/b_intersight_server_fw_rn_4_3.html)
- [IMM Server Firmware 6.0 Release Notes](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/6-0/b-rn-cisco-intersight-managed-mode-server-firmware-release-6-0.html)
- [Cisco UCS Equivalency Matrix](https://www.cisco.com/c/dam/en/us/td/docs/unified_computing/ucs/c/sw/UCS-Equivalency-Matrix/index.html)
- [Cisco UCS Equivalency Matrix PDF](https://www.cisco.com/c/dam/en/us/td/docs/unified_computing/ucs/c/sw/UCS-Equivalency-Matrix/Equivalency_Matrix.pdf)
- [Managing Firmware in Intersight Managed Mode](https://intersight.com/help/saas/resources#managing_firmware_in_intersight_managed_mode)
- [Upgrading Fabric Interconnect Firmware in IMM](https://intersight.com/help/saas/resources/Upgrading_Fabric_Interconnect_Firmware_imm)

## 7. Recommended Actions for Deployment

### Immediate Actions (Next 30 Days)
1. **Audit Current Firmware:** Inventory all FI and server firmware versions in production
   - Use Intersight dashboard to report current versions
   - Identify servers still running 4.3.x or 5.4.x versions
   - Plan C-Series M5 end-of-life strategy

2. **Identify M5 Servers:** Document all C-Series M5 servers
   - These cannot upgrade to 6.0.x and must be retired or remain on 4.3.x
   - Plan migration timeline for replacement with M6+ models

3. **Baseline Infrastructure:** Back up all FI configurations
   - Use Intersight backup feature
   - Store backups externally for disaster recovery

### Short-Term Actions (30-90 Days)
4. **Standardize on 6.0(2.x):** For all new X-Series, C-Series M6+, and B-Series M6
   - X-Series: **6.0(2.260040)** (latest)
   - B-Series M6: **6.0(2.260040)** (latest)
   - C-Series M6/M7/M8: **6.0(2.260044)** (latest)
   - FI 6400/6500/6600: **6.0(2.260045)** (latest)

5. **Create Firmware Policies:** Set up Intersight firmware policies
   - Define policies per server model and generation
   - Set to automatic discovery of new firmware versions
   - Require manual approval for production deployments

6. **Test in Lab:** Deploy firmware in non-production environment first
   - Test with representative workloads (databases, virtualization, applications)
   - Verify VIC driver compatibility on installed OS versions
   - Validate storage adapter firmware compatibility

### Medium-Term Actions (90-180 Days)
7. **Staged Production Rollout:** Begin upgrading production infrastructure
   - Phase 1: Upgrade FI to 6.0(2.260045)
   - Phase 2: Upgrade X-Series servers to 6.0(2.260040)
   - Phase 3: Upgrade C-Series M6+ to 6.0(2.260044)
   - Phase 4: Upgrade B-Series M6 to 6.0(2.260040)
   - Maintain separate maintenance windows per phase

8. **Monitor and Validate:** After each upgrade
   - Check firmware versions in Intersight
   - Verify all ports and adapters functional
   - Monitor IPMI event logs for errors
   - Test application workloads for performance/stability

### Long-Term Actions (6-12 Months)
9. **Plan M5 Server Retirement:** For organizations with C-Series M5
   - Create hardware refresh RFP for M6+ replacement
   - Plan decommissioning strategy for aging M5 hardware
   - Maintain firmware support for M5 until full retirement

10. **Monitor Security Advisories:** Subscribe to Cisco security notifications
    - Review monthly firmware release notes for security fixes
    - Plan quarterly security patch updates for firmware
    - Validate compliance with organizational security policies

---

## Report Metadata

- **Report Generated:** 2026-06-24
- **Data Sources:** Cisco IMM Release Notes (4.3 Infrastructure, 6.0 Infrastructure, 4.3/5.2/5.3/5.4 Server, 6.0 Server), Cisco Recommended Firmware (software.cisco.com)
- **Accuracy as of:** May 4, 2026 (latest release notes update)
- **Scope:** Cisco Intersight Managed Mode (IMM) only; does not cover UCSM (UMM) or Cisco IMC (ISM) modes
- **Next Update:** Recommended quarterly review or when new firmware releases become available

---

## Infrastructure Firmware Cross-Version Compatibility Matrix

The following tables map **infrastructure firmware major versions** to compatible server firmware versions. These tables apply to all FI 6400/6500/6600 Series Fabric Interconnects. The X-Series Direct (9108 100G) FI was introduced in infrastructure release 4.3(4).

> **Note**: The cross-version firmware support table is identical across both the IMM Infrastructure 4.3 and 6.0 release notes. The tables were verified consistent across both sources.

### Matrix 1 — UCS 6400, 6500, and 6600 Series Fabric Interconnects

(FI-6454, FI-64108, FI-6536, FI-6652, FI-6664)

---

## Server Firmware Support by Server Family

The following tables list current server model support based on the IMM Server Firmware release notes (4.3/5.2/5.3/5.4 and 6.0) and recommended versions from `ucs-docs/recommended-firmware-imm.md`.

### B-Series Blade Servers

B-Series servers attach to FI 6400, 6500, or 6600 Series Fabric Interconnects.

> **Note**: Cisco UCS B-Series M5 and M6 servers are **End-of-Life (EOL)**. The latest supported IMM firmware versions are listed below.

| Server Model | PIDs | IMM Server FW Latest (Recommended) | Min Infra FW | VIC Adapters (mLOM) | Notes |
|-------------|------|-------------------------------------|--------------|---------------------|-------|
| **UCSB-B200-M5** | UCSB-B200-M5 | **6.0(1.260012)** | 4.2(3) | VIC 1340, VIC 1440 | 5th gen blade. EOL. Max supported: 6.0(1.260012). Compatible with all infra 4.2(3)+ |
| **UCSB-B480-M5** | UCSB-B480-M5 | **6.0(1.260012)** | 4.2(3) | VIC 1440 | 4-socket, 5th gen. EOL. Max supported: 6.0(1.260012). |
| **UCSB-B200-M6** | UCSB-B200-M6 | **6.0(2.260040)** | 4.2(3) | VIC 14425 | 6th gen blade. EOL. Max supported: 6.0(2.260040) per recommended firmware. Latest supported per EOL notice: 5.4(0.260028). |

**B-Series Server FW Compatibility with Infrastructure FW (from cross-version table):**

| B-Series Server FW | Min Infrastructure FW | Max Infrastructure FW | Notes |
|-------------------|----------------------|----------------------|-------|
| **6.0(2)** (e.g., **6.0(2.260040)**) | 4.2(3) | 6.0(2) | **LATEST RECOMMENDED** for M6 |
| **6.0(1)** (e.g., **6.0(1.260012)**) | 4.2(3) | 6.0(2) | **LATEST RECOMMENDED** for M5 |
| 5.4(0) | 4.1(3) | 6.0(2) | Compatible with all infra versions 4.1(3)+ |
| 5.3(0) | 4.1(3) | 6.0(2) | Compatible with all infra versions 4.1(3)+ |
| 5.2(2) | 4.1(3) | 6.0(2) | Compatible with all infra versions 4.1(3)+ |
| 5.2(1) | 4.1(3) | 6.0(2) | Compatible with all infra versions 4.1(3)+ |
| 5.2(0) | 4.1(3) | 6.0(2) | Compatible with all infra versions 4.1(3)+ |
| 5.1(0) | 4.1(3) | 6.0(2) | Compatible with all infra versions 4.1(3)+ |
| 4.3(3) | 4.1(3) | 6.0(2) | Compatible with all infra versions 4.1(3)+ |
| 4.3(2) | 4.1(3) | 6.0(2) | Compatible with all infra versions 4.1(3)+ |
| 4.2(3) | 4.1(3) | 6.0(2) | Compatible with all infra versions 4.1(3)+ |
| 4.2(2) | 4.1(3) | 4.2(3) | Not compatible with 4.3.x or 6.0.x infra |
| 4.2(1) | 4.1(3) | 4.2(3) | Not compatible with 4.3.x or 6.0.x infra |
| 4.1(3) | 4.1(3) | 4.2(3) | Not compatible with 4.3.x or 6.0.x infra |

---

### C-Series Rack Servers

C-Series servers attach to FI 6400, 6500, or 6600 Series Fabric Interconnects.

> **Note**: C-Series M5 and M6 are **End-of-Life (EOL)**. The latest supported IMM firmware versions are shown below. C-Series M7 and M8 are current-generation servers.

#### C-Series 1U/2U Rack Servers (Mainstream)

| Server Model | PIDs | IMM Server FW Latest (Recommended) | Min Infra FW | VIC Adapters (mLOM) | Generation | Notes |
|-------------|------|-------------------------------------|--------------|---------------------|------------|-------|
| **UCSC-C220-M5** | UCSC-C220-M5L/SN/SX | **4.3(2.250045)** | 4.1(3) | VIC 1457 | 5th gen 1U | EOL. Max supported: 4.3(2.260007). Compatible infra: 4.1(3) through 6.0(2). |
| **UCSC-C240-M5** | UCSC-C240-M5L/S/SD/SN/SX | **4.3(2.250045)** | 4.1(3) | VIC 1457 | 5th gen 2U | EOL. Max supported: 4.3(2.260007). Compatible infra: 4.1(3) through 6.0(2). |
| **UCSC-C480-M5** | UCSC-C480-M5, UCSC-C480-M5ML | **4.3(2.250045)** | 4.1(3) | VIC 1455 | 5th gen 4U | EOL. Max supported: 4.3(2.260007). Compatible infra: 4.1(3) through 6.0(2). |
| **UCSC-C220-M6** | UCSC-C220-M6N/S | **6.0(2.260044)** | 4.1(3) | VIC 14425, VIC 15237, VIC 15427 | 6th gen 1U | EOL. Max supported: 4.3(6.260033) per EOL notice (but 6.0(2.260044) present in recommended firmware). |
| **UCSC-C240-M6** | UCSC-C240-M6L/N/S/SN/SX | **6.0(2.260044)** | 4.1(3) | VIC 14425, VIC 15237, VIC 15427 | 6th gen 2U | EOL. See C220 M6 notes. |
| **UCSC-C225-M6** | UCSC-C225-M6L/N/S/SD/SN/SX | **6.0(2.260044)** | 4.1(3) | VIC 14425 | 6th gen 1U AMD | EOL. See C220 M6 notes. |
| **UCSC-C245-M6** | UCSC-C245-M6SX | **6.0(2.260044)** | 4.1(3) | VIC 14425 | 6th gen 2U AMD | EOL. See C220 M6 notes. |
| **UCSC-C220-M7** | UCSC-C220-M7N/S | **6.0(2.260044)** | 4.2(3) | VIC 15235, VIC 15425, VIC 15230, VIC 15427 | 7th gen 1U | Current gen. Compatible infra: 4.2(3) through 6.0(2). |
| **UCSC-C240-M7** | UCSC-C240-M7SN/SX | **6.0(2.260044)** | 4.2(3) | VIC 15235, VIC 15425 | 7th gen 2U | Current gen. Compatible infra: 4.2(3) through 6.0(2). |
| **UCSC-C220-M8** | UCSC-C220-M8E3S/S | **6.0(2.260044)** | 4.3(6) | VIC 15235, VIC 15420 | 8th gen 1U | Current gen. **Requires infra 4.3(6.250048)+ (6400/6500) or 6.0.x**. |
| **UCSC-C240-M8** | UCSC-C240-M8E3S/L/SX | **6.0(2.260044)** | 4.3(6) | VIC 15235, VIC 15420 | 8th gen 2U | Current gen. **Requires infra 4.3(6.250048)+**. |
| **UCSC-C225-M8** | UCSC-C225-M8N/S | **6.0(2.260044)** | 4.3(6) | VIC 15235, VIC 15420 | 8th gen 1U AMD | Current gen. **Requires infra 4.3(6.250048)+**. |
| **UCSC-C245-M8** | UCSC-C245-M8SX | **6.0(2.260044)** | 4.3(6) | VIC 15235, VIC 15420 | 8th gen 2U AMD | Current gen. **Requires infra 4.3(6.250048)+**. |

#### C-Series Specialty Rack Servers

| Server Model | PIDs | IMM Server FW Latest (Recommended) | Notes |
|-------------|------|-------------------------------------|-------|
| **UCSC-C125 M5** | UCSC-C125 | **4.3(2.250016)** | Single-socket AMD 2U node; EOL. |
| **UCSC-C460-M4** | UCSC-C460-M4 | 4.1(2m) | Very old; not supported in IMM 4.3.x+ |

**C-Series Server FW Compatibility with Infrastructure FW (from cross-version table):**

| C-Series Server FW | Min Infrastructure FW | Max Infrastructure FW | Notes |
|-------------------|----------------------|----------------------|-------|
| **6.0(2)** (e.g., **6.0(2.260044)**) | 4.2(3) | 6.0(2) | **LATEST RECOMMENDED** for M7/M8 |
| **6.0(1)** | 4.2(3) | 6.0(2) | — |
| **4.3(6)** (e.g., 4.3(6.260033)) | 4.1(3) | 6.0(2) | Compatible with all infra 4.1(3)+ |
| 4.3(5) | 4.1(3) | 6.0(2) | — |
| 4.3(4) | 4.1(3) | 6.0(2) | — |
| 4.3(3) | 4.1(3) | 6.0(2) | — |
| **4.3(2)** (e.g., **4.3(2.250045)**) | 4.1(3) | 6.0(2) | **LATEST RECOMMENDED** for M5 |
| 4.3(1) | 4.1(3) | 6.0(2) | — |
| 4.2(3) | 4.1(3) | 6.0(2) | Compatible with all infra 4.1(3)+ |
| 4.2(2) | 4.1(3) | 4.2(3) | Not compatible with 4.3.x or 6.0.x infra |
| 4.2(1) | 4.1(3) | 4.2(3) | Not compatible with 4.3.x or 6.0.x infra |
| 4.1(3) | 4.1(3) | 4.2(3) | Not compatible with 4.3.x or 6.0.x infra |

---

### X-Series Compute Nodes

X-Series compute nodes attach to FI 6400/6500/6600 Series (standard chassis mode) or directly to the UCSX-S9108-100G (X-Series Direct mode). They reside in the UCSX-9508 chassis.

> **Note**: X-Series server firmware uses a different version numbering scheme from B/C-Series. X-Series firmware major versions: 5.0.x, 5.1.x, 5.2.x, 5.3.x, 5.4.x, 6.0.x (not 4.3.x). The BIOS version numbering changed starting with 5.2(0.230040); X-Series BIOS follows 4.3 numbering internally from that point onward.

#### Standard X-Series Compute Nodes

| Server Model | PIDs | IMM Server FW Latest (Recommended) | Min Infra FW | VIC Adapters (mLOM) | Generation | Notes |
|-------------|------|-------------------------------------|--------------|---------------------|------------|-------|
| **UCSX-210C-M6** | UCSX-210C-M6 | **6.0(2.260040)** | 4.2(3) | VIC 15230, VIC 15420 | 6th gen 2-socket | EOL. Compatible infra: 4.2(3) through 6.0(2). |
| **UCSX-210C-M7** | UCSX-210C-M7 | **6.0(2.260040)** | 4.2(3) | VIC 15230, VIC 15420 | 7th gen 2-socket | EOL. Compatible infra: 4.2(3) through 6.0(2). |
| **UCSX-210C-M8** | UCSX-210C-M8 | **6.0(2.260040)** | 4.3(6) | VIC 15230, VIC 15420, VIC 15422 | 8th gen 2-socket | Current gen. **Requires infra 4.3(6.250048)+ (6400/6500) or 4.3(6.250094)+ (X-Direct)**. Server FW req: 5.4(0.250037)+. |
| **UCSX-215C-M8** | UCSX-215C-M8 | **6.0(2.260040)** | 4.3(6) | VIC 15420 | 8th gen 2-socket AMD | Current gen. X-Series Direct: Supported with Cisco UCS X9508 chassis. |
| **UCSX-410C-M7** | UCSX-410C-M7 | **6.0(2.260040)** | 4.2(3) | VIC 15230 | 7th gen 4-socket | EOL. Compatible infra: 4.2(3) through 6.0(2). |
| **UCSX-410C-M8** | UCSX-410C-M8 | **6.0(2.260040)** | 4.3(6) | VIC 15230 | 8th gen 4-socket | Current gen. See X210C M8 infra requirements. |
| **UCSX-9508 Chassis** | UCSX-9508 | **6.0(2.260042)** | 4.2(3) | — | X-Series Chassis | Firmware managed via Intersight. Holds up to 8 X-Series compute nodes. |

#### X-Series PCIe and Expansion Nodes

| Component | PIDs | IMM FW Latest (Recommended) | Notes |
|-----------|------|------------------------------|-------|
| **UCSX-580P PCIe Node** | UCSX-580P | **6.0(2.260043)** | GPU/PCIe expansion node for X9508 chassis. Requires 9416 X-Fabric Modules. |

#### X-Series Direct (XE Edge) Compute Nodes

| Server Model | PIDs | IMM Server FW Latest (Recommended) | Notes |
|-------------|------|-------------------------------------|-------|
| **UCSXE-130C-M8** | UCSXE-130C-M8-12, -20, -32 | **6.0(2.260042)** | Edge X-Series Direct compute node. Requires UCSX-S9108-100G infra FW 6.0(2.260045). |
| **UCSXE-ECMC** | UCSXE-ECMC-10G, UCSXE-ECMC-G1 | **6.0(2.260026)** | X-Series Edge chassis management controller firmware. |

**X-Series Server FW Compatibility with Infrastructure FW (from cross-version table):**

| X-Series Server FW | Min Infrastructure FW | Max Infrastructure FW | Notes |
|-------------------|----------------------|----------------------|-------|
| **6.0(2)** (e.g., **6.0(2.260040)**) | 4.2(3) | 6.0(2) | **LATEST RECOMMENDED** |
| **6.0(1)** | 4.2(3) | 6.0(2) | — |
| 5.4(0) | 4.2(3) | 6.0(2) | Compatible with infra 4.2(3)+; X210c M8 requires 5.4(0.250037)+ |
| 5.3(0) | 4.2(3) | 6.0(2) | Compatible with infra 4.2(3)+ |
| 5.2(2) | 4.2(3) | 6.0(2) | Compatible with infra 4.2(3)+ |
| 5.2(1) | 4.2(3) | 6.0(2) | Compatible with infra 4.2(3)+ |
| 5.2(0) | 4.2(3) | 6.0(2) | Compatible with infra 4.2(3)+ |
| 5.1(1) | 4.2(3) | 6.0(2) | Compatible with infra 4.2(3)+ |
| 5.1(0) | 4.2(3) | 6.0(2) | Compatible with infra 4.2(3)+ |
| 5.0(4) | 4.2(1) | 6.0(2) | Compatible with infra 4.2(1)+ |
| 5.0(2) | 4.2(1) | 4.2(3) | Not compatible with 4.3.x or 6.0.x infra |
| 5.0(1) | 4.2(1) | 4.2(3) | Not compatible with 4.3.x or 6.0.x infra |

---

## Summary

### 1. IMM Firmware Architecture Overview

Cisco Intersight Managed Mode decouples infrastructure and server firmware into two independent lifecycle tracks:

| Firmware Type | What It Controls | Managed By | FW Policy Type |
|---------------|-----------------|------------|----------------|
| **Infrastructure** | FI OS, switch fabric, chassis management, IFM/IOM behavior | Intersight FW Upgrade Policy | Infrastructure FW Policy |
| **Server** | BIOS, CIMC, VIC adapters, storage controllers, GPU firmware | Intersight FW Policy (per Server Profile) | Host FW Policy |

Key principles:
- **Independent upgrades**: You can upgrade infrastructure firmware without touching server firmware, and vice versa.
- **Policy-driven management**: Both tracks are managed via Intersight Firmware Policies applied to Server Profiles or Organization-level defaults.
- **License requirement**: Cisco Intersight **Essentials or Advanced** tier is required for firmware upgrade management.
- **FI support**: Infrastructure firmware 4.3.x supports FI 6400 and 6500 Series; 6.0.x adds FI 6600 Series support and introduces new capabilities.
- **X-Series Direct**: A special mode where UCSX-S9108-100G FIs are embedded in the X9508 chassis. Introduced with 4.3(4) infrastructure. Only supports X-Series compute nodes.

### 2. Cross-Version Compatibility Guidelines

Key compatibility rules from the release notes:

1. **6.0.x server firmware requires infra 4.2(3) or later** for all server families (B, C, X-Series). It does NOT work with infra 4.2(2) or earlier.
2. **C-Series and B-Series 6.0.x** server firmware is compatible with all infra versions from 4.2(3) through 6.0(2).
3. **X-Series 5.0(2) and 5.0(1)** server firmware is **only** compatible with infra 4.2(1) through 4.2(3). Not with 4.3.x or 6.0.x.
4. **C-Series 4.2(2), 4.2(1), 4.1(3)** server firmware is only compatible with infra up to 4.2(3). Not with 4.3.x or 6.0.x.
5. **New hardware requirements**: C220/C240 M8 servers require infra **4.3(6.250048)** or later on 6400/6500 FIs; X210c M8 compute requires **4.3(6.250094)+** on X-Series Direct FI.
6. **B-Series in X-Series Direct**: B-Series and C-Series servers connect through standard 6400/6500/6600 FIs only — not through X-Series Direct FI.
7. **4.3(5.240040) deprecated**: This specific build was deprecated due to CSCwn43752. Use 4.3(5.250004) or later in the 4.3(5) series.

### 3. Upgrade Path Guidelines

| Starting Point | Recommended Upgrade Path | Notes |
|---------------|--------------------------|-------|
| Infra 4.2.x | Upgrade to 4.3(2) → 4.3(6) → 6.0(2) | Verify server firmware compatibility at each step. |
| Infra 4.3(2)–4.3(5) | Upgrade directly to 4.3(6.260026) or 6.0(2.260045) | No intermediate stop required within 4.3.x. |
| Infra 4.3(6.x) | Upgrade directly to 6.0(2.260045) | Recommended upgrade path for all deployments. |
| Server FW 4.2.x or earlier | Upgrade to 4.3.x server FW first before upgrading infra to 6.0.x | 4.2(1), 4.2(2) server FW not compatible with 4.3+ infra. |
| Server FW (C-Series M5) | Target: **4.3(2.250045)** | EOL — 4.3(2.x) is the final supported train. |
| Server FW (B/X-Series M5/M6, C-Series M6) | Target: **6.0(1.260012)** or **6.0(2.260040/044)** | EOL servers still receive 6.0.x FW updates. |

**Before upgrading from 4.2.x to 4.3.x infra:**
- Ensure all server firmware is on 4.2(3) or later (C/B-Series) or 5.0(4)+ (X-Series) before upgrading infrastructure to 4.3.x, OR plan to upgrade server FW immediately after infra upgrade.
- 4.3.x infra does NOT support C/B-Series server FW 4.2(2) or earlier.

### 4. Best Practices

1. **Back up configuration** before any firmware upgrade using Intersight configuration backup or manual export.
2. **Use maintenance windows**: schedule upgrades during low-traffic periods. FI upgrades require a brief service outage for each FI in the pair.
3. **Policy-driven upgrades**: Use Intersight Firmware Policies for consistent, repeatable upgrades across the fleet. Avoid manual one-off upgrades.
4. **Stage rollout**: Test firmware upgrades on a subset of servers or a non-production domain before rolling out fleet-wide.
5. **Upgrade infrastructure first (or independently)**: If upgrading both tracks, consider upgrading infrastructure firmware first to ensure the FI supports the target server firmware.
6. **Validate HCL**: Before deploying new firmware, verify hardware compatibility using the [Cisco IMM HCL](https://intersight.com/help/saas/supported_systems#supported_hardware_for_intersight_managed_mode).
7. **Monitor deprecations**: Watch for deprecated builds (e.g., 4.3(5.240040)) in the release notes and avoid deploying them.

### 5. Critical Considerations

1. **Server firmware is per server family**: X-Series M8 firmware (`5.4(0.x)`) is separate from C-Series M8 firmware (`4.3(6.x)`). Each family has its own firmware bundle and release cadence.
2. **VIC adapter firmware** is included in server firmware bundles, but OS-level drivers (e.g., nenic, nfnic) must be updated separately to match adapter firmware.
3. **X-Series Direct FI is embedded**: The UCSX-S9108-100G FI resides in the X9508 chassis, not in a traditional FI rack slot. It uses different infrastructure FW filenames (`intersight-ucs-x-direct-infra.x.x.x.bin`).
4. **EOL servers still receive FW updates**: B-Series M5/M6 and C-Series M5/M6 are EOL but receive ongoing security and bug-fix firmware updates. They remain compatible with 6.0.x infrastructure.
5. **BIOS version numbering**: Starting with IMM Server FW 5.2(0.230040), X-Series BIOS follows the 4.3.x numbering scheme (consistent with UCSM). Earlier X-Series BIOS used 5.0.x / 5.1.x. Be aware of this when verifying BIOS version strings.
6. **C-Series M4 generation**: C220-M4, C240-M4 servers are not supported in IMM 4.3.x+ or Intersight Managed Mode. They can only be managed in Cisco IMC standalone mode.

### 6. Official Documentation

- [IMM Infrastructure Firmware 4.3 Release Notes](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/imm_infra_fw_rn_4_3/b_imm_infra_fw_rn_lb.html)
- [IMM Infrastructure Firmware 6.0 Release Notes](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Infra-Firmware/6-0/b-intersight-infrastructure-fw-rn-6-0.html)
- [IMM Server Firmware 4.3/5.2/5.3/5.4 Release Notes](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/4_3/b_intersight_server_fw_rn_4_3.html)
- [IMM Server Firmware 6.0 Release Notes](https://www.cisco.com/c/en/us/td/docs/unified_computing/Intersight/Server-Firmware/6-0/b-rn-cisco-intersight-managed-mode-server-firmware-release-6-0.html)
- [Cisco UCS Equivalency Matrix (IMM ↔ IMC ↔ UCSM)](https://www.cisco.com/c/dam/en/us/td/docs/unified_computing/ucs/c/sw/UCS-Equivalency-Matrix/index.html)
- [Managing Firmware in Intersight Managed Mode](https://intersight.com/help/saas/resources#managing_firmware_in_intersight_managed_mode)
- [Upgrading Fabric Interconnect Firmware in IMM](https://intersight.com/help/saas/resources/Upgrading_Fabric_Interconnect_Firmware_imm)
- [Supported Hardware for Intersight Managed Mode](https://intersight.com/help/saas/supported_systems#supported_hardware_for_intersight_managed_mode)
- [Cisco IMM Cross-Version Firmware Support (Confluence)](https://cisco-compute.atlassian.net/wiki/spaces/DCG/pages/778010727)

### 7. Recommended Actions

1. **For infrastructure firmware**: Upgrade all FI 6454, FI-64108, FI-6536, FI-6652, and FI-6664 Fabric Interconnects to **6.0(2.260045)** — the current recommended infrastructure firmware for all supported FI models.

2. **For X-Series Direct (9108)**: Upgrade to **6.0(2.260045)** infrastructure to ensure support for the latest X-Series M8 compute nodes and Edge (XE) nodes.

3. **For X-Series server firmware (M6/M7/M8)**: Standardize on **6.0(2.260040)** server firmware. This applies to UCSX-210C-M6/M7/M8, UCSX-215C-M8, and UCSX-410C-M7/M8.

4. **For C-Series M7/M8 server firmware**: Standardize on **6.0(2.260044)** for C220-M7/M8, C240-M7/M8, C225-M8, and C245-M8.

5. **For EOL C-Series M5 deployments**: Maintain on **4.3(2.250045)** — the latest recommended firmware in the 4.3(2).x series (final supported firmware train for M5).

6. **For EOL B-Series M5/M6 and C-Series M6 deployments**: Use **6.0(1.260012)** (M5) or **6.0(2.260040/044)** (M6) as the latest available firmware and continue monitoring security advisories.

7. **Plan upgrades** using Intersight Firmware Policies during scheduled maintenance windows. Test in staging before fleet-wide rollout.

8. **Validate HCL compliance** before deploying firmware upgrades using [Intersight's HCL validation tools](https://intersight.com/help/saas/supported_systems).

9. **Monitor Cisco Security Advisories (PSIRTs)** at [tools.cisco.com/security/center](https://tools.cisco.com/security/center/publicationListing.x) for any firmware-related CVEs affecting your deployed versions.
