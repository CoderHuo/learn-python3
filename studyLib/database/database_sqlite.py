#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

__author__ = 'Mr.Huo'


def main():
    my_sqlite_conn = sqlite3.connect('mySQLite3.db')
    cursor = my_sqlite_conn.cursor()
    try:
        cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
        cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
    except sqlite3.OperationalError as err:
        print(err)
    print(cursor.rowcount)
    #cursor.close()
    my_sqlite_conn.commit()
    cursor.execute('select * from user where id=?', ('1',))
    values  = cursor.fetchall()
    print(values)
    cursor.close()
    my_sqlite_conn.close()

if __name__ == '__main__':
    main()