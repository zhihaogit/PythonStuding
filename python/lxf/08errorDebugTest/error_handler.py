# try...except...finally...
# try
try:
    print ('try...')
    r = 10 / 0
    print ('result:', r)
except ZeroDivisionError as e:
    print ('except:', e)
finally:
    print ('finally...')
print ('END')

# 多个 except捕获不同类型的错误
try:
    print ('try...')
    r = 10 / int('a')
    print ('result:', r)
except ValueError as e:
    print ('ValueError:', e)
except ZeroDivisionError as e:
    print ('ZeroDivisionError:', e)
# 没有错误，会自动执行 else语句
else:
    print ('no error!')
finally:
    print ('finally...')
print ('END')

# python的错误也是 class，都继承自 BaseException
# except不仅捕获该类型的错误，还会将继承该类型的子类也捕获

# 可以跨越多层调用
# 错误会被从里层向外抛出
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print ('Error:', e)
    finally:
        print ('finally...')
main()

# 记录错误
# 捕获错误，将错误堆栈打印出来，分析错误原因，同时让程序继续执行下去
# 通过配置，还可以把错误记录到日志文件里
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print ('END')

# 抛出错误
# 自定义错误 Class
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')

# 使用内置错误类型
# 捕获错误，向上抛出错误，让顶层调用者去处理
def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print ('ValueError!')
        raise

bar()

# 合理转换错误类型，不应该将一个 IOError转换成 ValueError















