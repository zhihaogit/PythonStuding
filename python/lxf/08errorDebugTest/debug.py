# 需要一整套调试程序来修复 bug
# 第一种方式
# 直接打印可能有问题的变量
def foo(s):
    n = int(s)
    print ('>>> n = %d' % n)
    return 10 / n

def main():
    foo('0')

# main()


# 第二种方式
# 断言(assert)
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

# main()
# 如果断言失败，assert语言本身就会抛出 AssertionError
# 启动解释器的时候，可以用 -O参数来关闭 assert


# 第三种方式
# 把 print换成 logging，logging不会抛出错误，可以输出到文件
import logging

s = '0'
n = int(s)
logging.info('n = %d' % n)
# print (10 / n)
'''
允许指定记录信息的级别，有以下级别
debug
info
warning
error
'''


# 第四种方式
# pdb调试器，让程序以单步方式运行，可以随时查看运行状态
import pdb
s = '0'
n = int(s)
# 在可能出错的地方放一个 pdb.set_trace()，设置一个断点
pdb.set_trace()
print (10 / n)

'''
python -m pdb err.py启动调试器
1 来查看代码
n 来单步执行代码
p 变量名 来查看变量
q 结束调试，退出程序

pdb.set_trace()
p 查看变量
c 继续运行
'''










