#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

__author__ = 'Mr.Huo'


def add(x):
    return x + x


def add_two(x, y):
    return x + y


def statistics(dic, k):
    if not k in dic:
        dic[k] = 1
    else:
        dic[k] += 1
    return dic


def main():
    # python map()函数,接收两个参数函数、Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
    list1 = [x for x in range(1, 12)]
    t1 = tuple(x for x in range(10, 29))
    map1 = map(add, list1)
    map2 = map(add, t1)
    print(list(map1))
    print(list(map2))
    # map 接收的函数有多个参数，iterable就需要对应有多个
    map3 = map(add_two, t1, list1)
    print(list(map3))

    # reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
    # reduce把结果继续和序列的下一个元素做累积计算，
    # 其效果就是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
    help(reduce)
    redu1 = reduce(add_two, list1)
    print(redu1)
    redu2 = reduce(statistics, list1, {})
    print(redu2)
    redu3 = reduce(statistics, list1, redu2)
    print(redu3)
    list2 = ['H', 'S', 'H']
    redu4 = reduce(statistics, list2, {})
    print(redu4)


if __name__ == '__main__':
    main()
