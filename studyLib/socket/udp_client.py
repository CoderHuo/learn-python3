#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import network_setting as nt
import socket

__author__ = 'Mr.Huo'


def main():
    """UDP client"""
    udp_server_addr = (nt.LOCALIP, nt.UDP_PORT_S)
    udp_client_addr = (nt.LOCALIP, nt.UDP_PORT_C)
    udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_client.bind(udp_client_addr)
    data = [b'haha', b'hehe', b'xixi']
    for d in data:
        udp_client.sendto(d, udp_server_addr)
        print('client receive data=(%s) from serveraddr=%s' % (udp_client.recv(1024).decode('utf-8'), udp_server_addr))

    while True:
        send_data = input("input the send data:")
        udp_client.sendto(send_data.encode(), udp_server_addr)
        recv_data, recv_addr = udp_client.recvfrom(1024)
        print('client receive data=(%s) from serveraddr=%s' % (recv_data.decode('utf-8'), recv_addr))
        if recv_data == b'ByeBye!':
            break
    udp_client.close()


if __name__ == '__main__':
    main()
