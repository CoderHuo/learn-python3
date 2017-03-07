#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' regular expression
\d      匹配一个数字
\w      匹配一个字母或者数字
.       匹配任意字符
*       匹配任意个字符(包括0个)
+       匹配至少一个字符
?       匹配0个或者一个字符
{n}     匹配n个字符
{n,m}   匹配n-m个字符
\s      匹配一个空格
[]      范围匹配
^       开始
$       结束
'''
__author__ = 'Mr.Huo'

import re

def main():
    print(help(re))


if __name__ == '__main__':
    main()