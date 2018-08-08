##
##   ## ,------. ##########################
##   ## |  .---' ,--,--.,-----.,--. ,--. ##
##   ## |  `--, ' ,-.  |`-.  /  \  '  / ###
##   ## |  `---.\ '-'  | /  `-.  \   ' ####
##   ## `------' `--`--'`-----'.-'  / #####
##   ########### framework ### `---' ######
##
##     make your fuckin' dream come true
##
## written by @ CiKu370
##
## follow my social media
##
## telegram: @CiKu370
## facebook: https://facebook.com/putriy.kaeysha
## github: https://github.com/ciku370
##

version = 1.19

def check_update():
    from core.misc import printf
    import os
    import requests
    cek = requests.get('https://raw.githubusercontent.com/CiKu370/Eazy/master/Eazy.py')
    for i in cek.text:
         if 'version = ' in i:
             k = i[10:]
             if k != version:
                 printf('[+] updating..')
                 os.system('cd ~;rm -rf Eazy;git clone https://github.com/ciku370/Eazy')
                 break
def main():
    check_update()
    from core.shell import debby_anggraini as bintari
    bintari()

if __name__ == '__main__':
    main()
