#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

__author__ = 'Mr.Huo'



def main():
    server_addr = ('146.11.22.128', 9999)
    client = socket.socket()
    client.connect(server_addr)
    send_data1 = [b'aheuo', b'ashxao', b'bhaua']
    print(client.recv(1024))
    for data in send_data1:
        client.send(data)
        print(client.recv(1024).decode())
    client.send(b'exit')
    client.close()
    pass


if __name__ == '__main__':
    main()
