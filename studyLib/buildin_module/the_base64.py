#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64

__author__ = 'Mr.Huo'


def main():
    base64.test()
    s='你好'
    print(s.encode())
    print(s.encode().decode().encode(encoding='gbk'))
    print(s.encode().decode().encode(encoding='gbk').decode(encoding='gbk'))

if __name__ == '__main__':
    main()