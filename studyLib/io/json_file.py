#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os

__author__ = 'Mr.Huo'
jsonFileName = 'jsonFile.txt'

def main():
    dp= {'huo' : 3, 'shao' : 4, 'hua' : 3}
    try:
        json_file = open(jsonFileName, 'xt')
        json.dump(dp, json_file)
        json_file = open(jsonFileName, 'rt')
        d1 = json.load(json_file)
        print(d1)
    except FileExistsError:
        json_file = open(jsonFileName, 'r+t')
        try:
            d1 = json.load(json_file)
            print(d1)
        except Exception as err:
            print(err)
            json.dump(dp, json_file)
            json_file.seek(0)
            d1 = json.load(json_file)
            print(d1)
    finally:
        if json_file:
            json_file.close()


if __name__ == '__main__':
    main()
