# 排序算法
l = [36, 5, -12, 9, 21]
s1 = sorted(l)

# 第二个参数
# sorted是高阶函数，接收一个 key函数来实现自定义的排序
s2 = sorted(l, key = abs)

# print (s1, s2)

l2 = ['bob', 'about', 'zoo', 'Credit']
s3 = sorted(l2)

# 第三个参数
# reverse=True，可反向排序
def noop(element):
    return element

s4 = sorted(l2, key = noop, reverse = True)

# print (s3, s4)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def handler(element, index = 0):
    return element[index]

s5 = sorted(L, key = handler, reverse = False)

print (s5)