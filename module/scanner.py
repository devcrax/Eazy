##
## scanner modules
##
## Credit to (https://github.com/s0md3v/Hash-Buster/blob/master/hash.py)
##

from core.misc import printf
from re        import search
from bs4       import BeautifulSoup
import cookielib
import random
import urllib2
import re
import requests

errors = {'MySQL': 'error in your SQL syntax',
             'MiscError': 'mysql_fetch',
             'MiscError2': 'num_rows',
             'Oracle': 'ORA-01756',
             'JDBC_CFM': 'Error Executing Database Query',
             'JDBC_CFM2': 'SQLServer JDBC Driver',
             'MSSQL_OLEdb': 'Microsoft OLE DB Provider for SQL Server',
             'MSSQL_Uqm': 'Unclosed quotation mark',
             'MS-Access_ODBC': 'ODBC Microsoft Access Driver',
             'MS-Access_JETdb': 'Microsoft JET Database',
             'Error Occurred While Processing Request' : 'Error Occurred While Processing Request',
             'Server Error' : 'Server Error',
             'Microsoft OLE DB Provider for ODBC Drivers error' : 'Microsoft OLE DB Provider for ODBC Drivers error',
             'Invalid Querystring' : 'Invalid Querystring',
             'OLE DB Provider for ODBC' : 'OLE DB Provider for ODBC',
             'VBScript Runtime' : 'VBScript Runtime',
             'ADODB.Field' : 'ADODB.Field',
             'BOF or EOF' : 'BOF or EOF',
             'ADODB.Command' : 'ADODB.Command',
             'JET Database' : 'JET Database',
             'mysql_fetch_array()' : 'mysql_fetch_array()',
             'Syntax error' : 'Syntax error',
             'mysql_numrows()' : 'mysql_numrows()',
             'GetArray()' : 'GetArray()',
             'FetchRow()' : 'FetchRow()',
             'Input string was not in a correct format' : 'Input string was not in a correct format',
             'Not found' : 'Not found'}

def hash_scan():
     hash = raw_input('\033[93m[?]\033[0m Enter hash: ')
     if hash == None and len(hash) not in [32,40,64,96]:
        printf('[!] Invalid hash',2)
     response = requests.get('https://lea.kz/api/hash/' + hash).text
     match = search(r': "(.*?)"', response)
     if match:
         printf('[+] hashed string: ' + match.group(1))
     else:
         data = {'md5' : hash, 'x' : '21', 'y' : '8'}
         response = requests.post('http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php', data).text
         match = search(r'<span class=\'middle_title\'>Hashed string</span>: [^<]*</div>', response)
         if match:
             printf('[+] hashed string: ' + match.group(1))
         else:
             if len(hash) == 32:
                 response = requests.get('http://www.nitrxgen.net/md5db/' + hash).text
                 if len(response) > 0:
                     printf('[+] hashed string: ' + response)
                 else:
                     r = requests.get('https://hashtoolkit.com/reverse-md5-hash/'+hash)
                     match = search(r'<span title="decrypted md5 hash">(.*?)</span>',r.text)
                     if match:
                         printf('[+] hashed string: ' + match.group(1))
                     else:
                         r = requests.get('https://md5.gromweb.com/?md5='+hash)
                         match = search(r'<em class="long-content string">(.*?)</em></p>',r.text)
                         if match:
                             printf('[+] hashed string: ' + match.group(1))
                         else:
                             printf('[!] string not found')
             elif len(hash) == 40:
                 data = {'auth':'8272hgt', 'hash':hash, 'string':'','Submit':'Submit'}
                 response = requests.post('http://hashcrack.com/index.php' , data).text
                 match = search(r'<span class=hervorheb2>(.*?)</span></div></TD>', response)
                 if match:
                     printf('[+] hashed string: ' + match.group(1))
                 else:
                     r = requests.post('https://sha1.gromweb.com/?hash='+hash)
                     match = search(r'<em class="long-content string">(.*?)</em></p>',r.text)
                     if match:
                         printf('[+] hashed string: ' +  match.group(1))
                     else:
                         printf('[!] string not found')
             elif len(hash) == 64:
                 response = requests.get('http://md5decrypt.net/Api/api.php?hash=%s&hash_type=sha256&email=deanna_abshire@proxymail.eu&code=1152464b80a61728' % hash).text
                 if len(response) != 0:
                     printf('[+] hashed string: ' + response)
                 else:
		     r = requests.get('https://hashtoolkit.com/reverse-sha256-hash/' + hash)
		     match = search(r'<span title="decrypted sha256 hash">(.*?)</span>',r.text)
		     if match:
			 printf('[+] hashed string: ' + match.group(1))
		     else:
                         printf('[!] string not found')
	     elif len(hash) == 96:
                 r = requests.get('http://hashtoolkit.com/decrypt-sha384-hash/' + hash)
		 match = search(r'<span title="decrypted sha384 hash">(.*?)</span>',r.text)
                 if match:
		     printf('[+] hashed string:' + match.group(1))
                 else:
                     printf('[!] string not found')
             else:
                printf('[!] hash not supported')
def dorking(string , sqlscan = None):
    debby = 0
    urls = []
    printf('[+] Searching..')
    for i in range(1,3):
        payload = { 'q' : string , 'start' : i }
        headers = { 'User-agent' : 'Mozilla/11.0' }
        req = requests.get( 'http://www.google.com/search',payload, headers = headers )
        soup = BeautifulSoup( req.text, 'html.parser' )
        h3tags = soup.find_all( 'h3', class_='r' )
        for h3 in h3tags:
            try:
                urls.append(re.search('url\?q=(.+?)\&sa', h3.a['href']).group(1).replace('%3F','?').replace('%3D','='))
            except:
                continue
        payload = { 'q' : string , 'first' : i }
        headers = { 'User-agent' : 'Mozilla/11.0' }
        req = requests.get( 'https://www.bing.com/search',payload,headers = headers )
        soup = BeautifulSoup( req.text, 'html.parser' )
        h3tags = soup.find_all( 'li', class_='b_algo' )
        for h3 in h3tags:
            try:
                urls.append(h3.find('a').attrs['href'].replace('%3F','?').replace('%3D','='))
            except:
                continue
    if len(urls) == 0:
        printf('[!] no url found',2)
    elif sqlscan == None:
        for i in urls:
            printf(' %s' % i)
    else:
        for url in urls:
            if '=' in url or '?' in url:
                source = requests.get(url + "'").text
                for type,eMSG in errors.items():
                    if re.search(eMSG, source):
                        printf(' %s [\033[92m%s\033[0m]' % (url,type))
                        debby += 1
        if debby == 0:
            printf('[!] no url found',2)
