#!/usr/bin/env python3
"""
Fetch Cisco UCSM Recommended Firmware Versions (v4 — requests only)
====================================================================
Runs on any vanilla Linux/macOS host with only the 'requests' package.

  pip install requests

How it works
------------
software.cisco.com is an Angular SPA protected by Akamai Edge.  Plain GET
requests receive HTTP 403 — but only because Akamai checks for session
cookies that the browser normally acquires on the first page load.

Two-step approach using a persistent requests.Session:
  1. GET the download page  →  Akamai + Cisco set JSESSIONID / swsession.
  2. GET the catalog API    →  Returns the full JSON release catalog.

Catalog API endpoint (discovered from the Angular bundle chunk-CMUZA25P.js):
  https://software.cisco.com/services/catalog/v1/releases?mdfid={mdfid}&softwareId={softwareId}

The mdfid and softwareId values are embedded in the download page URL:
  .../download/home/{mdfid}/type/{softwareId}/release/

JSON response structure:
  {
    "suggestedRelease": [ {"releaseVersion": "6.0(1e)", "isSuggested": "Y", ...}, ... ],
    "latestRelease":    [...],
    "allRelease":       [...],
    "deferredRelease":  [...],
    "betaRelease":      [...]
  }

Results are cached in recommended-firmware/jsonfiles/ for 24 hours.
"""

# Version 4.0 - complete rewrite with requests only, no Selenium or Playwright dependencies.


import json
import re
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

import requests as _requests

VERSION_RE = re.compile(r"^\d+\.\d+\(\d+\w*\)$")

# ---------------------------------------------------------------------------
# Targets
# ---------------------------------------------------------------------------
TARGETS = [
    {
        "heading": "Recommended firmware versions for Infrastructure",
        "intro":   "The recommended firmware versions for Cisco UCS Manager are",
        "url":     "https://software.cisco.com/download/home/283612660/type/283655658/release/",
    },
    {
        "heading": "Recommended firmware versions for Cisco UCS Blades",
        "intro":   "The recommended firmware versions for Cisco UCS Blades are",
        "url":     "https://software.cisco.com/download/home/283853163/type/283655681/release/",
    },
    {
        "heading": "Recommended firmware versions for Cisco UCS C-Series rack servers",
        "intro":   "The recommended firmware versions for Cisco UCS C-series rack servers are",
        "url":     "https://software.cisco.com/download/home/283862063/type/283655681/release/",
    },
]

# OUTPUT_PATH = Path(__file__).parent.parent / "ucs-docs" / "ucsm-recommended-firmware.md"
OUTPUT_PATH = Path(__file__).parent.parent / "ucs-docs" / "recommended-firmware-ucsm.md"

CATALOG_BASE = "https://software.cisco.com/services/catalog/v1/releases"

# ---------------------------------------------------------------------------
# Cache
# ---------------------------------------------------------------------------
CACHE_DIR     = Path(__file__).parent / "jsonfiles"
CACHE_MAX_AGE = timedelta(hours=24)

UA = (
    "Mozilla/5.0 (X11; Linux x86_64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/126.0.0.0 Safari/537.36"
)


def _api_url(page_url: str) -> str:
    """Derive the catalog API URL from the download page URL.

    Page URL pattern:  .../download/home/{mdfid}/type/{softwareId}/release/
    API URL pattern:   .../services/catalog/v1/releases?mdfid={mdfid}&softwareId={softwareId}
    """
    m = re.search(r"/home/(\d+)/type/(\d+)", page_url)
    if not m:
        raise ValueError(f"Cannot extract mdfid/softwareId from URL: {page_url}")
    return f"{CATALOG_BASE}?mdfid={m.group(1)}&softwareId={m.group(2)}"


def _cache_path(api_url: str) -> Path:
    slug = re.sub(r"https?://[^/]+", "", api_url)
    slug = re.sub(r"[^\w]", "_", slug).strip("_")[:100]
    return CACHE_DIR / f"{slug}.json"


def _load_cache(api_url: str) -> dict | None:
    path = _cache_path(api_url)
    if not path.exists():
        return None
    age = datetime.now() - datetime.fromtimestamp(path.stat().st_mtime)
    if age > CACHE_MAX_AGE:
        print(f"  [CACHE] expired ({str(age).split('.')[0]} old) — re-fetching")
        return None
    print(f"  [CACHE] hit ({str(age).split('.')[0]} old): {path.name}")
    return json.loads(path.read_text())


def _save_cache(api_url: str, data: dict) -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    path = _cache_path(api_url)
    path.write_text(json.dumps(data))
    n = len(data.get("suggestedRelease") or [])
    print(f"  [CACHE] saved {n} suggested releases → {path.name}")


# ---------------------------------------------------------------------------
# Parse
# ---------------------------------------------------------------------------
def _parse_suggested(data: dict) -> list[str]:
    """Return version strings from the 'suggestedRelease' list.

    Falls back to filtering 'allRelease' by isSuggested=='Y' if the
    dedicated key is absent or empty.
    """
    releases = data.get("suggestedRelease") or []
    if not releases:
        releases = [r for r in (data.get("allRelease") or []) if r.get("isSuggested") == "Y"]

    versions: list[str] = []
    seen: set[str] = set()
    for rel in releases:
        v = rel.get("releaseVersion", "").strip()
        if v and VERSION_RE.match(v) and v not in seen:
            versions.append(v)
            seen.add(v)
    return versions


# ---------------------------------------------------------------------------
# Fetch
# ---------------------------------------------------------------------------
def try_requests(page_url: str) -> list[str] | None:
    """Fetch the catalog API response and return suggested release versions.

    Step 1 — GET the download page with a fresh requests.Session.
             Cisco / Akamai set JSESSIONID + swsession cookies on the response.
    Step 2 — GET the catalog API using the same session (cookies ride along).
             The API returns a JSON dict with a 'suggestedRelease' list.
    """
    print("\n[requests] Fetching catalog API ...")
    api_url = _api_url(page_url)

    # Serve from JSON cache if still fresh.
    data = _load_cache(api_url)
    if data is not None:
        versions = _parse_suggested(data)
        if versions:
            print(f"  [OK] {versions}")
            return versions
        print("  [WARN] cached response has no suggested versions — re-fetching")

    try:
        sess = _requests.Session()
        sess.headers["User-Agent"] = UA

        # Step 1: load the page to acquire session cookies.
        print(f"  Loading page for session cookies ...")
        r1 = sess.get(page_url, timeout=20)
        r1.raise_for_status()

        # Step 2: call the catalog API (session cookie jar is populated).
        ts = int(time.time() * 1000)
        print(f"  Calling catalog API ...")
        r2 = sess.get(
            f"{api_url}&ts={ts}",
            headers={
                "Accept":  "application/json, text/plain, */*",
                "Referer": page_url,
            },
            timeout=20,
        )
        r2.raise_for_status()
        data = r2.json()

    except Exception as exc:
        print(f"  [ERROR] {exc}")
        return None

    _save_cache(api_url, data)

    versions = _parse_suggested(data)
    if versions:
        print(f"  [OK] {versions}")
        return versions

    print("  [FAIL] API responded but 'suggestedRelease' list is empty.")
    print(f"  [DEBUG] Response keys: {list(data.keys()) if isinstance(data, dict) else type(data)}")
    return None


# ---------------------------------------------------------------------------
# Markdown writer
# ---------------------------------------------------------------------------
def write_markdown(results: list[dict], output_path: Path) -> None:
    lines: list[str] = []
    for entry in results:
        versions = entry.get("versions") or []
        base_url = entry["url"].rstrip("/")

        lines.append(f"### {entry['heading']}")
        lines.append(f"{entry['intro']}:")
        lines.extend(f"- {v}" for v in versions) if versions else lines.append("- (no versions found)")
        lines.append("")
        lines.append("Source:")
        lines.extend(f"- {base_url}/{v}" for v in versions) if versions else lines.append(f"- {base_url}/")
        lines.append("")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"\n[REPORT] Written to {output_path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    print("=" * 60)
    print("Cisco UCS — Recommended Firmware Fetcher (v4)")
    print(f"Targets: {len(TARGETS)}")
    print(f"Output:  {OUTPUT_PATH}")
    print("=" * 60)

    results: list[dict] = []
    any_failed = False

    for target in TARGETS:
        print(f"\n--- {target['heading']} ---")

        versions = try_requests(target["url"])
        if not versions:
            print("  [FAIL] Could not retrieve versions.")
            any_failed = True

        results.append({**target, "versions": versions})

    write_markdown(results, OUTPUT_PATH)

    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    for entry in results:
        status = "OK" if entry.get("versions") else "FAIL"
        print(f"  [{status}] {entry['heading']}")
        for v in (entry.get("versions") or []):
            print(f"         {v}")

    if any_failed:
        print("\n[WARN] One or more targets failed.")
        sys.exit(1)


if __name__ == "__main__":
    main()
