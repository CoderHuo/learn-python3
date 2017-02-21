#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools

__author__ = 'Mr.Huo'


# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。

def main():
    int2 = functools.partial(int, base=2)
    print(int2)
    print(int2('10'))
    pass


if __name__ == '__main__':
    main()
