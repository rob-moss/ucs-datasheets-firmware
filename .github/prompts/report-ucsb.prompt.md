---
name: report-ucsb
description: Report on UCS B-series servers
tools: [execute, read, agent, edit, search, web, todo, ucs-docs/*]
---
Create a report in markdown format on UCS B-series servers based on the information available in the MCP server `ucs-docs`.

**Reportfile**: `ucs-firmware-reports/ucs-b-series-report.md`

# Inputs
The input data should include the following information about UCS B-series servers:
- B-Series servers and models
- Firmware versions
- Operating system or hypervisor

If there are no inputs then report should state that there is no information available on UCS B-series servers, and use these defaults:
- B-Series servers and models: UCS B200 M5
- Firmware versions: 4.3(6e)
- Operating system or hypervisor: VMware ESXi 8u3

# Outputs
All output should be in Markddown format and saved to the file **Reportfile**

Use headings and paragraphs when appropriate to organize the information in the report. Use bullet points or numbered lists when appropriate to present information in a clear and concise manner.

Use a table whenever there is a lot of data to display such as for the Firmware versions + Adapters + nenic/nfnic/ens-nenic versions for the different B-series server models.

The report should include the following sections:
- What are the compatible Fabric Interconnects (FIs) and IO Modules (IOMs)
- What is the latest firmware version available for UCS B-series servers
- What are the supported operating systems and hypervisors for UCS B-series servers
- What are the supported adapters for UCS the B-series servers
- What are the recommended adapter nenic/nfnic/ens-nenic versions for those servers and adapters for the firmware version specified.
