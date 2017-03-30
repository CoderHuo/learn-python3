#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件"""

from email.mime.text import MIMEText
import smtplib

__author__ = 'Mr.Huo'


def main():
    msg = MIMEText('Hello, send by Python...','plain','utf-8')
    #from_addr = input("From email:")
    from_addr = 'shaohua.huo@cienet.com.cn'
    password= input('PassWord:')
    #smtp_server = input("smtp server:")
    smtp_server = 'smtp.263xmail.com'
    to_addr = input('To email:')
    #to_addr = ['273139963@qq.com']

    email_server = smtplib.SMTP(smtp_server,465)
    email_server.set_debuglevel(1)
    email_server.login(from_addr,password)
    email_server.sendmail(from_addr, [to_addr], msg.as_string())
    email_server.quit()


if __name__ == '__main__':
    main()