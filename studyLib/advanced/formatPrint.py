#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Mr.Huo'


# 格式化输出

def main():
    '''%格式化字符串
    %s 字符
    %d 整数
    %? 占位符，%0? 只能用0当占位符
    %f 浮点数，%.3f指定保留小数点位数
'''
    day = 20170219
    pi = 3.1415926
    print("字符-> %s" % __author__)
    print("整数-> %d" % day)
    print("浮点-> %f" % pi)
    # 打印浮点数（指定保留小数点位数）
    print("浮点指定保留小数点位-> %.3f" % pi)
    # 指定占位符宽度默认右对齐
    print("字符带占位符-> |%10s|" % __author__)
    print("整数带占位符-> |%10d|" % day)
    print("浮点带占位符-> |%10.3f|" % pi)
    # 指定占位符宽度默左-对齐
    print("字符带占位符-> |%-10s|" % __author__)
    print("整数带占位符-> |%-10d|" % day)
    print("浮点带占位符-> |%-10.3f|" % pi)
    # 科学计数 .3e 小数后位数
    print('科学计数    -> |%10s|' % format(0.0000000023, '.2e'))


if __name__ == '__main__':
    main()
