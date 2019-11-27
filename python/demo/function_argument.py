import sys

# 位置参数
'''
def power(x):
	return x * x

def power(x, n):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s
'''

# 默认参数
def power(x, n = 2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s
print (power(13))

# 默认参数必须指向不变参数
'''
def add_end(L = []):
	L.append('End')
	return L
'''

def add_end(L = None):
	if L is None:
		L = []
	L.append('END')
	return L
add_end()
print (add_end())

# 可变参数
# 可变参数是指 传入的参数个数是可变的，可以是任意个
# 仅需在参数前面加一个 *号，参数接收到的是一个 tuple
# 可变参数在函数调用时自动组装为一个 tuple
'''
def calc(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
'''

def calc(*numbers):
	sum = 0
	for n in numbers: 
		sum = sum + n * n
	return sum

print (calc(1, 2, 3))
numberList = [1, 2, 3]
# 在list或 tuple前面加一个 *号，把 list或 tuple的元素变成可变参数传进去
print (calc(*numberList))

# 关键字参数
# 关键字参数在函数调用时自动组装为一个 dict
def person(name, age, **kw):
	print ('name:', name, 'age:', age, 'other:', kw)
person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, other={'gender': 'male', 'job': 'Engineer'})
extra = {
	'city': 'Beijing',
	'job': 'EE'
}
# **extra表示这个dict的所有key value用关键字参数传入到函数的 **kw参数，kw将获得一个 dict
# 注意：kw获得的 dict是 extra的一份拷贝，对 kw的改动不会影响到函数外的 extra
person('Jack', 24, **extra)

# 命名关键字
# 要限制关键字参数的名字，就可以用命名关键字参数
# 命名关键字需要一个特殊分隔符 *，*后面的参数被视为命名关键字参数
def personKey(name, age, *, city, job):
	# 缺少 *的话，city和 job会被当做位置参数
	print (name, age, city, job)

# personKey('Jack', 24, city = 'Beijing', job = 'Engineer', a = 'test')
personKey('Jack', 24, city = 'Beijing', job = 'Engineer')
# 如果函数定义中已有一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符 *了
def personKey2(name, age, *args, city, job):
	print (name, age, city, job, args)

personKey2('Jack', 25, city='Shanghai', job='fiance')
personKey2('Jerry', 26, 1, 2, 3, city = 'Beijing', job = 'Engineer')

# 参数组合
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字和关键字参数
def f1(a, b, c = 0, *args, **kw):
	print ('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)

def f2(a, b, c = 0, *, d, **kw):
	print ('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw, sep=' ')
	# sys.stdout.write ('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw, sep=' ')

f1(1, 2)
f1(1, 2, c = 3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x = 99)
f1(1, 2, d = 99, ext = None)
f2(1, 2, d = 99, ext = None)

args = (1, 2, 3, 4)
args2 = (1, 2, 3)
kw = {
	'd': 99,
	'x': '#'
}
f1(*args, **kw)
f1(*args2, **kw)
f2(*args2, **kw)

# 参数组合多达 5种，不要同时使用太多的组合，否则函数接口的可理解性会变差














