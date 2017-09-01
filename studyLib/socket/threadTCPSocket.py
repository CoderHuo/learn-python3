#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
import socket,time
import socketserver
from network_setting import *

__author__ = 'Mr.Huo'


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class ThreadedTCPRequsetHandler(socketserver.BaseRequestHandler):
    def handle(self):
        flag = True
        try:
            while flag:
                data = str(self.request.recv(1024), 'ascii')
                if not data:
                    flag = False
                cur_thread = threading.current_thread()
                response = bytes('{}: {}'.format(cur_thread, data), 'ascii')
                print("Send: {}".format(response))
                self.request.sendall(response)
        except WindowsError as winErr:
            print(winErr)
        finally:
            print('Closing ', self.request)
            self.request.close()


def client(addr, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(addr)
        sock.sendall(bytes(message, 'ascii'))
        response = str(sock.recv(1024), 'ascii')
        print("Received: {}".format(response))


def main():
    tcpServer = ThreadedTCPServer(TcpSerAddr, ThreadedTCPRequsetHandler)
    try:
        tcpServer_thread = threading.Thread(target=tcpServer.serve_forever)
        tcpServer_thread.daemon = True
        tcpServer_thread.start()
        print("Server loop running in thread:", tcpServer_thread.name)

        client(TcpSerAddr, 'Hello World 1')
        client(TcpSerAddr, 'Hello World 2')
        client(TcpSerAddr, 'Hello World 3')
        #tcpServer_thread.join()
        while True:
            print(threading.active_count(),threading.enumerate())
            time.sleep(1)
    except Exception as err:
        print(err)
    finally:
        tcpServer.shutdown()


if __name__ == '__main__':
    main()
