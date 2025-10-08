#!/opt/homebrew/bin/bash

source ./urldata.sh

datadir=./ucs-firmware-docs
jsondir=./jsondata


./json_to_markdown.py $jsondir --out $datadir
