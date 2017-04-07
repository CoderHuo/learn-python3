#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

__author__ = 'Mr.Huo'


def version_compare(v1, v2):
    v1 = _parse_version(v1)
    v2 = _parse_version(v2)
    minlength = 0
    print(len(v1),len(v2))
    if len(v1) < len(v2):
        result = compare(v1, v2, len(v1))


def compare(v1, v2, length):
    for i in range(length):
        if isinstance(v1[i],list):
            pass
    pass


def _parse_version(ver, separator='.', ignorecase=True):
    if ver == '' or ver == None:
        raise RuntimeError("Version is null")
    if ignorecase:
        ver = ver.lower()
    pattern = re.compile(r'\d+|\D+')
    ver_list = [int(x) if x.isdigit() else [int(y) if y.isdigit() else y for y in pattern.findall(x)] for x in
                ver.split(separator)]
    print(ver_list)
    # 去除末尾多余0及空标识
    while ver_list:
        if ver_list[-1] == [] or ver_list[-1] == 0:
            ver_list.pop()
        else:
            break
    print(ver_list)
    return ver_list


def main():
    v1 = '111b-2-@Aw**--.2..1'
    v2 = '111b-2-@Aw**--.2..1..0.01.00..'
    version_compare(v1, v2)
    pass


if __name__ == '__main__':
    main()
