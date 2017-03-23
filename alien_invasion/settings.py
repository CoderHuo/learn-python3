#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Mr.Huo'


class Settings():
    def __init__(self):
        # 主窗口设置
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # 飞船属性
        self.ship_speed = 3.5
        self.ai_time = 0.01
        self.ship_limit = 3
        # 子弹属性bullet
        self.bullet_speed = 2
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (100, 60, 60)
        # 子弹数量
        self.bullets_allowed = 10

        #外星人
        self.alien_speed = 1
        self.alien_direction = 1
        self.alien_drop_speed =10

    def __str__(self):
        return 'This is the alien invasion settings'


def main():
    alien_setting = Settings()
    print(alien_setting)


if __name__ == '__main__':
    main()
