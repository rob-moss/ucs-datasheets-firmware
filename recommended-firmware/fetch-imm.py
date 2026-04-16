#!/usr/bin/env python3
"""
Fetch Cisco IMM Recommended Firmware Distributables from Intersight API
=======================================================================
Uses the Intersight REST API with HTTP Signature authentication (EC key).

API endpoint: /api/v1/firmware/Distributables
Filter:       RecommendedBuild eq 'Y'
Select:       SupportedModels, Mfid, Version, RecommendedBuild, PlatformType, Name

Outputs:
    recommended-firmware-imm.json  — raw API response
    recommended-firmware-imm.md    — markdown table (SupportedModels, Version, Name, PlatformType)

Dependencies:
    pip install requests cryptography
"""

import base64
import hashlib
import json
import re
import sys
import urllib.parse
from email.utils import formatdate
from pathlib import Path

import requests
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
BASE_URL    = "https://us-east-1.intersight.com"
API_PATH    = "/api/v1/firmware/Distributables"
API_KEY_ID  = "59c84e4a16267c0001c23428/5f978c447564612d314de49f/69b106f775646131013d7975"
API_KEY_FILE  = Path(__file__).parent / ".apikey"
JSON_OUT_FILE = Path(__file__).parent / "jsonfiles/recommended-firmware-imm.json"
MD_OUT_FILE   = Path(__file__).parent / "../ucs-docs/recommended-firmware-imm.md"

QUERY_PARAMS = {
    "$filter": "RecommendedBuild eq 'Y'",
    "$select": "SupportedModels,Mfid,Version,RecommendedBuild,PlatformType,Name",
}


def _natural_key(value: str):
    """Build a natural-sort key so X210CM6 sorts before X210CM7."""
    normalized = re.sub(r"[^A-Za-z0-9]", "", value.upper())
    if normalized.startswith("UCS"):
        normalized = normalized[3:]
    parts = re.split(r"(\d+)", normalized)
    return [int(part) if part.isdigit() else part for part in parts if part]


def _row_sort_key(item: dict):
    """Sort rows with UCSX models first, then naturally by model name/number."""
    models = item.get("SupportedModels") or []
    models = [m for m in models if isinstance(m, str) and m.strip()]

    if not models:
        return (1, ["ZZZ"])

    normalized_models = [model.strip().upper() for model in models]
    has_ucsx = any(model.startswith("UCSX") for model in normalized_models)

    preferred_model = min(
        models,
        key=lambda model: (0 if model.strip().upper().startswith("UCSX") else 1, _natural_key(model)),
    )
    return (0 if has_ucsx else 1, _natural_key(preferred_model))

# ---------------------------------------------------------------------------
# HTTP Signature auth helpers
# ---------------------------------------------------------------------------

def _load_private_key(key_file: Path):
    """Load an EC (or RSA) PEM private key from disk.

    Intersight-exported keys are sometimes labelled 'BEGIN EC PRIVATE KEY' but
    contain PKCS#8 DER data.  Try re-wrapping as 'BEGIN PRIVATE KEY' first, then
    fall back to the original header.
    """
    key_text = key_file.read_text().strip()

    if "BEGIN EC PRIVATE KEY" in key_text:
        body = "".join(
            line for line in key_text.splitlines() if not line.startswith("-----")
        )
        pkcs8_pem = (
            "-----BEGIN PRIVATE KEY-----\n"
            + body + "\n"
            + "-----END PRIVATE KEY-----\n"
        )
        try:
            return serialization.load_pem_private_key(
                pkcs8_pem.encode(), password=None
            )
        except Exception:
            pass  # fall through to try the original header

    return serialization.load_pem_private_key(key_text.encode(), password=None)


def _build_auth_header(method: str, path_with_query: str, host: str,
                       body: bytes, key_id: str, private_key) -> dict[str, str]:
    """
    Build the headers required for Intersight HTTP Signature auth.

    Intersight mandates that host, date, digest, and (request-target) are
    all included in the signed headers list.

    Returns a dict of headers to merge into the request.
    """
    date = formatdate(usegmt=True)

    # Digest: SHA-256 of the request body (empty bytes for GET)
    body_hash = hashlib.sha256(body).digest()
    digest = "SHA-256=" + base64.b64encode(body_hash).decode("utf-8")

    # Signing string — order must match the 'headers' list in the auth header
    signing_string = (
        f"(request-target): {method.lower()} {path_with_query}\n"
        f"host: {host}\n"
        f"date: {date}\n"
        f"digest: {digest}"
    )

    # Sign with the private key.
    # Intersight only accepts "hs2019" (EC/generic) or "rsa-sha256" as the
    # algorithm label — "ecdsa-with-sha256" is rejected even though that
    # accurately describes the underlying operation for EC keys.
    if isinstance(private_key.public_key(), ec.EllipticCurvePublicKey):
        signature_bytes = private_key.sign(
            signing_string.encode("utf-8"),
            ec.ECDSA(hashes.SHA256()),
        )
        algorithm = "hs2019"
    else:
        from cryptography.hazmat.primitives.asymmetric import padding
        signature_bytes = private_key.sign(
            signing_string.encode("utf-8"),
            padding.PKCS1v15(),
            hashes.SHA256(),
        )
        algorithm = "rsa-sha256"

    signature_b64 = base64.b64encode(signature_bytes).decode("utf-8")

    auth_header = (
        f'Signature keyId="{key_id}",'
        f'algorithm="{algorithm}",'
        f'headers="(request-target) host date digest",'
        f'signature="{signature_b64}"'
    )

    return {
        "Date":          date,
        "Host":          host,
        "Digest":        digest,
        "Authorization": auth_header,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    # Load the EC private key
    if not API_KEY_FILE.exists():
        print(f"ERROR: API key file not found: {API_KEY_FILE}", file=sys.stderr)
        sys.exit(1)

    private_key = _load_private_key(API_KEY_FILE)

    # Build full path + query string.
    # Pass safe='$' so OData parameter names ($filter, $select) are not percent-encoded.
    query_string = urllib.parse.urlencode(
        QUERY_PARAMS, quote_via=urllib.parse.quote, safe="$"
    )
    full_path = f"{API_PATH}?{query_string}"
    url = f"{BASE_URL}{full_path}"

    # Extract hostname from BASE_URL for the Host header
    host = urllib.parse.urlparse(BASE_URL).netloc

    # Build signed headers (host, date, digest, request-target all required)
    signed_headers = _build_auth_header(
        "GET", full_path, host, b"", API_KEY_ID, private_key
    )
    headers = {**signed_headers, "Accept": "application/json"}

    # Make the request
    resp = requests.get(url, headers=headers, timeout=30)

    if not resp.ok:
        print(f"ERROR: HTTP {resp.status_code} {resp.reason}", file=sys.stderr)
        print(resp.text, file=sys.stderr)
        sys.exit(1)

    data = resp.json()

    # Print to screen
    print(json.dumps(data, indent=2))

    # Save raw JSON
    JSON_OUT_FILE.write_text(json.dumps(data, indent=2))
    print(f"\nJSON saved to {JSON_OUT_FILE}", file=sys.stderr)

    # Convert to Markdown table and save
    results = sorted(data.get("Results", []), key=_row_sort_key)
    md_lines = [
        "# IMM Recommended Firmware\n",
        "| SupportedModels | Version | Name | PlatformType |",
        "| --- | --- | --- | --- |",
    ]
    for item in results:
        models = ", ".join(item.get("SupportedModels") or [])
        version = item.get("Version", "")
        name = item.get("Name", "")
        platform = item.get("PlatformType", "")
        md_lines.append(f"| {models} | {version} | {name} | {platform} |")

    md_content = "\n".join(md_lines) + "\n"
    MD_OUT_FILE.write_text(md_content)
    print(f"Markdown saved to {MD_OUT_FILE}", file=sys.stderr)

    # MD_OUT_FILE2.parent.mkdir(parents=True, exist_ok=True)
    # MD_OUT_FILE2.write_text(md_content)
    # print(f"Markdown saved to {MD_OUT_FILE2}", file=sys.stderr)


if __name__ == "__main__":
    main()
