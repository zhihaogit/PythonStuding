# 读写文件之后必须正确关闭它们
# 使用 try...finally
'''
try:
    f.open('/path/file', 'r')
    f.read()
finally:
    if f:
        f.close()

# 使用 with
with open('/path/file', 'r') as f:
    f.read()
'''

# 并不只有 open()函数返回的 fp对象才能使用 with语句
# 任何对象，只要正确实现了上下文管理，就可以用 with语句
# 实现上下文管理是通过 __enter__和 __exit___两个方法来实现
class Query(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print ('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print ('Error')
        else:
            print ('End')

    def query(self):
        print ('Query info about %s...' % self.name)

with Query('Bob') as q:
    q.query()
# Begin
# Query info about Bob...
# End

# @contextmanager
# contextlib提供了简单 __enter__和 __exit__方法
from contextlib import contextmanager

class Query(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print ('Query info about %s...' % self.name)

# @contextmanager 这个 decorator接受一个 generator，用 yield语句把 with...as var把变量输出出去
@contextmanager
def create_query(name):
    print ('Begin')
    q = Query(name)
    yield q
    print ('End')

with create_query('Bob') as q:
    q.query()

# @contextmanager可以在某段代码执行前后自动执行特定代码
@contextmanager
def tag(name):
    print ("<%s>" % name)
    yield
    print ("</%s>" % name)

with tag('h1'):
    print ('hello')
    print ('world')
# 使用 @contextmanager简化上下文管理

# @closing
# 如果一个对象没有实现上下文，就不能把它用于 with语句，可以用 closing()把对象变成上下文对象
'''
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print (line)
'''

# closing也是一个经过 @contextmanager装饰的 generator
# 可以把任意对象变成上下文对象，并支持 with语句
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
