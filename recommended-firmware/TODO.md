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
