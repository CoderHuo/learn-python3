#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Mr.Huo'


# @property  @XXX.setter 将属性的读取方法变为属性

class Screen():
    __slots__ = ('_width', '_height')

    def __init__(self, width=None, height=None):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError("width must be an integer!")
        if value < 0 or value > 10000:
            raise ValueError("width out of range!")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError("height must be an integer!")
        if value < 0 or value > 10000:
            raise ValueError("height out of range!")
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


def main():
    s = Screen()
    s.height = 768
    s.width = 1024
    print(s.resolution)
    assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution


if __name__ == '__main__':
    main()
