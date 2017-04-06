#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import asyncio # 异步IO
import threading

__author__ = 'Mr.Huo'


# asyncio.coroutine把一个generator标记为coroutine类型
@asyncio.coroutine
def hello():
    print('Hello World! (%s)' % threading.current_thread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.current_thread())


@asyncio.coroutine
def web_get(host):
    print('Web get %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode().rstrip()))

    writer.close()


def main():
    loop = asyncio.get_event_loop()
    tasks = [hello(), hello()]
    loop.run_until_complete(asyncio.wait(tasks))

    tasks = [web_get(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    pass


if __name__ == '__main__':
    main()
