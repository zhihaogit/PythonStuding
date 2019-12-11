# 内置的 os模块可以直接调用操作系统提供的接口函数
# 封装了操作系统的目录和文件操作，分散在 os和 os.path模块中
import os

osName = os.name
print (osName)
# 如果结果是 posix，说明系统是 linux、unix、mac os
# 如果是 nt,就是 window系统

os.uname()
# 获取更详细的系统信息，window不支持

# 环境变量
os.environ

# 获取某个环境变量的值
os.environ.get('PATH')


# 操作文件和目录的函数分别在 os和 os.path模块中
# 查看当前目录的绝对路径
ap = os.path.abspath('.')
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
ph = os.path.join(ap, 'testdir')
# 然后创建一个目录
os.mkdir(ph)
# 删除一个目录
os.rmdir(ph)

# 合成，拆分路径只对字符串操作，并不要目录或文件真实存在
# 合成路径用
os.path.join('path1', 'path2')
# 拆分路径，拆成两部分，后一部分总是最后级别的目录或文件名
os.path.split('path1/path2')
# 直接获取文件拓展名
os.path.splittext('path1/path2/abc.txt')

# 对文件重命名
os.rename('abc.txt', 'newAbc.txt')

# 删除文件
os.remove('newAbc.txt')

# os中没有复制文件的操作
# 1. 可通过读写文件进行文件复制
# 2. shutil模块提供了 copyfile方法，shutil算是 os的补充

# 过滤文件
[x for x in os.listdir('.') if os.path.isdir(x)]

# 列出 .py文件
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splittext(x)[1] == '.py']

