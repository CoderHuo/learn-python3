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
from game_status import GameStatus
from  button import Button


def run_game():
    # 初始化游戏并创建一个屏幕对象
    clock = pygame.time.Clock()
    pygame.init()
    ai_settings = Settings()
    status = GameStatus(ai_settings)
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invision")
    # 创建一个ship
    ship = Ship(screen, ai_settings)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(screen, ai_settings, aliens)
    # 创建开始按钮
    play_button = Button(screen, "Play")
    # 开始游戏的主循环
    while True:
        time.sleep(ai_settings.ai_time)
        # if status.game_active:
        # 监视键盘和鼠标事件
        gf.check_events(screen, ai_settings, status, ship, bullets, aliens, play_button)
        gf.update_screen(screen, ai_settings, status, ship, bullets, aliens, play_button)
        clock.tick(60)
        # else:

    pygame.quit()


def main():
    run_game()


if __name__ == '__main__':
    main()
