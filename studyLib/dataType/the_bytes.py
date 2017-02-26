#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from  pprint import pprint
import struct

__author__ = 'Mr.Huo'


def main():
    blist = [1, 2, 3, 255]
    # bytes 由字节作为基本元素(8位，取值0-255)组成的序列，为不可变序列
    the_bytes = bytes(blist)
    print('the bytes:    {0} \nthe bytes len:{1}'.format(the_bytes, len(the_bytes)))
    print(bytes('霍少华', encoding='utf8'))
    # 字节数组
    the_byte_array = bytearray(blist)
    print('the byte array:    {0} \nthe byte array len:{1}'.format(the_byte_array, len(the_byte_array)))
    print(bytes(range(0, 255)))
    print(bytearray(range(0, 255)))
    pprint(bytes(range(0, 255)))
    pprint(bytearray(range(0, 255)))

    #struct 字节序列和python中的数据转换
    '''<  小端方案
       >  大端方案
       标识符  描述                    字节
        x      跳过一个字节             1
        b      有符号字节               1
        B      无符号字节               1
        h      有符号短整数             2
        H      无符号短整数             2
        i      有符号整数               4
        I      无符号整数               4
        l      有符号长整数             4
        L      无符号长整数             4
        Q      无符号long long型整数    8
        f      单精度浮点数             4
        d      双精度浮点数             8
        p      数量和字符               1+数量
        s      字符                     数量
        unpack()字节序列转换成python中的数据
        pack()  python中的数据转换成字节序列
    '''
    valid_png_header = b'\x89PNG\r\n\x1a\n'
    data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + \
           b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'
    if data[:8] == valid_png_header:
        width, height = struct.unpack('>LL', data[16:24])
        print('Valid PNG ,width:{0} height:{1}'.format(width, height))
    print(data[16:24])
    print(bytes('89PNG',encoding='utf8'))

    print(struct.pack('>2L',width,height))

if __name__ == '__main__':
    main()
