#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Mr.Huo'


def main():
    #list是一种可变的有序表，可以随时添加和删除其中的元素
    # 使用[],list()创建一个空列表
    empty_list = []
    another_empty_list = list()

    my_list = ['huo', 'shao', 'hua']

    empty_list = list('cat')

    a_tuple = ("liu", "zhi", 'xuan')
    #从一个元组创建list
    another_empty_list = list(a_tuple)

    print(empty_list)
    print(another_empty_list)
    print(my_list)

    # 列表推导式
    rows = range(1, 6)
    cols = range(2, 7)
    cells = [(row, col) for row in rows for col in cols]
    print(cells)

    #l.append(x)末尾增加x
    my_list.append('30')
    print(my_list)
    # l.insert(i,x)
    my_list.insert(3,'40')
    print(my_list)
    # l.pop([i])
    my_list.pop()
    print(my_list)
    my_list.pop(3)
    print(my_list)
    #切片操作tuple[x:y:z]
    print(my_list[-1::-1])

if __name__ == '__main__':
    main()
