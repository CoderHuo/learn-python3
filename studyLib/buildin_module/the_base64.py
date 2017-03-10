#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64, re

__author__ = 'Mr.Huo'


#处理去掉=的base64解码函数
def safe_base64_decode(s):
    s = base64._bytes_from_decode_data(s)
    i = len(s) % 4
    if 0 != i:
        s += (4 - i) * b"="
    return base64.b64decode(s)


#去掉末尾添加的=的BASE64
def safe_base64_encode(s):
    s = base64.b64encode(s)
    m = re.match(b'(^[A-Za-z0-9+/]*)(={0,2}$)', s)
    return m.group(1)


def main():
    s1 = '我爱你='
    print(s1.encode())
    print(s1.encode(encoding='gbk'))
    print(s1.encode(encoding='gbk').decode(encoding='gbk'))
    # s1的utf-8字节码
    s2 = s1.encode()
    print(len(s2))
    print("'%s'的utf-8字节码:%s" % (s1, s2))
    s3 = base64.b64encode(s2)
    print("'%s'的utf-8字节码转换成BASE64:%20s" % (s1, s3))
    #BASE64转换成字节码
    s4 = base64.b64decode(s3)
    assert s4 == s2
    #字节码解码成unicode
    s5 = s4.decode()
    assert s5 == s1

    #编码图片到BASE64
    with  open("Tulips.jpg", 'rb') as pic1:
        pic1_bytes = pic1.read()
        #print(pic1_bytes)
        #print(len(pic1_bytes))
        #print(type(pic1_bytes))
        pic1_base64 = base64.b64encode(pic1_bytes)
        #print(pic1_base64)
        print(pic1_bytes[::30])

        #按行读取 按行读取好像有问题，总数对不上？留待
        pic1.seek(0)
        pic1_base64_list = [base64.b64encode(x) for x in pic1.readlines()]
        #print(len(pic1_base64_list))
        for x in pic1_base64_list:
            #print(x)
            pass

    s6 = b'abcd'
    s7 = safe_base64_encode(s6)
    s8 = safe_base64_decode(s7)
    s9 = base64.b64encode(s6)
    assert s6 == s8
    print('%-10s 未去除末尾的=的BASE64为：        %s'%(s6, s9))
    print('%-10s 去除末尾的=的BASE64为：          %s'%(s6, s7))
    print('%-10s 去除末尾的=的BASE64转换成字节码：%s'%(s7, s8))


if __name__ == '__main__':
    main()
