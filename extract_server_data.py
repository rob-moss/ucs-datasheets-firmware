#!/usr/bin/env python3
"""
UCS Server Hardware Compatibility Matrix Generator (v4)

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
    Excludes Port Expander adapters per v2 requirements.
    """
    # Skip Port Expander adapters
    if 'Port Expander' in full_model_name:
        return None
    
    # Look for VIC model numbers (1340, 1380, 1440, 1480, 15411, etc.)
    vic_match = re.search(r'UCS\s+(\d+)\s+Virtual\s+Interface\s+Card', full_model_name)
    if vic_match:
        return f"VIC {vic_match.group(1)}"
    
    return None

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

def esxi_sort_key(esxi_version):
    """
    Create a sort key for ESXi versions to sort in descending order.
    Example: "ESXi 8.0 U3" -> (8, 0, 3)
    """
    match = re.search(r'ESXi\s+(\d+)\.(\d+)\s+U(\d+)', esxi_version)
    if match:
        return (int(match.group(1)), int(match.group(2)), int(match.group(3)))
    return (0, 0, 0)

def parse_json_file(filepath):
    """Parse a single JSON HCL file and extract adapter/driver data and server firmware."""
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        results = []
        server_firmware = None
        
        # JSON is an array of hardware versions
        if not isinstance(data, list):
            data = [data]
        
        for entry in data:
            # Extract server firmware version from Version field
            # Find the latest version that is 4.2(2) or above
            if 'Version' in entry:
                version = entry['Version']
                # Only include versions 4.2(2) and above
                if version:
                    try:
                        # Parse version like "4.2(2)" into major.minor(patch)
                        if '(' in version:
                            base_version = version.split('(')[0]
                            patch_version = version.split('(')[1].rstrip(')')
                            version_parts = base_version.split('.')
                            
                            if len(version_parts) >= 2:
                                major, minor = int(version_parts[0]), int(version_parts[1])
                                patch = int(patch_version) if patch_version else 0
                                
                                # Check if >= 4.2(2)
                                if major > 4 or (major == 4 and minor > 2) or (major == 4 and minor == 2 and patch >= 2):
                                    # Keep the latest qualifying version
                                    if not server_firmware:
                                        server_firmware = version
                                    else:
                                        # Compare versions - keep the higher one
                                        if '(' in server_firmware:
                                            curr_base = server_firmware.split('(')[0]
                                            curr_patch = server_firmware.split('(')[1].rstrip(')')
                                            curr_parts = curr_base.split('.')
                                            if len(curr_parts) >= 2:
                                                curr_major, curr_minor = int(curr_parts[0]), int(curr_parts[1])
                                                curr_p = int(curr_patch) if curr_patch else 0
                                                if major > curr_major or (major == curr_major and minor > curr_minor) or (major == curr_major and minor == curr_minor and patch > curr_p):
                                                    server_firmware = version
                    except:
                        pass
            
            # Only process adapters from entries with server_firmware >= 4.2
            if not server_firmware:
                continue
                
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
                                'driver_version': driver_version,
                                'server_firmware': server_firmware
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
        
        # Get server firmware (should be same for all adapters in file)
        server_firmware = adapters[0]['server_firmware'] if adapters and adapters[0].get('server_firmware') else 'Unknown'
        
        # Group by adapter+firmware to collect all drivers
        adapter_drivers = defaultdict(set)
        
        for adapter_info in adapters:
            # Skip if adapter is None (e.g., Port Expanders excluded)
            if not adapter_info['adapter']:
                continue
            if adapter_info['firmware'] and adapter_info['driver']:
                # Use dash separator instead of + FW
                adapter_key = f"{adapter_info['adapter']} - {adapter_info['firmware']}"
                # Extract just the version number (remove extra text after driver name)
                driver_parts = adapter_info['driver_version'].strip().split()
                if driver_parts:
                    # Version is everything except the last word (which is the driver name)
                    if len(driver_parts) > 1:
                        version = ' '.join(driver_parts[:-1])
                    else:
                        version = driver_parts[0]
                    driver_str = f"{adapter_info['driver']} {version}"
                else:
                    driver_str = adapter_info['driver']
                adapter_drivers[adapter_key].add(driver_str)
        
        # Create table rows
        for adapter_fw, drivers in sorted(adapter_drivers.items()):
            driver_list = "<br>".join(sorted(drivers))
            table_rows.append({
                'blade': blade_model,
                'cpu': cpu_version,
                'esxi': esxi_version,
                'adapter': adapter_fw,
                'drivers': driver_list,
                'server_firmware': server_firmware
            })
    
    # Sort rows by blade model, server firmware (ascending), CPU version (ascending), ESXi version (ascending - oldest first)
    def firmware_sort_key(fw):
        """Parse firmware version for sorting (e.g., 4.2(2) -> (4, 2, 2))"""
        try:
            if '(' in fw:
                base = fw.split('(')[0]
                patch = fw.split('(')[1].rstrip(')')
                parts = base.split('.')
                if len(parts) >= 2:
                    return (int(parts[0]), int(parts[1]), int(patch) if patch else 0)
        except:
            pass
        return (0, 0, 0)
    
    table_rows.sort(key=lambda x: (x['blade'], firmware_sort_key(x['server_firmware']), x['cpu'], esxi_sort_key(x['esxi'])))
    
    # Generate markdown output
    output_file = 'ucs-firmware-reports/server-adapter-driver-matrix-raw.md'
    
    # Create directory if it doesn't exist
    os.makedirs('ucs-firmware-reports', exist_ok=True)

    with open(output_file, 'w') as f:
        f.write("# UCS Server Hardware Compatibility Matrix\n\n")
        f.write("**Generated:** December 10, 2025\n\n")
        f.write("**Generated with:** process-server-firmware-adapter-matrix-v4\n\n")
        f.write("This matrix shows UCS blade server models with their supported adapters, firmware versions, ESXi versions, and drivers.\n\n")
        
        # Write single table with all data, inserting empty rows between blade models
        f.write("| Blade Model + CPU Version | Server Firmware | ESXi Version | Adapter Model + Firmware | Driver + Version |\n")
        f.write("|---------------------------|-----------------|--------------|--------------------------|------------------|\n")
        
        # Track current blade model to insert empty rows between different models
        current_blade = None
        for row in table_rows:
            blade_cpu = f"{row['blade']} {row['cpu']}"
            
            # Insert empty row when blade model changes
            if current_blade is not None and row['blade'] != current_blade:
                f.write("| | | | | |\n")
            
            f.write(f"| {blade_cpu} | {row['server_firmware']} | {row['esxi']} | {row['adapter']} | {row['drivers']} |\n")
            current_blade = row['blade']
        
        f.write("\n---\n\n")
        f.write("*Report generated from UCS HCL JSON files*\n")
    
    print(f"\nMarkdown file generated: {output_file}")
    print(f"Total table rows: {len(table_rows)}")

if __name__ == '__main__':
    main()
