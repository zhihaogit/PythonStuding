# 用 Python 写一个爬图片的程序
# from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup

link = input('type a link: ')
f = urllib.request.urlopen(link)
s = BeautifulSoup(f, 'html.parser')
images = s.find_all('img', pic_type = 0)
count = 1

def download(src):
    global count
    file_name = str(count) + '.jpg'
    content = urllib.request.urlopen(src).read()
    with open(file_name, 'wb') as f:
        f.write(content)
    count += 1

for image in images:
    download(image['src'])

