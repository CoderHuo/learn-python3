#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv

__author__ = 'Mr.Huo'


def main():
    file = "data.csv"
    with open(file) as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            print(row)
            for index, colum_header in enumerate(row):
                print(index,colum_header)


if __name__ == '__main__':
    main()