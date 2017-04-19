#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = 'Mr.Huo'


def extend_list(val, p_list=[]):
    p_list.append(val)
    print(id(p_list))
    return p_list


def extend_list_improve(val, p_list=None):
    if p_list is None:
        p_list = []
    p_list.append(val)
    return p_list


def main():
    list1 = extend_list(1)
    print('dir_main', dir())
    list2 = extend_list(2)
    print(id(list1), list1, id(list2), list2)
    list3 = extend_list_improve(1)
    list4 = extend_list_improve(2)
    print(id(list3), list3, id(list4), list4)


if __name__ == '__main__':
    main()
    a = 1
    print(type(main))
    print(type(a))
    print(dir(a))
    print(dir(int))
    print(a.__dir__)
    print(ascii(a),ascii(0x31))
    print(None)
    print(dir(None))
    print(None.__sizeof__())
    print(None.__hash__())
    print(None.__init__())