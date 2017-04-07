#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

__author__ = 'Mr.Huo'


def version_compare(v1, v2):
    v1 = _parse_version(v1)
    v2 = _parse_version(v2)
    try:
        return (v1 > v2) - (v1 < v2)
    except:
        return False


def _parse_version(ver,separator='.',ignorecase=True):
    if ver == '' or ver == None:
        raise RuntimeError("Version is null")
    if ignorecase:
        ver =ver.lower()
    pattern = re.compile(r'\d+|\D+')
    ver_list = [int(x) if x.isdigit() else [int(y) if y.isdigit() else y for y in pattern.findall(x)] for x in
                ver.split(separator)]
    return ver_list


def main():
    v1 = '111b-2-@Aw**--.2..1'
    v2 = '111b-2-@Aw**--.2..1'
    # res = version_compare(v1, v2)
    version_compare(v1, v2)
    pattern = re.compile(r'\d+|\D+')
    match = pattern.findall(v2)

    print(match)
    print([int(x) if x.isdigit() else x for x in match])
    print(_parse_version(v2))
    pass


if __name__ == '__main__':
    main()
    print( ''<'1')