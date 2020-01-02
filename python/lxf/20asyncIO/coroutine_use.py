# 协程，又称微线程，纤程，Coroutine
# 子程序是通过栈实现的，按照层级调用，一个线程就是执行一个子程序
# 子程序调用总是一个入口，一次返回，调用的顺序是明确的
# 协程看起来也是子程序，但在执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行

def A():
    print ('1')
    print ('2')
    print ('3')

def B():
    print ('x')
    print ('y')
    print ('z')
# 在协程中执行时，可能出现的结果是
'''
1
2
x
y
3
z
'''
# 协程的特点在于是在一个线程执行
# 与多线程比，最大的优势是
# 协程极高的执行效率，因为子程序切换不是线程切换，而是由程序自身控制，因此没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势越明显
# 第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了

# 利用多核 CPU，最简单的方式就是 多进程 + 协程

# python对协程的支持是通过 generator实现
# 在 generator中，不但可以通过 for循环来迭代，还可以不断调用 next()函数获取由 yield语句返回的下一个值
# yield不但可以返回一个值，还可以接受调用者发出的参数


# demo 生产者生产消息后，直接通过 yield跳转到消费者开始执行，待消费者执行完毕后，切换回生产者继续生产，效率高
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print ('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print ('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print ('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)

# 子程序就是协程的一种特例
