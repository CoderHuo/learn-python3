#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os

__author__ = 'Mr.Huo'
# json 类型 {} [] "string" 1234.56 true/false nul
jsonDictName = 'jsonDict.txt'
jsonClassName = 'jsonClass.txt'


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def student2json(std):
        return {'name': std.name, 'age': std.age}


def main():
    dp = {'huo': 3, 'shao': 4, 'hua': 3}
    std1 = Student('shaohua', '1818')
    try:
        json_file = open(jsonDictName, 'xt')
        json.dump(dp, json_file)
        json_file = open(jsonDictName, 'rt',encoding='utf-8')
        d1 = json.load(json_file)
        print("D1",d1)
    except FileExistsError:
        json_file = open(jsonDictName, 'r+t')
        try:
            d1 = json.load(json_file)
            print("D2",d1)
        except Exception as err:
            print(err)
            json.dump(dp, json_file)
            json_file.seek(0)
            d1 = json.load(json_file)
            print("D3",d1)
    finally:
        if json_file:
            json_file.close()


            # try:
            #     json_file = open(jsonClassName, 'xt')
            #     json.dump(std1, json_file,default=student2json)
            #     json_file = open(jsonClassName, 'rt')
            #     d2 = json.load(json_file,object_hook=student2json)
            #     print(d2)
            # except FileExistsError:
            #     json_file = open(jsonClassName, 'r+t')
            #     try:
            #         d1 = json.load(json_file)
            #         print(d2)
            #     except Exception as err:
            #         print(err)
            #         json.dump(std1, json_file)
            #         json_file.seek(0)
            #         d1 = json.load(json_file)
            #         print(d2)
            # finally:
            #     if json_file:
            #         json_file.close()


if __name__ == '__main__':
    main()
