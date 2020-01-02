# coding=utf-8

# i=10
# print(i)

# i = True
# if i:
#     print("True")
# else:
#     print("False")
#
# total = 'tem_one' + \
#         'tem_two' + \
#         'item_three'
# print(total)

# money = 99.9
# count = 5
# person = '小明'
# print(money, type(money))
# money = '9.9哈'
# print(money, type(money))
# money = 11
# print(money, type(money))
# print('AA', 'BB\n', '\tCC', sep='$', end='')
# print('ass')

# r -> raw, 原样输出字符串，忽略转义字符
# print(r'hello\py\thon')

# 大写的变量名约定为 常量
# NAME = '123'
# print(NAME)

# message = '''
# email:
#     123
#         456
#             789
#         456
#     123
# '''
# print(message)
'''
三引号作用：
    1. 保留格式化的字符串
    2. 未向变量赋值，多行注释作用
'''

# 格式化输出字符串

# 1. 使用占位符
# %s --> str()  强制类型转换，转成 string
# %d --> digit 数字，强制转成 init
# %f --> float 浮点型，可指定小数点后面的位数，是四舍五入的值
# name = 'haha'
# gender = 'female'
# age = 14
# print('name:' + name + ',gender:' + gender + ',age:' + 14) # TypeError
# print('name:%s,gender:%s,age:%s' % (name, gender, age))
# print('age%s' % age)
# print('age' + str(age))
# salary = 8899.99
# print('my salary is %.3f' % salary)
# title = 'hahaha'
# price = 123.5
# count = 20
# total = price * count
# message = '''
# title:%s
# price:%.0f
# count:%d
# total:%.2f
# ''' % (title, price, count, total)
# print(message)
# 2. format函数
# title = 'hahaha'
# price = 123.5
# count = 20
# total = price * count
# message = 'title:{},price:{},count:{},total:{}'.format(title, price, count, total)
# print(message)

# input()
# print('''
# *********************
#         hahaha
# *********************
# ''')
# username = input('username:')
# password = input('password:')
# print('%s pay the money' % username)
# money = input('money:')
# money = int(money)
# message = '{}Successfully, total is {}'.format(username, money)
# # print('$sSuccessfully, total is %d' %(username, money2))
# print(message)

# id() 取存在内存中的值得 id
# a = 1
# b = a
# print(id(a), id(a) == id(b), a, b)

# 拓展运算符
# += -= *= /=
# c = '1'
# c += '2'
# print(c)

# 算数运算符
# + - * /
# 与字符串相乘，表示重复前面的字符串多少次
# print('*' * 20)

# 拓展运算符
# ** // %
# a = 9
# b = 4
# c = a ** b  # a的 b次方
# d = a // b  # 取整
# e = a % b   # 取余
# print(c, d, e)

# 关系运算符
# > < >= <= == !=

# 小整数运算池
# Python对小整数的定义是[-5,257]这些整数对象是提前建立好的,不会被垃圾回收,在一个Python的程序中,所有位于这个范围内的整数使用的都是同一个对象
# 大整数对象池
# 每一个大整数,均创建了一个对象

# 身份运算符
# is 是判断两个标识符是不是引用自一个对象
# is
# is not
# a = 60000
# b = 60001
# print (a is not b)

# 逻辑运算符
# and
# or
# not
# flag = True and False
# flag1 = True or False
# flag2 = not True
# print(flag, flag1, flag2)

# 转 二进制
# print(bin(12))
# 转 十进制
# print(int(0b101001))

# 反码：二进制取反，再加一

# 位运算
'''
&   与
|   或
~   非
^   异或
    二进制的两个数，相对应的位置，相同为0，不同为1
    最后得到的二进制数再转为 十进制
<<  左移
    二进制的数值，向左移动n位，最右侧补充n位 0
    m << n, m * 2的 n次方
>>  右移
    二进制的数值，向右移动n位，最左侧补充n位 0
    m >> n, m / 2的 n次方，取整，简写 m // 2的 n次方
'''
# print(bin(2), bin(3), 2 & 3, 2 | 3, ~2, 2 ^ 3, 2 << 3, 36 >> 4, 36 // (2 * 2 * 2 * 2))

# 三目运算符
# a = 5
# b = 6
# result = a + b if (a > b) else a - b
# print(result)

# 条件判断语句
# username = ''
#
# if not username:
#     print (123)
# else:
#     print (456)

# 引入 随机模块，randint 随机生成一个指定范围的int
# import random
# theNumber = random.randint(1, 10)
#
# print (theNumber)

# 多层条件判断
# usernameInput = input('input a number')
#
# if usernameInput:
#     print (1)
# elif not usernameInput:
#     print (2)
# elif usernameInput == '12':
#     print (3)
# else:
#     print (4)

# for循环
# for ... in ...
# range(m, n) # 生成 m ~ n-1的序列
# for i in range(8, 8):
#     print(i)

# name = 'hahaha'
# for i in range(8):
#     print ('{}很饿，正在吃第{}馒头'.format(name, i + 1))
# print ('{}终于吃饱了'.format(name))

# for i in range(8):
#     print ('{}很饿，正在吃第{}馒头'.format(name, i + 1)) if (i != 4) else print ('{}很饿，但是却扔掉了第{}馒头'.format(name, i + 1))

# for ... else ...
# 适用于 for执行完或者没有循环数据时，需要做的事
# pass 空语句，占位使用，防止语法报错

# name = 'hahaha'
# for i in range(8):
#     print ('{}很饿，正在吃第{}馒头'.format(name, i + 1))
# else:
#     print ('{}说没有馒头了，还没有吃饱'.format(name))
#
# for i in range(8):
#     pass
# else:
#     print ('{}终于吃饱了'.format(name))
#
# for i in range(12):
#     print ('hahaha')
# else:
#     pass

for i in range(3):
    username = input('username:')
    password = input('password:')

    if username == '123' and password == '123':
        print ('successfully')
        print ('hahaha')
        break
    else:
        print ('login fail')
else:
    print ('lock user')












