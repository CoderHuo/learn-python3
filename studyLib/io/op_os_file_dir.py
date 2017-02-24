#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

__author__ = 'Mr.Huo'


def main():
    print("System name: ", os.name)
    # NT system do not support name()
    try:
        print("System Detail: ", os.uname())
    except Exception as err:
        print(err)
    # system environ
    print("System Environ: ", type(os.environ))
    print("System Environ: ", os.environ)
    env_var = dict(os.environ)

    print("System Environ:", env_var)
    for key in os.environ.keys():
        print('%25s = %s' % (key, os.environ.get(key)))

    print("-----System file operator-----")
    print("Current Dir:",os.path.abspath('.'))
    #create dir,if dir is exist create fail
    testdir=os.path.join(os.path.abspath('.'), 'testdir')
    print(testdir)
    try:
        os.mkdir(testdir)
        os.rmdir(testdir)
    except FileExistsError :
        os.rmdir(testdir)

if __name__ == '__main__':
    main()
