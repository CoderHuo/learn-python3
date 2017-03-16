#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from html.parser import HTMLParser
from html.entities import name2codepoint

__author__ = 'Mr.Huo'


class MyHtmlParser(HTMLParser):
    def __init__(self):
        super(MyHtmlParser, self).__init__()
        self.levels = 0
        self.events = {}
        self.event = []
        self.keys = []
        self.key_count_1 = 0
        self.key_count_2 = 0
        self.key_count_3 = 0
        self.tag = ('div', 'h2', 'h3', 'ul', 'li', 'time', 'span')
        self.tagclass = ('most-recent-events', 'shrubbery',
                         'widget-title', 'list-recent-events menu',
                         'event-title', 'say-no-more',
                         'event-location', 'widget-title just-missed'
                         )
        self.flag = {'div_1': False, 'div_2': False, 'h2': False, 'h3_1': False, 'h3_2': False,
                     'ul': False, 'li': False, 'time': False, 'span_1': False, 'span_2': False}

    def __str__(self):
        return str(self.events)

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
                        if value == self.tagclass[0]:
                            self.flag['div_1'] = True
                            self.levels += 1
                        elif value == self.tagclass[1]:
                            self.flag['div_2'] = True
                            self.levels += 1
                        elif value == self.tagclass[2]:
                            self.flag['h2'] = True
                            self.levels += 1
                        elif value == self.tagclass[3]:
                            self.flag['ul'] = True
                            self.levels += 1
                        elif value == self.tagclass[4]:
                            self.flag['h3_1'] = True
                            self.levels += 1
                        elif value == self.tagclass[5]:
                            self.flag['span_1'] = True
                            self.levels += 1
                        elif value == self.tagclass[6]:
                            self.flag['span_2'] = True
                            self.levels += 1
                        elif value == self.tagclass[7]:
                            self.flag['h3_2'] = True
                            self.levels += 1
                    elif key == 'datetime':
                        self.flag['time'] = True
                        self.levels += 1
            else:
                if tag == self.tag[4]:
                    self.flag['li'] = True
                    self.levels += 1

    # Overridable -- handle end tag: <tag.../>
    def handle_endtag(self, tag):
        if tag == self.tag[0]:
            if self.flag['div_2']:
                self.flag['div_2'] = False
                self.levels -= 1
            elif self.flag['div_2'] == False and self.flag['div_1']:
                self.flag['div_1'] = False
                self.levels -= 1
        elif tag == self.tag[1]:
            self.flag['h2'] = False
            self.levels -= 1
        elif tag == self.tag[2]:
            if self.flag['h3_1']:
                self.flag['h3_1'] = False
                self.levels -= 1
            elif self.flag['h3_1'] == False and self.flag['h3_2']:
                self.flag['h3_2'] = False
                self.levels -= 1
        elif tag == self.tag[3]:
            self.flag['ul'] = False
            self.levels -= 1
        elif tag == self.tag[4]:
            self.flag['li'] = False
            self.levels -= 1
            print('------------')
        elif tag == self.tag[5]:
            self.flag['time'] = False
            self.levels -= 1
        elif tag == self.tag[6]:
            if self.flag['span_1']:
                self.flag['span_1'] = False
                self.levels -= 1
            elif self.flag['span_2']:
                self.flag['span_2'] = False
                self.levels -= 1

    # Overridable -- handle character reference  &#
    def handle_charref(self, name):
        pass

    # Overridable -- handle entity reference
    def handle_entityref(self, name):
        pass

    # Overridable -- handle data
    def handle_data(self, data):
        if self.flag['div_1']:
            if self.flag['div_2']:
                if self.flag['h2']:
                    self.keys.append(data)
                    dt = {self.keys[self.key_count_1]: []}
                    self.key_count_1 += 1
                    self.events.update(dt)
                    print(self.keys, self.key_count_1)
                elif self.flag['li']:
                    if self.flag['h3_1']:
                        key1 = self.keys[self.key_count_1 - 1]
                        key2 = len(self.events[key1])
                        print('h3_1',key2)
                        if key2 ==0:
                            self.events[key1].append([data])
                        else:
                            #key2 = len(self.events[key1][key2-1])
                            self.events[key1][key2-1].append(data)
                    if self.flag['time'] and self.flag['span_1'] == False:
                        key1 = self.keys[self.key_count_1 - 1]
                        key2 = len(self.events[key1])
                        print('time',key2)
                        if key2 ==0:
                            self.events[key1].append([data])
                        else:
                            self.events[key1][key2-1].append(data)
                    if self.flag['span_2']:
                        key1 = self.keys[self.key_count_1 - 1]
                        key2 = len(self.events[key1])
                        print('span_2',key2)
                        if key2 ==0:
                            self.events[key1].append([data])
                        else:
                            self.events[key1][key2-1].append(data)
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


def main():
    myparser = MyHtmlParser()
    myparser.feed(htmldata)
    print(myparser)
    print(myparser.levels)
    myparser.close()
    pass


if __name__ == '__main__':
    main()
