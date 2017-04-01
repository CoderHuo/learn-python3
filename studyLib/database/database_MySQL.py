#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector

__author__ = 'Mr.Huo'


def main():
    mysql_user = 'root'
    mysql_password = input("Password:")
    mysql_host = '127.0.0.1'
    mysql_database = 'world'
    # 创建MYSQL连接
    mysql_conn = mysql.connector.connect(user=mysql_user, password=mysql_password)
    # 创建游标
    mysql_cursor = mysql_conn.cursor()
    # 创建数据库
    mysql_cursor.execute('CREATE database test')
    # 选择要操作的数据库
    mysql_cursor.execute('use test')
    # 新建一个表
    mysql_cursor.execute('CREATE TABLE user (id VARCHAR(20) PRIMARY KEY, name VARCHAR(20))')
    # 增加数据
    mysql_cursor.execute("INSERT INTO user (id, name) VALUES ('1', 'Michael')")
    print(mysql_cursor.rowcount)
    # 提交数据
    mysql_conn.commit()
    # 查询数据
    mysql_cursor.execute('select * from user where id = %s', ('1',))
    values = mysql_cursor.fetchall()
    print(values)
    # 删除数据库表
    mysql_cursor.execute("drop table user")
    # 删除数据库
    mysql_cursor.execute("drop database test")
    mysql_conn.commit()
    # 关闭游标
    mysql_cursor.close()
    # 关闭连接
    mysql_conn.close()


if __name__ == '__main__':
    main()
