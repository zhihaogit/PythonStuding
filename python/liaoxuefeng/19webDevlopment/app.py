# -- coding: utf-8 --
# 每个 url可以对应 get，post，put，delete请求
# 从 environ变量中取出 http请求的信息，然后逐个判断
def application1(environ, start_response):
    method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']
    if method == 'GET' and path == '/':
        return handle_home(environ, start_response)
    if method == 'POST' and path == '/signin':
        return handle_signin(environ, start_response)

# 需要在 WSGI接口之上进一步抽象，专注于一个函数处理一个 url，至于 url到函数的映射，可以交给 web框架
# 使用 flask框架
# pip install flask

# flask通过 python的装饰器在内部自动把 url和函数关联起来
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods = ['GET'])
def signin_from():
    return '''<form action="/signin" method="post">
        <p><input name="username"></p>
        <p><input name="password" type="password"></p>
        <p><button type="submit">Sign In</button></p>
    </form>'''

# @app.route('/signin', methods = ['POST'])
@app.route('/signin', methods=['POST'])
def sigin():
    # 需要从 request对象中读取表单内容
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello, admin</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()

# 常见 python web框架
'''
Django: 全能型 web框架
web.py: 小巧的 web框架
Bottle: 和 Flask类似的 web框架
Tornado: Facebook的开源异步 web框架
'''