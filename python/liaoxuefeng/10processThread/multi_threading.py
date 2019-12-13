# 线程是操作系统直接支持的执行单元，Python的线程是真正的Posix Thread，不是模拟出来的
# _thread是低级模块，threading是高级模块，对 _thread进行封装
'''
import time, threading

# 新线程执行的代码
def loop():
    print ('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print ('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print ('thread %s ended.' % threading.current_thread().name)

print ('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target = loop, name = 'LoopThread')
t.start()
t.join()
print ('thread %s ended.' % threading.current_thread().name)
'''
# 启动一个线程就是把一个函数传入并创建 Thread实例，然后调用 start()启动
# 任何进程默认会启动一个线程，这个线程叫做 主线程，主线程又可以启动 新的线程
# current_thread()返回当前线程的实例
# 主线程实例的名字叫 MainThread，子线程的名字没有意义，会被自动命名为 Thread-1, Thread-2


# Lock
# 多进程中，同一个变量各自有份拷贝存在于每个进程中，互不影响
# 多线程中，所有变量都由所有线程共享，任何一个变量都可以被任一线程修改
import time, threading

balance = 0

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

# def run_thread(n):
#     for i in range(1000000):
#         change_it(n)
lock = threading.Lock()
def run_thread(n):
    for i in range(100000):
        # 先要获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 最后释放锁，不然会成死线程
            lock.release()

t1 = threading.Thread(target = run_thread, args = (5,))
t2 = threading.Thread(target = run_thread, args = (8,))
t1.start()
t2.start()
t1.join()
t2.join()
print (balance)
# 高级语言中，一句语句在 cpu执行时是若干条语句
# 因为修改 balance需要多条语句，而执行这几条语句时，线程可能中断，从未导致多个线程把同一个对象内容改乱
# 一个线程因为获得了锁，因此其他线程不能同时执行 change_fit()，只能等待，知道锁被释放后，获得该锁以后才能改


# 多核 cpu
'''
解释器有一个 GIL锁（Global Interpreter Lock）
任何线程执行前，必须先获得 GIL锁，每执行 100条字节码，会自动释放 GIL锁
多线程在 Python中只能交替执行，只能用到 1个核
可以使用多进程实现多核任务，每个进程有各自独立的 GIL锁
'''




























