#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

__author__ = 'Mr.Huo'


def log(func):
    def wrapper(*args, **kwargs):
        #wrapper.__name__ = func.__name__
        print('call %s()' % func.__name__)
        result = func(*args, **kwargs)
        print('end  %s()' % (func.__name__))
        return result

    return wrapper


@log
def now1():
    print(time.strftime('%Y-%m-%d %H:%M:%S'))


def now2():
    print(time.strftime('%Y-%m-%d %H:%M:%S'))


# 如果装饰器本身要传入参数，则需要编写一个高阶函数返回装饰器
def log_text(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            #返回是wrapper函数，可以修改函数名为实际被装饰的函数名
            wrapper.__name__ = func.__name__
            print('%s %s()' % (text, func.__name__))
            return func(*args, **kwargs)
            print('end  %s()' % (func.__name__))

        return wrapper

    return decorator


@log_text("hello")
def now3():
    print(time.strftime('%Y-%m-%d %H:%M:%S'))


def main():
    # 装饰器
    d_now=now1
    d_now()
    print(d_now.__name__)
    time.sleep(1)
    # 无装饰器
    d_now = log(now2)
    d_now()
    time.sleep(1)
    d_now=now3
    d_now()
    print(d_now.__name__)


if __name__ == '__main__':
    main()
