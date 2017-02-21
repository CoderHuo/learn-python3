#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def Hanoi_Move(n, a='a', b='b', c='c'):
    if (n == 1):
        print(a, "-->", c)
        return
    Hanoi_Move(n - 1, a, c, b)
    print(a, "-->", c)
    Hanoi_Move(n - 1, b, a, c)


def fibonacci_big(end=10):
    '''斐波那契数列生成器，按照最大值生成'''
    a = b = 1
    if a < end:
        yield a
    if b < end:
        yield b
    while True:
        a, b = b, a + b
        if (b < end):
            yield b
        else:
            break


def fibonacci_cnt(cnt=10):
    '''斐波那契数列生成器，按照个数生成'''
    cn = 0
    a = b = 1
    if cn < cnt:
        cn += 1
        yield a
    if cn < cnt:
        cn += 1
        yield b
    while True:
        a, b = b, a + b
        if cn < cnt:
            cn += 1
            yield b
        else:
            break


def main():
    Hanoi_Move(10)
    print(list(fibonacci_big(10000)))
    print(list(fibonacci_cnt(2)))
    print(list(fibonacci_cnt(10)))


if __name__ == '__main__':
    main()
