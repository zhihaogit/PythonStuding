# 异步 IO
# 当代码需要执行一个耗时的 IO操作时，它只发出 IO指令，并不等待 IO结果，然后就去执行其他代码，一段时间后，当 IO返回结果时，再通知 CPU进行处理

# 同步 IO模型的代码无法实现异步 IO模型
do_some_code()
f = open('/path/to/file', 'r')
f = f.read() # <== 线程停在此处等待 IO操作结果
# IO操作完成后线程才能继续执行
do_some_code(r)

# 异步 IO模型需要一个消息循环，在消息循环中，主线程不断地重复 "读取消息-处理消息"这一过程
loop = get_event_loop()
while True:
    event = loop.get_event()
    process_event(event)

# 消息模型很早就应用在桌面应用程序中了
# 一个 GUI程序的主线程就负责不停的读取消息并处理消息