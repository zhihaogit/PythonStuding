# 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights
import random, sys, os
basePath = sys.path[0]
path = os.path.join(basePath, 'words.txt')

with open(path, 'r') as f:
    list = []
    for word in f.readlines():
        list.append(word.strip('\n'))
    print (list)

def isValid(word):
    for x in list:
        return False if word == x else True

myword = input('Please input a word: ')
if isValid(myword):
    print ('Human Rights')
else:
    print ('Freedom')
