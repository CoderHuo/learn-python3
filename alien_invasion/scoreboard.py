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

    def prep_score(self):
        """将得分转换为一幅渲染的图像"""
        score_str =  str(self.status.score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 20
        self.score_rect.bottom = self.screen_rect.bottom


    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)


def main():
    pass


if __name__ == '__main__':
    main()
