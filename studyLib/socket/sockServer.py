#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from network_setting import *
from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime
import selectors

__author__ = 'Mr.Huo'

TcpSerAddr = (LOCALIP, TCP_PORT_S)


class MyRequestHandler(SRH):
    def handle(self):
        print("self.connection:",self.connection)
        print("type of self.connection:",type(self.connection))
        print('...connect from:', self.client_address)
        flag = True
        while flag:
            data = self.rfile.readline()
            if not data or b'ByeBye' in data:
                flag = False
            print("CLIENT:%s RECEIVE DATA:%s"%(self.client_address,data))
            self.wfile.write(('[%s] %s' % (ctime(), data.decode("UTF-8"))).encode("UTF-8"))


def main():
    # TCPServer，IO多路复用，但是StreamRequestHandler还是同步阻塞IO
    # 同步阻塞IO、同步非阻塞IO、IO多路复用、异步IO
    with TCP(TcpSerAddr, MyRequestHandler) as tcpServ:
        print(tcpServ.fileno())
        with selectors.SelectSelector() as selector:
            key = selector.register(tcpServ,selectors.EVENT_READ)
            ready = selector.select()
            print(ready)
            fd = selector._fileobj_lookup(tcpServ)
            fd1 = selectors._fileobj_to_fd(tcpServ)
            print(tcpServ.fileno())
            print(selector,type(selector))
            print(key)
            print(fd)
            print(fd1)
            print(selector._fd_to_key)
        print('waiting for connection...')
        tcpServ.serve_forever()


if __name__ == '__main__':
    main()
