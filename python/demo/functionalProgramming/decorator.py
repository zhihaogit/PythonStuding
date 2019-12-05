'''
在面向对象(oop)的设计模式中，decorator被称为装饰模式
OOP的装饰模式需要通过继承和组合来实现
python的 decorator可以用函数实现，也可以用类实现
decorator可以增强函数的功能，定义复杂，使用灵活和方便
'''
import functools, time

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print ('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
# log函数是一个 decorator，所以接受一个函数作为参数，并返回一个函数，借助 @语法，把 decorator置于函数的定义处

def logText(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            # wrapper.__name__ =  func.__name__
            print ('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

# @log
@logText('execute')
def now():
    print('2019-12-05')
# 相当于 执行了 now = log(now)
# 原来的函数保留，只是 now变量指向了新的函数

# f = now
# print (now.__name__, f.__name__)
print (now(), now.__name__)


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        fn(*args, **kw)
        end = time.time()
        result = end - start
        print('%s executed in %s ms' % (fn.__name__, result))
        return result
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

fast(12, 13)







