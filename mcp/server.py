#!/usr/bin/env python3
"""
UCS Docs MCP Server

An MCP server that exposes Cisco UCS documentation (stored as Markdown files
in the ucs-guides-help-query directory) to AI assistants via the Model Context
Protocol.

Run from the command line:
    python mcp/server.py

Or with uv:
    uv run mcp/server.py
"""

import os
import re
import sys
from pathlib import Path
from typing import Optional

from mcp.server.fastmcp import FastMCP

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# Resolve the docs directories relative to this file so the server works
# regardless of the working directory it is launched from.
_HERE = Path(__file__).parent.resolve()
DOCS_DIRS: list[Path] = [
    _HERE.parent / "ucs-docs",
    _HERE.parent / "ucs-guides-help-query",
    _HERE.parent / "ucs-firmware-docs",
#    _HERE.parent / "ucs-docs-raw",
]

# File patterns to include
DOCS_GLOB = "*.md"

# How many characters of context to return around a search hit
SEARCH_CONTEXT_CHARS = 800

# Maximum number of search hits returned per document
MAX_HITS_PER_DOC = 5

# Stop words stripped from queries before keyword matching
_STOP_WORDS = frozenset({
    "a", "an", "the", "is", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "do", "does", "did", "will", "would", "could",
    "should", "may", "might", "shall", "can", "need",
    "to", "of", "in", "for", "on", "with", "at", "by", "from",
    "as", "into", "through", "during", "before", "after",
    "between", "out", "or", "and", "but", "not", "so",
    "this", "that", "these", "those", "it", "its",
    "what", "which", "who", "how", "when", "where", "why",
    "i", "me", "my", "we", "our", "you", "your",
    "he", "she", "they", "them", "their",
})

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _doc_files() -> list[Path]:
    """Return all Markdown files across all docs directories, sorted by name."""
    files: list[Path] = []
    for docs_dir in DOCS_DIRS:
        if docs_dir.is_dir():
            files.extend(docs_dir.glob(DOCS_GLOB))
    return sorted(files)


def _find_doc(filename: str) -> Path | None:
    """Search all DOCS_DIRS for a file by name. Returns the first match or None."""
    for docs_dir in DOCS_DIRS:
        candidate = docs_dir / filename
        if candidate.exists():
            return candidate
    return None


def _parse_metadata(text: str) -> dict:
    """Extract the source URL and fetch date from the file header."""
    url = None
    fetched = None

    url_match = re.search(r"^#\s+Documentation:\s+(https?://\S+)", text, re.MULTILINE)
    if url_match:
        url = url_match.group(1).strip()

    date_match = re.search(r"\*Fetched on:\s+([^*]+)\*", text)
    if date_match:
        fetched = date_match.group(1).strip()

    return {"source_url": url, "fetched_on": fetched}


def _extract_sections(text: str) -> list[dict]:
    """
    Split the document into page-level sections delimited by ## Page N: headings.
    Returns a list of dicts with keys: heading, url, content.
    """
    # Split on ## Page N: lines
    pattern = re.compile(r"^(##\s+Page\s+\d+:\s+(https?://\S+))", re.MULTILINE)
    parts = pattern.split(text)

    # parts layout when there are matches:
    # [preamble, full_heading, url, body, full_heading, url, body, ...]
    if len(parts) == 1:
        # No page sections — treat the whole file as one section
        return [{"heading": "Document", "url": None, "content": text.strip()}]

    sections = []
    # parts[0] is the preamble (metadata header), skip it
    i = 1
    while i + 2 < len(parts):
        heading = parts[i].strip()
        url = parts[i + 1].strip()
        content = parts[i + 2].strip()
        sections.append({"heading": heading, "url": url, "content": content})
        i += 3

    return sections


def _tokenize(query: str) -> list[str]:
    """
    Split a natural-language query into meaningful lowercase tokens.
    Drops stop words and single-character tokens.
    """
    tokens = re.findall(r"[a-z0-9][a-z0-9_-]*", query.lower())
    filtered = [t for t in tokens if t not in _STOP_WORDS and len(t) > 1]
    return filtered if filtered else tokens  # never return empty


def _find_context(text: str, query_lower: str, tokens: list[str]) -> tuple[int, str]:
    """
    Find the best snippet window in *text* for the given query.
    Tries exact phrase first, then the first keyword token.
    Returns (match_count, snippet).
    """
    text_lower = text.lower()
    match_count = 0

    # Prefer exact phrase position; fall back to first token hit
    pos = text_lower.find(query_lower)
    if pos == -1 and tokens:
        pos = text_lower.find(tokens[0])
    if pos == -1:
        pos = 0

    # Count all keyword occurrences
    for tok in tokens:
        match_count += text_lower.count(tok)

    half = SEARCH_CONTEXT_CHARS // 2
    start = max(0, pos - half)
    end = min(len(text), pos + len(query_lower) + half)
    snippet = text[start:end].strip()
    if start > 0:
        snippet = "\u2026" + snippet
    if end < len(text):
        snippet = snippet + "\u2026"

    return match_count, snippet


def _infer_title(filename: str, metadata: dict) -> str:
    """Attempt a human-readable title from the filename."""
    stem = Path(filename).stem
    # Replace underscores/hyphens with spaces and title-case
    title = stem.replace("_", " ").replace("-", " ").title()
    return title


# ---------------------------------------------------------------------------
# MCP Server
# ---------------------------------------------------------------------------

mcp = FastMCP(
    "ucs-docs",
    instructions=(
        "This server provides access to Cisco UCS documentation fetched from "
        "cisco.com. Use list_documents to see what is available, "
        "search_documents to find relevant sections by keyword, "
        "read_document to retrieve the full content of a file, and "
        "get_document_outline to inspect the structure of a document."
    ),
)


# ---------------------------------------------------------------------------
# Tools
# ---------------------------------------------------------------------------


@mcp.tool()
def list_documents() -> list[dict]:
    """
    List all available UCS documentation files.

    Returns a list of documents, each with:
    - filename: the file name (use this as the identifier for other tools)
    - title: a human-readable title derived from the filename
    - source_url: the original Cisco URL the document was fetched from
    - fetched_on: the date/time the document was downloaded
    - size_kb: approximate file size in KB
    """
    results = []
    for path in _doc_files():
        try:
            text = path.read_text(encoding="utf-8")
            meta = _parse_metadata(text)
            results.append(
                {
                    "filename": path.name,
                    "title": _infer_title(path.name, meta),
                    "source_url": meta.get("source_url"),
                    "fetched_on": meta.get("fetched_on"),
                    "size_kb": round(len(text) / 1024, 1),
                }
            )
        except Exception as exc:
            results.append({"filename": path.name, "error": str(exc)})
    return results


@mcp.tool()
def search_documents(
    query: str,
    filename: Optional[str] = None,
    max_results: int = 10,
) -> list[dict]:
    """
    Search across UCS documentation for the given query string.

    The query is tokenised into keywords so natural-language questions
    (e.g. "what is a policy") work in addition to exact CLI phrases
    (e.g. "show fabric-interconnect").  Sections that match ALL tokens
    are ranked above sections that match only some tokens.

    Args:
        query: The keyword or phrase to search for (case-insensitive).
                Natural language queries are automatically tokenised.
        filename: Optional. Restrict search to a single file.
        max_results: Maximum number of result snippets to return (default 10).

    Returns a list of matches, each with:
    - filename: which file the match was found in
    - page_url: the page URL within the document (if available)
    - snippet: a short excerpt of the surrounding text
    - match_count: total keyword occurrences in that section
    - matched_tokens: which query keywords were found
    """
    query_lower = query.lower().strip()
    tokens = _tokenize(query)
    if filename:
        found = _find_doc(filename)
        files = [found] if found else []
    else:
        files = _doc_files()

    # Bucket results: exact phrase > all tokens matched > partial match
    exact_results: list[dict] = []
    all_token_results: list[dict] = []
    partial_results: list[dict] = []

    for path in files:
        if not path.exists():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except Exception:
            continue

        # Quick pre-filter: skip file entirely if no token appears anywhere
        text_lower = text.lower()
        if not any(tok in text_lower for tok in tokens):
            continue

        sections = _extract_sections(text)
        hits_in_doc = 0

        for section in sections:
            content = section["content"]
            content_lower = content.lower()

            matched = [tok for tok in tokens if tok in content_lower]
            if not matched:
                continue

            match_count, snippet = _find_context(content, query_lower, matched)

            entry = {
                "filename": path.name,
                "page_url": section.get("url"),
                "snippet": snippet,
                "match_count": match_count,
                "matched_tokens": matched,
            }

            if query_lower in content_lower:
                exact_results.append(entry)
            elif len(matched) == len(tokens):
                all_token_results.append(entry)
            else:
                partial_results.append(entry)

            hits_in_doc += 1
            if hits_in_doc >= MAX_HITS_PER_DOC:
                break

    # Merge ranked results
    ranked = exact_results + all_token_results + partial_results

    # Sort each bucket by match_count descending so best snippets come first
    ranked.sort(key=lambda r: len(r["matched_tokens"]) * 1000 + r["match_count"], reverse=True)

    return ranked[:max_results]


@mcp.tool()
def read_document(filename: str, max_chars: int = 0) -> str:
    """
    Read the full content of a documentation file.

    Args:
        filename: The filename returned by list_documents (e.g. 'b_UCSM_CLI_Firmware_Management_Guide_4-3.md').
        max_chars: If > 0, truncate the output to this many characters.

    Returns the Markdown text of the document.
    """
    path = _find_doc(filename)
    if path is None:
        dirs = ", ".join(str(d) for d in DOCS_DIRS)
        return f"Error: file '{filename}' not found in [{dirs}]"

    text = path.read_text(encoding="utf-8")
    if max_chars > 0 and len(text) > max_chars:
        text = text[:max_chars] + f"\n\n[Truncated — {len(text)} total chars, showing first {max_chars}]"
    return text


@mcp.tool()
def get_document_outline(filename: str) -> list[dict]:
    """
    Return the heading structure (table of contents) of a documentation file.

    Args:
        filename: The filename returned by list_documents.

    Returns a list of headings, each with:
    - level: heading level (1 = #, 2 = ##, etc.)
    - text: the heading text
    - page_url: the page URL if this is a ## Page N heading
    """
    path = _find_doc(filename)
    if path is None:
        return [{"error": f"file '{filename}' not found in any docs directory"}]

    text = path.read_text(encoding="utf-8")
    outline = []

    for line in text.splitlines():
        m = re.match(r"^(#{1,6})\s+(.*)", line)
        if not m:
            continue
        level = len(m.group(1))
        heading_text = m.group(2).strip()

        # Extract URL from ## Page N: https://... headings
        page_url = None
        url_match = re.match(r"Page\s+\d+:\s+(https?://\S+)", heading_text)
        if url_match:
            page_url = url_match.group(1)

        outline.append({"level": level, "text": heading_text, "page_url": page_url})

    return outline


@mcp.tool()
def read_document_page(filename: str, page_number: int) -> str:
    """
    Read a single page section from a multi-page documentation file.

    Args:
        filename: The filename returned by list_documents.
        page_number: The 1-based page number (use get_document_outline to find page numbers).

    Returns the Markdown content of that page section.
    """
    path = _find_doc(filename)
    if path is None:
        dirs = ", ".join(str(d) for d in DOCS_DIRS)
        return f"Error: file '{filename}' not found in [{dirs}]"

    text = path.read_text(encoding="utf-8")
    sections = _extract_sections(text)

    if page_number < 1 or page_number > len(sections):
        return (
            f"Error: page {page_number} out of range. "
            f"Document has {len(sections)} section(s)."
        )

    section = sections[page_number - 1]
    header = f"{section['heading']}\n\n" if section.get("heading") else ""
    return header + section["content"]


# ---------------------------------------------------------------------------
# Resources
# ---------------------------------------------------------------------------


@mcp.resource("docs://index")
def docs_index() -> str:
    """A Markdown index of all available UCS documentation files."""
    lines = ["# UCS Documentation Index\n"]
    for path in _doc_files():
        try:
            text = path.read_text(encoding="utf-8")
            meta = _parse_metadata(text)
            title = _infer_title(path.name, meta)
            url = meta.get("source_url", "")
            fetched = meta.get("fetched_on", "unknown")
            lines.append(f"## [{title}](docs://{path.name})")
            if url:
                lines.append(f"- **Source:** {url}")
            lines.append(f"- **Fetched:** {fetched}")
            lines.append(f"- **File:** `{path.name}`\n")
        except Exception as exc:
            lines.append(f"## {path.name}\n- Error: {exc}\n")
    return "\n".join(lines)


@mcp.resource("docs://{filename}")
def doc_resource(filename: str) -> str:
    """Read a documentation file by name."""
    path = _find_doc(filename)
    if path is None:
        return f"# Error\nFile `{filename}` not found in any docs directory."
    return path.read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    mcp.run(transport="stdio")
