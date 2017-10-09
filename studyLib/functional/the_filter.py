#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Mr.Huo'


def is_odd(x):
    return x % 2 == 1


def is_palindrome(n):
    """判断一个数是不是回数"""
    return str(n) == str(n)[::-1]


# 用filter求素数
# 首先，列出从2开始的所有自然数，构造一个序列：
# 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
# 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
# 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
# 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 不断筛下去，就可以得到所有的素数
def _odd_iter():
    """从3开始的基数序列生成器，无限"""
    n = 1
    while True:
        #print('_odd_iter',n)
        n += 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes(max=10):
    """素数生成器，生成不大于max的素数"""
    n = 1
    if n <= max:
        yield n
        yield n+1
    it = _odd_iter()  # 初始序列，3开始的基数序列
    while True:
        n = next(it)  # 返回序列的第一个值
        if n <= max:
            yield n
        else:
            break
        it = filter(_not_divisible(n), it)  # 重新获取序列生成器，不包含能被第一个整数的。


def main():
    # Python内建的filter()函数用于过滤序列,把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
    # 关键在于正确实现一个“筛选”函数
    list1 = [x for x in range(0, 11)]
    fi1 = list(filter(is_odd, list1))
    print(fi1)

    # 回数
    output = filter(is_palindrome, range(1, 500))
    print("回数：", list(output))

    print("素数：", list(primes(100)))
    print(dir(_not_divisible(3)))

if __name__ == '__main__':
    main()
