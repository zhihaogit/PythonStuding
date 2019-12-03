# 迭代器
'''
凡是可作用于 for循环的对象都是 Iterable类型
凡是可作用于 next()函数的对象都是 Iterator类型，它们表示一个惰性计算序列
集合数据类型如 list、dict、str等是 Iterable但不是 Iterator，不过可以通过 iter()来获得一个 Iterator对象
Python的 for循环本质就是通过不断调用 next()函数实现的
'''

# 判断是不是 Iterable对象
from collections.abc import Iterable
b1 = isinstance([], Iterable)
b2 = isinstance({}, Iterable)
b3 = isinstance('abc', Iterable)
b4 = isinstance([x for x in range(10)], Iterable)
b5 = isinstance(100, Iterable)

print (b1, b2, b3, b4, b5)

# 判断是不是 Iterator对象
from collections.abc import Iterator
b6 = isinstance((x for x in range(10)), Iterator)
b7 = isinstance([], Iterator)
b8 = isinstance({}, Iterator)
b9 = isinstance('abc', Iterator)

print (b6, b7, b8, b9)

# 使用 iter()函数
b10 = isinstance(iter([]), Iterator)
b11 = isinstance(iter('abc'), Iterator)

print (b10, b11)