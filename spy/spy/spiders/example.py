# -*- coding: utf-8 -*-

from spy.items import SpyItem
from scrapy import Spider, Request
from scrapy.utils.response import get_base_url
from urllib.parse import urljoin


class ExampleSpider(Spider):
    name = 'example'
    allowed_domains = ['tencent.com']
    start_urls = ['http://hr.tencent.com/position.php']

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        base_url = get_base_url(response)
        sites_even = response.css('tr.even')
        sites_odd = (response.css('tr.odd'))
        for site in sites_even + sites_odd:
            item = SpyItem()
            item['title'] = site.css('.l.square a').xpath('text()').extract_first()
            # 热门职位标志
            hot = site.css('.l.square span').xpath('text()').extract_first()
            if hot is not None:
                item['hot'] = "yes"
            else:
                item['hot'] = "no"
            # 职位类别有空白
            item['category'] = site.css('tr > td:nth-child(2)::text').extract_first(default='未分类职位')
            item['recruitNumber'] = site.css('tr > td:nth-child(3)::text').extract_first()
            relative_url = site.css('.l.square a').xpath('@href').extract_first()
            item['link'] = urljoin(base_url, relative_url)
            item['workLocation'] = site.css('tr > td:nth-child(4)::text').extract_first()
            item['publishTime'] = site.css('tr > td:nth-child(5)::text').extract_first()
            yield item

        next_page = urljoin(base_url, response.xpath('//a[@id="next"]/@href').extract_first())
        if next_page is not None:
            yield response.follow(next_page, self.parse)
