# 多进程（multiprocessing）
# Unix/Linux操作系统提供了 fork()系统调用
# 普通函数调用一次，返回一次，fork()调用一次，返回两次
# 操作系统自动把 当前进程（父进程）复制了一份（子进程），分别在父进程和子进程进行返回
# 子进程永远返回 0，父进程返回子进程的ID
# 一个父进程可以 fork出很多子进程，子进程使用 getppid()拿到父进程ID

# os模块封装了包括 fork的系统调用
import os

'''
print ('Process (%s) start...' % os.getppid())

pid = os.fork()
if pid == 0:
    print ('I am child process (%s) and my parent is %s.' % (os.getppid(), os.getppid()))
else:
    print ('I (%s) just created a child process (%s).' % (os.getppid(), pid))
'''
print ('-----------------------------------------------------------------------------------------------------------------')

# window上没有 fork调用，可以使用 multiprcocessing模块
# multiprocessing模块提供了一个 process类来代表一个进程对象
from multiprocessing import Process
import os

def run_proc(name):
    print ('Run child process %s (%s)...' % (name, os.getppid()))

'''
if __name__ == '__main__':
    print ('Parent process %s.' % os.getppid())
    p = Process(target = run_proc, args = ('test', ))
    print ('Child process will start')
    p.start()
    p.join()
    print ('Child process end.')
'''
# 创建子进程，只需要传入一个执行函数和函数的参数，创建一个 Process实例，用 start()启动
# join() 可以等待子进程结束后再继续往下运行，通常用于进程间的同步

print ('-----------------------------------------------------------------------------------------------------------------')

# Pool
# 用进程池批量创建子进程
from multiprocessing import Pool
import os, time, random

'''
def long_time_task(name):
    print ('Run task %s (%s)...' % (name, os.getppid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print ('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__ == '__main__':
    print ('Parent process %s.' % os.getppid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args = (i, ))
    print ('Waiting for all subprocessing done...')
    p.close()
    p.join()
    print ('All subprocessing done.')
'''
# 对 Pool对象调用 join()会等待所有子进程执行完毕，调用 join()之前先调用 close()
# 调用 close()之后不再添加新的 Process
# Pool的默认大小是 cpu的核数，不是限制，可以自定义

print ('-----------------------------------------------------------------------------------------------------------------')

# 子进程
# subprocess模块可以启动子进程，并控制其输入和输出
import subprocess
'''
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)
'''

print ('-----------------------------------------------------------------------------------------------------------------')

import subprocess

'''
print ('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
# 使用 communicate()方法输入
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print (output.decode('utf-8'))
print ('Exit code:', p.returncode)
'''

print ('-----------------------------------------------------------------------------------------------------------------')

# 进程间的通信
# Process之间需要通信，multiprocessing模块提供了 Queue, Pipes等多种方式交换数据
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码
def write(q):
    print ('Process to write: %s' % os.getppid())
    for value in ['A', 'B', 'C']:
        print ('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码
def read(q):
    print ('Process to read: %s' % os.getppid())
    while True:
        value = q.get(True)
        print ('Get %s from queue.' % value)

if __name__ == '__main__':
    # 父进程创建 Queue，并传给各个子进程
    q = Queue()
    pw = Process(target = write, args = (q, ))
    pr = Process(target = read, args = (q, ))
    # 启动子进程 pw，写入
    pw.start()
    # 启动子进程 pr，读取
    pr.start()
    # 等待 pw结束
    pw.join()
    # pr 进程里是死循环，只能强制终止
    pr.terminate()











































