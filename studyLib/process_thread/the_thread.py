#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, time, random
import threading

__author__ = 'Mr.Huo'


def run_thread(*args, **kwargs):
    start_time = time.time()
    print('Task %2s>>> I am child process ID:%5s. \
    My parent process ID:%5s' % \
          (threading.current_thread().name,os.getpid(), os.getppid()))
    # time.sleep(random.random() * 3)
    time.sleep(1)
    end_time = time.time()
    print('Task %2s>>> runs %f seconds.' % (threading.current_thread().name, (end_time - start_time)))


def main():
    pid = os.getpid()
    print(pid)
    proc = threading.Thread(target=run_thread, args=('hi', 'hello'))
    print('Child process will start...')
    proc.start()
    # join()方法可以等待子进程结束后再继续往下运行
    proc.join()
    print('Child process end')


if __name__ == '__main__':
    main()
