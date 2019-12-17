# Base64是一种用 64个字符来表示任意二进制数据的方法
# Base64会把3字节的二进制数据编码成4字节的文本数据，长度增加33%，好处是编码后的文本数据在邮件和网页直接显示
# 不满足 3的倍数，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候自动去掉

# 内置的 base64
import base64
base64.b64encode(b'binary\x00string')
base64.b64decode(b'YmluYXJ5AHN0cmluZw==')

# 标准 Base64编码可能会出现 +和 /，在 url中不能直接作为参数，有一种 url safe的 base64编码，把 + /分别变成 - _
base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
base64.urlsafe_b64decode('abcd--__')