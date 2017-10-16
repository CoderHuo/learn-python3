#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = 'Mr.Huo'

"""
Python 2.x中默认都是经典类，只有显式继承了object才是新式类
Python 3.x中默认都是新式类,经典类被移除，不必显式的继承object
新式类的MRO(method resolution order 基类搜索顺序)算法采用C3算法广度优先搜索，
而旧式类的MRO算法是采用深度优先搜索.
新式类相同父类只执行一次构造函数，经典类重复执行多次
"""


class A():
    def __init__(self, *args, **kwargs):
        print("A__init__")
        super(A, self).__init__()


class B():
    def __init__(self, *args, **kwargs):
        print("B__init__")
        super(B, self).__init__()


class C(A):
    def __init__(self, *args, **kwargs):
        print("C__init__, args=", args)
        super(C, self).__init__(*args, **kwargs)


class D(B):
    def __init__(self, *args, **kwargs):
        print("D__init__, args=", args)
        super(D, self).__init__(*args, **kwargs)


class E(C, D):
    def __init__(self, *args, **kwargs):
        print("E__init__, args=", args)
        super(E, self).__init__(*args, **kwargs)


def main():
    print(E.__mro__)
    print(E.mro())
    e = E(10)


if __name__ == '__main__':
    main()
