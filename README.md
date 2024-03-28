# GTFOBINS-Python
A Python script to Quickly search GTFOBin.github.io without having to leave your terminal!

# Installation
Clone this repository.
```
git clone https://github.com/W4llyw/GTFOBINS-Python.git
```

From within the GTFOBINS-Python directory first install the requirements.
```
pip install -r requirements.txt
```

# How to use
```
python3 gtfo.py -b  python -f "sudo"
```
## Options
**-b** This option will tell you if you can escape the binary and the possible functions you can use for escaping.
```
python3 gtfo.py -b python
```
*Output:*
```
You may be able to Escape check it out!
https://gtfobins.github.io/gtfobins/python

Functions for possible escape:

Shell
Reverse shell
File upload
File download
File write
File read
Library load
SUID
Sudo
Capabilities
```

**-f** Once you have found a function that may allow you to escape from a specific binary, you can use the -f option with the discovered function in **"QUOTES"**.
```
python3 GTFO-V3.py -b python -f "SUID"
```
This will output the binary's options followed by the function you specified with an explaination and the Code for a possible escape.

*Output:*
```
You may be able to Escape check it out!
https://gtfobins.github.io/gtfobins/python

Functions for possible escape:

Shell
Reverse shell
File upload
File download
File write
File read
Library load
SUID
Sudo
Capabilities

SUID

If the binary has the SUID bit set, it does not drop the elevated privileges and may be abused to access the file system, escalate or maintain privileged access as a SUID backdoor. If it is used to run sh -p, omit the -p argument on systems like Debian (<= Stretch) that allow the default sh shell to run with SUID privileges. 

Code 

sudo install -m =xs $(which python) .

./python -c 'import os; os.execl("/bin/sh", "sh", "-p")'
```
