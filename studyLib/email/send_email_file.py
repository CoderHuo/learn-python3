#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
from email.message import Message
import smtplib

__author__ = 'Mr.Huo'

'''
在python中，MIME的这些对象的继承关系如下。
MIMEBase
    |-- MIMENonMultipart
        |-- MIMEApplication
        |-- MIMEAudio
        |-- MIMEImage
        |-- MIMEMessage
        |-- MIMEText
    |-- MIMEMultipart
MIMEMultipart有attach方法，而MIMENonMultipart没有，只能被attach。
MIME有很多种类型，这个略麻烦，如果附件是图片格式，我要用MIMEImage，如果是音频，要用MIMEAudio，
如果是word、excel，我都不知道该用哪种MIME类型了，得上google去查。
最懒的方法就是，不管什么类型的附件，都用MIMEApplication，
MIMEApplication默认子类型是application/octet-stream。
application/octet-stream表明“这是个二进制的文件，希望你们那边知道怎么处理”，然后客户端
'''


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def main():
    from_addr = input("From email:")
    password = input('PassWord:')
    # smtp_server = input("smtp server:")
    smtp_server = 'smtp.263xmail.com'
    to_addr = input('To email:')

    msg = MIMEMultipart()
    # 邮件正文
    msg.attach(MIMEText('Send with file','plain','utf-8'))
    # 邮件头:标题、发送者、接收者
    msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
    msg['To'] = _format_addr('Python爱好者 <%s>' % to_addr)
    msg['Subject'] = Header('Python爱好者', 'utf-8').encode()

    #添加附件，就是加上一个MIMEBase，从本地读取一个文件，从MIMEBase构造一个附件
    file_name ='sendemail_SMTP.py'
    with open(file_name,'rb') as file:
        attach_file = MIMEBase('application', 'octet-stream',filename=file_name)
        attach_file.add_header('Content-Disposition', 'attachment', filename=file_name + '1')
        attach_file.set_payload(file.read())
        encoders.encode_base64(attach_file)
        msg.attach(attach_file)

    #以MIMEApplication添加附件
    with open(file_name, 'rb') as file:
        attach_file = MIMEApplication(file.read())
        attach_file.add_header('Content-Disposition', 'attachment', filename=file_name+ '2')
        encoders.encode_base64(attach_file)
        msg.attach(attach_file)

    email_server = smtplib.SMTP(smtp_server, 465)
    #加密SMTP
    email_server.starttls()

    email_server.set_debuglevel(1)
    email_server.login(from_addr, password)
    email_server.sendmail(from_addr, [to_addr], msg.as_string())

    email_server.quit()


if __name__ == '__main__':
    main()
