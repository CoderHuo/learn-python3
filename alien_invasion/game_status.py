#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Mr.Huo'


class GameStatus():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        #最高得分
        self.high_score = 0
        #让游戏开始处于暂停状态
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0


def main():
    pass


if __name__ == '__main__':
    main()
