#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import namedtuple

__author__ = 'Mr.Huo'


def main():
    Point = namedtuple('Point',['x','y'])
    p1 =Point(1,2)
    print(p1.x,p1.y)


if __name__ == '__main__':
    main()