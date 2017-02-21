#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Mr.Huo'


# yield 可以简单理解为一个断点，返回一个值，下次从yield后执行，当没有yield可执行，即出现StopIteration异常
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    print('yield end')


def main():
    # generator：一边循环一边计算
    # 创建generator，根据列表生成式创建
    L = (x * x for x in range(10))
    print(L)
    print(L.__next__())
    for x in L:
        print(x)
    # 通过函数中带yield创建一个generator
    gen = odd()
    print('generator next 1')
    print(gen.__next__())
    print('generator next 2')
    print(gen.__next__())
    try:
        print(gen.__next__())
    except StopIteration as err:
        print(err)

    print(list(odd()))


if __name__ == '__main__':
    main()
