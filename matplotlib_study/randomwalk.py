#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from random import choice
import numpy as np
__author__ = 'Mr.Huo'


class RandomWalk():
    """一个生成随机漫步数据的类"""

    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points
        # 随机漫步初始值0点
        self.x_values = [0]
        self.y_values = [0]
        self.diction = [1, -1]
        self.distance = [1, 2, 3, 4]

    def get_step(self):
        dirction = choice(self.diction)
        distance = choice(self.distance)
        step = dirction * distance
        return step

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        # 不断漫步，直到达到指定的长度
        while len(self.x_values) < self.num_points:
            # 前进的方向以及沿这个方向前进的距离，前进的距离不为0在不会原地踏步
            # x_dirction = choice(self.diction)
            # x_distance = choice(self.distance)
            # x_step = x_dirction * x_distance

            # y_dirction = choice(self.diction)
            # y_distance = choice(self.distance)
            # y_step = y_dirction * y_distance

            x_step = self.get_step()
            y_step = self.get_step()
            # 计算下一个点的x,y值
            next_x = self.x_values[-1] + x_step
            next_y = self.x_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def fill_walk_no_passed(self):
        """计算随机漫步包含的所有点，去过的点不再去"""

        # 不断漫步，直到达到指定的长度
        while len(self.x_values) < self.num_points:
            # 前进的方向以及沿这个方向前进的距离，前进的距离不为0在不会原地踏步
            # x_dirction = choice(self.diction)
            # x_distance = choice(self.distance)
            # x_step = x_dirction * x_distance

            # y_dirction = choice(self.diction)
            # y_distance = choice(self.distance)
            # y_step = y_dirction * y_distance
            x_step = self.get_step()
            y_step = self.get_step()
            # 计算下一个点的x,y值
            next_x = self.x_values[-1] + x_step
            next_y = self.x_values[-1] + y_step

            # 去除已经去过的点
            if next_x in self.x_values:
                if next_y == self.y_values[self.x_values.index(next_x)]:
                    continue

            self.x_values.append(next_x)
            self.y_values.append(next_y)


def main():
    """绘制随机漫步值"""
    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    rw = RandomWalk(1000)
    point_numbers = list(range(rw.num_points))
    # rw.fill_walk()
    rw.fill_walk_no_passed()
    # 设置绘图窗口的尺寸
    # 同时绘制多幅图表，可以给figure()传递一个整数参数指定Figure对象的序号，如果序号所指定的Figure对象已经存在，
    # 将不创建新的对象，而只是让它成为当前的Figure对象
    plt.figure(1)
    # 在图表1中创建子图1
    ax1 = plt.subplot(211)
    # 在图表1中创建子图1
    ax2 = plt.subplot(212)
    # 选择图表1
    plt.figure(1)
    # 选择图表1的子图1
    plt.sca(ax1)
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, s=1)
    # 选择图表1的子图2
    plt.sca(ax2)
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, s=1)
    # while True:
    #     rw = RandomWalk(1000)
    #     rw.fill_walk()
    #     point_numbers = list(range(rw.num_points-2))
    #
    #     # 隐藏坐标轴
    #     plt.axes().get_xaxis().set_visible(False)
    #     plt.axes().get_yaxis().set_visible(False)
    #     # 绘制漫步点
    #     plt.scatter(0,0,c='green',s=10)
    #     plt.scatter(rw.x_values[1:len(rw.x_values)-1], rw.y_values[1:len(rw.y_values)-1],c=point_numbers, cmap=plt.cm.Blues,s=2)
    #     plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',s=10)
    #
    #     plt.show()
    #     keep_running = input('Make another randomwalk? (y/n)')
    #     if keep_running == 'n':
    #         break
    plt.figure(2)
    ax21 = plt.subplot(221)
    ax22 = plt.subplot(222)
    ax23 = plt.subplot(223)
    ax24 = plt.subplot(224)
    x = np.linspace(0, 3, 100)
    for i in range(5):
        plt.sca(ax21)
        plt.plot(x, np.exp(i * x / 3))
        plt.sca(ax22)
        plt.plot(x, np.sin(i * x))
        plt.sca(ax23)
        plt.plot(x, np.cos(i * x))
        plt.sca(ax24)
        plt.plot(x, np.cosh(i * x))
    plt.show()
if __name__ == '__main__':
    main()
