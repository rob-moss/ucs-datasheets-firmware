#!/usr/bin/env python3
"""
Validation Script for UCS Firmware Data
Compares JSON firmware data against the markdown report to identify discrepancies
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import defaultdict


class FirmwareValidator:
    def __init__(self, markdown_file: str, json_files: List[str]):
        self.markdown_file = Path(markdown_file)
        self.json_files = [Path(f) for f in json_files]
        self.markdown_data = []
        self.json_data = {}
        self.discrepancies = []
        
    def parse_markdown(self):
        """Parse the markdown file to extract firmware data"""
        print(f"Parsing markdown file: {self.markdown_file}")
        
        with open(self.markdown_file, 'r') as f:
            content = f.read()
        
        # Find the table data - lines starting with |
        lines = content.split('\n')
        in_table = False
        
        for line in lines:
            if line.startswith('| Blade Model'):
                in_table = True
                continue
            if line.startswith('|---'):
                continue
            if line.startswith('|') and in_table and line.strip() != '| | | | | |':
                # Parse the table row
                parts = [p.strip() for p in line.split('|')[1:-1]]
                if len(parts) == 5 and parts[0]:  # Valid data row
                    blade_model = parts[0]
                    server_fw = parts[1]
                    esxi_version = parts[2]
                    adapter_info = parts[3]
                    drivers_info = parts[4]
                    
                    # Filter by server firmware version (only 4.2(2) and above)
                    if not self._is_firmware_version_valid(server_fw):
                        continue
                    
                    # Extract adapter model and firmware
                    adapter_match = re.match(r'(.+?)\s+-\s+(.+)', adapter_info)
                    if adapter_match:
                        adapter_model = adapter_match.group(1).strip()
                        adapter_fw = adapter_match.group(2).strip()
                    else:
                        adapter_model = adapter_info
                        adapter_fw = ""
                    
                    # Parse drivers - they're separated by <br>
                    drivers = [d.strip() for d in drivers_info.split('<br>')]
                    
                    # Extract driver types and versions for nenic, nfnic, nenic-ens
                    # Exclude nfnic entries containing 'nvme'
                    for driver in drivers:
                        # Skip if this is an nfnic (nvme) entry
                        if 'nfnic' in driver.lower() and 'nvme' in driver.lower():
                            continue
                        
                        driver_match = re.match(r'(\w+)\s+([\d\.\-\w]+)', driver)
                        if driver_match:
                            driver_type = driver_match.group(1)
                            driver_version = driver_match.group(2)
                            
                            if driver_type in ['nenic', 'nfnic', 'nenic-ens']:
                                self.markdown_data.append({
                                    'blade_model': blade_model,
                                    'cpu_version': self._extract_cpu_version(blade_model),
                                    'server_fw': server_fw,
                                    'esxi_version': esxi_version,
                                    'adapter_model': adapter_model,
                                    'adapter_fw': adapter_fw,
                                    'driver_type': driver_type,
                                    'driver_version': driver_version
                                })
        
        print(f"  Found {len(self.markdown_data)} entries in markdown")
    
    def _extract_cpu_version(self, blade_model: str) -> str:
        """Extract CPU version from blade model string (e.g., 'B200 M4 V3' -> 'V3')"""
        match = re.search(r'(V\d+)', blade_model)
        return match.group(1) if match else ""
    
    def _extract_blade_server_type(self, blade_model: str) -> str:
        """Extract blade server type (e.g., 'B200 M4 V3' -> 'B200 M4')"""
        match = re.match(r'(B\d+\s+M\d+)', blade_model)
        return match.group(1) if match else blade_model
    
    def _parse_firmware_version(self, version_str: str) -> Tuple[int, int]:
        """Parse firmware version string to tuple for comparison (e.g., '4.2(2)' -> (4.2, 2))"""
        match = re.match(r'(\d+\.\d+)\((\d+)\)', version_str)
        if match:
            major = float(match.group(1))
            minor = int(match.group(2))
            return (major, minor)
        return (0, 0)
    
    def _is_firmware_version_valid(self, version_str: str) -> bool:
        """Check if firmware version is 4.2(2) or above"""
        parsed = self._parse_firmware_version(version_str)
        min_version = (4.2, 2)
        return parsed >= min_version
    
    def parse_json_files(self):
        """Parse JSON files to extract firmware data"""
        for json_file in self.json_files:
            print(f"Parsing JSON file: {json_file}")
            
            with open(json_file, 'r') as f:
                data_array = json.load(f)
            
            # Extract blade model and ESXi version from filename
            # e.g., ucsm-b200m4-v3-esxi-67u3.json
            filename = json_file.stem
            parts = filename.split('-')
            
            # Parse filename components
            blade_type = parts[1]  # e.g., b200m4
            cpu_version = parts[2].upper()  # e.g., v3
            esxi_parts = parts[3:]  # e.g., ['esxi', '67u3']
            esxi_raw = esxi_parts[-1] if esxi_parts else ''  # e.g., '67u3'
            
            # Format ESXi version to match markdown format
            # Convert '67u3' -> 'ESXi 6.7 U3' or '8u3' -> 'ESXi 8.0 U3'
            if esxi_raw:
                if esxi_raw.startswith('8'):
                    esxi_version = f"ESXi 8.0 U{esxi_raw[2].upper()}"
                elif esxi_raw.startswith('7'):
                    esxi_version = f"ESXi 7.0 U{esxi_raw[2].upper()}"
                elif esxi_raw.startswith('67'):
                    esxi_version = f"ESXi 6.7 U{esxi_raw[3].upper()}"
                else:
                    esxi_version = f"ESXi {esxi_raw.upper()}"
            else:
                esxi_version = "ESXi UNKNOWN"
            
            # Format blade model
            blade_match = re.match(r'(b\d+)(m\d+)', blade_type, re.I)
            if blade_match:
                blade_model = f"{blade_match.group(1).upper()} {blade_match.group(2).upper()} {cpu_version}"
            else:
                blade_model = f"{blade_type.upper()} {cpu_version}"
            
            # Store in dict with key
            key = f"{blade_model}_{esxi_version}"
            
            entries = []
            
            # JSON file contains array of version objects
            # Process each version in the array
            for data in data_array:
                # Filter by server firmware version (only 4.2(2) and above)
                server_fw_version = data.get('Version', '')
                if not self._is_firmware_version_valid(server_fw_version):
                    continue
                
                # Navigate to CNA adapters
                if 'HardwareTypes' in data and 'Adapters' in data['HardwareTypes']:
                    adapters = data['HardwareTypes']['Adapters']
                    if 'CNA' in adapters:
                        for adapter in adapters['CNA']:
                            model = adapter.get('Model', '')
                            
                            # Skip Port Expander adapters
                            if 'Port Expander' in model or 'MLOM-PT' in model:
                                continue
                            
                            # Extract VIC model number (e.g., "VIC 1240", "VIC 1340") for comparison
                            vic_match = re.search(r'(VIC\s+\d+)', model, re.I)
                            if vic_match:
                                adapter_model = vic_match.group(1).upper()
                            else:
                                adapter_model = model
                            
                            adapter_fw = adapter.get('FirmwareVersion', '')
                            driver_version = adapter.get('DriverVersion', '')
                            
                            # Skip nfnic entries containing 'nvme'
                            if 'nfnic' in driver_version.lower() and 'nvme' in driver_version.lower():
                                continue
                            
                            # Extract driver type and version
                            # Format: "1.0.42.0-1OEM.670.0.0.8169922 nenic"
                            driver_match = re.search(r'([\d\.\-\w]+)\s+(\S+)', driver_version)
                            if driver_match:
                                driver_ver = driver_match.group(1)
                                driver_type = driver_match.group(2)
                                
                                if driver_type in ['nenic', 'nfnic', 'nenic-ens']:
                                    entries.append({
                                        'blade_model': blade_model,
                                        'cpu_version': cpu_version,
                                        'server_fw': data.get('Version', ''),
                                        'esxi_version': esxi_version,
                                        'adapter_model': adapter_model,
                                        'adapter_full_name': model,  # Store full name for reporting
                                        'adapter_fw': adapter_fw,
                                        'driver_type': driver_type,
                                        'driver_version': driver_ver
                                    })
            
            self.json_data[key] = entries
            print(f"  Found {len(entries)} relevant entries in JSON")
    
    def compare_data(self):
        """Compare markdown and JSON data to find discrepancies"""
        print("\nComparing data...")
        
        # Group markdown data by key attributes
        md_grouped = defaultdict(list)
        for entry in self.markdown_data:
            key = (
                entry['blade_model'],
                entry['esxi_version'],
                entry['adapter_model'],
                entry['adapter_fw'],
                entry['driver_type']
            )
            md_grouped[key].append(entry)
        
        # Group JSON data by same key attributes
        json_grouped = defaultdict(list)
        for json_entries in self.json_data.values():
            for entry in json_entries:
                key = (
                    entry['blade_model'],
                    entry['esxi_version'],
                    entry['adapter_model'],
                    entry['adapter_fw'],
                    entry['driver_type']
                )
                json_grouped[key].append(entry)
        
        # Find entries in markdown but not in JSON
        md_keys = set(md_grouped.keys())
        json_keys = set(json_grouped.keys())
        
        # Entries only in markdown
        only_in_md = md_keys - json_keys
        for key in only_in_md:
            entries = md_grouped[key]
            for entry in entries:
                self.discrepancies.append({
                    'type': 'MISSING_IN_JSON',
                    'blade_model': entry['blade_model'],
                    'cpu_version': entry['cpu_version'],
                    'server_fw': entry['server_fw'],
                    'esxi_version': entry['esxi_version'],
                    'adapter_model': entry['adapter_model'],
                    'adapter_fw': entry['adapter_fw'],
                    'driver_type': entry['driver_type'],
                    'markdown_driver_version': entry['driver_version'],
                    'json_driver_version': None
                })
        
        # Entries only in JSON
        only_in_json = json_keys - md_keys
        for key in only_in_json:
            entries = json_grouped[key]
            for entry in entries:
                self.discrepancies.append({
                    'type': 'MISSING_IN_MARKDOWN',
                    'blade_model': entry['blade_model'],
                    'cpu_version': entry['cpu_version'],
                    'server_fw': entry['server_fw'],
                    'esxi_version': entry['esxi_version'],
                    'adapter_model': entry['adapter_model'],
                    'adapter_full_name': entry.get('adapter_full_name', entry['adapter_model']),
                    'adapter_fw': entry['adapter_fw'],
                    'driver_type': entry['driver_type'],
                    'markdown_driver_version': None,
                    'json_driver_version': entry['driver_version']
                })
        
        # Compare driver versions for matching keys
        common_keys = md_keys & json_keys
        for key in common_keys:
            md_entries = md_grouped[key]
            json_entries = json_grouped[key]
            
            # Compare driver versions
            md_versions = {e['driver_version'] for e in md_entries}
            json_versions = {e['driver_version'] for e in json_entries}
            
            if md_versions != json_versions:
                self.discrepancies.append({
                    'type': 'VERSION_MISMATCH',
                    'blade_model': md_entries[0]['blade_model'],
                    'cpu_version': md_entries[0]['cpu_version'],
                    'esxi_version': md_entries[0]['esxi_version'],
                    'adapter_model': md_entries[0]['adapter_model'],
                    'adapter_fw': md_entries[0]['adapter_fw'],
                    'driver_type': md_entries[0]['driver_type'],
                    'markdown_driver_version': ', '.join(sorted(md_versions)),
                    'json_driver_version': ', '.join(sorted(json_versions))
                })
    
    def generate_report(self):
        """Generate a report of discrepancies"""
        separator = "=" * 92
        subsep = "─" * 92
        
        print(f"\n{separator}")
        print("VALIDATION REPORT")
        print(separator)
        
        if not self.discrepancies:
            print("\n✓ No discrepancies found! All data matches between JSON and markdown.")
            return
        
        print(f"\nFound {len(self.discrepancies)} discrepancies:\n")
        
        # Group by type
        by_type = defaultdict(list)
        for disc in self.discrepancies:
            by_type[disc['type']].append(disc)
        
        # Report missing in JSON - Markdown Table Format
        if 'MISSING_IN_JSON' in by_type:
            print(f"\n{subsep}")
            print(f"ENTRIES IN MARKDOWN BUT NOT IN JSON ({len(by_type['MISSING_IN_JSON'])} items)")
            print(subsep)
            print()
            print("| Blade Model + CPU Version | Server Firmware | ESXi Version | Adapter Model + Firmware | Driver + Version |")
            print("| ------------ | ------------ | ------------ | ------------ | ------------ |")
            for disc in by_type['MISSING_IN_JSON']:
                blade_cpu = disc['blade_model']
                server_fw = disc.get('server_fw', 'N/A')
                esxi = disc['esxi_version']
                adapter = f"{disc['adapter_model']} - {disc['adapter_fw']}"
                driver = f"{disc['driver_type']} {disc['markdown_driver_version']}"
                print(f"| {blade_cpu} | {server_fw} | {esxi} | {adapter} | {driver} |")
        
        # Report missing in markdown - Markdown Table Format
        if 'MISSING_IN_MARKDOWN' in by_type:
            print(f"\n{subsep}")
            print(f"ENTRIES IN JSON BUT NOT IN MARKDOWN ({len(by_type['MISSING_IN_MARKDOWN'])} items)")
            print(subsep)
            print()
            print("| Blade Model + CPU Version | Server Firmware | ESXi Version | Adapter Model + Firmware | Driver + Version |")
            print("| ------------ | ------------ | ------------ | ------------ | ------------ |")
            for disc in by_type['MISSING_IN_MARKDOWN']:
                blade_cpu = disc['blade_model']
                server_fw = disc.get('server_fw', 'N/A')
                esxi = disc['esxi_version']
                adapter_display = disc.get('adapter_full_name', disc['adapter_model'])
                adapter = f"{adapter_display} - {disc['adapter_fw']}"
                driver = f"{disc['driver_type']} {disc['json_driver_version']}"
                print(f"| {blade_cpu} | {server_fw} | {esxi} | {adapter} | {driver} |")
        
        # Report version mismatches
        if 'VERSION_MISMATCH' in by_type:
            print(f"\n{subsep}")
            print(f"DRIVER VERSION MISMATCHES ({len(by_type['VERSION_MISMATCH'])} items)")
            print(subsep)
            for disc in by_type['VERSION_MISMATCH']:
                print(f"\nBlade: {disc['blade_model']} | CPU: {disc['cpu_version']} | ESXi: {disc['esxi_version']}")
                print(f"  Adapter: {disc['adapter_model']} (FW: {disc['adapter_fw']})")
                print(f"  Driver: {disc['driver_type']}")
                print(f"    Markdown: {disc['markdown_driver_version']}")
                print(f"    JSON:     {disc['json_driver_version']}")
        
        print(f"\n{separator}")
        print(f"SUMMARY: {len(self.discrepancies)} total discrepancies")
        print(f"  - Missing in JSON: {len(by_type.get('MISSING_IN_JSON', []))}")
        print(f"  - Missing in Markdown: {len(by_type.get('MISSING_IN_MARKDOWN', []))}")
        print(f"  - Version Mismatches: {len(by_type.get('VERSION_MISMATCH', []))}")
        print(separator)
    
    def run(self):
        """Run the complete validation process"""
        separator = "=" * 92
        print(f"\n{separator}")
        print("UCS FIRMWARE DATA VALIDATION")
        print(separator)
        
        self.parse_markdown()
        self.parse_json_files()
        self.compare_data()
        self.generate_report()


def main():
    # Define file paths
    markdown_file = "ucs-firmware-reports/server-adapter-driver-matrix-raw.md"
    
    # Auto-discover all relevant JSON files in jsondata/
    jsondata_dir = Path("jsondata")
    exclude_files = {
        "UCS-Equivalency-Matrix.json",
        "ucsmupgradematrix.json",
        "ucsmcrossver.json"
    }
    
    # Find all ucsm-*.json files, excluding the specified files
    json_files = []
    if jsondata_dir.exists():
        for json_file in sorted(jsondata_dir.glob("ucsm-*.json")):
            if json_file.name not in exclude_files:
                json_files.append(str(json_file))
    
    if not json_files:
        print("ERROR: No JSON files found in jsondata/ directory")
        return
    
    print(f"Found {len(json_files)} JSON files to validate")
    
    validator = FirmwareValidator(markdown_file, json_files)
    validator.run()


if __name__ == "__main__":
    main()
