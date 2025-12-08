::: {#fw-skiplinks}
-   [Skip to content](#fw-content){#skiplink-content}
-   [Skip to search](#){#skiplink-search}
-   [Skip to footer](#fw-footer-v2){#skiplink-footer .last}
:::

-   [Cisco.com Worldwide](https://www.cisco.com/site/us/en/index.html)
-   [Products and Services](/c/en/us/products/index.html)
-   [Solutions](https://www.cisco.com/site/us/en/solutions/index.html)
-   [Support](/c/en/us/support/index.html)
-   [Learn](/c/en/us/training-events.html)
-   [Explore Cisco](www.cisco.com/c/en/us/about/sitemap.html)
-   [How to Buy](/c/en/us/buy.html)
-   [Partners
    Home](https://www.cisco.com/site/us/en/partners/index.html?dtid=odicdc001129)
-   [Partner
    Program](https://www.cisco.com/site/us/en/partners/cisco-partner-program/index.html?ccid=cc000864&dtid=odiprc001129)
-   [Support](https://www.cisco.com/site/us/en/partners/support-help/index.html)
-   [Tools](https://www.cisco.com/site/us/en/partners/tools/index.html?dtid=odiprc001129)
-   [Find a Cisco
    Partner](https://locatr.cloudapps.cisco.com/WWChannels/LOCATR/pf/index.jsp#/)
-   [Meet our
    Partners](https://www.cisco.com/site/us/en/partners/connect-with-a-partner/index.html?ccid=cc000864&dtid=odiprc001129)
-   [Become a Cisco
    Partner](https://www.cisco.com/site/us/en/partners/index.html?dtid=odicdc001129)

::: {#fw-content .container .grid}
::: {.row .full .blowout owner="ID"}
::: {.col .full}
-   [](#){.skip}
-   [[Support]{itemprop="name"}](/c/en/us/support/index.html)
    []{.caret}
-   [[Product
    Support]{itemprop="name"}](/c/en/us/support/all-products.html)
    []{.caret}
-   [[Servers - Unified
    Computing]{itemprop="name"}](/c/en/us/support/servers-unified-computing/category.html)
    []{.caret}
-   [[Cisco UCS
    Manager]{itemprop="name"}](/c/en/us/support/servers-unified-computing/ucs-manager/series.html)
    []{.caret}
-   [[Release
    Notes]{itemprop="name"}](/c/en/us/support/servers-unified-computing/ucs-manager/products-release-notes-list.html)
    []{.caret}

# Cisco UCS Manager Cross-Version Firmware Support, Release 4.3 {#fw-pagetitle owner="ID"}
:::
:::

::: {.row .blowout .wide-narrow-v2 .visitedlinks}
::: {.col .wide-v2}
::: {.docHeaderComponent .base-blowout}
::: {.linksRow}
::: {.versionddcontainer}
:::

::: {.toolbar}
::: {#saveModule .noprint}
Save
:::

::: {.saveDocumentMessage .login .cdc-expandPanel role="region" aria-live="polite"}
[Log
in](/c/login/index.html?referer=/c/en/us/td/docs/unified_computing/ucs/release/notes/b_cross-version-fw-support_4_3.html)
to Save Content
:::

::: {.noprint .downloadDocument}
::: {.toolbarIcon .downloadIcon}
:::

Download
:::

::: {.noprint .printDocument .js-only}
::: {.toolbarIcon .printIcon}
:::

Print
:::
:::
:::

::: {.availableLanguagesList}
### Available Languages
:::

::: {#download-list-container .noprint .panelRow role="region" aria-live="polite"}
::: {.download-list aria-label="Download Options"}
### Download Options

-   ::: {.fileText}
    [](/c/en/us/td/docs/unified_computing/ucs/release/notes/b_cross-version-fw-support_4_3.pdf){.download-pdf}
    ::: {.fileIcon .pdfIcon}
    :::

    PDF [(144.8 KB)]{.docSize}\
    [View with Adobe Reader on a variety of devices]{.description}
    :::
:::
:::

::: {.infobarClearFix}
::: {.infobar}
::: {.updatedDate}
Updated:September 23, 2025
:::
:::

::: {.disclaimers .techdocs}
::: {.disclaimerButtons}
::: {.aboutBias}
Bias-Free Language
:::
:::

::: {.biasfreeContent .panel}
### Bias-Free Language

The documentation set for this product strives to use bias-free
language. For the purposes of this documentation set, bias-free is
defined as language that does not imply discrimination based on age,
disability, gender, racial identity, ethnic identity, sexual
orientation, socioeconomic status, and intersectionality. Exceptions may
be present in the documentation due to language that is hardcoded in the
user interfaces of the product software, language used based on RFP
documentation, or language that is used by a referenced third-party
product. [Learn
more](https://www.cisco.com/c/en/us/about/social-justice/inclusive-language-policy.html)
about how Cisco is using Inclusive Language.
:::
:::
:::
:::

::: {#eot-doc-wrapper}
::: {role="main"}
## Contents {#contents .topictitle2}

-   [Cisco UCS Manager Cross-Version Firmware Support, Release
    4.3](#ucsmRN_43_crossversion)

**First Published: September 23, 2025**

# Cisco UCS Manager Cross-Version Firmware Support, Release 4.3 {#ariaid-title1 .title .topictitle1}

::: {.body .conbody}
::: {#ucsmRN_43_crossversion__section_6ECD6C7EC81A4918A2143BBC86A94E28 .section .section}
The Cisco UCS Manager A bundle software (Cisco UCS Manager, Cisco NX-OS,
IOM and FEX firmware) can be mixed with previous B or C bundle releases
on the servers (host firmware \[FW\], BIOS, Cisco IMC, adapter FW and
drivers).

[Cisco UCS Equivalency Matrix for Cisco Intersight, Cisco IMC, and Cisco
UCS
Manager](https://www.cisco.com/c/dam/en/us/td/docs/unified_computing/ucs/c/sw/UCS-Equivalency-Matrix/index.html){.xref}
outlines the release timeline for Cisco Intersight, Cisco Integrated
Management Controller (IMC), and Cisco UCS Manager (UCS Manager). It
includes essential information such as the date each patch was posted,
the specific patch version, and the platforms that are supported by each
release. By referring to this matrix, you can identify the appropriate
firmware and software versions required for your servers before
migrating them to Cisco Intersight. This ensures that your server
infrastructure remains supported and operates efficiently during and
after the transition.

The following table lists the mixed A, B, and C bundle versions that are
supported on Cisco UCS 6300, 6400 series and 6536 Fabric Interconnects:

|                                   | Infrastructure Versions (A Bundles) |                             |                             |                                    |                                    |                                    |                                    |                                    |                                          |                                    |                                    |                                    |                                    |                                    |
|-----------------------------------|-------------------------------------|-----------------------------|-----------------------------|------------------------------------|------------------------------------|------------------------------------|------------------------------------|------------------------------------|------------------------------------------|------------------------------------|------------------------------------|------------------------------------|------------------------------------|------------------------------------|
| Host FW Versions (B or C Bundles) | 4.0(1)                              | 4.0(2)                      | 4.0(4)                      | 4.1(1)                             | 4.1(2)                             | 4.1(3)                             | 4.2(1)                             | 4.2(2)                             | 4.2(3)                                   | 4.3(2)                             | 4.3(3)                             | 4.3(4)                             | 4.3(5)                             | 4.3(6)                             |
| 4.3(6)                            | ---                                 | ---                         | ---                         | ---                                | ---                                | ---                                | ---                                | ---                                | ---                                      | 6332, 6332-16UP, 6454, 64108, 6536 | 6332, 6332-16UP, 6454, 64108, 6536 | 6332, 6332-16UP, 6454, 64108, 6536 | 6332, 6332-16UP, 6454, 64108, 6536 | 6332, 6332-16UP, 6454, 64108, 6536 |
| 4.3(5)                            | ---                                 | ---                         | ---                         | ---                                | ---                                | ---                                | ---                                | ---                                | ---                                      | 6332, 6332-16UP, 6454, 64108, 6536 | 6332, 6332-16UP, 6454, 64108, 6536 | 6332, 6332-16UP, 6454, 64108, 6536 | 6332, 6332-16UP, 6454, 64108, 6536 | 6332, 6332-16UP, 6454, 64108, 6536 |
| 4.3(4)                            | ---                                 | ---                         | ---                         | ---                                | ---                                | ---                                | ---                                | ---                                | ---                                      | 6332, 6332-16UP, 6454, 64108, 6536 | 6332, 6332-16UP, 6454, 64108, 6536 | 6332, 6332-16UP, 6454, 64108, 6536 | 6332, 6332-16UP, 6454, 64108, 6536 | 6332, 6332-16UP, 6454, 64108, 6536 |
| 4.3(3)                            | ---                                 | ---                         | ---                         | ---                                | ---                                | ---                                | ---                                | ---                                | ---                                      | 6332, 6332-16UP, 6454, 64108, 6536 | 6332, 6332-16UP, 6454, 64108, 6536 | 6332, 6332-16UP, 6454, 64108, 6536 | 6332, 6332-16UP, 6454, 64108, 6536 | 6332, 6332-16UP, 6454, 64108, 6536 |
| 4.3(2)                            | ---                                 | ---                         | ---                         | ---                                | ---                                | ---                                | ---                                | ---                                | ---                                      | 6332, 6332-16UP, 6454, 64108, 6536 | 6332, 6332-16UP, 6454, 64108, 6536 | 6332, 6332-16UP, 6454, 64108, 6536 | 6332, 6332-16UP, 6454, 64108, 6536 | 6332, 6332-16UP, 6454, 64108, 6536 |
| 4.2(3)                            | ---                                 | ---                         | ---                         | ---                                | ---                                | ---                                | 6200, 6332, 6332-16UP, 6454, 64108 | 6200, 6332, 6332-16UP, 6454, 64108 | 6200, 6332, 6332-16UP, 6454, 64108, 6536 | 6332, 6332-16UP, 6454, 64108, 6536 | 6332, 6332-16UP, 6454, 64108, 6536 | 6332, 6332-16UP, 6454, 64108, 6536 | 6332, 6332-16UP, 6454, 64108, 6536 | 6332, 6332-16UP, 6454, 64108, 6536 |
| 4.2(2)                            | ---                                 | ---                         | ---                         | ---                                | ---                                | ---                                | 6200, 6332, 6332-16UP, 6454, 64108 | 6200, 6332, 6332-16UP, 6454, 64108 | 6200, 6332, 6332-16UP, 6454, 64108       | 6332, 6332-16UP, 6454, 64108       | 6332, 6332-16UP, 6454, 64108       | 6332, 6332-16UP, 6454, 64108       | 6332, 6332-16UP, 6454, 64108       | 6332, 6332-16UP, 6454, 64108       |
| 4.2(1)                            | ---                                 | ---                         | ---                         | ---                                | ---                                | ---                                | 6200, 6332, 6332-16UP, 6454, 64108 | 6200, 6332, 6332-16UP, 6454, 64108 | 6200, 6332, 6332-16UP, 6454, 64108       | 6332, 6332-16UP, 6454, 64108       | 6332, 6332-16UP, 6454, 64108       | 6332, 6332-16UP, 6454, 64108       | 6332, 6332-16UP, 6454, 64108       | 6332, 6332-16UP, 6454, 64108       |
| 4.1(3)                            | ---                                 | ---                         | ---                         | 6200, 6332, 6332-16UP, 6454, 64108 | 6200, 6332, 6332-16UP, 6454, 64108 | 6200, 6332, 6332-16UP, 6454, 64108 | 6200, 6332, 6332-16UP, 6454, 64108 | 6200, 6332, 6332-16UP, 6454, 64108 | 6200, 6332, 6332-16UP, 6454, 64108       | 6332, 6332-16UP, 6454, 64108       | 6332, 6332-16UP, 6454, 64108       | 6332, 6332-16UP, 6454, 64108       | 6332, 6332-16UP, 6454, 64108       | 6332, 6332-16UP, 6454, 64108       |
| 4.1(2)                            | ---                                 | ---                         | ---                         | 6200, 6332, 6332-16UP, 6454, 64108 | 6200, 6332, 6332-16UP, 6454, 64108 | 6200, 6332, 6332-16UP, 6454, 64108 | 6200, 6332, 6332-16UP, 6454, 64108 | 6200, 6332, 6332-16UP, 6454, 64108 | 6200, 6332, 6332-16UP, 6454, 64108       | ---                                | ---                                | ---                                | ---                                | ---                                |
| 4.1(1)                            | ---                                 | ---                         | ---                         | 6200, 6332, 6332-16UP, 6454, 64108 | 6200, 6332, 6332-16UP, 6454, 64108 | 6200, 6332, 6332-16UP, 6454, 64108 | 6200, 6332, 6332-16UP, 6454, 64108 | 6200, 6332, 6332-16UP, 6454, 64108 | 6200, 6332, 6332-16UP, 6454, 64108       | ---                                | ---                                | ---                                | ---                                | ---                                |
| 4.0(4)                            | 6200, 6332, 6332-16UP, 6454         | 6200, 6332, 6332-16UP, 6454 | 6200, 6332, 6332-16UP, 6454 | 6200, 6332, 6332-16UP, 6454        | 6200, 6332, 6332-16UP, 6454        | 6200, 6332, 6332-16UP, 6454        | 6200, 6332, 6332-16UP, 6454        | 6200, 6332, 6332-16UP, 6454        | 6200, 6332, 6332-16UP, 6454              | ---                                | ---                                | ---                                | ---                                | ---                                |
| 4.0(2)                            | 6200, 6332, 6332-16UP, 6454         | 6200, 6332, 6332-16UP, 6454 | 6200, 6332, 6332-16UP, 6454 | 6200, 6332, 6332-16UP, 6454        | 6200, 6332, 6332-16UP, 6454        | 6200, 6332, 6332-16UP, 6454        | 6200, 6332, 6332-16UP, 6454        | 6200, 6332, 6332-16UP, 6454        | 6200, 6332, 6332-16UP, 6454              | ---                                | ---                                | ---                                | ---                                | ---                                |
| 4.0(1)                            | 6200, 6332, 6332-16UP, 6454         | 6200, 6332, 6332-16UP, 6454 | 6200, 6332, 6332-16UP, 6454 | 6200, 6332, 6332-16UP, 6454        | 6200, 6332, 6332-16UP, 6454        | 6200, 6332, 6332-16UP, 6454        | 6200, 6332, 6332-16UP, 6454        | 6200, 6332, 6332-16UP, 6454        | 6200, 6332, 6332-16UP, 6454              | ---                                | ---                                | ---                                | ---                                | ---                                |

: [Table 1. ]{.table--title-label .tabletitle}[Mixed Cisco UCS Releases
Supported on Cisco UCS 6300, 6400, 6536 Series Fabric
Interconnects]{.tabletitle}

The following table lists the mixed A and B bundle versions that are
supported on [Cisco UCS X-Series Direct]{.ph}:

+-----------------+-----------------+-----------------+-----------------+
| Host FW         | Infrastructure  |                 |                 |
| Versions (B     | Versions (A     |                 |                 |
| Bundles)        | Bundles)        |                 |                 |
+=================+=================+=================+=================+
|                 | 4.3(4)          | 4.3(5)          | 4.3(6)          |
+-----------------+-----------------+-----------------+-----------------+
| 4.3(6)          | UCSX-S9108-100G | UCSX-S9108-100G | UCSX-S9108-100G |
+-----------------+-----------------+-----------------+-----------------+
| 4.3(5)          | UCSX-S9108-100G | UCSX-S9108-100G | UCSX-S9108-100G |
+-----------------+-----------------+-----------------+-----------------+
| 4.3(4)          | UCSX-S9108-100G | UCSX-S9108-100G | UCSX-S9108-100G |
+-----------------+-----------------+-----------------+-----------------+
| <table          |                 |                 |                 |
| class="olh_note |                 |                 |                 |
| " data-border=" |                 |                 |                 |
| 0" role="note"> |                 |                 |                 |
| <colgroup>      |                 |                 |                 |
| <col style=     |                 |                 |                 |
| "width: 50%" /> |                 |                 |                 |
| <col style=     |                 |                 |                 |
| "width: 50%" /> |                 |                 |                 |
| </colgroup>     |                 |                 |                 |
| <tbody>         |                 |                 |                 |
| <               |                 |                 |                 |
| tr class="odd"> |                 |                 |                 |
| <               |                 |                 |                 |
| td class="olh_n |                 |                 |                 |
| ote" width="1%" |                 |                 |                 |
|  role="heading" |                 |                 |                 |
|  data-border="0 |                 |                 |                 |
| "><p><strong>No |                 |                 |                 |
| te</strong></p> |                 |                 |                 |
|  </td>          |                 |                 |                 |
| <td             |                 |                 |                 |
| class="olh_note |                 |                 |                 |
| " data-border=" |                 |                 |                 |
| 0"><div class=" |                 |                 |                 |
| note__content"> |                 |                 |                 |
| <p>In a setup e |                 |                 |                 |
| quipped with <s |                 |                 |                 |
| pan class="ph"> |                 |                 |                 |
| Cisco UCS X210c |                 |                 |                 |
|  M8 Compute Nod |                 |                 |                 |
| e</span>, you c |                 |                 |                 |
| annot downgrade |                 |                 |                 |
|  Infrastructure |                 |                 |                 |
|  Version (A Bun |                 |                 |                 |
| dle) or Host Fi |                 |                 |                 |
| rmware Version  |                 |                 |                 |
| (B bundle) to a |                 |                 |                 |
| ny release earl |                 |                 |                 |
| ier than <span  |                 |                 |                 |
| class="ph">4.3( |                 |                 |                 |
| 6a)</span>.</p> |                 |                 |                 |
| <p>             |                 |                 |                 |
| In a setup equi |                 |                 |                 |
| pped with <span |                 |                 |                 |
|  class="ph">Cis |                 |                 |                 |
| co UCS X-Series |                 |                 |                 |
|  Direct</span>, |                 |                 |                 |
|  you cannot dow |                 |                 |                 |
| ngrade Infrastr |                 |                 |                 |
| ucture Version  |                 |                 |                 |
| (A Bundle) to a |                 |                 |                 |
| ny release earl |                 |                 |                 |
| ier than <span  |                 |                 |                 |
| class="ph">4.3( |                 |                 |                 |
| 4b)</span>.</p> |                 |                 |                 |
| </div></td>     |                 |                 |                 |
| </tr>           |                 |                 |                 |
| </tbody>        |                 |                 |                 |
| </table>        |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

: [Table 2. ]{.table--title-label .tabletitle}[Mixed Cisco UCS Releases
Supported on [Cisco UCS X-Series Direct]{.ph}]{.tabletitle}

The following table lists the mixed A, B, and C bundle versions that are
supported on Cisco UCS Mini fabric interconnects:

|                                   | Infrastructure Versions (A Bundles) |        |        |        |        |        |        |        |        |        |        |        |        |        |
|-----------------------------------|-------------------------------------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| Host FW Versions (B or C Bundles) | 4.0(1)                              | 4.0(2) | 4.0(4) | 4.1(1) | 4.1(2) | 4.1(3) | 4.2(1) | 4.2(2) | 4.2(3) | 4.3(2) | 4.3(3) | 4.3(4) | 4.3(5) | 4.3(6) |
| 4.3(6)                            | ---                                 | ---    | ---    | ---    | ---    | ---    | ---    | ---    | ---    | 6324   | 6324   | 6324   | 6324   | 6324   |
| 4.3(5)                            | ---                                 | ---    | ---    | ---    | ---    | ---    | ---    | ---    | ---    | 6324   | 6324   | 6324   | 6324   | 6324   |
| 4.3(4)                            | ---                                 | ---    | ---    | ---    | ---    | ---    | ---    | ---    | ---    | 6324   | 6324   | 6324   | 6324   | 6324   |
| 4.3(3)                            | ---                                 | ---    | ---    | ---    | ---    | ---    | ---    | ---    | ---    | 6324   | 6324   | 6324   | 6324   | 6324   |
| 4.3(2)                            | ---                                 | ---    | ---    | ---    | ---    | ---    | ---    | ---    | ---    | 6324   | 6324   | 6324   | 6324   | 6324   |
| 4.2(3)                            | ---                                 | ---    | ---    | ---    | ---    | ---    | 6324   | 6324   | 6324   | 6324   | 6324   | 6324   | 6324   | 6324   |
| 4.2(2)                            | ---                                 | ---    | ---    | ---    | ---    | ---    | 6324   | 6324   | 6324   | 6324   | 6324   | 6324   | 6324   | 6324   |
| 4.2(1)                            | ---                                 | ---    | ---    | ---    | ---    | ---    | 6324   | 6324   | 6324   | 6324   | 6324   | 6324   | 6324   | 6324   |
| 4.1(3)                            | ---                                 | ---    | ---    | 6324   | 6324   | 6324   | 6324   | 6324   | 6324   | 6324   | 6324   | 6324   | 6324   | 6324   |
| 4.1(2)                            | ---                                 | ---    | ---    | 6324   | 6324   | 6324   | 6324   | 6324   | 6324   | ---    | ---    | ---    | ---    | ---    |
| 4.1(1)                            | ---                                 | ---    | ---    | 6324   | 6324   | 6324   | 6324   | 6324   | 6324   | ---    | ---    | ---    | ---    | ---    |
| 4.0(4)                            | 6324                                | 6324   | 6324   | 6324   | 6324   | 6324   | 6324   | 6324   | 6324   | ---    | ---    | ---    | ---    | ---    |
| 4.0(2)                            | 6324                                | 6324   | 6324   | 6324   | 6324   | 6324   | ---    | ---    | ---    | ---    | ---    | ---    | ---    | ---    |
| 4.0(1)                            | 6324                                | 6324   | 6324   | 6324   | 6324   | 6324   | ---    | ---    | ---    | ---    | ---    | ---    | ---    | ---    |

: [Table 3. ]{.table--title-label .tabletitle}[Mixed Cisco UCS Releases
Supported on Cisco UCS Mini Fabric Interconnects]{.tabletitle}

The following table lists the mixed B, C bundles that are supported on
all platforms with the 4.3(6)A bundle:

+----------+------------+------------+----------+----------+----------+
|          | Infr       |            |          |          |          |
|          | astructure |            |          |          |          |
|          | Versions   |            |          |          |          |
|          | (A         |            |          |          |          |
|          | Bundles)   |            |          |          |          |
+==========+============+============+==========+==========+==========+
| [Host FW | 4.3(6)     |            |          |          |          |
| Versions |            |            |          |          |          |
| (B, C    |            |            |          |          |          |
| Bu       |            |            |          |          |          |
| ndles)]{ |            |            |          |          |          |
| .keyword |            |            |          |          |          |
| .kwd}    |            |            |          |          |          |
+----------+------------+------------+----------+----------+----------+
|          | 6300       | 6324       | 6400     | 6500     | UCSX-S9  |
|          |            |            |          |          | 108-100G |
+----------+------------+------------+----------+----------+----------+
|          | <t         |            |          |          |          |
|          | able class |            |          |          |          |
|          | ="olh_note |            |          |          |          |
|          | " data-bor |            |          |          |          |
|          | der="0" ro |            |          |          |          |
|          | le="note"> |            |          |          |          |
|          | <colgroup> |            |          |          |          |
|          | <col s     |            |          |          |          |
|          | tyle="widt |            |          |          |          |
|          | h: 50%" /> |            |          |          |          |
|          | <col s     |            |          |          |          |
|          | tyle="widt |            |          |          |          |
|          | h: 50%" /> |            |          |          |          |
|          | <          |            |          |          |          |
|          | /colgroup> |            |          |          |          |
|          | <tbody>    |            |          |          |          |
|          | <tr cl     |            |          |          |          |
|          | ass="odd"> |            |          |          |          |
|          | <          |            |          |          |          |
|          | td class=" |            |          |          |          |
|          | olh_note"  |            |          |          |          |
|          | width="1%" |            |          |          |          |
|          |  role="hea |            |          |          |          |
|          | ding" data |            |          |          |          |
|          | -border="0 |            |          |          |          |
|          | "><p><stro |            |          |          |          |
|          | ng>Note</s |            |          |          |          |
|          | trong></p> |            |          |          |          |
|          |  </td>     |            |          |          |          |
|          | <td        |            |          |          |          |
|          | class="olh |            |          |          |          |
|          | _note" dat |            |          |          |          |
|          | a-border=" |            |          |          |          |
|          | 0"><div cl |            |          |          |          |
|          | ass="note_ |            |          |          |          |
|          | _content"> |            |          |          |          |
|          | <p>Cisco U |            |          |          |          |
|          | CSX-S9108- |            |          |          |          |
|          | 100G suppo |            |          |          |          |
|          | rts only C |            |          |          |          |
|          | isco UCS X |            |          |          |          |
|          | -Series Se |            |          |          |          |
|          | rvers.</p> |            |          |          |          |
|          | <          |            |          |          |          |
|          | /div></td> |            |          |          |          |
|          | </tr>      |            |          |          |          |
|          | </tbody>   |            |          |          |          |
|          | </table>   |            |          |          |          |
+----------+------------+------------+----------+----------+----------+
| 4.3(6)   | Yes        | Yes        | Yes      | Yes      | Yes      |
+----------+------------+------------+----------+----------+----------+
| 4.3(5)   | Yes        | Yes        | Yes      | Yes      | Yes      |
+----------+------------+------------+----------+----------+----------+
| 4.3(4)   | Yes        | Yes        | Yes      | Yes      | Yes      |
+----------+------------+------------+----------+----------+----------+
| 4.3(3)   | Yes        | Yes        | Yes      | Yes      | No       |
+----------+------------+------------+----------+----------+----------+
| 4.3(2)   | Yes        | Yes        | Yes      | Yes      | No       |
+----------+------------+------------+----------+----------+----------+
| 4.2(3)   | Yes        | Yes        | Yes      | Yes      | No       |
+----------+------------+------------+----------+----------+----------+
| 4.2(2)   | Yes        | Yes        | Yes      | Yes      | No       |
+----------+------------+------------+----------+----------+----------+
| 4.2(1)   | Yes        | Yes        | Yes      | Yes      | No       |
+----------+------------+------------+----------+----------+----------+
| 4.1(3)   | Yes        | Yes        | Yes      | Yes      | No       |
+----------+------------+------------+----------+----------+----------+
| 4.1(2)   | Yes        | Yes        | Yes      | No       | No       |
+----------+------------+------------+----------+----------+----------+
| 4.1(1)   | Yes        | Yes        | Yes      | No       | No       |
+----------+------------+------------+----------+----------+----------+
| 4.0(1),  | No         | No         | No       | No       | No       |
| 4.0(4)   |            |            |          |          |          |
|          |            |            |          |          |          |
| (B, C    |            |            |          |          |          |
| Bundles) |            |            |          |          |          |
+----------+------------+------------+----------+----------+----------+

: [Table 4. ]{.table--title-label .tabletitle}[Mixed B, C Bundles
Supported on All Platforms with the 4.3(6)A Bundle]{.tabletitle}

+-----------------------------------+-----------------------------------+
| ![]                               | ::: {.note__content}              |
| (https://www.cisco.com/content/da |                                   |
| m/en/us/td/i/templates/note.gif)\ | -------------------------------   |
|                                   |                                   |
| **Important**                     | If you implement cross-version    |
|                                   | firmware, you must ensure that    |
|                                   | the configurations for the [Cisco |
|                                   | UCS domain]{.ph} are supported by |
|                                   | the firmware version on the       |
|                                   | server endpoints.                 |
|                                   |                                   |
|                                   | -------------------------------   |
|                                   | :::                               |
+-----------------------------------+-----------------------------------+
:::
:::
:::

Copyright © 2025, Cisco Systems, Inc. All rights reserved.

::: {.row .full .visitedlinks style="padding: 0px; margin:0px"}
::: {.col .full}
:::
:::
:::
:::

::: {.col .narrow-v2}
::: {.rightRailComponent .base-blowout}
::: {.eotPersonalization}
::: {#eotTDCampaign .section}
:::
:::

<div>

::: {.tac-image}
:::

</div>

::: {.hideComponent}
::: {.eot-authors}
:::
:::

::: {.eot-feedback-container}
::: {.eot-feedback}
### Was this Document Helpful?

Yes

No

[
[![Feedback](//www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png "Feedback"){#feedback_img}Feedback](javascript:%20void(0);){.eot-feedback-ol}
]{.eot-feedback-olwrap lang="en"}
:::
:::

::: {.showComponent}
::: {.eot-vav}
:::
:::

::: {.showComponent}
::: {.eotLetUsHelp}
### Contact Cisco

-   [Open a Support
    Case](https://mycase.cloudapps.cisco.com/start?prodDocUrl=){#eotLetUsHelpProdDocUrl}![login
    required](/etc/designs/cdc/fw/i/icon_lock_small.png)
-   (Requires a [Cisco Service
    Contract](//www.cisco.com/c/en/us/services/order-services.html))
:::
:::

::: {#eotRightRailMBox}
<div>

::: {.mboxDefault}
:::

</div>
:::

::: {.showComponent}
::: {.eot-tdatp}
### This Document Applies to These Products

-   [UCS
    Manager](/c/en/us/support/servers-unified-computing/ucs-manager/series.html)
:::
:::

::: {.showClass}
:::
:::
:::
:::
:::

::: {#fw-overlay}
:::

![](//cisco.112.2o7.net/b/ss/cisco-mobile/5/12345){width="2" height="2"}
