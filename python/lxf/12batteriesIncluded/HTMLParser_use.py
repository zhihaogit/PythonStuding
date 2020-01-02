# 编写搜索引擎
# 第一步用爬虫把目标网站的页面抓下来
# 第二步解析 HTML页面
# HTML本质上是 XML的子集

from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starting(self, tag, attrs):
        print ('<%s>' % tag)

    def handle_ending(self, tag):
        print ('</%s>' % tag)

    def handle_startending(self, tag, attrs):
        print ('<%s>' % tag)

    def handle_data(self, data):
        print (data)

    def handle_comment(self, data):
        print ('<!--', data, '-->')

    def handle_entityref(self, name):
        print ('&%s;' % name)

    def handle_charref(self, name):
        print ('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')

# feed()方法可以多次调用，可以把字符串分次传进去
# 特殊字符：
# 一种英文表示的 &nbsp;
# 一种数字表示的 &#1234;
# 都可以通过 Parser解析出来