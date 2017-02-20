# encoding:UTF-8
from urllib import request, parse
import re, urllib
from collections import deque


def fetch(url):
    webPage = request.urlopen(baseurl)
    webPage.geturl()
    data = webPage.read()
    data = data.decode('utf-8')
    href = []
    href = re.compile(r'href=\"(.+?)\"').findall(data)
    return href


queue = deque()
visited = set()
baseurl = 'http://news.baidu.com'
headers = {'Connection': 'Keep-Alive',
           'Accept': 'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, */*',
           'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
           'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)'}
queue.append(baseurl)
cnt = 0

# href = fetch(baseurl)

# print(type(href))

# for i in range(0, len(href)):
#    print(href[i])
while queue:
    url = queue.popleft()  # 队首元素出队
    visited |= {url}  # 标记为已访问

    print('已经抓取: ' + str(cnt) + '   正在抓取 <---  ' + url)
    cnt += 1
    print(url)
    url = parse.quote(url, ':/?;@&=+$#,')
    print(url)
    try:
        req = urllib.request.Request(url, headers=headers)
        urlop = urllib.request.urlopen(req, timeout=5)
    except:
        continue
    # print(urlop.getheader('Content-Type'))
    if 'html' not in urlop.getheader('Content-Type'):
        continue

    # 避免程序异常中止, 用try..catch处理异常
    try:
        data = urlop.read().decode('utf-8', 'ignore')
    except:
        continue

    # 正则表达式提取页面中所有队列, 并判断是否已经访问过, 然后加入待爬队列
    linkre = re.compile('href=\"(.+?)\"')
    for x in linkre.findall(data):
        if ('http' in x) and (x not in visited) and ('py' not in x) and ('js' not in x) and ('css' not in x):
            queue.append(x)
            print('加入队列 --->  ' + x)

print(visited)
