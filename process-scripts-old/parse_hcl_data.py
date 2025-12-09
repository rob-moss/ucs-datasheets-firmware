#!/usr/bin/env python3
"""
Parse HCL data files to extract server model, adapter, ESXi, and driver information
for UCS Manager firmware versions 4.2(2) through 4.3(6)
"""

import json
import re
import os
from collections import defaultdict

# Firmware versions we care about (newest to oldest)
FIRMWARE_VERSIONS = ['4.3(6)', '4.3(5)', '4.3(4)', '4.3(3)', '4.3(2)', '4.2(3)', '4.2(2)']

# Map file patterns to server models
SERVER_MODEL_MAP = {
    'b200m4': 'UCS B200 M4',
    'b200m5': 'UCS B200 M5',
    'b200m6': 'UCS B200 M6',
    'b480m5': 'UCS B480 M5',
    'c220m5': 'UCS C220 M5',
    'c240m5': 'UCS C240 M5',
    'c220m6': 'UCS C220 M6',
    'c240m6': 'UCS C240 M6',
    'x210c': 'UCS X210c',
}

# ESXi version mapping
ESXI_MAP = {
    '67u3': 'ESXi 6.7 U3',
    '73u3': 'ESXi 7.3 U3',
    '7u3': 'ESXi 7.0 U3',
    '8u3': 'ESXi 8.0 U3',
}

def parse_md_file(filepath):
    """Parse markdown file with embedded JSON data"""
    data = []
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Find all JSON objects in the markdown
    # Look for patterns like: { "DbChangeLogs": ... }
    json_pattern = r'\{\s*"DbChangeLogs":\s*"[^"]*UCSM_([\d.()]+)".*?"HardwareTypes":\s*\{.*?\}\s*\}'
    
    # Try to find complete JSON blocks
    blocks = re.findall(r'\{[^{}]*"DbChangeLogs"[^{}]*"HardwareTypes"[^{}]*\{[^{}]*\}[^{}]*\}', content, re.DOTALL)
    
    for block in blocks:
        try:
            # Extract UCSM version from DbChangeLogs URL
            version_match = re.search(r'UCSM_([\d.()]+)', block)
            if not version_match:
                continue
            
            ucsm_version = version_match.group(1)
            
            # Parse the JSON
            json_obj = json.loads(block)
            
            # Extract adapter information
            if 'HardwareTypes' in json_obj and 'Adapters' in json_obj['HardwareTypes']:
                adapters = json_obj['HardwareTypes']['Adapters']
                
                for adapter in adapters:
                    adapter_info = {
                        'ucsm_version': ucsm_version,
                        'model': adapter.get('Model', ''),
                        'firmware': adapter.get('Firmware Version', ''),
                        'driver_name': adapter.get('Driver Name', ''),
                        'driver_version': adapter.get('Driver Version', ''),
                    }
                    data.append(adapter_info)
        except json.JSONDecodeError:
            continue
    
    return data

def extract_server_model(filename):
    """Extract server model from filename"""
    for pattern, model in SERVER_MODEL_MAP.items():
        if pattern in filename.lower():
            return model
    return None

def extract_esxi_version(filename):
    """Extract ESXi version from filename"""
    for pattern, version in ESXI_MAP.items():
        if pattern in filename.lower():
            return version
    return None

def main():
    """Main function to parse all HCL data files"""
    
    # Dictionary to store data by firmware version
    firmware_data = defaultdict(lambda: {
        'servers': set(),
        'adapters': defaultdict(set),  # adapter_model -> set of firmware versions
        'esxi_versions': set(),
        'drivers': defaultdict(set),  # driver_name -> set of driver versions
    })
    
    # Find all markdown files in ucs-firmware-docs directory
    docs_dir = 'ucs-firmware-docs'
    
    if not os.path.exists(docs_dir):
        print(f"Error: Directory {docs_dir} not found")
        return
    
    # Process each markdown file
    for filename in os.listdir(docs_dir):
        if not filename.endswith('.md'):
            continue
        
        filepath = os.path.join(docs_dir, filename)
        
        # Extract server model and ESXi version from filename
        server_model = extract_server_model(filename)
        esxi_version = extract_esxi_version(filename)
        
        if not server_model or not esxi_version:
            continue
        
        print(f"Processing: {filename} -> {server_model}, {esxi_version}")
        
        # Parse the file
        adapters = parse_md_file(filepath)
        
        for adapter in adapters:
            ucsm_ver = adapter['ucsm_version']
            
            # Only include versions we care about
            if ucsm_ver not in FIRMWARE_VERSIONS:
                continue
            
            # Add server model
            firmware_data[ucsm_ver]['servers'].add(server_model)
            
            # Add ESXi version
            firmware_data[ucsm_ver]['esxi_versions'].add(esxi_version)
            
            # Add adapter with firmware version
            if adapter['model'] and adapter['firmware']:
                firmware_data[ucsm_ver]['adapters'][adapter['model']].add(adapter['firmware'])
            
            # Add driver information for nenic/nfnic drivers
            driver_name = adapter['driver_name'].lower()
            if any(d in driver_name for d in ['nenic', 'nfnic']):
                if adapter['driver_version']:
                    firmware_data[ucsm_ver]['drivers'][adapter['driver_name']].add(adapter['driver_version'])
    
    # Generate markdown table and write to file
    output_file = 'server_models_table.md'
    
    with open(output_file, 'w') as f:
        f.write("\n\n## Server Models Support\n\n")
        f.write("| Server Firmware Version | Server Models Supported | Adapter and Firmware Supported | ESXi Versions | Driver nenic/nfnic versions |\n")
        f.write("|------------------------|------------------------|-------------------------------|---------------|------------------------------|\n")
        
        for fw_ver in FIRMWARE_VERSIONS:
            if fw_ver not in firmware_data:
                continue
            
            data = firmware_data[fw_ver]
            
            # Format server models
            servers = ', '.join(sorted(data['servers']))
            
            # Format adapters with firmware
            adapters_list = []
            for adapter_model in sorted(data['adapters'].keys()):
                fw_versions = sorted(data['adapters'][adapter_model])
                adapters_list.append(f"{adapter_model} ({', '.join(fw_versions)})")
            adapters = ', '.join(adapters_list)
            
            # Format ESXi versions
            esxi = ', '.join(sorted(data['esxi_versions']))
            
            # Format drivers
            drivers_list = []
            for driver_name in sorted(data['drivers'].keys()):
                driver_versions = sorted(data['drivers'][driver_name])
                for dv in driver_versions:
                    drivers_list.append(dv)
            drivers = ', '.join(drivers_list)
            
            f.write(f"| **{fw_ver}** | {servers} | {adapters} | {esxi} | {drivers} |\n")
    
    print(f"\nTable written to {output_file}")
    print(f"Processed {len(firmware_data)} firmware versions")

if __name__ == '__main__':
    main()
