#Passive Recon - WEB

-----------------------------------
## Target Validation
	* WHOIS, nslookup, dnsrecon

## Finding Subdomians
	* Google Fu, dig, Nmap(Active), Sublist3r, Bluto, crt.sh, etc.

## Fringerprinting
	* Nmap, Wappalyzer, WhatWeb, BuiltWith, Netcat

## Data Breach
	* HaveBeenPwned and Similar Lists

-----------------------------

### Sublist3r

> Install sublist3r from Github
> apt install sublit3r --> (In Kali)

`python sublist3r.py -d <target domain>`

-----------------------------

### crt.sh (Website)

> Website For Subdomaim Enumeration

`%.<target domain>.com`

-----------------------------

### SecurityHeader.io

> Show Security Header Required
>
> https://securityheaders.com

--------------------------------------

### Regex For BurpSuite Scope

>Changing the scope show Subdomains in Target List

`.*\.<target>\.com$`

----------------------------------------
