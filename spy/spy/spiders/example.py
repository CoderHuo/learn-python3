# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from spy.items import SpyItem


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['doc.scrapy.org']
    start_urls = ['http://doc.scrapy.org/en/latest/_static/selectors-sample1.html']

    def parse(self, response):
        items = SpyItem()
        filename = response.xpath('//title/text()').extract()[0]
        items['title'] = response.xpath('//title/text()').extract()
        for sel in response.xpath('//a'):
            pass
        print("-" * 80)
        print(filename)
        print(response)
        print(items['title'])
        print("-" * 80)
