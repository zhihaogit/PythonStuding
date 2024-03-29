# 处理任务的进程
import time, sys, queue
from multiprocessing.managers import BaseManager

# 创建类似的 QueueManager
class QueueManager(BaseManager):
    pass

# 由于这个 QueueManger只从网络上获取 Queue，所以注册时只提供名字：
QueueManager.register('get_task_name')
QueueManager.register('get_result_name')

# 连接到服务器，也就是运行 task_master.py的机器
server_addr = '127.0.0.1'
print ('Connect to server %s...' % server_addr)
# 端口和验证码注意保持与 task_master.py设置的完全一致
m = QueueManager(address = (server_addr, 5000), authkey = b'abc')
# 从网络连接
m.connect()
# 获取 Queue的对象
task = m.get_task_queue()
result = m.get_result_queue()
# 从 task队列获取任务，并把结果写入 result队列
for i in range(10):
    try:
        n = task.get(timeout = 1)
        print ('run task %s * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n * n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print ('task queue is empty')

# end
print ('Worker exit')
