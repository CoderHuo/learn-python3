#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Mr.Huo'

import matplotlib.pyplot as plt

'''绘制散列点'''


def main():
    x_squares = [x for x in range(101)]
    y_squares = [x * x for x in x_squares]
    # 设置坐标轴起点终点值，x,y轴都已0开始，这样就可以在0原点绘制0
    plt.axis([-100, 100, -100, 10000])
    # edgecolors 数据点的轮廓
    plt.scatter(x_squares, y_squares,c='yellow', s=1)
    #参数c修改点的颜色，RGB或者
    plt.scatter(50, 1000,c='red', s=1)
    #颜色映射 c=y_squares, cmap=plt.cm.Blues
    plt.scatter(x_squares, y_squares,c=y_squares, cmap=plt.cm.Blues,s=10)
    #自动保存图片
    plt.savefig('picture.png')

    plt.show()
    pass


if __name__ == '__main__':
    main()
