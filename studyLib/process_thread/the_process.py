#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, time, random
import multiprocessing

__author__ = 'Mr.Huo'


def run_proc(*args, **kwargs):
    start_time = time.time()
    print('Task %2s>>> I am child process ID:%5s. My parent process ID:%5s' % (args[0], os.getpid(), os.getppid()))
    # time.sleep(random.random() * 3)
    time.sleep(1)
    end_time = time.time()
    print('Task %2s>>> runs %f seconds.' % (args[0], (end_time - start_time)))


def main():
    pid = os.getpid()
    print(pid)
    proc = multiprocessing.Process(target=run_proc, args=('hi', 'hello'))
    print('Child process will start...')
    proc.start()
    # join()方法可以等待子进程结束后再继续往下运行
    proc.join()
    print('Child process end')
    print("cpu count:", os.cpu_count())
    # 批量生成进程
    for j in range(1, 17):
        print('|------------------------------------------------------------------|')
        # Poll对象创建进程 默认cpu数为电脑cpu数.
        # 如果设置的数大于电脑cpu数？
        mp = multiprocessing.Pool()
        mp_start = time.time()
        for i in range(j):
            mp.apply_async(run_proc, args=(i,))
        print('Waiting for all subprocesses done...')
        # 对Pool对象调用join()方法会等待所有子进程执行完毕
        # 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process
        mp.close()
        mp.join()
        mp_end = time.time()
        print('All subprocesses done. TOTLE TIME=%f seconds.' % (mp_end - mp_start))


if __name__ == '__main__':
    main()
