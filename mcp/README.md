# UCS Docs MCP Server

A Model Context Protocol (MCP) server that exposes Cisco UCS documentation to AI assistants such as GitHub Copilot in Visual Studio Code.

The server reads the Markdown files fetched into the `ucs-guides-help-query` directory and provides tools for listing, searching, and reading them.

---

## Prerequisites

Python 3.10+ and the `mcp` package. Install into the project virtual environment:

```bash
# From the repo root (virtual environment must be active)
pip install -r mcp/requirements.txt
```

Or use `uv`:

```bash
uv pip install -r mcp/requirements.txt
```

---

## Running the server

The server uses **stdio** transport — it is launched automatically by VS Code.

To test it manually from the command line:

```bash
# Activate the venv first
source .venv/bin/activate

python mcp/server.py
```

The server waits for JSON-RPC messages on stdin/stdout. Use `Ctrl+C` to stop it.

---

## VS Code / GitHub Copilot integration

The server is registered in `.vscode/mcp.json`. Once the file is saved VS Code will detect it and make the tools available to Copilot Chat in **Agent mode**.

To verify the server is running, open Copilot Chat, switch to **Agent** mode and type:

```
@workspace use ucs-docs to list all available documents
```

---

## Available tools

| Tool | Description |
|---|---|
| `list_documents` | List every doc file with title, source URL, fetch date, and size |
| `search_documents` | Full-text search across all docs; supports narrowing to a single file |
| `read_document` | Return the full Markdown content of a file |
| `get_document_outline` | Return the heading tree (table of contents) for a file |
| `read_document_page` | Return a single numbered page section from a multi-page document |

## Available resources

| URI | Description |
|---|---|
| `docs://index` | Markdown index of all documentation files |
| `docs://{filename}` | Raw content of any documentation file |

---

## Adding more documents

Run the fetcher script to download additional Cisco docs:

```bash
cd ucs-guides-help-query
python fetch_cisco_docs.py
```

New `.md` files placed in `ucs-guides-help-query/` are picked up automatically — no server restart is required for `search_documents` or `read_document` as files are read on each request.
