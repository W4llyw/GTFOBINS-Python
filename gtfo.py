#!/usr/bin/env python3
# A Python script to Quickly search GTFOBin.github.io without having to leave your terminal

import requests
import argparse
from bs4 import BeautifulSoup
from colorama import Fore

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=(Fore.BLUE+'''\
                      Quickly check if escaping from a bin is possible
                     --------------------------------------------------
                        >>>>>>> Powered by GTFObin.github.io <<<<<<<'''),
    epilog=Fore.GREEN+"Example: gtfo.py -b  python -f \"sudo\"")

parser.add_argument('-b','--bin', required=True, help="This will tell you if you can escape the binary and your options.")
parser.add_argument('-f','--found', help="The discovered function for escaping the binary\"IN QUOTES\".")
args = parser.parse_args()

bin = args.bin
found = args.found

url = "https://gtfobins.github.io/"
r = requests.get(url)

search = url+"gtfobins/"+bin
results = requests.get(search)
text = results.text
soup = BeautifulSoup(text, 'html.parser')

#Test if possible and provides link and options
def binopt():
    if results.status_code == 200:
        options = soup.ul.get_text()
        print("You may be able to Escape check it out!")
        print(Fore.LIGHTCYAN_EX+search+"\n")
        print(Fore.RESET+"Functions for possible escape:"+"\n"+options)
        return options
    else:
        print(Fore.RED+"Oh no trapped forever :(")
        exit()

spl = binopt().split("\n")
olist = [l.lower().replace(" ","-") for l in spl] #Terrible List

#Output for specific function
if found != None and found.lower().replace(" ","-") in olist:
    spaces = found.lower().replace(" ","-")
    format = '/#'+spaces
    combo = search+format
    frequest = requests.get(combo).text
    fsoup = BeautifulSoup(frequest, 'html.parser')
    fid = fsoup.find(id=spaces)
    p = fid.find_next_sibling("p").text
    u = fid.find_next_sibling("ul").text

    print(Fore.GREEN+fid.get_text()+"\n")
    print(Fore.RESET+p,Fore.GREEN+"\n\nCode",Fore.LIGHTMAGENTA_EX+u)
elif found != None and found.lower().replace(" ","-") not in olist:
    print(Fore.LIGHTYELLOW_EX+"You cannot escape with this Function! ^^^Try one of these^^^")
else:
    exit()
