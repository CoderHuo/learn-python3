#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame, pickle
from settings import Settings
from ship import Ship
from bullet import Bullet
import game_functions as gf
import time
from pygame.sprite import Group
from game_status import GameStatus
from button import Button
from scoreboard import Scoreboard

__author__ = 'Mr.Huo'

statusfile = 'status'


def run_game():
    # 初始化游戏并创建一个屏幕对象
    clock = pygame.time.Clock()
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invision")
    # 创建一个ship
    ship = Ship(screen, ai_settings)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(screen, ai_settings, aliens)
    # 创建开始按钮
    play_button = Button(screen, "Play")
    # 创建存储游戏统计信息的实例，并创建记分牌
    try:
        print('00000')
        status_file = open(statusfile, 'rb')
        status = pickle.load(status_file)
    except FileNotFoundError:
        print('11111')
        status = GameStatus(ai_settings)

    scoreboard = Scoreboard(screen, ai_settings, status)

    # 开始游戏的主循环
    while True:
        time.sleep(ai_settings.ai_time)
        # if status.game_active:
        # 监视键盘和鼠标事件
        gf.check_events(screen, ai_settings, status, ship, bullets, aliens, play_button, scoreboard)
        gf.update_screen(screen, ai_settings, status, ship, bullets, aliens, play_button, scoreboard)
        clock.tick(60)
        try:
            print('22222')
            status_file = open(statusfile, 'xb')
            pickle.dump(GameStatus, status_file)
        except FileExistsError:
            print('33333')
            status_file = open(statusfile, 'r+b')
            pickle.dump(GameStatus, status_file)
            pass


def main():
    run_game()


if __name__ == '__main__':
    main()
