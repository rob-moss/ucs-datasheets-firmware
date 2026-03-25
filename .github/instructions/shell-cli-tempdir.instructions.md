---
applyTo: "**"
---

# Shell, CLI, and Temp Directory Rules

Use these rules when running shell or CLI commands in this repository.

## Shell and CLI execution

1. Use non-interactive commands by default.
2. Run commands from the repository root unless a task requires a different working directory.
3. Prefer safe command structure:
   - Use `set -e` for multi-step scripts.
   - Quote variable expansions (for example `"$var"`).
   - Use command chaining with `&&` when later steps depend on earlier success.
4. Prefer reproducible text processing tools (`awk`, `sed`, `grep`, `sort`, `uniq`) for data extraction and transformation.
5. Avoid destructive operations unless explicitly requested.
6. Do not use `sudo`, `rm -rf`, reset/checkout-style git rewrites, or force options unless the user asked for them.
7. Before editing files based on command output, verify results with a quick check (`wc`, `head`, `tail`, `cat`, or targeted search).

## Temp directory usage

1. Use temporary files/directories for intermediate artifacts, not repository files.
2. Always use the repository-local `tmpdir` directory for temporary artifacts.
3. If needed, create it with `mkdir -p tmpdir` before use.
4. Name temp artifacts with clear prefixes (for example `ucs-links-*`) to aid debugging.
5. Treat temp outputs as ephemeral:
   - Never commit temp files.
   - Clean up files inside `tmpdir` when they are no longer needed.
6. If a temp result becomes important, copy only the final artifact into a tracked project file.

## Output and reporting

1. Summarize what was executed and why.
2. Report counts and outcomes for extraction tasks (discovered, filtered, added, skipped).
3. If command behavior is ambiguous or environment-limited, state the limitation and suggest the next best command.

## Tool approval minimization

Use tools that typically do not require repeated approval first, and only escalate when needed.

1. Preferred tools (default): `read_file`, `file_search`, `grep_search`, `list_dir`, `apply_patch`, `create_file`, `get_errors`, `get_changed_files`.
2. Avoid `run_in_terminal`, `fetch_webpage`, browser tools, and subagents unless the task cannot be completed with preferred tools.
3. If escalation is necessary, combine related work into as few tool calls as practical.
4. For URL extraction and text processing tasks, prefer repository scripts and workspace file tools over ad-hoc shell pipelines.
5. If a non-preferred tool is required, briefly state why before using it.
