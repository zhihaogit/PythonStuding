# Requests，更方便处理 URL资源
# 安装 Requests
# pip install requests

# 使用 requests
# 通过 get访问一个页面
import requests
r = requests.get('https://www.baidu.com/')
statusCode = r.status_code
responseText = r.text
print (statusCode, responseText)

# 传一个 dict作为 params参数来实现一个带参数的 URL
r2 = requests.get('https://www.douban.com/search', params = {
    'q': 'python',
    'cat': '1001'
})
urlLink = r2.url
print (urlLink)

# requests自动检测编码，可用 encoding属性查看
rE = r2.encoding
print (rE)

# content属性获得 bytes对象，无论文本还是二进制
rC = r2.content
print (rC)

# 对于特定类型的响应，如 JSON，可以直接获取
# r3 = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# print (r3.json())

# 传一个 dict作为 headers参数，当做 HTTP Header
r4 = requests.get('https://www.douban.com/', headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'
})
print (r4.text)

# Post请求
r5 = requests.post('https://accounts.douban.com/login', data = {
    'form_email': 'abc@example.com',
    'form_password': '123456'
})
# 默认使用 application/x-www-form-urlencoded对 post数据编码
# 需要传 JSON，直接传入 JSON参数
params = {
    'key': 'value'
}
r6 = requests.post(url, json = params) #内部序列话为JSON

# 上传文件需要更复杂的编码格式，但是 requests把它简化为 files参数
upload_files = {
    'file': open('report.xls', 'rb')
}
r7 = requests.post(url, files = upload_files)
# 读文件的时候，务必使用 'rb'即二进制模式读取，这样获取的 bytes长度才是文件的长度
# 还有 put(), delete()


# 获取 HTTP响应的其他信息
head = r.headers
contentType = r.headers['Content-Type']

# 获取指定 cookie
r.cookie['ts']

# 传入一个 dict来传入 Cookie
cs = {
    'token': '123456',
    'status': 'working'
}
r8 = requests.get(url, cookies = cs)

# 指定超时
r9 = requests.get(url, timeout = 2.5) # 2.5秒后超时
