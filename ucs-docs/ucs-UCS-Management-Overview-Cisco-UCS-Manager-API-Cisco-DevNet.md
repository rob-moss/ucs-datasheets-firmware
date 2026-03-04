# UCS Management Overview - Cisco UCS Manager API - Cisco DevNet

| | |
|---|---|
| **URL Title** | UCS Management Overview - Cisco UCS Manager API - Cisco DevNet |
| **URL** | https://developer.cisco.com/docs/ucs-dev-center/ucs-management-overview/ |
| **Long URL** |  |
| **HTML Title** | UCS Management Overview - Cisco UCS Manager API - Cisco DevNet |
| **Source file** | `ucs-docs-raw/html/ucs-management-overview.html` |
| **File type** | HTML |
| **Fetched on** | 2026-03-04 11:11:06 |

---

## Page 1: https://developer.cisco.com/docs/ucs-dev-center/ucs-management-overview/

# UCS Management Overview

![](https://pubhub.devnetcloud.com/media/ucs-dev-center/docs/images/blog-ucs-management-01-550x225.jpg)

Some hardware vendors are talking about their products as if they invented the concept of infrastructure as code. Cisco UCS was architected as [programmable infrastructure](https://www.cisco.com/c/en/us/solutions/data-center-virtualization/programmable-infrastructure/index.html#~overview) from its inception seven years ago. We’ve continued to enhance the programmability we offer you with application program interfaces (APIs), tools, orchestration and integration to fit your coding desires and requirements. 

## Unified UCS Management

The latest release of **UCS Manager, version 3** , brings together into one place support for the 2nd generation [UCS](https://www.cisco.com/go/ucs) hardware and the latest 3rd, 4th and 5th generation UCS hardware. It includes support for UCS Mini, UCS C-Series and B-Series servers, Cisco HyperFlex hyperconverged infrastructure, and Cisco composable infrastructure – the UCS C3260 and M-Series. It features a new HTLM5 interface.

![](https://pubhub.devnetcloud.com/media/ucs-dev-center/docs/images/blog-ucs-management-02.jpg)  
  


## UCS PowerTool Suite, It’s Sweet

I’m really excited about UCS Manager Version 3 and I think you should be too, because it is supplemented by some really great programmability tools. There is the [UCS PowerTool 2.0](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/sw/msft_tools/All_Plugin_RN/PowerTool/2x/b_Cisco_UCS_PowerTool_Suite_Release_Notes_2x.html) suite with support for [Microsoft’s Desired State Configuration](https://docs.microsoft.com/en-us/powershell/dsc/overview) (DSC). PowerTool has a unified installer and support for UCS Manager, UCS Central and UCS IMC on C and E-Series, as well as consolidation of duplicated cmdlets across the suite. For example, Set-UcsCentralConfiguration and Set-UcsPowerToolConfiguration are combined into Set-UcsPowerToolConfiguration. These changes as well as a listing of all the newly added Cmdlets are fully described in the [UCS PowerTool Release Notes](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/sw/msft_tools/All_Plugin_RN/PowerTool/2x/b_Cisco_UCS_PowerTool_Suite_Release_Notes_2x.html).

Be sure to read the release notes and the user guides as well as download the software.

A little more about UCS PowerTool and Microsoft DSC: UCS PowerTool includes a ConvertTo-UcsDSCConfig cmdlet. This cmdlet generates DSC configuration code based on actions carried out in the UCS Manager GUI. Utilize the ConvertTo-UcsDSCConfig cmdlet along with DSC support for UCS Objects, syncing a UCS Object from a reference UCS Domain, syncing a UCS Object from a backup or running a script to bring UCS objects to their desired state.

## UCS Python SDK

Maybe PowerShell isn’t you’re thing; perhaps you prefer [Python](https://www.python.org/). Well it just so happens that there is a [UCS Manager Python SDK](https://github.com/CiscoUcs/ucsmsdk) in the final stages of development. The UCS Manager Python SDK is currently hosted on [github](https://github.com/) under the [CiscoUcs](https://github.com/CiscoUcs) account. The SDK is currently beta. You can follow the progress of the UCS Python SDK in the UCS section of [Cisco Communities](https://communities.cisco.com/docs/DOC-64378) and check out the ever growing library of [UCS Manager Python SDK samples](https://github.com/CiscoUcs/ucsmsdk_samples) as well as the [documentation](https://github.com/CiscoUcs/ucsmsdk_samples).

The UCS Python SDKs are built to support Python 2 & 3, the SDKs can be installed via PIP, are PEP8 compliant and have support to create python code from actions in the UCS Manager Graphical Interface with the built-in convert_to_ucs_python() functionality. Let me reiterate to make sure I get the point across; the UCS Manager Python SDK can generate UCS Manager Python SDK code!

## Go Right to the Source

UCS PowerTool and the Python SDK are built on top of the UCS Management open XML APIs; they compose the XML needed for the API request and parse the response. Of course you can always go straight to the source and use the XML API directly. There are user guides for each of the UCS XML API choices. As long as the programming language you want to use supports writing an HTTP client you’re good to go. Or, use utilities like curl or Postman to quickly prototype.

  * [Cisco UCS Manager XML API Programmer’s Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/sw/api/b_ucs_api_book.html)
  * [Cisco UCS Rack-Mount Servers CIMC XML API Programmer’s Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/c/sw/api/b_cimc_api_book.html)
  * [Cisco UCS Central XML API Programmer’s Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-central/api/b_UCSC_XML_API_book.html)


## Emulation at Its Best

I know what you’re thinking, I can’t just have my developers go at it on our systems, they’re in production or being used for dev, CI, UA testing, UI testing, etc. No problem: just get the [UCS Platform Emulator 3.1](https://communities.cisco.com/docs/DOC-37827); every developer can have their own. The great thing about the UCS Platform Emulator is that it is built on the same code as the actual product. Code that is written against the emulator works with UCS Manager.

The emulator also has the complete UCS Manager Object Model documentation; the object model documentation alone is worth the download! The Object Model Documentation has all the classes, methods, faults, syslog messages, and more. Another benefit is that one or more UCS Platform Emulators can be registered to [UCS Central](https://www.cisco.com/c/en/us/products/servers-unified-computing/ucs-central-software/index.html), to truly represent a real UCS deployment. The UCS Platform Emulator works so well that it has become an integral part of the offerings at [Cisco dCloud](https://dcloud.cisco.com/); for example the “[Cisco ACI Business Value Demo v2](https://dcloud-docs.cisco.com/c/r/dcloud-docs/sites/en_us/explore/business_value/all-bvds/Cisco-ACI-V2.html)” dCloud offering utilizes the Cisco Unified Computing System [Platform Emulator 4.0](https://community.cisco.com/t5/unified-computing-system-knowledge-base/cisco-ucs-platform-emulator-4-0-4epe1/ta-p/3953328).(4.5.1).

## Free Tools and Community Support

Perhaps the biggest news of all is that UCS PowerTool Suite 2.X with support for Microsoft DSC, the Python UCS Manager SDK, the Python UCS IMC SDK and the UCS Platform Emulator are all Free! And UCS Programmability tools have [community support](https://communities.cisco.com/community/technology/datacenter/compute-and-storage/ucs_management) and are represented in [Cisco DevNet](https://developer.cisco.com/site/ucs-dev-center/index.gsp)

## UCS Central is Also Programmable

I’ve mentioned [UCS Central](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/release/notes/RN-CiscoUCSCentral_1-4.html) a couple of times. It was very recently updated with a significant number of additional capabilities, an HTML5 interface and a new task based orientation. Even if you only have one UCS Domain you should really be using UCS Central. UCS Management over multiple UCS domains through UCS Central is as programmable and automated as the other UCS management options via [UCS Central PowerTool](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/sw/msft_tools/UCS_Central/powertools/user_guide/2x/b_Cisco_UCS_Central_PowerTool_UG_Release_2_x.html) for UCS Central, and you can also go straight to the [UCS Central XML API](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-central/api/b_UCSC_XML_API_book.html).

PowerShell, Python, the emulator, and all Cisco UCS and Cisco HyperFlex products allow you take advantage of the ALL programmatic capabilities that UCS management options have to offer. How you use them is up to you…

---
