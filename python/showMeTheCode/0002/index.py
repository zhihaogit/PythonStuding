# 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中
import sys, os
curPath = os.path.realpath(__file__)
modulePath = os.path.dirname(curPath)
sys.path.append(modulePath + '/../0001')
from index0001 import generateString
import MySQLdb

KEY_LEN = 20
KEY_ALL = 200
randomList = generateString(KEY_ALL, KEY_LEN)

class mysqlInit(object):
    def __init__(self, conn):
        self.conn = None

    # connect to mysql
    def connect(self):
        self.conn = MySQLdb.connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            password = 'password',
            db = 'test',
            charset = 'utf8'
        )

    def cursor(self):
        try:
            return self.conn.cursor()
        except (AttributeError, MySQLdb.OperationalError):
            self.connect()
            return self.conn.cursor()

    def commit(self):
        return self.conn.commit()

    def close(self):
        return self.conn.close()

def process():
    dbconn.connect()
    conn = dbconn.cursor()
    DropTable(conn)
    CreateTable(conn)
    InsertDatas(conn)
    QueryData(conn)
    dbconn.close()

def query(sql, conn):
    '''查询 sql'''
    conn.execute(sql)
    rows = conn.fetchall()
    return rows

def DropTable(conn):
    conn.execute('DROP TABLE IF EXISTS `user_key`')

def CreateTable(conn):
    sql_create = '''
        CREATE TABLE `user_key` (`key` varchar(50) NOT NULL)
    '''
    conn.execute(sql_create)

def InsertDatas(conn):
    insert_sql = 'INSERT INTO user_key VALUES (%(value)s)'
    conn.executemany(insert_sql, [dict(value = v) for v in randomList])

def DeleteData():
    del_sql = 'delete from user_key where id=2'
    execute(del_sql)

def QueryData():
    sql = 'select * from user_key'
    rows = query(sql, conn)
    printResult(rows)

def printResult(rows):
    if rows is None:
        print ('rows None')
    for row in rows:
        print (row)

if __name__ == '__main__':
    dbconn = mysqlInit(None)
    process()






    







    







    







    







    







    







    







