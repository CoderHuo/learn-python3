#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from io import StringIO, BytesIO

__author__ = 'Mr.Huo'


def main():
    # 内存中读写字符串
    strio = StringIO()
    strio.write('hello world\nhello world\nhello world\n')
    print(strio.getvalue())

    strio1 = StringIO('hello world\nhello world\nhello world\n')
    while True:
        s = strio1.readline()
        if s == '':
            break
        print(s, end='')
    #内存中读写二进制
    byteio = BytesIO()
    byteio.write('中华'.encode("utf-8"))
    print(byteio.getvalue())

    byteio = BytesIO('中华'.encode("utf-8"))
    print(byteio.read())


if __name__ == '__main__':
    main()
