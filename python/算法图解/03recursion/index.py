# 递归
def countdown(i):
    print (i)
    if i <= 0: # 基准条件（base case）-> 函数不再自我调用，从而避免无限循环
        return
    else: # 递归条件（recursive case）-> 函数进行自我调用
        countdown(i - 1)

# 栈
# 调用栈（call stack）
# 压入 & 弹出

# 在一个函数中 调用另一个函数时，当前函数暂停并处于未完成状态。该函数的所有变量的值都还在内存中
def greet(name):
    print ('hello, ' + name + '!')
    greet2(name)
    print ('getting ready to say bye...')
    bye()

def greet2(name):
    print ('how are you, ' + name + '?')

def bye():
    print ('ok bye!')

# greet('haha')


# 递归调用栈
def fact(x):
    if x == 1:
        return 1
    else:
        return x + fact(x - 1)

print (fact(10))

'''
递归指的是调用自己的函数
每个递归函数都有两个条件，基线条件和 递归条件
栈有两种操作：压入和弹出
所有函数调用都进入调用栈
调用栈可能很长，这将占用大量的内存
'''
