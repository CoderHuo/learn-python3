#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Mr.Huo'


class MyDict(dict):
    '''
    doctest

    >>> d1 =MyDict()
    >>> d1
    {}
    >>> d1['x']=100
    >>> d1.x
    100
    >>> d2 = MyDict(a=1,b=2,c=3)
    >>> d2.c
    3
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    # doctest的异常匹配怎么做？ doc文档在保存时行尾的空被去掉(IDE?)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % item)

    def __setattr__(self, key, value):
        self[key] = value


if __name__ == '__main__':
    import doctest

    doctest.testmod()
