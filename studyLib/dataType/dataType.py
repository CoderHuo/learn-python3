#!/usr/bin/env python3
# coding: utf-8


def dataInt():
    """python int 可以处理任意大小的整数（正负）"""
    int1 = 1023
    intBin = bin(int1)  # 二进制
    intOct = oct(int1)  # 八进制
    intDec = int(int1)  # 十进制
    intHex = hex(int1)  # 十六进制

    print(type(int1), type(intBin), type(intDec), type(intOct), type(intHex))
    print('%d Bin：%12s\n%d Oct：%12s\n%d Dec：%12s\n%d Hex：%12s\n'
          % (int1, intBin, int1, intOct, int1, intDec, int1, intHex))


def dataFloat():
    """python float"""
    float1 = 1 / 3
    float2 = 1.2e-10
    print(float1, float2)


def dataComplex():
    """python complex"""
    complex1 = complex(-1)
    print(type(complex1), complex1)


def dataString():
    """python string"""
    str1 = 'My name is huoshaohua'
    print(str1)


def main():
    '''
        int(x [,base])        将x转换为一个整数
        float(x )             将x转换到一个浮点数
        complex(real [,imag]) 创建一个复数
        str(x)                将对象x转换为字符串
        repr(x)               将对象x转换为表达式字符串
        eval(str)             用来计算在字符串中的有效Python表达式,并返回一个对象
        tuple(s)              将序列s转换为一个元组
        list(s)               将序列s转换为一个列表
        chr(x)                将一个整数转换为一个字符
        unichr(x)             将一个整数转换为Unicode字符
        ord(x)                将一个字符转换为它的整数值
        hex(x)                将一个整数转换为一个十六进制字符串
        oct(x)                将一个整数转换为一个八进制字符串
    '''
    boolString = """ 布尔值：True False 布尔运算：and or not"""
    noneString = """ 空值：None
    None和False它们的主要区别是在语义上：False和True对应，它作为布尔类型用来描述逻辑中“假”这个概念；
    None和“存在元素”相对应，“存在元素”反过来为“不存在元素”，也就是None。
    这两个对象在实际使用中也应该遵守这个规则。
    None是一个对象，其类型为NoneType，作为一个对象其bool值为False"""
    dataInt()
    dataFloat()
    dataComplex()
    dataString()
    help(main)
    print(boolString)
    print(noneString)


if __name__ == '__main__':
    main()
