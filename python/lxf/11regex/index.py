# 正则表达式
'''
\d 匹配一个数字
\w 匹配一个字母或数字
. 匹配任意字符
* 表示任意长的字符（包括 0个）
+ 表示至少一个字符
? 表示 0或 1个字符
{n} 表示 n个字符
{n, m} 表示 n-m个字符
'''

'''
[] 表示范围
A|B 匹配 A或 B
^ 表示行的开头
    ^\d 表示必须以数字开头
$ 表示行的结束
    \d$ 表示必须以数字结束
'''


# python中的 re模块
# 会被转义
s = 'ABC\\-001'
s1 = r'ABC\\-001'

print (s, s1)

import re
result = re.match(r'^\d{3}\-\d{3, 8}$', '010-12345')
result1 = re.match(r'^\d{3}\-\d{3, 8}$', '010 12345')
print (result, result1)

# 常见判断方式
test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print ('ok')
else:
    print ('failed')


# 切分字符串
originStr = 'a b c   d'
originStr.split(' ')
re.split(r'\s+', originStr)
originStr1 = 'a,b, c   d'
re.split(r'[\s\,]+', originStr1)
originStr2 = 'a,b;; c   d'
re.split(r'[\s\,\;]+', originStr2)


# 分组匹配
# () 表示要提取的分组（Group）
# 提取区号和本地号码
rs = r'^(\d{3})-(\d{3,8})$'
m = re.match(rs, '010-12345')
print (m.group(0))
# 010-12345
print (m.group(1))
# 010
print (m.group(2))
# 12345
# 识别合法的时间
rs = r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$'
t = '19:05:03'
m = re.match(rs, t)
print (m.group(0))


# 贪婪匹配
# 正则匹配默认是 贪婪匹配，尽可能多的匹配字符


# 编译
# re模块内部处理
# 1. 编译正则表达式
# 2. 用编译后的正则表达式去匹配字符串

# 手动预编译
import re

re_telephont = re.compile(rs)
print (re_telephont)









