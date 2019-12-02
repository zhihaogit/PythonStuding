# 生成器
# 通过列表生成式，可以直接创建一个列表，但受内存限制，所以列表容量是有限的
# 在python中，一边循环一边计算的机制，称为生成器: generator
L = [x * x for x in range(10)]
print (L)

print ('-------------------------------------------------------------------')

# 第一种创建 generator的方法：把列表生成式的 []改为 ()
g = (x * x for x in range(10))
# next函数获得 generator的下一个返回值
# 没有更多的元素时，抛出 StopIteration错误
print (g, next(g), next(g))

print ('-------------------------------------------------------------------')

# 可以用 迭代的方法，拿到所有的元素
for n in g:
    print (n)

print ('-------------------------------------------------------------------')

# 菲波那切数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print (b)
        a, b = b, a + b
        n = n + 1
    return 'done'

print (fib(6))

print ('-------------------------------------------------------------------')

# 第二种创建 generator的方法：添加 yield关键字
def fibGenerator(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
# 函数是 顺序执行，遇到 return语句或者最后一行函数语句就返回
# 变成 generator函数，在每次调用 next()的时候执行，遇到 yield语句返回，再次执行时从上次返回的 yield语句处继续执行

print (fibGenerator(6))

print ('-------------------------------------------------------------------')

def odd():
    print ('step 1')
    yield 1
    print ('step 2')
    yield(3)
    print ('step 3')
    yield(5)
o = odd()
print (next(o), next(o), next(o))

print ('-------------------------------------------------------------------')

for n in fibGenerator(6):
    print (n)

print ('-------------------------------------------------------------------')

# for循环调用 generator时，无法拿到 generator的返回值，如果想要拿到返回值，必须捕获 StopIteration错误，返回值在 StopIteration的 value中
g = fibGenerator(6)

while True:
    try:
        x = next(g)
        print ('g:', x)
    except StopIteration as e:
        print ('Generator return value:', e.value)
        break

print ('-------------------------------------------------------------------')

# 杨辉三角
def triangles(max):
    L = [1]
    print (L)
    for i in range(1, max):
        L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1]
        yield L

for t in triangles(10):
    print(t)


















