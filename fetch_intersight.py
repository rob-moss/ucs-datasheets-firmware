#!/usr/bin/env python3
"""
fetch_intersight.py
-------------------
Download a fully JavaScript-rendered Intersight help page using Selenium,
save all raw assets (HTML, CSS, JS), write a self-contained
`intersight-full-page.html`, and convert it to `intersight-full-page.md`.

Usage:
    python fetch_intersight.py [URL]

Default URL:
    https://intersight.com/help/saas/configure/chassis

Output directory: wip/fetch-intersight/

Dependencies (all pip-installable):
    selenium  webdriver-manager  beautifulsoup4  html2text  markdownify

The script uses Selenium with Google Chrome in headless mode.
Chrome / Chromium must be installed on the system.
"""

import argparse
import os
import re
import sys
import time
import urllib.parse
from pathlib import Path

import requests
from bs4 import BeautifulSoup

# ---------------------------------------------------------------------------
# Selenium imports
# ---------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    from webdriver_manager.chrome import ChromeDriverManager
    _WDM_AVAILABLE = True
except ImportError:
    _WDM_AVAILABLE = False

# ---------------------------------------------------------------------------
# HTML → Markdown
# ---------------------------------------------------------------------------
try:
    from markdownify import markdownify as md_convert
    _MARKDOWNIFY_OK = True
except ImportError:
    _MARKDOWNIFY_OK = False

import html2text as _html2text


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
DEFAULT_URL = "https://intersight.com/help/saas/configure/chassis"
OUT_DIR = Path("wip/fetch-intersight")

# How long (seconds) to wait for the main content element or network idle
PAGE_LOAD_TIMEOUT = 90
# Extra settle time after the DOM appears ready (JS frameworks keep rendering)
SETTLE_SECONDS = 12
# Timeout for individual asset downloads
ASSET_TIMEOUT = 20


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _slug(url: str) -> str:
    """Turn a URL into a filesystem-safe slug."""
    parsed = urllib.parse.urlparse(url)
    path = parsed.path.strip("/").replace("/", "_")
    query = parsed.query.replace("=", "-").replace("&", "_")
    name = f"{parsed.netloc}_{path}"
    if query:
        name += f"_{query}"
    return re.sub(r"[^A-Za-z0-9._-]", "_", name)[:200]


def _ext_for_content_type(content_type: str) -> str:
    if "javascript" in content_type:
        return ".js"
    if "css" in content_type:
        return ".css"
    if "html" in content_type:
        return ".html"
    return ".bin"


def _make_chrome_driver() -> webdriver.Chrome:
    """Build a headless Chrome WebDriver, auto-managing the chromedriver binary."""
    opts = ChromeOptions()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--window-size=1920,1080")
    opts.add_argument("--disable-blink-features=AutomationControlled")
    opts.add_experimental_option("excludeSwitches", ["enable-automation"])
    opts.add_experimental_option("useAutomationExtension", False)

    if _WDM_AVAILABLE:
        print("[selenium] Using webdriver-manager to locate/download chromedriver …")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=opts)
    else:
        print("[selenium] webdriver-manager not found – using system chromedriver")
        driver = webdriver.Chrome(options=opts)

    driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    )
    return driver


def _wait_for_content(driver: webdriver.Chrome) -> None:
    """
    Wait until the page looks substantively loaded.

    Intersight help pages are Angular SPAs that embed the real documentation
    content inside one or more iframes (using GWT / user-guide widgets).
    Strategy:
      1. document.readyState == 'complete'
      2. Angular bootstrap marker (ng-version) – optional
      3. Wait for an iframe to appear and for its srcdoc/src to be set
      4. Extra settle time for remaining JS rendering
    """
    wait = WebDriverWait(driver, PAGE_LOAD_TIMEOUT)

    # 1. DOM + subresources loaded
    wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
    print("[selenium] readyState = complete")

    # 2. Try to detect Angular bootstrap (optional – don't fail if absent)
    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[ng-version]"))
        )
        print("[selenium] Angular framework detected and bootstrapped")
    except Exception:
        print("[selenium] Angular marker not found – continuing anyway")

    # 3. Wait for an iframe to appear (the help content is GWT-embedded)
    try:
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.TAG_NAME, "iframe"))
        )
        print("[selenium] iframe element detected")
        # Give it extra time to populate
        time.sleep(4)
    except Exception:
        print("[selenium] No iframe detected – continuing anyway")

    # 4. Wait for any heading or main content block in the outer DOM
    try:
        WebDriverWait(driver, 20).until(
            EC.any_of(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR,
                     "h1, h2, article, main, .help-content, .content-body, "
                     "[class*='content'], [class*='page'], [role='main']")
                ),
            )
        )
        print("[selenium] Content element detected in outer DOM")
    except Exception:
        print("[selenium] Content element not found in outer DOM – continuing")

    # 5. Extra settle time (Angular + GWT keep patching the DOM)
    print(f"[selenium] Waiting {SETTLE_SECONDS}s for JS rendering to settle …")
    time.sleep(SETTLE_SECONDS)


def _scroll_to_bottom(driver: webdriver.Chrome) -> None:
    """Scroll down slowly to trigger any lazy-loading."""
    total_height = driver.execute_script("return document.body.scrollHeight")
    step = 800
    y = 0
    while y < total_height:
        driver.execute_script(f"window.scrollTo(0, {y});")
        time.sleep(0.15)
        y += step
        total_height = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("window.scrollTo(0, 0);")


def _fetch_asset(url: str, out_dir: Path, session: requests.Session) -> Path | None:
    """Download a single CSS / JS asset and return its local path."""
    try:
        resp = session.get(url, timeout=ASSET_TIMEOUT)
        resp.raise_for_status()
        ct = resp.headers.get("content-type", "")
        ext = _ext_for_content_type(ct)
        slug = _slug(url)
        if not slug.endswith(ext):
            slug += ext
        dst = out_dir / slug
        dst.write_bytes(resp.content)
        return dst
    except Exception as exc:
        print(f"  [warn] Could not download asset {url}: {exc}")
        return None


def _collect_assets(soup: BeautifulSoup, base_url: str, out_dir: Path) -> dict[str, str]:
    """
    Download all external CSS and JS referenced in the page.

    Returns a mapping {original_url → local_relative_path} so callers can
    optionally rewrite <link>/<script> tags in the HTML.
    """
    session = requests.Session()
    session.headers["User-Agent"] = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )

    mapping: dict[str, str] = {}
    candidates: list[str] = []

    for tag in soup.find_all("link", rel=lambda v: v and "stylesheet" in v):
        href = tag.get("href", "")
        if href:
            candidates.append(urllib.parse.urljoin(base_url, href))

    for tag in soup.find_all("script", src=True):
        src = tag.get("src", "")
        if src:
            candidates.append(urllib.parse.urljoin(base_url, src))

    total = len(candidates)
    print(f"[assets] Downloading {total} CSS/JS asset(s) …")
    for i, url in enumerate(candidates, 1):
        print(f"  [{i}/{total}] {url[:100]}")
        local = _fetch_asset(url, out_dir, session)
        if local:
            mapping[url] = local.name

    return mapping


def _html_to_markdown(html_content: str, url: str) -> str:
    """Convert rendered HTML to clean Markdown."""
    if _MARKDOWNIFY_OK:
        md = md_convert(
            html_content,
            heading_style="ATX",
            bullets="-",
            strip=["script", "style", "nav", "footer", "header"],
        )
    else:
        h = _html2text.HTML2Text()
        h.ignore_links = False
        h.ignore_images = False
        h.ignore_tables = False
        h.body_width = 0
        h.unicode_snob = True
        h.skip_internal_links = True
        md = h.handle(html_content)

    # Deduplicate blank lines
    md = re.sub(r"\n{3,}", "\n\n", md)

    header = (
        f"# {url}\n\n"
        f"*Fetched: {time.strftime('%Y-%m-%d %H:%M:%S')}*\n\n"
        "---\n\n"
    )
    return header + md.strip() + "\n"


# ---------------------------------------------------------------------------
# Main fetch routine
# ---------------------------------------------------------------------------

def fetch_page(url: str) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    assets_dir = OUT_DIR / "assets"
    assets_dir.mkdir(exist_ok=True)

    html_out = OUT_DIR / "intersight-full-page.html"
    md_out   = OUT_DIR / "intersight-full-page.md"

    # ------------------------------------------------------------------
    # 1. Launch browser and navigate
    # ------------------------------------------------------------------
    print(f"[fetch] Target URL : {url}")
    print(f"[fetch] Output dir : {OUT_DIR.resolve()}")
    print()

    driver = _make_chrome_driver()
    try:
        print(f"[selenium] Navigating to {url} …")
        driver.get(url)

        _wait_for_content(driver)
        _scroll_to_bottom(driver)

        # Grab the fully-rendered outer page source
        rendered_html = driver.page_source
        page_title = driver.title
        final_url = driver.current_url

        # ------------------------------------------------------------------
        # Also capture content from any iframes (GWT help widget)
        # ------------------------------------------------------------------
        iframe_htmls: list[str] = []
        iframes = driver.find_elements(By.TAG_NAME, "iframe")
        print(f"[selenium] Found {len(iframes)} iframe(s) on the page")

        for idx, iframe in enumerate(iframes):
            try:
                src = iframe.get_attribute("src") or "(srcdoc)"
                print(f"  [iframe {idx+1}] src={src[:120]}")
                driver.switch_to.frame(iframe)
                # Wait a moment for the iframe DOM to stabilise
                time.sleep(2)
                iframe_doc = driver.page_source
                iframe_htmls.append(iframe_doc)
                print(f"  [iframe {idx+1}] captured {len(iframe_doc):,} bytes")
            except Exception as exc:
                print(f"  [iframe {idx+1}] could not capture: {exc}")
            finally:
                driver.switch_to.default_content()

    finally:
        driver.quit()
        print("[selenium] Browser closed")

    print(f"[fetch] Page title : {page_title!r}")
    print(f"[fetch] Final URL  : {final_url}")

    # ------------------------------------------------------------------
    # 2. Parse with BeautifulSoup and embed iframe content
    # ------------------------------------------------------------------
    soup = BeautifulSoup(rendered_html, "html.parser")

    # If iframes delivered content, embed each one as a <section> inside <body>
    if iframe_htmls:
        body = soup.body or soup
        for idx, iframe_html in enumerate(iframe_htmls, 1):
            iframe_soup = BeautifulSoup(iframe_html, "html.parser")
            # Extract just the body content (or full doc if no body tag)
            iframe_body = iframe_soup.body or iframe_soup
            wrapper = soup.new_tag("section", id=f"iframe-content-{idx}",
                                   **{"data-source": "iframe"})
            wrapper.append(BeautifulSoup(str(iframe_body), "html.parser"))
            body.append(wrapper)
        print(f"[parse] Embedded {len(iframe_htmls)} iframe document(s) into page")

    # Build combined HTML for final output
    combined_html = str(soup)

    # ------------------------------------------------------------------
    # 3. Download CSS / JS assets
    # ------------------------------------------------------------------
    print()
    asset_map = _collect_assets(soup, final_url, assets_dir)
    print(f"[assets] Saved {len(asset_map)} asset(s) to {assets_dir}")

    # ------------------------------------------------------------------
    # 4. Write full raw HTML
    # ------------------------------------------------------------------
    html_out.write_text(combined_html, encoding="utf-8")
    print(f"\n[output] HTML written → {html_out}  ({html_out.stat().st_size:,} bytes)")

    # ------------------------------------------------------------------
    # 5. Convert to Markdown  (prefer iframe content if outer page is thin)
    # ------------------------------------------------------------------
    if iframe_htmls and len(" ".join(iframe_htmls)) > len(rendered_html):
        # Use the combined (iframe-enriched) HTML for the best coverage
        md_source = combined_html
    else:
        md_source = combined_html

    md_content = _html_to_markdown(md_source, final_url)
    md_out.write_text(md_content, encoding="utf-8")
    print(f"[output] MD  written → {md_out}   ({md_out.stat().st_size:,} bytes)")

    # ------------------------------------------------------------------
    # 6. Summary
    # ------------------------------------------------------------------
    print()
    print("=" * 60)
    print("Done!")
    print(f"  HTML  : {html_out.resolve()}")
    print(f"  MD    : {md_out.resolve()}")
    print(f"  Assets: {assets_dir.resolve()}")
    print(f"          ({len(list(assets_dir.iterdir()))} file(s))")
    print("=" * 60)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Download a fully JS-rendered Intersight help page."
    )
    parser.add_argument(
        "url",
        nargs="?",
        default=DEFAULT_URL,
        help=f"URL to fetch (default: {DEFAULT_URL})",
    )
    args = parser.parse_args()
    fetch_page(args.url)


if __name__ == "__main__":
    main()
