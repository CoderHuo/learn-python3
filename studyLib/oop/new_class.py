#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = 'Mr.Huo'

"""
cls  代表类名
self 代表对象
__new__(cls,*args, **kwargs)   创建实例对象，返回一个实例对象
    (cls 可以为其他类名，返回传递的其他类实例对象，如果需要初始化，就需要显示调用
     该类的__init__()方法）
__init__(self,*args, **kwargs) 初始实例对象
"""


class Foo():
    def __init__(self, *args, **kwargs):
        self.name = 'Foo'
        print("Foo.__init__ call")

    def __new__(cls, *args, **kwargs):
        print("Foo.__new__")
        obj = object.__new__(Stranger, *args, **kwargs)
        obj.__init__(*args, **kwargs)
        return obj


class Stranger():
    def __init__(self, *args, **kwargs):
        self.name = 'Stranger'
        print("Stranger.__init__ call")

    def __new__(cls, *args, **kwargs):
        print("Stranger.__new__")
        return object.__new__(cls, *args, **kwargs)


def main():
    # Foo的new 传递的是Stranger，实际创建出来的是Stranger对象实例
    foo = Foo()
    print(type(foo))
    st = Stranger()
    print(type(st))
    print(id(foo))
    print(id(st))

    # 显示调用Foo.__new__，new中又调用了 Stranger的 __init__,顾foo1初始化了
    foo1 = Foo.__new__(Foo)
    print(type(foo1))
    print(id(foo1))
    print(foo1.name)

    # 显示调用Stranger.__new__，new中没有调用Stranger的__init__,顾没有初始化了，没有name属性
    st1 = Stranger.__new__(Stranger)
    print(type(st1))
    print(id(st1))
    print(hasattr(st1,'name'))
    # 显示初始化
    st1.__init__()
    print(hasattr(st1,'name'))




if __name__ == '__main__':
    main()
