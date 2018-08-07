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
    printf('\nUsage: ' + str(name) + ' [arguments]\n\noptional arguments:\n  -h, --help\t\tshow this help message\n' + text)
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
        hell('  -u <hostname>\t\thostname or domain name',name)
    elif name in encdec_array:
        hell('  -e, --enc\t\tencode strings\n  -d, --dec\t\tdecode strings',name)
    elif name in finder_array:
        hell('  -u <url>\t\twebsite target to scanning',name)
    elif name == 'nmap':
        hell('  -u\t\t\thostname or domain name\n  -t\t\t\ttype to scanning',name)
    elif name in hash_array:
        hell('  -s <string>\t\tstring to hashing',name)
    elif name == 'dork':
        printf('\nUsage: %s [arguments]\n\npositional arguments:\n  string\t\tdork, example: inurl:\'.php?id=\'\n\noptional arguments:\n  -s\t\t\tscan sql error' % name)
    elif name == 'wp_user':
        hell('  -u <url>\t\twebsite target to scanning\n  -n <num>\t\tnumber of users',name)
    elif name == 'wp_sym_exp':
        hell('  -u <url>\t\ttarget url\n  -f <file>\t\tfile name to upload',name)
    else:
        printf('%s: not found' % name,2)
