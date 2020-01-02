# ThreadLocal
# 全局存放数据，方便每个线程读写
import threading

# 创建全局 ThreadLocal对象
local_school = threading.local()

def process_student():
    # 获取当前线程关联的 student
    std = local_school.student
    print ('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定 ThreadLocal的 student
    local_school.student = name
    process_student()

t1 = threading.Thread(target = process_thread, args = ('Alice', ), name = 'Thread-A')
t2 = threading.Thread(target = process_thread, args = ('Bob', ), name = 'Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

# ThreadLocal的实例 可以看成是全局变量，每个属性都是线程的局部变量，可以被线程任意读写而互不干扰，也不用管理锁的问题
