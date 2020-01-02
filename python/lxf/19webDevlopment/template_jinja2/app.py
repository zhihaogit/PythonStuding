# MVC model-view-controller
# python处理 url的函数是 c
# 包含变量的 {{ name }}的模板的是 v
# model是用来传给 view的，view需要替换变量，就可以从 model中取出相应的数据
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods = ['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods = ['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return render_template('signin-ok.html', username = username)
    return render_template('form.html', message = 'Bad username or password', username = username)

if __name__ == '__main__':
    app.run()

# flask默认支持的模板是 jinja2
# 安装 jinja2
# pip install jinja2