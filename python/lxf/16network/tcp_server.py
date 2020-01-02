import socket
import threading
import time
# 服务器
# 服务器进程首先要绑定一个端口并监听来自其他客户端的连接，如果某个客户端连接过来，就建立 Socket连接
# 一个 Socket依赖 4项：服务器地址、服务器端口、客户端地址、客户端端口来唯一确定一个 Socket
# 服务器的每个连接都需要一个新的进程或者新的线程来处理，达到同时响应多个客户端请求的目的

# 创建一个基于 IPv4和 TCP协议的 Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定监听的地址和端口，可以用 0.0.0.0绑定到所有的网络地址
# 监听端口
s.bind(('127.0.0.1', 9999))

# 监听端口
s.listen(5)
print ('Waiting for connection...')

# 每个连接都必须创建新线程（或进程）来处理，否则单线程在处理连接的过程中，无法接受其他客户端的连接
def tcplink(sock, addr):
    print ('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print ('Connection from %s:%s closed.' % addr)

# 连接建立后，服务器首先发一条欢迎消息，然后等待客户端连接，并加上 Hello在发送给客户端
# 如果客户端发送了 exit字符串，就直接关闭连接

# 服务器程序通过一个永久循环来接受来自客户端的连接
# accept()会等待并返回一个客户端的连接
while True:
    # 接受一个新连接
    sock, addr = s.accept()
    # 创建新线程来处理 TCP连接
    t = threading.Thread(target = tcplink, args = (sock, addr))
    t.start()
