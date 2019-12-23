# Unicode表示的 str和 bytes两种数据类型，可以通过 encode()和 decode()方法转换
# 未知编码 bytes，要转成 str，需要先猜测编码
# chardet来检测编码

# 安装 chardet
# pip install chardet

# 使用 chardet
# 用 chardet检测编码
import chardet

bytesType = chardet.detect(b'Hello, world!')
print (bytesType)
# {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
# 检测出来是 ascii，confidence字段表示 检测的概率是 1.0(100%)

# 检测 gbk
data = '离离原上草，一岁一枯荣'.encode('gbk')
bytesType2 = chardet.detect(data)
print (bytesType2)
# {'encoding': 'GB2312', 'confidence': 0.7407407407407407, 'language': 'Chinese'}
# gbk是 gb2312的超集，两次是同一种编码，language指出是 chinese

# 检测 utf-8
data = '离离原上草，一岁一枯荣'.encode('utf-8')
bytesType3 = chardet.detect(data)
print (bytesType3)
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}

# 检测日文
data = '最新の主要ニュース'.encode('euc-jp')
bytesType4 = chardet.detect(data)
print (bytesType4)
# {'encoding': 'EUC-JP', 'confidence': 0.99, 'language': 'Japanese'}

# chartdet支持检测中文，日文，韩文等多种语言