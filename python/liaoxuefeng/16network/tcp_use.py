# 客户端
# 大多数连接都是可靠的 tcp连接
# 创建 tcp连接时，主动发起连接的叫客户端，被动响应连接的叫服务器

# 导入 socket库
import socket

# 创建一个 socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET指定使用 IPv4协议
# IPv6是 AF_INET6
# SOCK_STREAM指定使用面向流的 TCP协议

# 建立连接
s.connect(('www.sina.com.cn', 80))
# 80端口是 web服务的标准端口

# 建立 TCP连接后，向服务器发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据
buffer = []
while True:
    # 每次最多接收 1k字节
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

data = b''.join(buffer)
# 循环反复接收，知道 recv()返回空数据，表示接收完毕，退出循环

# 接收完数据，关闭 socket
s.close()

# 接收到的数据包括 HTTP头和网页本身，只需要把 HTTP头和网页分离一下，把 HTTP头打印出来，网页保存到文件
header, html = data.split(b'\r\n\r\n', 1)
print (header.decode('utf-8'))
# 把接收的数据写入文件
with open('sina.html', 'wb') as f:
    f.write(html)




























































































