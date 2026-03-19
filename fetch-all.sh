#!/bin/bash

source .venv/bin/activate

# fetch-cisco
python3 fetch-cisco-docs.py
if [ $? -ne 0 ]; then
    echo "Error fetching Cisco docs"
    exit 1
fi

# Fetch recommended
cd recommended-firmware
python3 fetch-imm.py
if [ $? -ne 0 ]; then
    echo "Error fetching recommended firmware"
    exit 1
fi
python3 fetch-ucsm.py
if [ $? -ne 0 ]; then
    echo "Error fetching recommended firmware"
    exit 1
fi

