# UCS Docs MCP Server

A [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server that exposes Cisco UCS documentation to AI assistants such as GitHub Copilot in Visual Studio Code.

The server reads the Markdown files stored in `ucs-docs/`, `ucs-guides-help-query/`, and `ucs-firmware-docs/` and provides tools for listing, searching, reading, and navigating them.

---

## Prerequisites

Python 3.10+ with the project virtual environment active.

Install the MCP dependency:

```bash
# From the repo root
source .venv/bin/activate
pip install -r mcp/requirements.txt
```

Or with `uv`:

```bash
uv pip install -r mcp/requirements.txt
```

---

## Starting the MCP server

The server uses **stdio** transport. In normal use it is launched automatically by VS Code (see next section). To start it manually for testing:

```bash
# From the repo root
source .venv/bin/activate
python mcp/server.py
```

The server listens for JSON-RPC messages on stdin/stdout and prints status to stderr. Press `Ctrl+C` to stop it.

> **Note:** You do not need to start the server manually when using it through VS Code — VS Code manages the process lifecycle automatically.

---

## Connecting Visual Studio Code to the MCP server

The server is pre-registered in `.vscode/mcp.json`. VS Code detects this file automatically and starts the server when it is needed.

### Step-by-step

1. **Open the workspace** in VS Code (the root `ucs-datasheets-firmware/` folder).

2. **Verify `.vscode/mcp.json`** contains the `ucs-docs` entry:
   ```json
   {
     "servers": {
       "ucs-docs": {
         "command": "/path/to/.venv/bin/python",
         "args": ["/path/to/mcp/server.py"]
       }
     }
   }
   ```
   The file already contains the correct paths for this repository.

3. **Open Copilot Chat** (`` Ctrl+Alt+I `` / `` Cmd+Alt+I ``).

4. **Switch to Agent mode** — click the mode selector in the chat input and choose **Agent**.

5. **Confirm the server is available** — the `ucs-docs` tools should appear in the tools list. You can type a query directly (the agent will call the appropriate tool automatically).

---

## Querying the MCP server

Once connected via Copilot Chat in Agent mode, type questions in plain English. The agent searches the documentation automatically. You do not need to invoke tools by name — just ask your question.

### Available tools (called automatically by the agent)

| Tool | What it does |
|------|--------------|
| `list_documents` | Lists every available documentation file with title, source URL, fetch date, and file size |
| `search_documents` | Full-text keyword search across all docs; returns ranked snippets |
| `read_document` | Returns the full Markdown content of a specific file |
| `get_document_outline` | Returns the heading tree (table of contents) for a file |
| `read_document_page` | Reads a single page/chapter from a multi-page document |

### Tips for better results

- Ask specific, action-oriented questions: *"How do I..."*, *"What is the CLI command for..."*
- Include product context: *UCS Manager*, *Intersight*, *Service Profile*, *Fabric Interconnect*
- If an answer is too brief, follow up with: *"Show me more detail from the documentation"*

---

## Example queries and expected output

### 1. How do I change the Fabric Interconnect cluster lead?

**Query:**
```
How do I change the Fabric Interconnect cluster lead?
```

**Expected response (summary):**
The agent searches UCS Manager documentation and returns the relevant procedure. Example output:

> To change the cluster lead in UCS Manager:
>
> 1. In the Navigation pane, click **Equipment**.
> 2. Expand **Equipment** > **Fabric Interconnects** and select the desired Fabric Interconnect.
> 3. In the Work pane click the **General** tab.
> 4. In the **Actions** area, click **Make Primary** (or equivalent command depending on release).
>
> Alternatively, via CLI:
> ```
> UCS-A# connect local-mgmt
> UCS-A(local-mgmt)# cluster lead b
> ```
> The command promotes Fabric Interconnect B to cluster lead.
>
> *Source: Cisco UCS Manager Infrastructure Management Guide, Release 4.3*

---

### 2. How do I set a Firmware policy on a UCS Service Profile?

**Query:**
```
How do I set a Firmware policy on a UCS Service Profile?
```

**Expected response (summary):**

> A **Host Firmware Package** policy controls the firmware versions applied to servers associated with a Service Profile.
>
> **GUI steps:**
> 1. Navigate to **Servers** > **Policies** > **root** > **Host Firmware Packages**.
> 2. Click **Create Host Firmware Package**, name the policy, and select the desired blade/rack package versions.
> 3. Open the target Service Profile (or Service Profile Template) under **Servers** > **Service Profiles**.
> 4. On the **Policies** tab, set the **Host Firmware Package** field to the policy you created.
> 5. Click **Save Changes**.
>
> **CLI steps:**
> ```
> UCS-A# scope org /
> UCS-A /org # create fw-host-pack MyFwPackage
> UCS-A /org/fw-host-pack # set blade-bundle-version 4.3(6c)B
> UCS-A /org/fw-host-pack # commit-buffer
> ```
>
> *Source: Cisco UCS Manager Firmware Management Guide, Release 4.3*

---

### 3. How do I create a Firmware Policy in Intersight Managed Mode?

**Query:**
```
How do I create a Firmware Policy in Intersight Managed Mode?
```

**Expected response (summary):**

> In **Intersight Managed Mode (IMM)**, firmware is managed through a **Firmware Policy** attached to a Server Profile or Server Profile Template.
>
> **Steps:**
> 1. In Intersight, go to **Infrastructure Service** > **Policies** and click **Create Policy**.
> 2. Select **Firmware** as the policy type and choose your target platform (e.g. UCS Server).
> 3. Specify the target firmware bundle version for the server components (CIMC, BIOS, adapters).
> 4. Assign the policy to a **Server Profile Template** under **Infrastructure Service** > **Profiles** > **Server Profile Templates**.
> 5. Deploy the template — Intersight will schedule firmware updates on association.
>
> *Source: Cisco UCS Manager / Intersight documentation*

---

### 4. Additional example queries

| Query | What the agent returns |
|-------|------------------------|
| `List all available UCS documentation files` | Table of filenames, source URLs, fetch dates, and sizes |
| `What UCS blade servers support 4.3(6c)?` | Compatibility information from firmware reports |
| `Show me the table of contents for the Getting Started guide` | Heading outline with page numbers |
| `What is the CLI command to show firmware versions on a blade?` | CLI snippet with explanation |
| `How do I upgrade UCS Manager firmware?` | Step-by-step upgrade procedure from the Firmware Management Guide |
| `What VIC adapters are supported on the B200 M6?` | Adapter compatibility table from hardware datasheets |

---

## Adding more documentation

Run the fetcher script from the repo root to download additional Cisco docs. New `.md` files placed in any of the watched directories are picked up automatically on the next request — no server restart is required.

```bash
source .venv/bin/activate
python fetch_cisco_docs.py
```

The server indexes files from these directories:

| Directory | Contents |
|-----------|----------|
| `ucs-docs/` | Converted Markdown from `fetch_cisco_docs.py` |
| `ucs-guides-help-query/` | Additional fetched guide files |
| `ucs-firmware-docs/` | Datasheet and firmware documentation |
