#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from atexit import register
from threading import Thread
from time import ctime
from urllib import request

__author__ = 'Mr.Huo'

REGEX = re.compile(b'#([\d,]+) in Books')
AMZN = 'http://www.amazon.com/dp/'
ISBNs = {
    '0132269937': 'Core Python Programming',
    '0132356139': 'Python Web Development with Django',
    '0137143419': 'Python Fundamentals'
}


def get_ranking(isbn):
    page = request.urlopen('%s%s' % (AMZN, isbn))
    data = page.read()
    page.close()
    return str(REGEX.findall(data)[0],'utf-8')


def _show_ranking(isbn):
    print('- %r ranked %s' % (ISBNs[isbn], get_ranking(isbn)))


def main():
    print('At', ctime(), 'on Amazon...')
    for isbn in ISBNs:
        _show_ranking(isbn)
    print('single thread DONE at:', ctime())
    for isbn in ISBNs:
        Thread(target=_show_ranking, args=(isbn,)).start()


@register
def _atx_exit():
    print('all DONE at:', ctime())


if __name__ == '__main__':
    main()
