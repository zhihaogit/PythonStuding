# 元组用 ()标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表
tuple = ('t', 'u', 'p', 'l', 'e')
tinyTuple = (123, 456)

print tuple # 输出完整元组 ('t', 'u', 'p', 'l', 'e')
print tuple[0] # 输出元组的第一个元素 ‘t
print tuple[1: 3] # 输出第二个至第四个（不包含）的元素 ('u', 'p')
print tuple[2: ] # 输出从第三个开始至列表末尾的所有元素 ('p', 'l', 'e')
print tinyTuple * 2 # 输出元组两次 (123, 456, 123, 456)
print tuple + tinyTuple # 打印组合的元组 ('t', 'u', 'p', 'l', 'e', 123, 456)

# 元组不允许更新，列表允许更新