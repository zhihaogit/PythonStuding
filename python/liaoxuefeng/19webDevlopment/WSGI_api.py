# web应用的本质
'''
1. 浏览器发送一个 HTTP请求
2. 服务器收到请求，生成一个 HTML文档
3. 服务器把 HTML文档作为 HTTP响应的 Body发送给浏览器
4. 浏览器收到 HTTP响应，从 HTTP Body取出 HTML文档并显示
'''
# 最简单的 Web应用就是先把 HTML用文件保存好
# 用现成的 HTTP服务器软件，接收用户请求，从文件中读取 HTML，返回
# Apache,Nginx,Lightted等静态服务器就是干这件事的

# 不用接触到 TCP连接、HTTP原始请求和响应格式，使用一个统一的接口 WSGI（Web Server Gateway Interface），更专心于业务

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]

# 上面的 application()函数就是符合 WSGI标准的 HTTP处理函数
# environ: 一个包含所有 HTTP请求信息的 dict对象
# start_response: 一个发送 HTTP响应的函数
# Header只能发送一次，就是只能调用一次 start_response()函数
# start_response函数接收，一个 HTTP响应码和一个一组 list表示的 HTTP Header
# 每个 Header用一个包含两个 str的 tuple表示

# python内置了 WSGI服务器，wsgiref