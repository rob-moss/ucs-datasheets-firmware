# Cisco UCS Manager PowerTool User Guide, Release 3.x - Cisco

| | |
|---|---|
| **URL Title** | Cisco UCS Manager PowerTool User Guide, Release 3.x - Cisco |
| **URL** | https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/sw/msft_tools/powertools/ucs_powertool_book/3x/b_cisco_ucsm_powertool_ug_release_3x.html |
| **Long URL** |  |
| **HTML Title** | Cisco UCS Manager PowerTool User Guide, Release 3.x |
| **Source file** | `ucs-docs-raw/html/b_cisco_ucsm_powertool_ug_release_3x.html` |
| **File type** | HTML |
| **Fetched on** | 2026-06-24 11:14:44 |

---

## Page 1: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/sw/msft_tools/powertools/ucs_powertool_book/3x/b_cisco_ucsm_powertool_ug_release_3x.html

![Clear Contents of Search](/etc/designs/cdc/fw/i/ic_clear_gray.png)

---

## Page 2: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/sw/msft_tools/powertools/ucs_powertool_book/3x/b_cisco_ucsm_powertool_ug_release_3x/m_ucsm_overview.html

## Cisco UCS Manager PowerTool 

Cisco UCS Manager PowerTool is a PowerShell module which helps automate all aspects of Cisco UCS Manager including server, network, storage, and hypervisor management. PowerTool enables easy integration with the existing IT management processes and tools. 

The PowerTool cmdlets work on the UCS Manager’s Management Information Tree (MIT), performing create, modify, or delete actions on the Managed Objects (MO) in the tree. The next chapter provides an overview of the Cisco UCS Management Information Model (MIM) and relation of PowerTool cmdlets with it. 

The easy way to learn UCS PowerTool configuration is by generating PowerTool cmdlets for performing configuration actions with the GUI using the ConvertTo-UcsCmdlet. For more information, see 

---

## Page 3: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/sw/msft_tools/powertools/ucs_powertool_book/3x/b_cisco_ucsm_powertool_ug_release_3x/m_ucsm_getting_started.html

## Connecting to Cisco UCS Manager

### Procedure

* * *

**Step 1** |  Launch Cisco UCS Manager PowerTool from the desktop shortcut.   
---|---  
**Step 2** |  View all cmdlets, functions, and aliases supported by the Cisco UCS Manager PowerTool. Get-Command -Module Cisco.UcsManager Get-Command -Module Cisco.UcsManager | group CommandType Get-Command -Module Cisco.UcsManager | measure  
**Step 3** |  Connect to a Cisco UCS domain. $handle = Connect-Ucs <ip or hostname> -NotDefault  
  
* * *

### What to do next

---

## Page 4: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/sw/msft_tools/powertools/ucs_powertool_book/3x/b_cisco_ucsm_powertool_ug_release_3x/m_ucsm_examples.html

## PowerTool Cmdlet Generation

Generate cmdlets for the specified actions in UCS Manager web UI, using the following cmdlet:
    
    
    ConvertTo-UcsCmdlet
    

Get xml request and generate cmdlets, using the following cmdlet:
    
    
    ConvertTo-UcsCmdlet -Verbose

Generate cmdlets for action in the specified web UI log, using the following cmdlets:
    
    
    ConvertTo-UcsCmdlet -GuiLog -LiteralPath 'C:\Work\centrale_7128.log.1'
    ConvertTo-UcsCmdlet -GuiLog -Path 'C:\Work\centrale_71*.log.?'
    

Generate cmdlets for the specified xml request, using the following cmdlet:
    
    
    ConvertTo-UcsCmdlet -Xml –Request ‘<lsClone dn="org-root/ls-sp1" inTargetOrg="org-root" inServerName="sp2" inHierarchical="false"></lsClone>’

Generate cmdlets for the specified xml requests in file, using the following cmdlet:
    
    
    ConvertTo-UcsCmdlet -Xml -LiteralPath 'C:\Work\config.xml'

###  Generate cmdlets for the specified MO

From release 1.2(1), you can pipe a manage object to the ConvertTo-UcsCmdlet, and get the cmdlets required to create the managed object. 
    
    
    Get-UcsServiceProfile -Name sp1 | ConvertTo-UcsCmdlet
    Get-UcsServiceProfile -Name sp1 -Hierarchy | ConvertTo-UcsCmdlet

### PowerTool DSC Configuration Generation

ConvertTo-UcsDSCConfig cmdlet reads the UCS Manager GUI logs and generates corresponding DSC configuration file. This functionality is similar to ConvertTo-UcsCmdlet cmdlets. The generated DSC configuration file uses the custom UCS DSC UcsManagedObject and UcsScript resources. 

Generate DSC configuration for the specified actions in UCS GUI.
    
    
    ConvertTo-UcsDSCConfig

![](https://www.cisco.com/content/dam/en/us/td/i/templates/note.gif)  
**Note** | 

* * *

The ConvertTo-UcsDSCConfig cmdlet is supported on UCS Manager Java GUI only.

* * *  
  
---|---  
  
### Generating DSC Configuration from UCS Manager GUI Actions 

You can generate DSC configuration for the actions performed on the UCS Manager GUI using the ConvertTo-UcsDSCConfig cmdlet.

ConvertTo-UcsDSCConfig cmdlet reads the UCS Manager GUI logs and generates corresponding DSC configuration file. This cmdlet is similar to ConvertTo-UcsCmdlet generates cmdlet. The generated DSC configuration file uses the UcsManagedObject and UcsScript resources, which is part of the UCS DSC module. 

For more information on launching UCS Manager GUI, see Generating Cmdlets from UCS Manager web UI Actions. 

After the UCS Manager web UI is launched using PowerShell window with the Cisco.UcsManager module loaded, run the ConvertTo-UcsDSCConfig cmdlet. 

#### Before you begin

### Generating Cmdlets From UCS Manager GUI Actions 

You can generate cmdlets for the actions performed on the UCS Manager GUI using the ConvertTo-UcsCmdlet cmdlet. The Cisco UCS Manager GUI considers a few XML snippets as secure and does not log them. So, the ConvertTo-UcsCmdlet does not find the logs to do the translation. 

To log the xml snippets of all the user actions in the GUI, launch the UCS Manager GUI by using one of the following ways: 

  * Using Start-UcsGuiSession -LogAllXml cmdlet 

  * Manually launch the UCS Manager GUI by performing the following steps: 


#### Procedure

* * *

**Step 1** |  Save the launch link in .jnlp file format. For example, https://<ip_or_hostname>/ucsm/ucsm.jnlp.   
---|---  
**Step 2** |  Right-click the file and open the file with Notepad.   
**Step 3** |  Add the following line after the other property definitions: 

  * For Java versions earlier than Java 7 Update 45, add <property name=" log.show.encrypted" value=" true" />
  * For Java 7 Update 45 and later versions, add <property name=" jnlp.ucsm.log.show.encrypted" value=" true" />

  
**Step 4** |  Save and close the file.   
**Step 5** |  Right-click the file and open with Java™ Web Start Launcher.   
  
* * *

After the UCS Manager GUI is launched, from a PowerShell window with the Cisco UCS Manager PowerTool module loaded, run the ConvertTo-UcsCmdlet cmdlet. 

### Generating Cmdlets from HTML 5 GUI 

In HTML GUI one can start XML recording before doing any operation, and stop the recording to download the log, once the operation is done. 

#### Procedure

* * *

**Step 1** |  Launch UCS Manager using HTML   
---|---  
**Step 2** |  To enable logging: 

  * Use shortcut keys Ctrl + Alt+ q 
  * A link (Record XML ) comes up on the top right corner of the UI. Click on the link.  Perform operation in the GUI. 

  
**Step 3** |  Click on Stop XML Recording link to stop logging.   
**Step 4** |  Enter a log file name in the pop-up.   
**Step 5** |  Click on OK button, file gets downloaded in local system.   
**Step 6** |  Launch UCS Manager PowerTool and run the ConvertTo-UcsCmdlet -xml -LiteralPath 'C:\Work\Ucsm.log’ cmdlet   
  
* * *

---

## Page 5: https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/sw/msft_tools/powertools/ucs_powertool_book/3x/b_cisco_ucsm_powertool_ug_release_3x/m_samples.html

## Fetch all Global Policies
    
    
    $id=(Get-UcsPowerToolConfiguration).InstallDir
    & "${id}\Samples\Get-UcsGlobalPolicy.ps1" bgl-abcd18

See [Cisco Communities](https://communities.cisco.com/docs/DOC-60339) for more Cisco UCS PowerTool sample scripts. 

---
