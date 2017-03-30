#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import network_setting as nt

__author__ = 'Mr.Huo'


def main():
    """UDP server"""
    udp_server_addr = (nt.LOCALIP, nt.UDP_PORT_S)
    udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_server.bind(udp_server_addr)
    print('Bind UDP on %d...' % nt.UDP_PORT_S)
    while True:
        data, addr = udp_server.recvfrom(1024)
        print('server receive data=(%s) from %s' % (data.decode(), addr))
        if data != b'exit':
            udp_server.sendto(b'Hello %s' % data, addr)
        elif data == b'exit':
            udp_server.sendto(b'ByeBye!', addr)
            break

    print('END')
    udp_server.close()


if __name__ == '__main__':
    main()
