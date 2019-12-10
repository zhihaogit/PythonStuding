# 数据读写不一定总是文件，还可以在内存中读写
# StringIO在内存中读写 str
from io import StringIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')

# getvalue()获取写入后的str
content = f.getvalue()
# print (content)

# 读取StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print (s.strip())


# BytesIO
# 操作字符串用 StringIO，操作二进制数据用 BytesIO
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))

content = f.getvalue()
# 写入的不是 str，而是经过 UTF-8编码的 bytes

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
content = f.read()
print(content)
