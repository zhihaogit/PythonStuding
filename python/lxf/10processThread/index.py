# 多任务
# 单核 操作系统轮流让各个任务交替执行
# 多核 并行执行的多任务在多核cpu上实现，由于任务数量多于 cpu核心数量，操作系统也会把很多任务轮流调度到每个核心上


# 有个任务就是一个进程（process）
# 一个进程内部，需要同时运行多个子任务，即线程（thread）
# 一个进程至少有一个线程


# python都是执行单任务的进程，同时执行多个任务：
# 1. 多进程模式，启动多个进程，每个进程虽然只有一个线程，但多个线程可以一块执行多个任务
# 2. 多线程模式，启动一个进程，在一个进程中启动多个线程
# 3. 多进程 + 多线程模式，启动多个进程，每个进程启动多个线程