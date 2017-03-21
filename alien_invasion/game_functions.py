#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import pygame
from bullet import Bullet
from alien import Alien
import time

__author__ = 'Mr.Huo'


def check_keydown_event(event, screen, ai_settings, ship, bullets):
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
        fire_bullet(screen, ai_settings, ship, bullets)


def check_keyup_event(event, ship):
    '''响应松开'''
    if event in (pygame.K_RIGHT, pygame.K_d):
        ship.m_RIGHT = False
    elif event in (pygame.K_LEFT, pygame.K_a):
        ship.m_LEFT = False
    elif event in (pygame.K_UP, pygame.K_w):
        ship.m_UP = False
    elif event in (pygame.K_DOWN, pygame.K_s):
        ship.m_DOWN = False


def fire_bullet(screen, ai_settings, ship, bullets):
    """如果还没有到达限制，就发射一颗子弹"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(screen, ai_settings, ship)
        bullets.add(new_bullet)


def check_events(screen, ai_settings, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event.key, screen, ai_settings, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event.key, ship)


def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_aliens(screen, ai_settings, aliens, alien_number):
    alien = Alien(screen, ai_settings)
    alien.x = alien.rect.width + 2 * alien.rect.width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)


def create_fleet(screen, ai_settings, aliens):
    alien = Alien(screen, ai_settings)
    alien_width = alien.rect.width
    alien_numbers = get_number_aliens_x(ai_settings, alien_width)
    for alien_number in range(alien_numbers):
        create_aliens(screen, ai_settings, aliens, alien_number)


def update_alien(aliens):
    aliens.update()


def update_bullets(bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    # 更新子弹的位置
    bullets.update()
    # 删除消失的子弹
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def update_screen(screen, ai_settings, ship, bullets, aliens):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 更新飞船
    ship.update()
    # 更新子弹
    update_bullets(bullets)
    # 创建外星人并更新
    # update_alien(aliens)
    # 填充背景色
    screen.fill(ai_settings.bg_color)
    # 绘制飞船、子弹、外星人
    ship.blitme()
    aliens.draw(screen)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip()


def main():
    pass


if __name__ == '__main__':
    main()
