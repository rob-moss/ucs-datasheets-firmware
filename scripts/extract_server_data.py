#!/usr/bin/env python3
# Generated with process-server-firmware-adapter-matrix-v4
"""Generate UCS server hardware compatibility matrix from JSON files.

Reads UCS JSON files, extracts server model/cpu/esxi from filename and
adapter/driver details from JSON, and writes markdown output to:
ucs-firmware-reports/server-adapter-driver-matrix-raw.md
"""

from __future__ import annotations

import datetime as dt
import json
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import DefaultDict

PROMPT_VERSION = "process-server-firmware-adapter-matrix-v4"
OUTPUT_FILE = Path("ucs-firmware-reports/server-adapter-driver-matrix-raw.md")
EXCLUDED_FILES = {
    "UCS-Equivalency-Matrix.json",
    "ucsmupgradematrix.json",
    "ucsmcrossver.json",
}
ALLOWED_DRIVERS = {"nenic", "nfnic", "nenic-ens", "nfnic-ens"}


@dataclass(frozen=True)
class RowKey:
    blade_model: str
    cpu_version: str
    server_firmware: str
    esxi_version: str
    adapter_model_firmware: str


def parse_filename(filename: str) -> tuple[str, str, str] | None:
    """Parse model, cpu version and ESXi version from JSON filename."""
    stem = filename.replace(".json", "")
    stem = stem.replace("ucsm-", "")

    model_match = re.search(r"([bc]\d+)(m\d+)", stem, flags=re.IGNORECASE)
    cpu_match = re.search(r"-(v\d+)-", stem, flags=re.IGNORECASE)
    esxi_match = re.search(r"esxi-(\d+)u(\d+)", stem, flags=re.IGNORECASE)

    if not (model_match and cpu_match and esxi_match):
        return None

    model = f"{model_match.group(1).upper()} {model_match.group(2).upper()}"
    cpu = cpu_match.group(1).upper()

    major_raw, update_raw = esxi_match.groups()
    if len(major_raw) == 2:
        major_fmt = f"{major_raw[0]}.{major_raw[1]}"
    else:
        major_fmt = f"{major_raw}.0"
    esxi = f"ESXi {major_fmt} U{int(update_raw)}"

    return model, cpu, esxi


def parse_server_firmware(value: str) -> tuple[int, int, int, str] | None:
    """Return sortable firmware tuple (major, minor, patch, suffix)."""
    if not value:
        return None
    match = re.match(r"^(\d+)\.(\d+)\((\d+)([a-z]?)\)$", value.strip(), re.IGNORECASE)
    if not match:
        return None
    major, minor, patch, suffix = match.groups()
    return int(major), int(minor), int(patch), suffix.lower()


def is_fw_supported(value: str) -> bool:
    parsed = parse_server_firmware(value)
    if not parsed:
        return False
    major, minor, patch, _ = parsed
    return (major, minor, patch) >= (4, 2, 2)


def fw_sort_key(value: str) -> tuple[int, int, int, str]:
    parsed = parse_server_firmware(value)
    if not parsed:
        return (0, 0, 0, "")
    return parsed


def cpu_sort_key(cpu: str) -> int:
    match = re.match(r"^V(\d+)$", cpu.strip(), flags=re.IGNORECASE)
    return int(match.group(1)) if match else 999


def esxi_sort_key(esxi: str) -> tuple[int, int, int]:
    match = re.search(r"ESXi\s+(\d+)\.(\d+)\s+U(\d+)", esxi)
    if not match:
        return (0, 0, 0)
    return int(match.group(1)), int(match.group(2)), int(match.group(3))


def extract_adapter_model(model_text: str) -> str | None:
    if not model_text:
        return None
    if "port expander" in model_text.lower():
        return None
    match = re.search(r"UCS\s+(\d+)\s+Virtual\s+Interface\s+Card", model_text, flags=re.IGNORECASE)
    if match:
        return f"VIC {match.group(1)}"
    return None


def parse_driver(driver_version: str) -> tuple[str, str] | None:
    """Split '<version> <driver>' into (driver, version)."""
    if not driver_version:
        return None

    text = " ".join(driver_version.strip().split())
    if not text:
        return None

    lower = text.lower()
    selected = None
    version = ""
    for candidate in sorted(ALLOWED_DRIVERS, key=len, reverse=True):
        needle = f" {candidate}"
        if lower.endswith(needle):
            selected = candidate
            version = text[: -len(needle)].strip()
            break

    if not selected or not version:
        return None

    return selected, version


def resolve_json_dir() -> Path:
    preferred = Path("jsondata")
    fallback = Path("archive/jsondata")

    if preferred.exists() and preferred.is_dir():
        print(f"Using data source directory: {preferred}")
        return preferred

    if fallback.exists() and fallback.is_dir():
        print(
            "Directory jsondata/ not found in repository root; "
            f"using fallback: {fallback}"
        )
        return fallback

    raise FileNotFoundError("Could not find jsondata/ or archive/jsondata/")


def main() -> int:
    try:
        json_dir = resolve_json_dir()
    except Exception as exc:
        print(f"Error: {exc}")
        return 1

    grouped_drivers: DefaultDict[RowKey, DefaultDict[str, set[str]]] = defaultdict(
        lambda: defaultdict(set)
    )

    files_seen = 0
    files_parsed = 0
    parse_errors = 0
    entries_scanned = 0

    for json_file in sorted(json_dir.glob("*.json")):
        files_seen += 1
        if json_file.name in EXCLUDED_FILES:
            print(f"Skipping excluded file: {json_file.name}")
            continue

        file_meta = parse_filename(json_file.name)
        if not file_meta:
            print(f"Skipping unrecognized filename pattern: {json_file.name}")
            continue

        blade_model, cpu_version, esxi_version = file_meta
        print(
            f"Processing {json_file.name} -> {blade_model} {cpu_version}, {esxi_version}"
        )

        try:
            payload = json.loads(json_file.read_text(encoding="utf-8"))
        except Exception as exc:
            parse_errors += 1
            print(f"  Error parsing {json_file.name}: {exc}")
            continue

        files_parsed += 1

        if isinstance(payload, dict):
            payload = [payload]
        if not isinstance(payload, list):
            print(f"  Skipping {json_file.name}: top-level JSON is not list/dict")
            continue

        for item in payload:
            if not isinstance(item, dict):
                continue
            fw = str(item.get("Version", "")).strip()
            if not is_fw_supported(fw):
                continue

            cna_items = (
                item.get("HardwareTypes", {})
                .get("Adapters", {})
                .get("CNA", [])
            )
            if not isinstance(cna_items, list):
                continue

            for adapter in cna_items:
                if not isinstance(adapter, dict):
                    continue
                entries_scanned += 1

                adapter_model = extract_adapter_model(str(adapter.get("Model", "")))
                if not adapter_model:
                    continue

                adapter_fw = str(adapter.get("FirmwareVersion", "")).strip()
                if not adapter_fw:
                    continue

                driver_info = parse_driver(str(adapter.get("DriverVersion", "")))
                if not driver_info:
                    continue

                driver_name, driver_version = driver_info
                adapter_model_fw = f"{adapter_model} - {adapter_fw}"

                key = RowKey(
                    blade_model=blade_model,
                    cpu_version=cpu_version,
                    server_firmware=fw,
                    esxi_version=esxi_version,
                    adapter_model_firmware=adapter_model_fw,
                )
                grouped_drivers[key][driver_name].add(driver_version)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    keys = sorted(
        grouped_drivers.keys(),
        key=lambda k: (
            k.blade_model,
            fw_sort_key(k.server_firmware),
            cpu_sort_key(k.cpu_version),
            esxi_sort_key(k.esxi_version),
            k.adapter_model_firmware,
        ),
    )

    rows_written = 0
    today = dt.date.today().isoformat()

    with OUTPUT_FILE.open("w", encoding="utf-8") as out:
        out.write("# UCS Server Hardware Compatibility Matrix\n\n")
        out.write(f"- Generated: {today}\n")
        out.write(f"- Generated with: {PROMPT_VERSION}\n")
        out.write(f"- Source directory: {json_dir}\n")
        out.write("\n")
        out.write("## Overview\n\n")
        out.write("- Grouped by blade/rack model\n")
        out.write("- Sorted by server firmware, CPU version, and ESXi version (ascending)\n")
        out.write("- Includes drivers: nenic, nfnic, nenic-ens, nfnic-ens\n\n")

        model_to_keys: DefaultDict[str, list[RowKey]] = defaultdict(list)
        for key in keys:
            model_to_keys[key.blade_model].append(key)

        for idx, model in enumerate(sorted(model_to_keys.keys())):
            if idx > 0:
                out.write("---\n\n")
            out.write(f"## {model}\n\n")
            out.write(
                "| Blade Model + CPU Version | Server Firmware | ESXi Version | "
                "Adapter Model + Firmware | Driver + Version |\n"
            )
            out.write(
                "|---------------------------|-----------------|--------------|"
                "--------------------------|------------------|\n"
            )

            model_keys = model_to_keys[model]
            for k in model_keys:
                driver_cell_parts = []
                for drv in ["nenic", "nfnic", "nenic-ens", "nfnic-ens"]:
                    versions = sorted(grouped_drivers[k].get(drv, set()))
                    if versions:
                        driver_cell_parts.append(f"{drv}: {', '.join(versions)}")
                if not driver_cell_parts:
                    continue

                out.write(
                    f"| {k.blade_model} {k.cpu_version} | {k.server_firmware} | "
                    f"{k.esxi_version} | {k.adapter_model_firmware} | "
                    f"{'<br>'.join(driver_cell_parts)} |\n"
                )
                rows_written += 1

            # Empty row between model server groups, per prompt requirement.
            out.write("| | | | | |\n\n")

    print("\nGeneration complete")
    print(f"  Files seen: {files_seen}")
    print(f"  Files parsed: {files_parsed}")
    print(f"  Parse errors: {parse_errors}")
    print(f"  CNA entries scanned: {entries_scanned}")
    print(f"  Matrix rows written: {rows_written}")
    print(f"  Output: {OUTPUT_FILE}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
