---
name: create-doc-index
description: This prompt creates a comprehensive index of all UCS documentation files with metadata and tags for easy searching.
---

> **Purpose:** Index all UCS documentation files with metadata and create a searchable summary map.
> **Model:** Use an efficient model like GPT-4o mini for quick indexing.
> **MCP Server:** Use `ucs-docs` to gather document information.

# Overview

This prompt creates a comprehensive, searchable index of all UCS documentation files. The resulting `docs-index.md` file serves as a master reference that helps the `query` and `query-mcp` prompts quickly locate the most relevant documentation to search.

## Core Task

For each documentation file available in the UCS MCP server:
1. **List the file** with its filename (MCP identifier)
2. **Extract core metadata:**
   - Document title
   - Primary topics/subject areas
   - Target audience/scope (e.g., "Fabric Interconnect", "IMM Mode", "CLI Reference")
   - Content type (Reference, Guide, Release Notes, etc.)
   - Applicable UCS versions/modes
3. **Generate searchable tags** that capture key concepts and commands
4. **Create a 1-2 line summary** of the document's purpose
5. **Document relationship hints** (cross-references to related documents)

## Instructions

### Step 1: Gather Document Information
Use the `ucs-docs` MCP server to list all available documents.  
For each document, extract:
- Filename (exact MCP identifier for referencing)
- Document title
- Source URL
- Approximate size and scope

### Step 2: Analyze Content Structure  
For each document, use `ucs-docs` get_document_outline or quick search to understand:
- Main sections and topics covered
- Key commands or features documented
- Version/mode applicability (UCS Manager, IMM, Intersight, etc.)
- Device types covered (Fabric Interconnect, Server, Chassis, etc.)

### Step 3: Generate Metadata Tags
Create tags in these categories (use 3-5 tags per category):

**Category Tags:**
- `type:<category>` — Reference, Guide, Release-Notes, Architecture, Troubleshooting, CLI, API, etc.

**Scope Tags:**
- `scope:<area>` — FabricInterconnect, Server, Chassis, Networking, Storage, Security, Firmware, etc.

**Mode Tags:**
- `mode:<mode>` — UCSManager, IMM, Intersight, LegacyUMM, etc.

**Feature Tags:**
- `feature:<feature>` — CLI, API, UI, Monitoring, Configuration, Deployment, etc.

**Content Tags:**
- `content:<topic>` — Commands, Troubleshooting, BestPractices, Compatibility, Upgrade, etc.

### Step 4: Create the Index File

Output to `ucs-docs/docs-index.md` with this structure:

```
# UCS Documentation Index

**Last Updated:** [date]  
**Total Documents:** [count]

---

## Quick Navigation

- [Fabric Interconnect](#fabric-interconnect)
- [Servers](#servers)
- [CLI References](#cli-references)
- [Management Modes](#management-modes)
- [Release Notes](#release-notes)

---

## Fabric Interconnect

### [Document Title](docs-index.md#fabric-interconnect-name)
**File:** `filename.md`  
**Purpose:** One-line summary of what this document covers.  
**Version/Mode:** IMM 4.3+, UCSM 4.2+, etc.  
**Tags:** `type:Reference` `scope:FabricInterconnect` `mode:IMM` `feature:CLI`  
**Key Content:** 
- Topic 1
- Topic 2
- Command examples (if applicable)

**See Also:** [Related Document Title](docs-index.md#related)

---

[Continue for each document section]

## Index by Tag

### type:CLI
- [Document 1](docs-index.md#...)
- [Document 2](docs-index.md#...)

### type:Reference
- [Document 1](docs-index.md#...)

### mode:IMM
- [Document 1](docs-index.md#...)
- [Document 2](docs-index.md#...)

[Continue for all meaningful tags...]

---

## Search Guide for Other Prompts

When `query` or `query-mcp` prompts need to find documentation:
1. **If searching for commands:** Filter by `type:CLI` + relevant scope
2. **If searching for a feature:** Use `feature:<feature>` tags
3. **If unsure about version:** Cross-reference `Version/Mode` field
4. **If need CLI reference:** Look for `type:Reference` + `scope:<device>`
5. **If troubleshooting:** Look for `content:Troubleshooting` + relevant scope
```

### Step 5: Organize by Sections

Group documents into logical sections:
- **Fabric Interconnect** — All FI-related docs
- **Servers** — Server management and firmware
- **CLI References** — Command references
- **Management Modes** — UCSM vs IMM
- **Release Notes** — Version-specific info
- **Intersight SaaS** — Cloud management
- **APIs** — REST/XML API docs
- **Architecture & Design** — Best practices and design guides
- **Troubleshooting** — Diagnostics and troubleshooting

### Step 6: Create Tag Index

At the end, create searchable tag indices so `query` prompts can filter by:
- Content type (Reference, Guide, CLI, API)
- Scope (FabricInterconnect, Server, Networking)
- Mode (IMM, UCSManager)
- Feature (Monitoring, Upgrade, Deployment)
- Version applicability

---

## Success Criteria

✓ All available documents are included  
✓ Each document has 3-5 relevant tags  
✓ Tags are consistent and reusable  
✓ 1-2 line summaries accurately capture purpose  
✓ Internal links enable quick navigation  
✓ Tag index allows filtering by mode, scope, and type  
✓ `query` prompts can reference this to find the right doc faster  

---

## Usage Examples for Other Prompts

**Example 1: Find fabric interconnect CLI reference**
```
"Look in docs-index.md under 'CLI References' → 'Fabric Interconnect'  
Filter by tags: type:CLI + scope:FabricInterconnect + mode:IMM"
```

**Example 2: Find troubleshooting guide**
```
"Search docs-index.md tag index for content:Troubleshooting  
Then look in relevant scope section"
```

**Example 3: Find IMM-specific documentation**
```
"Filter by tag mode:IMM in the tag index"
```
