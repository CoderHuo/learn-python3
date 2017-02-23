#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Mr.Huo'


# 读写文件前，我们先必须了解一下，在磁盘上读写文件的功能都是由操作系统提供的，
# 现代操作系统不允许普通的程序直接操作磁盘，所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），
# 然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）。


def main():
    # file 打开失败会有异常，用try ... finally 始终关闭文件
    try:
        file_op = open('file_open.py', encoding='UTF-8')
        print(file_op.read())
    except Exception as err:
        print(err)
    finally:
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



if __name__ == '__main__':
    main()
