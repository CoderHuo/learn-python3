#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

__author__ = 'Mr.Huo'



def main():
    server_addr = ('146.11.22.166', 20000)
    client = socket.socket()
    client.connect(server_addr)
    send_data1 = [b'1aheuo\r\n', b'2ashxao\r\n', b'3bhaua\r\n']
    print(client.getpeername())
    for data in send_data1:
        client.send(data)
        print(client.recv(1024))
    client.send(b'exit\r\n')
    client.close()
    pass


if __name__ == '__main__':
    main()
