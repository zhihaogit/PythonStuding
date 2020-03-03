# 字符串列表有 2种取值顺序
# 从左到右索引默认 0开始的，最大范围是字符串长度少 1
# 从右到左索引默认 -1开始的，最大范围是字符串开头

# 可以使用 [头索引 : 尾索引]来截取相应的字符串，左闭右开
s = 'abcdefg'
print s[1: 4]
# 'bcd'

# 加号是字符串连接运算符，星号是重复操作
str = 'Hello World!'

print str # 输出完整字符串 'Hello World!'
print str[0] # 输出字符串中的第一个字符 'H'
print str[2: 5] # 输出字符串中第三个至第六个之间的字符串 'llo'
print str[2:] # 输出从第三个字符开始的字符串 'llo World!'
print str * 2 # 输出字符串两次 'Hello World!Hello World!'
print str + 'TEST' # 输出连接的字符串 'Hello Wolrd!TEST'

# python 列表截取可以介绍第三个参数，表示截取的步长
print str[1: 4: 2]
# 'el'