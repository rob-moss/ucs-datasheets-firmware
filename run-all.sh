#!/bin/bash

echo "* Pull data"
./pull-data.sh

echo "* Process data"
./process-data.sh

echo "* Copy data to Onedrive: OneDrive/OneDrive - Cisco/CIRCUIT UCS Datasheets"
onedrivedir=~/OneDrive/"OneDrive - Cisco/CIRCUIT UCS Datasheets"
rm "$onedrivedir"/*
cp -R ucs-firmware-docs/* "$onedrivedir"

echo "* Add new files to Git"
git add *
git add */*
date=`date "+%Y-%m-%d %b %d %Y"`
git commit -m "Pulled data from $date"
git push all
