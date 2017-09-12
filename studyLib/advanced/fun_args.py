#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Mr.Huo'

"""可变参数args，关键字参数kwargs，作为参数传递给一个可变参数args、关键字参数kwargs，
应该使用 *args、**kwargs的形式.
位置参数传递：可以使用列表*args(列表长度不大于参数列表)、字典**kwargs(列表长度不大于参数列表，key为位置参数)
"""


def menu(wine, entree, dessert):
    """位置参数"""
    return {'wine': wine, 'entree': entree, 'dessert': dessert}


def print_args(*args):
    """可变参数"""
    print('args:', args, "\nargs's tpye is", type(args))
    print_ag(*args)


def print_kwargs(**kwargs):
    """关键字参数"""
    print('kwargs:', kwargs, "\nkwargs's tpye is", type(kwargs))
    print_kw(**kwargs)


def print_ag(*args):
    print('args:', args, "\nargs's tpye is", type(args))


def print_kw(**kw):
    print('kw:', kw, "\nkw's tpye is", type(kw))


def knights(a, b):
    def inner(c, d):
        return c * d

    return inner(a, b)


def knights2(a, b):
    def inner2():
        return a * b

    return inner2


def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step


def document_it(func):
    # print('Running21 function:', func.__name__)

    def new2_function(*args, **kwargs):
        print('Running22 function:', func.__name__)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result

    return new2_function


def square_it(func):
    # print('Running11 function:', func.__name__)

    def new1_function(*args, **kwargs):
        print('Running12 function:', func.__name__)
        print('huo')
        result = func(*args, **kwargs)
        print('huo')
        return result * result

    return new1_function


@document_it
@square_it
def add_ints(*args):
    y = 0
    for x in args:
        y += x
    return y


def main():
    a = menu(1, 2, 3)
    print(a)
    print(a, type(a))
    print(menu(3, entree=2, dessert=1))
    print_args(1, 2, 3, 4, 'aaaa', '6b')
    print_kwargs(key1=1, key2=2, key3=3, key4=4, key5='aaaa', key6='6b')
    help(menu)
    b = knights(3, 4)
    print(b)
    print(type(knights(2, 8)))
    c = knights2(5, 6)
    print(c, c())

    range1 = my_range(1, 20)
    for x in range1:
        print(x, 'H', end=' ')
    print(end='\n')
    range2 = document_it(my_range)
    range3 = range2(1, 10)
    for y in range3:
        print(y, end=' ')
    print(end='\n')
    print('====================', end='\n')
    d = add_ints(1, 2, 3, 4)
    print(d)

    args = [11, 12, 13]
    print(menu(*args))
    print(menu(110, *args[:2:]))
    kwargs = {'wine': 111, 'entree': 112, 'dessert': 113}
    print(menu(**kwargs))


if __name__ == '__main__':
    main()
