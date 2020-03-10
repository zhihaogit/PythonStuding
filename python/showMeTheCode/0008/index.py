# 一个HTML文件，找出里面的正文
import requests
from bs4 import BeautifulSoup

def get_content(content):
    soup = BeautifulSoup(content, features='lxml')
    return (soup.get_text().strip('\n'))

if __name__ == '__main__':
    r = requests.ge('https://github.com/')
    html = r.text
    content = get_content(html)
    print (content)