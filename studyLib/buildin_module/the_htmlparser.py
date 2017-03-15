#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from html.parser import HTMLParser
from html.entities import name2codepoint

__author__ = 'Mr.Huo'


class MyHtmlParser(HTMLParser):
    def __init__(self):
        super(MyHtmlParser, self).__init__()
        self.li_flag   = False
        self.h2_flag   = False
        self.h3_flag   = False
        self.p_flag    = False
        self.time_flag = False
        self.span_flag = False
        self.div_flag  = False
        self.ul_flag   = False
        self.events    = {}

    # Overridable -- finish processing of start+end tag: <tag.../>
    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    # Overridable -- handle start tag: <tag>
    def handle_starttag(self, tag, attrs):
        if tag == 'div' and attrs:
            for key,value in attrs:
                if key == 'class' and value == 'most-recent-events':
                    self.div_flag = True
        elif tag == 'h2' and attrs:
            for key,value in attrs:
                if key == 'class' and value == 'widget-title':
                    self.h2_flag = True
        elif tag == 'ul' and attrs:
            for key,value in attrs:
                if key == 'class' and value == 'list-recent-events menu':
                    self.ul_flag = True
        elif tag == 'li' :
            self.li_flag = True

        pass

    # Overridable -- handle end tag: <tag.../>
    def handle_endtag(self, tag):
        if tag == 'div':
            self.div_flag  = False
        elif tag  == 'h2':
            self.h2_flag   = False
        elif tag  == 'h3':
            self.h3_flag   = False
        elif tag  == 'li':
            self.li_flag   = False
        elif tag  == 'time':
            self.time_flag = False
        elif tag  == 'p':
            self.p_flag    = False
        elif tag  == 'h3':
            self.h3_flag   = False
        elif tag  == 'ul':
            self.ul_flag   = False

    # Overridable -- handle character reference  &#
    def handle_charref(self, name):
        pass

    # Overridable -- handle entity reference
    def handle_entityref(self, name):
        pass

    # Overridable -- handle data
    def handle_data(self, data):
        if self.li:
            print('data=%s' % data)
        pass

    # Overridable -- handle comment
    def handle_comment(self, data):
        print('comment=%s' % data)
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
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/498/">Rencontres Django 2017</a></h3>
                        <p>
                            <time datetime="2017-04-01T00:00:00+00:00">01 April &ndash; 03 April <span class="say-no-more"> 2017</span></time>
                            <span class="event-location">Toulon, France</span>
                        </p>
                    </li>
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/467/">DjangoCon Europe 2017</a></h3>
                        <p>
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
    myparser.close()
    pass


if __name__ == '__main__':
    main()
