#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
__author__ = 'Mr.Huo'


# 读写文件前，我们先必须了解一下，在磁盘上读写文件的功能都是由操作系统提供的，
# 现代操作系统不允许普通的程序直接操作磁盘，所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），
# 然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）。
# r
# 以读方式打开文件，可读取文件信息。
# w
# 以写方式打开文件，可向文件写入信息。如文件存在，则清空该文件，再写入新内容
# a
# 以追加模式打开文件（即一打开文件，文件指针自动移到文件末尾），如果文件不存在则创建
# r+
# 以读写方式打开文件，可对文件进行读和写操作。
# w+
# 消除文件内容，然后以读写方式打开文件。
# a+
# 以读写方式打开文件，并把文件指针移到文件尾。
# b
# 以二进制模式打开文件，而不是以文本模式。该模式只对Windows或Dos有效，类Unix的文件是用二进制模式进行操作的。

def print_line(var):
    var_list = list(var)
    for i in range(len(var_list)):
        print(var_list[i])

def main():
    base_fail_file = 'C:\\shaohua.huo\\work\\hv84442\\testresult\\base_fail.txt'
    tr_fail_file = 'C:\\shaohua.huo\\work\\hv84442\\testresult\\tr_fail.txt'
    base_fail = []
    tr_fail = []
    testsuit = set()
    with open(base_fail_file, encoding='UTF-8') as file_op:
        for line in file_op.readlines():
            line = line.replace('\n', '')
            base_fail.append(line)
    with open(tr_fail_file, encoding='UTF-8') as file_op:
        for line in file_op.readlines():
            line = line.replace('\n', '')
            tr_fail.append(line)
    print(len(tr_fail))
    print('--------------------')

    for v in base_fail:
        if v in tr_fail:
            print(v)
            tr_fail.remove(v)
        else:
            print('base fail',v)

    print('--------------------')
    print("Just tr fail")
    for i in range(len(tr_fail)):
        print(tr_fail[i])
        test = tr_fail[i].split('.')[0]
        testsuit.add(test)

    print("Testsuit of tr fail")
    print_line(testsuit)

if __name__ == '__main__':
    main()
