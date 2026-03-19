# Fetch the recommended firmware

The recommended firmware is the one that Cisco recommends for a given product. It is the one that is most likely to be stable and compatible with the product. It is also the one that is most likely to have the latest features and security updates.

There are two different platforms
- UCS Manager (UCSM)
- Cisco Intersight (Intersight)

### Instructions for Cisco Intersight
* Use an existing Intersight account that has an API key
* Fetch the Server recommended firmware for the product using the Intersight API path to the Firmware Policy
* Fetch the Infrastructure recommended firmware for the product using the Intersight API path to the Domain/FI firmware
* The script should be named `fetch-intersight.py`

The list of Recommended Firmware for Intersight can be found at the following API paths:
For a 6400 series FI:

```bash
curl 'https://us-east-1.intersight.com/api/v1/firmware/Distributables?$inlinecount=allpages&$skip=0&$top=10&$filter=Tags.Key%20eq%20%27cisco.meta.distributabletype%27%20and%20Tags.Value%20eq%20%27IMMFABRIC%27%20and%20Tags.Key%20eq%20%27cisco.meta.repositorytype%27%20and%20Tags.Value%20eq%20%27IntersightCloud%27%20and%20SupportedModels%20in%20(%27UCS-FI-6454%27)%20and%20SharedScope%20eq%20%27shared%27%20and%20(ImportState%20eq%20Imported%20or%20ImportState%20eq%20ReadyForImport)&$orderby=Version%20desc' \
  --compressed \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:148.0) Gecko/20100101 Firefox/148.0' \
  -H 'Accept: */*' \
  -H 'Accept-Language: en' \
  -H 'Accept-Encoding: gzip, deflate, br, zstd' \
  -H 'Referer: https://us-east-1.intersight.com/an/infrastructure-service/an/firmware/upgrade/imm/switch?_targetMoids=63c8cbfe6f72612d344b6745' \
  -H 'x-requested-with: XMLHttpRequest' \
  -H 'DNT: 1' \
  -H 'Sec-GPC: 1' \
  -H 'Connection: keep-alive' \
  -H 'Cookie: fs_uid=#17DKEW#f8eb9de3-3697-4802-bca7-ed7fcbe9a51b:14668768-9bed-4a20-b592-1daab845eb82:1773201913509::1#d408c980#/1804285813; wfx_unq=kxT3qrEXP3Nj7RgH; X-Starship-Token=cd9301908566769e85da39bc16e491b0fda72700dae83687f1f34ab60ab11321-69b0e9f375646133013044e5-5b25418d7a7662743465cf72&intersight-aws-us-east-1; fs_lua=1.1773202002845' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Priority: u=4'
```

Parameters for the API call are as follows:
```parameters
$inlinecount=allpages
$skip=0
$top=10
$filter=Tags.Key%20eq%20%27cisco.meta.distributabletype%27%20and%20Tags.Value%20eq%20%27IMMFABRIC%27%20and%20Tags.Key%20eq%20%27cisco.meta.repositorytype%27%20and%20Tags.Value%20eq%20%27IntersightCloud%27%20and%20SupportedModels%20in%20(%27UCS-FI-6454%27)%20and%20SharedScope%20eq%20%27shared%27%20and%20(ImportState%20eq%20Imported%20or%20ImportState%20eq%20ReadyForImport)
$orderby=Version%20desc
```


JSON blob will have
"RecommendedBuild": "Y",
results.[].RecommendedBuild


Query:
Tags.Key eq 'cisco.meta.distributabletype' and Tags.Value eq 'IMMFABRIC' and Tags.Key eq 'cisco.meta.repositorytype' and Tags.Value eq 'IntersightCloud' and SupportedModels in ('UCS-FI-6454') and SharedScope eq 'shared' and (ImportState eq Imported or ImportState eq ReadyForImport)

API query parameters:
Path:  /api/v1/firmware/Distributables 
$filter = SupportedModels in ('UCS-FI-6454') and RecommendedBuild eq 'Y'
$select = SupportedModels, Mfid, Version, RecommendedBuild, PlatformType, Name






### Instructions for UCS Manager (UCSM)
(Done)
* Visit the URL: `https://software.cisco.com/download/home/283612660/type/283655658/release/`
* Render the HTML of the page
* Find the HTML that matches `<span _ngcontent-xqt-c9="" id="selectedRelease" class="selectedRelease">6.0(1e)</span>`
* There are 3 versions that are the selectedRelease - return each of them
* The script file should be named `fetch-ucsm.py`
* Repeat this for all Infra, B and C series servers


# Script
A script will need to be written to handle the fetching of the recommended firmware. The script will need to be able to handle both UCS Manager and Cisco Intersight platforms. The script will need to be able to fetch the recommended firmware for a given product and return it in a format that can be easily used by other scripts or applications.

You can use any python plugin you need to fetch the HTML of the page and parse it. Some popular libraries for this include `requests` for fetching the HTML and `BeautifulSoup` for parsing the HTML.
Other options are to use the `selenium` library to automate a web browser to fetch the HTML and parse it. This can be useful if the page is dynamic and requires JavaScript to render the content.

If all of that fails, then you can use the MCP server `playwright` library to automate a web browser to fetch the HTML and parse it. This can be useful if the page is dynamic and requires JavaScript to render the content.

Tell me when there are errors, and tell me when there are successful fetches.
Keep going until have a list of recommended firmware, based on the above <span> tags
