list = ['l', 'i', 's', 't']
tinyList = ['123', '456']

# 加号是列表连接运算符，星号是重复操作
print list # 输出完整列表 ['l', 'i', 's', 't']
print list[0] # 输出列表的第一个元素 'l'
print list[1: 3] # 输出第二个至第三个元素 ['i', 's']
print list[2:] # 输出从第三个开始至列表末尾的所有元素 ['s', 't']
print tinyList * 2 # 输出列表两次 ['123', '456', '123', '456']
print list + tinyList # 打印组合的列表 ['l', 'i', 's', 't', '123', '456']
