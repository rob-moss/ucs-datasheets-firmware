---
name: query-mcp
description: Queries the MCP server for UCS guides with intelligent document lookup
tools: [agent, 'ucs-docs/*', todo]
---

> **Purpose:** Answer user questions by intelligently searching UCS documentation via the `ucs-docs` MCP server.
> **Model:** Use an efficient model (e.g., GPT-4o mini) for fast, accurate responses.
> **Output:** Full paragraph first, then summary with clickable links to sources.

# Query UCS Documentation via MCP Server

This prompt helps you find accurate, sourced answers from UCS documentation by using the `docs-index.md` to quickly identify relevant documents, then searching them efficiently.

## Step 1: Identify Relevant Documents

**Before searching**, consult `ucs-docs/docs-index.md` to identify which document(s) likely contain the answer. Use the tag reference below to narrow your search:

### Quick Tag Reference

**TYPE Tags** (what kind of content):
- `type:CLI` — CLI command references
- `type:Reference` — Technical specifications, matrices, datasheets
- `type:Guide` — Administration, deployment, configuration guides
- `type:Release-Notes` — Version-specific features and fixes
- `type:API` — API references and integration guides
- `type:Architecture` — Design principles and best practices
- `type:Troubleshooting` — Diagnostics and troubleshooting procedures

**SCOPE Tags** (what component/area):
- `scope:FabricInterconnect` — Fabric interconnect (FI) documentation
- `scope:Server` — Server and blade documentation
- `scope:Firmware` — Firmware matrices and compatibility
- `scope:Intersight` — Intersight SaaS and appliance docs
- `scope:UCSManager` — UCSM-specific documentation

**MODE Tags** (what management mode):
- `mode:IMM` — Intersight Managed Mode
- `mode:UCSManager` — UCS Manager (UCSM) mode
- `mode:Intersight` — Intersight SaaS/Appliance

**FEATURE Tags** (what capability):
- `feature:CLI` — Command-line interface
- `feature:API` — REST/XML API
- `feature:Configuration` — Configuration tasks
- `feature:Deployment` — Deployment and setup
- `feature:Monitoring` — Monitoring and diagnostics
- `feature:UI` — Web UI documentation

**CONTENT Tags** (what topic):
- `content:Commands` — Command definitions and usage
- `content:Compatibility` — Firmware/hardware compatibility
- `content:Upgrade` — Upgrade procedures and paths
- `content:BestPractices` — Design and operational guidance
- `content:Troubleshooting` — Problem diagnosis and resolution
- `content:Diagnostics` — Diagnostic tools and procedures
- `content:Integration` — Integration with external systems
- `content:Deployment` — Deployment guidelines

### Document Search Strategy

1. **If looking for CLI commands:** Search `type:CLI` + relevant `scope:` (e.g., `scope:FabricInterconnect`)
2. **If looking for compatibility/firmware:** Search `scope:Firmware` + `mode:` (e.g., `mode:IMM`)
3. **If looking for configuration:** Search `type:Guide` + `feature:Configuration`
4. **If troubleshooting:** Search `type:Troubleshooting` OR `content:Troubleshooting`
5. **If looking for API info:** Search `type:API` + `mode:` (e.g., `mode:Intersight`)
6. **If needing architecture/design:** Search `type:Architecture` + `content:BestPractices`

---

## Step 2: Search the MCP Server

Use the `ucs-docs` MCP server to search for specific information:
- Start with targeted keyword searches based on the user's question
- If initial search doesn't yield enough results, refine using related keywords
- Keep searching until you have enough information for a complete, accurate answer

**Search Tips:**
- Use keywords from the question itself (command names, device types, feature names)
- Use tags from the index to help guide your search focus
- Search for multiple related topics if needed
- Always read the full document section, not just snippet results

---

## Step 3: Format Your Response

Provide answers in this exact order:

### User's Question
State the original question or query string.

### Document Lookup Strategy
Briefly explain which documents you consulted and why (reference the tags/sections from `docs-index.md`).

### Full Source Content
**Provide the complete relevant paragraph/section from the source document first.** This is the primary answer content.

Format:
```
**From [Document Title]** ([filename.md](#file-path-with-anchor)):

[Full paragraph or section text from the document]
```

### Answer Summary with Source Link
After the full content, provide a concise summary with a clickable link to the exact location.

Format:
```
**Answer:** [Concise 1-2 sentence summary]

**Source:** [Document Title](ucs-docs/filename.md) — [Specific Section](#section-anchor)
```

### 20-Word Summary
Provide a 20-word summary of the complete answer at the very end.

---

## Example Output Format

**User's Question:** "What CLI command upgrades fabric interconnect firmware in IMM mode?"

**Document Lookup Strategy:** 
Used `docs-index.md` with tags `type:CLI` + `scope:FabricInterconnect` + `mode:IMM` to identify "Intersight SaaS Device Console" as the relevant document.

**Full Source Content:**

**From Intersight SaaS Device Console** ([intersight-saas_device_console.md](#fabric-interconnect-cli)):

The `upgrade-equipment` command is used to upgrade the server's BMC and BIOS firmware. This command is available in the device console for fabric interconnects operating in IMM mode. TFTP is not a secure protocol, so this command should only be used in trusted networks.

**Answer Summary:**

**Answer:** Use the `upgrade-equipment` CLI command to upgrade fabric interconnect firmware in IMM mode. TFTP must be available and network is assumed to be trusted.

**Source:** [Intersight SaaS Device Console](ucs-docs/intersight-saas_device_console.md#fabric-interconnect-cli)

**20-Word Summary:** Use upgrade-equipment CLI command for fabric interconnect firmware in IMM mode, requires trusted network with TFTP access.

---

## Key Principles

✓ **Use docs-index.md first** to identify relevant documents before searching  
✓ **Consult tags** to narrow search scope and read fewer documents  
✓ **Provide full paragraphs** as the primary content, not just snippets  
✓ **Include clickable links** to source files and sections  
✓ **Always cite sources** with filename and section  
✓ **Keep searching** until you have a complete, accurate answer  
✓ **Don't stop searching** after first result—verify with additional sources if needed  

---

## Output Checklist

Before providing your final answer, verify:

- [ ] Question or query string stated clearly
- [ ] Document lookup strategy explained (which docs/tags used)
- [ ] Full relevant paragraph/section from source provided first
- [ ] Document title and clickable link included with full content
- [ ] Concise answer summary provided after full content
- [ ] Source filename and section link included
- [ ] 20-word summary at the end
- [ ] All information sourced from MCP `ucs-docs` server
- [ ] Multiple sources consulted if appropriate
