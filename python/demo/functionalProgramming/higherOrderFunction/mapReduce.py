# map(function, Iterable)
def f(x):
    return x * x

listArr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

r = map(f, listArr)
l = list(r)
# list() 方法用于将元组转换为列表
print (l)

s = map(str, listArr)
print (list(s))


# reduce(function, Iterable)
from functools import reduce
def add(x, y):
    return x + y

result = reduce(add, listArr)
# 内建函数 sum求和

def num2Str(x, y):
    return x * 10 + y
    # return '{}{}'.format(x, y)
result = reduce(num2Str, listArr)

print (result)
