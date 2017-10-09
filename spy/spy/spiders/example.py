# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['news.baidu.com']
    start_urls = ['http://news.baidu.com/']

    def parse(self, response):
        links  =  response.xpath('//li')
        print(links)
