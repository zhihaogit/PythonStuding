# 负责启动 WSGI服务器，加载 application()函数

# 从 wsgiref模块导入
from wsgiref.simple_server import make_server
# 导入 application函数
from WSGI_api import application

# 创建服务，IP为空，端口为 8000，处理函数为 application
httpd = make_server('', 8000, application)
print ('Serving HTTP on port 8000...')
# 开始监听 HTTP请求
httpd.serve_forever()