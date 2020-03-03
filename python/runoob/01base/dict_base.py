# 字典(dictionary)是除列表之外 python之中最灵活的内置数据结构类型
# 列表是有序的对象集合，字典是无序的对象集合
# 两者的区别是：字典当中的元素是通过键来存取，而不是通过偏移存取

dict = {}
dict['one'] = 'This is one'
dict[2] = 'This is two'

tinyDict = {
    'name': 'john',
    'code': 6734,
    'dept': 'sales'
}

print dict['one'] # 输出键为 'one'的值    'This is one'
print dict[2] # 输出键为 2的值    'This is two'
print tinyDict # 输出完整的字典    {'dept': 'sales', 'code': 6734, 'name': 'john'}
print tinyDict.keys() # 输出所有键   ['dept', 'code', 'name']
print tinyDict.values() # 输出所有值     ['sales', 6734, 'john']