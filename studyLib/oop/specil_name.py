#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Mr.Huo'


class Fibonacci(object):
    def __init__(self, name='Fibonacci'):
        self.name = name
        self.a, self.b = 0, 1
        print('Init Class %s' % self.name)

    # __str__用于print()
    def __str__(self):
        '''用于print()'''
        return self.name

    # __repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的
    __repr__ = __str__

    # __iter__()返回迭代对象, 同__next__()做迭代使用
    def __iter__(self):
        print("[*]when self.a=%d,self.b=%d,__iter__ is called\n " % (self.a, self.b))
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a

    # __getitem__()取下标操作
    def __getitem__(self, item):
        pass

    # __getattr__()方法，动态返回一个属性
    def __getattr__(self, item):
        if item == 'test1':
            return "ShaoHua"
        elif item == 'test2':
            def fun_test2(*args, **kwargs):
                return args, kwargs

            return fun_test2
        else:
            raise AttributeError("%s object has no attribute %s" % (self.__class__, item))


def main():
    fi = Fibonacci('Huo')
    for x in fi:
        print(x)
    print(fi.test1)
    print(fi.test2(1, 2, name='Huo'))
    #fi.test3


if __name__ == '__main__':
    main()
