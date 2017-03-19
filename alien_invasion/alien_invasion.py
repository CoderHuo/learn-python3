#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Mr.Huo'

import sys

import pygame
from settings import Settings
from ship import Ship
import game_functions


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_setting = Settings()

    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invision")

    #创建一个ship
    ship = Ship(screen)
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        game_functions.check_events()

        screen.fill(ai_setting.bg_color)
        ship.blitme()
        #ship.move_left()
        ship.move_right()
        # 让最近绘制的屏幕可见
        pygame.display.flip()

def main():
    run_game()


if __name__ == '__main__':
    main()
