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


def check_events(screen, ai_settings, status, ship, bullets, aliens, play_button):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN and status.game_active:
            #未开始前，不发射子弹
            check_keydown_event(event.key, screen, ai_settings, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event.key, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(screen, ai_settings, status, ship, bullets, aliens, play_button, mouse_x, mouse_y)


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
    """创建外星人舰队"""
    alien = Alien(screen, ai_settings)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien_cols = get_number_aliens_cols(ai_settings, alien_width)
    alien_rows = get_number_aliens_rows(ai_settings, alien_height)

    for row_number in range(alien_rows):
        for col_number in range(alien_cols):
            create_aliens(screen, ai_settings, aliens, col_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """检查舰队是不是到达边缘"""
    for alien in aliens:
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    '''将整群外星人下移，并改变他们的方向'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.alien_drop_speed
    for alien in aliens:
        alien.direction *= -1


def update_alien(screen, ai_settings, status, ship, bullets, aliens):
    """更新外星人"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # 检查是外星人是否相撞
    hit_alien = None
    hit_alien = pygame.sprite.spritecollideany(ship, aliens)
    if hit_alien != None:
        print('Ship hit!!!')
        # 删除被撞外星人
        aliens.remove(hit_alien)
        # 重置飞船
        ship_hit(screen, ai_settings, status, ship, bullets, aliens)
    # 检查外星人是否到达底部
    check_aliens_bottom(screen, ai_settings, status, ship, bullets, aliens)


def check_aliens_bottom(screen, ai_settings, status, ship, bullets, aliens):
    """检查外星人是不是到达底部，如果是重置游戏"""
    screen_rect = screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(screen, ai_settings, status, ship, bullets, aliens)
            break


def ship_hit(screen, ai_settings, status, ship, bullets, aliens):
    if status.ships_left > 0:
        status.ships_left -= 1
        bullets.empty()
        aliens.empty()
        create_fleet(screen, ai_settings, aliens)
        ship.center_ship()
        time.sleep(0.5)
    else:
        status.game_active = False


def fire_bullet(screen, ai_settings, ship, bullets):
    """如果还没有到达限制，就发射一颗子弹"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(screen, ai_settings, ship)
        bullets.add(new_bullet)


def update_bullets(screen, ai_settings, bullets, aliens):
    """更新子弹的位置，并删除已消失的子弹"""
    # 更新子弹的位置
    bullets.update()
    # 删除消失的子弹
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(screen, ai_settings, bullets, aliens)


def check_bullet_alien_collisions(screen, ai_settings, bullets, aliens):
    '''检查是否有子弹击中外星人，如果是这样就删除对应的子弹和外星人'''
    pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(screen, ai_settings, aliens)


def check_play_button(screen, ai_settings, status, ship, bullets, aliens, play_button, mouse_x, mouse_y):
    """玩家单击Play按钮时开始游戏"""
    button_click = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_click and not status.game_active:
        #重置游戏
        ai_settings.initialize_dynamic_settings
        status.game_active = True
        bullets.empty()
        aliens.empty()
        create_fleet(screen, ai_settings, aliens)
        ship.center_ship()
        #隐藏光标
        pygame.mouse.set_visible(False)


def update_screen(screen, ai_settings, status, ship, bullets, aliens, play_button):
    """更新屏幕上的图像，并切换到新屏幕"""
    if status.game_active:
        # 更新飞船
        ship.update()
        # 更新子弹
        update_bullets(screen, ai_settings, bullets, aliens)
        # 创建外星人并更新
        update_alien(screen, ai_settings, status, ship, bullets, aliens)
    # 填充背景色
    screen.fill(ai_settings.bg_color)
    # 绘制飞船、子弹、外星人
    ship.blitme()
    aliens.draw(screen)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    if not status.game_active:
        play_button.draw_button()
        #显示光标
        pygame.mouse.set_visible(True)
    pygame.display.flip()


def main():
    pass


if __name__ == '__main__':
    main()
