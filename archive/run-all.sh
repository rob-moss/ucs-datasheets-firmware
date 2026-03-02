#!/bin/bash
# v1.0

echo "* Pull data"
./pull-data.sh

echo "* Process data"
./process-data.sh

onedrivedir=~/OneDrive/"OneDrive - Cisco/CIRCUIT Project - UCS Datasheets"
echo "* Copy data to Onedrive: ${onedrivedir}"
if [ -d "${onedrivedir}" ]; then
	rm "$onedrivedir"/*
	cp -R ucs-firmware-docs/* "$onedrivedir"
else
	echo "** directory ${onedrivedir} not found!! Exiting"
	exit 1
fi


echo "* Add new files to Git"
git add *
git add */*
date=`date "+%Y-%m-%d %b %d %Y"`
git commit -m "Pulled data from $date"
git push all
