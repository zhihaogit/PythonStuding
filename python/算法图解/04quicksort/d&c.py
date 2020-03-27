# 分而治之（divide and conquer, D&C）一种著名的递归式问题解决方案

# 递归相加数组中的元素
def recursionSum(list):
    return 0 if len(list) == 0 else list.pop() + recursionSum(list)

myList = [1, 2, 3, 4, 5, 6]
print (recursionSum(myList))

# D&C将问题逐步分解，使用 D&C处理列表，基线条件很可能是空数组或只包含一个元素的数组
