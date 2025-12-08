######################
# 
# urldata.sh
# URLs for pulling data from cisco.com
#





# Whitepapers
declare -A whitepapers
whitepapers["imm-sharing-across-orgs"]='https://www.cisco.com/c/en/us/products/collateral/cloud-systems-management/intersight/imm-con-sharing-across-organization-cloning-wp.html'
whitepapers["perf-tuning-m7"]='https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-b-series-blade-servers/ucs-m7-platforms-wp.html'
whitepapers["vic1500wp"]='https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/unified-computing-system-adapters/ucs-vic-15000-series-ether-fabric-wp.html'



# Release notes associative array
declare -A relnotes
relnotes["42"]='https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/release/notes/cisco-ucs-manager-rn-4-2.html'
relnotes["43"]='https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/release/notes/b_release-notes-ucsm-4_3.html'
relnotes["60"]='https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/release/notes/b_release-notes-ucsm-6_0.html'
relnotes["vic43"]='https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/release/notes/VIC/4-3/b-release-notes-for-cisco-ucs-virtual-interface-card-drivers-release-4-3.html'
relnotes["43crossver"]="https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/release/notes/b_cross-version-fw-support_4_3.html"


# JSON files
# UCS Manager Upgrade Matrix JSON
ucsmupgradematrix='https://www.cisco.com/c/dam/en/us/td/docs/unified_computing/ucs/ucs-manager/UCSM-upgrade-downgrade-matrix/ReleaseMatrix.json'
# Equivalency Matrix
equiv='https://www.cisco.com/c/dam/en/us/td/docs/unified_computing/ucs/c/sw/UCS-Equivalency-Matrix/custom_excel_data.json'
# JSON files associative array
declare -A jsons
jsons["UCS-Equivalency-Matrix"]="$equiv"
jsons["ucsmupgradematrix"]="$ucsmupgradematrix"



# Datasheets associative array
declare -A datasheets # UCS datasheets URLs
# B-Series blades
datasheets["b200m4"]="https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-b200-m4-blade-server/datasheet-c78-732434.html"
datasheets["b200m5"]="https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-b-series-blade-servers/datasheet-c78-739296.html"
datasheets["b200m6"]="https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-b-series-blade-servers/datasheet-c78-2368888.html"
datasheets["b480m5"]="https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-b-series-blade-servers/datasheet-c78-739280.html"
# X-Series blades
datasheets["x210cm6"]="https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-x-series-modular-system/datasheet-c78-2465523.html"
datasheets["x210cm7"]="https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-x-series-modular-system/ucs-x210c-m7-compute-node-ds.html"
datasheets["x210cm8"]="https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-x-series-modular-system/ucs-x210c-m8-compute-node-ds.html"
# # C-Series rackmount servers
# datasheets["c220m4s"]=""
# datasheets["c220m4sx"]=""
# datasheets["c220m5s"]=""
# chassis
datasheets["chas5108"]="https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-5100-series-blade-server-chassis/data_sheet_c78-526830.html"
datasheets["chas9108"]="https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-x-series-modular-system/datasheet-c78-2472574.html"
# IOMs
datasheets["iom2200"]="https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/data_sheet_c78-675243.html" # both 2204 and 2208
#datasheets["iom2208"]="" # same as 2204
datasheets["iom2304"]="https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/datasheet-c78-675243.html"
datasheets["iom2408"]="https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/datasheet-c78-742624.html"
# FIs
datasheets["fi6300"]="https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/datasheet-c78-736682.html"
datasheets["fi6324"]="https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-6300-series-fabric-interconnects/datasheet-c78-732207.html"
datasheets["fi6400"]="https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/datasheet-c78-741116.html"
datasheets["fi6500"]="https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs6536-fabric-interconnect-ds.html"
# VICs
#datasheets["vic1240"]=""
#datasheets["vic1280"]=""
datasheets["vic1340"]="https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/ucs-virtual-interface-card-1340/datasheet-c78-732517.html"
datasheets["vic1380"]="https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/ucs-virtual-interface-card-1380/datasheet-c78-732516.html"
datasheets["vic1400"]="https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/unified-computing-system-adapters/datasheet-c78-741130.html"
datasheets["vic15000"]="https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/unified-computing-system-adapters/ucs-vic-15000-series-ds.html"





declare -A hcl
# UCS Managed Mode
hcl["ucsm-b480m5-v1-esxi-8u3"]='https://pwc014-nextgen-prod-rcdn.cisco.com/public/v2/searchBy/server/searchResults?serverType_ID=0&serverModel_ID=209,248&processor_ID=153&osVendor_ID=5&osVersion_ID=1025&firmwareVersion_ID=-1&manageType=UCSM&searchBy=servers&loadDataFromJson=undefined'
hcl["ucsm-b480m5-v1-esxi-7u3"]='https://pwc014-nextgen-prod-rcdn.cisco.com/public/v2/searchBy/server/searchResults?serverType_ID=0&serverModel_ID=209,248&processor_ID=153&osVendor_ID=5&osVersion_ID=936&firmwareVersion_ID=-1&manageType=UCSM&searchBy=servers&loadDataFromJson=undefined'
# b200m4 cpuv3 variants
hcl["ucsm-b200m4-v3-esxi-67u3"]="https://pwc014-nextgen-prod-rcdn.cisco.com/public/v2/searchBy/server/searchResults?serverType_ID=0&serverModel_ID=51,157&processor_ID=61&osVendor_ID=5&osVersion_ID=909&firmwareVersion_ID=-1&manageType=UCSM&searchBy=servers&loadDataFromJson=undefined"
hcl["ucsm-b200m4-v3-esxi-73u3"]="https://pwc014-nextgen-prod-rcdn.cisco.com/public/v2/searchBy/server/searchResults?serverType_ID=0&serverModel_ID=51,157&processor_ID=61&osVendor_ID=5&osVersion_ID=936&firmwareVersion_ID=-1&manageType=UCSM&searchBy=servers&loadDataFromJson=undefined"
#hcl["ucsm-b200m4v3esxi83u3"]=""
# b200m4 cpuv4 variants
hcl["ucsm-b200m4-v4-esxi-67u3"]="https://pwc014-nextgen-prod-rcdn.cisco.com/public/v2/searchBy/server/searchResults?serverType_ID=0&serverModel_ID=51,157&processor_ID=84&osVendor_ID=5&osVersion_ID=909&firmwareVersion_ID=-1&manageType=UCSM&searchBy=servers&loadDataFromJson=undefined"
hcl["ucsm-b200m4-v4-esxi-73u3"]="https://pwc014-nextgen-prod-rcdn.cisco.com/public/v2/searchBy/server/searchResults?serverType_ID=0&serverModel_ID=51,157&processor_ID=84&osVendor_ID=5&osVersion_ID=936&firmwareVersion_ID=-1&manageType=UCSM&searchBy=servers&loadDataFromJson=undefined"
#hcl["ucsm-b200m4v4esxi83u3"]=""
# b200m5 variants
hcl["ucsm-b200m5-v1-esxi-67u3"]="https://pwc014-nextgen-prod-rcdn.cisco.com/public/v2/searchBy/server/searchResults?serverType_ID=0&serverModel_ID=199,247&processor_ID=148&osVendor_ID=5&osVersion_ID=909&firmwareVersion_ID=-1&manageType=UCSM&searchBy=servers&loadDataFromJson=undefined"
hcl["ucsm-b200m5-v1-esxi-7u3"]="https://pwc014-nextgen-prod-rcdn.cisco.com/public/v2/searchBy/server/searchResults?serverType_ID=0&serverModel_ID=199,247&processor_ID=148&osVendor_ID=5&osVersion_ID=936&firmwareVersion_ID=-1&manageType=UCSM&searchBy=servers&loadDataFromJson=undefined"
hcl["ucsm-b200m5-v1-esxi-8u3"]="https://pwc014-nextgen-prod-rcdn.cisco.com/public/v2/searchBy/server/searchResults?serverType_ID=0&serverModel_ID=199,247&processor_ID=148&osVendor_ID=5&osVersion_ID=1025&firmwareVersion_ID=-1&manageType=UCSM&searchBy=servers&loadDataFromJson=undefined"
hcl["ucsm-b200m5-v2-esxi-67u3"]="https://pwc014-nextgen-prod-rcdn.cisco.com/public/v2/searchBy/server/searchResults?serverType_ID=0&serverModel_ID=199,247&processor_ID=173&osVendor_ID=5&osVersion_ID=909&firmwareVersion_ID=-1&manageType=UCSM&searchBy=servers&loadDataFromJson=undefined"
hcl["ucsm-b200m5-v2-esxi-7u3"]="https://pwc014-nextgen-prod-rcdn.cisco.com/public/v2/searchBy/server/searchResults?serverType_ID=0&serverModel_ID=199,247&processor_ID=173&osVendor_ID=5&osVersion_ID=936&firmwareVersion_ID=-1&manageType=UCSM&searchBy=servers&loadDataFromJson=undefined"
hcl["ucsm-b200m5-v2-esxi-8u3"]="https://pwc014-nextgen-prod-rcdn.cisco.com/public/v2/searchBy/server/searchResults?serverType_ID=0&serverModel_ID=199,247&processor_ID=173&osVendor_ID=5&osVersion_ID=1025&firmwareVersion_ID=-1&manageType=UCSM&searchBy=servers&loadDataFromJson=undefined"
# b200m6 variants
hcl["ucsm-b200m6-v1-esxi-7u3"]="https://pwc014-nextgen-prod-rcdn.cisco.com/public/v2/searchBy/server/searchResults?serverType_ID=0&serverModel_ID=331&processor_ID=254&osVendor_ID=5&osVersion_ID=936&firmwareVersion_ID=-1&manageType=UCSM&searchBy=servers&loadDataFromJson=undefined"
hcl["ucsm-b200m6-v1-esxi-8u3"]="https://pwc014-nextgen-prod-rcdn.cisco.com/public/v2/searchBy/server/searchResults?serverType_ID=0&serverModel_ID=331&processor_ID=254&osVendor_ID=5&osVersion_ID=1025&firmwareVersion_ID=-1&manageType=UCSM&searchBy=servers&loadDataFromJson=undefined"
# Intersight Managed Mode (imm)
# hcl["imm-b200m4-v3-esxi-67u3"]=""
# hcl["imm-b200m4-v3-esxi-73u3"]=""
# hcl["imm-b200m4-v3-esxi-83u3"]=""


declare -A cliguides
cliguides["cli43admin"]="https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Admin-Management/4-3/b_cisco_ucs_manager_cli_administration_mgmt_guide_4-3.html"
cliguides["cli43firmware"]="https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Firmware-Mgmt/4-3/b_UCSM_CLI_Firmware_Management_Guide_4-3.html"
cliguides["cli43inframgt"]="https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Infrastructure-Mgmt/4-3/b_UCSM_CLI_Infrastructure_Management_Guide_4_3.html"
cliguides["cli43netmgt"]="https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Network-Mgmt/4-3/b_cli_ucsm_network_management_guide_4_3.html"
cliguides["cli43servermgt"]="https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/Server-Mgmt/4-3/b_cisco_ucs_manager_server_mgmt_cli_guide_4_3.html"
cliguides["cli43sysmgt"]="https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/CLI-User-Guides/System-Monitoring/4-3/b-ucsm-cli-system-monitoring-guide-4-3.html"
# cliguides["cli43"]=""
# cliguides["cli43"]=""
# cliguides["cli43"]=""


# Admin guides for CLI and GUI
# https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-and-configuration-guides-list.html
# There are many links here and these links sometimes have other links inside to chapters.
# Likely I will need to use a HTML Mirror mode in wget recursive or similar
# declare -A adminguides
# admninguides["60guigettingstarted"]="https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Getting-Started/6-0/b-cisco-ucs-manager-getting-started-guide-release-6_0.html"
# admninguides["60guiadminmgmt"]="https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Admin-Management/6-0/b_cisco_ucs_admin_mgmt_guide_6_0.html"
# admninguides["60guifwmgmt"]="https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Firmware-Mgmt/6-0/b_UCSM_GUI_Firmware_Management_Guide_6_0.html"
# admninguides["60guiinframgmt"]="https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Infrastructure-Mgmt/6-0/b_UCSM_GUI_Infrastructure_Management_Guide_6_0.html"
# admninguides["60gui"]=""
# admninguides["60gui"]=""



######################


# An attempt to create an associative array of server models for the HCL lookups
#     # {
#     # "T_ID": "238,239",
#     # "ID": "273,274",
#     # "SERVER_MODEL": "Cisco UCS C240 M4SX"
#     # },
# 	# {
# 	# 	"T_ID": "192,193",
# 	# 	"ID": "52,159",
# 	# 	"SERVER_MODEL": "Cisco UCS C220 M4S"
# 	# },

# declare -A server_model # UCSM Server models -- serverModel=
# #server_model[""]=
# server_model["c240m4s"]="52,159"           # serverModelId=52,159
# server_model["c220m4sx"]="273,274" # Cisco UCS C220 M4SX ID=273,274
# server_model["b200m4"]=
# server_model["b480m4"]=
# server_model["b200m5"]=
# server_model["b480m5"]=
# server_model["b200m6"]=


# cat servermodels.json | sed 's/Cisco UCS //g' | sed 's/ //g' | tr '[:upper:]' '[:lower:]' | jq -r '.[] | [ .SERVER_MODEL, .ID ] | @tsv' 
# cat servermodels.json | sed 's/Cisco UCS //g' | sed 's/ //g' | jq -r '.[] | [ .SERVER_MODEL, .ID ] | @tsv' | tr '[:upper:]' '[:lower:]' | awk '{print $1,"=",$2}'


# c220m5sx = 204,259
# c240m5l = 207,265
# c240m5s = 206,262
# c245m6sx = 335,337
# c240m8sx = 400
# c240m6sx = 341
# c245m8sx = 387,403
# c220m8s = 398
# c220m4l = 53,160
# c240m3s2 = 275,276
# c225m6s = 334,355
# c225m6n = 336,353
# c240m4snebs = 290,292
# c220m4s = 52,159
# c240m6l = 340
# c240m6n = 342
# c240m5sd = 300
# c240m6s = 333
# c220m3l = 19,36
# c240m7sn = 361,379
# c220m7n = 363,377
# c460m4 = 50,65,173
# c220m3s = 18,35
# c240m5snebs = 237,264
# c220m7s = 362,378
# c240m3l = 21,38
# c22m3l = 33,47
# c125 = 239,299
# c220m8e3s = 408
# c240m7sx = 360,380
# c240m3s = 20,37
# c22m3s = 22,46
# c220m5snebs = 233,260
# c240m5sx = 236,263
# c225m8s = 389,404
# c240m4s2 = 289,291
# c220m6n = 339
# c480m5 = 221,251
# c240m8e3s = 401
# c225m8n = 388,405
# c480m5ml = 244,293
# c220m6s = 332
# c24m3s2 = 48,295
# c240m4l = 55,162
# c24m3l = 34,49
# c240m4s = 54,161
# c220m5sn = 233,260
# c240m5sn = 237,264
# c24m3s = 23,296
# c220m5l = 205,253
# c240m4sx = 273,274
# c240snebs = 32,304
# c240m6sn = 343
# c3160m3 = 59
# c240m8l = 402



# B200M4 HCL variants
# HCL B200M4 / CPU v2 / ESXi 6.7u3 
# HCL B200M4 / CPU v2 / ESXi 7u3
# HCL B200M4 / CPU v2 / ESXi 8u3
# HCL B200M4 / CPU v3

# B200M5 variants
# HCL B200M5

# Get all Server Models for UCS Manager B-Series
# https://pwc014-nextgen-prod-rcdn.cisco.com/public/v3/searchBy/server/serverModels?treeIdRelease=undefined&osVendorID=undefined&osVersionID=undefined&productTypeID=undefined&productModelID=undefined&serverType=B&releaseID=0&managed=undefined
# Select B200m4 = serverModelID=51,157
# Get all CPU options for B200M4
# https://pwc014-nextgen-prod-rcdn.cisco.com/public/v3/searchBy/server/processors?treeIdServerModel=null&osVendorID=undefined&osVersionID=undefined&serverType=0&serverModel=undefined&serverModelID=51,157&productTypeID=undefined&productModelID=undefined
# b200m4 v3 cpu = processoVersionID=61
# b200m4 v4 cpu = processoVersionID=84
# https://pwc014-nextgen-prod-rcdn.cisco.com/public/v3/searchBy/server/osVendors?treeIdProcessor=null&serverType=0&processoVersionID=61&serverModelID=51,157
# osvendorID=5 # vmware
# osVersion_ID=936 # esxi 7u3
# osVersion_ID=909 # esxi 6.7u3


# b200m5
# serverModelID=199,247
# processoVersionID=148 = v1
# processoVersionID=173 = v2

# b200m6
# serverModelID=331
# processoVersionID=254 # cpu v3
# 


