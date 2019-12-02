# for...in...

# dict 迭代
d = {
    'a': 1,
    'b': 2,
    'c': 3
}

for key in d:
    print (key)	
# 因为 dict的存储不是按照 list的方式顺序排列，所以迭代出的结果顺序可能不同

for value in d.values():
    print (value)
# 迭代 value

for entries in d.items():
    print (entries[0], entries[1])
# 同时迭代 key和 value
print ('-------------------------------------')

# 迭代字符串
for ch in 'ABC':
    print (ch)

print ('-------------------------------------')

# 判断一个对象是否是可迭代对象
from collections.abc import Iterable
isBooleanString = isinstance('abc', Iterable)
isBooleanList = isinstance([1, 2, 3], Iterable)
isBooleanTuple = isinstance((1, 2, 3), Iterable)
isBooleanNumber = isinstance(123, Iterable)

print (isBooleanString, isBooleanList, isBooleanTuple, isBooleanNumber)

print ('-------------------------------------')

# 对 list实现下标循环
# enumerate函数会把一个 list变成索引-元素对，可以同时迭代索引和元素本身
for index, value in enumerate([1, '2', '3', '4', '5']):
    print (index, value)

print ('-------------------------------------')

# 同时引用两个变量
for x, y in [(1, 1), (2, 2), (3, 3), (9, 2)]:
    print (x, y)

print ('-------------------------------------')

# 冒泡排序
def sortByLocation(listArr = []):
    arrLength = len(listArr)
    for i in range(arrLength):
        for j in range(0, arrLength - i - 1):
            if listArr[j] > listArr[j + 1]:
                listArr[j], listArr[j + 1] = listArr[j + 1], listArr[i]
    return listArr

def getMaxValue(listArr):
    arrLength = len(listArr)
    return listArr[arrLength - 1]

sortResult = getMaxValue(sortByLocation([1, 2, 4,2, 4, 5]))
print ('max value is {}'.format(sortResult))

