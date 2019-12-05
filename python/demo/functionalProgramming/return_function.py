# 函数作为返回值
# 高阶函数除了可以接受函数作为参数，还可以把函数作为结果返回
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

tupleArg = (1, 3, 5, 7, 9)
f = lazy_sum(*tupleArg)
print (f())

# 每次调用都会返回一个新的函数，即使传入的参数相同
f2 = lazy_sum(*tupleArg)
print (f == f2)


# 闭包
# 返回的函数在其定义内部引用了局部变量，所以当一个函数返回了一个函数后，其内部的局部变量还被新函数引用
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print (f1(), f2(), f3())

# 注意：返回函数不要引用任何循环变量，或者后续会发生变化的变量
def count2():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f4, f5, f6 = count2()
print (f4(), f5(), f6())

'''
一个函数可以返回一个计算结果，也可以返回一个函数
返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量
'''

def count3():
    def f(j):
        return lambda : j * j
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f7, f8, f9 = count3()
print (f7(), f8(), f9(), 'count3')

def createCounter():
    def plus():
        n = 0
        while True:
            n = n + 1
            yield n

    x = plus()

    def counter():
        return next(x)
    return counter

def createCounter2():
    s = [0]

    def counter():
        s[0] += 1
        return s[0]
    return counter


counterA = createCounter()
counterB = createCounter2()

print(counterA(), counterA(), counterA(), counterA(), counterA())
print(counterB(), counterB(), counterB(), counterB(), counterB())




















