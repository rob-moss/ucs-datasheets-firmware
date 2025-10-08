# UCS Datasheets, HCL and Firmware

This project is used to collect UCS Datasheets, HCL data and Firmware recommendations for Cisco UCS server products including X-Series.

To be used for CIRCUIT or other AI LLMs to query for specific product information.

* Gathers UCS product datasheets in HTML format
* Gathers UCS Manager Release notes 4.2, 4.3 and 6.0 in HTML format
* Gathers UCS HCL JSON files for most common Blade models: b200, x210c for VMware ESXi 6.7u3, 7u3, 8u3
* Converts all JSON files to MarkDown format for consumption by CIRCUIT

## Setup and running
This has been intially prototyped in the Bash shell. This will work on any Linux host using Bash 5.x but will not work on MacOS built-in Bash shell (3.x). 

To run this on a Mac you will need to install a newer version of Bash, which can be done with the homebrew / brew command;
```brew install bash```

If you run this with the MacOS built-in Bash shell it will throw errors about the creation of associative arrays ```declare -A arrayname```

## Files
| File | Description |
| -- | -- |
| pull-data.sh | Pulls down the Datasheets HTML and HCL JSON data from cisco.com |
| process-data.sh | Converts all JSON files to MarkDown format |
| query-data.sh | Queries the JSON files and provides firmware information for a specific blade type. Still WIP  - no menu yet, you will need to edit vars inside the file to make it run on different blade models. |


## Directories
  
| Dir | Description |
|--|--|
| jsondata/ | JSON data files in JSON format -- HCL data, equivalency matrix, upgrade matrix |
| ucs-firmware-docs/ | All UCS product datasheets, HCL data in Markdown. All of these files can be added to a CIRCUIT Project | 
| wip/ | Work In Progress files, can be ignored |


