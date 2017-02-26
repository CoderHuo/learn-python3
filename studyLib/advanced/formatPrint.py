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
    %e 科学计数法
    %x 十六进制整数
    %o 八进制整数
    %g 十进制或科学计数法表示的浮点数
    %% 文本值%本身
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

    # {} format
    n = 42
    f = 7.03
    s = 'string cheese'
    #{}里面的数字为format后变量的序号
    print('{2} {1} {0}'.format(n,f,s))

    print('{0:d} {1:f} {2:s}'.format(n,f,s))
    d = dict(n = 42,f = 7.03,s='string cheese')
    #{0}代表整个字典
    print('{0[n]} {0[f]} {0[s]} {1}'.format(d,'hello'))
    #域宽 >右对齐  <左对齐 ^居中,字符串默认对齐方式为左，尽量不要使用默认，明确指明对齐方式
    print('{0:10s}'.format('hello'))
    print('{0[n]:15}|\n{0[f]:15}|\n{0[s]:15s}|\n{1:^15s}|'.format(d,'hello'))
    p_str= '{0[n]:15}|\n{0[f]:<15}|\n{0[s]:>15s}|\n{1:^15s}|'.format(d,'hello')
    print(p_str)

if __name__ == '__main__':
    main()
