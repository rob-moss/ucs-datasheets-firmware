#!/opt/homebrew/bin/bash

source ./urldata.sh

echo "* Create dirs"

datadir=./ucs-firmware-docs
jsondir=./jsondata


# getopts
## -b = blademodel (b200)
## -m = gen (m5)
## -c = cpu (v2)
## -f = firmware (4.2(3m))
## -o = o/s (esxi8u3)
## -n = mgmt mode (ucsm)

# Equivalency Matrix JSON
dataequiv="$jsondir/UCS-Equivalency-Matrix.json"
# Upgrade matrix
dataucsmupgradematrix=''

# HCL data
b200m5v1esxi8u3='./data/hcl-b200m5-v1-esxi-8u3.json'


# Pseudo code
# * Ask blade model, blade firmware bundle
# * Read equivalency matrix for firmware bundle version
# ** Input: blade + firmware bundle ie 4.2(3m)
# ** Output: firmware version ie 4.2(3j)
# * Read HCL for firmware bundle version + blade model
# * Output:
# ** Blade Model
# ** Blade firmware
# ** VIC model + nenic version

# Reading the equivalency matrix
# * search for:      .[].header = "Patch" and .[].value= "4.2(3m) and .productname == "Cisco UCS Manager""
# ** returns .rowindex ($rowindex)
# * search for:      .[].rowindex == $rowindex and .header == "Platforms"
# ** returns UCS Servers and their Blade firmware versions  ie 4.2(3j)


# Inputs for HCL
blademodel='b200'
bladegen='m5'
bladecputype='v1'
bladevendor='VMware'
bladeos='esxi-8u3'

bladefwbundle='4.2(3m)'

ucsmimm=ucsm

echo "* UCS Blade firmware bundle:      $bladefwbundle"
echo "* UCS Blade model, Gen and CPU:   $blademodel $bladegen $bladecputype"
echo "* UCS Blade O/S:                  $bladeos"
echo "* UCS Manager or IMM mode:        $ucsmimm"


# Work out which HCL file to use
hclfile=$b200m5v1esxi8u3


echo "* Opening $hclfile for UCS Blade model $blademodel $bladecputype $bladeos"


case $ucsmimm in
    ucsm) _productname="Cisco UCS Manager" ;;
    imm) _productname="Cisco Intersight" ;;
    *) echo "Invalid option: 'Cisco UCS Manager' or 'Cisco Intersight'"; exit 1 ;;
esac
echo "** Product name: $_productname"



# Get the rowindex for a Patch of version
# UCS Manager
## .[] | select(.header == "Patch" and .productname == "Cisco UCS Manager" and .value == "4.2(3m)") | .rowindex
#_rowindex=$(cat $dataequiv | jq -r '.[] | select(.header == "Patch" and .productname == "Cisco UCS Manager" and .value == "4.2(3m)") | .rowindex')
_rowindex=$(cat $dataequiv | jq -r ".[] | select(.header == \"Patch\" and .productname == \"$_productname\" and .value == \"$bladefwbundle\") | .rowindex")
echo "** Rowindex: $_rowindex"


# Check if blank
if [ -z $_rowindex ]; then
    echo "Error fetching Patch version for firmware $bladefwbundle on platform $_productname"
    exit 1
fi



# get the rowindex data for the patch
## .[] | select(.header == "Platforms" and .rowindex == 47) | .value
_bladefwvals=$(cat $dataequiv | jq -r ".[] | select(.header == \"Platforms\" and .rowindex == $_rowindex) | .value")
# echo "** Blade Vals: $_bladefwvals"


# Get the Equivalency Matrix Blade Bundle to Blade Actual Firmware version
echo "** Blade Firmware Versions:"
echo "$_bladefwvals" | sed 's/\n/\r/g' | grep -i "$bladegen" | grep -i "$blademodel"
_bladeequivmatrix=$(echo "$_bladefwvals" | sed 's/\n/\r/g' | grep -i "$bladegen" | grep -i "$blademodel")

# Get the actual Firmware version running on Blades (last column in row)
_bladefwver=$(echo "$_bladefwvals" | sed 's/\n/\r/g' | grep -i "$bladegen" | grep -i "$blademodel" | awk '{print $NF}')


echo "* Blade Firmware Version:     $_bladefwver"
# Get the Major.Minor firmware version
_bladefwmajor=$(echo $_bladefwver | sed 's/[[:alpha:]]//g')
echo "* Major firmware version:     $_bladefwmajor"



echo "* Processing HCL Versions"

## Begin work to pull nenic + fnic driver versions for blade version and 
# $hclfile
# .searchResultsDetails[] | select(.Version == "4.2(3)") | .HardwareTypes.Adapters.CNA.[] | [ .Model, .FirmwareVersion, .DriverVersion ]
# produces nfnic and nenic
# cat $hclfile | jq -r -c '.searchResultsDetails[] | select(.Version == "4.2(3)") | .HardwareTypes.Adapters.CNA.[] | [ .Model, .FirmwareVersion, .DriverVersion ]'
# produces nfnic and nenic

# cat $hclfile | jq -r -c ".searchResultsDetails[] | select(.Version == \"$_bladefwmajor\") | .HardwareTypes.Adapters.CNA.[] | [ .Model, .FirmwareVersion, .DriverVersion ] | @csv" |\
#     grep nenic | sed 's/ Cisco UCS /VIC /g' | sed 's/ Virtual Interface Card//g'

# _hcloutput=$(cat $hclfile | jq -r -c ".searchResultsDetails[] | select(.Version == \"$_bladefwmajor\") | .HardwareTypes.Adapters.CNA.[] | [ .Model, .FirmwareVersion, .DriverVersion ] | @csv" |\
#     grep nenic | sed 's/ Cisco UCS /VIC /g' | sed 's/ Virtual Interface Card//g')







#######################################################
# Print out customer friendly screen
echo "
UCS Blade recommended firmware and nenic drivers from the UCS Hardware Compatability List
UCS Blade Model, Gen and CPU:   $blademodel $bladegen $bladecputype
UCS Blade firmware bundle:      $bladefwbundle
UCS Blade equivalency matrix:   $_bladeequivmatrix
UCS Blade firmware actual:      $_bladefwver
UCS Blade O/S:                  $bladeos
UCS Manager or IMM mode:        $_productname


VIC Adapter Model               VIC FW  nenic version
-----------------               ------  -------------"


cat $hclfile | jq -r -c ".searchResultsDetails[] | select(.Version == \"$_bladefwmajor\") | .HardwareTypes.Adapters.CNA.[]" | \
    jq -r -c ' [ .Model, .FirmwareVersion, .DriverVersion ] | @tsv' |\
    grep nenic | sed 's/ Cisco UCS /VIC /g' | sed 's/ Virtual Interface Card//g' | sed 's/Cisco //g'


#Header:
# VIC Adapter Model               VIC FW  nenic version
# -----------------               ------  -------------
# UCSB-MLOM-40G-03:VIC 1340       4.5(3)  2.0.11.0-1OEM.800.1.0.20143090 nenic
# UCSB-MLOM-40G-04:VIC 1440       5.2(3)  2.0.11.0-1OEM.800.1.0.20143090 nenic
# UCSB-VIC-M83-8P:VIC 1380        4.5(3)  2.0.11.0-1OEM.800.1.0.20143090 nenic
# UCSB-VIC-M84-4P:VIC 1480        5.2(3)  2.0.11.0-1OEM.800.1.0.20143090 nenic

# tester
# cat $hclfile | jq -r -c ".searchResultsDetails[] | select(.Version == \"$_bladefwmajor\") | .HardwareTypes.Adapters.CNA.[]" | \
#     jq -r -c ' [ .Model, .FirmwareVersion, .DriverVersion ] | @tsv ' | column -t -s $'\t'

