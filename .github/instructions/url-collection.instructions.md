---
applyTo: "urls.md"
---

# URL Collection Rules For urls.md

When the user asks to pull URLs from a listing page and add them (for example, "all URLs" or "run /addurl for each sub-page"), follow these rules:

1. Treat "all URLs" as exhaustive for relevant page content.
2. Include all sub-pages and downloadable docs linked from the listing content (HTML pages, PDFs, datasheets, spec sheets, ordering guides, support listing pages, and related listing tabs).
3. Do not silently filter out links as "not important" when the user asked for all.
4. Exclude only obvious global navigation/footer/legal/social links unless the user explicitly asks to include those too.
5. For each included URL, apply the `/addurl` workflow:
   - Fetch the URL.
   - Extract its HTML title when possible.
   - Use the title as the link name.
   - Place under the best matching section in `urls.md`; if no fit exists, place under `# New URLs`.
6. Avoid duplicates:
   - Skip exact URL matches already present in `urls.md`.
   - Preserve URL canonical form where practical.
7. Report results clearly:
   - Number of URLs discovered.
   - Number added.
   - Number skipped as duplicates.
   - Any excluded categories (for example global nav/footer) and why.

If scope is ambiguous, ask one clarification before writing (for example: "include footer/nav links too, or only product/document links?").
