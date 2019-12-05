# 匿名函数
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lFormat = list(map(lambda x : x * x, l))

'''
关键字 lambda表示匿名函数，冒号前面是函数参数
只能有一个表达式，不用写 return，返回值是该表达式的结果
可以将匿名函数赋值给一个变量，再利用变量调用
'''

f = lambda x : x * x
print (lFormat)

def build(x, y):
    return lambda: x * x + y * y

print (build(2, 5)())

def is_odd(n):
    return n % 2 == 1

is_odd2 = lambda n : n % 2 == 1

L = list(filter(is_odd2, range(1, 20)))
print (L)