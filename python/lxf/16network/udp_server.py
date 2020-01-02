# TCP是建立可靠连接，并且通信双方都可以以流的形式发送数据
# UDP是面向无连接的协议，不需要建立连接，只需要对方的 IP地址和端口号，就可以直接发包，不关心发送效果
# 优点是速度快，适用于不要求可靠到达的数据
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口
s.bind(('127.0.0.1', 9999))

# 创建 Socket时，SOCK_DGRAM指定了类型是 UDP
# 不需要调用 listen()方法，而是直接接受来自任何客户端的数据
print ('Bind UDP on 9999...')
while True:
    # 接收数据
    data, addr = s.recvfrom(1024)
    # recvfrom()方法返回数据和客户端的地址和端口，直接调用 sendto()就可以把数据用 UDP发送给客户端
    print ('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)

# 服务器绑定 UDP端口和 TCP端口互不冲突
# UDP的 9999端口和 TCP的 9999端口可以各自绑定