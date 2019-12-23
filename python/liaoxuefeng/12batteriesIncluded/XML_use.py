# XML
# DOM vs SAX
# 操作 XML有两种方法：DOM和 SAX
# DOM会把整个 XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点
# SAX是流模式，边读边解析，占用内存小，解析快，缺点是需要手动处理事务

# SAX操作
# 节点 <a href="/">python</a>
# 1. start_element. end_element, char_data
# 2. start_element事件在读取 <a href="/">时
# 3. char_data事件在读取 python时
# 4. end_element事件在读取 </a>时

from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print ('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print ('sax:end_element: %s' % name)

    def char_data(self, text):
        print ('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)

# 读取一大段字符串时，CharacterDataHandler可能被多次调用，所以需要保存起来，在 EndElementHandler里合并


# 生成 XML
def generatorXML():
    L = []
    L.append(r'<?xml version="1.0"?>')
    L.append(r'<root>')
    L.append(encode('some & data'))
    L.append(r'</root>')
    return ''.join(L)



