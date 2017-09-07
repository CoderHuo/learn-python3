#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from threading import Thread, current_thread, Lock
import multiprocessing
import time

__author__ = 'Mr.Huo'


def counter():
    i = 0
    for _ in range(100000000):
        i += 1
    print(i)
    return True


num = 0

lock = Lock()


def add():
    global num
    for i in range(1000000):
        lock.acquire()
        num += 1
        lock.release()
    print(num, current_thread().name)


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
    process_array = list()
    process_start = time.time()
    for pid in range(2):
        proc = multiprocessing.Process(target=counter)
        proc.start()
        process_array.append(proc)
    for i in range(len(process_array)):
        process_array[i].join()

    process_end = time.time()
    print("Total time: {}".format(process_end - process_start))

    # 多进程 Pool
    mp = multiprocessing.Pool()
    mp_start = time.time()
    for i in range(2):
        mp.apply_async(counter)
    mp.close()
    mp.join()
    mp_end = time.time()
    print("Total time: {}".format(mp_end - mp_start))

    add_array = {}
    for tid in range(10):
        add_thread = Thread(target=add)
        add_thread.start()
        add_array[tid] = add_thread

    for tid in range(len(add_array)):
        add_array[tid].join()

    print(num)


if __name__ == '__main__':
    main()
