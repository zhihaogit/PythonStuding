# 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
import random, string

stringSelect = string.ascii_letters + '0123456789'
# string.ascii_letters 生成字母表

def generateString(count = 200, length = 20):
    result = []
    for x in range(count):
        re = ''
        for y in range(length):
            re += random.choice(stringSelect)
            # random.choice(values) 从 values随机提取一个元素
        result.append(re)
    return result

if __name__ == '__main__':
    result = generateString(200, 20)
    print (result)