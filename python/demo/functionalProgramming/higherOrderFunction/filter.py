# filter
# filter()的作用是从一个序列中筛出符合条件的元素
# 由于 filter()使用了惰性计算，所以只有在取 filter()结果的时候，才会真正筛选并每次返回下一次晒出的元素
def is_odd(n):
    return n % 2 == 1

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res = list(filter(is_odd, l))

print (res)