#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

__author__ = 'Mr.Huo'


def main():
    '''导入包路径为默认的sys.path'''
    for x in sys.path:
        print(x)


# 如果我们要添加自己的搜索目录，有两种方法
# 一是直接修改sys.path，添加要搜索的目录 sys.append('XXX'),这种方法是在运行时修改，运行结束后失效
# 第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中


if __name__ == '__main__':
    main()
