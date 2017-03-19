#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Mr.Huo'
import sys
import pygame


def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.m_RIGHT = True
            elif event.key == pygame.K_LEFT:
                ship.m_LEFT = True
            elif event.key == pygame.K_UP:
                ship.m_UP = True
            elif event.key == pygame.K_DOWN:
                ship.m_DOWN = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.m_RIGHT = False
            elif event.key == pygame.K_LEFT:
                ship.m_LEFT = False
            elif event.key == pygame.K_UP:
                ship.m_UP = False
            elif event.key == pygame.K_DOWN:
                ship.m_DOWN = False

    ship.update()


def update_screen(setting, screen, ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    screen.fill(setting.bg_color)
    ship.blitme()
    pygame.display.flip()
    pass


def main():
    pass


if __name__ == '__main__':
    main()
