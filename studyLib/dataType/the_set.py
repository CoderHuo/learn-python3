#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Mr.Huo'


def main():
    # set() 元素是唯一的，无序的集合
    # 一个{}里面放一些元素就构成了一个集合，set里面可以是多种数据类型（但不能是列表，集合，字典，可以是元组）
    t1 = (1, 2, 3)
    l1 = [11, 22, 33]
    d1 = {1: 'H', 2: 'S', 3: 'H'}
    str1 = 'huoshaohua'
    s1 = {'s1', t1}
    print(s1)
    try:
        se2 = {'s1', l1}
    except Exception as err:
        print(err)
    try:
        se3 = {'s1', d1}
    except Exception as err:
        print(err)
    try:
        se4 = {'s1', s1}
    except Exception as err:
        print(err)
    # 集合创建 set(x),x= list tuple,or string
    s2 = set(t1)
    print('create set from tuple      :', s2)
    s3 = set(l1)
    print('create set from list       :', s3)
    # 从字典创建集合，不指定键值，则以键来创建
    s4 = set(d1)
    print('create set from dict       :', s4)
    s5 = set(d1.keys())
    print('create set from dict keys  :', s5)
    s6 = set(d1.values())
    print('create set from dict values:', s6)
    s7 = set(str1)
    print('create set from string     :', s7)

    # set 基本函数与操作
    # s.add(x) 将元素x添加到集合s中，若重复则不进行任何操作
    set1 = {'huo', 'shao', 'hua'}
    set1.add('&')
    print('set.add(x)    :', set1)
    # s.update(x)将集合x并入原集合s中，x可以是元组、列表、字典，可以有多个
    set1.update(t1, l1, d1, d1.values())
    print('set.update(x) :', set1)
    # s.discard(x),将X从集合s中移除，不存在不会引发错误
    set1.discard(1)
    print('set.discard(x):', set1)
    # s.remove(x),将X从集合s中移除，不存在会引发错误
    try:
        set1.remove(1)
    except Exception as err:
        print('set.remove(x) err:', err)
    # s.pop() 随机移除一个值
    pop1 = set1.pop()
    print('set pop()     :', pop1)
    print('set.pop()     :', set1)
    pop2 = set1.pop()
    print('set pop()     :', pop2)
    print('set.pop()     :', set1)
    # clear()清空
    # x in s set支持in 操作
    print('x in s set    :', pop1 in set1)
    # s.union(x) 返回s与集合x的并集，不改变s，x可以是元组、列表、字典、字符串(当做set(str))
    str2 = 'liuzhixuan'
    set2 = set1.union(str2)
    print('union new set :', set2)
    print('union old set :', set1)
    # s.difference(x)返回在集合s中而不在集合x中的元素的集合，不改变集合s，x也可以是列表，元组，字典。
    set3 = set2.difference(set1)
    print('difference new set :', set3)
    #symmetric_difference(x) 返回s和集合x的对称差集，即只在其中一个集合中出现的元素，不改变集合s，x也可以是列表，元组，字典
    set4=set3.symmetric_difference(set2)
    print('symmetric_difference new set :', set4)

if __name__ == '__main__':
    main()
