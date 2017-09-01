#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import selectors, socket
from time import ctime
from network_setting import *

__author__ = 'Mr.Huo'

sel = selectors.DefaultSelector()
buff_size = 1024

def accept(sock, mask):
    conn, addr = sock.accept()
    print('Accept %s from %s' % (conn, addr))
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)


def read(conn, mask):
    try:
        data = conn.recv(buff_size)
        if data:
            print('Recv data from [%s]. Data is [%s]' % (conn.getpeername(), data))
            send_data = data
            try:
                conn.sendall(send_data)
            except BlockingIOError:
                print('10035')
        else:
            print('Closing ', conn)
            sel.unregister(conn)
            conn.close()
    except WindowsError as winErr:
        if winErr.errno == 10054:
            print(winErr)
            sel.unregister(conn)


def main():
    sock = socket.socket()
    sock.bind(TcpSerAddr)
    sock.listen(100)
    sock.setblocking(False)
    sel.register(sock, selectors.EVENT_READ, accept)

    while True:
        events = sel.select()
        print('Event:', events)
        for key, mask in events:
            callback = key.data
            callback(key.fileobj, mask)


if __name__ == '__main__':
    main()
