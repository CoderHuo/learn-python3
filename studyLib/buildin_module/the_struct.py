#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import struct
__author__ = 'Mr.Huo'


def main():
    #struct 字节序列和python中的数据转换
    '''<  小端方案
       >  大端方案  网络序
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
    s1 = struct.pack('>3I',1,2,3)
    print(s1)
    s2 = struct.unpack('>3I',s1)
    print(s2)
    s3 = struct.pack('>s',b's')
    print(s3)
    s4 = struct.unpack('>3I',s1)
    print(s4)
    s5 = b'\rIHDR'
    print(s5.decode())
    s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
    print(struct.unpack('<ccIIIIIIHH',s))
    pass


if __name__ == '__main__':
    main()