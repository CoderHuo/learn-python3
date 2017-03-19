#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Mr.Huo'


class Settings():
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230,230,230)

    def __str__(self):
        return 'Width:' + str(self.screen_width) + '\nHeight:' + str(self.screen_height) + '\nColor:' + str(self.bg_color)

def main():
    alien_setting = Settings()
    print(alien_setting)


if __name__ == '__main__':
    main()
