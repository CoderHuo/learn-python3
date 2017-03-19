#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Mr.Huo'
import sys
import pygame
from bullet import Bullet
import  time


def check_keydown_event(event, ai_setting, screen, ship, bullets):
    '''响应按键'''
    if event in (pygame.K_RIGHT, pygame.K_d):
        ship.m_RIGHT = True
    elif event in (pygame.K_LEFT, pygame.K_a):
        ship.m_LEFT = True
    elif event in (pygame.K_UP, pygame.K_w):
        ship.m_UP = True
    elif event in (pygame.K_DOWN, pygame.K_s):
        ship.m_DOWN = True
    elif event == pygame.K_SPACE:
        fire_bullet(ai_setting, screen, ship, bullets)

def check_keyup_event(event, ai_setting, screen, ship, bullets):
    '''响应松开'''
    if event in (pygame.K_RIGHT, pygame.K_d):
        ship.m_RIGHT = False
    elif event in (pygame.K_LEFT, pygame.K_a):
        ship.m_LEFT = False
    elif event in (pygame.K_UP, pygame.K_w):
        ship.m_UP = False
    elif event in (pygame.K_DOWN, pygame.K_s):
        ship.m_DOWN = False

def fire_bullet(ai_setting, screen, ship, bullets):
    """如果还没有到达限制，就发射一颗子弹"""
    if len(bullets)<ai_setting.bullets_allowed:
        new_bullet = Bullet(ai_setting, screen, ship)
        bullets.add(new_bullet)

def check_events(ai_setting, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event.key, ai_setting, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event.key, ai_setting, screen, ship, bullets)


def update_bullets(bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    # 更新子弹的位置
    bullets.update()
    # 删除消失的子弹
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))


def update_screen(setting, screen, ship, bullets):
    ship.update()
    update_bullets(bullets)
    """更新屏幕上的图像，并切换到新屏幕"""
    screen.fill(setting.bg_color)
    ship.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip()
    pass


def main():
    pass


if __name__ == '__main__':
    main()
