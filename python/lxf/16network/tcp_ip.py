'''
互联网协议包含了上百种协议标准，最重要的是 tcp和 ip协议
大家把互联网的协议简称为 TCP/IP协议
互联网上每个计算机的唯一标识是 IP地址
IP地址对应的实际上是计算机的网络接口，通常是网卡
IP包的特点是 按块发送，途径多个路由，但不保证能到达，也不能保证顺序到达

IP地址实际上是一个 32位整数（IPv4）
IPv6地址是一个 128位整数，是目前使用的 IPv4的升级版

TCP协议建立在 IP协议上，负责在两台计算机之间建立可靠连接，保证数据包按顺序到达
会通过握手建立连接，对每个 IP编号，确保对方按顺序收到，包丢了，就自动重发

常用的更高级协议都是建立在 TCP协议基础上，如 HTTP，SMTP

一个 TCP报文除了包含要传输的数据外，还包含源 IP地址和目标 IP地址，源端口和目标端口
端口用来区分一台计算机上同时运行的网络程序
每个网络程序都向操作系统申请唯一的端口号
'''