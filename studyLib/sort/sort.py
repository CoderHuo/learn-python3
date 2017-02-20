#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 排序算法练习

def bubble_sort(list, flag=True):
    """ 冒泡排序基本思想：从第一个元素开始，每每相邻的两个元素进行比较，若前者比后者大则交换位置。最后两个相邻元素，
        比较完成后最大的元素形成，然后再次从头开始进行比较，若元素个数为n+1个，则总共需要进行n轮比较就可完成排序
        （n轮比较后，n个最大的元素已经形成，最后一个元素当然是最小的，就不用再比了）。每轮比较中，每形成一个最大
        的元素，下一轮比较的时候 就少比较一次，第一轮需要比较n次，第二轮需要比较n-1次，以此类推，第n轮（最后一轮)
        只需要比较1次就可。这样，列表就排好序了
        时间复杂度:O(n^2) O(n),空间复杂度：O(1)"""
    if (len(list) > 0):
        for i in range(len(list) - 1):
            for j in range(len(list) - 1 - i):
                if (flag):
                    if (list[j] > list[j + 1]):
                        list[j], list[j + 1] = list[j + 1], list[j]
                else:
                    if (list[j] < list[j + 1]):
                        list[j], list[j + 1] = list[j + 1], list[j]
    return (list)


def insert_sort(list, flag=True):
    """ 插入排序基本思想：第一个元素已经排好，从第二个开始，依次跟前面的比较，按大小规则进行排序
        时间复杂度:O(n^2) O(n),空间复杂度：O(1)"""
    if len(list) > 0:
        for i in range(1, len(list)):
            key = list[i] #要插入的值
            j = i - 1
            while j >= 0:
                if flag:
                    if list[j] > key:   #列表y到0之间的值跟要插入的值比较，如果大于就换位
                        list[j + 1] ,list[j]= list[j],key
                    #print("i=", i, " j=", j, "KEY=",key,"list=", list)
                    j -= 1
                else:
                    if list[j] < key:
                        list[j + 1], list[j] = list[j], key
                    #print("i=", i, " j=", j, "KEY=",key,"list=", list)
                    j -= 1
    return list

def main():
    print(help(bubble_sort))
    list = [8, 7, 6, 3, 2, 1]
    print(bubble_sort(list))
    print(list)
    print(bubble_sort(list, False))

    list1 = [i for i in range(1000)]
    # print(bubble_sort(list1, False))
    list2 = [1, 0, 2, -1, -2, -3, 87]
    print(insert_sort(list2))
    print(insert_sort(list2, False))

if __name__ == '__main__':
    main()