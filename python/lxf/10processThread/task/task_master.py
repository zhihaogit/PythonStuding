# 一个服务进程可以作为调度者，将任务分布到其他多个进程，依靠网络通信
# 发送任务的进程
import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()

# 从 BaseManager继承的 QueueManager
class QueueManager(BaseManager):
    pass

# 把两个 Queue都注册到网络上，callable参数关联了Queue对象
QueueManager.register('get_task_queue', callable = lambda: task_queue)
QueueManager.register('get_result_queue', callable = lambda: result_queue)
# 绑定端口 5000，设置验证码 'abc'
manager = QueueManager(address = ('', 5000), authkey = b'abc')
# 启动 Queue
manager.start()
# 获得通过网络访问的 Queue对象：
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放几个任务进去
for i in range(10):
    n = random.randint(0, 10000)
    print ('put task %d...' % n)
    task.put(n)
# 从 result队列读取结果
print ('Try get results...')
for i in range(10):
    r = result.get(timeout = 10)
    print ('Result: %s' % r)
# 关闭
manager.shutdown()
print ('master exit.')

# 在分布式多进程环境下，添加任务到 Queue不可以直接对原始的 task_queue进行操作