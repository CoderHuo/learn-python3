#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Mr.Huo'


# 动态创建类
def fn(self, name='world'):
    print('Hello %s ' % name)


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


def main():
    print(type(type))
    # 要创建一个class对象，type()函数依次传入3个参数：
    #    1.class的名称；
    #    2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
    #    3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。#
    Hello = type('Hello', (object,), dict(hello=fn))
    print(type(Hello))
    h = Hello()
    h.hello()
    print(type(h))

    L = MyList()
    print(L)
    L.add(1)
    print(L)


if __name__ == '__main__':
    main()
