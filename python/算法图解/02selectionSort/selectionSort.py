# 选择排序
def findSmallest(arr):
    smallest = arr[0]
    smallestIndex = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallestIndex = i
    return smallestIndex

# 从小到大排序
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

myList = [9944, 222, 1341, 7654321, 3, 3, 4]
print (selectionSort(myList))

'''
O (n * 1/2 * n)
大 O表示法一般省略常数
简单表示为 O(n * n)
'''