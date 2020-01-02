# asyncio可以实现单线程并发 IO操作，作用于客户端，效果不大
# 用在 服务端，由于 http连接是 io操作，因此可以用单线程+coroutine实现多用户的高并发支持
# asyncio实现了 TCP、UDP、SSL等协议
# aiohttp则是基于 asyncio实现的 http框架

# 安装 aiohttp
# pip install aiohttp

# 编写 http服务器，处理 url
import asyncio

from aiohttp import web

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body = b'<h1>Index</h1>')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body = text.encode('utf-8'))

async def init(loop):
    app = web.Application(loop = loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print ('Server started at http://127.0.0.1:8000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()