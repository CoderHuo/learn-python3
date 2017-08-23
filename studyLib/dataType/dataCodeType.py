#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    '''
    计算机只能处理数字即0-1，跟字符有个编码过程。
    编码方式：
        ascii:一个字节编码，最开始的编码格式
        unicode:通常两个字节编码,在计算机内存中，统一使用Unicode编码,
                以Unicode表示的str通过encode()方法可以编码为指定的bytes
        uft-8:针对Unicode的可变长度字符编码,当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码,节省空间
        GB2312:中文编码
        等等
    编辑器打开以某种编码保存在硬盘的文件，转换到内存的Unicode，显示出来,脚本运行，解释器使用。当保存文件的时候又转换为原有编码
    python会在文件开头写上这两行
    #!/usr/bin/env python3    告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释
    # -*- coding: utf-8 -*-   告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码
    申明了UTF-8编码并且保存的文件也要是UTF-8
    decode的作用是将其他编码的字符串转换成某种编码格式的字节数组，如str1.decode('gb2312')，表示将str1转换成gb2312编码的字节数组。
    encode的作用是将字节数组已某种编码格式转换成字符串，如str2.encode('gb2312')，表示将字节数组str2转换成gb2312编码的字符串。
    Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言
    '''
    help(main)
    myname = ['擎', '天', '柱']
    mynameGB2312 = [x.encode('GB2312') for x in myname]
    mynameUTF8 = [x.encode('utf-8') for x in myname]
    b2s_nameGB2312 = [x.decode('GB2312') for x in mynameGB2312]
    print('擎天柱的GB2312编码为：         ', mynameGB2312, type(mynameGB2312[0]))
    print('擎天柱的UTF-8编码为：          ', mynameUTF8, type(mynameUTF8[0]))
    print('GB2313编码的bytes转换成字符串：', b2s_nameGB2312, type(b2s_nameGB2312[0]))
    # 单个字符的整数表示 y=ord(x)
    # 编码转换成对应字符 x=chr(y)
    mynameOrd = [ord(x) for x in myname]
    mynameOrdChr = [chr(x) for x in mynameOrd]
    mynameUnicode = [hex(ord(x)).replace('0x', '') for x in myname]
    print('擎天柱的Unicode编码为： \\u%s, \\u%s, \\u%s' % (mynameUnicode[0], mynameUnicode[1], mynameUnicode[2]))
    print('ord(擎天柱)为:         ', mynameOrd)
    print('chr(ord(擎天柱）)为:   ', mynameOrdChr)


if __name__ == '__main__':
    main()
