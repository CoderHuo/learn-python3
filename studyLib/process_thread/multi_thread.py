#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from threading import Thread
import multiprocessing
import time

__author__ = 'Mr.Huo'


def counter():
    i = 0
    for _ in range(100000000):
        i += 1
    return True


def main():
    # GIL的存在，多线程并不能正真的实现并发
    thread_array = {}
    start_time = time.time()
    for tid in range(2):
        t = Thread(target=counter)
        t.start()
        thread_array[tid] = t

    for i in range(2):
        thread_array[i].join()

    end_time = time.time()
    print("Total time: {}".format(end_time - start_time))

    # 多进程
    mp = multiprocessing.Pool()
    mp_start = time.time()
    for i in range(2):
        mp.apply_async(counter)
    mp.close()
    mp.join()
    mp_end = time.time()
    print("Total time: {}".format(mp_end - mp_start))


if __name__ == '__main__':
    main()
