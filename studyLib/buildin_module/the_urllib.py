#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request
import re, chardet
import gzip,zlib
from io import BytesIO,StringIO

__author__ = 'Mr.Huo'

headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
}


def main():
    with request.urlopen('https://api.douban.com/v2/book/2129650') as rsp_1:
        data = rsp_1.read()
        print('status.', rsp_1.status, rsp_1.reason)
        for k, v in rsp_1.getheaders():
            print('%s:%s' % (k, v))
        print('Data:', data.decode('utf-8'))

    req_1 = request.Request('http://www.baidu.com/', headers=headers)
    print(req_1.headers)
    with request.urlopen(req_1) as rsp_1:
        data = rsp_1.read()
        print('status.', rsp_1.status, rsp_1.reason)
        for k, v in rsp_1.getheaders():
            print('%s:%s' % (k, v))
        # 从响应头中获取网页编码格式
        try:
            charset = re.match(r'(.*charset=)(.*)', rsp_1.getheader('Content-Type')).group(2)
            print(charset)
            print('Data:', data.decode(encoding=charset, errors='ignore'))
        except Exception as e:
            print(e)
        # print(data)
        # 用chardet 获取编码方式
        charset = chardet.detect(data)['encoding']
        if charset != None:
            print('Data:', data.decode(encoding=charset, errors='ignore'))
        encoding = rsp_1.getheader('Content-Encoding')
        if encoding in ['gzip','deflate']:
            if encoding == 'gzip':
                data = gzip.GzipFile(fileobj=BytesIO(data)).read()
            if encoding == 'deflate':
                data = zlib.decompress(data)
            print(data.decode(encoding='utf-8', errors='ignore'))
if __name__ == '__main__':
    main()
