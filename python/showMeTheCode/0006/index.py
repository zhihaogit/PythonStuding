# 有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词
import os, re, sys

basePath = sys.path[0]

path = os.path.join(basePath, 'diaries')
files = os.listdir(path)

def pathHandler(f):
    return os.path.join(path, f);

def wordsHandler(words):
    dica = {}
    num = 0
    key = ''
    for w in words:
        if w in dica:
            dica[w] = dica[w] + 1
        else:
            dica[w] = 1
    for k, v in dica.items():
        if dica[k] > num:
            num = dica[k]
            key = k
    print(key, num)

for f in files:
    with open(pathHandler(f)) as d:
        words = re.findall("[a-zA-Z]+'*-*[a-zA-Z]*", d.read())
        wordsHandler(words)