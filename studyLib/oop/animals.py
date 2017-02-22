#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Mr.Huo'


# 继承
class Animal(object):
    def __init__(self, name='Animal'):
        self.__name = name

    def get_name(self):
        return self.__name

    def run(self):
        print(self.get_name(), "is running")


class Dog(Animal):
    def __init__(self, name='Dog'):
        self.__name = name

    def get_name(self):
        return self.__name


class Cat(Animal):
    def __init__(self, name='Cat'):
        self.__name = name

    def get_name(self):
        return self.__name


def run(Animal):
    Animal.run()


def main():
    dog = Dog()
    cat = Cat()
    dog.run()
    cat.run()
    run(dog)
    run(cat)

    # 判断对象类型，使用type()函数
    print('Dog type', type(dog))
    # isinstance() 判断
    print(isinstance(dog, Dog))
    print(isinstance(dog, Animal))
    print(isinstance(dog, (Animal, Dog, Cat)))
    # dir() 获取一个对象的所有属性和方法
    print(dir(dog))
    # 类似__xxx__的属性和方法在Python中都是有特殊用途的，
    # 比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，
    # 实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
    print(len('ABC'))
    print('ABC'.__len__())
    # getattr()、setattr()以及hasattr()操作一个对象的状态
    print(hasattr(dog, 'get_name'))
    print(setattr(dog, 'name', 'Dog'))
    print(getattr(dog, 'name'))


if __name__ == '__main__':
    main()
