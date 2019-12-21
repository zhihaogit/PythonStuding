# itertools模块提供了用于操作迭代对象的函数
import itertools

# 创建 “无限”迭代器
# count()会创建一个无限的迭代器，所以会打印出自然数序列
natuals = itertools.count(1)
# for n in natuals:
#     print (n)


# cycle()会把传入的一个序列无限重复下去
cs = itertools.cycle('ABC')
# for c in cs:
#     print (c)


# repeat()负责把一个元素无限重复下去，可以提供第二个参数限定重复次数
ns = itertools.repeat('ABC', 3)
for n in ns:
    print (n)


# 无限序列只有在 for迭代时才会无限的迭代下去，只是创建一个迭代对象，不会先把无限个元素生成出来
# takewhile() 函数会根据判断条件来截取一个有限的序列
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x : x <= 10, natuals)
nsl = list (ns)
print (nsl)


# chain()把一组迭代对象串联起来，形成更大的迭代器
for c in itertools.chain('ABC', 'XYZ'):
    print (c)


# groupby()把迭代器中相邻的重复元素跳出来放一起
for key, group in itertools.groupby('ABAABBBCCCAAA'):
    print (key, list(group))

print ('---------------------------------------------------------------------------------------')
# 挑选规则是通过函数完成的，只要作用于函数的两个元素的返回值相等，这两个元素就被认为在一组，而函数返回值作为组的 key
# 忽略大小写
for key,group in itertools.groupby('AaaBBbcCAAa', lambda c : c.upper()):
    print (key, list(group))