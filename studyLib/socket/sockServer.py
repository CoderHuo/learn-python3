#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from network_setting import *
from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

__author__ = 'Mr.Huo'

TcpSerAddr = (LOCALIP, TCP_PORT_S)


class MyRequestHandler(SRH):
    def handle(self):
        print('...connect from:', self.client_address)
        flag = True
        while flag:
            data = self.rfile.readline()
            print(type(data))
            if not data or b'ByeBye' in data:
                flag = False
            print(data)
            self.wfile.write(('[%s] %s' % (ctime(), data.decode("UTF-8"))).encode("UTF-8"))


def main():
    # TCPServer，IO多路复用，但是StreamRequestHandler还是同步阻塞IO
    # 同步阻塞IO、同步非阻塞IO、IO多路复用、异步IO
    tcpServ = TCP(TcpSerAddr, MyRequestHandler)
    print('waiting for connection...')
    tcpServ.serve_forever()


if __name__ == '__main__':
    main()
