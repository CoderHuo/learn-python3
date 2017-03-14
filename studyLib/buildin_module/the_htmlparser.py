#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from html.parser import HTMLParser
from html.entities import name2codepoint

__author__ = 'Mr.Huo'


class MyHtmlParser(HTMLParser):
    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)
        print('startendtag %s' % tag)

    # Overridable -- handle start tag
    def handle_starttag(self, tag, attrs):
        print('starttag %s' % tag)
        print('startattrs %s' % attrs)
        pass

    # Overridable -- handle end tag
    def handle_endtag(self, tag):
        print('endtag %s' % tag)
        pass

    # Overridable -- handle character reference
    def handle_charref(self, name):
        print('charref %s' % name)
        pass

    # Overridable -- handle entity reference
    def handle_entityref(self, name):
        print('entityref %s' % name)
        pass

    # Overridable -- handle data
    def handle_data(self, data):
        print('data=%s' % data)
        pass

    # Overridable -- handle comment
    def handle_comment(self, data):
        print('comment=%s' % data)
        pass

    # Overridable -- handle
    def handle_decl(self, decl):
        print('decl=%s' % decl)
        pass

    # Overridable -- handle processing instruction
    def handle_pi(self, data):
        print('pi=%s' % data)
        pass


htmldata = '''<html>
<head>huo shao hua</head>
<body>
<!-- test html parser -->
<p>Some<a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END
</p>
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
