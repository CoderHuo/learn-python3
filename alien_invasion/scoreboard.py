#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame.font

__author__ = 'Mr.Huo'


class Scoreboard():
    """显示得分的信息类"""

    def __init__(self,screen, ai_settings,status):
        """初始化显示得分涉及的属性"""
        self.screen =  screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.status = status

        #显示得分信息时使用的字体设置
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        #初始化得分图像
        self.prep_score()
        self.prep_hight_score()
        self.prep_level()

    def prep_score(self):
        """将得分转换为一幅渲染的图像"""
        rounded_score =int(round(self.status.score,-1))
        score_str =  "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right -10
        self.score_rect.top = self.screen_rect.top +10

    def prep_hight_score(self):
        """将最高得分转换为一幅渲染的图像"""
        high_rounded_score =int(round(self.status.high_score,-1))
        high_score_str =  "{:,}".format(high_rounded_score)
        self.high_score_image = self.font.render(high_score_str,True,self.text_color,self.ai_settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top +10

    def prep_level(self):
        """将级别转换为一幅渲染的图像"""
        level_str =  str(self.status.level)
        self.level_image = self.font.render(level_str,True,self.text_color,self.ai_settings.bg_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom +10

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)


def main():
    pass


if __name__ == '__main__':
    main()
