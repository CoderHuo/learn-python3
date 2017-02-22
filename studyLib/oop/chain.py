#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Mr.Huo'


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        # print(path)
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

    # 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用
    def __call__(self, item):
        return Chain('%s:%s' % (self._path, item))


def main():
    print(Chain('home').status.user.timeline.list)
    print(Chain('home').status.user('Huo').timeline.list)
    c = Chain('ZhiXuan')
    print(c.status.user.timeline.list)
    print(c('HUO'))
    print(c.status('HUO'))
    print(c.status.user.timeline.list("HUO"))


if __name__ == '__main__':
    main()
