#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Mr.Huo'




def main():
    #generator：一边循环一边计算
    #创建generator，根据列表生成式创建
    L=(x*x for x in range(10))
    print(L)
    print(L.__next__())

    D=()


if __name__ == '__main__':
    main()