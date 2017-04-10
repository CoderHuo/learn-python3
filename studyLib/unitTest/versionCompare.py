#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

__author__ = 'Mr.Huo'


def version_compare(v1, v2):
    """版本号比较"""
    ver1 = _parse_version(v1)
    ver2 = _parse_version(v2)
    if len(ver1) < len(ver2):
        result = _compare(ver1, ver2, len(ver1))
        if result == 0:
            result = -1
    elif len(ver1) > len(ver2):
        result = _compare(ver1, ver2, len(ver2))
        if result == 0:
            result = 1
    else:
        result = _compare(ver1, ver2, len(ver1))
    if result == -1:
        print('The version(%s) is the newer' % v2)
    elif result == 0:
        print('The two versions are the same')
    elif result == 1:
        print('The version(%s) is the newer' % v1)
    return result


def _compare(v1, v2, length):
    """
    由于python3 不支持不同类型的比较，顾自己写比较方法，都是int按照int比较，其他的按照str比较
    :param v1: 
    :param v2: 
    :param length: 
    :return: 
        -1 ：str1 < str2
        0  : str1 = str2
        1  : str1 > str2
    """
    for i in range(length):
        if isinstance(v1[i], list):
            # 都是list 则比较list里面元素，由于list里面元素有int、str，所以自己写比较方法
            if isinstance(v2[i], list):
                if len(v1[i]) < len(v2[i]):
                    result = _cmp_list(v1[i], v2[i], len(v1[i]))
                    if result == 0:
                        # 当v1 v2 [0:len(v1[i])] 相等，则v2大
                        result == -1
                elif len(v1[i]) > len(v2[i]):
                    result = _cmp_list(v1[i], v2[i], len(v2[i]))
                    if result == 0:
                        # 当v1 v2 [0:len(v2[i])] 相等，则v1大
                        result == 1
                else:
                    result = _cmp_list(v1[i], v2[i], len(v1[i]))
                # 如果比较结果不相等，则已有结果，退出循环
                if result != 0:
                    break
            # v2 不是list，则为int 或者str，比较
            else:
                result = _cmp(v1[i], v2[i])
                if result == 0:
                    result == 1
                break
        else:
            if isinstance(v2[i], list):
                result = _cmp(v1[i], v2[i])
                if result == 0:
                    result == -1
                break
            else:
                result = _cmp(v1[i], v2[i])
    return result


def _cmp_list(v1, v2, index):
    """
    比较列表[0:index]元素大小，列表里面只包含int、str类型
    :param v1: 
    :param v2: 
    :param index: 
    :return: result
        -1 ：str1 < str2
        0  : str1 = str2
        1  : str1 > str2
    """
    if v1 == []:
        if v2 == []:
            result = 0
        else:
            result = -1
    else:
        if v2 == []:
            result = 1
        else:
            for i in range(index):
                result = _cmp(v1[i], v2[i])
                if result != 0:
                    break
    return result


def _cmp(str1, str2):
    """
    比较str 和 int 大小，都是int则按照int比较，否则按照str比较
    :param str1: 
    :param str2: 
    :return:int 
        -1 ：str1 < str2
        0  : str1 = str2
        1  : str1 > str2
    """
    if isinstance(str1, int) and isinstance(str2, int):
        if str1 > str2:
            return 1
        elif str1 < str2:
            return -1
        else:
            return 0
    else:
        if str(str1) > str(str2):
            return 1
        elif str(str1) < str(str2):
            return -1
        else:
            return 0


def _parse_version(ver, separator='.', ignorecase=True, ignorenull=False):
    """
    版本号分析：默认以'.'分隔
    :param ver: 
    :param separator:  版本号分隔符默认'.'
    :param ignorecase: 是否字母大小写
    :param ignorenull: 是否忽略类似'..' 或'.' 版本号，不忽略则'..' 比'.'大
    :return: list
    """
    if ver == '' or ver == None:
        raise RuntimeError("Version is null")
    if ignorecase:
        ver = ver.lower()
    pattern = re.compile(r'\d+|\D+')
    #
    if ignorenull:
        ver_list = [int(x) if x.isdigit() else [int(y) if y.isdigit() else y for y in pattern.findall(x)] for x in
                    ver.split(separator) if x != '']
    else:
        ver_list = [int(x) if x.isdigit() else [int(y) if y.isdigit() else y for y in pattern.findall(x)] for x in
                    ver.split(separator)]
    print(ver_list)
    return ver_list


def main():
    v1 = '121b-2-@Aw**--.2......1.1'
    v2 = '121b-2-@Aw**--.2..1'
    print(version_compare(v1, v2))
    v1 = '121b-2-@Aw**--.2..1'
    v2 = '121b-2-@Aw**--.2..1'
    print(version_compare(v1, v2))
    v1 = '..'
    v2 = '.'
    print(version_compare(v1, v2))
    v1 = '.'
    v2 = '.'
    print(version_compare(v1, v2))
    pass


if __name__ == '__main__':
    main()
