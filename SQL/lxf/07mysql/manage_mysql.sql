-- 管理 mysql
-- 可以使用可视化图形界面 mysql workbench
-- 本质上，workbench和 mysql client命令行都是客户端，和 mysql交互的唯一接口是 SQL

-- 列出所有数据库
SHOW DATABASES;
-- information_schema, mysql, performance_schema和 sys都是系统库

-- 创建一个新数据库
CREATE DATABASE test;

-- 删除一个数据库
-- 即删除该数据库的所有表
DROP DATABASE test;

-- 对一个数据库进行操作时，首先将其切换为当前数据库
USE test;

-- 列出当前数据库的所有表
SHOW TABLES;

-- 查看一个表的结构
DESC students;

-- 查看创建表的 SQL语句
SHOW CREATE TABLE students;

-- 创建表
CREATE TABLE students;

-- 删除表
DROP TABLE students;

-- 给表新增一列
ALTER TABLE students ADD COLUMN birth VARCHAR(10) NOT NULL;

-- 修改 birth列的列名和类型
ALTER TABLE students CHANGE COLUMN birth birthday VARCHAR(20) NOT NULL;

-- 删除列
ALTER TABLE students DROP COLUMN birthday;

-- 退出 mysql
EXIT
-- 只是断开客户端和服务器的连接，mysql server仍然继续运行
