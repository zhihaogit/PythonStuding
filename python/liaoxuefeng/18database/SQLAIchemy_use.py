# 数据库表是一个二维表，包含多行多列
# 用 python的数据结构表示一个表的内容，一个 list表示多行，list的每一个元素是 tuple，表示一行元素
[
    ('1', 'Michael'),
    ('2', 'Bob'),
    ('3', 'Adam')
]
# python的 DB-API返回的数据结构类似上面
# 用 tuple表示一行很难看出表的结构
# 可以用 class实例表示，更容易看出表结构
class User(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

[
    User('1', 'Michael'),
    User('2', 'Bob'),
    User('3', 'Adam')
]

# ORM (Object-Relational Mapping)，把关系数据库的表结构映射到对象上
# ORM框架来实现这个转换
# python中最有名的是 SQLAlchemy

# 安装 SQLAlchemy
# pip install sqlalchemy

# 导入 SQLAlchemy，并初始化 DBSession
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()

# 定义 User对象
class User(Base):
    # 表的名字
    __tablename__ = 'user'

    # 表的结构
    id = Column(String(20), primary_key = True)
    name = Column(String(20))

# 初始化数据库连接
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
# 创建 DBSession类型
DBSession = sessionmaker(bind = engine)

# 如果有多个表，就继续定义其他 class

# create_engine()用来初始化数据库连接，SQLAlchemy用一个字符串表示连接信息
'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'

# 向数据库表中添加一行记录，可以视为添加一个 User对象
# 创建 session对象
session = DBSession()
# 创建新 User对象
new_user = User(id = '5', name = 'Bob')
# 添加到 session
session.add(new_user)
# 提交即保存到数据库
session.commit()
# 关闭 session
session.close()
# 关键是获取 session，然后把对象添加到 session中，最后提交并关闭
# DBSession对象可视为当前数据库连接

# 从数据库表中查询数据
# 创建 Session
session = DBSession()
# 创建 Query查询，filter是 where条件，最后调用 one()返回唯一行，如果调用 all()则返回所有行
user = session.query(User).filter(User.id == '5').one()
# 打印类型和对象的 name属性
print ('type:', type(user))
print ('name:', user.name)
# 关闭 session
session.close()
# ORM就是把数据库表的行与相应的对象建立关联，互相转换

# 由于关系数据库的多个表可以用外键实现一对多，多对多等关联
# ORM框架提供了两个对象之间的一对多，多对多等功能
class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key = True)
    name = Column(String(20))
    # 一对多
    books = reationship('Book')

class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key = True)
    name = Column(String(20))
    # 多 的一方的book表是通过外键关联到 user表的
    user_id = Column(String(20), ForeignKey('user.id'))








