#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from html.parser import HTMLParser
from html.entities import name2codepoint

__author__ = 'Mr.Huo'


class MyHtmlParser(HTMLParser):
    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)
        print('startendtag <%s>' % tag)

    # Overridable -- handle start tag
    def handle_starttag(self, tag, attrs):
        print('starttag <%s>' % tag)
        print('startattrs %s' % attrs)
        pass

    # Overridable -- handle end tag
    def handle_endtag(self, tag):
        print('endtag </%s>' % tag)
        pass

    # Overridable -- handle character reference
    def handle_charref(self, name):
        pass

    # Overridable -- handle entity reference
    def handle_entityref(self, name):
        pass

    # Overridable -- handle data
    def handle_data(self, data):
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


htmldata = '''<html html=1>
<head head=1 head1=2>huo shao hua</head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>
'''


def main():
    myparser = MyHtmlParser()
    myparser.feed(htmldata)
    myparser.close()
    pass


if __name__ == '__main__':
    main()
