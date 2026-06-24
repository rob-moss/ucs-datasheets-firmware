# Intersight CVA vs PVA: Feature Comparison Guide

## Executive Summary

### Connected Virtual Appliance (CVA)
**Best for:** Environments with strict data policies but that still allow outbound internet connections to Cisco.

The CVA is connected to Intersight from the inside out and can operate through a proxy with a whitelist. It periodically connects back to Cisco Intersight over HTTPS (port 443), allowing you to retain all device data locally while keeping hardware compatibility lists, alerts, and Intersight microservices automatically updated.

**Key Advantage:** Automatic updates, proactive support, and seamless Cisco integration with controlled outbound connectivity.

---

### Private Virtual Appliance (PVA)
**Best for:** Heavily secured, zero-trust, or "air-gapped" data centers (such as government, defense, or high-security financial sectors) that cannot have any system details leave the premises.

The PVA provides a fully isolated on-premises Intersight instance. Because it cannot phone home, network administrators must manually download, patch, and maintain the appliance software bundles using offline file transfers.

**Key Advantage:** Complete isolation and zero data exfiltration with full control over all operations.

---

## Common Features (Both CVA and PVA)

Both appliances support identical core operational and management capabilities:

### Core Management
- Server management and inventory
- Fabric Interconnect management
- Chassis and HyperFlex system management
- Unified Edge support
- Nutanix HCI cluster deployment and management
- Server diagnostics (M6 and later servers)
- Server profiles and policies
- Fleet management functionality
- Location features (geolocation and GPS coordinates)
- Tags and path tag propagation
- Custom privilege sets creation
- Role-Based Access Control (RBAC)
- Workflow Designer and Task Designer
- Multi-tenancy support via Organizations and Resource Groups

### Authentication & Security
- **SSO/SAML 2.0 authentication**
- **MFA (Multi-Factor Authentication)**
- LDAP integration
- API key and OAuth application management
- Session timeout configuration

### Monitoring & Analytics
- Real-time appliance health monitoring (CPU, memory, disk utilization)
- Metrics collection and monitoring
- Dashboard management
- Security advisory and field notice tracking
- Email notifications for security updates and EOL advisories

### Configuration Management
- Email notification configuration (SMTP settings)
- Webhook configuration for integrations
- Syslog configuration
- Certificate management (SSL/TLS)

---

## Feature Differentiation Matrix

| Feature Category | Connected Virtual Appliance (CVA) | Private Virtual Appliance (PVA) |
|---|---|---|
| **Connectivity Model** | Connected to Cisco via HTTPS (port 443) | Fully offline, air-gapped, no external connectivity |
| **Proxy Support** | Can operate through proxy with whitelist | N/A - no internet connectivity |
| **Firmware Management** | Pulls firmware images directly from Cisco | Manually downloaded from software.cisco.com and transferred via offline file transfer |
| **Software Updates** | Automatic OTA (Over-The-Air) updates pulled from Cisco | Manually downloaded from software.cisco.com and transferred via offline file transfer |
| **Proactive Support** | Yes - Proactive alerts enabled | No - no proactive alerts |
| **Connected TAC Integration** | Yes - Direct Cisco TAC integration available | No - Not available |
| **Cisco Software Download Service** | Direct access to Cisco repository for firmware | Requires manual download on internet-connected device |
| **Proactive RMA** | Yes - Automatic hardware failure detection and proactive RMA generation | No - Manual RMA initiation required |
| **Automatic Tech Support Bundle Generation** | Yes - Automatic when opening Cisco TAC service requests | No - Manual collection and sharing required |
| **Update Mechanism** | Automatic, periodic connection to Cisco services | Manual download and import process |
| **Data Residency** | All device data stays locally, only metadata/commands traverse to Cisco | All data remains strictly on-premises; zero data leaves the facility |
| **Deployment Complexity** | Lower - automatic updates and maintenance | Higher - manual patch and software management required |
| **Security Posture** | Cloud-connected with controlled outbound access | Air-gapped with zero trust / defense-in-depth model |
| **IP Access Management** | Supported | **Not supported** |
| **Advisory Updates** | Real-time from Cisco services | Only during scheduled appliance upgrades |
| **Typical Use Case** | Enterprise environments with internet access to Cisco | Government, defense, high-security financial, heavily regulated industries |

---

## Operational Workflow Differences

### CVA Operational Workflow
1. On-premises targets connect to CVA
2. CVA periodically initiates outbound connection to Cisco Intersight (HTTPS port 443)
3. CVA receives firmware updates, alerts, and service updates automatically
4. Hardware issues trigger automatic Proactive RMA generation
5. Tech support bundles automatically generated and uploaded when creating Cisco TAC cases
6. Administrators configure whitelist rules for proxy connectivity

### PVA Operational Workflow
1. On-premises targets connect to PVA
2. Administrator needs firmware update:
   - Logs into software.cisco.com on internet-connected device
   - Downloads firmware or software bundle
   - Transfers via offline file transfer (USB, secure drive, etc.)
   - Uploads to PVA manually
3. Hardware issues require manual RMA initiation
4. Tech support bundles must be manually collected and shared with Cisco TAC via external channels
5. All security updates and advisories reviewed during scheduled maintenance windows

---

## Key Technical Differences

### Connectivity Requirements
- **CVA:** Requires outbound HTTPS connectivity (port 443) to Cisco infrastructure. Can operate through corporate proxy with whitelist.
- **PVA:** Requires NO internet connectivity. Completely standalone and isolated.

### Data Flow
- **CVA:** Device data stays local; control/metadata/alerts flow between CVA and Cisco SaaS
- **PVA:** All data, configurations, and operations remain strictly on-premises

### Patching Strategy
- **CVA:** "Pull" model - CVA automatically downloads and applies updates from Cisco
- **PVA:** "Push" model - Administrators manually obtain and deploy updates

### Support Model
- **CVA:** Proactive - Cisco monitors appliance health and initiates support workflows
- **PVA:** Reactive - Administrators must manually initiate support interactions

---

## Deployment Considerations

### Choose CVA If You:
- Have outbound internet connectivity to Cisco (port 443)
- Want automatic firmware and software updates
- Need proactive hardware failure detection and RMA
- Want direct integration with Cisco TAC for support cases
- Prefer lower operational overhead for patch management
- Can accept cloud-connected metrics/monitoring
- Operate in standard enterprise environments

### Choose PVA If You:
- Operate in air-gapped or completely offline networks
- Have zero-trust security requirements
- Cannot allow any system details to leave the premises
- Work in government, defense, or high-security financial sectors
- Are under strict regulatory compliance (FedRAMP, EAL, etc.)
- Have dedicated teams to manage manual updates
- Require maximum data sovereignty and isolation
- Accept higher operational overhead for software maintenance

---

## Latest Feature Support (Version 1.1.6-0, March 2026)

Both CVA and PVA support:
- Cisco Unified Edge management
- Fleet management for multi-device orchestration
- Location-based resource organization
- Server diagnostics and bulk actions
- Custom privilege set creation
- Email advisory notifications
- 50 Gbps speed support on UCS 6664 Fabric Interconnect
- Support for latest hardware (X410c M8, 6652 FI, etc.)
- Nutanix Prism Central integration
- GPU and environment metrics collection
- Small appliance configuration options (8 vCPU, 32 GB RAM, 600 GB storage)

---

## Summary Table

| Aspect | CVA | PVA |
|--------|-----|-----|
| **Internet Required** | Yes (HTTPS port 443) | No |
| **Proxy Support** | Yes (with whitelist) | N/A |
| **Firmware Updates** | Automatic from Cisco | Manual from software.cisco.com |
| **Proactive Support** | Yes | No |
| **TAC Integration** | Direct (Connected TAC) | Manual |
| **Data Location** | Local + metadata to Cisco | Strictly local only |
| **RMA Process** | Automatic detection & generation | Manual initiation |
| **Operational Overhead** | Low | High |
| **Security Level** | High (controlled connectivity) | Highest (air-gapped) |
| **Best For** | Connected enterprises | Air-gapped/secure facilities |

---

## Conclusion

The fundamental difference between CVA and PVA is **connectivity and automation vs. isolation and manual control**:

- **CVA** optimizes for seamless, automated operations with controlled outbound connectivity to Cisco, making it ideal for most enterprise environments
- **PVA** optimizes for maximum isolation and zero data exfiltration, making it essential for highly regulated or air-gapped environments

Both platforms provide identical feature sets for infrastructure management, ensuring that security/compliance decisions don't limit operational capability—only the workflow and support model.
