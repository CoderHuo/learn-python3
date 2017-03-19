#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Mr.Huo'

import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
import game_functions as gf
import time
from pygame.sprite import Group


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_setting = Settings()

    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invision")
    # 创建一个ship
    ship = Ship(screen, ai_setting)
    bullets = Group()
    # 开始游戏的主循环
    while True:
        time.sleep(ai_setting.ai_time)
        # 监视键盘和鼠标事件
        gf.check_events(ai_setting, screen, ship, bullets)
        gf.update_screen(ai_setting, screen, ship, bullets)


def main():
    run_game()


if __name__ == '__main__':
    main()
