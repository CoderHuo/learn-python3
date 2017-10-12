#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spy.spiders.example import ExampleSpider
import sys

__author__ = 'Mr.Huo'


def main():
    # 将spy跟目录加入sys.path
    sys.path.append('..')
    settings = get_project_settings()
    process = CrawlerProcess(settings=settings)
    process.crawl(ExampleSpider)
    process.start()


if __name__ == '__main__':
    main()
