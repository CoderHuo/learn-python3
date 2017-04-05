#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Mr.Huo'

def consumer():
    print('3333')
    r = ''
    while True:
        print('4444')
        n = yield r
        print('5555')
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    print('1111')
    c.send(None)
    print('2222')
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


def main():
    c = consumer()
    produce(c)


if __name__ == '__main__':
    main()