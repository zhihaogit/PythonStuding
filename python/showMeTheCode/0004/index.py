# 任一个英文的纯文本文件，统计其中的单词出现的个数
import os, re, sys

baseDir = sys.path[0]
path  = os.path.join(baseDir, 'text.txt')
count = 0
with open(path, 'r') as file:
    for line in file.readlines():
        list = re.findall("[a-zA-z]+'*-*[a-zA-Z]", line)
        count += len(list)
print(count)