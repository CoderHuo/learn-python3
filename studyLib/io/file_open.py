#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

def main():
    # file 打开失败会有异常，用try ... finally 始终关闭文件
    try:
        file_op = open('file_open.py', encoding='UTF-8')
        print(file_op.read())
    except Exception as err:
        print(err)
    finally:
        if file_op:
            file_op.close()

    # 还有一种方式 with ...  as,自动调用close()方法
    # read() 读取全部内容，读小文件可以，读取大文件使用read(size)
    # readline() 读取一行内容
    # readlines()一次读取所有内容并按行返回list
    with open('file_open.py', encoding='UTF-8') as file_op:
        print(file_op.read())

    with open('file_open.py', encoding='UTF-8') as file_op:
        for line in file_op.readlines():
            print(line, end="")
    print(end="\n")


if __name__ == '__main__':
    main()