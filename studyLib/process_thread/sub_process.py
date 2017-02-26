#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess,sys
__author__ = 'Mr.Huo'


def main():
    #运行命令行
    sub_p1 = subprocess.call(['nslookup', 'www.baidu.org'])
    sub_p2 = subprocess.call(['ping', 'www.baidu.org'])
    print('Exit code:', sub_p1,sub_p2)

    print('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    #中文系统解码gbk
    print(output.decode('gbk'))
    print('Exit code:', p.returncode)

if __name__ == '__main__':
    main()