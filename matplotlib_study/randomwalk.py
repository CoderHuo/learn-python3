#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from random import choice

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
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, s=1)
    plt.show()
    plt.plot(rw.x_values, rw.y_values)
    plt.show()
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


if __name__ == '__main__':
    main()
