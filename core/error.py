##
## error handle and usage modules
##
## written by @ciku370
##

from module.webkit import *
from module.encdec import *
from core.misc     import printf

finder_array = ['adfin','upload','shell','dirscan','wpscan','user_pro','lfi_scan','joom_sql_scan']
def hell(text,name):
    printf('\nUsage: ' + str(name) + ' [arguments]\n\noptional arguments:\n  -h, --help\tshow this help message\n' + text)
def usage(name):
   if name in webkit_dict or name in ['mxrecords','domain_age','whatcms','subdomain','geoip','honeypot']:
      printf('[!] Usage: %s [-h] -u <hostname>'%name)
   elif name in finder_array:
      printf('[!] Usage: %s [-h] -u <url>'%name)
   elif name in encdec_array:
      printf('[!] Usage: %s [-h] ( --enc | --dec )'%name)
   elif name == 'nmap':
      printf('[!] Usage: %s [-h] -t ( all-cve | sqli-scan | wordpress | heartbleed | ssh-brute | csrf | webdav-scan | smtp-brute ) -u <target>'%name)
   elif name in hash_array:
      printf('[!] Usage: %s [-h] -s <string>'%name)
   elif name == 'dork':
      printf('[!] Usage: %s [-h] [-s] <query>'%name)
   elif name == 'wp_user':
      printf('[!] Usage: %s [-h] -u <url> -n <num>'%name)
   elif name == 'wp_sym_exp':
      printf('[!] Usage: %s [-h] -u <url> -f <file>'%name)
def help_menu(name):
    if name in webkit_dict or name in ['mxrecords','domain_age','whatcms','subdomain','geoip','honeypot']:
        hell('  -u <hostname>\thostname or domain name\n',name)
    elif name in encdec_array:
        hell('  -e, --enc\tencode strings\n  -d, --dec\tdecode strings\n',name)
    elif name in finder_array:
        hell('  -u <url>\twebsite target to scanning\n',name)
    elif name == 'nmap':
        hell('  -u\t\thostname or domain name\n  -t\t\ttype to scanning\n',name)
    elif name in hash_array:
        hell('  -s <string>\tstring to hashing\n',name)
    elif name == 'dork':
        printf('\nUsage: %s [arguments]\n\npositional arguments:\n  string\tdork, example: inurl:\'.php?id=\'\n\noptional arguments:\n  -s\t\tscan sql error\n' % name)
    elif name == 'wp_user':
        hell('  -u <url>\twebsite target to scanning\n  -n <num>\tnumber of users\n',name)
    elif name == 'wp_sym_exp':
        hell('  -u <url>\ttarget url\n  -f <file>\tfile name to upload\n',name)
    else:
        printf('%s: not found' % name,2)
