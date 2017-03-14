#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools

__author__ = 'Mr.Huo'


def main():
    #count(start=0, step=1) --> count object
    natuals = itertools.count(1)
    for x in natuals:
        if x > 1000:
            break
        print(x)

    #cycle() Return elements from the iterable until it is exhausted
    cs = itertools.cycle('A12')
    count = 0
    for x in cs:
        count += 1
        if count > 1000:
            break
        print(x)

    #repeat(object [,times])
    rs1 = itertools.repeat('a')
    count = 0
    for x in rs1:
        count += 1
        if count > 1000:
            break
        print(x)
    rs2 = itertools.repeat('a', 10)
    print([x for x in rs2])

    #takewhile() 指定一个条件终止迭代
    natuals = itertools.count(1)
    it1 = itertools.takewhile(lambda x: x < 10, natuals)
    print(list(it1))

    #chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
    for c in itertools.chain('ABC', 'DDD'):
        print(c)

    #groupby()把迭代器中相邻的重复元素挑出来放在一起
    for key, group in itertools.groupby('1111AA1AACCCBb'):
        print(key, ' ', list(group))
    #groupby() 不区分大小写,或者其他的可以传入一个处理函数
    for key, group in itertools.groupby('1111AA1AACCCBb',lambda x:x.upper()):
        print(key, ' ', list(group))


if __name__ == '__main__':
    main()
