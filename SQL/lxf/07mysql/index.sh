# 安装完 mysql之后，除了 mysql server还有一个 mysql client
# mysql client是命令行客户端

mysql -u root -p
# 输入口令
# 就连上了 mysql server
exit
# 断开与 mysql server的连接并返回到命令提示符

# mysql client的可执行程序是 mysql
# mysql server的可执行程序是 mysqld

# 在 mysql client中输入的 sql语句通过 tcp连接发送到 mysql server
# 默认端口号是 3306
# 如果发送到本机 mysql server，地址是 127.0.0.1:3306

# 也可以只安装 mysql client，然后连接到远程的 mysql server
# 假设 mysql server的 ip地址是 10.0.1.99
# 使用 -h指定 ip或域名
mysql -h 10.0.1.99 -u root -p