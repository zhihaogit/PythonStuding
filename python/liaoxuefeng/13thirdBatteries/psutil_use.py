# subprocess模块来获取系统运行状态
# psutil（process and system utilities）方便实现系统监控，跨平台使用

# 安装 psutil
# pip install psutil


# 获取 cpu信息
import psutil
# cpu逻辑数量
logicCount = psutil.cpu_count()
# cpu物理核心
phyCount = psutil.cpu_count(logical = False)
print (logicCount, phyCount)
# 8 4
# 4说明是 4核超线程，8说明是 8核非超线程

# 统计 cpu的用户/系统/空闲时间
cpuTime = psutil.cpu_times()
print (cpuTime)

# 实现类似 top命令的 cpu使用率，每秒刷新一次，累计 2次
for x in range(2):
    percent = psutil.cpu_percent(interval = 1, percpu = True)
    print (percent)

print ('------------------------------------------------------------------------------------')

# 获取内存信息
# 使用 psutil获取物理内存和交换内存信息
phyMemory = psutil.virtual_memory()
swapMemory = psutil.swap_memory()
print (phyMemory)
print (swapMemory)

print ('------------------------------------------------------------------------------------')

# 获取磁盘信息
# 获取磁盘分区、磁盘使用率和磁盘 IO信息
# 磁盘分区
diskPartitions = psutil.disk_partitions() # 磁盘分区信息
diskUsage = psutil.disk_usage('/') # 磁盘使用情况
diskIO = psutil.disk_io_counters() # 磁盘 IO
print (diskPartitions, diskUsage, diskIO, sep = '\n\n')
# 分区信息：[sdiskpart(device='/dev/disk1s1', mountpoint='/', fstype='apfs', opts='rw,local,rootfs,dovolfs,journaled,multilabel'), sdiskpart(device='/dev/disk1s4', mountpoint='/private/var/vm', fstype='apfs', opts='rw,noexec,local,dovolfs,dontbrowse,journaled,multilabel,noatime'), sdiskpart(device='/dev/disk2s2', mountpoint='/Volumes/InstallESD', fstype='hfs', opts='ro,nosuid,local,dovolfs,dontbrowse,multilabel'), sdiskpart(device='/dev/disk1s3', mountpoint='/Volumes/Recovery', fstype='apfs', opts='rw,local,dovolfs,dontbrowse,journaled,multilabel')]
# 文件格式是 apfs，opts中包含 rw可读写，journaled表示支持日志

print ('------------------------------------------------------------------------------------')

# 获取网络信息
# psutil可以获取网络接口和网络连接信息
# 获取网络读写字节/包的个数
netCounters = psutil.net_io_counters()
# 获取网络接口信息
netAddrs = psutil.net_if_addrs()
# 获取网络接口状态
netStats = psutil.net_if_stats()
print (netCounters, netAddrs, netStats, sep = '\n')

# 获取当前网络连接信息
# 需要 root权限
netConnect = psutil.net_connections()
print (netConnect)

print ('------------------------------------------------------------------------------------')

# 获取进程信息
# 所有进程 ID
psutil.pids()
# 获取指定进程的 id = xxxx
p = psutil.Process(3776)
# 进程的 name
p.name()
# 进程 exe路径
p.exe()
# 进程工作目录
p.cwd()
# 进程启动的命令行
p.cmdline()
# 父进程 ID
p.ppid()
# 父进程
p.parent()
# 子进程列表
p.children()
# 进程状态
p.status()
# 进程用户名
p.username()
# 进程创建时间
p.create_time()
# 进程终端
p.terminal()
# 进程使用的 cpu时间
p.cpu_times()
# 进程使用的内存
p.memory_info()
# 进程打开的文件
p.open_files()
# 进程相关网络连接
p.connections()
# 进程的线程数量
p.num_threads()
# 所有线程信息
p.threads()
# 进程环境变量
p.environ()
# 结束进程
p.terminate()


# psutil提供了 test()函数，模拟 ps命令的效果
psutil.test()
