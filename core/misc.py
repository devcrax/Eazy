##
## function modules
##
## written by @ciku370
##

def printf(msg,code = 0):
    msg = msg.replace('?*','\033[95;1m*\033[0m').replace('?-','\033[94;1m-\033[0m').replace('?=>','\033[94;1m=>\033[0m').replace('{0}','\033[91m').replace('{1}','\033[0m')
    if code == 0:
        print('\033[0m%s\033[0m'%msg)
    elif code == 1:
        print("\033[0m[\033[92m%s\033[0m] %s"%(u(" %T "),msg))
    elif code == 2:
        print("\033[0mError: %s"%msg)

def show_modules(t = None):
    if t == None or t == 'wibu bau bawang':
          printf("""{0}
 web scanner       description{1}
 -----------       -----------
 dork              dork scanner.
 traceroute        traceroute using MRT.
 nping             test ping/Nping.
 dns_lookup        dns lookup.
 reverse_dns       reverse dns lookup.
 host_search       find dns host records.
 shared_dns        find shared dns servers.
 zone_test         zone transfer test.
 whois             whois lookup.
 geoip             Ip location lookup.
 reverse_ip        reverse ip lookup.
 port              tcp port scan.
 subnet            subnet lookup.
 http_headers      http headers check.
 pagelinks         extract page link from page.
 mxrecords         find mx records.
 domain_age        domain age checker.
 whatcms           Check Content Management System (CMS).
 subdomain         subdomain scanner using AXFR technique.
 honeypot          honeypot detector.
 wpscan            wordpress plugins scanners.
 nmap              advanced nmap.
 user_pro          wordpress userpro vulnerability scanner.
 dirscan           directory scanner.
 shell             scan available shell on websites.
 hashbuster        online hash scanner/decrypter.
 adfin             search admin pages.
 upload            search upload pages.
 wp_user           Wordpress users enumerate
                   bypass to get the website users.
""")
    if t == 'wibu bau bawang':
          printf("""{0} encryption        description{1}
 ----------        -----------
 base16            base16 encryption.
 base32            base32 encryption.
 base64            base64 encryption.
 bin               binnary.
 decimal           decimal.
 hex               hexadecimal.
 rev               reverse strings.
 rot13             ROT 13 cipher.
 {0}
 hash              description{1}
 ----              -----------
 md4               md4 hashing.
 md5               md5 hashing.
 sha1              sha1 hashing.
 sha224            sha224 hashing.
 sha256            sha256 hashing.
 sha384            sha384 hashing.
 sha512            sha512 hashing.
 ripemd160         ripemd160 hashing.
 whirlpool         whirlpool hashing.
""")
