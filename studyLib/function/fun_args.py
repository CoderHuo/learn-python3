#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Mr.Huo'


def menu(wine, entree, dessert):
    '''位置参数'''
    return {'wine': wine, 'entree': entree, 'dessert': dessert}


def print_args(*args):
    '''可变参数'''
    print('args:', args, "\nargs's tpye is", type(args))


def print_kwargs(**kwargs):
    '''关键字参数'''
    print('kwargs:', kwargs, "\nkwargs's tpye is", type(kwargs))


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


if __name__ == '__main__':
    main()
