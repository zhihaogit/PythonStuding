# 读写是常见的 I/O操作
computerName = input('input your computer name: ')
src = '/Users/{}/StudingNotes/python/liaoxuefeng/09IO/test.py'.format(computerName)

# 读文件
f = open(src, 'r')
# 如果不存在会抛出 IOError
# 如果打开成功
f.read()
# 最后关闭文件使用
f.close()

try:
    # 只读模式
    f = open(src, 'r')
    content = f.read()
    # print (content)
finally:
    if f:
        f.close()

# with语句自动调用 close()方法
with open(src, 'r') as f:
    content = f.read()
    # print (content)

# read() 会一次性读取文件的全部内容，适合小文件
# read(size) 每次最多读取 size个字节的内容，适合大文件
# readline() 每次读取一行内容
# readlines() 一次读取所有内容并按行返回 list，适合读取配置文件


# file-like Object
# 像 open()函数返回的这种有个 read()方法的对象，叫做 file-like Object

# StringIO就是在内存中创建的 file-like Object，常用作临时缓冲

# 二进制文件
# rb模式打开文件，读取的是二进制文件
f = open(src, 'rb')
content = f.read()
# print (content)

# 字符编码
# 读取非 UTF-8的文件，需要在 open函数中传入 encoding参数
f = open(src, 'r', encoding = 'gbk', errors = 'ignore')
content = f.read()
# print (content)


# 写文件
# 调用 open()方法，传入标识符 w或 wb表示写文本文件或写二进制文件
f = open(src, 'w')
f.write('Hello Wolrd!')
f.close()
# 写入的时候，只有调用 close()方法，操作系统才会保证把没有写入的数据全部写入磁盘
# 没有调用 close()方法可能只写了一部分到磁盘，剩下的丢失了
# 使用 with语句
with open(src, 'w') as f:
    f.write('hghghghg')
# encoding参数将字符串自动转换为指定编码
# 文件已存在将直接覆盖内容

# 传入 'a'，表示 append模式写入











