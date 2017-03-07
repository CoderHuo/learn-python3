#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''datetime是Python处理日期和时间的标准库'''
__author__ = 'Mr.Huo'
from datetime import datetime, timezone, timedelta
import re


def tz_utc(hours):
    return timezone(timedelta(hours=hours))


def to_timestamp(dt_str, tz_str):
    '''按照给定时间、时区转换成timestamp'''
    utc_reg = re.match(r'^UTC([\+\-])(\d{1,2}):(\d{2}$)', tz_str)
    if utc_reg:
        try:
            time = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
        except BaseException as err:
            print('ValueError: %s is invalid' % err)
    else:
        raise ValueError('Invalid UTC-timezone_string was given.')
    time = time.replace(tzinfo=timezone.utc)
    print(time)
    hour = int(utc_reg.group(2))
    minute = int(utc_reg.group(3))
    td = timedelta(hours=hour, minutes=minute)
    if utc_reg.group(1) == '+':
        timestamp = (time - td).timestamp()
    else:
        timestamp = (time + td).timestamp()
    return timestamp


def main():
    # 获取当前时间
    now = datetime.now()
    print(now)
    # 用指定日期时间创建datetime
    dt = datetime(1986, 6, 6)
    print(dt)
    # 把datetime转换为timestamp
    gdt = dt.timestamp()
    print(gdt)
    # 把timestamp转换为datetime
    print(datetime.fromtimestamp(gdt))
    print(datetime.utcfromtimestamp(gdt))
    # 字符串转时间fromtimestamp()
    cday = datetime.strptime('1986-06-06 12:00:00', '%Y-%m-%d %H:%M:%S')
    print(cday)
    # 时间转字符串
    time_str = now.strftime('%a, %b %d %H:%M')
    print(time_str)
    tz_utc_8 = timezone(timedelta(hours=8))
    now = now.replace(tzinfo=tz_utc_8)
    print(now)
    # 时区转换

    utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
    print(utc_dt)
    bj_dt = utc_dt.astimezone(tz_utc(8))
    print(bj_dt)
    tokyo_dt = utc_dt.astimezone(tz_utc(9))
    print(tokyo_dt)

    t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
    assert t1 == 1433121030.0, t1
    t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
    assert t2 == 1433121030.0, t2


if __name__ == '__main__':
    main()
