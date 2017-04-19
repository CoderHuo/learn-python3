#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件"""

from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
from email.message import Message
import smtplib

__author__ = 'Mr.Huo'


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def main():
    from_addr = input("From email:")
    password = input('PassWord:')
    # smtp_server = input("smtp server:")
    smtp_server = 'smtp.263xmail.com'
    to_addr = input('To email:')

    # 邮件正文
    msg = MIMEText('Hello, send by Python...', 'plain', 'utf-8')
    # 邮件头:标题、发送者、接收者
    msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
    msg['To'] = _format_addr('Python爱好者 <%s>' % to_addr)
    msg['Subject'] = Header('Python爱好者', 'utf-8').encode()

    email_server = smtplib.SMTP(smtp_server, 465)
    email_server.set_debuglevel(1)
    email_server.login(from_addr, password)
    email_server.sendmail(from_addr, [to_addr], msg.as_string())

    # 发送HTML
    msg = MIMEText('<html><body><h1>Hello</h1>' +
                   '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
                   '</body></html>', 'html', 'utf-8')
    email_server.sendmail(from_addr, [to_addr], msg.as_string())
    
    email_server.quit()


if __name__ == '__main__':
    main()
