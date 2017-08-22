#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import poplib
from email.parser import Parser
from email.utils import parseaddr
from email.header import decode_header

__author__ = 'Mr.Huo'

'''
第一步：用poplib 把邮件的原始文本下载到本地
第二步：用email解析原始文本，还原邮件对象
'''


def print_info(msg, index=0):
    """分析邮件"""
    if index == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)
                #elif header == 'To':
                #    print('To==========BEGIN',value,'To==========END')
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print(('%s%s: %s') % (' ' * index, header, value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%s part %s' % (' ' * index, n))
            print('%s------------------------' % (' ' * index))
            print_info(part, index + 1)
    else:
        content_type = msg.get_content_type()
        if content_type in ('text/plain', 'text/html'):
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % (' ' * index, content + '...'))
        else:
            print('%sAttachment: %s' % (' ' * index, content_type))


def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos > 0:
            charset = content_type[pos + 8:].strip()
    return charset


def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def main():
    email_addr = input("Email addr:")
    password = input('PassWord:')
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
    #print(msg)
    print_info(msg)
    # 可以根据邮件索引直接从服务器中删除邮件
    # email_server.dele(len(mails))
    # 关闭连接

    email_server.quit()


if __name__ == '__main__':
    main()
