#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Mr.Huo'

import matplotlib.pyplot as plt

'''绘制散列点'''

def main():
    x_squares = [x for x in range(100)]
    y_squares = [x*x for x in x_squares]
    plt.scatter(x_squares,y_squares,s=100)
    plt.show()
    pass


if __name__ == '__main__':
    main()