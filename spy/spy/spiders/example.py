# -*- coding: utf-8 -*-

from spy.items import SpyItem
from scrapy.spiders.crawl import Rule
from scrapy import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy import Spider
from scrapy.spiders import CrawlSpider
from scrapy.utils.response import get_base_url
from urllib.parse import urljoin


class ExampleSpider(Spider):
    name = 'example'
    allowed_domains = ['tencent.com']
    start_urls = ['http://hr.tencent.com/position.php']
    #rules = [
    #    Rule(LinkExtractor(allow=('/position_detail.php\?id=\d{1,}')), follow=True,
    #         callback='parse_item')
    #]

    def parse(self, response):
        items = []
        base_url = get_base_url(response)
        sites_even = response.css('tr.even')
        for site in sites_even:
            item = SpyItem()
            item['title'] = site.css('.l.square a').xpath('text()').extract()
            item['category'] = site.css('tr > td:nth-child(2)::text').extract()
            item['recruitNumber'] = site.css('tr > td:nth-child(3)::text').extract()
            relative_url = site.css('.l.square a').xpath('@href').extract()[0]
            item['link'] = urljoin(base_url, relative_url)
            item['workLocation'] = site.css('tr > td:nth-child(4)::text').extract()
            item['publishTime'] = site.css('tr > td:nth-child(5)::text').extract()
            items.append(item)
        print("-"*100)
        print("base_url",base_url)
        for item in items:
            print(item)
        print("-"*100)
        return items

    #def _process_request(self, request):
    #    info('process ' + str(request))
    #    return request