#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from html.parser import HTMLParser
from collections import OrderedDict
from pprint import pprint
from urllib import request, parse

__author__ = 'Mr.Huo'


class MyHtmlParser(HTMLParser):
    def __init__(self):
        super(MyHtmlParser, self).__init__()
        self.levels = 0
        self.allEvents = {}
        self.events = []
        #self.event = {'event-title':'','event-time':'','event-location':''}
        self.event = OrderedDict()
        self.event['event-title'] = ''
        self.event['event-time'] = ''
        self.event['event-location'] = ''
        self.keys = []
        self.tag = ('div', 'h2', 'h3', 'ul', 'li', 'time', 'span')
        self.tagclass = ('most-recent-events', 'shrubbery',
                         'widget-title', 'list-recent-events menu',
                         'event-title', 'say-no-more',
                         'event-location', 'widget-title just-missed'
                         )
        self.flag = {'div_1': False, 'div_2': False, 'h2': False, 'h3_1': False, 'h3_2': False,
                     'ul': False, 'li': False, 'time': False, 'span_1': False, 'span_2': False}

    def __str__(self):
        return str(self.allEvents)

    def add_event_data(self, data):
        if self.flag['h3_1']:
            self.event['event-title'] = data
        if self.flag['time'] and self.flag['span_1'] == False:
            self.event['event-time'] = data
        if self.flag['span_2']:
            self.event['event-location'] = data

    # Overridable -- finish processing of start+end tag: <tag.../>
    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    # Overridable -- handle start tag: <tag>
    def handle_starttag(self, tag, attrs):
        if tag in self.tag:
            if attrs:
                for key, value in attrs:
                    if key == 'class':
                        #most-recent-events
                        if value == self.tagclass[0]:
                            self.flag['div_1'] = True
                        #shrubbery
                        if self.flag['div_1'] :
                            if value == self.tagclass[1]:
                                self.flag['div_2'] = True
                            #widget-title
                            elif value == self.tagclass[2]:
                                self.flag['h2'] = True
                            #list-recent-events menu
                            elif value == self.tagclass[3]:
                                self.flag['ul'] = True
                            #event-title
                            elif value == self.tagclass[4]:
                                self.flag['h3_1'] = True
                            #say-no-more
                            elif value == self.tagclass[5]:
                                self.flag['span_1'] = True
                            #event-location
                            elif value == self.tagclass[6]:
                                self.flag['span_2'] = True
                            #widget-title just-missed
                            elif value == self.tagclass[7]:
                                self.flag['h3_2'] = True
                    elif self.flag['div_1'] and key == 'datetime':
                        self.flag['time'] = True
            else:
                if self.flag['div_1'] and tag == self.tag[4]:
                    self.flag['li'] = True

    # Overridable -- handle end tag: <tag.../>
    def handle_endtag(self, tag):
        #'div', 'h2', 'h3', 'ul', 'li', 'time', 'span'
        if tag == self.tag[0]:
            if self.flag['div_2']:
                self.flag['div_2'] = False
            elif self.flag['div_2'] == False and self.flag['div_1']:
                self.flag['div_1'] = False
        elif tag == self.tag[1]:
            self.flag['h2'] = False
        elif tag == self.tag[2]:
            if self.flag['h3_1']:
                self.flag['h3_1'] = False
            elif self.flag['h3_1'] == False and self.flag['h3_2']:
                self.flag['h3_2'] = False
        elif tag == self.tag[3]:
            self.flag['ul'] = False
            #判断在需要的分区部分了才增加
            if self.flag['div_1']:
                key = self.keys[len(self.keys) - 1]
                dt = {key: self.events}
                self.events = []
                self.allEvents.update(dt)
        elif tag == self.tag[4]:
            self.flag['li'] = False
            if self.flag['div_1'] :
                self.events.append(self.event)
                self.event = OrderedDict()
                self.event['event-title'] = ''
                self.event['event-time'] = ''
                self.event['event-location'] = ''
                #self.event = {'event-title':'','event-time':'','event-location':''}
        elif tag == self.tag[5]:
            self.flag['time'] = False
        elif tag == self.tag[6]:
            if self.flag['span_1']:
                self.flag['span_1'] = False
            elif self.flag['span_2']:
                self.flag['span_2'] = False

    # Overridable -- handle data
    def handle_data(self, data):
        if self.flag['div_1']:
            if self.flag['div_2']:
                if self.flag['h2']:
                    self.keys.append(data)
                elif self.flag['ul'] and self.flag['li']:
                    self.add_event_data(data)
            else:
                if self.flag['h3_2']:
                    self.keys.append(data)
                elif self.flag['ul'] and self.flag['li']:
                    self.add_event_data(data)

    # Overridable -- handle character reference  &#
    def handle_charref(self, name):
        pass

    # Overridable -- handle entity reference
    def handle_entityref(self, name):
        pass

    # Overridable -- handle comment
    def handle_comment(self, data):
        pass

    # Overridable -- handle declaration
    def handle_decl(self, decl):
        pass

    # Overridable -- handle processing instruction
    def handle_pi(self, data):
        pass

    def unknown_decl(self, data):
        pass


htmldata = '''<html>
<head>huo shao hua</head>
<body>
<div class="container">
    <section class="main-content with-right-sidebar" role="main">
        <header class="article-header">
        <h3>from the Python Events Calendar</h3>
        </header>
        <div class="most-recent-events">
            <div class="shrubbery">
                <h2 class="widget-title"><span aria-hidden="true" class="icon-calendar"></span>Upcoming Events</h2>
                <p class="give-me-more"><a href="?page=2" title="More Events">More</a></p>
                <ul class="list-recent-events menu">
                1   <li>
                3       <p>
                4           <time datetime="2017-04-01T00:00:00+00:00">01 April &ndash; 03 April <span class="say-no-more"> 2017</span></time>
                5           <span class="event-location">Toulon, France</span>
                6       </p>
                2       <h3 class="event-title"><a href="/events/python-events/498/">Rencontres Django 2017</a></h3>
                7   </li>
                8   <li>
                9       <h3 class="event-title"><a href="/events/python-events/467/">DjangoCon Europe 2017</a></h3>
                0       <p>
                            <time datetime="2017-04-03T00:00:00+00:00">03 April &ndash; 08 April <span class="say-no-more"> 2017</span></time>
                            <span class="event-location">Florence, Italy</span>
                        </p>
                    </li>
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/504/">PyCon UA 2017</a></h3>
                        <p>
                            <time datetime="2017-04-08T00:00:00+00:00">08 April &ndash; 10 April <span class="say-no-more"> 2017</span></time>
                            <span class="event-location">Lviv Arena Stadium, Lviv City, Ukraine</span>
                        </p>
                    </li>
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/493/">PythonCamp 2017</a></h3>
                        <p>
                            <time datetime="2017-04-08T00:00:00+00:00">08 April &ndash; 10 April <span class="say-no-more"> 2017</span></time>
                            <span class="event-location">GFU Cyrus AG , Am Grauen Stein 27, 51105 Köln, Germany</span>
                        </p>
                    </li>
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/501/">PyDays Vienna</a></h3>
                        <p>
                            <time datetime="2017-05-05T00:00:00+00:00">05 May &ndash; 07 May <span class="say-no-more"> 2017</span></time>
                            <span class="event-location">FH Technikum Wien, Höchstädtplatz 6, 1200 Vienna, Austria</span>
                        </p>
                    </li>
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/463/">GeoPython 2017</a></h3>
                        <p>
                            <time datetime="2017-05-08T00:00:00+00:00">08 May &ndash; 11 May <span class="say-no-more"> 2017</span></time>
                            <span class="event-location">Basel, Switzerland</span>
                        </p>
                    </li>
                </ul>
                <h2 class="widget-title"><span aria-hidden="true" class="icon-calendar"></span>Upcoming Events1</h2>
                <ul class="list-recent-events menu">
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/463/">GeoPython 2017</a></h3>
                        <p>
                            <time datetime="2017-05-08T00:00:00+00:00">08 May &ndash; 11 May <span class="say-no-more"> 2017</span></time>
                            <span class="event-location">Basel, Switzerland</span>
                        </p>
                    </li>
                </ul>
                <h2 class="widget-title"><span aria-hidden="true" class="icon-calendar"></span>Upcoming Events2</h2>
                <ul class="list-recent-events menu">
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/463/">GeoPython 2017</a></h3>
                        <p>
                            <time datetime="2017-05-08T00:00:00+00:00">08 May &ndash; 11 May <span class="say-no-more"> 2017</span></time>
                            <span class="event-location">Basel, Switzerland</span>
                        </p>
                    </li>
                </ul>
            </div>
            <h3 class="widget-title just-missed">You just missed...</h3>
            <ul class="list-recent-events menu">
                <li>
                    <h3 class="event-title"><a href="/events/python-events/473/">PyCon SK 2017</a></h3>
                    <p>
                        <time datetime="2017-03-10T00:00:00+00:00">10 March &ndash; 13 March <span class="say-no-more"> 2017</span></time>
                        <span class="event-location">Bratislava, Slovakia</span>
                    </p>
                </li>
                <li>
                    <h3 class="event-title"><a href="/events/python-events/496/">PyCon Philippines 2017</a></h3>
                    <p>
                        <time datetime="2017-02-25T00:00:00+00:00">25 Feb. &ndash; 27 Feb. <span class="say-no-more"> 2017</span></time>
                        <span class="event-location">Cagayan de Oro City, Philippines</span>
                    </p>
                </li>
            </ul>
        </div>
    </section>
    <aside class="right-sidebar" role="secondary">
        <div class="sidebar-widget subscribe-widget">
            <h2 class="widget-title">Python Event Subscriptions</h2>
            <p>Subscribe to Python Event Calendars:</p>
            <ul class="menu">
                <li><a href="https://www.google.com/calendar/ical/j7gov1cmnqr9tvg14k621j7t5c@group.calendar.google.com/public/basic.ics"><span aria-hidden="true" class="icon-ical"></span>Events in iCal format</a></li>
            </ul>
            <h2 class="widget-title">Python Events Calendars</h2>
            <br>
            <p>For Python events near you, please have a look at the <a href="http://lmorillas.github.io/python_events/"><b>Python events map</b></a>.</p>
            <p>The Python events calendars are maintained by the <a href="https://wiki.python.org/moin/PythonEventsCalendar#Python_Calendar_Team">events calendar team</a>.</p>
            <p>Please see the <a href="https://wiki.python.org/moin/PythonEventsCalendar">events calendar project page</a> for details on how to <a href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event">submit events</a>, <a href="https://wiki.python.org/moin/PythonEventsCalendar#Available_Calendars">subscribe to the calendars</a>, get <a href="https://twitter.com/PythonEvents">Twitter feeds</a> or embed them.</p>
            <p>Thank you.</p>
        </div>
    </aside>
</div>
</body>
</html>
'''
class MyOpenurl(object):
    def __init__(self,url):
        self.headers = {'Connection': 'Keep-Alive',
           'Accept': 'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, ' \
                     + 'application/x-ms-xbap, */*',
           'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
           'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; ' \
                         +'.NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; ' \
                         +'.NET4.0C; .NET4.0E)'}
        self.url = request.Request(url,headers=self.headers)

    def openurl(self):
        with request.urlopen(self.url) as url_rsp:
            html = url_rsp.read().decode('utf-8', 'ignore')
            return html

def main():
    print('============================已字符串方式获取网页数据============================')
    myparser = MyHtmlParser()
    myparser.feed(htmldata)
    pprint(myparser.allEvents)
    myparser.close()
    print('============================已urllib方式获取网页数据============================')
    url = "https://www.python.org/events/python-events/"
    hmtl = MyOpenurl(url)
    myparser1 = MyHtmlParser()
    myparser1.feed(hmtl.openurl())
    pprint(myparser1.allEvents)
    myparser1.close()


if __name__ == '__main__':
    main()
