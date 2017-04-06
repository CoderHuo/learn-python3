#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Mr.Huo'

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    #c.send(None)
    c.__next__()
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


    def countdown(n):
        print("Counting down from", n)
        while n >= 0:
            newvalue = (yield n)
            # If a new value got sent in, reset n with it
            if newvalue is not None:
                print(111)
                n = newvalue
            else:
                n -= 1


    # The holy grail countdown
    c = countdown(5)
    for x in c:
        print(x)
        if x == 5:
            print(c.send(None))