'''
快速排序
比 选择排序快得多
使用了 D&C

1. 先从数组中选择一个元素，这个元素叫做 基准值（pivot）
2. 再找出比基准值小的元素，以及比基准值大的元素，这称为 分区（partitioning）
3. 对分成的两个子数组进行快速排序

快速排序的独特之处在于，其速度取决于选择的基准值
平均情况下，运行时间是 O(n log n)
'''
myList = [98765, 2345, 543, 999999, 435764, 43234, 12345, 3]

def quicksort(list):
    if len(list) <= 1:
        return list
    else:
        # 这是最糟的情况，栈长为 O(n)
        # 每次基准值是 第一个，数组没有被分为两半，其中一个数组始终为空，这导致调用栈非常长
        # 每层需要的时间是 O(n)，所以是 O(n * n)
        pivot = list[0]
        otherList = list[1: ]
        less = [i for i in otherList if i <= pivot]
        greater = [i for i in otherList if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

print (quicksort(myList))

def finalQuicksort(list):
    if len(list) <= 1:
        return list
    else:
        # 这是佳的情况，栈长为 O(log n)
        # 每层需要的时间是 O(n)，所以是 O(n log n)
        pivot = list[len(list) // 2]
        less = [i for i in list if i < pivot]
        greater = [i for i in list if i > pivot]
        return finalQuicksort(less) + [pivot] + finalQuicksort(greater)

print (finalQuicksort(myList))


'''
合并排序（merge sort）
运行时间是 O(n log n)
最糟情况下是 O(n * n)

实现快速排序，随机地选择用作基准值的元素
'''