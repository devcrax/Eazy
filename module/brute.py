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
import requests
import sys
import json

# start brute force attack
def parse(web):
     if web.startswith('https://') or web.startswith('http://'):
          return web
     else:
          try:
               requests.get('https://' + web)
               return('https://' + web)
          except:
               return('http://' + web)
def start(web,path):
     for i in path:
        i = i.strip()
        r = requests.get(web+i)
        if r.status_code == 200:
            code = '\033[92m%s\033[0m'%r.status_code
        else:
            code = '\033[91m%s\033[0m'%r.status_code
        printf('%s [%s]'%(r.url,code))
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
