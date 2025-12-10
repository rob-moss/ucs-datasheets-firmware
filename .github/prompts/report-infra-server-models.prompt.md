---
agent: agent
---
The purpose of this prompt is to generate a report on the recommended firmware versions for Cisco UCS Manager based on the data processed from the firmware datasheets.

# Firmware Recommendation Report for Cisco UCS Manager
Begin with the Recommended firmware versions for Infrastructure section.
Then list the recommended firmware versions for Cisco UCS Servers - Blades and Rack Servers

Read the data from the following files:
- ucs-firmware-reports/recommended-firmware.md


# Actions to take
1. Read the ucs-firmware-reports/ucs-crossfirmware-4.3.md file to extract all of the Infrastrucrture Firmware versions that match the Recommended firmware versions for Infrastrcture
2. Read the ucs-firmware-reports/server-adapter-driver-matrix-raw.md file to extract all of the Blade Firmware versions that match the Recommended firmware versions for Cisco UCS Blades
3. Match the Recommended firmware version ie 4.3(6c) with the main version ie 4.3(6) to find all matching firmware versions
4. List all of the B and C Server Bundle Versions that match the Recommended firmware version for Cisco UCS Blades


# Output

Write to the output file: ucs-firmware-reports/report-recommended-firmware.md





### Infrastructure Firmware Recommendations
Create a matrix as follows for all of the Recommended firmware versions for Infrastructure.

An example of the matrix is below:

| Recommended Version | Infrastructure Bundle |	B and C Server Bundle Versions |
| --------------------- | --------------------- | ------------------------------ |
| 4.3(6c)               | 4.3(6c)             | 4.3(6), 4.3(5), 4.3(4), 4.3(3), 4.3(2), 4.2(3), 4.2(2), 4.2(1), 4.1(3), 4.1(2), 4.1(1) |


