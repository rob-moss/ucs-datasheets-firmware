#!/opt/homebrew/bin/bash

echo "* Setting up to pull data"

source ./urldata.sh


# Pull data
## If it doesn't exist, pull it down
## If it's older than a week, pull it down
## If it's less than a week old, leave it and notify "File is fresh, not pulling down"

###
# Fetching JSON payload:
# curl --header 'Content-Type: application/json' \
#   'https://pwc014-nextgen-prod-rcdn.cisco.com/public/v2/searchBy/server/searchResults?serverType_ID=0&serverModel_ID=209,248&processor_ID=153&osVendor_ID=5&osVersion_ID=1025&firmwareVersion_ID=-1&manageType=UCSM&searchBy=servers&loadDataFromJson=undefined


echo "* Load functions"

#########################


function getjsontofile() {
    url="$1"
    file="$2"
    if [ -z $1 ]; then
        echo "No url specified, exiting"
        exit
    fi
    echo "Pulling $url to $file"

    # Fetching JSON payload:
    # curl --header 'Content-Type: application/json' \
    #   'https://pwc014-nextgen-prod-rcdn.cisco.com/public/v2/searchBy/server/searchResults?serverType_ID=0&serverModel_ID=209,248&processor_ID=153&osVendor_ID=5&osVersion_ID=1025&firmwareVersion_ID=-1&manageType=UCSM&searchBy=servers&loadDataFromJson=undefined

    curl --progress-bar --header 'Content-Type: application/json' "$url" -o "$file"
}

function gethtmltotitle() {
    url=$1
    echo "Pulling $url"

    curl --progress-bar "$url" -o "$outdir/temp_index.html"
#    wget -q --show-progress -O "$outdir/temp_index.html" "$url"

#    tidy -m "$outdir/temp_index.html"

    title_data=$(grep "<title" "$outdir/temp_index.html" | head -20 | cut -d'>' -f2-)

    if [[ "$title_data" =~ "</title>" ]]; then
        title_data=$(echo "$title_data" | sed 's/........$//')
    fi

    echo "Title is \"$title_data\""
    mv "$outdir/temp_index.html" "$outdir/$title_data".html

}




#########################
# Pull all the HTML and JSON files

echo "* Create dirs"

# output dir
# outdir="~/Downloads/ucs-firmware-docs"
outdir=./ucs-firmware-docs
mkdir -p $outdir
jsondir=./jsondata
mkdir -p $jsondir


echo "* Fetch CLI guides"
# Fetch CLI Guides
for key in "${!cliguides[@]}"; do
#  echo "Key: $key Value: ${relnotes[$key]}"
  gethtmltotitle "${cliguides[$key]}"
done


echo "* Fetch release notes"
# Fetch release notes
for key in "${!relnotes[@]}"; do
#  echo "Key: $key Value: ${relnotes[$key]}"
  gethtmltotitle "${relnotes[$key]}"
done

echo "* Fetch datasheets"
for key in "${!datasheets[@]}"; do
#  echo "Key: $key Value: ${datasheets[$key]}"
  gethtmltotitle "${datasheets[$key]}"
done

echo "* Fetch whitepapers"
for key in "${!whitepapers[@]}"; do
#  echo "Key: $key Value: ${datasheets[$key]}"
  gethtmltotitle "${whitepapers[$key]}"
done


echo "* Fetch HCL json data"
for key in "${!hcl[@]}"; do
#  echo "Key: $key Value: ${hcl[$key]}"
  getjsontofile "${hcl[$key]}" "$jsondir/$key.json"
done

echo "* Fetch JSON data - equivalency matrix and upgrade matrix"
for key in "${!jsons[@]}"; do
#  echo "Key: $key Value: ${jsons[$key]}"
  getjsontofile "${jsons[$key]}" "$jsondir/$key.json"
done
