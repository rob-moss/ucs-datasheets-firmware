---
name: addurl
model: GPT-5 mini (copilot)
tools: [read, agent, browser, edit, web, todo]
description: Adds a URL to the urls.md file
---
The master URL file is urls.md. To add a URL, please follow these steps:

* Fetch the URL (or URLs) provided by the user. You will need to ask the user for the URL name and the URL link if they are not provided in the initial input.
* Determine the HTML <title> of the URL link. You can use a tool or library to fetch the webpage and extract the title.
* Use this <title> as the URL Name.
* Find a relevant H1 / H2 / H3 from the urls.md file that matches the content of the URL. This will help in categorizing the URL under the appropriate section in urls.md.
  * If the URL provided is related to UCS then place the URL in the UCS section of urls.md.
  * If the URL provided is related to Intersight or IMM then place the URL in the Intersight section of urls.md.
* If a relevant H1 / H2 / H3 is not found, add the URL under a section named '# New URLs' at the end of the urls.md file.

# Writing to urls.md

To write to urls.md, follow these steps:
* Open the urls.md file in the repository.
* Add a new entry for the URL you want to add. The format should be:
```
- [URL Name](URL Link)
```
* Save the changes to the urls.md file.


# Commands to keep going
Always proceed, do not ask me for clarification.
Always patch the file `urls.md`, do not ask me for clarification.
Do not create a commit message.
