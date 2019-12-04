# 高阶函数 -> Higher-order function
# 变量可以指向函数
f = abs
result = f(-10) == abs(-10)
print (result)

# 函数名也是变量
# abs = 10
# abs(-10)
'''
Traceback (most recent call last):
  File "functionalProgramming/higherOrderFunction/index.py", line 9, in <module>
    abs(-10)
TypeError: 'int' object is not callable
'''

# 传入函数
# 一个函数接收另一个函数作为参数，这种函数称之为高阶函数
# 函数式就是指这种高度抽象的编程范式
def add(x, y, f):
    return f(x) + f(y)

result2 = add(-10, -9, abs)
print (result2)

# 编写高阶函数，就是让函数的参数能够接收别的函数