#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Mr.Huo'





def main():
    empty_list = []
    # 使用list()创建一个空列表
    another_empty_list = list()

    my_list = ['huo', 'shao', 'hua']

    empty_list = list('cat')

    a_tuple = ("liu", "zhi", 'xuan')
    another_empty_list = list(a_tuple)

    print(empty_list)
    print(another_empty_list)
    print(my_list)

    # 列表推导式
    rows = range(1, 6)
    cols = range(2, 7)
    cells = [(row, col) for row in rows for col in cols]
    print(cells)

    # 字典推导式
    words = "letters"
    word_count = {letter: words.count(letter) for letter in words}
    print(word_count)
    for name, contents in word_count.items():
        print(name, contents)
        print(list(word_count.items()))
        print(list(word_count.keys()))
        print(list(word_count.values()))

        # while True:
        #     value = input("Integer,please [q to quit]:")
        #     if value == 'q':
        #         break
        #     number = int(value)
        #     if number % 2 == 0:
        #         print(number, "squared is", number * number)
        #         continue


if __name__ == '__main__':
    main()