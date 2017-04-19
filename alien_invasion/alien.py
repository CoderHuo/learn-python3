#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Sprite

__author__ = 'Mr.Huo'


class Alien(Sprite):
    def __init__(self, screen, ai_settings):
        """初始化外星人并设置其起始位置"""
        super(Alien, self).__init__()
        self.screen = screen

        # 加载外星人图片，并设置其RECT属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 设置外星人初始位置
        self.rect.x = 0
        self.rect.y = 0
        # self.rect.x = self.rect.width
        # self.rect.y = self.rect.height
        # 存储外星人精确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # 外星人速度、方向
        self.speed = ai_settings.alien_speed
        self.direction = ai_settings.alien_direction

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)

    def update(self, *args):
        """移动外星人"""
        self.x += (self.speed * self.direction)
        self.rect.x = self.x

    def check_edges(self):
        """判断是不是到达边缘"""
        if self.rect.right >= self.screen_rect.right:
            return True
        elif self.rect.left <= self.screen_rect.left:
            return True
