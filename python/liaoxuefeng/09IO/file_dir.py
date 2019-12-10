# 内置的 os模块可以直接调用操作系统提供的接口函数
import os

osName = os.name
print (osName)
# 如果结果是 posix，说明系统是 linux、unix、mac os
# 如果是 nt,就是 window系统