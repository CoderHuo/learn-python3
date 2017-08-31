#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import selectors, socket
from time import ctime
from network_setting import *

__author__ = 'Mr.Huo'

sel = selectors.DefaultSelector()


def accept(sock, mask):
    conn, addr = sock.accept()
    print('Accept %s from %s' % (conn, addr))
    #conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)


def read(conn, mask):
    data = conn.recv(1000)
    if data:
        print('Recv data from [%s]. Data is [%s]' % (conn.getpeername(), data))
        #send_data = ('[' + ctime() + '] ').encode() + data
        send_data = data
        try:
            conn.sendall(send_data)
        except BlockingIOError:
            print('10035')
    else:
        print('Closing ', conn)
        sel.unregister(conn)
        conn.close()


def main():
    sock = socket.socket()
    sock.bind(TcpSerAddr)
    sock.listen(100)
    sock.setblocking(False)
    sel.register(sock, selectors.EVENT_READ, accept)

    while True:
        events = sel.select()
        print(events)
        for key, mask in events:
            callback = key.data
            callback(key.fileobj,mask)


if __name__ == '__main__':
    main()
