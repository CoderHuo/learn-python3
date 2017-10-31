#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = 'Mr.Huo'


class Dog():
    def __init__(self, name="sun"):
        self.name = name

    def __getattr__(self, item):
        print("call on:%s from __getattr__" % (item))
        if hasattr(self, item):
            return getattr(self, item)
        else:
            print("error")
            return None

    def __setattr__(self, key, value):
        print("call on:%s from __setattr__" % (key))
        return object.__setattr__(self, key, value)
        pass

    #def __getattribute__(self, item):
    #    print("call on:%s from __getattribute__" % (item))
    #    return object.__getattribute__(self, item)


def main():
    dog = Dog("dog")
    print('-' * 30)
    print(dog.name)
    #dog.weight = 100
    print(dog.weight)
    pass


if __name__ == '__main__':
    main()
