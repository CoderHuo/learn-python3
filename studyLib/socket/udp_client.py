#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import network_setting as nt
import socket

__author__ = 'Mr.Huo'


def main():
    """UDP client"""
    udp_addr = (nt.LOCALIP, nt.UDP_PORT)
    udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = [b'haha', b'hehe', b'xixi',b'exit']
    for d in data:
        udp_client.sendto(d,udp_addr)
        print('client receive data=(%s) from serveraddr=%s'%(udp_client.recv(1024).decode('utf-8'),udp_addr))

    udp_client.close()


if __name__ == '__main__':
    main()
