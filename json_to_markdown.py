#!/usr/bin/env python3
"""
json_to_markdown.py
Convert JSON/JSONL files to Markdown tables/lists, with a raw JSON appendix.

Usage examples:
  # Drag-and-drop files/folders onto this script (Windows/macOS Finder)
  # or run from a terminal:
  python json_to_markdown.py path/to/folder
  python json_to_markdown.py data1.json data2.json --out md_out
  python json_to_markdown.py . --no-title

Outputs .md files to ./markdown_out by default (or --out). Handles:
  - dict -> Key/Value table
  - list[dict] -> table with union of keys
  - list[scalars] -> bullet list
  - complex nested -> fenced JSON code block
Also appends a collapsible "Raw JSON" section for full fidelity.
"""

import argparse
import json
import sys
import os
from typing import Any, Dict, List

def md_escape(val: str) -> str:
    """Escape characters that break Markdown tables and inline code."""
    if val is None:
        return ""
    s = str(val)
    s = s.replace("|", "\\|")
    s = s.replace("\n", "<br>")
    s = s.replace("\r", "")
    s = s.replace("`", "\\`")
    return s

def is_list_of_dicts(lst: List[Any]) -> bool:
    return isinstance(lst, list) and len(lst) > 0 and all(isinstance(x, dict) for x in lst)

def is_list_of_scalars(lst: List[Any]) -> bool:
    return isinstance(lst, list) and all(not isinstance(x, (dict, list)) for x in lst)

def collect_keys(rows: List[Dict[str, Any]]) -> List[str]:
    keys = set()
    for r in rows:
        keys.update(r.keys())
    return sorted(keys)

def to_inline(value: Any) -> str:
    """Render nested values as inline JSON snippet (compact) or plain string for scalars."""
    if isinstance(value, (dict, list)):
        try:
            return md_escape(json.dumps(value, ensure_ascii=False, separators=(",", ":")))
        except Exception:
            return md_escape(str(value))
    return md_escape(value)

def dict_to_md_table(d: Dict[str, Any]) -> str:
    lines = ["| Key | Value |", "| --- | --- |"]
    for k, v in d.items():
        lines.append(f"| {md_escape(k)} | {to_inline(v)} |")
    return "\n".join(lines)

def list_of_dicts_to_md_table(rows: List[Dict[str, Any]]) -> str:
    headers = collect_keys(rows)
    if not headers:
        return "_(empty list)_"
    head = "| " + " | ".join(md_escape(h) for h in headers) + " |"
    sep = "| " + " | ".join("---" for _ in headers) + " |"
    out = [head, sep]
    for r in rows:
        row = [to_inline(r.get(h, "")) for h in headers]
        out.append("| " + " | ".join(row) + " |")
    return "\n".join(out)

def list_of_scalars_to_md(lst: List[Any]) -> str:
    return "\n".join(f"- {md_escape(x)}" for x in lst)

def value_to_markdown(data: Any) -> str:
    """Top-level renderer. Keeps things simple & readable."""
    if isinstance(data, dict):
        return dict_to_md_table(data)
    if isinstance(data, list):
        if is_list_of_dicts(data):
            return list_of_dicts_to_md_table(data)
        if is_list_of_scalars(data):
            return list_of_scalars_to_md(data)
        # Mixed/complex list → code block
        pretty = json.dumps(data, ensure_ascii=False, indent=2)
        return "```json\n" + pretty + "\n```"
    # scalar
    return md_escape(data)

def try_load_json(path: str) -> Any:
    # First try standard JSON
    with open(path, "r", encoding="utf-8") as f:
        txt = f.read().strip()
    if txt == "":
        return {}
    try:
        return json.loads(txt)
    except Exception:
        # Try JSON Lines (.jsonl)
        lines = [line for line in txt.splitlines() if line.strip()]
        objs = []
        ok = True
        for ln in lines:
            try:
                objs.append(json.loads(ln))
            except Exception:
                ok = False
                break
        if ok and len(objs) > 0:
            return objs
        raise

def process_file(path: str, out_dir: str, add_title: bool = True) -> str:
    data = try_load_json(path)
    stem = os.path.splitext(os.path.basename(path))[0]
    md = []
    if add_title:
        md.append(f"# {stem}")
        md.append("")
    md.append(value_to_markdown(data))
    md.append("")
    # Always include a collapsible pretty JSON section for full fidelity
    try:
        pretty = json.dumps(data, ensure_ascii=False, indent=2)
        md.append("<details><summary>Raw JSON</summary>\n\n```json")
        md.append(pretty)
        md.append("```\n\n</details>")
    except Exception:
        pass

    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{stem}.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    return out_path

def gather_json_files(paths: List[str]) -> List[str]:
    out = []
    for p in paths:
        if os.path.isdir(p):
            for root, _, files in os.walk(p):
                for name in files:
                    if name.lower().endswith((".json", ".jsonl")):
                        out.append(os.path.join(root, name))
        elif os.path.isfile(p) and p.lower().endswith((".json", ".jsonl")):
            out.append(p)
    # Deduplicate while preserving order
    seen = set()
    unique = []
    for p in out:
        if p not in seen:
            unique.append(p)
            seen.add(p)
    return unique

def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Convert JSON/JSONL files to Markdown tables/lists, with a raw JSON appendix."
    )
    parser.add_argument("paths", nargs="*", help="JSON files or directories (drag-and-drop works).")
    parser.add_argument("--out", default="markdown_out", help="Output directory (default: ./markdown_out)")
    parser.add_argument("--no-title", action="store_true", help="Do not add a # Title from the filename.")
    args = parser.parse_args(argv)

    files = gather_json_files(args.paths if args.paths else [os.getcwd()])
    if not files:
        print("No JSON files found.", file=sys.stderr)
        sys.exit(1)

    out_paths = []
    for fpath in files:
        try:
            out_paths.append(process_file(fpath, args.out, add_title=not args.no_title))
        except Exception as e:
            print(f"Failed to convert {fpath}: {e}", file=sys.stderr)

    print("Converted files:")
    for p in out_paths:
        print(p)

if __name__ == "__main__":
    main()
