#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Mr.Huo'


def main():
    # tuple是一种不可变的有序表，一旦初始化就不能修改
    # 空的tuple
    t0 = ()
    print("empty tuple:", t0)
    # 只有1个元素的tuple定义时必须加一个逗号，消除歧义
    t1 = (1,)
    print("one element tuple :", t1)
    # tuple所谓的“不变”是说，tuple的每个元素，指向永远不变,如下：
    t3 = (1, 2, ['A', 'B'])
    print("tuple:", t3)
    print("element id:", id(t3[0]), id(t3[1]), id(t3[2]))
    t3[2][0] = 'X'
    t3[2][1] = 'Y'
    print("tuple:", t3)
    print("element id:", id(t3[0]), id(t3[1]), id(t3[2]))
    #切片操作tuple[x:y:z],
    print(t3[:])
    print(t3[-1::-1])


if __name__ == '__main__':
    main()
