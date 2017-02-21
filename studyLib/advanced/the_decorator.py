#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

__author__ = 'Mr.Huo'


def log(func):
    def warpper(*args, **kwargs):
        print('call %s()' % func.__name__)
        return func(*args, **kwargs)

    return warpper


@log
def now1():
    print(time.strftime('%Y-%m-%d %H:%M:%S'))


def now2():
    print(time.strftime('%Y-%m-%d %H:%M:%S'))


# 如果装饰器本身要传入参数，则需要编写一个高阶函数返回装饰器
def log_text(text):
    def decorator(func):
        def warpper(*args, **kwargs):
            print('%s %s()' % (text, func.__name__))
            return func(*args, **kwargs)

        return warpper

    return decorator


@log_text("hello")
def now3():
    print(time.strftime('%Y-%m-%d %H:%M:%S'))


def main():
    # 装饰器
    now1()
    time.sleep(1)
    # 无装饰器
    d_now2 = log(now2)
    d_now2()
    time.sleep(1)
    now3()


if __name__ == '__main__':
    main()
