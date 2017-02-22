#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Mr.Huo'


class People(object):
    # __xxx__ 特殊变量，非私有变量
    def __init__(self, sex='Male'):
        # 私有变量 __ 开始,python实际是修改变量名为 _ClassName__XXX,实际还是可以通过这个访问
        self.__sex = sex


def main():
    # 面向对象最重要的概念就是类（Class）和实例（Instance），
    # 必须牢记类是抽象的模板，比如Student类，而实例是根据类创建出来的一个个具体的“对象”，
    # 每个对象都拥有相同的方法，但各自的数据可能不同
    man = People()
    print(man)
    # 可以自由地给一个实例变量绑定属性
    man.sex = 'Male1'
    man.__sex = 'Male2'
    print(man.sex)
    print(man._People__sex)
    print(man.__sex)
    print(dir(man))


if __name__ == '__main__':
    main()
