# 二分查找
def binary_search(list, item):
    low = 0
    high = len(list) - 1
    count = 0

    while low <= high:
        count += 1
        mid = (low + high) // 2 # 向下取整
        guess = list[mid]
        if guess == item:
            return [mid, count]
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None

myList = [1, 3, 5, 7, 9]
list128 = list(range(0, 128))

print (binary_search(myList, 5))
print (binary_search(myList, -1))
print (binary_search(list128, 127))

'''
简单查找逐个地检查数字，如果列表包含 100个数字，最多需要猜 100次。
最多需要猜测的次数与列表长度相同，这就被称为 线性时间（linear time） -> O(n)
二分查找的运行时间为 对数时间（或 log时间） -> O(log n)
'''
