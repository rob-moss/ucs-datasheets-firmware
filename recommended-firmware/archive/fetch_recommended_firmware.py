#!/usr/bin/env python3
"""
Fetch Cisco UCSM Recommended Firmware Versions
===============================================
Tries three methods in order:
  1. requests + BeautifulSoup  (fast, but Cisco CDN blocks bots - 403)
  2. Selenium                  (headless Chrome with anti-detection stealth flags)
  3. Playwright                (headless Chrome with anti-detection stealth flags)

Key finding: software.cisco.com is protected by Akamai Edge.
  - Plain requests/BeautifulSoup receives HTTP 403.
  - Headless browsers without stealth flags receive Access Denied.
  - Playwright/Selenium with --disable-blink-features=AutomationControlled
    plus navigator.webdriver override bypasses the protection successfully.

Target URL: https://software.cisco.com/download/home/283612660/type/283655658/release/

The page is an Angular SPA. The left-side tree shows release categories:
  Suggested Release -> 6.0(1e), 4.3(6e), 4.2(3p)   <- we want these three
  Latest Release    -> 4.3(6f), 6.0(1f), ...
  All Release       -> ...
  Deferred Release  -> ...
"""

import re
import sys
import time

TARGET_URL = "https://software.cisco.com/download/home/283612660/type/283655658/release/"
VERSION_RE = re.compile(r"^\d+\.\d+\(\d+\w*\)$")

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

# JavaScript executed inside the live page to extract Suggested Release versions
EXTRACT_JS = """
() => {
    const versionRE = /^\\d+\\.\\d+\\(\\d+\\w*\\)$/;
    const versions = [];
    const seen = new Set();
    document.querySelectorAll('tree-node').forEach(node => {
        if (!node.textContent.includes('Suggested Release')) return;
        node.querySelectorAll('span').forEach(span => {
            const t = span.textContent.trim();
            if (versionRE.test(t) && !seen.has(t)) {
                seen.add(t);
                versions.push({ version: t, id: span.id || '', cls: span.className || '' });
            }
        });
    });
    return versions;
}
"""


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
            versions.append(v)
            seen.add(v)

    # Walk the Angular tree-node structure.
    # The key insight: the Suggested Release tree-node-level-1 element contains
    # ONLY the label span + the 3 version child nodes.  We find the first
    # tree-node whose DIRECT text node is just "Suggested Release", then gather
    # version strings from its direct tree-node-level-2 children.
    # Because BeautifulSoup can't run JS we use a structural heuristic:
    # find every span that:
    #   (a) looks like a version, AND
    #   (b) its nearest tree-node ancestor itself only mentions "Suggested Release"
    #       (not "Latest Release", "All Release", etc.) as its first non-empty label.
    CATEGORY_LABELS = ("Latest Release", "All Release", "Deferred Release")
    for span in soup.find_all("span"):
        text = span.get_text(strip=True)
        if not VERSION_RE.match(text):
            continue
        # Walk up to the nearest tree-node ancestor
        node = span.parent
        nearest_tree_node = None
        while node and node.name not in ("[document]", None):
            if node.name == "tree-node":
                nearest_tree_node = node
                break
            node = node.parent
        if not nearest_tree_node:
            continue
        # Walk further up to the level-1 group tree-node
        parent_node = nearest_tree_node.parent
        while parent_node and parent_node.name not in ("[document]", None):
            if parent_node.name == "tree-node":
                break
            parent_node = parent_node.parent
        if not parent_node or parent_node.name != "tree-node":
            continue
        group_text = parent_node.get_text(" ", strip=True)
        # Accept only if within Suggested Release group and not a broader category
        if "Suggested Release" not in group_text:
            continue
        if any(lbl in group_text[:30] for lbl in CATEGORY_LABELS):
            continue
        if text not in seen:
            versions.append(text)
            seen.add(text)

    return versions


# ---------------------------------------------------------------------------
# Method 1: requests + BeautifulSoup
# ---------------------------------------------------------------------------
def try_requests() -> list[str] | None:
    print("\n[Method 1] Trying requests + BeautifulSoup ...")
    try:
        import requests

        headers = {
            "User-Agent": STEALTH_UA,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
        }
        resp = requests.get(TARGET_URL, headers=headers, timeout=15)
        resp.raise_for_status()
        html = resp.text
        print(f"  [OK] HTTP {resp.status_code}, {len(html):,} bytes received")

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
def try_selenium() -> list[str] | None:
    print("\n[Method 2] Trying Selenium (headless Chrome + stealth) ...")
    try:
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
            print(f"  Navigating to {TARGET_URL} ...")
            driver.get(TARGET_URL)

            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "selectedRelease"))
            )
            print("  [OK] Angular tree rendered (selectedRelease span found)")
            time.sleep(1.5)

            # Use the same JS extractor as Playwright for accuracy
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
def try_playwright() -> list[str] | None:
    print("\n[Method 3] Trying Playwright (headless Chrome + stealth) ...")
    try:
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

            print(f"  Navigating to {TARGET_URL} ...")
            page.goto(TARGET_URL, wait_until="domcontentloaded", timeout=25_000)

            print("  Waiting for Angular app to render ...")
            try:
                page.wait_for_selector("span#selectedRelease", timeout=15_000)
                print("  [OK] selectedRelease span detected")
            except Exception:
                print("  [WARN] selectedRelease span not found within timeout; continuing ...")

            page.wait_for_timeout(1500)

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
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    print("=" * 60)
    print("Cisco UCS Manager - Recommended Firmware Fetcher")
    print(f"URL: {TARGET_URL}")
    print("=" * 60)

    methods = [
        ("requests + BeautifulSoup", try_requests),
        ("Selenium",                 try_selenium),
        ("Playwright",               try_playwright),
    ]

    final_versions: list[str] | None = None

    for name, method in methods:
        result = method()
        if result:
            final_versions = result
            print(f"\n[SUCCESS] Method '{name}' succeeded.")
            break
        print(f"  -> Method '{name}' did not return versions, trying next ...")

    print("\n" + "=" * 60)
    if final_versions:
        print("UCSM Suggested / Recommended Firmware Releases:")
        for i, v in enumerate(final_versions, 1):
            print(f"  {i}. {v}")
    else:
        print("[FAIL] All three methods failed. Cannot retrieve firmware versions.")
        print("       Check network access and that Google Chrome is installed.")
        sys.exit(1)

    print("=" * 60)


if __name__ == "__main__":
    main()
