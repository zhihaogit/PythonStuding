# 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来
import os, re

commentLines = 0
whiteLines = 0
comment = False

path = '/path'

count = 0

def tree(path):
    filelist = os.listdir(path)
    for file in filelist:
        if os.path.isdir(os.path.join(path, file)):
            tree(os.path.join(path, file))
        else:
            filename = os.path.basename(os.path.join(path, file))
            if filename.endswith('.py'):
                with open(os.path.join(path, file)) as f:
                    parse(f)

def parse(f):
    global commentLines
    global whiteLines
    global comment
    for line in f.readlines():
        if line.startswith('#'):
            commentLines += 1
        elif re.match("^[\\s&&[^\\n]]*$", line):
            whiteLines += 1

tree(path)

print (commentLines, whiteLines)