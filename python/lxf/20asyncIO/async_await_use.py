# asyncio提供的 @asyncio.coroutine可以把一个 generator标记为 coroutine类型
# 然后在 coroutine内部用 yield from调用另一个 coroutine实现异步操作

# async和 await是针对 coroutine的新语法，只需两步替换
'''
1. 把 @asyncio.coroutine替换为 async
2. 把 yield from替换为 await
'''

import threading
import asyncio

# @asyncio.coroutine
# def hello():
#     print ('Hello world!')
#     r = yield from asyncio.sleep(1)
#     print ('Hello again!')

async def hello():
    print('Hello world! (%s)' % threading.currentThread())
    r = await asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()