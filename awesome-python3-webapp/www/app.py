#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging, socket
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web
import aiomysql

logging.basicConfig(level=logging.INFO)

__author__ = 'Mr.Huo'

'''
async web application.
'''

# 获取本机IP地址
LOCALIP = socket.gethostbyname(socket.gethostname())


def home_page(request):
    with open("templates\index.html") as home:
        return web.Response(body=home.read(), content_type='text/html')


def index_page(request):
    return web.Response(body=b'<h1>Awesome Index</h1>', content_type='text/html')


def go_page(request):
    return web.Response(body=b'<h1>Go Go Go</h1>', content_type='text/html')


# async def init(loop):
#    app = web.Application(loop=loop)
#    app.router.add_route('GET','/',index)
#    srv = await  loop.create_server(app.make_handler(),'127.0.0.1',9000)
#    logging.info('server started at http://127.0.0.1:9000...')
#    return  srv

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', home_page)
    app.router.add_route('GET', '/index', index_page)
    app.router.add_route('GET', '/go', go_page)
    srv = yield from loop.create_server(app.make_handler(), LOCALIP, 9000)
    logging.info('server started at http://%s:9000...' % LOCALIP)
    return srv


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    loop.run_forever()


if __name__ == '__main__':
    main()
