#!/usr/bin/env python3
"""
Extract server model, adapter, ESXi, and driver data from JSON HCL files
and export to a concise markdown format.
"""

import json
import os
import re
from collections import defaultdict

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
    """Main function to process all JSON files and generate markdown."""
    
    jsondata_dir = 'jsondata'
    
    if not os.path.exists(jsondata_dir):
        print(f"Error: Directory {jsondata_dir} not found")
        return
    
    # Dictionary to organize data by blade model, CPU version, and ESXi version
    # Key: (blade_model, cpu_version, esxi_version)
    server_data = defaultdict(lambda: {
        'adapters': set(),
        'driver_versions': defaultdict(set)  # driver_name -> set of full version strings
    })
    
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
        
        key = (blade_model, cpu_version, esxi_version)
        
        for adapter_info in adapters:
            # Add adapter with firmware version
            if adapter_info['adapter'] and adapter_info['firmware']:
                adapter_str = f"{adapter_info['adapter']} (FW: {adapter_info['firmware']})"
                server_data[key]['adapters'].add(adapter_str)
            
            # Add driver version string grouped by driver name
            if adapter_info['driver'] and adapter_info['driver_version']:
                server_data[key]['driver_versions'][adapter_info['driver']].add(adapter_info['driver_version'])
    
    # Generate markdown output
    output_file = 'ucs-firmware-reports/server-adapter-driver-matrix.md'
    
    # Create directory if it doesn't exist
    os.makedirs('ucs-firmware-reports', exist_ok=True)

    with open(output_file, 'w') as f:
        f.write("# UCS Server Hardware Compatibility Matrix\n\n")
        f.write("**Generated:** December 9, 2025\n\n")
        f.write("This matrix shows UCS blade server models with their supported adapters, firmware versions, ESXi versions, and drivers.\n\n")
        f.write("---\n\n")
        
        # Group by blade model
        current_model = None
        
        for key in sorted(server_data.keys()):
            blade_model, cpu_version, esxi_version = key
            data = server_data[key]
            
            # Add heading when model changes
            if blade_model != current_model:
                f.write(f"\n## {blade_model}\n\n")
                current_model = blade_model
            
            f.write(f"### {blade_model} - {cpu_version} - {esxi_version}\n\n")
            
            # Create table format
            f.write("| Adapter Model + Firmware | Driver + Version |\n")
            f.write("| ------------------------ | ---------------- |\n")
            
            # Group adapters and drivers together
            if data['adapters'] and data['driver_versions']:
                # Write adapters
                adapters_list = sorted(data['adapters'])
                
                # Write drivers
                driver_entries = []
                for driver_name in sorted(data['driver_versions'].keys()):
                    versions = sorted(data['driver_versions'][driver_name])
                    for ver in versions:
                        driver_entries.append(f"{driver_name}: {ver}")
                
                # Combine into table rows
                max_rows = max(len(adapters_list), len(driver_entries))
                for i in range(max_rows):
                    adapter_cell = adapters_list[i] if i < len(adapters_list) else ""
                    driver_cell = driver_entries[i] if i < len(driver_entries) else ""
                    f.write(f"| {adapter_cell} | {driver_cell} |\n")
            
            f.write("\n---\n\n")
    
    print(f"\nMarkdown file generated: {output_file}")
    print(f"Processed {len(server_data)} server configurations")

if __name__ == '__main__':
    main()
