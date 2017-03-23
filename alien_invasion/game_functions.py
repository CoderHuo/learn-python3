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


def check_events(screen, ai_settings, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event.key, screen, ai_settings, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event.key, ship)


def get_number_aliens_cols(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_aliens_rows(ai_settings, alien_height):
    available_space_y = ai_settings.screen_height / 3 * 2
    number_aliens_y = int(available_space_y / (alien_height * 2))
    return number_aliens_y


def create_aliens(screen, ai_settings, aliens, col_number, raw_number):
    alien = Alien(screen, ai_settings)
    alien.x = alien.rect.width + 2 * alien.rect.width * col_number
    alien.y = alien.rect.height * 2 * raw_number
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)


def create_fleet(screen, ai_settings, aliens):
    alien = Alien(screen, ai_settings)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien_cols = get_number_aliens_cols(ai_settings, alien_width)
    alien_rows = get_number_aliens_rows(ai_settings, alien_height)
    for row_number in range(alien_rows):
        for col_number in range(alien_cols):
            create_aliens(screen, ai_settings, aliens, col_number, row_number)

def check_fleet_edges(ai_settings,aliens):
    for alien in aliens:
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    '''将整群外星人下移，并改变他们的方向'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.alien_drop_speed
    for alien in aliens:
        alien.direction *= -1

def update_alien(ai_settings,aliens):
    check_fleet_edges(ai_settings,aliens)
    aliens.update()


def fire_bullet(screen, ai_settings, ship, bullets):
    """如果还没有到达限制，就发射一颗子弹"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(screen, ai_settings, ship)
        bullets.add(new_bullet)


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
    update_alien(ai_settings,aliens)
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
