#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Mr.Huo'


class GameStatus():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        #让游戏开始处于暂停状态
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit


def main():
    pass


if __name__ == '__main__':
    main()
