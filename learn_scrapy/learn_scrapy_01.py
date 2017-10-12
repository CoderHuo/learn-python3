#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scrapy import Selector

__author__ = 'Mr.Huo'

html = '''
    <ul class="list">
        <li>1</li>
        <li>2</li>
        <li>3</li>
    </ul>
    <ul class="list">
        <li>4</li>
        <li>5</li>
        <li>6</li>
    </ul>
    <div class="hero shout"><time datetime="2014-07-23 19:00">Special date</time></div>
'''


def print_iter(iter_list):
    if iter_list:
        for it in iter_list:
            print(it)
    print()


def main():
    sel = Selector(text=html)
    xp = lambda x: sel.xpath(x).extract()
    print(xp('//li'))
    print(xp('//li[1]'))
    print(xp('(//li)[1]'))
    print_iter(sel.xpath('//li'))
    print_iter(sel.css('li'))
    pass


if __name__ == '__main__':
    main()
