# encoding:UTF-8
from urllib import request, parse
import re, urllib

baseurl = 'https://www.baidu.com/img/wanshengdoodle_677234cad70a5974a64e4665c6485c71.gif'
headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)'
}

try:
    req = urllib.request.Request(baseurl, headers=headers)
    urlop = urllib.request.urlopen(req, timeout=5)
except Exception as err:
    print('1', err)

# 避免程序异常中止, 用try..catch处理异常
filename = "c:\\shaohua.huo\\aaa.gif"
try:
    data = urlop.read()
    with open(filename, mode='wb') as save_file:
        save_file.write(data)
except Exception as err:
    print('2', err)
