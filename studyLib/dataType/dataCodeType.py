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
编辑器以某种编码打开保存在硬盘的文件，显示出来,脚本运行，解释器、编译器会以某种指定的编码读取，转换到内存的Unicode
python会在文件开头写上这两行
#!/usr/bin/env python3    告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释
# -*- coding: utf-8 -*-   告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码
申明了UTF-8编码并且保存的文件也要是UTF-8
'''
help(main)
myname = ['霍', '少', '华']
mynameUnicode =[x.encode() for x in myname]
mynameGB2312 = [x.encode('GB2312') for x in myname]
mynameUTF8 =   [x.encode('utf-8')  for x in myname]
print('霍少华的Unicode编码为：',mynameUnicode)
print('霍少华的GB2312编码为： ',mynameGB2312)
print('霍少华的UTF-8编码为：  ',mynameUTF8)



if __name__ == '__main__':
    main()