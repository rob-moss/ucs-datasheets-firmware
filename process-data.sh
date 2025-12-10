#!/opt/homebrew/bin/bash

source ./urldata.sh

datadir=./ucs-firmware-docs
jsondir=./jsondata


./json_to_markdown.py $jsondir --out $datadir

pandoc "${datadir}/Cisco UCS Manager Cross-Version Firmware Support, Release 4.3 - Cisco.html" -f html -t markdown -o ${datadir}/cross-version-firmware-4.3.md

./extract_adapter_matrix.py

./validate_firmware_data.py > validation_report.md

