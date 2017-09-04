#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from threading import Thread
import time

__author__ = 'Mr.Huo'


def counter():
    i = 0
    for _ in range(100000000):
        i += 1
    return True


def main():
    thread_array = {}
    start_time = time.time()
    for tid in range(2):
        t = Thread(target=counter)
        t.start()
        t.join()

    end_time = time.time()
    print("Total time: {}".format(end_time - start_time))

if __name__ == '__main__':
    main()
