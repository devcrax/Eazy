##
## brute force modules
##
## credit to = {
##     https://github.com/cvar1984/spyder
##     https://github.com/blackholesecurity/leet1998
## }
##

from core.misc import printf
from time      import strftime as u
import re
import requests
import sys
import json

# start brute force attack
def parse(web):
     if 'http' not in web:
         try:
             requests.get('https://' + web)
             return('https://' + web)
         except:
             return('http://' + web)
     else:
         return web
def start(web,path):
    printf('[+] wait a minute, scanning (%s)' % web)
    for i in path:
        i = i.strip()
        r = requests.get(web+i)
        if r.status_code == 200:
            printf(' %s' % (web + i))
# admin panel finder
def adfin(web):
     path = open('core/wordlist/admin.txt','r').readlines()
     start(parse(web) + '/',path)
# upload pages finder
def upload(web):
     path = open('core/wordlist/upload.txt','r').readlines()
     start(parse(web) + '/',path)
# shell scanner
def shell(web):
     path = open('core/wordlist/shells','r').readlines()
     start(parse(web) + '/',path)
# dirscan
def dir(web):
     path = open('core/wordlist/dir','r').readlines()
     start(parse(web) + '/',path)
# wordpress scanner
def wpscan(web):
    path = open('core/wordlist/plugins.txt','r').readlines()
    start(parse(web) + '/wp-content/plugins/',path)
def lfiscan(web):
    url = parse(web)
    printf('[+] wait a minute, scanning (%s)' % url)
    lfis = open('core/wordlist/lfi.txt','r').readlines()
    for lfi in lfis:
        check = requests.get(url + lfi.strip()).text
        if re.findall("root:x", check):
            printf(' %s' % web + lfi.strip())
            break
