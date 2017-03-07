#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''Train tickets query via command-line.

Usage:
    trainTicket [-gdtkz] <from> <to> <date>

Options:
    -h,--help       显示帮助
    -g              高铁
    -d              动车
    -t              特快
    -k              快车
    -z              直达

Example:
    trainTicket 北京 上海 2016-08-25
'''
from docopt import docopt
import requests,re
import requests.packages.urllib3 as req_u3
from pprint import pprint

__author__ = 'Mr.Huo'
req_u3.disable_warnings(req_u3.exceptions.InsecureRequestWarning)

def cli():
    '''command-line interface'''
    arguments = docopt(__doc__)
    print(arguments)

def station_name():
    station_name_url = 'http://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8999'
    res = requests.get(station_name_url,verify=False)
    stations = [ x.split('|')[0:4]  for x in (res.text.split('@')[1::])]
    print(stations)

    #url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate={}&from_station={}&to_station={
    # }'.format(
    #    '2017-03-08', 'SHH', 'BJP'
    #)
    #r = requests.get(url, verify=False)
    #r.encoding = 'UTF8'
    #print(r.json())
    #stations = re.findall(r'([A-Z]+)\|([a-z]+)', res.text)
    #print('re.findall stations:',stations)
    #stations = dict(stations)
    #stations = dict(zip(stations.values(), stations.keys()))
    #pprint(stations, indent=4)
def main():
    cli()
    station_name()

if __name__ == '__main__':
    main()
