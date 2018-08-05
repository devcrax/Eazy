##
## main program
##
## written by @ciku370
##

# import modules
import os
from core.parse     import toxic
from core.banner    import banner
from core.misc      import *
from core.complete  import *
from module.webkit  import *
from module.brute   import *
from module.encdec  import *
from module.scanner import *
from module.wp_user import user_scan
from module.userpro import check_vuln
from module.nmap    import bintari as debby_lovlov
from core.error     import *

# shell script
def debby_anggraini():
    # banner and auto complete
    banner()
    complete(array)
    # loop forever :v
    while True:
        try:
            an = raw_input('\033[94mEazy \033[0m>> ')
            wibu = an.split()
            # parse argument manual XD
            arg = toxic(wibu,'-u,-t,-s,-n')
            # if an == '' or len(wibu) == 0:
            if not wibu:
                pass
            # help menu
            elif wibu[0] != '-h' and '-h' in wibu or wibu[0] != '--help' and '--help' in wibu:
                help_menu(wibu[0])
            # advanced nmap commands
            elif wibu[0] == 'nmap':
		debby_lovlov(arg['-t'],arg['-u'])
	    # webkit modules
	    elif wibu[0] in webkit_dict:
                # dirty hack XD
                for i in webkit_dict:
                     if wibu[0] == i:
                          hackertarget(webkit_dict[i],arg['-u'])
            elif wibu[0] == 'geoip':
                geoip(arg['-u'])
            elif wibu[0] == 'mxrecords':
                mx(arg['-u'])
            elif wibu[0] == 'domain_age':
                domage(arg['-u'])
            elif wibu[0] == 'whatcms':
                cms(arg['-u'])
            elif wibu[0] == 'subdomain':
                subdo(arg['-u'])
            elif wibu[0] == 'honeypot':
                honey(arg['-u'])
	    elif wibu[0] == 'wpscan':
                wpscan(arg['-u'])
            elif wibu[0] == 'user_pro':
                check_vuln(arg['-u'])
            elif wibu[0] == 'wp_user':
                user_scan(arg['-u'],arg['-n'])
            # scanner module
            elif wibu[0] == 'hashbuster':
                hash_scan()
            elif wibu[0] == 'shell':
                shell(arg['-u'])
            elif wibu[0] == 'dirscan': # dir
                dir(arg['-u'])
	    elif wibu[0] == 'dork' and wibu[1] != None:
                msg = an.replace(wibu[0] + ' ','').replace('-s ','').replace('-s','')
                if not msg:
                    usage('dork')
		elif '-s' in an:
                    dorking(msg,'scan')
                else:
                    dorking(msg)
            # brute force module
            elif wibu[0] == 'adfin':
                adfin(arg['-u'])
            elif wibu[0] == 'upload':
                upload(arg['-u'])
            # encryption modules
            elif wibu[0] in encdec_array:
                # bad coding :"
                if '--enc' in wibu or '-e' in wibu:
                     ende(wibu[0],'enc')
                elif '--dec' in wibu or '-d' in wibu:
                     ende(wibu[0],'dec')
                else:
                     usage(wibu[0])
            elif wibu[0] in hash_array:
	        hash(wibu[0],arg['-s'])
            # others
	    elif wibu[0] == ':!':
		 if len(wibu) == 1:
		     printf('sh: commands not found',2)
                 os.system(an[2:])
            elif wibu[0] in ['q','quit']:
                printf('bye bye..')
                break
            elif an == 'show modules' or an == 'help':
                show_modules()
	    elif an == 'show all modules' or an == 'help more':
	        show_modules('wibu bau bawang')
            else:
                printf('%s: not found.'%wibu[0],2)
            # end
        # usage
        except (IndexError,KeyError):
            usage(wibu[0])
        # user interrupt
        except KeyboardInterrupt:
            printf('\n\rError: Interrupt..')
        # handle error
        except (requests.exceptions.ConnectionError):
            printf('Connection Error..',2)
        except Exception as e:
            printf(str(e),2)
# EOF
