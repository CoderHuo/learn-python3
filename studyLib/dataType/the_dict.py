#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Mr.Huo'


def main():
    # python字典一种无序存储结构，存储的是键值对 key - value，键是唯一的不重复的，值可以不唯一
    # 通过包含键值的列表创建
    l = [('hello', 3), ('world1', 4), ('world2', 3)]
    d1 = dict(l)
    print("通过包含键值的列表创建d1:%s" % d1)
    # 通过包含键值的元组创建
    t = tuple(l)
    d2 = dict(t)
    print("通过包含键值的元组创建d2:%s" % d2)
    # 通过关键字参数创建
    d3 = dict(hello=3, world1=4, world2=3)
    print("通过关键字参数创建    d3:%s" % d3)
    # fromkeys(S [ , v]) 创建字典：已存在的 d.fromkeys(S [ , v]),或者dict.fromkeys(S [ , v]),或者{}.fromkeys(S [ , v])
    # 已存在的 d.fromkeys(S [ , v])创建新的dict，不改变原有dict
    keys = ['hello', 'world1', 'world2']
    d4 = d3.fromkeys(keys)
    print("通过d.fromkeys创建    d4:%s" % d4)
    d5 = dict.fromkeys(keys, '606')
    print("通过dict.fromkeys创建 d5:%s" % d5)
    d6 = {}.fromkeys(keys, '866')
    print("通过{}.fromkeys创建   d6:%s" % d6)
    # 字典推导式
    words = "letters"
    word_count = {letter: words.count(letter) for letter in set(words)}
    # 字典是无序的，所以不能通过索引来获取值，要通过键来找到关联值
    print(word_count)
    # 可以通过dict的items()、keys()、values()获取相应值，构造list、tuple
    print(word_count.items())
    print(word_count.keys())
    print(word_count.values())

    for key, value in word_count.items():
        print('dict: key=%-3s,value=%-3s' % (key, value))
    # 字典操作
    # len(d)返回字典d里面的键值对数目
    print('dict length：%5d' % len(word_count))
    # x in d查询字典d中是否有键 x
    print('hello' in word_count)
    print(word_count)
    # d.copy()对字典进行浅拷贝,字典内各项相同
    copydict = word_count.copy()
    print(copydict)
    print('原dict id=%s,新dict id=%s' % (id(word_count), id(copydict)))
    print('原dict id=%s' % (id(word_count['t'])))
    print('新dict id=%s' % (id(copydict['t'])))
    # d.get( x [ , y]) 返回字典 d 中键 x 对应的值，键 x 不存在的时候返回 y， y 的默认值为None
    print('dict.get():%s' % word_count.get('r'))
    # del d[x]  删除字典 d 中键为 x 的键值对，若 x 不存在会出现 KeyError
    del word_count['r']
    print('del 后dict.get():%s' % word_count.get('r'))
    # d.pop( x ) 返回给定键 x 对应的值，并将该键值对从字典中删除
    print('dict.pop():%s' % word_count.pop('l'))
    print('pop后dict.get():%s' % word_count.get('l'))
    # d.popitem( ) 返回并删除字典 d 中随机的键值对
    print(word_count)
    print('dict.popitem()随机返回字典键值对并删除:', word_count.popitem(), 'dict=', word_count)
    print('dict.popitem()随机返回字典键值对并删除:', word_count.popitem(), 'dict=', word_count)
    print('dict.popitem()随机返回字典键值对并删除:', word_count.popitem(), 'dict=', word_count)
    # d.clear() 清空字典
    copydict.clear()
    print("clear dict", copydict,word_count)
    # d.setdefault(x,[,y ])返回字典d中键x对应的值,若键x不存在,则返回y,并将x:y作为键值对添加到字典中,y的默认值为None
    print(d1.setdefault('hi',88),',d1=',d1)
    #d.update( x ) 将字典 x 所有键值对添加到字典 d 中（不重复，重复的键值对用字典 x 中的键值对替代字典 d 中）
    d2.update(d1)
    print('d2.update(d1):',d2)
if __name__ == '__main__':
    main()
