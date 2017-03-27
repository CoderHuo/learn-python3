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
        self.ai_time = 0.01
        self.ship_limit = 2
        # 子弹属性bullet

        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (100, 60, 60)
        # 子弹数量
        self.bullets_allowed = 10

        # 外星人
        self.alien_direction = 1
        self.alien_drop_speed = 10
        self.alien_points = 10

        # 游戏加速节奏
        self.speedup_scale = 1.2
        self.alien_points_up_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.bullet_speed = 4
        self.alien_speed = 2
        self.ship_speed = 3.5

    def increase_speed(self):
        """提高速度设置"""
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.alien_points_up_scale)

    def __str__(self):
        return 'This is the alien invasion settings'


def main():
    alien_setting = Settings()
    print(alien_setting)


if __name__ == '__main__':
    main()
