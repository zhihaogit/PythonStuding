# 列表生成式
# 列表生成式，快速生成 list，可以通过一个 list推导另一个 list
L = list(range(1, 11))

L = []
for x in range(1, 11):
    L.append(x * x)

# 列表生成式用一行语句代替循环生成上面的list
L = [x * x for x in range(1, 11)]

# 使用条件判断，筛选出仅有偶数的平方
L = [x * x for x in range(1, 11) if x % 2 == 0]

# 使用两层循环，可以全排列
L = [m + n for m in 'ABC' for n in 'XYZ']

# 列出当前目录下的所有文件和目录名
import os
L = [d for d in os.listdir('.')]

# for循环可以使用两个甚至多个变量
d = {
    'x': 'A',
    'y': 'B',
    'z': 'C'
}


for k, v in d.items():
    print(k, v)

L = ['{}={}'.format(k, v) for k, v in d.items()]

LArr = ['Hello', 'World', 'IBM', 'Apple']

L = [v.lower() for v in LArr]

print(L)

LArrCopy = [12, 'Hello', 'World', 18, 'IBM', 'Apple']

LResult = [v.lower() for v in LArrCopy if isinstance(v, str)]

print(LResult)
