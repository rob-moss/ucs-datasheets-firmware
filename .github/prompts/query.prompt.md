---
name: query
description: Queries docs and help files
---
Query guides in the following directories to answer user questions.
- `ucs-guides-help-query/*.md`
- `ucs-firmware-docs/*.md`


Process:
1. Identify relevant guide(s) from the query topic
2. Search guide(s) efficiently using grep/semantic search
3. Provide concise answer with file references
4. State if information is unavailable

Use subagents to query each directory separately and combine results if needed.
Use parallel processing to query multiple directories at once if applicable.

Be direct and cite specific guide sections when found.
