# 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」
import random, sys, os
basePath = sys.path[0]
path = os.path.join(basePath, 'words.txt')

with open(path, 'r') as f:
    list = []
    for word in f.readlines():
        list.append(word.strip('\n'))
    print (list)

def isValid(myStr):
    result = myStr
    for x in list:
        if result.find(x) != -1:
            result = result.replace(x, '**')
        return result

myStr = input('Please input a string: ')
print (isValid(myStr))
