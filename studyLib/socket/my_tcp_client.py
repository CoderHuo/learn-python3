#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import time
from network_setting import *

__author__ = 'Mr.Huo'
buff_size = 2048


def main():
    client = socket.socket()
    client.connect(TcpSerAddr)
    send_data1 = [b'111111', b'2ashxao\r\n', b'3bhaua\r\n']
    print(client.getpeername())
    while True:
        for data in send_data1:
            client.send(data)
            print(client.recv(1024))
            time.sleep(1)
    client.close()


if __name__ == '__main__':
    main()
