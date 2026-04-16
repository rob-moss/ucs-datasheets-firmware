# Rebuilding a Fabric Interconnect From Scratch - UMM & IMM - Tech Zone

## Objective

Provide a single, clear article explaining the step-by-step procedure to rebuild Fabric Interconnects 6400 series and ahead generations. 

## Prerequisites

- Console access to fabric interconnect
- Infrastructure bundle images containing required files according to the Managed Mode.

### For UMM 

- System .bin file 
- UCS Manager .bin file 

### For IMM 

- System .bin file

All files can be downloaded from: <https://cspg-releng.cisco.com/>

### Components Used

- TFTP server 
- Fabric Interconnect 6600 series

## Rebuild Steps

If you require to use USB, follow the deciated TZ article for USB port usage: [https://techzone.cisco.com/t5/B-Series/Rebuilding-64xx-from-scratch-using-the-builtin-USB-port/ta-p/...](https://techzone.cisco.com/t5/B-Series/Rebuilding-64xx-from-scratch-using-the-builtin-USB-port/ta-p/1324109)

Other related guides
[Recover 6400 FI](https://www.cisco.com/c/en/us/support/docs/servers-unified-computing/ucs-6400-series-fabric-interconnects/220718-troubleshoot-and-recover-6400-series-fab.html#toc-hId-1207758081)


1) Reboot Fabric Interconnect and interrumpt boot process to acces to the Loader. Press the key combination in the console as it boots: **Ctrl + C.**

_If it is a UCSX direct, you will need to use the combination of Ctrl + L and then Ctrl + C. The shell itself tells you. You have 10 seconds to make the combination._

2) Enable Recovey Mode.
At the loader prompt, enter:

```
loader > cmdline recoverymode=1     
```

3) Verify and Set IP Configuration.

```
loader > show ip                                                               
IP Addr: 10.1.1.136
Addr Mask: 255.255.255.0

loader > show gw                                                               
IP Default Gateway: 10.1.1.1
```

Set the IP address and gateway if needed.     
```
loader > set ip 10.31.123.110 255.255.255.0  
loader > set gw 10.31.123.1                                                    
Correct gateway addr 10.31.123.1
Address: 10.31.123.10
Netmask: 255.255.255.0
Server: 0.0.0.0
Gateway: 10.31.123.1
```


4) Boot system image via TFTP.

Nowadays we have system and ucsm files, not kickstart anymore. Use system image file to boot. 

```
loader > boot tftp://10.31.104.72/ucsfi.10.5.1.I60.2a.39.F.bin 
```
You should reach the prompt:

```
switch(boot)#
```

5) (Optional) Erase startup-config and initialize bootflash. 

You may try proceeding without this step first to see if the process works without performing a full initialization.

WARNING: Only perform this step if you intend to remove all files & configurations and rebuild the system from scratch. 

```
switch(boot)# init system
This command is going to erase your startup-config, licenses as well as the contents of your bootflash:
Do you want to continue? (y/n)
```

6) Configure network settings

```
switch(boot)# config terminal
switch(boot)(config)# interface mgmt 0
switch(boot)(config-if)# ip address 14.2.46.38 255.255.255.224
switch(boot)(config-if)# no shut
switch(boot)(config-if)# exit
switch(boot)(config)# ip default-gateway 14.2.46.33
```

Verify
```
switch(boot)# show ip
ip routing is disabled
Management Interface: ip address 10.31.123.110/24
ip default-gateway 10.31.123.1
```
7) Copy System and UCSM Binaries to Bootflash

For UCSM, copy both files. For IMM, copy system image file.

For reference: [https://techzone.cisco.com/t5/B-Series/Transfer-of-files-for-UCS-Devices-with-FTP-TFTP-SFTP-amp-SCP/...](https://techzone.cisco.com/t5/B-Series/Transfer-of-files-for-UCS-Devices-with-FTP-TFTP-SFTP-amp-SCP/ta-p/13857641#toc-hId-358849412)

  
Supported protocols: FTP, SCP, TFTP, SFTP. Example using TFTP:

```
copy tftp://14.2.43.184/ucsfi.10.5.1.I60.2a.39.F.bin bootflash:
copy tftp://10.31.104.72/ucs-manager-k9.6.0.2.250036.bin bootflash: <<< UCSM ONLY
```

Confirm files with:

```
switch(boot)# dir
4096Jan 18 2025 08:08:11  distributables/
4096Jan 18 2025 08:08:19  distributables_hdr/
4096Jan 18 2025 07:59:47  externalrep/
172Sep 10 2025 18:34:40  initial_setup.log
4096Sep 10 2025 18:29:54  installables/
4096Jan 18 2025 07:56:38  intersight-cache/
4096Jan 18 2025 07:59:51  intersightcache/
4096Jan 18 2025 08:00:47  license/
1073Sep 10 2025 18:30:08  log_profile.yaml
4096Jan 18 2025 08:08:54  lost+found/
 42Jan 18 2025 07:41:20  nuova-sim-mgmt-nsg.0.1.0.001.bin
4096Sep 10 2025 18:24:45  sw_trace_logs/
4096Sep 10 2025 17:56:02  sysdebug/
4096Jan 18 2025 07:51:49  techsupport/
 1022090872Sep 10 2025 23:21:12  ucs-manager-k9.6.0.2.250036.bin  <<<<
4096Jan 18 2025 07:35:47  ucs_chassis_imgs/
 1586619904Sep 10 2025 23:32:10  ucsfi.10.5.1.I60.2a.39.F.bin     <<<<
4096Dec 20 2024 20:28:32  ucsm-container/
```

**_SKIP TO STEP 10 IF YOU INTEND TO RECOVER THE FABRIC IN INTERSIGHT MANAGED MODE._**

8) (UCSM ONLY) At the boot prompt run "start" to drop into bash shell


```
switch(boot)# start 
bash-4.4#
```
9) (UCSM ONLY) Create Soft Link for UCS Manager Binary

```
bash-4.4# ln -sf /bootflash/ucs-manager-k9.6.0.2.250036.bin /bootflash/nuova-sim-mgmt-nsg.0.1.0.001.bin
bash-4.4# pwd
/bootflash
bash-4.4# ls -la
total 5115116
drwxrwxrwx 25 root  root                4096 Sep 10 23:38 .
drwxrwxr-t 58 root  network-admin       1860 Sep 10 23:33 ..
-rw-r--r--  1 root  root                  15 Sep 10 17:05 .disable-ssh
-rw-r--r--  1 root  root                 113 Jan 18  2025 .fips_mode_change.log
...
-rwxrwxrwx  1 root  root                1073 Sep 10 18:30 log_profile.yaml
drwxrwxrwx  2 root  root                4096 Jan 18  2025 lost+found
lrwxrwxrwx  1 root  root                  42 Sep 10 23:38 nuova-sim-mgmt-nsg.0.1.0.001.bin -> /bootflash/ucs-manager-k9.6.0.2.250036.bin    <<<<<<
-rw-rw-rw-  1 root  root                2664 Sep 10 18:41 obfl.dbg
-rw-rw-r--  1 admin network-admin          0 Jan 18  2025 platform-sdk.cmd
lrwxrwxrwx  1 root  root                  29 Sep 10 18:29 pnuos -> /bootflash/installables/pnuos
drwxrwxrwx  2 root  root                4096 Jan 18  2025 received
-rw-rw-rw-  1 root  root           990776957 Jan 18  2025 ucs-manager-k9.6.0.1.240021.bin
-rw-rw-rw-  1 root  root          1022090872 Sep 10 23:21 ucs-manager-k9.6.0.2.250036.bin               <<<<
drwxrwxrwx  2 root  root                4096 Jan 18  2025 ucs_chassis_imgs
-rw-rw-rw-  1 admin network-admin 1633111040 Jan 18  2025 ucsfi.10.5.1.I60.1a.103.F.bin     <<<<<
-rw-rw-rw-  1 root  root          1586619904 Sep 10 23:32 ucsfi.10.5.1.I60.2a.39.F.bin
drwxr-xr-x  6 root  floppy              4096 Dec 20  2024 ucsm-container
```

10) Reboot the Fabric Interconnect

```
bash-4.4# reboot
```
11) Boot from Bootflash Image.

The switch will reboot and come back up at the loader prompt; boot the system image from bootflash:

```
loader > boot bootflash:ucsfi.10.5.1.I60.2a.39.F.bin
Booting bootflash:ucsfi.10.5.1.I60.2a.39.F.bin
```
12) Initial UCS Configuration.

If you initialized the system, the UCS initial configuration prompt appears

```    
Enter the configuration method. (console/gui) ? console
...
```

13) Ensure Fabric Interconnect boots with system image.

To make Fabric Interconnect boots normally and not the loader prompt, you must install system binarie file into bootflash. 

_The alternative is to reflash or upgrade firmware version using auto-install option. But takes longer._

```    
FI-6662-A# connect nxos
FI-6662-A(nx-os)# run cid
daviher3#vsh
root@F241-04-09-FI-6454-B(nx-os)# conf t
root@F241-04-09-FI-6454-B(nx-os)# install all nxos bootflash:ucsfi.10.5.1.I60.2a.39.F.bin
```
This document provides a clear, step-by-step guide to rebuild Cisco Fabric Interconnect 6400 series and later, covering both UMM and IMM modes, including network configuration, image loading, and boot procedures.

Based in previous documents: 

\+ <https://techzone.cisco.com/t5/B-Series/Rebuilding-a-fabric-interconnect-from-scratch/ta-p/705829>

\+ [https://techzone.cisco.com/t5/B-Series/Rebuilding-64xx-from-scratch-using-the-builtin-USB-port/ta-p/...](https://techzone.cisco.com/t5/B-Series/Rebuilding-64xx-from-scratch-using-the-builtin-USB-port/ta-p/1324109)

\+ [https://www.cisco.com/c/en/us/support/docs/servers-unified-computing/ucs-6400-series-fabric-intercon...](https://www.cisco.com/c/en/us/support/docs/servers-unified-computing/ucs-6400-series-fabric-interconnects/220718-troubleshoot-and-recover-6400-series-fab.html)
