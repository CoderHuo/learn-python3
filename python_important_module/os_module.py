#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
from os.path import join, getsize

__author__ = 'Mr.Huo'


def main():
    '''
    :return:
    '''
    print(help(os))
    print("==========")
    print(os.listdir("c:/shaohua.huo/1"))
    print(os.times())
    print(dir(os))
    for root, dirs, files in os.walk("c:/shaohua.huo/1"):
        print(root, "consumes")
        print(sum([getsize(join(root, name)) for name in files]), end="")
        print("bytes in", len(files), "non-directory files")
        if 'CVS' in dirs:
            dirs.remove('CVS')  # don't visit CVS directories
    pass


if __name__ == '__main__':
    main()
