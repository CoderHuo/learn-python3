#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def Hanoi_Move(n, a='a', b='b', c='c'):
    if (n == 1):
        print(a, "-->", c)
        return
    Hanoi_Move(n - 1, a, c, b)
    print(a, "-->", c)
    Hanoi_Move(n - 1, b, a, c)


def fibonacci_max(max=10):
    '''斐波那契数列生成器，按照最大值生成'''
    a = 0
    b = 1
    while b < max:
        yield b
        a, b = b, a + b


def fibonacci_cnt(cnt=10):
    '''斐波那契数列生成器，按照个数生成'''
    cn = 0
    a = 0
    b = 1
    while cn<cnt:
        yield b
        a, b = b, a + b
        cn += 1


def main():
    Hanoi_Move(10)
    print(list(fibonacci_max(10000)))
    print(list(fibonacci_cnt(2)))
    print(list(fibonacci_cnt(20)))


if __name__ == '__main__':
    main()
