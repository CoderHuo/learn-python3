#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import multiprocessing,time
__author__ = 'Mr.Huo'

repertory = multiprocessing.Queue(100)
rep_len =100

def prodece(rep):
    while True:
        if rep.full() == False:
            time.sleep(1)
            rep.put("A")
            print('prodece  %d'%(rep.qsize()))
        else:
            print('full')
            time.sleep(30)
            break
            #continue 进程检测到不满时又可以生产
            #continue

def customer(rep):
    while True:
        if rep.empty() == False:
            time.sleep(2)
            rep.get()
            print('customer %d'%(rep.qsize()))
        else:
            print('empty')
            time.sleep(20)
            break
            #continue

def main():
    prodece1 = multiprocessing.Process(target=prodece,args=(repertory,))
    prodece2 = multiprocessing.Process(target=prodece,args=(repertory,))
    customer1 = multiprocessing.Process(target=customer,args=(repertory,))
    customer2 = multiprocessing.Process(target=customer,args=(repertory,))
    prodece1.start()
    prodece2.start()
    time.sleep(2)
    customer1.start()
    customer2.start()
    prodece1.join()
    prodece2.join()
    customer1.join()
    customer1.join()


if __name__ == '__main__':
    main()