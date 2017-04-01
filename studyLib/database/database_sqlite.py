#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

__author__ = 'Mr.Huo'


def main():
    my_sqlite_conn = sqlite3.connect('mySQLite3.db')
    # 创建一个游标，类似句柄
    cursor = my_sqlite_conn.cursor()
    # execute() 执行一条SQL语句
    try:
        cursor.execute('CREATE TABLE user (id VARCHAR(20) PRIMARY KEY, name VARCHAR(20))')
    except sqlite3.OperationalError as err:
        print(err)
    for i in range(10):
        try:
            cursor.execute("INSERT INTO user (id, name) VALUES ('{:d}', 'Michael{:d}')".format(i, i))
        except sqlite3.IntegrityError as err:
            print(err)
    #executemany("")--执行多条sql语句
    try:
        values = [('11', 'Michael11'), ('12', 'Michael12')]
        cursor.executemany("INSERT INTO user (id, name) VALUES (?,?)", values)
    except sqlite3.IntegrityError as err:
        print(err)
    # 游标的rowcount作用？
    print(cursor.rowcount)
    # 提交修改
    my_sqlite_conn.commit()
    # 查询结果
    cursor.execute('SELECT * FROM user')
    print(cursor.rowcount)
    # fetchone() --从结果中取一条记录，并将游标指向下一条记录
    values = cursor.fetchone()
    print(values)
    # fetchmany()--从结果中取多条记录，并将游标指向下N条记录
    values = cursor.fetchmany(5)
    print(values)
    # fetchall() --从结果中取出所有记录（游标位置开始到结束）
    values = cursor.fetchall()
    print(values)

    cursor.close()
    my_sqlite_conn.close()


if __name__ == '__main__':
    main()
