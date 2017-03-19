#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Mr.Huo'


class Settings():
    def __init__(self):
        # 主窗口设置
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # 飞船属性
        self.ship_speed_factor = 3.5
        self.ai_time = 0.01
        # 子弹属性bullet
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        # 子弹数量
        self.bullets_allowed = 5

    def __str__(self):
        return 'This is the alien invasion settings'


def main():
    alien_setting = Settings()
    print(alien_setting)


if __name__ == '__main__':
    main()
