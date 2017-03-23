#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Mr.Huo'


class GameStatus():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.game_active = True
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit


def main():
    pass


if __name__ == '__main__':
    main()
