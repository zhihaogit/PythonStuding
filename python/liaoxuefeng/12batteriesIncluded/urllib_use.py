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


# 模拟浏览器发送 GET请求，使用 Request对象，通过向 Request对象添加 HTTP头
from urllib import request

req = request.Request('http://www.douban.com')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print ('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print ('%s: %s' % (k, v))
    print ('Data:', f.read().decode('utf-8'))


# Post请求
# 需要把参数 data以 bytes形式传入
from urllib import request, parse

print ('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data = login_data.encode('utf-8')) as f:
    print ('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print ('%s: %s' % (k, v))
    print ('Data:', f.read().encode('utf-8'))


# Handler
# 更复杂的控制，用 ProxyHandler处理
proxy_handler = urllib.request.ProxyHandler({
    'http': 'http://www.example.com:3128/'
})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
    pass

# urllib的功能是 利用程序去执行各种 http请求
# 需要模拟浏览器完成特定功能，就把请求伪装成浏览器
# 方法是先监控浏览器发出的请求，再根据浏览器的请求头来伪装，User_Agent头来标识浏览器




































