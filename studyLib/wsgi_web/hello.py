#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Mr.Huo'

def application(environ,start_respone):
    start_respone('200 OK',[('Content-Type', 'text/html')])
    for key,value in environ.items():
        print("%-30s  = %s"%(key,value))
    return [b'<h1>Hello, web!</h1>']



def main():
    pass


if __name__ == '__main__':
    main()