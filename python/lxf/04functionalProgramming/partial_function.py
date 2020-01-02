# functools中有一个是 偏函数(partial function)
# 这里的偏函数与数学意义的偏函数不一样

# int函数可以把字符串转换为整数
s = '12345'
str2Int = int(s)

str2Int = int(s, base = 8)

str2Int = int(s, 16)

def int2(x, base = 2):
    return int(x, base)

s2 = '10000000'
str2Int = int2(s2)

print (str2Int)


'''
functools.partial的作用是
把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数
创建偏函数时，实际上可以接收函数对象、*args和 **kw这3个参数
'''

import functools
int3 = functools.partial(int, base = 2)
int4 = functools.partial(int, base = 10)

str2Int = int3(s2)
str2Int = int4(s2)

print (str2Int)
