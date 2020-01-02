# SQLite是嵌入式数据库，它的数据库是一个文件
# python内置了 SQLite3，直接使用
# 几个概念
# 表是数据库中存放关系数据的集合，一个数据库里面通常包含多个表
# 要操作关系数据库，首先需要连接到数据库，一个数据库连接称为 Connection
# 连接到数据库后，需要打开游标（Cursor），通过 Cursor执行 SQL语句，然后获得执行结果

# 导入 SQLite驱动
import sqlite3
# 连接到 SQLite数据库
# 数据库文件是 test.db
# 如果文件不存在，弧自动在当前目录创建
conn = sqlites.connect('test.db')
# 创建一个 Cursor
cursor = conn.cursor()
# 执行一条 SQL语句，创建 user表
cursor.execute('create table user (id varchart(20) primary key, name varchart(20))')
# 继续执行一条 SQL语句，插入一条记录
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# 通过 rowcount获得插入的行数
rowCount = cursor.rowcount
print (rowcount)
# 关闭 Cursor
cursor.close()
# 提交事务
conn.commit()
# 关闭 Connection
conn.close()


# 查询记录
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# 执行查询语句
cursor.execute('select * from user where id=?', ('1', ))
# 获得查询结果集
values = cursor.fetchall()
print (values)
cursor.close()
conn.close()


# 最后关闭 Connection和 Cursor
# 使用 Cursor对象执行 insert, update, delete语句时，执行结果由 rowcount返回影响的行数，就可以拿到执行结果
# 使用 Cursor对象执行 select语句时，通过 featchall()可以拿到结果集，结果集是一个 list,每个元素都是一个 tuple，对应一行记录

# SQL语句带有参数，需要把参数按位置传递给 execute()，?对应 参数
cursor.execute('select * from user where name=? and pwd=?', ('abc', 'password'))
