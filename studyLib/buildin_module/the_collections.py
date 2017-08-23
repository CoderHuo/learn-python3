#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import namedtuple, deque, defaultdict, OrderedDict,Counter

__author__ = 'Mr.Huo'


class FIFO_OrderDict(OrderedDict):
    def __init__(self, capacity):
        super().__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        else:
            if containsKey:
                del self[key]
                print('set:', (key, value))
            else:
                print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


def main():
    # namedtuple 是一个函数，它用来创建一个自定义的tuple对象，可以根据属性来引用，具备tuple的不变性
    Point = namedtuple('Point', ['x', 'y'])
    p1 = Point(1, 2)
    print(p1.x, p1.y, type(p1))
    print(isinstance(p1, Point))
    print(isinstance(p1, tuple))
    Student = namedtuple('Student','name classNum sex')
    std1 = Student("擎天柱",0,'F')
    print(std1)
    print(std1._asdict())

    # deque，list存储数据，按索引访问元素很快，但是插入和删除很慢，list是线性存储
    # deque 高效的实现插入和删除的双向链表，适用于队列
    que = deque((1, 2))
    que.append(3)
    que.appendleft(0)
    print(que)

    # 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
    dd = defaultdict(lambda: "N/A")
    dd['key1'] = 'a'
    print(dd['key1'])
    print(dd['key2'])

    # OrderedDict key顺序确定的dict,Key会按照插入的顺序排列
    od = OrderedDict(dd)
    print(od)
    od['key0'] = 'c'
    print(list(od.keys()))

    fd1 = FIFO_OrderDict(4)
    fd1['key1'] = 1
    fd1['key2'] = 1
    fd1['key3'] = 1
    fd1['key3'] = 2
    fd1['key4'] = 2
    fd1['key5'] = 2
    print(fd1)

    #Counter 计数器
    c = Counter()
    for ch in "python programing":
        c[ch] = c[ch]+1

    print(c)

    word  = "python programing"
    x = {x:word.count(x) for x in word}
    print(x)

if __name__ == '__main__':
    main()
