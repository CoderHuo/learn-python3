#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Mr.Huo'


def foo(s):
    n = int(s)
    if n == 0:
        # 抛出异常
        raise ValueError('Invalid Divisor: %s' % s)
    return 10 / n


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except ValueError as err:
        print(err)
    finally:
        print('END')

    print("Python's Exception:")
    bar(00)


if __name__ == '__main__':
    main()
