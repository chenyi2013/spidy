
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
 
page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    # print response.read()
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason

content = response.read().decode('utf-8')
pattern = re.compile('<div.*?article\sblock\suntagged\smb15.*?>.*?<div.*?author\sclearfix.*?>.*?<a.*?>.*?<img.*?>.*?</a>.*?<a.*?>.*?<h2>'
+'(.*?)</h2>.*?</a>.*?<div.*?>(.*?)</div>.*?<a.*?>.*?<div .*?content.*?>.*?<span>(.*?)</span>.*?</div>.*?</a>.*?<i.*?number.*?>(.*?)</i>.*?<i.*?number.*?>(.*?)</i>',re.S)
items = re.findall(pattern,content)
for item in items:
    print 'author: '+item[0]
    print 'age: '+ item[1]
    print 'content: '+item[2]
    print 'smile: '+item[3]
    print 'comment: '+item[4]