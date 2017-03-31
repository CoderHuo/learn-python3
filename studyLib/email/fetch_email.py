#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import poplib
from email.parser import Parser

__author__ = 'Mr.Huo'

'''
第一步：用poplib 把邮件的原始文本下载到本地
第二步：用email解析原始文本，还原邮件对象
'''


def main():
    # email_addr = input("Email addr:")
    # password = input('PassWord:')
    email_addr = 'shaohua.huo@cienet.com.cn'
    password = 'zhixuan_860606'
    # email_server = input("smtp server:")
    server_addr = 'pop3.263xmail.com'

    # 连接邮箱服务器 使用POP3_SSL
    email_server = poplib.POP3_SSL(server_addr, port=1995)
    email_server.set_debuglevel(0)
    # 获取欢迎信息
    print(email_server.getwelcome())

    email_server.user(email_addr)
    email_server.pass_(password)
    # stat()返回邮件数量和占用空间:
    print(email_server.stat())

    # list()返回所有邮件的编号:
    resp, mails, octets = email_server.list()
    print(mails)

    # 获取最新的一份邮件，注意序号从1开始
    resp, lines, octets = email_server.retr(len(mails))
    msg_content = b'\r\n'.join(lines).decode()
    msg = Parser().parsestr(msg_content)
    print(msg)
    # 可以根据邮件索引直接从服务器中删除邮件
    # email_server.dele(len(mails))
    # 关闭连接
    email_server.quit()


if __name__ == '__main__':
    main()
