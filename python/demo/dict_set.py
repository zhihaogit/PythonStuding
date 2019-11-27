'''
dict -> 字典类型
key -> value形式
'''
names = ['123', '456', '789']
scores = [90, 91, 92]
d = {}

for index, item in enumerate(names):
	d[item] = scores[index]

d['13'] = 99
d.pop('123')
print (d, d.get('11', 98))

'''
set ->
一组 key的集合，不存储 value
'''
s = set(names)

s.add('909')
s.remove('123')
names.sort()

print (s, names)

# 传入一个 tuple
t = ('123', '123', '456', '789')
st = set(t)
print (st)

# 不接受可变对象
stl = ('123', '123', '456', ['789', '999'])

print (stl)
