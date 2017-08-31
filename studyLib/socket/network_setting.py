#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

__author__ = 'Mr.Huo'

LOCALIP = socket.gethostbyname(socket.gethostname())
UDP_PORT_S = 10000
UDP_PORT_C = 10002
TCP_PORT_S = 20000
TCP_PORT_C = 20002

TcpSerAddr = (LOCALIP, TCP_PORT_S)
TcpCliAddr = (LOCALIP, TCP_PORT_C)
UdpSerAddr = (LOCALIP, UDP_PORT_S)
UdpCliAddr = (LOCALIP, UDP_PORT_C)