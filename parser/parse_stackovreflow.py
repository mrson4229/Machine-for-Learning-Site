import urllib.request, json, sys, os
from bs4 import BeautifulSoup

url = 'http://stackoverflow.com/search?q=%s' % (keyword)
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}
r = urllib.request.Request(url, headers=headers)
p = urllib.request.urlopen(r)
soup = BeautifulSoup(p.read(), 'html.parser')
