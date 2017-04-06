#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Mr.Huo'


def version_compare(v1, v2):
    if v1 == '' or v2 == '':
        raise RuntimeError("Version is null")

    t1 = v1.split('.')
    t2 = v2.split('.')
    print(t1, t2)
    result = 0
    if len(t1) < len(t2):
        result = compare(t1, t2, len(t1))
        if result == 0:
            result = -1
    elif len(t1) > len(t2):
        result = compare(t1, t2, len(t2))
        if result == 0:
            result = 1
    else:
        result = compare(t1, t2, len(t1))
    # 输出判断结果
    if result == 0:
        print('The two versions are the same.')
    elif result == -1:
        print('The vesion:[%s] is newer.' % v2)
    elif result == 1:
        print('The vesion:[%s] is newer.' % v1)
    return result


def compare(s1, s2, len):
    result = 0
    for i in range(len):
        if s1[i] < s2[i]:
            result = -1
            break
        elif s1[i] > s2[i]:
            result = 1
            break
        else:
            result = 0
    return result


def main():
    v1 = '111a-.2.1'
    v2 = '111b.2.1'
    res = version_compare(v1, v2)
    print(res)
    v1 = ''
    v2 = '111b.2.1'
    # res = version_compare(v1, v2)
    pass


if __name__ == '__main__': main()
