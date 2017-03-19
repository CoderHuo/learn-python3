#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Mr.Huo'
import pygame


class Ship():
    def __init__(self, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.imag = pygame.image.load('images/ship.bmp')
        self.rect = self.imag.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.imag, self.rect)

    def move_left(self):
        if self.rect.left > self.screen_rect.left:
            self.rect.centerx -= 1

    def move_right(self):
        if self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1


def main():
    pass


if __name__ == '__main__':
    main()
