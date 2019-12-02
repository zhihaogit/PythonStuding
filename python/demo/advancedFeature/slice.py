L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

r = []
n = 3
for i in range(n):
	r.append(L[i])

# slice方法
r = L[0: 3]
# 取 L list中的 0 ~ 3的值，左包右不包

r = L[-1:]
# 取 L中的最后一个元素

r = L[-2:]

r = L[-2: -1]

r = L[::2]
# 取 L中所有的数据，每2个取一个元素

r = L[:]
# 原样复制 L

print(r)


# tuple也是一种list，唯一区别是tuple不变，tuple也可以切片，只是操作结果仍是 tuple
t = (0, 1, 2, 3, 4, 5, 6)
tc = t[:3]
print (tc)


# 字符串也可以看做是一种list，每个元素就是一个字符
s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ap = s[0::3]
print (ap)
