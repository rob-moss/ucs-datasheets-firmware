# How to recover the UCS FI bootloader firmware


Customer Action Plan
==================
Enable Recovery Mode:
```
loader > cmdline recoverymode=1
```

2.       Verify and Set IP Configuration .
```
loader > show ip                                                               
IP Addr: a.b.c.d
Addr Mask: 255.255.255.x

loader > show gw                                                               
IP Default Gateway: x.y.z.v
 
Set the IP address and GW if needed (choose your preferred IP addressing, the below details are from my lab):
 
loader > set ip 10.31.123.110 255.255.255.0 
loader > set gw 10.31.123.1                                                   
Correct gateway addr 10.31.123.1
Address: 10.31.123.10
Netmask: 255.255.255.0
Server: 0.0.0.0
Gateway: 10.31.123.1
```
3.       Boot system image (example command as below)
```
loader > boot tftp://10.31.104.72/ucsfi.10.5.1.I60.2a.39.F.bin 
```

You should reach the prompt:
```switch(boot)#```
 
4.       Copy system image to bootflash 
```
copy tftp://14.2.43.184/ucsfi.10.5.1.I60.2a.39.F.bin bootflash:
```
5.       Confirms the file with:
```switch(boot)# dir ```
 
6.       Boot the bootflash image. The switch will reboot and come back up at the loader prompt; boot the system image from bootflash:
```
loader > boot bootflash:ucsfi.10.5.1.I60.2a.39.F.bin
Booting bootflash:ucsfi.10.5.1.I60.2a.39.F.bin
```

7.       Initial UCS Configuration. If you initialized the system, the UCS initial configuration prompt appears
```
Enter the configuration method. (console/gui) ? console
...
```

