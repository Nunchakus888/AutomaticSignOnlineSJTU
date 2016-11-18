# /usr/bin/python
# coding=utf-8

from HTMLParser import HTMLParser


class MyParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)

    """一个简单的HTMLparser的例子"""

    def handle_decl(self, decl):
        """处理头文档"""
        HTMLParser.handle_decl(self, decl)
        print decl

    def handle_starttag(self, tag, attrs):
        """处理起始标签"""
        HTMLParser.handle_starttag(self, tag, attrs)
        if tag == 'tr' and len(attrs) == 1:
            mm = tag
            print 'tag-->', tag
            print 'attrs-->', attrs

    def handle_data(self, data):
        """处理文本元素"""
        HTMLParser.handle_data(self, data)
        print data,

    def handle_endtag(self, tag):
        """处理结束标签"""
        HTMLParser.handle_endtag(self, tag)
        if not HTMLParser.get_starttag_text(self).endswith("/>"):
            print "</", tag, ">"

    def handle_startendtag(self, tag, attrs):
        """处理自闭标签"""
        HTMLParser.handle_startendtag(self, tag, attrs)
        print HTMLParser.get_starttag_text(self)

    def handle_comment(self, data):
        """处理注释"""
        HTMLParser.handle_comment(self, data)
        print data
        return data

    def close(self):
        HTMLParser.close(self)
        print "parser over"

