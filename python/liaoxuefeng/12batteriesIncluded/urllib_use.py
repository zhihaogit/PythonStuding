# urllib提供了一系列用于操作 URL的功能
# Get
# urllib的 request模块很方便抓取 url内容
import urllib.request

with urllib.request.urlopen('https://www.baidu.com/s?wd=%E5%AE%8B%E8%AF%8D') as f:
    data = f.read()
    print ('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print ('%s: %s' % (k, v))
    print ('Data:', data.decode('utf-8'))

