#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pickle

__author__ = 'Mr.Huo'
picFileName = 'pick'

def main():
    dp= {'huo' : 3, 'shao' : 4, 'hua' : 3}
    try:
        pick_file = open(picFileName, 'xb')
        pickle.dump(dp, pick_file)
        print(pick_file.tell())
        pick_file = open(picFileName, 'rb')
        d1 = pickle.load(pick_file)
        print(d1)
    except FileExistsError:
        pick_file = open(picFileName, 'r+b')
        try:
            d1 = pickle.load(pick_file)
            print(d1)
        except EOFError:
            pickle.dump(dp, pick_file)
            print(pick_file.tell())
            d1 = pickle.load(pick_file)
            print(d1)
    finally:
        if pick_file:
            pick_file.close()


if __name__ == '__main__':
    main()
