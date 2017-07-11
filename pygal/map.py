#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygal

__author__ = 'Mr.Huo'


def main():
    ch_chart = pygal.maps.ch.Cantons()
    ch_chart.title = 'Some cantons'
    ch_chart.add('Cantons 1', ['kt-zh', 'kt-be', 'kt-nw'])
    ch_chart.add('Cantons 2', ['kt-ow', 'kt-bs', 'kt-ne'])
    ch_chart.render_to_file('C:\\Users\\zhuosha\\PycharmProjects\\Cantons.svg')
    #ch_chart.render_tree()
    pass


if __name__ == '__main__':
    main()
