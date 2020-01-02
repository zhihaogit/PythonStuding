# MySQL是为服务器端设计的数据库，能承受高并发访问，占用内存比 SQLite大
# SQLite特点是轻量级、可嵌入、不能承受高并发访问，适合桌面和移动应用

# 安装 MySQL
# 官网下载 MySQL
# 会提示输入 root用户的口令
# 修改 MySQL配置文件，一般在 /etc/my.cnf或者 /etc/mysql/my.cnf
'''
[client]
default-character-set = utf8

[mysqld]
default-storage-engine = INNODB
character-set-server = utf8
collation-server = utf8_general_ci
'''
# 重启 MySQL，命令行检验编码
 # mysql -u root -p

# 如果 MySQL的版本大于等于 5.5.3，可以把编码设置为 utf8mb4
# utf8mb4和 utf8完全兼容，但支持最新的 Unicode标准，可以显示 emoji

# 安装 MySQL驱动
# 由于 MySQL服务器以独立的进程运行，并通过网络对外服务，所以需要支持 python的 MySQL驱动来连接到 MySQL服务器
# MySQL官方提供了 my-connector-python驱动
# pip install mysql-connector-python --allow-external mysql-connector-python
# 上面失败了，可以试下面一个
# pip install mysql-connector

# 导入 MySQL驱动
import mysql.connector
conn = mysql.connector.connect(user='root', password='password', database='test')
cursor = conn.cursor()
# 创建 user表
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
rowcount = cursor.rowcount()
print (rowcount)
# 提交事务
conn.commit()
cursor.close()
# 运行查询
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print (values)
# 关闭 cursor和 connection
cursor.close()
conn.close()

# 执行 INSERT等操作后，要调用 commit()提交事务
# MySQL的 SQL占位符是 %s
