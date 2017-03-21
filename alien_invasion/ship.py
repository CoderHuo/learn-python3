#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Mr.Huo'
import pygame


class Ship():
    def __init__(self, screen,ai_settings):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings =ai_settings

        # 加载飞船图像并获取其外接矩形
        self.imag = pygame.image.load('images/ship.bmp')
        self.rect = self.imag.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

        # 移动标志
        self.m_LEFT = False
        self.m_RIGHT = False

        self.m_UP = False
        self.m_DOWN = False

    def blitme(self):
        self.screen.blit(self.imag, self.rect)

    def move_left(self):
        if self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor
            self.rect.centerx =self.center

    def move_right(self):
        if self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
            self.rect.centerx =self.center

    def move_up(self):
        if self.rect.top > self.screen_rect.top:
            self.bottom -= self.ai_settings.ship_speed_factor
            self.rect.bottom = self.bottom

    def move_down(self):
        if self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.ai_settings.ship_speed_factor
            self.rect.bottom = self.bottom
    def update(self):
        if self.m_RIGHT:
            self.move_right()
        if self.m_LEFT:
            self.move_left()
        if self.m_UP:
            self.move_up()
        if self.m_DOWN:
            self.move_down()

