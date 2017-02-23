#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging

# logging 指定记录信息的级别，有debug，info，warning，error
logging.basicConfig(level=logging.INFO)
__author__ = 'Mr.Huo'


def foo(s):
    n = int(s)
    logging.info('n is %d' % n)
    return 10 / n


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except ZeroDivisionError as err:
        print(err)
    finally:
        print('END')


if __name__ == '__main__':
    main()
