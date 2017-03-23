#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Mr.Huo'
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, screen, ai_settings, ship):
        super(Bullet, self).__init__()
        self.screen = screen
        # 在0，0 创建一个子弹，在移动到正确位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed = ai_settings.bullet_speed

    def update(self):
        '''向上移动子弹'''
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)


def main():
    pass


if __name__ == '__main__':
    main()
