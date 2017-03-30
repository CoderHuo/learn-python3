#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket, threading, time,multiprocessing

__author__ = 'Mr.Huo'


def client_read(client):
    """客户端接收数据"""
    buffer = []
    while True:
        data = client.recv(1024)
        if data:
            buffer.append(data)
        else:
            break
    data = b''.join(buffer)
    return data


def my_tcplink(sock, addr):
    """服务端处理连接"""
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        print('server recv',data.decode())
        time.sleep(0.1)
        if not data or data == b'exit':
            sock.send(b'ByeBye!')
            break
        sock.send(b'Hello, %s!' % data)
    sock.close()
    print('Connection from %s:%s closed.' % addr)


def my_server(server_addr):
    # 服务端
    print(type(server_addr),server_addr)
    server = socket.socket()
    server.bind(server_addr)
    server.listen(5)
    print('Waiting for connection...')
    while True:
        sock, addr = server.accept()
        t = threading.Thread(target=my_tcplink, args=(sock, addr))
        t.start()


def my_client(server_addr,senddata):
    # 客户端
    client = socket.socket()
    client.connect(server_addr)
    print(client.recv(1024))
    for data in senddata:
        client.send(data)
        print(client.recv(1024).decode())
    client.send(b'exit')
    client.close()


def main():
    # 客户端tcp
    client = socket.socket()
    # 连接
    client.connect(('www.sina.com.cn', 80))
    # 发送
    client.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
    # 接收数据
    data = client_read(client)
    # 数据处理
    header, html = data.split(b'\r\n\r\n', 1)
    #print(header.decode())
    #print(html.decode())
    with open('sina.html', 'wb') as sina:
        sina.write(html)
    # 关闭连接
    client.close()

    server_addr = ('146.11.22.128', 9999)
    send_data1 = [b'aheuo',b'ashxao',b'bhaua']
    send_data2 = [b'aheuo',b'ashxao',b'bhaua']
    send_data3 = [b'aheuo',b'ashxao',b'bhaua']

    server_proc = multiprocessing.Process(target=my_server,args=(server_addr,))
    client_proc1 = multiprocessing.Process(target=my_client,args=(server_addr,send_data1))
    client_proc2 = multiprocessing.Process(target=my_client,args=(server_addr,send_data2))
    client_proc3 = multiprocessing.Process(target=my_client,args=(server_addr,send_data3))
    server_proc.start()
    client_proc1.start()
    client_proc2.start()
    client_proc3.start()
    server_proc.join()
    client_proc1.join()
    client_proc2.join()
    client_proc3.join()


if __name__ == '__main__':
    main()
