#!/usr/bin/env python3
"""
Fetch Cisco UCSM Recommended Firmware Versions (v3)
=====================================================
Tries three methods in order for each target URL:
  1. requests + BeautifulSoup  (fast, but Cisco CDN blocks bots - 403)
  2. Selenium                  (headless Chrome with anti-detection stealth flags)
  3. Playwright                (headless Chrome with anti-detection stealth flags)

Key finding: software.cisco.com is protected by Akamai Edge.
  - Plain requests/BeautifulSoup receives HTTP 403.
  - Headless browsers without stealth flags receive Access Denied.
  - Playwright/Selenium with --disable-blink-features=AutomationControlled
    plus navigator.webdriver override bypasses the protection successfully.

Targets:
  - UCS Infrastructure  (UCSM)
  - UCS B-Series Blade servers
  - UCS C-Series Rack servers

The page is an Angular SPA. The left-side tree shows release categories:
  Suggested Release -> 6.0(1e), 4.3(6e), 4.2(3p)   <- we want these three
  Latest Release    -> 4.3(6f), 6.0(1f), ...
  All Release       -> ...
  Deferred Release  -> ...

v2 change: version spans are only accepted when their parent element also
contains a sibling span with class 'icon-software-suggested' (the gold star
icon that Cisco renders alongside each Suggested/Recommended release):

  <span class="icon-software-suggested icon-small suggestedStar"></span>

This ensures we capture only the truly recommended releases and ignore any
version strings that happen to appear elsewhere in the Suggested Release
category label or surrounding chrome.

v3 change: multiple targets supported; results written to
  ucs-firmware-reports/recommended-firmware.md
"""

import re
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

VERSION_RE = re.compile(r"^\d+\.\d+\(\d+\w*\)$")

# ---------------------------------------------------------------------------
# Fetch targets
# ---------------------------------------------------------------------------
# Each entry: heading (used in markdown ###), intro (sentence before list), url.
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

# Output report path (relative to this script's parent directory)
OUTPUT_PATH = Path(__file__).parent.parent / "ucs-docs" / "ucsm-recommended-firmware.md"

# CSS class that marks a release as Suggested / Recommended by Cisco.
SUGGESTED_ICON_CLASS = "icon-software-suggested"

# ---------------------------------------------------------------------------
# HTML cache settings
# ---------------------------------------------------------------------------
# Resolved relative to this script file so it works regardless of cwd.
CACHE_DIR = Path(__file__).parent / "htmlfiles"
CACHE_MAX_AGE = timedelta(hours=24)

# Stealth Chrome launch arguments (bypass Akamai bot detection)
CHROMIUM_STEALTH_ARGS = [
    "--disable-blink-features=AutomationControlled",
    "--no-sandbox",
    "--disable-dev-shm-usage",
]
STEALTH_INIT_SCRIPT = (
    "Object.defineProperty(navigator, 'webdriver', {get: () => undefined});"
)
STEALTH_UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/145.0.0.0 Safari/537.36"
)

# JavaScript executed inside the live page to extract Suggested Release versions.
# v2: only accepts a version span when its parent element contains a sibling
# <span class="icon-software-suggested ..."> — the gold-star recommended icon.
EXTRACT_JS = """
() => {
    const versionRE = /^\\d+\\.\\d+\\(\\d+\\w*\\)$/;
    const versions = [];
    const seen = new Set();
    document.querySelectorAll('span').forEach(span => {
        const t = span.textContent.trim();
        if (!versionRE.test(t)) return;
        // Accept only if the immediate parent also contains the suggested-release
        // gold-star icon span: <span class="icon-software-suggested ..."></span>
        const parent = span.parentElement;
        if (!parent) return;
        if (!parent.querySelector('span.icon-software-suggested')) return;
        if (!seen.has(t)) {
            seen.add(t);
            versions.push({ version: t, id: span.id || '', cls: span.className || '' });
        }
    });
    return versions;
}
"""


# ---------------------------------------------------------------------------
# Cache helpers
# ---------------------------------------------------------------------------
def _cache_path(url: str) -> Path:
    """Return the local .html cache file path for *url*."""
    slug = re.sub(r"https?://", "", url)
    slug = re.sub(r"[^\w]", "_", slug).strip("_")[:120]
    return CACHE_DIR / f"{slug}.html"


def _load_cache(url: str) -> str | None:
    """Return cached HTML for *url* if it exists and is less than 24 hours old."""
    path = _cache_path(url)
    if not path.exists():
        print(f"  [CACHE] MISS — no cached file: {path.name}")
        return None
    age = datetime.now() - datetime.fromtimestamp(path.stat().st_mtime)
    if age > CACHE_MAX_AGE:
        print(f"  [CACHE] EXPIRED ({str(age).split('.')[0]} old): {path.name}")
        return None
    print(f"  [CACHE] HIT ({str(age).split('.')[0]} old): {path.name}")
    return path.read_text(encoding="utf-8")


def _save_cache(url: str, html: str) -> None:
    """Write *html* to the cache file for *url*."""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    path = _cache_path(url)
    path.write_text(html, encoding="utf-8")
    print(f"  [CACHE] Saved {len(html):,} bytes → {path.name}")


# ---------------------------------------------------------------------------
# HTML-only fallback parser (for static pages or when cookies are provided)
# ---------------------------------------------------------------------------
def _parse_versions_from_html(html: str) -> list[str]:
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, "html.parser")
    versions: list[str] = []
    seen: set[str] = set()

    # The active Suggested Release span carries id="selectedRelease"
    sel = soup.find("span", id="selectedRelease")
    if sel:
        v = sel.get_text(strip=True)
        if VERSION_RE.match(v) and v not in seen:
            # Verify the selectedRelease span's parent also contains the icon.
            parent = sel.parent
            if parent and parent.find("span", class_=SUGGESTED_ICON_CLASS):
                versions.append(v)
                seen.add(v)

    # Walk all version-like spans.
    # v2 filter: only accept a span when its direct parent element also contains
    # a <span class="icon-software-suggested ..."> sibling — the gold-star icon
    # that Cisco renders exclusively next to Suggested/Recommended releases.
    for span in soup.find_all("span"):
        text = span.get_text(strip=True)
        if not VERSION_RE.match(text):
            continue
        if text in seen:
            continue

        parent = span.parent
        if not parent:
            continue

        # Primary filter (v2): sibling icon span must be present.
        if not parent.find("span", class_=SUGGESTED_ICON_CLASS):
            continue

        versions.append(text)
        seen.add(text)

    return versions


# ---------------------------------------------------------------------------
# Method 1: requests + BeautifulSoup
# ---------------------------------------------------------------------------
def try_requests(url: str) -> list[str] | None:
    print("\n[Method 1] Trying requests + BeautifulSoup ...")
    try:
        # Check cache before hitting the network.
        html = _load_cache(url)
        if html is None:
            import requests

            headers = {
                "User-Agent": STEALTH_UA,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.9",
                "Accept-Encoding": "gzip, deflate, br",
            }
            resp = requests.get(url, headers=headers, timeout=15)
            resp.raise_for_status()
            html = resp.text
            print(f"  [OK] HTTP {resp.status_code}, {len(html):,} bytes received")
            _save_cache(url, html)
        else:
            print(f"  [OK] Using cached HTML ({len(html):,} bytes)")

        versions = _parse_versions_from_html(html)
        if versions:
            print(f"  [OK] Found versions: {versions}")
            return versions

        print("  [FAIL] Page fetched but no version spans found.")
        print("         The Angular app was not rendered (expected - JS is required).")
        return None

    except Exception as exc:
        print(f"  [ERROR] {exc}")
        return None


# ---------------------------------------------------------------------------
# Method 2: Selenium (headless Chrome)
# ---------------------------------------------------------------------------
def try_selenium(url: str) -> list[str] | None:
    print("\n[Method 2] Trying Selenium (headless Chrome + stealth) ...")
    try:
        # Use cached rendered HTML if available — avoids launching a browser.
        cached_html = _load_cache(url)
        if cached_html is not None:
            print(f"  [OK] Using cached HTML ({len(cached_html):,} bytes)")
            versions = _parse_versions_from_html(cached_html)
            if versions:
                print(f"  [OK] Found versions: {versions}")
                return versions
            print("  [WARN] Cache hit but parser found no versions; launching browser ...")

        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from webdriver_manager.chrome import ChromeDriverManager

        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1400,900")
        options.add_argument(f"--user-agent={STEALTH_UA}")
        for arg in CHROMIUM_STEALTH_ARGS:
            options.add_argument(arg)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        print("  Locating / installing ChromeDriver ...")
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

        driver.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument",
            {"source": STEALTH_INIT_SCRIPT},
        )

        try:
            print(f"  Navigating to {url} ...")
            driver.get(url)

            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "selectedRelease"))
            )
            print("  [OK] Angular tree rendered (selectedRelease span found)")
            time.sleep(1.5)

            # Save the fully-rendered DOM to the cache.
            _save_cache(url, driver.page_source)

            # Use the JS extractor with the icon-software-suggested filter.
            raw = driver.execute_script(f"return ({EXTRACT_JS})()")
        finally:
            driver.quit()

        print(f"  Raw JS result: {raw}")
        if not raw:
            print("  [FAIL] Page rendered but JS extractor found no versions.")
            return None

        versions = [item["version"] for item in raw]
        print(f"  [OK] Found versions: {versions}")
        return versions

    except Exception as exc:
        print(f"  [ERROR] {exc}")
        return None


# ---------------------------------------------------------------------------
# Method 3: Playwright (headless Chrome, system install)
# ---------------------------------------------------------------------------
def try_playwright(url: str) -> list[str] | None:
    print("\n[Method 3] Trying Playwright (headless Chrome + stealth) ...")
    try:
        # Use cached rendered HTML if available — avoids launching a browser.
        cached_html = _load_cache(url)
        if cached_html is not None:
            print(f"  [OK] Using cached HTML ({len(cached_html):,} bytes)")
            versions = _parse_versions_from_html(cached_html)
            if versions:
                print(f"  [OK] Found versions: {versions}")
                return versions
            print("  [WARN] Cache hit but parser found no versions; launching browser ...")

        from playwright.sync_api import sync_playwright

        with sync_playwright() as pw:
            browser = pw.chromium.launch(
                channel="chrome",
                headless=True,
                args=CHROMIUM_STEALTH_ARGS,
            )
            context = browser.new_context(user_agent=STEALTH_UA)
            page = context.new_page()
            page.add_init_script(STEALTH_INIT_SCRIPT)

            print(f"  Navigating to {url} ...")
            page.goto(url, wait_until="domcontentloaded", timeout=25_000)

            print("  Waiting for Angular app to render ...")
            try:
                page.wait_for_selector("span#selectedRelease", timeout=15_000)
                print("  [OK] selectedRelease span detected")
            except Exception:
                print("  [WARN] selectedRelease span not found within timeout; continuing ...")

            page.wait_for_timeout(1500)

            # Save the fully-rendered DOM to the cache.
            _save_cache(url, page.content())

            raw: list[dict] = page.evaluate(EXTRACT_JS)
            browser.close()

        print(f"  Raw JS result: {raw}")
        if not raw:
            print("  [FAIL] No version spans found after full page render.")
            return None

        versions = [item["version"] for item in raw]
        print(f"  [OK] Found versions: {versions}")
        return versions

    except Exception as exc:
        print(f"  [ERROR] {exc}")
        return None


# ---------------------------------------------------------------------------
# Orchestrator: fetch versions for a single URL using method fallback chain
# ---------------------------------------------------------------------------
def fetch_versions_for(url: str) -> list[str] | None:
    """Try all three methods in order and return the first successful result."""
    methods = [
        ("requests + BeautifulSoup", try_requests),
        ("Selenium",                 try_selenium),
        ("Playwright",               try_playwright),
    ]
    for name, method in methods:
        result = method(url)
        if result:
            print(f"  -> Method '{name}' succeeded.")
            return result
        print(f"  -> Method '{name}' did not return versions, trying next ...")
    return None


# ---------------------------------------------------------------------------
# Markdown writer
# ---------------------------------------------------------------------------
def write_markdown(
    results: list[dict],
    output_path: Path,
) -> None:
    """
    Write the firmware report to *output_path* in Markdown format.

    Each entry in *results* is a dict with keys:
      heading   – the ### section heading string
      intro     – sentence preceding the version bullet list
      url       – base Cisco download URL (version appended per bullet)
      versions  – list of version strings, or None if fetch failed
    """
    lines: list[str] = []
    for entry in results:
        heading  = entry["heading"]
        intro    = entry["intro"]
        base_url = entry["url"].rstrip("/")
        versions = entry.get("versions") or []

        lines.append(f"### {heading}")
        lines.append(f"{intro}:")
        if versions:
            for v in versions:
                lines.append(f"- {v}")
        else:
            lines.append("- (no versions found)")
        lines.append("")
        lines.append("Source:")
        if versions:
            for v in versions:
                lines.append(f"- {base_url}/{v}")
        else:
            lines.append(f"- {base_url}/")
        lines.append("")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"\n[REPORT] Written to {output_path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    print("=" * 60)
    print("Cisco UCS - Recommended Firmware Fetcher (v3)")
    print(f"Targets: {len(TARGETS)}")
    print(f"Filter: sibling span.{SUGGESTED_ICON_CLASS} must be present")
    print(f"Output: {OUTPUT_PATH}")
    print("=" * 60)

    results: list[dict] = []
    any_failed = False

    for target in TARGETS:
        heading = target["heading"]
        url     = target["url"]
        print(f"\n{'=' * 60}")
        print(f"[TARGET] {heading}")
        print(f"         {url}")
        print("=" * 60)

        versions = fetch_versions_for(url)
        if versions:
            print(f"\n  => Versions: {versions}")
        else:
            print("\n  => [FAIL] Could not retrieve versions for this target.")
            any_failed = True

        results.append({
            "heading":  heading,
            "intro":    target["intro"],
            "url":      url,
            "versions": versions,
        })

    # Write the report regardless — partial results are still useful.
    write_markdown(results, OUTPUT_PATH)

    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    for entry in results:
        versions = entry.get("versions") or []
        status   = "OK" if versions else "FAIL"
        print(f"  [{status}] {entry['heading']}")
        for v in versions:
            print(f"         {v}")

    if any_failed:
        print("\n[WARN] One or more targets failed. Check output above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
