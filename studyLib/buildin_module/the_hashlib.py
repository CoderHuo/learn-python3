#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
__author__ = 'Mr.Huo'


def main():
    s1 = '霍少华'
    md5 = hashlib.md5()
    md5.update(s1.encode(encoding='utf-8'))
    print(md5.hexdigest())
    pass


if __name__ == '__main__':
    main()