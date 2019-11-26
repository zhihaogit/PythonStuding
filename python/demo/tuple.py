classmates = ('123', '456', '789')

print (classmates[-2])

tt = (1, 3)

# 定义一个元素的 tuple
tOne = (1, )
# python规定,  小括号进行计算
tTwo = (1)

print (tt, tOne, tTwo)

t = ('a', 'b', ['A', 'B'])
t[2][0] = 'x'
t[2][1] = 'y'

print (t)
