#!/usr/bin/env python3
"""
UCS Server Hardware Compatibility Matrix Generator (v2)

This script extracts UCS blade server hardware compatibility data from JSON files
and generates a comprehensive markdown report in table format showing:
- Blade Model
- CPU Version  
- ESXi Version
- Adapter Model + Firmware
- Driver + Version
"""

import json
import os
import re
from collections import defaultdict, OrderedDict

def parse_filename(filename):
    """
    Extract blade model, generation (CPU version), and ESXi version from filename.
    Examples:
        b200m4-v3-esxi-67u3.json -> (B200 M4, v3, ESXi 6.7 U3)
        b200m5-v2-esxi-8u3.json -> (B200 M5, v2, ESXi 8.0 U3)
    """
    # Remove .json and ucsm- prefix
    name = filename.replace('.json', '').replace('ucsm-', '')
    
    # Extract model (b200m4, b200m5, b480m5, etc.)
    model_match = re.match(r'([bc]\d+)([ms]\d+)', name)
    if not model_match:
        return None, None, None
    
    model_prefix = model_match.group(1).upper()  # B200, C220, etc.
    model_suffix = model_match.group(2).upper()  # M4, M5, S1, etc.
    blade_model = f"{model_prefix} {model_suffix}"
    
    # Extract CPU version (v1, v2, v3, v4)
    cpu_match = re.search(r'-(v\d+)-', name)
    cpu_version = cpu_match.group(1).upper() if cpu_match else "Unknown"
    
    # Extract ESXi version (67u3 -> ESXi 6.7 U3, 8u3 -> ESXi 8.0 U3)
    esxi_match = re.search(r'esxi-(\d+)u(\d+)', name)
    if esxi_match:
        major = esxi_match.group(1)
        update = esxi_match.group(2)
        
        # Format the major version (67 -> 6.7, 7 -> 7.0, 8 -> 8.0)
        if len(major) == 2:
            formatted_major = f"{major[0]}.{major[1]}"
        else:
            formatted_major = f"{major}.0"
        
        esxi_version = f"ESXi {formatted_major} U{update}"
    else:
        esxi_version = "Unknown"
    
    return blade_model, cpu_version, esxi_version

def extract_adapter_model(full_model_name):
    """
    Extract just the adapter model number from full name.
    Example: "Cisco UCSB-MLOM-40G-04: Cisco UCS 1440 Virtual Interface Card" -> "VIC 1440"
    """
    # Look for VIC model numbers (1340, 1380, 1440, 1480, 15411, etc.)
    vic_match = re.search(r'UCS\s+(\d+)\s+Virtual\s+Interface\s+Card', full_model_name)
    if vic_match:
        return f"VIC {vic_match.group(1)}"
    
    # Look for other adapter patterns
    if 'Port Expander' in full_model_name:
        return "Port Expander"
    
    return full_model_name

def extract_driver_name(driver_version_string):
    """
    Extract just the driver name from the full driver version string.
    Example: "2.0.11.0-1OEM.800.1.0.20143090 nenic" -> "nenic"
    """
    if not driver_version_string:
        return None
    
    # Driver name is typically at the end
    parts = driver_version_string.strip().split()
    if parts:
        driver_name = parts[-1].lower()
        # Only return nenic, nfnic, nenic-ens, nfnic-ens
        if any(d in driver_name for d in ['nenic', 'nfnic']):
            return driver_name
    
    return None

def parse_json_file(filepath):
    """Parse a single JSON HCL file and extract adapter/driver data."""
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        results = []
        
        # JSON is an array of hardware versions
        if not isinstance(data, list):
            data = [data]
        
        for entry in data:
            # Extract adapters (CNA)
            if 'HardwareTypes' in entry and 'Adapters' in entry['HardwareTypes']:
                if 'CNA' in entry['HardwareTypes']['Adapters']:
                    for adapter in entry['HardwareTypes']['Adapters']['CNA']:
                        adapter_model = extract_adapter_model(adapter.get('Model', ''))
                        firmware_version = adapter.get('FirmwareVersion', '')
                        driver_version = adapter.get('DriverVersion', '')
                        driver_name = extract_driver_name(driver_version)
                        
                        if adapter_model and driver_name:
                            results.append({
                                'adapter': adapter_model,
                                'firmware': firmware_version,
                                'driver': driver_name,
                                'driver_version': driver_version
                            })
        
        return results
    
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
        return []

def main():
    """Main function to process all JSON files and generate markdown table."""
    
    jsondata_dir = 'jsondata'
    
    if not os.path.exists(jsondata_dir):
        print(f"Error: Directory {jsondata_dir} not found")
        return
    
    # List to store all rows for the table
    # Each row: (blade_model, cpu_version, esxi_version, adapter_fw, driver_ver)
    table_rows = []
    
    # Process each JSON file
    for filename in sorted(os.listdir(jsondata_dir)):
        if not filename.endswith('.json') or filename in ['UCS-Equivalency-Matrix.json', 
                                                           'ucsmupgradematrix.json',
                                                           'ucsmcrossver.json']:
            continue
        
        filepath = os.path.join(jsondata_dir, filename)
        
        # Parse filename to extract metadata
        blade_model, cpu_version, esxi_version = parse_filename(filename)
        
        if not blade_model:
            continue
        
        print(f"Processing: {filename} -> {blade_model}, {cpu_version}, {esxi_version}")
        
        # Parse JSON file
        adapters = parse_json_file(filepath)
        
        # Group by adapter+firmware to collect all drivers
        adapter_drivers = defaultdict(set)
        
        for adapter_info in adapters:
            if adapter_info['adapter'] and adapter_info['firmware'] and adapter_info['driver']:
                adapter_key = f"{adapter_info['adapter']} + FW {adapter_info['firmware']}"
                driver_str = f"{adapter_info['driver']} ({adapter_info['driver_version']})"
                adapter_drivers[adapter_key].add(driver_str)
        
        # Create table rows
        for adapter_fw, drivers in sorted(adapter_drivers.items()):
            driver_list = "<br>".join(sorted(drivers))
            table_rows.append({
                'blade': blade_model,
                'cpu': cpu_version,
                'esxi': esxi_version,
                'adapter': adapter_fw,
                'drivers': driver_list
            })
    
    # Generate markdown output
    output_file = 'ucs-firmware-reports/server-adapter-driver-matrix.md'
    
    # Create directory if it doesn't exist
    os.makedirs('ucs-firmware-reports', exist_ok=True)

    with open(output_file, 'w') as f:
        f.write("# UCS Server Hardware Compatibility Matrix\n\n")
        f.write("**Generated:** December 10, 2025\n\n")
        f.write("This matrix shows UCS blade server models with their supported adapters, firmware versions, ESXi versions, and drivers.\n\n")
        
        # Write table header
        f.write("| Blade Model | CPU Version | ESXi Version | Adapter Model + Firmware | Driver + Version |\n")
        f.write("|-------------|-------------|--------------|--------------------------|------------------|\n")
        
        # Write table rows
        for row in table_rows:
            f.write(f"| {row['blade']} | {row['cpu']} | {row['esxi']} | {row['adapter']} | {row['drivers']} |\n")
        
        f.write("\n---\n\n")
        f.write("*Report generated from UCS HCL JSON files*\n")
    
    print(f"\nMarkdown file generated: {output_file}")
    print(f"Total table rows: {len(table_rows)}")

if __name__ == '__main__':
    main()
