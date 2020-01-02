# asyncio是 python3.4版本引入的标准库，直接内置了对异步 IO的支持
# asyncio的编程就是一个消息循环
# 从 asyncio模块直接获取一个 EventLoop的引用，然后把需要执行的协程扔进 EventLoop中执行，就实现了异步 IO
import asyncio

@asyncio.coroutine
def hello():
    print ('Hello world!')
    # 异步调用 asyncio.sleep(1)
    r = yield from asyncio.sleep(1)
    print ('Hello again!')

# 获得 EventLoop
loop = asyncio.get_event_loop()
# 执行 coroutine
loop.run_until_complete(hello())
loop.close()




# 两个 coroutine是由同一个线程并发执行的
import threading
import asyncio

@asyncio.coroutine
def hello():
    print ('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print ('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()




import asyncio

@asyncio.coroutine
def wget(host):
    print ('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP /1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print ('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn',  'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
