'''
散列表（hash table）
也被称为散列映射、映射、字典和关联数组
散列表是一种包含额外逻辑的数据结构
数组和链表都被直接映射到内存，散列表使用散列函数来确定元素的存储位置

散列函数
1. 必须是一致的，每次取同一个 key都返回相同的值
2. 应该将不同的输入映射到不同的数字

python提供 dict来实现散列表
'''
# 用作查找
phoneBook = dict()
phoneBook['jenny'] = 987654
phoneBook['tom'] = 98762354
print (phoneBook['jenny'])

# 防止重复
voted = {}
def checkVoter(name):
    if voted.get(name):
        print ('kick them out!')
    else:
        voted[name] = True
        print ('let them vote!')

checkVoter('tom')
checkVoter('mike')
checkVoter('tom')

# 用作缓存
def getDataFromServer(url):
    return 'whatever'

cache = {}
def getPage(url):
    if cache.get(url):
        return cache[url]
    else:
        data = getDataFromServer(url)
        cache[url] = data
        return data
