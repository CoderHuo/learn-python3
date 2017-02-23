#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pdb
__author__ = 'Mr.Huo'

#启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态
#以参数-m pdb启动后，pdb定位到下一步要执行的代码-> s = '0'。
# 输入命令l来查看代码
#输入命令n可以单步执行代码
#任何时候都可以输入命令p 变量名来查看变量
#输入命令q结束调试，退出程序
def main():
    s = '0'
    n = int(s)
    #设置一个断点， P 查看变量，c继续执行
    pdb.set_trace()
    print(10/n)


if __name__ == '__main__':
    main()