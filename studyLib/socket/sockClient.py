#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket, threading, multiprocessing
from network_setting import *
from time import ctime

__author__ = 'Mr.Huo'

TcpSerAddr = (LOCALIP, TCP_PORT_S)
TcpCliAddr = (LOCALIP, TCP_PORT_C)


class MyTcpClient():
    def __init__(self, client_address, server_address, buff=1024, bind=True):
        self.client_address = client_address
        self.server_address = server_address
        self.socket = socket.socket()
        self.recvdata = None
        self.buff = buff
        if bind:
            try:
                self.socket.bind(self.client_address)
            except:
                self.socket.close()
                raise
        try:
            self.socket.connect(self.server_address)
        except:
            self.socket.close()
            raise

    def handle(self, send_data):
        pass

    def client_actions(self, send_data):
        self.socket.send(send_data.encode('utf-8') + b'\r\n')
        try:
            self.recvdata = self.socket.recv(self.buff)
        except Exception as err:
            print(err)
            self.shutdown()
        finally:
            print('Server Send: %s' % (self.recvdata.decode('utf-8')))

    def shutdown(self):
        self.socket.close()


def main():
    tcpClie = MyTcpClient(TcpCliAddr, TcpSerAddr)
    while True:
        send_data = input('input the send data to server:')
        tcpClie.client_actions(send_data)
        if b'ByeBye' in tcpClie.recvdata or not tcpClie.recvdata:
            break
    tcpClie.shutdown()


if __name__ == '__main__':
    main()
