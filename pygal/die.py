#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygal
from random import randint

__author__ = 'Mr.Huo'


class Die():
    """骰子类"""

    def __init__(self, num_sides=6):
        """骰子面数"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1和骰子面数之间的随机数"""
        return randint(1,self.num_sides)


def main():
    die = Die()
    results = []
    for roll_num in range(10000):
        result = die.roll()
        results.append(result)
    print(results)

    frequencies = []
    for value in range(1,die.num_sides+1):
        frequency = results.count(value)
        frequencies.append(frequency)
    print(frequencies)

    # 绘制直方图
    hist = pygal.Bar()
    hist.title = "Results of rolling one D6 1000 times."
    hist.x_labels = ['1','2','3','4','5','6']
    hist.x_title='Results'
    hist.y_title='Frequency of Result'
    hist.add(title="D6",values=frequencies)
    hist.render_to_file('C:\\Users\\zhuosha\\PycharmProjects\\haha.svg')

if __name__ == '__main__':
    main()
