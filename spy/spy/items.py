# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class SpyItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()         # 职位名称
    category = Field()      # 职位类别
    recruitNumber = Field() # 招聘人数
    workLocation = Field()  # 工作地点
    publishTime = Field()   # 发布时间
    link = Field()          # 链接
